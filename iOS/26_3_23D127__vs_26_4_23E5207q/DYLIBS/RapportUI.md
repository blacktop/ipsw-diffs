## RapportUI

> `/System/Library/PrivateFrameworks/RapportUI.framework/RapportUI`

```diff

-716.400.31.0.0
-  __TEXT.__text: 0x2a1c
-  __TEXT.__auth_stubs: 0x310
+716.500.91.0.0
+  __TEXT.__text: 0x328c
+  __TEXT.__auth_stubs: 0x360
   __TEXT.__objc_methlist: 0xa14
   __TEXT.__const: 0x198
   __TEXT.__cstring: 0x270
-  __TEXT.__unwind_info: 0x150
+  __TEXT.__unwind_info: 0x240
   __TEXT.__objc_classname: 0xd5
   __TEXT.__objc_methname: 0x14db
   __TEXT.__objc_methtype: 0x2a7

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x6b8
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x190
+  __AUTH_CONST.__auth_got: 0x1b8
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x1e0
   __AUTH_CONST.__objc_const: 0x12b8

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 36C1F96D-CFE1-36DC-AE49-70DA582380EA
+  UUID: 86837AD6-9DF3-33C6-9159-BFBE732A711A
   Functions: 160
-  Symbols:   576
+  Symbols:   581
   CStrings:  412
 
Symbols:
+ _objc_release_x2
+ _objc_release_x25
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x22
+ _objc_retain_x23
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
Functions:
~ -[RPPairingManagerUIController init] : 92 -> 100
~ -[RPPairingManagerUIController setDispatchQueue:] : 12 -> 64
~ -[RPPairingManagerUIController setPresentingViewController:] : 12 -> 64
~ -[RPPairingUIController init] : 92 -> 100
~ -[RPPairingUIController setPresentingViewController:] : 12 -> 64
~ -[RPPairingUIController setDispatchQueue:] : 12 -> 64
~ -[RPPINEntryView awakeFromNib] : 576 -> 584
~ -[RPPINEntryView setText:] : 96 -> 100
~ -[RPPINEntryView _updateFields] : 800 -> 828
~ -[RPPINEntryView setLabels:] : 20 -> 80
~ -[RPPINEntryView setLabel1:] : 20 -> 80
~ -[RPPINEntryView setLabel2:] : 20 -> 80
~ -[RPPINEntryView setLabel3:] : 20 -> 80
~ -[RPPINEntryView setLabel4:] : 20 -> 80
~ -[RPPINEntryView setLabel5:] : 20 -> 80
~ -[RPPINEntryView setLabel6:] : 20 -> 80
~ -[RPPINEntryView setLabel7:] : 20 -> 80
~ -[RPPINEntryView setLabel8:] : 20 -> 80
~ -[RPPINEntryView setWells:] : 20 -> 80
~ -[RPPINEntryView setWell1:] : 20 -> 80
~ -[RPPINEntryView setWell2:] : 20 -> 80
~ -[RPPINEntryView setWell3:] : 20 -> 80
~ -[RPPINEntryView setWell4:] : 20 -> 80
~ -[RPPINEntryView setWell5:] : 20 -> 80
~ -[RPPINEntryView setWell6:] : 20 -> 80
~ -[RPPINEntryView setWell7:] : 20 -> 80
~ -[RPPINEntryView setWell8:] : 20 -> 80
~ -[RPPINEntryView setWellFocusColor:] : 20 -> 80
~ +[RPPairingPromptViewController instantiateViewController] : 156 -> 168
~ -[RPPairingPromptViewController viewWillAppear:] : 212 -> 216
~ ___48-[RPPairingPromptViewController viewWillAppear:]_block_invoke : 144 -> 156
~ -[RPPairingPromptViewController handlePINEntered:] : 228 -> 232
~ -[RPPairingPromptViewController updateWithFlags:throttleSeconds:] : 480 -> 488
~ -[RPPairingPromptViewController _retryTimer] : 296 -> 284
~ -[RPPairingPromptViewController setCancelButton:] : 20 -> 80
~ -[RPPairingPromptViewController setTitleLabel:] : 20 -> 80
~ -[RPPairingPromptViewController setSubTitleLabel:] : 20 -> 80
~ -[RPPairingPromptViewController setPinEntryView:] : 20 -> 80
~ -[RPPairingPromptViewController setProgressSpinner:] : 20 -> 80
~ -[RPPairingPromptViewController setProgressLabel:] : 20 -> 80
~ +[RPPairingShowViewController instantiateViewController] : 156 -> 168
~ -[RPPairingShowViewController viewWillAppear:] : 120 -> 124
~ -[RPPairingShowViewController _updatePasswordUI] : 608 -> 612
~ -[RPPairingShowViewController setCancelButton:] : 20 -> 80
~ -[RPPairingShowViewController setTitleLabel:] : 20 -> 80
~ -[RPPairingShowViewController setSubTitleLabel:] : 20 -> 80
~ -[RPPairingShowViewController setVerificationCodeLabel:] : 20 -> 80
~ _RPUILocalizedString : 132 -> 148
~ ___RPUILocalizedString_block_invoke : 72 -> 76
~ _RPUILocalizedStringF : 64 -> 68
~ _RPUILocalizedStringV : 136 -> 152
~ -[UIView(RPUIViewExtensions) borderColor] : 80 -> 84
~ -[UIView(RPUIViewExtensions) setBorderColor:] : 108 -> 112
~ -[UIView(RPUIViewExtensions) borderWidth] : 72 -> 76
~ -[UIView(RPUIViewExtensions) setBorderWidth:] : 188 -> 200
~ -[UIView(RPUIViewExtensions) shadowUIColor] : 80 -> 84
~ -[UIView(RPUIViewExtensions) setShadowUIColor:] : 108 -> 112
~ _RPImageForDeviceModel : 528 -> 564

```
