## CoreMediaStream

> `/System/Library/PrivateFrameworks/CoreMediaStream.framework/CoreMediaStream`

```diff

-  __TEXT.__text: 0xcd34c
-  __TEXT.__objc_methlist: 0x82e0
-  __TEXT.__const: 0x248
-  __TEXT.__cstring: 0xa658
-  __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__gcc_except_tab: 0x2748
-  __TEXT.__oslogstring: 0xefd1
-  __TEXT.__unwind_info: 0x2d80
+  __TEXT.__text: 0xcd3e0
+  __TEXT.__objc_methlist: 0x8240
+  __TEXT.__const: 0x1b8
+  __TEXT.__cstring: 0xa4b5
+  __TEXT.__gcc_except_tab: 0x2770
+  __TEXT.__oslogstring: 0xef38
+  __TEXT.__unwind_info: 0x2d40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x2750
-  __DATA_CONST.__objc_classlist: 0x260
+  __DATA_CONST.__const: 0x2870
+  __DATA_CONST.__objc_classlist: 0x258
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4198
+  __DATA_CONST.__objc_selrefs: 0x4078
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x220
-  __DATA_CONST.__got: 0x500
-  __AUTH_CONST.__const: 0x890
-  __AUTH_CONST.__cfstring: 0x8880
-  __AUTH_CONST.__objc_const: 0x9a58
+  __DATA_CONST.__got: 0x4e8
+  __AUTH_CONST.__const: 0x870
+  __AUTH_CONST.__cfstring: 0x87e0
+  __AUTH_CONST.__objc_const: 0x9bf0
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__auth_got: 0x7f8
-  __AUTH.__objc_data: 0x50
-  __DATA.__objc_ivar: 0x714
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__objc_ivar: 0x738
   __DATA.__data: 0xaa0
-  __DATA.__bss: 0x228
+  __DATA.__bss: 0x1f8
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x1770
-  __DATA_DIRTY.__bss: 0x1b0
+  __DATA_DIRTY.__bss: 0x1c0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /System/Library/PrivateFrameworks/MMCS.framework/MMCS
   - /System/Library/PrivateFrameworks/MobileBackup.framework/MobileBackup
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
-  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 3636
-  Symbols:   11330
-  CStrings:  3400
+  Functions: 3615
+  Symbols:   11272
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
+ GCC_except_table1049
+ GCC_except_table1050
+ GCC_except_table1053
+ GCC_except_table1054
+ GCC_except_table1055
+ GCC_except_table1056
+ GCC_except_table1057
+ GCC_except_table1059
+ GCC_except_table1060
+ GCC_except_table1061
+ GCC_except_table1062
+ GCC_except_table1099
+ GCC_except_table1102
+ GCC_except_table1108
+ GCC_except_table1148
+ GCC_except_table1153
+ GCC_except_table1160
+ GCC_except_table1163
+ GCC_except_table1173
+ GCC_except_table1310
+ GCC_except_table1317
+ GCC_except_table1323
+ GCC_except_table1566
+ GCC_except_table1570
+ GCC_except_table1609
+ GCC_except_table1610
+ GCC_except_table1611
+ GCC_except_table1616
+ GCC_except_table1620
+ GCC_except_table1624
+ GCC_except_table1631
+ GCC_except_table1641
+ GCC_except_table1644
+ GCC_except_table1651
+ GCC_except_table1653
+ GCC_except_table1657
+ GCC_except_table1660
+ GCC_except_table1666
+ GCC_except_table1679
+ GCC_except_table1682
+ GCC_except_table1703
+ GCC_except_table1709
+ GCC_except_table1712
+ GCC_except_table1722
+ GCC_except_table1739
+ GCC_except_table1756
+ GCC_except_table1766
+ GCC_except_table1769
+ GCC_except_table1776
+ GCC_except_table1780
+ GCC_except_table1783
+ GCC_except_table1792
+ GCC_except_table1806
+ GCC_except_table1813
+ GCC_except_table1814
+ GCC_except_table1821
+ GCC_except_table1830
+ GCC_except_table1833
+ GCC_except_table1843
+ GCC_except_table1847
+ GCC_except_table1850
+ GCC_except_table1860
+ GCC_except_table1870
+ GCC_except_table1882
+ GCC_except_table1885
+ GCC_except_table1891
+ GCC_except_table1893
+ GCC_except_table1938
+ GCC_except_table1945
+ GCC_except_table1951
+ GCC_except_table1958
+ GCC_except_table1975
+ GCC_except_table1977
+ GCC_except_table2014
+ GCC_except_table2024
+ GCC_except_table2037
+ GCC_except_table2044
+ GCC_except_table2063
+ GCC_except_table2071
+ GCC_except_table2081
+ GCC_except_table2083
+ GCC_except_table2086
+ GCC_except_table2092
+ GCC_except_table2105
+ GCC_except_table2107
+ GCC_except_table2119
+ GCC_except_table2181
+ GCC_except_table2185
+ GCC_except_table2216
+ GCC_except_table2222
+ GCC_except_table2224
+ GCC_except_table2231
+ GCC_except_table2298
+ GCC_except_table2331
+ GCC_except_table2336
+ GCC_except_table2338
+ GCC_except_table2340
+ GCC_except_table2342
+ GCC_except_table2344
+ GCC_except_table243
+ GCC_except_table245
+ GCC_except_table247
+ GCC_except_table248
+ GCC_except_table250
+ GCC_except_table2608
+ GCC_except_table2609
+ GCC_except_table2610
+ GCC_except_table2612
+ GCC_except_table2614
+ GCC_except_table2616
+ GCC_except_table2617
+ GCC_except_table262
+ GCC_except_table2620
+ GCC_except_table2622
+ GCC_except_table2652
+ GCC_except_table2653
+ GCC_except_table2654
+ GCC_except_table2655
+ GCC_except_table2656
+ GCC_except_table2658
+ GCC_except_table2659
+ GCC_except_table266
+ GCC_except_table2660
+ GCC_except_table267
+ GCC_except_table2673
+ GCC_except_table269
+ GCC_except_table270
+ GCC_except_table2742
+ GCC_except_table2767
+ GCC_except_table2771
+ GCC_except_table2773
+ GCC_except_table2775
+ GCC_except_table2867
+ GCC_except_table2869
+ GCC_except_table2879
+ GCC_except_table2881
+ GCC_except_table2884
+ GCC_except_table2886
+ GCC_except_table3030
+ GCC_except_table3038
+ GCC_except_table3051
+ GCC_except_table3119
+ GCC_except_table3122
+ GCC_except_table3140
+ GCC_except_table3144
+ GCC_except_table3148
+ GCC_except_table3152
+ GCC_except_table3156
+ GCC_except_table3160
+ GCC_except_table3162
+ GCC_except_table3166
+ GCC_except_table3168
+ GCC_except_table3172
+ GCC_except_table3174
+ GCC_except_table3184
+ GCC_except_table3189
+ GCC_except_table3192
+ GCC_except_table3195
+ GCC_except_table3199
+ GCC_except_table3205
+ GCC_except_table3209
+ GCC_except_table3247
+ GCC_except_table3249
+ GCC_except_table3283
+ GCC_except_table3286
+ GCC_except_table3288
+ GCC_except_table3291
+ GCC_except_table3294
+ GCC_except_table3368
+ GCC_except_table3391
+ GCC_except_table3397
+ GCC_except_table3406
+ GCC_except_table3444
+ GCC_except_table3449
+ GCC_except_table3582
+ GCC_except_table3594
+ GCC_except_table3598
+ GCC_except_table3602
+ GCC_except_table367
+ GCC_except_table373
+ GCC_except_table375
+ GCC_except_table377
+ GCC_except_table381
+ GCC_except_table383
+ GCC_except_table390
+ GCC_except_table719
+ GCC_except_table723
+ GCC_except_table83
+ GCC_except_table838
+ GCC_except_table839
+ GCC_except_table840
+ GCC_except_table841
+ GCC_except_table842
+ GCC_except_table843
+ GCC_except_table929
+ OBJC_IVAR_$_CancelSharedCollectionsMigrationRequest._clientVersion
+ OBJC_IVAR_$_CompleteSharedCollectionsMigrationRequest._clientVersion
+ OBJC_IVAR_$_CompleteSharedCollectionsMigrationRequest._destinationAssetCount
+ OBJC_IVAR_$_CompleteSharedCollectionsMigrationRequest._has
+ OBJC_IVAR_$_CompleteSharedCollectionsMigrationRequest._sourceAssetCount
+ OBJC_IVAR_$_FailSharedCollectionsMigrationRequest._clientVersion
+ OBJC_IVAR_$_InitiateSharedCollectionsMigrationRequest._clientVersion
+ OBJC_IVAR_$_InitiateSharedCollectionsMigrationRequest._sourceAssetCount
+ OBJC_IVAR_$_UnarchiveSharedCollectionsMigrationRequest._clientVersion
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
+ ___81-[MSASStateMachine refreshContentOfAlbumWithGUID:resetSync:info:completionBlock:]_block_invoke_4
+ ___81-[MSASStateMachine refreshContentOfAlbumWithGUID:resetSync:info:completionBlock:]_block_invoke_5
+ ___81-[MSASStateMachine refreshContentOfAlbumWithGUID:resetSync:info:completionBlock:]_block_invoke_6
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
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80bs88r96w_e5_v8?0ls32l8w96l8s40l8r88l8s48l8s56l8s80l8s64l8s72l8
+ ___block_descriptor_69_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56bs64w_e65_v52?0"NSError"8B16"NSArray"20B28"MSASAlbum"32"NSString"40B48lw64l8s32l8s56l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56r64w_e5_v8?0lr56l8w64l8s32l8s40l8s48l8
+ ___block_descriptor_77_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56bs64r72w_e54_v40?0"NSError"8"NSString"16"NSArray"24"NSArray"32lw72l8s32l8r64l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56bs64r72w_e5_v8?0lw72l8r64l8s32l8s40l8s48l8s56l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_97_e8_32s40s48s56s64s72s80bs88w_e5_v8?0ls32l8w88l8s40l8s80l8s48l8s56l8s64l8s72l8
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
- GCC_except_table1075
- GCC_except_table1076
- GCC_except_table1079
- GCC_except_table1080
- GCC_except_table1081
- GCC_except_table1082
- GCC_except_table1083
- GCC_except_table1085
- GCC_except_table1086
- GCC_except_table1087
- GCC_except_table1088
- GCC_except_table1125
- GCC_except_table1126
- GCC_except_table1129
- GCC_except_table1135
- GCC_except_table1175
- GCC_except_table1180
- GCC_except_table1187
- GCC_except_table1190
- GCC_except_table1200
- GCC_except_table1340
- GCC_except_table1347
- GCC_except_table1353
- GCC_except_table1584
- GCC_except_table1588
- GCC_except_table1627
- GCC_except_table1628
- GCC_except_table1629
- GCC_except_table1634
- GCC_except_table1638
- GCC_except_table1642
- GCC_except_table1649
- GCC_except_table1659
- GCC_except_table1662
- GCC_except_table1671
- GCC_except_table1678
- GCC_except_table1684
- GCC_except_table1687
- GCC_except_table1693
- GCC_except_table1697
- GCC_except_table1721
- GCC_except_table1740
- GCC_except_table1748
- GCC_except_table1754
- GCC_except_table1757
- GCC_except_table1763
- GCC_except_table1774
- GCC_except_table1784
- GCC_except_table1794
- GCC_except_table1798
- GCC_except_table1801
- GCC_except_table1810
- GCC_except_table1823
- GCC_except_table1831
- GCC_except_table1832
- GCC_except_table1842
- GCC_except_table1848
- GCC_except_table1851
- GCC_except_table1857
- GCC_except_table1861
- GCC_except_table1865
- GCC_except_table1880
- GCC_except_table1887
- GCC_except_table1890
- GCC_except_table1896
- GCC_except_table1898
- GCC_except_table1943
- GCC_except_table1950
- GCC_except_table1961
- GCC_except_table1963
- GCC_except_table1980
- GCC_except_table1982
- GCC_except_table2019
- GCC_except_table2029
- GCC_except_table2047
- GCC_except_table2049
- GCC_except_table2073
- GCC_except_table2076
- GCC_except_table2078
- GCC_except_table2090
- GCC_except_table2093
- GCC_except_table2095
- GCC_except_table2097
- GCC_except_table2101
- GCC_except_table2114
- GCC_except_table2116
- GCC_except_table2118
- GCC_except_table2132
- GCC_except_table2191
- GCC_except_table2195
- GCC_except_table2229
- GCC_except_table2235
- GCC_except_table2237
- GCC_except_table2244
- GCC_except_table2312
- GCC_except_table2345
- GCC_except_table2350
- GCC_except_table2352
- GCC_except_table2354
- GCC_except_table2356
- GCC_except_table2358
- GCC_except_table251
- GCC_except_table255
- GCC_except_table256
- GCC_except_table2591
- GCC_except_table260
- GCC_except_table2631
- GCC_except_table2632
- GCC_except_table2633
- GCC_except_table2635
- GCC_except_table2637
- GCC_except_table2639
- GCC_except_table2640
- GCC_except_table2643
- GCC_except_table2645
- GCC_except_table2675
- GCC_except_table2676
- GCC_except_table2677
- GCC_except_table2678
- GCC_except_table2679
- GCC_except_table2681
- GCC_except_table2682
- GCC_except_table2683
- GCC_except_table2696
- GCC_except_table273
- GCC_except_table274
- GCC_except_table275
- GCC_except_table276
- GCC_except_table277
- GCC_except_table278
- GCC_except_table2788
- GCC_except_table2790
- GCC_except_table2794
- GCC_except_table2796
- GCC_except_table2798
- GCC_except_table2887
- GCC_except_table2889
- GCC_except_table2899
- GCC_except_table2901
- GCC_except_table2904
- GCC_except_table2906
- GCC_except_table3050
- GCC_except_table3058
- GCC_except_table3071
- GCC_except_table3139
- GCC_except_table3142
- GCC_except_table3159
- GCC_except_table3163
- GCC_except_table3167
- GCC_except_table3171
- GCC_except_table3175
- GCC_except_table3179
- GCC_except_table3181
- GCC_except_table3185
- GCC_except_table3191
- GCC_except_table3193
- GCC_except_table3206
- GCC_except_table3208
- GCC_except_table3214
- GCC_except_table3218
- GCC_except_table3222
- GCC_except_table3224
- GCC_except_table3228
- GCC_except_table3230
- GCC_except_table3266
- GCC_except_table3268
- GCC_except_table3302
- GCC_except_table3305
- GCC_except_table3307
- GCC_except_table3310
- GCC_except_table3313
- GCC_except_table3389
- GCC_except_table3412
- GCC_except_table3418
- GCC_except_table3427
- GCC_except_table3465
- GCC_except_table3470
- GCC_except_table3603
- GCC_except_table3615
- GCC_except_table3619
- GCC_except_table3623
- GCC_except_table387
- GCC_except_table389
- GCC_except_table391
- GCC_except_table393
- GCC_except_table395
- GCC_except_table397
- GCC_except_table402
- GCC_except_table739
- GCC_except_table743
- GCC_except_table861
- GCC_except_table862
- GCC_except_table863
- GCC_except_table864
- GCC_except_table865
- GCC_except_table866
- GCC_except_table89
- GCC_except_table954
- _CC_MD5_Final
- _CC_MD5_Init
- _CC_MD5_Update
- _CFStringGetCharacterAtIndex
- _CloudKitLibraryCore.frameworkLibrary
- _MSInitWithBase64Encoding:.DataDecodeTable
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
- _OBJC_CLASS_$_MBManager
- _OBJC_CLASS_$_MSFileUtilities
- _OBJC_METACLASS_$_MSFileUtilities
- _Win32SHA1OfUDID:._prepend
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
- ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
- ___block_descriptor_48_e8_32s40s_e30_v24?0"NSString"8"NSError"16ls32l8s40l8
- ___chkstk_darwin
- ___error
- ___getCKContainerClass_block_invoke
- __sl_dlopen
- _audit_stringCloudKit
- _defaultModel.model
- _defaultModel.onceToken
- _dispatch_group_enter
- _dispatch_group_leave
- _getCKContainerClass
- _getCKContainerClass.softClass
- _link
- _objc_getClass
- _objc_msgSend$MSDeepCopyWithZone:
- _objc_msgSend$MSMutableDeepCopy
- _objc_msgSend$applyUserDefaultOverridesToResponse:
- _objc_msgSend$backupDeviceUDID
- _objc_msgSend$backupDeviceUUID
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
CStrings:
+ "%{public}@: Failed to fetch asset collection metadata for album %{public}@ (with completion). Error: %{public}@"
+ "%{public}@: Failed to refresh content of album %{public}@ (with completion). Error: %{public}@"
+ "%{public}@: Reconciling contents of album GUID %{public}@ due to a reset sync (with completion)."
+ "%{public}@: Refreshing content of album %{public}@ (with completion). Reset sync: %d"
+ "%{public}@: Will fetch sharing info changes for reset synced album %{public}@."
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
- "Setting Backup deviceID: %@ Error: %@"
- "Setting Backup deviceUDID: %@"
- "Setting Backup deviceUUID: %@"
- "Setting MPS deviceID: %@"
- "Setting iCPL deviceID: %@ Error: %@"
- "The file at %@ could not be opened for hashing."
- "Unable to allocate memory for length (%lu)"
- "Unable to find class %s"
- "backupContainer is %p"
- "com.apple.backup.ios"
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
