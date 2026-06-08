## SpotlightReceiver

> `/System/Library/PrivateFrameworks/SpotlightReceiver.framework/SpotlightReceiver`

```diff

-2418.5.9.101.0
-  __TEXT.__text: 0xa0a8
-  __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__objc_methlist: 0x714
-  __TEXT.__const: 0x100
-  __TEXT.__gcc_except_tab: 0x244
-  __TEXT.__oslogstring: 0x5d2
-  __TEXT.__cstring: 0x8f8
-  __TEXT.__unwind_info: 0x1e8
-  __TEXT.__objc_classname: 0xd1
-  __TEXT.__objc_methname: 0x206d
-  __TEXT.__objc_methtype: 0x493
-  __TEXT.__objc_stubs: 0x1820
-  __DATA_CONST.__got: 0x168
-  __DATA_CONST.__const: 0x460
+2444.104.0.0.0
+  __TEXT.__text: 0xb7e4
+  __TEXT.__objc_methlist: 0x76c
+  __TEXT.__const: 0xf8
+  __TEXT.__gcc_except_tab: 0x538
+  __TEXT.__oslogstring: 0xbb6
+  __TEXT.__cstring: 0xa20
+  __TEXT.__unwind_info: 0x258
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x500
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7a0
+  __DATA_CONST.__objc_selrefs: 0x800
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__objc_arraydata: 0x48
-  __AUTH_CONST.__auth_got: 0x400
+  __DATA_CONST.__objc_arraydata: 0x58
+  __DATA_CONST.__got: 0x168
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x840
-  __AUTH_CONST.__objc_const: 0xe80
+  __AUTH_CONST.__cfstring: 0x8e0
+  __AUTH_CONST.__objc_const: 0xf10
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0xe0
-  __DATA.__data: 0x160
+  __AUTH_CONST.__auth_got: 0x0
+  __DATA.__objc_ivar: 0xec
+  __DATA.__data: 0x170
   __DATA.__bss: 0x30
-  __DATA_DIRTY.__objc_data: 0xa0
+  __DATA_DIRTY.__objc_data: 0x1e0
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: DC120FDD-1027-3E7A-997A-76F0946303BF
-  Functions: 224
-  Symbols:   1003
-  CStrings:  644
+  UUID: EFE210EF-48E1-3868-B3E2-37B05154A8FE
+  Functions: 246
+  Symbols:   1077
+  CStrings:  278
 
Symbols:
+ -[CSReceiverConnection handleCommand:info:connection:].cold.18
+ -[CSReceiverConnection indexWithCascadeData:donation:config:completionHandler:]
+ -[CSReceiverConnection indexWithCascadeData:donation:config:completionHandler:].cold.1
+ -[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:updateDestination:skipIndexCheck:completionHandler:]
+ -[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:updateDestination:skipIndexCheck:completionHandler:].cold.1
+ -[SpotlightReceiverDonation cascadeAttributeSets]
+ -[SpotlightReceiverDonation setCascadeAttributeSets:]
+ -[SpotlightScheduledReceiverConfig setSupportedAppEntitySchemas:]
+ -[SpotlightScheduledReceiverConfig setUnsupportedAppEntitySchemas:]
+ -[SpotlightScheduledReceiverConfig supportedAppEntitySchemas]
+ -[SpotlightScheduledReceiverConfig unsupportedAppEntitySchemas]
+ GCC_except_table100
+ GCC_except_table67
+ GCC_except_table69
+ GCC_except_table71
+ GCC_except_table77
+ GCC_except_table86
+ GCC_except_table99
+ _OBJC_IVAR_$_SpotlightReceiverDonation._cascadeAttributeSets
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._supportedAppEntitySchemas
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._unsupportedAppEntitySchemas
+ _SpotlightScheduledReceiverConfigSupportedAppEntitySchemas
+ _SpotlightScheduledReceiverConfigUnsupportedAppEntitySchemas
+ ___136-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:updateDestination:skipIndexCheck:completionHandler:]_block_invoke
+ ___136-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:updateDestination:skipIndexCheck:completionHandler:]_block_invoke.483
+ ___136-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:updateDestination:skipIndexCheck:completionHandler:]_block_invoke.483.cold.1
+ ___136-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:updateDestination:skipIndexCheck:completionHandler:]_block_invoke.487
+ ___136-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:updateDestination:skipIndexCheck:completionHandler:]_block_invoke.487.cold.1
+ ___136-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:updateDestination:skipIndexCheck:completionHandler:]_block_invoke.490
+ ___136-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:updateDestination:skipIndexCheck:completionHandler:]_block_invoke_2
+ ___136-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:updateDestination:skipIndexCheck:completionHandler:]_block_invoke_2.488
+ ___136-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:updateDestination:skipIndexCheck:completionHandler:]_block_invoke_2.492
+ ___136-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:updateDestination:skipIndexCheck:completionHandler:]_block_invoke_3
+ ___136-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:updateDestination:skipIndexCheck:completionHandler:]_block_invoke_3.494
+ ___54-[CSReceiverConnection handleCommand:info:connection:]_block_invoke.413
+ ___54-[CSReceiverConnection handleCommand:info:connection:]_block_invoke.417
+ ___54-[CSReceiverConnection handleCommand:info:connection:]_block_invoke.417.cold.1
+ ___54-[CSReceiverConnection handleCommand:info:connection:]_block_invoke.417.cold.2
+ ___54-[CSReceiverConnection handleCommand:info:connection:]_block_invoke.cold.1
+ ___54-[CSReceiverConnection handleCommand:info:connection:]_block_invoke.cold.2
+ ___76-[CSReceiverConnection deleteWithFd:offset:size:donation:completionHandler:]_block_invoke.499
+ ___76-[CSReceiverConnection deleteWithFd:offset:size:donation:completionHandler:]_block_invoke.500
+ ___76-[CSReceiverConnection deleteWithFd:offset:size:donation:completionHandler:]_block_invoke_2.502
+ ___79-[CSReceiverConnection indexWithCascadeData:donation:config:completionHandler:]_block_invoke
+ ___79-[CSReceiverConnection indexWithCascadeData:donation:config:completionHandler:]_block_invoke.506
+ ___79-[CSReceiverConnection indexWithCascadeData:donation:config:completionHandler:]_block_invoke.506.cold.1
+ ___79-[CSReceiverConnection indexWithCascadeData:donation:config:completionHandler:]_block_invoke.507
+ ___79-[CSReceiverConnection indexWithCascadeData:donation:config:completionHandler:]_block_invoke.cold.1
+ ___79-[CSReceiverConnection indexWithCascadeData:donation:config:completionHandler:]_block_invoke.cold.2
+ ___79-[CSReceiverConnection indexWithCascadeData:donation:config:completionHandler:]_block_invoke.cold.3
+ ___79-[CSReceiverConnection indexWithCascadeData:donation:config:completionHandler:]_block_invoke.cold.4
+ ___79-[CSReceiverConnection indexWithCascadeData:donation:config:completionHandler:]_block_invoke.cold.5
+ ___79-[CSReceiverConnection indexWithCascadeData:donation:config:completionHandler:]_block_invoke.cold.6
+ ___79-[CSReceiverConnection indexWithCascadeData:donation:config:completionHandler:]_block_invoke_2
+ ___block_descriptor_125_e8_32s40s48s56s64s72s80s88s96r104r112r_e54_v96?0q8r*16{?=*Q{?=IC}}24{?=*Q{?=IC}}48{?=*Q{?=IC}}72ls32l8s40l8s48l8s56l8s64l8s72l8s80l8r96l8s88l8r104l8r112l8
+ ___block_descriptor_157_e8_32s40s48s56s64s72s80s88s96r104r112r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8r96l8s88l8r104l8r112l8
+ ___block_descriptor_48_e8_32s40s_e41_v28?0i8q12"SpotlightReceiverDonation"20ls32l8s40l8
+ ___block_descriptor_52_e8_32s40s_e28_v28?0i8q12"NSDictionary"20ls32l8s40l8
+ ___block_descriptor_64_e8_32s40bs48r56r_e5_v8?0ls40l8r48l8r56l8s32l8
+ ___block_descriptor_64_e8_32s40s48r56r_e35_v16?0"SpotlightReceiverResponse"8lr48l8r56l8s32l8s40l8
+ ___block_descriptor_80_e8_32bs40r48r56r_e5_v8?0ls32l8r40l8r48l8r56l8
+ ___block_descriptor_80_e8_32s40s48s56s64r72r_e5_v8?0ls32l8r64l8s40l8s48l8s56l8r72l8
+ ___block_descriptor_90_e8_32s40s48s56s64r72r80r_e35_v16?0"SpotlightReceiverResponse"8lr64l8r72l8r80l8s32l8s40l8s48l8s56l8
+ ___block_literal_global.486
+ ___block_literal_global.581
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$attributeForKey:
+ _objc_msgSend$attributeSet
+ _objc_msgSend$cascadeAttributeSets
+ _objc_msgSend$decodeObjectOfClass:forKey:
+ _objc_msgSend$finishDecoding
+ _objc_msgSend$indexWithCascadeData:donation:config:completionHandler:
+ _objc_msgSend$indexWithFd:offset:size:donation:additionalAttributes:config:updateDestination:skipIndexCheck:completionHandler:
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$setCascadeAttributeSets:
+ _objc_msgSend$supportedAppEntitySchemas
+ _objc_msgSend$unsupportedAppEntitySchemas
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x9
+ _xpc_dictionary_get_bool
- -[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]
- -[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:].cold.1
- GCC_except_table63
- GCC_except_table72
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_9
- ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke
- ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke.453
- ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke.453.cold.1
- ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke.457
- ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke_2
- ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke_2.458
- ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke_3
- ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke_3.460
- ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke_4
- ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke_5
- ___54-[CSReceiverConnection handleCommand:info:connection:]_block_invoke.387
- ___76-[CSReceiverConnection deleteWithFd:offset:size:donation:completionHandler:]_block_invoke.467
- ___76-[CSReceiverConnection deleteWithFd:offset:size:donation:completionHandler:]_block_invoke.468
- ___76-[CSReceiverConnection deleteWithFd:offset:size:donation:completionHandler:]_block_invoke_2.470
- ___block_descriptor_115_e8_32s40s48s56s64s72s80s88s96r104r_e54_v96?0q8r*16{?=*Q{?=IC}}24{?=*Q{?=IC}}48{?=*Q{?=IC}}72ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8r96l8r104l8
- ___block_descriptor_147_e8_32s40s48s56s64s72s80s88s96r104r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8r96l8r104l8
- ___block_descriptor_52_e8_32s40s_e11_v20?0i8q12ls32l8s40l8
- ___block_descriptor_72_e8_32bs40r48r_e5_v8?0ls32l8r40l8r48l8
- ___block_descriptor_80_e8_32s40s48s56s64r72r_e35_v16?0"SpotlightReceiverResponse"8lr64l8r72l8s32l8s40l8s48l8s56l8
- ___block_literal_global.456
- ___block_literal_global.543
- _objc_msgSend$indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:
- _objc_retain_x24
CStrings:
+ "### SCHEDULED RECEIVER Cascade attribute set missing _kMDItemExternalID"
+ "### SCHEDULED RECEIVER deserialized %ld Cascade items"
+ "### SCHEDULED RECEIVER exception during Cascade deserialization: %@"
+ "### SCHEDULED RECEIVER exception encoding Cascade updates: %@"
+ "### SCHEDULED RECEIVER exception encoding redirected updates: %@"
+ "### SCHEDULED RECEIVER exception serializing redirected updates: %@"
+ "### SCHEDULED RECEIVER exception serializing updates: %@"
+ "### SCHEDULED RECEIVER failed to create attribute set unarchiver: %@"
+ "### SCHEDULED RECEIVER failed to create unarchiver: %@"
+ "### SCHEDULED RECEIVER failed to deserialize Cascade attribute set"
+ "### SCHEDULED RECEIVER failed to encode Cascade updates: %@"
+ "### SCHEDULED RECEIVER failed to encode redirected updates: %@"
+ "### SCHEDULED RECEIVER failed to serialize redirected update: %@"
+ "### SCHEDULED RECEIVER failed to serialize update: %@"
+ "### SCHEDULED RECEIVER indexWithCascadeData invalid request %@"
+ "### SCHEDULED RECEIVER missing Cascade data"
+ "### SCHEDULED RECEIVER no Cascade attribute sets found"
+ "### SCHEDULED RECEIVER no valid Cascade items after deserialization"
+ "### SCHEDULED RECEIVER processing Cascade items"
+ "### SCHEDULED RECEIVER processing add/updated batch (updateDestination=%llu, skipCheck=%d)"
+ "### SCHEDULED RECEIVER sending back %ld Cascade updates"
+ "### SCHEDULED RECEIVER sending back %ld redirected updates"
+ "### SCHEDULED RECEIVER serialized %ld Cascade updates to send back"
+ "### SCHEDULED RECEIVER serialized %ld updates for redirect"
+ "### SCHEDULED RECEIVER skipping index check, using all %ld identifiers"
+ "%@.%@.cascade"
+ "%@: %@ %@ %@ %@ %@ %@ %@ %@\n\treq:%@\n\topt:%@\n\texc:%@\n\tdon:%@\n\tbundles:%@\n\tdisableBundles:%@\n\tdomains:%@\n\tdisableDomains:%@\n\tcontentTypes:%@\n\tdisableTypes:%@\n\tappEntitySchemas:%@\n\tdisableAppEntitySchemas:%@\n\tquery:%@\n\t"
+ "SpotlightReceiver"
+ "_kMDItemAppEntitySchema"
+ "_kMDItemAppEntityTypeIdentifier"
+ "catrs"
+ "catrs-size"
+ "caupd"
+ "caupd-size"
+ "skipchk"
+ "supportedAppEntitySchemas"
+ "unsupportedAppEntitySchemas"
+ "updst"
+ "v28@?0i8q12@\"NSDictionary\"20"
+ "v28@?0i8q12@\"SpotlightReceiverDonation\"20"
- "### SCHEDULED RECEIVER processing add/updated batch"
- "%@: %@ %@ %@ %@ %@ %@ %@ %@\n\treq:%@\n\topt:%@\n\texc:%@\n\tdon:%@\n\tbundles:%@\n\tdisableBundles:%@\n\tdomains:%@\n\tdisableDomains:%@\n\tcontentTypes:%@\n\tdisableTypes:%@\n\tquery:%@\n\t"
- ".cxx_destruct"
- "@\"<SpotlightReceiverInfo>\""
- "@\"NSArray\""
- "@\"NSDictionary\""
- "@\"NSError\""
- "@\"NSMutableDictionary\""
- "@\"NSNumber\""
- "@\"NSObject<SpotlightDaemonClient>\""
- "@\"NSObject<SpotlightReceiver>\""
- "@\"NSObject<SpotlightScheduledReceiver>\""
- "@\"NSString\""
- "@\"SpotlightReceiverDonation\""
- "@16@0:8"
- "@24@0:8@16"
- "@32@0:8@16@24"
- "@40@0:8@16@24@32"
- "@40@0:8q16@24@32"
- "B"
- "B16@0:8"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "B40@0:8r*16@24@32"
- "CSReceiverConnection"
- "INIntentClassNames"
- "Internal"
- "Q"
- "Q16@0:8"
- "SpotlightDaemonClient"
- "SpotlightDaemonClientConnection"
- "SpotlightReceiverDonation"
- "SpotlightReceiverResponse"
- "SpotlightReceiverUpdate"
- "SpotlightResources"
- "SpotlightScheduledReceiverConfig"
- "T@\"<SpotlightReceiverInfo>\",R,N,V_info"
- "T@\"NSArray\",&,N,V_identifiers"
- "T@\"NSArray\",&,N,V_items"
- "T@\"NSArray\",C,N,V_INIntentClassNames"
- "T@\"NSArray\",C,N,V_bundleIDs"
- "T@\"NSArray\",C,N,V_contentTypes"
- "T@\"NSArray\",C,N,V_donationAttributes"
- "T@\"NSArray\",C,N,V_excludeAttributes"
- "T@\"NSArray\",C,N,V_optionalAttributes"
- "T@\"NSArray\",C,N,V_processes"
- "T@\"NSArray\",C,N,V_requiredAttributes"
- "T@\"NSArray\",C,N,V_supportedBundles"
- "T@\"NSArray\",C,N,V_supportedContentTypes"
- "T@\"NSArray\",C,N,V_supportedDomainIdentifiers"
- "T@\"NSArray\",C,N,V_unsupportedBundles"
- "T@\"NSArray\",C,N,V_unsupportedContentTypes"
- "T@\"NSArray\",C,N,V_unsupportedDomainIdentifiers"
- "T@\"NSArray\",R,N"
- "T@\"NSArray\",R,N,V_defaultAttributes"
- "T@\"NSDictionary\",R,N,V_attributes"
- "T@\"NSError\",C,N,V_error"
- "T@\"NSNumber\",C,N,V_versionValue"
- "T@\"NSNumber\",R,N"
- "T@\"NSObject<SpotlightDaemonClient>\",R,N,V_spotlightDaemonClient"
- "T@\"NSObject<SpotlightReceiver>\",R,N,V_receiver"
- "T@\"NSObject<SpotlightScheduledReceiver>\",R,N,V_scheduledReceiver"
- "T@\"NSString\",C,N,V_bundleIdentifier"
- "T@\"NSString\",C,N,V_configName"
- "T@\"NSString\",C,N,V_journalCookie"
- "T@\"NSString\",C,N,V_name"
- "T@\"NSString\",C,N,V_priority"
- "T@\"NSString\",C,N,V_protectionClass"
- "T@\"NSString\",C,N,V_supportedQuery"
- "T@\"NSString\",C,N,V_unsupportedQuery"
- "T@\"NSString\",C,N,V_versionName"
- "T@\"NSString\",R,N"
- "T@\"SpotlightReceiverDonation\",R,N,V_donation"
- "TB,N,V_needsDeletes"
- "TB,N,V_needsHTML"
- "TB,N,V_needsLanguage"
- "TB,N,V_needsText"
- "TB,N,V_needsUserActivities"
- "TB,R,N"
- "TQ,N,V_serialNumber"
- "Ti,R,N,V_supportedJobs"
- "Tq,N,V_donationType"
- "Tq,N,V_indexType"
- "Tq,N,V_options"
- "Tq,N,V_status"
- "Tq,R,N,V_status"
- "UTF8String"
- "_INIntentClassNames"
- "_attributes"
- "_bundleIDs"
- "_bundleIdentifier"
- "_configDescription"
- "_configName"
- "_configs"
- "_contentTypes"
- "_defaultAttributes"
- "_donation"
- "_donationAttributes"
- "_donationType"
- "_error"
- "_errorAttributeName"
- "_errorCodeAttributeName"
- "_excludeAttributes"
- "_fetchAttributes"
- "_identifiers"
- "_indexType"
- "_indexes"
- "_info"
- "_initWithName:protectionClass:bundleIdentifier:options:"
- "_items"
- "_journalCookie"
- "_lock"
- "_name"
- "_needsDeletes"
- "_needsHTML"
- "_needsLanguage"
- "_needsText"
- "_needsUserActivities"
- "_optionalAttributes"
- "_options"
- "_priority"
- "_processes"
- "_protectionClass"
- "_receiver"
- "_requiredAttributes"
- "_scheduledReceiver"
- "_serialNumber"
- "_spotlightDaemonClient"
- "_status"
- "_supportedBundles"
- "_supportedContentTypes"
- "_supportedDomainIdentifiers"
- "_supportedJobs"
- "_supportedQuery"
- "_unsupportedBundles"
- "_unsupportedContentTypes"
- "_unsupportedDomainIdentifiers"
- "_unsupportedQuery"
- "_updateAttributes"
- "_updates"
- "_versionName"
- "_versionValue"
- "addAttributesFromDictionary:"
- "addClientConnectionIfAllowedForConnection:"
- "addConfiguration:"
- "addInteraction:bundleID:protectionClass:"
- "addInteractions:bundleID:protectionClass:"
- "addObject:"
- "addObjectsFromArray:"
- "addOrUpdateSearchableItems:bundleID:"
- "addOrUpdateSearchableItems:bundleID:name:completionHandler:"
- "addUserAction:withItem:"
- "addUserActions:bundleID:protectionClass:"
- "allKeys"
- "allObjects"
- "allValues"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "array"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "attributes"
- "boolValue"
- "bundleIDs"
- "bundleIdentifier"
- "bytes"
- "code"
- "configForIdentifier:"
- "configName"
- "conformsToProtocol:"
- "containingAppForPlugInWithPid:"
- "containingBundleRecord"
- "containsObject:"
- "contentTypes"
- "copy"
- "copyNSArrayFromXPCArray:"
- "copyNSStringArrayFromXPCArray:"
- "copyNSStringForKey:fromXPCDictionary:"
- "copyNSStringOrDictArrayFromXPCArray:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "data"
- "dataWithBytesNoCopy:length:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "dataWrapperForKey:sizeKey:fromXPCDictionary:"
- "dateWithTimeIntervalSince1970:"
- "decodeObject:"
- "decodeObjectOfClasses:forKey:"
- "defaultAttributes"
- "defaultManager"
- "deleteAllInteractionsWithBundleID:protectionClass:"
- "deleteAllSearchableItemsWithBundleID:"
- "deleteAllUserActivities:"
- "deleteFromBundle:sinceDate:domains:deletes:"
- "deleteInteractionsWithGroupIdentifiers:bundleID:protectionClass:"
- "deleteInteractionsWithIdentifiers:bundleID:protectionClass:"
- "deleteSearchableItemsSinceDate:bundleID:"
- "deleteSearchableItemsWithDomainIdentifiers:bundleID:"
- "deleteSearchableItemsWithIdentifiers:bundleID:"
- "deleteUserActivitiesWithPersistentIdentifiers:bundleID:"
- "deleteWithFd:offset:size:donation:completionHandler:"
- "description"
- "dictionary:setStringArray:forKey:"
- "dictionary:setStringOrDictionaryArray:forKey:"
- "dictionaryWithCapacity:"
- "dictionaryWithContentsOfURL:error:"
- "domain"
- "donateRelevantActions:bundleID:"
- "donateRelevantShortcuts:bundleID:"
- "donation"
- "donationType"
- "enableDebuggability"
- "encodeURL:withSandboxExtensionData:"
- "enumerateObjectsUsingBlock:"
- "enumerateUpdatesUsingBlock:"
- "error"
- "errorAttributeName"
- "errorCodeAttributeName"
- "fetchAttributes"
- "fetchableIdentifiersFromDonation:additionalAttributes:config:"
- "fileExistsAtPath:"
- "fileSystemRepresentation"
- "fileURLWithPath:"
- "firstObject"
- "handleCommand:info:connection:"
- "handleSetup:"
- "hasPrefix:"
- "i16@0:8"
- "i24@0:8@16"
- "i32@0:8@16@24"
- "i40@0:8@16@24@32"
- "i48@0:8@16@24@32@40"
- "identifier"
- "identifiers"
- "incrementAttributeValue:forKey:"
- "indexForBundleID:protectionClass:"
- "indexFromBundle:protectionClass:items:itemsContent:"
- "indexSearchableItems:completionHandler:"
- "indexType"
- "indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:"
- "info"
- "informationForPlugInWithPid:"
- "init"
- "initForReadingFromData:error:"
- "initMachServiceListenerWithName:"
- "initWithAttributes:"
- "initWithBundleIdentifier:error:"
- "initWithClient:forServiceName:"
- "initWithConfigurationValues:"
- "initWithData:"
- "initWithDonation:"
- "initWithFileURL:andError:"
- "initWithItems:itemsContent:"
- "initWithKeyName:searchable:searchableByDefault:unique:multiValued:"
- "initWithName:protectionClass:bundleIdentifier:"
- "initWithReceiver:forServiceName:"
- "initWithScheduledReceiver:forServiceName:"
- "initWithStatus:info:attributes:"
- "initWithUniqueIdentifier:domainIdentifier:attributeSet:"
- "initWithVersionName:versionValue:"
- "isEqualToNumber:"
- "isEqualToString:"
- "items"
- "journalCookie"
- "length"
- "lostClientConnection:error:"
- "mutableCopy"
- "numberWithBool:"
- "numberWithInteger:"
- "obj"
- "objectAtIndexedSubscript:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "options"
- "path"
- "processDonation:completionHandler:"
- "protectionClass"
- "provideDataForBundleID:protectionClass:itemIdentifier:typeIdentifier:options:completionHandler:"
- "provideFileURLForBundleID:protectionClass:itemIdentifier:typeIdentifier:options:completionHandler:"
- "provideFileURLsForBundleID:protectionClass:itemIdentifiers:typeIdentifier:options:completionHandler:"
- "purgeFromBundle:identifiers:"
- "purgeSearchableItemsWithIdentifiers:bundleID:"
- "q"
- "q16@0:8"
- "queue"
- "reason"
- "receiver"
- "reindexAllItemsForBundleID:protectionClass:acknowledgementHandler:"
- "reindexAllItemsForBundleID:protectionClass:reason:acknowledgementHandler:"
- "reindexItemsWithIdentifiers:bundleID:protectionClass:acknowledgementHandler:"
- "removeAllObjects"
- "removeObject:"
- "requireBacklog"
- "requirePriority"
- "reset"
- "resume"
- "scheduledReceiver"
- "searchableItemsDidUpdate:mask:"
- "searchableItemsMediaAnalysisComplete:"
- "serialNumber"
- "serviceName"
- "setAttribute:forKey:"
- "setAttributeSet:"
- "setBackingStore:"
- "setBundleID:"
- "setBundleIDs:"
- "setBundleIdentifier:"
- "setConfigName:"
- "setContentTypes:"
- "setDonationAttributes:"
- "setDonationType:"
- "setError:"
- "setExcludeAttributes:"
- "setHTMLContentData:"
- "setINIntentClassNames:"
- "setIdentifiers:"
- "setIndexType:"
- "setIsUpdate:"
- "setItems:"
- "setJournalCookie:"
- "setName:"
- "setNeedsDeletes:"
- "setNeedsHTML:"
- "setNeedsLanguage:"
- "setNeedsText:"
- "setNeedsUserActivities:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setOptionalAttributes:"
- "setOptions:"
- "setPriority:"
- "setProcesses:"
- "setProtection:"
- "setProtectionClass:"
- "setRequiredAttributes:"
- "setSerialNumber:"
- "setStatus:"
- "setSupportedBundles:"
- "setSupportedContentTypes:"
- "setSupportedDomainIdentifiers:"
- "setSupportedQuery:"
- "setTextContent:"
- "setUnsupportedBundles:"
- "setUnsupportedContentTypes:"
- "setUnsupportedDomainIdentifiers:"
- "setUnsupportedQuery:"
- "setUpdate:forItem:"
- "setValue:forCustomKey:"
- "setVersionName:"
- "setVersionValue:"
- "setWithObject:"
- "setWithObjects:"
- "slowFetchAttributes:protectionClass:bundleID:identifiers:completionHandler:"
- "spotlightDaemonClient"
- "startListener"
- "stringByReplacingOccurrencesOfString:withString:"
- "stringWithFormat:"
- "stringWithUTF8String:"
- "supportedBundleIDs"
- "supportedDomainIdentifiers"
- "supportedINIntentClassNames"
- "supportedJobs"
- "supportsDeletes"
- "suspend"
- "unarchivedObjectOfClass:fromData:error:"
- "uniqueIdentifier"
- "unsupportedDomainIdentifiers"
- "v16@0:8"
- "v20@0:8B16"
- "v20@?0i8q12"
- "v24@0:8@\"NSArray\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8Q16"
- "v24@0:8q16"
- "v32@0:8@\"NSArray\"16q24"
- "v32@0:8@16q24"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?>32"
- "v40@0:8@16@24@?32"
- "v48@0:8@\"NSArray\"16@\"NSString\"24@\"NSString\"32@?<v@?>40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?>40"
- "v48@0:8@16@24@32@?40"
- "v52@0:8i16Q20Q28@36@?44"
- "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSArray\"32@\"NSString\"40q48@?<v@?@\"NSArray\"@\"NSError\">56"
- "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40q48@?<v@?@\"NSData\"@\"NSError\">56"
- "v64@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40q48@?<v@?@\"NSURL\"@\"NSError\">56"
- "v64@0:8@16@24@32@40q48@?56"
- "v68@0:8i16Q20Q28@36@44@52@?60"
- "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
