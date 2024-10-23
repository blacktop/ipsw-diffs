## FedStatsPluginCore

> `/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/FedStatsPluginCore`

```diff

-15.0.0.0.0
-  __TEXT.__text: 0x8000
-  __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_methlist: 0x60c
-  __TEXT.__const: 0x78
-  __TEXT.__cstring: 0xe0d
-  __TEXT.__oslogstring: 0x794
+17.0.0.0.0
+  __TEXT.__text: 0x9a80
+  __TEXT.__auth_stubs: 0x3c0
+  __TEXT.__objc_methlist: 0x764
+  __TEXT.__const: 0x80
+  __TEXT.__cstring: 0x12a0
+  __TEXT.__oslogstring: 0x892
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__unwind_info: 0x1c0
-  __TEXT.__objc_classname: 0x290
-  __TEXT.__objc_methname: 0x15d3
-  __TEXT.__objc_methtype: 0x274
-  __TEXT.__objc_stubs: 0x1480
-  __DATA_CONST.__got: 0x220
-  __DATA_CONST.__const: 0xd8
-  __DATA_CONST.__objc_classlist: 0xa0
+  __TEXT.__unwind_info: 0x208
+  __TEXT.__objc_classname: 0x2cf
+  __TEXT.__objc_methname: 0x19ee
+  __TEXT.__objc_methtype: 0x2ab
+  __TEXT.__objc_stubs: 0x17a0
+  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5a8
-  __DATA_CONST.__objc_superrefs: 0x60
-  __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x1f8
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x12a0
-  __AUTH_CONST.__objc_const: 0x1608
-  __AUTH_CONST.__objc_arrayobj: 0x60
+  __DATA_CONST.__objc_selrefs: 0x698
+  __DATA_CONST.__objc_superrefs: 0x70
+  __DATA_CONST.__objc_arraydata: 0xc0
+  __AUTH_CONST.__auth_got: 0x1f0
+  __AUTH_CONST.__const: 0x120
+  __AUTH_CONST.__cfstring: 0x1860
+  __AUTH_CONST.__objc_const: 0x1910
+  __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x640
-  __DATA.__objc_ivar: 0x6c
+  __AUTH.__objc_data: 0x730
+  __DATA.__objc_ivar: 0x84
   __DATA.__data: 0x128
   __DATA.__bss: 0x78
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 147
-  Symbols:   315
-  CStrings:  523
+  Functions: 178
+  Symbols:   352
+  CStrings:  620
 
Symbols:
+ _OBJC_CLASS_$_FedStatsCohortQueryURLBits
+ _OBJC_CLASS_$_FedStatsPluginEngine
+ _OBJC_CLASS_$_FedStatsUtils
+ _OBJC_CLASS_$_InstalledApp
+ _OBJC_METACLASS_$_FedStatsCohortQueryURLBits
+ _OBJC_METACLASS_$_FedStatsPluginEngine
+ _OBJC_METACLASS_$_InstalledApp
+ _kFedStatsCohortMissingField
- __os_log_fault_impl
CStrings:
+ "\x04"
+ "\a"
+ "@56@0:8@16@24@32@40@48"
+ "@72@0:8@16@24@32@40@48@56@64"
+ "Asset provider should have a single recipe for this call"
+ "B24@0:8^@16"
+ "B24@?0@\"InstalledApp\"8^B16"
+ "Cannot create recipe with identifier '%!@(MISSING)'. Error: %!@(MISSING)"
+ "Cannot decode and record some data."
+ "Cannot decode and record some data. Error:"
+ "Cannot download asset \"%!@(MISSING)\"."
+ "Cannot download asset \"%!@(MISSING)\". Error:"
+ "Cannot fetch assets using asset provider. Error: %!@(MISSING)"
+ "Cannot fill in URLs for the data-type-content."
+ "Cannot fill in URLs for the data-type-content. Error: "
+ "Cannot generate collection key"
+ "Cannot get consent for recipe with identifier '%!@(MISSING)'. Error: %!@(MISSING)"
+ "Cannot run query for recipe with identifier '%!@(MISSING)'. Error: %!@(MISSING)"
+ "Cannot validate Dedisco V2 config for this use-case."
+ "Error while collating data..."
+ "FedStatsCohortQueryInstalledApps#resolveDomainToBundleIds resolved domain to bundle ids: %!@(MISSING)"
+ "FedStatsCohortQueryURLBits"
+ "FedStatsPluginEngine"
+ "InstalledApp"
+ "InstalledApp { bundleIdentifier: %!@(MISSING) }"
+ "MCC"
+ "MNC"
+ "Recorded %!@(MISSING) payloads for recipe with identifier '%!@(MISSING)'"
+ "Recorded %!l(MISSING)u data for %!l(MISSING)u collection keys"
+ "SHA1AsBitString:"
+ "Some collection keys cannot be generated"
+ "T@\"NSArray\",&,N,V_supportedIntents"
+ "T@\"NSArray\",&,N,V_supportedMediaCategories"
+ "T@\"NSDictionary\",&,N,V_domainToInstalledApps"
+ "T@\"NSString\",&,N,V_appName"
+ "T@\"NSString\",&,N,V_bundleIdentifier"
+ "T@\"NSString\",R,N,V_recipeIdentifier"
+ "The data should have a String value for key \"%!@(MISSING)\""
+ "_appName"
+ "_bundleIdentifier"
+ "_domainToInstalledApps"
+ "_recipeIdentifier"
+ "_supportedIntents"
+ "_supportedMediaCategories"
+ "appName"
+ "applyFilteringForMediaDomain"
+ "array"
+ "assetKeysFromCollatedData:"
+ "assetURLForRecipe:forKey:error:"
+ "assetURLsForAssetKeys:"
+ "bitStringToInt:"
+ "bit_string_to_int"
+ "bitsOfURL"
+ "cardShownOrEngaged"
+ "category"
+ "checkConsentWithError:"
+ "collateQueryResults:"
+ "com.apple.insights.safari.highlights"
+ "com.charliemchapman.dark-noise"
+ "com.google.ios.youtube"
+ "com.iqiyi.child"
+ "com.iqiyi.iphone"
+ "com.qiyi.hd"
+ "com.soda.music"
+ "com.tencent.QQKSong"
+ "com.youku.YouKu"
+ "com.zhiliaoapp.musically.IntentExtension"
+ "deploymentIdentifierForRecipe:"
+ "domainToInstalledApps"
+ "evaluateQueryWithError:"
+ "experimentIdentifierForRecipe:"
+ "fedstats:com.apple.insights.safari.highlights"
+ "fetchAssets:error:"
+ "focusRegionType"
+ "footprint"
+ "initWithAssetProvider:recipeIdentifier:clientIdentifier:recordMetadata:dataTypeContent:sqlQuery:cohortNameList:"
+ "initWithBundleIdentifier:supportedMediaCategories:supportedIntents:appName:"
+ "initWithPrefix:cohortKeys:requiredFields:assetProvider:recipeIdentifier:"
+ "initialize"
+ "language"
+ "localizedName"
+ "matchedEmNumSource"
+ "memoryGenerated"
+ "memoryShared"
+ "memoryWatched"
+ "namespaceIdentifierForRecipe:"
+ "objectsPassingTest:"
+ "pageCount"
+ "passiveGestureAssessment"
+ "passiveLivenessAssessment"
+ "previous"
+ "protocol"
+ "recipeDictionaryForRecipe:error:"
+ "recipeIdentifier"
+ "recipeIdentifiers"
+ "recipeWithAssetProvider:recipeIdentifier:error:"
+ "recordCollatedData:assetURLs:"
+ "removeAssets"
+ "reportPluginForAssetProvider:recipeIdentifier:withError:"
+ "reportPluginSucceedForAssetProvider:recipeIdentifier:"
+ "runAllRecipesWithAssetProvider:"
+ "scope"
+ "setAppName:"
+ "setBundleIdentifier:"
+ "setDomainToInstalledApps:"
+ "setSet:"
+ "setSupportedIntents:"
+ "setSupportedMediaCategories:"
+ "sha1"
+ "sip380Procedure"
+ "sip380RedirectedURN"
+ "styleSelectionType"
+ "suggestionType"
+ "supportedMediaCategories"
+ "tokenizeAndSampleUnigramFromNgram:"
+ "tokenize_and_sample_unigram_from_ngram"
+ "treatmentIdentifierForRecipe:"
+ "tv.danmaku.bilianime"
+ "userLibraryAgeInDays"
+ "v40@0:8@16@24@32"
- "\x06"
- "@64@0:8@16@24@32@40@48@56"
- "Cannot decode and record some data"
- "Cannot download asset \"%!@(MISSING)\". Error: "
- "Cannot fill in URLs for the data-type-content"
- "Cannot record all data: %!@(MISSING)"
- "Cannot remove asset \"%!@(MISSING)\". Error: "
- "Error:"
- "Received nil data array"
- "SQL Query Recording Error"
- "T@\"NSDictionary\",&,N,V_domainToBundleIds"
- "_domainToBundleIds"
- "assetURLForKey:error:"
- "domainToBundleIds"
- "initWithAssetProvider:clientIdentifier:recordMetadata:dataTypeContent:sqlQuery:cohortNameList:"
- "initWithPrefix:cohortKeys:requiredFields:assetProvider:"
- "recipeDictionaryWithError:"
- "recordDataArray:error:"
- "recordDataArray:metadata:error:"
- "removeAssetForKey:error:"
- "reportPluginForAssetProvider:withError:"
- "reportPluginSucceedForAssetProvider:"
- "setDomainToBundleIds:"

```
