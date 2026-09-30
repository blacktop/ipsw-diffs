## AppStoreUtilities

> `/System/Library/PrivateFrameworks/AppStoreUtilities.framework/Versions/A/AppStoreUtilities`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_imageinfo`
- `__AUTH_CONST.__objc_intobj`

```diff

-13.0.40.0.0
-  __TEXT.__text: 0x10fac
-  __TEXT.__objc_methlist: 0x1484
-  __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x8cf
-  __TEXT.__gcc_except_tab: 0x37c
+13.0.43.0.0
+  __TEXT.__text: 0x13b24
+  __TEXT.__objc_methlist: 0x14fc
+  __TEXT.__const: 0x430
+  __TEXT.__swift5_typeref: 0x23c
+  __TEXT.__swift5_capture: 0x68
+  __TEXT.__cstring: 0x924
+  __TEXT.__swift5_fieldmd: 0x2c
+  __TEXT.__constg_swiftt: 0x7c
+  __TEXT.__swift5_reflstr: 0x22
+  __TEXT.__swift5_assocty: 0x48
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift5_proto: 0x28
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__swift_as_entry: 0x8
+  __TEXT.__swift_as_ret: 0x8
+  __TEXT.__swift_as_cont: 0x10
+  __TEXT.__gcc_except_tab: 0x394
   __TEXT.__oslogstring: 0x798
-  __TEXT.__unwind_info: 0x678
+  __TEXT.__unwind_info: 0x780
+  __TEXT.__eh_frame: 0x160
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xe8
-  __DATA_CONST.__objc_classlist: 0xe0
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__const: 0x120
+  __DATA_CONST.__objc_classlist: 0xe8
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb30
-  __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xc0
-  __DATA_CONST.__got: 0x1e0
-  __AUTH_CONST.__const: 0x950
-  __AUTH_CONST.__cfstring: 0xc40
-  __AUTH_CONST.__objc_const: 0x2328
+  __DATA_CONST.__objc_selrefs: 0xb68
+  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_superrefs: 0xc8
+  __DATA_CONST.__got: 0x228
+  __AUTH_CONST.__const: 0xac0
+  __AUTH_CONST.__cfstring: 0xc20
+  __AUTH_CONST.__objc_const: 0x2488
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH_CONST.__auth_got: 0x3b8
-  __AUTH.__objc_data: 0x8c0
-  __DATA.__objc_ivar: 0x120
-  __DATA.__data: 0x2a0
-  __DATA.__bss: 0x18
+  __AUTH_CONST.__auth_got: 0x548
+  __AUTH.__objc_data: 0x910
+  __DATA.__objc_ivar: 0x130
+  __DATA.__data: 0x330
+  __DATA.__bss: 0x4a0
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 495
-  Symbols:   1302
-  CStrings:  171
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  Functions: 581
+  Symbols:   1432
+  CStrings:  172
 
Symbols:
+ +[ASUDefaultsManager databaseEncryptionKeyWithIdentifier:domain:]
+ +[ASUDefaultsManager setDatabaseEncryptionKey:withIdentifier:domain:]
+ -[ASUSQLiteDatabase transactionQueue]
+ -[ASUSQLiteDatabaseStore modifyUsingTransactionClass:withBlock:]
+ -[ASUSQLiteEncryptionKeyIdentifier .cxx_destruct]
+ -[ASUSQLiteEncryptionKeyIdentifier _keychainAccount]
+ -[ASUSQLiteEncryptionKeyIdentifier domain]
+ -[ASUSQLiteEncryptionKeyIdentifier identifier]
+ -[ASUSQLiteEncryptionKeyIdentifier initWithPrefix:identifier:domain:]
+ -[ASUSQLiteEncryptionKeyIdentifier prefix]
+ -[ASUSQLiteEntity(ASUSQLiteTypeChecking) boolValueForProperty:]
+ -[ASUSQLiteEntity(ASUSQLiteTypeChecking) dictValueForProperty:]
+ -[ASUSQLiteEntity(ASUSQLiteTypeChecking) errorValueForProperty:]
+ -[ASUSQLiteEntity(ASUSQLiteTypeChecking) integerValueForProperty:]
+ -[ASUSQLiteEntity(ASUSQLiteTypeChecking) numberValueForProperty:]
+ -[ASUSQLiteEntity(ASUSQLiteTypeChecking) stringValueForProperty:]
+ -[ASUSQLiteEntity(ASUSQLiteTypeChecking) urlValueForProperty:]
+ -[ASUSQLiteEntity(ASUSQLiteTypeChecking) uuidValueForProperty:]
+ -[ASUSQLiteMemoryEntity(ASUSQLiteTypeChecking) arrayValueForProperty:]
+ -[ASUSQLiteMemoryEntity(ASUSQLiteTypeChecking) boolValueForProperty:]
+ -[ASUSQLiteMemoryEntity(ASUSQLiteTypeChecking) dateValueForProperty:]
+ -[ASUSQLiteMemoryEntity(ASUSQLiteTypeChecking) dictValueForProperty:]
+ -[ASUSQLiteMemoryEntity(ASUSQLiteTypeChecking) integerValueForProperty:]
+ -[ASUSQLiteMemoryEntity(ASUSQLiteTypeChecking) numberValueForProperty:]
+ -[ASUSQLiteMemoryEntity(ASUSQLiteTypeChecking) stringValueForProperty:]
+ -[ASUSQLiteMemoryEntity(ASUSQLiteTypeChecking) urlValueForProperty:]
+ -[ASUSQLiteMemoryEntity(ASUSQLiteTypeChecking) uuidValueForProperty:]
+ -[ASUSQLiteQuery allMemoryEntitiesWithProperties:]
+ -[ASUSQLiteQuery firstMemoryEntityWithProperties:]
+ GCC_except_table25
+ GCC_except_table53
+ GCC_except_table55
+ GCC_except_table58
+ GCC_except_table70
+ OBJC_IVAR_$_ASUSQLiteConnection._afterTransactionQueue
+ OBJC_IVAR_$_ASUSQLiteEncryptionKeyIdentifier._domain
+ OBJC_IVAR_$_ASUSQLiteEncryptionKeyIdentifier._identifier
+ OBJC_IVAR_$_ASUSQLiteEncryptionKeyIdentifier._prefix
+ _ASUSQLiteConfigLookaside
+ _OBJC_CLASS_$_ASUSQLiteEncryptionKeyIdentifier
+ _OBJC_METACLASS_$_ASUSQLiteEncryptionKeyIdentifier
+ __Block_copy
+ __Block_release
+ __OBJC_$_CLASS_METHODS_ASUSQLiteEntity(ASUSQLiteMemoryEntity|ASUSQLiteTypeChecking|ASUSQLiteQuery)
+ __OBJC_$_CLASS_METHODS_ASUSQLiteMemoryEntity(ASUSQLiteTypeChecking|ASUSQLiteQuery)
+ __OBJC_$_INSTANCE_METHODS_ASUSQLiteEncryptionKeyIdentifier
+ __OBJC_$_INSTANCE_METHODS_ASUSQLiteEntity(ASUSQLiteMemoryEntity|ASUSQLiteTypeChecking|ASUSQLiteQuery)
+ __OBJC_$_INSTANCE_METHODS_ASUSQLiteMemoryEntity(ASUSQLiteTypeChecking|ASUSQLiteQuery)
+ __OBJC_$_INSTANCE_VARIABLES_ASUSQLiteEncryptionKeyIdentifier
+ __OBJC_$_PROP_LIST_ASUSQLiteEncryptionKeyIdentifier
+ __OBJC_CLASS_RO_$_ASUSQLiteEncryptionKeyIdentifier
+ __OBJC_METACLASS_RO_$_ASUSQLiteEncryptionKeyIdentifier
+ ___50-[ASUSQLiteQuery allMemoryEntitiesWithProperties:]_block_invoke
+ ___50-[ASUSQLiteQuery firstMemoryEntityWithProperties:]_block_invoke
+ ___block_descriptor_40_e8_32s_e38_v32?0"ASUSQLiteMemoryEntity"8Q16^B24l
+ ___block_descriptor_64_e8_32s40s48bs56r_e41_v32?0"ASUSQLiteCursor"8"NSError"16^B24l
+ ___copy_helper_block_e8_32s40s48b56r
+ ___destroy_helper_block_e8_32s40s48s56r
+ ___swift_allocate_boxed_opaque_existential_0
+ ___swift_async_cont_functlets
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructorTm
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_project_boxed_opaque_existential_0
+ ___swift_reflection_version
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_AppStoreUtilities
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_AppStoreUtilities
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_AppStoreUtilities
+ __swift_FORCE_LOAD_$_swiftIOKit
+ __swift_FORCE_LOAD_$_swiftIOKit_$_AppStoreUtilities
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_AppStoreUtilities
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_AppStoreUtilities
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_AppStoreUtilities
+ __swift_closure_destructor
+ _associated conformance SC18ASUSQLiteErrorCodeLeV10Foundation021_ObjectiveCBridgeableB0SCs0B0
+ _associated conformance SC18ASUSQLiteErrorCodeLeV10Foundation13CustomNSErrorSCs0B0
+ _associated conformance SC18ASUSQLiteErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0C0AcDP_8RawValueSYs17FixedWidthInteger
+ _associated conformance SC18ASUSQLiteErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0C0AcDP_AC01_bC8Protocol
+ _associated conformance SC18ASUSQLiteErrorCodeLeV10Foundation21_BridgedStoredNSErrorSC0C0AcDP_SY
+ _associated conformance SC18ASUSQLiteErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC021_ObjectiveCBridgeableB0
+ _associated conformance SC18ASUSQLiteErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCAC06CustomG0
+ _associated conformance SC18ASUSQLiteErrorCodeLeV10Foundation21_BridgedStoredNSErrorSCSH
+ _associated conformance SC18ASUSQLiteErrorCodeLeVSHSCSQ
+ _associated conformance So18ASUSQLiteErrorCodeV10Foundation01_bC8ProtocolSC01_B4TypeAcDP_AC21_BridgedStoredNSError
+ _associated conformance So18ASUSQLiteErrorCodeV10Foundation01_bC8ProtocolSCSQ
+ _block_copy_helper
+ _block_descriptor
+ _block_destroy_helper
+ _flat unique So24ASUSQLiteDatabaseSession_p
+ _flat unique So28ASUSQLiteDatabaseTransaction_p
+ _objc_msgSend$asyncModifyUsingTransaction:completion:
+ _objc_msgSend$asyncReadUsingSession:completion:
+ _objc_msgSend$domain
+ _objc_msgSend$firstObject
+ _objc_msgSend$identifier
+ _objc_msgSend$modifyStore:usingTransactionClass:withBlock:
+ _objc_msgSend$subarrayWithRange:
+ _sqlite3_config
+ _swift_allocBox
+ _swift_allocObject
+ _swift_beginAccess
+ _swift_bridgeObjectRetain
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_deallocObject
+ _swift_getEnumCaseMultiPayload
+ _swift_getForeignTypeMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_projectBox
+ _swift_release
+ _swift_retain
+ _swift_storeEnumTagMultiPayload
+ _swift_task_alloc
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_willThrow
+ _swift_willThrowTypedImpl
+ _symbolic $s10Foundation18_ErrorCodeProtocolP
+ _symbolic $s10Foundation21_BridgedStoredNSErrorP
+ _symbolic $s17AppStoreUtilities018_ASUSQLiteDatabaseB8ProtocolP
+ _symbolic $sSY
+ _symbolic B0
+ _symbolic B1
+ _symbolic B2
+ _symbolic B3
+ _symbolic ScCyypSg_____G s5NeverO
+ _symbolic ScCyyt_____G s5NeverO
+ _symbolic Si
+ _symbolic So7NSErrorC
+ _symbolic _____ SC18ASUSQLiteErrorCodeLeV
+ _symbolic _____ So18ASUSQLiteErrorCodeV
+ _symbolic ______p s5ErrorP
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic _____yqd________pGSgz_x_qd__qd_0_qd_1_So22ASUSQLiteDatabaseStoreCyqd_0_qd_1_GRbz_____Rd_0______Rd_1_r_1_lXX s6ResultOsRi_zRi0_zrlE s5ErrorP So24ASUSQLiteDatabaseSessionP So0cD11TransactionP
+ _symbolic qd_0_
+ _symbolic qd_0_qd________pIeggrzo_ s5ErrorP
+ _symbolic qd_1_
+ _symbolic qd_1_qd________pIeggrzo_ s5ErrorP
+ _symbolic qd__
+ _symbolic x
+ _symbolic ypSg
+ _type_layout_string SC18ASUSQLiteErrorCodeLeV
+ block_copy_helper
+ block_descriptor
+ block_destroy_helper
- +[ASUDefaultsManager databaseEncryptionKeyWithIdentifier:]
- +[ASUDefaultsManager setDatabaseEncryptionKey:withIdentifier:]
- -[ASUSQLiteEntity(SQLiteTypeChecking) boolValueForProperty:]
- -[ASUSQLiteEntity(SQLiteTypeChecking) dictValueForProperty:]
- -[ASUSQLiteEntity(SQLiteTypeChecking) errorValueForProperty:]
- -[ASUSQLiteEntity(SQLiteTypeChecking) integerValueForProperty:]
- -[ASUSQLiteEntity(SQLiteTypeChecking) numberValueForProperty:]
- -[ASUSQLiteEntity(SQLiteTypeChecking) stringValueForProperty:]
- -[ASUSQLiteEntity(SQLiteTypeChecking) urlValueForProperty:]
- -[ASUSQLiteEntity(SQLiteTypeChecking) uuidValueForProperty:]
- -[ASUSQLiteMemoryEntity(SQLiteTypeChecking) arrayValueForProperty:]
- -[ASUSQLiteMemoryEntity(SQLiteTypeChecking) boolValueForProperty:]
- -[ASUSQLiteMemoryEntity(SQLiteTypeChecking) dateValueForProperty:]
- -[ASUSQLiteMemoryEntity(SQLiteTypeChecking) dictValueForProperty:]
- -[ASUSQLiteMemoryEntity(SQLiteTypeChecking) integerValueForProperty:]
- -[ASUSQLiteMemoryEntity(SQLiteTypeChecking) numberValueForProperty:]
- -[ASUSQLiteMemoryEntity(SQLiteTypeChecking) stringValueForProperty:]
- -[ASUSQLiteMemoryEntity(SQLiteTypeChecking) urlValueForProperty:]
- -[ASUSQLiteMemoryEntity(SQLiteTypeChecking) uuidValueForProperty:]
- GCC_except_table45
- GCC_except_table49
- GCC_except_table52
- GCC_except_table64
- __OBJC_$_CLASS_METHODS_ASUSQLiteEntity(ASUSQLiteMemoryEntity|SQLiteTypeChecking|ASUSQLiteQuery)
- __OBJC_$_CLASS_METHODS_ASUSQLiteMemoryEntity(SQLiteTypeChecking|ASUSQLiteQuery)
- __OBJC_$_INSTANCE_METHODS_ASUSQLiteEntity(ASUSQLiteMemoryEntity|SQLiteTypeChecking|ASUSQLiteQuery)
- __OBJC_$_INSTANCE_METHODS_ASUSQLiteMemoryEntity(SQLiteTypeChecking|ASUSQLiteQuery)
- ___block_descriptor_64_e8_32s40bs48r_e41_v32?0"ASUSQLiteCursor"8"NSError"16^B24l
- _objc_msgSend$appendFormat:
- _objc_msgSend$componentsJoinedByString:
- _objc_msgSend$dictionaryWithCapacity:
CStrings:
+ "_createCheckedContinuation(_:)"
+ "com.apple.appstored.ASUSQLiteConnection.AfterTransactionBlocks"
- " FROM %@"
```
