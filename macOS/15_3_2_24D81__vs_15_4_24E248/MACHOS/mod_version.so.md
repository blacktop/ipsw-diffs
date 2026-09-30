## mod_version.so

> `/usr/libexec/apache2/mod_version.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0xae8
+880.0.0.0.0
+  __TEXT.__text: 0x99c
   __TEXT.__auth_stubs: 0xd0
   __TEXT.__cstring: 0x1e7
-  __TEXT.__unwind_info: 0x48
+  __TEXT.__unwind_info: 0x58
   __DATA_CONST.__auth_got: 0x68
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 430D0F5E-4AD6-3EE4-AD52-CD4C86D62F9D
+  UUID: 39083C78-06CD-3159-AC13-86A02494A891
   Functions: 3
   Symbols:   20
   CStrings:  12
Functions:
~ _start_ifversion : 1744 -> 1496
~ _compare_version : 768 -> 696
~ _match_version : 280 -> 268
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/metadata/mod_version.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/metadata/mod_version.c"

```
