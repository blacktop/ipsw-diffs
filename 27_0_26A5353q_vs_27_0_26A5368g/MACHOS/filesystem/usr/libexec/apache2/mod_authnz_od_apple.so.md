## mod_authnz_od_apple.so

> `/usr/libexec/apache2/mod_authnz_od_apple.so`

```diff

 39.0.0.0.0
-  __TEXT.__text: 0xf1c sha256:b7f8b94edf3b517d0a41eb676d20819aeec32f752f50b30eef98e692a513000e
+  __TEXT.__text: 0xec0 sha256:0979a93a3bbe68a6c9906a257e80b51c8b37c9cd1f80734fb0bef364e643865a
   __TEXT.__auth_stubs: 0x210 sha256:dd89cdfe6948f6b9251cd133aeea54bed6f31dd83fe3dd96a51a2a79999342af
   __TEXT.__cstring: 0x3f1 sha256:3faabcb8b7b0d2852135d7112d7cb60f95776db249da93982d364f79088d7640
-  __TEXT.__unwind_info: 0x78 sha256:3dded679d1302d85b475a6523f7be87b063f07df65bc2fecfe645b5aa5309fd4
-  __DATA_CONST.__const: 0x20 sha256:52a83823ff39d825adb4482ec01ebed27fe1d975ed3e8aae61c0069971b6e6c0
+  __TEXT.__unwind_info: 0x78 sha256:da006e8cfaae23f60bcfcf57877a12d1eabf9d873bdfa94b34d7f356598bcb72
+  __DATA_CONST.__const: 0x20 sha256:fe200577525e5c4220b16634d0e3be7617ee8b0c4a689c766123900ca08a07e0
   __DATA_CONST.__auth_got: 0x108 sha256:3d74e5ed7bc7e19f30bfe8a15087dacb4c1f2f6525be00cf1fe1d1f527bc42d4
   __DATA_CONST.__got: 0x18 sha256:a3ee3cc1442b33b1ce2ebec1cb367ab1e7713d5cd83713566dbcf66bd0891fdf
-  __DATA.__data: 0x88 sha256:89421e8c89f9b5bc0715f3c20724706b1f26e7ba1d41096b251e27aafd25049f
+  __DATA.__data: 0x88 sha256:a51f30fd8017e4248cab04a44a7c13a8fc7b74b0da767a03451886a53d6c29c5
   __DATA.__bss: 0x30 sha256:17b0761f87b081d5cf10757ccc89f12be355c70e2e29df288b65b30710dcbcd1
   - /usr/lib/libSystem.B.dylib
-  UUID: D42DAF22-E0E4-368B-BC78-DEF78C65B638
+  UUID: FDAC525A-166B-35B2-8A94-FF43C00B3AB4
   Functions: 9
   Symbols:   55
   CStrings:  29
Functions:
~ _register_hooks : sha256 d294d780a646a60d90c2fcaa1db25647bf946842215a3dd736c1c5f6901fd457 -> adf42922d952665e90708ee72c845bac6e8308d4ce9e31324f6f5589b91baf20
~ _authn_cache_precfg : sha256 d5857f94faa89ecebb3d04702341806b3044d1d5909b0bf61a1630bc2fd5e60f -> 86bb77582aa6ce203cf0437fb2e00adacbe388c9c5a8988121c612cb625a64b9
~ _authn_cache_post_config : 656 -> 636
~ _authn_cache_child_init : sha256 d4d2ac0e356635e603b89d8259c8f93712d27c5614e7bfd32950f33f3b34fc93 -> d63ce619e4bab53cc7e65fa1a7cc09953dfb8ab888d0ca9de198337f20748061
~ _check_password : 1412 -> 1376
~ _group_check_authorization : 916 -> 880

```
