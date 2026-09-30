## libmacho.dylib

> `/usr/lib/system/libmacho.dylib`

```diff

-27050.4.0.0.0
-  __TEXT.__text: 0x2860 sha256:00810f9af84c59a7e64f35d00c72d9a4a4d941cb6ed476992ee177886898668a
+27056.0.0.0.0
+  __TEXT.__text: 0x2968 sha256:a24f74beb17a25badf6c1ea52630e8156bcfbc158cb56b35b7c82108aebff010
   __TEXT.__cstring: 0x492 sha256:23580a7bc73109fe76f608b832541f24ca11bb5ab829bed353daffb4b7cbc09f
   __TEXT.__const: 0x20 sha256:abffbb2c8bf5bbe75c584de74f69b93b9676b0b16e0acd01d5ce8aee99b3260a
-  __TEXT.__unwind_info: 0xc0 sha256:96cd85d6312c92b480ed04efad9d5cfec0834a260e43faaa3979ab52a624ddd0
+  __TEXT.__unwind_info: 0xc0 sha256:0f3a22331e71d407a08bc1418f6e77f8dbfc6412fd2709d2f08b59afbf2eb3b9
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x7a0 sha256:057127e1e7785fa9ae0c0dd98b2ac6fe6012cbadd20375e70f49b55321c73fc3
+  __DATA_CONST.__const: 0x7a0 sha256:ff2da9f1f6ef2ae66e72332364566700d6640f59ce78c5d0973b72ae6730718d
   __DATA_CONST.__got: 0x0
   __AUTH_CONST.__auth_got: 0x0
   - /usr/lib/system/libcompiler_rt.dylib

   - /usr/lib/system/libsystem_c.dylib
   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
-  UUID: 29DD638B-0DCB-31AA-8A76-6279CC8618F1
+  UUID: BB648264-46F0-31D4-ADC9-8EC7F3CAC327
   Functions: 91
   Symbols:   108
   CStrings:  122
Functions:
~ _getsectbyname : sha256 44c9f1a8c7810ca1a6304a32c1901fa535246b84261c0948396cc6db009cd843 -> 3ccdc1c03d045dfbf73ea44e122018914d375c8aad4cf3e57babc37ae1b06c3b
~ _getsectbynamefromheader_64 : 216 -> 236
~ _getsectdatafromheader_64 : sha256 4633e164ab650b83305dfa5d95244a03c13aea19d7816703ded2aee2224f8677 -> 77f3d2d21e8e8e88a8e58ec9c81dd5d5e943d5defaebf95ed58abc80794265ea
~ _getsegmentdata : sha256 b8efa9a126ea62eb0dd1295e1f40761ae784c85d619d14c4599f9d62c51b051a -> c917c218d4bee024493dce2035f1079c1a08dcee31503c99ed3b305346f6f21c
~ _getsegbyname : sha256 7d9aef3e095e2f3fd2ac4795e8cb011a685078402a16e8e7dbe9c5a6b36a4f70 -> 746641b0c33b549ec1b4535a838dbe95f415dcbd93df0c577bc90af100f59e72
~ _getsectiondata : 444 -> 496
~ _NXGetAllArchInfos : sha256 d057f13247c2fa22158bbe38702407f762143940bab964134457fd9c361031b4 -> 172be225776f7fdba02eb28db39ed579b077afaa431e3ef2966c31d07a9a785a
~ _NXGetLocalArchInfo : sha256 f3838ddf98fe4cea6b73486042fd0581dda01da845da53e168b27fe3ddead81c -> 7b84409199aff3c8fd1325b16b262aa01954f4859d6e0111809ba12114b35d08
~ _NXGetArchInfoFromCpuType : 344 -> 360
~ _NXGetArchInfoFromName : 76 -> 92
~ _NXFreeArchInfo : 96 -> 108
~ _internal_NXFindBestFatArch : 2696 -> 2616
~ _NXFindBestFatArch_64 : sha256 767104df8376f20de3142a8f2ca134684e841785cec16c62c201e972619280c9 -> 235d0e67c0d116fbe2bf28937eee5c6f0455f2475a0d25c89a67612466b53beb
~ _NXCombineCpuSubtypes : sha256 cbc12da2aa78e387539a34c46cf695f0a4c155446b6c8ada9b0d5f668436eff1 -> 66d3a188ac2f72013f743ccffb692328e5da5e0c1213188950c563ac607b7865
~ _get_end : sha256 bb941a1304d1e33be215e3c3a2b5ca6e206bde74fd753781c28d2d0c490eb8a2 -> 612f7277031e79db1edb705f299e18f62f15ba62c5a12bfc2fc2035500369c2d
~ _get_etext : sha256 f0bdeda15bf0dcc22fdb0015d2ccd5bb0d2308bfba60464c9d82ecc401d27384 -> 93f1084204fed54d766d17bff2a7f66d8c30b70988ad467d7bafdcddeea0f3aa
~ _get_edata : sha256 d9f4878a0b7653a8f6681d704ccfc6ae70da708effafd6171fb3db0fece99b2c -> 479622e26f6e496e94b5d3e0f809f15994b6038c17c6c24ff90240e2018355f8
~ _getsectbynamefromheader : 216 -> 236
~ _getsectbynamefromheaderwithswap : 300 -> 328
~ _getsectbynamefromheaderwithswap_64 : 300 -> 328
~ _getsectdata : sha256 b4918cb35469e50c79b03b362891276202b8f77e56e6897842dd528840833988 -> 07a54cac70612562a0d0caf8a99ae3a77978030ee9d39041be8fa8a9000509eb
~ _getsectdatafromheader : sha256 f88b15bdd8b44ff16e086e583cf565c3bf7af7f16813ac57eac880eb192f229f -> 4c76fd26cf39f977e9fd7207996388b5649172095e9b1b604d9832c5c2848281
~ _getsectdatafromFramework : sha256 c9b758cbb781f91f36e9c9490f885acf6a7876204a9c191b8eb585bd09fa7eaa -> c4187620916f710f7fa5725c031126f115db2901b91d0d146bdc62062d33b997
~ _slot_name : sha256 4ac505d41fef167b929a1ed3f749cf49fdbe1ce197307241e01bf45805cea73a -> f03ba62caa5e88d7b1f2e8437a8d540cd5dffc082e1df8ebc533bfee6ba0a653
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
