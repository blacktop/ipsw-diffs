## CarPlay

> `/System/Library/Frameworks/CarPlay.framework/CarPlay`

```diff

-488.39.0.0.0
-  __TEXT.__text: 0x551a4
-  __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_methlist: 0x7ce0
-  __TEXT.__const: 0x4a8
-  __TEXT.__cstring: 0x49eb
-  __TEXT.__oslogstring: 0x290b
-  __TEXT.__gcc_except_tab: 0x89c
-  __TEXT.__constg_swiftt: 0x1c0
-  __TEXT.__swift5_typeref: 0xd5
+515.10.1.0.0
+  __TEXT.__text: 0x68a6c
+  __TEXT.__auth_stubs: 0xc20
+  __TEXT.__objc_methlist: 0x8980
+  __TEXT.__const: 0x532
+  __TEXT.__cstring: 0x4ee6
+  __TEXT.__oslogstring: 0x2dab
+  __TEXT.__gcc_except_tab: 0x968
+  __TEXT.__constg_swiftt: 0x1f8
+  __TEXT.__swift5_typeref: 0x12f
   __TEXT.__swift5_builtin: 0x50
-  __TEXT.__swift5_reflstr: 0x97
+  __TEXT.__swift5_reflstr: 0xc4
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x14
-  __TEXT.__swift5_fieldmd: 0x64
-  __TEXT.__unwind_info: 0x1a10
-  __TEXT.__objc_classname: 0x1134
-  __TEXT.__objc_methname: 0xfeba
-  __TEXT.__objc_methtype: 0x279d
-  __TEXT.__objc_stubs: 0x97c0
-  __DATA_CONST.__got: 0x720
-  __DATA_CONST.__const: 0x1c48
-  __DATA_CONST.__objc_classlist: 0x358
-  __DATA_CONST.__objc_catlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x2c8
+  __TEXT.__swift5_fieldmd: 0x7c
+  __TEXT.__unwind_info: 0x1f30
+  __TEXT.__objc_classname: 0x127b
+  __TEXT.__objc_methname: 0x11eeb
+  __TEXT.__objc_methtype: 0x2c87
+  __TEXT.__objc_stubs: 0xaee0
+  __DATA_CONST.__got: 0x7f0
+  __DATA_CONST.__const: 0x1de8
+  __DATA_CONST.__objc_classlist: 0x390
+  __DATA_CONST.__objc_catlist: 0x48
+  __DATA_CONST.__objc_protolist: 0x2d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3648
+  __DATA_CONST.__objc_selrefs: 0x3bb8
   __DATA_CONST.__objc_protorefs: 0x158
-  __DATA_CONST.__objc_superrefs: 0x2b0
-  __AUTH_CONST.__auth_got: 0x5b0
-  __AUTH_CONST.__const: 0x9e8
-  __AUTH_CONST.__cfstring: 0x4360
-  __AUTH_CONST.__objc_const: 0x1c8d8
+  __DATA_CONST.__objc_superrefs: 0x2e8
+  __AUTH_CONST.__auth_got: 0x620
+  __AUTH_CONST.__const: 0xae8
+  __AUTH_CONST.__cfstring: 0x4c00
+  __AUTH_CONST.__objc_const: 0x1ec28
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH.__objc_data: 0x1b50
-  __AUTH.__data: 0x1e0
-  __DATA.__objc_ivar: 0x824
-  __DATA.__data: 0x1ea0
-  __DATA.__bss: 0x4b0
-  __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x640
+  __AUTH.__objc_data: 0x1ce0
+  __AUTH.__data: 0x230
+  __DATA.__objc_ivar: 0x920
+  __DATA.__data: 0x1fa0
+  __DATA.__bss: 0x4d0
+  __DATA.__common: 0x28
+  __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
+  - /System/Library/Frameworks/CoreMedia.framework/CoreMedia
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
+  - /System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/MapKit.framework/MapKit
   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/UIKit.framework/UIKit
+  - /System/Library/Frameworks/_LocationEssentials.framework/_LocationEssentials
   - /System/Library/PrivateFrameworks/AccessoryNavigation.framework/AccessoryNavigation
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
   - /System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework

   - /System/Library/PrivateFrameworks/UserAlerts.framework/UserAlerts
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 092AFD91-8060-3152-8F61-4B481F1AB017
-  Functions: 2727
-  Symbols:   10154
-  CStrings:  4586
+  UUID: 42F93BA0-3B04-32A7-A44E-4E360956AA6B
+  Functions: 3012
+  Symbols:   11218
+  CStrings:  5028
 
Symbols:
+ +[CADisplay(CPAdditions) cp_displayWithID:]
+ +[CPAccNavUpdate _decodeNumberForParameter:fromDecoder:accNavType:]
+ +[CPImageOverlay supportsSecureCoding]
+ +[CPListImageRowItem _setMaximumNumberOfGridImages:]
+ +[CPListImageRowItem maximumNumberOfGridImages]
+ +[CPListImageRowItemCardElement convertImage:aspectRatio:]
+ +[CPListImageRowItemCardElement maximumImageSizeForAspectRatio:]
+ +[CPListTemplate _setMaximumHeaderGridButtonCount:]
+ +[CPListTemplate _setMaximumItemCount:]
+ +[CPListTemplate _setMaximumSectionCount:]
+ +[CPListTemplateDetailsHeader maximumActionButtonSize]
+ +[CPListTemplateDetailsHeader maximumNumberOfActionButtons]
+ +[CPListTemplateDetailsHeader supportsSecureCoding]
+ +[CPPlaybackConfiguration supportsSecureCoding]
+ +[CPSportsOverlay supportsSecureCoding]
+ +[CPThumbnailImage convertImage:aspectRatio:]
+ +[CPThumbnailImage correctedAspectRatioForImage:]
+ +[CPThumbnailImage supportsSecureCoding]
+ +[CPVoiceControlState maximumActionButtonCount]
+ -[CPImageOverlay .cxx_destruct]
+ -[CPImageOverlay alignment]
+ -[CPImageOverlay backgroundColor]
+ -[CPImageOverlay encodeWithCoder:]
+ -[CPImageOverlay hash]
+ -[CPImageOverlay image]
+ -[CPImageOverlay initWithCoder:]
+ -[CPImageOverlay initWithImage:alignment:]
+ -[CPImageOverlay initWithText:textColor:backgroundColor:alignment:]
+ -[CPImageOverlay isEqual:]
+ -[CPImageOverlay setAlignment:]
+ -[CPImageOverlay setBackgroundColor:]
+ -[CPImageOverlay setImage:]
+ -[CPImageOverlay setText:]
+ -[CPImageOverlay setTextColor:]
+ -[CPImageOverlay textColor]
+ -[CPImageOverlay text]
+ -[CPImageSet computedHashAtInitialization]
+ -[CPImageSet hash]
+ -[CPImageSet setComputedHashAtInitialization:]
+ -[CPInterfaceController _pushVoiceControlTemplate:presentationStyle:animated:completion:]
+ -[CPListImageRowItem reloadThumbnail:]
+ -[CPListImageRowItem setIdentifier:]
+ -[CPListImageRowItemCardElement hash]
+ -[CPListImageRowItemCardElement initWithThumbnail:title:subtitle:tintColor:]
+ -[CPListImageRowItemCardElement isEqual:]
+ -[CPListImageRowItemCardElement setThumbnail:]
+ -[CPListImageRowItemCardElement thumbnail]
+ -[CPListImageRowItemCondensedElement hash]
+ -[CPListImageRowItemCondensedElement isEqual:]
+ -[CPListImageRowItemElement accessibilityLabel]
+ -[CPListImageRowItemElement hash]
+ -[CPListImageRowItemElement isEqual:]
+ -[CPListImageRowItemElement playbackConfiguration]
+ -[CPListImageRowItemElement setAccessibilityLabel:]
+ -[CPListImageRowItemElement setPlaybackConfiguration:]
+ -[CPListImageRowItemImageGridElement hash]
+ -[CPListImageRowItemImageGridElement isEqual:]
+ -[CPListImageRowItemRowElement hash]
+ -[CPListImageRowItemRowElement isEqual:]
+ -[CPListItem playbackConfiguration]
+ -[CPListItem resolvedIsPlaying]
+ -[CPListItem resolvedPlaybackProgress]
+ -[CPListItem setPlaybackConfiguration:]
+ -[CPListTemplate initWithTitle:listHeader:sections:assistantCellConfiguration:]
+ -[CPListTemplate listHeader]
+ -[CPListTemplate setListHeader:]
+ -[CPListTemplateDetailsHeader .cxx_destruct]
+ -[CPListTemplateDetailsHeader actionButtons]
+ -[CPListTemplateDetailsHeader bodyVariants]
+ -[CPListTemplateDetailsHeader encodeWithCoder:]
+ -[CPListTemplateDetailsHeader initWithCoder:]
+ -[CPListTemplateDetailsHeader initWithThumbnail:title:subtitle:actionButtons:]
+ -[CPListTemplateDetailsHeader initWithThumbnail:title:subtitle:bodyVariants:actionButtons:]
+ -[CPListTemplateDetailsHeader initWithThumbnail:title:subtitle:metadataTitleVariants:actionButtons:]
+ -[CPListTemplateDetailsHeader listTemplate]
+ -[CPListTemplateDetailsHeader metadataTitleVariants]
+ -[CPListTemplateDetailsHeader playbackConfiguration]
+ -[CPListTemplateDetailsHeader reloadThumbnail:]
+ -[CPListTemplateDetailsHeader setActionButtons:]
+ -[CPListTemplateDetailsHeader setAdaptiveBackgroundStyle:]
+ -[CPListTemplateDetailsHeader setBodyVariants:]
+ -[CPListTemplateDetailsHeader setListTemplate:]
+ -[CPListTemplateDetailsHeader setMetadataTitleVariants:]
+ -[CPListTemplateDetailsHeader setPlaybackConfiguration:]
+ -[CPListTemplateDetailsHeader setSubtitle:]
+ -[CPListTemplateDetailsHeader setThumbnail:]
+ -[CPListTemplateDetailsHeader setTitle:]
+ -[CPListTemplateDetailsHeader subtitle]
+ -[CPListTemplateDetailsHeader thumbnail]
+ -[CPListTemplateDetailsHeader title]
+ -[CPListTemplateDetailsHeader updateHeader]
+ -[CPListTemplateDetailsHeader wantsAdaptiveBackgroundStyle]
+ -[CPMapTemplate clientDestinationRequestReceivedFromVehicle:]
+ -[CPMapTemplate clientDestinationSharedFailedForTrip:error:]
+ -[CPMapTemplate clientDestinationSharedSuccessfullyForTrip:]
+ -[CPMapTemplate clientDestinationWillBeSharedForTrip:]
+ -[CPMapTemplate clientRouteSourceUpdateReceivedFromVehicle:]
+ -[CPMapTemplate clientWaypoint:accepted:]
+ -[CPMapTemplate clientWaypointReceivedFromVehicle:]
+ -[CPMapTemplate currentNavigationSession]
+ -[CPMapTemplate setCurrentNavigationSession:]
+ -[CPMapTemplateWaypoint .cxx_destruct]
+ -[CPMapTemplateWaypoint description]
+ -[CPMapTemplateWaypoint initWithWaypoint:travelEstimates:]
+ -[CPMapTemplateWaypoint setTravelEstimates:]
+ -[CPMapTemplateWaypoint setWaypoint:]
+ -[CPMapTemplateWaypoint travelEstimates]
+ -[CPMapTemplateWaypoint waypoint]
+ -[CPNavigationManager _configureBaseRouteGuidance:]
+ -[CPNavigationManager _destinationHandoffErrorWithReason:]
+ -[CPNavigationManager _externalAccessoryDestinationInformationForDestination:]
+ -[CPNavigationManager _handleAccessoryDidConnect:]
+ -[CPNavigationManager _handleAccessoryDidConnect:].cold.1
+ -[CPNavigationManager _startNavigationWithRouteInfo:]
+ -[CPNavigationManager currentCarPlayAccessory]
+ -[CPNavigationManager currentLeg]
+ -[CPNavigationManager handleSharedDestination:completion:]
+ -[CPNavigationManager setCurrentLeg:]
+ -[CPNavigationManager vehicleForCurrentSession]
+ -[CPNavigationManager vehicleNavigationSystemName]
+ -[CPNavigationManager vehicleSupportsDestinationSharing]
+ -[CPNavigationSession addRouteSegments:]
+ -[CPNavigationSession currentRouteGuidance]
+ -[CPNavigationSession currentSegment]
+ -[CPNavigationSession getRouteLineForCurrentSegments]
+ -[CPNavigationSession resumeTripWithUpdatedRouteSegments:currentSegment:rerouteReason:]
+ -[CPNavigationSession routeSegments]
+ -[CPNavigationSession setCurrentSegment:]
+ -[CPNavigationSession setRouteSegments:]
+ -[CPNavigationSession setSupportsRouteSharing:]
+ -[CPNavigationSession startNavigationForCurrentRouteInfo]
+ -[CPNavigationSession supportsRouteSharing]
+ -[CPNavigationWaypoint initWithCenterPoint:locationThreshold:name:address:entryPoints:entryPointsCount:timeZone:]
+ -[CPNavigationWaypoint initWithURL:]
+ -[CPNavigationWaypoint timeZone]
+ -[CPPlaybackConfiguration copyWithZone:]
+ -[CPPlaybackConfiguration duration]
+ -[CPPlaybackConfiguration elapsedTime]
+ -[CPPlaybackConfiguration encodeWithCoder:]
+ -[CPPlaybackConfiguration hash]
+ -[CPPlaybackConfiguration initWithCoder:]
+ -[CPPlaybackConfiguration initWithPreferredPresentation:playbackAction:elapsedTime:duration:]
+ -[CPPlaybackConfiguration initWithPreferredPresentation:playbackState:elapsedTime:duration:]
+ -[CPPlaybackConfiguration initWithPreferredPresentation:playbackState:progress:]
+ -[CPPlaybackConfiguration initWithPreferredPresentation:playbackState:progress:duration:]
+ -[CPPlaybackConfiguration initWithPreferredPresentation:playing:progress:]
+ -[CPPlaybackConfiguration isEqual:]
+ -[CPPlaybackConfiguration isPlaying]
+ -[CPPlaybackConfiguration playbackAction]
+ -[CPPlaybackConfiguration playbackState]
+ -[CPPlaybackConfiguration preferredPresentation]
+ -[CPPlaybackConfiguration progress]
+ -[CPRouteGuidance copyForLoading]
+ -[CPRouteInfo currentLeg]
+ -[CPRouteInfo initWithRouteGuidance:maneuvers:laneGuidances:routeLine:currentLeg:]
+ -[CPRouteLeg identifier]
+ -[CPRouteSegment .cxx_destruct]
+ -[CPRouteSegment coordinatesCount]
+ -[CPRouteSegment coordinates]
+ -[CPRouteSegment copyWithZone:]
+ -[CPRouteSegment currentLaneGuidance]
+ -[CPRouteSegment currentManeuvers]
+ -[CPRouteSegment dealloc]
+ -[CPRouteSegment description]
+ -[CPRouteSegment destination]
+ -[CPRouteSegment identifier]
+ -[CPRouteSegment initWithOrigin:destination:maneuvers:laneGuidances:currentManeuvers:currentLaneGuidance:tripTravelEstimates:maneuverTravelEstimates:coordinates:coordinatesCount:]
+ -[CPRouteSegment laneGuidances]
+ -[CPRouteSegment maneuverTravelEstimates]
+ -[CPRouteSegment maneuvers]
+ -[CPRouteSegment origin]
+ -[CPRouteSegment tripTravelEstimates]
+ -[CPSessionConfiguration _updateLimitedUIStatusForSession:]
+ -[CPSessionConfiguration supportsVideoPlayback]
+ -[CPSportsOverlay .cxx_destruct]
+ -[CPSportsOverlay encodeWithCoder:]
+ -[CPSportsOverlay eventStatus]
+ -[CPSportsOverlay hash]
+ -[CPSportsOverlay initWithCoder:]
+ -[CPSportsOverlay initWithLeftTeam:rightTeam:eventStatus:]
+ -[CPSportsOverlay isEqual:]
+ -[CPSportsOverlay leftTeam]
+ -[CPSportsOverlay rightTeam]
+ -[CPSportsOverlay setEventStatus:]
+ -[CPSportsOverlay setLeftTeam:]
+ -[CPSportsOverlay setRightTeam:]
+ -[CPThumbnailImage .cxx_destruct]
+ -[CPThumbnailImage aspectRatio]
+ -[CPThumbnailImage encodeWithCoder:]
+ -[CPThumbnailImage hash]
+ -[CPThumbnailImage identifier]
+ -[CPThumbnailImage imageOverlay]
+ -[CPThumbnailImage imageSet]
+ -[CPThumbnailImage image]
+ -[CPThumbnailImage initWithCoder:]
+ -[CPThumbnailImage initWithImage:]
+ -[CPThumbnailImage initWithImage:imageOverlay:sportsOverlay:]
+ -[CPThumbnailImage initWithImage:imageOverlay:sportsOverlay:playbackProgress:]
+ -[CPThumbnailImage initWithImageSet:]
+ -[CPThumbnailImage isEqual:]
+ -[CPThumbnailImage playbackProgress]
+ -[CPThumbnailImage setImage:]
+ -[CPThumbnailImage setImageOverlay:]
+ -[CPThumbnailImage setImageSet:]
+ -[CPThumbnailImage setSportsOverlay:]
+ -[CPThumbnailImage setThumbnailUpdater:]
+ -[CPThumbnailImage sportsOverlay]
+ -[CPThumbnailImage thumbnailUpdater]
+ -[CPThumbnailImage updateThumbnail]
+ -[CPTrip destinationWaypoint]
+ -[CPTrip hasShareableDestination]
+ -[CPTrip initWithOriginWaypoint:destinationWaypoint:routeChoices:]
+ -[CPTrip originWaypoint]
+ -[CPTrip routeSegmentsAvailableForRegion]
+ -[CPTrip setHasShareableDestination:]
+ -[CPTrip setRouteSegmentsAvailableForRegion:]
+ -[CPVoiceControlState actionButtons]
+ -[CPVoiceControlState setActionButtons:]
+ -[CPVoiceControlTemplate handleActionForControlIdentifier:]
+ GCC_except_table118
+ GCC_except_table14
+ GCC_except_table29
+ GCC_except_table53
+ GCC_except_table61
+ GCC_except_table70
+ GCC_except_table95
+ _$s10Foundation4UUIDV19_bridgeToObjectiveCSo6NSUUIDCyF
+ _$s10Foundation4UUIDV3key_s6UInt32V5valuetMR
+ _$s10Foundation4UUIDV3key_s6UInt32V5valuetMd
+ _$s10Foundation4UUIDVACSHAAWL
+ _$s10Foundation4UUIDVACs23CustomStringConvertibleAAWL
+ _$s10Foundation4UUIDVSHAAMc
+ _$s10Foundation4UUIDVSgWOcTm
+ _$s10Foundation4UUIDVSgWOf
+ _$s10Foundation4UUIDV_s6UInt32VtMR
+ _$s10Foundation4UUIDV_s6UInt32VtMd
+ _$s10Foundation4UUIDVs23CustomStringConvertibleAAMc
+ _$s7CarPlay17RouteSharingStateC14legIdentifiersSDy10Foundation4UUIDVs6UInt32VGvMTq
+ _$s7CarPlay17RouteSharingStateC14legIdentifiersSDy10Foundation4UUIDVs6UInt32VGvgTq
+ _$s7CarPlay17RouteSharingStateC14legIdentifiersSDy10Foundation4UUIDVs6UInt32VGvpWvd
+ _$s7CarPlay17RouteSharingStateC14legIdentifiersSDy10Foundation4UUIDVs6UInt32VGvsTq
+ _$s7CarPlay17RouteSharingStateC15currentLegIndexs6UInt32VSgvg
+ _$s7CarPlay17RouteSharingStateC15currentLegIndexs6UInt32VSgvgTq
+ _$s7CarPlay17RouteSharingStateC20currentLegIdentifier10Foundation4UUIDVSgvMTq
+ _$s7CarPlay17RouteSharingStateC20currentLegIdentifier10Foundation4UUIDVSgvW
+ _$s7CarPlay17RouteSharingStateC20currentLegIdentifier10Foundation4UUIDVSgvgTq
+ _$s7CarPlay17RouteSharingStateC20currentLegIdentifier10Foundation4UUIDVSgvpWvd
+ _$s7CarPlay17RouteSharingStateC20currentLegIdentifier10Foundation4UUIDVSgvsTq
+ _$s7CarPlay17RouteSharingStateCACycfc
+ _$sBbWV
+ _$sSD17dictionaryLiteralSDyxq_Gx_q_td_tcfC10Foundation4UUIDV_s6UInt32VTt0g5Tf4g_n
+ _$sSH13_rawHashValue4seedS2i_tFTj
+ _$sSKsSS7ElementRtzrlE6joined9separatorS2S_tF
+ _$sSSN
+ _$sSaySSGMR
+ _$sSaySSGMd
+ _$sSaySSGSayxGSKsWL
+ _$sSaySSGSayxGSKsWl
+ _$sSayxGSKsMc
+ _$sSo21CPVehicleStateManagerC7CarPlayE19routeSharingService_24didUpdateCurrentLegIndexySo08CAFRouteG0C_s6UInt32VtF
+ _$sSo21CPVehicleStateManagerC7CarPlayE19routeSharingService_24didUpdateCurrentLegIndexySo08CAFRouteG0C_s6UInt32VtFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE19sendCurrentLegIndex33_8CF23B4C98753B3B7E23CE4A41E0DBB4LLyyF
+ _$sSo21CPVehicleStateManagerC7CarPlayE19sendCurrentLegIndex33_8CF23B4C98753B3B7E23CE4A41E0DBB4LLyyFTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE20currentLegIdentifier10Foundation4UUIDVSgvgTo
+ _$sSo21CPVehicleStateManagerC7CarPlayE20currentLegIdentifier10Foundation4UUIDVSgvs
+ _$sSo21CPVehicleStateManagerC7CarPlayE20currentLegIdentifier10Foundation4UUIDVSgvsTo
+ _$sSo26CRBridgeRouteSharingStatusVSQSCSQ2eeoiySbx_xtFZTW
+ _$ss10_HashTableV11startBucketAB0D0Vvg
+ _$ss10_HashTableV14occupiedBucket5afterAB0D0VAF_tF
+ _$ss15ContiguousArrayV16_createNewBuffer14bufferIsUnique15minimumCapacity13growForAppendySb_SiSbtFSS_Tg5
+ _$ss15_print_unlockedyyx_q_zts16TextOutputStreamR_r0_lF
+ _$ss17_NativeDictionaryV20_copyOrMoveAndResize8capacity12moveElementsySi_SbtF10Foundation4UUIDV_s6UInt32VTg5
+ _$ss17_NativeDictionaryV4copyyyF10Foundation4UUIDV_s6UInt32VTg5
+ _$ss18_DictionaryStorageC4copy8originalAByxq_Gs05__RawaB0C_tFZ
+ _$ss18_DictionaryStorageC6resize8original8capacity4moveAByxq_Gs05__RawaB0C_SiSbtFZ
+ _$ss18_DictionaryStorageC8allocate8capacityAByxq_GSi_tFZ
+ _$ss18_DictionaryStorageCMn
+ _$ss18_DictionaryStorageCy10Foundation4UUIDVs6UInt32VGMR
+ _$ss18_DictionaryStorageCy10Foundation4UUIDVs6UInt32VGMd
+ _$ss22_ContiguousArrayBufferV20_consumeAndCreateNew14bufferIsUnique15minimumCapacity13growForAppendAByxGSb_SiSbtFSS_Tg5
+ _$ss22__RawDictionaryStorageC4find_9hashValues10_HashTableV6BucketV6bucket_Sb5foundtx_SitSHRzlF10Foundation4UUIDV_Tg5
+ _$ss22__RawDictionaryStorageC4findys10_HashTableV6BucketV6bucket_Sb5foundtxSHRzlF10Foundation4UUIDV_Tg5
+ _$ss23CustomStringConvertibleP11descriptionSSvgTj
+ _$ss23_ContiguousArrayStorageCySSGMR
+ _$ss23_ContiguousArrayStorageCySSGMd
+ _$ss26DefaultStringInterpolationVN
+ _$ss26DefaultStringInterpolationVs16TextOutputStreamsWP
+ _$ss53KEY_TYPE_OF_DICTIONARY_VIOLATES_HASHABLE_REQUIREMENTSys5NeverOypXpF
+ _$ss6UInt32VMn
+ _$ss6UInt32VN
+ _$ss6UInt32Vs23CustomStringConvertiblesWP
+ _BSEqualStrings
+ _CAFCharacteristicTypeCurrentLegIndex
+ _CGFloatNearlyEqualToFloat
+ _CLLocationCoordinate2DIsValid
+ _CLLocationCoordinate2DMake
+ _CLLocationDistanceMax
+ _CMTimeGetSeconds
+ _CMTimeMake
+ _CPCurrentProcessHasVoiceConversationalEntitlement
+ _CPVoiceConversationalTemplateClasses
+ _CPVoiceConversationalTemplateClasses.classes
+ _CPVoiceConversationalTemplateClasses.cold.1
+ _CPVoiceConversationalTemplateClasses.onceToken
+ _EAAccessoryDidConnectNotification
+ _EAVehicleInfoMapsDisplayNameKey
+ _NSLocaleLanguageCode
+ _OBJC_CLASS_$_CADisplay
+ _OBJC_CLASS_$_CPImageOverlay
+ _OBJC_CLASS_$_CPListTemplateDetailsHeader
+ _OBJC_CLASS_$_CPMapTemplateWaypoint
+ _OBJC_CLASS_$_CPPlaybackConfiguration
+ _OBJC_CLASS_$_CPRouteSegment
+ _OBJC_CLASS_$_CPSportsOverlay
+ _OBJC_CLASS_$_CPThumbnailImage
+ _OBJC_CLASS_$_CRVehicleAccessoryManager
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSTimeZone
+ _OBJC_CLASS_$_NSTimer
+ _OBJC_CLASS_$_NSURLComponents
+ _OBJC_IVAR_$_CPImageOverlay._alignment
+ _OBJC_IVAR_$_CPImageOverlay._backgroundColor
+ _OBJC_IVAR_$_CPImageOverlay._image
+ _OBJC_IVAR_$_CPImageOverlay._text
+ _OBJC_IVAR_$_CPImageOverlay._textColor
+ _OBJC_IVAR_$_CPImageSet._computedHashAtInitialization
+ _OBJC_IVAR_$_CPListImageRowItemCardElement._thumbnail
+ _OBJC_IVAR_$_CPListImageRowItemElement._accessibilityLabel
+ _OBJC_IVAR_$_CPListImageRowItemElement._playbackConfiguration
+ _OBJC_IVAR_$_CPListItem._playbackConfiguration
+ _OBJC_IVAR_$_CPListTemplate._listHeader
+ _OBJC_IVAR_$_CPListTemplateDetailsHeader._actionButtons
+ _OBJC_IVAR_$_CPListTemplateDetailsHeader._adaptiveBackgroundStyle
+ _OBJC_IVAR_$_CPListTemplateDetailsHeader._bodyVariants
+ _OBJC_IVAR_$_CPListTemplateDetailsHeader._listTemplate
+ _OBJC_IVAR_$_CPListTemplateDetailsHeader._metadataTitleVariants
+ _OBJC_IVAR_$_CPListTemplateDetailsHeader._playbackConfiguration
+ _OBJC_IVAR_$_CPListTemplateDetailsHeader._subtitle
+ _OBJC_IVAR_$_CPListTemplateDetailsHeader._thumbnail
+ _OBJC_IVAR_$_CPListTemplateDetailsHeader._title
+ _OBJC_IVAR_$_CPMapTemplate._currentNavigationSession
+ _OBJC_IVAR_$_CPMapTemplateWaypoint._travelEstimates
+ _OBJC_IVAR_$_CPMapTemplateWaypoint._waypoint
+ _OBJC_IVAR_$_CPNavigationManager._currentLeg
+ _OBJC_IVAR_$_CPNavigationSession._currentSegment
+ _OBJC_IVAR_$_CPNavigationSession._routeSegments
+ _OBJC_IVAR_$_CPNavigationSession._supportsRouteSharing
+ _OBJC_IVAR_$_CPNavigationWaypoint._timeZone
+ _OBJC_IVAR_$_CPPlaybackConfiguration._duration
+ _OBJC_IVAR_$_CPPlaybackConfiguration._elapsedTime
+ _OBJC_IVAR_$_CPPlaybackConfiguration._playbackAction
+ _OBJC_IVAR_$_CPPlaybackConfiguration._playbackState
+ _OBJC_IVAR_$_CPPlaybackConfiguration._preferredPresentation
+ _OBJC_IVAR_$_CPPlaybackConfiguration._progress
+ _OBJC_IVAR_$_CPRouteInfo._currentLeg
+ _OBJC_IVAR_$_CPRouteLeg._identifier
+ _OBJC_IVAR_$_CPRouteSegment._coordinates
+ _OBJC_IVAR_$_CPRouteSegment._coordinatesCount
+ _OBJC_IVAR_$_CPRouteSegment._currentLaneGuidance
+ _OBJC_IVAR_$_CPRouteSegment._currentManeuvers
+ _OBJC_IVAR_$_CPRouteSegment._destination
+ _OBJC_IVAR_$_CPRouteSegment._identifier
+ _OBJC_IVAR_$_CPRouteSegment._laneGuidances
+ _OBJC_IVAR_$_CPRouteSegment._maneuverTravelEstimates
+ _OBJC_IVAR_$_CPRouteSegment._maneuvers
+ _OBJC_IVAR_$_CPRouteSegment._origin
+ _OBJC_IVAR_$_CPRouteSegment._tripTravelEstimates
+ _OBJC_IVAR_$_CPSessionConfiguration._supportsVideoPlayback
+ _OBJC_IVAR_$_CPSportsOverlay._eventStatus
+ _OBJC_IVAR_$_CPSportsOverlay._leftTeam
+ _OBJC_IVAR_$_CPSportsOverlay._rightTeam
+ _OBJC_IVAR_$_CPThumbnailImage._aspectRatio
+ _OBJC_IVAR_$_CPThumbnailImage._identifier
+ _OBJC_IVAR_$_CPThumbnailImage._image
+ _OBJC_IVAR_$_CPThumbnailImage._imageOverlay
+ _OBJC_IVAR_$_CPThumbnailImage._playbackProgress
+ _OBJC_IVAR_$_CPThumbnailImage._sportsOverlay
+ _OBJC_IVAR_$_CPThumbnailImage._thumbnailUpdater
+ _OBJC_IVAR_$_CPTrip._destinationWaypoint
+ _OBJC_IVAR_$_CPTrip._hasShareableDestination
+ _OBJC_IVAR_$_CPTrip._originWaypoint
+ _OBJC_IVAR_$_CPTrip._routeSegmentsAvailableForRegion
+ _OBJC_IVAR_$_CPVoiceControlState._actionButtons
+ _OBJC_METACLASS_$_CPImageOverlay
+ _OBJC_METACLASS_$_CPListTemplateDetailsHeader
+ _OBJC_METACLASS_$_CPMapTemplateWaypoint
+ _OBJC_METACLASS_$_CPPlaybackConfiguration
+ _OBJC_METACLASS_$_CPRouteSegment
+ _OBJC_METACLASS_$_CPSportsOverlay
+ _OBJC_METACLASS_$_CPThumbnailImage
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ __OBJC_$_CATEGORY_CADisplay_$_CPAdditions
+ __OBJC_$_CATEGORY_CLASS_METHODS_CADisplay_$_CPAdditions
+ __OBJC_$_CLASS_METHODS_CPImageOverlay
+ __OBJC_$_CLASS_METHODS_CPListTemplateDetailsHeader
+ __OBJC_$_CLASS_METHODS_CPPlaybackConfiguration
+ __OBJC_$_CLASS_METHODS_CPSportsOverlay
+ __OBJC_$_CLASS_METHODS_CPThumbnailImage
+ __OBJC_$_CLASS_PROP_LIST_CPImageOverlay
+ __OBJC_$_CLASS_PROP_LIST_CPListTemplateDetailsHeader
+ __OBJC_$_CLASS_PROP_LIST_CPPlaybackConfiguration
+ __OBJC_$_CLASS_PROP_LIST_CPSportsOverlay
+ __OBJC_$_CLASS_PROP_LIST_CPThumbnailImage
+ __OBJC_$_INSTANCE_METHODS_CPImageOverlay
+ __OBJC_$_INSTANCE_METHODS_CPListTemplateDetailsHeader
+ __OBJC_$_INSTANCE_METHODS_CPMapTemplateWaypoint
+ __OBJC_$_INSTANCE_METHODS_CPPlaybackConfiguration
+ __OBJC_$_INSTANCE_METHODS_CPRouteSegment
+ __OBJC_$_INSTANCE_METHODS_CPSportsOverlay
+ __OBJC_$_INSTANCE_METHODS_CPThumbnailImage
+ __OBJC_$_INSTANCE_VARIABLES_CPImageOverlay
+ __OBJC_$_INSTANCE_VARIABLES_CPListTemplateDetailsHeader
+ __OBJC_$_INSTANCE_VARIABLES_CPMapTemplateWaypoint
+ __OBJC_$_INSTANCE_VARIABLES_CPPlaybackConfiguration
+ __OBJC_$_INSTANCE_VARIABLES_CPRouteSegment
+ __OBJC_$_INSTANCE_VARIABLES_CPSportsOverlay
+ __OBJC_$_INSTANCE_VARIABLES_CPThumbnailImage
+ __OBJC_$_PROP_LIST_CPImageOverlay
+ __OBJC_$_PROP_LIST_CPListTemplateDetailsHeader
+ __OBJC_$_PROP_LIST_CPMapTemplateWaypoint
+ __OBJC_$_PROP_LIST_CPPlayableItem
+ __OBJC_$_PROP_LIST_CPPlaybackConfiguration
+ __OBJC_$_PROP_LIST_CPRouteSegment
+ __OBJC_$_PROP_LIST_CPSportsOverlay
+ __OBJC_$_PROP_LIST_CPThumbnailImage
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CPPlayableItem
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CPMapTemplateProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CPNavigationSessionManaging
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CPTemplateProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CPThumbnailUpdating
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CPVoiceControlTemplateDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPPlayableItem
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPThumbnailUpdating
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CPVoiceControlTemplateDelegate
+ __OBJC_$_PROTOCOL_REFS_CPPlayableItem
+ __OBJC_$_PROTOCOL_REFS_CPThumbnailUpdating
+ __OBJC_CLASS_PROTOCOLS_$_CPImageOverlay
+ __OBJC_CLASS_PROTOCOLS_$_CPListImageRowItemCardElement
+ __OBJC_CLASS_PROTOCOLS_$_CPListTemplateDetailsHeader
+ __OBJC_CLASS_PROTOCOLS_$_CPPlaybackConfiguration
+ __OBJC_CLASS_PROTOCOLS_$_CPRouteSegment
+ __OBJC_CLASS_PROTOCOLS_$_CPSportsOverlay
+ __OBJC_CLASS_PROTOCOLS_$_CPThumbnailImage
+ __OBJC_CLASS_RO_$_CPImageOverlay
+ __OBJC_CLASS_RO_$_CPListTemplateDetailsHeader
+ __OBJC_CLASS_RO_$_CPMapTemplateWaypoint
+ __OBJC_CLASS_RO_$_CPPlaybackConfiguration
+ __OBJC_CLASS_RO_$_CPRouteSegment
+ __OBJC_CLASS_RO_$_CPSportsOverlay
+ __OBJC_CLASS_RO_$_CPThumbnailImage
+ __OBJC_LABEL_PROTOCOL_$_CPPlayableItem
+ __OBJC_LABEL_PROTOCOL_$_CPThumbnailUpdating
+ __OBJC_METACLASS_RO_$_CPImageOverlay
+ __OBJC_METACLASS_RO_$_CPListTemplateDetailsHeader
+ __OBJC_METACLASS_RO_$_CPMapTemplateWaypoint
+ __OBJC_METACLASS_RO_$_CPPlaybackConfiguration
+ __OBJC_METACLASS_RO_$_CPRouteSegment
+ __OBJC_METACLASS_RO_$_CPSportsOverlay
+ __OBJC_METACLASS_RO_$_CPThumbnailImage
+ __OBJC_PROTOCOL_$_CPPlayableItem
+ __OBJC_PROTOCOL_$_CPThumbnailUpdating
+ ___31-[CPListTemplate performUpdate]_block_invoke.130
+ ___32-[CPListTemplate setListHeader:]_block_invoke
+ ___38-[CPListImageRowItem reloadThumbnail:]_block_invoke
+ ___39-[CPNavigationManager _setupConnection]_block_invoke.358
+ ___39-[CPNavigationManager _setupConnection]_block_invoke.359
+ ___39-[CPNavigationManager _setupConnection]_block_invoke.361
+ ___40-[CPNavigationSession addRouteSegments:]_block_invoke
+ ___43+[CADisplay(CPAdditions) cp_displayWithID:]_block_invoke
+ ___43-[CPImageSet initWithImage:treatmentBlock:]_block_invoke
+ ___43-[CPImageSet initWithImage:treatmentBlock:]_block_invoke_2
+ ___43-[CPListTemplateDetailsHeader updateHeader]_block_invoke
+ ___45+[CPThumbnailImage convertImage:aspectRatio:]_block_invoke
+ ___47-[CPListTemplateDetailsHeader reloadThumbnail:]_block_invoke
+ ___47-[CPMapTemplate startNavigationSessionForTrip:]_block_invoke.32
+ ___47-[CPNavigationSession setSupportsRouteSharing:]_block_invoke
+ ___49-[CPNavigationManager didUpdateActiveComponents:]_block_invoke.370
+ ___50-[CPMapTemplate handleActionForControlIdentifier:]_block_invoke.45
+ ___51-[CPMapTemplate clientWaypointReceivedFromVehicle:]_block_invoke
+ ___51-[CPMapTemplate clientWaypointReceivedFromVehicle:]_block_invoke.140
+ ___51-[CPMapTemplate clientWaypointReceivedFromVehicle:]_block_invoke.141
+ ___51-[CPMapTemplate clientWaypointReceivedFromVehicle:]_block_invoke.cold.1
+ ___51-[CPMapTemplate clientWaypointReceivedFromVehicle:]_block_invoke.cold.2
+ ___52-[CPInterfaceController _connectToListenerEndpoint:]_block_invoke.470
+ ___52-[CPInterfaceController _connectToListenerEndpoint:]_block_invoke.470.cold.1
+ ___52-[CPInterfaceController _connectToListenerEndpoint:]_block_invoke.471
+ ___53-[CPTemplateApplicationScene _refreshTraitCollection]_block_invoke
+ ___54-[CPInterfaceController _completeSetupWithCompletion:]_block_invoke_5
+ ___54-[CPInterfaceController _completeSetupWithCompletion:]_block_invoke_6
+ ___54-[CPInterfaceController _completeSetupWithCompletion:]_block_invoke_7
+ ___54-[CPInterfaceController _completeSetupWithCompletion:]_block_invoke_8
+ ___54-[CPMapTemplate clientDestinationWillBeSharedForTrip:]_block_invoke
+ ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.344
+ ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.344.cold.1
+ ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.350
+ ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.350.cold.1
+ ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.351
+ ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.351.cold.1
+ ___57-[CPNavigationSession startNavigationForCurrentRouteInfo]_block_invoke
+ ___58+[CPListImageRowItemCardElement convertImage:aspectRatio:]_block_invoke
+ ___58-[CPNavigationManager _showRouteSharingWarmingForVehicle:]_block_invoke.323
+ ___58-[CPNavigationManager _showRouteSharingWarmingForVehicle:]_block_invoke.323.cold.1
+ ___58-[CPNavigationManager _showRouteSharingWarmingForVehicle:]_block_invoke.327
+ ___58-[CPNavigationManager _showRouteSharingWarmingForVehicle:]_block_invoke.332
+ ___58-[CPNavigationManager _showRouteSharingWarmingForVehicle:]_block_invoke.332.cold.1
+ ___58-[CPNavigationManager handleSharedDestination:completion:]_block_invoke
+ ___58-[CPNavigationManager handleSharedDestination:completion:]_block_invoke.257
+ ___58-[CPNavigationManager handleSharedDestination:completion:]_block_invoke_2
+ ___60-[CPMapTemplate clientDestinationSharedFailedForTrip:error:]_block_invoke
+ ___60-[CPMapTemplate clientDestinationSharedSuccessfullyForTrip:]_block_invoke
+ ___60-[CPMapTemplate clientRouteSourceUpdateReceivedFromVehicle:]_block_invoke
+ ___60-[CPMapTemplate clientRouteSourceUpdateReceivedFromVehicle:]_block_invoke.cold.1
+ ___61-[CPMapTemplate clientDestinationRequestReceivedFromVehicle:]_block_invoke
+ ___61-[CPMapTemplate clientDestinationRequestReceivedFromVehicle:]_block_invoke.cold.1
+ ___62-[CPInterfaceController clientPushNowPlayingTemplateAnimated:]_block_invoke.486
+ ___62-[CPTemplateApplicationDashboardScene _refreshTraitCollection]_block_invoke
+ ___65-[CPInterfaceController _pushTabBarTemplate:animated:completion:]_block_invoke.58
+ ___65-[CPNavigationManager initWithIdentifier:delegate:sessionStatus:]_block_invoke.210
+ ___70-[CPTemplateApplicationInstrumentClusterScene _refreshTraitCollection]_block_invoke
+ ___80-[CPImageSetAssetRegistration initWithLightImage:darkImage:baseTraitCollection:]_block_invoke
+ ___80-[CPImageSetAssetRegistration initWithLightImage:darkImage:baseTraitCollection:]_block_invoke_2
+ ___87-[CPNavigationSession resumeTripWithUpdatedRouteSegments:currentSegment:rerouteReason:]_block_invoke
+ ___89-[CPInterfaceController _pushVoiceControlTemplate:presentationStyle:animated:completion:]_block_invoke
+ ___96-[CPListTemplate listTemplateWithIdentifier:didSelectImageAtIndex:inImageRowItemWithIdentifier:]_block_invoke.156
+ ___CPSanitizedBackgroundColor_block_invoke
+ ___CPSanitizedBackgroundColor_block_invoke_2
+ ___CPSanitizedBackgroundColor_block_invoke_3
+ ___CPVoiceConversationalTemplateClasses_block_invoke
+ ___block_descriptor_32_e27_v16?0"<UIMutableTraits>"8l
+ ___block_descriptor_36_e19_B16?0"CADisplay"8l
+ ___block_descriptor_40_e8_32s_e18_v16?0"NSNumber"8ls32l8
+ ___block_descriptor_48_e8_32r40r_e5_v8?0lr32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e27_v16?0"<UIMutableTraits>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e27_v16?0"CPTravelEstimates"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e39_v16?0"<CPNavigationSessionManaging>"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s_e27_v16?0"<UIMutableTraits>"8ls32l8
+ ___block_descriptor_58_e8_32s40s48s_e39_v16?0"<CPNavigationSessionManaging>"8ls32l8s40l8s48l8
+ ___block_descriptor_58_e8_32s40s48s_e40_v16?0"<CPNavigationSessionProviding>"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40bs48bs56w_e17_v16?0"NSTimer"8ls32l8s40l8w56l8s48l8
+ ___block_descriptor_64_e8_32s40bs48bs56w_e24_v16?0"NSNotification"8ls32l8s40l8w56l8s48l8
+ ___block_descriptor_64_e8_32s40s48s_e39_v16?0"<CPNavigationSessionManaging>"8ls32l8s40l8s48l8
+ ___block_literal_global.159
+ ___block_literal_global.285
+ ___block_literal_global.288
+ ___block_literal_global.290
+ ___block_literal_global.292
+ ___block_literal_global.295
+ ___block_literal_global.297
+ ___block_literal_global.299
+ ___block_literal_global.302
+ ___block_literal_global.304
+ ___block_literal_global.306
+ ___block_literal_global.326
+ ___block_literal_global.334
+ ___block_literal_global.346
+ ___block_literal_global.353
+ ___block_literal_global.364
+ ___block_literal_global.376
+ ___block_literal_global.42
+ ___block_literal_global.44
+ ___block_literal_global.477
+ ___block_literal_global.488
+ ___block_literal_global.493
+ ___block_literal_global.501
+ ___block_literal_global.506
+ ___block_literal_global.53
+ ___block_literal_global.57
+ ___block_literal_global.631
+ ___block_literal_global.634
+ ___block_literal_global.636
+ ___block_literal_global.638
+ ___block_literal_global.640
+ ___block_literal_global.642
+ ___block_literal_global.644
+ ___block_literal_global.646
+ ___block_literal_global.648
+ ___block_literal_global.650
+ ___block_literal_global.652
+ ___block_literal_global.654
+ ___block_literal_global.656
+ ___block_literal_global.658
+ ___block_literal_global.7
+ ___block_literal_global.9
+ ___swift_instantiateConcreteTypeFromMangledNameAbstractV2
+ __maximumHeaderGridButtonCount
+ __maximumItemCount
+ __maximumNumberOfGridImages
+ __maximumSectionCount
+ __swiftEmptyDictionarySingleton
+ _bzero
+ _kCPSVoiceConversationalEntitlementKey
+ _objc_msgSend$_configureBaseRouteGuidance:
+ _objc_msgSend$_decodeNumberForParameter:fromDecoder:accNavType:
+ _objc_msgSend$_destinationHandoffErrorWithReason:
+ _objc_msgSend$_externalAccessoryDestinationInformationForDestination:
+ _objc_msgSend$_pushVoiceControlTemplate:presentationStyle:animated:completion:
+ _objc_msgSend$_setMaximumHeaderGridButtonCount:
+ _objc_msgSend$_setMaximumItemCount:
+ _objc_msgSend$_setMaximumNumberOfGridImages:
+ _objc_msgSend$_setMaximumSectionCount:
+ _objc_msgSend$_startNavigationWithRouteInfo:
+ _objc_msgSend$_updateLimitedUIStatusForSession:
+ _objc_msgSend$accessibilityLabel
+ _objc_msgSend$accessibilityValue
+ _objc_msgSend$alignment
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendString:
+ _objc_msgSend$applicationEnabled
+ _objc_msgSend$arrayWithCapacity:
+ _objc_msgSend$aspectRatio
+ _objc_msgSend$backgroundColor
+ _objc_msgSend$beingShownInApp
+ _objc_msgSend$bodyVariants
+ _objc_msgSend$bs_firstObjectPassingTest:
+ _objc_msgSend$carDidUpdateAccessories:
+ _objc_msgSend$carManager:didUpdateCurrentCar:
+ _objc_msgSend$centerPoint
+ _objc_msgSend$city
+ _objc_msgSend$clearNavigation
+ _objc_msgSend$clearRoute
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$componentsWithURL:resolvingAgainstBaseURL:
+ _objc_msgSend$computedHashAtInitialization
+ _objc_msgSend$connectedAccessories
+ _objc_msgSend$containsValueForKey:
+ _objc_msgSend$convertImage:aspectRatio:
+ _objc_msgSend$coordinates
+ _objc_msgSend$coordinates3D
+ _objc_msgSend$coordinates3DCount
+ _objc_msgSend$coordinatesCount
+ _objc_msgSend$copyForLoading
+ _objc_msgSend$copyWithZone:
+ _objc_msgSend$correctedAspectRatioForImage:
+ _objc_msgSend$country
+ _objc_msgSend$cp_displayWithID:
+ _objc_msgSend$currentCar
+ _objc_msgSend$currentCarPlayAccessory
+ _objc_msgSend$currentLeg
+ _objc_msgSend$currentLocale
+ _objc_msgSend$currentNavigationSession
+ _objc_msgSend$currentRouteGuidance
+ _objc_msgSend$currentSegment
+ _objc_msgSend$decodeInt64ForKey:
+ _objc_msgSend$decodeIntForKey:
+ _objc_msgSend$destinationLocation
+ _objc_msgSend$destinationWaypoint
+ _objc_msgSend$displayID
+ _objc_msgSend$displayId
+ _objc_msgSend$displayIdentity
+ _objc_msgSend$displays
+ _objc_msgSend$entryPoints
+ _objc_msgSend$entryPointsCount
+ _objc_msgSend$geodeticSystem
+ _objc_msgSend$getRouteLineForCurrentSegments
+ _objc_msgSend$getVehicleInfoData
+ _objc_msgSend$hasShareableDestination
+ _objc_msgSend$hostShowAddStopCardForWaypoint:withTravelEstimates:
+ _objc_msgSend$imageOverlay
+ _objc_msgSend$initWithAltitude:latitude:longitude:
+ _objc_msgSend$initWithCenterPoint:locationThreshold:name:address:entryPoints:entryPointsCount:timeZone:
+ _objc_msgSend$initWithCoordinates:destination:origin:
+ _objc_msgSend$initWithEntryPoints:location:locationThreshold:userVisibleAddress:userVisibleName:
+ _objc_msgSend$initWithItems:
+ _objc_msgSend$initWithOrigin:destination:maneuvers:laneGuidances:currentManeuvers:currentLaneGuidance:tripTravelEstimates:maneuverTravelEstimates:coordinates:coordinatesCount:
+ _objc_msgSend$initWithOriginWaypoint:destinationWaypoint:routeChoices:
+ _objc_msgSend$initWithPreferredPresentation:playbackState:progress:duration:
+ _objc_msgSend$initWithRouteGuidance:maneuvers:laneGuidances:routeLine:currentLeg:
+ _objc_msgSend$initWithService:characteristicType:value:
+ _objc_msgSend$listHeader
+ _objc_msgSend$localTimeZone
+ _objc_msgSend$locationThreshold
+ _objc_msgSend$manufacturer
+ _objc_msgSend$mapTemplate:didFailToShareDestinationForTrip:error:
+ _objc_msgSend$mapTemplate:didReceiveRequestForDestination:
+ _objc_msgSend$mapTemplate:didReceiveUpdatedRouteSource:
+ _objc_msgSend$mapTemplate:didRequestToInsertWaypoint:intoSegment:completion:
+ _objc_msgSend$mapTemplate:didShareDestinationForTrip:
+ _objc_msgSend$mapTemplate:mapTemplateWaypoint:accepted:forSegment:
+ _objc_msgSend$mapTemplate:willShareDestinationForTrip:
+ _objc_msgSend$mapTemplateShouldProvideRouteSharing:
+ _objc_msgSend$maximumActionButtonCount
+ _objc_msgSend$maximumImageSizeForAspectRatio:
+ _objc_msgSend$maximumNumberOfActionButtons
+ _objc_msgSend$maximumNumberOfGridImages
+ _objc_msgSend$metadataTitleVariants
+ _objc_msgSend$model
+ _objc_msgSend$navigation
+ _objc_msgSend$navigationAidedDrivingFeatureName
+ _objc_msgSend$navigationAidedDrivingFeatureShortName
+ _objc_msgSend$navigationName
+ _objc_msgSend$originLocation
+ _objc_msgSend$originWaypoint
+ _objc_msgSend$ownerString
+ _objc_msgSend$playbackAction
+ _objc_msgSend$playbackConfiguration
+ _objc_msgSend$playbackState
+ _objc_msgSend$pointOfInterestHandoffEnabled
+ _objc_msgSend$postalCode
+ _objc_msgSend$preferredImageRowMaximumNumberOfGridImagesWithReply:
+ _objc_msgSend$preferredListMaximumHeaderGridButtonCountWithReply:
+ _objc_msgSend$preferredListMaximumItemCountWithReply:
+ _objc_msgSend$preferredListMaximumSectionCountWithReply:
+ _objc_msgSend$preferredPresentation
+ _objc_msgSend$progress
+ _objc_msgSend$pushVoiceControlTemplate:withProxyDelegate:animated:presentationStyle:reply:
+ _objc_msgSend$queryItems
+ _objc_msgSend$receivedAllValues
+ _objc_msgSend$reloadThumbnail:
+ _objc_msgSend$reloadThumbnail:inListImageRowWithIdentifier:
+ _objc_msgSend$routeLegs
+ _objc_msgSend$routeLegsWithRouteLegs:
+ _objc_msgSend$routeSegments
+ _objc_msgSend$routeSegmentsAvailableForRegion
+ _objc_msgSend$routeSharing
+ _objc_msgSend$routeSharingService:didUpdateApplicationEnabled:
+ _objc_msgSend$routeSharingService:didUpdateUserEnabled:
+ _objc_msgSend$routeSharingService:didUpdateVehicleEnabled:
+ _objc_msgSend$routeStatus
+ _objc_msgSend$scheduledTimerWithTimeInterval:repeats:block:
+ _objc_msgSend$scheme
+ _objc_msgSend$sendCurrentLegIndex
+ _objc_msgSend$sendDestinationInformation:identifier:
+ _objc_msgSend$sendRoutingStates
+ _objc_msgSend$setApplicationEnabled:
+ _objc_msgSend$setCurrentLeg:
+ _objc_msgSend$setCurrentLegIdentifier:
+ _objc_msgSend$setCurrentLegIndex:
+ _objc_msgSend$setCurrentLegIndexInvalid
+ _objc_msgSend$setCurrentNavigationSession:
+ _objc_msgSend$setCurrentSegment:
+ _objc_msgSend$setDestination:
+ _objc_msgSend$setDisplayGamut:
+ _objc_msgSend$setDisplayScale:
+ _objc_msgSend$setGeodeticSystem:
+ _objc_msgSend$setInvalidatedUpdate:
+ _objc_msgSend$setLegs:
+ _objc_msgSend$setOrigin:
+ _objc_msgSend$setRerouteReason:
+ _objc_msgSend$setRouteSegments:
+ _objc_msgSend$setRouteState:
+ _objc_msgSend$setSharingState:
+ _objc_msgSend$setStopType:
+ _objc_msgSend$setThumbnailUpdater:
+ _objc_msgSend$setUserEnabled:
+ _objc_msgSend$setUserInterfaceIdiom:
+ _objc_msgSend$setUserInterfaceStyle:
+ _objc_msgSend$setUserVisibleApplicationName:
+ _objc_msgSend$setupInvalidateClearNavigationBatch
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$sourceName
+ _objc_msgSend$sourceSupportsRouteGuidance
+ _objc_msgSend$sportsOverlay
+ _objc_msgSend$startNavigationForCurrentRouteInfo
+ _objc_msgSend$startNavigationWithRouteInfo:
+ _objc_msgSend$state
+ _objc_msgSend$stopType
+ _objc_msgSend$street
+ _objc_msgSend$stringByRemovingPercentEncoding
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
+ _objc_msgSend$supportsCarPlay
+ _objc_msgSend$systemInformation
+ _objc_msgSend$systemInformationService:didUpdateRouteSource:
+ _objc_msgSend$textColor
+ _objc_msgSend$thumbnail
+ _objc_msgSend$thumbnailUpdater
+ _objc_msgSend$traitCollectionByModifyingTraits:
+ _objc_msgSend$traitCollectionWithTraits:
+ _objc_msgSend$travelEstimates
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSend$updateDetailsHeader:
+ _objc_msgSend$updateHeader
+ _objc_msgSend$updateNavigationOwnership
+ _objc_msgSend$updateThumbnail
+ _objc_msgSend$userEnabled
+ _objc_msgSend$userVisibleNavigationSystemName
+ _objc_msgSend$userVisibleVehicleBrand
+ _objc_msgSend$value
+ _objc_msgSend$vehicleEnabled
+ _objc_msgSend$vehicleForCurrentSession
+ _objc_msgSend$vehicleNavigationSystemName
+ _objc_msgSend$vehicleStateManager:didUpdateRouteSharingActive:
+ _objc_msgSend$vehicleStateManager:didUpdateRouteSharingUserEnabled:
+ _objc_msgSend$vehicleStateManager:didUpdateRouteSharingVehicleEnabled:
+ _objc_msgSend$vehicleStateManager:didUpdateRouteSource:
+ _objc_msgSend$vehicleStateManager:didUpdateSystemInfo:
+ _objc_msgSend$videoPlaybackSupported
+ _objc_msgSend$wantsAdaptiveBackgroundStyle
+ _objc_msgSend$waypoint
+ _swift_arrayInitWithCopy
+ _swift_getTypeByMangledNameInContextInMetadataState2
+ _symbolic SDy__________G 10Foundation4UUIDV s6UInt32V
+ _symbolic SaySSG
+ _symbolic _____3key______5valuet 10Foundation4UUIDV s6UInt32V
+ _symbolic ___________t 10Foundation4UUIDV s6UInt32V
+ _symbolic _____ySSG s23_ContiguousArrayStorageC
+ _symbolic _____y__________G s18_DictionaryStorageC 10Foundation4UUIDV s6UInt32V
- -[CPNavigationManager _startNavigationWithRouteInfo:originalState:]
- -[CPNavigationManager _vehicleForCurrentSession]
- -[CPNavigationManager startNavigationWithRouteInfo:].cold.1
- -[CPRouteChoice isEqual:]
- -[CPSessionConfiguration _updateLimitedUIStatus]
- GCC_except_table112
- GCC_except_table25
- GCC_except_table40
- GCC_except_table51
- GCC_except_table55
- GCC_except_table68
- GCC_except_table85
- _$s10Foundation4UUIDVSgWOc
- _$sSo20CAFSystemInformationC7CarPlayE14cpBridgedBrandSSvgTm
- _$sSo20CAFSystemInformationC7CarPlayE14cpBridgedBrandSSvgToTm
- _$sSo21CPVehicleStateManagerC7CarPlayE07currentD033_8CF23B4C98753B3B7E23CE4A41E0DBB4LLSo6CAFCarCSgvgToTm
- _$sSo21CPVehicleStateManagerC7CarPlayE17systemInformation33_8CF23B4C98753B3B7E23CE4A41E0DBB4LLSo09CAFSystemG0CSgvgToTm
- _$sSo21CPVehicleStateManagerC7CarPlayE19routeSharingService_20didUpdateUserEnabledySo08CAFRouteG0C_SbtFTm
- _$sSo21CPVehicleStateManagerC7CarPlayE19routeSharingService_20didUpdateUserEnabledySo08CAFRouteG0C_SbtFToTm
- _$sSo21CPVehicleStateManagerC7CarPlayE23routeSharingUserEnabledSbvgToTm
- _OBJC_CLASS_$_CLPlacemark
- _OBJC_CLASS_$_MKPlacemark
- ___31-[CPListTemplate performUpdate]_block_invoke.126
- ___39-[CPNavigationManager _setupConnection]_block_invoke.294
- ___39-[CPNavigationManager _setupConnection]_block_invoke.295
- ___39-[CPNavigationManager _setupConnection]_block_invoke.297
- ___47-[CPMapTemplate startNavigationSessionForTrip:]_block_invoke.30
- ___49-[CPNavigationManager didUpdateActiveComponents:]_block_invoke.306
- ___50-[CPMapTemplate handleActionForControlIdentifier:]_block_invoke.43
- ___52-[CPInterfaceController _connectToListenerEndpoint:]_block_invoke.431
- ___52-[CPInterfaceController _connectToListenerEndpoint:]_block_invoke.431.cold.1
- ___52-[CPInterfaceController _connectToListenerEndpoint:]_block_invoke.432
- ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.280
- ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.280.cold.1
- ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.286
- ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.286.cold.1
- ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.287
- ___56-[CPNavigationManager _showRouteSharingPopupForVehicle:]_block_invoke.287.cold.1
- ___58-[CPNavigationManager _showRouteSharingWarmingForVehicle:]_block_invoke.259
- ___58-[CPNavigationManager _showRouteSharingWarmingForVehicle:]_block_invoke.259.cold.1
- ___58-[CPNavigationManager _showRouteSharingWarmingForVehicle:]_block_invoke.263
- ___58-[CPNavigationManager _showRouteSharingWarmingForVehicle:]_block_invoke.268
- ___58-[CPNavigationManager _showRouteSharingWarmingForVehicle:]_block_invoke.268.cold.1
- ___62-[CPInterfaceController clientPushNowPlayingTemplateAnimated:]_block_invoke.446
- ___65-[CPInterfaceController _pushTabBarTemplate:animated:completion:]_block_invoke.54
- ___67-[CPNavigationManager _startNavigationWithRouteInfo:originalState:]_block_invoke
- ___96-[CPListTemplate listTemplateWithIdentifier:didSelectImageAtIndex:inImageRowItemWithIdentifier:]_block_invoke.152
- ___block_descriptor_33_e25_v16?0"CPRouteGuidance"8l
- ___block_descriptor_56_e8_32s40s48s_e40_v16?0"<CPNavigationSessionProviding>"8ls32l8s40l8s48l8
- ___block_literal_global.155
- ___block_literal_global.219
- ___block_literal_global.223
- ___block_literal_global.225
- ___block_literal_global.227
- ___block_literal_global.230
- ___block_literal_global.233
- ___block_literal_global.235
- ___block_literal_global.238
- ___block_literal_global.240
- ___block_literal_global.242
- ___block_literal_global.262
- ___block_literal_global.270
- ___block_literal_global.282
- ___block_literal_global.289
- ___block_literal_global.300
- ___block_literal_global.312
- ___block_literal_global.437
- ___block_literal_global.448
- ___block_literal_global.453
- ___block_literal_global.461
- ___block_literal_global.466
- ___block_literal_global.51
- ___block_literal_global.55
- ___block_literal_global.590
- ___block_literal_global.593
- ___block_literal_global.595
- ___block_literal_global.597
- ___block_literal_global.599
- ___block_literal_global.601
- ___block_literal_global.603
- ___block_literal_global.605
- ___block_literal_global.607
- ___block_literal_global.609
- ___block_literal_global.611
- ___block_literal_global.613
- ___block_literal_global.615
- ___block_literal_global.8
- __swift_FORCE_LOAD_$_swiftAccelerate
- __swift_FORCE_LOAD_$_swiftAccelerate_$_CarPlay
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend$CADisplay
- _objc_msgSend$_startNavigationWithRouteInfo:originalState:
- _objc_msgSend$_updateLimitedUIStatus
- _objc_msgSend$_vehicleForCurrentSession
- _objc_msgSend$displayConfiguration
- _objc_msgSend$encodeInt32:forKey:
- _objc_msgSend$initWithCenterPoint:locationThreshold:name:address:entryPoints:entryPointsCount:
- _objc_msgSend$initWithPlacemark:
- _objc_msgSend$placemarkWithLocation:name:postalAddress:
- _objc_msgSend$traitCollectionWithDisplayGamut:
- _objc_msgSend$traitCollectionWithDisplayScale:
- _objc_msgSend$traitCollectionWithTraitsFromCollections:
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ " "
+ "%s currentLegIdentifier=%s currentLegIndex=%s legIdentifiers=[%s] routeSharing=%@"
+ "%s: accessory connected"
+ "("
+ "+"
+ ","
+ ", destination = %@"
+ ", identifier = %@"
+ ", origin = %@"
+ "-[CPNavigationManager _handleAccessoryDidConnect:]"
+ "<%@: %p"
+ "<%@: %p, waypoint: %@, travelEstimates: %@>"
+ ">"
+ "@\"<CPThumbnailUpdating>\""
+ "@\"CPImageOverlay\""
+ "@\"CPListTemplateDetailsHeader\""
+ "@\"CPNavigationSession\""
+ "@\"CPPlaybackConfiguration\""
+ "@\"CPPlaybackConfiguration\"16@0:8"
+ "@\"CPRouteLeg\""
+ "@\"CPRouteSegment\""
+ "@\"CPSportsOverlay\""
+ "@\"CPThumbnailImage\""
+ "@\"NSTimeZone\""
+ "@20@0:8I16"
+ "@32@0:8@16q24"
+ "@36@0:8q16B24d28"
+ "@40@0:8@16@24q32"
+ "@40@0:8q16q24d32"
+ "@48@0:8@16@24@32d40"
+ "@48@0:8@16@24@32q40"
+ "@48@0:8q16@24@32@40"
+ "@48@0:8q16q24d32d40"
+ "@56@0:8@16@24@32@40@48"
+ "@64@0:8q16q24{?=qiIq}32d56"
+ "@88@0:8{?=ddd}16@40@48@56^{?=ddd}64Q72@80"
+ "@96@0:8@16@24@32@40@48@56@64@72^{?=ddd}80q88"
+ "Address"
+ "Application declares voice entitlement."
+ "B16@?0@\"CADisplay\"8"
+ "CPAdditions"
+ "CPImageOverlay"
+ "CPListImageRowItem setting MaximumNumberOfGridImages (%{public}@"
+ "CPListTemplate setting MaximumGridButtonImageSize (%{public}f,%{public}f)"
+ "CPListTemplate setting MaximumHeaderGridButtonCount %lu"
+ "CPListTemplate setting MaximumItemCount %lu"
+ "CPListTemplate setting MaximumSectionCount %lu"
+ "CPListTemplateDetailsHeader"
+ "CPMapTemplateWaypoint"
+ "CPNavigationManagerErrorDomain"
+ "CPPlayableItem"
+ "CPPlaybackConfiguration"
+ "CPRouteSegment"
+ "CPSportsOverlay"
+ "CPThumbnailImage"
+ "CPThumbnailUpdating"
+ "CenterCoordinate"
+ "CoordinateThreshold"
+ "Destination handoff failed"
+ "Destination handoff timed out"
+ "Destination sharing result - ID: %@, Success: %@, Parameters: %@"
+ "Destination sharing timed out for identifier: %@"
+ "DisplayName"
+ "EAAccessoryDestinationStatusDidSucceedKey"
+ "EAAccessoryDestinationStatusIdentifierKey"
+ "EAAccessoryDestinationStatusNotification"
+ "EAAccessoryDestinationStatusParametersUsedKey"
+ "EntryPoints"
+ "Invalid destination or completion handler"
+ "Invalid parameters for destination sharing"
+ "Locale"
+ "Mandated"
+ "Map delegate does not support receiving Route Source updates from vehicle."
+ "Map delegate does not support receiving requestUI destination updates."
+ "Map delegate does not support waypoint insertion: mapTemplate:didRequestToInsertWaypoint:intoSegment:completion:"
+ "No connected accessory available"
+ "No connected accessory available for destination sharing"
+ "No destination information available"
+ "No destination information available for trip"
+ "Sending destination information with identifier: %@"
+ "T@\"<CPThumbnailUpdating>\",W,N,V_thumbnailUpdater"
+ "T@\"CPBarButton\",&,D,N"
+ "T@\"CPImageOverlay\",&,N,V_imageOverlay"
+ "T@\"CPListTemplateDetailsHeader\",&,N,V_listHeader"
+ "T@\"CPNavigationSession\",&,N,V_currentNavigationSession"
+ "T@\"CPNavigationWaypoint\",&,N,V_waypoint"
+ "T@\"CPNavigationWaypoint\",R,N,V_destination"
+ "T@\"CPNavigationWaypoint\",R,N,V_destinationWaypoint"
+ "T@\"CPNavigationWaypoint\",R,N,V_origin"
+ "T@\"CPNavigationWaypoint\",R,N,V_originWaypoint"
+ "T@\"CPPlaybackConfiguration\",C,N"
+ "T@\"CPPlaybackConfiguration\",C,N,V_playbackConfiguration"
+ "T@\"CPRouteLeg\",&,N,V_currentLeg"
+ "T@\"CPRouteLeg\",R,N,V_currentLeg"
+ "T@\"CPRouteSegment\",&,N,V_currentSegment"
+ "T@\"CPSportsOverlay\",&,N,V_sportsOverlay"
+ "T@\"CPThumbnailImage\",&,N,V_thumbnail"
+ "T@\"CPTravelEstimates\",&,N,V_travelEstimates"
+ "T@\"NSArray\",C,N,V_bodyVariants"
+ "T@\"NSArray\",C,N,V_metadataTitleVariants"
+ "T@\"NSMeasurement\",R,N,V_locationThreshold"
+ "T@\"NSMutableArray\",&,N,V_routeSegments"
+ "T@\"NSString\",C,N,V_accessibilityLabel"
+ "T@\"NSTimeZone\",R,N,V_timeZone"
+ "T@\"NSUUID\",N,C"
+ "T@\"UIColor\",R,N,V_backgroundColor"
+ "T@\"UIColor\",R,N,V_textColor"
+ "TB,?,N"
+ "TB,N,GwantsAdaptiveBackgroundStyle,V_adaptiveBackgroundStyle"
+ "TB,N,V_hasShareableDestination"
+ "TB,N,V_routeSegmentsAvailableForRegion"
+ "TB,N,V_supportsRouteSharing"
+ "TB,R,N,GisPlaying"
+ "TB,R,N,V_supportsVideoPlayback"
+ "TQ,N,V_computedHashAtInitialization"
+ "T^{?=ddd},R,N,V_coordinates"
+ "Td,R,N"
+ "Td,R,N,V_aspectRatio"
+ "Td,R,N,V_playbackProgress"
+ "Td,R,N,V_progress"
+ "Tq,R,N,V_alignment"
+ "Tq,R,N,V_coordinatesCount"
+ "Tq,R,N,V_geodeticSystem"
+ "Tq,R,N,V_playbackAction"
+ "Tq,R,N,V_playbackState"
+ "Tq,R,N,V_preferredPresentation"
+ "T{?=qiIq},R,N,V_elapsedTime"
+ "Waypoint insertion completed with travel estimates: %@"
+ "_accessibilityLabel"
+ "_adaptiveBackgroundStyle"
+ "_alignment"
+ "_aspectRatio"
+ "_backgroundColor"
+ "_bodyVariants"
+ "_computedHashAtInitialization"
+ "_configureBaseRouteGuidance:"
+ "_coordinates"
+ "_coordinatesCount"
+ "_currentLeg"
+ "_currentNavigationSession"
+ "_currentSegment"
+ "_decodeNumberForParameter:fromDecoder:accNavType:"
+ "_destinationHandoffErrorWithReason:"
+ "_destinationWaypoint"
+ "_elapsedTime"
+ "_externalAccessoryDestinationInformationForDestination:"
+ "_handleAccessoryDidConnect:"
+ "_hasShareableDestination"
+ "_imageOverlay"
+ "_listHeader"
+ "_metadataTitleVariants"
+ "_originWaypoint"
+ "_playbackAction"
+ "_playbackConfiguration"
+ "_playbackState"
+ "_preferredPresentation"
+ "_progress"
+ "_pushVoiceControlTemplate:presentationStyle:animated:completion:"
+ "_routeSegments"
+ "_routeSegmentsAvailableForRegion"
+ "_setMaximumHeaderGridButtonCount:"
+ "_setMaximumItemCount:"
+ "_setMaximumNumberOfGridImages:"
+ "_setMaximumSectionCount:"
+ "_sportsOverlay"
+ "_startNavigationWithRouteInfo"
+ "_startNavigationWithRouteInfo:"
+ "_supportsRouteSharing"
+ "_supportsVideoPlayback"
+ "_textColor"
+ "_thumbnail"
+ "_thumbnailUpdater"
+ "_timeZone"
+ "_travelEstimates"
+ "_updateLimitedUIStatusForSession:"
+ "_waypoint"
+ "accessibilityLabel"
+ "accessibilityValue"
+ "adaptiveBackgroundStyle"
+ "addRouteSegments:"
+ "alignment"
+ "appendFormat:"
+ "appendString:"
+ "arrayWithCapacity:"
+ "aspectRatio"
+ "backgroundColor"
+ "bodyVariants"
+ "bs_firstObjectPassingTest:"
+ "city"
+ "clientDestinationRequestReceivedFromVehicle:"
+ "clientDestinationSharedFailedForTrip:error:"
+ "clientDestinationSharedSuccessfullyForTrip:"
+ "clientDestinationWillBeSharedForTrip:"
+ "clientRouteSourceUpdateReceivedFromVehicle:"
+ "clientWaypoint:accepted:"
+ "clientWaypointReceivedFromVehicle:"
+ "com.apple.developer.carplay-voice-based-conversation"
+ "componentsSeparatedByString:"
+ "componentsWithURL:resolvingAgainstBaseURL:"
+ "computedHashAtInitialization"
+ "connectedAccessories"
+ "containsValueForKey:"
+ "convertImage:aspectRatio:"
+ "coordinates"
+ "coordinatesCount"
+ "copyForLoading"
+ "correctedAspectRatioForImage:"
+ "country"
+ "cp_displayWithID:"
+ "currentCarPlayAccessory"
+ "currentLeg"
+ "currentLegIdentifier"
+ "currentLocale"
+ "currentNavigationSession"
+ "currentRouteGuidance"
+ "currentSegment"
+ "d24@0:8@16"
+ "decodeInt64ForKey:"
+ "decodeIntForKey:"
+ "destinationWaypoint"
+ "didSet currentLegIndex=%s oldValue=%s"
+ "displayID"
+ "displayId"
+ "displayIdentity"
+ "displays"
+ "elapsedTime"
+ "getRouteLineForCurrentSegments"
+ "getVehicleInfoData"
+ "handleSharedDestination:completion:"
+ "handleWaypointFromVehicle: mapDelegate is nil, cannot handle waypoint insertion"
+ "hasShareableDestination"
+ "hostShowAddStopCardForWaypoint:withTravelEstimates:"
+ "imageOverlay"
+ "initWithCenterPoint:locationThreshold:name:address:entryPoints:entryPointsCount:timeZone:"
+ "initWithImage:alignment:"
+ "initWithImage:imageOverlay:sportsOverlay:"
+ "initWithImage:imageOverlay:sportsOverlay:playbackProgress:"
+ "initWithLeftTeam:rightTeam:eventStatus:"
+ "initWithOrigin:destination:maneuvers:laneGuidances:currentManeuvers:currentLaneGuidance:tripTravelEstimates:maneuverTravelEstimates:coordinates:coordinatesCount:"
+ "initWithOriginWaypoint:destinationWaypoint:routeChoices:"
+ "initWithPreferredPresentation:playbackAction:elapsedTime:duration:"
+ "initWithPreferredPresentation:playbackState:elapsedTime:duration:"
+ "initWithPreferredPresentation:playbackState:progress:"
+ "initWithPreferredPresentation:playbackState:progress:duration:"
+ "initWithPreferredPresentation:playing:progress:"
+ "initWithRouteGuidance:maneuvers:laneGuidances:routeLine:currentLeg:"
+ "initWithText:textColor:backgroundColor:alignment:"
+ "initWithThumbnail:title:subtitle:actionButtons:"
+ "initWithThumbnail:title:subtitle:bodyVariants:actionButtons:"
+ "initWithThumbnail:title:subtitle:metadataTitleVariants:actionButtons:"
+ "initWithThumbnail:title:subtitle:tintColor:"
+ "initWithTitle:listHeader:sections:assistantCellConfiguration:"
+ "initWithURL:"
+ "initWithWaypoint:travelEstimates:"
+ "kCPImageOverlayAlignmentKey"
+ "kCPImageOverlayBackgroundColorKey"
+ "kCPImageOverlayImageKey"
+ "kCPImageOverlayTextColorKey"
+ "kCPImageOverlayTextKey"
+ "kCPListImageRowItemCardElementThumbnailKey"
+ "kCPListImageRowItemElementAccessibilityLabelKey"
+ "kCPListImageRowItemElementPlaybackConfigurationKey"
+ "kCPListItemPlaybackConfigurationKey"
+ "kCPListTemplateDetailsHeaderActionButtonsKey"
+ "kCPListTemplateDetailsHeaderAdaptiveBackgroundStyleKey"
+ "kCPListTemplateDetailsHeaderBodyVariantsKey"
+ "kCPListTemplateDetailsHeaderKey"
+ "kCPListTemplateDetailsHeaderMetadataTitleVariantsKey"
+ "kCPListTemplateDetailsHeaderPlaybackConfigurationKey"
+ "kCPListTemplateDetailsHeaderSubtitleKey"
+ "kCPListTemplateDetailsHeaderThumbnailKey"
+ "kCPListTemplateDetailsHeaderTitleKey"
+ "kCPNavigationWaypointTimeZoneKey"
+ "kCPPlaybackConfigurationDurationKey"
+ "kCPPlaybackConfigurationPlaybackActionKey"
+ "kCPPlaybackConfigurationPlaybackStateKey"
+ "kCPPlaybackConfigurationPlayingKey"
+ "kCPPlaybackConfigurationPreferredPresentationKey"
+ "kCPPlaybackConfigurationProgressKey"
+ "kCPRouteInfoCurrentLegKey"
+ "kCPRouteLegDestinationLocationKey"
+ "kCPRouteLegOriginLocationKey"
+ "kCPRouteLegUUIDKey"
+ "kCPRouteLineDestinationLocationKey"
+ "kCPRouteLineOriginLocationKey"
+ "kCPSportsOverlayEventStatusLabelKey"
+ "kCPSportsOverlayLeftTeamKey"
+ "kCPSportsOverlayRightTeamKey"
+ "kCPThumbnailAspectRatioKey"
+ "kCPThumbnailIdentifierKey"
+ "kCPThumbnailImageOverlayKey"
+ "kCPThumbnailImageSetKey"
+ "kCPThumbnailPlaybackProgressKey"
+ "kCPThumbnailSportsOverlayKey"
+ "kCPTripHasShareableDestinationKey"
+ "kCPVoiceControlActionButtonsKey"
+ "legIdentifiers"
+ "listHeader"
+ "ll"
+ "localTimeZone"
+ "mapTemplate:didFailToShareDestinationForTrip:error:"
+ "mapTemplate:didReceiveRequestForDestination:"
+ "mapTemplate:didReceiveUpdatedRouteSource:"
+ "mapTemplate:didRequestToInsertWaypoint:intoSegment:completion:"
+ "mapTemplate:didShareDestinationForTrip:"
+ "mapTemplate:mapTemplateWaypoint:accepted:forSegment:"
+ "mapTemplate:willShareDestinationForTrip:"
+ "mapTemplateShouldProvideRouteSharing:"
+ "maps"
+ "maximumActionButtonCount"
+ "maximumActionButtonSize"
+ "maximumImageSizeForAspectRatio:"
+ "maximumNumberOfActionButtons"
+ "maximumNumberOfGridImages"
+ "metadataTitleVariants"
+ "originWaypoint"
+ "playbackAction"
+ "playbackConfiguration"
+ "playbackState"
+ "pointOfInterestHandoffEnabled"
+ "postalCode"
+ "preferredImageRowMaximumNumberOfGridImagesWithReply:"
+ "preferredListMaximumHeaderGridButtonCountWithReply:"
+ "preferredListMaximumItemCountWithReply:"
+ "preferredListMaximumSectionCountWithReply:"
+ "preferredPresentation"
+ "progress"
+ "pushVoiceControlTemplate:withProxyDelegate:animated:presentationStyle:reply:"
+ "queryItems"
+ "reloadThumbnail:"
+ "reloadThumbnail:inListImageRowWithIdentifier:"
+ "resolvedIsPlaying"
+ "resolvedPlaybackProgress"
+ "resumeTripWithUpdatedRouteSegments:currentSegment:rerouteReason:"
+ "routeSegments"
+ "routeSegmentsAvailableForRegion"
+ "routeSharingService:didUpdateCurrentLegIndex:"
+ "scheduledTimerWithTimeInterval:repeats:block:"
+ "scheme"
+ "sendCurrentLegIndex"
+ "sendCurrentLegIndex()"
+ "sendDestinationInformation:identifier:"
+ "setAccessibilityLabel:"
+ "setAdaptiveBackgroundStyle:"
+ "setAlignment:"
+ "setBackgroundColor:"
+ "setBodyVariants:"
+ "setComputedHashAtInitialization:"
+ "setCurrentLeg:"
+ "setCurrentLegIdentifier:"
+ "setCurrentLegIndex:"
+ "setCurrentLegIndexInvalid"
+ "setCurrentNavigationSession:"
+ "setCurrentSegment:"
+ "setDisplayGamut:"
+ "setDisplayScale:"
+ "setEventStatus:"
+ "setHasShareableDestination:"
+ "setImageOverlay:"
+ "setLeftTeam:"
+ "setListHeader:"
+ "setMetadataTitleVariants:"
+ "setPlaybackConfiguration:"
+ "setRightTeam:"
+ "setRouteSegments:"
+ "setRouteSegmentsAvailableForRegion:"
+ "setSportsOverlay:"
+ "setTextColor:"
+ "setThumbnail:"
+ "setThumbnailUpdater:"
+ "setTravelEstimates:"
+ "setUserInterfaceIdiom:"
+ "setUserInterfaceStyle:"
+ "setWaypoint:"
+ "sharedInstance"
+ "sportsOverlay"
+ "startNavigation: ignoring routeInfo.routeGuidance guidanceState=%@"
+ "startNavigation: set route guidance with original route guidance guidanceState=%@"
+ "startNavigationForCurrentRouteInfo"
+ "startNavigationWithRouteInfo: supportsAccNav=%@ supportsRouteSharing=%@"
+ "state"
+ "street"
+ "stringByRemovingPercentEncoding"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "supportsCarPlay"
+ "supportsVideoPlayback"
+ "textColor"
+ "thumbnail"
+ "thumbnailUpdater"
+ "traitCollectionByModifyingTraits:"
+ "traitCollectionWithTraits:"
+ "travelEstimates"
+ "unsignedIntValue"
+ "updateDetailsHeader:"
+ "updateHeader"
+ "updateThumbnail"
+ "v16@?0@\"<UIMutableTraits>\"8"
+ "v16@?0@\"CPTravelEstimates\"8"
+ "v16@?0@\"NSTimer\"8"
+ "v24@0:8@\"CPListTemplateDetailsHeader\"16"
+ "v24@0:8@\"CPNavigationWaypoint\"16"
+ "v24@0:8@\"CPPlaybackConfiguration\"16"
+ "v24@0:8@\"CPRouteInfo\"16"
+ "v24@0:8@\"CPRouteLine\"16"
+ "v24@0:8@\"CPThumbnailImage\"16"
+ "v24@0:8@\"CPTrip\"16"
+ "v24@0:8@?<v@?@\"NSNumber\">16"
+ "v28@0:8@\"CAFRouteSharing\"16I24"
+ "v28@0:8@\"CPNavigationWaypoint\"16B24"
+ "v28@0:8@16I24"
+ "v32@0:8@\"CPNavigationWaypoint\"16@\"CPTravelEstimates\"24"
+ "v32@0:8@\"CPThumbnailImage\"16@\"NSUUID\"24"
+ "v32@0:8@\"CPTrip\"16@\"NSError\"24"
+ "v32@0:8q16@\"CPRouteInfo\"24"
+ "v40@0:8@16@24q32"
+ "v56@0:8@\"CPVoiceControlTemplate\"16@\"<CPVoiceControlTemplateDelegate>\"24@\"NSNumber\"32Q40@?<v@?@\"<CPVoiceTemplateProviding>\">48"
+ "value"
+ "vehicleForCurrentSession"
+ "vehicleNavigationSystemName"
+ "vehicleSupportsDestinationSharing"
+ "videoPlaybackSupported"
+ "wantsAdaptiveBackgroundStyle"
+ "waypoint"
+ "{?=\"value\"q\"timescale\"i\"flags\"I\"epoch\"q}"
+ "{?=qiIq}16@0:8"
+ "{CGSize=dd}24@0:8d16"
+ "\xc1"
- "@44@0:8@16I24^{?=ddd}28Q36"
- "@44@0:8C16@20@28@36"
- "CADisplay"
- "CPListTemplate setting maxImageSize (%{public}f,%{public}f)"
- "Forced"
- "G"
- "TC,R,N,V_geodeticSystem"
- "TI,R,N,V_locationThreshold"
- "WaypointAdded"
- "WaypointRemoved"
- "_startNavigationWithRouteInfo:originalState:"
- "_startNavigationWithRouteInfo:originalState: %{public}@"
- "_updateLimitedUIStatus"
- "_vehicleForCurrentSession"
- "displayConfiguration"
- "encodeInt32:forKey:"
- "initWithPlacemark:"
- "placemarkWithLocation:name:postalAddress:"
- "startNavigation: set route guidance with original route guidance"
- "startNavigationWithRouteInfo"
- "traitCollectionWithDisplayGamut:"
- "traitCollectionWithDisplayScale:"
- "traitCollectionWithTraitsFromCollections:"
- "unexpected state in startNavigation: %{public}@"
- "v28@0:8C16@\"CPRouteInfo\"20"
- "v28@0:8C16@20"

```
