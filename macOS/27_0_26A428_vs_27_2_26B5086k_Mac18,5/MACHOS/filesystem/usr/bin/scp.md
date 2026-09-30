## scp

> `/usr/bin/scp`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

-369.0.4.0.0
-  __TEXT.__text: 0x12204
+369.40.2.0.0
+  __TEXT.__text: 0x1237c
   __TEXT.__auth_stubs: 0x6c0
   __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0x31d8
+  __TEXT.__cstring: 0x3214
   __TEXT.__unwind_info: 0x380
   __DATA_CONST.__const: 0x68
   __DATA_CONST.__auth_got: 0x360

   - /usr/lib/libz.1.dylib
   Functions: 189
   Symbols:   133
-  CStrings:  539
+  CStrings:  541
 
Symbols:
+ _OPENSSL_init_crypto
- _ERR_load_crypto_strings
Functions:
~ sub_100004784 : 1012 -> 1056
~ sub_1000087a4 -> sub_1000087d0 : 3344 -> 3404
~ sub_10000aed8 -> sub_10000af40 : 2712 -> 2768
~ sub_10000d378 -> sub_10000d418 : 228 -> 392
~ sub_10000f968 -> sub_10000faac : 820 -> 832
~ sub_10000fc9c -> sub_10000fdec : 244 -> 252
~ sub_10000fd90 -> sub_10000fee8 : 408 -> 416
~ sub_100010c40 -> sub_100010da0 : 732 -> 756
CStrings:
+ "cryptographic operation failed"
+ "server sent zero data length"
```
