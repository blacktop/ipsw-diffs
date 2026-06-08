## libUTF8MAC.dylib

> `/usr/lib/i18n/libUTF8MAC.dylib`

```diff

-115.120.2.0.0
-  __TEXT.__text: 0xde4 sha256:2122b13025f2cfa9803737d78e17da8d086be7607b387eb8a49794636969d2dc
-  __TEXT.__auth_stubs: 0x50 sha256:a07a12496bbbfca4080f64bbd970dd0bf8890a9b310e79ef02741fbac666f6e1
+121.0.0.0.0
+  __TEXT.__text: 0xdfc sha256:534a4d1e68680d1bd44418da0a00b329b78dc34480ded86df13d5c56509a7f36
   __TEXT.__const: 0x34d4 sha256:5f2250dfb493a27d9f05f6f75463df55edfeca95df77f1e42f7cadd79ce4c081
   __TEXT.__cstring: 0x76 sha256:b391014ce2a051247cc39bbcec7e0ad06984f4f4d5f251ef3b08c37ea9529ed7
-  __TEXT.__unwind_info: 0x90 sha256:6a0eaa118d6b6d8ee794b8ec091ae9be89d4b34abb1d55c4430fb057e00a430a
-  __DATA_CONST.__got: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
-  __AUTH_CONST.__auth_got: 0x28 sha256:2c34ce1df23b838c5abf2a7f6437cca3d3067ed509ff25f11df6b11b582b51eb
-  __AUTH.__data: 0x58 sha256:d97a80a0e2f44af34d0aa76dbaecadf06f1c5bc0520d0487d34a522bdcb065e6
+  __TEXT.__unwind_info: 0x90 sha256:5b2304b3b6ccf8e889f06d65772dbf9fd4cf8706d357a003ae035ebca107bd56
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__data: 0x58 sha256:8ff658efc02c059bc6a39b4d946b74ccde1f59f0d9606af2388a5272f5b071ac
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libiconv.2.dylib
-  UUID: C79EDACC-EE50-30F6-A3C3-197966AB5EA9
+  UUID: 104EB50A-02A1-3BFA-9880-223176F86F59
   Functions: 17
   Symbols:   47
   CStrings:  6
Functions:
~ __citrus_UTF8MAC_stdenc_init : sha256 3985ce26776bfe29fbb980baec18181ab8eb4c01b4acd39be357f74b85a9da3d -> daeeae0c889f7fa1c919c7bc0b77970781d7863f07f22b5bd32ecfb582e8c396
~ __citrus_UTF8MAC_stdenc_uninit : sha256 dce44475d77f7d779c70a36cfbd439895838e7d3f9fc6d6385ce114c8eed86f4 -> b4013facded009deea39d3bf6a85185e4a0f41816d0799a3ff6a1e8ad14f19da
~ __citrus_UTF8MAC_stdenc_mbtocs : sha256 66c753b9c4414bf5c645786e49e92aa226982aa9fd44362eda366bfb9db602df -> df30f4256d96dbe1a660b2c8ed7cb218046256fc5fc62ea887101fa70e442892
~ __citrus_UTF8MAC_stdenc_cstomb : sha256 e5d368eb9e074da8ea68837b74f181e0e49d893376a1330d296169b6abcd5e39 -> 7ba8f64ef1e47951f64e55f8ba33970c3e654b599d34df52bbe7acc1130e0993
~ __citrus_UTF8MAC_stdenc_mbtowc : sha256 7a53e562bcdf5c73c72d9e32952acf5f7225e51354971a58b7b1566a1e8c8f71 -> 9a3eb11d82cd33fddc09967453199f181868256776394b2235c1489d2f5f826b
~ __citrus_UTF8MAC_stdenc_wctomb : sha256 9b413300121be48e2bded783a56f140764f679d9905261e5b1379b8a0fbfc432 -> f8a9e7960c656864089f701f8d69991460d771992435e39c8ee91bf2a857b2a7
~ __citrus_UTF8MAC_stdenc_mbtocsn : 356 -> 368
~ __citrus_UTF8MAC_stdenc_cstombn : 260 -> 268
~ __citrus_UTF8MAC_stdenc_getops : sha256 0d1d7261339c12d2fda6cb0554b38a2b89ec63d71b5be0404464bca9e96fd9dd -> 5af3b85952eb2728bee644a7e46a66f435325ca575977bebd41bc1a8c7be9763
~ __citrus_UTF8MAC_mbrtowc_priv : 1204 -> 1208
~ __citrus_UTF8MAC_wcrtomb_priv : sha256 3902fd9e22a9009ffe38e19303397559a7f3b937f44685ad2b5165d93c1536a5 -> 3cebfa6d3a25958f3c8de71d7c278d5a3257470b0df3c94dbf154caf4e8f0c90
~ _unicode_recursive_decompose : sha256 c25fe2f064e92c6745b69ecad7a32d2d2de94be85729f1d195670c7eba3b4cca -> 2e89cf9cde22ba256caae96cff62bf8bd353adbab3f3299e81a9f4fe0f134211
~ __citrus_UTF8MAC_stdenc_mbtocsn.cold.1 : sha256 086d8a675755518a8c4f9bccf9c18b1fc31230744e8765937dd296b97dd1983e -> b0d849a99725302b2b18b59dcd1b1a38d229494abf3b5783a872c4e0ad84a61f
~ __citrus_UTF8MAC_stdenc_mbtocsn.cold.2 : sha256 340c7efa657eaeac2807c7baf9383b8edec4b272fc932c0d3a69e6abf26ce10c -> f7d2adf2a1afd5b5fbe98c5a9e474d631fe10986b11ca47771f9c984812bb379
~ __citrus_UTF8MAC_stdenc_cstombn.cold.1 : sha256 0755a43a3ebb0babe132da3fca250537b8f694633b1690c38563d0c05988f1db -> 6154e3ed712bf9bbcbaa724702ab294646c62dc34ead8705200c1cf381605c80

```
