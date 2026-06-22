## srp.so

> `/usr/lib/sasl2/srp.so`

```diff

-215.0.0.0.0
-  __TEXT.__text: 0x49a8 sha256:4d25de09e1557d7a3e2e10112a7fd2fe4a1dd1908566ef374c8a96a545706a86
+217.0.0.0.0
+  __TEXT.__text: 0x4a88 sha256:21f22ffe930a39d275ce0389a57f8325ac1e0ab81a654893637c027e3737c655
   __TEXT.__auth_stubs: 0x4d0 sha256:711105344646134d08bed4160586aefd91cca249a7e105eb90958725af2b4a10
-  __TEXT.__cstring: 0x12d8 sha256:e7f51244433f238f643dc2401680028809df126549de85d76f9a3443eefa49c6
+  __TEXT.__cstring: 0x12d8 sha256:481562d51df204e135bb5613a725bf96b6fa962b23082afa39a32a0cfdd501ee
   __TEXT.__const: 0x602 sha256:38693ff29c82c8d68cfadfd13dce066733affcc461cc9c845198a95c01ea7c73
-  __TEXT.__unwind_info: 0x108 sha256:cdd92bd97ab8ff1cac23ca55e6a9d82fabb31355589b7de5dc5cdd4fbe9e94ed
-  __DATA_CONST.__const: 0x18 sha256:fd777c3b7665b99fdc0293d21063b791bafe0c749f7bd355b538e11bc6c42871
-  __DATA_CONST.__cfstring: 0x60 sha256:eb294bb6d391b12ae90a39d8ff80ad79947abed4e81c71ac70d0ef7bf5f5e229
+  __TEXT.__unwind_info: 0x110 sha256:cd0e90187ff7be00fa92ac3a5dc769bf63da0c8fe6f167c39da53d2950f0a57c
+  __DATA_CONST.__const: 0x18 sha256:5c2e3e3cb12ff1d4794e0ef585aabe32f32cefcb09dbc2b209b349f4b5e70ccd
+  __DATA_CONST.__cfstring: 0x60 sha256:2e4e4fb7f0fc8785be9eb8fa9fb88338de556a78d88f02c4fc50bc0bfc18c72d
   __DATA_CONST.__auth_got: 0x268 sha256:bc5a5298a786f9e5b08a12c053a3a100394437bd5bede18f121a45dffa5d8df8
   __DATA_CONST.__got: 0x28 sha256:367d56fce8a0ca844815abd0831ee2ff1b29e5e3d48617056dab35d484c68512
-  __DATA.__data: 0x228 sha256:8174d0bcc6974a10a2294f24b5795c6d735310db968ee8a726988b7c7f7d8e75
+  __DATA.__data: 0x228 sha256:a17655588fb49baf06bb1123f1a54a241ef974ebc808ccc870265eb2191ee208
   __DATA.__bss: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
   - /usr/lib/libSystem.B.dylib
-  UUID: D895340C-E1D8-384D-9F6B-E2A666852E19
+  UUID: C7AAAB7D-3459-3659-935E-974664A0EED1
   Functions: 47
   Symbols:   137
   CStrings:  131
Functions:
~ __plug_ipfromstring : 572 -> 568
~ __plug_iovec_to_buf : 340 -> 364
~ __plug_buf_alloc : sha256 4d0a724fa7332f3ba7f951ce1b300c98d2e84af00bdad5c34c39be50958c6fab -> f64b5071e10c1210c47abe7bb8dc8425127ca8572cb366f64bac522e85fbce9c
~ __plug_strdup : sha256 d9ea93f4c66f83fe62fd82ac877c18310c210b75c7965722ab20201d64ed8b36 -> 598325e88261355869457de1ba254ea254c7398a9e7fcb3c02725fe305d77f4c
~ __plug_free_string : sha256 be4efc0b48241e95b7f3f716c194932bcf888983322160b8ca8f9477b77095c3 -> bf80d2afa5aeaf07f99a0f263320683ed6b9e9bdefc05b1b3e9073d4e29dc05c
~ __plug_find_prompt : 48 -> 64
~ __plug_get_simple : sha256 7e8c672c3cac3df0277595def3ff64aa3765c9b84e49c29ce67e0bdda3ce58be -> 89f0d734b1c520f83de03a667ce6eeb81e059eef675d7ac71fed58b57c4ec5b8
~ __plug_get_password : 372 -> 364
~ __plug_challenge_prompt : sha256 eedd1d3f3cc133da2aa2e2fb8cde6e026a790d11895f93a893e2bb75a4625713 -> af7d4b242675a011d93adde7dd83e0ef0b6b12be95a144128f435d5fa707b331
~ __plug_get_realm : sha256 436f28d120bd220f747a5c8526aaf57a5271f6ad29a7caba992a76cbe7c00021 -> 21585eaef0486df91c6e1c5b03a7d900e52e60d14bb6a034263999f0b2ecdf80
~ __plug_make_prompts : sha256 74eca3a1936dffe4a09adaac39c0e1fc96ccf7adecf4e86205e1269b235c8b62 -> fdce66b8bb23209d4a5e5050b89d2504fbd442ac7048b5e0c7475ad031b38b77
~ __plug_decode : sha256 ccf7cf0632bbbf0081c190e07123ac59ea39bfcaae91828dab9a3802b588afd4 -> 114632e033079657df5b951f1dd6c4ac7ed771d8d33e8f6bfc760d101ba17aee
~ __plug_parseuser : sha256 21f8fcf26f126dd8e8b1ac3818a4ca915403e8598886e7a4e68cb484a990ae80 -> f79f7c682a64497f4e7a960e905d0052d4beb9311f71dd32384a90c9e7cb142c
~ __plug_make_fulluser : sha256 c0d14f427c5e8db1402bc9f26a5a8708bd7a3e09484ac2b405abe092ef2fb151 -> 07fbf67b64005fb5b4d9f4d35a04a88d94b00a943c5e8d3f14c62109a1eee82e
~ __plug_get_error_message : sha256 4924c0955d078d28f7c9eaaa5d090b6901fdd9d9b31ee838ec9d18d54a898e90 -> 340785e5538402d7c66719890374466ab87544c32dbe42aca9f18085b5221d2e
~ __plug_snprintf_os_info : sha256 9e788852119e14f19071ccac5566ccdc99bdc1dc18f86c8ff84fe23d079e8893 -> fb59dffd8e7e029dd0e233d6d5de59032bd85f28ef250c740512bbfa96cb5bdd
~ _srp_server_plug_init : 432 -> 444
~ _cc_get_digestbyname : sha256 789e4831b706ffe9614de6a7651cfb43d10066a1e7a261f9f8864893041b83f7 -> 72dabfb5ac3220427dba1843ad2534815b7fdb3512a0227efc755a84bb478ffb
~ _srp_client_plug_init : 252 -> 248
~ _srp_server_mech_new : sha256 340fd01f49e570ff90f7b9d6d193fb84311a8689af924c8f9facf4c89c9c608a -> 0484e12c7bf33f3a2875fb98075bf491fc66734d6e822de00798e5d4817099e6
~ _srp_server_mech_step : sha256 3cb02e7fa3aa7f9852b7868910aefad5f9a11005b8da688e8a4620d65c2f55be -> 11a9d27c6d90cbebc2df91d6706bc28ab288ed2756015612b2cf3c1471be4bcb
~ _srp_common_mech_dispose : sha256 47a4becad08a0f3c1972e2d91a0dc0b4ac735d6f2cb6ddfc982a55addd846d03 -> 69d8b6c686a8687ff80737a65943955d8f2f22309989d3c0cce1871f8c8c7491
~ _srp_mech_avail : sha256 16c40ff1aaacc5c64887d0f6e072e8d8822b1780a1313f45a5f6ac162e2a4f37 -> ed6d53bb831d7a8eae1b6201889a0fc4226e5beb9827b3a11fb9d0cb880f6683
~ _srp_common_context_init : sha256 a8e6e62e5c979d78e500f6ca72400ec46fbb6049a7431d57d42ed14e85468378 -> 5116a7a0b943353d170460dc99673cce8bda350612ef82934351da87dec96a43
~ _UnBuffer : sha256 ea86ae3ee517e392a2c6dc7d3fff276d84c00d045b6dc52e47d7ca608e3c38ed -> be573d9de754d5caaa38349cc83c614dae947117125e740174619ef2e8318fc4
~ _srp_load_authdata_dict : sha256 4b707f90e49b15cc486013a44a14d125b17f49dd09d2546e5ece7011c9fe5bb3 -> 4999f2e3c7861f6382c4f8bd3b6378f76e5e5d9383734baa3ec0915047dbc3cd
~ _srp_generate_authdata_dict : 736 -> 764
~ _CreateServerOptions : 320 -> 312
~ _MakeBuffer : 896 -> 908
~ _generate_N_and_g : 160 -> 196
~ _set_ccsrp_groups : sha256 4888bb887074b953002b8de1fa3850942c927d8854c299da006ffabc55a3bc9a -> 9bac709f031d6c341216a67c2a58f9d36ba2c5c395dbf632049afcc3e7b6ef1c
~ _OptionsToString : 1028 -> 1052
~ _ParseOptions : 1124 -> 1128
~ _SetMDA : 136 -> 132
~ _LayerInit : 524 -> 520
~ _srp_encode : 420 -> 440
~ _srp_decode : sha256 0d12b97c321e3899cb988266a8fc7528633000e2b2bf1279a535e739031dc612 -> b0184204f4a0b5edd12ffc68e9d7ecb1f28c129cfc233e09d9b8e51185e49e0b
~ _srp_decode_packet : sha256 3e1b782b9f3c065b2785c3f94910212002e1ca088270a8e84dbd32debf47e166 -> 9ebec1b2cc9c242899c6f8a1dd79c55832046ebb52c623513e066aac6f109c06
~ _srp_client_mech_new : sha256 65d2677a9ab1aed78ae1886ead4a05fe14cb654e3ecace15d169aee545aa026e -> 1495b55f345eb2ebf7063c382048fbbfaec7aa79bece1cccb58c5f00ff345eda
~ _srp_client_mech_step : 2332 -> 2404
~ _CreateClientOpts : 436 -> 444
~ _sasl_client_plug_init : sha256 d882a8b35a7251087d07b0d77e62247d19f06e2c07c5fe449db3a3dfaf417c22 -> dd7ff3ee89abb6662df13771d00f4d5f645f352db7693d4f9409213b8c6618fd
~ _sasl_server_plug_init : sha256 714cb1fbe4e1228d49d4ae182840a79de2dfc27756d68532de795c8d64d12600 -> e8789476696963ba5b7f982b484ecb08e7f100cf7dd26c472c11ab50e55e430f
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/srp.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/srp.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/srp.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/srp.c near line %d"

```
