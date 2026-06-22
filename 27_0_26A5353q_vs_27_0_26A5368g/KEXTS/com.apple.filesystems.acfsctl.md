## com.apple.filesystems.acfsctl

> `com.apple.filesystems.acfsctl`

```diff

 813.0.0.0.0
-  __TEXT.__cstring: 0x275 sha256:b972a5b3f459b181abde754ed3724368312371453bdb67550ad1ea8aa7fd88ad
-  __TEXT_EXEC.__text: 0xb00 sha256:1eebcd9d29be910d773da7884d8e89e923931e920fff2bf9ad698c66bc41c3bd
-  __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x170 sha256:3efedb6e8cbfac5d1472178722d93b851d0a979105ab25f72b5aa1d38dd67f04
+  __TEXT.__cstring: 0x275 sha256:7495fcecf364cbb41174e3bc2f9e0947ef577567123739bfaa0ab2ba754c9e19
+  __TEXT_EXEC.__text: 0xb00 sha256:56f43616c145bbd27fec5421fe7920d9e06970747bc390329148f28b509e7064
+  __TEXT_EXEC.__auth_stubs: 0x300 sha256:ed4d77910838970dffa5664d6c1296ba7fab79121f661c945506a531545242b3
+  __DATA.__data: 0x170 sha256:700242d0d75b141a4d7c949220253a62835a6aeaab5cfad4798247645608c2ad
   __DATA.__common: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
-  __DATA_CONST.__auth_got: 0x180 sha256:393f7a4dd0420e04a40f92b4b8478ff223fa95610a1740a61d4d7653491db48b
-  __DATA_CONST.__got: 0x28 sha256:aac13979285de8c85dc856fc60063e0c4de35fa847cd5cb0eeac098104c0efe0
-  UUID: B52CBB02-5C88-369C-BD0E-A38AF93ECCC9
+  __DATA_CONST.__auth_got: 0x180 sha256:9ea7b4b189531b40eb49d24add5b155305b4868bfdc657dd291bbdb1c14ffb26
+  __DATA_CONST.__got: 0x28 sha256:8764fa3535636b1ab074a3621ee4ea113da93a8c146aa60f50a298e89e187acb
+  UUID: 5E6281A7-B017-3CC0-92F4-57545F12CCEB
   Functions: 14
   Symbols:   77
   CStrings:  16
Functions:
~ _cvfsctl_kextstart : sha256 af35fbe53d9d6c53110598180c7eab3448ab7da4bc13a7724501181caae0bfe3 -> c421a1b24e53cb9817798ca5af0e1ae7f60448220df0215ef4d96e6ea1d3e7e3
~ _cvfsctl_kextstop : sha256 f5dcef6bb12afb444d28f58f671b6e08accb3cdfeb130f84bc9bd5ac42079bb2 -> 671e775ff88320874e0ac6fb4feb4ff1ba17fba4e9d879f4113d4abdf2070822
~ _cvfsctl_strategy : sha256 8910b40fc6be0696a5b79983bd7d06c54b973a7488202bb141d45b2b7dae82bf -> f639c5dbe17e22f4c3a8782abdea901e599e39aa4f11126fbbcd5cfe1b25b441
~ _cvfsctl_ioctl : sha256 4820206fb8a76dd39dfaf1a3c3557780cb23e0fcd1a04c4a74ff6d127cf022f2 -> eb1f9659dfc5e06539d0fd534bb6fe06786cc894309187433dcaf9b537fde075
~ _cvfsctl_rdwrt : sha256 96031fd742aee3220d0a141992bd29d963b905e231db233907fde0a268ea77ea -> 0dd8fb3854a5826ca0aef279368f5a7a7f8d5ccc6ff14cf8199a8c2a39d66ddd
~ _OUTLINED_FUNCTION_0 : sha256 f52cffac6c129a0f4b8d1d9b777a996f429322914516282e42f61b5cb8832725 -> 416c5a323d35db356556904b78894618b36bf7236862460d1c46f94d170c10ba
~ cvfsctl_strategy.cold.1 : sha256 2fe40231402e1c13f56d3399e6102a3afffc456f7c881595c6413f68b3081405 -> 95eb6b66476e62305748175f3ccd3d768fc1d10f58a1de6f14eb311411cdcc0f
~ cvfsctl_ioctl.cold.1 : sha256 ec5a6b756112725aff2f6687dd43b3f83c0ae1240d9b12cc094e8f502ce5d58c -> 5668198a3f6183c63aa413e07022d3eefedb1e338d82f6d2063303c7e69d3648
~ cvfsctl_ioctl.cold.2 : sha256 a3b1a5bc4d591c96deb1483d79abc14bffbb8b7da9908b3cd8c41fb2de03b49f -> ddd00a34900a141285687cb20df194f9737b6e21eee2589611fbdb57e12d1fc3
~ cvfsctl_ioctl.cold.3 : sha256 c63f9e00b87c0f2fcf8d528387f7ab5f7a20b74869bf8f69b5c3f853f8896f0f -> 177dfbe7bd852b502e220d661ce9bd2f7b83c18b78ff9d5aa8d2288c99458cc0
~ cvfsctl_ioctl.cold.5 : sha256 4e0ed60aaa1b6ce1de160343ed78341686354d6979420420b1c3409f92c1d5f9 -> 8a2d6cecbbbc8f2a26bfc87a21a5bd52ce9c53581b88fc42e56f888d6d11101e
~ cvfsctl_rdwrt.cold.1 : sha256 063c7c72385161370ad3f483a14a1c1af8833a11cded45b4bc441aa8287de62c -> 9dd0da209d38b958d9798199f9cace668b08db5ec8003a0d648cef6446ba8629
CStrings:
+ "/AppleInternal/Library/BuildRoots/4~CR6kugAsAO-Z2xvge2f4o3g9SnrYPGr3zsL1w4M/Library/Caches/com.apple.xbs/TemporaryDirectory.13sYI9/Sources/XsanFS/snfs/client/fsctl/nomad/fsctl.c"
- "/AppleInternal/Library/BuildRoots/4~CQdcugBAe334_ZrQY8Io2Uh2VGCXFZXwara6HJk/Library/Caches/com.apple.xbs/TemporaryDirectory.xhos8y/Sources/XsanFS/snfs/client/fsctl/nomad/fsctl.c"

```
