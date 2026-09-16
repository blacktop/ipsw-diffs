## ContainerManagerCommon

> `/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/ContainerManagerCommon`

```diff

-833.0.8.0.1
-  __TEXT.__text: 0xeed90
-  __TEXT.__objc_methlist: 0xae74
-  __TEXT.__const: 0x13b0
-  __TEXT.__cstring: 0x9585
-  __TEXT.__swift5_typeref: 0x6d3
-  __TEXT.__oslogstring: 0xe983
-  __TEXT.__constg_swiftt: 0x670
-  __TEXT.__swift5_reflstr: 0x3da
-  __TEXT.__swift5_fieldmd: 0x4c8
-  __TEXT.__swift5_builtin: 0x104
+833.40.14.0.0
+  __TEXT.__text: 0x1010b4
+  __TEXT.__objc_methlist: 0xb3ac
+  __TEXT.__const: 0x15e0
+  __TEXT.__cstring: 0x9bc4
+  __TEXT.__swift5_typeref: 0x85b
+  __TEXT.__oslogstring: 0xfd87
+  __TEXT.__constg_swiftt: 0x7b0
+  __TEXT.__swift5_reflstr: 0x56a
+  __TEXT.__swift5_fieldmd: 0x644
+  __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_assocty: 0x138
   __TEXT.__swift5_proto: 0xb0
-  __TEXT.__swift5_types: 0x98
+  __TEXT.__swift5_types: 0xb8
+  __TEXT.__swift5_capture: 0xa8
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__swift5_capture: 0x78
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__gcc_except_tab: 0x2498
+  __TEXT.__gcc_except_tab: 0x2544
   __TEXT.__ustring: 0x16c
-  __TEXT.__unwind_info: 0x3af8
-  __TEXT.__eh_frame: 0x5d8
+  __TEXT.__unwind_info: 0x3df0
+  __TEXT.__eh_frame: 0x958
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x18d8
-  __DATA_CONST.__objc_classlist: 0x5c0
-  __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x528
+  __DATA_CONST.__const: 0x18e0
+  __DATA_CONST.__objc_classlist: 0x5d8
+  __DATA_CONST.__objc_catlist: 0x30
+  __DATA_CONST.__objc_protolist: 0x610
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3770
-  __DATA_CONST.__objc_protorefs: 0xc8
+  __DATA_CONST.__objc_selrefs: 0x3960
+  __DATA_CONST.__objc_protorefs: 0x1a8
   __DATA_CONST.__objc_superrefs: 0x4a8
-  __DATA_CONST.__objc_arraydata: 0x2e0
-  __DATA_CONST.__got: 0x500
-  __AUTH_CONST.__const: 0x12c8
-  __AUTH_CONST.__cfstring: 0x4d40
-  __AUTH_CONST.__objc_const: 0x17058
+  __DATA_CONST.__objc_arraydata: 0x2e8
+  __DATA_CONST.__got: 0x520
+  __AUTH_CONST.__const: 0x15c0
+  __AUTH_CONST.__cfstring: 0x4e20
+  __AUTH_CONST.__objc_const: 0x178d8
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH_CONST.__objc_intobj: 0x1590
+  __AUTH_CONST.__objc_intobj: 0x15a8
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH_CONST.__auth_got: 0x12d0
-  __AUTH.__objc_data: 0xd70
-  __AUTH.__data: 0xd0
-  __DATA.__objc_ivar: 0xc10
-  __DATA.__data: 0x3bb0
+  __AUTH_CONST.__auth_got: 0x13e0
+  __AUTH.__objc_data: 0xf40
+  __AUTH.__data: 0x1e8
+  __DATA.__objc_ivar: 0xc48
+  __DATA.__data: 0x3d50
   __DATA.__crash_info: 0x148
+  __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0x3020
   __DATA_DIRTY.__data: 0x448
   __DATA_DIRTY.__bss: 0x6b0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3659
-  Symbols:   8476
-  CStrings:  2023
+  Functions: 3856
+  Symbols:   8667
+  CStrings:  2107
 
Symbols:
+ +[MCMConcreteContainerIdentity containerIdentityWithUUID:userIdentity:identifier:containerConfig:platform:posixOwnership:instanceUUID:transient:userIdentityCache:error:]
+ +[MCMConcreteContainerIdentity containerIdentityWithUUID:userIdentity:identifier:containerConfig:platform:posixOwnership:instanceUUID:userIdentityCache:error:]
+ +[MCMConcreteContainerIdentityForLibsystem containerIdentityWithUUID:userIdentity:identifier:containerConfig:platform:posixOwnership:instanceUUID:containerPathIdentifier:existed:transient:userIdentityCache:error:]
+ +[MCMContainerCacheEntry verificationErrorIsRecoverable:]
+ +[MCMContainerCacheEntry(xattr) instanceUUIDForFileHandle:]
+ +[MCMContainerCacheEntry(xattr) instanceUUIDForURL:]
+ +[MCMContainerCacheEntry(xattr) setInstanceUUID:forFileHandle:]
+ +[MCMContainerCacheEntry(xattr) setInstanceUUID:forURL:]
+ +[MCMContainerIdentity containerIdentityWithIdentifier:containerConfig:platform:posixOwnership:instanceUUID:userIdentityCache:error:]
+ +[MCMContainerIdentity containerIdentityWithUserIdentity:identifier:containerConfig:platform:posixOwnership:instanceUUID:transient:userIdentityCache:error:]
+ +[MCMContainerIdentity containerIdentityWithUserIdentity:identifier:containerConfig:platform:posixOwnership:instanceUUID:userIdentityCache:error:]
+ +[MCMContainerSchema containerSchemaWithMetadata:finalContainerPath:dataProtectionClass:libraryRepair:error:]
+ +[MCMPOSIXUser _getCachedUID:GID:name:flush:error:onCacheMiss:]
+ +[MCMPOSIXUser _posixUserWithUID:GID:name:error:]
+ +[MCMPOSIXUser _validatedHomeDirectoryURLFromURL:redactName:resolvable:]
+ +[MCMPOSIXUser posixUserWithUID:GID:error:]
+ +[MCMPOSIXUser unvalidatedPOSIXUserWithUID:GID:unvalidatedHomeDirectoryURL:]
+ +[NSUUID(MCMUUIDIsNull) MCM_null]
+ -[MCMChildParentMapCache _lock_childIdentifiersForParentIdentifier:]
+ -[MCMChildParentMapCache lock_cache]
+ -[MCMChildParentMapCache removeMappingsForIdentifier:]
+ -[MCMClientIdentity isAllowedToSupersedeContainer]
+ -[MCMCommandQuery defaultInstanceUUID]
+ -[MCMCommandQuery instanceUUID]
+ -[MCMConcreteContainerIdentity initWithUUID:userIdentity:identifier:containerConfig:platform:posixOwnership:instanceUUID:transient:userIdentityCache:error:]
+ -[MCMConcreteContainerIdentity initWithVersion1And2And3PlistDictionary:containerIdentity:error:]
+ -[MCMConcreteContainerIdentityForLibsystem initWithUUID:userIdentity:identifier:containerConfig:platform:posixOwnership:instanceUUID:containerPathIdentifier:existed:transient:userIdentityCache:error:]
+ -[MCMContainerCache _claimContainer:forInstanceUUID:classCache:error:]
+ -[MCMContainerCache entriesForContainerIdentityIgnoringInstance:error:]
+ -[MCMContainerCache entryForContainerIdentity:classCache:mutationAllowed:error:]
+ -[MCMContainerCache removeContainerForUserIdentity:contentClass:containerIdentity:containerPath:transient:error:]
+ -[MCMContainerCacheEntry _fabricateMetadataForContainerPath:identifier:uuid:schemaVersion:posixOwnership:instanceUUID:userIdentityCache:]
+ -[MCMContainerCacheEntry _metadataFromContainerPath:identifier:uuid:schemaVersion:posixOwnership:instanceUUID:userIdentityCache:]
+ -[MCMContainerCacheEntry initFromContainerPath:identifier:uuid:schemaVersion:posixOwnership:instanceUUID:userIdentityCache:]
+ -[MCMContainerCacheEntry initWithIdentifier:containerPath:schemaVersion:posixOwnership:instanceUUID:uuid:metadata:userIdentityCache:]
+ -[MCMContainerCacheEntry instanceUUID]
+ -[MCMContainerClassCache _concurrent_generateCacheEntryWithURL:identifier:containerPath:schemaVersion:posixOwnership:instanceUUID:uuid:metadata:]
+ -[MCMContainerClassCache _concurrent_slowGenerateCacheEntryWithFileHandle:URL:identifier:uuid:schemaVersion:posixOwnership:instanceUUID:containerPath:]
+ -[MCMContainerClassCache _lock_addIdentityToInstanceIndex:]
+ -[MCMContainerClassCache _lock_removeIdentityFromInstanceIndex:]
+ -[MCMContainerClassCache cacheEntriesForIdentityIgnoringInstance:]
+ -[MCMContainerClassCache cacheEntryForIdentity:multiInstance:]
+ -[MCMContainerClassCache lock_instanceIndex]
+ -[MCMContainerClassCache removeCacheEntryForIdentity:containerPath:]
+ -[MCMContainerConfiguration deleteCorruptContainers]
+ -[MCMContainerConfiguration usesInstanceUUID]
+ -[MCMContainerIdentity initWithUserIdentity:identifier:containerConfig:platform:posixOwnership:instanceUUID:transient:userIdentityCache:error:]
+ -[MCMContainerIdentity initWithVersion1PlistDictionary:posixOwnership:instanceUUID:userIdentityCache:error:]
+ -[MCMContainerIdentity initWithVersion2PlistDictionary:instanceUUID:userIdentityCache:error:]
+ -[MCMContainerIdentity initWithVersion3PlistDictionary:instanceUUID:userIdentityCache:error:]
+ -[MCMContainerIdentityMinimal identityByChangingInstanceUUID:]
+ -[MCMContainerIdentityMinimal initWithUserIdentity:identifier:containerConfig:platform:posixOwnership:instanceUUID:userIdentityCache:error:]
+ -[MCMContainerIdentityMinimal initWithVersion1PlistDictionary:posixOwnership:instanceUUID:userIdentityCache:error:]
+ -[MCMContainerIdentityMinimal initWithVersion2PlistDictionary:instanceUUID:userIdentityCache:error:]
+ -[MCMContainerIdentityMinimal initWithVersion3PlistDictionary:userIdentityCache:error:]
+ -[MCMContainerIdentityMinimal instanceUUID]
+ -[MCMContainerSchema initWithMetadata:finalContainerPath:dataProtectionClass:libraryRepair:error:]
+ -[MCMEntitlements canSupersedeContainer]
+ -[MCMEntitlements isAllowedToSupersedeContainer]
+ -[MCMError errorByChangingType:]
+ -[MCMMetadata metadataByChangingSuperseded:]
+ -[MCMMetadata metadataByClearingPersistedStatus]
+ -[MCMMetadata superseded]
+ -[MCMMetadataMinimal instanceUUID]
+ -[MCMPOSIXPermission posixUserWithError:]
+ -[MCMPOSIXUser initWithUID:primaryGID:homeDirectoryURL:unvalidatedHomeDirectoryURL:name:roleUser:validatedUser:]
+ -[MCMPOSIXUser validatedUser]
+ -[MCMResultContainerFromPath initWithUUID:containerPathIdentifier:identifier:containerConfig:POSIXUser:personaUniqueString:sandboxToken:existed:url:info:transient:userManagedAssetsRelPath:creator:posixOwnership:instanceUUID:relativePath:]
+ -[MCMResultWithContainerBase initWithUUID:containerPathIdentifier:identifier:containerConfig:POSIXUser:personaUniqueString:sandboxToken:existed:url:info:transient:userManagedAssetsRelPath:creator:posixOwnership:instanceUUID:]
+ -[MCMResultWithContainerBase instanceUUID]
+ -[MCMXPCMessageQuery defaultInstanceUUID]
+ -[MCMXPCMessageQuery instanceUUID]
+ -[NSUUID(MCMUUIDIsNull) MCM_isNull]
+ GCC_except_table1008
+ GCC_except_table1042
+ GCC_except_table1044
+ GCC_except_table1100
+ GCC_except_table1109
+ GCC_except_table1113
+ GCC_except_table1163
+ GCC_except_table1186
+ GCC_except_table1191
+ GCC_except_table1194
+ GCC_except_table1200
+ GCC_except_table1202
+ GCC_except_table1204
+ GCC_except_table1209
+ GCC_except_table1211
+ GCC_except_table1215
+ GCC_except_table1217
+ GCC_except_table1219
+ GCC_except_table1225
+ GCC_except_table1228
+ GCC_except_table1230
+ GCC_except_table1238
+ GCC_except_table1253
+ GCC_except_table1257
+ GCC_except_table1259
+ GCC_except_table1314
+ GCC_except_table1324
+ GCC_except_table1355
+ GCC_except_table1596
+ GCC_except_table1746
+ GCC_except_table1750
+ GCC_except_table1904
+ GCC_except_table1910
+ GCC_except_table2013
+ GCC_except_table2150
+ GCC_except_table2293
+ GCC_except_table2310
+ GCC_except_table2311
+ GCC_except_table2376
+ GCC_except_table2422
+ GCC_except_table2438
+ GCC_except_table2459
+ GCC_except_table2528
+ GCC_except_table2540
+ GCC_except_table2609
+ GCC_except_table2619
+ GCC_except_table2644
+ GCC_except_table2667
+ GCC_except_table2677
+ GCC_except_table2702
+ GCC_except_table2705
+ GCC_except_table2708
+ GCC_except_table2713
+ GCC_except_table2761
+ GCC_except_table2765
+ GCC_except_table2932
+ GCC_except_table2936
+ GCC_except_table3016
+ GCC_except_table315
+ GCC_except_table343
+ GCC_except_table352
+ GCC_except_table371
+ GCC_except_table394
+ GCC_except_table403
+ GCC_except_table500
+ GCC_except_table688
+ GCC_except_table785
+ GCC_except_table877
+ GCC_except_table955
+ _MCMParentBundleKey
+ _MCM_null.onceToken
+ _MCM_null.uuid
+ _OBJC_CLASS_$_MCMCommandSupersedeContainer
+ _OBJC_CLASS_$_MCMContainerSupersession
+ _OBJC_CLASS_$__TtC22ContainerManagerCommon31MCMXPCMessageSupersedeContainer
+ _OBJC_IVAR_$_MCMChildParentMapCache._cacheLock
+ _OBJC_IVAR_$_MCMChildParentMapCache._lock_cache
+ _OBJC_IVAR_$_MCMCommandQuery._defaultInstanceUUID
+ _OBJC_IVAR_$_MCMCommandQuery._instanceUUID
+ _OBJC_IVAR_$_MCMContainerCacheEntry._instanceUUID
+ _OBJC_IVAR_$_MCMContainerClassCache._lock_instanceIndex
+ _OBJC_IVAR_$_MCMContainerConfiguration._deleteCorruptContainers
+ _OBJC_IVAR_$_MCMContainerConfiguration._usesInstanceUUID
+ _OBJC_IVAR_$_MCMContainerIdentityMinimal._instanceUUID
+ _OBJC_IVAR_$_MCMMetadata._superseded
+ _OBJC_IVAR_$_MCMPOSIXPermission._lock_posixUser
+ _OBJC_IVAR_$_MCMPOSIXPermission._posixUserLock
+ _OBJC_IVAR_$_MCMPOSIXUser._validatedUser
+ _OBJC_IVAR_$_MCMResultWithContainerBase._instanceUUID
+ _OBJC_IVAR_$_MCMXPCMessageQuery._defaultInstanceUUID
+ _OBJC_IVAR_$_MCMXPCMessageQuery._instanceUUID
+ _OBJC_METACLASS_$_MCMCommandSupersedeContainer
+ _OBJC_METACLASS_$_MCMContainerSupersession
+ _OBJC_METACLASS_$__TtC22ContainerManagerCommon31MCMXPCMessageSupersedeContainer
+ __CLASS_METHODS_MCMCommandSupersedeContainer
+ __DATA_MCMCommandSupersedeContainer
+ __DATA_MCMContainerSupersession
+ __DATA__TtC22ContainerManagerCommon31MCMXPCMessageSupersedeContainer
+ __INSTANCE_METHODS_MCMCommandSupersedeContainer
+ __INSTANCE_METHODS_MCMContainerSupersession
+ __INSTANCE_METHODS__TtC22ContainerManagerCommon31MCMXPCMessageSupersedeContainer
+ __IVARS_MCMCommandSupersedeContainer
+ __IVARS_MCMContainerSupersession
+ __IVARS__TtC22ContainerManagerCommon31MCMXPCMessageSupersedeContainer
+ __MCMCrashIfClassUsesInstanceUUID
+ __METACLASS_DATA_MCMCommandSupersedeContainer
+ __METACLASS_DATA_MCMContainerSupersession
+ __METACLASS_DATA__TtC22ContainerManagerCommon31MCMXPCMessageSupersedeContainer
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSUUID_$_MCMUUIDIsNull
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSUUID_$_MCMUUIDIsNull
+ __OBJC_$_CATEGORY_NSUUID_$_MCMUUIDIsNull
+ __OBJC_$_PROP_LIST_MCMContainerIdentityHasInstanceUUID
+ __OBJC_$_PROP_LIST_NSUUID_$_MCMUUIDIsNull
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_MCMContainerIdentityHasInstanceUUID
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MCMContainerIdentityHasInstanceUUID
+ __OBJC_$_PROTOCOL_REFS_MCMContainerIdentityHasInstanceUUID
+ __OBJC_LABEL_PROTOCOL_$_MCMContainerIdentityHasInstanceUUID
+ __OBJC_PROTOCOL_$_MCMContainerIdentityHasInstanceUUID
+ __PROPERTIES_MCMCommandSupersedeContainer
+ __PROPERTIES_MCMContainerSupersession
+ ___113-[MCMContainerCache removeContainerForUserIdentity:contentClass:containerIdentity:containerPath:transient:error:]_block_invoke
+ ___33+[NSUUID(MCMUUIDIsNull) MCM_null]_block_invoke
+ ___43+[MCMPOSIXUser posixUserWithUID:GID:error:]_block_invoke
+ ___49+[MCMPOSIXUser _posixUserWithUID:GID:name:error:]_block_invoke
+ ___63+[MCMPOSIXUser _getCachedUID:GID:name:flush:error:onCacheMiss:]_block_invoke
+ ___block_descriptor_48_e23_"MCMPOSIXUser"16?0^8l
+ ___block_descriptor_48_e8_32s_e23_"MCMPOSIXUser"16?0^8ls32l8
+ ___swift_allocate_boxed_opaque_existential_0
+ ___swift_memcpy40_8
+ ___swift_project_boxed_opaque_existential_0
+ __getCachedUID:GID:name:flush:error:onCacheMiss:.cacheByName
+ __getCachedUID:GID:name:flush:error:onCacheMiss:.cacheByUID
+ __getCachedUID:GID:name:flush:error:onCacheMiss:.cacheByUIDGID
+ __getCachedUID:GID:name:flush:error:onCacheMiss:.onceToken
+ __objc_autoreleasePoolPop
+ __objc_autoreleasePoolPush
+ _container_get_instance_uuid
+ _flat unique So11MCMMetadata_p
+ _flat unique So14MCMFileManager_p
+ _flat unique So17MCMCommandContext_p
+ _flat unique So22MCMContainerCacheEntry_p
+ _objc_msgSend$MCM_isNull
+ _objc_msgSend$MCM_null
+ _objc_msgSend$_claimContainer:forInstanceUUID:classCache:error:
+ _objc_msgSend$_concurrent_generateCacheEntryWithURL:identifier:containerPath:schemaVersion:posixOwnership:instanceUUID:uuid:metadata:
+ _objc_msgSend$_concurrent_slowGenerateCacheEntryWithFileHandle:URL:identifier:uuid:schemaVersion:posixOwnership:instanceUUID:containerPath:
+ _objc_msgSend$_fabricateMetadataForContainerPath:identifier:uuid:schemaVersion:posixOwnership:instanceUUID:userIdentityCache:
+ _objc_msgSend$_getCachedUID:GID:name:flush:error:onCacheMiss:
+ _objc_msgSend$_instanceUUID
+ _objc_msgSend$_lock_addIdentityToInstanceIndex:
+ _objc_msgSend$_lock_childIdentifiersForParentIdentifier:
+ _objc_msgSend$_lock_removeIdentityFromInstanceIndex:
+ _objc_msgSend$_metadataFromContainerPath:identifier:uuid:schemaVersion:posixOwnership:instanceUUID:userIdentityCache:
+ _objc_msgSend$_posixUserWithUID:GID:name:error:
+ _objc_msgSend$_validatedHomeDirectoryURLFromURL:redactName:resolvable:
+ _objc_msgSend$cacheEntriesForIdentityIgnoringInstance:
+ _objc_msgSend$cacheEntryForIdentity:multiInstance:
+ _objc_msgSend$canSupersedeContainer
+ _objc_msgSend$client
+ _objc_msgSend$containerIdentityWithIdentifier:containerConfig:platform:posixOwnership:instanceUUID:userIdentityCache:error:
+ _objc_msgSend$containerIdentityWithUUID:userIdentity:identifier:containerConfig:platform:posixOwnership:instanceUUID:containerPathIdentifier:existed:transient:userIdentityCache:error:
+ _objc_msgSend$containerIdentityWithUUID:userIdentity:identifier:containerConfig:platform:posixOwnership:instanceUUID:transient:userIdentityCache:error:
+ _objc_msgSend$containerIdentityWithUUID:userIdentity:identifier:containerConfig:platform:posixOwnership:instanceUUID:userIdentityCache:error:
+ _objc_msgSend$containerIdentityWithUserIdentity:identifier:containerConfig:platform:posixOwnership:instanceUUID:transient:userIdentityCache:error:
+ _objc_msgSend$containerIdentityWithUserIdentity:identifier:containerConfig:platform:posixOwnership:instanceUUID:userIdentityCache:error:
+ _objc_msgSend$containerSchemaWithMetadata:finalContainerPath:dataProtectionClass:libraryRepair:error:
+ _objc_msgSend$defaultInstanceUUID
+ _objc_msgSend$deleteCorruptContainers
+ _objc_msgSend$entriesForContainerIdentityIgnoringInstance:error:
+ _objc_msgSend$entryForContainerIdentity:classCache:mutationAllowed:error:
+ _objc_msgSend$errorByChangingType:
+ _objc_msgSend$formerContainerPathIdentifier
+ _objc_msgSend$formerIdentifier
+ _objc_msgSend$formerInstanceUUID
+ _objc_msgSend$formerUUID
+ _objc_msgSend$identityByChangingInstanceUUID:
+ _objc_msgSend$identityIgnoringInstance
+ _objc_msgSend$initFromContainerPath:identifier:uuid:schemaVersion:posixOwnership:instanceUUID:userIdentityCache:
+ _objc_msgSend$initWithConcreteContainerIdentity:predecessorContainerIdentity:parentIdentifier:renamePreferences:context:resultPromise:
+ _objc_msgSend$initWithFormerIdentity:predecessorIdentity:renamePreferences:client:date:
+ _objc_msgSend$initWithIdentifier:containerPath:schemaVersion:posixOwnership:instanceUUID:uuid:metadata:userIdentityCache:
+ _objc_msgSend$initWithIdentifier:ownership:instanceUUID:
+ _objc_msgSend$initWithMetadata:finalContainerPath:dataProtectionClass:libraryRepair:error:
+ _objc_msgSend$initWithPlist:
+ _objc_msgSend$initWithUID:primaryGID:homeDirectoryURL:unvalidatedHomeDirectoryURL:name:roleUser:validatedUser:
+ _objc_msgSend$initWithUUID:containerPathIdentifier:identifier:containerConfig:POSIXUser:personaUniqueString:sandboxToken:existed:url:info:transient:userManagedAssetsRelPath:creator:posixOwnership:instanceUUID:
+ _objc_msgSend$initWithUUID:containerPathIdentifier:identifier:containerConfig:POSIXUser:personaUniqueString:sandboxToken:existed:url:info:transient:userManagedAssetsRelPath:creator:posixOwnership:instanceUUID:relativePath:
+ _objc_msgSend$initWithUUID:userIdentity:identifier:containerConfig:platform:posixOwnership:instanceUUID:containerPathIdentifier:existed:transient:userIdentityCache:error:
+ _objc_msgSend$initWithUUID:userIdentity:identifier:containerConfig:platform:posixOwnership:instanceUUID:transient:userIdentityCache:error:
+ _objc_msgSend$initWithUserIdentity:identifier:containerConfig:platform:posixOwnership:instanceUUID:transient:userIdentityCache:error:
+ _objc_msgSend$initWithUserIdentity:identifier:containerConfig:platform:posixOwnership:instanceUUID:userIdentityCache:error:
+ _objc_msgSend$initWithVersion1And2And3PlistDictionary:containerIdentity:error:
+ _objc_msgSend$initWithVersion1PlistDictionary:posixOwnership:instanceUUID:userIdentityCache:error:
+ _objc_msgSend$initWithVersion2PlistDictionary:instanceUUID:userIdentityCache:error:
+ _objc_msgSend$initWithVersion3PlistDictionary:userIdentityCache:error:
+ _objc_msgSend$instanceUUID
+ _objc_msgSend$instanceUUIDForFileHandle:
+ _objc_msgSend$instanceUUIDForURL:
+ _objc_msgSend$isAllowedToSupersedeContainer
+ _objc_msgSend$lock_instanceIndex
+ _objc_msgSend$metadataByChangingSuperseded:
+ _objc_msgSend$metadataByClearingPersistedStatus
+ _objc_msgSend$parentIdentifier
+ _objc_msgSend$posixUserWithError:
+ _objc_msgSend$posixUserWithUID:GID:error:
+ _objc_msgSend$predecessorContainerIdentity
+ _objc_msgSend$predecessorContainerPathIdentifier
+ _objc_msgSend$recordsFormerIdentityWithIdentifier:uuid:
+ _objc_msgSend$removeCacheEntryForIdentity:containerPath:
+ _objc_msgSend$removeContainerForUserIdentity:contentClass:containerIdentity:containerPath:transient:error:
+ _objc_msgSend$removeMappingsForIdentifier:
+ _objc_msgSend$renamePreferences
+ _objc_msgSend$setInstanceUUID:forFileHandle:
+ _objc_msgSend$stageForContainerPathIdentifier:
+ _objc_msgSend$storedDate
+ _objc_msgSend$storedFormerInstanceUUID
+ _objc_msgSend$storedFormerUUID
+ _objc_msgSend$superseded
+ _objc_msgSend$unvalidatedPOSIXUserWithUID:GID:unvalidatedHomeDirectoryURL:
+ _objc_msgSend$usesInstanceUUID
+ _objc_msgSend$validatedUser
+ _objc_msgSend$verificationErrorIsRecoverable:
+ _swift_allocBox
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithTake
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getExistentialTypeMetadata
+ _swift_retain_x25
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_unknownObjectRetain_n
+ _symbolic So24MCMContainerSupersessionC
+ _symbolic So38MCMXPCMessageWithConcreteContainerBaseC
+ _symbolic So40MCMConcreteContainerIdentityForLibsystemCSg
+ _symbolic _____ 22ContainerManagerCommon022MCMXPCMessageSupersedeA0C
+ _symbolic _____ 22ContainerManagerCommon23MCMCommandSupersedePlanO
+ _symbolic _____ 22ContainerManagerCommon23MCMCommandSupersedePlanO9PreflightO
+ _symbolic _____ 22ContainerManagerCommon27MCMCommandSupersedeExecutorV
+ _symbolic _____ 22ContainerManagerCommon27MCMCommandSupersedeExecutorV8Progress33_E7A3FEDC1F76939CD5C7857805CE17D5LLV
+ _symbolic _____ 22ContainerManagerCommon29MCMCommandSupersedeResumptionV
+ _symbolic _____ 22ContainerManagerCommon29MCMCommandSupersedeResumptionV5FoundV
+ _symbolic _____ So17container_error_ta
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____Sg 10Foundation4UUIDV
+ _symbolic ______p So11MCMMetadataP
+ _symbolic ______p So14MCMFileManagerP
+ _symbolic ______p So17MCMCommandContextP
+ _symbolic ______p So22MCMContainerCacheEntryP
+ _symbolic ______pSg So11MCMMetadataP
+ _symbolic _____ySo15MCMUserIdentityCG s11_SetStorageC
+ _symbolic _____y_____G s16IteratorSequenceV 10Foundation017NSFastEnumerationA0V
+ _symbolic _____y_____ypG s18_DictionaryStorageC s11AnyHashableV
+ _symbolic _____yyXlG s23_ContiguousArrayStorageC
+ _type_layout_string 22ContainerManagerCommon23MCMCommandSupersedePlanO9PreflightO
+ _type_layout_string 22ContainerManagerCommon27MCMCommandSupersedeExecutorV
+ _type_layout_string 22ContainerManagerCommon29MCMCommandSupersedeResumptionV
+ _type_layout_string 22ContainerManagerCommon29MCMCommandSupersedeResumptionV5FoundV
+ _type_layout_string So17container_error_ta
- +[MCMConcreteContainerIdentity containerIdentityWithUUID:userIdentity:identifier:containerConfig:platform:posixOwnership:transient:userIdentityCache:error:]
- +[MCMConcreteContainerIdentityForLibsystem containerIdentityWithUUID:userIdentity:identifier:containerConfig:platform:posixOwnership:containerPathIdentifier:existed:transient:userIdentityCache:error:]
- +[MCMContainerSchema containerSchemaWithMetadata:finalContainerPath:dataProtectionClass:libraryRepair:]
- +[MCMPOSIXUser _getCachedUID:GID:name:flush:onCacheMiss:]
- +[MCMPOSIXUser _posixUserWithUID:GID:name:]
- -[MCMChildParentMapCache cache]
- -[MCMCommandUserDataMigration _replaceContainer:withContainer:changingParentIdentifier:]
- -[MCMConcreteContainerIdentity initWithUUID:userIdentity:identifier:containerConfig:platform:posixOwnership:transient:userIdentityCache:error:]
- -[MCMConcreteContainerIdentity initWithVersion1And2PlistDictionary:containerIdentity:error:]
- -[MCMConcreteContainerIdentityForLibsystem initWithUUID:userIdentity:identifier:containerConfig:platform:posixOwnership:containerPathIdentifier:existed:transient:userIdentityCache:error:]
- -[MCMContainerCacheEntry _fabricateMetadataForContainerPath:identifier:uuid:schemaVersion:posixOwnership:userIdentityCache:]
- -[MCMContainerCacheEntry _metadataFromContainerPath:identifier:uuid:schemaVersion:posixOwnership:userIdentityCache:]
- -[MCMContainerCacheEntry initFromContainerPath:identifier:uuid:schemaVersion:posixOwnership:userIdentityCache:]
- -[MCMContainerCacheEntry initWithIdentifier:containerPath:schemaVersion:posixOwnership:uuid:metadata:userIdentityCache:]
- -[MCMContainerClassCache _concurrent_generateCacheEntryWithURL:identifier:containerPath:schemaVersion:posixOwnership:uuid:metadata:]
- -[MCMContainerClassCache _concurrent_slowGenerateCacheEntryWithFileHandle:URL:identifier:uuid:schemaVersion:posixOwnership:containerPath:]
- -[MCMContainerClassCache cacheEntryForIdentity:]
- -[MCMContainerIdentity initWithUserIdentity:identifier:containerConfig:platform:posixOwnership:transient:userIdentityCache:error:]
- -[MCMContainerIdentity initWithVersion1PlistDictionary:posixOwnership:userIdentityCache:error:]
- -[MCMContainerIdentity initWithVersion2PlistDictionary:userIdentityCache:error:]
- -[MCMContainerIdentityMinimal initWithUserIdentity:identifier:containerConfig:platform:posixOwnership:userIdentityCache:error:]
- -[MCMContainerIdentityMinimal initWithVersion1PlistDictionary:posixOwnership:userIdentityCache:error:]
- -[MCMContainerIdentityMinimal initWithVersion2PlistDictionary:userIdentityCache:error:]
- -[MCMContainerSchema initWithMetadata:finalContainerPath:dataProtectionClass:libraryRepair:]
- -[MCMPOSIXPermission initWithUID:GID:mode:isNull:]
- -[MCMPOSIXPermission posixUser]
- -[MCMPOSIXUser initWithUID:primaryGID:homeDirectoryURL:unvalidatedHomeDirectoryURL:name:roleUser:]
- -[MCMResultContainerFromPath initWithUUID:containerPathIdentifier:identifier:containerConfig:POSIXUser:personaUniqueString:sandboxToken:existed:url:info:transient:userManagedAssetsRelPath:creator:posixOwnership:relativePath:]
- -[MCMResultWithContainerBase initWithUUID:containerPathIdentifier:identifier:containerConfig:POSIXUser:personaUniqueString:sandboxToken:existed:url:info:transient:userManagedAssetsRelPath:creator:posixOwnership:]
- GCC_except_table1021
- GCC_except_table1023
- GCC_except_table1079
- GCC_except_table1088
- GCC_except_table1092
- GCC_except_table1141
- GCC_except_table1142
- GCC_except_table1158
- GCC_except_table1160
- GCC_except_table1164
- GCC_except_table1169
- GCC_except_table1172
- GCC_except_table1178
- GCC_except_table1184
- GCC_except_table1187
- GCC_except_table1189
- GCC_except_table1193
- GCC_except_table1195
- GCC_except_table1197
- GCC_except_table1203
- GCC_except_table1208
- GCC_except_table1216
- GCC_except_table1231
- GCC_except_table1235
- GCC_except_table1237
- GCC_except_table1292
- GCC_except_table1302
- GCC_except_table1333
- GCC_except_table1571
- GCC_except_table1721
- GCC_except_table1725
- GCC_except_table1879
- GCC_except_table1885
- GCC_except_table1987
- GCC_except_table2121
- GCC_except_table2262
- GCC_except_table2279
- GCC_except_table2280
- GCC_except_table2345
- GCC_except_table2391
- GCC_except_table2407
- GCC_except_table2428
- GCC_except_table2497
- GCC_except_table2509
- GCC_except_table2578
- GCC_except_table2588
- GCC_except_table2613
- GCC_except_table2636
- GCC_except_table2646
- GCC_except_table2670
- GCC_except_table2672
- GCC_except_table2675
- GCC_except_table2680
- GCC_except_table2726
- GCC_except_table2730
- GCC_except_table2896
- GCC_except_table2899
- GCC_except_table2976
- GCC_except_table305
- GCC_except_table323
- GCC_except_table342
- GCC_except_table361
- GCC_except_table384
- GCC_except_table393
- GCC_except_table490
- GCC_except_table677
- GCC_except_table763
- GCC_except_table865
- GCC_except_table942
- GCC_except_table990
- _OBJC_IVAR_$_MCMChildParentMapCache._cache
- _OBJC_IVAR_$_MCMPOSIXPermission._posixUser
- ___37+[MCMPOSIXUser posixUserWithUID:GID:]_block_invoke
- ___39-[MCMChildParentMapCache capturedState]_block_invoke
- ___43+[MCMPOSIXUser _posixUserWithUID:GID:name:]_block_invoke
- ___57+[MCMPOSIXUser _getCachedUID:GID:name:flush:onCacheMiss:]_block_invoke
- ___99-[MCMContainerCache removeContainerForUserIdentity:contentClass:containerIdentity:transient:error:]_block_invoke
- ___block_descriptor_48_e19_"MCMPOSIXUser"8?0l
- ___block_descriptor_48_e8_32s_e19_"MCMPOSIXUser"8?0ls32l8
- __getCachedUID:GID:name:flush:onCacheMiss:.cacheByName
- __getCachedUID:GID:name:flush:onCacheMiss:.cacheByUID
- __getCachedUID:GID:name:flush:onCacheMiss:.cacheByUIDGID
- __getCachedUID:GID:name:flush:onCacheMiss:.onceToken
- _objc_msgSend$_concurrent_generateCacheEntryWithURL:identifier:containerPath:schemaVersion:posixOwnership:uuid:metadata:
- _objc_msgSend$_concurrent_slowGenerateCacheEntryWithFileHandle:URL:identifier:uuid:schemaVersion:posixOwnership:containerPath:
- _objc_msgSend$_fabricateMetadataForContainerPath:identifier:uuid:schemaVersion:posixOwnership:userIdentityCache:
- _objc_msgSend$_getCachedUID:GID:name:flush:onCacheMiss:
- _objc_msgSend$_metadataFromContainerPath:identifier:uuid:schemaVersion:posixOwnership:userIdentityCache:
- _objc_msgSend$_posixUserWithUID:GID:name:
- _objc_msgSend$_replaceContainer:withContainer:changingParentIdentifier:
- _objc_msgSend$cacheEntryForIdentity:
- _objc_msgSend$containerIdentityWithUUID:userIdentity:identifier:containerConfig:platform:posixOwnership:containerPathIdentifier:existed:transient:userIdentityCache:error:
- _objc_msgSend$containerIdentityWithUUID:userIdentity:identifier:containerConfig:platform:posixOwnership:transient:userIdentityCache:error:
- _objc_msgSend$containerSchemaWithMetadata:finalContainerPath:dataProtectionClass:libraryRepair:
- _objc_msgSend$initFromContainerPath:identifier:uuid:schemaVersion:posixOwnership:userIdentityCache:
- _objc_msgSend$initWithIdentifier:containerPath:schemaVersion:posixOwnership:uuid:metadata:userIdentityCache:
- _objc_msgSend$initWithIdentifier:ownership:
- _objc_msgSend$initWithMetadata:finalContainerPath:dataProtectionClass:libraryRepair:
- _objc_msgSend$initWithUID:GID:mode:isNull:
- _objc_msgSend$initWithUID:primaryGID:homeDirectoryURL:unvalidatedHomeDirectoryURL:name:roleUser:
- _objc_msgSend$initWithUUID:containerPathIdentifier:identifier:containerConfig:POSIXUser:personaUniqueString:sandboxToken:existed:url:info:transient:userManagedAssetsRelPath:creator:posixOwnership:
- _objc_msgSend$initWithUUID:containerPathIdentifier:identifier:containerConfig:POSIXUser:personaUniqueString:sandboxToken:existed:url:info:transient:userManagedAssetsRelPath:creator:posixOwnership:relativePath:
- _objc_msgSend$initWithUUID:userIdentity:identifier:containerConfig:platform:posixOwnership:containerPathIdentifier:existed:transient:userIdentityCache:error:
- _objc_msgSend$initWithUUID:userIdentity:identifier:containerConfig:platform:posixOwnership:transient:userIdentityCache:error:
- _objc_msgSend$initWithUserIdentity:identifier:containerConfig:platform:posixOwnership:transient:userIdentityCache:error:
- _objc_msgSend$initWithUserIdentity:identifier:containerConfig:platform:posixOwnership:userIdentityCache:error:
- _objc_msgSend$initWithVersion1And2PlistDictionary:containerIdentity:error:
- _objc_msgSend$initWithVersion1PlistDictionary:posixOwnership:userIdentityCache:error:
- _objc_msgSend$initWithVersion2PlistDictionary:userIdentityCache:error:
- _objc_msgSend$stringWithFileSystemRepresentation:
CStrings:
+ "%llu-%@-%d-%@-%@%@%@"
+ "%s built a no-instance identity for class %s"
+ "(%@|g%llu|%@|s%@|u%@|O%@|i%@|x%@%s%s)"
+ "+[MCMConcreteContainerIdentity containerIdentityWithUUID:userIdentity:identifier:containerConfig:platform:posixOwnership:userIdentityCache:error:]"
+ "+[MCMContainerIdentity containerIdentityWithIdentifier:containerConfig:platform:posixOwnership:userIdentityCache:error:]"
+ "+[MCMContainerIdentity containerIdentityWithUserIdentity:identifier:containerConfig:platform:posixOwnership:transient:userIdentityCache:error:]"
+ "+[MCMContainerIdentity containerIdentityWithUserIdentity:identifier:containerConfig:platform:posixOwnership:userIdentityCache:error:]"
+ "-%@"
+ ":superseded"
+ "<%@(%@%s);%@;O%@;x%@;u%@;p%@;pf%d%s>"
+ "<%@(%@%s);%@;O%@;x%@;u%@;pf%d>"
+ "<%@(%@%s);%@;pf%d;O%@;x%@>"
+ "<%@(%@%s);%@;u%@;p%@;dp%d;uma%@;x%@%@>"
+ "<%@(%@-);%@;pf%d;O%@;x%@>"
+ "<%@: %p; identifier = %@, generation = %llu, containerPath = %@, schemaVersion = %@, uuid = %@, posixOwnership = %@, fsNode = %@, instanceUUID = %@%s%s>"
+ "<%@: %p; userIdentity = %@, identifier = %@, class = %@, platform = %d, ownership = %@, instanceUUID = %@, transient = %d, uuid = %@, containerPathIdentifier = %@, existed = %d>"
+ "<%@: %p; userIdentity = %@, identifier = %@, class = %@, platform = %d, ownership = %@, instanceUUID = %@, transient = %d, uuid = %@>"
+ "<%@: %p; userIdentity = %@, identifier = %@, class = %@, platform = %d, ownership = %@, instanceUUID = %@, transient = %d>"
+ "<%@: %p; userIdentity = %@, identifier = %@, class = %@, platform = %d, ownership = %@, instanceUUID = %@>"
+ "<%@: %p; userIdentity = %@, uuid = %@, containerClass = %@, transient = %d, identifier = %@, containerPath = %@, dataProtectionClass = %d, userManagedAssetsDirName = %@, instanceUUID = %@, superseded = %d>"
+ "<containermanager>"
+ "@\"MCMPOSIXUser\"16@?0^@8"
+ "Abandoned supersede after moving the survivor; the surviving container is on disk but not in the cache; identifier = [🔒%{private}s]-->[🔒%{private}s], error = %@"
+ "Cache entry failed verification, instance UUID doesn't match; cacheEntry = %@, current instanceUUID = %@"
+ "Cannot resume a supersede whose record predates the predecessor path identifier; identifier = [🔒%{private}s]"
+ "Claimed container; container = %@, instanceUUID = %@"
+ "Container owned by non-existent user (%@|%@|%@|%@), deleting; path = %@, error = %@"
+ "ContainerManagerCommon.MCMXPCMessageSupersedeContainer"
+ "ContainerManagerCommon_Internal.MCMCommandSupersedeContainer"
+ "ContainerManagerCommon_Internal.MCMContainerSupersession"
+ "Could not delete container with mismatched instance UUID; path = %@, error = %@"
+ "Could not generate posix user details for user=[%@]"
+ "Could not read the child/parent map, starting empty; error = %@"
+ "Created new POSIX user: [%@]"
+ "DELETED: [%@] (mismatched instance UUID); existing = [%@], requested = [%@]"
+ "Default POSIX owner is invalid; owner = %@, error = %@"
+ "Failed reading metadata during claim; container = %@; error = %@"
+ "Failed to add surviving container to cache for supersede; metadata = %s, error = %s"
+ "Failed to build successor container identity; error = (%llu) %s"
+ "Failed to decode successor container; error = (%llu) %s"
+ "Failed to delete superseded container for supersede; path = 🔒%{private}s, error = %s"
+ "Failed to derive new metadata for supersede; successor = %s"
+ "Failed to get xattr instance uuid; error = %@"
+ "Failed to invalidate code signing info after supersede; identifier = [🔒%{private}s], error = %@"
+ "Failed to move successor into the predecessor's place for supersede; from = 🔒%{private}s, to = 🔒%{private}s, error = %@"
+ "Failed to rebuild a container path while resuming a supersede: %@"
+ "Failed to restate the survivor's path after resuming a supersede: %s"
+ "Failed to restore metadata after abandoning supersede; identifier = [🔒%{private}s], error = %s"
+ "Failed to restore predecessor to cache after abandoning supersede; identifier = [🔒%{private}s], error = %s"
+ "Failed to restore survivor to cache after abandoning supersede; identifier = [🔒%{private}s], error = %s"
+ "Failed to set xattr instance uuid; error = %@"
+ "Failed writing metadata during claim; container = %@; error = %@"
+ "Found an in-flight supersession by scanning the class directory, which the cache could not report; identifier = [🔒%{private}s], path = [🔒%{private}s]"
+ "Ignoring a supersession record whose container is at neither path it names; identifier = [🔒%{private}s], here = [🔒%{private}s]"
+ "InstanceUUID"
+ "Invalid container identity plist data. Invalid %@. Data: %@"
+ "Invalid container identity plist data. Invalid %@; string = [%@]"
+ "Invalid metadata Superseded: %@"
+ "Invalid metadata Superseded; failed to interpret: %@"
+ "Invalid metadata instance UUID [%@(%{public}@)]: %@"
+ "Invalid metadata instance UUID type [%@(%{public}@)]: %@"
+ "MCMMetadataInstanceUUID"
+ "MCMMetadataSuperseded"
+ "MCMSupersessionClient"
+ "MCMSupersessionDate"
+ "MCMSupersessionFormerContainerPathIdentifier"
+ "MCMSupersessionFormerIdentifier"
+ "MCMSupersessionFormerInstanceUUID"
+ "MCMSupersessionFormerUUID"
+ "MCMSupersessionPredecessorContainerPathIdentifier"
+ "MCMSupersessionRenamePreferences"
+ "MCMSupersessionVersion"
+ "Matching cache entry found, but failed to claim: requested = [%@]"
+ "Matching cache entry found, but instance UUIDs mismatch: requested = [%@] vs. cache entry = [%@]"
+ "MobileContainerManager-833.40.14~50"
+ "No %s container with identity: %@; error = %s"
+ "No predecessor container provided for supersede"
+ "Nothing to resume: no supersession is in flight for [🔒%{private}s]"
+ "Ownership specifies a non-existent user [%u]; error = %@"
+ "Refusing a supersede carrying flags this daemon does not implement; flags = %llx, known = %llx"
+ "Refusing to supersede a container with one that already has its identifier; identifier = [🔒%{private}s]"
+ "Refusing to supersede across container classes; successor = %llu, predecessor = %llu"
+ "Refusing to supersede across users; successor = %s, predecessor = %s"
+ "Refusing to supersede: [🔒%{private}s] already took this identity over from a different container called [🔒%{private}s], recorded = %s"
+ "Resuming a supersede that did not get past its metadata write; identifier = [🔒%{private}s]-->[🔒%{private}s], recorded = %s"
+ "Retrieved cache entries ignoring instance; identity = %@, count = %lu"
+ "Retrieving cache entries ignoring instance; identity = %@, count = %lu"
+ "Schema creation failed; error = %@"
+ "Skipping a candidate whose metadata would not read while resuming a supersede; path = 🔒%{private}s, error = %s"
+ "Skipping a claimant whose metadata will not read while resuming a supersede; identifier = [🔒%{private}s], error = %s"
+ "Successor container has no metadata file URL: %s"
+ "SuccessorContainer"
+ "Supersede already carried out, so reporting it as done rather than repeating it; identifier = [🔒%{private}s]-->[🔒%{private}s], recorded = %s"
+ "Supersede already carried out, so resuming reports it as done; identifier = [🔒%{private}s]-->[🔒%{private}s], recorded = %s"
+ "Superseded; identifier = [🔒%{private}s]-->[🔒%{private}s]"
+ "Unable to enumerate claimants while resuming a supersede; identifier = [🔒%{private}s], error = %s"
+ "Unable to fetch posix user %u when constructing schema; error = %@"
+ "Unable to get user (%u/[%@]); error = %{public}@"
+ "Unable to migrate container identity; fromIdentifier = [%@], toIdentifier = [%@], userIdentity = %@, error = %@"
+ "Unable to read the class directory while resuming a supersede; path = 🔒%{private}s, error = %@"
+ "Unable to remove predecessor from cache for supersede; identifier = [🔒%{private}s], userIdentity = %s, error = %s"
+ "Unable to remove successor from cache for supersede; identifier = [🔒%{private}s], userIdentity = %s, error = %s"
+ "Unable to rename preference domain for supersede; from = 🔒%{private}s, to = 🔒%{private}s, error = %@"
+ "Unable to resolve the class directory while resuming a supersede; identifier = [🔒%{private}s], class = %llu"
+ "Unable to take a container out of the cache while resuming a supersede; identifier = [🔒%{private}s], path = [🔒%{private}s], error = %s"
+ "Unable to write new metadata for supersede; identifier = [🔒%{private}s], error = %s"
+ "Updating [🔒%{private}s] parent key to [🔒%{private}s]"
+ "User home directory at [%@] does not exist"
+ "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu:x 🔒%{private}@] Action [%@] failed; error = %@"
+ "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu:x 🔒%{private}@] Could not fetch fsNode for [%@]: %{public}@"
+ "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu:x 🔒%{private}@] Could not form action [%@] with args: %@, error = %@"
+ "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu:x 🔒%{private}@] Could not update schema from (%{public}@) → (%{public}@), actions count = %{public}lu, error = %{public}@"
+ "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu:x 🔒%{private}@] Could not update schema from (%{public}@) → (%{public}@), no actions available"
+ "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu:x 🔒%{private}@] Read metadata from [%@]: %@"
+ "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu:x 🔒%{private}@] Successfully updated schema from (%{public}@) → (%{public}@), actions count = %{public}lu"
+ "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu:x 🔒%{private}@] Trying to target a version [%@] higher than available [%lu], capping to max"
+ "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu:x 🔒%{private}@] Wrote metadata to [%@]: %@"
+ "com.apple.containermanager.instance-uuid"
+ "com.apple.private.MobileContainerManager.supersede"
+ "container_realpath([%@]) failed: %{public, darwin.errno}d"
+ "container_realpath([%@]) → [%@]"
+ "init(concreteContainer:context:)"
+ "instanceUUID"
+ "predecessor"
+ "successor"
+ "\x91"
- "%llu-%@-%d-%@-%@%@"
- "(%@|%llu|%@|%@|%@|%@|%@%s%s)"
- "<%@(%@%s);%@;O%@;u%@;p%@;pf%d%s>"
- "<%@(%@%s);%@;O%@;u%@;pf%d>"
- "<%@(%@%s);%@;pf%d;O%@>"
- "<%@(%@%s);%@;u%@;p%@;dp%d;uma%@>"
- "<%@(%@-);%@;pf%d;%@>"
- "<%@: %p; identifier = %@, generation = %llu, containerPath = %@, schemaVersion = %@, uuid = %@, posixOwnership = %@, fsNode = %@%s%s>"
- "<%@: %p; userIdentity = %@, identifier = %@, class = %@, platform = %d, ownership = %@, transient = %d, uuid = %@, containerPathIdentifier = %@, existed = %d>"
- "<%@: %p; userIdentity = %@, identifier = %@, class = %@, platform = %d, ownership = %@, transient = %d, uuid = %@>"
- "<%@: %p; userIdentity = %@, identifier = %@, class = %@, platform = %d, ownership = %@, transient = %d>"
- "<%@: %p; userIdentity = %@, identifier = %@, class = %@, platform = %d, ownership = %@>"
- "<%@: %p; userIdentity = %@, uuid = %@, containerClass = %@, transient = %d, identifier = %@, containerPath = %@, dataProtectionClass = %d, userManagedAssetsDirName = %@>"
- "@\"MCMPOSIXUser\"8@?0"
- "Could not generate posix user details for user=%{public}@"
- "Created new POSIX user: %{public}@"
- "Failed to re-add container to cache for migration; metadata = %@, error = %@"
- "Migrated [%@]-->[%@]"
- "MobileContainerManager-833.0.8.0.1~204"
- "Preferences"
- "Unable to delete old container for migration; fromIdentifier = [%@], toIdentifier = [%@], userIdentity = %@, error = %@"
- "Unable to fetch metadata for (from) container for migration; identifier = [%@], userIdentity = %@, error = %@"
- "Unable to get user (%u/[%@]); error = %{public}s"
- "Unable to remove (from) container from cache for migration; identifier = [%@], userIdentity = %@, error = %@"
- "Unable to remove (to) container from cache for migration; identifier = [%@], userIdentity = %@, error = %@"
- "Unable to rename prefs for migration; fromPreferencesURL = [%@], toPreferencesURL = [%@], userIdentity = %@, error = %@"
- "Unable to replace containers for migration; fromIdentifier = [%@], toIdentifier = [%@], userIdentity = %@, error = %@"
- "Unable to write new metadata to (from) container for migration; identifier = [%@], userIdentity = %@, error = %@"
- "Updating [%@] parent key to [%@]"
- "User home directory at [%{public}@] does not exist"
- "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu] Action [%@] failed; error = %@"
- "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu] Could not fetch fsNode for [%@]: %{public}@"
- "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu] Could not form action [%@] with args: %@, error = %@"
- "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu] Could not update schema from (%{public}@) → (%{public}@), actions count = %{public}lu, error = %{public}@"
- "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu] Could not update schema from (%{public}@) → (%{public}@), no actions available"
- "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu] Read metadata from [%@]: %@"
- "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu] Successfully updated schema from (%{public}@) → (%{public}@), actions count = %{public}lu"
- "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu] Trying to target a version [%@] higher than available [%lu], capping to max"
- "[u %{public}@:p 🔒%{private}@:c %@(%{public}@):i%llu] Wrote metadata to [%@]: %@"
- "container_realpath([%{public}@]) failed: %{public, darwin.errno}d"
- "container_realpath([%{public}@]) → [%{public}@]"
- "\x81"
```
