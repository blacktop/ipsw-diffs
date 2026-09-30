## ssh-agent

> `/usr/bin/ssh-agent`

```diff

-342.0.0.0.0
-  __TEXT.__text: 0x18654
-  __TEXT.__auth_stubs: 0xce0
-  __TEXT.__const: 0x1bfd0
-  __TEXT.__cstring: 0x3602
-  __TEXT.__unwind_info: 0x3c8
-  __DATA_CONST.__auth_got: 0x670
+346.0.0.0.0
+  __TEXT.__text: 0x189a0
+  __TEXT.__auth_stubs: 0xdb0
+  __TEXT.__const: 0x1bfa0
+  __TEXT.__cstring: 0x36c4
+  __TEXT.__unwind_info: 0x3e0
+  __DATA_CONST.__auth_got: 0x6d8
   __DATA_CONST.__got: 0x48
   __DATA_CONST.__auth_ptr: 0x18
   __DATA_CONST.__const: 0xa48

   - /usr/lib/libpam.2.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 3CC703BD-D076-3742-9B54-320C98DB19DE
-  Functions: 310
-  Symbols:   229
-  CStrings:  537
+  UUID: 6EA617B1-D265-3133-AAD2-67E30E8C4C3A
+  Functions: 314
+  Symbols:   239
+  CStrings:  547
 
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
+ _EVP_PKEY_get0_EC_KEY
+ _EVP_PKEY_get0_RSA
+ _EVP_PKEY_get1_EC_KEY
+ _EVP_PKEY_get1_RSA
+ _EVP_PKEY_keygen
+ _EVP_PKEY_keygen_init
+ _EVP_PKEY_new
+ _EVP_PKEY_set1_EC_KEY
+ _EVP_PKEY_set1_RSA
+ _EVP_PKEY_size
+ _RSA_pkey_ctx_ctrl
+ _i2d_ECDSA_SIG
+ _mmap
+ _munmap
- _BN_free
- _BN_set_word
- _ECDSA_do_sign
- _ECDSA_do_verify
- _EC_GROUP_cmp
- _EC_GROUP_free
- _EC_GROUP_new_by_curve_name
- _EC_GROUP_set_asn1_flag
- _EC_KEY_generate_key
- _EC_KEY_set_asn1_flag
- _EC_KEY_set_group
- _EC_KEY_up_ref
- _EC_POINT_cmp
- _RSA_generate_key_ex
- _RSA_public_decrypt
- _RSA_sign
- _RSA_up_ref
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/entropy.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/misc.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/msg.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/platform-tracing.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/readpass.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-agent.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-ed25519-sk.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-ed25519.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-pkcs11-client.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-sk-client.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/xmalloc.c"
+ "EC_KEY_set_method failed"
+ "EVP_PKEY_set1_EC_KEY failed"
+ "EVP_PKEY_set1_RSA failed"
+ "RSA_set_method failed"
+ "no EC cert pkey"
+ "no EC pkey"
+ "no ECDSA key"
+ "no RSA cert pkey"
+ "no RSA key"
+ "no RSA pkey"
+ "pkey setup failed"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/entropy.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/misc.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/msg.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/platform-tracing.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/readpass.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-agent.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-ed25519-sk.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-ed25519.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-pkcs11-client.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-sk-client.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/xmalloc.c"
- "csh"

```
