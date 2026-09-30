## mod_echo.so

> `/usr/libexec/apache2/mod_echo.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0xbec
+880.0.0.0.0
+  __TEXT.__text: 0xb3c
   __TEXT.__auth_stubs: 0x120
   __TEXT.__cstring: 0x15b
-  __TEXT.__unwind_info: 0x54
+  __TEXT.__unwind_info: 0x60
   __DATA_CONST.__auth_got: 0x90
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 38B1802B-9E1B-3C3F-A264-81A2B9CFDB55
+  UUID: F654F122-9E6A-3987-906C-1882F51F318F
   Functions: 6
   Symbols:   27
   CStrings:  7
Functions:
~ _echo_on : 76 -> 72
~ _process_echo_connection : 1984 -> 1888
~ _update_echo_child_status : 336 -> 304
~ _brigade_peek : 516 -> 472
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/echo/mod_echo.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/echo/mod_echo.c"

```
