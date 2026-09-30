## libanonymous.2.so

> `/usr/lib/sasl2/libanonymous.2.so`

```diff

-215.0.0.0.0
-  __TEXT.__text: 0x18e4 sha256:8a52d14cf21c78edb081c6711927b06141bf424baf813d4a0e009d9ffd7f8a8d
+217.0.0.0.0
+  __TEXT.__text: 0x1900 sha256:e287afd6c2729db5806c71fe98371d7d30a8e610623d5ad4f3a82c7eb5faf281
   __TEXT.__auth_stubs: 0xf0 sha256:307b218808fb5afc8dad15aa958d2ae1995b85dddd3efc0c803c58c32acdc2d0
-  __TEXT.__cstring: 0x4dd sha256:e017114784b2896db659f2eef2da413b702085098e8215f4be9bbe4641af154a
+  __TEXT.__cstring: 0x4dd sha256:3227b415133935e2d0d257d989726f67e3c044109bb3e83e8d25f3d90df4e5be
   __TEXT.__const: 0x18 sha256:eeaa6ffb52a871778b1f7ee11fc05a89617005d5643d88482f81896da29a0332
-  __TEXT.__unwind_info: 0xc0 sha256:791169c2504f1537c0ee0c79a43a2e5350a728a47f8316f1a14e0a3c199b6621
+  __TEXT.__unwind_info: 0xc0 sha256:17b659c57f4496dd4a4166fa9d483a29cc73910fa036230599b85c877fb937e7
   __DATA_CONST.__auth_got: 0x78 sha256:38c345cb9cf8745099627a43c391a1581c0c6e90e4af5679a2e9737df975dec9
   __DATA_CONST.__got: 0x8 sha256:342c14f50cc87ae753fbb43ed5599d9575578190e65d4f72909a50c20c019698
-  __DATA.__data: 0xc8 sha256:6646a29b453b259f3714b686d10ec9913b89754778465ef079520e8e532cde1d
+  __DATA.__data: 0xc8 sha256:26921a876e4df6c7d5d08ddc8deb57719febd0902b8f83e4290c78b99a13202b
   - /usr/lib/libSystem.B.dylib
-  UUID: 832D62D3-26B3-3388-BDD5-A007248E360B
+  UUID: E378CFD1-B5A7-3F3A-A432-92832EE8CF61
   Functions: 28
   Symbols:   48
   CStrings:  17
Functions:
~ _anonymous_server_plug_init : sha256 805c03b20104da0058bbd3f838f81a61c7418fa1018429ce5bd89e3d1e39ffdd -> 0bbf0dc688a2e39a80740b5977b0ec57f5ff5e3ba92f66aba6a8e65a51612988
~ _anonymous_client_plug_init : sha256 133a7c5626c8ecfc14d5a05e5193ffa497108f2b825f1c47dde4b43e6c75d47d -> 93aae903960450e46c1a2b476c86df8b648cc17951c1d1afe66e391a10f52710
~ _anonymous_server_mech_new : sha256 903c0df45e82682b3954cb24da06a0eb89162f0bc6ec50d693cc687611449cab -> 2e6a14f968d422872ab66c0f9928bb8929eb5975225dcade41fcb1628059b186
~ _anonymous_server_mech_step : sha256 53fd3716f6f79acdbc2f94973c1329f7c60c1d3a93ec9b47a25c67b916b88544 -> 5f1001606985a287840319a92f119c34c30c2b39a6e500570d478d9e31f24a7f
~ _anonymous_client_mech_new : sha256 3df2ced81a14aceda064e6ab5459023d3c5ed996f10c3ecee3eeca8754da706c -> e724b583e9076a2a77ff8a0378ea6c8d07b6908cfed6498cd8e71a3bc1f108f0
~ _anonymous_client_mech_step : sha256 1b2a7d16bf5503a5764ec6bf555a1f034739fce26ab55dfa5f6954d7269d98c2 -> 1a29a3aebdec3c27368f92bbc035c7c79f050be1848ca257fa4deb4a1d269d63
~ __plug_ipfromstring : 572 -> 568
~ __plug_iovec_to_buf : 340 -> 364
~ __plug_buf_alloc : sha256 8d29407a5fbf2d95b6c49856087ec9414327f65c6a2abd58d7f4cb9933b338d8 -> 27415b848759e46bf533c4ba766c3e5251d3e43656d2af1239538b4128abdca2
~ __plug_strdup : sha256 2bea69e30b826e3ce33c3decc1d1481e332ea6c579e0468d6223df59adc28542 -> b8a06fbe10f5f645dfb98fd57b8b3d0f8bd2ca721c0952142f7ae62f094250dc
~ __plug_free_string : sha256 748b8648e4676eb8c7fa73021a3205a95a872b819a37d66a536d08a5d5a84f7a -> ea073f130e00a369cbed1b7e3aa889d27ee9ef886683710611a25bd53336675a
~ __plug_find_prompt : 48 -> 64
~ __plug_get_simple : sha256 b0862bd71a0c152a2f7c0d16b954ddbcbd242675cef3b110d873da6a69ea42cb -> 5df863127ee7ce739084c67f4711ad8070162a450a400d3a63b9f5845163d107
~ __plug_get_password : 372 -> 364
~ __plug_challenge_prompt : sha256 03b2bec75d8af5cb487811806e5ea3cfcfbec5b1921187f906ac3bf6e2ff00e3 -> f0dfc030dbfde81161781d51909002c99e0dd1af1ac7096035037d209ac557ff
~ __plug_get_realm : sha256 f8c8ac92caa0683f27c8645e5c0f04e6fef1635ae7e9057f8d9c002967ef5970 -> a6d93cc65510d81e8e4fc7adfee52084b49af7dcb62449066ef613aa9eb468a6
~ __plug_make_prompts : sha256 43affd99c62adff58a45d0ea50caf516dbc67a5e9c56c133d635fa19c0018d9a -> eb3218c5a7677c13aa8edf606da3a9616963b4a6ddedd793d7b4f5c559187d18
~ __plug_decode : sha256 29be8ebdad54d785a8687fd0304b70cda861624e6d3ff5909469831a909973dd -> 464cf10c63ffc674f4f503a6a1fee5474f7c857a80b661ac88ea503e51898745
~ __plug_parseuser : sha256 8335c987ad89dd3f19987cc46e5bb25f27124a9768494dde841436899f547f6b -> c049ca6c03e0c9990531a3c62308e6e7718dcf6134d970110fb165725437547a
~ __plug_make_fulluser : sha256 b08105685d019dad2ed5e938d484eab4ff0349a48560ec9a3b9eadf7ce6b618b -> 1a46b7dd5cb5a37fef62337c67805a95a9c1e369181226eb0fc1baef6a16e950
~ __plug_get_error_message : sha256 cd144b083688ea147b48292ddcb3e723330b043a2ea0242a1b665200383e4f9b -> 98f7ecf59e0d9b9f93f7d25285b4de7b7c0a52fdbe03582fb5a3d94749cf4441
~ __plug_snprintf_os_info : sha256 8415e5b98c394ac5f3a34f67c12dca27825e01c4c26d9538aa9ac4a9ead00147 -> b397a7410fb736dc818902e3b4885f19196bcf02c043c2064c89477627170508
~ _sasl_client_plug_init : sha256 edf0634c0b685cb03f77e538336e441546e6c051f77862572cd9f5c061cba87b -> f7fb2a03c19e88d15081b04a4422d7aeef6b4dc6187c835094c68d1ae95b3169
~ _sasl_server_plug_init : sha256 af700ea9d9418310a48f03cd6eb2f6b3b3e4a95df98f142e1fd31ec7b0715f18 -> 69693baa99540c5ea0e99dfa9bf7924ad3abdeba0723e143a6e4e6abe2874a18
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/anonymous.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/anonymous.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/anonymous.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/anonymous.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"

```
