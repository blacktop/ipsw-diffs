## libcorecrypto_trace.dylib

> `/usr/lib/system/libcorecrypto_trace.dylib`

```diff

-1922.80.7.0.0
-  __TEXT.__text: 0x86988
+1922.100.95.0.0
+  __TEXT.__text: 0x877f4
   __TEXT.__auth_stubs: 0x230
-  __TEXT.__cstring: 0x62c9
-  __TEXT.__const: 0x1e338
+  __TEXT.__cstring: 0x61ae
+  __TEXT.__const: 0x1e4e8
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x1ae8
+  __TEXT.__unwind_info: 0x1b20
   __TEXT.__eh_frame: 0x350
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x21a8
   __AUTH_CONST.__auth_got: 0x118
   __AUTH_CONST.__const: 0x1ea8
-  __AUTH.__data: 0xd0
+  __AUTH.__data: 0x130
   __DATA.__data: 0x6868
   __DATA.__bss: 0x20a0
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
-  UUID: D09805BB-D768-3904-922F-711778CCA8E1
-  Functions: 2441
-  Symbols:   4402
-  CStrings:  582
+  UUID: 7F57F5B6-E04A-3AB3-BCD9-356242B31A86
+  Functions: 2482
+  Symbols:   4500
+  CStrings:  578
 
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
- "fipspost_post_tdes_ecb"
- "fipspost_post_tdes_ecb_decrypt"

```
