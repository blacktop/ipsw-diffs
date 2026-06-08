## CoreMediaStream

> `/System/Library/PrivateFrameworks/CoreMediaStream.framework/CoreMediaStream`

```diff

-852.0.102.0.0
-  __TEXT.__text: 0xc7d00
-  __TEXT.__auth_stubs: 0xf40
-  __TEXT.__objc_methlist: 0x74e8
-  __TEXT.__const: 0x1eb
-  __TEXT.__cstring: 0xa004
+910.14.107.0.0
+  __TEXT.__text: 0xcbad0
+  __TEXT.__objc_methlist: 0x8110
+  __TEXT.__const: 0x238
+  __TEXT.__cstring: 0xa5f7
   __TEXT.__dlopen_cstrs: 0x47
-  __TEXT.__gcc_except_tab: 0x2f54
-  __TEXT.__oslogstring: 0xe918
-  __TEXT.__unwind_info: 0x2e08
-  __TEXT.__objc_classname: 0x813
-  __TEXT.__objc_methname: 0x12ac4
-  __TEXT.__objc_methtype: 0x438d
-  __TEXT.__objc_stubs: 0xc940
-  __DATA_CONST.__got: 0x4a0
-  __DATA_CONST.__const: 0x22f8
-  __DATA_CONST.__objc_classlist: 0x200
+  __TEXT.__gcc_except_tab: 0x2748
+  __TEXT.__oslogstring: 0xef75
+  __TEXT.__unwind_info: 0x2d90
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x26a8
+  __DATA_CONST.__objc_classlist: 0x260
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3ee0
+  __DATA_CONST.__objc_selrefs: 0x4150
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1c0
-  __AUTH_CONST.__auth_got: 0x7b0
+  __DATA_CONST.__objc_superrefs: 0x220
+  __DATA_CONST.__got: 0x500
   __AUTH_CONST.__const: 0x890
-  __AUTH_CONST.__cfstring: 0x80e0
-  __AUTH_CONST.__objc_const: 0x8768
-  __AUTH_CONST.__objc_intobj: 0x30
-  __DATA.__objc_ivar: 0x654
+  __AUTH_CONST.__cfstring: 0x87c0
+  __AUTH_CONST.__objc_const: 0x97d8
+  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH_CONST.__auth_got: 0x7f8
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x6ec
   __DATA.__data: 0xaa0
   __DATA.__bss: 0x228
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0x1400
+  __DATA_DIRTY.__objc_data: 0x1770
   __DATA_DIRTY.__bss: 0x1b0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 2D695642-5BA6-3993-AFFB-E21F26DB5D70
-  Functions: 3280
-  Symbols:   10395
-  CStrings:  6294
+  UUID: 26B6D377-B5C0-3DEC-8FDE-D67CE829537A
+  Functions: 3597
+  Symbols:   11237
+  CStrings:  3387
 
Symbols:
+ +[InitiateSharedCollectionsMigrationResponse personIdToCKUserIdType]
+ +[MSProtocolUtilities _errorForSCMigrationStatusCode:]
+ +[MSProtocolUtilities cancelMigrationToCPLForAlbumWithGUID:personID:completionBlock:]
+ +[MSProtocolUtilities completeMigrationToCPLForAlbumWithGUID:clientOrgKey:personID:completionBlock:]
+ +[MSProtocolUtilities failMigrationToCPLForAlbumWithGUID:migrationError:personID:completionBlock:]
+ +[MSProtocolUtilities initiateMigrationToCPLForAlbumWithGUID:sharedAlbumTitle:personID:isSilentMigration:completionBlock:]
+ +[MSProtocolUtilities unarchiveMigrationToCPLForAlbumWithGUID:personID:completionBlock:]
+ -[CancelSharedCollectionsMigrationRequest .cxx_destruct]
+ -[CancelSharedCollectionsMigrationRequest copyTo:]
+ -[CancelSharedCollectionsMigrationRequest copyWithZone:]
+ -[CancelSharedCollectionsMigrationRequest description]
+ -[CancelSharedCollectionsMigrationRequest dictionaryRepresentation]
+ -[CancelSharedCollectionsMigrationRequest hasSaAlbumGuid]
+ -[CancelSharedCollectionsMigrationRequest hash]
+ -[CancelSharedCollectionsMigrationRequest isEqual:]
+ -[CancelSharedCollectionsMigrationRequest mergeFrom:]
+ -[CancelSharedCollectionsMigrationRequest readFrom:]
+ -[CancelSharedCollectionsMigrationRequest saAlbumGuid]
+ -[CancelSharedCollectionsMigrationRequest setSaAlbumGuid:]
+ -[CancelSharedCollectionsMigrationRequest writeTo:]
+ -[CancelSharedCollectionsMigrationResponse StringAsStatus:]
+ -[CancelSharedCollectionsMigrationResponse copyTo:]
+ -[CancelSharedCollectionsMigrationResponse copyWithZone:]
+ -[CancelSharedCollectionsMigrationResponse description]
+ -[CancelSharedCollectionsMigrationResponse dictionaryRepresentation]
+ -[CancelSharedCollectionsMigrationResponse hasStatus]
+ -[CancelSharedCollectionsMigrationResponse hash]
+ -[CancelSharedCollectionsMigrationResponse isEqual:]
+ -[CancelSharedCollectionsMigrationResponse mergeFrom:]
+ -[CancelSharedCollectionsMigrationResponse readFrom:]
+ -[CancelSharedCollectionsMigrationResponse setHasStatus:]
+ -[CancelSharedCollectionsMigrationResponse setStatus:]
+ -[CancelSharedCollectionsMigrationResponse statusAsString:]
+ -[CancelSharedCollectionsMigrationResponse status]
+ -[CancelSharedCollectionsMigrationResponse writeTo:]
+ -[CompleteSharedCollectionsMigrationRequest .cxx_destruct]
+ -[CompleteSharedCollectionsMigrationRequest clientOrgKey]
+ -[CompleteSharedCollectionsMigrationRequest copyTo:]
+ -[CompleteSharedCollectionsMigrationRequest copyWithZone:]
+ -[CompleteSharedCollectionsMigrationRequest description]
+ -[CompleteSharedCollectionsMigrationRequest dictionaryRepresentation]
+ -[CompleteSharedCollectionsMigrationRequest hasClientOrgKey]
+ -[CompleteSharedCollectionsMigrationRequest hasSaAlbumGuid]
+ -[CompleteSharedCollectionsMigrationRequest hash]
+ -[CompleteSharedCollectionsMigrationRequest isEqual:]
+ -[CompleteSharedCollectionsMigrationRequest mergeFrom:]
+ -[CompleteSharedCollectionsMigrationRequest readFrom:]
+ -[CompleteSharedCollectionsMigrationRequest saAlbumGuid]
+ -[CompleteSharedCollectionsMigrationRequest setClientOrgKey:]
+ -[CompleteSharedCollectionsMigrationRequest setSaAlbumGuid:]
+ -[CompleteSharedCollectionsMigrationRequest writeTo:]
+ -[CompleteSharedCollectionsMigrationResponse StringAsStatus:]
+ -[CompleteSharedCollectionsMigrationResponse copyTo:]
+ -[CompleteSharedCollectionsMigrationResponse copyWithZone:]
+ -[CompleteSharedCollectionsMigrationResponse description]
+ -[CompleteSharedCollectionsMigrationResponse dictionaryRepresentation]
+ -[CompleteSharedCollectionsMigrationResponse hasStatus]
+ -[CompleteSharedCollectionsMigrationResponse hash]
+ -[CompleteSharedCollectionsMigrationResponse isEqual:]
+ -[CompleteSharedCollectionsMigrationResponse mergeFrom:]
+ -[CompleteSharedCollectionsMigrationResponse readFrom:]
+ -[CompleteSharedCollectionsMigrationResponse setHasStatus:]
+ -[CompleteSharedCollectionsMigrationResponse setStatus:]
+ -[CompleteSharedCollectionsMigrationResponse statusAsString:]
+ -[CompleteSharedCollectionsMigrationResponse status]
+ -[CompleteSharedCollectionsMigrationResponse writeTo:]
+ -[FailSharedCollectionsMigrationRequest .cxx_destruct]
+ -[FailSharedCollectionsMigrationRequest copyTo:]
+ -[FailSharedCollectionsMigrationRequest copyWithZone:]
+ -[FailSharedCollectionsMigrationRequest description]
+ -[FailSharedCollectionsMigrationRequest dictionaryRepresentation]
+ -[FailSharedCollectionsMigrationRequest errorCode]
+ -[FailSharedCollectionsMigrationRequest errorDomain]
+ -[FailSharedCollectionsMigrationRequest hasErrorCode]
+ -[FailSharedCollectionsMigrationRequest hasErrorDomain]
+ -[FailSharedCollectionsMigrationRequest hasSaAlbumGuid]
+ -[FailSharedCollectionsMigrationRequest hash]
+ -[FailSharedCollectionsMigrationRequest isEqual:]
+ -[FailSharedCollectionsMigrationRequest mergeFrom:]
+ -[FailSharedCollectionsMigrationRequest readFrom:]
+ -[FailSharedCollectionsMigrationRequest saAlbumGuid]
+ -[FailSharedCollectionsMigrationRequest setErrorCode:]
+ -[FailSharedCollectionsMigrationRequest setErrorDomain:]
+ -[FailSharedCollectionsMigrationRequest setHasErrorCode:]
+ -[FailSharedCollectionsMigrationRequest setSaAlbumGuid:]
+ -[FailSharedCollectionsMigrationRequest writeTo:]
+ -[FailSharedCollectionsMigrationResponse StringAsStatus:]
+ -[FailSharedCollectionsMigrationResponse copyTo:]
+ -[FailSharedCollectionsMigrationResponse copyWithZone:]
+ -[FailSharedCollectionsMigrationResponse description]
+ -[FailSharedCollectionsMigrationResponse dictionaryRepresentation]
+ -[FailSharedCollectionsMigrationResponse hasStatus]
+ -[FailSharedCollectionsMigrationResponse hash]
+ -[FailSharedCollectionsMigrationResponse isEqual:]
+ -[FailSharedCollectionsMigrationResponse mergeFrom:]
+ -[FailSharedCollectionsMigrationResponse readFrom:]
+ -[FailSharedCollectionsMigrationResponse setHasStatus:]
+ -[FailSharedCollectionsMigrationResponse setStatus:]
+ -[FailSharedCollectionsMigrationResponse statusAsString:]
+ -[FailSharedCollectionsMigrationResponse status]
+ -[FailSharedCollectionsMigrationResponse writeTo:]
+ -[InitiateSharedCollectionsMigrationRequest .cxx_destruct]
+ -[InitiateSharedCollectionsMigrationRequest archiveKeyword]
+ -[InitiateSharedCollectionsMigrationRequest archiveTitle]
+ -[InitiateSharedCollectionsMigrationRequest copyTo:]
+ -[InitiateSharedCollectionsMigrationRequest copyWithZone:]
+ -[InitiateSharedCollectionsMigrationRequest description]
+ -[InitiateSharedCollectionsMigrationRequest dictionaryRepresentation]
+ -[InitiateSharedCollectionsMigrationRequest hasArchiveKeyword]
+ -[InitiateSharedCollectionsMigrationRequest hasArchiveTitle]
+ -[InitiateSharedCollectionsMigrationRequest hasIsSilentMigration]
+ -[InitiateSharedCollectionsMigrationRequest hasSaAlbumGuid]
+ -[InitiateSharedCollectionsMigrationRequest hash]
+ -[InitiateSharedCollectionsMigrationRequest isEqual:]
+ -[InitiateSharedCollectionsMigrationRequest isSilentMigration]
+ -[InitiateSharedCollectionsMigrationRequest mergeFrom:]
+ -[InitiateSharedCollectionsMigrationRequest readFrom:]
+ -[InitiateSharedCollectionsMigrationRequest saAlbumGuid]
+ -[InitiateSharedCollectionsMigrationRequest setArchiveKeyword:]
+ -[InitiateSharedCollectionsMigrationRequest setArchiveTitle:]
+ -[InitiateSharedCollectionsMigrationRequest setHasIsSilentMigration:]
+ -[InitiateSharedCollectionsMigrationRequest setIsSilentMigration:]
+ -[InitiateSharedCollectionsMigrationRequest setSaAlbumGuid:]
+ -[InitiateSharedCollectionsMigrationRequest writeTo:]
+ -[InitiateSharedCollectionsMigrationResponse .cxx_destruct]
+ -[InitiateSharedCollectionsMigrationResponse StringAsStatus:]
+ -[InitiateSharedCollectionsMigrationResponse addPersonIdToCKUserId:]
+ -[InitiateSharedCollectionsMigrationResponse clearPersonIdToCKUserIds]
+ -[InitiateSharedCollectionsMigrationResponse copyTo:]
+ -[InitiateSharedCollectionsMigrationResponse copyWithZone:]
+ -[InitiateSharedCollectionsMigrationResponse description]
+ -[InitiateSharedCollectionsMigrationResponse dictionaryRepresentation]
+ -[InitiateSharedCollectionsMigrationResponse hasScZoneIdentifier]
+ -[InitiateSharedCollectionsMigrationResponse hasStatus]
+ -[InitiateSharedCollectionsMigrationResponse hash]
+ -[InitiateSharedCollectionsMigrationResponse isEqual:]
+ -[InitiateSharedCollectionsMigrationResponse mergeFrom:]
+ -[InitiateSharedCollectionsMigrationResponse personIdToCKUserIdAtIndex:]
+ -[InitiateSharedCollectionsMigrationResponse personIdToCKUserIdsCount]
+ -[InitiateSharedCollectionsMigrationResponse personIdToCKUserIds]
+ -[InitiateSharedCollectionsMigrationResponse readFrom:]
+ -[InitiateSharedCollectionsMigrationResponse scZoneIdentifier]
+ -[InitiateSharedCollectionsMigrationResponse setHasStatus:]
+ -[InitiateSharedCollectionsMigrationResponse setPersonIdToCKUserIds:]
+ -[InitiateSharedCollectionsMigrationResponse setScZoneIdentifier:]
+ -[InitiateSharedCollectionsMigrationResponse setStatus:]
+ -[InitiateSharedCollectionsMigrationResponse statusAsString:]
+ -[InitiateSharedCollectionsMigrationResponse status]
+ -[InitiateSharedCollectionsMigrationResponse writeTo:]
+ -[MSASAlbum descriptionForSCMigrationState:]
+ -[MSASAlbum setSharedCollectionMigrationExpungeDate:]
+ -[MSASAlbum setSharedCollectionMigrationState:]
+ -[MSASAlbum setSharedCollectionZoneIdentifier:]
+ -[MSASAlbum sharedCollectionMigrationExpungeDate]
+ -[MSASAlbum sharedCollectionMigrationState]
+ -[MSASAlbum sharedCollectionZoneIdentifier]
+ -[MSASDirectAssetDownloader .cxx_destruct]
+ -[MSASDirectAssetDownloader MMCSEngine:didCreateRequestorContext:forAssets:]
+ -[MSASDirectAssetDownloader MMCSEngine:didFinishGettingAsset:path:error:]
+ -[MSASDirectAssetDownloader MMCSEngine:didFinishPuttingAsset:putReceipt:error:]
+ -[MSASDirectAssetDownloader MMCSEngine:didMakeGetProgress:state:onAsset:]
+ -[MSASDirectAssetDownloader MMCSEngine:didMakePutProgress:state:onAsset:]
+ -[MSASDirectAssetDownloader _attemptReauthAndRetryForAsset:originalError:]
+ -[MSASDirectAssetDownloader _finishWithPath:error:]
+ -[MSASDirectAssetDownloader _startDownloadForAsset:]
+ -[MSASDirectAssetDownloader cleanUpWorkingDirectory]
+ -[MSASDirectAssetDownloader didFinishGettingAllAssets]
+ -[MSASDirectAssetDownloader didFinishPuttingAllAssets]
+ -[MSASDirectAssetDownloader downloadAsset:protocol:album:albumURLString:completionBlock:]
+ -[MSASDirectAssetDownloader initWithPersonID:]
+ -[MSASDirectAssetDownloader shutDownCompletionBlock:]
+ -[MSASProtocol updateAlbum:albumURLString:sharedCollectionMigrationState:completionBlock:]
+ -[MSASServerSideModel cancelMigrationToCPLForAlbumWithGUID:completionBlock:]
+ -[MSASServerSideModel completeMigrationToCPLForAlbumWithGUID:completionBlock:]
+ -[MSASServerSideModel failMigrationToCPLForAlbumWithGUID:migrationError:completionBlock:]
+ -[MSASServerSideModel initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:completionBlock:]
+ -[MSASServerSideModel refreshAccessControlListForAlbumWithGUID:info:completionBlock:]
+ -[MSASServerSideModel refreshResetSync:info:completionBlock:]
+ -[MSASServerSideModel setSharedCollectionMigrationState:forAlbumWithGUID:info:]
+ -[MSASServerSideModel unarchiveMigrationToCPLForAlbumWithGUID:completionBlock:]
+ -[MSASStateMachine cancelMigrationToCPLForAlbumWithGUID:completionBlock:]
+ -[MSASStateMachine checkForChangesResetSync:info:completionBlock:]
+ -[MSASStateMachine completeMigrationToCPLForAlbumWithGUID:completionBlock:]
+ -[MSASStateMachine failMigrationToCPLForAlbumWithGUID:migrationError:completionBlock:]
+ -[MSASStateMachine getAccessControlsForAlbumWithGUID:info:completionBlock:]
+ -[MSASStateMachine initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:completionBlock:]
+ -[MSASStateMachine unarchiveMigrationToCPLForAlbumWithGUID:completionBlock:]
+ -[MSAlbumSharingDaemon cancelMigrationToCPLForAlbumWithGUID:personID:completionBlock:]
+ -[MSAlbumSharingDaemon completeMigrationToCPLForAlbumWithGUID:personID:completionBlock:]
+ -[MSAlbumSharingDaemon failMigrationToCPLForAlbumWithGUID:migrationError:personID:completionBlock:]
+ -[MSAlbumSharingDaemon initiateMigrationToCPLForAlbumWithGUID:personID:isSilentMigration:completionBlock:]
+ -[MSAlbumSharingDaemon refreshAccessControlListOfAlbumWithGUID:personID:info:completionBlock:]
+ -[MSAlbumSharingDaemon refreshResetSync:personID:info:completionBlock:]
+ -[MSAlbumSharingDaemon retrieveAsset:inAlbumWithGUID:personID:destinationPath:completionBlock:]
+ -[MSAlbumSharingDaemon setSharedCollectionMigrationState:forAlbumWithGUID:personID:info:]
+ -[MSAlbumSharingDaemon unarchiveMigrationToCPLForAlbumWithGUID:personID:completionBlock:]
+ -[NSError(MMCSKit) MMCSIsRetryableDownloadError]
+ -[NSError(MSErrorUtilities) MSASMigrationErrorIsNotMigrating]
+ -[PersonIdToCKUserIdEntry .cxx_destruct]
+ -[PersonIdToCKUserIdEntry copyTo:]
+ -[PersonIdToCKUserIdEntry copyWithZone:]
+ -[PersonIdToCKUserIdEntry description]
+ -[PersonIdToCKUserIdEntry dictionaryRepresentation]
+ -[PersonIdToCKUserIdEntry hasKey]
+ -[PersonIdToCKUserIdEntry hasValue]
+ -[PersonIdToCKUserIdEntry hash]
+ -[PersonIdToCKUserIdEntry isEqual:]
+ -[PersonIdToCKUserIdEntry key]
+ -[PersonIdToCKUserIdEntry mergeFrom:]
+ -[PersonIdToCKUserIdEntry readFrom:]
+ -[PersonIdToCKUserIdEntry setKey:]
+ -[PersonIdToCKUserIdEntry setValue:]
+ -[PersonIdToCKUserIdEntry value]
+ -[PersonIdToCKUserIdEntry writeTo:]
+ -[UnarchiveSharedCollectionsMigrationRequest .cxx_destruct]
+ -[UnarchiveSharedCollectionsMigrationRequest copyTo:]
+ -[UnarchiveSharedCollectionsMigrationRequest copyWithZone:]
+ -[UnarchiveSharedCollectionsMigrationRequest description]
+ -[UnarchiveSharedCollectionsMigrationRequest dictionaryRepresentation]
+ -[UnarchiveSharedCollectionsMigrationRequest hasSaAlbumGuid]
+ -[UnarchiveSharedCollectionsMigrationRequest hash]
+ -[UnarchiveSharedCollectionsMigrationRequest isEqual:]
+ -[UnarchiveSharedCollectionsMigrationRequest mergeFrom:]
+ -[UnarchiveSharedCollectionsMigrationRequest readFrom:]
+ -[UnarchiveSharedCollectionsMigrationRequest saAlbumGuid]
+ -[UnarchiveSharedCollectionsMigrationRequest setSaAlbumGuid:]
+ -[UnarchiveSharedCollectionsMigrationRequest writeTo:]
+ -[UnarchiveSharedCollectionsMigrationResponse StringAsStatus:]
+ -[UnarchiveSharedCollectionsMigrationResponse copyTo:]
+ -[UnarchiveSharedCollectionsMigrationResponse copyWithZone:]
+ -[UnarchiveSharedCollectionsMigrationResponse description]
+ -[UnarchiveSharedCollectionsMigrationResponse dictionaryRepresentation]
+ -[UnarchiveSharedCollectionsMigrationResponse hasStatus]
+ -[UnarchiveSharedCollectionsMigrationResponse hash]
+ -[UnarchiveSharedCollectionsMigrationResponse isEqual:]
+ -[UnarchiveSharedCollectionsMigrationResponse mergeFrom:]
+ -[UnarchiveSharedCollectionsMigrationResponse readFrom:]
+ -[UnarchiveSharedCollectionsMigrationResponse setHasStatus:]
+ -[UnarchiveSharedCollectionsMigrationResponse setStatus:]
+ -[UnarchiveSharedCollectionsMigrationResponse statusAsString:]
+ -[UnarchiveSharedCollectionsMigrationResponse status]
+ -[UnarchiveSharedCollectionsMigrationResponse writeTo:]
+ GCC_except_table1059
+ GCC_except_table1060
+ GCC_except_table1063
+ GCC_except_table1064
+ GCC_except_table1065
+ GCC_except_table1066
+ GCC_except_table1067
+ GCC_except_table1069
+ GCC_except_table1070
+ GCC_except_table1071
+ GCC_except_table1072
+ GCC_except_table1109
+ GCC_except_table1110
+ GCC_except_table1113
+ GCC_except_table1119
+ GCC_except_table1159
+ GCC_except_table1164
+ GCC_except_table1171
+ GCC_except_table1174
+ GCC_except_table1184
+ GCC_except_table1324
+ GCC_except_table1331
+ GCC_except_table1337
+ GCC_except_table1553
+ GCC_except_table1557
+ GCC_except_table1596
+ GCC_except_table1598
+ GCC_except_table1603
+ GCC_except_table1607
+ GCC_except_table1611
+ GCC_except_table1618
+ GCC_except_table1628
+ GCC_except_table1631
+ GCC_except_table1638
+ GCC_except_table1640
+ GCC_except_table1644
+ GCC_except_table1647
+ GCC_except_table1653
+ GCC_except_table1656
+ GCC_except_table1662
+ GCC_except_table1669
+ GCC_except_table1687
+ GCC_except_table1690
+ GCC_except_table1699
+ GCC_except_table1705
+ GCC_except_table1709
+ GCC_except_table1714
+ GCC_except_table1717
+ GCC_except_table1723
+ GCC_except_table1726
+ GCC_except_table1732
+ GCC_except_table1743
+ GCC_except_table1753
+ GCC_except_table1756
+ GCC_except_table1767
+ GCC_except_table1770
+ GCC_except_table1774
+ GCC_except_table1779
+ GCC_except_table1793
+ GCC_except_table1800
+ GCC_except_table1801
+ GCC_except_table1808
+ GCC_except_table1820
+ GCC_except_table1826
+ GCC_except_table1844
+ GCC_except_table1849
+ GCC_except_table1856
+ GCC_except_table1859
+ GCC_except_table1865
+ GCC_except_table1867
+ GCC_except_table1912
+ GCC_except_table1919
+ GCC_except_table1925
+ GCC_except_table1930
+ GCC_except_table1932
+ GCC_except_table1949
+ GCC_except_table1951
+ GCC_except_table1988
+ GCC_except_table1998
+ GCC_except_table2011
+ GCC_except_table2016
+ GCC_except_table2018
+ GCC_except_table2037
+ GCC_except_table2042
+ GCC_except_table2045
+ GCC_except_table2047
+ GCC_except_table2057
+ GCC_except_table2059
+ GCC_except_table2062
+ GCC_except_table2064
+ GCC_except_table2066
+ GCC_except_table2070
+ GCC_except_table2083
+ GCC_except_table2085
+ GCC_except_table2087
+ GCC_except_table2101
+ GCC_except_table2152
+ GCC_except_table2156
+ GCC_except_table2190
+ GCC_except_table2196
+ GCC_except_table2198
+ GCC_except_table2205
+ GCC_except_table2273
+ GCC_except_table2306
+ GCC_except_table2311
+ GCC_except_table2313
+ GCC_except_table2315
+ GCC_except_table2317
+ GCC_except_table2319
+ GCC_except_table2552
+ GCC_except_table2592
+ GCC_except_table2593
+ GCC_except_table2594
+ GCC_except_table2596
+ GCC_except_table2598
+ GCC_except_table2600
+ GCC_except_table2601
+ GCC_except_table2604
+ GCC_except_table2606
+ GCC_except_table2636
+ GCC_except_table2637
+ GCC_except_table2638
+ GCC_except_table2639
+ GCC_except_table2640
+ GCC_except_table2642
+ GCC_except_table2643
+ GCC_except_table2644
+ GCC_except_table2657
+ GCC_except_table2726
+ GCC_except_table2749
+ GCC_except_table2751
+ GCC_except_table2755
+ GCC_except_table2757
+ GCC_except_table2759
+ GCC_except_table2848
+ GCC_except_table2860
+ GCC_except_table2865
+ GCC_except_table2867
+ GCC_except_table3011
+ GCC_except_table3019
+ GCC_except_table3032
+ GCC_except_table3100
+ GCC_except_table3103
+ GCC_except_table3120
+ GCC_except_table3124
+ GCC_except_table3128
+ GCC_except_table3132
+ GCC_except_table3136
+ GCC_except_table3140
+ GCC_except_table3142
+ GCC_except_table3146
+ GCC_except_table3148
+ GCC_except_table3152
+ GCC_except_table3154
+ GCC_except_table3164
+ GCC_except_table3167
+ GCC_except_table3169
+ GCC_except_table3172
+ GCC_except_table3175
+ GCC_except_table3179
+ GCC_except_table3183
+ GCC_except_table3185
+ GCC_except_table3189
+ GCC_except_table3191
+ GCC_except_table3227
+ GCC_except_table3229
+ GCC_except_table3266
+ GCC_except_table3268
+ GCC_except_table3271
+ GCC_except_table3274
+ GCC_except_table3350
+ GCC_except_table3373
+ GCC_except_table3379
+ GCC_except_table3388
+ GCC_except_table3426
+ GCC_except_table3431
+ GCC_except_table3564
+ GCC_except_table3576
+ GCC_except_table3580
+ GCC_except_table3584
+ GCC_except_table402
+ GCC_except_table723
+ GCC_except_table727
+ GCC_except_table845
+ GCC_except_table846
+ GCC_except_table847
+ GCC_except_table848
+ GCC_except_table849
+ GCC_except_table850
+ GCC_except_table938
+ OBJC_IVAR_$_CancelSharedCollectionsMigrationRequest._saAlbumGuid
+ OBJC_IVAR_$_CancelSharedCollectionsMigrationResponse._has
+ OBJC_IVAR_$_CancelSharedCollectionsMigrationResponse._status
+ OBJC_IVAR_$_CompleteSharedCollectionsMigrationRequest._clientOrgKey
+ OBJC_IVAR_$_CompleteSharedCollectionsMigrationRequest._saAlbumGuid
+ OBJC_IVAR_$_CompleteSharedCollectionsMigrationResponse._has
+ OBJC_IVAR_$_CompleteSharedCollectionsMigrationResponse._status
+ OBJC_IVAR_$_FailSharedCollectionsMigrationRequest._errorCode
+ OBJC_IVAR_$_FailSharedCollectionsMigrationRequest._errorDomain
+ OBJC_IVAR_$_FailSharedCollectionsMigrationRequest._has
+ OBJC_IVAR_$_FailSharedCollectionsMigrationRequest._saAlbumGuid
+ OBJC_IVAR_$_FailSharedCollectionsMigrationResponse._has
+ OBJC_IVAR_$_FailSharedCollectionsMigrationResponse._status
+ OBJC_IVAR_$_InitiateSharedCollectionsMigrationRequest._archiveKeyword
+ OBJC_IVAR_$_InitiateSharedCollectionsMigrationRequest._archiveTitle
+ OBJC_IVAR_$_InitiateSharedCollectionsMigrationRequest._has
+ OBJC_IVAR_$_InitiateSharedCollectionsMigrationRequest._isSilentMigration
+ OBJC_IVAR_$_InitiateSharedCollectionsMigrationRequest._saAlbumGuid
+ OBJC_IVAR_$_InitiateSharedCollectionsMigrationResponse._has
+ OBJC_IVAR_$_InitiateSharedCollectionsMigrationResponse._personIdToCKUserIds
+ OBJC_IVAR_$_InitiateSharedCollectionsMigrationResponse._scZoneIdentifier
+ OBJC_IVAR_$_InitiateSharedCollectionsMigrationResponse._status
+ OBJC_IVAR_$_PersonIdToCKUserIdEntry._key
+ OBJC_IVAR_$_PersonIdToCKUserIdEntry._value
+ OBJC_IVAR_$_UnarchiveSharedCollectionsMigrationRequest._saAlbumGuid
+ OBJC_IVAR_$_UnarchiveSharedCollectionsMigrationResponse._has
+ OBJC_IVAR_$_UnarchiveSharedCollectionsMigrationResponse._status
+ _CancelSharedCollectionsMigrationRequestReadFrom
+ _CancelSharedCollectionsMigrationResponseReadFrom
+ _CompleteSharedCollectionsMigrationRequestReadFrom
+ _CompleteSharedCollectionsMigrationResponseReadFrom
+ _FailSharedCollectionsMigrationRequestReadFrom
+ _FailSharedCollectionsMigrationResponseReadFrom
+ _InitiateSharedCollectionsMigrationRequestReadFrom
+ _InitiateSharedCollectionsMigrationResponseReadFrom
+ _MSPathMigrationMMCSLibraryForPersonID
+ _OBJC_CLASS_$_CancelSharedCollectionsMigrationRequest
+ _OBJC_CLASS_$_CancelSharedCollectionsMigrationResponse
+ _OBJC_CLASS_$_CompleteSharedCollectionsMigrationRequest
+ _OBJC_CLASS_$_CompleteSharedCollectionsMigrationResponse
+ _OBJC_CLASS_$_FailSharedCollectionsMigrationRequest
+ _OBJC_CLASS_$_FailSharedCollectionsMigrationResponse
+ _OBJC_CLASS_$_InitiateSharedCollectionsMigrationRequest
+ _OBJC_CLASS_$_InitiateSharedCollectionsMigrationResponse
+ _OBJC_CLASS_$_MSASDirectAssetDownloader
+ _OBJC_CLASS_$_PersonIdToCKUserIdEntry
+ _OBJC_CLASS_$_UnarchiveSharedCollectionsMigrationRequest
+ _OBJC_CLASS_$_UnarchiveSharedCollectionsMigrationResponse
+ _OBJC_IVAR_$_MSASAlbum._sharedCollectionMigrationExpungeDate
+ _OBJC_IVAR_$_MSASAlbum._sharedCollectionMigrationState
+ _OBJC_IVAR_$_MSASAlbum._sharedCollectionZoneIdentifier
+ _OBJC_IVAR_$_MSASDirectAssetDownloader._album
+ _OBJC_IVAR_$_MSASDirectAssetDownloader._albumURLString
+ _OBJC_IVAR_$_MSASDirectAssetDownloader._completionBlock
+ _OBJC_IVAR_$_MSASDirectAssetDownloader._currentAsset
+ _OBJC_IVAR_$_MSASDirectAssetDownloader._didAttemptReauth
+ _OBJC_IVAR_$_MSASDirectAssetDownloader._engine
+ _OBJC_IVAR_$_MSASDirectAssetDownloader._personID
+ _OBJC_IVAR_$_MSASDirectAssetDownloader._protocol
+ _OBJC_IVAR_$_MSASDirectAssetDownloader._workQueue
+ _OBJC_METACLASS_$_CancelSharedCollectionsMigrationRequest
+ _OBJC_METACLASS_$_CancelSharedCollectionsMigrationResponse
+ _OBJC_METACLASS_$_CompleteSharedCollectionsMigrationRequest
+ _OBJC_METACLASS_$_CompleteSharedCollectionsMigrationResponse
+ _OBJC_METACLASS_$_FailSharedCollectionsMigrationRequest
+ _OBJC_METACLASS_$_FailSharedCollectionsMigrationResponse
+ _OBJC_METACLASS_$_InitiateSharedCollectionsMigrationRequest
+ _OBJC_METACLASS_$_InitiateSharedCollectionsMigrationResponse
+ _OBJC_METACLASS_$_MSASDirectAssetDownloader
+ _OBJC_METACLASS_$_PersonIdToCKUserIdEntry
+ _OBJC_METACLASS_$_UnarchiveSharedCollectionsMigrationRequest
+ _OBJC_METACLASS_$_UnarchiveSharedCollectionsMigrationResponse
+ _PBDataWriterWriteBOOLField
+ _PBDataWriterWriteSubmessage
+ _PBReaderPlaceMark
+ _PBReaderRecallMark
+ _PersonIdToCKUserIdEntryReadFrom
+ _UnarchiveSharedCollectionsMigrationRequestReadFrom
+ _UnarchiveSharedCollectionsMigrationResponseReadFrom
+ __OBJC_$_CLASS_METHODS_InitiateSharedCollectionsMigrationResponse
+ __OBJC_$_INSTANCE_METHODS_CancelSharedCollectionsMigrationRequest
+ __OBJC_$_INSTANCE_METHODS_CancelSharedCollectionsMigrationResponse
+ __OBJC_$_INSTANCE_METHODS_CompleteSharedCollectionsMigrationRequest
+ __OBJC_$_INSTANCE_METHODS_CompleteSharedCollectionsMigrationResponse
+ __OBJC_$_INSTANCE_METHODS_FailSharedCollectionsMigrationRequest
+ __OBJC_$_INSTANCE_METHODS_FailSharedCollectionsMigrationResponse
+ __OBJC_$_INSTANCE_METHODS_InitiateSharedCollectionsMigrationRequest
+ __OBJC_$_INSTANCE_METHODS_InitiateSharedCollectionsMigrationResponse
+ __OBJC_$_INSTANCE_METHODS_MSASDirectAssetDownloader
+ __OBJC_$_INSTANCE_METHODS_PersonIdToCKUserIdEntry
+ __OBJC_$_INSTANCE_METHODS_UnarchiveSharedCollectionsMigrationRequest
+ __OBJC_$_INSTANCE_METHODS_UnarchiveSharedCollectionsMigrationResponse
+ __OBJC_$_INSTANCE_VARIABLES_CancelSharedCollectionsMigrationRequest
+ __OBJC_$_INSTANCE_VARIABLES_CancelSharedCollectionsMigrationResponse
+ __OBJC_$_INSTANCE_VARIABLES_CompleteSharedCollectionsMigrationRequest
+ __OBJC_$_INSTANCE_VARIABLES_CompleteSharedCollectionsMigrationResponse
+ __OBJC_$_INSTANCE_VARIABLES_FailSharedCollectionsMigrationRequest
+ __OBJC_$_INSTANCE_VARIABLES_FailSharedCollectionsMigrationResponse
+ __OBJC_$_INSTANCE_VARIABLES_InitiateSharedCollectionsMigrationRequest
+ __OBJC_$_INSTANCE_VARIABLES_InitiateSharedCollectionsMigrationResponse
+ __OBJC_$_INSTANCE_VARIABLES_MSASDirectAssetDownloader
+ __OBJC_$_INSTANCE_VARIABLES_PersonIdToCKUserIdEntry
+ __OBJC_$_INSTANCE_VARIABLES_UnarchiveSharedCollectionsMigrationRequest
+ __OBJC_$_INSTANCE_VARIABLES_UnarchiveSharedCollectionsMigrationResponse
+ __OBJC_$_PROP_LIST_CancelSharedCollectionsMigrationRequest
+ __OBJC_$_PROP_LIST_CancelSharedCollectionsMigrationResponse
+ __OBJC_$_PROP_LIST_CompleteSharedCollectionsMigrationRequest
+ __OBJC_$_PROP_LIST_CompleteSharedCollectionsMigrationResponse
+ __OBJC_$_PROP_LIST_FailSharedCollectionsMigrationRequest
+ __OBJC_$_PROP_LIST_FailSharedCollectionsMigrationResponse
+ __OBJC_$_PROP_LIST_InitiateSharedCollectionsMigrationRequest
+ __OBJC_$_PROP_LIST_InitiateSharedCollectionsMigrationResponse
+ __OBJC_$_PROP_LIST_MSASDirectAssetDownloader
+ __OBJC_$_PROP_LIST_MSDeleter.130
+ __OBJC_$_PROP_LIST_MSPublisher.295
+ __OBJC_$_PROP_LIST_MSSubscriber.258
+ __OBJC_$_PROP_LIST_PersonIdToCKUserIdEntry
+ __OBJC_$_PROP_LIST_UnarchiveSharedCollectionsMigrationRequest
+ __OBJC_$_PROP_LIST_UnarchiveSharedCollectionsMigrationResponse
+ __OBJC_CLASS_PROTOCOLS_$_CancelSharedCollectionsMigrationRequest
+ __OBJC_CLASS_PROTOCOLS_$_CancelSharedCollectionsMigrationResponse
+ __OBJC_CLASS_PROTOCOLS_$_CompleteSharedCollectionsMigrationRequest
+ __OBJC_CLASS_PROTOCOLS_$_CompleteSharedCollectionsMigrationResponse
+ __OBJC_CLASS_PROTOCOLS_$_FailSharedCollectionsMigrationRequest
+ __OBJC_CLASS_PROTOCOLS_$_FailSharedCollectionsMigrationResponse
+ __OBJC_CLASS_PROTOCOLS_$_InitiateSharedCollectionsMigrationRequest
+ __OBJC_CLASS_PROTOCOLS_$_InitiateSharedCollectionsMigrationResponse
+ __OBJC_CLASS_PROTOCOLS_$_MSASDirectAssetDownloader
+ __OBJC_CLASS_PROTOCOLS_$_PersonIdToCKUserIdEntry
+ __OBJC_CLASS_PROTOCOLS_$_UnarchiveSharedCollectionsMigrationRequest
+ __OBJC_CLASS_PROTOCOLS_$_UnarchiveSharedCollectionsMigrationResponse
+ __OBJC_CLASS_RO_$_CancelSharedCollectionsMigrationRequest
+ __OBJC_CLASS_RO_$_CancelSharedCollectionsMigrationResponse
+ __OBJC_CLASS_RO_$_CompleteSharedCollectionsMigrationRequest
+ __OBJC_CLASS_RO_$_CompleteSharedCollectionsMigrationResponse
+ __OBJC_CLASS_RO_$_FailSharedCollectionsMigrationRequest
+ __OBJC_CLASS_RO_$_FailSharedCollectionsMigrationResponse
+ __OBJC_CLASS_RO_$_InitiateSharedCollectionsMigrationRequest
+ __OBJC_CLASS_RO_$_InitiateSharedCollectionsMigrationResponse
+ __OBJC_CLASS_RO_$_MSASDirectAssetDownloader
+ __OBJC_CLASS_RO_$_PersonIdToCKUserIdEntry
+ __OBJC_CLASS_RO_$_UnarchiveSharedCollectionsMigrationRequest
+ __OBJC_CLASS_RO_$_UnarchiveSharedCollectionsMigrationResponse
+ __OBJC_METACLASS_RO_$_CancelSharedCollectionsMigrationRequest
+ __OBJC_METACLASS_RO_$_CancelSharedCollectionsMigrationResponse
+ __OBJC_METACLASS_RO_$_CompleteSharedCollectionsMigrationRequest
+ __OBJC_METACLASS_RO_$_CompleteSharedCollectionsMigrationResponse
+ __OBJC_METACLASS_RO_$_FailSharedCollectionsMigrationRequest
+ __OBJC_METACLASS_RO_$_FailSharedCollectionsMigrationResponse
+ __OBJC_METACLASS_RO_$_InitiateSharedCollectionsMigrationRequest
+ __OBJC_METACLASS_RO_$_InitiateSharedCollectionsMigrationResponse
+ __OBJC_METACLASS_RO_$_MSASDirectAssetDownloader
+ __OBJC_METACLASS_RO_$_PersonIdToCKUserIdEntry
+ __OBJC_METACLASS_RO_$_UnarchiveSharedCollectionsMigrationRequest
+ __OBJC_METACLASS_RO_$_UnarchiveSharedCollectionsMigrationResponse
+ ___100+[MSProtocolUtilities completeMigrationToCPLForAlbumWithGUID:clientOrgKey:personID:completionBlock:]_block_invoke
+ ___106-[MSAlbumSharingDaemon initiateMigrationToCPLForAlbumWithGUID:personID:isSilentMigration:completionBlock:]_block_invoke
+ ___122+[MSProtocolUtilities initiateMigrationToCPLForAlbumWithGUID:sharedAlbumTitle:personID:isSilentMigration:completionBlock:]_block_invoke
+ ___122+[MSProtocolUtilities initiateMigrationToCPLForAlbumWithGUID:sharedAlbumTitle:personID:isSilentMigration:completionBlock:]_block_invoke.93
+ ___44-[MSASStateMachine shutDownCompletionBlock:]_block_invoke.50
+ ___44-[MSASStateMachine shutDownCompletionBlock:]_block_invoke.54
+ ___44-[MSASStateMachine shutDownCompletionBlock:]_block_invoke_2.53
+ ___44-[MSASStateMachine shutDownCompletionBlock:]_block_invoke_2.55
+ ___46-[MSASDirectAssetDownloader initWithPersonID:]_block_invoke
+ ___47-[MSASStateMachine workQueuePerformNextCommand]_block_invoke.79
+ ___47-[MSASStateMachine workQueuePerformNextCommand]_block_invoke.83
+ ___47-[MSASStateMachine workQueuePerformNextCommand]_block_invoke_2.84
+ ___48-[MSASStateMachine initWithPersonID:eventQueue:]_block_invoke.43
+ ___48-[MSASStateMachine initWithPersonID:eventQueue:]_block_invoke_2.44
+ ___48-[MSASStateMachine workQueueCheckForNextCommand]_block_invoke.78
+ ___48-[NSError(MMCSKit) MMCSIsRetryableDownloadError]_block_invoke
+ ___50-[MSASStateMachine _addCommentDisposition:params:]_block_invoke.289
+ ___50-[MSASStateMachine _addCommentDisposition:params:]_block_invoke.290
+ ___50-[MSASStateMachine _addCommentDisposition:params:]_block_invoke.291
+ ___50-[MSASStateMachine _addCommentDisposition:params:]_block_invoke_2.292
+ ___51-[MSASStateMachine _createAlbumDisposition:params:]_block_invoke.239
+ ___51-[MSASStateMachine _createAlbumDisposition:params:]_block_invoke.240
+ ___51-[MSASStateMachine _createAlbumDisposition:params:]_block_invoke_2.241
+ ___51-[MSASStateMachine _deleteAlbumDisposition:params:]_block_invoke.223
+ ___51-[MSASStateMachine _deleteAlbumDisposition:params:]_block_invoke.224
+ ___51-[MSASStateMachine _deleteAlbumDisposition:params:]_block_invoke_2.225
+ ___51-[MSASStateMachine _updateAlbumDisposition:params:]_block_invoke.245
+ ___51-[MSASStateMachine _updateAlbumDisposition:params:]_block_invoke.246
+ ___51-[MSASStateMachine _updateAlbumDisposition:params:]_block_invoke_2.247
+ ___52-[MSASDirectAssetDownloader _startDownloadForAsset:]_block_invoke
+ ___52-[MSASDirectAssetDownloader _startDownloadForAsset:]_block_invoke_2
+ ___53-[MSASDirectAssetDownloader shutDownCompletionBlock:]_block_invoke
+ ___53-[MSASDirectAssetDownloader shutDownCompletionBlock:]_block_invoke_2
+ ___53-[MSASDirectAssetDownloader shutDownCompletionBlock:]_block_invoke_3
+ ___53-[MSASStateMachine _deleteCommentDisposition:params:]_block_invoke.233
+ ___53-[MSASStateMachine _deleteCommentDisposition:params:]_block_invoke.234
+ ___53-[MSASStateMachine _deleteCommentDisposition:params:]_block_invoke.235
+ ___53-[MSASStateMachine _deleteCommentDisposition:params:]_block_invoke_2.236
+ ___53-[MSAlbumSharingDaemon boundStateMachineForPersonID:]_block_invoke.369
+ ___55-[MSASStateMachine _checkForChangesDisposition:params:]_block_invoke.134
+ ___55-[MSASStateMachine _checkForChangesDisposition:params:]_block_invoke_2.135
+ ___56-[MSASStateMachine _subscribeToAlbumDisposition:params:]_block_invoke.162
+ ___56-[MSASStateMachine _subscribeToAlbumDisposition:params:]_block_invoke.163
+ ___56-[MSASStateMachine _subscribeToAlbumDisposition:params:]_block_invoke_2.164
+ ___56-[MSAlbumSharingDaemon forgetEverythingCompletionBlock:]_block_invoke.274
+ ___56-[MSAlbumSharingDaemon forgetEverythingCompletionBlock:]_block_invoke.275
+ ___57-[MSASStateMachine _getAccessControlsDisposition:params:]_block_invoke.156
+ ___57-[MSASStateMachine _getAccessControlsDisposition:params:]_block_invoke.157
+ ___57-[MSASStateMachine _getAccessControlsDisposition:params:]_block_invoke.158
+ ___57-[MSASStateMachine _getAccessControlsDisposition:params:]_block_invoke_2.159
+ ___58-[MSASStateMachine _sendUploadCompleteDisposition:params:]_block_invoke.260
+ ___58-[MSASStateMachine _sendUploadCompleteDisposition:params:]_block_invoke.262
+ ___58-[MSASStateMachine _sendUploadCompleteDisposition:params:]_block_invoke_2.261
+ ___58-[MSASStateMachine _sendUploadCompleteDisposition:params:]_block_invoke_2.263
+ ___59-[MSASStateMachine _sendGetUploadTokensDisposition:params:]_block_invoke.273
+ ___59-[MSASStateMachine _sendGetUploadTokensDisposition:params:]_block_invoke.275
+ ___59-[MSASStateMachine _sendGetUploadTokensDisposition:params:]_block_invoke_2.274
+ ___59-[MSASStateMachine _sendGetUploadTokensDisposition:params:]_block_invoke_2.276
+ ___59-[MSASStateMachine _sendGetUploadTokensDisposition:params:]_block_invoke_3.277
+ ___59-[MSASStateMachine _setAlbumSyncedStateDisposition:params:]_block_invoke.208
+ ___59-[MSASStateMachine _setAlbumSyncedStateDisposition:params:]_block_invoke.209
+ ___59-[MSASStateMachine _setAlbumSyncedStateDisposition:params:]_block_invoke.211
+ ___59-[MSASStateMachine _setAlbumSyncedStateDisposition:params:]_block_invoke_2.210
+ ___59-[MSASStateMachine _setAlbumSyncedStateDisposition:params:]_block_invoke_2.215
+ ___60-[MSASStateMachine MSBackoffManagerDidUpdateNextExpiryDate:]_block_invoke.77
+ ___60-[MSASStateMachine _unsubscribeFromAlbumDisposition:params:]_block_invoke.168
+ ___60-[MSASStateMachine _unsubscribeFromAlbumDisposition:params:]_block_invoke.169
+ ___60-[MSASStateMachine _unsubscribeFromAlbumDisposition:params:]_block_invoke_2.170
+ ___62-[MSASStateMachine _checkForCommentChangesDisposition:params:]_block_invoke.194
+ ___62-[MSASStateMachine _checkForCommentChangesDisposition:params:]_block_invoke.195
+ ___62-[MSASStateMachine _checkForCommentChangesDisposition:params:]_block_invoke.196
+ ___62-[MSASStateMachine _checkForCommentChangesDisposition:params:]_block_invoke_2.197
+ ___62-[MSASStateMachine _deleteAssetCollectionsDisposition:params:]_block_invoke.228
+ ___62-[MSASStateMachine _deleteAssetCollectionsDisposition:params:]_block_invoke.229
+ ___62-[MSASStateMachine _deleteAssetCollectionsDisposition:params:]_block_invoke_2.230
+ ___63-[MSASStateMachine _sendPutAssetCollectionsDisposition:params:]_block_invoke.265
+ ___63-[MSASStateMachine _sendPutAssetCollectionsDisposition:params:]_block_invoke.267
+ ___63-[MSASStateMachine _sendPutAssetCollectionsDisposition:params:]_block_invoke_2.266
+ ___63-[MSASStateMachine _sendPutAssetCollectionsDisposition:params:]_block_invoke_2.268
+ ___63-[MSASStateMachine _sendPutAssetCollectionsDisposition:params:]_block_invoke_3.269
+ ___63-[MSASStateMachine validateInvitationForAlbum:completionBlock:]_block_invoke.180
+ ___64-[MSASStateMachine _checkForAlbumSyncedStateDisposition:params:]_block_invoke.202
+ ___64-[MSASStateMachine _checkForAlbumSyncedStateDisposition:params:]_block_invoke_2.203
+ ___64-[MSASStateMachine _checkForAlbumSyncedStateDisposition:params:]_block_invoke_3.205
+ ___65+[MSASServerSideModelGroupedCommandQueue calloutBlockForCommand:]_block_invoke.125
+ ___66-[MSASStateMachine _removeSharingRelationshipsDisposition:params:]_block_invoke.284
+ ___66-[MSASStateMachine _removeSharingRelationshipsDisposition:params:]_block_invoke.285
+ ___66-[MSASStateMachine _removeSharingRelationshipsDisposition:params:]_block_invoke_2.286
+ ___66-[MSASStateMachine checkForChangesResetSync:info:completionBlock:]_block_invoke
+ ___66-[MSASStateMachine checkForChangesResetSync:info:completionBlock:]_block_invoke.120
+ ___66-[MSASStateMachine checkForChangesResetSync:info:completionBlock:]_block_invoke.121
+ ___66-[MSASStateMachine checkForChangesResetSync:info:completionBlock:]_block_invoke.130
+ ___66-[MSASStateMachine checkForChangesResetSync:info:completionBlock:]_block_invoke_2
+ ___67-[MSASStateMachine acceptInvitationWithToken:info:completionBlock:]_block_invoke.179
+ ___68-[MSASStateMachine _markAsSpamInvitationForAlbumDisposition:params:]_block_invoke.173
+ ___68-[MSASStateMachine _markAsSpamInvitationForAlbumDisposition:params:]_block_invoke.174
+ ___68-[MSASStateMachine _markAsSpamInvitationForTokenDisposition:params:]_block_invoke.177
+ ___68-[MSASStateMachine _markAsSpamInvitationForTokenDisposition:params:]_block_invoke.178
+ ___69-[MSASStateMachine _setAssetCollectionSyncedStateDisposition:params:]_block_invoke.218
+ ___69-[MSASStateMachine _setAssetCollectionSyncedStateDisposition:params:]_block_invoke.219
+ ___69-[MSASStateMachine _setAssetCollectionSyncedStateDisposition:params:]_block_invoke_2.220
+ ___70-[MSASStateMachine _checkForAssetCollectionUpdatesDisposition:params:]_block_invoke.184
+ ___70-[MSASStateMachine _checkForAssetCollectionUpdatesDisposition:params:]_block_invoke.185
+ ___70-[MSASStateMachine _checkForAssetCollectionUpdatesDisposition:params:]_block_invoke.186
+ ___70-[MSASStateMachine _checkForAssetCollectionUpdatesDisposition:params:]_block_invoke_2.191
+ ___70-[MSASStateMachine _continueAddingAssetCollectionsDisposition:params:]_block_invoke.259
+ ___70-[MSASStateMachine _sendGetServerSideConfigurationDisposition:params:]_block_invoke.71
+ ___70-[MSASStateMachine _sendGetServerSideConfigurationDisposition:params:]_block_invoke.73
+ ___70-[MSASStateMachine _sendGetServerSideConfigurationDisposition:params:]_block_invoke_2.72
+ ___70-[MSASStateMachine _sendGetServerSideConfigurationDisposition:params:]_block_invoke_2.74
+ ___71-[MSASStateMachine videoURLForAssetCollection:inAlbum:completionBlock:]_block_invoke.304
+ ___71-[MSASStateMachine videoURLForAssetCollection:inAlbum:completionBlock:]_block_invoke.305
+ ___71-[MSAlbumSharingDaemon refreshResetSync:personID:info:completionBlock:]_block_invoke
+ ___72-[MSASStateMachine _sendReauthorizeAssetsForDownloadDisposition:params:]_block_invoke.327
+ ___72-[MSASStateMachine _sendReauthorizeAssetsForDownloadDisposition:params:]_block_invoke.328
+ ___72-[MSASStateMachine _sendReauthorizeAssetsForDownloadDisposition:params:]_block_invoke.330
+ ___72-[MSASStateMachine _sendReauthorizeAssetsForDownloadDisposition:params:]_block_invoke.331
+ ___72-[MSASStateMachine _sendReauthorizeAssetsForDownloadDisposition:params:]_block_invoke_2.329
+ ___73-[MSASDirectAssetDownloader MMCSEngine:didFinishGettingAsset:path:error:]_block_invoke
+ ___73-[MSASStateMachine cancelMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke
+ ___73-[MSASStateMachine cancelMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke.318
+ ___73-[MSASStateMachine cancelMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke_2
+ ___73-[MSASStateMachine setPublicAccessEnabled:forAlbum:info:completionBlock:]_block_invoke.302
+ ___74-[MSASDirectAssetDownloader _attemptReauthAndRetryForAsset:originalError:]_block_invoke
+ ___74-[MSASDirectAssetDownloader _attemptReauthAndRetryForAsset:originalError:]_block_invoke_2
+ ___75-[MSASStateMachine completeMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke
+ ___75-[MSASStateMachine completeMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke.317
+ ___75-[MSASStateMachine completeMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke_2
+ ___75-[MSASStateMachine getAccessControlsForAlbumWithGUID:info:completionBlock:]_block_invoke
+ ___75-[MSASStateMachine getAccessControlsForAlbumWithGUID:info:completionBlock:]_block_invoke.152
+ ___75-[MSASStateMachine getAccessControlsForAlbumWithGUID:info:completionBlock:]_block_invoke.153
+ ___75-[MSASStateMachine getAccessControlsForAlbumWithGUID:info:completionBlock:]_block_invoke.154
+ ___75-[MSASStateMachine getAccessControlsForAlbumWithGUID:info:completionBlock:]_block_invoke_2
+ ___76-[MSASServerSideModel cancelMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke
+ ___76-[MSASServerSideModel cancelMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke_2
+ ___76-[MSASStateMachine unarchiveMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke
+ ___76-[MSASStateMachine unarchiveMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke.320
+ ___76-[MSASStateMachine unarchiveMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke_2
+ ___76-[MSAlbumSharingDaemon shutDownStateMachine:forDestruction:completionBlock:]_block_invoke.272
+ ___76-[MSAlbumSharingDaemon shutDownStateMachine:forDestruction:completionBlock:]_block_invoke.273
+ ___78-[MSASServerSideModel completeMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke
+ ___78-[MSASServerSideModel completeMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke_2
+ ___78-[MSASStateMachine addSharingRelationships:toOwnedAlbum:info:completionBlock:]_block_invoke.278
+ ___78-[MSASStateMachine addSharingRelationships:toOwnedAlbum:info:completionBlock:]_block_invoke.279
+ ___78-[MSASStateMachine addSharingRelationships:toOwnedAlbum:info:completionBlock:]_block_invoke.280
+ ___78-[MSASStateMachine addSharingRelationships:toOwnedAlbum:info:completionBlock:]_block_invoke_2.281
+ ___79-[MSASServerSideModel setSharedCollectionMigrationState:forAlbumWithGUID:info:]_block_invoke
+ ___79-[MSASServerSideModel unarchiveMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke
+ ___79-[MSASServerSideModel unarchiveMigrationToCPLForAlbumWithGUID:completionBlock:]_block_invoke_2
+ ___81-[MSASStateMachine setMultipleContributorsEnabled:forAlbum:info:completionBlock:]_block_invoke.303
+ ___85+[MSProtocolUtilities cancelMigrationToCPLForAlbumWithGUID:personID:completionBlock:]_block_invoke
+ ___86-[MSASStateMachine failMigrationToCPLForAlbumWithGUID:migrationError:completionBlock:]_block_invoke
+ ___86-[MSASStateMachine failMigrationToCPLForAlbumWithGUID:migrationError:completionBlock:]_block_invoke.319
+ ___86-[MSASStateMachine failMigrationToCPLForAlbumWithGUID:migrationError:completionBlock:]_block_invoke_2
+ ___86-[MSAlbumSharingDaemon cancelMigrationToCPLForAlbumWithGUID:personID:completionBlock:]_block_invoke
+ ___88+[MSProtocolUtilities unarchiveMigrationToCPLForAlbumWithGUID:personID:completionBlock:]_block_invoke
+ ___88-[MSAlbumSharingDaemon completeMigrationToCPLForAlbumWithGUID:personID:completionBlock:]_block_invoke
+ ___89-[MSASDirectAssetDownloader downloadAsset:protocol:album:albumURLString:completionBlock:]_block_invoke
+ ___89-[MSASServerSideModel failMigrationToCPLForAlbumWithGUID:migrationError:completionBlock:]_block_invoke
+ ___89-[MSASServerSideModel failMigrationToCPLForAlbumWithGUID:migrationError:completionBlock:]_block_invoke_2
+ ___89-[MSAlbumSharingDaemon setSharedCollectionMigrationState:forAlbumWithGUID:personID:info:]_block_invoke
+ ___89-[MSAlbumSharingDaemon unarchiveMigrationToCPLForAlbumWithGUID:personID:completionBlock:]_block_invoke
+ ___90-[MSASProtocol updateAlbum:albumURLString:sharedCollectionMigrationState:completionBlock:]_block_invoke
+ ___90-[MSASStateMachine videoURLsForAssetCollection:forMediaAssetType:inAlbum:completionBlock:]_block_invoke.310
+ ___90-[MSASStateMachine videoURLsForAssetCollection:forMediaAssetType:inAlbum:completionBlock:]_block_invoke.311
+ ___90-[MSASStateMachine videoURLsForAssetCollection:forMediaAssetType:inAlbum:completionBlock:]_block_invoke.312
+ ___90-[MSASStateMachine videoURLsForAssetCollection:forMediaAssetType:inAlbum:completionBlock:]_block_invoke.313
+ ___90-[MSASStateMachine videoURLsForAssetCollection:forMediaAssetType:inAlbum:completionBlock:]_block_invoke.314
+ ___91-[MSASProtocol _sendOneURLRequest:checkServerSideConfigVersion:retryCount:completionBlock:]_block_invoke.210
+ ___91-[MSASProtocol _sendOneURLRequest:checkServerSideConfigVersion:retryCount:completionBlock:]_block_invoke.220
+ ___91-[MSASProtocol sendURLRequest:method:bodyObj:checkServerSideConfigVersion:completionBlock:]_block_invoke.202
+ ___91-[MSASProtocol sendURLRequest:method:bodyObj:checkServerSideConfigVersion:completionBlock:]_block_invoke.204
+ ___93-[MSASStateMachine initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:completionBlock:]_block_invoke
+ ___93-[MSASStateMachine initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:completionBlock:]_block_invoke.316
+ ___93-[MSASStateMachine initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:completionBlock:]_block_invoke_2
+ ___94-[MSASServerSideModel markCommentsForAssetCollectionWithGUID:asViewedWithLastViewedDate:info:]_block_invoke.306
+ ___94-[MSASStateMachine workQueueEndCommandWithError:command:params:albumGUID:assetCollectionGUID:]_block_invoke.91
+ ___94-[MSAlbumSharingDaemon refreshAccessControlListOfAlbumWithGUID:personID:info:completionBlock:]_block_invoke
+ ___95-[MSAlbumSharingDaemon retrieveAsset:inAlbumWithGUID:personID:destinationPath:completionBlock:]_block_invoke
+ ___95-[MSAlbumSharingDaemon retrieveAsset:inAlbumWithGUID:personID:destinationPath:completionBlock:]_block_invoke.267
+ ___95-[MSAlbumSharingDaemon retrieveAsset:inAlbumWithGUID:personID:destinationPath:completionBlock:]_block_invoke_2
+ ___95-[MSAlbumSharingDaemon retrieveAsset:inAlbumWithGUID:personID:destinationPath:completionBlock:]_block_invoke_2.268
+ ___96-[MSASServerSideModel initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:completionBlock:]_block_invoke
+ ___96-[MSASServerSideModel initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:completionBlock:]_block_invoke_2
+ ___96-[MSASServerSideModel initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:completionBlock:]_block_invoke_3
+ ___98+[MSProtocolUtilities failMigrationToCPLForAlbumWithGUID:migrationError:personID:completionBlock:]_block_invoke
+ ___98-[MSASProtocol getCommentChanges:inAlbumWithGUID:withClientOrgKey:albumURLString:completionBlock:]_block_invoke.598
+ ___99-[MSAlbumSharingDaemon failMigrationToCPLForAlbumWithGUID:migrationError:personID:completionBlock:]_block_invoke
+ ___Block_byref_object_copy_.2429
+ ___Block_byref_object_copy_.4413
+ ___Block_byref_object_copy_.5423
+ ___Block_byref_object_copy_.5744
+ ___Block_byref_object_copy_.6143
+ ___Block_byref_object_copy_.6295
+ ___Block_byref_object_copy_.6546
+ ___Block_byref_object_copy_.6698
+ ___Block_byref_object_copy_.7898
+ ___Block_byref_object_copy_.8036
+ ___Block_byref_object_copy_.8732
+ ___Block_byref_object_dispose_.2430
+ ___Block_byref_object_dispose_.4414
+ ___Block_byref_object_dispose_.5424
+ ___Block_byref_object_dispose_.5745
+ ___Block_byref_object_dispose_.6144
+ ___Block_byref_object_dispose_.6296
+ ___Block_byref_object_dispose_.6547
+ ___Block_byref_object_dispose_.6699
+ ___Block_byref_object_dispose_.7899
+ ___Block_byref_object_dispose_.8037
+ ___Block_byref_object_dispose_.8733
+ ___block_descriptor_106_e8_32s40s48s56s64s72s80s88bs96w_e5_v8?0ls32l8s40l8s48l8w96l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_40_e8_32s_e40_v32?0"PersonIdToCKUserIdEntry"8Q16^B24ls32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e47_v32?0"NSError"8"NSDictionary"16"NSString"24ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e47_v32?0"NSError"8"NSDictionary"16"NSString"24ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e46_v32?0"NSError"8"NSArray"16"NSDictionary"24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e29_v24?0"NSError"8"NSArray"16lw56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48bs56w_e5_v8?0ls32l8w56l8s48l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e30_v24?0"NSString"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls56l8s32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48bs56w_e69_v52?0"NSError"8B16"NSString"20"NSArray"28"NSArray"36"NSArray"44lw56l8s32l8s40l8s48l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s72l8s48l8s56l8s64l8
+ ___block_literal_global.104
+ ___block_literal_global.106
+ ___block_literal_global.109
+ ___block_literal_global.110
+ ___block_literal_global.114
+ ___block_literal_global.114.9315
+ ___block_literal_global.118
+ ___block_literal_global.122
+ ___block_literal_global.127
+ ___block_literal_global.140
+ ___block_literal_global.145
+ ___block_literal_global.153
+ ___block_literal_global.159
+ ___block_literal_global.164
+ ___block_literal_global.169
+ ___block_literal_global.17.6701
+ ___block_literal_global.174
+ ___block_literal_global.181
+ ___block_literal_global.186
+ ___block_literal_global.191
+ ___block_literal_global.2597
+ ___block_literal_global.27.7161
+ ___block_literal_global.32.7156
+ ___block_literal_global.37.7149
+ ___block_literal_global.531
+ ___block_literal_global.5531
+ ___block_literal_global.5752
+ ___block_literal_global.579
+ ___block_literal_global.6173
+ ___block_literal_global.6708
+ ___block_literal_global.6839
+ ___block_literal_global.6967
+ ___block_literal_global.7166
+ ___block_literal_global.728
+ ___block_literal_global.7433
+ ___block_literal_global.7690
+ ___block_literal_global.809
+ ___block_literal_global.8297
+ ___block_literal_global.84
+ ___block_literal_global.846
+ ___block_literal_global.90
+ ___block_literal_global.9079
+ ___block_literal_global.9311
+ ___block_literal_global.94
+ ___masterManifest.1390
+ ___masterManifest.268
+ __canceledError.error.7150
+ __canceledError.onceToken.7148
+ __commitMasterManifest.267
+ __commitMasterManifest.3746
+ __createBadFieldError.3910
+ __didFailAuthentication.1802
+ __didFailAuthentication.2742
+ __didFailAuthentication.2755
+ __didFailAuthentication.2975
+ __didFailAuthentication.3163
+ __didFailAuthentication.3903
+ __didFinish.1803
+ __didFinish.2743
+ __didFinish.2756
+ __didFinish.2976
+ __didFinish.3164
+ __didFinish.3904
+ __didReceiveRetryAfter.1801
+ __didReceiveRetryAfter.3162
+ __didReceiveRetryAfter.3902
+ __didReceiveServerSideConfigurationVersion.1761
+ __didReceiveServerSideConfigurationVersion.1800
+ __didReceiveServerSideConfigurationVersion.2974
+ __didReceiveServerSideConfigurationVersion.3161
+ __didReceiveServerSideConfigurationVersion.3901
+ __getItemDoneCallback.6635
+ __getItemProgressCallback.6636
+ __masterNextActivityDateByPersonID.295
+ __masterNextActivityDateByPersonID.3771
+ __nonNumericNonSpaceCharacterSet.charSet.7435
+ __pointerComparisonCallback.6345
+ __protocolDidFailAuthentication.3055
+ __protocolDidFailAuthentication.3201
+ __protocolDidFailAuthentication.3857
+ __protocolDidFinish.3056
+ __protocolDidFinish.3202
+ __protocolDidFinish.3858
+ __protocolDidReceiveRetryAfterDate.1245
+ __protocolDidReceiveRetryAfterDate.3200
+ __protocolDidReceiveRetryAfterDate.3856
+ __protocolDidReceiveServerSideConfigurationVersion.3054
+ __protocolDidReceiveServerSideConfigurationVersion.3199
+ __protocolDidReceiveServerSideConfigurationVersion.3855
+ __putItemDoneCallback.6633
+ __putItemProgressCallback.6634
+ __requestCompletedCallback.6632
+ __retryAfterDateFormatter.df.7437
+ __retryAfterDateFormatter.once.7436
+ _kMSASDestinationPathKey
+ _kMSASDownloadedFilePathKey
+ _kMSASIsSilentMigrationKey
+ _kMSASMigrationErrorKey
+ _kMSASModelCancelMigrationToCPLFn
+ _kMSASModelCompleteMigrationToCPLFn
+ _kMSASModelFailMigrationToCPLFn
+ _kMSASModelInitiateMigrationToCPLFn
+ _kMSASModelRefreshAccessControlListOfAlbumWithGUIDWithCompletionFn
+ _kMSASModelRefreshWithCompletionFn
+ _kMSASModelRetrieveAssetInAlbumWithGUIDWithCompletionFn
+ _kMSASModelSetSCMigrationStateForAlbumWithGUIDFn
+ _kMSASModelUnarchiveMigrationToCPLFn
+ _kMSASPersonIdToCKUserIdDictKey
+ _kMSASSCMigrationStateKey
+ _kMSASScZoneIdentifierKey
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_attemptReauthAndRetryForAsset:originalError:
+ _objc_msgSend$_errorForSCMigrationStatusCode:
+ _objc_msgSend$_finishWithPath:error:
+ _objc_msgSend$_startDownloadForAsset:
+ _objc_msgSend$addPersonIdToCKUserId:
+ _objc_msgSend$cancelMigrationToCPLForAlbumWithGUID:completionBlock:
+ _objc_msgSend$cancelMigrationToCPLForAlbumWithGUID:personID:completionBlock:
+ _objc_msgSend$checkForChangesResetSync:info:completionBlock:
+ _objc_msgSend$cleanUpWorkingDirectory
+ _objc_msgSend$clearPersonIdToCKUserIds
+ _objc_msgSend$completeMigrationToCPLForAlbumWithGUID:clientOrgKey:personID:completionBlock:
+ _objc_msgSend$completeMigrationToCPLForAlbumWithGUID:completionBlock:
+ _objc_msgSend$descriptionForSCMigrationState:
+ _objc_msgSend$downloadAsset:protocol:album:albumURLString:completionBlock:
+ _objc_msgSend$failMigrationToCPLForAlbumWithGUID:migrationError:completionBlock:
+ _objc_msgSend$failMigrationToCPLForAlbumWithGUID:migrationError:personID:completionBlock:
+ _objc_msgSend$getAccessControlsForAlbumWithGUID:info:completionBlock:
+ _objc_msgSend$initiateMigrationToCPLForAlbumWithGUID:isSilentMigration:completionBlock:
+ _objc_msgSend$initiateMigrationToCPLForAlbumWithGUID:sharedAlbumTitle:personID:isSilentMigration:completionBlock:
+ _objc_msgSend$key
+ _objc_msgSend$personIdToCKUserIdAtIndex:
+ _objc_msgSend$personIdToCKUserIds
+ _objc_msgSend$personIdToCKUserIdsCount
+ _objc_msgSend$refreshAccessControlListForAlbumWithGUID:info:completionBlock:
+ _objc_msgSend$refreshResetSync:info:completionBlock:
+ _objc_msgSend$scZoneIdentifier
+ _objc_msgSend$setArchiveKeyword:
+ _objc_msgSend$setArchiveTitle:
+ _objc_msgSend$setErrorCode:
+ _objc_msgSend$setErrorDomain:
+ _objc_msgSend$setIsSilentMigration:
+ _objc_msgSend$setKey:
+ _objc_msgSend$setSaAlbumGuid:
+ _objc_msgSend$setScZoneIdentifier:
+ _objc_msgSend$setSharedCollectionMigrationExpungeDate:
+ _objc_msgSend$setSharedCollectionMigrationState:
+ _objc_msgSend$setSharedCollectionMigrationState:forAlbumWithGUID:info:
+ _objc_msgSend$setSharedCollectionZoneIdentifier:
+ _objc_msgSend$setValue:
+ _objc_msgSend$sharedCollectionMigrationExpungeDate
+ _objc_msgSend$sharedCollectionMigrationState
+ _objc_msgSend$sharedCollectionZoneIdentifier
+ _objc_msgSend$status
+ _objc_msgSend$stringValue
+ _objc_msgSend$unarchiveMigrationToCPLForAlbumWithGUID:completionBlock:
+ _objc_msgSend$unarchiveMigrationToCPLForAlbumWithGUID:personID:completionBlock:
+ _objc_msgSend$updateAlbum:albumURLString:sharedCollectionMigrationState:completionBlock:
+ _objc_msgSend$value
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x9
- -[MSASAlbum setUpdatedSharedAlbumURL:]
- -[MSASAlbum updatedSharedAlbumURL]
- -[MSASProtocol updateAlbum:albumURLString:completionBlock:]
- GCC_except_table1003
- GCC_except_table1043
- GCC_except_table1048
- GCC_except_table1055
- GCC_except_table1058
- GCC_except_table1068
- GCC_except_table1187
- GCC_except_table1194
- GCC_except_table1200
- GCC_except_table1332
- GCC_except_table1336
- GCC_except_table1355
- GCC_except_table1356
- GCC_except_table1357
- GCC_except_table1362
- GCC_except_table1366
- GCC_except_table1370
- GCC_except_table1377
- GCC_except_table1387
- GCC_except_table1390
- GCC_except_table1397
- GCC_except_table1399
- GCC_except_table1403
- GCC_except_table1406
- GCC_except_table1412
- GCC_except_table1415
- GCC_except_table1421
- GCC_except_table1425
- GCC_except_table1428
- GCC_except_table1446
- GCC_except_table1449
- GCC_except_table1455
- GCC_except_table1458
- GCC_except_table1464
- GCC_except_table1468
- GCC_except_table1473
- GCC_except_table1476
- GCC_except_table1482
- GCC_except_table1485
- GCC_except_table1491
- GCC_except_table1502
- GCC_except_table1512
- GCC_except_table1515
- GCC_except_table1522
- GCC_except_table1526
- GCC_except_table1529
- GCC_except_table1533
- GCC_except_table1538
- GCC_except_table1551
- GCC_except_table1552
- GCC_except_table1559
- GCC_except_table1560
- GCC_except_table1567
- GCC_except_table1570
- GCC_except_table1576
- GCC_except_table1579
- GCC_except_table1585
- GCC_except_table1589
- GCC_except_table1602
- GCC_except_table1609
- GCC_except_table1612
- GCC_except_table1659
- GCC_except_table1672
- GCC_except_table1677
- GCC_except_table1679
- GCC_except_table1698
- GCC_except_table1735
- GCC_except_table1745
- GCC_except_table1758
- GCC_except_table1765
- GCC_except_table1784
- GCC_except_table1789
- GCC_except_table1794
- GCC_except_table1804
- GCC_except_table1806
- GCC_except_table1809
- GCC_except_table1813
- GCC_except_table1832
- GCC_except_table1848
- GCC_except_table1869
- GCC_except_table1873
- GCC_except_table1907
- GCC_except_table1913
- GCC_except_table1915
- GCC_except_table1922
- GCC_except_table1990
- GCC_except_table2023
- GCC_except_table2028
- GCC_except_table2030
- GCC_except_table2032
- GCC_except_table2034
- GCC_except_table2255
- GCC_except_table2295
- GCC_except_table2296
- GCC_except_table2297
- GCC_except_table2299
- GCC_except_table2301
- GCC_except_table2303
- GCC_except_table2304
- GCC_except_table2307
- GCC_except_table2309
- GCC_except_table2339
- GCC_except_table2340
- GCC_except_table2341
- GCC_except_table2342
- GCC_except_table2343
- GCC_except_table2345
- GCC_except_table2346
- GCC_except_table2347
- GCC_except_table2360
- GCC_except_table2429
- GCC_except_table2452
- GCC_except_table2454
- GCC_except_table2458
- GCC_except_table2460
- GCC_except_table2462
- GCC_except_table2551
- GCC_except_table2553
- GCC_except_table2563
- GCC_except_table2565
- GCC_except_table2568
- GCC_except_table2570
- GCC_except_table2698
- GCC_except_table2706
- GCC_except_table2719
- GCC_except_table2784
- GCC_except_table2787
- GCC_except_table2803
- GCC_except_table2807
- GCC_except_table2811
- GCC_except_table2815
- GCC_except_table2819
- GCC_except_table2823
- GCC_except_table2825
- GCC_except_table2829
- GCC_except_table2831
- GCC_except_table2835
- GCC_except_table2837
- GCC_except_table2847
- GCC_except_table2852
- GCC_except_table2855
- GCC_except_table2858
- GCC_except_table2866
- GCC_except_table2868
- GCC_except_table2872
- GCC_except_table2874
- GCC_except_table2910
- GCC_except_table2912
- GCC_except_table2946
- GCC_except_table2949
- GCC_except_table2951
- GCC_except_table2954
- GCC_except_table2957
- GCC_except_table3033
- GCC_except_table3056
- GCC_except_table3062
- GCC_except_table3071
- GCC_except_table3109
- GCC_except_table3114
- GCC_except_table3247
- GCC_except_table3259
- GCC_except_table3267
- GCC_except_table401
- GCC_except_table629
- GCC_except_table633
- GCC_except_table734
- GCC_except_table735
- GCC_except_table736
- GCC_except_table737
- GCC_except_table738
- GCC_except_table739
- GCC_except_table827
- GCC_except_table944
- GCC_except_table945
- GCC_except_table948
- GCC_except_table949
- GCC_except_table950
- GCC_except_table951
- GCC_except_table952
- GCC_except_table953
- GCC_except_table954
- GCC_except_table955
- GCC_except_table956
- GCC_except_table993
- GCC_except_table994
- GCC_except_table997
- _OBJC_IVAR_$_MSASAlbum._updatedSharedAlbumURL
- __OBJC_$_PROP_LIST_MSDeleter.131
- __OBJC_$_PROP_LIST_MSPublisher.296
- __OBJC_$_PROP_LIST_MSSubscriber.259
- ___44-[MSASStateMachine shutDownCompletionBlock:]_block_invoke.53
- ___44-[MSASStateMachine shutDownCompletionBlock:]_block_invoke.55
- ___44-[MSASStateMachine shutDownCompletionBlock:]_block_invoke_2.54
- ___44-[MSASStateMachine shutDownCompletionBlock:]_block_invoke_2.56
- ___47-[MSASStateMachine workQueuePerformNextCommand]_block_invoke.85
- ___47-[MSASStateMachine workQueuePerformNextCommand]_block_invoke.86
- ___47-[MSASStateMachine workQueuePerformNextCommand]_block_invoke_2.87
- ___48-[MSASStateMachine initWithPersonID:eventQueue:]_block_invoke.44
- ___48-[MSASStateMachine initWithPersonID:eventQueue:]_block_invoke_2.45
- ___48-[MSASStateMachine workQueueCheckForNextCommand]_block_invoke.81
- ___50-[MSASStateMachine _addCommentDisposition:params:]_block_invoke.283
- ___50-[MSASStateMachine _addCommentDisposition:params:]_block_invoke.284
- ___50-[MSASStateMachine _addCommentDisposition:params:]_block_invoke.285
- ___50-[MSASStateMachine _addCommentDisposition:params:]_block_invoke_2.286
- ___51-[MSASStateMachine _createAlbumDisposition:params:]_block_invoke.233
- ___51-[MSASStateMachine _createAlbumDisposition:params:]_block_invoke.234
- ___51-[MSASStateMachine _createAlbumDisposition:params:]_block_invoke_2.235
- ___51-[MSASStateMachine _deleteAlbumDisposition:params:]_block_invoke.217
- ___51-[MSASStateMachine _deleteAlbumDisposition:params:]_block_invoke.218
- ___51-[MSASStateMachine _deleteAlbumDisposition:params:]_block_invoke_2.219
- ___51-[MSASStateMachine _updateAlbumDisposition:params:]_block_invoke.239
- ___51-[MSASStateMachine _updateAlbumDisposition:params:]_block_invoke.240
- ___51-[MSASStateMachine _updateAlbumDisposition:params:]_block_invoke_2.241
- ___53-[MSASStateMachine _deleteCommentDisposition:params:]_block_invoke.227
- ___53-[MSASStateMachine _deleteCommentDisposition:params:]_block_invoke.228
- ___53-[MSASStateMachine _deleteCommentDisposition:params:]_block_invoke.229
- ___53-[MSASStateMachine _deleteCommentDisposition:params:]_block_invoke_2.230
- ___53-[MSAlbumSharingDaemon boundStateMachineForPersonID:]_block_invoke.351
- ___55-[MSASStateMachine _checkForChangesDisposition:params:]_block_invoke.123
- ___55-[MSASStateMachine _checkForChangesDisposition:params:]_block_invoke_2.134
- ___56-[MSASStateMachine _subscribeToAlbumDisposition:params:]_block_invoke.156
- ___56-[MSASStateMachine _subscribeToAlbumDisposition:params:]_block_invoke.157
- ___56-[MSASStateMachine _subscribeToAlbumDisposition:params:]_block_invoke_2.158
- ___56-[MSAlbumSharingDaemon forgetEverythingCompletionBlock:]_block_invoke.255
- ___56-[MSAlbumSharingDaemon forgetEverythingCompletionBlock:]_block_invoke.256
- ___57-[MSASStateMachine _getAccessControlsDisposition:params:]_block_invoke.149
- ___57-[MSASStateMachine _getAccessControlsDisposition:params:]_block_invoke.150
- ___57-[MSASStateMachine _getAccessControlsDisposition:params:]_block_invoke.151
- ___57-[MSASStateMachine _getAccessControlsDisposition:params:]_block_invoke_2.153
- ___58-[MSASStateMachine _sendUploadCompleteDisposition:params:]_block_invoke.254
- ___58-[MSASStateMachine _sendUploadCompleteDisposition:params:]_block_invoke.256
- ___58-[MSASStateMachine _sendUploadCompleteDisposition:params:]_block_invoke_2.255
- ___58-[MSASStateMachine _sendUploadCompleteDisposition:params:]_block_invoke_2.257
- ___59-[MSASProtocol updateAlbum:albumURLString:completionBlock:]_block_invoke
- ___59-[MSASStateMachine _sendGetUploadTokensDisposition:params:]_block_invoke.267
- ___59-[MSASStateMachine _sendGetUploadTokensDisposition:params:]_block_invoke.269
- ___59-[MSASStateMachine _sendGetUploadTokensDisposition:params:]_block_invoke_2.268
- ___59-[MSASStateMachine _sendGetUploadTokensDisposition:params:]_block_invoke_2.270
- ___59-[MSASStateMachine _sendGetUploadTokensDisposition:params:]_block_invoke_3.271
- ___59-[MSASStateMachine _setAlbumSyncedStateDisposition:params:]_block_invoke.202
- ___59-[MSASStateMachine _setAlbumSyncedStateDisposition:params:]_block_invoke.203
- ___59-[MSASStateMachine _setAlbumSyncedStateDisposition:params:]_block_invoke.205
- ___59-[MSASStateMachine _setAlbumSyncedStateDisposition:params:]_block_invoke_2.204
- ___59-[MSASStateMachine _setAlbumSyncedStateDisposition:params:]_block_invoke_2.209
- ___60-[MSASStateMachine MSBackoffManagerDidUpdateNextExpiryDate:]_block_invoke.80
- ___60-[MSASStateMachine _unsubscribeFromAlbumDisposition:params:]_block_invoke.162
- ___60-[MSASStateMachine _unsubscribeFromAlbumDisposition:params:]_block_invoke.163
- ___60-[MSASStateMachine _unsubscribeFromAlbumDisposition:params:]_block_invoke_2.164
- ___62-[MSASStateMachine _checkForCommentChangesDisposition:params:]_block_invoke.188
- ___62-[MSASStateMachine _checkForCommentChangesDisposition:params:]_block_invoke.189
- ___62-[MSASStateMachine _checkForCommentChangesDisposition:params:]_block_invoke.190
- ___62-[MSASStateMachine _checkForCommentChangesDisposition:params:]_block_invoke_2.191
- ___62-[MSASStateMachine _deleteAssetCollectionsDisposition:params:]_block_invoke.222
- ___62-[MSASStateMachine _deleteAssetCollectionsDisposition:params:]_block_invoke.223
- ___62-[MSASStateMachine _deleteAssetCollectionsDisposition:params:]_block_invoke_2.224
- ___63-[MSASStateMachine _sendPutAssetCollectionsDisposition:params:]_block_invoke.259
- ___63-[MSASStateMachine _sendPutAssetCollectionsDisposition:params:]_block_invoke.261
- ___63-[MSASStateMachine _sendPutAssetCollectionsDisposition:params:]_block_invoke_2.260
- ___63-[MSASStateMachine _sendPutAssetCollectionsDisposition:params:]_block_invoke_2.262
- ___63-[MSASStateMachine _sendPutAssetCollectionsDisposition:params:]_block_invoke_3.263
- ___63-[MSASStateMachine validateInvitationForAlbum:completionBlock:]_block_invoke.174
- ___64-[MSASStateMachine _checkForAlbumSyncedStateDisposition:params:]_block_invoke.196
- ___64-[MSASStateMachine _checkForAlbumSyncedStateDisposition:params:]_block_invoke_2.197
- ___64-[MSASStateMachine _checkForAlbumSyncedStateDisposition:params:]_block_invoke_3.199
- ___65+[MSASServerSideModelGroupedCommandQueue calloutBlockForCommand:]_block_invoke.126
- ___66-[MSASStateMachine _removeSharingRelationshipsDisposition:params:]_block_invoke.278
- ___66-[MSASStateMachine _removeSharingRelationshipsDisposition:params:]_block_invoke.279
- ___66-[MSASStateMachine _removeSharingRelationshipsDisposition:params:]_block_invoke_2.280
- ___67-[MSASStateMachine acceptInvitationWithToken:info:completionBlock:]_block_invoke.173
- ___68-[MSASStateMachine _markAsSpamInvitationForAlbumDisposition:params:]_block_invoke.167
- ___68-[MSASStateMachine _markAsSpamInvitationForAlbumDisposition:params:]_block_invoke.168
- ___68-[MSASStateMachine _markAsSpamInvitationForTokenDisposition:params:]_block_invoke.171
- ___68-[MSASStateMachine _markAsSpamInvitationForTokenDisposition:params:]_block_invoke.172
- ___69-[MSASStateMachine _setAssetCollectionSyncedStateDisposition:params:]_block_invoke.212
- ___69-[MSASStateMachine _setAssetCollectionSyncedStateDisposition:params:]_block_invoke.213
- ___69-[MSASStateMachine _setAssetCollectionSyncedStateDisposition:params:]_block_invoke_2.214
- ___70-[MSASStateMachine _checkForAssetCollectionUpdatesDisposition:params:]_block_invoke.178
- ___70-[MSASStateMachine _checkForAssetCollectionUpdatesDisposition:params:]_block_invoke.179
- ___70-[MSASStateMachine _checkForAssetCollectionUpdatesDisposition:params:]_block_invoke.180
- ___70-[MSASStateMachine _checkForAssetCollectionUpdatesDisposition:params:]_block_invoke_2.185
- ___70-[MSASStateMachine _continueAddingAssetCollectionsDisposition:params:]_block_invoke.253
- ___70-[MSASStateMachine _sendGetServerSideConfigurationDisposition:params:]_block_invoke.74
- ___70-[MSASStateMachine _sendGetServerSideConfigurationDisposition:params:]_block_invoke.76
- ___70-[MSASStateMachine _sendGetServerSideConfigurationDisposition:params:]_block_invoke_2.75
- ___70-[MSASStateMachine _sendGetServerSideConfigurationDisposition:params:]_block_invoke_2.77
- ___71-[MSASStateMachine videoURLForAssetCollection:inAlbum:completionBlock:]_block_invoke.298
- ___71-[MSASStateMachine videoURLForAssetCollection:inAlbum:completionBlock:]_block_invoke.299
- ___72-[MSASStateMachine _sendReauthorizeAssetsForDownloadDisposition:params:]_block_invoke.315
- ___72-[MSASStateMachine _sendReauthorizeAssetsForDownloadDisposition:params:]_block_invoke.316
- ___72-[MSASStateMachine _sendReauthorizeAssetsForDownloadDisposition:params:]_block_invoke.318
- ___72-[MSASStateMachine _sendReauthorizeAssetsForDownloadDisposition:params:]_block_invoke.319
- ___72-[MSASStateMachine _sendReauthorizeAssetsForDownloadDisposition:params:]_block_invoke_2.317
- ___73-[MSASStateMachine setPublicAccessEnabled:forAlbum:info:completionBlock:]_block_invoke.296
- ___76-[MSAlbumSharingDaemon shutDownStateMachine:forDestruction:completionBlock:]_block_invoke.253
- ___76-[MSAlbumSharingDaemon shutDownStateMachine:forDestruction:completionBlock:]_block_invoke.254
- ___78-[MSASStateMachine addSharingRelationships:toOwnedAlbum:info:completionBlock:]_block_invoke.272
- ___78-[MSASStateMachine addSharingRelationships:toOwnedAlbum:info:completionBlock:]_block_invoke.273
- ___78-[MSASStateMachine addSharingRelationships:toOwnedAlbum:info:completionBlock:]_block_invoke.274
- ___78-[MSASStateMachine addSharingRelationships:toOwnedAlbum:info:completionBlock:]_block_invoke_2.275
- ___81-[MSASStateMachine setMultipleContributorsEnabled:forAlbum:info:completionBlock:]_block_invoke.297
- ___90-[MSASStateMachine videoURLsForAssetCollection:forMediaAssetType:inAlbum:completionBlock:]_block_invoke.304
- ___90-[MSASStateMachine videoURLsForAssetCollection:forMediaAssetType:inAlbum:completionBlock:]_block_invoke.305
- ___90-[MSASStateMachine videoURLsForAssetCollection:forMediaAssetType:inAlbum:completionBlock:]_block_invoke.306
- ___90-[MSASStateMachine videoURLsForAssetCollection:forMediaAssetType:inAlbum:completionBlock:]_block_invoke.307
- ___90-[MSASStateMachine videoURLsForAssetCollection:forMediaAssetType:inAlbum:completionBlock:]_block_invoke.308
- ___91-[MSASProtocol _sendOneURLRequest:checkServerSideConfigVersion:retryCount:completionBlock:]_block_invoke.212
- ___91-[MSASProtocol _sendOneURLRequest:checkServerSideConfigVersion:retryCount:completionBlock:]_block_invoke.221
- ___91-[MSASProtocol sendURLRequest:method:bodyObj:checkServerSideConfigVersion:completionBlock:]_block_invoke.203
- ___91-[MSASProtocol sendURLRequest:method:bodyObj:checkServerSideConfigVersion:completionBlock:]_block_invoke.205
- ___94-[MSASServerSideModel markCommentsForAssetCollectionWithGUID:asViewedWithLastViewedDate:info:]_block_invoke.307
- ___94-[MSASStateMachine workQueueEndCommandWithError:command:params:albumGUID:assetCollectionGUID:]_block_invoke.94
- ___98-[MSASProtocol getCommentChanges:inAlbumWithGUID:withClientOrgKey:albumURLString:completionBlock:]_block_invoke.595
- ___Block_byref_object_copy_.2006
- ___Block_byref_object_copy_.3892
- ___Block_byref_object_copy_.4543
- ___Block_byref_object_copy_.4863
- ___Block_byref_object_copy_.5153
- ___Block_byref_object_copy_.5304
- ___Block_byref_object_copy_.5545
- ___Block_byref_object_copy_.5687
- ___Block_byref_object_copy_.6813
- ___Block_byref_object_copy_.6936
- ___Block_byref_object_copy_.7585
- ___Block_byref_object_dispose_.2007
- ___Block_byref_object_dispose_.3893
- ___Block_byref_object_dispose_.4544
- ___Block_byref_object_dispose_.4864
- ___Block_byref_object_dispose_.5154
- ___Block_byref_object_dispose_.5305
- ___Block_byref_object_dispose_.5546
- ___Block_byref_object_dispose_.5688
- ___Block_byref_object_dispose_.6814
- ___Block_byref_object_dispose_.6937
- ___Block_byref_object_dispose_.7586
- ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s40l8s48l8s56l8
- ___block_descriptor_80_e8_32s40s48s56s64s72bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8
- ___block_literal_global.103
- ___block_literal_global.107
- ___block_literal_global.107.8142
- ___block_literal_global.111
- ___block_literal_global.112
- ___block_literal_global.115
- ___block_literal_global.117
- ___block_literal_global.119
- ___block_literal_global.123
- ___block_literal_global.128
- ___block_literal_global.154
- ___block_literal_global.160
- ___block_literal_global.165
- ___block_literal_global.17.5690
- ___block_literal_global.170
- ___block_literal_global.175
- ___block_literal_global.182
- ___block_literal_global.187
- ___block_literal_global.193
- ___block_literal_global.2118
- ___block_literal_global.27.6175
- ___block_literal_global.32.6170
- ___block_literal_global.37.6163
- ___block_literal_global.4653
- ___block_literal_global.4878
- ___block_literal_global.5183
- ___block_literal_global.534
- ___block_literal_global.5697
- ___block_literal_global.576
- ___block_literal_global.5827
- ___block_literal_global.5954
- ___block_literal_global.6180
- ___block_literal_global.6353
- ___block_literal_global.6604
- ___block_literal_global.7159
- ___block_literal_global.726
- ___block_literal_global.7910
- ___block_literal_global.807
- ___block_literal_global.8138
- ___block_literal_global.844
- ___block_literal_global.85
- ___block_literal_global.91
- ___block_literal_global.93
- ___block_literal_global.95
- ___masterManifest.1119
- ___masterManifest.271
- __canceledError.error.6164
- __canceledError.onceToken.6162
- __commitMasterManifest.270
- __commitMasterManifest.3255
- __createBadFieldError.3419
- __didFailAuthentication.1520
- __didFailAuthentication.2255
- __didFailAuthentication.2268
- __didFailAuthentication.2489
- __didFailAuthentication.2675
- __didFailAuthentication.3412
- __didFinish.1521
- __didFinish.2256
- __didFinish.2269
- __didFinish.2490
- __didFinish.2676
- __didFinish.3413
- __didReceiveRetryAfter.1519
- __didReceiveRetryAfter.2674
- __didReceiveRetryAfter.3411
- __didReceiveServerSideConfigurationVersion.1479
- __didReceiveServerSideConfigurationVersion.1518
- __didReceiveServerSideConfigurationVersion.2488
- __didReceiveServerSideConfigurationVersion.2673
- __didReceiveServerSideConfigurationVersion.3410
- __getItemDoneCallback.5626
- __getItemProgressCallback.5627
- __masterNextActivityDateByPersonID.300
- __masterNextActivityDateByPersonID.3280
- __nonNumericNonSpaceCharacterSet.charSet.6355
- __os_feature_enabled_impl
- __pointerComparisonCallback.5354
- __protocolDidFailAuthentication.2566
- __protocolDidFailAuthentication.2712
- __protocolDidFailAuthentication.3366
- __protocolDidFinish.2567
- __protocolDidFinish.2713
- __protocolDidFinish.3367
- __protocolDidReceiveRetryAfterDate.2711
- __protocolDidReceiveRetryAfterDate.3365
- __protocolDidReceiveRetryAfterDate.988
- __protocolDidReceiveServerSideConfigurationVersion.2565
- __protocolDidReceiveServerSideConfigurationVersion.2710
- __protocolDidReceiveServerSideConfigurationVersion.3364
- __putItemDoneCallback.5624
- __putItemProgressCallback.5625
- __requestCompletedCallback.5623
- __retryAfterDateFormatter.df.6357
- __retryAfterDateFormatter.once.6356
- _objc_msgSend$setUpdatedSharedAlbumURL:
- _objc_msgSend$updateAlbum:albumURLString:completionBlock:
- _objc_msgSend$updatedSharedAlbumURL
CStrings:
+ " SC migration expunge date: %@"
+ " SC migration state: %@"
+ " SC zone identifier: %@"
+ "%{public}@: Canceling migration to CPL for album %{public}@"
+ "%{public}@: Checking for album list updates (with completion). Reset sync: %d"
+ "%{public}@: Completing migration to CPL for album %{public}@"
+ "%{public}@: Failed to check for changes (with completion). Error: %{public}@"
+ "%{public}@: Failed to retrieve access controls for album %{public}@ (with completion). Error: %{public}@"
+ "%{public}@: Failing migration to CPL for album %{public}@"
+ "%{public}@: Global reset sync found (with completion)."
+ "%{public}@: Initiating migration to CPL for album %{public}@"
+ "%{public}@: Retrieving access controls for album %{public}@ (with completion)"
+ "%{public}@: Successfully checked for changes updates (with completion)."
+ "%{public}@: Successfully retrieved %ld access control entries for album %{public}@ (with completion)"
+ "%{public}@: Unarchiving migration to CPL for album %{public}@"
+ "Asset has no MMCS access token and no protocol available for reauth"
+ "CancelSharedCollectionsMigrationResponse %{public}@"
+ "CompleteSharedCollectionsMigrationResponse %{public}@"
+ "FailSharedCollectionsMigrationResponse %{public}@"
+ "InitiateSharedCollectionsMigrationResponse %{public}@"
+ "MSASDirectAssetDownloader.workQueue"
+ "MSASDirectAssetDownloader: Failed to download asset. Error: %{public}@"
+ "MSASDirectAssetDownloader: MMCS auth error, attempting reauth for asset %{public}@."
+ "MSASDirectAssetDownloader: Reauth failed for asset %{public}@. Error: %{public}@"
+ "MSASDirectAssetDownloader: Reauth succeeded for asset %{public}@, retrying download."
+ "MSASDirectAssetDownloader: Successfully downloaded asset to %{public}@."
+ "MSAlbumSharingDaemon: Failed to copy downloaded asset from %{public}@ to %{public}@. Error: %{public}@"
+ "SCMigrationStatusCode %d in the response"
+ "SC_MIGRATION_ALREADY_MIGRATING"
+ "SC_MIGRATION_INCOMPLETE"
+ "SC_MIGRATION_MAID_RESTRICTED"
+ "SC_MIGRATION_NOT_MIGRATING"
+ "SC_MIGRATION_SHAREDCOLLECTION_NOT_FOUND"
+ "SC_MIGRATION_SUCCESS"
+ "SC_MIGRATION_U13_RESTRICTED"
+ "SC_MIGRATION_UNKNOWN"
+ "SC_MIGRATION_VALIDATION_FAILED"
+ "SHARED_ALBUM_ARCHIVED_TITLE_FORMAT"
+ "SHARED_ALBUM_ARCHIVE_KEYWORD"
+ "Server is throttled with status code %ld in the response"
+ "UnarchiveSharedCollectionsMigrationResponse %{public}@"
+ "archiveKeyword"
+ "archiveTitle"
+ "cancelMigrationToCPL"
+ "cancelled"
+ "completeMigrationToCPL"
+ "completed"
+ "destinationPath"
+ "downloadedFilePath"
+ "errorCode"
+ "errorDomain"
+ "failMigrationToCPL"
+ "failed"
+ "in-progress"
+ "initiateMigrationToCPL"
+ "isSilentMigration"
+ "key"
+ "migrationError"
+ "mmcs-migration"
+ "modelRefreshAccessControlListOfAlbumWithGUIDWithCompletion"
+ "modelRefreshWithCompletion"
+ "modelSetSCMigrationStateForAlbumWithGUID"
+ "personIdToCKUserId"
+ "personIdToCKUserIdDict"
+ "retrieveAssetInAlbumWithGUIDWithCompletion"
+ "saAlbumGuid"
+ "scMigrationState"
+ "scZoneIdentifier"
+ "sharedCollectionMigrationExpungeDate"
+ "sharedCollectionMigrationState"
+ "sharedCollectionZoneIdentifier"
+ "sharedcollections/cancelmigration"
+ "sharedcollections/completemigration"
+ "sharedcollections/failmigration"
+ "sharedcollections/initiatemigration"
+ "sharedcollections/unarchivemigration"
+ "status"
+ "unarchiveMigrationToCPL"
+ "unarchived"
+ "unknown (%d)"
+ "v32@?0@\"PersonIdToCKUserIdEntry\"8Q16^B24"
+ "value"
- " updated shared album URL: %@"
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"<MMCSAsset>\"32@0:8@\"MMCSEngine\"16Q24"
- "@\"<MMCSEngineDelegate>\""
- "@\"<MSAlbumSharingDaemonDelegate>\""
- "@\"<MSBackoffManagerDelegate>\""
- "@\"<MSDeleterDelegate>\""
- "@\"<MSDeleterDelegate>\"16@0:8"
- "@\"<MSMediaStreamDaemonDelegate>\""
- "@\"<MSPublishStorageProtocol>\""
- "@\"<MSPublishStorageProtocolDelegate>\""
- "@\"<MSPublishStorageProtocolDelegate>\"16@0:8"
- "@\"<MSPublisherDelegate>\""
- "@\"<MSPublisherDelegate>\"16@0:8"
- "@\"<MSServerSideConfigProtocolDelegate>\""
- "@\"<MSStreamsProtocolDelegate>\""
- "@\"<MSSubscribeStorageProtocol>\""
- "@\"<MSSubscribeStorageProtocolDelegate>\""
- "@\"<MSSubscribeStorageProtocolDelegate>\"16@0:8"
- "@\"<MSSubscriberDelegate>\""
- "@\"<MSSubscriberDelegate>\"16@0:8"
- "@\"<NSObject>\""
- "@\"<NSObject><NSCoding>\""
- "@\"IDSService\""
- "@\"MMCSEngine\""
- "@\"MSASAlbum\""
- "@\"MSASAlbum\"24@0:8@\"NSString\"16"
- "@\"MSASAssetCollection\"24@0:8@\"NSString\"16"
- "@\"MSASAssetDownloader\""
- "@\"MSASAssetUploader\""
- "@\"MSASComment\""
- "@\"MSASComment\"24@0:8@\"NSString\"16"
- "@\"MSASDaemonModel\""
- "@\"MSASEnqueuedCommand\""
- "@\"MSASInvitation\""
- "@\"MSASInvitation\"24@0:8@\"NSString\"16"
- "@\"MSASModelEnumerator\"16@0:8"
- "@\"MSASModelEnumerator\"24@0:8@\"NSString\"16"
- "@\"MSASPConnectionGate\""
- "@\"MSASPendingChanges\""
- "@\"MSASPersonModel\""
- "@\"MSASPhoneInvitations\""
- "@\"MSASProtocol\""
- "@\"MSASServerSideModel\""
- "@\"MSASServerSideModelGroupedCommandQueue\""
- "@\"MSASSharingRelationship\"24@0:8@\"NSString\"16"
- "@\"MSASStateMachine\""
- "@\"MSASStateMachine\"16@0:8"
- "@\"MSAlbumSharingDaemon\""
- "@\"MSAsset\""
- "@\"MSBackoffManager\""
- "@\"MSDeleteStreamsProtocol\""
- "@\"MSImageScalingSpecification\""
- "@\"MSMediaStreamDaemon\""
- "@\"MSObjectQueue\""
- "@\"MSPublishStreamsProtocol\""
- "@\"MSReauthorizationProtocol\""
- "@\"MSResetServerProtocol\""
- "@\"MSServerSideConfigProtocol\""
- "@\"MSSubscribeStreamsProtocol\""
- "@\"MSSubscribedStream\"16@0:8"
- "@\"MSTimerGate\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSCountedSet\""
- "@\"NSData\""
- "@\"NSData\"16@0:8"
- "@\"NSDate\""
- "@\"NSDate\"16@0:8"
- "@\"NSDate\"24@0:8@\"NSString\"16"
- "@\"NSDictionary\""
- "@\"NSDictionary\"16@0:8"
- "@\"NSError\""
- "@\"NSError\"16@0:8"
- "@\"NSMutableArray\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSNumber\"24@0:8@\"NSString\"16"
- "@\"NSObject<OS_dispatch_group>\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSString\"24@0:8@\"NSString\"16"
- "@\"NSString\"32@0:8@\"NSString\"16@\"NSDictionary\"24"
- "@\"NSThread\""
- "@\"NSTimer\""
- "@\"NSURL\""
- "@16@0:8"
- "@20@0:8B16"
- "@20@0:8i16"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@\"NSString\"16"
- "@24@0:8@16"
- "@24@0:8Q16"
- "@24@0:8^{_NSZone=}16"
- "@24@0:8q16"
- "@28@0:8@16i24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8@16Q24"
- "@32@0:8@16^@24"
- "@32@0:8@16i24i28"
- "@32@0:8@16q24"
- "@32@0:8^{sqlite3_stmt=}16^q24"
- "@32@0:8q16q24"
- "@36@0:8@16@24i32"
- "@36@0:8i16^@20^q28"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24#32"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24^@32"
- "@40@0:8@16^@24^@32"
- "@40@0:8@16q24@32"
- "@40@0:8^{sqlite3=}16@24@?32"
- "@40@0:8{CGSize=dd}16@32"
- "@44@0:8@16@24B32i36B40"
- "@48@0:8@16@24@32@40"
- "@48@0:8@16q24@32@40"
- "@52@0:8@16@24B32@36@44"
- "@56@0:8@16@24@32@40@48"
- "@56@0:8@16q24@32@40@48"
- "@56@0:8^@16^q24^@32^@40^@48"
- "@56@0:8d16d24d32d40@48"
- "@64@0:8@16^@24^q32^@40^@48^@56"
- "@64@0:8q16^@24^q32^@40^@48^@56"
- "@?"
- "@?16@0:8"
- "@?24@0:8@16"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"NSError\"16"
- "B24@0:8@\"NSString\"16"
- "B24@0:8@\"NSURLConnection\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B24@0:8i16i20"
- "B28@0:8@\"MMCSEngine\"16i24"
- "B28@0:8@16i24"
- "B32@0:8@\"MSASStateMachine\"16@\"NSString\"24"
- "B32@0:8@\"NSURLConnection\"16@\"NSURLProtectionSpace\"24"
- "B32@0:8@16@24"
- "B32@0:8@16^@24"
- "B32@0:8@16q24"
- "B40@0:8@16@24^@32"
- "B48@0:8Q16^i24^@32^@40"
- "B56@0:8@16@24@32@40@48"
- "B56@0:8@16^@24^@32^@40^@48"
- "B68@0:8i16@20^@28^@36^@44^B52^@60"
- "B72@0:8@16^@24^Q32^@40^@48^B56^@64"
- "B80@0:8@16^@24^@32^@40^@48^@56^@64^@72"
- "B80@0:8@16^@24^@32^@40^@48^@56^q64^@72"
- "GroupedCommands"
- "HTTPBody"
- "HTTPErrorWithStatusCode:"
- "I16@0:8"
- "IDSServiceDelegate"
- "MCDictionaryUtilities"
- "MMCSAsset"
- "MMCSBackoffManagerParameters"
- "MMCSConcurrentConnectionsCount"
- "MMCSDownloadSocketOptionsForPersonID:"
- "MMCSEngine"
- "MMCSEngine:didCreateRequestorContext:forAssets:"
- "MMCSEngine:didFinishGettingAsset:path:error:"
- "MMCSEngine:didFinishPuttingAsset:error:"
- "MMCSEngine:didFinishPuttingAsset:putReceipt:error:"
- "MMCSEngine:didMakeGetProgress:state:onAsset:"
- "MMCSEngine:didMakePutProgress:state:onAsset:"
- "MMCSEngine:didRequestAssetWithItemID:"
- "MMCSEngine:logMessage:logLevel:"
- "MMCSEngine:logPerformanceMetrics:"
- "MMCSEngine:shouldLogAtLogLevel:"
- "MMCSEngineDelegate"
- "MMCSError"
- "MMCSErrorType"
- "MMCSErrorWithDomain:code:description:"
- "MMCSHash"
- "MMCSIsAuthorizationError"
- "MMCSIsCancelError"
- "MMCSIsFatalError"
- "MMCSIsNetworkConditionsError"
- "MMCSItemFlags"
- "MMCSItemID"
- "MMCSItemSize"
- "MMCSItemType"
- "MMCSOpenNewFileDescriptor"
- "MMCSRequestorContext"
- "MMCSUTI"
- "MMCSUploadSocketOptionsForPersonID:"
- "MPSStateRequest"
- "MPSStateResponse"
- "MSASAddDictionary:"
- "MSASAddEventIsDueToAlbumDeletionAlbumGUID:"
- "MSASAddEventIsDueToAssetCollectionDeletionAssetCollectionGUID:"
- "MSASAddIsAlbumResetSyncAlbumGUID:"
- "MSASAddIsErrorRecovery"
- "MSASAddIsGlobalResetSync"
- "MSASAddIsLocalChange"
- "MSASAddNotInterestingKey"
- "MSASAlbum"
- "MSASAlbumChange"
- "MSASAlbumResetSyncAlbumGUID"
- "MSASAssetCollection"
- "MSASAssetCollectionChange"
- "MSASAssetDownloader"
- "MSASAssetDownloader:didFinishDownloadingAsset:inAlbumGUID:error:"
- "MSASAssetDownloader:willBeginBatchCount:"
- "MSASAssetDownloaderDelegate"
- "MSASAssetDownloaderDidFinishBatch:"
- "MSASAssetInfoToReauthForDownload"
- "MSASAssetTransferer"
- "MSASAssetUploader"
- "MSASAssetUploader:didFinishUploadingAssetCollection:intoAlbum:error:"
- "MSASAssetUploaderDelegate"
- "MSASCloudKitPlugin"
- "MSASComment"
- "MSASCommentChange"
- "MSASCommentCheckOperation"
- "MSASCounterpartInstance"
- "MSASDaemonModel"
- "MSASDefinitions"
- "MSASDictionaryWithCopyOfDictionary:"
- "MSASEnqueuedCommand"
- "MSASEventIsDueToAlbumDeletionAlbumGUID"
- "MSASEventIsDueToAssetCollectionDeletionAssetCollectionGUID"
- "MSASGroupedQueue"
- "MSASInvitation"
- "MSASIsAllowedToTransferMetadata"
- "MSASIsAllowedToUploadAssets"
- "MSASIsErrorRecovery"
- "MSASIsGlobalResetSync"
- "MSASIsLocalChange"
- "MSASIsNotInteresting"
- "MSASModel"
- "MSASModel:didDeleteComment:forAssetCollection:inAlbum:"
- "MSASModel:didDeleteComment:forAssetCollection:inAlbum:info:"
- "MSASModel:didFailToFindAssetsForAssetCollectionGUID:assetTypeFlags:"
- "MSASModel:didFindAccessControlChange:inAlbum:"
- "MSASModel:didFindAccessControlChange:inAlbum:info:"
- "MSASModel:didFindAlbumMetadataChange:"
- "MSASModel:didFindAlbumMetadataChange:info:"
- "MSASModel:didFindAssetCollectionChange:inAlbum:"
- "MSASModel:didFindAssetCollectionChange:inAlbum:info:"
- "MSASModel:didFindCommentChange:inAssetCollection:inAlbum:"
- "MSASModel:didFindCommentChange:inAssetCollection:inAlbum:info:"
- "MSASModel:didFindDeletedAccessControl:inAlbum:"
- "MSASModel:didFindDeletedAccessControl:inAlbum:info:"
- "MSASModel:didFindDeletedAccessControls:inAlbum:info:"
- "MSASModel:didFindDeletedAlbum:"
- "MSASModel:didFindDeletedAlbum:info:"
- "MSASModel:didFindDeletedAlbums:info:"
- "MSASModel:didFindDeletedAssetCollection:inAlbum:"
- "MSASModel:didFindDeletedAssetCollection:inAlbum:info:"
- "MSASModel:didFindDeletedAssetCollections:inAlbum:info:"
- "MSASModel:didFindDeletedComments:forAssetCollection:inAlbum:info:"
- "MSASModel:didFindDeletedInvitation:"
- "MSASModel:didFindDeletedInvitation:info:"
- "MSASModel:didFindDeletedInvitations:info:"
- "MSASModel:didFindGlobalResetSyncInfo:"
- "MSASModel:didFindInvitationChange:"
- "MSASModel:didFindInvitationChange:info:"
- "MSASModel:didFindLastViewedCommentDate:forAssetCollection:inAlbum:"
- "MSASModel:didFindLastViewedCommentDate:forAssetCollection:inAlbum:info:"
- "MSASModel:didFindNewAccessControl:inAlbum:"
- "MSASModel:didFindNewAccessControl:inAlbum:info:"
- "MSASModel:didFindNewAccessControls:inAlbum:info:"
- "MSASModel:didFindNewAlbum:"
- "MSASModel:didFindNewAlbum:info:"
- "MSASModel:didFindNewAlbums:info:"
- "MSASModel:didFindNewAssetCollection:inAlbum:"
- "MSASModel:didFindNewAssetCollection:inAlbum:info:"
- "MSASModel:didFindNewAssetCollections:inAlbum:info:"
- "MSASModel:didFindNewComment:forAssetCollection:inAlbum:"
- "MSASModel:didFindNewComment:forAssetCollection:inAlbum:info:"
- "MSASModel:didFindNewComments:forAssetCollection:inAlbum:info:"
- "MSASModel:didFindNewInvitation:"
- "MSASModel:didFindNewInvitation:info:"
- "MSASModel:didFindNewInvitations:info:"
- "MSASModel:didFinishAcceptingInvitation:forAlbum:error:"
- "MSASModel:didFinishAcceptingInvitation:forAlbum:info:error:"
- "MSASModel:didFinishAddingAccessControlEntry:toAlbum:error:"
- "MSASModel:didFinishAddingAccessControlEntry:toAlbum:info:error:"
- "MSASModel:didFinishAddingAlbum:error:"
- "MSASModel:didFinishAddingAlbum:info:error:"
- "MSASModel:didFinishAddingAssetCollection:toAlbum:error:"
- "MSASModel:didFinishAddingAssetCollection:toAlbum:info:error:"
- "MSASModel:didFinishAddingComment:toAssetCollection:inAlbum:error:"
- "MSASModel:didFinishAddingComment:toAssetCollection:inAlbum:info:error:"
- "MSASModel:didFinishCheckingForChangesInfo:error:"
- "MSASModel:didFinishDeletingAlbum:error:"
- "MSASModel:didFinishDeletingAlbum:info:error:"
- "MSASModel:didFinishDeletingAssetCollection:fromAlbum:error:"
- "MSASModel:didFinishDeletingAssetCollection:fromAlbum:info:error:"
- "MSASModel:didFinishDeletingComment:fromAssetCollection:inAlbum:error:"
- "MSASModel:didFinishDeletingComment:fromAssetCollection:inAlbum:info:error:"
- "MSASModel:didFinishEnqueueingAssetsForDownload:inAlbumWithGUID:"
- "MSASModel:didFinishMarkingAlbumAsViewed:error:"
- "MSASModel:didFinishMarkingAlbumAsViewed:info:error:"
- "MSASModel:didFinishMarkingAsSpamInvitation:info:error:"
- "MSASModel:didFinishMarkingAsSpamInvitationWithToken:info:error:"
- "MSASModel:didFinishMarkingCommentsAsViewedInAssetCollection:inAlbum:error:"
- "MSASModel:didFinishMarkingCommentsAsViewedInAssetCollection:inAlbum:info:error:"
- "MSASModel:didFinishModifyingAlbumMetadata:error:"
- "MSASModel:didFinishModifyingAlbumMetadata:info:error:"
- "MSASModel:didFinishRejectingInvitation:error:"
- "MSASModel:didFinishRejectingInvitation:info:error:"
- "MSASModel:didFinishRemovingAccessControlEntry:fromAlbum:error:"
- "MSASModel:didFinishRemovingAccessControlEntry:fromAlbum:info:error:"
- "MSASModel:didFinishRetrievingAsset:inAlbum:error:"
- "MSASModel:didFinishSendingInvitationByPhone:toAlbum:info:error:"
- "MSASModel:didFinishSubscribingToAlbum:error:"
- "MSASModel:didFinishSubscribingToAlbum:info:error:"
- "MSASModel:didFinishUnsubscribingFromAlbum:error:"
- "MSASModel:didFinishUnsubscribingFromAlbum:info:error:"
- "MSASModel:didMarkAlbum:asHavingUnreadContent:"
- "MSASModel:didMarkAlbum:asHavingUnreadContent:info:"
- "MSASModel:didMarkAssetCollection:asHavingUnreadComments:inAlbum:"
- "MSASModel:didMarkAssetCollection:asHavingUnreadComments:inAlbum:info:"
- "MSASModel:didRequestDerivativesForAssetCollections:specifications:completionBlock:"
- "MSASModel:didRequestDerivativesForAssetCollections:specifications:info:completionBlock:"
- "MSASModel:didUpdateUnviewedAssetCollectionCount:forAlbum:"
- "MSASModel:didUpdateUnviewedAssetCollectionCount:forAlbum:info:"
- "MSASModelBase"
- "MSASModelDidDeleteAllAlbumsInAlbumList:"
- "MSASModelDidReceiveNewServerSideConfiguration:"
- "MSASModelDidReceiveNewServerSideConfiguration:info:"
- "MSASModelEnumerator"
- "MSASModelWillBeForgotten:"
- "MSASModelWillBeForgotten:info:"
- "MSASPAssetCollectionFromProtocolDictionary:"
- "MSASPAssetFromProtocolDictionary:"
- "MSASPCommentFromProtocolDictionary:"
- "MSASPConnectionGate"
- "MSASPInvitationFromProtocolDictionary:"
- "MSASPProtocolDictionary"
- "MSASPSharingRelationshipFromProtocolDictionary:"
- "MSASPendingChanges"
- "MSASPersonIDForPollingTriggeredByPushNotification"
- "MSASPersonIDIsAllowedToDownloadAssets:"
- "MSASPersonInfoManager"
- "MSASPersonModel"
- "MSASPersonModelItem"
- "MSASPhoneInvitations"
- "MSASProtocol"
- "MSASServerSideModel"
- "MSASServerSideModelGroupedCommandQueue"
- "MSASSharingRelationship"
- "MSASStateMachine"
- "MSASStateMachine:didFindAccessControlChangesForAlbumGUIDS:info:"
- "MSASStateMachine:didFindAlbumChanges:info:"
- "MSASStateMachine:didFindAlbumSyncedState:forAlbum:info:"
- "MSASStateMachine:didFindAssetCollectionChanges:forAlbum:info:"
- "MSASStateMachine:didFindAssetCollectionSyncedState:forAssetCollectionGUID:inAlbum:assetCollectionStateCtag:info:"
- "MSASStateMachine:didFindChangesInAlbum:info:error:"
- "MSASStateMachine:didFindCommentChanges:inAssetCollectionWithGUID:inAlbumWithGUID:info:"
- "MSASStateMachine:didFindNewURLString:forAlbumWithGUID:info:"
- "MSASStateMachine:didFindSyncedKeyValueChangesForAlbumGUIDS:albumChanges:accessControlChangesForAlbumGUIDS:info:"
- "MSASStateMachine:didFindSyncedKeyValueChangesForAlbumGUIDS:info:"
- "MSASStateMachine:didFinishAddingAssetCollection:toAlbum:info:error:"
- "MSASStateMachine:didFinishAddingComment:toAssetCollection:inAlbum:info:error:"
- "MSASStateMachine:didFinishAddingSharingRelationships:toOwnedAlbum:info:error:"
- "MSASStateMachine:didFinishCheckingForAlbumSyncedStateChangesInAlbum:info:error:newAlbumStateCtag:"
- "MSASStateMachine:didFinishCheckingForChangesInfo:error:"
- "MSASStateMachine:didFinishCheckingForCommentChangesInAssetCollectionWithGUID:largestCommentID:info:error:"
- "MSASStateMachine:didFinishCheckingForUpdatesInAlbum:info:error:"
- "MSASStateMachine:didFinishCheckingForUpdatesInAlbums:info:"
- "MSASStateMachine:didFinishCreatingAlbum:info:error:"
- "MSASStateMachine:didFinishDeletingAlbum:info:error:"
- "MSASStateMachine:didFinishDeletingAssetCollection:inAlbum:info:error:"
- "MSASStateMachine:didFinishDeletingComment:inAssetCollection:inAlbum:info:error:"
- "MSASStateMachine:didFinishEnqueueingAssetsForDownload:inAlbumWithGUID:"
- "MSASStateMachine:didFinishGettingAccessControls:forAlbum:info:error:"
- "MSASStateMachine:didFinishMarkingAsSpamInvitationForAlbum:invitationGUID:info:error:"
- "MSASStateMachine:didFinishMarkingAsSpamInvitationForToken:info:error:"
- "MSASStateMachine:didFinishRemovingSharingRelationship:fromOwnedAlbum:info:error:"
- "MSASStateMachine:didFinishRetrievingAsset:inAlbum:error:"
- "MSASStateMachine:didFinishSendingInvitationByPhone:toOwnedAlbum:info:error:"
- "MSASStateMachine:didFinishSettingSyncedStateForAlbum:info:error:newAlbumStateCtag:"
- "MSASStateMachine:didFinishSettingSyncedStateForAssetCollection:inAlbum:assetStateCtag:info:error:"
- "MSASStateMachine:didFinishSubscribingToAlbum:info:error:"
- "MSASStateMachine:didFinishUnsubscribingFromAlbum:info:error:"
- "MSASStateMachine:didFinishUpdatingAlbum:info:error:"
- "MSASStateMachine:didFinishUpdatingAssetCollections:inAlbum:info:error:"
- "MSASStateMachine:didFireScheduledEvent:forAssetCollectionGUID:albumGUID:info:"
- "MSASStateMachine:didQueryIsAssetCollectionWithGUIDInModel:"
- "MSASStateMachine:didRequestAssetsForAddingAssetCollections:inAlbum:specifications:info:"
- "MSASStateMachine:willCheckForAlbumSyncedStateChangesInAlbum:info:"
- "MSASStateMachine:willCheckForUpdatesInAlbum:info:"
- "MSASStateMachine:willUpdateAssetCollections:inAlbum:info:"
- "MSASStateMachineDelegate"
- "MSASStateMachineDidFindGlobalResetSync:info:"
- "MSASStateMachineDidRequestAlbumStateCtagForAlbumWithGUID:info:"
- "MSASStateMachineDidRequestAlbumURLStringForAlbumWithGUID:info:"
- "MSASStateMachineDidRequestAlbumWithGUID:"
- "MSASStateMachineDidRequestAssetCollectionStateCtagForAssetCollectionWithGUID:info:"
- "MSASStateMachineDidStart:"
- "MSASStateMachineDidUpdateServerCommunicationBackoffDate:"
- "MSASStateMachineIsCanceledError"
- "MSAlbumSharingDaemon"
- "MSAlbumSharingDaemon:didForgetPersonID:"
- "MSAlbumSharingDaemon:didReceiveCommentTooLongError:forAssetCollection:inAlbum:personID:"
- "MSAlbumSharingDaemon:didReceiveTooManyAlbumsError:personID:"
- "MSAlbumSharingDaemon:didReceiveTooManyCommentsError:forAssetCollection:inAlbum:personID:"
- "MSAlbumSharingDaemon:didReceiveTooManyPhotosError:forAlbum:personID:"
- "MSAlbumSharingDaemon:didReceiveTooManySubscriptionsError:personID:"
- "MSAlbumSharingDaemonDidIdle:"
- "MSAlbumSharingDaemonDidUnidle:"
- "MSArrayUtilities"
- "MSAsset"
- "MSAssetCollection"
- "MSBackoffManager"
- "MSBackoffManagerDelegate"
- "MSBackoffManagerDidUpdateNextExpiryDate:"
- "MSBase64Encoding"
- "MSCanBeIgnored"
- "MSContainsErrorWithDomain:code:"
- "MSCupidStateMachine"
- "MSDSPAssetCollectionWithMasterFileHash:"
- "MSDaemon"
- "MSDataUtilities"
- "MSDeepCopy"
- "MSDeepCopyWithZone:"
- "MSDeleteStreamsProtocol"
- "MSDeleteStreamsProtocolDelegate"
- "MSDeleter"
- "MSErrorUtilities"
- "MSErrorWithDomain:code:description:"
- "MSErrorWithDomain:code:description:suggestion:"
- "MSErrorWithDomain:code:description:underlyingError:"
- "MSErrorWithDomain:code:description:underlyingError:additionalUserInfo:"
- "MSFileUtilities"
- "MSFindPrimaryError"
- "MSHexData"
- "MSHexString"
- "MSImageScalingSpecification"
- "MSInitWithBase64Encoding:"
- "MSIsAuthError"
- "MSIsBadTokenError"
- "MSIsCounted"
- "MSIsFatal"
- "MSIsQuotaError"
- "MSIsRegistrationError"
- "MSIsTemporaryNetworkError"
- "MSMMCSProtocol"
- "MSMMCSRetryAfterDate"
- "MSMakePrimaryError"
- "MSMakeUUID"
- "MSMediaStreamDaemon"
- "MSMutableDeepCopy"
- "MSMutableDeepCopyWithZone:"
- "MSNeedsBackoff"
- "MSObjectQueue"
- "MSObjectWrapper"
- "MSPerformanceLogger"
- "MSProtocolUtilities"
- "MSPublishMMCSProtocol"
- "MSPublishStorageProtocol"
- "MSPublishStorageProtocolDelegate"
- "MSPublishStreamsProtocol"
- "MSPublishStreamsProtocolDelegate"
- "MSPublisher"
- "MSReauthorizationProtocol"
- "MSReauthorizationProtocolDelegate"
- "MSRemoveOneObject:"
- "MSRemoveOneObjectByPointerComparison:"
- "MSResetServer"
- "MSResetServerProtocol"
- "MSResetServerProtocolDelegate"
- "MSSafeUnarchiveAllowedClasses"
- "MSSafeUnarchiveObjectWithData:outError:"
- "MSSafeUnarchiveObjectWithFile:outError:"
- "MSServerSideConfigManager"
- "MSServerSideConfigProtocol"
- "MSServerSideConfigProtocolDelegate"
- "MSStorageProtocol"
- "MSStreamsProtocol"
- "MSStreamsProtocolDelegate"
- "MSStringUtilities"
- "MSStringWithBool:"
- "MSSubscribeMMCSProtocol"
- "MSSubscribeStorageProtocol"
- "MSSubscribeStorageProtocolDelegate"
- "MSSubscribeStreamsProtocol"
- "MSSubscribeStreamsProtocolDelegate"
- "MSSubscribedStream"
- "MSSubscriber"
- "MSTempFileOutFileName:"
- "MSTimerGate"
- "MSUniqueID"
- "MSUtilities"
- "MSVerboseDescription"
- "MSVideoDerivativeSpecification"
- "NSCoding"
- "NSCopying"
- "NSObject"
- "NSSecureCoding"
- "NSURLConnectionDelegate"
- "OSString"
- "Photos"
- "Q"
- "Q16@0:8"
- "SharedAlbumsDBR"
- "StringAsIcplAction:"
- "StringAsMpsAction:"
- "T#,R"
- "T@\"<MMCSEngineDelegate>\",W,N,V_delegate"
- "T@\"<MSASAssetDownloaderDelegate>\",W,D,N"
- "T@\"<MSASAssetUploaderDelegate>\",W,D,N"
- "T@\"<MSAlbumSharingDaemonDelegate>\",W,N,V_delegate"
- "T@\"<MSBackoffManagerDelegate>\",N,V_delegate"
- "T@\"<MSDeleteStreamsProtocolDelegate>\",D,N"
- "T@\"<MSDeleterDelegate>\",N"
- "T@\"<MSDeleterDelegate>\",N,V_delegate"
- "T@\"<MSMediaStreamDaemonDelegate>\",N,V_delegate"
- "T@\"<MSPublishStorageProtocolDelegate>\",N"
- "T@\"<MSPublishStorageProtocolDelegate>\",N,V_delegate"
- "T@\"<MSPublisherDelegate>\",N"
- "T@\"<MSPublisherDelegate>\",N,V_delegate"
- "T@\"<MSServerSideConfigProtocolDelegate>\",N,V_delegate"
- "T@\"<MSStreamsProtocolDelegate>\",N,V_delegate"
- "T@\"<MSSubscribeStorageProtocolDelegate>\",N"
- "T@\"<MSSubscribeStorageProtocolDelegate>\",N,V_delegate"
- "T@\"<MSSubscriberDelegate>\",N"
- "T@\"<MSSubscriberDelegate>\",N,V_delegate"
- "T@\"<NSCoding>\",R,N,V_object"
- "T@\"<NSObject>\",&,N,V_object"
- "T@\"IDSService\",&,N,V_idsService"
- "T@\"MMCSEngine\",R,N,V_engine"
- "T@\"MMCSEngine\",W,N,V_engine"
- "T@\"MSASAlbum\",&,N,V_album"
- "T@\"MSASComment\",&,N,V_comment"
- "T@\"MSASDaemonModel\",&,N,V_daemonModel"
- "T@\"MSASEnqueuedCommand\",&,N,V_lastEnqueuedCommand"
- "T@\"MSASInvitation\",&,N,V_invitation"
- "T@\"MSASPConnectionGate\",&,N,V_gate"
- "T@\"MSASPendingChanges\",&,N,V_pendingChanges"
- "T@\"MSASPersonModel\",W,N,V_model"
- "T@\"MSASPhoneInvitations\",&,N,V_phoneInvitations"
- "T@\"MSASProtocol\",&,N,V_protocol"
- "T@\"MSASServerSideModel\",W,N,V_model"
- "T@\"MSASServerSideModelGroupedCommandQueue\",&,N,V_commandQueue"
- "T@\"MSASStateMachine\",&,N,V_stateMachine"
- "T@\"MSASStateMachine\",N"
- "T@\"MSASStateMachine\",N,V_counterpartInstance"
- "T@\"MSASStateMachine\",R,N"
- "T@\"MSAlbumSharingDaemon\",W,N,V_daemon"
- "T@\"MSAsset\",&,N,V_asset"
- "T@\"MSAsset\",&,N,V_masterAsset"
- "T@\"MSBackoffManager\",W,N,V_backoffManager"
- "T@\"MSImageScalingSpecification\",R,&,N,V_derivativeImageScalingSpecification"
- "T@\"MSImageScalingSpecification\",R,&,N,V_thumbnailImageScalingSpecification"
- "T@\"MSMediaStreamDaemon\",N,V_daemon"
- "T@\"MSTimerGate\",&,N,V_idleTimerGate"
- "T@\"MSTimerGate\",&,N,V_stalenessTimerGate"
- "T@\"NSArray\",&,N"
- "T@\"NSArray\",&,N,V_assets"
- "T@\"NSArray\",&,N,V_emails"
- "T@\"NSArray\",&,N,V_phones"
- "T@\"NSArray\",R,&,N,V_derivativeSpecifications"
- "T@\"NSCountedSet\",&,N,V_observers"
- "T@\"NSData\",&,N"
- "T@\"NSData\",&,N,V_fileData"
- "T@\"NSData\",&,N,V_fileHash"
- "T@\"NSData\",&,N,V_masterAssetHash"
- "T@\"NSData\",R,W,N"
- "T@\"NSDate\",&"
- "T@\"NSDate\",&,N"
- "T@\"NSDate\",&,N,V_MMCSAccessHeaderTimeStamp"
- "T@\"NSDate\",&,N,V_batchCreationDate"
- "T@\"NSDate\",&,N,V_clientTimestamp"
- "T@\"NSDate\",&,N,V_photoCreationDate"
- "T@\"NSDate\",&,N,V_serverUploadedDate"
- "T@\"NSDate\",&,N,V_subscriptionDate"
- "T@\"NSDate\",&,N,V_timestamp"
- "T@\"NSDate\",&,V_retryAfterDate"
- "T@\"NSDictionary\",&,N"
- "T@\"NSDictionary\",&,N,V_MMCSBackoffManagerParameters"
- "T@\"NSDictionary\",&,N,V_invariantParam"
- "T@\"NSDictionary\",&,N,V_metadata"
- "T@\"NSDictionary\",&,N,V_metadataBackoffManagerParameters"
- "T@\"NSDictionary\",&,N,V_serverSideConfiguration"
- "T@\"NSDictionary\",&,N,V_variantParam"
- "T@\"NSError\",&,N"
- "T@\"NSError\",&,N,V_error"
- "T@\"NSMutableArray\",&,N,S_setAssetInfoToReauthForDownload:,V_assetInfoToReauthForDownload"
- "T@\"NSMutableArray\",&,N,V_finishedAssetCollections"
- "T@\"NSMutableArray\",&,N,V_finishedAssets"
- "T@\"NSMutableArray\",&,N,V_itemsInFlight"
- "T@\"NSMutableDictionary\",&,N,V_assetCollectionGUIDToRequestorContext"
- "T@\"NSMutableDictionary\",&,N,V_assetCollectionsToItemInFlightMap"
- "T@\"NSMutableDictionary\",&,N,V_assetToAssetCollectionMap"
- "T@\"NSMutableDictionary\",&,N,V_assetToItemInFlightMap"
- "T@\"NSMutableDictionary\",&,N,V_nextUpdateDateByPersonID"
- "T@\"NSMutableDictionary\",&,N,V_pendingAlbumGUIDToAssetCollections"
- "T@\"NSMutableDictionary\",&,N,V_personIDToDelegateMap"
- "T@\"NSMutableDictionary\",&,N,V_personIDToPersonInfoDictionary"
- "T@\"NSMutableDictionary\",&,N,V_personIDToStateMachineMap"
- "T@\"NSMutableDictionary\",&,N,V_sendMessageIdentifierToPhone"
- "T@\"NSMutableDictionary\",&,N,V_userManifest"
- "T@\"NSMutableSet\",&,N,V_assetCollectionsWithAuthorizationError"
- "T@\"NSMutableSet\",&,N,V_pendingAlbumChanges"
- "T@\"NSMutableSet\",&,N,V_pendingAlbumGUIDsWithKeyValueChanges"
- "T@\"NSMutableSet\",&,N,V_pendingAlbumGUIDsWithSharingInfoChanges"
- "T@\"NSObject<OS_dispatch_group>\",&,N,V_pendingConnectionsGroup"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_eventQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_idleCountQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_mapQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_memberQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_pendingConnectionsQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_queue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_serverSideConfigQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_statementQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_workQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,N,V_dbQueue"
- "T@\"NSString\",&,N"
- "T@\"NSString\",&,N,V_GUID"
- "T@\"NSString\",&,N,V_MMCSAccessHeader"
- "T@\"NSString\",&,N,V_MMCSReceipt"
- "T@\"NSString\",&,N,V_URLString"
- "T@\"NSString\",&,N,V_albumGUID"
- "T@\"NSString\",&,N,V_assetCollectionGUID"
- "T@\"NSString\",&,N,V_assetCollectionID"
- "T@\"NSString\",&,N,V_backupDeviceID"
- "T@\"NSString\",&,N,V_backupDeviceUDID"
- "T@\"NSString\",&,N,V_backupDeviceUUID"
- "T@\"NSString\",&,N,V_clientOrgKey"
- "T@\"NSString\",&,N,V_content"
- "T@\"NSString\",&,N,V_ctag"
- "T@\"NSString\",&,N,V_currentFocusAlbumGUID"
- "T@\"NSString\",&,N,V_currentFocusAssetCollectionGUID"
- "T@\"NSString\",&,N,V_downloadBatchPerfGUID"
- "T@\"NSString\",&,N,V_email"
- "T@\"NSString\",&,N,V_fileName"
- "T@\"NSString\",&,N,V_firstName"
- "T@\"NSString\",&,N,V_focusAlbumGUID"
- "T@\"NSString\",&,N,V_focusAssetCollectionGUID"
- "T@\"NSString\",&,N,V_foreignCtag"
- "T@\"NSString\",&,N,V_fullName"
- "T@\"NSString\",&,N,V_iCPLDeviceID"
- "T@\"NSString\",&,N,V_lastName"
- "T@\"NSString\",&,N,V_mPSDeviceID"
- "T@\"NSString\",&,N,V_name"
- "T@\"NSString\",&,N,V_objectGUID"
- "T@\"NSString\",&,N,V_ownerEmail"
- "T@\"NSString\",&,N,V_ownerFirstName"
- "T@\"NSString\",&,N,V_ownerFullName"
- "T@\"NSString\",&,N,V_ownerLastName"
- "T@\"NSString\",&,N,V_ownerPersonID"
- "T@\"NSString\",&,N,V_path"
- "T@\"NSString\",&,N,V_pathForPersonInfoDictionary"
- "T@\"NSString\",&,N,V_personID"
- "T@\"NSString\",&,N,V_publicURLString"
- "T@\"NSString\",&,N,V_serverSideConfigVersion"
- "T@\"NSString\",&,N,V_streamID"
- "T@\"NSString\",&,N,V_type"
- "T@\"NSString\",&,N,V_updatedSharedAlbumURL"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_command"
- "T@\"NSString\",C,N,V_focusAlbumGUID"
- "T@\"NSString\",C,N,V_focusAssetCollectionGUID"
- "T@\"NSString\",C,N,V_ownerEmail"
- "T@\"NSString\",C,N,V_ownerFirstName"
- "T@\"NSString\",C,N,V_ownerFullName"
- "T@\"NSString\",C,N,V_ownerLastName"
- "T@\"NSString\",C,N,V_ownerPersonID"
- "T@\"NSString\",C,N,V_personID"
- "T@\"NSString\",R,&,N"
- "T@\"NSString\",R,&,N,V_personID"
- "T@\"NSString\",R,&,N,V_serverSideConfigurationVersion"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N,V_headerVersion"
- "T@\"NSString\",R,N,V_personID"
- "T@\"NSString\",R,N,V_videoType"
- "T@\"NSThread\",&,N,V_workThread"
- "T@\"NSTimer\",&,N,V_hysteresisTimer"
- "T@\"NSTimer\",&,N,V_threadKeepAliveTimer"
- "T@\"NSURL\",&,N,V_MMCSURL"
- "T@\"NSURL\",&,N,V_baseURL"
- "T@\"NSURL\",&,N,V_storageProtocolURL"
- "T@\"NSURL\",R,W,N"
- "T@,&,N,V_context"
- "T@,&,N,V_userInfo"
- "T@,W,N,V_delegate"
- "T@?,C,N,S_setStopHandlerBlock:,V_stopHandlerBlock"
- "T@?,C,N,V_postCommandCompletionBlock"
- "T@?,C,N,V_stepBlock"
- "TB,N"
- "TB,N,V_assetDataAvailableOnServer"
- "TB,N,V_autoGenerateItemID"
- "TB,N,V_dbWasRecreated"
- "TB,N,V_didEncounterNetworkConditionError"
- "TB,N,V_enabled"
- "TB,N,V_hasComments"
- "TB,N,V_hasDeactivated"
- "TB,N,V_hasShutDown"
- "TB,N,V_isBatchComment"
- "TB,N,V_isCaption"
- "TB,N,V_isDeletable"
- "TB,N,V_isDone"
- "TB,N,V_isDownloadingThumbnails"
- "TB,N,V_isFamilySharedAlbum"
- "TB,N,V_isLike"
- "TB,N,V_isMetricsGatheringEnabled"
- "TB,N,V_isMine"
- "TB,N,V_isRetryingOutstandingActivities"
- "TB,N,V_isShuttingDown"
- "TB,N,V_isWaitingForFirstDownloadEvent"
- "TB,N,V_ownerIsWhitelisted"
- "TB,N,V_shouldDownloadEarliestPhotosFirst"
- "TB,N,V_stabilizedIsBusy"
- "TB,N,V_wasDeleted"
- "TB,R"
- "TB,R,N"
- "TB,R,N,V_isAssertingBusyAssertion"
- "TB,R,N,V_powerRequired"
- "TB,R,N,V_useCellular"
- "TI,N"
- "TQ,N"
- "TQ,N,V_count"
- "TQ,N,V_mediaAssetType"
- "TQ,N,V_protocolFileSize"
- "TQ,R"
- "TQ,R,N,V_mediaAssetType"
- "T^*,N,V_authTokens"
- "T^*,N,V_signatures"
- "T^I,N,V_itemFlags"
- "T^Q,N,V_itemIDs"
- "T^{__CFDictionary=},N,V_statements"
- "T^{_mmcs_engine=},R,N,V_engine"
- "T^{sqlite3=},N,V_db"
- "T^{sqlite3=},R,N,V_db"
- "T^{sqlite3_stmt=},N,V_stmt"
- "Td,N"
- "Td,N,V_backoffFactor"
- "Td,N,V_currentInterval"
- "Td,N,V_initialInterval"
- "Td,N,V_maxBackoffInterval"
- "Td,N,V_maxGroupedCallbackEventIdleInterval"
- "Td,N,V_maxGroupedCallbackEventStaleness"
- "Td,N,V_maxMMCSTokenValidityTimeInterval"
- "Td,N,V_maximumLongSideLength"
- "Td,N,V_minimumLongSideLength"
- "Td,N,V_nominalShortSideLength"
- "Td,N,V_randomizeFactor"
- "Td,R,N,V_bitRate"
- "Ti,N"
- "Ti,N,V_ID"
- "Ti,N,V_UIBusyCount"
- "Ti,N,V_assetTypeFlags"
- "Ti,N,V_batchSize"
- "Ti,N,V_busyCount"
- "Ti,N,V_deletionIndex"
- "Ti,N,V_errorCount"
- "Ti,N,V_icplAction"
- "Ti,N,V_maxBatchCount"
- "Ti,N,V_maxGroupedCallbackEventBatchCount"
- "Ti,N,V_maxMetadataRetryCount"
- "Ti,N,V_maxRetryCount"
- "Ti,N,V_mpsAction"
- "Ti,N,V_publishBatchSize"
- "Ti,N,V_relationshipState"
- "Ti,N,V_retrievalBatchSize"
- "Ti,N,V_state"
- "Ti,N,V_type"
- "Tq,N,V_initialFailureDate"
- "Tq,N,V_originalLibrarySize"
- "Tq,N,V_photoNumber"
- "Tq,N,V_publishTargetByteCount"
- "Tq,N,V_retryAfterSeconds"
- "Tq,N,V_size"
- "Tq,N,V_targetRetrievalByteCount"
- "Tq,N,V_uniqueID"
- "Tq,N,V_version"
- "Tq,R"
- "UIBusyCount"
- "URL"
- "URLByAppendingPathComponent:"
- "URLString"
- "URLWithString:"
- "URLWithString:relativeToURL:"
- "UTF8String"
- "Vv16@0:8"
- "Win32SHA1OfUDID:"
- "^*"
- "^*16@0:8"
- "^I"
- "^I16@0:8"
- "^Q"
- "^Q16@0:8"
- "^{_NSZone=}16@0:8"
- "^{__CFDictionary=}"
- "^{__CFDictionary=}16@0:8"
- "^{__MSSSPCChunkParsingContext=^v^?^?^?^?^?^{__CFString}^{__CFURL}^{__CFString}^{__CFString}i}"
- "^{_mmcs_engine=}"
- "^{_mmcs_engine=}16@0:8"
- "^{sqlite3=}"
- "^{sqlite3=}16@0:8"
- "^{sqlite3_stmt=}"
- "^{sqlite3_stmt=}16@0:8"
- "^{sqlite3_stmt=}24@0:8@16"
- "^{sqlite3_stmt=}32@0:8@16r*24"
- "_GUID"
- "_ID"
- "_MMCSAccessHeader"
- "_MMCSAccessHeaderTimeStamp"
- "_MMCSApplyBlock:"
- "_MMCSBackoffManager"
- "_MMCSBackoffManagerParameters"
- "_MMCSDirPath"
- "_MMCSReceipt"
- "_MMCSTokenTooOldError"
- "_MMCSURL"
- "_MSApplyBlock:"
- "_MSVerboseDescriptionRecursionCount:"
- "_UCContext"
- "_UIBusyCount"
- "_URLReauthFailureWithUnderlyingError:"
- "_URLString"
- "_abort"
- "_abortedError"
- "_actionDidFinishWithError:album:"
- "_addAssetCollectionsDisposition:params:"
- "_addAssetToFileHashMap:"
- "_addCommentDisposition:params:"
- "_addCommentURLWithBaseURL:"
- "_album"
- "_albumForRequestFromParams:"
- "_albumGUID"
- "_albumStateURL"
- "_albumSummaryURLWithBaseURL:"
- "_appIDHeader"
- "_asset"
- "_assetCollectionFailedError"
- "_assetCollectionGUID"
- "_assetCollectionGUIDToRequestorContext"
- "_assetCollectionID"
- "_assetCollectionRejectedError"
- "_assetCollectionsFromCoreArray:personID:outError:"
- "_assetCollectionsInFlight"
- "_assetCollectionsToItemInFlightMap"
- "_assetCollectionsWithAuthorizationError"
- "_assetDataAvailableOnServer"
- "_assetDownloader"
- "_assetFromCoreDictionary:personID:outError:"
- "_assetInfoToReauthForDownload"
- "_assetToAssetCollectionMap"
- "_assetToItemInFlightMap"
- "_assetTypeFlags"
- "_assetUploader"
- "_assetWithItemID:"
- "_assets"
- "_assetsBeingRetrieved"
- "_assetsInFlight"
- "_authTokens"
- "_autoGenerateItemID"
- "_autoItemIDDictionary"
- "_autoItemIDDictionaryQueue"
- "_autoItemIDPersistenceURL"
- "_backoffFactor"
- "_backoffMMCSBackoffTimer"
- "_backoffManager"
- "_backoffStreamsBackoffTimer"
- "_backupDeviceID"
- "_backupDeviceUDID"
- "_backupDeviceUUID"
- "_baseURL"
- "_batchCreationDate"
- "_batchSize"
- "_bitRate"
- "_boundDeleterForPersonID:"
- "_boundPublisherForPersonID:"
- "_boundServerSideConfigManagerForPersonID:"
- "_boundSubscriberForPersonID:"
- "_busyCount"
- "_cancelOutstandingCommandsDisposition:params:"
- "_canceledError"
- "_categorizeError:setOutIsIgnorable:setOutIsCounted:setOutIsFatal:setOutNeedsBackoff:setOutIsTemporary:setOutIsTokenAuth:setOutIsAuthError:"
- "_changeRetrievalStateTo:"
- "_changeStateTo:"
- "_checkAssetCollectionFiles:"
- "_checkForAlbumSyncedStateDisposition:params:"
- "_checkForAssetCollectionUpdatesDisposition:params:"
- "_checkForChangesDisposition:params:"
- "_checkForCommentChangesDisposition:params:"
- "_checkForNewAssetCollections"
- "_checkForUpdatesInAlbumDisposition:params:"
- "_checkObjectWrappers:"
- "_checkOneMoreTime"
- "_chunkDidBeginStreamForPersonID:wasReset:metadata:"
- "_chunkDidEndStreamForPersonID:ctag:"
- "_chunkDidFindSubscriptionGoneForPersonID:"
- "_chunkDidFindSubscriptionTemporarilyUnavailableForPersonID:"
- "_chunkDidParseAssetCollections:forPersonID:"
- "_chunkIndex"
- "_clearInstantiatedDeletersByPersonID"
- "_clearInstantiatedPublishersByPersonID"
- "_clearInstantiatedSubscribersByPersonID"
- "_clientOrgKey"
- "_clientTimestamp"
- "_collectionWithNoDerivatives:"
- "_collectionsInFlight"
- "_command"
- "_commandQueue"
- "_commandState"
- "_commandWithMinimumIdentifier:outParams:outCommandIdentifier:outPersonID:outAlbumGUID:outAssetCollectionGUID:"
- "_comment"
- "_commitUserManifest"
- "_complainAboutMissingKeyInArchive:"
- "_config"
- "_configPath"
- "_configURL"
- "_content"
- "_context"
- "_continueAddingAssetCollectionsDisposition:params:"
- "_coreProtocolDidFailAuthentication:"
- "_coreProtocolDidFailAuthenticationError:"
- "_coreProtocolDidFinishError:"
- "_coreProtocolDidFinishResponse:error:"
- "_coreProtocolDidFinishUCResults:error:"
- "_coreProtocolDidGetDataChunk:"
- "_couldNotReauthorizeError"
- "_count"
- "_counterpartInstance"
- "_createAlbumDisposition:params:"
- "_createAlbumURL"
- "_createCopiedAssetsInAssetCollections:"
- "_ctag"
- "_currentCommand"
- "_currentCommandID"
- "_currentCommandParams"
- "_currentFocusAlbumGUID"
- "_currentFocusAssetCollectionGUID"
- "_currentInterval"
- "_daemon"
- "_daemonModel"
- "_dataClass"
- "_db"
- "_dbQueue"
- "_dbWasRecreated"
- "_decryptedObjectForRecord:forKey:validateClass:"
- "_delegate"
- "_delegateForPersonID:"
- "_deleteAlbumDisposition:params:"
- "_deleteAssetCollectionsDisposition:params:"
- "_deleteAssetFilesInAssetCollection:"
- "_deleteAssetFilesInAssetCollections:"
- "_deleteAssetsURLWithBaseURL:"
- "_deleteCommentDisposition:params:"
- "_deleteCommentURLWithBaseURL:"
- "_deleteQueue"
- "_deleteURLWithBaseURL:"
- "_deletionIndex"
- "_derivativeImageScalingSpecification"
- "_derivativeSpecifications"
- "_derivativesQueue"
- "_derivedAssets"
- "_descriptionForRetrievalState:"
- "_descriptionForState:"
- "_didChangeIdleBusyState:"
- "_didEncounterNetworkConditionError"
- "_didFailAuthenticationWithError:"
- "_didFindServerSideConfigurationVersion:"
- "_didFinishCheckingUpdatesInAlbumsDisposition:params:"
- "_didFinishRetrievingSubscriptionUpdate"
- "_didFinishUsingAssetCollections:"
- "_didFinishWithResponse:error:"
- "_didReceiveAuthenticationError:"
- "_didReceiveMMCSRetryAfterDate:"
- "_didReceiveRetryAfterDate:"
- "_didReceiveStreamsRetryAfterDate:"
- "_doNothingTimerHandler:"
- "_downloadBatchPerfGUID"
- "_email"
- "_emails"
- "_enableMultipleContributorsURLWithBaseURL:"
- "_enablePublicAccessURLWithBaseURL:"
- "_enabled"
- "_engine"
- "_engineClientContext"
- "_engineDirPath"
- "_error"
- "_errorCount"
- "_eventQueue"
- "_fetchClientOrgKeyAndPersistLocallyForResponseDict:isOwned:completionHandler:"
- "_fetchRecordWithRecordID:zoneName:fieldName:ownerUserID:isOwned:completionHandler:"
- "_fileData"
- "_fileHash"
- "_fileHashToAssetMap"
- "_fileName"
- "_fileSize"
- "_fileSizeOnDisk"
- "_finishedAssetCollections"
- "_finishedAssets"
- "_finishedRetrievingAsset:"
- "_firstName"
- "_focusAlbumGUID"
- "_focusAssetCollectionGUID"
- "_foreignCtag"
- "_forget"
- "_fullName"
- "_gate"
- "_getAccessControlsDisposition:params:"
- "_getAlbumURL"
- "_getAlbumURLDisposition:params:"
- "_getAssetsURLWithBaseURL:"
- "_getChangesURL"
- "_getCommentsURLWithBaseURL:"
- "_getFileDescriptorAndContentTypeFromItemID:outFD:outItemType:outError:"
- "_getFileDescriptorFromItem:"
- "_getItemDone:path:error:"
- "_getItemDoneItemID:path:requestorContext:error:"
- "_getItemProgressItemID:state:progress:requestorContext:error:"
- "_getTokensURLWithBaseURL:"
- "_getUTIFromItem:"
- "_getUploadTokensURLWithBaseURL:"
- "_getVideoURLWithBaseURL:"
- "_has"
- "_hasComments"
- "_hasDeactivated"
- "_hasOutstandingPoll"
- "_hasShutDown"
- "_headerVersion"
- "_hysteresisTimer"
- "_hysteresisTimerDidFire:"
- "_iCPLDeviceID"
- "_icplAction"
- "_idleCountQueue"
- "_idleTimerGate"
- "_idsService"
- "_initItemIDPersistence"
- "_initialFailureDate"
- "_initialInterval"
- "_insertInfoAboutAsset:intoDictionary:outError:"
- "_invalidAccessControlGUIDErrorwithGUID:"
- "_invalidAssetCollectionGUIDErrorwithGUID:"
- "_invalidFieldErrorWithFieldName:"
- "_invalidFieldErrorWithFieldName:suggestion:"
- "_invalidInvitationGUIDErrorWithGUID:"
- "_invalidStreamsResponseErrorUnderlyingError:"
- "_invariantParam"
- "_invitation"
- "_isAllowedToDelete"
- "_isAllowedToDownload"
- "_isAllowedToUpload"
- "_isAssertingBusyAssertion"
- "_isBatchComment"
- "_isCaption"
- "_isDeletable"
- "_isDone"
- "_isDownloadingThumbnails"
- "_isFamilySharedAlbum"
- "_isInRetryState"
- "_isLike"
- "_isMetricsGatheringEnabled"
- "_isMine"
- "_isRetryingOutstandingActivities"
- "_isShuttingDown"
- "_isWaitingForFirstDownloadEvent"
- "_itemCount"
- "_itemFlags"
- "_itemIDToAssetDict"
- "_itemIDToAssetMap"
- "_itemIDToAssetMapQueue"
- "_itemIDs"
- "_itemsInFlight"
- "_lastEnqueuedCommand"
- "_lastName"
- "_latestNextActivityDate"
- "_logSqliteErrorLine:"
- "_mPSDeviceID"
- "_manifestPath"
- "_mapQueue"
- "_markAsSpamInvitationForAlbumDisposition:params:"
- "_markAsSpamInvitationForTokenDisposition:params:"
- "_masterAsset"
- "_masterAssetHash"
- "_maxBackoffInterval"
- "_maxBatchCount"
- "_maxErrorCount"
- "_maxGroupedCallbackEventBatchCount"
- "_maxGroupedCallbackEventIdleInterval"
- "_maxGroupedCallbackEventStaleness"
- "_maxMMCSTokenValidityTimeInterval"
- "_maxMetadataRetryCount"
- "_maxRetryCount"
- "_maxSizeByUTI"
- "_maximumLongSideLength"
- "_mediaAssetType"
- "_memberQueue"
- "_metadata"
- "_metadataBackoffManager"
- "_metadataBackoffManagerParameters"
- "_metadataDictForAsset:outError:"
- "_metadataDictForAssetCollection:outError:"
- "_minimumLongSideLength"
- "_missingAssetFieldErrorWithFieldName:"
- "_missingMMCSTokenError"
- "_missingURLError"
- "_model"
- "_mpsAction"
- "_name"
- "_newSubscriptionsByStreamID"
- "_nextExpiryDate"
- "_nextItemID"
- "_nextUpdateDateByPersonID"
- "_nominalShortSideLength"
- "_object"
- "_objectGUID"
- "_objectWrapperFromQueueQuery:outSize:"
- "_observers"
- "_options"
- "_originalLibrarySize"
- "_orphanedAssetCollectionError"
- "_orphanedAssetError"
- "_ownerEmail"
- "_ownerFirstName"
- "_ownerFullName"
- "_ownerIsWhitelisted"
- "_ownerLastName"
- "_ownerPersonID"
- "_parseChunks"
- "_parseContext"
- "_parseNextChunk"
- "_path"
- "_pathForPersonID:"
- "_pathForPersonInfoDictionary"
- "_pathToChunkIndex:"
- "_pendingAlbumChanges"
- "_pendingAlbumGUIDToAssetCollections"
- "_pendingAlbumGUIDsWithKeyValueChanges"
- "_pendingAlbumGUIDsWithSharingInfoChanges"
- "_pendingChanges"
- "_pendingConnectionsGroup"
- "_pendingConnectionsQueue"
- "_pendingDerivativesQueue"
- "_personID"
- "_personIDToDelegateMap"
- "_personIDToPersonInfoDictionary"
- "_personIDToStateMachineMap"
- "_phoneInvitations"
- "_phones"
- "_photoCreationDate"
- "_photoNumber"
- "_postCommandCompletionBlock"
- "_postModelShutdownForPersonID:completionBlock:"
- "_powerRequired"
- "_prepareHeadersForRequest:"
- "_protocol"
- "_protocolErrorForUnderlyingError:"
- "_protocolFileSize"
- "_publicURLString"
- "_publishBatchSize"
- "_publishTargetByteCount"
- "_putAssetsURLWithBaseURL:"
- "_putItemDone:putReceipt:error:"
- "_putItemDoneItemID:requestorContext:putReceipt:error:"
- "_putItemProgressItemID:state:progress:requestorContext:error:"
- "_putItemsFailure"
- "_quarantineOrDiscardWrappers:withError:"
- "_quarantinedQueue"
- "_queue"
- "_randomizeFactor"
- "_reauthProtocol"
- "_reauthorizeAssets"
- "_reconstruct"
- "_refreshAuthTokenForContext:"
- "_refreshServerSideConfigurationParameters"
- "_refreshServerSideConfiguredParameters"
- "_registerAllAssetsForWrapper:"
- "_registerAsset:"
- "_registerRequestorContext:"
- "_relationshipState"
- "_removeAssetForItemID:"
- "_removeAssetFromFileHashMap:"
- "_removeAssetsInAssetCollectionWrappersFromAssetMap:"
- "_removeRequestorContext:"
- "_removeSharingRelationshipsDisposition:params:"
- "_reportSpamURL"
- "_reqestorContextQueue"
- "_requestAuthQueue"
- "_requestCompleted"
- "_requestCompletedRequestorContext:"
- "_requestDerivatives"
- "_requestedDeleteWrappers"
- "_requestorContexts"
- "_rereadPerformanceLoggingSetting"
- "_resetConnectionVariables"
- "_resetMMCSBackoffTimer"
- "_resetStreamsBackoffTimer"
- "_retainedObjects"
- "_retrievalBatchSize"
- "_retrievalQueue"
- "_retrievalState"
- "_retrieveAssets"
- "_retrieveNextAssets"
- "_retryAfterDate"
- "_retryAfterSeconds"
- "_scheduleEventDisposition:params:"
- "_selfReference"
- "_sendDeleteRequest"
- "_sendDidIdleNotification"
- "_sendFilesToMMCS"
- "_sendGetServerSideConfigurationDisposition:params:"
- "_sendGetUploadTokensDisposition:params:"
- "_sendMessageIdentifierToPhone"
- "_sendMetadataToStreams"
- "_sendOneURLRequest:checkServerSideConfigVersion:retryCount:completionBlock:"
- "_sendPutAssetCollectionsDisposition:params:"
- "_sendReauthorizeAssetsForDownloadDisposition:params:"
- "_sendUploadComplete"
- "_sendUploadCompleteDisposition:params:"
- "_sendingQueue"
- "_sendingQueueCount"
- "_serverSideConfigDictionaryByApplyingDefaultsToDictionary:"
- "_serverSideConfigQueue"
- "_serverSideConfigURL"
- "_serverSideConfigVersion"
- "_serverSideConfiguration"
- "_serverSideConfigurationDidChange:"
- "_serverSideConfigurationVersion"
- "_serverUploadedDate"
- "_setAlbumStateURL"
- "_setAlbumSyncedStateDisposition:params:"
- "_setAssetCollectionSyncedStateDisposition:params:"
- "_setAssetInfoToReauthForDownload:"
- "_setAssetStateURL"
- "_setClientOrgKeyForRequestBody:clientOrgKey:"
- "_setCommentPositionURL"
- "_setError"
- "_setHasOutstandingPoll:"
- "_setMasterNextActivityDate:forPersonID:"
- "_setStopHandlerBlock:"
- "_setSubscriptionsByStreamID:"
- "_shareURL"
- "_sharingInfoURLWithBaseURL:"
- "_shouldDownloadEarliestPhotosFirst"
- "_signatures"
- "_size"
- "_stabilizedIsBusy"
- "_stalenessTimerGate"
- "_startOfUpload"
- "_state"
- "_stateMachine"
- "_statementLabel:query:"
- "_statementQueue"
- "_statements"
- "_stepBlock"
- "_stmt"
- "_stop"
- "_stopHandlerBlock"
- "_stopOutSubscriberState:outRetrievalState:"
- "_stoppedError"
- "_storageProtocol"
- "_storageProtocolURL"
- "_streamID"
- "_streamsBackoffManager"
- "_subscribeToAlbumDisposition:params:"
- "_subscribeURL"
- "_subscriptionDate"
- "_subscriptionsByStreamID"
- "_targetRetrievalByteCount"
- "_tellDelegateProtocolDidFinishRetrievingAssetParams:"
- "_tempFiles"
- "_threadKeepAliveTimer"
- "_thumbnailImageScalingSpecification"
- "_timestamp"
- "_type"
- "_uniqueID"
- "_unshareURL"
- "_unsubscribeFromAlbumDisposition:params:"
- "_unsubscribeURL"
- "_updateAlbumDisposition:params:"
- "_updateAlbumURLWithBaseURL:"
- "_updateMasterManifest"
- "_updatedSharedAlbumURL"
- "_uploadCompleteURLWithBaseURL:"
- "_uploadQueue"
- "_urlSession"
- "_useCellular"
- "_userInfo"
- "_userManifest"
- "_validateInvitationURL"
- "_variantParam"
- "_verifyAssetFile:"
- "_version"
- "_videoType"
- "_wasDeleted"
- "_workPathURL"
- "_workQueue"
- "_workQueueDidFinishWithItem:error:"
- "_workQueueEmptyFileTransferQueuesCompletionBlock:"
- "_workQueueGoIdle"
- "_workQueueStop"
- "_workQueueStopTrackingItem:"
- "_workThread"
- "abort"
- "abortAllActivities"
- "abortAllActivityForPersonID:"
- "absoluteString"
- "acceptInvitationWithGUID:"
- "acceptInvitationWithGUID:info:"
- "acceptInvitationWithGUID:personID:"
- "acceptInvitationWithGUID:personID:info:"
- "acceptInvitationWithToken:completionBlock:"
- "acceptInvitationWithToken:info:completionBlock:"
- "acceptInvitationWithToken:personID:completionBlock:"
- "acceptInvitationWithToken:personID:info:completionBlock:"
- "accessControlGUIDsForAlbumWithGUID:"
- "accessControlWithGUID:"
- "accessControlsForAlbumWithGUID:"
- "accounts"
- "addAccessControlEntries:toAlbumWithGUID:completionBlock:"
- "addAccessControlEntries:toAlbumWithGUID:info:completionBlock:"
- "addAccessControlEntries:toAlbumWithGUID:personID:completionBlock:"
- "addAccessControlEntries:toAlbumWithGUID:personID:info:completionBlock:"
- "addAlbum:"
- "addAlbum:info:"
- "addAlbum:personID:"
- "addAlbum:personID:info:"
- "addAssetCollections:toAlbum:info:"
- "addAssetCollections:toAlbumWithGUID:"
- "addAssetCollections:toAlbumWithGUID:info:"
- "addAssetCollections:toAlbumWithGUID:personID:"
- "addAssetCollections:toAlbumWithGUID:personID:info:"
- "addComment:toAssetCollection:inAlbum:albumURLString:completionBlock:"
- "addComments:toAssetCollection:inAlbum:info:"
- "addComments:toAssetCollectionWithGUID:"
- "addComments:toAssetCollectionWithGUID:info:"
- "addComments:toAssetCollectionWithGUID:personID:"
- "addComments:toAssetCollectionWithGUID:personID:info:"
- "addDelegate:queue:"
- "addEntriesFromDictionary:"
- "addIndex:"
- "addMetadataValue:forKey:"
- "addObject:"
- "addObjectsFromArray:"
- "addObserver:"
- "addObserver:selector:name:object:"
- "addObserverForName:object:queue:usingBlock:"
- "addOperation:"
- "addPendingAssetCollectionChanges:forAlbumGUID:"
- "addPendingAssetCollectionGUID:albumGUID:"
- "addPendingChangesForAlbumGUID:"
- "addPendingPhoneInvitations:toOwnedAlbum:inStateMachin:"
- "addSharingRelationships:toAlbum:completionBlock:"
- "addSharingRelationships:toOwnedAlbum:info:completionBlock:"
- "addTimer:forMode:"
- "albumGUIDs"
- "albumSummaryAlbum:albumURLString:resetSync:completionBlock:"
- "albumWithAlbum:"
- "albumWithGUID:"
- "allHTTPHeaderFields"
- "allHeaderFields"
- "allKeys"
- "allObjectWrappersMaxCount:"
- "allObjectWrappersOrderedByDescendingErrorCountMaxCount:"
- "allObjects"
- "allValues"
- "allocWithZone:"
- "alphanumericCharacterSet"
- "anyObject"
- "appBundleInfoString"
- "appendFormat:"
- "appendObjectWrappers:"
- "appendString:"
- "appleIDHeadersForRequest:"
- "appleIDSession"
- "applyUserDefaultOverridesToResponse:"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "array"
- "arrayWithCapacity:"
- "arrayWithObject:"
- "arrayWithObjects:count:"
- "assertBusyAssertion"
- "assetCollectionGUIDToRequestorContext"
- "assetCollectionGUIDsInAlbumWithGUID:"
- "assetCollectionWithAssetCollection:"
- "assetCollectionWithGUID:"
- "assetCollectionsInAlbumWithGUID:"
- "assetCollectionsInUploadQueue"
- "assetCollectionsInUploadQueueAlbumGUID:"
- "assetCollectionsToItemInFlightMap"
- "assetCollectionsWithAuthorizationError"
- "assetToAssetCollectionMap"
- "assetToItemInFlightMap"
- "assetWithAsset:"
- "assetsInDownloadQueue"
- "assetsInDownloadQueueAlbumGUID:"
- "assetsToGenerateFromImageWithInputSize:toConformToSpecifications:"
- "attributesOfItemAtPath:error:"
- "authTokenForPersonID:"
- "authTokens"
- "autoGenerateItemID"
- "autorelease"
- "backoff"
- "backoffManager"
- "backupDeviceID"
- "backupDeviceUDID"
- "backupDeviceUUID"
- "base64EncodedStringWithOptions:"
- "baseSharingURLForPersonID:"
- "baseURL"
- "baseURLForPersonID:"
- "batchSize"
- "beginTransaction"
- "boolValue"
- "boundStateMachineForPersonID:"
- "bundleForClass:"
- "busyCount"
- "bytes"
- "cStringUsingEncoding:"
- "calloutBlockForCommand:"
- "canBeGroupedWithCommand:"
- "cancel"
- "cancelActivitiesForPersonID:"
- "cancelAllOperations"
- "cancelAssetCollections:"
- "cancelCompletionBlock:"
- "cancelOperationsWithContext:"
- "cancelOutstandingCommandsForAlbumWithGUID:"
- "cancelOutstandingCommandsForAssetCollectionWithGUID:"
- "captionForAssetCollectionWithGUID:"
- "caseInsensitiveCompare:"
- "checkForAlbumSyncedStateChangesInAlbums:info:"
- "checkForAssetCollectionUpdates:inAlbum:info:"
- "checkForChangesIfMissingRootCtag"
- "checkForChangesResetSync:info:"
- "checkForCommentChanges:inAlbumWithGUID:withClientOrgKey:"
- "checkForNewAssetCollections"
- "checkForNewAssetCollectionsIfMissingCtag"
- "checkForOutstandingActivities"
- "checkForUpdatesInAlbums:resetSync:info:"
- "class"
- "clearAllNextActivityDates"
- "clientOrgKeyForRecordID:zoneName:ownerUserID:personID:"
- "collectionWithMasterAsset:fileName:"
- "collectionWithMasterAsset:fileName:derivedAssets:"
- "commandAtHeadOfQueueOutParams:outCommandIdentifier:outPersonID:outAlbumGUID:outAssetCollectionGUID:"
- "commandCount"
- "commandQueue"
- "commandWithMinimumIdentifier:outParams:outCommandIdentifier:outPersonID:outAlbumGUID:outAssetCollectionGUID:"
- "commandwithCommand:variantParam:invariantParam:"
- "commentWithGUID:"
- "commentsForAssetCollectionWithGUID:"
- "commitErrorCountsForObjectWrappers:"
- "commitObjectsWrappers:"
- "compare:"
- "compare:options:"
- "componentsJoinedByString:"
- "componentsSeparatedByCharactersInSet:"
- "componentsSeparatedByString:"
- "computeHashForAsset:"
- "computeHashForAsset:personID:"
- "computeItemIDForAsset:"
- "configManagerForPersonID:"
- "conformsToProtocol:"
- "connection:canAuthenticateAgainstProtectionSpace:"
- "connection:didCancelAuthenticationChallenge:"
- "connection:didFailWithError:"
- "connection:didReceiveAuthenticationChallenge:"
- "connection:willSendRequestForAuthenticationChallenge:"
- "connectionShouldUseCredentialStorage:"
- "containerWithIdentifier:"
- "containsObject:"
- "containsValueForKey:"
- "contentURLForPersonID:"
- "contentsOfDirectoryAtPath:error:"
- "contextWithEngine:type:"
- "continueAddingAssetCollections:skipAssetCollections:toAlbum:info:"
- "copy"
- "copyItemAtPath:toPath:error:"
- "copyParameters"
- "copyTo:"
- "copyWithZone:"
- "countByEnumeratingWithState:objects:count:"
- "countOfEnqueuedCommand:"
- "countOfEnqueuedCommands"
- "createAlbum:completionBlock:"
- "createAlbum:info:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "currentFocusAlbumGUID"
- "currentFocusAssetCollectionGUID"
- "currentHandler"
- "currentOwnerCKUserID"
- "currentRunLoop"
- "currentThread"
- "d"
- "d16@0:8"
- "d32@0:8{CGSize=dd}16"
- "d40@0:8@16@24d32"
- "daemon"
- "daemonModel"
- "data"
- "dataTaskWithRequest:completionHandler:"
- "dataUsingEncoding:"
- "dataWithBytes:length:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "dataWithContentsOfFile:"
- "dataWithPropertyList:format:options:error:"
- "date"
- "dateFromString:"
- "dateWithTimeIntervalSince1970:"
- "dateWithTimeIntervalSinceNow:"
- "dateWithTimeIntervalSinceReferenceDate:"
- "db"
- "dbQueue"
- "dbQueueAccessControlGUIDsForAlbumWithGUID:"
- "dbQueueAccessControlWithGUID:outObject:outAlbumGUID:outEmail:outUserInfoData:"
- "dbQueueAccessControlsForAlbumWithGUID:"
- "dbQueueAddCommentCheckOperation:"
- "dbQueueAlbumGUIDs"
- "dbQueueAlbumMetadataWithAlbumGUID:key:outValue:"
- "dbQueueAlbumWithGUID:outObject:outName:outCtag:outForeignCtag:outURLString:outUserInfoData:outClientOrgKey:"
- "dbQueueAssetCollectionContainsCommentsFromMeAssetCollectionGUID:"
- "dbQueueAssetCollectionGUIDsInAlbumWithGUID:"
- "dbQueueAssetCollectionMetadataWithAssetCollectionGUID:key:outValue:"
- "dbQueueAssetCollectionWithGUID:outObject:outCtag:outAlbumGUID:outBatchDate:outPhotoDate:outPhotoNumber:outUserInfoData:"
- "dbQueueAssetCountAlbumGUID:inQueue:"
- "dbQueueBeginTransaction"
- "dbQueueCheckToClearUnviewedStateOnAlbumWithGUID:info:"
- "dbQueueCheckToClearUnviewedStateOnAssetCollectionWithGUID:info:"
- "dbQueueCommentWithGUID:outObject:outID:outTimestamp:outAssetCollectionGUID:outIsCaption:outUserInfoData:"
- "dbQueueCommentWithID:assetCollectionGUID:outObject:outGUID:outTimestamp:outIsCaption:outUserInfoData:"
- "dbQueueCommentsForAssetCollectionWithGUID:"
- "dbQueueCountOfUnviewedAssetCollectionsInAlbumWithGUID:"
- "dbQueueDB"
- "dbQueueDeleteAccessControlWithGUID:info:"
- "dbQueueDeleteAlbumMetadataAlbumGUID:key:info:"
- "dbQueueDeleteAlbumWithGUID:info:"
- "dbQueueDeleteAllAlbumMetadataForAlbumWithGUID:info:"
- "dbQueueDeleteAllAssetCollectionMetadataForAssetCollectionWithGUID:info:"
- "dbQueueDeleteAllPendingCommentCheckOperations"
- "dbQueueDeleteAssetCollectionMetadataAssetCollectionGUID:key:info:"
- "dbQueueDeleteAssetCollectionWithGUID:info:"
- "dbQueueDeleteCommentWithGUID:info:"
- "dbQueueDeleteInvitationForAlbumWithGUID:info:"
- "dbQueueDeleteInvitationWithGUID:info:"
- "dbQueueDeletePersistentValueWithKey:"
- "dbQueueDiscardOperation:itemGUID:"
- "dbQueueEndTransaction"
- "dbQueueEnqueueCommand:params:personID:albumGUID:assetCollectionGUID:"
- "dbQueueEnqueueCommand:params:personID:albumGUID:assetCollectionGUID:sequenceNumber:"
- "dbQueueFlushAllPendingCommentCheckOperations"
- "dbQueueInitializeDatabasePath:currentVersion:"
- "dbQueueInvitationForAlbumWithGUID:"
- "dbQueueInvitationWithAlbumGUID:outObject:outInvitationGUID:outEmail:outUserInfoData:"
- "dbQueueInvitationWithGUID:outObject:outAlbumGUID:outEmail:outUserInfoData:"
- "dbQueueIsAssetCollectionWithGUIDPending:"
- "dbQueueIsGUIDQueued:inQueue:"
- "dbQueueLookupOrCreateAlbumWithGUID:"
- "dbQueueLookupOrCreateAssetCollectionWithGUID:outAlbum:"
- "dbQueueLookupOrCreateCommentWithGUID:outAssetCollection:outAlbum:"
- "dbQueueMaximumCommentIDForAssetCollectionWithGUID:"
- "dbQueueMaximumPhotoNumberForAlbumWithGUID:"
- "dbQueueNextCommandSequenceNumber"
- "dbQueuePendingCommentCheckOperations"
- "dbQueuePersistentDataForKey:"
- "dbQueuePersistentObjectForKey:"
- "dbQueuePersistentStringForKey:"
- "dbQueueRemoveAllEntriesFromTable:"
- "dbQueueRemoveCommandAtHeadOfQueue"
- "dbQueueRemoveCommandIdentifier:"
- "dbQueueRemoveGUID:fromQueue:"
- "dbQueueRequeuePendingCommandsWithAlbumGUID:"
- "dbQueueRequeuePendingCommandsWithAssetCollectionGUID:"
- "dbQueueRequeuePendingCommandsWithQueryStatement:deleteStatement:"
- "dbQueueRollbackTransaction"
- "dbQueueSetAccessControl:info:"
- "dbQueueSetAlbum:info:"
- "dbQueueSetAlbumMetadataAlbumGUID:key:value:info:"
- "dbQueueSetAssetCollection:inAlbumWithGUID:info:"
- "dbQueueSetAssetCollectionMetadataAssetCollectionGUID:key:value:info:"
- "dbQueueSetComment:forAssetCollectionWithGUID:info:"
- "dbQueueSetErrorCount:forGUID:inQueue:"
- "dbQueueSetInvitation:info:"
- "dbQueueSetPersistentData:forKey:"
- "dbQueueSetPersistentObject:forKey:"
- "dbQueueSetPersistentString:forKey:"
- "dbQueueSetUnviewedState:onAlbumWithGUID:info:"
- "dbQueueSetUnviewedState:onAssetCollectionWithGUID:info:"
- "dbQueueSmallestCommandSequenceNumber"
- "dbQueueUnviewedAlbumCount"
- "dbQueueUnviewedAssetCollectionCountForAlbumWithGUID:"
- "dbQueueUpdateAlbumCtag:"
- "dbQueueUpgradeFromDatabaseVersion:currentVersion:"
- "dbWasRecreated"
- "deactivate"
- "deactivateRemoveAllFiles:"
- "dealloc"
- "deassertBusyAssertion"
- "debugDescription"
- "decodeBoolForKey:"
- "decodeDoubleForKey:"
- "decodeInt64ForKey:"
- "decodeIntForKey:"
- "decodeIntegerForKey:"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "decodePropertyListForKey:"
- "defaultCenter"
- "defaultManager"
- "defaultModel"
- "defaultSessionConfiguration"
- "delegate"
- "delegatePluginForPersonID:"
- "deleteAlbum:completionBlock:"
- "deleteAlbum:info:"
- "deleteAlbumWithGUID:"
- "deleteAlbumWithGUID:info:"
- "deleteAlbumWithGUID:inviterAddress:"
- "deleteAlbumWithGUID:personID:"
- "deleteAlbumWithGUID:personID:info:"
- "deleteAssetCollectionWithGUID:"
- "deleteAssetCollectionWithGUID:info:"
- "deleteAssetCollectionWithGUID:personID:"
- "deleteAssetCollectionWithGUID:personID:info:"
- "deleteAssetCollections:"
- "deleteAssetCollections:forPersonID:"
- "deleteAssetCollections:inAlbum:completionBlock:"
- "deleteAssetCollections:inAlbum:info:"
- "deleteAssetCollectionsWithGUIDs:"
- "deleteAssetCollectionsWithGUIDs:personID:"
- "deleteComment:fromAssetCollection:inAlbum:albumURLString:completionBlock:"
- "deleteCommentWithGUID:"
- "deleteCommentWithGUID:info:"
- "deleteCommentWithGUID:personID:"
- "deleteCommentWithGUID:personID:info:"
- "deleteComments:inAssetCollection:inAlbum:info:"
- "deletePersistentValueWithKey:"
- "deletePluginClass"
- "deleteProtocol:didFinishSuccessfulCollections:failedCollections:error:"
- "deleteProtocol:didReceiveAuthenticationError:"
- "deleteURL"
- "deleter:didFinishDeletingAssetCollection:error:"
- "deleterForPersonID:"
- "deleterPluginForPersonID:"
- "deleterWillAssignPluginAsDelegateOfDeleter:"
- "deletionIndex"
- "dequeueAssetCollectionWithGUIDs:outError:"
- "dequeueAssetCollectionWithGUIDs:personID:outError:"
- "derivativeImageScalingSpecification"
- "derivativeSpecifications"
- "description"
- "deviceInfoDict"
- "deviceInfoDictForPersonID:"
- "dictionary"
- "dictionaryRepresentation"
- "dictionaryWithCapacity:"
- "dictionaryWithContentsOfFile:"
- "dictionaryWithContentsOfURL:"
- "dictionaryWithObject:forKey:"
- "dictionaryWithObjects:forKeys:count:"
- "dictionaryWithObjectsAndKeys:"
- "didCreateStateMachineForPersonID:"
- "didDestroyStateMachineForPersonID:"
- "didDetectUnrecoverableCondition"
- "didEncounterNetworkConditionError"
- "didEnqueueAsset:forAlbumGUID:"
- "didExceedPublishQuotaForPersonID:retryDate:"
- "didFindDeletedAlbumWithGUID:inviterAddress:"
- "didFindNewAlbum:"
- "didFinishGettingAllAssets"
- "didFinishPuttingAllAssets"
- "didFinishUsingAssets:"
- "didIdle"
- "didReceiveAuthFailureForPersonID:"
- "didReceiveAuthSuccessForPersonID:"
- "didReceiveAuthenticationFailureForPersonID:"
- "didReceiveAuthenticationSuccessForPersonID:"
- "didReceiveCommentTooLongError:forAssetCollection:inAlbum:personID:"
- "didReceiveGlobalResetSyncForPersonID:"
- "didReceiveNewServerSideConfigurationForPersonID:"
- "didReceiveNewShareState:oldShareState:forPersonID:"
- "didReceivePushNotificationForPersonID:"
- "didReceiveRetryAfterDate:"
- "didReceiveServerSideConfigurationVersion:forPersonID:"
- "didReceiveTooManyAlbumsError:personID:"
- "didReceiveTooManyCommentsError:forAssetCollection:inAlbum:personID:"
- "didReceiveTooManyPhotosError:forAlbum:personID:"
- "didReceiveTooManySubscriptionsError:personID:"
- "didUnidle"
- "disable"
- "discardOperation:itemGUID:"
- "distantFuture"
- "distantPast"
- "domain"
- "doubleValue"
- "doubleValueForParameter:forPersonID:defaultValue:"
- "downloadBatchPerfGUID"
- "earlierDate:"
- "earliestNextActivityDate"
- "earliestUnviewedAssetCollectionGUIDInAlbumWithGUID:"
- "emailForPersonID:"
- "enable"
- "encodeBool:forKey:"
- "encodeDouble:forKey:"
- "encodeInt64:forKey:"
- "encodeInt:forKey:"
- "encodeInteger:forKey:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encryptedValues"
- "endTransaction"
- "engine"
- "enqueueAssetCollection:personID:outError:"
- "enqueueAssetCollectionForUpload:album:"
- "enqueueAssetCollections:outError:"
- "enqueueAssetForDownload:inAlbumWithGUID:"
- "enqueueCommand:"
- "enqueueCommand:params:personID:albumGUID:assetCollectionGUID:"
- "enqueueCommand:params:personID:albumGUID:pendingOnAssetCollectionGUID:"
- "enqueueCommandAtHeadOfQueue:params:personID:albumGUID:assetCollectionGUID:"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "enumeratorWithDatabase:query:stepBlock:"
- "errorFromStandardProcessingOnResponse:responseObject:checkServerSideConfigVersion:error:body:"
- "errorIsCancellation:"
- "errorWithDomain:code:userInfo:"
- "eventQueue"
- "eventQueueNotifyObserversOfUpdatedUnviewedCountInAlbum:unviewedCount:info:"
- "eventQueuePerformBlockOnObservers:"
- "exceptionWithName:reason:userInfo:"
- "existingConfigManagerForPersonID:"
- "existingDeleterForPersonID:"
- "existingModelForPersonID:"
- "existingPublisherForPersonID:"
- "existingStateMachineForPersonID:"
- "existingSubscriberForPersonID:"
- "fetchClientOrgKeyForRecordID:zoneName:fieldName:ownerUserID:isOwned:completionHandler:"
- "fetchCurrentDeviceIDWithCompletionHandler:"
- "fetchMPSStateWithBaseAvailabilityURL:personID:originalLibrarySize:completionBlock:"
- "fetchMigrationCtag"
- "fileExistsAtPath:"
- "fileExistsAtPath:isDirectory:"
- "fileSystemRepresentation"
- "fileURLWithPath:"
- "finishedAssetCollections"
- "finishedAssets"
- "firstNameForPersonID:"
- "firstObject"
- "floatValue"
- "flushAllPendingCommentCheckOperations"
- "flushQueue"
- "flushQueueCompletionBlock:"
- "forget"
- "forgetEverything"
- "forgetEverythingAboutPersonID:"
- "forgetEverythingAboutPersonID:completionBlock:"
- "forgetEverythingCompletionBlock:"
- "forgetEverythingInfo:"
- "forgetEverythingInfo:completionBlock:"
- "forgetPersonID:"
- "fullNameForPersonID:"
- "gate"
- "getAccessControlsForAlbums:info:"
- "getAlbumSyncedStateForAlbum:assetCollectionStateBlock:completionBlock:"
- "getAlbumURLForAlbumWithGUID:completionBlock:"
- "getAssetCollections:inAlbum:albumURLString:completionBlock:"
- "getAssets:requestURL:DSID:options:"
- "getBytes:range:"
- "getCFRunLoop"
- "getChangesRootCtag:migrationCtag:completionBlock:"
- "getCharacters:range:"
- "getCommentChanges:inAlbumWithGUID:withClientOrgKey:albumURLString:completionBlock:"
- "getServerSideConfigCompletionBlock:"
- "getSharingInfoForAlbum:albumURLString:completionBlock:"
- "getTokensForAssets:inAlbum:albumURLString:completionBlock:"
- "getURL"
- "getUploadTokens:forAssetCollectionWithGUID:inAlbumWithGUID:albumURLString:completionBlock:"
- "getVideoURL:forAssetCollectionWithGUID:inAlbumWithGUID:albumURLString:withClientOrgKey:completionBlock:"
- "handleFailureInFunction:file:lineNumber:description:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "handleResponse:forRequest:shouldRetry:"
- "handleWithEmailAddress:"
- "hardlinkOrCopyFileFromPath:toPath:outError:"
- "hardwareString"
- "hasBackupDeviceID"
- "hasBackupDeviceUDID"
- "hasBackupDeviceUUID"
- "hasCommandsInGroupedCommandQueue"
- "hasComments"
- "hasDeactivated"
- "hasEnqueuedActivities"
- "hasEnqueuedItems"
- "hasError"
- "hasICPLDeviceID"
- "hasIcplAction"
- "hasItemsForDownloadCountFocusAlbumGUID:focusAssetCollectionGUID:"
- "hasMPSDeviceID"
- "hasMpsAction"
- "hasOriginalLibrarySize"
- "hasOutstandingActivity"
- "hasPendingChanges"
- "hasRetryAfterSeconds"
- "hasShutDown"
- "hasVersion"
- "hasVideoAsset"
- "hash"
- "headerVersion"
- "hysteresisTimer"
- "i16@0:8"
- "i24@0:8@\"NSString\"16"
- "i24@0:8@16"
- "i24@0:8Q16"
- "i24@0:8^@16"
- "i32@0:8@\"<MSPublishStorageProtocol>\"16@\"MSAsset\"24"
- "i32@0:8@16@24"
- "i36@0:8@16@24i32"
- "icplActionAsString:"
- "idleCountQueue"
- "idleTimerGate"
- "idsService"
- "indexOfObject:inWrapperArray:"
- "indexSet"
- "infoDictionary"
- "init"
- "initWithBytes:length:encoding:"
- "initWithBytesNoCopy:length:encoding:freeWhenDone:"
- "initWithBytesNoCopy:length:freeWhenDone:"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithCommand:variantParam:invariantParam:"
- "initWithContainerID:options:"
- "initWithContainerIdentifier:environment:"
- "initWithContentsOfFile:"
- "initWithContentsOfFile:options:error:"
- "initWithData:"
- "initWithData:encoding:"
- "initWithDatabase:query:stepBlock:"
- "initWithDictionary:"
- "initWithEngine:type:"
- "initWithFileDescriptor:closeOnDealloc:"
- "initWithFileName:path:"
- "initWithFormat:"
- "initWithFormat:arguments:"
- "initWithGUID:"
- "initWithIdentifier:"
- "initWithInitialInterval:backoffFactor:randomizeFactor:maxBackoffInterval:retryAfterDate:"
- "initWithLocaleIdentifier:"
- "initWithMasterAsset:fileName:derivedAssets:"
- "initWithObject:size:"
- "initWithObjects:"
- "initWithObjectsAndKeys:"
- "initWithPath:"
- "initWithPersonID:"
- "initWithPersonID:baseURL:"
- "initWithPersonID:databasePath:"
- "initWithPersonID:databasePath:currentVersion:"
- "initWithPersonID:databasePath:eventQueue:"
- "initWithPersonID:eventQueue:"
- "initWithPersonID:path:"
- "initWithRecordIDs:"
- "initWithRecordName:zoneID:"
- "initWithScheme:host:path:"
- "initWithService:"
- "initWithStreamID:"
- "initWithString:"
- "initWithString:relativeToURL:"
- "initWithSyncedKeyValueChangesForAlbumGUIDS:albumChanges:accessControlChangesForAlbumGUIDS:"
- "initWithTarget:selector:object:"
- "initWithTimeIntervalSinceNow:"
- "initWithUnsignedLongLong:"
- "initWithWorkPath:appIDHeader:dataClass:options:"
- "initWithWorkPath:appIDHeader:dataClass:options:modes:"
- "initWithZoneName:ownerName:"
- "intValue"
- "intValueForParameter:forPersonID:defaultValue:"
- "integerForKey:"
- "integerValue"
- "invalidate"
- "invariantParam"
- "invertedSet"
- "invitation"
- "invitationForAlbumWithGUID:"
- "invitationGUIDs"
- "invitationWithGUID:"
- "isActive"
- "isAlbumWithGUIDMarkedAsUnviewed:"
- "isAssertingBusyAssertion"
- "isAssetCollectionWithGUIDMarkedAsUnviewed:"
- "isAssetCollectionWithGUIDPending:"
- "isAutoloopVideo"
- "isBusy"
- "isDone"
- "isDownloadingThumbnails"
- "isEqual:"
- "isEqualToData:"
- "isEqualToDate:"
- "isEqualToDictionary:"
- "isEqualToSharingRelationship:"
- "isEqualToString:"
- "isFamilySharedAlbum"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isMetricsGatheringEnabled"
- "isPerformanceLoggingEnabled"
- "isPhoto"
- "isPhotoIris"
- "isProxy"
- "isPublicAccessEnabledForAlbumWithGUID:"
- "isRetryingOutstandingActivities"
- "isShuttingDown"
- "isSubclassOfClass:"
- "isVideo"
- "isWaitingForAuth"
- "isWaitingForFirstDownloadEvent"
- "itemFlags"
- "itemIDs"
- "itemsForDownloadCountFocusAlbumGUID:focusAssetCollectionGUID:"
- "itemsForUpload"
- "itemsInFlight"
- "keyEnumerator"
- "lastEnqueuedCommand"
- "lastNameForPersonID:"
- "lastObject"
- "lastViewedCommentDateForAssetCollectionWithGUID:"
- "latestNextActivityDate"
- "length"
- "localizedDescription"
- "localizedRecoverySuggestion"
- "localizedStringForKey:value:table:"
- "logFacility:level:format:args:"
- "logFile:func:line:facility:level:format:args:"
- "logLevel:personID:albumGUID:format:"
- "logStringForGetItemState:"
- "logStringForPutItemState:"
- "longLongValue"
- "longLongValueForParameter:forPersonID:defaultValue:"
- "longValue"
- "longValueForParameter:forPersonID:defaultValue:"
- "mPSDeviceID"
- "mainQueue"
- "mainThread"
- "mapQueue"
- "mapQueueShutDownStateMachineInMap:personIDs:index:forDestruction:completionBlock:"
- "markAlbumGUIDAsViewed:"
- "markAlbumGUIDAsViewed:info:"
- "markAlbumGUIDAsViewed:moveLastViewedAssetCollectionMarker:info:"
- "markAlbumGUIDAsViewed:personID:"
- "markAlbumGUIDAsViewed:personID:info:"
- "markAlbumGUIDAsViewed:personID:moveLastViewedAssetCollectionMarker:info:"
- "markAsSpamAlbumWithGUID:info:"
- "markAsSpamAlbumWithGUID:personID:"
- "markAsSpamInvitationForAlbum:completionBlock:"
- "markAsSpamInvitationForAlbum:invitationGUID:info:"
- "markAsSpamInvitationForToken:completionBlock:"
- "markAsSpamInvitationForToken:info:"
- "markAsSpamInvitationWithGUID:info:"
- "markAsSpamInvitationWithGUID:personID:"
- "markAsSpamInvitationWithToken:info:"
- "markAsSpamInvitationWithToken:personID:"
- "markCommentsForAssetCollectionWithGUID:asViewedWithLastViewedDate:"
- "markCommentsForAssetCollectionWithGUID:asViewedWithLastViewedDate:info:"
- "markCommentsForAssetCollectionWithGUID:asViewedWithLastViewedDate:personID:"
- "markCommentsForAssetCollectionWithGUID:asViewedWithLastViewedDate:personID:info:"
- "maxBatchCount"
- "maxGroupedCallbackEventBatchCount"
- "maxGroupedCallbackEventIdleInterval"
- "maxGroupedCallbackEventStaleness"
- "maxMMCSTokenValidityTimeInterval"
- "maxMetadataRetryCount"
- "maxRetryCount"
- "maximumLongSideLength"
- "mayDownloadPersonID:"
- "mediaStreamDaemonDidIdle:"
- "mediaStreamDaemonDidUnidle:"
- "memberQueue"
- "memberQueueIsAssertingBusyAssertion"
- "memberQueueMetadataBackoffManager"
- "memberQueueSetIsAssertingBusyAssertion:"
- "mergeFrom:"
- "metadataBackoffManagerParameters"
- "metadataValueForKey:"
- "migrationCtagToCheckForChanges"
- "minimumLongSideLength"
- "model"
- "modelForPersonID:"
- "modifyAlbumMetadata:"
- "modifyAlbumMetadata:info:"
- "modifyAlbumMetadata:personID:"
- "modifyAlbumMetadata:personID:info:"
- "mpsActionAsString:"
- "mutableCopy"
- "nextActivityDateForPersonID:"
- "nextCommandGroupMaxCount:outCommand:outLastCommandIndex:"
- "nextItemsForDownloadFocusAlbumGUID:focusAssetCollectionGUID:maxCount:"
- "nextItemsForDownloadFocusAlbumGUID:focusAssetCollectionGUID:thumbnails:maxCount:isInflight:"
- "nextItemsForUploadAlbumGUID:maxPriority:maxCount:"
- "nextItemsForUploadMaxCount:"
- "nextObject"
- "nextUpdateDateByPersonID"
- "nominalShortSideLength"
- "nukeCompletionBlock:"
- "null"
- "numberWithBool:"
- "numberWithDouble:"
- "numberWithFloat:"
- "numberWithInt:"
- "numberWithInteger:"
- "numberWithLongLong:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLong:"
- "numberWithUnsignedLongLong:"
- "object"
- "objectAtIndex:"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKey:forPersonID:defaultValue:"
- "objectForKeyedSubscript:"
- "objectGUID"
- "objectWrappersWithZeroSizeMaxCount:"
- "objectsFromWrappers:"
- "objectsFromWrappers:equalToObject:"
- "observers"
- "originalLibrarySize"
- "ownSubscribedStream"
- "ownSubscribedStreamForPersonID:"
- "pathAlbumSharingDir"
- "pathExtension"
- "pathForPersonInfoDictionary"
- "pathMediaStreamDir"
- "pendingAlbumChanges"
- "pendingAlbumGUIDToAssetCollections"
- "pendingAlbumGUIDsWithKeyValueChanges"
- "pendingAlbumGUIDsWithSharingInfoChanges"
- "pendingChanges"
- "pendingConnectionsGroup"
- "pendingConnectionsQueue"
- "performBlock:"
- "performBlockOnObservers:"
- "performBlockOnWorkThread:"
- "performBlockOnWorkThread:waitUntilDone:"
- "performOutstandingActivities"
- "performSelector:"
- "performSelector:onThread:withObject:waitUntilDone:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performSelectorOnMainThread:withObject:waitUntilDone:"
- "persistentObjectForKey:"
- "persistentObjectForKey:personID:"
- "persistentStringForKey:"
- "personIDEnabledForAlbumSharing:"
- "personIDForPollingTriggeredByPushNotification"
- "personIDHasOutstandingPublications:"
- "personIDListeningToPushNotification"
- "personIDToDelegateMap"
- "personIDToPersonInfoDictionary"
- "personIDToStateMachineMap"
- "personIDsEnabledForAlbumSharing"
- "personIDsWithOutstandingActivities"
- "phoneInvitations"
- "pluginClass"
- "policyMayDownload"
- "policyMaySendDelete"
- "policyMayUpload"
- "pollForSubscriptionUpdatesForPersonID:"
- "pollForSubscriptionUpdatesTriggeredByPushNotificationForPersonID:"
- "pollForSubscriptionUpdatesWithAccountAnchors:"
- "position"
- "postCommandCompletionBlock"
- "postNotificationName:object:"
- "postNotificationName:object:userInfo:"
- "preferredFilenameExtension"
- "privateCloudDatabase"
- "propertyListWithData:options:format:error:"
- "protocol:didReceiveRetryAfterDate:"
- "publish"
- "publishAssets:URL:"
- "publishBatchSize"
- "publishStorageProtocol:didFinishUploadingAsset:error:"
- "publishStorageProtocol:didFinishUsingFD:forAsset:"
- "publishStorageProtocol:didRequestFDForAsset:"
- "publishStorageProtocolDidFinishPublishingAllAssets:"
- "publishStreamsProtocol:didFinishSendingUploadCompleteError:"
- "publishStreamsProtocol:didFinishUploadingMetadataResponse:error:"
- "publishStreamsProtocol:didReceiveAuthenticationError:"
- "publishTargetByteCount"
- "publisher:didEncounterError:publishingAssetCollections:"
- "publisher:didFinishPublishingAssetCollections:"
- "publisher:didRequestCloseFileDescriptor:forAsset:"
- "publisher:didRequestOpenFileDescriptorForAsset:"
- "publisher:didRequestSubmissionOfAssetCollections:"
- "publisher:willPublishAssetCollections:"
- "publisherForPersonID:"
- "publisherPluginClass"
- "publisherPluginForPersonID:"
- "publisherWillAssignPluginAsDelegateOfPublisher:"
- "publisherWillDeassignPluginAsDelegateOfPublisher:"
- "purgeCompletionBlock:"
- "purgeEverythingCompletionBlock:"
- "pushTokenForPersonID:"
- "putAssetCollections:intoAlbum:albumURLString:completionBlock:"
- "putAssets:requestURL:DSID:options:"
- "putURL"
- "q"
- "q16@0:8"
- "q24@0:8@16"
- "q32@0:8@16@24"
- "q40@0:8@16@24q32"
- "queryConfiguration"
- "queue"
- "r^*"
- "raise"
- "raise:format:"
- "readFrom:"
- "reauthorizationProtocol:didReceiveAuthenticationError:"
- "reauthorizationProtocol:reauthorizedAssets:rejectedAssets:error:"
- "reauthorizeURL"
- "recordName"
- "recordType"
- "redactedDescription"
- "reenqueueQuarantinedActivitiesWithReason:"
- "reenqueueQuarantinedAssetCollections"
- "refreshAccessControlListForAlbumWithGUID:"
- "refreshAccessControlListForAlbumWithGUID:info:"
- "refreshAccessControlListOfAlbumWithGUID:personID:"
- "refreshAccessControlListOfAlbumWithGUID:personID:info:"
- "refreshCommentsForAssetCollectionWithGUID:resetSync:"
- "refreshCommentsForAssetCollectionWithGUID:resetSync:info:"
- "refreshCommentsForAssetCollectionWithGUID:resetSync:personID:"
- "refreshCommentsForAssetCollectionWithGUID:resetSync:personID:info:"
- "refreshConfiguration"
- "refreshContentOfAlbumWithGUID:resetSync:"
- "refreshContentOfAlbumWithGUID:resetSync:info:"
- "refreshContentOfAlbumWithGUID:resetSync:personID:"
- "refreshContentOfAlbumWithGUID:resetSync:personID:info:"
- "refreshResetSync:"
- "refreshResetSync:info:"
- "refreshResetSync:personID:"
- "refreshResetSync:personID:info:"
- "refreshServerSideConfig"
- "refreshServerSideConfigurationForPersonID:"
- "registerAssetCollections:completionBlock:"
- "registerAssetForUpload:completionBlock:"
- "registerAssets:completionBlock:"
- "registerAssets:forDownloadCompletionBlock:"
- "rejectInvitationWithGUID:"
- "rejectInvitationWithGUID:info:"
- "rejectInvitationWithGUID:personID:"
- "rejectInvitationWithGUID:personID:info:"
- "release"
- "releaseBusy"
- "releasePowerAssertion"
- "releaseUIBusy"
- "removeAccessControlEntryWithGUID:"
- "removeAccessControlEntryWithGUID:info:"
- "removeAccessControlEntryWithGUID:personID:"
- "removeAccessControlEntryWithGUID:personID:info:"
- "removeAllObjects"
- "removeAssetCollectionsFromUploadQueue:"
- "removeAssetsFromDownloadQueue:"
- "removeCommandIdentifier:"
- "removeCommandsUpToCommandIndex:"
- "removeItemAtPath:error:"
- "removeObject:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "removeObjectWrappersFromQueue:"
- "removeObjectsAtIndexes:"
- "removeObjectsInArray:"
- "removeObserver:"
- "removePendingAssetCollection:forAlbumGUID:"
- "removePendingChangesForAlbumGUID:"
- "removePendingKeyValueChangesForAlbumGUID:"
- "removePendingSharingInfoChangesForAlbumGUID:"
- "removeSharingRelationships:forAlbum:"
- "removeSharingRelationships:fromAlbum:completionBlock:"
- "removeSharingRelationships:fromOwnedAlbum:info:"
- "reputationForHandle:timeout:error:"
- "requestReauthorizationForAssets:"
- "requestWithURL:"
- "requeuePendingAssetCollectionGUID:"
- "requeuePendingAssetCollectionsWithAlbumGUID:"
- "reregisterAssetForDownload:"
- "reregisterAssetForUpload:"
- "resetServer"
- "resetServerObjectWithPersonID:baseURL:"
- "resetServerProtocol:didFinishWithError:"
- "resetServerProtocol:didReceiveAuthenticationError:"
- "resetServerState"
- "resetSubscriberSyncForPersonID:"
- "resetURL"
- "respondsToSelector:"
- "responseDict:containsLimitErrorCode:outMaxAllowed:"
- "resume"
- "retain"
- "retainBusy"
- "retainCount"
- "retainPowerAssertion"
- "retainUIBusy"
- "retrievalBatchSize"
- "retrieveAssets:"
- "retrieveAssets:inAlbumWithGUID:"
- "retrieveAssets:inAlbumWithGUID:personID:"
- "retrieveAssetsFromAssetCollectionsWithGUIDs:assetTypeFlags:"
- "retrieveAssetsInAssetCollectionsWithGUIDs:assetTypeFlags:personID:"
- "retryAfterDateBasedOnRetryAfterHeaderString:"
- "retryOutstandingActivitiesForPersonID:"
- "rootCtagToCheckForChanges"
- "runMode:beforeDate:"
- "scaleFactorForInputSize:"
- "scheduleEvent:assetCollectionGUID:albumGUID:info:"
- "scheme"
- "score"
- "self"
- "sendAsynchronousRequest:queue:completionHandler:"
- "sendDeletionRequestForAssetCollections:"
- "sendMessage:fromAccount:toDestinations:priority:options:identifier:error:"
- "sendMessageIdentifierToPhone"
- "sendMetadataForAssetCollections:"
- "sendServerSideConfigurationDidChangeNotificationForPersonID:"
- "sendURLRequest:bodyObj:completionBlock:"
- "sendURLRequest:method:bodyObj:checkServerSideConfigVersion:completionBlock:"
- "sendUploadCompleteForAssetCollections:"
- "sendUploadCompleteSuccessfulAssetCollections:failedAssetCollections:album:completionBlock:"
- "serverCommunicationBackoffDate"
- "serverSideConfigProtocol:didFinishWithConfiguration:error:"
- "serverSideConfigProtocol:didReceiveAuthenticationError:"
- "serverSideConfigQueue"
- "serverSideConfiguration"
- "serverSideConfigurationForPersonID:"
- "serverSideConfigurationVersion"
- "serverSideQueueServerSideConfiguration"
- "serverSideQueueSetServerSideConfiguration:"
- "service:account:didReceiveLocalNetworkHandshake:fromID:context:"
- "service:account:identifier:didSendWithSuccess:error:"
- "service:account:identifier:didSendWithSuccess:error:context:"
- "service:account:identifier:fromID:hasBeenDeliveredWithContext:"
- "service:account:identifier:hasBeenDeliveredWithContext:"
- "service:account:identifier:sentBytes:totalBytes:"
- "service:account:incomingData:fromID:context:"
- "service:account:incomingMessage:fromID:context:"
- "service:account:incomingOpportunisticData:withIdentifier:fromID:context:"
- "service:account:incomingPendingMessageOfType:fromID:context:"
- "service:account:incomingResourceAtURL:fromID:context:"
- "service:account:incomingResourceAtURL:metadata:fromID:context:"
- "service:account:incomingUnhandledProtobuf:fromID:context:"
- "service:account:inviteDroppedForSessionID:fromID:context:error:"
- "service:account:inviteReceivedForSession:fromID:"
- "service:account:inviteReceivedForSession:fromID:withContext:"
- "service:account:inviteReceivedForSession:fromID:withOptions:"
- "service:account:pendingResourceWithMetadata:fromID:acknowledgementBlock:context:"
- "service:account:receivedGroupSessionParticipantDataUpdate:"
- "service:account:receivedGroupSessionParticipantUpdate:"
- "service:account:receivedGroupSessionParticipantUpdate:context:"
- "service:activeAccountsChanged:"
- "service:connectedDevicesChanged:"
- "service:devicesChanged:"
- "service:didCancelMessageWithSuccess:error:identifier:"
- "service:didSendOpportunisticDataWithIdentifier:toIDs:"
- "service:didSwitchActivePairedDevice:acknowledgementBlock:"
- "service:linkedDevicesChanged:"
- "service:nearbyDevicesChanged:"
- "serviceAllowedTrafficClassifiersDidReset:"
- "serviceSpaceDidBecomeAvailable:"
- "sessionWithConfiguration:"
- "set"
- "setAlbum:"
- "setAlbumGUID:"
- "setAlbumSyncedState:forAlbum:albumStateCtag:completionBlock:"
- "setAlbumSyncedState:forAlbum:info:"
- "setAllHTTPHeaderFields:"
- "setApplicationBundleIdentifierOverrideForContainerAccess:"
- "setApplicationBundleIdentifierOverrideForNetworkAttribution:"
- "setApplicationBundleIdentifierOverrideForPushTopicGeneration:"
- "setAsset:"
- "setAssetCollectionGUID:"
- "setAssetCollectionGUIDToRequestorContext:"
- "setAssetCollectionID:"
- "setAssetCollectionSyncedState:forAssetCollection:album:info:"
- "setAssetCollectionSyncedState:forAssetCollection:inAlbum:assetCollectionStateCtag:completionBlock:"
- "setAssetCollectionsToItemInFlightMap:"
- "setAssetCollectionsWithAuthorizationError:"
- "setAssetDataAvailableOnServer:"
- "setAssetToAssetCollectionMap:"
- "setAssetToItemInFlightMap:"
- "setAssetTypeFlags:"
- "setAssets:"
- "setAuthTokens:"
- "setAutoGenerateItemID:"
- "setBackoffFactor:"
- "setBackoffManager:"
- "setBackupDeviceID:"
- "setBackupDeviceUDID:"
- "setBackupDeviceUUID:"
- "setBaseURL:"
- "setBatchCreationDate:"
- "setBatchSize:"
- "setBusyCount:"
- "setClientOrgKey:"
- "setClientOrgKey:forAlbumWithGUID:"
- "setClientOrgKey:forAlbumWithGUID:info:"
- "setClientOrgKey:forAlbumWithGUID:personID:"
- "setClientOrgKey:forAlbumWithGUID:personID:info:"
- "setClientTimestamp:"
- "setCommand:"
- "setCommandQueue:"
- "setComment:"
- "setConfig:"
- "setConfiguration:"
- "setContainer:"
- "setContent:"
- "setContext:"
- "setCount:"
- "setCtag:"
- "setCurrentFocusAlbumGUID:"
- "setCurrentFocusAssetCollectionGUID:"
- "setCurrentInterval:"
- "setDaemon:"
- "setDaemonModel:"
- "setDateFormat:"
- "setDb:"
- "setDbWasRecreated:"
- "setDelegate:"
- "setDeletionIndex:"
- "setDerivedAssets:"
- "setDesiredKeys:"
- "setDidEncounterNetworkConditionError:"
- "setDownloadBatchPerfGUID:"
- "setEmail:"
- "setEmails:"
- "setEnabled:"
- "setEngine:"
- "setError:"
- "setErrorCount:"
- "setErrorCount:forAssetCollectionInUploadQueue:"
- "setErrorCount:forAssetInDownloadQueue:"
- "setEventQueue:"
- "setFetchRecordsCompletionBlock:"
- "setFileData:"
- "setFileHash:"
- "setFileName:"
- "setFinishedAssetCollections:"
- "setFinishedAssets:"
- "setFireDate:"
- "setFirstName:"
- "setFocusAlbumGUID:"
- "setFocusAlbumGUID:forPersonID:"
- "setFocusAssetCollectionGUID:"
- "setFocusAssetCollectionGUID:forPersonID:"
- "setForeignCtag:"
- "setFullName:"
- "setGUID:"
- "setGate:"
- "setHTTPBody:"
- "setHTTPMethod:"
- "setHasComments:"
- "setHasDeactivated:"
- "setHasIcplAction:"
- "setHasMpsAction:"
- "setHasOriginalLibrarySize:"
- "setHasRetryAfterSeconds:"
- "setHasShutDown:"
- "setHasVersion:"
- "setHysteresisTimer:"
- "setICPLDeviceID:"
- "setID:"
- "setIcplAction:"
- "setIdleCountQueue:"
- "setIdleTimerGate:"
- "setIdsService:"
- "setInFlightAssets:"
- "setInitialFailureDate:"
- "setInitialInterval:"
- "setInvariantParam:"
- "setInvitation:"
- "setIsBatchComment:"
- "setIsCaption:"
- "setIsDeletable:"
- "setIsDone:"
- "setIsDownloadingThumbnails:"
- "setIsFamilySharedAlbum:"
- "setIsLike:"
- "setIsMetricsGatheringEnabled:"
- "setIsMine:"
- "setIsRetryingOutstandingActivities:"
- "setIsShuttingDown:"
- "setIsWaitingForFirstDownloadEvent:"
- "setItemFlags:"
- "setItemIDs:"
- "setItemsInFlight:"
- "setLastEnqueuedCommand:"
- "setLastName:"
- "setLocale:"
- "setMMCSAccessHeader:"
- "setMMCSAccessHeader:andTimeStamp:"
- "setMMCSAccessHeaderTimeStamp:"
- "setMMCSBackoffManagerParameters:"
- "setMMCSError:"
- "setMMCSHash:"
- "setMMCSItemFlags:"
- "setMMCSItemID:"
- "setMMCSItemSize:"
- "setMMCSReceipt:"
- "setMMCSURL:"
- "setMMCSUTI:"
- "setMPSDeviceID:"
- "setMSASCounterpartInstance:"
- "setMapQueue:"
- "setMasterAsset:"
- "setMasterAssetHash:"
- "setMaxBackoffInterval:"
- "setMaxBatchCount:"
- "setMaxGroupedCallbackEventBatchCount:"
- "setMaxGroupedCallbackEventIdleInterval:"
- "setMaxGroupedCallbackEventStaleness:"
- "setMaxMMCSTokenValidityTimeInterval:"
- "setMaxMetadataRetryCount:"
- "setMaxRetryCount:"
- "setMaximumLongSideLength:"
- "setMediaAssetType:"
- "setMemberQueue:"
- "setMetadata:"
- "setMetadataBackoffManagerParameters:"
- "setMetadataValue:forKey:"
- "setMigrationMarker:"
- "setMigrationMarker:personID:"
- "setMinimumLongSideLength:"
- "setModel:"
- "setMpsAction:"
- "setMultipleContributorsEnabled:forAlbum:completionBlock:"
- "setMultipleContributorsEnabled:forAlbum:info:completionBlock:"
- "setMultipleContributorsEnabled:forAlbumWithGUID:completionBlock:"
- "setMultipleContributorsEnabled:forAlbumWithGUID:info:completionBlock:"
- "setMultipleContributorsEnabled:forAlbumWithGUID:personID:completionBlock:"
- "setMultipleContributorsEnabled:forAlbumWithGUID:personID:info:completionBlock:"
- "setName:"
- "setNextActivityDate:forPersonID:"
- "setNextExpiryDate:"
- "setNextUpdateDateByPersonID:"
- "setNominalShortSideLength:"
- "setObject:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setObjectGUID:"
- "setObservers:"
- "setOriginalLibrarySize:"
- "setOwnerEmail:"
- "setOwnerFirstName:"
- "setOwnerFullName:"
- "setOwnerIsWhitelisted:"
- "setOwnerLastName:"
- "setOwnerPersonID:"
- "setParams:forCommandWithIdentifier:"
- "setPath:"
- "setPathForPersonInfoDictionary:"
- "setPendingAlbumChanges:"
- "setPendingAlbumGUIDToAssetCollections:"
- "setPendingAlbumGUIDsWithKeyValueChanges:"
- "setPendingAlbumGUIDsWithSharingInfoChanges:"
- "setPendingChanges:"
- "setPendingConnectionsGroup:"
- "setPendingConnectionsQueue:"
- "setPendingRootCtag:"
- "setPersistentObject:forKey:"
- "setPersistentObject:forKey:personID:"
- "setPersistentString:forKey:"
- "setPersonID:"
- "setPersonIDToDelegateMap:"
- "setPersonIDToPersonInfoDictionary:"
- "setPersonIDToStateMachineMap:"
- "setPhoneInvitations:"
- "setPhones:"
- "setPhotoCreationDate:"
- "setPhotoNumber:"
- "setPosition:"
- "setPostCommandCompletionBlock:"
- "setProtocol:"
- "setProtocolFileSize:"
- "setPublicAccessEnabled:forAlbum:completionBlock:"
- "setPublicAccessEnabled:forAlbum:info:completionBlock:"
- "setPublicAccessEnabled:forAlbumWithGUID:completionBlock:"
- "setPublicAccessEnabled:forAlbumWithGUID:info:completionBlock:"
- "setPublicAccessEnabled:forAlbumWithGUID:personID:completionBlock:"
- "setPublicAccessEnabled:forAlbumWithGUID:personID:info:completionBlock:"
- "setPublicURLString:"
- "setPublishBatchSize:"
- "setPublishTargetByteCount:"
- "setQueue:"
- "setRandomizeFactor:"
- "setRelationshipState:"
- "setRetrievalBatchSize:"
- "setRetryAfterDate:"
- "setRetryAfterSeconds:"
- "setRootCtagFromPendingRootCtag"
- "setSendMessageIdentifierToPhone:"
- "setServerSideConfigQueue:"
- "setServerSideConfigVersion:"
- "setServerSideConfiguration:"
- "setServerUploadedDate:"
- "setShouldDownloadEarliestPhotosFirst:"
- "setSignatures:"
- "setSize:"
- "setStabilizedIsBusy:"
- "setStalenessTimerGate:"
- "setState:"
- "setStateMachine:"
- "setStatementQueue:"
- "setStatements:"
- "setStepBlock:"
- "setStmt:"
- "setStorageProtocolURL:"
- "setStreamID:"
- "setSubscriptionDate:"
- "setSuppressCellular:"
- "setTargetRetrievalByteCount:"
- "setThreadKeepAliveTimer:"
- "setTimeZone:"
- "setTimestamp:"
- "setType:"
- "setUIBusyCount:"
- "setURL:"
- "setURLString:"
- "setUniqueID:"
- "setUpdatedSharedAlbumURL:"
- "setUserInfo:"
- "setUserInfo:forAccessControlWithGUID:"
- "setUserInfo:forAlbumWithGUID:"
- "setUserInfo:forAssetCollectionWithGUID:"
- "setUserInfo:forCommentWithGUID:"
- "setUserInfo:forInvitationWithGUID:"
- "setValue:forKey:"
- "setVariantParam:"
- "setVersion:"
- "setWasDeleted:"
- "setWithArray:"
- "setWithCapacity:"
- "setWithObject:"
- "setWithObjects:"
- "setWorkQueue:"
- "setWorkThread:"
- "set_appleIDContext:"
- "set_userManifest:"
- "sharedCloudDatabase"
- "sharedLogger"
- "sharedManager"
- "sharedStreamsProtocolVersionString"
- "shouldDownloadEarliestPhotosFirst"
- "shouldEnableNewFeatures"
- "shouldLogAtLevel:"
- "showInvitationFailureAlertForPersonID:failures:"
- "shutDown"
- "shutDownCompletionBlock:"
- "shutDownError"
- "shutDownFlush:completionBlock:"
- "shutDownForDestruction:completionBlock:"
- "shutDownStateMachine:forDestruction:completionBlock:"
- "signatures"
- "smallestObjectWrappersTargetTotalSize:maxCount:"
- "socketOptions"
- "sortUsingComparator:"
- "specificationWithSharedAlbumSpecificationString:"
- "stabilizedDidIdle"
- "stabilizedDidUnidle"
- "stabilizedIsBusy"
- "stalenessTimerGate"
- "standardUserDefaults"
- "startOperation:itemGUID:"
- "stateMachine"
- "statementForString:"
- "statementQueue"
- "statements"
- "statusCode"
- "stepBlock"
- "stmt"
- "stopAllActivities"
- "stopAssetDownloadsCompletionBlock:"
- "stopAssetDownloadsForPersonID:"
- "stopCompletionBlock:"
- "stopHandlerBlock"
- "stopOperation:itemGUID:"
- "stoppingError"
- "storageProtocolURL"
- "stringByAppendingPathComponent:"
- "stringByAppendingPathExtension:"
- "stringByAppendingString:"
- "stringByDeletingLastPathComponent"
- "stringByDeletingPathExtension"
- "stringForKey:"
- "stringWithCString:encoding:"
- "stringWithFileSystemRepresentation:length:"
- "stringWithFormat:"
- "stringWithString:"
- "stringWithUTF8String:"
- "subarrayWithRange:"
- "submitAssetCollectionsForPublication:skipAssetCollections:"
- "subscribeStorageProtocol:didFinishRetrievingAsset:error:"
- "subscribeStorageProtocolDidFinishRetrievingAllAssets:"
- "subscribeStreamsProtocol:didFindDisappearedSubscriptionForPersonID:"
- "subscribeStreamsProtocol:didFindTemporarilyUnavailableSubscriptionForPersonID:"
- "subscribeStreamsProtocol:didFinishError:"
- "subscribeStreamsProtocol:didFinishReceivingUpdatesForPersonID:ctag:"
- "subscribeStreamsProtocol:didReceiveAssetCollections:forPersonID:"
- "subscribeStreamsProtocol:didReceiveAuthenticationError:"
- "subscribeStreamsProtocol:willReceiveUpdatesForPersonID:wasReset:metadata:"
- "subscribeToAlbum:completionBlock:"
- "subscribeToAlbum:info:"
- "subscribeToAlbumWithGUID:"
- "subscribeToAlbumWithGUID:info:"
- "subscribeToAlbumWithGUID:personID:"
- "subscribeToAlbumWithGUID:personID:info:"
- "subscribedStreamWithStreamID:"
- "subscribedStreams"
- "subscribedStreamsForPersonID:"
- "subscriber:didFailToRetriveSubscriptionUpdateWithError:"
- "subscriber:didFindDisappearedSubscriptionforStreamID:"
- "subscriber:didFinishRequestingAssetRetrievalForStreamID:"
- "subscriber:didFinishRetrievingAsset:error:"
- "subscriber:didReceiveDeleteForAssetCollections:streamID:"
- "subscriber:didRequestAssetRetrievalForAssetCollections:streamID:"
- "subscriber:didResetSyncForStreamID:"
- "subscriber:willBeginRequestingAssetRetrievalForStreamID:"
- "subscriberDidCompleteCheckForNewAssetCollections:"
- "subscriberForPersonID:"
- "subscriberPluginClass"
- "subscriberPluginForPersonID:"
- "subscriberWillAssignPluginAsDelegateOfSubscriber:"
- "subscriberWillDeassignPluginAsDelegateOfSubscriber:"
- "substringToIndex:"
- "summarizeOperation:itemGUID:formatBlock:"
- "superclass"
- "supportsSecureCoding"
- "targetRetrievalByteCount"
- "theDaemon"
- "threadKeepAliveTimer"
- "threadMain:"
- "thumbnailImageScalingSpecification"
- "timeIntervalSinceDate:"
- "timeIntervalSinceNow"
- "timeIntervalSinceReferenceDate"
- "timeZoneForSecondsFromGMT:"
- "timerWithTimeInterval:target:selector:userInfo:repeats:"
- "typeWithIdentifier:"
- "unarchivedObjectOfClasses:fromData:error:"
- "uniqueID"
- "unregisterAsset:"
- "unregisterAssetCollections:"
- "unregisterAssetCollections:completionBlock:"
- "unregisterAssets:"
- "unsignedIntegerValue"
- "unsignedLongLongValue"
- "unsignedLongValue"
- "unsubscribeFromAlbum:completionBlock:"
- "unsubscribeFromAlbum:info:"
- "unsubscribeFromAlbumWithGUID:"
- "unsubscribeFromAlbumWithGUID:info:"
- "unsubscribeFromAlbumWithGUID:personID:"
- "unsubscribeFromAlbumWithGUID:personID:info:"
- "unviewedAlbumCount"
- "unviewedAssetCollectionCountForAlbumWithGUID:"
- "updateAlbum:albumURLString:completionBlock:"
- "updateAlbum:updateAlbumFlags:info:"
- "updateOwnerReputationScoreForAlbum:"
- "updateWithSharingRelationship:"
- "updatedSharedAlbumURL"
- "uploadCompleteURL"
- "useCellular"
- "useForeignCtag"
- "userInfoForAccessControlWithGUID:"
- "userInfoForAlbumWithGUID:"
- "userInfoForAssetCollectionWithGUID:"
- "userInfoForCommentWithGUID:"
- "userInfoForInvitationWithGUID:"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8i16"
- "v24@0:8@\"<MSASModelObserver>\"16"
- "v24@0:8@\"<MSDeleterDelegate>\"16"
- "v24@0:8@\"<MSPublishStorageProtocol>\"16"
- "v24@0:8@\"<MSPublishStorageProtocolDelegate>\"16"
- "v24@0:8@\"<MSPublisherDelegate>\"16"
- "v24@0:8@\"<MSSubscribeStorageProtocol>\"16"
- "v24@0:8@\"<MSSubscribeStorageProtocolDelegate>\"16"
- "v24@0:8@\"<MSSubscriberDelegate>\"16"
- "v24@0:8@\"IDSService\"16"
- "v24@0:8@\"MSASAlbum\"16"
- "v24@0:8@\"MSASAssetDownloader\"16"
- "v24@0:8@\"MSASStateMachine\"16"
- "v24@0:8@\"MSAsset\"16"
- "v24@0:8@\"MSBackoffManager\"16"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@\"NSData\"16"
- "v24@0:8@\"NSDate\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8^*16"
- "v24@0:8^I16"
- "v24@0:8^Q16"
- "v24@0:8^{__CFDictionary=}16"
- "v24@0:8^{__MSSPCContext=^v^{__CFString}^{__CFString}^{__CFDictionary}^{__CFDictionary}d^?^?^?^?^?^{CFURLConnectionClient_V1}^{_CFURLConnection}^{__CFData}^{__CFHTTPMessage}^{__CFError}}16"
- "v24@0:8^{sqlite3=}16"
- "v24@0:8^{sqlite3_stmt=}16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8@\"NSArray\"16i24"
- "v28@0:8@\"NSString\"16B24"
- "v28@0:8@16B24"
- "v28@0:8@16i24"
- "v28@0:8@?16B24"
- "v28@0:8B16@\"NSDictionary\"20"
- "v28@0:8B16@20"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?>20"
- "v28@0:8i16@20"
- "v32@0:8@\"<NSCoding>\"16@\"NSString\"24"
- "v32@0:8@\"IDSService\"16@\"NSArray\"24"
- "v32@0:8@\"IDSService\"16@\"NSSet\"24"
- "v32@0:8@\"MMCSEngine\"16@\"NSString\"24"
- "v32@0:8@\"MSASAlbum\"16@\"NSDictionary\"24"
- "v32@0:8@\"MSASAlbum\"16@?<v@?B@\"NSError\">24"
- "v32@0:8@\"MSASAssetDownloader\"16Q24"
- "v32@0:8@\"MSASStateMachine\"16@\"NSDictionary\"24"
- "v32@0:8@\"MSDeleteStreamsProtocol\"16@\"NSError\"24"
- "v32@0:8@\"MSPublishStreamsProtocol\"16@\"NSError\"24"
- "v32@0:8@\"MSReauthorizationProtocol\"16@\"NSError\"24"
- "v32@0:8@\"MSResetServerProtocol\"16@\"NSError\"24"
- "v32@0:8@\"MSServerSideConfigProtocol\"16@\"NSError\"24"
- "v32@0:8@\"MSStreamsProtocol\"16@\"NSDate\"24"
- "v32@0:8@\"MSSubscribeStreamsProtocol\"16@\"NSError\"24"
- "v32@0:8@\"MSSubscribeStreamsProtocol\"16@\"NSString\"24"
- "v32@0:8@\"NSArray\"16@\"NSArray\"24"
- "v32@0:8@\"NSArray\"16@\"NSString\"24"
- "v32@0:8@\"NSArray\"16@\"NSURL\"24"
- "v32@0:8@\"NSDictionary\"16@?<v@?>24"
- "v32@0:8@\"NSString\"16@\"NSDate\"24"
- "v32@0:8@\"NSString\"16@\"NSDictionary\"24"
- "v32@0:8@\"NSString\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\"@\"NSURL\"@\"NSDate\">24"
- "v32@0:8@\"NSURLConnection\"16@\"NSError\"24"
- "v32@0:8@\"NSURLConnection\"16@\"NSURLAuthenticationChallenge\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8@16q24"
- "v32@0:8^i16^i24"
- "v32@0:8^{sqlite3_stmt=}16^{sqlite3_stmt=}24"
- "v36@0:8@\"<MSPublishStorageProtocol>\"16i24@\"MSAsset\"28"
- "v36@0:8@\"MMCSEngine\"16@\"NSString\"24i32"
- "v36@0:8@\"NSString\"16B24@\"NSDictionary\"28"
- "v36@0:8@16@24i32"
- "v36@0:8@16B24@28"
- "v36@0:8@16B24@?28"
- "v36@0:8@16i24@28"
- "v36@0:8B16@\"NSString\"20@?<v@?@\"NSError\">28"
- "v36@0:8B16@20@28"
- "v36@0:8B16@20@?28"
- "v36@0:8i16@20@28"
- "v40@0:8@\"<MSPublishStorageProtocol>\"16@\"MSAsset\"24@\"NSError\"32"
- "v40@0:8@\"<MSSubscribeStorageProtocol>\"16@\"MSAsset\"24@\"NSError\"32"
- "v40@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSGroupSessionParticipantUpdate\"32"
- "v40@0:8@\"IDSService\"16@\"IDSDevice\"24@?<v@?>32"
- "v40@0:8@\"IDSService\"16@\"NSString\"24@\"NSArray\"32"
- "v40@0:8@\"MMCSEngine\"16@\"MMCSRequestorContext\"24@\"NSArray\"32"
- "v40@0:8@\"MMCSEngine\"16f24i28@\"<MMCSAsset>\"32"
- "v40@0:8@\"MSASStateMachine\"16@\"MSASAlbum\"24@\"NSDictionary\"32"
- "v40@0:8@\"MSASStateMachine\"16@\"NSArray\"24@\"NSDictionary\"32"
- "v40@0:8@\"MSASStateMachine\"16@\"NSArray\"24@\"NSString\"32"
- "v40@0:8@\"MSASStateMachine\"16@\"NSDictionary\"24@\"NSError\"32"
- "v40@0:8@\"MSPublishStreamsProtocol\"16@\"NSDictionary\"24@\"NSError\"32"
- "v40@0:8@\"MSServerSideConfigProtocol\"16@\"NSDictionary\"24@\"NSError\"32"
- "v40@0:8@\"MSSubscribeStreamsProtocol\"16@\"NSArray\"24@\"NSString\"32"
- "v40@0:8@\"MSSubscribeStreamsProtocol\"16@\"NSString\"24@\"NSString\"32"
- "v40@0:8@\"NSArray\"16@\"NSString\"24@\"NSDictionary\"32"
- "v40@0:8@\"NSArray\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSDate\"24@\"NSDictionary\"32"
- "v40@0:8@\"NSString\"16@\"NSDictionary\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32"
- "v40@0:8@\"NSString\"16Q24@?<v@?@\"NSError\"@\"NSArray\"@\"NSDate\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16@?24@?32"
- "v40@0:8@16Q24@?32"
- "v40@0:8@16f24i28@32"
- "v40@0:8Q16@24@32"
- "v44@0:8@\"IDSService\"16B24@\"NSError\"28@\"NSString\"36"
- "v44@0:8@\"MSSubscribeStreamsProtocol\"16@\"NSString\"24B32@\"NSDictionary\"36"
- "v44@0:8@16@24B32@36"
- "v44@0:8@16@24B32@?36"
- "v44@0:8@16B24@28@36"
- "v44@0:8@16B24Q28@?36"
- "v44@0:8B16@\"NSString\"20@\"NSDictionary\"28@?<v@?@\"NSDictionary\"@\"NSError\">36"
- "v44@0:8B16@20@28@?36"
- "v48@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSGroupSessionParticipantUpdate\"32@\"IDSMessageContext\"40"
- "v48@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSSession\"32@\"NSString\"40"
- "v48@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@40"
- "v48@0:8@\"MMCSEngine\"16@\"<MMCSAsset>\"24@\"NSString\"32@\"NSError\"40"
- "v48@0:8@\"MSASAssetDownloader\"16@\"MSAsset\"24@\"NSString\"32@\"NSError\"40"
- "v48@0:8@\"MSASAssetUploader\"16@\"MSASAssetCollection\"24@\"MSASAlbum\"32@\"NSError\"40"
- "v48@0:8@\"MSASStateMachine\"16@\"MSASAlbum\"24@\"NSDictionary\"32@\"NSError\"40"
- "v48@0:8@\"MSASStateMachine\"16@\"MSAsset\"24@\"MSASAlbum\"32@\"NSError\"40"
- "v48@0:8@\"MSASStateMachine\"16@\"NSArray\"24@\"MSASAlbum\"32@\"NSDictionary\"40"
- "v48@0:8@\"MSASStateMachine\"16@\"NSDictionary\"24@\"MSASAlbum\"32@\"NSDictionary\"40"
- "v48@0:8@\"MSASStateMachine\"16@\"NSString\"24@\"NSDictionary\"32@\"NSError\"40"
- "v48@0:8@\"MSASStateMachine\"16@\"NSString\"24@\"NSString\"32@\"NSDictionary\"40"
- "v48@0:8@\"MSDeleteStreamsProtocol\"16@\"NSArray\"24@\"NSArray\"32@\"NSError\"40"
- "v48@0:8@\"MSReauthorizationProtocol\"16@\"NSArray\"24@\"NSArray\"32@\"NSError\"40"
- "v48@0:8@\"NSArray\"16@\"NSString\"24@\"NSDictionary\"32@?<v@?@\"NSError\">40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16Q24@32@?40"
- "v48@0:8Q16@24@32@40"
- "v52@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32B40@\"NSError\"44"
- "v52@0:8@\"IDSService\"16@\"IDSAccount\"24B32@\"NSString\"36@\"NSData\"44"
- "v52@0:8@\"MSASStateMachine\"16@\"NSString\"24i32@\"NSDictionary\"36@\"NSError\"44"
- "v52@0:8@16@24@32B40@44"
- "v52@0:8@16@24@32B40@?44"
- "v52@0:8@16@24B32@36@44"
- "v52@0:8@16@24Q32B40@?44"
- "v52@0:8@16@24i32@36@44"
- "v52@0:8B16@20@28@36@?44"
- "v52@0:8Q16i24d28@36@44"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSProtobuf\"32@\"NSString\"40@\"IDSMessageContext\"48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSSession\"32@\"NSString\"40@\"NSData\"48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"IDSSession\"32@\"NSString\"40@\"NSDictionary\"48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSData\"32@\"NSString\"40@\"IDSMessageContext\"48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSDictionary\"32@\"NSString\"40@\"IDSMessageContext\"48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32q40q48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSURL\"32@\"NSString\"40@\"IDSMessageContext\"48"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24q32@\"NSString\"40@\"IDSMessageContext\"48"
- "v56@0:8@\"MSASStateMachine\"16@\"MSASAlbum\"24@\"NSDictionary\"32@\"NSError\"40@\"NSString\"48"
- "v56@0:8@\"MSASStateMachine\"16@\"MSASAlbum\"24@\"NSString\"32@\"NSDictionary\"40@\"NSError\"48"
- "v56@0:8@\"MSASStateMachine\"16@\"MSASAssetCollection\"24@\"MSASAlbum\"32@\"NSDictionary\"40@\"NSError\"48"
- "v56@0:8@\"MSASStateMachine\"16@\"MSASSharingRelationship\"24@\"MSASAlbum\"32@\"NSDictionary\"40@\"NSError\"48"
- "v56@0:8@\"MSASStateMachine\"16@\"NSArray\"24@\"MSASAlbum\"32@\"NSArray\"40@\"NSDictionary\"48"
- "v56@0:8@\"MSASStateMachine\"16@\"NSArray\"24@\"MSASAlbum\"32@\"NSDictionary\"40@\"NSError\"48"
- "v56@0:8@\"MSASStateMachine\"16@\"NSArray\"24@\"NSArray\"32@\"NSArray\"40@\"NSDictionary\"48"
- "v56@0:8@\"MSASStateMachine\"16@\"NSArray\"24@\"NSString\"32@\"NSString\"40@\"NSDictionary\"48"
- "v56@0:8@\"MSASStateMachine\"16@\"NSString\"24@\"MSASAlbum\"32@\"NSDictionary\"40@\"NSError\"48"
- "v56@0:8@\"MSASStateMachine\"16@24@\"NSString\"32@\"NSString\"40@\"NSDictionary\"48"
- "v56@0:8@16@24@32@40@48"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16@24@32q40q48"
- "v56@0:8@16@24q32@40@48"
- "v60@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32B40@\"NSError\"44@\"IDSMessageContext\"52"
- "v60@0:8@16@24@32@40B48@?52"
- "v60@0:8@16@24@32B40@44@52"
- "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSData\"32@\"NSString\"40@\"NSString\"48@\"IDSMessageContext\"56"
- "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSDictionary\"32@\"NSString\"40@?<v@?B>48@\"IDSMessageContext\"56"
- "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSData\"48@\"NSError\"56"
- "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSURL\"32@\"NSDictionary\"40@\"NSString\"48@\"IDSMessageContext\"56"
- "v64@0:8@\"MSASStateMachine\"16@\"MSASAssetCollection\"24@\"MSASAlbum\"32@\"NSString\"40@\"NSDictionary\"48@\"NSError\"56"
- "v64@0:8@\"MSASStateMachine\"16@\"MSASComment\"24@\"MSASAssetCollection\"32@\"MSASAlbum\"40@\"NSDictionary\"48@\"NSError\"56"
- "v64@0:8@\"MSASStateMachine\"16@\"NSDictionary\"24@\"NSString\"32@\"MSASAlbum\"40@\"NSString\"48@\"NSDictionary\"56"
- "v64@0:8@16@24@32@40@48@56"
- "v64@0:8@16@24@32@40@48@?56"
- "v64@0:8@16@24@32@40@48q56"
- "v64@0:8@16@24@32@40@?48@56"
- "v80@0:8@16^B24^B32^B40^B48^B56^B64^B72"
- "validateInvitationForAlbum:completionBlock:"
- "valueForKey:"
- "variantParam"
- "videoDerivativeSpecificationsWithDictionaryArray:"
- "videoURLForAssetCollection:inAlbum:completionBlock:"
- "videoURLForAssetCollectionWithGUID:completionBlock:"
- "videoURLsForAssetCollection:forMediaAssetType:inAlbum:completionBlock:"
- "videoURLsForAssetCollectionWithGUID:forMediaAssetType:completionBlock:"
- "waitUntilFinished"
- "willDestroyStateMachineForPersonID:"
- "workQueue"
- "workQueueApplyServerSideConfiguration"
- "workQueueAssertBusyAssertion"
- "workQueueCancel"
- "workQueueCancelAllCommandsFilteredByAlbumGUID:assetCollectionGUID:"
- "workQueueCancelAssetCollections:"
- "workQueueCancelCompletionBlock:"
- "workQueueCheckForNextCommand"
- "workQueueClearIdleTimer"
- "workQueueClearStalenessTimer"
- "workQueueDeassertBusyAssertion"
- "workQueueDidEnqueueFirstItem"
- "workQueueDidEnqueueSubsequentItem"
- "workQueueDidFailToFinishCommandDueToTemporaryError:"
- "workQueueDidFinishCommand"
- "workQueueDidFinishCommandByLeavingCommandInQueue"
- "workQueueDidFinishCommandByReplacingCurrentCommandWithCommand:params:personID:albumGUID:assetCollectionGUID:"
- "workQueueDidFinishCommandDueToCancellation"
- "workQueueDidFinishWithItem:error:"
- "workQueueDownloadNextBatch"
- "workQueueEndCommandWithError:command:params:albumGUID:assetCollectionGUID:"
- "workQueueEnqueueCommand:variantParam:invariantParam:"
- "workQueueFlushQueue"
- "workQueueForgetEverythingAboutPersonID:completionBlock:"
- "workQueueForgetEverythingAboutPersonIDs:index:completionBlock:"
- "workQueueGoIdle"
- "workQueueMaxMMCSTokenValidityTimeInterval"
- "workQueueNextItemID"
- "workQueueObjectGUID"
- "workQueuePerformNextCommand"
- "workQueueRefreshServerSideConfig"
- "workQueueRegisterAssetCollections:index:results:completionBlock:"
- "workQueueRegisterAssets:completionBlock:"
- "workQueueRegisterAssets:index:completionBlock:"
- "workQueueRestartIdleTimer"
- "workQueueRestartStalenessTimer"
- "workQueueRetryOutstandingActivities"
- "workQueueScheduleReauthForAssets:inAlbum:"
- "workQueueShutDownCompletionBlock:"
- "workQueueStop"
- "workQueueStopTrackingItem:"
- "workQueueUnregisterAssets:"
- "workQueueUpdateNextActivityDate"
- "workQueueUploadNextBatch"
- "workThread"
- "wrapperWithObject:size:"
- "writeData:"
- "writeTo:"
- "writeToFile:atomically:"
- "writeToURL:atomically:"
- "zone"
- "{?=\"originalLibrarySize\"b1}"
- "{?=\"retryAfterSeconds\"b1\"version\"b1\"icplAction\"b1\"mpsAction\"b1}"
- "{?=\"version\"q\"context\"^v\"getFileDescriptorAndContentTypeFromItemCallback\"^?\"getItemProgressCallback\"^?\"getItemDoneCallback\"^?\"putItemProgressCallback\"^?\"putItemDoneCallback\"^?\"requestCompletedCallback\"^?}"
- "{_MSDSPCContext=\"_super\"{__MSSPCContext=\"owner\"^v\"personID\"^{__CFString}\"authToken\"^{__CFString}\"deviceInfo\"^{__CFDictionary}\"clientHeadersRef\"^{__CFDictionary}\"connectionTimeout\"d\"__didReceiveDataCallback\"^?\"__didFinishCallback\"^?\"__didFailAuthenticationCallback\"^?\"__didReceiveServerSideConfigVersionCallback\"^?\"__didReceiveRetryAfterCallback\"^?\"__client\"^{CFURLConnectionClient_V1}\"__connection\"^{_CFURLConnection}\"__responseData\"^{__CFData}\"__response\"^{__CFHTTPMessage}\"__error\"^{__CFError}}\"finishedCallback\"^?\"authFailedCallback\"^?\"didReceiveServerSideConfigurationVersionCallback\"^?\"didReceiveRetryAfterCallback\"^?}"
- "{__MSPSPCContext=\"_super\"{__MSSPCContext=\"owner\"^v\"personID\"^{__CFString}\"authToken\"^{__CFString}\"deviceInfo\"^{__CFDictionary}\"clientHeadersRef\"^{__CFDictionary}\"connectionTimeout\"d\"__didReceiveDataCallback\"^?\"__didFinishCallback\"^?\"__didFailAuthenticationCallback\"^?\"__didReceiveServerSideConfigVersionCallback\"^?\"__didReceiveRetryAfterCallback\"^?\"__client\"^{CFURLConnectionClient_V1}\"__connection\"^{_CFURLConnection}\"__responseData\"^{__CFData}\"__response\"^{__CFHTTPMessage}\"__error\"^{__CFError}}\"finishedCallback\"^?\"authFailedCallback\"^?\"didReceiveServerSideConfigurationVersionCallback\"^?\"didReceiveRetryAfterCallback\"^?}"
- "{__MSPSPCUCContext=\"_super\"{__MSSPCContext=\"owner\"^v\"personID\"^{__CFString}\"authToken\"^{__CFString}\"deviceInfo\"^{__CFDictionary}\"clientHeadersRef\"^{__CFDictionary}\"connectionTimeout\"d\"__didReceiveDataCallback\"^?\"__didFinishCallback\"^?\"__didFailAuthenticationCallback\"^?\"__didReceiveServerSideConfigVersionCallback\"^?\"__didReceiveRetryAfterCallback\"^?\"__client\"^{CFURLConnectionClient_V1}\"__connection\"^{_CFURLConnection}\"__responseData\"^{__CFData}\"__response\"^{__CFHTTPMessage}\"__error\"^{__CFError}}\"finishedCallback\"^?\"authFailedCallback\"^?\"didReceiveServerSideConfigurationVersionCallback\"^?}"
- "{__MSRPCContext=\"_super\"{__MSSPCContext=\"owner\"^v\"personID\"^{__CFString}\"authToken\"^{__CFString}\"deviceInfo\"^{__CFDictionary}\"clientHeadersRef\"^{__CFDictionary}\"connectionTimeout\"d\"__didReceiveDataCallback\"^?\"__didFinishCallback\"^?\"__didFailAuthenticationCallback\"^?\"__didReceiveServerSideConfigVersionCallback\"^?\"__didReceiveRetryAfterCallback\"^?\"__client\"^{CFURLConnectionClient_V1}\"__connection\"^{_CFURLConnection}\"__responseData\"^{__CFData}\"__response\"^{__CFHTTPMessage}\"__error\"^{__CFError}}\"finishedCallback\"^?\"authFailedCallback\"^?\"didReceiveRetryAfterCallback\"^?\"didReceiveServerSideConfigurationVersionCallback\"^?}"
- "{__MSRSPCContext=\"_super\"{__MSSPCContext=\"owner\"^v\"personID\"^{__CFString}\"authToken\"^{__CFString}\"deviceInfo\"^{__CFDictionary}\"clientHeadersRef\"^{__CFDictionary}\"connectionTimeout\"d\"__didReceiveDataCallback\"^?\"__didFinishCallback\"^?\"__didFailAuthenticationCallback\"^?\"__didReceiveServerSideConfigVersionCallback\"^?\"__didReceiveRetryAfterCallback\"^?\"__client\"^{CFURLConnectionClient_V1}\"__connection\"^{_CFURLConnection}\"__responseData\"^{__CFData}\"__response\"^{__CFHTTPMessage}\"__error\"^{__CFError}}\"finishedCallback\"^?\"authFailedCallback\"^?\"didReceiveServerSideConfigurationVersionCallback\"^?}"
- "{__MSSSCPCContext=\"_super\"{__MSSPCContext=\"owner\"^v\"personID\"^{__CFString}\"authToken\"^{__CFString}\"deviceInfo\"^{__CFDictionary}\"clientHeadersRef\"^{__CFDictionary}\"connectionTimeout\"d\"__didReceiveDataCallback\"^?\"__didFinishCallback\"^?\"__didFailAuthenticationCallback\"^?\"__didReceiveServerSideConfigVersionCallback\"^?\"__didReceiveRetryAfterCallback\"^?\"__client\"^{CFURLConnectionClient_V1}\"__connection\"^{_CFURLConnection}\"__responseData\"^{__CFData}\"__response\"^{__CFHTTPMessage}\"__error\"^{__CFError}}\"didFinishCallback\"^?\"didFailAuthenticationCallback\"^?}"
- "{__MSSSPCContext=\"_super\"{__MSSPCContext=\"owner\"^v\"personID\"^{__CFString}\"authToken\"^{__CFString}\"deviceInfo\"^{__CFDictionary}\"clientHeadersRef\"^{__CFDictionary}\"connectionTimeout\"d\"__didReceiveDataCallback\"^?\"__didFinishCallback\"^?\"__didFailAuthenticationCallback\"^?\"__didReceiveServerSideConfigVersionCallback\"^?\"__didReceiveRetryAfterCallback\"^?\"__client\"^{CFURLConnectionClient_V1}\"__connection\"^{_CFURLConnection}\"__responseData\"^{__CFData}\"__response\"^{__CFHTTPMessage}\"__error\"^{__CFError}}\"finishedCallback\"^?\"gotDataChunkCallback\"^?\"authFailedCallback\"^?\"didReceiveServerSideConfigurationVersionCallback\"^?\"didReceiveRetryAfterCallback\"^?\"connectionTimeout\"d\"__state\"q\"__chunkLengthData\"^{__CFData}\"__currentChunkData\"^{__CFData}\"__chunkBytesRemaining\"q}"

```
