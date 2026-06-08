## 00LaunchServicesMigrator

> `/System/Library/DataClassMigrators/00LaunchServicesMigrator.migrator/00LaunchServicesMigrator`

```diff

-1444.5.2.0.0
-  __TEXT.__text: 0x78c sha256:1a5d4c8ed6bba80bea9f92ae4d733f090a17b21051d028ce5586cff011f9b6dc
-  __TEXT.__auth_stubs: 0x100 sha256:c9f3ad595aaa1b1ad846dde26e18403f6c192d73039c5a5e234318e3c544296a
-  __TEXT.__objc_stubs: 0x2e0 sha256:618821e77a6ccf63733178336b5aafd91455dc15fbd400b54a629da99a08f4cf
-  __TEXT.__objc_methlist: 0x68 sha256:312b7119c563096eb020b99f3449398a77451321207f64053f8c8a1501490dbd
+1498.0.0.0.0
+  __TEXT.__text: 0x724 sha256:c5ad6192c93137639daad2fee730c5156322360d67ef681fdbfd6897e4a531d9
+  __TEXT.__auth_stubs: 0x100 sha256:ca791b657a7711425113ec02b3bd6c787eef531f211dbbda011a30db93f6c941
+  __TEXT.__objc_stubs: 0x2e0 sha256:72eb0a212ec12e961b29aaa0bdab3498020aa453c470b9d7d56d81d58b9372f4
+  __TEXT.__objc_methlist: 0x68 sha256:28129afb7c0fae6f72ea24a4aeb62a5bc1bbfc02ea45cf03beac7763e4dde84d
   __TEXT.__const: 0x60 sha256:c18b35e03139901b9404dc564180d0204b02f785116e5a9e5bb8f14714cd4640
   __TEXT.__objc_methname: 0x2bb sha256:8afbb894e9f5135556af5811f4f8b2261b44808e1ba9c71ebe6c4f3ea1dd9b24
   __TEXT.__cstring: 0x5b sha256:f804a50975bf46bf8c5362474fc5b43aca2f0eb933805368d76f2c7a7495ba12
   __TEXT.__oslogstring: 0x2aa sha256:a9a9c20871a8afc0857395d81a8ed2b453c50b1b12ae67404342da1a6a169760
   __TEXT.__objc_classname: 0x13 sha256:2842e228a041e9e2d6742cb65defca55350327bcff29f38d2239259653c8f7a4
   __TEXT.__objc_methtype: 0x18 sha256:6404870a6dbab538b4bdad51c08745b53e39f57fc4e93f7b87c1fbbc52729c46
-  __TEXT.__unwind_info: 0x88 sha256:7d604055fce4284a7832cd48a6c4cfda050ca27ea46857ee07acc56ff218744a
-  __DATA_CONST.__auth_got: 0x88 sha256:27bbfea54df58c994fa4191004e52df860cf4496314efe05d61041304212be4d
-  __DATA_CONST.__got: 0x28 sha256:318f1f51be17b75115bf31d5eb6d7802a6cfe5f0aff881519ae46ffeddac347d
-  __DATA_CONST.__cfstring: 0x80 sha256:13432c4c7a2fe0c4d45c02c2138ec082441bebdd157e447f6d5894a97f33c950
+  __TEXT.__unwind_info: 0x88 sha256:b933eaf2bec3de8807c6e63389e36962a91219c27aa79c2a468ee49277ec807f
+  __DATA_CONST.__cfstring: 0x80 sha256:af840b063c6f52555476a2e9ed36aa2e3229e1e674b6ac8ea5211f8b92cc2c12
   __DATA_CONST.__objc_classlist: 0x8 sha256:0a60d9d82c3303c364b5090eefb71a8da0ebdd9f25d2dcd0294deeec467fea62
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:1fa65ffcccc24c72d5d7f804a2be05ae57dfbb8769ffb33c4272ed6795b7e61c
-  __DATA_CONST.__objc_superrefs: 0x8 sha256:dd142257871d35bc029c57d79f238014b97bb05539bf35ba6bea4836918fa8ea
-  __DATA.__objc_const: 0x90 sha256:699279c9c820ae3b2ec6984048320b1fce4f68c46ebcb9bc19fdb0c5abb09e44
-  __DATA.__objc_selrefs: 0xe8 sha256:b662f4310548a9b27ee04194a25a79d6622fa3144cdb3b2e3569725fb45dd462
+  __DATA_CONST.__objc_superrefs: 0x8 sha256:438cf79430e7e7f81bcdd72df86bde8f1cefbb52239c942f0736d9a88fb040fe
+  __DATA_CONST.__auth_got: 0x88 sha256:5379588d64ffd389709190bdc3a806492011d076aca63e0d31f4bd7307efffa5
+  __DATA_CONST.__got: 0x28 sha256:3caf782f45589287ea0cbfd86ef554b8204079b709fd4278325a718685f41b28
+  __DATA.__objc_const: 0x90 sha256:5c764b54617b7e14c1a37b27d48409774fbf811d98224306d3321ec64a9b37b9
+  __DATA.__objc_selrefs: 0xe8 sha256:48f7cd168bb75ea3bb56feedaf9eca828d93f064cfef3ed93a986762d266055d
   __DATA.__objc_data: 0x50 sha256:faac870c41ae2dcca93efcd45b927347495be9ae3a0fd43955cb1d4f02ef2e84
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/DataMigration.framework/DataMigration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1A1CDF1E-986F-3A51-B903-C06CDD8F9709
+  UUID: 21DE9582-2CC0-3724-919F-B6CDFDA11D1E
   Functions: 9
   Symbols:   32
   CStrings:  49
Symbols:
+ _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleasedReturnValue
Functions:
~ sub_a80 : sha256 5b53220fc1b07869b6dda983cdad32a2a296f5a910b2fa5cfd04ff35c84482ec -> 7f63f97405743e98954d149beace952c29d76ab82d441ce21248f6fbcdff2dce
~ sub_ab8 : sha256 5a466983a4ab2979020b38df8581f44e9b9bfbf0dea3b4f1f7d1c1326c7ac6de -> 58375722e0b9bd0fa3ba04cf3fe639bf704a7abba855e7264b75c6fcf6ff4b8e
~ sub_ac4 : 548 -> 532
~ sub_ce8 -> sub_cd8 : 844 -> 768
~ sub_1034 -> sub_fd8 : 256 -> 244
~ sub_1134 -> sub_10cc : sha256 e4be193dca768b1cd00d745cd90a3e3524fb2fa395bdf1aa49cd9fb0d710b06b -> d7724db7458b711e0beb9f864469089b4dbf7ec25cf92b1e307012cc16c29087
~ sub_1174 -> sub_110c : sha256 23d2038a27164a3bba16a93d0bf3018cb17c126ecbad24b792dc66f013774527 -> 220df07ad62f239e083f548feaacafeb0d174b6cd13267364e21b3219db058c1
~ sub_11c8 -> sub_1160 : sha256 cdcb85898503bbcaa0473bdbb4fe0619cca0e3853f1116849d6bc77a08e1f970 -> 97e8f09096870fa3faaa0266996c999a6d4d3967e741cc3f8e7b581fcb60e3d2

```
