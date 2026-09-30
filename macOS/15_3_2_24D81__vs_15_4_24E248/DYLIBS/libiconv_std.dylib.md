## libiconv_std.dylib

> `/usr/lib/i18n/libiconv_std.dylib`

```diff

-109.0.0.0.0
-  __TEXT.__text: 0x2a48
+109.100.2.0.0
+  __TEXT.__text: 0x2950
   __TEXT.__auth_stubs: 0x100
   __TEXT.__cstring: 0x236
   __TEXT.__const: 0x1c

   __AUTH.__data: 0x28
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libiconv.2.dylib
-  UUID: B7B3A557-3853-39E9-AA7C-1608D3B1C911
+  UUID: 0C4D6185-B658-37EB-B328-1C2460D63B76
   Functions: 44
   Symbols:   62
   CStrings:  30
Functions:
~ __citrus_iconv_std_iconv_init_shared : 432 -> 420
~ __citrus_iconv_std_iconv_convert : 4944 -> 4680
~ _open_srcs : 808 -> 816
~ _close_srcs : 92 -> 84
~ _close_dsts : 92 -> 84
~ _iconv_std_early_fallback : 160 -> 172
~ _do_conv : 980 -> 976
~ _iconv_std_late_fallback : 132 -> 144
~ __citrus_iconv_std_write_mb : 100 -> 108
~ __citrus_iconv_std_write_uc : 356 -> 364

```
