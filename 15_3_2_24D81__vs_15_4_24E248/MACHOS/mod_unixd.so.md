## mod_unixd.so

> `/usr/libexec/apache2/mod_unixd.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x113c
+880.0.0.0.0
+  __TEXT.__text: 0xfa8
   __TEXT.__auth_stubs: 0x190
   __TEXT.__cstring: 0x653
-  __TEXT.__unwind_info: 0x48
+  __TEXT.__unwind_info: 0x58
   __DATA_CONST.__auth_got: 0xc8
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0xd0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: 18C2243C-1400-3D3C-B5C8-D7BEB854F890
+  UUID: D225B79F-B3BA-3CCE-9C4E-E20DB237FAAD
   Functions: 10
   Symbols:   39
   CStrings:  36
Functions:
~ _ap_unixd_setup_child : 1012 -> 888
~ _set_group_privs : 728 -> 680
~ _unixd_set_user : 176 -> 156
~ _unixd_set_group : 140 -> 128
~ _unixd_set_chroot_dir : 168 -> 148
~ _unixd_set_suexec : 268 -> 232
~ _unixd_pre_config : 360 -> 328
~ _unixd_dump_config : 356 -> 316
~ _unixd_drop_privileges : 1056 -> 984
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/arch/unix/mod_unixd.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/arch/unix/mod_unixd.c"

```
