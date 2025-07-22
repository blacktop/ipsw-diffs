## MediaAnalysis

> `/System/Library/PrivateFrameworks/MediaAnalysis.framework/MediaAnalysis`

```diff

-345.67.3.0.0
-  __TEXT.__text: 0x458b8c
+345.71.2.11.1
+  __TEXT.__text: 0x45e89c
   __TEXT.__auth_stubs: 0x3f90
-  __TEXT.__objc_methlist: 0x1cd10
+  __TEXT.__objc_methlist: 0x1cd88
   __TEXT.__const: 0x14b28
-  __TEXT.__gcc_except_tab: 0x592a8
-  __TEXT.__cstring: 0x20518
-  __TEXT.__oslogstring: 0x28ccb
+  __TEXT.__gcc_except_tab: 0x59dd0
+  __TEXT.__cstring: 0x21120
+  __TEXT.__oslogstring: 0x2938b
   __TEXT.__dlopen_cstrs: 0x4b8
   __TEXT.__ustring: 0x40
-  __TEXT.__swift5_typeref: 0x3a8
+  __TEXT.__swift5_typeref: 0x3b8
   __TEXT.__swift5_reflstr: 0xf1
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__constg_swiftt: 0x2a0

   __TEXT.__swift5_fieldmd: 0x100
   __TEXT.__swift5_proto: 0x2c
   __TEXT.__swift5_types: 0x28
-  __TEXT.__swift5_capture: 0xd8
+  __TEXT.__swift5_capture: 0xe0
   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x30
-  __TEXT.__unwind_info: 0x11270
+  __TEXT.__unwind_info: 0x11370
   __TEXT.__eh_frame: 0x940
   __TEXT.__objc_classname: 0x4366
-  __TEXT.__objc_methname: 0x3ca14
-  __TEXT.__objc_methtype: 0xcd83
-  __TEXT.__objc_stubs: 0x29280
-  __DATA_CONST.__got: 0x1cb8
-  __DATA_CONST.__const: 0x6660
+  __TEXT.__objc_methname: 0x3cc48
+  __TEXT.__objc_methtype: 0xcde3
+  __TEXT.__objc_stubs: 0x29300
+  __DATA_CONST.__got: 0x1cc8
+  __DATA_CONST.__const: 0x6810
   __DATA_CONST.__objc_classlist: 0x1278
   __DATA_CONST.__objc_catlist: 0x1b8
   __DATA_CONST.__objc_protolist: 0x138
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc928
+  __DATA_CONST.__objc_selrefs: 0xc970
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0xec8
-  __DATA_CONST.__objc_arraydata: 0x11f0
+  __DATA_CONST.__objc_arraydata: 0x11e0
   __AUTH_CONST.__auth_got: 0x1fe0
   __AUTH_CONST.__const: 0x5aa8
-  __AUTH_CONST.__cfstring: 0x177c0
-  __AUTH_CONST.__objc_const: 0x38200
+  __AUTH_CONST.__cfstring: 0x17b20
+  __AUTH_CONST.__objc_const: 0x38238
   __AUTH_CONST.__objc_floatobj: 0x290
   __AUTH_CONST.__objc_doubleobj: 0x460
   __AUTH_CONST.__objc_intobj: 0x2ec8
-  __AUTH_CONST.__objc_arrayobj: 0xc30
+  __AUTH_CONST.__objc_arrayobj: 0xc18
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH.__objc_data: 0x1da0
   __AUTH.__data: 0x1d8
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x9d0
-  __DATA.__objc_ivar: 0x3270
+  __DATA.__objc_ivar: 0x3274
   __DATA.__data: 0x1b88
-  __DATA.__bss: 0xea9
+  __DATA.__bss: 0xe99
   __DATA.__common: 0x3c1
   __DATA_DIRTY.__objc_data: 0x9d40
   __DATA_DIRTY.__data: 0x160

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CB1DE6EF-A06F-3E17-9574-5E7DA3FBF346
-  Functions: 16719
-  Symbols:   56657
-  CStrings:  21837
+  UUID: DDB2D20D-3E17-36CB-A0E3-32ABF0723160
+  Functions: 16743
+  Symbols:   56748
+  CStrings:  21966
 
Symbols:
+ +[VCPAnalysisProgressQuery queryVideoCountAndDurationBreakdown:photoLibrary:taskID:cancelOrExtendTimeoutBlock:]
+ -[MADChangeRequest error]
+ -[MADChangeRequest(ProcessingStatus) _hardFailAllRunningProcessingStatusForTaskID:additionalPredicates:]
+ -[MADChangeRequest(ProcessingStatus) _hardFailAllRunningProcessingStatusForTaskID:additionalPredicates:].cold.1
+ -[MADChangeRequest(ProcessingStatus) _hardFailAllRunningProcessingStatusWithPredicate:]
+ -[MADChangeRequest(ProcessingStatus) _hardFailAllRunningProcessingStatusWithPredicate:].cold.1
+ -[MADChangeRequest(ProcessingStatus) _setAttempts:asset:taskID:status:lastAttemptDate:mediaType:mediaSubtypes:errorCode:errorLine:]
+ -[MADChangeRequest(ProcessingStatus) _updateProcessingStatus:nextAttemptDate:errorCode:errorLine:localIdentifier:taskID:]
+ -[MADPhotosDataStoreBatchIterator performBlockAndWait:]
+ -[MADPhotosDataStoreClient _releaseSharedDataStoreForPhotoLibrary:]
+ -[MADPhotosDataStoreClient releaseSharedDataStoreForPhotoLibrary:]
+ -[NSManagedObjectContext(MediaAnalysis) mad_hasChanges]
+ -[NSManagedObjectContext(MediaAnalysis) mad_insertBatch:entityName:insertedCount:]
+ -[PHPhotoLibrary(MADataStore) mad_performAnalysisDataStoreChanges:error:]
+ -[PHPhotoLibrary(MediaAnalysis) mad_countOfUnprocessedAssetsForTaskID:cancelBlock:extendTimeoutBlock:error:]
+ _MADGenerationService_AlchemistClientOption
+ _OBJC_CLASS_$_NSBatchInsertRequest
+ _OBJC_IVAR_$_MADChangeRequest._error
+ _VCPAnalysisCountFullAnalysisLongVideoCountKey
+ _VCPAnalysisCountFullAnalysisLongVideoFailedKey
+ _VCPAnalysisCountFullAnalysisLongVideoGatedKey
+ _VCPAnalysisCountFullAnalysisLongVideoProcessedKey
+ _VCPAnalysisCountFullAnalysisSlowmoVideoCountKey
+ _VCPAnalysisCountFullAnalysisSlowmoVideoFailedKey
+ _VCPAnalysisCountFullAnalysisSlowmoVideoGatedKey
+ _VCPAnalysisCountFullAnalysisSlowmoVideoProcessedKey
+ _VCPAnalysisCountFullAnalysisVideoFailedKey
+ _VCPAnalysisCountFullAnalysisVideoGatedKey
+ _VCPAnalysisFullAnalysisFailedLongVideoDurationKey
+ _VCPAnalysisFullAnalysisFailedSlowmoVideoDurationKey
+ _VCPAnalysisFullAnalysisFailedVideoDurationKey
+ _VCPAnalysisFullAnalysisGatedLongVideoDurationKey
+ _VCPAnalysisFullAnalysisGatedSlowmoVideoDurationKey
+ _VCPAnalysisFullAnalysisGatedVideoDurationKey
+ _VCPAnalysisFullAnalysisLongVideoDurationKey
+ _VCPAnalysisFullAnalysisProcessedLongVideoDurationKey
+ _VCPAnalysisFullAnalysisProcessedSlowmoVideoDurationKey
+ _VCPAnalysisFullAnalysisProcessedVideoDurationKey
+ _VCPAnalysisFullAnalysisSlowmoVideoDurationKey
+ _VCPAnalysisFullAnalysisVideoDurationKey
+ __OBJC_$_PROP_LIST_MADChangeRequest
+ ___101-[VCPMediaAnalyzer findTimeRangesFor:inURLAsset:withOptions:andProgressHandler:andCompletionHandler:]_block_invoke.1029
+ ___105-[PHPhotoLibrary(MediaAnalysis) mad_performChangesAndWait:activity:cancelBlock:extendTimeoutBlock:error:]_block_invoke.669
+ ___105-[PHPhotoLibrary(MediaAnalysis) mad_performChangesAndWait:activity:cancelBlock:extendTimeoutBlock:error:]_block_invoke.670
+ ___108-[PHPhotoLibrary(MediaAnalysis) mad_countOfUnprocessedAssetsForTaskID:cancelBlock:extendTimeoutBlock:error:]_block_invoke
+ ___108-[PHPhotoLibrary(MediaAnalysis) mad_countOfUnprocessedAssetsForTaskID:cancelBlock:extendTimeoutBlock:error:]_block_invoke_2
+ ___112-[VCPMediaAnalyzer _analyzeOndemand:forAnalysisTypes:withExistingAnalysis:andOptions:storeAnalysis:cancelBlock:]_block_invoke.926
+ ___112-[VCPMediaAnalyzer _analyzeOndemand:forAnalysisTypes:withExistingAnalysis:andOptions:storeAnalysis:cancelBlock:]_block_invoke.927
+ ___118+[MADManagedBackgroundActivitySchedule _querySchedulingHistoryRecords:predicate:sortDescriptors:managedObjectContext:]_block_invoke
+ ___37+[MADSystemDataStore systemDataStore]_block_invoke.224
+ ___37+[MADSystemDataStore systemDataStore]_block_invoke.226
+ ___37+[MADSystemDataStore systemDataStore]_block_invoke.235
+ ___37+[MADSystemDataStore systemDataStore]_block_invoke.238
+ ___37+[MADSystemDataStore systemDataStore]_block_invoke_2
+ ___42-[VCPMobileAssetManager queryMobileAssets]_block_invoke.553
+ ___42-[VCPMobileAssetManager queryMobileAssets]_block_invoke.555
+ ___45-[MADPhotosDataStoreBatchIterator nextObject]_block_invoke_2
+ ___48-[VCPMobileAssetManager purgeAllInstalledAssets]_block_invoke.566
+ ___53-[MADPhotosDataStoreBatchIterator _retrieveNextBatch]_block_invoke_2
+ ___55-[NSManagedObjectContext(MediaAnalysis) mad_hasChanges]_block_invoke
+ ___56-[VCPMediaAnalyzer _setupMediaAnalysisServiceConnection]_block_invoke.896
+ ___56-[VCPMediaAnalyzer _setupMediaAnalysisServiceConnection]_block_invoke.897
+ ___57-[MADChangeRequest(Asset) assetWithPhotosAsset:analysis:]_block_invoke.216
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.695
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.695.cold.1
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.703
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.703.cold.1
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.707
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.707.cold.1
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.715
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.715.cold.1
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.715.cold.2
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.719
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.719.cold.1
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.719.cold.2
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.723
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.723.cold.1
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.723.cold.2
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.736
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.736.cold.1
+ ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.739.cold.2
+ ___60-[MADPhotosDataStoreClient setDatabaseVersion:photoLibrary:]_block_invoke.458
+ ___65-[VCPMobileAssetManager downloadMobileAssetIfNeeded:petWatchDog:]_block_invoke.558
+ ___65-[VCPMobileAssetManager downloadMobileAssetIfNeeded:petWatchDog:]_block_invoke.560
+ ___67-[MADPhotosDataStoreClient _releaseSharedDataStoreForPhotoLibrary:]_block_invoke
+ ___67-[MADPhotosDataStoreClient _releaseSharedDataStoreForPhotoLibrary:]_block_invoke_2
+ ___67-[VCPMediaAnalyzer _getDatabaseSandboxExtensionForPhotoLibraryURL:]_block_invoke.910
+ ___69-[VCPMediaAnalyzer analyzeOndemand:pairedURL:forAnalysisTypes:error:]_block_invoke.935
+ ___73-[PHPhotoLibrary(MADataStore) mad_performAnalysisDataStoreChanges:error:]_block_invoke
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.746
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.746.cold.1
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.746.cold.2
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.753
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.753.cold.1
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.753.cold.2
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.753.cold.3
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.753.cold.4
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.753.cold.5
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.753.cold.6
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.753.cold.7
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.753.cold.8
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.753.cold.9
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.766
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.766.cold.1
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.766.cold.2
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.771
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.771.cold.1
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.771.cold.2
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.776
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.776.cold.1
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.776.cold.2
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.781
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.781.cold.1
+ ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.781.cold.2
+ ___82-[NSManagedObjectContext(MediaAnalysis) mad_insertBatch:entityName:insertedCount:]_block_invoke
+ ___84-[VCPMediaAnalyzer _getSandboxExtensionForMediaAnalysisDatabaseWithPhotoLibraryURL:]_block_invoke.899
+ ___87+[MADManagedBackgroundActivitySchedule(Migration) migrateDataWithManagedObjectContext:]_block_invoke
+ ___96-[MADChangeRequest(PersistentHistory) prunePersistentHistoryWithCancelBlock:extendTimeoutBlock:]_block_invoke.cold.1
+ ___97+[MADManagedBackgroundActivitySchedule updateSessionLogWithTaskID:startTime:duration:exitStatus:]_block_invoke.418
+ ___Block_byref_object_copy_.693
+ ___Block_byref_object_dispose_.694
+ ___block_descriptor_40_e8_32s_e9_B16?0^8ls32l8
+ ___block_descriptor_48_e8_32s40s_e9_B16?0^8ls32l8s40l8
+ ___block_descriptor_48_ea8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_64_e8_32s40s48bs_e9_B16?0^8ls48l8s32l8s40l8
+ ___block_descriptor_64_ea8_32s40bs48r56r_e5_v8?0lr48l8s40l8r56l8s32l8
+ ___block_descriptor_64_ea8_32s40s48r56r_e9_B16?0^8ls32l8s40l8r48l8r56l8
+ ___block_descriptor_80_e8_32s40s48r56r64r_e9_B16?0^8ls32l8r48l8s40l8r56l8r64l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8r72l8
+ ___block_descriptor_84_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___block_descriptor_84_ea8_32s40s48s56r64r_e5_v8?0lr56l8s32l8s40l8r64l8s48l8
+ ___block_descriptor_84_ea8_32s40s48s56r64r_e5_v8?0ls32l8s40l8s48l8r56l8r64l8
+ ___block_literal_global.1003
+ ___block_literal_global.1020
+ ___block_literal_global.1034
+ ___block_literal_global.2610
+ ___block_literal_global.2712
+ ___block_literal_global.2719
+ ___block_literal_global.387
+ ___block_literal_global.496
+ ___block_literal_global.503
+ ___block_literal_global.551
+ ___block_literal_global.621
+ ___block_literal_global.626
+ ___block_literal_global.634
+ ___block_literal_global.639
+ ___block_literal_global.644
+ ___block_literal_global.652
+ ___block_literal_global.663
+ ___block_literal_global.696
+ ___block_literal_global.730
+ ___block_literal_global.761
+ ___block_literal_global.774
+ ___block_literal_global.934
+ ___block_literal_global.957
+ ___block_literal_global.975
+ ___block_literal_global.987
+ ___block_literal_global.992
+ _objc_msgSend$_hardFailAllRunningProcessingStatusForTaskID:additionalPredicates:
+ _objc_msgSend$_hardFailAllRunningProcessingStatusWithPredicate:
+ _objc_msgSend$_releaseSharedDataStoreForPhotoLibrary:
+ _objc_msgSend$_setAttempts:asset:taskID:status:lastAttemptDate:mediaType:mediaSubtypes:errorCode:errorLine:
+ _objc_msgSend$_updateProcessingStatus:nextAttemptDate:errorCode:errorLine:localIdentifier:taskID:
+ _objc_msgSend$convertAlchemist:focalLengthPX:preset:resolution:client:completion:
+ _objc_msgSend$countOfUnprocessedAssetsForMediaProcessingTaskID:priority:algorithmVersion:sceneConfidenceThreshold:error:
+ _objc_msgSend$initWithEntityName:objects:
+ _objc_msgSend$mad_hasChanges
+ _symbolic So8NSStringCSg
- +[PHMediaProcessingAlgorithmVersionProvider(MediaAnalysis) mad_sharedVersionProviderForBackupWithPhotoLibrary:]
- +[VCPAnalysisProgressQuery queryVideoTotalDuration:processedDuration:failedDuration:photoLibrary:taskID:cancelOrExtendTimeoutBlock:]
- -[MADChangeRequest(PersistentHistory) prunePersistentHistoryWithCancelBlock:extendTimeoutBlock:].cold.1
- -[MADChangeRequest(PersistentHistory) prunePersistentHistoryWithCancelBlock:extendTimeoutBlock:].cold.2
- -[MADChangeRequest(PersistentHistory) prunePersistentHistoryWithCancelBlock:extendTimeoutBlock:].cold.3
- -[MADChangeRequest(ProcessingStatus) hardFailAllRunningProcessingStatusWithPredicate:]
- -[MADChangeRequest(ProcessingStatus) hardFailAllRunningProcessingStatusWithPredicate:].cold.1
- -[MADChangeRequest(ProcessingStatus) setAttempts:asset:taskID:status:lastAttemptDate:mediaType:mediaSubtypes:errorCode:errorLine:].cold.1
- -[MADChangeRequest(ProcessingStatus) updateProcessingStatus:nextAttemptDate:errorCode:errorLine:localIdentifier:taskID:].cold.1
- -[PHPhotoLibrary(MADataStore) mad_performAnalysisDataStoreChanges:]
- __ZZ111+[PHMediaProcessingAlgorithmVersionProvider(MediaAnalysis) mad_sharedVersionProviderForBackupWithPhotoLibrary:]E4once
- __ZZ111+[PHMediaProcessingAlgorithmVersionProvider(MediaAnalysis) mad_sharedVersionProviderForBackupWithPhotoLibrary:]E8instance
- ___101-[VCPMediaAnalyzer findTimeRangesFor:inURLAsset:withOptions:andProgressHandler:andCompletionHandler:]_block_invoke.1032
- ___105-[PHPhotoLibrary(MediaAnalysis) mad_performChangesAndWait:activity:cancelBlock:extendTimeoutBlock:error:]_block_invoke.672
- ___105-[PHPhotoLibrary(MediaAnalysis) mad_performChangesAndWait:activity:cancelBlock:extendTimeoutBlock:error:]_block_invoke.673
- ___111+[PHMediaProcessingAlgorithmVersionProvider(MediaAnalysis) mad_sharedVersionProviderForBackupWithPhotoLibrary:]_block_invoke
- ___112-[VCPMediaAnalyzer _analyzeOndemand:forAnalysisTypes:withExistingAnalysis:andOptions:storeAnalysis:cancelBlock:]_block_invoke.929
- ___112-[VCPMediaAnalyzer _analyzeOndemand:forAnalysisTypes:withExistingAnalysis:andOptions:storeAnalysis:cancelBlock:]_block_invoke.930
- ___42-[VCPMobileAssetManager queryMobileAssets]_block_invoke.556
- ___42-[VCPMobileAssetManager queryMobileAssets]_block_invoke.558
- ___48-[VCPMobileAssetManager purgeAllInstalledAssets]_block_invoke.569
- ___56-[VCPMediaAnalyzer _setupMediaAnalysisServiceConnection]_block_invoke.899
- ___56-[VCPMediaAnalyzer _setupMediaAnalysisServiceConnection]_block_invoke.900
- ___57-[MADChangeRequest(Asset) assetWithPhotosAsset:analysis:]_block_invoke.210
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.701
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.701.cold.1
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.706
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.706.cold.1
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.710
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.710.cold.1
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.718
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.718.cold.1
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.718.cold.2
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.726
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.726.cold.1
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.726.cold.2
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.728
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.728.cold.1
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.728.cold.2
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.742
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.742.cold.1
- ___58-[VCPPhotoAnalyzer analyzeImage:performedAnalyses:cancel:]_block_invoke.742.cold.2
- ___65-[VCPMobileAssetManager downloadMobileAssetIfNeeded:petWatchDog:]_block_invoke.561
- ___65-[VCPMobileAssetManager downloadMobileAssetIfNeeded:petWatchDog:]_block_invoke.563
- ___67-[PHPhotoLibrary(MADataStore) mad_performAnalysisDataStoreChanges:]_block_invoke
- ___67-[VCPMediaAnalyzer _getDatabaseSandboxExtensionForPhotoLibraryURL:]_block_invoke.913
- ___69-[VCPMediaAnalyzer analyzeOndemand:pairedURL:forAnalysisTypes:error:]_block_invoke.938
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.749
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.749.cold.1
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.749.cold.2
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.756
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.756.cold.1
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.756.cold.2
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.756.cold.3
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.756.cold.4
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.756.cold.5
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.756.cold.6
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.756.cold.7
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.756.cold.8
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.756.cold.9
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.769
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.769.cold.1
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.769.cold.2
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.774
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.774.cold.1
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.774.cold.2
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.779
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.779.cold.1
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.779.cold.2
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.784
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.784.cold.1
- ___74-[VCPMovieAnalyzer analyzeVideoSegment:timerange:forAnalysisTypes:cancel:]_block_invoke.784.cold.2
- ___84-[VCPMediaAnalyzer _getSandboxExtensionForMediaAnalysisDatabaseWithPhotoLibraryURL:]_block_invoke.902
- ___Block_byref_object_copy_.696
- ___Block_byref_object_dispose_.697
- ___block_descriptor_40_e8_32s_e5_i8?0ls32l8
- ___block_descriptor_48_e8_32s40s_e5_i8?0ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e5_i8?0ls32l8r48l8s40l8
- ___block_descriptor_64_e8_32s40s48bs_e5_i8?0ls48l8s32l8s40l8
- ___block_descriptor_64_ea8_32s40bs48r56r_e5_v8?0lr48l8s40l8s32l8r56l8
- ___block_descriptor_76_ea8_32s40s48r56r_e5_v8?0ls32l8s40l8r48l8r56l8
- ___block_literal_global.1006
- ___block_literal_global.1023
- ___block_literal_global.2544
- ___block_literal_global.2646
- ___block_literal_global.2653
- ___block_literal_global.390
- ___block_literal_global.499
- ___block_literal_global.506
- ___block_literal_global.554
- ___block_literal_global.632
- ___block_literal_global.640
- ___block_literal_global.650
- ___block_literal_global.655
- ___block_literal_global.666
- ___block_literal_global.674
- ___block_literal_global.699
- ___block_literal_global.723
- ___block_literal_global.764
- ___block_literal_global.777
- ___block_literal_global.898
- ___block_literal_global.940
- ___block_literal_global.960
- ___block_literal_global.973
- ___block_literal_global.978
- ___block_literal_global.990
- ___block_literal_global.995
- _objc_msgSend$convertAlchemist:focalLengthPX:preset:resolution:completion:
- _objc_msgSend$hardFailAllRunningProcessingStatusForTaskID:additionalPredicates:
- _objc_msgSend$hardFailAllRunningProcessingStatusWithPredicate:
- _objc_msgSend$setAttempts:asset:taskID:status:lastAttemptDate:mediaType:mediaSubtypes:errorCode:errorLine:
- _objc_msgSend$updateProcessingStatus:nextAttemptDate:errorCode:errorLine:localIdentifier:taskID:
CStrings:
+ "AlchemistClient"
+ "B16@?0^@8"
+ "Failed to fetch or create managed processing status of asset %@ for task %@"
+ "Failed to hard fail all running processing status for task %@"
+ "Failed to hard fail all running processing status for task %@ with addtional predicates %@"
+ "Failed to prune persistent history before transaction"
+ "Failed to remove all moments scheduled assets"
+ "Failed to remove moments scheduled asset %@ for task %@"
+ "Failed to set attempts for asset %@ for task %@"
+ "FailedLongVideoDuration"
+ "FailedSlowmoVideoDuration"
+ "FailedVideoDuration"
+ "FullAnalysisLongVideoCount"
+ "FullAnalysisLongVideoFailed"
+ "FullAnalysisLongVideoGated"
+ "FullAnalysisLongVideoProcessed"
+ "FullAnalysisSlowmoVideoCount"
+ "FullAnalysisSlowmoVideoFailed"
+ "FullAnalysisSlowmoVideoGated"
+ "FullAnalysisSlowmoVideoProcessed"
+ "FullAnalysisVideoFailed"
+ "FullAnalysisVideoGated"
+ "GatedLongVideoDuration"
+ "GatedSlowmoVideoDuration"
+ "GatedVideoDuration"
+ "LongVideoDuration"
+ "ProcessedLongVideoDuration"
+ "ProcessedSlowmoVideoDuration"
+ "ProcessedVideoDuration"
+ "Q48@0:8Q16@?24@?32^@40"
+ "SlowmoVideoDuration"
+ "T@\"NSError\",R,N,V_error"
+ "Unable to fetch or create managed processing status with local identifier %@ for task %@"
+ "Unable to remove all processing status"
+ "Unable to remove all processing status for task %@"
+ "Unable to remove all processing status with media type %d and media subtypes %d for task %@"
+ "Unable to remove processing status with local identifier %@ for task %@"
+ "Unable to remove processing status with local identifiers %@ for task %@"
+ "Unable to update processing status of asset %@ for task %@"
+ "VisualEncoder"
+ "[%@] Releasing shared data store for library %@"
+ "[%@][mad_countOfUnprocessedAssetsForTaskID] Canceled while waiting"
+ "[%@][mad_countOfUnprocessedAssetsForTaskID] Failed to fetch assets count for taskID: %u, %@"
+ "[%@][mad_countOfUnprocessedAssetsForTaskID] Finished fetching %u unprocessed assets count for taskID: %u"
+ "[%@][mad_countOfUnprocessedAssetsForTaskID] Timeout while waiting"
+ "[%@][mad_countOfUnprocessedAssetsForTaskID] Waiting ..."
+ "[MACD] Error running block before saving changes: %@"
+ "[MACD] Error saving changes: %@"
+ "[MACD] Failed to execute batch insert request for entity %@ with error %@"
+ "[MACD] Failed to perform and save changes on photo library %@: %@"
+ "[MACD] Failed to perform changes block on photo library %@: %@"
+ "[MACD|Asset] Failed to remove assets with local identifiers: %@"
+ "[MACD|ChangeToken] Failed to remove all change tokens"
+ "[MACD|ChangeToken] Failed to remove all change tokens for task %@"
+ "[MACD|ChangeToken] Failed to remove change token with type %d for task %@"
+ "[MACD|ProgressHistory] Failed to remove all background analysis process history"
+ "[MADPhotosDataStoreBatchIterator] failed to remove query generation, error: %@"
+ "[MADPhotosDataStoreBatchIterator] fetch failed with error: %@"
+ "[PhotosDBPersistence] Failed with UNKNOWN Error"
+ "[ProgressQuery](Video duration) output progress dictionary must be non-nil"
+ "_error"
+ "_hardFailAllRunningProcessingStatusForTaskID:additionalPredicates:"
+ "_hardFailAllRunningProcessingStatusWithPredicate:"
+ "_releaseSharedDataStoreForPhotoLibrary:"
+ "_setAttempts:asset:taskID:status:lastAttemptDate:mediaType:mediaSubtypes:errorCode:errorLine:"
+ "_updateProcessingStatus:nextAttemptDate:errorCode:errorLine:localIdentifier:taskID:"
+ "com.apple.mediaanalysisd.UnprocessedAssetCountFetch"
+ "convertAlchemist:focalLengthPX:preset:resolution:client:completion:"
+ "countOfUnprocessedAssetsForMediaProcessingTaskID:priority:algorithmVersion:sceneConfidenceThreshold:error:"
+ "i40@0:8@16@24^Q32"
+ "i48@0:8@16@24Q32@?40"
+ "initWithEntityName:objects:"
+ "mad_countOfUnprocessedAssetsForTaskID:cancelBlock:extendTimeoutBlock:error:"
+ "mad_hasChanges"
+ "mad_insertBatch:entityName:insertedCount:"
+ "mad_performAnalysisDataStoreChanges:error:"
+ "mubb_md"
+ "queryVideoCountAndDurationBreakdown:photoLibrary:taskID:cancelOrExtendTimeoutBlock:"
+ "releaseSharedDataStoreForPhotoLibrary:"
+ "v32@0:8@?16@?24"
+ "v32@0:8q16@24"
+ "v40@0:8@16Q24@32"
+ "v40@0:8@16Q24Q32"
+ "v40@0:8Q16q24Q32"
+ "v48@0:8@16Q24Q32@40"
+ "v48@0:8Q16@24@32Q40"
+ "v56@0:8Q16@24Q32Q40@48"
+ "v60@0:8^{__CVBuffer=}16f24@28@36@44@?52"
+ "v64@0:8Q16@24Q32Q40@48Q56"
+ "v64@0:8Q16Q24Q32Q40Q48@56"
+ "v88@0:8Q16@24Q32Q40@48q56Q64Q72Q80"
- "[%@] Removed persistent store and moc for library %@"
- "[MACD] Error running block before saving changes"
- "[MACD] Error saving changes"
- "[MACD] Failed to perform and save changes on photo library %@"
- "[MACD] Failed to perform changes block on photo library %@"
- "[MADPhotosDataStoreBatchIterator] fetch failed with status: %d"
- "[ProgressQuery](Video duration) output parameter statistics must be non-nil"
- "[ProgressQuery](Video duration) skipping asset %@, ineligible for download"
- "convertAlchemist:focalLengthPX:preset:resolution:completion:"
- "hardFailAllRunningProcessingStatusWithPredicate:"
- "i28@0:8B16@20"
- "i32@0:8@16Q24"
- "i32@0:8@?16^@24"
- "i40@0:8@16Q24Q32"
- "i40@0:8Q16q24Q32"
- "i48@0:8@16Q24Q32@40"
- "i48@0:8Q16@24@32Q40"
- "i56@0:8Q16@24Q32Q40@48"
- "i64@0:8Q16Q24Q32Q40Q48@56"
- "i64@0:8^d16^d24^d32@40Q48@?56"
- "mad_performAnalysisDataStoreChanges:"
- "mad_sharedVersionProviderForBackupWithPhotoLibrary:"
- "mubb_md5"
- "queryVideoTotalDuration:processedDuration:failedDuration:photoLibrary:taskID:cancelOrExtendTimeoutBlock:"
- "v52@0:8^{__CVBuffer=}16f24@28@36@?44"

```
