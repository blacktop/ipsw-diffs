## com.apple.security.sandbox

> `com.apple.security.sandbox`

```diff

-3051.40.70.0.0
-  __TEXT.__os_log: 0x1d8e
-  __TEXT.__const: 0x1f18d1
+3051.40.80.0.0
+  __TEXT.__os_log: 0x1d90
+  __TEXT.__const: 0x1f2991
   __TEXT.__cstring: 0x6f21
-  __TEXT_EXEC.__text: 0x381e8
+  __TEXT_EXEC.__text: 0x38234
   __TEXT_EXEC.__auth_stubs: 0x1080
   __DATA.__data: 0x220
   __DATA_CONST.__const: 0x3928
Functions:
~ sub_fffffe000aa533f8 -> sub_fffffe000a9e6a68 : 400 -> 424
~ _hook_mount_notify_mount : 1192 -> 1228
~ _eval : 13824 -> 13828
~ sub_fffffe000aa695cc -> sub_fffffe000a9fcc7c : 720 -> 704
~ _re_cache_init : 496 -> 504
~ _collection_init : 1008 -> 1028
CStrings:
+ "%s set rootless flags on %s with flags=0x%lx"
- "%s set rootless flags on %s with flags=%lu"
```
