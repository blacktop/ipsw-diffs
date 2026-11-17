## libcorecrypto.dylib

> `/usr/lib/system/libcorecrypto.dylib`

```diff

-2109.60.2.0.0
-  __TEXT.__text: 0x8bb50
+2109.60.7.0.0
+  __TEXT.__text: 0x8bca4
   __TEXT.__cstring: 0x5a03
   __TEXT.__const: 0x204e8
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x2428
+  __TEXT.__unwind_info: 0x2420
   __TEXT.__eh_frame: 0x3c8
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x2108

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libsystem_trace.dylib
-  Functions: 2656
+  Functions: 2654
   Symbols:   2969
   CStrings:  537
 
Functions:
~ _OUTLINED_FUNCTION_0 : 20 -> 16
~ _OUTLINED_FUNCTION_0 : 16 -> 24
~ _OUTLINED_FUNCTION_0 : 24 -> 16
~ _OUTLINED_FUNCTION_0 : 16 -> 12
~ _OUTLINED_FUNCTION_0 : 12 -> 20
~ _OUTLINED_FUNCTION_0 : 20 -> 16
~ _OUTLINED_FUNCTION_0 : 16 -> 20
~ _OUTLINED_FUNCTION_0 : 20 -> 48
~ _OUTLINED_FUNCTION_0 : 48 -> 56
~ _OUTLINED_FUNCTION_0 : 56 -> 36
- _OUTLINED_FUNCTION_0
~ _OUTLINED_FUNCTION_1 : 20 -> 12
~ _OUTLINED_FUNCTION_1 : 12 -> 20
~ _OUTLINED_FUNCTION_1 : 20 -> 12
~ _OUTLINED_FUNCTION_1 : 12 -> 24
~ _OUTLINED_FUNCTION_1 : 24 -> 16
~ _OUTLINED_FUNCTION_1 : 16 -> 12
~ _OUTLINED_FUNCTION_1 : 12 -> 20
~ _OUTLINED_FUNCTION_1 : 20 -> 24
~ _OUTLINED_FUNCTION_1 : 24 -> 16
~ _OUTLINED_FUNCTION_1 : 16 -> 20
~ _OUTLINED_FUNCTION_1 : 20 -> 12
~ _OUTLINED_FUNCTION_1 : 12 -> 48
~ _OUTLINED_FUNCTION_1 : 48 -> 20
~ _OUTLINED_FUNCTION_1 : 20 -> 16
- _OUTLINED_FUNCTION_1
~ _OUTLINED_FUNCTION_3 : 32 -> 24
~ _ccmode_gcm_update_pad : 112 -> 96
~ _ccn_write_uint_public_value : 188 -> 192
~ _ccn_write_int_public_value : 92 -> 100
~ _cczp_modn_ws : 376 -> 408
~ _cczp_sqr_default_ws : 160 -> 148
~ _ccn_recode_jsf_init : 136 -> 132
~ _ccec25519_sub_asm_ws : 28 -> 16
~ _ccnistkdf_ctr_hmac : 380 -> 420
~ _ccn_cmp : 104 -> 96
+ sub_1d3f50460
- sub_1d3887480
~ _ccnistkdf_ctr_cmac_internal : 388 -> 448
~ _ccmlkem_poly_decode_decompress_d1_masked : 124 -> 128
+ _cced25519_make_key_pair
~ _cced25519_make_pub_internal : 220 -> 244
~ _cced25519_make_pub_with_rng : 72 -> 104
- _cced25519_make_key_pair
~ _cche_galois_key_generate_ws : 884 -> 924
~ _cche_galois_key_save_ws : 236 -> 248
~ _cche_galois_key_load_ws : 684 -> 740
~ _cccmac_final_generate_internal : 316 -> 328
~ _cccmac_final_verify_internal : 112 -> 148
~ _cczp_generate_non_zero_element_ws : 268 -> 284
~ _ccec_x963_import_priv_ws : 280 -> 272
```
