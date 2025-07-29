## CarPlay

> `/System/Library/Frameworks/CarPlay.framework/CarPlay`

```diff

-271.7.10.0.0
-  __TEXT.__text: 0x3a2bc
-  __TEXT.__auth_stubs: 0x600
-  __TEXT.__objc_methlist: 0x4f08
-  __TEXT.__const: 0x178
-  __TEXT.__cstring: 0x309a
-  __TEXT.__oslogstring: 0x138c
-  __TEXT.__gcc_except_tab: 0x580
-  __TEXT.__unwind_info: 0x12d0
-  __TEXT.__objc_classname: 0xd6c
-  __TEXT.__objc_methname: 0xc121
-  __TEXT.__objc_methtype: 0x1f6b
-  __TEXT.__objc_stubs: 0x74a0
-  __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x17b8
-  __DATA_CONST.__objc_classlist: 0x288
+294.16.1.0.0
+  __TEXT.__text: 0x3d814
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__objc_methlist: 0x5360
+  __TEXT.__const: 0x180
+  __TEXT.__cstring: 0x31d5
+  __TEXT.__oslogstring: 0x1712
+  __TEXT.__gcc_except_tab: 0x5c8
+  __TEXT.__unwind_info: 0x13cc
+  __TEXT.__objc_classname: 0xdb5
+  __TEXT.__objc_methname: 0xcae7
+  __TEXT.__objc_methtype: 0x2014
+  __TEXT.__objc_stubs: 0x7da0
+  __DATA_CONST.__got: 0xa0
+  __DATA_CONST.__const: 0x18a8
+  __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x210
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x162f0
-  __DATA_CONST.__objc_selrefs: 0x28e8
-  __AUTH_CONST.__cfstring: 0x3300
-  __AUTH_CONST.__objc_const: 0x26a8
-  __AUTH_CONST.__const: 0x760
+  __DATA_CONST.__objc_const: 0x16ca0
+  __DATA_CONST.__objc_selrefs: 0x2a78
+  __DATA_CONST.__objc_protorefs: 0x100
+  __DATA_CONST.__objc_classrefs: 0x498
+  __DATA_CONST.__objc_superrefs: 0x210
+  __AUTH_CONST.__cfstring: 0x3480
+  __AUTH_CONST.__objc_const: 0x27c8
+  __AUTH_CONST.__const: 0x7c0
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x310
-  __AUTH.__objc_data: 0x1568
-  __DATA.__objc_protorefs: 0x100
-  __DATA.__objc_classrefs: 0x480
-  __DATA.__objc_superrefs: 0x200
-  __DATA.__objc_ivar: 0x608
+  __AUTH_CONST.__auth_got: 0x308
+  __AUTH.__objc_data: 0x15e0
+  __DATA.__objc_ivar: 0x67c
   __DATA.__data: 0x18c0
   __DATA.__bss: 0x198
-  __DATA_DIRTY.__objc_data: 0x3e8
+  __DATA_DIRTY.__objc_data: 0x460
   __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MapKit.framework/MapKit
+  - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AccessoryNavigation.framework/AccessoryNavigation
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard

   - /System/Library/PrivateFrameworks/NetAppsUtilities.framework/NetAppsUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 96AB2BE3-277A-3DC1-B79E-2D7731454D54
-  Functions: 1969
-  Symbols:   7423
-  CStrings:  3438
+  UUID: 889B107E-423D-329A-BB9B-D8B20129DAAD
+  Functions: 2081
+  Symbols:   7790
+  CStrings:  3581
 
Symbols:
+ +[CPRouteInfo supportsSecureCoding]
+ -[CPListImageRowItem imageTitles]
+ -[CPListImageRowItem initWithText:images:imageTitles:]
+ -[CPListImageRowItem setImageTitles:]
+ -[CPManeuver highwayExitLabel]
+ -[CPManeuver setHighwayExitLabel:]
+ -[CPNavigationManager _createRouteGuidanceObject]
+ -[CPNavigationManager _startNavigationWithRouteInfo:originalState:]
+ -[CPNavigationManager bundleName]
+ -[CPNavigationManager cancelRerouting]
+ -[CPNavigationManager destinationTimeZoneOffsetMinutes]
+ -[CPNavigationManager routeChangedWithReason:routeInfo:]
+ -[CPNavigationManager setBundleName:]
+ -[CPNavigationManager setDestinationTimeZoneOffsetMinutes:]
+ -[CPNavigationManager startNavigationWithRouteInfo:]
+ -[CPNavigationManager startNavigationWithRouteInfo:].cold.1
+ -[CPNavigationManager startRerouting]
+ -[CPNavigationSession _updateLaneGuidanceIndiciesWithStartIndex:laneGuidances:]
+ -[CPNavigationSession _updateManeuverIndiciesWithStartIndex:maneuvers:]
+ -[CPNavigationSession addLaneGuidances:]
+ -[CPNavigationSession addManeuvers:]
+ -[CPNavigationSession clientTripNotPausedException]
+ -[CPNavigationSession currentLaneGuidance]
+ -[CPNavigationSession currentRoadNameVariants]
+ -[CPNavigationSession destinationNameVariants]
+ -[CPNavigationSession laneGuidances]
+ -[CPNavigationSession maneuverState]
+ -[CPNavigationSession maneuvers]
+ -[CPNavigationSession pauseReason]
+ -[CPNavigationSession resumeTripWithUpdatedRouteInformation:]
+ -[CPNavigationSession sendsNavigationMetadata]
+ -[CPNavigationSession setCurrentLaneGuidance:]
+ -[CPNavigationSession setCurrentRoadNameVariants:]
+ -[CPNavigationSession setDestinationNameVariants:]
+ -[CPNavigationSession setLaneGuidances:]
+ -[CPNavigationSession setManeuverState:]
+ -[CPNavigationSession setManeuvers:]
+ -[CPNavigationSession setPauseReason:]
+ -[CPNavigationSession setSendsNavigationMetadata:]
+ -[CPRouteGuidance maneuverTravelEstimates]
+ -[CPRouteGuidance setTimeRemainingToNextManeuver:]
+ -[CPRouteGuidance timeRemainingToNextManeuver]
+ -[CPRouteGuidance tripTravelEstimates]
+ -[CPRouteInfo .cxx_destruct]
+ -[CPRouteInfo encodeWithCoder:]
+ -[CPRouteInfo initWithCoder:]
+ -[CPRouteInfo initWithRouteGuidance:maneuvers:laneGuidances:]
+ -[CPRouteInfo laneGuidances]
+ -[CPRouteInfo maneuvers]
+ -[CPRouteInfo routeGuidance]
+ -[CPRouteInformation .cxx_destruct]
+ -[CPRouteInformation currentLaneGuidance]
+ -[CPRouteInformation currentManeuvers]
+ -[CPRouteInformation initWithManeuvers:laneGuidances:currentManeuvers:currentLaneGuidance:tripTravelEstimates:maneuverTravelEstimates:]
+ -[CPRouteInformation laneGuidances]
+ -[CPRouteInformation maneuverTravelEstimates]
+ -[CPRouteInformation maneuvers]
+ -[CPRouteInformation routeInfoWithAccNavSupported:roadNameVariants:destinationNameVariants:timeZoneOffset:]
+ -[CPRouteInformation tripTravelEstimates]
+ -[CPTemplateApplicationDashboardScene _frameRateLimit]
+ -[CPTemplateApplicationDashboardScene _performActionsForUIScene:withUpdatedFBSScene:settingsDiff:fromSettings:transitionContext:lifecycleActionType:]
+ -[CPTemplateApplicationDashboardScene _templateSettings]
+ -[CPTemplateApplicationDashboardScene _updateFrameRateLimit]
+ -[CPTemplateApplicationDashboardScene frameRateLimitInspector]
+ -[CPTemplateApplicationDashboardScene frameRateLimit]
+ -[CPTemplateApplicationDashboardScene setFrameRateLimit:]
+ -[CPTemplateApplicationDashboardScene setFrameRateLimitInspector:]
+ -[CPTemplateApplicationInstrumentClusterScene _frameRateLimit]
+ -[CPTemplateApplicationInstrumentClusterScene _updateFrameRateLimit]
+ -[CPTemplateApplicationInstrumentClusterScene frameRateLimitInspector]
+ -[CPTemplateApplicationInstrumentClusterScene frameRateLimit]
+ -[CPTemplateApplicationInstrumentClusterScene setFrameRateLimit:]
+ -[CPTemplateApplicationInstrumentClusterScene setFrameRateLimitInspector:]
+ -[CPTemplateApplicationScene _frameRateLimit]
+ -[CPTemplateApplicationScene _updateFrameRateLimit]
+ -[CPTemplateApplicationScene frameRateLimitInspector]
+ -[CPTemplateApplicationScene frameRateLimit]
+ -[CPTemplateApplicationScene setFrameRateLimit:]
+ -[CPTemplateApplicationScene setFrameRateLimitInspector:]
+ -[CPTravelEstimates distanceRemainingToDisplay]
+ -[CPTravelEstimates initWithDistanceRemaining:distanceRemainingToDisplay:timeRemaining:]
+ -[CPTrip destinationNameVariants]
+ -[CPTrip destinationTimeZoneOffsetFromGMT]
+ -[CPTrip sendsNavigationMetadata]
+ -[CPTrip setDestinationNameVariants:]
+ -[CPTrip setSendsNavigationMetadata:]
+ -[CPUIFrameRateLimitDiffInspector observeFrameRateLimitWithBlock:]
+ -[CPUIMutableTemplateApplicationSceneSettings frameRateLimit]
+ -[CPUIMutableTemplateApplicationSceneSettings setFrameRateLimit:]
+ -[CPUITemplateApplicationSceneSettings frameRateLimit]
+ GCC_except_table49
+ _NSStringFromCPRerouteReason
+ _OBJC_CLASS_$_CPRouteInfo
+ _OBJC_CLASS_$_CPRouteInformation
+ _OBJC_CLASS_$_CPUIFrameRateLimitDiffInspector
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_IVAR_$_CPListImageRowItem._imageTitles
+ _OBJC_IVAR_$_CPManeuver._highwayExitLabel
+ _OBJC_IVAR_$_CPNavigationManager._bundleName
+ _OBJC_IVAR_$_CPNavigationManager._destinationTimeZoneOffsetMinutes
+ _OBJC_IVAR_$_CPNavigationSession._currentLaneGuidance
+ _OBJC_IVAR_$_CPNavigationSession._currentRoadNameVariants
+ _OBJC_IVAR_$_CPNavigationSession._destinationNameVariants
+ _OBJC_IVAR_$_CPNavigationSession._laneGuidances
+ _OBJC_IVAR_$_CPNavigationSession._maneuverState
+ _OBJC_IVAR_$_CPNavigationSession._maneuvers
+ _OBJC_IVAR_$_CPNavigationSession._pauseReason
+ _OBJC_IVAR_$_CPNavigationSession._sendsNavigationMetadata
+ _OBJC_IVAR_$_CPRouteGuidance._timeRemainingToNextManeuver
+ _OBJC_IVAR_$_CPRouteInfo._laneGuidances
+ _OBJC_IVAR_$_CPRouteInfo._maneuvers
+ _OBJC_IVAR_$_CPRouteInfo._routeGuidance
+ _OBJC_IVAR_$_CPRouteInformation._currentLaneGuidance
+ _OBJC_IVAR_$_CPRouteInformation._currentManeuvers
+ _OBJC_IVAR_$_CPRouteInformation._laneGuidances
+ _OBJC_IVAR_$_CPRouteInformation._maneuverTravelEstimates
+ _OBJC_IVAR_$_CPRouteInformation._maneuvers
+ _OBJC_IVAR_$_CPRouteInformation._tripTravelEstimates
+ _OBJC_IVAR_$_CPTemplateApplicationDashboardScene._frameRateLimit
+ _OBJC_IVAR_$_CPTemplateApplicationDashboardScene._frameRateLimitInspector
+ _OBJC_IVAR_$_CPTemplateApplicationInstrumentClusterScene._frameRateLimit
+ _OBJC_IVAR_$_CPTemplateApplicationInstrumentClusterScene._frameRateLimitInspector
+ _OBJC_IVAR_$_CPTemplateApplicationScene._frameRateLimit
+ _OBJC_IVAR_$_CPTemplateApplicationScene._frameRateLimitInspector
+ _OBJC_IVAR_$_CPTravelEstimates._distanceRemainingToDisplay
+ _OBJC_IVAR_$_CPTrip._destinationNameVariants
+ _OBJC_IVAR_$_CPTrip._sendsNavigationMetadata
+ _OBJC_METACLASS_$_CPRouteInfo
+ _OBJC_METACLASS_$_CPRouteInformation
+ _OBJC_METACLASS_$_CPUIFrameRateLimitDiffInspector
+ __OBJC_$_CLASS_METHODS_CPRouteInfo
+ __OBJC_$_CLASS_PROP_LIST_CPRouteInfo
+ __OBJC_$_INSTANCE_METHODS_CPRouteInfo
+ __OBJC_$_INSTANCE_METHODS_CPRouteInformation
+ __OBJC_$_INSTANCE_METHODS_CPUIFrameRateLimitDiffInspector
+ __OBJC_$_INSTANCE_VARIABLES_CPRouteInfo
+ __OBJC_$_INSTANCE_VARIABLES_CPRouteInformation
+ __OBJC_$_PROP_LIST_CPNavigationSessionManaging
+ __OBJC_$_PROP_LIST_CPRouteInfo
+ __OBJC_$_PROP_LIST_CPRouteInformation
+ __OBJC_$_PROP_LIST_CPUITemplateApplicationSceneSettings.55
+ __OBJC_CLASS_PROTOCOLS_$_CPRouteInfo
+ __OBJC_CLASS_RO_$_CPRouteInfo
+ __OBJC_CLASS_RO_$_CPRouteInformation
+ __OBJC_CLASS_RO_$_CPUIFrameRateLimitDiffInspector
+ __OBJC_METACLASS_RO_$_CPRouteInfo
+ __OBJC_METACLASS_RO_$_CPRouteInformation
+ __OBJC_METACLASS_RO_$_CPUIFrameRateLimitDiffInspector
+ ___36-[CPNavigationManager addManeuvers:]_block_invoke_3
+ ___36-[CPNavigationManager setManeuvers:]_block_invoke_2
+ ___36-[CPNavigationSession addManeuvers:]_block_invoke
+ ___37-[CPNavigationManager startRerouting]_block_invoke
+ ___38-[CPNavigationManager cancelRerouting]_block_invoke
+ ___39-[CPNavigationManager _setupConnection]_block_invoke.52
+ ___39-[CPNavigationManager _setupConnection]_block_invoke.53
+ ___39-[CPNavigationManager _setupConnection]_block_invoke.55
+ ___40-[CPNavigationManager addLaneGuidances:]_block_invoke_3
+ ___40-[CPNavigationManager setLaneGuidances:]_block_invoke_2
+ ___40-[CPNavigationSession addLaneGuidances:]_block_invoke
+ ___40-[CPNavigationSession setManeuverState:]_block_invoke
+ ___46-[CPNavigationSession setCurrentLaneGuidance:]_block_invoke
+ ___47-[CPMapTemplate startNavigationSessionForTrip:]_block_invoke.30
+ ___49-[CPNavigationManager didUpdateActiveComponents:]_block_invoke.64
+ ___50-[CPMapTemplate handleActionForControlIdentifier:]_block_invoke.43
+ ___50-[CPNavigationSession setCurrentRoadNameVariants:]_block_invoke
+ ___50-[CPNavigationSession setDestinationNameVariants:]_block_invoke
+ ___50-[CPNavigationSession setSendsNavigationMetadata:]_block_invoke
+ ___51-[CPNavigationSession clientTripNotPausedException]_block_invoke
+ ___52-[CPDashboardController _connectToListenerEndpoint:]_block_invoke.57
+ ___52-[CPDashboardController _connectToListenerEndpoint:]_block_invoke.57.cold.1
+ ___52-[CPInterfaceController _connectToListenerEndpoint:]_block_invoke.394
+ ___52-[CPInterfaceController _connectToListenerEndpoint:]_block_invoke.394.cold.1
+ ___58-[CPDashboardController handleActionForControlIdentifier:]_block_invoke.58
+ ___58-[CPNowPlayingTemplate handleAction:forControlIdentifier:]_block_invoke.81
+ ___60-[CPInstrumentClusterController _connectToListenerEndpoint:]_block_invoke.54
+ ___60-[CPInstrumentClusterController _connectToListenerEndpoint:]_block_invoke.54.cold.1
+ ___61-[CPNavigationSession resumeTripWithUpdatedRouteInformation:]_block_invoke
+ ___62-[CPInterfaceController clientPushNowPlayingTemplateAnimated:]_block_invoke.404
+ ___64-[CPTemplateApplicationScene initWithSession:connectionOptions:]_block_invoke_3
+ ___66-[CPUIFrameRateLimitDiffInspector observeFrameRateLimitWithBlock:]_block_invoke
+ ___66-[CPUIFrameRateLimitDiffInspector observeFrameRateLimitWithBlock:]_block_invoke_2
+ ___67-[CPNavigationManager _startNavigationWithRouteInfo:originalState:]_block_invoke
+ ___73-[CPTemplateApplicationDashboardScene initWithSession:connectionOptions:]_block_invoke.5
+ ___81-[CPTemplateApplicationInstrumentClusterScene initWithSession:connectionOptions:]_block_invoke_2
+ ___block_descriptor_32_e25_v16?0"CPRouteGuidance"8l
+ ___block_descriptor_33_e25_v16?0"CPRouteGuidance"8l
+ ___block_descriptor_33_e39_v16?0"<CPNavigationSessionManaging>"8l
+ ___block_descriptor_40_e39_v16?0"<CPNavigationSessionManaging>"8l
+ ___block_descriptor_40_e8_32s_e25_v16?0"CPRouteGuidance"8ls32l8
+ ___block_descriptor_40_e8_32s_e39_v16?0"<CPNavigationSessionManaging>"8ls32l8
+ ___block_literal_global.129
+ ___block_literal_global.145
+ ___block_literal_global.286
+ ___block_literal_global.32
+ ___block_literal_global.38
+ ___block_literal_global.40
+ ___block_literal_global.406
+ ___block_literal_global.411
+ ___block_literal_global.419
+ ___block_literal_global.424
+ ___block_literal_global.45
+ ___block_literal_global.47
+ ___block_literal_global.49
+ ___block_literal_global.55
+ ___block_literal_global.552
+ ___block_literal_global.555
+ ___block_literal_global.557
+ ___block_literal_global.559
+ ___block_literal_global.561
+ ___block_literal_global.563
+ ___block_literal_global.565
+ ___block_literal_global.567
+ ___block_literal_global.569
+ ___block_literal_global.571
+ ___block_literal_global.573
+ ___block_literal_global.575
+ ___block_literal_global.58
+ ___block_literal_global.8
+ _dispatch_sync
+ _kCADisplayTimingRefreshRate
+ _objc_msgSend$CADisplay
+ _objc_msgSend$_createRouteGuidanceObject
+ _objc_msgSend$_frameRateLimit
+ _objc_msgSend$_startNavigationWithRouteInfo:originalState:
+ _objc_msgSend$_updateFrameRateLimit
+ _objc_msgSend$_updateLaneGuidanceIndiciesWithStartIndex:laneGuidances:
+ _objc_msgSend$_updateManeuverIndiciesWithStartIndex:maneuvers:
+ _objc_msgSend$addLaneGuidances:
+ _objc_msgSend$addManeuvers:
+ _objc_msgSend$bundleName
+ _objc_msgSend$bundleRecordWithApplicationIdentifier:error:
+ _objc_msgSend$clearCurrentLaneGuidance
+ _objc_msgSend$clientTripNotPausedException
+ _objc_msgSend$currentLaneGuidance
+ _objc_msgSend$currentManeuvers
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$description
+ _objc_msgSend$destinationTimeZoneOffsetFromGMT
+ _objc_msgSend$destinationTimeZoneOffsetMinutes
+ _objc_msgSend$displayConfiguration
+ _objc_msgSend$distanceRemainingToDisplay
+ _objc_msgSend$distanceRemainingToNextManeuver
+ _objc_msgSend$distanceRemainingToNextManeuverDisplay
+ _objc_msgSend$frameRateLimit
+ _objc_msgSend$highwayExitLabel
+ _objc_msgSend$imageTitles
+ _objc_msgSend$infoDictionary
+ _objc_msgSend$initWithArray:copyItems:
+ _objc_msgSend$initWithDistanceRemaining:distanceRemainingToDisplay:timeRemaining:
+ _objc_msgSend$initWithRouteGuidance:maneuvers:laneGuidances:
+ _objc_msgSend$initWithText:images:imageTitles:
+ _objc_msgSend$laneGuidances
+ _objc_msgSend$maneuverTravelEstimates
+ _objc_msgSend$maneuvers
+ _objc_msgSend$mapTemplateShouldProvideNavigationMetadata:
+ _objc_msgSend$modifyRouteGuidance:
+ _objc_msgSend$objectForKey:ofClass:
+ _objc_msgSend$observeFrameRateLimitWithBlock:
+ _objc_msgSend$overrideDisplayTimings:
+ _objc_msgSend$pauseReason
+ _objc_msgSend$resetRouteGuidance
+ _objc_msgSend$routeChangedWithReason:routeInfo:
+ _objc_msgSend$routeInfoWithAccNavSupported:roadNameVariants:destinationNameVariants:timeZoneOffset:
+ _objc_msgSend$secondsFromGMT
+ _objc_msgSend$sendsNavigationMetadata
+ _objc_msgSend$setBeingShownInApp:
+ _objc_msgSend$setCurrentLaneGuidance:
+ _objc_msgSend$setCurrentManeuvers:
+ _objc_msgSend$setCurrentRoadNameVariants:
+ _objc_msgSend$setDestinationNameVariants:
+ _objc_msgSend$setDestinationTimeZoneOffsetMinutes:
+ _objc_msgSend$setDistanceRemaining:
+ _objc_msgSend$setDistanceRemainingDisplay:
+ _objc_msgSend$setDistanceRemainingToNextManeuver:
+ _objc_msgSend$setDistanceRemainingToNextManeuverDisplay:
+ _objc_msgSend$setEstimatedTimeOfArrival:
+ _objc_msgSend$setGuidanceState:
+ _objc_msgSend$setHighwayExitLabel:
+ _objc_msgSend$setLaneGuidanceShowing:
+ _objc_msgSend$setLaneGuidances:
+ _objc_msgSend$setManeuverState:
+ _objc_msgSend$setManeuvers:
+ _objc_msgSend$setPauseReason:
+ _objc_msgSend$setSendsNavigationMetadata:
+ _objc_msgSend$setSourceName:
+ _objc_msgSend$setSourceSupportsRouteGuidance:
+ _objc_msgSend$setTimeRemaining:
+ _objc_msgSend$setTotalLaneGuidanceCount:
+ _objc_msgSend$setTotalManeuverCount:
+ _objc_msgSend$startRerouting
+ _objc_msgSend$timeRemainingToNextManeuver
+ _objc_msgSend$timeZone
+ _objc_msgSend$tripTravelEstimates
- GCC_except_table36
- _OBJC_IVAR_$_CPManeuver._exitInfo
- _OBJC_IVAR_$_CPTravelEstimates._distanceRemainingDisplay
- __OBJC_$_PROP_LIST_CPUITemplateApplicationSceneSettings.50
- ___39-[CPNavigationManager _setupConnection]_block_invoke.42
- ___39-[CPNavigationManager _setupConnection]_block_invoke.43
- ___39-[CPNavigationManager _setupConnection]_block_invoke.45
- ___47-[CPMapTemplate startNavigationSessionForTrip:]_block_invoke.28
- ___49-[CPNavigationManager didUpdateActiveComponents:]_block_invoke.54
- ___50-[CPMapTemplate handleActionForControlIdentifier:]_block_invoke.41
- ___52-[CPDashboardController _connectToListenerEndpoint:]_block_invoke.56
- ___52-[CPDashboardController _connectToListenerEndpoint:]_block_invoke.56.cold.1
- ___52-[CPInterfaceController _connectToListenerEndpoint:]_block_invoke.366
- ___52-[CPInterfaceController _connectToListenerEndpoint:]_block_invoke.366.cold.1
- ___58-[CPDashboardController handleActionForControlIdentifier:]_block_invoke.57
- ___58-[CPNowPlayingTemplate handleAction:forControlIdentifier:]_block_invoke.80
- ___60-[CPInstrumentClusterController _connectToListenerEndpoint:]_block_invoke.53
- ___60-[CPInstrumentClusterController _connectToListenerEndpoint:]_block_invoke.53.cold.1
- ___62-[CPInterfaceController clientPushNowPlayingTemplateAnimated:]_block_invoke.376
- ___block_literal_global.128
- ___block_literal_global.144
- ___block_literal_global.2
- ___block_literal_global.20
- ___block_literal_global.22
- ___block_literal_global.284
- ___block_literal_global.33
- ___block_literal_global.37
- ___block_literal_global.378
- ___block_literal_global.383
- ___block_literal_global.391
- ___block_literal_global.396
- ___block_literal_global.48
- ___block_literal_global.524
- ___block_literal_global.527
- ___block_literal_global.529
- ___block_literal_global.53
- ___block_literal_global.531
- ___block_literal_global.533
- ___block_literal_global.535
- ___block_literal_global.537
- ___block_literal_global.539
- ___block_literal_global.541
- ___block_literal_global.543
- ___block_literal_global.545
- ___block_literal_global.547
- _objc_getProperty
- _objc_msgSend$initWithDistanceRemaining:distanceRemainingDisplay:timeRemaining:
- _objc_setProperty_atomic_copy
CStrings:
+ "\x02\x13\x11\x13"
+ "\x02\x13\x12\x13"
+ "\x02\x13\x13"
+ "\x06"
+ "\x13\x11\x13\x12"
+ "\x17"
+ "\x1a\x11\"\x13\x14"
+ "!\x18"
+ "\""
+ "%@ {distanceRemaining: %@, distanceRemainingToDisplay: %@, timeRemaining: %f}"
+ "3\x12\x16"
+ "@\"CPUIFrameRateLimitDiffInspector\""
+ "@\"NSNumber\"16@0:8"
+ "@40@0:8B16@20@28s36"
+ "AlternateRoute"
+ "Attempted to resume trip without pausing first."
+ "CADisplay"
+ "CFBundleName"
+ "CPRouteInfo"
+ "CPRouteInformation"
+ "CPUIFrameRateLimitDiffInspector"
+ "Cluster scene frame rate limit updated to %{public}f fps"
+ "Cluster scene updated to unrestricted frame rate"
+ "MissedTurn"
+ "Offline"
+ "T@\"CPLaneGuidance\",C,N,V_currentLaneGuidance"
+ "T@\"CPLaneGuidance\",R,C,N,V_currentLaneGuidance"
+ "T@\"CPRouteGuidance\",R,C,N,V_routeGuidance"
+ "T@\"CPTravelEstimates\",R,C,N,V_maneuverTravelEstimates"
+ "T@\"CPTravelEstimates\",R,C,N,V_tripTravelEstimates"
+ "T@\"CPTravelEstimates\",R,N"
+ "T@\"CPUIFrameRateLimitDiffInspector\",&,N,V_frameRateLimitInspector"
+ "T@\"NSArray\",C,N,V_imageTitles"
+ "T@\"NSArray\",R,C,N,V_currentManeuvers"
+ "T@\"NSArray\",R,C,N,V_laneGuidances"
+ "T@\"NSArray\",R,C,N,V_maneuvers"
+ "T@\"NSMeasurement\",R,C,N"
+ "T@\"NSMeasurement\",R,C,N,V_distanceRemainingToDisplay"
+ "T@\"NSMutableArray\",&,N,V_laneGuidances"
+ "T@\"NSMutableArray\",&,N,V_maneuvers"
+ "T@\"NSNumber\",&,N"
+ "T@\"NSNumber\",N,V_frameRateLimit"
+ "T@\"NSNumber\",R,N"
+ "T@\"NSString\",?,&,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",C,N,V_bundleName"
+ "T@\"NSString\",C,N,V_highwayExitLabel"
+ "TB,N,V_sendsNavigationMetadata"
+ "TQ,N,V_junctionType"
+ "TQ,N,V_maneuverType"
+ "TQ,N,V_pauseReason"
+ "TQ,N,V_trafficSide"
+ "Td,N,V_timeRemainingToNextManeuver"
+ "Template app scene frameRateLimit updated to %{public}f fps"
+ "Template app scene updated to unrestricted frame rate"
+ "Template dashboard scene frameRateLimit updated to %{public}f fps"
+ "Template dashboard scene updated to unrestricted frame rate"
+ "Tq,N,V_maneuverState"
+ "Tq,N,V_status"
+ "Unable to retrieve app record: %@"
+ "WaypointAdded"
+ "_bundleName"
+ "_createRouteGuidanceObject"
+ "_distanceRemainingToDisplay"
+ "_frameRateLimit"
+ "_frameRateLimitInspector"
+ "_highwayExitLabel"
+ "_imageTitles"
+ "_laneGuidances"
+ "_maneuverTravelEstimates"
+ "_maneuvers"
+ "_pauseReason"
+ "_sendsNavigationMetadata"
+ "_startNavigationWithRouteInfo:originalState:"
+ "_startNavigationWithRouteInfo:originalState: %@"
+ "_timeRemainingToNextManeuver"
+ "_tripTravelEstimates"
+ "_updateFrameRateLimit"
+ "_updateLaneGuidanceIndiciesWithStartIndex:laneGuidances:"
+ "_updateManeuverIndiciesWithStartIndex:maneuvers:"
+ "bundleName"
+ "bundleRecordWithApplicationIdentifier:error:"
+ "cancelRerouting"
+ "cancelRerouting guidanceState: %@"
+ "cancelRerouting: setting guidance state to active"
+ "cancelRerouting: state was rerouting, setting to active"
+ "clearCurrentLaneGuidance"
+ "clientTripNotPausedException"
+ "dateWithTimeIntervalSinceNow:"
+ "destinationTimeZoneOffsetFromGMT"
+ "displayConfiguration"
+ "distanceRemainingToDisplay"
+ "frameRateLimit"
+ "frameRateLimitInspector"
+ "highwayExitLabel"
+ "imageTitles"
+ "infoDictionary"
+ "initWithArray:copyItems:"
+ "initWithDistanceRemaining:distanceRemainingToDisplay:timeRemaining:"
+ "initWithManeuvers:laneGuidances:currentManeuvers:currentLaneGuidance:tripTravelEstimates:maneuverTravelEstimates:"
+ "initWithRouteGuidance:maneuvers:laneGuidances:"
+ "initWithText:images:imageTitles:"
+ "kCPListImageRowItemImageTitlesKey"
+ "kCPRouteGuidanceTimeRemainingToNextManeuver"
+ "kCPRouteInfoLaneGuidancesKey"
+ "kCPRouteInfoManeuversKey"
+ "kCPRouteInfoRouteGuidanceKey"
+ "maneuverTravelEstimates"
+ "mapTemplateShouldProvideNavigationMetadata:"
+ "objectForKey:ofClass:"
+ "observeFrameRateLimitWithBlock:"
+ "overrideDisplayTimings:"
+ "pauseReason"
+ "resumeTripWithUpdatedRouteInformation:"
+ "routeChangedWithReason: %@"
+ "routeChangedWithReason:routeInfo:"
+ "routeInfoWithAccNavSupported:roadNameVariants:destinationNameVariants:timeZoneOffset:"
+ "secondsFromGMT"
+ "sendSuggestUI:"
+ "sendsNavigationMetadata"
+ "setBundleName:"
+ "setFrameRateLimit:"
+ "setFrameRateLimitInspector:"
+ "setHighwayExitLabel:"
+ "setImageTitles:"
+ "setPauseReason:"
+ "setSendsNavigationMetadata:"
+ "setTimeRemainingToNextManeuver:"
+ "settingsObserver"
+ "startNavigation: route reset"
+ "startNavigation: set route guidance with loading state and counts"
+ "startNavigation: set route guidance with original route guidance"
+ "startNavigationWithRouteInfo"
+ "startNavigationWithRouteInfo:"
+ "startRerouting"
+ "startRerouting: current state: %@"
+ "startRerouting: set rerouting routeguidance"
+ "timeRemainingToNextManeuver"
+ "timeZone"
+ "tripTravelEstimates"
+ "unexpected state in startNavigation: %@"
+ "v16@?0@\"CPRouteGuidance\"8"
+ "v24@0:8@\"CPLaneGuidance\"16"
+ "v28@0:8@16C24"
+ "v28@0:8C16@\"CPRouteInfo\"20"
+ "v28@0:8C16@20"
+ "v28@0:8S16@20"
+ "\x81"
- "\x01!"
- "\x02\x12"
- "\x02\x13\x11\x12"
- "\x02\x13\x12"
- "\x02\x13\x12\x12"
- "!\x17"
- "#\x18"
- "%@ {distanceRemaining: %@, distanceRemainingDisplay: %@, timeRemaining: %f}"
- ",\x17\x11"
- "T@\"NSMeasurement\",R,C,N,V_distanceRemainingDisplay"
- "T@\"NSString\",C,V_exitInfo"
- "TC,N,V_junctionType"
- "TC,N,V_maneuverState"
- "TC,N,V_maneuverType"
- "TC,N,V_status"
- "TC,N,V_trafficSide"
- "_exitInfo"

```
