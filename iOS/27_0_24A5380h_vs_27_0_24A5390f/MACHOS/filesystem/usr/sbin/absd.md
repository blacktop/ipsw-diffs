## absd

> `/usr/sbin/absd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__auth_got`

```diff

 0.0.0.0.0
-  __TEXT.__text: 0x22e9ac
+  __TEXT.__text: 0x243de8
   __TEXT.__auth_stubs: 0x1f0
   __TEXT.__cstring: 0x31
-  __TEXT.__const: 0x3fcd0
-  __TEXT.__unwind_info: 0x358
-  __TEXT.__eh_frame: 0x178
-  __DATA_CONST.__const: 0x135e8
+  __TEXT.__const: 0x3bf50
+  __TEXT.__unwind_info: 0x480
+  __TEXT.__eh_frame: 0xd0
+  __DATA_CONST.__const: 0x13c50
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__auth_got: 0xf8
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA.__data: 0xa18
-  __DATA.__common: 0x14b4
+  __DATA.__data: 0xce0
+  __DATA.__common: 0x14c0
   __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  Functions: 239
+  Functions: 282
   Symbols:   94
   CStrings:  4
 
```
