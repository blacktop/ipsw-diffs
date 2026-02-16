## MetricKitCore

> `/System/Library/PrivateFrameworks/MetricKitCore.framework/MetricKitCore`

```diff

-294.80.3.0.0
-  __TEXT.__text: 0x16824
-  __TEXT.__auth_stubs: 0x590
-  __TEXT.__objc_methlist: 0x19f4
-  __TEXT.__const: 0x158
-  __TEXT.__cstring: 0x892
+297.100.9.0.0
+  __TEXT.__text: 0x1815c
+  __TEXT.__auth_stubs: 0x7b0
+  __TEXT.__objc_methlist: 0x19bc
+  __TEXT.__const: 0x26a
   __TEXT.__oslogstring: 0x1c96
+  __TEXT.__cstring: 0x8f1
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0x510
-  __TEXT.__objc_classname: 0x2be
-  __TEXT.__objc_methname: 0x4920
-  __TEXT.__objc_methtype: 0x98d
-  __TEXT.__objc_stubs: 0x3960
-  __DATA_CONST.__got: 0x3b0
-  __DATA_CONST.__const: 0x180
+  __TEXT.__swift5_typeref: 0x4f
+  __TEXT.__swift5_reflstr: 0x9
+  __TEXT.__swift5_assocty: 0x18
+  __TEXT.__constg_swiftt: 0x54
+  __TEXT.__swift5_fieldmd: 0x10
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_proto: 0xc
+  __TEXT.__swift5_types: 0x8
+  __TEXT.__unwind_info: 0x5e8
+  __TEXT.__objc_classname: 0x2e5
+  __TEXT.__objc_methname: 0x4923
+  __TEXT.__objc_methtype: 0x9e8
+  __TEXT.__objc_stubs: 0x3900
+  __DATA_CONST.__got: 0x3e0
+  __DATA_CONST.__const: 0x1a8
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1058
+  __DATA_CONST.__objc_selrefs: 0x1060
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x88
+  __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x598
-  __AUTH_CONST.__auth_got: 0x2d8
-  __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x820
-  __AUTH_CONST.__objc_const: 0x2c18
+  __AUTH_CONST.__auth_got: 0x3e8
+  __AUTH_CONST.__const: 0x40
+  __AUTH_CONST.__cfstring: 0x860
+  __AUTH_CONST.__objc_const: 0x2b48
   __AUTH_CONST.__objc_arrayobj: 0x288
-  __AUTH_CONST.__objc_intobj: 0x78
-  __DATA.__objc_ivar: 0x140
-  __DATA.__data: 0x660
-  __DATA_DIRTY.__objc_data: 0x5a0
-  __DATA_DIRTY.__bss: 0x30
+  __AUTH_CONST.__objc_intobj: 0x198
+  __AUTH.__objc_data: 0x48
+  __DATA.__objc_ivar: 0x134
+  __DATA.__data: 0x688
+  __DATA.__common: 0x10
+  __DATA.__bss: 0x1c0
+  __DATA_DIRTY.__objc_data: 0x5b8
+  __DATA_DIRTY.__data: 0x30
+  __DATA_DIRTY.__bss: 0x60
+  __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A7901FB2-37AB-318B-99B9-C0A31207C673
-  Functions: 633
-  Symbols:   2348
-  CStrings:  1093
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  UUID: F6B2BB4A-AF5A-348F-907A-2BF8475944E8
+  Functions: 679
+  Symbols:   2413
+  CStrings:  1103
 
Symbols:
+ -[MXClientUtil clientDictionaryLock]
+ -[MXClientUtil clientTeamIDsLock]
+ -[MXClientUtil setClientDictionaryLock:]
+ -[MXClientUtil setClientTeamIDsLock:]
+ -[MXDiagnosticServices initWithSourcePathUtil:]
+ -[MXSourcePathUtil initWithStorageUtil:]
+ _OBJC_CLASS_$__TtC13MetricKitCore15MXDateFormatter
+ _OBJC_IVAR_$_MXClientUtil._clientDictionaryLock
+ _OBJC_IVAR_$_MXClientUtil._clientTeamIDsLock
+ _OBJC_METACLASS_$__TtC13MetricKitCore15MXDateFormatter
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ __CLASS_METHODS__TtC13MetricKitCore15MXDateFormatter
+ __CLASS_PROPERTIES__TtC13MetricKitCore15MXDateFormatter
+ __DATA__TtC13MetricKitCore15MXDateFormatter
+ __INSTANCE_METHODS__TtC13MetricKitCore15MXDateFormatter
+ __METACLASS_DATA__TtC13MetricKitCore15MXDateFormatter
+ ___block_descriptor_48_e19_"NSDictionary"8?0l
+ ___swift_allocate_value_buffer
+ ___swift_instantiateConcreteTypeFromMangledNameV2
+ ___swift_project_value_buffer
+ ___swift_reflection_version
+ __swiftEmptySetSingleton
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_MetricKitCore
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_MetricKitCore
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_MetricKitCore
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_MetricKitCore
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_MetricKitCore
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_MetricKitCore
+ _associated conformance 13MetricKitCore15MXDateFormatterC10DateFormatOSHAASQ
+ _objc_allocWithZone
+ _objc_msgSend$dateFromString:format:
+ _objc_msgSend$dateTruncatedToMinute:
+ _objc_msgSend$init
+ _objc_msgSend$initWithClientUtil:andDeliveryPathUtil:
+ _objc_msgSend$initWithSourcePathUtil:
+ _objc_msgSend$initWithStorageUtil:
+ _objc_msgSend$oneDay
+ _objc_msgSend$stringFromDate:format:
+ _objc_opt_self
+ _objc_retainAutoreleasedReturnValue
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_deallocClassInstance
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_once
+ _swift_setDeallocating
+ _swift_slowAlloc
+ _symbolic $sSY
+ _symbolic Si
+ _symbolic So8NSObjectC
+ _symbolic _____ 13MetricKitCore15MXDateFormatterC
+ _symbolic _____ 13MetricKitCore15MXDateFormatterC10DateFormatO
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____y_____G s11_SetStorageC 10Foundation8CalendarV9ComponentO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 10Foundation8CalendarV9ComponentO
- -[MXCleanUtil dateUtil]
- -[MXCleanUtil initWithClientUtil:andDeliveryPathUtil:andDateUtil:]
- -[MXCleanUtil setDateUtil:]
- -[MXDateUtil .cxx_destruct]
- -[MXDateUtil dateFormatter]
- -[MXDateUtil dateFromString:]
- -[MXDateUtil init]
- -[MXDateUtil setDateFormatter:]
- -[MXDateUtil stringFromDate:]
- -[MXDependencyFactory dateUtil]
- -[MXDiagnosticServices dateUtil]
- -[MXDiagnosticServices initWithSourcePathUtil:andDateUtil:]
- -[MXDiagnosticServices setDateUtil:]
- -[MXSourcePathUtil dateUtil]
- -[MXSourcePathUtil initWithDateUtil:andStorageUtil:]
- -[MXSourcePathUtil setDateUtil:]
- _OBJC_CLASS_$_MXDateUtil
- _OBJC_CLASS_$_NSLocale
- _OBJC_CLASS_$_NSTimeZone
- _OBJC_IVAR_$_MXCleanUtil._dateUtil
- _OBJC_IVAR_$_MXDateUtil._dateFormatter
- _OBJC_IVAR_$_MXDependencyFactory._dateUtil
- _OBJC_IVAR_$_MXDiagnosticServices._dateUtil
- _OBJC_IVAR_$_MXSourcePathUtil._dateUtil
- _OBJC_METACLASS_$_MXDateUtil
- __OBJC_$_INSTANCE_METHODS_MXDateUtil
- __OBJC_$_INSTANCE_VARIABLES_MXDateUtil
- __OBJC_$_PROP_LIST_MXDateUtil
- __OBJC_CLASS_RO_$_MXDateUtil
- __OBJC_METACLASS_RO_$_MXDateUtil
- ___block_descriptor_48_e8_32s_e19_"NSDictionary"8?0ls32l8
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$clientDictionary
- _objc_msgSend$clientTeamIDs
- _objc_msgSend$dateUtil
- _objc_msgSend$initWithClientUtil:andDeliveryPathUtil:andDateUtil:
- _objc_msgSend$initWithDateUtil:andStorageUtil:
- _objc_msgSend$initWithLocaleIdentifier:
- _objc_msgSend$initWithObjects:
- _objc_msgSend$initWithSourcePathUtil:andDateUtil:
- _objc_msgSend$localTimeZone
- _objc_msgSend$setClientDictionary:
- _objc_msgSend$setClientTeamIDs:
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
CStrings:
+ "\v"
+ "@32@0:8@16q24"
+ "Td,N,R"
+ "T{os_unfair_lock_s=I},N,V_clientDictionaryLock"
+ "T{os_unfair_lock_s=I},N,V_clientTeamIDsLock"
+ "_TtC13MetricKitCore15MXDateFormatter"
+ "_clientDictionaryLock"
+ "_clientTeamIDsLock"
+ "clientDictionaryLock"
+ "clientTeamIDsLock"
+ "d16@0:8"
+ "dateFromString:format:"
+ "dateTruncatedToMinute:"
+ "dealloc"
+ "initWithSourcePathUtil:"
+ "initWithStorageUtil:"
+ "oneDay"
+ "setClientDictionaryLock:"
+ "setClientTeamIDsLock:"
+ "stringFromDate:format:"
+ "testBinaryName1"
+ "testBinaryName2"
+ "testBinaryName3"
+ "testBinaryName4"
+ "v20@0:8{os_unfair_lock_s=I}16"
+ "yyyy-MM-dd HH:mm:ss"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
+ "{os_unfair_lock_s=I}16@0:8"
- "\f"
- "@\"MXDateUtil\""
- "@\"NSDateFormatter\""
- "MXDateUtil"
- "T@\"MXDateUtil\",&,V_dateUtil"
- "T@\"MXDateUtil\",R,V_dateUtil"
- "T@\"NSDateFormatter\",&,V_dateFormatter"
- "_dateFormatter"
- "_dateUtil"
- "dateFormatter"
- "dateUtil"
- "en_US_POSIX"
- "initWithClientUtil:andDeliveryPathUtil:andDateUtil:"
- "initWithDateUtil:andStorageUtil:"
- "initWithLocaleIdentifier:"
- "initWithObjects:"
- "initWithSourcePathUtil:andDateUtil:"
- "localTimeZone"
- "setDateFormatter:"
- "setDateUtil:"

```
