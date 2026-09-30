## WatchdogClient

> `/System/Library/PrivateFrameworks/WatchdogClient.framework/Versions/A/WatchdogClient`

```diff

-333.0.0.0.0
-  __TEXT.__text: 0x1354 sha256:3822ed538aab19b810745fce9d6c872f6fd6dd14cdeac7152ded94e1a9e6a407
+334.0.1.0.0
+  __TEXT.__text: 0x13ac sha256:a0b9edde3f338d7605c3ad275067b3b11ad264d14dfa0e01dc42abf557b57e38
   __TEXT.__const: 0x8 sha256:3e990d45c83fa01d9bf0c64b79ed7678df3c723614f0f7eccdc3d196fa3073e9
   __TEXT.__cstring: 0x13e sha256:d31a2f1564f2b06082b1344da12ba4c2fbe525d5e89d0e151eed4a19c6f15f8e
-  __TEXT.__unwind_info: 0xa0 sha256:b63ebeee4aec1eb250c4598d8867d29e6712e2fd4db4be2de7e7f1e388942f7d
+  __TEXT.__unwind_info: 0xa0 sha256:5e82cbcc6f9bd3176cc9170a08115c2f95970f1e36daa899fa85eca3e151c33d
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x60 sha256:25ea326e419de501f153ec2263743bc064968e050f114f09a126b94cbb7d86b4
+  __DATA_CONST.__const: 0x60 sha256:e240234e3130230344c6c9db6f692f8fedd3eea90ad10259a45b3ee70b3fc023
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x48 sha256:29103688e726e3e0f0a917cb768e8970e2ec7ecf4ae25b20d1ee8189dbab8598
+  __AUTH_CONST.__const: 0x48 sha256:98de7a7b28f33dacd1370e7e713c2c07f18f78a8e49757bf76de9b655fa9432a
   __AUTH_CONST.__auth_got: 0x120 sha256:2d5565fb483d8ea4525a7a9229677d1038ad34b6e22c8d5152e1d7f7b9817597
   __DATA_DIRTY.__bss: 0x388 sha256:cc401ce5099578287fd15c062a92893754851bdb7ca3c1fe742bbff85e2281c2
   - /usr/lib/libSystem.B.dylib
-  UUID: C5F255CC-D1E6-39BF-8EBC-2E4D7C6D7EF4
+  UUID: 9C655157-C626-325D-B069-CA82F8F65EEA
   Functions: 21
   Symbols:   109
   CStrings:  11
Functions:
~ __WDOGClient_PollIsAlive : 1300 -> 1328
~ _wd_kickoff_ping : 596 -> 604
~ _wd_endpoint_register : sha256 5bf92c44d5c9b3f4c1614d40556117094a9f2c37d0b675da3b0cd9a200b42646 -> e2a8e59862cd9aecde2073119b50062933b227c6ad157cb0b115cca1dbaf2453
~ _wd_endpoint_add_queue : sha256 8301bc350e6ca63f3838778975c1a5e99a178841cd698a1eff11556c32124166 -> ea52b66847629f43c7494e56a69b54509879cc90e2a321cea1c70a8eb6e14909
~ _wd_endpoint_add_work_processor : sha256 9b275a56bd78dd145f17f5c95e1e53387ece0fea5ca4c9d9922bce91ab843237 -> 0380dd2d014d8299c448f3029dcf503d778427f084d3943b85c08b302a4cf229
~ _wd_endpoint_add_work_processor_block : sha256 f553e1ec28c6043b8753af5c8570782bf527245d8ade317ea73615826e932dca -> 3d330c13453cd43a73ed089a60427ca43f31c89de602bf0f596e676e202564f1
~ _wd_endpoint_set_alive_func : sha256 9e9a5b1957b7a22b80059f386a002f505f241436a84eadac517c4b5d68768cc7 -> 0fc70ab959b3ec1ac4ef669c894cd8fff67686c9d0958f3f439d02483f252a35
~ _wd_endpoint_activate : sha256 c9cd3874a13069dfdaed64b2e4d9e57ddfa95b87b7fb7c47c0b293408f5c471f -> 8f55a528114ee27a3d7db4ac79f4adff46deda91d5516b4dc97f2a85f7283e3a
~ _wd_endpoint_set_platform_controller : sha256 76f8ae26f7d357bfbbea78048d7592170135c7beedfde2f89b95023c7297015f -> af891726c62e5b47605d720493cb3d31a0d9e27cd90323121c8d37484cbcb2cc
~ _wd_endpoint_begin_watchdog_monitoring_for_service : 316 -> 336
~ _wd_endpoint_disable_monitoring_for_service : 212 -> 232
~ ___wd_kickoff_ping_block_invoke : 72 -> 76
~ ___wd_kickoff_ping_block_invoke_2 : 76 -> 80
~ ___wd_kickoff_ping_block_invoke_3 : 76 -> 80
~ _wd_server_handler : sha256 0b0ee747071a379c54cdb654f9c70618a2eee5114f10f86384bcd60f6ac3e061 -> e526de3773e87fa847e1e561f2ae134ec1b0c33b2fed5218283d49e8017e1511
~ _WatchdogServicePing_server_routine : sha256 432bd6d6bcc4bef3ff5f114e690c9b4596d7b0d7bb25280e1e657a1c57bdf21f -> c558e7308eef0308c78bcfe767e324fa0164b8eff5a1c4b5bf02c153863560e1
~ __XPollIsAlive : sha256 6499a28d20e63d0433d41f6d4e5fa7a175b34c54b2f0ead4c2b0723d86424657 -> 096105c675fa841667d2a3b2579210ff2abbd3f8ebda976b594c695d81bb73ad
~ _WatchdogServicePing_server : sha256 d89ae3d43668a7aa98545dff794dc970df564a141cdb92b9573f681652eb61e9 -> f30413ff00753559ced76f1695b126f52c64fdad0ba469efb11978a683f116ea
~ __WDOGClient_ReplyIsAlive : sha256 e6bb3666753e77073d151d9b69d2c0091b4cd23823f8290461d6931a5f577bd3 -> 0a9dab2a75d69219f8c078a0bc5debcce80f0c400480375fedfad22e37442fd2
~ _WDOGClient_PollIsAlive.cold.1 : sha256 5249430a143e8dc99a9534638f1e64892c6944ca269511d08b18537e680fdfff -> 9c8a9ea7574c4dafaad9e80f1c79895bf7c7c2fdce516eb9b98e74bbb1061f98
~ wd_server_handler.cold.1 : sha256 b5334a31728a44734cf8ac994915bde77e97628d6fb780b37e23673df68e19a2 -> f4862ea88ac7ab686541599c6cfcd86ab78e3a1d9ad5e54a39a624c96f1a4a0b

```
