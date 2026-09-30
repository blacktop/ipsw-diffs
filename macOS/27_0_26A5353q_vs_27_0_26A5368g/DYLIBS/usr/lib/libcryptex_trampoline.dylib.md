## libcryptex_trampoline.dylib

> `/usr/lib/libcryptex_trampoline.dylib`

```diff

-746.0.0.0.0
-  __TEXT.__text: 0x6e4 sha256:7feec1e55f5576b378e2e49112b3dc51ed9b07212941be64468810c50f081d29
-  __TEXT.__const: 0x68 sha256:89ed8c673e8416a6fa44d10b7773a5d4df2995fdb45542822cf9ced0e71c93b3
-  __TEXT.__cstring: 0x235 sha256:36d926e4494e429e5f2c815f0a8942e00b3f49c874ef39610464862f43a23ab8
+757.0.0.0.0
+  __TEXT.__text: 0x6e4 sha256:3cadb600952c9e0d693301515a297ff558c15ad6df1c03c4af6b317a4911ec2f
+  __TEXT.__const: 0x68 sha256:2c8dbbacc6606b5f4c1ec539aacd453190600d9ded87d67ddffbedb168e8952e
+  __TEXT.__cstring: 0x235 sha256:5939c00bece06313426c2f9e773d85927e6d9e53ef70f6402c7de6ac1c603d90
   __TEXT.__oslogstring: 0x104 sha256:54ae7e34b6b7a2b8e3e57a11ff8c643306866a2a34d7a2d127ee5a00b130d76c
   __TEXT.__unwind_info: 0x88 sha256:4834d1bbc7ec00f6f4162044a40e03e2e268daedd0d852dc9c1ee7f98b5c10e0
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x20 sha256:0e4c956fc70a9fe618483ada830ca6d17a388c7fb341249bf0123728aa4e6169
+  __DATA_CONST.__const: 0x20 sha256:baa196a2cd9008a4368e2ac3e1de0719e3c6390092b49d26e0cc06505bad0dd3
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x20 sha256:d3192d4169d6a0ea9d2eae637e85672b499bdfaa58d79f8d7beb957dfea78e28
+  __AUTH_CONST.__const: 0x20 sha256:e938888c5c0fda5467a26e84e768d7dc028ec38447df238216a7a1cd4ce6d4eb
   __AUTH_CONST.__auth_got: 0x0
-  __DATA.__data: 0x28 sha256:af2bef7d48cc6e0288d1cdd3a9856b62586774f849072d507d699e3ecaf3c2a5
+  __DATA.__data: 0x28 sha256:ea9461553984d3ad9b479758817c071770f0ec260825f2b4a19318a7473d57e8
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcryptex_interface.dylib
-  UUID: 0DC732E5-C821-3571-AF36-77100F1B4851
+  UUID: E14C306C-676C-3020-A013-728160EF369A
   Functions: 12
   Symbols:   50
   CStrings:  15
Functions:
~ _cryptex_trampoline_upgrade_wait_options_create : sha256 ca7275aead00ba7197c1b8fb7f09491959062ffe6e00db3bcfe929a99dae7dbd -> 811ab3190161464c54b6fc1ed498c4544fc5819cc7db37f0003200703f036189
~ _cryptex_trampoline_upgrade_wait_options_destroy : sha256 51cb42019813410fd77e613737256df658459099597685a5fe4bfe4dd62fbaf0 -> c40a1ee9d222163972506aaf57aee265d94a113cfa3bac396d69ebd6769231e4
~ _cryptex_trampoline_upgrade_wait_options_set_cryptex_name : sha256 473b0f8ea97a9d09dabc712c91a23a3965adca6d43864fb9bf8c8be66247d4ad -> f3594c0def218c3e5493f7ea9958aab632295be2f7ab08632b6a6d2cc8a74271
~ _cryptex_trampoline_upgrade_wait : sha256 d113c8bf4fdfff92538d1afaad1807b4ccab28bdc1e7485e3d88ea9f506fc31c -> 9068d8fac88c835550117dec7e89110aec2fa0345a46e1104d8c458fee1177a7
~ ___cryptex_trampoline_osl_block_invoke : sha256 1428e82297cb956056d8e801514a23d2901df0b465e1b317e2c6a731347d9d88 -> aea3c34fffa47bab5346b7015b10a40b0524bee4098285068ece145da2182520
~ _OUTLINED_FUNCTION_0 : sha256 9af7a2d47d33a6506db2274d65008d55efbc214801d1c8ca95c7db388103549f -> c2915a8a81cc5386588826f9be8440f3d38d0e1840482e0c6a175ac9e644cd58
~ _OUTLINED_FUNCTION_1 : sha256 834bb2410af052d48d729b24d8449a697818c53ca7dea24009483fc9c2b7dcdd -> 87584142a4c15ed97048379a741ef2b5b688ebf70fa0e3bf68ef1e319c8ac581
~ _OUTLINED_FUNCTION_2 : sha256 b5b52f4672cda71df29407e138f356886bc1ca9fb1a9bfe86bfd98a8d64bf43a -> e0f9f4732a3d417d2b09c1d85b1267a0f76ecb957678f69af3ea2c5dd80147fc
~ _sysctl_upgrade_is_ongoing : sha256 47777cc80d7008a33751de2a8f62ad6c9ecda1479c9b1ac9682afbc39382d7f4 -> bdc623a2c21be42d6ea3fb1904893be6113f30ebb3d8ff19c60a511ae11e8987
~ cryptex_trampoline_upgrade_wait_options_create.cold.1 : sha256 144b68b81039892dc8bcc83915ac67f315515d65dd74dcf4b931656a0a130feb -> 3486bf7b989e74d8731f578066917ac98a9e81b28b22b1a9bdc6daad986ec833
~ cryptex_trampoline_upgrade_wait_options_set_cryptex_name.cold.1 : sha256 34e7aae03825f8bdf6c0d83af2ea186856e0beb393c88f110e38b4581d890eb0 -> 6fffde5527eb97b37a7ec8f0ed42d2a70ddf31b0edd75571753559d417ed5e2d
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CRxNugBdsS3jAXL521_ygITUQHPiVpwnTXsyprA/Library/Caches/com.apple.xbs/TemporaryDirectory.zqiwBm/Binaries/libcryptex/install/Symbols/libcryptex_trampoline"
+ "757"
+ "@(#)VERSION:Monitor Cryptex Upgrades Version 2.0.0: Sat Jun 13 22:34:51 PDT 2026; root:libcryptex-757~443/libcryptex_trampoline/RELEASE_ARM64E"
+ "Monitor Cryptex Upgrades Version 2.0.0: Sat Jun 13 22:34:51 PDT 2026; root:libcryptex-757~443/libcryptex_trampoline/RELEASE_ARM64E"
- "/AppleInternal/Library/BuildRoots/4~CQCfugDKNS0pF0vCdUyGhQTCtIYWt7_b4096a9M/Library/Caches/com.apple.xbs/TemporaryDirectory.UfyHdq/Binaries/libcryptex/install/Symbols/libcryptex_trampoline"
- "746"
- "@(#)VERSION:Monitor Cryptex Upgrades Version 2.0.0: Thu May 21 07:45:01 PDT 2026; root:libcryptex-746~410/libcryptex_trampoline/RELEASE_ARM64E"
- "Monitor Cryptex Upgrades Version 2.0.0: Thu May 21 07:45:01 PDT 2026; root:libcryptex-746~410/libcryptex_trampoline/RELEASE_ARM64E"

```
