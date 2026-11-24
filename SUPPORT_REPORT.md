# Task 1 - Support Report
By: Nathaniel Isheoluwa

## What I Helped With
Guided a beginner through setting up VS Code, Git, GitHub, VMware and Ubuntu VM from scratch:
- Installed VS Code
- Installed Git and configured name/email
- Created GitHub account and first repository `my-first-repo`
- Installed VMware Workstation Player
- Downloaded Ubuntu 22.04 LTS and created an Ubuntu Virtual Machine

## Issues Encountered and How I Resolved Them

### Issue 1: Git not recognized in VS Code Terminal
- Problem: After installing Git, `git --version` showed "git is not recognized"
- Fix: Closed VS Code completely and reopened it, then restarted laptop. Ran `git --version` again and it worked.

### Issue 2: VMware - Virtualization Disabled
- Problem: VMware showed error "Virtualization is disabled"
- Fix: Restarted laptop, entered BIOS with F2, enabled Intel VT-x / AMD-V, saved and restarted. VMware then worked.

### Issue 3: Ubuntu VM was very slow
- Problem: Ubuntu was lagging inside VMware
- Fix: Closed other apps and increased VM memory from 2GB to 4GB in VMware Settings > Memory. It became faster.

### Issue 4: Ubuntu download was slow / large
- Problem: Ubuntu file is about 5GB and download was slow
- Fix: Switched to stronger WiFi and did not use mobile data. Download completed.

### Issue 5: GitHub email not verified
- Problem: Beginner could not create repo until email was verified
- Fix: Checked Spam folder, found GitHub verification email, clicked verify.

## Final Result
After support:
- [x] VS Code opens
- [x] `git --version` works
- [x] GitHub account created
- [x] First repo created
- [x] VMware installed
- [x] Ubuntu VM opens and shows desktop

Setup is complete.
