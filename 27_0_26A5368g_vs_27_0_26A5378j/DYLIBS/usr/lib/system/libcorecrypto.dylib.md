## libcorecrypto.dylib

> `/usr/lib/system/libcorecrypto.dylib`

```diff

-  __TEXT.__text: 0x8cd6c
+  __TEXT.__text: 0x8cb20
   __TEXT.__cstring: 0x5534
   __TEXT.__const: 0x20488
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x1ce8
+  __TEXT.__unwind_info: 0x1ce0
   __TEXT.__eh_frame: 0x3d8
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x1ec8
Sections:
~ __TEXT.__fips_hmacs : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Functions:
~ _ccaes_vng_ctr_crypt : 404 -> 340
~ _eay_RC4 : 604 -> 616
~ _deskey : 612 -> 608
~ _desfunc3 : 1020 -> 1004
~ _AccelerateCrypto_SHA3_keccak : 900 -> 892
~ sub_1805d0130 -> sub_1805d00e0 : 16 -> 32
~ _ccaes_cfb_encrypt_vng : 344 -> 300
~ _ccaes_ofb_crypt_vng : 344 -> 300
~ _ccrsa_crt_exp_mod_pq_star_ws : 480 -> 472
~ _desfunc : 532 -> 528
~ _cckeccak_squeeze_internal : 932 -> 616
~ _ccaes_cfb_decrypt_vng : 356 -> 312
~ _ccaes_ecb_decrypt : 860 -> 856
~ _ccmldsa_poly_bitunpack_eta2 : 160 -> 156
~ _ccmldsa_poly_bitunpack_eta4 : 56 -> 48
~ _ccmldsa_poly_bitpack_t0 : 224 -> 220
~ _ccmldsa_poly_bitunpack_t0 : 300 -> 296
~ _ccmldsa_poly_bitpack_t1 : 140 -> 136
~ _ccmldsa_poly_bitunpack_t1 : 128 -> 124
~ _ccmldsa_poly_bitpack_z : 104 -> 100
~ _ccaes_gladman_encrypt : 3108 -> 3092
~ _ccaes_gladman_decrypt : 3292 -> 3268
~ _ccpolyzp_po2cyc_ctx_init_ws : 1808 -> 1820

```
