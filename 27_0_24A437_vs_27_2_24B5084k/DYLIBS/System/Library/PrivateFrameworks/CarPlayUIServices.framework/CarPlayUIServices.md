## CarPlayUIServices

> `/System/Library/PrivateFrameworks/CarPlayUIServices.framework/CarPlayUIServices`

```diff

-581.7.2.0.0
-  __TEXT.__text: 0x36e50
-  __TEXT.__objc_methlist: 0x398c
-  __TEXT.__const: 0xea4
-  __TEXT.__oslogstring: 0x1818
-  __TEXT.__cstring: 0x1a13
+591.2.0.0.0
+  __TEXT.__text: 0x37f88
+  __TEXT.__objc_methlist: 0x3c54
+  __TEXT.__const: 0xf94
+  __TEXT.__oslogstring: 0x1a14
+  __TEXT.__cstring: 0x1ae3
   __TEXT.__gcc_except_tab: 0x4a4
-  __TEXT.__constg_swiftt: 0x7a4
-  __TEXT.__swift5_typeref: 0x628
-  __TEXT.__swift5_reflstr: 0x34b
-  __TEXT.__swift5_fieldmd: 0x3a0
-  __TEXT.__swift5_types: 0x58
-  __TEXT.__swift5_builtin: 0x50
+  __TEXT.__constg_swiftt: 0x840
+  __TEXT.__swift5_typeref: 0x6b6
+  __TEXT.__swift5_reflstr: 0x389
+  __TEXT.__swift5_fieldmd: 0x428
+  __TEXT.__swift5_types: 0x64
+  __TEXT.__swift5_capture: 0xf4
+  __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift5_assocty: 0xc0
+  __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0x60
-  __TEXT.__swift5_capture: 0xe4
-  __TEXT.__swift5_protos: 0x4
   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
   __TEXT.__swift_as_cont: 0xc
-  __TEXT.__unwind_info: 0x16e0
+  __TEXT.__unwind_info: 0x1780
   __TEXT.__eh_frame: 0x1d0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xb50
-  __DATA_CONST.__objc_classlist: 0x338
-  __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x1c0
+  __DATA_CONST.__const: 0xbe0
+  __DATA_CONST.__objc_classlist: 0x390
+  __DATA_CONST.__objc_catlist: 0x38
+  __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b78
-  __DATA_CONST.__objc_protorefs: 0xd0
-  __DATA_CONST.__objc_superrefs: 0x1a8
+  __DATA_CONST.__objc_selrefs: 0x1ca0
+  __DATA_CONST.__objc_protorefs: 0xf0
+  __DATA_CONST.__objc_superrefs: 0x198
   __DATA_CONST.__objc_arraydata: 0x40
-  __DATA_CONST.__got: 0x6c8
-  __AUTH_CONST.__const: 0x10d8
-  __AUTH_CONST.__cfstring: 0x14e0
-  __AUTH_CONST.__objc_const: 0x11c40
+  __DATA_CONST.__got: 0x728
+  __AUTH_CONST.__const: 0x1280
+  __AUTH_CONST.__cfstring: 0x1520
+  __AUTH_CONST.__objc_const: 0x12b08
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x960
-  __AUTH.__objc_data: 0x300
+  __AUTH_CONST.__auth_got: 0x970
+  __AUTH.__objc_data: 0x670
   __AUTH.__data: 0x668
-  __DATA.__objc_ivar: 0x388
-  __DATA.__data: 0x1630
+  __DATA.__objc_ivar: 0x394
+  __DATA.__data: 0x1880
   __DATA.__common: 0x140
-  __DATA_DIRTY.__objc_data: 0x2018
+  __DATA_DIRTY.__objc_data: 0x2020
   __DATA_DIRTY.__data: 0x168
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1687
-  Symbols:   3558
-  CStrings:  388
+  Functions: 1746
+  Symbols:   3747
+  CStrings:  398
 
Symbols:
+ +[CRSUIFrameRateLimitSceneExtension clientComponents]
+ +[CRSUIFrameRateLimitSceneExtension hostComponents]
+ +[CRSUIFrameRateLimitSceneExtension propagateToSceneWithDefinition:]
+ +[CRSUIFrameRateLimitSceneExtension settingsExtensions]
+ +[CRSUIFrameRateLimitSceneSettings configureSetting:]
+ +[CRSUIFrameRateLimitSceneSettings protocol]
+ +[CRSUIMapStyleSceneExtension clientComponents]
+ +[CRSUIMapStyleSceneExtension hostComponents]
+ +[CRSUIMapStyleSceneExtension propagateToSceneWithDefinition:]
+ +[CRSUIMapStyleSceneExtension settingsExtensions]
+ +[CRSUIMapStyleSceneSettings configureSetting:]
+ +[CRSUIMapStyleSceneSettings protocol]
+ +[CRSUIProxyApplicationSceneExtension clientComponents]
+ +[CRSUIProxyApplicationSceneExtension hostComponents]
+ +[CRSUIProxyApplicationSceneExtension settingsExtensions]
+ -[CRSUIApplicationSceneSpecification defaultExtensions]
+ -[CRSUIClusterThemeManager _isConnectionUsable]
+ -[CRSUIDashboardWidgetSceneSettings itemType]
+ -[CRSUIDashboardWidgetSceneSpecification defaultExtensions]
+ -[CRSUIFrameRateLimitSceneClientComponent .cxx_destruct]
+ -[CRSUIFrameRateLimitSceneClientComponent addFrameRateLimitObserver:]
+ -[CRSUIFrameRateLimitSceneClientComponent frameRateLimit]
+ -[CRSUIFrameRateLimitSceneClientComponent observers]
+ -[CRSUIFrameRateLimitSceneClientComponent removeFrameRateLimitObserver:]
+ -[CRSUIFrameRateLimitSceneClientComponent scene:didUpdateSettings:]
+ -[CRSUIFrameRateLimitSceneClientComponent setObservers:]
+ -[CRSUIFrameRateLimitSceneClientComponent settings]
+ -[CRSUIFrameRateLimitSceneHostComponent frameRateLimit]
+ -[CRSUIFrameRateLimitSceneHostComponent setFrameRateLimit:]
+ -[CRSUIFrameRateLimitSceneHostComponent settings]
+ -[CRSUIFrameRateLimitSceneHostComponent updateSettings:]
+ -[CRSUIInstrumentClusterSceneSpecification defaultExtensions]
+ -[CRSUIMapStyleSceneClientComponent .cxx_destruct]
+ -[CRSUIMapStyleSceneClientComponent addMapStyleObserver:]
+ -[CRSUIMapStyleSceneClientComponent mapStyle]
+ -[CRSUIMapStyleSceneClientComponent observers]
+ -[CRSUIMapStyleSceneClientComponent removeMapStyleObserver:]
+ -[CRSUIMapStyleSceneClientComponent scene:didUpdateSettings:]
+ -[CRSUIMapStyleSceneClientComponent setObservers:]
+ -[CRSUIMapStyleSceneClientComponent settings]
+ -[CRSUIMapStyleSceneHostComponent mapStyle]
+ -[CRSUIMapStyleSceneHostComponent setMapStyle:]
+ -[CRSUIMapStyleSceneHostComponent settings]
+ -[CRSUIMapStyleSceneHostComponent updateSettings:]
+ -[CRSUIMutableDashboardWidgetSceneSettings itemType]
+ -[CRSUIMutableDashboardWidgetSceneSettings setItemType:]
+ -[CRSUIProxyApplicationSceneClientComponent proxiedApplicationBundleIdentifier]
+ -[CRSUIProxyApplicationSceneClientComponent settings]
+ -[CRSUIProxyApplicationSceneHostComponent proxiedApplicationBundleIdentifier]
+ -[CRSUIProxyApplicationSceneHostComponent setProxiedApplicationBundleIdentifier:]
+ -[CRSUIProxyApplicationSceneHostComponent settings]
+ -[CRSUIProxyApplicationSceneHostComponent updateSettings:]
+ -[CRSUIProxyApplicationSceneSpecification defaultExtensions]
+ -[CRSUIResolvedWallpaper viewHandlesAppearanceChanges]
+ -[CRSUITemplateDashboardWidgetSceneSpecification defaultExtensions]
+ -[CRSUITemplateInstrumentClusterSceneSpecification defaultExtensions]
+ -[CRSUIWallpaperTraits initWithSupportsDynamicAppearance:supportsDashboardPlatterMaterials:iconLabelsRequireBackground:hideRoundedCorners:black:imageContentMode:transform:]
+ -[CRSUIWallpaperTraits transform]
+ -[CRSUIWindow scene:didUpdateMapStyle:]
+ -[FBScene(CRSUIFrameRateLimitProviding) crsui_frameRateLimitProvider]
+ -[FBScene(CRSUIMapStyleProviding) crsui_mapStyleProvider]
+ -[FBScene(CRSUIProxyApplication) crsui_proxiedApplicationBundleIdentifier]
+ -[FBScene(CRSUIProxyApplication) crsui_setProxiedApplicationBundleIdentifier:]
+ -[UIScene(CRSUIFrameRateLimitProviding) crsui_frameRateLimitProvider]
+ -[UIScene(CRSUIMapStyleProviding) crsui_mapStyleProvider]
+ -[UIScene(CRSUIProxyApplication) crsui_proxiedApplicationBundleIdentifier]
+ GCC_except_table33
+ _CGAffineTransformIdentity
+ _CGRectIsEmpty
+ _CRSUIFrameRateLimitUnrestricted
+ _NSStringFromCGAffineTransform
+ _NSStringFromCGSize
+ _OBJC_CLASS_$_CRSUIFrameRateLimitSceneClientComponent
+ _OBJC_CLASS_$_CRSUIFrameRateLimitSceneExtension
+ _OBJC_CLASS_$_CRSUIFrameRateLimitSceneHostComponent
+ _OBJC_CLASS_$_CRSUIFrameRateLimitSceneSettings
+ _OBJC_CLASS_$_CRSUIMapStyleSceneClientComponent
+ _OBJC_CLASS_$_CRSUIMapStyleSceneExtension
+ _OBJC_CLASS_$_CRSUIMapStyleSceneHostComponent
+ _OBJC_CLASS_$_CRSUIMapStyleSceneSettings
+ _OBJC_CLASS_$_CRSUIProxyApplicationSceneClientComponent
+ _OBJC_CLASS_$_CRSUIProxyApplicationSceneExtension
+ _OBJC_CLASS_$_CRSUIProxyApplicationSceneHostComponent
+ _OBJC_CLASS_$_FBSSceneComponent
+ _OBJC_CLASS_$_FBSSceneExtension
+ _OBJC_CLASS_$_FBSSettingsExtension
+ _OBJC_CLASS_$_UIScene
+ _OBJC_IVAR_$_CRSUIFrameRateLimitSceneClientComponent._observers
+ _OBJC_IVAR_$_CRSUIMapStyleSceneClientComponent._observers
+ _OBJC_IVAR_$_CRSUIWallpaperTraits._transform
+ _OBJC_METACLASS_$_CRSUIFrameRateLimitSceneClientComponent
+ _OBJC_METACLASS_$_CRSUIFrameRateLimitSceneExtension
+ _OBJC_METACLASS_$_CRSUIFrameRateLimitSceneHostComponent
+ _OBJC_METACLASS_$_CRSUIFrameRateLimitSceneSettings
+ _OBJC_METACLASS_$_CRSUIMapStyleSceneClientComponent
+ _OBJC_METACLASS_$_CRSUIMapStyleSceneExtension
+ _OBJC_METACLASS_$_CRSUIMapStyleSceneHostComponent
+ _OBJC_METACLASS_$_CRSUIMapStyleSceneSettings
+ _OBJC_METACLASS_$_CRSUIProxyApplicationSceneClientComponent
+ _OBJC_METACLASS_$_CRSUIProxyApplicationSceneExtension
+ _OBJC_METACLASS_$_CRSUIProxyApplicationSceneHostComponent
+ _OBJC_METACLASS_$_FBSSceneComponent
+ _OBJC_METACLASS_$_FBSSceneExtension
+ _OBJC_METACLASS_$_FBSSettingsExtension
+ __OBJC_$_CATEGORY_UIScene_$_CRSUIFrameRateLimitProviding
+ __OBJC_$_CLASS_METHODS_CRSUIFrameRateLimitSceneExtension
+ __OBJC_$_CLASS_METHODS_CRSUIFrameRateLimitSceneSettings
+ __OBJC_$_CLASS_METHODS_CRSUIMapStyleSceneExtension
+ __OBJC_$_CLASS_METHODS_CRSUIMapStyleSceneSettings
+ __OBJC_$_CLASS_METHODS_CRSUIProxyApplicationSceneExtension
+ __OBJC_$_INSTANCE_METHODS_CRSUIFrameRateLimitSceneClientComponent
+ __OBJC_$_INSTANCE_METHODS_CRSUIFrameRateLimitSceneHostComponent
+ __OBJC_$_INSTANCE_METHODS_CRSUIMapStyleSceneClientComponent
+ __OBJC_$_INSTANCE_METHODS_CRSUIMapStyleSceneHostComponent
+ __OBJC_$_INSTANCE_METHODS_CRSUIProxyApplicationSceneClientComponent
+ __OBJC_$_INSTANCE_METHODS_CRSUIProxyApplicationSceneHostComponent
+ __OBJC_$_INSTANCE_METHODS_FBScene(InstrumentClusterSceneSettings|CRSUIFrameRateLimitProviding|CRSUIMapStyleProviding|CRSUIProxyApplication)
+ __OBJC_$_INSTANCE_METHODS_UIScene(CRSUIFrameRateLimitProviding|CRSUIMapStyleProviding|CRSUIProxyApplication)
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIFrameRateLimitSceneClientComponent
+ __OBJC_$_INSTANCE_VARIABLES_CRSUIMapStyleSceneClientComponent
+ __OBJC_$_PROP_LIST_CRSUIFrameRateLimitProvidingClient
+ __OBJC_$_PROP_LIST_CRSUIFrameRateLimitProvidingHost
+ __OBJC_$_PROP_LIST_CRSUIFrameRateLimitSceneClientComponent
+ __OBJC_$_PROP_LIST_CRSUIFrameRateLimitSceneHostComponent
+ __OBJC_$_PROP_LIST_CRSUIFrameRateLimitSceneSettings
+ __OBJC_$_PROP_LIST_CRSUIMapStyleProvidingClient
+ __OBJC_$_PROP_LIST_CRSUIMapStyleProvidingHost
+ __OBJC_$_PROP_LIST_CRSUIMapStyleSceneClientComponent
+ __OBJC_$_PROP_LIST_CRSUIMapStyleSceneHostComponent
+ __OBJC_$_PROP_LIST_CRSUIMapStyleSceneSettings
+ __OBJC_$_PROP_LIST_CRSUIProxyApplicationSceneSettingsExtension
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIFrameRateLimitObserving
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIFrameRateLimitProvidingClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIFrameRateLimitProvidingHost
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIFrameRateLimitSceneSettings
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIMapStyleObserving
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIMapStyleProvidingClient
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIMapStyleProvidingHost
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIMapStyleSceneSettings
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIProxyApplicationSceneSettingsExtension
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_FBSSceneObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIFrameRateLimitObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIFrameRateLimitProvidingClient
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIFrameRateLimitProvidingHost
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIFrameRateLimitSceneSettings
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIMapStyleObserving
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIMapStyleProvidingClient
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIMapStyleProvidingHost
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIMapStyleSceneSettings
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIProxyApplicationSceneSettingsExtension
+ __OBJC_$_PROTOCOL_METHOD_TYPES_FBSSceneObserver
+ __OBJC_$_PROTOCOL_REFS_CRSUIFrameRateLimitObserving
+ __OBJC_$_PROTOCOL_REFS_CRSUIFrameRateLimitProvidingClient
+ __OBJC_$_PROTOCOL_REFS_CRSUIFrameRateLimitProvidingHost
+ __OBJC_$_PROTOCOL_REFS_CRSUIFrameRateLimitSceneSettings
+ __OBJC_$_PROTOCOL_REFS_CRSUIMapStyleObserving
+ __OBJC_$_PROTOCOL_REFS_CRSUIMapStyleProvidingClient
+ __OBJC_$_PROTOCOL_REFS_CRSUIMapStyleProvidingHost
+ __OBJC_$_PROTOCOL_REFS_CRSUIMapStyleSceneSettings
+ __OBJC_$_PROTOCOL_REFS_CRSUIProxyApplicationSceneSettingsExtension
+ __OBJC_$_PROTOCOL_REFS_FBSSceneObserver
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIFrameRateLimitSceneClientComponent
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIFrameRateLimitSceneHostComponent
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIMapStyleSceneClientComponent
+ __OBJC_CLASS_PROTOCOLS_$_CRSUIMapStyleSceneHostComponent
+ __OBJC_CLASS_RO_$_CRSUIFrameRateLimitSceneClientComponent
+ __OBJC_CLASS_RO_$_CRSUIFrameRateLimitSceneExtension
+ __OBJC_CLASS_RO_$_CRSUIFrameRateLimitSceneHostComponent
+ __OBJC_CLASS_RO_$_CRSUIFrameRateLimitSceneSettings
+ __OBJC_CLASS_RO_$_CRSUIMapStyleSceneClientComponent
+ __OBJC_CLASS_RO_$_CRSUIMapStyleSceneExtension
+ __OBJC_CLASS_RO_$_CRSUIMapStyleSceneHostComponent
+ __OBJC_CLASS_RO_$_CRSUIMapStyleSceneSettings
+ __OBJC_CLASS_RO_$_CRSUIProxyApplicationSceneClientComponent
+ __OBJC_CLASS_RO_$_CRSUIProxyApplicationSceneExtension
+ __OBJC_CLASS_RO_$_CRSUIProxyApplicationSceneHostComponent
+ __OBJC_LABEL_PROTOCOL_$_CRSUIFrameRateLimitObserving
+ __OBJC_LABEL_PROTOCOL_$_CRSUIFrameRateLimitProvidingClient
+ __OBJC_LABEL_PROTOCOL_$_CRSUIFrameRateLimitProvidingHost
+ __OBJC_LABEL_PROTOCOL_$_CRSUIFrameRateLimitSceneSettings
+ __OBJC_LABEL_PROTOCOL_$_CRSUIMapStyleObserving
+ __OBJC_LABEL_PROTOCOL_$_CRSUIMapStyleProvidingClient
+ __OBJC_LABEL_PROTOCOL_$_CRSUIMapStyleProvidingHost
+ __OBJC_LABEL_PROTOCOL_$_CRSUIMapStyleSceneSettings
+ __OBJC_LABEL_PROTOCOL_$_CRSUIProxyApplicationSceneSettingsExtension
+ __OBJC_LABEL_PROTOCOL_$_FBSSceneObserver
+ __OBJC_METACLASS_RO_$_CRSUIFrameRateLimitSceneClientComponent
+ __OBJC_METACLASS_RO_$_CRSUIFrameRateLimitSceneExtension
+ __OBJC_METACLASS_RO_$_CRSUIFrameRateLimitSceneHostComponent
+ __OBJC_METACLASS_RO_$_CRSUIFrameRateLimitSceneSettings
+ __OBJC_METACLASS_RO_$_CRSUIMapStyleSceneClientComponent
+ __OBJC_METACLASS_RO_$_CRSUIMapStyleSceneExtension
+ __OBJC_METACLASS_RO_$_CRSUIMapStyleSceneHostComponent
+ __OBJC_METACLASS_RO_$_CRSUIMapStyleSceneSettings
+ __OBJC_METACLASS_RO_$_CRSUIProxyApplicationSceneClientComponent
+ __OBJC_METACLASS_RO_$_CRSUIProxyApplicationSceneExtension
+ __OBJC_METACLASS_RO_$_CRSUIProxyApplicationSceneHostComponent
+ __OBJC_PROTOCOL_$_CRSUIFrameRateLimitObserving
+ __OBJC_PROTOCOL_$_CRSUIFrameRateLimitProvidingClient
+ __OBJC_PROTOCOL_$_CRSUIFrameRateLimitProvidingHost
+ __OBJC_PROTOCOL_$_CRSUIFrameRateLimitSceneSettings
+ __OBJC_PROTOCOL_$_CRSUIMapStyleObserving
+ __OBJC_PROTOCOL_$_CRSUIMapStyleProvidingClient
+ __OBJC_PROTOCOL_$_CRSUIMapStyleProvidingHost
+ __OBJC_PROTOCOL_$_CRSUIMapStyleSceneSettings
+ __OBJC_PROTOCOL_$_CRSUIProxyApplicationSceneSettingsExtension
+ __OBJC_PROTOCOL_$_FBSSceneObserver
+ __OBJC_PROTOCOL_REFERENCE_$_CRSUIFrameRateLimitObserving
+ __OBJC_PROTOCOL_REFERENCE_$_CRSUIFrameRateLimitSceneSettings
+ __OBJC_PROTOCOL_REFERENCE_$_CRSUIMapStyleObserving
+ __OBJC_PROTOCOL_REFERENCE_$_CRSUIMapStyleSceneSettings
+ __OBJC_PROTOCOL_REFERENCE_$_CRSUIProxyApplicationSceneSettingsExtension
+ ___47-[CRSUIMapStyleSceneHostComponent setMapStyle:]_block_invoke
+ ___59-[CRSUIFrameRateLimitSceneHostComponent setFrameRateLimit:]_block_invoke
+ ___81-[CRSUIProxyApplicationSceneHostComponent setProxiedApplicationBundleIdentifier:]_block_invoke
+ ___block_descriptor_40_e61_v16?0"FBSMutableSceneSettings<CRSUIMapStyleSceneSettings>"8l
+ ___block_descriptor_40_e67_v16?0"FBSMutableSceneSettings<CRSUIFrameRateLimitSceneSettings>"8l
+ ___block_descriptor_40_e8_32s_e78_v16?0"FBSMutableSceneSettings<CRSUIProxyApplicationSceneSettingsExtension>"8ls32l8
+ ___block_descriptor_56_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_65_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___swift_memcpy24_8
+ ___swift_memcpy4_4
+ ___swift_memcpy9_8
+ __os_log_debug_impl
+ _objc_msgSend$_isConnectionUsable
+ _objc_msgSend$_sceneForFBSScene:
+ _objc_msgSend$addMapStyleObserver:
+ _objc_msgSend$clusterThemeManager:didUpdateExtraAssetsURL:assetVersion:
+ _objc_msgSend$componentForExtension:ofClass:
+ _objc_msgSend$containsProperty:
+ _objc_msgSend$crsui_mapStyleProvider
+ _objc_msgSend$decodeCGAffineTransformForKey:
+ _objc_msgSend$encodeCGAffineTransform:forKey:
+ _objc_msgSend$extensionForProtocol:
+ _objc_msgSend$frameRateLimit
+ _objc_msgSend$hostScene
+ _objc_msgSend$initWithSupportsDynamicAppearance:supportsDashboardPlatterMaterials:iconLabelsRequireBackground:hideRoundedCorners:black:imageContentMode:transform:
+ _objc_msgSend$matchesProperty:
+ _objc_msgSend$proxiedApplicationBundleIdentifierNew
+ _objc_msgSend$scene
+ _objc_msgSend$scene:didUpdateFrameRateLimit:
+ _objc_msgSend$scene:didUpdateMapStyle:
+ _objc_msgSend$setDefaultValue:
+ _objc_msgSend$setFrameRateLimit:
+ _objc_msgSend$setMapStyle:
+ _objc_msgSend$setNullPreserving:
+ _objc_msgSend$setPropagating:
+ _objc_msgSend$setProxiedApplicationBundleIdentifier:
+ _objc_msgSend$setProxiedApplicationBundleIdentifierNew:
+ _objc_msgSend$settingsDiff
+ _objc_msgSend$transform
+ _objc_msgSend$updateSettings:
+ _symbolic $s17CarPlayUIServices19CRSUIIconImageStoreP
+ _symbolic SDySSSo6ISIconCG
+ _symbolic So7UIImageC
+ _symbolic _____ 17CarPlayUIServices14CRSUIIconImageV
+ _symbolic _____ 17CarPlayUIServices14ImageMapISIcon33_1D7B3B656E236C8479D65891BF38C1AFLLC11CachedIconsV
+ _symbolic _____ So16os_unfair_lock_sV
+ _symbolic _____ s6UInt32V
+ _symbolic _____Sg___________tc 17CarPlayUIServices14CRSUIIconImageV So19IFAppearanceVariantV So0F0V
+ _symbolic __________So7UIImageCSgIegyyo_ So19IFAppearanceVariantV So0A0V
+ _symbolic ______pSg 17CarPlayUIServices19CRSUIIconImageStoreP
+ _symbolic _____ySSSo6ISIconCG s18_DictionaryStorageC
+ _symbolic _____y_____G 2os21OSAllocatedUnfairLockV 17CarPlayUIServices14ImageMapISIcon33_1D7B3B656E236C8479D65891BF38C1AFLLC11CachedIconsV
+ _symbolic _____y__________G s13ManagedBufferCsRi__rlE 17CarPlayUIServices14ImageMapISIcon33_1D7B3B656E236C8479D65891BF38C1AFLLC11CachedIconsV So16os_unfair_lock_sV
+ _type_layout_string 17CarPlayUIServices14CRSUIIconImageV
+ _type_layout_string 17CarPlayUIServices14ImageMapISIcon33_1D7B3B656E236C8479D65891BF38C1AFLLC11CachedIconsV
+ _type_layout_string So16os_unfair_lock_sV
- -[CRSUIApplicationSceneSettings frameRateLimit]
- -[CRSUIApplicationSceneSettings mapStyle]
- -[CRSUIApplicationSceneSettingsDiffInspector observeFrameRateLimitWithBlock:]
- -[CRSUIApplicationSceneSettingsDiffInspector observeMapStyleWithBlock:]
- -[CRSUIDashboardWidgetSceneSettings frameRateLimit]
- -[CRSUIDashboardWidgetSceneSettings mapStyle]
- -[CRSUIInstrumentClusterSceneSettings frameRateLimit]
- -[CRSUIInstrumentClusterSceneSettings mapStyle]
- -[CRSUIMutableApplicationSceneSettings frameRateLimit]
- -[CRSUIMutableApplicationSceneSettings mapStyle]
- -[CRSUIMutableApplicationSceneSettings setFrameRateLimit:]
- -[CRSUIMutableApplicationSceneSettings setMapStyle:]
- -[CRSUIMutableDashboardWidgetSceneSettings frameRateLimit]
- -[CRSUIMutableDashboardWidgetSceneSettings mapStyle]
- -[CRSUIMutableDashboardWidgetSceneSettings setFrameRateLimit:]
- -[CRSUIMutableDashboardWidgetSceneSettings setMapStyle:]
- -[CRSUIMutableInstrumentClusterSceneSettings frameRateLimit]
- -[CRSUIMutableInstrumentClusterSceneSettings mapStyle]
- -[CRSUIMutableInstrumentClusterSceneSettings setFrameRateLimit:]
- -[CRSUIMutableInstrumentClusterSceneSettings setMapStyle:]
- -[CRSUIMutableProxyApplicationSceneSettings frameRateLimit]
- -[CRSUIMutableProxyApplicationSceneSettings mapStyle]
- -[CRSUIMutableProxyApplicationSceneSettings setFrameRateLimit:]
- -[CRSUIMutableProxyApplicationSceneSettings setMapStyle:]
- -[CRSUIMutableTemplateDashboardWidgetSceneSettings proxiedApplicationBundleIdentifier]
- -[CRSUIMutableTemplateDashboardWidgetSceneSettings setProxiedApplicationBundleIdentifier:]
- -[CRSUIMutableTemplateInstrumentClusterSceneSettings description]
- -[CRSUIMutableTemplateInstrumentClusterSceneSettings proxiedApplicationBundleIdentifier]
- -[CRSUIMutableTemplateInstrumentClusterSceneSettings setProxiedApplicationBundleIdentifier:]
- -[CRSUIProxyApplicationSceneSettings frameRateLimit]
- -[CRSUIProxyApplicationSceneSettings mapStyle]
- -[CRSUITemplateDashboardWidgetSceneSettings proxiedApplicationBundleIdentifier]
- -[CRSUITemplateInstrumentClusterSceneSettings description]
- -[CRSUITemplateInstrumentClusterSceneSettings proxiedApplicationBundleIdentifier]
- -[CRSUIWallpaperTraits initWithSupportsDynamicAppearance:supportsDashboardPlatterMaterials:iconLabelsRequireBackground:hideRoundedCorners:black:imageContentMode:]
- -[CRSUIWindow _mapSettings]
- -[CRSUIWindow _updateMapStyleTrait]
- GCC_except_table31
- __OBJC_$_CATEGORY_INSTANCE_METHODS_FBScene_$_InstrumentClusterSceneSettings
- __OBJC_$_PROP_LIST_CRSUIFrameRateLimitProviding
- __OBJC_$_PROP_LIST_CRSUIMapStyleProviding
- __OBJC_$_PROP_LIST_CRSUIMutableFrameRateLimitProviding
- __OBJC_$_PROP_LIST_CRSUIMutableMapStyleProviding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIFrameRateLimitProviding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIMapStyleProviding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIMutableFrameRateLimitProviding
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_CRSUIMutableMapStyleProviding
- __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIFrameRateLimitProviding
- __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIMapStyleProviding
- __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIMutableFrameRateLimitProviding
- __OBJC_$_PROTOCOL_METHOD_TYPES_CRSUIMutableMapStyleProviding
- __OBJC_$_PROTOCOL_REFS_CRSUIApplicationSceneSettings
- __OBJC_$_PROTOCOL_REFS_CRSUIFrameRateLimitProviding
- __OBJC_$_PROTOCOL_REFS_CRSUIInstrumentClusterSceneSettings
- __OBJC_$_PROTOCOL_REFS_CRSUIMapStyleProviding
- __OBJC_$_PROTOCOL_REFS_CRSUIMutableFrameRateLimitProviding
- __OBJC_$_PROTOCOL_REFS_CRSUIMutableMapStyleProviding
- __OBJC_$_PROTOCOL_REFS_CRSUIProxyApplicationSceneSettings
- __OBJC_LABEL_PROTOCOL_$_CRSUIFrameRateLimitProviding
- __OBJC_LABEL_PROTOCOL_$_CRSUIMapStyleProviding
- __OBJC_LABEL_PROTOCOL_$_CRSUIMutableFrameRateLimitProviding
- __OBJC_LABEL_PROTOCOL_$_CRSUIMutableMapStyleProviding
- __OBJC_PROTOCOL_$_CRSUIFrameRateLimitProviding
- __OBJC_PROTOCOL_$_CRSUIMapStyleProviding
- __OBJC_PROTOCOL_$_CRSUIMutableFrameRateLimitProviding
- __OBJC_PROTOCOL_$_CRSUIMutableMapStyleProviding
- __OBJC_PROTOCOL_REFERENCE_$_CRSUIMapStyleProviding
- ___25-[CRSUIWindow commonInit]_block_invoke_2
- ___71-[CRSUIApplicationSceneSettingsDiffInspector observeMapStyleWithBlock:]_block_invoke
- ___77-[CRSUIApplicationSceneSettingsDiffInspector observeFrameRateLimitWithBlock:]_block_invoke
- ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
- _objc_msgSend$_mapSettings
- _objc_msgSend$_updateMapStyleTrait
- _objc_msgSend$clusterThemeManager:didUpdateExtraAssetsURL:
- _objc_msgSend$initWithSupportsDynamicAppearance:supportsDashboardPlatterMaterials:iconLabelsRequireBackground:hideRoundedCorners:black:imageContentMode:
- _objc_msgSend$observeMapStyleWithBlock:
- _symbolic SDy_____So6ISIconCG 10Foundation4UUIDV
- _symbolic So7UIImageCSg___________tc So19IFAppearanceVariantV So0A0V
- _symbolic _____y_____So6ISIconCG s18_DictionaryStorageC 10Foundation4UUIDV
CStrings:
+ "(initial)"
+ "<CRSUICAPackageView> Skipping layout with empty bounds (package size %{public}@)"
+ "[Appearance-Flip] <CRSUICAPackageView %p %.0fx%.0f> setState %{public}@ -> %{public}@ animated=%{public}@ %.1fms"
+ "[Appearance-Flip] <CRSUICAPackageView %p %.0fx%.0f> setState %{public}@ NOT FOUND in package, appearance unchanged"
+ "[Appearance-Flip] <CRSUICAPackageView %p %.0fx%.0f> setState nil (reset to initial) %.1fms"
+ "[Appearance-Flip] <CRSUICAPackageView %p %.0fx%.0f> trait -> %{public}@, self-flipping state -> %{public}@"
+ "transform"
+ "unspecified"
+ "v16@?0@\"FBSMutableSceneSettings<CRSUIFrameRateLimitSceneSettings>\"8"
+ "v16@?0@\"FBSMutableSceneSettings<CRSUIMapStyleSceneSettings>\"8"
+ "v16@?0@\"FBSMutableSceneSettings<CRSUIProxyApplicationSceneSettingsExtension>\"8"
- "%@: proxied bundle identifier: %@"
```
