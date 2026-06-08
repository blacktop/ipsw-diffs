## com.apple.FontServices.FontProviderLoader

> `/System/Library/PrivateFrameworks/FontServices.framework/XPCServices/com.apple.FontServices.FontProviderLoader.xpc/com.apple.FontServices.FontProviderLoader`

```diff

-157.4.0.2.0
-  __TEXT.__text: 0x2568
-  __TEXT.__auth_stubs: 0x3f0
+167.0.0.0.0
+  __TEXT.__text: 0x2444
+  __TEXT.__auth_stubs: 0x430
   __TEXT.__objc_stubs: 0x9a0
   __TEXT.__objc_methlist: 0x428
   __TEXT.__const: 0x60
-  __TEXT.__objc_classname: 0xc9
+  __TEXT.__objc_classname: 0xc5
   __TEXT.__objc_methname: 0xd6b
   __TEXT.__objc_methtype: 0x3e5
-  __TEXT.__cstring: 0x402
-  __TEXT.__unwind_info: 0xe8
-  __DATA_CONST.__auth_got: 0x200
-  __DATA_CONST.__got: 0x100
+  __TEXT.__cstring: 0x405
+  __TEXT.__unwind_info: 0xf0
   __DATA_CONST.__const: 0x1b8
   __DATA_CONST.__cfstring: 0x400
   __DATA_CONST.__objc_classlist: 0x18

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__auth_got: 0x220
+  __DATA_CONST.__got: 0x100
   __DATA.__objc_const: 0x578
   __DATA.__objc_selrefs: 0x460
   __DATA.__objc_ivar: 0x10

   - /System/Library/PrivateFrameworks/UserManagement.framework/UserManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 545596FB-E11B-399A-AA62-0ACCC532597F
+  UUID: 008859F6-7789-3741-B1B9-44219E2883FA
   Functions: 37
-  Symbols:   122
+  Symbols:   126
   CStrings:  273
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x26
CStrings:
+ "FontProvider \"%@\" tried to install fonts in the background.  Installation cancelled."
+ "FontProvider couldn't get processInfo for \"%@\".  Error = %@"
+ "couldn't get applicationBundlePath for %@"
- "FontProvider \"%@\" tried to install fonts in the background.  Installaion cancelled."
- "FontProvider couldn't get processInfor for \"%@\".  Error = %@"
- "couldn't get applicationBundlePath foor %@"

```
