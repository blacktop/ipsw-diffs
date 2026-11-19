## HealthDaemonFoundation

> `/System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/Versions/A/HealthDaemonFoundation`

```diff

-7027.0.72.1.1
-  __TEXT.__text: 0x78004
-  __TEXT.__objc_methlist: 0x3d8c
-  __TEXT.__const: 0x22f2
-  __TEXT.__cstring: 0x496a
-  __TEXT.__oslogstring: 0x35f6
-  __TEXT.__gcc_except_tab: 0x3010
-  __TEXT.__swift5_typeref: 0xc12
-  __TEXT.__swift5_reflstr: 0x88b
-  __TEXT.__swift5_assocty: 0xd8
-  __TEXT.__constg_swiftt: 0xbb0
+7027.1.56.1.1
+  __TEXT.__text: 0x7b62c
+  __TEXT.__objc_methlist: 0x3e34
+  __TEXT.__const: 0x2372
+  __TEXT.__cstring: 0x4b1b
+  __TEXT.__oslogstring: 0x3745
+  __TEXT.__gcc_except_tab: 0x30f8
+  __TEXT.__swift5_typeref: 0xd2c
+  __TEXT.__swift5_reflstr: 0x90b
+  __TEXT.__swift5_assocty: 0xa8
+  __TEXT.__constg_swiftt: 0xcec
   __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_fieldmd: 0x938
-  __TEXT.__swift5_proto: 0x10c
-  __TEXT.__swift5_types: 0xb8
-  __TEXT.__swift5_capture: 0x494
-  __TEXT.__swift5_protos: 0x2c
+  __TEXT.__swift5_fieldmd: 0xa04
+  __TEXT.__swift5_proto: 0x100
+  __TEXT.__swift5_types: 0xc4
+  __TEXT.__swift5_capture: 0x520
+  __TEXT.__swift5_protos: 0x38
+  __TEXT.__swift5_mpenum: 0x24
   __TEXT.__swift5_types2: 0xc
-  __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x2938
-  __TEXT.__eh_frame: 0x1490
+  __TEXT.__unwind_info: 0x2a08
+  __TEXT.__eh_frame: 0x1510
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x570
-  __DATA_CONST.__objc_classlist: 0x2f0
+  __DATA_CONST.__objc_classlist: 0x308
   __DATA_CONST.__objc_catlist: 0x18
-  __DATA_CONST.__objc_protolist: 0xf0
+  __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2178
-  __DATA_CONST.__objc_protorefs: 0x70
+  __DATA_CONST.__objc_selrefs: 0x21a8
+  __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x18
-  __DATA_CONST.__got: 0x698
-  __AUTH_CONST.__const: 0x3688
-  __AUTH_CONST.__cfstring: 0x4000
-  __AUTH_CONST.__objc_const: 0x86d0
+  __DATA_CONST.__got: 0x6b0
+  __AUTH_CONST.__const: 0x38f8
+  __AUTH_CONST.__cfstring: 0x40e0
+  __AUTH_CONST.__objc_const: 0x8968
   __AUTH_CONST.__weak_auth_got: 0x18
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0xef0
-  __AUTH_CONST.__auth_ptr: 0x2f0
-  __AUTH.__objc_data: 0xa60
-  __AUTH.__data: 0x150
+  __AUTH_CONST.__auth_got: 0xef8
+  __AUTH_CONST.__auth_ptr: 0x300
+  __AUTH.__objc_data: 0xb20
+  __AUTH.__data: 0x2d0
   __DATA.__objc_ivar: 0x568
-  __DATA.__data: 0xc50
-  __DATA.__bss: 0x1f90
+  __DATA.__data: 0xbf0
+  __DATA.__bss: 0x1d30
   __DATA_DIRTY.__objc_data: 0x16d8
-  __DATA_DIRTY.__data: 0xa28
-  __DATA_DIRTY.__bss: 0xd0
+  __DATA_DIRTY.__data: 0xae8
+  __DATA_DIRTY.__bss: 0xe0
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3126
-  Symbols:   4680
-  CStrings:  895
+  Functions: 3183
+  Symbols:   4733
+  CStrings:  910
 
Symbols:
+ +[HDSQLiteSchemaEntity hasStaticJoinClauses]
+ -[HDDatabaseAssertionManager _lock_releaseBackgroundAccessForFiles:]
+ -[HDSQLiteDatabase truncateWriteAheadLogWithBusyTimeout:contended:error:]
+ -[HDSQLiteQueryDescriptor _uncachedJoinClauseForProperties:predicateJoinClauses:]
+ -[HDXPCProcess isFirstParty]
+ -[HDXPCProcess unitTest_copyProcessWithBundleIdentifier:]
+ GCC_except_table112
+ GCC_except_table117
+ GCC_except_table122
+ GCC_except_table124
+ GCC_except_table130
+ GCC_except_table44
+ GCC_except_table94
+ GCC_except_table96
+ GCC_except_table98
+ _OBJC_METACLASS_$__TtC22HealthDaemonFoundationP33_5018826988AE70FF0AC90E49818760A638_ContentProtectionAvailabilityObserver
+ _PROTOCOLS__TtC22HealthDaemonFoundationP33_5018826988AE70FF0AC90E49818760A638_ContentProtectionAvailabilityObserver
+ __CLASS_METHODS_HDFastPassBackgroundTask
+ __CLASS_METHODS_HDOneShotBackgroundTask
+ __DATA__TtC22HealthDaemonFoundationP33_5018826988AE70FF0AC90E49818760A638_ContentProtectionAvailabilityObserver
+ __DATA__TtC22HealthDaemonFoundationP33_5018826988AE70FF0AC90E49818760A641_ContentProtectionAvailabilityObservation
+ __DATA__TtCC22HealthDaemonFoundation31SQLiteDatabaseConnectionManagerP33_B2576AEC8BE9BB02E063715B6C40AF0F25DatabaseConnectionFlusher
+ __INSTANCE_METHODS__TtC22HealthDaemonFoundationP33_5018826988AE70FF0AC90E49818760A638_ContentProtectionAvailabilityObserver
+ __IVARS__TtC22HealthDaemonFoundationP33_5018826988AE70FF0AC90E49818760A638_ContentProtectionAvailabilityObserver
+ __IVARS__TtC22HealthDaemonFoundationP33_5018826988AE70FF0AC90E49818760A641_ContentProtectionAvailabilityObservation
+ __IVARS__TtCC22HealthDaemonFoundation31SQLiteDatabaseConnectionManagerP33_B2576AEC8BE9BB02E063715B6C40AF0F25DatabaseConnectionFlusher
+ __METACLASS_DATA__TtC22HealthDaemonFoundationP33_5018826988AE70FF0AC90E49818760A638_ContentProtectionAvailabilityObserver
+ __METACLASS_DATA__TtC22HealthDaemonFoundationP33_5018826988AE70FF0AC90E49818760A641_ContentProtectionAvailabilityObservation
+ __METACLASS_DATA__TtCC22HealthDaemonFoundation31SQLiteDatabaseConnectionManagerP33_B2576AEC8BE9BB02E063715B6C40AF0F25DatabaseConnectionFlusher
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HDContentProtectionObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HDContentProtectionObserver
+ __OBJC_$_PROTOCOL_REFS_HDContentProtectionObserver
+ __OBJC_LABEL_PROTOCOL_$_HDContentProtectionObserver
+ __OBJC_PROTOCOL_$_HDContentProtectionObserver
+ __PROTOCOLS__TtC22HealthDaemonFoundationP33_5018826988AE70FF0AC90E49818760A638_ContentProtectionAvailabilityObserver
+ __ZZ25HDSQLiteEntityForPropertyE18propertyOwnerCache
+ __ZZ25HDSQLiteEntityForPropertyE23_propertyOwnerCacheLock
+ __ZZL25_HDSQLiteCachedJoinClauseP10objc_classP7NSArrayIP8NSStringEU13block_pointerFS3_vEE15joinClauseCache
+ __ZZL25_HDSQLiteCachedJoinClauseP10objc_classP7NSArrayIP8NSStringEU13block_pointerFS3_vEE19joinClauseCacheLock
+ __ZZL25_HDSQLiteCachedJoinClauseP10objc_classP7NSArrayIP8NSStringEU13block_pointerFS3_vEE25reportedSaturatedEntities
+ ___52-[HDSQLiteQueryDescriptor _joinClauseForProperties:]_block_invoke
+ ___73-[HDSQLiteDatabase truncateWriteAheadLogWithBusyTimeout:contended:error:]_block_invoke
+ ___block_descriptor_56_ea8_32s40s48s_e15_"NSString"8?0l
+ ___swift_memcpy41_8
+ ___swift_project_boxed_opaque_existential_0
+ _get_enum_tag_for_layout_string 22HealthDaemonFoundation14DataProtectionO
+ _objc_msgSend$addContentProtectionObserver:withQueue:
+ _objc_msgSend$hasStaticJoinClauses
+ _objc_msgSend$mapTableWithKeyOptions:valueOptions:
+ _objc_msgSend$removeContentProtectionObserver:
+ _objc_msgSend$unsignedLongLongValue
+ _symbolic $s22HealthDaemonFoundation0B14PluginProviderP
+ _symbolic $s22HealthDaemonFoundation27ContentProtectionMonitoringP
+ _symbolic $s22HealthDaemonFoundation28ContentProtectionObservationP
+ _symbolic SS4name______12directoryURL_____10protectiont 10Foundation3URLV 012HealthDaemonA014DataProtectionO
+ _symbolic So26HDContentProtectionManagerCSgXw
+ _symbolic So26HDContentProtectionManagerCSgXwz_Xx
+ _symbolic _____ 22HealthDaemonFoundation14DataProtectionO
+ _symbolic _____ 22HealthDaemonFoundation31SQLiteDatabaseConnectionManagerC0eF7Flusher33_B2576AEC8BE9BB02E063715B6C40AF0FLLC
+ _symbolic _____ 22HealthDaemonFoundation38_ContentProtectionAvailabilityObserver33_5018826988AE70FF0AC90E49818760A6LLC
+ _symbolic _____ 22HealthDaemonFoundation41_ContentProtectionAvailabilityObservation33_5018826988AE70FF0AC90E49818760A6LLC
+ _symbolic _____Sg 22HealthDaemonFoundation31SQLiteDatabaseConnectionManagerC0eF7Flusher33_B2576AEC8BE9BB02E063715B6C40AF0FLLC
+ _symbolic ______p 22HealthDaemonFoundation28ContentProtectionObservationP
+ _symbolic ______p7monitor_t 22HealthDaemonFoundation27ContentProtectionMonitoringP
+ _symbolic _____ySbG 15Synchronization5MutexVAARi_zrlE
+ _symbolic ySbYbc
+ _symbolic yyYbc
+ _type_layout_string 22HealthDaemonFoundation14DataProtectionO
- GCC_except_table100
- GCC_except_table103
- GCC_except_table107
- GCC_except_table115
- GCC_except_table118
- GCC_except_table119
- GCC_except_table126
- GCC_except_table128
- GCC_except_table20
- GCC_except_table83
- _associated conformance So20NSFileProtectionTypeaSHSCSQ
- _associated conformance So20NSFileProtectionTypeas20_SwiftNewtypeWrapperSCSY
- _associated conformance So20NSFileProtectionTypeas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
- _symbolic SS4name______12directoryURL_____18fileProtectionTypet 10Foundation3URLV So20NSFileProtectionTypea
- _symbolic _____ So20NSFileProtectionTypea
CStrings:
+ "\" entitlement: got "
+ "%{public}@: Failed to open a database file to release the assertion: %d"
+ "/locked-access"
+ "<%@ %@ %@ %@%@ ctx:%ld%@: %@>"
+ "@\"NSString\"8@?0"
+ "Cannot resolve process identifier for empty application identifier."
+ "Failed to continue activity"
+ "Failed to open a database file to request the assertion: %d"
+ "Failed to publish XPC event for %llu with error: %d"
+ "Failed to request the assertion: %d"
+ "HDXPCClient connection is nil; cannot validate \""
+ "HealthDaemonFoundation._ContentProtectionAvailabilityObserver"
+ "Join clause memo reached its ceiling of %lu shapes for %{public}@; fragments for this entity are now rebuilt per query"
+ "PRAGMA wal_checkpoint(truncate)"
+ "Published XPC event for %llu"
+ "[%s] Unable to open or prepare database due to error: %@"
+ "[%{public}s] protected data unavailable, flushing cached connections"
+ "com.apple."
+ "com.apple.HealthDaemonFoundation.connection-flush-on-lock."
+ "com.appleinternal."
+ "name directoryURL protection "
- "<%@ %@ %@ %@%@: %@>"
- "Failed to publish XPC event for %ld with error: %d"
- "Published XPC event for %ld"
- "[%s] Unable to prepare database due to error: %@"
- "name directoryURL fileProtectionType "
- "\x91"
```
