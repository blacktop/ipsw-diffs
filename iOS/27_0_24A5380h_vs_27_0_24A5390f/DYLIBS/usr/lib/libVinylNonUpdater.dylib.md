## libVinylNonUpdater.dylib

> `/usr/lib/libVinylNonUpdater.dylib`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__weak_got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`

```diff

 178.0.0.0.0
-  __TEXT.__text: 0x59e2c
+  __TEXT.__text: 0x59f10
   __TEXT.__init_offsets: 0x54
-  __TEXT.__const: 0x73cc
+  __TEXT.__const: 0x7424
   __TEXT.__gcc_except_tab: 0x4e94
-  __TEXT.__cstring: 0xc9ea
+  __TEXT.__cstring: 0xca08
   __TEXT.__oslogstring: 0x7c
-  __TEXT.__unwind_info: 0x1f78
+  __TEXT.__unwind_info: 0x1f80
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x1e90
   __DATA_CONST.__weak_got: 0x10

   __AUTH_CONST.__cfstring: 0xcc0
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__auth_got: 0xe88
-  __DATA.__data: 0xc70
+  __DATA.__data: 0xc98
   __DATA.__bss: 0x4d8
   __DATA.__common: 0x48
   __DATA_DIRTY.__data: 0x28

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 1698
-  Symbols:   3137
-  CStrings:  1554
+  Functions: 1701
+  Symbols:   3148
+  CStrings:  1555
 
Symbols:
+ ___der_key_last_mesa_auth
+ ___der_key_last_mesa_unlock
+ ___der_key_last_passcode_auth
+ ___der_key_last_passcode_unlock
+ ___der_key_sks_heap_stats
+ _aks_get_convenience_bio_state
+ _der_key_last_mesa_auth
+ _der_key_last_mesa_unlock
+ _der_key_last_passcode_auth
+ _der_key_last_passcode_unlock
+ _der_key_sks_heap_stats
Functions:
~ _OUTLINED_FUNCTION_22 : 12 -> 20
~ _OUTLINED_FUNCTION_23 : 32 -> 12
+ _OUTLINED_FUNCTION_24
+ _firebloom_cp_prime_size
~ _aks_kext_get_options : 204 -> 188
~ _aks_get_internal_info_for_key : 384 -> 376
+ _aks_get_convenience_bio_state
CStrings:
+ "aks_get_convenience_bio_state"
```
