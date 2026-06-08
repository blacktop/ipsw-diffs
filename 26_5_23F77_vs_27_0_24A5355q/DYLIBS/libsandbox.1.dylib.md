## libsandbox.1.dylib

> `/usr/lib/libsandbox.1.dylib`

```diff

-2680.120.12.0.0
-  __TEXT.__text: 0x1734
-  __TEXT.__auth_stubs: 0x160
+3033.0.0.0.1
+  __TEXT.__text: 0x182c
   __TEXT.__const: 0x20
   __TEXT.__oslogstring: 0x1f
-  __TEXT.__cstring: 0x16e
-  __TEXT.__unwind_info: 0xe0
-  __DATA_CONST.__got: 0x18
+  __TEXT.__cstring: 0x1c2
+  __TEXT.__unwind_info: 0xe8
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x20
-  __AUTH_CONST.__auth_got: 0xb0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__auth_got: 0x0
   - /usr/lib/libMatch.1.dylib
   - /usr/lib/libSystem.B.dylib
-  UUID: D37545FB-664F-338E-B7AA-F63E7CFE2ADF
-  Functions: 48
-  Symbols:   95
-  CStrings:  19
+  UUID: D878385A-8953-37C6-97DC-D07A190B6201
+  Functions: 50
+  Symbols:   97
+  CStrings:  22
 
Symbols:
+ _sb_packbuff_extend
+ _sb_packbuff_pack_item.cold.3
+ _sb_packbuff_pack_string.cold.1
- ___stack_chk_fail
- ___stack_chk_guard
- _sb_packbuff_realloc
CStrings:
+ "C7CDAAD8-33DB-4677-8224-7E1A0221C01C"
+ "item_type != SB_PACKBUFF_ITEM_TYPE_STRING"
+ "sb_packbuff_pack_string"
+ "str_value != NULL"
- "21F2AA5D-510A-4585-978E-A4E40C7DF520"

```
