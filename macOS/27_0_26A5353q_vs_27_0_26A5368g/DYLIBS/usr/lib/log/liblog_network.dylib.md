## liblog_network.dylib

> `/usr/lib/log/liblog_network.dylib`

```diff

-6681.0.372.0.10
-  __TEXT.__text: 0x188c sha256:53ff2808be19288820acdb9224ee79bda83700572d385f35f6a0a3c5272a689a
-  __TEXT.__const: 0x58 sha256:ae1e47cc6f849d16b6e715a57351c0c448713c328b51ae1382c1c81d82c60a47
+6681.0.436.0.8
+  __TEXT.__text: 0x1874 sha256:e6d25ded048fe3acfab6c760e7b33b774b74d866fecc8d471ea1dda31eb521a3
+  __TEXT.__const: 0x50 sha256:6a0e427802d879605441a9fef68d59757fa9043d340361b8574181336da07532
   __TEXT.__cstring: 0x2f7 sha256:94ef7f4f90389e72e1cd2cdbaf9666e014bb851dbcf4f1cc30b77a173f9808df
   __TEXT.__gcc_except_tab: 0x54 sha256:cfeb2b3076f6c6b21eb66897d64bb188724911366c2df8b7dd1c479c9eef9304
-  __TEXT.__unwind_info: 0xb0 sha256:9c646b9263e06ebad6a54c16c782521b60b3cd54a7188d9d24d4b9e52a0e0e53
+  __TEXT.__unwind_info: 0xb0 sha256:8552ff13e7913b8a563e8edb4bd4211160dc54838db801b40f96127f390a4267
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0x90 sha256:21ea85fea7bbe76038198c3381ce841815b955c365a149dbd6166c5f1b37b67f
+  __DATA_CONST.__const: 0x90 sha256:19bc1ceb1f76933a02ec159ccbab10516a7b60c709806bee0615d85307763a1c
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x60 sha256:089a94d49d305539dbc25fad838b32a05f4da49334424abdaf6ffaac23431124
+  __DATA_CONST.__objc_selrefs: 0x60 sha256:a544044b4ddb2e7f5ffc55da180bb6dbaf613ebcde337117b99c39c6807de62a
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0xe0 sha256:ddff68a78d7fa50dcdec644bb2adbf1d843f0823b804115e0eb3ef79c3422706
-  __AUTH_CONST.__cfstring: 0x380 sha256:dc559bc6e954c719db6ab433b40491f4ddd3950a30a61a931145b402349a86e5
+  __AUTH_CONST.__const: 0xe0 sha256:715a093e8e7c73dba728b9c6ca8bb9c1181e282505a1e759b5210b3d20aee37d
+  __AUTH_CONST.__cfstring: 0x380 sha256:a6021fd44b767c2fb8bd1e128a1a8a2bd27a0a9d59341fa5e9c023ba5cf5bc1d
   __AUTH_CONST.__auth_got: 0x0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libquic.dylib
-  UUID: 507E309C-39F7-3D89-A5C8-91DA037D4758
+  UUID: 4EDDCE21-DD5C-339A-8E82-FC0DA0A7D23E
   Functions: 15
   Symbols:   65
   CStrings:  90
Functions:
~ _OSLogCopyFormattedString : sha256 f9d9d5589c6354be080cabbaa90dc73b72ab7335a2a6c1ee99a1b0be1c4bfaf6 -> fa366d87a65097d68e7f6f93bafdcc601d921e43bfa656241207eb3803d07a2d
~ _NWOLCopyFormattedStringIPv4Address : sha256 5cd56d18733c52b008f6142bf0387888b4888f011906f19b750d3560bede61c3 -> 9165df351f8776145fe97a42de8fa99b63585d6f3dba796c85a8b9a963c7e368
~ _NWOLCopyFormattedStringIPv6Address : sha256 7049c0fa90c1dffa122824a84dcd4bc90396a3bcfa188d71b2c8891e3779b537 -> 238e1d7520d91e2eb6ea085624ef89103a289a605fbf52aef8f235b6b6e7f4dc
~ _NWOLCopyFormattedStringSockaddr : 1436 -> 1432
~ _NWOLCopyFormattedStringTCPFlags : sha256 6ab2a80d0586deb88570de435042a1c4c4fcd25f22cc9a9ff7f920af27ccd7ab -> 4fbf733d2f251da764d69e6731f424d114a95bbca825cb1cc37ca9fe3a6a16cc
~ _NWOLCopyFormattedStringTCPState : sha256 fcd9a703c5ea09afff0c50f42897864a3e408f4a3c613b6abe2c9074a8b8d864 -> e1279fea2c028806d4866d136a4b99cf45cd6c2a4ccedfae5b0d7780e77eb23d
~ _NWOLCopyFormattedStringTCPPackets : sha256 f5d2b4cc44b6123dc2aa1c808302ebb31367f6940772778418f3fc9b0a67cfea -> 06cf083b5a2fa44ac2b03834bd2cd9270f74a7bd643870c8c54464159c2ab39b
~ _NWOLCopyFormattedStringQUICPackets : sha256 4745641777552378afccbd60393143cf0b6666a9d394564b557ed74e21473230 -> a0a6923b1a4ce6f9f4d09055d829e327d748bcd6ad4e0e3d882be9c245fbfb19
~ _NWOLCopyFormattedStringData : 724 -> 712
~ ___Block_byref_object_dispose_ : sha256 b3a3fba8dae8e63930d3c2060883eb4c15e4d689780e2db16554fe323169f770 -> e1dcaaeb378ce3b394737f0882d2741b1d6eb41cb9c59e7a9813360d47d789d5
~ ___NWOLCopyFormattedStringTCPPackets_block_invoke : 628 -> 620
~ ___copy_helper_block_e8_32r : sha256 39afe7037a5ae46bcacdfd96f70745b2f3f22fac9f0726862294179e5f858c42 -> e92ebf00bce3b3730a7aaa65ab6e8106778969763207a34fca635645ddf90b2b
~ ___destroy_helper_block_e8_32r : sha256 33764a791f126757124df1db6914713ac8d542974274492ced07c1bb0ad89ac8 -> 54a5b3a37a36b058cf1b6ea20db04cc1ac7724c41fd0bf6dbdffb6e4646c091d
~ ___NWOLCopyFormattedStringQUICPackets_block_invoke : sha256 5629089ba232324595e26615c8d9a04ba9bbe1cb13b5d4e32a2512a3deb4e9d0 -> bd4882532eda3d94245a736cb7e3a17a28aea946eeccf447b41a1963efa2c80c

```
