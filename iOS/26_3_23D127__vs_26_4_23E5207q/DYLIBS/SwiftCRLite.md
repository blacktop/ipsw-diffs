## SwiftCRLite

> `/System/Library/PrivateFrameworks/SwiftCRLite.framework/SwiftCRLite`

```diff

-3.60.1.0.0
-  __TEXT.__text: 0x49cc
-  __TEXT.__auth_stubs: 0x760
-  __TEXT.__objc_methlist: 0x50
-  __TEXT.__const: 0x31a
-  __TEXT.__cstring: 0x2aa
-  __TEXT.__swift5_typeref: 0x139
-  __TEXT.__oslogstring: 0x98
-  __TEXT.__swift5_reflstr: 0x23
-  __TEXT.__swift5_assocty: 0x18
-  __TEXT.__constg_swiftt: 0xcc
-  __TEXT.__swift5_fieldmd: 0x44
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_proto: 0x20
-  __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x1a0
-  __TEXT.__eh_frame: 0xf0
-  __TEXT.__objc_methname: 0x84
-  __TEXT.__objc_stubs: 0x60
-  __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0x58
-  __DATA_CONST.__objc_classlist: 0x8
+3.100.14.0.0
+  __TEXT.__text: 0x2bd1c
+  __TEXT.__auth_stubs: 0x1490
+  __TEXT.__objc_methlist: 0x460
+  __TEXT.__const: 0x275c
+  __TEXT.__cstring: 0x192c
+  __TEXT.__oslogstring: 0x2e1
+  __TEXT.__swift5_typeref: 0x835
+  __TEXT.__swift5_reflstr: 0x97f
+  __TEXT.__swift5_assocty: 0x198
+  __TEXT.__constg_swiftt: 0xa58
+  __TEXT.__swift5_fieldmd: 0xc7c
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_proto: 0x1d0
+  __TEXT.__swift5_types: 0xb4
+  __TEXT.__swift_as_entry: 0x4
+  __TEXT.__swift_as_ret: 0x4
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift5_capture: 0xd4
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__unwind_info: 0xba8
+  __TEXT.__eh_frame: 0x1658
+  __TEXT.__objc_classname: 0x193
+  __TEXT.__objc_methname: 0x7ab
+  __TEXT.__objc_methtype: 0x3e2
+  __TEXT.__objc_stubs: 0x8a0
+  __DATA_CONST.__got: 0x290
+  __DATA_CONST.__const: 0xb8
+  __DATA_CONST.__objc_classlist: 0x50
+  __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x3b8
-  __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0x70
-  __AUTH.__objc_data: 0x100
-  __AUTH.__data: 0xa8
-  __DATA.__data: 0xc0
-  __DATA.__bss: 0x430
+  __DATA_CONST.__objc_selrefs: 0x310
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x10
+  __AUTH_CONST.__auth_got: 0xa50
+  __AUTH_CONST.__const: 0x1880
+  __AUTH_CONST.__cfstring: 0x160
+  __AUTH_CONST.__objc_const: 0xa00
+  __AUTH.__objc_data: 0x1f0
+  __AUTH.__data: 0xc00
+  __DATA.__objc_ivar: 0x18
+  __DATA.__data: 0x7e0
+  __DATA.__bss: 0x3990
+  __DATA.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
+  - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/CascadingFilters.framework/CascadingFilters
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/libsqlite3.dylib
+  - /usr/lib/libz.1.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: D804DAE7-33BF-38E9-99B1-4C15BB2C0846
-  Functions: 102
-  Symbols:   153
-  CStrings:  31
+  UUID: C223CE27-F5DE-386B-B883-8EE69E5E8554
+  Functions: 1015
+  Symbols:   736
+  CStrings:  380
 
Symbols:
+ -[ValidDBObjc .cxx_destruct]
+ -[ValidDBObjc autoVacuumSetting]
+ -[ValidDBObjc close]
+ -[ValidDBObjc db]
+ -[ValidDBObjc dealloc]
+ -[ValidDBObjc executeSQL:]
+ -[ValidDBObjc executeSQL:arguments:]
+ -[ValidDBObjc executeSQLStmt:]
+ -[ValidDBObjc initDatabaseWithURL:]
+ -[ValidDBObjc log]
+ -[ValidDBObjc prepareStatement:error:]
+ -[ValidDBObjc setDb:]
+ -[ValidDBObjc setLog:]
+ -[ValidDBStmt .cxx_destruct]
+ -[ValidDBStmt allObjectsByColumnName]
+ -[ValidDBStmt allObjects]
+ -[ValidDBStmt bindData:column:]
+ -[ValidDBStmt bindDate:column:]
+ -[ValidDBStmt bindDouble:column:]
+ -[ValidDBStmt bindInt64:column:]
+ -[ValidDBStmt bindInt:column:]
+ -[ValidDBStmt bindNullAtColumn:]
+ -[ValidDBStmt bindString:column:]
+ -[ValidDBStmt blobAtColumn:]
+ -[ValidDBStmt clearBindings]
+ -[ValidDBStmt columnCount]
+ -[ValidDBStmt columnNameAtColumn:]
+ -[ValidDBStmt columnTypeAtColumn:]
+ -[ValidDBStmt dateAtColumn:]
+ -[ValidDBStmt db]
+ -[ValidDBStmt dealloc]
+ -[ValidDBStmt doubleAtColumn:]
+ -[ValidDBStmt enumerateColumnsUsingBlock:]
+ -[ValidDBStmt generateDone]
+ -[ValidDBStmt generateDone].cold.1
+ -[ValidDBStmt generateError:method:]
+ -[ValidDBStmt indexForColumnName:]
+ -[ValidDBStmt indexesByColumnName]
+ -[ValidDBStmt initWithStatement:db:error:]
+ -[ValidDBStmt int64AtColumn:]
+ -[ValidDBStmt intAtColumn:]
+ -[ValidDBStmt needReset]
+ -[ValidDBStmt objectAtColumn:]
+ -[ValidDBStmt reset]
+ -[ValidDBStmt setDb:]
+ -[ValidDBStmt setIndexesByColumnName:]
+ -[ValidDBStmt setNeedReset:]
+ -[ValidDBStmt setStmt:]
+ -[ValidDBStmt stepWithError:]
+ -[ValidDBStmt steps:error:]
+ -[ValidDBStmt stmt]
+ -[ValidDBStmt textAtColumn:]
+ _NSLocalizedDescriptionKey
+ _NSLocalizedFailureReasonErrorKey
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSMutableArray
+ _OBJC_CLASS_$_NSMutableData
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSNull
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_NSURLSession
+ _OBJC_CLASS_$_OS_dispatch_queue
+ _OBJC_CLASS_$_ValidDBObjc
+ _OBJC_CLASS_$_ValidDBStmt
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_ValidDBObjc._db
+ _OBJC_IVAR_$_ValidDBObjc._log
+ _OBJC_IVAR_$_ValidDBStmt._db
+ _OBJC_IVAR_$_ValidDBStmt._indexesByColumnName
+ _OBJC_IVAR_$_ValidDBStmt._needReset
+ _OBJC_IVAR_$_ValidDBStmt._stmt
+ _OBJC_METACLASS_$_ValidDBObjc
+ _OBJC_METACLASS_$_ValidDBStmt
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _SecCMSVerify
+ _SecCRLiteCopyCoverageInfo
+ _SecCertificateCopyData
+ _SecPolicyCreateApplePinned
+ _SecTrustGetTrustResult
+ _ValidDBObjcErrorDomain
+ _ValidDeflatedNTO1Data
+ _ValidInflatedNTO1Data
+ __Block_copy
+ __Block_release
+ __DATA__TtC11SwiftCRLite12ValidSwiftDB
+ __DATA__TtC11SwiftCRLite13ValidDatabase
+ __DATA__TtC11SwiftCRLite15ValidDownloader
+ __DATA__TtC11SwiftCRLite15ValidPatchApply
+ __DATA__TtC11SwiftCRLite17ValidUpdateParser
+ __DATA__TtCC11SwiftCRLite12ValidSwiftDB12SQLStatement
+ __DATA__TtCC11SwiftCRLite12ValidSwiftDB6SQLRow
+ __IVARS__TtC11SwiftCRLite12ValidSwiftDB
+ __IVARS__TtC11SwiftCRLite13ValidDatabase
+ __IVARS__TtC11SwiftCRLite15ValidPatchApply
+ __IVARS__TtC11SwiftCRLite17ValidUpdateParser
+ __IVARS__TtCC11SwiftCRLite12ValidSwiftDB12SQLStatement
+ __IVARS__TtCC11SwiftCRLite12ValidSwiftDB6SQLRow
+ __METACLASS_DATA__TtC11SwiftCRLite12ValidSwiftDB
+ __METACLASS_DATA__TtC11SwiftCRLite13ValidDatabase
+ __METACLASS_DATA__TtC11SwiftCRLite15ValidDownloader
+ __METACLASS_DATA__TtC11SwiftCRLite15ValidPatchApply
+ __METACLASS_DATA__TtC11SwiftCRLite17ValidUpdateParser
+ __METACLASS_DATA__TtCC11SwiftCRLite12ValidSwiftDB12SQLStatement
+ __METACLASS_DATA__TtCC11SwiftCRLite12ValidSwiftDB6SQLRow
+ __NSConcreteGlobalBlock
+ __NSConcreteStackBlock
+ __OBJC_$_INSTANCE_METHODS_ValidDBObjc
+ __OBJC_$_INSTANCE_METHODS_ValidDBStmt
+ __OBJC_$_INSTANCE_VARIABLES_ValidDBObjc
+ __OBJC_$_INSTANCE_VARIABLES_ValidDBStmt
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROP_LIST_ValidDBObjc
+ __OBJC_$_PROP_LIST_ValidDBStmt
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_ValidDBRow
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_ValidDBRow
+ __OBJC_$_PROTOCOL_REFS_ValidDBRow
+ __OBJC_CLASS_PROTOCOLS_$_ValidDBStmt
+ __OBJC_CLASS_RO_$_ValidDBObjc
+ __OBJC_CLASS_RO_$_ValidDBStmt
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_ValidDBRow
+ __OBJC_METACLASS_RO_$_ValidDBObjc
+ __OBJC_METACLASS_RO_$_ValidDBStmt
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_ValidDBRow
+ ___25-[ValidDBStmt allObjects]_block_invoke
+ ___27-[ValidDBStmt generateDone]_block_invoke
+ ___37-[ValidDBStmt allObjectsByColumnName]_block_invoke
+ ___block_descriptor_32_e5_v8?0l
+ ___block_descriptor_48_e8_32s40s_e21_v24?0Q8"NSString"16ls32l8s40l8
+ ___block_literal_global
+ ___swift_allocate_boxed_opaque_existential_1
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_memcpy0_1
+ ___swift_memcpy16_8
+ ___swift_memcpy17_8
+ ___swift_memcpy1_1
+ ___swift_memcpy24_8
+ ___swift_memcpy32_8
+ ___swift_memcpy40_8
+ ___swift_memcpy4_4
+ ___swift_memcpy64_8
+ ___swift_memcpy80_8
+ ___swift_memcpy9_8
+ ___swift_mutable_project_boxed_opaque_existential_1
+ ___swift_noop_void_return
+ ___swift_project_boxed_opaque_existential_1
+ __objc_autoreleasePoolPop
+ __objc_autoreleasePoolPush
+ __swiftImmortalRefCount
+ _associated conformance 11SwiftCRLite05ValidA7DBErrorO10Foundation13CustomNSErrorAAs5Error
+ _associated conformance 11SwiftCRLite05ValidA7DBErrorO10Foundation14LocalizedErrorAAs0G0
+ _associated conformance 11SwiftCRLite05ValidA7DBErrorOSHAASQ
+ _associated conformance 11SwiftCRLite0B14FilterMetaDataV10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLOSHAASQ
+ _associated conformance 11SwiftCRLite0B14FilterMetaDataV10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 11SwiftCRLite0B14FilterMetaDataV10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 11SwiftCRLite0B8MetaDataV10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLOSHAASQ
+ _associated conformance 11SwiftCRLite0B8MetaDataV10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 11SwiftCRLite0B8MetaDataV10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 11SwiftCRLite0aB5ErrorO10Foundation13CustomNSErrorAAs0C0
+ _associated conformance 11SwiftCRLite10ByteBufferVSHAASQ
+ _associated conformance 11SwiftCRLite11ParsingStepOSHAASQ
+ _associated conformance 11SwiftCRLite13ValidDatabaseC0C11GroupSearchV10CodingKeys011_DB83DCB2C0K20B812CDB9A1B19594C35ELLOSHAASQ
+ _associated conformance 11SwiftCRLite13ValidDatabaseC0C11GroupSearchV10CodingKeys011_DB83DCB2C0K20B812CDB9A1B19594C35ELLOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 11SwiftCRLite13ValidDatabaseC0C11GroupSearchV10CodingKeys011_DB83DCB2C0K20B812CDB9A1B19594C35ELLOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 11SwiftCRLite13ValidDatabaseC0C5GroupV10CodingKeys011_DB83DCB2C0J20B812CDB9A1B19594C35ELLOSHAASQ
+ _associated conformance 11SwiftCRLite13ValidDatabaseC0C5GroupV10CodingKeys011_DB83DCB2C0J20B812CDB9A1B19594C35ELLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 11SwiftCRLite13ValidDatabaseC0C5GroupV10CodingKeys011_DB83DCB2C0J20B812CDB9A1B19594C35ELLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 11SwiftCRLite13ValidDatabaseC0C8HashTypeOSHAASQ
+ _associated conformance 11SwiftCRLite13ValidDatabaseC9AdminDataV10CodingKeysOSHAASQ
+ _associated conformance 11SwiftCRLite13ValidDatabaseC9AdminDataV10CodingKeysOs0G3KeyAAs23CustomStringConvertible
+ _associated conformance 11SwiftCRLite13ValidDatabaseC9AdminDataV10CodingKeysOs0G3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 11SwiftCRLite14ValidInfoFlagsVs10SetAlgebraAASQ
+ _associated conformance 11SwiftCRLite14ValidInfoFlagsVs10SetAlgebraAAs25ExpressibleByArrayLiteral
+ _associated conformance 11SwiftCRLite14ValidInfoFlagsVs12CaseIterableAA8AllCasessADP_Sl
+ _associated conformance 11SwiftCRLite14ValidInfoFlagsVs9OptionSetAASY
+ _associated conformance 11SwiftCRLite14ValidInfoFlagsVs9OptionSetAAs0G7Algebra
+ _associated conformance 11SwiftCRLite15ByteBufferErrorOSHAASQ
+ _associated conformance 11SwiftCRLite15ValidInfoFormatOSHAASQ
+ _associated conformance 11SwiftCRLite15ValidInfoFormatOs12CaseIterableAA8AllCasessADP_Sl
+ _associated conformance 11SwiftCRLite15ValidUpdateNTO1V10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLOSHAASQ
+ _associated conformance 11SwiftCRLite15ValidUpdateNTO1V10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 11SwiftCRLite15ValidUpdateNTO1V10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 11SwiftCRLite16ValidCertificateV10CodingKeys33_09663FE52D983112A60B038FA6E8E857LLOSHAASQ
+ _associated conformance 11SwiftCRLite16ValidCertificateV10CodingKeys33_09663FE52D983112A60B038FA6E8E857LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 11SwiftCRLite16ValidCertificateV10CodingKeys33_09663FE52D983112A60B038FA6E8E857LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 11SwiftCRLite16ValidEnvironmentOSHAASQ
+ _associated conformance 11SwiftCRLite16ValidEnvironmentOs12CaseIterableAA8AllCasessADP_Sl
+ _associated conformance 11SwiftCRLite16ValidUpdatePlistV10CodingKeysOSHAASQ
+ _associated conformance 11SwiftCRLite16ValidUpdatePlistV10CodingKeysOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 11SwiftCRLite16ValidUpdatePlistV10CodingKeysOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance 11SwiftCRLite18ValidUpdateElementV10CodingKeysOSHAASQ
+ _associated conformance 11SwiftCRLite18ValidUpdateElementV10CodingKeysOs0F3KeyAAs23CustomStringConvertible
+ _associated conformance 11SwiftCRLite18ValidUpdateElementV10CodingKeysOs0F3KeyAAs28CustomDebugStringConvertible
+ _associated conformance SC16ValidDBObjcErrorLeV10Foundation021_ObjectiveCBridgeableC0SCs0C0
+ _associated conformance SC16ValidDBObjcErrorLeV10Foundation13CustomNSErrorSCs0C0
+ _associated conformance SC16ValidDBObjcErrorLeV10Foundation21_BridgedStoredNSErrorSC4CodeAcDP_8RawValueSYs17FixedWidthInteger
+ _associated conformance SC16ValidDBObjcErrorLeV10Foundation21_BridgedStoredNSErrorSC4CodeAcDP_AC01_cH8Protocol
+ _associated conformance SC16ValidDBObjcErrorLeV10Foundation21_BridgedStoredNSErrorSC4CodeAcDP_SY
+ _associated conformance SC16ValidDBObjcErrorLeV10Foundation21_BridgedStoredNSErrorSCAC021_ObjectiveCBridgeableC0
+ _associated conformance SC16ValidDBObjcErrorLeV10Foundation21_BridgedStoredNSErrorSCAC06CustomG0
+ _associated conformance SC16ValidDBObjcErrorLeV10Foundation21_BridgedStoredNSErrorSCSH
+ _associated conformance SC16ValidDBObjcErrorLeVSHSCSQ
+ _associated conformance So16ValidDBObjcErrorV10Foundation01_C12CodeProtocolSC01_C4TypeAcDP_AC21_BridgedStoredNSError
+ _associated conformance So16ValidDBObjcErrorV10Foundation01_C12CodeProtocolSCSQ
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _deflate
+ _deflateEnd
+ _deflateInit_
+ _dispatch_once
+ _flat unique So10ValidDBRow_p
+ _free
+ _generateDone.done
+ _generateDone.onceToken
+ _get_enum_tag_for_layout_string 10Foundation4DataV15_RepresentationO
+ _get_enum_tag_for_layout_string 10Foundation4DataVSg
+ _inflate
+ _inflateEnd
+ _inflateInit2_
+ _malloc_good_size
+ _malloc_type_malloc
+ _memcpy
+ _objc_alloc
+ _objc_getProperty
+ _objc_msgSend$UTF8String
+ _objc_msgSend$appendBytes:length:
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$autoVacuumSetting
+ _objc_msgSend$bindData:column:
+ _objc_msgSend$bindDate:column:
+ _objc_msgSend$bindDouble:column:
+ _objc_msgSend$bindInt64:column:
+ _objc_msgSend$bindInt:column:
+ _objc_msgSend$bindNullAtColumn:
+ _objc_msgSend$bindString:column:
+ _objc_msgSend$blobAtColumn:
+ _objc_msgSend$bytes
+ _objc_msgSend$columnCount
+ _objc_msgSend$columnNameAtColumn:
+ _objc_msgSend$columnTypeAtColumn:
+ _objc_msgSend$copy
+ _objc_msgSend$data
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$dateAtColumn:
+ _objc_msgSend$dateWithTimeIntervalSinceReferenceDate:
+ _objc_msgSend$db
+ _objc_msgSend$dictionaryWithCapacity:
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$doubleAtColumn:
+ _objc_msgSend$enumerateColumnsUsingBlock:
+ _objc_msgSend$errorWithDomain:code:userInfo:
+ _objc_msgSend$executeSQL:
+ _objc_msgSend$executeSQL:arguments:
+ _objc_msgSend$executeSQLStmt:
+ _objc_msgSend$fileSystemRepresentation
+ _objc_msgSend$generateDone
+ _objc_msgSend$generateError:method:
+ _objc_msgSend$init
+ _objc_msgSend$initDatabaseWithURL:
+ _objc_msgSend$initWithFormat:arguments:
+ _objc_msgSend$initWithStatement:db:error:
+ _objc_msgSend$int64AtColumn:
+ _objc_msgSend$intAtColumn:
+ _objc_msgSend$isEqual:
+ _objc_msgSend$length
+ _objc_msgSend$log
+ _objc_msgSend$needReset
+ _objc_msgSend$null
+ _objc_msgSend$numberWithDouble:
+ _objc_msgSend$numberWithInt:
+ _objc_msgSend$numberWithLongLong:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$objectAtColumn:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$prepareStatement:error:
+ _objc_msgSend$reset
+ _objc_msgSend$setDb:
+ _objc_msgSend$setLog:
+ _objc_msgSend$setNeedReset:
+ _objc_msgSend$setObject:atIndexedSubscript:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$sharedSession
+ _objc_msgSend$stepWithError:
+ _objc_msgSend$steps:error:
+ _objc_msgSend$stmt
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$textAtColumn:
+ _objc_msgSend$timeIntervalSinceReferenceDate
+ _objc_msgSend$unsignedIntegerValue
+ _objc_release
+ _objc_release_x1
+ _objc_release_x27
+ _objc_release_x28
+ _objc_release_x8
+ _objc_retainAutorelease
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x12
+ _objc_retain_x19
+ _objc_retain_x23
+ _objc_retain_x24
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x27
+ _objc_retain_x28
+ _objc_setProperty_atomic
+ _objc_storeStrong
+ _objectdestroy.71Tm
+ _os_log_create
+ _sqlite3_bind_blob
+ _sqlite3_bind_double
+ _sqlite3_bind_int
+ _sqlite3_bind_int64
+ _sqlite3_bind_null
+ _sqlite3_bind_text
+ _sqlite3_clear_bindings
+ _sqlite3_close
+ _sqlite3_column_blob
+ _sqlite3_column_bytes
+ _sqlite3_column_count
+ _sqlite3_column_double
+ _sqlite3_column_int
+ _sqlite3_column_int64
+ _sqlite3_column_name
+ _sqlite3_column_text
+ _sqlite3_column_type
+ _sqlite3_errmsg
+ _sqlite3_exec
+ _sqlite3_finalize
+ _sqlite3_open_v2
+ _sqlite3_prepare_v2
+ _sqlite3_prepare_v3
+ _sqlite3_reset
+ _sqlite3_step
+ _swift_allocBox
+ _swift_arrayDestroy
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain_n
+ _swift_cvw_initEnumMetadataMultiPayloadWithLayoutString
+ _swift_cvw_multiPayloadEnumGeneric_destructiveInjectEnumTag
+ _swift_cvw_multiPayloadEnumGeneric_getEnumTag
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_deallocPartialClassInstance
+ _swift_dynamicCast
+ _swift_getEnumCaseMultiPayload
+ _swift_getForeignTypeMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTupleTypeMetadata2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_makeBoxUnique
+ _swift_projectBox
+ _swift_release_n
+ _swift_storeEnumTagMultiPayload
+ _swift_task_alloc
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_updateClassMetadata2
+ _symbolic $s10Foundation18_ErrorCodeProtocolP
+ _symbolic $s10Foundation21_BridgedStoredNSErrorP
+ _symbolic $s11SwiftCRLite22ValidateUpdateDelegateP
+ _symbolic $ss10SetAlgebraP
+ _symbolic $ss12CaseIterableP
+ _symbolic $ss25ExpressibleByArrayLiteralP
+ _symbolic $ss9OptionSetP
+ _symbolic SDy__________G 11SwiftCRLite13ValidDatabaseC0C8HashTypeO 10Foundation4DataV
+ _symbolic SS
+ _symbolic SSSg
+ _symbolic SS______t 11SwiftCRLite14ValidInfoFlagsV
+ _symbolic SaySSG
+ _symbolic SaySiG
+ _symbolic SaySiGSg
+ _symbolic Say_____G 10Foundation4DataV
+ _symbolic Say_____G 11SwiftCRLite14ValidInfoFlagsV
+ _symbolic Say_____G 11SwiftCRLite15ValidInfoFormatO
+ _symbolic Say_____G 11SwiftCRLite16ValidEnvironmentO
+ _symbolic Say_____G 11SwiftCRLite18ValidUpdateElementV
+ _symbolic Say_____G So17OS_dispatch_queueC8DispatchE10AttributesV
+ _symbolic Say_____G s5UInt8V
+ _symbolic Say_____G s6UInt32V
+ _symbolic Say_____GSg 10Foundation4DataV
+ _symbolic Say_____GSg 11SwiftCRLite18ValidUpdateElementV
+ _symbolic Say_____GSg s6UInt32V
+ _symbolic Sb
+ _symbolic SbSg
+ _symbolic Sd
+ _symbolic Sdz_Xx
+ _symbolic Si11fromVersion_t
+ _symbolic Si7version_t
+ _symbolic SiSg
+ _symbolic SnySiG
+ _symbolic So11ValidDBObjcCSg
+ _symbolic So11ValidDBStmtC
+ _symbolic So17OS_dispatch_queueC
+ _symbolic So7NSErrorC
+ _symbolic Su3key______5valuet 11SwiftCRLite05ValidA2DBC8SQLValueO
+ _symbolic Su______t 11SwiftCRLite05ValidA2DBC8SQLValueO
+ _symbolic _____ 10Foundation19PropertyListDecoderC
+ _symbolic _____ 10Foundation3URLV
+ _symbolic _____ 10Foundation4DataV
+ _symbolic _____ 10Foundation4DateV
+ _symbolic _____ 11SwiftCRLite05ValidA2DBC
+ _symbolic _____ 11SwiftCRLite05ValidA2DBC12SQLStatementC
+ _symbolic _____ 11SwiftCRLite05ValidA2DBC6SQLRowC
+ _symbolic _____ 11SwiftCRLite05ValidA2DBC8SQLValueO
+ _symbolic _____ 11SwiftCRLite05ValidA7DBErrorO
+ _symbolic _____ 11SwiftCRLite0B14FilterMetaDataV
+ _symbolic _____ 11SwiftCRLite0B14FilterMetaDataV10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLO
+ _symbolic _____ 11SwiftCRLite0B8MetaDataV
+ _symbolic _____ 11SwiftCRLite0B8MetaDataV10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLO
+ _symbolic _____ 11SwiftCRLite0aB5ErrorO
+ _symbolic _____ 11SwiftCRLite10ByteBufferV
+ _symbolic _____ 11SwiftCRLite11ParsingStepO
+ _symbolic _____ 11SwiftCRLite12ValidVersionO
+ _symbolic _____ 11SwiftCRLite13ValidDatabaseC
+ _symbolic _____ 11SwiftCRLite13ValidDatabaseC0C11GroupSearchV
+ _symbolic _____ 11SwiftCRLite13ValidDatabaseC0C11GroupSearchV10CodingKeys011_DB83DCB2C0K20B812CDB9A1B19594C35ELLO
+ _symbolic _____ 11SwiftCRLite13ValidDatabaseC0C5DatesV
+ _symbolic _____ 11SwiftCRLite13ValidDatabaseC0C5GroupV
+ _symbolic _____ 11SwiftCRLite13ValidDatabaseC0C5GroupV10CodingKeys011_DB83DCB2C0J20B812CDB9A1B19594C35ELLO
+ _symbolic _____ 11SwiftCRLite13ValidDatabaseC0C8HashTypeO
+ _symbolic _____ 11SwiftCRLite13ValidDatabaseC9AdminDataV
+ _symbolic _____ 11SwiftCRLite13ValidDatabaseC9AdminDataV10CodingKeysO
+ _symbolic _____ 11SwiftCRLite14ValidInfoFlagsV
+ _symbolic _____ 11SwiftCRLite15ByteBufferErrorO
+ _symbolic _____ 11SwiftCRLite15ValidDownloaderC
+ _symbolic _____ 11SwiftCRLite15ValidInfoFormatO
+ _symbolic _____ 11SwiftCRLite15ValidPatchApplyC
+ _symbolic _____ 11SwiftCRLite15ValidUpdateNTO1V
+ _symbolic _____ 11SwiftCRLite15ValidUpdateNTO1V10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLO
+ _symbolic _____ 11SwiftCRLite16ValidCertificateV
+ _symbolic _____ 11SwiftCRLite16ValidCertificateV10CodingKeys33_09663FE52D983112A60B038FA6E8E857LLO
+ _symbolic _____ 11SwiftCRLite16ValidEnvironmentO
+ _symbolic _____ 11SwiftCRLite16ValidUpdatePlistV
+ _symbolic _____ 11SwiftCRLite16ValidUpdatePlistV10CodingKeysO
+ _symbolic _____ 11SwiftCRLite17ValidUpdateParserC
+ _symbolic _____ 11SwiftCRLite18ValidUpdateElementV
+ _symbolic _____ 11SwiftCRLite18ValidUpdateElementV10CodingKeysO
+ _symbolic _____ 11SwiftCRLite28ValidDownloaderConfigurationV
+ _symbolic _____ 11SwiftCRLite9ValidInfoV
+ _symbolic _____ SC16ValidDBObjcErrorLeV
+ _symbolic _____ So16ValidDBObjcErrorV
+ _symbolic _____ s5Int32V
+ _symbolic _____ s5Int64V
+ _symbolic _____SbIeggd_ 11SwiftCRLite05ValidA2DBC6SQLRowC
+ _symbolic _____Sg 10Foundation3URLV
+ _symbolic _____Sg 10Foundation4DataV
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____Sg 11SwiftCRLite05ValidA2DBC8SQLValueO
+ _symbolic _____Sg 11SwiftCRLite13ValidDatabaseC0C11GroupSearchV
+ _symbolic _____Sg 11SwiftCRLite13ValidDatabaseC0C5DatesV
+ _symbolic _____Sg 11SwiftCRLite13ValidDatabaseC0C5GroupV
+ _symbolic _____Sg 11SwiftCRLite9ValidInfoV
+ _symbolic _____Sg So11SecTrustRefa
+ _symbolic _____Sg s5Int32V
+ _symbolic _____Sg s5Int64V
+ _symbolic _____Sg_ABt 10Foundation4DateV
+ _symbolic ___________t 11SwiftCRLite13ValidDatabaseC0C8HashTypeO 10Foundation4DataV
+ _symbolic ___________t s5Int32V 10Foundation4DataV
+ _symbolic ______p 10Foundation15ContiguousBytesP
+ _symbolic ______p So10ValidDBRowP
+ _symbolic ______p s5ErrorP
+ _symbolic ______pSg 10Foundation15ContiguousBytesP
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
+ _symbolic _____ySS_____G s18_DictionaryStorageC 11SwiftCRLite14ValidInfoFlagsV
+ _symbolic _____ySu_____G s18_DictionaryStorageC 11SwiftCRLite05ValidC2DBC8SQLValueO
+ _symbolic _____ySu______tG s23_ContiguousArrayStorageC 11SwiftCRLite05ValidD2DBC8SQLValueO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 11SwiftCRLite0E14FilterMetaDataV10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 11SwiftCRLite0E8MetaDataV10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 11SwiftCRLite13ValidDatabaseC0F11GroupSearchV10CodingKeys011_DB83DCB2C0N20B812CDB9A1B19594C35ELLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 11SwiftCRLite13ValidDatabaseC0F5GroupV10CodingKeys011_DB83DCB2C0M20B812CDB9A1B19594C35ELLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 11SwiftCRLite13ValidDatabaseC9AdminDataV10CodingKeysO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 11SwiftCRLite15ValidUpdateNTO1V10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 11SwiftCRLite16ValidCertificateV10CodingKeys33_09663FE52D983112A60B038FA6E8E857LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 11SwiftCRLite16ValidUpdatePlistV10CodingKeysO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 11SwiftCRLite18ValidUpdateElementV10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 11SwiftCRLite0E14FilterMetaDataV10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 11SwiftCRLite0E8MetaDataV10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 11SwiftCRLite13ValidDatabaseC0F11GroupSearchV10CodingKeys011_DB83DCB2C0N20B812CDB9A1B19594C35ELLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 11SwiftCRLite13ValidDatabaseC0F5GroupV10CodingKeys011_DB83DCB2C0M20B812CDB9A1B19594C35ELLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 11SwiftCRLite13ValidDatabaseC9AdminDataV10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 11SwiftCRLite15ValidUpdateNTO1V10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 11SwiftCRLite16ValidCertificateV10CodingKeys33_09663FE52D983112A60B038FA6E8E857LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 11SwiftCRLite16ValidUpdatePlistV10CodingKeysO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 11SwiftCRLite18ValidUpdateElementV10CodingKeysO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation4DataV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y__________G s18_DictionaryStorageC 11SwiftCRLite13ValidDatabaseC0E8HashTypeO 10Foundation4DataV
+ _symbolic _____y___________tG s23_ContiguousArrayStorageC 11SwiftCRLite13ValidDatabaseC0F8HashTypeO 10Foundation4DataV
+ _symbolic _____z_Xx 9CryptoKit6SHA256V
+ _type_layout_string 11SwiftCRLite0B14FilterMetaDataV
+ _type_layout_string 11SwiftCRLite0B8MetaDataV
+ _type_layout_string 11SwiftCRLite10ByteBufferV
+ _type_layout_string 11SwiftCRLite13ValidDatabaseC0C11GroupSearchV
+ _type_layout_string 11SwiftCRLite13ValidDatabaseC0C5DatesV
+ _type_layout_string 11SwiftCRLite13ValidDatabaseC0C5GroupV
+ _type_layout_string 11SwiftCRLite14ValidInfoFlagsV
+ _type_layout_string 11SwiftCRLite15ValidUpdateNTO1V
+ _type_layout_string 11SwiftCRLite16ValidCertificateV
+ _type_layout_string 11SwiftCRLite16ValidUpdatePlistV
+ _type_layout_string SC16ValidDBObjcErrorLeV
- _OBJC_CLASS_$_NSArray
- _associated conformance 11SwiftCRLite011SecInternalB5ErrorO10Foundation021_ObjectiveCBridgeableE0AAs0E0
- _associated conformance 11SwiftCRLite011SecInternalB5ErrorO10Foundation09LocalizedE0AAs0E0
- _associated conformance 11SwiftCRLite011SecInternalB5ErrorO10Foundation13CustomNSErrorAAs0E0
- _associated conformance 11SwiftCRLite011SecInternalB5ErrorO10Foundation15_BridgedNSErrorAA8RawValueSY_s17FixedWidthInteger
- _associated conformance 11SwiftCRLite011SecInternalB5ErrorO10Foundation15_BridgedNSErrorAASH
- _associated conformance 11SwiftCRLite011SecInternalB5ErrorO10Foundation15_BridgedNSErrorAASY
- _associated conformance 11SwiftCRLite011SecInternalB5ErrorO10Foundation15_BridgedNSErrorAaD021_ObjectiveCBridgeableE0
- _associated conformance 11SwiftCRLite011SecInternalB5ErrorOSHAASQ
- _objc_claimAutoreleasedReturnValue
- _swift_dynamicCastObjCClassUnconditional
- _symbolic _____ 11SwiftCRLite011SecInternalB5ErrorO
CStrings:
+ " is missing data "
+ " is missing flags "
+ " is missing format "
+ " is missing policies "
+ "#16@0:8"
+ "%@"
+ "%@: %s"
+ "1.2.12"
+ "1.2.840.113635.100.6.2.10"
+ "1.2.840.113635.100.6.51"
+ "@\"NSArray\"16@0:8"
+ "@\"NSData\"24@0:8Q16"
+ "@\"NSDate\"24@0:8Q16"
+ "@\"NSDictionary\""
+ "@\"NSDictionary\"16@0:8"
+ "@\"NSObject<OS_os_log>\""
+ "@\"NSString\"16@0:8"
+ "@\"NSString\"24@0:8Q16"
+ "@\"ValidDBObjc\""
+ "@24@0:8:16"
+ "@24@0:8@16"
+ "@24@0:8Q16"
+ "@24@0:8^@16"
+ "@28@0:8i16@20"
+ "@32@0:8:16@24"
+ "@32@0:8@16^@24"
+ "@40@0:8:16@24@32"
+ "@40@0:8@16@24^@32"
+ "ATTACH DATABASE ? AS source_db;\nINSERT INTO issuers              SELECT * FROM source_db.issuers;\nINSERT INTO serials              SELECT * FROM source_db.serials;\nINSERT INTO hashes               SELECT * FROM source_db.hashes;\nINSERT INTO dates                SELECT * FROM source_db.dates;\nINSERT INTO crlitefiltercoverage SELECT * FROM source_db.crlitefiltercoverage;\nINSERT INTO crlitefilters        SELECT * FROM source_db.crlitefilters;\nDEATTACH DATABASE source_db;"
+ "Apply have no issuer hash"
+ "B"
+ "B16@0:8"
+ "B16@?0@\"<ValidDBRow>\"8"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "B32@0:8@16*24"
+ "B32@0:8@?16^@24"
+ "CMS signature"
+ "CMS signature length"
+ "CMS verify failed"
+ "CREATE TABLE IF NOT EXISTS admin(\n    key TEXT PRIMARY KEY NOT NULL,\n    ival INTEGER NOT NULL,\n    value BLOB\n);\nCREATE TABLE IF NOT EXISTS issuers(\n   groupid INTEGER NOT NULL,\n   issuer_hash BLOB PRIMARY KEY NOT NULL\n);\nCREATE INDEX IF NOT EXISTS issuer_idx ON issuers(issuer_hash);\nCREATE TABLE IF NOT EXISTS groups(\n   groupid INTEGER PRIMARY KEY AUTOINCREMENT,\n   flags INTEGER,\n   format INTEGER,\n   data BLOB,\n   policies BLOB\n);\nCREATE TABLE IF NOT EXISTS serials(\n   groupid INTEGER NOT NULL,\n   serial BLOB NOT NULL,\n   UNIQUE(groupid,serial)\n);\nCREATE TABLE IF NOT EXISTS hashes(\n   groupid INTEGER NOT NULL,\n   sha256 BLOB NOT NULL,\n   UNIQUE(groupid,sha256)\n);\nCREATE TABLE IF NOT EXISTS dates(\n   groupid INTEGER PRIMARY KEY NOT NULL,\n   notbefore REAL,\n   notafter REAL\n);\nCREATE TABLE IF NOT EXISTS crlitefilters(\n   filterid INTEGER PRIMARY KEY NOT NULL,\n   filterversion INTEGER,\n   data BLOB\n);\nCREATE TABLE IF NOT EXISTS crlitefiltercoverage(\n   filterid INTEGER NOT NULL,\n   logid BLOB NOT NULL,\n   generatedat REAL,\n   start REAL,\n   end REAL,\n   UNIQUE(filterid,logid)\n);\nCREATE TRIGGER IF NOT EXISTS group_del \n   BEFORE DELETE ON groups FOR EACH ROW \n   BEGIN \n       DELETE FROM serials WHERE groupid=OLD.groupid; \n       DELETE FROM hashes WHERE groupid=OLD.groupid; \n       DELETE FROM issuers WHERE groupid=OLD.groupid; \n       DELETE FROM dates WHERE groupid=OLD.groupid; \n   END"
+ "CRLite data"
+ "CRLite data length"
+ "CRLite metadata"
+ "CRLite metadata length"
+ "Can't do delta update with a original database"
+ "DELETE FROM admin;"
+ "DELETE FROM crlitefiltercoverage;\nDELETE FROM crlitefilters;"
+ "DELETE FROM groups WHERE groupid = ?"
+ "DELETE FROM groups;\nDELETE FROM dates;\nDELETE FROM hashes;\nDELETE FROM serials;\nDELETE FROM issuers;"
+ "DELETE FROM hashes WHERE groupid=? AND sha256 = ?"
+ "DELETE FROM issuers WHERE groupid = ?"
+ "DELETE FROM serials WHERE groupid=? AND serial = ?"
+ "Database was closed"
+ "Date missing in database"
+ "Failed to get new GroupID "
+ "First patch is missing generation"
+ "First patch is missing version"
+ "Group has invalid NTO1 data"
+ "Hashes mismatch at index "
+ "Hashes missing from patch update"
+ "INSERT OR REPLACE INTO admin (key,ival,value) VALUES (?,?,?)"
+ "INSERT OR REPLACE INTO dates (groupid,notbefore,notafter) VALUES (?,?,?)"
+ "INSERT OR REPLACE INTO groups  (groupid,flags,format,data,policies) VALUES (?,?,?,?,?) RETURNING groupid"
+ "INSERT OR REPLACE INTO hashes (groupid,sha256) VALUES (?,?)"
+ "INSERT OR REPLACE INTO issuers (groupid,issuer_hash) VALUES (?,?)"
+ "INSERT OR REPLACE INTO serials (groupid,serial) VALUES (?,?)"
+ "NSObject"
+ "NTO1 patch failed"
+ "No such issuer hash: "
+ "No such serial rowid for "
+ "No such sha256 rowid for "
+ "Not full update, but previous hashes are missing"
+ "Number of hashes mismatch"
+ "PRAGMA auto_vacuum"
+ "Patch failed store group "
+ "Patch failed to patch group "
+ "Patch have no format "
+ "Pinning policy can't be created"
+ "Q16@0:8"
+ "Q24@0:8@\"NSString\"16"
+ "Q24@0:8@16"
+ "Row count invalid in "
+ "SELECT DISTINCT groupid FROM issuers ORDER BY issuer_hash ASC"
+ "SELECT DISTINCT groupid FROM issuers WHERE issuer_hash=?"
+ "SELECT count(*) FROM "
+ "SELECT data FROM crlitefilters ORDER by data ASC"
+ "SELECT flags,format,data,policies FROM groups WHERE groupid=?"
+ "SELECT issuer_hash FROM issuers WHERE groupid=? ORDER BY issuer_hash ASC"
+ "SELECT key, ival, value FROM admin"
+ "SELECT notbefore,notafter FROM dates WHERE groupid = ?"
+ "SELECT notbefore,notafter FROM dates WHERE groupid=?"
+ "SELECT rowid FROM hashes WHERE groupid=? AND sha256=?"
+ "SELECT rowid FROM serials WHERE groupid=? AND serial=?"
+ "SELECT serial FROM serials WHERE groupid=?"
+ "SELECT serial FROM serials WHERE groupid=? ORDER BY serial ASC"
+ "SELECT sha256 FROM hashes WHERE groupid=?"
+ "SELECT sha256 FROM hashes WHERE groupid=? ORDER BY sha256 ASC"
+ "SecTrustEvaluate failed with error: %d"
+ "SecTrustEvaluate not trusted: %u"
+ "T#,R"
+ "T@\"NSDictionary\",&,N,V_indexesByColumnName"
+ "T@\"NSObject<OS_os_log>\",&,V_log"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "T@\"ValidDBObjc\",&,V_db"
+ "TB,V_needReset"
+ "TQ,R"
+ "T^{sqlite3=},V_db"
+ "T^{sqlite3_stmt=},V_stmt"
+ "The data ended prematurely "
+ "UTF8String"
+ "Unexpected column type: %d"
+ "Unexpected end of file "
+ "VACUUM"
+ "ValidDBObjc"
+ "ValidDBObjcError"
+ "ValidDBRow"
+ "ValidDBStmt"
+ "ValidDBStmt prepare: %@"
+ "ValidUpdateParser"
+ "Vv16@0:8"
+ "^{_NSZone=}16@0:8"
+ "^{sqlite3=}"
+ "^{sqlite3=}16@0:8"
+ "^{sqlite3_stmt=}"
+ "^{sqlite3_stmt=}16@0:8"
+ "_TtC11SwiftCRLite12ValidSwiftDB"
+ "_TtC11SwiftCRLite13ValidDatabase"
+ "_TtC11SwiftCRLite15ValidDownloader"
+ "_TtC11SwiftCRLite15ValidPatchApply"
+ "_TtC11SwiftCRLite17ValidUpdateParser"
+ "_TtCC11SwiftCRLite12ValidSwiftDB12SQLStatement"
+ "_TtCC11SwiftCRLite12ValidSwiftDB6SQLRow"
+ "_db"
+ "_indexesByColumnName"
+ "_log"
+ "_needReset"
+ "_stmt"
+ "add"
+ "allObjects"
+ "allObjectsByColumnName"
+ "appendBytes:length:"
+ "arrayWithCapacity:"
+ "autoVacuumSetting"
+ "autorelease"
+ "bindData:column:"
+ "bindDate:column:"
+ "bindDouble:column:"
+ "bindInt64:column:"
+ "bindInt:column:"
+ "bindNullAtColumn:"
+ "bindString:column:"
+ "blobAtColumn:"
+ "bytes"
+ "can't build download URL"
+ "carry-prod"
+ "carry-uat"
+ "check-again"
+ "check-ocsp"
+ "check_again"
+ "class"
+ "clearBindings"
+ "close"
+ "columnCount"
+ "columnNameAtColumn:"
+ "columnTypeAtColumn:"
+ "com.apple.ValidSwiftDBError"
+ "complete"
+ "conformsToProtocol:"
+ "copy"
+ "d24@0:8Q16"
+ "data"
+ "dataWithBytes:length:"
+ "database"
+ "dateAtColumn:"
+ "dateWithTimeIntervalSinceReferenceDate:"
+ "db"
+ "db_format"
+ "db_hash"
+ "db_source"
+ "db_version"
+ "debugDescription"
+ "decoder"
+ "delete"
+ "description"
+ "dictionaryWithCapacity:"
+ "dictionaryWithObjects:forKeys:count:"
+ "doubleAtColumn:"
+ "enumerateColumnsUsingBlock:"
+ "environment"
+ "errorWithDomain:code:userInfo:"
+ "executeSQL:"
+ "executeSQL:arguments:"
+ "executeSQLStmt:"
+ "fileSystemRepresentation"
+ "filter count"
+ "filter data"
+ "filter data length"
+ "filter metadata"
+ "filter metadata length"
+ "firstUpdate"
+ "format"
+ "full"
+ "fullCRLiteUpdate"
+ "generateDone"
+ "generateError:method:"
+ "generation"
+ "hash"
+ "hashes"
+ "i16@0:8"
+ "i24@0:8Q16"
+ "ignoring key %s in admin table"
+ "indexForColumnName:"
+ "indexesByColumnName"
+ "initDatabaseWithURL:"
+ "initWithFormat:arguments:"
+ "initWithStatement:db:error:"
+ "int64AtColumn:"
+ "intAtColumn:"
+ "interval"
+ "isEqual:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "issuer-hash"
+ "issuer-id"
+ "known-intermediates-only"
+ "knownIntermediatesOnly"
+ "length"
+ "log"
+ "needReset"
+ "no date for group %d"
+ "no serial number on certifiate"
+ "no-ca"
+ "no-ca-v2"
+ "not-after"
+ "not-before"
+ "nto1 applier here"
+ "null"
+ "numberWithDouble:"
+ "numberWithInt:"
+ "numberWithLongLong:"
+ "numberWithUnsignedInteger:"
+ "objectAtColumn:"
+ "objectForKeyedSubscript:"
+ "overridable"
+ "params"
+ "patchDatabase"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "plist count"
+ "plist data"
+ "plist length"
+ "policies"
+ "policy for group is invalid %d"
+ "policyConstraints"
+ "pragma auto_vacuum = incremental"
+ "pragma journal_mode = WAL"
+ "prepareStatement:error:"
+ "previous-hash"
+ "processed group: %d"
+ "processed serial: delete: %ld, add: %ld"
+ "processed sha256: delete: %ld, add: %ld"
+ "prod"
+ "q24@0:8Q16"
+ "q48@0:8^{__SecCertificate=}16^{__SecCertificate=}24@32^@40"
+ "qa"
+ "qa-carry"
+ "queue"
+ "release"
+ "require-ct"
+ "reset"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "row"
+ "seed"
+ "self"
+ "setDb:"
+ "setIndexesByColumnName:"
+ "setLog:"
+ "setNeedReset:"
+ "setObject:atIndexedSubscript:"
+ "setObject:forKeyedSubscript:"
+ "setStmt:"
+ "sharedSession"
+ "signed data"
+ "signed data length"
+ "sqlite3_bind_blob: %d"
+ "sqlite3_bind_double: %d"
+ "sqlite3_bind_int64: %d"
+ "sqlite3_bind_int: %d"
+ "sqlite3_bind_text: %d"
+ "sqlite3_exec: %s[%d]"
+ "sqlite3_prepare_v2: %s[%d]"
+ "sqlite3_step: %s[%d]"
+ "sqliteCode"
+ "step"
+ "stepWithError %d error: %@"
+ "stepWithError:"
+ "steps"
+ "steps: %@"
+ "steps:error:"
+ "stmt"
+ "stringWithFormat:"
+ "stringWithUTF8String:"
+ "superclass"
+ "textAtColumn:"
+ "timeIntervalSinceReferenceDate"
+ "uat"
+ "unsignedIntegerValue"
+ "update"
+ "v20@0:8B16"
+ "v24@0:8@16"
+ "v24@0:8@?16"
+ "v24@0:8Q16"
+ "v24@0:8^{sqlite3=}16"
+ "v24@0:8^{sqlite3_stmt=}16"
+ "v24@?0Q8@\"NSString\"16"
+ "v28@0:8i16Q20"
+ "v32@0:8@16Q24"
+ "v32@0:8d16Q24"
+ "v32@0:8q16Q24"
+ "v8@?0"
+ "valid"
+ "valid-qa.apple.com"
+ "valid-qa.apple.com/carry"
+ "valid-uat.apple.com"
+ "valid-uat.apple.com/carry"
+ "valid.apple.com/carry"
+ "valid.apple.com/seed"
+ "version"
+ "xor"
+ "zone"
- "B48@0:8^{__SecCertificate=}16^{__SecCertificate=}24r^{__CFArray=}32^@40"
- "SwiftCRLite.SecInternalCRLiteError"
- "i48@0:8^{__SecCertificate=}16^{__SecCertificate=}24r^{__CFArray=}32^@40"
- "isCertCovered:issuerCert:scts:error:"
- "scts was not an array of Data"

```
