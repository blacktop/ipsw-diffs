## libLogRedirect.dylib

> `/usr/lib/libLogRedirect.dylib`

```diff

-64578.47.1.0.0
-  __TEXT.__text: 0x24b8 sha256:f389d4ad9499f0ba7af609b30e21debdcfa6c41f94086ba479fffc4e69df28dd
+64578.53.1.0.0
+  __TEXT.__text: 0x24ac sha256:9fceae0b66e0fdd1118defcb20abca6a514c3050d3dac134e86280a763c552a7
   __TEXT.__auth_stubs: 0x290 sha256:a9a88031b489952e67effea8b478f6d45e67a573352b77b5438f2da247882bad
-  __TEXT.__init_offsets: 0x4 sha256:32fcdcc2b0e503a34955606262880901e8deaed0947d21b89db0aee82fe99258
-  __TEXT.__const: 0x60 sha256:f117852eeeb8eaf4bbc4839ca5e19da1ae7eaaa357f23dc69e608c489be64112
+  __TEXT.__init_offsets: 0x4 sha256:93a23f65445030d5ed2d3db33decf8912f11385523247c7e6fe603c0c8c18d52
+  __TEXT.__const: 0x60 sha256:d0f2cc2982fea865e90fa9e441fc39e301e6e327be03b5f480a22a37c951ab06
   __TEXT.__cstring: 0x4b9 sha256:48c036d5932425fe1392bab1c8e7382f78e10362a44bd5e47c2e76c2104ee421
   __TEXT.__oslogstring: 0x19 sha256:03b9c5af5002b261a2485a2822310bbf11b00e36e6276fedfa0298632161cfa9
-  __TEXT.__unwind_info: 0xc8 sha256:2c9aa3b7ba5b05cf938292bd459ae7aea90fe3c89e8200352c9e35593ac15842
-  __DATA_CONST.__const: 0x60 sha256:0c718bdc9e3c6abc099dd9abf80760d5d8262e630dd031c87636dd0f66bd1a7a
+  __TEXT.__unwind_info: 0xc8 sha256:e98b6c07f3dd3c1779e49641f061c8174a69d64ad7ab3b25e2c7ef0f57a41eef
+  __DATA_CONST.__const: 0x60 sha256:50ab1798e00217166d1174d8a29de071af475a2e60a3ab175775b65ac3cbf0b0
   __DATA_CONST.__auth_got: 0x148 sha256:ae68491e27c8941d25c5f1c5b1fe2d6fefee1e72cf2ce84430f0185d5348ac99
   __DATA_CONST.__got: 0x28 sha256:681548202ddfd7d08a137d621e23a14dcc51789d79d9dee3cbe7a428dbb9d43f
   __DATA_CONST.__auth_ptr: 0x8 sha256:1c19ed81af03cadb5e4c42f613fb11eab92f53f7575a3d332a684a2169f3802b
-  __AUTH_CONST.__interpose: 0x50 sha256:1cff44299c4fe877e8105b19cca1cad7859768574912738e4d68bfa3c7dca895
+  __AUTH_CONST.__interpose: 0x50 sha256:18222030b322995cf901cf4d7bcffcc8ba2692445f2a9acb290deeddc886aec3
   __DATA.__data: 0x58 sha256:edcc5872fe2f32094c7977efc2905a211f9445ee4e455504b882acdb57742b99
   __DATA.__common: 0x18 sha256:9d908ecfb6b256def8b49a7c504e6c889c4b0e41fe6ce3e01863dd7b61a20aa0
   __DATA.__bss: 0x21ac sha256:9678b994aeabe08a6685767eb067893df19fc4e1ff74fee5bd72fa128bbadbd6
   - /usr/lib/libSystem.B.dylib
-  UUID: 50EFF61D-7B9E-3C14-A97F-BE34F4C0D668
+  UUID: 9103CCA4-77C0-3F90-9F72-DADB27C266BB
   Functions: 25
   Symbols:   114
   CStrings:  65
Functions:
~ _resetDyldInsertLibraries : 436 -> 424
~ _LogRedirect_init : sha256 c8e68c4288765267d0f8b04ad9c1ad30c32861f017c119ef8d778e2d1de433d3 -> 1eb73407b08be5c8e6248d7295a775b3a93267510574bb8d95d93ac84903987d
~ _LogRedirectWritev : sha256 67d8987498d96387ff400c3dab12cb8b57ef26319fd51a8ff2434c6b44e3f462 -> 65078f7a864ef373918a84d06c6c987c930bed9f578be045b2b3537ec2695c19
~ _LogRedirectSendToOSLog : sha256 7395503ee1eededad113d51b3a6199d27cd1f934d60edd07d669afb639fb44e0 -> 622620291cc430822e8fa5ab178270cfa4b6c6f33211d0021c31bc4462319689
~ _LogHook_init : sha256 bb108d458628095a54e5740ccb055d7302dd8704c2e07d8f5dde881039f83f01 -> e14c3d121139da676fa6bc7f405fa21205327f0e97cd402b2e3e6bd767ff9530
~ _LibLogRedirect_InitComplete : sha256 1e4e557813d14b5f88812db1f7283c915d7f91f79a7d2b1d0211a75c767453a0 -> 91e95a83f6a211246bbd7346540cc2de8c2436bbbf0f1a3457cfb5db156316a6
~ _HookWriteError : sha256 02e1d39bb35749acdbca2651799991c9ff1790ca9d4beb56a0b919e93a7dd12e -> d6b1a13e0ddf3855b0c909f6de6a0a7170eabe1f10ad090a0751a3266f324328
~ _HookWrite : 376 -> 372
~ _HookBufferAppendMetadataEndWithLineCount : sha256 c0c48b70cb5d0f0dfa3c6d943c64c84e028d584e08126e02a887dea0f903ef51 -> 4f5b005804c3f928fda1da1cd92f38b08490c367228b205988b4b6d1e464c377
~ ___LibLogRedirect_OSLogHook_block_invoke : sha256 10fa99a3ba6bdc21810a7f45b52bcdb77ad214f30f5963f27af1eb13431aa12f -> cc308ca4f70f2bb3fe59184bb6554e4745d32a2ea64c205be84266ad918090b3
~ _HookBufferAppendEscapedString : 560 -> 548
~ _LogPredicate_Init : sha256 d05ac1a4c87a0a66ba5696eda87b7ed3c51f69c5d333d3aea37c5cfbd8f9d715 -> 4927a498360771cda74b51498aebce8ae288e3848d63f73ca65db2ced1b87d4b
~ _ParsePathList : 352 -> 344
~ _LogPredicate_Evaluate : 632 -> 640
~ _GetIsSystemFramework : 144 -> 160
~ ___library_initializer : sha256 bc3e0db2be2ea68b06a8d5c915626c8ee7a1c4847163e65607494935a3ebd177 -> 1cfa9faf888dd787aee0d6c586c24d4d939b6acfe5b32c797de8d9e8230cb231

```
