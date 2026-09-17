## sftp

> `/usr/bin/sftp`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-369.0.4.0.0
-  __TEXT.__text: 0x13104
+369.40.2.0.0
+  __TEXT.__text: 0x1327c
   __TEXT.__auth_stubs: 0x7c0
   __TEXT.__const: 0x110
-  __TEXT.__cstring: 0x3fcb
+  __TEXT.__cstring: 0x4019
   __TEXT.__unwind_info: 0x398
   __DATA_CONST.__const: 0x3f8
   __DATA_CONST.__auth_got: 0x3e0

   - /usr/lib/libpam.2.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 198
+  Functions: 199
   Symbols:   153
-  CStrings:  607
+  CStrings:  608
 
Symbols:
+ _OPENSSL_init_crypto
- _ERR_load_crypto_strings
CStrings:
+ "cryptographic operation failed"
+ "fcntl(%d, F_SETFD, FD_CLOEXEC): %s"
+ "server sent zero data length"
- " -a"
- "get%s %s%s%s"
```
