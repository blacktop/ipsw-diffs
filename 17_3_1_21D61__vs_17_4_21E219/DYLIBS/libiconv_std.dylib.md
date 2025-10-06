## libiconv_std.dylib

> `/usr/lib/i18n/libiconv_std.dylib`

```diff

-92.80.2.0.0
-  __TEXT.__text: 0x17ec
-  __TEXT.__auth_stubs: 0xd0
-  __TEXT.__cstring: 0x141
-  __TEXT.__unwind_info: 0x8c
-  __DATA_CONST.__got: 0x8
-  __AUTH_CONST.__auth_got: 0x68
+99.0.0.0.0
+  __TEXT.__text: 0x1ee8
+  __TEXT.__auth_stubs: 0xf0
+  __TEXT.__cstring: 0x1c6
+  __TEXT.__unwind_info: 0x90
+  __DATA_CONST.__got: 0x10
+  __AUTH_CONST.__auth_got: 0x78
   __AUTH.__data: 0x28
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libiconv.2.dylib
-  UUID: A593B82F-40C9-357D-AB37-A14B1BF48736
-  Functions: 24
-  Symbols:   60
-  CStrings:  14
+  UUID: 312CC9C0-6771-3CE2-BE20-E38003B56209
+  Functions: 29
+  Symbols:   73
+  CStrings:  21
 
Symbols:
+ ___mb_cur_max
+ __citrus_iconv_std_iconv_convert.cold.12
+ __citrus_iconv_std_iconv_convert.cold.13
+ __citrus_iconv_std_iconv_convert.cold.14
+ __citrus_iconv_std_iconv_convert.cold.15
+ _mbrtowc
+ _mbtocsx
+ _wcrtomb
CStrings:
+ "cur_min < MB_LEN_MAX"
+ "iconv_std_delta_remap"
+ "iconv_std_mbtowc"
+ "wcdelta[i] <= curmb"
+ "wcdelta[j] <= curmb"
+ "wcsz != (size_t)-2"
+ "wcsz <= tmpsz"

```
