## HealthAppHealthDaemon

> `/System/Library/PrivateFrameworks/HealthAppHealthDaemon.framework/HealthAppHealthDaemon`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__DATA.__objc_stublist`
- `__DATA_DIRTY.__objc_data`

```diff

-7027.0.64.0.0
-  __TEXT.__text: 0x3b9b8
-  __TEXT.__objc_methlist: 0x1adc
-  __TEXT.__const: 0x1fd0
+7027.0.67.2.1
+  __TEXT.__text: 0x45d8c
+  __TEXT.__objc_methlist: 0x1ddc
+  __TEXT.__const: 0x2180
   __TEXT.__gcc_except_tab: 0x114
-  __TEXT.__cstring: 0x1456
-  __TEXT.__oslogstring: 0x2193
-  __TEXT.__constg_swiftt: 0x89c
-  __TEXT.__swift5_typeref: 0x7d6
-  __TEXT.__swift5_fieldmd: 0x634
+  __TEXT.__cstring: 0x15a6
+  __TEXT.__oslogstring: 0x23d4
+  __TEXT.__constg_swiftt: 0x934
+  __TEXT.__swift5_typeref: 0x814
+  __TEXT.__swift5_fieldmd: 0x67c
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__swift5_types: 0xb4
-  __TEXT.__swift5_reflstr: 0x566
-  __TEXT.__swift5_proto: 0x160
-  __TEXT.__swift5_capture: 0x104
+  __TEXT.__swift5_reflstr: 0x598
+  __TEXT.__swift5_assocty: 0x1b0
+  __TEXT.__swift5_proto: 0x174
+  __TEXT.__swift5_types: 0xc0
+  __TEXT.__swift5_capture: 0x14c
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__swift5_assocty: 0x198
   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x1c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x11e0
-  __TEXT.__eh_frame: 0x1b50
+  __TEXT.__unwind_info: 0x13e8
+  __TEXT.__eh_frame: 0x2018
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x648
-  __DATA_CONST.__objc_classlist: 0x108
+  __DATA_CONST.__const: 0x638
+  __DATA_CONST.__objc_classlist: 0x120
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x140
+  __DATA_CONST.__objc_protolist: 0x148
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1238
+  __DATA_CONST.__objc_selrefs: 0x13d8
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0x70
+  __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x720
-  __AUTH_CONST.__const: 0x1290
-  __AUTH_CONST.__cfstring: 0x840
-  __AUTH_CONST.__objc_const: 0x2c80
+  __DATA_CONST.__got: 0x758
+  __AUTH_CONST.__const: 0x1488
+  __AUTH_CONST.__cfstring: 0x900
+  __AUTH_CONST.__objc_const: 0x3068
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0xf10
-  __AUTH.__objc_data: 0x320
-  __AUTH.__data: 0xc0
-  __DATA.__objc_ivar: 0xf8
-  __DATA.__data: 0xff0
+  __AUTH_CONST.__auth_got: 0xfe0
+  __AUTH.__objc_data: 0x470
+  __AUTH.__data: 0xe8
+  __DATA.__objc_ivar: 0x11c
+  __DATA.__data: 0x1100
   __DATA.__objc_stublist: 0x8
-  __DATA.__bss: 0x1c10
+  __DATA.__bss: 0x1e90
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xb88
-  __DATA_DIRTY.__data: 0x900
+  __DATA_DIRTY.__data: 0x930
   __DATA_DIRTY.__bss: 0xd80
   __DATA_DIRTY.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MobileInstallation.framework/MobileInstallation
+  - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1450
-  Symbols:   1674
-  CStrings:  284
+  Functions: 1614
+  Symbols:   1828
+  CStrings:  302
 
Symbols:
+ +[HACodableUserInteractionSync interactionsType]
+ -[HACodableUserInteraction .cxx_destruct]
+ -[HACodableUserInteraction copyTo:]
+ -[HACodableUserInteraction copyWithZone:]
+ -[HACodableUserInteraction description]
+ -[HACodableUserInteraction dictionaryRepresentation]
+ -[HACodableUserInteraction expirationDate]
+ -[HACodableUserInteraction featureIdentifier]
+ -[HACodableUserInteraction hasExpirationDate]
+ -[HACodableUserInteraction hasFeatureIdentifier]
+ -[HACodableUserInteraction hasInteractionDate]
+ -[HACodableUserInteraction hasInteractionType]
+ -[HACodableUserInteraction hasItemIdentifier]
+ -[HACodableUserInteraction hasUuid]
+ -[HACodableUserInteraction hash]
+ -[HACodableUserInteraction interactionDate]
+ -[HACodableUserInteraction interactionType]
+ -[HACodableUserInteraction isEqual:]
+ -[HACodableUserInteraction itemIdentifier]
+ -[HACodableUserInteraction mergeFrom:]
+ -[HACodableUserInteraction readFrom:]
+ -[HACodableUserInteraction setExpirationDate:]
+ -[HACodableUserInteraction setFeatureIdentifier:]
+ -[HACodableUserInteraction setHasExpirationDate:]
+ -[HACodableUserInteraction setHasInteractionDate:]
+ -[HACodableUserInteraction setInteractionDate:]
+ -[HACodableUserInteraction setInteractionType:]
+ -[HACodableUserInteraction setItemIdentifier:]
+ -[HACodableUserInteraction setUuid:]
+ -[HACodableUserInteraction uuid]
+ -[HACodableUserInteraction writeTo:]
+ -[HACodableUserInteractionSync .cxx_destruct]
+ -[HACodableUserInteractionSync addInteractions:]
+ -[HACodableUserInteractionSync clearInteractions]
+ -[HACodableUserInteractionSync copyTo:]
+ -[HACodableUserInteractionSync copyWithZone:]
+ -[HACodableUserInteractionSync description]
+ -[HACodableUserInteractionSync dictionaryRepresentation]
+ -[HACodableUserInteractionSync hash]
+ -[HACodableUserInteractionSync interactionsAtIndex:]
+ -[HACodableUserInteractionSync interactionsCount]
+ -[HACodableUserInteractionSync interactions]
+ -[HACodableUserInteractionSync isEqual:]
+ -[HACodableUserInteractionSync mergeFrom:]
+ -[HACodableUserInteractionSync readFrom:]
+ -[HACodableUserInteractionSync setInteractions:]
+ -[HACodableUserInteractionSync writeTo:]
+ -[HDHealthAppDaemonExtension runUpdateSharingReminderScheduledAlarmCommand]
+ -[HDHealthAppSharingReminderRestorableAlarm _migrateLegacySyncedSharingReminderDateIfNeeded]
+ OBJC_IVAR_$_HACodableUserInteraction._expirationDate
+ OBJC_IVAR_$_HACodableUserInteraction._featureIdentifier
+ OBJC_IVAR_$_HACodableUserInteraction._has
+ OBJC_IVAR_$_HACodableUserInteraction._interactionDate
+ OBJC_IVAR_$_HACodableUserInteraction._interactionType
+ OBJC_IVAR_$_HACodableUserInteraction._itemIdentifier
+ OBJC_IVAR_$_HACodableUserInteraction._uuid
+ OBJC_IVAR_$_HACodableUserInteractionSync._interactions
+ _HACodableUserInteractionReadFrom
+ _HACodableUserInteractionSyncReadFrom
+ _IsOutgoingInvite
+ _OBJC_CLASS_$_HACodableUserInteraction
+ _OBJC_CLASS_$_HACodableUserInteractionSync
+ _OBJC_CLASS_$_HAHDUserInteractionStateSyncEntity
+ _OBJC_CLASS_$_PBCodable
+ _OBJC_IVAR_$_HDHealthAppSharingReminderRestorableAlarm._legacySyncedSharingKeyValueDomain
+ _OBJC_METACLASS_$_HACodableUserInteraction
+ _OBJC_METACLASS_$_HACodableUserInteractionSync
+ _OBJC_METACLASS_$_HAHDUserInteractionStateSyncEntity
+ _OBJC_METACLASS_$_PBCodable
+ _PBDataWriterWriteDataField
+ _PBDataWriterWriteDoubleField
+ _PBDataWriterWriteStringField
+ _PBDataWriterWriteSubmessage
+ _PBReaderPlaceMark
+ _PBReaderReadData
+ _PBReaderReadString
+ _PBReaderRecallMark
+ _PBReaderSkipValueWithTag
+ __CLASS_METHODS_HAHDUserInteractionStateSyncEntity
+ __CLASS_PROPERTIES_HAHDUserInteractionStateSyncEntity
+ __DATA_HAHDUserInteractionStateSyncEntity
+ __INSTANCE_METHODS_HAHDUserInteractionStateSyncEntity
+ __METACLASS_DATA_HAHDUserInteractionStateSyncEntity
+ __OBJC_$_CLASS_METHODS_HACodableUserInteractionSync
+ __OBJC_$_INSTANCE_METHODS_HACodableUserInteraction
+ __OBJC_$_INSTANCE_METHODS_HACodableUserInteractionSync
+ __OBJC_$_INSTANCE_METHODS_HDHealthAppDaemonExtension(HealthAppHealthDaemon)
+ __OBJC_$_INSTANCE_VARIABLES_HACodableUserInteraction
+ __OBJC_$_INSTANCE_VARIABLES_HACodableUserInteractionSync
+ __OBJC_$_PROP_LIST_HACodableUserInteraction
+ __OBJC_$_PROP_LIST_HACodableUserInteractionSync
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_CLASS_PROTOCOLS_$_HACodableUserInteraction
+ __OBJC_CLASS_PROTOCOLS_$_HACodableUserInteractionSync
+ __OBJC_CLASS_RO_$_HACodableUserInteraction
+ __OBJC_CLASS_RO_$_HACodableUserInteractionSync
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_METACLASS_RO_$_HACodableUserInteraction
+ __OBJC_METACLASS_RO_$_HACodableUserInteractionSync
+ __OBJC_PROTOCOL_$_NSCopying
+ __PROTOCOLS_HAHDUserInteractionStateSyncEntity
+ ___75-[HDHealthAppDaemonExtension runUpdateSharingReminderScheduledAlarmCommand]_block_invoke
+ __swift_stdlib_bridgeErrorToNSError
+ _associated conformance 09HealthAppA6Daemon30UserInteractionStateSyncEntityC11DecodeErrorOSHAASQ
+ _objc_msgSend$_migrateLegacySyncedSharingReminderDateIfNeeded
+ _objc_msgSend$_setError
+ _objc_msgSend$addInteractions:
+ _objc_msgSend$allocWithZone:
+ _objc_msgSend$clearInteractions
+ _objc_msgSend$commandLineDispatcher
+ _objc_msgSend$copyWithZone:
+ _objc_msgSend$dictionary
+ _objc_msgSend$dictionaryRepresentation
+ _objc_msgSend$expirationDate
+ _objc_msgSend$featureIdentifier
+ _objc_msgSend$getBytes:range:
+ _objc_msgSend$hasError
+ _objc_msgSend$hasExpirationDate
+ _objc_msgSend$hash
+ _objc_msgSend$initWithCapacity:
+ _objc_msgSend$interactionDate
+ _objc_msgSend$interactionType
+ _objc_msgSend$interactions
+ _objc_msgSend$interactionsAtIndex:
+ _objc_msgSend$interactionsCount
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isMemberOfClass:
+ _objc_msgSend$itemIdentifier
+ _objc_msgSend$length
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$objectAtIndex:
+ _objc_msgSend$position
+ _objc_msgSend$queue
+ _objc_msgSend$registerDebugCommandsWithDaemon:
+ _objc_msgSend$removeAllObjects
+ _objc_msgSend$removeValuesForKeys:error:
+ _objc_msgSend$runUpdateSharingReminderScheduledAlarmCommand
+ _objc_msgSend$schemaWithDomain:
+ _objc_msgSend$setFeatureIdentifier:
+ _objc_msgSend$setInteractionDate:
+ _objc_msgSend$setInteractionType:
+ _objc_msgSend$setItemIdentifier:
+ _objc_msgSend$setObject:forKey:
+ _objc_msgSend$setPosition:
+ _objc_msgSend$setUuid:
+ _objc_msgSend$setWithObject:
+ _objc_msgSend$uuid
+ _swift_release_x12
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _symbolic So26HDHealthAppDaemonExtensionCSgXw
+ _symbolic _____ 09HealthAppA6Daemon04WeakC9Extension33_DCA2C41A74E113AF13803D8BBA83189DLLV
+ _symbolic _____ 09HealthAppA6Daemon30UserInteractionStateSyncEntityC
+ _symbolic _____ 09HealthAppA6Daemon30UserInteractionStateSyncEntityC11DecodeErrorO
+ _type_layout_string 09HealthAppA6Daemon04WeakC9Extension33_DCA2C41A74E113AF13803D8BBA83189DLLV
- _HAHealthAppLegacySharingEntriesDomain
- _HAHealthAppLegacySharingReminderNotificationDateKey
- __OBJC_$_INSTANCE_METHODS_HDHealthAppDaemonExtension
CStrings:
+ " WHERE feature_identifier = ?"
+ "$"
+ "%@ %@"
+ "Re-run HDHealthAppDaemonExtension -updateSharingReminderScheduledAlarm"
+ "SELECT DISTINCT feature_identifier FROM HealthAppDatabaseSchema_user_interactions"
+ "[%s] Bulk updateData was called on a dynamic-key entity; per-key path expected"
+ "[%s] Encoded interaction record is %ld bytes; approaching CloudKit per-record limit"
+ "[%s] Failed to fetch distinct feature identifiers: %@"
+ "[%s] No user interaction store on profile for feature %s"
+ "[%s] State sync finished for feature %s with %s"
+ "[%{public}@] Could not migrate sharing reminder date to device-local store: %{public}@"
+ "[%{public}@] Could not read device-local sharing reminder date during migration: %{public}@"
+ "[%{public}@] Could not remove legacy synced sharing reminder date after migration: %{public}@"
+ "[%{public}@] Could not set sharing reminder anchor date: %{public}@. Will try again on handling alarm event."
+ "[%{public}@] Migrated sharing reminder date %{public}@ from legacy synced store to device-local store"
+ "[%{public}@] Set sharing reminder anchor date to: %{public}@"
+ "expirationDate"
+ "extension deallocated"
+ "featureIdentifier"
+ "health-sharing-reminder-notification-trigger"
+ "interactionDate"
+ "interactionType"
+ "interactions"
+ "itemIdentifier"
- "SharingReminderNotificationDate"
- "[%{public}@] Could not set sharing reminder date: %{public}@. Will try again on handling alarm event."
- "[%{public}@] No fallback date found, using current date as backup to the backup: %@"
- "[%{public}@] Set sharing reminder date to existing date: %{public}@"
- "[%{public}@] Set sharing reminder date to fallback date: %{public}@"
- "com.apple.Health.SharingEntries"
```
