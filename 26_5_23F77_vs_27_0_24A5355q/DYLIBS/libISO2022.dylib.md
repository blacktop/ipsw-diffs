## libISO2022.dylib

> `/usr/lib/i18n/libISO2022.dylib`

```diff

-115.120.2.0.0
-  __TEXT.__text: 0x178c
-  __TEXT.__auth_stubs: 0xb0
+121.0.0.0.0
+  __TEXT.__text: 0x1888
   __TEXT.__const: 0x470
-  __TEXT.__cstring: 0x80
-  __TEXT.__unwind_info: 0x88
-  __DATA_CONST.__got: 0x8
+  __TEXT.__cstring: 0xd4
+  __TEXT.__unwind_info: 0x90
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x110
-  __AUTH_CONST.__auth_got: 0x58
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__data: 0x58
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libiconv.2.dylib
-  UUID: 7314AE92-79D1-3340-A1F8-458A3D855E4A
-  Functions: 15
-  Symbols:   44
-  CStrings:  28
+  UUID: 714FBE4C-A23F-3EA0-9892-473236EA12D6
+  Functions: 17
+  Symbols:   49
+  CStrings:  32
 
Symbols:
+ __ISO2022_sputwchar.cold.1
+ __ISO2022_sputwchar.cold.2
+ ___assert_rtn
Functions:
~ __citrus_ISO2022_stdenc_init : 1308 -> 1312
~ __citrus_ISO2022_stdenc_put_state_reset : 152 -> 196
~ __citrus_ISO2022_mbrtowc_priv : 788 -> 792
~ __ISO2022_sgetwchar : 1224 -> 1228
~ __citrus_ISO2022_wcrtomb_priv : 140 -> 184
~ __ISO2022_sputwchar : 1504 -> 1568
CStrings:
+ "(p - tmp) + i <= sizeof(tmp)"
+ "0 && \"Unreachable\""
+ "_ISO2022_sputwchar"
+ "citrus_iso2022.c"

```
