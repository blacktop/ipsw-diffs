## libboringssl.dylib

> `/usr/lib/libboringssl.dylib`

```diff

-532.100.26.0.0
-  __TEXT.__text: 0x9e7c4
+532.100.28.0.0
+  __TEXT.__text: 0x9efc4
   __TEXT.__auth_stubs: 0x1e60
   __TEXT.__objc_methlist: 0x1dc
-  __TEXT.__cstring: 0x11fae
+  __TEXT.__cstring: 0x1208d
   __TEXT.__const: 0xff28
   __TEXT.__oslogstring: 0x5ec6
   __TEXT.__gcc_except_tab: 0x2944
-  __TEXT.__unwind_info: 0x2548
+  __TEXT.__unwind_info: 0x2540
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_classname: 0x241
-  __TEXT.__objc_methname: 0xf23
+  __TEXT.__objc_methname: 0xf5c
   __TEXT.__objc_methtype: 0x62b
   __TEXT.__objc_stubs: 0xa0
   __DATA_CONST.__got: 0xf8

   __AUTH_CONST.__auth_got: 0xf48
   __AUTH_CONST.__const: 0x1908
   __AUTH_CONST.__cfstring: 0xe0
-  __AUTH_CONST.__objc_const: 0x2208
+  __AUTH_CONST.__objc_const: 0x2268
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x314
-  __DATA.__data: 0xd20
+  __DATA.__objc_ivar: 0x320
+  __DATA.__data: 0xd48
   __DATA.__bss: 0x540
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0x218

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 4129C9E4-8078-3D50-8A93-A3736F216228
-  Functions: 3221
-  Symbols:   7637
-  CStrings:  3674
+  UUID: E3411E1B-B0D3-3355-8DE1-0522B3D8DB73
+  Functions: 3228
+  Symbols:   7659
+  CStrings:  3685
 
Symbols:
+ GCC_except_table135
+ GCC_except_table56
+ _OBJC_IVAR_$_boringssl_concrete_boringssl_ctx.ats_applicable
+ _OBJC_IVAR_$_boringssl_concrete_boringssl_ctx.is_local_networking
+ _OBJC_IVAR_$_boringssl_concrete_boringssl_ctx.legacy_ats_applicable
+ _TLS_METRIC_ATS_APPLICABLE
+ _TLS_METRIC_IS_LOCAL_NETWORKING
+ _TLS_METRIC_LEGACY_ATS_APPLICABLE
+ _TLS_METRIC_PEER_PUBLIC_KEY_SIZE
+ _TLS_METRIC_TLS_COMPLIANCE_POLICY
+ ___block_literal_global.90
+ ___boringssl_context_certificate_request_callback_block_invoke.219
+ ___boringssl_context_evaluate_trust_async_external_block_invoke.210
+ ___boringssl_context_evaluate_trust_async_internal_block_invoke.202
+ ___boringssl_context_evaluate_trust_async_internal_block_invoke.206
+ ___boringssl_context_new_session_handler_block_invoke.244
+ ___boringssl_context_update_encryption_level_block_invoke.223
+ ___boringssl_context_update_encryption_level_block_invoke.225
+ _boringssl_context_get_ats_applicable
+ _boringssl_context_get_fcs_tls_v2_compliance_mode_enabled
+ _boringssl_context_get_is_local_networking
+ _boringssl_context_get_legacy_ats_applicable
+ _boringssl_context_set_ats_applicable
+ _boringssl_context_set_is_local_networking
+ _boringssl_context_set_legacy_ats_applicable
- GCC_except_table129
- GCC_except_table162
- ___block_literal_global.86
- ___boringssl_context_certificate_request_callback_block_invoke.216
- ___boringssl_context_evaluate_trust_async_external_block_invoke.207
- ___boringssl_context_evaluate_trust_async_internal_block_invoke.199
- ___boringssl_context_evaluate_trust_async_internal_block_invoke.203
- ___boringssl_context_new_session_handler_block_invoke.241
- ___boringssl_context_update_encryption_level_block_invoke.220
- ___boringssl_context_update_encryption_level_block_invoke.222
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CJIfugAcl6Nd26aZhmNIOh9jeQjBMNtdrYvalV0/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/apple/crypto/boringssl_crypto_aes.m"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/apple/crypto/boringssl_crypto_chacha20poly1305.m"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/apple/crypto/boringssl_crypto_ecdh.m"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/apple/crypto/boringssl_crypto_rsa.m"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/bio/bio.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/bio/bio_mem.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/bio/file.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/bn_extra/bn_asn1.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/buf/buf.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/bytestring/cbb.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/cipher_extra/e_tls.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/dsa/dsa_asn1.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/ec_extra/ec_asn1.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/evp/evp.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/evp/evp_asn1.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/evp/evp_ctx.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/evp/p_dsa_asn1.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/evp/p_ec.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/evp/p_ec_asn1.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/evp/p_ed25519.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/evp/p_ed25519_asn1.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/evp/p_rsa.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/evp/p_rsa_asn1.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/evp/p_x25519.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/evp/p_x25519_asn1.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/ex_data.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/bn/add.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/bn/bn.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/bn/ctx.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/bn/div.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/bn/exponentiation.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/bn/jacobi.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/bn/montgomery.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/bn/mul.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/bn/prime.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/bn/random.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/bn/shift.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/bn/sqrt.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/cipher/aead.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/cipher/cipher.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/digest/digest.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/digestsign/digestsign.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/ec/ec.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/ec/ec_key.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/ec/ec_montgomery.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/ec/felem.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/ec/oct.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/ec/p224-64.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/ec/p256.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/ec/scalar.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/ec/simple.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/fipsmodule/rsa/padding.c.inc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/hpke/hpke.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/mem.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/rsa_extra/rsa_asn1.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/crypto/stack/stack.c"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/d1_both.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/d1_lib.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/d1_pkt.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/dtls_method.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/dtls_record.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/encrypted_client_hello.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/extensions.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/handshake.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/handshake_client.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/handshake_server.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/internal.h"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/s3_both.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/s3_pkt.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/ssl_aead_ctx.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/ssl_asn1.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/ssl_buffer.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/ssl_cert.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/ssl_cipher.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/ssl_credential.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/ssl_key_share.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/ssl_lib.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/ssl_privkey.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/ssl_session.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/ssl_transcript.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/ssl_versions.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/t1_enc.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/tls13_both.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/tls13_client.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/tls13_enc.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/tls13_server.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/tls_method.cc"
+ "/Library/Caches/com.apple.xbs/DCF0BEFB-C807-4DC5-8B19-2DC37E65E56E/TemporaryDirectory.CR9mpn/Sources/boringssl/ssl/tls_record.cc"
+ "ats_applicable"
+ "boringssl_context_set_ats_applicable"
+ "boringssl_context_set_is_local_networking"
+ "boringssl_context_set_legacy_ats_applicable"
+ "is_local_networking"
+ "legacy_ats_applicable"
+ "peer_public_key_size"
+ "tls_compliance_policy"
- "/AppleInternal/Library/BuildRoots/4~CIVBugApxyrzzObvCvs3ZQF1rOkGU7zHi4R2gfc/Applications/Xcode.app/Contents/Developer/Platforms/iPhoneOS.platform/Developer/SDKs/iPhoneOS26.4.Internal.sdk/usr/include/c++/v1/__bit_reference:111: libc++ Hardening assertion __ctz + __clz < sizeof(_StorageType) * 8 failed: __fill_masked_range called with invalid range\n"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/apple/crypto/boringssl_crypto_aes.m"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/apple/crypto/boringssl_crypto_chacha20poly1305.m"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/apple/crypto/boringssl_crypto_ecdh.m"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/apple/crypto/boringssl_crypto_rsa.m"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/bio/bio.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/bio/bio_mem.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/bio/file.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/bn_extra/bn_asn1.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/buf/buf.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/bytestring/cbb.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/cipher_extra/e_tls.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/dsa/dsa_asn1.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/ec_extra/ec_asn1.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/evp/evp.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/evp/evp_asn1.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/evp/evp_ctx.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/evp/p_dsa_asn1.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/evp/p_ec.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/evp/p_ec_asn1.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/evp/p_ed25519.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/evp/p_ed25519_asn1.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/evp/p_rsa.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/evp/p_rsa_asn1.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/evp/p_x25519.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/evp/p_x25519_asn1.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/ex_data.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/bn/add.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/bn/bn.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/bn/ctx.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/bn/div.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/bn/exponentiation.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/bn/jacobi.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/bn/montgomery.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/bn/mul.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/bn/prime.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/bn/random.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/bn/shift.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/bn/sqrt.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/cipher/aead.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/cipher/cipher.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/digest/digest.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/digestsign/digestsign.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/ec/ec.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/ec/ec_key.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/ec/ec_montgomery.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/ec/felem.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/ec/oct.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/ec/p224-64.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/ec/p256.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/ec/scalar.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/ec/simple.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/fipsmodule/rsa/padding.c.inc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/hpke/hpke.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/mem.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/rsa_extra/rsa_asn1.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/crypto/stack/stack.c"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/d1_both.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/d1_lib.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/d1_pkt.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/dtls_method.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/dtls_record.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/encrypted_client_hello.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/extensions.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/handshake.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/handshake_client.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/handshake_server.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/internal.h"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/s3_both.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/s3_pkt.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/ssl_aead_ctx.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/ssl_asn1.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/ssl_buffer.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/ssl_cert.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/ssl_cipher.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/ssl_credential.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/ssl_key_share.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/ssl_lib.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/ssl_privkey.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/ssl_session.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/ssl_transcript.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/ssl_versions.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/t1_enc.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/tls13_both.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/tls13_client.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/tls13_enc.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/tls13_server.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/tls_method.cc"
- "/Library/Caches/com.apple.xbs/A8961670-83EE-4643-9373-95227AD4BF65/TemporaryDirectory.IFPFFG/Sources/boringssl/ssl/tls_record.cc"

```
