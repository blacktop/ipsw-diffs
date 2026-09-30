## ssh-keygen

> `/usr/bin/ssh-keygen`

```diff

-342.0.0.0.0
-  __TEXT.__text: 0x2d120
-  __TEXT.__auth_stubs: 0x1410
-  __TEXT.__const: 0x1bff0
-  __TEXT.__cstring: 0x79ab
-  __TEXT.__unwind_info: 0x638
-  __DATA_CONST.__auth_got: 0xa08
+346.0.0.0.0
+  __TEXT.__text: 0x2d454
+  __TEXT.__auth_stubs: 0x14c0
+  __TEXT.__const: 0x1bfa0
+  __TEXT.__cstring: 0x7ad5
+  __TEXT.__unwind_info: 0x650
+  __DATA_CONST.__auth_got: 0xa60
   __DATA_CONST.__got: 0x58
   __DATA_CONST.__auth_ptr: 0x30
   __DATA_CONST.__const: 0xb50

   - /usr/lib/libpam.2.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 0FB39AF9-0EF0-3C83-9BE5-509BCC359460
-  Functions: 503
-  Symbols:   345
-  CStrings:  1181
+  UUID: 17787FC2-D270-3FC6-A986-76AD11793DD7
+  Functions: 506
+  Symbols:   353
+  CStrings:  1191
 
Symbols:
+ _EVP_DigestSignFinal
+ _EVP_DigestSignInit
+ _EVP_DigestVerifyFinal
+ _EVP_DigestVerifyInit
+ _EVP_PKEY_CTX_ctrl
+ _EVP_PKEY_CTX_free
+ _EVP_PKEY_CTX_new_id
+ _EVP_PKEY_bits
+ _EVP_PKEY_cmp
+ _EVP_PKEY_keygen
+ _EVP_PKEY_keygen_init
+ _EVP_PKEY_size
+ _EVP_PKEY_up_ref
+ _RSA_pkey_ctx_ctrl
+ _d2i_ECDSA_SIG
+ _i2d_ECDSA_SIG
- _ECDSA_do_sign
- _ECDSA_do_verify
- _EC_KEY_generate_key
- _EC_KEY_set_asn1_flag
- _EC_POINT_cmp
- _RSA_generate_key_ex
- _RSA_public_decrypt
- _RSA_sign
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/dlopen_lv.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/addrmatch.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/authfd.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/authfile.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/dns.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/entropy.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/hostfile.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/krl.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/misc.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/moduli.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/msg.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/readpass.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-ed25519-sk.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-ed25519.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-keygen.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-pkcs11.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-sk-client.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/sshsig.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/xmalloc.c"
+ "EC_KEY_set_ex_data failed"
+ "EC_KEY_set_method failed"
+ "EVP_PKEY_new failed"
+ "EVP_PKEY_set1_EC_KEY failed"
+ "EVP_PKEY_set1_RSA failed"
+ "Enter passphrase for \"%s\" (empty for no passphrase): "
+ "Enter passphrase for \"%s\": "
+ "RSA_set0_crt_params failed"
+ "RSA_set_ex_data failed"
+ "RSA_set_method failed"
+ "generate RSA CRT parameters"
+ "pkcs11_ecdsa_wrap"
+ "pkcs11_rsa_wrap"
+ "sshkey_ecdsa_fixup_group failed"
- "-"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/dlopen_lv.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/addrmatch.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/authfd.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/authfile.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/dns.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/entropy.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/hostfile.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/krl.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/misc.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/moduli.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/msg.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/readpass.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-ed25519-sk.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-ed25519.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-keygen.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-pkcs11.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-sk-client.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/sshsig.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/xmalloc.c"
- "0x"
- "Enter passphrase (empty for no passphrase): "
- "generate RSA parameters"

```
