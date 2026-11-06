## CarPlay

> `/System/iOSSupport/System/Library/Frameworks/CarPlay.framework/Versions/A/CarPlay`

```diff

-542.8.0.0.0
-  __TEXT.__text: 0x5d95c
-  __TEXT.__objc_methlist: 0x9000
-  __TEXT.__const: 0x35a
-  __TEXT.__cstring: 0x5306
-  __TEXT.__oslogstring: 0x242e
-  __TEXT.__gcc_except_tab: 0x79c
+552.7.2.0.0
+  __TEXT.__text: 0x5eb90
+  __TEXT.__objc_methlist: 0x90e0
+  __TEXT.__const: 0x36a
+  __TEXT.__cstring: 0x5486
+  __TEXT.__oslogstring: 0x24ce
+  __TEXT.__gcc_except_tab: 0x794
   __TEXT.__constg_swiftt: 0x134
   __TEXT.__swift5_typeref: 0x7f
   __TEXT.__swift5_reflstr: 0x94
   __TEXT.__swift5_fieldmd: 0x64
   __TEXT.__swift5_proto: 0x4
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x1c40
+  __TEXT.__unwind_info: 0x1c78
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1cf8
-  __DATA_CONST.__objc_classlist: 0x3f0
+  __DATA_CONST.__const: 0x1d20
+  __DATA_CONST.__objc_classlist: 0x3e8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x220
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3c80
-  __DATA_CONST.__objc_protorefs: 0x100
-  __DATA_CONST.__objc_superrefs: 0x340
+  __DATA_CONST.__objc_selrefs: 0x3d18
+  __DATA_CONST.__objc_protorefs: 0x108
+  __DATA_CONST.__objc_superrefs: 0x348
   __DATA_CONST.__got: 0x680
-  __AUTH_CONST.__const: 0x988
-  __AUTH_CONST.__cfstring: 0x5300
-  __AUTH_CONST.__objc_const: 0x1f600
+  __AUTH_CONST.__const: 0x9a8
+  __AUTH_CONST.__cfstring: 0x5420
+  __AUTH_CONST.__objc_const: 0x1f880
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x650
+  __AUTH_CONST.__auth_got: 0x630
   __AUTH_CONST.__auth_ptr: 0x0
-  __AUTH.__objc_data: 0x48
-  __DATA.__objc_ivar: 0xa04
+  __AUTH.__objc_data: 0x98
+  __DATA.__objc_ivar: 0xa18
   __DATA.__data: 0x1940
-  __DATA.__bss: 0x310
+  __DATA.__bss: 0x360
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x2738
+  __DATA_DIRTY.__objc_data: 0x2698
   __DATA_DIRTY.__data: 0x1f8
   __DATA_DIRTY.__bss: 0x90
   __DATA_DIRTY.__common: 0x10

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3092
-  Symbols:   7141
-  CStrings:  955
+  Functions: 3111
+  Symbols:   7184
+  CStrings:  968
 
Symbols:
+ +[CPInterfaceController _setRemoteSupportedSelectorsForTesting:]
+ +[CPListImageRowItemCardElement _setImageSizeForAspectRatioWide:portrait:square:]
+ +[CPListImageRowItemCardElement _setMaximumImageSize:maximumFullHeightImageSize:]
+ +[CPPlaybackItemIdentifier supportsSecureCoding]
+ +[CPTabBarTemplate maximumNumberOfBarButtons]
+ -[CPButton isCollapsible]
+ -[CPButton setCollapsible:]
+ -[CPGridButton initWithTitleVariants:subtitleVariants:image:handler:]
+ -[CPGridButton setSubtitleVariants:]
+ -[CPGridButton subtitleVariants]
+ -[CPGridButton updateSubtitleVariants:]
+ -[CPGridTemplate gridButton:setSubtitleVariants:]
+ -[CPListTemplate _playableItemForMatchingIdentifier:]
+ -[CPListTemplate listTemplateWithIdentifier:requestPlaybackConfirmationForMatchingIdentifier:completionHandler:]
+ -[CPMapTemplate setPanningInterfaceVisible:]
+ -[CPPlaybackConfiguration .cxx_destruct]
+ -[CPPlaybackConfiguration initWithPreferredPresentation:playbackAction:elapsedTime:duration:requiresPlaybackConfirmation:]
+ -[CPPlaybackConfiguration playbackConfirmationBlock]
+ -[CPPlaybackConfiguration requiresPlaybackConfirmation]
+ -[CPPlaybackConfiguration setPlaybackConfirmationBlock:]
+ -[CPPlaybackItemIdentifier .cxx_destruct]
+ -[CPPlaybackItemIdentifier elementIndex]
+ -[CPPlaybackItemIdentifier encodeWithCoder:]
+ -[CPPlaybackItemIdentifier identifier]
+ -[CPPlaybackItemIdentifier initWithCoder:]
+ -[CPPlaybackItemIdentifier initWithIdentifier:]
+ -[CPPlaybackItemIdentifier initWithIdentifier:elementIndex:]
+ -[CPTabBarTemplate _clampedBarButtons:]
+ -[CPTemplateApplicationDashboardScene scene:didUpdateMapStyle:]
+ -[CPTrip destinationTimeZoneOffsetMinutesFromGMT]
+ CPBarButtonSanitizedImage
+ GCC_except_table135
+ GCC_except_table16
+ OBJC_IVAR_$_CPButton._collapsible
+ OBJC_IVAR_$_CPGridButton._subtitleVariants
+ OBJC_IVAR_$_CPMapTemplate._panningInterfaceVisible
+ OBJC_IVAR_$_CPPlaybackConfiguration._playbackConfirmationBlock
+ OBJC_IVAR_$_CPPlaybackConfiguration._requiresPlaybackConfirmation
+ OBJC_IVAR_$_CPPlaybackItemIdentifier._elementIndex
+ OBJC_IVAR_$_CPPlaybackItemIdentifier._identifier
+ _CPBarButtonMaximumImageSize
+ _CPBarButtonSanitizedImage
+ _OBJC_CLASS_$_CPPlaybackItemIdentifier
+ _OBJC_METACLASS_$_CPPlaybackItemIdentifier
+ __OBJC_$_CLASS_METHODS_CPPlaybackItemIdentifier
+ __OBJC_$_CLASS_PROP_LIST_CPPlaybackItemIdentifier
+ __OBJC_$_INSTANCE_METHODS_CPPlaybackItemIdentifier
+ __OBJC_$_INSTANCE_VARIABLES_CPPlaybackItemIdentifier
+ __OBJC_$_PROP_LIST_CPPlaybackItemIdentifier
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CPListClientTemplateDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CPPlaybackItemIdentifier
+ __OBJC_CLASS_RO_$_CPPlaybackItemIdentifier
+ __OBJC_METACLASS_RO_$_CPPlaybackItemIdentifier
+ __OBJC_PROTOCOL_REFERENCE_$_CPPlayableItem
+ ___112-[CPListTemplate listTemplateWithIdentifier:requestPlaybackConfirmationForMatchingIdentifier:completionHandler:]_block_invoke
+ ___36-[CPNavigationManager guidanceState]_block_invoke
+ ___49-[CPGridTemplate gridButton:setSubtitleVariants:]_block_invoke
+ ___53-[CPTabBarTemplate handleActionForControlIdentifier:]_block_invoke_2
+ ___66-[CPInterfaceController _configureTemplateProviderWithCompletion:]_block_invoke_10
+ ___66-[CPInterfaceController _configureTemplateProviderWithCompletion:]_block_invoke_9
+ ___73-[CPGridButton initWithTitleVariants:image:messageConfiguration:handler:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e29_v24?0"NSValue"8"NSValue"16ls32l8
+ ___block_descriptor_40_e8_32s_e41_v32?0"NSValue"8"NSValue"16"NSValue"24ls32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ _maximumFullHeightImageSize
+ _maximumImageSizeForAspectRatioPortrait
+ _maximumImageSizeForAspectRatioSquare
+ _maximumImageSizeForAspectRatioWide
+ _objc_msgSend$_clampedBarButtons:
+ _objc_msgSend$_playableItemForMatchingIdentifier:
+ _objc_msgSend$_setImageSizeForAspectRatioWide:portrait:square:
+ _objc_msgSend$_setMaximumImageSize:maximumFullHeightImageSize:
+ _objc_msgSend$destinationTimeZoneOffsetMinutesFromGMT
+ _objc_msgSend$elementIndex
+ _objc_msgSend$gridButton:setSubtitleVariants:
+ _objc_msgSend$initWithIdentifier:elementIndex:
+ _objc_msgSend$initWithPreferredPresentation:playbackAction:elapsedTime:duration:requiresPlaybackConfirmation:
+ _objc_msgSend$isCollapsible
+ _objc_msgSend$maximumNumberOfBarButtons
+ _objc_msgSend$playbackConfirmationBlock
+ _objc_msgSend$postNotificationName:object:
+ _objc_msgSend$preferredImageSizesForListImageRowItemCardElementWithAspectRatio:
+ _objc_msgSend$preferredImageSizesForListImageRowItemCardElementWithReply:
+ _objc_msgSend$requiresPlaybackConfirmation
+ _objc_msgSend$setCollapsible:
+ _objc_msgSend$setPanningInterfaceVisible:
+ _objc_msgSend$setPlaybackConfirmationBlock:
- -[CPTabBarTemplate leadingNavigationBarButtons]
- -[CPTabBarTemplate trailingNavigationBarButtons]
- -[CPTemplateApplicationDashboardScene sceneSettingsDiffAction]
- -[CPTemplateApplicationDashboardScene setSceneSettingsDiffAction:]
- -[CPTemplateApplicationInstrumentClusterScene sceneSettingsDiffAction]
- -[CPTemplateApplicationInstrumentClusterScene setSceneSettingsDiffAction:]
- -[CPTrip destinationTimeZoneOffsetFromGMT]
- -[CPUIContentStyleDiffInspector observeMapStyleWithBlock:]
- -[CPUIFrameRateLimitDiffInspector observeFrameRateLimitWithBlock:]
- -[CPUIMutableTemplateApplicationSceneSettings frameRateLimit]
- -[CPUIMutableTemplateApplicationSceneSettings mapStyle]
- -[CPUIMutableTemplateApplicationSceneSettings setFrameRateLimit:]
- -[CPUIMutableTemplateApplicationSceneSettings setMapStyle:]
- -[CPUITemplateApplicationSceneSettings frameRateLimit]
- -[CPUITemplateApplicationSceneSettings mapStyle]
- GCC_except_table132
- GCC_except_table21
- GCC_except_table74
- GCC_except_table85
- OBJC_IVAR_$_CPTemplateApplicationDashboardScene._sceneSettingsDiffAction
- OBJC_IVAR_$_CPTemplateApplicationInstrumentClusterScene._sceneSettingsDiffAction
- _OBJC_CLASS_$_CPUIContentStyleDiffInspector
- _OBJC_CLASS_$_CPUIFrameRateLimitDiffInspector
- _OBJC_CLASS_$_FBSSceneSettingsDiffInspector
- _OBJC_METACLASS_$_CPUIContentStyleDiffInspector
- _OBJC_METACLASS_$_CPUIFrameRateLimitDiffInspector
- _OBJC_METACLASS_$_FBSSceneSettingsDiffInspector
- __53-[CPTabBarTemplate handleActionForControlIdentifier:]_block_invoke
- __OBJC_$_INSTANCE_METHODS_CPUIContentStyleDiffInspector
- __OBJC_$_INSTANCE_METHODS_CPUIFrameRateLimitDiffInspector
- __OBJC_CLASS_RO_$_CPUIContentStyleDiffInspector
- __OBJC_CLASS_RO_$_CPUIFrameRateLimitDiffInspector
- __OBJC_METACLASS_RO_$_CPUIContentStyleDiffInspector
- __OBJC_METACLASS_RO_$_CPUIFrameRateLimitDiffInspector
- ___42-[CPMapTemplate isPanningInterfaceVisible]_block_invoke
- ___42-[CPMapTemplate isPanningInterfaceVisible]_block_invoke_2
- ___block_descriptor_48_e8_32s40r_e34_v16?0"<CPMapTemplateProviding>"8lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e8_v12?0B8lr40l8s32l8
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _dispatch_time
- _objc_msgSend$destinationTimeZoneOffsetFromGMT
- _objc_msgSend$hostPanInterfaceVisible:
CStrings:
+ "%@ requesting playback confirmation for %{public}@"
+ "%@ {UUID: %@, collapsible: %@, enabled: %@}"
+ "%@: %lu bar buttons provided, but a tab bar template supports %lu per side; ignoring the rest."
+ "CPButtonCollapsible"
+ "CPGridButtonSubtitleVariants"
+ "CPImageSet: encoding via PNG fallback (remoteSupportsIOSurface=%d, light surface=%@, dark surface=%@)"
+ "Failed to identify a local playable item for %@ %lu"
+ "kCPDarkContentImageKey"
+ "kCPLightContentImageKey"
+ "kCPPlaybackConfigurationRequiresPlaybackConfirmationKey"
+ "kCPPlaybackItemIdentifierElementIndexKey"
+ "kCPPlaybackItemIdentifierIdentifierKey"
+ "kCPSymbolRenderingModeKey"
+ "v24@?0@\"NSValue\"8@\"NSValue\"16"
+ "v32@?0@\"NSValue\"8@\"NSValue\"16@\"NSValue\"24"
- "CPImageSet: encoding via PNG fallback (light surface=%@, dark surface=%@)"
- "Failed to identify a local template for identifier %@"
```
