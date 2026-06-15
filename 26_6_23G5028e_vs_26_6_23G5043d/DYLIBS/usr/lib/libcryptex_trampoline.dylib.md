## libcryptex_trampoline.dylib

> `/usr/lib/libcryptex_trampoline.dylib`

```diff

-662.160.6.0.0
-  __TEXT.__text: 0x6e4 sha256:b173ca2d8c8f3482f4a4969ab7131514a9039fbc99900ec58f93fb2fc03d0ef9
-  __TEXT.__auth_stubs: 0x110 sha256:02a804557cc210046812eae799bfecbca59a7938fb83ccda22359cd73d950656
-  __TEXT.__const: 0x70 sha256:0d821b5058c6c7c6c80c6ea50165de83379534eeb82b79898824f45e44f1d781
-  __TEXT.__cstring: 0x21d sha256:75c138d9445b260606dc3cd5fd3a67cda3fc49833b96fe06cce6cbddb4a4bb1d
+662.160.12.0.0
+  __TEXT.__text: 0x6e4 sha256:c8adbdd2f101db9b3d5063d5136f572bdfb1b2ae0e126f3b47d15d4c16636e5b
+  __TEXT.__auth_stubs: 0x110 sha256:e0b17021e42435bcc5449295d293de580b423b5f4cda0301f7dc9be6700e0b1c
+  __TEXT.__const: 0x70 sha256:9db9b19bbfe24bdb4e5490f3e77bbe408a03e85745b8a23d3ea6d4b91c33d5c8
+  __TEXT.__cstring: 0x222 sha256:7dd10629c3071d4ebb3b046e71d9e915b431567f1c801ce8ddabd0ff02a4e5b3
   __TEXT.__oslogstring: 0x104 sha256:54ae7e34b6b7a2b8e3e57a11ff8c643306866a2a34d7a2d127ee5a00b130d76c
   __TEXT.__unwind_info: 0x88 sha256:0025af637eddecce6c0d3ae2d55b2273e5fd302214929272eb552c035f121fa2
   __DATA_CONST.__got: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
-  __DATA_CONST.__const: 0x20 sha256:a21b3a5164813b337c42f101f7e2661a047030acc12232a14ab3cebb414ed394
+  __DATA_CONST.__const: 0x20 sha256:e5658d11890f4745e00c7f5e5948c5291aad200eb58c093670c1b172caf06c7f
   __AUTH_CONST.__auth_got: 0x88 sha256:b707241545a346265aab1ffb32ff64b55bf8f8dc1b56a46ef33ce3d15db11d33
-  __AUTH_CONST.__const: 0x20 sha256:c92e6e3e7ea10926c8959940423acb3284051ff8ab05d91ec6f2db7c541573f9
-  __DATA.__data: 0x28 sha256:2357c2026a9e7c5411a09edefb42125849fdf2f106738db9e9a417c6b654e514
+  __AUTH_CONST.__const: 0x20 sha256:1e015c7fe7c760d76170817b772ecc0b94949eb50f7bcfb766bd15c4ab824aef
+  __DATA.__data: 0x28 sha256:cbb80c40c0b2439e7920b13ee9d5e499194b02b942d25d6548fda79941957203
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcryptex_interface.dylib
-  UUID: 13AD10D3-FD73-3585-BA3C-CED2BA82F209
+  UUID: E308B0B7-B2ED-30F9-8D0A-A2275E537C3B
   Functions: 12
   Symbols:   62
   CStrings:  15
Functions:
~ _cryptex_trampoline_upgrade_wait_options_create : sha256 6d7f39d79b001118af10d51659249bc5bcf669fe0449d6f7405203612aa5a248 -> 6ea3e50f394cc2e7bcabba962d51d1e57279ba1ca385c670df34d6d4fbb5bca7
~ _cryptex_trampoline_upgrade_wait_options_set_cryptex_name : sha256 cefab6e973756924f28c6dd30ab7a4ebfd80fa790da1037aa96413eea9efb5fc -> f3b53525f1520321a631ac8c0d833691cf3be5d9a4b897984f7e8aa41d8ad6e7
~ _cryptex_trampoline_upgrade_wait : sha256 724f003835908d8c382fe8d76a70996aee2c7885a719ab5aa339c0952883cf6b -> 56371d44d12bcdb532ec85ba08f095bb16b9fb1c845eee3c6b93631b0e6376b6
~ ___cryptex_trampoline_osl_block_invoke : sha256 a805f5c632f15f316884f98a77be16f5875a2d33bd08fbe9a2d9db6e6e3d4034 -> 9d8042609723b53c8478e07465624a91b5754fd653a6c62970c97af27c82dc45
~ _OUTLINED_FUNCTION_0 : sha256 2b4f679f13da09f97f77b44bfda26d912656f298fd40265f3ffcb67f3c235588 -> a613e1e3f70526c9ba7d4bed4fdf0796a657f1afb7b0a2808677964ff89ff729
~ _OUTLINED_FUNCTION_1 : sha256 f67177707a4ee826a0f03ed0f1e4fc08252abd4b7c8551f14534d010cb6004c2 -> 819abafb3bc2df19c2e6f0cb3cfbe02884164739e4ec1b9c810b16c790db0d0d
~ _OUTLINED_FUNCTION_2 : sha256 2353abdefa9d30e4c13b5f124c7eb62d25fb50b7c303356fbb1218dae2e686ae -> 1336bb14b0b61a77018e4b093368e758136324635c92a9516c746e9f518c4108
~ _sysctl_upgrade_is_ongoing : sha256 94c1783834b0fed6b9e2e4918dd6260701e10d9cce0363f623a07bcb73771b49 -> c0a040e270a82fd3d67ae5e66ca9cf0b2dc70a09b8814e1abad78880d030f882
~ _cryptex_trampoline_upgrade_wait_options_create.cold.1 : sha256 8b8d271166a12f732bac9b3f9fe62483ddcd4b23cb120610807207fe6418b81a -> 44b547d1d637221ef9bc72c559156d0b9077a419a74d8c2e8442ee24a8de3d3e
~ _cryptex_trampoline_upgrade_wait_options_set_cryptex_name.cold.1 : sha256 646dfa042a55e30847da90269c22479b27dbe5924d841530b1644c933d3d2924 -> 66f2aef4ba9a6c2883230ff72985f278e3b64a75100a933d472b4637904c3c74
CStrings:
+ "662.160.12"
+ "@(#)VERSION:Monitor Cryptex Upgrades Version 2.0.0: Sun Jun  7 19:34:14 PDT 2026; root:libcryptex-662.160.12~26/libcryptex_trampoline/RELEASE_ARM64E"
+ "Monitor Cryptex Upgrades Version 2.0.0: Sun Jun  7 19:34:14 PDT 2026; root:libcryptex-662.160.12~26/libcryptex_trampoline/RELEASE_ARM64E"
- "662.160.6"
- "@(#)VERSION:Monitor Cryptex Upgrades Version 2.0.0: Thu May 14 23:37:09 PDT 2026; root:libcryptex-662.160.6~9/libcryptex_trampoline/RELEASE_ARM64E"
- "Monitor Cryptex Upgrades Version 2.0.0: Thu May 14 23:37:09 PDT 2026; root:libcryptex-662.160.6~9/libcryptex_trampoline/RELEASE_ARM64E"

```
