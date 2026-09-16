## SoftwareUpdateController

> `/System/Library/PrivateFrameworks/SoftwareUpdateController.framework/SoftwareUpdateController`

```diff

-196.0.1.0.0
-  __TEXT.__text: 0xeff8
-  __TEXT.__objc_methlist: 0x158c
-  __TEXT.__const: 0xb0
-  __TEXT.__cstring: 0x3b96
+201.40.1.0.0
+  __TEXT.__text: 0xf020
+  __TEXT.__objc_methlist: 0x1594
+  __TEXT.__const: 0xc0
+  __TEXT.__cstring: 0x3bad
   __TEXT.__oslogstring: 0xcb
   __TEXT.__gcc_except_tab: 0x48
   __TEXT.__unwind_info: 0x410

   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf30
+  __DATA_CONST.__objc_selrefs: 0xf38
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__got: 0x230

   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x3c0
   __DATA.__objc_ivar: 0x1c8
-  __DATA.__data: 0x348
+  __DATA.__data: 0x350
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 425
-  Symbols:   1293
-  CStrings:  462
+  Functions: 426
+  Symbols:   1296
+  CStrings:  463
 
Symbols:
+ -[SUControllerManager installUpdate:rediscoverNetwork:]
+ _SUControllerMessageManagerRediscoverNetworkKey
+ _objc_msgSend$installUpdate:rediscoverNetwork:
Functions:
~ -[SUControllerManager installUpdate:] : 180 -> 8
+ -[SUControllerManager installUpdate:rediscoverNetwork:]
CStrings:
+ "RaveBSeed"
+ "RediscoverNetwork"
- "Rave"
```
