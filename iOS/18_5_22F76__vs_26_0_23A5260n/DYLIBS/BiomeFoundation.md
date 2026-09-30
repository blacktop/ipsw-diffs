## BiomeFoundation

> `/System/Library/PrivateFrameworks/BiomeFoundation.framework/BiomeFoundation`

```diff

-166.23.1.0.0
-  __TEXT.__text: 0x35b00
-  __TEXT.__auth_stubs: 0xdd0
-  __TEXT.__objc_methlist: 0x2934
-  __TEXT.__const: 0x22a
-  __TEXT.__cstring: 0x4f36
-  __TEXT.__oslogstring: 0x3362
-  __TEXT.__gcc_except_tab: 0xdf4
+192.0.0.0.0
+  __TEXT.__text: 0x36f7c
+  __TEXT.__auth_stubs: 0xdc0
+  __TEXT.__objc_methlist: 0x29a4
+  __TEXT.__const: 0x25a
+  __TEXT.__cstring: 0x4f56
+  __TEXT.__oslogstring: 0x3582
+  __TEXT.__gcc_except_tab: 0xdd0
   __TEXT.__dlopen_cstrs: 0x2d4
   __TEXT.__constg_swiftt: 0x64
   __TEXT.__swift5_typeref: 0x21
   __TEXT.__swift5_reflstr: 0x2f
   __TEXT.__swift5_fieldmd: 0x44
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xda0
-  __TEXT.__objc_classname: 0x658
-  __TEXT.__objc_methname: 0x5841
-  __TEXT.__objc_methtype: 0x10c2
-  __TEXT.__objc_stubs: 0x4840
+  __TEXT.__unwind_info: 0xdf0
+  __TEXT.__objc_classname: 0x669
+  __TEXT.__objc_methname: 0x59dc
+  __TEXT.__objc_methtype: 0x10d9
+  __TEXT.__objc_stubs: 0x4880
   __DATA_CONST.__got: 0x380
-  __DATA_CONST.__const: 0xcc8
-  __DATA_CONST.__objc_classlist: 0x1c0
+  __DATA_CONST.__const: 0xca0
+  __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x17e8
+  __DATA_CONST.__objc_selrefs: 0x1810
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x12f8
-  __AUTH_CONST.__auth_got: 0x6f8
-  __AUTH_CONST.__const: 0x4c0
-  __AUTH_CONST.__cfstring: 0x5740
-  __AUTH_CONST.__objc_const: 0x6768
+  __AUTH_CONST.__auth_got: 0x6f0
+  __AUTH_CONST.__const: 0x480
+  __AUTH_CONST.__cfstring: 0x5680
+  __AUTH_CONST.__objc_const: 0x6890
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x230
-  __AUTH.__objc_data: 0x4d0
+  __AUTH.__objc_data: 0x3e0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x280
+  __DATA.__objc_ivar: 0x290
   __DATA.__data: 0x5b8
-  __DATA.__bss: 0x168
+  __DATA.__bss: 0x138
   __DATA.__common: 0x8
-  __DATA_DIRTY.__objc_data: 0xd20
-  __DATA_DIRTY.__data: 0x1b0
-  __DATA_DIRTY.__bss: 0x150
+  __DATA_DIRTY.__objc_data: 0xe60
+  __DATA_DIRTY.__data: 0x198
+  __DATA_DIRTY.__bss: 0x168
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /usr/lib/swift/libswiftObjectiveC.dylib
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
-  UUID: 586E1676-1CE8-3401-9F46-4E2AC21A00C3
-  Functions: 1201
-  Symbols:   4503
-  CStrings:  3013
+  UUID: 7EC26970-0D08-3870-983C-425C141AA88D
+  Functions: 1213
+  Symbols:   4506
+  CStrings:  3027
 
Symbols:
+ +[BMAccessControlPolicy(LegacyViewEntitlement) setLegacyStreamNameMappingCallback:]
+ +[BMAccessControlPolicy(LegacyViewEntitlement) setUUIDStreamNameMappingCallback:]
+ +[BMStoreDirectory(BiomeInternalOnly) pendingBatches]
+ +[BMXPCConnectionFactory connectionToAccessServerInDomain:user:useCase:options:]
+ +[BMXPCConnectionFactory connectionToComputeSourceServerInDomain:user:useCase:options:]
+ +[BMXPCConnectionFactory connectionToFileServerInDomain:user:useCase:options:]
+ -[BMCurrentDevice canOpenFilesForProtectionClass:]
+ -[BMCurrentDevice setCanOpen:filesForProtectionClass:]
+ -[BMFileBackedCounter _createFileDictionary:]
+ -[BMFileBackedCounter _createFileDictionary:].cold.1
+ -[BMFileBackedCounter initWithFilename:protectionClass:directory:domain:readOnly:error:]
+ -[BMProcessCurrent allowedToHaveDatavaultEntitlement]
+ -[BMProcessCurrent enforceDatavaultEntitlementRestrictions]
+ -[BMViewResourceMapper setStreamIdentifierForLegacyStreamName:]
+ -[BMViewResourceMapper setStreamIdentifierForUUIDString:]
+ -[BMViewResourceMapper streamIdentifierForLegacyStreamName]
+ -[BMViewResourceMapper streamIdentifierForUUIDString]
+ -[BMXPCConnectionFactory initWithType:domain:user:useCase:options:]
+ -[_BMXPCConnection serviceName]
+ GCC_except_table12
+ GCC_except_table24
+ GCC_except_table47
+ GCC_except_table48
+ GCC_except_table59
+ _NSFileProtectionCompleteWhenUserInactive
+ _OBJC_CLASS_$_BMCurrentDevice
+ _OBJC_IVAR_$_BMFileBackedCounter._readOnly
+ _OBJC_IVAR_$_BMViewResourceMapper._streamIdentifierForLegacyStreamName
+ _OBJC_IVAR_$_BMViewResourceMapper._streamIdentifierForUUIDString
+ _OBJC_IVAR_$_BMXPCConnectionFactory._options
+ _OBJC_METACLASS_$_BMCurrentDevice
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __OBJC_$_INSTANCE_METHODS_BMCurrentDevice
+ __OBJC_$_PROP_LIST__BMXPCConnection
+ __OBJC_CLASS_RO_$_BMCurrentDevice
+ __OBJC_METACLASS_RO_$_BMCurrentDevice
+ ___59-[BMProcessCurrent enforceDatavaultEntitlementRestrictions]_block_invoke
+ ___59-[BMProcessCurrent enforceDatavaultEntitlementRestrictions]_block_invoke.cold.1
+ ___BMResourcesAndAccessModesListedUnderEntitlement_block_invoke.321
+ ___BMResourcesAndAccessModesListedUnderEntitlement_block_invoke_2.322
+ ___BMResourcesAndAccessModesListedUnderEntitlement_block_invoke_3.323
+ ___block_literal_global.218
+ ___block_literal_global.255
+ ___block_literal_global.267
+ __bm_fd_supports_content_protection
+ __bm_openat_dprotected.cold.3
+ __os_crash
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_BiomeFoundation
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_BiomeFoundation
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_BiomeFoundation
+ _bm_new_temporary_file.cold.7
+ _bm_openat_dprotected.cold.5
+ _bm_openat_dprotected.cold.6
+ _bm_opendirat.cold.9
+ _bm_replace_file.cold.18
+ _enforceDatavaultEntitlementRestrictions.onceToken
+ _objc_msgSend$_createFileDictionary:
+ _objc_msgSend$allowedToHaveDatavaultEntitlement
+ _objc_msgSend$canOpenFilesForProtectionClass:
+ _objc_msgSend$connectionToAccessServerInDomain:user:useCase:options:
+ _objc_msgSend$connectionToFileServerInDomain:user:useCase:options:
+ _objc_msgSend$deviceLockState
+ _objc_msgSend$enforceDatavaultEntitlementRestrictions
+ _objc_msgSend$hasDatavaultEntitlement
+ _objc_msgSend$initWithType:domain:user:useCase:options:
+ _objc_msgSend$isDeviceUnlocked
+ _objc_msgSend$setStreamIdentifierForLegacyStreamName:
+ _objc_msgSend$setStreamIdentifierForUUIDString:
+ _objc_msgSend$streamIdentifierForLegacyStreamName
+ _objc_msgSend$streamIdentifierForUUIDString
+ _objc_unsafeClaimAutoreleasedReturnValue
- +[BMPaths localFlexibleStorageDirectory]
- +[BMStoreDirectory(BiomeInternalOnly) flexibleStorage]
- +[BMXPCConnectionFactory connectionToAccessServerInDomain:user:useCase:]
- +[BMXPCConnectionFactory connectionToComputeSourceServerInDomain:user:useCase:]
- +[BMXPCConnectionFactory connectionToFileServerInDomain:user:useCase:]
- -[BMAccessControlPolicy allowsAccessToFlexibleStorage]
- -[BMAccessControlPolicy allowsAccessToStream:withMode:].cold.1
- -[BMAccessControlPolicy allowsAccessToStream:withMode:].cold.2
- -[BMAccessControlPolicy allowsConnectionToAccessServiceWithDomain:].cold.3
- -[BMFileBackedCounter _createFileIfNotExists:]
- -[BMFileBackedCounter _createFileIfNotExists:].cold.1
- -[BMFileBackedCounter initWithFilename:protectionClass:directory:domain:error:]
- -[BMProcessCurrent reliesOnDirectAccessForDomain:].cold.1
- -[BMProcessCurrent reliesOnDirectAccessForDomain:].cold.2
- -[BMXPCConnectionFactory initWithType:domain:user:useCase:]
- GCC_except_table44
- GCC_except_table45
- GCC_except_table54
- _BMBiomeLibraryIdentifierForLegacyName.mapping
- _BMBiomeLibraryIdentifierForLegacyName.onceToken
- _BMBiomeLibraryIdentifierForUUIDString.mapping
- _BMBiomeLibraryIdentifierForUUIDString.onceToken
- _BMFlexibleStorageResource
- _OBJC_CLASS_$_NSException
- ___BMBiomeLibraryIdentifierForLegacyName_block_invoke
- ___BMBiomeLibraryIdentifierForUUIDString_block_invoke
- ___BMNormalizedResourcesAndAccessModesListedUnderEntitlement_block_invoke.cold.3
- ___BMNormalizedResourcesAndAccessModesListedUnderEntitlement_block_invoke.cold.4
- ___BMResourcesAndAccessModesListedUnderEntitlement_block_invoke.320
- ___BMResourcesAndAccessModesListedUnderEntitlement_block_invoke_2.321
- ___BMResourcesAndAccessModesListedUnderEntitlement_block_invoke_3.322
- ___block_literal_global.224
- ___block_literal_global.254
- ___block_literal_global.266
- ___block_literal_global.324
- ___block_literal_global.332
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_errno_$_BiomeFoundation
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_math_$_BiomeFoundation
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_signal_$_BiomeFoundation
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_stdio_$_BiomeFoundation
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swift_time_$_BiomeFoundation
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftsys_time_$_BiomeFoundation
- __swift_FORCE_LOAD_$_swiftunistd
- __swift_FORCE_LOAD_$_swiftunistd_$_BiomeFoundation
- _dup
- _objc_exception_throw
- _objc_msgSend$_createFileIfNotExists:
- _objc_msgSend$allStreams
- _objc_msgSend$allowsAccessToFlexibleStorage
- _objc_msgSend$connectionToAccessServerInDomain:user:useCase:
- _objc_msgSend$connectionToFileServerInDomain:user:useCase:
- _objc_msgSend$dictionaryWithDictionary:
- _objc_msgSend$exceptionWithName:reason:userInfo:
- _objc_msgSend$flexibleStorage
- _objc_msgSend$initWithType:domain:user:useCase:
- _objc_msgSend$isUnlocked
- _objc_msgSend$localFlexibleStorageDirectory
- _objc_msgSend$lockState
- _swift_bridgeObjectRetain
CStrings:
+ " "
+ " %@"
+ " %@%@lockState:%d expired:%d"
+ "/Library/Caches/com.apple.xbs/Sources/Biome/BiomeFoundation/BiomeFoundation/Filesystem/BMFilesystem.m"
+ "@40@0:8Q16I24@28C36"
+ "@48@0:8Q16Q24I32@36C44"
+ "@56@0:8@16i24@28Q36B44^@48"
+ "BMCurrentDevice"
+ "FATAL ERROR IN CLIENT: Use of `com.apple.private.security.storage.Biome` not allowed"
+ "F_GETPATH"
+ "F_GETPROTECTIONCLASS"
+ "F_SETPROTECTIONCLASS"
+ "T@?,C,V_streamIdentifierForLegacyStreamName"
+ "T@?,C,V_streamIdentifierForUUIDString"
+ "_createFileDictionary:"
+ "_readOnly"
+ "_streamIdentifierForLegacyStreamName"
+ "_streamIdentifierForUUIDString"
+ "a"
+ "allowedToHaveDatavaultEntitlement"
+ "cannot increment read-only %@ instance (path: %@)"
+ "close(%d) -> %d, %{darwin.errno}d (%s:%d)"
+ "connectionToAccessServerInDomain:user:useCase:options:"
+ "connectionToComputeSourceServerInDomain:user:useCase:options:"
+ "connectionToFileServerInDomain:user:useCase:options:"
+ "deviceLockState"
+ "enforceDatavaultEntitlementRestrictions"
+ "fclonefileat(%d, %d, \"%s\", ...) -> %d, %{darwin.errno}d (%s:%d)\n"
+ "fcntl(%d, %s, ...) -> %d, %{darwin.errno}d (%s:%d)\n"
+ "fcntl(F_DUPFD_CLOEXEC) failed: %{darwin.errno}d"
+ "fcntl(F_DUPFD_CLOEXEC): %s: %d"
+ "fcopyfile(%d, %d, ...) -> %d, %{darwin.errno}d (%s:%d)\n"
+ "fstat(%d, ...) -> %d, %{darwin.errno}d (%s:%d)\n"
+ "fstatfs(%d, ...) -> %d, %{darwin.errno}d (%s:%d)\n"
+ "initWithFilename:protectionClass:directory:domain:readOnly:error:"
+ "initWithType:domain:user:useCase:options:"
+ "isDeviceUnlocked"
+ "lseek(%d, ...) -> %lld, %{darwin.errno}d (%s:%d)\n"
+ "mkdirat(%d, \"%s\", ...) -> %d, %{darwin.errno}d (%s:%d)\n"
+ "mkostempsat_np(%d, \"%s\", ...) -> %d, %{darwin.errno}d (%s:%d)\n"
+ "mktemp(%s) -> %d, %{darwin.errno}d (%s:%d)\n"
+ "openat(%d, \"%s\", 0x%x, ...) -> %d, %{darwin.errno}d (%s:%d)\n"
+ "openat_dprotected_np(%d, \"%s\", ...) -> %d, %{darwin.errno}d (%s:%d)\n"
+ "pendingBatches"
+ "renameat(%d, \"%s\", %d, \"%s\") -> %d, %{darwin.errno}d (%s:%d)\n"
+ "serviceName"
+ "setCanOpen:filesForProtectionClass:"
+ "setLegacyStreamNameMappingCallback:"
+ "setStreamIdentifierForLegacyStreamName:"
+ "setStreamIdentifierForUUIDString:"
+ "setUUIDStreamNameMappingCallback:"
+ "streamIdentifierForLegacyStreamName"
+ "streamIdentifierForUUIDString"
+ "unlinkat(%d, \"%s\", ...) -> %d, %{darwin.errno}d (%s:%d)\n"
+ "v28@0:8B16Q20"
- " locked:%d"
- "@36@0:8Q16I24@28"
- "@44@0:8Q16Q24I32@36"
- "@52@0:8@16i24@28Q36^@44"
- "BMAccessClient.requestAccessToResource: BFS"
- "BMFlexibleStorageResource"
- "BiomeFlexibleStorage"
- "BiomeSecurityException"
- "Client Error: root/system processes cannot access Biome using datavault entitlement"
- "Discoverability.Signals"
- "FlexibleStorage"
- "Use of `com.apple.private.security.storage.Biome` not allowed"
- "Utilizing temporary exception to allow %@ access to Biome"
- "Utilizing temporary exception to allow %{public}@ access to %{public}@"
- "_createFileIfNotExists:"
- "allStreams"
- "allowsAccessToFlexibleStorage"
- "com.apple.activitysharingd"
- "com.apple.camera"
- "configuration.legacyNames"
- "configuration.streamIdentifier"
- "configuration.streamUUID.UUIDString"
- "connectionToAccessServerInDomain:user:useCase:"
- "connectionToComputeSourceServerInDomain:user:useCase:"
- "connectionToFileServerInDomain:user:useCase:"
- "dictionaryWithDictionary:"
- "dup() failed: %{darwin.errno}d"
- "dup(): %s: %d"
- "exceptionWithName:reason:userInfo:"
- "flexibleStorage"
- "initWithFilename:protectionClass:directory:domain:error:"
- "initWithType:domain:user:useCase:"
- "isUnlocked"
- "localFlexibleStorageDirectory"
- "lockState"

```
