## OpenDirectoryConfigUI

> `/System/Library/PrivateFrameworks/OpenDirectoryConfigUI.framework/Versions/A/OpenDirectoryConfigUI`

```diff

 91.0.0.0.0
-  __TEXT.__text: 0x875c
+  __TEXT.__text: 0x874c
   __TEXT.__auth_stubs: 0x240
-  __TEXT.__objc_methlist: 0xc5c
+  __TEXT.__objc_methlist: 0xf44
   __TEXT.__cstring: 0xae9
   __TEXT.__const: 0x18
-  __TEXT.__unwind_info: 0x2b8
+  __TEXT.__unwind_info: 0x2c0
   __TEXT.__objc_classname: 0x262
   __TEXT.__objc_methname: 0x2e35
   __TEXT.__objc_methtype: 0xa8f

   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb30
+  __DATA_CONST.__objc_selrefs: 0xc90
   __DATA_CONST.__objc_superrefs: 0x80
   __AUTH_CONST.__auth_got: 0x128
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__cfstring: 0xda0
-  __AUTH_CONST.__objc_const: 0x28e8
+  __AUTH_CONST.__objc_const: 0x2380
   __AUTH.__objc_data: 0x550
   __DATA.__objc_ivar: 0x208
   __DATA.__data: 0x2a0

   - /System/Library/PrivateFrameworks/ServerInformation.framework/Versions/A/ServerInformation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A5FE254F-2426-3E18-9EF9-3916D81D0609
-  Functions: 264
-  Symbols:   972
+  UUID: DF04DBF9-8277-33C9-BD7C-F1FC9B7594BE
+  Functions: 266
+  Symbols:   974
   CStrings:  913
 
Symbols:
+ +[XSDomainNameFormatter separatorCharacters].cold.1
+ +[XSDomainNameFormatter validCharacters].cold.1
Functions:
~ -[ODCServersViewController(PrivateMethods) foundServers:] : 1324 -> 1320
~ -[ODCAddServerSheetController(PrivateMethods) didFinishGettingServerInfo:] : 676 -> 680
~ -[ODCSummaryViewController(PrivateMethods) foundServers:] : 1200 -> 1164
~ -[ODCViewControllerBase setAuthView:] : 140 -> 128
~ -[XSBonjourComboBox setDisplaysResolvedAddresses:] : 88 -> 92
~ -[XSBonjourComboBox stopBrowsing:] : 112 -> 116
~ -[XSBonjourComboBox netServiceBrowser:didNotSearch:] : 24 -> 28
~ +[XSDomainNameFormatter validCharacters] : 68 -> 56
~ +[XSDomainNameFormatter separatorCharacters] : 68 -> 56
~ -[XSDisablingTextField setEnabled:] : 184 -> 188

```
