## unzip

> `/usr/bin/unzip`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-33.0.0.0.0
-  __TEXT.__text: 0x17144
-  __TEXT.__auth_stubs: 0x4d0
+35.0.0.0.0
+  __TEXT.__text: 0x171cc
+  __TEXT.__auth_stubs: 0x4f0
   __TEXT.__const: 0x4a99
-  __TEXT.__cstring: 0x2fb4
-  __TEXT.__unwind_info: 0x208
+  __TEXT.__cstring: 0x2fbc
+  __TEXT.__unwind_info: 0x210
   __DATA_CONST.__const: 0x9e0
-  __DATA_CONST.__auth_got: 0x268
+  __DATA_CONST.__auth_got: 0x278
   __DATA_CONST.__got: 0x28
   __DATA.__data: 0x38
   __DATA.__common: 0xf0cd0
   - /usr/lib/libSystem.B.dylib
-  Functions: 99
-  Symbols:   638
-  CStrings:  325
+  Functions: 100
+  Symbols:   641
+  CStrings:  326
 
Symbols:
+ _asprintf
+ _faccessat
+ extract_or_test_files
Functions:
~ _extract_or_test_files : 15220 -> 15272
+ extract_or_test_files.cold.1
CStrings:
+ "%.*s/%s"
+ "Apple LLVM 21.0.0 (clang-2100.3.34.1) [+internal-os]"
- "Apple LLVM 21.0.0 (clang-2100.3.31.1) [+internal-os]"
```
