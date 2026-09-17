## ssh-agent

> `/usr/bin/ssh-agent`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__auth_got`

```diff

-369.0.4.0.0
-  __TEXT.__text: 0x18f40
+369.40.2.0.0
+  __TEXT.__text: 0x2eb34
   __TEXT.__auth_stubs: 0xc60
-  __TEXT.__const: 0x1bf98
-  __TEXT.__cstring: 0x3cb6
-  __TEXT.__unwind_info: 0x560
-  __DATA_CONST.__const: 0x9a8
+  __TEXT.__const: 0x1c0a8
+  __TEXT.__cstring: 0x3e07
+  __TEXT.__unwind_info: 0x608
+  __TEXT.__eh_frame: 0x50
+  __DATA_CONST.__const: 0xa88
   __DATA_CONST.__auth_got: 0x630
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__auth_ptr: 0x20
+  __DATA_CONST.__auth_ptr: 0x28
   __DATA.__data: 0x18
   __DATA.__common: 0x60
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libpam.2.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 318
+  Functions: 353
   Symbols:   218
-  CStrings:  587
+  CStrings:  600
 
Symbols:
+ _OpenSSL_version
- _ERR_load_crypto_strings
CStrings:
+ "%s, %s\n"
+ "%s: unveil %s %s"
+ "COMPSIG-MLDSA44-Ed25519-SHA512"
+ "CompositeAlgorithmSignatures2025"
+ "MLDSA44-ED25519"
+ "MLDSA44-ED25519-CERT"
+ "OpenSSH_10.5"
+ "attempt to use extension \"%s\" while locked"
+ "c"
+ "cDdksTuUVE:a:O:P:t:l"
+ "cryptographic operation failed"
+ "ssh-mldsa44-ed25519-cert-v01@openssh.com"
+ "ssh-mldsa44-ed25519@openssh.com"
+ "usage: ssh-agent [-c | -s] [-DdTU] [-a bind_address] [-E fingerprint_hash]\n                 [-O option] [-P allowed_providers] [-t life]\n       ssh-agent [-TU] [-a bind_address] [-E fingerprint_hash] [-O option]\n                 [-P allowed_providers] [-t life] command [arg ...]\n       ssh-agent [-c | -s] -k\n       ssh-agent -u\n       ssh-agent -V\n"
+ "user match pattern too long"
- "cDdksTuUE:a:O:P:t:l"
- "usage: ssh-agent [-c | -s] [-DdTU] [-a bind_address] [-E fingerprint_hash]\n                 [-O option] [-P allowed_providers] [-t life]\n       ssh-agent [-TU] [-a bind_address] [-E fingerprint_hash] [-O option]\n                 [-P allowed_providers] [-t life] command [arg ...]\n       ssh-agent [-c | -s] -k\n       ssh-agent -u\n"
```
