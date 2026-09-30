## SpotlightReceiver

> `/System/Library/PrivateFrameworks/SpotlightReceiver.framework/SpotlightReceiver`

```diff

-2333.50.1.0.0
-  __TEXT.__text: 0x44f0
-  __TEXT.__auth_stubs: 0x5e0
-  __TEXT.__objc_methlist: 0x204
-  __TEXT.__const: 0xa0
-  __TEXT.__gcc_except_tab: 0x1c8
-  __TEXT.__cstring: 0x262
-  __TEXT.__oslogstring: 0x3a1
-  __TEXT.__unwind_info: 0xf8
-  __TEXT.__objc_classname: 0x4f
-  __TEXT.__objc_methname: 0xce5
-  __TEXT.__objc_methtype: 0x30e
-  __TEXT.__objc_stubs: 0xb20
-  __DATA_CONST.__got: 0xf0
-  __DATA_CONST.__const: 0x190
-  __DATA_CONST.__objc_classlist: 0x10
+2374.0.1.0.0
+  __TEXT.__text: 0x8adc
+  __TEXT.__auth_stubs: 0x750
+  __TEXT.__objc_methlist: 0x624
+  __TEXT.__const: 0xf0
+  __TEXT.__gcc_except_tab: 0x530
+  __TEXT.__cstring: 0x838
+  __TEXT.__oslogstring: 0x595
+  __TEXT.__unwind_info: 0x190
+  __TEXT.__objc_classname: 0x93
+  __TEXT.__objc_methname: 0x1cbe
+  __TEXT.__objc_methtype: 0x3e5
+  __TEXT.__objc_stubs: 0x1500
+  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__const: 0x2e8
+  __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x330
+  __DATA_CONST.__objc_selrefs: 0x6c8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x300
-  __AUTH_CONST.__cfstring: 0x80
-  __AUTH_CONST.__objc_const: 0x2a0
-  __DATA.__objc_ivar: 0x18
-  __DATA.__data: 0x80
+  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__objc_arraydata: 0x48
+  __AUTH_CONST.__auth_got: 0x3b8
+  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__cfstring: 0x7a0
+  __AUTH_CONST.__objc_const: 0xb40
+  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0xb0
+  __DATA.__data: 0x170
+  __DATA.__bss: 0x30
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/PlugInKit.framework/PlugInKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E4461C34-E62E-3437-BF4C-8888246157C3
-  Functions: 77
-  Symbols:   420
-  CStrings:  224
+  UUID: 43760202-42F5-38E2-9023-DF4F46E7ED77
+  Functions: 189
+  Symbols:   864
+  CStrings:  574
 
Symbols:
+ -[CSReceiverConnection addConfiguration:]
+ -[CSReceiverConnection configForIdentifier:]
+ -[CSReceiverConnection configs]
+ -[CSReceiverConnection deleteWithFd:offset:size:donation:completionHandler:]
+ -[CSReceiverConnection deleteWithFd:offset:size:donation:completionHandler:].cold.1
+ -[CSReceiverConnection deleteWithFd:offset:size:donation:completionHandler:].cold.2
+ -[CSReceiverConnection enableDebuggability]
+ -[CSReceiverConnection enableDebuggability].cold.1
+ -[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]
+ -[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:].cold.1
+ -[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:].cold.2
+ -[CSReceiverConnection initWithScheduledReceiver:forServiceName:]
+ -[CSReceiverConnection initWithScheduledReceiver:forServiceName:].cold.1
+ -[CSReceiverConnection scheduledReceiver]
+ -[SpotlightReceiverDonation .cxx_destruct]
+ -[SpotlightReceiverDonation bundleIdentifier]
+ -[SpotlightReceiverDonation configName]
+ -[SpotlightReceiverDonation donationType]
+ -[SpotlightReceiverDonation identifiers]
+ -[SpotlightReceiverDonation indexType]
+ -[SpotlightReceiverDonation items]
+ -[SpotlightReceiverDonation journalCookie]
+ -[SpotlightReceiverDonation protectionClass]
+ -[SpotlightReceiverDonation serialNumber]
+ -[SpotlightReceiverDonation setBundleIdentifier:]
+ -[SpotlightReceiverDonation setConfigName:]
+ -[SpotlightReceiverDonation setDonationType:]
+ -[SpotlightReceiverDonation setIdentifiers:]
+ -[SpotlightReceiverDonation setIndexType:]
+ -[SpotlightReceiverDonation setItems:]
+ -[SpotlightReceiverDonation setJournalCookie:]
+ -[SpotlightReceiverDonation setProtectionClass:]
+ -[SpotlightReceiverDonation setSerialNumber:]
+ -[SpotlightScheduledReceiverConfig .cxx_destruct]
+ -[SpotlightScheduledReceiverConfig _updateAttributes]
+ -[SpotlightScheduledReceiverConfig defaultAttributes]
+ -[SpotlightScheduledReceiverConfig description]
+ -[SpotlightScheduledReceiverConfig donationAttributes]
+ -[SpotlightScheduledReceiverConfig excludeAttributes]
+ -[SpotlightScheduledReceiverConfig fetchAttributes]
+ -[SpotlightScheduledReceiverConfig identifier]
+ -[SpotlightScheduledReceiverConfig initWithConfigurationValues:]
+ -[SpotlightScheduledReceiverConfig name]
+ -[SpotlightScheduledReceiverConfig needsDeletes]
+ -[SpotlightScheduledReceiverConfig needsHTML]
+ -[SpotlightScheduledReceiverConfig needsLanguage]
+ -[SpotlightScheduledReceiverConfig needsText]
+ -[SpotlightScheduledReceiverConfig needsUserActivities]
+ -[SpotlightScheduledReceiverConfig optionalAttributes]
+ -[SpotlightScheduledReceiverConfig options]
+ -[SpotlightScheduledReceiverConfig priority]
+ -[SpotlightScheduledReceiverConfig processes]
+ -[SpotlightScheduledReceiverConfig requireBacklog]
+ -[SpotlightScheduledReceiverConfig requirePriority]
+ -[SpotlightScheduledReceiverConfig requiredAttributes]
+ -[SpotlightScheduledReceiverConfig setDonationAttributes:]
+ -[SpotlightScheduledReceiverConfig setExcludeAttributes:]
+ -[SpotlightScheduledReceiverConfig setName:]
+ -[SpotlightScheduledReceiverConfig setNeedsDeletes:]
+ -[SpotlightScheduledReceiverConfig setNeedsHTML:]
+ -[SpotlightScheduledReceiverConfig setNeedsLanguage:]
+ -[SpotlightScheduledReceiverConfig setNeedsText:]
+ -[SpotlightScheduledReceiverConfig setNeedsUserActivities:]
+ -[SpotlightScheduledReceiverConfig setOptionalAttributes:]
+ -[SpotlightScheduledReceiverConfig setOptions:]
+ -[SpotlightScheduledReceiverConfig setPriority:]
+ -[SpotlightScheduledReceiverConfig setProcesses:]
+ -[SpotlightScheduledReceiverConfig setRequiredAttributes:]
+ -[SpotlightScheduledReceiverConfig setSupportedBundles:]
+ -[SpotlightScheduledReceiverConfig setSupportedContentTypes:]
+ -[SpotlightScheduledReceiverConfig setSupportedDomainIdentifiers:]
+ -[SpotlightScheduledReceiverConfig setSupportedQuery:]
+ -[SpotlightScheduledReceiverConfig setTrackingAttributes:]
+ -[SpotlightScheduledReceiverConfig setUnsupportedBundles:]
+ -[SpotlightScheduledReceiverConfig setUnsupportedContentTypes:]
+ -[SpotlightScheduledReceiverConfig setUnsupportedDomainIdentifiers:]
+ -[SpotlightScheduledReceiverConfig setUnsupportedQuery:]
+ -[SpotlightScheduledReceiverConfig setVersionName:]
+ -[SpotlightScheduledReceiverConfig setVersionValue:]
+ -[SpotlightScheduledReceiverConfig supportedBundles]
+ -[SpotlightScheduledReceiverConfig supportedContentTypes]
+ -[SpotlightScheduledReceiverConfig supportedDomainIdentifiers]
+ -[SpotlightScheduledReceiverConfig supportedQuery]
+ -[SpotlightScheduledReceiverConfig supportsDeletes]
+ -[SpotlightScheduledReceiverConfig supportsUpdates]
+ -[SpotlightScheduledReceiverConfig trackingAttributes]
+ -[SpotlightScheduledReceiverConfig unsupportedBundles]
+ -[SpotlightScheduledReceiverConfig unsupportedContentTypes]
+ -[SpotlightScheduledReceiverConfig unsupportedDomainIdentifiers]
+ -[SpotlightScheduledReceiverConfig unsupportedQuery]
+ -[SpotlightScheduledReceiverConfig versionName]
+ -[SpotlightScheduledReceiverConfig versionValue]
+ GCC_except_table137
+ GCC_except_table66
+ GCC_except_table74
+ GCC_except_table82
+ _CFGetTypeID
+ _CFStringGetTypeID
+ _MDJournalReaderMDPlistObjectCopy
+ _MDJournalReaderProcessRecordBatchWithBytes
+ _OBJC_CLASS_$_CSSearchableIndex
+ _OBJC_CLASS_$_CSSearchableItemAttributeSet
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSObject
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_SpotlightReceiverDonation
+ _OBJC_CLASS_$_SpotlightScheduledReceiverConfig
+ _OBJC_IVAR_$_CSReceiverConnection._configs
+ _OBJC_IVAR_$_CSReceiverConnection._scheduledReceiver
+ _OBJC_IVAR_$_SpotlightReceiverDonation._bundleIdentifier
+ _OBJC_IVAR_$_SpotlightReceiverDonation._configName
+ _OBJC_IVAR_$_SpotlightReceiverDonation._donationType
+ _OBJC_IVAR_$_SpotlightReceiverDonation._identifiers
+ _OBJC_IVAR_$_SpotlightReceiverDonation._indexType
+ _OBJC_IVAR_$_SpotlightReceiverDonation._items
+ _OBJC_IVAR_$_SpotlightReceiverDonation._journalCookie
+ _OBJC_IVAR_$_SpotlightReceiverDonation._protectionClass
+ _OBJC_IVAR_$_SpotlightReceiverDonation._serialNumber
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._configDescription
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._defaultAttributes
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._donationAttributes
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._excludeAttributes
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._fetchAttributes
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._name
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._needsDeletes
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._needsHTML
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._needsLanguage
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._needsText
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._needsUserActivities
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._optionalAttributes
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._options
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._priority
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._processes
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._requiredAttributes
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._supportedBundles
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._supportedContentTypes
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._supportedDomainIdentifiers
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._supportedQuery
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._trackingAttributes
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._unsupportedBundles
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._unsupportedContentTypes
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._unsupportedDomainIdentifiers
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._unsupportedQuery
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._versionName
+ _OBJC_IVAR_$_SpotlightScheduledReceiverConfig._versionValue
+ _OBJC_METACLASS_$_SpotlightReceiverDonation
+ _OBJC_METACLASS_$_SpotlightScheduledReceiverConfig
+ _SpotlightScheduledReceiverConfigDonationAttributes
+ _SpotlightScheduledReceiverConfigExcludeAttributes
+ _SpotlightScheduledReceiverConfigIncludeDeletedItems
+ _SpotlightScheduledReceiverConfigIncludeLanguage
+ _SpotlightScheduledReceiverConfigIncludeUpdatedItems
+ _SpotlightScheduledReceiverConfigName
+ _SpotlightScheduledReceiverConfigNeedsDeletes
+ _SpotlightScheduledReceiverConfigNeedsHTML
+ _SpotlightScheduledReceiverConfigNeedsLanguage
+ _SpotlightScheduledReceiverConfigNeedsText
+ _SpotlightScheduledReceiverConfigNeedsUserActivities
+ _SpotlightScheduledReceiverConfigOptionalAttributes
+ _SpotlightScheduledReceiverConfigPriority
+ _SpotlightScheduledReceiverConfigProcesses
+ _SpotlightScheduledReceiverConfigRequireBacklogItems
+ _SpotlightScheduledReceiverConfigRequirePriorityItems
+ _SpotlightScheduledReceiverConfigRequiredAttributes
+ _SpotlightScheduledReceiverConfigSupportedBundles
+ _SpotlightScheduledReceiverConfigSupportedContentTypes
+ _SpotlightScheduledReceiverConfigSupportedDomains
+ _SpotlightScheduledReceiverConfigSupportedQuery
+ _SpotlightScheduledReceiverConfigTrackingAttributes
+ _SpotlightScheduledReceiverConfigUnsupportedBundles
+ _SpotlightScheduledReceiverConfigUnsupportedContentTypes
+ _SpotlightScheduledReceiverConfigUnsupportedDomains
+ _SpotlightScheduledReceiverConfigUnsupportedQuery
+ _SpotlightScheduledReceiverConfigVersionName
+ _SpotlightScheduledReceiverConfigVersionValue
+ _SpotlightScheduledReceiverConnectionUIDKey
+ _SpotlightScheduledReceiverConnectionUIDKeyCStr
+ _SpotlightScheduledReceiverRegister
+ _SpotlightScheduledReceiverRegister.onceToken
+ _SpotlightScheduledReceiverRegisterConfigs
+ _SpotlightScheduledReceiverRegisterWithConfig
+ __MDPlistDataGetBytePtr
+ __MDPlistDictionaryGetPlistObjectForKey
+ __MDPlistGetRootPlistObjectFromBytes
+ __MDPlistNumberGetIntValue
+ __MDPlistStringGetValue
+ __NSConcreteGlobalBlock
+ __OBJC_$_INSTANCE_METHODS_SpotlightReceiverDonation
+ __OBJC_$_INSTANCE_METHODS_SpotlightScheduledReceiverConfig
+ __OBJC_$_INSTANCE_VARIABLES_SpotlightReceiverDonation
+ __OBJC_$_INSTANCE_VARIABLES_SpotlightScheduledReceiverConfig
+ __OBJC_$_PROP_LIST_SpotlightReceiverDonation
+ __OBJC_$_PROP_LIST_SpotlightScheduledReceiverConfig
+ __OBJC_CLASS_RO_$_SpotlightReceiverDonation
+ __OBJC_CLASS_RO_$_SpotlightScheduledReceiverConfig
+ __OBJC_METACLASS_RO_$_SpotlightReceiverDonation
+ __OBJC_METACLASS_RO_$_SpotlightScheduledReceiverConfig
+ ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke
+ ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke.458
+ ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke.458.cold.1
+ ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke.462
+ ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke_2
+ ___103-[CSReceiverConnection indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:]_block_invoke_2.463
+ ___43-[CSReceiverConnection enableDebuggability]_block_invoke
+ ___54-[CSReceiverConnection handleCommand:info:connection:]_block_invoke
+ ___54-[CSReceiverConnection handleCommand:info:connection:]_block_invoke.398
+ ___76-[CSReceiverConnection deleteWithFd:offset:size:donation:completionHandler:]_block_invoke
+ ___76-[CSReceiverConnection deleteWithFd:offset:size:donation:completionHandler:]_block_invoke.469
+ ___76-[CSReceiverConnection deleteWithFd:offset:size:donation:completionHandler:]_block_invoke.470
+ ___76-[CSReceiverConnection deleteWithFd:offset:size:donation:completionHandler:]_block_invoke_2
+ ___76-[CSReceiverConnection deleteWithFd:offset:size:donation:completionHandler:]_block_invoke_3
+ ___NSArray0__struct
+ ___SpotlightScheduledReceiverRegister_block_invoke
+ ___SpotlightScheduledReceiverRegister_block_invoke.cold.1
+ ___block_descriptor_104_e8_32s40s48s56r64r_e5_v8?0ls32l8s40l8s48l8r56l8r64l8
+ ___block_descriptor_131_e8_32s40s48s56s64s72s80r88r_e5_v8?0lr80l8s32l8s40l8s48l8s56l8s64l8s72l8r88l8
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e19_v32?0{?=*Q{?=IC}}8ls32l8
+ ___block_descriptor_44_e8_32r_e20_v20?0i8"NSError"12lr32l8
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8lr40l8s32l8
+ ___block_descriptor_64_e8_32s40s48s56r_e29_v52?0q8r*16{?=*Q{?=IC}}24B48ls32l8s40l8s48l8r56l8
+ ___block_descriptor_99_e8_32s40s48s56s64s72s80r88r_e54_v96?0q8r*16{?=*Q{?=IC}}24{?=*Q{?=IC}}48{?=*Q{?=IC}}72lr80l8s32l8s40l8s48l8s56l8s64l8s72l8r88l8
+ ___block_literal_global
+ ___block_literal_global.461
+ ___block_literal_global.538
+ ___getScheduledReceiverConfigPathForService_block_invoke
+ __os_feature_enabled_impl
+ _close
+ _dispatch_group_async
+ _dispatch_group_wait
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _dispatch_queue_attr_make_with_qos_class
+ _dispatch_queue_create
+ _dispatch_time
+ _enableDebuggability.onceToken
+ _enableDebuggability.sDebugEnabled
+ _getScheduledReceiverConfigPathForService.onceToken
+ _getScheduledReceiverConfigPathForService.sReceiverConfigs
+ _indexTypeForValue
+ _mmap
+ _munmap
+ _objc_msgSend$_initWithName:protectionClass:bundleIdentifier:options:
+ _objc_msgSend$_updateAttributes
+ _objc_msgSend$addConfiguration:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$addOrUpdateSearchableItems:bundleID:name:completionHandler:
+ _objc_msgSend$allObjects
+ _objc_msgSend$allValues
+ _objc_msgSend$capitalizedString
+ _objc_msgSend$configForIdentifier:
+ _objc_msgSend$configName
+ _objc_msgSend$configs
+ _objc_msgSend$containsObject:
+ _objc_msgSend$copyNSStringOrDictArrayFromXPCArray:
+ _objc_msgSend$deleteWithFd:offset:size:donation:completionHandler:
+ _objc_msgSend$dictionary:setStringOrDictionaryArray:forKey:
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$dictionaryWithContentsOfURL:error:
+ _objc_msgSend$donationAttributes
+ _objc_msgSend$enableDebuggability
+ _objc_msgSend$excludeAttributes
+ _objc_msgSend$fetchAttributes
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$fileURLWithPath:
+ _objc_msgSend$handleDonation:completionHandler:
+ _objc_msgSend$identifier
+ _objc_msgSend$indexSearchableItems:completionHandler:
+ _objc_msgSend$indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:
+ _objc_msgSend$initWithAttributes:
+ _objc_msgSend$initWithConfigurationValues:
+ _objc_msgSend$initWithScheduledReceiver:forServiceName:
+ _objc_msgSend$initWithUniqueIdentifier:domainIdentifier:attributeSet:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$name
+ _objc_msgSend$needsDeletes
+ _objc_msgSend$needsHTML
+ _objc_msgSend$needsLanguage
+ _objc_msgSend$needsText
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$objectForKey:
+ _objc_msgSend$optionalAttributes
+ _objc_msgSend$priority
+ _objc_msgSend$processes
+ _objc_msgSend$protectionClass
+ _objc_msgSend$requireBacklog
+ _objc_msgSend$requirePriority
+ _objc_msgSend$requiredAttributes
+ _objc_msgSend$reset
+ _objc_msgSend$resume
+ _objc_msgSend$scheduledReceiver
+ _objc_msgSend$serviceName
+ _objc_msgSend$setAttribute:forKey:
+ _objc_msgSend$setBundleIdentifier:
+ _objc_msgSend$setConfigName:
+ _objc_msgSend$setDonationType:
+ _objc_msgSend$setHTMLContentData:
+ _objc_msgSend$setINIntentClassNames:
+ _objc_msgSend$setIdentifiers:
+ _objc_msgSend$setIndexType:
+ _objc_msgSend$setIsUpdate:
+ _objc_msgSend$setItems:
+ _objc_msgSend$setJournalCookie:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setOptions:
+ _objc_msgSend$setSerialNumber:
+ _objc_msgSend$setTextContent:
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$supportedBundles
+ _objc_msgSend$supportedDomainIdentifiers
+ _objc_msgSend$supportedINIntentClassNames
+ _objc_msgSend$supportedQuery
+ _objc_msgSend$supportsDeletes
+ _objc_msgSend$supportsUpdates
+ _objc_msgSend$suspend
+ _objc_msgSend$trackingAttributes
+ _objc_msgSend$unsupportedBundles
+ _objc_msgSend$unsupportedContentTypes
+ _objc_msgSend$unsupportedDomainIdentifiers
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x25
+ _objc_retain_x27
+ _sCSScheduledReceiverConnection
+ _vm_page_size
+ _xpc_fd_dup
- GCC_except_table3
- _OUTLINED_FUNCTION_3
CStrings:
+ ""
+ "### RECEIVER adding config %@"
+ "### SCHEDULED RECEIVER deleteWithFd invalid request"
+ "### SCHEDULED RECEIVER indexWithFd invalid request %@"
+ "### SCHEDULED RECEIVER processing add/updated batch"
+ "### SCHEDULED RECEIVER processing delete item batch"
+ "### SCHEDULED RECEIVER request timed out wait for deletion to be handled"
+ "### SCHEDULED RECEIVER reset %@"
+ "### SCHEDULED RECEIVER resume %@"
+ "### SCHEDULED RECEIVER sending %ld items"
+ "### SCHEDULED RECEIVER sending delete items"
+ "### SCHEDULED RECEIVER suspend %@"
+ "%@"
+ "%@-%@"
+ "%@.%@.adds"
+ "%@.deletes"
+ "%@/%@.plist"
+ "%@: %@ %@ %@ %@ %@ %@ %@ %@\n\ttra:%@\n\treq:%@\n\topt:%@\n\texc:%@\n\tdon:%@\n\tbundles:%@\n\tdisableBundles:%@\n\tdomains:%@\n\tdisableDomains:%@\n\tcontentTypes:%@\n\tdisableTypes:%@\n\tquery:%@\n\t"
+ "/System/Library/PrivateFrameworks/TextUnderstandingRuntime.framework"
+ "@\"NSMutableDictionary\""
+ "@\"NSNumber\""
+ "@\"NSObject<SpotlightScheduledReceiver>\""
+ "@\"NSString\""
+ "@24@0:8@16"
+ "B"
+ "B16@0:8"
+ "Q"
+ "Q16@0:8"
+ "SenderUpdate"
+ "Spotlight"
+ "SpotlightReceiverDonation"
+ "SpotlightScheduledReceiverConfig"
+ "SpotlightScheduledReceiverConnectionUIDKey"
+ "SpotlightScheduledReceiverDebug"
+ "T@\"NSArray\",C,N,V_donationAttributes"
+ "T@\"NSArray\",C,N,V_excludeAttributes"
+ "T@\"NSArray\",C,N,V_optionalAttributes"
+ "T@\"NSArray\",C,N,V_processes"
+ "T@\"NSArray\",C,N,V_requiredAttributes"
+ "T@\"NSArray\",C,N,V_supportedBundles"
+ "T@\"NSArray\",C,N,V_supportedContentTypes"
+ "T@\"NSArray\",C,N,V_supportedDomainIdentifiers"
+ "T@\"NSArray\",C,N,V_trackingAttributes"
+ "T@\"NSArray\",C,N,V_unsupportedBundles"
+ "T@\"NSArray\",C,N,V_unsupportedContentTypes"
+ "T@\"NSArray\",C,N,V_unsupportedDomainIdentifiers"
+ "T@\"NSArray\",R,N"
+ "T@\"NSArray\",R,N,V_defaultAttributes"
+ "T@\"NSArray\",R,N,V_identifiers"
+ "T@\"NSArray\",R,N,V_items"
+ "T@\"NSNumber\",C,N,V_versionValue"
+ "T@\"NSObject<SpotlightScheduledReceiver>\",R,N,V_scheduledReceiver"
+ "T@\"NSString\",C,N,V_name"
+ "T@\"NSString\",C,N,V_priority"
+ "T@\"NSString\",C,N,V_supportedQuery"
+ "T@\"NSString\",C,N,V_unsupportedQuery"
+ "T@\"NSString\",C,N,V_versionName"
+ "T@\"NSString\",R,N"
+ "T@\"NSString\",R,N,V_bundleIdentifier"
+ "T@\"NSString\",R,N,V_configName"
+ "T@\"NSString\",R,N,V_journalCookie"
+ "T@\"NSString\",R,N,V_protectionClass"
+ "TB,N,V_needsDeletes"
+ "TB,N,V_needsHTML"
+ "TB,N,V_needsLanguage"
+ "TB,N,V_needsText"
+ "TB,N,V_needsUserActivities"
+ "TB,R,N"
+ "TQ,R,N,V_serialNumber"
+ "Tq,N,V_options"
+ "Tq,R,N,V_donationType"
+ "Tq,R,N,V_indexType"
+ "_bundleIdentifier"
+ "_configDescription"
+ "_configName"
+ "_configs"
+ "_defaultAttributes"
+ "_donationAttributes"
+ "_donationType"
+ "_excludeAttributes"
+ "_fetchAttributes"
+ "_identifiers"
+ "_indexType"
+ "_initWithName:protectionClass:bundleIdentifier:options:"
+ "_items"
+ "_journalCookie"
+ "_kMDItem%@Version"
+ "_kMDItemBundleID"
+ "_kMDItemDomainIdentifier"
+ "_kMDItemExternalID"
+ "_kMDItemProcessedBacklog"
+ "_kMDItemProcessedBySpotlightSender"
+ "_kMDItemProcessedPriority"
+ "_kMDItemProtectionClass"
+ "_kMDItemSnippet"
+ "_kMDItemTextContentIndexExists"
+ "_kMDItemUserActivityType"
+ "_name"
+ "_needsDeletes"
+ "_needsHTML"
+ "_needsLanguage"
+ "_needsText"
+ "_needsUserActivities"
+ "_optionalAttributes"
+ "_options"
+ "_priority"
+ "_processes"
+ "_protectionClass"
+ "_requiredAttributes"
+ "_scheduledReceiver"
+ "_serialNumber"
+ "_supportedBundles"
+ "_supportedContentTypes"
+ "_supportedDomainIdentifiers"
+ "_supportedQuery"
+ "_trackingAttributes"
+ "_unsupportedBundles"
+ "_unsupportedContentTypes"
+ "_unsupportedDomainIdentifiers"
+ "_unsupportedQuery"
+ "_updateAttributes"
+ "_versionName"
+ "_versionValue"
+ "aatrs"
+ "addConfiguration:"
+ "addObjectsFromArray:"
+ "addOrUpdateSearchableItems:bundleID:name:completionHandler:"
+ "allObjects"
+ "allValues"
+ "capitalizedString"
+ "cnm"
+ "com.apple.Passbook"
+ "com.apple.corespotlight.scheduled.receiver.textunderstandingd"
+ "configForIdentifier:"
+ "configName"
+ "configs"
+ "containsObject:"
+ "copyNSStringOrDictArrayFromXPCArray:"
+ "defaultAttributes"
+ "deleteWithFd:offset:size:donation:completionHandler:"
+ "description"
+ "dictionary:setStringOrDictionaryArray:forKey:"
+ "dictionaryWithCapacity:"
+ "dictionaryWithContentsOfURL:error:"
+ "donationAttributes"
+ "donationType"
+ "enableDebuggability"
+ "excludeAttributes"
+ "f-off"
+ "f-size"
+ "fd"
+ "fetchAttributes"
+ "fileExistsAtPath:"
+ "fileURLWithPath:"
+ "handleDonation:completionHandler:"
+ "identifier"
+ "identifiers"
+ "includeDeletedItems"
+ "includeLanguage"
+ "includeUpdatedItems"
+ "indexSearchableItems:completionHandler:"
+ "indexType"
+ "indexWithFd:offset:size:donation:additionalAttributes:config:completionHandler:"
+ "init"
+ "initWithAttributes:"
+ "initWithConfigurationValues:"
+ "initWithScheduledReceiver:forServiceName:"
+ "initWithUniqueIdentifier:domainIdentifier:attributeSet:"
+ "isEqualToString:"
+ "items"
+ "itype"
+ "j-cook"
+ "journalCookie"
+ "jps"
+ "kMDItemContentType"
+ "kMDItemExtraData"
+ "kMDItemHTMLContentData"
+ "kMDItemTextContent"
+ "kMDItemTextContentLanguage"
+ "name"
+ "needsDeletes"
+ "needsHTML"
+ "needsLanguage"
+ "needsText"
+ "needsUserActivities"
+ "numberWithBool:"
+ "objectForKey:"
+ "optionalAttributes"
+ "options"
+ "priority"
+ "processes"
+ "protectionClass"
+ "q"
+ "q16@0:8"
+ "requireBacklog"
+ "requireBacklogItems"
+ "requirePriority"
+ "requirePriorityItems"
+ "requiredAttributes"
+ "requiresHTML"
+ "requiresText"
+ "reset"
+ "resume"
+ "s-num"
+ "scheduledReceiver"
+ "serialNumber"
+ "serviceName"
+ "setAttribute:forKey:"
+ "setBundleIdentifier:"
+ "setConfigName:"
+ "setDonationAttributes:"
+ "setDonationType:"
+ "setExcludeAttributes:"
+ "setHTMLContentData:"
+ "setIdentifiers:"
+ "setIndexType:"
+ "setIsUpdate:"
+ "setItems:"
+ "setJournalCookie:"
+ "setName:"
+ "setNeedsDeletes:"
+ "setNeedsHTML:"
+ "setNeedsLanguage:"
+ "setNeedsText:"
+ "setNeedsUserActivities:"
+ "setObject:forKey:"
+ "setObject:forKeyedSubscript:"
+ "setOptionalAttributes:"
+ "setOptions:"
+ "setPriority:"
+ "setProcesses:"
+ "setRequiredAttributes:"
+ "setSerialNumber:"
+ "setSupportedBundles:"
+ "setSupportedContentTypes:"
+ "setSupportedDomainIdentifiers:"
+ "setSupportedQuery:"
+ "setTextContent:"
+ "setTrackingAttributes:"
+ "setUnsupportedBundles:"
+ "setUnsupportedContentTypes:"
+ "setUnsupportedDomainIdentifiers:"
+ "setUnsupportedQuery:"
+ "setVersionName:"
+ "setVersionValue:"
+ "stringWithFormat:"
+ "stringWithUTF8String:"
+ "supportedBundles"
+ "supportedDomainIdentifiers"
+ "supportedDomains"
+ "supportedINIntentClassNames"
+ "supportedQuery"
+ "supportsDeletes"
+ "supportsUpdates"
+ "suspend"
+ "trackingAttributes"
+ "unsupportedBundles"
+ "unsupportedContentTypes"
+ "unsupportedDomainIdentifiers"
+ "unsupportedDomains"
+ "unsupportedQuery"
+ "v16@?0@\"NSError\"8"
+ "v20@0:8B16"
+ "v20@?0i8@\"NSError\"12"
+ "v24@0:8Q16"
+ "v24@0:8q16"
+ "v52@0:8i16Q20Q28@36@?44"
+ "v52@?0q8r*16{?=*Q{?=IC}}24B48"
+ "v68@0:8i16Q20Q28@36@44@52@?60"
+ "v96@?0q8r*16{?=*Q{?=IC}}24{?=*Q{?=IC}}48{?=*Q{?=IC}}72"
+ "versionName"
+ "versionValue"

```
