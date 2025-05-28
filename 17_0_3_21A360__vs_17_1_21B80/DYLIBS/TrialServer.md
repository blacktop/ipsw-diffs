## TrialServer

> `/System/Library/PrivateFrameworks/TrialServer.framework/TrialServer`

```diff

-395.2.0.0.0
-  __TEXT.__text: 0x154454
+395.1.10.0.0
+  __TEXT.__text: 0x15448c
   __TEXT.__auth_stubs: 0xed0
-  __TEXT.__objc_methlist: 0xa2c8
+  __TEXT.__objc_methlist: 0xa320
   __TEXT.__const: 0xce8
-  __TEXT.__gcc_except_tab: 0x766c
-  __TEXT.__cstring: 0x14f32
-  __TEXT.__oslogstring: 0x1c892
+  __TEXT.__gcc_except_tab: 0x76e4
+  __TEXT.__cstring: 0x14f49
+  __TEXT.__oslogstring: 0x1ca27
   __TEXT.__dlopen_cstrs: 0x74
-  __TEXT.__unwind_info: 0x42a0
+  __TEXT.__unwind_info: 0x42ac
   __TEXT.__objc_classname: 0x23ac
-  __TEXT.__objc_methname: 0x1c445
-  __TEXT.__objc_methtype: 0x4f92
-  __TEXT.__objc_stubs: 0x13880
+  __TEXT.__objc_methname: 0x1c513
+  __TEXT.__objc_methtype: 0x4fc8
+  __TEXT.__objc_stubs: 0x13940
   __DATA_CONST.__got: 0x4e8
-  __DATA_CONST.__const: 0x6a28
+  __DATA_CONST.__const: 0x6a08
   __DATA_CONST.__objc_classlist: 0x878
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x10698
-  __DATA_CONST.__objc_selrefs: 0x56e0
+  __DATA_CONST.__objc_const: 0x10690
+  __DATA_CONST.__objc_selrefs: 0x5718
   __DATA_CONST.__objc_arraydata: 0x390
-  __AUTH_CONST.__cfstring: 0xd100
-  __AUTH_CONST.__objc_const: 0x6af0
+  __AUTH_CONST.__cfstring: 0xd120
+  __AUTH_CONST.__objc_const: 0x6b38
   __AUTH_CONST.__const: 0xf00
   __AUTH_CONST.__objc_arrayobj: 0x2b8
   __AUTH_CONST.__objc_intobj: 0x888

   __DATA.__objc_ivar: 0xa0c
   __DATA.__data: 0x21a0
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x388
+  __DATA.__bss: 0x390
   __DATA_DIRTY.__objc_data: 0x3b88
   __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/CloudKit.framework/CloudKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 4657
-  Symbols:   16547
-  CStrings:  8315
+  Functions: 4661
+  Symbols:   16564
+  CStrings:  8332
 
Symbols:
+ +[TRISQLiteMAAutoAsset setPaths:]
+ -[TRIInternalSystemServiceRequestHandler saveAssetWithIdentifier:sourcePath:flockWitness:removeSourceOnFailure:sourceExtension:completion:]
+ -[TRIMAAutoAsset currentAssetSizeOnDiskUsingStatus:]
+ -[TRIMAProvider cancelActivityForSelector:completion:]
+ -[TRISQLiteMAAutoAsset currentAssetSizeOnDiskUsingStatus:]
+ -[TRISQLiteMADatabase cancelActivityForSelector:completion:]
+ -[TRIStorageManagement _eliminateAllMAAssets]
+ -[TRIStorageManagement _readSchemaVersion:fileExists:]
+ _TRIDNotificationBeginRetryActivity
+ __OBJC_$_CLASS_METHODS_TRISQLiteMAAutoAsset
+ ___102-[TRICKNativeArtifactProvider _fetchRolloutNotificationWithRolloutId:deploymentId:options:completion:]_block_invoke.217
+ ___108-[TRICKNativeArtifactProvider fetchAssetsWithIndexes:fromTreatmentWithRecordId:options:progress:completion:]_block_invoke.206
+ ___108-[TRICKNativeArtifactProvider fetchAssetsWithIndexes:fromTreatmentWithRecordId:options:progress:completion:]_block_invoke_2.210
+ ___115-[TRICKNativeArtifactProvider _fetchRecordIdsForAssetsWithIds:options:cursor:cancelableOp:resultBuffer:completion:]_block_invoke.232
+ ___116-[TRICKNativeArtifactProvider _fetchRolloutNotificationsWithCursor:options:sinceDate:namespaceNames:resultsHandler:]_block_invoke.215
+ ___119-[TRICKNativeArtifactProvider fetchDiffSourceRecordIdsWithTargetAssetIds:isAcceptableSourceAssetId:options:completion:]_block_invoke.260
+ ___119-[TRICKNativeArtifactProvider fetchDiffSourceRecordIdsWithTargetAssetIds:isAcceptableSourceAssetId:options:completion:]_block_invoke.262
+ ___127-[TRICKNativeArtifactProvider _fetchNotificationsWithQueryType:withCursor:withNamespaceNames:sinceDate:options:resultsHandler:]_block_invoke.154
+ ___127-[TRICKNativeArtifactProvider _fetchNotificationsWithQueryType:withCursor:withNamespaceNames:sinceDate:options:resultsHandler:]_block_invoke.158
+ ___129-[TRICKNativeArtifactProvider fetchExperimentNotificationsForLimitedCarryExperimentWithManager:options:rollbacksOnly:completion:]_block_invoke.175
+ ___156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.275
+ ___158-[TRICKNativeArtifactProvider fetchDiffsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.263
+ ___158-[TRICKNativeArtifactProvider fetchDiffsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.266
+ ___159-[TRICKNativeArtifactProvider fetchAssetsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.238
+ ___159-[TRICKNativeArtifactProvider fetchAssetsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.240
+ ___159-[TRICKNativeArtifactProvider fetchAssetsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke_2.244
+ ___34-[TRICancelableMAOperation cancel]_block_invoke.395
+ ___45-[TRIStorageManagement _eliminateAllMAAssets]_block_invoke
+ ___53-[TRIMAProvider installedAssetsMatchingFullAssetIds:]_block_invoke.419
+ ___71-[TRICKNativeArtifactProvider fetchTreatmentWithId:options:completion:]_block_invoke.197
+ ___75-[TRICKNativeArtifactProvider fetchFactorPackSetWithId:options:completion:]_block_invoke.221
+ ___79-[TRIFactorPackSetStorage migrateEligibleFactorPacksToGlobalWithServerContext:]_block_invoke.134
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.426
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.430
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.431
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.434
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.439
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.442
+ ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke_2.432
+ ___82-[TRICKNativeArtifactProvider fetchBMLTCatalogNotificationWithOptions:completion:]_block_invoke.270
+ ___84-[TRICKNativeArtifactProvider _fetchBMLTNotificationsWithCursor:options:completion:]_block_invoke.280
+ ___84-[TRIRemoteAssetStoreOperator saveFactorPackToGlobalPath:fromTemporaryPath:factors:]_block_invoke.291
+ ___86-[TRICKNativeArtifactProvider fetchBMLTNotificationWithDeployment:options:completion:]_block_invoke.275
+ ___87-[TRICKNativeArtifactProvider _fetchRolloutNotificationsWithCursor:options:completion:]_block_invoke.216
+ ___88-[TRIAssetStoreDatabase initWithPaths:databasePath:storageManagement:performMigrations:]_block_invoke.60
+ ___98-[TRIAssetStoreDatabase enumerateOnDiskMAReferencesWithoutCorrespondingDatabaseEntriesUsingBlock:]_block_invoke.153
+ ___Block_byref_object_copy_.235
+ ___Block_byref_object_dispose_.236
+ ___block_descriptor_64_e8_32s40s48r56w_e48_v24?0"TRIClientFactorPackStreamingParser"8^B16lw56l8s32l8s40l8r48l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e53_v32?0"TRIFullMAAssetId"8"TRIMAAssetMetadata"16^B24ls32l8r56l8s40l8s48l8r64l8
+ ___block_literal_global.149
+ ___block_literal_global.156
+ ___block_literal_global.177
+ ___block_literal_global.269
+ ___block_literal_global.422
+ __unnamed_array_storage.181
+ __unnamed_array_storage.414
+ __unnamed_array_storage.421
+ __unnamed_array_storage.66
+ _objc_msgSend$_eliminateAllMAAssets
+ _objc_msgSend$_readSchemaVersion:fileExists:
+ _objc_msgSend$availableForUseAttributes
+ _objc_msgSend$cStringUsingEncoding:
+ _objc_msgSend$cancelActivityForSelector:completion:
+ _objc_msgSend$currentAssetSizeOnDiskUsingStatus:
+ _objc_msgSend$downloadedFactorsWithPaths:
+ _objc_msgSend$numberWithLong:
+ _objc_msgSend$saveAssetWithIdentifier:sourcePath:flockWitness:removeSourceOnFailure:sourceExtension:completion:
+ _sqliteMADatabasePaths
- -[TRIInternalSystemServiceRequestHandler saveAssetWithIdentifier:sourcePath:flockWitness:removeSourceOnFailure:completion:]
- -[TRIStorageManagement _readSchemaVersion:]
- ___102-[TRICKNativeArtifactProvider _fetchRolloutNotificationWithRolloutId:deploymentId:options:completion:]_block_invoke.216
- ___108-[TRICKNativeArtifactProvider fetchAssetsWithIndexes:fromTreatmentWithRecordId:options:progress:completion:]_block_invoke.205
- ___108-[TRICKNativeArtifactProvider fetchAssetsWithIndexes:fromTreatmentWithRecordId:options:progress:completion:]_block_invoke_2.209
- ___115-[TRICKNativeArtifactProvider _fetchRecordIdsForAssetsWithIds:options:cursor:cancelableOp:resultBuffer:completion:]_block_invoke.231
- ___116-[TRICKNativeArtifactProvider _fetchRolloutNotificationsWithCursor:options:sinceDate:namespaceNames:resultsHandler:]_block_invoke.214
- ___119-[TRICKNativeArtifactProvider fetchDiffSourceRecordIdsWithTargetAssetIds:isAcceptableSourceAssetId:options:completion:]_block_invoke.259
- ___119-[TRICKNativeArtifactProvider fetchDiffSourceRecordIdsWithTargetAssetIds:isAcceptableSourceAssetId:options:completion:]_block_invoke.261
- ___127-[TRICKNativeArtifactProvider _fetchNotificationsWithQueryType:withCursor:withNamespaceNames:sinceDate:options:resultsHandler:]_block_invoke.153
- ___127-[TRICKNativeArtifactProvider _fetchNotificationsWithQueryType:withCursor:withNamespaceNames:sinceDate:options:resultsHandler:]_block_invoke.157
- ___129-[TRICKNativeArtifactProvider fetchExperimentNotificationsForLimitedCarryExperimentWithManager:options:rollbacksOnly:completion:]_block_invoke.173
- ___156-[TRIAssetStoreOperator collectGarbageOlderThanNumScans:deletedAssetSize:ignoreRecentlyCreatedAssets:dryRun:includedCacheDeletableAssetIds:deletedAssetIds:]_block_invoke.278
- ___158-[TRICKNativeArtifactProvider fetchDiffsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.262
- ___158-[TRICKNativeArtifactProvider fetchDiffsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.265
- ___159-[TRICKNativeArtifactProvider fetchAssetsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.237
- ___159-[TRICKNativeArtifactProvider fetchAssetsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke.239
- ___159-[TRICKNativeArtifactProvider fetchAssetsWithRecordIds:options:perRecordProgress:perRecordCompletionBlockOnSuccess:perRecordCompletionBlockOnError:completion:]_block_invoke_2.243
- ___34-[TRICancelableMAOperation cancel]_block_invoke.389
- ___37-[TRIStorageManagement _clearStorage]_block_invoke
- ___53-[TRIMAProvider installedAssetsMatchingFullAssetIds:]_block_invoke.413
- ___71-[TRICKNativeArtifactProvider fetchTreatmentWithId:options:completion:]_block_invoke.196
- ___75-[TRICKNativeArtifactProvider fetchFactorPackSetWithId:options:completion:]_block_invoke.220
- ___79-[TRIFactorPackSetStorage migrateEligibleFactorPacksToGlobalWithServerContext:]_block_invoke.138
- ___79-[TRIFactorPackSetStorage migrateEligibleFactorPacksToGlobalWithServerContext:]_block_invoke_2
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.420
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.424
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.425
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.428
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.433
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke.436
- ___79-[TRIMAProvider downloadAssets:attribution:aggregateProgress:group:completion:]_block_invoke_2.426
- ___80-[TRIPostUpgradeCleanupTask _saveProtoToFlatbufferFormatWithPaths:namespaceUrl:]_block_invoke
- ___82-[TRICKNativeArtifactProvider fetchBMLTCatalogNotificationWithOptions:completion:]_block_invoke.269
- ___84-[TRICKNativeArtifactProvider _fetchBMLTNotificationsWithCursor:options:completion:]_block_invoke.279
- ___84-[TRIRemoteAssetStoreOperator saveFactorPackToGlobalPath:fromTemporaryPath:factors:]_block_invoke.288
- ___86-[TRICKNativeArtifactProvider fetchBMLTNotificationWithDeployment:options:completion:]_block_invoke.274
- ___87-[TRICKNativeArtifactProvider _fetchRolloutNotificationsWithCursor:options:completion:]_block_invoke.215
- ___88-[TRIAssetStoreDatabase initWithPaths:databasePath:storageManagement:performMigrations:]_block_invoke.61
- ___98-[TRIAssetStoreDatabase enumerateOnDiskMAReferencesWithoutCorrespondingDatabaseEntriesUsingBlock:]_block_invoke.154
- ___Block_byref_object_copy_.234
- ___Block_byref_object_dispose_.235
- ___block_descriptor_64_e8_32s40s48s56r_e48_v24?0"TRIClientFactorPackStreamingParser"8^B16ls32l8s40l8s48l8r56l8
- ___block_descriptor_64_e8_32s40s48s56s_e28_v24?0"TRIFactorLevel"8^B16ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56r64r_e53_v32?0"TRIFullMAAssetId"8"TRIMAAssetMetadata"16^B24ls32l8s40l8s48l8r56l8r64l8
- ___block_literal_global.155
- ___block_literal_global.176
- ___block_literal_global.268
- ___block_literal_global.416
- __unnamed_array_storage.180
- __unnamed_array_storage.413
- __unnamed_array_storage.420
- __unnamed_array_storage.67
- _objc_msgSend$_readSchemaVersion:
- _objc_msgSend$hostingProcessIsTriald
- _objc_msgSend$saveAssetWithIdentifier:sourcePath:flockWitness:removeSourceOnFailure:completion:
CStrings:
+ "@\"NSNumber\"24@0:8^@16"
+ "B32@0:8^I16^B24"
+ "Failed to consume a sandbox extension"
+ "Failed to create or copy global factor pack to a temporary directory."
+ "Failed to create or copy global fb factor pack to a temporary directory."
+ "Flatbuffer Storage: Factor pack set %{public}@ contains ineligible factor pack. Re-fetching factor pack to find replacement."
+ "Flatbuffer Storage: Factor pack set %{public}@ is already present; skipping download of factor packs. Path: %@"
+ "Removing local asset store following successful migration to global."
+ "Sep 30 2023"
+ "Successfully consumed save asset extension."
+ "Successfully created save asset extension."
+ "Successfully migrated assets to the global asset store"
+ "TrialXP-395.1.10"
+ "Unable to get extension token. Bailing out from saveAssetWithIdentifier"
+ "Upon fetch operation being cancelled, cancelled activity for MAAutoAsset: %{public}@"
+ "Upon fetch operation being cancelled, failed to cancel activity for MAAutoAsset %{public}@: %{public}@"
+ "_UnarchivedSize"
+ "_eliminateAllMAAssets"
+ "_readSchemaVersion:fileExists:"
+ "availableForUseAttributes"
+ "bmlt_completed_fetch"
+ "cStringUsingEncoding:"
+ "cancelActivityForSelector:completion:"
+ "cloudkit container unknown for: %{public}@"
+ "com.apple.trial.Server.test.retries-networking"
+ "currentAssetSizeOnDiskUsingStatus:"
+ "downloadedFactorsWithPaths:"
+ "globalSourcePath"
+ "numberWithLong:"
+ "saveAssetWithIdentifier:sourcePath:flockWitness:removeSourceOnFailure:sourceExtension:completion:"
+ "setPaths:"
+ "v60@0:8@\"NSString<TRIAssetId>\"16@\"NSString\"24^{TRIFlockWitness_=i}32B40@\"NSString\"44@?<v@?B>52"
+ "v60@0:8@16@24^{TRIFlockWitness_=i}32B40@44@?52"
- "%@/factorPacks/%@/maRefs/%@"
- "Aug  6 2023"
- "Flabuffer Storage: Factor pack set %{public}@ contains ineligible factor pack. Re-fetching factor pack to find replacement."
- "Flabuffer Storage: Factor pack set %{public}@ is already present; skipping download of factor packs. Path: %@"
- "Get asset size for garbage collect"
- "Successfully migrated assets to the global asset store. Removing local asset store."
- "TrialXP-395.2"
- "Upon fetch operation being cancelled, eliminated MAAutoAsset: %{public}@"
- "Upon fetch operation being cancelled, failed to eliminate MAAutoAsset %{public}@: %{public}@"
- "_readSchemaVersion:"
- "bmlt_notification"
- "cloudkit container unkown for: %{public}@"
- "hostingProcessIsTriald"
- "saveAssetWithIdentifier:sourcePath:flockWitness:removeSourceOnFailure:completion:"
- "v52@0:8@\"NSString<TRIAssetId>\"16@\"NSString\"24^{TRIFlockWitness_=i}32B40@?<v@?B>44"
- "v52@0:8@16@24^{TRIFlockWitness_=i}32B40@?44"

```
