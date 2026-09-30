## ssh-keysign

> `/usr/libexec/ssh-keysign`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__got`
- `__DATA.__data`

```diff

-369.0.4.0.0
-  __TEXT.__text: 0x1ecd0
-  __TEXT.__auth_stubs: 0xd70
-  __TEXT.__const: 0x1bfb0
-  __TEXT.__cstring: 0x512b
-  __TEXT.__unwind_info: 0x658
-  __DATA_CONST.__const: 0x1d98
-  __DATA_CONST.__auth_got: 0x6b8
+369.40.2.0.0
+  __TEXT.__text: 0x34740
+  __TEXT.__auth_stubs: 0xd60
+  __TEXT.__const: 0x1c0c8
+  __TEXT.__cstring: 0x5285
+  __TEXT.__unwind_info: 0x6f0
+  __TEXT.__eh_frame: 0x50
+  __DATA_CONST.__const: 0x1e90
+  __DATA_CONST.__auth_got: 0x6b0
   __DATA_CONST.__got: 0x38
-  __DATA_CONST.__auth_ptr: 0x30
+  __DATA_CONST.__auth_ptr: 0x38
   __DATA.__data: 0xe0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libpam.2.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 371
-  Symbols:   245
-  CStrings:  839
+  Functions: 405
+  Symbols:   244
+  CStrings:  850
 
Symbols:
- _ERR_load_crypto_strings
CStrings:
+ ".ssh/id_mldsa44_ed25519"
+ "/etc/ssh/ssh_host_mldsa44_ed25519_key"
+ "COMPSIG-MLDSA44-Ed25519-SHA512"
+ "CompositeAlgorithmSignatures2025"
+ "MLDSA44-ED25519"
+ "MLDSA44-ED25519-CERT"
+ "Match directive not supported as a command-line option"
+ "OpenSSH_10.5p1"
+ "cryptographic operation failed"
+ "mlkem768nistp256-sha256"
+ "ssh-mldsa44-ed25519-cert-v01@openssh.com"
+ "ssh-mldsa44-ed25519@openssh.com"
- "OpenSSH_10.3p1"
```
