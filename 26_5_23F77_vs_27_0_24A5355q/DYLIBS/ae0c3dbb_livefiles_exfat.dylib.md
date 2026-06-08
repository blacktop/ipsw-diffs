## livefiles_exfat.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_exfat.dylib`

```diff

-522.100.20.0.0
-  __TEXT.__text: 0x1c8fc sha256:481889131f15d7dfc77ef8240977284068969383830ca328a4715c36e9d0a385
-  __TEXT.__auth_stubs: 0x430 sha256:1d65dc32df531aa04962eb1272141a816d61638bfd2c3908398dddee6d06d8e2
+560.0.0.0.0
+  __TEXT.__text: 0x1be14 sha256:15dfd5a8bb02038e63f66038ee6449af71bffd5d6ca49595f35cf920f7bdb787
   __TEXT.__const: 0x4b78 sha256:6e38d37b07f4980ff610a6c48d7eb2db7463ef8ea29c56b872d29f771f7cd953
-  __TEXT.__oslogstring: 0x46d8 sha256:39ade92a034b802b543e3fdac3b524f7461d16734f30891d868f457b870c053f
+  __TEXT.__oslogstring: 0x4745 sha256:adb3d97d772ad413c129d4d6446b0688c35bbd3068775bb9598abcf47af919bd
   __TEXT.__cstring: 0x70d sha256:9b1c0b585da637df183ee3bad11c75855aadc15c28873fdc526cbf68541deb8a
-  __TEXT.__unwind_info: 0x258 sha256:95b0f311dc81363b60e6de8c7ed2edc47c9435d7274e3e12e971097f052de337
-  __TEXT.__objc_methname: 0xe2 sha256:fee00cdb547188df62796dd406a065daca2f6e6a34ffdacf7b4ac1f670b5db72
-  __TEXT.__objc_stubs: 0xe0 sha256:3462388bcefc2bd8ed7651e8ab3f6cc219c39c22f8a4000d1bf4918db657b9a7
-  __DATA_CONST.__got: 0x20 sha256:66687aadf862bd776c8fc18b8e9f8e20089714856ee233b3902a591d0d5f2925
+  __TEXT.__unwind_info: 0x258 sha256:2a22f39c9c7e39e0d58d405a05b600638a495bd583eb34c2105897df75acc013
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x38 sha256:620def72e27d25aa21cca5a62578ba81ebeb4548b789a0ec95bf19f48a0e5e73
-  __AUTH_CONST.__auth_got: 0x220 sha256:44ddd2f478477ebd1c1cd5b99400af48cd46033c59173195f48870e608cec810
-  __AUTH.__data: 0x140 sha256:76b6bb98b98ecd468c6bfa6e86f055f753af6a09f47bca6eef24fa152e8f6d38
+  __DATA_CONST.__objc_selrefs: 0x38 sha256:58c1690db778f80c35cb5d2ed74600cd36e0feed79d9ef4a4cc84fead49be421
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__data: 0x148 sha256:970933896c205fbda113d1f53f6d8435b6a06cf77bb9dec0cc8bc4cc93681ef8
   __DATA.__data: 0x27 sha256:dd9411bcfe65ea5f1489ecad0f049facf180b43ab1a762248aca928f0397d5d6
   __DATA.__common: 0x18 sha256:9d908ecfb6b256def8b49a7c504e6c889c4b0e41fe6ce3e01863dd7b61a20aa0
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb

   - /System/Library/PrivateFrameworks/LiveFS.framework/LiveFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 96D7CBF9-C259-3F99-82A6-AFB8C8F7B007
-  Functions: 182
-  Symbols:   349
-  CStrings:  446
+  UUID: 91DDF4FA-2910-3DAE-A9B1-7B1091912D64
+  Functions: 181
+  Symbols:   346
+  CStrings:  441
 
Symbols:
+ _CONV_NormalizeUnistr255ToPrecomposed
+ _objc_claimAutoreleasedReturnValue
- _OUTLINED_FUNCTION_1
- _OUTLINED_FUNCTION_2
- _objc_retainAutoreleasedReturnValue
Functions:
~ _exfat_timestamp_to_unix : sha256 21cf837446cb12f56c272ac7e82e2fc10f1a1e7705f04ec8a7b62032f50adea0 -> fe0e8d9b224ac38174ae6b921459ac8be1ad630fd4b099bd52cd15e4a6ac718a
~ _exfat_timestamp_from_unix : sha256 e10d5f152728feed3d162f50dce17de10f45a5c52b4f06a058550d7935b096e1 -> 3cee4f072c0a9268fc91dd2f9557bdc6c02476058f23d812da6765c1b7d49d82
~ _FSOPS_SetDeviceAsDirty : 296 -> 252
~ _FSOPS_SetDirtyBitAndAcquireLck : sha256 c7449a16128e13567457cf09099ac84669c367dea8e6729bdde2518f8914fbf0 -> 444982638fb083df5a1f16c3aa2d973696eb73888e2cd55303092445e6108a91
~ _FSOPS_FlushCacheAndFreeLck : sha256 52d3537cfb9f8a03d57bed964835d8513f8c0c20a1d16c0394c5064e61732dfb -> 42bee01404bc10a1d039677780e7efdc82c91e8712b65cdab7bdaecb15c113b8
~ _EXFAT_Init : 276 -> 232
~ _EXFAT_Fini : sha256 455f114a56a87afec8ab33d31ba39c4aa2694a0db02491381f890fcb0cc4607d -> 8a2658fc8cbee0e402ea75b9791db33bdfb03a59748c4d7e507da13970ed3826
~ _EXFAT_Taste : 584 -> 540
~ _EXFAT_Mount : 960 -> 916
~ _EXFAT_Sync : 488 -> 444
~ _EXFAT_Sync_async : 488 -> 444
~ _EXFAT_Unmount : 484 -> 440
~ _EXFAT_GetFSAttr : 1964 -> 1920
~ _EXFAT_SetFSAttr : 1220 -> 1176
~ _EXFAT_check : sha256 18837decf6b5a87fac91ce467c2db1e408af350ee4f914722118bea6f330cb80 -> 611ca5e4925a9555e5a984534544f28818e22d0ccac5edef782e5d8865cd600c
~ _EXFAT_ScanVols : 1256 -> 1212
~ _EXFAT_GetFSRepresentation : sha256 6a71c86655e170cb10fb201efef0013e093223f5c3010de25c7a45ea7bd7d50b -> ab2cb42af4b896168b008d793119c7036bd2b22cc7990e688c31b49c1c52c723
~ _livefiles_plugin_init : sha256 1dec4434894feb07d52055e7a19993125cdee7605b259d09cd895b036ff3e183 -> 5c1a0fb0961cd08f5c0e4ee3341aac83d4f64404a39f3be79d811f57017fa79a
~ _EXFAT_GetGMTDiffOffset : sha256 2cab9a23763787e37184610e6ea9106ad21f3d625d5f65899ae0ceddfa1508a5 -> 0d59c5480681ac2ba4a1a01555580bc4d3049a672f7e32d5660b05d6cec6610e
~ _FSOPS_ReadBootSector : 2108 -> 2068
~ _FSOPS_CreateRootRecord : 1572 -> 1524
~ _FSOPS_lookupVolumeLabel : 772 -> 724
~ _FSOPS_ReadUpcase : 1272 -> 1240
~ _FSOPS_CreateUUidFromSerial : sha256 74be0737498c2c5d4f73728c4d75e47f39178b239de70fd18aeb013c83135b11 -> 1de68de39160f2032e527989e27e476c19908b0d368df157bc3d3c0d941e2867
~ _exfat_sync_internal : 464 -> 420
~ _RAWFILE_read : 1276 -> 1236
~ _RAWFILE_write : 1520 -> 1476
~ _metaWrite : 520 -> 472
~ _metaWriteSync : 520 -> 472
~ _metaRead : 560 -> 512
~ _metaFlush : 320 -> 276
~ _metaClear : 376 -> 328
~ _metaPurge : 328 -> 284
~ _ZeroFill_Init : sha256 cd7404a0b4567750b4e358207ef240569123b19a4898dbf5690685cceb80e345 -> a39a5f5dff9bd31ef36291d227e96333116c2974b587360293a0e84dcf8d057a
~ _ZeroFill_DeInit : 236 -> 192
~ _ZeroFill_Fill : 332 -> 288
~ _ZeroFill_FillClusterSuffixWithZeros : 272 -> 228
~ _MultiReadSingleWrite_Init : sha256 babe4d40167bb47f093ceeb329a5b9dbf435650b4a8b256a99c86c40829a69c0 -> 733d039892d785361c357fac6b172d4f088819666c34332da31b6f33bdd75f71
~ _MultiReadSingleWrite_DeInit : sha256 1a5eda368c4cbfee7d868cacb2c6ed31cd811a317779637bd3ff1c4657c72466 -> 46233091e904342a4d156cc60544b45966f4e8d20ad0aa14763c90b09412269c
~ _MultiReadSingleWrite_LockRead : sha256 58a1635747edd062cbcec71752f15e863786b3933c93816e7c2657e2a5ff7b22 -> b85915b1cce56879cbcb1ad716de53711e740a6598fd27a4e2c8dcb568a9a7a5
~ _MultiReadSingleWrite_FreeRead : sha256 bd5b5ce5be1a6fd56425370acbc0b1f4b319bd05a13955888a23d7e45efe7492 -> f47da427e2e0f34dd614ace7939ade0b31c653f14ea9888faad671d23f48e398
~ _MultiReadSingleWrite_LockWrite : sha256 a7fb9a638e9c8e93387cf48010f8b3f5dec71da9fbce250d467b58ff555b3a9b -> 33d0e2d76c03edf81691888584cf1a427d92830c47c01f691e156575e5c1e51e
~ _MultiReadSingleWrite_TryLockWrite : sha256 9e70d74fe21c29d250ef05507daece2d61fd537f4260d2257a1d55297a950a6f -> f56a6da25fbf66d2b004eca56cab053cb178b05855f75b3394dca2d62277acd2
~ _MultiReadSingleWrite_FreeWrite : sha256 5a4923df39e1287598fab535e2409dd8c9fbb45949a194fecabcc0a0e17a5c56 -> 821dd6b8eaafe9f0c15e20eb7103871fc229dccd45813ff438b4afa813a4a3f0
~ _OUTLINED_FUNCTION_0 : sha256 5955f1626adcdddb5b8b8289597b05685d471a639c448e9e534e3f3c2fa46bdd -> 47cf9dedc1a97acae89f502e29fcccae45356f05223c913b19013e242931c2a5
- _OUTLINED_FUNCTION_1
~ _OUTLINED_FUNCTION_2 -> _FILEOPS_GetFileAllocatedSize : sha256 0a7d2317f2a602b04fbcb9d5c3f3495f405b0d609bd4938e267486deca46d441 -> be506f6c1da1d79d9255be5bc8f7e55ce5e4d45dc64875c901e1b353ebea1018
- _FILEOPS_GetFileAllocatedSize
~ _FileOPS_SetAttrToDirEntry : 2044 -> 1992
~ _FileOPS_FillFileSuffixWithZeros : 664 -> 620
~ _FILEOPS_GetAtrrFromDirEntry : 548 -> 552
~ _EXFAT_Read : 824 -> 780
~ _EXFAT_Write : 2556 -> 2552
~ _EXFAT_BeginBlockmap : 2628 -> 2564
~ _FILEOPS_FetchFileExtents : 816 -> 772
~ _FILEOPS_CreateBlockmapRequestEntry : 336 -> 292
~ _EXFAT_EndBlockmap : 1868 -> 1748
~ _EXFAT_Create : 1420 -> 1376
~ _EXFAT_GetAttr : sha256 f2d7f16c85c84c682e0191d4abca5320bd2fd4ec9b51cb87e0518b975ce4ee5f -> b5395e752c231c6895ab4c77a18e58d0284058e303d8f941a4ebe12fc6ebd4a3
~ _EXFAT_SetAttr : sha256 430a372746ef64b32a8241183c138102b750616d5a31e0bf8131efdca236b2da -> 4aeab97c93e5a5251ee98a2ac99d3acfc7700561f5517d83e9833b58943e9700
~ _EXFAT_Inactive : 936 -> 892
~ _FILEOPS_FreeUnusedPreAllocatedClusters : sha256 dc6f64daa10614ef7bcde4bf1f076b8b419e6b0f014a9d725d24722ef5911134 -> 7f0660b28077468719e7ebc69655b2e49eecadd90cbea03056a8828b2cbcbc25
~ _EXFAT_Reclaim : 796 -> 752
~ _EXFAT_ReadLink : 1128 -> 1092
~ _EXFAT_SymLink : 1392 -> 1348
~ _DIROPS_CreateLinkAccordingToContent : 944 -> 904
~ _EXFAT_Rename : 4612 -> 4600
~ _FILEOPS_PreAllocateClusters : 1168 -> 1124
~ _FILEOPS_FlushDirEntryIfNeeded : 316 -> 272
~ _CONV_UTF8ToUnistr255 : 1324 -> 1360
~ _unicode_combinable : sha256 ccad426a1b9261acfbf99282623ca7a0d9087210be2b9afd0309a8a9c47ec086 -> 84a4af3d18bf176cec5698946f8af5cc6c7cdfac5339b45a6f003766a1ce8f83
~ _priortysort : sha256 160ab5addd1d78a8e0c749199e930eab8e4344029b913cfe3ca68161d25b8b51 -> 648d73d823a1e904a01a2e0c14ec7cc6fbbff3b5a2f79da454c94b7afaf57c11
~ _CONV_Unistr255ToUTF8 : 872 -> 876
~ _CONV_Unistr255ToUpperCase : 56 -> 60
~ _CONV_UnistrUTF8ToUpperCase : 204 -> 208
+ _CONV_NormalizeUnistr255ToPrecomposed
~ _CONV_GetCurrentTime : sha256 801ec25cce931c95d86883c8f0ff60bb1c5712dfbff3ad2da23f0162f47d4692 -> 685c812f9e479d648cbcc84868067f999e64f79afdcbe9fe251758d4b2a0ed44
~ _CONV_DuplicateName : sha256 a958c28d9ef304f5ab519af74345dbe88b8cc0cbe13f639890cffe10a4008c24 -> e764987baf80986d29d06757de1e2c312a8f7ab89bfcc0dbf9a1519b6efddcf4
~ _unicode_recursive_decompose : sha256 d528f069de78747339ec5e1603c15b1ed6567dd79b576d0bc6b54588cf6cb183 -> bbb9ed56b905a72d1907cdb4e6e813461f94b9406331c05cac18f4a9460f2f24
~ _DIROPS_IsDotOrDotDotName : sha256 2c525bb07e095e00511da515f079ca29d343b9249c49e80cd71ea9e4d681efc0 -> 8fde8d7277b840f95f91c57fcaa4c252e6c8981c7bdc6a79ba76662bf0bf11f9
~ _DIROPS_ChecksumFileSet : 76 -> 80
~ _DIROPS_GetFileDirEntryDataByOffset : 624 -> 580
~ _DIROPS_GetDirEntryByOffset : 3284 -> 3244
~ _DIROPS_isDirEmpty : 964 -> 920
~ _DIROPS_AllocateDirBlockBuffer : 316 -> 272
~ _DIROPS_FreeDirBlockBuffer : 280 -> 212
~ _DIROPS_GetMD5Digest : 216 -> 220
~ _DIROPS_VerifyIfLinkAndGetLinkLength : 220 -> 224
~ _DIROPS_GetRecordId : 876 -> 832
~ _DIROPS_LookForDirEntryByName : 1552 -> 1716
~ _DIROPS_LookForDirEntry : 2668 -> 2932
~ _DIROPS_PurgeNodeMetaBlocksFromCache : sha256 76511c65f8d424107bcbadb56e335c0585f20e8024194f3d4a0520ab60186d78 -> a50ef2aeb1a4c742609224759dd4763f99cb9c8797764fb64253bb05a9cc4e8f
~ _DIROPS_CreateNewEntry : 2240 -> 2196
~ _DIROPS_LookForFreeEntriesInDirectory : 2140 -> 2080
~ _DIROPS_CreateFileEntrySet : 800 -> 808
~ _DIROPS_SaveNewEntriesIntoDevice : 1000 -> 956
~ _DIROPS_UpdateDirLastModifiedTime : 364 -> 316
~ _DIROPS_MarkNodeDirEntriesAsDeleted : 1364 -> 1320
~ _DIROPS_GetDirBlockRelative : sha256 2e1fb235f3d475f0a17ec6cf24441cb043b76140584341be169a0d0d4221b9d7 -> a79d4e23369a319b3521886ad6a4a1b9e4f54a06a71f99436ef31b286c1997db
~ _DIROPS_PopulateHT : 1008 -> 1224
~ _DIROPS_UpdateDirectoryEntries : 2804 -> 2768
~ _DIROPS_GetDirBlockAbsolute : sha256 c9731b4dbc524e16af0eaaed915f0821a82cbabde903a28dc1ed7dc70fe43cb6 -> 943e6d5bd074425619c5e94e42b38b617443a589b290b89fe7a28f759428efc1
~ _DIROPS_CreateHTForDirectory : sha256 83e98f3f02f9e9e935abd844ca056818e280dc719237be4e39232befb7025d40 -> 12497647133f5373e0e8be6156ad35c62b83f5a09494496be7ea571bdce48932
~ _DIROPS_AcquireHTLRUSlotAndUnlockNode : sha256 bbe2100f86febf212a6dfa16f4792c5a0df13231383fdcf310bea428607b832d -> 8b2a51b0865d570f9b544e18d49046c5334357cee6ec5569b5c152bf0eb82ed2
~ _DIROPS_MaybeFreeEvictedHTAndUnlockNode : sha256 e208be0f1cb0832e9d9730f007d9e97b42606483b6a3802ad446e18b069949ea -> 030dc6b718cb5ef5e4e6c3a313cc8933919b3932e47078d234a317b982c5d879
~ _DIROPS_ReleaseHTForDirectory : sha256 abada2347c0fa36d1e2ed9571651086c538a7b6ff17d1cdd9532ba9fc8eda2aa -> 1253f79fa7713d1441a0105c175045bec7218c3165d4de7c1765cfd2da3015a2
~ _DIROPS_WasEvictedFromHTLRUSlot : sha256 523a52e3593b9055544f52bf1963d6076b6af88a85e114b9166948acdced51cd -> f3ff9ad1c9780368cbeb0609da304ab76f153f03e9b8488a002f3cdbdfc2dec7
~ _DIROPS_DestroyHTForDirectory : sha256 991fe04095dd61437fbf4b982cb4542e9c0177607fca98ce3d6051fadde90ab9 -> eb9ea5702d9fa17663a8ccb52aeaa341496963b87d436c75b15899c5d3120b17
~ _EXFAT_ReadDir : sha256 e8374457c1091dbcb0f1dae91c91784c36003d72037d212a459fc91cbfdf52a4 -> 8d2586f5193de38be5c0d3b0b025366fc1192f07554f91f561521daf34445c34
~ _DIROPS_ReadDirInternal : 2872 -> 2784
~ _EXFAT_ReadDirAttr : sha256 ab3e6d5d3a5ac6411aebff669c87b935d8aec2007b01751c721f7d7d579d5fa6 -> 76536027f3ffe11d7cf84c4034e0d1f7bc2c8b278f8681cb7511b726354bb419
~ _EXFAT_MkDir : 1428 -> 1384
~ _DIROPS_ClearNewDirectoryClusters : 724 -> 892
~ _DIROPS_LookupInternal : 732 -> 692
~ _EXFAT_RmDir : 1360 -> 1312
~ _EXFAT_Remove : 1128 -> 1084
~ _EXFAT_Lookup : sha256 3926d61b34e9a128ef8aa02bfe79fd85153a0d1fab069d599de12c5638d497e8 -> f8fba6b4557fa7776c9a2c85181c2ea36f907d637321d0c077bd3a9edc1d4e9e
~ _EXFAT_ScanDir : 944 -> 900
~ _DIROPS_VerifyCookie : 880 -> 836
~ _DIROPS_GetDirEntryOffsetByIndex : 916 -> 872
~ _DIROPS_WriteVolumeLableEntry : 1312 -> 1300
~ _ht_AllocateHashTable : sha256 132394ebdce30d8e782f4dff6e4d56c93996b3d4dfaac2d4964d3603419ae373 -> 0cc3b6ad18f6a0107037805f01ced06d92dceb8da51b9fdacdc8324d89feb584
~ _ht_insert : 568 -> 524
~ _ht_remove : 604 -> 560
~ _ht_remove_from_list : sha256 5abbc8614c41672dc9e2931f42b3117a7f07be4171ac0e18aa1906a0f8d5fb4b -> 76aafe33af3af84fcb439345108260fc536d6a8c824e3a81418c5902e761e1e6
~ _ht_free_all : 124 -> 128
~ _ht_DeAllocateHashTable : sha256 834f00d2bf135e58ad3f70ccae3ab08b7657c8cdb53ebe0b24e703667d1a4885 -> f269833157d741e93061de023664d91f846058f9b6a3b53fc28dabd729e4612c
~ _ht_set_incomplete : sha256 67708521d8da6f272565b57a9dc2f0c018d8b9434ef24ed60cf7051ee0d6d6f7 -> 7c6ccb87dffa2a0e2e252cde39e57943e99d0337146ef740462cafee1760bff6
~ _FILERECORD_AllocateRecord : 1308 -> 1312
~ _FILERECORD_FreeRecord : 400 -> 356
~ _FILERECORD_EvictAllFileChainCacheEntriesFromGivenOffset : sha256 d1d8e3f108c2cabd3990d1b88720732e5751930a1aec19c3df4853df696e4afe -> 73bae7ef3973ca258df24351b253e425f6b8b9ab84fd9a49687e6fadadebf748
~ _FILERECORD_InitChainCache : sha256 401a2666cc527c5fa9f6d76d00ae4dd5b83b691f0bc524ca5ea809c6fa17339d -> cc3cf060ce86608a5bbf55d30b1e59bb23d665c9deac336995edeafb6363fc07
~ _FILERECORD_DeInitChainCache : sha256 5c1dd885565b5444d22361a6acc4b9507184d47d0daa3d1c240a1f947ffcd38f -> cb46d4b06f32c16c25c0c0f524b2c33fc98fe2cd614e578cc5d281ac1ad93a7f
~ _FILERECORD_RemoveChainCacheEntry : sha256 0349ad0bffdfbebe95e263933b4fe2f42f5d0eabca9c1aa7c6295d9e42e590c1 -> 07acf40225d237ad8827a294b36d7f6198d76cf26733a82607760809b6d5d6b1
~ _FILERECORD_GetChainFromCache : 1840 -> 1796
~ _FILERECORD_FindClusterToCreateChainCacheEntry : 976 -> 932
~ _FILERECORD_GetClusterFromChainArray : 504 -> 460
~ _FILERECORD_UpdateNewAllocatedClustersInChain : sha256 6cd2c5b4cbca54cb15bda5df2a724c90c477a25728b0656fc6963fb1635f4141 -> 582235804b191cf46fad5d17a39e2d8556a2dfa78912829d6827979aae8a02be
~ _FILERECORD_AddChainCacheEntryToMainList : 348 -> 356
~ _FILERECORD_SetChainCacheEntryInFileLocations : sha256 fb063cd04f4481236a883971bcea8c3442b1d9f059433810e70f27c8aba048e3 -> e72bf026713cfd13292e8ff69e41eda8b6bc370a0ceea785c51d3d144b0c51e9
~ _FILERECORD_GetLastElementNumInCacheEntry : sha256 f4b078b206a8a62277c45097cf2171f1424fb79b656719b0590b10e3e1eb2780 -> 804341ae62e01639a4d2187e07d1eeccf3187ed10720aa5a29b500242b90e28e
~ _FILERECORD_MultiLock : sha256 81d5313b55e9ac3661a6ad14429c05eeff44630e1c366d1c95493de61e3c5662 -> e82ed0257a3cfa2e012d1c057eb6bcb8a1a55c5805d391362380f9f9141c11ca
~ _EXFAT_LoggerInit : sha256 8a08d5eba8da2c321535fcf034e24d9a615f6596db8ddc2dc434cb78dc986393 -> fc53aba621a63431d34e5cfc79ce5cdf7a92d114b954a9a4deadfdf27ddb5200
~ _FAT_Access_M_GetClustersFatEntryContent : sha256 f75ef9bf9f15e8ad7b91e6a07ab67c5a5974bc00e0709f0dc117e5f1aff74ef5 -> 9d391ed240652dfa8aab67df33341264e6602f7daf97d9860960032483e9011b
~ _FAT_Access_M_GetFatEntry : 1136 -> 1092
~ _FAT_Access_M_ContiguousClustersInChain : 360 -> 316
~ _FAT_Access_M_ChainLength : 496 -> 452
~ _FAT_Access_M_GetTotalFreeClusters : sha256 9e105d897dae539178a282f42f3b3ce07080b80e0af55576e0c7ce672cea97b6 -> 34eef0c3ea80202d180200767d7cc80e4ab771c5e52e822fb4fb888cc4c772c9
~ _FAT_Access_M_BitmapMap : 1468 -> 1424
~ _FATMOD_FlushAllCacheEntries : 736 -> 692
~ _FAT_Access_M_FlushCacheEntry : 520 -> 476
~ _FAT_Access_M_FATChainFree : 780 -> 736
~ _FAT_Access_M_SetClustersFatEntryContent : sha256 cbc684b9f1184dedb1f27a1dcac963a734b7f50bf6d4c2ff40fdf590547b5c81 -> fbccb8228618abb436cdd3f5eaf82e50985fd2d80b7402f1b7b58ef5919b8e0e
~ _FAT_Access_M_BitmapMarkBits : 896 -> 852
~ _FAT_Access_M_AllocateClusters : 4288 -> 4252
~ _FAT_Access_M_FATChainAlloc : 352 -> 304
~ _FAT_Access_M_CreateClusterInfo : sha256 7fe8a7bafd9d23100b44799f1557096dc2cb86dea12098e9f4350f3c1034db06 -> a956b87a5b6478069e4596b5d610aa1752c9399ac6c1806098fc1437b328ec54
~ _FAT_Access_M_TruncateLastClusters : 524 -> 480
~ _FAT_Access_M_FATInit : sha256 232255ab95adb7b22a55886a9e704b9ec4bf7fb2bb998c7c89d036a44e147a84 -> 84d40ff5367c097b874cc32c8f22600a5e4eb3e48d98d6bbd39e0168014c0690
~ _FAT_Access_M_FATFini : sha256 1c3a2498a188dc5ca8cd4d171c80d1934ba7f5e5631fdbdb211ef3e2e8997012 -> d313b30a88f5fcfbe8900e40d9e6e3734a75574d3438300a01d75b929302ce39
~ _FAT_Access_M_BitmapCacheFini : sha256 8a61f67efbdaf939cccda8e252a462be72565c670f08f3325ad2f1ba8ffa7f4b -> dd1eb5c3780fa72f511d2371a55fa2720630dec3c44ff2fc1fbf75c689840384
~ _FAT_Access_M_BitmapCacheInit : sha256 4058b4fd7a9256c6a2480a30eda25a10e749b11a8cbadd39c91b7c2f4532f7f6 -> e7a36142f061b8e791d7940e5d2147ae87fc838fbb2e9d3530c960dc8d7343ca
~ _FAT_Access_M_FindFirstFreeCluster : sha256 d450cc12fa45e2bd4bf9b573db210ac5935caaab81f38b6c90a4cf691cdfd04d -> d5976f6fce2b2e432881ed6687794d98f17163f5adee9b25a527b7b573332cd9
~ _FAT_Access_M_FlushPartialBitmapCache : 488 -> 444
~ _FAT_Access_M_MarkAllBitGivenRange : 556 -> 512
~ _FAT_Access_M_SetBitampCacheDirtyBitmap : 348 -> 304
~ _MultiReadSingleWrite_LockRead.cold.1 : 92 -> 76
~ _MultiReadSingleWrite_LockWrite.cold.1 : 92 -> 76
CStrings:
+ "%s: (%{private}s) got ENOENT with normalization enabled"
+ "%s: Failed normalizing UTF-16 file name. Error = %d."
- "clearMetaBlocks:ranges:rangesCount:wait:"
- "defaultClient"
- "flushMeta:wait:"
- "purgeMetaBlocks:ranges:rangesCount:"
- "readMeta:buffer:offset:length:"
- "readMetaWithRA:buffer:offset:length:raList:raListCount:"
- "writeMeta:buffer:offset:length:"

```
