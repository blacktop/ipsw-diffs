## WatchdogClient

> `/System/Library/PrivateFrameworks/WatchdogClient.framework/WatchdogClient`

```diff

-333.0.0.0.0
-  __TEXT.__text: 0x1350 sha256:e8b605c7fe725e7312f07cc7ffc017f792bf3df95ad7921366f1cc2efd0119cd
+334.0.1.0.0
+  __TEXT.__text: 0x13a8 sha256:8d841f41d1d1d8c8cb820011fa8f792e48e63a68b05805c9850f4011af53dda7
   __TEXT.__const: 0x8 sha256:3e990d45c83fa01d9bf0c64b79ed7678df3c723614f0f7eccdc3d196fa3073e9
   __TEXT.__cstring: 0x13e sha256:d31a2f1564f2b06082b1344da12ba4c2fbe525d5e89d0e151eed4a19c6f15f8e
-  __TEXT.__unwind_info: 0xa0 sha256:c7472d5d1d49715c43ab56d951e5f477c24c2ce01e3f6e1c75c9ad86da6e15e1
+  __TEXT.__unwind_info: 0xa8 sha256:298fcb90252d1927a586d25cf6ac09ccc48a7ac3f0bebf4a679a078ba72c6257
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x60 sha256:e638604bc8376977f1745b3227e5c251365da888eeded002775b2c3efd6864b7
+  __DATA_CONST.__const: 0x60 sha256:1321c1b62f2a0c912651e6590a2dd0820175bf7ceaaf3efbc8172f161f29cbdd
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x48 sha256:cf5a5c27d4898b8fc13919afa330824ce883462aecd39d4dd544058b1ba273d2
+  __AUTH_CONST.__const: 0x48 sha256:9a23d789097ddff362817417d8c10fb28c46831d8edc615558411d711f690967
   __AUTH_CONST.__auth_got: 0x120 sha256:2d5565fb483d8ea4525a7a9229677d1038ad34b6e22c8d5152e1d7f7b9817597
   __DATA_DIRTY.__bss: 0x388 sha256:cc401ce5099578287fd15c062a92893754851bdb7ca3c1fe742bbff85e2281c2
   - /usr/lib/libSystem.B.dylib
-  UUID: 7F430F3B-5136-3E07-81C8-8A0CA13F915A
+  UUID: 13B13281-3846-3DC1-BBC2-911C66BE389B
   Functions: 21
   Symbols:   162
   CStrings:  11
Functions:
~ __WDOGClient_PollIsAlive : 1300 -> 1328
~ _wd_kickoff_ping : 596 -> 604
~ _wd_server_handler : sha256 4c0913d3a3dd77cb68fa9c0327728efb9781b9e5e0cbe059f6c7912d6c7bd90a -> d9ff833cdaeebe5c638b98b6f3e8b76c24918a05162d414e1ddabf28441504d6
~ __XPollIsAlive : sha256 4c5e5372d57452f148ecbb43375f4a6f5f087cc0b441e8dc84027cb2e08e4f26 -> cfc009cc5f3471adf32a6d01846d764bb576e4cbad6f1d046d052633d3dd99ee
~ ___wd_kickoff_ping_block_invoke : 72 -> 76
~ ___wd_kickoff_ping_block_invoke_2 : 76 -> 80
~ __WDOGClient_ReplyIsAlive : sha256 ec3f5dab19c1053e571cbbc99602759b93a4e4788d069b15fe168426ac5df5ff -> 756fc89ed630945ccb747aa714e51b48b75414fff2c191c153f21491d62ce799
~ _wd_endpoint_register : sha256 6ba3faadec6fad53f411dd2c9c68254163478b410d73c2ab844c7168f3b78099 -> bc6a28aa1cebbabefaa6c5009809da020b082e27187f894e7360d23f440f1d9c
~ _wd_endpoint_add_queue : sha256 7bd1b8e64490cc92d0959930f6875bc131c4338130e26c2edf33fc4d62aff17f -> fab19220dc9d5752921c538a740e387f1cd75554f0677eb8adf7c2cc47528a7e
~ _wd_endpoint_add_work_processor : sha256 21ef8eeefb83a7bfd60cc88458c77314c342d779bbffaf92e424a65db1606e70 -> 4547b4ba6025fa1b42628a0cb5cfc6ad6af3b81c4bf39f77624cc78594345e56
~ _wd_endpoint_add_work_processor_block : sha256 a15555687fcbd72dd4c6f0ee9b88bb74211d22ed444e769234f41c682d826735 -> 9e2e6b71e10a2cb0b645fb382243c22d4225c4d56bd97fbf5c566f33619d1371
~ _wd_endpoint_set_alive_func : sha256 0cf0a9743d32e936047ea390cbcbb024007dbe353cbc010d543e30395022e3ae -> 5bae921f249cee445170883906ef6486dd09bfba60c38cd91263e16a24b087b8
~ _wd_endpoint_activate : sha256 83ac829e068d97bc78f9790836c4422ebd1419d762235b836def563f6a2f4cd8 -> 480e567fd231335d9f088ad4b23119f49cc0e3eaee7e02c3ff887b5ff01bd93f
~ _wd_endpoint_set_platform_controller : sha256 06739e358a7772ad6ff463a35b024128c2e29ef1709f603e0d4b50441a226151 -> f517df9c1d500e390395117912b31b5b6912824261b4f51eebde1fd60ff70d06
~ _wd_endpoint_begin_watchdog_monitoring_for_service : 316 -> 336
~ _wd_endpoint_disable_monitoring_for_service : 212 -> 232
~ ___wd_kickoff_ping_block_invoke_3 : 76 -> 80
~ _WatchdogServicePing_server_routine : sha256 3f4cb9909fdb316b730dcbba41e4b9a605900b8ea40d7ce0917d0d274c278d75 -> ec8c5084f8680c96752570cc6312b5803392b188b18fe48863389cd4d48b6807
~ _WatchdogServicePing_server : sha256 57534c4b58d76d23e9163d5166a12d5e4acc6a146a27b961cc9eca459ce77be0 -> 8b307e1e7b42420f6ee20fcbb380a21977ba67349c145779a747f1263d771753
~ _wd_kickoff_ping.cold.1 : sha256 f8ad0343aab4cc1c1e67d81ce3e2eb17fbeffd5d84b676cd44a75572c72b3f49 -> ddba1d2b4393d01b79d1898d8b0a7f03868c1484eb0d530d42a5497e743595b9
~ _wd_server_handler.cold.1 : sha256 ba5e5cda4a7f96d29eef739da9dd4b588d84a00a978863498362af97e1b882a7 -> aebe48e2199d5125efed471e373d698fa9cbbf70a7777c9aa4bacbf428816fe4

```
