## ocspcheck

> `/usr/bin/ocspcheck`

```diff

-106.0.0.0.0
-  __TEXT.__text: 0x2220
+107.0.0.0.0
+  __TEXT.__text: 0x221c
   __TEXT.__auth_stubs: 0x600
-  __TEXT.__cstring: 0xa46
+  __TEXT.__cstring: 0xa44
   __TEXT.__unwind_info: 0xb0
   __DATA_CONST.__auth_got: 0x300
   __DATA_CONST.__got: 0x38

   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
   - /usr/lib/libtls.20.dylib
-  UUID: 71168CC0-9F8C-3B4C-BBB8-6AD8C9835EB9
+  UUID: E1DCB347-CCEC-3B5B-A650-1ED024413E77
   Functions: 23
   Symbols:   232
-  CStrings:  101
+  CStrings:  100
 
Symbols:
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/libressl/install/TempContent/Objects/libressl.build/libressl-3.3.build/DerivedSources/arm64e/apps/ocspcheck/http.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Binaries/libressl/install/TempContent/Objects/libressl.build/libressl-3.3.build/DerivedSources/arm64e/apps/ocspcheck/ocspcheck.o
+ /AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/libressl/libressl-3.3/apps/ocspcheck/
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/libressl/install/TempContent/Objects/libressl.build/libressl-3.3.build/DerivedSources/arm64e/apps/ocspcheck/http.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Binaries/libressl/install/TempContent/Objects/libressl.build/libressl-3.3.build/DerivedSources/arm64e/apps/ocspcheck/ocspcheck.o
- /AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/libressl/libressl-3.3/apps/ocspcheck/
Functions:
~ _http_alloc : 816 -> 812
~ _http_get : 348 -> 344
~ _main : 3080 -> 3084
CStrings:
- "-"

```
