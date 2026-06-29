## libcryptex_trampoline.dylib

> `/usr/lib/libcryptex_trampoline.dylib`

```diff

 662.160.12.0.0
-  __TEXT.__text: 0x6e4 sha256:c8adbdd2f101db9b3d5063d5136f572bdfb1b2ae0e126f3b47d15d4c16636e5b
-  __TEXT.__auth_stubs: 0x110 sha256:e0b17021e42435bcc5449295d293de580b423b5f4cda0301f7dc9be6700e0b1c
+  __TEXT.__text: 0x6e4 sha256:f2aff9219af97956fa540a73c84feb4b9a18424a79452fa5baac15717ecd19fa
+  __TEXT.__auth_stubs: 0x110 sha256:756991e3eb95dd7b5c8aedc2e0822ce67dfd3c0183747b24ebd67feb988ecbc0
   __TEXT.__const: 0x70 sha256:9db9b19bbfe24bdb4e5490f3e77bbe408a03e85745b8a23d3ea6d4b91c33d5c8
-  __TEXT.__cstring: 0x222 sha256:7dd10629c3071d4ebb3b046e71d9e915b431567f1c801ce8ddabd0ff02a4e5b3
+  __TEXT.__cstring: 0x222 sha256:2e14fee7c6ff257714b3e4311df59e2314b42aaeff592361e085778454e551b4
   __TEXT.__oslogstring: 0x104 sha256:54ae7e34b6b7a2b8e3e57a11ff8c643306866a2a34d7a2d127ee5a00b130d76c
   __TEXT.__unwind_info: 0x88 sha256:0025af637eddecce6c0d3ae2d55b2273e5fd302214929272eb552c035f121fa2
   __DATA_CONST.__got: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
-  __DATA_CONST.__const: 0x20 sha256:e5658d11890f4745e00c7f5e5948c5291aad200eb58c093670c1b172caf06c7f
+  __DATA_CONST.__const: 0x20 sha256:980bf44bc15565d91a967f4af686bb546f21ad3d51a2ee72013bb2ba80994a1a
   __AUTH_CONST.__auth_got: 0x88 sha256:b707241545a346265aab1ffb32ff64b55bf8f8dc1b56a46ef33ce3d15db11d33
-  __AUTH_CONST.__const: 0x20 sha256:1e015c7fe7c760d76170817b772ecc0b94949eb50f7bcfb766bd15c4ab824aef
-  __DATA.__data: 0x28 sha256:cbb80c40c0b2439e7920b13ee9d5e499194b02b942d25d6548fda79941957203
+  __AUTH_CONST.__const: 0x20 sha256:57b11223ad4a7007d4bbe489f6270f115a0cfb003e16b118af7fccc6babf89fb
+  __DATA.__data: 0x28 sha256:36624e28a7ee28b73de9b3ceedd311ba1a37d827495480932898da8999c17854
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcryptex_interface.dylib
-  UUID: E308B0B7-B2ED-30F9-8D0A-A2275E537C3B
+  UUID: F9A54B40-4A76-37AA-A211-9420481F9F14
   Functions: 12
   Symbols:   62
   CStrings:  15
Functions:
~ _cryptex_trampoline_upgrade_wait_options_create : sha256 6ea3e50f394cc2e7bcabba962d51d1e57279ba1ca385c670df34d6d4fbb5bca7 -> a5bb2911fd0a8392fb91043a2f9e7d67209a1824fc21f1aaeea3df818e0515a3
~ _cryptex_trampoline_upgrade_wait_options_set_cryptex_name : sha256 f3b53525f1520321a631ac8c0d833691cf3be5d9a4b897984f7e8aa41d8ad6e7 -> 0d55e76c12ed0800b889977ecae0c53a5cc4a1ca74fa04af006a51864b116642
~ _cryptex_trampoline_upgrade_wait : sha256 56371d44d12bcdb532ec85ba08f095bb16b9fb1c845eee3c6b93631b0e6376b6 -> de8719ed88b9f6c78ea406a5238192029e07daf72eaed31387f8146534f11f2f
~ ___cryptex_trampoline_osl_block_invoke : sha256 9d8042609723b53c8478e07465624a91b5754fd653a6c62970c97af27c82dc45 -> 6d0be2373b29d937e6f187466ee486b121d8704ff9a92c9debb79aa943a11050
~ _OUTLINED_FUNCTION_0 : sha256 a613e1e3f70526c9ba7d4bed4fdf0796a657f1afb7b0a2808677964ff89ff729 -> 14aacdb4ede6de224a9f3955c3214279a2b064dd234791a19e29c8dd63bfe266
~ _OUTLINED_FUNCTION_1 : sha256 819abafb3bc2df19c2e6f0cb3cfbe02884164739e4ec1b9c810b16c790db0d0d -> 47a13a69b69beb315a98f987dfffae5055b743ec851ba28742e3692d2fdf7590
~ _OUTLINED_FUNCTION_2 : sha256 1336bb14b0b61a77018e4b093368e758136324635c92a9516c746e9f518c4108 -> 364f77d11fc20435b06b77de119fd571608174fa5c952faa366f18221daf7554
~ _sysctl_upgrade_is_ongoing : sha256 c0a040e270a82fd3d67ae5e66ca9cf0b2dc70a09b8814e1abad78880d030f882 -> 4a8ce13ed2332fcac5e57f5d5f0b7b609b8e868b38ca6f2e14c2b7c41f80ef6a
~ _cryptex_trampoline_upgrade_wait_options_create.cold.1 : sha256 44b547d1d637221ef9bc72c559156d0b9077a419a74d8c2e8442ee24a8de3d3e -> c206a3ac65f77d2f7dcebe9785eaaa78073ac7f51827e000b8e73d60cb4ccf8a
~ _cryptex_trampoline_upgrade_wait_options_set_cryptex_name.cold.1 : sha256 66f2aef4ba9a6c2883230ff72985f278e3b64a75100a933d472b4637904c3c74 -> f7a3c9c88005d131c5026b48059e2246621d88e0378f94b576e606fbe377e7ff
CStrings:
+ "@(#)VERSION:Monitor Cryptex Upgrades Version 2.0.0: Wed Jun 17 03:36:37 PDT 2026; root:libcryptex-662.160.12~38/libcryptex_trampoline/RELEASE_ARM64E"
+ "Monitor Cryptex Upgrades Version 2.0.0: Wed Jun 17 03:36:37 PDT 2026; root:libcryptex-662.160.12~38/libcryptex_trampoline/RELEASE_ARM64E"
- "@(#)VERSION:Monitor Cryptex Upgrades Version 2.0.0: Sun Jun  7 19:34:14 PDT 2026; root:libcryptex-662.160.12~26/libcryptex_trampoline/RELEASE_ARM64E"
- "Monitor Cryptex Upgrades Version 2.0.0: Sun Jun  7 19:34:14 PDT 2026; root:libcryptex-662.160.12~26/libcryptex_trampoline/RELEASE_ARM64E"

```
