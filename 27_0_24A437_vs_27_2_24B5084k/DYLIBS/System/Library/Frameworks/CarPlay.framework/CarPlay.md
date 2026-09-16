## CarPlay

> `/System/Library/Frameworks/CarPlay.framework/CarPlay`

```diff

-542.7.0.0.0
-  __TEXT.__text: 0x6d740
-  __TEXT.__objc_methlist: 0x9ac8
+552.3.0.0.0
+  __TEXT.__text: 0x6d23c
+  __TEXT.__objc_methlist: 0x9a30
   __TEXT.__const: 0x552
-  __TEXT.__cstring: 0x5a76
-  __TEXT.__oslogstring: 0x36d6
-  __TEXT.__gcc_except_tab: 0x9bc
+  __TEXT.__cstring: 0x5ae6
+  __TEXT.__oslogstring: 0x3726
+  __TEXT.__gcc_except_tab: 0x934
   __TEXT.__constg_swiftt: 0x1f8
   __TEXT.__swift5_typeref: 0x13d
   __TEXT.__swift5_builtin: 0x50

   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x14
   __TEXT.__swift5_fieldmd: 0x7c
-  __TEXT.__unwind_info: 0x2820
+  __TEXT.__unwind_info: 0x27e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1f50
-  __DATA_CONST.__objc_classlist: 0x3f0
+  __DATA_CONST.__const: 0x1f00
+  __DATA_CONST.__objc_classlist: 0x3e0
   __DATA_CONST.__objc_catlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x2e8
+  __DATA_CONST.__objc_protolist: 0x2f8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x43b8
+  __DATA_CONST.__objc_selrefs: 0x43e0
   __DATA_CONST.__objc_protorefs: 0x160
   __DATA_CONST.__objc_superrefs: 0x348
-  __DATA_CONST.__got: 0x880
-  __AUTH_CONST.__const: 0xbc8
-  __AUTH_CONST.__cfstring: 0x5720
-  __AUTH_CONST.__objc_const: 0x215a0
+  __DATA_CONST.__got: 0x878
+  __AUTH_CONST.__const: 0xbe8
+  __AUTH_CONST.__cfstring: 0x57a0
+  __AUTH_CONST.__objc_const: 0x21650
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x7d0
+  __AUTH_CONST.__auth_got: 0x7b8
   __AUTH.__objc_data: 0x48
-  __DATA.__objc_ivar: 0xa44
-  __DATA.__data: 0x2050
+  __DATA.__objc_ivar: 0xa34
+  __DATA.__data: 0x2110
   __DATA.__common: 0x18
-  __DATA_DIRTY.__objc_data: 0x2738
+  __DATA_DIRTY.__objc_data: 0x2698
   __DATA_DIRTY.__data: 0x248
   __DATA_DIRTY.__bss: 0x90
   __DATA_DIRTY.__common: 0x10

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 3402
-  Symbols:   7939
-  CStrings:  1108
+  Functions: 3380
+  Symbols:   7915
+  CStrings:  1111
 
Symbols:
+ +[CPInterfaceController _setRemoteSupportedSelectorsForTesting:]
+ +[CPTabBarTemplate maximumNumberOfBarButtons]
+ -[CPButton isCollapsible]
+ -[CPButton setCollapsible:]
+ -[CPGridButton initWithTitleVariants:subtitleVariants:image:handler:]
+ -[CPGridButton setSubtitleVariants:]
+ -[CPGridButton subtitleVariants]
+ -[CPGridButton updateSubtitleVariants:]
+ -[CPGridTemplate gridButton:setSubtitleVariants:]
+ -[CPMapTemplate setPanningInterfaceVisible:]
+ -[CPSessionConfiguration _updateContentStyle:]
+ -[CPTabBarTemplate _clampedBarButtons:]
+ -[CPTemplateApplicationDashboardScene _setFrameRateLimit:]
+ -[CPTemplateApplicationDashboardScene scene:didUpdateFrameRateLimit:]
+ -[CPTemplateApplicationDashboardScene scene:didUpdateMapStyle:]
+ -[CPTemplateApplicationInstrumentClusterScene _setContentStyle:]
+ -[CPTemplateApplicationInstrumentClusterScene _setFrameRateLimit:]
+ -[CPTemplateApplicationInstrumentClusterScene scene:didUpdateFrameRateLimit:]
+ -[CPTemplateApplicationInstrumentClusterScene scene:didUpdateMapStyle:]
+ -[CPTemplateApplicationScene _setContentStyle:]
+ -[CPTemplateApplicationScene _setFrameRateLimit:]
+ -[CPTemplateApplicationScene scene:didUpdateFrameRateLimit:]
+ -[CPTemplateApplicationScene scene:didUpdateMapStyle:]
+ -[CPTrip destinationTimeZoneOffsetMinutesFromGMT]
+ GCC_except_table105
+ GCC_except_table120
+ GCC_except_table123
+ GCC_except_table133
+ _CRSUIFrameRateLimitUnrestricted
+ _OBJC_CLASS_$_CRSUIApplicationSceneSpecification
+ _OBJC_IVAR_$_CPButton._collapsible
+ _OBJC_IVAR_$_CPGridButton._subtitleVariants
+ _OBJC_IVAR_$_CPMapTemplate._panningInterfaceVisible
+ _OBJC_METACLASS_$_CRSUIApplicationSceneSpecification
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIFrameRateLimitObserving
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIMapStyleObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIFrameRateLimitObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIMapStyleObserving
+ __OBJC_$_PROTOCOL_REFS_CRSUIFrameRateLimitObserving
+ __OBJC_$_PROTOCOL_REFS_CRSUIMapStyleObserving
+ __OBJC_LABEL_PROTOCOL_$_CRSUIFrameRateLimitObserving
+ __OBJC_LABEL_PROTOCOL_$_CRSUIMapStyleObserving
+ __OBJC_PROTOCOL_$_CRSUIFrameRateLimitObserving
+ __OBJC_PROTOCOL_$_CRSUIMapStyleObserving
+ ___36-[CPNavigationManager guidanceState]_block_invoke
+ ___45-[CPNavigationManager routeGuidanceProviding]_block_invoke
+ ___49-[CPGridTemplate gridButton:setSubtitleVariants:]_block_invoke
+ ___49-[CPNavigationManager didUpdateActiveComponents:]_block_invoke_2
+ ___53-[CPTabBarTemplate handleActionForControlIdentifier:]_block_invoke_2
+ ___73-[CPGridButton initWithTitleVariants:image:messageConfiguration:handler:]_block_invoke_2
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ _objc_msgSend$_clampedBarButtons:
+ _objc_msgSend$_setContentStyle:
+ _objc_msgSend$_setFrameRateLimit:
+ _objc_msgSend$_updateContentStyle:
+ _objc_msgSend$addFrameRateLimitObserver:
+ _objc_msgSend$addMapStyleObserver:
+ _objc_msgSend$crsui_frameRateLimitProvider
+ _objc_msgSend$crsui_mapStyleProvider
+ _objc_msgSend$destinationTimeZoneOffsetMinutesFromGMT
+ _objc_msgSend$gridButton:setSubtitleVariants:
+ _objc_msgSend$isCollapsible
+ _objc_msgSend$maximumNumberOfBarButtons
+ _objc_msgSend$setCollapsible:
+ _objc_msgSend$setFrameRateLimit:
+ _objc_msgSend$setPanningInterfaceVisible:
- -[CPSessionConfiguration _updateContentStyleWithScene:]
- -[CPTabBarTemplate leadingNavigationBarButtons]
- -[CPTabBarTemplate trailingNavigationBarButtons]
- -[CPTemplateApplicationDashboardScene _frameRateLimit]
- -[CPTemplateApplicationDashboardScene _templateSettings]
- -[CPTemplateApplicationDashboardScene _updateFrameRateLimit]
- -[CPTemplateApplicationDashboardScene frameRateLimitInspector]
- -[CPTemplateApplicationDashboardScene sceneSettingsDiffAction]
- -[CPTemplateApplicationDashboardScene setFrameRateLimitInspector:]
- -[CPTemplateApplicationDashboardScene setSceneSettingsDiffAction:]
- -[CPTemplateApplicationInstrumentClusterScene _frameRateLimit]
- -[CPTemplateApplicationInstrumentClusterScene _mapStyle]
- -[CPTemplateApplicationInstrumentClusterScene _templateSettings]
- -[CPTemplateApplicationInstrumentClusterScene _updateContentStyle]
- -[CPTemplateApplicationInstrumentClusterScene _updateFrameRateLimit]
- -[CPTemplateApplicationInstrumentClusterScene frameRateLimitInspector]
- -[CPTemplateApplicationInstrumentClusterScene mapStyleInspector]
- -[CPTemplateApplicationInstrumentClusterScene sceneSettingsDiffAction]
- -[CPTemplateApplicationInstrumentClusterScene setFrameRateLimitInspector:]
- -[CPTemplateApplicationInstrumentClusterScene setMapStyleInspector:]
- -[CPTemplateApplicationInstrumentClusterScene setSceneSettingsDiffAction:]
- -[CPTemplateApplicationScene _frameRateLimit]
- -[CPTemplateApplicationScene _mapStyle]
- -[CPTemplateApplicationScene _templateSettings]
- -[CPTemplateApplicationScene _updateContentStyle]
- -[CPTemplateApplicationScene _updateFrameRateLimit]
- -[CPTemplateApplicationScene frameRateLimitInspector]
- -[CPTemplateApplicationScene mapStyleInspector]
- -[CPTemplateApplicationScene setFrameRateLimitInspector:]
- -[CPTemplateApplicationScene setMapStyleInspector:]
- -[CPTrip destinationTimeZoneOffsetFromGMT]
- -[CPUIContentStyleDiffInspector observeMapStyleWithBlock:]
- -[CPUIFrameRateLimitDiffInspector observeFrameRateLimitWithBlock:]
- -[CPUIMutableTemplateApplicationSceneSettings frameRateLimit]
- -[CPUIMutableTemplateApplicationSceneSettings mapStyle]
- -[CPUIMutableTemplateApplicationSceneSettings setFrameRateLimit:]
- -[CPUIMutableTemplateApplicationSceneSettings setMapStyle:]
- -[CPUITemplateApplicationSceneSettings frameRateLimit]
- -[CPUITemplateApplicationSceneSettings mapStyle]
- GCC_except_table104
- GCC_except_table132
- GCC_except_table21
- GCC_except_table85
- _OBJC_CLASS_$_CPUIContentStyleDiffInspector
- _OBJC_CLASS_$_CPUIFrameRateLimitDiffInspector
- _OBJC_CLASS_$_FBSSceneSettingsDiffInspector
- _OBJC_CLASS_$_UIApplicationStarkSceneSpecification
- _OBJC_IVAR_$_CPTemplateApplicationDashboardScene._frameRateLimitInspector
- _OBJC_IVAR_$_CPTemplateApplicationDashboardScene._sceneSettingsDiffAction
- _OBJC_IVAR_$_CPTemplateApplicationInstrumentClusterScene._frameRateLimitInspector
- _OBJC_IVAR_$_CPTemplateApplicationInstrumentClusterScene._mapStyleInspector
- _OBJC_IVAR_$_CPTemplateApplicationInstrumentClusterScene._sceneSettingsDiffAction
- _OBJC_IVAR_$_CPTemplateApplicationScene._frameRateLimitInspector
- _OBJC_IVAR_$_CPTemplateApplicationScene._mapStyleInspector
- _OBJC_METACLASS_$_CPUIContentStyleDiffInspector
- _OBJC_METACLASS_$_CPUIFrameRateLimitDiffInspector
- _OBJC_METACLASS_$_FBSSceneSettingsDiffInspector
- _OBJC_METACLASS_$_UIApplicationStarkSceneSpecification
- __OBJC_$_INSTANCE_METHODS_CPUIContentStyleDiffInspector
- __OBJC_$_INSTANCE_METHODS_CPUIFrameRateLimitDiffInspector
- __OBJC_CLASS_RO_$_CPUIContentStyleDiffInspector
- __OBJC_CLASS_RO_$_CPUIFrameRateLimitDiffInspector
- __OBJC_METACLASS_RO_$_CPUIContentStyleDiffInspector
- __OBJC_METACLASS_RO_$_CPUIFrameRateLimitDiffInspector
- ___42-[CPMapTemplate isPanningInterfaceVisible]_block_invoke
- ___42-[CPMapTemplate isPanningInterfaceVisible]_block_invoke_2
- ___58-[CPUIContentStyleDiffInspector observeMapStyleWithBlock:]_block_invoke
- ___58-[CPUIContentStyleDiffInspector observeMapStyleWithBlock:]_block_invoke_2
- ___64-[CPTemplateApplicationScene initWithSession:connectionOptions:]_block_invoke_2
- ___64-[CPTemplateApplicationScene initWithSession:connectionOptions:]_block_invoke_3
- ___66-[CPUIFrameRateLimitDiffInspector observeFrameRateLimitWithBlock:]_block_invoke
- ___66-[CPUIFrameRateLimitDiffInspector observeFrameRateLimitWithBlock:]_block_invoke_2
- ___81-[CPTemplateApplicationInstrumentClusterScene initWithSession:connectionOptions:]_block_invoke_2
- ___block_descriptor_40_e8_32bs_e12_v24?0Q8^v16ls32l8
- ___block_descriptor_48_e8_32s40r_e34_v16?0"<CPMapTemplateProviding>"8lr40l8s32l8
- ___block_descriptor_48_e8_32s40r_e8_v12?0B8lr40l8s32l8
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
- _objc_msgSend$_frameRateLimit
- _objc_msgSend$_mapStyle
- _objc_msgSend$_templateSettings
- _objc_msgSend$_updateContentStyle
- _objc_msgSend$_updateContentStyleWithScene:
- _objc_msgSend$_updateFrameRateLimit
- _objc_msgSend$destinationTimeZoneOffsetFromGMT
- _objc_msgSend$hostPanInterfaceVisible:
- _objc_msgSend$observeFrameRateLimitWithBlock:
- _objc_msgSend$observeMapStyleWithBlock:
- _objc_msgSend$observeOtherSetting:withBlock:
CStrings:
+ "%@ {UUID: %@, collapsible: %@, enabled: %@}"
+ "%@: %lu bar buttons provided, but a tab bar template supports %lu per side; ignoring the rest."
+ "CPButtonCollapsible"
+ "CPGridButtonSubtitleVariants"
+ "CPImageSet: encoding via PNG fallback (remoteSupportsIOSurface=%d, light surface=%@, dark surface=%@)"
+ "kCPSymbolRenderingModeKey"
- "CPImageSet: encoding via PNG fallback (light surface=%@, dark surface=%@)"
- "Failed to identify a local template for identifier %@"
- "v24@?0Q8^v16"
```
