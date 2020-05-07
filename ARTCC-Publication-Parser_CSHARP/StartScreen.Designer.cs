namespace ARTCC_Publication_Parser_CSHARP
{
    partial class MainWindow
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainWindow));
            this.vatusaLogo = new System.Windows.Forms.PictureBox();
            this.vatsimLogo = new System.Windows.Forms.PictureBox();
            this.zlcLogo = new System.Windows.Forms.PictureBox();
            this.startDisclaimerText = new System.Windows.Forms.RichTextBox();
            this.startButton = new System.Windows.Forms.Button();
            this.aboutButton = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.vatusaLogo)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.vatsimLogo)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.zlcLogo)).BeginInit();
            this.SuspendLayout();
            // 
            // vatusaLogo
            // 
            this.vatusaLogo.Image = global::ARTCC_Publication_Parser_CSHARP.Properties.Resources.vatusalogo;
            this.vatusaLogo.Location = new System.Drawing.Point(405, 12);
            this.vatusaLogo.Name = "vatusaLogo";
            this.vatusaLogo.Size = new System.Drawing.Size(338, 72);
            this.vatusaLogo.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.vatusaLogo.TabIndex = 2;
            this.vatusaLogo.TabStop = false;
            // 
            // vatsimLogo
            // 
            this.vatsimLogo.Image = global::ARTCC_Publication_Parser_CSHARP.Properties.Resources.vatsimlogo;
            this.vatsimLogo.Location = new System.Drawing.Point(12, 12);
            this.vatsimLogo.Name = "vatsimLogo";
            this.vatsimLogo.Size = new System.Drawing.Size(387, 72);
            this.vatsimLogo.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.vatsimLogo.TabIndex = 1;
            this.vatsimLogo.TabStop = false;
            // 
            // zlcLogo
            // 
            this.zlcLogo.Image = global::ARTCC_Publication_Parser_CSHARP.Properties.Resources.zlclogo;
            this.zlcLogo.ImageLocation = "";
            this.zlcLogo.Location = new System.Drawing.Point(12, 90);
            this.zlcLogo.Name = "zlcLogo";
            this.zlcLogo.Size = new System.Drawing.Size(731, 90);
            this.zlcLogo.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.zlcLogo.TabIndex = 0;
            this.zlcLogo.TabStop = false;
            // 
            // startDisclaimerText
            // 
            this.startDisclaimerText.BackColor = System.Drawing.SystemColors.ControlDarkDark;
            this.startDisclaimerText.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.startDisclaimerText.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.startDisclaimerText.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.startDisclaimerText.Location = new System.Drawing.Point(12, 186);
            this.startDisclaimerText.Name = "startDisclaimerText";
            this.startDisclaimerText.Size = new System.Drawing.Size(731, 235);
            this.startDisclaimerText.TabIndex = 3;
            this.startDisclaimerText.Text = resources.GetString("startDisclaimerText.Text");
            // 
            // startButton
            // 
            this.startButton.BackColor = System.Drawing.SystemColors.ControlDark;
            this.startButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.startButton.ForeColor = System.Drawing.SystemColors.ControlText;
            this.startButton.Location = new System.Drawing.Point(235, 427);
            this.startButton.Name = "startButton";
            this.startButton.Size = new System.Drawing.Size(164, 23);
            this.startButton.TabIndex = 4;
            this.startButton.Text = "START";
            this.startButton.UseVisualStyleBackColor = false;
            this.aboutButton.Click += new System.EventHandler(this.StartButton_Click);
            // 
            // aboutButton
            // 
            this.aboutButton.BackColor = System.Drawing.SystemColors.ControlDark;
            this.aboutButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.aboutButton.ForeColor = System.Drawing.SystemColors.ControlText;
            this.aboutButton.Location = new System.Drawing.Point(405, 427);
            this.aboutButton.Name = "aboutButton";
            this.aboutButton.Size = new System.Drawing.Size(164, 23);
            this.aboutButton.TabIndex = 5;
            this.aboutButton.Text = "ABOUT";
            this.aboutButton.UseVisualStyleBackColor = false;
            this.aboutButton.Click += new System.EventHandler(this.AboutButton_Click);
            // 
            // MainWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ControlDarkDark;
            this.ClientSize = new System.Drawing.Size(767, 462);
            this.Controls.Add(this.aboutButton);
            this.Controls.Add(this.startButton);
            this.Controls.Add(this.startDisclaimerText);
            this.Controls.Add(this.vatusaLogo);
            this.Controls.Add(this.vatsimLogo);
            this.Controls.Add(this.zlcLogo);
            this.ForeColor = System.Drawing.SystemColors.Control;
            this.Name = "MainWindow";
            this.Text = "ARTCC Publication Parser";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.vatusaLogo)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.vatsimLogo)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.zlcLogo)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox zlcLogo;
        private System.Windows.Forms.PictureBox vatsimLogo;
        private System.Windows.Forms.PictureBox vatusaLogo;
        private System.Windows.Forms.RichTextBox startDisclaimerText;
        private System.Windows.Forms.Button startButton;
        private System.Windows.Forms.Button aboutButton;
    }
}

