## PhotoLibraryServices

> `/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices`

```diff

-  __TEXT.__text: 0x744d40
+  __TEXT.__text: 0x744dd0
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0x455a4
-  __TEXT.__const: 0x7128
-  __TEXT.__dlopen_cstrs: 0xa6e
-  __TEXT.__swift5_typeref: 0x11e0
-  __TEXT.__cstring: 0x6c038
+  __TEXT.__objc_methlist: 0x4568c
+  __TEXT.__const: 0x7158
+  __TEXT.__dlopen_cstrs: 0xb28
+  __TEXT.__swift5_typeref: 0x11b2
+  __TEXT.__cstring: 0x6c454
   __TEXT.__swift5_capture: 0x1528
   __TEXT.__constg_swiftt: 0x290
   __TEXT.__swift5_builtin: 0x78

   __TEXT.__swift5_fieldmd: 0x200
   __TEXT.__swift5_proto: 0x70
   __TEXT.__swift5_types: 0x3c
-  __TEXT.__oslogstring: 0x8348f
+  __TEXT.__oslogstring: 0x83dc5
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x20058
+  __TEXT.__gcc_except_tab: 0x2017c
   __TEXT.__ustring: 0xa3a
-  __TEXT.__unwind_info: 0x166f8
+  __TEXT.__unwind_info: 0x16758
   __TEXT.__eh_frame: 0xf88
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x165e0
-  __DATA_CONST.__objc_classlist: 0x23e0
+  __DATA_CONST.__const: 0x166e8
+  __DATA_CONST.__objc_classlist: 0x23d0
   __DATA_CONST.__objc_catlist: 0xf8
-  __DATA_CONST.__objc_protolist: 0x768
+  __DATA_CONST.__objc_protolist: 0x760
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x24f90
-  __DATA_CONST.__objc_protorefs: 0xd0
+  __DATA_CONST.__objc_selrefs: 0x250a0
+  __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x15a0
-  __DATA_CONST.__objc_arraydata: 0x1ce8
-  __DATA_CONST.__got: 0x50d8
-  __AUTH_CONST.__const: 0x9b90
-  __AUTH_CONST.__cfstring: 0x52d60
-  __AUTH_CONST.__objc_const: 0x6fc88
+  __DATA_CONST.__objc_arraydata: 0x1cc0
+  __DATA_CONST.__got: 0x5108
+  __AUTH_CONST.__const: 0x9bb0
+  __AUTH_CONST.__cfstring: 0x52ec0
+  __AUTH_CONST.__objc_const: 0x6fef0
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__objc_intobj: 0x53d0
-  __AUTH_CONST.__objc_arrayobj: 0x14b8
+  __AUTH_CONST.__objc_intobj: 0x5340
+  __AUTH_CONST.__objc_arrayobj: 0x1488
   __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x2f8
   __AUTH_CONST.__objc_floatobj: 0x40
-  __AUTH_CONST.__auth_got: 0x2a78
-  __AUTH.__objc_data: 0x132b0
+  __AUTH_CONST.__auth_got: 0x2a80
+  __AUTH.__objc_data: 0x13350
   __AUTH.__data: 0x1e8
-  __DATA.__objc_ivar: 0x3de4
-  __DATA.__data: 0x7004
+  __DATA.__objc_ivar: 0x3e28
+  __DATA.__data: 0x6fd4
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x3538
+  __DATA.__bss: 0x3540
   __DATA.__common: 0x4
-  __DATA_DIRTY.__objc_data: 0x3660
+  __DATA_DIRTY.__objc_data: 0x3520
   __DATA_DIRTY.__data: 0x50
-  __DATA_DIRTY.__bss: 0x1a0
+  __DATA_DIRTY.__bss: 0x1e0
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 29103
-  Symbols:   94602
-  CStrings:  32398
+  Functions: 29130
+  Symbols:   94713
+  CStrings:  32449
 
Sections:
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__weak_got : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__weak_auth_got : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH.__data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ +[PLAggdLogging shouldExcludeAssetFromLibrarySummary:]
+ +[PLCloudSharedAssetSaveJob assetsdProcessMetadataForAssetCollectionsAndWait:inAlbum:personID:info:libraryServicesManager:]
+ +[PLCloudSharedCommentsJob assetsdLocallyProcessAddedCommentsAndWait:assetGUID:albumGUID:info:libraryServicesManager:]
+ +[PLCollectionShareMigrationSession isRetryableMigrationError:]
+ +[PLCollectionShareMigrationSessionPhaseSilentMigrationCleanup _resetLocalStateForOriginatingScopeIdentifier:photoLibrary:completionHandler:]
+ +[PLCollectionShareMigrationSessionPhaseSilentMigrationCleanup _revertMSASForOriginatingScopeIdentifier:photoLibrary:completionHandler:]
+ +[PLCollectionShareMigrationSessionPhaseSilentMigrationCleanup revertSilentMigrationForOriginatingScopeIdentifier:photoLibrary:completionHandler:]
+ +[PLLibraryOpenerCreationOptions validateContinerIdentifier:]
+ +[PLManagedAsset(Share) _addFullResourceRecordsForAssets:toBatchManager:photoLibrary:]
+ +[PLManagedAsset(Share) _directUploadFullResourcesForProxyAssets:photoLibrary:]
+ +[PLManagedAsset(Share) _successfulProxyAssetsFromResults:proxyMap:]
+ +[PLManagedKeyword deleteAllKeywordsWithoutPersistingInManagedObjectContext:]
+ +[PLManagedKeyword rebuildAllKeywordsFromDirectoryJournalInManagedObjectContext:pathManager:keywordUUIDRemapping:]
+ +[PLMediaAnalysisEmbeddingSearch _baseMADEmbeddingSearchOptionsForSearchOptions:]
+ +[PLMediaAnalysisEmbeddingSearch searchWithQueryTexts:photoLibraryURL:searchOptions:outEmbeddingDatas:error:]
+ +[PLModelMigrationAction_PersistKeywordsToJournalAndFilesystem actionProgressWeight]
+ +[PLModelMigrationAction_RelocateUBFOriginalResourceTypes actionProgressWeight]
+ +[PLPhotoLibraryIdentifier libraryCreateOptionsForApplicationLibraryWithContainerIdentifier:]
+ +[PLPhotoLibraryOpener ensureApplicationLibraryExistsWithContainerIdentifier:uuid:name:error:]
+ +[PLSearchManagedObjectUtilities leoDonatableItemForManagedObject:partialUpdateMask:indexingContext:fetchHelper:embeddingsFetcher:messagesFetcher:]
+ +[PLSearchManagedObjectUtilities searchableItemForObject:fetchHelper:partialUpdateMask:libraryIdentifier:indexingContext:embeddingsFetcher:messagesFetcher:]
+ -[PLAssetsdConnectionAuthorization restrictedResourcesAccessAuthorized]
+ -[PLAssetsdCrashRecoveryClientAuthorization restrictedResourcesAccessAuthorized]
+ -[PLAssetsdMigrationService _ensureSystemColocatedApplicationLibraries]
+ -[PLCloudSharedAssetSaveJob _runDaemonSideWaitUntilFinished:]
+ -[PLCloudSharedAssetSaveJob runDaemonSideAndWait]
+ -[PLCloudSharedCommentsJob _runDaemonSideWaitUntilFinished:]
+ -[PLCloudSharedCommentsJob runDaemonSideAndWait]
+ -[PLCollectionShare checkServerForChangesWithCompletionHandler:]
+ -[PLCollectionShare hasActiveSilentMigration]
+ -[PLCollectionShare informMSASToCompleteMigrationToCPLWithSourceAssetCount:destinationAssetCount:completionHandler:]
+ -[PLCollectionShare informMSASToInitiateMigrationToCPLWithIsSilentMigration:sourceAssetCount:completionHandler:]
+ -[PLCollectionShare setLastModifiedDateIfNeeded:fromMigration:]
+ -[PLCollectionShareCPLBackend checkServerForChangesForCollectionShare:completionHandler:]
+ -[PLCollectionShareCPLBackend informMSASToCompleteMigrationToCPLForCollectionShare:sourceAssetCount:destinationAssetCount:completionHandler:]
+ -[PLCollectionShareCPLBackend informMSASToInitiateMigrationToCPLForCollectionShare:isSilentMigration:sourceAssetCount:completionHandler:]
+ -[PLCollectionShareMigrator _continueMigrationSetupForShareUUID:silent:progress:plLibrary:completionHandler:]
+ -[PLCollectionShareSharedStreamBackend checkServerForChangesForCollectionShare:completionHandler:]
+ -[PLCollectionShareSharedStreamBackend informMSASToCompleteMigrationToCPLForCollectionShare:sourceAssetCount:destinationAssetCount:completionHandler:]
+ -[PLCollectionShareSharedStreamBackend informMSASToInitiateMigrationToCPLForCollectionShare:isSilentMigration:sourceAssetCount:completionHandler:]
+ -[PLFileSystemAssetImporter keywordUUIDRemapping]
+ -[PLFileSystemAssetImporter setKeywordUUIDRemapping:]
+ -[PLGenericAlbum _bumpLastModifiedDate:]
+ -[PLGenericAlbum bumpLastModifiedDateIfValidWithDate:]
+ -[PLLeoDonatableItem addLexemeWithCategory:text:localizationKey:additionalVariants:identifier:]
+ -[PLLeoDonatableItem addLexemeWithCategory:text:localizationKey:identifier:]
+ -[PLLeoDonatableItem(Asset) _addMessagesSenderAndReceiversFromAsset:withMessagesFetcher:]
+ -[PLLeoDonatableItem(Asset) addContentFromAsset:forPropertySets:withIndexingContext:fetchHelper:embeddingsFetcher:messagesFetcher:]
+ -[PLLibraryOpenerCreationOptions initWithDomain:containerIdentifier:uuid:name:]
+ -[PLManagedAsset setKeywordsFromPersistedAttributes:keywordUUIDRemapping:]
+ -[PLManagedAsset synchronizeWithPersistedFileSystemAttributesWithKeywordUUIDRemapping:]
+ -[PLManagedKeyword didSave]
+ -[PLManagedKeyword prepareForDeletion]
+ -[PLManagedKeyword shouldUpdatePersistence]
+ -[PLMediaAnalysisEmbeddingSearchOptions embeddingSearchMode]
+ -[PLMediaAnalysisEmbeddingSearchOptions setEmbeddingSearchMode:]
+ -[PLModelMigrationAction_PersistKeywordsToJournalAndFilesystem performActionWithManagedObjectContext:error:]
+ -[PLModelMigrationAction_RelocateUBFOriginalResourceTypes performActionWithManagedObjectContext:error:]
+ -[PLModelMigrator _importFileSystemImportAssets:intoLibrary:type:progress:keywordUUIDRemapping:]
+ -[PLMomentGeneration _supportsHighlightGeneration]
+ -[PLMomentGenerationThrottle initWithName:canDelayAnyQOS:singleThreadedMode:minDelayBetweenRuns:maxDelayBetweenRuns:timeProvider:targetQueue:target:]
+ -[PLPhotoLibraryOpener _recreationOptionsForMissingApplicationLibraryDatabaseAtURL:]
+ -[PLPhotosHighlight oldestAndNewestDatesForAssetsWithFilter:useDayGroupAssets:error:]
+ -[PLPrimaryResourceDataStoreKeyHelper .cxx_destruct]
+ -[PLSearchIndexingContext contactStore]
+ -[PLSearchIndexingContext setContactStore:]
+ -[PLSearchIndexingEngine _inq_donateSpotlightItemsByBundleID:leoDonatableItems:leoLexemeScoreUpdates:deleteIdentifiers:spotlightClientState:completion:]
+ -[PLSearchIndexingEngine pauseProcessingIncrementalUpdates]
+ -[PLSearchIndexingMessagesFetcher .cxx_destruct]
+ -[PLSearchIndexingMessagesFetcher _batchResolveDisplayNamesForHandles:]
+ -[PLSearchIndexingMessagesFetcher _cachedDisplayNameForHandle:]
+ -[PLSearchIndexingMessagesFetcher _cachedMessageInfoForAsset:]
+ -[PLSearchIndexingMessagesFetcher _isEnabled]
+ -[PLSearchIndexingMessagesFetcher initWithLibraryIdentifier:indexingContext:]
+ -[PLSearchIndexingMessagesFetcher prefetchForAssets:]
+ -[PLSearchIndexingMessagesFetcher receiverDisplayNamesForAsset:]
+ -[PLSearchIndexingMessagesFetcher senderDisplayNameForAsset:]
+ -[PLSyndicationDeleteEngine _processDeletesForBundleID:unprefixedIdentifiers:error:]
+ -[PLTextEmbeddingServiceOptions setUseCache:]
+ -[PLTextEmbeddingServiceOptions useCache]
+ -[PLUnmanagedAdjustment _generativeEditsRenderTypeFromAssetAdjustments:adjustmentEnvelope:]
+ GCC_except_table1005
+ GCC_except_table10052
+ GCC_except_table10076
+ GCC_except_table10088
+ GCC_except_table10104
+ GCC_except_table10109
+ GCC_except_table10115
+ GCC_except_table10119
+ GCC_except_table10122
+ GCC_except_table10130
+ GCC_except_table10132
+ GCC_except_table10141
+ GCC_except_table10151
+ GCC_except_table10233
+ GCC_except_table10247
+ GCC_except_table10263
+ GCC_except_table10275
+ GCC_except_table10287
+ GCC_except_table10289
+ GCC_except_table10303
+ GCC_except_table10305
+ GCC_except_table10312
+ GCC_except_table10349
+ GCC_except_table10354
+ GCC_except_table10369
+ GCC_except_table10379
+ GCC_except_table10400
+ GCC_except_table10408
+ GCC_except_table10427
+ GCC_except_table10429
+ GCC_except_table10442
+ GCC_except_table10452
+ GCC_except_table10537
+ GCC_except_table10539
+ GCC_except_table10543
+ GCC_except_table10545
+ GCC_except_table10551
+ GCC_except_table10555
+ GCC_except_table10557
+ GCC_except_table10563
+ GCC_except_table10599
+ GCC_except_table10619
+ GCC_except_table1062
+ GCC_except_table10650
+ GCC_except_table10653
+ GCC_except_table10706
+ GCC_except_table10757
+ GCC_except_table10763
+ GCC_except_table10765
+ GCC_except_table10779
+ GCC_except_table10785
+ GCC_except_table10787
+ GCC_except_table10798
+ GCC_except_table10803
+ GCC_except_table10806
+ GCC_except_table10826
+ GCC_except_table1083
+ GCC_except_table10940
+ GCC_except_table10984
+ GCC_except_table11066
+ GCC_except_table11071
+ GCC_except_table11074
+ GCC_except_table11075
+ GCC_except_table11077
+ GCC_except_table11083
+ GCC_except_table11089
+ GCC_except_table11091
+ GCC_except_table11095
+ GCC_except_table11097
+ GCC_except_table11099
+ GCC_except_table11101
+ GCC_except_table11105
+ GCC_except_table11113
+ GCC_except_table11117
+ GCC_except_table11125
+ GCC_except_table11129
+ GCC_except_table11134
+ GCC_except_table11146
+ GCC_except_table11148
+ GCC_except_table11151
+ GCC_except_table11154
+ GCC_except_table11157
+ GCC_except_table11158
+ GCC_except_table11162
+ GCC_except_table11167
+ GCC_except_table11168
+ GCC_except_table11170
+ GCC_except_table11171
+ GCC_except_table11172
+ GCC_except_table11173
+ GCC_except_table11174
+ GCC_except_table11175
+ GCC_except_table11176
+ GCC_except_table11178
+ GCC_except_table11179
+ GCC_except_table11180
+ GCC_except_table11182
+ GCC_except_table11183
+ GCC_except_table11184
+ GCC_except_table11185
+ GCC_except_table11186
+ GCC_except_table11187
+ GCC_except_table11190
+ GCC_except_table11191
+ GCC_except_table11195
+ GCC_except_table11197
+ GCC_except_table11199
+ GCC_except_table11201
+ GCC_except_table11204
+ GCC_except_table11205
+ GCC_except_table11207
+ GCC_except_table11277
+ GCC_except_table11281
+ GCC_except_table11292
+ GCC_except_table1134
+ GCC_except_table11362
+ GCC_except_table11444
+ GCC_except_table11485
+ GCC_except_table11497
+ GCC_except_table1157
+ GCC_except_table11597
+ GCC_except_table11602
+ GCC_except_table11625
+ GCC_except_table1163
+ GCC_except_table11678
+ GCC_except_table1172
+ GCC_except_table11736
+ GCC_except_table1191
+ GCC_except_table1192
+ GCC_except_table11954
+ GCC_except_table1198
+ GCC_except_table1199
+ GCC_except_table11995
+ GCC_except_table1205
+ GCC_except_table12253
+ GCC_except_table1227
+ GCC_except_table12277
+ GCC_except_table12278
+ GCC_except_table12279
+ GCC_except_table12280
+ GCC_except_table12281
+ GCC_except_table12283
+ GCC_except_table12285
+ GCC_except_table12300
+ GCC_except_table12383
+ GCC_except_table12401
+ GCC_except_table12406
+ GCC_except_table12416
+ GCC_except_table12420
+ GCC_except_table12434
+ GCC_except_table12444
+ GCC_except_table12449
+ GCC_except_table1245
+ GCC_except_table12454
+ GCC_except_table12458
+ GCC_except_table12463
+ GCC_except_table12474
+ GCC_except_table12487
+ GCC_except_table12498
+ GCC_except_table12502
+ GCC_except_table12513
+ GCC_except_table12531
+ GCC_except_table12599
+ GCC_except_table12607
+ GCC_except_table12610
+ GCC_except_table12614
+ GCC_except_table12616
+ GCC_except_table12618
+ GCC_except_table12620
+ GCC_except_table12629
+ GCC_except_table12631
+ GCC_except_table12640
+ GCC_except_table12649
+ GCC_except_table12652
+ GCC_except_table12656
+ GCC_except_table12685
+ GCC_except_table12689
+ GCC_except_table12707
+ GCC_except_table12709
+ GCC_except_table12711
+ GCC_except_table12713
+ GCC_except_table12716
+ GCC_except_table12718
+ GCC_except_table12720
+ GCC_except_table12722
+ GCC_except_table12724
+ GCC_except_table12727
+ GCC_except_table12732
+ GCC_except_table12736
+ GCC_except_table12738
+ GCC_except_table12741
+ GCC_except_table12745
+ GCC_except_table12747
+ GCC_except_table12749
+ GCC_except_table12750
+ GCC_except_table12761
+ GCC_except_table12767
+ GCC_except_table12793
+ GCC_except_table12797
+ GCC_except_table12798
+ GCC_except_table12806
+ GCC_except_table12834
+ GCC_except_table12863
+ GCC_except_table1289
+ GCC_except_table12949
+ GCC_except_table13040
+ GCC_except_table1305
+ GCC_except_table13057
+ GCC_except_table13059
+ GCC_except_table13078
+ GCC_except_table13080
+ GCC_except_table13084
+ GCC_except_table13098
+ GCC_except_table13102
+ GCC_except_table13109
+ GCC_except_table13114
+ GCC_except_table1312
+ GCC_except_table13125
+ GCC_except_table13130
+ GCC_except_table1321
+ GCC_except_table13210
+ GCC_except_table13226
+ GCC_except_table13231
+ GCC_except_table13235
+ GCC_except_table13254
+ GCC_except_table13263
+ GCC_except_table13265
+ GCC_except_table13316
+ GCC_except_table13325
+ GCC_except_table13331
+ GCC_except_table13333
+ GCC_except_table13335
+ GCC_except_table1336
+ GCC_except_table13378
+ GCC_except_table13491
+ GCC_except_table13512
+ GCC_except_table13519
+ GCC_except_table13523
+ GCC_except_table13570
+ GCC_except_table13647
+ GCC_except_table13653
+ GCC_except_table13672
+ GCC_except_table13684
+ GCC_except_table13738
+ GCC_except_table13766
+ GCC_except_table13769
+ GCC_except_table13775
+ GCC_except_table13778
+ GCC_except_table13787
+ GCC_except_table1381
+ GCC_except_table13836
+ GCC_except_table13854
+ GCC_except_table13860
+ GCC_except_table13882
+ GCC_except_table13976
+ GCC_except_table14031
+ GCC_except_table14042
+ GCC_except_table14046
+ GCC_except_table14061
+ GCC_except_table14069
+ GCC_except_table14093
+ GCC_except_table14103
+ GCC_except_table14105
+ GCC_except_table14107
+ GCC_except_table14126
+ GCC_except_table14217
+ GCC_except_table14222
+ GCC_except_table1423
+ GCC_except_table14245
+ GCC_except_table14258
+ GCC_except_table14260
+ GCC_except_table14262
+ GCC_except_table1434
+ GCC_except_table14370
+ GCC_except_table14371
+ GCC_except_table14375
+ GCC_except_table14408
+ GCC_except_table1442
+ GCC_except_table14429
+ GCC_except_table14445
+ GCC_except_table14446
+ GCC_except_table14447
+ GCC_except_table14449
+ GCC_except_table14450
+ GCC_except_table14451
+ GCC_except_table14453
+ GCC_except_table14457
+ GCC_except_table14461
+ GCC_except_table14517
+ GCC_except_table14523
+ GCC_except_table14538
+ GCC_except_table14546
+ GCC_except_table14554
+ GCC_except_table14558
+ GCC_except_table14592
+ GCC_except_table14596
+ GCC_except_table14600
+ GCC_except_table14607
+ GCC_except_table14611
+ GCC_except_table14622
+ GCC_except_table14658
+ GCC_except_table14711
+ GCC_except_table14715
+ GCC_except_table1473
+ GCC_except_table14778
+ GCC_except_table14801
+ GCC_except_table1481
+ GCC_except_table14823
+ GCC_except_table14966
+ GCC_except_table1501
+ GCC_except_table15047
+ GCC_except_table15109
+ GCC_except_table1512
+ GCC_except_table15126
+ GCC_except_table15133
+ GCC_except_table15136
+ GCC_except_table15137
+ GCC_except_table15156
+ GCC_except_table1517
+ GCC_except_table15245
+ GCC_except_table15252
+ GCC_except_table15254
+ GCC_except_table15255
+ GCC_except_table15258
+ GCC_except_table15267
+ GCC_except_table15445
+ GCC_except_table15475
+ GCC_except_table15531
+ GCC_except_table1558
+ GCC_except_table1566
+ GCC_except_table15701
+ GCC_except_table15711
+ GCC_except_table15721
+ GCC_except_table15723
+ GCC_except_table15749
+ GCC_except_table15768
+ GCC_except_table15779
+ GCC_except_table15806
+ GCC_except_table15846
+ GCC_except_table15850
+ GCC_except_table15917
+ GCC_except_table15921
+ GCC_except_table15924
+ GCC_except_table15927
+ GCC_except_table160
+ GCC_except_table16085
+ GCC_except_table16115
+ GCC_except_table1613
+ GCC_except_table16132
+ GCC_except_table16140
+ GCC_except_table16151
+ GCC_except_table16157
+ GCC_except_table16159
+ GCC_except_table16165
+ GCC_except_table16169
+ GCC_except_table16171
+ GCC_except_table16172
+ GCC_except_table16178
+ GCC_except_table16180
+ GCC_except_table16182
+ GCC_except_table16188
+ GCC_except_table16234
+ GCC_except_table1624
+ GCC_except_table16249
+ GCC_except_table16252
+ GCC_except_table16269
+ GCC_except_table16273
+ GCC_except_table16286
+ GCC_except_table16295
+ GCC_except_table16299
+ GCC_except_table1633
+ GCC_except_table16396
+ GCC_except_table16400
+ GCC_except_table16402
+ GCC_except_table16404
+ GCC_except_table16427
+ GCC_except_table16428
+ GCC_except_table16435
+ GCC_except_table16444
+ GCC_except_table16453
+ GCC_except_table16462
+ GCC_except_table16475
+ GCC_except_table16534
+ GCC_except_table16536
+ GCC_except_table16628
+ GCC_except_table16689
+ GCC_except_table16702
+ GCC_except_table16723
+ GCC_except_table16815
+ GCC_except_table16835
+ GCC_except_table16841
+ GCC_except_table16846
+ GCC_except_table16853
+ GCC_except_table16881
+ GCC_except_table16893
+ GCC_except_table16934
+ GCC_except_table17001
+ GCC_except_table17006
+ GCC_except_table17014
+ GCC_except_table17024
+ GCC_except_table17036
+ GCC_except_table17050
+ GCC_except_table17056
+ GCC_except_table17066
+ GCC_except_table17079
+ GCC_except_table17089
+ GCC_except_table17099
+ GCC_except_table17129
+ GCC_except_table17135
+ GCC_except_table17198
+ GCC_except_table17201
+ GCC_except_table17248
+ GCC_except_table17259
+ GCC_except_table17279
+ GCC_except_table17286
+ GCC_except_table173
+ GCC_except_table17352
+ GCC_except_table17362
+ GCC_except_table17374
+ GCC_except_table17375
+ GCC_except_table17381
+ GCC_except_table17384
+ GCC_except_table17387
+ GCC_except_table17389
+ GCC_except_table17390
+ GCC_except_table17425
+ GCC_except_table17431
+ GCC_except_table17515
+ GCC_except_table17552
+ GCC_except_table17566
+ GCC_except_table17618
+ GCC_except_table17636
+ GCC_except_table17676
+ GCC_except_table17681
+ GCC_except_table17720
+ GCC_except_table17728
+ GCC_except_table17731
+ GCC_except_table17743
+ GCC_except_table17768
+ GCC_except_table1778
+ GCC_except_table17799
+ GCC_except_table17800
+ GCC_except_table17801
+ GCC_except_table17836
+ GCC_except_table1784
+ GCC_except_table17846
+ GCC_except_table17887
+ GCC_except_table17894
+ GCC_except_table17912
+ GCC_except_table17928
+ GCC_except_table17929
+ GCC_except_table17954
+ GCC_except_table17973
+ GCC_except_table18009
+ GCC_except_table18011
+ GCC_except_table18016
+ GCC_except_table18019
+ GCC_except_table18021
+ GCC_except_table18088
+ GCC_except_table18113
+ GCC_except_table18115
+ GCC_except_table18176
+ GCC_except_table18314
+ GCC_except_table18373
+ GCC_except_table18386
+ GCC_except_table18405
+ GCC_except_table18446
+ GCC_except_table18457
+ GCC_except_table18476
+ GCC_except_table18480
+ GCC_except_table18494
+ GCC_except_table18505
+ GCC_except_table18535
+ GCC_except_table18564
+ GCC_except_table18567
+ GCC_except_table18626
+ GCC_except_table18644
+ GCC_except_table18669
+ GCC_except_table18681
+ GCC_except_table18689
+ GCC_except_table18692
+ GCC_except_table18697
+ GCC_except_table18701
+ GCC_except_table18702
+ GCC_except_table18712
+ GCC_except_table18717
+ GCC_except_table18718
+ GCC_except_table18721
+ GCC_except_table18773
+ GCC_except_table18790
+ GCC_except_table18817
+ GCC_except_table18958
+ GCC_except_table18996
+ GCC_except_table19001
+ GCC_except_table19004
+ GCC_except_table19028
+ GCC_except_table19029
+ GCC_except_table19036
+ GCC_except_table19037
+ GCC_except_table19042
+ GCC_except_table19051
+ GCC_except_table19054
+ GCC_except_table19057
+ GCC_except_table19062
+ GCC_except_table19068
+ GCC_except_table19071
+ GCC_except_table19074
+ GCC_except_table19077
+ GCC_except_table19085
+ GCC_except_table19093
+ GCC_except_table19094
+ GCC_except_table19101
+ GCC_except_table19106
+ GCC_except_table19121
+ GCC_except_table19131
+ GCC_except_table19135
+ GCC_except_table19143
+ GCC_except_table19153
+ GCC_except_table19158
+ GCC_except_table19161
+ GCC_except_table19162
+ GCC_except_table19170
+ GCC_except_table19171
+ GCC_except_table19179
+ GCC_except_table19180
+ GCC_except_table19183
+ GCC_except_table19186
+ GCC_except_table19189
+ GCC_except_table19192
+ GCC_except_table19201
+ GCC_except_table19204
+ GCC_except_table19205
+ GCC_except_table19216
+ GCC_except_table19220
+ GCC_except_table19224
+ GCC_except_table19322
+ GCC_except_table19328
+ GCC_except_table19342
+ GCC_except_table19343
+ GCC_except_table19351
+ GCC_except_table19352
+ GCC_except_table19359
+ GCC_except_table19374
+ GCC_except_table194
+ GCC_except_table19484
+ GCC_except_table19496
+ GCC_except_table19515
+ GCC_except_table1957
+ GCC_except_table19590
+ GCC_except_table19595
+ GCC_except_table19600
+ GCC_except_table19603
+ GCC_except_table19611
+ GCC_except_table1962
+ GCC_except_table19632
+ GCC_except_table19638
+ GCC_except_table19644
+ GCC_except_table19648
+ GCC_except_table19658
+ GCC_except_table19665
+ GCC_except_table19673
+ GCC_except_table19674
+ GCC_except_table19677
+ GCC_except_table19678
+ GCC_except_table19681
+ GCC_except_table19746
+ GCC_except_table19809
+ GCC_except_table19827
+ GCC_except_table19898
+ GCC_except_table19900
+ GCC_except_table19910
+ GCC_except_table19919
+ GCC_except_table19921
+ GCC_except_table19925
+ GCC_except_table19927
+ GCC_except_table19929
+ GCC_except_table19943
+ GCC_except_table20084
+ GCC_except_table20095
+ GCC_except_table20132
+ GCC_except_table20142
+ GCC_except_table20147
+ GCC_except_table20173
+ GCC_except_table20207
+ GCC_except_table20216
+ GCC_except_table20222
+ GCC_except_table20225
+ GCC_except_table20234
+ GCC_except_table20239
+ GCC_except_table20245
+ GCC_except_table20251
+ GCC_except_table20262
+ GCC_except_table20274
+ GCC_except_table20421
+ GCC_except_table20425
+ GCC_except_table20460
+ GCC_except_table20464
+ GCC_except_table20468
+ GCC_except_table20470
+ GCC_except_table20498
+ GCC_except_table20538
+ GCC_except_table20542
+ GCC_except_table20546
+ GCC_except_table20550
+ GCC_except_table20554
+ GCC_except_table20558
+ GCC_except_table20562
+ GCC_except_table20566
+ GCC_except_table20570
+ GCC_except_table20574
+ GCC_except_table20578
+ GCC_except_table20582
+ GCC_except_table20586
+ GCC_except_table20590
+ GCC_except_table20594
+ GCC_except_table20598
+ GCC_except_table20602
+ GCC_except_table20606
+ GCC_except_table20610
+ GCC_except_table20614
+ GCC_except_table20618
+ GCC_except_table20655
+ GCC_except_table20658
+ GCC_except_table20663
+ GCC_except_table20666
+ GCC_except_table20692
+ GCC_except_table20697
+ GCC_except_table20698
+ GCC_except_table20704
+ GCC_except_table20705
+ GCC_except_table20717
+ GCC_except_table20783
+ GCC_except_table20827
+ GCC_except_table20834
+ GCC_except_table20840
+ GCC_except_table20866
+ GCC_except_table20873
+ GCC_except_table20880
+ GCC_except_table20892
+ GCC_except_table20896
+ GCC_except_table20900
+ GCC_except_table20904
+ GCC_except_table20919
+ GCC_except_table20947
+ GCC_except_table20972
+ GCC_except_table20975
+ GCC_except_table21021
+ GCC_except_table21038
+ GCC_except_table21060
+ GCC_except_table21065
+ GCC_except_table21070
+ GCC_except_table21073
+ GCC_except_table21075
+ GCC_except_table21080
+ GCC_except_table21081
+ GCC_except_table21083
+ GCC_except_table21091
+ GCC_except_table21094
+ GCC_except_table21097
+ GCC_except_table21104
+ GCC_except_table21105
+ GCC_except_table21107
+ GCC_except_table21111
+ GCC_except_table21115
+ GCC_except_table21117
+ GCC_except_table21119
+ GCC_except_table21121
+ GCC_except_table21123
+ GCC_except_table21125
+ GCC_except_table21129
+ GCC_except_table21133
+ GCC_except_table21136
+ GCC_except_table21140
+ GCC_except_table21151
+ GCC_except_table21282
+ GCC_except_table21289
+ GCC_except_table21302
+ GCC_except_table21308
+ GCC_except_table21326
+ GCC_except_table21428
+ GCC_except_table21501
+ GCC_except_table21517
+ GCC_except_table21527
+ GCC_except_table21587
+ GCC_except_table216
+ GCC_except_table21702
+ GCC_except_table21714
+ GCC_except_table21715
+ GCC_except_table21733
+ GCC_except_table21735
+ GCC_except_table21742
+ GCC_except_table21767
+ GCC_except_table21785
+ GCC_except_table21833
+ GCC_except_table21840
+ GCC_except_table2186
+ GCC_except_table21867
+ GCC_except_table21873
+ GCC_except_table21877
+ GCC_except_table21882
+ GCC_except_table21944
+ GCC_except_table21960
+ GCC_except_table21977
+ GCC_except_table21982
+ GCC_except_table21996
+ GCC_except_table21998
+ GCC_except_table22035
+ GCC_except_table2205
+ GCC_except_table2210
+ GCC_except_table22107
+ GCC_except_table22109
+ GCC_except_table22157
+ GCC_except_table22164
+ GCC_except_table2218
+ GCC_except_table22194
+ GCC_except_table22207
+ GCC_except_table2221
+ GCC_except_table22210
+ GCC_except_table22236
+ GCC_except_table22267
+ GCC_except_table22356
+ GCC_except_table22402
+ GCC_except_table22406
+ GCC_except_table22408
+ GCC_except_table22410
+ GCC_except_table22437
+ GCC_except_table2246
+ GCC_except_table22509
+ GCC_except_table2251
+ GCC_except_table22510
+ GCC_except_table22550
+ GCC_except_table22583
+ GCC_except_table22587
+ GCC_except_table22628
+ GCC_except_table2265
+ GCC_except_table2267
+ GCC_except_table22697
+ GCC_except_table2289
+ GCC_except_table2295
+ GCC_except_table2311
+ GCC_except_table23110
+ GCC_except_table2323
+ GCC_except_table23409
+ GCC_except_table23421
+ GCC_except_table23429
+ GCC_except_table23476
+ GCC_except_table23480
+ GCC_except_table23536
+ GCC_except_table23548
+ GCC_except_table23564
+ GCC_except_table23665
+ GCC_except_table23674
+ GCC_except_table23704
+ GCC_except_table23780
+ GCC_except_table23781
+ GCC_except_table23848
+ GCC_except_table23866
+ GCC_except_table23873
+ GCC_except_table23897
+ GCC_except_table2404
+ GCC_except_table24091
+ GCC_except_table24095
+ GCC_except_table24140
+ GCC_except_table24174
+ GCC_except_table24206
+ GCC_except_table24251
+ GCC_except_table24252
+ GCC_except_table24318
+ GCC_except_table24321
+ GCC_except_table24338
+ GCC_except_table24351
+ GCC_except_table24360
+ GCC_except_table24362
+ GCC_except_table24366
+ GCC_except_table24373
+ GCC_except_table24389
+ GCC_except_table24396
+ GCC_except_table24423
+ GCC_except_table2456
+ GCC_except_table24612
+ GCC_except_table24616
+ GCC_except_table24623
+ GCC_except_table24625
+ GCC_except_table24626
+ GCC_except_table24630
+ GCC_except_table24636
+ GCC_except_table24641
+ GCC_except_table24643
+ GCC_except_table24646
+ GCC_except_table24647
+ GCC_except_table24648
+ GCC_except_table24651
+ GCC_except_table24652
+ GCC_except_table24653
+ GCC_except_table24683
+ GCC_except_table24686
+ GCC_except_table24709
+ GCC_except_table24712
+ GCC_except_table24713
+ GCC_except_table24718
+ GCC_except_table24723
+ GCC_except_table24727
+ GCC_except_table2476
+ GCC_except_table24790
+ GCC_except_table24797
+ GCC_except_table24799
+ GCC_except_table24801
+ GCC_except_table24803
+ GCC_except_table24805
+ GCC_except_table24813
+ GCC_except_table24815
+ GCC_except_table24829
+ GCC_except_table24855
+ GCC_except_table24858
+ GCC_except_table24865
+ GCC_except_table24867
+ GCC_except_table24869
+ GCC_except_table24871
+ GCC_except_table24875
+ GCC_except_table24895
+ GCC_except_table24898
+ GCC_except_table24916
+ GCC_except_table2492
+ GCC_except_table24921
+ GCC_except_table24925
+ GCC_except_table24927
+ GCC_except_table24929
+ GCC_except_table24931
+ GCC_except_table24939
+ GCC_except_table24943
+ GCC_except_table24947
+ GCC_except_table24951
+ GCC_except_table24953
+ GCC_except_table24965
+ GCC_except_table24989
+ GCC_except_table25023
+ GCC_except_table25024
+ GCC_except_table25027
+ GCC_except_table25052
+ GCC_except_table25054
+ GCC_except_table25056
+ GCC_except_table25079
+ GCC_except_table25082
+ GCC_except_table25085
+ GCC_except_table25087
+ GCC_except_table25141
+ GCC_except_table25203
+ GCC_except_table25207
+ GCC_except_table25210
+ GCC_except_table25213
+ GCC_except_table25220
+ GCC_except_table25246
+ GCC_except_table25249
+ GCC_except_table25261
+ GCC_except_table25264
+ GCC_except_table25277
+ GCC_except_table25282
+ GCC_except_table25286
+ GCC_except_table25289
+ GCC_except_table25310
+ GCC_except_table25319
+ GCC_except_table25325
+ GCC_except_table25332
+ GCC_except_table25340
+ GCC_except_table25341
+ GCC_except_table25342
+ GCC_except_table25349
+ GCC_except_table25442
+ GCC_except_table25443
+ GCC_except_table25444
+ GCC_except_table25445
+ GCC_except_table25449
+ GCC_except_table25453
+ GCC_except_table25454
+ GCC_except_table25455
+ GCC_except_table25458
+ GCC_except_table25488
+ GCC_except_table25496
+ GCC_except_table25500
+ GCC_except_table25528
+ GCC_except_table25543
+ GCC_except_table25577
+ GCC_except_table25581
+ GCC_except_table25589
+ GCC_except_table25605
+ GCC_except_table2561
+ GCC_except_table2562
+ GCC_except_table25625
+ GCC_except_table25629
+ GCC_except_table25660
+ GCC_except_table25666
+ GCC_except_table25735
+ GCC_except_table25753
+ GCC_except_table25762
+ GCC_except_table25765
+ GCC_except_table25768
+ GCC_except_table25771
+ GCC_except_table25777
+ GCC_except_table25780
+ GCC_except_table25783
+ GCC_except_table25786
+ GCC_except_table25789
+ GCC_except_table25792
+ GCC_except_table25795
+ GCC_except_table25798
+ GCC_except_table25801
+ GCC_except_table25804
+ GCC_except_table25807
+ GCC_except_table25810
+ GCC_except_table25813
+ GCC_except_table25816
+ GCC_except_table25819
+ GCC_except_table25822
+ GCC_except_table25825
+ GCC_except_table25831
+ GCC_except_table25834
+ GCC_except_table25837
+ GCC_except_table25840
+ GCC_except_table25843
+ GCC_except_table25846
+ GCC_except_table25849
+ GCC_except_table25852
+ GCC_except_table25855
+ GCC_except_table25858
+ GCC_except_table25861
+ GCC_except_table25864
+ GCC_except_table25867
+ GCC_except_table25870
+ GCC_except_table25873
+ GCC_except_table25876
+ GCC_except_table25879
+ GCC_except_table25882
+ GCC_except_table25885
+ GCC_except_table25888
+ GCC_except_table25891
+ GCC_except_table25894
+ GCC_except_table25897
+ GCC_except_table25900
+ GCC_except_table25903
+ GCC_except_table25909
+ GCC_except_table25912
+ GCC_except_table25918
+ GCC_except_table25921
+ GCC_except_table25924
+ GCC_except_table25927
+ GCC_except_table25930
+ GCC_except_table25933
+ GCC_except_table25936
+ GCC_except_table25939
+ GCC_except_table25942
+ GCC_except_table25945
+ GCC_except_table25948
+ GCC_except_table25951
+ GCC_except_table25960
+ GCC_except_table25963
+ GCC_except_table25966
+ GCC_except_table25969
+ GCC_except_table25972
+ GCC_except_table25975
+ GCC_except_table26033
+ GCC_except_table26036
+ GCC_except_table26039
+ GCC_except_table26077
+ GCC_except_table26083
+ GCC_except_table26131
+ GCC_except_table26163
+ GCC_except_table26168
+ GCC_except_table26170
+ GCC_except_table26172
+ GCC_except_table26218
+ GCC_except_table26263
+ GCC_except_table26271
+ GCC_except_table26276
+ GCC_except_table26287
+ GCC_except_table26308
+ GCC_except_table26315
+ GCC_except_table26317
+ GCC_except_table26318
+ GCC_except_table26450
+ GCC_except_table26456
+ GCC_except_table26478
+ GCC_except_table26520
+ GCC_except_table26526
+ GCC_except_table26531
+ GCC_except_table26535
+ GCC_except_table26543
+ GCC_except_table26570
+ GCC_except_table26576
+ GCC_except_table26578
+ GCC_except_table26619
+ GCC_except_table26763
+ GCC_except_table26767
+ GCC_except_table26770
+ GCC_except_table26772
+ GCC_except_table26884
+ GCC_except_table27076
+ GCC_except_table27079
+ GCC_except_table27086
+ GCC_except_table27101
+ GCC_except_table27109
+ GCC_except_table27116
+ GCC_except_table27118
+ GCC_except_table2713
+ GCC_except_table27132
+ GCC_except_table27137
+ GCC_except_table27141
+ GCC_except_table2715
+ GCC_except_table27159
+ GCC_except_table2725
+ GCC_except_table2729
+ GCC_except_table2752
+ GCC_except_table2755
+ GCC_except_table2793
+ GCC_except_table280
+ GCC_except_table2805
+ GCC_except_table2808
+ GCC_except_table2815
+ GCC_except_table2822
+ GCC_except_table285
+ GCC_except_table2866
+ GCC_except_table2873
+ GCC_except_table2925
+ GCC_except_table2965
+ GCC_except_table3075
+ GCC_except_table3083
+ GCC_except_table3105
+ GCC_except_table3301
+ GCC_except_table3307
+ GCC_except_table332
+ GCC_except_table3359
+ GCC_except_table3411
+ GCC_except_table3413
+ GCC_except_table3421
+ GCC_except_table3438
+ GCC_except_table3448
+ GCC_except_table3463
+ GCC_except_table3492
+ GCC_except_table3512
+ GCC_except_table3521
+ GCC_except_table3525
+ GCC_except_table3529
+ GCC_except_table3531
+ GCC_except_table3535
+ GCC_except_table3539
+ GCC_except_table3586
+ GCC_except_table3841
+ GCC_except_table3844
+ GCC_except_table3847
+ GCC_except_table3850
+ GCC_except_table3853
+ GCC_except_table3863
+ GCC_except_table3923
+ GCC_except_table3961
+ GCC_except_table3972
+ GCC_except_table3978
+ GCC_except_table3997
+ GCC_except_table4006
+ GCC_except_table4034
+ GCC_except_table4094
+ GCC_except_table4099
+ GCC_except_table4110
+ GCC_except_table4115
+ GCC_except_table4118
+ GCC_except_table4142
+ GCC_except_table4144
+ GCC_except_table4153
+ GCC_except_table4154
+ GCC_except_table4156
+ GCC_except_table416
+ GCC_except_table4174
+ GCC_except_table4177
+ GCC_except_table4183
+ GCC_except_table419
+ GCC_except_table4212
+ GCC_except_table4215
+ GCC_except_table422
+ GCC_except_table4231
+ GCC_except_table4236
+ GCC_except_table4240
+ GCC_except_table4244
+ GCC_except_table425
+ GCC_except_table4255
+ GCC_except_table4271
+ GCC_except_table428
+ GCC_except_table434
+ GCC_except_table4436
+ GCC_except_table4438
+ GCC_except_table4444
+ GCC_except_table4446
+ GCC_except_table4469
+ GCC_except_table4471
+ GCC_except_table4479
+ GCC_except_table4483
+ GCC_except_table4489
+ GCC_except_table4512
+ GCC_except_table4530
+ GCC_except_table4531
+ GCC_except_table4556
+ GCC_except_table4606
+ GCC_except_table4610
+ GCC_except_table466
+ GCC_except_table4811
+ GCC_except_table4818
+ GCC_except_table4877
+ GCC_except_table4899
+ GCC_except_table4903
+ GCC_except_table4926
+ GCC_except_table5026
+ GCC_except_table5034
+ GCC_except_table5060
+ GCC_except_table5134
+ GCC_except_table5236
+ GCC_except_table524
+ GCC_except_table5275
+ GCC_except_table5283
+ GCC_except_table5285
+ GCC_except_table5288
+ GCC_except_table538
+ GCC_except_table5507
+ GCC_except_table5522
+ GCC_except_table5548
+ GCC_except_table5625
+ GCC_except_table5638
+ GCC_except_table5641
+ GCC_except_table569
+ GCC_except_table5701
+ GCC_except_table5720
+ GCC_except_table5727
+ GCC_except_table5731
+ GCC_except_table574
+ GCC_except_table5740
+ GCC_except_table5743
+ GCC_except_table5803
+ GCC_except_table5808
+ GCC_except_table5818
+ GCC_except_table5828
+ GCC_except_table5859
+ GCC_except_table5870
+ GCC_except_table5877
+ GCC_except_table5885
+ GCC_except_table5887
+ GCC_except_table591
+ GCC_except_table5922
+ GCC_except_table5923
+ GCC_except_table5926
+ GCC_except_table5927
+ GCC_except_table5935
+ GCC_except_table5948
+ GCC_except_table6039
+ GCC_except_table6041
+ GCC_except_table6064
+ GCC_except_table6102
+ GCC_except_table6106
+ GCC_except_table6110
+ GCC_except_table6131
+ GCC_except_table6136
+ GCC_except_table6141
+ GCC_except_table6145
+ GCC_except_table6163
+ GCC_except_table6166
+ GCC_except_table6168
+ GCC_except_table6172
+ GCC_except_table6174
+ GCC_except_table6232
+ GCC_except_table6255
+ GCC_except_table6276
+ GCC_except_table6281
+ GCC_except_table6285
+ GCC_except_table6289
+ GCC_except_table6294
+ GCC_except_table6299
+ GCC_except_table6307
+ GCC_except_table6311
+ GCC_except_table6322
+ GCC_except_table6333
+ GCC_except_table6336
+ GCC_except_table6338
+ GCC_except_table6349
+ GCC_except_table6350
+ GCC_except_table6352
+ GCC_except_table6354
+ GCC_except_table6357
+ GCC_except_table6359
+ GCC_except_table6362
+ GCC_except_table6375
+ GCC_except_table6384
+ GCC_except_table6388
+ GCC_except_table6390
+ GCC_except_table6396
+ GCC_except_table6398
+ GCC_except_table6400
+ GCC_except_table6401
+ GCC_except_table6403
+ GCC_except_table6405
+ GCC_except_table6406
+ GCC_except_table6407
+ GCC_except_table6409
+ GCC_except_table6411
+ GCC_except_table6412
+ GCC_except_table6413
+ GCC_except_table6414
+ GCC_except_table6443
+ GCC_except_table6481
+ GCC_except_table6494
+ GCC_except_table6521
+ GCC_except_table6587
+ GCC_except_table6703
+ GCC_except_table673
+ GCC_except_table6772
+ GCC_except_table678
+ GCC_except_table691
+ GCC_except_table693
+ GCC_except_table697
+ GCC_except_table6985
+ GCC_except_table7044
+ GCC_except_table706
+ GCC_except_table7090
+ GCC_except_table7097
+ GCC_except_table7108
+ GCC_except_table7114
+ GCC_except_table712
+ GCC_except_table7121
+ GCC_except_table7134
+ GCC_except_table7137
+ GCC_except_table7140
+ GCC_except_table7146
+ GCC_except_table7151
+ GCC_except_table7159
+ GCC_except_table7165
+ GCC_except_table7168
+ GCC_except_table7176
+ GCC_except_table7184
+ GCC_except_table7192
+ GCC_except_table7204
+ GCC_except_table7216
+ GCC_except_table7230
+ GCC_except_table726
+ GCC_except_table7260
+ GCC_except_table7263
+ GCC_except_table7265
+ GCC_except_table7278
+ GCC_except_table7282
+ GCC_except_table7287
+ GCC_except_table7289
+ GCC_except_table7292
+ GCC_except_table7297
+ GCC_except_table730
+ GCC_except_table735
+ GCC_except_table7367
+ GCC_except_table7368
+ GCC_except_table7370
+ GCC_except_table7374
+ GCC_except_table7378
+ GCC_except_table7382
+ GCC_except_table7385
+ GCC_except_table7390
+ GCC_except_table7393
+ GCC_except_table7396
+ GCC_except_table7398
+ GCC_except_table7400
+ GCC_except_table7402
+ GCC_except_table7404
+ GCC_except_table7407
+ GCC_except_table7409
+ GCC_except_table7420
+ GCC_except_table7424
+ GCC_except_table7429
+ GCC_except_table7433
+ GCC_except_table7448
+ GCC_except_table7452
+ GCC_except_table7456
+ GCC_except_table7462
+ GCC_except_table7464
+ GCC_except_table7479
+ GCC_except_table7481
+ GCC_except_table7487
+ GCC_except_table7489
+ GCC_except_table7493
+ GCC_except_table7521
+ GCC_except_table7525
+ GCC_except_table7551
+ GCC_except_table7553
+ GCC_except_table7569
+ GCC_except_table761
+ GCC_except_table7805
+ GCC_except_table7809
+ GCC_except_table7822
+ GCC_except_table7823
+ GCC_except_table7836
+ GCC_except_table7858
+ GCC_except_table7859
+ GCC_except_table7870
+ GCC_except_table7899
+ GCC_except_table7917
+ GCC_except_table7919
+ GCC_except_table7929
+ GCC_except_table7933
+ GCC_except_table7934
+ GCC_except_table7941
+ GCC_except_table7944
+ GCC_except_table798
+ GCC_except_table8001
+ GCC_except_table8005
+ GCC_except_table8007
+ GCC_except_table8018
+ GCC_except_table8025
+ GCC_except_table8089
+ GCC_except_table809
+ GCC_except_table8101
+ GCC_except_table8103
+ GCC_except_table8125
+ GCC_except_table8129
+ GCC_except_table813
+ GCC_except_table8133
+ GCC_except_table8152
+ GCC_except_table8158
+ GCC_except_table8170
+ GCC_except_table8178
+ GCC_except_table8187
+ GCC_except_table8206
+ GCC_except_table8207
+ GCC_except_table8211
+ GCC_except_table8212
+ GCC_except_table8216
+ GCC_except_table8223
+ GCC_except_table8236
+ GCC_except_table8241
+ GCC_except_table8248
+ GCC_except_table8258
+ GCC_except_table8268
+ GCC_except_table8271
+ GCC_except_table8280
+ GCC_except_table8285
+ GCC_except_table830
+ GCC_except_table8313
+ GCC_except_table836
+ GCC_except_table8371
+ GCC_except_table8372
+ GCC_except_table8384
+ GCC_except_table8390
+ GCC_except_table8395
+ GCC_except_table8396
+ GCC_except_table843
+ GCC_except_table8430
+ GCC_except_table8435
+ GCC_except_table8441
+ GCC_except_table8453
+ GCC_except_table8466
+ GCC_except_table8479
+ GCC_except_table848
+ GCC_except_table8503
+ GCC_except_table853
+ GCC_except_table8533
+ GCC_except_table8568
+ GCC_except_table8571
+ GCC_except_table860
+ GCC_except_table8624
+ GCC_except_table8632
+ GCC_except_table864
+ GCC_except_table8647
+ GCC_except_table8649
+ GCC_except_table867
+ GCC_except_table872
+ GCC_except_table8814
+ GCC_except_table8815
+ GCC_except_table8839
+ GCC_except_table8868
+ GCC_except_table8869
+ GCC_except_table890
+ GCC_except_table9039
+ GCC_except_table9051
+ GCC_except_table9061
+ GCC_except_table9064
+ GCC_except_table9069
+ GCC_except_table9070
+ GCC_except_table9095
+ GCC_except_table9119
+ GCC_except_table9123
+ GCC_except_table9126
+ GCC_except_table9133
+ GCC_except_table9137
+ GCC_except_table9179
+ GCC_except_table919
+ GCC_except_table9193
+ GCC_except_table925
+ GCC_except_table9315
+ GCC_except_table9353
+ GCC_except_table9359
+ GCC_except_table9361
+ GCC_except_table9367
+ GCC_except_table9370
+ GCC_except_table9407
+ GCC_except_table9453
+ GCC_except_table9593
+ GCC_except_table9596
+ GCC_except_table9621
+ GCC_except_table9623
+ GCC_except_table9625
+ GCC_except_table9627
+ GCC_except_table9628
+ GCC_except_table9634
+ GCC_except_table9636
+ GCC_except_table9637
+ GCC_except_table9650
+ GCC_except_table9653
+ GCC_except_table966
+ GCC_except_table970
+ GCC_except_table9703
+ GCC_except_table9704
+ GCC_except_table9705
+ GCC_except_table9722
+ GCC_except_table9727
+ GCC_except_table9740
+ GCC_except_table9774
+ GCC_except_table9785
+ GCC_except_table9815
+ GCC_except_table9846
+ GCC_except_table9929
+ GCC_except_table9930
+ GCC_except_table9961
+ GCC_except_table9962
+ GCC_except_table9964
+ GCC_except_table9967
+ GCC_except_table9969
+ GCC_except_table9970
+ GCC_except_table9972
+ GCC_except_table9974
+ GCC_except_table9975
+ OBJC_IVAR_$_PLPrimaryResourceDataStoreKeyHelper.cvtBaseData
+ OBJC_IVAR_$_PLPrimaryResourceDataStoreKeyHelper.restrictedBaseData
+ _IMDPersistenceLibraryCore.frameworkLibrary
+ _IMSharedUtilitiesLibraryCore
+ _OBJC_CLASS_$_CNContactStoreConfiguration
+ _OBJC_CLASS_$_PLModelMigrationAction_PersistKeywordsToJournalAndFilesystem
+ _OBJC_CLASS_$_PLModelMigrationAction_RelocateUBFOriginalResourceTypes
+ _OBJC_CLASS_$_PLSearchIndexingMessagesFetcher
+ _OBJC_CLASS_$_PNContentClassifier
+ _OBJC_IVAR_$_PLAssetsdConnectionAuthorization._restrictedResourcesAccessAuthorized
+ _OBJC_IVAR_$_PLAssetsdCrashRecoveryClientAuthorization._restrictedResourcesAccessAuthorized
+ _OBJC_IVAR_$_PLFileSystemAssetImporter._keywordUUIDRemapping
+ _OBJC_IVAR_$_PLManagedKeyword._fromRebuild
+ _OBJC_IVAR_$_PLManagedKeyword._needsPersistenceUpdate
+ _OBJC_IVAR_$_PLMediaAnalysisEmbeddingSearchOptions._embeddingSearchMode
+ _OBJC_IVAR_$_PLMomentGenerationThrottle._maxDelayBetweenRuns
+ _OBJC_IVAR_$_PLMomentGenerationThrottle._maxIntervalBeforeDelayReset
+ _OBJC_IVAR_$_PLMomentGenerationThrottle._minDelayBetweenRuns
+ _OBJC_IVAR_$_PLPrimaryResourceDataStoreKeyHelper._pathManager
+ _OBJC_IVAR_$_PLSearchIndexingContext._contactStore
+ _OBJC_IVAR_$_PLSearchIndexingMessagesFetcher._displayNameCache
+ _OBJC_IVAR_$_PLSearchIndexingMessagesFetcher._indexingContext
+ _OBJC_IVAR_$_PLSearchIndexingMessagesFetcher._libraryIdentifier
+ _OBJC_IVAR_$_PLSearchIndexingMessagesFetcher._messageGUIDCache
+ _OBJC_IVAR_$_PLTextEmbeddingServiceOptions._useCache
+ _OBJC_METACLASS_$_PLModelMigrationAction_PersistKeywordsToJournalAndFilesystem
+ _OBJC_METACLASS_$_PLModelMigrationAction_RelocateUBFOriginalResourceTypes
+ _OBJC_METACLASS_$_PLSearchIndexingMessagesFetcher
+ _PFAdjustmentIdentifierGenerativeEdits
+ _PFGenerativeEditsOperationIdentifierCleanUpPrefix
+ _PFGenerativeEditsOperationIdentifierKey
+ _PFGenerativeEditsOperationIdentifierOutfill
+ _PFGenerativeEditsOperationIdentifierSpatialReframe
+ _PFGenerativeEditsSettingsOperationsKey
+ _PLCollectionShareMigrationAttributesKeyMigrationOriginatingAssetCount
+ _PLFileSystemPersistenceKeywordsKey
+ _PLFilesAppBundleID
+ _PLFilterIdentityDocumentClassificationsWithThresholds
+ _PLPathForResourceProperties
+ _PLResourceStorageTierForResourceType
+ _PLSearchLeoMessagesSenderReceiverSPLEnabled
+ _PLSearchLeoMessagesSenderReceiverSPLEnabled.enabled
+ _PLSearchLeoMessagesSenderReceiverSPLEnabled.onceToken
+ _PLSearchLeoMessagesSenderReceiverSyndicationEnabled
+ _PLSearchLeoMessagesSenderReceiverSyndicationEnabled.enabled
+ _PLSearchLeoMessagesSenderReceiverSyndicationEnabled.onceToken
+ _PLSearchUnifiedMADEmbeddingSearchEnabled
+ _PLSearchUnifiedMADEmbeddingSearchEnabled.enabled
+ _PLSearchUnifiedMADEmbeddingSearchEnabled.onceToken
+ _PhotoLibraryServicesEntitlementAllowRestrictedResourcesRead
+ __OBJC_$_CLASS_METHODS_PLCollectionShareMigrationSession
+ __OBJC_$_CLASS_METHODS_PLModelMigrationAction_PersistKeywordsToJournalAndFilesystem
+ __OBJC_$_CLASS_METHODS_PLModelMigrationAction_RelocateUBFOriginalResourceTypes
+ __OBJC_$_INSTANCE_METHODS_PLModelMigrationAction_PersistKeywordsToJournalAndFilesystem
+ __OBJC_$_INSTANCE_METHODS_PLModelMigrationAction_RelocateUBFOriginalResourceTypes
+ __OBJC_$_INSTANCE_METHODS_PLSearchIndexingMessagesFetcher
+ __OBJC_$_INSTANCE_VARIABLES_PLManagedKeyword
+ __OBJC_$_INSTANCE_VARIABLES_PLSearchIndexingMessagesFetcher
+ __OBJC_$_PROP_LIST_PLModelMigrationAction_PersistKeywordsToJournalAndFilesystem
+ __OBJC_$_PROP_LIST_PLModelMigrationAction_RelocateUBFOriginalResourceTypes
+ __OBJC_CLASS_PROTOCOLS_$_PLModelMigrationAction_PersistKeywordsToJournalAndFilesystem
+ __OBJC_CLASS_PROTOCOLS_$_PLModelMigrationAction_RelocateUBFOriginalResourceTypes
+ __OBJC_CLASS_RO_$_PLModelMigrationAction_PersistKeywordsToJournalAndFilesystem
+ __OBJC_CLASS_RO_$_PLModelMigrationAction_RelocateUBFOriginalResourceTypes
+ __OBJC_CLASS_RO_$_PLSearchIndexingMessagesFetcher
+ __OBJC_METACLASS_RO_$_PLModelMigrationAction_PersistKeywordsToJournalAndFilesystem
+ __OBJC_METACLASS_RO_$_PLModelMigrationAction_RelocateUBFOriginalResourceTypes
+ __OBJC_METACLASS_RO_$_PLSearchIndexingMessagesFetcher
+ __PLResolvedBundleIdentifierForDisplay
+ ___108-[PLModelMigrationAction_PersistKeywordsToJournalAndFilesystem performActionWithManagedObjectContext:error:]_block_invoke
+ ___109-[PLCollectionShareMigrator _continueMigrationSetupForShareUUID:silent:progress:plLibrary:completionHandler:]_block_invoke
+ ___112-[PLCollectionShare informMSASToInitiateMigrationToCPLWithIsSilentMigration:sourceAssetCount:completionHandler:]_block_invoke
+ ___114+[PLManagedKeyword rebuildAllKeywordsFromDirectoryJournalInManagedObjectContext:pathManager:keywordUUIDRemapping:]_block_invoke
+ ___116-[PLCollectionShare informMSASToCompleteMigrationToCPLWithSourceAssetCount:destinationAssetCount:completionHandler:]_block_invoke
+ ___117-[PLCollectionShareMigrator _startMigrationForSharedStreamCollectionShareWithUUID:silent:progress:completionHandler:]_block_invoke_2
+ ___117-[PLCollectionShareMigrator _startMigrationForSharedStreamCollectionShareWithUUID:silent:progress:completionHandler:]_block_invoke_3
+ ___136+[PLCollectionShareMigrationSessionPhaseSilentMigrationCleanup _revertMSASForOriginatingScopeIdentifier:photoLibrary:completionHandler:]_block_invoke
+ ___141+[PLCollectionShareMigrationSessionPhaseSilentMigrationCleanup _resetLocalStateForOriginatingScopeIdentifier:photoLibrary:completionHandler:]_block_invoke
+ ___146+[PLCollectionShareMigrationSessionPhaseSilentMigrationCleanup revertSilentMigrationForOriginatingScopeIdentifier:photoLibrary:completionHandler:]_block_invoke
+ ___146-[PLCollectionShareSharedStreamBackend informMSASToInitiateMigrationToCPLForCollectionShare:isSilentMigration:sourceAssetCount:completionHandler:]_block_invoke
+ ___147-[PLCollectionShareMigrator _pullLatestAlbumStateAndReconcileForCollectionShareWithUUID:originatingScopeIdentifier:photoLibrary:completionHandler:]_block_invoke_3
+ ___147-[PLCollectionShareMigrator _pullLatestAlbumStateAndReconcileForCollectionShareWithUUID:originatingScopeIdentifier:photoLibrary:completionHandler:]_block_invoke_4
+ ___150-[PLCollectionShareSharedStreamBackend informMSASToCompleteMigrationToCPLForCollectionShare:sourceAssetCount:destinationAssetCount:completionHandler:]_block_invoke
+ ___152-[PLSearchIndexingEngine _inq_donateSpotlightItemsByBundleID:leoDonatableItems:leoLexemeScoreUpdates:deleteIdentifiers:spotlightClientState:completion:]_block_invoke
+ ___152-[PLSearchIndexingEngine _inq_donateSpotlightItemsByBundleID:leoDonatableItems:leoLexemeScoreUpdates:deleteIdentifiers:spotlightClientState:completion:]_block_invoke_2
+ ___53-[PLSearchIndexingMessagesFetcher prefetchForAssets:]_block_invoke
+ ___56-[PLDirectoryJournal enumeratePayloadsUsingBlock:error:]_block_invoke_3
+ ___59-[PLSearchIndexingEngine pauseProcessingIncrementalUpdates]_block_invoke
+ ___60-[PLCloudSharedCommentsJob _runDaemonSideWaitUntilFinished:]_block_invoke
+ ___61-[PLCloudSharedAssetSaveJob _runDaemonSideWaitUntilFinished:]_block_invoke
+ ___71-[PLAssetsdMigrationService _ensureSystemColocatedApplicationLibraries]_block_invoke
+ ___77-[PLSearchIndexingEngine reportFeatureProcessingSnapshot:library:completion:]_block_invoke_2
+ ___79+[PLManagedAsset(Share) _directUploadFullResourcesForProxyAssets:photoLibrary:]_block_invoke
+ ___84-[PLSyndicationDeleteEngine _processDeletesForBundleID:unprefixedIdentifiers:error:]_block_invoke
+ ___84-[PLSyndicationDeleteEngine _processDeletesForBundleID:unprefixedIdentifiers:error:]_block_invoke_2
+ ___91-[PLUnmanagedAdjustment _generativeEditsRenderTypeFromAssetAdjustments:adjustmentEnvelope:]_block_invoke
+ ___96-[PLModelMigrator _importFileSystemImportAssets:intoLibrary:type:progress:keywordUUIDRemapping:]_block_invoke
+ ___96-[PLModelMigrator _importFileSystemImportAssets:intoLibrary:type:progress:keywordUUIDRemapping:]_block_invoke_2
+ ___96-[PLModelMigrator _importFileSystemImportAssets:intoLibrary:type:progress:keywordUUIDRemapping:]_block_invoke_3
+ ___98-[PLCollectionShareSharedStreamBackend checkServerForChangesForCollectionShare:completionHandler:]_block_invoke
+ ___98-[PLCollectionShareSharedStreamBackend checkServerForChangesForCollectionShare:completionHandler:]_block_invoke_2
+ ___98-[PLCollectionShareSharedStreamBackend checkServerForChangesForCollectionShare:completionHandler:]_block_invoke_3
+ ___98-[PLCollectionShareSharedStreamBackend checkServerForChangesForCollectionShare:completionHandler:]_block_invoke_4
+ ___98-[PLCollectionShareSharedStreamBackend checkServerForChangesForCollectionShare:completionHandler:]_block_invoke_5
+ ___98-[PLCollectionShareSharedStreamBackend checkServerForChangesForCollectionShare:completionHandler:]_block_invoke_6
+ ___98-[PLCollectionShareSharedStreamBackend checkServerForChangesForCollectionShare:completionHandler:]_block_invoke_7
+ ___98-[PLCollectionShareSharedStreamBackend checkServerForChangesForCollectionShare:completionHandler:]_block_invoke_8
+ ___IMDPersistenceLibraryCore_block_invoke
+ ___PLSearchLeoMessagesSenderReceiverSPLEnabled_block_invoke
+ ___PLSearchLeoMessagesSenderReceiverSyndicationEnabled_block_invoke
+ ___PLSearchUnifiedMADEmbeddingSearchEnabled_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56s64bs72r80n11_8_8_s0_t8w8_e5_v8?0l
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88bs96bs_e29_v16?0"MSASAssetCollection"8ls32l8s40l8s48l8s56l8s64l8s88l8s72l8s96l8s80l8
+ ___block_descriptor_113_e8_32s40s48s56r64r72r80r88r96r_e5_v8?0ls32l8s40l8r56l8s48l8r64l8r72l8r80l8r88l8r96l8
+ ___block_descriptor_169_e8_32s40s48s56s64s72s80s88s96s104s112s120bs128r136n11_8_8_s0_t8w8_e5_v8?0l
+ ___block_descriptor_48_e8_32r40r_e26_v16?0"IMDMessageRecord"8lr32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e42_v24?0"PLKeywordJournalEntryPayload"8^B16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48r56r_e26_v16?0"PLManagedKeyword"8ls32l8r48l8s40l8r56l8
+ ___block_descriptor_64_e8_32s40s48s56bs_e21_v16?0"MSASComment"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s_e24_v16?0"PLManagedAsset"8ls32l8s40l8s48l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e32_v16?0"NSManagedObjectContext"8ls32l8s40l8s48l8r56l8r64l8
+ ___block_descriptor_73_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_81_e8_32s40s48s56s64s72s_e35_v16?0"PLFileSystemAssetImporter"8ls32l8s40l8s48l8s56l8s64l8s72l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e17_v16?0"NSArray"8ls32l8s40l8s48l8s80l8s56l8s64l8s72l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e17_v16?0"NSError"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_89_e8_32s40s48s56s64s72s80r_e5_v8?0ls32l8s40l8s48l8r80l8s56l8s64l8s72l8
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80bs88bs_e17_v16?0"NSArray"8ls80l8s32l8s40l8s48l8s56l8s64l8s88l8s72l8
+ ___copy_helper_block_e8_136n11_8_8_s0_t8w8
+ ___destroy_helper_block_e8_136n4_8_s0
+ ___getIMContactStoreClass_block_invoke
+ ___getIMDDatabaseClass_block_invoke
+ ___getIMMessageGuidFromIMFileTransferGuidSymbolLoc_block_invoke
+ _audit_stringIMDPersistence
+ _getIMContactStoreClass
+ _getIMContactStoreClass.softClass
+ _getIMDDatabaseClass
+ _getIMDDatabaseClass.softClass
+ _getIMMessageGuidFromIMFileTransferGuidSymbolLoc
+ _getIMMessageGuidFromIMFileTransferGuidSymbolLoc.ptr
+ _objc_msgSend$UUIDStringsForKey:
+ _objc_msgSend$_addFullResourceRecordsForAssets:toBatchManager:photoLibrary:
+ _objc_msgSend$_addMessagesSenderAndReceiversFromAsset:withMessagesFetcher:
+ _objc_msgSend$_baseMADEmbeddingSearchOptionsForSearchOptions:
+ _objc_msgSend$_batchResolveDisplayNamesForHandles:
+ _objc_msgSend$_bumpLastModifiedDate:
+ _objc_msgSend$_cachedDisplayNameForHandle:
+ _objc_msgSend$_cachedMessageInfoForAsset:
+ _objc_msgSend$_continueMigrationSetupForShareUUID:silent:progress:plLibrary:completionHandler:
+ _objc_msgSend$_directUploadFullResourcesForProxyAssets:photoLibrary:
+ _objc_msgSend$_ensureSystemColocatedApplicationLibraries
+ _objc_msgSend$_generativeEditsRenderTypeFromAssetAdjustments:adjustmentEnvelope:
+ _objc_msgSend$_importFileSystemImportAssets:intoLibrary:type:progress:keywordUUIDRemapping:
+ _objc_msgSend$_inq_donateSpotlightItemsByBundleID:leoDonatableItems:leoLexemeScoreUpdates:deleteIdentifiers:spotlightClientState:completion:
+ _objc_msgSend$_isEnabled
+ _objc_msgSend$_processDeletesForBundleID:unprefixedIdentifiers:error:
+ _objc_msgSend$_recreationOptionsForMissingApplicationLibraryDatabaseAtURL:
+ _objc_msgSend$_resetLocalStateForOriginatingScopeIdentifier:photoLibrary:completionHandler:
+ _objc_msgSend$_revertMSASForOriginatingScopeIdentifier:photoLibrary:completionHandler:
+ _objc_msgSend$_runDaemonSideWaitUntilFinished:
+ _objc_msgSend$_successfulProxyAssetsFromResults:proxyMap:
+ _objc_msgSend$_supportsHighlightGeneration
+ _objc_msgSend$addContentFromAsset:forPropertySets:withIndexingContext:fetchHelper:embeddingsFetcher:messagesFetcher:
+ _objc_msgSend$addLexemeWithCategory:text:localizationKey:additionalVariants:identifier:
+ _objc_msgSend$addLexemeWithCategory:text:localizationKey:identifier:
+ _objc_msgSend$assetsdLocallyProcessAddedCommentsAndWait:assetGUID:albumGUID:info:libraryServicesManager:
+ _objc_msgSend$assetsdProcessMetadataForAssetCollectionsAndWait:inAlbum:personID:info:libraryServicesManager:
+ _objc_msgSend$bumpLastModifiedDateIfValidWithDate:
+ _objc_msgSend$cancelMigrationToCPLForAlbumWithGUID:personID:clientVersion:completionBlock:
+ _objc_msgSend$canonicalizedURIString
+ _objc_msgSend$chatRecord
+ _objc_msgSend$checkServerForChangesForCollectionShare:completionHandler:
+ _objc_msgSend$checkServerForChangesWithCompletionHandler:
+ _objc_msgSend$completeMigrationToCPLForAlbumWithGUID:personID:clientVersion:sourceAssetCount:destinationAssetCount:completionBlock:
+ _objc_msgSend$embeddingSearchMode
+ _objc_msgSend$ensureApplicationLibraryExistsWithContainerIdentifier:uuid:name:error:
+ _objc_msgSend$failMigrationToCPLForAlbumWithGUID:migrationError:personID:clientVersion:completionBlock:
+ _objc_msgSend$fetchMessageRecordWithGUID:excludeRecoverableMessages:completionHandler:
+ _objc_msgSend$handleRecord
+ _objc_msgSend$handleRecords
+ _objc_msgSend$hasActiveSilentMigration
+ _objc_msgSend$highPrecision
+ _objc_msgSend$highRecall
+ _objc_msgSend$iCloudLibraryClientNeedsToVerifyTerms
+ _objc_msgSend$identityDocumentNodeThresholdsForContentClassificationVersion:
+ _objc_msgSend$informMSASToCompleteMigrationToCPLForCollectionShare:sourceAssetCount:destinationAssetCount:completionHandler:
+ _objc_msgSend$informMSASToCompleteMigrationToCPLWithSourceAssetCount:destinationAssetCount:completionHandler:
+ _objc_msgSend$informMSASToInitiateMigrationToCPLForCollectionShare:isSilentMigration:sourceAssetCount:completionHandler:
+ _objc_msgSend$informMSASToInitiateMigrationToCPLWithIsSilentMigration:sourceAssetCount:completionHandler:
+ _objc_msgSend$initWithConfiguration:
+ _objc_msgSend$initWithDomain:containerIdentifier:uuid:name:
+ _objc_msgSend$initWithLibraryIdentifier:indexingContext:
+ _objc_msgSend$initWithName:canDelayAnyQOS:singleThreadedMode:minDelayBetweenRuns:maxDelayBetweenRuns:timeProvider:targetQueue:target:
+ _objc_msgSend$initiateMigrationToCPLForAlbumWithGUID:personID:isSilentMigration:clientVersion:sourceAssetCount:completionBlock:
+ _objc_msgSend$isFromMe
+ _objc_msgSend$isRetryableMigrationError:
+ _objc_msgSend$keywordUUIDRemapping
+ _objc_msgSend$lastAddressedHandle
+ _objc_msgSend$leoDonatableItemForManagedObject:partialUpdateMask:indexingContext:fetchHelper:embeddingsFetcher:messagesFetcher:
+ _objc_msgSend$libraryCreateOptionsForApplicationLibraryWithContainerIdentifier:
+ _objc_msgSend$migrationOriginatingAssetCount
+ _objc_msgSend$numberOfProbes
+ _objc_msgSend$oldestAndNewestDatesForAssetsWithFilter:useDayGroupAssets:error:
+ _objc_msgSend$pause
+ _objc_msgSend$pauseProcessingIncrementalUpdates
+ _objc_msgSend$predicateForContactsMatchingHandleStrings:
+ _objc_msgSend$prefetchForAssets:
+ _objc_msgSend$queryEmbedding
+ _objc_msgSend$rebuildAllKeywordsFromDirectoryJournalInManagedObjectContext:pathManager:keywordUUIDRemapping:
+ _objc_msgSend$receiverDisplayNamesForAsset:
+ _objc_msgSend$refreshContentOfAlbumWithGUID:resetSync:personID:completionBlock:
+ _objc_msgSend$revertSilentMigrationForOriginatingScopeIdentifier:photoLibrary:completionHandler:
+ _objc_msgSend$runDaemonSideAndWait
+ _objc_msgSend$searchWithQueryTexts:photoLibraryURL:options:error:
+ _objc_msgSend$searchableItemForObject:fetchHelper:partialUpdateMask:libraryIdentifier:indexingContext:embeddingsFetcher:messagesFetcher:
+ _objc_msgSend$senderDisplayNameForAsset:
+ _objc_msgSend$setCheckSafety:
+ _objc_msgSend$setEmbeddingSourceTypes:
+ _objc_msgSend$setIncludeAcceptedIntroductions:
+ _objc_msgSend$setKeywordUUIDRemapping:
+ _objc_msgSend$setKeywordsFromPersistedAttributes:keywordUUIDRemapping:
+ _objc_msgSend$setLastModifiedDateIfNeeded:fromMigration:
+ _objc_msgSend$setMigrationOriginatingAssetCount:
+ _objc_msgSend$setSearchMode:
+ _objc_msgSend$setUUIDStrings:forKey:
+ _objc_msgSend$setUseCache:
+ _objc_msgSend$setUseInProcessMapperExclusively:
+ _objc_msgSend$shouldExcludeAssetFromLibrarySummary:
+ _objc_msgSend$sortedResults
+ _objc_msgSend$synchronizeWithPersistedFileSystemAttributesWithKeywordUUIDRemapping:
+ _objc_msgSend$synchronousDatabase
+ _objc_msgSend$unarchiveMigrationToCPLForAlbumWithGUID:personID:clientVersion:completionBlock:
+ _objc_msgSend$uploadedBatch
+ _objc_msgSend$useCache
+ _objc_msgSend$validateAndCleanupID:
+ _objc_msgSend$validateContinerIdentifier:
+ _softlink_IMMessageGuidFromIMFileTransferGuid
- +[PLDayGroupPhotosHighlightTitleGenerator assetsToUseForDayGroupHighlight:withFilter:]
- +[PLDayPhotosHighlightTitleGenerator assetsToUseForDayHighlight:withFilter:]
- +[PLMediaAnalysisEmbeddingSearch _searchWithEmbeddings:photoLibraryURL:searchOptions:numberOfProbes:error:]
- +[PLSearchManagedObjectUtilities leoDonatableItemForManagedObject:partialUpdateMask:indexingContext:fetchHelper:embeddingsFetcher:]
- +[PLSearchManagedObjectUtilities psiObjectForIdentifierRequiringAdditionalWork:entity:]
- +[PLSearchManagedObjectUtilities psiObjectForObject:fetchHelper:partialUpdateMask:indexingContext:]
- +[PLSearchManagedObjectUtilities searchableItemForObject:fetchHelper:partialUpdateMask:libraryIdentifier:indexingContext:embeddingsFetcher:]
- +[PSIAlbumTranslator psiCollectionFromAlbum:indexingContext:]
- +[PSIAssetTranslator _addContentClassificationToAsset:nodeLabel:nodeSynonyms:nodeSceneID:]
- +[PSIAssetTranslator _appendAssetTextDataToAsset:forAsset:]
- +[PSIAssetTranslator _appendAudioClassificationToAsset:forAsset:]
- +[PSIAssetTranslator _appendContentClassificationsToAsset:sceneTaxonomyProvider:forAsset:fetchHelper:]
- +[PSIAssetTranslator _appendContributorToAsset:forAsset:]
- +[PSIAssetTranslator _appendDateCreatedToAsset:indexingContext:forAsset:]
- +[PSIAssetTranslator _appendExifDataToAsset:forAsset:]
- +[PSIAssetTranslator _appendFavoriteToAsset:forAsset:]
- +[PSIAssetTranslator _appendFilenameToAsset:forAsset:]
- +[PSIAssetTranslator _appendGEODataToAsset:forAsset:countrySynonymProvider:]
- +[PSIAssetTranslator _appendGraphDataToAsset:forMomentFromFetchHelper:hasValidReverseLocationData:indexingContext:]
- +[PSIAssetTranslator _appendHumanActionsToAsset:forAsset:fetchHelper:]
- +[PSIAssetTranslator _appendKeywords:toAsset:]
- +[PSIAssetTranslator _appendLibraryScopeToAsset:forAsset:]
- +[PSIAssetTranslator _appendMediaTypesToAsset:forAsset:]
- +[PSIAssetTranslator _appendOCRTextForAsset:documentObservation:]
- +[PSIAssetTranslator _appendPerson:fetchHelper:toAsset:]
- +[PSIAssetTranslator _appendPersonsAndPetsToAsset:forAsset:fetchHelper:]
- +[PSIAssetTranslator _appendPet:fetchHelper:toAsset:]
- +[PSIAssetTranslator _appendPrivateEncryptedComputeScenes:forAsset:fetchHelper:csuTaxonomyObjectStore:locale:]
- +[PSIAssetTranslator _appendSavedFromAppToAsset:forAsset:]
- +[PSIAssetTranslator _appendSceneClassificationsToAsset:sceneTaxonomyProvider:forAsset:fetchHelper:]
- +[PSIAssetTranslator _appendStickerSuggestionsToAsset:fetchHelper:sceneTaxonomyProvider:forAsset:]
- +[PSIAssetTranslator _appendStyleCastToAsset:forAsset:]
- +[PSIAssetTranslator _appendUtilityTypesToAsset:forAsset:indexingContext:]
- +[PSIAssetTranslator _containsPersonWithSceneTaxonomyProvider:forAsset:]
- +[PSIAssetTranslator _nameForContributor:]
- +[PSIAssetTranslator psiAssetFromAsset:fetchHelper:propertySets:indexingContext:documentObservation:]
- +[PSICollectionShareTranslator psiCollectionFromCollectionShare:indexingContext:]
- +[PSIMemoryTranslator _endDateForMemory:]
- +[PSIMemoryTranslator _fetchCuratedAssetsForMemory:sortedAscending:]
- +[PSIMemoryTranslator _startDateForMemory:]
- +[PSIMemoryTranslator psiCollectionFromMemory:indexingContext:]
- +[PSISearchEntityTranslator _indexCategoryForSearchEntityType:]
- +[PSISearchEntityTranslator _lookupIdentifierForSearchEntity:]
- +[PSISearchEntityTranslator psiGroupFromSearchEntity:]
- +[PSISearchEntityTranslator zeroScorePSIGroupFromLabel:type:identifier:]
- -[PLCollectionShare informMSASToCompleteMigrationToCPLWithCompletionHandler:]
- -[PLCollectionShare informMSASToInitiateMigrationToCPLWithIsSilentMigration:completionHandler:]
- -[PLCollectionShareCPLBackend informMSASToCompleteMigrationToCPLForCollectionShare:completionHandler:]
- -[PLCollectionShareCPLBackend informMSASToInitiateMigrationToCPLForCollectionShare:isSilentMigration:completionHandler:]
- -[PLCollectionShareMigrationSessionPhaseSilentMigrationCleanup _performLocalCleanupWithCompletionHandler:]
- -[PLCollectionShareMigrationSessionPhaseSilentMigrationCleanup _performServerCleanupWithCompletionHandler:]
- -[PLCollectionShareSharedStreamBackend informMSASToCompleteMigrationToCPLForCollectionShare:completionHandler:]
- -[PLCollectionShareSharedStreamBackend informMSASToInitiateMigrationToCPLForCollectionShare:isSilentMigration:completionHandler:]
- -[PLLeoDonatableItem(Asset) addContentFromAsset:forPropertySets:withIndexingContext:fetchHelper:embeddingsFetcher:]
- -[PLManagedAsset synchronizeWithPersistedFileSystemAttributes]
- -[PLModelMigrator _importFileSystemImportAssets:intoLibrary:type:progress:]
- -[PLMomentGenerationThrottle initWithName:canDelayAnyQOS:singleThreadedMode:timeProvider:targetQueue:target:]
- -[PLResourceModelValidationError init]
- -[PLSearchIndexingEngine _inq_donatePSIObjectsByType:spotlightItemsByBundleID:leoDonatableItems:leoLexemeScoreUpdates:deleteIdentifiers:spotlightClientState:completion:]
- -[PLSearchIndexingEngine _safePerformBlockWithPSIDatabase:sync:]
- -[PLSearchIndexingEngine safePerformBlockAndWaitWithPSIDatabase:]
- -[PLSearchIndexingEngine safePerformBlockWithPSIDatabase:]
- -[PLSearchIndexingEngine supportsPSI]
- -[PLSyndicationDeleteEngine _deleteSyndicationAssetsWithBundleID:syndicationIdentifiers:deleteCount:]
- -[PLSyndicationDeleteEngine _processDeletesForBundleID:unprefixedIdentifiers:]
- GCC_except_table10008
- GCC_except_table10015
- GCC_except_table10027
- GCC_except_table10029
- GCC_except_table1003
- GCC_except_table10054
- GCC_except_table10058
- GCC_except_table10061
- GCC_except_table10071
- GCC_except_table10080
- GCC_except_table10153
- GCC_except_table10172
- GCC_except_table10186
- GCC_except_table10190
- GCC_except_table10202
- GCC_except_table10226
- GCC_except_table10228
- GCC_except_table10242
- GCC_except_table10244
- GCC_except_table10288
- GCC_except_table10293
- GCC_except_table10308
- GCC_except_table10318
- GCC_except_table10330
- GCC_except_table10339
- GCC_except_table10347
- GCC_except_table10366
- GCC_except_table10368
- GCC_except_table10381
- GCC_except_table10470
- GCC_except_table10476
- GCC_except_table10478
- GCC_except_table10482
- GCC_except_table10484
- GCC_except_table10490
- GCC_except_table10494
- GCC_except_table10496
- GCC_except_table10502
- GCC_except_table10538
- GCC_except_table10558
- GCC_except_table10589
- GCC_except_table1061
- GCC_except_table10643
- GCC_except_table10694
- GCC_except_table10700
- GCC_except_table10702
- GCC_except_table10716
- GCC_except_table10722
- GCC_except_table10724
- GCC_except_table10735
- GCC_except_table10739
- GCC_except_table10742
- GCC_except_table10762
- GCC_except_table1082
- GCC_except_table10876
- GCC_except_table10920
- GCC_except_table11002
- GCC_except_table11003
- GCC_except_table11006
- GCC_except_table11007
- GCC_except_table11010
- GCC_except_table11011
- GCC_except_table11013
- GCC_except_table11019
- GCC_except_table11023
- GCC_except_table11025
- GCC_except_table11027
- GCC_except_table11029
- GCC_except_table11031
- GCC_except_table11033
- GCC_except_table11035
- GCC_except_table11037
- GCC_except_table11039
- GCC_except_table11041
- GCC_except_table11043
- GCC_except_table11046
- GCC_except_table11049
- GCC_except_table11053
- GCC_except_table11056
- GCC_except_table11059
- GCC_except_table11061
- GCC_except_table11063
- GCC_except_table11065
- GCC_except_table11069
- GCC_except_table11073
- GCC_except_table11076
- GCC_except_table11079
- GCC_except_table11082
- GCC_except_table11084
- GCC_except_table11090
- GCC_except_table11094
- GCC_except_table11098
- GCC_except_table11104
- GCC_except_table11106
- GCC_except_table11108
- GCC_except_table11109
- GCC_except_table11111
- GCC_except_table11112
- GCC_except_table11114
- GCC_except_table11115
- GCC_except_table11116
- GCC_except_table11118
- GCC_except_table11119
- GCC_except_table11121
- GCC_except_table11122
- GCC_except_table11126
- GCC_except_table11135
- GCC_except_table11141
- GCC_except_table11213
- GCC_except_table11217
- GCC_except_table11228
- GCC_except_table11298
- GCC_except_table1132
- GCC_except_table11380
- GCC_except_table11421
- GCC_except_table11433
- GCC_except_table11533
- GCC_except_table11538
- GCC_except_table1155
- GCC_except_table11561
- GCC_except_table1161
- GCC_except_table11614
- GCC_except_table11672
- GCC_except_table1168
- GCC_except_table1188
- GCC_except_table1189
- GCC_except_table11890
- GCC_except_table11931
- GCC_except_table1196
- GCC_except_table1197
- GCC_except_table1203
- GCC_except_table12157
- GCC_except_table12190
- GCC_except_table12214
- GCC_except_table12215
- GCC_except_table12216
- GCC_except_table12217
- GCC_except_table12218
- GCC_except_table12222
- GCC_except_table12237
- GCC_except_table1225
- GCC_except_table12320
- GCC_except_table12332
- GCC_except_table12338
- GCC_except_table12343
- GCC_except_table12348
- GCC_except_table12353
- GCC_except_table12357
- GCC_except_table12361
- GCC_except_table12371
- GCC_except_table12381
- GCC_except_table12386
- GCC_except_table12391
- GCC_except_table12400
- GCC_except_table12405
- GCC_except_table12421
- GCC_except_table1243
- GCC_except_table12435
- GCC_except_table12439
- GCC_except_table12450
- GCC_except_table12536
- GCC_except_table12541
- GCC_except_table12544
- GCC_except_table12551
- GCC_except_table12553
- GCC_except_table12555
- GCC_except_table12557
- GCC_except_table12559
- GCC_except_table12561
- GCC_except_table12563
- GCC_except_table12566
- GCC_except_table12568
- GCC_except_table12577
- GCC_except_table12586
- GCC_except_table12589
- GCC_except_table12593
- GCC_except_table12598
- GCC_except_table12608
- GCC_except_table12644
- GCC_except_table12646
- GCC_except_table12648
- GCC_except_table12650
- GCC_except_table12653
- GCC_except_table12655
- GCC_except_table12657
- GCC_except_table12659
- GCC_except_table12664
- GCC_except_table12669
- GCC_except_table12673
- GCC_except_table12675
- GCC_except_table12678
- GCC_except_table12680
- GCC_except_table12682
- GCC_except_table12684
- GCC_except_table12686
- GCC_except_table12698
- GCC_except_table12704
- GCC_except_table12735
- GCC_except_table12770
- GCC_except_table12799
- GCC_except_table1287
- GCC_except_table12885
- GCC_except_table12976
- GCC_except_table12993
- GCC_except_table12995
- GCC_except_table13014
- GCC_except_table13016
- GCC_except_table13020
- GCC_except_table1303
- GCC_except_table13034
- GCC_except_table13038
- GCC_except_table13045
- GCC_except_table13050
- GCC_except_table13061
- GCC_except_table13066
- GCC_except_table1310
- GCC_except_table13146
- GCC_except_table13162
- GCC_except_table13167
- GCC_except_table1317
- GCC_except_table13171
- GCC_except_table13188
- GCC_except_table13190
- GCC_except_table13197
- GCC_except_table13199
- GCC_except_table13201
- GCC_except_table13203
- GCC_except_table13207
- GCC_except_table13269
- GCC_except_table13281
- GCC_except_table13300
- GCC_except_table1334
- GCC_except_table13362
- GCC_except_table13475
- GCC_except_table13496
- GCC_except_table13503
- GCC_except_table13507
- GCC_except_table13554
- GCC_except_table13634
- GCC_except_table13642
- GCC_except_table13661
- GCC_except_table13673
- GCC_except_table13727
- GCC_except_table13752
- GCC_except_table13755
- GCC_except_table13764
- GCC_except_table13768
- GCC_except_table13780
- GCC_except_table1379
- GCC_except_table13829
- GCC_except_table13847
- GCC_except_table13853
- GCC_except_table13875
- GCC_except_table13969
- GCC_except_table14024
- GCC_except_table14035
- GCC_except_table14039
- GCC_except_table14054
- GCC_except_table14062
- GCC_except_table14086
- GCC_except_table14096
- GCC_except_table14098
- GCC_except_table14100
- GCC_except_table14119
- GCC_except_table1419
- GCC_except_table14210
- GCC_except_table14215
- GCC_except_table14238
- GCC_except_table14251
- GCC_except_table14253
- GCC_except_table14255
- GCC_except_table1430
- GCC_except_table14361
- GCC_except_table14362
- GCC_except_table14366
- GCC_except_table14399
- GCC_except_table1440
- GCC_except_table14420
- GCC_except_table14431
- GCC_except_table14432
- GCC_except_table14433
- GCC_except_table14434
- GCC_except_table14435
- GCC_except_table14436
- GCC_except_table14437
- GCC_except_table14438
- GCC_except_table14439
- GCC_except_table14508
- GCC_except_table14514
- GCC_except_table14529
- GCC_except_table14537
- GCC_except_table14540
- GCC_except_table14545
- GCC_except_table14583
- GCC_except_table14587
- GCC_except_table14591
- GCC_except_table14598
- GCC_except_table14602
- GCC_except_table14613
- GCC_except_table14649
- GCC_except_table14705
- GCC_except_table1471
- GCC_except_table14713
- GCC_except_table14780
- GCC_except_table1479
- GCC_except_table14803
- GCC_except_table14827
- GCC_except_table14971
- GCC_except_table1499
- GCC_except_table15052
- GCC_except_table1510
- GCC_except_table15114
- GCC_except_table15131
- GCC_except_table15138
- GCC_except_table15141
- GCC_except_table15142
- GCC_except_table1515
- GCC_except_table15161
- GCC_except_table15250
- GCC_except_table15257
- GCC_except_table15259
- GCC_except_table15263
- GCC_except_table15265
- GCC_except_table15272
- GCC_except_table15450
- GCC_except_table15480
- GCC_except_table15536
- GCC_except_table1556
- GCC_except_table1563
- GCC_except_table15706
- GCC_except_table15716
- GCC_except_table15726
- GCC_except_table15728
- GCC_except_table15754
- GCC_except_table15773
- GCC_except_table15784
- GCC_except_table15811
- GCC_except_table15855
- GCC_except_table15856
- GCC_except_table159
- GCC_except_table15922
- GCC_except_table15926
- GCC_except_table15929
- GCC_except_table15932
- GCC_except_table16090
- GCC_except_table1610
- GCC_except_table16120
- GCC_except_table16147
- GCC_except_table16155
- GCC_except_table16161
- GCC_except_table16162
- GCC_except_table16164
- GCC_except_table16170
- GCC_except_table16174
- GCC_except_table16177
- GCC_except_table16181
- GCC_except_table16183
- GCC_except_table16187
- GCC_except_table16190
- GCC_except_table16193
- GCC_except_table1621
- GCC_except_table16239
- GCC_except_table16254
- GCC_except_table16257
- GCC_except_table16274
- GCC_except_table16291
- GCC_except_table16293
- GCC_except_table1630
- GCC_except_table16300
- GCC_except_table16304
- GCC_except_table16401
- GCC_except_table16405
- GCC_except_table16407
- GCC_except_table16409
- GCC_except_table16432
- GCC_except_table16433
- GCC_except_table16440
- GCC_except_table16449
- GCC_except_table16463
- GCC_except_table16467
- GCC_except_table16480
- GCC_except_table16539
- GCC_except_table16541
- GCC_except_table16632
- GCC_except_table16693
- GCC_except_table16706
- GCC_except_table16727
- GCC_except_table16819
- GCC_except_table16839
- GCC_except_table16845
- GCC_except_table16850
- GCC_except_table16857
- GCC_except_table16885
- GCC_except_table16897
- GCC_except_table16942
- GCC_except_table17005
- GCC_except_table17010
- GCC_except_table17018
- GCC_except_table17028
- GCC_except_table17040
- GCC_except_table17054
- GCC_except_table17060
- GCC_except_table17070
- GCC_except_table17083
- GCC_except_table17093
- GCC_except_table17103
- GCC_except_table17139
- GCC_except_table17141
- GCC_except_table172
- GCC_except_table17202
- GCC_except_table17205
- GCC_except_table17252
- GCC_except_table17263
- GCC_except_table17283
- GCC_except_table17294
- GCC_except_table17356
- GCC_except_table17366
- GCC_except_table17379
- GCC_except_table17382
- GCC_except_table17385
- GCC_except_table17392
- GCC_except_table17394
- GCC_except_table17395
- GCC_except_table17397
- GCC_except_table17429
- GCC_except_table17435
- GCC_except_table17519
- GCC_except_table17555
- GCC_except_table17568
- GCC_except_table17620
- GCC_except_table17638
- GCC_except_table17678
- GCC_except_table17683
- GCC_except_table17722
- GCC_except_table17730
- GCC_except_table17733
- GCC_except_table17745
- GCC_except_table1775
- GCC_except_table17770
- GCC_except_table17803
- GCC_except_table17804
- GCC_except_table17805
- GCC_except_table1781
- GCC_except_table17840
- GCC_except_table17850
- GCC_except_table17891
- GCC_except_table17902
- GCC_except_table17916
- GCC_except_table17932
- GCC_except_table17933
- GCC_except_table17958
- GCC_except_table17977
- GCC_except_table18013
- GCC_except_table18015
- GCC_except_table18020
- GCC_except_table18023
- GCC_except_table18029
- GCC_except_table18092
- GCC_except_table18125
- GCC_except_table18131
- GCC_except_table18180
- GCC_except_table18312
- GCC_except_table18371
- GCC_except_table18382
- GCC_except_table18401
- GCC_except_table18441
- GCC_except_table18452
- GCC_except_table18466
- GCC_except_table18475
- GCC_except_table18489
- GCC_except_table18490
- GCC_except_table18530
- GCC_except_table18559
- GCC_except_table18562
- GCC_except_table18624
- GCC_except_table18642
- GCC_except_table18667
- GCC_except_table18675
- GCC_except_table18682
- GCC_except_table18683
- GCC_except_table18695
- GCC_except_table18699
- GCC_except_table18700
- GCC_except_table18703
- GCC_except_table18710
- GCC_except_table18716
- GCC_except_table18719
- GCC_except_table18771
- GCC_except_table18788
- GCC_except_table18815
- GCC_except_table18954
- GCC_except_table18994
- GCC_except_table18999
- GCC_except_table19002
- GCC_except_table19023
- GCC_except_table19026
- GCC_except_table19031
- GCC_except_table19032
- GCC_except_table19040
- GCC_except_table19043
- GCC_except_table19052
- GCC_except_table19055
- GCC_except_table19058
- GCC_except_table19066
- GCC_except_table19069
- GCC_except_table19072
- GCC_except_table19075
- GCC_except_table19083
- GCC_except_table19087
- GCC_except_table19092
- GCC_except_table19099
- GCC_except_table19102
- GCC_except_table19111
- GCC_except_table19129
- GCC_except_table19133
- GCC_except_table19137
- GCC_except_table19145
- GCC_except_table19155
- GCC_except_table19156
- GCC_except_table19160
- GCC_except_table19165
- GCC_except_table19168
- GCC_except_table19172
- GCC_except_table19177
- GCC_except_table19181
- GCC_except_table19184
- GCC_except_table19187
- GCC_except_table19190
- GCC_except_table19193
- GCC_except_table19200
- GCC_except_table19203
- GCC_except_table19214
- GCC_except_table19218
- GCC_except_table19222
- GCC_except_table193
- GCC_except_table19320
- GCC_except_table19326
- GCC_except_table19339
- GCC_except_table19340
- GCC_except_table19344
- GCC_except_table19345
- GCC_except_table19357
- GCC_except_table19370
- GCC_except_table19482
- GCC_except_table19494
- GCC_except_table19513
- GCC_except_table1953
- GCC_except_table1958
- GCC_except_table19588
- GCC_except_table19591
- GCC_except_table19598
- GCC_except_table19601
- GCC_except_table19609
- GCC_except_table19630
- GCC_except_table19636
- GCC_except_table19640
- GCC_except_table19646
- GCC_except_table19656
- GCC_except_table19661
- GCC_except_table19671
- GCC_except_table19672
- GCC_except_table19675
- GCC_except_table19676
- GCC_except_table19679
- GCC_except_table19744
- GCC_except_table19807
- GCC_except_table19824
- GCC_except_table19895
- GCC_except_table19897
- GCC_except_table19907
- GCC_except_table19916
- GCC_except_table19918
- GCC_except_table19922
- GCC_except_table19924
- GCC_except_table19926
- GCC_except_table19940
- GCC_except_table20080
- GCC_except_table20091
- GCC_except_table20128
- GCC_except_table20134
- GCC_except_table20143
- GCC_except_table20169
- GCC_except_table20203
- GCC_except_table20212
- GCC_except_table20218
- GCC_except_table20221
- GCC_except_table20226
- GCC_except_table20235
- GCC_except_table20241
- GCC_except_table20247
- GCC_except_table20258
- GCC_except_table20412
- GCC_except_table20416
- GCC_except_table20451
- GCC_except_table20455
- GCC_except_table20459
- GCC_except_table20461
- GCC_except_table20489
- GCC_except_table20529
- GCC_except_table20533
- GCC_except_table20537
- GCC_except_table20541
- GCC_except_table20545
- GCC_except_table20549
- GCC_except_table20553
- GCC_except_table20557
- GCC_except_table20561
- GCC_except_table20565
- GCC_except_table20569
- GCC_except_table20573
- GCC_except_table20577
- GCC_except_table20581
- GCC_except_table20585
- GCC_except_table20589
- GCC_except_table20593
- GCC_except_table20597
- GCC_except_table20601
- GCC_except_table20605
- GCC_except_table20609
- GCC_except_table20646
- GCC_except_table20649
- GCC_except_table20654
- GCC_except_table20657
- GCC_except_table20683
- GCC_except_table20687
- GCC_except_table20688
- GCC_except_table20689
- GCC_except_table20695
- GCC_except_table20708
- GCC_except_table20774
- GCC_except_table20818
- GCC_except_table20825
- GCC_except_table20831
- GCC_except_table20857
- GCC_except_table20864
- GCC_except_table20871
- GCC_except_table20883
- GCC_except_table20887
- GCC_except_table20891
- GCC_except_table20895
- GCC_except_table20910
- GCC_except_table20938
- GCC_except_table20963
- GCC_except_table20966
- GCC_except_table21012
- GCC_except_table21029
- GCC_except_table21047
- GCC_except_table21051
- GCC_except_table21057
- GCC_except_table21061
- GCC_except_table21062
- GCC_except_table21064
- GCC_except_table21072
- GCC_except_table21074
- GCC_except_table21082
- GCC_except_table21085
- GCC_except_table21086
- GCC_except_table21087
- GCC_except_table21088
- GCC_except_table21090
- GCC_except_table21092
- GCC_except_table21098
- GCC_except_table21102
- GCC_except_table21106
- GCC_except_table21112
- GCC_except_table21114
- GCC_except_table21116
- GCC_except_table21118
- GCC_except_table21120
- GCC_except_table21122
- GCC_except_table21124
- GCC_except_table21142
- GCC_except_table21270
- GCC_except_table21277
- GCC_except_table21290
- GCC_except_table21296
- GCC_except_table21314
- GCC_except_table21416
- GCC_except_table21490
- GCC_except_table215
- GCC_except_table21506
- GCC_except_table21516
- GCC_except_table21576
- GCC_except_table21691
- GCC_except_table21692
- GCC_except_table21704
- GCC_except_table21722
- GCC_except_table21724
- GCC_except_table21731
- GCC_except_table21756
- GCC_except_table21774
- GCC_except_table2182
- GCC_except_table21822
- GCC_except_table21829
- GCC_except_table21845
- GCC_except_table21862
- GCC_except_table21866
- GCC_except_table21871
- GCC_except_table21932
- GCC_except_table21948
- GCC_except_table21965
- GCC_except_table21970
- GCC_except_table21984
- GCC_except_table21986
- GCC_except_table2201
- GCC_except_table22023
- GCC_except_table2206
- GCC_except_table22083
- GCC_except_table22097
- GCC_except_table22128
- GCC_except_table2214
- GCC_except_table22145
- GCC_except_table2217
- GCC_except_table22182
- GCC_except_table22195
- GCC_except_table22198
- GCC_except_table22255
- GCC_except_table22344
- GCC_except_table22390
- GCC_except_table22394
- GCC_except_table22396
- GCC_except_table22398
- GCC_except_table2242
- GCC_except_table22425
- GCC_except_table2247
- GCC_except_table22497
- GCC_except_table22498
- GCC_except_table22538
- GCC_except_table22571
- GCC_except_table22575
- GCC_except_table2261
- GCC_except_table22616
- GCC_except_table2263
- GCC_except_table22685
- GCC_except_table2285
- GCC_except_table2291
- GCC_except_table2307
- GCC_except_table23096
- GCC_except_table2319
- GCC_except_table23395
- GCC_except_table23407
- GCC_except_table23415
- GCC_except_table23462
- GCC_except_table23466
- GCC_except_table23522
- GCC_except_table23534
- GCC_except_table23550
- GCC_except_table23651
- GCC_except_table23660
- GCC_except_table23690
- GCC_except_table23752
- GCC_except_table23767
- GCC_except_table23834
- GCC_except_table23852
- GCC_except_table23859
- GCC_except_table23883
- GCC_except_table2400
- GCC_except_table24058
- GCC_except_table24076
- GCC_except_table24121
- GCC_except_table24155
- GCC_except_table24187
- GCC_except_table24232
- GCC_except_table24233
- GCC_except_table24299
- GCC_except_table24302
- GCC_except_table24319
- GCC_except_table24324
- GCC_except_table24332
- GCC_except_table24341
- GCC_except_table24347
- GCC_except_table24354
- GCC_except_table24370
- GCC_except_table24377
- GCC_except_table24404
- GCC_except_table2450
- GCC_except_table24593
- GCC_except_table24597
- GCC_except_table24604
- GCC_except_table24605
- GCC_except_table24606
- GCC_except_table24607
- GCC_except_table24610
- GCC_except_table24611
- GCC_except_table24613
- GCC_except_table24614
- GCC_except_table24615
- GCC_except_table24617
- GCC_except_table24622
- GCC_except_table24627
- GCC_except_table24628
- GCC_except_table24664
- GCC_except_table24667
- GCC_except_table24690
- GCC_except_table24693
- GCC_except_table24694
- GCC_except_table24699
- GCC_except_table2470
- GCC_except_table24704
- GCC_except_table24708
- GCC_except_table24771
- GCC_except_table24778
- GCC_except_table24780
- GCC_except_table24782
- GCC_except_table24784
- GCC_except_table24786
- GCC_except_table24794
- GCC_except_table24796
- GCC_except_table2480
- GCC_except_table24810
- GCC_except_table24836
- GCC_except_table24839
- GCC_except_table24846
- GCC_except_table24848
- GCC_except_table24850
- GCC_except_table24852
- GCC_except_table24856
- GCC_except_table24860
- GCC_except_table24876
- GCC_except_table24883
- GCC_except_table24887
- GCC_except_table24897
- GCC_except_table24908
- GCC_except_table24910
- GCC_except_table24912
- GCC_except_table24920
- GCC_except_table24924
- GCC_except_table24928
- GCC_except_table24932
- GCC_except_table24934
- GCC_except_table24946
- GCC_except_table24970
- GCC_except_table24986
- GCC_except_table25004
- GCC_except_table25008
- GCC_except_table25033
- GCC_except_table25035
- GCC_except_table25037
- GCC_except_table25060
- GCC_except_table25063
- GCC_except_table25066
- GCC_except_table25068
- GCC_except_table25122
- GCC_except_table25184
- GCC_except_table25188
- GCC_except_table25191
- GCC_except_table25194
- GCC_except_table25201
- GCC_except_table25227
- GCC_except_table25230
- GCC_except_table25241
- GCC_except_table25244
- GCC_except_table25257
- GCC_except_table25262
- GCC_except_table25266
- GCC_except_table25269
- GCC_except_table25290
- GCC_except_table25299
- GCC_except_table25302
- GCC_except_table25305
- GCC_except_table25312
- GCC_except_table25320
- GCC_except_table25321
- GCC_except_table25329
- GCC_except_table25419
- GCC_except_table25420
- GCC_except_table25421
- GCC_except_table25422
- GCC_except_table25426
- GCC_except_table25430
- GCC_except_table25431
- GCC_except_table25432
- GCC_except_table25435
- GCC_except_table25465
- GCC_except_table25473
- GCC_except_table25477
- GCC_except_table2549
- GCC_except_table25505
- GCC_except_table25520
- GCC_except_table25554
- GCC_except_table25558
- GCC_except_table2556
- GCC_except_table25566
- GCC_except_table25582
- GCC_except_table25602
- GCC_except_table25606
- GCC_except_table25637
- GCC_except_table25643
- GCC_except_table25712
- GCC_except_table25730
- GCC_except_table25739
- GCC_except_table25742
- GCC_except_table25745
- GCC_except_table25748
- GCC_except_table25754
- GCC_except_table25757
- GCC_except_table25760
- GCC_except_table25763
- GCC_except_table25766
- GCC_except_table25769
- GCC_except_table25772
- GCC_except_table25775
- GCC_except_table25778
- GCC_except_table25781
- GCC_except_table25784
- GCC_except_table25787
- GCC_except_table25790
- GCC_except_table25793
- GCC_except_table25796
- GCC_except_table25799
- GCC_except_table25802
- GCC_except_table25808
- GCC_except_table25811
- GCC_except_table25814
- GCC_except_table25817
- GCC_except_table25820
- GCC_except_table25823
- GCC_except_table25826
- GCC_except_table25829
- GCC_except_table25832
- GCC_except_table25835
- GCC_except_table25838
- GCC_except_table25841
- GCC_except_table25844
- GCC_except_table25847
- GCC_except_table25850
- GCC_except_table25853
- GCC_except_table25856
- GCC_except_table25859
- GCC_except_table25862
- GCC_except_table25865
- GCC_except_table25868
- GCC_except_table25871
- GCC_except_table25874
- GCC_except_table25877
- GCC_except_table25880
- GCC_except_table25886
- GCC_except_table25889
- GCC_except_table25895
- GCC_except_table25898
- GCC_except_table25901
- GCC_except_table25904
- GCC_except_table25907
- GCC_except_table25910
- GCC_except_table25913
- GCC_except_table25916
- GCC_except_table25919
- GCC_except_table25922
- GCC_except_table25925
- GCC_except_table25928
- GCC_except_table25937
- GCC_except_table25940
- GCC_except_table25943
- GCC_except_table25946
- GCC_except_table25949
- GCC_except_table25952
- GCC_except_table26010
- GCC_except_table26013
- GCC_except_table26016
- GCC_except_table26054
- GCC_except_table26060
- GCC_except_table26108
- GCC_except_table26140
- GCC_except_table26145
- GCC_except_table26147
- GCC_except_table26149
- GCC_except_table26195
- GCC_except_table26240
- GCC_except_table26248
- GCC_except_table26253
- GCC_except_table26264
- GCC_except_table26285
- GCC_except_table26292
- GCC_except_table26294
- GCC_except_table26295
- GCC_except_table26425
- GCC_except_table26431
- GCC_except_table26452
- GCC_except_table26491
- GCC_except_table26494
- GCC_except_table26500
- GCC_except_table26505
- GCC_except_table26509
- GCC_except_table26544
- GCC_except_table26550
- GCC_except_table26552
- GCC_except_table26593
- GCC_except_table26737
- GCC_except_table26741
- GCC_except_table26744
- GCC_except_table26746
- GCC_except_table26858
- GCC_except_table27050
- GCC_except_table27053
- GCC_except_table27060
- GCC_except_table27064
- GCC_except_table2707
- GCC_except_table27075
- GCC_except_table27083
- GCC_except_table27085
- GCC_except_table2709
- GCC_except_table27092
- GCC_except_table27106
- GCC_except_table27115
- GCC_except_table27133
- GCC_except_table2719
- GCC_except_table2723
- GCC_except_table2746
- GCC_except_table2749
- GCC_except_table278
- GCC_except_table2787
- GCC_except_table2799
- GCC_except_table2802
- GCC_except_table2809
- GCC_except_table2816
- GCC_except_table284
- GCC_except_table2860
- GCC_except_table2861
- GCC_except_table2919
- GCC_except_table2959
- GCC_except_table3069
- GCC_except_table3077
- GCC_except_table3099
- GCC_except_table3294
- GCC_except_table3300
- GCC_except_table331
- GCC_except_table3352
- GCC_except_table3404
- GCC_except_table3406
- GCC_except_table3414
- GCC_except_table3431
- GCC_except_table3441
- GCC_except_table3456
- GCC_except_table3485
- GCC_except_table3500
- GCC_except_table3505
- GCC_except_table3510
- GCC_except_table3518
- GCC_except_table3522
- GCC_except_table3528
- GCC_except_table3532
- GCC_except_table3572
- GCC_except_table3830
- GCC_except_table3834
- GCC_except_table3840
- GCC_except_table3843
- GCC_except_table3846
- GCC_except_table3856
- GCC_except_table3916
- GCC_except_table3954
- GCC_except_table3957
- GCC_except_table3965
- GCC_except_table3990
- GCC_except_table3999
- GCC_except_table4027
- GCC_except_table4087
- GCC_except_table4092
- GCC_except_table4103
- GCC_except_table4108
- GCC_except_table4111
- GCC_except_table4135
- GCC_except_table4137
- GCC_except_table4146
- GCC_except_table4147
- GCC_except_table4149
- GCC_except_table415
- GCC_except_table4167
- GCC_except_table4170
- GCC_except_table4176
- GCC_except_table418
- GCC_except_table4198
- GCC_except_table4201
- GCC_except_table421
- GCC_except_table4224
- GCC_except_table4229
- GCC_except_table4233
- GCC_except_table4237
- GCC_except_table424
- GCC_except_table4241
- GCC_except_table4264
- GCC_except_table427
- GCC_except_table433
- GCC_except_table4415
- GCC_except_table4431
- GCC_except_table4437
- GCC_except_table4439
- GCC_except_table4455
- GCC_except_table4457
- GCC_except_table4472
- GCC_except_table4478
- GCC_except_table4499
- GCC_except_table4517
- GCC_except_table4518
- GCC_except_table4543
- GCC_except_table4593
- GCC_except_table4597
- GCC_except_table465
- GCC_except_table4798
- GCC_except_table4805
- GCC_except_table4864
- GCC_except_table4886
- GCC_except_table4890
- GCC_except_table4913
- GCC_except_table5008
- GCC_except_table5013
- GCC_except_table5047
- GCC_except_table5121
- GCC_except_table5223
- GCC_except_table523
- GCC_except_table5261
- GCC_except_table5269
- GCC_except_table5271
- GCC_except_table5274
- GCC_except_table537
- GCC_except_table5493
- GCC_except_table5508
- GCC_except_table5534
- GCC_except_table5610
- GCC_except_table5611
- GCC_except_table5627
- GCC_except_table568
- GCC_except_table5687
- GCC_except_table5706
- GCC_except_table5713
- GCC_except_table5717
- GCC_except_table5726
- GCC_except_table5729
- GCC_except_table573
- GCC_except_table5789
- GCC_except_table5794
- GCC_except_table5804
- GCC_except_table5814
- GCC_except_table5842
- GCC_except_table5845
- GCC_except_table5863
- GCC_except_table5871
- GCC_except_table5873
- GCC_except_table590
- GCC_except_table5902
- GCC_except_table5903
- GCC_except_table5906
- GCC_except_table5907
- GCC_except_table5915
- GCC_except_table5928
- GCC_except_table6019
- GCC_except_table6021
- GCC_except_table6044
- GCC_except_table6082
- GCC_except_table6086
- GCC_except_table6090
- GCC_except_table6111
- GCC_except_table6116
- GCC_except_table6121
- GCC_except_table6123
- GCC_except_table6125
- GCC_except_table6146
- GCC_except_table6148
- GCC_except_table6152
- GCC_except_table6154
- GCC_except_table6212
- GCC_except_table6235
- GCC_except_table6256
- GCC_except_table6261
- GCC_except_table6265
- GCC_except_table6269
- GCC_except_table6274
- GCC_except_table6279
- GCC_except_table6283
- GCC_except_table6287
- GCC_except_table6291
- GCC_except_table6302
- GCC_except_table6305
- GCC_except_table6313
- GCC_except_table6314
- GCC_except_table6315
- GCC_except_table6316
- GCC_except_table6317
- GCC_except_table6318
- GCC_except_table6319
- GCC_except_table6324
- GCC_except_table6326
- GCC_except_table6327
- GCC_except_table6329
- GCC_except_table6330
- GCC_except_table6332
- GCC_except_table6341
- GCC_except_table6342
- GCC_except_table6351
- GCC_except_table6353
- GCC_except_table6358
- GCC_except_table6368
- GCC_except_table6369
- GCC_except_table6370
- GCC_except_table6372
- GCC_except_table6376
- GCC_except_table6380
- GCC_except_table6394
- GCC_except_table6423
- GCC_except_table6461
- GCC_except_table6474
- GCC_except_table6501
- GCC_except_table6567
- GCC_except_table6684
- GCC_except_table672
- GCC_except_table6751
- GCC_except_table677
- GCC_except_table690
- GCC_except_table692
- GCC_except_table696
- GCC_except_table6964
- GCC_except_table7023
- GCC_except_table705
- GCC_except_table7069
- GCC_except_table7076
- GCC_except_table7087
- GCC_except_table7093
- GCC_except_table7100
- GCC_except_table7109
- GCC_except_table711
- GCC_except_table7113
- GCC_except_table7116
- GCC_except_table7119
- GCC_except_table7125
- GCC_except_table7138
- GCC_except_table7144
- GCC_except_table7147
- GCC_except_table7155
- GCC_except_table7163
- GCC_except_table7171
- GCC_except_table7183
- GCC_except_table7195
- GCC_except_table7209
- GCC_except_table7221
- GCC_except_table7239
- GCC_except_table7244
- GCC_except_table7247
- GCC_except_table725
- GCC_except_table7255
- GCC_except_table7257
- GCC_except_table7261
- GCC_except_table7266
- GCC_except_table7271
- GCC_except_table729
- GCC_except_table7328
- GCC_except_table734
- GCC_except_table7346
- GCC_except_table7347
- GCC_except_table7353
- GCC_except_table7354
- GCC_except_table7356
- GCC_except_table7357
- GCC_except_table7361
- GCC_except_table7362
- GCC_except_table7364
- GCC_except_table7369
- GCC_except_table7372
- GCC_except_table7379
- GCC_except_table7381
- GCC_except_table7386
- GCC_except_table7388
- GCC_except_table7391
- GCC_except_table7399
- GCC_except_table7403
- GCC_except_table7408
- GCC_except_table7410
- GCC_except_table7414
- GCC_except_table7418
- GCC_except_table7427
- GCC_except_table7437
- GCC_except_table7441
- GCC_except_table7443
- GCC_except_table7466
- GCC_except_table7468
- GCC_except_table7472
- GCC_except_table7500
- GCC_except_table7504
- GCC_except_table7530
- GCC_except_table7532
- GCC_except_table7548
- GCC_except_table760
- GCC_except_table7784
- GCC_except_table7788
- GCC_except_table7801
- GCC_except_table7802
- GCC_except_table7815
- GCC_except_table7837
- GCC_except_table7838
- GCC_except_table7849
- GCC_except_table7878
- GCC_except_table7896
- GCC_except_table7898
- GCC_except_table7908
- GCC_except_table7912
- GCC_except_table7913
- GCC_except_table7920
- GCC_except_table7923
- GCC_except_table797
- GCC_except_table7980
- GCC_except_table7984
- GCC_except_table7986
- GCC_except_table7997
- GCC_except_table8004
- GCC_except_table8059
- GCC_except_table8068
- GCC_except_table808
- GCC_except_table8082
- GCC_except_table8104
- GCC_except_table8108
- GCC_except_table8112
- GCC_except_table812
- GCC_except_table8131
- GCC_except_table8137
- GCC_except_table8149
- GCC_except_table8157
- GCC_except_table8166
- GCC_except_table8185
- GCC_except_table8186
- GCC_except_table8190
- GCC_except_table8191
- GCC_except_table8195
- GCC_except_table8199
- GCC_except_table8202
- GCC_except_table8215
- GCC_except_table8222
- GCC_except_table8227
- GCC_except_table8237
- GCC_except_table8247
- GCC_except_table8250
- GCC_except_table8259
- GCC_except_table829
- GCC_except_table8292
- GCC_except_table835
- GCC_except_table8350
- GCC_except_table8351
- GCC_except_table8386
- GCC_except_table8391
- GCC_except_table8397
- GCC_except_table8409
- GCC_except_table842
- GCC_except_table8420
- GCC_except_table8433
- GCC_except_table8457
- GCC_except_table847
- GCC_except_table8487
- GCC_except_table852
- GCC_except_table8522
- GCC_except_table8525
- GCC_except_table8578
- GCC_except_table8586
- GCC_except_table859
- GCC_except_table8601
- GCC_except_table8603
- GCC_except_table863
- GCC_except_table866
- GCC_except_table871
- GCC_except_table8723
- GCC_except_table8768
- GCC_except_table8793
- GCC_except_table8822
- GCC_except_table8823
- GCC_except_table889
- GCC_except_table8993
- GCC_except_table9005
- GCC_except_table9013
- GCC_except_table9016
- GCC_except_table9021
- GCC_except_table9022
- GCC_except_table9047
- GCC_except_table9071
- GCC_except_table9075
- GCC_except_table9078
- GCC_except_table9085
- GCC_except_table9089
- GCC_except_table9135
- GCC_except_table918
- GCC_except_table924
- GCC_except_table9257
- GCC_except_table9291
- GCC_except_table9295
- GCC_except_table9301
- GCC_except_table9303
- GCC_except_table9309
- GCC_except_table9312
- GCC_except_table9395
- GCC_except_table9521
- GCC_except_table9535
- GCC_except_table9538
- GCC_except_table9563
- GCC_except_table9565
- GCC_except_table9567
- GCC_except_table9569
- GCC_except_table9570
- GCC_except_table9576
- GCC_except_table9578
- GCC_except_table9588
- GCC_except_table9592
- GCC_except_table9595
- GCC_except_table9644
- GCC_except_table9645
- GCC_except_table965
- GCC_except_table9663
- GCC_except_table9668
- GCC_except_table9681
- GCC_except_table969
- GCC_except_table9715
- GCC_except_table9726
- GCC_except_table9756
- GCC_except_table9787
- GCC_except_table9868
- GCC_except_table9869
- GCC_except_table9900
- GCC_except_table9901
- GCC_except_table9903
- GCC_except_table9906
- GCC_except_table9908
- GCC_except_table9909
- GCC_except_table9911
- GCC_except_table9913
- GCC_except_table9914
- GCC_except_table9982
- GCC_except_table9987
- GCC_except_table9991
- _OBJC_CLASS_$_PSIAlbumTranslator
- _OBJC_CLASS_$_PSIAssetTranslator
- _OBJC_CLASS_$_PSICollectionShareTranslator
- _OBJC_CLASS_$_PSIMemoryTranslator
- _OBJC_CLASS_$_PSISearchEntityTranslator
- _OBJC_IVAR_$_PLSearchIndexingEngine._queue_psiDatabase
- _OBJC_METACLASS_$_PSIAlbumTranslator
- _OBJC_METACLASS_$_PSIAssetTranslator
- _OBJC_METACLASS_$_PSICollectionShareTranslator
- _OBJC_METACLASS_$_PSIMemoryTranslator
- _OBJC_METACLASS_$_PSISearchEntityTranslator
- _PLContainingBundleRecord
- _PLSearchEnablePSIForSyndicationLibrary
- _PLSearchEnablePSIForSyndicationLibrary.enablePSIForSyndicationLibrary
- _PLSearchEnablePSIForSyndicationLibrary.onceToken
- _PLURLForResourceProperties
- __OBJC_$_CLASS_METHODS_PSIAlbumTranslator
- __OBJC_$_CLASS_METHODS_PSIAssetTranslator
- __OBJC_$_CLASS_METHODS_PSICollectionShareTranslator
- __OBJC_$_CLASS_METHODS_PSIMemoryTranslator
- __OBJC_$_CLASS_METHODS_PSISearchEntityTranslator
- __OBJC_CLASS_RO_$_PSIAlbumTranslator
- __OBJC_CLASS_RO_$_PSIAssetTranslator
- __OBJC_CLASS_RO_$_PSICollectionShareTranslator
- __OBJC_CLASS_RO_$_PSIMemoryTranslator
- __OBJC_CLASS_RO_$_PSISearchEntityTranslator
- __OBJC_METACLASS_RO_$_PSIAlbumTranslator
- __OBJC_METACLASS_RO_$_PSIAssetTranslator
- __OBJC_METACLASS_RO_$_PSICollectionShareTranslator
- __OBJC_METACLASS_RO_$_PSIMemoryTranslator
- __OBJC_METACLASS_RO_$_PSISearchEntityTranslator
- ___100+[PSIAssetTranslator _appendSceneClassificationsToAsset:sceneTaxonomyProvider:forAsset:fetchHelper:]_block_invoke
- ___101-[PLSyndicationDeleteEngine _deleteSyndicationAssetsWithBundleID:syndicationIdentifiers:deleteCount:]_block_invoke
- ___101-[PLSyndicationDeleteEngine _deleteSyndicationAssetsWithBundleID:syndicationIdentifiers:deleteCount:]_block_invoke_2
- ___106-[PLCollectionShareMigrationSessionPhaseSilentMigrationCleanup _performLocalCleanupWithCompletionHandler:]_block_invoke
- ___107-[PLCollectionShareMigrationSessionPhaseSilentMigrationCleanup _performServerCleanupWithCompletionHandler:]_block_invoke
- ___110+[PLInitialSuggestionsStorageManager updateInitialSuggestionsWithIdentifiers:dateLastUsed:photoLibrary:error:]_block_invoke
- ___110+[PLInitialSuggestionsStorageManager updateInitialSuggestionsWithIdentifiers:dateLastUsed:photoLibrary:error:]_block_invoke_2
- ___111-[PLCollectionShareSharedStreamBackend informMSASToCompleteMigrationToCPLForCollectionShare:completionHandler:]_block_invoke
- ___115+[PSIAssetTranslator _appendGraphDataToAsset:forMomentFromFetchHelper:hasValidReverseLocationData:indexingContext:]_block_invoke
- ___129-[PLCollectionShareSharedStreamBackend informMSASToInitiateMigrationToCPLForCollectionShare:isSilentMigration:completionHandler:]_block_invoke
- ___169-[PLSearchIndexingEngine _inq_donatePSIObjectsByType:spotlightItemsByBundleID:leoDonatableItems:leoLexemeScoreUpdates:deleteIdentifiers:spotlightClientState:completion:]_block_invoke
- ___169-[PLSearchIndexingEngine _inq_donatePSIObjectsByType:spotlightItemsByBundleID:leoDonatableItems:leoLexemeScoreUpdates:deleteIdentifiers:spotlightClientState:completion:]_block_invoke_2
- ___41-[PLCloudSharedCommentsJob runDaemonSide]_block_invoke
- ___42-[PLCloudSharedAssetSaveJob runDaemonSide]_block_invoke
- ___53+[PSIAssetTranslator _appendPet:fetchHelper:toAsset:]_block_invoke
- ___53+[PSIAssetTranslator _appendPet:fetchHelper:toAsset:]_block_invoke_2
- ___55+[PSIAssetTranslator _appendStyleCastToAsset:forAsset:]_block_invoke
- ___56+[PSIAssetTranslator _appendPerson:fetchHelper:toAsset:]_block_invoke
- ___56+[PSIAssetTranslator _appendPerson:fetchHelper:toAsset:]_block_invoke_2
- ___57+[PSIAssetTranslator _appendContributorToAsset:forAsset:]_block_invoke
- ___64-[PLSearchIndexingEngine _safePerformBlockWithPSIDatabase:sync:]_block_invoke
- ___64-[PLSearchIndexingEngine _safePerformBlockWithPSIDatabase:sync:]_block_invoke_2
- ___64-[PLSearchIndexingEngine _safePerformBlockWithPSIDatabase:sync:]_block_invoke_3
- ___65+[PSIAssetTranslator _appendAudioClassificationToAsset:forAsset:]_block_invoke
- ___70+[PSIAssetTranslator _appendHumanActionsToAsset:forAsset:fetchHelper:]_block_invoke
- ___73+[PSIAssetTranslator _appendDateCreatedToAsset:indexingContext:forAsset:]_block_invoke
- ___73+[PSIAssetTranslator _appendDateCreatedToAsset:indexingContext:forAsset:]_block_invoke_2
- ___73+[PSIAssetTranslator _appendDateCreatedToAsset:indexingContext:forAsset:]_block_invoke_3
- ___74+[PSIAssetTranslator _appendUtilityTypesToAsset:forAsset:indexingContext:]_block_invoke
- ___75-[PLModelMigrator _importFileSystemImportAssets:intoLibrary:type:progress:]_block_invoke
- ___75-[PLModelMigrator _importFileSystemImportAssets:intoLibrary:type:progress:]_block_invoke_2
- ___75-[PLModelMigrator _importFileSystemImportAssets:intoLibrary:type:progress:]_block_invoke_3
- ___76+[PSIAssetTranslator _appendGEODataToAsset:forAsset:countrySynonymProvider:]_block_invoke
- ___77-[PLCollectionShare informMSASToCompleteMigrationToCPLWithCompletionHandler:]_block_invoke
- ___78-[PLSyndicationDeleteEngine _processDeletesForBundleID:unprefixedIdentifiers:]_block_invoke
- ___80+[PLInitialSuggestionsStorageManager saveInitialSuggestions:photoLibrary:error:]_block_invoke
- ___80+[PLInitialSuggestionsStorageManager saveInitialSuggestions:photoLibrary:error:]_block_invoke_2
- ___80-[PLSearchIndexingEngine _inq_dropSearchIndexWithSourceName:reasons:completion:]_block_invoke_3
- ___80-[PLSearchIndexingEngine _inq_dropSearchIndexWithSourceName:reasons:completion:]_block_invoke_4
- ___95-[PLCollectionShare informMSASToInitiateMigrationToCPLWithIsSilentMigration:completionHandler:]_block_invoke
- ___98+[PSIAssetTranslator _appendStickerSuggestionsToAsset:fetchHelper:sceneTaxonomyProvider:forAsset:]_block_invoke
- ___PLIndexRevGeoPlace_block_invoke
- ___PLIndexRevGeoPlace_block_invoke_2
- ___PLSearchEnablePSIForSyndicationLibrary_block_invoke
- ___block_descriptor_112_e8_32s40s48s56r64r72r80r88r96r_e5_v8?0ls32l8s40l8r56l8s48l8r64l8r72l8r80l8r88l8r96l8
- ___block_descriptor_128_e8_32s40s48s56s64bs72r80n11_8_8_s0_t8w8_e5_v8?0l
- ___block_descriptor_177_e8_32s40s48s56s64s72s80s88s96s104s112s120s128bs136r144n11_8_8_s0_t8w8_e5_v8?0l
- ___block_descriptor_32_e21_v16?0"PSIDatabase"8l
- ___block_descriptor_40_e8_32bs_e17_v16?0"NSArray"8ls32l8
- ___block_descriptor_40_e8_32s_e21_v16?0"PSIDatabase"8ls32l8
- ___block_descriptor_40_e8_32s_e57_v32?0"<PLSearchDetectionTrait>"8"NSString"16"NSSet"24ls32l8
- ___block_descriptor_48_e8_32s40s_e21_v16?0"PSIDatabase"8ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e24_v16?0"PLManagedAsset"8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e28_v24?0"NSString"8"NSSet"16ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e44_v24?0"PLSearchEntityRelationToPerson"8^B16ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48bs_e17_v16?0"NSError"8ls32l8s48l8s40l8
- ___block_descriptor_64_e8_32s40s48s_e32_v16?0"NSManagedObjectContext"8ls32l8s40l8s48l8
- ___block_descriptor_73_e8_32s40s48s56s64s_e35_v16?0"PLFileSystemAssetImporter"8ls32l8s40l8s48l8s56l8s64l8
- ___copy_helper_block_e8_144n11_8_8_s0_t8w8
- ___destroy_helper_block_e8_144n4_8_s0
- _flat unique So30PLIntersectedSearchIndexEntity_p
- _objc_msgSend$_addContentClassificationToAsset:nodeLabel:nodeSynonyms:nodeSceneID:
- _objc_msgSend$_appendAssetTextDataToAsset:forAsset:
- _objc_msgSend$_appendAudioClassificationToAsset:forAsset:
- _objc_msgSend$_appendContentClassificationsToAsset:sceneTaxonomyProvider:forAsset:fetchHelper:
- _objc_msgSend$_appendContributorToAsset:forAsset:
- _objc_msgSend$_appendDateCreatedToAsset:indexingContext:forAsset:
- _objc_msgSend$_appendExifDataToAsset:forAsset:
- _objc_msgSend$_appendFavoriteToAsset:forAsset:
- _objc_msgSend$_appendFilenameToAsset:forAsset:
- _objc_msgSend$_appendGEODataToAsset:forAsset:countrySynonymProvider:
- _objc_msgSend$_appendGraphDataToAsset:forMomentFromFetchHelper:hasValidReverseLocationData:indexingContext:
- _objc_msgSend$_appendHumanActionsToAsset:forAsset:fetchHelper:
- _objc_msgSend$_appendKeywords:toAsset:
- _objc_msgSend$_appendLibraryScopeToAsset:forAsset:
- _objc_msgSend$_appendMediaTypesToAsset:forAsset:
- _objc_msgSend$_appendOCRTextForAsset:documentObservation:
- _objc_msgSend$_appendPerson:fetchHelper:toAsset:
- _objc_msgSend$_appendPersonsAndPetsToAsset:forAsset:fetchHelper:
- _objc_msgSend$_appendPet:fetchHelper:toAsset:
- _objc_msgSend$_appendPrivateEncryptedComputeScenes:forAsset:fetchHelper:csuTaxonomyObjectStore:locale:
- _objc_msgSend$_appendSavedFromAppToAsset:forAsset:
- _objc_msgSend$_appendSceneClassificationsToAsset:sceneTaxonomyProvider:forAsset:fetchHelper:
- _objc_msgSend$_appendStickerSuggestionsToAsset:fetchHelper:sceneTaxonomyProvider:forAsset:
- _objc_msgSend$_appendStyleCastToAsset:forAsset:
- _objc_msgSend$_appendUtilityTypesToAsset:forAsset:indexingContext:
- _objc_msgSend$_deleteSyndicationAssetsWithBundleID:syndicationIdentifiers:deleteCount:
- _objc_msgSend$_endDateForMemory:
- _objc_msgSend$_fetchCuratedAssetsForMemory:sortedAscending:
- _objc_msgSend$_importFileSystemImportAssets:intoLibrary:type:progress:
- _objc_msgSend$_indexCategoryForSearchEntityType:
- _objc_msgSend$_inq_donatePSIObjectsByType:spotlightItemsByBundleID:leoDonatableItems:leoLexemeScoreUpdates:deleteIdentifiers:spotlightClientState:completion:
- _objc_msgSend$_lookupIdentifierForSearchEntity:
- _objc_msgSend$_performLocalCleanupWithCompletionHandler:
- _objc_msgSend$_performServerCleanupWithCompletionHandler:
- _objc_msgSend$_processDeletesForBundleID:unprefixedIdentifiers:
- _objc_msgSend$_safePerformBlockWithPSIDatabase:sync:
- _objc_msgSend$_searchWithEmbeddings:photoLibraryURL:searchOptions:numberOfProbes:error:
- _objc_msgSend$_startDateForMemory:
- _objc_msgSend$addContentFromAsset:forPropertySets:withIndexingContext:fetchHelper:embeddingsFetcher:
- _objc_msgSend$addIdentifier:category:owningCategory:
- _objc_msgSend$addSynonym:category:originalContentString:
- _objc_msgSend$assetsPrivate
- _objc_msgSend$assetsShared
- _objc_msgSend$assetsToUseForDayGroupHighlight:withFilter:
- _objc_msgSend$assetsToUseForDayHighlight:withFilter:
- _objc_msgSend$cancelMigrationToCPLForAlbumWithGUID:personID:completionBlock:
- _objc_msgSend$completeMigrationToCPLForAlbumWithGUID:personID:completionBlock:
- _objc_msgSend$dayGroupAssetsPrivate
- _objc_msgSend$dayGroupAssetsShared
- _objc_msgSend$dayGroupExtendedAssetsPrivate
- _objc_msgSend$dayGroupExtendedAssetsShared
- _objc_msgSend$deleteAllInitialSuggestions
- _objc_msgSend$dropDatabaseAtPath:withCompletion:
- _objc_msgSend$dropDatabaseWithCompletion:
- _objc_msgSend$failMigrationToCPLForAlbumWithGUID:migrationError:personID:completionBlock:
- _objc_msgSend$informMSASToCompleteMigrationToCPLForCollectionShare:completionHandler:
- _objc_msgSend$informMSASToCompleteMigrationToCPLWithCompletionHandler:
- _objc_msgSend$informMSASToInitiateMigrationToCPLForCollectionShare:isSilentMigration:completionHandler:
- _objc_msgSend$informMSASToInitiateMigrationToCPLWithIsSilentMigration:completionHandler:
- _objc_msgSend$initWithName:canDelayAnyQOS:singleThreadedMode:timeProvider:targetQueue:target:
- _objc_msgSend$initWithUUID:startDate:endDate:title:subtitle:type:assetsCountPrivate:assetsCountShared:sortDate:
- _objc_msgSend$initiateMigrationToCPLForAlbumWithGUID:personID:isSilentMigration:completionBlock:
- _objc_msgSend$leoDonatableItemForManagedObject:partialUpdateMask:indexingContext:fetchHelper:embeddingsFetcher:
- _objc_msgSend$objectType
- _objc_msgSend$psiAssetFromAsset:fetchHelper:propertySets:indexingContext:documentObservation:
- _objc_msgSend$psiCollectionFromAlbum:indexingContext:
- _objc_msgSend$psiCollectionFromCollectionShare:indexingContext:
- _objc_msgSend$psiCollectionFromMemory:indexingContext:
- _objc_msgSend$psiGroupFromSearchEntity:
- _objc_msgSend$psiObjectForIdentifierRequiringAdditionalWork:entity:
- _objc_msgSend$psiObjectForObject:fetchHelper:partialUpdateMask:indexingContext:
- _objc_msgSend$removeUnusedGroups
- _objc_msgSend$safePerformBlockAndWaitWithPSIDatabase:
- _objc_msgSend$safePerformBlockWithPSIDatabase:
- _objc_msgSend$saveInitialSuggestions:
- _objc_msgSend$searchIndexEmbeddingModelVersion
- _objc_msgSend$searchableItemForObject:fetchHelper:partialUpdateMask:libraryIdentifier:indexingContext:embeddingsFetcher:
- _objc_msgSend$setPropertySets:
- _objc_msgSend$supportsPSI
- _objc_msgSend$synchronizeWithPersistedFileSystemAttributes
- _objc_msgSend$unarchiveMigrationToCPLForAlbumWithGUID:personID:completionBlock:
- _objc_msgSend$updateInitialSuggestionsWithIdentifiers:dateLastUsed:
- _objc_msgSend$updateRankingScoreForGroups:withCompletion:
- _objc_msgSend$zeroScorePSIGroupFromLabel:type:identifier:
- _symbolic ______p So30PLIntersectedSearchIndexEntityP
CStrings:
+ "%@ : runDaemonSide %@ waitUntilFinished:%d"
+ "%@:assetsdProcessMetadataForAssetCollectionsAndWait:%@ inAlbum:%@ personID:%@ can't have nil arguments"
+ "%{public}@ Error deleting items for bundle ID: %{public}@, items; %{public}@"
+ "%{public}@ Skipping conversation delete because deleted asset count matched identifiers count"
+ "-[PLAssetsdMigrationService _ensureSystemColocatedApplicationLibraries]"
+ "-[PLCloudSharedAssetSaveJob _runDaemonSideWaitUntilFinished:]"
+ "-[PLCloudSharedCommentsJob _runDaemonSideWaitUntilFinished:]"
+ "-[PLCollectionShareSharedStreamBackend checkServerForChangesForCollectionShare:completionHandler:]"
+ "-[PLSyndicationDeleteEngine _processDeletesForBundleID:unprefixedIdentifiers:error:]"
+ ";@0"
+ "AgentMediaPhotoLibrary"
+ "CSSearchableItems: %tu, DeleteIdentifiers: %tu"
+ "Class getIMContactStoreClass(void)_block_invoke"
+ "Class getIMDDatabaseClass(void)_block_invoke"
+ "Deleted %tu asset(s) using %tu unprefixed identifiers"
+ "Ensured Visual Intelligence application library exists"
+ "Error getting bundle %@ LSM %@ from bundle controller for URL %@"
+ "Error getting bundle or LSM"
+ "Error instantiating existing app library identifier for URL %@ - %@"
+ "Error instantiating existing library identifier for URL %@ - %@"
+ "Error obtaining path for restricted derivatives directory: %@"
+ "Error removing restricted derivatives directory: %@"
+ "Failed to direct upload full resources for proxy assets: %@"
+ "Failed to ensure Visual Intelligence application library: %@"
+ "Failed to execute semantic search"
+ "Failed to fetch oldest and newest asset dates for day group highlight with filter: %ld, error: %@"
+ "Failed to fetch oldest and newest asset dates for day highlight with filter: %ld, error: %@"
+ "Failed to generate full record changes for placeholder asset %@ during full resource direct upload"
+ "Failed to persist keyword %@ to journal: %@"
+ "Going to direct upload full resources for %lu proxy-uploaded assets"
+ "IMContactStore"
+ "IMDDatabase"
+ "IMMessageGuidFromIMFileTransferGuid"
+ "ITEMS_ADDED_SHARED_ALBUM_NOTIFICATION_MESSAGE"
+ "ITEMS_WITH_CAPTION_ADDED_SHARED_ALBUM_NOTIFICATION_MESSAGE"
+ "Messages sender/receiver: batch contact resolution failed: %{public}@"
+ "NSString *softlink_IMMessageGuidFromIMFileTransferGuid(NSString *__strong)"
+ "Not ensuring application library %{public}@; deletion tombstone present"
+ "Originating asset count changed during migration (persisted=%d, current=%d) for originating %@"
+ "PLSearchIndexCategoryReceiver"
+ "PLSearchIndexCategorySender"
+ "PLSearchIndexingMessagesFetcher.m"
+ "PLSearchLeoMessagesSenderReceiverSPLEnabled"
+ "PLSearchLeoMessagesSenderReceiverSPLEnabled: %d"
+ "PLSearchLeoMessagesSenderReceiverSyndicationEnabled"
+ "PLSearchLeoMessagesSenderReceiverSyndicationEnabled: %d"
+ "PLSearchUnifiedMADEmbeddingSearchEnabled"
+ "PLSearchUnifiedMADEmbeddingSearchEnabled: %d"
+ "Pausing incremental updates for library: %@"
+ "Persisted keywords to journal (%ld) and keyword UUIDs to asset extended attributes (%ld)"
+ "Photos Backend Storage"
+ "Placeholder asset %@ has no master during full resource direct upload"
+ "Proxy direct upload partially failed: %lu of %lu proxy assets did not appear in successful results"
+ "Rebuild: could not find keyword for uuid: %{public}@ for asset: %{public}@"
+ "Rebuild: unable to fetch %{public}@ to delete: %@"
+ "Rebuild: using re-mapped uuid for keyword %@, %{public}@ -> %{public}@, for asset: %{public}@"
+ "Recreating missing database in place for application library: %@"
+ "Search index unavailable, may have been closed%@"
+ "Skipping App Entity tagging: missing entityInstanceIdentifier for typeIdentifier %{public}@"
+ "Successfully direct uploaded full resources batch for proxy assets"
+ "VIDEOS_ADDED_SHARED_ALBUM_NOTIFICATION_MESSAGE"
+ "VIDEOS_WITH_CAPTION_ADDED_SHARED_ALBUM_NOTIFICATION_MESSAGE"
+ "Will create new identifier with container identifier %{public}@, uuid %{public}@, name %@, userDescription %@"
+ "[SC Migration] Cleanup: %{public}@ no longer has an active silent migration; skipping teardown"
+ "[SC Migration] Cleanup: could not find originating share %{public}@ for local cleanup"
+ "[SC Migration] MSAS completed — CPL share exists, transitioning to Complete for share %@"
+ "[SC Migration] Silent migration teardown before user-initiated migration of %{public}@ hit an error: %@ (proceeding)"
+ "about to call connection refreshContentOfAlbumWithGUID:%@ personID:%@ (with completion)"
+ "assertion failure: Unexpected nil managed object context on PLInternalResource."
+ "assertion failure: Unexpected nil pathManager on managed object context."
+ "local primary image (internal resource)"
+ "local primary image (virtual resource)"
+ "master thumbnail cache"
+ "maxDelayBetweenRuns > 0"
+ "migrationOriginatingAssetCount"
+ "minDelayBetweenRuns > 0"
+ "newKeyAssetThumbnailDataForAsset: failed to create image source from %{public}@ for key asset %{public}@; returning nil"
+ "newKeyAssetThumbnailDataForAsset: failed to create thumbnail image from %{public}@ for key asset %{public}@; returning nil"
+ "newKeyAssetThumbnailDataForAsset: generated thumbnail for key asset %{public}@ from %{public}@ (encoded %lu bytes, final %lu bytes, budget %ld bytes)"
+ "newKeyAssetThumbnailDataForAsset: no current+local primary image for key asset %{public}@; falling back to master thumbnail cache"
+ "newKeyAssetThumbnailDataForAsset: no usable image source for key asset %{public}@ (hasAdjustments=%d, %lu candidate resources, no current+local primary image and no cached master thumbnail); returning nil"
+ "newKeyAssetThumbnailDataForAsset: rejected primary image for key asset %{public}@ (version=%ld, current=%d, localAvailability=%ld)"
+ "newKeyAssetThumbnailDataForAsset: using %{public}@ for key asset %{public}@"
+ "p"
+ "refreshContentOfAlbumWithGUID:%@ failed with error: %@"
+ "softlink:r:path:/System/Library/PrivateFrameworks/IMDPersistence.framework/IMDPersistence"
+ "v16@?0@\"IMDMessageRecord\"8"
+ "v16@?0@\"PLManagedKeyword\"8"
+ "void *IMDPersistenceLibrary(void)"
+ "yue"
- ", PSI index missing"
- "-[PLCloudSharedAssetSaveJob runDaemonSide]"
- "-[PLCloudSharedCommentsJob runDaemonSide]"
- "-[PLSyndicationDeleteEngine _deleteSyndicationAssetsWithBundleID:syndicationIdentifiers:deleteCount:]"
- "-[PLSyndicationDeleteEngine _processDeletesForBundleID:unprefixedIdentifiers:]"
- "<@0"
- "CSSearchableItems: %tu, PSI Assets: %tu, PSI Collections: %tu, PSI Groups: %tu, DeleteIdentifiers: %tu"
- "CSU: Duplicate PrivateEncryptedCompute label: '%@' found in synonyms for Scene (%lu, %llu)"
- "Found %tu asset(s) for deletion using %tu unprefixed identifiers"
- "Invalid Album UUID: %{public}@. Not inserting Album into PSI."
- "Invalid Asset UUID: %{public}@. Not inserting Asset into PSI."
- "Invalid CollectionShare UUID: %{public}@. Not inserting CollectionShare into PSI."
- "Invalid Memory UUID: %{public}@. Not inserting Memory into PSI."
- "Invalid entity for additional work"
- "No curated assets for Memory. Not adding to PSI: %{public}@"
- "PLIndexRevGeoPlace"
- "PLSearchManagedObjectUtilities.m"
- "PSI asset donation completed, elapsed: %f"
- "PSI collection donation completed, elapsed: %f"
- "PSI delete assets completed, elapsed: %f"
- "PSI delete collections completed, elapsed: %f"
- "PSI update rankings completed, elapsed: %f"
- "PSIAssetTranslator.m"
- "PSIAssetTranslator: Asset translation time"
- "PSIAssetTranslator: Content"
- "PSIAssetTranslator: OCR"
- "PSIAssetTranslator: Persons & Pets"
- "PSIAssetTranslator: Scenes"
- "PSIAssetTranslator: Stickers"
- "PSIAssetTranslator: Utility Types V2"
- "Search Indexing: duplicate scene keyword: '%@' found in scene synonyms array for scene ID: %llu"
- "Search index unavailable, may have been closed%@%@"
- "Skipping perform block with PSI due to index drop in progress"
- "Skipping perform block with PSI due to nil PSI database"
- "Unexpected detection type (%hd) for pet: %@"
- "Unexpected nil pathManager on managed object context."
- "Unexpected nil syndicationIdentifier on asset %{public}@"
- "[SC Migration] Starting silent migration local cleanup for originating %{public}@"
- "currentEmbeddingModelVersion: %tu != searchIndexEmbeddingModelVersion: %tu"
- "drop psi"
- "enablePSIForSyndicationLibrary"
- "enablePSIForSyndicationLibrary: %@."
- "keyword for asset: %@"
- "memoriesBeingCuratedAssets CONTAINS %@"
- "psi assets"
- "psi collections"
- "psi delete assets"
- "psi delete collections"
- "psi groups"
- "v16@?0@\"PSIDatabase\"8"

```
