## livefiles_msdos.dylib

> `/System/Library/PrivateFrameworks/UserFS.framework/PlugIns/livefiles_msdos.dylib`

```diff

-788.100.31.0.0
-  __TEXT.__text: 0x19ad4 sha256:47ab67a23b9670a404228a9859c1eb05f2d51b563b8b2a1da007f7dd17e219d6
-  __TEXT.__auth_stubs: 0x430 sha256:2dd22fa74813c3beeb5c595dff68602f71dd11b9682810c7b2627613d0413de9
+844.0.0.0.0
+  __TEXT.__text: 0x19150 sha256:5e3f9d715741bd042642ebfdbd577240f3b78bf320d711767de38d2c75208d66
   __TEXT.__const: 0x4da0 sha256:676c19c1b8f18cad5c003a5fd22464ebf587ce3434561a3dfc97b5ca65f41410
   __TEXT.__oslogstring: 0x45d9 sha256:0b49955d533c80da525452e4141f59bd361c8a2688ac05e3f3989424dd669901
   __TEXT.__cstring: 0x71f sha256:7f0a102c0fbac605a7da8d35420b5f26706392c082b06720d67bfa3cfff6efb7
-  __TEXT.__unwind_info: 0x260 sha256:f1f37c256ee922d334eda5467c1eaa2ff03328942169f7127e20d226236244ac
-  __TEXT.__objc_methname: 0xe2 sha256:fee00cdb547188df62796dd406a065daca2f6e6a34ffdacf7b4ac1f670b5db72
-  __TEXT.__objc_stubs: 0xe0 sha256:9da1cac8f30e82d55e136c2c2b387d491890e2177f94ce1aee4b868c4e0adcb8
-  __DATA_CONST.__got: 0x20 sha256:66687aadf862bd776c8fc18b8e9f8e20089714856ee233b3902a591d0d5f2925
+  __TEXT.__unwind_info: 0x260 sha256:99fe5bb060aa576d583d1b2ba4c8a82857bb974b939343be8a43bce26ce38793
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
   __DATA_CONST.__objc_imageinfo: 0x8 sha256:59fc9e64071aa89b9247d029e0b37ebe0fe9fc5434efb8e67b0b36435fb494cf
-  __DATA_CONST.__objc_selrefs: 0x38 sha256:24d32b648d1e46f2e2528a78d1f78c37712c92d6e770052485c3826e5c6fb533
-  __AUTH_CONST.__auth_got: 0x220 sha256:44ddd2f478477ebd1c1cd5b99400af48cd46033c59173195f48870e608cec810
-  __AUTH.__data: 0x140 sha256:a4f05508f34749d8d3cf9a5e3d3fbc2e3cd5d86e0f98d77b836295d89b1606c2
+  __DATA_CONST.__objc_selrefs: 0x38 sha256:8a614dac9139411df9518f24c4c95c5d4cdf1b07c8a1433a125229903cb6337b
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__data: 0x148 sha256:267bcb3c98a5adeb90636dea30f392d20e2b19053fa61445dd175b73fc3f964e
   __DATA.__data: 0x165 sha256:64f85fd4d9b74ca778111a1a0b0175f1f6a58ab3eda4402703d469858cbe9ae0
   __DATA.__common: 0x18 sha256:9d908ecfb6b256def8b49a7c504e6c889c4b0e41fe6ce3e01863dd7b61a20aa0
   __DATA.__bss: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb

   - /System/Library/PrivateFrameworks/LiveFS.framework/LiveFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 291CBAA2-E1F8-3121-9BD5-0F7524DC76BA
+  UUID: 08D3E5D3-8756-3444-A8AD-D1712D0BE850
   Functions: 186
   Symbols:   350
-  CStrings:  429
+  CStrings:  422
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleasedReturnValue
Functions:
~ _msdosfs_unix2dostime : sha256 524f95300f88a0a7a91ef87633b87457db056c55e377143acf0c3897e9dab487 -> f3f64a20c4b8cc83b6d3911cb1fd2cd101ae273f7a2132ea85f44b01b267e02c
~ _msdosfs_dos2unixtime : sha256 5c7cc85258ef575b9630224a6c314eaf463fa8b3e3d81f937ac21a50d37fa152 -> ad351b1a13bd138d8d3b8d6ab9a6885684dacae9c0c7880249411044904def59
~ _msdosfs_unicode2dos : 320 -> 324
~ _msdosfs_dos2unicodefn : 296 -> 316
~ _msdosfs_unicode_to_dos_name : 944 -> 960
~ _msdosfs_apply_generation_to_short_name : 176 -> 192
~ _msdosfs_unicode2winfn : 220 -> 232
~ _msdosfs_winChkName : 456 -> 492
~ _msdosfs_getunicodefn : 272 -> 284
~ _FSOPS_SetDirtyBitAndAcquireLck : sha256 fe5e8813571661d0de7c15bd4cd9e3bd6eace0a5dcd8dec38de04660e181b829 -> f35a16b65a50ed71a861d8d12e0de159621a5f8fc2f622985b51006fd0ca2033
~ _FSOPS_FlushCacheAndFreeLck : sha256 381b1f6d4bf936801f79cf515a3489878909f1674085e0acfb82cead236c415e -> 36c86a417677036d014aeb7ece9cb3f6fe4a37f3dfcc18a22a1b64b3f2e3bca1
~ _MSDOS_Init : 224 -> 180
~ _MSDOS_Fini : sha256 8cf71d27ca585728f5c984f661ba6b93c228912cb0b688f0a22c4fa8b119815c -> d719e81c2b6f842881f0110689b1d3df142d06be7ee4a8e20b88ac5ccf52ab6a
~ _MSDOS_Taste : sha256 223c29f5714bfee0646c7f41a85c14eec9d4420ba29b0974abe27ca6a55ed049 -> 76d807d580d6aa8a81b3ea9da270ab7c6c83bd49694a9e19083fddd86ff6b1a3
~ _MSDOS_Mount : 1372 -> 1328
~ _MSDOS_Sync : 328 -> 284
~ _MSDOS_Sync_async : 328 -> 284
~ _MSDOS_Unmount : 520 -> 476
~ _MSDOS_GetFSAttr : sha256 1c0432fe2cb0c6d4918c70d8f914a09dbbd074dca9a509eb2e74909dfdd39d99 -> 9e495dd812e0e959b228f930fefd33c7d1eb0d083fc83649c268992f61a83d3a
~ _MSDOS_SetFSAttr : sha256 e7ed19c5c1470ed20ce63614a3a53a2b85d7b29570a134a938892b68bb87af10 -> bf6e85192fe2b1873f564e1ed6414f5853f1f7efaca38c989250940b84268411
~ _MSDOS_check : sha256 853c8fae3d229dab0d7e01a6cda0ba28d1d4d1f730066dc1b7ee39d8dab9df4c -> c23a80c6e213f2907f05e59180c80a16a2d29552648bbca784692892fb35b384
~ _MSDOS_ScanVols : sha256 7e156e002328681b1530624916e364e5848b12479ff60d6ec47b5fc8d91cdc0b -> 1f698e4aea99d60c6851aa61ebb8332276cdfdfb634ec46642517160c2ca9346
~ _MSDOS_GetFSRepresentation : sha256 ced734437eff021f7c494d3f0bb215d492c40ad7d2381db208277b3ec3247d07 -> e2d0f25824e7bd598aaaad76bf7906c15419066c15f8a8ee2953a908222d50d0
~ _livefiles_plugin_init : sha256 3efdfcbc1c9e90972fe97ec8590e5315c3a9aac50a05d6185836165eef06bb94 -> afe57f464d50949fdc114b2705da5d84ff049fabb8d3756b0af861270b333c31
~ _FSOPS_InitReadBootSectorAndSetFATType : 3956 -> 3952
~ _FSOPS_CreateRootRecord : sha256 a27359bd412d9bc31003e6d34021a310d18e16696f5719d9b1de91f844a74a89 -> a8cc54b07e86cc4ca209fa8b743a66dc0532c99fedf87d5b503897966fb76ba1
~ _FSOPS_validateBootSectorSignature : 444 -> 400
~ _FSOPS_generate_volume_uuid : sha256 d3c62824a603b75535ec3c8e99c14ca44650b742496624dcf2302915f04bc5ef -> fea8ced81d8c05582502b4198e0a5405c02ccec69b7fc997147368dd011edff1
~ _FSOPS_CopyVolumeLabel : 500 -> 468
~ _msdos_sync_interal : 568 -> 524
~ _FSOPS_UpdateLabelInBootSector : sha256 94d0f5fed7e9a9f4cbf2bb418c50d8856a89a7cb2322bf2f8c7f5e96fbf3e0b5 -> c18eba74407727fdda307642971165ec67d0d34dac43149c790df4a15cda5a03
~ _MultiReadSingleWrite_Init : sha256 6a918e0ea93b451a9322de9dc3cd5199dd995c18ae5345a70a2b6147016ba06d -> 7e85fc0c8802c82f1c53781ea637b1db11d2df99aa376226d0ed7ce12f366d72
~ _MultiReadSingleWrite_DeInit : sha256 04b65663b44ad404363fb261b5587d5db846c26ff0a7dc05824d3f616bbf73a9 -> 6daa0c9ad030fbfeab8b3e52fef767bf57beaaea6086f4d6706b76926d01645e
~ _MultiReadSingleWrite_LockRead : sha256 063563c651f83278cfcd27e02bf538df95b0e0daa9f6362867851c1a3907da52 -> fbcb6c8e3b9e1a512223c338318f21d495cb3ed4de11ee530c9d063f9052ef1f
~ _MultiReadSingleWrite_FreeRead : sha256 420f72a9cc01f33dd53d0a10b875dab81471b35c5558853aa55ef8d8b5037cfa -> ca6c18271db7218bfde0bcd411cda23fc5dff365859d720589906cc5238d6fd8
~ _MultiReadSingleWrite_LockWrite : sha256 c64ac9ad9880bc1495ad480aba5ea80021df4426573e003b016a3a1c00085791 -> 0ea9dba51d8e3abfd996471b453bbc45613c2d05a5030ba9eb7407d441d49336
~ _MultiReadSingleWrite_TryLockWrite : sha256 404ea5b5efd7491389d7731460996eb3bfddf559fe0953f23d75db1f9857d1d0 -> 7a098f196eb112f3cbf882fa126d0393d83dea8c311d1bf92b6c6eef9598b4f2
~ _MultiReadSingleWrite_FreeWrite : sha256 bab8b0ae2fdde9dab308e57a746652393e1326b6922d013f0c785e0a8d305190 -> 5d781c26fcfdbab1270779abe8105424054156d0c76d0d28b15cbfc0f14acda3
~ _metaWrite : 528 -> 480
~ _metaRead : 568 -> 520
~ _metaFlush : 340 -> 292
~ _metaClear : 396 -> 348
~ _metaPurge : 348 -> 300
~ _ZeroFill_Init : sha256 e2ece48c1d39efab71cd2aab7cb939cceaf9bac0ddff1c0f480557a3d4a35d76 -> 7daaccb21ef4216f2bc7524d231e1db545f8d3aa1009eb36b4792a7a86051abd
~ _ZeroFill_DeInit : 236 -> 192
~ _ZeroFill_Fill : 332 -> 288
~ _ZeroFill_FillClusterSuffixWithZeros : 272 -> 228
~ _FILERECORD_AllocateRecord : 1360 -> 1364
~ _FILERECORD_FreeRecord : 380 -> 336
~ _FILERECORD_EvictAllFileChainCacheEntriesFromGivenOffset : sha256 5e207b3535415ea1d0f25901fcca76a66894f8a9674969930c101c863fa7c909 -> a86fdcf460ca0de9b99edd54c750fd8a3ff17789ece52749fe0d85ecb2507a4e
~ _FILERECORD_InitChainCache : sha256 5683e33b2ba9544ae2e41d634bfc57f3bc046c43f52e7b9e0cfeb04030a7aa2d -> 0f853ff70c839a571a75629a180eebd4ede15b54367eb3906c134a1cd15b5059
~ _FILERECORD_DeInitChainCache : sha256 5e20e81fb3e0c2efa142e7b319189f9e21173ceba59ec576cb2ca3a174cffda6 -> 2061a4405ccef60e3d3c616093ea3fdab646fc333f3171e05eb9dc8295a52f8c
~ _FILERECORD_RemoveChainCacheEntry : sha256 f49a0e4b6c9f96cbbf795a45724826abf2a0c2202760f3a0965d73fa88e6de0b -> 9459b931f058724a72d2d8b0e3119dd1db492bdf544a9cfc0a6bb3c627325f3b
~ _FILERECORD_GetChainFromCache : 1868 -> 1824
~ _FILERECORD_FindClusterToCreateChainCacheEntry : 884 -> 840
~ _FILERECORD_GetClusterFromChainArray : 504 -> 460
~ _FILERECORD_UpdateNewAllocatedClustersInChain : sha256 0a0dab67a9027e4d5b97d61b65f74cd89de0f2ff03d59f3f5b764cfabece51b9 -> 0d3d09a4e6a7cf8f0c90cd404b6f682211ed19138a7755560382a6dcb6ed9bdb
~ _FILERECORD_AddChainCacheEntryToMainList : 348 -> 356
~ _FILERECORD_SetChainCacheEntryInFileLocations : sha256 c7ec1429a91bec4fb1b43059748132e8a1863205a14878af7964d7949d86bc43 -> 411ac87f1d9086a53fdeeb468dfc065dc87316eae59f5060b1d4d6335a98e918
~ _FILERECORD_GetLastElementNumInCacheEntry : sha256 a164a5e9eee3ee51e02333d394b4cb81a4f726ba8d7113f8be05131fe83d2640 -> 009ceb29860bbe9c450bd70ffdf57c866170f9ceb7c5790b4c00e029bfa08f2a
~ _FILERECORD_MultiLock : sha256 71fff9120235cf8de881b81f5faf8a7590750e0a10444911a1292f75646e6479 -> dba1ad0c0edf506f6ca5b9510ca835cbfaf843205d0cee1a06da29e68207433e
~ _FILEOPS_UpdateLastModifiedTime : sha256 a338815a8f874f45536609a0d51f68a231ea4ef8aeb144ebebc3c48c350b00ef -> 31a75530f30ad362ec0b797959758b58dd4f2b5c9dcf8fe4e73ce3832a6b6b12
~ _MSDOS_SetAttrToDirEntry : sha256 7c5069c1f7ab5167c48756e1d0bca01f44820f303f668200a2cfd9aa2980f160 -> aa70b5446f6c1bd6967e5bda58e15f5b2587c81e5725e1762a8a32fe03aebd90
~ _MSDOS_GetAttrFromDirEntry : 1208 -> 1172
~ _MSDOS_GetAttr : sha256 2d240f8705c225c809613af0bf7b5514dca73fc3897b9a69738b3596a2e992aa -> c693a9a8adad4643e2dd7c1222d14d8d4a8e2b0e62e02f8a4bb7e57f53fae680
~ _MSDOS_SetAttr : sha256 8fd16594cddf544cea7269ed25cde48f0598245f5fec0832c03d35f5973ae249 -> 41d5721e7ee49e6abac2593856a4313cf137dacd9512ebdfe23334db5795bf89
~ _MSDOS_Inactive : 528 -> 484
~ _FILEOPS_FreeUnusedPreAllocatedClusters : 680 -> 636
~ _MSDOS_Reclaim : 524 -> 480
~ _MSDOS_ReadLink : 1332 -> 1292
~ _MSDOS_Read : 720 -> 676
~ _MSDOS_Write : 2732 -> 2688
~ _MSDOS_BeginBlockmap : 2576 -> 2412
~ _FILEOPS_FetchFileExtents : 648 -> 604
~ _FILEOPS_CreateBlockmapRequestEntry : 320 -> 276
~ _MSDOS_EndBlockmap : 1904 -> 1828
~ _MSDOS_Create : 1384 -> 1392
~ _MSDOS_SymLink : 1376 -> 1380
~ _DIROPS_CreateLinkAccordingToContent : 940 -> 888
~ _MSDOS_Rename : 4068 -> 4076
~ _FILEOPS_PreAllocateClusters : 996 -> 952
~ _FileOPS_FillFileSuffixWithZeros : 664 -> 620
~ _FATMOD_FlushAllCacheEntries : sha256 8e11dfab672b676682691f5002c775e36bad8f565246fe1bcd6f321a54b0ae38 -> 8802fd863d4befb78c97ce538333fee520a0f55351e1d1d25374736f8177a0f4
~ _FAT_Access_M_FlushCacheEntry : 404 -> 360
~ _FAT_Access_M_FindFirstFreeClusterFromGivenCluster : sha256 7600c3a3a3d136d39ddc94bc0d20c503ab7241a895ddf59aff87c7a0c771e6b3 -> 964132f6a56d6acb0831a19632a3972dc3b914f1a69fcea5742970e71d5c999b
~ _FAT_Access_M_GetClustersFatEntryContent : sha256 69b725755b5511fef9e24b4d74f5bc77484058ea79428f3e8a68a7999b9f3a49 -> 998e64aa3481624bd86ecc01d72fa2681c35afcc7dbf015a4043f9483153712d
~ _FAT_Access_M_ContiguousClustersInChain : 376 -> 332
~ _FAT_Access_M_GetFatEntry : 944 -> 900
~ _FAT_Access_M_ChainLength : 624 -> 580
~ _FAT_Access_M_FATInit : sha256 f6731dae8920d2c15c6c11e60339b1e9d878422c2c2059122e9157379a1a9614 -> df7e0a2e2efbb6ea2a8a786f72bbae2d7103e3f262efd1710b35662b4ca2d14d
~ _FAT_Access_M_FATFini : sha256 c013bfa05c53c25aef51d424c7b5c9241e2a90dba1f22d7143caeecc8298dcfc -> 89edaa962843387f8b898f6b8cb4eaff64e634a723ff09d221d51efdbdeda9d8
~ _FAT_Access_M_FATChainFree : 604 -> 560
~ _FAT_Access_M_SetClustersFatEntryContent : sha256 de68059f8b7e518b43c25e6eb30da2b1d8e23b2260e17039fe7cc0764eaf12c2 -> 8e2e0494ca487d4d1501969cd5a412aa3e2422f535f78e63cb8aedf03da78347
~ _FAT_Access_M_AllocateClusters : 1736 -> 1692
~ _FAT_Access_M_TruncateLastClusters : 512 -> 480
~ _FATMOD_SetDriveDirtyBit : 576 -> 536
~ _FATMOD_FlushSpecificCacheEntry : sha256 1aee8463046d4b575616db5cda391b61867c9372c3771c6535e9930ed46890e4 -> 39ba0473a0146db27ae2d2ae48048d434677f50ebd29672477206a12de5cfacc
~ _FAT_Access_M_GetTotalFreeClusters : 328 -> 284
~ _FAT_Access_M_FreeChainLength : sha256 f971bab1e026179edb6f07beadfce8a0c6c9026246ddee4fe5c266a8f54cea05 -> 1ea4a7230e0c526438c6cb13413ac0a114cfc05746400728bd956200609e4a80
~ _FAT_Access_M_FATChainAlloc : 364 -> 308
~ _ht_AllocateHashTable : sha256 f6bf4927138e8f8464a2dbefb170733e5a8d010bd36691d792721357b5dc5aff -> b5105199f8ea46d40bbc33636c6b65f4c9faecc123235a7e84672678afaa3abb
~ _ht_insert : 564 -> 520
~ _ht_remove : 620 -> 576
~ _ht_remove_from_list : sha256 92b08bad0c6fa825236354c1fad99c372293bdae50d593e0acef00cdec814c4f -> 2e83d27ef81bd92f9ed5a7cad1937ac671b45912fa7385c6ee1183592b0887f7
~ _ht_free_all : 124 -> 128
~ _ht_DeAllocateHashTable : sha256 3ca68149069444d205753f2c850b027889f699b1193f0d4b4dcf64d31ddf5195 -> 020d83cd802a17f51442f1af43b767ae1340f1cb4f60e79a20e9c019b30fcf18
~ _ht_set_incomplete : sha256 4d62dd07002f08b6cd8fd918d62cd23e51f06404e37692664da03225bc185f4f -> 19915b824c7759ea3e4af7e1ab51af89b699dc89788f78296562665e4ffc0635
~ _CONV_UTF8ToUnistr255 : 1324 -> 1364
~ _unicode_combinable : sha256 306fbded61160fc1dec15280775cf2c7cd4eff3004551884929ab3fcb1ebd439 -> 8cb100248fe4c07067adde7b34d700ae4c32111fde4eed29ce1f5fff9ac032f7
~ _priortysort : sha256 777c42caa649b00b7f15d41c7738315844fc8e4e9b6fa58dea419587f8aaa6c2 -> 20ed6990e002ac00ccce70262a24217243166377730f6b367f7c82ba2c43b571
~ _CONV_Unistr255ToUTF8 : 836 -> 840
~ _CONV_Unistr255ToLowerCase : 56 -> 60
~ _CONV_GetCurrentTime : sha256 c217d422daf552f3b99722bed98c45b8bc1e097af9d592d5812b973cd6e10799 -> 207be5482189bdf8282d5e6586cda6a9f0121f9723a5be2405bcc6a7c5b9d442
~ _CONV_UTF8ToLowerCase : 200 -> 204
~ _CONV_ConvertToFSM : 120 -> 124
~ _CONV_DuplicateName : sha256 3bdbe45f7ff6545420c7b240d829c5eed150974b8a3e71d9eacb09e7e62b371d -> 1f41b6fc461a0911811f56b0231e97a9901fc2ca6180aa29b9918ab8411590e7
~ _CONV_LabelUTF8ToUTF16LocalEncoding : 332 -> 344
~ _unicode_recursive_decompose : sha256 fc28a67f08034af1d1fea37dd33eef510730a05526e09b8b63a603a813c48dda -> 00619a148999618b7059241fc1225184c570e19bc2f56bb93c43e8dd9aeeb179
~ _RAWFILE_read : 1236 -> 1192
~ _RAWFILE_write : 1440 -> 1396
~ _DIROPS_FlushEntrySector : sha256 244278e9a13789004431232d193011c2d874a84f6834598ee4e24b4a31af7af2 -> 2ab83df9d593284d6920854c7bcf44d113b8c809d918821ac5c1277df862e90b
~ _DIROPS_UpdateDirLastModifiedTime : 512 -> 468
~ _DIROPS_AllocateDirBlockBuffer : 332 -> 288
~ _DIROPS_GetDirBlockRelative : 1112 -> 1116
~ _DIROPS_FreeDirBlockBuffer : 280 -> 212
~ _DIROPS_GetMD5Digest : 216 -> 220
~ _DIROPS_VerifyIfLinkAndGetLinkLength : 220 -> 224
~ _DIROPS_IsDotOrDotDotName : sha256 c078c6c435a604bfa97c9f82de6707fca8e5f820efa878dd8d7e133bd89a193f -> 4f9c65648d0a946c48edca17acbb1d7c0cddb3226fc956f617095eb2bd2a6505
~ _DIROPS_PurgeNodeMetaBlocksFromCache : sha256 2048995f824fc20da76bcfa1239efbe7a176e4dcfa64c9a1e79e2c0f2b36673d -> 31d3a4a2c2fe0f1a8e6f1cfd75124271ef6b72db2e4dcbcca6ff543c44955158
~ _DIROPS_CreateNewEntry : sha256 47be3628c171faac36b72b3125a6969c1702ef73f47493fe2ea8efbd609c67a6 -> 0a7d3b922839c2f4ca5da43b40e6519911f0811c1ed3f667054cb996a5ab0d0d
~ _DIROPS_LookForFreeEntriesInDirectory : sha256 ba8fe385d36bf3818451ff6c32b3720499903df92a096afc88f7e4a2ee6ff249 -> 326a874d25240eb60570b7580fd3efe16429abe022e16eca947b5c7e1174e6f3
~ _DIROPS_CreateShortNameEntry : 1192 -> 1196
~ _DIROPS_SaveNewEntriesIntoDevice : sha256 220f301148701b5be76f38149571024b65b3442077efe07b97f97c7a29b41099 -> 6783bb058f41ee10ed462393fec1f8c4a54efdb51f2715eb3ffbea957f16a6d6
~ _MSDOS_MkDir : sha256 0776af6d21134065f9ad0a63264e931e8971848a717a85e8039fdca28877961c -> d03cdb48c464ad4d9413e3e19077fdada9640d63b9b7e181b0407b4ad07ea395
~ _DIROPS_CreateHTForDirectory : sha256 f3df0195a88a77ab3f0592342f9e69f9742b6f795883ffb8d5e91d8fdb0ab55c -> d8f7138909c902cea20baffeaf2046ceb4dfc553e7d6daf2e09b94ba113730c0
~ _DIROPS_LookForDirEntryByName : 1360 -> 1316
~ _DIROPS_ClearNewDirectoryClusters : sha256 9c94c5cd94d98d6cfbd8b5dcb12efd21312e1576917bd021fdd713ebf3b96ffa -> 6921c4cbaa0e844f237725f3d5d5f9d86fad4eca66372a0aa1adab86222719b7
~ _DIROPS_LookupInternal : 872 -> 876
~ _DIROPS_ReleaseHTForDirectory : sha256 6cc1eb41688fb91738e19619ad67b525dd47b6f4cf4fe1127a6c06b5b9affce1 -> 850745fb7ddb29f0acca20e27301b12ebb8bad09e7af48b61c0fafcc8934af54
~ _DIROPS_GetRecordId : 856 -> 808
~ _MSDOS_ReadDir : sha256 9c08eff1df0ffd3c01b0c45bfcdad6d813505b912bb65a0841958813c3455e1b -> c310aee80abef530e5fa898ff158c6928fc6cc3edf8ef5fa92474432c217aa89
~ _DIROPS_ReadDirInternal : 2784 -> 2816
~ _MSDOS_ReadDirAttr : sha256 9df7a17c2a5efdeb1606f80151fb9e2ff8a88ae833f5a93c0ea32721990c283c -> e3f509c7e16691f1d41369e8aad4512095afc1b9b251bc0f9261bb6815fbc630
~ _DIROPS_GetFileDirEntryDataByOffset : 640 -> 596
~ _DIROPS_GetDirEntryByOffset : 1468 -> 1436
~ _DIROPS_HandleLongNameCharacter : 88 -> 92
~ _DIROPS_MarkNodeDirEntriesAsDeleted : 1224 -> 1180
~ _DIROPS_PopulateHT : sha256 b131d3d859c80f2f50262a221e8a6bfcdc00c055d329e571b49824db9d9a3926 -> 4438e6febd2e3aacf1db421fdbd691fe99ee08c806c6ab11ceaa8cd39f314027
~ _DIROPS_isDirEmpty : sha256 d40df40a74096ed544ae49056421b93920de3d47fe4e358bdeeaf8ad722da525 -> 77f4dacb5a31ac2bc130aca0894911e50acf17aa0e25abf8fe73866f3726a47e
~ _DIROPS_AcquireHTLRUSlotAndUnlockNode : sha256 2f538c1da7e723c1b3d0f3305b56e74e4555e4f5b3b2b50a1b0826376363796f -> 8acba4df23bb73fad7644a7d2c4f53666b4ddfc2e68d2f5361fc360ace27705c
~ _DIROPS_MaybeFreeEvictedHTAndUnlockNode : sha256 b50c50c4a90cb22509141248b1c5aad16179d6e2c4b9d52ffccb8fd3ec18513b -> d515a9e89d760f62daaa38c90dd009599f2a24edf71f9cf26101d8433e16bd3b
~ _DIROPS_WasEvictedFromHTLRUSlot : sha256 0a298aee7d6eb10d4d7b29628aca1d3ee4b70e81ecacbeaec9bbee4a65df5f26 -> 05f1cdfc3a3285f1527d703476da80ec29dbe34db33d47e36260c27fc9726f29
~ _DIROPS_DestroyHTForDirectory : sha256 daf074ed01373174eda121aa897e31824dba0d8c78e71278ebe745c96514858d -> 49da2d08451b283b31c158c72da4868f0253c4832c57086e0a1a76832d291531
~ _DIROPS_LookForDirEntry : 2700 -> 2712
~ _MSDOS_Lookup : sha256 254e42607ccca87f4af796e0a0697e242b660f6c43e318f6e680e772c4a020cc -> e87d07b0a14f5bb4903c7cba46d1903c10781b3a37d3de47123d842f1981ea2e
~ _MSDOS_Remove : sha256 8194f08b084971b5d182c0680397dc578b1f2a26d5f59ff2ff3135cf3609175a -> d359338339d8e72ff2caeeee694e8864cf7256f029d089898851bb1e2595346b
~ _MSDOS_RmDir : sha256 0c2c93a9190da57fd3b929cbe7a152933df08ec964ef4d634b5802630df38e8b -> 9c60e26c3df4d289a09501db3c37120ba0b24b3b9593393f72044c1c88cde518
~ _DIROPS_UpdateDirectoryEntry : 1188 -> 1144
~ _DIROPS_GetDirBlockAbsolute : sha256 fee45c4e4be899a8deeb36c7fa34e5d04fadd3f0e9aa287615ce6b5def0a27a6 -> 77749b4c5514ef666db35e8f9f3029c7050da4763387824c04563f66c1830b2a
~ _MSDOS_ScanDir : sha256 7957a2af873008094f555bc251d8c06b4563eaf8f41bfb1bd9348b7cc606865a -> f501be33496d567569e4813657f70d9d77d9b7ca4696e9580593b46185c5c060
~ _DIROPS_VerifyCookie : 1168 -> 1124
~ _DIROPS_GetDirEntryOffsetByIndex : sha256 20f5fe8fa896ed2c3dfaa8b007c4e6664d3ff74d2d6d30d14b4de101031a65a1 -> c17e9673f6c13b22f857175a1ada2bf6f12297bf0b5ac7234e68dd9a6dc21685
~ _MSDOS_LoggerInit : sha256 cb75a4c58374bb30e38423ef254a40d6a4a6f8fbbb6ab8c938aa831c2530af7d -> 9441212912aa24af39b35320d836aada585893da1d8c88a04f6dda93255cb979
CStrings:
- "clearMetaBlocks:ranges:rangesCount:wait:"
- "defaultClient"
- "flushMeta:wait:"
- "purgeMetaBlocks:ranges:rangesCount:"
- "readMeta:buffer:offset:length:"
- "readMetaWithRA:buffer:offset:length:raList:raListCount:"
- "writeMeta:buffer:offset:length:"

```
