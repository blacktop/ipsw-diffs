## ContinuitySing

> `/System/Library/PrivateFrameworks/ContinuitySing.framework/ContinuitySing`

```diff

-659.0.0.0.4
-  __TEXT.__text: 0x405b8
-  __TEXT.__auth_stubs: 0x1420
-  __TEXT.__objc_methlist: 0x28c4
-  __TEXT.__const: 0x944
-  __TEXT.__gcc_except_tab: 0x98c
-  __TEXT.__cstring: 0x4859
-  __TEXT.__oslogstring: 0x2529
+661.0.0.0.3
+  __TEXT.__text: 0x4db70
+  __TEXT.__auth_stubs: 0x1660
+  __TEXT.__objc_methlist: 0x2fc4
+  __TEXT.__const: 0xb44
+  __TEXT.__gcc_except_tab: 0xaa8
+  __TEXT.__cstring: 0x4f19
+  __TEXT.__oslogstring: 0x26f9
   __TEXT.__ustring: 0x2a
-  __TEXT.__swift5_typeref: 0x768
-  __TEXT.__swift5_capture: 0x270
-  __TEXT.__constg_swiftt: 0x514
-  __TEXT.__swift5_reflstr: 0x22a
-  __TEXT.__swift5_fieldmd: 0x288
+  __TEXT.__swift5_typeref: 0x87c
+  __TEXT.__swift5_fieldmd: 0x30c
+  __TEXT.__constg_swiftt: 0x660
+  __TEXT.__swift5_reflstr: 0x26a
+  __TEXT.__swift5_capture: 0x300
+  __TEXT.__swift5_protos: 0x8
+  __TEXT.__swift5_proto: 0x4c
+  __TEXT.__swift5_types: 0x3c
+  __TEXT.__swift_as_entry: 0x78
+  __TEXT.__swift_as_ret: 0x84
   __TEXT.__swift5_assocty: 0x78
-  __TEXT.__swift5_proto: 0x30
-  __TEXT.__swift5_types: 0x34
-  __TEXT.__swift_as_entry: 0x30
-  __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x11b8
-  __TEXT.__eh_frame: 0x848
-  __TEXT.__objc_classname: 0x646
-  __TEXT.__objc_methname: 0x7b79
-  __TEXT.__objc_methtype: 0x107f
-  __TEXT.__objc_stubs: 0x6160
-  __DATA_CONST.__got: 0x7d8
-  __DATA_CONST.__const: 0x11f0
-  __DATA_CONST.__objc_classlist: 0x220
-  __DATA_CONST.__objc_protolist: 0x78
+  __TEXT.__unwind_info: 0x1578
+  __TEXT.__eh_frame: 0xe08
+  __TEXT.__objc_classname: 0x76d
+  __TEXT.__objc_methname: 0x8a7e
+  __TEXT.__objc_methtype: 0x124e
+  __TEXT.__objc_stubs: 0x6c80
+  __DATA_CONST.__got: 0x878
+  __DATA_CONST.__const: 0x13b8
+  __DATA_CONST.__objc_classlist: 0x288
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2118
+  __DATA_CONST.__objc_selrefs: 0x24e0
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x1c8
-  __AUTH_CONST.__auth_got: 0xa20
-  __AUTH_CONST.__const: 0xfa0
-  __AUTH_CONST.__cfstring: 0x1920
-  __AUTH_CONST.__objc_const: 0x5550
+  __DATA_CONST.__objc_superrefs: 0x240
+  __AUTH_CONST.__auth_got: 0xb40
+  __AUTH_CONST.__const: 0x10d8
+  __AUTH_CONST.__cfstring: 0x1cc0
+  __AUTH_CONST.__objc_const: 0x65e0
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH.__objc_data: 0x1900
-  __AUTH.__data: 0x370
-  __DATA.__objc_ivar: 0x360
-  __DATA.__data: 0x7f8
-  __DATA.__bss: 0x6e8
+  __AUTH.__objc_data: 0x1cc0
+  __AUTH.__data: 0x568
+  __DATA.__objc_ivar: 0x3ec
+  __DATA.__data: 0x8a0
+  __DATA.__bss: 0x848
   __DATA.__common: 0x68
+  - /System/Library/Frameworks/AVKit.framework/AVKit
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 93A07CF0-781F-39AE-A3D6-E13A97BCA88A
-  Functions: 1382
-  Symbols:   4345
-  CStrings:  2525
+  UUID: 67FA4375-254A-318E-A39E-0BBD6953D3EA
+  Functions: 1628
+  Symbols:   4939
+  CStrings:  2819
 
Symbols:
+ +[CSAttributionRequestMessage messageID]
+ +[CSAttributionRequestMessage requiredParameters]
+ +[CSAttributionRequestMessage responseMessageFromDictionary:]
+ +[CSAttributionResponseMessage messageID]
+ +[CSAttributionResponseMessage requiredParameters]
+ +[CSAvatarRequestMessage messageID]
+ +[CSAvatarRequestMessage requiredParameters]
+ +[CSAvatarRequestMessage responseMessageFromDictionary:]
+ +[CSAvatarResponseMessage messageID]
+ +[CSAvatarResponseMessage requiredParameters]
+ +[CSQueueAttributionManager sharedManager]
+ +[CSQueueAttributionManager sharedManager].cold.1
+ -[CSAttributionRequestMessage .cxx_destruct]
+ -[CSAttributionRequestMessage dictionaryRepresentation]
+ -[CSAttributionRequestMessage initWithMessage:]
+ -[CSAttributionRequestMessage initWithQueueIdentifiers:]
+ -[CSAttributionRequestMessage queueIdentifiersToAttribute]
+ -[CSAttributionResponseMessage .cxx_destruct]
+ -[CSAttributionResponseMessage dictionaryRepresentation]
+ -[CSAttributionResponseMessage initWithAttributions:]
+ -[CSAttributionResponseMessage initWithMessage:]
+ -[CSAttributionResponseMessage queueIdentifierAttributionMap]
+ -[CSAvatarRequestMessage .cxx_destruct]
+ -[CSAvatarRequestMessage dictionaryRepresentation]
+ -[CSAvatarRequestMessage initWithMessage:]
+ -[CSAvatarRequestMessage initWithSocialProfileIdentifier:]
+ -[CSAvatarRequestMessage socialProfileIdentifier]
+ -[CSAvatarResponseMessage .cxx_destruct]
+ -[CSAvatarResponseMessage avatar]
+ -[CSAvatarResponseMessage dictionaryRepresentation]
+ -[CSAvatarResponseMessage initWithAvatar:]
+ -[CSAvatarResponseMessage initWithMessage:]
+ -[CSMicControlSymbolView .cxx_destruct]
+ -[CSMicControlSymbolView _micImageForState:]
+ -[CSMicControlSymbolView glowView]
+ -[CSMicControlSymbolView imageView]
+ -[CSMicControlSymbolView init]
+ -[CSMicControlSymbolView layoutSubviews]
+ -[CSMicControlSymbolView offImage]
+ -[CSMicControlSymbolView onImage]
+ -[CSMicControlSymbolView setGlowView:]
+ -[CSMicControlSymbolView setImageView:]
+ -[CSMicControlSymbolView setOffImage:]
+ -[CSMicControlSymbolView setOnImage:]
+ -[CSMicControlSymbolView updateForState:]
+ -[CSMiniPlayerControlButton initWithSymbolName:withFont:scale:]
+ -[CSMiniPlayerControlButton layoutSubviews]
+ -[CSMiniPlayerControlButton replaceSymbol:withFont:scale:]
+ -[CSPlaybackManager _stringFromSeconds:]
+ -[CSPlaybackManager currentValueText]
+ -[CSPlaybackManager currentValue]
+ -[CSPlaybackManager isLoading]
+ -[CSPlaybackManager isPlaying]
+ -[CSPlaybackManager maxValueText]
+ -[CSPlaybackManager maxValue]
+ -[CSPlaybackManager minValue]
+ -[CSPlaybackManager timeRangeMarks]
+ -[CSPlaybackManager tracklist]
+ -[CSPlayerResponseItemWrapper .cxx_destruct]
+ -[CSPlayerResponseItemWrapper hash]
+ -[CSPlayerResponseItemWrapper initWithResponseItem:]
+ -[CSPlayerResponseItemWrapper isEqual:]
+ -[CSPlayerResponseItemWrapper responseItem]
+ -[CSQueueAttributionManager .cxx_destruct]
+ -[CSQueueAttributionManager init]
+ -[CSQueueAttributionManager retrieveAttributionsForQueueIdentifiers:withResultHandler:]
+ -[CSQueueAttributionManager retrieveAvatarForParticipant:withResultHandler:]
+ -[CSQueueCell .cxx_destruct]
+ -[CSQueueCell albumArtImageView]
+ -[CSQueueCell content]
+ -[CSQueueCell initWithStyle:reuseIdentifier:]
+ -[CSQueueCell isNowPlaying]
+ -[CSQueueCell participantBadgeView]
+ -[CSQueueCell participantInfo]
+ -[CSQueueCell prepareForReuse]
+ -[CSQueueCell setContent:]
+ -[CSQueueCell setIsNowPlaying:]
+ -[CSQueueCell setParticipantInfo:]
+ -[CSQueueCell setupAlbumArtImageView]
+ -[CSQueueCell setupArtistLabel]
+ -[CSQueueCell setupConstraints]
+ -[CSQueueCell setupLabelsStackView]
+ -[CSQueueCell setupParticipantBadgeView]
+ -[CSQueueCell setupTitleLabel]
+ -[CSQueueCell setupViews]
+ -[CSQueueCell updateContent]
+ -[CSQueueCell updateFonts]
+ -[CSQueuePlaybackControlsView .cxx_destruct]
+ -[CSQueuePlaybackControlsView _localizedAddSongString]
+ -[CSQueuePlaybackControlsView _localizedAddSongString].cold.1
+ -[CSQueuePlaybackControlsView _symbolFont]
+ -[CSQueuePlaybackControlsView initWithPlayAction:backAction:forwardAction:addSongAction:]
+ -[CSQueuePlaybackControlsView playbackManager:didUpdateState:]
+ -[CSQueuePlaybackControlsView setupAddSongButtonWithAction:]
+ -[CSQueuePlaybackControlsView setupConstraints]
+ -[CSQueuePlaybackControlsView setupPlaybackControlButtonsWithPlayAction:backAction:forwardAction:]
+ -[CSQueuePlaybackControlsView setupTimelineControl]
+ -[CSQueuePlaybackControlsView setupViewsWithPlayAction:backAction:forwardAction:addSongAction:]
+ -[CSQueuePlaybackControlsView updatePlayPauseButtonWithState:]
+ -[CSQueueSectionHeader .cxx_destruct]
+ -[CSQueueSectionHeader dealloc]
+ -[CSQueueSectionHeader initWithCoder:]
+ -[CSQueueSectionHeader init]
+ -[CSQueueSectionHeader setupConstraints]
+ -[CSQueueSectionHeader setupPlayingNextLabel]
+ -[CSQueueSectionHeader setupSingersLabel]
+ -[CSQueueSectionHeader setupViews]
+ -[CSQueueSectionHeader shieldManager:didUpdateSessionState:]
+ -[CSQueueSectionHeader updateSingersText]
+ -[CSQueueViewController .cxx_destruct]
+ -[CSQueueViewController _canShowWhileLocked]
+ -[CSQueueViewController _onAddSongPressed]
+ -[CSQueueViewController _onBackwardPressed]
+ -[CSQueueViewController _onForwardPressed]
+ -[CSQueueViewController _onPlayPausePressed]
+ -[CSQueueViewController initWithAddSongHandler:]
+ -[CSQueueViewController initWithCoder:]
+ -[CSQueueViewController playbackManager:didUpdateTracklist:]
+ -[CSQueueViewController setupPlayerControlsView]
+ -[CSQueueViewController tableView:heightForHeaderInSection:]
+ -[CSQueueViewController tableView:heightForRowAtIndexPath:]
+ -[CSQueueViewController tableView:viewForHeaderInSection:]
+ -[CSQueueViewController updateDataSource]
+ -[CSQueueViewController viewDidLayoutSubviews]
+ -[CSQueueViewController viewDidLoad]
+ -[CSQueuedTrack description]
+ -[CSRemoteRequestClient retrieveAttributionsForQueueIdentifiers:handler:]
+ -[CSRemoteRequestClient retrieveAvatarForParticipant:handler:]
+ -[CSReverbMessage initWithReverbLevel:]
+ -[CSReverbMessage reverbLevel]
+ -[CSReverbResponse initWithReverbLevel:]
+ -[CSReverbResponse reverbLevel]
+ -[CSSessionStateUpdate participants]
+ -[CSShieldManager _requestInitialSessionStateWithCompletion:]
+ -[CSShieldViewController handleOpenQueueTap:]
+ -[CSSingSessionState initWithMicVolume:reverbLevel:activeMicRemoteDisplayID:participants:]
+ -[CSSingSessionState participants]
+ GCC_except_table131
+ GCC_except_table137
+ GCC_except_table15
+ GCC_except_table56
+ GCC_except_table69
+ GCC_except_table85
+ GCC_except_table91
+ GCC_except_table94
+ _CFDictionaryGetTypeID
+ _CGPathCreateWithEllipseInRect
+ _CGPathRelease
+ _CGRectGetMinX
+ _CGRectGetMinY
+ _CGRectInset
+ _CGSizeZero
+ _MPModelPropertySongHasVideo
+ _NSStringFromCSReverbLevel
+ _OBJC_CLASS_$_AVMediaTimelineControl
+ _OBJC_CLASS_$_AVMediaTimelineControlLabelsConfiguration
+ _OBJC_CLASS_$_CSAttributionRequestMessage
+ _OBJC_CLASS_$_CSAttributionResponseMessage
+ _OBJC_CLASS_$_CSAvatarRequestMessage
+ _OBJC_CLASS_$_CSAvatarResponseMessage
+ _OBJC_CLASS_$_CSMicControlSymbolView
+ _OBJC_CLASS_$_CSPlayerResponseItemWrapper
+ _OBJC_CLASS_$_CSQueueAttributionManager
+ _OBJC_CLASS_$_CSQueueCell
+ _OBJC_CLASS_$_CSQueuePlaybackControlsView
+ _OBJC_CLASS_$_CSQueueSectionHeader
+ _OBJC_CLASS_$_CSQueueViewController
+ _OBJC_CLASS_$_NSBlockOperation
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDateComponents
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSDiffableDataSourceSnapshot
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_UITableViewCell
+ _OBJC_CLASS_$_UITableViewController
+ _OBJC_CLASS_$_UITableViewDiffableDataSource
+ _OBJC_CLASS_$__UIGrabber
+ _OBJC_IVAR_$_CSAttributionRequestMessage._queueIdentifiersToAttribute
+ _OBJC_IVAR_$_CSAttributionResponseMessage._queueIdentifierAttributionMap
+ _OBJC_IVAR_$_CSAvatarRequestMessage._socialProfileIdentifier
+ _OBJC_IVAR_$_CSAvatarResponseMessage._avatar
+ _OBJC_IVAR_$_CSMicControlSymbolView._glowView
+ _OBJC_IVAR_$_CSMicControlSymbolView._imageView
+ _OBJC_IVAR_$_CSMicControlSymbolView._offImage
+ _OBJC_IVAR_$_CSMicControlSymbolView._onImage
+ _OBJC_IVAR_$_CSPlaybackManager._currentResponse
+ _OBJC_IVAR_$_CSPlaybackManager._responseDate
+ _OBJC_IVAR_$_CSPlayerResponseItemWrapper._responseItem
+ _OBJC_IVAR_$_CSQueueAttributionManager._attributions
+ _OBJC_IVAR_$_CSQueueAttributionManager._avatars
+ _OBJC_IVAR_$_CSQueueAttributionManager._pendingAvatarHandlers
+ _OBJC_IVAR_$_CSQueueAttributionManager._requestedAttributions
+ _OBJC_IVAR_$_CSQueueCell._albumArtImageView
+ _OBJC_IVAR_$_CSQueueCell._artistLabel
+ _OBJC_IVAR_$_CSQueueCell._content
+ _OBJC_IVAR_$_CSQueueCell._isNowPlaying
+ _OBJC_IVAR_$_CSQueueCell._labelsStackView
+ _OBJC_IVAR_$_CSQueueCell._labelsStackViewYPositionConstraint
+ _OBJC_IVAR_$_CSQueueCell._participantBadgeView
+ _OBJC_IVAR_$_CSQueueCell._participantInfo
+ _OBJC_IVAR_$_CSQueueCell._titleLabel
+ _OBJC_IVAR_$_CSQueuePlaybackControlsView._addSongButton
+ _OBJC_IVAR_$_CSQueuePlaybackControlsView._goBackButton
+ _OBJC_IVAR_$_CSQueuePlaybackControlsView._goForwardButton
+ _OBJC_IVAR_$_CSQueuePlaybackControlsView._playPauseButton
+ _OBJC_IVAR_$_CSQueuePlaybackControlsView._timelineControl
+ _OBJC_IVAR_$_CSQueueSectionHeader._playingNextLabel
+ _OBJC_IVAR_$_CSQueueSectionHeader._singersLabel
+ _OBJC_IVAR_$_CSQueueViewController._addSongHandler
+ _OBJC_IVAR_$_CSQueueViewController._attributions
+ _OBJC_IVAR_$_CSQueueViewController._dataSource
+ _OBJC_IVAR_$_CSQueueViewController._grabberView
+ _OBJC_IVAR_$_CSQueueViewController._itemsPendingAttribution
+ _OBJC_IVAR_$_CSQueueViewController._playerControlsView
+ _OBJC_IVAR_$_CSReverbMessage._reverbLevel
+ _OBJC_IVAR_$_CSReverbResponse._reverbLevel
+ _OBJC_IVAR_$_CSSessionStateUpdate._participants
+ _OBJC_IVAR_$_CSSingSessionState._participants
+ _OBJC_METACLASS_$_CSAttributionRequestMessage
+ _OBJC_METACLASS_$_CSAttributionResponseMessage
+ _OBJC_METACLASS_$_CSAvatarRequestMessage
+ _OBJC_METACLASS_$_CSAvatarResponseMessage
+ _OBJC_METACLASS_$_CSMicControlSymbolView
+ _OBJC_METACLASS_$_CSPlayerResponseItemWrapper
+ _OBJC_METACLASS_$_CSQueueAttributionManager
+ _OBJC_METACLASS_$_CSQueueCell
+ _OBJC_METACLASS_$_CSQueuePlaybackControlsView
+ _OBJC_METACLASS_$_CSQueueSectionHeader
+ _OBJC_METACLASS_$_CSQueueViewController
+ _OBJC_METACLASS_$_UITableViewCell
+ _OBJC_METACLASS_$_UITableViewController
+ _ReverbLevelFromReverbValue
+ _ReverbValueFromReverbLevel
+ _UIContentSizeCategoryMedium
+ _UIFontWeightMedium
+ _UIImagePNGRepresentation
+ _UITableViewAutomaticDimension
+ _WiFiCopyCurrentNetworkInfoEx
+ __DATA__TtC14ContinuitySingP33_0966ECFEC73A60E9F4456608686DCC0E17ArtworkDownloader
+ __DATA__TtC14ContinuitySingP33_0966ECFEC73A60E9F4456608686DCC0E24ArtworkDownloaderManager
+ __IVARS__TtC14ContinuitySingP33_0966ECFEC73A60E9F4456608686DCC0E17ArtworkDownloader
+ __IVARS__TtC14ContinuitySingP33_0966ECFEC73A60E9F4456608686DCC0E24ArtworkDownloaderManager
+ __METACLASS_DATA__TtC14ContinuitySingP33_0966ECFEC73A60E9F4456608686DCC0E17ArtworkDownloader
+ __METACLASS_DATA__TtC14ContinuitySingP33_0966ECFEC73A60E9F4456608686DCC0E24ArtworkDownloaderManager
+ __OBJC_$_CLASS_METHODS_CSAttributionRequestMessage
+ __OBJC_$_CLASS_METHODS_CSAttributionResponseMessage
+ __OBJC_$_CLASS_METHODS_CSAvatarRequestMessage
+ __OBJC_$_CLASS_METHODS_CSAvatarResponseMessage
+ __OBJC_$_CLASS_METHODS_CSQueueAttributionManager
+ __OBJC_$_INSTANCE_METHODS_CSAttributionRequestMessage
+ __OBJC_$_INSTANCE_METHODS_CSAttributionResponseMessage
+ __OBJC_$_INSTANCE_METHODS_CSAvatarRequestMessage
+ __OBJC_$_INSTANCE_METHODS_CSAvatarResponseMessage
+ __OBJC_$_INSTANCE_METHODS_CSMicControlSymbolView
+ __OBJC_$_INSTANCE_METHODS_CSPlayerResponseItemWrapper
+ __OBJC_$_INSTANCE_METHODS_CSQueueAttributionManager
+ __OBJC_$_INSTANCE_METHODS_CSQueueCell(ContinuitySing)
+ __OBJC_$_INSTANCE_METHODS_CSQueuePlaybackControlsView
+ __OBJC_$_INSTANCE_METHODS_CSQueueSectionHeader
+ __OBJC_$_INSTANCE_METHODS_CSQueueViewController
+ __OBJC_$_INSTANCE_VARIABLES_CSAttributionRequestMessage
+ __OBJC_$_INSTANCE_VARIABLES_CSAttributionResponseMessage
+ __OBJC_$_INSTANCE_VARIABLES_CSAvatarRequestMessage
+ __OBJC_$_INSTANCE_VARIABLES_CSAvatarResponseMessage
+ __OBJC_$_INSTANCE_VARIABLES_CSMicControlSymbolView
+ __OBJC_$_INSTANCE_VARIABLES_CSPlayerResponseItemWrapper
+ __OBJC_$_INSTANCE_VARIABLES_CSQueueAttributionManager
+ __OBJC_$_INSTANCE_VARIABLES_CSQueueCell
+ __OBJC_$_INSTANCE_VARIABLES_CSQueuePlaybackControlsView
+ __OBJC_$_INSTANCE_VARIABLES_CSQueueSectionHeader
+ __OBJC_$_INSTANCE_VARIABLES_CSQueueViewController
+ __OBJC_$_PROP_LIST_AVMediaTimelineControlSource
+ __OBJC_$_PROP_LIST_CSAttributionRequestMessage
+ __OBJC_$_PROP_LIST_CSAttributionResponseMessage
+ __OBJC_$_PROP_LIST_CSAvatarRequestMessage
+ __OBJC_$_PROP_LIST_CSAvatarResponseMessage
+ __OBJC_$_PROP_LIST_CSMicControlSymbolView
+ __OBJC_$_PROP_LIST_CSPlayerResponseItemWrapper
+ __OBJC_$_PROP_LIST_CSQueueCell
+ __OBJC_$_PROP_LIST_CSQueuePlaybackControlsView
+ __OBJC_$_PROP_LIST_CSQueueSectionHeader
+ __OBJC_$_PROP_LIST_CSQueueViewController
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AVMediaTimelineControlSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CSPlaybackManagerObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AVMediaTimelineControlSource
+ __OBJC_$_PROTOCOL_REFS_AVMediaTimelineControlSource
+ __OBJC_CLASS_PROTOCOLS_$_CSQueuePlaybackControlsView
+ __OBJC_CLASS_PROTOCOLS_$_CSQueueSectionHeader
+ __OBJC_CLASS_PROTOCOLS_$_CSQueueViewController
+ __OBJC_CLASS_RO_$_CSAttributionRequestMessage
+ __OBJC_CLASS_RO_$_CSAttributionResponseMessage
+ __OBJC_CLASS_RO_$_CSAvatarRequestMessage
+ __OBJC_CLASS_RO_$_CSAvatarResponseMessage
+ __OBJC_CLASS_RO_$_CSMicControlSymbolView
+ __OBJC_CLASS_RO_$_CSPlayerResponseItemWrapper
+ __OBJC_CLASS_RO_$_CSQueueAttributionManager
+ __OBJC_CLASS_RO_$_CSQueueCell
+ __OBJC_CLASS_RO_$_CSQueuePlaybackControlsView
+ __OBJC_CLASS_RO_$_CSQueueSectionHeader
+ __OBJC_CLASS_RO_$_CSQueueViewController
+ __OBJC_LABEL_PROTOCOL_$_AVMediaTimelineControlSource
+ __OBJC_METACLASS_RO_$_CSAttributionRequestMessage
+ __OBJC_METACLASS_RO_$_CSAttributionResponseMessage
+ __OBJC_METACLASS_RO_$_CSAvatarRequestMessage
+ __OBJC_METACLASS_RO_$_CSAvatarResponseMessage
+ __OBJC_METACLASS_RO_$_CSMicControlSymbolView
+ __OBJC_METACLASS_RO_$_CSPlayerResponseItemWrapper
+ __OBJC_METACLASS_RO_$_CSQueueAttributionManager
+ __OBJC_METACLASS_RO_$_CSQueueCell
+ __OBJC_METACLASS_RO_$_CSQueuePlaybackControlsView
+ __OBJC_METACLASS_RO_$_CSQueueSectionHeader
+ __OBJC_METACLASS_RO_$_CSQueueViewController
+ __OBJC_PROTOCOL_$_AVMediaTimelineControlSource
+ ___34-[CSQueueCell setParticipantInfo:]_block_invoke
+ ___34-[CSQueueCell setParticipantInfo:]_block_invoke_2
+ ___36-[CSQueueViewController viewDidLoad]_block_invoke
+ ___41-[CSQueueViewController updateDataSource]_block_invoke
+ ___41-[CSQueueViewController updateDataSource]_block_invoke_2
+ ___41-[CSQueueViewController updateDataSource]_block_invoke_3
+ ___42+[CSQueueAttributionManager sharedManager]_block_invoke
+ ___42-[CSShieldViewController _showMusicUpsell]_block_invoke.224
+ ___44-[CSShieldViewController presentMusicPicker]_block_invoke.132
+ ___45-[CSShieldViewController handleOpenQueueTap:]_block_invoke
+ ___46-[CSShieldViewController _presentPairingError]_block_invoke.197
+ ___48-[CSAttributionResponseMessage initWithMessage:]_block_invoke
+ ___48-[CSQueueViewController setupPlayerControlsView]_block_invoke
+ ___48-[CSQueueViewController setupPlayerControlsView]_block_invoke_2
+ ___48-[CSQueueViewController setupPlayerControlsView]_block_invoke_3
+ ___48-[CSQueueViewController setupPlayerControlsView]_block_invoke_4
+ ___50-[CSShieldViewController _tryBootstrapAgainAction]_block_invoke.265
+ ___50-[CSShieldViewController _tryBootstrapAgainAction]_block_invoke.266
+ ___53-[CSShieldConnectionManager _requestGroupSessionURL:]_block_invoke.34
+ ___55-[CSShieldViewController _presentVersionMismatchError:]_block_invoke.208
+ ___56-[CSAttributionResponseMessage dictionaryRepresentation]_block_invoke
+ ___57-[CSShieldConnectionManager _bootstrapFromSingQRCodeURL:]_block_invoke.29
+ ___57-[CSShieldViewController _handleInvalidMusicAccountError]_block_invoke.234
+ ___57-[CSShieldViewController _handleInvalidMusicAccountError]_block_invoke.234.cold.1
+ ___57-[CSShieldViewController _handleInvalidMusicAccountError]_block_invoke.240
+ ___57-[CSShieldViewController _handleInvalidMusicAccountError]_block_invoke.240.cold.1
+ ___57-[CSShieldViewController _handleInvalidMusicAccountError]_block_invoke.241
+ ___57-[CSShieldViewController _handleMusicProfileUpdateNeeded]_block_invoke.250
+ ___57-[CSShieldViewController _handleMusicProfileUpdateNeeded]_block_invoke.250.cold.1
+ ___57-[CSShieldViewController _handleMusicProfileUpdateNeeded]_block_invoke.251
+ ___59-[CSShieldViewController _presentEndpointDisconnectedError]_block_invoke.261
+ ___61-[CSShieldManager _requestInitialSessionStateWithCompletion:]_block_invoke
+ ___61-[CSShieldManager _requestInitialSessionStateWithCompletion:]_block_invoke_2
+ ___61-[CSShieldManager _requestInitialSessionStateWithCompletion:]_block_invoke_2.cold.1
+ ___62-[CSRemoteRequestClient retrieveAvatarForParticipant:handler:]_block_invoke
+ ___62-[CSRemoteRequestClient retrieveAvatarForParticipant:handler:]_block_invoke.cold.1
+ ___62-[CSShieldManager _bootstrapRequestClientIfNeededAndAvailable]_block_invoke_7
+ ___62-[CSShieldViewController consumeSinglePressDownForButtonKind:]_block_invoke.139
+ ___62-[CSShieldViewController consumeSinglePressDownForButtonKind:]_block_invoke_2.142
+ ___62-[CSShieldViewController consumeSinglePressDownForButtonKind:]_block_invoke_2.142.cold.1
+ ___73-[CSRemoteRequestClient retrieveAttributionsForQueueIdentifiers:handler:]_block_invoke
+ ___73-[CSRemoteRequestClient retrieveAttributionsForQueueIdentifiers:handler:]_block_invoke.cold.1
+ ___76-[CSQueueAttributionManager retrieveAvatarForParticipant:withResultHandler:]_block_invoke
+ ___76-[CSQueueAttributionManager retrieveAvatarForParticipant:withResultHandler:]_block_invoke_2
+ ___76-[CSQueueAttributionManager retrieveAvatarForParticipant:withResultHandler:]_block_invoke_3
+ ___76-[CSQueueAttributionManager retrieveAvatarForParticipant:withResultHandler:]_block_invoke_4
+ ___87-[CSQueueAttributionManager retrieveAttributionsForQueueIdentifiers:withResultHandler:]_block_invoke
+ ___87-[CSQueueAttributionManager retrieveAttributionsForQueueIdentifiers:withResultHandler:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e22_v16?0"NSDictionary"8ls32l8
+ ___block_descriptor_40_e8_32s_e39_v32?0"NSString"8"NSDictionary"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e61_v32?0"NSString"8"CMContinuityCaptureParticipantInfo"16^B24ls32l8
+ ___block_descriptor_40_e8_32w_e86_"UITableViewCell"32?0"UITableView"8"NSIndexPath"16"CSPlayerResponseItemWrapper"24lw32l8
+ ___block_descriptor_48_e8_32s40bs_e40_v24?0"CSSingSessionState"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e45_v24?0"CSAvatarResponseMessage"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40bs_e50_v24?0"CSAttributionResponseMessage"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e17_v16?0"UIImage"8ls32l8s40l8
+ ___block_descriptor_48_e8_32s40s_e29_v24?0"UIImage"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs48w_e5_v8?0lw48l8s40l8s32l8
+ ___block_descriptor_56_e8_32s40s48bs_e34_v24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8
+ ___block_literal_global.135
+ ___block_literal_global.138
+ ___block_literal_global.141
+ ___block_literal_global.167
+ ___block_literal_global.236
+ ___block_literal_global.243
+ _objc_msgSend$_micImageForState:
+ _objc_msgSend$_onAddSongPressed
+ _objc_msgSend$_preferredFontForTextStyle:maximumContentSizeCategory:
+ _objc_msgSend$_requestInitialSessionStateWithCompletion:
+ _objc_msgSend$_stringFromSeconds:
+ _objc_msgSend$addEntriesFromDictionary:
+ _objc_msgSend$addExecutionBlock:
+ _objc_msgSend$addObjectsFromArray:
+ _objc_msgSend$addOperation:
+ _objc_msgSend$allItems
+ _objc_msgSend$allKeys
+ _objc_msgSend$appendItemsWithIdentifiers:intoSectionWithIdentifier:
+ _objc_msgSend$appendSectionsWithIdentifiers:
+ _objc_msgSend$applySnapshot:animatingDifferences:
+ _objc_msgSend$avatar
+ _objc_msgSend$belowConfiguration
+ _objc_msgSend$bringSubviewToFront:
+ _objc_msgSend$cellForRowAtIndexPath:
+ _objc_msgSend$constraintEqualToAnchor:multiplier:
+ _objc_msgSend$containsObject:
+ _objc_msgSend$containsString:
+ _objc_msgSend$contentInset
+ _objc_msgSend$contentInsets
+ _objc_msgSend$currentCalendar
+ _objc_msgSend$currentValue
+ _objc_msgSend$dateFromComponents:
+ _objc_msgSend$dequeueReusableCellWithIdentifier:forIndexPath:
+ _objc_msgSend$didChangeValueForKey:
+ _objc_msgSend$displayItems
+ _objc_msgSend$duration
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$grayButtonConfiguration
+ _objc_msgSend$hash
+ _objc_msgSend$imageWithData:
+ _objc_msgSend$indexPathsForVisibleRows
+ _objc_msgSend$initWithAddSongHandler:
+ _objc_msgSend$initWithMicVolume:reverbLevel:activeMicRemoteDisplayID:participants:
+ _objc_msgSend$initWithPlayAction:backAction:forwardAction:addSongAction:
+ _objc_msgSend$initWithQueueIdentifiers:
+ _objc_msgSend$initWithResponseItem:
+ _objc_msgSend$initWithReverbLevel:
+ _objc_msgSend$initWithSocialProfileIdentifier:
+ _objc_msgSend$initWithSource:
+ _objc_msgSend$initWithSymbolName:withFont:scale:
+ _objc_msgSend$initWithTableView:cellProvider:
+ _objc_msgSend$isNowPlaying
+ _objc_msgSend$isPlaying
+ _objc_msgSend$itemIdentifierForIndexPath:
+ _objc_msgSend$localizedStringWithFormat:
+ _objc_msgSend$lowercaseString
+ _objc_msgSend$maxValue
+ _objc_msgSend$minValue
+ _objc_msgSend$now
+ _objc_msgSend$participants
+ _objc_msgSend$playbackManager:didUpdateTracklist:
+ _objc_msgSend$queueIdentifierAttributionMap
+ _objc_msgSend$queueItemIdentifier
+ _objc_msgSend$registerClass:forCellReuseIdentifier:
+ _objc_msgSend$replaceSymbol:withFont:scale:
+ _objc_msgSend$responseItem
+ _objc_msgSend$retrieveAttributionsForQueueIdentifiers:handler:
+ _objc_msgSend$retrieveAttributionsForQueueIdentifiers:withResultHandler:
+ _objc_msgSend$retrieveAvatarForParticipant:handler:
+ _objc_msgSend$retrieveAvatarForParticipant:withResultHandler:
+ _objc_msgSend$section
+ _objc_msgSend$sectionIdentifierForIndex:
+ _objc_msgSend$set
+ _objc_msgSend$setAccessibilityLabel:
+ _objc_msgSend$setAllowsSelection:
+ _objc_msgSend$setAttributedText:
+ _objc_msgSend$setContent:
+ _objc_msgSend$setContentInset:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setHidden:
+ _objc_msgSend$setIsNowPlaying:
+ _objc_msgSend$setLabelsConfiguration:
+ _objc_msgSend$setMinute:
+ _objc_msgSend$setParticipantInfo:
+ _objc_msgSend$setSecond:
+ _objc_msgSend$setSectionHeaderTopPadding:
+ _objc_msgSend$setSeparatorStyle:
+ _objc_msgSend$setShadowOffset:
+ _objc_msgSend$setShadowOpacity:
+ _objc_msgSend$setShadowPath:
+ _objc_msgSend$setVerticalScrollIndicatorInsets:
+ _objc_msgSend$setupAddSongButtonWithAction:
+ _objc_msgSend$setupAlbumArtImageView
+ _objc_msgSend$setupArtistLabel
+ _objc_msgSend$setupLabelsStackView
+ _objc_msgSend$setupParticipantBadgeView
+ _objc_msgSend$setupPlaybackControlButtonsWithPlayAction:backAction:forwardAction:
+ _objc_msgSend$setupPlayerControlsView
+ _objc_msgSend$setupPlayingNextLabel
+ _objc_msgSend$setupSingersLabel
+ _objc_msgSend$setupTimelineControl
+ _objc_msgSend$setupTitleLabel
+ _objc_msgSend$setupViewsWithPlayAction:backAction:forwardAction:addSongAction:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$subarrayWithRange:
+ _objc_msgSend$systemFontOfSize:weight:
+ _objc_msgSend$tableView
+ _objc_msgSend$timeIntervalSinceDate:
+ _objc_msgSend$updateArtwork
+ _objc_msgSend$updateContent
+ _objc_msgSend$updateDataSource
+ _objc_msgSend$updateFonts
+ _objc_msgSend$updateForState:
+ _objc_msgSend$updatePlayPauseButtonWithState:
+ _objc_msgSend$updateSingersText
+ _objc_msgSend$willChangeValueForKey:
+ _objc_retain_x5
+ _objc_retain_x9
+ _os_variant_has_internal_diagnostics
+ _sharedManager.sharedManager
+ _swift_defaultActor_deallocate
+ _swift_defaultActor_destroy
+ _swift_defaultActor_initialize
+ _swift_deletedAsyncMethodErrorTu
+ _symbolic $s14ContinuitySing18ArtworkDownloadingP
+ _symbolic BD
+ _symbolic SDy__________G 10Foundation3URLV 14ContinuitySing17ArtworkDownloader33_0966ECFEC73A60E9F4456608686DCC0ELLC
+ _symbolic SayScCySo7UIImageCSg_____GG s5NeverO
+ _symbolic ScCySo7UIImageCSg_____G s5NeverO
+ _symbolic So11CSQueueCellC
+ _symbolic So20NSURLSessionDataTaskCSg
+ _symbolic _____ 14ContinuitySing17ArtworkDownloader33_0966ECFEC73A60E9F4456608686DCC0ELLC
+ _symbolic _____ 14ContinuitySing24ArtworkDownloaderManager33_0966ECFEC73A60E9F4456608686DCC0ELLC
+ _symbolic _____ 8MusicKit4SongV
+ _symbolic _____Sg 10Foundation4DataV
+ _symbolic _____Sg 16MusicKitInternal0A14PlaybackSourceO
+ _symbolic _____Sg 8MusicKit0A5VideoV
+ _symbolic _____Sg 8MusicKit4SongV
+ _symbolic _____yScCySo7UIImageCSg_____GG s23_ContiguousArrayStorageC s5NeverO
+ _symbolic _____y__________G 8MusicKit0A17AttributePropertyC AA6ArtistV AA7ArtworkV
+ _symbolic _____y__________G s18_DictionaryStorageC 10Foundation3URLV 14ContinuitySing17ArtworkDownloader33_0966ECFEC73A60E9F4456608686DCC0ELLC
- -[CSMicControl _micImageForCurrentState]
- -[CSMiniPlayerView _makeControlButtonForSymbolName:symbolScale:]
- -[CSMiniPlayerView addBackwardAction:]
- -[CSMiniPlayerView addForwardAction:]
- -[CSMiniPlayerView addPlayPauseAction:]
- -[CSMiniPlayerViewController _onBackwardPressed]
- -[CSMiniPlayerViewController _onForwardPressed]
- -[CSMiniPlayerViewController _onPlayPausePressed]
- -[CSMiniPlayerViewController viewDidLoad]
- -[CSShieldManager updateSessionState]
- -[CSSingSessionState initWithMicVolume:reverbLevel:activeMicRemoteDisplayID:]
- GCC_except_table129
- GCC_except_table135
- GCC_except_table3
- GCC_except_table67
- GCC_except_table83
- GCC_except_table89
- GCC_except_table92
- _OBJC_CLASS_$_ICMediaUserStateCenter
- _OBJC_CLASS_$_ICPrivacyInfo
- _OBJC_CLASS_$_NSSymbolReplaceContentTransition
- _OBJC_IVAR_$_CSMiniPlayerView._backwardButtonView
- _OBJC_IVAR_$_CSMiniPlayerView._forwardButtonView
- _OBJC_IVAR_$_CSMiniPlayerView._pauseButtonView
- _OBJC_IVAR_$_CSMiniPlayerView._playPauseButtonView
- _OBJC_IVAR_$_CSReverbMessage._reverb
- _OBJC_IVAR_$_CSReverbResponse._reverb
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CSPlaybackManagerObserver
- ___37-[CSShieldManager updateSessionState]_block_invoke
- ___37-[CSShieldManager updateSessionState]_block_invoke.cold.1
- ___37-[CSShieldManager updateSessionState]_block_invoke_2
- ___41-[CSMiniPlayerViewController viewDidLoad]_block_invoke
- ___41-[CSMiniPlayerViewController viewDidLoad]_block_invoke_2
- ___41-[CSMiniPlayerViewController viewDidLoad]_block_invoke_3
- ___42-[CSShieldViewController _showMusicUpsell]_block_invoke.207
- ___44-[CSShieldViewController presentMusicPicker]_block_invoke.125
- ___46-[CSShieldViewController _presentPairingError]_block_invoke.179
- ___50-[CSShieldViewController _tryBootstrapAgainAction]_block_invoke.248
- ___50-[CSShieldViewController _tryBootstrapAgainAction]_block_invoke.249
- ___53-[CSShieldConnectionManager _requestGroupSessionURL:]_block_invoke.36
- ___55-[CSShieldViewController _presentVersionMismatchError:]_block_invoke.190
- ___57-[CSShieldConnectionManager _bootstrapFromSingQRCodeURL:]_block_invoke.31
- ___57-[CSShieldViewController _handleInvalidMusicAccountError]_block_invoke.217
- ___57-[CSShieldViewController _handleInvalidMusicAccountError]_block_invoke.217.cold.1
- ___57-[CSShieldViewController _handleInvalidMusicAccountError]_block_invoke.223
- ___57-[CSShieldViewController _handleInvalidMusicAccountError]_block_invoke.223.cold.1
- ___57-[CSShieldViewController _handleInvalidMusicAccountError]_block_invoke.224
- ___57-[CSShieldViewController _handleMusicProfileUpdateNeeded]_block_invoke.233
- ___57-[CSShieldViewController _handleMusicProfileUpdateNeeded]_block_invoke.233.cold.1
- ___57-[CSShieldViewController _handleMusicProfileUpdateNeeded]_block_invoke.234
- ___59-[CSShieldViewController _presentEndpointDisconnectedError]_block_invoke.244
- ___62-[CSShieldViewController consumeSinglePressDownForButtonKind:]_block_invoke.132
- ___62-[CSShieldViewController consumeSinglePressDownForButtonKind:]_block_invoke_2.135
- ___62-[CSShieldViewController consumeSinglePressDownForButtonKind:]_block_invoke_2.135.cold.1
- ___block_descriptor_40_e8_32s_e40_v24?0"CSSingSessionState"8"NSError"16ls32l8
- ___block_literal_global.124
- ___block_literal_global.128
- ___block_literal_global.134
- ___block_literal_global.160
- ___block_literal_global.201
- ___block_literal_global.226
- _objc_msgSend$_makeControlButtonForSymbolName:symbolScale:
- _objc_msgSend$_micImageForCurrentState
- _objc_msgSend$activeUserState
- _objc_msgSend$addBackwardAction:
- _objc_msgSend$addForwardAction:
- _objc_msgSend$addPlayPauseAction:
- _objc_msgSend$displayNameAccepted
- _objc_msgSend$initWithMicVolume:reverbLevel:activeMicRemoteDisplayID:
- _objc_msgSend$initWithReverb:
- _objc_msgSend$initWithSymbolName:scale:
- _objc_msgSend$music
- _objc_msgSend$privacyAcknowledgementRequiredForMusic
- _objc_msgSend$replaceSymbol:scale:
- _objc_msgSend$reverb
- _objc_msgSend$setBaseForegroundColor:
- _objc_msgSend$setBottomPadding:
- _objc_msgSend$setSymbolImage:withContentTransition:
- _objc_msgSend$sharedPrivacyInfo
- _objc_msgSend$transition
- _objc_msgSend$updateSessionState
- _objc_msgSend$userProfile
CStrings:
+ "$defaultActor"
+ "%@\n\n[INTERNAL ONLY]\nReminder: AppleWiFi is not supported."
+ "%s: Add song button pressed!"
+ "%s: Got Message %@"
+ "%s: Got Reverb %@"
+ "%s: Override password set through internal defaults: %@"
+ "%s: Session State updated to %@.\nActive mic remote display identifier %@\nReverb:%@"
+ "%s: Update reverb button for level %@"
+ "%s: failed to send reverb %@ with error: %@"
+ "%s: sent reverb %@"
+ "-%@"
+ "-[CSPairingServer createNewPassword]"
+ "-[CSQueuePlaybackControlsView _localizedAddSongString]"
+ "-[CSQueueViewController _onAddSongPressed]"
+ "-[CSQueueViewController _onBackwardPressed]"
+ "-[CSQueueViewController _onForwardPressed]"
+ "-[CSQueueViewController _onPlayPausePressed]"
+ "-[CSRemoteRequestClient retrieveAttributionsForQueueIdentifiers:handler:]_block_invoke"
+ "-[CSRemoteRequestClient retrieveAvatarForParticipant:handler:]_block_invoke"
+ "-[CSRemoteRequestClient sendReverb:]"
+ "-[CSShieldManager _requestInitialSessionStateWithCompletion:]_block_invoke_2"
+ "<CSQueuedTrack title:%@; artist:%@; catalogID:%@; type:%@"
+ "@\"AVMediaTimelineControl\""
+ "@\"CSMicControlSymbolView\""
+ "@\"CSQueuePlaybackControlsView\""
+ "@\"MPCPlayerResponse\""
+ "@\"MPCPlayerResponseItem\""
+ "@\"NSArray\"16@0:8"
+ "@\"NSDate\""
+ "@\"NSDictionary\""
+ "@\"NSMutableDictionary\""
+ "@\"NSMutableSet\""
+ "@\"UITableViewCell\"32@?0@\"UITableView\"8@\"NSIndexPath\"16@\"CSPlayerResponseItemWrapper\"24"
+ "@\"UITableViewDiffableDataSource\""
+ "@\"_UIGrabber\""
+ "@20@0:8f16"
+ "@40@0:8@16@24q32"
+ "@48@0:8@16@24@32@40"
+ "@48@0:8d16q24@32@40"
+ "AVMediaTimelineControlSource"
+ "Avatar"
+ "CSAttributionRequestMessage"
+ "CSAttributionResponseMessage"
+ "CSAvatarRequestMessage"
+ "CSAvatarResponseMessage"
+ "CSMicControlSymbolView"
+ "CSPlayerResponseItemWrapper"
+ "CSQueueAttributionManager"
+ "CSQueueCell"
+ "CSQueuePlaybackControlsView"
+ "CSQueueSectionHeader"
+ "CSQueueViewController"
+ "CSReverbLevelHigh"
+ "CSReverbLevelLow"
+ "CSReverbLevelMedium"
+ "CSReverbLevelNone"
+ "ContinuitySing/ArtworkDownloader.swift"
+ "ContinuitySing/CSQueueCell.swift"
+ "Failed to enqueue song to system music player: %@"
+ "Failed to play music videos on system music player: %@"
+ "Failed to play songs on system music player: %@"
+ "HELP_BUTTON_ACCESSIBILITY_LABEL"
+ "Now Playing"
+ "Participants"
+ "QUEUE_UP_NEXT_TITLE"
+ "QueueAttributions"
+ "QueueIdentifiers"
+ "SocialProfileIdentifier"
+ "T@\"CMContinuityCaptureParticipantInfo\",&,N,V_participantInfo"
+ "T@\"CSMicControlSymbolView\",&,N,V_micSymbolView"
+ "T@\"MPCPlayerResponseItem\",&,N,V_content"
+ "T@\"MPCPlayerResponseItem\",R,N,V_responseItem"
+ "T@\"MPCPlayerResponseTracklist\",R,N"
+ "T@\"NSArray\",&,N"
+ "T@\"NSArray\",R,N,V_participants"
+ "T@\"NSArray\",R,N,V_queueIdentifiersToAttribute"
+ "T@\"NSDictionary\",R,N,V_queueIdentifierAttributionMap"
+ "T@\"NSString\",R,C,N,V_socialProfileIdentifier"
+ "T@\"UIImage\",&,N,V_offImage"
+ "T@\"UIImage\",&,N,V_onImage"
+ "T@\"UIImage\",R,N,V_avatar"
+ "T@\"UIImageView\",&,N,V_imageView"
+ "T@\"UIImageView\",R,N,V_albumArtImageView"
+ "T@\"UIImageView\",R,N,V_participantBadgeView"
+ "T@\"UIView\",&,N,V_glowView"
+ "TB,N,V_isNowPlaying"
+ "TB,R,N,GisLoading"
+ "TB,R,N,GisPlaying"
+ "Tf,R,N"
+ "Tq,R,N,V_reverbLevel"
+ "Unknown"
+ "Up Next"
+ "_TtC14ContinuitySingP33_0966ECFEC73A60E9F4456608686DCC0E17ArtworkDownloader"
+ "_TtC14ContinuitySingP33_0966ECFEC73A60E9F4456608686DCC0E24ArtworkDownloaderManager"
+ "_addSongButton"
+ "_addSongHandler"
+ "_albumArtImageView"
+ "_artistLabel"
+ "_attributions"
+ "_avatar"
+ "_avatars"
+ "_content"
+ "_currentResponse"
+ "_dataSource"
+ "_glowView"
+ "_goBackButton"
+ "_goForwardButton"
+ "_grabberView"
+ "_isNowPlaying"
+ "_itemsPendingAttribution"
+ "_labelsStackView"
+ "_labelsStackViewYPositionConstraint"
+ "_micImageForState:"
+ "_onAddSongPressed"
+ "_participantBadgeView"
+ "_participants"
+ "_pendingAvatarHandlers"
+ "_playPauseButton"
+ "_playerControlsView"
+ "_playingNextLabel"
+ "_preferredFontForTextStyle:maximumContentSizeCategory:"
+ "_queueIdentifierAttributionMap"
+ "_queueIdentifiersToAttribute"
+ "_requestInitialSessionStateWithCompletion:"
+ "_requestedAttributions"
+ "_responseDate"
+ "_responseItem"
+ "_singersLabel"
+ "_socialProfileIdentifier"
+ "_stringFromSeconds:"
+ "_timelineControl"
+ "addEntriesFromDictionary:"
+ "addExecutionBlock:"
+ "addObjectsFromArray:"
+ "addOperation:"
+ "albumArtImageView"
+ "allItems"
+ "allKeys"
+ "appendItemsWithIdentifiers:intoSectionWithIdentifier:"
+ "appendSectionsWithIdentifiers:"
+ "applewifi"
+ "applySnapshot:animatingDifferences:"
+ "avatar"
+ "belowConfiguration"
+ "bringSubviewToFront:"
+ "cell"
+ "cellForRowAtIndexPath:"
+ "com.apple.ContinuitySing.attributionRequest"
+ "com.apple.ContinuitySing.attributionRespone"
+ "com.apple.ContinuitySing.avatarRequest"
+ "com.apple.ContinuitySing.avatarResponse"
+ "constraintEqualToAnchor:multiplier:"
+ "containsObject:"
+ "containsString:"
+ "content"
+ "contentInset"
+ "contentInsets"
+ "contentItemIdentifier"
+ "continuations"
+ "currentCalendar"
+ "currentValue"
+ "currentValueText"
+ "d32@0:8@16@24"
+ "d32@0:8@16q24"
+ "dataTaskWithURL:completionHandler:"
+ "dateFromComponents:"
+ "dequeueReusableCellWithIdentifier:forIndexPath:"
+ "didChangeValueForKey:"
+ "displayItems"
+ "enqueuing music videos %s"
+ "enqueuing songs %s"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "f16@0:8"
+ "fetchTask"
+ "grayButtonConfiguration"
+ "handleOpenQueueTap:"
+ "image"
+ "imageWithData:"
+ "indexPathsForVisibleRows"
+ "initWithAddSongHandler:"
+ "initWithAttributions:"
+ "initWithAvatar:"
+ "initWithData:"
+ "initWithMicVolume:reverbLevel:activeMicRemoteDisplayID:participants:"
+ "initWithPlayAction:backAction:forwardAction:addSongAction:"
+ "initWithQueueIdentifiers:"
+ "initWithResponseItem:"
+ "initWithReverbLevel:"
+ "initWithSocialProfileIdentifier:"
+ "initWithSource:"
+ "initWithStyle:"
+ "initWithStyle:reuseIdentifier:"
+ "initWithSymbolName:withFont:scale:"
+ "initWithTableView:cellProvider:"
+ "isNowPlaying"
+ "isPlaying"
+ "itemIdentifierForIndexPath:"
+ "localizedStringWithFormat:"
+ "lowercaseString"
+ "m:ss"
+ "maxValue"
+ "maxValueText"
+ "minValue"
+ "music.note"
+ "now"
+ "offImage"
+ "onImage"
+ "overridePairingCode"
+ "participantBadgeView"
+ "participants"
+ "playbackManager:didUpdateTracklist:"
+ "player sees no active queue entry, playing songs %s"
+ "playing"
+ "playing sees no active queue entry, playing music videos %s"
+ "prepareForReuse"
+ "presentedViewController"
+ "queueIdentifierAttributionMap"
+ "queueIdentifiersToAttribute"
+ "queueItemIdentifier"
+ "registerClass:forCellReuseIdentifier:"
+ "replaceSymbol:withFont:scale:"
+ "responseItem"
+ "resume"
+ "retrieveAttributionsForQueueIdentifiers:handler:"
+ "retrieveAttributionsForQueueIdentifiers:withResultHandler:"
+ "retrieveAvatarForParticipant:handler:"
+ "retrieveAvatarForParticipant:withResultHandler:"
+ "section"
+ "sectionIdentifierForIndex:"
+ "set"
+ "setAccessibilityLabel:"
+ "setAllowsSelection:"
+ "setAttributedText:"
+ "setContent:"
+ "setContentInset:"
+ "setDateFormat:"
+ "setGlowView:"
+ "setHidden:"
+ "setImageView:"
+ "setIsNowPlaying:"
+ "setLabelsConfiguration:"
+ "setMinute:"
+ "setOffImage:"
+ "setOnImage:"
+ "setParticipantInfo:"
+ "setSecond:"
+ "setSectionHeaderTopPadding:"
+ "setSeparatorStyle:"
+ "setShadowOffset:"
+ "setShadowOpacity:"
+ "setShadowPath:"
+ "setTimeRangeMarks:"
+ "setVerticalScrollIndicatorInsets:"
+ "setupAddSongButtonWithAction:"
+ "setupAlbumArtImageView"
+ "setupArtistLabel"
+ "setupLabelsStackView"
+ "setupParticipantBadgeView"
+ "setupPlaybackControlButtonsWithPlayAction:backAction:forwardAction:"
+ "setupPlayerControlsView"
+ "setupPlayingNextLabel"
+ "setupSingersLabel"
+ "setupTimelineControl"
+ "setupTitleLabel"
+ "setupViewsWithPlayAction:backAction:forwardAction:addSongAction:"
+ "ssid"
+ "stringFromDate:"
+ "subarrayWithRange:"
+ "systemFontOfSize:weight:"
+ "tableView"
+ "tableView:heightForHeaderInSection:"
+ "tableView:heightForRowAtIndexPath:"
+ "tableView:viewForHeaderInSection:"
+ "timeIntervalSinceDate:"
+ "timeRangeMarks"
+ "updateArtwork"
+ "updateContent"
+ "updateDataSource"
+ "updateFonts"
+ "updateForState:"
+ "updatePlayPauseButtonWithState:"
+ "updateSingersText"
+ "urlDownloaders"
+ "v16@?0@\"NSDictionary\"8"
+ "v16@?0@\"UIImage\"8"
+ "v24@0:8@\"NSArray\"16"
+ "v24@?0@\"CSAttributionResponseMessage\"8@\"NSError\"16"
+ "v24@?0@\"CSAvatarResponseMessage\"8@\"NSError\"16"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"
+ "v24@?0@\"UIImage\"8@\"NSError\"16"
+ "v32@0:8@\"CSPlaybackManager\"16@\"MPCPlayerResponseTracklist\"24"
+ "v32@?0@\"NSData\"8@\"NSURLResponse\"16@\"NSError\"24"
+ "v32@?0@\"NSString\"8@\"CMContinuityCaptureParticipantInfo\"16^B24"
+ "v32@?0@\"NSString\"8@\"NSDictionary\"16^B24"
+ "v40@0:8@16@24q32"
+ "v48@0:8@16@24@32@40"
+ "willChangeValueForKey:"
+ "with %lld Singers"
- "\t"
- "%s: Active mic remote display identifier %@"
- "%s: Update reverb button for level %f"
- "%s: failed to send reverb %f with error: %@"
- "%s: sent reverb %f"
- "-[CSMiniPlayerViewController _onBackwardPressed]"
- "-[CSMiniPlayerViewController _onForwardPressed]"
- "-[CSMiniPlayerViewController _onPlayPausePressed]"
- "-[CSShieldManager updateSessionState]_block_invoke"
- "@40@0:8d16d24@32"
- "Failed to enqueue songs to system music player: %@"
- "T@\"UIImageView\",&,N,V_micSymbolView"
- "Td,R,N,V_reverb"
- "Td,R,N,V_reverbLevel"
- "_backwardButtonView"
- "_forwardButtonView"
- "_makeControlButtonForSymbolName:symbolScale:"
- "_micImageForCurrentState"
- "_pauseButtonView"
- "_playPauseButtonView"
- "_reverb"
- "activeUserState"
- "addBackwardAction:"
- "addForwardAction:"
- "addPlayPauseAction:"
- "displayNameAccepted"
- "initWithMicVolume:reverbLevel:activeMicRemoteDisplayID:"
- "privacyAcknowledgementRequiredForMusic"
- "setBaseForegroundColor:"
- "setSymbolImage:withContentTransition:"
- "sharedPrivacyInfo"
- "transition"
- "updateSessionState"
- "userProfile"

```
