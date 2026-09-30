## CarPlay

> `/System/Library/Frameworks/CarPlay.framework/CarPlay`

```diff

-488.11.0.0.0
-  __TEXT.__text: 0x484c8
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x7290
-  __TEXT.__const: 0x238
-  __TEXT.__cstring: 0x3d1c
-  __TEXT.__oslogstring: 0x1f64
-  __TEXT.__gcc_except_tab: 0x884
-  __TEXT.__unwind_info: 0x17b8
-  __TEXT.__objc_classname: 0xfdf
-  __TEXT.__objc_methname: 0xe5f6
-  __TEXT.__objc_methtype: 0x22a6
-  __TEXT.__objc_stubs: 0x8d80
-  __DATA_CONST.__got: 0x5f8
-  __DATA_CONST.__const: 0x1b38
-  __DATA_CONST.__objc_classlist: 0x328
+488.17.3.0.0
+  __TEXT.__text: 0x4ecfc
+  __TEXT.__auth_stubs: 0xb30
+  __TEXT.__objc_methlist: 0x78d8
+  __TEXT.__const: 0x308
+  __TEXT.__cstring: 0x431b
+  __TEXT.__oslogstring: 0x22bb
+  __TEXT.__gcc_except_tab: 0x890
+  __TEXT.__swift5_typeref: 0xad
+  __TEXT.__constg_swiftt: 0xe4
+  __TEXT.__swift5_reflstr: 0x43
+  __TEXT.__swift5_fieldmd: 0x4c
+  __TEXT.__swift5_proto: 0x4
+  __TEXT.__swift5_types: 0x4
+  __TEXT.__unwind_info: 0x1940
+  __TEXT.__objc_classname: 0x10c4
+  __TEXT.__objc_methname: 0xf20b
+  __TEXT.__objc_methtype: 0x2622
+  __TEXT.__objc_stubs: 0x9100
+  __DATA_CONST.__got: 0x688
+  __DATA_CONST.__const: 0x1bc0
+  __DATA_CONST.__objc_classlist: 0x350
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x220
+  __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3110
-  __DATA_CONST.__objc_protorefs: 0x108
-  __DATA_CONST.__objc_superrefs: 0x290
-  __AUTH_CONST.__auth_got: 0x390
-  __AUTH_CONST.__const: 0x8c0
-  __AUTH_CONST.__cfstring: 0x3ec0
-  __AUTH_CONST.__objc_const: 0x1a408
+  __DATA_CONST.__objc_selrefs: 0x33a8
+  __DATA_CONST.__objc_protorefs: 0x140
+  __DATA_CONST.__objc_superrefs: 0x2a8
+  __AUTH_CONST.__auth_got: 0x5a8
+  __AUTH_CONST.__const: 0x8e1
+  __AUTH_CONST.__cfstring: 0x40a0
+  __AUTH_CONST.__objc_const: 0x1bc20
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x1950
-  __DATA.__objc_ivar: 0x790
-  __DATA.__data: 0x1980
-  __DATA.__bss: 0x228
+  __AUTH.__objc_data: 0x1b00
+  __AUTH.__data: 0x188
+  __DATA.__objc_ivar: 0x7ec
+  __DATA.__data: 0x1d30
+  __DATA.__bss: 0x2b0
+  __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x640
   __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AccessoryNavigation.framework/AccessoryNavigation
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
+  - /System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework
   - /System/Library/PrivateFrameworks/CarKit.framework/CarKit
   - /System/Library/PrivateFrameworks/CarKitNavigation.framework/CarKitNavigation
   - /System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices

   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
+  - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8E028587-63C1-34DB-B38F-3B0A2AABCB0B
-  Functions: 2443
-  Symbols:   9044
-  CStrings:  4096
+  - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCore.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftMapKit.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
+  UUID: F74560F1-F6FD-3C99-845A-0F0E69166F81
+  Functions: 2600
+  Symbols:   9704
+  CStrings:  4353
 
Symbols:
+ +[CPNavigationWaypoint supportsSecureCoding]
+ +[CPRouteLeg supportsSecureCoding]
+ +[CPRouteLine supportsSecureCoding]
+ -[CPListImageRowItem imageTitles]
+ -[CPNavigationManager _sendRouteLine]
+ -[CPNavigationManager _sendRouteLine].cold.1
+ -[CPNavigationManager carManager]
+ -[CPNavigationManager routeLine]
+ -[CPNavigationManager routeSharingActive]
+ -[CPNavigationManager setRouteLine:]
+ -[CPNavigationManager setRouteLine:].cold.1
+ -[CPNavigationManager setSupportsRouteSharing:]
+ -[CPNavigationManager setVehicleStateManager:]
+ -[CPNavigationManager supportsRouteSharing]
+ -[CPNavigationManager vehicleStateManager:didUpdateRouteSharingEnabled:]
+ -[CPNavigationManager vehicleStateManager:didUpdateRouteSharingEnabled:].cold.1
+ -[CPNavigationManager vehicleStateManager]
+ -[CPNavigationWaypoint .cxx_destruct]
+ -[CPNavigationWaypoint address]
+ -[CPNavigationWaypoint centerPoint]
+ -[CPNavigationWaypoint dealloc]
+ -[CPNavigationWaypoint encodeWithCoder:]
+ -[CPNavigationWaypoint entryPointsCount]
+ -[CPNavigationWaypoint entryPoints]
+ -[CPNavigationWaypoint initWithCenterPoint:locationThreshold:name:address:entryPoints:entryPointsCount:]
+ -[CPNavigationWaypoint initWithCoder:]
+ -[CPNavigationWaypoint initWithMapItem:locationThreshold:entryPoints:entryPointsCount:]
+ -[CPNavigationWaypoint locationThreshold]
+ -[CPNavigationWaypoint name]
+ -[CPRouteInfo initWithRouteGuidance:maneuvers:laneGuidances:routeLine:]
+ -[CPRouteInfo routeLine]
+ -[CPRouteLeg .cxx_destruct]
+ -[CPRouteLeg coordinates3DCount]
+ -[CPRouteLeg coordinates3D]
+ -[CPRouteLeg dealloc]
+ -[CPRouteLeg destinationLocation]
+ -[CPRouteLeg destination]
+ -[CPRouteLeg encodeWithCoder:]
+ -[CPRouteLeg initWithCoder:]
+ -[CPRouteLeg initWithOrigin:destination:coordinates3D:coordinates3DCount:]
+ -[CPRouteLeg initWithOriginLocation:destinationLocation:coordinates3D:coordinates3DCount:]
+ -[CPRouteLeg originLocation]
+ -[CPRouteLeg origin]
+ -[CPRouteLine .cxx_destruct]
+ -[CPRouteLine destinationLocation]
+ -[CPRouteLine destination]
+ -[CPRouteLine encodeWithCoder:]
+ -[CPRouteLine geodeticSystem]
+ -[CPRouteLine hash]
+ -[CPRouteLine identifier]
+ -[CPRouteLine initWithCoder:]
+ -[CPRouteLine initWithGeodeticSystem:origin:destination:routeLegs:]
+ -[CPRouteLine initWithGeodeticSystem:originLocation:destinationLocation:routeLegs:]
+ -[CPRouteLine isEqual:]
+ -[CPRouteLine isEqualToRouteLine:]
+ -[CPRouteLine originLocation]
+ -[CPRouteLine origin]
+ -[CPRouteLine routeLegs]
+ GCC_except_table66
+ _$s10Foundation4UUIDV10uuidStringSSvg
+ _$s10Foundation4UUIDV36_unconditionallyBridgeFromObjectiveCyACSo6NSUUIDCSgFZ
+ _$s10Foundation4UUIDVACSQAAWL
+ _$s10Foundation4UUIDVACSQAAWl
+ _$s10Foundation4UUIDVMa
+ _$s10Foundation4UUIDVMn
+ _$s10Foundation4UUIDVSQAAMc
+ _$s10Foundation4UUIDVSgMD
+ _$s10Foundation4UUIDVSgML
+ _$s10Foundation4UUIDVSgMa
+ _$s10Foundation4UUIDVSgWOcTm
+ _$s10Foundation4UUIDVSgWOd
+ _$s10Foundation4UUIDVSgWOhTm
+ _$s10Foundation4UUIDVSg_ADtMD
+ _$s2os32getNullTerminatedUTF8PointerImpl_21storingStringOwnersInSVSS_SpyypGSgztF
+ _$s2os6LoggerV7CarPlayE19vehicleStateManagerACvau
+ _$s2os6LoggerV7CarPlayE19vehicleStateManagerACvgZ
+ _$s2os6LoggerV7CarPlayE19vehicleStateManagerACvpZ
+ _$s2os6LoggerV7CarPlayE19vehicleStateManager_WZ
+ _$s2os6LoggerV7CarPlayE19vehicleStateManager_Wz
+ _$s2os6LoggerV9logObjectSo03OS_a1_C0Cvg
+ _$s2os6LoggerV9subsystem8categoryACSS_SStcfC
+ _$s2os6LoggerVMa
+ _$s7CarPlay17RouteSharingStateC08supportscD0SbvMTq
+ _$s7CarPlay17RouteSharingStateC08supportscD0SbvW
+ _$s7CarPlay17RouteSharingStateC08supportscD0SbvgTq
+ _$s7CarPlay17RouteSharingStateC08supportscD0SbvpWvd
+ _$s7CarPlay17RouteSharingStateC08supportscD0SbvsTq
+ _$s7CarPlay17RouteSharingStateC11descriptionSSvg
+ _$s7CarPlay17RouteSharingStateC11userEnabledSbvgTq
+ _$s7CarPlay17RouteSharingStateC14lastIdentifier10Foundation4UUIDVSgvMTq
+ _$s7CarPlay17RouteSharingStateC14lastIdentifier10Foundation4UUIDVSgvgTq
+ _$s7CarPlay17RouteSharingStateC14lastIdentifier10Foundation4UUIDVSgvpWvd
+ _$s7CarPlay17RouteSharingStateC14lastIdentifier10Foundation4UUIDVSgvsTq
+ _$s7CarPlay17RouteSharingStateC14ownsNavigationSbvMTq
+ _$s7CarPlay17RouteSharingStateC14ownsNavigationSbvW
+ _$s7CarPlay17RouteSharingStateC14ownsNavigationSbvgTq
+ _$s7CarPlay17RouteSharingStateC14ownsNavigationSbvpWvd
+ _$s7CarPlay17RouteSharingStateC14ownsNavigationSbvsTq
+ _$s7CarPlay17RouteSharingStateC14vehicleEnabledSbvgTq
+ _$s7CarPlay17RouteSharingStateC5routeSo8CAFRouteCSgvMTq
+ _$s7CarPlay17RouteSharingStateC5routeSo8CAFRouteCSgvgTq
+ _$s7CarPlay17RouteSharingStateC5routeSo8CAFRouteCSgvpWvd
+ _$s7CarPlay17RouteSharingStateC5routeSo8CAFRouteCSgvsTq
+ _$s7CarPlay17RouteSharingStateC7enabledSbvg
+ _$s7CarPlay17RouteSharingStateC7enabledSbvgTq
+ _$s7CarPlay17RouteSharingStateC8delegateSo09CPVehicleE15ManagerDelegate_pSgvMTq
+ _$s7CarPlay17RouteSharingStateC8delegateSo09CPVehicleE15ManagerDelegate_pSgvgTq
+ _$s7CarPlay17RouteSharingStateC8delegateSo09CPVehicleE15ManagerDelegate_pSgvpWvd
+ _$s7CarPlay17RouteSharingStateC8delegateSo09CPVehicleE15ManagerDelegate_pSgvsTq
+ _$s7CarPlay17RouteSharingStateCACycfCTq
+ _$s7CarPlay17RouteSharingStateCMF
+ _$s7CarPlay17RouteSharingStateCMU
+ _$s7CarPlay17RouteSharingStateCMa
+ _$s7CarPlay17RouteSharingStateCMf
+ _$s7CarPlay17RouteSharingStateCMl
+ _$s7CarPlay17RouteSharingStateCMm
+ _$s7CarPlay17RouteSharingStateCMn
+ _$s7CarPlay17RouteSharingStateCMr
+ _$s7CarPlay17RouteSharingStateCN
+ _$s7CarPlay17RouteSharingStateCfD
+ _$s7CarPlay17RouteSharingStateCs23CustomStringConvertibleAAMc
+ _$s7CarPlay17RouteSharingStateCs23CustomStringConvertibleAAMcMK
+ _$s7CarPlay17RouteSharingStateCs23CustomStringConvertibleAAsADP11descriptionSSvgTW
+ _$s7CarPlayMXM
+ _$sBoWV
+ _$sSD10FoundationE19_bridgeToObjectiveCSo12NSDictionaryCyF
+ _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCs11AnyHashableV_ypTt0g5Tf4g_n
+ _$sSQ2eeoiySbx_xtFZTj
+ _$sSS10FoundationE19_bridgeToObjectiveCSo8NSStringCyF
+ _$sSS10FoundationE36_unconditionallyBridgeFromObjectiveCySSSo8NSStringCSgFZ
+ _$sSS6appendyySSF
+ _$sSS8UTF8ViewV13_foreignCountSiyF
+ _$sSa034_makeUniqueAndReserveCapacityIfNotB0yyFyXl_Ts5
+ _$sSa10FoundationE19_bridgeToObjectiveCSo7NSArrayCyF
+ _$sSa10FoundationE36_unconditionallyBridgeFromObjectiveCySayxGSo7NSArrayCSgFZ
+ _$sSa16_createNewBuffer14bufferIsUnique15minimumCapacity13growForAppendySb_SiSbtFyXl_Ts5
+ _$sSa37_appendElementAssumeUniqueAndCapacity_03newB0ySi_xntFyXl_Ts5
+ _$sSa6append10contentsOfyqd__n_t7ElementQyd__RszSTRd__lFs5UInt8V_SayAFGTgq5
+ _$sSbN
+ _$sSo11CAFRouteLegCML
+ _$sSo13CAFCoordinateCML
+ _$sSo13CAFCoordinateCMaTm
+ _$sSo13os_log_type_ta0A0E5debugABvgZ
+ _$sSo16CPBridgeRouteLegP7CarPlayE3cafSo08CAFRouteC0Cvg
+ _$sSo16CPBridgeRouteLeg_pMD
+ _$sSo17CPBridgeRouteLineP7CarPlayE4legsSo12CAFRouteLegsCvg
+ _$sSo21CPVehicleStateManagerC7CarPlayE012routeSharingB033_8CF23B4C98753B3B7E23CE4A41E0DBB4LLAC05RoutegB0CvpWvd
+ _$sSo21CPVehicleStateManagerC7CarPlayE03carC0So06CAFCarC0CvgTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE03carC0So06CAFCarC0CvpWvd
+ _$sSo21CPVehicleStateManagerC7CarPlayE03carC0_016didUpdateCurrentD0ySo06CAFCarC0C_So0J0CSgtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE03carC0_016didUpdateCurrentD0ySo06CAFCarC0C_So0J0CSgtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE07currentD033_8CF23B4C98753B3B7E23CE4A41E0DBB4LLSo6CAFCarCSgvgTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE07currentD033_8CF23B4C98753B3B7E23CE4A41E0DBB4LLSo6CAFCarCSgvgToTm
+ _$sSo21CPVehicleStateManagerC7CarPlayE10clearRoute33_8CF23B4C98753B3B7E23CE4A41E0DBB4LLyyF
+ _$sSo21CPVehicleStateManagerC7CarPlayE10clearRoute33_8CF23B4C98753B3B7E23CE4A41E0DBB4LLyyFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE10navigation33_8CF23B4C98753B3B7E23CE4A41E0DBB4LLSo13CAFNavigationCSgvgTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_014didUpdateRouteB0ySo8CAFRouteC_So0kB0VtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_014didUpdateRouteB0ySo8CAFRouteC_So0kB0VtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_13didUpdateLegsySo8CAFRouteC_So0kJ0CSgtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_13didUpdateLegsySo8CAFRouteC_So0kJ0CSgtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_15didUpdateOriginySo8CAFRouteC_So18CAFPointOfInterestCSgtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_15didUpdateOriginySo8CAFRouteC_So18CAFPointOfInterestCSgtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_20didUpdateDestinationySo8CAFRouteC_So18CAFPointOfInterestCSgtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_20didUpdateDestinationySo8CAFRouteC_So18CAFPointOfInterestCSgtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_20didUpdateUserEnabledySo8CAFRouteC_SbtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_20didUpdateUserEnabledySo8CAFRouteC_SbtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_23didUpdateGeodeticSystemySo8CAFRouteC_So011CAFGeodeticK0VtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_23didUpdateGeodeticSystemySo8CAFRouteC_So011CAFGeodeticK0VtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_23didUpdateVehicleEnabledySo8CAFRouteC_SbtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_23didUpdateVehicleEnabledySo8CAFRouteC_SbtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_27didUpdateApplicationEnabledySo8CAFRouteC_SbtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_27didUpdateApplicationEnabledySo8CAFRouteC_SbtFTm
+ _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_27didUpdateApplicationEnabledySo8CAFRouteC_SbtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_27didUpdateApplicationEnabledySo8CAFRouteC_SbtFToTm
+ _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_35didUpdateUserVisibleApplicationNameySo8CAFRouteC_SSSgtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_35didUpdateUserVisibleApplicationNameySo8CAFRouteC_SSSgtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE14clearRouteLine33_8CF23B4C98753B3B7E23CE4A41E0DBB4LLyyF
+ _$sSo21CPVehicleStateManagerC7CarPlayE14clearRouteLine33_8CF23B4C98753B3B7E23CE4A41E0DBB4LLyyFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE20supportsRouteSharingSbvgTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE20supportsRouteSharingSbvsTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE23carDidUpdateAccessoriesyySo6CAFCarCF
+ _$sSo21CPVehicleStateManagerC7CarPlayE23carDidUpdateAccessoriesyySo6CAFCarCFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE25forceUserEnabledIfAllowed33_8CF23B4C98753B3B7E23CE4A41E0DBB4LL6reasonyAbCE11ForceReasonAELLO_tF
+ _$sSo21CPVehicleStateManagerC7CarPlayE28didUpdateNavigationOwnershipyyF
+ _$sSo21CPVehicleStateManagerC7CarPlayE28didUpdateNavigationOwnershipyyFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE30willReleaseNavigationOwnershipyyF
+ _$sSo21CPVehicleStateManagerC7CarPlayE30willReleaseNavigationOwnershipyyFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE4sendyySo016CPBridgeGuidanceB0VF
+ _$sSo21CPVehicleStateManagerC7CarPlayE4sendyySo016CPBridgeGuidanceB0VFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE4sendyySo17CPBridgeRouteLine_pSgF
+ _$sSo21CPVehicleStateManagerC7CarPlayE4sendyySo17CPBridgeRouteLine_pSgFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE5route33_8CF23B4C98753B3B7E23CE4A41E0DBB4LLSo8CAFRouteCSgvgTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE8delegate33_8CF23B4C98753B3B7E23CE4A41E0DBB4LLSo0abC8Delegate_pSgvgTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE8delegate33_8CF23B4C98753B3B7E23CE4A41E0DBB4LLSo0abC8Delegate_pSgvpWvd
+ _$sSo21CPVehicleStateManagerC7CarPlayE8delegate33_8CF23B4C98753B3B7E23CE4A41E0DBB4LLSo0abC8Delegate_pSgvpfi
+ _$sSo21CPVehicleStateManagerC7CarPlayE8delegate33_8CF23B4C98753B3B7E23CE4A41E0DBB4LLSo0abC8Delegate_pSgvsTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE8delegateABSo0abC8Delegate_p_tcfc
+ _$sSo21CPVehicleStateManagerC7CarPlayE8delegateABSo0abC8Delegate_p_tcfcTo
+ _$sSo21CPVehicleStateManagerC7CarPlayEABycfC
+ _$sSo21CPVehicleStateManagerC7CarPlayEABycfc
+ _$sSo21CPVehicleStateManagerC7CarPlayEABycfcTo
+ _$sSo21CPVehicleStateManagerCML
+ _$sSo21CPVehicleStateManagerCMa
+ _$sSo21CPVehicleStateManagerCfETo
+ _$sSo26CPBridgeNavigationWaypointP7CarPlayE3cafSo18CAFPointOfInterestCvg
+ _$sSo29CPVehicleStateManagerDelegate_pSgXwWOh
+ _$sSq7CarPlaySpySo28CPBridgeLocationCoordinate3DaGRszlE11coordinates5countSaySo13CAFCoordinateCGSgSi_tF
+ _$sSqMa
+ _$ss018_bridgeAnyObjectToB0yypyXlSgF
+ _$ss11AnyHashableV13_rawHashValue4seedS2i_tF
+ _$ss11AnyHashableV2eeoiySbAB_ABtFZ
+ _$ss11AnyHashableVMn
+ _$ss11AnyHashableVN
+ _$ss11AnyHashableVSHsWP
+ _$ss11AnyHashableVWOc
+ _$ss11AnyHashableVWOh
+ _$ss11AnyHashableV_yptMD
+ _$ss11_StringGutsV16_deconstructUTF87scratchyXlSg5owner_xSi6lengthSb11usesScratchSb15allocatedMemorytSwSg_ts8_PointerRzlFSV_Tgq5
+ _$ss11_StringGutsV16_foreignCopyUTF84intoSiSgSrys5UInt8VG_tF
+ _$ss11_StringGutsV23_allocateForDeconstructyXl5owner_SVSi6lengthtyF
+ _$ss11_StringGutsV23_allocateForDeconstructyXl5owner_SVSi6lengthtyFTv_r
+ _$ss11_StringGutsV4growyySiF
+ _$ss11_StringGutsVN
+ _$ss12_ArrayBufferV19_getElementSlowPathyyXlSiFyXl_Ts5
+ _$ss12_ArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtFs5UInt8V_Tgq5
+ _$ss13_StringObjectV10sharedUTF8SRys5UInt8VGvg
+ _$ss15ContiguousArrayV034_makeUniqueAndReserveCapacityIfNotD0yyFyXl_Ts5
+ _$ss15ContiguousArrayV12_endMutationyyFyXl_Ts5
+ _$ss15ContiguousArrayV15reserveCapacityyySiFyXl_Ts5
+ _$ss15ContiguousArrayV36_reserveCapacityAssumingUniqueBuffer8oldCountySi_tFyXl_Ts5
+ _$ss15ContiguousArrayV37_appendElementAssumeUniqueAndCapacity_03newD0ySi_xntFyXl_Ts5
+ _$ss18_CocoaArrayWrapperV8endIndexSivg
+ _$ss18_DictionaryStorageC8allocate8capacityAByxq_GSi_tFZ
+ _$ss18_DictionaryStorageCMn
+ _$ss18_DictionaryStorageCys11AnyHashableVypGMD
+ _$ss20__StaticArrayStorageCN
+ _$ss22_ContiguousArrayBufferV19_uninitializedCount15minimumCapacityAByxGSi_SitcfCs5UInt8V_Tt1gq5
+ _$ss22__RawDictionaryStorageC4find_9hashValues10_HashTableV6BucketV6bucket_Sb5foundtx_SitSHRzlFs11AnyHashableV_Tg5
+ _$ss22__RawDictionaryStorageC4findys10_HashTableV6BucketV6bucket_Sb5foundtxSHRzlFs11AnyHashableV_Tg5
+ _$ss23CustomStringConvertibleMp
+ _$ss23CustomStringConvertibleP11descriptionSSvgTq
+ _$ss23_ContiguousArrayStorageCMn
+ _$ss23_ContiguousArrayStorageCys5UInt8VGMD
+ _$ss32_copyCollectionToContiguousArrayys0dE0Vy7ElementQzGxSlRzlFSS8UTF8ViewV_Tgq5
+ _$ss5UInt8VMn
+ _$sypN
+ _$sypSgMD
+ _$sypWOb
+ _$sypWOc
+ _OBJC_CLASS_$_CAFCarManager
+ _OBJC_CLASS_$_CAFCoordinate
+ _OBJC_CLASS_$_CAFPointOfInterest
+ _OBJC_CLASS_$_CAFRouteLeg
+ _OBJC_CLASS_$_CAFRouteLegs
+ _OBJC_CLASS_$_CPNavigationWaypoint
+ _OBJC_CLASS_$_CPRouteLeg
+ _OBJC_CLASS_$_CPRouteLine
+ _OBJC_CLASS_$_CPVehicleStateManager
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$__TtCs12_SwiftObject
+ _OBJC_IVAR_$_CPNavigationManager._routeLine
+ _OBJC_IVAR_$_CPNavigationManager._routeSharingActive
+ _OBJC_IVAR_$_CPNavigationManager._vehicleStateManager
+ _OBJC_IVAR_$_CPNavigationWaypoint._address
+ _OBJC_IVAR_$_CPNavigationWaypoint._centerPoint
+ _OBJC_IVAR_$_CPNavigationWaypoint._entryPoints
+ _OBJC_IVAR_$_CPNavigationWaypoint._entryPointsCount
+ _OBJC_IVAR_$_CPNavigationWaypoint._locationThreshold
+ _OBJC_IVAR_$_CPNavigationWaypoint._name
+ _OBJC_IVAR_$_CPRouteInfo._routeLine
+ _OBJC_IVAR_$_CPRouteLeg._coordinates3D
+ _OBJC_IVAR_$_CPRouteLeg._coordinates3DCount
+ _OBJC_IVAR_$_CPRouteLeg._destination
+ _OBJC_IVAR_$_CPRouteLeg._destinationLocation
+ _OBJC_IVAR_$_CPRouteLeg._origin
+ _OBJC_IVAR_$_CPRouteLeg._originLocation
+ _OBJC_IVAR_$_CPRouteLine._destination
+ _OBJC_IVAR_$_CPRouteLine._destinationLocation
+ _OBJC_IVAR_$_CPRouteLine._geodeticSystem
+ _OBJC_IVAR_$_CPRouteLine._identifier
+ _OBJC_IVAR_$_CPRouteLine._origin
+ _OBJC_IVAR_$_CPRouteLine._originLocation
+ _OBJC_IVAR_$_CPRouteLine._routeLegs
+ _OBJC_METACLASS_$_CPNavigationWaypoint
+ _OBJC_METACLASS_$_CPRouteLeg
+ _OBJC_METACLASS_$_CPRouteLine
+ _OBJC_METACLASS_$_CPVehicleStateManager
+ _OBJC_METACLASS_$__TtCs12_SwiftObject
+ _OUTLINED_FUNCTION_7
+ __DATA_CPVehicleStateManager
+ __DATA__TtC7CarPlay17RouteSharingState
+ __IVARS_CPVehicleStateManager
+ __IVARS__TtC7CarPlay17RouteSharingState
+ __METACLASS_DATA_CPVehicleStateManager
+ __METACLASS_DATA__TtC7CarPlay17RouteSharingState
+ __OBJC_$_CLASS_METHODS_CPNavigationWaypoint
+ __OBJC_$_CLASS_METHODS_CPRouteLeg
+ __OBJC_$_CLASS_METHODS_CPRouteLine
+ __OBJC_$_CLASS_PROP_LIST_CPNavigationWaypoint
+ __OBJC_$_CLASS_PROP_LIST_CPRouteLeg
+ __OBJC_$_CLASS_PROP_LIST_CPRouteLine
+ __OBJC_$_INSTANCE_METHODS_CPNavigationWaypoint
+ __OBJC_$_INSTANCE_METHODS_CPRouteLeg
+ __OBJC_$_INSTANCE_METHODS_CPRouteLine
+ __OBJC_$_INSTANCE_METHODS_CPVehicleStateManager(CarPlay|CarPlay1|CarPlay2|CarPlay3)
+ __OBJC_$_INSTANCE_VARIABLES_CPNavigationWaypoint
+ __OBJC_$_INSTANCE_VARIABLES_CPRouteLeg
+ __OBJC_$_INSTANCE_VARIABLES_CPRouteLine
+ __OBJC_$_PROP_LIST_CPBridgeNavigationWaypoint
+ __OBJC_$_PROP_LIST_CPBridgeRouteLeg
+ __OBJC_$_PROP_LIST_CPBridgeRouteLine
+ __OBJC_$_PROP_LIST_CPVehicleStateManagerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFCarManagerObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFCarObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFRouteObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPBridgeNavigationWaypoint
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPBridgeRouteLeg
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPBridgeRouteLine
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPVehicleStateManagerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CAFCarObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CAFServiceObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFCarManagerObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFCarObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFRouteObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFServiceObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPBridgeNavigationWaypoint
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPBridgeRouteLeg
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPBridgeRouteLine
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPVehicleStateManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_CAFCarManagerObserver
+ __OBJC_$_PROTOCOL_REFS_CAFCarObserver
+ __OBJC_$_PROTOCOL_REFS_CAFRouteObserver
+ __OBJC_$_PROTOCOL_REFS_CAFServiceObserver
+ __OBJC_$_PROTOCOL_REFS_CPBridgeNavigationWaypoint
+ __OBJC_$_PROTOCOL_REFS_CPBridgeRouteLeg
+ __OBJC_$_PROTOCOL_REFS_CPBridgeRouteLine
+ __OBJC_$_PROTOCOL_REFS_CPVehicleStateManagerDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CPNavigationWaypoint(SwiftRouteBridge)
+ __OBJC_CLASS_PROTOCOLS_$_CPRouteLeg(SwiftRouteBridge)
+ __OBJC_CLASS_PROTOCOLS_$_CPRouteLine(SwiftRouteBridge)
+ __OBJC_CLASS_PROTOCOLS_$_CPVehicleStateManager(CarPlay|CarPlay1|CarPlay2|CarPlay3)
+ __OBJC_CLASS_RO_$_CPNavigationWaypoint
+ __OBJC_CLASS_RO_$_CPRouteLeg
+ __OBJC_CLASS_RO_$_CPRouteLine
+ __OBJC_LABEL_PROTOCOL_$_CAFCarManagerObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFCarObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFRouteObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFServiceObserver
+ __OBJC_LABEL_PROTOCOL_$_CPBridgeNavigationWaypoint
+ __OBJC_LABEL_PROTOCOL_$_CPBridgeRouteLeg
+ __OBJC_LABEL_PROTOCOL_$_CPBridgeRouteLine
+ __OBJC_LABEL_PROTOCOL_$_CPVehicleStateManagerDelegate
+ __OBJC_METACLASS_RO_$_CPNavigationWaypoint
+ __OBJC_METACLASS_RO_$_CPRouteLeg
+ __OBJC_METACLASS_RO_$_CPRouteLine
+ __OBJC_PROTOCOL_$_CAFCarManagerObserver
+ __OBJC_PROTOCOL_$_CAFCarObserver
+ __OBJC_PROTOCOL_$_CAFRouteObserver
+ __OBJC_PROTOCOL_$_CAFServiceObserver
+ __OBJC_PROTOCOL_$_CPBridgeNavigationWaypoint
+ __OBJC_PROTOCOL_$_CPBridgeRouteLeg
+ __OBJC_PROTOCOL_$_CPBridgeRouteLine
+ __OBJC_PROTOCOL_$_CPVehicleStateManagerDelegate
+ __PROPERTIES_CPVehicleStateManager
+ ___39-[CPNavigationManager _setupConnection]_block_invoke.230
+ ___39-[CPNavigationManager _setupConnection]_block_invoke.231
+ ___39-[CPNavigationManager _setupConnection]_block_invoke.233
+ ___49-[CPNavigationManager didUpdateActiveComponents:]_block_invoke.242
+ ___51-[CPNavigationManager initWithIdentifier:delegate:]_block_invoke.174
+ ___51-[CPNavigationManager initWithIdentifier:delegate:]_block_invoke.180
+ ___51-[CPNavigationManager initWithIdentifier:delegate:]_block_invoke.180.cold.1
+ ___51-[CPNavigationManager initWithIdentifier:delegate:]_block_invoke.187
+ ___51-[CPNavigationManager initWithIdentifier:delegate:]_block_invoke.187.cold.1
+ ___81-[CPTemplateApplicationInstrumentClusterScene initWithSession:connectionOptions:]_block_invoke.7
+ ___81-[CPTemplateApplicationInstrumentClusterScene initWithSession:connectionOptions:]_block_invoke.9
+ ___block_literal_global.202
+ ___block_literal_global.206
+ ___block_literal_global.208
+ ___block_literal_global.210
+ ___block_literal_global.213
+ ___block_literal_global.216
+ ___block_literal_global.218
+ ___block_literal_global.221
+ ___block_literal_global.223
+ ___block_literal_global.225
+ ___block_literal_global.236
+ ___block_literal_global.249
+ ___chkstk_darwin
+ ___swift_allocate_value_buffer
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_instantiateConcreteTypeFromMangledName
+ ___swift_project_value_buffer
+ ___swift_reflection_version
+ __swiftEmptyArrayStorage
+ __swiftEmptyDictionarySingleton
+ __swiftImmortalRefCount
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftAccelerate_$_CarPlay
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftCoreFoundation_$_CarPlay
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_CarPlay
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __swift_FORCE_LOAD_$_swiftCoreLocation_$_CarPlay
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftDispatch_$_CarPlay
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftFoundation_$_CarPlay
+ __swift_FORCE_LOAD_$_swiftMapKit
+ __swift_FORCE_LOAD_$_swiftMapKit_$_CarPlay
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftMetal_$_CarPlay
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_CarPlay
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftObjectiveC_$_CarPlay
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftQuartzCore_$_CarPlay
+ __swift_FORCE_LOAD_$_swiftUIKit
+ __swift_FORCE_LOAD_$_swiftUIKit_$_CarPlay
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers_$_CarPlay
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swiftXPC_$_CarPlay
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_Builtin_float_$_CarPlay
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_CarPlay
+ __swift_FORCE_LOAD_$_swiftsimd
+ __swift_FORCE_LOAD_$_swiftsimd_$_CarPlay
+ __swift_stdlib_malloc_size
+ __swift_stdlib_reportUnimplementedInitializer
+ _flat unique So16CPBridgeRouteLeg_p
+ _flat unique So29CPVehicleStateManagerDelegate_p
+ _malloc_size
+ _malloc_type_malloc
+ _memmove
+ _objc_allocWithZone
+ _objc_msgSend$_sendRouteLine
+ _objc_msgSend$address
+ _objc_msgSend$altitude
+ _objc_msgSend$carManager
+ _objc_msgSend$coordinate
+ _objc_msgSend$dataWithBytes:length:
+ _objc_msgSend$decodeArrayOfObjectsOfClass:forKey:
+ _objc_msgSend$decodeInt32ForKey:
+ _objc_msgSend$didUpdateLastNavigatingBundleIdentifier:
+ _objc_msgSend$didUpdateNavigationOwnership
+ _objc_msgSend$didUpdateRouteSharingActive:
+ _objc_msgSend$encodeInt32:forKey:
+ _objc_msgSend$fullAddress
+ _objc_msgSend$getBytes:length:
+ _objc_msgSend$initWithCenterPoint:locationThreshold:name:address:entryPoints:entryPointsCount:
+ _objc_msgSend$initWithDelegate:
+ _objc_msgSend$initWithGeodeticSystem:originLocation:destinationLocation:routeLegs:
+ _objc_msgSend$initWithMapItem:locationThreshold:entryPoints:entryPointsCount:
+ _objc_msgSend$initWithOriginLocation:destinationLocation:coordinates3D:coordinates3DCount:
+ _objc_msgSend$initWithRouteGuidance:maneuvers:laneGuidances:routeLine:
+ _objc_msgSend$isEqualToRouteLine:
+ _objc_msgSend$routeLine
+ _objc_msgSend$sendGuidanceState:
+ _objc_msgSend$sendRouteLine:
+ _objc_msgSend$setSupportsRouteSharing:
+ _objc_msgSend$supportsRouteSharing
+ _objc_msgSend$vehicleStateManager
+ _objc_msgSend$willReleaseNavigationOwnership
+ _swift_allocObject
+ _swift_arrayDestroy
+ _swift_beginAccess
+ _swift_bridgeObjectRelease
+ _swift_bridgeObjectRetain
+ _swift_deallocClassInstance
+ _swift_deletedMethodError
+ _swift_dynamicCast
+ _swift_endAccess
+ _swift_getObjCClassFromMetadata
+ _swift_getObjCClassMetadata
+ _swift_getObjectType
+ _swift_getSingletonMetadata
+ _swift_getTypeByMangledNameInContext2
+ _swift_getWitnessTable
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_once
+ _swift_release
+ _swift_retain
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_unknownObjectRelease
+ _swift_unknownObjectRelease_n
+ _swift_unknownObjectRetain
+ _swift_unknownObjectWeakAssign
+ _swift_unknownObjectWeakDestroy
+ _swift_unknownObjectWeakInit
+ _swift_unknownObjectWeakLoadStrong
+ _swift_updateClassMetadata2
+ _symbolic Sb
+ _symbolic So8CAFRouteCSgXw
+ _symbolic _____ 7CarPlay17RouteSharingStateC
+ _symbolic _____Sg 10Foundation4UUIDV
+ _symbolic _____Sg_ABt 10Foundation4UUIDV
+ _symbolic ______p So16CPBridgeRouteLegP
+ _symbolic ______pSgXw So29CPVehicleStateManagerDelegateP
+ _symbolic ______ypt s11AnyHashableV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic _____y_____ypG s18_DictionaryStorageC s11AnyHashableV
+ _symbolic ypSg
- GCC_except_table60
- ___39-[CPNavigationManager _setupConnection]_block_invoke.121
- ___39-[CPNavigationManager _setupConnection]_block_invoke.122
- ___39-[CPNavigationManager _setupConnection]_block_invoke.124
- ___49-[CPNavigationManager didUpdateActiveComponents:]_block_invoke.133
- ___51-[CPNavigationManager initWithIdentifier:delegate:]_block_invoke.74
- ___51-[CPNavigationManager initWithIdentifier:delegate:]_block_invoke.74.cold.1
- ___51-[CPNavigationManager initWithIdentifier:delegate:]_block_invoke.81
- ___51-[CPNavigationManager initWithIdentifier:delegate:]_block_invoke.81.cold.1
- ___81-[CPTemplateApplicationInstrumentClusterScene initWithSession:connectionOptions:]_block_invoke.3
- ___81-[CPTemplateApplicationInstrumentClusterScene initWithSession:connectionOptions:]_block_invoke.5
- ___block_literal_global.101
- ___block_literal_global.104
- ___block_literal_global.107
- ___block_literal_global.109
- ___block_literal_global.112
- ___block_literal_global.116
- ___block_literal_global.127
- ___block_literal_global.181
- ___block_literal_global.94
- ___block_literal_global.97
- ___block_literal_global.99
CStrings:
+ " lastIdentifier="
+ " ownsNavigation="
+ " supportsRouteSharing="
+ " vehicleEnabled="
+ "%s failed: delegate is nil"
+ "%s failed: route is nil"
+ "%s failed: routeLine.identifier=%s  lastRouteLineIdentifier=%s"
+ "%s failed: routeLineSupport.enabled is false - %s"
+ "%s failed: routeLineSupport.ownsNavigation is false"
+ "%s ownsNavigation=%{bool}d"
+ "%s ownsNavigation=%{bool}d delegate=%s"
+ "%s reason=%s, failed: routeLineSupport.ownsNavigation is false"
+ "%s reason=%s, failed: routeSharingState.supportsRouteSharing is false"
+ "%s reason=%s, forcing userEnabled"
+ "%s reason=%s, not touching userEnabled"
+ "%s reason=%s, userEnabled is already true"
+ "%s sending routeLine.identifier %s"
+ "%s: enabled=%{public}@"
+ "%s: ownsNavigation=%{public}@ routeLine=%@"
+ "%s: routeLine=%{public}p"
+ "-[CPNavigationManager _sendRouteLine]"
+ "-[CPNavigationManager setRouteLine:]"
+ "-[CPNavigationManager vehicleStateManager:didUpdateRouteSharingEnabled:]"
+ "<RouteSharingState: enabled="
+ "?"
+ "@\"<CPBridgeNavigationWaypoint>\"16@0:8"
+ "@\"CAFCarManager\""
+ "@\"CPNavigationWaypoint\""
+ "@\"CPRouteLine\""
+ "@\"CPVehicleStateManager\""
+ "@44@0:8@16I24^{?=ddd}28Q36"
+ "@44@0:8C16@20@28@36"
+ "@48@0:8@16@24^{?=ddd}32Q40"
+ "@76@0:8{?=ddd}16I40@44@52^{?=ddd}60Q68"
+ "CAFCarManagerObserver"
+ "CAFCarObserver"
+ "CAFRouteObserver"
+ "CAFServiceObserver"
+ "CPBridgeNavigationWaypoint"
+ "CPBridgeRouteLeg"
+ "CPBridgeRouteLine"
+ "CPNavForceUserEnabled"
+ "CPNavTool"
+ "CPNavigationWaypoint"
+ "CPRouteLeg"
+ "CPRouteLine"
+ "CPVehicleStateManager"
+ "CPVehicleStateManagerDelegate"
+ "CarPlay1"
+ "CarPlay2"
+ "CarPlay3"
+ "CarPlay_Bridging.CPVehicleStateManager"
+ "I16@0:8"
+ "SwiftRouteBridge"
+ "T@\"<CPBridgeNavigationWaypoint>\",R,N"
+ "T@\"<CPVehicleStateManagerDelegate>\",N,W,Vdelegate"
+ "T@\"CAFCar\",N,R"
+ "T@\"CAFCarManager\",N,R,VcarManager"
+ "T@\"CAFCarManager\",R,N"
+ "T@\"CAFNavigation\",N,R"
+ "T@\"CAFRoute\",N,R"
+ "T@\"CPNavigationWaypoint\",R,N,V_destinationLocation"
+ "T@\"CPNavigationWaypoint\",R,N,V_originLocation"
+ "T@\"CPRouteLine\",&,N,V_routeLine"
+ "T@\"CPRouteLine\",R,N,V_routeLine"
+ "T@\"CPVehicleStateManager\",&,N,V_vehicleStateManager"
+ "T@\"NSArray\",R,N,V_routeLegs"
+ "T@\"NSString\",R,N,V_address"
+ "T@\"NSString\",R,N,V_name"
+ "T@\"NSUUID\",R,N"
+ "TB,R,N,V_routeSharingActive"
+ "TC,R,N,V_geodeticSystem"
+ "TI,R,N"
+ "TI,R,N,V_locationThreshold"
+ "TQ,R,N,V_coordinates3DCount"
+ "TQ,R,N,V_entryPointsCount"
+ "T^{?=ddd},R,N"
+ "T^{?=ddd},R,N,V_coordinates3D"
+ "T^{?=ddd},R,N,V_entryPoints"
+ "T{?=ddd},R,N"
+ "T{?=ddd},R,N,V_centerPoint"
+ "^{?=ddd}"
+ "^{?=ddd}16@0:8"
+ "_TtC7CarPlay17RouteSharingState"
+ "_address"
+ "_centerPoint"
+ "_coordinates3D"
+ "_coordinates3DCount"
+ "_destinationLocation"
+ "_entryPoints"
+ "_entryPointsCount"
+ "_geodeticSystem"
+ "_locationThreshold"
+ "_originLocation"
+ "_routeLegs"
+ "_routeLine"
+ "_routeSharingActive"
+ "_sendRouteLine"
+ "_vehicleStateManager"
+ "address"
+ "altitude"
+ "carDidUpdate:accessory:service:characteristic:"
+ "carDidUpdate:accessory:service:control:"
+ "carDidUpdate:receivedAllValues:"
+ "carDidUpdateAccessories:"
+ "carManager"
+ "carManager:didUpdateCurrentCar:"
+ "centerPoint"
+ "clearRoute"
+ "clearRouteLine"
+ "coordinate"
+ "coordinates3D"
+ "coordinates3DCount"
+ "currentCar"
+ "dataWithBytes:length:"
+ "decodeArrayOfObjectsOfClass:forKey:"
+ "decodeInt32ForKey:"
+ "destinationLocation"
+ "didSet ownsNavigation= %s oldValue=%s"
+ "didSet supportsRouteSharing: %{bool}d"
+ "didUpdateLastNavigatingBundleIdentifier:"
+ "didUpdateNavigationOwnership"
+ "didUpdateNavigationOwnership()"
+ "didUpdateRouteSharingActive:"
+ "encodeInt32:forKey:"
+ "entryPoints"
+ "entryPointsCount"
+ "forceUserEnabledIfAllowed(reason:)"
+ "fullAddress"
+ "geodeticSystem"
+ "getBytes:length:"
+ "init()"
+ "initWithAltitude:latitude:longitude:"
+ "initWithCenterPoint:locationThreshold:name:address:entryPoints:entryPointsCount:"
+ "initWithCoordinates:destination:origin:"
+ "initWithDictionary:"
+ "initWithEntryPoints:location:locationThreshold:userVisibleAddress:userVisibleName:"
+ "initWithGeodeticSystem:origin:destination:routeLegs:"
+ "initWithGeodeticSystem:originLocation:destinationLocation:routeLegs:"
+ "initWithMapItem:locationThreshold:entryPoints:entryPointsCount:"
+ "initWithOrigin:destination:coordinates3D:coordinates3DCount:"
+ "initWithOriginLocation:destinationLocation:coordinates3D:coordinates3DCount:"
+ "initWithRouteGuidance:maneuvers:laneGuidances:routeLine:"
+ "isEqualToRouteLine:"
+ "kCPNavigationWaypointAddressKey"
+ "kCPNavigationWaypointCenterPointKey"
+ "kCPNavigationWaypointEntryPointsKey"
+ "kCPNavigationWaypointLocationThresholdKey"
+ "kCPNavigationWaypointNameKey"
+ "kCPRouteInfoRouteLineKey"
+ "kCPRouteLegCoordinates3DKey"
+ "kCPRouteLegDestinationKey"
+ "kCPRouteLegOriginKey"
+ "kCPRouteLineDestinationKey"
+ "kCPRouteLineGeodeticSystemKey"
+ "kCPRouteLineIdentifier"
+ "kCPRouteLineOriginKey"
+ "kCPRouteLineRouteLegsKey"
+ "lastIdentifier"
+ "locationThreshold"
+ "navigation"
+ "originLocation"
+ "route"
+ "routeLegs"
+ "routeLegsWithArray:"
+ "routeLegsWithRouteLegs:"
+ "routeLine"
+ "routeService:didUpdateApplicationEnabled:"
+ "routeService:didUpdateDestination:"
+ "routeService:didUpdateGeodeticSystem:"
+ "routeService:didUpdateLegs:"
+ "routeService:didUpdateOrigin:"
+ "routeService:didUpdateRouteState:"
+ "routeService:didUpdateUserEnabled:"
+ "routeService:didUpdateUserVisibleApplicationName:"
+ "routeService:didUpdateVehicleEnabled:"
+ "routeSharingActive"
+ "routeSharingState"
+ "sendGuidanceState:"
+ "sendRouteLine:"
+ "serviceDidFinishGroupUpdate:"
+ "serviceDidUpdate:characteristic:fromGroupUpdate:"
+ "serviceDidUpdate:control:"
+ "serviceDidUpdate:receivedAllValues:"
+ "setApplicationEnabled:"
+ "setDestination:"
+ "setGeodeticSystem:"
+ "setLegs:"
+ "setOrigin:"
+ "setRouteLine:"
+ "setRouteState:"
+ "setSupportsRouteSharing"
+ "setSupportsRouteSharing:"
+ "setUserEnabled:"
+ "setUserVisibleApplicationName:"
+ "setVehicleStateManager:"
+ "supportsRouteSharing"
+ "updateNavigationOwnership"
+ "userEnabled"
+ "v24@0:8@\"CAFCar\"16"
+ "v24@0:8@\"CAFService\"16"
+ "v28@0:8@\"CAFCar\"16B24"
+ "v28@0:8@\"CAFRoute\"16B24"
+ "v28@0:8@\"CAFRoute\"16C24"
+ "v28@0:8@\"CAFService\"16B24"
+ "v28@0:8@\"CPVehicleStateManager\"16B24"
+ "v32@0:8@\"CAFCarManager\"16@\"CAFCar\"24"
+ "v32@0:8@\"CAFRoute\"16@\"CAFPointOfInterest\"24"
+ "v32@0:8@\"CAFRoute\"16@\"CAFRouteLegs\"24"
+ "v32@0:8@\"CAFRoute\"16@\"NSString\"24"
+ "v32@0:8@\"CAFService\"16@\"CAFControl\"24"
+ "v36@0:8@\"CAFService\"16@\"CAFCharacteristic\"24B32"
+ "v36@0:8@16@24B32"
+ "v48@0:8@\"CAFCar\"16@\"CAFAccessory\"24@\"CAFService\"32@\"CAFCharacteristic\"40"
+ "v48@0:8@\"CAFCar\"16@\"CAFAccessory\"24@\"CAFService\"32@\"CAFControl\"40"
+ "v48@0:8@16@24@32@40"
+ "vehicleEnabled"
+ "vehicleStateManager"
+ "vehicleStateManager:didUpdateRouteSharingEnabled:"
+ "willReleaseNavigationOwnership"
+ "willReleaseNavigationOwnership()"
+ "{?=\"latitude\"d\"longitude\"d\"altitude\"d}"
+ "{?=ddd}16@0:8"

```
