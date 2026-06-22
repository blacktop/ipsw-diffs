## libcache.dylib

> `/usr/lib/system/libcache.dylib`

```diff

 95.0.0.0.0
-  __TEXT.__text: 0x2bf4 sha256:f28fbfbd567a487365a33f47b0c37d1da16df026c11d30ec25c8a1c0c7064787
+  __TEXT.__text: 0x2c3c sha256:bf56cd12b73e7c4db4848ddaf8bd72d5b6f6d2e390ea47df425ebae37109d6cb
   __TEXT.__const: 0x40 sha256:a0f439d700dd3d3ce981479c12220f3b822d81675bea49a380fba4ba151ecc64
   __TEXT.__cstring: 0x179 sha256:68720f9193633ffa8da38c16afc83177d3470c0e849d7723aa269ab126a2e3c8
-  __TEXT.__dof_cache: 0x1837 sha256:308f2627d2c7d7e62109870bf11bb94d14fa7ecdd7790c810c571df04e821003
-  __TEXT.__unwind_info: 0x108 sha256:9c664ca008818cca6f70dd92803bf46a80da849c8a1301efb5f24ec34a23264a
+  __TEXT.__dof_cache: 0x1837 sha256:5efbacef0a81c861ed09172f67cf38200ba15d6eb794ba834c67fb623bf023b2
+  __TEXT.__unwind_info: 0x108 sha256:4b65bf31f521d230bc5986f7e071092e8efbd5ec4edb85647a6ceabddc3f75c7
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x88 sha256:12db056e99338974c653fdd907ff4855ee7cf09efd96fd0f9c2238c1d4936b57
+  __DATA_CONST.__const: 0x88 sha256:bc2c3cffa83a8a4f9ab45c9e0d4b909d348d30a4c5701d31f74e2003d85071be
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__auth_got: 0x0
   - /usr/lib/system/libcompiler_rt.dylib

   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
   - /usr/lib/system/libsystem_platform.dylib
-  UUID: 7E91BB65-DE08-31ED-9C4A-E175411C25F5
+  UUID: 728736D9-577D-31B4-9DA1-DD01A5C46088
   Functions: 56
   Symbols:   116
   CStrings:  21
Functions:
~ _cache_get : 504 -> 508
~ __entry_get_optionally_checking_collisions : 400 -> 392
~ __entry_remove_from_list : 228 -> 240
~ __entry_add_to_list : 196 -> 208
~ _cache_set_and_retain : 1448 -> 1476
~ __cache_update_limits : sha256 fb5f1b1e6cea3b39cec19cc8b1008e2cf902f4698e94193037494be726ab584b -> 670d66a1d6a0fbe11068119e3a2c7a30a0de5acda928391e3db917171942bd6c
~ __value_entry_table_get : 232 -> 216
~ _cache_release_value : sha256 c64b33b5985ecff5ab0c9829e04e4555f3c6229e75852860e6bfe37c70b91215 -> 4db71b2c8a55f219cc03614e751d7dd6b059d85deca98d648df12f178d60b078
~ __cache_enforce_limits : 264 -> 268
~ _cache_get_and_retain : 512 -> 524
~ _cache_release : sha256 6194a65896ce42755291ec57c929a04b81a0994bc5ccba07bec1828cae27da51 -> d39bc77bd014a7bfda68207e84e756ceaf3c82f509f877de64450cb6963dadbf
~ __value_entry_release : sha256 07cb7c8ac62be24181c279dfd923b73714aea8b2b1d40a329749f63f3fce2014 -> cfac90532f117e584325ac4e5a3949beb796e104f77dcbbc00aee1d193436fb9
~ _cache_create : 544 -> 556
~ __value_entry_table_resize : 620 -> 624
~ __entry_table_resize : 584 -> 568
~ _cache_set_count_hint : sha256 eb939b0e6e5bb4588964e92b7417fffc528aecc03d9b964974286529f7b55f78 -> 1446022c536578f71d8f8c1a6a41840bcda2b9670b8541487f6764c93330a162
~ _cache_create.cold.1 : sha256 f821cd11f81921f777f6838c477448b77e1b0404cd68ed9d4f0140aeb236e5a6 -> eb0e63c39b6af3ac4c2168db509195a4819fcf8125e4857d040a7b8949ac9058
~ __evict_last : 132 -> 136
~ __entry_evict : sha256 f08a675d6db91caf50e6c578f48a718ac35d10f38872ecb4bd387fe1d04a944b -> a1ba811f41ea4571a7df3b0914ce3de2efafab4426c8cf01222f30ad5c409a34
~ __entry_remove : 300 -> 304
~ ____cache_enable_memory_pressure_event_block_invoke : sha256 89efadfcd02020f94827be3f49545d5add112cbb030bf8df2964319181706005 -> 737d11441300b39a0ac55e266abbb75538cb0e67757a65d3347e787b1d55428d
~ _cache_remove_all : sha256 3c703cb62d920ad90cc4a34a437f4f7b118f91b47c13968118d93083962b5a0e -> c59b1f9b0537659cdaabfafba46abca9d6943a92132b41ac36113334fbff65a8
~ __cache_remove_all_locked : sha256 02fb36144bd9e2da7253855ccdafb9c5ca9972964f3024a4fba97a9322aaef4a -> 1c8b62f1fcac63a2c20fda9d889f7742b43ebf59fbbb80eb2533216a9da16bea
~ __cache_handle_memory_pressure_event : sha256 1546bedfd8e1e92fd98803e9aef8060397faa96db49690a4129197871fb3f526 -> f2404d9fccf574d227b206b89952a45dd14ee825840292b1eb086122a7634781
~ ____cache_handle_memory_pressure_event_block_invoke : sha256 0d436569d237da77e5bacf09343d27d6f5e751b2cc195fc41313c99f6ee7fe89 -> 7395d64cc3d8b12ecb07205c3dc8b6cff637e2915b4e91c17f1c1b3d2655ce28
~ __value_entry_remove : 244 -> 248
~ __cache_init_globals : sha256 56014193740b1bc70a05fdd466bc550f9e2d02cd901a8cdaf0413cee68118168 -> ed726a6f3b8385e0353e294d31a5198581561ea99a14fd28fc62d23217ff1a7d
~ _cache_destroy : sha256 d1fa14ab635a68f12e7597df36f45c2b6047cef43c6eac3a9d399dbe0cf20204 -> 7ede8755e230f0f95caed03a330ae5e4c27915384d55739d8338dc11f98382aa
~ _cache_remove : sha256 bc00d7a2fbc5311c845a60895be1ca0ce1bdfeeab1f171742aaa20868ccedf6a -> ecd9eaa95bfbe72f30ed993241ef520ad411757725a3b213aeba4a2368140efa
~ _cache_set_cost_hint : sha256 57c29b91e40452ef2001ac4e390a998b155bac841202d91068ec3ff21ba924f4 -> e4d9782de85a8864af62096787ff732daa7b0935865e43e639ce27d83fad0d71
~ _cache_remove_with_block : sha256 03f4e3215193f4d1aa60e385ce7d1527fdbab57be37bbd09cd171a339108eb8b -> 66e9fe498b3765d67cf9037ed2623d310ae12fd39b9d1d6cf58e0ec2c9291c6a
~ __cache_get_info_for_key : 124 -> 128
~ _cache_get_info_for_key : sha256 6b33bf4011ea371112b722ef60886f98ec32e516fccdbc551cc0be8b1212cd38 -> 920e5f3fe6ccc36594c259fd251816af33f8ed779a59f6f09cf4d419ad77c116
~ _cache_set_name : sha256 cf885350037a0b1eb3c9060a627cc15f445d21d24310642a498a586b933c1818 -> d106df482633e61f319e93b9cbe2762f0585cea2bef9fe6ae153daddfdd468e3
~ _cache_invoke : 204 -> 208
~ _cache_print : 880 -> 884
~ _cache_print_stats : sha256 ae70bf016f2f052096b04e37c7fc0c1869b83b45c84f10631ae0ca842cafe69c -> 8eafcad8067b973f517b42a01e508042ea25bd533981d383fb1c138837f78e70
~ _cache_get_info : sha256 433e85bf94217834333afee726a5ca2d3f2e3d02c324d1c0e55dedde02f3c850 -> 33fd2e1e925778838ba47a2047589c2245b7119f7b04484c645fa702c021c006
~ _cache_get_info_for_keys : sha256 38661c38ac8e8fa6d3f0fa9d064a4629077efbbed46ec0a013b18a0394b32304 -> 634b3c61b6f2675a9d0c7a05ac153fdad6677d5a295bae18ef5b8b8b43ca8454
~ _cache_simulate_memory_warning_event : sha256 40b799c9d475a5edc7b1da3bf2e38b9fb7027c36c735a9869bfc7e66b11b986c -> 880a9d7a06527b9d042ff365fabbd34a14704a793a0a50cde3bc600389b88893
~ ___cache_simulate_memory_warning_event_block_invoke : sha256 44856167098f0e56a88ed3740198cfb6d9440d73a2311f9852b2a5dfe8a08190 -> 7485e1ddc3c06ca6fe6f2d24a41643f2ede4fb84dacd816ab64867bcc5430300
~ _cache_key_hash_cb_cstring : sha256 588182a2d40bb7e7acdb4eb20e9cf2b6e66e6f6aa4d6a19546affc76fc6f7833 -> 84f4d357068951ea20c7aca4c7ebd016497cdb6848fff80ba08461e4f77a2d63
~ _cache_key_is_equal_cb_cstring : sha256 75761dd067c8181f9f13944ce7bb369d6eeed96189cad063ba509d9856638b17 -> 9643c57a730b66a95c4a62065134a7d872758aaa9d5f8efc496e962e1d403abe
~ _cache_key_hash_cb_integer : sha256 547ef1e6ebdc6c8012f2898aa7c2fd000f0dfc86cbe38c0b15f3bea36e3c74ac -> 60cc02997623ced640da2e8b108854d623dff81d33c5776560f468b972b367c2
~ _cache_release_cb_free : sha256 1a7eef1ea8faadf482d1893ea07ccb1c9e10e3d20f9fcc7c7c44caa14afe7b6d -> 1b49615bd836ebdaf80459ae6d61f554252ec0ba78674cf7a494315b24c65272
~ _cache_value_make_purgeable_cb : sha256 a23703fc4e547291d9e5c0dc2d7cfd107ea5149bec5d80cc0c774b7f458f9a02 -> 627f3cd7f53141732001f777103bdf8861b4244b7dad08cad320366775013e33
~ _cache_value_make_nonpurgeable_cb : sha256 41ed2ff7aa110c8ecd4d231e240f3cc50b114717ef562c09ddd765bfc718adce -> c4f2c6d9b5c64ac669b2a47c7084fc4873fadfa01ce9f78561a030274933160a
~ _cache_hash_byte_string : sha256 366a0989d9a7d25b578cfaede37ce38de1ed0f9b584ab70106f85980d681ca91 -> 51cb4c3a55fcc900b554a8a772b630a2bb06f063383cfb30d235dff598c2595b

```
