## CPMLBestShim

> `/System/Library/PrivateFrameworks/CPMLBestShim.framework/Versions/A/CPMLBestShim`

```diff

 117.0.0.0.0
-  __TEXT.__text: 0x3a4 sha256:a621450f8dfba6272be7d3a426e97a108173952146bc875e93473e9b04f305d7
-  __TEXT.__objc_methlist: 0xac sha256:b028f03539498eea7c08ecacb932383c120dd5ea0d0a31ed9c9350d6499d3fca
+  __TEXT.__text: 0x3a4 sha256:b229f58b50439210a58e98dbc804cf1bccd99eedb9ac78d19df7297171365cf9
+  __TEXT.__objc_methlist: 0xac sha256:1b7a722a29befcf3f5a6d7c5d224611ecd39b989e1db9f6d58c329ba0dd2cf68
   __TEXT.__cstring: 0x2c6 sha256:330a6dbbbb0c90eb828a46d0e70175274777b75eb99f8dece6287e4031064331
   __TEXT.__unwind_info: 0x80 sha256:0562223a367c09a3d15b3ad55d0516932a6aac5c6ef5dbcf2f011d57e87be9ba
   __TEXT.__objc_stubs: 0x0

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x120 sha256:22d63e17e7d4fe35d9d602f0ffead76e257586bcf340e73a4b51aca4da49cc07
-  __DATA_CONST.__objc_classlist: 0x18 sha256:13547dc7a3556a0c0fddf38f0029b7f5691a623a2c7700d58c13454c2d28465f
+  __DATA_CONST.__const: 0x120 sha256:4a65764babec13bbbaf902fe946cd4717800051b54b1dbe98b6c38bc28d9559e
+  __DATA_CONST.__objc_classlist: 0x18 sha256:f4b3990fddd768b82870f2f406be45cfce3172fb97c1ea32690934daf85b145f
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x70 sha256:b730a204fb526307468b9524aa5ce44b3852d401cd61e3295bee9d6880f452e4
-  __DATA_CONST.__got: 0x18 sha256:8ac0bf4bcfdfac2ce2e34ffd393e2d535dfaef1af17bdfb9e244f749f21109da
-  __AUTH_CONST.__const: 0x40 sha256:d8bae31e936b17df136a9682d24b9369f89685436ca62297efded16493b9c13b
-  __AUTH_CONST.__cfstring: 0x420 sha256:85548c11382167478945cb011b77852091d9012a80a86d4a513e3506926eacd7
-  __AUTH_CONST.__objc_const: 0x1f0 sha256:e1704d5674acfb5a2c70d59173238c20253906e37c6c7183e414fd2fd8ce8027
+  __DATA_CONST.__objc_selrefs: 0x70 sha256:51b26beb1042f87361219c49e16ab1f18059299985821bc115a4f43f97a36955
+  __DATA_CONST.__got: 0x18 sha256:ee813079017dd1b0fd2a76206e35ba1e62689d7ef80dfc06feac6e125afecc1c
+  __AUTH_CONST.__const: 0x40 sha256:568dc630e79a84ad482821b384f60573bf5198a9c06500805dc68c3737061939
+  __AUTH_CONST.__cfstring: 0x420 sha256:c51815856b7fa4f7cef7bee3dd6db7f081475847f92a799756aa098d5890d014
+  __AUTH_CONST.__objc_const: 0x1f0 sha256:5f99cc2bc8a53b4c29c887c585115933835228d03331b775bf671ef656263a1d
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xf0 sha256:4243eade620555a007595a8b7cef8cc6cd890338bee28c8b09f86167c40e8fe2
+  __AUTH.__objc_data: 0xf0 sha256:d4df62bfc3b650622fa013fde84f8aa05062e341ec4b16765402a3e1721b2d1e
   __DATA.__objc_ivar: 0x4 sha256:dc765660b06ee03dd16fd7ca5b957e8c805161ac2c4af28c5a100ab2ab432ca1
   __DATA.__common: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb

   - /System/Library/PrivateFrameworks/CorePrediction.framework/Versions/A/CorePrediction
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2C6D3A5F-C7FE-3F88-A499-77D82A039410
+  UUID: 54C3CB5B-57C6-3174-BD02-48DF010C9975
   Functions: 14
   Symbols:   97
   CStrings:  67
Functions:
~ +[CPMLBestShim bestShim] : sha256 8436e075a2b85b0a6a32763dcd1cc4042ca5786dd7e384435e7cd76435a7a206 -> 51861a4ae325fbad9075201ec5768a97ca0e892424d4f273539a618cc389a1ad
~ +[CPMLBestShim bestShimWithDBPath:withModelPath:withPListPath:] : sha256 ea7e57c08c7dc6a230c58ea86e5f9e6c71d699b48bd425690d8cfb44a1fec091 -> 1864ec00411ec447edab1b60be93b941e4cae3a4803454a0877c6c337190f57e
~ -[CPMLBestShim rankItems:withMetaInfo:withNumOfRankItem:] : sha256 abdf3129ba2f4e3b1c58e08b33920d030b5b6b59e2aa3c363aaf7694f05e9900 -> 31c9f46265e9fb94e3b87dc3496615bd61b7efe227bf31b41ac4f43e62c7ecea
~ -[CPMLBestShim feedback:withItemsVisited:] : sha256 4898122cfbeafaaff46cabadf3e6a239c8343401ba769f575ef3c655c528e1c2 -> 5504fa6906d475eb0610a3aea15854a474805528603dc623aba1e579b34ae8ed
~ -[CPMLBestShimContext orderedSuggestions] : sha256 07968ef7e3327a20f7bed6ad43614451cdf4f0159fc630437b3fb073bb7ced26 -> ef327d82579e68ad3016242000f014087eb61030a498b5394daf159cb0a30dc7
~ -[CPMLBestShimContext setOrderedSuggestions:] : sha256 c29049e414b0f4608f770fd3b5cb0f09b1051b790471c865cf8a854230d0cfc0 -> 974ab23286f687e48060e2f4f7467bef5c0b4545dbab2b9cf2ce3f450a7eb6a9
~ -[CPMLBestShimContext .cxx_destruct] : sha256 e11c8b7e4b34acf0240ee2cb856a113e9cf453bd8af0192ba77033ea2dce68ce -> 51c73ca5cb8ab357cb620564620597e6dac908cb58ef2d4f99d9480531e422cd
~ +[CPMLBestAppShim bestShim] : sha256 abc54c2df5edb01b460cd1c2873f3a0205519e347fffc11b2e34cfa21e29c803 -> a1042c6aa146e5be20afe41413a14cd52cff4a3d54ff7847bc965daa9fb178e4
~ +[CPMLBestAppShim bestShimWithDBPath:withModelPath:withPListPath:] : sha256 53c3c086c128f2e29730c68968039bf1bcd9e835dacefaea84681bcd4d5e4fff -> 5243dad111db6e545e6df6e0b7d2b64e0b37c7fab2138812e1335ee2a672920a
~ ___66+[CPMLBestAppShim bestShimWithDBPath:withModelPath:withPListPath:]_block_invoke : sha256 e7aa21a07906312dfbb8a9be3f47ec7a9ff3383c6bf89262c703499e641e6d52 -> 6cbb3a95b9ee1508e4d1c8b02d4f2bbcf14b0cb289884da0af2bda346c42845e
~ -[CPMLBestAppShim rankItems:withMetaInfo:withNumOfRankItem:] : sha256 a1ff00b9ae445cb497d275afd336c19a0a96647e90b89f6eb41a78c00ef1d7a5 -> ea4c8ebddc0ecc09771f5a379fc389d516365b6c19249fd07f30bdd47eea2515
~ ___60-[CPMLBestAppShim rankItems:withMetaInfo:withNumOfRankItem:]_block_invoke : sha256 1ecac53bd52154684f66535c4aa503c6772d45e4bee242e58ffd26cb2e0a5611 -> 7e1d1f237f10a1a0dfd128f5c0334d468143dc76faf297350e1924e227d8c86c
~ -[CPMLBestAppShim feedback:withItemsVisited:] : sha256 844698fcbdea915c6e1b5f1f2bb17c6c22ba5a54051e94e69514c56af13f591d -> 72c3d40821da79e0e70a76176d9511e3b2e49b1031f2ef95225d3d5c44669baf
~ +[CPMLBestAppShim bestShimWithDBPath:withModelPath:withPListPath:].cold.1 : sha256 156edca20a599ddb047615103822648ba823ae5c601a89872629c2ea7435ea4e -> d61f7c345ec79d47c527a5d45723b60278ea4ffec9e28dde91e461d5c76553c5

```
