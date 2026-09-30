## mod_socache_shmcb.so

> `/usr/libexec/apache2/mod_socache_shmcb.so`

```diff

-  __TEXT.__text: 0x5cbc
+  __TEXT.__text: 0x5cd8
   __TEXT.__auth_stubs: 0x180
   __TEXT.__cstring: 0xde7
   __TEXT.__unwind_info: 0x88
Sections:
~ __TEXT.__cstring : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__const : content changed
~ __DATA.__data : content changed
Functions:
~ _socache_shmcb_init : 5348 -> 5352
~ _socache_shmcb_store : 1404 -> 1408
~ _socache_shmcb_retrieve : 1100 -> 1104
~ _socache_shmcb_remove : 1232 -> 1236
~ _socache_shmcb_status : 3392 -> 3396
~ _socache_shmcb_iterate : 276 -> 280
~ _shmcb_subcache_iterate : 2032 -> 2036
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.HCJruC/Sources/apache/httpd/modules/cache/mod_socache_shmcb.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.QaP6H4/Sources/apache/httpd/modules/cache/mod_socache_shmcb.c"

```
