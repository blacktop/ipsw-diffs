## libLogRedirect.dylib

> `/usr/lib/libLogRedirect.dylib`

```diff

-64578.47.1.0.0
-  __TEXT.__text: 0x24b8 sha256:b22526ea85e73d1b2f8538c310d943f5da18c64f0b1c02136269064d5f61a235
+64578.53.1.0.0
+  __TEXT.__text: 0x24ac sha256:077d91bc0bdf66cc6cfb4aa96235ae252b583ff12bc4050c8c8f0ff69f6f07f4
   __TEXT.__auth_stubs: 0x290 sha256:a9a88031b489952e67effea8b478f6d45e67a573352b77b5438f2da247882bad
-  __TEXT.__init_offsets: 0x4 sha256:dcb136d1dc7e49c749e0cdbaffe652de5109b41f661e4a4109899d8880305107
-  __TEXT.__const: 0x60 sha256:f117852eeeb8eaf4bbc4839ca5e19da1ae7eaaa357f23dc69e608c489be64112
+  __TEXT.__init_offsets: 0x4 sha256:6fb69f64497025a0c459d4efa8ac6e940ec5f3fde44996693db38e0e5190af72
+  __TEXT.__const: 0x60 sha256:d0f2cc2982fea865e90fa9e441fc39e301e6e327be03b5f480a22a37c951ab06
   __TEXT.__cstring: 0x4b9 sha256:48c036d5932425fe1392bab1c8e7382f78e10362a44bd5e47c2e76c2104ee421
   __TEXT.__oslogstring: 0x19 sha256:03b9c5af5002b261a2485a2822310bbf11b00e36e6276fedfa0298632161cfa9
-  __TEXT.__unwind_info: 0xc8 sha256:a5619fb961af31453a9abd269ec54e4ee1f3644ce4a95727386f124ae9648433
-  __DATA_CONST.__const: 0x60 sha256:a41b73be31053dd0c4559cb654ccd855a66b32e9623405e01aa6c02bdef19f1c
+  __TEXT.__unwind_info: 0xc8 sha256:8dc1af4c832a7d00fdb6fb61081c0f167b4d262abf5c64e97e560006ca1440c5
+  __DATA_CONST.__const: 0x60 sha256:98f574598695775204f7b4f9ec8e805d8279999cdf6c734de51eb97fbd7bb8e6
   __DATA_CONST.__auth_got: 0x148 sha256:ae68491e27c8941d25c5f1c5b1fe2d6fefee1e72cf2ce84430f0185d5348ac99
   __DATA_CONST.__got: 0x28 sha256:681548202ddfd7d08a137d621e23a14dcc51789d79d9dee3cbe7a428dbb9d43f
   __DATA_CONST.__auth_ptr: 0x8 sha256:1c19ed81af03cadb5e4c42f613fb11eab92f53f7575a3d332a684a2169f3802b
-  __AUTH_CONST.__interpose: 0x50 sha256:bc64dad105a7aace4e0dbed8dc3281028069f730386a60dbb5f939b6552a316b
+  __AUTH_CONST.__interpose: 0x50 sha256:dd7ee44da2889063b35732ff713714cf26e0e16caea76b87e50a6425cf46e582
   __DATA.__data: 0x58 sha256:edcc5872fe2f32094c7977efc2905a211f9445ee4e455504b882acdb57742b99
   __DATA.__common: 0x18 sha256:9d908ecfb6b256def8b49a7c504e6c889c4b0e41fe6ce3e01863dd7b61a20aa0
   __DATA.__bss: 0x21ac sha256:9678b994aeabe08a6685767eb067893df19fc4e1ff74fee5bd72fa128bbadbd6
   - /usr/lib/libSystem.B.dylib
-  UUID: 23946312-B822-3A98-AA16-214DD59B389E
+  UUID: 5113E905-7EF1-346B-A22D-6492181C724A
   Functions: 25
   Symbols:   114
   CStrings:  65
Functions:
~ _resetDyldInsertLibraries : 436 -> 424
~ _LogRedirect_init : sha256 ea0d40829452d23adcfcf5e4f7ea136658d7ca698311297a499d355afcb798f2 -> a944c8d9eb32b036801436f74f0b2779f121e367aa2c0136567af6cee5587a63
~ _LogRedirectWritev : sha256 3919394884d205412c44d1e08bd7dcaa6ad318248ea8952d6aecf436879b79bb -> 0a57be4bdb16cc025ff79086ef60142ac4083d7ef7bd063d7a86a4975624bc4e
~ _LogRedirectSendToOSLog : sha256 d6f83afb5abd3be31e4dd9e5ea63be4ae70609266c7b96cce69ce0a0ecad872a -> aeef380935bbf3695657676727d3d085db3cb87223f0adcf67d7a5458bc38eb4
~ _LogHook_init : sha256 1e18661485bb1183d4f971f4191f1f5ef1b0177b73514adb3cd631bde4257810 -> abee181a88f0368a11465552b36b1077c8c52b281851745cc2d25d078ed64e79
~ _LibLogRedirect_InitComplete : sha256 40bad39d09d79d082f3a8784e69fe9dae5c524936ead8890d6165690abb06646 -> dcc77749c12f57c9bc68c3b7e7a8bcd415b221120a8e01754f79775b83f6692a
~ _HookWriteError : sha256 6a7d5ab9b4c669d8a7e6c93ae5ce1bdd93bbb89b9c11f8cb03ae963cf2e2ad26 -> 9421ff9d188e458299fe5ecfbfbf7f06439ae0e958d2558590409281f47f3c8b
~ _HookWrite : 376 -> 372
~ _HookBufferAppendMetadataEndWithLineCount : sha256 288cec23803c69b11f761819c84b512b50a6f0bc10dc6c398a9fc7c39e9fbd0a -> 8819b90cfaae8fc2e0e8907d2a33690b2de4431f1f2ec9d53db4e610b88b4508
~ ___LibLogRedirect_OSLogHook_block_invoke : sha256 f096d1ce45ca540ea617d32dff9f7c8a14f7cd12e92b6999bb55b1a3257f2c27 -> 902412b52b2909f23c211bdc1b070f53dd8687dd655b5cc714edf45f5d02b169
~ _HookBufferAppendEscapedString : 560 -> 548
~ _LogPredicate_Init : sha256 8546e82209ded6fe3746a1204069233e99f22b0f98f503a7854ca45fe3d387b5 -> 9feecd42522bcc96a08b8a2c19b413e533dd315e1ca9d5ff08ff38b8d7ebbe07
~ _ParsePathList : 352 -> 344
~ _LogPredicate_Evaluate : 632 -> 640
~ _GetIsSystemFramework : 144 -> 160
~ ___library_initializer : sha256 899711d9acc7a0e3d1397da92ca6b964c95f6477c51633adc33ef1bd8fdd3f35 -> d0ad6fdd6cd28092997fabae81b2d229544826f15cd63912fd89b8a6decef0d7

```
