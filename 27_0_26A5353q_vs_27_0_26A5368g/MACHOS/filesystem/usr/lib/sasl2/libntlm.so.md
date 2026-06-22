## libntlm.so

> `/usr/lib/sasl2/libntlm.so`

```diff

-215.0.0.0.0
-  __TEXT.__text: 0x3de8 sha256:7fdb33f240d1a02803fd9c652d1af327232937b315f6c3550eeef1d76f01cb5d
+217.0.0.0.0
+  __TEXT.__text: 0x3df0 sha256:be56bafd81f3903710e573a014b71078e0ffa6db563958cff6a5ce0f1b5235f5
   __TEXT.__auth_stubs: 0x200 sha256:66d9e63c58eff2bfc1748b9fb1da000378a95fd447582131f4b085d15a1c99b0
-  __TEXT.__cstring: 0xc11 sha256:799ade69699298c4090df120af1b5dc4a212815cd307a135d82827c0bc0b5720
+  __TEXT.__cstring: 0xc11 sha256:c38162d7a245836a2662aa2fcc01f56e94452fbf556e3e1d49f1785afb464c2f
   __TEXT.__const: 0x8 sha256:6160d291f069f8cd014bb760f7d165c45a04d289b68b766e2660c44366718030
-  __TEXT.__unwind_info: 0xf0 sha256:584f9647dd0c1129e662c3294de2531100b317348d11e76ee3813c7372f95311
-  __DATA_CONST.__const: 0x30 sha256:99290f7f88b7677e6f69479d91a85b30c272ebcbd81d093004442aed4f1d1fe4
+  __TEXT.__unwind_info: 0xf0 sha256:b41094e9b20eae4cfc70f1f4b7f2635d48c5dbd07a60d868efdf549ac2e89b48
+  __DATA_CONST.__const: 0x30 sha256:7822e1c8e78c69b0ccc7e7fb76cd6794b574390a0ef7cd837beb71dba493bf0a
   __DATA_CONST.__auth_got: 0x100 sha256:bcb56104e98c44685043211cbaeb106a0a56a3745b5269224002a7a8487c3c4e
   __DATA_CONST.__got: 0x10 sha256:d01e215c7999dd0c6e0ceef704703c7a60064f559c0ff8f46940978a8aa74a46
-  __DATA.__data: 0xd0 sha256:c86a54bf36b85a69bfa5784817f993b2fc6199c7d0c46535755adefaf7cba643
+  __DATA.__data: 0xd0 sha256:695774b687c2a85782f69f5abd29d12d0ab128dfb9c617f8ab8f1a23471b70b6
   __DATA.__common: 0x500 sha256:bfe492baf731a0dbf6e1e050f5bc3fe8c1b049383194dcdf82f023bfa409f462
   - /usr/lib/libSystem.B.dylib
-  UUID: C6B3C8D6-9873-3DA1-BB3F-93B739A1CF7C
+  UUID: 615C6374-E453-3DBA-8B1C-7B9EF66ADCC5
   Functions: 44
   Symbols:   82
   CStrings:  82
Functions:
~ _sasl_client_plug_init : sha256 c74081ede463ff699dced2e4131c54b24568718fd6bfda7f642fd433f55514a7 -> 3297e7fcdda8d3145c3a7c6b686e5c5154b49c76acce56c17515fe91e1fd73b8
~ _sasl_server_plug_init : sha256 20a845a719bc813717c106099633cd5eb1aa61eb2b416fd337fe25b844b2eca2 -> 9bb1941bf2b7410148ee500f0aa8eea8d48818fb3884b3959c1ff93d80a71a9b
~ __plug_ipfromstring : 572 -> 568
~ __plug_iovec_to_buf : 340 -> 364
~ __plug_buf_alloc : sha256 4191823d1bd1eaea5aef33ecf59c339ba3b37738702350e3ee9e0190f75e9213 -> bb77653e97c1f1983af78628c49b03daa49252c792695aaea03e3044e74eadad
~ __plug_strdup : sha256 5dc6624c7b655fea98fe070ae04b7b627fffe85d4116ff5796cfbd9b673eec0f -> b0d079d26fd1a1f59e4d7cbaf69bed2c99ce4ac6f02e0b7a26bfb52886eeedfe
~ __plug_free_string : sha256 9125ea53b923c53ccbfdda9a4f02a933e34bbde776573fae634a09259837fcc4 -> 40ad22147088ad4e041a984fe0c620ebb10b8adead1258e63272e3495abc35c6
~ __plug_find_prompt : 48 -> 64
~ __plug_get_simple : sha256 5879a1b80d28b7df1af896e452ece343df2b1c93c220b40eab5ed9d7b756b0b7 -> fca0f15d7417adc5b697f4d5ac33be11b61e3c5fd79df334e319b589cedc3bf7
~ __plug_get_password : 372 -> 364
~ __plug_challenge_prompt : sha256 aaa37fc43ed2e7af2cc4cc082052f837221ba7a0709e26f4454becb1a775339b -> e0d1e360ec1ac2abc54ed022dd74f11c703c9db86f3333e05c0fa1e6b69e5c91
~ __plug_get_realm : sha256 7912506bee204f2b3dab47df163d4a0043b9b0d0c1873df8887cba9b40b8cff7 -> 2d82eee65b4da8e826240280f30081c4eb0c5a601afb94c93636b5f533b82999
~ __plug_make_prompts : sha256 5830ce1dc55deecd015e3dde375201b773d9e1b30711c65df8acada37dbc108a -> 6db21e0adde2803419b18d3290aa92ac7001f37677972b8ad40a4bb0c1599a08
~ __plug_decode : sha256 446e9bc3b71fd2e8f5e1150df6ec765f4e12f4d961c6ce92ca5367184af921cb -> 3503fa2fade16e74a1be51987ed2b2a05973724543528df8e710d5c0a3255a77
~ __plug_parseuser : sha256 95fadface28e1079b314507e399fc283d764620334409c2b5a1703aca58c9543 -> 695e2957dee04b16de5c628c34512c82e261b0dfc34845ea5c9a5d4d012e3c10
~ __plug_make_fulluser : sha256 ff1a7b4b0f3e5adb43d0321522672e452705e94e5d5b02e30ccc67d5a1e66882 -> 4b775b7751b994d811804682ff962a2fda071413fe071853ed0e72fb48d79e8a
~ __plug_get_error_message : sha256 3af8caad940e0c6170d1571c85724e9b4d91be440943b3a8be3977b15f5ae596 -> f46c30f22377d0ad040086d9c7b48f92511bc4b6b3e7fe0b351c3a5d69369e49
~ __plug_snprintf_os_info : sha256 ffe85fa40e44391b6833625a731ce9d52229c14703dc1a91d6124e79b925e194 -> 08cb232c15402c8491f3b744de4a644b95be2a8dcb0bf644ed8f4c28110bce0c
~ _ntlm_server_plug_init : sha256 4926143b9a951deb0ec674106798bdc36619e998e7b053f93ce136e0497abb11 -> fbbab04a72b707e3220909ec71791e073126e8b3f590fc79738b4d9a5abcfc7b
~ _ntlm_client_plug_init : sha256 30ff83822b554ba787f5d33a839b5329f165af3384dfaf6c1cec381048d7050c -> 008f11b2b3ca9f888faf8c70486ecc10e88a37fec210a200f252044ae74ae640
~ _ntlm_server_mech_new : 1376 -> 1364
~ _ntlm_server_mech_step : sha256 17773b537940ccb55e5cd683e29fbe2c713eebdf4b0f4c2427e6ffed0b81e0c0 -> 927d27f94021ff56bd5c86c458d4325f790b7180628eef4a438d7d431f91297b
~ _ntlm_server_mech_dispose : sha256 2777bdfc1d962913c2e3f8e73ba5295d9205430d8c6a31e02ac065650f34514a -> c6ad8d0e0df146b3e1c55a531d94883fcb70b766508d06fe87ef89a883e9c8e2
~ _make_netbios_name : 224 -> 228
~ _retry_writev : 300 -> 288
~ _unload_buffer : sha256 fb5dd901feb709d54366db6b40be3310366ff44b5f18d0da746cde42e3f6a87c -> 84ff30e5d5fcd5fdaa089e10c63af048802e3d439ab16a6c57557b0b7e538897
~ _V2 : sha256 0938ea9ea2a7694136f3f60ace535c47283b10a1036a8538ee740cce1055fa76 -> 88377a982312e1ddd424cfe6f9d59ae07670034aeab86e922297408a3e95f33a
~ _P16_nt : sha256 22a5295183ae991ab79ffb73740a67826a5724fbd3bd3a43847e55e3ac07f4f5 -> 287474794eba2a21721020b1e7399cbe49e75d7e690a688b68d2010012f9dba1
~ _smb_session_setup : sha256 8f25b7be207a29baa12b52db6903bf7ab2c24d641b18a5a793274adff7000bd3 -> da6c6eefa4636735c7539459247da3555c1792f5151c4ce3974e2804f714f898
~ _E : sha256 b25c39d80c39cbd96580d7b986c9e0eded1be75483c88d6ee0f0da6235cb042c -> 0f95090daaacbc1405ad50d0685c293ffe93f5fd21d02f373ea0a29f5ca5c755
~ _ntlm_client_mech_new : sha256 82631d841acaf8408fdb537206f470e22bd1afd5770f4d7f4d7fd0c504658e15 -> 4b9acd944f2aa935ea7de4fda9647f42b42f7d5bd55525c0cd1a8d8da8e1b968
~ _ntlm_client_mech_step : sha256 399dba924f6350e6ba7a9030c31310c42ca230a1a3471b4fd0d773f4f876347d -> 32ac716756f3af81969dfd4d4e042fe84ff4dd8c3d7f688d12ae37bf8ab9fca1
~ _create_response : sha256 6f7092ddf3ffdd30c3ac78eeda4092b6362b8ae634ae4a5076f67956cb854c31 -> 7ac3318206524c3709d4024809b747aef7bc026fae460c11aad550a01b7ca76b
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/ntlm.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/ntlm.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"

```
