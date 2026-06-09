## libcryptex_trampoline.dylib

> `/usr/lib/libcryptex_trampoline.dylib`

```diff

-662.120.27.0.0
-  __TEXT.__text: 0x6e4 sha256:c668c149b80f8182346e8e0c60d9b274c32662938ed7a16e9603a07a6e3a1439
-  __TEXT.__auth_stubs: 0x110 sha256:ebd47b47f45acbec32eeb1f26448ed1d9aff72fe35b3a433c8110d2f55b36cd0
-  __TEXT.__const: 0x70 sha256:ca825ef6dbc75f7e380613b678a9c7ef0ea640b73f2563bf98b69b387fb5155a
-  __TEXT.__cstring: 0x222 sha256:1766f7c4379a87b5c24ee4b2a4714a3eb4bc0b1c10f8bdc9b249d77fad12427d
+746.0.0.0.0
+  __TEXT.__text: 0x6e4 sha256:55f6f5c05184253e8ee0d113fa19266f183a9618270eaa8f19e9ebf1c77542df
+  __TEXT.__const: 0x68 sha256:89ed8c673e8416a6fa44d10b7773a5d4df2995fdb45542822cf9ced0e71c93b3
+  __TEXT.__cstring: 0x20f sha256:8f6ec5a1ce0b3ce0cfd711214e9d385ce4103ee036c2f52b987e65b10c91bb5f
   __TEXT.__oslogstring: 0x104 sha256:54ae7e34b6b7a2b8e3e57a11ff8c643306866a2a34d7a2d127ee5a00b130d76c
-  __TEXT.__unwind_info: 0x88 sha256:0025af637eddecce6c0d3ae2d55b2273e5fd302214929272eb552c035f121fa2
-  __DATA_CONST.__got: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
-  __DATA_CONST.__const: 0x20 sha256:6543660f4d0d245c009acb2fbdcfb56cabcd674c2542fa6cfb5bc6cb205004da
-  __AUTH_CONST.__auth_got: 0x88 sha256:b707241545a346265aab1ffb32ff64b55bf8f8dc1b56a46ef33ce3d15db11d33
-  __AUTH_CONST.__const: 0x20 sha256:87df14bb628fa4ea8fcf2eb2a23a4e1b290af76b941e5b0ea386fcfb63fbd583
-  __DATA.__data: 0x28 sha256:e3de32e70af64c66152d6f01e5f18acad26182bb0241b643f3633459f5dd0ee5
+  __TEXT.__unwind_info: 0x88 sha256:cd9eca24d1605ea99e5f770590146826d3a526de4639a6ef1e3890a2d9d1e5c0
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x20 sha256:18f1a6d9ece0fd8302d549b9acd271a23f48310177dff2ffb260ed34c3c2b2ba
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x20 sha256:c09603e913ac3e6582513b0e050a79369cd2ed0991be0892e7c11348dc2f1f42
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__data: 0x28 sha256:805b1e764e6436eb1575b9c71a6dbb6d7b8bd236459fd4cd3cc58124b9fd4b75
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcryptex_interface.dylib
-  UUID: 2BAAC5A0-7E5D-39D0-88AE-2F729F470F8D
+  UUID: 869F3D59-8AFC-31FD-8C03-2650B8168E42
   Functions: 12
   Symbols:   62
   CStrings:  15
Functions:
~ _cryptex_trampoline_upgrade_wait_options_create : sha256 bc6ecddc21c7e646684302aad124b3797e4b06f19c92f01b68a397ccd26013bb -> 49230bfac7bf5f3536e4229fdb7359e73161b6f3429ac345eb2007d141d223a3
~ _cryptex_trampoline_upgrade_wait_options_destroy : sha256 33e781223b65b50a6ad93f63d5ed4b7c698ba0c53ac9262b58b4e937df4f868c -> a954060f8b110c9a93f385cbd4fa1b0f409dc8c241a67a32c77639d5e9933e49
~ _cryptex_trampoline_upgrade_wait_options_set_cryptex_name : sha256 d6f07afd76ddcf1e925c4f4c152e9676b75122047e891fa61976fa598569933e -> fcec088bf5b5a411e7abf344d9de9c73d77d2ab684800b392fd9e71f36e468d9
~ _cryptex_trampoline_upgrade_wait : sha256 e392349f8061734973657fcaaa9e46f91c42679e7c6cef6cfcc621d5f44f4369 -> 6392c264eb379654254dd5bb45f48b0b63dfc7659394fb8dae0c92c5737047f3
~ ___cryptex_trampoline_osl_block_invoke : sha256 8fa19b5f8c68b79e038c5531da5de3c68e205dc965ee9a1c551478769cd91ce1 -> 4904180ddefdd58ae310fe3e04cbc1683b6b6b42b7078691dc45ce9621a7103b
~ _OUTLINED_FUNCTION_0 : sha256 d8738fa24eaa8bfd9296fe93ff0bb36efe27a4c8d9caae6e903b315f35b0b087 -> 47212ec734ce7a26e78fc3c5b3b36a6b182f293610e7bc2ff836c5b77235098b
~ _OUTLINED_FUNCTION_1 : sha256 524d2721ed18f636ea3d94136259b1ab2659581bfe6bb13d8a8b00132619ceca -> 7cbe2b8a3584bfc9db9187611ae3a930a94e9fc9de44b76421b9b97c4d209944
~ _OUTLINED_FUNCTION_2 : sha256 794a0e2ce873f305b42e890700a337bfd74b5969c046c4543a103a1f847fcd9e -> adf099621430d2fd06e45950954cb515968b958e3258022f0a6c796116b04992
~ _sysctl_upgrade_is_ongoing : sha256 c233a64828ea72d2a1f0ce05d98ef1e7aa19de53ee6b7b0db16fb4d58c867f91 -> d95b5fb702a4dc46529072f28e50eb7498e550f2de09ca3f584f790e0c72bdce
~ _cryptex_trampoline_upgrade_wait_options_create.cold.1 : sha256 21c007558e17d549cc706d1a597ca7fc218bb966ec21f4161beee7a143dbb33e -> e446c5772607a9dff5921b4e6e6cbfcbe1949a051a5ae98e518f8dfb6aa0bed3
~ _cryptex_trampoline_upgrade_wait_options_set_cryptex_name.cold.1 : sha256 31dd211fbbe89bbc2491843dbc16d1e48c807128b4335d0a15197958fae9f561 -> ce9be39202cba557a907e01a9039189a366d688a346bba041f964e7817c5dda5
CStrings:
+ "746"
+ "@(#)VERSION:Monitor Cryptex Upgrades Version 2.0.0: Thu May 21 08:14:42 PDT 2026; root:libcryptex-746~413/libcryptex_trampoline/RELEASE_ARM64E"
+ "Monitor Cryptex Upgrades Version 2.0.0: Thu May 21 08:14:42 PDT 2026; root:libcryptex-746~413/libcryptex_trampoline/RELEASE_ARM64E"
- "662.120.27"
- "@(#)VERSION:Monitor Cryptex Upgrades Version 2.0.0: Sat Apr 18 17:49:08 PDT 2026; root:libcryptex-662.120.27~92/libcryptex_trampoline/RELEASE_ARM64E"
- "Monitor Cryptex Upgrades Version 2.0.0: Sat Apr 18 17:49:08 PDT 2026; root:libcryptex-662.120.27~92/libcryptex_trampoline/RELEASE_ARM64E"

```
