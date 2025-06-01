## MediaControls

> `/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls`

```diff

-4023.410.2.0.0
-  __TEXT.__text: 0xd1ea4
-  __TEXT.__auth_stubs: 0x1220
-  __TEXT.__objc_methlist: 0x10420
-  __TEXT.__cstring: 0x4485
+4023.510.2.0.0
+  __TEXT.__text: 0xd73a0
+  __TEXT.__auth_stubs: 0x1230
+  __TEXT.__objc_methlist: 0x10af0
+  __TEXT.__cstring: 0x44d9
   __TEXT.__ustring: 0x30
-  __TEXT.__const: 0xcb0
-  __TEXT.__gcc_except_tab: 0x122c
-  __TEXT.__oslogstring: 0x56ab
+  __TEXT.__const: 0xc80
+  __TEXT.__gcc_except_tab: 0x1298
+  __TEXT.__oslogstring: 0x578d
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__unwind_info: 0x3604
-  __TEXT.__objc_classname: 0x2448
-  __TEXT.__objc_methname: 0x2bd3b
-  __TEXT.__objc_methtype: 0x7a33
-  __TEXT.__objc_stubs: 0x1a300
+  __TEXT.__unwind_info: 0x377c
+  __TEXT.__objc_classname: 0x247a
+  __TEXT.__objc_methname: 0x2c259
+  __TEXT.__objc_methtype: 0x7ac4
+  __TEXT.__objc_stubs: 0x1a540
   __DATA_CONST.__got: 0x530
-  __DATA_CONST.__const: 0x2ca8
-  __DATA_CONST.__objc_classlist: 0x630
-  __DATA_CONST.__objc_catlist: 0x90
+  __DATA_CONST.__const: 0x2d20
+  __DATA_CONST.__objc_classlist: 0x640
+  __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x370
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x37648
-  __DATA_CONST.__objc_selrefs: 0x8a68
+  __DATA_CONST.__objc_const: 0x38918
+  __DATA_CONST.__objc_selrefs: 0x8b20
+  __DATA_CONST.__objc_classrefs: 0xcb8
+  __DATA_CONST.__objc_superrefs: 0x5b0
   __DATA_CONST.__objc_arraydata: 0x168
-  __AUTH_CONST.__cfstring: 0x4960
-  __AUTH_CONST.__const: 0xb40
-  __AUTH_CONST.__objc_const: 0x4410
+  __AUTH_CONST.__cfstring: 0x4a00
+  __AUTH_CONST.__const: 0xb80
+  __AUTH_CONST.__objc_const: 0x44e0
   __AUTH_CONST.__objc_intobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_dictobj: 0x140
-  __AUTH_CONST.__auth_got: 0x920
-  __AUTH.__objc_data: 0x1338
+  __AUTH_CONST.__auth_got: 0x928
+  __AUTH.__objc_data: 0x11f8
   __AUTH.__data: 0x8
-  __DATA.__objc_classrefs: 0xca8
-  __DATA.__objc_superrefs: 0x5a0
-  __DATA.__objc_ivar: 0x16e8
+  __DATA.__objc_ivar: 0x1774
   __DATA.__data: 0x2968
-  __DATA.__bss: 0x88
-  __DATA_DIRTY.__objc_data: 0x2aa8
+  __DATA.__bss: 0x79
+  __DATA_DIRTY.__objc_data: 0x2c88
   __DATA_DIRTY.__data: 0x38
-  __DATA_DIRTY.__bss: 0x200
+  __DATA_DIRTY.__bss: 0x218
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 82100143-97C2-3E2E-A8E4-D33E0746713F
-  Functions: 6142
-  Symbols:   21444
-  CStrings:  9742
+  UUID: 9A6FFBB7-4DB3-3DE6-85C4-1C2F9B391796
+  Functions: 6305
+  Symbols:   21881
+  CStrings:  9808
 
Symbols:
+ +[MRUFeatureFlagProvider isMediaSuggestionsDevEnabled]
+ +[MRURecommendation recommendationWithIRCandidateResult:contextIdentifier:]
+ +[MRUStringsProvider accessoryBatteryLevelCase:]
+ +[MRUStringsProvider accessoryBatteryLevelCombinedLeft:right:]
+ +[MRUStringsProvider accessoryBatteryLevelLeft:]
+ +[MRUStringsProvider accessoryBatteryLevelRight:]
+ +[MRUStringsProvider accessoryBatteryLevelSingle:]
+ +[MRUStringsProvider airPlayConnectionErrorMessage:]
+ +[MRUStringsProvider composedBy:]
+ +[MRUStringsProvider localizedStringWithKey:expectedFormat:]
+ +[MRUStringsProvider localizedUppercaseStringWithKey:expectedFormat:]
+ +[MRUStringsProvider routingHijackLocalMessagePresentingApp:busyRouteName:]
+ +[MRUStringsProvider routingHijackLocalTitle:]
+ +[MRUStringsProvider routingInUseOnPairedDevice:]
+ -[MRUControlCenterViewController pendingState]
+ -[MRUControlCenterViewController setPendingState:]
+ -[MRUControlCenterViewController willTransitionToExpandedContentMode:]
+ -[MRULockscreenView .cxx_destruct]
+ -[MRULockscreenView artworkView]
+ -[MRULockscreenView contentEdgeInsets]
+ -[MRULockscreenView headerView]
+ -[MRULockscreenView initWithFrame:]
+ -[MRULockscreenView isDimmed]
+ -[MRULockscreenView isOnScreen]
+ -[MRULockscreenView layoutSubviews]
+ -[MRULockscreenView pointerInteraction:regionForRequest:defaultRegion:]
+ -[MRULockscreenView pointerInteraction:styleForRegion:]
+ -[MRULockscreenView setContentEdgeInsets:]
+ -[MRULockscreenView setDimmed:]
+ -[MRULockscreenView setOnScreen:]
+ -[MRULockscreenView setShowArtworkView:]
+ -[MRULockscreenView setShowSuggestionsView:]
+ -[MRULockscreenView setShowVolumeControlsView:]
+ -[MRULockscreenView setStylingProvider:]
+ -[MRULockscreenView setSuggestionsView:]
+ -[MRULockscreenView showArtworkView]
+ -[MRULockscreenView showSuggestionsView]
+ -[MRULockscreenView showVolumeControlsView]
+ -[MRULockscreenView sizeThatFits:]
+ -[MRULockscreenView stylingProvider]
+ -[MRULockscreenView suggestionsFrame]
+ -[MRULockscreenView suggestionsView]
+ -[MRULockscreenView timeControlsView]
+ -[MRULockscreenView transportControlsView]
+ -[MRULockscreenView updateOnScreen]
+ -[MRULockscreenView updateTextAlignment]
+ -[MRULockscreenView updateVisibility]
+ -[MRULockscreenView volumeControlsView]
+ -[MRULockscreenViewController .cxx_destruct]
+ -[MRULockscreenViewController _canShowWhileLocked]
+ -[MRULockscreenViewController _setStylingProvider:]
+ -[MRULockscreenViewController _stateDumpObject]
+ -[MRULockscreenViewController _timelinesForDateInterval:]
+ -[MRULockscreenViewController _updateWithFrameSpecifier:]
+ -[MRULockscreenViewController artworkView:didChangeArtworkImage:]
+ -[MRULockscreenViewController artworkView]
+ -[MRULockscreenViewController backlightSceneEnvironment]
+ -[MRULockscreenViewController callMonitorDidUpdateOnCall:isOnCall:]
+ -[MRULockscreenViewController createNowPlayingController]
+ -[MRULockscreenViewController createSuggestionsViewController]
+ -[MRULockscreenViewController createWaveformViewController]
+ -[MRULockscreenViewController dealloc]
+ -[MRULockscreenViewController delegate]
+ -[MRULockscreenViewController didSelectArtworkView:]
+ -[MRULockscreenViewController didSelectLabelView:]
+ -[MRULockscreenViewController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:]
+ -[MRULockscreenViewController hardwareVolumeControlAssertion]
+ -[MRULockscreenViewController hasPendingTraitCollectionUpdates]
+ -[MRULockscreenViewController invalidateAllTimelinesForReason:]
+ -[MRULockscreenViewController isDimmed]
+ -[MRULockscreenViewController isOnScreen]
+ -[MRULockscreenViewController isShowingMediaSuggestions]
+ -[MRULockscreenViewController loadView]
+ -[MRULockscreenViewController lockScreenInternalRoutePickerOverrideWithDefaultStyle:]
+ -[MRULockscreenViewController lockScreenPresentsOverrideRoutePicker]
+ -[MRULockscreenViewController mediaControls]
+ -[MRULockscreenViewController mediaSuggestionsViewController:didSelectSuggestion:completion:]
+ -[MRULockscreenViewController nowPlayingController:endpointController:didChangeRoute:]
+ -[MRULockscreenViewController nowPlayingController:mediaSuggestionsController:didChangeMediaSuggestions:]
+ -[MRULockscreenViewController nowPlayingController:metadataController:didChangeArtwork:]
+ -[MRULockscreenViewController nowPlayingController:metadataController:didChangeBundleID:]
+ -[MRULockscreenViewController nowPlayingController:metadataController:didChangeNowPlayingInfo:]
+ -[MRULockscreenViewController nowPlayingController:metadataController:didChangeTimeControls:]
+ -[MRULockscreenViewController nowPlayingController:metadataController:didChangeTransportControls:]
+ -[MRULockscreenViewController nowPlayingController:tvRemoteController:didChangeShowTVRemote:]
+ -[MRULockscreenViewController nowPlayingControllerShouldAutomaticallyUpdateResponse:]
+ -[MRULockscreenViewController nowPlayingController]
+ -[MRULockscreenViewController pendingDimmed]
+ -[MRULockscreenViewController pendingTimelineInvalidation]
+ -[MRULockscreenViewController pendingVisualStylingProvider]
+ -[MRULockscreenViewController restrictedRects]
+ -[MRULockscreenViewController schedulePendingTraitCollectionUpdates]
+ -[MRULockscreenViewController setDelegate:]
+ -[MRULockscreenViewController setDimmed:]
+ -[MRULockscreenViewController setHardwareVolumeControlAssertion:]
+ -[MRULockscreenViewController setHasPendingTraitCollectionUpdates:]
+ -[MRULockscreenViewController setMediaControls:]
+ -[MRULockscreenViewController setOnScreen:]
+ -[MRULockscreenViewController setPendingDimmed:]
+ -[MRULockscreenViewController setPendingTimelineInvalidation:]
+ -[MRULockscreenViewController setPendingVisualStylingProvider:]
+ -[MRULockscreenViewController setShowArtworkView:]
+ -[MRULockscreenViewController setStateHandle:]
+ -[MRULockscreenViewController setStylingProvider:]
+ -[MRULockscreenViewController setSuggestionsViewController:]
+ -[MRULockscreenViewController setWaveformController:]
+ -[MRULockscreenViewController setWaveformViewController:]
+ -[MRULockscreenViewController showArtworkView]
+ -[MRULockscreenViewController stateHandle]
+ -[MRULockscreenViewController stylingProvider]
+ -[MRULockscreenViewController suggestionsViewController]
+ -[MRULockscreenViewController traitCollectionDidChange:]
+ -[MRULockscreenViewController transportControlsView:didSelectRoutingButton:]
+ -[MRULockscreenViewController transportControlsView:didSelectTVRemoteButton:]
+ -[MRULockscreenViewController updateArtwork]
+ -[MRULockscreenViewController updateDimmed]
+ -[MRULockscreenViewController updateEverything]
+ -[MRULockscreenViewController updateLayoutDependantProperties]
+ -[MRULockscreenViewController updateLayoutWithAnimations:completion:]
+ -[MRULockscreenViewController updateNowPlayingInfo]
+ -[MRULockscreenViewController updatePreferredContentSize]
+ -[MRULockscreenViewController updateRestrictedRects]
+ -[MRULockscreenViewController updateRouteLabel]
+ -[MRULockscreenViewController updateRoutingButtonAnimated:]
+ -[MRULockscreenViewController updateRoutingButton]
+ -[MRULockscreenViewController updateSuggestions]
+ -[MRULockscreenViewController updateTimeControlsForPresentationInterval:]
+ -[MRULockscreenViewController updateTimeControls]
+ -[MRULockscreenViewController updateTransportControls]
+ -[MRULockscreenViewController updateVisibility]
+ -[MRULockscreenViewController updateVisualStyling]
+ -[MRULockscreenViewController updateVolumeControls]
+ -[MRULockscreenViewController updateWaveformVisibility]
+ -[MRULockscreenViewController viewDidLayoutSubviews]
+ -[MRULockscreenViewController viewDidLoad]
+ -[MRULockscreenViewController viewWillAppear:]
+ -[MRULockscreenViewController viewWillDisappear:]
+ -[MRULockscreenViewController volumeControlsView:volumeValueDidChange:]
+ -[MRULockscreenViewController waveformController]
+ -[MRULockscreenViewController waveformViewController]
+ -[MRUNowPlayingHeaderView initWithFrame:]
+ -[MRUNowPlayingTimeControlsView regexNumberDecimalDigit]
+ -[MRUNowPlayingTimeControlsView setRegexNumberDecimalDigit:]
+ -[MRUNowPlayingView initWithFrame:]
+ -[MRURecommendation contextIdentifier]
+ -[MRURecommendation setContextIdentifier:]
+ -[MRURouteRecommendationPlatterViewController _timelinesForDateInterval:]
+ -[MRURouteRecommendationPlatterViewController backlightSceneEnvironment]
+ -[MRURouteRecommendationPlatterViewController hasPendingTraitCollectionUpdates]
+ -[MRURouteRecommendationPlatterViewController invalidateAllTimelinesForReason:]
+ -[MRURouteRecommendationPlatterViewController isDimmed]
+ -[MRURouteRecommendationPlatterViewController pendingDimmed]
+ -[MRURouteRecommendationPlatterViewController schedulePendingTraitCollectionUpdates]
+ -[MRURouteRecommendationPlatterViewController setDimmed:]
+ -[MRURouteRecommendationPlatterViewController setHasPendingTraitCollectionUpdates:]
+ -[MRURouteRecommendationPlatterViewController setPendingDimmed:]
+ -[MRURouteRecommendationPlatterViewController traitCollectionDidChange:]
+ -[MRURouteRecommendationPlatterViewController updateDimmed]
+ -[MRURouteRecommendationPlatterViewController updateMarqueeAnimation]
+ -[MRURoutingViewController _wouldEndGroupSessionForViewItem:operation:pickedRoutes:]
+ -[MRUVolumeViewController pendingExpanded]
+ -[MRUVolumeViewController setPendingExpanded:]
+ -[MRUVolumeViewController willTransitionToExpandedContentMode:]
+ -[MRUWaveformSettings nonVariableFramerate]
+ -[MRUWaveformSettings setNonVariableFramerate:]
+ -[MRUWaveformSettings setSupportsVariableFramerate:]
+ -[MRUWaveformSettings supportsVariableFramerate]
+ -[MediaControlsEndpointsManager loadActiveSystemRoute]
+ -[MediaControlsEndpointsManager updateActiveSystemRoute:]
+ -[UIImage(MediaControls) mru_imageFittingSize:]
+ GCC_except_table105
+ GCC_except_table138
+ GCC_except_table175
+ GCC_except_table222
+ GCC_except_table31
+ GCC_except_table91
+ GCC_except_table97
+ _MRGroupSessionRouteTypeForOutputDevices
+ _MRUDeviceSupportsVariableFrameRate
+ _MRUDeviceSupportsVariableFrameRate.__supports
+ _MRUDeviceSupportsVariableFrameRate.onceToken
+ _OBJC_CLASS_$_MRULockscreenView
+ _OBJC_CLASS_$_MRULockscreenViewController
+ _OBJC_CLASS_$_UITraitPreferredContentSizeCategory
+ _OBJC_IVAR_$_MRUControlCenterViewController._pendingState
+ _OBJC_IVAR_$_MRULockscreenView._artworkView
+ _OBJC_IVAR_$_MRULockscreenView._contentEdgeInsets
+ _OBJC_IVAR_$_MRULockscreenView._dimmed
+ _OBJC_IVAR_$_MRULockscreenView._headerView
+ _OBJC_IVAR_$_MRULockscreenView._onScreen
+ _OBJC_IVAR_$_MRULockscreenView._showArtworkView
+ _OBJC_IVAR_$_MRULockscreenView._showSuggestionsView
+ _OBJC_IVAR_$_MRULockscreenView._showVolumeControlsView
+ _OBJC_IVAR_$_MRULockscreenView._stylingProvider
+ _OBJC_IVAR_$_MRULockscreenView._suggestionsView
+ _OBJC_IVAR_$_MRULockscreenView._timeControlsView
+ _OBJC_IVAR_$_MRULockscreenView._transportControlsView
+ _OBJC_IVAR_$_MRULockscreenView._volumeControlsView
+ _OBJC_IVAR_$_MRULockscreenViewController._delegate
+ _OBJC_IVAR_$_MRULockscreenViewController._dimmed
+ _OBJC_IVAR_$_MRULockscreenViewController._hardwareVolumeControlAssertion
+ _OBJC_IVAR_$_MRULockscreenViewController._hasPendingTraitCollectionUpdates
+ _OBJC_IVAR_$_MRULockscreenViewController._mediaControls
+ _OBJC_IVAR_$_MRULockscreenViewController._nowPlayingController
+ _OBJC_IVAR_$_MRULockscreenViewController._onScreen
+ _OBJC_IVAR_$_MRULockscreenViewController._pendingDimmed
+ _OBJC_IVAR_$_MRULockscreenViewController._pendingTimelineInvalidation
+ _OBJC_IVAR_$_MRULockscreenViewController._pendingVisualStylingProvider
+ _OBJC_IVAR_$_MRULockscreenViewController._showArtworkView
+ _OBJC_IVAR_$_MRULockscreenViewController._stateHandle
+ _OBJC_IVAR_$_MRULockscreenViewController._stylingProvider
+ _OBJC_IVAR_$_MRULockscreenViewController._suggestionsViewController
+ _OBJC_IVAR_$_MRULockscreenViewController._waveformController
+ _OBJC_IVAR_$_MRULockscreenViewController._waveformViewController
+ _OBJC_IVAR_$_MRUNowPlayingTimeControlsView._regexNumberDecimalDigit
+ _OBJC_IVAR_$_MRURecommendation._contextIdentifier
+ _OBJC_IVAR_$_MRURouteRecommendationPlatterViewController._dimmed
+ _OBJC_IVAR_$_MRURouteRecommendationPlatterViewController._hasPendingTraitCollectionUpdates
+ _OBJC_IVAR_$_MRURouteRecommendationPlatterViewController._pendingDimmed
+ _OBJC_IVAR_$_MRUVolumeViewController._pendingExpanded
+ _OBJC_IVAR_$_MRUWaveformSettings._nonVariableFramerate
+ _OBJC_IVAR_$_MRUWaveformSettings._supportsVariableFramerate
+ _OBJC_METACLASS_$_MRULockscreenView
+ _OBJC_METACLASS_$_MRULockscreenViewController
+ __OBJC_$_CATEGORY_UIImage_$_MediaControls
+ __OBJC_$_INSTANCE_METHODS_MRULockscreenView
+ __OBJC_$_INSTANCE_METHODS_MRULockscreenViewController
+ __OBJC_$_INSTANCE_METHODS_MRUNowPlayingViewController(Analytics)
+ __OBJC_$_INSTANCE_METHODS_UIImage(MediaControls)
+ __OBJC_$_INSTANCE_VARIABLES_MRULockscreenView
+ __OBJC_$_INSTANCE_VARIABLES_MRULockscreenViewController
+ __OBJC_$_PROP_LIST_MRULockscreenView
+ __OBJC_$_PROP_LIST_MRULockscreenViewController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__UISliderFluidInteractionDelegate
+ __OBJC_CLASS_PROTOCOLS_$_MRULockscreenView
+ __OBJC_CLASS_PROTOCOLS_$_MRULockscreenViewController
+ __OBJC_CLASS_RO_$_MRULockscreenView
+ __OBJC_CLASS_RO_$_MRULockscreenViewController
+ __OBJC_METACLASS_RO_$_MRULockscreenView
+ __OBJC_METACLASS_RO_$_MRULockscreenViewController
+ ___40-[MRULockscreenView setSuggestionsView:]_block_invoke
+ ___41-[MRURoutingViewController _applyUpdate:]_block_invoke.231
+ ___41-[MRURoutingViewController _applyUpdate:]_block_invoke.239
+ ___41-[MRURoutingViewController _applyUpdate:]_block_invoke_2.232
+ ___41-[MRURoutingViewController _applyUpdate:]_block_invoke_3.234
+ ___41-[MRURoutingViewController _applyUpdate:]_block_invoke_4.235
+ ___42-[MRULockscreenViewController viewDidLoad]_block_invoke
+ ___42-[MRULockscreenViewController viewDidLoad]_block_invoke_2
+ ___51-[MRULockscreenViewController updateNowPlayingInfo]_block_invoke
+ ___51-[MRULockscreenViewController updateNowPlayingInfo]_block_invoke_2
+ ___53-[MRUMediaSuggestionsController updateLastPlayedDate]_block_invoke.7
+ ___54-[MediaControlsEndpointsManager loadActiveSystemRoute]_block_invoke
+ ___54-[MediaControlsEndpointsManager loadActiveSystemRoute]_block_invoke_2
+ ___55-[MRURouteRecommender initializeSessionWhenAppropriate]_block_invoke.142
+ ___59-[MRULockscreenViewController updateRoutingButtonAnimated:]_block_invoke
+ ___62-[MRULockscreenViewController updateLayoutDependantProperties]_block_invoke
+ ___62-[MRULockscreenViewController updateLayoutDependantProperties]_block_invoke_2
+ ___63-[MRULockscreenViewController invalidateAllTimelinesForReason:]_block_invoke
+ ___66-[MRURoutingViewController handleGroupSessionJoinWithPickedRoute:]_block_invoke.206
+ ___67-[MRURoutingViewController selectRoutes:operation:routingViewItem:]_block_invoke.276
+ ___68-[MRULockscreenViewController schedulePendingTraitCollectionUpdates]_block_invoke
+ ___69-[MediaControlsEndpointsManager getOutputDeviceIsPlaying:completion:]_block_invoke.29
+ ___69-[MediaControlsEndpointsManager getOutputDeviceIsPlaying:completion:]_block_invoke.31
+ ___76-[MRULockscreenViewController transportControlsView:didSelectRoutingButton:]_block_invoke
+ ___84-[MRURouteRecommendationPlatterViewController schedulePendingTraitCollectionUpdates]_block_invoke
+ ___84-[MRURoutingViewController _wouldEndGroupSessionForViewItem:operation:pickedRoutes:]_block_invoke
+ ___84-[MRURoutingViewController _wouldEndGroupSessionForViewItem:operation:pickedRoutes:]_block_invoke_2
+ ___84-[MRURoutingViewController _wouldEndGroupSessionForViewItem:operation:pickedRoutes:]_block_invoke_3
+ ___93-[MRULockscreenViewController mediaSuggestionsViewController:didSelectSuggestion:completion:]_block_invoke
+ ___MRUDeviceSupportsVariableFrameRate_block_invoke
+ ___block_descriptor_32_e29_"NSString"16?0"MPAVRoute"8l
+ ___block_descriptor_32_e37_"MRAVOutputDevice"16?0"MPAVRoute"8l
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_40_e8_32s_e46_"MRURecommendation"16?0"IRCandidateResult"8ls32l8
+ ___block_descriptor_40_e8_32w_e19_v16?0"MPAVRoute"8lw32l8
+ ___block_descriptor_41_e8_32s_e8_v12?0B8ls32l8
+ ___block_descriptor_45_e8_32s_e5_v8?0ls32l8
+ ___block_literal_global.137
+ ___block_literal_global.199
+ ___block_literal_global.203
+ ___block_literal_global.214
+ ___block_literal_global.217
+ ___block_literal_global.229
+ ___block_literal_global.251
+ ___block_literal_global.256
+ ___block_literal_global.278
+ ___block_literal_global.282
+ _objc_msgSend$_wouldEndGroupSessionForViewItem:operation:pickedRoutes:
+ _objc_msgSend$accessoryBatteryLevelCase:
+ _objc_msgSend$accessoryBatteryLevelCombinedLeft:right:
+ _objc_msgSend$accessoryBatteryLevelLeft:
+ _objc_msgSend$accessoryBatteryLevelRight:
+ _objc_msgSend$accessoryBatteryLevelSingle:
+ _objc_msgSend$airPlayConnectionErrorMessage:
+ _objc_msgSend$composedBy:
+ _objc_msgSend$contextIdentifier
+ _objc_msgSend$createNowPlayingController
+ _objc_msgSend$createWaveformViewController
+ _objc_msgSend$isMediaSuggestionsDevEnabled
+ _objc_msgSend$loadActiveSystemRoute
+ _objc_msgSend$localizedStringWithKey:expectedFormat:
+ _objc_msgSend$localizedUppercaseStringWithKey:expectedFormat:
+ _objc_msgSend$lockscreenViewController:didSelectArtworkView:
+ _objc_msgSend$lockscreenViewController:didUpdatePreferredContentSize:
+ _objc_msgSend$lockscreenViewController:didUpdateRestrictedRects:
+ _objc_msgSend$mru_imageFittingSize:
+ _objc_msgSend$nonVariableFramerate
+ _objc_msgSend$pendingExpanded
+ _objc_msgSend$pendingState
+ _objc_msgSend$recommendationWithIRCandidateResult:contextIdentifier:
+ _objc_msgSend$routingHijackLocalMessagePresentingApp:busyRouteName:
+ _objc_msgSend$routingHijackLocalTitle:
+ _objc_msgSend$routingInUseOnPairedDevice:
+ _objc_msgSend$setContextIdentifier:
+ _objc_msgSend$setWaveformView:
+ _objc_msgSend$supportsVariableFramerate
+ _objc_msgSend$updateActiveSystemRoute:
+ _objc_msgSend$updateLayoutDependantProperties
+ _objc_msgSend$updateLayoutWithAnimations:completion:
+ _objc_msgSend$updateMarqueeAnimation
+ _objc_msgSend$waveformNonVariableFramerate
- +[MRURecommendation recommendationWithIRCandidateResult:]
- +[MRUStringsProvider accessoryBatteryLevelCase]
- +[MRUStringsProvider accessoryBatteryLevelCombined]
- +[MRUStringsProvider accessoryBatteryLevelLeft]
- +[MRUStringsProvider accessoryBatteryLevelRight]
- +[MRUStringsProvider accessoryBatteryLevelSingle]
- +[MRUStringsProvider airPlayConnectionErrorMessage]
- +[MRUStringsProvider composedBy]
- +[MRUStringsProvider routingHijackLocalMessage]
- +[MRUStringsProvider routingHijackLocalTitle]
- +[MRUStringsProvider routingInUseOnPairedDevice]
- -[MRUAssetManager resizeImage:size:]
- -[MRUControlCenterViewController didTransitionToExpandedContentMode:]
- -[MRUNowPlayingHeaderView initWithWaveformView:]
- -[MRUNowPlayingHeaderView init]
- -[MRUNowPlayingTransportControlsView didSelectLeadingButton:]
- -[MRUNowPlayingTransportControlsView leadingButtonHandler]
- -[MRUNowPlayingTransportControlsView setLeadingButtonHandler:]
- -[MRUNowPlayingTransportControlsView showLeadingButton]
- -[MRUNowPlayingView initWithWaveformView:]
- -[MRUNowPlayingView init]
- -[MRUNowPlayingViewController setWaveformController:]
- -[MRUNowPlayingViewController setWaveformViewController:]
- -[MRUNowPlayingViewController updateWaveformVisibility]
- -[MRUNowPlayingViewController waveformController]
- -[MRUNowPlayingViewController waveformViewController]
- -[MRUNowPlayingViewController(Debugging) lockScreenInternalRoutePickerOverrideWithDefaultStyle:]
- -[MRUNowPlayingViewController(Debugging) lockScreenPresentsOverrideRoutePicker]
- -[MediaControlsEndpointsManager _updateActiveRouteWithReason:]
- GCC_except_table106
- GCC_except_table134
- GCC_except_table171
- GCC_except_table214
- GCC_except_table30
- GCC_except_table92
- GCC_except_table98
- _MRUCondensedModuleMaxWidth
- _OBJC_IVAR_$_MRUNowPlayingTransportControlsView._leadingButtonHandler
- _OBJC_IVAR_$_MRUNowPlayingViewController._waveformController
- _OBJC_IVAR_$_MRUNowPlayingViewController._waveformViewController
- __OBJC_$_INSTANCE_METHODS_MRUNowPlayingViewController(Analytics|Debugging)
- ___41-[MRURoutingViewController _applyUpdate:]_block_invoke.225
- ___41-[MRURoutingViewController _applyUpdate:]_block_invoke.233
- ___41-[MRURoutingViewController _applyUpdate:]_block_invoke_2.226
- ___41-[MRURoutingViewController _applyUpdate:]_block_invoke_3.228
- ___41-[MRURoutingViewController _applyUpdate:]_block_invoke_4.229
- ___53-[MRUMediaSuggestionsController updateLastPlayedDate]_block_invoke.6
- ___55-[MRURouteRecommender initializeSessionWhenAppropriate]_block_invoke.132
- ___60-[MRUNowPlayingTransportControlsView configureLeadingButton]_block_invoke_2
- ___62-[MediaControlsEndpointsManager _updateActiveRouteWithReason:]_block_invoke
- ___62-[MediaControlsEndpointsManager _updateActiveRouteWithReason:]_block_invoke_2
- ___66-[MRURoutingViewController handleGroupSessionJoinWithPickedRoute:]_block_invoke.198
- ___67-[MRURoutingViewController selectRoutes:operation:routingViewItem:]_block_invoke.270
- ___69-[MediaControlsEndpointsManager getOutputDeviceIsPlaying:completion:]_block_invoke.34
- ___69-[MediaControlsEndpointsManager getOutputDeviceIsPlaying:completion:]_block_invoke.36
- ___block_descriptor_32_e46_"MRURecommendation"16?0"IRCandidateResult"8l
- ___block_descriptor_42_e8_32s_e56_v16?0"<UIViewControllerTransitionCoordinatorContext>"8ls32l8
- ___block_descriptor_48_e8_32s40w_e19_v16?0"MPAVRoute"8lw40l8s32l8
- ___block_descriptor_56_e8_32s_e56_v16?0"<UIViewControllerTransitionCoordinatorContext>"8ls32l8
- ___block_literal_global.127
- ___block_literal_global.153
- ___block_literal_global.207
- ___block_literal_global.210
- ___block_literal_global.223
- ___block_literal_global.245
- ___block_literal_global.250
- ___block_literal_global.269
- ___block_literal_global.276
- _objc_msgSend$_updateActiveRouteWithReason:
- _objc_msgSend$accessoryBatteryLevelCase
- _objc_msgSend$accessoryBatteryLevelCombined
- _objc_msgSend$accessoryBatteryLevelLeft
- _objc_msgSend$accessoryBatteryLevelRight
- _objc_msgSend$accessoryBatteryLevelSingle
- _objc_msgSend$airPlayConnectionErrorMessage
- _objc_msgSend$composedBy
- _objc_msgSend$isPlatterLiveWaveformEnabled
- _objc_msgSend$recommendationWithIRCandidateResult:
- _objc_msgSend$resizeImage:size:
- _objc_msgSend$routingHijackLocalMessage
- _objc_msgSend$routingHijackLocalTitle
- _objc_msgSend$routingInUseOnPairedDevice
- _objc_msgSend$setActiveSystemRoute:reason:
- _objc_msgSend$showLeadingButton
CStrings:
+ "\x11\x11%\x12\x11\x11"
+ "\x11\x16\x12"
+ "\x12;"
+ "!\xd1"
+ "#\x14"
+ "%@ %lu"
+ "%lu"
+ "%{public}@ removing hardware assertion: on screen: %{BOOL}u | show: %{BOOL}u | call: %{BOOL}u | route: %{public}@"
+ "%{public}@ taking hardware assertion: on screen: %{BOOL}u | show: %{BOOL}u | call: %{BOOL}u | route: %{public}@"
+ ", contextIdentifier: %@"
+ "@\"<MRULockscreenViewControllerDelegate>\""
+ "@\"MRAVOutputDevice\"16@?0@\"MPAVRoute\"8"
+ "@\"NSRegularExpression\""
+ "@\"NSString\"16@?0@\"MPAVRoute\"8"
+ "@32@0:8{CGSize=dd}16"
+ "Activity"
+ "ActivityBanner"
+ "B40@0:8@\"UISlider\"16{CGPoint=dd}24"
+ "B40@0:8@16{CGPoint=dd}24"
+ "GdXjx1ixZYvN9Gg8iSf68A"
+ "MRULockscreenView"
+ "MRULockscreenViewController"
+ "MediaSuggestionsDev"
+ "T@\"<MRULockscreenViewControllerDelegate>\",W,N,V_delegate"
+ "T@\"<SBUISystemApertureElement>\",?,R,W,N"
+ "T@\"BSAction\",?,R,N"
+ "T@\"MRULockscreenView\",&,D,N"
+ "T@\"NSArray\",?,R,N"
+ "T@\"NSRegularExpression\",&,N,V_regexNumberDecimalDigit"
+ "T@\"NSSet\",?,R,C,N"
+ "T@\"NSString\",&,N,V_contextIdentifier"
+ "T@\"NSString\",?,&,N"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"
+ "T@\"NSString\",?,R,C,N,V_associatedAppBundleIdentifier"
+ "T@\"NSString\",?,R,C,N,VassociatedScenePersistenceIdentifier"
+ "T@\"NSString\",?,R,N"
+ "T@\"NSURL\",?,R,C,N"
+ "T@\"UIColor\",?,R,C,N"
+ "T@\"UIView<SBUISystemApertureAccessoryView>\",?,R,N"
+ "T@\"UIViewPropertyAnimator\",?,R,N"
+ "T@\"UIWindowScene\",?,R,N"
+ "TB,?,N"
+ "TB,?,R,N"
+ "TB,?,R,N,GisOnScreen"
+ "TB,?,R,N,GisOnScreenForVolumeDisplay"
+ "TB,N,V_pendingExpanded"
+ "TB,N,V_supportsVariableFramerate"
+ "TQ,?,N"
+ "TQ,?,R,N"
+ "Td,?,R,N"
+ "Ti,N,V_nonVariableFramerate"
+ "Tq,?,R,N"
+ "Tq,N,V_pendingState"
+ "T{CGSize=dd},?,R,N"
+ "_contextIdentifier"
+ "_nonVariableFramerate"
+ "_pendingExpanded"
+ "_pendingState"
+ "_regexNumberDecimalDigit"
+ "_slider:shouldBeginDragAtPoint:"
+ "_supportsVariableFramerate"
+ "_wouldEndGroupSessionForViewItem:operation:pickedRoutes:"
+ "accessoryBatteryLevelCase:"
+ "accessoryBatteryLevelCombinedLeft:right:"
+ "accessoryBatteryLevelLeft:"
+ "accessoryBatteryLevelRight:"
+ "accessoryBatteryLevelSingle:"
+ "airPlayConnectionErrorMessage:"
+ "composedBy:"
+ "contextIdentifier"
+ "createNowPlayingController"
+ "createWaveformViewController"
+ "isMediaSuggestionsDevEnabled"
+ "loadActiveSystemRoute"
+ "localizedStringWithKey:expectedFormat:"
+ "localizedUppercaseStringWithKey:expectedFormat:"
+ "lockscreenViewController:didSelectArtworkView:"
+ "lockscreenViewController:didUpdatePreferredContentSize:"
+ "lockscreenViewController:didUpdateRestrictedRects:"
+ "mru_imageFittingSize:"
+ "nonVariableFramerate"
+ "now playing artwork changed"
+ "now playing route changed"
+ "now playing route image changed"
+ "pendingExpanded"
+ "pendingState"
+ "recommendationWithIRCandidateResult:contextIdentifier:"
+ "regexNumberDecimalDigit"
+ "route recommendation platter"
+ "routingHijackLocalMessagePresentingApp:busyRouteName:"
+ "routingHijackLocalTitle:"
+ "routingInUseOnPairedDevice:"
+ "setContextIdentifier:"
+ "setNonVariableFramerate:"
+ "setPendingExpanded:"
+ "setPendingState:"
+ "setRegexNumberDecimalDigit:"
+ "setSupportsVariableFramerate:"
+ "supportsVariableFramerate"
+ "updateActiveSystemRoute:"
+ "updateLayoutDependantProperties"
+ "updateLayoutWithAnimations:completion:"
+ "updateMarqueeAnimation"
+ "waveformNonVariableFramerate"
+ "\xa2"
- "\x11\x11'\x12\x11\x11"
- "\x12:"
- "!\xf1"
- "#\x15"
- "Analytics: Discovery mode changed to enabled"
- "Analytics: MPAVRoutingControllerActiveSystemRouteDidChangeNotification"
- "Analytics: Prewarm"
- "Analytics: Routes updated"
- "Session"
- "T@\"<SBUISystemApertureElement>\",R,W,N"
- "T@\"BSAction\",R,N"
- "T@\"NSSet\",R,C,N"
- "T@\"NSString\",R,C,N,V_associatedAppBundleIdentifier"
- "T@\"NSString\",R,C,N,VassociatedScenePersistenceIdentifier"
- "T@\"NSURL\",R,C,N"
- "T@\"UIColor\",R,C,N"
- "T@\"UIView<SBUISystemApertureAccessoryView>\",R,N"
- "T@\"UIViewPropertyAnimator\",R,N"
- "T@\"UIWindowScene\",R,N"
- "T@?,C,N,V_leadingButtonHandler"
- "TB,R,N,GisOnScreen"
- "TB,R,N,GisOnScreenForVolumeDisplay"
- "TQ,N"
- "TQ,R,N"
- "T{CGSize=dd},R,N"
- "_leadingButtonHandler"
- "_updateActiveRouteWithReason:"
- "accessoryBatteryLevelCase"
- "accessoryBatteryLevelCombined"
- "accessoryBatteryLevelLeft"
- "accessoryBatteryLevelRight"
- "accessoryBatteryLevelSingle"
- "airPlayConnectionErrorMessage"
- "com.apple.ScreenMirroringModule"
- "composedBy"
- "didSelectLeadingButton:"
- "leadingButtonHandler"
- "recommendationWithIRCandidateResult:"
- "resizeImage:size:"
- "routingHijackLocalMessage"
- "routingHijackLocalTitle"
- "routingInUseOnPairedDevice"
- "setLeadingButtonHandler:"
- "showLeadingButton"
- "\x92"

```
