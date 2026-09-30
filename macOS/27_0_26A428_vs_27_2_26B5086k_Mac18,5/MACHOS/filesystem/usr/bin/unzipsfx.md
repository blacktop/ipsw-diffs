## unzipsfx

> `/usr/bin/unzipsfx`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-33.0.0.0.0
-  __TEXT.__text: 0xbc5c
-  __TEXT.__auth_stubs: 0x450
+35.0.0.0.0
+  __TEXT.__text: 0xbd7c
+  __TEXT.__auth_stubs: 0x470
   __TEXT.__const: 0x12bb
-  __TEXT.__cstring: 0x427
-  __TEXT.__unwind_info: 0x188
-  __DATA_CONST.__auth_got: 0x228
+  __TEXT.__cstring: 0x42f
+  __TEXT.__unwind_info: 0x190
+  __DATA_CONST.__auth_got: 0x238
   __DATA_CONST.__got: 0x28
   __DATA.__data: 0x30
   __DATA.__common: 0xccc80
   - /usr/lib/libSystem.B.dylib
-  Functions: 68
-  Symbols:   272
-  CStrings:  58
+  Functions: 69
+  Symbols:   275
+  CStrings:  59
 
Symbols:
+ _asprintf
+ _faccessat
+ extract_or_test_files
Functions:
~ _extract_or_test_files : 9920 -> 10124
+ extract_or_test_files.cold.1
CStrings:
+ "%.*s/%s"
```
