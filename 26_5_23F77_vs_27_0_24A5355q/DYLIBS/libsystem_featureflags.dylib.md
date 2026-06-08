## libsystem_featureflags.dylib

> `/usr/lib/system/libsystem_featureflags.dylib`

```diff

-103.0.0.0.0
-  __TEXT.__text: 0x1f18
-  __TEXT.__auth_stubs: 0x370
+107.0.0.0.0
+  __TEXT.__text: 0x1ecc
   __TEXT.__const: 0x50
   __TEXT.__cstring: 0x279
   __TEXT.__unwind_info: 0xa0
-  __DATA_CONST.__got: 0x38
+  __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x1b8
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0x21
   __DATA.__bss: 0x10
   __DATA_DIRTY.__bss: 0x20

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: CA0341F7-7B22-30EA-9C7B-09687593FA0F
+  UUID: F6EEE9F9-A8D3-315D-880F-05AC430AFC6D
   Functions: 20
-  Symbols:   109
+  Symbols:   112
   CStrings:  26
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retain_x2
+ _objc_retain_x22
+ _objc_retain_x23
+ _objc_retain_x8
- _objc_release_x27
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x28
Functions:
~ __os_feature_enabled_impl -> __os_feature_enabled_simple_impl : 2000 -> 1816
~ __os_feature_enabled_simple_impl -> _OUTLINED_FUNCTION_0 : 1816 -> 20
~ _OUTLINED_FUNCTION_1 -> __os_feature_enabled_impl : 20 -> 2000
~ __os_feature_table_once -> __os_feature_enabled_SLOWPATH : 216 -> 2044
~ __os_feature_enabled_envvar_check_once -> __os_feature_table_once : 72 -> 216
~ __os_feature_search_paths -> __os_feature_enabled_envvar_check_once : 12 -> 72
~ __os_feature_enabled_SLOWPATH -> __os_feature_internal_search_path : 2092 -> 12
~ __os_feature_enabled_extract : 312 -> 304
~ __os_feature_enabled_extract_domain : 124 -> 120
~ ____os_featureenabled_slow_load_disclosures_block_invoke : 120 -> 116
~ ____os_featureenabled_slow_load_disclosures_block_invoke_2 : 152 -> 144
~ __os_feature_enabled_write_nested_value_into_plist : 320 -> 316

```
