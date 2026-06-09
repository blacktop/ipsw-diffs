## libETLSAHDynamic.dylib

> `/usr/lib/libETLSAHDynamic.dylib`

```diff

-1418.1.0.0.0
-  __TEXT.__text: 0x2244 sha256:97f645474a757b2d02d521b79601cb016b3071b5c1886a4faab8f293e9d2815b
-  __TEXT.__auth_stubs: 0xc0 sha256:9801d1795f0c4ce4f87925813e7907548a004b4fe37fa5be5a7ba53cdfe60ae2
+1563.0.0.0.0
+  __TEXT.__text: 0x2500 sha256:60f7fce3019bc2066e46f35d43cd9a1ce957dff7f5640aef557642640c556c88
   __TEXT.__const: 0x40 sha256:5d2d7350a52e369c7bb1a1ed08c37783c70cc3d4cd0b19387e0ad4ff19de31c2
-  __TEXT.__cstring: 0x7fe sha256:ce6ab9b47d8438366a52240bc5f1cb6b5db6742458986d930fa41c7b1a8dd14a
-  __TEXT.__unwind_info: 0xe0 sha256:aed02b10938034acea28c30f659cb9e59fd207c7970da7b9ea863f2689559030
-  __DATA_CONST.__const: 0x80 sha256:c24ca5146612bb672c327c2e66cfe1decc1ec8f97a6b3e4a4b67aecf277b88b1
-  __AUTH_CONST.__auth_got: 0x60 sha256:2ea9ab9198d1638007400cd2c3bef1cc745b864b76011a0e1bc52180ac6452d4
+  __TEXT.__cstring: 0x95d sha256:c33d1d7fa2eb3802d5748d859c871969f1ab9d3851e36b373e2aa8cabe2100f6
+  __TEXT.__unwind_info: 0xe0 sha256:ff30d4c05f07bedbd8877274af2178ef8d3b2eda2c14fea60dc3686b4e136225
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x80 sha256:db6404845a8e5acfccf6e862c45d46c268092f79e66b8bce9d7e6fa5125c12c5
+  __AUTH_CONST.__auth_got: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libETLDLOADDynamic.dylib
   - /usr/lib/libETLDynamic.dylib

   - /usr/lib/libTelephonyCapabilities.dylib
   - /usr/lib/libTelephonyUtilDynamic.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: 6C7C03DC-DF97-3400-BC06-B60A63A5E572
+  UUID: 354C49B9-D341-3A56-B1C2-1A66BA6837C2
   Functions: 41
-  Symbols:   54
-  CStrings:  67
+  Symbols:   55
+  CStrings:  75
 
Symbols:
+ __ETLDebugPrintBinaryVerbose
Functions:
~ _ETLSAHReturnAsString : sha256 7d4ff8f5a5817f2aae42fad824303d00c89e626215158b633c9a62fe0db75efc -> 1c4400a5985c94daf510d78fca2d5677e620ab1adcc25949133d8c56d47d4426
~ _ETLSAHModeAsString : sha256 bb9ffc645518dd93604db612c74c84c821750ae73b255abdcf6990ce5ba2e5bb -> 6aa7d284767c0acab9c4d7872d6f06d3d66dba01bfb12d16dc7cdfb185fe8f96
~ _ETLSAHExecutionCommandIDAsString : sha256 60ebbfd33429e05fd3fd359043f819f6db4cdcf0ab6df9e620327d35808db581 -> bd0a73d9e40549395c1f275cfcff399026ad54e079eae2226e7c3f5d70ebff51
~ _ETLSAHCommandSend : 112 -> 200
~ _ETLSAHSendReadData : 120 -> 160
~ _ETLSAHCommandReceive : 308 -> 400
~ _ETLSAHCommandExecute : 724 -> 832
~ _ETLSAHCommandExecuteCreate : sha256 7eb9d3bd04c909583baa47bcc57b81e61d6ab31dcc39211807f4e43e55640ba1 -> a832bcbd50ba6193f7d4f9c536360e947f575bc0f50ba7464194485c93c73e88
~ _ETLSAHCommandExecuteParseResponse : sha256 ccd8c94eb1472ead0fefd607e1e870278ba04962a7cb2aca9e7ac7a49d057e1a -> 7767162c1fe4820a282eef9dd3d7b5ef76a6ba8a69cae9a604b95dccfaa10bf2
~ _ETLSAHCommandExecuteDataCreate : sha256 8280df5306ca8d946a166ddb060f683ab1e45bc8f96a78739248ec741a4ee927 -> c7ce214460f7d99b9e8ba792274332101e5548a0e34d7efde58ecdbb027ea60e
~ _ETLSAHCommandParseHello : sha256 53d1a9a45c29140f1231c02519fa0ac16b05c44f38fb96324a9a4ee0ebcd2310 -> 1ab9d54be6422651eee202aeb95f7e12fc6ad5014a86903af2d883b705c4b679
~ _ETLSAHCommandCreateHelloResponse : sha256 56c77b3658b81fb55df14ec611e0fcd9c26a491a1e2d7c942255c33553d2bb2d -> b4b60075536ae4647b1ad75460fea379df6f57eff368c6b26be4a107d99a7f48
~ _ETLSAHCommandCreateHelloResponseExt : 108 -> 176
~ _ETLSAHCommandParseMemoryDebug : sha256 8aa422014b3915d6c6e0d421c28c7eb613b96f4b492123517660386100a3ec33 -> feb83ee85212f0885dcd35d2acef43ee4f86120897d53f3c61d96610ceb6df04
~ _ETLSAHCommandParseMemoryDebug64Bit : sha256 cd8c218d6b7bb854f10622c1935d798d474b56880d461f442d62e3cef90c10c3 -> ed40dc463d4f23e8b97b1a9c4b316189ca04868741b0008f8580c73429040aae
~ _ETLSAHCommandCreateMemoryRead : sha256 16cc133b600476a3d09e59f87aa0a878b193f069a18ef853cb8e4d4811875480 -> d6e2cee10024c1cc1f83de9098750ead78f09c5f0dbbea60c0edd5728529f073
~ _ETLSAHCommandCreateMemoryRead64Bit : sha256 16cc133b600476a3d09e59f87aa0a878b193f069a18ef853cb8e4d4811875480 -> d6e2cee10024c1cc1f83de9098750ead78f09c5f0dbbea60c0edd5728529f073
~ _ETLSAHGetDebugRecordCount : 420 -> 476
~ _ETLSAHGetDebugRecordCount64Bit : 416 -> 472
~ _ETLSAHGetDebugTable : sha256 2dc3f7abd1531d207696fe9a952b8e1da503d7c30e0d497d72530d5cc69b3e6f -> 74bdde65568b878f9c0f32396de608907e07451188bc2aabb795c6768b3fcbd2
~ _ETLSAHGetDebugTable64Bit : sha256 4caded47d993f066d4b6b29654f23edafd919904ec9e6f0a7c0c7b9bb7259e35 -> c4626c9a96a5e77cfba9d51003711dfab723d173ff8162cbabb9c0c1f3239f88
~ _ETLSAHGetRecordEx : 560 -> 656
~ _ETLSAHGetRecordEx64Bit : 572 -> 668
~ _ETLSAHCommandParseReadData : sha256 5286c55ed6277787e797fd2ef4559ebfe4d7163560f0290077440622847977c1 -> 5ff8b9d7de276e2fdf814548c2bb16fc959603592037b0138170f8e79ce0bd0f
~ _ETLSAHCommandParseEndOfImageTransfer : sha256 144635c9e49ef3f031b0a9b7bd0a3b8fc14debf128e1fb737b7136fcee5adf5d -> 6d3bf8868c82a09caa3d99d76dd064908a6982983198011935db724cd0cd66df
~ _ETLSAHCommandCreateDone : sha256 651457f2878964b7592c22da06c65d66265d925b6630c24d7353333a7b48f96a -> 9e10dcac001847511e598870874fd0ff160e064c2ef75d3dac9d2fad6e7e5c0b
~ _ETLSAHCommandParseDoneResponse : sha256 88975047d23c492fdf62582454efdf4b89db411a1011fc9186058caf909864f8 -> 12372941e03c4259e81ee6dee7b313d3534cc26a4130e8f3a4b7a306e2cdb033
~ _ETLSAHCommandCreateReset : sha256 f3bbba21a15476d474e87ad67572b074da052f734a2a50fd5a904d06cb604097 -> 079b84ec3ef9c9b0ab9184c6d3fc6a02e66a63575a69d47bffd8ebc7755b4e5f
~ _ETLSAHCommandParseResetResponse : sha256 c7c7791344832e55e884b254210238f6b432f3ecb0aea4e2b0fddd51ffadda0e -> 1b891f6685f50ad1b5f5f6f953c3765bbde6f0db2774f34a890d4ce76e234656
~ _ETLSAHCommandParseCommandReady : sha256 3d85a9741b6945dec869f9347b094f9a5c911629673c49cda09e0142dcae6343 -> a4e11e7a442945ac78b0e91c90fc953fa05491ff3583af8dc4c6b2bc795830ce
~ _ETLSAHCommandCreateSwitchMode : sha256 2ba9e75389b6a8da5a57b7f64049c4c6d0a789c957ba6bda16933fa18eef4996 -> 29856b9444fd2802d7f284d3720758ff8a3d4dda943d6097bf42e739a6922b3b
~ _ETLSAHCommandParseMaverickEraseQuery : sha256 baa92a5dfef2d4e7766257ff790b08915f4ddb6b8b92ac5d2aba8a017f99c331 -> 789bd5c02753a75533467e018b00584a4d80f2963357fe74cf9000bb9e7047bd
~ _ETLSAHCommandParseMaverickSendHashesQuery : sha256 0c802b37157cea821ccd0d12224536f9e79627a35d8bc415c5f12f919bc8e1fe -> 12dc023b796041bddc27408ad55a4100f369efd502cd51761a10b7689f508968
~ _ETLSAHCommandParseMaverickConfigQuery : sha256 983d4b4378ce14f9accde9c2ca2cdb2844ef8851cceb3c0848d06ad6cac21536 -> f8ecb72ba702b53fe3a7f523880095b97043eb6c86ba49877ddd724a2b9e50e6
~ _ETLSAHCommandCreateMaverickConfigResponse : sha256 cd1aaa9bb55c04b59428f23135313312efa4e8f18b362ddc026a24c4a49e8a7c -> 1d389cc83ff8dc1dd672751bccd00a0835a40d9849334ca60ecedef68692ac76
~ _ETLSAHCommandCreateMaverickHashResponse : sha256 33e3c7d7fee9b339577be5ce2eec15c2bf8d33a183d23b869d7834687ba3f9c5 -> 13928586610b6f43b640f339bd2c202d26acecd37c6d4dc53eaba12ab6e6d7ed
~ _ETLSAHCommandParseChipID : sha256 0db4aed2a3178c7a8e7431b3d3f5545cd3e95d13908d42e41375f55418e91bd5 -> a2ceb3983e4c0e2d9b5eeddcfb2ef883d0ed3fb808642f1ebf4da5434476b983
~ _ETLSAHCommandParseMaverickRootManifestQuery : sha256 283fe21359b49cfbf7bc1317ca1fc9861e4c5e75969de0961ecd4c8b613aef96 -> 84f210c907726acab04dba20c1ffe3395ca02f521379e1715ecfcbeaf3c3006a
~ _ETLSAHCommandCreateMaverickRootManifestResponse : sha256 b6886c9a05c58c4d7eff7ecf151cb406cc475cd2d3d8028ff37fb99dc64a9bc4 -> 185baead10fdde0a86a7bb08a57b3fd3db0cbd702e64cd84c81a9a53f7edc980
~ _ETLSAHCommandMaverickParseEnd : sha256 2e46c8293d3b36af1a4de9ebedeb5962f90696dc6fbd519d16ca6f2764cc142f -> 018fab5d1bcf7ed1982211c7de71243b723bc711d2517159dc356389afa6ed1b
CStrings:
+ "Command buffer has invalid length %u, which is less than the size of the command header (%zu)\n"
+ "Couldn't allocate memory for memory read buffer\n"
+ "ETLSAHCommandCreateHelloResponseExt"
+ "ETLSAHCommandSend"
+ "ETLSAHSendReadData"
+ "Error: Given Reserved Length cannot be more than %lu bytes\n"
+ "Got Command of type %u, length %u\n"
+ "Sending command of length %u, type %u\n"

```
