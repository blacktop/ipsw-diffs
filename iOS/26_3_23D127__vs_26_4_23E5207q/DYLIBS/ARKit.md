## ARKit

> `/System/Library/Frameworks/ARKit.framework/ARKit`

```diff

-738.80.1.0.0
-  __TEXT.__text: 0xb08
-  __TEXT.__auth_stubs: 0x1b0
+738.100.1.0.0
+  __TEXT.__text: 0xb54
+  __TEXT.__auth_stubs: 0x1a0
   __TEXT.__const: 0x40
   __TEXT.__cstring: 0x111
   __TEXT.__oslogstring: 0xb

   __DATA_CONST.__const: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x58
-  __AUTH_CONST.__auth_got: 0xe0
+  __AUTH_CONST.__auth_got: 0xd8
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x260
   __DATA.__bss: 0x20

   - /System/Library/PrivateFrameworks/ARKitUI.framework/ARKitUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 18076E19-B725-335B-8980-543B9087D670
+  UUID: 78CC28EF-318C-3F17-B90B-01C755CC80B4
   Functions: 26
-  Symbols:   96
+  Symbols:   95
   CStrings:  43
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x21
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
Functions:
~ ___ARFileDescriptorIsTTY_block_invoke : 128 -> 140
~ __printFormat : 256 -> 260
~ __ARLogGeneral : 68 -> 84
~ __printError : 224 -> 232
~ __printInfo : 224 -> 232
~ __printWarning : 224 -> 232
~ _ARPrintToiTerm : 132 -> 140
~ _ARKitBuildVersionString : 132 -> 144

```
