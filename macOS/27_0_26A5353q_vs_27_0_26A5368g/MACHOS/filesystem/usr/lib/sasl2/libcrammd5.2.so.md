## libcrammd5.2.so

> `/usr/lib/sasl2/libcrammd5.2.so`

```diff

-215.0.0.0.0
-  __TEXT.__text: 0x1f8c sha256:7cc47160ac29766e3772a2a271425c1b55763e88a5e346ba1934e6cb98976a90
+217.0.0.0.0
+  __TEXT.__text: 0x1fa8 sha256:0cc81ab5bb115e3c333601913847ab4087a05e4abd606fa20e98409d11b62b70
   __TEXT.__auth_stubs: 0x110 sha256:c4d9f44af171aceb6dc171b1b3d89ba6cba0bf08cbd8a625545337590d3f13a9
-  __TEXT.__cstring: 0x5ae sha256:0c0dcb193cfb638ec86363356dfaac21e3725caf82d501b52876ac0e7e598ca5
-  __TEXT.__unwind_info: 0xc0 sha256:7a2e655fe39527ac0f3e32109a1c42bac8bcad6b56ecb36d97e3d951f5585d5a
-  __DATA_CONST.__const: 0x18 sha256:79b5643160c84e3d0e776a0216698161b4968e1e3bb7d16fcc6c2cb373c53a4e
+  __TEXT.__cstring: 0x5ae sha256:e89d91cea26c359add9f23ef651298bebccd42be67940781f4389ed36daa9a7a
+  __TEXT.__unwind_info: 0xc0 sha256:ab5a15d416d1c12e24a09a69b205b5233069126ab75f8f185b3acc18b838caba
+  __DATA_CONST.__const: 0x18 sha256:624b1c64cdffa6abf0c0188c4d8fec6d6e4a3b4b5a26ad17f3f4975746416d50
   __DATA_CONST.__auth_got: 0x88 sha256:27bbfea54df58c994fa4191004e52df860cf4496314efe05d61041304212be4d
   __DATA_CONST.__got: 0x8 sha256:1d845810d7c459d90e6ec3eed65b8db4b9b9d8e72bf7eaac383bbab28bbc8693
-  __DATA.__data: 0xc8 sha256:b2541a8a1bf05f887716f4b01126a8e24f672138990ab1742bbe6bfa896640fe
+  __DATA.__data: 0xc8 sha256:0d96001f36597e6bd729bc18de51f899e93427acd3b11aeb61112e79f4f71d15
   - /usr/lib/libSystem.B.dylib
-  UUID: 4A3C8767-DCBF-36A1-94F3-F3AFACF4DDFD
+  UUID: B1913E64-39E4-31AA-900A-8BBDD6014A0D
   Functions: 31
   Symbols:   52
   CStrings:  29
Functions:
~ _crammd5_server_plug_init : sha256 8e73eba048240c3dc2cedd9c7a99f936c41afea4f4eb140307b2beb3405c6690 -> 30799b87c69972d17d5d9d9d9ce69ae9d202d26bd47622943dc547167d7a0a0f
~ _crammd5_client_plug_init : sha256 75102a6fd2fc8c7f04efd90e7b1e4243ce356e7ccd7d63660a7dae4c690add82 -> 8ec9b1fddd5dec1b406ea2dd17eb7113614631ec9f6006e5fb53b3eb0895b660
~ _crammd5_server_mech_new : sha256 c2c65d290b571bf6ab24a32fd1b9e971c3d8b47524d2c051080b24304df4c9f9 -> 8e8ce4b2ed515c9bac8f912cbcb469f0fbd5ef62bc397c6a659c42d00e287a47
~ _crammd5_server_mech_step : 1540 -> 1536
~ _crammd5_server_mech_dispose : sha256 7fa85ec4149c1b8eb4ef599cf68aae53dbfdadfe3fd636730c0e703d8324fc08 -> ea7f938a578d281906732931d5077bdda9ad6969e7f52a6395f686fd008602b8
~ _convert16 : 120 -> 124
~ _crammd5_client_mech_new : sha256 686aa868caebe75e95bf72bc262d1c2b43fa60d767f76655cca03116b92bdd6a -> 110f5d336daf076dbb2ce8fc1e7742830e3c60e2151b7fda2236bea36d4c2be9
~ _crammd5_client_mech_step : sha256 0c3ef1239998bf523897a4636ed1b9b2ed4e0986380f18868fed9f27b2918cab -> d2a6428ef9a5e6e2236b98da79bfd458ac00228e9c2165ef9fe663f457fd5dc2
~ _make_hashed : sha256 7dde41f2089b72013464e6260139067e3246ddedc15ec161c94bec890901ace4 -> 0760ea95d8c72b6e6a5eba9b9b9da1aa9c332cfe5f5af36f7da36355b7f2cb93
~ __plug_ipfromstring : 572 -> 568
~ __plug_iovec_to_buf : 340 -> 364
~ __plug_buf_alloc : sha256 86d7d80ff354acad0cc5b93f9aa226f259d6e72df00b5bcc8f7c498bdb9bdccc -> 30d1c394fa7ce42f620e9f84631acbd2857f55b366b3c919635bb2bfe5dbb33f
~ __plug_strdup : sha256 236c77921360d0b850904ffc4955203e023a7f7279f3d716c17931b932f9ca5d -> 961ca67d15eb4d380e38938a77776a875c5608ad697af88f5bc4ec8c10a444e8
~ __plug_free_string : sha256 748b8648e4676eb8c7fa73021a3205a95a872b819a37d66a536d08a5d5a84f7a -> ea073f130e00a369cbed1b7e3aa889d27ee9ef886683710611a25bd53336675a
~ __plug_find_prompt : 48 -> 64
~ __plug_get_simple : sha256 d9c6b6c75df0ef80d0c7a2c7839a45217e1cf77a902f007f5aa0f0fe322e672a -> 76bc99fdb8ace69676a24acf8d485bd9ae13463a6c99d126ad8e35822bd28b03
~ __plug_get_password : 372 -> 364
~ __plug_challenge_prompt : sha256 0d14bccb2ceb0766825a7b5ab7d644950f7635004d70b2f21775ab09b09c1b1e -> c3aa4cff95b0bedbcf7757ee8a563e286d02ab7c4b6788ca056385898f6aec28
~ __plug_get_realm : sha256 1d1381097eb8cc8d75bcd15c32fd7ea01f32178afe6aad1f2143f3e69ea669a5 -> 1ddd2d5c01be693ac2fdb68b05cc6d5eabc8505030b3be2fefd4faf8dcf2518a
~ __plug_make_prompts : sha256 b5a859ad267dbcc01020c9678784109f2d16dd6e55e18ec3b562357fedb20da0 -> c9320234f8a5d12a1e736009d88919e724d2d230248973ef7d840715f31bd29b
~ __plug_decode : sha256 0afa1bdf4217c43b6907dfaf68b39e3f064e9090f6d010bdc35e7a2018e45d1c -> c6f29b9a6d94c38b6131d9842deefa815b2397d97ab433a27a136660ab2ddf5d
~ __plug_parseuser : sha256 994d43e0a1feb58438436ef96d09a5dd3d53e951cc8ccdca95d77856a3029608 -> eba63c456ed36270b08e162df4965c8727b7209ee0c495333f9136834000a3ec
~ __plug_make_fulluser : sha256 926222c2f7e57b63b21a5b0e9e70bb5f829fca45d0b8f9ce02b0d954ae6833dc -> 385b6b210951898f5ff2c972d814152daea5bac6c5e59a4c4db91b1e61653c68
~ __plug_get_error_message : sha256 cd144b083688ea147b48292ddcb3e723330b043a2ea0242a1b665200383e4f9b -> 98f7ecf59e0d9b9f93f7d25285b4de7b7c0a52fdbe03582fb5a3d94749cf4441
~ __plug_snprintf_os_info : sha256 f8e197b8ba2b125ec18ef4b9eec37bb0128e342bd32a9da2405ed974a29ed400 -> f553ec6690f946400eee5c16b074bf74255abd6cf0a6086719825480027aff7f
~ _sasl_client_plug_init : sha256 50525c6d47e42695a79fcd65f76184be47946297b19ed2f1d8b6644baf744aa1 -> 92f5d70914e284236aeacc01ab4892a4a30e8e3742d57187146c79ae044b548f
~ _sasl_server_plug_init : sha256 bb76acb8e24548b361e6fe9ef3650c32de470e069019da48599f6a707e1a8003 -> 0b696ad63c35a9d94c914dd07f3baa98b096505394e3b0a83eaef9517bde32ac
CStrings:
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/cram.c near line %d"
+ "Out of Memory in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/cram.c near line %d"
+ "Parameter Error in /AppleInternal/Library/BuildRoots/4~CRa8ugDo-VpAEDF3itcuZTO06m8KJ3w-H10Y3KY/Library/Caches/com.apple.xbs/TemporaryDirectory.d2EdcA/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/cram.c near line %d"
- "Out of Memory in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/cram.c near line %d"
- "Parameter Error in /AppleInternal/Library/BuildRoots/4~CQBgugA2CeLdOJHHJvfzbXVHc2KPps42fc0MheQ/Library/Caches/com.apple.xbs/TemporaryDirectory.kHcsmx/Sources/passwordserver_sasl/cyrus_sasl/plugins/plugin_common.c near line %d"

```
