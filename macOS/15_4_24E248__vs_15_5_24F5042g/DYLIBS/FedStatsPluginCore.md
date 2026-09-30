## FedStatsPluginCore

> `/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/Versions/A/FedStatsPluginCore`

```diff

-32.0.0.0.0
-  __TEXT.__text: 0xcfdc
-  __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__objc_methlist: 0x9dc
-  __TEXT.__const: 0x98
-  __TEXT.__cstring: 0x1963
-  __TEXT.__oslogstring: 0x9e3
-  __TEXT.__unwind_info: 0x250
-  __TEXT.__objc_classname: 0x33e
-  __TEXT.__objc_methname: 0x1f23
-  __TEXT.__objc_methtype: 0x30d
-  __TEXT.__objc_stubs: 0x1b40
-  __DATA_CONST.__got: 0x260
-  __DATA_CONST.__const: 0xb0
-  __DATA_CONST.__objc_classlist: 0xd0
+36.0.0.0.0
+  __TEXT.__text: 0x11264
+  __TEXT.__auth_stubs: 0x260
+  __TEXT.__objc_methlist: 0xbec
+  __TEXT.__const: 0xa0
+  __TEXT.__cstring: 0x1f7a
+  __TEXT.__gcc_except_tab: 0x2c
+  __TEXT.__oslogstring: 0x11b7
+  __TEXT.__unwind_info: 0x2e8
+  __TEXT.__objc_classname: 0x3d3
+  __TEXT.__objc_methname: 0x2562
+  __TEXT.__objc_methtype: 0x37e
+  __TEXT.__objc_stubs: 0x2080
+  __DATA_CONST.__got: 0x288
+  __DATA_CONST.__const: 0xe0
+  __DATA_CONST.__objc_classlist: 0xf0
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x818
-  __DATA_CONST.__objc_superrefs: 0x80
-  __DATA_CONST.__objc_arraydata: 0xe8
-  __AUTH_CONST.__auth_got: 0xf8
-  __AUTH_CONST.__const: 0x170
-  __AUTH_CONST.__cfstring: 0x1fe0
-  __AUTH_CONST.__objc_const: 0x1a30
-  __AUTH_CONST.__objc_arrayobj: 0xa8
+  __DATA_CONST.__objc_selrefs: 0x980
+  __DATA_CONST.__objc_superrefs: 0x98
+  __DATA_CONST.__objc_arraydata: 0x108
+  __AUTH_CONST.__auth_got: 0x140
+  __AUTH_CONST.__const: 0x240
+  __AUTH_CONST.__cfstring: 0x25c0
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
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/Versions/A/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Intents.framework/Versions/A/Intents
+  - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/BiomeFoundation.framework/Versions/A/BiomeFoundation
+  - /System/Library/PrivateFrameworks/BiomeLibrary.framework/Versions/A/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/Versions/A/BiomeStreams
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/Versions/A/CrashReporterSupport
   - /System/Library/PrivateFrameworks/DifferentialPrivacy.framework/Versions/A/DifferentialPrivacy

   - /System/Library/PrivateFrameworks/Trial.framework/Versions/A/Trial
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 206
-  Symbols:   803
-  CStrings:  737
+  Functions: 304
+  Symbols:   1013
+  CStrings:  900
 
Symbols:
+ +[FedStatsPluginBiomeStreamPruner pruneBiomeStream:forNamespace:eventsPassingTest:]
+ +[FedStatsPluginBiomeStreamPruner pruneBiomeStream:forNamespace:eventsPassingTest:].cold.1
+ +[FedStatsPluginBiomeStreamPruner pruneBiomeStream:forNamespace:eventsPassingTest:].cold.2
+ +[FedStatsPluginBiomeStreamPruner pruneBiomeStream:forNamespace:eventsPassingTest:].cold.3
+ +[FedStatsPluginBiomeStreamPruner pruneBiomeStream:forNamespace:eventsPassingTest:].cold.4
+ +[FedStatsPluginBiomeStreamPruner pruneBiomeStream:forNamespace:eventsPassingTest:].cold.5
+ +[FedStatsPluginBiomeStreamPruner sharedInstance]
+ +[FedStatsPluginBiomeStreamPruner sharedInstance].cold.1
+ +[FedStatsPluginCoreConsentCheck checkConsentConfigurationItem:]
+ +[FedStatsPluginCoreConsentCheck checkConsentConfigurationItem:].cold.1
+ +[FedStatsPluginCoreConsentCheck checkConsentConfigurationItem:].cold.2
+ +[FedStatsPluginCoreConsentCheck checkConsentConfigurationItem:].cold.3
+ +[FedStatsPluginCoreConsentCheck checkConsentConfigurationItem:].cold.4
+ +[FedStatsPluginCoreConsentCheck checkConsentConfigurationItem:].cold.5
+ +[FedStatsPluginCoreConsentCheck checkConsentConfigurationItem:].cold.6
+ +[FedStatsPluginCoreConsentCheck checkConsentConfigurationItem:].cold.7
+ +[FedStatsPluginCoreConsentCheck checkConsentConfigurationItem:].cold.8
+ +[FedStatsPluginCoreConsentCheck checkConsentConfigurationItem:].cold.9
+ +[FedStatsPluginCoreConsentCheck isConsentedForUseCase:]
+ +[FedStatsPluginCoreConsentCheck isConsentedForUseCase:].cold.1
+ +[FedStatsPluginCoreConsentCheck isConsentedForUseCase:].cold.2
+ +[FedStatsPluginCoreConsentCheck isConsentedForUseCase:].cold.3
+ +[FedStatsPluginCoreConsentCheck isConsentedForUseCase:].cold.4
+ +[FedStatsPluginCoreConsentCheck sharedInstance]
+ +[FedStatsPluginCoreConsentCheck sharedInstance].cold.1
+ +[FedStatsPluginCoreConsentCheckHelper checkDnU]
+ +[FedStatsPluginCoreConsentCheckHelper checkIDV]
+ +[FedStatsPluginCoreConsentCheckHelper checkIHA]
+ +[FedStatsPluginCoreConsentCheckHelper checkLocation]
+ +[FedStatsPluginCoreConsentCheckHelper checkMCN]
+ +[FedStatsPluginCoreConsentCheckHelper checkRSAEligibilityForApple]
+ +[FedStatsPluginCoreConsentCheckHelper checkRSAEligibilityForCondition:]
+ +[FedStatsPluginCoreConsentCheckHelper checkRSAEligibilityForCondition:].cold.1
+ +[FedStatsPluginCoreConsentCheckHelper checkRSAEligibilityForCondition:].cold.2
+ +[FedStatsPluginCoreConsentCheckHelper checkRSAEligibilityForCondition:].cold.3
+ +[FedStatsPluginCoreConsentCheckHelper checkRSAEligibilityForCondition:].cold.4
+ +[FedStatsPluginCoreConsentCheckHelper checkRSAEligibilityForThirdParty]
+ +[FedStatsPluginDummyDataInjectionParameters parametersWithConfiguration:error:]
+ +[FedStatsPluginDummyDataInjectionParameters parametersWithConfiguration:error:].cold.1
+ +[FedStatsPluginEngine hasRecipeIdentifier:usedWithAssetProvider:].cold.2
+ +[FedStatsPluginEngine hasRecipeIdentifier:usedWithAssetProvider:].cold.3
+ -[FedStatsDataCohort checkCohortValue:forCohortName:namespaceIdentifier:]
+ -[FedStatsDataCohort valueAllowList]
+ -[FedStatsDataCohort valueBlockList]
+ -[FedStatsPluginBiomeStreamPruner .cxx_destruct]
+ -[FedStatsPluginBiomeStreamPruner biomeStreamAssociation]
+ -[FedStatsPluginBiomeStreamPruner initWithBiomeStreamAssociation:]
+ -[FedStatsPluginBiomeStreamPruner setBiomeStreamAssociation:]
+ -[FedStatsPluginCoreConsentCheck .cxx_destruct]
+ -[FedStatsPluginCoreConsentCheck consentConfiguration]
+ -[FedStatsPluginCoreConsentCheck initWithConsentConfiguration:]
+ -[FedStatsPluginCoreConsentCheck setConsentConfiguration:]
+ -[FedStatsPluginDummyDataInjectionParameters .cxx_destruct]
+ -[FedStatsPluginDummyDataInjectionParameters dummyData]
+ -[FedStatsPluginDummyDataInjectionParameters dummyData].cold.1
+ -[FedStatsPluginDummyDataInjectionParameters fieldValueSets]
+ -[FedStatsPluginDummyDataInjectionParameters initWithInjectionRate:fieldValueSets:]
+ -[FedStatsPluginDummyDataInjectionParameters injectionRate]
+ -[FedStatsPluginDummyDataInjectionParameters shouldInjectDummyData]
+ -[FedStatsPluginRecipe accessedStreams]
+ -[FedStatsPluginRecipe biomeSQL]
+ -[FedStatsPluginRecipe dummyDataInjectionParameters]
+ -[FedStatsPluginRecipe initWithAssetProvider:recipeIdentifier:clientIdentifier:recordMetadata:dataTypeContent:sqlQuery:cohortNameList:defaultDonationParameters:dummyDataInjectionParameters:]
+ -[FedStatsPluginRecipe setBiomeSQL:]
+ -[FedStatsPluginSQL accessInformation]
+ -[FedStatsPluginSQL accessedColumnsForStream:]
+ -[FedStatsPluginSQL accessedStreams]
+ -[FedStatsPluginSQL setAccessInformation:]
+ GCC_except_table3
+ OBJC_IVAR_$_FedStatsDataCohort._valueAllowList
+ OBJC_IVAR_$_FedStatsDataCohort._valueBlockList
+ OBJC_IVAR_$_FedStatsPluginBiomeStreamPruner._biomeStreamAssociation
+ OBJC_IVAR_$_FedStatsPluginCoreConsentCheck._consentConfiguration
+ OBJC_IVAR_$_FedStatsPluginDummyDataInjectionParameters._fieldValueSets
+ OBJC_IVAR_$_FedStatsPluginDummyDataInjectionParameters._injectionRate
+ OBJC_IVAR_$_FedStatsPluginRecipe._biomeSQL
+ OBJC_IVAR_$_FedStatsPluginRecipe._dummyDataInjectionParameters
+ OBJC_IVAR_$_FedStatsPluginSQL._accessInformation
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
+ __48+[FedStatsPluginCoreConsentCheck sharedInstance]_block_invoke.cold.1
+ __48+[FedStatsPluginCoreConsentCheck sharedInstance]_block_invoke.cold.2
+ __48+[FedStatsPluginCoreConsentCheck sharedInstance]_block_invoke.cold.3
+ __48+[FedStatsPluginCoreConsentCheck sharedInstance]_block_invoke.cold.4
+ __48+[FedStatsPluginCoreConsentCheck sharedInstance]_block_invoke.cold.5
+ __48+[FedStatsPluginCoreConsentCheck sharedInstance]_block_invoke.cold.6
+ __48+[FedStatsPluginCoreConsentCheck sharedInstance]_block_invoke.cold.7
+ __49+[FedStatsPluginBiomeStreamPruner sharedInstance]_block_invoke.cold.1
+ __49+[FedStatsPluginBiomeStreamPruner sharedInstance]_block_invoke.cold.2
+ __49+[FedStatsPluginBiomeStreamPruner sharedInstance]_block_invoke.cold.3
+ __49+[FedStatsPluginBiomeStreamPruner sharedInstance]_block_invoke.cold.4
+ __49+[FedStatsPluginBiomeStreamPruner sharedInstance]_block_invoke.cold.5
+ __49+[FedStatsPluginBiomeStreamPruner sharedInstance]_block_invoke.cold.6
+ __49+[FedStatsPluginBiomeStreamPruner sharedInstance]_block_invoke.cold.7
+ __49+[FedStatsPluginBiomeStreamPruner sharedInstance]_block_invoke.cold.8
+ __Block_object_assign
+ __Block_object_dispose
+ __OBJC_$_CLASS_METHODS_FedStatsPluginBiomeStreamPruner
+ __OBJC_$_CLASS_METHODS_FedStatsPluginCoreConsentCheck
+ __OBJC_$_CLASS_METHODS_FedStatsPluginCoreConsentCheckHelper
+ __OBJC_$_CLASS_METHODS_FedStatsPluginDummyDataInjectionParameters
+ __OBJC_$_INSTANCE_METHODS_FedStatsPluginBiomeStreamPruner
+ __OBJC_$_INSTANCE_METHODS_FedStatsPluginCoreConsentCheck
+ __OBJC_$_INSTANCE_METHODS_FedStatsPluginDummyDataInjectionParameters
+ __OBJC_$_INSTANCE_VARIABLES_FedStatsPluginBiomeStreamPruner
+ __OBJC_$_INSTANCE_VARIABLES_FedStatsPluginCoreConsentCheck
+ __OBJC_$_INSTANCE_VARIABLES_FedStatsPluginDummyDataInjectionParameters
+ __OBJC_$_PROP_LIST_FedStatsPluginBiomeStreamPruner
+ __OBJC_$_PROP_LIST_FedStatsPluginCoreConsentCheck
+ __OBJC_$_PROP_LIST_FedStatsPluginDummyDataInjectionParameters
+ __OBJC_CLASS_RO_$_FedStatsPluginBiomeStreamPruner
+ __OBJC_CLASS_RO_$_FedStatsPluginCoreConsentCheck
+ __OBJC_CLASS_RO_$_FedStatsPluginCoreConsentCheckHelper
+ __OBJC_CLASS_RO_$_FedStatsPluginDummyDataInjectionParameters
+ __OBJC_METACLASS_RO_$_FedStatsPluginBiomeStreamPruner
+ __OBJC_METACLASS_RO_$_FedStatsPluginCoreConsentCheck
+ __OBJC_METACLASS_RO_$_FedStatsPluginCoreConsentCheckHelper
+ __OBJC_METACLASS_RO_$_FedStatsPluginDummyDataInjectionParameters
+ __Unwind_Resume
+ ___35-[FedStatsPluginSQL initWithError:]_block_invoke_6
+ ___35-[FedStatsPluginSQL initWithError:]_block_invoke_7
+ ___48+[FedStatsPluginCoreConsentCheck sharedInstance]_block_invoke
+ ___49+[FedStatsPluginBiomeStreamPruner sharedInstance]_block_invoke
+ ___55+[FedStatsPluginEngine runAllRecipesWithAssetProvider:]_block_invoke
+ ___83+[FedStatsPluginBiomeStreamPruner pruneBiomeStream:forNamespace:eventsPassingTest:]_block_invoke
+ ___block_descriptor_32_e26_B24?0"BMStoreEvent"8^B16l
+ ___block_descriptor_48_e8_32bs40r_e26_B24?0"BMStoreEvent"8^B16l
+ ___copy_helper_block_e8_32b40r
+ ___destroy_helper_block_e8_32s40r
+ ___objc_personality_v0
+ __block_literal_global.54
+ __block_literal_global.56
+ __block_literal_global.59
+ __block_literal_global.61
+ __block_literal_global.66
+ __block_literal_global.71
+ _arc4random_uniform
+ _checkDummyDataInjectionRequirements
+ _kFedStatsDataCohortValueAllowList
+ _kFedStatsDataCohortValueBlockList
+ _kFedStatsPluginDummyDataInjectionRateLowerBound
+ _objc_msgSend$accessInformation
+ _objc_msgSend$accessedStreams
+ _objc_msgSend$biomeSQL
+ _objc_msgSend$biomeStreamAssociation
+ _objc_msgSend$checkCohortValue:forCohortName:namespaceIdentifier:
+ _objc_msgSend$checkConsentConfigurationItem:
+ _objc_msgSend$checkDnU
+ _objc_msgSend$checkIDV
+ _objc_msgSend$checkIHA
+ _objc_msgSend$checkLocation
+ _objc_msgSend$checkMCN
+ _objc_msgSend$checkRSAEligibilityForApple
+ _objc_msgSend$checkRSAEligibilityForCondition:
+ _objc_msgSend$checkRSAEligibilityForThirdParty
+ _objc_msgSend$configuration
+ _objc_msgSend$consentConfiguration
+ _objc_msgSend$deleteWithPolicy:eventsPassingTest:
+ _objc_msgSend$dummyData
+ _objc_msgSend$dummyDataInjectionParameters
+ _objc_msgSend$eventClass
+ _objc_msgSend$fieldValueSets
+ _objc_msgSend$initWithAssetProvider:recipeIdentifier:clientIdentifier:recordMetadata:dataTypeContent:sqlQuery:cohortNameList:defaultDonationParameters:dummyDataInjectionParameters:
+ _objc_msgSend$initWithBiomeStreamAssociation:
+ _objc_msgSend$initWithConsentConfiguration:
+ _objc_msgSend$initWithInjectionRate:fieldValueSets:
+ _objc_msgSend$initWithJSONDictionary:error:
+ _objc_msgSend$injectionRate
+ _objc_msgSend$isAppleIntelligenceEligible
+ _objc_msgSend$isAppleIntelligenceToggledOn
+ _objc_msgSend$isConsentedForUseCase:
+ _objc_msgSend$isOnboarded3rdParty
+ _objc_msgSend$isThirdPartyAllowedUseCaseID:
+ _objc_msgSend$parametersWithConfiguration:error:
+ _objc_msgSend$pruneBiomeStream:forNamespace:eventsPassingTest:
+ _objc_msgSend$pruner
+ _objc_msgSend$setAccessInformation:
+ _objc_msgSend$setBiomeSQL:
+ _objc_msgSend$shouldInjectDummyData
+ _objc_msgSend$streamWithIdentifier:error:
+ _objc_msgSend$table
+ _objc_msgSend$transformUseCaseID:
+ _objc_msgSend$uppercaseString
+ _objc_msgSend$valueAllowList
+ _objc_msgSend$valueBlockList
+ checkDummyDataInjectionRequirements.cold.1
+ checkDummyDataInjectionRequirements.cold.2
+ sharedInstance.consentChecker
+ sharedInstance.kFedStatsPluginCoreConsentConfigurationAllowedKeys
+ sharedInstance.onceToken.358
- -[FedStatsPluginRecipe initWithAssetProvider:recipeIdentifier:clientIdentifier:recordMetadata:dataTypeContent:sqlQuery:cohortNameList:defaultDonationParameters:]
- __block_literal_global.48
- __block_literal_global.50
- __block_literal_global.53
- __block_literal_global.55
- _objc_msgSend$initWithAssetProvider:recipeIdentifier:clientIdentifier:recordMetadata:dataTypeContent:sqlQuery:cohortNameList:defaultDonationParameters:
- _objc_msgSend$unionSet:
- sharedInstance.onceToken.331
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
