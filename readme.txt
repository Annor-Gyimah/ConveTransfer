************************************************************
*  Product: Intel(R) Chipset Device Software
*  Package version: 10.1.18807.8279
*  Installer version: 3.1.7.143
*  Date: 06/19/2021
************************************************************

   NOTE: 
            For the list of supported chipsets, please refer
            to the Release Notes

************************************************************
*  CONTENTS OF THIS DOCUMENT
************************************************************
This document contains the following sections:

1.  Overview
2.  System Requirements
3.  Contents of the Distribution Package
    3A. Public and NDA Configurations
4.  List of Available Command Line Switch Options 
5.  Installing the Software in Interactive Mode
6.  Installing the Software in Silent Mode
7.  Installing the INF Files Prior to OS Installation
8.  Installing the INF Files After OS Installation
9.  Verifying Installation of the Software and 
     Identifying the Software Version Number
10. Troubleshooting


************************************************************
* 1.  OVERVIEW
************************************************************
The Intel(R) Chipset Device Software installs Windows* 
INF files to the target system. These files outline to 
the operating system how to configure the Intel(R) chipset 
components in order to ensure that the following feature 
functions properly:

            - Identification of Intel(R) Chipset Components in 
              the Device Manager
            - Modern Standby requires that 0 devices report 
              problems (no yellow bangs in Device Manager)

This software can be installed in three modes: Interactive,
Silent and Unattended Preload. Interactive Mode requires 
user input during installation; Silent Mode and Unattended 
Preload do not.

This software is DCHU compliant
    D - compliant
    C - compliant, due to not implemented
    H - compliant, due to no UI components
    U - compliant

This software also offers a set of command line switches, 
which provide additional installation choices. Refer to
Section 4 for detailed descriptions of these switches.

Note: Intel(R) Chipset Device Software uses an unusual date 
for the devices it is targeting. The date 07/18/1968 is 
symbolic - Intel was founded that day. The reason this
date is used is to lower the rank of Intel(R) Chipset Device
Software.
This is necessary because it's a supporting utility that
should not overwrite any other drivers. Updating Intel(R)
Chipset Device Software is not needed - do not worry if you
don't have the latest version.


************************************************************
* 2.  SYSTEM REQUIREMENTS 
************************************************************
1.  It is mandatory that the Intel(R) Chipset Device Software 
    be installed onto the target system prior to the 
    installation of other drivers.

2.  Please refer to the Release Notes to view the list of 
    chipsets that the software included with this distribution 
    package is designed to operate with.

3.  One of the following operating systems must be 
    fully installed and running on the system
    before installing this software:

    Microsoft Windows Server 2012 R2 x64
    Microsoft Windows 10 (Refer Release Notes for details.)
    Microsoft Windows 10 x64
    Microsoft Windows* Server 2016 x64
    Microsoft Windows* Server 2019 x64
	Microsoft Windows* Server 2022 x64
    
    This software is designed for the latest Service packs 
    releases of above operating systems.

    To verify which operating system has been installed onto 
    the target system, follow the steps below:

    a.  Click on Start.
    b.  Select Settings.
    c.  Select Control Panel.
    d.  Double-click on the System icon.
    e.  Click on the General system properties tab.
    f.  Verify which OS has been installed by reading
        the System information.
                              
4.  It is recommended that the software be installed on 
    systems with at least 64MB of system memory.

5.  It is recommended that there be a minimum of 5MB of hard
    disk space on the system in order to install this software.

6.  The operating system must be fully installed and running on 
    the system before running this software.

7.  Close any running applications to avoid installation problems.

Please check with the system provider to determine which 
operating system and Intel(R) chipset are used in the system.


************************************************************
* 3.  CONTENTS OF THE DISTRIBUTION PACKAGE
************************************************************
The Intel(R) Chipset Device Software package contains the 
following items:

    File(s)       
    -------
    SetupChipset.exe
       -or-
    Chipset_<version>_VIP.zip
       -or-
    Chipset_<version>_MUP.zip
       -or-
    Chipset_<version>_BKC.zip
       -or-
    Chipset_<version>_<configuration>_MUP.zip
       -or-
    Chipset_<version>_<configuration>_BKC.zip

The <version> string could be similar to "10.0.0", and
the <configuration> string could be similar to "Pre-Alpha",
"Alpha", "Beta, "Public", or "NDA".


************************************************************
* 3A. PUBLIC AND NDA CONFIGURATIONS
************************************************************
The Intel(R) Chipset Device Software supports two types of
configurations, "Public" and "NDA". The Public configuration
has all Intel Confidential (IC) information, such as platform
codenames, stripped out of the build. The NDA configuration
includes this information, as well as extra installation
functionality that is not safe enough to be released
publicly, but is required for validation efforts. For this
reason, NDA-configured releases are not permitted to be
released publicly or to anyone not possessing a Non-Dislosure
Agreement (NDA) with Intel Corporation.

To help identify whether a given build configured with NDA
functionality, a large red banner has been added to the user
interface of the installer, stating that it is an NDA build.

The Public and NDA configurations are only available for
production releases, "Production Candidate" (PC) and
"Production Version" (PV). For non-production releases
Pre-Alpha, Alpha, and Beta, it is assumed that the build
will not be released publicly. Therefore, non-production
releases only have one configuration, the NDA configuration.

The Intel(R) Chipset Device Software does not support
installation of both build configurations on a single
machine, this will result in an error thrown by the
Microsoft Windows* Installer framework during the second
installation, manifesting as an error message in the log
files and on the installer user interface when running in 
Interactive mode. The installer will exit with code 666.


************************************************************
* 4.  LIST OF AVAILABLE COMMAND LINE FLAG OPTIONS
************************************************************
The Intel(R) Chipset Device Software supports several 
command line switches for various installation options. 

Below is a list of all the available command line switches that
may be used with the program call.

Switch          Description
----            -----------
-?              Displays the the help dialog

-downgrade      Ignores the downgrade warning.

-extract <path> Extracts all driver files to the path specified.

-l <path>       
-log <path>     Changes the default log path.      


-lang <lcid>    Specifies the language of the UI.

-norestart      Inhibits the installer from automatically initiating
                system reboot after installer, when reboot is required 
                and installer UI mode is not interactive (silent or
                passive).

-overall        Overwrites all drivers.

-p <path>       Changes the default install path.

-q
-quiet
-s              
-silent         Does not display any setup dialogs.              


Below are the language codes used with the '-lang' switch:

   LCID       Language
 --------    ------------------------
   0401       Arabic (International)
   0804       Chinese (Simplified)
   0404       Chinese (Traditional)
   0405       Czech
   0406       Danish
   0413       Dutch
   0409       English (United States)
   040B       Finnish
   040C       French (International)
   0407       German
   0408       Greek
   040D       Hebrew
   040E       Hungarian
   0410       Italian
   0411       Japanese
   0412       Korean
   0414       Norwegian
   0415       Polish
   041B       Slovak
   0416       Portuguese (Brazil)
   0816       Portuguese (Standard)
   0419       Russian
   040A       Spanish (International)
   041D       Swedish
   041E       Thai
   041F       Turkish

************************************************************
* 5.  INSTALLING THE SOFTWARE IN INTERACTIVE MODE
************************************************************
1.  Verify that all system requirements have been met as 
     described in Section 2 above.

2.  Run the setup program:
     SetupChipset.exe

3.  You will be prompted to agree to the license agreement.  
     If you do not agree, the installation program will exit.
    
4.  Upon successful installation you will see a screen listing
     Intel(R) Chipset Device Software as installed.
     You can view the instalation logs by clicking on
     View Log Files in the bottom left-hand side corner.


************************************************************
* 6.  INSTALLING THE SOFTWARE IN SILENT MODE
************************************************************
1.  Verify that all system requirements have been met as 
     described in section 2.

2.  Run the setup program:
     For silent install:
       SetupChipset.exe -s

3.  The utility will perform the necessary updates and 
     record the installation status in the following system 
     registry key:
        HKEY_LOCAL_MACHINE\Software\Intel\INFInst

4.  If the utility was not invoked with the "-norestart"
     swith, the system may automatically restart if the
     setup was successful.

    NOTE: If prompted, the system MUST be restarted for all 
     device updates to take effect.

5.  To determine whether the install was successful, verify 
     the "version" value in the registry key specified in 
     Step 3.

6.  In Silent Mode the utility will not display the license
     agreement. When using Silent Mode the license agreement,
     license.txt, will be placed in the following folder:
     %ProgramFiles%\Intel\Intel(R) Chipset Device Software
     Please read this agreement.

   The following describes the registry entry made:

             Name: "version"          
             Type: String          
             Data: <varies> 
                  Current version number of the Intel(R) Chipset Device 
                  Software 


************************************************************
* 7.  INSTALLING THE INF FILES PRIOR TO OS INSTALLATION
************************************************************
    This procedure requires a minimum of 5MB of hard disk space.
    It is important to make sure there is enough disk space
    before beginning the copy process. Copy the operating system
    installation files from the setup directory to a directory
    on the hard disk. This can be done by opening 'My Computer',
    right-clicking on the correct drive, and selecting 'Properties'.

    IMPORTANT NOTE:
    The installer executable (SetupChipset.exe) must always be run
    to guarantee correct installation. In the case of INF injection,
    this means that the installer must be run after the OS installation
    completes, even if the INF files have already been installed via
    INF injection or Have Disk installation.

By [supported Windows OS] it is meant a Windows operating system
that is listed in section 2.

The simplest method for installing Windows onto new hardware is to
start directly from the Windows product DVD with an answer file called 
Autounattend.xml. Boot the computer with the Windows Setup media in the 
DVD drive and the configuration set available on an external drive. 
By default, Windows Setup searches all removable media for an answer 
file called Autounattend.xml. Autounattend.xml must be located at the 
root of the removable media.

The answer file enables you to automate all or parts of Windows Setup 
Including adding INF files. You can create an answer file by using Windows
System Image Manager (Windows SIM).

Microsoft* published a Windows Automated Installation Kit(WAIK) 
(Must be the supported Windows OS version) which facilitates creation of answer files 
and image creation for unattended installs of supported Windows OS with tools such as
Windows SIM

To create a configuration set you will need:
	Windows System Image Manager (Windows SIM) installed on a technician computer.
	An authorized copy of a supported Windows OS product DVD.
	Chipset device driver .inf files.
	Access to a network share or removable media with sufficient storage space.

1. Create a New Answer File
(In this step, you define basic disk configuration and other settings that are required 
for an unattended installation.)
	A. On your technician computer, insert the supported Windows OS product DVD into 
	   the local DVD-ROM drive.
	B. On the desktop of the technician computer, navigate to the \Sources directory
	   on your DVD-ROM drive. Copy the Install.wim file from the Windows product DVD
           to a location on the computer.
	C. Open Windows SIM. On the desktop of the computer, click Start, point to 
           Programs, point to Microsoft Windows OPK (or Windows AIK), and then click 
           Windows System Image Manager.
	D. On the File menu, click Select Windows Image.
	E. In the Select a Windows Image dialog box, navigate to the location where 
	   you saved the Install.wim file, and then click Open.
		Note:  
		A warning will appear that a .clg file does not exist. 
		Click OK to create a .clg file. 
		If there is more than one Windows image in the .wim file, you are prompted
		to select the Windows image to open.
	F. On the File menu, click New Answer File.
2. Create a Distribution Share
(In this step, you create a distribution-share folder on your technician computer. 
The distribution share will store out-of-box drivers, applications, and any resource 
files needed for your custom installation.)
	A. In Windows SIM, in the Distribution Share pane, click Select a Distribution
	   Share.
	B. Right-click to select Create Distribution Share.
	C. The Create a Distribution Share dialog box appears.
	D. Click New Folder, and then type a name for the folder. For example 
	   "C:\MyDistributionShareClick"
	E. In the Distribution Share pane, the distribution share folder opens. 
	   Windows SIM automatically creates the following folder structure.
		C:\MyDistributionShare\$OEM$ Folders
		C:\MyDistributionShare\Packages
		C:\MyDistributionShare\Out-of-Box 
3. Add Drivers and Applications to Distribution Share
	A. In Windows SIM, on the Tools menu, select Explore Distribution Share.
	B. The Distribution Share window opens.
	C. Copy your device driver files (.inf) to the Out-of-Box Drivers folder.
		1. Create subdirectories for each driver. For example, 
		   create directories "Chipset" and "Video" in the Out-of-Box Drivers 
		   folder.
	D. Close the distribution share folder.
4. Add a Device Driver to the Answer File
(In this step, you add an out-of-box drivers (.inf) path to your answer file.)	
	A. In Windows SIM, on the Insert menu, click Driver Path, and then click Pass 1
	   windowsPE. 
	B. The Browse for Folder dialog box appears.
	C. Select the driver path to add to the answer file, and then click OK. 
	   For example, "C:\MyDistributionShare\Out-of-Box Drivers\Chipset"
5. Validate the Answer File
(In this step, you validate the settings in your answer file and then save them to a file.)
	A. In Windows SIM, click Tools, and then click Validate Answer File.
	B. If the answer file validates successfully, a "success" message appears in the
           Messages pane; otherwise, error messages appear in the same location.
	C. If an error occurs, in the Messages pane, double-click the error to navigate
           to the incorrect setting. Change the setting to fix the error, and then 
           revalidate the answer file.
	D. On the File menu, click Save Answer File. Save the file as Unattend.xml.
6. Create a Configuration Set
(In this step, you create a configuration set that will gather all of the resource files 
that you specified in your answer file into one location.)
	A. In Windows SIM, on the Tools menu, select Create Configuration Set.
	B. The Create Configuration Set window opens.
	C. Specify a destination location where you intend to publish the configuration set
	D. Select a removable drive such as a USB flash drive (UFD), and then click OK.
7. Deploying a Configuration Set Without a Network
	A. Turn on the new computer.
	B. Insert both the removable media containing your configuration set and the
	   supported Windows OS product DVD into the new computer.	
		Note: When using a USB flash drive, insert the drive directly into the 
                      primary set of USB ports for the computer. For a desktop computer, 
                      this is typically in the back of the computer.
 	C. Restart the computer by pressing CTRL+ALT+DEL.
		Note: This example assumes that the hard drive is blank.
	D. Windows Setup (Setup.exe) begins automatically.
	E. By default, Windows Setup searches all removable media for an answer file 
	   called Autounattend.xml. Autounattend.xml must be located at the root of the 
           removable media.
	F. After Setup completes, validate that all customizations were applied, and then
	   reseal the computer by using the generalize option

    For more information about supported Windows OS answer 
    files and unattended installations, please refer to the 
    Windows Automated Installation Kit (WAIK) User's Guide.

************************************************************
* 8.  INSTALLING THE INF FILES AFTER OS INSTALLATION
************************************************************

By [supported Windows OS] it is meant a Windows operating system
that is listed in section 2.

Some Intel(R) chipset platforms already are supported by
supported Windows OS so it may not be necessary to use the 
INF files provided by this software to update the supported
Windows OS.

The following steps describe the installation process of
the supported Windows OS INF files.  You may need to repeat these 
steps to update all Intel(R) chipset devices not supported
by supported Windows OS.

    1.  Copy the contents of the <INF Extract Directory>
        to the root directory of a removable media, such as 
        a USB flash drive (UFD) or floppy disk (A:\).
    2.  Close all programs currently running on the system.
    3.  Click on Start.
    4.  Select Settings.
    5.  Select the Control Panel.
    6.  Double-click on the System icon.
    7.  Click on the Hardware tab.
    8.  Click on the Device Manager button.
    9.  Select "Devices by connection" under the View menu.
    10. Click on MPS Uniprocessor PC -OR- MPS 
            Multiprocessor PC.
            
        NOTE: 
            Only one of the above items will be 
            displayed for a given system.
            
    11. Click on PCI bus.
    12. Right-click on the line containing the description
            PCI standard host CPU bridge
            -or-
            PCI standard ISA bridge
            -or-
            PCI standard PCI-to-PCI bridge
            -or- 
            PCI System Management Bus
            -or- 
            Standard Dual PCI IDE Controller
            -or-
            Standard Universal PCI to USB Host Controller
            (This line will be selected.)
    13. Select Properties from the pull-down menu.
    14. Click on the Driver tab.
    15. Click on the Update Driver button.
    16. Supported Windows OS will launch the Upgrade Device.
            Driver Wizard. Select Browse my computer for the driver software.
    17. Enter "X:\" in the Combo Box, where X is the drive letter
        for your UFD or floppy disk
    18. Ensure that the Include Subfolders checkbox is checked.
    19. Select Next.
    20. The window Will Display the Device that was installed.
    21. Select Close.
    22. Reboot the system if prompted to do so.

************************************************************
* 9.   IDENTIFYING THE SOFTWARE VERSION NUMBER
************************************************************
The version numbers displayed by Device Manager for a given 
device may not be the same as the Intel(R) Chipset Device 
Software package version.
The package contains several independent releases, all
of which are listed at the beginning of this readme.
 
The correct package version number is indicated at the
registry entry specified in section 6 after installing
using SetupChipset.exe.
When installing without using SetupChipset.exe no registry
entry is made.

************************************************************
* 10.  TROUBLESHOOTING
************************************************************
It is assumed that the system requirements in Section 2 above 
have been satisfied.

Issue:      System locks up during Device Manager Remove or 
            during restart.

Solution:   System lockup can occur during reboot as a 
            result of several possible system issues.  In 
            the event of system lockup, reboot the machine 
            and view Device Manager.  If devices are listed 
            properly and the system experiences no further 
            problems, then the .INF file restore process was 
            successful. If devices are not configured 
            correctly, try re-running the procedures 
            outlined in Section 3.

            If this does not fix the issue or further issues
            are experienced, reinstall the operating system.

Issue:      After running the setup program and rebooting 
            the machine, Windows reports that it cannot find 
            one of the following files: ESDI_506.pdr

Solution:   Click Browse in the dialog box where this issue
            occurs, locate the <Windows>\System\IOSubsys
            directory. Click OK. The system should be able to
            locate this file in this directory and continue 
            re-enumerating for the new devices.

Issue:      After running the setup program and rebooting 
            the machine, Windows reports that it cannot find 
            one of the following files:
 
                  UHCD.SYS
                  USBD.SYS
                  USBHUB.SYS

Solution:   Click Browse in the dialog box where this issue 
            occurs and locate the following directory:
			
                  <Winnt>\System32\drivers 
                  
            Click OK. The system should be able to locate the 
            files in this directory and continue re-enumerating 
            for the new devices.

Issue:      After running the setup program and rebooting 
            the machine, Windows reports that it cannot find 
            the following file: ISAPNP.VXD

Solution:   Click Browse in the dialog box where this issue 
            occurs and locate the <Winnt>\System directory. 
            Click OK. The system should be able to locate this 
            file in this directory and continue re-enumerating 
            for the new devices.

Issue:      After performing the silent install, the 
            HKLM\Software\Intel\InfInst key was not created.

Solution:   This is caused by one of the following 
            scenarios:
               - The current system does not contain a 
                 supported operating system, or
                 -or-
               - The current system does not contain a 
                 supported chipset.

            Verify that the System Requirements are met as 
            outlined in Section 2.


************************************************************
* DISCLAIMER
************************************************************
Intel is making no claims of usability, efficacy or warranty.  
The Intel(R) SOFTWARE LICENSE AGREEMENT
(OEM / IHV / ISV Distribution & Single User) 
completely defines the licensed use of this software.
************************************************************
Information in this document is provided in connection with 
Intel(R) products.  No license, express or implied, by estoppel 
or otherwise, to any intellectual property rights is granted 
by this document.  Intel assumes no liability whatsoever, 
and Intel disclaims any express or implied warranty relating 
to sale and/or use of Intel(R) products, including liability 
or warranties relating to fitness for a particular purpose, 
merchantability or infringement of any patent, copyright or 
other intellectual property right.  Intel(R) products are 
not intended for use in medical, life saving, or 
life-sustaining applications.

************************************************************
Intel Corporation disclaims all warranties and liabilities 
for the use of this document and the information contained 
herein, and assumes no responsibility for any errors which 
may appear in this document, nor does Intel make a 
commitment to update the information contained herein.  
Intel reserves the right to make changes to this document at 
any time, without notice.
************************************************************
************************************************************

* Intel is a trademark or registered trademark of Intel Corporation 
  or its subsidiaries in the United States and other countries.
* Other brands and names are the property of their 
  respective owners.

Copyright (c) Intel Corporation, 1997-2020
