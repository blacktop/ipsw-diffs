## libmacho.dylib

> `/usr/lib/system/libmacho.dylib`

```diff

-1378.0.0.0.0
-  __TEXT.__text: 0x285c sha256:a8c237c1d15f111a3728505923d052ef17611288acc20a9545fb4013ccdc7a3d
-  __TEXT.__auth_stubs: 0xe0 sha256:26dbebe7937604442291d62055f91e9cb5cc330dec32c9b8f6b4217d276d9b58
+27050.4.0.0.0
+  __TEXT.__text: 0x2860 sha256:00810f9af84c59a7e64f35d00c72d9a4a4d941cb6ed476992ee177886898668a
   __TEXT.__cstring: 0x492 sha256:23580a7bc73109fe76f608b832541f24ca11bb5ab829bed353daffb4b7cbc09f
   __TEXT.__const: 0x20 sha256:abffbb2c8bf5bbe75c584de74f69b93b9676b0b16e0acd01d5ce8aee99b3260a
-  __TEXT.__unwind_info: 0xb8 sha256:23f286c8957606a0496562d5ae86016ba9e24e9878bbe434c068a6c4b9f91b2b
-  __DATA_CONST.__got: 0x8 sha256:af5570f5a1810b7af78caf4bc70a660f0df51e42baf91d4de5b2328de0e83dfc
-  __DATA_CONST.__const: 0x7a0 sha256:302f18022487f98e7ed05273b87d691b5fca0ab8faa2b79400c40d094b6c2cd1
-  __AUTH_CONST.__auth_got: 0x70 sha256:b5fdab78d8947eacc864bfeecb4d2100780e5afe1cd8efafb124887913ac49fa
+  __TEXT.__unwind_info: 0xc0 sha256:96cd85d6312c92b480ed04efad9d5cfec0834a260e43faaa3979ab52a624ddd0
+  __TEXT.__auth_stubs: 0x0
+  __DATA_CONST.__const: 0x7a0 sha256:057127e1e7785fa9ae0c0dd98b2ac6fe6012cbadd20375e70f49b55321c73fc3
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__auth_got: 0x0
   - /usr/lib/system/libcompiler_rt.dylib
   - /usr/lib/system/libdyld.dylib
   - /usr/lib/system/libsystem_c.dylib
   - /usr/lib/system/libsystem_kernel.dylib
   - /usr/lib/system/libsystem_malloc.dylib
-  UUID: 7E6E20B0-7267-3D97-A8E0-E056D08F5D2A
+  UUID: 29DD638B-0DCB-31AA-8A76-6279CC8618F1
   Functions: 91
   Symbols:   108
   CStrings:  122
Functions:
~ _getsegbyname -> _getsectbyname : 112 -> 64
~ _getsectbynamefromheader_64 : sha256 58bd21ebc56441a74fc0014923ce163a57a68d2fdf24167b03e3320dac07a449 -> 79e59ff18a31e8b36604e991a0868f462c1e30aa0efd3a002953f7591d2f9473
~ _getsegmentdata -> _getsectdatafromheader_64 : 180 -> 60
~ _getsectbyname -> _getsegmentdata : 64 -> 180
~ _getsectiondata -> _getsegbyname : 444 -> 112
~ _getsectdatafromheader_64 -> _getsectiondata : 60 -> 444
~ _NXGetAllArchInfos : sha256 b8163c3e18d7d24a3331e0287970c7f4c7856f56e5a11cdf6103aa934c12c3ba -> d057f13247c2fa22158bbe38702407f762143940bab964134457fd9c361031b4
~ _NXGetLocalArchInfo : sha256 3c77c190c1784d83c2d32e8bad62e3efe3cf3e52bc39157c4a3695ff8abe4366 -> f3838ddf98fe4cea6b73486042fd0581dda01da845da53e168b27fe3ddead81c
~ _NXGetArchInfoFromCpuType : sha256 f75f06e4e3d245418f354c3165d097c1bfc461a5282176e9157bd662c282df0d -> 8df271b56be5fa3b1f2dd71d343aa40c6c474626a20147652951192d1572c54d
~ _NXGetArchInfoFromName : sha256 09f5bc93f1285fa0de30aa767b042d6e4aa636d1a5f2a78bc1d032bfec507fd1 -> 18406ce11c734611c933cd98ad0a499c13c0ef5b569c2614f25ad50e3ab97809
~ _NXFreeArchInfo : sha256 add4e38e386415d52aa98d817998e67ee7ec33dc4617ea08747c50a341051824 -> 18061800a799a21feb3ac4baaa08dac45066a1ddb2b449145249c75f20b13bb3
~ _NXFindBestFatArch : 60 -> 64
~ _internal_NXFindBestFatArch : sha256 18d8f36120e4e044b920c6bba6fcaae1ed49385a0cde16367d048ba5b302fd4c -> bd8527ca8ff467f62b3ea536af1c5e4dfb76d5727a949aa08ad5e98093c140a4
~ _NXCombineCpuSubtypes : sha256 c8f5d20cc4318bf72933995c4993cb0507004827b53efda796b70bc87a627898 -> cbc12da2aa78e387539a34c46cf695f0a4c155446b6c8ada9b0d5f668436eff1
~ _get_end : sha256 95d4945a108028f9c516c1db68945b3f2b625ad052969935a3c9e8196c3d4fe4 -> bb941a1304d1e33be215e3c3a2b5ca6e206bde74fd753781c28d2d0c490eb8a2
~ _get_etext : sha256 026b6962846077530f0bfec0d3a562ec10cd2f635412a7b93882988c87404b9f -> f0bdeda15bf0dcc22fdb0015d2ccd5bb0d2308bfba60464c9d82ecc401d27384
~ _get_edata : sha256 3b9f01ee32022a05d63aef065b3f3b43dca58312e482e87c862132db2c2b95de -> d9f4878a0b7653a8f6681d704ccfc6ae70da708effafd6171fb3db0fece99b2c
~ _getsectbynamefromheader : sha256 2b0d4c63f60784193c6a8b8d2c944b0728dff15f614b1b698137304f5568f08c -> fe0fe00361a3aba73f673f0a5185d5d002ae7b9ac1024be7565ebc906c041700
~ _getsectbynamefromheaderwithswap : sha256 c09b9a59915c74e9b6aec0072116123314754a233ca6fac26c09068a6b4b19a5 -> cfcd4cca1e2d6249839045f666ffb21d7dc3117818a425e49a022ffd61ace2b0
~ _getsectbynamefromheaderwithswap_64 : sha256 25da8bc68445d7909e9e75e43393940b690929951ed951c1c2d1d94bc31645ee -> 21ab712cfa4d65695a75f4f196bff3443f52576f8908ae51aa8797f5e9142ee8
~ _getsectdata : sha256 0dea857adc3cf4e39de870724b0e30428e31c374103c087f9f93cffeae020411 -> b4918cb35469e50c79b03b362891276202b8f77e56e6897842dd528840833988
~ _getsectdatafromFramework : sha256 db5c626c6b3d98da8a348ef7b11e9b29c7780565f97b27b8f6a81bec8e6b561c -> c9b758cbb781f91f36e9c9490f885acf6a7876204a9c191b8eb585bd09fa7eaa
~ _slot_name : sha256 6343281c38d1c699e96ba4c5136809666a6ad82f1d00fd41a34b86fa05403c5c -> 4ac505d41fef167b929a1ed3f749cf49fdbe1ce197307241e01bf45805cea73a

```
