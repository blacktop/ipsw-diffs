## libcryptex_trampoline.dylib

> `/usr/lib/libcryptex_trampoline.dylib`

```diff

-746.0.0.0.0
-  __TEXT.__text: 0x6e4 sha256:55f6f5c05184253e8ee0d113fa19266f183a9618270eaa8f19e9ebf1c77542df
-  __TEXT.__const: 0x68 sha256:89ed8c673e8416a6fa44d10b7773a5d4df2995fdb45542822cf9ced0e71c93b3
-  __TEXT.__cstring: 0x20f sha256:8f6ec5a1ce0b3ce0cfd711214e9d385ce4103ee036c2f52b987e65b10c91bb5f
+757.0.0.0.0
+  __TEXT.__text: 0x6e4 sha256:790ae833f9aa735a2e34168e8aafcf50bcdfd1a552e5001efb0ee6fd1d574f89
+  __TEXT.__const: 0x68 sha256:2c8dbbacc6606b5f4c1ec539aacd453190600d9ded87d67ddffbedb168e8952e
+  __TEXT.__cstring: 0x20f sha256:9b2bea64028a1aaf7665de10587f190d4a1a5071a046f929633128f8db3b6314
   __TEXT.__oslogstring: 0x104 sha256:54ae7e34b6b7a2b8e3e57a11ff8c643306866a2a34d7a2d127ee5a00b130d76c
   __TEXT.__unwind_info: 0x88 sha256:cd9eca24d1605ea99e5f770590146826d3a526de4639a6ef1e3890a2d9d1e5c0
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x20 sha256:18f1a6d9ece0fd8302d549b9acd271a23f48310177dff2ffb260ed34c3c2b2ba
+  __DATA_CONST.__const: 0x20 sha256:f13045f3c3e18b0a2816373d572ac379a3927eb39d96c303b200a92c6a008fc8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x20 sha256:c09603e913ac3e6582513b0e050a79369cd2ed0991be0892e7c11348dc2f1f42
+  __AUTH_CONST.__const: 0x20 sha256:e8d4411b51588b29585c23c17575d431b6e777ef112207d567e963206fe1d8b2
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__data: 0x28 sha256:805b1e764e6436eb1575b9c71a6dbb6d7b8bd236459fd4cd3cc58124b9fd4b75
+  __DATA.__data: 0x28 sha256:b472901ae28712d32566ee0f6d405894017ad3f2d4691386c84e812146ba767b
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcryptex_interface.dylib
-  UUID: 869F3D59-8AFC-31FD-8C03-2650B8168E42
+  UUID: CF37AE41-64FA-363A-A5ED-A68C269981F2
   Functions: 12
   Symbols:   62
   CStrings:  15
Functions:
~ _cryptex_trampoline_upgrade_wait_options_create : sha256 49230bfac7bf5f3536e4229fdb7359e73161b6f3429ac345eb2007d141d223a3 -> 5feca951580ef4a07c957f55591d717d4de90f34429208c7d12580fbe1b7446b
~ _cryptex_trampoline_upgrade_wait_options_destroy : sha256 a954060f8b110c9a93f385cbd4fa1b0f409dc8c241a67a32c77639d5e9933e49 -> de28b10612b4bb7acddd60f46433f0dbcda3a8452e2452d2e682a033f7cf0fb4
~ _cryptex_trampoline_upgrade_wait_options_set_cryptex_name : sha256 fcec088bf5b5a411e7abf344d9de9c73d77d2ab684800b392fd9e71f36e468d9 -> b5d5f7d663b55c1ae2c7a094282132022f5cbc8c5afe1ce1815dae680de17a83
~ _cryptex_trampoline_upgrade_wait : sha256 6392c264eb379654254dd5bb45f48b0b63dfc7659394fb8dae0c92c5737047f3 -> 59e7bd87cab3824f9fd2e842060d2340cc5964ee344cea757e886d35bac0726e
~ ___cryptex_trampoline_osl_block_invoke : sha256 4904180ddefdd58ae310fe3e04cbc1683b6b6b42b7078691dc45ce9621a7103b -> 59f26ccf2be1bf05e0ca4653e153fc660c0f45c1327a1228c49efd133b1e1e88
~ _OUTLINED_FUNCTION_0 : sha256 47212ec734ce7a26e78fc3c5b3b36a6b182f293610e7bc2ff836c5b77235098b -> da530675337ac116addd53120d490f32e335667c105413f7af667d981aa7a863
~ _OUTLINED_FUNCTION_1 : sha256 7cbe2b8a3584bfc9db9187611ae3a930a94e9fc9de44b76421b9b97c4d209944 -> 93c86bce709e0a535f18a6990881eb05b2e8802e83ba094d719a97ea63e0d60e
~ _OUTLINED_FUNCTION_2 : sha256 adf099621430d2fd06e45950954cb515968b958e3258022f0a6c796116b04992 -> 304f34329da3b26403d88e95f52777bb2dc9bdd662a21dc9f419583ce365f43c
~ _sysctl_upgrade_is_ongoing : sha256 d95b5fb702a4dc46529072f28e50eb7498e550f2de09ca3f584f790e0c72bdce -> 26dc5befbd35febcf592d920e3af11fcf9354c3e40d6a1e68170e081daca0d43
~ _cryptex_trampoline_upgrade_wait_options_create.cold.1 : sha256 e446c5772607a9dff5921b4e6e6cbfcbe1949a051a5ae98e518f8dfb6aa0bed3 -> 1dc91aec57d0fc4a302cf1cf77305c25862b39eff03c900050a5327631462678
~ _cryptex_trampoline_upgrade_wait_options_set_cryptex_name.cold.1 : sha256 ce9be39202cba557a907e01a9039189a366d688a346bba041f964e7817c5dda5 -> cb4aa47e48ebc45dad07dab8e6402f5f08f5d361f397bad31791fd5f10a12f5f
CStrings:
+ "757"
+ "@(#)VERSION:Monitor Cryptex Upgrades Version 2.0.0: Sat Jun 13 08:36:07 PDT 2026; root:libcryptex-757~412/libcryptex_trampoline/RELEASE_ARM64E"
+ "Monitor Cryptex Upgrades Version 2.0.0: Sat Jun 13 08:36:07 PDT 2026; root:libcryptex-757~412/libcryptex_trampoline/RELEASE_ARM64E"
- "746"
- "@(#)VERSION:Monitor Cryptex Upgrades Version 2.0.0: Thu May 21 08:14:42 PDT 2026; root:libcryptex-746~413/libcryptex_trampoline/RELEASE_ARM64E"
- "Monitor Cryptex Upgrades Version 2.0.0: Thu May 21 08:14:42 PDT 2026; root:libcryptex-746~413/libcryptex_trampoline/RELEASE_ARM64E"

```
