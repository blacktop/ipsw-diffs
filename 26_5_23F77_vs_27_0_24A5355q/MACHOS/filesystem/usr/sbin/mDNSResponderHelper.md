## mDNSResponderHelper

> `/usr/sbin/mDNSResponderHelper`

```diff

-2881.120.11.0.0
-  __TEXT.__text: 0x2ef4 sha256:9e81ada195af2629c13fcc1f2ba220d682e1e2d1368641e9c577a1eb99663551
-  __TEXT.__auth_stubs: 0x460 sha256:a8c9c3a7bfc379ae18dddbb71057f7812fcb3cd9bb33d44d8d55b9bb1a646d45
-  __TEXT.__const: 0x151 sha256:5d27ccddbbe9630b73b656c1ecae26b10f8c52ef80381890af222d3ac47daffd
+3066.0.0.502.1
+  __TEXT.__text: 0x2e78 sha256:99b3a80a6c65ef85a2994e40a4ee26eeff4cec5dc9eb7b3fd91677324412b5c3
+  __TEXT.__auth_stubs: 0x460 sha256:51215e256a3675d73f0a919fc60f3bdcaa2a7ff00142122a9fc8f3698feb380d
+  __TEXT.__const: 0x158 sha256:3726b3ab48bd92ef684f14a29828222351c76c1242527c0484d37ae2c39fe5ef
   __TEXT.__cstring: 0x2e0 sha256:782e4afbf74e9c4d504eb557bc17f7ba58059b4eeb72fb6c269d505a3a4993b7
   __TEXT.__oslogstring: 0xce7 sha256:cb5bb434c2e52e6ea9395c9bd727f7a371f88aa2b5952a2c05b67d002aaaaffe
-  __TEXT.__unwind_info: 0xa0 sha256:81c6f8306da17749b142054e0e15b8625216f02c6412681a18af099fc07ada10
-  __DATA_CONST.__auth_got: 0x230 sha256:ed6ce869d3baeac21c495050e46cefb615f9e0e36b14e9a9c8b47e80903e4cc5
-  __DATA_CONST.__got: 0x70 sha256:fb0b60ca1aedeb0f04283abe97d6956b7b69c999dbb1c81030db238a523d082a
-  __DATA_CONST.__const: 0xa0 sha256:7d78b2510a8e5a49e34a8b90e9aa491689aa957949606b27b554af1edcc08180
+  __TEXT.__unwind_info: 0x98 sha256:744aa610fc6e7fd357a767effd435dcc39ed82f7f508039f59f455c0e00abe28
+  __DATA_CONST.__const: 0xa0 sha256:ff423ad486f1526e490f3519933915ca285d3fbbc0d4df497e43d43361b3f2b7
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
+  __DATA_CONST.__auth_got: 0x230 sha256:0895dff6ce1fd624f0ac53bcea25ec358d61ae26abacd2684dda1d7a5d32329b
+  __DATA_CONST.__got: 0x70 sha256:4a76ddefec3f9071bff74872d0f40688cce952dbd962f34cdb05121e27488973
   __DATA.__data: 0x18 sha256:4c9287d23b7a1cc25b140602a87333d874b37b852e9e056e3ecf0f8b4252c371
   __DATA.__bss: 0x40 sha256:f5a5fd42d16a20302798ef6ed309979b43003d2320d9f0e8ea9831a92759fb4b
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CAC1D860-4B9C-3F00-AC84-FB78395BC402
+  UUID: 1BD9AF9D-4B24-3632-A368-B9D0A66FDE01
   Functions: 16
   Symbols:   130
   CStrings:  98
Functions:
~ _mdns_bpf_open : sha256 d4bb02398e8fd142df6eef7d5063a0fde8253781e14e6c9d75159554058f0b93 -> 9cdb6a4bb00932e9aa1cae736463953c9345651d2960168bbf8ab065d15f09fb
~ ____mdns_bpf_log_block_invoke : sha256 f96a7abdaa5247be561cc7bedd199037ab95c73c9dc5424b4235fd5a56f29738 -> ba3a12b605be8ffeadd8c032940165ee04b634f8fe8fd64e7434c6d0ab609d7d
~ _helper_exit : sha256 b9b6e196060ae78a506e3d182755420e96f609c59773be2be2bf460318fe741c -> cb38e60372f5ca244c537670991a24adcfdd0a95105d3a4e1d433ee54d51d9c2
~ _PowerSleepSystem : 196 -> 152
~ _SetLocalAddressCacheEntry : sha256 1861cc583b4e719ff4e899461b70f984f0851345f6f033da36215ab1f1430d9a -> d2c2da0d9f8a18888d7ad78e8005c8ccb7e7d9921ffe217c92ea720fc8fe030e
~ _SendWakeupPacket : 1176 -> 1184
~ _SendKeepalive : sha256 5c09e848dc0ec576afe92b4cf893255b4800754fedb20945da8a7953ebeb86ea -> 17099166d1e917ffea571ed6749bae26fa5529be6519f87ec09ef6b4d5f2c4ec
~ _update_idle_timer : sha256 c5e5ae97ea84077597b8be02cfe396f2d39bdd8d87f07740e3ece14c5bfa3c8e -> e6c62f3684917740504571627606d7df26d0c5d7621827b67f48e544821209a3
~ _main : sha256 2c9e3606e9993f22e131177aa703e9b8bcc2d68af17058c647799031b5a6e03f -> 82aca723d60b67ee69985341014c2ad80fd995e57f4d31377430bade9f97e7f0
~ ___init_helper_service_block_invoke -> _handle_sigterm : 768 -> 56
~ ___accept_client_block_invoke -> _diediedie : 2264 -> 268
~ _idletimer : sha256 70b27d8cb9fc236e26fa9fb7779494da5eaf7a6bad9c56ba8cadf44d55427123 -> 01d40d206ed8e3a0761089a29c0d79e0a3d2576e64b37ac55d0073de3a7d2857
~ _diediedie -> ___init_helper_service_block_invoke : 268 -> 724
~ _handle_sigterm -> ___accept_client_block_invoke : 56 -> 2220
~ __mhs_handle_set_ip_forwarding_request : sha256 dad6e615dbea4bdd70865307b180a25dc8ea230af38dc413a352bc38f30d99a4 -> dd6e4418ff0a7bf7569febf3e507a336e57c52fc77a9c6a6387c4a18361b0b1f

```
