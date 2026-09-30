## libcorecrypto.dylib

> `/usr/lib/system/libcorecrypto.dylib`

```diff

-  __TEXT.__text: 0x8c794
+  __TEXT.__text: 0x8c538
   __TEXT.__cstring: 0x5530
   __TEXT.__const: 0x20488
   __TEXT.__fips_hmacs: 0x20
Sections:
~ __TEXT.__fips_hmacs : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
Functions:
~ _ccaes_vng_ctr_crypt : 388 -> 308
~ _ccmode_gcm_update_pad : 112 -> 128
~ _ccaes_cfb_encrypt_vng : 348 -> 300
~ _ccaes_ofb_crypt_vng : 348 -> 300
~ _eay_RC4 : 604 -> 616
~ _deskey : 612 -> 608
~ _desfunc : 532 -> 528
~ _desfunc3 : 1020 -> 1004
~ _cckeccak_squeeze_internal : 932 -> 616
~ _ccaes_cfb_decrypt_vng : 360 -> 312
~ _ccaes_ecb_decrypt : 864 -> 856
~ _ccmldsa_poly_bitunpack_eta2 : 160 -> 156
~ _ccmldsa_poly_bitunpack_eta4 : 56 -> 48
~ _ccmldsa_poly_bitpack_t0 : 224 -> 220
~ _ccmldsa_poly_bitunpack_t0 : 300 -> 296
~ _ccmldsa_poly_bitpack_t1 : 140 -> 136
~ _ccmldsa_poly_bitunpack_t1 : 128 -> 124
~ _ccmldsa_poly_bitpack_z : 104 -> 100
~ _ccaes_gladman_encrypt : 3108 -> 3092
~ _ccaes_gladman_decrypt : 3292 -> 3268
~ _ccpolyzp_po2cyc_ctx_init_ws : 1784 -> 1796

```
