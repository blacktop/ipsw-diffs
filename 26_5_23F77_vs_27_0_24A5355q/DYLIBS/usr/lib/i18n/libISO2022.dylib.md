## libISO2022.dylib

> `/usr/lib/i18n/libISO2022.dylib`

```diff

-115.120.2.0.0
-  __TEXT.__text: 0x178c sha256:1145df2b5f894ce00763b26d850bbb18b91d0d97eec1c93fc0632dcb71f37b05
-  __TEXT.__auth_stubs: 0xb0 sha256:4daad4f05eb260c0ab94628ef971da7b2e6a4453b31b1a62ca83578cd419c626
+121.0.0.0.0
+  __TEXT.__text: 0x1888 sha256:b15b48f6f190868aea491d3c79aa49832398a653dbd4197f11f797fc56b13f13
   __TEXT.__const: 0x470 sha256:ac05acc16b59c48b04117a2862d3f00e887ebab584243e41b9f7152282573c20
-  __TEXT.__cstring: 0x80 sha256:dddf624fd369fa379b590afbd7c6b56fa8f0a8fe2ffccb35bce2667edbfcb6ca
-  __TEXT.__unwind_info: 0x88 sha256:56e593b989155c55da964d660599095c70332490bf1c6154a652cfb4369eafaf
-  __DATA_CONST.__got: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
-  __DATA_CONST.__const: 0x110 sha256:d80cdd83019f59262f9373940c39f2b70f47f35b64b7cf3c5f6ab3310596c59d
-  __AUTH_CONST.__auth_got: 0x58 sha256:10eef285deef7a4b7c82b22aa53589b7833df29de3814649c772bbd5c832f365
-  __AUTH.__data: 0x58 sha256:cbb4d02ef6af5995810c8e56c562d4f165ec083172ece39ad885619f3c4e2ee4
+  __TEXT.__cstring: 0xd4 sha256:d943e9022e886c9385e67c177e134d4f139a3ec08b41da16432272d316a5e93c
+  __TEXT.__unwind_info: 0x90 sha256:65634bb416f6d7e7b70bf197e084a32c299d55579fb4005b1ebf7a03a4a2c8b6
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x110 sha256:29fb926491614663d6e918b341860e8725e49d1170f60129b3aae50770cca15c
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__data: 0x58 sha256:9781f876c61d649a7bcc1310b3390f87bdae54fa39e7b13ac2bb9eb1e39f2f10
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libiconv.2.dylib
-  UUID: 7314AE92-79D1-3340-A1F8-458A3D855E4A
-  Functions: 15
-  Symbols:   44
-  CStrings:  28
+  UUID: 714FBE4C-A23F-3EA0-9892-473236EA12D6
+  Functions: 17
+  Symbols:   49
+  CStrings:  32
 
Symbols:
+ __ISO2022_sputwchar.cold.1
+ __ISO2022_sputwchar.cold.2
+ ___assert_rtn
Functions:
~ __citrus_ISO2022_stdenc_init : 1308 -> 1312
~ __citrus_ISO2022_stdenc_uninit : sha256 726216d87ac045525fe26fd81bb4280e035b0268a608dc11c3d2f54198fec8e9 -> edbc99a8edb7329ea8afefc013accb7e828766fc4d74544f78ba5f44a14844f6
~ __citrus_ISO2022_stdenc_mbtocs : sha256 8fe13ffc022d768326f2bc26e421fc056e4b4c776377036cd58f991449b6f434 -> f2c530a674fb70df8f16bdde74711fa41ec5ec0feeeaf8d60dfaae4986d61e38
~ __citrus_ISO2022_stdenc_cstomb : sha256 18c7a24d9c80dc6ad17954bd56ca60c2b9ffb59f1c5e458f90d312062e3dfa10 -> db9ed47b6ea22e591ed4ca788b98f7fc5622287227e128b296ff032d2ba8d0c5
~ __citrus_ISO2022_stdenc_mbtowc : sha256 6d34f07e7569fd1b96fe141aef7cd3ebd41e46d414c6c535f734248451534131 -> 7649ce1c910a2fb3f6d9c5c851771e382a760e20f378579f9c80a602cef62324
~ __citrus_ISO2022_stdenc_wctomb : sha256 b549a787f730efbe58a2744ea1bc3085e11cee137992877cb2dde48e82011e55 -> b8974d738923a4159d07404cd0c401cdfc7e814bc7f7d08d698e4fe1689a870d
~ __citrus_ISO2022_stdenc_put_state_reset : 152 -> 196
~ __citrus_ISO2022_stdenc_getops : sha256 2e245512f8d06bf40ad71cfb581860902f6c79c1961b9d0e2c840331df9b8eab -> 15911c901ad0f6a72aa278654a703b9033e0f92296ae72abee34243b65fd26d0
~ __citrus_ISO2022_mbrtowc_priv : 788 -> 792
~ __ISO2022_sgetwchar : 1224 -> 1228
~ _seqmatch : sha256 5f2e4a7279f394f38f428af7541fb78120cc5671b1d0004d56456fd57cdac439 -> 942f0a3d5d651508e839768d9d5112cf9213c7fdf6f3510b77131cad3f88705a
~ __citrus_ISO2022_wcrtomb_priv : 140 -> 184
~ __ISO2022_sputwchar : 1504 -> 1568
CStrings:
+ "(p - tmp) + i <= sizeof(tmp)"
+ "0 && \"Unreachable\""
+ "_ISO2022_sputwchar"
+ "citrus_iso2022.c"

```
