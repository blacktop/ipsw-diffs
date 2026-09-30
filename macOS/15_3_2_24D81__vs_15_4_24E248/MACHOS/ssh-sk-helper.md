## ssh-sk-helper

> `/usr/libexec/ssh-sk-helper`

```diff

-342.0.0.0.0
-  __TEXT.__text: 0xfc88
-  __TEXT.__auth_stubs: 0x8d0
-  __TEXT.__const: 0x1aeb8
-  __TEXT.__cstring: 0x19f1
-  __TEXT.__unwind_info: 0x2f8
-  __DATA_CONST.__auth_got: 0x468
+346.0.0.0.0
+  __TEXT.__text: 0xfdc0
+  __TEXT.__auth_stubs: 0x9e0
+  __TEXT.__const: 0x1ae90
+  __TEXT.__cstring: 0x1a09
+  __TEXT.__unwind_info: 0x310
+  __DATA_CONST.__auth_got: 0x4f0
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__const: 0xae8

   - /usr/lib/libpam.2.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  UUID: A0E3A400-882C-397E-9534-39E42EAA6A56
-  Functions: 234
-  Symbols:   162
-  CStrings:  273
+  UUID: D1E2F897-95CA-339C-A0DF-1F627F3A664D
+  Functions: 236
+  Symbols:   176
+  CStrings:  274
 
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
+ _d2i_ECDSA_SIG
+ _i2d_ECDSA_SIG
- _BN_free
- _BN_set_word
- _ECDSA_do_sign
- _ECDSA_do_verify
- _EC_GROUP_cmp
- _EC_KEY_generate_key
- _EC_KEY_set_asn1_flag
- _EC_POINT_cmp
- _RSA_generate_key_ex
- _RSA_public_decrypt
- _RSA_sign
- _RSA_size
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/dlopen_lv.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/misc.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/msg.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-ed25519-sk.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-ed25519.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-sk-helper.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-sk.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/xmalloc.c"
+ "Assigning EC_KEY failed"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/dlopen_lv.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/misc.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/msg.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-ed25519-sk.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-ed25519.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-sk-helper.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-sk.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/xmalloc.c"

```
