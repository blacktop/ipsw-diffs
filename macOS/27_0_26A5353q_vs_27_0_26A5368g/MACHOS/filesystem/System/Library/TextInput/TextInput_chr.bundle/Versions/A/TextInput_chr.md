## TextInput_chr

> `/System/Library/TextInput/TextInput_chr.bundle/Versions/A/TextInput_chr`

```diff

-3557.12.1.0.0
-  __TEXT.__text: 0xc50 sha256:f0e004e64ce2c8ab2d9ec0caad0770c972a19172bc5a65db2a2ff89ee5494d42
-  __TEXT.__init_offsets: 0x4 sha256:557c48d00197ba1622347478c2326cdb80fc369678880a3b09e38ef687962de3
-  __TEXT.__objc_methlist: 0x68 sha256:0454a8198e47fd02aba756a91b9c630bf381f91482ecc31edf40c874f2660417
+3557.15.0.0.0
+  __TEXT.__text: 0xc44 sha256:fde01e7079564c668139fb29f561f651279afe91f55b4a0b2015c02d9fe03ae5
+  __TEXT.__init_offsets: 0x4 sha256:9015f39c242389b1c38754e9878289a1b44d2f9f16da2cbbfc7dae4dbb01002b
+  __TEXT.__objc_methlist: 0x68 sha256:d5c29210d28dbb26eeb5f30d96b96952c9f135792596a7dd1bf70657a7b83155
   __TEXT.__const: 0xa8 sha256:cb1d839b8aebe0737d3b70d93a871d56633e5ae9b998f0cb0ef18aaca615b048
   __TEXT.__ustring: 0x18 sha256:fbbfc95aae940992553507f713a611fc0ec20dce480f439c8bf192e4d0ee97ff
   __TEXT.__cstring: 0xb sha256:b18c71802e37e67a227ae848cfabbdb84e3ed0d9a603771733819c6f494b42dc

   __TEXT.__objc_methtype: 0x24 sha256:061c7e44e91023eb8374fd9410a5b2454a45768e48a537bf0ba9b8d46cd1bfcc
   __DATA_CONST.__objc_classlist: 0x8 sha256:400c52dd5bd0047d64c0582af027b387a7938a64283d0d4f727331140cb6462c
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
-  __DATA_CONST.__objc_selrefs: 0xd0 sha256:065c1a3cdcec4cd2f93de5f1859fc8857a5e38bb2bce0a4501dc3d59d8090f44
+  __DATA_CONST.__objc_selrefs: 0xd0 sha256:fad76753b1684a47191e02933160e428acb3dc13bee3021295a501566579247f
   __DATA_CONST.__objc_arraydata: 0x30 sha256:e9a61a4f85c99d08df3f963987fd929b24788224213e843dc52b1fbecb3fc300
   __DATA_CONST.__got: 0x28 sha256:e4d52ddc0b9dbcbb8e0275986609b49d9357a72fc5f228a7fac72ba8631f90d9
-  __AUTH_CONST.__cfstring: 0xe0 sha256:974852ee5ef2eefebe65175fe212f1695a6f5509fdb4425f8a64cf9e42180af5
-  __AUTH_CONST.__objc_const: 0x90 sha256:0cf75fbcc5ff603f380fc28fc7b2a002bb19791bd6dde3f692ff8455287084c3
+  __AUTH_CONST.__cfstring: 0xe0 sha256:da4cb4fa3ebc6a87b67c5ddc1b359f2ef19198bb8e3614d5d5ebaafbbf9c9b34
+  __AUTH_CONST.__objc_const: 0x90 sha256:a124095f35e163e3fdc19f163ee7bc769df78b7a1aab390b0673e56751c31229
   __AUTH_CONST.__weak_auth_got: 0x10 sha256:ae7b42daa3eeb9d3a45387f6bf419e652b0c622ceb6554e7496e44c758f5cb37
   __AUTH_CONST.__objc_arrayobj: 0x18 sha256:97cc2191b664e994c3ea7984b060ff01e1a869a5e6ca9cb18eb2d11fc00f309f
   __AUTH_CONST.__auth_got: 0x68 sha256:0bbecb4c94b80f3fe1faf2e036e288fd3e0337464c8163685ea403e108857e3b

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4E673710-8A85-379E-BFB0-9A721FB1F66A
+  UUID: 172A9EDB-522B-398C-BB1D-28A82645ED1F
   Functions: 10
   Symbols:   64
   CStrings:  39
Functions:
~ __ZN2KB14LikelihoodInfoD1Ev : sha256 145dfafc29510491b874c8f767b96f258c68c36874964b0cd2b68ac6931798f5 -> cbd287eb9f129d0f5a7905131d3c26116fd91dbdb93a1c105342c13bf8dfd540
~ -[TIKeyboardInputManager_chr initImplementation] : sha256 4b98bd3a6b62d6bda6546fa9f5ff28860c56e188a996beac5d25897abc0ac068 -> c2819ae9afcc3348f8d13c081b1b1e44d1778d8546f180b3bb5638a7821653f9
~ -[TIKeyboardInputManager_chr doesComposeText] : sha256 852192ed78caf35b706405f22198a6953fb59a37db7816e6620c7d0bd2eb5c65 -> cb3ca0263666149357fdc5ffd7b0dadaf59ba2689ee6eaada649c06df36405d0
~ +[TIKeyboardInputManager_chr stringByComposingInput:] : 776 -> 772
~ -[TIKeyboardInputManager_chr internalStringToExternal:] : sha256 cf0604bb8a6b13129c1a1833ce9eb56fd133466d2225c719ac27c2315704d492 -> d7a782f87266af65361e153fe1cf7c7552648cb755bbe267d216589be30eca63
~ -[TIKeyboardInputManager_chr externalStringToInternal:] : 972 -> 968
~ sub_151c -> sub_1514 : sha256 e273a201ed3ff9218bad0b0a8ae558316f576e8fdfaa729eceaf69749ff025a3 -> 7bcb5d97eae5200c999e750a9b01a14aee2f16df00e1ffe717e0e81e68081912
~ -[TIKeyboardInputManager_chr contextualDisplayKeys] : 612 -> 608
~ _GLOBAL__sub_I_TIKeyboardInputManager_chr.mm : sha256 6deb3a8e5554a880623b4ddbbb36eafb9734c5a31956b54413f9d0ca693c7cf3 -> 111856809ce964a7df7530cde2165c62dfe05cf7de7ce35e910bf8783a1b014d

```
