## HealthDiagnosticExtensionCore

> `/System/Library/PrivateFrameworks/HealthDiagnosticExtensionCore.framework/HealthDiagnosticExtensionCore`

```diff

-5200.5.1.0.0
-  __TEXT.__text: 0xe35c
-  __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_methlist: 0x7c4
+6074.1.2.4.0
+  __TEXT.__text: 0xb948
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_methlist: 0x6cc
   __TEXT.__const: 0x3a
-  __TEXT.__cstring: 0x2fe9
+  __TEXT.__cstring: 0x27c7
   __TEXT.__oslogstring: 0x34
-  __TEXT.__gcc_except_tab: 0x358
-  __TEXT.__unwind_info: 0x3b0
-  __TEXT.__objc_classname: 0x1b2
-  __TEXT.__objc_methname: 0x265f
-  __TEXT.__objc_methtype: 0x26f
-  __TEXT.__objc_stubs: 0x29e0
-  __DATA_CONST.__got: 0x448
-  __DATA_CONST.__const: 0x710
+  __TEXT.__gcc_except_tab: 0x304
+  __TEXT.__unwind_info: 0x328
+  __TEXT.__objc_classname: 0x1bb
+  __TEXT.__objc_methname: 0x1fe8
+  __TEXT.__objc_methtype: 0x253
+  __TEXT.__objc_stubs: 0x2160
+  __DATA_CONST.__got: 0x3f8
+  __DATA_CONST.__const: 0x5e0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xad8
+  __DATA_CONST.__objc_selrefs: 0x8b8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_arraydata: 0x1e8
-  __AUTH_CONST.__auth_got: 0x3b8
-  __AUTH_CONST.__const: 0x80
-  __AUTH_CONST.__cfstring: 0x3040
+  __DATA_CONST.__objc_arraydata: 0xa8
+  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__cfstring: 0x2700
   __AUTH_CONST.__objc_const: 0x8b8
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__objc_arrayobj: 0xd8
+  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0x370
   __DATA.__objc_ivar: 0x2c
   __DATA.__data: 0xc0

   - /System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
+  - /System/Library/PrivateFrameworks/RegulatoryDomain.framework/RegulatoryDomain
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 6CF35B0F-163E-3BEE-BD42-DF30F7933EB7
-  Functions: 216
-  Symbols:   1210
-  CStrings:  1233
+  UUID: 80FE5333-221E-342F-9B8D-A2E301EEF8BF
+  Functions: 185
+  Symbols:   1046
+  CStrings:  1008
 
Symbols:
+ +[HDUserDomainConceptDiagnosticOperation _udcTableColumnTitles]
+ -[HDFeatureStatusDiagnosticOperation _reportCountryCodeOverride]
+ -[HDFeatureStatusDiagnosticOperation _reportCountryCodeSource]
+ -[HDUserDomainConceptDiagnosticOperation _enumerateUDCTableInDatabase:appendToFormatter:error:]
+ -[HDUserDomainConceptDiagnosticOperation _logAndAndAppendFormat:]
+ -[HDUserDomainConceptDiagnosticOperation _reportCountsForUDCTableRowsInDatabase:]
+ -[HDUserDomainConceptDiagnosticOperation _reportUDCTableInDatabase:]
+ -[HDUserDomainConceptDiagnosticOperation _reportUserDomainConceptsForDatabase:]
+ -[HDUserDomainConceptDiagnosticOperation _reportUserDomainConcepts]
+ -[HDUserDomainConceptDiagnosticOperation reportFilename]
+ -[HDUserDomainConceptDiagnosticOperation run]
+ _HKPreferredRegulatoryDomainProvider
+ _HKRegulatoryDomainEstimateOverrideISOCode
+ _NSStringFromHKOnboardingCompletionCountryCodeProvenance
+ _OBJC_CLASS_$_HDUserDomainConceptDiagnosticOperation
+ _OBJC_CLASS_$_RDEstimate
+ _OBJC_METACLASS_$_HDUserDomainConceptDiagnosticOperation
+ __OBJC_$_CLASS_METHODS_HDUserDomainConceptDiagnosticOperation
+ __OBJC_$_INSTANCE_METHODS_HDUserDomainConceptDiagnosticOperation
+ __OBJC_CLASS_RO_$_HDUserDomainConceptDiagnosticOperation
+ __OBJC_METACLASS_RO_$_HDUserDomainConceptDiagnosticOperation
+ ___95-[HDUserDomainConceptDiagnosticOperation _enumerateUDCTableInDatabase:appendToFormatter:error:]_block_invoke
+ ___block_literal_global.431
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_HealthDiagnosticExtensionCore
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_HealthDiagnosticExtensionCore
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_HealthDiagnosticExtensionCore
+ _notify_cancel
+ _notify_is_valid_token
+ _objc_msgSend$ISOCode
+ _objc_msgSend$_reportCountryCodeOverride
+ _objc_msgSend$_reportCountryCodeSource
+ _objc_msgSend$currentEstimate
+ _objc_msgSend$currentEstimates
+ _objc_msgSend$featureAvailabilityProvidingForFeatureIdentifier:
+ _objc_msgSend$fetchCloudDescriptionWithProgress:useDescriptionForLogs:prettyPrinted:updateCacheAndPrepareForSync:completion:
+ _objc_msgSend$provenance
+ _objc_msgSend$timestamp
- +[HDOntologyDiagnosticOperation _appendEntry:tableFormatter:]
- +[HDOntologyDiagnosticOperation _udcTableColumnTitles]
- -[HDOntologyDiagnosticOperation _appendDateStringForDefaultKey:tableFormatter:healthStore:]
- -[HDOntologyDiagnosticOperation _countOfElementsPerSlotInDatabase:]
- -[HDOntologyDiagnosticOperation _entriesForSlots:database:]
- -[HDOntologyDiagnosticOperation _enumerateUDCTableInDatabase:appendToFormatter:error:]
- -[HDOntologyDiagnosticOperation _expandResultsToIndividualSlots:]
- -[HDOntologyDiagnosticOperation _logAndAndAppendFormat:]
- -[HDOntologyDiagnosticOperation _reportBasicChecksForDatabase:]
- -[HDOntologyDiagnosticOperation _reportCountsForUDCTableRowsInDatabase:]
- -[HDOntologyDiagnosticOperation _reportDomain:keyValues:]
- -[HDOntologyDiagnosticOperation _reportElementCountsBySlot:entriesBySlot:]
- -[HDOntologyDiagnosticOperation _reportElementCountsBySlotForDatabase:]
- -[HDOntologyDiagnosticOperation _reportForOntologyDatabase:]
- -[HDOntologyDiagnosticOperation _reportForOntologyDatabase]
- -[HDOntologyDiagnosticOperation _reportForOntologyFeaturesWithOntologyStore:]
- -[HDOntologyDiagnosticOperation _reportForOntologyKeyValueDomainsWithDatabase:]
- -[HDOntologyDiagnosticOperation _reportForOntologyKeyValueDomains]
- -[HDOntologyDiagnosticOperation _reportForOntologyUserDefaultsWithHealthStore:]
- -[HDOntologyDiagnosticOperation _reportForShardRequirementStatuses:]
- -[HDOntologyDiagnosticOperation _reportLocaleAndRegion]
- -[HDOntologyDiagnosticOperation _reportNetworkReachabilityForEnvironment:]
- -[HDOntologyDiagnosticOperation _reportOntologyHostURLWithOntologyStore:]
- -[HDOntologyDiagnosticOperation _reportOntologyMetadataForDatabase:]
- -[HDOntologyDiagnosticOperation _reportReachabilityFlags:]
- -[HDOntologyDiagnosticOperation _reportShardRegistryForDatabase:]
- -[HDOntologyDiagnosticOperation _reportUDCTableInDatabase:]
- -[HDOntologyDiagnosticOperation _reportUserDomainConceptsForDatabase:]
- -[HDOntologyDiagnosticOperation _reportUserDomainConcepts]
- -[HDOntologyDiagnosticOperation _valueForDaemonDefaultKey:healthStore:]
- -[HDOntologyDiagnosticOperation reportFilename]
- -[HDOntologyDiagnosticOperation run]
- GCC_except_table23
- GCC_except_table3
- GCC_except_table31
- _CFRelease
- _HDOntologyShardRegistryEntityPropertySlot
- _HKCompareIntegers
- _HKFeatureIdentifierIsProvidedBySleepDaemon
- _HKOntologyShardRegistryEntrySizeUnknown
- _HKStringFromOntologyShardSettings
- _HKStringFromOntologyShardState
- _HKStringFromOntologyShardVersion
- _HKStringFromOptionalBooleanResult
- _OBJC_CLASS_$_HDOntologyDiagnosticOperation
- _OBJC_CLASS_$_HDOntologyShardRegistryEntity
- _OBJC_CLASS_$_HDSQLiteContainsPredicate
- _OBJC_CLASS_$_HDSimpleGraphDatabaseAttributeEntity
- _OBJC_CLASS_$_HDSimpleGraphDatabaseMetadataEntity
- _OBJC_CLASS_$_HDSimpleGraphDatabaseNodeEntity
- _OBJC_CLASS_$_HDSimpleGraphDatabaseRelationshipEntity
- _OBJC_CLASS_$_HKFeatureAvailabilityStore
- _OBJC_CLASS_$_HKOntologyStore
- _OBJC_CLASS_$_NSLocale
- _OBJC_METACLASS_$_HDOntologyDiagnosticOperation
- _SCNetworkReachabilityCreateWithName
- _SCNetworkReachabilityGetFlags
- __OBJC_$_CLASS_METHODS_HDOntologyDiagnosticOperation
- __OBJC_$_INSTANCE_METHODS_HDOntologyDiagnosticOperation
- __OBJC_CLASS_RO_$_HDOntologyDiagnosticOperation
- __OBJC_METACLASS_RO_$_HDOntologyDiagnosticOperation
- ___59-[HDOntologyDiagnosticOperation _entriesForSlots:database:]_block_invoke
- ___65-[HDOntologyDiagnosticOperation _reportShardRegistryForDatabase:]_block_invoke
- ___65-[HDOntologyDiagnosticOperation _reportShardRegistryForDatabase:]_block_invoke_2
- ___67-[HDOntologyDiagnosticOperation _countOfElementsPerSlotInDatabase:]_block_invoke
- ___68-[HDOntologyDiagnosticOperation _reportOntologyMetadataForDatabase:]_block_invoke
- ___71-[HDOntologyDiagnosticOperation _valueForDaemonDefaultKey:healthStore:]_block_invoke
- ___73-[HDOntologyDiagnosticOperation _reportOntologyHostURLWithOntologyStore:]_block_invoke
- ___77-[HDOntologyDiagnosticOperation _reportForOntologyFeaturesWithOntologyStore:]_block_invoke
- ___86-[HDOntologyDiagnosticOperation _enumerateUDCTableInDatabase:appendToFormatter:error:]_block_invoke
- ___block_descriptor_32_e71_q24?0"HKOntologyShardRegistryEntry"8"HKOntologyShardRegistryEntry"16l
- ___block_descriptor_40_e8_32s_e35_B32?0"NSString"8"NSString"16^24ls32l8
- ___block_descriptor_40_e8_32s_e42_B24?0"HKOntologyShardRegistryEntry"8^16ls32l8
- ___block_descriptor_48_e8_32s40r_e27_v24?0"NSURL"8"NSError"16lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e34_v24?0"NSDictionary"8"NSError"16lr40l8s32l8
- ___block_descriptor_48_e8_32s40s_e42_v32?0"NSString"8"NSArray"16"NSError"24ls32l8s40l8
- ___block_descriptor_56_e8_32s40r48r_e20_v24?08"NSError"16lr40l8r48l8s32l8
- ___block_literal_global.428
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_HealthDiagnosticExtensionCore
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_HealthDiagnosticExtensionCore
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_HealthDiagnosticExtensionCore
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_HealthDiagnosticExtensionCore
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_HealthDiagnosticExtensionCore
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_HealthDiagnosticExtensionCore
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_HealthDiagnosticExtensionCore
- _objc_msgSend$_appendDateStringForDefaultKey:tableFormatter:healthStore:
- _objc_msgSend$_appendEntry:tableFormatter:
- _objc_msgSend$_countOfElementsPerSlotInDatabase:
- _objc_msgSend$_entriesForSlots:database:
- _objc_msgSend$_expandResultsToIndividualSlots:
- _objc_msgSend$_fetchDaemonPreferenceForKey:completion:
- _objc_msgSend$_reportBasicChecksForDatabase:
- _objc_msgSend$_reportDomain:keyValues:
- _objc_msgSend$_reportElementCountsBySlot:entriesBySlot:
- _objc_msgSend$_reportElementCountsBySlotForDatabase:
- _objc_msgSend$_reportForOntologyDatabase
- _objc_msgSend$_reportForOntologyDatabase:
- _objc_msgSend$_reportForOntologyFeaturesWithOntologyStore:
- _objc_msgSend$_reportForOntologyKeyValueDomains
- _objc_msgSend$_reportForOntologyKeyValueDomainsWithDatabase:
- _objc_msgSend$_reportForOntologyUserDefaultsWithHealthStore:
- _objc_msgSend$_reportForShardRequirementStatuses:
- _objc_msgSend$_reportLocaleAndRegion
- _objc_msgSend$_reportNetworkReachabilityForEnvironment:
- _objc_msgSend$_reportOntologyHostURLWithOntologyStore:
- _objc_msgSend$_reportOntologyMetadataForDatabase:
- _objc_msgSend$_reportReachabilityFlags:
- _objc_msgSend$_reportShardRegistryForDatabase:
- _objc_msgSend$_valueForDaemonDefaultKey:healthStore:
- _objc_msgSend$absoluteString
- _objc_msgSend$allKeys
- _objc_msgSend$availableChecksum
- _objc_msgSend$availableChecksumDate
- _objc_msgSend$availableLocale
- _objc_msgSend$availableLocaleDate
- _objc_msgSend$availableRegion
- _objc_msgSend$availableRegionDate
- _objc_msgSend$availableSize
- _objc_msgSend$availableSizeDate
- _objc_msgSend$availableState
- _objc_msgSend$availableStateDate
- _objc_msgSend$availableURL
- _objc_msgSend$availableURLDate
- _objc_msgSend$availableVersion
- _objc_msgSend$availableVersionDate
- _objc_msgSend$containsString:
- _objc_msgSend$countryCode
- _objc_msgSend$currentLocale
- _objc_msgSend$currentLocaleDate
- _objc_msgSend$currentRegion
- _objc_msgSend$currentRegionDate
- _objc_msgSend$currentVersion
- _objc_msgSend$currentVersionDate
- _objc_msgSend$desiredState
- _objc_msgSend$desiredStateDate
- _objc_msgSend$doubleValue
- _objc_msgSend$enumerateEntriesWithPredicate:orderingTerms:database:error:enumerationHandler:
- _objc_msgSend$enumerateMetadataValuesWithPredicate:database:error:enumerationHandler:
- _objc_msgSend$features
- _objc_msgSend$fetchCloudDescriptionWithProgress:completion:
- _objc_msgSend$fullDescription
- _objc_msgSend$hk_sortedKeys
- _objc_msgSend$identifier
- _objc_msgSend$initWithFeatureIdentifier:healthStore:
- _objc_msgSend$initWithProperty:values:contains:
- _objc_msgSend$integerValue
- _objc_msgSend$languageCode
- _objc_msgSend$localeIdentifier
- _objc_msgSend$longLongValue
- _objc_msgSend$mutableCopy
- _objc_msgSend$numberWithInteger:
- _objc_msgSend$ontologyServerURLWithCompletion:
- _objc_msgSend$schemaType
- _objc_msgSend$schemaVersion
- _objc_msgSend$settings
- _objc_msgSend$shardRequirementStatusesWithCompletion:
- _objc_msgSend$shardedOntology
- _objc_msgSend$slot
- _objc_msgSend$sortUsingComparator:
- _objc_msgSend$supportsOntology
- _objc_msgSend$supportsOntologyDatabaseUpdates
- _objc_msgSend$unsignedLongLongValue
- _objc_retainAutoreleaseReturnValue
CStrings:
+ "%@ (%@)"
+ "Country Code Information"
+ "Country Code Override"
+ "HDUserDomainConceptDiagnosticOperation"
+ "HKBehavior:"
+ "HKRegulatoryDomainEstimate"
+ "ISOCode"
+ "RDEstimate.currentEstimates"
+ "Retrieved: %@"
+ "UserDomainConcepts.txt"
+ "_reportCountryCodeOverride"
+ "_reportCountryCodeSource"
+ "currentEstimate"
+ "currentEstimates"
+ "featureAvailabilityProvidingForFeatureIdentifier:"
+ "fetchCloudDescriptionWithProgress:useDescriptionForLogs:prettyPrinted:updateCacheAndPrepareForSync:completion:"
+ "provenance"
- "        %lld %@"
- " %@ %@ %ld"
- "%@ Key Value Domain"
- "Analyzing ontology database...\n"
- "Available Locale"
- "Available Locale Date"
- "Available Region"
- "Available Region Date"
- "Available State"
- "Available State Date"
- "Available Version"
- "Available Version Date"
- "B24@?0@\"HKOntologyShardRegistryEntry\"8^@16"
- "B32@?0@\"NSString\"8@\"NSString\"16^@24"
- "Checksum"
- "Checksum Date"
- "ConnectionOnDemand"
- "ConnectionOnTraffic"
- "ConnectionRequired"
- "Current Country/Region: %@"
- "Current Language: %@"
- "Current Locale"
- "Current Locale Date"
- "Current Locale: %@"
- "Current Region"
- "Current Region Date"
- "Current Version"
- "Current Version Date"
- "Desired State"
- "Desired State Date"
- "Error getting daemon default for key \"%@\": %@"
- "Failed to enumerate ontology metadata: %@"
- "Failed to enumerate shard registry entries: %@"
- "Failed to get count of elements per shard slot: %@"
- "Feature"
- "HDOntologyDiagnosticOperation"
- "HDOntologyUpdateCoordinator"
- "HealthOntology.db"
- "ID"
- "InterventionRequired"
- "IsDirect"
- "IsLocalAddress"
- "IsWWAN"
- "Key"
- "No feature evaluators to report required shards"
- "Ontology Database %@"
- "Ontology Feature Evaluator Statuses"
- "Ontology Host URL: %@"
- "Ontology Metadata"
- "Ontology Shard Registry"
- "Ontology.txt"
- "PeriodicActivity-com.apple.healthd.ontology.update-EarliestNextRun"
- "PeriodicActivity-com.apple.healthd.ontology.update-ErrorCount"
- "PeriodicActivity-com.apple.healthd.ontology.update-LastSuccessfulRun"
- "Reachability Flag"
- "Reachable"
- "Required"
- "SELECT 'nodes', slots, COUNT(*) FROM nodes GROUP BY slots UNION ALL SELECT 'attributes', slots, COUNT(*) FROM attributes GROUP BY slots UNION ALL SELECT 'relationships', slots, COUNT(*) FROM relationships GROUP BY slots"
- "Schema"
- "Schema Version"
- "Settings"
- "Sharded Ontology Enabled: %@"
- "Size"
- "Size Date"
- "Slot"
- "Slot %@%@"
- "Supports Ontology Database Updates: %@"
- "Supports Ontology: %@"
- "Timed out attempting to get daemon default for key \"%@\""
- "Timed out attempting to get shard requirement statuses"
- "Timed out attempting to get the ontology host URL"
- "TransientConnection"
- "URL"
- "URL Date"
- "Unable to get reachability flags for \"%@\""
- "Value"
- "_appendDateStringForDefaultKey:tableFormatter:healthStore:"
- "_appendEntry:tableFormatter:"
- "_countOfElementsPerSlotInDatabase:"
- "_entriesForSlots:database:"
- "_expandResultsToIndividualSlots:"
- "_fetchDaemonPreferenceForKey:completion:"
- "_reportBasicChecksForDatabase:"
- "_reportDomain:keyValues:"
- "_reportElementCountsBySlot:entriesBySlot:"
- "_reportElementCountsBySlotForDatabase:"
- "_reportForOntologyDatabase"
- "_reportForOntologyDatabase:"
- "_reportForOntologyFeaturesWithOntologyStore:"
- "_reportForOntologyKeyValueDomains"
- "_reportForOntologyKeyValueDomainsWithDatabase:"
- "_reportForOntologyUserDefaultsWithHealthStore:"
- "_reportForShardRequirementStatuses:"
- "_reportLocaleAndRegion"
- "_reportNetworkReachabilityForEnvironment:"
- "_reportOntologyHostURLWithOntologyStore:"
- "_reportOntologyMetadataForDatabase:"
- "_reportReachabilityFlags:"
- "_reportShardRegistryForDatabase:"
- "_valueForDaemonDefaultKey:healthStore:"
- "absoluteString"
- "allKeys"
- "attributes"
- "availableChecksum"
- "availableChecksumDate"
- "availableLocale"
- "availableLocaleDate"
- "availableRegion"
- "availableRegionDate"
- "availableSize"
- "availableSizeDate"
- "availableState"
- "availableStateDate"
- "availableURL"
- "availableURLDate"
- "availableVersion"
- "availableVersionDate"
- "containsString:"
- "countryCode"
- "currentLocale"
- "currentLocaleDate"
- "currentRegion"
- "currentRegionDate"
- "currentVersion"
- "currentVersionDate"
- "desiredState"
- "desiredStateDate"
- "doubleValue"
- "enumerateEntriesWithPredicate:orderingTerms:database:error:enumerationHandler:"
- "enumerateMetadataValuesWithPredicate:database:error:enumerationHandler:"
- "features"
- "fetchCloudDescriptionWithProgress:completion:"
- "fullDescription"
- "healthd User Defaults"
- "hk_sortedKeys"
- "identifier"
- "initWithFeatureIdentifier:healthStore:"
- "initWithProperty:values:contains:"
- "integerValue"
- "languageCode"
- "localeIdentifier"
- "longLongValue"
- "mutableCopy"
- "nodes"
- "numberWithInteger:"
- "ontology"
- "ontologyServerURLWithCompletion:"
- "q24@?0@\"HKOntologyShardRegistryEntry\"8@\"HKOntologyShardRegistryEntry\"16"
- "relationships"
- "schemaType"
- "schemaVersion"
- "settings"
- "shardRequirementStatusesWithCompletion:"
- "shardedOntology"
- "slot"
- "sortUsingComparator:"
- "supportsOntology"
- "supportsOntologyDatabaseUpdates"
- "unkown"
- "unsignedLongLongValue"
- "updateEndDate"
- "updateError"
- "updateStartDate"
- "v20@0:8I16"
- "v24@?0@\"NSDictionary\"8@\"NSError\"16"
- "v24@?0@\"NSURL\"8@\"NSError\"16"
- "v24@?0@8@\"NSError\"16"
- "v32@?0@\"NSString\"8@\"NSArray\"16@\"NSError\"24"
- "v40@0:8@16@24@32"

```
