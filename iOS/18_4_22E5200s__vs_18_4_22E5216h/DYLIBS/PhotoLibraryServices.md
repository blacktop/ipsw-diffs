## PhotoLibraryServices

> `/System/Library/PrivateFrameworks/PhotoLibraryServices.framework/PhotoLibraryServices`

```diff

-750.5.104.0.0
-  __TEXT.__text: 0x695ec0
-  __TEXT.__auth_stubs: 0x3f20
+750.11.101.0.0
+  __TEXT.__text: 0x697628
+  __TEXT.__auth_stubs: 0x3f30
   __TEXT.__delay_stubs: 0x2c
   __TEXT.__delay_helper: 0xa4
-  __TEXT.__objc_methlist: 0x40bc4
+  __TEXT.__objc_methlist: 0x40ca4
   __TEXT.__const: 0x5f40
   __TEXT.__dlopen_cstrs: 0xa03
-  __TEXT.__gcc_except_tab: 0x22a68
-  __TEXT.__oslogstring: 0x776e4
-  __TEXT.__cstring: 0x61188
+  __TEXT.__gcc_except_tab: 0x22a0c
+  __TEXT.__oslogstring: 0x77704
+  __TEXT.__cstring: 0x61176
   __TEXT.__ustring: 0x57c
-  __TEXT.__unwind_info: 0x14130
-  __TEXT.__objc_classname: 0x9c55
-  __TEXT.__objc_methname: 0xbb686
-  __TEXT.__objc_methtype: 0x12207
-  __TEXT.__objc_stubs: 0x77520
-  __DATA_CONST.__got: 0x4a08
-  __DATA_CONST.__const: 0x14a88
+  __TEXT.__unwind_info: 0x14178
+  __TEXT.__objc_classname: 0x9c4f
+  __TEXT.__objc_methname: 0xbbba9
+  __TEXT.__objc_methtype: 0x1226c
+  __TEXT.__objc_stubs: 0x777c0
+  __DATA_CONST.__got: 0x4ae0
+  __DATA_CONST.__const: 0x14af0
   __DATA_CONST.__objc_classlist: 0x20e0
   __DATA_CONST.__objc_catlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x688
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x22cb0
+  __DATA_CONST.__objc_selrefs: 0x22d70
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x1528
-  __DATA_CONST.__objc_arraydata: 0x1938
-  __AUTH_CONST.__auth_got: 0x1fa8
+  __DATA_CONST.__objc_arraydata: 0x18f0
+  __AUTH_CONST.__auth_got: 0x1fb0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x5358
-  __AUTH_CONST.__cfstring: 0x4c9e0
-  __AUTH_CONST.__objc_const: 0x68090
-  __AUTH_CONST.__objc_intobj: 0x4758
-  __AUTH_CONST.__objc_arrayobj: 0x1218
+  __AUTH_CONST.__cfstring: 0x4c8c0
+  __AUTH_CONST.__objc_const: 0x68078
+  __AUTH_CONST.__objc_intobj: 0x4710
+  __AUTH_CONST.__objc_arrayobj: 0x1200
   __AUTH_CONST.__objc_doubleobj: 0x110
   __AUTH_CONST.__objc_dictobj: 0x348
   __AUTH_CONST.__objc_floatobj: 0x50
   __AUTH.__objc_data: 0x11490
-  __DATA.__objc_ivar: 0x3c70
+  __DATA.__objc_ivar: 0x3c6c
   __DATA.__data: 0x5ec0
   __DATA.__crash_info: 0x40
-  __DATA.__bss: 0x24f8
+  __DATA.__bss: 0x2508
   __DATA.__common: 0xc
   __DATA_DIRTY.__objc_data: 0x3430
   __DATA_DIRTY.__bss: 0x1d8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 25594
-  Symbols:   31647
-  CStrings:  47095
+  Functions: 25621
+  Symbols:   31689
+  CStrings:  47110
 
Symbols:
+ _ACAccountDataclassImagePlayground
+ _ACAccountDataclassMediaStream
+ _ACAccountDataclassSharedStreams
+ _PLAzimuthBetweenCoordinates
+ _PLAzimuthDistancePairFrom
+ _PLImagePlaygroundAppBundleIdentifier
+ _PLIsImagePlaygroundApp
+ _PLMigrationKitBundleId
+ _PLPersistedFolderMetadataAssetUUIDsKey
+ _PLPersistedFolderMetadataCloudGUIDKey
+ _PLPersistedFolderMetadataCustomSortAscendingKey
+ _PLPersistedFolderMetadataCustomSortKeyKey
+ _PLPersistedFolderMetadataIsInTrashKey
+ _PLPersistedFolderMetadataIsPinnedKey
+ _PLPersistedFolderMetadataIsPrototypeKey
+ _PLPersistedFolderMetadataKindKey
+ _PLPersistedFolderMetadataLastModifiedDateKey
+ _PLPersistedFolderMetadataTitleKey
+ _PLPersistedFolderMetadataUuidKey
+ _PLScreenshotsBundleId
+ _PLSearchJSONPhotosInferredTimeZoneOffsetKey
+ _PLSearchSemanticSearchQueriesSupportedForWhatsNew
- _MigrationKitBundleId
- _PLACAccountDataclassImagePlayground
- _PLCreateShortLivedPhotoLibraryWithPhotoLibraryURL
- _PLPhotosPickerBundleId
- _PLSearchPartsOfDayForLocalDate
- _PLSearchPartsOfWeekForLocalDate
- _ScreenshotsBundleId
CStrings:
+ " album %@ : title:%@, uuid:%@, cloudGUID:%@, kind:%@, pin:%@, prototype:%@, trash:%@, sort:%@ asc:%@, lastModifiedDate:%@, childCount:%lu"
+ "%K >= %@ && %K < %llu && %K < %d"
+ "%s %{public}@ / %{public}@"
+ "%s calling SPL syndicationDeleteManager to delete %{public}@ for bundleID %{public}@"
+ "%s done deleting %{public}@ from SPL"
+ "%s failed attempting to delete %{public}@ from SPL, error %@"
+ "%{public}@ Deleted %lu syndication guest asset(s) in %@ for bundleID: %{public}@"
+ "%{public}@: Running await block, state before enqueue: %{public}@ at QoS: %{public}@)"
+ "(%K != %d) || (%K != %d)"
+ "(%K < %d) || (%K < %d)"
+ "+[PLPhotoLibraryOpener runningLibraryServicesManagerForPhotoLibraryURL:error:]"
+ "-[PLManagedAsset(Syndication) rejectSyndicatedAsset]"
+ "-[PLManagedAsset(Syndication) rejectSyndicatedAsset]_block_invoke"
+ "-[PLManagedAssetRecoveryManager identifyAssetsWithInconsistentAdjustedFullSizeRenderDeferredProcessing]"
+ ".CPL"
+ ".Rebuild"
+ "<%@: %p> asset=%@ dataStoreSubtype=%@ size=%lldx%lld availability local=%@/remote=%@"
+ "@32@0:8q16^@24"
+ "@40@0:8@16@24^q32"
+ "@72@0:8r*16r*24r*32s40d44Q52Q60B68"
+ "@88@0:8@16@24@32@40@48Q56Q64Q72@80"
+ "Attempt to open library with well known identifier %ld"
+ "Auto-create %{public}@ succeeded. LSM in createMode with options %@"
+ "CSSearchableIndex provideDataForBundle %@ returned no data and no error for item %@ type %@"
+ "Determined trip moment %@ is outlier due to angle %f between previous (%@) and next (%@)"
+ "Distributed notification handler: Unable to open system photo library: %@"
+ "Failed to update feature availability after missing Spotlight client state, error: %@"
+ "Failed to update feature availability after search index drop, error: %@"
+ "Failed to update feature availability in response to search index rebuild, error: %@"
+ "Found %tu asset(s) for deletion using %tu unprefixed identifiers"
+ "INSERT INTO collections(uuid_0, uuid_1, startDate, endDate, title, subtitle, type, assetsCountPrivate, assetsCountShared, sortDate) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
+ "Inserted collection with UUID %{public}@, title \"%@\", at collectionId: %{public}lld"
+ "Insufficent number of assets with all members present"
+ "Missing dateCreated for asset: %{public}@. Unable to index creation date."
+ "No curated assets for Memory. Not adding to PSI: %{public}@"
+ "No curated assets for Memory. Not adding to Spotlight: %{public}@"
+ "PLSearchIndexCategoryPartOfDaySynonym"
+ "PLSearchIndexCategoryPartOfWeekSynonym"
+ "SELECT content_string, normalized_string, lookup_identifier, category, rowid, owning_groupid, score FROM groups WHERE rowid IN matchingIds"
+ "SELECT content_string, normalized_string, lookup_identifier, category, rowid, owning_groupid, score from groups"
+ "SELECT content_string, normalized_string, lookup_identifier, category, rowid, owning_groupid, score from groups WHERE category IN (?"
+ "SELECT content_string, normalized_string, lookup_identifier, category, rowid, owning_groupid, score from groups WHERE owning_groupid IN matchingIds AND category IN (?"
+ "SELECT content_string, normalized_string, lookup_identifier, category, rowid, owning_groupid, score from groups WHERE rowid IN matchingIds AND category IN (?"
+ "Service instance deallocated"
+ "Service was deallocated"
+ "TCC Observer: Unable to open system photo library: %@"
+ "Unsupported Memory. Not indexing Memory: %{public}@"
+ "_assetIDsPassingContainmentRequirementsFromAssetPersonEdgeDictionaries:potentialAssetIDs:personIDsByAssetID:error:"
+ "_assetIDsWithRequiredPersonsPresentWithAssetIDs:minimumNumberOfSharedAssets:error:"
+ "_autoCreateWellKnownPhotoLibraryIfNeededWithURL:libraryServicesManager:wellKnownLibraryIdentifier:"
+ "_containmentResultFromPersonIDsByAssetID:exclusivePotentialAssetIDs:error:"
+ "_cplViewPresentationFromPLViewPresentation:"
+ "_exclusivePotentialAssetIDsFromAssetPersonEdgeDictionaries:potentialInclusiveAssetIDs:containmentProgress:error:"
+ "_inqGenerateGroupsInfoDictionaryFromContentString:normalizedString:identifier:category:score:groupId:owningGroupId:includeUUIDs:"
+ "_isCurrentMomentOutlierWithPreviousMoment:currentMoment:nextMoment:"
+ "_isTimeDeltaViableForDistanceDeltaBetweenPreviousMoment:currentMoment:"
+ "_isValidChangeSourceForUpdate"
+ "_isValidLibraryRoleForUpdate"
+ "_partsOfDayForAsset:"
+ "_partsOfWeekForAsset:"
+ "_removeOutliersFromTripsMoments:"
+ "_runAssetContainmentOnAssetIDs:minimumNumberOfSharedAssets:error:"
+ "_splitTripsMomentsFromTripsMoments:"
+ "_stateHandler == nil"
+ "_updateViewPresentationForCPLAssetChange:"
+ "_updateViewPresentationFromCPLAssetViewPresentation:"
+ "autoCreateWellKnownPhotoLibraryIfNeededWithURL:libraryServicesManager:wellKnownLibraryIdentifier:"
+ "cloudViewPresentation"
+ "deleteAllSearchableItemsWithProtectionClass:forBundleID:options:completionHandler:"
+ "enqueueOperationWithName:requiredState:executionBlock:"
+ "estimatedLibrarySizes started at QoS: %{public}@"
+ "estimatedLibrarySizes took: %fs"
+ "fingerprintSchemeForFingerprint:"
+ "identifyAssetsWithInconsistentAdjustedFullSizeRenderDeferredProcessing"
+ "initForTestingWithLibraryBundle:delegateClass:"
+ "initWithUUID:startDate:endDate:title:subtitle:type:assetsCountPrivate:assetsCountShared:sortDate:"
+ "isEquivalentToFingerprint:andStableHash:fingerprintContext:"
+ "lsm != nil"
+ "normalized_string"
+ "operationWithName:libraryServicesManager:requiredState:parentProgress:executionBlock:"
+ "partOfDayLocalizedStringsForLocalDate:result:"
+ "partOfWeekLocalizedStringsForLocalDate:result:"
+ "photosInferredTimeZoneOffset"
+ "providesEnhancedPrivacy"
+ "runAssetContainmentWithMinimumNumberOfSharedAssets:error:"
+ "runningLibraryServicesManagerForPhotoLibraryURL:error:"
+ "runningLibraryServicesManagerForWellKnownPhotoLibraryIdentifier:error:"
+ "setCloudViewPresentation:"
+ "setPhotosInferredTimeZoneOffset:"
+ "stableHashFromOriginalResourceError:"
+ "v16@?0@\"PLLibraryServicesManager\"8"
+ "v40@0:8@\"NSArray\"16@\"NSString\"24@?<v@?@\"NSData\"@\"NSError\">32"
+ "validatePromptSuggestionsWithSuggestionUUIDs:operationID:reply:"
- "\x04\x11\""
- "\x18"
- " album %@ : title:%@, uuid:%@, cloudGUID:%@, kind:%@, pin:%@, prototype:%@, trash:%@, sort:%@ asc:%@, childCount:%lu"
- "%K != %@ && %K < %llu && %K < %d"
- "%K != %d AND %K == %d AND (%K != %d)"
- "%{public}@ Deleted %lu syndication guest asset(s) in %@ for bundleID: %{public}@, identifiers: %{public}@"
- "%{public}@: Running await block, current state: %{public}@ at QoS: %{public}@)"
- "(%K != %d) && (%K != %d)"
- "(%K < %d) && (%K < %d)"
- "<%@: %p> asset=%@ dataStoreSubtype=%@ size=%lldx%lld availability remote/local=%@/%@"
- "@\"NSArray\"24@0:8q16"
- "@\"PSIAsset\""
- "@64@0:8r*16r*24s32d36Q44Q52B60"
- "Album %@ keyAssetUUID caught exception: %@"
- "Distributed notification handler: No library bundle for URL %@"
- "Distributed notification handler: Unable to open library at URL: %@, error: %@"
- "Failed to get Parts-of-Day for localDate: %@, error: %@"
- "Failed to get Parts-of-Week for localDate: %@, error: %@"
- "Found %tu asset(s) for deletion using unprefixed identifiers: %{public}@"
- "INSERT INTO collections(uuid_0, uuid_1, startDate, endDate, title, subtitle, type, keyAssetUUIDPrivate, keyAssetUUIDShared, assetsCountPrivate, assetsCountShared, sortDate) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
- "Inserted collection with UUID %{public}@, title \"%@\", keyAssetUUIDPrivate %{public}@, keyAssetUUIDShared: %{public}@, at collectionId: %{public}lld"
- "No assets found for Album. Not translating Album: %@"
- "No assets found for Memory. Not indexing Memory: %@"
- "No key asset for collection UUID: %{public}@"
- "No key asset found for Album. Not translating Album: %@"
- "No key asset found for Memory. Not translating Memory: %@"
- "PLLibraryServicesManager * _Nullable PLLibraryServicesManagerForPhotoLibraryURL(NSURL *__strong, PLPhotoLibraryBundleController *__strong, NSError *__autoreleasing *)"
- "SELECT normalized_string, lookup_identifier, category, rowid, owning_groupid, score FROM groups WHERE rowid IN matchingIds"
- "SELECT normalized_string, lookup_identifier, category, rowid, owning_groupid, score from groups"
- "SELECT normalized_string, lookup_identifier, category, rowid, owning_groupid, score from groups WHERE category IN (?"
- "SELECT normalized_string, lookup_identifier, category, rowid, owning_groupid, score from groups WHERE owning_groupid IN matchingIds AND category IN (?"
- "SELECT normalized_string, lookup_identifier, category, rowid, owning_groupid, score from groups WHERE rowid IN matchingIds AND category IN (?"
- "T@\"PSIAsset\",C,N,V_keyAssetPrivate"
- "T@\"PSIAsset\",C,N,V_keyAssetShared"
- "TCC Observer: No library bundle for URL %@"
- "TCC Observer: Unable to open library at URL: %@, error: %@"
- "Unsupported Memory. Not indexing Memory: %@"
- "_assetIDsPassingContainmentRequirementsFromAssetPersonEdgeDictionaries:error:"
- "_assetIDsWithRequiredPersonsPresentWithAssetIDs:error:"
- "_inqGenerateGroupsInfoDictionaryFromText:identifier:category:score:groupId:owningGroupId:includeUUIDs:"
- "_keyAssetPrivate"
- "_keyAssetShared"
- "_keyAssetUUIDForAlbum:"
- "_potentialAssetIDsFromAssetPersonEdgeDictionaries:containmentProgress:error:"
- "_psiAssetForAlbum:calendar:"
- "_psiAssetForMemory:calendar:"
- "_stableHashFromOriginalResourceOfMaster:error:"
- "autoCreateWellKnownPhotoLibraryIfNeededWithURL:wellKnownLibraryIdentifier:"
- "com.apple.Capture"
- "com.apple.CarPlayApp"
- "com.apple.CloudDocs.MobileDocumentsFileProvider"
- "com.apple.CloudDocs.iCloudDriveFileProvider"
- "com.apple.CloudDocs.iCloudDriveFileProviderManaged"
- "com.apple.Dataclass.ImagePlayground"
- "com.apple.FileProvider.LocalStorage"
- "com.apple.GenerativePlaygroundApp"
- "com.apple.MigrationKit"
- "com.apple.MobileSMS"
- "com.apple.ScreenshotServicesService"
- "com.apple.Spotlight"
- "com.apple.Stickers"
- "com.apple.SurfBoard"
- "com.apple.mobilenotes"
- "com.apple.photos.filesPlaceholder"
- "com.apple.quicklook.extension.previewUI"
- "com.apple.share.System.add-to-iphoto"
- "com.apple.sharingd"
- "com.apple.springboard"
- "estimatedLibrarySizes took: %fs)"
- "initWithUUID:startDate:endDate:title:subtitle:keyAssetPrivate:keyAssetShared:type:assetsCountPrivate:assetsCountShared:sortDate:"
- "keyAssetUUIDPrivate: %@, "
- "keyAssetUUIDShared: %@, "
- "operationWithName:requiredState:parentProgress:execution:"
- "operationsForLibraryStateTransition:"
- "partOfDayLocalizedNamesForLocalDate:error:"
- "partOfWeekLocalizedNamesForLocalDate:error:"
- "rejectSyndicatedAsset: %{public}@ / %{public}@"
- "rejectSyndicatedAsset: calling SPL syndicationDeleteManager to delete %{public}@ for bundleID %{public}@"
- "rejectSyndicatedAsset: done deleting %{public}@ from SPL"

```
