## libboringssl.dylib

> `/usr/lib/libboringssl.dylib`

```diff

-  __TEXT.__text: 0xa57ec
+  __TEXT.__text: 0xa5828
   __TEXT.__objc_methlist: 0x1dc
   __TEXT.__cstring: 0x13864
   __TEXT.__const: 0xff58
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Functions:
~ __ZN4bsslL26ssl_cipher_process_rulestrEPKcPPNS_15cipher_order_stES4_b : 1592 -> 1632
~ _RSA_verify_PKCS1_PSS_mgf1 : 892 -> 924
~ __ZN4bssl25tls13_process_certificateEPNS_13SSL_HANDSHAKEERKNS_10SSLMessageEb : 2792 -> 2800
~ __ZN4bssl19ssl_nid_to_group_idEPti : 68 -> 72
~ _boringssl_ciphers_create_set_bitmask : 156 -> 164
~ _SSL_CREDENTIAL_set1_PAKE_client_password_record : 228 -> 220
~ __ZN4bssl22tls13_server_handshakeEPNS_13SSL_HANDSHAKEE : 8864 -> 8856
~ _SSL_SESSION_get_version : 68 -> 72
~ __ZN4bssl27ssl_pkey_supports_algorithmEPK6ssl_stP11evp_pkey_sttb : 360 -> 368
~ __ZL16set_sigalg_prefsPN4bssl5ArrayItEENS_4SpanIKtEE : 584 -> 568
~ _BN_sub_word : 260 -> 268
~ __ZN4bsslL32tls13_add_compressed_certificateEP6ssl_stPNS_8internal14StackAllocatedI6cbb_stvXadL_Z8CBB_zeroEEXadL_Z11CBB_cleanupEEEEPNS_13SSL_HANDSHAKEEPS4_S9_PPhPm : 768 -> 760
~ __ZN4bssl34ssl_get_local_application_settingsEPKNS_13SSL_HANDSHAKEEPNS_4SpanIKhEES5_ : 152 -> 144
~ __ZN4bssl28ssl_parse_clienthello_tlsextEPNS_13SSL_HANDSHAKEEPK22ssl_early_callback_ctx : 724 -> 732
~ __ZN4bssl28ssl_parse_serverhello_tlsextEPNS_13SSL_HANDSHAKEEPK6cbs_st : 748 -> 756
~ _bn_sqr_normal : 276 -> 256
~ __ZN4bssl20ssl_name_to_group_idEPtPKcm : 192 -> 204
~ _SSL_get_group_name : 60 -> 72
~ _tls1_sha256_final_raw : 72 -> 68
~ _tls1_sha512_final_raw : 116 -> 112
~ _parse_base128_integer : 108 -> 104
~ __ZN4bssl20ssl_server_handshakeEPNS_13SSL_HANDSHAKEE : 11108 -> 11100
~ _OPENSSL_strlcat : 96 -> 92
CStrings:
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/apple/crypto/boringssl_crypto_aes.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/apple/crypto/boringssl_crypto_chacha20poly1305.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/apple/crypto/boringssl_crypto_ecdh.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/apple/crypto/boringssl_crypto_rsa.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/bio/bio.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/bio/bio_mem.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/bio/file.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/bn_extra/bn_asn1.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/buf/buf.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/bytestring/cbb.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/cipher_extra/e_tls.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/dsa/dsa_asn1.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/ec_extra/ec_asn1.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/evp/evp.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/evp/evp_asn1.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/evp/evp_ctx.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/evp/p_dsa_asn1.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/evp/p_ec.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/evp/p_ec_asn1.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/evp/p_ed25519.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/evp/p_ed25519_asn1.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/evp/p_rsa.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/evp/p_rsa_asn1.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/evp/p_x25519.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/evp/p_x25519_asn1.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/ex_data.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/bn/add.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/bn/bn.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/bn/ctx.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/bn/div.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/bn/exponentiation.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/bn/jacobi.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/bn/montgomery.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/bn/mul.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/bn/prime.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/bn/random.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/bn/shift.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/bn/sqrt.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/cipher/aead.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/cipher/cipher.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/digest/digest.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/digestsign/digestsign.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/ec/ec.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/ec/ec_key.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/ec/ec_montgomery.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/ec/felem.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/ec/oct.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/ec/p224-64.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/ec/p256.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/ec/scalar.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/ec/simple.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/fipsmodule/rsa/padding.c.inc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/hpke/hpke.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/mem.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/rsa_extra/rsa_asn1.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/crypto/stack/stack.c"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/d1_both.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/d1_lib.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/d1_pkt.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/dtls_method.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/dtls_record.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/encrypted_client_hello.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/extensions.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/handshake.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/handshake_client.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/handshake_server.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/internal.h"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/s3_both.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/s3_pkt.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/ssl_aead_ctx.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/ssl_asn1.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/ssl_buffer.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/ssl_cert.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/ssl_cipher.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/ssl_credential.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/ssl_key_share.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/ssl_lib.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/ssl_privkey.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/ssl_session.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/ssl_transcript.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/ssl_versions.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/t1_enc.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/tls13_both.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/tls13_client.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/tls13_enc.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/tls13_server.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/tls_method.cc"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.DWS4Ri/Sources/boringssl/ssl/tls_record.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/apple/crypto/boringssl_crypto_aes.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/apple/crypto/boringssl_crypto_chacha20poly1305.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/apple/crypto/boringssl_crypto_ecdh.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/apple/crypto/boringssl_crypto_rsa.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/bio/bio.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/bio/bio_mem.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/bio/file.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/bn_extra/bn_asn1.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/buf/buf.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/bytestring/cbb.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/cipher_extra/e_tls.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/dsa/dsa_asn1.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/ec_extra/ec_asn1.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/evp/evp.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/evp/evp_asn1.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/evp/evp_ctx.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/evp/p_dsa_asn1.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/evp/p_ec.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/evp/p_ec_asn1.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/evp/p_ed25519.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/evp/p_ed25519_asn1.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/evp/p_rsa.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/evp/p_rsa_asn1.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/evp/p_x25519.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/evp/p_x25519_asn1.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/ex_data.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/bn/add.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/bn/bn.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/bn/ctx.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/bn/div.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/bn/exponentiation.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/bn/jacobi.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/bn/montgomery.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/bn/mul.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/bn/prime.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/bn/random.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/bn/shift.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/bn/sqrt.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/cipher/aead.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/cipher/cipher.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/digest/digest.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/digestsign/digestsign.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/ec/ec.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/ec/ec_key.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/ec/ec_montgomery.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/ec/felem.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/ec/oct.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/ec/p224-64.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/ec/p256.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/ec/scalar.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/ec/simple.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/fipsmodule/rsa/padding.c.inc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/hpke/hpke.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/mem.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/rsa_extra/rsa_asn1.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/crypto/stack/stack.c"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/d1_both.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/d1_lib.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/d1_pkt.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/dtls_method.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/dtls_record.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/encrypted_client_hello.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/extensions.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/handshake.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/handshake_client.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/handshake_server.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/internal.h"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/s3_both.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/s3_pkt.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/ssl_aead_ctx.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/ssl_asn1.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/ssl_buffer.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/ssl_cert.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/ssl_cipher.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/ssl_credential.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/ssl_key_share.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/ssl_lib.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/ssl_privkey.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/ssl_session.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/ssl_transcript.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/ssl_versions.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/t1_enc.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/tls13_both.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/tls13_client.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/tls13_enc.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/tls13_server.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/tls_method.cc"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.mBJ2AD/Sources/boringssl/ssl/tls_record.cc"

```
