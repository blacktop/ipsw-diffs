## com.apple.driver.AppleSEPKeyStore

> `com.apple.driver.AppleSEPKeyStore`

```diff

-  __TEXT.__cstring: 0x51db
+  __TEXT.__cstring: 0x51a1
   __TEXT.__os_log: 0x83
   __TEXT.__const: 0xa7c
-  __TEXT_EXEC.__text: 0x4316c
+  __TEXT_EXEC.__text: 0x434d0
   __TEXT_EXEC.__auth_stubs: 0xa40
-  __DATA.__data: 0x414
+  __DATA.__data: 0x41c
   __DATA.__common: 0xe8
   __DATA.__bss: 0x4e0
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x4f50
+  __DATA_CONST.__const: 0x4f58
   __DATA_CONST.__kalloc_type: 0xe00
   __DATA_CONST.__kalloc_var: 0xa0
   __DATA_CONST.__auth_got: 0x520
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__auth_ptr: 0x18
-  Functions: 1101
-  Symbols:   1969
-  CStrings:  444
+  Functions: 1103
+  Symbols:   1973
+  CStrings:  443
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__mod_init_func : content changed
~ __DATA_CONST.__mod_term_func : content changed
~ __DATA_CONST.__kalloc_type : content changed
~ __DATA_CONST.__kalloc_var : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
Symbols:
+ _OUTLINED_FUNCTION_122
+ _OUTLINED_FUNCTION_134
+ __ZN13AppleKeyStore17change_lock_stateEyiiPiPKvjbb
+ __ZN13AppleKeyStore22fv_unwrap_vek_with_acmEyP14aks_fv_param_sjP13aks_fv_data_sS3_S3_S3_P12aks_fv_key_sS3_
+ __ZN13AppleKeyStore28pf_fv_unwrap_and_migrate_vekEP14aks_fv_param_sjP13aks_fv_data_sS3_S3_P12aks_fv_key_sS3_
+ __ZZN13AppleKeyStore13event_enqueueEP14events_entry_sE21kalloc_type_view_3903
+ __ZZN13AppleKeyStore13handle_eventsEvE21kalloc_type_view_3936
+ __ZZN13AppleKeyStore13tdm_new_entryEP19AppleTDMAKSServicesE21kalloc_type_view_3617
+ __ZZN13AppleKeyStore13unload_keybagEyiE21kalloc_type_view_1991
+ __ZZN13AppleKeyStore16tdm_remove_entryEP19AppleTDMAKSServicesE21kalloc_type_view_3646
+ __ZZN13AppleKeyStore17set_volume_keybagEyijP6OSDataS1_S1_bE21kalloc_type_view_2899
+ __ZZN13AppleKeyStore17set_volume_keybagEyijP6OSDataS1_S1_bE21kalloc_type_view_2926
+ __ZZN13AppleKeyStore22unload_session_keybagsEyiE21kalloc_type_view_2015
+ ___der_key_vek_group_seed_generation
+ __ipc_fv_unwrap_vek_v1
+ _der_key_vek_group_seed_generation
- _OUTLINED_FUNCTION_123
- _OUTLINED_FUNCTION_135
- _OUTLINED_FUNCTION_142
- __ZN13AppleKeyStore17change_lock_stateEyiiPiPKvjb
- __ZN13AppleKeyStore22fv_unwrap_vek_with_acmEyP14aks_fv_param_sjP13aks_fv_data_sS3_S3_S3_P12aks_fv_key_s
- __ZZN13AppleKeyStore13event_enqueueEP14events_entry_sE21kalloc_type_view_3895
- __ZZN13AppleKeyStore13handle_eventsEvE21kalloc_type_view_3928
- __ZZN13AppleKeyStore13tdm_new_entryEP19AppleTDMAKSServicesE21kalloc_type_view_3609
- __ZZN13AppleKeyStore13unload_keybagEyiE21kalloc_type_view_1983
- __ZZN13AppleKeyStore16tdm_remove_entryEP19AppleTDMAKSServicesE21kalloc_type_view_3638
- __ZZN13AppleKeyStore17set_volume_keybagEyijP6OSDataS1_S1_bE21kalloc_type_view_2891
- __ZZN13AppleKeyStore17set_volume_keybagEyijP6OSDataS1_S1_bE21kalloc_type_view_2918
- __ZZN13AppleKeyStore22unload_session_keybagsEyiE21kalloc_type_view_2007
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.0IQtjA/Sources/AppleKeyStore_SEP_kexts/AppleKeyStore.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.0IQtjA/Sources/AppleKeyStore_SEP_kexts/ipc.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.0IQtjA/Sources/AppleKeyStore_SEP_kexts/msg.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.0IQtjA/Sources/AppleKeyStore_SEP_kexts/platform/platform.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.0IQtjA/Sources/AppleKeyStore_SEP_kexts/platform/platform_kernel.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.0IQtjA/Sources/AppleKeyStore_SEP_kexts/timestamp_ticket.c"
+ "2383.0.14.0.1"
+ "23:26:28"
+ "Jun 29 2026"
+ "com.apple.keystore.config.set.escrow_period"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Xt6ZPx/Sources/AppleKeyStore_SEP_kexts/AppleKeyStore.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Xt6ZPx/Sources/AppleKeyStore_SEP_kexts/ipc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Xt6ZPx/Sources/AppleKeyStore_SEP_kexts/msg.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Xt6ZPx/Sources/AppleKeyStore_SEP_kexts/platform/platform.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Xt6ZPx/Sources/AppleKeyStore_SEP_kexts/platform/platform_kernel.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.Xt6ZPx/Sources/AppleKeyStore_SEP_kexts/timestamp_ticket.c"
- "22:20:15"
- "2383.0.6.0.1"
- "Jun 15 2026"
- "com.apple.keystore.config.set.escrow_passcode_period"
- "com.apple.keystore.config.set.escrow_token_period"

```
