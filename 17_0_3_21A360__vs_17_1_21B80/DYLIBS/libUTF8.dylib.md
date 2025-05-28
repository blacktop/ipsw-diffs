## libUTF8.dylib

> `/usr/lib/i18n/libUTF8.dylib`

```diff

-80.0.0.0.0
-  __TEXT.__text: 0x4a0
-  __TEXT.__auth_stubs: 0x30
+86.0.0.0.0
+  __TEXT.__text: 0x72c
+  __TEXT.__auth_stubs: 0x40
   __TEXT.__const: 0x130
-  __TEXT.__unwind_info: 0x68
-  __AUTH_CONST.__auth_got: 0x18
-  __AUTH.__data: 0x48
+  __TEXT.__cstring: 0x65
+  __TEXT.__unwind_info: 0x7c
+  __AUTH_CONST.__auth_got: 0x20
+  __AUTH.__data: 0x58
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libiconv.2.dylib
-  Functions: 12
-  Symbols:   29
-  CStrings:  0
+  Functions: 15
+  Symbols:   36
+  CStrings:  5
 
Symbols:
+ ___assert_rtn
+ __citrus_UTF8_stdenc_cstombn
+ __citrus_UTF8_stdenc_cstombn.cold.1
+ __citrus_UTF8_stdenc_mbtocsn
+ __citrus_UTF8_stdenc_mbtocsn.cold.1
- __citrus_UTF8_stdenc_init_state
CStrings:
+ "_citrus_UTF8_stdenc_cstombn"
+ "_citrus_UTF8_stdenc_mbtocsn"
+ "accum <= n"
+ "citrus_stdenc_template.h"
+ "tmp <= n"

```
