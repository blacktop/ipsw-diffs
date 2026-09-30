## ssh-pkcs11-helper

> `/usr/libexec/ssh-pkcs11-helper`

```diff

-342.0.0.0.0
-  __TEXT.__text: 0x104a4
-  __TEXT.__auth_stubs: 0xbb0
-  __TEXT.__const: 0x1af08
-  __TEXT.__cstring: 0x1ff9
-  __TEXT.__unwind_info: 0x2d8
-  __DATA_CONST.__auth_got: 0x5d8
+346.0.0.0.0
+  __TEXT.__text: 0x10934
+  __TEXT.__auth_stubs: 0xca0
+  __TEXT.__const: 0x1aee0
+  __TEXT.__cstring: 0x210a
+  __TEXT.__unwind_info: 0x2f0
+  __DATA_CONST.__auth_got: 0x650
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0x868

   - /usr/lib/libpam.2.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 398E21A6-FD57-379B-977F-81AE69F00860
-  Functions: 226
-  Symbols:   199
-  CStrings:  328
+  UUID: DB7D7F25-455E-3885-AF59-3FF488D16AEB
+  Functions: 231
+  Symbols:   211
+  CStrings:  342
 
Symbols:
+ _EVP_DigestSignFinal
+ _EVP_DigestSignInit
+ _EVP_DigestUpdate
+ _EVP_DigestVerifyFinal
+ _EVP_DigestVerifyInit
+ _EVP_MD_CTX_free
+ _EVP_MD_CTX_new
+ _EVP_PKEY_CTX_ctrl
+ _EVP_PKEY_CTX_free
+ _EVP_PKEY_CTX_new_id
+ _EVP_PKEY_bits
+ _EVP_PKEY_cmp
+ _EVP_PKEY_free
+ _EVP_PKEY_get1_EC_KEY
+ _EVP_PKEY_get1_RSA
+ _EVP_PKEY_keygen
+ _EVP_PKEY_keygen_init
+ _EVP_PKEY_new
+ _EVP_PKEY_set1_EC_KEY
+ _EVP_PKEY_set1_RSA
+ _EVP_PKEY_size
+ _RSA_pkey_ctx_ctrl
+ _d2i_ECDSA_SIG
+ _i2d_ECDSA_SIG
- _BN_set_word
- _ECDSA_do_sign
- _ECDSA_do_verify
- _EC_GROUP_cmp
- _EC_GROUP_new_by_curve_name
- _EC_GROUP_set_asn1_flag
- _EC_KEY_generate_key
- _EC_KEY_set_asn1_flag
- _EC_POINT_cmp
- _RSA_generate_key_ex
- _RSA_public_decrypt
- _RSA_sign
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/dlopen_lv.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/entropy.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/misc.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/readpass.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-ed25519-sk.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-ed25519.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-pkcs11-helper.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-pkcs11.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/xmalloc.c"
+ "ECDSA_sign failed"
+ "EC_KEY_set_ex_data failed"
+ "EC_KEY_set_method failed"
+ "EVP_PKEY_new failed"
+ "EVP_PKEY_set1_EC_KEY failed"
+ "EVP_PKEY_set1_RSA failed"
+ "RSA_private_encrypt failed"
+ "RSA_set_ex_data failed"
+ "RSA_set_method failed"
+ "bad ECDSA length"
+ "bad RSA length"
+ "no ECDSA in pkey"
+ "no RSA in pkey"
+ "pkcs11_ecdsa_wrap"
+ "pkcs11_rsa_wrap"
+ "unsupported key type %d"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/dlopen_lv.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/entropy.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/misc.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/readpass.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-ed25519-sk.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-ed25519.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-pkcs11-helper.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-pkcs11.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/xmalloc.c"
- "ECDSA_sign returned %d"
- "don't know how to sign with key type %d"

```
