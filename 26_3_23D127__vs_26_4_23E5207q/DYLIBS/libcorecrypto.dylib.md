## libcorecrypto.dylib

> `/usr/lib/system/libcorecrypto.dylib`

```diff

-1922.80.7.0.0
-  __TEXT.__text: 0x85dd0
+1922.100.95.0.0
+  __TEXT.__text: 0x86c68
   __TEXT.__auth_stubs: 0x230
-  __TEXT.__cstring: 0x5f92
-  __TEXT.__const: 0x1e338
+  __TEXT.__cstring: 0x5e8e
+  __TEXT.__const: 0x1e4d8
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x1978
+  __TEXT.__unwind_info: 0x19a8
   __TEXT.__eh_frame: 0x350
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x21a8
   __AUTH_CONST.__auth_got: 0x118
   __AUTH_CONST.__const: 0x1ea8
-  __AUTH.__data: 0xb8
+  __AUTH.__data: 0x118
   __DATA.__data: 0x6858
   __DATA.__bss: 0xed0
   __DATA.__common: 0x8
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0xa30
+  __DATA_DIRTY.__bss: 0xa40
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdispatch.dylib
-  - /usr/lib/system/libdyld.dylib
-  - /usr/lib/system/libmacho.dylib
   - /usr/lib/system/libsystem_blocks.dylib
   - /usr/lib/system/libsystem_c.dylib
   - /usr/lib/system/libsystem_kernel.dylib

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 750CB60B-7AA1-32AE-AC77-C7517F9EA49B
-  Functions: 2435
-  Symbols:   4382
-  CStrings:  549
+  UUID: C098EFCD-7C35-3FDA-B581-89EBA8663A7C
+  Functions: 2476
+  Symbols:   4480
+  CStrings:  546
 
Symbols:
+ _OUTLINED_FUNCTION_7
+ _ccec_sign_composite_hedged
+ _ccmlkem_ntt_basemul_cache_compute
+ _ccshake256_internal
+ _ccsigma_exclave_pairing_session_info
+ _ccsigma_session_clear
+ _ccsigma_session_export
+ _ccsigma_session_import
+ _ccsigma_session_init
+ _ccsigma_session_open
+ _ccsigma_session_seal
+ _ccxof_absorb_internal
+ _ccxof_squeeze_internal
+ _ep_session_advance_seqnum
+ _ep_session_clear
+ _ep_session_derive
+ _ep_session_duplex_init
+ _ep_session_export_to_bytes
+ _ep_session_get_seqnum
+ _ep_session_info
+ _ep_session_init_from_bytes
+ _ep_session_open
+ _ep_session_seal
+ _ep_session_serialized_nbytes
+ _ep_session_set_seqnum
- _ccmlkem_ntt_basemul
- _fipspost_post_tdes_ecb
CStrings:
+ "ep i traffic"
+ "ep r traffic"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: des3_ecb_decrypt cmp\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: des3_ecb_decrypt one_shot\n"
- "FIPSPOST_USER [%llu] %s:%d: FAILED: fipspost_post_tdes_ecb: %d\n"
- "FIPSPOST_USER [%llu] %s:%d: PASSED: (%u ms) - fipspost_post_tdes_ecb\n"
- "fipspost_post_tdes_ecb_decrypt"

```
