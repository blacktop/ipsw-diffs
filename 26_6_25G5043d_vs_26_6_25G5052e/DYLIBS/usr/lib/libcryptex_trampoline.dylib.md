## libcryptex_trampoline.dylib

> `/usr/lib/libcryptex_trampoline.dylib`

```diff

 662.160.12.0.0
-  __TEXT.__text: 0x6e4 sha256:93965ef054a779ce7dbcdae77510293c67c1e1f84fb0c198a849716aca2efa0a
-  __TEXT.__auth_stubs: 0x110 sha256:c0f0a33e30d27441a58dac02bc9a8ff19b92d6d4879fdc2efe9bbe544a649138
+  __TEXT.__text: 0x6e4 sha256:835417ceafef40e26b19522bd006e14225e57970b6f77f2bee7a52a2563c35d5
+  __TEXT.__auth_stubs: 0x110 sha256:f4206f81854cf331ce4121e3abb0c1fcbf68de6dee694a2ebebd1ee66b188af4
   __TEXT.__const: 0x70 sha256:9db9b19bbfe24bdb4e5490f3e77bbe408a03e85745b8a23d3ea6d4b91c33d5c8
-  __TEXT.__cstring: 0x248 sha256:f8695d90f9c2e2430cbb6147b7405eca2e6bd88e912460404e9ac9061af71a11
+  __TEXT.__cstring: 0x248 sha256:513a64dea9b33c6b157e159c7a442b47e1f5932ed0b44e9ca36de68185f7bbe1
   __TEXT.__oslogstring: 0x104 sha256:54ae7e34b6b7a2b8e3e57a11ff8c643306866a2a34d7a2d127ee5a00b130d76c
   __TEXT.__unwind_info: 0x88 sha256:0025af637eddecce6c0d3ae2d55b2273e5fd302214929272eb552c035f121fa2
   __DATA_CONST.__got: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
-  __DATA_CONST.__const: 0x20 sha256:81c715d9ab7fbf6e39342a1717ac1ccc1b520ec865eb3ad6a91c4516d542abef
+  __DATA_CONST.__const: 0x20 sha256:fe7278fe919b3e8446a60734b0f338bbd41524ea73fe9d69afaba38d5edf8948
   __AUTH_CONST.__auth_got: 0x88 sha256:b707241545a346265aab1ffb32ff64b55bf8f8dc1b56a46ef33ce3d15db11d33
-  __AUTH_CONST.__const: 0x20 sha256:5172740fcbf82fb660658501dd8de70c851b83c5c75ddf90644d97e274523bba
-  __DATA.__data: 0x28 sha256:bf444d79cf3b1b0a0168f3e9e7ed71187f79d36c39cfb215aec772c8f62984bc
+  __AUTH_CONST.__const: 0x20 sha256:26f8a10c4132cf9eda4019334368e57772cf4f2674b324bb57cc09c208563ce2
+  __DATA.__data: 0x28 sha256:b34835353358d3b7f40e18bec8270d0af82bc169fe9cab7ceec525cccb50386e
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcryptex_interface.dylib
-  UUID: 699BB7F2-44FA-335B-9E75-073111D8E5BD
+  UUID: F2EAA0B4-A4AC-3EA0-9470-DFD41820DFE5
   Functions: 12
   Symbols:   50
   CStrings:  15
Functions:
~ _cryptex_trampoline_upgrade_wait_options_create : sha256 6b1a2d84214896aee70f70a77cec6b4607ffdf62d521a23ec1695b245035732d -> 952341a724507471b0a62fdc430df658fdc5e572db52f91a97559cbaefd3017e
~ _cryptex_trampoline_upgrade_wait_options_set_cryptex_name : sha256 43face398a9fb1997055f661425c40e0be683b07e2640a4d1fdbe3fb9c58e786 -> 4484bba40a28ef61a24b672fd087310c1236038e74c27ecfcb7eeacf92a80919
~ _cryptex_trampoline_upgrade_wait : sha256 a2d9f1d85e424ffcb53bd343c58a4b5365ad78c800c49d55e87e0bedbe8a597e -> 24f1a05ec257a645b26125c233bc912978ea79d5b665721465b16cd2b2a3ba5e
~ ___cryptex_trampoline_osl_block_invoke : sha256 747b8690e31fe0657c69e7db139fb36e555ca0c75ff9c7235fb393bf7095a2f0 -> fd2f659a54d2b1bd0004e6e898afecc74da6b4c8eb5807fabc4db552f6f80e39
~ _OUTLINED_FUNCTION_1 : sha256 a2c7bf1e5bed716f8dcf0527e4a251b97cb184a7d87ba2c1a881cfcd88eb64bb -> 2ecae0d2c304dff9abdc2b5c792a1e3de6b49c39ca5fa80e27b9f892b3f879bf
~ _OUTLINED_FUNCTION_2 : sha256 ff75528eed5462c69bc21a85de2d696864dfb369bb2d51525780391435ed813a -> 159c8fb2c3005bbbce6608531772eccc20baf966abb05e5a028b8a54cb51920a
~ cryptex_trampoline_upgrade_wait_options_create.cold.1 : sha256 ba29dc07b36ce7c08ce4d677f65cf2ebfa33f31eec2ebf2db9394bfa8dfef85c -> 42583e2d5c9b9e6512d0641c119088237bc4f6a55789968623b7bc781e69d760
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CSA6ugBO7lb6n2BXQF0itQwW7_qBH9nKffcyAAM/Library/Caches/com.apple.xbs/TemporaryDirectory.2VkI4N/Binaries/libcryptex/install/Symbols/libcryptex_trampoline"
+ "@(#)VERSION:Monitor Cryptex Upgrades Version 2.0.0: Wed Jun 17 07:00:53 PDT 2026; root:libcryptex-662.160.12~37/libcryptex_trampoline/RELEASE_ARM64E"
+ "Monitor Cryptex Upgrades Version 2.0.0: Wed Jun 17 07:00:53 PDT 2026; root:libcryptex-662.160.12~37/libcryptex_trampoline/RELEASE_ARM64E"
- "/AppleInternal/Library/BuildRoots/4~CRUougA1QXzKQTdL5ggtL305ZIVNl96Aurz7t3g/Library/Caches/com.apple.xbs/TemporaryDirectory.5uzmP3/Binaries/libcryptex/install/Symbols/libcryptex_trampoline"
- "@(#)VERSION:Monitor Cryptex Upgrades Version 2.0.0: Sun Jun  7 20:15:28 PDT 2026; root:libcryptex-662.160.12~27/libcryptex_trampoline/RELEASE_ARM64E"
- "Monitor Cryptex Upgrades Version 2.0.0: Sun Jun  7 20:15:28 PDT 2026; root:libcryptex-662.160.12~27/libcryptex_trampoline/RELEASE_ARM64E"

```
