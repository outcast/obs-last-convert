# obs-last-convert
used to post "live" message to twitter from OBS/SLOBS using Streamdeck Buttons

# Requirements

## All OSes
  * [Python 3.6](http://python.org)


## macOS and Linux
  * [FFmpeg](http://ffmpeg.org)

*note: This comes with a tested prebuild version of FFmpeg for Windows 10*

# Install
Run the install script for your operating system:
  * install.ps1 for Windows 10 with Powershell
  * install.sh for macOS and Linux

# Setup
## OBS/SLOBS
Setup the directory you want your recordings to go to. This will use the first
file in descending order that ends with the flv extension.

## Streamdeck
Import the Streamdeck profile. ( Profile.streamDeckProfile ). Adjust the settings
as needed. Pay attention mainly to make sure paths are in the right place.

#### Windows
  Open the multi-action button and make sure the path to the wrapper powershell
  script is correct.

#### macOS and Linux
Open the multi-action button and make sure the path to the wrapper bash
script is correct.

After that is all done be sure to test it. Then should just be able to copy and
paste that button into any profile where you want it.


# Support
Please understand if you use this it is at your own risk and can break at any time.
I will try to support and make improvements as needed. Please if you have any issues
file an issue on this Github Page.

# Contact
You can contact me on [Discord](http://discord.gg/outcast) or
[Twitter](http://twitter.com/OutcastMakerLab)
