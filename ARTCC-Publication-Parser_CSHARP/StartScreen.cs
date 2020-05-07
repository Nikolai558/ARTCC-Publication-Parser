using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Text;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace ARTCC_Publication_Parser_CSHARP
{
    public partial class MainWindow : Form
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void AboutButton_Click(object sender, EventArgs e) 
        {
            Form form = new AboutScreen();
            form.ShowDialog(this);
            form.Dispose();
        }

        private void StartButton_Click(object sender, EventArgs e)
        {
            
            Form form = new DownLoadAPTScreen();
            form.ShowDialog(this);
            form.Dispose();

        }
    }
}
