## libsandbox.1.dylib

> `/usr/lib/libsandbox.1.dylib`

```diff

-  __TEXT.__text: 0x31d04
+  __TEXT.__text: 0x31eb4
   __TEXT.__const: 0x15501
   __TEXT.__cstring: 0x1f3a4
   __TEXT.__oslogstring: 0x4f1
-  __TEXT.__unwind_info: 0x8d8
+  __TEXT.__unwind_info: 0x8c8
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0xd4b0
   __DATA_CONST.__got: 0x0
Sections:
~ __TEXT.__cstring : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __DATA.__data : content changed
Symbols:
+ _sb_byteset_get_hash
+ _sb_hash_finalize
- _can_combine_conjunction
- _can_combine_disjunction
CStrings:
+ "1E6E9E4D-48D5-4ECF-9960-348479364C5B"
- "1D40CEF4-AF1B-4A4E-BEEB-79D1637A8255"

```
