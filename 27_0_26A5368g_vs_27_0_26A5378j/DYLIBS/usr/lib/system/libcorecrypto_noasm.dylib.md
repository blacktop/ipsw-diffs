## libcorecrypto_noasm.dylib

> `/usr/lib/system/libcorecrypto_noasm.dylib`

```diff

-  __TEXT.__text: 0x88b5c
+  __TEXT.__text: 0x889b0
   __TEXT.__const: 0x201e8
   __TEXT.__cstring: 0x5534
   __TEXT.__fips_hmacs: 0x20
   __TEXT.__oslogstring: 0x60
-  __TEXT.__unwind_info: 0x1c30
+  __TEXT.__unwind_info: 0x1c20
   __TEXT.__eh_frame: 0x490
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
~ _ccmlkem_poly_compress_encode_d4 : 1296 -> 1300
~ _ccmlkem_poly_compress_encode_d5 : 1824 -> 1816
~ _ccmlkem_poly_compress_encode_d10 : 1028 -> 1024
~ _ccmlkem_poly_compress_encode_d11 : 284 -> 280
~ _ccmlkem_poly_decode_decompress_d1 : 260 -> 256
~ _ccmlkem_poly_decode_decompress_d4 : 88 -> 84
~ _ccmlkem_poly_decode_decompress_d5 : 288 -> 284
~ _ccmlkem_poly_decode_decompress_d10 : 188 -> 184
~ _ccmlkem_poly_decode_decompress_d11 : 368 -> 356
~ _eay_RC4 : 604 -> 616
~ _deskey : 612 -> 608
~ _desfunc : 532 -> 528
~ _desfunc3 : 1020 -> 1004
~ _cckeccak_squeeze_internal : 932 -> 616
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
