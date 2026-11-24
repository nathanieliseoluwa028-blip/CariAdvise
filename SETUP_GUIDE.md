TASK 1 - BEGINNER SETUP GUIDE
By: Nathaniel Isheoluwa
For: Complete Beginner with Windows Laptop

This guide will help a complete beginner set up everything needed to start coding from zero: VS Code, Git, GitHub, VMware and Ubuntu Virtual Machine.

Follow it in order. Do not skip Part 0.

What You Need Before You Start


Windows 10 or 11 laptop.
At least 8GB RAM.
At least 30GB free space.
Good WiFi- Ubuntu download is about 5GB.
About 2 hours total.

PART 0: ENABLE VIRTUALIZATION FIRST - DO THIS BEFORE ANYTHING

Virtualization is a setting in your laptop that lets VMware run a virtual machine. If it is OFF, VMware will install but Ubuntu will NOT start. So we check this first.

Step 1: Check if it is already Enabled

1. Right-click on the Taskbar at the bottom of your screen
2. Click Task Manager
3. Click Performance at the top
4. Click CPU on the left
5. Look at the bottom right. It will say:

Virtualization: Enabled OR Virtualization: Disabled

If it says Enabled: Perfect. Go to Part 1.
If it says Disabled, you must turn it ON:

1. Save all your work and restart your laptop
2. As soon as it starts turning on, keep pressing F2 or Del or F10 repeatedly. Different laptops use different keys. If Windows loads, you were too slow - restart and try again.
3. You will enter a blue or black screen called BIOS / UEFI Setup. Use the arrow keys on your keyboard .mouse may not work here.
4 .Look for one of these menus: Advanced, Configuration, System, or Security
5.Inside, look for one of these options:


Intel Virtualization Technology.
Intel VT-x
AMD-V
SVM mode
Virtualization Technology

6. Change it to Enabled.
7. Press F10 to Save and Exit. Your laptop will restart.
8.Go back to Task Manager > Performance > CPU and check again. It should now say Virtualization: Enabled.

Do not download VMware or Ubuntu until this says Enabled.

PART 1: INSTALL VS CODE
VS Code is the app we use to write code.
1. Go to code.visualstudio.com.
2. Click Download for Windows. 
3. Open the downloaded file.
4. Click Next, Next, Install, then Finish. Tick "Add to PATH" if you see it.
5. Open VS Code.
Check: You should see a screen that says "Welcome to VS Code". If it opens, it works.

PART 2: INSTALL GIT
Git is the tool that tracks your code and connects VS Code to GitHub.
1. Go to git-scm.com.
2. Click Download for Windows.
3. Open the installer. Keep clicking Next, then Install, then Finish.
4. Open VS Code. Press Ctrl + ` - that is the key under Esc - to open Terminal.
5. Type this and press Enter: git --version.
6. If it shows something like git version 2.43.0, Git works.
Set your name - very important, do this once:
Type these two lines one by one. Replace with your own name and email:
git config --global {{IE_5}}http://user.name{{/IE_5}} "Your Full Name"
git config --global {{IE_6}}http://user.email{{/IE_6}} "youremail@gmail.com"
Check: If git --version shows a version number, Git is installed correctly.

PART 3: CREATE GITHUB ACCOUNT AND FIRST REPOSITORY
GitHub is a website where your code is stored online.
1. Go to github.com.
2. Click Sign Up.
3. Enter your email, create a password, choose a username.
4. Verify your email - check your inbox and Spam folder for GitHub email.
5. Once logged in, click the + at the top right > New Repository.
6. Repository name: my-first-repo.
7. Tick "Add a README file"Click.
8. Create Repository.
Check: You now have a link like
{{IE_7}}http://github.com/yourusername/my-first-repo{{/IE_7}}. Save this link - this is your first repository link for submission.
PART 4: INSTALL VMWARE AND UBUNTU VIRTUAL MACHINE
This is the longest part. Do it last, after Parts 1-3 are done.
Step A: Install VMware Workstation Player - Free
1. Go to vmware.com and search for Download Workstation Player.
2. Download for Windows.
3. Open installer. Click Next, Next, Install, Finish.
4. Restart laptop if it asks you to.
Step B: Download Ubuntu
1. Go to ubuntu.com/download/desktop.
2. Download Ubuntu 22.04 LTS. The file is about 5GB.
3. Wait for it to finish. Do not open it yet. Remember where it saved.
Step C: Create the Virtual Machine
1. Open VMware Workstation Player.
2. Click Create a New Virtual Machine.
3. Choose "Installer disc image file (iso)" > Browse > Select the Ubuntu file you downloaded.
4. Full Name: Your Name, Username: yourname, Password: Choose a simple password and WRITE DOWN.
5. Virtual Machine Name: Ubuntu.
6. Disk size: 20GB, choose "Store virtual disk as a single file".
7. Memory: Give it 2GB if your laptop has 8GB RAM, 4GB if you have 16GB RAM.
8. Click Finish, then click Play Virtual Machine.
Step D: Install Ubuntu
1. It will load and ask for Language - Choose English.
2. Click Install Ubuntu, keep clicking Continue / Install Now.
3. Wait 15-20 minutes. Do not turn off your laptop
4. When it finishes, it will restart and show the Ubuntu Desktop.
Check: You should see the purple/orange Ubuntu desktop INSIDE VMware. Take a screenshot of this - this is your proof that Ubuntu VM is running.
PART 5: FINAL CHECK - DID EVERYTHING WORK?
Tick this list:
[ ] Virtualization: Enabled in Task Manager.
[ ] VS Code opens.
[ ] git --version works in Terminal.
[ ] GitHub account created.
[ ] First repo created - link saved.
[ ] VMware installed.
[ ] Ubuntu VM opens and shows desktop
If all 7 are ticked, setup is DONE.
COMMON ISSUES AND HOW I FIXED THEM
1. Virtualization was Disabled: Fixed by entering BIOS, enabling Intel VT-x / AMD-V, saving and restarting. Checked again in Task Manager.
2. Git not recognized: Closed VS Code and opened it again, or restarted laptop. Then tried git --version again.
3. VMware says "No virtualization": This means Part 0 was skipped. Go back to Part 0 and enable virtualization.
4. Ubuntu is very slow: Closed other apps, gave VM more RAM in VMware Settings > Memory.
5. Ubuntu download is slow: Used strong WiFi, did not download on mobile data.
6. GitHub email not verified: Checked Spam folder for GitHub email.
SUPPORT REPORT
Beginner Helped:
Name: [Beginner Full Name]
Laptop: [e.g. HP, Windows 11, 8GB RAM]
Date of Support: [e.g. 20 Nov 2026]
How We Met: [WhatsApp call / In person]
What We Did:
1. Installed VS Code — [Worked / Had issue].
2. Installed Git + Set Name/Email — [Worked / Had issue].
3. Created GitHub Account + First Repo — [Worked / Had issue]
4. Repo Link: [paste link here]Installed VMware + Ubuntu VM — [Worked / Had issue]
Issues We Had And How I Fixed Them:
1. Issue: [e.g. Git not recognized]
Fix: [e.g. Restarted VS Code and tried again]
2. Issue: [e.g. Virtualization was Disabled]
Fix: [e.g. Entered BIOS, enabled Intel VT-x]
Final Check:
[ ] VS Code opens.
[ ] git --version works.
[ ] GitHub repo created.
[ ] Ubuntu VM opens
Proof:
Screenshot 1: [VS Code open]
Screenshot 2: [git --version in Terminal]
Screenshot 3: [GitHub repo page]
Screenshot 4: [Ubuntu desktop in VMware]




