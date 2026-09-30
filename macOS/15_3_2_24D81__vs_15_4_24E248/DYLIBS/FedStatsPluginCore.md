## FedStatsPluginCore

> `/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/Versions/A/FedStatsPluginCore`

```diff

-21.0.0.0.0
-  __TEXT.__text: 0xb654
-  __TEXT.__auth_stubs: 0x1c0
-  __TEXT.__objc_methlist: 0x7a4
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x14c2
-  __TEXT.__oslogstring: 0x8ba
-  __TEXT.__unwind_info: 0x208
-  __TEXT.__objc_classname: 0x2ef
-  __TEXT.__objc_methname: 0x1aff
-  __TEXT.__objc_methtype: 0x2b6
-  __TEXT.__objc_stubs: 0x18a0
-  __DATA_CONST.__got: 0x250
+32.0.0.0.0
+  __TEXT.__text: 0xcfdc
+  __TEXT.__auth_stubs: 0x1e0
+  __TEXT.__objc_methlist: 0x9dc
+  __TEXT.__const: 0x98
+  __TEXT.__cstring: 0x1963
+  __TEXT.__oslogstring: 0x9e3
+  __TEXT.__unwind_info: 0x250
+  __TEXT.__objc_classname: 0x33e
+  __TEXT.__objc_methname: 0x1f23
+  __TEXT.__objc_methtype: 0x30d
+  __TEXT.__objc_stubs: 0x1b40
+  __DATA_CONST.__got: 0x260
   __DATA_CONST.__const: 0xb0
-  __DATA_CONST.__objc_classlist: 0xc0
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d8
-  __DATA_CONST.__objc_superrefs: 0x70
+  __DATA_CONST.__objc_selrefs: 0x818
+  __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__auth_got: 0xe8
-  __AUTH_CONST.__const: 0x150
-  __AUTH_CONST.__cfstring: 0x1b80
-  __AUTH_CONST.__objc_const: 0x1a00
+  __AUTH_CONST.__auth_got: 0xf8
+  __AUTH_CONST.__const: 0x170
+  __AUTH_CONST.__cfstring: 0x1fe0
+  __AUTH_CONST.__objc_const: 0x1a30
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x780
-  __DATA.__objc_ivar: 0x84
+  __AUTH.__objc_data: 0x820
+  __DATA.__objc_ivar: 0x9c
   __DATA.__data: 0x140
-  __DATA.__bss: 0x78
+  __DATA.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /System/Library/PrivateFrameworks/Trial.framework/Versions/A/Trial
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0EAB0EA1-F45D-32D8-8367-A53D5999CA35
-  Functions: 182
-  Symbols:   730
-  CStrings:  870
+  UUID: F99E44D5-6625-38E4-A9D2-043FA038333D
+  Functions: 206
+  Symbols:   803
+  CStrings:  988
 
Symbols:
+ +[FedStatsCohortQueryUserSetDeviceRegion cohortInstance]
+ +[FedStatsCohortQueryUserSetDeviceRegion cohortInstance].cold.1
+ +[FedStatsPluginDefaultDonationParameters defaultDonationParametersWithConfiguration:error:]
+ +[FedStatsPluginDefaultDonationParameters expectedCohortSizesKeyForCohortVariable:cohortValue:]
+ +[FedStatsPluginLog logger].cold.1
+ -[FedStatsCohortQueryUserSetDeviceRegion .cxx_destruct]
+ -[FedStatsCohortQueryUserSetDeviceRegion cohortKeyForParameters:possibleError:]
+ -[FedStatsCohortQueryUserSetDeviceRegion init]
+ -[FedStatsCohortQueryUserSetDeviceRegion userSetDeviceRegion]
+ -[FedStatsPluginDefaultDonationParameters .cxx_destruct]
+ -[FedStatsPluginDefaultDonationParameters defaultExpectedCohortSize]
+ -[FedStatsPluginDefaultDonationParameters determineDefaultRecordCountFor:]
+ -[FedStatsPluginDefaultDonationParameters distributionFor:]
+ -[FedStatsPluginDefaultDonationParameters distributionFor:].cold.1
+ -[FedStatsPluginDefaultDonationParameters expectedCohortSizeFor:]
+ -[FedStatsPluginDefaultDonationParameters expectedCohortSizeFor:].cold.1
+ -[FedStatsPluginDefaultDonationParameters expectedCohortSizeFor:].cold.2
+ -[FedStatsPluginDefaultDonationParameters expectedCohortSizes]
+ -[FedStatsPluginDefaultDonationParameters initWithEpsilon:delta:defaultExpectedCohortSize:expectedCohortSizes:]
+ -[FedStatsPluginDefaultDonationParameters successProbability]
+ -[FedStatsPluginDefaultDonationParameters successRateNaught]
+ -[FedStatsPluginRecipe collateQueryResults:].cold.3
+ -[FedStatsPluginRecipe defaultDonationParameters]
+ -[FedStatsPluginRecipe initWithAssetProvider:recipeIdentifier:clientIdentifier:recordMetadata:dataTypeContent:sqlQuery:cohortNameList:defaultDonationParameters:]
+ OBJC_IVAR_$_FedStatsCohortQueryUserSetDeviceRegion._userSetDeviceRegion
+ OBJC_IVAR_$_FedStatsPluginDefaultDonationParameters._defaultExpectedCohortSize
+ OBJC_IVAR_$_FedStatsPluginDefaultDonationParameters._expectedCohortSizes
+ OBJC_IVAR_$_FedStatsPluginDefaultDonationParameters._successProbability
+ OBJC_IVAR_$_FedStatsPluginDefaultDonationParameters._successRateNaught
+ OBJC_IVAR_$_FedStatsPluginRecipe._defaultDonationParameters
+ _OBJC_CLASS_$_FedStatsCohortQueryUserSetDeviceRegion
+ _OBJC_CLASS_$_FedStatsPluginDefaultDonationParameters
+ _OBJC_CLASS_$_FedStatsUtilsNegativeBinomialDistribution
+ _OBJC_METACLASS_$_FedStatsCohortQueryUserSetDeviceRegion
+ _OBJC_METACLASS_$_FedStatsPluginDefaultDonationParameters
+ __OBJC_$_CLASS_METHODS_FedStatsCohortQueryUserSetDeviceRegion
+ __OBJC_$_CLASS_METHODS_FedStatsPluginDefaultDonationParameters
+ __OBJC_$_INSTANCE_METHODS_FedStatsCohortQueryUserSetDeviceRegion
+ __OBJC_$_INSTANCE_METHODS_FedStatsPluginDefaultDonationParameters
+ __OBJC_$_INSTANCE_VARIABLES_FedStatsCohortQueryUserSetDeviceRegion
+ __OBJC_$_INSTANCE_VARIABLES_FedStatsPluginDefaultDonationParameters
+ __OBJC_$_PROP_LIST_FedStatsCohortQueryUserSetDeviceRegion
+ __OBJC_$_PROP_LIST_FedStatsPluginDefaultDonationParameters
+ __OBJC_CLASS_PROTOCOLS_$_FedStatsCohortQueryUserSetDeviceRegion
+ __OBJC_CLASS_RO_$_FedStatsCohortQueryUserSetDeviceRegion
+ __OBJC_CLASS_RO_$_FedStatsPluginDefaultDonationParameters
+ __OBJC_METACLASS_RO_$_FedStatsCohortQueryUserSetDeviceRegion
+ __OBJC_METACLASS_RO_$_FedStatsPluginDefaultDonationParameters
+ ___56+[FedStatsCohortQueryUserSetDeviceRegion cohortInstance]_block_invoke
+ _exp
+ _log
+ _objc_msgSend$arrayByAddingObjectsFromArray:
+ _objc_msgSend$autoupdatingCurrentLocale
+ _objc_msgSend$defaultDataPointForDataTypeContent:
+ _objc_msgSend$defaultDonationParameters
+ _objc_msgSend$defaultDonationParametersWithConfiguration:error:
+ _objc_msgSend$defaultExpectedCohortSize
+ _objc_msgSend$determineDefaultRecordCountFor:
+ _objc_msgSend$distributionFor:
+ _objc_msgSend$distributionWithSuccessCount:successProbability:
+ _objc_msgSend$expectedCohortSizeFor:
+ _objc_msgSend$expectedCohortSizes
+ _objc_msgSend$expectedCohortSizesKeyForCohortVariable:cohortValue:
+ _objc_msgSend$getDeviceRegion
+ _objc_msgSend$initWithAssetProvider:recipeIdentifier:clientIdentifier:recordMetadata:dataTypeContent:sqlQuery:cohortNameList:defaultDonationParameters:
+ _objc_msgSend$initWithEpsilon:delta:defaultExpectedCohortSize:expectedCohortSizes:
+ _objc_msgSend$integerValue
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$languageIdentifier
+ _objc_msgSend$removeObject:
+ _objc_msgSend$sample
+ _objc_msgSend$sortUsingSelector:
+ _objc_msgSend$successProbability
+ _objc_msgSend$successRateNaught
+ _objc_msgSend$tokenizeSentence:removePunctuation:tokenizePerson:tokenizeLocation:tokenizeNumber:action:
+ _objc_msgSend$userSetDeviceRegion
+ cohortInstance.sharedInstance
+ sharedInstance.onceToken.331
- -[FedStatsPluginRecipe initWithAssetProvider:recipeIdentifier:clientIdentifier:recordMetadata:dataTypeContent:sqlQuery:cohortNameList:]
- _NSLocaleCountryCode
- _objc_msgSend$currentLocale
- _objc_msgSend$initWithAssetProvider:recipeIdentifier:clientIdentifier:recordMetadata:dataTypeContent:sqlQuery:cohortNameList:
- _objc_msgSend$preferredLanguages
- _objc_msgSend$tokenizeAndSampleUnigramFromNgram:
- sharedInstance.onceToken.282
CStrings:
+ "%@=%@"
+ "'%@' requires 6 args."
+ "1"
+ "@\"FedStatsPluginDefaultDonationParameters\""
+ "@48@0:8d16d24Q32@40"
+ "@80@0:8@16@24@32@40@48@56@64@72"
+ "Adding %lu default values = %@"
+ "Asset provider should have a single recipe for this call: %@"
+ "Cannot create privacy parameters from provided configuration"
+ "Cannot sample default count for cohort value set %@"
+ "FedStatsCohortQueryUserSetDeviceRegion"
+ "FedStatsPluginDefaultDonationParameters"
+ "NB(%e,%e) failed. Check the logs."
+ "No default donation parameters are set, continuing without injecting default values"
+ "No expected cohort size for cohort values %@"
+ "No expected cohort size value for cohort values %@"
+ "Privacy parameter `defaultExpectedCohortSize` must be a positive integer"
+ "Privacy parameter `delta` must be non-negative and less than %e"
+ "Privacy parameter `epsilon` must be greater than %e"
+ "Privacy parameter `expectedCohortSizes` has repeated cohort values for row %@"
+ "Privacy parameter `expectedCohortSizes` is missing `expectedCohortSize` number for row %@"
+ "Privacy parameter `expectedCohortSizes` should all have the same number of keys in each entry; first row has %lu keys but not row %@"
+ "Privacy parameters in recipe is missing `defaultExpectedCohortSize` number"
+ "Privacy parameters in recipe is missing `delta` number"
+ "Privacy parameters in recipe is missing `epsilon` number"
+ "Privacy parameters in recipe is missing `expectedCohortSizes` array"
+ "Privacy parameters in recipe must be a dictionary"
+ "Q24@0:8@16"
+ "T@\"FedStatsPluginDefaultDonationParameters\",R,N,V_defaultDonationParameters"
+ "T@\"NSDictionary\",R,N,V_expectedCohortSizes"
+ "T@\"NSString\",R,N,V_userSetDeviceRegion"
+ "TQ,R,N,V_defaultExpectedCohortSize"
+ "Td,R,N,V_successProbability"
+ "Td,R,N,V_successRateNaught"
+ "_defaultDonationParameters"
+ "_defaultExpectedCohortSize"
+ "_expectedCohortSizes"
+ "_successProbability"
+ "_successRateNaught"
+ "_userSetDeviceRegion"
+ "actions"
+ "arrayByAddingObjectsFromArray:"
+ "autoupdatingCurrentLocale"
+ "blockingReason"
+ "compare:"
+ "d"
+ "d16@0:8"
+ "defaultDataPointForDataTypeContent:"
+ "defaultDonationParameters"
+ "defaultDonationParametersWithConfiguration:error:"
+ "defaultExpectedCohortSize"
+ "delta"
+ "determineDefaultRecordCountFor:"
+ "distributionFor:"
+ "distributionWithSuccessCount:successProbability:"
+ "epsilon"
+ "expectedCohortSize"
+ "expectedCohortSizeFor:"
+ "expectedCohortSizes"
+ "expectedCohortSizesKeyForCohortVariable:cohortValue:"
+ "failedMechanisms"
+ "failingAction"
+ "getDeviceRegion"
+ "initWithAssetProvider:recipeIdentifier:clientIdentifier:recordMetadata:dataTypeContent:sqlQuery:cohortNameList:defaultDonationParameters:"
+ "initWithEpsilon:delta:defaultExpectedCohortSize:expectedCohortSizes:"
+ "integerValue"
+ "isEqualToNumber:"
+ "languageIdentifier"
+ "mechanisms"
+ "memoryPromptSuggestionSource"
+ "modelName"
+ "modelVersion"
+ "portType"
+ "region"
+ "removeObject:"
+ "sample"
+ "shootingCategory"
+ "shootingMode"
+ "sortUsingSelector:"
+ "successProbability"
+ "successRateNaught"
+ "successfulMechanism"
+ "taxonomy"
+ "tokenizeSentence:removePunctuation:tokenizePerson:tokenizeLocation:tokenizeNumber:action:"
+ "tokenize_ngram"
+ "usecaseId"
+ "userSetDeviceRegion"
- "%@_%@"
- "@72@0:8@16@24@32@40@48@56@64"
- "Asset provider should have a single recipe for this call"
- "currentLocale"
- "initWithAssetProvider:recipeIdentifier:clientIdentifier:recordMetadata:dataTypeContent:sqlQuery:cohortNameList:"
- "preferredLanguages"
- "tokenizeAndSampleUnigramFromNgram:"
- "tokenize_and_sample_unigram_from_ngram"

```
