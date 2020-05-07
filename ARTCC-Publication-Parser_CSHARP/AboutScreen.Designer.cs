namespace ARTCC_Publication_Parser_CSHARP
{
    partial class AboutScreen
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(AboutScreen));
            this.zlcLogo = new System.Windows.Forms.PictureBox();
            this.aboutAndCredits = new System.Windows.Forms.RichTextBox();
            ((System.ComponentModel.ISupportInitialize)(this.zlcLogo)).BeginInit();
            this.SuspendLayout();
            // 
            // zlcLogo
            // 
            this.zlcLogo.Image = global::ARTCC_Publication_Parser_CSHARP.Properties.Resources.zlclogo;
            this.zlcLogo.ImageLocation = "";
            this.zlcLogo.Location = new System.Drawing.Point(12, 12);
            this.zlcLogo.Name = "zlcLogo";
            this.zlcLogo.Size = new System.Drawing.Size(776, 90);
            this.zlcLogo.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.zlcLogo.TabIndex = 1;
            this.zlcLogo.TabStop = false;
            // 
            // aboutAndCredits
            // 
            this.aboutAndCredits.BackColor = System.Drawing.SystemColors.ControlDarkDark;
            this.aboutAndCredits.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.aboutAndCredits.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.aboutAndCredits.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.aboutAndCredits.Location = new System.Drawing.Point(12, 108);
            this.aboutAndCredits.Name = "aboutAndCredits";
            this.aboutAndCredits.Size = new System.Drawing.Size(776, 330);
            this.aboutAndCredits.TabIndex = 4;
            this.aboutAndCredits.Text = resources.GetString("aboutAndCredits.Text");
            this.aboutAndCredits.TextChanged += new System.EventHandler(this.aboutAndCredits_TextChanged);
            // 
            // AboutScreen
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ControlDarkDark;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.aboutAndCredits);
            this.Controls.Add(this.zlcLogo);
            this.ForeColor = System.Drawing.SystemColors.Control;
            this.Name = "AboutScreen";
            this.Text = "About";
            ((System.ComponentModel.ISupportInitialize)(this.zlcLogo)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox zlcLogo;
        private System.Windows.Forms.RichTextBox aboutAndCredits;
    }
}