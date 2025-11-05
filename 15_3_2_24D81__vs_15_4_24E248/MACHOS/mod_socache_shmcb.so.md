## mod_socache_shmcb.so

> `/usr/libexec/apache2/mod_socache_shmcb.so`

```diff

-879.0.0.0.0
-  __TEXT.__text: 0x617c
+880.0.0.0.0
+  __TEXT.__text: 0x5c84
   __TEXT.__auth_stubs: 0x180
   __TEXT.__cstring: 0xdc8
-  __TEXT.__unwind_info: 0x78
+  __TEXT.__unwind_info: 0x88
   __DATA_CONST.__auth_got: 0xc0
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcrypto.46.dylib
   - /usr/lib/libssl.48.dylib
-  UUID: F20E07EB-6EBC-3C4F-AB07-40F7CB6367CD
+  UUID: ADBD58E3-8F0D-3073-9169-2B2E55949F0F
   Functions: 19
   Symbols:   46
   CStrings:  81
Functions:
~ _socache_shmcb_create : 604 -> 556
~ _socache_shmcb_init : 5540 -> 5348
~ _socache_shmcb_destroy : 96 -> 88
~ _socache_shmcb_store : 1468 -> 1404
~ _socache_shmcb_retrieve : 1168 -> 1100
~ _socache_shmcb_remove : 1292 -> 1232
~ _socache_shmcb_status : 3680 -> 3392
~ _socache_shmcb_iterate : 304 -> 276
~ _socache_shmcb_cleanup : 96 -> 84
~ _shmcb_subcache_remove : 1216 -> 1140
~ _shmcb_subcache_store : 2988 -> 2884
~ _shmcb_cyclic_memcmp : 264 -> 252
~ _shmcb_subcache_expire : 1468 -> 1364
~ _shmcb_cyclic_ntoc_memcpy : 228 -> 224
~ _shmcb_subcache_retrieve : 1876 -> 1780
~ _shmcb_cyclic_cton_memcpy : 228 -> 224
~ _ap_rputs : 212 -> 200
~ _shmcb_subcache_iterate : 2116 -> 2024
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/cache/mod_socache_shmcb.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/apache/httpd/modules/cache/mod_socache_shmcb.c"

```
