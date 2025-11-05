## libcorecrypto_noasm.dylib

> `/usr/lib/system/libcorecrypto_noasm.dylib`

```diff

-1736.80.2.0.0
-  __TEXT.__text: 0x75550
+1736.100.95.0.0
+  __TEXT.__text: 0x73ea0
   __TEXT.__auth_stubs: 0x220
-  __TEXT.__const: 0x18cd8
+  __TEXT.__const: 0x18d08
   __TEXT.__cstring: 0x584c
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x16c8
-  __TEXT.__eh_frame: 0x310
+  __TEXT.__unwind_info: 0x18d0
+  __TEXT.__eh_frame: 0x3a0
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0xf30
   __AUTH_CONST.__auth_got: 0x110

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: AC91AFE3-6154-35CF-86D8-43BAE11B24E3
-  Functions: 2005
-  Symbols:   2432
+  UUID: 3CCFFC54-647A-374C-A061-BA4598A05CFA
+  Functions: 2113
+  Symbols:   2551
   CStrings:  499
 
Symbols:
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ __MergedGlobals
+ _ccn_gcd_approximate
+ _ccrsa_crt_exp_mod_pq_star_ws
+ _ccrsa_crt_init_pq_star_ws
+ _ccrsa_find_prime_multiple_ws
+ _ccrsa_recover_pq_ws
+ cc_log_default.cold.1
+ ccrng_atfork_child.cold.1
+ ccrng_atfork_parent.cold.1
+ ccrng_atfork_prepare.cold.1
+ ccrng_getentropy_generate.cold.1
+ ccrng_prng.cold.1
+ generate.cold.1
+ init.cold.1
- _ccrsa_init_pub_ws
- _cczp_inv_update_ws
- _cczp_mm_init_copy
- _cczp_mm_inv_ws
- _cczp_mm_sqrt_ws
- cc_log_default.initp
- cc_log_default.log
- cced25519_sign_with_rng_internal.cold.1

```
