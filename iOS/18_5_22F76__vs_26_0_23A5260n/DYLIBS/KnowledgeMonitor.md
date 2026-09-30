## KnowledgeMonitor

> `/System/Library/PrivateFrameworks/KnowledgeMonitor.framework/KnowledgeMonitor`

```diff

-458.8.0.0.0
-  __TEXT.__text: 0x2d920
-  __TEXT.__auth_stubs: 0xc00
-  __TEXT.__objc_methlist: 0x2fc4
-  __TEXT.__const: 0x240
-  __TEXT.__gcc_except_tab: 0x824
-  __TEXT.__cstring: 0x2cae
-  __TEXT.__oslogstring: 0x2896
-  __TEXT.__dlopen_cstrs: 0x49
-  __TEXT.__unwind_info: 0xc28
-  __TEXT.__objc_classname: 0x5da
-  __TEXT.__objc_methname: 0x875a
-  __TEXT.__objc_methtype: 0xcc5
-  __TEXT.__objc_stubs: 0x6c40
-  __DATA_CONST.__got: 0x608
-  __DATA_CONST.__const: 0x928
-  __DATA_CONST.__objc_classlist: 0x168
+468.0.0.0.0
+  __TEXT.__text: 0x2ee44
+  __TEXT.__auth_stubs: 0xc30
+  __TEXT.__objc_methlist: 0x322c
+  __TEXT.__const: 0x250
+  __TEXT.__gcc_except_tab: 0x8b8
+  __TEXT.__cstring: 0x2ced
+  __TEXT.__oslogstring: 0x28ea
+  __TEXT.__unwind_info: 0xca8
+  __TEXT.__objc_classname: 0x63b
+  __TEXT.__objc_methname: 0x8e07
+  __TEXT.__objc_methtype: 0xe17
+  __TEXT.__objc_stubs: 0x70e0
+  __DATA_CONST.__got: 0x648
+  __DATA_CONST.__const: 0x9e0
+  __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x68
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2308
-  __DATA_CONST.__objc_superrefs: 0x150
+  __DATA_CONST.__objc_selrefs: 0x2470
+  __DATA_CONST.__objc_superrefs: 0x158
   __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__auth_got: 0x610
-  __AUTH_CONST.__const: 0x3e0
-  __AUTH_CONST.__cfstring: 0x1f60
-  __AUTH_CONST.__objc_const: 0x4ac0
+  __AUTH_CONST.__auth_got: 0x628
+  __AUTH_CONST.__const: 0x400
+  __AUTH_CONST.__cfstring: 0x1fa0
+  __AUTH_CONST.__objc_const: 0x50c8
   __AUTH_CONST.__objc_arrayobj: 0x1c8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x168
-  __DATA.__objc_ivar: 0x33c
-  __DATA.__data: 0x4e8
-  __DATA.__bss: 0x18
-  __DATA_DIRTY.__objc_data: 0xe10
-  __DATA_DIRTY.__bss: 0xc0
+  __AUTH.__objc_data: 0x140
+  __DATA.__objc_ivar: 0x38c
+  __DATA.__data: 0x548
+  __DATA.__bss: 0x10
+  __DATA_DIRTY.__objc_data: 0xdc0
+  __DATA_DIRTY.__bss: 0xb0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
+  - /System/Library/Frameworks/AVRouting.framework/AVRouting
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/EventKit.framework/EventKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/HealthKit.framework/HealthKit
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/NetworkExtension.framework/NetworkExtension
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AppConduit.framework/AppConduit
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
   - /System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices

   - /System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine
   - /System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi
   - /System/Library/PrivateFrameworks/DoNotDisturb.framework/DoNotDisturb
+  - /System/Library/PrivateFrameworks/DuetActivityScheduler.framework/DuetActivityScheduler
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BE2B6C81-4353-3B23-A4A8-D7F90E56E8CF
-  Functions: 1186
-  Symbols:   4448
-  CStrings:  2464
+  UUID: D8D20E3E-672D-37A4-BD13-D9CBC48876C4
+  Functions: 1238
+  Symbols:   4643
+  CStrings:  2566
 
Symbols:
+ -[DKApplicationState .cxx_destruct]
+ -[DKApplicationState application]
+ -[DKApplicationState compare:]
+ -[DKApplicationState description]
+ -[DKApplicationState displayType]
+ -[DKApplicationState hasKeyboardFocus]
+ -[DKApplicationState initWithDisplayType:element:]
+ -[DKApplicationState level]
+ -[DKApplicationState role]
+ -[DKApplicationState setApplication:]
+ -[DKApplicationState setDisplayType:]
+ -[DKApplicationState setHasKeyboardFocus:]
+ -[DKApplicationState setLevel:]
+ -[DKApplicationState setRole:]
+ -[DKApplicationState setZIndex:]
+ -[DKApplicationState zIndex]
+ -[DKApplicationStateStore .cxx_destruct]
+ -[DKApplicationStateStore continuityApplication]
+ -[DKApplicationStateStore externalApplication]
+ -[DKApplicationStateStore focalApplication]
+ -[DKApplicationStateStore mainApplication]
+ -[DKApplicationStateStore updateElements:displayType:]
+ -[_DKApplicationMonitor displayMonitor:didConnectIdentity:withConfiguration:]
+ -[_DKApplicationMonitor displayMonitor]
+ -[_DKApplicationMonitor elementsForDisplayLayout:]
+ -[_DKApplicationMonitor setDisplayMonitor:]
+ -[_DKApplicationMonitor updateFocalApplication:timestamp:displayType:transitionReason:transaction:]
+ -[_DKApplicationMonitor updateFocusStream]
+ -[_DKApplicationMonitorGuardedData .cxx_destruct]
+ -[_DKApplicationMonitorGuardedData applications]
+ -[_DKApplicationMonitorGuardedData continuityLayoutMonitor]
+ -[_DKApplicationMonitorGuardedData externalLayoutMonitor]
+ -[_DKApplicationMonitorGuardedData latestDate]
+ -[_DKApplicationMonitorGuardedData latestReason]
+ -[_DKApplicationMonitorGuardedData mainLayoutMonitor]
+ -[_DKApplicationMonitorGuardedData refreshTimer]
+ -[_DKApplicationMonitorGuardedData setApplications:]
+ -[_DKApplicationMonitorGuardedData setContinuityLayoutMonitor:]
+ -[_DKApplicationMonitorGuardedData setExternalLayoutMonitor:]
+ -[_DKApplicationMonitorGuardedData setLatestDate:]
+ -[_DKApplicationMonitorGuardedData setLatestReason:]
+ -[_DKApplicationMonitorGuardedData setMainLayoutMonitor:]
+ -[_DKApplicationMonitorGuardedData setRefreshTimer:]
+ -[_DKApplicationMonitorGuardedData setTransaction:]
+ -[_DKApplicationMonitorGuardedData transaction]
+ -[_DKLocationCoordinatesMonitor init].cold.2
+ -[_DKNavigationMonitor .cxx_destruct]
+ -[_DKNavigationMonitor didSetNavigating]
+ -[_DKNavigationMonitor setShutdownHandler:]
+ -[_DKNavigationMonitor shutdownHandler]
+ GCC_except_table13
+ GCC_except_table39
+ GCC_except_table40
+ GCC_except_table42
+ GCC_except_table49
+ GCC_except_table55
+ GCC_except_table60
+ _OBJC_CLASS_$_BMMapsNavigation
+ _OBJC_CLASS_$_DKApplicationState
+ _OBJC_CLASS_$_DKApplicationStateStore
+ _OBJC_CLASS_$_FBSDisplayMonitor
+ _OBJC_CLASS_$_HKWorkout
+ _OBJC_CLASS_$__DASPredictionTimeline
+ _OBJC_CLASS_$__DKApplicationMonitorGuardedData
+ _OBJC_CLASS_$__PASLock
+ _OBJC_CLASS_$__PASSimpleCoalescingTimer
+ _OBJC_IVAR_$_DKApplicationState._application
+ _OBJC_IVAR_$_DKApplicationState._displayType
+ _OBJC_IVAR_$_DKApplicationState._hasKeyboardFocus
+ _OBJC_IVAR_$_DKApplicationState._level
+ _OBJC_IVAR_$_DKApplicationState._role
+ _OBJC_IVAR_$_DKApplicationState._zIndex
+ _OBJC_IVAR_$_DKApplicationStateStore._continuityApplication
+ _OBJC_IVAR_$_DKApplicationStateStore._externalApplication
+ _OBJC_IVAR_$_DKApplicationStateStore._mainApplication
+ _OBJC_IVAR_$__DKApplicationMonitor._displayMonitor
+ _OBJC_IVAR_$__DKApplicationMonitor._guardedData
+ _OBJC_IVAR_$__DKApplicationMonitorGuardedData._applications
+ _OBJC_IVAR_$__DKApplicationMonitorGuardedData._continuityLayoutMonitor
+ _OBJC_IVAR_$__DKApplicationMonitorGuardedData._externalLayoutMonitor
+ _OBJC_IVAR_$__DKApplicationMonitorGuardedData._latestDate
+ _OBJC_IVAR_$__DKApplicationMonitorGuardedData._latestReason
+ _OBJC_IVAR_$__DKApplicationMonitorGuardedData._mainLayoutMonitor
+ _OBJC_IVAR_$__DKApplicationMonitorGuardedData._refreshTimer
+ _OBJC_IVAR_$__DKApplicationMonitorGuardedData._transaction
+ _OBJC_IVAR_$__DKNavigationMonitor._shutdownHandler
+ _OBJC_IVAR_$__DKNavigationMonitor._source
+ _OBJC_METACLASS_$_DKApplicationState
+ _OBJC_METACLASS_$_DKApplicationStateStore
+ _OBJC_METACLASS_$__DKApplicationMonitorGuardedData
+ _SBSCreateLayoutServiceEndpointForExternalDisplay
+ __HKWorkoutSessionStateName
+ __OBJC_$_INSTANCE_METHODS_DKApplicationState
+ __OBJC_$_INSTANCE_METHODS_DKApplicationStateStore
+ __OBJC_$_INSTANCE_METHODS__DKApplicationMonitorGuardedData
+ __OBJC_$_INSTANCE_VARIABLES_DKApplicationState
+ __OBJC_$_INSTANCE_VARIABLES_DKApplicationStateStore
+ __OBJC_$_INSTANCE_VARIABLES__DKApplicationMonitorGuardedData
+ __OBJC_$_PROP_LIST_DKApplicationState
+ __OBJC_$_PROP_LIST_DKApplicationStateStore
+ __OBJC_$_PROP_LIST__DKApplicationMonitorGuardedData
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FBSDisplayObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSDisplayObserving
+ __OBJC_$_PROTOCOL_REFS_FBSDisplayObserving
+ __OBJC_CLASS_PROTOCOLS_$__DKApplicationMonitor
+ __OBJC_CLASS_RO_$_DKApplicationState
+ __OBJC_CLASS_RO_$_DKApplicationStateStore
+ __OBJC_CLASS_RO_$__DKApplicationMonitorGuardedData
+ __OBJC_LABEL_PROTOCOL_$_FBSDisplayObserving
+ __OBJC_METACLASS_RO_$_DKApplicationState
+ __OBJC_METACLASS_RO_$_DKApplicationStateStore
+ __OBJC_METACLASS_RO_$__DKApplicationMonitorGuardedData
+ __OBJC_PROTOCOL_$_FBSDisplayObserving
+ ___28-[_DKBacklightMonitor start]_block_invoke.cold.1
+ ___28-[_DKBacklightMonitor start]_block_invoke.cold.2
+ ___29-[_DKNavigationMonitor start]_block_invoke.15
+ ___29-[_DKNavigationMonitor start]_block_invoke_2.17
+ ___37-[_DKLocationCoordinatesMonitor init]_block_invoke.16
+ ___42-[_DKApplicationMonitor updateFocusStream]_block_invoke
+ ___43-[_DKApplicationMonitor obtainCurrentValue]_block_invoke
+ ___43-[_DKNavigationMonitor setShutdownHandler:]_block_invoke
+ ___45-[_DKApplicationMonitor platformSpecificStop]_block_invoke
+ ___46-[_DKApplicationMonitor platformSpecificStart]_block_invoke_2
+ ___46-[_DKApplicationMonitor platformSpecificStart]_block_invoke_3
+ ___50-[_DKApplicationMonitor elementsForDisplayLayout:]_block_invoke
+ ___51-[_DKLocationCoordinatesMonitor _fetchAndCacheLOIs]_block_invoke.19
+ ___51-[_DKLocationCoordinatesMonitor _fetchAndCacheLOIs]_block_invoke.19.cold.1
+ ___55-[_DKApplicationMonitor displayLayoutTransitionHandler]_block_invoke.228
+ ___55-[_DKApplicationMonitor displayLayoutTransitionHandler]_block_invoke.cold.1
+ ___55-[_DKApplicationMonitor displayLayoutTransitionHandler]_block_invoke.cold.2
+ ___55-[_DKApplicationMonitor displayLayoutTransitionHandler]_block_invoke_2.cold.1
+ ___65-[_DKBacklightMonitor donateRetroactiveShutdownBacklightOffEvent]_block_invoke.30
+ ___77-[_DKApplicationMonitor displayMonitor:didConnectIdentity:withConfiguration:]_block_invoke
+ ___block_descriptor_32_e42_v16?0"_DKApplicationMonitorGuardedData"8l
+ ___block_descriptor_40_e8_32s_e42_v16?0"_DKApplicationMonitorGuardedData"8ls32l8
+ ___block_descriptor_48_e8_32s40r_e42_v16?0"_DKApplicationMonitorGuardedData"8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e42_v16?0"_DKApplicationMonitorGuardedData"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e92_v32?0"FBSDisplayLayoutMonitor"8"FBSDisplayLayout"16"FBSDisplayLayoutTransitionContext"24lw40l8s32l8
+ ___block_descriptor_72_e8_32r40r48r56r64r_e42_v16?0"_DKApplicationMonitorGuardedData"8lr32l8r40l8r48l8r56l8r64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80r_e42_v16?0"_DKApplicationMonitorGuardedData"8ls32l8s40l8s48l8s56l8s64l8s72l8r80l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72s80s_e5_v8?0ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_literal_global.205
+ ___block_literal_global.231
+ ___getBiomeLibraryInternalSymbolLoc_block_invoke
+ _dispatch_queue_create_with_target$V2
+ _getBiomeLibraryInternalSymbolLoc.ptr
+ _objc_msgSend$Coordinates
+ _objc_msgSend$Maps
+ _objc_msgSend$Navigation
+ _objc_msgSend$application
+ _objc_msgSend$applications
+ _objc_msgSend$cancelPendingOperations
+ _objc_msgSend$configurationForContinuityDisplay
+ _objc_msgSend$configurationWithEndpoint:
+ _objc_msgSend$continuityApplication
+ _objc_msgSend$continuityLayoutMonitor
+ _objc_msgSend$didSetNavigating
+ _objc_msgSend$displayMonitor
+ _objc_msgSend$displayType
+ _objc_msgSend$elementsForDisplayLayout:
+ _objc_msgSend$externalApplication
+ _objc_msgSend$externalLayoutMonitor
+ _objc_msgSend$focalApplication
+ _objc_msgSend$initWithDisplayType:element:
+ _objc_msgSend$initWithFormat:
+ _objc_msgSend$initWithGuardedData:
+ _objc_msgSend$initWithLaunchReason:type:starting:absoluteTimestamp:bundleID:parentBundleID:extensionHostID:shortVersionString:exactVersionString:dyldPlatform:isNativeArchitecture:displayType:
+ _objc_msgSend$initWithQueue:leewaySeconds:operation:
+ _objc_msgSend$initWithValues:forDurations:startingAt:
+ _objc_msgSend$latestDate
+ _objc_msgSend$latestReason
+ _objc_msgSend$mainApplication
+ _objc_msgSend$mainLayoutMonitor
+ _objc_msgSend$refreshTimer
+ _objc_msgSend$role
+ _objc_msgSend$runAfterDelaySeconds:coalescingBehavior:
+ _objc_msgSend$runWithLockAcquired:
+ _objc_msgSend$setApplications:
+ _objc_msgSend$setContinuityLayoutMonitor:
+ _objc_msgSend$setDisplayMonitor:
+ _objc_msgSend$setExternalLayoutMonitor:
+ _objc_msgSend$setLatestDate:
+ _objc_msgSend$setLatestReason:
+ _objc_msgSend$setMainLayoutMonitor:
+ _objc_msgSend$setNavigating:
+ _objc_msgSend$setRefreshTimer:
+ _objc_msgSend$setTransaction:
+ _objc_msgSend$sortUsingSelector:
+ _objc_msgSend$transaction
+ _objc_msgSend$updateElements:displayType:
+ _objc_msgSend$updateFocalApplication:timestamp:displayType:transitionReason:transaction:
+ _objc_msgSend$updateFocusStream
+ _objc_msgSend$zIndex
+ _objc_msgSend$zOrderIndex
- +[_DKNavigationMonitor setIsNavigating:]
- -[_DKApplicationMonitor focalApplicationFromDisplayLayout:]
- -[_DKApplicationMonitor layoutMonitor:didUpdateDisplayLayout:withContext:]
- -[_DKApplicationMonitor layoutMonitor:didUpdateDisplayLayout:withContext:].cold.1
- -[_DKApplicationMonitor layoutMonitor:didUpdateDisplayLayout:withContext:].cold.2
- -[_DKNavigationMonitor setNavigationStatus:]
- GCC_except_table32
- GCC_except_table43
- GCC_except_table44
- GCC_except_table5
- _BiomeLibraryInternalNodeBridge
- _BiomeLibraryInternalNodeBridge.cold.1
- _BiomeLibraryInternalNodeBridge.cold.2
- _BiomeLibraryInternalNodeBridge.cold.3
- _HealthKitLibraryCore
- _HealthKitLibraryCore.frameworkLibrary
- _OBJC_CLASS_$__DKPredictionTimeline
- _OBJC_IVAR_$__DKApplicationMonitor._layoutMonitor
- ___37-[_DKLocationCoordinatesMonitor init]_block_invoke.19
- ___51-[_DKLocationCoordinatesMonitor _fetchAndCacheLOIs]_block_invoke.22
- ___51-[_DKLocationCoordinatesMonitor _fetchAndCacheLOIs]_block_invoke.22.cold.1
- ___59-[_DKApplicationMonitor focalApplicationFromDisplayLayout:]_block_invoke
- ___59-[_DKApplicationMonitor focalApplicationFromDisplayLayout:]_block_invoke.70
- ___65-[_DKBacklightMonitor donateRetroactiveShutdownBacklightOffEvent]_block_invoke.29
- ___HKWorkoutSessionStateName
- ___HKWorkoutSessionStateName.cold.1
- ___HealthKitLibraryCore_block_invoke
- ___block_descriptor_32_e29_q24?0"NSArray"8"NSArray"16l
- ___block_descriptor_40_e5_v8?0l
- ___block_descriptor_40_e8_32w_e92_v32?0"FBSDisplayLayoutMonitor"8"FBSDisplayLayout"16"FBSDisplayLayoutTransitionContext"24lw32l8
- ___block_literal_global.73
- ___block_literal_global.92
- ___getBiomeLibraryInternalNodeSymbolLoc_block_invoke
- ___getHKWorkoutClass_block_invoke
- ___get_HKWorkoutSessionStateNameSymbolLoc_block_invoke
- _audit_stringHealthKit
- _getBiomeLibraryInternalNodeSymbolLoc
- _getBiomeLibraryInternalNodeSymbolLoc.ptr
- _getHKWorkoutClass.softClass
- _get_HKWorkoutSessionStateNameSymbolLoc.ptr
- _objc_msgSend$focalApplicationFromDisplayLayout:
- _objc_msgSend$initWithLaunchReason:launchType:starting:absoluteTimestamp:duration:bundleID:parentBundleID:extensionHostID:shortVersionString:exactVersionString:
- _objc_msgSend$initWithLaunchReason:launchType:starting:absoluteTimestamp:duration:bundleID:parentBundleID:extensionHostID:shortVersionString:exactVersionString:dyldPlatform:isNativeArchitecture:
- _objc_msgSend$launchType
- _objc_msgSend$layoutMonitor:didUpdateDisplayLayout:withContext:
- _objc_msgSend$objectsForKeys:notFoundMarker:
- _objc_msgSend$predictionUnavailable
- _objc_msgSend$setIsNavigating:
- _objc_msgSend$setNavigationStatus:
- _objc_msgSend$streamWithIdentifier:error:
- _objc_msgSend$timelineWithValues:forDurations:startingAt:
CStrings:
+ "\t"
+ "%{public}@ %llu"
+ "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBacklightMonitor.m:193"
+ "<DKApplicationState: %@ lvl:%zd zind:%zd keyb:%@ role:%zd dt:%zd>"
+ "@\"DKApplicationState\""
+ "@\"DKApplicationStateStore\""
+ "@\"FBSDisplayMonitor\""
+ "@\"NSObject<OS_os_transaction>\""
+ "@\"_PASLock\""
+ "@\"_PASSimpleCoalescingTimer\""
+ "@32@0:8Q16@24"
+ "BiomeLibraryInternal"
+ "Coordinates"
+ "DKApplicationMonitor: External monitor detected"
+ "DKApplicationMonitor: transitioning due to %@ with App: %@ Others: [%@, %@, %@]"
+ "DKApplicationState"
+ "DKApplicationStateStore"
+ "FBSDisplayObserving"
+ "False"
+ "Maps"
+ "Navigation"
+ "T@\"DKApplicationState\",R,N,V_continuityApplication"
+ "T@\"DKApplicationState\",R,N,V_externalApplication"
+ "T@\"DKApplicationState\",R,N,V_mainApplication"
+ "T@\"DKApplicationStateStore\",&,N,V_applications"
+ "T@\"FBSDisplayLayoutMonitor\",&,N,V_continuityLayoutMonitor"
+ "T@\"FBSDisplayLayoutMonitor\",&,N,V_externalLayoutMonitor"
+ "T@\"FBSDisplayLayoutMonitor\",&,N,V_mainLayoutMonitor"
+ "T@\"FBSDisplayMonitor\",&,N,V_displayMonitor"
+ "T@\"NSDate\",&,N,V_latestDate"
+ "T@\"NSObject<OS_os_transaction>\",&,N,V_transaction"
+ "T@\"NSString\",&,N,V_application"
+ "T@\"NSString\",&,N,V_latestReason"
+ "T@\"_PASSimpleCoalescingTimer\",&,N,V_refreshTimer"
+ "TB,N,V_hasKeyboardFocus"
+ "TQ,N,V_displayType"
+ "Tq,N,V_level"
+ "Tq,N,V_role"
+ "Tq,N,V_zIndex"
+ "True"
+ "_DKApplicationMonitorGuardedData"
+ "_DKBacklightMonitor Display Status"
+ "_DKBacklightMonitor received update while stopped"
+ "_application"
+ "_applications"
+ "_continuityApplication"
+ "_continuityLayoutMonitor"
+ "_displayMonitor"
+ "_displayType"
+ "_externalApplication"
+ "_externalLayoutMonitor"
+ "_guardedData"
+ "_hasKeyboardFocus"
+ "_latestDate"
+ "_latestReason"
+ "_level"
+ "_mainApplication"
+ "_mainLayoutMonitor"
+ "_refreshTimer"
+ "_role"
+ "_transaction"
+ "_zIndex"
+ "application"
+ "applications"
+ "cancelPendingOperations"
+ "configurationForContinuityDisplay"
+ "configurationWithEndpoint:"
+ "continuityApplication"
+ "continuityLayoutMonitor"
+ "didSetNavigating"
+ "displayMonitor"
+ "displayMonitor:didConnectIdentity:withConfiguration:"
+ "displayMonitor:didUpdateIdentity:withConfiguration:"
+ "displayMonitor:willDisconnectIdentity:"
+ "displayType"
+ "elementsForDisplayLayout:"
+ "externalApplication"
+ "externalLayoutMonitor"
+ "focalApplication"
+ "initWithDisplayType:element:"
+ "initWithFormat:"
+ "initWithGuardedData:"
+ "initWithLaunchReason:type:starting:absoluteTimestamp:bundleID:parentBundleID:extensionHostID:shortVersionString:exactVersionString:dyldPlatform:isNativeArchitecture:displayType:"
+ "initWithQueue:leewaySeconds:operation:"
+ "initWithValues:forDurations:startingAt:"
+ "latestDate"
+ "latestReason"
+ "mainApplication"
+ "mainLayoutMonitor"
+ "notify_get_state failed"
+ "q24@0:8@16"
+ "refreshTimer"
+ "role"
+ "runAfterDelaySeconds:coalescingBehavior:"
+ "runWithLockAcquired:"
+ "setApplication:"
+ "setApplications:"
+ "setContinuityLayoutMonitor:"
+ "setDisplayMonitor:"
+ "setDisplayType:"
+ "setExternalLayoutMonitor:"
+ "setHasKeyboardFocus:"
+ "setLatestDate:"
+ "setLatestReason:"
+ "setLevel:"
+ "setMainLayoutMonitor:"
+ "setRefreshTimer:"
+ "setRole:"
+ "setTransaction:"
+ "setZIndex:"
+ "sortUsingSelector:"
+ "transaction"
+ "updateElements:displayType:"
+ "updateFocalApplication:timestamp:displayType:transitionReason:transaction:"
+ "updateFocusStream"
+ "v16@?0@\"_DKApplicationMonitorGuardedData\"8"
+ "v32@0:8@\"FBSDisplayMonitor\"16@\"FBSDisplayIdentity\"24"
+ "v32@0:8@16Q24"
+ "v40@0:8@\"FBSDisplayMonitor\"16@\"FBSDisplayIdentity\"24@\"FBSDisplayConfiguration\"32"
+ "v56@0:8@16@24Q32@40@48"
+ "zIndex"
+ "zOrderIndex"
- "/Library/Caches/com.apple.xbs/Sources/DuetKnowledgeCollector/KnowledgeMonitor/KnowledgeMonitor/Monitors/_DKBacklightMonitor.m:191"
- "Applications: %@ Ordered applications: %@"
- "BiomeLibraryInternal unavailable"
- "BiomeLibraryInternalNode"
- "Failed to load root library node from BiomeLibraryInternal"
- "HKWorkout"
- "Location.Coordinates"
- "_HKWorkoutSessionStateName"
- "_layoutMonitor"
- "focalApplicationFromDisplayLayout:"
- "initWithLaunchReason:launchType:starting:absoluteTimestamp:duration:bundleID:parentBundleID:extensionHostID:shortVersionString:exactVersionString:"
- "initWithLaunchReason:launchType:starting:absoluteTimestamp:duration:bundleID:parentBundleID:extensionHostID:shortVersionString:exactVersionString:dyldPlatform:isNativeArchitecture:"
- "launchType"
- "layoutMonitor:didUpdateDisplayLayout:withContext:"
- "objectsForKeys:notFoundMarker:"
- "predictionUnavailable"
- "q24@?0@\"NSArray\"8@\"NSArray\"16"
- "setIsNavigating:"
- "setNavigationStatus:"
- "softlink:o:path:/System/Library/Frameworks/HealthKit.framework/HealthKit"
- "streamWithIdentifier:error:"
- "timelineWithValues:forDurations:startingAt:"

```
