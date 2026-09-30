## mod_authn_dbd.so

> `/usr/libexec/apache2/mod_authn_dbd.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x1000
+880.0.0.0.0
+  __TEXT.__text: 0xefc
   __TEXT.__auth_stubs: 0x140
   __TEXT.__cstring: 0x453
-  __TEXT.__unwind_info: 0x54
+  __TEXT.__unwind_info: 0x60
   __DATA_CONST.__auth_got: 0xa0
   __DATA_CONST.__const: 0x88
   __DATA.__data: 0x70

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 990B0168-EC75-33BC-B145-BBEC608F2CED
+  UUID: 35E450B9-8917-311D-80AB-B3EF1A46AEF8
   Functions: 7
   Symbols:   34
   CStrings:  24
Functions:
~ _authn_dbd_cr_conf : 68 -> 64
~ _authn_dbd_merge_conf : 224 -> 196
~ _authn_dbd_hooks : 112 -> 120
~ _authn_dbd_prepare : 308 -> 280
~ _authn_dbd_password : 1656 -> 1548
~ _authn_dbd_realm : 1688 -> 1588
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authn_dbd.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/aaa/mod_authn_dbd.c"

```
