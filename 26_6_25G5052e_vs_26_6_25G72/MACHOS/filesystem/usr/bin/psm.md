## psm

> `/usr/bin/psm`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`

```diff

-2155.160.11.0.0
-  __TEXT.__text: 0xb2b0
+2155.160.13.0.1
+  __TEXT.__text: 0xb2b8
   __TEXT.__auth_stubs: 0x7f0
-  __TEXT.__const: 0x119c
-  __TEXT.__cstring: 0x278a
+  __TEXT.__const: 0x1204
+  __TEXT.__cstring: 0x27ac
   __TEXT.__unwind_info: 0x2d8
   __DATA_CONST.__auth_got: 0x3f8
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x1748
+  __DATA_CONST.__const: 0x1768
   __DATA_CONST.__cfstring: 0x140
-  __DATA.__data: 0x730
+  __DATA.__data: 0x760
   __DATA.__common: 0x21
   __DATA.__bss: 0x468
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS
   - /System/Library/PrivateFrameworks/AppleKeyStore.framework/Versions/A/AppleKeyStore
   - /usr/lib/libSystem.B.dylib
-  Functions: 321
+  Functions: 325
   Symbols:   143
-  CStrings:  377
+  CStrings:  379
 
CStrings:
+ "proposed"
+ "unmanaged-system-wrapped"
```
