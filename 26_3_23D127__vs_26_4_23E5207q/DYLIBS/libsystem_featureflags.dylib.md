## libsystem_featureflags.dylib

> `/usr/lib/system/libsystem_featureflags.dylib`

```diff

-101.0.0.0.0
-  __TEXT.__text: 0x1ed0
-  __TEXT.__auth_stubs: 0x3a0
+103.0.0.0.0
+  __TEXT.__text: 0x1f18
+  __TEXT.__auth_stubs: 0x370
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x254
+  __TEXT.__cstring: 0x279
   __TEXT.__unwind_info: 0xa0
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x1d0
-  __DATA.__data: 0x19
+  __AUTH_CONST.__auth_got: 0x1b8
+  __DATA.__data: 0x21
   __DATA.__bss: 0x10
   __DATA_DIRTY.__bss: 0x20
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 02AF0CB6-DE2D-3EDA-B65B-F59A6D4D039D
+  UUID: 954C99C6-44E5-364C-AE91-7FF1B4A4462C
   Functions: 20
-  Symbols:   112
-  CStrings:  25
+  Symbols:   109
+  CStrings:  26
 
Symbols:
+ _objc_release_x27
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x2
- _objc_retain_x22
- _objc_retain_x23
- _objc_retain_x8
Functions:
~ __os_feature_enabled_impl : 2004 -> 2000
~ __os_feature_enabled_SLOWPATH : 2044 -> 2092
~ __os_feature_enabled_extract : 304 -> 312
~ __os_feature_enabled_extract_domain : 120 -> 124
~ ____os_featureenabled_slow_load_disclosures_block_invoke : 116 -> 120
~ ____os_featureenabled_slow_load_disclosures_block_invoke_2 : 144 -> 152
~ __os_feature_enabled_write_nested_value_into_plist : 316 -> 320
CStrings:
+ "/System/Library/FeatureFlags/Unified"

```
