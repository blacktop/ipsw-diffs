## ssh-keygen

> `/usr/bin/ssh-keygen`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__auth_got`

```diff

-369.0.4.0.0
-  __TEXT.__text: 0x2d4e8
+369.40.2.0.0
+  __TEXT.__text: 0x4306c
   __TEXT.__auth_stubs: 0x12a0
-  __TEXT.__const: 0x1bff8
-  __TEXT.__cstring: 0x7ea5
-  __TEXT.__unwind_info: 0x848
-  __DATA_CONST.__const: 0xa90
+  __TEXT.__const: 0x1c0f8
+  __TEXT.__cstring: 0x80af
+  __TEXT.__unwind_info: 0x8e0
+  __TEXT.__eh_frame: 0x50
+  __DATA_CONST.__const: 0xb98
   __DATA_CONST.__auth_got: 0x950
   __DATA_CONST.__got: 0x58
-  __DATA_CONST.__auth_ptr: 0x38
+  __DATA_CONST.__auth_ptr: 0x40
   __DATA.__data: 0x20
   __DATA.__common: 0x30
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libpam.2.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 497
+  Functions: 531
   Symbols:   319
-  CStrings:  1196
+  CStrings:  1210
 
Symbols:
+ _fileno
- _ERR_load_crypto_strings
CStrings:
+ "%s: original FIDO key flags: %stouch-required %sverify-required"
+ "%s: updated FIDO key flags: %stouch-required %sverify-required"
+ ".ssh/id_mldsa44_ed25519"
+ "/etc/ssh/ssh_host_mldsa44_ed25519_key"
+ "COMPSIG-MLDSA44-Ed25519-SHA512"
+ "CompositeAlgorithmSignatures2025"
+ "FIDO-specific option requested for non-FIDO key %s"
+ "MLDSA44-ED25519"
+ "MLDSA44-ED25519-CERT"
+ "Option \"%s\" is unsupported for key passphrase change"
+ "cryptographic operation failed"
+ "mldsa44-ed25519"
+ "ssh-mldsa44-ed25519-cert-v01@openssh.com"
+ "ssh-mldsa44-ed25519@openssh.com"
+ "usage: ssh-keygen [-q] [-a rounds] [-b bits] [-C comment] [-f output_keyfile]\n                  [-m format] [-N new_passphrase] [-O option]\n                  [-t ecdsa|ecdsa-sk|ed25519|ed25519-sk|mldsa44-ed25519|rsa]\n                  [-w provider] [-Z cipher]\n       ssh-keygen -p [-a rounds] [-f keyfile] [-m format] [-N new_passphrase]\n                   [-P old_passphrase] [-Z cipher]\n       ssh-keygen -i [-f input_keyfile] [-m key_format]\n       ssh-keygen -e [-f input_keyfile] [-m key_format]\n       ssh-keygen -y [-f input_keyfile]\n       ssh-keygen -c [-a rounds] [-C comment] [-f keyfile] [-P passphrase]\n       ssh-keygen -l [-v] [-E fingerprint_hash] [-f input_keyfile]\n       ssh-keygen -B [-f input_keyfile]\n"
- "usage: ssh-keygen [-q] [-a rounds] [-b bits] [-C comment] [-f output_keyfile]\n                  [-m format] [-N new_passphrase] [-O option]\n                  [-t ecdsa | ecdsa-sk | ed25519 | ed25519-sk | rsa]\n                  [-w provider] [-Z cipher]\n       ssh-keygen -p [-a rounds] [-f keyfile] [-m format] [-N new_passphrase]\n                   [-P old_passphrase] [-Z cipher]\n       ssh-keygen -i [-f input_keyfile] [-m key_format]\n       ssh-keygen -e [-f input_keyfile] [-m key_format]\n       ssh-keygen -y [-f input_keyfile]\n       ssh-keygen -c [-a rounds] [-C comment] [-f keyfile] [-P passphrase]\n       ssh-keygen -l [-v] [-E fingerprint_hash] [-f input_keyfile]\n       ssh-keygen -B [-f input_keyfile]\n"
```
