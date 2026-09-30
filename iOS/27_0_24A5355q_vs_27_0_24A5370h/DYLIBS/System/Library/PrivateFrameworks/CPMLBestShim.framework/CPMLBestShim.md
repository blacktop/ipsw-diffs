## CPMLBestShim

> `/System/Library/PrivateFrameworks/CPMLBestShim.framework/CPMLBestShim`

```diff

 117.0.0.0.0
-  __TEXT.__text: 0x358 sha256:a0dbaed1312b36fbb44634d55bb9b06c75ecbbe02bf60cf048aa86d3da0394d5
-  __TEXT.__objc_methlist: 0xac sha256:2c22353df191ae1943699d3e9a06ff594c9c452a4d4b29a990481e9223978920
+  __TEXT.__text: 0x358 sha256:cd93a18a010b072f34bf9508fb277191b23d39b0b16360c4f3039a172ba144bd
+  __TEXT.__objc_methlist: 0xac sha256:ed1c75ed3d745bda2351fb9fa8ffb1f9f6361132d954a28cf5dfdbd9bc1b37fe
   __TEXT.__cstring: 0x2c6 sha256:330a6dbbbb0c90eb828a46d0e70175274777b75eb99f8dece6287e4031064331
   __TEXT.__unwind_info: 0x80 sha256:26d52688380e1218e0d0e91d0e8593edde8e743c8c36c567b3069fc0ce6826c4
   __TEXT.__objc_stubs: 0x0

   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x120 sha256:28fa020c04e028bddd6668eff78aa9bb786e74f3203ea666982fbe5dec3c6658
-  __DATA_CONST.__objc_classlist: 0x18 sha256:ed7d6426f0bd476c741057c4d63caebf81a9e8e1fec18c67f219123944376a84
+  __DATA_CONST.__const: 0x120 sha256:5b0de85ab0e50706609e03b320346d172eaaa59fbfddd01fbc3a1a34fa10a961
+  __DATA_CONST.__objc_classlist: 0x18 sha256:882553103b9ee5e4261381325d4c6a1e8b9d98caa117afcf3cc7dd9cffae4c07
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x70 sha256:7d3d54575ee33c1dcca1255ddbb8251687b81377907ffe276cfe230147760bc8
-  __DATA_CONST.__got: 0x18 sha256:84e2134fd2d352338b8af9b91d26975984ad2c7709b11145c9ea420992556317
-  __AUTH_CONST.__const: 0x40 sha256:0a5ea9749ec5a7c02c5d04e6731d85683eb70268c8d8ff864243276ecd0a34a0
-  __AUTH_CONST.__cfstring: 0x420 sha256:5533085e805b1a89b49bdec91b26894cc2ae8918433cfac72375c94f804d1ab9
-  __AUTH_CONST.__objc_const: 0x1f0 sha256:9c59b8541adfec63a9c110e153aafa3168ff0442abc40dafa486b1f034f2c38e
+  __DATA_CONST.__objc_selrefs: 0x70 sha256:a1d83708c403669ab473a0c50dba631b18e95eb4685ecd37aa25579c9b5ebca5
+  __DATA_CONST.__got: 0x18 sha256:0a18aa6e1bfe456d7bb22fbb3db10680f2b2829b1708867b01580d256f9cd5e2
+  __AUTH_CONST.__const: 0x40 sha256:6145c0bdf1a8575dc758d5008699ce759a6d55087b76d51812ded882aac3e89d
+  __AUTH_CONST.__cfstring: 0x420 sha256:58178b68261acd0ca69dad33fe59a1d067c6d6e0fbd1349af33362d4e0bf0a9c
+  __AUTH_CONST.__objc_const: 0x1f0 sha256:ec64cd678d95398029cae512b00102f5ad4ce3d66292f948143adc43bda4daff
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0xf0 sha256:a796ce46da0c949d8258c8c18d4b2961ee31941ca57df637cb9e93fc8287284e
+  __AUTH.__objc_data: 0xf0 sha256:21afab541d68100b1a1b8de31da25c2955ad0b5eeec62d5e45413fc08a59950b
   __DATA.__objc_ivar: 0x4 sha256:dc765660b06ee03dd16fd7ca5b957e8c805161ac2c4af28c5a100ab2ab432ca1
   __DATA.__common: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb

   - /System/Library/PrivateFrameworks/CorePrediction.framework/CorePrediction
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C0B4CD8E-9086-3EA7-A636-B34980C72C03
+  UUID: 6AA891C3-C119-3873-8E75-25C99F5033AC
   Functions: 14
   Symbols:   118
   CStrings:  67
Functions:
~ +[CPMLBestShim bestShim] : sha256 df3509288bccfaed7a4d391342e486825f4f7e1d243f6c7ec01be66077512fe5 -> d40190ea81d260a01ec00d4367b580be1e53e2fa3f29c9ded063ebcaf1ea181c
~ +[CPMLBestShim bestShimWithDBPath:withModelPath:withPListPath:] : sha256 f39e3b83a10b8c6a6f832f846267f357b0be9d400988ed9d042426a9d50b33aa -> c1573166026d1c3202ebd5607b3a6cf30815401f89b80ec4793c147f057be093
~ -[CPMLBestShim rankItems:withMetaInfo:withNumOfRankItem:] : sha256 b299e99f823e8f988e2b9472f7cacddfd9d2f752a05a4db8b11e2a8b548b6de9 -> 1957a5c1db66bc7bc3daab3042e0e7702c55863d5c48d626b1676b413666f889
~ -[CPMLBestShim feedback:withItemsVisited:] : sha256 c3f5ff6c0b9630a53cd87aed9a45d22746555ffc2139999d57775d7598578e1a -> 8f47a0e8292a646d25a35f41c8770c8915de2a62fe4202344552f42b625f2a75
~ -[CPMLBestShimContext orderedSuggestions] : sha256 0fea3991d7ce4b0ba7df24d8b03901c2bd5988a817d9dea8df6d10ead9b486ab -> 3756351de565951c285d629cbad9aa830d61f518f19a1d43bc353f4ce19c1dc2
~ -[CPMLBestShimContext setOrderedSuggestions:] : sha256 bc43025ab4ae2aa45c8823be37d3ce01a8cb5e936ef9870827508997d574e21f -> abbdd9c59a531cbca284879684376234cbe63efaf06272bdce817d5010fa958c
~ -[CPMLBestShimContext .cxx_destruct] : sha256 9f31a5fc6bead1133d2612687a34ab2ed23cb6146459844724bb27eac012f5f1 -> 845066e661e317a17d6b486d004b5872cb697b57816aad6796bc74c6fabe8917
~ +[CPMLBestAppShim bestShim] : sha256 e796209bf2c9982480103dee910f82f7137a10a1bd2ab4e45b8c053bd174ac44 -> 645a3b00e47baca873ebd3ebec4970eb581cbdad6365de75b1457005999d6ccb
~ +[CPMLBestAppShim bestShimWithDBPath:withModelPath:withPListPath:] : sha256 5efddb839cf70035fc713d8209b7a4bc7bf533bcd168126489ec7f27abe622be -> 96567bbd7ac0bf211b9ca0bfba44cb619d65e7a0957173451e1e5d2b9e5177ef
~ ___66+[CPMLBestAppShim bestShimWithDBPath:withModelPath:withPListPath:]_block_invoke : sha256 a23c621a7944e2853d5113a5da7170a18a0e89a088f414590f54b228a7ff64d7 -> ef44a47ddfa04074ddb225f1218cc3cb6505497571de29d939274abeec0fe7b2
~ -[CPMLBestAppShim rankItems:withMetaInfo:withNumOfRankItem:] : sha256 cd72a3e05ed149adc98ce05dbc376a29dd26f5804aa2aa0acfc8285c516e5902 -> a988194dc44cf5fd60f51a25803fb934f5868eeb87cd26ab7e1bccb84e0b86bd
~ ___60-[CPMLBestAppShim rankItems:withMetaInfo:withNumOfRankItem:]_block_invoke : sha256 282ce7dc6acea351b2171c4d58122392e8458c6af2defc6a865d02ecbf8d0d2c -> 0281b657fa6a653ce92f6f19a7bd27a9b9070f061080d8160a73e5e16e27b226
~ -[CPMLBestAppShim feedback:withItemsVisited:] : sha256 804315ecba1e51a70e5d2dd8158143151901bd776d092e1c5914df45ce207350 -> 1afd7bb3eb97ed7fef25eccbce81426eee38877096628ed51dc757706d66bece
~ +[CPMLBestAppShim bestShimWithDBPath:withModelPath:withPListPath:].cold.1 : sha256 102a2db43cf50f1d8c85e447fcb7e6463d3822c2af24a47f4fade4e18667ec9e -> c11379495d10e339e77e32ef62f8d73f22f75bee6e79bc5f866bd6754050d323

```
