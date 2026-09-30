## psm

> `/usr/bin/psm`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`

```diff

-2383.0.14.0.1
-  __TEXT.__text: 0xb6d4
+2383.0.22.0.2
+  __TEXT.__text: 0xb7b8
   __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__const: 0x121c
-  __TEXT.__cstring: 0x28b7
+  __TEXT.__const: 0x1274
+  __TEXT.__cstring: 0x28d5
   __TEXT.__unwind_info: 0x300
   __DATA_CONST.__const: 0x1768
   __DATA_CONST.__cfstring: 0x140
   __DATA_CONST.__auth_got: 0x3f8
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA.__data: 0x768
+  __DATA.__data: 0x790
   __DATA.__common: 0x21
   __DATA.__bss: 0x468
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS
   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/Versions/A/AppleKeyStore
   - /usr/lib/libSystem.B.dylib
-  Functions: 333
+  Functions: 336
   Symbols:   143
-  CStrings:  383
+  CStrings:  384
 
CStrings:
+ "aks_get_convenience_bio_state"
```
