## PrivacyAccounting

> `/System/Library/PrivateFrameworks/PrivacyAccounting.framework/PrivacyAccounting`

```diff

-134.0.0.0.0
-  __TEXT.__text: 0x14e7c
-  __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__objc_methlist: 0x1ae0
-  __TEXT.__const: 0xf0
-  __TEXT.__cstring: 0xfd6
+137.0.0.0.0
+  __TEXT.__text: 0x20390
+  __TEXT.__auth_stubs: 0xe30
+  __TEXT.__objc_methlist: 0x1c54
+  __TEXT.__const: 0x574
+  __TEXT.__cstring: 0x1287
   __TEXT.__oslogstring: 0x93f
-  __TEXT.__gcc_except_tab: 0x46c
-  __TEXT.__unwind_info: 0x8a4
-  __TEXT.__objc_classname: 0x68b
-  __TEXT.__objc_methname: 0x334b
-  __TEXT.__objc_methtype: 0xb9d
-  __TEXT.__objc_stubs: 0x27a0
-  __DATA_CONST.__got: 0xa0
-  __DATA_CONST.__const: 0x7d8
-  __DATA_CONST.__objc_classlist: 0x158
+  __TEXT.__gcc_except_tab: 0x4b4
+  __TEXT.__constg_swiftt: 0x230
+  __TEXT.__swift5_typeref: 0x219
+  __TEXT.__swift5_fieldmd: 0x13c
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_reflstr: 0xbd
+  __TEXT.__swift5_assocty: 0x68
+  __TEXT.__swift5_proto: 0x30
+  __TEXT.__swift5_types: 0x24
+  __TEXT.__swift5_capture: 0x10
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__unwind_info: 0xabc
+  __TEXT.__eh_frame: 0x200
+  __TEXT.__objc_classname: 0x6b6
+  __TEXT.__objc_methname: 0x360b
+  __TEXT.__objc_methtype: 0xc65
+  __TEXT.__objc_stubs: 0x2900
+  __DATA_CONST.__got: 0xf8
+  __DATA_CONST.__const: 0x880
+  __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0xa8
+  __DATA_CONST.__objc_protolist: 0xd8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5678
-  __DATA_CONST.__objc_selrefs: 0xc60
-  __AUTH_CONST.__objc_const: 0x1128
-  __AUTH_CONST.__cfstring: 0xda0
-  __AUTH_CONST.__const: 0x320
+  __DATA_CONST.__objc_const: 0x3980
+  __DATA_CONST.__objc_selrefs: 0xd18
+  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_classrefs: 0x220
+  __DATA_CONST.__objc_superrefs: 0x140
+  __AUTH_CONST.__objc_const: 0x1170
+  __AUTH_CONST.__cfstring: 0xde0
+  __AUTH_CONST.__const: 0x690
   __AUTH_CONST.__objc_intobj: 0x78
-  __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__auth_got: 0x400
-  __AUTH.__objc_data: 0x780
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0x218
-  __DATA.__objc_superrefs: 0x140
-  __DATA.__objc_ivar: 0x208
-  __DATA.__data: 0x808
-  __DATA.__bss: 0x10
+  __AUTH_CONST.__auth_ptr: 0x10
+  __AUTH_CONST.__auth_got: 0x728
+  __AUTH.__objc_data: 0x938
+  __AUTH.__data: 0x180
+  __DATA.__objc_ivar: 0x218
+  __DATA.__data: 0xa90
+  __DATA.__bss: 0x5a8
   __DATA_DIRTY.__objc_data: 0x5f0
   __DATA_DIRTY.__bss: 0xb8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 671
-  Symbols:   2638
-  CStrings:  1006
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  Functions: 871
+  Symbols:   2782
+  CStrings:  1074
 
Symbols:
+ -[PAAccess accessCount]
+ -[PAAccess initWithAccessor:identifier:kind:assetIdentifiers:visibilityState:accessEventCount:accessCount:]
+ -[PAAccess setAccessCount:]
+ -[PAAccessInterval endWithTimestampAdjustment:accessCount:]
+ -[PAAccessLogger endIntervalWithSlot:timestampAdjustment:accessCount:]
+ -[PAAccessLogger endIntervalWithSlot:timestampAdjustment:accessCount:].cold.1
+ -[PAAccessReader(PAAccessEventRecords) accessRecordsForReportFrom:to:error:]
+ -[PACoalescingIntervalState accessCount]
+ -[PACoalescingIntervalState clock]
+ -[PACoalescingIntervalState initWithInterval:intervalExpirationTime:expiryQueue:clock:onExpiration:]
+ -[PACoalescingIntervalState initWithInterval:intervalExpirationTime:expiryQueue:clock:onExpiration:expiry:]
+ -[PACoalescingIntervalState initWithInterval:matcher:tracker:expiry:]
+ -[PACoalescingIntervalState intervalEndTime]
+ -[PACoalescingIntervalState setAccessCount:]
+ -[PACoalescingIntervalState setClock:]
+ -[PACoalescingIntervalState setIntervalEndTime:]
+ -[PAPBAccess accessCount]
+ -[PAPBAccess hasAccessCount]
+ -[PAPBAccess setAccessCount:]
+ -[PAPBAccess setHasAccessCount:]
+ GCC_except_table13
+ GCC_except_table18
+ GCC_except_table21
+ GCC_except_table24
+ OBJC_IVAR_$_PAPBAccess._accessCount
+ _MGGetBoolAnswer
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$__TtC17PrivacyAccounting12InitialSwift
+ _OBJC_IVAR_$_PAAccess._accessCount
+ _OBJC_IVAR_$_PAAccessInterval._accessCount
+ _OBJC_IVAR_$_PACoalescingIntervalState._accessCount
+ _OBJC_IVAR_$_PACoalescingIntervalState._clock
+ _OBJC_IVAR_$_PACoalescingIntervalState._intervalEndTime
+ _OBJC_IVAR_$_PACoalescingIntervalState._startTimes
+ _OBJC_METACLASS_$__TtC17PrivacyAccounting12InitialSwift
+ _OBJC_METACLASS_$__TtCFE17PrivacyAccountingCSo14PAAccessReader23_accessRecordsForReportFzT4fromV10Foundation4Date2toS2__CSo12NSEnumeratorL_18AccessRecordObject
+ __Block_copy
+ __Block_release
+ __DATA__TtC17PrivacyAccounting12InitialSwift
+ __DATA__TtCFE17PrivacyAccountingCSo14PAAccessReader23_accessRecordsForReportFzT4fromV10Foundation4Date2toS2__CSo12NSEnumeratorL_18AccessRecordObject
+ __IVARS__TtCFE17PrivacyAccountingCSo14PAAccessReader23_accessRecordsForReportFzT4fromV10Foundation4Date2toS2__CSo12NSEnumeratorL_18AccessRecordObject
+ __METACLASS_DATA__TtC17PrivacyAccounting12InitialSwift
+ __METACLASS_DATA__TtCFE17PrivacyAccountingCSo14PAAccessReader23_accessRecordsForReportFzT4fromV10Foundation4Date2toS2__CSo12NSEnumeratorL_18AccessRecordObject
+ __OBJC_$_CLASS_METHODS_PAAccessReader(PAAccessEventRecords|PrivacyAccounting)
+ __OBJC_$_CLASS_METHODS__TtC17PrivacyAccounting12InitialSwift
+ __OBJC_$_INSTANCE_METHODS_PAAccessReader(PAAccessEventRecords|PrivacyAccounting)
+ __OBJC_$_INSTANCE_METHODS__TtC17PrivacyAccounting12InitialSwift
+ __OBJC_$_INSTANCE_METHODS__TtCFE17PrivacyAccountingCSo14PAAccessReader23_accessRecordsForReportFzT4fromV10Foundation4Date2toS2__CSo12NSEnumeratorL_18AccessRecordObject
+ __OBJC_$_PROP_LIST_PAAccessEventRecord
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_PAAccessEventRecord
+ __OBJC_$_PROTOCOL_METHOD_TYPES_PAAccessEventRecord
+ __OBJC_$_PROTOCOL_REFS_PAAccessEventRecord
+ __OBJC_LABEL_PROTOCOL_$_PAAccessEventRecord
+ __OBJC_PROTOCOL_$_PAAccessEventRecord
+ __PROPERTIES__TtCFE17PrivacyAccountingCSo14PAAccessReader23_accessRecordsForReportFzT4fromV10Foundation4Date2toS2__CSo12NSEnumeratorL_18AccessRecordObject
+ __PROTOCOLS__TtCFE17PrivacyAccountingCSo14PAAccessReader23_accessRecordsForReportFzT4fromV10Foundation4Date2toS2__CSo12NSEnumeratorL_18AccessRecordObject
+ __PROTOCOLS__TtCFE17PrivacyAccountingCSo14PAAccessReader23_accessRecordsForReportFzT4fromV10Foundation4Date2toS2__CSo12NSEnumeratorL_18AccessRecordObject.4
+ ___107-[PACoalescingIntervalState initWithInterval:intervalExpirationTime:expiryQueue:clock:onExpiration:expiry:]_block_invoke
+ ___69-[PACoalescingIntervalState initWithInterval:matcher:tracker:expiry:]_block_invoke
+ ___69-[PACoalescingIntervalState initWithInterval:matcher:tracker:expiry:]_block_invoke_2
+ ___70-[PAAccessLogger endIntervalWithSlot:timestampAdjustment:accessCount:]_block_invoke
+ ___77-[PAAccessReader initWithConnection:queue:enablementChangedNotificationName:]_block_invoke.112
+ ___block_descriptor_32_e16_{PATimes=QQ}8?0l
+ ___block_descriptor_48_e8_32bs40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32s40w48w_e5_v8?0lw40l8w48l8s32l8
+ ___block_literal_global.110
+ ___block_literal_global.126
+ ___block_literal_global.131
+ ___block_literal_global.210
+ ___block_literal_global.239
+ ___block_literal_global.248
+ ___block_literal_global.91
+ ___block_literal_global.94
+ ___isGreenTeaSKU_block_invoke
+ ___swift_allocate_boxed_opaque_existential_1
+ ___swift_assign_boxed_opaque_existential_1
+ ___swift_destroy_boxed_opaque_existential_1
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_instantiateConcreteTypeFromMangledNameAbstract
+ ___swift_instantiateGenericMetadata
+ ___swift_memcpy16_8
+ ___swift_memcpy40_8
+ ___swift_mutable_project_boxed_opaque_existential_1
+ ___swift_reflection_version
+ ___unnamed_3
+ ___unnamed_5
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_PrivacyAccounting
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_PrivacyAccounting
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_PrivacyAccounting
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_PrivacyAccounting
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_PrivacyAccounting
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_PrivacyAccounting
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_PrivacyAccounting
+ __swift_stdlib_malloc_size
+ __swift_stdlib_reportUnimplementedInitializer
+ _associated conformance 17PrivacyAccounting12AccessRecordV10AccessorIDOSHAASQ
+ _associated conformance 17PrivacyAccounting13AccessHistoryVyxGSTAA8IteratorST_St
+ _associated conformance So16PAAccessCategoryaSHSCSQ
+ _associated conformance So16PAAccessCategoryas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So16PAAccessCategoryas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _block_copy_helper
+ _block_copy_helper.11
+ _block_descriptor
+ _block_descriptor.13
+ _block_destroy_helper
+ _block_destroy_helper.12
+ _flat unique St_px7ElementStRts_XP
+ _isGreenTeaSKU.deviceIsChinaSKU
+ _isGreenTeaSKU.once
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_msgSend$_accessRecordsForReportFrom:to:error:
+ _objc_msgSend$accessCount
+ _objc_msgSend$clock
+ _objc_msgSend$components:fromDate:
+ _objc_msgSend$currentCalendar
+ _objc_msgSend$date
+ _objc_msgSend$endIntervalWithSlot:timestampAdjustment:accessCount:
+ _objc_msgSend$endWithTimestampAdjustment:accessCount:
+ _objc_msgSend$initWithAccessor:identifier:kind:assetIdentifiers:visibilityState:accessEventCount:accessCount:
+ _objc_msgSend$initWithInterval:intervalExpirationTime:expiryQueue:clock:onExpiration:expiry:
+ _objc_msgSend$initWithInterval:matcher:tracker:expiry:
+ _objc_msgSend$numberWithUnsignedInteger:
+ _objc_msgSend$objectAtIndexedSubscript:
+ _objc_msgSend$publisherWithStartTime:endTime:maxEvents:lastN:reversed:
+ _objc_msgSend$second
+ _objc_msgSend$setAccessCount:
+ _objc_opt_self
+ _objc_retainAutoreleasedReturnValue
+ _objc_setProperty_nonatomic_copy
+ _swift_allocBox
+ _swift_allocObject
+ _swift_allocateGenericValueMetadata
+ _swift_arrayInitWithCopy
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain
+ _swift_deallocObject
+ _swift_deletedMethodError
+ _swift_dynamicCastObjCClass
+ _swift_dynamicCastObjCProtocolConditional
+ _swift_endAccess
+ _swift_errorRelease
+ _swift_getEnumCaseMultiPayload
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getForeignTypeMetadata
+ _swift_getGenericMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTupleTypeLayout2
+ _swift_getTypeByMangledNameInContext2
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _swift_getWitnessTable
+ _swift_initEnumMetadataMultiPayload
+ _swift_initStructMetadata
+ _swift_isUniquelyReferenced_nonNull_bridgeObject
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_lookUpClassMethod
+ _swift_makeBoxUnique
+ _swift_release
+ _swift_retain
+ _swift_storeEnumTagMultiPayload
+ _swift_storeEnumTagSinglePayloadGeneric
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _swift_updateClassMetadata2
+ _swift_willThrow
+ _symbolic $s17PrivacyAccounting11AccessOrderP
+ _symbolic $sST
+ _symbolic $sSY
+ _symbolic $sSt
+ _symbolic $ss21_ObjectiveCBridgeableP
+ _symbolic 7ElementStQyd__
+ _symbolic SNy_____G 10Foundation4DateV
+ _symbolic SS
+ _symbolic SS_ypt
+ _symbolic SaySo14PAAccessRecord_pG
+ _symbolic Say_____G 17PrivacyAccounting12AccessRecordV
+ _symbolic So14PAAccessReaderC
+ _symbolic So14PAAccessRecord_p
+ _symbolic So8NSObjectC
+ _symbolic So8NSStringC
+ _symbolic SuSg
+ _symbolic _____ 10Foundation4DateV
+ _symbolic _____ 17PrivacyAccounting12AccessRecordV
+ _symbolic _____ 17PrivacyAccounting12AccessRecordV10AccessorIDO
+ _symbolic _____ 17PrivacyAccounting12AccessRecordV6TimingO
+ _symbolic _____ 17PrivacyAccounting12InitialSwiftC
+ _symbolic _____ 17PrivacyAccounting13AccessHistoryV
+ _symbolic _____ 17PrivacyAccounting14AccessIteratorV
+ _symbolic _____ 17PrivacyAccounting20ReverseChronologicalO
+ _symbolic _____ So14PAAccessReaderC17PrivacyAccountingE23_accessRecordsForReport4from2toSo12NSEnumeratorC10Foundation4DateV_AKtKF18AccessRecordObjectL_C
+ _symbolic _____ So16PAAccessCategorya
+ _symbolic _____5lower_AA5uppert 10Foundation4DateV
+ _symbolic _____5start_AA3endt 10Foundation4DateV
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____Sg 17PrivacyAccounting12AccessRecordV
+ _symbolic ______AAt 17PrivacyAccounting12AccessRecordV6TimingO
+ _symbolic __________Xj lSt_px7ElementRts_XPXGMq 17PrivacyAccounting12AccessRecordV
+ _symbolic _____ySSypG s18_DictionaryStorageC
+ _symbolic _____ySay_____GG s16IndexingIteratorV 17PrivacyAccounting12AccessRecordV
+ _symbolic _____ySnySiGG s23_ContiguousArrayStorageC
+ _symbolic _____y_____G 17PrivacyAccounting14AccessIteratorV AA20ReverseChronologicalO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 17PrivacyAccounting12AccessRecordV
+ _symbolic _____yxG 17PrivacyAccounting14AccessIteratorV
+ _symbolic _____yyXlG s23_ContiguousArrayStorageC
+ _symbolic qd__
+ _symbolic x
- -[PAAccess initWithAccessor:identifier:kind:assetIdentifiers:visibilityState:accessEventCount:]
- -[PAAccessInterval endWithTimestampAdjustment:]
- -[PAAccessLogger endIntervalWithSlot:timestampAdjustment:]
- -[PAAccessLogger endIntervalWithSlot:timestampAdjustment:].cold.1
- GCC_except_table17
- GCC_except_table2
- GCC_except_table23
- GCC_except_table28
- _OBJC_IVAR_$_PACoalescingIntervalState._absoluteStartTime
- _OBJC_IVAR_$_PACoalescingIntervalState._continuousStartTime
- _OBJC_IVAR_$_PACoalescingIntervalState._tracker
- __OBJC_$_CLASS_METHODS_PAAccessReader
- __OBJC_$_INSTANCE_METHODS_PAAccessReader
- ___58-[PAAccessLogger endIntervalWithSlot:timestampAdjustment:]_block_invoke
- ___62-[PACoalescingIntervalState initWithInterval:matcher:tracker:]_block_invoke
- ___77-[PAAccessReader initWithConnection:queue:enablementChangedNotificationName:]_block_invoke.111
- ___block_literal_global.109
- ___block_literal_global.207
- ___block_literal_global.238
- ___block_literal_global.247
- ___block_literal_global.90
- ___block_literal_global.93
- _objc_msgSend$endIntervalWithSlot:timestampAdjustment:
- _objc_msgSend$endWithTimestampAdjustment:
- _objc_msgSend$initWithAccessor:identifier:kind:assetIdentifiers:visibilityState:accessEventCount:
- _objc_msgSend$objectAtIndex:
- _objc_msgSend$publisherWithStartTime:endTime:maxEvents:reversed:
CStrings:
+ "#"
+ "1"
+ "2\x11\x11"
+ "<%@ %p> accessor:<%@> identifier:%@ kind:%@ timestampAdjustment:%@ visibilityState:%lu assetIdentifierCount:%lu accessCount:%lu"
+ "@\"NSDate\"16@0:8"
+ "@\"NSNumber\"16@0:8"
+ "@48@0:8@16@24@32d40"
+ "@56@0:8@16d24@32@?40@?48"
+ "@64@0:8@16d24@32@?40@?48d56"
+ "@72@0:8@16@24q32@40q48Q56Q64"
+ "@?"
+ "@?16@0:8"
+ "B16@?0@8"
+ "Down-casted Array element failed to match the target type\nExpected "
+ "Fatal error"
+ "NSArray element failed to match the Swift Array Element type\nExpected "
+ "PAAccessEventRecord"
+ "PAAccessEventRecords"
+ "PrivacyAccounting.AccessRecordObject"
+ "T@\"NSDate\",N,R"
+ "T@\"NSDate\",R"
+ "T@\"NSNumber\",N,R"
+ "T@\"NSNumber\",R"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",N,R"
+ "T@\"NSString\",R"
+ "T@?,C,N,V_clock"
+ "TQ,N,V_accessCount"
+ "Ti,N,V_accessCount"
+ "Tq,N,R"
+ "Tq,N,V_accessCount"
+ "Tq,R"
+ "_TtC17PrivacyAccounting12InitialSwift"
+ "_TtCFE17PrivacyAccountingCSo14PAAccessReader23_accessRecordsForReportFzT4fromV10Foundation4Date2toS2__CSo12NSEnumeratorL_18AccessRecordObject"
+ "_accessCount"
+ "_accessRecordsForReportFrom:to:error:"
+ "_clock"
+ "_startTimes"
+ "accessCount"
+ "accessRecordsForReportFrom:to:error:"
+ "accessorBundleID"
+ "clock"
+ "components:fromDate:"
+ "currentCalendar"
+ "date"
+ "endDate"
+ "endIntervalWithSlot:timestampAdjustment:accessCount:"
+ "endWithTimestampAdjustment:accessCount:"
+ "functionalFunction"
+ "green-tea"
+ "hasAccessCount"
+ "init()"
+ "initWithAccessor:identifier:kind:assetIdentifiers:visibilityState:accessEventCount:accessCount:"
+ "initWithInterval:intervalExpirationTime:expiryQueue:clock:onExpiration:"
+ "initWithInterval:intervalExpirationTime:expiryQueue:clock:onExpiration:expiry:"
+ "initWithInterval:matcher:tracker:expiry:"
+ "initWithUnsignedInteger:"
+ "numberWithUnsignedInteger:"
+ "objectAtIndexedSubscript:"
+ "objectEnumerator"
+ "publisherWithStartTime:endTime:maxEvents:lastN:reversed:"
+ "second"
+ "setAccessCount:"
+ "setClock:"
+ "setHasAccessCount:"
+ "startDate"
+ "timing"
+ "v24@0:8Q16"
+ "v32@0:8d16q24"
+ "v40@0:8@16d24q32"
+ "{?=\"timestampAdjustment\"b1\"accessCount\"b1\"kind\"b1}"
+ "{PATimes=\"absolute\"Q\"continuous\"Q}"
+ "{PATimes=QQ}8@?0"
- "\x13"
- "!"
- "4"
- "<%@ %p> accessor:<%@> identifier:%@ kind:%@ timestampAdjustment:%@ visibilityState:%lu assetIdentifierCount:%lu"
- "@64@0:8@16@24q32@40q48Q56"
- "_absoluteStartTime"
- "_continuousStartTime"
- "_tracker"
- "endIntervalWithSlot:timestampAdjustment:"
- "endWithTimestampAdjustment:"
- "initWithAccessor:identifier:kind:assetIdentifiers:visibilityState:accessEventCount:"
- "objectAtIndex:"
- "publisherWithStartTime:endTime:maxEvents:reversed:"
- "v32@0:8@16d24"
- "{?=\"timestampAdjustment\"b1\"kind\"b1}"

```
