## libboringssl.dylib

> `/usr/lib/libboringssl.dylib`

```diff

-486.0.10.0.0
-  __TEXT.__text: 0x982b8
-  __TEXT.__auth_stubs: 0x1770
+486.60.4.0.0
+  __TEXT.__text: 0x98178
+  __TEXT.__auth_stubs: 0x1790
   __TEXT.__objc_methlist: 0xd8
-  __TEXT.__cstring: 0xfc0e
-  __TEXT.__const: 0x10c48
-  __TEXT.__oslogstring: 0x5315
-  __TEXT.__gcc_except_tab: 0x28cc
-  __TEXT.__unwind_info: 0x2140
+  __TEXT.__cstring: 0x103ac
+  __TEXT.__const: 0x10068
+  __TEXT.__oslogstring: 0x5362
+  __TEXT.__gcc_except_tab: 0x2978
+  __TEXT.__unwind_info: 0x21f8
   __TEXT.__eh_frame: 0xe8
   __TEXT.__objc_classname: 0x245
   __TEXT.__objc_methname: 0xe17
   __TEXT.__objc_methtype: 0x6f7
   __DATA_CONST.__got: 0xb8
-  __DATA_CONST.__const: 0xb590
+  __DATA_CONST.__const: 0xb7f0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0xbc8
-  __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x16b0
+  __AUTH_CONST.__auth_got: 0xbd8
+  __AUTH_CONST.__auth_ptr: 0x20
+  __AUTH_CONST.__const: 0x1618
   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0x2318
   __AUTH.__objc_data: 0x140
   __AUTH.__data: 0x28
   __DATA.__objc_ivar: 0x2f8
-  __DATA.__data: 0xab0
-  __DATA.__bss: 0x110
+  __DATA.__data: 0xcd8
+  __DATA.__bss: 0x990
   __DATA_DIRTY.__objc_data: 0x140
-  __DATA_DIRTY.__data: 0x2c0
-  __DATA_DIRTY.__bss: 0xab8
+  __DATA_DIRTY.__data: 0x1f0
+  __DATA_DIRTY.__bss: 0x970
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 2950
-  Symbols:   3424
-  CStrings:  3492
+  Functions: 2984
+  Symbols:   3465
+  CStrings:  3584
 
Symbols:
+ _CRYPTO_get_ex_new_index_ex
+ __ZdlPvSt19__type_descriptor_t
+ _snprintf
- _CBS_data
- _CBS_init
- _CBS_len
- _CRYPTO_get_ex_new_index
- _SSL_CIPHER_get_value
- _SSL_CTX_set1_curves
- _SSL_get_curve_id
- _SSL_set1_curves
- __ZTIN4bssl11SSLKeyShareE
- _rsa_default_decrypt
- _sk_deep_copy
- _sk_free
- _sk_new_null
- _sk_num
- _sk_pop
- _sk_pop_free_ex
- _sk_push
- _sk_set
- _sk_shift
- _sk_value
CStrings:
+ "!BN_is_negative(&mont->N)"
+ "!BN_is_zero(&mont->N)"
+ "!buffers_alias(dst, n, src, n)"
+ "%!{(MISSING)public}s(%!d(MISSING)) RSA_padding_add_PKCS1_OAEP_mgf1 not implemented"
+ "%!{(MISSING)public}s(%!d(MISSING)) RSA_padding_check_PKCS1_OAEP_mgf1 not implemented"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/stack/stack.c"
+ "/Library/Caches/com.apple.xbs/Sources/boringssl/ssl/ssl_credential.cc"
+ "ASN1"
+ "ASN1_LIB"
+ "BIO"
+ "BIO_LIB"
+ "BN"
+ "BN_LIB"
+ "BORINGSSL_keccak_absorb"
+ "BUF"
+ "BUF_LIB"
+ "CBS_len(&server_hello.session_id) <= SSL3_SESSION_ID_SIZE"
+ "CIPHER"
+ "CIPHER_LIB"
+ "COMP"
+ "COMP_LIB"
+ "CONF"
+ "CONF_LIB"
+ "CRYPTO"
+ "CRYPTO_LIB"
+ "CRYPTO_addc_u64"
+ "CRYPTO_get_ex_new_index_ex"
+ "CRYPTO_subc_u64"
+ "DH"
+ "DH_LIB"
+ "DIGEST"
+ "DIGEST_LIB"
+ "DSA_LIB"
+ "Decap"
+ "Dup"
+ "EC"
+ "ECDHE-RSA-AES128-SHA256"
+ "ECDH_LIB"
+ "ECDSA_LIB"
+ "EC_LIB"
+ "ENGINE"
+ "ENGINE_LIB"
+ "EVP"
+ "EVP_LIB"
+ "Generate"
+ "HKDF_LIB"
+ "HMAC_LIB"
+ "INTERNAL_ERROR"
+ "MALLOC_FAILURE"
+ "NONE"
+ "NONE_LIB"
+ "OBJ"
+ "OBJ_LIB"
+ "OCSP_LIB"
+ "OPENSSL_sk_find"
+ "OVERFLOW"
+ "PASSED_NULL_PARAMETER"
+ "PEM"
+ "PEM_LIB"
+ "PKCS7"
+ "PKCS7_LIB"
+ "PKCS8"
+ "PKCS8_LIB"
+ "RAND"
+ "RAND_LIB"
+ "RSA_LIB"
+ "RSA_padding_add_PKCS1_OAEP_mgf1"
+ "RSA_padding_check_PKCS1_OAEP_mgf1"
+ "SHOULD_NOT_HAVE_BEEN_CALLED"
+ "SSL"
+ "SSL_CIPHER_get_handshake_digest"
+ "SSL_LIB"
+ "SYS"
+ "SYS_LIB"
+ "TLS server cert_callback"
+ "TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256"
+ "TRUST_TOKEN"
+ "TRUST_TOKEN_LIB"
+ "UI"
+ "UI_LIB"
+ "USER"
+ "USER_LIB"
+ "X25519Kyber768Draft00"
+ "X509V3"
+ "X509V3_LIB"
+ "X509_LIB"
+ "ab"
+ "ab+"
+ "bn.c"
+ "bn_minimal_width(&mont->N) == mont->N.width"
+ "bn_mont_ctx_set_RR_consttime"
+ "bn_set_static_words"
+ "co_list[num - 1].cipher != nullptr"
+ "compress"
+ "constant_time_conditional_memxor"
+ "constant_time_declassify_int((s[31] & 0x80) == 0)"
+ "constant_time_declassify_int(1 == ((uint128_t)u * 2 * alpha) - ((uint128_t)v * beta))"
+ "constant_time_declassify_int(BN_ucmp(a, m) < 0)"
+ "constant_time_declassify_int(b < 16)"
+ "constant_time_declassify_int(bn_in_range_words(r->d, min_inclusive, max_exclusive->d, words))"
+ "constant_time_declassify_int(borrow <= 1)"
+ "constant_time_declassify_int(c == 0)"
+ "constant_time_declassify_int(carry + 1 <= 1)"
+ "constant_time_declassify_int(carry <= 1)"
+ "constant_time_declassify_int(f->v[_assert_fe_i] <= (0x1a666666666664ULL))"
+ "constant_time_declassify_int(f->v[_assert_fe_i] <= (0x8ccccccccccccULL))"
+ "constant_time_declassify_int(fits_in_bytes(in, in_len, out_len))"
+ "constant_time_declassify_int(g->v[_assert_fe_i] <= (0x8ccccccccccccULL))"
+ "constant_time_declassify_int(h->v[_assert_fe_i] <= (0x1a666666666664ULL))"
+ "constant_time_declassify_int(h->v[_assert_fe_i] <= (0x8ccccccccccccULL))"
+ "constant_time_declassify_int(in1[_assert_fe_i] <= (0x1a666666666664ULL))"
+ "constant_time_declassify_int(in2[_assert_fe_i] <= (0x1a666666666664ULL))"
+ "constant_time_declassify_int(n < d)"
+ "constant_time_declassify_int(out[_assert_fe_i] <= (0x8ccccccccccccULL))"
+ "constant_time_declassify_int(uniform_iterations >= (crypto_word_t)checks)"
+ "ctx->absorb_offset < ctx->rate_bytes"
+ "do_cert_callback"
+ "ext_alps_parse_serverhello_impl"
+ "ext_sct_add_serverhello"
+ "field_len == BN_num_bytes(&group->field.N)"
+ "group->field.N.width == group->order.N.width"
+ "group->has_order"
+ "has_ecdhe_group"
+ "hex_char_consttime"
+ "hs->credential != nullptr"
+ "hs->credential->UsesX509()"
+ "hs->credential->type == SSLCredentialType::kX509"
+ "hs->new_session->group_id != 0"
+ "hs->scts_requested"
+ "hs->signature_algorithm != 0"
+ "keccak.c"
+ "keccak_ctx->rate_bytes == 168"
+ "keccak_ctx->squeeze_offset == 0"
+ "kyber.c"
+ "lgBigR >= n_bits"
+ "num <= BN_MAX_WORDS"
+ "num == OPENSSL_ARRAY_SIZE(co_list)"
+ "num_funcs <= (size_t)(INT_MAX - ex_data_class->num_reserved)"
+ "num_funcs == 0"
+ "rb"
+ "rb+"
+ "reduce"
+ "reduce_once"
+ "remainder < 2u * kPrime"
+ "scalar_from_keccak_vartime"
+ "ssl_create_cipher_list"
+ "ssl_credential.cc"
+ "ssl_send_tls12_certificate"
+ "ssl_str_to_group_ids"
+ "threshold == mont->N.width"
+ "tls13_add_certificate_in_buffer"
+ "tls13_add_certificate_verify_in_buffer"
+ "type == SSLCredentialType::kX509"
+ "use_new_codepoint == hs->config->alps_use_new_codepoint"
+ "wb"
+ "x < 2 * kPrime"
+ "x < kPrime + 2u * kPrime * kPrime"
- "!BN_is_zero(&group->order)"
- "!is_zero"
- "%!{(MISSING)public}s(%!d(MISSING)) rsa_default_decrypt not implemented"
- "(s[31] & 0x80) == 0"
- "/Library/Caches/com.apple.xbs/Sources/boringssl/crypto/fipsmodule/ec/wnaf.c"
- "1 == ((BN_ULLONG)u * 2 * alpha) - ((BN_ULLONG)v * beta)"
- "BN_ucmp(a, m) < 0"
- "CECPQ2"
- "Finish"
- "HRSS_poly3_invert"
- "Offer"
- "P256Kyber768"
- "SSL_CIPHER_get_prf_nid"
- "TLS server select_certificate"
- "UNDEF"
- "X25519Kyber768"
- "a"
- "a+"
- "bn_big_endian_to_words"
- "bn_in_range_words(r->d, min_inclusive, max_exclusive->d, words)"
- "bn_mod_exp_base_2_consttime"
- "carry == 0 || carry == (BN_ULONG)-1"
- "coeffs[N-1] == 0"
- "delta == 0"
- "do_select_certificate"
- "ec_felem_equal(group, &group->one, &group->generator->raw.Z)"
- "ec_group_set_generator"
- "ec_point_set_affine_coordinates"
- "ext_alps_parse_serverhello"
- "f->v[_assert_fe_i] <= UINT64_C(0x1a666666666664)"
- "f->v[_assert_fe_i] <= UINT64_C(0x8cccccccccccc)"
- "f.v[0] & 1"
- "field_len == BN_num_bytes(&group->field)"
- "fits_in_bytes(in, in_len, out_len)"
- "g->v[_assert_fe_i] <= UINT64_C(0x8cccccccccccc)"
- "group->field.width == group->order.width"
- "group->generator == NULL"
- "h->v[_assert_fe_i] <= UINT64_C(0x1a666666666664)"
- "h->v[_assert_fe_i] <= UINT64_C(0x8cccccccccccc)"
- "hrss.c"
- "hs->ssl->s3->have_version"
- "in1[_assert_fe_i] <= UINT64_C(0x1a666666666664)"
- "in2[_assert_fe_i] <= UINT64_C(0x1a666666666664)"
- "in_len == 0"
- "n < d"
- "out[_assert_fe_i] <= UINT64_C(0x8cccccccccccc)"
- "p > n_bits"
- "poly_assert_normalized"
- "poly_invert_mod2"
- "poly_marshal_mod3"
- "r"
- "r+"
- "rsa_default_decrypt"
- "sk_CRYPTO_EX_DATA_FUNCS_num(func_pointers) <= (size_t)(INT_MAX - ex_data_class->num_reserved)"
- "sk_find"
- "ssl_can_serve_dc"
- "ssl_has_private_key(hs)"
- "tls13 "
- "tls1_set_curves_list"
- "undefined"
- "uniform_iterations >= (crypto_word_t)checks"
- "w"
- "x->v[N + 1] == 0"
- "x->v[N + 2] == 0"
- "x->v[N] == 0"

```
