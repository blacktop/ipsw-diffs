## MusicApplication

> `/System/Library/AccessibilityBundles/MusicApplication.axbundle/MusicApplication`

```diff

-3005.4.19.0.0
-  __TEXT.__text: 0x12198
-  __TEXT.__auth_stubs: 0x500
+3005.16.0.0.0
+  __TEXT.__text: 0x12f24
+  __TEXT.__auth_stubs: 0x4b0
   __TEXT.__objc_methlist: 0x2960
   __TEXT.__cstring: 0x4413
   __TEXT.__const: 0x18

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x8c0
   __DATA_CONST.__objc_superrefs: 0x288
-  __AUTH_CONST.__auth_got: 0x290
+  __AUTH_CONST.__auth_got: 0x268
   __AUTH_CONST.__const: 0x440
   __AUTH_CONST.__cfstring: 0x4f80
   __AUTH_CONST.__objc_const: 0x72b0

   - /usr/lib/libAccessibility.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 94FF4577-58F6-38CC-B9BD-81851EC4BCE1
+  UUID: DEAEFB5A-AE37-3248-99D2-0B527FB54A56
   Functions: 761
-  Symbols:   2981
+  Symbols:   2976
   CStrings:  1831
 
Symbols:
+ _objc_retain_x27
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x8
Functions:
~ -[NowPlayingQueueHeaderViewAccessibility _accessibilityLoadAccessibilityInformation] : 128 -> 132
~ +[NowPlayingQueueCellAccessibility _accessibilityPerformValidations:] : 180 -> 188
~ -[NowPlayingQueueCellAccessibility accessibilityLabel] : 336 -> 364
~ +[ReactionsButtonAccessibility _accessibilityPerformValidations:] : 132 -> 144
~ -[ReactionsButtonAccessibility accessibilityValue] : 228 -> 248
~ +[QRCodeOverlayViewControllerAccessibility _accessibilityPerformValidations:] : 176 -> 184
~ -[QRCodeOverlayViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 284 -> 304
~ -[AccountButtonAccessibility accessibilityTraits] : 196 -> 204
~ +[PersonHorizontalCellAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[PersonHorizontalCellAccessibility accessibilityLabel] : 148 -> 160
~ +[VocalsAttenuationSliderAccessibility _accessibilityPerformValidations:] : 156 -> 164
~ -[VocalsAttenuationSliderAccessibility accessibilityValue] : 116 -> 124
~ +[VerticalToggleSliderAccessibility _accessibilityPerformValidations:] : 304 -> 312
~ -[VerticalToggleSliderAccessibility accessibilityValue] : 160 -> 172
~ ___66-[VerticalToggleSliderAccessibility _accessibilityIncreaseSlider:]_block_invoke : 280 -> 296
~ -[VerticalToggleSliderAccessibility _accessibilityAnnounceNewValue] : 120 -> 124
~ +[MusicApplicationSearchBarAccessibility _accessibilityPerformValidations:] : 180 -> 188
~ -[MusicApplicationSearchBarAccessibility _accessibilityLoadAccessibilityInformation] : 156 -> 168
~ -[UIViewControllerAccessibility__MusicApplication__UIKit viewDidLoad] : 196 -> 204
~ -[UIViewControllerAccessibility__MusicApplication__UIKit didChangeVoiceOverOrSwitchControlStatus:] : 188 -> 196
~ +[MusicInterstellarContentViewAccessibility _accessibilityPerformValidations:] : 184 -> 196
~ -[MusicInterstellarContentViewAccessibility accessibilityLabel] : 388 -> 424
~ -[MusicInterstellarContentViewAccessibility _accessibilitySupplementaryFooterViews] : 172 -> 180
~ +[NowPlayingContentViewAccessibility _accessibilityPerformValidations:] : 120 -> 132
~ -[NowPlayingContentViewAccessibility isAccessibilityElement] : 64 -> 68
~ -[NowPlayingContentViewAccessibility _axIsVideo] : 72 -> 76
~ -[NowPlayingContentViewAccessibility accessibilityLabel] : 72 -> 76
~ +[VolumeSliderAccessibility _accessibilityPerformValidations:] : 168 -> 176
~ -[VolumeSliderAccessibility accessibilityValue] : 100 -> 108
~ -[VolumeSliderAccessibility _accessibilityIncreaseVolume:] : 224 -> 228
~ +[LyricsSelectionViewControllerAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ ___72-[LyricsSelectionViewControllerAccessibility accessibilityDidSelectItem]_block_invoke : 136 -> 144
~ +[PlayerTimeControlAccessibility _accessibilityPerformValidations:] : 228 -> 236
~ -[PlayerTimeControlAccessibility isAccessibilityElement] : 92 -> 96
~ -[PlayerTimeControlAccessibility accessibilityLabel] : 168 -> 184
~ -[PlayerTimeControlAccessibility accessibilityValue] : 312 -> 344
~ +[RadioStationCellAccessibility _accessibilityPerformValidations:] : 188 -> 200
~ -[RadioStationCellAccessibility accessibilityLabel] : 268 -> 292
~ -[RadioStationCellAccessibility accessibilityUserInputLabels] : 148 -> 160
~ +[UICollectionViewListCellAccessibility__MusicUI__UIKit _accessibilityPerformValidations:] : 100 -> 108
~ -[UICollectionViewListCellAccessibility__MusicUI__UIKit accessibilityLabel] : 160 -> 172
~ -[UICollectionViewListCellAccessibility__MusicUI__UIKit _axIsInViewControllerClass:] : 172 -> 176
~ ___84-[UICollectionViewListCellAccessibility__MusicUI__UIKit _axIsInViewControllerClass:]_block_invoke : 80 -> 84
~ +[PersonVerticalCellAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[PersonVerticalCellAccessibility accessibilityLabel] : 148 -> 160
~ +[LiveRadioCellAccessibility _accessibilityPerformValidations:] : 328 -> 340
~ -[LiveRadioCellAccessibility accessibilityLabel] : 84 -> 92
~ -[LiveRadioCellAccessibility accessibilityUserInputLabels] : 112 -> 120
~ -[LiveRadioCellAccessibility _accessibilitySupplementaryFooterViews] : 292 -> 312
~ +[UIButtonBarButtonAccessibility__Music__UIKit _accessibilityPerformValidations:] : 352 -> 360
~ -[UIButtonBarButtonAccessibility__Music__UIKit accessibilityLabel] : 212 -> 228
~ -[UIButtonBarButtonAccessibility__Music__UIKit isAccessibilityElement] : 104 -> 108
~ -[UIButtonBarButtonAccessibility__Music__UIKit _accessibilityLoadAccessibilityInformation] : 236 -> 248
~ +[DetailHeaderAccessibility _accessibilityPerformValidations:] : 672 -> 680
~ -[DetailHeaderAccessibility _accessibilityLoadAccessibilityInformation] : 564 -> 612
~ ___71-[DetailHeaderAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 80 -> 84
~ -[DetailHeaderAccessibility _axLabelForActionButtonForContainerProperties:] : 400 -> 424
~ -[DetailHeaderAccessibility _axStringForActiveCallaborators:] : 228 -> 248
~ -[DetailHeaderAccessibility _axIsCollaborativeForModelPlaylist:] : 92 -> 96
~ -[DetailHeaderAccessibility _axCuratorNameForPlaylist:] : 172 -> 188
~ -[DetailHeaderAccessibility _axOwnerNameForPlaylist:] : 112 -> 120
~ -[DetailHeaderAccessibility _axNameForAuthor:] : 172 -> 188
~ +[TitleSectionHeaderViewAccessibility _accessibilityPerformValidations:] : 184 -> 196
~ -[TitleSectionHeaderViewAccessibility isAccessibilityElement] : 60 -> 64
~ -[TitleSectionHeaderViewAccessibility accessibilityLabel] : 148 -> 160
~ -[TitleSectionHeaderViewAccessibility _accessibilitySupplementaryFooterViews] : 168 -> 180
~ +[SymbolButtonAccessibility _accessibilityPerformValidations:] : 452 -> 464
~ -[SymbolButtonAccessibility isAccessibilityElement] : 76 -> 80
~ -[SymbolButtonAccessibility _axIsCircularProgressView] : 100 -> 104
~ -[SymbolButtonAccessibility _accessibilityLabelHelper] : 1048 -> 1104
~ -[SymbolButtonAccessibility accessibilityLabel] : 128 -> 136
~ -[SymbolButtonAccessibility accessibilityValue] : 164 -> 176
~ -[SymbolButtonAccessibility accessibilityTraits] : 204 -> 212
~ -[TextViewLabelAccessibility accessibilityValue] : 76 -> 84
~ -[TextViewLabelAccessibility _accessibilityLineNumberAndColumnForPoint:] : 100 -> 108
~ -[TextViewLabelAccessibility _accessibilityRangeForLineNumberAndColumn:] : 96 -> 100
~ -[TextViewLabelAccessibility _accessibilitySetSelectedTextRange:] : 88 -> 92
~ -[TextViewLabelAccessibility _accessibilitySelectedTextRange] : 72 -> 76
~ -[TextViewLabelAccessibility accessibilityTraits] : 56 -> 60
~ +[PosterCellAccessibility _accessibilityPerformValidations:] : 284 -> 296
~ -[PosterCellAccessibility accessibilityLabel] : 276 -> 300
~ -[PosterCellAccessibility _accessibilityLoadAccessibilityInformation] : 184 -> 192
~ +[AlbumCellAccessibility _accessibilityPerformValidations:] : 188 -> 200
~ -[AlbumCellAccessibility accessibilityLabel] : 268 -> 292
~ -[AlbumCellAccessibility accessibilityUserInputLabels] : 184 -> 200
~ -[NowPlayingAutoPlayButtonAccessibility accessibilityValue] : 80 -> 84
~ +[LibraryRecommendationBannerViewControllerAccessibility _accessibilityPerformValidations:] : 248 -> 260
~ -[LibraryRecommendationBannerViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 440 -> 444
~ ___100-[LibraryRecommendationBannerViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 188 -> 200
~ +[MenuCellAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[MenuCellAccessibility accessibilityValue] : 152 -> 168
~ -[MenuCellAccessibility accessibilityActivationPoint] : 140 -> 148
~ -[MenuCellAccessibility accessibilityTraits] : 176 -> 180
~ +[RadioShowCellAccessibility _accessibilityPerformValidations:] : 184 -> 196
~ +[BrickCellAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ +[CustomRoomAlbumCellAccessibility _accessibilityPerformValidations:] : 184 -> 196
~ +[CustomRoomMusicVideoCellAccessibility _accessibilityPerformValidations:] : 184 -> 196
~ +[UITransitionViewAccessibility__MusicUI__UIKit _accessibilityPerformValidations:] : 248 -> 256
~ -[UITransitionViewAccessibility__MusicUI__UIKit accessibilityViewIsModal] : 388 -> 408
~ -[UITransitionViewAccessibility__MusicUI__UIKit _foundNowPlayingViewControllerForIPad] : 464 -> 512
~ +[FeaturedShowcaseCellAccessibility _accessibilityPerformValidations:] : 184 -> 196
~ +[FeaturedSongCellAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ +[UserDetailsCellAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[UserDetailsCellAccessibility accessibilityLabel] : 148 -> 160
~ +[GridItemButtonCellAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ +[GroupedTextListViewAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[GroupedTextListViewAccessibility _accessibilityLoadAccessibilityInformation] : 384 -> 400
~ ___78-[GroupedTextListViewAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 124 -> 132
~ +[BottomPlayerViewControllerAccessibility _accessibilityPerformValidations:] : 616 -> 624
~ -[BottomPlayerViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 2440 -> 2520
~ ___85-[BottomPlayerViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 160 -> 176
~ ___85-[BottomPlayerViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 100 -> 108
~ ___85-[BottomPlayerViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_4 : 8 -> 56
~ -[BottomPlayerViewControllerAccessibility setArtworkView:] : 220 -> 228
~ +[JSDrivenViewControllerAccessibility _accessibilityPerformValidations:] : 232 -> 240
~ -[JSDrivenViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 124 -> 128
~ +[JSInlinePopupViewControllerAccessibility _accessibilityPerformValidations:] : 180 -> 192
~ -[JSInlinePopupViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 432 -> 464
~ -[JSSocialProfileVerticalStackViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 148 -> 160
~ +[MovieHorizontalCellAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[MovieHorizontalCellAccessibility accessibilityLabel] : 244 -> 264
~ +[UICollectionViewAccessibility__MusicApplication__UIKit _accessibilityPerformValidations:] : 228 -> 236
~ -[UICollectionViewAccessibility__MusicApplication__UIKit accessibilityShouldSpeakItemReorderEvents] : 64 -> 68
~ ___99-[UICollectionViewAccessibility__MusicApplication__UIKit accessibilityShouldSpeakItemReorderEvents]_block_invoke : 116 -> 120
~ -[UICollectionViewAccessibility__MusicApplication__UIKit _accessibilitySupplementaryViewSectionHeaderIdentifiers] : 272 -> 292
~ ___113-[UICollectionViewAccessibility__MusicApplication__UIKit _accessibilitySupplementaryViewSectionHeaderIdentifiers]_block_invoke : 92 -> 96
~ -[UICollectionViewAccessibility__MusicApplication__UIKit _accessibilityIsShelfCollectionView] : 120 -> 124
~ +[SyncedLyricsViewControllerAccessibility _accessibilityPerformValidations:] : 116 -> 124
~ -[SyncedLyricsViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 108 -> 112
~ +[MultiChoiceCellAccessibility _accessibilityPerformValidations:] : 160 -> 172
~ -[MusicUINavigationButtonAccessibility accessibilityLabel] : 160 -> 172
~ -[JSSettingsContainerViewControllerAccessibility accessibilityPerformEscape] : 196 -> 200
~ ___76-[JSSettingsContainerViewControllerAccessibility accessibilityPerformEscape]_block_invoke : 76 -> 80
~ +[MusicVideoHorizontalCellAccessibility _accessibilityPerformValidations:] : 212 -> 224
~ -[MusicVideoHorizontalCellAccessibility accessibilityTraits] : 236 -> 244
~ +[NowPlayingTransportButtonAccessibility _accessibilityPerformValidations:] : 108 -> 120
~ +[MusicVideoVerticalCellAccessibility _accessibilityPerformValidations:] : 188 -> 200
~ -[MusicVideoVerticalCellAccessibility accessibilityLabel] : 268 -> 292
~ +[UIButtonAccessibility__MusicApplication__UIKit _accessibilityPerformValidations:] : 128 -> 140
~ -[UIButtonAccessibility__MusicApplication__UIKit isAccessibilityElement] : 260 -> 280
~ -[UIButtonAccessibility__MusicApplication__UIKit accessibilityLabel] : 212 -> 228
~ -[UILabelAccessibility__MusicApplication__UIKit isAccessibilityElement] : 120 -> 124
~ -[JSSearchLandingViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 156 -> 164
~ +[UIViewAccessibility__MusicApplication__UIKit _accessibilityPerformValidations:] : 112 -> 120
~ -[UIViewAccessibility__MusicApplication__UIKit _axViewContainsSwitch] : 368 -> 376
~ -[UIViewAccessibility__MusicApplication__UIKit isAccessibilityElement] : 120 -> 124
~ -[UIViewAccessibility__MusicApplication__UIKit accessibilityValue] : 152 -> 168
~ -[UIViewAccessibility__MusicApplication__UIKit accessibilityActivationPoint] : 140 -> 148
~ -[UIViewAccessibility__MusicApplication__UIKit accessibilityTraits] : 124 -> 132
~ -[UIViewAccessibility__MusicApplication__UIKit _accessibilitySupplementaryFooterViews] : 248 -> 272
~ ___86-[UIViewAccessibility__MusicApplication__UIKit _accessibilitySupplementaryFooterViews]_block_invoke : 80 -> 84
~ +[FlowcaseCellAccessibility _accessibilityPerformValidations:] : 184 -> 196
~ -[FlowcaseCellAccessibility accessibilityLabel] : 216 -> 236
~ +[SongCellAccessibility _accessibilityPerformValidations:] : 608 -> 620
~ -[SongCellAccessibility accessibilityLabel] : 860 -> 924
~ -[SongCellAccessibility accessibilityUserInputLabels] : 84 -> 92
~ -[SongCellAccessibility accessibilityValue] : 84 -> 92
~ -[SongCellAccessibility accessibilityTraits] : 212 -> 220
~ -[SongCellAccessibility _isSongDownloaded] : 60 -> 64
~ ___42-[SongCellAccessibility _isSongDownloaded]_block_invoke : 280 -> 300
~ -[SongCellAccessibility _axPlaybackStateLabel] : 260 -> 280
~ -[NowPlayingRepeatButtonAccessibility accessibilityValue] : 84 -> 88
~ -[NowPlayingShuffleButtonAccessibility accessibilityValue] : 84 -> 88
~ +[PageHeaderContentViewAccessibility _accessibilityPerformValidations:] : 216 -> 228
~ -[PageHeaderContentViewAccessibility _accessibilitySupplementaryFooterViews] : 364 -> 376
~ ___76-[PageHeaderContentViewAccessibility _accessibilitySupplementaryFooterViews]_block_invoke_3 : 340 -> 344
~ ___76-[PageHeaderContentViewAccessibility _accessibilitySupplementaryFooterViews]_block_invoke_4 : 80 -> 84
~ +[ParagraphViewAccessibility _accessibilityPerformValidations:] : 160 -> 172
~ -[ParagraphViewAccessibility isAccessibilityElement] : 116 -> 128
~ -[ParagraphViewAccessibility _accessibilityLoadAccessibilityInformation] : 276 -> 296
~ _accessibilityMusicLocalizedString : 176 -> 184
~ _accessibilityOasisMusicLocalizedString : 176 -> 184
~ _speakReorderItems : 632 -> 672
~ _speakReorderItemsTableView : 632 -> 672
~ _accessibilityStripUnfavorableCharacters : 148 -> 156
~ +[AXMusicApplicationGlue accessibilityInitializeBundle] : 164 -> 168
~ ___55+[AXMusicApplicationGlue accessibilityInitializeBundle]_block_invoke : 412 -> 416
~ ___55+[AXMusicApplicationGlue accessibilityInitializeBundle]_block_invoke_2 : 84 -> 88
~ ___55+[AXMusicApplicationGlue accessibilityInitializeBundle]_block_invoke_3 : 2072 -> 2080
~ +[NSObject(AXPrivResponse) accessibilityIsFavoriteEnabledForResponse:] : 120 -> 132
~ +[NSObject(AXPrivResponse) _accessibilitySkipIntervalInDirection:forResponse:] : 164 -> 176
~ +[NSObject(AXPrivResponse) accessibilityIsSeekEnabledInDirection:forResponse:] : 276 -> 280
~ ___78+[NSObject(AXPrivResponse) accessibilityIsSeekEnabledInDirection:forResponse:]_block_invoke : 100 -> 104
~ +[NSObject(AXPrivResponse) accessibilitySeekButtonStringInDirection:response:] : 156 -> 164
~ +[NSObject(AXPrivResponse) accessibilityPlayPauseStopButtonString:] : 264 -> 280
~ +[NSObject(AXPrivResponse) accessibilityAttributesForAccountButtonInAccessoryView:] : 328 -> 348
~ +[NowPlayingControlsViewControllerAccessibility _accessibilityPerformValidations:] : 780 -> 788
~ -[NowPlayingControlsViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 1440 -> 1492
~ ___91-[NowPlayingControlsViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke : 148 -> 160
~ ___91-[NowPlayingControlsViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_2 : 76 -> 80
~ ___91-[NowPlayingControlsViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_3 : 104 -> 112
~ ___91-[NowPlayingControlsViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_4 : 148 -> 160
~ ___91-[NowPlayingControlsViewControllerAccessibility _accessibilityLoadAccessibilityInformation]_block_invoke_7 : 76 -> 80
~ -[NowPlayingControlsViewControllerAccessibility _axLikedBannedValueForState:] : 84 -> 88
~ -[NowPlayingControlsViewControllerAccessibility _accessibilityLeftbuttonValueString] : 248 -> 268
~ -[NowPlayingControlsViewControllerAccessibility _axUpNextBadgeValue] : 528 -> 580
~ -[NowPlayingControlsViewControllerAccessibility _accessibilityResponseTracklist] : 84 -> 92
~ -[NowPlayingControlsViewControllerAccessibility _accessibilityResponseTracklistPlayingItem] : 84 -> 92
~ +[SyncedLyricsLineViewAccessibility _accessibilityPerformValidations:] : 348 -> 356
~ -[SyncedLyricsLineViewAccessibility accessibilityLabel] : 580 -> 628
~ -[SyncedLyricsLineViewAccessibility setSelected:animator:] : 248 -> 260
~ -[ProgressViewAccessibility accessibilityValue] : 168 -> 180
~ +[PromotionalImageryViewAccessibility _accessibilityPerformValidations:] : 120 -> 128
~ +[SearchResultCellAccessibility _accessibilityPerformValidations:] : 188 -> 200
~ -[SearchResultCellAccessibility accessibilityLabel] : 268 -> 292
~ +[RankedMusicVideoVerticalCellAccessibility _accessibilityPerformValidations:] : 188 -> 200
~ -[RankedMusicVideoVerticalCellAccessibility accessibilityLabel] : 168 -> 180
~ +[SearchResultsViewControllerAccessibility _accessibilityPerformValidations:] : 120 -> 128
~ -[SearchResultsViewControllerAccessibility _accessibilityLoadAccessibilityInformation] : 184 -> 192
~ +[PersonCellAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[PersonCellAccessibility accessibilityValue] : 84 -> 92
~ -[PersonCellAccessibility accessibilityActivate] : 224 -> 228
~ +[FeaturedRadioShowCellAccessibility _accessibilityPerformValidations:] : 188 -> 200
~ -[FeaturedRadioShowCellAccessibility accessibilityLabel] : 240 -> 260
~ +[PlaylistCellAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[PlaylistCellAccessibility accessibilityLabel] : 148 -> 160
~ +[ShowcaseCellAccessibility _accessibilityPerformValidations:] : 188 -> 200
~ -[ShowcaseCellAccessibility accessibilityLabel] : 176 -> 188
~ +[SocialPersonVerticalCellAccessibility _accessibilityPerformValidations:] : 184 -> 196
~ -[SocialPersonVerticalCellAccessibility _accessibilitySupplementaryFooterViews] : 292 -> 316
~ +[SocialProfilesAccessoryViewAccessibility _accessibilityPerformValidations:] : 120 -> 128
~ +[TVShowCellAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ +[TVShowEpisodeCellAccessibility _accessibilityPerformValidations:] : 244 -> 256
~ -[TVShowEpisodeCellAccessibility accessibilityElements] : 524 -> 568
~ +[HorizontalLockupCollectionViewCellAccessibility _accessibilityPerformValidations:] : 388 -> 396
~ -[HorizontalLockupCollectionViewCellAccessibility accessibilityCustomActions] : 1204 -> 1260
~ -[HorizontalLockupCollectionViewCellAccessibility automationElements] : 192 -> 208
~ -[HorizontalLockupCollectionViewCellAccessibility _accessibilityIndexPathForCell] : 240 -> 256
~ -[HorizontalLockupCollectionViewCellAccessibility _privateAccessibilityCustomActions] : 400 -> 432
~ -[HorizontalLockupCollectionViewCellAccessibility _axPerformCustomAction:] : 256 -> 264
~ ___74-[HorizontalLockupCollectionViewCellAccessibility _axPerformCustomAction:]_block_invoke : 140 -> 148
~ -[HorizontalLockupCollectionViewCellAccessibility axCustomActionForContextualAction:] : 200 -> 208
~ -[TVShowEpisodeDetailViewAccessibility _accessibilityLoadAccessibilityInformation] : 208 -> 220
~ +[TVShowPlayBarViewAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[TVShowPlayBarViewAccessibility _axPlayButton] : 196 -> 208
~ -[TVShowPlayBarViewAccessibility _axContextActionButton] : 196 -> 208
~ -[TVShowPlayBarViewAccessibility _accessibilityPerformMoreAction:] : 52 -> 56
~ -[TVShowPlayBarViewAccessibility _accessibilityPerformPlayAction:] : 52 -> 56
~ -[TVShowPlayBarViewAccessibility accessibilityCustomActions] : 372 -> 400
~ -[TVShowPlayBarViewAccessibility automationElements] : 216 -> 236
~ +[FeaturedMusicVideoVerticalCellAccessibility _accessibilityPerformValidations:] : 156 -> 168
~ -[FeaturedMusicVideoVerticalCellAccessibility accessibilityLabel] : 380 -> 408
~ -[ToggleCellAccessibility accessibilityValue] : 152 -> 168
~ -[ToggleCellAccessibility accessibilityActivationPoint] : 140 -> 148
~ -[ToggleCellAccessibility accessibilityTraits] : 124 -> 132
~ +[MusicApplicationUIScrollViewAccessibility _accessibilityPerformValidations:] : 204 -> 212
~ -[MusicApplicationUIScrollViewAccessibility _accessibilityDrawsFocusRingWhenChildrenFocused] : 64 -> 68
~ ___92-[MusicApplicationUIScrollViewAccessibility _accessibilityDrawsFocusRingWhenChildrenFocused]_block_invoke : 80 -> 84
~ -[MusicApplicationUIScrollViewAccessibility _accessibilityScrollStatus] : 616 -> 644
~ ___71-[MusicApplicationUIScrollViewAccessibility _accessibilityScrollStatus]_block_invoke : 80 -> 84
~ -[MusicApplicationUIScrollViewAccessibility _accessibilityScrollHeightDistance] : 332 -> 356
~ ___79-[MusicApplicationUIScrollViewAccessibility _accessibilityScrollHeightDistance]_block_invoke : 80 -> 84
~ +[UpsellBannerViewAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[UpsellBannerViewAccessibility accessibilityLabel] : 244 -> 260
~ +[FeaturedPlaylistCellAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[FeaturedPlaylistCellAccessibility accessibilityLabel] : 148 -> 160
~ +[UserDetailsEditCellAccessibility _accessibilityPerformValidations:] : 128 -> 140
~ -[VerticalLockupCollectionViewCellAccessibility _axCollectionViewLayout] : 184 -> 196
~ -[VerticalLockupCollectionViewCellAccessibility _accessibilityLoadAccessibilityInformation] : 156 -> 164
~ -[VideoHeaderLockupViewAccessibility accessibilityLabel] : 140 -> 152
~ -[VideoHeaderLockupViewAccessibility accessibilityValue] : 84 -> 92
~ +[SocialPersonHorizontalCellAccessibility _accessibilityPerformValidations:] : 244 -> 256
~ -[SocialPersonHorizontalCellAccessibility automationElements] : 184 -> 200
~ -[SocialPersonHorizontalCellAccessibility _accessibilitySupplementaryFooterViews] : 156 -> 168
~ -[SocialPersonHorizontalCellAccessibility _accessibilityApproveButtonAction:] : 72 -> 76
~ -[SocialPersonHorizontalCellAccessibility _accessibilityDeclineButtonAction:] : 72 -> 76
~ -[SocialPersonHorizontalCellAccessibility accessibilityCustomActions] : 308 -> 320

```
