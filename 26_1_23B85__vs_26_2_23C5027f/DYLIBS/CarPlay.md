## CarPlay

> `/System/Library/Frameworks/CarPlay.framework/CarPlay`

```diff

-488.18.3.2.0
-  __TEXT.__text: 0x4ee18
-  __TEXT.__auth_stubs: 0xb30
-  __TEXT.__objc_methlist: 0x78d8
-  __TEXT.__const: 0x338
-  __TEXT.__cstring: 0x431b
-  __TEXT.__oslogstring: 0x22bb
-  __TEXT.__gcc_except_tab: 0x890
-  __TEXT.__swift5_typeref: 0xad
-  __TEXT.__constg_swiftt: 0xe4
-  __TEXT.__swift5_reflstr: 0x43
-  __TEXT.__swift5_fieldmd: 0x4c
+488.25.0.0.0
+  __TEXT.__text: 0x51fac
+  __TEXT.__auth_stubs: 0xb20
+  __TEXT.__objc_methlist: 0x7d58
+  __TEXT.__const: 0x342
+  __TEXT.__cstring: 0x499b
+  __TEXT.__oslogstring: 0x254d
+  __TEXT.__gcc_except_tab: 0x89c
+  __TEXT.__swift5_typeref: 0x96
+  __TEXT.__constg_swiftt: 0x10c
+  __TEXT.__swift5_reflstr: 0x7c
+  __TEXT.__swift5_fieldmd: 0x58
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x1948
-  __TEXT.__objc_classname: 0x10c4
-  __TEXT.__objc_methname: 0xf20b
-  __TEXT.__objc_methtype: 0x2622
-  __TEXT.__objc_stubs: 0x9120
-  __DATA_CONST.__got: 0x688
-  __DATA_CONST.__const: 0x1bc0
-  __DATA_CONST.__objc_classlist: 0x350
-  __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x298
+  __TEXT.__unwind_info: 0x19f8
+  __TEXT.__objc_classname: 0x1134
+  __TEXT.__objc_methname: 0xffdf
+  __TEXT.__objc_methtype: 0x27c1
+  __TEXT.__objc_stubs: 0x97e0
+  __DATA_CONST.__got: 0x698
+  __DATA_CONST.__const: 0x1c48
+  __DATA_CONST.__objc_classlist: 0x358
+  __DATA_CONST.__objc_catlist: 0x40
+  __DATA_CONST.__objc_protolist: 0x2c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x33a8
-  __DATA_CONST.__objc_protorefs: 0x140
-  __DATA_CONST.__objc_superrefs: 0x2a8
-  __AUTH_CONST.__auth_got: 0x5a8
-  __AUTH_CONST.__const: 0x8e1
-  __AUTH_CONST.__cfstring: 0x40a0
-  __AUTH_CONST.__objc_const: 0x1bc20
+  __DATA_CONST.__objc_selrefs: 0x3658
+  __DATA_CONST.__objc_protorefs: 0x158
+  __DATA_CONST.__objc_superrefs: 0x2b0
+  __AUTH_CONST.__auth_got: 0x5a0
+  __AUTH_CONST.__const: 0x928
+  __AUTH_CONST.__cfstring: 0x42c0
+  __AUTH_CONST.__objc_const: 0x1c4f8
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x1b00
-  __AUTH.__data: 0x188
-  __DATA.__objc_ivar: 0x7ec
-  __DATA.__data: 0x1d30
+  __AUTH.__objc_data: 0x1b50
+  __AUTH.__data: 0x1b8
+  __DATA.__objc_ivar: 0x820
+  __DATA.__data: 0x1e40
   __DATA.__bss: 0x2b0
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x640

   - /System/Library/PrivateFrameworks/GraphicsServices.framework/GraphicsServices
   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /System/Library/PrivateFrameworks/UIFoundation.framework/UIFoundation
+  - /System/Library/PrivateFrameworks/UserAlerts.framework/UserAlerts
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 8E879487-1507-34C2-A951-487A977E51C6
-  Functions: 2600
-  Symbols:   9712
-  CStrings:  4353
+  UUID: 492B4D47-5880-3C41-9CF4-15D60EB879F2
+  Functions: 2725
+  Symbols:   10049
+  CStrings:  4566
 
Symbols:
+ -[CPNavigationManager _showRouteSharingPopoverForVehicle:]
+ -[CPNavigationManager _showRouteSharingPopoverForVehicle:].cold.1
+ -[CPNavigationManager _showRouteSharingPopoverIfNecessaryForVehicle:]
+ -[CPNavigationManager _vehicleForCurrentSession]
+ -[CPNavigationManager alertPresenter]
+ -[CPNavigationManager currentSession]
+ -[CPNavigationManager initWithIdentifier:delegate:sessionStatus:]
+ -[CPNavigationManager navigatingCount]
+ -[CPNavigationManager navigationAidedDrivingActive]
+ -[CPNavigationManager pairedVehicleManager]
+ -[CPNavigationManager routeSharingUserEnabled]
+ -[CPNavigationManager routeSharingVehicleEnabled]
+ -[CPNavigationManager routeSource]
+ -[CPNavigationManager sessionDidConnect:]
+ -[CPNavigationManager sessionDidConnect:].cold.1
+ -[CPNavigationManager sessionDidDisconnect:]
+ -[CPNavigationManager sessionDidDisconnect:].cold.1
+ -[CPNavigationManager sessionStatus]
+ -[CPNavigationManager setCurrentSession:]
+ -[CPNavigationManager setNavigatingCount:]
+ -[CPNavigationManager setSessionStatus:]
+ -[CPNavigationManager setShowingRouteSharingPopup:]
+ -[CPNavigationManager setSystemInfo:]
+ -[CPNavigationManager sharingConsentChanged:]
+ -[CPNavigationManager showingRouteSharingPopup]
+ -[CPNavigationManager systemInfo]
+ -[CPNavigationManager userRouteSharingStatus]
+ -[CPNavigationManager userRouteSharingStatus].cold.1
+ -[CPNavigationManager vehicleStateManager:didUpdateNavigationAidedDrivingActive:]
+ -[CPNavigationManager vehicleStateManager:didUpdateRouteSharingActive:]
+ -[CPNavigationManager vehicleStateManager:didUpdateRouteSharingActive:].cold.1
+ -[CPNavigationManager vehicleStateManager:didUpdateRouteSharingUserEnabled:]
+ -[CPNavigationManager vehicleStateManager:didUpdateRouteSharingUserEnabled:].cold.1
+ -[CPNavigationManager vehicleStateManager:didUpdateRouteSharingVehicleEnabled:]
+ -[CPNavigationManager vehicleStateManager:didUpdateRouteSharingVehicleEnabled:].cold.1
+ -[CPNavigationManager vehicleStateManager:didUpdateRouteSource:]
+ -[CPNavigationManager vehicleStateManager:didUpdateRouteSource:].cold.1
+ -[CPNavigationManager vehicleStateManager:didUpdateSystemInfo:]
+ -[CPNavigationManager vehicleStateManager:didUpdateSystemInfo:].cold.1
+ -[CPNavigationSystemInfo .cxx_destruct]
+ -[CPNavigationSystemInfo brand]
+ -[CPNavigationSystemInfo initWithModel:brand:manufacturer:navigationName:nadFeatureLongName:nadFeatureShortName:]
+ -[CPNavigationSystemInfo manufacturer]
+ -[CPNavigationSystemInfo model]
+ -[CPNavigationSystemInfo name]
+ -[CPNavigationSystemInfo navigationAidedDrivingFeatureName]
+ -[CPNavigationSystemInfo navigationAidedDrivingFeatureShortName]
+ -[CPNavigationSystemInfo navigationName]
+ -[CPNavigationSystemInfo(SwiftRouteBridge) initWithBridge:]
+ -[CPRouteInfo routeLineUnavailableForRegion]
+ -[CPRouteInfo setRouteLineUnavailableForRegion:]
+ GCC_except_table2
+ GCC_except_table80
+ _$s10Foundation4UUIDVSgWOc
+ _$s10Foundation4UUIDVSgWOh
+ _$s2os0A11LogInternal_3log4typeyAA12OSLogMessageV_So03OS_a1_D0CSo0a1_d1_E2_tatFyySpys5UInt8VGz_SpySo8NSObjectCSgGSgzSpyypGSgztcXEfU_
+ _$s2os14OSLogArgumentsV6appendyySSycFySpys5UInt8VGz_SpySo8NSObjectCSgGSgzSpyypGSgztcfU_
+ _$s2os14OSLogArgumentsV6appendyys5UInt8VFySpyAFGz_SpySo8NSObjectCSgGSgzSpyypGSgztcfU_
+ _$s2os18OSLogInterpolationV06appendC0_5align7privacyySSyXA_AA0B15StringAlignmentVAA0B7PrivacyVtFSSycfu_
+ _$s2os18OSLogInterpolationV06appendC0_6format7privacyySbyXA_AA0B10BoolFormatOAA0B7PrivacyVtFs5Int32Vycfu_
+ _$s2os18OSLogInterpolationV06appendC0_6format7privacyys5Int32VyXA_AA0bG14ExtendedFormatOAA0B7PrivacyVtFAHycfu_
+ _$s2os9serialize_2atys5UInt8V_SpyAEGztF
+ _$s2os9serialize_2atyx_Spys5UInt8VGzts17FixedWidthIntegerRzlFySWXEfU_
+ _$s7CarPlay17RouteSharingStateC05routeD0So08CAFRouteD0CSgvMTq
+ _$s7CarPlay17RouteSharingStateC05routeD0So08CAFRouteD0CSgvgTq
+ _$s7CarPlay17RouteSharingStateC05routeD0So08CAFRouteD0CSgvpWvd
+ _$s7CarPlay17RouteSharingStateC05routeD0So08CAFRouteD0CSgvsTq
+ _$s7CarPlay17RouteSharingStateC11userEnabledSbvMTq
+ _$s7CarPlay17RouteSharingStateC11userEnabledSbvs
+ _$s7CarPlay17RouteSharingStateC11userEnabledSbvsTq
+ _$s7CarPlay17RouteSharingStateC29routeLineUnavailableForRegionSbvMTq
+ _$s7CarPlay17RouteSharingStateC29routeLineUnavailableForRegionSbvW
+ _$s7CarPlay17RouteSharingStateC29routeLineUnavailableForRegionSbvgTq
+ _$s7CarPlay17RouteSharingStateC29routeLineUnavailableForRegionSbvpWvd
+ _$s7CarPlay17RouteSharingStateC29routeLineUnavailableForRegionSbvsTq
+ _$sSo13CAFRouteStateV7CarPlayE13sharingStatus3forSo010CAFSharingB0VAC012RouteSharingB0C_tF
+ _$sSo20CAFSystemInformationC7CarPlayE14cpBridgedBrandSSvg
+ _$sSo20CAFSystemInformationC7CarPlayE14cpBridgedBrandSSvgTo
+ _$sSo20CAFSystemInformationC7CarPlayE14cpBridgedBrandSSvpMV
+ _$sSo20CAFSystemInformationC7CarPlayE14cpBridgedModelSSvg
+ _$sSo20CAFSystemInformationC7CarPlayE14cpBridgedModelSSvgTm
+ _$sSo20CAFSystemInformationC7CarPlayE14cpBridgedModelSSvgTo
+ _$sSo20CAFSystemInformationC7CarPlayE14cpBridgedModelSSvgToTm
+ _$sSo20CAFSystemInformationC7CarPlayE14cpBridgedModelSSvpMV
+ _$sSo20CAFSystemInformationC7CarPlayE21cpBridgedManufacturerSSvg
+ _$sSo20CAFSystemInformationC7CarPlayE21cpBridgedManufacturerSSvgTo
+ _$sSo20CAFSystemInformationC7CarPlayE21cpBridgedManufacturerSSvpMV
+ _$sSo20CAFSystemInformationC7CarPlayE23cpBridgedNavigationNameSSvg
+ _$sSo20CAFSystemInformationC7CarPlayE23cpBridgedNavigationNameSSvgTo
+ _$sSo20CAFSystemInformationC7CarPlayE23cpBridgedNavigationNameSSvpMV
+ _$sSo20CAFSystemInformationC7CarPlayE42cpBridgedNavigationAidedDrivingFeatureNameSSSgvg
+ _$sSo20CAFSystemInformationC7CarPlayE42cpBridgedNavigationAidedDrivingFeatureNameSSSgvgTm
+ _$sSo20CAFSystemInformationC7CarPlayE42cpBridgedNavigationAidedDrivingFeatureNameSSSgvgTo
+ _$sSo20CAFSystemInformationC7CarPlayE42cpBridgedNavigationAidedDrivingFeatureNameSSSgvgToTm
+ _$sSo20CAFSystemInformationC7CarPlayE42cpBridgedNavigationAidedDrivingFeatureNameSSSgvpMV
+ _$sSo20CAFSystemInformationC7CarPlayE47cpBridgedNavigationAidedDrivingFeatureShortNameSSSgvg
+ _$sSo20CAFSystemInformationC7CarPlayE47cpBridgedNavigationAidedDrivingFeatureShortNameSSSgvgTo
+ _$sSo20CAFSystemInformationC7CarPlayE47cpBridgedNavigationAidedDrivingFeatureShortNameSSSgvpMV
+ _$sSo21CPVehicleStateManagerC7CarPlayE10systemInfoSo024CPBridgeNavigationSystemG0_pSgvgTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE11routeSourceSo013CPBridgeRouteG0VvgTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE11routeStatus33_8CF23B4C98753B3B7E23CE4A41E0DBB4LLSo08CAFRouteG0CSgvgTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE12routeSharing33_8CF23B4C98753B3B7E23CE4A41E0DBB4LLSo08CAFRouteG0CSgvgTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE15clearNavigation33_8CF23B4C98753B3B7E23CE4A41E0DBB4LLyyF
+ _$sSo21CPVehicleStateManagerC7CarPlayE15clearNavigation33_8CF23B4C98753B3B7E23CE4A41E0DBB4LLyyFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE17systemInformation33_8CF23B4C98753B3B7E23CE4A41E0DBB4LLSo09CAFSystemG0CSgvgTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE17systemInformation33_8CF23B4C98753B3B7E23CE4A41E0DBB4LLSo09CAFSystemG0CSgvgToTm
+ _$sSo21CPVehicleStateManagerC7CarPlayE18routeSharingActiveSbvg
+ _$sSo21CPVehicleStateManagerC7CarPlayE18routeSharingActiveSbvgTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE18routeStatusService_014didUpdateRouteB0ySo08CAFRouteG0C_So0lB0VtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE18routeStatusService_014didUpdateRouteB0ySo08CAFRouteG0C_So0lB0VtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE18routeStatusService_15didUpdateOriginySo08CAFRouteG0C_So18CAFPointOfInterestCSgtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE18routeStatusService_15didUpdateOriginySo08CAFRouteG0C_So18CAFPointOfInterestCSgtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE18routeStatusService_20didUpdateDestinationySo08CAFRouteG0C_So18CAFPointOfInterestCSgtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE18routeStatusService_20didUpdateDestinationySo08CAFRouteG0C_So18CAFPointOfInterestCSgtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE18routeStatusService_22didUpdateRerouteReasonySo08CAFRouteG0C_So010CAFRerouteL0VtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE18routeStatusService_22didUpdateRerouteReasonySo08CAFRouteG0C_So010CAFRerouteL0VtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE18routeStatusService_23didUpdateGeodeticSystemySo08CAFRouteG0C_So011CAFGeodeticL0VtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE18routeStatusService_23didUpdateGeodeticSystemySo08CAFRouteG0C_So011CAFGeodeticL0VtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE18routeStatusService_35didUpdateUserVisibleApplicationNameySo08CAFRouteG0C_SSSgtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE18routeStatusService_35didUpdateUserVisibleApplicationNameySo08CAFRouteG0C_SSSgtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE19routeSharingService_09didUpdategB0ySo08CAFRouteG0C_So010CAFSharingB0VtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE19routeSharingService_09didUpdategB0ySo08CAFRouteG0C_So010CAFSharingB0VtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE19routeSharingService_13didUpdateLegsySo08CAFRouteG0C_So0lK0CSgtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE19routeSharingService_13didUpdateLegsySo08CAFRouteG0C_So0lK0CSgtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE19routeSharingService_20didUpdateUserEnabledySo08CAFRouteG0C_SbtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE19routeSharingService_20didUpdateUserEnabledySo08CAFRouteG0C_SbtFTm
+ _$sSo21CPVehicleStateManagerC7CarPlayE19routeSharingService_20didUpdateUserEnabledySo08CAFRouteG0C_SbtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE19routeSharingService_20didUpdateUserEnabledySo08CAFRouteG0C_SbtFToTm
+ _$sSo21CPVehicleStateManagerC7CarPlayE19routeSharingService_23didUpdateVehicleEnabledySo08CAFRouteG0C_SbtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE19routeSharingService_23didUpdateVehicleEnabledySo08CAFRouteG0C_SbtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE19routeSharingService_26didUpdateUserVisibleReasonySo08CAFRouteG0C_SStF
+ _$sSo21CPVehicleStateManagerC7CarPlayE19routeSharingService_26didUpdateUserVisibleReasonySo08CAFRouteG0C_SStFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE19routeSharingService_27didUpdateApplicationEnabledySo08CAFRouteG0C_SbtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE19routeSharingService_27didUpdateApplicationEnabledySo08CAFRouteG0C_SbtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE23carDidUpdateAccessoriesyySo6CAFCarCFTf4dn_n
+ _$sSo21CPVehicleStateManagerC7CarPlayE23routeSharingUserEnabledSbvgTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE24systemInformationService_20didUpdateRouteSourceySo09CAFSystemG0C_So08CAFRouteL0VtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE24systemInformationService_20didUpdateRouteSourceySo09CAFSystemG0C_So08CAFRouteL0VtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE24systemInformationService_32didUpdateUserVisibleVehicleBrandySo09CAFSystemG0C_SStF
+ _$sSo21CPVehicleStateManagerC7CarPlayE24systemInformationService_32didUpdateUserVisibleVehicleBrandySo09CAFSystemG0C_SStFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE24systemInformationService_32didUpdateUserVisibleVehicleModelySo09CAFSystemG0C_SStF
+ _$sSo21CPVehicleStateManagerC7CarPlayE24systemInformationService_32didUpdateUserVisibleVehicleModelySo09CAFSystemG0C_SStFTm
+ _$sSo21CPVehicleStateManagerC7CarPlayE24systemInformationService_32didUpdateUserVisibleVehicleModelySo09CAFSystemG0C_SStFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE24systemInformationService_32didUpdateUserVisibleVehicleModelySo09CAFSystemG0C_SStFToTm
+ _$sSo21CPVehicleStateManagerC7CarPlayE24systemInformationService_37didUpdateNavigationAidedDrivingActiveySo09CAFSystemG0C_SbtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE24systemInformationService_37didUpdateNavigationAidedDrivingActiveySo09CAFSystemG0C_SbtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE24systemInformationService_39didUpdateUserVisibleVehicleManufacturerySo09CAFSystemG0C_SStF
+ _$sSo21CPVehicleStateManagerC7CarPlayE24systemInformationService_39didUpdateUserVisibleVehicleManufacturerySo09CAFSystemG0C_SStFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE24systemInformationService_40didUpdateUserVisibleNavigationSystemNameySo09CAFSystemG0C_SStF
+ _$sSo21CPVehicleStateManagerC7CarPlayE24systemInformationService_40didUpdateUserVisibleNavigationSystemNameySo09CAFSystemG0C_SStFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE24systemInformationService_53didUpdateUserVisibleNavigationAidedDrivingFeatureNameySo09CAFSystemG0C_SSSgtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE24systemInformationService_53didUpdateUserVisibleNavigationAidedDrivingFeatureNameySo09CAFSystemG0C_SSSgtFTm
+ _$sSo21CPVehicleStateManagerC7CarPlayE24systemInformationService_53didUpdateUserVisibleNavigationAidedDrivingFeatureNameySo09CAFSystemG0C_SSSgtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE24systemInformationService_58didUpdateUserVisibleNavigationAidedDrivingFeatureShortNameySo09CAFSystemG0C_SSSgtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE24systemInformationService_58didUpdateUserVisibleNavigationAidedDrivingFeatureShortNameySo09CAFSystemG0C_SSSgtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE26routeSharingVehicleEnabledSbvgTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE28navigationAidedDrivingActiveSbvgTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE28navigationAidedDrivingActiveSbvgToTm
+ _$sSo21CPVehicleStateManagerC7CarPlayE29routeLineUnavailableForRegionSbvgTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE29routeLineUnavailableForRegionSbvsTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE30willReleaseNavigationOwnership9lastOwnerySb_tF
+ _$sSo21CPVehicleStateManagerC7CarPlayE30willReleaseNavigationOwnership9lastOwnerySb_tFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE31didUpdateUserRouteSharingStatusyyF
+ _$sSo21CPVehicleStateManagerC7CarPlayE31didUpdateUserRouteSharingStatusyyFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE4send08guidanceB0ySo016CPBridgeGuidanceB0V_tF
+ _$sSo21CPVehicleStateManagerC7CarPlayE4send08guidanceB0ySo016CPBridgeGuidanceB0V_tFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE4send13rerouteReasonySo015CPBridgeRerouteH0V_tF
+ _$sSo21CPVehicleStateManagerC7CarPlayE4send13rerouteReasonySo015CPBridgeRerouteH0V_tFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE4send9routeLineySo013CPBridgeRouteH0_pSg_tF
+ _$sSo21CPVehicleStateManagerC7CarPlayE4send9routeLineySo013CPBridgeRouteH0_pSg_tFTo
+ _$sSo26CRBridgeRouteSharingStatusVSYSCSY8rawValue03RawF0QzvgTW
+ _$ss5Int32VIegd_ABIegr_TR
+ _CRLocalizedStringForKey
+ _NSStringFromCPRouteSource
+ _NSStringFromRouteState
+ _NSStringFromSharingState
+ _OBJC_CLASS_$_CAFSystemInformation
+ _OBJC_CLASS_$_CPNavigationSystemInfo
+ _OBJC_CLASS_$_CRPairedVehicleManager
+ _OBJC_CLASS_$_NSDistributedNotificationCenter
+ _OBJC_CLASS_$_URTAlert
+ _OBJC_CLASS_$_URTAlertAction
+ _OBJC_CLASS_$_URTAlertPresenter
+ _OBJC_IVAR_$_CPNavigationManager._alertPresenter
+ _OBJC_IVAR_$_CPNavigationManager._currentSession
+ _OBJC_IVAR_$_CPNavigationManager._navigatingCount
+ _OBJC_IVAR_$_CPNavigationManager._pairedVehicleManager
+ _OBJC_IVAR_$_CPNavigationManager._sessionStatus
+ _OBJC_IVAR_$_CPNavigationManager._showingRouteSharingPopup
+ _OBJC_IVAR_$_CPNavigationManager._systemInfo
+ _OBJC_IVAR_$_CPNavigationSystemInfo._brand
+ _OBJC_IVAR_$_CPNavigationSystemInfo._manufacturer
+ _OBJC_IVAR_$_CPNavigationSystemInfo._model
+ _OBJC_IVAR_$_CPNavigationSystemInfo._navigationAidedDrivingFeatureName
+ _OBJC_IVAR_$_CPNavigationSystemInfo._navigationAidedDrivingFeatureShortName
+ _OBJC_IVAR_$_CPNavigationSystemInfo._navigationName
+ _OBJC_IVAR_$_CPRouteInfo._routeLineUnavailableForRegion
+ _OBJC_METACLASS_$_CPNavigationSystemInfo
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __CATEGORY_CAFSystemInformation_$_CarPlay
+ __CATEGORY_INSTANCE_METHODS_CAFSystemInformation_$_CarPlay
+ __CATEGORY_PROPERTIES_CAFSystemInformation_$_CarPlay
+ __CATEGORY_PROTOCOLS_CAFSystemInformation_$_CarPlay
+ __OBJC_$_CLASS_METHODS_CPManeuver(CRAccNavInfo|CPAccNavUpdate)
+ __OBJC_$_INSTANCE_METHODS_CPManeuver(CRAccNavInfo|CPAccNavUpdate)
+ __OBJC_$_INSTANCE_METHODS_CPNavigationSystemInfo(SwiftRouteBridge)
+ __OBJC_$_INSTANCE_METHODS_CPVehicleStateManager(CarPlay|CarPlay1|CarPlay2|CarPlay3|CarPlay4|CarPlay5)
+ __OBJC_$_INSTANCE_VARIABLES_CPNavigationSystemInfo
+ __OBJC_$_PROP_LIST_CPBridgeNavigationSystemInfo
+ __OBJC_$_PROP_LIST_CPNavigationSystemInfo
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFRouteSharingObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFRouteStatusObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFSystemInformationObserver
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPBridgeNavigationSystemInfo
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFRouteSharingObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFRouteStatusObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CAFSystemInformationObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPBridgeNavigationSystemInfo
+ __OBJC_$_PROTOCOL_REFS_CAFRouteSharingObserver
+ __OBJC_$_PROTOCOL_REFS_CAFRouteStatusObserver
+ __OBJC_$_PROTOCOL_REFS_CAFSystemInformationObserver
+ __OBJC_$_PROTOCOL_REFS_CPBridgeNavigationSystemInfo
+ __OBJC_CLASS_PROTOCOLS_$_CPManeuver(CRAccNavInfo|CPAccNavUpdate)
+ __OBJC_CLASS_PROTOCOLS_$_CPVehicleStateManager(CarPlay|CarPlay1|CarPlay2|CarPlay3|CarPlay4|CarPlay5)
+ __OBJC_CLASS_RO_$_CPNavigationSystemInfo
+ __OBJC_LABEL_PROTOCOL_$_CAFRouteSharingObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFRouteStatusObserver
+ __OBJC_LABEL_PROTOCOL_$_CAFSystemInformationObserver
+ __OBJC_LABEL_PROTOCOL_$_CPBridgeNavigationSystemInfo
+ __OBJC_METACLASS_RO_$_CPNavigationSystemInfo
+ __OBJC_PROTOCOL_$_CAFRouteSharingObserver
+ __OBJC_PROTOCOL_$_CAFRouteStatusObserver
+ __OBJC_PROTOCOL_$_CAFSystemInformationObserver
+ __OBJC_PROTOCOL_$_CPBridgeNavigationSystemInfo
+ ___39-[CPNavigationManager _setupConnection]_block_invoke.268
+ ___39-[CPNavigationManager _setupConnection]_block_invoke.269
+ ___39-[CPNavigationManager _setupConnection]_block_invoke.271
+ ___49-[CPNavigationManager didUpdateActiveComponents:]_block_invoke.280
+ ___58-[CPNavigationManager _showRouteSharingPopoverForVehicle:]_block_invoke
+ ___58-[CPNavigationManager _showRouteSharingPopoverForVehicle:]_block_invoke.252
+ ___58-[CPNavigationManager _showRouteSharingPopoverForVehicle:]_block_invoke.252.cold.1
+ ___58-[CPNavigationManager _showRouteSharingPopoverForVehicle:]_block_invoke.260
+ ___58-[CPNavigationManager _showRouteSharingPopoverForVehicle:]_block_invoke.260.cold.1
+ ___58-[CPNavigationManager _showRouteSharingPopoverForVehicle:]_block_invoke.261
+ ___58-[CPNavigationManager _showRouteSharingPopoverForVehicle:]_block_invoke.261.cold.1
+ ___58-[CPNavigationManager _showRouteSharingPopoverForVehicle:]_block_invoke.cold.1
+ ___65-[CPNavigationManager initWithIdentifier:delegate:sessionStatus:]_block_invoke
+ ___65-[CPNavigationManager initWithIdentifier:delegate:sessionStatus:]_block_invoke.178
+ ___65-[CPNavigationManager initWithIdentifier:delegate:sessionStatus:]_block_invoke.184
+ ___65-[CPNavigationManager initWithIdentifier:delegate:sessionStatus:]_block_invoke.184.cold.1
+ ___65-[CPNavigationManager initWithIdentifier:delegate:sessionStatus:]_block_invoke.191
+ ___65-[CPNavigationManager initWithIdentifier:delegate:sessionStatus:]_block_invoke.191.cold.1
+ ___block_descriptor_32_e31_v24?0"CRVehicle"8"NSError"16l
+ ___block_descriptor_48_e8_32s40s_e24_v16?0"URTAlertAction"8ls32l8s40l8
+ ___block_literal_global.220
+ ___block_literal_global.222
+ ___block_literal_global.224
+ ___block_literal_global.227
+ ___block_literal_global.230
+ ___block_literal_global.232
+ ___block_literal_global.235
+ ___block_literal_global.237
+ ___block_literal_global.239
+ ___block_literal_global.255
+ ___block_literal_global.263
+ ___block_literal_global.274
+ _objc_msgSend$MFiCertificateSerialNumber
+ _objc_msgSend$_showRouteSharingPopoverForVehicle:
+ _objc_msgSend$_showRouteSharingPopoverIfNecessaryForVehicle:
+ _objc_msgSend$_vehicleForCurrentSession
+ _objc_msgSend$actionWithTitle:handler:
+ _objc_msgSend$addAlert:forDestination:preferringStyle:
+ _objc_msgSend$alertPresenter
+ _objc_msgSend$alertWithTitle:message:
+ _objc_msgSend$brand
+ _objc_msgSend$cpBridgedBrand
+ _objc_msgSend$cpBridgedManufacturer
+ _objc_msgSend$cpBridgedModel
+ _objc_msgSend$cpBridgedNavigationAidedDrivingFeatureName
+ _objc_msgSend$cpBridgedNavigationAidedDrivingFeatureShortName
+ _objc_msgSend$cpBridgedNavigationName
+ _objc_msgSend$didUpdateNavigationAidedDrivingActive:
+ _objc_msgSend$didUpdateRouteSharingUserEnabled:
+ _objc_msgSend$didUpdateRouteSharingVehicleEnabled:
+ _objc_msgSend$didUpdateRouteSource:
+ _objc_msgSend$didUpdateSystemInfo:
+ _objc_msgSend$didUpdateUserRouteSharingStatus
+ _objc_msgSend$hasShownRouteSharingFollowup
+ _objc_msgSend$initWithBridge:
+ _objc_msgSend$initWithIdentifier:delegate:sessionStatus:
+ _objc_msgSend$initWithModel:brand:manufacturer:navigationName:nadFeatureLongName:nadFeatureShortName:
+ _objc_msgSend$model
+ _objc_msgSend$navigatingCount
+ _objc_msgSend$navigationAidedDrivingActive
+ _objc_msgSend$oemName
+ _objc_msgSend$pairedVehicleManager
+ _objc_msgSend$present
+ _objc_msgSend$routeLineUnavailableForRegion
+ _objc_msgSend$routeSharingActive
+ _objc_msgSend$routeSharingReason
+ _objc_msgSend$routeSharingStatus
+ _objc_msgSend$routeSharingUserEnabled
+ _objc_msgSend$routeSharingVehicleEnabled
+ _objc_msgSend$routeSource
+ _objc_msgSend$saveVehicle:completion:
+ _objc_msgSend$sendRerouteReason:
+ _objc_msgSend$setAllowedApplicationBundleIDs:
+ _objc_msgSend$setCancelAction:
+ _objc_msgSend$setHasShownRouteSharingFollowup:
+ _objc_msgSend$setNavigatingCount:
+ _objc_msgSend$setOtherAction:
+ _objc_msgSend$setRouteLineUnavailableForRegion:
+ _objc_msgSend$setRouteSharingStatus:
+ _objc_msgSend$setShowingRouteSharingPopup:
+ _objc_msgSend$setSystemInfo:
+ _objc_msgSend$showingRouteSharingPopup
+ _objc_msgSend$systemInfo
+ _objc_msgSend$userRouteSharingStatus
+ _objc_msgSend$vehicleForCertificateSerial:
+ _objc_msgSend$vehicleName
+ _objc_msgSend$willReleaseNavigationOwnershipLastOwner:
+ _swift_release_n
+ _swift_retain_n
+ _symbolic So15CAFRouteSharingCSgXw
- -[CPNavigationManager vehicleStateManager:didUpdateRouteSharingEnabled:]
- -[CPNavigationManager vehicleStateManager:didUpdateRouteSharingEnabled:].cold.1
- GCC_except_table66
- _$s10Foundation4UUIDVSgWOcTm
- _$s7CarPlay17RouteSharingStateC5routeSo8CAFRouteCSgvMTq
- _$s7CarPlay17RouteSharingStateC5routeSo8CAFRouteCSgvgTq
- _$s7CarPlay17RouteSharingStateC5routeSo8CAFRouteCSgvpWvd
- _$s7CarPlay17RouteSharingStateC5routeSo8CAFRouteCSgvsTq
- _$s7CarPlay17RouteSharingStateC7enabledSbvg
- _$sSD10FoundationE19_bridgeToObjectiveCSo12NSDictionaryCyF
- _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfCs11AnyHashableV_ypTt0g5Tf4g_n
- _$sSbN
- _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_014didUpdateRouteB0ySo8CAFRouteC_So0kB0VtF
- _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_014didUpdateRouteB0ySo8CAFRouteC_So0kB0VtFTo
- _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_13didUpdateLegsySo8CAFRouteC_So0kJ0CSgtF
- _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_13didUpdateLegsySo8CAFRouteC_So0kJ0CSgtFTo
- _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_15didUpdateOriginySo8CAFRouteC_So18CAFPointOfInterestCSgtF
- _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_15didUpdateOriginySo8CAFRouteC_So18CAFPointOfInterestCSgtFTo
- _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_20didUpdateDestinationySo8CAFRouteC_So18CAFPointOfInterestCSgtF
- _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_20didUpdateDestinationySo8CAFRouteC_So18CAFPointOfInterestCSgtFTo
- _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_20didUpdateUserEnabledySo8CAFRouteC_SbtF
- _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_20didUpdateUserEnabledySo8CAFRouteC_SbtFTo
- _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_23didUpdateGeodeticSystemySo8CAFRouteC_So011CAFGeodeticK0VtF
- _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_23didUpdateGeodeticSystemySo8CAFRouteC_So011CAFGeodeticK0VtFTo
- _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_23didUpdateVehicleEnabledySo8CAFRouteC_SbtF
- _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_23didUpdateVehicleEnabledySo8CAFRouteC_SbtFTo
- _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_27didUpdateApplicationEnabledySo8CAFRouteC_SbtF
- _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_27didUpdateApplicationEnabledySo8CAFRouteC_SbtFTm
- _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_27didUpdateApplicationEnabledySo8CAFRouteC_SbtFTo
- _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_27didUpdateApplicationEnabledySo8CAFRouteC_SbtFToTm
- _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_35didUpdateUserVisibleApplicationNameySo8CAFRouteC_SSSgtF
- _$sSo21CPVehicleStateManagerC7CarPlayE12routeService_35didUpdateUserVisibleApplicationNameySo8CAFRouteC_SSSgtFTo
- _$sSo21CPVehicleStateManagerC7CarPlayE14clearRouteLine33_8CF23B4C98753B3B7E23CE4A41E0DBB4LLyyF
- _$sSo21CPVehicleStateManagerC7CarPlayE14clearRouteLine33_8CF23B4C98753B3B7E23CE4A41E0DBB4LLyyFTo
- _$sSo21CPVehicleStateManagerC7CarPlayE25forceUserEnabledIfAllowed33_8CF23B4C98753B3B7E23CE4A41E0DBB4LL6reasonyAbCE11ForceReasonAELLO_tF
- _$sSo21CPVehicleStateManagerC7CarPlayE30willReleaseNavigationOwnershipyyF
- _$sSo21CPVehicleStateManagerC7CarPlayE30willReleaseNavigationOwnershipyyFTo
- _$sSo21CPVehicleStateManagerC7CarPlayE4sendyySo016CPBridgeGuidanceB0VF
- _$sSo21CPVehicleStateManagerC7CarPlayE4sendyySo016CPBridgeGuidanceB0VFTo
- _$sSo21CPVehicleStateManagerC7CarPlayE4sendyySo17CPBridgeRouteLine_pSgF
- _$sSo21CPVehicleStateManagerC7CarPlayE4sendyySo17CPBridgeRouteLine_pSgFTo
- _$sSo21CPVehicleStateManagerC7CarPlayE5route33_8CF23B4C98753B3B7E23CE4A41E0DBB4LLSo8CAFRouteCSgvgTo
- _$ss018_bridgeAnyObjectToB0yypyXlSgF
- _$ss11AnyHashableV13_rawHashValue4seedS2i_tF
- _$ss11AnyHashableV2eeoiySbAB_ABtFZ
- _$ss11AnyHashableVMn
- _$ss11AnyHashableVN
- _$ss11AnyHashableVSHsWP
- _$ss11AnyHashableVWOc
- _$ss11AnyHashableVWOh
- _$ss11AnyHashableV_yptMR
- _$ss11AnyHashableV_yptMd
- _$ss18_DictionaryStorageC8allocate8capacityAByxq_GSi_tFZ
- _$ss18_DictionaryStorageCMn
- _$ss18_DictionaryStorageCys11AnyHashableVypGMR
- _$ss18_DictionaryStorageCys11AnyHashableVypGMd
- _$ss22__RawDictionaryStorageC4find_9hashValues10_HashTableV6BucketV6bucket_Sb5foundtx_SitSHRzlFs11AnyHashableV_Tg5
- _$ss22__RawDictionaryStorageC4findys10_HashTableV6BucketV6bucket_Sb5foundtxSHRzlFs11AnyHashableV_Tg5
- _$sypSgMR
- _$sypSgMd
- _$sypWOb
- _OBJC_IVAR_$_CPNavigationManager._routeSharingActive
- __OBJC_$_CLASS_METHODS_CPManeuver(CPAccNavUpdate|CRAccNavInfo)
- __OBJC_$_INSTANCE_METHODS_CPManeuver(CPAccNavUpdate|CRAccNavInfo)
- __OBJC_$_INSTANCE_METHODS_CPVehicleStateManager(CarPlay|CarPlay1|CarPlay2|CarPlay3)
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CAFRouteObserver
- __OBJC_$_PROTOCOL_METHOD_TYPES_CAFRouteObserver
- __OBJC_$_PROTOCOL_REFS_CAFRouteObserver
- __OBJC_CLASS_PROTOCOLS_$_CPManeuver(CPAccNavUpdate|CRAccNavInfo)
- __OBJC_CLASS_PROTOCOLS_$_CPVehicleStateManager(CarPlay|CarPlay1|CarPlay2|CarPlay3)
- __OBJC_LABEL_PROTOCOL_$_CAFRouteObserver
- __OBJC_PROTOCOL_$_CAFRouteObserver
- ___39-[CPNavigationManager _setupConnection]_block_invoke.230
- ___39-[CPNavigationManager _setupConnection]_block_invoke.231
- ___39-[CPNavigationManager _setupConnection]_block_invoke.233
- ___49-[CPNavigationManager didUpdateActiveComponents:]_block_invoke.242
- ___51-[CPNavigationManager initWithIdentifier:delegate:]_block_invoke
- ___51-[CPNavigationManager initWithIdentifier:delegate:]_block_invoke.174
- ___51-[CPNavigationManager initWithIdentifier:delegate:]_block_invoke.180
- ___51-[CPNavigationManager initWithIdentifier:delegate:]_block_invoke.180.cold.1
- ___51-[CPNavigationManager initWithIdentifier:delegate:]_block_invoke.187
- ___51-[CPNavigationManager initWithIdentifier:delegate:]_block_invoke.187.cold.1
- ___block_literal_global.202
- ___block_literal_global.206
- ___block_literal_global.208
- ___block_literal_global.210
- ___block_literal_global.213
- ___block_literal_global.218
- ___block_literal_global.221
- ___block_literal_global.223
- ___block_literal_global.225
- ___block_literal_global.236
- ___block_literal_global.249
- __swiftEmptyDictionarySingleton
- _objc_msgSend$willReleaseNavigationOwnership
- _swift_dynamicCast
- _symbolic So8CAFRouteCSgXw
- _symbolic ______ypt s11AnyHashableV
- _symbolic _____y_____ypG s18_DictionaryStorageC s11AnyHashableV
- _symbolic ypSg
CStrings:
+ " routeLineUnavailableForRegion="
+ "%@ %@"
+ "%s done"
+ "%s failed: enabled is false - %s"
+ "%s failed: identifiers match - routeLine.identifier=%s  lastRouteLineIdentifier=%s"
+ "%s failed: ownsNavigation is false"
+ "%s failed: routeSharing or routeStatus is nil"
+ "%s failed: routeStatus is nil"
+ "%s guidanceState=%hhu"
+ "%s ownsNavigation=%{bool}d lastOwner=%{bool}d"
+ "%s rerouteReason=%hhu"
+ "%s routeState=%s supportsRouteSharing=%{bool}d routeLineUnavailableForRegion=%{bool}d lastIdentifier=%s -> %s"
+ "%s start"
+ "%s userEnabled=%{bool}d delegate=%s userRouteSharingStatus=%s"
+ "%s: ownsNavigation=%{public}@ routeLine=%@ hasPresentedPopover=%{public}@ limitedUI=%{public}@ showingPopup=%{public}@"
+ "%s: routeSharingActive=%{public}@"
+ "%s: routeSource=%{public}@"
+ "%s: session=%{public}@"
+ "%s: systemInfo=%{public}@"
+ "%s: vehicle=%{public}@ session=%{public}@ routeSharingStatus=%lu"
+ "-[CPNavigationManager _showRouteSharingPopoverIfNecessaryForVehicle:]"
+ "-[CPNavigationManager sessionDidConnect:]"
+ "-[CPNavigationManager sessionDidDisconnect:]"
+ "-[CPNavigationManager userRouteSharingStatus]"
+ "-[CPNavigationManager vehicleStateManager:didUpdateRouteSharingActive:]"
+ "-[CPNavigationManager vehicleStateManager:didUpdateRouteSharingUserEnabled:]"
+ "-[CPNavigationManager vehicleStateManager:didUpdateRouteSharingVehicleEnabled:]"
+ "-[CPNavigationManager vehicleStateManager:didUpdateRouteSource:]"
+ "-[CPNavigationManager vehicleStateManager:didUpdateSystemInfo:]"
+ "@\"CARSession\""
+ "@\"CPNavigationSystemInfo\""
+ "@\"CRPairedVehicleManager\""
+ "@\"URTAlertPresenter\""
+ "CAFRouteSharingObserver"
+ "CAFRouteStatusObserver"
+ "CAFSystemInformationObserver"
+ "CPBridgeNavigationSystemInfo"
+ "CPNavigationSystemInfo"
+ "CRPairedVehiclesDidChangeNotification"
+ "CRRouteSharingConsentDidChangeNotificationName"
+ "CarPlay4"
+ "CarPlay5"
+ "Error saving Route Sharing acceptance to vehicle: %@"
+ "Error saving Route Sharing decline to vehicle: %@"
+ "Forced"
+ "Inactive"
+ "MFiCertificateSerialNumber"
+ "ROUTE_SHARING_POPUP_ACCEPT"
+ "ROUTE_SHARING_POPUP_DECLINE"
+ "ROUTE_SHARING_POPUP_MESSAGE_%@_%@"
+ "ROUTE_SHARING_POPUP_TITLE_%@"
+ "Route sharing popover accepted"
+ "Route sharing popover declined"
+ "Showing Route Sharing Popup for ID: %@"
+ "T@\"<CPBridgeNavigationSystemInfo>\",N,R"
+ "T@\"CAFRouteSharing\",N,R"
+ "T@\"CAFRouteStatus\",N,R"
+ "T@\"CAFSystemInformation\",N,R"
+ "T@\"CARSession\",&,N,V_currentSession"
+ "T@\"CARSessionStatus\",&,N,V_sessionStatus"
+ "T@\"CPNavigationSystemInfo\",&,N,V_systemInfo"
+ "T@\"CRPairedVehicleManager\",R,N,V_pairedVehicleManager"
+ "T@\"NSString\",N,R"
+ "T@\"NSString\",R,C,N,V_brand"
+ "T@\"NSString\",R,C,N,V_manufacturer"
+ "T@\"NSString\",R,C,N,V_model"
+ "T@\"NSString\",R,C,N,V_navigationAidedDrivingFeatureName"
+ "T@\"NSString\",R,C,N,V_navigationAidedDrivingFeatureShortName"
+ "T@\"NSString\",R,C,N,V_navigationName"
+ "T@\"URTAlertPresenter\",R,N,V_alertPresenter"
+ "TB,N,R"
+ "TB,N,V_routeLineUnavailableForRegion"
+ "TB,V_showingRouteSharingPopup"
+ "TC,N,R"
+ "Tq,N,V_navigatingCount"
+ "Vehicle"
+ "WaypointModified"
+ "WaypointRemoved"
+ "_alertPresenter"
+ "_brand"
+ "_currentSession"
+ "_manufacturer"
+ "_model"
+ "_navigatingCount"
+ "_navigationAidedDrivingFeatureName"
+ "_navigationAidedDrivingFeatureShortName"
+ "_navigationName"
+ "_pairedVehicleManager"
+ "_routeLineUnavailableForRegion"
+ "_sessionStatus"
+ "_showRouteSharingPopoverForVehicle:"
+ "_showRouteSharingPopoverIfNecessaryForVehicle:"
+ "_showingRouteSharingPopup"
+ "_systemInfo"
+ "_vehicleForCurrentSession"
+ "actionWithTitle:handler:"
+ "addAlert:forDestination:preferringStyle:"
+ "alertPresenter"
+ "alertWithTitle:message:"
+ "applicationEnabled"
+ "brand"
+ "clearNavigation"
+ "clearNavigation()"
+ "cpBridgedBrand"
+ "cpBridgedManufacturer"
+ "cpBridgedModel"
+ "cpBridgedNavigationAidedDrivingFeatureName"
+ "cpBridgedNavigationAidedDrivingFeatureShortName"
+ "cpBridgedNavigationName"
+ "didSet routeLineUnavailableForRegion: %{bool}d"
+ "didSet userEnabled: %{bool}d"
+ "didUpdateNavigationAidedDrivingActive:"
+ "didUpdateRouteSharingUserEnabled:"
+ "didUpdateRouteSharingVehicleEnabled:"
+ "didUpdateRouteSource:"
+ "didUpdateSystemInfo:"
+ "didUpdateUserRouteSharingStatus"
+ "didUpdateUserRouteSharingStatus()"
+ "hasShownRouteSharingFollowup"
+ "iOSDestinationsOnly"
+ "iOSRouteDestinationsModified"
+ "iOSRouteModified"
+ "iOSUnchanged"
+ "initWithBridge:"
+ "initWithIdentifier:delegate:sessionStatus:"
+ "initWithModel:brand:manufacturer:navigationName:nadFeatureLongName:nadFeatureShortName:"
+ "kCPRouteInfoRouteLineUnavailableForRegion"
+ "manufacturer"
+ "model"
+ "navigatingCount"
+ "navigationAidedDrivingActive"
+ "navigationAidedDrivingFeatureName"
+ "navigationAidedDrivingFeatureShortName"
+ "navigationName"
+ "oemName"
+ "pairedVehicleManager"
+ "present"
+ "releaseNavigationOwnership for %{public}@ navigatingCount=%ld"
+ "routeLineUnavailableForRegion"
+ "routeSharing"
+ "routeSharingReason"
+ "routeSharingService:didUpdateApplicationEnabled:"
+ "routeSharingService:didUpdateLegs:"
+ "routeSharingService:didUpdateSharingState:"
+ "routeSharingService:didUpdateUserEnabled:"
+ "routeSharingService:didUpdateUserVisibleReason:"
+ "routeSharingService:didUpdateVehicleEnabled:"
+ "routeSharingStatus"
+ "routeSharingUserEnabled"
+ "routeSharingVehicleEnabled"
+ "routeSource"
+ "routeState"
+ "routeStatus"
+ "routeStatusService:didUpdateDestination:"
+ "routeStatusService:didUpdateGeodeticSystem:"
+ "routeStatusService:didUpdateOrigin:"
+ "routeStatusService:didUpdateRerouteReason:"
+ "routeStatusService:didUpdateRouteState:"
+ "routeStatusService:didUpdateUserVisibleApplicationName:"
+ "saveVehicle:completion:"
+ "send(guidanceState:)"
+ "send(rerouteReason:)"
+ "send(routeLine:)"
+ "sendRerouteReason:"
+ "setAllowedApplicationBundleIDs:"
+ "setCancelAction:"
+ "setCurrentSession:"
+ "setHasShownRouteSharingFollowup:"
+ "setNavigatingCount:"
+ "setOtherAction:"
+ "setRerouteReason:"
+ "setRouteLineUnavailableForRegion:"
+ "setRouteSharingStatus:"
+ "setSessionStatus:"
+ "setSharingState:"
+ "setShowingRouteSharingPopup:"
+ "setSystemInfo:"
+ "sharingConsentChanged:"
+ "sharingStatus(for:)"
+ "showingRouteSharingPopup"
+ "systemInfo"
+ "systemInformation"
+ "systemInformationService:didUpdateNavigationAidedDrivingActive:"
+ "systemInformationService:didUpdateRouteSource:"
+ "systemInformationService:didUpdateUserVisibleNavigationAidedDrivingFeatureName:"
+ "systemInformationService:didUpdateUserVisibleNavigationAidedDrivingFeatureShortName:"
+ "systemInformationService:didUpdateUserVisibleNavigationSystemName:"
+ "systemInformationService:didUpdateUserVisibleVehicleBrand:"
+ "systemInformationService:didUpdateUserVisibleVehicleManufacturer:"
+ "systemInformationService:didUpdateUserVisibleVehicleModel:"
+ "userRouteSharingStatus"
+ "userVisibleNavigationAidedDrivingFeatureName"
+ "userVisibleNavigationAidedDrivingFeatureShortName"
+ "userVisibleNavigationSystemName"
+ "userVisibleVehicleBrand"
+ "userVisibleVehicleManufacturer"
+ "userVisibleVehicleModel"
+ "v16@?0@\"URTAlertAction\"8"
+ "v24@?0@\"CRVehicle\"8@\"NSError\"16"
+ "v28@0:8@\"CAFRouteSharing\"16B24"
+ "v28@0:8@\"CAFRouteSharing\"16C24"
+ "v28@0:8@\"CAFRouteStatus\"16C24"
+ "v28@0:8@\"CAFSystemInformation\"16B24"
+ "v28@0:8@\"CAFSystemInformation\"16C24"
+ "v28@0:8@\"CPVehicleStateManager\"16C24"
+ "v32@0:8@\"CAFRouteSharing\"16@\"CAFRouteLegs\"24"
+ "v32@0:8@\"CAFRouteSharing\"16@\"NSString\"24"
+ "v32@0:8@\"CAFRouteStatus\"16@\"CAFPointOfInterest\"24"
+ "v32@0:8@\"CAFRouteStatus\"16@\"NSString\"24"
+ "v32@0:8@\"CAFSystemInformation\"16@\"NSString\"24"
+ "v32@0:8@\"CPVehicleStateManager\"16@\"<CPBridgeNavigationSystemInfo>\"24"
+ "vehicleForCertificateSerial:"
+ "vehicleName"
+ "vehicleStateManager:didUpdateNavigationAidedDrivingActive:"
+ "vehicleStateManager:didUpdateRouteSharingActive:"
+ "vehicleStateManager:didUpdateRouteSharingUserEnabled:"
+ "vehicleStateManager:didUpdateRouteSharingVehicleEnabled:"
+ "vehicleStateManager:didUpdateRouteSource:"
+ "vehicleStateManager:didUpdateSystemInfo:"
+ "willReleaseNavigationOwnership(lastOwner:)"
+ "willReleaseNavigationOwnershipLastOwner:"
- "%s failed: route is nil"
- "%s failed: routeLine.identifier=%s  lastRouteLineIdentifier=%s"
- "%s failed: routeLineSupport.enabled is false - %s"
- "%s failed: routeLineSupport.ownsNavigation is false"
- "%s ownsNavigation=%{bool}d"
- "%s reason=%s, failed: routeLineSupport.ownsNavigation is false"
- "%s reason=%s, failed: routeSharingState.supportsRouteSharing is false"
- "%s reason=%s, forcing userEnabled"
- "%s reason=%s, not touching userEnabled"
- "%s reason=%s, userEnabled is already true"
- "-[CPNavigationManager vehicleStateManager:didUpdateRouteSharingEnabled:]"
- "CAFRouteObserver"
- "CPNavForceUserEnabled"
- "T@\"CAFRoute\",N,R"
- "TB,R,N,V_routeSharingActive"
- "_routeSharingActive"
- "clearRouteLine"
- "forceUserEnabledIfAllowed(reason:)"
- "initWithDictionary:"
- "releaseNavigationOwnership for %{public}@"
- "route"
- "routeLegsWithArray:"
- "routeService:didUpdateApplicationEnabled:"
- "routeService:didUpdateDestination:"
- "routeService:didUpdateGeodeticSystem:"
- "routeService:didUpdateLegs:"
- "routeService:didUpdateOrigin:"
- "routeService:didUpdateRouteState:"
- "routeService:didUpdateUserEnabled:"
- "routeService:didUpdateUserVisibleApplicationName:"
- "routeService:didUpdateVehicleEnabled:"
- "setSupportsRouteSharing"
- "updateNavigationOwnership"
- "v28@0:8@\"CAFRoute\"16B24"
- "v28@0:8@\"CAFRoute\"16C24"
- "v32@0:8@\"CAFRoute\"16@\"CAFPointOfInterest\"24"
- "v32@0:8@\"CAFRoute\"16@\"CAFRouteLegs\"24"
- "v32@0:8@\"CAFRoute\"16@\"NSString\"24"
- "vehicleStateManager:didUpdateRouteSharingEnabled:"
- "willReleaseNavigationOwnership"
- "willReleaseNavigationOwnership()"

```
