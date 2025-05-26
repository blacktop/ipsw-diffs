## MediaControls

> `/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls`

```diff

-4023.110.7.0.0
-  __TEXT.__text: 0xd1ab0
-  __TEXT.__auth_stubs: 0x1210
-  __TEXT.__objc_methlist: 0x10340
-  __TEXT.__const: 0xca0
-  __TEXT.__cstring: 0x435f
+4023.210.1.0.0
+  __TEXT.__text: 0xd1d2c
+  __TEXT.__auth_stubs: 0x1220
+  __TEXT.__objc_methlist: 0x103c0
+  __TEXT.__cstring: 0x43aa
   __TEXT.__ustring: 0x30
-  __TEXT.__gcc_except_tab: 0x1270
-  __TEXT.__oslogstring: 0x54fd
+  __TEXT.__const: 0xcb0
+  __TEXT.__gcc_except_tab: 0x11f4
+  __TEXT.__oslogstring: 0x56ab
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__unwind_info: 0x3620
-  __TEXT.__objc_classname: 0x247e
-  __TEXT.__objc_methname: 0x2b7c3
-  __TEXT.__objc_methtype: 0x79ea
-  __TEXT.__objc_stubs: 0x1a300
-  __DATA_CONST.__got: 0x528
-  __DATA_CONST.__const: 0x2d70
-  __DATA_CONST.__objc_classlist: 0x640
+  __TEXT.__unwind_info: 0x35fc
+  __TEXT.__objc_classname: 0x2448
+  __TEXT.__objc_methname: 0x2bbcd
+  __TEXT.__objc_methtype: 0x7a33
+  __TEXT.__objc_stubs: 0x1a1c0
+  __DATA_CONST.__got: 0x530
+  __DATA_CONST.__const: 0x2ca8
+  __DATA_CONST.__objc_classlist: 0x630
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x370
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x37620
-  __DATA_CONST.__objc_selrefs: 0x89c0
+  __DATA_CONST.__objc_const: 0x37578
+  __DATA_CONST.__objc_selrefs: 0x8a18
   __DATA_CONST.__objc_arraydata: 0x168
-  __AUTH_CONST.__cfstring: 0x48c0
-  __AUTH_CONST.__const: 0xb60
-  __AUTH_CONST.__objc_const: 0x44a0
+  __AUTH_CONST.__cfstring: 0x48a0
+  __AUTH_CONST.__const: 0xb40
+  __AUTH_CONST.__objc_const: 0x4410
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_dictobj: 0x140
-  __AUTH_CONST.__auth_got: 0x918
-  __AUTH.__objc_data: 0x1388
+  __AUTH_CONST.__auth_got: 0x920
+  __AUTH.__objc_data: 0x1338
   __AUTH.__data: 0x8
-  __DATA.__objc_classrefs: 0xca8
-  __DATA.__objc_superrefs: 0x5b0
-  __DATA.__objc_ivar: 0x16c8
+  __DATA.__objc_classrefs: 0xca0
+  __DATA.__objc_superrefs: 0x5a0
+  __DATA.__objc_ivar: 0x16e4
   __DATA.__data: 0x2968
-  __DATA.__bss: 0x80
-  __DATA_DIRTY.__objc_data: 0x2af8
+  __DATA.__bss: 0x88
+  __DATA_DIRTY.__objc_data: 0x2aa8
   __DATA_DIRTY.__data: 0x38
   __DATA_DIRTY.__bss: 0x200
-  __DATA_DIRTY.__common: 0x8
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6127
-  Symbols:   21410
-  CStrings:  9098
+  Functions: 6133
+  Symbols:   21417
+  CStrings:  9135
 
Symbols:
+ +[MRUImageUtilities imageIsEfficientFormat:]
+ +[UIView(MRUAnimations) mru_animateWithSpringParameters:options:animations:]
+ +[UIView(MRUAnimations) mru_animateWithSpringParameters:options:animations:completion:]
+ -[MPAVRoute(MediaControls) isWiredDevice]
+ -[MRUAmbientNowPlayingView labelViewLayoutGuideHeightConstraint]
+ -[MRUAmbientNowPlayingView labelViewLayoutGuide]
+ -[MRUAmbientNowPlayingView setLabelViewLayoutGuide:]
+ -[MRUAmbientNowPlayingView setLabelViewLayoutGuideHeightConstraint:]
+ -[MRUAmbientNowPlayingView setTransportControlsLayoutGuideBottomConstraint:]
+ -[MRUAmbientNowPlayingView setTransportControlsLayoutGuideTopConstraint:]
+ -[MRUAmbientNowPlayingView transportControlsLayoutGuideBottomConstraint]
+ -[MRUAmbientNowPlayingView transportControlsLayoutGuideTopConstraint]
+ -[MRUAmbientNowPlayingView visualStylingProviderDidChange:]
+ -[MRUAmbientNowPlayingVolumeControlsView _packageStateForVolume:]
+ -[MRUAmbientNowPlayingVolumeControlsView ignoreAnimationForVolumeEvents]
+ -[MRUAmbientNowPlayingVolumeControlsView setIgnoreAnimationForVolumeEvents:]
+ -[MRUAssetManager imageForEndpointRoute:photoRealisticAssetTimeout:completion:]
+ -[MRUAssetManager shouldLoadPhotorealisticAssetForRoute:]
+ -[MRUAssetManager symbolImageForEndpointRoute:]
+ -[MRUFlippingArtworkLayer makeAnimation:fromValue:toValue:duration:]
+ -[MRUFlippingArtworkLayer makeSpringAnimation:fromValue:toValue:]
+ -[MRUFlippingArtworkLayer updatePlaceholderFrame]
+ -[MRUFlippingArtworkView shadowViewInsets]
+ -[MRUHoldTransportButton dragEnter:]
+ -[MRUNowPlayingLabelView estimatedHeight]
+ -[MRUNowPlayingLabelView intrinsicHeightForTextInLabel:]
+ -[MRUNowPlayingLabelView isLabelOversized:]
+ -[MRUNowPlayingLabelView marqueeContentGap]
+ -[MRUNowPlayingLabelView placeholderFont]
+ -[MRUNowPlayingLabelView routeFont]
+ -[MRUNowPlayingLabelView setMarqueeContentGap:]
+ -[MRUNowPlayingLabelView setPlaceholderFont:]
+ -[MRUNowPlayingLabelView setRouteFont:]
+ -[MRUNowPlayingLabelView setSubtitleFont:]
+ -[MRUNowPlayingLabelView setTitleFont:]
+ -[MRUNowPlayingLabelView subtitleFont]
+ -[MRUNowPlayingLabelView titleFont]
+ -[MRUNowPlayingLabelView updateFonts]
+ -[MRUNowPlayingTimeControlsView viewForLastBaselineLayout]
+ -[MRURouteRecommendationPlatterView updateVisualStyling]
+ -[MRURouteRecommendationPlatterView visualStylingProviderDidChange:]
+ -[MRURouteRecommendationPlatterViewController routeTextFormatter]
+ -[MRURouteRecommendationPlatterViewController setRouteTextFormatter:]
+ -[MediaControlsExpandableButton resetMessageAnimated:]
+ -[MediaControlsExpandableButton resetMessage]
+ GCC_except_table19
+ _MRUAmbientNowPlayingLabelViewHorizontalInset
+ _MRUAmbientNowPlayingMarqueeContentGap
+ _MRUAmbientNowPlayingTimeControlsBottomInset
+ _MRUFlippingArtworkInsets
+ _MRUFlippingArtworkScale
+ _MRUFlippingArtworkSpringParameters
+ _MRUNowPlayingHeaderCenterYOffset
+ _MRUNowPlayingOversizedFontScale
+ _MRUNowPlayingTimeControlsStretchLimit
+ _MRUVolumeIdentifierPrimaryMultiCategoryVolumeSlider
+ _OBJC_CLASS_$_MRAVOutputDeviceSymbolProvider
+ _OBJC_CLASS_$_MRBlockGuard
+ _OBJC_IVAR_$_MRUAmbientNowPlayingView._labelViewLayoutGuide
+ _OBJC_IVAR_$_MRUAmbientNowPlayingView._labelViewLayoutGuideHeightConstraint
+ _OBJC_IVAR_$_MRUAmbientNowPlayingView._transportControlsLayoutGuideBottomConstraint
+ _OBJC_IVAR_$_MRUAmbientNowPlayingView._transportControlsLayoutGuideTopConstraint
+ _OBJC_IVAR_$_MRUAmbientNowPlayingVolumeControlsView._ignoreAnimationForVolumeEvents
+ _OBJC_IVAR_$_MRUFlippingArtworkView._playing
+ _OBJC_IVAR_$_MRUNowPlayingLabelView._marqueeContentGap
+ _OBJC_IVAR_$_MRUNowPlayingLabelView._placeholderFont
+ _OBJC_IVAR_$_MRUNowPlayingLabelView._routeFont
+ _OBJC_IVAR_$_MRUNowPlayingLabelView._subtitleFont
+ _OBJC_IVAR_$_MRUNowPlayingLabelView._titleFont
+ _OBJC_IVAR_$_MRURouteRecommendationPlatterViewController._routeTextFormatter
+ _UIEdgeInsetsAdd
+ _UIRectRoundToScale
+ __MPAVLog._log
+ __OBJC_CLASS_PROTOCOLS_$_MRURouteRecommendationPlatterView
+ ___102-[MRURouteRecommendationPlatterViewController nowPlayingController:endpointController:didChangeRoute:]_block_invoke
+ ___37-[MRUFlippingArtworkView setPlaying:]_block_invoke
+ ___41-[MPAVRoute(MediaControls) isWiredDevice]_block_invoke
+ ___45-[MRUTransportControls leftItemFromResponse:]_block_invoke.38
+ ___45-[MRUTransportControls leftItemFromResponse:]_block_invoke.40
+ ___45-[MRUTransportControls leftItemFromResponse:]_block_invoke_2.39
+ ___45-[MRUTransportControls leftItemFromResponse:]_block_invoke_2.41
+ ___45-[MediaControlsExpandableButton setExpanded:]_block_invoke_2
+ ___54-[MediaControlsExpandableButton resetMessageAnimated:]_block_invoke
+ ___55-[MRURouteRecommender initializeSessionWhenAppropriate]_block_invoke.124
+ ___58-[MRUAmbientNowPlayingViewController updateVolumeControls]_block_invoke
+ ___79-[MRUAssetManager imageForEndpointRoute:photoRealisticAssetTimeout:completion:]_block_invoke
+ ___79-[MRUAssetManager imageForEndpointRoute:photoRealisticAssetTimeout:completion:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e40_"MPVolumeControllerRouteDataSource"8?0ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e29_v24?0"UIImage"8"NSError"16ls32l8s48l8s40l8
+ ___block_literal_global.119
+ ___block_literal_global.145
+ ___block_literal_global.261
+ _objc_msgSend$_packageStateForVolume:
+ _objc_msgSend$beganHold:
+ _objc_msgSend$disarm
+ _objc_msgSend$estimatedHeight
+ _objc_msgSend$imageForEndpointRoute:photoRealisticAssetTimeout:completion:
+ _objc_msgSend$imageIsEfficientFormat:
+ _objc_msgSend$initWithTimeout:reason:queue:handler:
+ _objc_msgSend$intrinsicHeightForTextInLabel:
+ _objc_msgSend$isLabelOversized:
+ _objc_msgSend$isWiredDevice
+ _objc_msgSend$makeAnimation:fromValue:toValue:duration:
+ _objc_msgSend$makeSpringAnimation:fromValue:toValue:
+ _objc_msgSend$mru_animateWithSpringParameters:options:animations:
+ _objc_msgSend$mru_animateWithSpringParameters:options:animations:completion:
+ _objc_msgSend$resetMessageAnimated:
+ _objc_msgSend$setInoperative:
+ _objc_msgSend$setMarqueeContentGap:
+ _objc_msgSend$shadowViewInsets
+ _objc_msgSend$shouldLoadPhotorealisticAssetForRoute:
+ _objc_msgSend$symbolImageForEndpointRoute:
+ _objc_msgSend$symbolNameForOutputDevices:
+ _objc_msgSend$updateFonts
+ _objc_msgSend$updatePlaceholderFrame
- -[MRUAmbientNowPlayingVolumeControlsView gestureRecognizerShouldBegin:]
- -[MRUAssetManager imageForEndpointRoute:completion:]
- -[MRUFlippingArtworkView placeholderImageView]
- -[MRUFlippingArtworkView setPlaceholderImageView:]
- -[MRUMirroringMenuModuleItem .cxx_destruct]
- -[MRUMirroringMenuModuleItem hash]
- -[MRUMirroringMenuModuleItem isEqual:]
- -[MRUMirroringMenuModuleItem setSymbolName:]
- -[MRUMirroringMenuModuleItem symbolName]
- -[MRUMirroringViewController .cxx_destruct]
- -[MRUMirroringViewController _canShowWhileLocked]
- -[MRUMirroringViewController controller]
- -[MRUMirroringViewController displayMonitor]
- -[MRUMirroringViewController isConnectedToExternalDisplay]
- -[MRUMirroringViewController leadingImageForMenuItem:]
- -[MRUMirroringViewController mirroringController:didChangeAvailableOutputDevices:]
- -[MRUMirroringViewController mirroringController:didChangeOutputDevice:]
- -[MRUMirroringViewController mirroringController:didUpdateBusyIdenifiers:]
- -[MRUMirroringViewController selectOutputDevice:]
- -[MRUMirroringViewController setController:]
- -[MRUMirroringViewController setDisplayMonitor:]
- -[MRUMirroringViewController setShowMoreExpanded:]
- -[MRUMirroringViewController shouldBeginTransitionToExpandedContentModule]
- -[MRUMirroringViewController shouldExpandModuleOnTouch:]
- -[MRUMirroringViewController showMoreExpanded]
- -[MRUMirroringViewController stopMirroringDismissOnComplete:]
- -[MRUMirroringViewController updateFooter]
- -[MRUMirroringViewController updateItems]
- -[MRUMirroringViewController updateState]
- -[MRUMirroringViewController viewDidLoad]
- -[MRUMirroringViewController viewWillAppear:]
- -[MRUMirroringViewController viewWillDisappear:]
- -[MRUMirroringViewController willTransitionToExpandedContentMode:]
- GCC_except_table27
- _CGAffineTransformConcat
- _MRUMirroringGlyphStateOff
- _MRUMirroringGlyphStateOn
- _MRUMirroringMinimumItems
- _MRUMirroringVisibleItems
- _MediaControlsVersionNumber
- _MediaControlsVersionString
- _OBJC_CLASS_$_CCUIMenuModuleItem
- _OBJC_CLASS_$_CCUIMenuModuleViewController
- _OBJC_CLASS_$_FBSDisplayMonitor
- _OBJC_CLASS_$_MRUMirroringMenuModuleItem
- _OBJC_CLASS_$_MRUMirroringViewController
- _OBJC_IVAR_$_MRUFlippingArtworkView._placeholderImageView
- _OBJC_IVAR_$_MRUMirroringMenuModuleItem._symbolName
- _OBJC_IVAR_$_MRUMirroringViewController._controller
- _OBJC_IVAR_$_MRUMirroringViewController._displayMonitor
- _OBJC_IVAR_$_MRUMirroringViewController._showMoreExpanded
- _OBJC_METACLASS_$_CCUIMenuModuleItem
- _OBJC_METACLASS_$_CCUIMenuModuleViewController
- _OBJC_METACLASS_$_MRUMirroringMenuModuleItem
- _OBJC_METACLASS_$_MRUMirroringViewController
- __OBJC_$_INSTANCE_METHODS_MRUMirroringMenuModuleItem
- __OBJC_$_INSTANCE_METHODS_MRUMirroringViewController
- __OBJC_$_INSTANCE_VARIABLES_MRUMirroringMenuModuleItem
- __OBJC_$_INSTANCE_VARIABLES_MRUMirroringViewController
- __OBJC_$_PROP_LIST_MRUMirroringMenuModuleItem
- __OBJC_$_PROP_LIST_MRUMirroringViewController
- __OBJC_CLASS_PROTOCOLS_$_MRUMirroringViewController
- __OBJC_CLASS_RO_$_MRUMirroringMenuModuleItem
- __OBJC_CLASS_RO_$_MRUMirroringViewController
- __OBJC_METACLASS_RO_$_MRUMirroringMenuModuleItem
- __OBJC_METACLASS_RO_$_MRUMirroringViewController
- ___41-[MRUMirroringViewController updateItems]_block_invoke
- ___41-[MRUMirroringViewController updateItems]_block_invoke_2
- ___41-[MRUMirroringViewController updateItems]_block_invoke_3
- ___41-[MRUMirroringViewController updateItems]_block_invoke_4
- ___42-[MRUMirroringViewController updateFooter]_block_invoke
- ___45-[MRUTransportControls leftItemFromResponse:]_block_invoke.47
- ___45-[MRUTransportControls leftItemFromResponse:]_block_invoke.49
- ___45-[MRUTransportControls leftItemFromResponse:]_block_invoke_2.48
- ___45-[MRUTransportControls leftItemFromResponse:]_block_invoke_2.50
- ___45-[MediaControlsExpandableButton showMessage:]_block_invoke_2
- ___45-[MediaControlsExpandableButton showMessage:]_block_invoke_3
- ___49-[MRUMirroringViewController selectOutputDevice:]_block_invoke
- ___52-[MRUAssetManager imageForEndpointRoute:completion:]_block_invoke
- ___55-[MRURouteRecommender initializeSessionWhenAppropriate]_block_invoke.127
- ___61-[MRUMirroringViewController stopMirroringDismissOnComplete:]_block_invoke
- ___66-[MRUMirroringViewController willTransitionToExpandedContentMode:]_block_invoke
- ___74-[MRUMirroringViewController mirroringController:didUpdateBusyIdenifiers:]_block_invoke
- ___block_descriptor_32_e23_v16?0"UIAlertAction"8l
- ___block_descriptor_32_e24_B16?0"AVOutputDevice"8l
- ___block_descriptor_40_e8_32s_e5_B8?0ls32l8
- ___block_descriptor_40_e8_32w_e5_B8?0lw32l8
- ___block_descriptor_41_e8_32w_e8_v16?0q8lw32l8
- ___block_descriptor_48_e8_32s40bs_e29_v24?0"UIImage"8"NSError"16ls40l8s32l8
- ___block_descriptor_50_e8_32s40w_e5_B8?0lw40l8s32l8
- ___block_literal_global.122
- ___block_literal_global.148
- ___block_literal_global.264
- ___block_literal_global.32
- __log
- _contentLayerScale
- _makeAnimation
- _makeSpringAnimation
- _objc_msgSend$airPlayProperties
- _objc_msgSend$airplayErrorExternalDisplay
- _objc_msgSend$buttonView
- _objc_msgSend$connectedIdentities
- _objc_msgSend$connectionType
- _objc_msgSend$contentModuleContext
- _objc_msgSend$designatedGroupLeaderRouteUID
- _objc_msgSend$dismissModule
- _objc_msgSend$hash
- _objc_msgSend$imageForEndpointRoute:
- _objc_msgSend$initWithTitle:identifier:handler:
- _objc_msgSend$isConnectedToExternalDisplay
- _objc_msgSend$isStereoPair
- _objc_msgSend$playing
- _objc_msgSend$removeFooterButton
- _objc_msgSend$selectOutputDevice:
- _objc_msgSend$setBehaviorIdentifier:
- _objc_msgSend$setBusy:
- _objc_msgSend$setDecrementImage:
- _objc_msgSend$setFooterButtonTitle:handler:
- _objc_msgSend$setIncrementImage:
- _objc_msgSend$setIndentation:
- _objc_msgSend$setMenuItems:
- _objc_msgSend$setMinimumMenuItems:
- _objc_msgSend$setShowMoreExpanded:
- _objc_msgSend$setSymbolName:
- _objc_msgSend$setUseTrailingCheckmarkLayout:
- _objc_msgSend$setVisibleMenuItems:
- _objc_msgSend$showMoreExpanded
- _objc_msgSend$startMirroringToOutputDevice:completion:
- _objc_msgSend$stopMirroringDismissOnComplete:
- _objc_msgSend$updateFooter
- _objc_msgSend$updateItems
- _packageState
- _sliderTransform
CStrings:
+ "\x03\x11\x1f\x06"
+ "\x12\x16\x11"
+ "\x15:"
+ "\x17\x13\x13\x11"
+ "%{public}@ change audio destination to %{public}@"
+ "%{public}@ start detailed discovery"
+ "%{public}@ start mirroring to device %{public}@"
+ "%{public}@ stop detailed discovery"
+ "%{public}@ stop mirroring to device %{public}@"
+ "%{public}@ update audio output devices: %{public}@"
+ "%{public}@ update output devices: %{public}@"
+ "%{public}@ update selected audio output device: %{public}@ | previous: %{public}@"
+ "%{public}@ update selected output device: %{public}@ | previous: %{public}@"
+ "@\"MPVolumeControllerRouteDataSource\"8@?0"
+ "@48@0:8@16@24@32d40"
+ "MPCMRContentItemArtworkDataToken"
+ "MRUVolumeIdentifierPrimaryMultiCategoryVolumeSlider"
+ "T@\"MRURouteRecommendationPlatterView\",&,D,N"
+ "T@\"NSLayoutConstraint\",&,N,V_labelViewLayoutGuideHeightConstraint"
+ "T@\"NSLayoutConstraint\",&,N,V_transportControlsLayoutGuideBottomConstraint"
+ "T@\"NSLayoutConstraint\",&,N,V_transportControlsLayoutGuideTopConstraint"
+ "T@\"UIFont\",&,N,V_placeholderFont"
+ "T@\"UIFont\",&,N,V_routeFont"
+ "T@\"UIFont\",&,N,V_subtitleFont"
+ "T@\"UIFont\",&,N,V_titleFont"
+ "T@\"UILayoutGuide\",&,N,V_labelViewLayoutGuide"
+ "Td,N,V_marqueeContentGap"
+ "_labelViewLayoutGuide"
+ "_labelViewLayoutGuideHeightConstraint"
+ "_marqueeContentGap"
+ "_packageStateForVolume:"
+ "_placeholderFont"
+ "_routeFont"
+ "_subtitleFont"
+ "_titleFont"
+ "_transportControlsLayoutGuideBottomConstraint"
+ "_transportControlsLayoutGuideTopConstraint"
+ "disarm"
+ "dragEnter:"
+ "estimatedHeight"
+ "imageForEndpointRoute:photoRealisticAssetTimeout:completion:"
+ "imageIsEfficientFormat:"
+ "initWithTimeout:reason:queue:handler:"
+ "intrinsicHeightForTextInLabel:"
+ "isLabelOversized:"
+ "isWiredDevice"
+ "labelViewLayoutGuide"
+ "labelViewLayoutGuideHeightConstraint"
+ "makeAnimation:fromValue:toValue:duration:"
+ "makeSpringAnimation:fromValue:toValue:"
+ "marqueeContentGap"
+ "mru_animateWithSpringParameters:options:animations:"
+ "mru_animateWithSpringParameters:options:animations:completion:"
+ "photorealistic asset loading"
+ "placeholderFont"
+ "public.heic"
+ "public.heif"
+ "resetMessage"
+ "resetMessageAnimated:"
+ "routeFont"
+ "setInoperative:"
+ "setLabelViewLayoutGuide:"
+ "setLabelViewLayoutGuideHeightConstraint:"
+ "setMarqueeContentGap:"
+ "setPlaceholderFont:"
+ "setRouteFont:"
+ "setSubtitleFont:"
+ "setTitleFont:"
+ "setTransportControlsLayoutGuideBottomConstraint:"
+ "setTransportControlsLayoutGuideTopConstraint:"
+ "shadowViewInsets"
+ "shouldLoadPhotorealisticAssetForRoute:"
+ "subtitleFont"
+ "symbolImageForEndpointRoute:"
+ "symbolNameForOutputDevices:"
+ "titleFont"
+ "transportControlsLayoutGuideBottomConstraint"
+ "transportControlsLayoutGuideTopConstraint"
+ "updateFonts"
+ "updatePlaceholderFrame"
+ "v40@0:8@16d24@?32"
+ "v72@0:8{?=ddddd}16Q56@?64"
+ "v80@0:8{?=ddddd}16Q56@?64@?72"
+ "viewForLastBaselineLayout"
- "\x03\x11\x1f\x02"
- "\x12\x17\x11"
- "\x15&"
- "\x16\x13\x14\x11"
- "%{public}@ displaying items: %{public}@"
- "@\"FBSDisplayMonitor\""
- "IsDiscoveredOverInfra"
- "MPNowPlayingContentItemRemoteArtworkToken"
- "MRUMirroringMenuModuleItem"
- "MRUMirroringViewController"
- "Mirroring"
- "MirroringNonAnimated"
- "T@\"FBSDisplayMonitor\",&,N,V_displayMonitor"
- "T@\"MRUMirroringController\",&,N,V_controller"
- "T@\"NSString\",&,N,V_symbolName"
- "TB,N,GisPlaying"
- "TB,N,V_showMoreExpanded"
- "_showMoreExpanded"
- "airPlayProperties"
- "buttonView"
- "connectedIdentities"
- "connectionType"
- "contentModuleContext"
- "designatedGroupLeaderRouteUID"
- "dismissModule"
- "imageForEndpointRoute:completion:"
- "initWithTitle:identifier:handler:"
- "isConnectedToExternalDisplay"
- "isStereoPair"
- "leadingImageForMenuItem:"
- "removeFooterButton"
- "selectOutputDevice:"
- "setBehaviorIdentifier:"
- "setBusy:"
- "setFooterButtonTitle:handler:"
- "setIndentation:"
- "setMenuItems:"
- "setMinimumMenuItems:"
- "setShowMoreExpanded:"
- "setSymbolName:"
- "setUseTrailingCheckmarkLayout:"
- "setVisibleMenuItems:"
- "showMoreExpanded"
- "showmore"
- "stopMirroringDismissOnComplete:"
- "updateFooter"
- "updateItems"

```
