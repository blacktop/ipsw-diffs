## appprotectiond

> `/usr/libexec/appprotectiond`

```diff

-30.0.0.0.0
-  __TEXT.__text: 0x10
+32.0.0.0.0
+  __TEXT.__text: 0x34
   __TEXT.__auth_stubs: 0x10
+  __TEXT.__objc_stubs: 0x20
   __TEXT.__info_plist: 0x45a
+  __TEXT.__objc_methname: 0x21
   __TEXT.__unwind_info: 0x58
-  __DATA_CONST.__auth_got: 0x8
+  __DATA_CONST.__auth_got: 0x10
+  __DATA_CONST.__got: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA.__objc_selrefs: 0x8
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AppProtection.framework/AppProtection
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Symbols:   3
+  Symbols:   5
   Functions: 1
 

```
