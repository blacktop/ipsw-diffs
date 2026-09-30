## com.apple.driver.AppleSEPKeyStore

> `com.apple.driver.AppleSEPKeyStore`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`
- `__DATA.__data`
- `__DATA_CONST.__mod_init_func`
- `__DATA_CONST.__mod_term_func`
- `__DATA_CONST.__kalloc_type`
- `__DATA_CONST.__kalloc_var`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-2383.0.14.0.1
+2383.0.22.0.2
   __TEXT.__cstring: 0x51a1
   __TEXT.__os_log: 0x83
   __TEXT.__const: 0xa7c

   __DATA.__bss: 0x4e0
   __DATA_CONST.__mod_init_func: 0x10
   __DATA_CONST.__mod_term_func: 0x10
-  __DATA_CONST.__const: 0x4f58
+  __DATA_CONST.__const: 0x4ff8
   __DATA_CONST.__kalloc_type: 0xe00
   __DATA_CONST.__kalloc_var: 0xa0
   __DATA_CONST.__auth_got: 0x520
Symbols:
+ __ZZN13AppleKeyStore13event_enqueueEP14events_entry_sE21kalloc_type_view_3912
+ __ZZN13AppleKeyStore13handle_eventsEvE21kalloc_type_view_3945
+ __ZZN13AppleKeyStore13tdm_new_entryEP19AppleTDMAKSServicesE21kalloc_type_view_3626
+ __ZZN13AppleKeyStore13unload_keybagEyiE21kalloc_type_view_2000
+ __ZZN13AppleKeyStore16tdm_remove_entryEP19AppleTDMAKSServicesE21kalloc_type_view_3655
+ __ZZN13AppleKeyStore17set_volume_keybagEyijP6OSDataS1_S1_bE21kalloc_type_view_2908
+ __ZZN13AppleKeyStore17set_volume_keybagEyijP6OSDataS1_S1_bE21kalloc_type_view_2935
+ __ZZN13AppleKeyStore22unload_session_keybagsEyiE21kalloc_type_view_2024
- __ZZN13AppleKeyStore13event_enqueueEP14events_entry_sE21kalloc_type_view_3903
- __ZZN13AppleKeyStore13handle_eventsEvE21kalloc_type_view_3936
- __ZZN13AppleKeyStore13tdm_new_entryEP19AppleTDMAKSServicesE21kalloc_type_view_3617
- __ZZN13AppleKeyStore13unload_keybagEyiE21kalloc_type_view_1991
- __ZZN13AppleKeyStore16tdm_remove_entryEP19AppleTDMAKSServicesE21kalloc_type_view_3646
- __ZZN13AppleKeyStore17set_volume_keybagEyijP6OSDataS1_S1_bE21kalloc_type_view_2899
- __ZZN13AppleKeyStore17set_volume_keybagEyijP6OSDataS1_S1_bE21kalloc_type_view_2926
- __ZZN13AppleKeyStore22unload_session_keybagsEyiE21kalloc_type_view_2015
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mzdCFR/Sources/AppleKeyStore_SEP_kexts/AppleKeyStore.cpp"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mzdCFR/Sources/AppleKeyStore_SEP_kexts/ipc.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mzdCFR/Sources/AppleKeyStore_SEP_kexts/msg.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mzdCFR/Sources/AppleKeyStore_SEP_kexts/platform/platform.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mzdCFR/Sources/AppleKeyStore_SEP_kexts/platform/platform_kernel.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mzdCFR/Sources/AppleKeyStore_SEP_kexts/timestamp_ticket.c"
+ "21:18:32"
+ "2383.0.22.0.2"
+ "Jul 14 2026"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.0IQtjA/Sources/AppleKeyStore_SEP_kexts/AppleKeyStore.cpp"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.0IQtjA/Sources/AppleKeyStore_SEP_kexts/ipc.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.0IQtjA/Sources/AppleKeyStore_SEP_kexts/msg.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.0IQtjA/Sources/AppleKeyStore_SEP_kexts/platform/platform.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.0IQtjA/Sources/AppleKeyStore_SEP_kexts/platform/platform_kernel.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.0IQtjA/Sources/AppleKeyStore_SEP_kexts/timestamp_ticket.c"
- "2383.0.14.0.1"
- "23:26:28"
- "Jun 29 2026"
```
