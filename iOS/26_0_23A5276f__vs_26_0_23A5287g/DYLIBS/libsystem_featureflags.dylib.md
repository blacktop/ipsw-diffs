## libsystem_featureflags.dylib

> `/usr/lib/system/libsystem_featureflags.dylib`

```diff

   __TEXT.__auth_stubs: 0x3a0
   __TEXT.__const: 0x50
   __TEXT.__cstring: 0x254
-  __TEXT.__unwind_info: 0x98
+  __TEXT.__unwind_info: 0xa0
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: D935498A-B164-3676-9F6B-0F8830509CA5
+  UUID: 629D32B7-00C0-37BC-AE2B-6A60673AD8AB
   Functions: 20
   Symbols:   112
   CStrings:  25
Functions:
~ __os_feature_enabled_simple_impl -> __os_feature_table : 1816 -> 56
~ __os_feature_table -> __os_feature_enabled_simple_impl : 56 -> 1816
~ __os_feature_table_once -> __os_feature_table.cold.1 : 216 -> 52
~ __os_feature_table.cold.1 -> __os_feature_table_once : 52 -> 216
~ __os_feature_enabled_SLOWPATH -> __os_feature_search_paths : 2044 -> 12
~ __os_feature_internal_search_path -> __os_feature_enabled_SLOWPATH : 12 -> 2044

```
