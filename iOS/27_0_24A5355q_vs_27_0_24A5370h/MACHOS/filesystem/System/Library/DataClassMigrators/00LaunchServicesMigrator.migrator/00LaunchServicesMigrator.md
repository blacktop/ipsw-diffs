## 00LaunchServicesMigrator

> `/System/Library/DataClassMigrators/00LaunchServicesMigrator.migrator/00LaunchServicesMigrator`

```diff

-1498.0.0.0.0
-  __TEXT.__text: 0x724 sha256:c5ad6192c93137639daad2fee730c5156322360d67ef681fdbfd6897e4a531d9
+1504.0.0.0.0
+  __TEXT.__text: 0x720 sha256:26a477525d051563b82299cf95303d7cb0b083069847106a7bb5d70cc6f40a61
   __TEXT.__auth_stubs: 0x100 sha256:ca791b657a7711425113ec02b3bd6c787eef531f211dbbda011a30db93f6c941
   __TEXT.__objc_stubs: 0x2e0 sha256:72eb0a212ec12e961b29aaa0bdab3498020aa453c470b9d7d56d81d58b9372f4
-  __TEXT.__objc_methlist: 0x68 sha256:28129afb7c0fae6f72ea24a4aeb62a5bc1bbfc02ea45cf03beac7763e4dde84d
+  __TEXT.__objc_methlist: 0x68 sha256:b4d223e1720a3ad3e6a360b846abf27e16c3c8d8fc68b3dbccef123905f20126
   __TEXT.__const: 0x60 sha256:c18b35e03139901b9404dc564180d0204b02f785116e5a9e5bb8f14714cd4640
   __TEXT.__objc_methname: 0x2bb sha256:8afbb894e9f5135556af5811f4f8b2261b44808e1ba9c71ebe6c4f3ea1dd9b24
   __TEXT.__cstring: 0x5b sha256:f804a50975bf46bf8c5362474fc5b43aca2f0eb933805368d76f2c7a7495ba12
   __TEXT.__oslogstring: 0x2aa sha256:a9a9c20871a8afc0857395d81a8ed2b453c50b1b12ae67404342da1a6a169760
   __TEXT.__objc_classname: 0x13 sha256:2842e228a041e9e2d6742cb65defca55350327bcff29f38d2239259653c8f7a4
   __TEXT.__objc_methtype: 0x18 sha256:6404870a6dbab538b4bdad51c08745b53e39f57fc4e93f7b87c1fbbc52729c46
-  __TEXT.__unwind_info: 0x88 sha256:b933eaf2bec3de8807c6e63389e36962a91219c27aa79c2a468ee49277ec807f
-  __DATA_CONST.__cfstring: 0x80 sha256:af840b063c6f52555476a2e9ed36aa2e3229e1e674b6ac8ea5211f8b92cc2c12
+  __TEXT.__unwind_info: 0x88 sha256:e05df65c828514045978d190f43c6b7bc1dbfe32eea7a6a835153afcf50cd7ac
+  __DATA_CONST.__cfstring: 0x80 sha256:322d1ecd7a570f1536c4e21ae4cb169b0a7c5333950ee4fce67b49108d0ad7ce
   __DATA_CONST.__objc_classlist: 0x8 sha256:0a60d9d82c3303c364b5090eefb71a8da0ebdd9f25d2dcd0294deeec467fea62
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
   __DATA_CONST.__objc_superrefs: 0x8 sha256:438cf79430e7e7f81bcdd72df86bde8f1cefbb52239c942f0736d9a88fb040fe
   __DATA_CONST.__auth_got: 0x88 sha256:5379588d64ffd389709190bdc3a806492011d076aca63e0d31f4bd7307efffa5
   __DATA_CONST.__got: 0x28 sha256:3caf782f45589287ea0cbfd86ef554b8204079b709fd4278325a718685f41b28
-  __DATA.__objc_const: 0x90 sha256:5c764b54617b7e14c1a37b27d48409774fbf811d98224306d3321ec64a9b37b9
-  __DATA.__objc_selrefs: 0xe8 sha256:48f7cd168bb75ea3bb56feedaf9eca828d93f064cfef3ed93a986762d266055d
+  __DATA.__objc_const: 0x90 sha256:51f69fcfd2882f44386045dcad5fbe6da237a16ff54e301937740aa535d1d15f
+  __DATA.__objc_selrefs: 0xe8 sha256:21ef0d1c0e60a9d28ebcb685b957ee620e1f2d1e5c27b1424e2ac83ea15bec54
   __DATA.__objc_data: 0x50 sha256:faac870c41ae2dcca93efcd45b927347495be9ae3a0fd43955cb1d4f02ef2e84
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 21DE9582-2CC0-3724-919F-B6CDFDA11D1E
+  UUID: 856AEE52-80BF-3747-A3CE-DCB149D09404
   Functions: 9
   Symbols:   32
   CStrings:  49
Functions:
~ sub_a80 : sha256 7f63f97405743e98954d149beace952c29d76ab82d441ce21248f6fbcdff2dce -> c4ececbf6b6974e57eae079fe7b6813ceafc37aa73734a101b1aead0e0130dc3
~ sub_ac4 : 532 -> 528
~ sub_cd8 -> sub_cd4 : sha256 995d17a63000d226edd2961b2ba24e720024e16c0ca614620457f8c5ec818230 -> 48f96ce0592046db44da1503f8d062f050439c0dfd694eee9383a7a1d6d8fc6b
~ sub_fd8 -> sub_fd4 : sha256 f813d81f46ea223b016ddba3fcb7fee361d3623664636e701219d54e137ec4ac -> 699ccf08c4b2c7d50d09ab5c81357e7ad83c5d14f6c2b1775e393d38b109568c
~ sub_10cc -> sub_10c8 : sha256 d7724db7458b711e0beb9f864469089b4dbf7ec25cf92b1e307012cc16c29087 -> dc85809900e98ad4685f309082753ace97129fac66a79fa313a5643eedb7a8f8
~ sub_1160 -> sub_115c : sha256 97e8f09096870fa3faaa0266996c999a6d4d3967e741cc3f8e7b581fcb60e3d2 -> da8551601abf32a5ec05c2c75a8bd63e3d23a8df6791f9c125d0a7f0dcc238a9

```
