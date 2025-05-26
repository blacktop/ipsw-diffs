## CarPlayUI

> `/System/Library/PrivateFrameworks/CarPlayUI.framework/CarPlayUI`

```diff

-271.7.10.0.0
-  __TEXT.__text: 0x21918
+294.16.1.0.0
+  __TEXT.__text: 0x21b90
   __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_methlist: 0x2c48
+  __TEXT.__objc_methlist: 0x2c54
   __TEXT.__const: 0x308
-  __TEXT.__cstring: 0x6f4
+  __TEXT.__cstring: 0x9d0
   __TEXT.__ustring: 0x12
   __TEXT.__oslogstring: 0x338
-  __TEXT.__unwind_info: 0x778
-  __TEXT.__objc_classname: 0x67f
-  __TEXT.__objc_methname: 0x952f
-  __TEXT.__objc_methtype: 0x10f4
-  __TEXT.__objc_stubs: 0x6d20
+  __TEXT.__unwind_info: 0x788
+  __TEXT.__objc_classname: 0x689
+  __TEXT.__objc_methname: 0x9527
+  __TEXT.__objc_methtype: 0x10e3
+  __TEXT.__objc_stubs: 0x6d40
   __DATA_CONST.__got: 0x1a0
-  __DATA_CONST.__const: 0x3e8
+  __DATA_CONST.__const: 0x410
   __DATA_CONST.__objc_classlist: 0x1a8
-  __DATA_CONST.__objc_catlist: 0x8
+  __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x5ea8
+  __DATA_CONST.__objc_const: 0x5e90
   __DATA_CONST.__objc_selrefs: 0x2208
+  __DATA_CONST.__objc_protorefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x350
+  __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x58
-  __AUTH_CONST.__objc_const: 0x13f0
+  __AUTH_CONST.__objc_const: 0x1430
+  __AUTH_CONST.__cfstring: 0xf80
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0xbe0
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_arrayobj: 0xa8
   __AUTH_CONST.__auth_got: 0x290
   __AUTH.__objc_data: 0x1090
-  __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x350
-  __DATA.__objc_superrefs: 0x130
-  __DATA.__objc_ivar: 0x444
+  __DATA.__objc_ivar: 0x440
   __DATA.__data: 0x4a0
   __DATA.__bss: 0xc0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/iTunesCloud.framework/iTunesCloud
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 974
-  Symbols:   3823
-  CStrings:  1967
+  Functions: 976
+  Symbols:   3830
+  CStrings:  1997
 
Symbols:
+ -[CPUINowPlayingView _updateAudioSessionRenderingMode]
+ -[CPUINowPlayingView audioSessionOperationQueue]
+ -[CPUINowPlayingView setAudioSessionOperationQueue:]
+ -[CPUIShadowImageView setupVisibleEffects:]
+ -[UIImage(CarPlayUI) isSquared]
+ _OBJC_IVAR_$_CPUINowPlayingView._audioSessionOperationQueue
+ __OBJC_$_CATEGORY_UIImage_$_CarPlayUI
+ __OBJC_$_INSTANCE_METHODS_UIImage(CarPlayUI)
+ ___54-[CPUINowPlayingView _updateAudioSessionRenderingMode]_block_invoke
+ ___54-[CPUINowPlayingView _updateAudioSessionRenderingMode]_block_invoke_2
+ ___67-[CPUINowPlayingViewController _updateArtworkIfNeeded:placeholder:]_block_invoke.147
+ ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
+ ___block_literal_global.151
+ __unnamed_array_storage.131
+ __unnamed_array_storage.51
+ __unnamed_array_storage.57
+ __unnamed_array_storage.62
+ _objc_msgSend$_updateAudioSessionRenderingMode
+ _objc_msgSend$audioSessionOperationQueue
+ _objc_msgSend$isSquared
+ _objc_msgSend$setupVisibleEffects:
- -[CPUINowPlayingView audioBadgeConstraints]
- -[CPUINowPlayingView progressBarToBottomBarGuide]
- -[CPUINowPlayingView setAudioBadgeConstraints:]
- -[CPUINowPlayingView setProgressBarToBottomBarGuide:]
- -[CPUIShadowImageView setupEffects]
- _OBJC_IVAR_$_CPUINowPlayingView._audioBadgeConstraints
- _OBJC_IVAR_$_CPUINowPlayingView._progressBarToBottomBarGuide
- ___67-[CPUINowPlayingViewController _updateArtworkIfNeeded:placeholder:]_block_invoke.144
- ___block_literal_global.150
- __unnamed_array_storage.125
- __unnamed_array_storage.48
- __unnamed_array_storage.54
- __unnamed_array_storage.59
- _objc_msgSend$audioBadgeConstraints
- _objc_msgSend$progressBarToBottomBarGuide
- _objc_msgSend$setupEffects
CStrings:
+ "\x16\x17"
+ "CPListAssistantCell"
+ "CPListImageRowItem"
+ "CPListImageRowItemImage"
+ "CPListImageRowItemImageTitle"
+ "CPListItem"
+ "CPListItemSubtitle"
+ "CPListItemTitle"
+ "CPListItemTrailingLabel"
+ "CPMessageListItem"
+ "CPNowPlayingAddToLibraryButton"
+ "CPNowPlayingBackButton"
+ "CPNowPlayingModeControlView"
+ "CPNowPlayingMoreButton"
+ "CPNowPlayingPlayPauseStopButton"
+ "CPNowPlayingPlaybackRateButton"
+ "CPNowPlayingProgressBarLive"
+ "CPNowPlayingProgressBarLiveTrackView"
+ "CPNowPlayingProgressBarTime"
+ "CPNowPlayingProgressBarTimeRemaining"
+ "CPNowPlayingRepeatButton"
+ "CPNowPlayingShuffleButton"
+ "CPNowPlayingSongAlbum"
+ "CPNowPlayingSongArtist"
+ "CPNowPlayingSongDetailsView"
+ "CPNowPlayingSongTitle"
+ "CPNowPlayingTransportLeftButton"
+ "CPNowPlayingTransportRightButton"
+ "CPNowPlayingView"
+ "CarPlayUI"
+ "T@\"NSOperationQueue\",&,N,V_audioSessionOperationQueue"
+ "T@\"NSString\",?,R,C"
+ "TB,?,N,GisResizeAnimationCustomizationPermitted"
+ "TB,R,N,GisSquared"
+ "_audioSessionOperationQueue"
+ "_updateAudioSessionRenderingMode"
+ "audioSessionOperationQueue"
+ "com.apple.carplayui.audioSession"
+ "isSquared"
+ "person.spatialaudio.fill"
+ "setAudioSessionOperationQueue:"
+ "setupVisibleEffects:"
+ "squared"
- "\x16\x18"
- "@\"UILayoutGuide\""
- "T@\"NSArray\",&,N,V_audioBadgeConstraints"
- "T@\"UILayoutGuide\",&,N,V_progressBarToBottomBarGuide"
- "TB,N,GisResizeAnimationCustomizationPermitted"
- "_audioBadgeConstraints"
- "_progressBarToBottomBarGuide"
- "audioBadgeConstraints"
- "person.spatialaudio.stereo.fill"
- "progressBarToBottomBarGuide"
- "setAudioBadgeConstraints:"
- "setProgressBarToBottomBarGuide:"
- "setupEffects"

```
