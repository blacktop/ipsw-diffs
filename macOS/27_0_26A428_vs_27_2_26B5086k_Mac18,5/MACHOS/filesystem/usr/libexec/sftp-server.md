## sftp-server

> `/usr/libexec/sftp-server`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-369.0.4.0.0
-  __TEXT.__text: 0x9f70
-  __TEXT.__auth_stubs: 0x680
+369.40.2.0.0
+  __TEXT.__text: 0xa1e8
+  __TEXT.__auth_stubs: 0x690
   __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x2196
+  __TEXT.__cstring: 0x2255
   __TEXT.__unwind_info: 0x280
   __DATA_CONST.__const: 0x698
-  __DATA_CONST.__auth_got: 0x340
+  __DATA_CONST.__auth_got: 0x348
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__auth_ptr: 0x10
   __DATA.__data: 0x18

   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
   Functions: 127
-  Symbols:   112
-  CStrings:  393
+  Symbols:   113
+  CStrings:  398
 
Symbols:
+ _OPENSSL_init_crypto
+ _bzero
- _ERR_load_crypto_strings
Functions:
~ sub_100003a5c : 836 -> 772
~ sub_100005eb4 -> sub_100005e74 : 1360 -> 1864
~ sub_1000075c4 -> sub_10000777c : 228 -> 392
~ sub_10000952c -> sub_100009788 : 820 -> 832
~ sub_100009860 -> sub_100009ac8 : 244 -> 252
~ sub_100009954 -> sub_100009bc4 : 408 -> 416
CStrings:
+ "bad read or write fd"
+ "cryptographic operation failed"
+ "fstat read_fd failed: %s"
+ "fstat write_fd failed: %s"
+ "refusing to read/write same file: read \"%s\" dev %lu ino %lu, write \"%s\" dev %lu ino %lu"
```
