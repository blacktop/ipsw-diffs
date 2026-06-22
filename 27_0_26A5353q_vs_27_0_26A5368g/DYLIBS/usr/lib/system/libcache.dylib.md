## libcache.dylib

> `/usr/lib/system/libcache.dylib`

```diff

 95.0.0.0.0
-  __TEXT.__text: 0x2bd0 sha256:9029d8d63a197c88a3040edfef2135cb59c5382ccc8fad678a8b4a341b33404f
+  __TEXT.__text: 0x2bfc sha256:3f862d9315b6d157beaee83282ad14ccdf33db550e2812e312e05d66847d4bbc
   __TEXT.__const: 0x38 sha256:b7bab6c5f65f2ccd5204092f6b370276a8bf31ca1b32c3eb20ea7369c14a48e0
   __TEXT.__cstring: 0x162 sha256:b5b64fdb2ac546aca3f9d6c9d11d9b5f0f2b90b578b1416f5179daf45ae2dca4
-  __TEXT.__dof_cache: 0x1837 sha256:f2d428fa897a4c1bea953dd28023b7f26df51649c3d063f6ff215e8a8d6154c1
-  __TEXT.__unwind_info: 0x118 sha256:3d91b0d2fa6d68645c9fc05576f25b11b4436bc397e77a5c89334f332d133488
+  __TEXT.__dof_cache: 0x1837 sha256:a263105c44ecb0c1cba7c99f3611bdec5ce57e0c0fd8f6dbd0b51013bdafa6ad
+  __TEXT.__unwind_info: 0x108 sha256:c45474a59b172a904798a8fe0c3e9e42c9c810b86193186037b9a20fe8684a0f
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x88 sha256:cbac2c2bc54784d3e572ea0e05467e1da0accfd32626d68dcd7beac0d5cf507c
+  __DATA_CONST.__const: 0x88 sha256:d9901f97987f9e15e04f54322b97b0cbb24aa022a64ed4a7e63d8d6c7d30c447
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__auth_got: 0x0
   - /usr/lib/system/libcompiler_rt.dylib

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
-  UUID: 045DF282-E418-3E94-9572-E47775105F03
+  UUID: 082AE788-E782-3E1C-9694-A631E823766D
   Functions: 56
   Symbols:   92
   CStrings:  20
Functions:
~ _cache_create : 536 -> 548
~ __cache_init_globals : sha256 6c1985bd5b451964510f61f08cbcef8751f1783a20e05b971bc11fa4b6f0b4b5 -> 8e94b42a9c8e4edb279c02dc69be616f90db8a0226d95e7ecfb53ee1c559d68f
~ __entry_table_resize : 592 -> 568
~ __value_entry_table_resize : 648 -> 656
~ _cache_set_name : sha256 ffd15c2bfc777c1b3cf3654b0f397df9e593662d224ddd6b12fd508dc252d902 -> a7fe679c22fdca84d54eb3ebb7f13fe31a176e61e981a338860e92d423dfe394
~ _cache_set_and_retain : 1492 -> 1520
~ __entry_get_optionally_checking_collisions : 380 -> 372
~ __entry_add_to_list : 168 -> 176
~ __cache_update_limits : sha256 42628f3a65929a504583415255a3651a96297a6dc6db7768806a7051d8a83b4e -> 28b4227f1a9380121f12113f104ffc5afa47c8a8ced06dda3b68c3c9730d0e22
~ __cache_enforce_limits : 264 -> 256
~ _cache_release : sha256 a6d8e1de2b6e2199309c23c145ce5bdb5d792f67450291ca7f8534cb28859589 -> 439d1c5829f5c457b9b10f8f1e8f2df944de74c1c2e62b39aadc965ddb699da7
~ _cache_release_value : sha256 7b3fcee7d304aa9bc6098680ad440644377b5bb5d2d6b046f8181ceb44f9d0df -> aace9fe20d92022682d450ccc5c45337c8e91ef07ae6419c40ca295b92caf501
~ _cache_set_count_hint : sha256 fe8fddd6f392e5fa3be2308afb28b03b01c87cb54218a1fe39f56332e3003758 -> c2a153ccd28bc18a0d6cc5a2db811a2722f43aedb5e395f165aaef30312a7fa0
~ _cache_get : 520 -> 528
~ __entry_remove_from_list : 200 -> 212
~ __value_entry_table_get : 232 -> 216
~ _cache_remove_all : sha256 9022fdb178b0da6caae53a0e2a6c03af97108378d95c64f5783a0f1d392a6c5b -> 60a69dd4cd3becf1dc5d5e60467f44332041b25c370b6d617b942fc44c54c04b
~ __cache_remove_all_locked : 120 -> 108
~ _cache_destroy : sha256 f2023740ca8e9c04bd46be9f92415358f25977214206231254c723b91f8ea380 -> 535b1dde4e4e456d74a1d76e252708dc1580ef12b49b5e04b87b4d3356d46c3f
~ _cache_get_and_retain : 528 -> 544
~ _cache_hash_byte_string : sha256 ce172cf39bce83992442150ccc51cc2822653886adae8a6afb782aae06a43c8a -> 4cdcef14e73eb2bca5e2cf968d444e16427471df1223a45541983e619580775a
~ __value_entry_unmap : sha256 f414337b33f1c70136b2717a1f81ed99d4c41a383c4a26983a450c0ed0292796 -> 6342c530683b1140dd95482951605944d88224ff50a127596115595eb9b11245
~ _cache_set_cost_hint : sha256 e9bbac62867d06395105be1e3e8124eb22f9ba662d8917791ac2936bc1b0fe2d -> c5f82a2970733adda82fa6fa2f7f1468c2c87c2d4940081a497083fcf4fd184f
~ _cache_key_hash_cb_cstring : sha256 d378be0859acd0d2479067f795f5bdbfa4a5455c4331eff16d2f2d30066a0130 -> d9c6f2c3c96766c5868d87a9c0bbe0224d1bdcd9dbaaa071065da33668f47d49
~ _cache_remove : sha256 d2ba018575838ae51df1134e26291adb93f7874e2a3337f04cb44570d419d91f -> 5d9dd8f9f7e9734f6e2cc28da21917e022e8f6c83f5353c397fcae1d5b3088ce
~ __entry_remove : 328 -> 332
~ __value_entry_remove : 244 -> 248
~ __evict_last : sha256 fda05623f2576faff2bc0955d3e8cba3e8bd3ce9e070ccad89d8babaa7753f38 -> be91224c3f3fe881033f3ec807afdaaafaf082eafc559657d21affd98bbc399c
~ __entry_evict : 196 -> 200
~ _cache_key_is_equal_cb_cstring : sha256 81b92b9447e5ef95c1ae0fca665ea21911013ccaeca71b7a7d3bced9a3c0f872 -> 703d45ab421983a1d16c733a4c8305d664597edf9ee322756aba81f23904e5f5
~ _cache_get_info_for_key : sha256 42aacf651af11c6bd3a57d9c5c6f84584ecb34b85b9059aa6dada266e3354646 -> c6a946aa00988161fd96c105300de74d95f9da45a8d9221bc0dd960f8c542700
~ _cache_get_info : sha256 fe51be6965be1cdf595b30ae9232eb7f639e13d534c3f14790ef0d824a75cdbd -> 3bef7b4d0c269340d87601b45246ee11f4ffecf4ab7c780c225e0496d6e3dee4
~ __value_entry_release : sha256 2ba55db172c0dea2986889a5af8af14a2e8f8c6b84b9affe2e96102df37b281a -> b826d0c946a200d73160a6559595278adeb107d7b0ee0c2f7b5c4baac6707b0d
~ _cache_remove_with_block : 284 -> 276
~ _cache_print : 872 -> 876
~ _cache_print_stats : sha256 62802cf28e326926295e1e412a2557545058f5e7256aa39cfc5d723ed4081687 -> 94fc93e44ea6bfde631ef18e12995b300884dae611aac4bb92f674b04d875dbb
~ _cache_invoke : 208 -> 212
~ _cache_get_info_for_keys : sha256 ce237c76af88dcc4835f25b911f7d04bba400166c672298f3b42327b92203981 -> d87b4ccd82893110fb482a9b738010bf7bd433a5de5ad99484c4e2712d504a2f
~ __cache_get_info_for_key : 132 -> 140
~ _cache_simulate_memory_warning_event : sha256 560dd2e281b35917faad62338d79b09b5d2dabfccb18b4408740f2bbea8d04bb -> 360ed04fa27ea0cea62b42f76434d7dbe0e0cd70cd5cb1c32d88e8573f2b4630
~ __cache_handle_memory_pressure_event : sha256 208d2846b63a2cf60d5df05b6175622ec46c475931145dcb35bb573099932474 -> c46d8b4d0ba109304cfc5973ea31a65287a89475e52bf9853c1eb944ed17f54c
~ ____cache_enable_memory_pressure_event_block_invoke : sha256 3dee52de1504d1c6d3ab8514baac669dd32990dfda18d7934fcce4e28934706e -> 1c890711d7edb4a1be5d9cee79ac3c63c4773db5d3b01817c901706023d3dea7
~ ____cache_handle_memory_pressure_event_block_invoke : sha256 85c77f4f92e49d860104de1bd89a1ea3b061e425496dfd80f53f446669825b15 -> b22c2f1bc17428ee2798d93f9362a87091ae1ff8786878f95fe7c8ff3a8beb56
~ _cache_key_hash_cb_integer : sha256 0eb9196d789420708e58232acb2ba2464dac4b9314ba4f00b6ab7e490b9fa4d1 -> 034ac7c5ca0d2dc2ca37620d37b206bc51c1aace2c21ad2147e882842233a401
~ _cache_release_cb_free : sha256 f51c055d7520dadc31725909644b5f5cfb8f6659c7bd3d67362a52ec4da1c37e -> dcdeae4b58b289a8b76a9b7a4ef3ba2acaba1142478246c96d3d0ce2bd47f915
~ _cache_value_make_purgeable_cb : sha256 d5eb1471ad23959cd551585a903602e4aedca07059e1b2beb7d383c54bed2d4f -> 7914635782940290fd3b3393237e9fd58e2023a09a8a385b1bdc35e415bced05
~ _cache_value_make_nonpurgeable_cb : sha256 4ccd0ab43cf2b03ed206b2da8137571f6649b7b81d7a848f7b9abed070849efa -> 0f81db62c3555f414627e8f93f0f340417697f312583b0860d6a21f32d8a5e9b
~ cache_create.cold.1 : sha256 c9f520e35bbca00899c577587700f8b5bcf78da916029bddd829bfebfeef4f7a -> 2dc41a16c72e3166919fd9e10582727d614505111110330f26685f178c9f50ae

```
