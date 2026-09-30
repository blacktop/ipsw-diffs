## WatchListKit

> `/System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit`

```diff

-907.0.2.0.0
-  __TEXT.__text: 0x67264
+907.10.4.0.1
+  __TEXT.__text: 0x67330
   __TEXT.__auth_stubs: 0x810
   __TEXT.__objc_methlist: 0x7044
   __TEXT.__const: 0x1a4
-  __TEXT.__cstring: 0x7b5c
+  __TEXT.__cstring: 0x7be5
   __TEXT.__oslogstring: 0x6327
   __TEXT.__gcc_except_tab: 0x11b0
   __TEXT.__unwind_info: 0x1de8
   __TEXT.__objc_classname: 0x1321
-  __TEXT.__objc_methname: 0x1072d
+  __TEXT.__objc_methname: 0x1074b
   __TEXT.__objc_methtype: 0x1da5
-  __TEXT.__objc_stubs: 0x9d80
+  __TEXT.__objc_stubs: 0x9da0
   __DATA_CONST.__got: 0x8f8
   __DATA_CONST.__const: 0x2778
   __DATA_CONST.__objc_classlist: 0x560
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3938
+  __DATA_CONST.__objc_selrefs: 0x3940
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x4b0
   __DATA_CONST.__objc_arraydata: 0x628
   __AUTH_CONST.__auth_got: 0x418
   __AUTH_CONST.__const: 0xe80
-  __AUTH_CONST.__cfstring: 0xa420
+  __AUTH_CONST.__cfstring: 0xa460
   __AUTH_CONST.__objc_const: 0x11b90
   __AUTH_CONST.__objc_intobj: 0x378
   __AUTH_CONST.__objc_dictobj: 0x190

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F9966ABE-ED7C-3C57-8C9D-4BF1E833B718
+  UUID: 9DE5CB95-22A6-38EC-BE55-6627C5BEA33F
   Functions: 2753
-  Symbols:   10090
-  CStrings:  6458
+  Symbols:   10091
+  CStrings:  6463
 
Symbols:
+ _objc_msgSend$acknowledgementNeededForPrivacyIdentifier:account:
+ _objc_msgSend$setAccountIdentifier:
- _objc_msgSend$acknowledgementNeededForPrivacyIdentifier:
Functions:
~ -[WLKUserEnvironment init] : 908 -> 932
~ +[WLKNetworkRequestUtilities isGDPRAccepted] : 188 -> 224
~ -[_WLKAppInstallSession _doPurchaseWithAppAdamID:offerBuyParams:] : 976 -> 1120
CStrings:
+ "WLKAppInstaller - No account or DSID found, letting ASD use default"
+ "WLKAppInstaller - Setting account identifier (DSID) for purchase: %@"
+ "acknowledgementNeededForPrivacyIdentifier:account:"
+ "setAccountIdentifier:"
- "acknowledgementNeededForPrivacyIdentifier:"

```
