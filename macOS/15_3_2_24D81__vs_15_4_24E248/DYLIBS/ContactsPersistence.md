## ContactsPersistence

> `/System/Library/PrivateFrameworks/ContactsPersistence.framework/Versions/A/ContactsPersistence`

```diff

-3770.400.11.0.0
-  __TEXT.__text: 0x53e20
-  __TEXT.__auth_stubs: 0xf70
-  __TEXT.__objc_methlist: 0x4bc4
+3770.500.41.0.0
+  __TEXT.__text: 0x533ac
+  __TEXT.__auth_stubs: 0xf40
+  __TEXT.__objc_methlist: 0x529c
   __TEXT.__const: 0xa2c
-  __TEXT.__cstring: 0x386f
+  __TEXT.__cstring: 0x359f
   __TEXT.__oslogstring: 0x349a
   __TEXT.__gcc_except_tab: 0x778
   __TEXT.__constg_swiftt: 0x820

   __TEXT.__swift5_types: 0x50
   __TEXT.__swift5_capture: 0x70
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x1658
-  __TEXT.__eh_frame: 0x390
+  __TEXT.__unwind_info: 0x16b0
+  __TEXT.__eh_frame: 0x2c8
   __TEXT.__objc_classname: 0x109d
   __TEXT.__objc_methname: 0xc86c
   __TEXT.__objc_methtype: 0x153d
   __TEXT.__objc_stubs: 0x9680
   __DATA_CONST.__got: 0x870
-  __DATA_CONST.__const: 0x1048
+  __DATA_CONST.__const: 0x1058
   __DATA_CONST.__objc_classlist: 0x4d0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x30e0
+  __DATA_CONST.__objc_selrefs: 0x31f8
   __DATA_CONST.__objc_protorefs: 0x58
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x88
-  __AUTH_CONST.__auth_got: 0x7c8
+  __AUTH_CONST.__auth_got: 0x7b0
   __AUTH_CONST.__const: 0x1e08
   __AUTH_CONST.__cfstring: 0x3f60
-  __AUTH_CONST.__objc_const: 0xc118
+  __AUTH_CONST.__objc_const: 0xb4f8
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0xa8
-  __AUTH.__objc_data: 0x1818
+  __AUTH.__objc_data: 0x17f8
   __AUTH.__data: 0x490
   __DATA.__objc_ivar: 0x408
-  __DATA.__data: 0xe88
+  __DATA.__data: 0xe78
   __DATA.__bss: 0xf70
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x1ef0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 878A8AB3-A36D-32C0-B7E7-47E37E42BCE1
-  Functions: 2222
-  Symbols:   5800
-  CStrings:  3945
+  UUID: 0DBBD010-13FF-3B9F-AC80-12E82DA9C676
+  Functions: 2270
+  Symbols:   5849
+  CStrings:  3928
 
Symbols:
+ +[ABCDContainer makeDefaultContainerPermissions].cold.1
+ +[ABCDCustomProperty os_log].cold.1
+ +[ABCDCustomProperty recordTypePredicateTemplate].cold.1
+ +[ABCDDateUtils calendarWithOffsetFromGMT:].cold.1
+ +[ABCDDateUtils gregorianCalendar].cold.1
+ +[ABCDDistributionListConfig distributionListConfigWithProperty:personIdentifier:groupIdentifier:inContext:].cold.1
+ +[ABCDPlatform isTimeMachineURL:].cold.1
+ +[ABCDSocialProfile privateKeysForPublicKeys].cold.1
+ +[CNAccountCollectionUpdateWatcher os_log].cold.1
+ +[CNCDCardDAVLegacyCustomPropertyMigrator os_log].cold.1
+ +[CNCDChangeHistoryClient os_log].cold.1
+ +[CNCDContact os_log].cold.1
+ +[CNCDContact preferredNameSortDescriptors].cold.1
+ +[CNCDContact preferredPhotoSortDescriptors].cold.1
+ +[CNCDContactIndexMigrator log].cold.1
+ +[CNCDDatabasePreparation os_log].cold.1
+ +[CNCDDatabaseRemoval os_log].cold.1
+ +[CNCDDuplicateCustomPropertyMigrator os_log].cold.1
+ +[CNCDDuplicateInfoCleanupMigrator os_log].cold.1
+ +[CNCDIOSLegacyIdentifierRegistrarOnDiskPropertyListPersistence log].cold.1
+ +[CNCDIOSLegacyIdentifierXPCRegistrar log].cold.1
+ +[CNCDNote accessViolationReporter].cold.1
+ +[CNCDOrphanRecordMigrator os_log].cold.1
+ +[CNCDPersistenceContext log].cold.1
+ +[CNCDPersistenceStack defaultAccountCollection].cold.1
+ +[CNCDPersistenceStack os_log_t].cold.1
+ +[CNCDPersistentBackend os_log].cold.1
+ +[CNCDPhoneNumberMigrator log].cold.1
+ +[CNCDRecord _newUniqueIdForTable:].cold.2
+ +[CNCDRecord fetchObjectForClass:withUniqueId:managedObjectContext:affectedStores:].cold.1
+ +[CNCDRecord initialize].cold.1
+ +[CNCDRecord os_log].cold.1
+ +[CNCDRemotePersistence os_log].cold.1
+ +[CNCDRemotePersistence shouldCurrentProcessUseRemotePersistenceImpl].cold.8
+ +[CNCustomPropertyMigrationTask os_log].cold.1
+ +[CNPersistentStoreBuilder migration_os_log].cold.1
+ +[CNPersistentStoreBuilder os_log].cold.1
+ +[CNPersistentStoreCoordinatorCache log].cold.1
+ +[CNTempFileHelper temporaryDatabaseUrlByCopyingDatabaseAtPath:withCoordinator:error:].cold.8
+ -[ACAccount(CNAccountDescription) _interestedAccountTypeIdentifiers].cold.1
+ -[ACAccount(CNAccountDescription) isPersistent].cold.1
+ -[CNCDDatabasePreflightTask initWithURL:options:].cold.2
+ -[CNCDDatabasePreparationRequest initWithURL:readOnly:registrar:].cold.2
+ -[CNCDDatabasePreparationResult initWithURL:options:pristineDatabase:readOnly:didMigrate:].cold.3
+ -[CNCDDatabasePreparationResult initWithURL:options:pristineDatabase:readOnly:didMigrate:].cold.4
+ -[CNCDTestPersistenceStack initWithModel:].cold.2
+ -[CNPersistentStoreCoordinatorUpdater updateCacheEntriesWithKeys:accountURLs:].cold.1
+ ABCDCompareByOrderingIndexWithPrimaryFirst_block_invoke_6.cold.1
+ ___swift_destroy_boxed_opaque_existential_0Tm
+ __softLink_CSBackupURLIsBackupItemAvailable_block_invoke.cold.1
+ _swift_retain_n
+ init_CSBackupURLIsBackupItem.cold.1
- _OUTLINED_FUNCTION_11
- ___swift_destroy_boxed_opaque_existential_1
CStrings:
- "Division by zero"
- "Division results in an overflow"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/IntegerTypes.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutablePointer.initialize with negative count"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "invalid Collection: less than 'count' elements in collection"

```
