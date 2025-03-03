## FedStatsPluginCore

> `/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/FedStatsPluginCore`

```diff

-21.0.0.0.0
-  __TEXT.__text: 0xa898
-  __TEXT.__auth_stubs: 0x3d0
-  __TEXT.__objc_methlist: 0x7a4
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x152a
-  __TEXT.__oslogstring: 0x8e7
+29.0.0.0.0
+  __TEXT.__text: 0xc00c
+  __TEXT.__auth_stubs: 0x3f0
+  __TEXT.__objc_methlist: 0x9dc
+  __TEXT.__const: 0x98
+  __TEXT.__cstring: 0x19cb
+  __TEXT.__oslogstring: 0xa10
   __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__unwind_info: 0x218
-  __TEXT.__objc_classname: 0x2ef
-  __TEXT.__objc_methname: 0x1b5e
-  __TEXT.__objc_methtype: 0x2b6
-  __TEXT.__objc_stubs: 0x1920
-  __DATA_CONST.__got: 0x258
+  __TEXT.__unwind_info: 0x260
+  __TEXT.__objc_classname: 0x33e
+  __TEXT.__objc_methname: 0x1f82
+  __TEXT.__objc_methtype: 0x30d
+  __TEXT.__objc_stubs: 0x1bc0
+  __DATA_CONST.__got: 0x268
   __DATA_CONST.__const: 0x100
-  __DATA_CONST.__objc_classlist: 0xc0
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6f8
-  __DATA_CONST.__objc_superrefs: 0x70
+  __DATA_CONST.__objc_selrefs: 0x838
+  __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__auth_got: 0x1f8
-  __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x1bc0
-  __AUTH_CONST.__objc_const: 0x1a00
+  __AUTH_CONST.__auth_got: 0x208
+  __AUTH_CONST.__const: 0x140
+  __AUTH_CONST.__cfstring: 0x2020
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
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 184
-  Symbols:   366
-  CStrings:  663
+  Functions: 208
+  Symbols:   396
+  CStrings:  745
 
Symbols:
+ _OBJC_CLASS_$_FedStatsCohortQueryUserSetDeviceRegion
+ _OBJC_CLASS_$_FedStatsPluginDefaultDonationParameters
+ _OBJC_CLASS_$_FedStatsUtilsNegativeBinomialDistribution
+ _OBJC_METACLASS_$_FedStatsCohortQueryUserSetDeviceRegion
+ _OBJC_METACLASS_$_FedStatsPluginDefaultDonationParameters
+ _exp
+ _log
- _NSLocaleCountryCode
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
- "\a"
- "%@_%@"
- "@72@0:8@16@24@32@40@48@56@64"
- "Asset provider should have a single recipe for this call"
- "currentLocale"
- "initWithAssetProvider:recipeIdentifier:clientIdentifier:recordMetadata:dataTypeContent:sqlQuery:cohortNameList:"
- "preferredLanguages"
- "tokenizeAndSampleUnigramFromNgram:"
- "tokenize_and_sample_unigram_from_ngram"

```
