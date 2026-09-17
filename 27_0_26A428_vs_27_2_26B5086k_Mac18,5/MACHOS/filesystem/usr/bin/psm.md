## psm

> `/usr/bin/psm`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`

```diff

-2383.1.1.0.0
-  __TEXT.__text: 0xb644
+2383.40.14.0.0
+  __TEXT.__text: 0xb790
   __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__const: 0x1274
+  __TEXT.__const: 0x12d4
   __TEXT.__cstring: 0x28d5
   __TEXT.__unwind_info: 0x418
   __DATA_CONST.__const: 0x1768

   __DATA_CONST.__auth_got: 0x3f8
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA.__data: 0x790
+  __DATA.__data: 0x7b8
   __DATA.__common: 0x21
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS
   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/Versions/A/AppleKeyStore
   - /usr/lib/libSystem.B.dylib
-  Functions: 336
+  Functions: 335
   Symbols:   143
   CStrings:  384
 
```
