## ssh-sk-helper

> `/usr/libexec/ssh-sk-helper`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__got`

```diff

-369.0.4.0.0
-  __TEXT.__text: 0xf520
-  __TEXT.__auth_stubs: 0x920
-  __TEXT.__const: 0x1aeb0
-  __TEXT.__cstring: 0x1c06
-  __TEXT.__unwind_info: 0x430
-  __DATA_CONST.__const: 0xa48
-  __DATA_CONST.__auth_got: 0x490
+369.40.2.0.0
+  __TEXT.__text: 0x25094
+  __TEXT.__auth_stubs: 0x930
+  __TEXT.__const: 0x1afac
+  __TEXT.__cstring: 0x1d3d
+  __TEXT.__unwind_info: 0x4d0
+  __TEXT.__eh_frame: 0x50
+  __DATA_CONST.__const: 0xb28
+  __DATA_CONST.__auth_got: 0x498
   __DATA_CONST.__got: 0x30
-  __DATA_CONST.__auth_ptr: 0x10
+  __DATA_CONST.__auth_ptr: 0x18
   __DATA.__data: 0x10
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Kerberos.framework/Versions/A/Kerberos

   - /usr/lib/libpam.2.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 233
-  Symbols:   164
-  CStrings:  277
+  Functions: 268
+  Symbols:   165
+  CStrings:  288
 
Symbols:
+ _OPENSSL_init_crypto
+ _memcmp
- _ERR_load_crypto_strings
CStrings:
+ "COMPSIG-MLDSA44-Ed25519-SHA512"
+ "CompositeAlgorithmSignatures2025"
+ "MLDSA44-ED25519"
+ "MLDSA44-ED25519-CERT"
+ "cryptographic operation failed"
+ "ssh-mldsa44-ed25519-cert-v01@openssh.com"
+ "ssh-mldsa44-ed25519@openssh.com"
+ "xcalloc"
+ "xcalloc: nmemb * size > SIZE_MAX"
+ "xcalloc: out of memory (allocating %zu bytes)"
+ "xcalloc: zero size"
```
