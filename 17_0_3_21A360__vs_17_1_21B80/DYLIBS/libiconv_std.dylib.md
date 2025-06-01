## libiconv_std.dylib

> `/usr/lib/i18n/libiconv_std.dylib`

```diff

-80.0.0.0.0
-  __TEXT.__text: 0xb20
-  __TEXT.__auth_stubs: 0xa0
-  __TEXT.__unwind_info: 0x74
-  __AUTH_CONST.__auth_got: 0x50
+86.0.0.0.0
+  __TEXT.__text: 0x1434
+  __TEXT.__auth_stubs: 0xd0
+  __TEXT.__cstring: 0x100
+  __TEXT.__unwind_info: 0x80
+  __DATA_CONST.__got: 0x8
+  __AUTH_CONST.__auth_got: 0x68
   __AUTH.__data: 0x28
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libiconv.2.dylib
-  UUID: FF282A20-DCA3-3353-A872-7D7788B9F971
-  Functions: 9
-  Symbols:   28
-  CStrings:  0
+  UUID: E9513710-10D1-37C4-B628-E2A749B4CE03
+  Functions: 18
+  Symbols:   50
+  CStrings:  10
 
Symbols:
+ ___assert_rtn
+ ___stack_chk_fail
+ ___stack_chk_guard
+ __citrus_iconv_std_iconv_convert.cold.1
+ __citrus_iconv_std_iconv_convert.cold.2
+ __citrus_iconv_std_iconv_convert.cold.3
+ __citrus_iconv_std_iconv_convert.cold.4
+ __citrus_iconv_std_iconv_convert.cold.5
+ __citrus_iconv_std_iconv_convert.cold.6
+ __citrus_iconv_std_iconv_convert.cold.7
+ _bzero
+ _init_encoding
+ _init_encoding.cold.1
CStrings:
+ "(se->se_ps == NULL && se->se_pssaved == NULL) || (se->se_ps != NULL && se->se_pssaved != NULL)"
+ "(signed short)diff > 0"
+ "_citrus_iconv_std_iconv_convert"
+ "citrus_iconv_std.c"
+ "do_conv"
+ "elen < len"
+ "elen == len"
+ "init_encoding"
+ "ret == E2BIG || ret == EILSEQ"
+ "tmpin > *in"

```
