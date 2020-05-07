namespace ARTCC_Publication_Parser_CSHARP
{
    partial class DownLoadAPTScreen
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
            this.zlcLogo = new System.Windows.Forms.PictureBox();
            this.startDisclaimerText = new System.Windows.Forms.RichTextBox();
            this.yesResponse = new System.Windows.Forms.Button();
            this.noResponse = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.zlcLogo)).BeginInit();
            this.SuspendLayout();
            // 
            // zlcLogo
            // 
            this.zlcLogo.Image = global::ARTCC_Publication_Parser_CSHARP.Properties.Resources.zlclogo;
            this.zlcLogo.ImageLocation = "";
            this.zlcLogo.Location = new System.Drawing.Point(12, 12);
            this.zlcLogo.Name = "zlcLogo";
            this.zlcLogo.Size = new System.Drawing.Size(394, 96);
            this.zlcLogo.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.zlcLogo.TabIndex = 1;
            this.zlcLogo.TabStop = false;
            // 
            // startDisclaimerText
            // 
            this.startDisclaimerText.BackColor = System.Drawing.SystemColors.ControlDarkDark;
            this.startDisclaimerText.BorderStyle = System.Windows.Forms.BorderStyle.None;
            this.startDisclaimerText.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.startDisclaimerText.ForeColor = System.Drawing.SystemColors.ControlLightLight;
            this.startDisclaimerText.Location = new System.Drawing.Point(13, 114);
            this.startDisclaimerText.Name = "startDisclaimerText";
            this.startDisclaimerText.Size = new System.Drawing.Size(394, 22);
            this.startDisclaimerText.TabIndex = 4;
            this.startDisclaimerText.Text = "Do you currently have the Airport Text File from the FAA?";
            // 
            // yesResponse
            // 
            this.yesResponse.BackColor = System.Drawing.SystemColors.ControlDark;
            this.yesResponse.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.yesResponse.ForeColor = System.Drawing.SystemColors.ControlText;
            this.yesResponse.Location = new System.Drawing.Point(12, 142);
            this.yesResponse.Name = "yesResponse";
            this.yesResponse.Size = new System.Drawing.Size(164, 23);
            this.yesResponse.TabIndex = 5;
            this.yesResponse.Text = "YES";
            this.yesResponse.UseVisualStyleBackColor = false;
            // 
            // noResponse
            // 
            this.noResponse.BackColor = System.Drawing.SystemColors.ControlDark;
            this.noResponse.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.noResponse.ForeColor = System.Drawing.SystemColors.ControlText;
            this.noResponse.Location = new System.Drawing.Point(224, 142);
            this.noResponse.Name = "noResponse";
            this.noResponse.Size = new System.Drawing.Size(164, 23);
            this.noResponse.TabIndex = 6;
            this.noResponse.Text = "NO";
            this.noResponse.UseVisualStyleBackColor = false;
            // 
            // DownLoadAPTScreen
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ControlDarkDark;
            this.ClientSize = new System.Drawing.Size(419, 358);
            this.Controls.Add(this.noResponse);
            this.Controls.Add(this.yesResponse);
            this.Controls.Add(this.startDisclaimerText);
            this.Controls.Add(this.zlcLogo);
            this.ForeColor = System.Drawing.SystemColors.Control;
            this.Name = "DownLoadAPTScreen";
            this.Text = "DownLoadAPTScreen";
            ((System.ComponentModel.ISupportInitialize)(this.zlcLogo)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.PictureBox zlcLogo;
        private System.Windows.Forms.RichTextBox startDisclaimerText;
        private System.Windows.Forms.Button yesResponse;
        private System.Windows.Forms.Button noResponse;
    }
}