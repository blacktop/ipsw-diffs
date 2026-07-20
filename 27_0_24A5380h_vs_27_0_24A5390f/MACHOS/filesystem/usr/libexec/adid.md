## adid

> `/usr/libexec/adid`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__oslogstring`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`

```diff

-21.1.0.0.0
-  __TEXT.__text: 0x24ac34
+21.3.0.0.0
+  __TEXT.__text: 0x256cd0
   __TEXT.__auth_stubs: 0x10
   __TEXT.__const: 0x58330
   __TEXT.__oslogstring: 0xd2
   __TEXT.__cstring: 0xf
-  __TEXT.__unwind_info: 0x180
+  __TEXT.__unwind_info: 0x1d8
   __TEXT.__eh_frame: 0x50
-  __DATA_CONST.__const: 0x14420
+  __DATA_CONST.__const: 0x14b58
   __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__auth_got: 0x8
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA.__data: 0xfd0
-  __DATA.__common: 0x198
+  __DATA.__data: 0x10d0
+  __DATA.__common: 0x190
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  Functions: 91
+  Functions: 106
   Symbols:   128
   CStrings:  32
 
```
