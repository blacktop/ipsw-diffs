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
   - /usr/lib/libobjc.A.dylib
-  UUID: 1260847D-1066-3193-AAD0-F4BCC33043DF
+  UUID: 50577859-C643-3FD7-9D3B-6A6941EFA431
   Functions: 1
   Symbols:   8
   CStrings:  1

```
