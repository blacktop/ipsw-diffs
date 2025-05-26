## PrivacySettingsUI

> `/System/Library/PrivateFrameworks/Settings/PrivacySettingsUI.framework/PrivacySettingsUI`

```diff

-1160.3.3.1.0
-  __TEXT.__text: 0x440e0
+1160.5.6.100.0
+  __TEXT.__text: 0x44bb0
   __TEXT.__auth_stubs: 0xbc0
   __TEXT.__objc_methlist: 0x2d5c
   __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0x898
-  __TEXT.__cstring: 0x56b1
-  __TEXT.__dlopen_cstrs: 0x7fa
-  __TEXT.__oslogstring: 0x1630
+  __TEXT.__gcc_except_tab: 0x8a8
+  __TEXT.__cstring: 0x57c7
+  __TEXT.__dlopen_cstrs: 0x84a
+  __TEXT.__oslogstring: 0x16aa
   __TEXT.__objc_const_ax: 0xe8
-  __TEXT.__unwind_info: 0xe7c
+  __TEXT.__unwind_info: 0xea0
   __TEXT.__objc_classname: 0x787
-  __TEXT.__objc_methname: 0xa38c
+  __TEXT.__objc_methname: 0xa3ec
   __TEXT.__objc_methtype: 0xd6e
-  __TEXT.__objc_stubs: 0x88a0
-  __DATA_CONST.__got: 0x470
-  __DATA_CONST.__const: 0x1050
+  __TEXT.__objc_stubs: 0x8900
+  __DATA_CONST.__got: 0x488
+  __DATA_CONST.__const: 0x10a0
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x42b8
-  __DATA_CONST.__objc_selrefs: 0x2748
+  __DATA_CONST.__objc_selrefs: 0x2760
+  __DATA_CONST.__objc_classrefs: 0x4a8
+  __DATA_CONST.__objc_superrefs: 0x170
   __DATA_CONST.__objc_arraydata: 0x178
-  __AUTH_CONST.__const: 0x4a0
-  __AUTH_CONST.__cfstring: 0x4f00
+  __AUTH_CONST.__const: 0x4c0
+  __AUTH_CONST.__cfstring: 0x50a0
   __AUTH_CONST.__objc_const: 0x1430
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_dictobj: 0x50

   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__auth_got: 0x5f0
   __AUTH.__objc_data: 0xb40
-  __DATA.__objc_classrefs: 0x4a8
-  __DATA.__objc_superrefs: 0x170
   __DATA.__objc_ivar: 0x364
   __DATA.__objc_const_ax: 0x0
   __DATA.__data: 0x3c0
-  __DATA.__bss: 0x280
+  __DATA.__bss: 0x2a0
   __DATA_DIRTY.__objc_data: 0x5f0
   __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
-  - /System/Library/Frameworks/ExposureNotification.framework/ExposureNotification
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/ImageCaptureCore.framework/ImageCaptureCore

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1364
-  Symbols:   5257
-  CStrings:  2824
+  Functions: 1373
+  Symbols:   5289
+  CStrings:  2848
 
Symbols:
+ GCC_except_table22
+ GCC_except_table24
+ _PUITCCAccessControllerPromptDetailKey
+ _PUITCCAccessControllerPromptTitleKey
+ _SEServiceLibraryCore.frameworkLibrary
+ ___49-[PUITCCAccessController setAccess:forSpecifier:]_block_invoke
+ ___49-[PUITCCAccessController setAccess:forSpecifier:]_block_invoke.94
+ ___49-[PUITCCAccessController setAccess:forSpecifier:]_block_invoke_2
+ ___SEServiceLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32bs_e23_v16?0"UIAlertAction"8ls32l8
+ ___block_literal_global.91
+ ___getSESSettingsEligiblityClass_block_invoke
+ ___getSESSettingsEligiblityClass_block_invoke.cold.1
+ ___isGreenTeaSKU_block_invoke
+ _audit_stringSEService
+ _calloc
+ _getSESSettingsEligiblityClass
+ _getSESSettingsEligiblityClass.softClass
+ _isGreenTeaSKU.deviceIsChinaSKU
+ _isGreenTeaSKU.once
+ _kTCCServiceContactlessAccess
+ _kTCCServiceSecureElementAccess
+ _kTCCServiceWebBrowserPublicKeyCredential
+ _objc_msgSend$accessCount
+ _objc_msgSend$isContactlessTCCServiceEligible
+ _objc_msgSend$isSecureElementTCCServiceEligible
- GCC_except_table23
- _malloc_type_calloc
CStrings:
+ "%@ (%lu)"
+ "%s: not removing CONTACTLESS_NFC"
+ "%s: not removing SECURE_ELEMENT"
+ "%s: removing CONTACTLESS_NFC"
+ "%s: removing SECURE_ELEMENT"
+ "-[PUIPrivacyController specifiers]"
+ "CONTACTLESS_NFC"
+ "PASSKEYS"
+ "PUITCCAccessControllerPromptDetailKey"
+ "PUITCCAccessControllerPromptTitleKey"
+ "Privacy/WalletPrivacySettings"
+ "SECURE_ELEMENT"
+ "SESSettingsEligiblity"
+ "T@\"NSString\",?,R,C"
+ "TCC_ALERT_CANCEL"
+ "TCC_ALERT_TURN_OFF"
+ "WALLET"
+ "WILLOW"
+ "Wallet"
+ "accessCount"
+ "green-tea"
+ "isContactlessTCCServiceEligible"
+ "isSecureElementTCCServiceEligible"
+ "softlink:r:path:/System/Library/PrivateFrameworks/SEService.framework/SEService"

```
