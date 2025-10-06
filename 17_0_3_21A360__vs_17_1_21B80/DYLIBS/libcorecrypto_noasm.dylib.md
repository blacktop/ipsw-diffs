## libcorecrypto_noasm.dylib

> `/usr/lib/system/libcorecrypto_noasm.dylib`

```diff

-1608.0.18.0.0
-  __TEXT.__text: 0x73808
+1608.40.12.0.0
+  __TEXT.__text: 0x73d20
   __TEXT.__auth_stubs: 0x220
-  __TEXT.__const: 0x18964
-  __TEXT.__cstring: 0x51a1
+  __TEXT.__const: 0x189d4
+  __TEXT.__cstring: 0x51d6
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x16d0
+  __TEXT.__unwind_info: 0x16e0
   __TEXT.__eh_frame: 0x270
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0xf00

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  UUID: 50AB6C09-6130-3B4D-86D7-D97CA67C2F1F
-  Functions: 1820
-  Symbols:   3094
-  CStrings:  607
+  UUID: 4021EBE1-C34B-343D-AC3D-176DF8629DDD
+  Functions: 1827
+  Symbols:   3106
+  CStrings:  610
 
Symbols:
+ _PQCLEAN_KYBER768_CLEAN_kyber_shake256_rkprf
+ _ccbfv_encrypt_params_eq
+ _ccbfv_param_ctx_chain_const
+ _ccbfv_param_ctx_coefficient_moduli
+ _ccbfv_param_ctx_eq
+ _ccbfv_param_ctx_plaintext_ctx
+ _ccbfv_param_ctx_plaintext_ctx_const
+ _ccbfv_secret_key_generate_ws
+ _ccbfv_serialize_ciphertext_coeff_max_nskip_lsbs
+ _ccrsa_sign_pkcs1v15_msg_blinded
+ _sizeof_struct_ccbfv_encrypt_params
- _PQCLEAN_KYBER768_CLEAN_cmov
- _PQCLEAN_KYBER768_CLEAN_kyber_shake128_absorb
- _PQCLEAN_KYBER768_CLEAN_verify
- _ccbfv_ptext_ctx_valid
CStrings:
+ "ccnistkdf_ctr_cmac_fixed"
+ "ccshake128_xi"
+ "ccshake256_xi"

```
