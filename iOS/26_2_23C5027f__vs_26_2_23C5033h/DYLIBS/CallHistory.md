## CallHistory

> `/System/Library/PrivateFrameworks/CallHistory.framework/CallHistory`

```diff

-106.300.18.0.0
-  __TEXT.__text: 0x19e468
-  __TEXT.__auth_stubs: 0x2430
-  __TEXT.__objc_methlist: 0x38a4
-  __TEXT.__const: 0x1de74
-  __TEXT.__cstring: 0x4dc4
-  __TEXT.__oslogstring: 0x59f9
-  __TEXT.__gcc_except_tab: 0x834
+106.300.23.2.3
+  __TEXT.__text: 0x1a05c0
+  __TEXT.__auth_stubs: 0x2450
+  __TEXT.__objc_methlist: 0x3994
+  __TEXT.__const: 0x1e034
+  __TEXT.__cstring: 0x4e44
+  __TEXT.__oslogstring: 0x5d09
+  __TEXT.__gcc_except_tab: 0x888
   __TEXT.__dlopen_cstrs: 0x147
   __TEXT.__swift5_typeref: 0x516f
-  __TEXT.__swift5_reflstr: 0x68a0
+  __TEXT.__swift5_reflstr: 0x6940
   __TEXT.__swift5_assocty: 0x1b98
-  __TEXT.__swift5_fieldmd: 0x55ac
-  __TEXT.__constg_swiftt: 0x1122c
+  __TEXT.__swift5_fieldmd: 0x560c
+  __TEXT.__constg_swiftt: 0x1134c
   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_proto: 0xdec

   __TEXT.__swift_as_ret: 0xc8
   __TEXT.__swift5_capture: 0x334
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x6518
-  __TEXT.__eh_frame: 0x7840
-  __TEXT.__objc_classname: 0x65d
-  __TEXT.__objc_methname: 0x979e
-  __TEXT.__objc_methtype: 0x1255
-  __TEXT.__objc_stubs: 0x7600
+  __TEXT.__unwind_info: 0x6588
+  __TEXT.__eh_frame: 0x78a0
+  __TEXT.__objc_classname: 0x6b4
+  __TEXT.__objc_methname: 0x99ea
+  __TEXT.__objc_methtype: 0x12c3
+  __TEXT.__objc_stubs: 0x7760
   __DATA_CONST.__got: 0x978
-  __DATA_CONST.__const: 0x1300
-  __DATA_CONST.__objc_classlist: 0x458
+  __DATA_CONST.__const: 0x1330
+  __DATA_CONST.__objc_classlist: 0x460
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0xd0
+  __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2448
+  __DATA_CONST.__objc_selrefs: 0x2490
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x138
-  __AUTH_CONST.__auth_got: 0x1228
-  __AUTH_CONST.__const: 0x4c48
+  __DATA_CONST.__objc_superrefs: 0x140
+  __AUTH_CONST.__auth_got: 0x1238
+  __AUTH_CONST.__const: 0x4ca8
   __AUTH_CONST.__cfstring: 0x2f20
-  __AUTH_CONST.__objc_const: 0x14438
+  __AUTH_CONST.__objc_const: 0x14d10
   __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH.__objc_data: 0x1be0
-  __AUTH.__data: 0x14d18
-  __DATA.__objc_ivar: 0x2b0
-  __DATA.__data: 0x4820
-  __DATA.__bss: 0x1e3a0
+  __AUTH.__objc_data: 0x1c30
+  __AUTH.__data: 0x14e70
+  __DATA.__objc_ivar: 0x2c0
+  __DATA.__data: 0x48e8
+  __DATA.__bss: 0x1e3f0
   __DATA.__common: 0x128
   __DATA_DIRTY.__objc_data: 0xe10
   __DATA_DIRTY.__bss: 0xe0

   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EFD8AB43-FF35-35AA-8BB1-967069BAEF5D
-  Functions: 12178
-  Symbols:   7661
-  CStrings:  3326
+  UUID: 52D43279-6C13-3564-8A90-445AB6AA5609
+  Functions: 12251
+  Symbols:   7762
+  CStrings:  3366
 
Symbols:
+ -[CHDatabaseLocationProvider init]
+ -[CHDatabaseLocationProvider permanentDatabaseLocationWithError:]
+ -[CHDatabaseLocationProvider temporaryDatabaseLocationWithError:]
+ -[CallDBManagerClient createPermanent].cold.4
+ -[CallDBManagerClient createPermanent].cold.5
+ -[CallDBManagerClient createTemporary].cold.3
+ -[CallDBManagerClient createTemporary].cold.4
+ -[CallDBManagerClient createTemporary].cold.5
+ -[CallDBManagerClient databaseLocationProvider]
+ -[CallDBManagerClient handleTemporaryCreated]
+ -[CallDBManagerClient initWithProcessHandle:metaInfoProvider:]
+ -[CallDBManagerClient initWithProcessHandle:metaInfoProvider:databaseLocationProvider:]
+ -[CallDBManagerClient init]
+ -[CallDBManagerClient interruptionRetryCount]
+ -[CallDBManagerClient metaInfoProvider]
+ -[CallDBManagerClient setInterruptionRetryCount:]
+ -[CallDBManagerClient validatePermDatabase].cold.1
+ -[CallDBManagerClient validateTempDatabase].cold.1
+ -[CallDBManagerServer bootUpDBAtLocation:isEncrypted:isTemporary:]
+ -[CallDBManagerServer bootUpDBAtLocation:isEncrypted:isTemporary:].cold.1
+ -[CallDBManagerServer bootUpDBAtLocation:isEncrypted:isTemporary:].cold.2
+ -[CallDBManagerServer bootUpDBAtLocation:isEncrypted:isTemporary:].cold.3
+ -[CallDBManagerServer bootUpDBAtLocation:isEncrypted:isTemporary:].cold.4
+ -[CallDBManagerServer bootUpDBAtLocationWithRecovery:isEncrypted:isTemporary:]
+ -[CallDBManagerServer bootUpDBAtLocationWithRecovery:isEncrypted:isTemporary:].cold.1
+ -[CallDBManagerServer bootUpDBAtLocationWithRecovery:isEncrypted:isTemporary:].cold.2
+ -[CallDBManagerServer createPermanent].cold.1
+ -[CallDBManagerServer createPermanent].cold.2
+ -[CallDBManagerServer createTemporary].cold.1
+ -[CallDBManagerServer createTemporary].cold.2
+ -[CallDBManagerServer handleBootUpFailure:isTemporary:]
+ -[CallDBManagerServer handleBootUpFailure:isTemporary:].cold.1
+ -[CallDBManagerServer initWithDeviceObserver:metaInfoProvider:]
+ -[CallDBManagerServer metaInfoProvider]
+ GCC_except_table17
+ _OBJC_CLASS_$_CHDatabaseLocationProvider
+ _OBJC_IVAR_$_CallDBManagerClient._databaseLocationProvider
+ _OBJC_IVAR_$_CallDBManagerClient._interruptionRetryCount
+ _OBJC_IVAR_$_CallDBManagerClient._metaInfoProvider
+ _OBJC_IVAR_$_CallDBManagerServer._metaInfoProvider
+ _OBJC_METACLASS_$_CHDatabaseLocationProvider
+ __OBJC_$_INSTANCE_METHODS_CHDatabaseLocationProvider
+ __OBJC_$_PROP_LIST_CHDatabaseLocationProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CHDatabaseLocationProviderProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CallDBMetaInfoProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CHDatabaseLocationProviderProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CallDBMetaInfoProtocol
+ __OBJC_$_PROTOCOL_REFS_CHDatabaseLocationProviderProtocol
+ __OBJC_$_PROTOCOL_REFS_CallDBMetaInfoProtocol
+ __OBJC_CLASS_PROTOCOLS_$_CHDatabaseLocationProvider
+ __OBJC_CLASS_PROTOCOLS_$_CallDBMetaInfo
+ __OBJC_CLASS_RO_$_CHDatabaseLocationProvider
+ __OBJC_LABEL_PROTOCOL_$_CHDatabaseLocationProviderProtocol
+ __OBJC_LABEL_PROTOCOL_$_CallDBMetaInfoProtocol
+ __OBJC_METACLASS_RO_$_CHDatabaseLocationProvider
+ __OBJC_PROTOCOL_$_CHDatabaseLocationProviderProtocol
+ __OBJC_PROTOCOL_$_CallDBMetaInfoProtocol
+ ___45-[CallDBManagerClient createHelperConnection]_block_invoke.70
+ ___45-[CallDBManagerClient createHelperConnection]_block_invoke.70.cold.1
+ ___45-[CallDBManagerClient createHelperConnection]_block_invoke.cold.3
+ ___45-[CallDBManagerClient initWithProcessHandle:]_block_invoke
+ ___46-[CallDBManagerServer initWithDeviceObserver:]_block_invoke
+ ___87-[CallDBManagerClient initWithProcessHandle:metaInfoProvider:databaseLocationProvider:]_block_invoke
+ ___block_descriptor_32_e41_"<CallDBMetaInfoProtocol>"16?0"NSURL"8l
+ ___block_literal_global.4
+ ___block_literal_global.42
+ ___block_literal_global.48
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_CallHistory
+ __swift_FORCE_LOAD_$_swiftIntents
+ __swift_FORCE_LOAD_$_swiftIntents_$_CallHistory
+ _objc_msgSend$bootUpDBAtLocation:isEncrypted:isTemporary:
+ _objc_msgSend$bootUpDBAtLocationWithRecovery:isEncrypted:isTemporary:
+ _objc_msgSend$databaseLocationProvider
+ _objc_msgSend$handleBootUpFailure:isTemporary:
+ _objc_msgSend$initWithDeviceObserver:metaInfoProvider:
+ _objc_msgSend$initWithProcessHandle:
+ _objc_msgSend$initWithProcessHandle:metaInfoProvider:
+ _objc_msgSend$initWithProcessHandle:metaInfoProvider:databaseLocationProvider:
+ _objc_msgSend$interruptionRetryCount
+ _objc_msgSend$metaInfoProvider
+ _objc_msgSend$permanentDatabaseLocationWithError:
+ _objc_msgSend$setInterruptionRetryCount:
+ _objc_msgSend$temporaryDatabaseLocationWithError:
+ _objc_msgSend$validateTempDatabase
- -[CallDBManagerClient setCurrentProcessHandle:]
- -[CallDBManagerServer bootUpDBAtLocation:isEncrypted:]
- -[CallDBManagerServer bootUpDBAtLocation:isEncrypted:].cold.1
- -[CallDBManagerServer bootUpDBAtLocation:isEncrypted:].cold.2
- -[CallDBManagerServer bootUpDBAtLocation:isEncrypted:].cold.3
- -[CallDBManagerServer bootUpDBAtLocation:isEncrypted:].cold.4
- -[CallDBManagerServer bootUpDBAtLocationWithRecovery:isEncrypted:]
- -[CallDBManagerServer bootUpDBAtLocationWithRecovery:isEncrypted:].cold.1
- -[CallDBManagerServer bootUpDBAtLocationWithRecovery:isEncrypted:].cold.2
- -[CallDBManagerServer handleBootUpFailure:]
- GCC_except_table12
- ___45-[CallDBManagerClient createHelperConnection]_block_invoke.64
- ___45-[CallDBManagerClient createHelperConnection]_block_invoke.64.cold.1
- ___45-[CallDBManagerClient pokeSyncHelperToInitDB]_block_invoke.cold.1
- ___45-[CallDBManagerClient pokeSyncHelperToInitDB]_block_invoke.cold.2
- ___block_literal_global.45
- _objc_msgSend$bootUpDBAtLocation:isEncrypted:
- _objc_msgSend$bootUpDBAtLocationWithRecovery:isEncrypted:
- _objc_msgSend$handleBootUpFailure:
CStrings:
+ "106.300.23.2.3"
+ "106.300.23.2.3~7"
+ "@\"<CHDatabaseLocationProviderProtocol>\""
+ "@\"<CallDBMetaInfoProtocol>\"16@?0@\"NSURL\"8"
+ "@\"NSURL\"24@0:8^C16"
+ "@24@0:8@\"NSURL\"16"
+ "@32@0:8@16@?24"
+ "@40@0:8@16@?24@32"
+ "Attempting to reconnect to the SyncHelper (retry %lu/%lu)"
+ "B28@0:8q16B24"
+ "CHDatabaseLocationProvider"
+ "CHDatabaseLocationProviderProtocol"
+ "CallDBMetaInfoProtocol"
+ "Database already initialized (perm:%d temp:%d), skipping recovery"
+ "Failed to add permanent data store at location: %{public}@ after successful validation"
+ "Failed to add temporary data store at location: %{public}@ after successful validation"
+ "Failed to clear database version after failed permanent store creation"
+ "Failed to clear database version after failed temporary store creation"
+ "Failed to clear database version metadata after deletion"
+ "Failed to write database version metadata for permanent store"
+ "Failed to write database version metadata for temporary store"
+ "Maximum interruption retry count (%lu) reached, giving up"
+ "Permanent database file does not exist at path: %{public}@"
+ "Permanent database metadata valid but data store check failed with code: %{public}@; poking sync helper"
+ "Permanent database validated successfully"
+ "Permanent database validation failed, poking sync helper"
+ "T@\"<CHDatabaseLocationProviderProtocol>\",R,N,V_databaseLocationProvider"
+ "T@\"CHProcessHandle\",R,N,V_currentProcessHandle"
+ "T@?,R,N,V_metaInfoProvider"
+ "TQ,V_interruptionRetryCount"
+ "Temporary database file does not exist at path: %{public}@"
+ "Temporary database file doesn't exist; poking sync helper. Error code: %{public}@"
+ "Temporary database metadata valid but data store check failed with code: %{public}@; poking sync helper"
+ "Temporary database validated successfully"
+ "Temporary database validation failed; poking sync helper"
+ "_databaseLocationProvider"
+ "_interruptionRetryCount"
+ "_metaInfoProvider"
+ "_neededSCAnnouncement"
+ "bootUpDBAtLocation:isEncrypted:isTemporary:"
+ "bootUpDBAtLocationWithRecovery:isEncrypted:isTemporary:"
+ "createTemporary client"
+ "createTemporary client location: %{public}@"
+ "databaseLocationProvider"
+ "handleBootUpFailure:isTemporary:"
+ "initWithDeviceObserver:metaInfoProvider:"
+ "initWithProcessHandle:metaInfoProvider:"
+ "initWithProcessHandle:metaInfoProvider:databaseLocationProvider:"
+ "interruptionRetryCount"
+ "metaInfoProvider"
+ "neededSCAnnouncement"
+ "permanentDatabaseLocationWithError:"
+ "setInterruptionRetryCount:"
+ "temporaryDatabaseLocationWithError:"
- "106.300.18"
- "106.300.18~130"
- "Attempting to reconnect to the SyncHelper"
- "MetaInfo says permanent database should be initialized but looks like not"
- "MetaInfo says temporary database should be initialized but looks like not"
- "Permanent database state in client is out of sync with the server."
- "Permanent database version: %ld is not the same as current version: %ld"
- "Permanent database version: %ld is the same as  current version: %ld"
- "Temporary database state in client is out of sync with the server."
- "Temporary database version: %ld is not the same as current version: %ld"
- "bootUpDBAtLocation:isEncrypted:"
- "bootUpDBAtLocationWithRecovery:isEncrypted:"
- "createTemporary client: %{public}@"
- "handleBootUpFailure:"
- "v28@0:8q16B24"

```
