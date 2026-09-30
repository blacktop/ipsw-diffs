## ControlCenterUI

> `/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI`

```diff

-652.102.0.0.0
-  __TEXT.__text: 0x9e9d4
-  __TEXT.__auth_stubs: 0x24f0
-  __TEXT.__objc_methlist: 0x9c38
-  __TEXT.__const: 0x227a
-  __TEXT.__cstring: 0x7524
-  __TEXT.__gcc_except_tab: 0x7b4
-  __TEXT.__oslogstring: 0x32c1
+655.100.0.0.0
+  __TEXT.__text: 0xa25bc
+  __TEXT.__auth_stubs: 0x2510
+  __TEXT.__objc_methlist: 0xa068
+  __TEXT.__const: 0x233a
+  __TEXT.__cstring: 0x7ab4
+  __TEXT.__gcc_except_tab: 0x828
+  __TEXT.__oslogstring: 0x3221
   __TEXT.__dlopen_cstrs: 0x14e
-  __TEXT.__constg_swiftt: 0x23b4
-  __TEXT.__swift5_typeref: 0x24cc
-  __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_reflstr: 0x18d2
-  __TEXT.__swift5_fieldmd: 0x10bc
-  __TEXT.__swift5_assocty: 0x180
-  __TEXT.__swift5_proto: 0xd0
-  __TEXT.__swift5_types: 0x10c
-  __TEXT.__swift5_capture: 0xb9c
+  __TEXT.__constg_swiftt: 0x24fc
+  __TEXT.__swift5_typeref: 0x25ec
+  __TEXT.__swift5_builtin: 0x190
+  __TEXT.__swift5_reflstr: 0x19d2
+  __TEXT.__swift5_fieldmd: 0x116c
+  __TEXT.__swift5_assocty: 0x198
+  __TEXT.__swift5_proto: 0xd4
+  __TEXT.__swift5_types: 0x118
+  __TEXT.__swift5_capture: 0xbe0
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__unwind_info: 0x2708
+  __TEXT.__unwind_info: 0x2820
   __TEXT.__eh_frame: 0x448
-  __TEXT.__objc_classname: 0x1575
-  __TEXT.__objc_methname: 0x1ae6c
-  __TEXT.__objc_methtype: 0x7aea
-  __TEXT.__objc_stubs: 0xb760
-  __DATA_CONST.__got: 0xc18
-  __DATA_CONST.__const: 0x1160
-  __DATA_CONST.__objc_classlist: 0x360
+  __TEXT.__objc_classname: 0x15e0
+  __TEXT.__objc_methname: 0x1b896
+  __TEXT.__objc_methtype: 0x7b63
+  __TEXT.__objc_stubs: 0xbc40
+  __DATA_CONST.__got: 0xc20
+  __DATA_CONST.__const: 0x1130
+  __DATA_CONST.__objc_classlist: 0x380
   __DATA_CONST.__objc_catlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x540
+  __DATA_CONST.__objc_protolist: 0x560
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5cd0
-  __DATA_CONST.__objc_protorefs: 0x1f0
-  __DATA_CONST.__objc_superrefs: 0x1c0
+  __DATA_CONST.__objc_selrefs: 0x5ea8
+  __DATA_CONST.__objc_protorefs: 0x200
+  __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x1288
-  __AUTH_CONST.__const: 0x38a8
-  __AUTH_CONST.__cfstring: 0x2520
-  __AUTH_CONST.__objc_const: 0xedf0
+  __AUTH_CONST.__auth_got: 0x1298
+  __AUTH_CONST.__const: 0x3a18
+  __AUTH_CONST.__cfstring: 0x2800
+  __AUTH_CONST.__objc_const: 0xf5a0
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0x90
-  __AUTH.__objc_data: 0x15d8
-  __AUTH.__data: 0x708
-  __DATA.__objc_ivar: 0x62c
-  __DATA.__data: 0x3538
-  __DATA.__bss: 0x1190
+  __AUTH.__objc_data: 0x17a0
+  __AUTH.__data: 0x768
+  __DATA.__objc_ivar: 0x678
+  __DATA.__data: 0x3678
+  __DATA.__bss: 0x1210
   __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x2f50
-  __DATA_DIRTY.__data: 0xae8
+  __DATA_DIRTY.__objc_data: 0x30e8
+  __DATA_DIRTY.__data: 0xb08
   __DATA_DIRTY.__bss: 0x9f8
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 95CF920E-7657-3486-A167-53B3FFF834AE
-  Functions: 4294
-  Symbols:   9167
-  CStrings:  6130
+  UUID: 6CF3DC8C-2CA0-33FD-8212-848F3EC9A002
+  Functions: 4422
+  Symbols:   9401
+  CStrings:  6299
 
Symbols:
+ +[CCUIFluidPagingSettings settingsControllerModule]
+ +[CCUIInvokeSettings settingsControllerModule]
+ +[CCUIOverlayStatusBarPresentationProvider _accessoryScaleCAAnimationParametersForTransitionState:]
+ +[CCUIOverlayStatusBarPresentationProvider _moduleStretchAnimationParametersForTransitionState:settings:]
+ +[CCUIOverlayStatusBarPresentationProvider _moduleTranslationAnimationParametersForTransitionState:settings:]
+ +[UIView(CCUIFluidAnimatingAdditions) ccui_animateWithSettings:animations:]
+ -[CCUIControlCenterRootSettings fluidPagingSettings]
+ -[CCUIControlCenterRootSettings invokeSettings]
+ -[CCUIControlCenterRootSettings setFluidPagingSettings:]
+ -[CCUIControlCenterRootSettings setInvokeSettings:]
+ -[CCUIFluidPagingSettings .cxx_destruct]
+ -[CCUIFluidPagingSettings maxVelocityStretchScaleMagnitude]
+ -[CCUIFluidPagingSettings maxVelocityStretchScaleScalarMagnitude]
+ -[CCUIFluidPagingSettings maxVelocityStretchTranslation]
+ -[CCUIFluidPagingSettings setDefaultValues]
+ -[CCUIFluidPagingSettings setMaxVelocityStretchScaleMagnitude:]
+ -[CCUIFluidPagingSettings setMaxVelocityStretchScaleScalarMagnitude:]
+ -[CCUIFluidPagingSettings setMaxVelocityStretchTranslation:]
+ -[CCUIFluidPagingSettings setVelocityForMaxStretch:]
+ -[CCUIFluidPagingSettings setVelocityStretchAnimationSettings:]
+ -[CCUIFluidPagingSettings velocityForMaxStretch]
+ -[CCUIFluidPagingSettings velocityStretchAnimationSettings]
+ -[CCUIInvokeSettings .cxx_destruct]
+ -[CCUIInvokeSettings maxOverscrollStretchScaleMagnitude]
+ -[CCUIInvokeSettings maxVelocityStretchScaleMagnitude]
+ -[CCUIInvokeSettings maxVelocityStretchScaleScalarMagnitude]
+ -[CCUIInvokeSettings maxVelocityStretchTranslation]
+ -[CCUIInvokeSettings overscrollStretchAnimationSettings]
+ -[CCUIInvokeSettings overscrollStretchRubberbandDistance]
+ -[CCUIInvokeSettings overscrollTranslationAnimationSettings]
+ -[CCUIInvokeSettings setDefaultValues]
+ -[CCUIInvokeSettings setMaxOverscrollStretchScaleMagnitude:]
+ -[CCUIInvokeSettings setMaxVelocityStretchScaleMagnitude:]
+ -[CCUIInvokeSettings setMaxVelocityStretchScaleScalarMagnitude:]
+ -[CCUIInvokeSettings setMaxVelocityStretchTranslation:]
+ -[CCUIInvokeSettings setOverscrollStretchAnimationSettings:]
+ -[CCUIInvokeSettings setOverscrollStretchRubberbandDistance:]
+ -[CCUIInvokeSettings setOverscrollTranslationAnimationSettings:]
+ -[CCUIInvokeSettings setVelocityForMaxStretch:]
+ -[CCUIInvokeSettings setVelocityStretchAnimationSettings:]
+ -[CCUIInvokeSettings velocityForMaxStretch]
+ -[CCUIInvokeSettings velocityStretchAnimationSettings]
+ -[CCUIMainViewController addModuleStretchSourceWithParameters:]
+ -[CCUIModuleInstanceManager dealloc]
+ -[CCUIOverlayStatusBarPresentationProvider _accessoryScaleTransformForTransitionState:layoutRect:]
+ -[CCUIOverlayStatusBarPresentationProvider _maxBaseTranslation]
+ -[CCUIOverlayStatusBarPresentationProvider _moduleViewStretchPercentageForTransitionState:]
+ -[CCUIOverlayStatusBarPresentationProvider _setUpStretchSources]
+ -[CCUIOverlayStatusBarPresentationProvider _tearDownStretchSources]
+ -[CCUIOverlayStatusBarPresentationProvider _updateForScrollPositionPropertyChanged]
+ -[CCUIOverlayStatusBarPresentationProvider invokeSettings]
+ -[CCUIOverlayStatusBarPresentationProvider overscrollStretchSource]
+ -[CCUIOverlayStatusBarPresentationProvider scrollPositionProperty]
+ -[CCUIOverlayStatusBarPresentationProvider scrollVelocityStretchSource]
+ -[CCUIOverlayStatusBarPresentationProvider setInvokeSettings:]
+ -[CCUIOverlayStatusBarPresentationProvider setOverscrollStretchSource:]
+ -[CCUIOverlayStatusBarPresentationProvider setScrollPositionProperty:]
+ -[CCUIOverlayStatusBarPresentationProvider setScrollVelocityStretchSource:]
+ -[CCUIWiFiModuleViewController _glyphImageForState:currentSignalBars:network:applyConfiguration:]
+ GCC_except_table144
+ GCC_except_table151
+ GCC_except_table97
+ _CGAffineTransformDecompose
+ _CGAffineTransformMakeWithComponents
+ _OBJC_CLASS_$_CCUIFluidPagingSettings
+ _OBJC_CLASS_$_CCUIInvokeSettings
+ _OBJC_CLASS_$_CCUIStretchApplier
+ _OBJC_CLASS_$_UIViewFloatAnimatableProperty
+ _OBJC_CLASS_$__TtCE15ControlCenterUICSo18CCUIStretchApplier14_StretchSource
+ _OBJC_IVAR_$_CCUIControlCenterRootSettings._fluidPagingSettings
+ _OBJC_IVAR_$_CCUIControlCenterRootSettings._invokeSettings
+ _OBJC_IVAR_$_CCUIFluidPagingSettings._maxVelocityStretchScaleMagnitude
+ _OBJC_IVAR_$_CCUIFluidPagingSettings._maxVelocityStretchScaleScalarMagnitude
+ _OBJC_IVAR_$_CCUIFluidPagingSettings._maxVelocityStretchTranslation
+ _OBJC_IVAR_$_CCUIFluidPagingSettings._velocityForMaxStretch
+ _OBJC_IVAR_$_CCUIFluidPagingSettings._velocityStretchAnimationSettings
+ _OBJC_IVAR_$_CCUIInvokeSettings._maxOverscrollStretchScaleMagnitude
+ _OBJC_IVAR_$_CCUIInvokeSettings._maxVelocityStretchScaleMagnitude
+ _OBJC_IVAR_$_CCUIInvokeSettings._maxVelocityStretchScaleScalarMagnitude
+ _OBJC_IVAR_$_CCUIInvokeSettings._maxVelocityStretchTranslation
+ _OBJC_IVAR_$_CCUIInvokeSettings._overscrollStretchAnimationSettings
+ _OBJC_IVAR_$_CCUIInvokeSettings._overscrollStretchRubberbandDistance
+ _OBJC_IVAR_$_CCUIInvokeSettings._overscrollTranslationAnimationSettings
+ _OBJC_IVAR_$_CCUIInvokeSettings._velocityForMaxStretch
+ _OBJC_IVAR_$_CCUIInvokeSettings._velocityStretchAnimationSettings
+ _OBJC_IVAR_$_CCUIOverlayStatusBarPresentationProvider._invokeSettings
+ _OBJC_IVAR_$_CCUIOverlayStatusBarPresentationProvider._overscrollStretchSource
+ _OBJC_IVAR_$_CCUIOverlayStatusBarPresentationProvider._scrollPositionProperty
+ _OBJC_IVAR_$_CCUIOverlayStatusBarPresentationProvider._scrollVelocityStretchSource
+ _OBJC_METACLASS_$_CCUIFluidPagingSettings
+ _OBJC_METACLASS_$_CCUIInvokeSettings
+ _OBJC_METACLASS_$_CCUIStretchApplier
+ _OBJC_METACLASS_$__TtCE15ControlCenterUICSo18CCUIStretchApplier14_StretchSource
+ __DATA_CCUIStretchApplier
+ __DATA__TtCE15ControlCenterUICSo18CCUIStretchApplier14_StretchSource
+ __INSTANCE_METHODS_CCUIStretchApplier
+ __INSTANCE_METHODS__TtCE15ControlCenterUICSo18CCUIStretchApplier14_StretchSource
+ __IVARS_CCUIStretchApplier
+ __IVARS__TtC15ControlCenterUI28IconListRootFolderController
+ __IVARS__TtCE15ControlCenterUICSo18CCUIStretchApplier14_StretchSource
+ __METACLASS_DATA_CCUIStretchApplier
+ __METACLASS_DATA__TtCE15ControlCenterUICSo18CCUIStretchApplier14_StretchSource
+ __OBJC_$_CATEGORY_UIView_$_CCUIFluidAnimatingAdditions
+ __OBJC_$_CLASS_METHODS_CCUIFluidPagingSettings
+ __OBJC_$_CLASS_METHODS_CCUIInvokeSettings
+ __OBJC_$_CLASS_METHODS_UIView(CCUIFluidAnimatingAdditions|ControlCenterUI|ControlCenterUI)
+ __OBJC_$_INSTANCE_METHODS_CCUIFluidPagingSettings
+ __OBJC_$_INSTANCE_METHODS_CCUIInvokeSettings
+ __OBJC_$_INSTANCE_METHODS_SBIconView(ControlCenterUIStaging|ControlCenterUI|ControlCenterUI1)
+ __OBJC_$_INSTANCE_METHODS_UIView(CCUIFluidAnimatingAdditions|ControlCenterUI|ControlCenterUI)
+ __OBJC_$_INSTANCE_METHODS__TtC15ControlCenterUI28IconListRootFolderController(ControlCenterUI)
+ __OBJC_$_INSTANCE_VARIABLES_CCUIFluidPagingSettings
+ __OBJC_$_INSTANCE_VARIABLES_CCUIInvokeSettings
+ __OBJC_$_PROP_LIST_CCUIFluidPagingSettings
+ __OBJC_$_PROP_LIST_CCUIInvokeSettings
+ __OBJC_$_PROP_LIST_CCUIStretchSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCUIStretchSource
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CCUIStretchable
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CCUIStretchSource
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CCUIStretchable
+ __OBJC_$_PROTOCOL_REFS_CCUIStretchSource
+ __OBJC_CLASS_PROTOCOLS_$_SBIconView(ControlCenterUIStaging|ControlCenterUI|ControlCenterUI1)
+ __OBJC_CLASS_PROTOCOLS_$__TtC15ControlCenterUI28IconListRootFolderController(ControlCenterUI)
+ __OBJC_CLASS_RO_$_CCUIFluidPagingSettings
+ __OBJC_CLASS_RO_$_CCUIInvokeSettings
+ __OBJC_LABEL_PROTOCOL_$_CCUIStretchSource
+ __OBJC_LABEL_PROTOCOL_$_CCUIStretchable
+ __OBJC_METACLASS_RO_$_CCUIFluidPagingSettings
+ __OBJC_METACLASS_RO_$_CCUIInvokeSettings
+ __OBJC_PROTOCOL_$_CCUIStretchSource
+ __OBJC_PROTOCOL_$_CCUIStretchable
+ __PROPERTIES_CCUIStretchApplier
+ __PROPERTIES__TtCE15ControlCenterUICSo18CCUIStretchApplier14_StretchSource
+ __PROTOCOLS__TtCE15ControlCenterUICSo18CCUIStretchApplier14_StretchSource
+ __PROTOCOLS__TtCE15ControlCenterUICSo18CCUIStretchApplier14_StretchSource.2
+ ___64-[CCUIOverlayStatusBarPresentationProvider _setUpStretchSources]_block_invoke
+ ___77-[CCUIModuleInstanceManager _instantiateModuleWithMetadata:uniqueIdentifier:]_block_invoke.99
+ ___83-[CCUIOverlayStatusBarPresentationProvider _updateForScrollPositionPropertyChanged]_block_invoke
+ ___93-[CCUIOverlayStatusBarPresentationProvider _addModuleScaleAnimationsToBatch:transitionState:]_block_invoke
+ ___swift_memcpy24_8
+ _block_copy_helper.10
+ _block_copy_helper.102
+ _block_copy_helper.108
+ _block_copy_helper.115
+ _block_copy_helper.122
+ _block_copy_helper.129
+ _block_copy_helper.135
+ _block_copy_helper.14
+ _block_copy_helper.141
+ _block_copy_helper.148
+ _block_copy_helper.155
+ _block_copy_helper.165
+ _block_copy_helper.171
+ _block_copy_helper.177
+ _block_copy_helper.266
+ _block_copy_helper.284
+ _block_copy_helper.294
+ _block_copy_helper.305
+ _block_copy_helper.33
+ _block_copy_helper.331
+ _block_copy_helper.335
+ _block_copy_helper.341
+ _block_copy_helper.365
+ _block_copy_helper.375
+ _block_copy_helper.382
+ _block_copy_helper.385
+ _block_copy_helper.391
+ _block_copy_helper.410
+ _block_copy_helper.414
+ _block_copy_helper.417
+ _block_copy_helper.424
+ _block_copy_helper.73
+ _block_copy_helper.80
+ _block_copy_helper.86
+ _block_copy_helper.95
+ _block_descriptor.104
+ _block_descriptor.110
+ _block_descriptor.117
+ _block_descriptor.12
+ _block_descriptor.124
+ _block_descriptor.131
+ _block_descriptor.137
+ _block_descriptor.143
+ _block_descriptor.150
+ _block_descriptor.157
+ _block_descriptor.16
+ _block_descriptor.167
+ _block_descriptor.173
+ _block_descriptor.179
+ _block_descriptor.268
+ _block_descriptor.286
+ _block_descriptor.296
+ _block_descriptor.307
+ _block_descriptor.333
+ _block_descriptor.337
+ _block_descriptor.343
+ _block_descriptor.35
+ _block_descriptor.367
+ _block_descriptor.377
+ _block_descriptor.384
+ _block_descriptor.387
+ _block_descriptor.393
+ _block_descriptor.412
+ _block_descriptor.416
+ _block_descriptor.419
+ _block_descriptor.426
+ _block_descriptor.75
+ _block_descriptor.82
+ _block_descriptor.88
+ _block_descriptor.97
+ _block_destroy_helper.103
+ _block_destroy_helper.109
+ _block_destroy_helper.11
+ _block_destroy_helper.116
+ _block_destroy_helper.123
+ _block_destroy_helper.130
+ _block_destroy_helper.136
+ _block_destroy_helper.142
+ _block_destroy_helper.149
+ _block_destroy_helper.15
+ _block_destroy_helper.156
+ _block_destroy_helper.166
+ _block_destroy_helper.172
+ _block_destroy_helper.178
+ _block_destroy_helper.267
+ _block_destroy_helper.285
+ _block_destroy_helper.295
+ _block_destroy_helper.306
+ _block_destroy_helper.332
+ _block_destroy_helper.336
+ _block_destroy_helper.34
+ _block_destroy_helper.342
+ _block_destroy_helper.366
+ _block_destroy_helper.376
+ _block_destroy_helper.383
+ _block_destroy_helper.386
+ _block_destroy_helper.392
+ _block_destroy_helper.411
+ _block_destroy_helper.415
+ _block_destroy_helper.418
+ _block_destroy_helper.425
+ _block_destroy_helper.74
+ _block_destroy_helper.81
+ _block_destroy_helper.87
+ _block_destroy_helper.96
+ _convertDampingRatioAndResponseToTensionAndFriction
+ _flat unique So15CCUIStretchable_p
+ _flat unique So17CCUIStretchSource_p
+ _objc_msgSend$_accessoryScaleCAAnimationParametersForTransitionState:
+ _objc_msgSend$_accessoryScaleTransformForTransitionState:layoutRect:
+ _objc_msgSend$_createTransformerWithInputAnimatableProperties:presentationValueChangedCallback:
+ _objc_msgSend$_glyphImageForState:currentSignalBars:network:applyConfiguration:
+ _objc_msgSend$_maxBaseTranslation
+ _objc_msgSend$_moduleStretchAnimationParametersForTransitionState:settings:
+ _objc_msgSend$_moduleTranslationAnimationParametersForTransitionState:settings:
+ _objc_msgSend$_moduleViewStretchPercentageForTransitionState:
+ _objc_msgSend$_setUpStretchSources
+ _objc_msgSend$_tearDownStretchSources
+ _objc_msgSend$_updateForScrollPositionPropertyChanged
+ _objc_msgSend$addModuleStretchSourceWithParameters:
+ _objc_msgSend$ccui_animateWithSettings:animations:
+ _objc_msgSend$dampingRatio
+ _objc_msgSend$fluidPagingSettings
+ _objc_msgSend$invokeSettings
+ _objc_msgSend$isSecure
+ _objc_msgSend$maxOverscrollStretchScaleMagnitude
+ _objc_msgSend$maxVelocityStretchScaleMagnitude
+ _objc_msgSend$maxVelocityStretchScaleScalarMagnitude
+ _objc_msgSend$maxVelocityStretchTranslation
+ _objc_msgSend$overscrollStretchAnimationSettings
+ _objc_msgSend$overscrollStretchRubberbandDistance
+ _objc_msgSend$overscrollStretchSource
+ _objc_msgSend$overscrollTranslationAnimationSettings
+ _objc_msgSend$parentViewController
+ _objc_msgSend$response
+ _objc_msgSend$sb_animateWithSettings:mode:animations:completion:
+ _objc_msgSend$scrollPositionProperty
+ _objc_msgSend$scrollVelocityStretchSource
+ _objc_msgSend$setDampingRatio:
+ _objc_msgSend$setFrameRateRange:highFrameRateReason:
+ _objc_msgSend$setInvokeSettings:
+ _objc_msgSend$setMaxOverscrollStretchScaleMagnitude:
+ _objc_msgSend$setMaxVelocityStretchScaleMagnitude:
+ _objc_msgSend$setMaxVelocityStretchScaleScalarMagnitude:
+ _objc_msgSend$setMaxVelocityStretchTranslation:
+ _objc_msgSend$setOverscrollStretchRubberbandDistance:
+ _objc_msgSend$setOverscrollStretchSource:
+ _objc_msgSend$setResponse:
+ _objc_msgSend$setScrollPositionProperty:
+ _objc_msgSend$setScrollVelocityStretchSource:
+ _objc_msgSend$setStretchValue:
+ _objc_msgSend$setValue:
+ _objc_msgSend$setVelocityForMaxStretch:
+ _objc_msgSend$velocity
+ _objc_msgSend$velocityForMaxStretch
+ _objc_msgSend$velocityStretchAnimationSettings
+ _objc_msgSend$windowScene
+ _objectdestroy.31Tm
+ _objectdestroy.345Tm
+ _swift_dynamicCastClass
+ _symbolic So18CCUIInvokeSettingsC
+ _symbolic So18CCUIStretchApplierC
+ _symbolic So18CCUIStretchApplierCSg
+ _symbolic So18CCUIStretchApplierCSgXw
+ _symbolic So18SBFolderControllerCSgXw
+ _symbolic So18SBFolderControllerCSgXwz_Xx
+ _symbolic So23CCUIFluidPagingSettingsC
+ _symbolic _____ So15CCUIStretchAxisV
+ _symbolic _____ So18CCUIStretchApplierC15ControlCenterUIE14_StretchSourceC
+ _symbolic _____ So21CCUIStretchParametersV
+ _symbolic ______p So15CCUIStretchableP
+ _symbolic ______pSg So17CCUIStretchSourceP
+ _symbolic _____y_____G s11_SetStorageC So18CCUIStretchApplierC15ControlCenterUIE14_StretchSourceC
+ _type_layout_string So21CCUIStretchParametersV
- +[CCUIOverlayStatusBarPresentationProvider _moduleC2AnimationParametersForTransitionState:layoutRect:]
- +[CCUIOverlayStatusBarPresentationProvider _moduleScaleCAAnimationParametersForTransitionState:]
- -[CCUIOverlayStatusBarPresentationProvider _addPageContentTransformAnimationsToBatch:transitionState:]
- -[CCUIOverlayStatusBarPresentationProvider _moduleViewScaleTransformForTransitionState:layoutRect:]
- -[CCUIWiFiModuleViewController _connectingImage]
- -[CCUIWiFiModuleViewController _glyphImageForState:currentSignalBars:applyConfiguration:]
- -[CCUIWiFiModuleViewController connectingNetworkIdentifier]
- -[CCUIWiFiModuleViewController setConnectingNetworkIdentifier:]
- GCC_except_table143
- GCC_except_table150
- _OBJC_CLASS_$__UIImageSymbolConfiguration
- _OBJC_IVAR_$_CCUIWiFiModuleViewController._connectingNetworkIdentifier
- __INSTANCE_METHODS__TtC15ControlCenterUI28IconListRootFolderController
- __OBJC_$_CATEGORY_CLASS_METHODS_UIView_$_ControlCenterUI
- __OBJC_$_CATEGORY_UIView_$_ControlCenterUI
- __OBJC_$_INSTANCE_METHODS_SBIconView(ControlCenterUIStaging|ControlCenterUI)
- __OBJC_$_INSTANCE_METHODS_UIView(ControlCenterUI|ControlCenterUI)
- __OBJC_CLASS_PROTOCOLS_$_SBIconView(ControlCenterUIStaging|ControlCenterUI)
- ___102-[CCUIOverlayStatusBarPresentationProvider _addPageContentTransformAnimationsToBatch:transitionState:]_block_invoke
- ___77-[CCUIModuleInstanceManager _instantiateModuleWithMetadata:uniqueIdentifier:]_block_invoke.97
- _block_copy_helper.100
- _block_copy_helper.107
- _block_copy_helper.114
- _block_copy_helper.121
- _block_copy_helper.127
- _block_copy_helper.13
- _block_copy_helper.140
- _block_copy_helper.147
- _block_copy_helper.157
- _block_copy_helper.163
- _block_copy_helper.169
- _block_copy_helper.24
- _block_copy_helper.263
- _block_copy_helper.272
- _block_copy_helper.290
- _block_copy_helper.300
- _block_copy_helper.317
- _block_copy_helper.32
- _block_copy_helper.324
- _block_copy_helper.344
- _block_copy_helper.348
- _block_copy_helper.354
- _block_copy_helper.378
- _block_copy_helper.388
- _block_copy_helper.395
- _block_copy_helper.404
- _block_copy_helper.411
- _block_copy_helper.423
- _block_copy_helper.430
- _block_copy_helper.437
- _block_copy_helper.440
- _block_copy_helper.65
- _block_copy_helper.7
- _block_copy_helper.72
- _block_copy_helper.78
- _block_descriptor.102
- _block_descriptor.109
- _block_descriptor.116
- _block_descriptor.123
- _block_descriptor.129
- _block_descriptor.142
- _block_descriptor.149
- _block_descriptor.15
- _block_descriptor.159
- _block_descriptor.165
- _block_descriptor.171
- _block_descriptor.26
- _block_descriptor.265
- _block_descriptor.274
- _block_descriptor.292
- _block_descriptor.302
- _block_descriptor.319
- _block_descriptor.326
- _block_descriptor.34
- _block_descriptor.346
- _block_descriptor.350
- _block_descriptor.356
- _block_descriptor.380
- _block_descriptor.390
- _block_descriptor.397
- _block_descriptor.406
- _block_descriptor.413
- _block_descriptor.425
- _block_descriptor.432
- _block_descriptor.439
- _block_descriptor.442
- _block_descriptor.67
- _block_descriptor.74
- _block_descriptor.80
- _block_descriptor.9
- _block_destroy_helper.101
- _block_destroy_helper.108
- _block_destroy_helper.115
- _block_destroy_helper.122
- _block_destroy_helper.128
- _block_destroy_helper.14
- _block_destroy_helper.141
- _block_destroy_helper.148
- _block_destroy_helper.158
- _block_destroy_helper.164
- _block_destroy_helper.170
- _block_destroy_helper.25
- _block_destroy_helper.264
- _block_destroy_helper.273
- _block_destroy_helper.291
- _block_destroy_helper.301
- _block_destroy_helper.318
- _block_destroy_helper.325
- _block_destroy_helper.33
- _block_destroy_helper.345
- _block_destroy_helper.349
- _block_destroy_helper.355
- _block_destroy_helper.379
- _block_destroy_helper.389
- _block_destroy_helper.396
- _block_destroy_helper.405
- _block_destroy_helper.412
- _block_destroy_helper.424
- _block_destroy_helper.431
- _block_destroy_helper.438
- _block_destroy_helper.441
- _block_destroy_helper.66
- _block_destroy_helper.73
- _block_destroy_helper.79
- _block_destroy_helper.8
- _objc_msgSend$_addPageContentTransformAnimationsToBatch:transitionState:
- _objc_msgSend$_glyphImageForState:currentSignalBars:applyConfiguration:
- _objc_msgSend$_moduleScaleCAAnimationParametersForTransitionState:
- _objc_msgSend$_moduleViewScaleTransformForTransitionState:layoutRect:
- _objc_msgSend$connectingNetworkIdentifier
- _objc_msgSend$setConnectingNetworkIdentifier:
- _objc_msgSend$setOverlayPageContentAlpha:
- _objc_msgSend$setOverlayPageContentScale:
- _objc_msgSend$setOverlayPageContentTranslation:
- _objc_msgSend$setShouldExtendAreaForPagingContinuation:
- _objectdestroy.22Tm
- _objectdestroy.261Tm
- _objectdestroy.358Tm
CStrings:
+ "$"
+ "?"
+ "@"
+ "@\"<CCUIStretchSource>\""
+ "@\"<CCUIStretchSource>\"40@0:8{CCUIStretchParameters=ddd}16"
+ "@\"CCUIFluidPagingSettings\""
+ "@\"CCUIInvokeSettings\""
+ "@\"NSString\"24@0:8@\"<SBLeafIconDataSource>\"16"
+ "@\"SBHIconModel\""
+ "@\"UIViewFloatAnimatableProperty\""
+ "@40@0:8{CCUIStretchParameters=ddd}16"
+ "@44@0:8q16@24@32B40"
+ "@48@0:8{CCUIStretchParameters=ddd}16q40"
+ "CCUIFluidAnimatingAdditions"
+ "CCUIFluidPagingSettings"
+ "CCUIInvokeSettings"
+ "CCUIStretchApplier"
+ "CCUIStretchSource"
+ "CCUIStretchable"
+ "ControlCenterUI.StretchApplier"
+ "ControlCenterUI._StretchSource"
+ "Fluid Paging"
+ "Invoke"
+ "Max Overscroll Stretch"
+ "Max Velocity Stretch"
+ "Max Velocity Stretch Scalar"
+ "Max Velocity Translation"
+ "Overscroll Stretch Animation"
+ "Overscroll Translation Animation"
+ "Stretch Rubberband Distance"
+ "T@\"<CCUIStretchSource>\",&,N,V_overscrollStretchSource"
+ "T@\"<CCUIStretchSource>\",&,N,V_scrollVelocityStretchSource"
+ "T@\"CCUIFluidPagingSettings\",&,N,V_fluidPagingSettings"
+ "T@\"CCUIInvokeSettings\",&,N,V_invokeSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_overscrollStretchAnimationSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_overscrollTranslationAnimationSettings"
+ "T@\"SBFFluidBehaviorSettings\",&,N,V_velocityStretchAnimationSettings"
+ "T@\"UIViewFloatAnimatableProperty\",&,N,V_scrollPositionProperty"
+ "T@,N,&,Vstretchables"
+ "Td,N,V_maxOverscrollStretchScaleMagnitude"
+ "Td,N,V_maxVelocityStretchScaleMagnitude"
+ "Td,N,V_maxVelocityStretchScaleScalarMagnitude"
+ "Td,N,V_maxVelocityStretchTranslation"
+ "Td,N,V_overscrollStretchRubberbandDistance"
+ "Td,N,V_velocityForMaxStretch"
+ "Td,N,VstretchValue"
+ "T{CCUIStretchParameters=ddd},N,R,Vparameters"
+ "T{CGPoint=dd},N,VeffectiveScale"
+ "T{CGVector=dd},N,VeffectiveTranslation"
+ "Velocity For Max Stretch"
+ "Velocity Stretch Animation"
+ "_TtCE15ControlCenterUICSo18CCUIStretchApplier14_StretchSource"
+ "_accessoryScaleCAAnimationParametersForTransitionState:"
+ "_accessoryScaleTransformForTransitionState:layoutRect:"
+ "_createTransformerWithInputAnimatableProperties:presentationValueChangedCallback:"
+ "_fluidPagingSettings"
+ "_glyphImageForState:currentSignalBars:network:applyConfiguration:"
+ "_invokeSettings"
+ "_maxBaseTranslation"
+ "_maxOverscrollStretchScaleMagnitude"
+ "_maxVelocityStretchScaleMagnitude"
+ "_maxVelocityStretchScaleScalarMagnitude"
+ "_maxVelocityStretchTranslation"
+ "_moduleStretchAnimationParametersForTransitionState:settings:"
+ "_moduleTranslationAnimationParametersForTransitionState:settings:"
+ "_moduleViewStretchPercentageForTransitionState:"
+ "_overscrollStretchAnimationSettings"
+ "_overscrollStretchRubberbandDistance"
+ "_overscrollStretchSource"
+ "_overscrollTranslationAnimationSettings"
+ "_scrollPositionProperty"
+ "_scrollVelocityStretchSource"
+ "_setUpStretchSources"
+ "_tearDownStretchSources"
+ "_updateForScrollPositionPropertyChanged"
+ "_velocityForMaxStretch"
+ "_velocityStretchAnimationSettings"
+ "_verticalVelocity"
+ "addIcon:toListAtIndex:options:"
+ "addModuleStretchSourceWithParameters:"
+ "addStretchSourceWithParameters:primaryAxis:"
+ "applier"
+ "applyStretch"
+ "applyStretchScale:"
+ "applyStretchTo:"
+ "applyStretchTranslation:"
+ "applyWithScale:translation:to:"
+ "backdropGroupNameForActiveDataSource:"
+ "beginApplyingStretchToStretchable:"
+ "ccui_animateWithSettings:animations:"
+ "com.apple.control-center.DisplayModule"
+ "com.apple.mediaremote.controlcenter.audio"
+ "dampingRatio"
+ "effectiveScale"
+ "effectiveTranslation"
+ "endApplyingStretchToStretchable:"
+ "evaluateStretch"
+ "fluidPagingSettings"
+ "indexOfListContainingIcon:"
+ "initWithParameters:"
+ "invokeSettings"
+ "isSecure"
+ "maxOverscrollStretchScaleMagnitude"
+ "maxVelocityStretchScaleMagnitude"
+ "maxVelocityStretchScaleScalarMagnitude"
+ "maxVelocityStretchTranslation"
+ "moduleStretchApplier"
+ "negativeScrollVelocityModuleTranslationSource"
+ "overscrollStretchAnimationSettings"
+ "overscrollStretchRubberbandDistance"
+ "overscrollStretchSource"
+ "overscrollTranslationAnimationSettings"
+ "positiveScrollVelocityModuleTranslationSource"
+ "primaryAxis"
+ "removeStretchSource:"
+ "response"
+ "scrollPositionProperty"
+ "scrollVelocityModuleStretchSource"
+ "scrollVelocityStretchSource"
+ "setEffectiveScale:"
+ "setEffectiveTranslation:"
+ "setFluidPagingSettings:"
+ "setFrameRateRange:highFrameRateReason:"
+ "setInvokeSettings:"
+ "setMaxOverscrollStretchScaleMagnitude:"
+ "setMaxVelocityStretchScaleMagnitude:"
+ "setMaxVelocityStretchScaleScalarMagnitude:"
+ "setMaxVelocityStretchTranslation:"
+ "setOverscrollStretchAnimationSettings:"
+ "setOverscrollStretchRubberbandDistance:"
+ "setOverscrollStretchSource:"
+ "setOverscrollTranslationAnimationSettings:"
+ "setScrollPositionProperty:"
+ "setScrollVelocityStretchSource:"
+ "setStretchSources:"
+ "setStretchValue:"
+ "setStretchables:"
+ "setValue:"
+ "setVelocityForMaxStretch:"
+ "setVelocityStretchAnimationSettings:"
+ "stretchApplier"
+ "stretchSources"
+ "stretchValue"
+ "stretchables"
+ "tA"
+ "updateStretch"
+ "v32@0:8{CGVector=dd}16"
+ "v56@0:8{CGPoint=dd}16{CGVector=dd}32@48"
+ "velocity"
+ "velocityForMaxStretch"
+ "velocityStretchAnimationSettings"
+ "wifi.badge.lock"
+ "{CCUIStretchParameters=ddd}"
+ "{CCUIStretchParameters=ddd}16@0:8"
+ "{CGPoint=dd}"
+ "{CGRect={CGPoint=dd}{CGSize=dd}}"
+ "{CGVector=dd}"
+ "{CGVector=dd}16@0:8"
+ "{SBIconImageInfo={CGSize=dd}dd}"
- "@\"SBHIconImageAppearance\"16@0:8"
- "@\"SBHIconImageStyleConfiguration\"16@0:8"
- "@36@0:8q16@24B32"
- "CONTROL_CENTER_GAME_MODE_STATE_FORCED_OFF"
- "CONTROL_CENTER_GAME_MODE_STATE_FORCED_ON"
- "CONTROL_CENTER_GAME_MODE_STATE_OFF"
- "CONTROL_CENTER_GAME_MODE_STATE_ON"
- "CONTROL_CENTER_GAME_MODE_STATE_REQUIRED"
- "CONTROL_CENTER_GAME_MODE_STATE_UNAVAILABLE"
- "CONTROL_CENTER_GAME_MODE_STATE_UNKNOWN"
- "Calculated customHorizontalPadding is not finite %s, pageControlFrame: %s"
- "Calculated customVerticalPadding is not finite %s, pageControlFrame: %s"
- "T@\"SBHIconImageAppearance\",?,C,N"
- "T@\"SBHIconImageStyleConfiguration\",?,C,N"
- "TQ,N,V_connectingNetworkIdentifier"
- "_addPageContentTransformAnimationsToBatch:transitionState:"
- "_connectingNetworkIdentifier"
- "_glyphImageForState:currentSignalBars:applyConfiguration:"
- "_moduleScaleCAAnimationParametersForTransitionState:"
- "_moduleViewScaleTransformForTransitionState:layoutRect:"
- "_shouldExtendAreaForPagingContinuation"
- "addIcon:toListAtIndex:options:didBump:"
- "connectingNetworkIdentifier"
- "controlCenterDarkMaterial"
- "gamecontroller.fill"
- "overrideIconImageAppearance"
- "overrideIconImageStyleConfiguration"
- "roundButton"
- "setConnectingNetworkIdentifier:"
- "setOverrideIconImageAppearance:"
- "setOverrideIconImageStyleConfiguration:"
- "setShouldExtendAreaForPagingContinuation:"
- "shouldExtendAreaForPagingContinuation"
- "tQ"
- "v24@0:8@\"SBHIconImageAppearance\"16"
- "v24@0:8@\"SBHIconImageStyleConfiguration\"16"

```
