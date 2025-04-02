## FedStatsPluginCore

> `/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/FedStatsPluginCore`

```diff

-31.0.0.0.0
-  __TEXT.__text: 0xc00c
-  __TEXT.__auth_stubs: 0x3f0
-  __TEXT.__objc_methlist: 0x9dc
-  __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x19cb
-  __TEXT.__oslogstring: 0xa10
-  __TEXT.__gcc_except_tab: 0x28
-  __TEXT.__unwind_info: 0x260
-  __TEXT.__objc_classname: 0x33e
-  __TEXT.__objc_methname: 0x1f82
-  __TEXT.__objc_methtype: 0x30d
-  __TEXT.__objc_stubs: 0x1bc0
-  __DATA_CONST.__got: 0x268
-  __DATA_CONST.__const: 0x100
-  __DATA_CONST.__objc_classlist: 0xd0
+36.0.0.0.0
+  __TEXT.__text: 0x10154
+  __TEXT.__auth_stubs: 0x440
+  __TEXT.__objc_methlist: 0xbec
+  __TEXT.__const: 0xa8
+  __TEXT.__cstring: 0x1fe2
+  __TEXT.__gcc_except_tab: 0x84
+  __TEXT.__oslogstring: 0x1242
+  __TEXT.__unwind_info: 0x320
+  __TEXT.__objc_classname: 0x3d3
+  __TEXT.__objc_methname: 0x25c1
+  __TEXT.__objc_methtype: 0x37e
+  __TEXT.__objc_stubs: 0x2100
+  __DATA_CONST.__got: 0x290
+  __DATA_CONST.__const: 0x158
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x838
-  __DATA_CONST.__objc_superrefs: 0x80
-  __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__auth_got: 0x208
-  __AUTH_CONST.__const: 0x140
-  __AUTH_CONST.__cfstring: 0x2020
-  __AUTH_CONST.__objc_const: 0x1a30
-  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __DATA_CONST.__objc_selrefs: 0x9a0
+  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__objc_arraydata: 0x108
+  __AUTH_CONST.__auth_got: 0x230
+  __AUTH_CONST.__const: 0x1e0
+  __AUTH_CONST.__cfstring: 0x2600
+  __AUTH_CONST.__objc_const: 0x1e50
+  __AUTH_CONST.__objc_arrayobj: 0xd8
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x820
-  __DATA.__objc_ivar: 0x9c
-  __DATA.__data: 0x140
-  __DATA.__bss: 0x88
+  __AUTH.__objc_data: 0x960
+  __DATA.__objc_ivar: 0xc0
+  __DATA.__data: 0x148
+  __DATA.__bss: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/CoreIDVUI.framework/CoreIDVUI
   - /System/Library/PrivateFrameworks/DifferentialPrivacy.framework/DifferentialPrivacy

   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 208
-  Symbols:   396
-  CStrings:  745
+  Functions: 310
+  Symbols:   522
+  CStrings:  910
 
Symbols:
+ _BiomeLibrary
+ _CFRelease
+ _OBJC_CLASS_$_FedStatsPluginBiomeStreamPruner
+ _OBJC_CLASS_$_FedStatsPluginCoreConsentCheck
+ _OBJC_CLASS_$_FedStatsPluginCoreConsentCheckHelper
+ _OBJC_CLASS_$_FedStatsPluginDummyDataInjectionParameters
+ _OBJC_CLASS_$_FedStatsUtilsUniformUnitIntervalDistribution
+ _OBJC_METACLASS_$_FedStatsPluginBiomeStreamPruner
+ _OBJC_METACLASS_$_FedStatsPluginCoreConsentCheck
+ _OBJC_METACLASS_$_FedStatsPluginCoreConsentCheckHelper
+ _OBJC_METACLASS_$_FedStatsPluginDummyDataInjectionParameters
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateFromSelf
+ _arc4random_uniform
+ _kFedStatsDataCohortValueAllowList
+ _kFedStatsDataCohortValueBlockList
+ _kFedStatsPluginDummyDataInjectionRateLowerBound
CStrings:
+ "\x03"
+ "\n"
+ "\x11"
+ "%@: expected string input"
+ "@\"FedStatsPluginDummyDataInjectionParameters\""
+ "@\"FedStatsPluginSQL\""
+ "@32@0:8d16@24"
+ "@88@0:8@16@24@32@40@48@56@64@72@80"
+ "B20@0:8B16"
+ "B24@?0@\"BMStoreEvent\"8^B16"
+ "Bypassing default record check for namespace %@"
+ "CN"
+ "Cannot access CoreIDVUI consent manager. Error: %@"
+ "Cannot create consent check instance. Check the logs"
+ "Cannot create dummy data injection parameters from provided configuration"
+ "Cannot find consent configuration file in class bundle"
+ "Cannot find prunable streams file in class bundle"
+ "Cannot find the stream %@. Error: %@"
+ "Cannot get consent for recipe with identifier '%@'."
+ "Cannot load consent configuration file in class bundle"
+ "Cannot load prunable streams file in class bundle"
+ "Cannot read entitlement for the current process: %@"
+ "Checking consent for %@"
+ "Cohort value '%@' for cohort '%@' is not allowed for the namespace '%@'"
+ "Configuration key '%@' is not allowed"
+ "Consent configuration must have dictionary of strings to booleans as values"
+ "Consent configuration must have strings as keys"
+ "D&U consent is bypassed for this use-case"
+ "D&U consent is required and given for this use-case"
+ "D&U consent is required for this use-case but not given"
+ "Dummy data = %@"
+ "Dummy data injection parameters field names does not contain the data type '%@'"
+ "Dummy data injection parameters required for this SQL query but not provided properly"
+ "Error converting the event: %@"
+ "Error evaluating Biome query \"%@\": %@"
+ "Error getting %@ stream to check RSA eligibility: %@"
+ "Error getting Biome DB instance"
+ "Expected entitlement as an array but found something else"
+ "FED_STATS_BIOME_AI_SAFETY_FIRST"
+ "FED_STATS_BIOME_AI_SAFETY_THIRD"
+ "FedStatsCohortValueAllowList"
+ "FedStatsCohortValueBlockList"
+ "FedStatsPluginBiomeStreamPruner"
+ "FedStatsPluginCoreConsentCheck"
+ "FedStatsPluginCoreConsentCheckHelper"
+ "FedStatsPluginCoreConsentConfiguration"
+ "FedStatsPluginDummyDataInjectionParameters"
+ "FedStatsPluginPrunableStreams"
+ "Found the stream %@ in %@ entitlement"
+ "IH&A consent is required for this use-case but not given"
+ "Location consent is required for this use-case but not given"
+ "Mainland CN consent is required for this use-case but not given"
+ "No FedStatsPluginBiomeStreamPruner can be created. Check the logs."
+ "No special consent is required for this use-case. Gating through defaults."
+ "No streams are available to prune for namespace %@"
+ "Overriding injection rate %.2f to %.2f"
+ "Performing consent check"
+ "Processing Biome stream association for namespace %@"
+ "Prunable streams file must have strings as keys and array of strings as values"
+ "Pruned %lu events from %@"
+ "Recipe identifier %@ is not available, blocking the execution"
+ "Regional safety consent for 3rd party is required for this use-case but not given"
+ "Regional safety consent for Apple is required for this use-case but not given"
+ "RegionalSafetyAnalysis.Eligibility"
+ "SELECT * FROM 'RegionalSafetyAnalysis.Eligibility' ORDER BY eventTimestamp DESC LIMIT 1"
+ "SQL query '%@' does not match any required pattern for dummy data injection"
+ "SQL query '%@' matches the required pattern '%@' for dummy data injection"
+ "T@\"FedStatsPluginDummyDataInjectionParameters\",R,N,V_dummyDataInjectionParameters"
+ "T@\"FedStatsPluginSQL\",&,N,V_biomeSQL"
+ "T@\"NSDictionary\",&,N,V_accessInformation"
+ "T@\"NSDictionary\",&,V_biomeStreamAssociation"
+ "T@\"NSDictionary\",&,V_consentConfiguration"
+ "T@\"NSDictionary\",R,N,V_fieldValueSets"
+ "T@\"NSDictionary\",R,N,V_valueAllowList"
+ "T@\"NSDictionary\",R,N,V_valueBlockList"
+ "Td,R,N,V_injectionRate"
+ "The stream %@ is not entitled to be written"
+ "The stream '%@' is not prunable for %@"
+ "User Proofing consent is required for this use-case but not given"
+ "^.*RegionalSafetyAnalysis\\.Disablement.*$"
+ "^.*RegionalSafetyAnalysis\\.KeywordID.*$"
+ "_accessInformation"
+ "_biomeSQL"
+ "_biomeStreamAssociation"
+ "_consentConfiguration"
+ "_dummyDataInjectionParameters"
+ "_fieldValueSets"
+ "_injectionRate"
+ "_valueAllowList"
+ "_valueBlockList"
+ "`configuration['%@']['%@']` is an empty array"
+ "`configuration['%@']['%@']` is not an array"
+ "`configuration['%@']` dictionary key `%@` is not a string"
+ "`configuration['%@']` is an empty dictionary"
+ "`configuration['%@']` is not a dictionary"
+ "`configuration['%@']` is not a number"
+ "`configuration['%@']` is not in [0.0,1.0]"
+ "`configuration` does not have value for key '%@'"
+ "`configuration` parameter is not a dictionary"
+ "accessInformation"
+ "accessedColumnsForStream:"
+ "accessedStreams"
+ "assetVersion"
+ "biomeSQL"
+ "biomeStreamAssociation"
+ "checkCohortValue:forCohortName:namespaceIdentifier:"
+ "checkConsentConfigurationItem:"
+ "checkDnU"
+ "checkIDV"
+ "checkIHA"
+ "checkLocation"
+ "checkMCN"
+ "checkRSAEligibilityForApple"
+ "checkRSAEligibilityForCondition:"
+ "checkRSAEligibilityForThirdParty"
+ "cohort1"
+ "cohort2"
+ "cohort3"
+ "cohort4"
+ "cohortName:cohortValue => %@=%@ for namespace %@"
+ "com.apple.private.biome.read-write"
+ "configuration"
+ "consentConfiguration"
+ "deleteWithPolicy:eventsPassingTest:"
+ "dummyData"
+ "dummyDataInjectionParameters"
+ "eventClass"
+ "eventCount"
+ "fedstats-pruner"
+ "fieldValueSets"
+ "initWithAssetProvider:recipeIdentifier:clientIdentifier:recordMetadata:dataTypeContent:sqlQuery:cohortNameList:defaultDonationParameters:dummyDataInjectionParameters:"
+ "initWithBiomeStreamAssociation:"
+ "initWithConsentConfiguration:"
+ "initWithInjectionRate:fieldValueSets:"
+ "initWithJSONDictionary:error:"
+ "injectionRate"
+ "isAppleIntelligenceEligible"
+ "isAppleIntelligenceToggledOn"
+ "isConsentedForUseCase:"
+ "isOnboarded3rdParty"
+ "isThirdPartyAllowedUseCaseID:"
+ "is_third_party_allowed"
+ "needsDnU"
+ "needsIDV"
+ "needsIHA"
+ "needsLocation"
+ "needsMCN"
+ "needsRSAFirst"
+ "needsRSAThird"
+ "parametersWithConfiguration:error:"
+ "pruneBiomeStream:forNamespace:eventsPassingTest:"
+ "pruner"
+ "safetyDataVersion"
+ "setAccessInformation:"
+ "setBiomeSQL:"
+ "setBiomeStreamAssociation:"
+ "setConsentConfiguration:"
+ "shouldInjectDummyData"
+ "streamWithIdentifier:error:"
+ "table"
+ "transformUseCaseID:"
+ "transform_use_case_id"
+ "uppercaseString"
+ "v40@0:8@16@24@?32"
+ "valueAllowList"
+ "valueBlockList"
- "@80@0:8@16@24@32@40@48@56@64@72"
- "Cannot get consent for recipe with identifier '%@'. Error: %@"
- "The returned SQL accessed columns from BIOME is empty"
- "cohortName:cohortKey => %@=%@ for namespace %@"
- "initWithAssetProvider:recipeIdentifier:clientIdentifier:recordMetadata:dataTypeContent:sqlQuery:cohortNameList:defaultDonationParameters:"
- "unionSet:"

```
