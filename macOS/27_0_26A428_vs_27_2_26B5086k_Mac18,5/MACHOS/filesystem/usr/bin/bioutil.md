## bioutil

> `/usr/bin/bioutil`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-577.0.0.0.0
-  __TEXT.__text: 0x12e94
+578.40.6.0.0
+  __TEXT.__text: 0x12e1c
   __TEXT.__auth_stubs: 0x370
   __TEXT.__objc_stubs: 0x6a0
   __TEXT.__const: 0x131
   __TEXT.__gcc_except_tab: 0x3e4
   __TEXT.__cstring: 0x3269
-  __TEXT.__oslogstring: 0x209
+  __TEXT.__oslogstring: 0x20c
   __TEXT.__objc_methname: 0x470
   __TEXT.__unwind_info: 0x4c8
   __DATA_CONST.__const: 0xa0

   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_selrefs: 0x1a8
   __DATA.__data: 0x1c2
-  __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/Versions/A/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 453
+  Functions: 452
   Symbols:   82
   CStrings:  398
 
CStrings:
+ "AssertMacros: %s (value = 0x%lx), version: BiometricKit-578.40.6~27, %s file: %s, line: %d\n\n"
- "AssertMacros: %s (value = 0x%lx), version: BiometricKit-577~3086, %s file: %s, line: %d\n\n"
```
