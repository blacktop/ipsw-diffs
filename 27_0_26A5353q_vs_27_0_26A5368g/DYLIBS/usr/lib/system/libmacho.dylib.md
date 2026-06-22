## libmacho.dylib

> `/usr/lib/system/libmacho.dylib`

```diff

-27050.3.0.0.0
-  __TEXT.__text: 0x284c sha256:d6b9322be8a2b8c7c0e5876a31a29d9a05b75c0640813eebfc67c2179fa2f7fd
+27056.1.0.0.0
+  __TEXT.__text: 0x2958 sha256:5ed03671ffc0197f12f7031ac1341383d5ff57bc9c92b2b8ad090941f7d5b731
   __TEXT.__cstring: 0x492 sha256:23580a7bc73109fe76f608b832541f24ca11bb5ab829bed353daffb4b7cbc09f
   __TEXT.__const: 0x20 sha256:abffbb2c8bf5bbe75c584de74f69b93b9676b0b16e0acd01d5ce8aee99b3260a
-  __TEXT.__unwind_info: 0xb8 sha256:911f96c2b2ceec7a3a104329dba779627c61a93f4dcd84de411ce35e76e303ea
+  __TEXT.__unwind_info: 0xc0 sha256:422382349d858e887125b9ff422854287fb2a41caec5269387be6a5851f924cd
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x7a0 sha256:5929b112396a891587f208a25ae6c12bd996b8ce7b751a38c782f3caccb59f89
+  __DATA_CONST.__const: 0x7a0 sha256:f637ccd37eae40205496fd7210f6455adccd000fbdace848e4c67263b957aa0b
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__auth_got: 0x0
   - /usr/lib/system/libcompiler_rt.dylib

   - /usr/lib/system/libsystem_c.dylib
   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
-  UUID: F41256E3-BC84-3408-8DA9-28AF2C0BA0F4
+  UUID: CA32DB9F-F7CD-3D32-8E5B-924D7A06A238
   Functions: 91
   Symbols:   107
   CStrings:  122
Functions:
~ _getsectiondata : 444 -> 496
~ _getsegmentdata : sha256 1ab0020d0d8844a4708bc62d2bc4f23bdcda21072b3bf53c2e66c0751ca3c4bf -> 3b950e50bc27bc567c666e01eb349646fa7598f267daab837ce5397ab26644cc
~ _getsectbyname : sha256 95c3eeab877b03b4a191eee190cd2bae8c834f868d35181626bc73285f38a0c2 -> 0a79287a93556ce08b36a4bde0cfbd6276964230f3be92cf5590ca6c162f79a7
~ _getsectbynamefromheader_64 : 216 -> 236
~ _getsegbyname : sha256 e6daf53eb79586d2acd5532e0f5ddf13d62a74c7f65a57c7bde08bf2df5b08f9 -> cb7a6eb5604429c0c438bfbaebcd3e4afe7b4233ea4e27fcb89f73a05a13a5de
~ _NXGetLocalArchInfo : sha256 8ae3102a930e3366d68f5b1f9151ae8e38658757885b786e5c26310f4c79c042 -> 4449c6f513a9b989655ab1dd27d3177220aa271c0afa2bc4e7b68a73e1815559
~ _NXGetArchInfoFromCpuType : 344 -> 360
~ _internal_NXFindBestFatArch : 2676 -> 2600
~ _getsectdatafromFramework : sha256 f0b3ac48a97a3191a510c92f7a0f1535e8290d77cc527f5ffcc9a99c32d6728e -> 311d80af2748a56efbdbbf0c058a82f92f0081f49908d485647ea8fa226260b1
~ _getsectbynamefromheader : 216 -> 236
~ _getsectdata : sha256 5395c08d9dbd25727728ebc03f4eef05bc9c3a699461d4237af79560a28188f5 -> 176ec4294eb6c86952eb0c49977bb68b02acd22cd885b4e88efda23ac19a9c9b
~ _NXGetAllArchInfos : sha256 fd29489403cc54d359c4767686584c09df1b44ba7cdd938fd6dbbc6a02bc6fa2 -> 7f945c39464e0b10275cb9bc660b3eca60f9c60ef1ff21ded376d003a13f9844
~ _NXGetArchInfoFromName : 76 -> 92
~ _NXFreeArchInfo : 96 -> 108
~ _NXFindBestFatArch_64 : sha256 bdf92292f0a8637e0f2b155b0fceaac6682fca542508894447408050ead6943f -> d7d46947574d835201eb6649bf26022d223fcd059807f381430dd38d1871e941
~ _NXCombineCpuSubtypes : sha256 bef98e60295379348739914817d8aefc2c1a959f71cbc4cc63dd0207cda26aa0 -> c6277bb290bfd1ef3d5a1cba4153be4bd0dc64013a9232fb1afa7636289c4452
~ _get_end : sha256 6dcd38e8d64839752c866d40c7522516857af17641469191a8a209d6550d2d25 -> ce3a990ac93e40e1826183e8093b5d85a3c176162d7d50609606938958f4b69c
~ _get_etext : sha256 4594630757d32739911693accb7b3db03c2a5d16e7ab196e3fb2987fe9a23b4d -> 889ff8c8b80f41fd35d47acf02b2d15322af565889e8d7e53acfba5d4f3461b3
~ _get_edata : sha256 9660fc242375731728361200e7466226179dd44281a3325b3a1478326f7e10c3 -> 80b32a546520ca14654283ba89c9f3b4884ab9280b334b2419df4d268ab21f25
~ _getsectbynamefromheaderwithswap : 300 -> 328
~ _getsectbynamefromheaderwithswap_64 : 300 -> 328
~ _getsectdatafromheader : sha256 f1d22584232ba606240993216453cad89d17c2806316b724b2dea607cae54e4e -> 44212360dd3b2784136e25ae6d51af13e522e94730d040fe40315ee1eb7b5839
~ _getsectdatafromheader_64 : sha256 68c2fbdba946702343ba06a8bb5b458f56f3cb735aff9e2834bf1c7096ea5c21 -> bdf1abe09c1b7254a43010d6af8fd16f826c60f82d0032e97a1f9e79c710ab41
~ _slot_name : sha256 ba3ec766dfddf72d1b6249fe96ddd2d38e6d24323e70213f0b8b9b1d747ce25f -> 1ee0c82fbfeeaaf4f4428856cc727d4cd42b92a5888b6e34dfddd37c2507f152
~ _swap_fat_arch : 48 -> 60
~ _swap_fat_arch_64 : 60 -> 68
~ _swap_section : 52 -> 64
~ _swap_section_64 : 52 -> 64
~ _swap_twolevel_hint : 56 -> 64
~ _swap_build_tool_version : 32 -> 40
~ _swap_nlist : 64 -> 76
~ _swap_nlist_64 : 64 -> 72
~ _swap_ranlib : 32 -> 40
~ _swap_ranlib_64 : 28 -> 36
~ _swap_relocation_info : 168 -> 172
~ _swap_indirect_symbols : 32 -> 40
~ _swap_dylib_reference : 56 -> 64
~ _swap_dylib_module : 64 -> 80
~ _swap_dylib_module_64 : 68 -> 80
~ _swap_dylib_table_of_contents : 32 -> 40

```
