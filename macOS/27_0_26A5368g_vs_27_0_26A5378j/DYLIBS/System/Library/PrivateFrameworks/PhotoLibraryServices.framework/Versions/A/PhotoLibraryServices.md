## PhotoLibraryServices

> `/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/Versions/A/PhotoLibraryServices`

```diff

-  __TEXT.__text: 0x796da8
-  __TEXT.__objc_methlist: 0x44cf4
-  __TEXT.__const: 0x7020
-  __TEXT.__dlopen_cstrs: 0x6c9
-  __TEXT.__swift5_typeref: 0x11e0
-  __TEXT.__cstring: 0x6a59d
+  __TEXT.__text: 0x796ab0
+  __TEXT.__objc_methlist: 0x44ddc
+  __TEXT.__const: 0x7050
+  __TEXT.__dlopen_cstrs: 0x783
+  __TEXT.__swift5_typeref: 0x11b2
+  __TEXT.__cstring: 0x6a9b3
   __TEXT.__swift5_capture: 0x1528
   __TEXT.__constg_swiftt: 0x290
   __TEXT.__swift5_builtin: 0x78

   __TEXT.__swift5_fieldmd: 0x200
   __TEXT.__swift5_proto: 0x70
   __TEXT.__swift5_types: 0x3c
-  __TEXT.__oslogstring: 0x802cb
+  __TEXT.__oslogstring: 0x80b8d
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x1f734
+  __TEXT.__gcc_except_tab: 0x1f858
   __TEXT.__ustring: 0xa3a
-  __TEXT.__unwind_info: 0x162d8
+  __TEXT.__unwind_info: 0x16330
   __TEXT.__eh_frame: 0xfa0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x6740
-  __DATA_CONST.__objc_classlist: 0x2390
+  __DATA_CONST.__const: 0x6798
+  __DATA_CONST.__objc_classlist: 0x2380
   __DATA_CONST.__objc_catlist: 0xf8
-  __DATA_CONST.__objc_protolist: 0x738
+  __DATA_CONST.__objc_protolist: 0x730
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x246e0
-  __DATA_CONST.__objc_protorefs: 0xd0
+  __DATA_CONST.__objc_selrefs: 0x247f0
+  __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x1548
-  __DATA_CONST.__objc_arraydata: 0x1da8
-  __DATA_CONST.__got: 0x4f48
-  __AUTH_CONST.__const: 0x1c4f8
-  __AUTH_CONST.__cfstring: 0x52020
-  __AUTH_CONST.__objc_const: 0x6ec88
+  __DATA_CONST.__objc_arraydata: 0x1d80
+  __DATA_CONST.__got: 0x4f78
+  __AUTH_CONST.__const: 0x1c5d8
+  __AUTH_CONST.__cfstring: 0x52160
+  __AUTH_CONST.__objc_const: 0x6eef0
   __AUTH_CONST.__weak_auth_got: 0x28
-  __AUTH_CONST.__objc_intobj: 0x54f0
-  __AUTH_CONST.__objc_arrayobj: 0x1560
+  __AUTH_CONST.__objc_intobj: 0x5460
+  __AUTH_CONST.__objc_arrayobj: 0x1530
   __AUTH_CONST.__objc_doubleobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x2f8
   __AUTH_CONST.__objc_floatobj: 0x30
-  __AUTH_CONST.__auth_got: 0x2798
-  __AUTH.__objc_data: 0xc438
+  __AUTH_CONST.__auth_got: 0x27a0
+  __AUTH.__objc_data: 0xc4d8
   __AUTH.__data: 0x190
-  __DATA.__objc_ivar: 0x3d34
-  __DATA.__data: 0x6d18
-  __DATA.__bss: 0x2db8
+  __DATA.__objc_ivar: 0x3d78
+  __DATA.__data: 0x6d08
+  __DATA.__bss: 0x2df8
   __DATA.__common: 0x4
-  __DATA_DIRTY.__objc_data: 0xa1b8
+  __DATA_DIRTY.__objc_data: 0xa078
   __DATA_DIRTY.__data: 0xe8
   __DATA_DIRTY.__crash_info: 0x148
-  __DATA_DIRTY.__bss: 0x690
+  __DATA_DIRTY.__bss: 0x698
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/AVFoundation.framework/Versions/A/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 29001
-  Symbols:   66497
-  CStrings:  31911
+  Functions: 29029
+  Symbols:   66584
+  CStrings:  31958
 
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
+ GCC_except_table10002
+ GCC_except_table10003
+ GCC_except_table10005
+ GCC_except_table10008
+ GCC_except_table10010
+ GCC_except_table10011
+ GCC_except_table10013
+ GCC_except_table10015
+ GCC_except_table10016
+ GCC_except_table10082
+ GCC_except_table10087
+ GCC_except_table10091
+ GCC_except_table10108
+ GCC_except_table10115
+ GCC_except_table10127
+ GCC_except_table10129
+ GCC_except_table10143
+ GCC_except_table10202
+ GCC_except_table10221
+ GCC_except_table10235
+ GCC_except_table10239
+ GCC_except_table10251
+ GCC_except_table10263
+ GCC_except_table10277
+ GCC_except_table10291
+ GCC_except_table10293
+ GCC_except_table10300
+ GCC_except_table10337
+ GCC_except_table10342
+ GCC_except_table1035
+ GCC_except_table10367
+ GCC_except_table10379
+ GCC_except_table1039
+ GCC_except_table10390
+ GCC_except_table10398
+ GCC_except_table10417
+ GCC_except_table10419
+ GCC_except_table10432
+ GCC_except_table10442
+ GCC_except_table10521
+ GCC_except_table10529
+ GCC_except_table10533
+ GCC_except_table10535
+ GCC_except_table10541
+ GCC_except_table10545
+ GCC_except_table10553
+ GCC_except_table10582
+ GCC_except_table10589
+ GCC_except_table1060
+ GCC_except_table10609
+ GCC_except_table10640
+ GCC_except_table10643
+ GCC_except_table10696
+ GCC_except_table10747
+ GCC_except_table10755
+ GCC_except_table10769
+ GCC_except_table10775
+ GCC_except_table10777
+ GCC_except_table10788
+ GCC_except_table10793
+ GCC_except_table10798
+ GCC_except_table10818
+ GCC_except_table10932
+ GCC_except_table10975
+ GCC_except_table11058
+ GCC_except_table11061
+ GCC_except_table11062
+ GCC_except_table11065
+ GCC_except_table11068
+ GCC_except_table11078
+ GCC_except_table11082
+ GCC_except_table11086
+ GCC_except_table11090
+ GCC_except_table11092
+ GCC_except_table11104
+ GCC_except_table11108
+ GCC_except_table11116
+ GCC_except_table11120
+ GCC_except_table11125
+ GCC_except_table11137
+ GCC_except_table11139
+ GCC_except_table11142
+ GCC_except_table11145
+ GCC_except_table11148
+ GCC_except_table11149
+ GCC_except_table11153
+ GCC_except_table11158
+ GCC_except_table11159
+ GCC_except_table11161
+ GCC_except_table11162
+ GCC_except_table11163
+ GCC_except_table11164
+ GCC_except_table11165
+ GCC_except_table11166
+ GCC_except_table11167
+ GCC_except_table11168
+ GCC_except_table11170
+ GCC_except_table11171
+ GCC_except_table11172
+ GCC_except_table11174
+ GCC_except_table11175
+ GCC_except_table11176
+ GCC_except_table11177
+ GCC_except_table11178
+ GCC_except_table11179
+ GCC_except_table1118
+ GCC_except_table11182
+ GCC_except_table11183
+ GCC_except_table11187
+ GCC_except_table11189
+ GCC_except_table11191
+ GCC_except_table11193
+ GCC_except_table11196
+ GCC_except_table11197
+ GCC_except_table11199
+ GCC_except_table11269
+ GCC_except_table11273
+ GCC_except_table11284
+ GCC_except_table11354
+ GCC_except_table1139
+ GCC_except_table11436
+ GCC_except_table11477
+ GCC_except_table11489
+ GCC_except_table11589
+ GCC_except_table11594
+ GCC_except_table11617
+ GCC_except_table11670
+ GCC_except_table11726
+ GCC_except_table11935
+ GCC_except_table1197
+ GCC_except_table11976
+ GCC_except_table1220
+ GCC_except_table12203
+ GCC_except_table12236
+ GCC_except_table1226
+ GCC_except_table12260
+ GCC_except_table12261
+ GCC_except_table12262
+ GCC_except_table12263
+ GCC_except_table12264
+ GCC_except_table12266
+ GCC_except_table12268
+ GCC_except_table12283
+ GCC_except_table1233
+ GCC_except_table12366
+ GCC_except_table12378
+ GCC_except_table12384
+ GCC_except_table12389
+ GCC_except_table12394
+ GCC_except_table12399
+ GCC_except_table12407
+ GCC_except_table12427
+ GCC_except_table12437
+ GCC_except_table12441
+ GCC_except_table12446
+ GCC_except_table12451
+ GCC_except_table12457
+ GCC_except_table12467
+ GCC_except_table12470
+ GCC_except_table12481
+ GCC_except_table12485
+ GCC_except_table12496
+ GCC_except_table1251
+ GCC_except_table12514
+ GCC_except_table1252
+ GCC_except_table12530
+ GCC_except_table12582
+ GCC_except_table12587
+ GCC_except_table12593
+ GCC_except_table12597
+ GCC_except_table12599
+ GCC_except_table1260
+ GCC_except_table12601
+ GCC_except_table12603
+ GCC_except_table12605
+ GCC_except_table12607
+ GCC_except_table12609
+ GCC_except_table12612
+ GCC_except_table12614
+ GCC_except_table12623
+ GCC_except_table12644
+ GCC_except_table12650
+ GCC_except_table12654
+ GCC_except_table12670
+ GCC_except_table12672
+ GCC_except_table12690
+ GCC_except_table12692
+ GCC_except_table12694
+ GCC_except_table12696
+ GCC_except_table12699
+ GCC_except_table12701
+ GCC_except_table12703
+ GCC_except_table12705
+ GCC_except_table12707
+ GCC_except_table12710
+ GCC_except_table12713
+ GCC_except_table12715
+ GCC_except_table12719
+ GCC_except_table12721
+ GCC_except_table12724
+ GCC_except_table12726
+ GCC_except_table12728
+ GCC_except_table12730
+ GCC_except_table12732
+ GCC_except_table12733
+ GCC_except_table12744
+ GCC_except_table12750
+ GCC_except_table12776
+ GCC_except_table12780
+ GCC_except_table12781
+ GCC_except_table12789
+ GCC_except_table12818
+ GCC_except_table1282
+ GCC_except_table12847
+ GCC_except_table12933
+ GCC_except_table1300
+ GCC_except_table13048
+ GCC_except_table13050
+ GCC_except_table13054
+ GCC_except_table13068
+ GCC_except_table13072
+ GCC_except_table13079
+ GCC_except_table13085
+ GCC_except_table13096
+ GCC_except_table13101
+ GCC_except_table13180
+ GCC_except_table13196
+ GCC_except_table13201
+ GCC_except_table13205
+ GCC_except_table13222
+ GCC_except_table13224
+ GCC_except_table13231
+ GCC_except_table13233
+ GCC_except_table13235
+ GCC_except_table13240
+ GCC_except_table13284
+ GCC_except_table13293
+ GCC_except_table13299
+ GCC_except_table13301
+ GCC_except_table13303
+ GCC_except_table13346
+ GCC_except_table1337
+ GCC_except_table13459
+ GCC_except_table13480
+ GCC_except_table13487
+ GCC_except_table13491
+ GCC_except_table1353
+ GCC_except_table13538
+ GCC_except_table1360
+ GCC_except_table13618
+ GCC_except_table13624
+ GCC_except_table13655
+ GCC_except_table1369
+ GCC_except_table13709
+ GCC_except_table13730
+ GCC_except_table13733
+ GCC_except_table13737
+ GCC_except_table13740
+ GCC_except_table13742
+ GCC_except_table13746
+ GCC_except_table13749
+ GCC_except_table13758
+ GCC_except_table13807
+ GCC_except_table13825
+ GCC_except_table13831
+ GCC_except_table1384
+ GCC_except_table13853
+ GCC_except_table13947
+ GCC_except_table14002
+ GCC_except_table14015
+ GCC_except_table14019
+ GCC_except_table14043
+ GCC_except_table14067
+ GCC_except_table14077
+ GCC_except_table14079
+ GCC_except_table14081
+ GCC_except_table14100
+ GCC_except_table14191
+ GCC_except_table14196
+ GCC_except_table14219
+ GCC_except_table14232
+ GCC_except_table14234
+ GCC_except_table14236
+ GCC_except_table1430
+ GCC_except_table14344
+ GCC_except_table14345
+ GCC_except_table14349
+ GCC_except_table14382
+ GCC_except_table14403
+ GCC_except_table14418
+ GCC_except_table14419
+ GCC_except_table14420
+ GCC_except_table14422
+ GCC_except_table14423
+ GCC_except_table14424
+ GCC_except_table14426
+ GCC_except_table14427
+ GCC_except_table14431
+ GCC_except_table14435
+ GCC_except_table14491
+ GCC_except_table14497
+ GCC_except_table14522
+ GCC_except_table14527
+ GCC_except_table14531
+ GCC_except_table14565
+ GCC_except_table14569
+ GCC_except_table14573
+ GCC_except_table14580
+ GCC_except_table14584
+ GCC_except_table14595
+ GCC_except_table14631
+ GCC_except_table14681
+ GCC_except_table14684
+ GCC_except_table14688
+ GCC_except_table14705
+ GCC_except_table1472
+ GCC_except_table14751
+ GCC_except_table14775
+ GCC_except_table14797
+ GCC_except_table1483
+ GCC_except_table1491
+ GCC_except_table14930
+ GCC_except_table15011
+ GCC_except_table15073
+ GCC_except_table15090
+ GCC_except_table15097
+ GCC_except_table15100
+ GCC_except_table15120
+ GCC_except_table15209
+ GCC_except_table1521
+ GCC_except_table15216
+ GCC_except_table15218
+ GCC_except_table15219
+ GCC_except_table15224
+ GCC_except_table15231
+ GCC_except_table1529
+ GCC_except_table15409
+ GCC_except_table15488
+ GCC_except_table1549
+ GCC_except_table1559
+ GCC_except_table1564
+ GCC_except_table15655
+ GCC_except_table15656
+ GCC_except_table15663
+ GCC_except_table15665
+ GCC_except_table15670
+ GCC_except_table15680
+ GCC_except_table15682
+ GCC_except_table15708
+ GCC_except_table15727
+ GCC_except_table15738
+ GCC_except_table15765
+ GCC_except_table15805
+ GCC_except_table15810
+ GCC_except_table15876
+ GCC_except_table15889
+ GCC_except_table16046
+ GCC_except_table1605
+ GCC_except_table16076
+ GCC_except_table16093
+ GCC_except_table16098
+ GCC_except_table16101
+ GCC_except_table16103
+ GCC_except_table16108
+ GCC_except_table16109
+ GCC_except_table16114
+ GCC_except_table16115
+ GCC_except_table16117
+ GCC_except_table16127
+ GCC_except_table1613
+ GCC_except_table16133
+ GCC_except_table16134
+ GCC_except_table16140
+ GCC_except_table16147
+ GCC_except_table16150
+ GCC_except_table16196
+ GCC_except_table16211
+ GCC_except_table16214
+ GCC_except_table16231
+ GCC_except_table16240
+ GCC_except_table16245
+ GCC_except_table16248
+ GCC_except_table16250
+ GCC_except_table16257
+ GCC_except_table16358
+ GCC_except_table16364
+ GCC_except_table16389
+ GCC_except_table16390
+ GCC_except_table16397
+ GCC_except_table16406
+ GCC_except_table16415
+ GCC_except_table16420
+ GCC_except_table16437
+ GCC_except_table16496
+ GCC_except_table16498
+ GCC_except_table16590
+ GCC_except_table1660
+ GCC_except_table16651
+ GCC_except_table16666
+ GCC_except_table1671
+ GCC_except_table16774
+ GCC_except_table16795
+ GCC_except_table16801
+ GCC_except_table16806
+ GCC_except_table16814
+ GCC_except_table1682
+ GCC_except_table16843
+ GCC_except_table16855
+ GCC_except_table16899
+ GCC_except_table16962
+ GCC_except_table16967
+ GCC_except_table16975
+ GCC_except_table16985
+ GCC_except_table16997
+ GCC_except_table17011
+ GCC_except_table17017
+ GCC_except_table17027
+ GCC_except_table17040
+ GCC_except_table17050
+ GCC_except_table17060
+ GCC_except_table17090
+ GCC_except_table17094
+ GCC_except_table17096
+ GCC_except_table17098
+ GCC_except_table17159
+ GCC_except_table17211
+ GCC_except_table17222
+ GCC_except_table17242
+ GCC_except_table17249
+ GCC_except_table17253
+ GCC_except_table17315
+ GCC_except_table17325
+ GCC_except_table17337
+ GCC_except_table17338
+ GCC_except_table17342
+ GCC_except_table17349
+ GCC_except_table17353
+ GCC_except_table17354
+ GCC_except_table17390
+ GCC_except_table17396
+ GCC_except_table17480
+ GCC_except_table17517
+ GCC_except_table17531
+ GCC_except_table17583
+ GCC_except_table17601
+ GCC_except_table17641
+ GCC_except_table17646
+ GCC_except_table17685
+ GCC_except_table17697
+ GCC_except_table17700
+ GCC_except_table17712
+ GCC_except_table17737
+ GCC_except_table17768
+ GCC_except_table17769
+ GCC_except_table17770
+ GCC_except_table17805
+ GCC_except_table17818
+ GCC_except_table17859
+ GCC_except_table17866
+ GCC_except_table17870
+ GCC_except_table17884
+ GCC_except_table17900
+ GCC_except_table17901
+ GCC_except_table17928
+ GCC_except_table17947
+ GCC_except_table17985
+ GCC_except_table18051
+ GCC_except_table18076
+ GCC_except_table18078
+ GCC_except_table18080
+ GCC_except_table18082
+ GCC_except_table18084
+ GCC_except_table18086
+ GCC_except_table18090
+ GCC_except_table18139
+ GCC_except_table1827
+ GCC_except_table18277
+ GCC_except_table1833
+ GCC_except_table18336
+ GCC_except_table18347
+ GCC_except_table18349
+ GCC_except_table18406
+ GCC_except_table18417
+ GCC_except_table18431
+ GCC_except_table18436
+ GCC_except_table18440
+ GCC_except_table18456
+ GCC_except_table18457
+ GCC_except_table18464
+ GCC_except_table18469
+ GCC_except_table18499
+ GCC_except_table185
+ GCC_except_table18528
+ GCC_except_table18531
+ GCC_except_table18548
+ GCC_except_table18554
+ GCC_except_table18596
+ GCC_except_table18614
+ GCC_except_table18639
+ GCC_except_table18647
+ GCC_except_table18649
+ GCC_except_table18658
+ GCC_except_table18660
+ GCC_except_table18662
+ GCC_except_table18667
+ GCC_except_table18671
+ GCC_except_table18675
+ GCC_except_table18677
+ GCC_except_table18681
+ GCC_except_table18683
+ GCC_except_table18687
+ GCC_except_table18691
+ GCC_except_table18743
+ GCC_except_table18760
+ GCC_except_table18787
+ GCC_except_table18926
+ GCC_except_table18928
+ GCC_except_table18966
+ GCC_except_table18974
+ GCC_except_table18997
+ GCC_except_table18998
+ GCC_except_table18999
+ GCC_except_table19003
+ GCC_except_table19007
+ GCC_except_table19008
+ GCC_except_table19016
+ GCC_except_table19018
+ GCC_except_table19020
+ GCC_except_table19025
+ GCC_except_table19033
+ GCC_except_table19035
+ GCC_except_table19050
+ GCC_except_table19052
+ GCC_except_table19056
+ GCC_except_table19060
+ GCC_except_table19061
+ GCC_except_table19071
+ GCC_except_table19073
+ GCC_except_table19080
+ GCC_except_table19082
+ GCC_except_table19084
+ GCC_except_table19086
+ GCC_except_table19088
+ GCC_except_table19098
+ GCC_except_table19102
+ GCC_except_table19106
+ GCC_except_table19108
+ GCC_except_table19110
+ GCC_except_table19114
+ GCC_except_table19116
+ GCC_except_table19118
+ GCC_except_table19120
+ GCC_except_table19124
+ GCC_except_table19125
+ GCC_except_table19126
+ GCC_except_table19130
+ GCC_except_table19131
+ GCC_except_table19136
+ GCC_except_table19141
+ GCC_except_table19145
+ GCC_except_table19149
+ GCC_except_table19150
+ GCC_except_table19166
+ GCC_except_table19168
+ GCC_except_table19175
+ GCC_except_table19176
+ GCC_except_table19187
+ GCC_except_table19191
+ GCC_except_table19195
+ GCC_except_table19293
+ GCC_except_table19299
+ GCC_except_table19319
+ GCC_except_table19320
+ GCC_except_table19321
+ GCC_except_table19328
+ GCC_except_table19341
+ GCC_except_table19343
+ GCC_except_table19453
+ GCC_except_table19465
+ GCC_except_table19484
+ GCC_except_table19562
+ GCC_except_table19564
+ GCC_except_table19569
+ GCC_except_table19574
+ GCC_except_table19582
+ GCC_except_table19603
+ GCC_except_table19609
+ GCC_except_table19613
+ GCC_except_table19615
+ GCC_except_table19619
+ GCC_except_table19629
+ GCC_except_table19634
+ GCC_except_table19636
+ GCC_except_table19644
+ GCC_except_table19648
+ GCC_except_table19652
+ GCC_except_table19717
+ GCC_except_table19779
+ GCC_except_table19797
+ GCC_except_table198
+ GCC_except_table19872
+ GCC_except_table19882
+ GCC_except_table19891
+ GCC_except_table19899
+ GCC_except_table19901
+ GCC_except_table19915
+ GCC_except_table20056
+ GCC_except_table2006
+ GCC_except_table20067
+ GCC_except_table20104
+ GCC_except_table20110
+ GCC_except_table20119
+ GCC_except_table2012
+ GCC_except_table20145
+ GCC_except_table20179
+ GCC_except_table20188
+ GCC_except_table20194
+ GCC_except_table20202
+ GCC_except_table20211
+ GCC_except_table20217
+ GCC_except_table20223
+ GCC_except_table20234
+ GCC_except_table20246
+ GCC_except_table20393
+ GCC_except_table20397
+ GCC_except_table20436
+ GCC_except_table20440
+ GCC_except_table20442
+ GCC_except_table20470
+ GCC_except_table20510
+ GCC_except_table20514
+ GCC_except_table20518
+ GCC_except_table20522
+ GCC_except_table20526
+ GCC_except_table20530
+ GCC_except_table20534
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
+ GCC_except_table20627
+ GCC_except_table20630
+ GCC_except_table20635
+ GCC_except_table20638
+ GCC_except_table20666
+ GCC_except_table20670
+ GCC_except_table20671
+ GCC_except_table20672
+ GCC_except_table20678
+ GCC_except_table20679
+ GCC_except_table20691
+ GCC_except_table20759
+ GCC_except_table20803
+ GCC_except_table20810
+ GCC_except_table20816
+ GCC_except_table20859
+ GCC_except_table20863
+ GCC_except_table20878
+ GCC_except_table20906
+ GCC_except_table20931
+ GCC_except_table20934
+ GCC_except_table20980
+ GCC_except_table20997
+ GCC_except_table21015
+ GCC_except_table21031
+ GCC_except_table21035
+ GCC_except_table21036
+ GCC_except_table21042
+ GCC_except_table21047
+ GCC_except_table21050
+ GCC_except_table21058
+ GCC_except_table21063
+ GCC_except_table21065
+ GCC_except_table21066
+ GCC_except_table21074
+ GCC_except_table21078
+ GCC_except_table21081
+ GCC_except_table21082
+ GCC_except_table21086
+ GCC_except_table21103
+ GCC_except_table21105
+ GCC_except_table21107
+ GCC_except_table21109
+ GCC_except_table21111
+ GCC_except_table21116
+ GCC_except_table21120
+ GCC_except_table21131
+ GCC_except_table21257
+ GCC_except_table21277
+ GCC_except_table21283
+ GCC_except_table21301
+ GCC_except_table21403
+ GCC_except_table21476
+ GCC_except_table21496
+ GCC_except_table21506
+ GCC_except_table21566
+ GCC_except_table21694
+ GCC_except_table21695
+ GCC_except_table21715
+ GCC_except_table21717
+ GCC_except_table21724
+ GCC_except_table21742
+ GCC_except_table21752
+ GCC_except_table21770
+ GCC_except_table21818
+ GCC_except_table21825
+ GCC_except_table21841
+ GCC_except_table21895
+ GCC_except_table21911
+ GCC_except_table21928
+ GCC_except_table21933
+ GCC_except_table21945
+ GCC_except_table21947
+ GCC_except_table21976
+ GCC_except_table22032
+ GCC_except_table22044
+ GCC_except_table22046
+ GCC_except_table22077
+ GCC_except_table22089
+ GCC_except_table22094
+ GCC_except_table22101
+ GCC_except_table22144
+ GCC_except_table22147
+ GCC_except_table22175
+ GCC_except_table222
+ GCC_except_table22206
+ GCC_except_table22295
+ GCC_except_table22341
+ GCC_except_table22345
+ GCC_except_table22347
+ GCC_except_table22349
+ GCC_except_table2237
+ GCC_except_table22376
+ GCC_except_table22448
+ GCC_except_table22449
+ GCC_except_table22489
+ GCC_except_table22529
+ GCC_except_table2256
+ GCC_except_table22598
+ GCC_except_table2261
+ GCC_except_table2269
+ GCC_except_table2272
+ GCC_except_table2297
+ GCC_except_table23005
+ GCC_except_table2302
+ GCC_except_table2320
+ GCC_except_table2322
+ GCC_except_table23304
+ GCC_except_table23316
+ GCC_except_table23324
+ GCC_except_table23371
+ GCC_except_table23375
+ GCC_except_table23431
+ GCC_except_table23443
+ GCC_except_table23459
+ GCC_except_table23560
+ GCC_except_table23569
+ GCC_except_table2357
+ GCC_except_table23599
+ GCC_except_table23675
+ GCC_except_table23676
+ GCC_except_table2373
+ GCC_except_table23743
+ GCC_except_table23761
+ GCC_except_table23768
+ GCC_except_table23792
+ GCC_except_table23967
+ GCC_except_table23986
+ GCC_except_table23990
+ GCC_except_table24035
+ GCC_except_table24069
+ GCC_except_table24101
+ GCC_except_table24146
+ GCC_except_table24147
+ GCC_except_table24213
+ GCC_except_table24231
+ GCC_except_table24245
+ GCC_except_table24254
+ GCC_except_table24256
+ GCC_except_table24260
+ GCC_except_table24267
+ GCC_except_table24283
+ GCC_except_table24290
+ GCC_except_table24317
+ GCC_except_table24518
+ GCC_except_table24519
+ GCC_except_table24523
+ GCC_except_table24524
+ GCC_except_table24528
+ GCC_except_table24530
+ GCC_except_table24535
+ GCC_except_table24537
+ GCC_except_table2454
+ GCC_except_table24540
+ GCC_except_table24541
+ GCC_except_table24542
+ GCC_except_table24545
+ GCC_except_table24546
+ GCC_except_table24547
+ GCC_except_table24577
+ GCC_except_table24580
+ GCC_except_table246
+ GCC_except_table24603
+ GCC_except_table24606
+ GCC_except_table24607
+ GCC_except_table24612
+ GCC_except_table24617
+ GCC_except_table24621
+ GCC_except_table24684
+ GCC_except_table24691
+ GCC_except_table24693
+ GCC_except_table24695
+ GCC_except_table24697
+ GCC_except_table24699
+ GCC_except_table24707
+ GCC_except_table24709
+ GCC_except_table24723
+ GCC_except_table24752
+ GCC_except_table24759
+ GCC_except_table24761
+ GCC_except_table24763
+ GCC_except_table24765
+ GCC_except_table24773
+ GCC_except_table24789
+ GCC_except_table24792
+ GCC_except_table24796
+ GCC_except_table24800
+ GCC_except_table24810
+ GCC_except_table24815
+ GCC_except_table24819
+ GCC_except_table24823
+ GCC_except_table24833
+ GCC_except_table24837
+ GCC_except_table24841
+ GCC_except_table24845
+ GCC_except_table24847
+ GCC_except_table24859
+ GCC_except_table24883
+ GCC_except_table24899
+ GCC_except_table24917
+ GCC_except_table24918
+ GCC_except_table24921
+ GCC_except_table24946
+ GCC_except_table24948
+ GCC_except_table24950
+ GCC_except_table24973
+ GCC_except_table24976
+ GCC_except_table24979
+ GCC_except_table24981
+ GCC_except_table25035
+ GCC_except_table2506
+ GCC_except_table25093
+ GCC_except_table25097
+ GCC_except_table25100
+ GCC_except_table25103
+ GCC_except_table25110
+ GCC_except_table25136
+ GCC_except_table25139
+ GCC_except_table25151
+ GCC_except_table25155
+ GCC_except_table25168
+ GCC_except_table25174
+ GCC_except_table25178
+ GCC_except_table25202
+ GCC_except_table25214
+ GCC_except_table25217
+ GCC_except_table25224
+ GCC_except_table25232
+ GCC_except_table25233
+ GCC_except_table25234
+ GCC_except_table25241
+ GCC_except_table2526
+ GCC_except_table25334
+ GCC_except_table25335
+ GCC_except_table25336
+ GCC_except_table25337
+ GCC_except_table25341
+ GCC_except_table25345
+ GCC_except_table25346
+ GCC_except_table25347
+ GCC_except_table25350
+ GCC_except_table25380
+ GCC_except_table25388
+ GCC_except_table25392
+ GCC_except_table2542
+ GCC_except_table25420
+ GCC_except_table25435
+ GCC_except_table25469
+ GCC_except_table25481
+ GCC_except_table25517
+ GCC_except_table25521
+ GCC_except_table25552
+ GCC_except_table25558
+ GCC_except_table25627
+ GCC_except_table25696
+ GCC_except_table25774
+ GCC_except_table25783
+ GCC_except_table25822
+ GCC_except_table25825
+ GCC_except_table25852
+ GCC_except_table25855
+ GCC_except_table25858
+ GCC_except_table25861
+ GCC_except_table25864
+ GCC_except_table25867
+ GCC_except_table25925
+ GCC_except_table25928
+ GCC_except_table25931
+ GCC_except_table25969
+ GCC_except_table25975
+ GCC_except_table26023
+ GCC_except_table26056
+ GCC_except_table26061
+ GCC_except_table26063
+ GCC_except_table26065
+ GCC_except_table2611
+ GCC_except_table26111
+ GCC_except_table2612
+ GCC_except_table26165
+ GCC_except_table26170
+ GCC_except_table26181
+ GCC_except_table26202
+ GCC_except_table26209
+ GCC_except_table26211
+ GCC_except_table26212
+ GCC_except_table26344
+ GCC_except_table26350
+ GCC_except_table26372
+ GCC_except_table26411
+ GCC_except_table26414
+ GCC_except_table26420
+ GCC_except_table26425
+ GCC_except_table26429
+ GCC_except_table26464
+ GCC_except_table26470
+ GCC_except_table26472
+ GCC_except_table26513
+ GCC_except_table26657
+ GCC_except_table26661
+ GCC_except_table26664
+ GCC_except_table26666
+ GCC_except_table26778
+ GCC_except_table26973
+ GCC_except_table26980
+ GCC_except_table26984
+ GCC_except_table26995
+ GCC_except_table27003
+ GCC_except_table27005
+ GCC_except_table27010
+ GCC_except_table27012
+ GCC_except_table27031
+ GCC_except_table27035
+ GCC_except_table27053
+ GCC_except_table2765
+ GCC_except_table2767
+ GCC_except_table2779
+ GCC_except_table2783
+ GCC_except_table2808
+ GCC_except_table2811
+ GCC_except_table2851
+ GCC_except_table2860
+ GCC_except_table2863
+ GCC_except_table2870
+ GCC_except_table2879
+ GCC_except_table2923
+ GCC_except_table2930
+ GCC_except_table2986
+ GCC_except_table3026
+ GCC_except_table312
+ GCC_except_table3135
+ GCC_except_table3144
+ GCC_except_table3165
+ GCC_except_table319
+ GCC_except_table3361
+ GCC_except_table3367
+ GCC_except_table3460
+ GCC_except_table3462
+ GCC_except_table3470
+ GCC_except_table3488
+ GCC_except_table3499
+ GCC_except_table3515
+ GCC_except_table3544
+ GCC_except_table3564
+ GCC_except_table3573
+ GCC_except_table3577
+ GCC_except_table3581
+ GCC_except_table3583
+ GCC_except_table3587
+ GCC_except_table3591
+ GCC_except_table3638
+ GCC_except_table366
+ GCC_except_table3894
+ GCC_except_table3897
+ GCC_except_table3900
+ GCC_except_table3903
+ GCC_except_table3906
+ GCC_except_table3916
+ GCC_except_table3974
+ GCC_except_table4012
+ GCC_except_table4023
+ GCC_except_table4029
+ GCC_except_table4050
+ GCC_except_table4061
+ GCC_except_table4090
+ GCC_except_table4152
+ GCC_except_table4157
+ GCC_except_table4168
+ GCC_except_table4173
+ GCC_except_table4176
+ GCC_except_table4200
+ GCC_except_table4202
+ GCC_except_table4211
+ GCC_except_table4212
+ GCC_except_table4214
+ GCC_except_table4232
+ GCC_except_table4235
+ GCC_except_table4241
+ GCC_except_table4270
+ GCC_except_table4273
+ GCC_except_table4292
+ GCC_except_table4296
+ GCC_except_table4300
+ GCC_except_table4311
+ GCC_except_table4327
+ GCC_except_table4478
+ GCC_except_table4487
+ GCC_except_table4495
+ GCC_except_table4497
+ GCC_except_table4503
+ GCC_except_table4505
+ GCC_except_table452
+ GCC_except_table4528
+ GCC_except_table4530
+ GCC_except_table4538
+ GCC_except_table4542
+ GCC_except_table4548
+ GCC_except_table455
+ GCC_except_table4571
+ GCC_except_table458
+ GCC_except_table4604
+ GCC_except_table461
+ GCC_except_table464
+ GCC_except_table4654
+ GCC_except_table4658
+ GCC_except_table470
+ GCC_except_table4837
+ GCC_except_table4844
+ GCC_except_table4901
+ GCC_except_table4923
+ GCC_except_table4927
+ GCC_except_table4956
+ GCC_except_table502
+ GCC_except_table5055
+ GCC_except_table5063
+ GCC_except_table5089
+ GCC_except_table5161
+ GCC_except_table5264
+ GCC_except_table5303
+ GCC_except_table5311
+ GCC_except_table5313
+ GCC_except_table5316
+ GCC_except_table5534
+ GCC_except_table5549
+ GCC_except_table5575
+ GCC_except_table5653
+ GCC_except_table566
+ GCC_except_table5666
+ GCC_except_table5728
+ GCC_except_table5747
+ GCC_except_table5755
+ GCC_except_table5759
+ GCC_except_table5768
+ GCC_except_table5771
+ GCC_except_table582
+ GCC_except_table5831
+ GCC_except_table5836
+ GCC_except_table5846
+ GCC_except_table5856
+ GCC_except_table5887
+ GCC_except_table5898
+ GCC_except_table5905
+ GCC_except_table5913
+ GCC_except_table5915
+ GCC_except_table5950
+ GCC_except_table5951
+ GCC_except_table5954
+ GCC_except_table5955
+ GCC_except_table5963
+ GCC_except_table5976
+ GCC_except_table6069
+ GCC_except_table6071
+ GCC_except_table6094
+ GCC_except_table613
+ GCC_except_table6132
+ GCC_except_table6136
+ GCC_except_table6140
+ GCC_except_table6161
+ GCC_except_table6166
+ GCC_except_table6171
+ GCC_except_table6175
+ GCC_except_table6193
+ GCC_except_table6196
+ GCC_except_table6198
+ GCC_except_table620
+ GCC_except_table6202
+ GCC_except_table6204
+ GCC_except_table6263
+ GCC_except_table6290
+ GCC_except_table6295
+ GCC_except_table6299
+ GCC_except_table6303
+ GCC_except_table6308
+ GCC_except_table6313
+ GCC_except_table6321
+ GCC_except_table6325
+ GCC_except_table6336
+ GCC_except_table6347
+ GCC_except_table6350
+ GCC_except_table6352
+ GCC_except_table6363
+ GCC_except_table6364
+ GCC_except_table6366
+ GCC_except_table6368
+ GCC_except_table637
+ GCC_except_table6371
+ GCC_except_table6373
+ GCC_except_table6376
+ GCC_except_table6389
+ GCC_except_table6398
+ GCC_except_table6402
+ GCC_except_table6404
+ GCC_except_table6410
+ GCC_except_table6412
+ GCC_except_table6414
+ GCC_except_table6415
+ GCC_except_table6417
+ GCC_except_table6419
+ GCC_except_table6420
+ GCC_except_table6421
+ GCC_except_table6423
+ GCC_except_table6425
+ GCC_except_table6426
+ GCC_except_table6427
+ GCC_except_table6428
+ GCC_except_table6458
+ GCC_except_table6537
+ GCC_except_table6603
+ GCC_except_table6719
+ GCC_except_table6788
+ GCC_except_table7001
+ GCC_except_table7060
+ GCC_except_table7106
+ GCC_except_table7113
+ GCC_except_table7124
+ GCC_except_table7144
+ GCC_except_table7148
+ GCC_except_table7151
+ GCC_except_table7154
+ GCC_except_table7158
+ GCC_except_table7163
+ GCC_except_table7171
+ GCC_except_table7177
+ GCC_except_table7180
+ GCC_except_table7182
+ GCC_except_table7188
+ GCC_except_table719
+ GCC_except_table7211
+ GCC_except_table7215
+ GCC_except_table7225
+ GCC_except_table7235
+ GCC_except_table7242
+ GCC_except_table7244
+ GCC_except_table7249
+ GCC_except_table726
+ GCC_except_table7264
+ GCC_except_table7266
+ GCC_except_table7296
+ GCC_except_table7299
+ GCC_except_table7301
+ GCC_except_table7314
+ GCC_except_table7318
+ GCC_except_table7323
+ GCC_except_table7325
+ GCC_except_table7328
+ GCC_except_table7333
+ GCC_except_table7404
+ GCC_except_table741
+ GCC_except_table7410
+ GCC_except_table7414
+ GCC_except_table7418
+ GCC_except_table7419
+ GCC_except_table7421
+ GCC_except_table7424
+ GCC_except_table7427
+ GCC_except_table743
+ GCC_except_table7430
+ GCC_except_table7432
+ GCC_except_table7434
+ GCC_except_table7436
+ GCC_except_table7438
+ GCC_except_table7441
+ GCC_except_table7443
+ GCC_except_table7454
+ GCC_except_table7458
+ GCC_except_table7463
+ GCC_except_table7467
+ GCC_except_table7482
+ GCC_except_table7486
+ GCC_except_table749
+ GCC_except_table7490
+ GCC_except_table7494
+ GCC_except_table7498
+ GCC_except_table7513
+ GCC_except_table7517
+ GCC_except_table7523
+ GCC_except_table7527
+ GCC_except_table7531
+ GCC_except_table7559
+ GCC_except_table7563
+ GCC_except_table7589
+ GCC_except_table7591
+ GCC_except_table760
+ GCC_except_table7606
+ GCC_except_table766
+ GCC_except_table780
+ GCC_except_table7839
+ GCC_except_table7845
+ GCC_except_table785
+ GCC_except_table7858
+ GCC_except_table7859
+ GCC_except_table7872
+ GCC_except_table7894
+ GCC_except_table7895
+ GCC_except_table790
+ GCC_except_table7906
+ GCC_except_table7935
+ GCC_except_table7953
+ GCC_except_table7955
+ GCC_except_table7961
+ GCC_except_table7965
+ GCC_except_table7971
+ GCC_except_table7978
+ GCC_except_table7981
+ GCC_except_table8038
+ GCC_except_table8042
+ GCC_except_table8044
+ GCC_except_table8055
+ GCC_except_table8062
+ GCC_except_table8126
+ GCC_except_table8138
+ GCC_except_table8140
+ GCC_except_table816
+ GCC_except_table8162
+ GCC_except_table8168
+ GCC_except_table8172
+ GCC_except_table8191
+ GCC_except_table8197
+ GCC_except_table8239
+ GCC_except_table8252
+ GCC_except_table8257
+ GCC_except_table8259
+ GCC_except_table8264
+ GCC_except_table8274
+ GCC_except_table8286
+ GCC_except_table8289
+ GCC_except_table8298
+ GCC_except_table8303
+ GCC_except_table8331
+ GCC_except_table8389
+ GCC_except_table8390
+ GCC_except_table8402
+ GCC_except_table8408
+ GCC_except_table8413
+ GCC_except_table8414
+ GCC_except_table8448
+ GCC_except_table8453
+ GCC_except_table8459
+ GCC_except_table8471
+ GCC_except_table8484
+ GCC_except_table8497
+ GCC_except_table8521
+ GCC_except_table855
+ GCC_except_table8551
+ GCC_except_table8586
+ GCC_except_table8589
+ GCC_except_table8642
+ GCC_except_table8650
+ GCC_except_table866
+ GCC_except_table8665
+ GCC_except_table8667
+ GCC_except_table870
+ GCC_except_table8832
+ GCC_except_table8833
+ GCC_except_table8857
+ GCC_except_table887
+ GCC_except_table893
+ GCC_except_table902
+ GCC_except_table9033
+ GCC_except_table9037
+ GCC_except_table9050
+ GCC_except_table9054
+ GCC_except_table909
+ GCC_except_table9110
+ GCC_except_table9122
+ GCC_except_table9129
+ GCC_except_table9132
+ GCC_except_table9137
+ GCC_except_table9138
+ GCC_except_table914
+ GCC_except_table9163
+ GCC_except_table9187
+ GCC_except_table9191
+ GCC_except_table9194
+ GCC_except_table9201
+ GCC_except_table9205
+ GCC_except_table921
+ GCC_except_table9247
+ GCC_except_table925
+ GCC_except_table9263
+ GCC_except_table930
+ GCC_except_table935
+ GCC_except_table9386
+ GCC_except_table9420
+ GCC_except_table9424
+ GCC_except_table9430
+ GCC_except_table9432
+ GCC_except_table9438
+ GCC_except_table9441
+ GCC_except_table9478
+ GCC_except_table9524
+ GCC_except_table953
+ GCC_except_table9746
+ GCC_except_table9747
+ GCC_except_table9748
+ GCC_except_table9765
+ GCC_except_table9770
+ GCC_except_table9783
+ GCC_except_table9818
+ GCC_except_table9829
+ GCC_except_table984
+ GCC_except_table9885
+ GCC_except_table992
+ GCC_except_table9970
+ GCC_except_table9971
+ IMDPersistenceLibraryCore.frameworkLibrary
+ IMSharedUtilitiesLibrary
+ OBJC_IVAR_$_PLAssetsdConnectionAuthorization._restrictedResourcesAccessAuthorized
+ OBJC_IVAR_$_PLAssetsdCrashRecoveryClientAuthorization._restrictedResourcesAccessAuthorized
+ OBJC_IVAR_$_PLFileSystemAssetImporter._keywordUUIDRemapping
+ OBJC_IVAR_$_PLManagedKeyword._fromRebuild
+ OBJC_IVAR_$_PLManagedKeyword._needsPersistenceUpdate
+ OBJC_IVAR_$_PLMediaAnalysisEmbeddingSearchOptions._embeddingSearchMode
+ OBJC_IVAR_$_PLMomentGenerationThrottle._maxDelayBetweenRuns
+ OBJC_IVAR_$_PLMomentGenerationThrottle._maxIntervalBeforeDelayReset
+ OBJC_IVAR_$_PLMomentGenerationThrottle._minDelayBetweenRuns
+ OBJC_IVAR_$_PLPrimaryResourceDataStoreKeyHelper._pathManager
+ OBJC_IVAR_$_PLPrimaryResourceDataStoreKeyHelper.cvtBaseData
+ OBJC_IVAR_$_PLPrimaryResourceDataStoreKeyHelper.restrictedBaseData
+ OBJC_IVAR_$_PLSearchIndexingContext._contactStore
+ OBJC_IVAR_$_PLSearchIndexingMessagesFetcher._displayNameCache
+ OBJC_IVAR_$_PLSearchIndexingMessagesFetcher._indexingContext
+ OBJC_IVAR_$_PLSearchIndexingMessagesFetcher._libraryIdentifier
+ OBJC_IVAR_$_PLSearchIndexingMessagesFetcher._messageGUIDCache
+ OBJC_IVAR_$_PLTextEmbeddingServiceOptions._useCache
+ PLSearchLeoMessagesSenderReceiverSPLEnabled.enabled
+ PLSearchLeoMessagesSenderReceiverSPLEnabled.onceToken
+ PLSearchLeoMessagesSenderReceiverSyndicationEnabled.enabled
+ PLSearchLeoMessagesSenderReceiverSyndicationEnabled.onceToken
+ PLSearchUnifiedMADEmbeddingSearchEnabled.enabled
+ PLSearchUnifiedMADEmbeddingSearchEnabled.onceToken
+ _IMSharedUtilitiesLibraryCore
+ _OBJC_CLASS_$_CNContactStoreConfiguration
+ _OBJC_CLASS_$_PLModelMigrationAction_PersistKeywordsToJournalAndFilesystem
+ _OBJC_CLASS_$_PLModelMigrationAction_RelocateUBFOriginalResourceTypes
+ _OBJC_CLASS_$_PLSearchIndexingMessagesFetcher
+ _OBJC_CLASS_$_PNContentClassifier
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
+ _PLSearchLeoMessagesSenderReceiverSyndicationEnabled
+ _PLSearchUnifiedMADEmbeddingSearchEnabled
+ _PhotoLibraryServicesEntitlementAllowRestrictedResourcesRead
+ __109-[PLCollectionShareMigrator _continueMigrationSetupForShareUUID:silent:progress:plLibrary:completionHandler:]_block_invoke
+ __119-[PLBackgroundJobResourceUploadExtensionRunnerWorker _handleProcessingResult:bundleIdentifier:library:completionBlock:]_block_invoke
+ __146+[PLCollectionShareMigrationSessionPhaseSilentMigrationCleanup revertSilentMigrationForOriginatingScopeIdentifier:photoLibrary:completionHandler:]_block_invoke
+ __152-[PLSearchIndexingEngine _inq_donateSpotlightItemsByBundleID:leoDonatableItems:leoLexemeScoreUpdates:deleteIdentifiers:spotlightClientState:completion:]_block_invoke
+ __79+[PLManagedAsset(Share) _directUploadFullResourcesForProxyAssets:photoLibrary:]_block_invoke
+ __96-[PLModelMigrator _importFileSystemImportAssets:intoLibrary:type:progress:keywordUUIDRemapping:]_block_invoke
+ __98-[PLCollectionShareSharedStreamBackend checkServerForChangesForCollectionShare:completionHandler:]_block_invoke
+ __98-[PLCollectionShareSharedStreamBackend checkServerForChangesForCollectionShare:completionHandler:]_block_invoke_2
+ __98-[PLCollectionShareSharedStreamBackend checkServerForChangesForCollectionShare:completionHandler:]_block_invoke_3
+ __IMSharedUtilitiesLibraryCore_block_invoke
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
+ ___56-[PLDirectoryJournal enumeratePayloadsUsingBlock:error:]_block_invoke_2
+ ___59-[PLSearchIndexingEngine pauseProcessingIncrementalUpdates]_block_invoke
+ ___60-[PLCloudSharedCommentsJob _runDaemonSideWaitUntilFinished:]_block_invoke
+ ___61-[PLCloudSharedAssetSaveJob _runDaemonSideWaitUntilFinished:]_block_invoke
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
+ ___IMDPersistenceLibraryCore_block_invoke
+ ___PLSearchLeoMessagesSenderReceiverSPLEnabled_block_invoke
+ ___PLSearchLeoMessagesSenderReceiverSyndicationEnabled_block_invoke
+ ___PLSearchUnifiedMADEmbeddingSearchEnabled_block_invoke
+ ___block_descriptor_104_e8_32s40s48s56s64bs72r80n11_8_8_s0_t8w8_e5_v8?0l
+ ___block_descriptor_104_e8_32s40s48s56s64s72s80s88bs96bs_e29_v16?0"MSASAssetCollection"8l
+ ___block_descriptor_113_e8_32s40s48s56r64r72r80r88r96r_e5_v8?0l
+ ___block_descriptor_169_e8_32s40s48s56s64s72s80s88s96s104s112s120bs128r136n11_8_8_s0_t8w8_e5_v8?0l
+ ___block_descriptor_48_e8_32r40r_e26_v16?0"IMDMessageRecord"8l
+ ___block_descriptor_48_e8_32s40s_e42_v24?0"PLKeywordJournalEntryPayload"8^B16l
+ ___block_descriptor_64_e8_32s40s48r56r_e26_v16?0"PLManagedKeyword"8l
+ ___block_descriptor_64_e8_32s40s48s56bs_e21_v16?0"MSASComment"8l
+ ___block_descriptor_64_e8_32s40s48s_e24_v16?0"PLManagedAsset"8l
+ ___block_descriptor_72_e8_32s40s48s56r64r_e32_v16?0"NSManagedObjectContext"8l
+ ___block_descriptor_73_e8_32s40s48s56s64bs_e5_v8?0l
+ ___block_descriptor_81_e8_32s40s48s56s64s72s_e35_v16?0"PLFileSystemAssetImporter"8l
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e17_v16?0"NSArray"8l
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e17_v16?0"NSError"8l
+ ___block_descriptor_89_e8_32s40s48s56s64s72s80r_e5_v8?0l
+ ___block_descriptor_96_e8_32s40s48s56s64s72s80bs88bs_e17_v16?0"NSArray"8l
+ ___copy_helper_block_e8_32s40s48s56s64s72s80b88b
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88b96b
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120b128r136n11_8_8_s0_t8w8
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128r136n4_8_s0
+ ___getIMContactStoreClass_block_invoke
+ ___getIMDDatabaseClass_block_invoke
+ ___getIMMessageGuidFromIMFileTransferGuidSymbolLoc_block_invoke
+ _audit_stringIMDPersistence
+ _getIMContactStoreClass
+ _getIMDDatabaseClass
+ _getIMMessageGuidFromIMFileTransferGuidSymbolLoc
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
+ audit_stringIMSharedUtilities
+ getIMContactStoreClass.softClass
+ getIMDDatabaseClass.softClass
+ getIMMessageGuidFromIMFileTransferGuidSymbolLoc.ptr
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
- GCC_except_table10020
- GCC_except_table10025
- GCC_except_table10029
- GCC_except_table10046
- GCC_except_table10053
- GCC_except_table10065
- GCC_except_table10067
- GCC_except_table10081
- GCC_except_table10140
- GCC_except_table10159
- GCC_except_table10173
- GCC_except_table10177
- GCC_except_table10189
- GCC_except_table10201
- GCC_except_table10213
- GCC_except_table10215
- GCC_except_table10229
- GCC_except_table10231
- GCC_except_table10238
- GCC_except_table10280
- GCC_except_table10295
- GCC_except_table10305
- GCC_except_table10317
- GCC_except_table10328
- GCC_except_table10336
- GCC_except_table1034
- GCC_except_table10355
- GCC_except_table10370
- GCC_except_table1038
- GCC_except_table10380
- GCC_except_table10459
- GCC_except_table10465
- GCC_except_table10467
- GCC_except_table10471
- GCC_except_table10473
- GCC_except_table10479
- GCC_except_table10483
- GCC_except_table10485
- GCC_except_table10491
- GCC_except_table10520
- GCC_except_table10578
- GCC_except_table1058
- GCC_except_table10581
- GCC_except_table10632
- GCC_except_table10683
- GCC_except_table10689
- GCC_except_table10691
- GCC_except_table10705
- GCC_except_table10711
- GCC_except_table10713
- GCC_except_table10724
- GCC_except_table10728
- GCC_except_table10733
- GCC_except_table10867
- GCC_except_table10910
- GCC_except_table10992
- GCC_except_table10993
- GCC_except_table10996
- GCC_except_table10997
- GCC_except_table11000
- GCC_except_table11001
- GCC_except_table11003
- GCC_except_table11009
- GCC_except_table11013
- GCC_except_table11015
- GCC_except_table11017
- GCC_except_table11019
- GCC_except_table11021
- GCC_except_table11023
- GCC_except_table11025
- GCC_except_table11027
- GCC_except_table11029
- GCC_except_table11031
- GCC_except_table11033
- GCC_except_table11036
- GCC_except_table11039
- GCC_except_table11043
- GCC_except_table11046
- GCC_except_table11049
- GCC_except_table11051
- GCC_except_table11053
- GCC_except_table11055
- GCC_except_table11059
- GCC_except_table11060
- GCC_except_table11063
- GCC_except_table11069
- GCC_except_table11072
- GCC_except_table11077
- GCC_except_table11083
- GCC_except_table11093
- GCC_except_table11097
- GCC_except_table11099
- GCC_except_table11100
- GCC_except_table11102
- GCC_except_table11103
- GCC_except_table11105
- GCC_except_table11106
- GCC_except_table11107
- GCC_except_table11109
- GCC_except_table11110
- GCC_except_table11112
- GCC_except_table11113
- GCC_except_table11117
- GCC_except_table11126
- GCC_except_table11132
- GCC_except_table1117
- GCC_except_table11204
- GCC_except_table11208
- GCC_except_table11219
- GCC_except_table11289
- GCC_except_table11371
- GCC_except_table1138
- GCC_except_table11412
- GCC_except_table11424
- GCC_except_table11524
- GCC_except_table11529
- GCC_except_table11552
- GCC_except_table11605
- GCC_except_table11661
- GCC_except_table11870
- GCC_except_table11911
- GCC_except_table1195
- GCC_except_table12139
- GCC_except_table12172
- GCC_except_table1218
- GCC_except_table12196
- GCC_except_table12197
- GCC_except_table12198
- GCC_except_table12199
- GCC_except_table12200
- GCC_except_table12202
- GCC_except_table12204
- GCC_except_table12219
- GCC_except_table1224
- GCC_except_table12302
- GCC_except_table1231
- GCC_except_table12314
- GCC_except_table12320
- GCC_except_table12325
- GCC_except_table12330
- GCC_except_table12335
- GCC_except_table12339
- GCC_except_table12343
- GCC_except_table12353
- GCC_except_table12363
- GCC_except_table12368
- GCC_except_table12373
- GCC_except_table12377
- GCC_except_table12382
- GCC_except_table12387
- GCC_except_table12393
- GCC_except_table12406
- GCC_except_table12421
- GCC_except_table12450
- GCC_except_table12466
- GCC_except_table1249
- GCC_except_table1250
- GCC_except_table12518
- GCC_except_table12523
- GCC_except_table12526
- GCC_except_table12529
- GCC_except_table12533
- GCC_except_table12535
- GCC_except_table12537
- GCC_except_table12539
- GCC_except_table12541
- GCC_except_table12543
- GCC_except_table12545
- GCC_except_table12548
- GCC_except_table12550
- GCC_except_table12559
- GCC_except_table12568
- GCC_except_table12571
- GCC_except_table12575
- GCC_except_table1258
- GCC_except_table12580
- GCC_except_table12586
- GCC_except_table12604
- GCC_except_table12606
- GCC_except_table12608
- GCC_except_table12626
- GCC_except_table12628
- GCC_except_table12630
- GCC_except_table12637
- GCC_except_table12641
- GCC_except_table12643
- GCC_except_table12646
- GCC_except_table12649
- GCC_except_table12651
- GCC_except_table12653
- GCC_except_table12655
- GCC_except_table12657
- GCC_except_table12660
- GCC_except_table12662
- GCC_except_table12664
- GCC_except_table12666
- GCC_except_table12669
- GCC_except_table12680
- GCC_except_table12686
- GCC_except_table12712
- GCC_except_table12716
- GCC_except_table12725
- GCC_except_table12753
- GCC_except_table12782
- GCC_except_table1280
- GCC_except_table12868
- GCC_except_table1298
- GCC_except_table12983
- GCC_except_table12985
- GCC_except_table12989
- GCC_except_table13003
- GCC_except_table13007
- GCC_except_table13014
- GCC_except_table13020
- GCC_except_table13031
- GCC_except_table13036
- GCC_except_table13115
- GCC_except_table13131
- GCC_except_table13136
- GCC_except_table13140
- GCC_except_table13157
- GCC_except_table13159
- GCC_except_table13166
- GCC_except_table13168
- GCC_except_table13170
- GCC_except_table13175
- GCC_except_table13219
- GCC_except_table13228
- GCC_except_table13234
- GCC_except_table13236
- GCC_except_table13238
- GCC_except_table13248
- GCC_except_table13267
- GCC_except_table13329
- GCC_except_table1335
- GCC_except_table13442
- GCC_except_table13463
- GCC_except_table13470
- GCC_except_table13474
- GCC_except_table1351
- GCC_except_table13521
- GCC_except_table1358
- GCC_except_table13604
- GCC_except_table13612
- GCC_except_table13631
- GCC_except_table1365
- GCC_except_table13697
- GCC_except_table13722
- GCC_except_table13725
- GCC_except_table13729
- GCC_except_table13732
- GCC_except_table13734
- GCC_except_table13738
- GCC_except_table13741
- GCC_except_table13750
- GCC_except_table13799
- GCC_except_table13817
- GCC_except_table1382
- GCC_except_table13823
- GCC_except_table13845
- GCC_except_table13939
- GCC_except_table13994
- GCC_except_table14007
- GCC_except_table14011
- GCC_except_table14027
- GCC_except_table14059
- GCC_except_table14069
- GCC_except_table14071
- GCC_except_table14073
- GCC_except_table14092
- GCC_except_table14183
- GCC_except_table14188
- GCC_except_table14211
- GCC_except_table14224
- GCC_except_table14226
- GCC_except_table14228
- GCC_except_table1428
- GCC_except_table14334
- GCC_except_table14335
- GCC_except_table14339
- GCC_except_table14372
- GCC_except_table14393
- GCC_except_table14404
- GCC_except_table14405
- GCC_except_table14406
- GCC_except_table14407
- GCC_except_table14408
- GCC_except_table14409
- GCC_except_table14410
- GCC_except_table14411
- GCC_except_table14412
- GCC_except_table14413
- GCC_except_table14481
- GCC_except_table14487
- GCC_except_table14507
- GCC_except_table14512
- GCC_except_table14521
- GCC_except_table14555
- GCC_except_table14559
- GCC_except_table14563
- GCC_except_table14570
- GCC_except_table14574
- GCC_except_table14585
- GCC_except_table14621
- GCC_except_table14677
- GCC_except_table1468
- GCC_except_table14680
- GCC_except_table14685
- GCC_except_table14704
- GCC_except_table14752
- GCC_except_table14776
- GCC_except_table1479
- GCC_except_table14800
- GCC_except_table1489
- GCC_except_table14934
- GCC_except_table15015
- GCC_except_table15077
- GCC_except_table15094
- GCC_except_table15104
- GCC_except_table15105
- GCC_except_table15124
- GCC_except_table1519
- GCC_except_table15213
- GCC_except_table15220
- GCC_except_table15223
- GCC_except_table15226
- GCC_except_table15228
- GCC_except_table15235
- GCC_except_table1527
- GCC_except_table15413
- GCC_except_table1547
- GCC_except_table15492
- GCC_except_table1557
- GCC_except_table1562
- GCC_except_table15659
- GCC_except_table15660
- GCC_except_table15667
- GCC_except_table15669
- GCC_except_table15674
- GCC_except_table15684
- GCC_except_table15686
- GCC_except_table15712
- GCC_except_table15731
- GCC_except_table15742
- GCC_except_table15769
- GCC_except_table15813
- GCC_except_table15814
- GCC_except_table15888
- GCC_except_table15893
- GCC_except_table1603
- GCC_except_table16050
- GCC_except_table16080
- GCC_except_table16097
- GCC_except_table1610
- GCC_except_table16102
- GCC_except_table16105
- GCC_except_table16107
- GCC_except_table16112
- GCC_except_table16113
- GCC_except_table16118
- GCC_except_table16119
- GCC_except_table16121
- GCC_except_table16135
- GCC_except_table16137
- GCC_except_table16146
- GCC_except_table16148
- GCC_except_table16151
- GCC_except_table16154
- GCC_except_table16200
- GCC_except_table16215
- GCC_except_table16218
- GCC_except_table16239
- GCC_except_table16244
- GCC_except_table16249
- GCC_except_table16252
- GCC_except_table16254
- GCC_except_table16265
- GCC_except_table16368
- GCC_except_table16370
- GCC_except_table16393
- GCC_except_table16394
- GCC_except_table16401
- GCC_except_table16410
- GCC_except_table16419
- GCC_except_table16428
- GCC_except_table16441
- GCC_except_table16500
- GCC_except_table16502
- GCC_except_table1657
- GCC_except_table16593
- GCC_except_table16654
- GCC_except_table16669
- GCC_except_table1668
- GCC_except_table16777
- GCC_except_table1679
- GCC_except_table16798
- GCC_except_table16804
- GCC_except_table16809
- GCC_except_table16817
- GCC_except_table16846
- GCC_except_table16858
- GCC_except_table16902
- GCC_except_table16965
- GCC_except_table16970
- GCC_except_table16978
- GCC_except_table16988
- GCC_except_table17000
- GCC_except_table17014
- GCC_except_table17020
- GCC_except_table17030
- GCC_except_table17043
- GCC_except_table17053
- GCC_except_table17063
- GCC_except_table17093
- GCC_except_table17097
- GCC_except_table17099
- GCC_except_table17101
- GCC_except_table17165
- GCC_except_table17214
- GCC_except_table17225
- GCC_except_table17245
- GCC_except_table17252
- GCC_except_table17256
- GCC_except_table17318
- GCC_except_table17328
- GCC_except_table17340
- GCC_except_table17341
- GCC_except_table17348
- GCC_except_table17357
- GCC_except_table17359
- GCC_except_table17361
- GCC_except_table17393
- GCC_except_table17399
- GCC_except_table17483
- GCC_except_table17519
- GCC_except_table17532
- GCC_except_table17584
- GCC_except_table17602
- GCC_except_table17642
- GCC_except_table17647
- GCC_except_table17686
- GCC_except_table17698
- GCC_except_table17701
- GCC_except_table17713
- GCC_except_table17738
- GCC_except_table17771
- GCC_except_table17772
- GCC_except_table17773
- GCC_except_table17808
- GCC_except_table17821
- GCC_except_table17862
- GCC_except_table17869
- GCC_except_table17873
- GCC_except_table17887
- GCC_except_table17903
- GCC_except_table17904
- GCC_except_table17931
- GCC_except_table17950
- GCC_except_table17988
- GCC_except_table18054
- GCC_except_table18079
- GCC_except_table18081
- GCC_except_table18083
- GCC_except_table18085
- GCC_except_table18087
- GCC_except_table18089
- GCC_except_table18093
- GCC_except_table18142
- GCC_except_table1824
- GCC_except_table18274
- GCC_except_table1830
- GCC_except_table18333
- GCC_except_table18344
- GCC_except_table18346
- GCC_except_table184
- GCC_except_table18400
- GCC_except_table18411
- GCC_except_table18425
- GCC_except_table18430
- GCC_except_table18434
- GCC_except_table18450
- GCC_except_table18451
- GCC_except_table18458
- GCC_except_table18463
- GCC_except_table18493
- GCC_except_table18522
- GCC_except_table18525
- GCC_except_table18543
- GCC_except_table18544
- GCC_except_table18593
- GCC_except_table18611
- GCC_except_table18636
- GCC_except_table18644
- GCC_except_table18646
- GCC_except_table18648
- GCC_except_table18652
- GCC_except_table18653
- GCC_except_table18664
- GCC_except_table18668
- GCC_except_table18669
- GCC_except_table18674
- GCC_except_table18676
- GCC_except_table18678
- GCC_except_table18680
- GCC_except_table18684
- GCC_except_table18740
- GCC_except_table18757
- GCC_except_table18784
- GCC_except_table18923
- GCC_except_table18925
- GCC_except_table18963
- GCC_except_table18968
- GCC_except_table18992
- GCC_except_table18994
- GCC_except_table18996
- GCC_except_table19000
- GCC_except_table19001
- GCC_except_table19002
- GCC_except_table19010
- GCC_except_table19015
- GCC_except_table19017
- GCC_except_table19019
- GCC_except_table19027
- GCC_except_table19032
- GCC_except_table19038
- GCC_except_table19049
- GCC_except_table19053
- GCC_except_table19055
- GCC_except_table19057
- GCC_except_table19065
- GCC_except_table19070
- GCC_except_table19077
- GCC_except_table19079
- GCC_except_table19081
- GCC_except_table19083
- GCC_except_table19085
- GCC_except_table19095
- GCC_except_table19099
- GCC_except_table19103
- GCC_except_table19105
- GCC_except_table19107
- GCC_except_table19111
- GCC_except_table19113
- GCC_except_table19115
- GCC_except_table19117
- GCC_except_table19121
- GCC_except_table19122
- GCC_except_table19123
- GCC_except_table19127
- GCC_except_table19128
- GCC_except_table19133
- GCC_except_table19135
- GCC_except_table19139
- GCC_except_table19144
- GCC_except_table19146
- GCC_except_table19148
- GCC_except_table19165
- GCC_except_table19167
- GCC_except_table19169
- GCC_except_table19184
- GCC_except_table19188
- GCC_except_table19192
- GCC_except_table19290
- GCC_except_table19296
- GCC_except_table19309
- GCC_except_table19313
- GCC_except_table19314
- GCC_except_table19325
- GCC_except_table19338
- GCC_except_table19340
- GCC_except_table19450
- GCC_except_table19462
- GCC_except_table19481
- GCC_except_table19556
- GCC_except_table19561
- GCC_except_table19566
- GCC_except_table19571
- GCC_except_table19579
- GCC_except_table19600
- GCC_except_table19606
- GCC_except_table19610
- GCC_except_table19612
- GCC_except_table19616
- GCC_except_table19626
- GCC_except_table19631
- GCC_except_table19633
- GCC_except_table19641
- GCC_except_table19642
- GCC_except_table19646
- GCC_except_table197
- GCC_except_table19714
- GCC_except_table19776
- GCC_except_table19793
- GCC_except_table19864
- GCC_except_table19878
- GCC_except_table19887
- GCC_except_table19889
- GCC_except_table19895
- GCC_except_table19911
- GCC_except_table2002
- GCC_except_table20051
- GCC_except_table20062
- GCC_except_table2008
- GCC_except_table20099
- GCC_except_table20105
- GCC_except_table20109
- GCC_except_table20140
- GCC_except_table20174
- GCC_except_table20183
- GCC_except_table20189
- GCC_except_table20192
- GCC_except_table20201
- GCC_except_table20212
- GCC_except_table20218
- GCC_except_table20229
- GCC_except_table20383
- GCC_except_table20387
- GCC_except_table20422
- GCC_except_table20426
- GCC_except_table20430
- GCC_except_table20460
- GCC_except_table20500
- GCC_except_table20504
- GCC_except_table20508
- GCC_except_table20512
- GCC_except_table20516
- GCC_except_table20520
- GCC_except_table20524
- GCC_except_table20528
- GCC_except_table20532
- GCC_except_table20536
- GCC_except_table20540
- GCC_except_table20544
- GCC_except_table20548
- GCC_except_table20552
- GCC_except_table20556
- GCC_except_table20560
- GCC_except_table20564
- GCC_except_table20568
- GCC_except_table20572
- GCC_except_table20576
- GCC_except_table20580
- GCC_except_table20617
- GCC_except_table20620
- GCC_except_table20625
- GCC_except_table20628
- GCC_except_table20656
- GCC_except_table20660
- GCC_except_table20661
- GCC_except_table20662
- GCC_except_table20668
- GCC_except_table20669
- GCC_except_table20681
- GCC_except_table20749
- GCC_except_table20793
- GCC_except_table20800
- GCC_except_table20806
- GCC_except_table20849
- GCC_except_table20853
- GCC_except_table20868
- GCC_except_table20896
- GCC_except_table20921
- GCC_except_table20924
- GCC_except_table20970
- GCC_except_table20987
- GCC_except_table21005
- GCC_except_table21011
- GCC_except_table21020
- GCC_except_table21025
- GCC_except_table21026
- GCC_except_table21032
- GCC_except_table21037
- GCC_except_table21038
- GCC_except_table21053
- GCC_except_table21054
- GCC_except_table21055
- GCC_except_table21056
- GCC_except_table21062
- GCC_except_table21067
- GCC_except_table21068
- GCC_except_table21071
- GCC_except_table21076
- GCC_except_table21083
- GCC_except_table21085
- GCC_except_table21089
- GCC_except_table21091
- GCC_except_table21106
- GCC_except_table21110
- GCC_except_table21121
- GCC_except_table21244
- GCC_except_table21251
- GCC_except_table21270
- GCC_except_table21288
- GCC_except_table21390
- GCC_except_table21464
- GCC_except_table21484
- GCC_except_table21494
- GCC_except_table21554
- GCC_except_table21670
- GCC_except_table21671
- GCC_except_table21703
- GCC_except_table21705
- GCC_except_table21712
- GCC_except_table21730
- GCC_except_table21740
- GCC_except_table21758
- GCC_except_table21806
- GCC_except_table21813
- GCC_except_table21829
- GCC_except_table21882
- GCC_except_table21898
- GCC_except_table21915
- GCC_except_table21920
- GCC_except_table21932
- GCC_except_table21934
- GCC_except_table21963
- GCC_except_table22019
- GCC_except_table22031
- GCC_except_table22033
- GCC_except_table22064
- GCC_except_table22076
- GCC_except_table22081
- GCC_except_table22088
- GCC_except_table221
- GCC_except_table22118
- GCC_except_table22134
- GCC_except_table22193
- GCC_except_table22282
- GCC_except_table22328
- GCC_except_table2233
- GCC_except_table22332
- GCC_except_table22334
- GCC_except_table22336
- GCC_except_table22363
- GCC_except_table22435
- GCC_except_table22436
- GCC_except_table22476
- GCC_except_table22516
- GCC_except_table2252
- GCC_except_table2257
- GCC_except_table22585
- GCC_except_table2265
- GCC_except_table2268
- GCC_except_table2293
- GCC_except_table2298
- GCC_except_table22990
- GCC_except_table2316
- GCC_except_table2318
- GCC_except_table23289
- GCC_except_table23301
- GCC_except_table23309
- GCC_except_table23356
- GCC_except_table23360
- GCC_except_table23416
- GCC_except_table23428
- GCC_except_table23444
- GCC_except_table2353
- GCC_except_table23545
- GCC_except_table23554
- GCC_except_table23584
- GCC_except_table23646
- GCC_except_table23660
- GCC_except_table2369
- GCC_except_table23728
- GCC_except_table23746
- GCC_except_table23753
- GCC_except_table23777
- GCC_except_table23952
- GCC_except_table23966
- GCC_except_table23970
- GCC_except_table24015
- GCC_except_table24049
- GCC_except_table24081
- GCC_except_table24126
- GCC_except_table24127
- GCC_except_table24193
- GCC_except_table24196
- GCC_except_table24211
- GCC_except_table24225
- GCC_except_table24234
- GCC_except_table24240
- GCC_except_table24247
- GCC_except_table24263
- GCC_except_table24270
- GCC_except_table24297
- GCC_except_table24486
- GCC_except_table24490
- GCC_except_table24497
- GCC_except_table24498
- GCC_except_table24499
- GCC_except_table245
- GCC_except_table2450
- GCC_except_table24500
- GCC_except_table24503
- GCC_except_table24504
- GCC_except_table24507
- GCC_except_table24508
- GCC_except_table24515
- GCC_except_table24521
- GCC_except_table24522
- GCC_except_table24525
- GCC_except_table24557
- GCC_except_table24560
- GCC_except_table24583
- GCC_except_table24586
- GCC_except_table24587
- GCC_except_table24592
- GCC_except_table24597
- GCC_except_table24601
- GCC_except_table24664
- GCC_except_table24671
- GCC_except_table24673
- GCC_except_table24675
- GCC_except_table24677
- GCC_except_table24679
- GCC_except_table24687
- GCC_except_table24689
- GCC_except_table24703
- GCC_except_table24729
- GCC_except_table24732
- GCC_except_table24739
- GCC_except_table24741
- GCC_except_table24743
- GCC_except_table24745
- GCC_except_table24753
- GCC_except_table24772
- GCC_except_table24776
- GCC_except_table24780
- GCC_except_table24790
- GCC_except_table24795
- GCC_except_table24799
- GCC_except_table24801
- GCC_except_table24803
- GCC_except_table24805
- GCC_except_table24813
- GCC_except_table24817
- GCC_except_table24827
- GCC_except_table24839
- GCC_except_table24863
- GCC_except_table24879
- GCC_except_table24897
- GCC_except_table24898
- GCC_except_table24901
- GCC_except_table24926
- GCC_except_table24928
- GCC_except_table24930
- GCC_except_table24953
- GCC_except_table24956
- GCC_except_table24959
- GCC_except_table24961
- GCC_except_table2500
- GCC_except_table25015
- GCC_except_table25073
- GCC_except_table25077
- GCC_except_table25080
- GCC_except_table25083
- GCC_except_table25090
- GCC_except_table25116
- GCC_except_table25119
- GCC_except_table25130
- GCC_except_table25134
- GCC_except_table25147
- GCC_except_table25153
- GCC_except_table25157
- GCC_except_table25160
- GCC_except_table25190
- GCC_except_table25193
- GCC_except_table25196
- GCC_except_table2520
- GCC_except_table25203
- GCC_except_table25212
- GCC_except_table25213
- GCC_except_table25220
- GCC_except_table2530
- GCC_except_table25310
- GCC_except_table25311
- GCC_except_table25312
- GCC_except_table25313
- GCC_except_table25317
- GCC_except_table25321
- GCC_except_table25322
- GCC_except_table25323
- GCC_except_table25326
- GCC_except_table25356
- GCC_except_table25364
- GCC_except_table25368
- GCC_except_table25396
- GCC_except_table25411
- GCC_except_table25445
- GCC_except_table25449
- GCC_except_table25457
- GCC_except_table25493
- GCC_except_table25528
- GCC_except_table25534
- GCC_except_table25603
- GCC_except_table25621
- GCC_except_table25630
- GCC_except_table25633
- GCC_except_table25636
- GCC_except_table25639
- GCC_except_table25648
- GCC_except_table25651
- GCC_except_table25666
- GCC_except_table25720
- GCC_except_table25798
- GCC_except_table25807
- GCC_except_table25901
- GCC_except_table25904
- GCC_except_table25907
- GCC_except_table25945
- GCC_except_table25951
- GCC_except_table2599
- GCC_except_table25999
- GCC_except_table26032
- GCC_except_table26037
- GCC_except_table26039
- GCC_except_table26041
- GCC_except_table2606
- GCC_except_table26087
- GCC_except_table26133
- GCC_except_table26141
- GCC_except_table26146
- GCC_except_table26178
- GCC_except_table26185
- GCC_except_table26187
- GCC_except_table26188
- GCC_except_table26318
- GCC_except_table26324
- GCC_except_table26345
- GCC_except_table26384
- GCC_except_table26387
- GCC_except_table26393
- GCC_except_table26398
- GCC_except_table26402
- GCC_except_table26410
- GCC_except_table26443
- GCC_except_table26445
- GCC_except_table26486
- GCC_except_table26630
- GCC_except_table26634
- GCC_except_table26637
- GCC_except_table26639
- GCC_except_table26751
- GCC_except_table26946
- GCC_except_table26953
- GCC_except_table26957
- GCC_except_table26968
- GCC_except_table26976
- GCC_except_table26978
- GCC_except_table26983
- GCC_except_table26985
- GCC_except_table26999
- GCC_except_table27004
- GCC_except_table27008
- GCC_except_table2759
- GCC_except_table2761
- GCC_except_table2773
- GCC_except_table2777
- GCC_except_table2802
- GCC_except_table2805
- GCC_except_table2845
- GCC_except_table2854
- GCC_except_table2857
- GCC_except_table2864
- GCC_except_table2873
- GCC_except_table2917
- GCC_except_table2918
- GCC_except_table2980
- GCC_except_table3020
- GCC_except_table310
- GCC_except_table3129
- GCC_except_table3138
- GCC_except_table3159
- GCC_except_table318
- GCC_except_table3354
- GCC_except_table3360
- GCC_except_table3453
- GCC_except_table3455
- GCC_except_table3463
- GCC_except_table3481
- GCC_except_table3492
- GCC_except_table3508
- GCC_except_table3537
- GCC_except_table3552
- GCC_except_table3557
- GCC_except_table3562
- GCC_except_table3570
- GCC_except_table3574
- GCC_except_table3580
- GCC_except_table3584
- GCC_except_table3624
- GCC_except_table365
- GCC_except_table3883
- GCC_except_table3887
- GCC_except_table3893
- GCC_except_table3896
- GCC_except_table3899
- GCC_except_table3909
- GCC_except_table3967
- GCC_except_table4005
- GCC_except_table4008
- GCC_except_table4016
- GCC_except_table4043
- GCC_except_table4054
- GCC_except_table4083
- GCC_except_table4145
- GCC_except_table4150
- GCC_except_table4161
- GCC_except_table4166
- GCC_except_table4169
- GCC_except_table4193
- GCC_except_table4195
- GCC_except_table4204
- GCC_except_table4205
- GCC_except_table4207
- GCC_except_table4225
- GCC_except_table4228
- GCC_except_table4234
- GCC_except_table4256
- GCC_except_table4259
- GCC_except_table4285
- GCC_except_table4289
- GCC_except_table4293
- GCC_except_table4297
- GCC_except_table4320
- GCC_except_table4471
- GCC_except_table4480
- GCC_except_table4488
- GCC_except_table4490
- GCC_except_table4496
- GCC_except_table4498
- GCC_except_table451
- GCC_except_table4514
- GCC_except_table4516
- GCC_except_table4531
- GCC_except_table4537
- GCC_except_table454
- GCC_except_table4558
- GCC_except_table457
- GCC_except_table4591
- GCC_except_table460
- GCC_except_table463
- GCC_except_table4641
- GCC_except_table4645
- GCC_except_table469
- GCC_except_table4824
- GCC_except_table4831
- GCC_except_table4888
- GCC_except_table4910
- GCC_except_table4914
- GCC_except_table4943
- GCC_except_table501
- GCC_except_table5037
- GCC_except_table5042
- GCC_except_table5076
- GCC_except_table5148
- GCC_except_table5251
- GCC_except_table5289
- GCC_except_table5297
- GCC_except_table5299
- GCC_except_table5302
- GCC_except_table5520
- GCC_except_table5535
- GCC_except_table5561
- GCC_except_table5638
- GCC_except_table5639
- GCC_except_table565
- GCC_except_table5714
- GCC_except_table5733
- GCC_except_table5741
- GCC_except_table5745
- GCC_except_table5754
- GCC_except_table5757
- GCC_except_table581
- GCC_except_table5817
- GCC_except_table5822
- GCC_except_table5832
- GCC_except_table5842
- GCC_except_table5870
- GCC_except_table5873
- GCC_except_table5891
- GCC_except_table5899
- GCC_except_table5901
- GCC_except_table5930
- GCC_except_table5931
- GCC_except_table5934
- GCC_except_table5935
- GCC_except_table5943
- GCC_except_table5956
- GCC_except_table6049
- GCC_except_table6051
- GCC_except_table6074
- GCC_except_table6112
- GCC_except_table6116
- GCC_except_table612
- GCC_except_table6120
- GCC_except_table6141
- GCC_except_table6146
- GCC_except_table6151
- GCC_except_table6153
- GCC_except_table6155
- GCC_except_table6176
- GCC_except_table6178
- GCC_except_table6182
- GCC_except_table6184
- GCC_except_table619
- GCC_except_table6243
- GCC_except_table6270
- GCC_except_table6275
- GCC_except_table6279
- GCC_except_table6283
- GCC_except_table6288
- GCC_except_table6293
- GCC_except_table6297
- GCC_except_table6301
- GCC_except_table6305
- GCC_except_table6316
- GCC_except_table6319
- GCC_except_table6327
- GCC_except_table6328
- GCC_except_table6329
- GCC_except_table6330
- GCC_except_table6331
- GCC_except_table6332
- GCC_except_table6333
- GCC_except_table6338
- GCC_except_table6340
- GCC_except_table6341
- GCC_except_table6343
- GCC_except_table6344
- GCC_except_table6346
- GCC_except_table6355
- GCC_except_table6356
- GCC_except_table636
- GCC_except_table6365
- GCC_except_table6367
- GCC_except_table6372
- GCC_except_table6382
- GCC_except_table6383
- GCC_except_table6384
- GCC_except_table6386
- GCC_except_table6390
- GCC_except_table6394
- GCC_except_table6408
- GCC_except_table6438
- GCC_except_table6517
- GCC_except_table6583
- GCC_except_table6700
- GCC_except_table6767
- GCC_except_table6980
- GCC_except_table7039
- GCC_except_table7085
- GCC_except_table7092
- GCC_except_table7103
- GCC_except_table7109
- GCC_except_table7116
- GCC_except_table7123
- GCC_except_table7127
- GCC_except_table7133
- GCC_except_table7142
- GCC_except_table7150
- GCC_except_table7156
- GCC_except_table7159
- GCC_except_table7161
- GCC_except_table7167
- GCC_except_table7173
- GCC_except_table718
- GCC_except_table7186
- GCC_except_table7190
- GCC_except_table7204
- GCC_except_table7214
- GCC_except_table7221
- GCC_except_table7223
- GCC_except_table7243
- GCC_except_table7245
- GCC_except_table725
- GCC_except_table7257
- GCC_except_table7275
- GCC_except_table7280
- GCC_except_table7283
- GCC_except_table7291
- GCC_except_table7293
- GCC_except_table7297
- GCC_except_table7302
- GCC_except_table7307
- GCC_except_table7364
- GCC_except_table7382
- GCC_except_table7383
- GCC_except_table7389
- GCC_except_table7390
- GCC_except_table7392
- GCC_except_table7393
- GCC_except_table7397
- GCC_except_table7398
- GCC_except_table740
- GCC_except_table7400
- GCC_except_table7409
- GCC_except_table7415
- GCC_except_table7417
- GCC_except_table742
- GCC_except_table7420
- GCC_except_table7422
- GCC_except_table7425
- GCC_except_table7433
- GCC_except_table7437
- GCC_except_table7442
- GCC_except_table7444
- GCC_except_table7448
- GCC_except_table7452
- GCC_except_table7461
- GCC_except_table7471
- GCC_except_table7475
- GCC_except_table7477
- GCC_except_table748
- GCC_except_table7502
- GCC_except_table7506
- GCC_except_table7510
- GCC_except_table7538
- GCC_except_table7542
- GCC_except_table7568
- GCC_except_table7570
- GCC_except_table7585
- GCC_except_table759
- GCC_except_table765
- GCC_except_table779
- GCC_except_table7818
- GCC_except_table7824
- GCC_except_table7837
- GCC_except_table7838
- GCC_except_table784
- GCC_except_table7851
- GCC_except_table7873
- GCC_except_table7874
- GCC_except_table7885
- GCC_except_table789
- GCC_except_table7914
- GCC_except_table7932
- GCC_except_table7934
- GCC_except_table7940
- GCC_except_table7944
- GCC_except_table7950
- GCC_except_table7957
- GCC_except_table7960
- GCC_except_table8017
- GCC_except_table8021
- GCC_except_table8023
- GCC_except_table8034
- GCC_except_table8041
- GCC_except_table8096
- GCC_except_table8105
- GCC_except_table8119
- GCC_except_table8141
- GCC_except_table8147
- GCC_except_table815
- GCC_except_table8151
- GCC_except_table8170
- GCC_except_table8176
- GCC_except_table8218
- GCC_except_table8231
- GCC_except_table8236
- GCC_except_table8238
- GCC_except_table8243
- GCC_except_table8253
- GCC_except_table8261
- GCC_except_table8265
- GCC_except_table8268
- GCC_except_table8277
- GCC_except_table8310
- GCC_except_table8368
- GCC_except_table8369
- GCC_except_table8404
- GCC_except_table8409
- GCC_except_table8415
- GCC_except_table8427
- GCC_except_table8438
- GCC_except_table8451
- GCC_except_table8475
- GCC_except_table8505
- GCC_except_table854
- GCC_except_table8540
- GCC_except_table8543
- GCC_except_table8596
- GCC_except_table8604
- GCC_except_table8619
- GCC_except_table8621
- GCC_except_table865
- GCC_except_table869
- GCC_except_table8741
- GCC_except_table8786
- GCC_except_table8811
- GCC_except_table886
- GCC_except_table892
- GCC_except_table8987
- GCC_except_table8991
- GCC_except_table9004
- GCC_except_table9008
- GCC_except_table901
- GCC_except_table9064
- GCC_except_table9076
- GCC_except_table908
- GCC_except_table9082
- GCC_except_table9085
- GCC_except_table9090
- GCC_except_table9091
- GCC_except_table9116
- GCC_except_table913
- GCC_except_table9140
- GCC_except_table9144
- GCC_except_table9147
- GCC_except_table9154
- GCC_except_table9158
- GCC_except_table920
- GCC_except_table9204
- GCC_except_table924
- GCC_except_table929
- GCC_except_table9327
- GCC_except_table934
- GCC_except_table9361
- GCC_except_table9365
- GCC_except_table9371
- GCC_except_table9373
- GCC_except_table9379
- GCC_except_table9382
- GCC_except_table9419
- GCC_except_table9465
- GCC_except_table952
- GCC_except_table9686
- GCC_except_table9687
- GCC_except_table9688
- GCC_except_table9705
- GCC_except_table9710
- GCC_except_table9723
- GCC_except_table9758
- GCC_except_table9769
- GCC_except_table9825
- GCC_except_table983
- GCC_except_table9908
- GCC_except_table9909
- GCC_except_table991
- GCC_except_table9940
- GCC_except_table9941
- GCC_except_table9943
- GCC_except_table9946
- GCC_except_table9948
- GCC_except_table9949
- GCC_except_table9951
- GCC_except_table9953
- GCC_except_table9954
- OBJC_IVAR_$_PLSearchIndexingEngine._queue_psiDatabase
- PLSearchEnablePSIForSyndicationLibrary.enablePSIForSyndicationLibrary
- PLSearchEnablePSIForSyndicationLibrary.onceToken
- _OBJC_CLASS_$_PSIAlbumTranslator
- _OBJC_CLASS_$_PSIAssetTranslator
- _OBJC_CLASS_$_PSICollectionShareTranslator
- _OBJC_CLASS_$_PSIMemoryTranslator
- _OBJC_CLASS_$_PSISearchEntityTranslator
- _OBJC_METACLASS_$_PSIAlbumTranslator
- _OBJC_METACLASS_$_PSIAssetTranslator
- _OBJC_METACLASS_$_PSICollectionShareTranslator
- _OBJC_METACLASS_$_PSIMemoryTranslator
- _OBJC_METACLASS_$_PSISearchEntityTranslator
- _PLContainingBundleRecord
- _PLSearchEnablePSIForSyndicationLibrary
- _PLURLForResourceProperties
- __169-[PLSearchIndexingEngine _inq_donatePSIObjectsByType:spotlightItemsByBundleID:leoDonatableItems:leoLexemeScoreUpdates:deleteIdentifiers:spotlightClientState:completion:]_block_invoke
- __75-[PLModelMigrator _importFileSystemImportAssets:intoLibrary:type:progress:]_block_invoke
- __84+[PLInitialSuggestionsStorageManager deleteInitialSuggestionsForPhotoLibrary:error:]_block_invoke
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
- ___block_descriptor_112_e8_32s40s48s56r64r72r80r88r96r_e5_v8?0l
- ___block_descriptor_128_e8_32s40s48s56s64bs72r80n11_8_8_s0_t8w8_e5_v8?0l
- ___block_descriptor_177_e8_32s40s48s56s64s72s80s88s96s104s112s120s128bs136r144n11_8_8_s0_t8w8_e5_v8?0l
- ___block_descriptor_32_e21_v16?0"PSIDatabase"8l
- ___block_descriptor_40_e8_32bs_e17_v16?0"NSArray"8l
- ___block_descriptor_40_e8_32s_e21_v16?0"PSIDatabase"8l
- ___block_descriptor_40_e8_32s_e57_v32?0"<PLSearchDetectionTrait>"8"NSString"16"NSSet"24l
- ___block_descriptor_48_e8_32s40s_e21_v16?0"PSIDatabase"8l
- ___block_descriptor_56_e8_32s40s48s_e24_v16?0"PLManagedAsset"8l
- ___block_descriptor_56_e8_32s40s48s_e28_v24?0"NSString"8"NSSet"16l
- ___block_descriptor_56_e8_32s40s48s_e44_v24?0"PLSearchEntityRelationToPerson"8^B16l
- ___block_descriptor_64_e8_32s40s48s_e32_v16?0"NSManagedObjectContext"8l
- ___block_descriptor_73_e8_32s40s48s56s64s_e35_v16?0"PLFileSystemAssetImporter"8l
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128b136r144n11_8_8_s0_t8w8
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s136r144n4_8_s0
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
+ "-[PLCloudSharedAssetSaveJob _runDaemonSideWaitUntilFinished:]"
+ "-[PLCloudSharedCommentsJob _runDaemonSideWaitUntilFinished:]"
+ "-[PLCollectionShareSharedStreamBackend checkServerForChangesForCollectionShare:completionHandler:]"
+ "-[PLSyndicationDeleteEngine _processDeletesForBundleID:unprefixedIdentifiers:error:]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/Projects/PhotoLibraryServices/Sources/PLCollectionShareCPLBackend.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/Projects/PhotoLibraryServices/Sources/PLCompositionHelper.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/Projects/PhotoLibraryServices/Sources/PLComputeCacheManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/Projects/PhotoLibraryServices/Sources/PLDetectedFaceJournalEntryPayload.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/Projects/PhotoLibraryServices/Sources/PLDuplicateAlbum.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/Projects/PhotoLibraryServices/Sources/PLJournal.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/Projects/PhotoLibraryServices/Sources/PLJournalManagerCore.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/Projects/PhotoLibraryServices/Sources/PLNotificationManager.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.AnfnE8/Sources/Photos/Projects/PhotoLibraryServices/Sources/PLRebuildJournalManager.m"
+ "/System/Library/PrivateFrameworks/IMDPersistence.framework/Contents/MacOS/IMDPersistence"
+ ";@0"
+ "CSSearchableItems: %tu, DeleteIdentifiers: %tu"
+ "Class getIMContactStoreClass(void)_block_invoke"
+ "Class getIMDDatabaseClass(void)_block_invoke"
+ "Deleted %tu asset(s) using %tu unprefixed identifiers"
+ "Error getting bundle %@ LSM %@ from bundle controller for URL %@"
+ "Error getting bundle or LSM"
+ "Error instantiating existing app library identifier for URL %@ - %@"
+ "Error instantiating existing library identifier for URL %@ - %@"
+ "Error obtaining path for restricted derivatives directory: %@"
+ "Error removing restricted derivatives directory: %@"
+ "Failed to direct upload full resources for proxy assets: %@"
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
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/Projects/PhotoLibraryServices/Sources/PLCollectionShareCPLBackend.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/Projects/PhotoLibraryServices/Sources/PLCompositionHelper.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/Projects/PhotoLibraryServices/Sources/PLComputeCacheManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/Projects/PhotoLibraryServices/Sources/PLDetectedFaceJournalEntryPayload.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/Projects/PhotoLibraryServices/Sources/PLDuplicateAlbum.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/Projects/PhotoLibraryServices/Sources/PLJournal.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/Projects/PhotoLibraryServices/Sources/PLJournalManagerCore.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/Projects/PhotoLibraryServices/Sources/PLNotificationManager.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.c1NpFB/Sources/Photos/Projects/PhotoLibraryServices/Sources/PLRebuildJournalManager.m"
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
