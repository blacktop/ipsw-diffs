## FlightUtilitiesCore

> `/System/Library/PrivateFrameworks/FlightUtilitiesCore.framework/FlightUtilitiesCore`

```diff

-155.2.0.0.0
-  __TEXT.__text: 0x70f0
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_methlist: 0xa8c
-  __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x571
-  __TEXT.__unwind_info: 0x1b8
-  __TEXT.__objc_classname: 0x115
-  __TEXT.__objc_methname: 0x14a5
-  __TEXT.__objc_methtype: 0x419
-  __TEXT.__objc_stubs: 0x1500
-  __DATA_CONST.__got: 0x118
-  __DATA_CONST.__const: 0x130
-  __DATA_CONST.__objc_classlist: 0x50
+171.0.0.0.0
+  __TEXT.__text: 0xdb20
+  __TEXT.__auth_stubs: 0x8f0
+  __TEXT.__objc_methlist: 0xb6c
+  __TEXT.__const: 0x27a
+  __TEXT.__cstring: 0x8d0
+  __TEXT.__swift5_typeref: 0x10f
+  __TEXT.__swift5_capture: 0x170
+  __TEXT.__constg_swiftt: 0x98
+  __TEXT.__swift5_reflstr: 0x36
+  __TEXT.__swift5_fieldmd: 0x54
+  __TEXT.__swift5_builtin: 0x14
+  __TEXT.__swift5_mpenum: 0x8
+  __TEXT.__swift5_proto: 0x8
+  __TEXT.__swift5_types: 0xc
+  __TEXT.__swift_as_entry: 0x3c
+  __TEXT.__swift_as_ret: 0x3c
+  __TEXT.__unwind_info: 0x3b0
+  __TEXT.__eh_frame: 0x6d0
+  __TEXT.__objc_classname: 0x102
+  __TEXT.__objc_methname: 0x1871
+  __TEXT.__objc_methtype: 0x56e
+  __TEXT.__objc_stubs: 0x16c0
+  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__const: 0x1f8
+  __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x680
-  __DATA_CONST.__objc_superrefs: 0x38
-  __AUTH_CONST.__auth_got: 0x1c0
-  __AUTH_CONST.__cfstring: 0x960
-  __AUTH_CONST.__objc_const: 0x1340
+  __DATA_CONST.__objc_selrefs: 0x730
+  __DATA_CONST.__objc_superrefs: 0x30
+  __AUTH_CONST.__auth_got: 0x480
+  __AUTH_CONST.__const: 0x338
+  __AUTH_CONST.__cfstring: 0xa00
+  __AUTH_CONST.__objc_const: 0x13a0
   __AUTH_CONST.__objc_intobj: 0x18
+  __AUTH.__objc_data: 0xb0
+  __AUTH.__data: 0xc8
   __DATA.__objc_ivar: 0xb8
-  __DATA.__data: 0x2a0
-  __DATA.__bss: 0x8
-  __DATA_DIRTY.__objc_data: 0x320
+  __DATA.__data: 0x2c8
+  __DATA.__bss: 0x130
+  __DATA_DIRTY.__objc_data: 0x2d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/CoreParsec.framework/CoreParsec
   - /System/Library/PrivateFrameworks/DataDetectorsCore.framework/DataDetectorsCore
+  - /System/Library/PrivateFrameworks/InternalSwiftProtobuf.framework/InternalSwiftProtobuf
+  - /System/Library/PrivateFrameworks/PegasusAPI.framework/PegasusAPI
+  - /System/Library/PrivateFrameworks/PegasusKit.framework/PegasusKit
+  - /System/Library/PrivateFrameworks/SearchFoundation.framework/SearchFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FB4CAEA4-A042-3419-9AE3-9EF23F8AA8B0
-  Functions: 179
-  Symbols:   797
-  CStrings:  533
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: 1E492F3E-1EC3-3895-B9FB-0A5BEDA31DA6
+  Functions: 304
+  Symbols:   940
+  CStrings:  591
 
Symbols:
+ +[FUFlightFactory fetchUpdateForChannelId:completionHandler:]
+ +[FUFlightFactory subscribeToUpdatesForFlightsWithNumber:airlineCode:date:completionHandler:]
+ +[FUFlightFactory subscribeToUpdatesForFlightsWithNumber:airlineCode:date:updatesHandler:completionHandler:]
+ +[FUFlightFactory unsubscribeFromFlightUpdateChannel:]
+ +[FUFlightFactory_Parsec fetchUpdateForChannelId:completionHandler:]
+ +[FUFlightFactory_Parsec gRPCQuery:date:bundleIdentifier:completionHandler:]
+ +[FUFlightFactory_Parsec httpQuery:date:bundleIdentifier:userAgent:sessionID:completionHandler:]
+ +[FUFlightFactory_Parsec subscribeToUpdatesForFlightsWithNumber:airlineCode:date:completionHandler:]
+ +[FUFlightFactory_Parsec subscribeToUpdatesForFlightsWithNumber:airlineCode:date:updatesHandler:completionHandler:]
+ +[FUFlightFactory_Parsec unsubscribeFromFlightUpdateChannel:]
+ +[FUFlightFactory_Parsec validatedFlightNumber:airlineCode:error:]
+ -[FUFlight operatorAirline]
+ -[FUFlight operatorFlightCode]
+ -[FUFlight operatorFlightNumber]
+ -[FUFlight setOperatorAirline:]
+ -[FUFlight setOperatorFlightNumber:]
+ -[FUFlightLeg _currentProgress]
+ -[FUFlightLeg dateLastUpdated]
+ -[FUFlightLeg setDateLastUpdated:]
+ _OBJC_CLASS_$_SFFlight
+ _OBJC_CLASS_$__SFPBFlight
+ _OBJC_CLASS_$__TtC19FlightUtilitiesCore15FUPegasusBridge
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_FUFlight._operatorAirline
+ _OBJC_IVAR_$_FUFlight._operatorFlightNumber
+ _OBJC_IVAR_$_FUFlightLeg._dateLastUpdated
+ _OBJC_IVAR_$_FUFlightStep._delayFromSchedule
+ _OBJC_METACLASS_$__TtC19FlightUtilitiesCore15FUPegasusBridge
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ __Block_copy
+ __Block_release
+ __CLASS_METHODS__TtC19FlightUtilitiesCore15FUPegasusBridge
+ __DATA__TtC19FlightUtilitiesCore15FUPegasusBridge
+ __DATA__TtC19FlightUtilitiesCoreP33_82CA416D011F476DE6B2459D8021B5EC10ProxyActor
+ __INSTANCE_METHODS__TtC19FlightUtilitiesCore15FUPegasusBridge
+ __IVARS__TtC19FlightUtilitiesCoreP33_82CA416D011F476DE6B2459D8021B5EC10ProxyActor
+ __METACLASS_DATA__TtC19FlightUtilitiesCore15FUPegasusBridge
+ __METACLASS_DATA__TtC19FlightUtilitiesCoreP33_82CA416D011F476DE6B2459D8021B5EC10ProxyActor
+ ___115+[FUFlightFactory_Parsec subscribeToUpdatesForFlightsWithNumber:airlineCode:date:updatesHandler:completionHandler:]_block_invoke
+ ___68+[FUFlightFactory_Parsec fetchUpdateForChannelId:completionHandler:]_block_invoke
+ ___96+[FUFlightFactory_Parsec httpQuery:date:bundleIdentifier:userAgent:sessionID:completionHandler:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSArray"8ls32l8
+ ___block_descriptor_40_e8_32bs_e29_v24?0"NSArray"8"NSError"16ls32l8
+ ___block_descriptor_48_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls40l8s32l8
+ ___block_descriptor_80_e8_32s40s48s56s64bs_e5_v8?0ls32l8s40l8s64l8s48l8s56l8
+ ___chkstk_darwin
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_memcpy17_8
+ ___swift_reflection_version
+ __swiftEmptyArrayStorage
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_FlightUtilitiesCore
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_FlightUtilitiesCore
+ __swift_FORCE_LOAD_$_swiftDarwin
+ __swift_FORCE_LOAD_$_swiftDarwin_$_FlightUtilitiesCore
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_FlightUtilitiesCore
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_FlightUtilitiesCore
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_FlightUtilitiesCore
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_FlightUtilitiesCore
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_FlightUtilitiesCore
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_FlightUtilitiesCore
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_FlightUtilitiesCore
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_FlightUtilitiesCore
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_FlightUtilitiesCore
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_FlightUtilitiesCore
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_FlightUtilitiesCore
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_FlightUtilitiesCore
+ _get_enum_tag_for_layout_string 19FlightUtilitiesCore10ProxyActor33_82CA416D011F476DE6B2459D8021B5ECLLC12PegasusErrorO
+ _objc_allocWithZone
+ _objc_autorelease
+ _objc_msgSend$_currentProgress
+ _objc_msgSend$fetchUpdateFor:completionHandler:
+ _objc_msgSend$flightSearchResponseFor:date:clientBundleIdentifier:completionHandler:
+ _objc_msgSend$gRPCQuery:date:bundleIdentifier:completionHandler:
+ _objc_msgSend$httpQuery:date:bundleIdentifier:userAgent:sessionID:completionHandler:
+ _objc_msgSend$lastUpdatedTime
+ _objc_msgSend$operatorAirline
+ _objc_msgSend$operatorCarrierCode
+ _objc_msgSend$operatorFlightNumber
+ _objc_msgSend$setDateLastUpdated:
+ _objc_msgSend$setOperatorAirline:
+ _objc_msgSend$setOperatorFlightNumber:
+ _objc_msgSend$subscribeTo:date:clientBundleIdentifier:completionHandler:
+ _objc_msgSend$subscribeTo:date:clientBundleIdentifier:pushMessagesHandler:completionHandler:
+ _objc_msgSend$unsubscribeWithChannelId:
+ _objc_msgSend$validatedFlightNumber:airlineCode:error:
+ _objc_opt_self
+ _objc_release_x9
+ _objc_retain_x4
+ _objc_retain_x5
+ _objectdestroy.13Tm
+ _objectdestroy.29Tm
+ _swift_allocError
+ _swift_allocObject
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_deallocObject
+ _swift_defaultActor_deallocate
+ _swift_defaultActor_destroy
+ _swift_deletedMethodError
+ _swift_errorRelease
+ _swift_getErrorValue
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_once
+ _swift_release
+ _swift_retain
+ _swift_task_alloc
+ _swift_task_create
+ _swift_task_dealloc
+ _swift_task_switch
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRetain
+ _symbolic BD
+ _symbolic IeAgH_
+ _symbolic IeghH_
+ _symbolic SS
+ _symbolic SaySo8SFFlightCGIegg_
+ _symbolic ScA_pSg
+ _symbolic ScPSg
+ _symbolic So6NSDateCSg
+ _symbolic So7NSArrayCIeyBy_
+ _symbolic So7NSArrayCSgSo7NSErrorCSgIeyByy_
+ _symbolic So8NSObjectC
+ _symbolic So8NSStringC
+ _symbolic So8NSStringCSg
+ _symbolic So8NSStringCSgSo7NSErrorCSgIeyByy_
+ _symbolic _____ 19FlightUtilitiesCore10ProxyActor33_82CA416D011F476DE6B2459D8021B5ECLLC
+ _symbolic _____ 19FlightUtilitiesCore10ProxyActor33_82CA416D011F476DE6B2459D8021B5ECLLC12PegasusErrorO
+ _symbolic _____ 19FlightUtilitiesCore15FUPegasusBridgeC
+ _symbolic _____Sg 10Foundation4DateV
+ _symbolic _____XMT 19FlightUtilitiesCore10ProxyActor33_82CA416D011F476DE6B2459D8021B5ECLLC
+ _symbolic _____XMo 19FlightUtilitiesCore15FUPegasusBridgeC
+ _symbolic _____yypG s23_ContiguousArrayStorageC
+ _symbolic ytIeAgHr_
+ _type_layout_string 19FlightUtilitiesCore10ProxyActor33_82CA416D011F476DE6B2459D8021B5ECLLC12PegasusErrorO
- +[FUFlightCodeShare supportsSecureCoding]
- -[FUFlight codeShares]
- -[FUFlight setCodeShares:]
- -[FUFlightCodeShare .cxx_destruct]
- -[FUFlightCodeShare airline]
- -[FUFlightCodeShare encodeWithCoder:]
- -[FUFlightCodeShare flightNumber]
- -[FUFlightCodeShare initWithCoder:]
- -[FUFlightCodeShare isEqual:]
- -[FUFlightCodeShare setAirline:]
- -[FUFlightCodeShare setFlightNumber:]
- OBJC_IVAR_$_FUFlightStep._delayFromSchedule
- _OBJC_CLASS_$_FUFlightCodeShare
- _OBJC_IVAR_$_FUFlight._codeShares
- _OBJC_IVAR_$_FUFlightCodeShare._airline
- _OBJC_IVAR_$_FUFlightCodeShare._flightNumber
- _OBJC_METACLASS_$_FUFlightCodeShare
- __OBJC_$_CLASS_METHODS_FUFlightCodeShare
- __OBJC_$_CLASS_PROP_LIST_FUFlightCodeShare
- __OBJC_$_INSTANCE_METHODS_FUFlightCodeShare
- __OBJC_$_INSTANCE_VARIABLES_FUFlightCodeShare
- __OBJC_$_PROP_LIST_FUFlightCodeShare
- __OBJC_CLASS_PROTOCOLS_$_FUFlightCodeShare
- __OBJC_CLASS_RO_$_FUFlightCodeShare
- __OBJC_METACLASS_RO_$_FUFlightCodeShare
- ___127+[FUFlightFactory_Parsec loadFlightStructuresWithFlightNumber:airlineCode:date:dateType:userAgent:sessionID:completionHandler:]_block_invoke_2
- ___block_descriptor_56_e8_32s40bs_e29_v24?0"NSArray"8"NSError"16ls40l8s32l8
- ___block_descriptor_96_e8_32s40s48s56s64bs_e5_v8?0ls32l8s64l8s40l8s48l8s56l8
- _objc_msgSend$codeShares
- _objc_msgSend$uppercaseString
- _objc_retain_x27
CStrings:
+ "$"
+ "$defaultActor"
+ "@\"NSError\"24@0:8@\"NSString\"16"
+ "@40@0:8Q16@24^@32"
+ "Fetching updates not supported in the class FUFlightFactory"
+ "Not enough channel IDs"
+ "Pegasus flight response status unknown or error"
+ "Pegasus subscribe response status unknown or error"
+ "Subscriptions not supported in the class FUFlightFactory"
+ "T@\"FUAirline\",&,V_operatorAirline"
+ "T@\"NSDate\",&,V_dateLastUpdated"
+ "TQ,V_operatorFlightNumber"
+ "_TtC19FlightUtilitiesCore15FUPegasusBridge"
+ "_TtC19FlightUtilitiesCoreP33_82CA416D011F476DE6B2459D8021B5EC10ProxyActor"
+ "_currentProgress"
+ "_dateLastUpdated"
+ "_operatorAirline"
+ "_operatorFlightNumber"
+ "com.apple.FlightUtilities"
+ "com.apple.nanopassd"
+ "com.apple.passd"
+ "dateLastUpdated"
+ "dealloc"
+ "fetchUpdateFor:completionHandler:"
+ "fetchUpdateForChannelId:completionHandler:"
+ "flightSearchResponseFor:date:clientBundleIdentifier:completionHandler:"
+ "gRPCQuery:date:bundleIdentifier:completionHandler:"
+ "httpQuery:date:bundleIdentifier:userAgent:sessionID:completionHandler:"
+ "initWithData:"
+ "initWithProtobuf:"
+ "lastUpdatedTime"
+ "operatorAirline"
+ "operatorCarrierCode"
+ "operatorFlightCode"
+ "operatorFlightNumber"
+ "setDateLastUpdated:"
+ "setOperatorAirline:"
+ "setOperatorFlightNumber:"
+ "subscribeTo:date:clientBundleIdentifier:completionHandler:"
+ "subscribeTo:date:clientBundleIdentifier:pushMessagesHandler:completionHandler:"
+ "subscribeToUpdatesForFlightsWithNumber:airlineCode:date:completionHandler:"
+ "subscribeToUpdatesForFlightsWithNumber:airlineCode:date:updatesHandler:completionHandler:"
+ "unsubscribeFromFlightUpdateChannel:"
+ "unsubscribeWithChannelId:"
+ "v16@?0@\"NSArray\"8"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v48@0:8@\"NSString\"16@\"NSDate\"24@\"NSString\"32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "v48@0:8@\"NSString\"16@\"NSDate\"24@\"NSString\"32@?<v@?@\"NSString\"@\"NSError\">40"
+ "v48@0:8@16@24@32@?40"
+ "v48@0:8Q16@\"NSString\"24@\"NSDate\"32@?<v@?@\"NSString\"@\"NSError\">40"
+ "v48@0:8Q16@24@32@?40"
+ "v56@0:8@\"NSString\"16@\"NSDate\"24@\"NSString\"32@?<v@?@\"NSArray\">40@?<v@?@\"NSString\"@\"NSError\">48"
+ "v56@0:8Q16@\"NSString\"24@\"NSDate\"32@?<v@?@\"NSArray\">40@?<v@?@\"NSString\"@\"NSError\">48"
+ "v56@0:8Q16@24@32@?40@?48"
+ "v64@0:8@16@24@32@40@48@?56"
+ "validatedFlightNumber:airlineCode:error:"
- "#"
- "FUFlightCodeShare"
- "T@\"NSArray\",&,V_codeShares"
- "_codeShares"
- "codeShares"
- "setCodeShares:"
- "uppercaseString"

```
