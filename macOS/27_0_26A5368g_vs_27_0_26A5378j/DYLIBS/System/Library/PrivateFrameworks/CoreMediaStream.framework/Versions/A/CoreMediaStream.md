## CoreMediaStream

> `/System/Library/PrivateFrameworks/CoreMediaStream.framework/Versions/A/CoreMediaStream`

```diff

-  __TEXT.__text: 0xd907c
-  __TEXT.__objc_methlist: 0x82e0
-  __TEXT.__const: 0x248
-  __TEXT.__cstring: 0xa6b0
-  __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__gcc_except_tab: 0x2768
-  __TEXT.__oslogstring: 0xef59
-  __TEXT.__unwind_info: 0x2d50
+  __TEXT.__text: 0xd9628
+  __TEXT.__objc_methlist: 0x8240
+  __TEXT.__const: 0x1b8
+  __TEXT.__cstring: 0xa4dc
+  __TEXT.__gcc_except_tab: 0x2788
+  __TEXT.__oslogstring: 0xef38
+  __TEXT.__unwind_info: 0x2d20
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xea0
-  __DATA_CONST.__objc_classlist: 0x260
+  __DATA_CONST.__const: 0xea8
+  __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4188
+  __DATA_CONST.__objc_selrefs: 0x4068
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x220
-  __DATA_CONST.__got: 0x4f0
-  __AUTH_CONST.__const: 0x25f0
-  __AUTH_CONST.__cfstring: 0x8860
-  __AUTH_CONST.__objc_const: 0x9a58
+  __DATA_CONST.__got: 0x4e0
+  __AUTH_CONST.__const: 0x2720
+  __AUTH_CONST.__cfstring: 0x87e0
+  __AUTH_CONST.__objc_const: 0x9bf0
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0x708
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x714
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__objc_ivar: 0x738
   __DATA.__data: 0xaa0
-  __DATA.__bss: 0x208
+  __DATA.__bss: 0x1d8
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x1770
-  __DATA_DIRTY.__bss: 0x1b0
+  __DATA_DIRTY.__bss: 0x1c0
   - /System/Library/Frameworks/CFNetwork.framework/Versions/A/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/Versions/A/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts

   - /System/Library/PrivateFrameworks/IDS.framework/Versions/A/IDS
   - /System/Library/PrivateFrameworks/MMCS.framework/Versions/A/MMCS
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3712
-  Symbols:   7830
-  CStrings:  3395
+  Functions: 3695
+  Symbols:   7789
+  CStrings:  3365
 
Sections:
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ +[MSASCloudKitPlugin _migrationErrorForCKError:]
+ +[MSProtocolUtilities cancelMigrationToCPLForAlbumWithGUID:personID:clientVersion:completionBlock:]
+ +[MSProtocolUtilities completeMigrationToCPLForAlbumWithGUID:clientOrgKey:personID:clientVersion:sourceAssetCount:destinationAssetCount:completionBlock:]
+ +[MSProtocolUtilities failMigrationToCPLForAlbumWithGUID:migrationError:personID:clientVersion:completionBlock:]
+ +[MSProtocolUtilities initiateMigrationToCPLForAlbumWithGUID:sharedAlbumTitle:personID:isSilentMigration:clientVersion:sourceAssetCount:completionBlock:]
+ +[MSProtocolUtilities unarchiveMigrationToCPLForAlbumWithGUID:personID:clientVersion:completionBlock:]
+ -[CancelSharedCollectionsMigrationRequest clientVersion]
+ -[CancelSharedCollectionsMigrationRequest hasClientVersion]
+ -[CancelSharedCollectionsMigrationRequest setClientVersion:]
+ -[CompleteSharedCollectionsMigrationRequest clientVersion]
+ -[CompleteSharedCollectionsMigrationRequest destinationAssetCount]
+ -[CompleteSharedCollectionsMigrationRequest hasClientVersion]
+ -[CompleteSharedCollectionsMigrationRequest hasDestinationAssetCount]
+ -[CompleteSharedCollectionsMigrationRequest hasSourceAssetCount]
+ -[CompleteSharedCollectionsMigrationRequest setClientVersion:]
+ -[CompleteSharedCollectionsMigrationRequest setDestinationAssetCount:]
+ -[CompleteSharedCollectionsMigrationRequest setHasDestinationAssetCount:]
+ -[CompleteSharedCollectionsMigrationRequest setHasSourceAssetCount:]
+ -[CompleteSharedCollectionsMigrationRequest setSourceAssetCount:]
+ -[CompleteSharedCollectionsMigrationRequest sourceAssetCount]
+ -[FailSharedCollectionsMigrationRequest clientVersion]
+ -[FailSharedCollectionsMigrationRequest hasClientVersion]
+ -[FailSharedCollectionsMigrationRequest setClientVersion:]
+ -[InitiateSharedCollectionsMigrationRequest clientVersion]
+ -[InitiateSharedCollectionsMigrationRequest hasClientVersion]
+ -[InitiateSharedCollectionsMigrationRequest hasSourceAssetCount]
+ -[InitiateSharedCollectionsMigrationRequest setClientVersion:]
+ -[InitiateSharedCollectionsMigrationRequest setHasSourceAssetCount:]
+ -[InitiateSharedCollectionsMigrationRequest setSourceAssetCount:]
+ -[InitiateSharedCollectionsMigrationRequest sourceAssetCount]
+ -[MSASServerSideModel MSASStateMachine:didFinishAlbumSummaryWithAssetCollectionChanges:forAlbum:info:]
+ -[MSASServerSideModel cancelMigrationToCPLForAlbumWithGUID:clientVersion:completionBlock:]
+ -[MSASServerSideModel completeMigrationToCPLForAlbumWithGUID:clientVersion:sourceAssetCount:destinationAssetCount:completionBlock:]
+ -[MSASServerSideModel failMigrationToCPLForAlbumWithGUID:migrationError:clientVersion:completionBlock:]
+ -[MSASServerSideModel initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:clientVersion:sourceAssetCount:completionBlock:]
+ -[MSASServerSideModel refreshContentOfAlbumWithGUID:resetSync:info:completionBlock:]
+ -[MSASServerSideModel unarchiveMigrationToCPLForAlbumWithGUID:clientVersion:completionBlock:]
+ -[MSASStateMachine cancelMigrationToCPLForAlbumWithGUID:clientVersion:completionBlock:]
+ -[MSASStateMachine completeMigrationToCPLForAlbumWithGUID:clientVersion:sourceAssetCount:destinationAssetCount:completionBlock:]
+ -[MSASStateMachine failMigrationToCPLForAlbumWithGUID:migrationError:clientVersion:completionBlock:]
+ -[MSASStateMachine initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:clientVersion:sourceAssetCount:completionBlock:]
+ -[MSASStateMachine refreshContentOfAlbumWithGUID:resetSync:info:completionBlock:]
+ -[MSASStateMachine unarchiveMigrationToCPLForAlbumWithGUID:clientVersion:completionBlock:]
+ -[MSAlbumSharingDaemon cancelMigrationToCPLForAlbumWithGUID:personID:clientVersion:completionBlock:]
+ -[MSAlbumSharingDaemon completeMigrationToCPLForAlbumWithGUID:personID:clientVersion:sourceAssetCount:destinationAssetCount:completionBlock:]
+ -[MSAlbumSharingDaemon failMigrationToCPLForAlbumWithGUID:migrationError:personID:clientVersion:completionBlock:]
+ -[MSAlbumSharingDaemon initiateMigrationToCPLForAlbumWithGUID:personID:isSilentMigration:clientVersion:sourceAssetCount:completionBlock:]
+ -[MSAlbumSharingDaemon refreshContentOfAlbumWithGUID:resetSync:personID:info:completionBlock:]
+ -[MSAlbumSharingDaemon unarchiveMigrationToCPLForAlbumWithGUID:personID:clientVersion:completionBlock:]
+ -[UnarchiveSharedCollectionsMigrationRequest clientVersion]
+ -[UnarchiveSharedCollectionsMigrationRequest hasClientVersion]
+ -[UnarchiveSharedCollectionsMigrationRequest setClientVersion:]
+ GCC_except_table1065
+ GCC_except_table1066
+ GCC_except_table1069
+ GCC_except_table1070
+ GCC_except_table1071
+ GCC_except_table1072
+ GCC_except_table1073
+ GCC_except_table1075
+ GCC_except_table1076
+ GCC_except_table1077
+ GCC_except_table1078
+ GCC_except_table1115
+ GCC_except_table1118
+ GCC_except_table1124
+ GCC_except_table1166
+ GCC_except_table1173
+ GCC_except_table1180
+ GCC_except_table1183
+ GCC_except_table1194
+ GCC_except_table1336
+ GCC_except_table1343
+ GCC_except_table1349
+ GCC_except_table1592
+ GCC_except_table1598
+ GCC_except_table1643
+ GCC_except_table1644
+ GCC_except_table1647
+ GCC_except_table1655
+ GCC_except_table1660
+ GCC_except_table1666
+ GCC_except_table1687
+ GCC_except_table1695
+ GCC_except_table1697
+ GCC_except_table1701
+ GCC_except_table1704
+ GCC_except_table1712
+ GCC_except_table1721
+ GCC_except_table1725
+ GCC_except_table1728
+ GCC_except_table1750
+ GCC_except_table1753
+ GCC_except_table1760
+ GCC_except_table1763
+ GCC_except_table1769
+ GCC_except_table1773
+ GCC_except_table1790
+ GCC_except_table1809
+ GCC_except_table1819
+ GCC_except_table1822
+ GCC_except_table1829
+ GCC_except_table1833
+ GCC_except_table1836
+ GCC_except_table1845
+ GCC_except_table1859
+ GCC_except_table1866
+ GCC_except_table1867
+ GCC_except_table1874
+ GCC_except_table1883
+ GCC_except_table1886
+ GCC_except_table1896
+ GCC_except_table1900
+ GCC_except_table1903
+ GCC_except_table1919
+ GCC_except_table1929
+ GCC_except_table1934
+ GCC_except_table1945
+ GCC_except_table1954
+ GCC_except_table1956
+ GCC_except_table2003
+ GCC_except_table2010
+ GCC_except_table2016
+ GCC_except_table2021
+ GCC_except_table2025
+ GCC_except_table2042
+ GCC_except_table2044
+ GCC_except_table2081
+ GCC_except_table2092
+ GCC_except_table2105
+ GCC_except_table2110
+ GCC_except_table2112
+ GCC_except_table2131
+ GCC_except_table2136
+ GCC_except_table2149
+ GCC_except_table2151
+ GCC_except_table2160
+ GCC_except_table2173
+ GCC_except_table2175
+ GCC_except_table2187
+ GCC_except_table2251
+ GCC_except_table2255
+ GCC_except_table2286
+ GCC_except_table2292
+ GCC_except_table2294
+ GCC_except_table2301
+ GCC_except_table2368
+ GCC_except_table2401
+ GCC_except_table2406
+ GCC_except_table2408
+ GCC_except_table2410
+ GCC_except_table2412
+ GCC_except_table2414
+ GCC_except_table249
+ GCC_except_table251
+ GCC_except_table253
+ GCC_except_table254
+ GCC_except_table256
+ GCC_except_table2678
+ GCC_except_table2679
+ GCC_except_table268
+ GCC_except_table2680
+ GCC_except_table2682
+ GCC_except_table2684
+ GCC_except_table2686
+ GCC_except_table2687
+ GCC_except_table2690
+ GCC_except_table2692
+ GCC_except_table272
+ GCC_except_table2722
+ GCC_except_table2723
+ GCC_except_table2724
+ GCC_except_table2725
+ GCC_except_table2726
+ GCC_except_table2728
+ GCC_except_table2729
+ GCC_except_table273
+ GCC_except_table2730
+ GCC_except_table275
+ GCC_except_table276
+ GCC_except_table2812
+ GCC_except_table2837
+ GCC_except_table2839
+ GCC_except_table2843
+ GCC_except_table2845
+ GCC_except_table2847
+ GCC_except_table2939
+ GCC_except_table2941
+ GCC_except_table2951
+ GCC_except_table2953
+ GCC_except_table2956
+ GCC_except_table2958
+ GCC_except_table3102
+ GCC_except_table3111
+ GCC_except_table3124
+ GCC_except_table3192
+ GCC_except_table3195
+ GCC_except_table3213
+ GCC_except_table3217
+ GCC_except_table3221
+ GCC_except_table3225
+ GCC_except_table3229
+ GCC_except_table3233
+ GCC_except_table3235
+ GCC_except_table3239
+ GCC_except_table3241
+ GCC_except_table3245
+ GCC_except_table3247
+ GCC_except_table3257
+ GCC_except_table3265
+ GCC_except_table3268
+ GCC_except_table3276
+ GCC_except_table3278
+ GCC_except_table3282
+ GCC_except_table3284
+ GCC_except_table3320
+ GCC_except_table3324
+ GCC_except_table3358
+ GCC_except_table3361
+ GCC_except_table3363
+ GCC_except_table3366
+ GCC_except_table3369
+ GCC_except_table3444
+ GCC_except_table3467
+ GCC_except_table3473
+ GCC_except_table3483
+ GCC_except_table3523
+ GCC_except_table3529
+ GCC_except_table3662
+ GCC_except_table3674
+ GCC_except_table3678
+ GCC_except_table3682
+ GCC_except_table373
+ GCC_except_table381
+ GCC_except_table383
+ GCC_except_table387
+ GCC_except_table389
+ GCC_except_table391
+ GCC_except_table400
+ GCC_except_table733
+ GCC_except_table739
+ GCC_except_table854
+ GCC_except_table855
+ GCC_except_table856
+ GCC_except_table857
+ GCC_except_table858
+ GCC_except_table859
+ GCC_except_table89
+ GCC_except_table945
+ OBJC_IVAR_$_CancelSharedCollectionsMigrationRequest._clientVersion
+ OBJC_IVAR_$_CompleteSharedCollectionsMigrationRequest._clientVersion
+ OBJC_IVAR_$_CompleteSharedCollectionsMigrationRequest._destinationAssetCount
+ OBJC_IVAR_$_CompleteSharedCollectionsMigrationRequest._has
+ OBJC_IVAR_$_CompleteSharedCollectionsMigrationRequest._sourceAssetCount
+ OBJC_IVAR_$_FailSharedCollectionsMigrationRequest._clientVersion
+ OBJC_IVAR_$_InitiateSharedCollectionsMigrationRequest._clientVersion
+ OBJC_IVAR_$_InitiateSharedCollectionsMigrationRequest._sourceAssetCount
+ OBJC_IVAR_$_UnarchiveSharedCollectionsMigrationRequest._clientVersion
+ __100-[MSASStateMachine failMigrationToCPLForAlbumWithGUID:migrationError:clientVersion:completionBlock:]_block_invoke
+ __102-[MSASServerSideModel MSASStateMachine:didFinishAlbumSummaryWithAssetCollectionChanges:forAlbum:info:]_block_invoke
+ __124-[MSASStateMachine initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:clientVersion:sourceAssetCount:completionBlock:]_block_invoke
+ __128-[MSASStateMachine completeMigrationToCPLForAlbumWithGUID:clientVersion:sourceAssetCount:destinationAssetCount:completionBlock:]_block_invoke
+ __153+[MSProtocolUtilities initiateMigrationToCPLForAlbumWithGUID:sharedAlbumTitle:personID:isSilentMigration:clientVersion:sourceAssetCount:completionBlock:]_block_invoke
+ __81-[MSASStateMachine refreshContentOfAlbumWithGUID:resetSync:info:completionBlock:]_block_invoke
+ __81-[MSASStateMachine refreshContentOfAlbumWithGUID:resetSync:info:completionBlock:]_block_invoke_2
+ __81-[MSASStateMachine refreshContentOfAlbumWithGUID:resetSync:info:completionBlock:]_block_invoke_3
+ __87-[MSASStateMachine cancelMigrationToCPLForAlbumWithGUID:clientVersion:completionBlock:]_block_invoke
+ __90-[MSASStateMachine unarchiveMigrationToCPLForAlbumWithGUID:clientVersion:completionBlock:]_block_invoke
+ ___100-[MSASStateMachine failMigrationToCPLForAlbumWithGUID:migrationError:clientVersion:completionBlock:]_block_invoke
+ ___100-[MSASStateMachine failMigrationToCPLForAlbumWithGUID:migrationError:clientVersion:completionBlock:]_block_invoke_2
+ ___100-[MSAlbumSharingDaemon cancelMigrationToCPLForAlbumWithGUID:personID:clientVersion:completionBlock:]_block_invoke
+ ___102+[MSProtocolUtilities unarchiveMigrationToCPLForAlbumWithGUID:personID:clientVersion:completionBlock:]_block_invoke
+ ___102-[MSASServerSideModel MSASStateMachine:didFinishAlbumSummaryWithAssetCollectionChanges:forAlbum:info:]_block_invoke
+ ___103-[MSASServerSideModel failMigrationToCPLForAlbumWithGUID:migrationError:clientVersion:completionBlock:]_block_invoke
+ ___103-[MSASServerSideModel failMigrationToCPLForAlbumWithGUID:migrationError:clientVersion:completionBlock:]_block_invoke_2
+ ___103-[MSAlbumSharingDaemon unarchiveMigrationToCPLForAlbumWithGUID:personID:clientVersion:completionBlock:]_block_invoke
+ ___112+[MSProtocolUtilities failMigrationToCPLForAlbumWithGUID:migrationError:personID:clientVersion:completionBlock:]_block_invoke
+ ___113-[MSAlbumSharingDaemon failMigrationToCPLForAlbumWithGUID:migrationError:personID:clientVersion:completionBlock:]_block_invoke
+ ___124-[MSASStateMachine initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:clientVersion:sourceAssetCount:completionBlock:]_block_invoke
+ ___124-[MSASStateMachine initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:clientVersion:sourceAssetCount:completionBlock:]_block_invoke_2
+ ___127-[MSASServerSideModel initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:clientVersion:sourceAssetCount:completionBlock:]_block_invoke
+ ___127-[MSASServerSideModel initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:clientVersion:sourceAssetCount:completionBlock:]_block_invoke_2
+ ___127-[MSASServerSideModel initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:clientVersion:sourceAssetCount:completionBlock:]_block_invoke_3
+ ___128-[MSASStateMachine completeMigrationToCPLForAlbumWithGUID:clientVersion:sourceAssetCount:destinationAssetCount:completionBlock:]_block_invoke
+ ___128-[MSASStateMachine completeMigrationToCPLForAlbumWithGUID:clientVersion:sourceAssetCount:destinationAssetCount:completionBlock:]_block_invoke_2
+ ___131-[MSASServerSideModel completeMigrationToCPLForAlbumWithGUID:clientVersion:sourceAssetCount:destinationAssetCount:completionBlock:]_block_invoke
+ ___131-[MSASServerSideModel completeMigrationToCPLForAlbumWithGUID:clientVersion:sourceAssetCount:destinationAssetCount:completionBlock:]_block_invoke_2
+ ___137-[MSAlbumSharingDaemon initiateMigrationToCPLForAlbumWithGUID:personID:isSilentMigration:clientVersion:sourceAssetCount:completionBlock:]_block_invoke
+ ___141-[MSAlbumSharingDaemon completeMigrationToCPLForAlbumWithGUID:personID:clientVersion:sourceAssetCount:destinationAssetCount:completionBlock:]_block_invoke
+ ___153+[MSProtocolUtilities completeMigrationToCPLForAlbumWithGUID:clientOrgKey:personID:clientVersion:sourceAssetCount:destinationAssetCount:completionBlock:]_block_invoke
+ ___153+[MSProtocolUtilities initiateMigrationToCPLForAlbumWithGUID:sharedAlbumTitle:personID:isSilentMigration:clientVersion:sourceAssetCount:completionBlock:]_block_invoke
+ ___81-[MSASStateMachine refreshContentOfAlbumWithGUID:resetSync:info:completionBlock:]_block_invoke
+ ___81-[MSASStateMachine refreshContentOfAlbumWithGUID:resetSync:info:completionBlock:]_block_invoke_2
+ ___81-[MSASStateMachine refreshContentOfAlbumWithGUID:resetSync:info:completionBlock:]_block_invoke_3
+ ___87-[MSASStateMachine cancelMigrationToCPLForAlbumWithGUID:clientVersion:completionBlock:]_block_invoke
+ ___87-[MSASStateMachine cancelMigrationToCPLForAlbumWithGUID:clientVersion:completionBlock:]_block_invoke_2
+ ___90-[MSASServerSideModel cancelMigrationToCPLForAlbumWithGUID:clientVersion:completionBlock:]_block_invoke
+ ___90-[MSASServerSideModel cancelMigrationToCPLForAlbumWithGUID:clientVersion:completionBlock:]_block_invoke_2
+ ___90-[MSASStateMachine unarchiveMigrationToCPLForAlbumWithGUID:clientVersion:completionBlock:]_block_invoke
+ ___90-[MSASStateMachine unarchiveMigrationToCPLForAlbumWithGUID:clientVersion:completionBlock:]_block_invoke_2
+ ___93-[MSASServerSideModel unarchiveMigrationToCPLForAlbumWithGUID:clientVersion:completionBlock:]_block_invoke
+ ___93-[MSASServerSideModel unarchiveMigrationToCPLForAlbumWithGUID:clientVersion:completionBlock:]_block_invoke_2
+ ___94-[MSAlbumSharingDaemon refreshContentOfAlbumWithGUID:resetSync:personID:info:completionBlock:]_block_invoke
+ ___99+[MSProtocolUtilities cancelMigrationToCPLForAlbumWithGUID:personID:clientVersion:completionBlock:]_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80bs88r96w_e5_v8?0l
+ ___block_descriptor_69_e8_32s40s48s56bs_e5_v8?0l
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e65_v52?0"NSError"8B16"NSArray"20B28"MSASAlbum"32"NSString"40B48l
+ ___block_descriptor_72_e8_32s40s48s56r64w_e5_v8?0l
+ ___block_descriptor_77_e8_32s40s48s56s64bs_e5_v8?0l
+ ___block_descriptor_80_e8_32s40s48s56bs64r72w_e54_v40?0"NSError"8"NSString"16"NSArray"24"NSArray"32l
+ ___block_descriptor_80_e8_32s40s48s56bs64r72w_e5_v8?0l
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e5_v8?0l
+ ___block_descriptor_97_e8_32s40s48s56s64s72s80bs88w_e5_v8?0l
+ ___copy_helper_block_e8_32s40s48s56b64r72w
+ ___copy_helper_block_e8_32s40s48s56s64s72s80b88r96w
+ _kMSASClientVersionKey
+ _kMSASDestinationAssetCountKey
+ _kMSASModelRefreshContentOfAlbumWithGUIDWithCompletionFn
+ _kMSASSourceAssetCountKey
+ _objc_msgSend$MSASStateMachine:didFinishAlbumSummaryWithAssetCollectionChanges:forAlbum:info:
+ _objc_msgSend$_migrationErrorForCKError:
+ _objc_msgSend$cancelMigrationToCPLForAlbumWithGUID:clientVersion:completionBlock:
+ _objc_msgSend$cancelMigrationToCPLForAlbumWithGUID:personID:clientVersion:completionBlock:
+ _objc_msgSend$completeMigrationToCPLForAlbumWithGUID:clientOrgKey:personID:clientVersion:sourceAssetCount:destinationAssetCount:completionBlock:
+ _objc_msgSend$completeMigrationToCPLForAlbumWithGUID:clientVersion:sourceAssetCount:destinationAssetCount:completionBlock:
+ _objc_msgSend$failMigrationToCPLForAlbumWithGUID:migrationError:clientVersion:completionBlock:
+ _objc_msgSend$failMigrationToCPLForAlbumWithGUID:migrationError:personID:clientVersion:completionBlock:
+ _objc_msgSend$initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:clientVersion:sourceAssetCount:completionBlock:
+ _objc_msgSend$initiateMigrationToCPLForAlbumWithGUID:sharedAlbumTitle:personID:isSilentMigration:clientVersion:sourceAssetCount:completionBlock:
+ _objc_msgSend$refreshContentOfAlbumWithGUID:resetSync:info:completionBlock:
+ _objc_msgSend$setClientVersion:
+ _objc_msgSend$setDestinationAssetCount:
+ _objc_msgSend$setSourceAssetCount:
+ _objc_msgSend$unarchiveMigrationToCPLForAlbumWithGUID:clientVersion:completionBlock:
+ _objc_msgSend$unarchiveMigrationToCPLForAlbumWithGUID:personID:clientVersion:completionBlock:
- +[MSASDaemonModel defaultModel]
- +[MSDeleter _clearInstantiatedDeletersByPersonID]
- +[MSFileUtilities hardlinkOrCopyFileFromPath:toPath:outError:]
- +[MSObjectWrapper objectsFromWrappers:equalToObject:]
- +[MSPerformanceLogger nukeCompletionBlock:]
- +[MSProtocolUtilities Win32SHA1OfUDID:]
- +[MSProtocolUtilities cancelMigrationToCPLForAlbumWithGUID:personID:completionBlock:]
- +[MSProtocolUtilities completeMigrationToCPLForAlbumWithGUID:clientOrgKey:personID:completionBlock:]
- +[MSProtocolUtilities failMigrationToCPLForAlbumWithGUID:migrationError:personID:completionBlock:]
- +[MSProtocolUtilities fetchMPSStateWithBaseAvailabilityURL:personID:originalLibrarySize:completionBlock:]
- +[MSProtocolUtilities initiateMigrationToCPLForAlbumWithGUID:sharedAlbumTitle:personID:isSilentMigration:completionBlock:]
- +[MSProtocolUtilities unarchiveMigrationToCPLForAlbumWithGUID:personID:completionBlock:]
- +[MSServerSideConfigManager longValueForParameter:forPersonID:defaultValue:]
- -[MPSStateRequest copyTo:]
- -[MPSStateResponse StringAsIcplAction:]
- -[MPSStateResponse StringAsMpsAction:]
- -[MPSStateResponse copyTo:]
- -[MPSStateResponse icplActionAsString:]
- -[MPSStateResponse mpsActionAsString:]
- -[MSASAssetCollection isAutoloopVideo]
- -[MSASModelBase dbQueueRollbackTransaction]
- -[MSASPersonModel assetCollectionsInUploadQueueAlbumGUID:]
- -[MSASPersonModel assetsInDownloadQueueAlbumGUID:]
- -[MSASPersonModel dbQueueRemoveCommandAtHeadOfQueue]
- -[MSASPersonModel isAssetCollectionWithGUIDPending:]
- -[MSASServerSideModel cancelMigrationToCPLForAlbumWithGUID:completionBlock:]
- -[MSASServerSideModel completeMigrationToCPLForAlbumWithGUID:completionBlock:]
- -[MSASServerSideModel failMigrationToCPLForAlbumWithGUID:migrationError:completionBlock:]
- -[MSASServerSideModel initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:completionBlock:]
- -[MSASServerSideModel unarchiveMigrationToCPLForAlbumWithGUID:completionBlock:]
- -[MSASStateMachine cancelMigrationToCPLForAlbumWithGUID:completionBlock:]
- -[MSASStateMachine completeMigrationToCPLForAlbumWithGUID:completionBlock:]
- -[MSASStateMachine failMigrationToCPLForAlbumWithGUID:migrationError:completionBlock:]
- -[MSASStateMachine initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:completionBlock:]
- -[MSASStateMachine unarchiveMigrationToCPLForAlbumWithGUID:completionBlock:]
- -[MSAlbumSharingDaemon cancelMigrationToCPLForAlbumWithGUID:personID:completionBlock:]
- -[MSAlbumSharingDaemon completeMigrationToCPLForAlbumWithGUID:personID:completionBlock:]
- -[MSAlbumSharingDaemon deleteAssetCollectionWithGUID:personID:]
- -[MSAlbumSharingDaemon failMigrationToCPLForAlbumWithGUID:migrationError:personID:completionBlock:]
- -[MSAlbumSharingDaemon initiateMigrationToCPLForAlbumWithGUID:personID:isSilentMigration:completionBlock:]
- -[MSAlbumSharingDaemon markAlbumGUIDAsViewed:personID:]
- -[MSAlbumSharingDaemon refreshAccessControlListOfAlbumWithGUID:personID:]
- -[MSAlbumSharingDaemon refreshCommentsForAssetCollectionWithGUID:resetSync:personID:]
- -[MSAlbumSharingDaemon rejectInvitationWithGUID:personID:]
- -[MSAlbumSharingDaemon unarchiveMigrationToCPLForAlbumWithGUID:personID:completionBlock:]
- -[MSMediaStreamDaemon computeHashForAsset:personID:]
- -[MSMediaStreamDaemon hasOutstandingActivity]
- -[MSMediaStreamDaemon ownSubscribedStreamForPersonID:]
- -[MSMediaStreamDaemon personIDHasOutstandingPublications:]
- -[MSMediaStreamDaemon resetSubscriberSyncForPersonID:]
- -[MSMediaStreamDaemon subscribedStreamsForPersonID:]
- -[MSObjectQueue removeAllObjectWrappersFromQueue]
- -[NSArray(MSArrayUtilities) MSDeepCopy]
- -[NSData(MSDataUtilities) MSBase64Encoding]
- -[NSData(MSDataUtilities) MSInitWithBase64Encoding:]
- -[NSDictionary(MCDictionaryUtilities) MSDeepCopy]
- -[NSDictionary(MSASDefinitions) MSASEventIsDueToAlbumDeletionAlbumGUID]
- -[NSDictionary(MSASDefinitions) MSASEventIsDueToAssetCollectionDeletionAssetCollectionGUID]
- -[NSDictionary(MSASDefinitions) MSASIsErrorRecovery]
- -[NSDictionary(MSASDefinitions) MSASIsLocalChange]
- -[NSDictionary(MSASDefinitions) MSASIsNotInteresting]
- -[NSError(MMCSKit) MMCSErrorType]
- -[NSError(MSErrorUtilities) MSMakePrimaryError]
- -[NSMutableDictionary(MSASServerSideModel) MSASAddDictionary:]
- -[NSString(MSStringUtilities) MSUniqueID]
- CloudKitLibraryCore.frameworkLibrary
- GCC_except_table1091
- GCC_except_table1092
- GCC_except_table1095
- GCC_except_table1096
- GCC_except_table1097
- GCC_except_table1098
- GCC_except_table1099
- GCC_except_table1101
- GCC_except_table1102
- GCC_except_table1103
- GCC_except_table1104
- GCC_except_table1141
- GCC_except_table1142
- GCC_except_table1145
- GCC_except_table1151
- GCC_except_table1193
- GCC_except_table1200
- GCC_except_table1207
- GCC_except_table1210
- GCC_except_table1221
- GCC_except_table1366
- GCC_except_table1373
- GCC_except_table1379
- GCC_except_table1610
- GCC_except_table1616
- GCC_except_table1661
- GCC_except_table1662
- GCC_except_table1665
- GCC_except_table1678
- GCC_except_table1691
- GCC_except_table1702
- GCC_except_table1705
- GCC_except_table1713
- GCC_except_table1719
- GCC_except_table1722
- GCC_except_table1730
- GCC_except_table1733
- GCC_except_table1739
- GCC_except_table1743
- GCC_except_table1746
- GCC_except_table1768
- GCC_except_table1771
- GCC_except_table1791
- GCC_except_table1799
- GCC_except_table1805
- GCC_except_table1808
- GCC_except_table1814
- GCC_except_table1827
- GCC_except_table1837
- GCC_except_table1847
- GCC_except_table1851
- GCC_except_table1854
- GCC_except_table1863
- GCC_except_table1876
- GCC_except_table1884
- GCC_except_table1885
- GCC_except_table1895
- GCC_except_table1901
- GCC_except_table1904
- GCC_except_table1910
- GCC_except_table1914
- GCC_except_table1918
- GCC_except_table1928
- GCC_except_table1935
- GCC_except_table1951
- GCC_except_table1957
- GCC_except_table1959
- GCC_except_table2006
- GCC_except_table2013
- GCC_except_table2019
- GCC_except_table2024
- GCC_except_table2028
- GCC_except_table2045
- GCC_except_table2047
- GCC_except_table2084
- GCC_except_table2095
- GCC_except_table2108
- GCC_except_table2113
- GCC_except_table2115
- GCC_except_table2134
- GCC_except_table2142
- GCC_except_table2144
- GCC_except_table2159
- GCC_except_table2161
- GCC_except_table2163
- GCC_except_table2167
- GCC_except_table2180
- GCC_except_table2182
- GCC_except_table2184
- GCC_except_table2198
- GCC_except_table2259
- GCC_except_table2263
- GCC_except_table2297
- GCC_except_table2303
- GCC_except_table2305
- GCC_except_table2312
- GCC_except_table2380
- GCC_except_table2413
- GCC_except_table2418
- GCC_except_table2420
- GCC_except_table2422
- GCC_except_table2424
- GCC_except_table2426
- GCC_except_table257
- GCC_except_table261
- GCC_except_table262
- GCC_except_table2658
- GCC_except_table266
- GCC_except_table2697
- GCC_except_table2698
- GCC_except_table2699
- GCC_except_table2701
- GCC_except_table2703
- GCC_except_table2705
- GCC_except_table2706
- GCC_except_table2709
- GCC_except_table2711
- GCC_except_table2741
- GCC_except_table2742
- GCC_except_table2744
- GCC_except_table2745
- GCC_except_table2747
- GCC_except_table2748
- GCC_except_table2749
- GCC_except_table2762
- GCC_except_table279
- GCC_except_table280
- GCC_except_table281
- GCC_except_table282
- GCC_except_table283
- GCC_except_table2831
- GCC_except_table284
- GCC_except_table2856
- GCC_except_table2858
- GCC_except_table2862
- GCC_except_table2864
- GCC_except_table2866
- GCC_except_table2955
- GCC_except_table2957
- GCC_except_table2967
- GCC_except_table2969
- GCC_except_table2972
- GCC_except_table2974
- GCC_except_table3118
- GCC_except_table3127
- GCC_except_table3140
- GCC_except_table3208
- GCC_except_table3211
- GCC_except_table3228
- GCC_except_table3232
- GCC_except_table3236
- GCC_except_table3240
- GCC_except_table3244
- GCC_except_table3248
- GCC_except_table3250
- GCC_except_table3254
- GCC_except_table3256
- GCC_except_table3275
- GCC_except_table3277
- GCC_except_table3280
- GCC_except_table3283
- GCC_except_table3287
- GCC_except_table3291
- GCC_except_table3293
- GCC_except_table3297
- GCC_except_table3299
- GCC_except_table3335
- GCC_except_table3339
- GCC_except_table3373
- GCC_except_table3376
- GCC_except_table3378
- GCC_except_table3381
- GCC_except_table3384
- GCC_except_table3461
- GCC_except_table3484
- GCC_except_table3490
- GCC_except_table3500
- GCC_except_table3540
- GCC_except_table3546
- GCC_except_table3679
- GCC_except_table3691
- GCC_except_table3695
- GCC_except_table3699
- GCC_except_table385
- GCC_except_table399
- GCC_except_table401
- GCC_except_table403
- GCC_except_table405
- GCC_except_table407
- GCC_except_table412
- GCC_except_table753
- GCC_except_table759
- GCC_except_table877
- GCC_except_table878
- GCC_except_table879
- GCC_except_table880
- GCC_except_table881
- GCC_except_table882
- GCC_except_table95
- GCC_except_table970
- MSInitWithBase64Encoding:.DataDecodeTable
- Win32SHA1OfUDID:._prepend
- _CC_MD5_Final
- _CC_MD5_Init
- _CC_MD5_Update
- _CFStringGetCharacterAtIndex
- _MSLog
- _MSLogFile
- _MSMMCSHashForFileAtPath
- _MSMediaStreamDir
- _MSPathDeleteManifestForPersonID
- _MSPathPublishManifestForPersonID
- _MSPathShareManifestForPersonID
- _MSSHA1HashForData
- _MSSHA1HashForFileAtPath
- _MSSPCCreateDataFromHexString
- _MSShouldLogAtLevel
- _OBJC_CLASS_$_MSFileUtilities
- _OBJC_METACLASS_$_MSFileUtilities
- __105+[MSProtocolUtilities fetchMPSStateWithBaseAvailabilityURL:personID:originalLibrarySize:completionBlock:]_block_invoke
- __122+[MSProtocolUtilities initiateMigrationToCPLForAlbumWithGUID:sharedAlbumTitle:personID:isSilentMigration:completionBlock:]_block_invoke
- __73-[MSASStateMachine cancelMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke
- __75-[MSASStateMachine completeMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke
- __76-[MSASStateMachine unarchiveMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke
- __86-[MSASStateMachine failMigrationToCPLForAlbumWithGUID:migrationError:completionBlock:]_block_invoke
- __93-[MSASStateMachine initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:completionBlock:]_block_invoke
- __OBJC_$_CLASS_METHODS_MSASDaemonModel
- __OBJC_$_CLASS_METHODS_MSFileUtilities
- __OBJC_CLASS_RO_$_MSFileUtilities
- __OBJC_METACLASS_RO_$_MSFileUtilities
- ___100+[MSProtocolUtilities completeMigrationToCPLForAlbumWithGUID:clientOrgKey:personID:completionBlock:]_block_invoke
- ___105+[MSProtocolUtilities fetchMPSStateWithBaseAvailabilityURL:personID:originalLibrarySize:completionBlock:]_block_invoke
- ___106-[MSAlbumSharingDaemon initiateMigrationToCPLForAlbumWithGUID:personID:isSilentMigration:completionBlock:]_block_invoke
- ___122+[MSProtocolUtilities initiateMigrationToCPLForAlbumWithGUID:sharedAlbumTitle:personID:isSilentMigration:completionBlock:]_block_invoke
- ___31+[MSASDaemonModel defaultModel]_block_invoke
- ___43+[MSPerformanceLogger nukeCompletionBlock:]_block_invoke
- ___50-[MSASPersonModel assetsInDownloadQueueAlbumGUID:]_block_invoke
- ___52-[MSASPersonModel dbQueueRemoveCommandAtHeadOfQueue]_block_invoke
- ___52-[MSASPersonModel isAssetCollectionWithGUIDPending:]_block_invoke
- ___58-[MSASPersonModel assetCollectionsInUploadQueueAlbumGUID:]_block_invoke
- ___73-[MSASStateMachine cancelMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke
- ___73-[MSASStateMachine cancelMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke_2
- ___75-[MSASStateMachine completeMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke
- ___75-[MSASStateMachine completeMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke_2
- ___76-[MSASServerSideModel cancelMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke
- ___76-[MSASServerSideModel cancelMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke_2
- ___76-[MSASStateMachine unarchiveMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke
- ___76-[MSASStateMachine unarchiveMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke_2
- ___78-[MSASServerSideModel completeMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke
- ___78-[MSASServerSideModel completeMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke_2
- ___79-[MSASServerSideModel unarchiveMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke
- ___79-[MSASServerSideModel unarchiveMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke_2
- ___85+[MSProtocolUtilities cancelMigrationToCPLForAlbumWithGUID:personID:completionBlock:]_block_invoke
- ___86-[MSASStateMachine failMigrationToCPLForAlbumWithGUID:migrationError:completionBlock:]_block_invoke
- ___86-[MSASStateMachine failMigrationToCPLForAlbumWithGUID:migrationError:completionBlock:]_block_invoke_2
- ___86-[MSAlbumSharingDaemon cancelMigrationToCPLForAlbumWithGUID:personID:completionBlock:]_block_invoke
- ___88+[MSProtocolUtilities unarchiveMigrationToCPLForAlbumWithGUID:personID:completionBlock:]_block_invoke
- ___88-[MSAlbumSharingDaemon completeMigrationToCPLForAlbumWithGUID:personID:completionBlock:]_block_invoke
- ___89-[MSASServerSideModel failMigrationToCPLForAlbumWithGUID:migrationError:completionBlock:]_block_invoke
- ___89-[MSASServerSideModel failMigrationToCPLForAlbumWithGUID:migrationError:completionBlock:]_block_invoke_2
- ___89-[MSAlbumSharingDaemon unarchiveMigrationToCPLForAlbumWithGUID:personID:completionBlock:]_block_invoke
- ___93-[MSASStateMachine initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:completionBlock:]_block_invoke
- ___93-[MSASStateMachine initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:completionBlock:]_block_invoke_2
- ___96-[MSASServerSideModel initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:completionBlock:]_block_invoke
- ___96-[MSASServerSideModel initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:completionBlock:]_block_invoke_2
- ___96-[MSASServerSideModel initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:completionBlock:]_block_invoke_3
- ___98+[MSProtocolUtilities failMigrationToCPLForAlbumWithGUID:migrationError:personID:completionBlock:]_block_invoke
- ___99-[MSAlbumSharingDaemon failMigrationToCPLForAlbumWithGUID:migrationError:personID:completionBlock:]_block_invoke
- ___CloudKitLibraryCore_block_invoke
- ___block_descriptor_40_e8_32r_e5_v8?0l
- ___block_descriptor_48_e8_32s40s_e30_v24?0"NSString"8"NSError"16l
- ___chkstk_darwin
- ___error
- ___getCKContainerClass_block_invoke
- __sl_dlopen
- _audit_stringCloudKit
- _dispatch_group_enter
- _dispatch_group_leave
- _link
- _objc_getClass
- _objc_msgSend$MSDeepCopyWithZone:
- _objc_msgSend$MSMutableDeepCopy
- _objc_msgSend$applyUserDefaultOverridesToResponse:
- _objc_msgSend$cancelMigrationToCPLForAlbumWithGUID:completionBlock:
- _objc_msgSend$cancelMigrationToCPLForAlbumWithGUID:personID:completionBlock:
- _objc_msgSend$completeMigrationToCPLForAlbumWithGUID:clientOrgKey:personID:completionBlock:
- _objc_msgSend$completeMigrationToCPLForAlbumWithGUID:completionBlock:
- _objc_msgSend$containerWithIdentifier:
- _objc_msgSend$deleteAssetCollectionWithGUID:personID:info:
- _objc_msgSend$failMigrationToCPLForAlbumWithGUID:migrationError:completionBlock:
- _objc_msgSend$failMigrationToCPLForAlbumWithGUID:migrationError:personID:completionBlock:
- _objc_msgSend$fetchCurrentDeviceIDWithCompletionHandler:
- _objc_msgSend$getCharacters:range:
- _objc_msgSend$handleFailureInFunction:file:lineNumber:description:
- _objc_msgSend$initWithBytesNoCopy:length:encoding:freeWhenDone:
- _objc_msgSend$initWithContentsOfFile:options:error:
- _objc_msgSend$initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:completionBlock:
- _objc_msgSend$initiateMigrationToCPLForAlbumWithGUID:sharedAlbumTitle:personID:isSilentMigration:completionBlock:
- _objc_msgSend$logFacility:level:format:args:
- _objc_msgSend$logFile:func:line:facility:level:format:args:
- _objc_msgSend$longValue
- _objc_msgSend$markAlbumGUIDAsViewed:personID:info:
- _objc_msgSend$ownSubscribedStream
- _objc_msgSend$refreshAccessControlListOfAlbumWithGUID:personID:info:
- _objc_msgSend$refreshCommentsForAssetCollectionWithGUID:resetSync:personID:info:
- _objc_msgSend$rejectInvitationWithGUID:personID:info:
- _objc_msgSend$resetSync
- _objc_msgSend$setOriginalLibrarySize:
- _objc_msgSend$subscribedStreams
- _objc_msgSend$unarchiveMigrationToCPLForAlbumWithGUID:completionBlock:
- _objc_msgSend$unarchiveMigrationToCPLForAlbumWithGUID:personID:completionBlock:
- _strerror
- defaultModel.model
- defaultModel.onceToken
- getCKContainerClass.softClass
CStrings:
+ "%{public}@: Failed to fetch asset collection metadata for album %{public}@ (with completion). Error: %{public}@"
+ "%{public}@: Failed to refresh content of album %{public}@ (with completion). Error: %{public}@"
+ "%{public}@: Reconciling contents of album GUID %{public}@ due to a reset sync (with completion)."
+ "%{public}@: Refreshing content of album %{public}@ (with completion). Reset sync: %d"
+ "%{public}@: Will fetch sharing info changes for reset synced album %{public}@."
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/workspaces/coremediastream/MSPerformanceLogger.m"
+ "CloudKit network failure during shared collection migration"
+ "clientVersion"
+ "destinationAssetCount"
+ "modelRefreshContentOfAlbumWithGUIDWithCompletion"
+ "sourceAssetCount"
- "%s"
- "%{public}@: Copying path %@ to %@."
- "%{public}@: Could not hardlink path %@ to %@. Error: %{public}@"
- "%{public}@: Hardlinked path %@ to %@."
- "%{public}@: Rolling back transaction."
- "(length & 1) == 0"
- "+[MSProtocolUtilities Win32SHA1OfUDID:]"
- "-[NSString(MSStringUtilities) MSUniqueID]"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/workspaces/coremediastream/MSPerformanceLogger.m"
- "/System/Library/Frameworks/CloudKit.framework/Contents/MacOS/CloudKit"
- "CKContainer"
- "Class getCKContainerClass(void)_block_invoke"
- "MPSStateResponse %{public}@"
- "MSProtocolUtilities.m"
- "MSSHA1HashForData"
- "MSSPCCreateDataFromHexString"
- "MSSPCCreateDataFromHexString Could not create data object."
- "MSStringUtilities.m"
- "PersonID %@ using server-side value for parameter %{public}@. Value: %ld"
- "Removing all entries from the queue."
- "Setting MPS deviceID: %@"
- "Setting iCPL deviceID: %@ Error: %@"
- "The file at %@ could not be opened for hashing."
- "Unable to allocate memory for length (%lu)"
- "Unable to find class %s"
- "data is too large to encode"
- "delete from Queue;"
- "iCPLContainer is %p"
- "len <= UINT32_MAX"
- "length < UINT32_MAX"
- "mpsstate"
- "removeAllObjectWrappersFromQueue"
- "rollback transaction;"
- "softlink:r:path:/System/Library/Frameworks/CloudKit.framework/CloudKit"
- "udidLength < UINT32_MAX"
- "unable to allocate memory for length (%lu)"
- "void *CloudKitLibrary(void)"

```
