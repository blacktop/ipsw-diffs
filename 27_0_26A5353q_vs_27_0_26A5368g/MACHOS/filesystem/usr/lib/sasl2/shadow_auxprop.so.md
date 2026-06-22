## shadow_auxprop.so

> `/usr/lib/sasl2/shadow_auxprop.so`

```diff

 195.0.0.0.0
-  __TEXT.__text: 0x1ed0 sha256:b9dee94004dcde39b7d364f7c6568eeed1afec288c63f2406098e17b1756b770
+  __TEXT.__text: 0x1ee8 sha256:ec1ee4367ecc7438ee024c547b381bfb4241c4aeee8c51f18a0ba572de32e0c4
   __TEXT.__auth_stubs: 0x2c0 sha256:79fc051cfcea56348ac6cfe8287884ea05a223ec6acf75cf3decd1e17d3770f4
-  __TEXT.__cstring: 0x52b sha256:626eb454e0f073e4a41d3f01744914db4590351f300709a65169946e20581b40
-  __TEXT.__unwind_info: 0xb8 sha256:b1abe3724f3c5a7f12a38ffb778561e9b8160b87724de63582b356b614242af5
-  __DATA_CONST.__const: 0x70 sha256:473a3c9f911929657690cb0dab6057db0437cadf37b7c71bafc90ebdb5e015aa
+  __TEXT.__cstring: 0x52b sha256:86a247c8413b1de0a9505e134d3c5b134989b252cbe49219454bf7d6f900066a
+  __TEXT.__unwind_info: 0xb8 sha256:2cb26b5860e065ea5fd2f42f668debaa5f470b56cb49ac38028e6892c7cca466
+  __DATA_CONST.__const: 0x70 sha256:86ed4fff2c0c177d8fb208631b4628c87c49fe210e30aa0537ade6a7f374b841
   __DATA_CONST.__auth_got: 0x160 sha256:bfa106d8edc5d7ea94383b90e52ad004d98bb4b80609808dd1d09e6fa882e2bd
   __DATA_CONST.__got: 0x8 sha256:f3199712f83d6eb7760d9e2f386bb9880caf14cddfe4f156a2fcece741e85705
   __DATA_CONST.__auth_ptr: 0x8 sha256:1c19ed81af03cadb5e4c42f613fb11eab92f53f7575a3d332a684a2169f3802b
   __DATA.__data: 0x30 sha256:c498598dcf1ce535a337efa2b0b54383b8a700cd59167edf6de26b32f3cb784d
   - /System/Library/Frameworks/DirectoryService.framework/Versions/A/DirectoryService
   - /usr/lib/libSystem.B.dylib
-  UUID: 57FEF5CB-2054-3D4A-949D-130DCA0A12EF
+  UUID: EA439B58-D1EE-36CE-911E-7110903DF90A
   Functions: 26
   Symbols:   74
   CStrings:  25
Functions:
~ _ConvertHexToBinary : 112 -> 108
~ _OpenRecord : sha256 40fc86887455efe4b34cb7e865cd557cc7f7c61817455d9846fcdee3ad6ba585 -> 6187caa785fd9dca4de21d3cdf35f80861a13d37d5bbdd7dc4ba3c91f7ddfcab
~ _get_guid_for_username : sha256 61df3c3a719e0ac02d566fc5e77acae9ba90c307be33c2faa646388bd768220b -> b9145124ccccd8015079c451a2b5fdd4fae84a3935534619beff81fef4034bd5
~ _get_node_for_username : sha256 95e08f9d571e95332e04b59fb38377d88e0dbfd0efbc4aabd73d8e1bee938b1f -> cb36175150605bd1d4b75e4951e7a24417f42a8514824ada9103e5a72a314f61
~ _get_prop_id : 124 -> 128
~ _shadow_getdata : sha256 0f1a260d680ed89d147c4ddf6e08f3f57aed900b53d113355d6d6f008b58f6e0 -> 6725229230eca47a52539dfd52cae9e6aa56f2fd1edf48ce373952ac7f379fcc
~ _shadow_readfile : sha256 3aedd431e26f91ea0302924919c3f849ebcda1459d394f056bac1d444476549b -> a9c336624c38d28d07fb9a7723d4111f89fa53529da85abda909dd4d86fbf0a1
~ _shadow_auxprop_lookup : 804 -> 800
~ __plug_ipfromstring : 572 -> 568
~ __plug_iovec_to_buf : 340 -> 364
~ __plug_buf_alloc : sha256 83481d6d59eb8a86b756e541867ab1682cb6e2c12b1f18995485b6fffc428e5d -> 14584f1318780b0659a7387c2daa36fc74886322d00785b22d73cddacd65bd38
~ __plug_strdup : sha256 a3f9d2e382694ffed9176c8462ce58c36e8389e5defe6aa2cc0c8a02eec0d931 -> bd593fb5977944c23a35b7b610479c614797ae34b411351b4ab09c5afaca7efa
~ __plug_free_string : sha256 c89f43f6f22b154050e973e5229f42b4764dd531ba7efbabc175bb96eb3120b4 -> e4f428a61b2a19be9d2469a84aab4070fff5a62a546f4911db7cb21473419ed1
~ __plug_find_prompt : 48 -> 64
~ __plug_get_simple : sha256 6b80d57455c99e5c3dc7ca8136cfc09246cf13998d78c4ed20eb9e7bdd78f2e0 -> 13e0e7e43d381f72372bf09ee715ea73dae9559836c325eb39166383349b2ff2
~ __plug_get_password : 368 -> 360
~ __plug_challenge_prompt : sha256 c9903a975370ad94204fdb829bf5b18c8fbdad1d2a248d1868bdda35181f27bd -> 5036e387cf43b02b664f473b9a5e7fecc633653914d1582830ae6b0eeec53212
~ __plug_get_realm : sha256 cf3203a402b56295660c2c9f42f0c9871cc1b3c09562315db0344423a220507a -> 0f34deddfd56782a530ec868489c0cd691f7a2a7b9c97e1bfd7d5ea244e46249
~ __plug_make_prompts : sha256 b5c492d5271574a3d25f063894403d0a0f50079fc2df7a31994f91872b3ab133 -> 23dd2118b3de14ea44df6cb12e891aaab241096ca5fd2ba1321dba19e74e7eea
~ __plug_decode : sha256 e916c5b7b3b69847730d40724e0fa26d9e0fd7bf65fad45b453bd1e505283d0e -> 072f0220df1750a92cf6a53e37e8f96206c803ddcc81a3b28a53440ae7bc5daa
~ __plug_parseuser : sha256 78d631f9982862c8db1964ccb7c83948dfde32cf952f7b7bcd155127450faef9 -> d903d1d5ae7539422e3007c5ee2702d2880d2f1fd096ef706ae1c1effa167526
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/shadow_auxprop.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRbjugCRhMFFzaInYXomKBTrZdlRzjmybz6OP28/Library/Caches/com.apple.xbs/TemporaryDirectory.Q9P69u/Sources/passwordserver_saslplugins/shadow_auxprop.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/shadow_auxprop.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQCNugC_21xWLnVaKf3I5DKm4S9h3s8tdXTWZgQ/Library/Caches/com.apple.xbs/TemporaryDirectory.00Mar5/Sources/passwordserver_saslplugins/shadow_auxprop.c near line %d"

```
