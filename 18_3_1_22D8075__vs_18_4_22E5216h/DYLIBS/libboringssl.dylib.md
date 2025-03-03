## libboringssl.dylib

> `/usr/lib/libboringssl.dylib`

```diff

-486.60.4.0.0
-  __TEXT.__text: 0x98178
-  __TEXT.__auth_stubs: 0x1790
-  __TEXT.__objc_methlist: 0xd8
-  __TEXT.__cstring: 0x103ac
-  __TEXT.__const: 0x10068
-  __TEXT.__oslogstring: 0x5362
-  __TEXT.__gcc_except_tab: 0x2978
-  __TEXT.__unwind_info: 0x21a0
-  __TEXT.__eh_frame: 0xe8
-  __TEXT.__objc_classname: 0x245
-  __TEXT.__objc_methname: 0xe17
+486.100.28.0.0
+  __TEXT.__text: 0x9df58
+  __TEXT.__auth_stubs: 0x1950
+  __TEXT.__objc_methlist: 0x1dc
+  __TEXT.__cstring: 0x105de
+  __TEXT.__const: 0xfef8
+  __TEXT.__oslogstring: 0x577e
+  __TEXT.__gcc_except_tab: 0x2900
+  __TEXT.__unwind_info: 0x2480
+  __TEXT.__eh_frame: 0x130
+  __TEXT.__objc_classname: 0x241
+  __TEXT.__objc_methname: 0xe76
   __TEXT.__objc_methtype: 0x6f7
-  __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0xb7f0
+  __TEXT.__objc_stubs: 0x60
+  __DATA_CONST.__got: 0xc0
+  __DATA_CONST.__const: 0xb890
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10
+  __DATA_CONST.__objc_selrefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0xbd8
-  __AUTH_CONST.__auth_ptr: 0x20
-  __AUTH_CONST.__const: 0x1618
-  __AUTH_CONST.__cfstring: 0x40
-  __AUTH_CONST.__objc_const: 0x2318
+  __AUTH_CONST.__auth_got: 0xcc0
+  __AUTH_CONST.__auth_ptr: 0x10
+  __AUTH_CONST.__const: 0x18c8
+  __AUTH_CONST.__cfstring: 0xe0
+  __AUTH_CONST.__objc_const: 0x2168
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x2f8
-  __DATA.__data: 0xcb8
+  __DATA.__objc_ivar: 0x300
+  __DATA.__data: 0xd00
   __DATA.__bss: 0x550
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0x210

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2984
-  Symbols:   3465
-  CStrings:  3584
+  Functions: 3117
+  Symbols:   3657
+  CStrings:  3620
 
Symbols:
+ _OBJC_CLASS_$_NSString
+ __ZN4bssl22dtls_max_seal_overheadEPK6ssl_stt
+ _cchkdf
+ _cckem_decapsulate
+ _cckem_encapsulate
+ _cckem_export_pubkey
+ _cckem_full_ctx_init
+ _cckem_generate_key
+ _cckem_import_pubkey
+ _cckem_kyber768
+ _cckem_pub_ctx_init
+ _cckem_public_ctx
+ _cckem_sizeof_full_ctx
+ _cckem_sizeof_pub_ctx
+ _nw_endpoint_create_host_with_numeric_port
+ _nw_path_is_direct
+ _nw_path_is_local
+ _nw_protocol_get_input_handler
+ _nw_protocol_get_path
+ _nw_settings_get_pqtls_enabled
+ _objc_msgSend
+ _objc_retain_x26
+ _sec_identity_copy_SPAKE2PLUSV1_client_identity
+ _sec_identity_copy_SPAKE2PLUSV1_client_password_verifier
+ _sec_identity_copy_SPAKE2PLUSV1_context
+ _sec_identity_copy_SPAKE2PLUSV1_registration_record
+ _sec_identity_copy_SPAKE2PLUSV1_server_identity
+ _sec_identity_copy_SPAKE2PLUSV1_server_password_verifier
+ _sec_identity_copy_type
+ _sec_protocol_configuration_copy_transformed_options_for_address
+ _sec_protocol_configuration_copy_transformed_options_for_host
- __ZN4bssl22dtls_max_seal_overheadEPK6ssl_stNS_17dtls1_use_epoch_tE
CStrings:
+ "!buffers_alias(out, in_len, in, in_len) || in == out"
+ "!hs->received_hello_verify_request"
+ "%{public}s(%d) %{public}s[%p] Invalid sec_identity provided (SEC_PROTOCOL_IDENTITY_TYPE_INVALID)"
+ "%{public}s(%d) %{public}s[%p] SSL_shutdown returned. Disconnect successful? %@"
+ "%{public}s(%d) %{public}s[%p] TLS configured [min_version(0x%04x) max_version(0x%04x) name(%{public}s) tickets(%{bool}d) false_start(%{bool}d) enforce_ev(%{bool}d) enforce_ats(%{bool}d) ats_non_pfs_ciphersuite_allowed(%{bool}d) ech(%{bool}d) pqtls(%{bool}d)]"
+ "%{public}s(%d) %{public}s[%p] Unsupported sec_identity provided (%d)"
+ "%{public}s(%d) %{public}s[%p] boringssl session state changed from %s to %s"
+ "%{public}s(%d) %{public}s[%p] calling SSL_shutdown."
+ "%{public}s(%d) %{public}s[%p] secret_len: %zu, identity_len: %zu"
+ "%{public}s(%d) KYBER_private_key not initialized"
+ "%{public}s(%d) KYBER_public_key not initialized"
+ "%{public}s(%d) MLKEM768_private_key not initialized"
+ "%{public}s(%d) MLKEM768_public_key not initialized"
+ "%{public}s(%d) cckem_decapsulate failed"
+ "%{public}s(%d) cckem_encapsulate failed"
+ "%{public}s(%d) cckem_export_pubkey failed"
+ "."
+ ".local"
+ ".local."
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/add.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/bn.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/ctx.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/div.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/exponentiation.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/jacobi.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/montgomery.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/mul.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/prime.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/random.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/shift.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/sqrt.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/cipher/aead.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/cipher/cipher.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/digest/digest.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/digestsign/digestsign.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/ec.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/ec_key.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/ec_montgomery.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/felem.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/oct.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/p224-64.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/p256.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/scalar.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/simple.c.inc"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/rsa/padding.c.inc"
+ "BN_div"
+ "CRYPTO_chacha_20"
+ "ConfirmationKeys"
+ "DTLSv1.3"
+ "KYBER_decap"
+ "KYBER_encap"
+ "KYBER_generate_key"
+ "KYBER_parse_public_key"
+ "MLKEM768_decap"
+ "MLKEM768_encap"
+ "MLKEM768_generate_key"
+ "MLKEM768_parse_public_key"
+ "SharedKey"
+ "X25519MLKEM768"
+ "aead.c.inc"
+ "aes_nohw.c.inc"
+ "aes_nohw_from_batch"
+ "aes_nohw_to_batch"
+ "ats_non_pfs_ciphersuite_allowed"
+ "began nw_protocol_boringssl_disconnect: boringssl session state is: %s"
+ "bn.c.inc"
+ "boringssl called disconnect down the stack"
+ "boringssl_context_set_ats_non_pfs_ciphersuite_allowed"
+ "boringssl_context_set_identity"
+ "boringssl_session_disconnect"
+ "boringssl_session_set_state"
+ "bytes.c.inc"
+ "chacha.c"
+ "cipher->algorithm_enc & (SSL_AES128GCM | SSL_AES256GCM)"
+ "cipher.c.inc"
+ "containsString:"
+ "ctx.c.inc"
+ "d0 & (((BN_ULONG)1) << (BN_BITS2 - 1))"
+ "digest.c.inc"
+ "digest_len == hs->new_session->original_handshake_hash.size()"
+ "div.c.inc"
+ "div_extra.c.inc"
+ "ec.c.inc"
+ "ec_key.c.inc"
+ "exponentiation.c.inc"
+ "felem.c.inc"
+ "handle_hello_verify_request"
+ "hasSuffix:"
+ "kdf.c.inc"
+ "len == hs->secret.size()"
+ "montgomery_inv.c.inc"
+ "msg.type == DTLS1_MT_HELLO_VERIFY_REQUEST"
+ "mul.c.inc"
+ "n0 < d0"
+ "nonce_len == fixed_nonce_.size()"
+ "nope"
+ "num_blocks <= AES_NOHW_BATCH_SIZE"
+ "nw_protocol_boringssl_disconnect has been called re-entrantly and will call boringssl_session_disconnect a second time."
+ "oct.c.inc"
+ "p224-64.c.inc"
+ "p256.c.inc"
+ "padding.c.inc"
+ "pqtls_enabled"
+ "prime.c.inc"
+ "random.c.inc"
+ "seal_next_message"
+ "session->secret.size() == EVP_MD_size(digest)"
+ "sha256.c.inc"
+ "sha512.c.inc"
+ "sn"
+ "ssl->d1->outgoing_written < ssl->d1->outgoing_messages.size()"
+ "ssl->s3->initial_handshake_complete == !ssl->s3->previous_client_finished.empty()"
+ "ssl->s3->previous_client_finished.size() == ssl->s3->previous_server_finished.size()"
+ "ssl->s3->version != 0"
+ "ssl->s3->version == 0"
+ "ssl->s3->version == 0 || (hs->early_data_offered && ssl->s3->version == hs->early_session->ssl_version)"
+ "ssl_protocol_version(ssl) < TLS1_3_VERSION"
+ "ssl_record_prefix_len"
+ "ssl_session_protocol_version(hs->early_session.get()) >= TLS1_3_VERSION"
+ "stringWithUTF8String:"
+ "tls13_derive_session_psk"
+ "tls1_record_handshake_hashes_for_channel_id"
+ "wnaf.c.inc"
+ "yes"
- "!expected_len || ssl->s3->previous_client_finished_len"
- "!expected_len || ssl->s3->previous_server_finished_len"
- "!ssl->s3->have_version"
- "%{public}s(%d) %{public}s[%p] TLS configured [min_version(0x%04x) max_version(0x%04x) name(%{public}s) tickets(%{bool}d) false_start(%{bool}d) enforce_ev(%{bool}d) enforce_ats(%{bool}d) ech(%{bool}d)]"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/add.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/bn.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/ctx.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/div.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/exponentiation.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/jacobi.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/montgomery.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/mul.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/prime.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/random.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/shift.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/bn/sqrt.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/cipher/aead.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/cipher/cipher.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/digest/digest.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/digestsign/digestsign.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/ec.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/ec_key.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/ec_montgomery.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/felem.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/oct.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/p224-64.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/p256.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/scalar.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/simple.c"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/rsa/padding.c"
- "0 `"
- "BORINGSSL_keccak_absorb"
- "CBS_len(&server_hello.session_id) <= SSL3_SESSION_ID_SIZE"
- "ProtocolVersion"
- "RecordVersion"
- "TLS client read_hello_verify_request"
- "aead.c"
- "aead_ctx->ProtocolVersion() == protocol_version"
- "bn.c"
- "bytes.c"
- "cipher.c"
- "ciphertext_len == len_copy"
- "compress"
- "ctx->absorb_offset < ctx->rate_bytes"
- "ctx.c"
- "digest.c"
- "div.c"
- "div_extra.c"
- "do_read_hello_verify_request"
- "dtls_record.cc"
- "dtls_seal_record"
- "ec.c"
- "ec_key.c"
- "exponentiation.c"
- "felem.c"
- "fixed_iv.size() <= sizeof(aead_ctx->fixed_nonce_)"
- "get_write_aead"
- "hs->expected_client_finished().size() <= 0xff"
- "hs->max_version < TLS1_3_VERSION"
- "hs->session_id_len <= sizeof(hs->session_id)"
- "is_null_cipher()"
- "kdf.c"
- "keccak.c"
- "keccak_ctx->rate_bytes == 168"
- "keccak_ctx->squeeze_offset == 0"
- "kyber.c"
- "len == hs->secret().size()"
- "montgomery_inv.c"
- "mul.c"
- "nonce_len == fixed_nonce_len_"
- "oct.c"
- "p224-64.c"
- "p256.c"
- "padding.c"
- "prime.c"
- "random.c"
- "reduce"
- "reduce_once"
- "remainder < 2u * kPrime"
- "scalar_from_keccak_vartime"
- "sha256.c"
- "sha512.c"
- "ssl->d1->w_epoch >= 1"
- "ssl->s3->have_version"
- "ssl->s3->have_version == ssl->s3->initial_handshake_complete"
- "ssl->s3->initial_handshake_complete == (ssl->s3->previous_client_finished_len != 0)"
- "ssl->s3->initial_handshake_complete == (ssl->s3->previous_server_finished_len != 0)"
- "wnaf.c"
- "x < 2 * kPrime"
- "x < kPrime + 2u * kPrime * kPrime"

```
