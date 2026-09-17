## ssh-keyscan

> `/usr/bin/ssh-keyscan`

### Sections with Same Size but Changed Content

- `__TEXT.__eh_frame`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-369.0.4.0.0
-  __TEXT.__text: 0x22950
-  __TEXT.__auth_stubs: 0xcb0
-  __TEXT.__const: 0x1b208
-  __TEXT.__cstring: 0x4f03
-  __TEXT.__unwind_info: 0x768
+369.40.2.0.0
+  __TEXT.__text: 0x38874
+  __TEXT.__auth_stubs: 0xca0
+  __TEXT.__const: 0x1b260
+  __TEXT.__cstring: 0x4f80
+  __TEXT.__unwind_info: 0x810
   __TEXT.__eh_frame: 0xa0
-  __DATA_CONST.__const: 0xf78
-  __DATA_CONST.__auth_got: 0x658
+  __DATA_CONST.__const: 0x1070
+  __DATA_CONST.__auth_got: 0x650
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__auth_ptr: 0x28
   __DATA.__data: 0x20

   - /usr/lib/libpam.2.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 461
-  Symbols:   224
-  CStrings:  547
+  Functions: 499
+  Symbols:   223
+  CStrings:  555
 
Symbols:
- _ERR_load_crypto_strings
CStrings:
+ "COMPSIG-MLDSA44-Ed25519-SHA512"
+ "CompositeAlgorithmSignatures2025"
+ "MLDSA44-ED25519"
+ "MLDSA44-ED25519-CERT"
+ "SSH-"
+ "cryptographic operation failed"
+ "mlkem768nistp256-sha256"
+ "multiple KEXINIT received from peer"
+ "non-transport message %u received from peer during key exchange"
+ "ssh-mldsa44-ed25519-cert-v01@openssh.com"
+ "ssh-mldsa44-ed25519@openssh.com"
- "%s: bad greeting"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.<TMP>/Sources/OpenSSH/openssh/libcrux_mlkem768_sha3.h"
- "unwrap_26_68"
```
