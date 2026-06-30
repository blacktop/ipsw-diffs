## libmarisa.dylib

> `/usr/lib/libmarisa.dylib`

```diff

 26.202.0.0.0
-  __TEXT.__text: 0xfd84 sha256:186920632ccab526e91c43c4f053ab772616afe5afa3aab6eb9c49f44ee67ee8
-  __TEXT.__auth_stubs: 0x210 sha256:dec209bc61a1fc9e9ebf5b399bced369de38af2ad41219b154f9d522457b97bb
-  __TEXT.__gcc_except_tab: 0x768 sha256:34196970de281b8f30391e5f7141a95bcec107f48fcfacb8428da27723273c57
-  __TEXT.__cstring: 0x6d0e sha256:698d978ec498d0e0b9a2bda9edffe7f7f57a224360311a9cad38cdb1f4d9b5e2
+  __TEXT.__text: 0xfd84 sha256:43946b69cc422e3e0c3a9e7c63acd1bd0dda4a64ea704bd0b682b8bd1b42cb29
+  __TEXT.__auth_stubs: 0x210 sha256:a4fdc021d04577004d11e998c8ad4a5c68b36976e8f40f5d39bfdaa65b9920f9
+  __TEXT.__gcc_except_tab: 0x768 sha256:4f86960a76465da22e69298681b5fe26ca3418ebb324d16d5c019a52001848e1
+  __TEXT.__cstring: 0x6d0e sha256:1d748e3689ea0a74c6ef1906b228e7cd9237d49486c0ad39a159723bab4dda4c
   __TEXT.__const: 0x8e0 sha256:0e98ae520f4df953dc6bca01eb1843ad7a383aaae50d5e52fbb44459bd34c7ad
-  __TEXT.__unwind_info: 0x678 sha256:8dc733943795e10b18fe2c9d3780b0166aeac47a29b1075cf3e74dfd42b7c8eb
+  __TEXT.__unwind_info: 0x678 sha256:dc74d31a5e24bea7764eb14197f7873e494fc47a862adafacf25dece26fb8ad1
   __DATA_CONST.__got: 0x30 sha256:17b0761f87b081d5cf10757ccc89f12be355c70e2e29df288b65b30710dcbcd1
   __AUTH_CONST.__auth_got: 0x110 sha256:a94b5c349050699caacb00a31462b4ed3c9afcb9a490a4cb8983451288f6c925
-  __AUTH_CONST.__const: 0x40 sha256:3bacc71416a622947ac7fa2cfa4cd534ffc00a23527ca4677ae87989fe77fa77
+  __AUTH_CONST.__const: 0x40 sha256:0176f4673d763bee2c324ab7c621202995195985aca818bb404aa7c73c733786
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  UUID: AAE00924-042F-3983-92E0-AD06E1D50FB0
+  UUID: 4C44864B-6719-32AE-AF06-24775B5FA246
   Functions: 423
   Symbols:   627
   CStrings:  131
Functions:
~ _OUTLINED_FUNCTION_0 : sha256 b0273a230d6af3cd013c15580b0d67affc4c6afb362548fcf9269c2157f7db9a -> 5545cd1beed2903e81fc9e8a58732b463e03fa191a911cd22a73d8175caea143
~ _OUTLINED_FUNCTION_1 : sha256 22073a3a87e9f061e96cb0f6e3381b14b09ce40c1356f8d70e04125941ae2a8d -> b715432e129263aa85a10c83ecb548710999730188bf2cec51cb185c7d76d6dd
~ __ZN6marisa8grimoire4trie9LoudsTrie4map_ERNS0_2io6MapperE : sha256 63be96137cd253383a56536e1235f93a2eda2d3bd2c47fdb05d9ad6f2cf413e5 -> 51505a2af0791439bac2887fc6d2a12243fb3d6aec511446ce457cecc5a24490
~ __ZN6marisa8grimoire4trie6Header4readERNS0_2io6ReaderE : sha256 3f1999fe4e85c18500828dfe4d10003ed70ae96f3bd7ec50d5916742651d98c1 -> 607045c3348319f0528011e277ff93c0c1482a13c962ddd709b3aa7637af48f2
~ __ZN6marisa8grimoire4trie9LoudsTrie5read_ERNS0_2io6ReaderE : sha256 c127c845189781d6f591464cbec800332568f58054ac9755ac21c923a0c66aac -> 24acc0f7b5650e8ddec09910a992fdbb574ec7792aa1387d7cc09153edc697d6
~ __ZN6marisa8grimoire4trie9LoudsTrie15build_next_trieINS1_3KeyEEEvRNS0_6vector6VectorIT_EEPNS6_IjEERKNS1_6ConfigEm : sha256 9265994a8794b6b86390bc36bfe7612af1e62cbe22f8ef1b7251030306a71f46 -> 1638997fb14f628f47bb19dc724ffd761f2108f4e340cadcb30337d9fa8be8e4
~ __ZN6marisa8grimoire4trie9LoudsTrie15build_next_trieINS1_10ReverseKeyEEEvRNS0_6vector6VectorIT_EEPNS6_IjEERKNS1_6ConfigEm : sha256 ca36d3e818075df5ed81abc4fbbca942b612c753707a0ac3b4ebc8043393fbb4 -> cb00847d0bcb8e02fa70482a24011c6b4f9fdb993bc1b3bccf1b21d178a5e0f7
~ __ZN6marisa8grimoire6vector6VectorIcE7reallocEm : sha256 bee4c44b6b792de301caa58891aff10bb2a6015fa3ba52f0710e7d98696fd45e -> 6c4a3472a4541db74da77b3d59e47b06603ace10eb885ba12086b5cbb6c0d29a
~ __ZN6marisa8grimoire6vector6VectorINS0_4trie7HistoryEE7reallocEm : sha256 38b0d5a44a54395451431010004c9c496d194999cdc869119680bf72a9ba0bfc -> e5f3b2b7a1dcb9e7a4d4da3651ad6dc67aa1c3cc612ca259f2f26ded5247a1e2
~ __ZN6marisa8grimoire6vector6VectorIyE7reallocEm : sha256 6aa22fb87c11128e2cb04128f8713ff6dabd78ba1e4ef04f543f60fec52c744b -> 3cf2dd588c0b0a5917991e536856180392cc8fcfd41fc170effad052a0ee6ba5
~ __ZN6marisa8grimoire6vector6VectorINS1_9RankIndexEE7reallocEm : sha256 3f7b8967aa480b88979a8b17a4cfeac350a116d914f5648231548fecbc9fb169 -> 604784610ca49af09b512d78ce829722b35eb8fca4130fa964e3a9448e3e53d1
~ __ZN6marisa8grimoire6vector6VectorIjE7reallocEm : sha256 acb7dc6f270ce6f477d9d5860546e5b06532e98ebdc5459f2e3115f99d3d5405 -> 94209e3d2cfcdf2ca65bb580d890c52536db54302ba5650f39c62dfa2b8e8d30
~ __ZN6marisa8grimoire6vector6VectorINS0_4trie3KeyEE7reallocEm : sha256 d77b0595b861c16d86b36b1162c4ed03cdab18e2ac912c1ee31b0bf61d73eddd -> 95274f4d5ec8be443793fdb9955744c602eddc7c45e6b1055932a0425cdc71fd
~ __ZN6marisa8grimoire4trie9LoudsTrie18build_current_trieINS1_3KeyEEEvRNS0_6vector6VectorIT_EEPNS6_IjEERKNS1_6ConfigEm : sha256 286aa119d3865fd3e55bd15f02661acb183990679f386345902ecc5037b4fb8d -> 714e498b44bb855db150aa78f1174b5e1957c9c00948caef39352a10a4a7d4e3
~ __ZSt28__throw_bad_array_new_lengthB9nqe210106v : sha256 e262d37b366e7ff6af7543c60861b5368347213fb2293208d9a496b3e4f6ba72 -> 9e95a9779d8745b230757cb8146250649c9f80dd22439adf297589540899375a
~ __ZN6marisa8grimoire6vector6VectorINS0_4trie13WeightedRangeEE7reallocEm : sha256 468f3852097b24a94f9ff589f9b4fc5859538997278b7b4943f94b99d2120e78 -> 6eb1399e6901b2f543156a6b6bbd2e0e9231ae0dbc37964f54fa842a3016b16c
~ __ZNSt3__118__stable_sort_implB9nqe210106INS_17_ClassicAlgPolicyEPN6marisa8grimoire4trie13WeightedRangeENS_7greaterIS5_EEEEvT0_S9_RT1_ : sha256 91695b992f6194326d742d810fd4281a2bf831630f6fcf2f4975d0b8f974be2e -> 7defba3eb580bb492aa77df605a1c6bb7c3184441bf390003b0a949513307d55
~ __ZN6marisa8grimoire6vector6VectorINS0_4trie5EntryEE7reallocEm : sha256 28b08548645c6128340895a7b829399cdc3f7897f7482a1440ed1559af1edf57 -> fa0257794c508f5efb24cf955b1c9b0df9900fac67e7694c9faa15f2b85a4b45
~ __ZN6marisa8grimoire4trie9LoudsTrie18build_current_trieINS1_10ReverseKeyEEEvRNS0_6vector6VectorIT_EEPNS6_IjEERKNS1_6ConfigEm : sha256 84026ea29dc9b305cf5c500c9f2314c5e34a82ecee25cb3fb444a686af19e8fd -> 2c42c7a344f2852bf233f8566ac6d8630b995d69bb73e60ebe2e3957ec75540e
~ __ZN6marisa8grimoire6vector6VectorINS0_4trie5CacheEE7reallocEm : sha256 64b4ef5d40d4c768c381e92f8830e5bb461c969f0c044582a1285b760cf15775 -> 02ea7e4ba31861bdd49d75bc40e55dcb49536c7f2332a1ad68749306410f2e74
~ _OUTLINED_FUNCTION_1 : sha256 b7219142d16979d22a18f24c717e21183b894c984132f6fd8878950def45ccb8 -> 796a6ca50a78d6ec8131f447503f5ea4d54684ede616963b099ee353e559f414
~ _OUTLINED_FUNCTION_2 : sha256 b7219142d16979d22a18f24c717e21183b894c984132f6fd8878950def45ccb8 -> 796a6ca50a78d6ec8131f447503f5ea4d54684ede616963b099ee353e559f414
~ _OUTLINED_FUNCTION_3 : sha256 b7219142d16979d22a18f24c717e21183b894c984132f6fd8878950def45ccb8 -> 796a6ca50a78d6ec8131f447503f5ea4d54684ede616963b099ee353e559f414
~ _OUTLINED_FUNCTION_4 : sha256 b7219142d16979d22a18f24c717e21183b894c984132f6fd8878950def45ccb8 -> 796a6ca50a78d6ec8131f447503f5ea4d54684ede616963b099ee353e559f414
~ _OUTLINED_FUNCTION_5 : sha256 e4ad1860f7b59319b8e50a65d2b36f1eecfaf2d82e08ffa2d789df87d2f88012 -> a915ef4f454db78fcbce36d830137ce33e4884c4e570350dd7f8c6e19a4b5fbb
~ _OUTLINED_FUNCTION_6 : sha256 e4ad1860f7b59319b8e50a65d2b36f1eecfaf2d82e08ffa2d789df87d2f88012 -> a915ef4f454db78fcbce36d830137ce33e4884c4e570350dd7f8c6e19a4b5fbb
~ _OUTLINED_FUNCTION_7 : sha256 b7219142d16979d22a18f24c717e21183b894c984132f6fd8878950def45ccb8 -> 796a6ca50a78d6ec8131f447503f5ea4d54684ede616963b099ee353e559f414
~ _OUTLINED_FUNCTION_8 : sha256 b7219142d16979d22a18f24c717e21183b894c984132f6fd8878950def45ccb8 -> 796a6ca50a78d6ec8131f447503f5ea4d54684ede616963b099ee353e559f414
~ _OUTLINED_FUNCTION_9 : sha256 e4ad1860f7b59319b8e50a65d2b36f1eecfaf2d82e08ffa2d789df87d2f88012 -> a915ef4f454db78fcbce36d830137ce33e4884c4e570350dd7f8c6e19a4b5fbb
~ __ZN6marisa6Keyset16append_key_blockEv : sha256 5d3ed892ec33a56f66495c2a2faa0843c95c2a88bb90c9547ae7c7c3f6e968ce -> d951129d465510e4e3024724648cc78b1ab177283b9dc4e35eb715bb00e671e2
~ __ZN6marisa6Keyset18append_extra_blockEm : sha256 06a491296974d0f8911836c71b38c7642184d3e610cc7cdd25b36bb78ffbe417 -> c62ad75adb6d0546655770959d0f654377131b058c3f3429989eeadd57d9eda9
~ __ZN6marisa6Keyset17append_base_blockEv : sha256 8ae0e7a8330d54a7d64d949861041e410b783fbf08c74c6e731189b3899623f2 -> 37521720448f25ffa313198b72da95aa44615e189b2a50fbfb5b98fc740fa8fa
~ _OUTLINED_FUNCTION_0 : sha256 7ad22fb51a000c95b890448036342592421585810b57348aa54a50767d0beb1d -> 889211a26d50597225023abe7daf6a11a1677c70b4a99de52ea09647d1e62fbf
~ __ZN6marisa4Trie5buildERNS_6KeysetEi : sha256 64126535654a4b619701a246add279f0b104704befd9c036d0b45c2591f16217 -> 596a08b0fc495152116ffbd171816dc2417c74b8306030e70ba4b46676d09942
~ __ZN6marisa4Trie4mmapEPKc : sha256 f362b7df004e67bfd3b802c84bc10aef87c92af0327e585abc4f52ca8eebe4ba -> 70c4c996bb1d03516416243bcb552053c7427b29e4303dc3534a1ccfbf277871
~ __ZN6marisa4Trie3mapEPKvm : sha256 2e098c74d758d840fc02088f2b6c916cf0199e0e3bace8f52826ba53c768bc89 -> f5e3efc8666683c8f37e6590f123302867e9baa67eb641100e2573a78515cfbb
~ __ZN6marisa4Trie4loadEPKc : sha256 d9f3d48de4cce296475ef1efc71c5b2c4d0ad20866041c7aa2437162a70782c5 -> 450d59957aa9ac2b231e11fa5f4b77599611aaee6d65f0077ed4336be452c0ef
~ __ZN6marisa4Trie4readEi : sha256 29f75d8e8b7adff38f00fffb6c6236fe32466a4eecf299a9376407f526e727c9 -> ef37135ec266cf4bffdff0b8ebd6d347c6b2a2ddaaa5a10d12f8f206dd2140cc
~ __ZN6marisa6TrieIO5freadEP7__sFILEPNS_4TrieE : sha256 368021742f1598cbd5e1055b461c67a4fb0fddb2ec59b660d6844baa68d5d592 -> a8a358ed218cbad2c8a442c0a1420d32a78f9e08fefef008c4367d2c986ec08b
~ __ZN6marisa6TrieIO4readERNSt3__113basic_istreamIcNS1_11char_traitsIcEEEEPNS_4TrieE : sha256 8c93d034b654a498e860c2741cd2dbd48c6c1a46634c25c992836e5ad54a5a14 -> fa314402c79da65d1d16e6165aa54b97d7aa6e0f8a2c4703aa9deef3213f2ccc
~ _OUTLINED_FUNCTION_0 : sha256 712ca7ae162914f465dd0792184d4673feef148a0ad73a14de855e98204c2c6a -> 08f1852121d65e327876e235f7a5dccc00f9e13918fca7103e2d4b3a57dd3ce7
~ __ZN6marisa8grimoire2io6Reader4seekEm : sha256 dcd2109dc1658863855a4d2df0313af443e53dcd319f69fa763f1b8213074547 -> f40f5ba9350939ea3f8a0331dbaf4e989729432cc5191e7cd3632fc7742c856c
~ __ZN6marisa8grimoire2io6Reader9read_dataEPvm : sha256 c2a6f4764bb664c3e91719379dac38518e832810fdc60c584e0e04f0f637dfae -> 7e62f01eef667e6cc0dee4a7841f5a90b09147156f3cc6bacac2a2d00fdc3fc7
~ _OUTLINED_FUNCTION_0 : sha256 76d2662f52f3d120b1fd872eb371eafb9642289c33109f81358354c3450c8021 -> 2de81469e22fe07fb8c09f63c9d159479bddfd2a5131e0dbf2b8cd10ec7863e2
~ __ZN6marisa8grimoire4trie4Tail6build_ERNS0_6vector6VectorINS1_5EntryEEEPNS4_IjEE17marisa_tail_mode_ : sha256 9fa6ef8ac361b915df233bbf3fb8c56f714a0d8d5640a9e2b31671cbc33d0cb6 -> 124031017fa5e48b28aad446ef20dfb434589fd163bd70cbb963911799260cac
~ _OUTLINED_FUNCTION_2 : sha256 46c672d4ae20cfdcbac031ecd5938329253f1e7af99ef85dc93f9337ca8e1484 -> 3cc2299e89bba648813131bd155025ca562e4ff27d643eafd305c9fcfc0e1c2c
~ _OUTLINED_FUNCTION_3 : sha256 46c672d4ae20cfdcbac031ecd5938329253f1e7af99ef85dc93f9337ca8e1484 -> 3cc2299e89bba648813131bd155025ca562e4ff27d643eafd305c9fcfc0e1c2c
~ _OUTLINED_FUNCTION_4 : sha256 46c672d4ae20cfdcbac031ecd5938329253f1e7af99ef85dc93f9337ca8e1484 -> 3cc2299e89bba648813131bd155025ca562e4ff27d643eafd305c9fcfc0e1c2c
~ _OUTLINED_FUNCTION_6 : sha256 fe4baf368c5f3c5f97d36e837dd740898ce6f2932edba4f0e24e91495f22e692 -> 6cccbaf3fa4c9e72ffecb4187ddfeb98f1136174a1c4aa653c2831eab345ca70
~ __ZN6marisa8grimoire2io6Writer4seekEm : sha256 b0a7ef70f64dd2ed88925db80b3e0370d0d1b3ae9ee9eb470ee0d5f84275f2c4 -> a1963f8928ed1e580e971a6fc910f4076b9a27fe75ca2eaef55db38445ea685f
~ __ZN6marisa8grimoire2io6Writer10write_dataEPKvm : sha256 f86ad22eb66b6410a5c394a3b30576cd2bb0cfb174df7845be99aa54139cc263 -> d9e499d3f24f3bf0087a9643b35ec4d64a3b4a117ab68d1f7a046c1ecf60b80b
~ _OUTLINED_FUNCTION_0 : sha256 46c672d4ae20cfdcbac031ecd5938329253f1e7af99ef85dc93f9337ca8e1484 -> 3cc2299e89bba648813131bd155025ca562e4ff27d643eafd305c9fcfc0e1c2c
~ __ZN6marisa5Agent10init_stateEv : sha256 6f7df3c7a8a83a2e87ae092c2bd842ee33a0603d684af6fc1ce1a96fcd288a76 -> 3fecb1ab63df031b85f55e609fad2146c184ac5e9881e3be01215145924ed573
~ _OUTLINED_FUNCTION_1 : sha256 9bf2005213103d6da6f5ecfb2197c72856726bd0e108195ec1e29eb9a66b9913 -> 3459c173429e720441611982ba07dc467d8245e2baed1c17a4e84c22c62b33bb
~ _ZN6marisa10scoped_ptrINS_8grimoire4trie9LoudsTrieEE5resetEPS3_.cold.1 : sha256 b955118dcaa5182235415e2cbb32ffdac629b4e61562ad93c73169dfadedff82 -> 446a36134659fe122f54f9471cefd17d29bc2aa2b96bdfa7e624c181c5cc6bfc
~ _ZN6marisa8grimoire6vector6VectorIjE6shrinkEv.cold.1 : sha256 65ced7f8181de031ae1b9624f7c33c58d3ddaf7ca1ee11982b4e651c74094502 -> f81aa89cbf599a575e676207a8e64847fe28f3304dc8ffe8638f4fe8f0bbefc7
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/include/marisa/scoped-ptr.h"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/include/marisa/scoped-ptr.h:19: MARISA_RESET_ERROR: (ptr != NULL) && (ptr == ptr_)"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/agent.cc"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/agent.cc:13: MARISA_NULL_ERROR: str == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/agent.cc:21: MARISA_NULL_ERROR: (ptr == NULL) && (length != 0)"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/agent.cc:36: MARISA_STATE_ERROR: state_.get() != NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/agent.cc:38: MARISA_MEMORY_ERROR: state_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:100: MARISA_IO_ERROR: size > avail_"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:141: MARISA_IO_ERROR: ::stat(filename, &st) != 0"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:146: MARISA_IO_ERROR: fd_ == -1"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:149: MARISA_IO_ERROR: origin_ == MAP_FAILED"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:55: MARISA_NULL_ERROR: filename == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:63: MARISA_NULL_ERROR: (ptr == NULL) && (size != 0)"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:71: MARISA_STATE_ERROR: !is_open()"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:72: MARISA_IO_ERROR: size > avail_"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:99: MARISA_STATE_ERROR: !is_open()"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/reader.cc"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/reader.cc:113: MARISA_STATE_ERROR: !is_open()"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/reader.cc:129: MARISA_IO_ERROR: size_read <= 0"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/reader.cc:134: MARISA_IO_ERROR: ::fread(buf, 1, size, file_) != size"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/reader.cc:138: MARISA_IO_ERROR: !stream_->read(static_cast<char *>(buf), size)"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/reader.cc:140: MARISA_IO_ERROR: std::ios_base::failure"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/reader.cc:27: MARISA_NULL_ERROR: filename == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/reader.cc:35: MARISA_NULL_ERROR: file == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/reader.cc:43: MARISA_CODE_ERROR: fd == -1"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/reader.cc:68: MARISA_STATE_ERROR: !is_open()"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/reader.cc:94: MARISA_IO_ERROR: file == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/writer.cc"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:113: MARISA_STATE_ERROR: !is_open()"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:129: MARISA_IO_ERROR: size_written <= 0"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:134: MARISA_IO_ERROR: ::fwrite(data, 1, size, file_) != size"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:135: MARISA_IO_ERROR: ::fflush(file_) != 0"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:139: MARISA_IO_ERROR: !stream_->write(static_cast<const char *>(data), size)"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:141: MARISA_IO_ERROR: std::ios_base::failure"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:27: MARISA_NULL_ERROR: filename == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:35: MARISA_NULL_ERROR: file == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:43: MARISA_CODE_ERROR: fd == -1"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:68: MARISA_STATE_ERROR: !is_open()"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:94: MARISA_IO_ERROR: file == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../io/mapper.h"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../io/mapper.h:28: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../io/mapper.h:30: MARISA_SIZE_ERROR: num_objs > (MARISA_SIZE_MAX / sizeof(T))"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../io/reader.h"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../io/reader.h:31: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../io/reader.h:33: MARISA_SIZE_ERROR: num_objs > (MARISA_SIZE_MAX / sizeof(T))"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../io/writer.h"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../io/writer.h:30: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../io/writer.h:32: MARISA_SIZE_ERROR: num_objs > (MARISA_SIZE_MAX / sizeof(T))"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../vector/../io/mapper.h"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../vector/../io/mapper.h:28: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../vector/../io/mapper.h:30: MARISA_SIZE_ERROR: num_objs > (MARISA_SIZE_MAX / sizeof(T))"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../vector/../io/reader.h"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../vector/../io/reader.h:31: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../vector/../io/reader.h:33: MARISA_SIZE_ERROR: num_objs > (MARISA_SIZE_MAX / sizeof(T))"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../vector/../io/writer.h"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../vector/../io/writer.h:30: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../vector/../io/writer.h:32: MARISA_SIZE_ERROR: num_objs > (MARISA_SIZE_MAX / sizeof(T))"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../vector/bit-vector.h"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../vector/bit-vector.h:135: MARISA_FORMAT_ERROR: temp_num_1s > size_"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../vector/bit-vector.h:153: MARISA_FORMAT_ERROR: temp_num_1s > size_"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../vector/bit-vector.h:52: MARISA_SIZE_ERROR: size_ == MARISA_UINT32_MAX"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../vector/flat-vector.h"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../vector/flat-vector.h:134: MARISA_FORMAT_ERROR: temp_value_size > 32"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../vector/flat-vector.h:155: MARISA_FORMAT_ERROR: temp_value_size > 32"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h:100: MARISA_STATE_ERROR: fixed_"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h:107: MARISA_STATE_ERROR: fixed_"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h:202: MARISA_FORMAT_ERROR: (total_size % sizeof(T)) != 0"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h:213: MARISA_FORMAT_ERROR: (total_size % sizeof(T)) != 0"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/config.h"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/config.h:101: MARISA_CODE_ERROR: undefined cache level"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/config.h:121: MARISA_CODE_ERROR: undefined tail mode"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/config.h:141: MARISA_CODE_ERROR: undefined node order"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/config.h:59: MARISA_CODE_ERROR: (config_flags & ~MARISA_CONFIG_MASK) != 0"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/header.h"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/header.h:21: MARISA_FORMAT_ERROR: !test_header(ptr)"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/header.h:26: MARISA_FORMAT_ERROR: !test_header(buf)"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:428: MARISA_MEMORY_ERROR: std::bad_alloc"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:451: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:468: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:542: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:568: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:73: MARISA_BOUND_ERROR: agent.query().id() >= size()"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:13: MARISA_NULL_ERROR: offsets == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:170: MARISA_RANGE_ERROR: current.length() == 0"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:192: MARISA_SIZE_ERROR: buf_.size() > MARISA_UINT32_MAX"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:36: MARISA_CODE_ERROR: undefined tail mode"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/vector/vector.h"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/grimoire/vector/vector.h:100: MARISA_STATE_ERROR: fixed_"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/keyset.cc"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/keyset.cc:129: MARISA_MEMORY_ERROR: new_blocks.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/keyset.cc:138: MARISA_MEMORY_ERROR: new_block.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/keyset.cc:151: MARISA_MEMORY_ERROR: new_blocks.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/keyset.cc:159: MARISA_MEMORY_ERROR: new_block.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/keyset.cc:169: MARISA_MEMORY_ERROR: new_blocks.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/keyset.cc:177: MARISA_MEMORY_ERROR: new_block.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/keyset.cc:50: MARISA_NULL_ERROR: str == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/keyset.cc:61: MARISA_NULL_ERROR: (ptr == NULL) && (length != 0)"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/keyset.cc:62: MARISA_SIZE_ERROR: length > MARISA_UINT32_MAX"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:134: MARISA_STATE_ERROR: trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:139: MARISA_STATE_ERROR: trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:14: MARISA_MEMORY_ERROR: temp.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:180: MARISA_NULL_ERROR: trie == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:184: MARISA_MEMORY_ERROR: temp.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:192: MARISA_NULL_ERROR: file == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:193: MARISA_STATE_ERROR: trie.trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:200: MARISA_NULL_ERROR: trie == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:204: MARISA_MEMORY_ERROR: temp.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:213: MARISA_STATE_ERROR: trie.trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:21: MARISA_NULL_ERROR: filename == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:222: MARISA_NULL_ERROR: file == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:223: MARISA_NULL_ERROR: trie == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:228: MARISA_NULL_ERROR: file == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:233: MARISA_NULL_ERROR: trie == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:24: MARISA_MEMORY_ERROR: temp.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:33: MARISA_NULL_ERROR: (ptr == NULL) && (size != 0)"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:36: MARISA_MEMORY_ERROR: temp.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:45: MARISA_NULL_ERROR: filename == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:48: MARISA_MEMORY_ERROR: temp.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:57: MARISA_CODE_ERROR: fd == -1"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:60: MARISA_MEMORY_ERROR: temp.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:69: MARISA_STATE_ERROR: trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:70: MARISA_NULL_ERROR: filename == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:78: MARISA_STATE_ERROR: trie_.get() == NULL"
+ "/AppleInternal/Library/BuildRoots/4~CR_4ugD_Xct9qS-YkKEdyVAHn8WvhtyXGvjLTV4/Library/Caches/com.apple.xbs/TemporaryDirectory.NRWwWS/Sources/Marisa/lib/marisa/trie.cc:79: MARISA_CODE_ERROR: fd == -1"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/include/marisa/scoped-ptr.h"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/include/marisa/scoped-ptr.h:19: MARISA_RESET_ERROR: (ptr != NULL) && (ptr == ptr_)"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/agent.cc"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/agent.cc:13: MARISA_NULL_ERROR: str == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/agent.cc:21: MARISA_NULL_ERROR: (ptr == NULL) && (length != 0)"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/agent.cc:36: MARISA_STATE_ERROR: state_.get() != NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/agent.cc:38: MARISA_MEMORY_ERROR: state_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:100: MARISA_IO_ERROR: size > avail_"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:141: MARISA_IO_ERROR: ::stat(filename, &st) != 0"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:146: MARISA_IO_ERROR: fd_ == -1"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:149: MARISA_IO_ERROR: origin_ == MAP_FAILED"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:55: MARISA_NULL_ERROR: filename == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:63: MARISA_NULL_ERROR: (ptr == NULL) && (size != 0)"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:71: MARISA_STATE_ERROR: !is_open()"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:72: MARISA_IO_ERROR: size > avail_"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/mapper.cc:99: MARISA_STATE_ERROR: !is_open()"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/reader.cc"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/reader.cc:113: MARISA_STATE_ERROR: !is_open()"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/reader.cc:129: MARISA_IO_ERROR: size_read <= 0"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/reader.cc:134: MARISA_IO_ERROR: ::fread(buf, 1, size, file_) != size"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/reader.cc:138: MARISA_IO_ERROR: !stream_->read(static_cast<char *>(buf), size)"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/reader.cc:140: MARISA_IO_ERROR: std::ios_base::failure"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/reader.cc:27: MARISA_NULL_ERROR: filename == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/reader.cc:35: MARISA_NULL_ERROR: file == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/reader.cc:43: MARISA_CODE_ERROR: fd == -1"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/reader.cc:68: MARISA_STATE_ERROR: !is_open()"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/reader.cc:94: MARISA_IO_ERROR: file == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/writer.cc"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:113: MARISA_STATE_ERROR: !is_open()"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:129: MARISA_IO_ERROR: size_written <= 0"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:134: MARISA_IO_ERROR: ::fwrite(data, 1, size, file_) != size"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:135: MARISA_IO_ERROR: ::fflush(file_) != 0"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:139: MARISA_IO_ERROR: !stream_->write(static_cast<const char *>(data), size)"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:141: MARISA_IO_ERROR: std::ios_base::failure"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:27: MARISA_NULL_ERROR: filename == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:35: MARISA_NULL_ERROR: file == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:43: MARISA_CODE_ERROR: fd == -1"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:68: MARISA_STATE_ERROR: !is_open()"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/io/writer.cc:94: MARISA_IO_ERROR: file == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../io/mapper.h"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../io/mapper.h:28: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../io/mapper.h:30: MARISA_SIZE_ERROR: num_objs > (MARISA_SIZE_MAX / sizeof(T))"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../io/reader.h"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../io/reader.h:31: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../io/reader.h:33: MARISA_SIZE_ERROR: num_objs > (MARISA_SIZE_MAX / sizeof(T))"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../io/writer.h"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../io/writer.h:30: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../io/writer.h:32: MARISA_SIZE_ERROR: num_objs > (MARISA_SIZE_MAX / sizeof(T))"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../vector/../io/mapper.h"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../vector/../io/mapper.h:28: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../vector/../io/mapper.h:30: MARISA_SIZE_ERROR: num_objs > (MARISA_SIZE_MAX / sizeof(T))"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../vector/../io/reader.h"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../vector/../io/reader.h:31: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../vector/../io/reader.h:33: MARISA_SIZE_ERROR: num_objs > (MARISA_SIZE_MAX / sizeof(T))"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../vector/../io/writer.h"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../vector/../io/writer.h:30: MARISA_NULL_ERROR: (objs == NULL) && (num_objs != 0)"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../vector/../io/writer.h:32: MARISA_SIZE_ERROR: num_objs > (MARISA_SIZE_MAX / sizeof(T))"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../vector/bit-vector.h"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../vector/bit-vector.h:135: MARISA_FORMAT_ERROR: temp_num_1s > size_"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../vector/bit-vector.h:153: MARISA_FORMAT_ERROR: temp_num_1s > size_"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../vector/bit-vector.h:52: MARISA_SIZE_ERROR: size_ == MARISA_UINT32_MAX"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../vector/flat-vector.h"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../vector/flat-vector.h:134: MARISA_FORMAT_ERROR: temp_value_size > 32"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../vector/flat-vector.h:155: MARISA_FORMAT_ERROR: temp_value_size > 32"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h:100: MARISA_STATE_ERROR: fixed_"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h:107: MARISA_STATE_ERROR: fixed_"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h:202: MARISA_FORMAT_ERROR: (total_size % sizeof(T)) != 0"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/../vector/vector.h:213: MARISA_FORMAT_ERROR: (total_size % sizeof(T)) != 0"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/config.h"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/config.h:101: MARISA_CODE_ERROR: undefined cache level"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/config.h:121: MARISA_CODE_ERROR: undefined tail mode"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/config.h:141: MARISA_CODE_ERROR: undefined node order"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/config.h:59: MARISA_CODE_ERROR: (config_flags & ~MARISA_CONFIG_MASK) != 0"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/header.h"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/header.h:21: MARISA_FORMAT_ERROR: !test_header(ptr)"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/header.h:26: MARISA_FORMAT_ERROR: !test_header(buf)"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:428: MARISA_MEMORY_ERROR: std::bad_alloc"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:451: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:468: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:542: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:568: MARISA_MEMORY_ERROR: next_trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/louds-trie.cc:73: MARISA_BOUND_ERROR: agent.query().id() >= size()"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:13: MARISA_NULL_ERROR: offsets == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:170: MARISA_RANGE_ERROR: current.length() == 0"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:192: MARISA_SIZE_ERROR: buf_.size() > MARISA_UINT32_MAX"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/trie/tail.cc:36: MARISA_CODE_ERROR: undefined tail mode"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/vector/vector.h"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/grimoire/vector/vector.h:100: MARISA_STATE_ERROR: fixed_"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/keyset.cc"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/keyset.cc:129: MARISA_MEMORY_ERROR: new_blocks.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/keyset.cc:138: MARISA_MEMORY_ERROR: new_block.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/keyset.cc:151: MARISA_MEMORY_ERROR: new_blocks.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/keyset.cc:159: MARISA_MEMORY_ERROR: new_block.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/keyset.cc:169: MARISA_MEMORY_ERROR: new_blocks.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/keyset.cc:177: MARISA_MEMORY_ERROR: new_block.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/keyset.cc:50: MARISA_NULL_ERROR: str == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/keyset.cc:61: MARISA_NULL_ERROR: (ptr == NULL) && (length != 0)"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/keyset.cc:62: MARISA_SIZE_ERROR: length > MARISA_UINT32_MAX"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:134: MARISA_STATE_ERROR: trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:139: MARISA_STATE_ERROR: trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:14: MARISA_MEMORY_ERROR: temp.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:180: MARISA_NULL_ERROR: trie == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:184: MARISA_MEMORY_ERROR: temp.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:192: MARISA_NULL_ERROR: file == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:193: MARISA_STATE_ERROR: trie.trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:200: MARISA_NULL_ERROR: trie == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:204: MARISA_MEMORY_ERROR: temp.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:213: MARISA_STATE_ERROR: trie.trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:21: MARISA_NULL_ERROR: filename == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:222: MARISA_NULL_ERROR: file == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:223: MARISA_NULL_ERROR: trie == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:228: MARISA_NULL_ERROR: file == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:233: MARISA_NULL_ERROR: trie == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:24: MARISA_MEMORY_ERROR: temp.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:33: MARISA_NULL_ERROR: (ptr == NULL) && (size != 0)"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:36: MARISA_MEMORY_ERROR: temp.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:45: MARISA_NULL_ERROR: filename == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:48: MARISA_MEMORY_ERROR: temp.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:57: MARISA_CODE_ERROR: fd == -1"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:60: MARISA_MEMORY_ERROR: temp.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:69: MARISA_STATE_ERROR: trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:70: MARISA_NULL_ERROR: filename == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:78: MARISA_STATE_ERROR: trie_.get() == NULL"
- "/AppleInternal/Library/BuildRoots/4~CQ4iugCjYyV6DYpgcASxkql0ILbW-zvvdN8m4mA/Library/Caches/com.apple.xbs/TemporaryDirectory.gMbyqn/Sources/Marisa/lib/marisa/trie.cc:79: MARISA_CODE_ERROR: fd == -1"

```
