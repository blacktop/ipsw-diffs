## ContainerManagerCommon

> `/System/Library/PrivateFrameworks/ContainerManagerCommon.framework/Versions/A/ContainerManagerCommon`

```diff

-833.0.8.0.1
-  __TEXT.__text: 0xf5144
-  __TEXT.__objc_methlist: 0xad24
-  __TEXT.__const: 0x1378
-  __TEXT.__swift5_typeref: 0x6bb
-  __TEXT.__oslogstring: 0xd45c
-  __TEXT.__cstring: 0x9df4
-  __TEXT.__constg_swiftt: 0x650
-  __TEXT.__swift5_reflstr: 0x39a
-  __TEXT.__swift5_fieldmd: 0x458
-  __TEXT.__swift5_builtin: 0xf0
+833.40.14.0.0
+  __TEXT.__text: 0x1090d8
+  __TEXT.__objc_methlist: 0xb26c
+  __TEXT.__const: 0x1598
+  __TEXT.__swift5_typeref: 0x843
+  __TEXT.__oslogstring: 0xeb7c
+  __TEXT.__cstring: 0xa434
+  __TEXT.__constg_swiftt: 0x790
+  __TEXT.__swift5_reflstr: 0x52a
+  __TEXT.__swift5_fieldmd: 0x5d4
+  __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_assocty: 0x138
   __TEXT.__swift5_proto: 0xb0
-  __TEXT.__swift5_types: 0x94
+  __TEXT.__swift5_types: 0xb4
+  __TEXT.__swift5_capture: 0x88
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__swift5_capture: 0x58
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__gcc_except_tab: 0x2348
+  __TEXT.__gcc_except_tab: 0x23f4
   __TEXT.__ustring: 0x16c
-  __TEXT.__unwind_info: 0x3ab0
-  __TEXT.__eh_frame: 0x5d8
+  __TEXT.__unwind_info: 0x3da8
+  __TEXT.__eh_frame: 0x958
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x448
-  __DATA_CONST.__objc_classlist: 0x5b8
-  __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x530
+  __DATA_CONST.__const: 0x450
+  __DATA_CONST.__objc_classlist: 0x5d0
+  __DATA_CONST.__objc_catlist: 0x30
+  __DATA_CONST.__objc_protolist: 0x618
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x36b8
-  __DATA_CONST.__objc_protorefs: 0xc8
+  __DATA_CONST.__objc_selrefs: 0x38b0
+  __DATA_CONST.__objc_protorefs: 0x1a8
   __DATA_CONST.__objc_superrefs: 0x4a8
-  __DATA_CONST.__objc_arraydata: 0x3c8
-  __DATA_CONST.__got: 0x510
-  __AUTH_CONST.__const: 0x2918
-  __AUTH_CONST.__cfstring: 0x5640
-  __AUTH_CONST.__objc_const: 0x16f70
+  __DATA_CONST.__objc_arraydata: 0x3d0
+  __DATA_CONST.__got: 0x530
+  __AUTH_CONST.__const: 0x2c10
+  __AUTH_CONST.__cfstring: 0x5720
+  __AUTH_CONST.__objc_const: 0x177f0
   __AUTH_CONST.__objc_dictobj: 0x3e8
-  __AUTH_CONST.__objc_intobj: 0x15c0
+  __AUTH_CONST.__objc_intobj: 0x15d8
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__auth_got: 0x1120
-  __AUTH.__objc_data: 0xcd0
-  __AUTH.__data: 0xd0
-  __DATA.__objc_ivar: 0xbfc
-  __DATA.__data: 0x3bc0
+  __AUTH_CONST.__auth_got: 0x1230
+  __AUTH.__objc_data: 0xea0
+  __AUTH.__data: 0x1e8
+  __DATA.__objc_ivar: 0xc34
+  __DATA.__data: 0x3d70
   __DATA.__crash_info: 0x148
+  __DATA.__common: 0x48
   __DATA_DIRTY.__objc_data: 0x3070
-  __DATA_DIRTY.__data: 0x450
+  __DATA_DIRTY.__data: 0x460
   __DATA_DIRTY.__bss: 0x850
   __DATA_DIRTY.__common: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3651
-  Symbols:   8439
-  CStrings:  2008
+  Functions: 3848
+  Symbols:   8630
+  CStrings:  2102
 
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
+ GCC_except_table1030
+ GCC_except_table1034
+ GCC_except_table1045
+ GCC_except_table1088
+ GCC_except_table1097
+ GCC_except_table1103
+ GCC_except_table1153
+ GCC_except_table1170
+ GCC_except_table1177
+ GCC_except_table1186
+ GCC_except_table1190
+ GCC_except_table1192
+ GCC_except_table1199
+ GCC_except_table1202
+ GCC_except_table1204
+ GCC_except_table1214
+ GCC_except_table1217
+ GCC_except_table1219
+ GCC_except_table1229
+ GCC_except_table1244
+ GCC_except_table1248
+ GCC_except_table1250
+ GCC_except_table1305
+ GCC_except_table1315
+ GCC_except_table1346
+ GCC_except_table1587
+ GCC_except_table1734
+ GCC_except_table1738
+ GCC_except_table1891
+ GCC_except_table1897
+ GCC_except_table2000
+ GCC_except_table2139
+ GCC_except_table2291
+ GCC_except_table2308
+ GCC_except_table2309
+ GCC_except_table2374
+ GCC_except_table2420
+ GCC_except_table2434
+ GCC_except_table2455
+ GCC_except_table2524
+ GCC_except_table2536
+ GCC_except_table2602
+ GCC_except_table2614
+ GCC_except_table2639
+ GCC_except_table2666
+ GCC_except_table2690
+ GCC_except_table2693
+ GCC_except_table2696
+ GCC_except_table2703
+ GCC_except_table2753
+ GCC_except_table2757
+ GCC_except_table2928
+ GCC_except_table2932
+ GCC_except_table3012
+ GCC_except_table310
+ GCC_except_table333
+ GCC_except_table353
+ GCC_except_table374
+ GCC_except_table403
+ GCC_except_table412
+ GCC_except_table696
+ GCC_except_table790
+ GCC_except_table945
+ GCC_except_table998
+ MCM_null.onceToken
+ MCM_null.uuid
+ OBJC_IVAR_$_MCMChildParentMapCache._cacheLock
+ OBJC_IVAR_$_MCMChildParentMapCache._lock_cache
+ OBJC_IVAR_$_MCMCommandQuery._defaultInstanceUUID
+ OBJC_IVAR_$_MCMCommandQuery._instanceUUID
+ OBJC_IVAR_$_MCMContainerCacheEntry._instanceUUID
+ OBJC_IVAR_$_MCMContainerClassCache._lock_instanceIndex
+ OBJC_IVAR_$_MCMContainerConfiguration._deleteCorruptContainers
+ OBJC_IVAR_$_MCMContainerConfiguration._usesInstanceUUID
+ OBJC_IVAR_$_MCMContainerIdentityMinimal._instanceUUID
+ OBJC_IVAR_$_MCMMetadata._superseded
+ OBJC_IVAR_$_MCMPOSIXPermission._lock_posixUser
+ OBJC_IVAR_$_MCMPOSIXPermission._posixUserLock
+ OBJC_IVAR_$_MCMPOSIXUser._validatedUser
+ OBJC_IVAR_$_MCMResultWithContainerBase._instanceUUID
+ OBJC_IVAR_$_MCMXPCMessageQuery._defaultInstanceUUID
+ OBJC_IVAR_$_MCMXPCMessageQuery._instanceUUID
+ _MCMParentBundleKey
+ _OBJC_CLASS_$_MCMCommandSupersedeContainer
+ _OBJC_CLASS_$_MCMContainerSupersession
+ _OBJC_CLASS_$__TtC22ContainerManagerCommon31MCMXPCMessageSupersedeContainer
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
+ ___block_descriptor_48_e8_32s_e23_"MCMPOSIXUser"16?0^8l
+ ___swift_allocate_boxed_opaque_existential_0
+ ___swift_memcpy40_8
+ ___swift_project_boxed_opaque_existential_0
+ __objc_autoreleasePoolPop
+ __objc_autoreleasePoolPush
+ _container_get_instance_uuid
+ _flat unique So11MCMMetadata_p
+ _flat unique So14MCMFileManager_p
+ _flat unique So17MCMCommandContext_p
+ _flat unique So22MCMContainerCacheEntry_p
+ _getCachedUID:GID:name:flush:error:onCacheMiss:.cacheByName
+ _getCachedUID:GID:name:flush:error:onCacheMiss:.cacheByUID
+ _getCachedUID:GID:name:flush:error:onCacheMiss:.cacheByUIDGID
+ _getCachedUID:GID:name:flush:error:onCacheMiss:.onceToken
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
+ _swift_retain_n
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
- GCC_except_table1008
- GCC_except_table1012
- GCC_except_table1023
- GCC_except_table1066
- GCC_except_table1075
- GCC_except_table1081
- GCC_except_table1130
- GCC_except_table1131
- GCC_except_table1147
- GCC_except_table1150
- GCC_except_table1154
- GCC_except_table1160
- GCC_except_table1163
- GCC_except_table1167
- GCC_except_table1169
- GCC_except_table1171
- GCC_except_table1176
- GCC_except_table1179
- GCC_except_table1181
- GCC_except_table1191
- GCC_except_table1221
- GCC_except_table1225
- GCC_except_table1227
- GCC_except_table1282
- GCC_except_table1292
- GCC_except_table1323
- GCC_except_table1561
- GCC_except_table1708
- GCC_except_table1712
- GCC_except_table1865
- GCC_except_table1871
- GCC_except_table1973
- GCC_except_table2109
- GCC_except_table2259
- GCC_except_table2276
- GCC_except_table2277
- GCC_except_table2342
- GCC_except_table2388
- GCC_except_table2402
- GCC_except_table2423
- GCC_except_table2492
- GCC_except_table2504
- GCC_except_table2570
- GCC_except_table2582
- GCC_except_table2607
- GCC_except_table2634
- GCC_except_table2657
- GCC_except_table2659
- GCC_except_table2662
- GCC_except_table2669
- GCC_except_table2717
- GCC_except_table2721
- GCC_except_table2891
- GCC_except_table2894
- GCC_except_table2971
- GCC_except_table300
- GCC_except_table323
- GCC_except_table343
- GCC_except_table364
- GCC_except_table393
- GCC_except_table402
- GCC_except_table685
- GCC_except_table768
- GCC_except_table931
- GCC_except_table979
- OBJC_IVAR_$_MCMChildParentMapCache._cache
- OBJC_IVAR_$_MCMPOSIXPermission._posixUser
- ___37+[MCMPOSIXUser posixUserWithUID:GID:]_block_invoke
- ___39-[MCMChildParentMapCache capturedState]_block_invoke
- ___43+[MCMPOSIXUser _posixUserWithUID:GID:name:]_block_invoke
- ___57+[MCMPOSIXUser _getCachedUID:GID:name:flush:onCacheMiss:]_block_invoke
- ___99-[MCMContainerCache removeContainerForUserIdentity:contentClass:containerIdentity:transient:error:]_block_invoke
- ___block_descriptor_48_e19_"MCMPOSIXUser"8?0l
- ___block_descriptor_48_e8_32s_e19_"MCMPOSIXUser"8?0l
- _getCachedUID:GID:name:flush:onCacheMiss:.cacheByName
- _getCachedUID:GID:name:flush:onCacheMiss:.cacheByUID
- _getCachedUID:GID:name:flush:onCacheMiss:.cacheByUIDGID
- _getCachedUID:GID:name:flush:onCacheMiss:.onceToken
- _objc_msgSend$_concurrent_generateCacheEntryWithURL:identifier:containerPath:schemaVersion:posixOwnership:uuid:metadata:
- _objc_msgSend$_concurrent_slowGenerateCacheEntryWithFileHandle:URL:identifier:uuid:schemaVersion:posixOwnership:containerPath:
- _objc_msgSend$_fabricateMetadataForContainerPath:identifier:uuid:schemaVersion:posixOwnership:userIdentityCache:
- _objc_msgSend$_getCachedUID:GID:name:flush:onCacheMiss:
- _objc_msgSend$_metadataFromContainerPath:identifier:uuid:schemaVersion:posixOwnership:userIdentityCache:
- _objc_msgSend$_posixUserWithUID:GID:name:
- _objc_msgSend$cacheEntryForIdentity:
- _objc_msgSend$containerIdentityWithUUID:userIdentity:identifier:containerConfig:platform:posixOwnership:containerPathIdentifier:existed:transient:userIdentityCache:error:
- _objc_msgSend$containerIdentityWithUUID:userIdentity:identifier:containerConfig:platform:posixOwnership:transient:userIdentityCache:error:
- _objc_msgSend$containerIdentityWithUserIdentity:identifier:containerConfig:platform:posixOwnership:transient:userIdentityCache:error:
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
+ "%s built a no-instance identity for class %s"
+ "(%@|g%llu|%@|s%@|u%@|O%@|i%@|x%@%s%s)"
+ "+[MCMConcreteContainerIdentity containerIdentityWithUUID:userIdentity:identifier:containerConfig:platform:posixOwnership:userIdentityCache:error:]"
+ "+[MCMContainerIdentity containerIdentityWithIdentifier:containerConfig:platform:posixOwnership:userIdentityCache:error:]"
+ "+[MCMContainerIdentity containerIdentityWithUserIdentity:identifier:containerConfig:platform:posixOwnership:transient:userIdentityCache:error:]"
+ "+[MCMContainerIdentity containerIdentityWithUserIdentity:identifier:containerConfig:platform:posixOwnership:userIdentityCache:error:]"
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
+ "Could not delete corrupt container; path = %@, error = %@"
+ "Could not generate posix user details for user=[%@]"
+ "Could not read the child/parent map, starting empty; error = %@"
+ "Created new POSIX user: [%@]"
+ "DELETED: [%@] (corrupt container)"
+ "DELETED: [%@] (mismatched instance UUID); existing = [%@], requested = [%@]"
+ "Default POSIX owner is invalid; owner = %@, error = %@"
+ "Failed reading metadata during claim; container = %@; error = %@"
+ "Failed to add surviving container to cache for supersede; metadata = %s, error = %s"
+ "Failed to build successor container identity; error = (%llu) %s"
+ "Failed to decode successor container; error = (%llu) %s"
+ "Failed to delete superseded container for supersede; path = 🔒%{private}s, error = %s"
+ "Failed to derive new metadata for supersede; successor = %s"
+ "Failed to get xattr instance uuid; error = %@"
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
+ "MobileContainerManager-833.40.14~46"
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
- "MobileContainerManager-833.0.8.0.1~200"
- "Unable to get user (%u/[%@]); error = %{public}s"
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
