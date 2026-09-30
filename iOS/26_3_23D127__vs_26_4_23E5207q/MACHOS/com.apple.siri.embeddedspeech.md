## com.apple.siri.embeddedspeech

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/XPCServices/com.apple.siri.embeddedspeech.xpc/com.apple.siri.embeddedspeech`

```diff

-3515.11.1.0.0
-  __TEXT.__text: 0x2fc14
-  __TEXT.__auth_stubs: 0x940
-  __TEXT.__objc_stubs: 0x7d80
-  __TEXT.__objc_methlist: 0x1a44
-  __TEXT.__const: 0x110
-  __TEXT.__gcc_except_tab: 0x1c70
-  __TEXT.__cstring: 0x4328
-  __TEXT.__objc_methname: 0x9a85
-  __TEXT.__oslogstring: 0x476a
-  __TEXT.__objc_classname: 0x201
-  __TEXT.__objc_methtype: 0x19bf
-  __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x6e8
-  __DATA_CONST.__auth_got: 0x4b0
-  __DATA_CONST.__got: 0x6d0
+3520.87.3.1.5
+  __TEXT.__text: 0x34360
+  __TEXT.__auth_stubs: 0x900
+  __TEXT.__objc_stubs: 0x81e0
+  __TEXT.__objc_methlist: 0x1be4
+  __TEXT.__const: 0xf8
+  __TEXT.__gcc_except_tab: 0x1b78
+  __TEXT.__cstring: 0x47cc
+  __TEXT.__objc_methname: 0xa267
+  __TEXT.__oslogstring: 0x4983
+  __TEXT.__objc_classname: 0x2bb
+  __TEXT.__objc_methtype: 0x1b74
+  __TEXT.__unwind_info: 0x790
+  __DATA_CONST.__auth_got: 0x490
+  __DATA_CONST.__got: 0x730
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0xb80
-  __DATA_CONST.__cfstring: 0x2c80
-  __DATA_CONST.__objc_classlist: 0x88
+  __DATA_CONST.__const: 0xc68
+  __DATA_CONST.__cfstring: 0x2e00
+  __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_superrefs: 0x70
-  __DATA_CONST.__objc_intobj: 0x90
+  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_arraydata: 0xf8
   __DATA_CONST.__objc_dictobj: 0x50
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2890
-  __DATA.__objc_selrefs: 0x2320
-  __DATA.__objc_ivar: 0x278
-  __DATA.__objc_data: 0x550
-  __DATA.__data: 0x268
+  __DATA.__objc_const: 0x3118
+  __DATA.__objc_selrefs: 0x2458
+  __DATA.__objc_ivar: 0x2f4
+  __DATA.__objc_data: 0x780
+  __DATA.__data: 0x328
   __DATA.__bss: 0x140
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /System/Library/PrivateFrameworks/TrialProto.framework/TrialProto
   - /System/Library/PrivateFrameworks/UnifiedAssetFramework.framework/UnifiedAssetFramework
+  - /System/Library/PrivateFrameworks/VectorSearch.framework/VectorSearch
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4C9C7CC9-F88E-335B-B1EE-4EC14BD3D62B
-  Functions: 556
-  Symbols:   381
-  CStrings:  2768
+  UUID: 6EBB493E-2FA7-37EE-88B2-1BDB1BC85A9A
+  Functions: 587
+  Symbols:   389
+  CStrings:  2913
 
Symbols:
+ _CESRGetLogCategory
+ _CESRLogContextSpeechProfile
+ _CESRProfileServiceGetXPCInterface
+ _CESRSetError
+ _OBJC_CLASS_$_CESREntityCleanupHandler
+ _OBJC_CLASS_$_CESREntityExtractionHandler
+ _OBJC_CLASS_$_EAREuclidCascadeItemPayload
+ _OBJC_CLASS_$_NSIndexSet
+ _OBJC_CLASS_$_NSKeyedArchiver
+ _OBJC_CLASS_$_NSLock
+ _OBJC_CLASS_$_SFSpeechAssetManager
+ _OBJC_CLASS_$_SFUtilities
+ _OBJC_CLASS_$_VSKAsset
+ _OBJC_CLASS_$_VSKAttribute
+ _OBJC_CLASS_$_VSKClient
+ _OBJC_CLASS_$_VSKColumnType
+ _OBJC_CLASS_$_VSKConfig
+ _OBJC_CLASS_$_VSKDatabaseValue
+ _OBJC_CLASS_$_VSKDisjunctiveFilter
+ _OBJC_CLASS_$_VSKFilter
+ _OBJC_CLASS_$__EAREuclid
+ _SFGetOrCreateDirectoryURL
- _CESRSpeechProfileBuilderServiceGetXPCInterface
- _OBJC_CLASS_$_AFFeatureFlags
- _OBJC_CLASS_$_CESRGeoLMRegionIDCache
- _OBJC_CLASS_$_EAREntityCleanup
- _OBJC_CLASS_$_NSBundle
- _OBJC_CLASS_$__EAREntityTagger
- _OBJC_CLASS_$__EARGeoLMHelper
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x6
- _objc_retain_x9
CStrings:
+ "\t-"
+ "!"
+ "%s %@, error: %@"
+ "%s (%@) About to process %lu update(s) for CESREuclidVectorDB"
+ "%s (%@) Attempting to delete assets matching %lu identifier(s) for CESREuclidVectorDB"
+ "%s (%@) Attempting to insert %lu embedding(s) for CESREuclidVectorDB"
+ "%s (%@) Creating payload for item with displayName: %@, itemType: %@"
+ "%s (%@) Creating shared item identifier attribute for CESREuclidVectorDB"
+ "%s (%@) Failed to archive payload for CESREuclidVectorDB entry, error: %@"
+ "%s (%@) Failed to delete %lu embedding(s) from CESREuclidVectorDB, error: %@"
+ "%s (%@) Failed to delete items from CESREuclidVectorDB, error: %@"
+ "%s (%@) Failed to drop CESREuclidVectorDB, error: %@"
+ "%s (%@) Failed to find embedding(s) matching deletion filter within CESREuclidVectorDB, error: %@"
+ "%s (%@) Failed to get size of CESREuclidVectorDB, error: %@"
+ "%s (%@) Failed to initialize VSKClient for CESREuclidVectorDB, error: %@"
+ "%s (%@) Failed to initialize VSKConfig for CESREuclidVectorDB, error: %@"
+ "%s (%@) Failed to insert %lu embedding(s) into CESREuclidVectorDB, error: %@"
+ "%s (%@) Failed to insert items into CESREuclidVectorDB, error: %@"
+ "%s (%@) Failed to load CESREuclidVectorDB database, error: %@"
+ "%s (%@) Failed to rebuild CESREuclidVectorDB, error: %@"
+ "%s (%@) Successfully created payload for sharedItemIdentifier: %@"
+ "%s (%@) Successfully deleted %lu embedding(s) from CESREuclidVectorDB"
+ "%s (%@) Successfully dropped CESREuclidVectorDB"
+ "%s (%@) Successfully inserted %lu embedding(s) into CESREuclidVectorDB"
+ "%s (%@) Successfully updated CESREuclidVectorDB (%lu embeddings total)"
+ "%s About to load CESREuclidVectorDB at path: %@"
+ "%s Accepted %zu/%zu first party contacts."
+ "%s Accepted %zu/%zu group names."
+ "%s Accepted %zu/%zu third party contacts."
+ "%s AppEntity does not have displayRepresentation. Skipping processing."
+ "%s CCSharedItem does not have sourceBundleId. Skipping processing."
+ "%s Enrolled %tu items for template: %@, tag: %@"
+ "%s Enrolled %tu radio entities."
+ "%s Enrolled %tu/%tu processed app entities."
+ "%s Entity Cleanup: Failed to initialize NSDataDetector for NSTextCheckingTypes-based entity sanitization, error: %@"
+ "%s Entity Extraction: Enrolled %ld extracted entities."
+ "%s Existing profile found at path: %@"
+ "%s Failed to deserialize JSON data: %@, error: %@"
+ "%s Failed to enumerate fields, error: %@"
+ "%s Failed to fetch or create CESREuclidVectorDB directory for language: %@, error: %@"
+ "%s Failed to process contact item for first party contacts"
+ "%s Failed to process contact item for group names"
+ "%s Failed to process contact item for third party contacts"
+ "%s Failed to process radio item"
+ "%s Failed to process vocabulary item"
+ "%s Failed to read JSON file at path: %@"
+ "%s Failed to remove speech profile JSON at path: %@, error: %@"
+ "%s Failed to write speech profile JSON to path: %@, error: %@"
+ "%s No Euclid embedding generated for item. Skipping"
+ "%s No assets for insertion."
+ "%s No items for deletion."
+ "%s No items to delete."
+ "%s No items to insert."
+ "%s No metrics for user data."
+ "%s No version for category: %@"
+ "%s Processing %tu items for speech categories: %{public}@"
+ "%s Removing speech profile JSON at path: %@"
+ "%s Siri/asr_speech_profile_app_entities is %@, app entities will %@be consumed."
+ "%s Successfully loaded CESREuclidVectorDB (%lu embeddings total) at path: %@"
+ "%s Successfully removed speech profile JSON at path: %@"
+ "%s Successfully updated speech profile JSON at path: %@"
+ "%s Updating speech profile JSON at path: %@"
+ "%s Using %@ asset for %@ at path: %@"
+ "%s siri_signpost_end_nomsg `%s`"
+ "+[ESContactItemProcessor applyContactLimitsToFirstPartyContacts:thirdPartyContacts:groupNames:]"
+ "+[ESSpeechProfileBuilderConnection userProfileWithAssetConfig:assetManager:modelOverridePath:overrides:isJit:returningFoundPath:error:]"
+ "+[ESUserDataUtilities mutableDictionaryForJSONFile:]"
+ "-[ESAppEntityItemProcessor processAppEntityItem:vocabularyWords:]"
+ "-[ESContactItemProcessor processContactItem:contactWords:]"
+ "-[ESItemProcessor _textDataTypeDetector]"
+ "-[ESItemProcessor addExtractedEntitiesToVocabularyWords:vocabularyWords:]_block_invoke"
+ "-[ESItemProcessor processItem:vocabularyWords:]"
+ "-[ESRadioItemProcessor processRadioItem:radioWords:]"
+ "-[ESSpeechProfileBuilderConnection _aggregateMetricsForUserDatas:]"
+ "-[ESSpeechProfileBuilderConnection _didDeleteEmbeddingsForDeletionIdentifiers:error:]"
+ "-[ESSpeechProfileBuilderConnection _didInsertEmbeddingsFromEuclidProfileInsertionsForAssetIdentifiers:error:]"
+ "-[ESSpeechProfileBuilderConnection _didInsertEmbeddingsFromEuclidProfileInsertionsForAssetIdentifiers:error:]_block_invoke"
+ "-[ESSpeechProfileBuilderConnection _rebuildDatabase:]"
+ "-[ESSpeechProfileBuilderConnection _sharedItemIdentifierAttribute]"
+ "-[ESSpeechProfileBuilderConnection _updateJSONForProfilePath:userDatas:removedCategories:]"
+ "-[ESSpeechProfileBuilderConnection addCodepathId:completion:]"
+ "-[ESSpeechProfileBuilderConnection dropDatabaseWithCompletion:]"
+ "-[ESSpeechProfileBuilderConnection fetchDatabaseWithLanguage:completion:]"
+ "-[ESSpeechProfileBuilderConnection getVersionForCategory:completion:]"
+ "-[ESSpeechProfileBuilderConnection removeCodepathId:completion:]"
+ "-[ESSpeechProfileBuilderConnection updateDatabaseWithEuclidProfileUpdates:completion:]"
+ "-[ESUserData _logUserDataPopulationResultsWithAppEntitiesEnrolled:appEntitiesProcessed:radioWords:vocabularyWords:]"
+ "-[ESUserData _logUserDataPopulationResultsWithAppEntitiesEnrolled:appEntitiesProcessed:radioWords:vocabularyWords:]_block_invoke"
+ "@\"CESREntityCleanupHandler\""
+ "@\"CESREntityExtractionHandler\""
+ "@\"ESAppEntityItemProcessor\""
+ "@\"ESContactItemProcessor\""
+ "@\"ESEntityBudget\""
+ "@\"ESItemProcessor\""
+ "@\"ESRadioItemProcessor\""
+ "@\"NSLock\""
+ "@\"NSURL\""
+ "@\"SFEntitledAssetManager\""
+ "@\"VSKAttribute\""
+ "@\"VSKClient\""
+ "@\"_EAREuclid\""
+ "@24@0:8Q16"
+ "@56@0:8@16Q24Q32Q40Q48"
+ "@68@0:8@16@24@32@40B48^@52^@60"
+ "@84@0:8@16@24@32B40@44@52@60@68@76"
+ "B20@0:8S16"
+ "B24@0:8Q16"
+ "B24@0:8^@16"
+ "B32@0:8@16^@24"
+ "B40@0:8@16@24^@32"
+ "B48@0:8@16@24@32^@40"
+ "CESREuclidProfileService"
+ "CESRProfileService"
+ "ESAppEntityItemProcessor"
+ "ESContactItemProcessor"
+ "ESEntityBudget"
+ "ESItemProcessor"
+ "ESRadioItemProcessor"
+ "ESUserDataUtilities"
+ "ESUserDataWriter"
+ "EnableSpeechProfileJSONDump"
+ "Failed to load speech assets."
+ "Failed to read the existing speech profile."
+ "Failed to resolve CESREuclidVectorDB directory path for language: %@"
+ "File path cannot be nil"
+ "No installed %@ asset for language: %@"
+ "PersonalName"
+ "Speech category %@ has already been committed with a call to Begin followed by Finish."
+ "Speech category %@ is unsupported."
+ "T@\"ESAppEntityItemProcessor\",R,N"
+ "T@\"ESContactItemProcessor\",R,N"
+ "T@\"ESItemProcessor\",R,N"
+ "T@\"ESRadioItemProcessor\",R,N"
+ "Vv32@0:8@\"NSArray\"16@?<v@?B@\"NSError\">24"
+ "Vv60@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32q40B48@?<v@?B@\"NSError\">52"
+ "Vv60@0:8@16@24@32q40B48@?52"
+ "\\appentity-appcontact-first-extracted"
+ "_aggregateMetricsForUserDatas:"
+ "_appEntityItemProcessor"
+ "_applicableSpeechCategories"
+ "_assetManager"
+ "_assetPath"
+ "_contactItemProcessor"
+ "_didDeleteEmbeddingsForDeletionIdentifiers:error:"
+ "_didInsertEmbeddingsFromEuclidProfileInsertionsForAssetIdentifiers:error:"
+ "_earEuclidInstance"
+ "_enableDatatypeCleanupFromNonAppEntities"
+ "_entitiesExtractedPerCategory"
+ "_entityCleanupHandler"
+ "_entityExtractionHandler"
+ "_euclidProfileLanguage"
+ "_initialBudget"
+ "_isSupportedFieldType:"
+ "_itemProcessor"
+ "_lock"
+ "_logUserDataPopulationResultsWithAppEntitiesEnrolled:appEntitiesProcessed:radioWords:vocabularyWords:"
+ "_numEntitiesPerCategoryFromVocabularyWords:totalFirstPartyContactComponents:totalThirdPartyContactComponents:totalGroupNameWords:totalRadioWords:"
+ "_phoneticVectorDatabaseURL"
+ "_radioItemProcessor"
+ "_rebuildDatabase:"
+ "_remainingBudget"
+ "_sharedItemIdentifierAttribute"
+ "_shouldAddExtractedEntities"
+ "_textDataTypeDetector"
+ "_updateJSONForProfilePath:userDatas:removedCategories:"
+ "_vskClient"
+ "addExtractedEntitiesToVocabularyWords:vocabularyWords:"
+ "addWord:withLabel:toWords:"
+ "addressComponentsToSanitize"
+ "appEntityItemProcessor"
+ "applyContactLimitsToFirstPartyContacts:thirdPartyContacts:groupNames:"
+ "applyEntityCleanupToAppEntity:bundleId:entityType:entityCleanupConfig:"
+ "applyEntityCleanupToNonAppEntity:entityCleanupConfig:"
+ "archivedDataWithRootObject:requiringSecureCoding:error:"
+ "boolForKey:"
+ "category cannot be nil."
+ "codepathId cannot be nil."
+ "computeEmbeddings:"
+ "consumeBudget:"
+ "consumedBudget"
+ "contactItemProcessor"
+ "convertVectorToData:"
+ "countWithError:"
+ "dataWithContentsOfFile:"
+ "deleteWithApplyingFilters:error:"
+ "deletionIdentifiers"
+ "dictionaryWithOrthography:"
+ "disabled"
+ "dropDatabaseWithCompletion:"
+ "dropWithError:"
+ "embeddingDim"
+ "enabled"
+ "ensureDirectoryExistsForFilePath:error:"
+ "entityExtractionCategoryLimit"
+ "euclidProfilePathForLanguage:"
+ "extractionLabelForLabel:"
+ "fetchAppEntityMappingForBundleId:appEntityConfig:assistantSchemas:entityType:"
+ "fetchDatabaseWithLanguage:completion:"
+ "field"
+ "fullVersion"
+ "getOrCreateMutableArrayForKey:inDictionary:"
+ "i48@0:8Q16Q24@32@40"
+ "indexSetWithIndexesInRange:"
+ "initWithAttribute:disjunctiveFilters:"
+ "initWithBaseDirectory:distanceMetric:filterableAttributes:dimension:averagePartitionSize:batchSize:batchFactor:tradeOffParameterBetweenClusteringAndBalance:enableFTS:dataType:maxIndexConstructionBatches:readOnly:pretokenizationEnabled:prefixIndices:perConnectionPeakMemory:clientVersion:error:"
+ "initWithBudget:"
+ "initWithConfig:error:"
+ "initWithConfiguration:euclidEncoderType:initFlag:language:"
+ "initWithDirectDonationConfig:entityCleanupHandler:entityExtractionHandler:enableDatatypeCleanupFromNonAppEntities:appEntityConfig:extractedEntityBudget:entitiesExtractedPerCategory:applicableSpeechCategories:entityCleanupConfig:"
+ "initWithDisplayName:itemType:"
+ "initWithEntityCleanupConfig:entityCleanupHandler:"
+ "initWithEntityCleanupHandler:entityCleanupConfig:"
+ "initWithItems:applicableSpeechCategories:assetPath:"
+ "initWithName:columnType:"
+ "initWithObjects:"
+ "initWithOperator:value:"
+ "initWithSet:"
+ "initWithSpeechProfileMetrics:codepathIds:"
+ "initWithSpeechProfileMetrics:codepathIds:entitiesExtractedPerCategory:applicableSpeechCategories:assetPath:"
+ "initWithStringDefaultValue:"
+ "initWithStringIdentifier:vectors:attributes:payload:"
+ "initWithStringValue:"
+ "insertAssets:error:"
+ "insertObjects:atIndexes:"
+ "insertions"
+ "installedAssetWithConfig:shouldSubscribe:subscriberId:expiration:"
+ "itemProcessor"
+ "json"
+ "limitVocabularyWords:toApplicableSpeechCategories:"
+ "lock"
+ "mutableDictionaryForJSONFile:"
+ "mutableDictionaryRepresentationForUserData:"
+ "not "
+ "numEntitiesPerCategory"
+ "numberWithInt:"
+ "orthography"
+ "performEntityExtraction:extractionVocabLabels:"
+ "personExtractionLabel"
+ "processAppEntityItem:vocabularyWords:"
+ "processContactItem:contactWords:"
+ "processItem:vocabularyWords:"
+ "processItemFieldContent:fieldType:vocabularyLabel:vocabularyWords:"
+ "processRadioItem:radioWords:"
+ "profileFilePathFromBasePath:language:"
+ "pronunciations"
+ "purgeInstalledAssetsExceptLanguages is currently unsupported."
+ "radioItemProcessor"
+ "rebuildWithError:"
+ "remainingBudget"
+ "removeItemAtPath:error:"
+ "removeObjectsForKeys:"
+ "sanitizeText:detector:"
+ "setNumEntitiesPerCategory:"
+ "setProfileConfigWithLanguage:profileDir:personaId:dataProtectionClass:isInUserVault:completion:"
+ "sharedItemIdentifier"
+ "shouldSampleRequest"
+ "speechProfilePathsForLanguage:"
+ "standardUserDefaults"
+ "stringByAppendingPathExtension:"
+ "stringIdentifiersApplyingFilters:error:"
+ "structuredEntryWithOrthography:componentKey:"
+ "structuredRadioWordsFromRadioWords:"
+ "subscribeToAssetWithConfig:subscriberId:expiration:error:"
+ "subtitle"
+ "systemClientId"
+ "totalContactComponentsInSet:"
+ "unlock"
+ "updateDatabaseWithEuclidProfileUpdates:completion:"
+ "userProfileWithAssetConfig:assetManager:modelOverridePath:overrides:isJit:returningFoundPath:error:"
+ "v20@?0B8@\"NSError\"12"
+ "v24@?0@8@\"NSError\"16"
+ "v24@?0q8@\"NSError\"16"
+ "v32@?0@\"NSString\"8@\"CESREuclidProfileInsertion\"16^B24"
+ "v44@0:8@16S24@28@36"
+ "vocabularyLabelForFieldType:directDonationConfig:"
+ "writeToJSONFile:removeCategories:error:"
+ "writeUserData:toJSONFile:removeCategories:error:"
- "\n&"
- "%s %@: %@"
- "%s Cached recognizer is for language: %{public}@, regionId: %{private}@, but this request specifies a different regionId: %{private}@. Discarding the cached recognizer upon cooldown."
- "%s Enrolled %ld extracted entities."
- "%s Enrolled %tu items for (%@, %@)."
- "%s Entity Cleanup: Apply Regex %@ enabled"
- "%s Entity Cleanup: Cleanup %@ enabled."
- "%s Entity Cleanup: Cleanup Ingestion %@ enabled."
- "%s Entity Cleanup: Emoji Removal %@ enabled for AppEntities"
- "%s Entity Cleanup: Emoji Removal %@ enabled for Non-AppEntities"
- "%s Entity Cleanup: Failed applying regex: %@"
- "%s Entity Cleanup: Failed to initialize NSDataDetector for NSTextCheckingTypes-based entity sanitization, skipping enrolling entities of impacted types."
- "%s Entity Cleanup: Special Character Removal %@ enabled for AppEntities"
- "%s Entity Cleanup: Special Character Removal %@ enabled for Non-AppEntities"
- "%s Entity Extraction: Entity Extraction Limit is %ld"
- "%s Entity Extraction: Extracted entity equals original string. Skipping."
- "%s Entity Extraction: Extraction %@ enabled."
- "%s Entity Extraction: Extraction Ingestion %@ enabled."
- "%s Entity Extraction: No mapping found for extracted entity with tagName %@. Skipping."
- "%s Entity Extraction: No mapping found for extracted entity with tagName: %@. Using default mapping."
- "%s Error enumerating CCItemFields: %@"
- "%s Error replacing the cached recognizer: %@"
- "%s Existing profile found at %@"
- "%s GeoLM: Exception thrown while reading geo-config json"
- "%s GeoLM: Exception thrown while reading json configs"
- "%s GeoLM: For the given location, selected regionId=%@"
- "%s GeoLM: _EARGeoLMHelper not initialized"
- "%s GeoLM: geoLM region specific [%{private}@] asset exists on device, but not compatible."
- "%s GeoLM: location is nil."
- "%s GeoLM: model-info.version doesn't match. mainASRModelInfo.version=%@ geoLMModelInfo.version=%@ mainAssetConfig=%@ geoAssetConfig=%@"
- "%s GeoLM: region mapping json file is nil Or there is no regionMapping for given language=%@"
- "%s GeoLM: region mapping json file=%@"
- "%s GeoLM: region specific [%{private}@] geo-config json file=%{public}@"
- "%s GeoLM: region specific asset is not found for given language=%{public}@ regionId=%{private}@"
- "%s No installed %@ asset for language: %@"
- "%s On-Device ASR: Replacing the cached recognizer for language: %{public}@, regionId: %{private}@ to account for the pending regionId: %{private}@"
- "%s Processed %ld App Entities, enrolled %ld."
- "%s Processed %tu radio entities."
- "%s Processed first party contacts: %tu (accepted=%tu)"
- "%s Processed group names: %tu (accepted=%tu)"
- "%s Processed third party contacts: %tu (accepted=%tu)"
- "%s Processing %tu items for speech categories: %@."
- "%s Siri/asr_speech_profile_app_entities feature flag disabled, App Entities will not be consumed."
- "%s Siri/asr_speech_profile_app_entities feature flag enabled, App Entities will be consumed."
- "%s Trial asset delivery is explicitly disabled!"
- "%s Using model from %@ asset for %@ at path: %@"
- "+[ESConnection _replaceCachedRecognizerIfNeeded]"
- "+[ESSpeechProfileBuilderConnection userProfileWithAssetConfig:modelOverridePath:overrides:isJit:returningFoundPath:error:]"
- "+[ESUserData _applyContactLimitsToFirstPartyContacts:thirdPartyContacts:groupNames:]"
- "+[ESUserData _fetchExtractedEntityMappingsForEntities:extractionVocabLabels:originalInputString:]"
- "-[ESAssetManager _geoLMCompatibleWithMainAsset:geoAssetConfig:]"
- "-[ESAssetManager _installedGeoLMRegionMappingForLanguage:]"
- "-[ESAssetManager geoLMRegionIdForLocation:]"
- "-[ESAssetManager installedGeoLMRegionSpecificAssetForLanguage:regionId:mainAssetConfig:]"
- "-[ESAssetManager isTrialAssetDeliveryEnabled]"
- "-[ESUserData _applyEntityCleanup:enableEmojiCleanup:enableSpecialCharacterCleanup:customRegex:]"
- "-[ESUserData _performEntityExtractionAndAddToVocabWords:vocabularyWords:extractionVocabLabels:]_block_invoke"
- "-[ESUserData _populateUserDataFromItems:applicableSpeechCategories:]_block_invoke"
- "-[ESUserData _processContactItem:contactWords:vocabularyWords:]"
- "-[ESUserData _processRadioItem:radioWords:]"
- "-[ESUserData _processVocabularyItem:vocabularyWords:]"
- "-[ESUserData _textDatatypeDetector]"
- "-[ESUserData logEntityCleanupConfig]"
- "-[ESUserData logEntityExtractionConfig]"
- "@\"_EAREntityTagger\""
- "@40@0:8@16B24B28@32"
- "B40@0:8@16Q24^@32"
- "Failed to load speech assets"
- "Failed to read the existing speech profile"
- "IS"
- "IS NOT"
- "Speech category %@ has already been committed with a call to Begin followed by Finish"
- "Speech category %@ is unsupported"
- "Vv68@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40q48B56@?<v@?B@\"NSError\">60"
- "Vv68@0:8@16@24@32@40q48B56@?60"
- "_addVocabWord:vocabularyLabel:toVocabularyWords:"
- "_applyContactLimitsToFirstPartyContacts:thirdPartyContacts:groupNames:"
- "_applyEntityCleanup:enableEmojiCleanup:enableSpecialCharacterCleanup:customRegex:"
- "_applyEntityCleanupToNonAppEntity:"
- "_entityTagger"
- "_extractedLabelForLabel:"
- "_fetchAppEntityMappingForBundleId:appEntityConfig:assistantSchemas:entityType:"
- "_fetchExtractedEntityMappingsForEntities:extractionVocabLabels:originalInputString:"
- "_geoLMCompatibleWithMainAsset:geoAssetConfig:"
- "_installedGeoLMRegionMappingForLanguage:"
- "_isEntityInExclusionList:bundleId:type:"
- "_limitVocabularyWords:toApplicableSpeechCategories:"
- "_normalize:"
- "_performEntityExtractionAndAddToVocabWords:vocabularyWords:extractionVocabLabels:"
- "_processAppEntity:vocabularyWords:"
- "_processContactItem:contactWords:vocabularyWords:"
- "_processRadioItem:radioWords:"
- "_processSingleVocabItem:fieldContent:vocabularyLabel:vocabularyWords:"
- "_processVocabularyItem:vocabularyWords:"
- "_sanitizeTextForDatatypes:detector:"
- "_textDatatypeDetector"
- "_totalContactComponentsInSet:"
- "_userId"
- "_vocabularyLabelsForFieldType:directDonationConfig:"
- "applyRegex:toString:"
- "arrayWithCapacity:"
- "assistantDefinedSchemas"
- "com.apple.internal.ck"
- "coordinate"
- "disableTrialAssetDelivery"
- "enableTrialAssetDelivery"
- "entitiesExcludedFromEmojiCleanup"
- "entitiesExcludedFromSpecialCharacterCleanup"
- "entityContent"
- "extractionVocabLabels"
- "geoLMRegionIdForLocation:"
- "geoLMRegionIdWithLanguage:location:"
- "geoLmInitialized"
- "initWithSuiteName:"
- "initializeGeoLMWithLanguage:"
- "installedAssetWithConfig:regionId:shouldSubscribe:subscriberId:expiration:"
- "installedGeoLMRegionSpecificAssetForLanguage:regionId:mainAssetConfig:"
- "installedQuasarModelPathForAssetConfig:error:triggerDownload:"
- "installedQuasarModelPathForAssetConfig:error:triggerDownload:ignoreSpellingModel:"
- "isRequestSelectedForSamplingFromConfigForLanguage:"
- "isSiriXEnabled"
- "isTrialAssetDeliveryEnabled"
- "lastUsedGeoLMRegionIdForLanguage:"
- "logEntityCleanupConfig"
- "logEntityExtractionConfig"
- "mainBundle"
- "precomposedStringWithCanonicalMapping"
- "primaryVocabLabel"
- "profileFilePathFromBasePath:language:userId:"
- "purgeUnusedGeoLMAssetsForLanguage:"
- "purgeUnusedGeoLMRegionIdFromCacheForLanguage:"
- "purgeUserDefaultsGeoLMAssetsInfoDictForLanguages:"
- "regionIdForLatitude:longitude:"
- "removeDuplicateWhitespace:"
- "removeEmojis:"
- "removeSpecialCharacters:fromString:"
- "setProfileConfigWithLanguage:profileDir:userId:personaId:dataProtectionClass:isInUserVault:completion:"
- "setUserId:"
- "sharedManager"
- "specialCharactersToRemove"
- "speechProfilePathsWithLanguage:"
- "subscribeToAssetWithConfig:regionId:subscriberId:expiration:"
- "subscriberIdForDictationAssets"
- "tagEntitiesWithTagNamesIn:"
- "tagName"
- "unsubscribeFromAssetWithConfig:regionId:subscriberId:"
- "updateGeoLMAssetsInfoDictWithRegionId:language:"
- "userProfileWithAssetConfig:modelOverridePath:overrides:isJit:returningFoundPath:error:"
- "v44@0:8S16@20@28@36"
- "\u00a0"

```
