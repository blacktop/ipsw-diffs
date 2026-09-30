## ContinuitySing

> `/System/Library/PrivateFrameworks/ContinuitySing.framework/ContinuitySing`

```diff

-650.0.0.122.4
-  __TEXT.__text: 0x31ff8
-  __TEXT.__auth_stubs: 0x11c0
-  __TEXT.__objc_methlist: 0x2148
-  __TEXT.__const: 0x5f4
-  __TEXT.__cstring: 0x35f9
-  __TEXT.__oslogstring: 0x1f99
-  __TEXT.__gcc_except_tab: 0x878
+655.0.0.122.4
+  __TEXT.__text: 0x38850
+  __TEXT.__auth_stubs: 0x11f0
+  __TEXT.__objc_methlist: 0x2788
+  __TEXT.__const: 0x624
+  __TEXT.__gcc_except_tab: 0x924
+  __TEXT.__cstring: 0x41e9
+  __TEXT.__oslogstring: 0x2559
   __TEXT.__ustring: 0x2a
   __TEXT.__swift5_typeref: 0x5ec
   __TEXT.__swift5_capture: 0x198

   __TEXT.__swift5_types: 0x24
   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x34
-  __TEXT.__unwind_info: 0xe58
+  __TEXT.__unwind_info: 0xfe0
   __TEXT.__eh_frame: 0x718
-  __TEXT.__objc_classname: 0x592
-  __TEXT.__objc_methname: 0x6265
-  __TEXT.__objc_methtype: 0xf8a
-  __TEXT.__objc_stubs: 0x5620
-  __DATA_CONST.__got: 0x5f8
-  __DATA_CONST.__const: 0x10a0
-  __DATA_CONST.__objc_classlist: 0x1c8
+  __TEXT.__objc_classname: 0x639
+  __TEXT.__objc_methname: 0x75c2
+  __TEXT.__objc_methtype: 0x1054
+  __TEXT.__objc_stubs: 0x5f00
+  __DATA_CONST.__got: 0x668
+  __DATA_CONST.__const: 0x11e8
+  __DATA_CONST.__objc_classlist: 0x208
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ac8
-  __DATA_CONST.__objc_superrefs: 0x170
-  __AUTH_CONST.__auth_got: 0x8f0
-  __AUTH_CONST.__const: 0x7d0
-  __AUTH_CONST.__cfstring: 0x1320
-  __AUTH_CONST.__objc_const: 0x4500
-  __AUTH.__objc_data: 0x12b8
+  __DATA_CONST.__objc_selrefs: 0x1ee0
+  __DATA_CONST.__objc_superrefs: 0x1c8
+  __AUTH_CONST.__auth_got: 0x908
+  __AUTH_CONST.__const: 0x810
+  __AUTH_CONST.__cfstring: 0x1860
+  __AUTH_CONST.__objc_const: 0x51b0
+  __AUTH_CONST.__objc_intobj: 0x48
+  __AUTH.__objc_data: 0x1538
   __AUTH.__data: 0x378
-  __DATA.__objc_ivar: 0x2a4
+  __DATA.__objc_ivar: 0x358
   __DATA.__data: 0x6e8
   __DATA.__bss: 0x350
   __DATA.__common: 0x30
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreHaptics.framework/CoreHaptics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/DeveloperToolsSupport.framework/DeveloperToolsSupport
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/MediaPlaybackCore.framework/MediaPlaybackCore
   - /System/Library/PrivateFrameworks/MediaPlayerUI.framework/MediaPlayerUI
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
+  - /System/Library/PrivateFrameworks/MediaServices.framework/MediaServices
   - /System/Library/PrivateFrameworks/MusicKitInternal.framework/MusicKitInternal
   - /System/Library/PrivateFrameworks/ProxCardKit.framework/ProxCardKit
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F5AE3F35-AD3B-3582-85C8-07AB5A86F06C
-  Functions: 1066
-  Symbols:   3633
-  CStrings:  2024
+  UUID: A4AFE540-F97E-3254-B4C5-A79F59320006
+  Functions: 1241
+  Symbols:   4186
+  CStrings:  2389
 
Symbols:
+ +[CSDisplayModeMessage messageID]
+ +[CSDisplayModeMessage requiredParameters]
+ +[CSDisplayModeRequest messageID]
+ +[CSDisplayModeRequest responseMessageFromDictionary:]
+ +[CSDisplayModeResponse messageID]
+ +[CSDisplayModeResponse requiredParameters]
+ +[CSHandshakeMessage responseMessageFromDictionary:]
+ +[CSHandshakeResponseMessage messageID]
+ +[CSHandshakeResponseMessage requiredParameters]
+ +[CSVocalMessage messageID]
+ +[CSVocalMessage requiredParameters]
+ -[CSClient initWithHandshake:]
+ -[CSDisplayModeMessage dictionaryRepresentation]
+ -[CSDisplayModeMessage enableSDR]
+ -[CSDisplayModeMessage initWithEnableSDR:]
+ -[CSDisplayModeMessage initWithMessage:]
+ -[CSDisplayModeResponse dictionaryRepresentation]
+ -[CSDisplayModeResponse enableSDR]
+ -[CSDisplayModeResponse initWithEnableSDR:]
+ -[CSDisplayModeResponse initWithMessage:]
+ -[CSHandshakeMessage minimumRequiredOperatingSystemVersion]
+ -[CSHandshakeMessage minimumRequiredProtocolVersion]
+ -[CSHandshakeResponseMessage dictionaryRepresentation]
+ -[CSHandshakeResponseMessage initWithMessage:]
+ -[CSHandshakeResponseMessage initWithMicrophoneActivation:]
+ -[CSHandshakeResponseMessage operatingSystemVersion]
+ -[CSHandshakeResponseMessage protocolVersion]
+ -[CSHandshakeResponseMessage shouldActivateMicrophone]
+ -[CSHapticsPlayer .cxx_destruct]
+ -[CSHapticsPlayer _hapticIntensityValueForIntensity:]
+ -[CSHapticsPlayer _onEngineReset]
+ -[CSHapticsPlayer _onEngineStopsWithReason:]
+ -[CSHapticsPlayer _onEngineStopsWithReason:].cold.1
+ -[CSHapticsPlayer _playButtonFeedbackWithIntensity:andSharpness:]
+ -[CSHapticsPlayer _playButtonFeedbackWithIntensity:andSharpness:].cold.1
+ -[CSHapticsPlayer _playButtonFeedbackWithIntensity:andSharpness:].cold.2
+ -[CSHapticsPlayer _playButtonFeedbackWithIntensity:andSharpness:].cold.3
+ -[CSHapticsPlayer _playButtonFeedbackWithIntensity:andSharpness:].cold.4
+ -[CSHapticsPlayer _playButtonFeedbackWithIntensity:andSharpness:].cold.5
+ -[CSHapticsPlayer _reverbHapticSharpnessValueForIntensity:]
+ -[CSHapticsPlayer _setupHapticEngine]
+ -[CSHapticsPlayer _setupHapticEngine].cold.1
+ -[CSHapticsPlayer _setupHapticEngine].cold.2
+ -[CSHapticsPlayer _startHapticsEngineWithCompletion:]
+ -[CSHapticsPlayer engine]
+ -[CSHapticsPlayer init]
+ -[CSHapticsPlayer playButtonFeedback]
+ -[CSHapticsPlayer playButtonFeedback].cold.1
+ -[CSHapticsPlayer playReverbButtonFeedbackWithIntensity:]
+ -[CSHapticsPlayer playReverbButtonFeedbackWithIntensity:].cold.1
+ -[CSHapticsPlayer playVocalButtonFeedbackWithIntensity:]
+ -[CSHapticsPlayer playVocalButtonFeedbackWithIntensity:].cold.1
+ -[CSHapticsPlayer player]
+ -[CSHapticsPlayer setEngine:]
+ -[CSHapticsPlayer setPlayer:]
+ -[CSHapticsPlayer setState:]
+ -[CSHapticsPlayer setSupportsHaptics:]
+ -[CSHapticsPlayer state]
+ -[CSHapticsPlayer supportsHaptics]
+ -[CSHelpPanelViewController .cxx_destruct]
+ -[CSHelpPanelViewController _canShowWhileLocked]
+ -[CSHelpPanelViewController _createViews]
+ -[CSHelpPanelViewController _handleDismiss]
+ -[CSHelpPanelViewController _handleSDRSwitch]
+ -[CSHelpPanelViewController _labelWithLocalizationKey:textStyle:weight:color:variant:]
+ -[CSHelpPanelViewController _setupConstraints]
+ -[CSHelpPanelViewController _setupStackView]
+ -[CSHelpPanelViewController _updateSDRButtonTitle]
+ -[CSHelpPanelViewController divider]
+ -[CSHelpPanelViewController gameModeNoticeLabel]
+ -[CSHelpPanelViewController gameModeTitleLabel]
+ -[CSHelpPanelViewController gameModelDescriptionLabel]
+ -[CSHelpPanelViewController initWithRequestClient:]
+ -[CSHelpPanelViewController isSDREnabled]
+ -[CSHelpPanelViewController latencyCardViewController]
+ -[CSHelpPanelViewController requestClient]
+ -[CSHelpPanelViewController scrollView]
+ -[CSHelpPanelViewController sdrDescriptionLabel]
+ -[CSHelpPanelViewController sdrSwitchButtonDescription]
+ -[CSHelpPanelViewController sdrSwitchButton]
+ -[CSHelpPanelViewController sdrTitleLabel]
+ -[CSHelpPanelViewController setDivider:]
+ -[CSHelpPanelViewController setGameModeNoticeLabel:]
+ -[CSHelpPanelViewController setGameModeTitleLabel:]
+ -[CSHelpPanelViewController setGameModelDescriptionLabel:]
+ -[CSHelpPanelViewController setIsSDREnabled:]
+ -[CSHelpPanelViewController setLatencyCardViewController:]
+ -[CSHelpPanelViewController setScrollView:]
+ -[CSHelpPanelViewController setSdrDescriptionLabel:]
+ -[CSHelpPanelViewController setSdrSwitchButton:]
+ -[CSHelpPanelViewController setSdrSwitchButtonDescription:]
+ -[CSHelpPanelViewController setSdrTitleLabel:]
+ -[CSHelpPanelViewController setStackView:]
+ -[CSHelpPanelViewController setTitleLabel:]
+ -[CSHelpPanelViewController stackView]
+ -[CSHelpPanelViewController titleLabel]
+ -[CSHelpPanelViewController viewDidLoad]
+ -[CSLatencyCardViewController _cancel]
+ -[CSLatencyCardViewController _handleButtonAction]
+ -[CSLatencyCardViewController _latencyResultForCurrentState]
+ -[CSLatencyCardViewController _setUpContentView]
+ -[CSLatencyCardViewController _setupActionButton]
+ -[CSLatencyCardViewController _updateViewFromCurrentStateAnimated:]
+ -[CSLatencyCardViewController _updateViewFromCurrentState]
+ -[CSLatencyCardViewController actionButton]
+ -[CSLatencyCardViewController activityIndicatorView]
+ -[CSLatencyCardViewController cardState]
+ -[CSLatencyCardViewController errorState]
+ -[CSLatencyCardViewController idleStateConstraints]
+ -[CSLatencyCardViewController instructionDescriptionLabel]
+ -[CSLatencyCardViewController instructionTitleLabel]
+ -[CSLatencyCardViewController latency]
+ -[CSLatencyCardViewController resultLabel]
+ -[CSLatencyCardViewController resultStateConstraints]
+ -[CSMicControl nextInitialVelocityForAnimation]
+ -[CSMicControl setNextInitialVelocityForAnimation:]
+ -[CSPaddingView .cxx_destruct]
+ -[CSPaddingView _updateConstraints]
+ -[CSPaddingView bottomPadding]
+ -[CSPaddingView initWithWrappedView:]
+ -[CSPaddingView leadingPadding]
+ -[CSPaddingView setBottomPadding:]
+ -[CSPaddingView setHorizontalPadding:]
+ -[CSPaddingView setLeadingPadding:]
+ -[CSPaddingView setTopPadding:]
+ -[CSPaddingView setTrailingPadding:]
+ -[CSPaddingView setVerticalPadding:]
+ -[CSPaddingView setWrappedView:]
+ -[CSPaddingView topPadding]
+ -[CSPaddingView trailingPadding]
+ -[CSPaddingView wrappedView]
+ -[CSRemoteRequestClient _handleHandshakeResponse:error:]
+ -[CSRemoteRequestClient _handleHandshakeResponse:error:].cold.1
+ -[CSRemoteRequestClient _handleHandshakeResponse:error:].cold.2
+ -[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]
+ -[CSRemoteRequestClient retrieveDisplayMode:]
+ -[CSRemoteRequestClient sendDisplayMode:]
+ -[CSRemoteRequestClient sendVocalLevel:]
+ -[CSShieldConnectionManager _attemptReconnect]
+ -[CSShieldConnectionManager _handlePresentShieldError:].cold.1
+ -[CSShieldConnectionManager _handleServerConnectionError:]
+ -[CSShieldConnectionManager _handleServerConnectionError:].cold.1
+ -[CSShieldConnectionManager bootstrapFromRemoteDisplayConnection:]
+ -[CSShieldConnectionManager sceneDidBecomeActive]
+ -[CSShieldManager _finishLoading]
+ -[CSShieldManager _invalidateRequestClient]
+ -[CSShieldManager requestMicrophoneActivationWithCompletion:]
+ -[CSShieldViewController _presentEndpointDisconnectedError]
+ -[CSShieldViewController _presentVersionMismatchError:]
+ -[CSVocalMessage dictionaryRepresentation]
+ -[CSVocalMessage initWithMessage:]
+ -[CSVocalMessage initWithVocalLevel:]
+ -[CSVocalMessage vocalLevel]
+ GCC_except_table129
+ GCC_except_table14
+ GCC_except_table32
+ GCC_except_table34
+ GCC_except_table41
+ GCC_except_table45
+ GCC_except_table61
+ GCC_except_table64
+ GCC_except_table85
+ GCC_except_table88
+ _CFDictionaryGetInt64
+ _CHHapticEventParameterIDHapticIntensity
+ _CHHapticEventParameterIDHapticSharpness
+ _CHHapticEventTypeHapticTransient
+ _CSMinRequiredTVOSVersion
+ _CSRemoteRequestClientErrorCodeKey
+ _CSRemoteRequestClientErrorNotification
+ _CSRemoteRequestServerErrorDomain
+ _OBJC_CLASS_$_CHHapticEngine
+ _OBJC_CLASS_$_CHHapticEvent
+ _OBJC_CLASS_$_CHHapticEventParameter
+ _OBJC_CLASS_$_CHHapticPattern
+ _OBJC_CLASS_$_CSDisplayModeMessage
+ _OBJC_CLASS_$_CSDisplayModeRequest
+ _OBJC_CLASS_$_CSDisplayModeResponse
+ _OBJC_CLASS_$_CSHandshakeResponseMessage
+ _OBJC_CLASS_$_CSHapticsPlayer
+ _OBJC_CLASS_$_CSHelpPanelViewController
+ _OBJC_CLASS_$_CSPaddingView
+ _OBJC_CLASS_$_CSVocalMessage
+ _OBJC_CLASS_$_MSVBlockGuard
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_UIBarButtonItem
+ _OBJC_CLASS_$_UINavigationController
+ _OBJC_CLASS_$_UIScrollView
+ _OBJC_IVAR_$_CSDisplayModeMessage._enableSDR
+ _OBJC_IVAR_$_CSDisplayModeResponse._enableSDR
+ _OBJC_IVAR_$_CSHandshakeMessage._minimumRequiredOperatingSystemVersion
+ _OBJC_IVAR_$_CSHandshakeMessage._minimumRequiredProtocolVersion
+ _OBJC_IVAR_$_CSHandshakeResponseMessage._operatingSystemVersion
+ _OBJC_IVAR_$_CSHandshakeResponseMessage._protocolVersion
+ _OBJC_IVAR_$_CSHandshakeResponseMessage._shouldActivateMicrophone
+ _OBJC_IVAR_$_CSHapticsPlayer._engine
+ _OBJC_IVAR_$_CSHapticsPlayer._player
+ _OBJC_IVAR_$_CSHapticsPlayer._state
+ _OBJC_IVAR_$_CSHapticsPlayer._supportsHaptics
+ _OBJC_IVAR_$_CSHelpPanelViewController._divider
+ _OBJC_IVAR_$_CSHelpPanelViewController._gameModeNoticeLabel
+ _OBJC_IVAR_$_CSHelpPanelViewController._gameModeTitleLabel
+ _OBJC_IVAR_$_CSHelpPanelViewController._gameModelDescriptionLabel
+ _OBJC_IVAR_$_CSHelpPanelViewController._isSDREnabled
+ _OBJC_IVAR_$_CSHelpPanelViewController._latencyCardViewController
+ _OBJC_IVAR_$_CSHelpPanelViewController._requestClient
+ _OBJC_IVAR_$_CSHelpPanelViewController._scrollView
+ _OBJC_IVAR_$_CSHelpPanelViewController._sdrDescriptionLabel
+ _OBJC_IVAR_$_CSHelpPanelViewController._sdrSwitchButton
+ _OBJC_IVAR_$_CSHelpPanelViewController._sdrSwitchButtonDescription
+ _OBJC_IVAR_$_CSHelpPanelViewController._sdrTitleLabel
+ _OBJC_IVAR_$_CSHelpPanelViewController._stackView
+ _OBJC_IVAR_$_CSHelpPanelViewController._titleLabel
+ _OBJC_IVAR_$_CSLatencyCardViewController._actionButton
+ _OBJC_IVAR_$_CSLatencyCardViewController._activityIndicatorView
+ _OBJC_IVAR_$_CSLatencyCardViewController._cardState
+ _OBJC_IVAR_$_CSLatencyCardViewController._errorState
+ _OBJC_IVAR_$_CSLatencyCardViewController._idleStateConstraints
+ _OBJC_IVAR_$_CSLatencyCardViewController._instructionDescriptionLabel
+ _OBJC_IVAR_$_CSLatencyCardViewController._instructionTitleLabel
+ _OBJC_IVAR_$_CSLatencyCardViewController._latency
+ _OBJC_IVAR_$_CSLatencyCardViewController._resultLabel
+ _OBJC_IVAR_$_CSLatencyCardViewController._resultStateConstraints
+ _OBJC_IVAR_$_CSMicControl._nextInitialVelocityForAnimation
+ _OBJC_IVAR_$_CSPaddingView._bottomConstraint
+ _OBJC_IVAR_$_CSPaddingView._bottomPadding
+ _OBJC_IVAR_$_CSPaddingView._leadingConstraint
+ _OBJC_IVAR_$_CSPaddingView._leadingPadding
+ _OBJC_IVAR_$_CSPaddingView._topConstraint
+ _OBJC_IVAR_$_CSPaddingView._topPadding
+ _OBJC_IVAR_$_CSPaddingView._trailingConstraint
+ _OBJC_IVAR_$_CSPaddingView._trailingPadding
+ _OBJC_IVAR_$_CSPaddingView._wrappedView
+ _OBJC_IVAR_$_CSRemoteRequestClient._activationGuard
+ _OBJC_IVAR_$_CSRemoteRequestClient._connectionCompletionHandler
+ _OBJC_IVAR_$_CSRemoteRequestClient._pendingActivationDeviceFoundHandler
+ _OBJC_IVAR_$_CSRemoteRequestClient._serverHandshake
+ _OBJC_IVAR_$_CSShieldConnectionManager._firstSceneDidBecomeActive
+ _OBJC_IVAR_$_CSShieldViewController._hapticsPlayer
+ _OBJC_IVAR_$_CSVocalMessage._vocalLevel
+ _OBJC_METACLASS_$_CSDisplayModeMessage
+ _OBJC_METACLASS_$_CSDisplayModeRequest
+ _OBJC_METACLASS_$_CSDisplayModeResponse
+ _OBJC_METACLASS_$_CSHandshakeResponseMessage
+ _OBJC_METACLASS_$_CSHapticsPlayer
+ _OBJC_METACLASS_$_CSHelpPanelViewController
+ _OBJC_METACLASS_$_CSPaddingView
+ _OBJC_METACLASS_$_CSVocalMessage
+ _UIEdgeInsetsMakeWithEdges
+ _UIFontTextStyleCallout
+ _UIFontTextStyleTitle2
+ __OBJC_$_CLASS_METHODS_CSDisplayModeMessage
+ __OBJC_$_CLASS_METHODS_CSDisplayModeRequest
+ __OBJC_$_CLASS_METHODS_CSDisplayModeResponse
+ __OBJC_$_CLASS_METHODS_CSHandshakeResponseMessage
+ __OBJC_$_CLASS_METHODS_CSVocalMessage
+ __OBJC_$_INSTANCE_METHODS_CSDisplayModeMessage
+ __OBJC_$_INSTANCE_METHODS_CSDisplayModeResponse
+ __OBJC_$_INSTANCE_METHODS_CSHandshakeResponseMessage
+ __OBJC_$_INSTANCE_METHODS_CSHapticsPlayer
+ __OBJC_$_INSTANCE_METHODS_CSHelpPanelViewController
+ __OBJC_$_INSTANCE_METHODS_CSPaddingView
+ __OBJC_$_INSTANCE_METHODS_CSVocalMessage
+ __OBJC_$_INSTANCE_VARIABLES_CSDisplayModeMessage
+ __OBJC_$_INSTANCE_VARIABLES_CSDisplayModeResponse
+ __OBJC_$_INSTANCE_VARIABLES_CSHandshakeResponseMessage
+ __OBJC_$_INSTANCE_VARIABLES_CSHapticsPlayer
+ __OBJC_$_INSTANCE_VARIABLES_CSHelpPanelViewController
+ __OBJC_$_INSTANCE_VARIABLES_CSPaddingView
+ __OBJC_$_INSTANCE_VARIABLES_CSVocalMessage
+ __OBJC_$_PROP_LIST_CSDisplayModeMessage
+ __OBJC_$_PROP_LIST_CSDisplayModeResponse
+ __OBJC_$_PROP_LIST_CSHandshakeResponseMessage
+ __OBJC_$_PROP_LIST_CSHapticsPlayer
+ __OBJC_$_PROP_LIST_CSHelpPanelViewController
+ __OBJC_$_PROP_LIST_CSPaddingView
+ __OBJC_$_PROP_LIST_CSVocalMessage
+ __OBJC_CLASS_RO_$_CSDisplayModeMessage
+ __OBJC_CLASS_RO_$_CSDisplayModeRequest
+ __OBJC_CLASS_RO_$_CSDisplayModeResponse
+ __OBJC_CLASS_RO_$_CSHandshakeResponseMessage
+ __OBJC_CLASS_RO_$_CSHapticsPlayer
+ __OBJC_CLASS_RO_$_CSHelpPanelViewController
+ __OBJC_CLASS_RO_$_CSPaddingView
+ __OBJC_CLASS_RO_$_CSVocalMessage
+ __OBJC_METACLASS_RO_$_CSDisplayModeMessage
+ __OBJC_METACLASS_RO_$_CSDisplayModeRequest
+ __OBJC_METACLASS_RO_$_CSDisplayModeResponse
+ __OBJC_METACLASS_RO_$_CSHandshakeResponseMessage
+ __OBJC_METACLASS_RO_$_CSHapticsPlayer
+ __OBJC_METACLASS_RO_$_CSHelpPanelViewController
+ __OBJC_METACLASS_RO_$_CSPaddingView
+ __OBJC_METACLASS_RO_$_CSVocalMessage
+ ___119-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke
+ ___119-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke.11
+ ___119-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke.12
+ ___119-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke.12.cold.1
+ ___119-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke.14
+ ___119-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke_2
+ ___119-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke_3
+ ___37-[CSHapticsPlayer _setupHapticEngine]_block_invoke
+ ___37-[CSHapticsPlayer _setupHapticEngine]_block_invoke_2
+ ___40-[CSRemoteRequestClient sendVocalLevel:]_block_invoke
+ ___40-[CSRemoteRequestClient sendVocalLevel:]_block_invoke.cold.1
+ ___41-[CSRemoteRequestClient sendDisplayMode:]_block_invoke
+ ___41-[CSRemoteRequestClient sendDisplayMode:]_block_invoke.cold.1
+ ___42-[CSShieldViewController _showMusicUpsell]_block_invoke.211
+ ___44-[CSShieldViewController presentMusicPicker]_block_invoke.115
+ ___45-[CSRemoteRequestClient retrieveDisplayMode:]_block_invoke
+ ___45-[CSRemoteRequestClient retrieveDisplayMode:]_block_invoke.cold.1
+ ___46-[CSShieldViewController _presentPairingError]_block_invoke.175
+ ___46-[CSShieldViewController _presentPairingError]_block_invoke.179
+ ___46-[CSShieldViewController _presentPairingError]_block_invoke.184
+ ___46-[CSShieldViewController _presentPairingError]_block_invoke_2.183
+ ___49-[CSLatencyCardViewController _setupActionButton]_block_invoke
+ ___49-[CSShieldConnectionManager sceneDidBecomeActive]_block_invoke
+ ___51-[CSHelpPanelViewController initWithRequestClient:]_block_invoke
+ ___51-[CSHelpPanelViewController initWithRequestClient:]_block_invoke_2
+ ___53-[CSHapticsPlayer _startHapticsEngineWithCompletion:]_block_invoke
+ ___53-[CSHapticsPlayer _startHapticsEngineWithCompletion:]_block_invoke.cold.1
+ ___53-[CSHapticsPlayer _startHapticsEngineWithCompletion:]_block_invoke.cold.2
+ ___53-[CSRemoteRequestClient sendEventMessage:completion:]_block_invoke.31
+ ___53-[CSShieldConnectionManager _requestGroupSessionURL:]_block_invoke.38
+ ___55-[CSRemoteRequestClient sendRequestMessage:completion:]_block_invoke.29
+ ___55-[CSShieldViewController _presentVersionMismatchError:]_block_invoke
+ ___55-[CSShieldViewController _presentVersionMismatchError:]_block_invoke.194
+ ___56-[CSRemoteRequestClient _activateMessageClientIfNeeded:]_block_invoke.25
+ ___56-[CSRemoteRequestClient _activateMessageClientIfNeeded:]_block_invoke_2.26
+ ___56-[CSRemoteRequestClient _activateMessageClientIfNeeded:]_block_invoke_3
+ ___56-[CSRemoteRequestClient _activateMessageClientIfNeeded:]_block_invoke_3.cold.1
+ ___56-[CSRemoteRequestClient _handleHandshakeResponse:error:]_block_invoke
+ ___57-[CSShieldConnectionManager _bootstrapFromSingQRCodeURL:]_block_invoke.33
+ ___57-[CSShieldViewController _handleInvalidMusicAccountError]_block_invoke.226
+ ___57-[CSShieldViewController _handleInvalidMusicAccountError]_block_invoke.227
+ ___57-[CSShieldViewController _handleInvalidMusicAccountError]_block_invoke.234
+ ___57-[CSShieldViewController _handleInvalidMusicAccountError]_block_invoke_2.233
+ ___57-[CSShieldViewController _handleInvalidMusicAccountError]_block_invoke_2.233.cold.1
+ ___58-[CSLatencyCardViewController _startAudioLatencyEstimator]_block_invoke_2
+ ___58-[CSShieldConnectionManager calculateErrorWithCompletion:]_block_invoke.29
+ ___59-[CSShieldViewController _presentEndpointDisconnectedError]_block_invoke
+ ___59-[CSShieldViewController _presentEndpointDisconnectedError]_block_invoke.244
+ ___59-[CSShieldViewController _presentEndpointDisconnectedError]_block_invoke.248
+ ___59-[CSShieldViewController _presentEndpointDisconnectedError]_block_invoke_2
+ ___61-[CSShieldManager requestMicrophoneActivationWithCompletion:]_block_invoke
+ ___61-[CSShieldManager requestMicrophoneActivationWithCompletion:]_block_invoke.cold.1
+ ___61-[CSShieldManager requestMicrophoneActivationWithCompletion:]_block_invoke_2
+ ___62-[CSShieldManager _bootstrapRequestClientIfNeededAndAvailable]_block_invoke_4
+ ___62-[CSShieldManager _bootstrapRequestClientIfNeededAndAvailable]_block_invoke_5
+ ___62-[CSShieldManager _bootstrapRequestClientIfNeededAndAvailable]_block_invoke_6
+ ___62-[CSShieldViewController consumeSinglePressDownForButtonKind:]_block_invoke.122
+ ___62-[CSShieldViewController consumeSinglePressDownForButtonKind:]_block_invoke_2.125
+ ___62-[CSShieldViewController consumeSinglePressDownForButtonKind:]_block_invoke_2.125.cold.1
+ ___65-[CSHapticsPlayer _playButtonFeedbackWithIntensity:andSharpness:]_block_invoke
+ ___65-[CSHapticsPlayer _playButtonFeedbackWithIntensity:andSharpness:]_block_invoke.18
+ ___65-[CSHapticsPlayer _playButtonFeedbackWithIntensity:andSharpness:]_block_invoke.cold.1
+ ___65-[CSHapticsPlayer _playButtonFeedbackWithIntensity:andSharpness:]_block_invoke_2
+ ___67-[CSLatencyCardViewController _updateViewFromCurrentStateAnimated:]_block_invoke
+ ___NSArray0__struct
+ ___block_descriptor_32_e17_q16?0"NSError"8l
+ ___block_descriptor_40_e8_32bs_e19_v16?0"MPAVRoute"8ls32l8
+ ___block_descriptor_40_e8_32bs_e20_v24?0q8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e48_v24?0"CSHandshakeResponseMessage"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e8_v16?0q8ls32l8
+ ___block_descriptor_40_e8_32w_e20_v20?0B8"NSError"12lw32l8
+ ___block_descriptor_40_e8_32w_e8_v16?0q8lw32l8
+ ___block_descriptor_41_e8_32w_e5_v8?0lw32l8
+ ___block_descriptor_48_e8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_48_e8_32s_e25_v24?0Q8"NSDictionary"16ls32l8
+ ___block_descriptor_56_e8_32s40bs48w_e43_v24?0"CSDisplayModeResponse"8"NSError"16lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40s48w_e18_v16?0"UIAction"8ls32l8w48l8s40l8
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_literal_global.114
+ ___block_literal_global.118
+ ___block_literal_global.121
+ ___block_literal_global.124
+ ___block_literal_global.150
+ ___block_literal_global.177
+ ___block_literal_global.20
+ ___block_literal_global.205
+ ___block_literal_global.213
+ ___block_literal_global.229
+ ___block_literal_global.46
+ ___block_literal_global.67
+ __os_log_debug_impl
+ _expf
+ _objc_msgSend$_attemptReconnect
+ _objc_msgSend$_cancel
+ _objc_msgSend$_createViews
+ _objc_msgSend$_finishLoading
+ _objc_msgSend$_handleButtonAction
+ _objc_msgSend$_handleHandshakeResponse:error:
+ _objc_msgSend$_hapticIntensityValueForIntensity:
+ _objc_msgSend$_invalidateRequestClient
+ _objc_msgSend$_labelWithLocalizationKey:textStyle:weight:color:variant:
+ _objc_msgSend$_latencyResultForCurrentState
+ _objc_msgSend$_onEngineReset
+ _objc_msgSend$_onEngineStopsWithReason:
+ _objc_msgSend$_playButtonFeedbackWithIntensity:andSharpness:
+ _objc_msgSend$_presentEndpointDisconnectedError
+ _objc_msgSend$_presentVersionMismatchError:
+ _objc_msgSend$_reverbHapticSharpnessValueForIntensity:
+ _objc_msgSend$_setContinuousCornerRadius:
+ _objc_msgSend$_setUpContentView
+ _objc_msgSend$_setupActionButton
+ _objc_msgSend$_setupConstraints
+ _objc_msgSend$_setupHapticEngine
+ _objc_msgSend$_setupStackView
+ _objc_msgSend$_startHapticsEngineWithCompletion:
+ _objc_msgSend$_updateConstraints
+ _objc_msgSend$_updateSDRButtonTitle
+ _objc_msgSend$_updateViewFromCurrentState
+ _objc_msgSend$_updateViewFromCurrentStateAnimated:
+ _objc_msgSend$animateWithSpringDuration:bounce:initialSpringVelocity:delay:options:animations:completion:
+ _objc_msgSend$bootstrapFromRemoteDisplayConnection:
+ _objc_msgSend$borderedButtonConfiguration
+ _objc_msgSend$capabilitiesForHardware
+ _objc_msgSend$code
+ _objc_msgSend$constraintGreaterThanOrEqualToAnchor:
+ _objc_msgSend$constraintGreaterThanOrEqualToConstant:
+ _objc_msgSend$constraintLessThanOrEqualToAnchor:
+ _objc_msgSend$constraintLessThanOrEqualToAnchor:constant:
+ _objc_msgSend$contentLayoutGuide
+ _objc_msgSend$createPlayerWithPattern:error:
+ _objc_msgSend$deactivateConstraints:
+ _objc_msgSend$disarm
+ _objc_msgSend$domain
+ _objc_msgSend$enableSDR
+ _objc_msgSend$initWithAudioSession:sessionIsShared:options:error:
+ _objc_msgSend$initWithEnableSDR:
+ _objc_msgSend$initWithEventType:parameters:relativeTime:duration:
+ _objc_msgSend$initWithEvents:parameters:error:
+ _objc_msgSend$initWithImage:style:target:action:
+ _objc_msgSend$initWithParameterID:value:
+ _objc_msgSend$initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:
+ _objc_msgSend$initWithRootViewController:
+ _objc_msgSend$initWithTimeout:interruptionHandler:
+ _objc_msgSend$initWithVocalLevel:
+ _objc_msgSend$initWithWrappedView:
+ _objc_msgSend$isSDREnabled
+ _objc_msgSend$navigationItem
+ _objc_msgSend$notifyWhenPlayersFinished:
+ _objc_msgSend$playButtonFeedback
+ _objc_msgSend$playReverbButtonFeedbackWithIntensity:
+ _objc_msgSend$playVocalButtonFeedbackWithIntensity:
+ _objc_msgSend$player
+ _objc_msgSend$quaternarySystemFillColor
+ _objc_msgSend$requestMicrophoneActivationWithCompletion:
+ _objc_msgSend$retrieveDisplayMode:
+ _objc_msgSend$sendDisplayMode:
+ _objc_msgSend$sendVocalLevel:
+ _objc_msgSend$separatorColor
+ _objc_msgSend$setAccessibilityIdentifier:
+ _objc_msgSend$setCustomSpacing:afterView:
+ _objc_msgSend$setHorizontalPadding:
+ _objc_msgSend$setIsSDREnabled:
+ _objc_msgSend$setLayoutMargins:
+ _objc_msgSend$setLayoutMarginsRelativeArrangement:
+ _objc_msgSend$setMuteHapticsWhileRecordingAudio:
+ _objc_msgSend$setPlaysHapticsOnly:
+ _objc_msgSend$setPrefersGrabberVisible:
+ _objc_msgSend$setPriority:
+ _objc_msgSend$setResetHandler:
+ _objc_msgSend$setRightBarButtonItem:
+ _objc_msgSend$setStoppedHandler:
+ _objc_msgSend$setSymbolConfiguration:
+ _objc_msgSend$setTitle:forState:
+ _objc_msgSend$setUserInterfaceStyle:
+ _objc_msgSend$sheetPresentationController
+ _objc_msgSend$shouldActivateMicrophone
+ _objc_msgSend$startAtTime:error:
+ _objc_msgSend$startWithCompletionHandler:
+ _objc_msgSend$stopAnimating
+ _objc_msgSend$supportsHaptics
+ _objc_msgSend$traitOverrides
+ _objc_msgSend$wrappedView
- -[CSClient deviceIdentifier]
- -[CSClient groupSessionIdentifier]
- -[CSClient initWithCompanionLinkDevice:handshake:]
- -[CSHandshakeMessage initWithMessage:].cold.1
- -[CSLatencyCardViewController _actionsForProgressEvent:]
- -[CSLatencyCardViewController _cancelAndDismiss]
- -[CSLatencyCardViewController _setupPRXActions]
- -[CSLatencyCardViewController cancelAction]
- -[CSLatencyCardViewController doneAction]
- -[CSLatencyCardViewController imageViewWidthConstraint]
- -[CSLatencyCardViewController instructionsLabel]
- -[CSLatencyCardViewController retryAction]
- -[CSLatencyCardViewController startAction]
- -[CSRemoteRequestClient _activateMessageClientIfNeeded:].cold.2
- -[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:]
- GCC_except_table127
- GCC_except_table15
- GCC_except_table22
- GCC_except_table36
- GCC_except_table40
- GCC_except_table56
- GCC_except_table82
- GCC_except_table86
- GCC_except_table89
- _OBJC_CLASS_$_PRXIconContentViewController
- _OBJC_IVAR_$_CSClient._deviceIdentifier
- _OBJC_IVAR_$_CSLatencyCardViewController._cancelAction
- _OBJC_IVAR_$_CSLatencyCardViewController._doneAction
- _OBJC_IVAR_$_CSLatencyCardViewController._imageViewWidthConstraint
- _OBJC_IVAR_$_CSLatencyCardViewController._instructionsLabel
- _OBJC_IVAR_$_CSLatencyCardViewController._retryAction
- _OBJC_IVAR_$_CSLatencyCardViewController._startAction
- _OBJC_METACLASS_$_PRXIconContentViewController
- ___42-[CSShieldViewController _showMusicUpsell]_block_invoke.191
- ___44-[CSShieldViewController presentMusicPicker]_block_invoke.102
- ___46-[CSShieldViewController _presentPairingError]_block_invoke.165
- ___46-[CSShieldViewController _presentPairingError]_block_invoke.169
- ___46-[CSShieldViewController _presentPairingError]_block_invoke.174
- ___46-[CSShieldViewController _presentPairingError]_block_invoke_2.173
- ___47-[CSLatencyCardViewController _setupPRXActions]_block_invoke
- ___47-[CSLatencyCardViewController _setupPRXActions]_block_invoke_2
- ___47-[CSLatencyCardViewController _setupPRXActions]_block_invoke_3
- ___47-[CSLatencyCardViewController _setupPRXActions]_block_invoke_4
- ___48-[CSShieldViewController _sendConnectMicRequest]_block_invoke.124
- ___48-[CSShieldViewController _sendConnectMicRequest]_block_invoke.124.cold.1
- ___53-[CSRemoteRequestClient sendEventMessage:completion:]_block_invoke.21
- ___53-[CSShieldConnectionManager _requestGroupSessionURL:]_block_invoke.36
- ___55-[CSRemoteRequestClient sendRequestMessage:completion:]_block_invoke.19
- ___57-[CSShieldConnectionManager _bootstrapFromSingQRCodeURL:]_block_invoke.31
- ___57-[CSShieldViewController _handleInvalidMusicAccountError]_block_invoke.206
- ___57-[CSShieldViewController _handleInvalidMusicAccountError]_block_invoke.207
- ___57-[CSShieldViewController _handleInvalidMusicAccountError]_block_invoke.214
- ___57-[CSShieldViewController _handleInvalidMusicAccountError]_block_invoke_2.213
- ___57-[CSShieldViewController _handleInvalidMusicAccountError]_block_invoke_2.213.cold.1
- ___58-[CSShieldConnectionManager calculateErrorWithCompletion:]_block_invoke.27
- ___62-[CSShieldViewController consumeSinglePressDownForButtonKind:]_block_invoke.109
- ___62-[CSShieldViewController consumeSinglePressDownForButtonKind:]_block_invoke_2.112
- ___62-[CSShieldViewController consumeSinglePressDownForButtonKind:]_block_invoke_2.112.cold.1
- ___91-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:]_block_invoke
- ___91-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:]_block_invoke.10
- ___91-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:]_block_invoke.5
- ___91-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:]_block_invoke.6
- ___91-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:]_block_invoke.6.cold.1
- ___91-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:]_block_invoke.8
- ___91-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:]_block_invoke_2
- ___91-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:]_block_invoke_2.cold.1
- ___block_descriptor_40_e8_32s_e20_v24?0q8"NSError"16ls32l8
- ___block_descriptor_40_e8_32w_e19_v16?0"MPAVRoute"8lw32l8
- ___block_descriptor_40_e8_32w_e25_v24?0Q8"NSDictionary"16lw32l8
- ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
- ___block_descriptor_48_e8_32s40w_e18_v16?0"UIAction"8lw40l8s32l8
- ___block_literal_global.101
- ___block_literal_global.105
- ___block_literal_global.108
- ___block_literal_global.111
- ___block_literal_global.140
- ___block_literal_global.167
- ___block_literal_global.185
- ___block_literal_global.193
- ___block_literal_global.209
- ___block_literal_global.35
- ___block_literal_global.56
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_ContinuitySing
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_ContinuitySing
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_ContinuitySing
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_ContinuitySing
- _objc_msgSend$_actionsForProgressEvent:
- _objc_msgSend$_setupPRXActions
- _objc_msgSend$_titleForProgressEvent:
- _objc_msgSend$actions
- _objc_msgSend$cancelAction
- _objc_msgSend$deviceIdentifier
- _objc_msgSend$doneAction
- _objc_msgSend$groupSessionIdentifier
- _objc_msgSend$hideActivityIndicator
- _objc_msgSend$imageView
- _objc_msgSend$imageViewWidthConstraint
- _objc_msgSend$initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:
- _objc_msgSend$instructionsLabel
- _objc_msgSend$removeAction:
- _objc_msgSend$retryAction
- _objc_msgSend$setBodyLabel:
- _objc_msgSend$setImageViews:
- _objc_msgSend$size
- _objc_msgSend$startAction
CStrings:
+ "\""
+ "%@\n%@"
+ "%s: %@ Ignoring first notification that scene did become active"
+ "%s: %@ Prox: %@"
+ "%s: %@ _invalidateRequestClient %@"
+ "%s: %@ sceneDidBecomeActive"
+ "%s: <%p> Attempt reconnect with remoteDisplayIdentifier: %@ URL: %@"
+ "%s: <%p> Skip reconnect we are already loaded"
+ "%s: Activating message client to %@ with %@"
+ "%s: CHHapticEngine reset"
+ "%s: Device does not support haptics."
+ "%s: Device found pending activation: %@"
+ "%s: Error creating CHHapticEngine: %@"
+ "%s: Error encountered while creating CHHapticPattern: %@"
+ "%s: Error encountered while creating CHHapticPatternPlayer: %@"
+ "%s: Error encountered while starting CHHapticEngine: %@"
+ "%s: Failed to start the haptic player. Error: %@"
+ "%s: Got handshake response but don't have a connectionCompletionHandler - are we getting this twice?"
+ "%s: Handshake indicates we should turn on the mic - let's do it!"
+ "%s: Haptics player starting"
+ "%s: HapticsEngine stopped! Reason: %ld"
+ "%s: Received mediaVocalLevel %f with min %f, max %f and unit level %f"
+ "%s: Restarting the haptics engine."
+ "%s: Server handshake successful: %@"
+ "%s: Setting unit level to %f with mediaVocalLevel %f, min %f and max %f"
+ "%s: Successfully started the CHHapticEngine."
+ "%s: Timed out waiting to find device with identifier: %@ with %@"
+ "%s: Trying to play haptics but we haptic engine failed to create."
+ "%s: Trying to play haptics but we haptics engine is starting. Nothing will happen."
+ "%s: Trying to play haptics."
+ "%s: Unexpected state: %@"
+ "%s: Update reverb button for level %f"
+ "%s: Update vocal attenuation button for level %f"
+ "%s: failed to get endpoint route; cannot request mic"
+ "%s: failed to send display mode enable sdr %@ with error: %@"
+ "%s: failed to send vocal level %f with error: %@"
+ "%s: requested mic with result %@, error: %@"
+ "%s: sent display mode enable sdr %@"
+ "%s: sent vocal level %f"
+ "-[CSHapticsPlayer _onEngineReset]"
+ "-[CSHapticsPlayer _onEngineStopsWithReason:]"
+ "-[CSHapticsPlayer _playButtonFeedbackWithIntensity:andSharpness:]"
+ "-[CSHapticsPlayer _playButtonFeedbackWithIntensity:andSharpness:]_block_invoke"
+ "-[CSHapticsPlayer _setupHapticEngine]"
+ "-[CSHapticsPlayer _startHapticsEngineWithCompletion:]_block_invoke"
+ "-[CSHapticsPlayer playButtonFeedback]"
+ "-[CSHapticsPlayer playReverbButtonFeedbackWithIntensity:]"
+ "-[CSHapticsPlayer playVocalButtonFeedbackWithIntensity:]"
+ "-[CSLatencyCardViewController _cancel]"
+ "-[CSPlaybackManager controller:defersResponseReplacement:]_block_invoke"
+ "-[CSRemoteRequestClient _activateMessageClientIfNeeded:]_block_invoke_3"
+ "-[CSRemoteRequestClient _handleHandshakeResponse:error:]"
+ "-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke"
+ "-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:]_block_invoke_3"
+ "-[CSRemoteRequestClient retrieveDisplayMode:]_block_invoke"
+ "-[CSRemoteRequestClient sendDisplayMode:]_block_invoke"
+ "-[CSRemoteRequestClient sendVocalLevel:]_block_invoke"
+ "-[CSShieldConnectionManager _attemptReconnect]"
+ "-[CSShieldConnectionManager _handleServerConnectionError:]"
+ "-[CSShieldConnectionManager bootstrapFromRemoteDisplayConnection:]"
+ "-[CSShieldConnectionManager sceneDidBecomeActive]"
+ "-[CSShieldManager _invalidateRequestClient]"
+ "-[CSShieldManager requestMicrophoneActivationWithCompletion:]_block_invoke"
+ "-[CSShieldManager requestMicrophoneActivationWithCompletion:]_block_invoke_2"
+ "-[CSShieldViewController _presentEndpointDisconnectedError]"
+ "-[CSShieldViewController _presentEndpointDisconnectedError]_block_invoke"
+ "-[CSShieldViewController _presentEndpointDisconnectedError]_block_invoke_2"
+ "-[CSShieldViewController _presentVersionMismatchError:]_block_invoke"
+ "-[CSShieldViewController _updateReverbButtonForLevel:]"
+ "-[CSShieldViewController _updateVocalAttenuationButtonForLevel:]"
+ "<CSClient idsDeviceIdentifier:%@ sessionPairingIdentifier:%@ participantInfo:%@ protocolVersion:%f>"
+ "@\"<CHHapticPatternPlayer>\""
+ "@\"CHHapticEngine\""
+ "@\"CSHandshakeResponseMessage\""
+ "@\"CSHapticsPlayer\""
+ "@\"CSLatencyCardViewController\""
+ "@\"CSPaddingView\""
+ "@\"MSVBlockGuard\""
+ "@\"UIScrollView\""
+ "@48@0:8@16@24@?32@?40"
+ "@56@0:8@16@24d32@40q48"
+ "AUDIO_HELP_GAME_MODE_DESCRIPTION"
+ "AUDIO_HELP_GAME_MODE_NOTICE"
+ "AUDIO_HELP_GAME_MODE_TITLE"
+ "AUDIO_HELP_NAV_TITLE"
+ "AUDIO_HELP_SDR_DESCRIPTION"
+ "AUDIO_HELP_SDR_TITLE"
+ "AUDIO_HELP_SDR_TURN_OFF"
+ "AUDIO_HELP_SDR_TURN_ON"
+ "AUDIO_HELP_TITLE"
+ "CONNECTION_LOST_ERROR_ALERT_CANCEL_ACTION"
+ "CONNECTION_LOST_ERROR_ALERT_MESSAGE"
+ "CONNECTION_LOST_ERROR_ALERT_TITLE"
+ "CONNECTION_LOST_ERROR_ALERT_TRY_AGAIN"
+ "CSDisplayModeMessage"
+ "CSDisplayModeRequest"
+ "CSDisplayModeResponse"
+ "CSHandshakeResponseMessage"
+ "CSHapticsPlayer"
+ "CSHapticsPlayerStateFailed"
+ "CSHapticsPlayerStateIdle"
+ "CSHapticsPlayerStateRunning"
+ "CSHapticsPlayerStateStarting"
+ "CSHelpPanelViewController"
+ "CSPaddingView"
+ "CSRemoteRequestClientErrorCode"
+ "CSRemoteRequestClientErrorNotification"
+ "CSRemoteRequestServerErrorDomain"
+ "CSVocalMessage"
+ "ContinuitySing.CSShieldViewController.AddSongButton"
+ "ContinuitySing.CSShieldViewController.DisconnectButton"
+ "ContinuitySing.CSShieldViewController.MicControl"
+ "ContinuitySing.CSShieldViewController.View"
+ "ContinuitySingErrorCodeEndpointDisconnect"
+ "ContinuitySingErrorCodeHandshakeFailedGeneric"
+ "ContinuitySingErrorCodeHandshakeFailedTVOSTooOld"
+ "ContinuitySingSDR"
+ "ContinuitySingVocal"
+ "OSMajorVersionRequired"
+ "OSMinorVersionRequired"
+ "OSPatchVersionRequired"
+ "RequiredProtocolVersion"
+ "ShouldActivateMicrophone"
+ "T@\"<CHHapticPatternPlayer>\",&,N,V_player"
+ "T@\"CHHapticEngine\",&,N,V_engine"
+ "T@\"CSLatencyCardViewController\",&,N,V_latencyCardViewController"
+ "T@\"CSPaddingView\",&,N,V_divider"
+ "T@\"CSPaddingView\",&,N,V_gameModeNoticeLabel"
+ "T@\"CSPaddingView\",&,N,V_gameModeTitleLabel"
+ "T@\"CSPaddingView\",&,N,V_gameModelDescriptionLabel"
+ "T@\"CSPaddingView\",&,N,V_sdrDescriptionLabel"
+ "T@\"CSPaddingView\",&,N,V_sdrSwitchButtonDescription"
+ "T@\"CSPaddingView\",&,N,V_sdrTitleLabel"
+ "T@\"CSPaddingView\",&,N,V_titleLabel"
+ "T@\"NSArray\",R,N,V_idleStateConstraints"
+ "T@\"NSArray\",R,N,V_resultStateConstraints"
+ "T@\"UIActivityIndicatorView\",R,N,V_activityIndicatorView"
+ "T@\"UIButton\",&,N,V_sdrSwitchButton"
+ "T@\"UIButton\",R,N,V_actionButton"
+ "T@\"UILabel\",R,N,V_instructionDescriptionLabel"
+ "T@\"UILabel\",R,N,V_instructionTitleLabel"
+ "T@\"UILabel\",R,N,V_resultLabel"
+ "T@\"UIScrollView\",&,N,V_scrollView"
+ "T@\"UIStackView\",&,N,V_stackView"
+ "T@\"UIView\",&,N,V_wrappedView"
+ "TB,N,V_isSDREnabled"
+ "TB,N,V_supportsHaptics"
+ "TB,R,N,V_enableSDR"
+ "TB,R,N,V_shouldActivateMicrophone"
+ "TQ,N,V_state"
+ "TQ,R,N,V_cardState"
+ "TQ,R,N,V_errorState"
+ "TQ,R,N,V_latency"
+ "Td,N,V_bottomPadding"
+ "Td,N,V_leadingPadding"
+ "Td,N,V_nextInitialVelocityForAnimation"
+ "Td,N,V_topPadding"
+ "Td,N,V_trailingPadding"
+ "Td,R,N,V_minimumRequiredProtocolVersion"
+ "Td,R,N,V_vocalLevel"
+ "T{?=qqq},R,N,V_minimumRequiredOperatingSystemVersion"
+ "VERSION_MISMATCH_ERROR_ALERT_TITLE"
+ "VERSION_MISMATCH_ERROR_MESSAGE_UPDATE_IPHONE"
+ "VERSION_MISMATCH_ERROR_MESSAGE_UPDATE_TV"
+ "_actionButton"
+ "_activationGuard"
+ "_activityIndicatorView"
+ "_attemptReconnect"
+ "_bottomConstraint"
+ "_bottomPadding"
+ "_cancel"
+ "_cardState"
+ "_connectionCompletionHandler"
+ "_createViews"
+ "_divider"
+ "_enableSDR"
+ "_engine"
+ "_errorState"
+ "_finishLoading"
+ "_firstSceneDidBecomeActive"
+ "_gameModeNoticeLabel"
+ "_gameModeTitleLabel"
+ "_gameModelDescriptionLabel"
+ "_handleButtonAction"
+ "_handleDismiss"
+ "_handleHandshakeResponse:error:"
+ "_handleSDRSwitch"
+ "_handleServerConnectionError:"
+ "_hapticIntensityValueForIntensity:"
+ "_hapticsPlayer"
+ "_idleStateConstraints"
+ "_instructionDescriptionLabel"
+ "_instructionTitleLabel"
+ "_invalidateRequestClient"
+ "_isSDREnabled"
+ "_labelWithLocalizationKey:textStyle:weight:color:variant:"
+ "_latency"
+ "_latencyCardViewController"
+ "_latencyResultForCurrentState"
+ "_leadingConstraint"
+ "_leadingPadding"
+ "_minimumRequiredOperatingSystemVersion"
+ "_minimumRequiredProtocolVersion"
+ "_nextInitialVelocityForAnimation"
+ "_onEngineReset"
+ "_onEngineStopsWithReason:"
+ "_pendingActivationDeviceFoundHandler"
+ "_playButtonFeedbackWithIntensity:andSharpness:"
+ "_player"
+ "_presentEndpointDisconnectedError"
+ "_presentVersionMismatchError:"
+ "_resultLabel"
+ "_resultStateConstraints"
+ "_reverbHapticSharpnessValueForIntensity:"
+ "_scrollView"
+ "_sdrDescriptionLabel"
+ "_sdrSwitchButton"
+ "_sdrSwitchButtonDescription"
+ "_sdrTitleLabel"
+ "_serverHandshake"
+ "_setContinuousCornerRadius:"
+ "_setUpContentView"
+ "_setupActionButton"
+ "_setupConstraints"
+ "_setupHapticEngine"
+ "_setupStackView"
+ "_shouldActivateMicrophone"
+ "_stackView"
+ "_startHapticsEngineWithCompletion:"
+ "_state"
+ "_supportsHaptics"
+ "_topConstraint"
+ "_topPadding"
+ "_trailingConstraint"
+ "_trailingPadding"
+ "_updateConstraints"
+ "_updateSDRButtonTitle"
+ "_updateViewFromCurrentState"
+ "_updateViewFromCurrentStateAnimated:"
+ "_vocalLevel"
+ "_wrappedView"
+ "actionButton"
+ "activityIndicatorView"
+ "animateWithSpringDuration:bounce:initialSpringVelocity:delay:options:animations:completion:"
+ "bootstrapFromRemoteDisplayConnection:"
+ "borderedButtonConfiguration"
+ "bottomPadding"
+ "capabilitiesForHardware"
+ "cardState"
+ "code"
+ "com.apple.ContinuitySing.displayModeEvent"
+ "com.apple.ContinuitySing.displayModeRequest"
+ "com.apple.ContinuitySing.displayModeResponse"
+ "com.apple.ContinuitySing.handshakeResponse"
+ "com.apple.ContinuitySing.vocal"
+ "constraintGreaterThanOrEqualToAnchor:"
+ "constraintGreaterThanOrEqualToConstant:"
+ "constraintLessThanOrEqualToAnchor:"
+ "constraintLessThanOrEqualToAnchor:constant:"
+ "contentLayoutGuide"
+ "createPlayerWithPattern:error:"
+ "deactivateConstraints:"
+ "disarm"
+ "divider"
+ "domain"
+ "enableSDR"
+ "engine"
+ "errorState"
+ "f24@0:8Q16"
+ "gameModeNoticeLabel"
+ "gameModeTitleLabel"
+ "gameModelDescriptionLabel"
+ "idleStateConstraints"
+ "initWithAudioSession:sessionIsShared:options:error:"
+ "initWithEnableSDR:"
+ "initWithEventType:parameters:relativeTime:duration:"
+ "initWithEvents:parameters:error:"
+ "initWithHandshake:"
+ "initWithImage:style:target:action:"
+ "initWithMicrophoneActivation:"
+ "initWithParameterID:value:"
+ "initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:connectionCompletionHandler:"
+ "initWithRootViewController:"
+ "initWithTimeout:interruptionHandler:"
+ "initWithVocalLevel:"
+ "initWithWrappedView:"
+ "instructionDescriptionLabel"
+ "instructionTitleLabel"
+ "isSDREnabled"
+ "latency"
+ "latencyCardViewController"
+ "leadingPadding"
+ "minimumRequiredOperatingSystemVersion"
+ "minimumRequiredProtocolVersion"
+ "navigationItem"
+ "nextInitialVelocityForAnimation"
+ "notifyWhenPlayersFinished:"
+ "playButtonFeedback"
+ "playReverbButtonFeedbackWithIntensity:"
+ "playVocalButtonFeedbackWithIntensity:"
+ "player"
+ "q16@?0@\"NSError\"8"
+ "quaternarySystemFillColor"
+ "requestMicrophoneActivationWithCompletion:"
+ "resultLabel"
+ "resultStateConstraints"
+ "retrieveDisplayMode:"
+ "sceneDidBecomeActive"
+ "scrollView"
+ "sdrDescriptionLabel"
+ "sdrSwitchButton"
+ "sdrSwitchButtonDescription"
+ "sdrTitleLabel"
+ "sendDisplayMode:"
+ "sendVocalLevel:"
+ "separatorColor"
+ "setAccessibilityIdentifier:"
+ "setBottomPadding:"
+ "setCustomSpacing:afterView:"
+ "setDivider:"
+ "setEngine:"
+ "setGameModeNoticeLabel:"
+ "setGameModeTitleLabel:"
+ "setGameModelDescriptionLabel:"
+ "setHorizontalPadding:"
+ "setIsSDREnabled:"
+ "setLatencyCardViewController:"
+ "setLayoutMargins:"
+ "setLayoutMarginsRelativeArrangement:"
+ "setLeadingPadding:"
+ "setMuteHapticsWhileRecordingAudio:"
+ "setNextInitialVelocityForAnimation:"
+ "setPlayer:"
+ "setPlaysHapticsOnly:"
+ "setPrefersGrabberVisible:"
+ "setPriority:"
+ "setResetHandler:"
+ "setRightBarButtonItem:"
+ "setScrollView:"
+ "setSdrDescriptionLabel:"
+ "setSdrSwitchButton:"
+ "setSdrSwitchButtonDescription:"
+ "setSdrTitleLabel:"
+ "setStackView:"
+ "setStoppedHandler:"
+ "setSupportsHaptics:"
+ "setSymbolConfiguration:"
+ "setTitle:forState:"
+ "setTitleLabel:"
+ "setTopPadding:"
+ "setTrailingPadding:"
+ "setUserInterfaceStyle:"
+ "setVerticalPadding:"
+ "setWrappedView:"
+ "sheetPresentationController"
+ "shouldActivateMicrophone"
+ "stackView"
+ "startAtTime:error:"
+ "startWithCompletionHandler:"
+ "stopAnimating"
+ "supportsHaptics"
+ "titleLabel"
+ "topPadding"
+ "trailingPadding"
+ "traitOverrides"
+ "v20@?0B8@\"NSError\"12"
+ "v24@0:8f16f20"
+ "v24@?0@\"CSDisplayModeResponse\"8@\"NSError\"16"
+ "v24@?0@\"CSHandshakeResponseMessage\"8@\"NSError\"16"
+ "vocalLevel"
+ "wrappedView"
- "%s: %@ failed to get endpoint route; cannot request mic"
- "%s: %@ requested mic with result %@, error: %@"
- "%s: Failed to decode CSHandshakeMessage with message: %@"
- "%s: Failed to find device with identifier: %@"
- "%s: Setting vocal attenuation level to %f"
- "%s: sent continuity sing session handshake %@"
- "-[CSHandshakeMessage initWithMessage:]"
- "-[CSLatencyCardViewController _cancelAndDismiss]"
- "-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:]_block_invoke"
- "-[CSRemoteRequestClient initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:]_block_invoke_2"
- "-[CSShieldViewController _sendConnectMicRequest]_block_invoke"
- "-[CSShieldViewController _sendConnectMicRequest]_block_invoke_2"
- "<CSClient deviceIdentifier:%@ idsDeviceIdentifier:%@ sessionPairingIdentifier:%@ participantInfo:%@ protocolVersion:%f>"
- "@\"PRXAction\""
- "@\"PRXLabel\""
- "@40@0:8@16@24@?32"
- "MEASUREMENT_DONE"
- "T@\"NSLayoutConstraint\",R,N,V_imageViewWidthConstraint"
- "T@\"NSString\",R,C,N,V_deviceIdentifier"
- "T@\"PRXAction\",R,N,V_cancelAction"
- "T@\"PRXAction\",R,N,V_doneAction"
- "T@\"PRXAction\",R,N,V_retryAction"
- "T@\"PRXAction\",R,N,V_startAction"
- "T@\"PRXLabel\",R,N,V_instructionsLabel"
- "_actionsForProgressEvent:"
- "_cancelAction"
- "_deviceIdentifier"
- "_doneAction"
- "_imageViewWidthConstraint"
- "_instructionsLabel"
- "_retryAction"
- "_setupPRXActions"
- "_startAction"
- "actions"
- "cancelAction"
- "deviceIdentifier"
- "doneAction"
- "groupSessionIdentifier"
- "hideActivityIndicator"
- "imageViewWidthConstraint"
- "initWithCompanionLinkDevice:handshake:"
- "initWithRemoteDisplayIdentifier:participantInfo:disconnectHandler:"
- "instructionsLabel"
- "removeAction:"
- "retryAction"
- "setBodyLabel:"
- "setImageViews:"
- "size"
- "startAction"

```
