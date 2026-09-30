## CoreEmbeddedSpeechRecognition

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition`

```diff

   __AUTH.__data: 0x770
   __DATA.__objc_ivar: 0x554
   __DATA.__data: 0x1930
-  __DATA.__bss: 0xd78
+  __DATA.__bss: 0xd88
   __DATA.__common: 0x88
   __DATA_DIRTY.__objc_data: 0xed0
   __DATA_DIRTY.__data: 0xce0
-  __DATA_DIRTY.__bss: 0x7a8
+  __DATA_DIRTY.__bss: 0x798
   __DATA_DIRTY.__common: 0x1a
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 92E0228E-F699-3E8A-A4BC-18234C0BBA69
+  UUID: 3B39245F-0AFC-3A52-8E25-A92DEACC8193
   Functions: 5156
   Symbols:   6165
   CStrings:  4783
Symbols:
+ ___103-[CoreEmbeddedSpeechRecognizer preheatSpeechRecognitionWithAssetConfig:preheatSource:modelOverrideURL:]_block_invoke.357
+ ___120-[CESRSpeechProfileBuilder _setProfileConfigWithLanguage:profileDir:userId:personaId:dataProtectionClass:isInUserVault:]_block_invoke.392
+ ___43-[CoreEmbeddedSpeechRecognizer _connection]_block_invoke.353
+ ___48-[CESRSpeechProfileBuilder addCodepathId:error:]_block_invoke.396
+ ___49-[CESRSpeechProfileBuilder _flushItemsWithError:]_block_invoke.407
+ ___50-[CESRSpeechProfileSiteManager handleNewPersonas:]_block_invoke.326
+ ___51+[CoreEmbeddedSpeechRecognizer forceCooldownIfIdle]_block_invoke.370
+ ___51-[CESRSpeechProfileBuilder removeCodepathId:error:]_block_invoke.397
+ ___52-[CESRSpeechProfileBuilder getCodepathIdsWithError:]_block_invoke.399
+ ___54-[CESRSpeechProfileBuilder cancelCategoriesWithError:]_block_invoke.408
+ ___55-[CESRSpeechProfileBuilder finishAndSaveProfile:error:]_block_invoke.409
+ ___56-[CESRSpeechProfileBuilder getVersionForCategory:error:]_block_invoke.394
+ ___58+[CoreEmbeddedSpeechRecognizer cleanupUnusedSubscriptions]_block_invoke.361
+ ___58-[CESRSpeechProfileSiteWriter logRequiredProfileInstances]_block_invoke.299
+ ___62+[CoreEmbeddedSpeechRecognizer handlePostInstallSubscriptions]_block_invoke.359
+ ___62-[CESRSpeechProfileSiteManager handleSiteAvailableForPersona:]_block_invoke.325
+ ___65-[CoreEmbeddedSpeechRecognizer removePersonalizedLMForFidesOnly:]_block_invoke.435
+ ___68+[CoreEmbeddedSpeechRecognizer compileAllAssetsWithType:completion:]_block_invoke.365
+ ___69-[CESRSpeechProfileDispatcher handleDarwinNotificationEventWithName:]_block_invoke.365
+ ___69-[CESRSpeechProfileSiteManager _registerTrialExperimentUpdateHandler]_block_invoke.314
+ ___70-[CESRSpeechProfileSiteWriter addBookmarksForLocale:toChangeRegistry:]_block_invoke.305
+ ___73+[CESRUtilities AFSpeechInfoPackageForEARSpeechRecognitionResultPackage:]_block_invoke.361
+ ___74-[CESRSpeechProfileBuilder beginWithCategoriesAndVersions:bundleId:error:]_block_invoke.401
+ ___75+[CoreEmbeddedSpeechRecognizer compilePrimaryAssistantAssetWithCompletion:]_block_invoke.369
+ ___78-[CoreEmbeddedSpeechRecognizer deleteAllDESRecordsForDictationPersonalization]_block_invoke.409
+ ___83-[CESRSpeechProfileSiteWriter _updateRequiredProfileInstancesWithSets:shouldDefer:]_block_invoke.320
+ ___86-[CoreEmbeddedSpeechRecognizer preheatSpeechRecognitionWithLanguage:modelOverrideURL:]_block_invoke.355
+ ___93-[CoreEmbeddedSpeechRecognizer startSpeechRecognitionWithParameters:didStartHandlerWithInfo:]_block_invoke.383
+ ___93-[CoreEmbeddedSpeechRecognizer startSpeechRecognitionWithParameters:didStartHandlerWithInfo:]_block_invoke.384
+ ___Block_byref_object_copy_.1059
+ ___Block_byref_object_copy_.1434
+ ___Block_byref_object_copy_.2168
+ ___Block_byref_object_copy_.2902
+ ___Block_byref_object_copy_.3388
+ ___Block_byref_object_copy_.390
+ ___Block_byref_object_copy_.456
+ ___Block_byref_object_copy_.946
+ ___Block_byref_object_dispose_.1060
+ ___Block_byref_object_dispose_.1435
+ ___Block_byref_object_dispose_.2169
+ ___Block_byref_object_dispose_.2903
+ ___Block_byref_object_dispose_.3389
+ ___Block_byref_object_dispose_.391
+ ___Block_byref_object_dispose_.457
+ ___Block_byref_object_dispose_.947
+ ___block_literal_global.1470
+ ___block_literal_global.2152
+ ___block_literal_global.2263
+ ___block_literal_global.2967
+ ___block_literal_global.323
+ ___block_literal_global.3425
+ ___block_literal_global.345
+ ___block_literal_global.355
+ ___block_literal_global.357
+ ___block_literal_global.365.756
+ ___block_literal_global.368
+ ___block_literal_global.370
+ ___block_literal_global.372
+ ___block_literal_global.374
+ ___block_literal_global.376
+ ___block_literal_global.3785
+ ___block_literal_global.383
+ ___block_literal_global.391
+ ___block_literal_global.393
+ ___block_literal_global.408
+ ___block_literal_global.411
+ ___block_literal_global.4271
+ ___block_literal_global.432
+ ___block_literal_global.434
+ ___block_literal_global.437
+ ___block_literal_global.439
+ ___block_literal_global.4541
+ ___block_literal_global.732
+ ___block_literal_global.745
+ _sharedManager.onceToken.2966
+ _sharedManager.onceToken.731
+ _sharedManager.sharedMyManager.2968
+ _sharedManager.sharedMyManager.733
- ___103-[CoreEmbeddedSpeechRecognizer preheatSpeechRecognitionWithAssetConfig:preheatSource:modelOverrideURL:]_block_invoke.348
- ___120-[CESRSpeechProfileBuilder _setProfileConfigWithLanguage:profileDir:userId:personaId:dataProtectionClass:isInUserVault:]_block_invoke.383
- ___43-[CoreEmbeddedSpeechRecognizer _connection]_block_invoke.344
- ___48-[CESRSpeechProfileBuilder addCodepathId:error:]_block_invoke.387
- ___49-[CESRSpeechProfileBuilder _flushItemsWithError:]_block_invoke.398
- ___50-[CESRSpeechProfileSiteManager handleNewPersonas:]_block_invoke.317
- ___51+[CoreEmbeddedSpeechRecognizer forceCooldownIfIdle]_block_invoke.361
- ___51-[CESRSpeechProfileBuilder removeCodepathId:error:]_block_invoke.388
- ___52-[CESRSpeechProfileBuilder getCodepathIdsWithError:]_block_invoke.390
- ___54-[CESRSpeechProfileBuilder cancelCategoriesWithError:]_block_invoke.399
- ___55-[CESRSpeechProfileBuilder finishAndSaveProfile:error:]_block_invoke.400
- ___56-[CESRSpeechProfileBuilder getVersionForCategory:error:]_block_invoke.385
- ___58+[CoreEmbeddedSpeechRecognizer cleanupUnusedSubscriptions]_block_invoke.352
- ___58-[CESRSpeechProfileSiteWriter logRequiredProfileInstances]_block_invoke.290
- ___62+[CoreEmbeddedSpeechRecognizer handlePostInstallSubscriptions]_block_invoke.350
- ___62-[CESRSpeechProfileSiteManager handleSiteAvailableForPersona:]_block_invoke.316
- ___65-[CoreEmbeddedSpeechRecognizer removePersonalizedLMForFidesOnly:]_block_invoke.426
- ___68+[CoreEmbeddedSpeechRecognizer compileAllAssetsWithType:completion:]_block_invoke.356
- ___69-[CESRSpeechProfileDispatcher handleDarwinNotificationEventWithName:]_block_invoke.356
- ___69-[CESRSpeechProfileSiteManager _registerTrialExperimentUpdateHandler]_block_invoke.305
- ___70-[CESRSpeechProfileSiteWriter addBookmarksForLocale:toChangeRegistry:]_block_invoke.296
- ___73+[CESRUtilities AFSpeechInfoPackageForEARSpeechRecognitionResultPackage:]_block_invoke.352
- ___74-[CESRSpeechProfileBuilder beginWithCategoriesAndVersions:bundleId:error:]_block_invoke.392
- ___75+[CoreEmbeddedSpeechRecognizer compilePrimaryAssistantAssetWithCompletion:]_block_invoke.360
- ___78-[CoreEmbeddedSpeechRecognizer deleteAllDESRecordsForDictationPersonalization]_block_invoke.400
- ___83-[CESRSpeechProfileSiteWriter _updateRequiredProfileInstancesWithSets:shouldDefer:]_block_invoke.311
- ___86-[CoreEmbeddedSpeechRecognizer preheatSpeechRecognitionWithLanguage:modelOverrideURL:]_block_invoke.346
- ___93-[CoreEmbeddedSpeechRecognizer startSpeechRecognitionWithParameters:didStartHandlerWithInfo:]_block_invoke.374
- ___93-[CoreEmbeddedSpeechRecognizer startSpeechRecognitionWithParameters:didStartHandlerWithInfo:]_block_invoke.375
- ___Block_byref_object_copy_.1057
- ___Block_byref_object_copy_.1430
- ___Block_byref_object_copy_.2166
- ___Block_byref_object_copy_.2879
- ___Block_byref_object_copy_.3369
- ___Block_byref_object_copy_.388
- ___Block_byref_object_copy_.454
- ___Block_byref_object_copy_.941
- ___Block_byref_object_dispose_.1058
- ___Block_byref_object_dispose_.1431
- ___Block_byref_object_dispose_.2167
- ___Block_byref_object_dispose_.2880
- ___Block_byref_object_dispose_.3370
- ___Block_byref_object_dispose_.389
- ___Block_byref_object_dispose_.455
- ___Block_byref_object_dispose_.942
- ___block_literal_global.1466
- ___block_literal_global.2150
- ___block_literal_global.2261
- ___block_literal_global.2945
- ___block_literal_global.305
- ___block_literal_global.327
- ___block_literal_global.338
- ___block_literal_global.3406
- ___block_literal_global.341
- ___block_literal_global.343
- ___block_literal_global.346
- ___block_literal_global.348
- ___block_literal_global.363
- ___block_literal_global.367
- ___block_literal_global.369
- ___block_literal_global.373
- ___block_literal_global.3767
- ___block_literal_global.381
- ___block_literal_global.384
- ___block_literal_global.399
- ___block_literal_global.402
- ___block_literal_global.423
- ___block_literal_global.425
- ___block_literal_global.4269
- ___block_literal_global.428
- ___block_literal_global.430
- ___block_literal_global.4548
- ___block_literal_global.730
- ___block_literal_global.741
- _sharedManager.onceToken.2944
- _sharedManager.onceToken.729
- _sharedManager.sharedMyManager.2946
- _sharedManager.sharedMyManager.731

```
