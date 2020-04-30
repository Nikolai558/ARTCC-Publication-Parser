import tkinter as tk
import os
from sys import exit
import xml.etree.ElementTree as ET
import requests
import urllib.request
from tkinter import font as tkfont, filedialog
from io import BytesIO
from tkcalendar import DateEntry
from babel.numbers import *
from zipfile import ZipFile
from tkinter import ttk


class NasrParser(tk.Tk):
    def __init__(self, *args, **kwargs):
        self.user_input1 = None
        self.user_input2 = None
        self.user_input3 = None

        self.do_all = True

        self.all_artccs = ['All Artcc', 'ZAP', 'ZAN', 'ZJX', 'ZME', 'ZTL', 'ZHU', 'ZID', 'ZFW', 'ZKC', 'ZHN', 'ZAB',
                           'ZLA', 'ZDV', 'ZSE', 'ZOA', 'ZUA', 'ZBW', 'ZNY', 'ZDC', 'ZMA', 'ZAU', 'ZMP', 'ZLC', 'ZOB',
                           'ZYZ', 'ZSU', 'ZVR', 'ZEG', 'FIM', 'SBA', 'ZAK', 'ZUL', 'ZWG']

        self.exe_directory = os.getcwd()
        self.in_directory = os.getcwd()
        self.out_directory = os.getcwd()
        self.out_folder_name = "Error_Occurred"

        self.label_fg_color = "black"
        self.label_bg_color = "dark gray"
        self.button_fg_color = "black"
        self.button_bg_color = "light gray"
        self.entry_fg_color = "black"
        self.entry_bg_color = "light gray"
        self.image_fg_color = "black"
        self.image_bg_color = "dark gray"
        self.frame_bg_color = "dark gray"

        self.has_apt_file = None
        self.has_meta_file = None

        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=12, slant="italic")
        self.helv10 = tkfont.Font(family='Helvetica', size=10)
        self.helv12 = tkfont.Font(family='Helvetica', size=12)
        self.logo = tk.PhotoImage(file="zlclogo.png")
        self.wip = tk.PhotoImage(file="wip.png")

        menu_bar = tk.Menu(self)
        instruction_menu = tk.Menu(menu_bar, tearoff=0)
        instruction_menu.add_command(label="About",
                                     command=lambda: self.show_frame("WorkInProgress"))
        instruction_menu.add_command(label="Help",
                                     command=lambda: self.show_frame("WorkInProgress"))
        instruction_menu.add_separator()
        instruction_menu.add_command(label="exit",
                                     command=lambda: self.show_frame("WorkInProgress"))
        menu_bar.add_cascade(label="About / Help", menu=instruction_menu)
        self.config(menu=menu_bar)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(3, weight=1)

        self.frames = {}
        for F in (StartScreen, UserInputScreen, DirectoryViewScreen, WorkInProgress,
                  SplashScreen, CompletedScreen, DownLoadingScreen):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("SplashScreen")

    # def artcc_list(self):
    #     with open(f"{self.in_directory}/APT.txt", "r") as apt_file:
    #         text = apt_file.read()
    #         lines = text.split("\n")
    #
    #         for line in lines:
    #             line_type = line[0:3]
    #             if line_type == "APT":
    #                 code = line[674:677]
    #                 self.all_artccs.append(code)


    def get_apt_txt(self):
        if self.has_apt_file == "NO":
            text = str(self.user_input3)
            new_text = text.split("-")
            print(new_text[0], new_text[1], new_text[2])
            print("APT.TXT FILE NOT FOUND DOWNLOADING IT NOW.")

            url = urllib.request.urlopen(
                f"https://nfdc.faa.gov/webContent/28DaySub/{new_text[0]}-{new_text[1]}-{new_text[2]}/APT.zip")

            with ZipFile(BytesIO(url.read())) as my_zip_file:
                for contained_file in my_zip_file.namelist():
                    with open(f"{self.in_directory}\\APT.txt",
                              "wb") as output:

                        for line in my_zip_file.open(contained_file).readlines():
                            # print(line)
                            output.write(line)
                        my_zip_file.close()


            self.has_apt_file = "YES"
            cal.config(state='disabled')
            print(f"APT.TXT FILE DOWNLOAD COMPLETE. \nLocation: {self.in_directory}")
        else:
            # They already have the APT.TXT file. No further action needed, unless they lied about the location of it.
            pass

        self.get_apt_in_artcc(self.do_all)
        self.get_procedures(self.do_all)

        self.show_frame("CompletedScreen")

    def get_apt_in_artcc(self, doing_all):
        if doing_all is True:
            x_var = 0
            input_file = None

            try:
                input_file = open(f"{self.in_directory}/APT.txt", "r")
                print(f"APT.TXT FILE FOUND: {self.in_directory}")
            except FileNotFoundError:
                # Basic error message right now. Need to have in case user selects wrong input directory.
                # This will in the future be automated to take them back to select a new input directory.
                # TODO: If user selects 'invalid' directory, doesnt cause crash and they can select new one.
                print("ERROR: FILE_NOT_FOUND - {}/APT.TXT".format(self.in_directory))
                exit()

            text = input_file.read()
            lines = text.split("\n")

            try:
                os.mkdir(f"{self.out_directory}/{self.user_input1}_{self.user_input2}")
            except FileExistsError:
                # print("ERROR: FILE_EXISTS_ERROR!")
                # IF this part of the code is reached, the Folder already exists.
                # We don't need to do anything if this is the case we just Pass.
                pass

            # Create the Three output files we need. This is okay as long as we close them when we are done with them.

            for working_artcc in self.all_artccs:
                x_var += 1
                if x_var > len(self.all_artccs):
                    x_var = False
                if x_var is not False:
                    try:
                        os.mkdir(f"{self.out_directory}/All Artcc_{self.user_input2}/{working_artcc}_{self.user_input2}")
                    except FileExistsError:
                        # print("ERROR: FILE_EXISTS_ERROR!")
                        # IF this part of the code is reached, the Folder already exists.
                        # We don't need to do anything if this is the case we just Pass.
                        pass

                    apt_output_file = open("{}/All Artcc_{}/{}_{}/{}_{}_AIRPORTS.TXT".format(self.out_directory,
                                                                                             self.user_input2,
                                                                                             working_artcc,
                                                                                             self.user_input2,
                                                                                             working_artcc,
                                                                                             self.user_input2), "w")
                    for line in lines:
                        line_type = line[0:3]
                        artcc = line[674:677]

                        if line_type == "APT":
                            if artcc == working_artcc:
                                airport = line[27:31]
                                f_string = "%s\n" % airport
                                apt_output_file.write(f_string)

                    apt_output_file.close()

                else:
                    pass

        else:
            input_file = None

            try:
                input_file = open(f"{self.in_directory}/APT.txt", "r")
                print(f"APT.TXT FILE FOUND: {self.in_directory}")
            except FileNotFoundError:
                # Basic error message right now. Need to have in case user selects wrong input directory.
                # This will in the future be automated to take them back to select a new input directory.
                # TODO: If user selects 'invalid' directory, doesnt cause crash and they can select new one.
                print("ERROR: FILE_NOT_FOUND - {}/APT.TXT".format(self.in_directory))
                exit()

            text = input_file.read()
            lines = text.split("\n")
            responsible_artcc = self.user_input1

            try:
                os.mkdir(f"{self.out_directory}/{self.user_input1}_{self.user_input2}")
            except FileExistsError:
                # print("ERROR: FILE_EXISTS_ERROR!")
                # IF this part of the code is reached, the Folder already exists.
                # We don't need to do anything if this is the case we just Pass.
                pass

            # Create the Three output files we need. This is okay as long as we close them when we are done with them.

            apt_output_file = open("{}/{}_{}/{}_{}_AIRPORTS.TXT".format(self.out_directory,
                                                                        self.user_input1,
                                                                        self.user_input2,
                                                                        self.user_input1,
                                                                        self.user_input2), "w")

            for line in lines:
                line_type = line[0:3]
                artcc = line[674:677]

                if line_type == "APT":
                    if artcc == responsible_artcc:
                        airport = line[27:31]
                        f_string = "%s\n" % airport
                        apt_output_file.write(f_string)

            apt_output_file.close()
            input_file.close()


    def get_procedures(self, doing_all):
        if doing_all is True:
            x_var = 0

            # Downloads the META file.
            try:
                meta_file = open(f"{self.in_directory}/PROCEDURE_META_{self.user_input2}.xml", "r")
                print(F"FOUND META FILE: {self.in_directory}/PROCEDURE_META_{self.user_input2}.xml")
                meta_file.close()
                self.has_meta_file = "YES"
            except FileNotFoundError:
                self.has_meta_file = "NO"
                print("META FILE NOT FOUND DOWNLOADING IT NOW.")

                url = f"https://aeronav.faa.gov/d-tpp/{self.user_input2}/xml_data/d-tpp_Metafile.xml"
                faa_website_resp = requests.get(url)

                with open(f"{self.in_directory}/PROCEDURE_META_{self.user_input2}.xml", "wb") as file:
                    for chunk in faa_website_resp.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)
                print(
                    F"META FILE DOWNLOAD COMPLETE. \nLocation: {self.in_directory}/PROCEDURE_META_{self.user_input2}.xml")
                self.has_meta_file = "YES"

            for working_artcc in self.all_artccs:
                x_var += 1
                if x_var > len(self.all_artccs):
                    x_var = False
                if x_var is not False:

                    procedure_output_file = open(f"{self.out_directory}/All Artcc_{self.user_input2}/{working_artcc}_{self.user_input2}/{working_artcc}_{self.user_input2}_PROCEDURES.TXT", "w")

                    procedure_changes_output_file = open(f"{self.out_directory}/All Artcc_{self.user_input2}/{working_artcc}_{self.user_input2}/{working_artcc}_{self.user_input2}_PROCEDURE_CHANGES.TXT", "w")

                    apt_in_artcc = open(f"{self.out_directory}/All Artcc_{self.user_input2}/{working_artcc}_{self.user_input2}/{working_artcc}_{self.user_input2}_AIRPORTS.TXT", "r")

                    apt_txt = apt_in_artcc.read()
                    apt_lines = apt_txt.split("\n")

                    tree = ET.parse(f"{self.in_directory}/PROCEDURE_META_{self.user_input2}.xml")
                    root = tree.getroot()

                    for state in root.iter('state_code'):
                        for city in state.iter('city_name'):
                            for airport in city.iter('airport_name'):
                                for line in apt_lines:
                                    wanted_apt = line[:].strip(" ")
                                    if wanted_apt == airport.attrib['apt_ident']:
                                        procedure_output_file.write(f"[{airport.attrib['apt_ident']}]\n")
                                        for record in airport.iter('record'):
                                            procedure_output_file.write(f"      {record[2].text} ")
                                            procedure_output_file.write("| https://aeronav.faa.gov/d-tpp/{}/{}\n".format(
                                                self.user_input2,
                                                record[4].text
                                            ))
                                    else:
                                        # If it gets here, this means the Airport is not in the APT.TXT for that ARTCC.
                                        pass
                    procedure_output_file.close()

                    for state in root.iter('state_code'):
                        for city in state.iter('city_name'):
                            for airport in city.iter('airport_name'):
                                for line in apt_lines:
                                    wanted_apt = line[:].strip(" ")
                                    if wanted_apt == airport.attrib['apt_ident']:
                                        procedure_changes_output_file.write(f"[{airport.attrib['apt_ident']}]\n")

                                        for record in airport.iter('record'):
                                            link_text = record[4].text
                                            link_text_striped = link_text[:-4]

                                            # print(link_text_striped)
                                            link_comp = "https://aeronav.faa.gov/d-tpp/{}/compare_pdf/{}_cmp.pdf".format(
                                                self.user_input2,
                                                link_text_striped
                                            )

                                            if record[3].text == "A":
                                                procedure_changes_output_file.write(f"      ({record[3].text}) ")
                                                procedure_changes_output_file.write(f"{record[2].text}\n")
                                            elif record[3].text == "C":
                                                procedure_changes_output_file.write(f"      ({record[3].text}) ")
                                                procedure_changes_output_file.write(f"{record[2].text} | {link_comp}\n")
                                            elif record[3].text == "D":
                                                procedure_changes_output_file.write(f"      ({record[3].text}) ")
                                                procedure_changes_output_file.write(f"{record[2].text}\n")
                                            else:
                                                pass
                                    else:
                                        # If it gets here, this means the Airport is not in the APT.TXT for that ARTCC.
                                        pass

                    procedure_changes_output_file.close()
                    apt_in_artcc.close()
                    meta_file.close()
                else:
                    pass
        else:
            procedure_output_file = open("{}/{}_{}/{}_{}_PROCEDURES.TXT".format(self.out_directory,
                                                                                self.user_input1,
                                                                                self.user_input2,
                                                                                self.user_input1,
                                                                                self.user_input2), "w")
            procedure_changes_output_file = open("{}/{}_{}/{}_{}_PROCEDURE_CHANGES.TXT".format(self.out_directory,
                                                                                               self.user_input1,
                                                                                               self.user_input2,
                                                                                               self.user_input1,
                                                                                               self.user_input2), "w")
            apt_in_artcc = open("{}/{}_{}/{}_{}_AIRPORTS.TXT".format(self.out_directory,
                                                                     self.user_input1,
                                                                     self.user_input2,
                                                                     self.user_input1,
                                                                     self.user_input2), "r")
            apt_txt = apt_in_artcc.read()
            apt_lines = apt_txt.split("\n")

            # Downloads the META file.
            try:
                meta_file = open(f"{self.in_directory}/PROCEDURE_META_{self.user_input2}.xml", "r")
                print(F"FOUND META FILE: {self.in_directory}/PROCEDURE_META_{self.user_input2}.xml")
                meta_file.close()
                self.has_meta_file = "YES"
            except FileNotFoundError:
                self.has_meta_file = "NO"
                print("META FILE NOT FOUND DOWNLOADING IT NOW.")

                url = f"https://aeronav.faa.gov/d-tpp/{self.user_input2}/xml_data/d-tpp_Metafile.xml"
                faa_website_resp = requests.get(url)

                with open(f"{self.in_directory}/PROCEDURE_META_{self.user_input2}.xml", "wb") as file:
                    for chunk in faa_website_resp.iter_content(chunk_size=1024):
                        if chunk:
                            file.write(chunk)
                print(F"META FILE DOWNLOAD COMPLETE. \nLocation: {self.in_directory}/PROCEDURE_META_{self.user_input2}.xml")
                self.has_meta_file = "YES"

            tree = ET.parse(f"{self.in_directory}/PROCEDURE_META_{self.user_input2}.xml")
            root = tree.getroot()

            for state in root.iter('state_code'):
                for city in state.iter('city_name'):
                    for airport in city.iter('airport_name'):
                        for line in apt_lines:
                            wanted_apt = line[:].strip(" ")
                            if wanted_apt == airport.attrib['apt_ident']:
                                procedure_output_file.write(f"[{airport.attrib['apt_ident']}]\n")
                                for record in airport.iter('record'):
                                    procedure_output_file.write(f"      {record[2].text} ")
                                    procedure_output_file.write("| https://aeronav.faa.gov/d-tpp/{}/{}\n".format(
                                        self.user_input2,
                                        record[4].text
                                    ))
                            else:
                                # If it gets here, this means the Airport is not in the APT.TXT for that ARTCC.
                                pass
            procedure_output_file.close()

            for state in root.iter('state_code'):
                for city in state.iter('city_name'):
                    for airport in city.iter('airport_name'):
                        for line in apt_lines:
                            wanted_apt = line[:].strip(" ")
                            if wanted_apt == airport.attrib['apt_ident']:
                                procedure_changes_output_file.write(f"[{airport.attrib['apt_ident']}]\n")

                                for record in airport.iter('record'):
                                    link_text = record[4].text
                                    link_text_striped = link_text[:-4]

                                    # print(link_text_striped)
                                    link_comp = "https://aeronav.faa.gov/d-tpp/{}/compare_pdf/{}_cmp.pdf".format(
                                        self.user_input2,
                                        link_text_striped
                                    )

                                    if record[3].text == "A":
                                        procedure_changes_output_file.write(f"      ({record[3].text}) ")
                                        procedure_changes_output_file.write(f"{record[2].text}\n")
                                    elif record[3].text == "C":
                                        procedure_changes_output_file.write(f"      ({record[3].text}) ")
                                        procedure_changes_output_file.write(f"{record[2].text} | {link_comp}\n")
                                    elif record[3].text == "D":
                                        procedure_changes_output_file.write(f"      ({record[3].text}) ")
                                        procedure_changes_output_file.write(f"{record[2].text}\n")
                                    else:
                                        pass
                            else:
                                # If it gets here, this means the Airport is not in the APT.TXT for that ARTCC.
                                pass

            procedure_changes_output_file.close()
            apt_in_artcc.close()

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


class StartScreen(tk.Frame):
    """ This Window is the First thing that will be displayed when the program starts."""
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("ARTCC PUBLICATIONS PARSER")
        self.config(bg=controller.frame_bg_color)

        # Define Label Widget Var
        text_first_screen = ""

        # Create Label Widgets
        spacer = tk.Label(self, text="                              ",
                          bg=controller.label_bg_color, fg=controller.label_fg_color)
        spacer1 = tk.Label(self, text="                              ",
                           bg=controller.label_bg_color, fg=controller.label_fg_color)
        w1 = tk.Label(self, image=controller.logo)
        w2 = tk.Label(self, justify=tk.LEFT, padx=10, text=text_first_screen,
                      bg=controller.label_bg_color, fg=controller.label_fg_color)

        # Create Starting Buttons
        b1 = tk.Button(self, text="Start", width=40,
                       command=lambda: controller.show_frame("UserInputScreen"),
                       bg=controller.button_bg_color, fg=controller.button_fg_color)
        b2 = tk.Button(self, text="exit", width=40,
                       command=exit, bg=controller.button_bg_color, fg=controller.button_fg_color)

        # Insert the Widgets into the Window
        w1.grid(row=0, column=1)
        w2.grid(row=0, column=0)
        spacer.grid(row=1, column=0)
        spacer1.grid(row=1, column=1)
        b1.grid(row=2, column=0, sticky="s")
        b2.grid(row=2, column=1, sticky="s")


class UserInputScreen(tk.Frame):
    """ This Window will show up once the user clicks on the button 'Start'. """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        e1_var = None
        e2_var = None
        self.controller = controller
        self.config(bg=controller.frame_bg_color)
        global cal
        global w3_input

        def artcc_selection(var1):
            controller.user_input1 = var1

        def get_user_text():
            # get list of all artcc's possible
            all_good = True
            if controller.user_input1 == 'All Artcc':
                controller.do_all = True
                controller.all_artccs.remove('All Artcc')
            else:
                controller.do_all = False

            # controller.user_input1 = e1_input.get()
            controller.user_input2 = e2_input.get()
            controller.user_input3 = cal.get_date()


            if all_good == True:
                controller.get_apt_txt()
            else:
                controller.show_frame("UserInputScreen")


        def start_prog(event):
            if controller.has_apt_file == "YES" and controller.has_meta_file == "YES":
                w1_download_var = "Parsing through Data, Please wait. I am not Frozen, I promise."
                w1_download.config(text=w1_download_var)
            controller.show_frame("DownLoadingScreen")
            controller.update()
            get_user_text()

        # Define Label Widget Var
        w1_input_text = "ARTCC 3LD: "
        w2_input_text = "AIRAC CYCLE: "
        w3_input_text = "AIRACC EFFECTIVE DATE:"

        tkvar = tk.StringVar(controller)
        tkvar.set('ZLC')
        controller.user_input1 = 'ZLC'

        # Create Widgets
        input_logo = tk.Label(self, image=controller.logo,
                              bg=controller.image_bg_color, fg=controller.image_fg_color)
        spacer1 = tk.Label(self, justify=tk.LEFT, text="              ",
                           bg=controller.label_bg_color, fg=controller.label_fg_color)
        spacer2 = tk.Label(self, justify=tk.LEFT, text="              ",
                           bg=controller.label_bg_color, fg=controller.label_fg_color)
        spacer3 = tk.Label(self, justify=tk.LEFT, text="              ",
                           bg=controller.label_bg_color, fg=controller.label_fg_color)
        spacer4 = tk.Label(self, justify=tk.LEFT, text="              ",
                           bg=controller.label_bg_color, fg=controller.label_fg_color)
        spacer5 = tk.Label(self, justify=tk.LEFT, text="              ",
                           bg=controller.label_bg_color, fg=controller.label_fg_color)

        w1_input = tk.Label(self, justify=tk.RIGHT, text=w1_input_text,
                            bg=controller.label_bg_color, fg=controller.label_fg_color)

        d1_input = tk.OptionMenu(self, tkvar, *controller.all_artccs, command=artcc_selection)
        d1_input.config(width=30, bg=controller.entry_bg_color, fg=controller.entry_fg_color)

        w2_input = tk.Label(self, justify=tk.RIGHT, text=w2_input_text,
                            bg=controller.label_bg_color, fg=controller.label_fg_color)
        w3_input = tk.Label(self, justify=tk.RIGHT, text=w3_input_text,
                            bg=controller.label_bg_color, fg=controller.label_fg_color)

        # Create Entry Fields
        # e1_input = tk.Entry(self, width=40, textvariable=e1_var,
        #                     bg=controller.entry_bg_color, fg=controller.entry_fg_color)
        e2_input = tk.Entry(self, width=40, textvariable=e2_var,
                            bg=controller.entry_bg_color, fg=controller.entry_fg_color)
        this_var = None
        cal = DateEntry(self, width=36, background='darkblue',
                        bg=controller.entry_bg_color, fg=controller.entry_fg_color,
                        borderwidth=2, textvariable=this_var)

        # Create Buttons
        b1_input = tk.Button(self, text="Create Files", width=40,
                             bg=controller.button_bg_color, fg=controller.button_fg_color)

        b1_input.bind("<ButtonRelease>", start_prog)

        # Insert ALL into the window
        input_logo.grid(row=0, column=0, columnspan=2)
        spacer5.grid(row=1, column=0, columnspan=2)
        spacer1.grid(row=4, column=0)
        spacer2.grid(row=4, column=1)
        w1_input.grid(row=5, column=0)
        d1_input.grid(row=5, column=1, sticky='nesw')
        # e1_input.grid(row=5, column=1)
        w2_input.grid(row=6, column=0)
        e2_input.grid(row=6, column=1)
        w3_input.grid(row=7, column=0)
        cal.grid(row=7, column=1)
        spacer3.grid(row=8, column=0)
        spacer4.grid(row=8, column=1)
        b1_input.grid(row=9, column=0, columnspan=2)
        # b2_input.grid(row=9, column=1)




class DirectoryViewScreen(tk.Frame):
    """ This is the Directory Viewer/Selector window. It is displayed when the user clicks on the button
    'View Directories' """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=controller.frame_bg_color)

        # Create Label Widgets
        spacer10 = tk.Label(self, text="                              ",
                            bg=controller.label_bg_color, fg=controller.label_fg_color)
        spacer11 = tk.Label(self, text="                              ",
                            bg=controller.label_bg_color, fg=controller.label_fg_color)
        logo = tk.Label(self, image=controller.logo, bg=controller.image_bg_color, fg=controller.image_fg_color)

        # Define Widget Var
        w1_directory_text = "Input Directory: "
        w2_directory_text = controller.in_directory
        w3_directory_text = "Output Directory: "
        w4_directory_text = controller.out_directory

        # Create Widgets
        spacer = tk.Label(self, text="                              ",
                          bg=controller.label_bg_color, fg=controller.label_fg_color)
        spacer1 = tk.Label(self, text="                              ",
                           bg=controller.label_bg_color, fg=controller.label_fg_color)
        w1_directory = tk.Label(self, justify=tk.CENTER, text=w1_directory_text,
                                bg=controller.label_bg_color, fg=controller.label_fg_color)
        w2_directory = tk.Label(self, justify=tk.CENTER, text=w2_directory_text,
                                wraplength=350, width=50, bg=controller.label_bg_color, fg=controller.label_fg_color)
        w3_directory = tk.Label(self, justify=tk.CENTER, text=w3_directory_text,
                                bg=controller.label_bg_color, fg=controller.label_fg_color)
        w4_directory = tk.Label(self, justify=tk.CENTER, text=w4_directory_text, wraplength=350,
                                width=50, bg=controller.label_bg_color, fg=controller.label_fg_color)

        # Create Buttons
        b1_directory = tk.Button(self, text="Change", width=40,
                                 command=lambda: change_directory("IN"), bg=controller.button_bg_color,
                                 fg=controller.button_fg_color)
        b2_directory = tk.Button(self, text="Change", width=40,
                                 command=lambda: change_directory(), bg=controller.button_bg_color,
                                 fg=controller.button_fg_color)
        b3 = tk.Button(self, text="Start", width=40, bg=controller.button_bg_color, fg=controller.button_fg_color,
                       command=lambda: controller.show_frame("UserInputScreen"))
        b4 = tk.Button(self, text="exit", width=40,
                       command=exit, bg=controller.button_bg_color, fg=controller.button_fg_color)

        # Insert ALL into the window
        logo.grid(row=0, column=0, columnspan=2)
        spacer10.grid(row=1, column=0, columnspan=2)
        w1_directory.grid(row=2, column=0)
        w2_directory.grid(row=2, column=1)
        b1_directory.grid(row=3, column=0)
        spacer.grid(row=4, column=0, columnspan=2)
        spacer1.grid(row=5, column=0, columnspan=2)
        w3_directory.grid(row=6, column=0)
        w4_directory.grid(row=6, column=1)
        b2_directory.grid(row=7, column=0)
        spacer11.grid(row=8, column=0, columnspan=2)
        b3.grid(row=9, column=0, sticky="s")
        b4.grid(row=9, column=1, sticky="s")

        def change_directory(in_or_out=None):
            if in_or_out == "IN":
                controller.in_directory = filedialog.askdirectory(initialdir=controller.exe_directory)
                w2_directory.configure(text=controller.in_directory)
            else:
                controller.out_directory = filedialog.askdirectory(initialdir=controller.exe_directory)
                w4_directory.configure(text=controller.out_directory)


class WorkInProgress(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=controller.frame_bg_color)
        wip_pic = tk.Label(self, image=controller.wip, bg=controller.image_bg_color, fg=controller.image_fg_color)
        b1 = tk.Button(self,
                       text="Go Back To Start Screen",
                       width=50,
                       font=controller.title_font,
                       bg=controller.button_bg_color, fg=controller.button_fg_color,
                       command=lambda: controller.show_frame("DirectoryViewScreen"))
        wip_pic.grid(row=0, column=0, columnspan=2)
        b1.grid(row=1, column=0, columnspan=2)


class SplashScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=controller.frame_bg_color)

        def button_yes():
            cal.config(state='disabled')
            cal.grid_remove()
            w3_input.grid_remove()
            controller.has_apt_file = "YES"
            controller.show_frame("DirectoryViewScreen")

        def button_no():
            cal.config(state='normal')
            controller.has_apt_file = "NO"
            controller.show_frame("DirectoryViewScreen")

        logo = tk.Label(self, image=controller.logo, bg=controller.image_bg_color, fg=controller.image_fg_color)
        spacer = tk.Label(self, text="                              ",
                          bg=controller.label_bg_color, fg=controller.label_fg_color)
        spacer2 = tk.Label(self, text="                              ",
                           bg=controller.label_bg_color, fg=controller.label_fg_color)
        w1_var = "Do you currently have the Airport Text File from the FAA?"
        w1 = tk.Label(self, text=w1_var, width=50, font=controller.title_font,
                      bg=controller.label_bg_color, fg=controller.label_fg_color)

        b1 = tk.Button(self, text="Yes, I have APT.TXT already!", width=40,
                       command=button_yes, bg=controller.button_bg_color, fg=controller.button_fg_color)
        b2 = tk.Button(self, text="Whats that? Please download it for me.", width=40,
                       command=button_no, bg=controller.button_bg_color, fg=controller.button_fg_color)

        logo.grid(row=0, column=0, columnspan=2)
        spacer.grid(row=1, column=0, columnspan=2)
        w1.grid(row=5, column=0, columnspan=2)
        spacer2.grid(row=6, column=0, columnspan=2)
        b1.grid(row=9, column=0, sticky="w")
        b2.grid(row=9, column=1, sticky="e")


class CompletedScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=controller.frame_bg_color)

        logo = tk.Label(self, image=controller.logo, bg=controller.image_bg_color, fg=controller.image_fg_color)
        spacer = tk.Label(self, text="                              ",
                          bg=controller.label_bg_color, fg=controller.label_fg_color)
        spacer2 = tk.Label(self, text="                              ",
                           bg=controller.label_bg_color, fg=controller.label_fg_color)
        w1_var = "Completed! Would you like to complete another ARTCC?"
        w1 = tk.Label(self, text=w1_var, width=50, font=controller.title_font,
                      bg=controller.label_bg_color, fg=controller.label_fg_color)

        b1 = tk.Button(self, text="Yes, this is awesome!", width=40,
                       command=lambda: controller.show_frame("UserInputScreen"),
                       bg=controller.button_bg_color, fg=controller.button_fg_color)
        b2 = tk.Button(self, text="No, I got what I needed.", width=40,
                       command=exit, bg=controller.button_bg_color, fg=controller.button_fg_color)

        logo.grid(row=0, column=0, columnspan=2)
        spacer.grid(row=1, column=0, columnspan=2)
        w1.grid(row=5, column=0, columnspan=2)
        spacer2.grid(row=6, column=0, columnspan=2)
        b1.grid(row=9, column=0, sticky="w")
        b2.grid(row=9, column=1, sticky="e")


class DownLoadingScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(bg=controller.frame_bg_color)
        global w1_download_var
        global w1_download
        # A lot of this code in here will be global so I can call it without changing where the download functions are.
        logo = tk.Label(self, image=controller.logo, bg=controller.image_bg_color, fg=controller.image_fg_color)
        spacer = tk.Label(self, text="                              ",
                          bg=controller.label_bg_color, fg=controller.label_fg_color)
        spacer2 = tk.Label(self, text="                              ",
                           bg=controller.label_bg_color, fg=controller.label_fg_color)
        w1_download_var = "Downloading Files, Please wait. I am not Frozen, I promise."
        w1_download = tk.Label(self, text=w1_download_var, width=50, font=controller.title_font,
                      bg=controller.label_bg_color, fg=controller.label_fg_color)

        logo.grid(row=0, column=0, columnspan=2)
        spacer.grid(row=1, column=0, columnspan=2)
        w1_download.grid(row=5, column=0, columnspan=2)
        spacer2.grid(row=6, column=0, columnspan=2)



try:
    app = NasrParser()
    app.mainloop()
except MemoryError:
    print("MEMORY ERROR")
    exit()
