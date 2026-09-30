## ssh-keyscan

> `/usr/bin/ssh-keyscan`

```diff

-342.0.0.0.0
-  __TEXT.__text: 0x1c510
-  __TEXT.__auth_stubs: 0xc40
-  __TEXT.__const: 0x1afb0
-  __TEXT.__cstring: 0x4a5a
-  __TEXT.__unwind_info: 0x548
-  __DATA_CONST.__auth_got: 0x620
+346.0.0.0.0
+  __TEXT.__text: 0x24d58
+  __TEXT.__auth_stubs: 0xd60
+  __TEXT.__const: 0x1b210
+  __TEXT.__cstring: 0x4b4e
+  __TEXT.__unwind_info: 0x570
+  __TEXT.__eh_frame: 0x68
+  __DATA_CONST.__auth_got: 0x6b0
   __DATA_CONST.__got: 0x50
-  __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0xfe8
+  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__const: 0x1018
   __DATA.__data: 0x20
   __DATA.__common: 0x44
   __DATA.__bss: 0x6d

   - /usr/lib/libpam.2.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  UUID: DE842346-31BD-37C1-B8C0-9599F4A3F52F
-  Functions: 441
-  Symbols:   220
-  CStrings:  539
+  UUID: D48F6BFC-8D78-3EC2-AF7C-CD00AEC1F22C
+  Functions: 459
+  Symbols:   235
+  CStrings:  541
 
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
+ ___memcpy_chk
+ _d2i_ECDSA_SIG
+ _i2d_ECDSA_SIG
+ _munmap
- _BN_set_word
- _ECDSA_do_sign
- _ECDSA_do_verify
- _EC_GROUP_cmp
- _EC_KEY_set_asn1_flag
- _EC_POINT_cmp
- _RSA_generate_key_ex
- _RSA_public_decrypt
- _RSA_sign
- _RSA_size
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/canohost.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/compat.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/dh.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/dispatch.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/dns.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/entropy.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/hostfile.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/kex.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/kexgen.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/kexgexc.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/libcrux_mlkem768_sha3.h"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/misc.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/packet.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-ed25519-sk.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-ed25519.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-keyscan.c"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/xmalloc.c"
+ "mlkem768x25519-sha256"
+ "sntrup761x25519-sha512"
+ "sntrup761x25519-sha512,sntrup761x25519-sha512@openssh.com,mlkem768x25519-sha256,curve25519-sha256,curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group16-sha512,diffie-hellman-group18-sha512,diffie-hellman-group14-sha256"
+ "unwrap_41_ac"
- "-"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/canohost.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/compat.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/dh.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/dispatch.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/dns.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/entropy.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/hostfile.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/kex.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/kexgen.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/kexgexc.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/misc.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/packet.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-ed25519-sk.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-ed25519.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/ssh-keyscan.c"
- "/AppleInternal/Library/BuildRoots/d187755d-b9a3-11ef-83e5-aabfac210453/Library/Caches/com.apple.xbs/Sources/OpenSSH/openssh/xmalloc.c"
- "sntrup761x25519-sha512@openssh.com,curve25519-sha256,curve25519-sha256@libssh.org,ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521,diffie-hellman-group-exchange-sha256,diffie-hellman-group16-sha512,diffie-hellman-group18-sha512,diffie-hellman-group14-sha256"
- "zlib"

```
