## Categories

> `/System/Library/PrivateFrameworks/Categories.framework/Categories`

```diff

-49.4.1.0.0
-  __TEXT.__text: 0xa08c
-  __TEXT.__auth_stubs: 0x410
-  __TEXT.__objc_methlist: 0x4e0
-  __TEXT.__const: 0xa8
-  __TEXT.__gcc_except_tab: 0x45c
-  __TEXT.__cstring: 0x2b15
-  __TEXT.__oslogstring: 0x49c
-  __TEXT.__unwind_info: 0x300
-  __TEXT.__objc_classname: 0x6d
-  __TEXT.__objc_methname: 0x13fa
-  __TEXT.__objc_methtype: 0x1b5
-  __TEXT.__objc_stubs: 0x1160
-  __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x5e8
-  __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x18
+53.1.0.0.0
+  __TEXT.__text: 0xadd0
+  __TEXT.__objc_methlist: 0x794
+  __TEXT.__const: 0xb0
+  __TEXT.__gcc_except_tab: 0x428
+  __TEXT.__cstring: 0x2cd2
+  __TEXT.__oslogstring: 0x5ff
+  __TEXT.__unwind_info: 0x378
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x680
+  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x580
+  __DATA_CONST.__objc_selrefs: 0x6a8
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x10
-  __DATA_CONST.__objc_arraydata: 0xa40
-  __AUTH_CONST.__auth_got: 0x218
-  __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x3480
-  __AUTH_CONST.__objc_const: 0x520
-  __AUTH_CONST.__objc_arrayobj: 0x960
+  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_arraydata: 0xa88
+  __DATA_CONST.__got: 0x100
+  __AUTH_CONST.__const: 0x140
+  __AUTH_CONST.__cfstring: 0x3660
+  __AUTH_CONST.__objc_const: 0xc70
+  __AUTH_CONST.__objc_arrayobj: 0x978
   __AUTH_CONST.__objc_dictobj: 0x50
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0x20
-  __DATA.__data: 0x128
-  __DATA.__bss: 0x58
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x4c
+  __DATA.__data: 0x1e8
+  __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x88
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 58CA30D0-930B-39D2-8F3C-003F8EFF6410
-  Functions: 170
-  Symbols:   756
-  CStrings:  1122
+  UUID: E05D053B-96F8-3BA2-8FB6-5E31449F688C
+  Functions: 205
+  Symbols:   921
+  CStrings:  932
 
Symbols:
+ +[CTAppStoreCategories supportsSecureCoding]
+ +[CTBundleCategoriesLookupResult supportsSecureCoding]
+ +[CTCategoriesVersionProvider setSharedProviderForTesting:]
+ +[CTCategoriesVersionProvider sharedProvider]
+ +[CTCategoryResolver resolvedIdentifierForVersion:appStoreCategories:ckIdentifier:systemOverride:]
+ -[CTAppStoreCategories .cxx_destruct]
+ -[CTAppStoreCategories encodeWithCoder:]
+ -[CTAppStoreCategories initWithCoder:]
+ -[CTAppStoreCategories initWithCoder:].cold.1
+ -[CTAppStoreCategories initWithPrimary:secondary:]
+ -[CTAppStoreCategories primary]
+ -[CTAppStoreCategories secondary]
+ -[CTBundleCategoriesLookupResult .cxx_destruct]
+ -[CTBundleCategoriesLookupResult appStoreCategories]
+ -[CTBundleCategoriesLookupResult applicationBundleIdentifier]
+ -[CTBundleCategoriesLookupResult counterpartBundleIdentifiers]
+ -[CTBundleCategoriesLookupResult encodeWithCoder:]
+ -[CTBundleCategoriesLookupResult initWithApplicationBundleIdentifier:appStoreCategories:parentAppBundleIdentifier:counterpartBundleIdentifiers:]
+ -[CTBundleCategoriesLookupResult initWithCoder:]
+ -[CTBundleCategoriesLookupResult initWithCoder:].cold.1
+ -[CTBundleCategoriesLookupResult parentAppBundleIdentifier]
+ -[CTCategories setVersion:completion:]
+ -[CTCategoriesVersionProvider .cxx_destruct]
+ -[CTCategoriesVersionProvider _categoriesDidChange:]
+ -[CTCategoriesVersionProvider _xpcConnection]
+ -[CTCategoriesVersionProvider currentVersion]
+ -[CTCategoriesVersionProvider dealloc]
+ -[CTCategoriesVersionProvider init]
+ GCC_except_table21
+ GCC_except_table22
+ GCC_except_table29
+ GCC_except_table33
+ GCC_except_table35
+ GCC_except_table37
+ GCC_except_table5
+ GCC_except_table9
+ _OBJC_CLASS_$_CTAppStoreCategories
+ _OBJC_CLASS_$_CTBundleCategoriesLookupResult
+ _OBJC_CLASS_$_CTCategoriesVersionProvider
+ _OBJC_CLASS_$_CTCategoryResolver
+ _OBJC_IVAR_$_CTAppStoreCategories._primary
+ _OBJC_IVAR_$_CTAppStoreCategories._secondary
+ _OBJC_IVAR_$_CTBundleCategoriesLookupResult._appStoreCategories
+ _OBJC_IVAR_$_CTBundleCategoriesLookupResult._applicationBundleIdentifier
+ _OBJC_IVAR_$_CTBundleCategoriesLookupResult._counterpartBundleIdentifiers
+ _OBJC_IVAR_$_CTBundleCategoriesLookupResult._parentAppBundleIdentifier
+ _OBJC_IVAR_$_CTCategoriesVersionProvider._cacheGeneration
+ _OBJC_IVAR_$_CTCategoriesVersionProvider._cacheLock
+ _OBJC_IVAR_$_CTCategoriesVersionProvider._cachedVersion
+ _OBJC_IVAR_$_CTCategoriesVersionProvider._hasCachedVersion
+ _OBJC_IVAR_$_CTCategoriesVersionProvider._xpcConnection
+ _OBJC_METACLASS_$_CTAppStoreCategories
+ _OBJC_METACLASS_$_CTBundleCategoriesLookupResult
+ _OBJC_METACLASS_$_CTCategoriesVersionProvider
+ _OBJC_METACLASS_$_CTCategoryResolver
+ __OBJC_$_CLASS_METHODS_CTAppStoreCategories
+ __OBJC_$_CLASS_METHODS_CTBundleCategoriesLookupResult
+ __OBJC_$_CLASS_METHODS_CTCategoriesVersionProvider
+ __OBJC_$_CLASS_METHODS_CTCategoryResolver
+ __OBJC_$_CLASS_PROP_LIST_CTAppStoreCategories
+ __OBJC_$_CLASS_PROP_LIST_CTBundleCategoriesLookupResult
+ __OBJC_$_CLASS_PROP_LIST_CTCategoriesVersionProvider
+ __OBJC_$_INSTANCE_METHODS_CTAppStoreCategories
+ __OBJC_$_INSTANCE_METHODS_CTBundleCategoriesLookupResult
+ __OBJC_$_INSTANCE_METHODS_CTCategoriesVersionProvider
+ __OBJC_$_INSTANCE_VARIABLES_CTAppStoreCategories
+ __OBJC_$_INSTANCE_VARIABLES_CTBundleCategoriesLookupResult
+ __OBJC_$_INSTANCE_VARIABLES_CTCategoriesVersionProvider
+ __OBJC_$_PROP_LIST_CTAppStoreCategories
+ __OBJC_$_PROP_LIST_CTBundleCategoriesLookupResult
+ __OBJC_$_PROP_LIST_CTCategoriesVersionProvider
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CTCategoriesVersionProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CTCategoriesVersionProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_CTCategoriesVersionProviding
+ __OBJC_CLASS_PROTOCOLS_$_CTAppStoreCategories
+ __OBJC_CLASS_PROTOCOLS_$_CTBundleCategoriesLookupResult
+ __OBJC_CLASS_PROTOCOLS_$_CTCategoriesVersionProvider
+ __OBJC_CLASS_RO_$_CTAppStoreCategories
+ __OBJC_CLASS_RO_$_CTBundleCategoriesLookupResult
+ __OBJC_CLASS_RO_$_CTCategoriesVersionProvider
+ __OBJC_CLASS_RO_$_CTCategoryResolver
+ __OBJC_LABEL_PROTOCOL_$_CTCategoriesVersionProviding
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_METACLASS_RO_$_CTAppStoreCategories
+ __OBJC_METACLASS_RO_$_CTBundleCategoriesLookupResult
+ __OBJC_METACLASS_RO_$_CTCategoriesVersionProvider
+ __OBJC_METACLASS_RO_$_CTCategoryResolver
+ __OBJC_PROTOCOL_$_CTCategoriesVersionProviding
+ __OBJC_PROTOCOL_$_NSObject
+ ___38-[CTCategories setVersion:completion:]_block_invoke
+ ___38-[CTCategories setVersion:completion:]_block_invoke.39
+ ___38-[CTCategories setVersion:completion:]_block_invoke.39.cold.1
+ ___38-[CTCategories setVersion:completion:]_block_invoke.cold.1
+ ___45+[CTCategoriesVersionProvider sharedProvider]_block_invoke
+ ___45-[CTCategoriesVersionProvider _xpcConnection]_block_invoke
+ ___45-[CTCategoriesVersionProvider currentVersion]_block_invoke
+ ___45-[CTCategoriesVersionProvider currentVersion]_block_invoke.7
+ ___45-[CTCategoriesVersionProvider currentVersion]_block_invoke.cold.1
+ ___58-[CTCategories categoriesForDomainURLs:completionHandler:]_block_invoke.49
+ ___59+[CTCategory categoryForDomainNames:withCompletionHandler:]_block_invoke.226
+ ___59-[CTCategories categoriesForDomainNames:completionHandler:]_block_invoke.46
+ ___59-[CTCategories categoriesForDomainNames:completionHandler:]_block_invoke.47
+ ___66+[CTCategory _lookupAppStoreUsing:platform:withCompletionHandler:]_block_invoke.277
+ ___74+[CTCategory categoryForBundleIdentifiers:platform:withCompletionHandler:]_block_invoke.213
+ ___74+[CTCategory categoryForBundleIdentifiers:platform:withCompletionHandler:]_block_invoke.217
+ ___74+[CTCategory categoryForBundleIdentifiers:platform:withCompletionHandler:]_block_invoke.217.cold.1
+ ___74+[CTCategory categoryForBundleIdentifiers:platform:withCompletionHandler:]_block_invoke.219
+ ___74+[CTCategory categoryForBundleIdentifiers:platform:withCompletionHandler:]_block_invoke.221
+ ___74+[CTCategory categoryForBundleIdentifiers:platform:withCompletionHandler:]_block_invoke.223
+ ___block_descriptor_32_e17_v16?0"NSError"8l
+ ___block_descriptor_48_e8_32r40r_e8_v16?0q8lr32l8r40l8
+ ___block_descriptor_48_e8_32r_e57_v32?0"NSString"8"CTBundleCategoriesLookupResult"16^B24lr32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
+ ___block_descriptor_48_e8_32w40w_e5_v8?0lw32l8w40l8
+ ___block_descriptor_64_e8_32s40r_e57_v32?0"NSString"8"CTBundleCategoriesLookupResult"16^B24ls32l8r40l8
+ ___block_descriptor_72_e8_32s40bs48r_e34_v24?0"NSDictionary"8"NSError"16ls32l8r48l8s40l8
+ ___block_literal_global.230
+ ___block_literal_global.253
+ ___block_literal_global.276
+ ___block_literal_global.301
+ ___block_literal_global.527
+ __default
+ __override
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$appStoreCategories
+ _objc_msgSend$appStoreCategoriesForBundleIDs:platform:replyHandler:
+ _objc_msgSend$applicationBundleIdentifier
+ _objc_msgSend$categorizationVersionWithReplyHandler:
+ _objc_msgSend$counterpartBundleIdentifiers
+ _objc_msgSend$currentVersion
+ _objc_msgSend$initWithApplicationBundleIdentifier:appStoreCategories:parentAppBundleIdentifier:counterpartBundleIdentifiers:
+ _objc_msgSend$initWithPrimary:secondary:
+ _objc_msgSend$installedAppCategoriesForBundleIDs:replyHandler:
+ _objc_msgSend$parentAppBundleIdentifier
+ _objc_msgSend$primary
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$resolvedIdentifierForVersion:appStoreCategories:ckIdentifier:systemOverride:
+ _objc_msgSend$secondary
+ _objc_msgSend$setCategorizationVersion:replyHandler:
+ _objc_msgSend$setClasses:forSelector:argumentIndex:ofReply:
+ _objc_msgSend$setInterruptionHandler:
+ _objc_msgSend$setInvalidationHandler:
+ _objc_msgSend$sharedProvider
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x3
+ _objc_retain_x4
+ _objc_retain_x7
+ _objc_retain_x9
+ _sharedProvider.onceToken
- GCC_except_table15
- GCC_except_table19
- GCC_except_table27
- GCC_except_table28
- GCC_except_table32
- GCC_except_table36
- _OBJC_CLASS_$_CTError
- _OBJC_CLASS_$_NSError
- _OBJC_CLASS_$_NSIndexSet
- _OBJC_METACLASS_$_CTError
- _OBJC_METACLASS_$_NSError
- _OUTLINED_FUNCTION_2
- _OUTLINED_FUNCTION_3
- __OBJC_CLASS_RO_$_CTError
- __OBJC_METACLASS_RO_$_CTError
- ___58-[CTCategories categoriesForDomainURLs:completionHandler:]_block_invoke.47
- ___59+[CTCategory categoryForDomainNames:withCompletionHandler:]_block_invoke.214
- ___59-[CTCategories categoriesForDomainNames:completionHandler:]_block_invoke.44
- ___59-[CTCategories categoriesForDomainNames:completionHandler:]_block_invoke.45
- ___66+[CTCategory _lookupAppStoreUsing:platform:withCompletionHandler:]_block_invoke.266
- ___74+[CTCategory categoryForBundleIdentifiers:platform:withCompletionHandler:]_block_invoke.202
- ___74+[CTCategory categoryForBundleIdentifiers:platform:withCompletionHandler:]_block_invoke.206
- ___74+[CTCategory categoryForBundleIdentifiers:platform:withCompletionHandler:]_block_invoke.206.cold.1
- ___74+[CTCategory categoryForBundleIdentifiers:platform:withCompletionHandler:]_block_invoke.208
- ___74+[CTCategory categoryForBundleIdentifiers:platform:withCompletionHandler:]_block_invoke.209
- ___74+[CTCategory categoryForBundleIdentifiers:platform:withCompletionHandler:]_block_invoke.211
- ___block_descriptor_48_e8_32r_e34_v32?0"NSString"8"NSArray"16^B24lr32l8
- ___block_descriptor_56_e8_32s40r_e34_v32?0"NSString"8"NSArray"16^B24ls32l8r40l8
- ___block_descriptor_64_e8_32s40bs48r_e34_v24?0"NSDictionary"8"NSError"16ls32l8r48l8s40l8
- ___block_literal_global.218
- ___block_literal_global.241
- ___block_literal_global.265
- ___block_literal_global.290
- ___block_literal_global.516
- _objc_msgSend$genreIDsAndCounterpartIdentifiersForInstalledBundleIDs:replyHandler:
- _objc_msgSend$indexSetWithIndexesInRange:
- _objc_msgSend$lookupAppStoreForBundleIDs:platform:replyHandler:
- _objc_msgSend$objectsAtIndexes:
- _objc_retain_x26
- _objc_retain_x27
CStrings:
+ "CTAppStoreCategories: decode failed — missing required `primary`"
+ "CTBundleCategoriesLookupResult: decode failed — missing required `applicationBundleIdentifier`"
+ "CTCategories setVersion: XPC error: %{public}@"
+ "CTCategories setVersion: service returned error: %{public}@"
+ "CTCategoriesVersionProvider: XPC error querying version; defaulting to Classic: %{public}@"
+ "appStoreCategories"
+ "appStoreCategoriesForBundleIDs:platform:replyHandler: %@"
+ "appStoreCategoriesForBundleIDs:platform:replyHandler: platform: %@, %{private}@"
+ "applicationBundleIdentifier"
+ "com.apple.ScreenshotServicesService"
+ "counterpartBundleIdentifiers"
+ "installedAppCategoriesForBundleIDs:replyHandler: platform: %@, %{private}@ error:%@"
+ "ios://com.apple.SiriApp"
+ "ios://com.apple.campo"
+ "macos://com.apple.campo"
+ "parentAppBundleIdentifier"
+ "primary"
+ "secondary"
+ "v16@?0q8"
+ "v32@?0@\"NSString\"8@\"CTBundleCategoriesLookupResult\"16^B24"
+ "visionos://com.apple.SiriApp"
+ "visionos://com.apple.campo"
+ "watchos://com.apple.NanoContacts"
+ "watchos://com.apple.SiriApp"
+ "watchos://com.apple.campo"
- ".cxx_destruct"
- "@\"NSArray\""
- "@\"NSLock\""
- "@\"NSString\""
- "@16@0:8"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@24@0:8q16"
- "@32@0:8@16@24"
- "@40@0:8@16@24@32"
- "@48@0:8@16@24@32@40"
- "@56@0:8@16@24@32@40@48"
- "@64@0:8@16@24@32@40@48@56"
- "B16@0:8"
- "B24@0:8@16"
- "CTCategories"
- "CTCategory"
- "CTError"
- "CTLogging"
- "CTUtilities"
- "CategoriesServiceProtocol"
- "NSCoding"
- "NSSecureCoding"
- "Q16@0:8"
- "T@\"CKContextClient\",R"
- "T@\"CTCategories\",R"
- "T@\"NSArray\",C,N,V_webDomains"
- "T@\"NSArray\",R,C"
- "T@\"NSArray\",R,C,N,V_equivalentBundleIdentifiers"
- "T@\"NSString\",C,N,V_bundleIdentifier"
- "T@\"NSString\",C,N,V_canonicalBundleIdentifier"
- "T@\"NSString\",C,N,V_identifier"
- "T@\"NSString\",C,N,V_primaryWebDomain"
- "T@\"NSString\",R,C,N"
- "TB,R"
- "URL"
- "URLWithString:"
- "_DHIDtoCategoryDisplayNameMap"
- "_DHToAppStoreCategoriesMap"
- "_appBundleIdentifierStringFor:categoryIdentifier:"
- "_bundleIdentifier"
- "_bundleIdentifierForContextResponse:"
- "_canonicalBundleIdentifier"
- "_ctCategoryCommonInitWithIdentifier:equivalentBundleIdentifiers:webDomains:bundleIdentifier:primaryWebDomain:canonicalBundleIdentifier:"
- "_emptySharedCache:"
- "_equivalentBundleIDsMapping"
- "_equivalentBundleIDsMappingForWatchOSBundleID:"
- "_equivalentBundleIDsWithSchemesRemovedMapping"
- "_equivalentBundleIdentifiers"
- "_getAssociatedDomainsForHostNames:"
- "_getCategoryTypeForDomainName:withCompletionHandler:"
- "_getEquivalentBundleIdentifiers:"
- "_identifier"
- "_identifierForContextResponse:"
- "_indexVersionId"
- "_lookupAppStoreUsing:platform:withCompletionHandler:"
- "_lookupLock"
- "_newXpcConnection"
- "_overrideEquivalentIdentifiers:forBundleID:"
- "_primaryWebDomain"
- "_relatedItemsForContextResponse:"
- "_urlComponentsForHostName:"
- "_urlStringsForHostNames:"
- "_webDomains"
- "_xpcConnection"
- "absoluteString"
- "addEntriesFromDictionary:"
- "addObject:"
- "addObserver:selector:name:object:"
- "allKeys"
- "allValues"
- "appHandle"
- "array"
- "arrayWithCapacity:"
- "arrayWithObjects:count:"
- "availableCategoryIDs"
- "boolValue"
- "bundleForClass:"
- "bundleIDForPlatform:fromBundleID:platform:"
- "bundleIdentifier"
- "canonicalBundleIdentifier"
- "caseInsensitiveCompare:"
- "categoriesForBundleIDs:completionHandler:"
- "categoriesForBundleIDs:platform:completionHandler:"
- "categoriesForDomainNames:completionHandler:"
- "categoriesForDomainURLs:completionHandler:"
- "categoryForBundleID:completionHandler:"
- "categoryForBundleID:platform:completionHandler:"
- "categoryForBundleID:platform:withCompletionHandler:"
- "categoryForBundleID:withCompletionHandler:"
- "categoryForBundleIdentifiers:platform:withCompletionHandler:"
- "categoryForDomainName:completionHandler:"
- "categoryForDomainName:withCompletionHandler:"
- "categoryForDomainNames:withCompletionHandler:"
- "categoryForDomainURL:completionHandler:"
- "categoryForDomainURL:withCompletionHandler:"
- "categoryForDomainURLs:withCompletionHandler:"
- "client"
- "clientWithDefaultRequestType:"
- "code"
- "containsObject:"
- "contextKitHandle"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "currentIOSDevice"
- "dealloc"
- "decodeObjectOfClass:forKey:"
- "decodeObjectOfClasses:forKey:"
- "defaultCenter"
- "description"
- "dictionary"
- "dictionaryWithObjects:forKeys:count:"
- "domainHandle"
- "emptyCache"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "entitlements"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "equivalentBundleIdentifers"
- "equivalentBundleIdentifiers"
- "equivalentIdentifiersForBundleID:"
- "error"
- "executeCategorizationRequestWithReply:"
- "firstObject"
- "genreIDsAndCounterpartIdentifiersForInstalledBundleIDs:completionHandler: platform: %@, %{private}@ error:%@"
- "genreIDsAndCounterpartIdentifiersForInstalledBundleIDs:replyHandler:"
- "hasPrefix:"
- "hash"
- "host"
- "identifier"
- "indexSetWithIndexesInRange:"
- "init"
- "initWithCapacity:"
- "initWithCoder:"
- "initWithIdentifier:equivalentBundleIdentifiers:webDomains:bundleIdentifier:"
- "initWithIdentifier:equivalentBundleIdentifiers:webDomains:bundleIdentifier:primaryWebDomain:"
- "initWithIdentifier:equivalentBundleIdentifiers:webDomains:bundleIdentifier:primaryWebDomain:canonicalBundleIdentifier:"
- "initWithIdentifier:webDomains:bundleIdentifier:"
- "initWithIdentifier:webDomains:bundleIdentifier:primaryWebDomain:"
- "initWithObjects:"
- "initWithServiceName:"
- "initialize"
- "interfaceWithProtocol:"
- "isClassCLocked"
- "isEqual:"
- "isEqualToCategory:"
- "isEqualToString:"
- "isSystemBundleIdentifier"
- "itemWith:platform:array:"
- "length"
- "level1Topics"
- "level2Topics"
- "localizedName"
- "localizedNameForIdentifier:"
- "localizedStringForKey:value:table:"
- "lock"
- "lookupAppStoreForBundleID:completionHandler: %@"
- "lookupAppStoreForBundleID:completionHandler: platform: %@, %{private}@"
- "lookupAppStoreForBundleIDs:platform:replyHandler:"
- "minusSet:"
- "mutableCopy"
- "newRequest"
- "numberOfMatchesInString:options:range:"
- "objectForKey:"
- "objectForKey:ofClass:valuesOfClass:"
- "objectForKeyedSubscript:"
- "objectsAtIndexes:"
- "orderedSet"
- "orderedSetWithArray:"
- "parentAppBundleIdentifierForAppRecord:"
- "primaryLocalizedNameForIdentifier:"
- "primaryWebDomain"
- "q16@0:8"
- "rangeOfString:"
- "rangeOfString:options:range:"
- "regularExpressionWithPattern:options:error:"
- "relatedItems"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllObjects"
- "removeObjectsInArray:"
- "removeObserver:name:object:"
- "resume"
- "scheme"
- "schemeStringForPlatform:"
- "set"
- "setBundleIdentifier:"
- "setCanonicalBundleIdentifier:"
- "setHost:"
- "setIdentifier:"
- "setIncludeHigherLevelTopics:"
- "setObject:forKey:"
- "setObject:forKeyedSubscript:"
- "setPrimaryWebDomain:"
- "setRemoteObjectInterface:"
- "setScheme:"
- "setUrl:"
- "setUrls:"
- "setWebDomains:"
- "setWithArray:"
- "setWithObjects:"
- "sharedCategories"
- "shortLocalizedNameForIdentifier:"
- "string"
- "stringByAppendingString:"
- "stringWithFormat:"
- "substringFromIndex:"
- "substringToIndex:"
- "supportedWebBrowserBundleIdentifiersForDeviceFamily:"
- "supportsSecureCoding"
- "systemAppCategoryIdentifierForBundleIdentifier:"
- "systemBlockableBundleIdentifiersForDeviceFamily:"
- "systemCategoryIDWithPatternMatching:"
- "systemHiddenBundleIdentifiersForDeviceFamily:"
- "systemUnblockableBundleIdentifiersForDeviceFamily:"
- "topicId"
- "unCategorizedDomainsFromDomains:withCompletionHandler:"
- "unionOrderedSet:"
- "unionSet:"
- "unlock"
- "v16@0:8"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v32@0:8@\"NSArray\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "v32@0:8@16@?24"
- "v40@0:8@\"NSArray\"16@\"NSString\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@16@24@?32"
- "v64@0:8@16@24@32@40@48@56"
- "webDomains"

```
