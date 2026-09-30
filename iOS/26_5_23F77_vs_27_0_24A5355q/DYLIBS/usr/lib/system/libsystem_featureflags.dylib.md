## libsystem_featureflags.dylib

> `/usr/lib/system/libsystem_featureflags.dylib`

```diff

-103.0.0.0.0
-  __TEXT.__text: 0x1f18 sha256:e6e1a7a1186913a3c518605ccd9f97f7994fc5bb61269b0e335bc41feddc0710
-  __TEXT.__auth_stubs: 0x370 sha256:f013e42f1abe7dd34edeeb451efa50ed87ff23c334f29eed1f894f04e3407e51
-  __TEXT.__const: 0x50 sha256:fcdcb49eca0fa2475c06708dd6ef948c0efbfe77a5a9d9399942c7ce808318f3
-  __TEXT.__cstring: 0x279 sha256:e9c907f6964b8cf097c4122240cc19075f2e917f59e766c656f59fcac83c59e7
-  __TEXT.__unwind_info: 0xa0 sha256:7aa5cf154affd9847dfb1d163e6fb0bead25bece42864956042e78220ca75d8c
-  __DATA_CONST.__got: 0x38 sha256:d4817aa5497628e7c77e6b606107042bbba3130888c5f47a375e6179be789fbb
-  __DATA_CONST.__const: 0x28 sha256:1fcd05afee842e378eee602b01eace8d46125b4ffc0990fcaa8422ef06dcf1d4
+107.0.0.0.0
+  __TEXT.__text: 0x1ecc sha256:9da99172b1bc65ce076dd86bd8d06c3c44326f2751773638f419c9d8eedca7fa
+  __TEXT.__const: 0x50 sha256:1b56bb09c08d612eb19d9b6be473936452cbab2e22312fd5c7518a5f304e0784
+  __TEXT.__cstring: 0x279 sha256:b9d4075519d40d7b7b6e042d921f0ad2c3861f127c3045f74721d48274aa2869
+  __TEXT.__unwind_info: 0xa0 sha256:8c19ac5bb62aabdddcb7348a53b1216a3894dae97337b33845f19bcd28898f43
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x28 sha256:0cb42a45cceed2adbe11b34107332717f9ab93c1063ec02dd2b3dbc8e7308a6e
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __AUTH_CONST.__auth_got: 0x1b8 sha256:360d579dbd14759b41afdf7fb5e80c0101e15150ae401d59f92a1e32d129f7cb
-  __DATA.__data: 0x21 sha256:b1e7c7357faa735c9dd63eb02f12394b50e9ff21abee6574aedf63f52ebb9a18
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__data: 0x21 sha256:ad62aefa457fa4939ce91e54475eee88fc5384e8a9d2dcc6c206bc1c6be88d86
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   __DATA_DIRTY.__bss: 0x20 sha256:66687aadf862bd776c8fc18b8e9f8e20089714856ee233b3902a591d0d5f2925
   - /usr/lib/libobjc.A.dylib

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
~ __os_feature_table : sha256 2987ac0550979de4fbc2996829451dcc31376f8910044f0139a016408a13f266 -> ce565ad631175d518bd82510aeedca4f865ffcc8dac3f6fc9e7c1cc075e44c49
~ __os_feature_enabled_simple_impl -> _OUTLINED_FUNCTION_0 : 1816 -> 20
~ _OUTLINED_FUNCTION_1 -> __os_feature_enabled_impl : 20 -> 2000
~ __os_feature_table.cold.1 : sha256 4c7b53baab90efaac8685c18af52b28fd46b62cef52af035664264c3b451ca35 -> 60c5683702fbc59e888c3eda623dff2582af1851af50190216be0b3d659208d5
~ __os_feature_table_once -> __os_feature_enabled_SLOWPATH : 216 -> 2044
~ __os_feature_enabled_impl.cold.1 : sha256 2ce5d22297c861f37f2e48e79efb0dc5c93f76f1973c8dab353634fc31091496 -> edc957889beede08443e851d229d60b1e9f6fbbd096dcff10c49db3dd7d3106e
~ __os_feature_enabled_envvar_check_once -> __os_feature_table_once : 72 -> 216
~ __os_feature_search_paths -> __os_feature_enabled_envvar_check_once : 12 -> 72
~ __os_feature_internal_search_path -> __os_feature_search_paths : sha256 366eb2316693e59ec88006e73fa56d19f5f2282ca0f3e3d24a507ba74dfb37e9 -> 44d147289058c5ca7c5ea61111161d596c3003b7be663711e1313495c70dc1cf
~ __os_feature_enabled_SLOWPATH -> __os_feature_internal_search_path : 2092 -> 12
~ __os_feature_enabled_load : sha256 b13adf0ed3d7ae41250e2b213673ec2e9a86492cf0ff2358e9caaf3ed2f9e353 -> 9c44b1cb4eefdb8d8f421fb61e6f69bdb50bf759b5de430d340f4564b468f96b
~ __os_feature_enabled_extract : 312 -> 304
~ __os_feature_enabled_extract_domain : 124 -> 120
~ ____os_featureenabled_slow_load_disclosures_block_invoke : 120 -> 116
~ ____os_featureenabled_slow_load_disclosures_block_invoke_2 : 152 -> 144
~ __os_feature_enabled_write_nested_value_into_plist : 320 -> 316
~ __os_feature_enabled_is_safe_mode : sha256 2224a728981f1e0434b8f65e2decb4a02d40c05a7bc452b3773cd4202b98a942 -> fae7e0391fdc8bbfa30efb48785d2e7b13399b4c374514a50d768755e8a31308
~ __os_feature_enabled_write_nested_value_into_plist.cold.1 : sha256 157c2899880fc80ec47c6e4d73baa4877f38492d324826f97a929a6f9388c745 -> 83afe0490ccc9935c80c879068dadd7446a60ace280da470a10767880825e7df

```
