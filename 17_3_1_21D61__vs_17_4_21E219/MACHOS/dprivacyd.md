## dprivacyd

> `/usr/libexec/dprivacyd`

```diff

-485.80.4.0.0
+558.0.0.0.0
   __TEXT.__text: 0x48
   __TEXT.__auth_stubs: 0x40
   __TEXT.__objc_stubs: 0x20

   __TEXT.__unwind_info: 0x48
   __DATA_CONST.__auth_got: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x8
   __DATA.__objc_selrefs: 0x8
-  __DATA.__objc_classrefs: 0x8
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy
   - /usr/lib/libSystem.B.dylib

```
