## com.apple.driver.AppleSEPKeyStore

> `com.apple.driver.AppleSEPKeyStore`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`

```diff

-2155.160.11.0.0
-  __TEXT.__cstring: 0x4834
+2155.160.13.0.1
+  __TEXT.__cstring: 0x4838
   __TEXT.__const: 0x96c
-  __TEXT_EXEC.__text: 0x3db5c
+  __TEXT_EXEC.__text: 0x3e038
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x3a4
+  __DATA.__data: 0x3ac
   __DATA.__common: 0xe8
   __DATA.__bss: 0x300
   __DATA_CONST.__auth_got: 0x4f8

   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x4c88
+  __DATA_CONST.__const: 0x4c90
   __DATA_CONST.__kalloc_type: 0xe00
   __DATA_CONST.__kalloc_var: 0xa0
-  Functions: 1024
-  Symbols:   1606
+  Functions: 1029
+  Symbols:   1615
   CStrings:  379
 
Symbols:
+ _OUTLINED_FUNCTION_100
+ _OUTLINED_FUNCTION_123
+ _OUTLINED_FUNCTION_127
+ _OUTLINED_FUNCTION_128
+ _OUTLINED_FUNCTION_129
+ __ZN13AppleKeyStore17change_lock_stateEyiiPiPKvjbb
+ __ZN13AppleKeyStore22fv_unwrap_vek_with_acmEyP14aks_fv_param_sjP13aks_fv_data_sS3_S3_S3_P12aks_fv_key_sS3_
+ __ZN13AppleKeyStore28pf_fv_unwrap_and_migrate_vekEP14aks_fv_param_sjP13aks_fv_data_sS3_S3_P12aks_fv_key_sS3_
+ __ZZN13AppleKeyStore13event_enqueueEP14events_entry_sE21kalloc_type_view_3757
+ __ZZN13AppleKeyStore13handle_eventsEvE21kalloc_type_view_3790
+ __ZZN13AppleKeyStore13tdm_new_entryEP19AppleTDMAKSServicesE21kalloc_type_view_3470
+ __ZZN13AppleKeyStore13unload_keybagEyiE21kalloc_type_view_1829
+ __ZZN13AppleKeyStore16tdm_remove_entryEP19AppleTDMAKSServicesE21kalloc_type_view_3499
+ __ZZN13AppleKeyStore17set_volume_keybagEyijP6OSDataS1_S1_bE21kalloc_type_view_2727
+ __ZZN13AppleKeyStore17set_volume_keybagEyijP6OSDataS1_S1_bE21kalloc_type_view_2754
+ __ZZN13AppleKeyStore22unload_session_keybagsEyiE21kalloc_type_view_1853
+ ___der_key_vek_group_seed_generation
+ __blob_free
+ __ipc_fv_unwrap_vek_v1
+ _der_key_vek_group_seed_generation
- _OUTLINED_FUNCTION_126
- __ZN13AppleKeyStore17change_lock_stateEyiiPiPKvjb
- __ZN13AppleKeyStore22fv_unwrap_vek_with_acmEyP14aks_fv_param_sjP13aks_fv_data_sS3_S3_S3_P12aks_fv_key_s
- __ZZN13AppleKeyStore13event_enqueueEP14events_entry_sE21kalloc_type_view_3749
- __ZZN13AppleKeyStore13handle_eventsEvE21kalloc_type_view_3782
- __ZZN13AppleKeyStore13tdm_new_entryEP19AppleTDMAKSServicesE21kalloc_type_view_3462
- __ZZN13AppleKeyStore13unload_keybagEyiE21kalloc_type_view_1821
- __ZZN13AppleKeyStore16tdm_remove_entryEP19AppleTDMAKSServicesE21kalloc_type_view_3491
- __ZZN13AppleKeyStore17set_volume_keybagEyijP6OSDataS1_S1_bE21kalloc_type_view_2719
- __ZZN13AppleKeyStore17set_volume_keybagEyijP6OSDataS1_S1_bE21kalloc_type_view_2746
- __ZZN13AppleKeyStore22unload_session_keybagsEyiE21kalloc_type_view_1845
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fUqyNN/Sources/AppleKeyStore_SEP_kexts/AppleKeyStore.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fUqyNN/Sources/AppleKeyStore_SEP_kexts/ipc.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fUqyNN/Sources/AppleKeyStore_SEP_kexts/msg.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fUqyNN/Sources/AppleKeyStore_SEP_kexts/platform/platform.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.fUqyNN/Sources/AppleKeyStore_SEP_kexts/platform/platform_kernel.c"
+ "14:21:40"
+ "2155.160.13.0.1"
+ "Jul 11 2026"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wExWkF/Sources/AppleKeyStore_SEP_kexts/AppleKeyStore.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wExWkF/Sources/AppleKeyStore_SEP_kexts/ipc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wExWkF/Sources/AppleKeyStore_SEP_kexts/msg.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wExWkF/Sources/AppleKeyStore_SEP_kexts/platform/platform.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.wExWkF/Sources/AppleKeyStore_SEP_kexts/platform/platform_kernel.c"
- "19:03:31"
- "2155.160.11"
- "Jun 21 2026"
```
