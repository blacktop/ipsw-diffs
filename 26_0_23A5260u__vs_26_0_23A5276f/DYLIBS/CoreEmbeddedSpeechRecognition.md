## CoreEmbeddedSpeechRecognition

> `/System/Library/PrivateFrameworks/CoreEmbeddedSpeechRecognition.framework/CoreEmbeddedSpeechRecognition`

```diff

-3500.97.2.1.1
-  __TEXT.__text: 0x17e7c0
-  __TEXT.__auth_stubs: 0x2d80
-  __TEXT.__objc_methlist: 0x3fc0
+3500.104.2.0.0
+  __TEXT.__text: 0x17e874
+  __TEXT.__auth_stubs: 0x2d70
+  __TEXT.__objc_methlist: 0x3fe0
   __TEXT.__const: 0x1600
-  __TEXT.__cstring: 0xab52
+  __TEXT.__cstring: 0xab7b
   __TEXT.__swift5_typeref: 0x1c76
   __TEXT.__swift5_capture: 0x4680
   __TEXT.__constg_swiftt: 0xa74

   __TEXT.__swift5_assocty: 0x150
   __TEXT.__swift5_proto: 0xa0
   __TEXT.__swift5_types: 0xa0
-  __TEXT.__oslogstring: 0x7cb2
+  __TEXT.__oslogstring: 0x7d71
   __TEXT.__swift_as_entry: 0x160
   __TEXT.__swift_as_ret: 0x1c0
-  __TEXT.__gcc_except_tab: 0xb6c
-  __TEXT.__unwind_info: 0x2278
+  __TEXT.__gcc_except_tab: 0xb58
+  __TEXT.__unwind_info: 0x2268
   __TEXT.__eh_frame: 0x2360
   __TEXT.__objc_classname: 0xa0f
-  __TEXT.__objc_methname: 0xd523
-  __TEXT.__objc_methtype: 0x2c81
-  __TEXT.__objc_stubs: 0x71a0
-  __DATA_CONST.__got: 0xf40
-  __DATA_CONST.__const: 0x1460
+  __TEXT.__objc_methname: 0xd573
+  __TEXT.__objc_methtype: 0x2c76
+  __TEXT.__objc_stubs: 0x72a0
+  __DATA_CONST.__got: 0xf48
+  __DATA_CONST.__const: 0x1418
   __DATA_CONST.__objc_classlist: 0x2b0
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c38
+  __DATA_CONST.__objc_selrefs: 0x2c58
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x1f0
   __DATA_CONST.__objc_arraydata: 0x190
-  __AUTH_CONST.__auth_got: 0x16d8
+  __AUTH_CONST.__auth_got: 0x16d0
   __AUTH_CONST.__const: 0xbc88
-  __AUTH_CONST.__cfstring: 0x4840
+  __AUTH_CONST.__cfstring: 0x4860
   __AUTH_CONST.__objc_const: 0x8110
   __AUTH_CONST.__objc_intobj: 0x630
   __AUTH_CONST.__objc_arrayobj: 0x1e0

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EED48856-17E5-36E4-8207-73456D66904D
-  Functions: 4561
-  Symbols:   5783
-  CStrings:  4542
+  UUID: 17F6997A-679E-32B9-9012-FD9A60445BF3
+  Functions: 4558
+  Symbols:   5781
+  CStrings:  4550
 
Symbols:
+ +[CESRSpeechProfileSettings _isAssistantRequired]
+ +[CESRSpeechProfileSettings _isDictationRequired]
+ +[CESRSpeechProfileSettings _requiredAssistantLocale]
+ +[CESRSpeechProfileSettings _requiredDictationLocales]
+ +[CESRUtilities installedDictationLocaleIdentifiers]
+ +[CESRUtilities isAutomaticCompilationEnabled]
+ -[CESRSpeechProfileSettings _initWithAssistantLocale:dictationLocales:]
+ -[CESRSpeechProfileSettings updateRequiredLocales]
+ -[CESRSpeechProfileSiteManager updateRequiredLocales]
+ GCC_except_table136
+ GCC_except_table157
+ GCC_except_table170
+ GCC_except_table242
+ GCC_except_table258
+ GCC_except_table261
+ GCC_except_table307
+ GCC_except_table328
+ GCC_except_table478
+ GCC_except_table483
+ GCC_except_table486
+ GCC_except_table490
+ GCC_except_table493
+ GCC_except_table496
+ GCC_except_table499
+ GCC_except_table502
+ GCC_except_table505
+ GCC_except_table508
+ GCC_except_table629
+ _OBJC_CLASS_$_SFSpeechAssetManager
+ ___103-[CoreEmbeddedSpeechRecognizer preheatSpeechRecognitionWithAssetConfig:preheatSource:modelOverrideURL:]_block_invoke.348
+ ___120-[CESRSpeechProfileBuilder _setProfileConfigWithLanguage:profileDir:userId:personaId:dataProtectionClass:isInUserVault:]_block_invoke.383
+ ___43-[CoreEmbeddedSpeechRecognizer _connection]_block_invoke.344
+ ___48-[CESRSpeechProfileBuilder addCodepathId:error:]_block_invoke.387
+ ___49-[CESRSpeechProfileBuilder _flushItemsWithError:]_block_invoke.398
+ ___51+[CoreEmbeddedSpeechRecognizer forceCooldownIfIdle]_block_invoke.361
+ ___51-[CESRSpeechProfileBuilder removeCodepathId:error:]_block_invoke.388
+ ___52-[CESRSpeechProfileBuilder getCodepathIdsWithError:]_block_invoke.390
+ ___53-[CESRSpeechProfileSiteManager updateRequiredLocales]_block_invoke
+ ___54-[CESRSpeechProfileBuilder cancelCategoriesWithError:]_block_invoke.399
+ ___55-[CESRSpeechProfileBuilder finishAndSaveProfile:error:]_block_invoke.400
+ ___56-[CESRSpeechProfileBuilder getVersionForCategory:error:]_block_invoke.385
+ ___58+[CoreEmbeddedSpeechRecognizer cleanupUnusedSubscriptions]_block_invoke.352
+ ___58-[CESRSpeechProfileSiteWriter logRequiredProfileInstances]_block_invoke.290
+ ___62+[CoreEmbeddedSpeechRecognizer handlePostUpgradeSubscriptions]_block_invoke.350
+ ___62-[CESRSpeechProfileSiteManager handleSiteAvailableForPersona:]_block_invoke.314
+ ___65-[CoreEmbeddedSpeechRecognizer removePersonalizedLMForFidesOnly:]_block_invoke.426
+ ___68+[CoreEmbeddedSpeechRecognizer compileAllAssetsWithType:completion:]_block_invoke.356
+ ___69-[CESRSpeechProfileSiteManager _registerTrialExperimentUpdateHandler]_block_invoke.305
+ ___73+[CESRUtilities AFSpeechInfoPackageForEARSpeechRecognitionResultPackage:]_block_invoke.352
+ ___74-[CESRSpeechProfileBuilder beginWithCategoriesAndVersions:bundleId:error:]_block_invoke.392
+ ___75+[CoreEmbeddedSpeechRecognizer compilePrimaryAssistantAssetWithCompletion:]_block_invoke.360
+ ___78-[CoreEmbeddedSpeechRecognizer deleteAllDESRecordsForDictationPersonalization]_block_invoke.400
+ ___83-[CESRSpeechProfileSiteWriter _updateRequiredProfileInstancesWithSets:shouldDefer:]_block_invoke.310
+ ___86-[CoreEmbeddedSpeechRecognizer preheatSpeechRecognitionWithLanguage:modelOverrideURL:]_block_invoke.346
+ ___93-[CoreEmbeddedSpeechRecognizer startSpeechRecognitionWithParameters:didStartHandlerWithInfo:]_block_invoke.374
+ ___93-[CoreEmbeddedSpeechRecognizer startSpeechRecognitionWithParameters:didStartHandlerWithInfo:]_block_invoke.375
+ ___Block_byref_object_copy_.1341
+ ___Block_byref_object_copy_.2069
+ ___Block_byref_object_copy_.2771
+ ___Block_byref_object_copy_.4194
+ ___Block_byref_object_copy_.473
+ ___Block_byref_object_copy_.866
+ ___Block_byref_object_copy_.977
+ ___Block_byref_object_dispose_.1342
+ ___Block_byref_object_dispose_.2070
+ ___Block_byref_object_dispose_.2772
+ ___Block_byref_object_dispose_.4195
+ ___Block_byref_object_dispose_.474
+ ___Block_byref_object_dispose_.867
+ ___Block_byref_object_dispose_.978
+ ___block_literal_global.1887
+ ___block_literal_global.2053
+ ___block_literal_global.2165
+ ___block_literal_global.2836
+ ___block_literal_global.314
+ ___block_literal_global.323
+ ___block_literal_global.328
+ ___block_literal_global.334
+ ___block_literal_global.343
+ ___block_literal_global.345
+ ___block_literal_global.3477
+ ___block_literal_global.351
+ ___block_literal_global.382
+ ___block_literal_global.384
+ ___block_literal_global.3963
+ ___block_literal_global.402
+ ___block_literal_global.402.4190
+ ___block_literal_global.423
+ ___block_literal_global.4239
+ ___block_literal_global.428
+ ___block_literal_global.430
+ ___block_literal_global.670
+ ___block_literal_global.681
+ _objc_msgSend$_initWithAssistantLocale:dictationLocales:
+ _objc_msgSend$_requiredAssistantLocale
+ _objc_msgSend$_requiredDictationLocales
+ _objc_msgSend$assetType
+ _objc_msgSend$boolForKey:
+ _objc_msgSend$installedDictationLocaleIdentifiers
+ _objc_msgSend$isAutomaticCompilationEnabled
+ _objc_msgSend$isEqualToSet:
+ _objc_msgSend$sortUsingSelector:
+ _objc_msgSend$subscriptionsForSubscriberId:
+ _objc_msgSend$systemClientId
+ _objc_msgSend$updateRequiredLocales
+ _sharedManager.onceToken.2835
+ _sharedManager.onceToken.669
+ _sharedManager.sharedMyManager.2837
+ _sharedManager.sharedMyManager.671
- +[CESRUtilities currentDictationLanguageCodes]
- -[CESRSpeechProfileSettings _isAssistantRequired]
- -[CESRSpeechProfileSettings _isDictationRequired]
- -[CESRSpeechProfileSettings initWithAssistantLocale:dictationLocales:]
- -[CESRSpeechProfileSettings refreshRequiredLocales:]
- -[CESRSpeechProfileSiteManager handleAssetUpdate]
- -[CESRSpeechProfileSiteManager handleSettingsChange]
- GCC_except_table134
- GCC_except_table155
- GCC_except_table168
- GCC_except_table240
- GCC_except_table256
- GCC_except_table259
- GCC_except_table305
- GCC_except_table326
- GCC_except_table349
- GCC_except_table476
- GCC_except_table481
- GCC_except_table484
- GCC_except_table488
- GCC_except_table491
- GCC_except_table494
- GCC_except_table497
- GCC_except_table500
- GCC_except_table503
- GCC_except_table506
- GCC_except_table627
- _AFOfflineDictationStatusStringIsInstalled
- ___103-[CoreEmbeddedSpeechRecognizer preheatSpeechRecognitionWithAssetConfig:preheatSource:modelOverrideURL:]_block_invoke.345
- ___120-[CESRSpeechProfileBuilder _setProfileConfigWithLanguage:profileDir:userId:personaId:dataProtectionClass:isInUserVault:]_block_invoke.380
- ___43-[CoreEmbeddedSpeechRecognizer _connection]_block_invoke.341
- ___46+[CESRUtilities currentDictationLanguageCodes]_block_invoke
- ___48-[CESRSpeechProfileBuilder addCodepathId:error:]_block_invoke.384
- ___49-[CESRSpeechProfileBuilder _flushItemsWithError:]_block_invoke.395
- ___49-[CESRSpeechProfileSiteManager handleAssetUpdate]_block_invoke
- ___51+[CoreEmbeddedSpeechRecognizer forceCooldownIfIdle]_block_invoke.358
- ___51-[CESRSpeechProfileBuilder removeCodepathId:error:]_block_invoke.385
- ___52-[CESRSpeechProfileBuilder getCodepathIdsWithError:]_block_invoke.387
- ___52-[CESRSpeechProfileSiteManager handleSettingsChange]_block_invoke
- ___54-[CESRSpeechProfileBuilder cancelCategoriesWithError:]_block_invoke.396
- ___55-[CESRSpeechProfileBuilder finishAndSaveProfile:error:]_block_invoke.397
- ___56-[CESRSpeechProfileBuilder getVersionForCategory:error:]_block_invoke.382
- ___58+[CoreEmbeddedSpeechRecognizer cleanupUnusedSubscriptions]_block_invoke.349
- ___58-[CESRSpeechProfileSiteWriter logRequiredProfileInstances]_block_invoke.287
- ___62+[CoreEmbeddedSpeechRecognizer handlePostUpgradeSubscriptions]_block_invoke.347
- ___62-[CESRSpeechProfileSiteManager handleSiteAvailableForPersona:]_block_invoke.311
- ___65-[CoreEmbeddedSpeechRecognizer removePersonalizedLMForFidesOnly:]_block_invoke.423
- ___68+[CoreEmbeddedSpeechRecognizer compileAllAssetsWithType:completion:]_block_invoke.353
- ___69-[CESRSpeechProfileSiteManager _registerTrialExperimentUpdateHandler]_block_invoke.302
- ___73+[CESRUtilities AFSpeechInfoPackageForEARSpeechRecognitionResultPackage:]_block_invoke.345
- ___74-[CESRSpeechProfileBuilder beginWithCategoriesAndVersions:bundleId:error:]_block_invoke.389
- ___75+[CoreEmbeddedSpeechRecognizer compilePrimaryAssistantAssetWithCompletion:]_block_invoke.357
- ___78-[CoreEmbeddedSpeechRecognizer deleteAllDESRecordsForDictationPersonalization]_block_invoke.397
- ___83-[CESRSpeechProfileSiteWriter _updateRequiredProfileInstancesWithSets:shouldDefer:]_block_invoke.307
- ___86-[CoreEmbeddedSpeechRecognizer preheatSpeechRecognitionWithLanguage:modelOverrideURL:]_block_invoke.343
- ___93-[CoreEmbeddedSpeechRecognizer startSpeechRecognitionWithParameters:didStartHandlerWithInfo:]_block_invoke.371
- ___93-[CoreEmbeddedSpeechRecognizer startSpeechRecognitionWithParameters:didStartHandlerWithInfo:]_block_invoke.372
- ___Block_byref_object_copy_.1340
- ___Block_byref_object_copy_.2059
- ___Block_byref_object_copy_.2756
- ___Block_byref_object_copy_.4177
- ___Block_byref_object_copy_.470
- ___Block_byref_object_copy_.862
- ___Block_byref_object_copy_.976
- ___Block_byref_object_dispose_.1341
- ___Block_byref_object_dispose_.2060
- ___Block_byref_object_dispose_.2757
- ___Block_byref_object_dispose_.4178
- ___Block_byref_object_dispose_.471
- ___Block_byref_object_dispose_.863
- ___Block_byref_object_dispose_.977
- ___block_descriptor_40_e8_32r_e35_v32?0"NSString"8"NSString"16^B24lr32l8
- ___block_literal_global.1877
- ___block_literal_global.2043
- ___block_literal_global.2155
- ___block_literal_global.2823
- ___block_literal_global.311
- ___block_literal_global.320
- ___block_literal_global.322
- ___block_literal_global.327
- ___block_literal_global.333
- ___block_literal_global.335
- ___block_literal_global.3464
- ___block_literal_global.347
- ___block_literal_global.375
- ___block_literal_global.381
- ___block_literal_global.3948
- ___block_literal_global.396
- ___block_literal_global.399.4173
- ___block_literal_global.420
- ___block_literal_global.4217
- ___block_literal_global.422
- ___block_literal_global.427
- ___block_literal_global.667
- ___block_literal_global.678
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_CoreEmbeddedSpeechRecognition
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_CoreEmbeddedSpeechRecognition
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_CoreEmbeddedSpeechRecognition
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_CoreEmbeddedSpeechRecognition
- _objc_msgSend$currentDictationLanguageCodes
- _objc_msgSend$initWithAssistantLocale:dictationLocales:
- _objc_msgSend$installationStatusForLanguagesWithAssetType:
- _objc_msgSend$refreshRequiredLocales:
- _sharedManager.onceToken.2822
- _sharedManager.onceToken.666
- _sharedManager.sharedMyManager.2824
- _sharedManager.sharedMyManager.668
CStrings:
+ "%s Automatic model compilation is disabled."
+ "%s Failed to resolve locale from localeIdentifier: %@"
+ "%s Required locales for Dictation have changed, previous: %@, current: %@"
+ "%s The required locale for Assistant has changed, previous: %@, current: %@"
+ "%s Updating required locales..."
+ "+[CESRSpeechProfileSettings _isAssistantRequired]"
+ "+[CESRSpeechProfileSettings _isDictationRequired]"
+ "+[CESRUtilities isAutomaticCompilationEnabled]"
+ "-[CESRSpeechProfileSettings updateRequiredLocales]"
+ "ASRAutomaticCompilationOverride"
+ "_initWithAssistantLocale:dictationLocales:"
+ "_requiredAssistantLocale"
+ "_requiredDictationLocales"
+ "installedDictationLocaleIdentifiers"
+ "isAutomaticCompilationEnabled"
+ "isEqualToSet:"
+ "sortUsingSelector:"
+ "subscriptionsForSubscriberId:"
+ "systemClientId"
+ "updateRequiredLocales"
- "%s Failed to resolve locale for language: %@"
- "%s Refreshing required locales as needed..."
- "-[CESRSpeechProfileSettings _isAssistantRequired]"
- "-[CESRSpeechProfileSettings _isDictationRequired]"
- "-[CESRSpeechProfileSettings refreshRequiredLocales:]"
- "B20@0:8B16"
- "currentDictationLanguageCodes"
- "handleAssetUpdate"
- "handleSettingsChange"
- "initWithAssistantLocale:dictationLocales:"
- "installationStatusForLanguagesWithAssetType:"
- "refreshRequiredLocales:"
- "v32@?0@\"NSString\"8@\"NSString\"16^B24"

```
