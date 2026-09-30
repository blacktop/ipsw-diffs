## ContainerManagerCommon

> `/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon`

```diff

-725.0.8.0.0
-  __TEXT.__text: 0xe3f50
+725.0.10.0.0
+  __TEXT.__text: 0xe44fc
   __TEXT.__auth_stubs: 0x2090
-  __TEXT.__objc_methlist: 0xa3a4
+  __TEXT.__objc_methlist: 0xa3ac
   __TEXT.__const: 0xc00
-  __TEXT.__cstring: 0x9025
+  __TEXT.__cstring: 0x9063
   __TEXT.__swift5_typeref: 0x330
-  __TEXT.__oslogstring: 0xe38f
+  __TEXT.__oslogstring: 0xe3be
   __TEXT.__constg_swiftt: 0x2ec
   __TEXT.__swift5_reflstr: 0x113
   __TEXT.__swift5_fieldmd: 0x18c

   __TEXT.__swift5_proto: 0x70
   __TEXT.__swift5_types: 0x58
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__gcc_except_tab: 0x2b0c
+  __TEXT.__gcc_except_tab: 0x2b14
   __TEXT.__ustring: 0x16c
-  __TEXT.__unwind_info: 0x2018
+  __TEXT.__unwind_info: 0x2100
   __TEXT.__eh_frame: 0x160
   __TEXT.__objc_classname: 0x1dd2
-  __TEXT.__objc_methname: 0x135a7
+  __TEXT.__objc_methname: 0x135b0
   __TEXT.__objc_methtype: 0x40f9
-  __TEXT.__objc_stubs: 0xb9c0
+  __TEXT.__objc_stubs: 0xb9e0
   __DATA_CONST.__got: 0x340
   __DATA_CONST.__const: 0x1a58
   __DATA_CONST.__objc_classlist: 0x5c0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x4a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x34e8
+  __DATA_CONST.__objc_selrefs: 0x34f0
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x4e8
   __DATA_CONST.__objc_arraydata: 0x2a8
   __AUTH_CONST.__auth_got: 0x1058
   __AUTH_CONST.__const: 0xb80
-  __AUTH_CONST.__cfstring: 0x45a0
-  __AUTH_CONST.__objc_const: 0x16188
+  __AUTH_CONST.__cfstring: 0x45c0
+  __AUTH_CONST.__objc_const: 0x16198
   __AUTH_CONST.__objc_dictobj: 0x140
-  __AUTH_CONST.__objc_intobj: 0x1458
+  __AUTH_CONST.__objc_intobj: 0x1470
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH.__objc_data: 0xa90
   __AUTH.__data: 0xe0
   __DATA.__objc_ivar: 0xbcc
   __DATA.__data: 0x3838
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0xda8
+  __DATA.__bss: 0xdb8
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x30c0
   __DATA_DIRTY.__data: 0x88

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 752544A9-99CF-39C6-80B7-9B31CCCE105E
-  Functions: 3304
-  Symbols:   11492
-  CStrings:  6091
+  UUID: 13DCE798-1A67-3E71-A40F-FFB0F1052674
+  Functions: 3307
+  Symbols:   11501
+  CStrings:  6096
 
Symbols:
+ +[MCMError unsupported]
+ -[MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier _finalizeWithSynthesizedPathWithReason:containerConfig:error:]
+ -[MCMMetadata _modifiedDictBySettingValue:forKey:onInfo:]
+ GCC_except_table1036
+ GCC_except_table1045
+ GCC_except_table1049
+ GCC_except_table1087
+ GCC_except_table1088
+ GCC_except_table1100
+ GCC_except_table1102
+ GCC_except_table1106
+ GCC_except_table1114
+ GCC_except_table1116
+ GCC_except_table1122
+ GCC_except_table1124
+ GCC_except_table1126
+ GCC_except_table1131
+ GCC_except_table1133
+ GCC_except_table1140
+ GCC_except_table1142
+ GCC_except_table1151
+ GCC_except_table1153
+ GCC_except_table1161
+ GCC_except_table1177
+ GCC_except_table1187
+ GCC_except_table1192
+ GCC_except_table1196
+ GCC_except_table1198
+ GCC_except_table1250
+ GCC_except_table1260
+ GCC_except_table1291
+ GCC_except_table1339
+ GCC_except_table1341
+ GCC_except_table1345
+ GCC_except_table1346
+ GCC_except_table1559
+ GCC_except_table1608
+ GCC_except_table1697
+ GCC_except_table1842
+ GCC_except_table1880
+ GCC_except_table1890
+ GCC_except_table1905
+ GCC_except_table1909
+ GCC_except_table1944
+ GCC_except_table1950
+ GCC_except_table2025
+ GCC_except_table2136
+ GCC_except_table2273
+ GCC_except_table2290
+ GCC_except_table2291
+ GCC_except_table2367
+ GCC_except_table2424
+ GCC_except_table2439
+ GCC_except_table2499
+ GCC_except_table2511
+ GCC_except_table2571
+ GCC_except_table2581
+ GCC_except_table2606
+ GCC_except_table2635
+ GCC_except_table2657
+ GCC_except_table2664
+ GCC_except_table2668
+ GCC_except_table2724
+ GCC_except_table2813
+ GCC_except_table2864
+ GCC_except_table2935
+ GCC_except_table678
+ GCC_except_table679
+ GCC_except_table755
+ GCC_except_table766
+ GCC_except_table828
+ GCC_except_table904
+ GCC_except_table949
+ GCC_except_table980
+ GCC_except_table982
+ ___111-[MCMFileManager createDirectoryAtURL:withIntermediateDirectories:mode:owner:dataProtectionClass:fsNode:error:]_block_invoke.39
+ ___111-[MCMFileManager createDirectoryAtURL:withIntermediateDirectories:mode:owner:dataProtectionClass:fsNode:error:]_block_invoke.58
+ ___23+[MCMError unsupported]_block_invoke
+ ___40-[MCMFileManager stripACLFromURL:error:]_block_invoke.487
+ ___50-[MCMFileManager targetOfSymbolicLinkAtURL:error:]_block_invoke.93
+ ___53-[MCMFileManager _traverseDirectory:error:withBlock:]_block_invoke.160
+ ___53-[MCMFileManager writeData:toURL:options:mode:error:]_block_invoke.383
+ ___55-[MCMFileManager _fixPOSIXPermsOnFD:FTSENT:stat:error:]_block_invoke.627
+ ___55-[MCMFileManager readDataFromURL:options:fsNode:error:]_block_invoke.337
+ ___55-[MCMFileManager readDataFromURL:options:fsNode:error:]_block_invoke.340
+ ___60-[MCMFileManager symbolicallyLinkURL:toSymlinkTarget:error:]_block_invoke.76
+ ___62-[MCMFileManager _copyItemAtURL:toURL:failIfSrcMissing:error:]_block_invoke.104
+ ___62-[MCMFileManager _moveItemAtURL:toURL:failIfSrcMissing:error:]_block_invoke.115
+ ___62-[MCMFileManager standardizeOwnershipAtURL:toPOSIXUser:error:]_block_invoke.244
+ ___63-[MCMFileManager repairPermissionsAtURL:uid:gid:options:error:]_block_invoke.565
+ ___67-[MCMFileManager compareVolumeForURL:versusURL:isSameVolume:error:]_block_invoke.399
+ ___67-[MCMFileManager compareVolumeForURL:versusURL:isSameVolume:error:]_block_invoke.420
+ ___67-[MCMFileManager compareVolumeForURL:versusURL:isSameVolume:error:]_block_invoke.423
+ ___67-[MCMFileManager fixUserPermissionsAtURL:limitToTopLevelURL:error:]_block_invoke.500
+ ___68-[MCMFileManager _enumeratePOSIX1eACLEntriesAtURL:error:usingBlock:]_block_invoke.455
+ ___75-[MCMFileManager checkFileSystemAtURL:isCaseSensitive:canAtomicSwap:error:]_block_invoke.431
+ ___75-[MCMFileManager checkFileSystemAtURL:isCaseSensitive:canAtomicSwap:error:]_block_invoke.434
+ ___75-[MCMFileManager dataProtectionClassOfItemAtURL:dataProtectionClass:error:]_block_invoke.267
+ ___78-[MCMFileManager createTemporaryDirectoryInDirectoryURL:withNamePrefix:error:]_block_invoke.139
+ ___79-[MCMFileManager _CreateSystemUserACEInACL:withPermissions:andFlags:withError:]_block_invoke.226
+ ___91-[MCMFileManager _fixACLOnFD:removeACLFilesec:denyDeleteFilesec:denyDeleteText:path:error:]_block_invoke.616
+ ___95-[MCMFileManager setDataProtectionAtURL:toDataProtectionClass:directoriesOnly:recursive:error:]_block_invoke.578
+ ___Block_byref_object_copy_.11785
+ ___Block_byref_object_copy_.12475
+ ___Block_byref_object_copy_.12820
+ ___Block_byref_object_copy_.14234
+ ___Block_byref_object_copy_.14590
+ ___Block_byref_object_copy_.14848
+ ___Block_byref_object_copy_.2504
+ ___Block_byref_object_copy_.3942
+ ___Block_byref_object_copy_.4340
+ ___Block_byref_object_copy_.5077
+ ___Block_byref_object_copy_.5349
+ ___Block_byref_object_copy_.7283
+ ___Block_byref_object_copy_.7816
+ ___Block_byref_object_copy_.8968
+ ___Block_byref_object_copy_.9160
+ ___Block_byref_object_copy_.9294
+ ___Block_byref_object_copy_.9762
+ ___Block_byref_object_copy_.9991
+ ___Block_byref_object_dispose_.11786
+ ___Block_byref_object_dispose_.12476
+ ___Block_byref_object_dispose_.12821
+ ___Block_byref_object_dispose_.14235
+ ___Block_byref_object_dispose_.14591
+ ___Block_byref_object_dispose_.14849
+ ___Block_byref_object_dispose_.2505
+ ___Block_byref_object_dispose_.3943
+ ___Block_byref_object_dispose_.4341
+ ___Block_byref_object_dispose_.5078
+ ___Block_byref_object_dispose_.5350
+ ___Block_byref_object_dispose_.7284
+ ___Block_byref_object_dispose_.7817
+ ___Block_byref_object_dispose_.8969
+ ___Block_byref_object_dispose_.9161
+ ___Block_byref_object_dispose_.9295
+ ___Block_byref_object_dispose_.9763
+ ___Block_byref_object_dispose_.9992
+ ___block_literal_global.10886
+ ___block_literal_global.11823
+ ___block_literal_global.12028
+ ___block_literal_global.1207
+ ___block_literal_global.1269
+ ___block_literal_global.12829
+ ___block_literal_global.1292
+ ___block_literal_global.1395
+ ___block_literal_global.14582
+ ___block_literal_global.14671
+ ___block_literal_global.14691
+ ___block_literal_global.1755
+ ___block_literal_global.2626
+ ___block_literal_global.463
+ ___block_literal_global.5054
+ ___block_literal_global.539
+ ___block_literal_global.5395
+ ___block_literal_global.6551
+ ___block_literal_global.7175
+ ___block_literal_global.7719
+ ___block_literal_global.8329
+ ___block_literal_global.8599
+ ___block_literal_global.9419
+ ___block_literal_global.9516
+ _defaultManager.onceToken.9408
+ _objc_msgSend$_modifiedDictBySettingValue:forKey:onInfo:
+ _objc_msgSend$unsupported
+ _sharedInstance.instance.12339
+ _sharedInstance.onceToken.10293
+ _sharedInstance.onceToken.12338
+ _unsupported._unsupported
+ _unsupported.onceToken
- -[MCMCommandCreateOrLookupAppGroupByAppGroupIdentifier _finalizeWithSynthesizedPathWithReason:containerIdentity:error:]
- -[MCMMetadata _modifiedDictBySetttingValue:forKey:onInfo:]
- GCC_except_table1033
- GCC_except_table1042
- GCC_except_table1046
- GCC_except_table1084
- GCC_except_table1085
- GCC_except_table1097
- GCC_except_table1099
- GCC_except_table1103
- GCC_except_table1108
- GCC_except_table1113
- GCC_except_table1119
- GCC_except_table1121
- GCC_except_table1123
- GCC_except_table1125
- GCC_except_table1130
- GCC_except_table1134
- GCC_except_table1139
- GCC_except_table1145
- GCC_except_table1150
- GCC_except_table1158
- GCC_except_table1174
- GCC_except_table1184
- GCC_except_table1189
- GCC_except_table1193
- GCC_except_table1195
- GCC_except_table1247
- GCC_except_table1257
- GCC_except_table1288
- GCC_except_table1336
- GCC_except_table1338
- GCC_except_table1342
- GCC_except_table1343
- GCC_except_table1556
- GCC_except_table1605
- GCC_except_table1694
- GCC_except_table1839
- GCC_except_table1877
- GCC_except_table1881
- GCC_except_table1902
- GCC_except_table1906
- GCC_except_table1941
- GCC_except_table1947
- GCC_except_table2019
- GCC_except_table2133
- GCC_except_table2270
- GCC_except_table2287
- GCC_except_table2288
- GCC_except_table2364
- GCC_except_table2421
- GCC_except_table2436
- GCC_except_table2496
- GCC_except_table2508
- GCC_except_table2568
- GCC_except_table2578
- GCC_except_table2603
- GCC_except_table2632
- GCC_except_table2654
- GCC_except_table2658
- GCC_except_table2665
- GCC_except_table2721
- GCC_except_table2810
- GCC_except_table2858
- GCC_except_table2932
- GCC_except_table675
- GCC_except_table676
- GCC_except_table752
- GCC_except_table763
- GCC_except_table825
- GCC_except_table901
- GCC_except_table946
- GCC_except_table977
- GCC_except_table979
- ___111-[MCMFileManager createDirectoryAtURL:withIntermediateDirectories:mode:owner:dataProtectionClass:fsNode:error:]_block_invoke.40
- ___40-[MCMFileManager stripACLFromURL:error:]_block_invoke.481
- ___50-[MCMFileManager targetOfSymbolicLinkAtURL:error:]_block_invoke.81
- ___53-[MCMFileManager _traverseDirectory:error:withBlock:]_block_invoke.148
- ___53-[MCMFileManager writeData:toURL:options:mode:error:]_block_invoke.347
- ___55-[MCMFileManager _fixPOSIXPermsOnFD:FTSENT:stat:error:]_block_invoke.621
- ___55-[MCMFileManager readDataFromURL:options:fsNode:error:]_block_invoke.307
- ___55-[MCMFileManager readDataFromURL:options:fsNode:error:]_block_invoke.334
- ___60-[MCMFileManager symbolicallyLinkURL:toSymlinkTarget:error:]_block_invoke.64
- ___62-[MCMFileManager _copyItemAtURL:toURL:failIfSrcMissing:error:]_block_invoke.98
- ___62-[MCMFileManager _moveItemAtURL:toURL:failIfSrcMissing:error:]_block_invoke.109
- ___62-[MCMFileManager standardizeOwnershipAtURL:toPOSIXUser:error:]_block_invoke.238
- ___63-[MCMFileManager repairPermissionsAtURL:uid:gid:options:error:]_block_invoke.547
- ___67-[MCMFileManager compareVolumeForURL:versusURL:isSameVolume:error:]_block_invoke.393
- ___67-[MCMFileManager compareVolumeForURL:versusURL:isSameVolume:error:]_block_invoke.396
- ___67-[MCMFileManager compareVolumeForURL:versusURL:isSameVolume:error:]_block_invoke.411
- ___67-[MCMFileManager fixUserPermissionsAtURL:limitToTopLevelURL:error:]_block_invoke.494
- ___68-[MCMFileManager _enumeratePOSIX1eACLEntriesAtURL:error:usingBlock:]_block_invoke.443
- ___75-[MCMFileManager checkFileSystemAtURL:isCaseSensitive:canAtomicSwap:error:]_block_invoke.425
- ___75-[MCMFileManager checkFileSystemAtURL:isCaseSensitive:canAtomicSwap:error:]_block_invoke.428
- ___75-[MCMFileManager dataProtectionClassOfItemAtURL:dataProtectionClass:error:]_block_invoke.261
- ___78-[MCMFileManager createTemporaryDirectoryInDirectoryURL:withNamePrefix:error:]_block_invoke.133
- ___79-[MCMFileManager _CreateSystemUserACEInACL:withPermissions:andFlags:withError:]_block_invoke.166
- ___91-[MCMFileManager _fixACLOnFD:removeACLFilesec:denyDeleteFilesec:denyDeleteText:path:error:]_block_invoke.586
- ___95-[MCMFileManager setDataProtectionAtURL:toDataProtectionClass:directoriesOnly:recursive:error:]_block_invoke.572
- ___Block_byref_object_copy_.11783
- ___Block_byref_object_copy_.12473
- ___Block_byref_object_copy_.12819
- ___Block_byref_object_copy_.14231
- ___Block_byref_object_copy_.14587
- ___Block_byref_object_copy_.14845
- ___Block_byref_object_copy_.2505
- ___Block_byref_object_copy_.3943
- ___Block_byref_object_copy_.4342
- ___Block_byref_object_copy_.5075
- ___Block_byref_object_copy_.5347
- ___Block_byref_object_copy_.7280
- ___Block_byref_object_copy_.7813
- ___Block_byref_object_copy_.8964
- ___Block_byref_object_copy_.9156
- ___Block_byref_object_copy_.9290
- ___Block_byref_object_copy_.9758
- ___Block_byref_object_copy_.9987
- ___Block_byref_object_dispose_.11784
- ___Block_byref_object_dispose_.12474
- ___Block_byref_object_dispose_.12820
- ___Block_byref_object_dispose_.14232
- ___Block_byref_object_dispose_.14588
- ___Block_byref_object_dispose_.14846
- ___Block_byref_object_dispose_.2506
- ___Block_byref_object_dispose_.3944
- ___Block_byref_object_dispose_.4343
- ___Block_byref_object_dispose_.5076
- ___Block_byref_object_dispose_.5348
- ___Block_byref_object_dispose_.7281
- ___Block_byref_object_dispose_.7814
- ___Block_byref_object_dispose_.8965
- ___Block_byref_object_dispose_.9157
- ___Block_byref_object_dispose_.9291
- ___Block_byref_object_dispose_.9759
- ___Block_byref_object_dispose_.9988
- ___block_literal_global.10884
- ___block_literal_global.11821
- ___block_literal_global.12026
- ___block_literal_global.1208
- ___block_literal_global.1270
- ___block_literal_global.12828
- ___block_literal_global.1293
- ___block_literal_global.1399
- ___block_literal_global.14579
- ___block_literal_global.14668
- ___block_literal_global.14688
- ___block_literal_global.1758
- ___block_literal_global.2627
- ___block_literal_global.457
- ___block_literal_global.5051
- ___block_literal_global.533
- ___block_literal_global.5393
- ___block_literal_global.6548
- ___block_literal_global.7172
- ___block_literal_global.7716
- ___block_literal_global.8326
- ___block_literal_global.8596
- ___block_literal_global.9415
- ___block_literal_global.9512
- _defaultManager.onceToken.9404
- _objc_msgSend$_modifiedDictBySetttingValue:forKey:onInfo:
- _sharedInstance.instance.12337
- _sharedInstance.onceToken.10289
- _sharedInstance.onceToken.12336
CStrings:
+ "23:13:18"
+ "Error should be set if result is not."
+ "Jun 30 2025"
+ "MobileContainerManager-725.0.10~142"
+ "Unexpected result with nil error; type = [%s]."
+ "_finalizeWithSynthesizedPathWithReason:containerConfig:error:"
+ "_modifiedDictBySettingValue:forKey:onInfo:"
+ "dirfd of %s failed: %s"
+ "unsupported"
- "00:54:12"
- "Jun 17 2025"
- "MobileContainerManager-725.0.8~334"
- "_finalizeWithSynthesizedPathWithReason:containerIdentity:error:"
- "_modifiedDictBySetttingValue:forKey:onInfo:"

```
