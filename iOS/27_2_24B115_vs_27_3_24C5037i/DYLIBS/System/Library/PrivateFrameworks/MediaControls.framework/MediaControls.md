## MediaControls

> `/System/Library/PrivateFrameworks/MediaControls.framework/MediaControls`

```diff

-4026.210.3.0.0
-  __TEXT.__text: 0x21ab18
-  __TEXT.__objc_methlist: 0x15de4
-  __TEXT.__cstring: 0x6f24
+4026.300.11.0.0
+  __TEXT.__text: 0x21c278
+  __TEXT.__objc_methlist: 0x15f0c
+  __TEXT.__cstring: 0x6fa4
   __TEXT.__ustring: 0x28
-  __TEXT.__const: 0xbd94
-  __TEXT.__gcc_except_tab: 0x1598
-  __TEXT.__oslogstring: 0x86d9
+  __TEXT.__const: 0xbdc4
+  __TEXT.__gcc_except_tab: 0x15d8
+  __TEXT.__oslogstring: 0x8779
   __TEXT.__dlopen_cstrs: 0x64
-  __TEXT.__constg_swiftt: 0x7830
-  __TEXT.__swift5_typeref: 0x340a
-  __TEXT.__swift5_reflstr: 0x4bed
-  __TEXT.__swift5_fieldmd: 0x4c48
+  __TEXT.__constg_swiftt: 0x78c0
+  __TEXT.__swift5_typeref: 0x341a
+  __TEXT.__swift5_reflstr: 0x4c8d
+  __TEXT.__swift5_fieldmd: 0x4c84
   __TEXT.__swift5_types: 0x614
-  __TEXT.__swift5_capture: 0x14d8
+  __TEXT.__swift5_capture: 0x1500
   __TEXT.__swift5_protos: 0xb8
   __TEXT.__swift5_proto: 0x5fc
   __TEXT.__swift5_builtin: 0x35c

   __TEXT.__swift_as_ret: 0x3c
   __TEXT.__swift_as_cont: 0x7c
   __TEXT.__swift5_assocty: 0x390
-  __TEXT.__unwind_info: 0xaa90
+  __TEXT.__unwind_info: 0xab00
   __TEXT.__eh_frame: 0x1a08
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3090
+  __DATA_CONST.__const: 0x30b8
   __DATA_CONST.__objc_classlist: 0x9b8
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x480
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa7f0
+  __DATA_CONST.__objc_selrefs: 0xa8d8
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0x608
   __DATA_CONST.__objc_arraydata: 0x1e8
-  __DATA_CONST.__got: 0x18c8
-  __AUTH_CONST.__const: 0xac60
-  __AUTH_CONST.__cfstring: 0x5200
-  __AUTH_CONST.__objc_const: 0x44848
+  __DATA_CONST.__got: 0x18e0
+  __AUTH_CONST.__const: 0xad00
+  __AUTH_CONST.__cfstring: 0x5280
+  __AUTH_CONST.__objc_const: 0x44b38
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_doubleobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x140
   __AUTH_CONST.__auth_got: 0x2108
-  __AUTH.__objc_data: 0x82b0
+  __AUTH.__objc_data: 0x8300
   __AUTH.__data: 0x34d8
-  __DATA.__objc_ivar: 0x18d4
-  __DATA.__data: 0x4dc8
-  __DATA.__common: 0x1250
-  __DATA_DIRTY.__objc_data: 0x28a0
-  __DATA_DIRTY.__data: 0x5b8
+  __DATA.__objc_ivar: 0x18e4
+  __DATA.__data: 0x4e08
+  __DATA.__common: 0x1260
+  __DATA_DIRTY.__objc_data: 0x2908
+  __DATA_DIRTY.__data: 0x5c8
   __DATA_DIRTY.__bss: 0x3f0
   __DATA_DIRTY.__common: 0x60
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 14489
-  Symbols:   13893
-  CStrings:  1623
+  Functions: 14533
+  Symbols:   13931
+  CStrings:  1632
 
Symbols:
+ -[MRUActivityNowPlayingView compactArtworkInsetsForLeadingSize:isLimitedSize:]
+ -[MRUActivityNowPlayingViewController routeSymbolName]
+ -[MRUActivityNowPlayingViewController setRouteSymbolName:]
+ -[MRUActivityNowPlayingViewController updateArtworkPlaceholder]
+ -[MRUAmbientNowPlayingViewController backlightLuminanceDidChange]
+ -[MRUAmbientNowPlayingViewController flushAlwaysOnInvalidation]
+ -[MRUAmbientNowPlayingViewController invalidateAlwaysOnContentForReason:]
+ -[MRUAmbientNowPlayingViewController pendingAlwaysOnInvalidation]
+ -[MRUAmbientNowPlayingViewController performWithoutAnimationIfDimmed:]
+ -[MRUAmbientNowPlayingViewController setPendingAlwaysOnInvalidation:]
+ -[MRUAmbientNowPlayingVolumeControlsView contentDidChangeForReason:]
+ -[MRUAmbientNowPlayingVolumeControlsView contentDidChangeHandler]
+ -[MRUAmbientNowPlayingVolumeControlsView setContentDidChangeHandler:]
+ -[MRUFlippingArtworkLayer setPlaying:animated:]
+ -[MRUFlippingArtworkLayer updateOpacityAnimated:]
+ -[MRUFlippingArtworkLayer updateScaleAnimated:]
+ -[MRULockscreenViewController observeScreenChangesForWindowScene:]
+ -[MRULockscreenViewController screenObservedWindowScene]
+ -[MRULockscreenViewController setScreenObservedWindowScene:]
+ -[MRULockscreenViewController windowSceneDidMoveToScreen:]
+ GCC_except_table20
+ GCC_except_table26
+ GCC_except_table33
+ GCC_except_table34
+ _OBJC_IVAR_$_MRUActivityNowPlayingViewController._routeSymbolName
+ _OBJC_IVAR_$_MRUAmbientNowPlayingViewController._pendingAlwaysOnInvalidation
+ _OBJC_IVAR_$_MRUAmbientNowPlayingVolumeControlsView._contentDidChangeHandler
+ _OBJC_IVAR_$_MRULockscreenViewController._screenObservedWindowScene
+ __UIWindowHostingSceneDidMoveToScreenNotification
+ __UIWindowHostingSceneNewScreenUserInfoKey
+ __UIWindowHostingSceneOldScreenUserInfoKey
+ ___105-[MRUAmbientNowPlayingViewController nowPlayingController:metadataController:didChangeTransportControls:]_block_invoke
+ ___49-[MRUAmbientNowPlayingViewController viewDidLoad]_block_invoke
+ ___60-[MRUAmbientNowPlayingVolumeControlsView setSliderExpanded:]_block_invoke_2
+ ___65-[MRUAmbientNowPlayingVolumeControlsView updatePackageWithValue:]_block_invoke
+ ___73-[MRUAmbientNowPlayingViewController invalidateAlwaysOnContentForReason:]_block_invoke
+ ___93-[MRUAmbientNowPlayingViewController nowPlayingController:endpointController:didChangeRoute:]_block_invoke
+ ___block_descriptor_40_e8_32w_e18_v16?0"NSString"8lw32l8
+ _symbolic _____Sg So6UIViewC13MediaControlsE19AnimationParametersV
+ _symbolic _____SgXw 13MediaControls0aB17ModuleSessionViewC
- -[MRUFlippingArtworkLayer updateOpacity]
- -[MRUFlippingArtworkLayer updateScale]
CStrings:
+ "!+"
+ "!q"
+ "%{public}@ window scene moved screens: %{public}@ -> %{public}@"
+ "StandBy now playing state changed"
+ "[AOD] StandBy enqueueing timeline invalidation because %{public}@"
+ "[AOD] StandBy invalidating all timelines"
+ "routing button image changed"
+ "v16@?0@\"NSString\"8"
+ "volume slider collapsed"
+ "volume slider expanded"
- "!*"
```
