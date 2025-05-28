## CarPlaySupport

> `/System/Library/PrivateFrameworks/CarPlaySupport.framework/CarPlaySupport`

```diff

-271.7.10.0.0
-  __TEXT.__text: 0xd4b38
+294.16.1.0.0
+  __TEXT.__text: 0xd8090
   __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__objc_methlist: 0x799c
-  __TEXT.__const: 0x388
-  __TEXT.__cstring: 0x158e
-  __TEXT.__gcc_except_tab: 0xbb8
-  __TEXT.__oslogstring: 0x1dc9
+  __TEXT.__objc_methlist: 0x7b7c
+  __TEXT.__const: 0x390
+  __TEXT.__cstring: 0x15f4
+  __TEXT.__gcc_except_tab: 0xbd0
+  __TEXT.__oslogstring: 0x2026
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1814
-  __TEXT.__objc_classname: 0x157e
-  __TEXT.__objc_methname: 0x19d40
-  __TEXT.__objc_methtype: 0x50d6
-  __TEXT.__objc_stubs: 0x11160
+  __TEXT.__unwind_info: 0x1868
+  __TEXT.__objc_classname: 0x15b9
+  __TEXT.__objc_methname: 0x1a400
+  __TEXT.__objc_methtype: 0x51d1
+  __TEXT.__objc_stubs: 0x11820
   __DATA_CONST.__got: 0x1c0
-  __DATA_CONST.__const: 0x1e00
+  __DATA_CONST.__const: 0x1ea8
   __DATA_CONST.__objc_classlist: 0x3f0
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x2c0
+  __DATA_CONST.__objc_protolist: 0x2d0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1e0e0
-  __DATA_CONST.__objc_selrefs: 0x5148
+  __DATA_CONST.__objc_const: 0x1e668
+  __DATA_CONST.__objc_selrefs: 0x5310
+  __DATA_CONST.__objc_protorefs: 0x68
+  __DATA_CONST.__objc_classrefs: 0x898
+  __DATA_CONST.__objc_superrefs: 0x370
   __DATA_CONST.__objc_arraydata: 0x110
-  __AUTH_CONST.__objc_const: 0x2b50
+  __AUTH_CONST.__objc_const: 0x2b98
   __AUTH_CONST.__objc_intobj: 0x1c8
   __AUTH_CONST.__objc_arrayobj: 0x1c8
-  __AUTH_CONST.__cfstring: 0x13a0
+  __AUTH_CONST.__cfstring: 0x1440
   __AUTH_CONST.__const: 0x540
   __AUTH_CONST.__auth_ptr: 0x10
   __AUTH_CONST.__auth_got: 0x400
   __AUTH.__objc_data: 0x2760
-  __DATA.__objc_protorefs: 0x68
-  __DATA.__objc_classrefs: 0x898
-  __DATA.__objc_superrefs: 0x370
-  __DATA.__objc_ivar: 0x9bc
-  __DATA.__data: 0x2188
+  __DATA.__objc_ivar: 0x9cc
+  __DATA.__data: 0x2248
   __DATA.__bss: 0x130
   - /System/Library/Frameworks/CarPlay.framework/CarPlay
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2952
-  Symbols:   11723
-  CStrings:  5180
+  Functions: 3009
+  Symbols:   11913
+  CStrings:  5279
 
Symbols:
+ +[CPSMultilineLabel _rangeOfTrailingWhiteSpace:]
+ -[CPSBannerItem initWithIdentifier:bundleIdentifier:textVariants:detailTextVariants:attributedDetailTextVariants:imageSet:isManeuverItem:]
+ -[CPSBannerItem isManeuverItem]
+ -[CPSBannerSource sendSuggestUI:]
+ -[CPSInstrumentClusterCardLayout initWithCarScreenInfo:isRightHandDrive:]
+ -[CPSInstrumentClusterCardLayout initWithLayout:]
+ -[CPSInstrumentClusterCardLayout initWithSafeAreaFrame:viewAreaFrame:displayFrame:physicalPixelWidth:isRightHandDrive:]
+ -[CPSInstrumentClusterCardLayout safeArea]
+ -[CPSInstrumentClusterCardLayout setSafeArea:]
+ -[CPSInstrumentClusterCardLayout setViewArea:]
+ -[CPSInstrumentClusterCardLayout viewArea]
+ -[CPSInstrumentClusterCardViewController _evaluateCARScreenInfo]
+ -[CPSInstrumentClusterCardViewController carScreenInfo]
+ -[CPSInstrumentClusterCardViewController isRightHandDrive]
+ -[CPSInstrumentClusterCardViewController setCARScreenInfo:isRightHandDrive:]
+ -[CPSInstrumentClusterCardViewController setIsRightHandDrive:]
+ -[CPSNavigator _sync_displayUpdateManeuverTravelEstimates:forManeuver:]
+ -[CPSNavigator _sync_displayUpdateTripTravelEstimates:]
+ -[CPSNavigator addLaneGuidances:]
+ -[CPSNavigator addManeuvers:]
+ -[CPSNavigator clearCurrentLaneGuidance]
+ -[CPSNavigator initWithIdentifier:currentSession:forTrip:]
+ -[CPSNavigator metadataDelegate]
+ -[CPSNavigator routeChangedWithReason:routeInfo:]
+ -[CPSNavigator sendsNavigationMetadata]
+ -[CPSNavigator setCurrentLaneGuidance:]
+ -[CPSNavigator setCurrentRoadNameVariants:]
+ -[CPSNavigator setDestinationNameVariants:]
+ -[CPSNavigator setManeuverState:]
+ -[CPSNavigator setMetadataDelegate:]
+ -[CPSNavigator setSendsNavigationMetadata:]
+ -[CPSNavigator startRerouting]
+ -[CPSTabBarViewController viewDidLoad]
+ -[CPSTemplateInstance addLaneGuidances:]
+ -[CPSTemplateInstance addManeuvers:]
+ -[CPSTemplateInstance cancelTrip]
+ -[CPSTemplateInstance finishTrip]
+ -[CPSTemplateInstance navigationManager]
+ -[CPSTemplateInstance navigationOwnershipChangedToOwner:]
+ -[CPSTemplateInstance pauseTripForReason:]
+ -[CPSTemplateInstance routeChangedWithReason:routeInfo:]
+ -[CPSTemplateInstance sendSuggestUI:]
+ -[CPSTemplateInstance setActiveManeuvers:]
+ -[CPSTemplateInstance setCurrentLaneGuidance:]
+ -[CPSTemplateInstance setCurrentRoadNameVariants:]
+ -[CPSTemplateInstance setDestinationNameVariants:]
+ -[CPSTemplateInstance setDestinationTimeZoneOffsetMinutes:]
+ -[CPSTemplateInstance setManeuverState:]
+ -[CPSTemplateInstance setNavigationManager:]
+ -[CPSTemplateInstance setSendsNavigationMetadata:]
+ -[CPSTemplateInstance startRerouting]
+ -[CPSTemplateInstance updateTravelEstimates:forManeuver:]
+ -[CPSTemplateInstance updateTripTravelEstimates:]
+ GCC_except_table64
+ GCC_except_table86
+ GCC_except_table92
+ GCC_except_table96
+ _CPGuidanceStateFromCPTripPauseReason
+ _OBJC_CLASS_$_CPNavigationManager
+ _OBJC_IVAR_$_CPSBannerItem._isManeuverItem
+ _OBJC_IVAR_$_CPSInstrumentClusterCardLayout._safeArea
+ _OBJC_IVAR_$_CPSInstrumentClusterCardLayout._viewArea
+ _OBJC_IVAR_$_CPSInstrumentClusterCardViewController._carScreenInfo
+ _OBJC_IVAR_$_CPSInstrumentClusterCardViewController._isRightHandDrive
+ _OBJC_IVAR_$_CPSNavigator._metadataDelegate
+ _OBJC_IVAR_$_CPSNavigator._sendsNavigationMetadata
+ _OBJC_IVAR_$_CPSTemplateInstance._navigationManager
+ __OBJC_$_CLASS_METHODS_CPSMultilineLabel
+ __OBJC_$_PROP_LIST_CPNavigationSessionManaging
+ __OBJC_$_PROP_LIST_CPSBaseTemplateViewController.259
+ __OBJC_$_PROP_LIST_CPSNavigationMetadataDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPNavigationManagerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CPSNavigationMetadataDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPNavigationManagerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPSNavigationMetadataDelegate
+ __OBJC_$_PROTOCOL_REFS_CPNavigationManagerDelegate
+ __OBJC_$_PROTOCOL_REFS_CPSNavigationMetadataDelegate
+ __OBJC_LABEL_PROTOCOL_$_CPNavigationManagerDelegate
+ __OBJC_LABEL_PROTOCOL_$_CPSNavigationMetadataDelegate
+ __OBJC_PROTOCOL_$_CPNavigationManagerDelegate
+ __OBJC_PROTOCOL_$_CPSNavigationMetadataDelegate
+ ___40-[CPSTemplateInstance setManeuverState:]_block_invoke
+ ___42-[CPSTemplateInstance pauseTripForReason:]_block_invoke
+ ___42-[CPSTemplateInstance setActiveManeuvers:]_block_invoke
+ ___45-[CPSListTemplateViewController reloadItems:]_block_invoke.160
+ ___46-[CPSTemplateInstance setCurrentLaneGuidance:]_block_invoke
+ ___49-[CPSNavigator routeChangedWithReason:routeInfo:]_block_invoke
+ ___49-[CPSTemplateInstance updateTripTravelEstimates:]_block_invoke
+ ___50-[CPSTemplateInstance setCurrentRoadNameVariants:]_block_invoke
+ ___50-[CPSTemplateInstance setDestinationNameVariants:]_block_invoke
+ ___50-[CPSTemplateInstance setSendsNavigationMetadata:]_block_invoke
+ ___57-[CPSTemplateInstance updateTravelEstimates:forManeuver:]_block_invoke
+ ___58-[CPSTemplateInstance listener:shouldAcceptNewConnection:]_block_invoke
+ ___62-[CPSTemplateInstance viewController:didUpdateSafeAreaInsets:]_block_invoke.161
+ ___62-[CPSTemplateInstance viewController:didUpdateSafeAreaInsets:]_block_invoke.162
+ ___77-[CPSTemplateInstance presentVoiceTemplate:withProxyDelegate:animated:reply:]_block_invoke.90
+ ___90-[CPSTemplateInstance pushMapTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.77
+ ___91-[CPSTemplateInstance pushGridTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.73
+ ___91-[CPSTemplateInstance pushListTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.79
+ ___91-[CPSTemplateInstance pushListTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.81
+ ___93-[CPSTemplateInstance pushEntityTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.97
+ ___93-[CPSTemplateInstance pushSearchTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.88
+ ___97-[CPSTemplateInstance pushNowPlayingTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.85
+ ___98-[CPSTemplateInstance pushInformationTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.75
+ ___block_descriptor_33_e25_v16?0"CPRouteGuidance"8l
+ ___block_descriptor_40_e25_v16?0"CPRouteGuidance"8l
+ ___block_descriptor_40_e8_32s_e25_v16?0"CPRouteGuidance"8ls32l8
+ ___block_descriptor_48_e8_32s40s_e25_v16?0"CPRouteGuidance"8ls32l8s40l8
+ ___block_literal_global.105
+ ___block_literal_global.125
+ ___block_literal_global.131
+ ___block_literal_global.135
+ ___block_literal_global.231
+ ___block_literal_global.266
+ ___block_literal_global.269
+ ___block_literal_global.271
+ ___block_literal_global.274
+ ___block_literal_global.276
+ ___block_literal_global.278
+ ___block_literal_global.280
+ ___block_literal_global.76
+ ___os_log_helper_16_0_6_8_0_8_0_8_0_8_0_4_0_8_0
+ ___os_log_helper_16_2_4_8_64_8_64_8_64_8_64
+ __unnamed_array_storage.112
+ __unnamed_array_storage.117
+ __unnamed_array_storage.120
+ __unnamed_array_storage.130
+ __unnamed_array_storage.135
+ __unnamed_array_storage.140
+ __unnamed_array_storage.145
+ __unnamed_array_storage.93
+ __unnamed_array_storage.99
+ _kCPSuggestUIHybridString
+ _kCPSuggestUIMapString
+ _kCPSuggestUITurnCardString
+ _malloc_type_calloc
+ _objc_msgSend$URLWithString:
+ _objc_msgSend$_evaluateCARScreenInfo
+ _objc_msgSend$_sync_displayUpdateManeuverTravelEstimates:forManeuver:
+ _objc_msgSend$_sync_displayUpdateTripTravelEstimates:
+ _objc_msgSend$addLaneGuidances:
+ _objc_msgSend$addManeuvers:
+ _objc_msgSend$cancelTrip
+ _objc_msgSend$carScreenInfo
+ _objc_msgSend$configurationWithText:images:imageTitles:selectGridItemBlock:selectTitleBlock:showActivityIndicator:enabled:
+ _objc_msgSend$currentManeuverIndexes
+ _objc_msgSend$currentManeuvers
+ _objc_msgSend$currentViewArea
+ _objc_msgSend$dateWithTimeIntervalSinceNow:
+ _objc_msgSend$destinationTimeZoneOffsetFromGMT
+ _objc_msgSend$distanceRemainingToDisplay
+ _objc_msgSend$finishTrip
+ _objc_msgSend$hardwareIdentifier
+ _objc_msgSend$imageTitles
+ _objc_msgSend$initWithCarScreenInfo:isRightHandDrive:
+ _objc_msgSend$initWithIdentifier:bundleIdentifier:textVariants:detailTextVariants:attributedDetailTextVariants:imageSet:isManeuverItem:
+ _objc_msgSend$initWithIdentifier:currentSession:forTrip:
+ _objc_msgSend$initWithLayout:
+ _objc_msgSend$initWithSafeAreaFrame:viewAreaFrame:displayFrame:physicalPixelWidth:isRightHandDrive:
+ _objc_msgSend$isManeuverItem
+ _objc_msgSend$isRightHandDrive
+ _objc_msgSend$maneuverTravelEstimates
+ _objc_msgSend$metadataDelegate
+ _objc_msgSend$modifyRouteGuidance:
+ _objc_msgSend$navigationManager
+ _objc_msgSend$pauseTripForReason:
+ _objc_msgSend$physicalSize
+ _objc_msgSend$pixelSize
+ _objc_msgSend$resetRouteGuidance
+ _objc_msgSend$routeChangedWithReason:routeInfo:
+ _objc_msgSend$routeGuidance
+ _objc_msgSend$safeArea
+ _objc_msgSend$safeFrame
+ _objc_msgSend$screens
+ _objc_msgSend$sendSuggestUI:
+ _objc_msgSend$sendsNavigationMetadata
+ _objc_msgSend$setAccessibilityIdentifier:
+ _objc_msgSend$setActiveManeuvers:
+ _objc_msgSend$setCARScreenInfo:isRightHandDrive:
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
+ _objc_msgSend$setLaneGuidanceShowing:
+ _objc_msgSend$setManeuverState:
+ _objc_msgSend$setMetadataDelegate:
+ _objc_msgSend$setSendsNavigationMetadata:
+ _objc_msgSend$setSourceSupportsRouteGuidance:
+ _objc_msgSend$setSupportsAccNav:
+ _objc_msgSend$setTimeRemaining:
+ _objc_msgSend$startRerouting
+ _objc_msgSend$tripTravelEstimates
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$updateTravelEstimates:forManeuver:
+ _objc_msgSend$viewArea
+ _objc_msgSend$visibleFrame
- -[CPSBannerItem initWithIdentifier:bundleIdentifier:textVariants:detailTextVariants:attributedDetailTextVariants:imageSet:]
- -[CPSInstrumentClusterCardLayout safeAreaFrame]
- -[CPSInstrumentClusterCardLayout safeAreaInsets]
- -[CPSInstrumentClusterCardLayout setSafeAreaFrame:]
- -[CPSInstrumentClusterCardLayout setSafeAreaInsets:]
- -[CPSInstrumentClusterCardLayout setViewAreaFrame:]
- -[CPSInstrumentClusterCardLayout viewAreaFrame]
- -[CPSMultilineLabel _rangeOfTrailingWhiteSpace:]
- -[CPSNavigator initWithIdentifier:currentSession:]
- -[CPSNavigator navigationOwnershipChangedToOwner:]
- -[CPSNavigator navigationOwnershipManager]
- -[CPSNavigator setNavigationOwnershipManager:]
- GCC_except_table63
- GCC_except_table90
- GCC_except_table94
- _OBJC_CLASS_$_CARNavigationOwnershipManager
- _OBJC_IVAR_$_CPSInstrumentClusterCardLayout._safeAreaFrame
- _OBJC_IVAR_$_CPSInstrumentClusterCardLayout._safeAreaInsets
- _OBJC_IVAR_$_CPSInstrumentClusterCardLayout._viewAreaFrame
- _OBJC_IVAR_$_CPSNavigator._navigationOwnershipManager
- __OBJC_$_PROP_LIST_CPSBaseTemplateViewController.255
- ___45-[CPSListTemplateViewController reloadItems:]_block_invoke.156
- ___62-[CPSTemplateInstance viewController:didUpdateSafeAreaInsets:]_block_invoke.159
- ___62-[CPSTemplateInstance viewController:didUpdateSafeAreaInsets:]_block_invoke.160
- ___77-[CPSTemplateInstance presentVoiceTemplate:withProxyDelegate:animated:reply:]_block_invoke.89
- ___90-[CPSTemplateInstance pushMapTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.76
- ___91-[CPSTemplateInstance pushGridTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.72
- ___91-[CPSTemplateInstance pushListTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.78
- ___91-[CPSTemplateInstance pushListTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.80
- ___93-[CPSTemplateInstance pushEntityTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.96
- ___93-[CPSTemplateInstance pushSearchTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.87
- ___97-[CPSTemplateInstance pushNowPlayingTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.84
- ___98-[CPSTemplateInstance pushInformationTemplate:withProxyDelegate:animated:presentationStyle:reply:]_block_invoke.74
- ___block_literal_global.103
- ___block_literal_global.121
- ___block_literal_global.130
- ___block_literal_global.134
- ___block_literal_global.230
- ___block_literal_global.265
- ___block_literal_global.268
- ___block_literal_global.270
- ___block_literal_global.273
- ___block_literal_global.275
- ___block_literal_global.277
- ___block_literal_global.279
- ___block_literal_global.75
- __unnamed_array_storage.111
- __unnamed_array_storage.116
- __unnamed_array_storage.119
- __unnamed_array_storage.129
- __unnamed_array_storage.134
- __unnamed_array_storage.139
- __unnamed_array_storage.144
- __unnamed_array_storage.92
- __unnamed_array_storage.98
- _malloc_type_malloc
- _objc_msgSend$appSupportsInstrumentCluster
- _objc_msgSend$configurationWithText:images:selectGridItemBlock:selectTitleBlock:showActivityIndicator:enabled:
- _objc_msgSend$initWithIdentifier:bundleIdentifier:textVariants:detailTextVariants:attributedDetailTextVariants:imageSet:
- _objc_msgSend$initWithIdentifier:currentSession:
- _objc_msgSend$initWithSafeAreaFrame:viewAreaFrame:safeAreaInsets:
- _objc_msgSend$navigationOwnershipChangedToOwner:
- _objc_msgSend$navigationOwnershipDelegate
- _objc_msgSend$navigationOwnershipManager
- _objc_msgSend$origin
- _objc_msgSend$owningView
- _objc_msgSend$safeAreaFrame
- _objc_msgSend$setTrip:
- _objc_msgSend$viewAreaFrame
CStrings:
+ "\x12$"
+ "\x12\x7f\t"
+ "@\"<CPSNavigationMetadataDelegate>\""
+ "@\"CARScreenInfo\""
+ "@\"CPNavigationManager\""
+ "@124@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16{CGRect={CGPoint=dd}{CGSize=dd}}48{CGRect={CGPoint=dd}{CGSize=dd}}80d112B120"
+ "@68@0:8@16@24@32@40@48@56B64"
+ "CPBackButton"
+ "CPListSection"
+ "CPListTemplate"
+ "CPNavigationManagerDelegate"
+ "CPSNavigationMetadataDelegate"
+ "CPTabBar"
+ "CPTabBarNowPlayingButton"
+ "Cluster nav card: Setting constraints for ETA Card with layout: %lu"
+ "Cluster nav card: Setting constraints for platter view with layout: %lu"
+ "Cluster nav card: setShowETA %@"
+ "Cluster nav card: view area or safe area changed. Reevaluating Layout."
+ "Layout Calculation: Not showing ETA with turn card"
+ "Layout Calculation: Safe area width %f is greater than %f. Safe area mid: %f, Display mid: %f. is RHD: %d. using layout %lu"
+ "Layout Calculation: Using center layout"
+ "Layout Calculation: Using undefined layout"
+ "Layout Calculation: pixelSafeArea: %@, pixelViewArea: %@, pixelDisplayFrame: %@, pixelPhysicalWidth: %@"
+ "T@\"<BNPresentableContext>\",?,W,N"
+ "T@\"<CPSNavigationMetadataDelegate>\",&,N,V_metadataDelegate"
+ "T@\"CARScreenInfo\",R,N,V_carScreenInfo"
+ "T@\"CPNavigationManager\",&,N,V_navigationManager"
+ "T@\"CPSInstrumentClusterCardLayout\",R,N,V_layout"
+ "T@\"NSArray\",?,C,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "T@\"UIViewController\",?,R,N"
+ "TB,?,N"
+ "TB,?,R,N"
+ "TB,?,R,N,GisDraggingDismissalEnabled"
+ "TB,?,R,N,GisDraggingInteractionEnabled"
+ "TB,?,R,N,GisTouchOutsideDismissalEnabled"
+ "TB,N,V_isRightHandDrive"
+ "TB,N,V_sendsNavigationMetadata"
+ "TB,R,N,V_isManeuverItem"
+ "Tq,?,R,N"
+ "Ts,?,N"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_safeArea"
+ "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_viewArea"
+ "URLWithString:"
+ "_carScreenInfo"
+ "_evaluateCARScreenInfo"
+ "_isManeuverItem"
+ "_isRightHandDrive"
+ "_metadataDelegate"
+ "_navigationManager"
+ "_safeArea"
+ "_sendsNavigationMetadata"
+ "_sync_displayUpdateManeuverTravelEstimates:forManeuver:"
+ "_sync_displayUpdateTripTravelEstimates:"
+ "_viewArea"
+ "addLaneGuidances:"
+ "addManeuvers:"
+ "carScreenInfo"
+ "clearCurrentLaneGuidance"
+ "configurationWithText:images:imageTitles:selectGridItemBlock:selectTitleBlock:showActivityIndicator:enabled:"
+ "currentManeuverIndexes"
+ "currentManeuvers"
+ "currentViewArea"
+ "dateWithTimeIntervalSinceNow:"
+ "destinationNameVariants"
+ "destinationTimeZoneOffsetFromGMT"
+ "destinationTimeZoneOffsetMinutes"
+ "distanceRemainingToDisplay"
+ "hardwareIdentifier"
+ "imageTitles"
+ "initWithCarScreenInfo:isRightHandDrive:"
+ "initWithIdentifier:bundleIdentifier:textVariants:detailTextVariants:attributedDetailTextVariants:imageSet:isManeuverItem:"
+ "initWithIdentifier:currentSession:forTrip:"
+ "initWithLayout:"
+ "initWithSafeAreaFrame:viewAreaFrame:displayFrame:physicalPixelWidth:isRightHandDrive:"
+ "isManeuverItem"
+ "isRightHandDrive"
+ "maneuverTravelEstimates"
+ "metadataDelegate"
+ "modifyRouteGuidance:"
+ "navigationManager"
+ "pauseTripForReason:"
+ "physicalSize"
+ "pixelSize"
+ "resetRouteGuidance"
+ "routeChangedWithReason:routeInfo:"
+ "routeGuidance"
+ "s16@0:8"
+ "safeArea"
+ "safeFrame"
+ "screens"
+ "sendSuggestUI:"
+ "sendsNavigationMetadata"
+ "setAccessibilityIdentifier:"
+ "setActiveManeuvers:"
+ "setCARScreenInfo:isRightHandDrive:"
+ "setCurrentLaneGuidance:"
+ "setCurrentManeuvers:"
+ "setCurrentRoadNameVariants:"
+ "setDestinationNameVariants:"
+ "setDestinationTimeZoneOffsetMinutes:"
+ "setDistanceRemaining:"
+ "setDistanceRemainingDisplay:"
+ "setDistanceRemainingToNextManeuver:"
+ "setDistanceRemainingToNextManeuverDisplay:"
+ "setEstimatedTimeOfArrival:"
+ "setGuidanceState:"
+ "setIsRightHandDrive:"
+ "setLaneGuidanceShowing:"
+ "setManeuverState:"
+ "setMetadataDelegate:"
+ "setNavigationManager:"
+ "setSafeArea:"
+ "setSendsNavigationMetadata:"
+ "setSourceSupportsRouteGuidance:"
+ "setSupportsAccNav:"
+ "setTimeRemaining:"
+ "setViewArea:"
+ "startRerouting"
+ "tripTravelEstimates"
+ "unsignedIntValue"
+ "v16@?0@\"CPRouteGuidance\"8"
+ "v20@0:8s16"
+ "v24@0:8@\"CPLaneGuidance\"16"
+ "v28@0:8C16@\"CPRouteInfo\"20"
+ "v28@0:8C16@20"
+ "viewArea"
+ "visibleFrame"
- "\x12\x7f\b"
- "5"
- "@\"CARNavigationOwnershipManager\""
- "@64@0:8@16@24@32@40@48@56"
- "T@\"<BNPresentableContext>\",W,N"
- "T@\"CARNavigationOwnershipManager\",&,N,V_navigationOwnershipManager"
- "T@\"CPSInstrumentClusterCardLayout\",&,N,V_layout"
- "T@\"UIViewController\",R,N"
- "TB,R,N,GisDraggingDismissalEnabled"
- "TB,R,N,GisDraggingInteractionEnabled"
- "TB,R,N,GisTouchOutsideDismissalEnabled"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_safeAreaFrame"
- "T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_viewAreaFrame"
- "T{UIEdgeInsets=dddd},N,V_safeAreaInsets"
- "_navigationOwnershipManager"
- "_safeAreaFrame"
- "_safeAreaInsets"
- "_viewAreaFrame"
- "configurationWithText:images:selectGridItemBlock:selectTitleBlock:showActivityIndicator:enabled:"
- "initWithIdentifier:bundleIdentifier:textVariants:detailTextVariants:attributedDetailTextVariants:imageSet:"
- "initWithIdentifier:currentSession:"
- "navigationOwnershipManager"
- "origin"
- "owningView"
- "safeAreaFrame"
- "setNavigationOwnershipManager:"
- "setSafeAreaFrame:"
- "setSafeAreaInsets:"
- "setViewAreaFrame:"
- "viewAreaFrame"

```
