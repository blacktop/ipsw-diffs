## ssh-pkcs11-helper

> `/usr/libexec/ssh-pkcs11-helper`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__got`

```diff

-369.0.4.0.0
-  __TEXT.__text: 0x10a44
-  __TEXT.__auth_stubs: 0xaf0
-  __TEXT.__const: 0x1af0c
-  __TEXT.__cstring: 0x2421
-  __TEXT.__unwind_info: 0x430
-  __DATA_CONST.__const: 0x7c8
-  __DATA_CONST.__auth_got: 0x578
+369.40.2.0.0
+  __TEXT.__text: 0x264d4
+  __TEXT.__auth_stubs: 0xae0
+  __TEXT.__const: 0x1b034
+  __TEXT.__cstring: 0x24ee
+  __TEXT.__unwind_info: 0x4c8
+  __TEXT.__eh_frame: 0x50
+  __DATA_CONST.__const: 0x8a8
+  __DATA_CONST.__auth_got: 0x570
   __DATA_CONST.__got: 0x28
-  __DATA_CONST.__auth_ptr: 0x18
+  __DATA_CONST.__auth_ptr: 0x20
   __DATA.__data: 0x10
   __DATA.__common: 0x38
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libpam.2.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 229
-  Symbols:   184
-  CStrings:  350
+  Functions: 263
+  Symbols:   183
+  CStrings:  357
 
Symbols:
- _ERR_load_crypto_strings
CStrings:
+ "COMPSIG-MLDSA44-Ed25519-SHA512"
+ "CompositeAlgorithmSignatures2025"
+ "MLDSA44-ED25519"
+ "MLDSA44-ED25519-CERT"
+ "cryptographic operation failed"
+ "ssh-mldsa44-ed25519-cert-v01@openssh.com"
+ "ssh-mldsa44-ed25519@openssh.com"
```
