## BiomeFoundation

> `/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation`

```diff

-123.2.8.0.0
-  __TEXT.__text: 0x23910
-  __TEXT.__auth_stubs: 0xa10
-  __TEXT.__objc_methlist: 0x1618
-  __TEXT.__const: 0xe8
-  __TEXT.__cstring: 0x3e73
-  __TEXT.__oslogstring: 0x239a
-  __TEXT.__gcc_except_tab: 0x9ac
+123.5.23.1.0
+  __TEXT.__text: 0x26e14
+  __TEXT.__auth_stubs: 0xa00
+  __TEXT.__objc_methlist: 0x1820
+  __TEXT.__const: 0xf0
+  __TEXT.__cstring: 0x4089
+  __TEXT.__oslogstring: 0x2589
+  __TEXT.__gcc_except_tab: 0xa5c
   __TEXT.__dlopen_cstrs: 0x20c
-  __TEXT.__unwind_info: 0x8dc
-  __TEXT.__objc_classname: 0x3c9
-  __TEXT.__objc_methname: 0x398c
-  __TEXT.__objc_methtype: 0xb15
-  __TEXT.__objc_stubs: 0x3100
+  __TEXT.__unwind_info: 0x98c
+  __TEXT.__objc_classname: 0x411
+  __TEXT.__objc_methname: 0x3cbe
+  __TEXT.__objc_methtype: 0xb3b
+  __TEXT.__objc_stubs: 0x3480
   __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0x898
-  __DATA_CONST.__objc_classlist: 0x110
+  __DATA_CONST.__const: 0x988
+  __DATA_CONST.__objc_classlist: 0x128
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3758
-  __DATA_CONST.__objc_selrefs: 0xf80
-  __DATA_CONST.__objc_arraydata: 0x1270
-  __AUTH_CONST.__cfstring: 0x4700
-  __AUTH_CONST.__objc_intobj: 0x150
+  __DATA_CONST.__objc_const: 0x3898
+  __DATA_CONST.__objc_selrefs: 0x10b0
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0x200
+  __DATA_CONST.__objc_superrefs: 0xe8
+  __DATA_CONST.__objc_arraydata: 0x12c8
+  __AUTH_CONST.__cfstring: 0x4a00
+  __AUTH_CONST.__objc_intobj: 0x198
   __AUTH_CONST.__objc_arrayobj: 0x4f8
-  __AUTH_CONST.__objc_dictobj: 0x1b8
-  __AUTH_CONST.__objc_const: 0xe40
+  __AUTH_CONST.__objc_dictobj: 0x208
+  __AUTH_CONST.__objc_const: 0xff0
   __AUTH_CONST.__const: 0x320
-  __AUTH_CONST.__auth_got: 0x518
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x1e8
-  __DATA.__objc_superrefs: 0xd8
-  __DATA.__objc_ivar: 0x160
-  __DATA.__data: 0x4f0
-  __DATA.__bss: 0x80
+  __AUTH_CONST.__auth_got: 0x510
+  __AUTH.__objc_data: 0x190
+  __DATA.__objc_ivar: 0x170
+  __DATA.__data: 0x4e8
+  __DATA.__bss: 0x78
   __DATA_DIRTY.__objc_data: 0xa00
-  __DATA_DIRTY.__data: 0x198
-  __DATA_DIRTY.__bss: 0xf8
+  __DATA_DIRTY.__data: 0x1b0
+  __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7F6E008E-2C7D-3F3C-A839-2822C88981CB
-  Functions: 809
-  Symbols:   2921
-  CStrings:  2228
+  UUID: FC373A97-31BC-33DF-876D-A7673A94A548
+  Functions: 875
+  Symbols:   3116
+  CStrings:  2338
 
Symbols:
+ +[BMAccount _hashOfString:]
+ +[BMAccount verifyFormattedLikeIdentifier:]
+ +[BMAccountManager new]
+ +[BMPaths pathForSetIdentifier:]
+ +[BMPaths pathForSharedSyncWithAccount:domain:]
+ +[BMPaths pathForSharedSyncWithAccount:streamType:domain:]
+ +[BMPaths setsDirectoryForDomain:]
+ +[BMResourceDescriptor _validateInput:description:error:]
+ +[BMResourceDescriptor descriptorsFromEncodedString:error:]
+ +[BMResourceDescriptor encodedStringFromDescriptors:error:]
+ +[BMStoreDirectory(BiomeInternalOnly) sets]
+ +[BMWeakProxy weakProxyToObject:]
+ -[BMAccessClient configureConnection:]
+ -[BMAccessClient configureConnection:].cold.1
+ -[BMAccessControlPolicy allowsAccessToSet:withMode:]
+ -[BMAccessControlPolicy allowsAccessToSetsWithMode:]
+ -[BMAccessControlPolicy(SetStoreUpdateService) allowsAccessToSetStoreUpdateServiceForSet:]
+ -[BMAccessControlPolicy(SetStoreUpdateService) allowsConnectionToSetStoreUpdateService]
+ -[BMAccount altDSID]
+ -[BMAccount hash]
+ -[BMAccount identifier]
+ -[BMAccount initWithAltDSID:]
+ -[BMAccount initWithIdentifier:]
+ -[BMAccount initWithIdentifier:].cold.1
+ -[BMAccount isEqual:]
+ -[BMAccountManager .cxx_destruct]
+ -[BMAccountManager _accountIdentifiers]
+ -[BMAccountManager _accountIdentifiers].cold.1
+ -[BMAccountManager accounts]
+ -[BMAccountManager deviceIdentifiersForAccount:]
+ -[BMAccountManager deviceIdentifiersForAccount:].cold.1
+ -[BMAccountManager initWithUseCase:]
+ -[BMAccountManager init]
+ -[BMFileServer entitledToAccessSharedSyncWithError:]
+ -[BMFileServer fileHandleForFileAtPath:flags:protection:reply:].cold.4
+ -[BMFileServer replaceFileAtPath:withFileHandle:protection:reply:].cold.4
+ -[BMResourceDescriptor .cxx_destruct]
+ -[BMResourceDescriptor copyWithZone:]
+ -[BMResourceDescriptor description]
+ -[BMResourceDescriptor encodedString]
+ -[BMResourceDescriptor hash]
+ -[BMResourceDescriptor initWithEncodedString:error:]
+ -[BMResourceDescriptor initWithKey:value:error:]
+ -[BMResourceDescriptor isEqual:]
+ -[BMResourceDescriptor key]
+ -[BMResourceDescriptor value]
+ -[BMWeakProxy .cxx_destruct]
+ -[BMWeakProxy forwardingTargetForSelector:]
+ GCC_except_table12
+ GCC_except_table13
+ GCC_except_table27
+ GCC_except_table38
+ GCC_except_table49
+ _BMAccessModeFromEntitlementAccessModeString
+ _BMBiomeLibraryIdentifierForUUIDString.mapping
+ _BMBiomeLibraryIdentifierForUUIDString.onceToken
+ _BMExpandBiomeLibraryPremigrationIdentifiersAccessModeDictionary
+ _BMExpandBiomeStreamsPremigrationIdentifiersAccessModeDictionary
+ _BMLegacyBiomeClientIdentifierEntitlement
+ _BMResourceDescriptorErrorDomain
+ _BMServiceDomainForSet
+ _BMSetsResource
+ _BMSharedSyncResource
+ _BMUseCaseLegacyKoa
+ _BMValidatePath.cold.2
+ _OBJC_CLASS_$_BMAccountManager
+ _OBJC_CLASS_$_BMResourceDescriptor
+ _OBJC_CLASS_$_BMWeakProxy
+ _OBJC_CLASS_$_NSMutableCharacterSet
+ _OBJC_CLASS_$_NSProxy
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_IVAR_$_BMAccount._altDSID
+ _OBJC_IVAR_$_BMAccount._identifier
+ _OBJC_IVAR_$_BMAccountManager._fileManager
+ _OBJC_IVAR_$_BMResourceDescriptor._key
+ _OBJC_IVAR_$_BMResourceDescriptor._value
+ _OBJC_IVAR_$_BMWeakProxy._target
+ _OBJC_METACLASS_$_BMAccountManager
+ _OBJC_METACLASS_$_BMResourceDescriptor
+ _OBJC_METACLASS_$_BMWeakProxy
+ _OBJC_METACLASS_$_NSProxy
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ __OBJC_$_CLASS_METHODS_BMAccessControlPolicy(SetStoreUpdateService|WriteService)
+ __OBJC_$_CLASS_METHODS_BMAccountManager
+ __OBJC_$_CLASS_METHODS_BMFileManager
+ __OBJC_$_CLASS_METHODS_BMResourceDescriptor
+ __OBJC_$_CLASS_METHODS_BMWeakProxy
+ __OBJC_$_INSTANCE_METHODS_BMAccessControlPolicy(SetStoreUpdateService|WriteService)
+ __OBJC_$_INSTANCE_METHODS_BMAccountManager
+ __OBJC_$_INSTANCE_METHODS_BMFileManager
+ __OBJC_$_INSTANCE_METHODS_BMResourceDescriptor
+ __OBJC_$_INSTANCE_METHODS_BMWeakProxy
+ __OBJC_$_INSTANCE_VARIABLES_BMAccountManager
+ __OBJC_$_INSTANCE_VARIABLES_BMResourceDescriptor
+ __OBJC_$_INSTANCE_VARIABLES_BMWeakProxy
+ __OBJC_$_PROP_LIST_BMResourceDescriptor
+ __OBJC_CLASS_PROTOCOLS_$_BMResourceDescriptor
+ __OBJC_CLASS_RO_$_BMAccountManager
+ __OBJC_CLASS_RO_$_BMResourceDescriptor
+ __OBJC_CLASS_RO_$_BMWeakProxy
+ __OBJC_METACLASS_RO_$_BMAccountManager
+ __OBJC_METACLASS_RO_$_BMResourceDescriptor
+ __OBJC_METACLASS_RO_$_BMWeakProxy
+ ___38-[BMAccessClient configureConnection:]_block_invoke
+ ___38-[BMAccessClient configureConnection:]_block_invoke.96
+ ___38-[BMAccessClient configureConnection:]_block_invoke.cold.1
+ ___38-[BMAccessClient configureConnection:]_block_invoke_2
+ ___39-[BMAccountManager _accountIdentifiers]_block_invoke
+ ___42-[BMAccessClient _newConnectionForDomain:]_block_invoke.75
+ ___42-[BMAccessClient _newConnectionForDomain:]_block_invoke.75.cold.1
+ ___42-[BMAccessClient _newConnectionForDomain:]_block_invoke.79
+ ___42-[BMAccessClient _newConnectionForDomain:]_block_invoke.79.cold.1
+ ___42-[_BMXPCFileManager _configureConnection:]_block_invoke.124
+ ___44-[BMAccessControlPolicy authorizedResources]_block_invoke
+ ___48-[BMAccountManager deviceIdentifiersForAccount:]_block_invoke
+ ___54-[BMAccessClient _requestAccessToResource:mode:error:]_block_invoke.107
+ ___59+[BMResourceDescriptor encodedStringFromDescriptors:error:]_block_invoke
+ ___69-[BMAccessClient(ConnectionProxying) requestEndpointForDomain:error:]_block_invoke.131
+ ___BMBiomeLibraryIdentifierForUUIDString_block_invoke
+ ___BMResourcesAndAccessModesListedUnderEntitlement_block_invoke
+ ___BMResourcesAndAccessModesListedUnderEntitlement_block_invoke.194
+ ___BMResourcesAndAccessModesListedUnderEntitlement_block_invoke.197
+ ___BMResourcesAndAccessModesListedUnderEntitlement_block_invoke_2
+ ___BMResourcesAndAccessModesListedUnderEntitlement_block_invoke_2.198
+ ___BMResourcesAndAccessModesListedUnderEntitlement_block_invoke_3
+ ___Block_byref_object_copy_.81
+ ___Block_byref_object_dispose_.82
+ ___block_descriptor_32_e18_B16?0"NSString"8l
+ ___block_descriptor_40_e8_32r_e55_q24?0"BMResourceDescriptor"8"BMResourceDescriptor"16lr32l8
+ ___block_descriptor_40_e8_32s_e25_v32?0"NSString"816^B24ls32l8
+ ___block_descriptor_40_e8_32s_e35_v32?0"NSString"8"NSNumber"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e46_v32?0"BMResourceSpecifier"8"NSNumber"16^B24ls32l8
+ ___block_descriptor_49_e8_32s_e35_v32?0"NSString"8"NSNumber"16^B24ls32l8
+ ___block_literal_global.208
+ ___block_literal_global.219
+ ___block_literal_global.221
+ ___block_literal_global.7
+ ___block_literal_global.78
+ ___block_literal_global.98
+ ___softlink__BiomeLibrary
+ ___softlink__BiomeLibrary.cold.1
+ __unnamed_array_storage.124
+ __unnamed_array_storage.125
+ __unnamed_array_storage.126
+ __unnamed_array_storage.278
+ __unnamed_array_storage.279
+ __unnamed_array_storage.29
+ __unnamed_array_storage.571
+ __unnamed_array_storage.63
+ __unnamed_array_storage.77
+ __unnamed_array_storage.99
+ _objc_msgSend$_accountIdentifiers
+ _objc_msgSend$_hashOfString:
+ _objc_msgSend$_pas_filteredArrayWithTest:
+ _objc_msgSend$_validateInput:description:error:
+ _objc_msgSend$addCharactersInString:
+ _objc_msgSend$allObjects
+ _objc_msgSend$allStreams
+ _objc_msgSend$allowsAccessToSet:withMode:
+ _objc_msgSend$allowsAccessToSetsWithMode:
+ _objc_msgSend$allowsConnectionToSetStoreUpdateService
+ _objc_msgSend$characterIsMember:
+ _objc_msgSend$compare:
+ _objc_msgSend$configureConnection:
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$encodedString
+ _objc_msgSend$entitledToAccessSharedSyncWithError:
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$firstObject
+ _objc_msgSend$initWithAltDSID:
+ _objc_msgSend$initWithEncodedString:error:
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$initWithKey:value:error:
+ _objc_msgSend$initWithUUIDString:
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$key
+ _objc_msgSend$lastObject
+ _objc_msgSend$pathForSetIdentifier:
+ _objc_msgSend$pathForSharedSyncWithAccount:domain:
+ _objc_msgSend$pathForSharedSyncWithAccount:streamType:domain:
+ _objc_msgSend$remoteDevices
+ _objc_msgSend$sets
+ _objc_msgSend$setsDirectoryForDomain:
+ _objc_msgSend$sortedArrayUsingComparator:
+ _objc_msgSend$value
+ _objc_msgSend$verifyFormattedLikeIdentifier:
+ _objc_msgSend$whitespaceAndNewlineCharacterSet
- +[BMAccount biomeIdentifierForAccountIdentifier:]
- +[BMFileManager(BMAccount) bm_accountIds]
- +[BMFileManager(BMAccount) bm_accountIds].cold.1
- +[BMPaths pathForSharedCurrentAccountStreamType:domain:]
- +[BMPaths pathForSharedSyncUserIdentifier:streamType:domain:]
- GCC_except_table11
- _BMExpandBiomeLibraryPremigrationIdentifiers
- _BMExpandBiomeLibraryPremigrationIdentifiers.cold.1
- _BMExpandBiomeStreamsPremigrationIdentifiers
- _BMSharedSyncPathRegex.names
- _BMSharedSyncPathRegex.onceToken
- _BMSharedSyncPathRegex.regex
- _OBJC_IVAR_$_BMAccount._accountIdentifier
- _OBJC_IVAR_$_BMAccount._biomeAccountIdentifier
- __OBJC_$_CLASS_METHODS_BMAccessControlPolicy(WriteService)
- __OBJC_$_CLASS_METHODS_BMFileManager(BMAccount)
- __OBJC_$_INSTANCE_METHODS_BMAccessControlPolicy(WriteService)
- __OBJC_$_INSTANCE_METHODS_BMFileManager(BMAccount)
- ___42-[BMAccessClient _newConnectionForDomain:]_block_invoke.74
- ___42-[BMAccessClient _newConnectionForDomain:]_block_invoke.74.cold.1
- ___42-[BMAccessClient _newConnectionForDomain:]_block_invoke.90
- ___42-[BMAccessClient _newConnectionForDomain:]_block_invoke_2
- ___42-[_BMXPCFileManager _configureConnection:]_block_invoke.123
- ___54-[BMAccessClient _requestAccessToResource:mode:error:]_block_invoke.102
- ___69-[BMAccessClient(ConnectionProxying) requestEndpointForDomain:error:]_block_invoke.125
- ___BMResourcesListedUnderEntitlement_block_invoke
- ___BMResourcesListedUnderEntitlement_block_invoke_2
- ___BMResourcesListedUnderEntitlement_block_invoke_3
- ___BMSharedSyncPathRegex_block_invoke
- ___BMSharedSyncPathRegex_block_invoke.cold.1
- ___Block_byref_object_copy_.88
- ___Block_byref_object_dispose_.89
- ___block_descriptor_32_e39_"BMResourceSpecifier"16?0"NSString"8l
- ___block_literal_global.190
- ___block_literal_global.192
- ___block_literal_global.194
- ___block_literal_global.211
- ___block_literal_global.213
- ___block_literal_global.93
- ___block_literal_global.97
- __unnamed_array_storage.118
- __unnamed_array_storage.223
- __unnamed_array_storage.26
- __unnamed_array_storage.274
- __unnamed_array_storage.275
- __unnamed_array_storage.55
- __unnamed_array_storage.569
- __unnamed_array_storage.81
- __unnamed_array_storage.90
- __unnamed_array_storage.91
- _bm_replace_file.cold.18
- _getuid
- _objc_msgSend$_pas_mappedSetWithTransform:
- _objc_msgSend$accountIdentifier
- _objc_msgSend$biomeAccountIdentifier
- _objc_msgSend$biomeIdentifierForAccountIdentifier:
- _objc_msgSend$description
- _objc_msgSend$initWithAccountIdentifier:
- _objc_msgSend$initWithBiomeAccountIdentifier:
- _objc_msgSend$pathForSharedSyncUserIdentifier:streamType:domain:
CStrings:
+ "%@ - key: %@ value: %@"
+ "%@%@%@"
+ "&"
+ "'%@' is missing entitlement 'com.apple.private.biome.sync'"
+ "/private/var/db/biome/streams/restricted/Device.Power.EnergyMode"
+ "/private/var/mobile/Library/Biome/streams/restricted/Device.Power.EnergyMode"
+ "<BMResource: set/%@>"
+ "="
+ "@"
+ "@40@0:8@16@24^@32"
+ "B16@?0@\"NSString\"8"
+ "B40@0:8@16@24^@32"
+ "BMAccessClient.requestAccessToResource: Set"
+ "BMAccessClient.requestAccessToResource: Sets"
+ "BMAccessClient.requestAccessToResource: SharedSync"
+ "BMAccount passed invalid identifier %@"
+ "BMAccount(identifier: %@ altDSID: %@)"
+ "BMAccountManager"
+ "BMResourceDescriptor"
+ "BMResourceDescriptorError"
+ "BMSetsResource"
+ "BMSharedSyncResource"
+ "BMWeakProxy"
+ "BiomeCascade"
+ "Encoded string invalid: %@ (%@)"
+ "Failed to retrieve device list for account identifier %@ stream %{public}@ with error: %@"
+ "Failed to retrieve streams list for account identifier %@ with error: %@"
+ "Found descriptors with duplicate keys: %@"
+ "Invalid %@: \"%@\" contains whitespace or separator character: '%c'"
+ "Invalid class for %@ - expected: %@ received: %@"
+ "Invalid class for descriptors - expected: %@ received: %@"
+ "Invalid class for encodedString - expected: %@ received: %@"
+ "Invalid empty string for %@"
+ "SetStoreUpdateService"
+ "Sets"
+ "Shared sync is not supported on this platform"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,N,V_altDSID"
+ "T@\"NSString\",R,N,V_key"
+ "T@\"NSString\",R,N,V_value"
+ "Unable to determine current connection in diff update service"
+ "Unexpected protection class specified for remote sharedSync file %{public}@ %d"
+ "^streams/(public|restricted)(?:/([a-zA-Z0-9_][a-zA-Z0-9_\\-\\.]*+)(?:(/lock)|(/metadata)|(/local)(/tombstone)?(/[0-9][0-9]*+)?|(/remote)(?:(/[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12})(/tombstone)?(/[0-9][0-9]*+)?)?))?$"
+ "__Koa__"
+ "_accountIdentifiers"
+ "_altDSID"
+ "_hashOfString:"
+ "_key"
+ "_pas_filteredArrayWithTest:"
+ "_target"
+ "_validateInput:description:error:"
+ "_value"
+ "accounts"
+ "addCharactersInString:"
+ "allObjects"
+ "allStreams"
+ "allowsAccessToSet:withMode:"
+ "allowsAccessToSetStoreUpdateServiceForSet:"
+ "allowsAccessToSetsWithMode:"
+ "allowsConnectionToSetStoreUpdateService"
+ "altDSID"
+ "characterIsMember:"
+ "com.apple.SetStoreUpdateService"
+ "com.apple.cascadetool"
+ "com.apple.internal.biome.sync"
+ "com.apple.private.biome.sync"
+ "com.apple.private.intelligenceplatform.client-identifier"
+ "compare:"
+ "configuration.streamIdentifier"
+ "configureConnection:"
+ "descriptorsFromEncodedString:error:"
+ "deviceIdentifiersForAccount:"
+ "dictionaryWithDictionary:"
+ "encodedString"
+ "encodedStringFromDescriptors:error:"
+ "entitledToAccessSharedSyncWithError:"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "firstObject"
+ "forwardingTargetForSelector:"
+ "id"
+ "initWithAltDSID:"
+ "initWithEncodedString:error:"
+ "initWithIdentifier:"
+ "initWithKey:value:error:"
+ "initWithUUIDString:"
+ "isEqualToNumber:"
+ "key"
+ "lastObject"
+ "pathForSetIdentifier:"
+ "pathForSharedSyncWithAccount:domain:"
+ "pathForSharedSyncWithAccount:streamType:domain:"
+ "q24@?0@\"BMResourceDescriptor\"8@\"BMResourceDescriptor\"16"
+ "sets"
+ "setsDirectoryForDomain:"
+ "sortedArrayUsingComparator:"
+ "v32@?0@\"BMResourceSpecifier\"8@\"NSNumber\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSNumber\"16^B24"
+ "v32@?0@\"NSString\"8@16^B24"
+ "value"
+ "verifyFormattedLikeIdentifier:"
+ "weakProxyToObject:"
+ "whitespaceAndNewlineCharacterSet"
- "@\"BMResourceSpecifier\"16@?0@\"NSString\"8"
- "BMSiriMemoryReferenceResolutionEvent"
- "Mismatch between accountIdentifier and derived biomeAccountIdentifier"
- "Siri.MemoryReferenceResolution"
- "SiriMemoryReferenceResolutionStream"
- "T@\"NSString\",R,C,N,V_accountIdentifier"
- "T@\"NSString\",R,C,N,V_biomeAccountIdentifier"
- "^sharedSync/(currentAccountIdentifier|[0-9A-F]{32})/streams/(public|restricted)/([a-zA-Z0-9_][a-zA-Z0-9_\\-\\.]*+)(?:(/lock)|(/metadata)|(/local)(/tombstone)?(/[0-9][0-9]*+)?|(/remote)(?:(/[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12})(/tombstone)?(/[0-9][0-9]*+)?)?)$"
- "^streams/(public|restricted)/([a-zA-Z0-9_][a-zA-Z0-9_\\-\\.]*+)(?:(/lock)|(/metadata)|(/local)(/tombstone)?(/[0-9][0-9]*+)?|(/remote)(?:(/[0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12})(/tombstone)?(/[0-9][0-9]*+)?)?)$"
- "_accountIdentifier"
- "_biomeAccountIdentifier"
- "_pas_mappedSetWithTransform:"
- "accountIdentifier: %@ biomeAccountIdentifier:%@"
- "biomeIdentifierForAccountIdentifier:"
- "bm_accountIds"
- "currentAccountIdentifier"
- "mktemp() failed: %{darwin.errno}d"
- "pathForSharedCurrentAccountStreamType:domain:"
- "pathForSharedSyncUserIdentifier:streamType:domain:"

```
