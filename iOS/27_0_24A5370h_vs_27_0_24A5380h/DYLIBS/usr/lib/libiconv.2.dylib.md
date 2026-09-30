## libiconv.2.dylib

> `/usr/lib/libiconv.2.dylib`

```diff

-  __TEXT.__text: 0x62e4
+  __TEXT.__text: 0x62a4
   __TEXT.__cstring: 0x3a3
   __TEXT.__const: 0x49
   __TEXT.__unwind_info: 0x1d0

   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__auth_got: 0x178
+  __AUTH.__data: 0x58
   __DATA.__data: 0x3c
-  __DATA_DIRTY.__data: 0x2b0
+  __DATA_DIRTY.__data: 0x258
   __DATA_DIRTY.__bss: 0x768
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcharset.1.dylib
Sections:
~ __TEXT.__unwind_info : content changed
~ __AUTH_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ __citrus_bcs_strtol : 732 -> 708
~ __citrus_bcs_strtoul : 640 -> 608
~ __citrus_bcs_convert_to_lower : 48 -> 40
~ __citrus_bcs_convert_to_upper : 52 -> 44
~ __citrus_db_factory_serialize : 852 -> 844
~ __citrus_prop_parse_variable : 908 -> 924

```
