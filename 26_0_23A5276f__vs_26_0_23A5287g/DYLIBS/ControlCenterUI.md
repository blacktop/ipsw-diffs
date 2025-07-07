## ControlCenterUI

> `/System/Library/PrivateFrameworks/ControlCenterUI.framework/ControlCenterUI`

```diff

-649.101.0.0.0
-  __TEXT.__text: 0x9d754
-  __TEXT.__auth_stubs: 0x24b0
-  __TEXT.__objc_methlist: 0x9af0
-  __TEXT.__const: 0x224a
-  __TEXT.__cstring: 0x74f4
-  __TEXT.__gcc_except_tab: 0x78c
-  __TEXT.__oslogstring: 0x3221
+649.104.102.0.0
+  __TEXT.__text: 0x9e880
+  __TEXT.__auth_stubs: 0x24f0
+  __TEXT.__objc_methlist: 0x9bf8
+  __TEXT.__const: 0x227a
+  __TEXT.__cstring: 0x7524
+  __TEXT.__gcc_except_tab: 0x7b4
+  __TEXT.__oslogstring: 0x32c1
   __TEXT.__dlopen_cstrs: 0x14e
-  __TEXT.__constg_swiftt: 0x239c
-  __TEXT.__swift5_typeref: 0x24a2
+  __TEXT.__constg_swiftt: 0x23b4
+  __TEXT.__swift5_typeref: 0x24cc
   __TEXT.__swift5_builtin: 0x168
-  __TEXT.__swift5_reflstr: 0x18a2
-  __TEXT.__swift5_fieldmd: 0x10b0
+  __TEXT.__swift5_reflstr: 0x18d2
+  __TEXT.__swift5_fieldmd: 0x10bc
   __TEXT.__swift5_assocty: 0x180
   __TEXT.__swift5_proto: 0xd0
   __TEXT.__swift5_types: 0x10c
-  __TEXT.__swift5_capture: 0xb8c
+  __TEXT.__swift5_capture: 0xb9c
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__unwind_info: 0x26b0
-  __TEXT.__eh_frame: 0x420
-  __TEXT.__objc_classname: 0x155e
-  __TEXT.__objc_methname: 0x1aba8
-  __TEXT.__objc_methtype: 0x7aa8
-  __TEXT.__objc_stubs: 0xb660
-  __DATA_CONST.__got: 0xc10
+  __TEXT.__unwind_info: 0x26f0
+  __TEXT.__eh_frame: 0x448
+  __TEXT.__objc_classname: 0x1575
+  __TEXT.__objc_methname: 0x1ad94
+  __TEXT.__objc_methtype: 0x7abc
+  __TEXT.__objc_stubs: 0xb740
+  __DATA_CONST.__got: 0xc18
   __DATA_CONST.__const: 0x1138
   __DATA_CONST.__objc_classlist: 0x360
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x540
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5c58
+  __DATA_CONST.__objc_selrefs: 0x5ca8
   __DATA_CONST.__objc_protorefs: 0x1f0
   __DATA_CONST.__objc_superrefs: 0x1c0
   __DATA_CONST.__objc_arraydata: 0x68
-  __AUTH_CONST.__auth_got: 0x1268
-  __AUTH_CONST.__const: 0x3880
+  __AUTH_CONST.__auth_got: 0x1288
+  __AUTH_CONST.__const: 0x38a8
   __AUTH_CONST.__cfstring: 0x2520
-  __AUTH_CONST.__objc_const: 0xecf0
+  __AUTH_CONST.__objc_const: 0xedb8
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH.__objc_data: 0x15d8
   __AUTH.__data: 0x708
-  __DATA.__objc_ivar: 0x620
-  __DATA.__data: 0x3508
+  __DATA.__objc_ivar: 0x62c
+  __DATA.__data: 0x3538
   __DATA.__bss: 0x1190
   __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x2f30
-  __DATA_DIRTY.__data: 0xad8
+  __DATA_DIRTY.__objc_data: 0x2f50
+  __DATA_DIRTY.__data: 0xae8
   __DATA_DIRTY.__bss: 0x9f8
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 1C3591D9-290F-3D25-A731-5F4D98218B98
-  Functions: 4258
-  Symbols:   9114
-  CStrings:  6105
+  UUID: 5CB6C00F-1E98-37F4-BBBD-5936BDF7DEBB
+  Functions: 4289
+  Symbols:   9155
+  CStrings:  6124
 
Symbols:
+ -[CCUIContentModuleContainerViewController activePointerRegions]
+ -[CCUIContentModuleContainerViewController allowsGlassGrouping]
+ -[CCUIContentModuleContainerViewController isPointerActive]
+ -[CCUIContentModuleContainerViewController pointerInteraction:willEnterRegion:animator:]
+ -[CCUIContentModuleContainerViewController pointerInteraction:willExitRegion:animator:]
+ -[CCUIContentModuleContainerViewController setAllowsGlassGrouping:]
+ -[CCUIContentModuleContentContainerView allowsGlassGrouping]
+ -[CCUIContentModuleContentContainerView setAllowsGlassGrouping:]
+ -[CCUIHeaderPocketView inactiveMicrophoneAttributionChanged:]
+ -[CCUIMainViewController _getCameraSensorActivityData:micSensorActivityData:isMutedMic:isInactiveMicModeSelection:]
+ -[CCUIMainViewController contentModuleContextRequestsMutedMicrophoneSensorActivityData:]
+ -[CCUIModuleAlertViewController pointerDidExitContentModuleContainerViewController:]
+ -[CCUIModuleAlertViewController pointerWillEnterContentModuleContainerViewController:]
+ -[CCUIModuleInstanceManager contentModuleContextRequestsMutedMicrophoneSensorActivityData:]
+ -[CCUISensorAttributionCompactControl inactiveMicrophoneAttributionChanged:]
+ -[SBIconView(ControlCenterUIStaging) ccui_disallowGlassGroupingForReason:]
+ GCC_except_table150
+ _OBJC_CLASS_$_NSCountedSet
+ _OBJC_IVAR_$_CCUIContentModuleContainerViewController._activePointerRegions
+ _OBJC_IVAR_$_CCUIContentModuleContainerViewController._allowsGlassGrouping
+ _OBJC_IVAR_$_CCUIContentModuleContentContainerView._allowsGlassGrouping
+ _OBJC_IVAR_$_CCUISensorAttributionCompactControl._displayedInactiveMicrophoneAttribution
+ _OBJC_IVAR_$_CCUISensorAttributionCompactControl._inactiveMicrophoneAttribution
+ __OBJC_$_CATEGORY_SBIconView_$_ControlCenterUIStaging
+ __OBJC_$_INSTANCE_METHODS_SBIconView(ControlCenterUIStaging|ControlCenterUI)
+ __OBJC_CLASS_PROTOCOLS_$_SBIconView(ControlCenterUIStaging|ControlCenterUI)
+ ___115-[CCUIMainViewController _getCameraSensorActivityData:micSensorActivityData:isMutedMic:isInactiveMicModeSelection:]_block_invoke
+ ___115-[CCUIMainViewController _getCameraSensorActivityData:micSensorActivityData:isMutedMic:isInactiveMicModeSelection:]_block_invoke.128
+ ___115-[CCUIMainViewController _getCameraSensorActivityData:micSensorActivityData:isMutedMic:isInactiveMicModeSelection:]_block_invoke_2
+ ___115-[CCUIMainViewController _getCameraSensorActivityData:micSensorActivityData:isMutedMic:isInactiveMicModeSelection:]_block_invoke_2.132
+ ___115-[CCUIMainViewController _getCameraSensorActivityData:micSensorActivityData:isMutedMic:isInactiveMicModeSelection:]_block_invoke_3
+ ___87-[CCUIContentModuleContainerViewController pointerInteraction:willExitRegion:animator:]_block_invoke
+ ___block_literal_global.138
+ _block_copy_helper.263
+ _block_copy_helper.272
+ _block_copy_helper.290
+ _block_copy_helper.300
+ _block_copy_helper.311
+ _block_copy_helper.317
+ _block_copy_helper.324
+ _block_copy_helper.344
+ _block_copy_helper.348
+ _block_copy_helper.354
+ _block_copy_helper.378
+ _block_copy_helper.388
+ _block_copy_helper.395
+ _block_copy_helper.398
+ _block_copy_helper.404
+ _block_copy_helper.411
+ _block_copy_helper.423
+ _block_copy_helper.427
+ _block_copy_helper.430
+ _block_copy_helper.437
+ _block_copy_helper.440
+ _block_descriptor.265
+ _block_descriptor.274
+ _block_descriptor.292
+ _block_descriptor.302
+ _block_descriptor.313
+ _block_descriptor.319
+ _block_descriptor.326
+ _block_descriptor.346
+ _block_descriptor.350
+ _block_descriptor.356
+ _block_descriptor.380
+ _block_descriptor.390
+ _block_descriptor.397
+ _block_descriptor.400
+ _block_descriptor.406
+ _block_descriptor.413
+ _block_descriptor.425
+ _block_descriptor.429
+ _block_descriptor.432
+ _block_descriptor.439
+ _block_descriptor.442
+ _block_destroy_helper.264
+ _block_destroy_helper.273
+ _block_destroy_helper.291
+ _block_destroy_helper.301
+ _block_destroy_helper.312
+ _block_destroy_helper.318
+ _block_destroy_helper.325
+ _block_destroy_helper.345
+ _block_destroy_helper.349
+ _block_destroy_helper.355
+ _block_destroy_helper.379
+ _block_destroy_helper.389
+ _block_destroy_helper.396
+ _block_destroy_helper.399
+ _block_destroy_helper.405
+ _block_destroy_helper.412
+ _block_destroy_helper.424
+ _block_destroy_helper.428
+ _block_destroy_helper.431
+ _block_destroy_helper.438
+ _block_destroy_helper.441
+ _objc_msgSend$_getCameraSensorActivityData:micSensorActivityData:isMutedMic:isInactiveMicModeSelection:
+ _objc_msgSend$ccui_applyGlassWithGrouping:
+ _objc_msgSend$ccui_applySubduedGlassWithGrouping:
+ _objc_msgSend$contentModuleContextRequestsMutedMicrophoneSensorActivityData:
+ _objc_msgSend$disallowGlassGroupingForReason:
+ _objc_msgSend$inactiveMicrophoneAttributionChanged:
+ _objc_msgSend$isPointerActive
+ _objc_msgSend$mutedMicrophoneSensorActivityData
+ _objc_msgSend$pointerDidExitContentModuleContainerViewController:
+ _objc_msgSend$pointerWillEnterContentModuleContainerViewController:
+ _objc_msgSend$setAllowsGlassGrouping:
+ _objectdestroy.261Tm
+ _objectdestroy.358Tm
+ _symbolic So10NSMapTableCySo10SBIconViewC______pGSg So15BSInvalidatableP
- -[CCUIHeaderPocketView inactiveMicModeSelectionAttributionChanged:]
- -[CCUIMainViewController _getCameraSensorActivityData:micSensorActivityData:isInactiveMicModeSelection:]
- -[CCUISensorAttributionCompactControl inactiveMicModeSelectionAttributionChanged:]
- GCC_except_table149
- _OBJC_IVAR_$_CCUISensorAttributionCompactControl._displayedInactiveMicModeSelectionAttribution
- _OBJC_IVAR_$_CCUISensorAttributionCompactControl._inactiveMicModeSelectionAttribution
- __CATEGORY_INSTANCE_METHODS_SBIconView_$_ControlCenterUI
- __CATEGORY_PROPERTIES_SBIconView_$_ControlCenterUI
- __CATEGORY_PROTOCOLS_SBIconView_$_ControlCenterUI
- __CATEGORY_SBIconView_$_ControlCenterUI
- ___104-[CCUIMainViewController _getCameraSensorActivityData:micSensorActivityData:isInactiveMicModeSelection:]_block_invoke
- ___104-[CCUIMainViewController _getCameraSensorActivityData:micSensorActivityData:isInactiveMicModeSelection:]_block_invoke.128
- ___104-[CCUIMainViewController _getCameraSensorActivityData:micSensorActivityData:isInactiveMicModeSelection:]_block_invoke_2
- ___104-[CCUIMainViewController _getCameraSensorActivityData:micSensorActivityData:isInactiveMicModeSelection:]_block_invoke_2.129
- ___block_literal_global.135
- _block_copy_helper.260
- _block_copy_helper.269
- _block_copy_helper.287
- _block_copy_helper.297
- _block_copy_helper.308
- _block_copy_helper.314
- _block_copy_helper.321
- _block_copy_helper.341
- _block_copy_helper.345
- _block_copy_helper.351
- _block_copy_helper.370
- _block_copy_helper.380
- _block_copy_helper.387
- _block_copy_helper.390
- _block_copy_helper.396
- _block_copy_helper.403
- _block_copy_helper.415
- _block_copy_helper.419
- _block_copy_helper.422
- _block_copy_helper.429
- _block_copy_helper.432
- _block_descriptor.262
- _block_descriptor.271
- _block_descriptor.289
- _block_descriptor.299
- _block_descriptor.310
- _block_descriptor.316
- _block_descriptor.323
- _block_descriptor.343
- _block_descriptor.347
- _block_descriptor.353
- _block_descriptor.372
- _block_descriptor.382
- _block_descriptor.389
- _block_descriptor.392
- _block_descriptor.398
- _block_descriptor.405
- _block_descriptor.417
- _block_descriptor.421
- _block_descriptor.424
- _block_descriptor.431
- _block_descriptor.434
- _block_destroy_helper.261
- _block_destroy_helper.270
- _block_destroy_helper.288
- _block_destroy_helper.298
- _block_destroy_helper.309
- _block_destroy_helper.315
- _block_destroy_helper.322
- _block_destroy_helper.342
- _block_destroy_helper.346
- _block_destroy_helper.352
- _block_destroy_helper.371
- _block_destroy_helper.381
- _block_destroy_helper.388
- _block_destroy_helper.391
- _block_destroy_helper.397
- _block_destroy_helper.404
- _block_destroy_helper.416
- _block_destroy_helper.420
- _block_destroy_helper.423
- _block_destroy_helper.430
- _block_destroy_helper.433
- _objc_msgSend$_getCameraSensorActivityData:micSensorActivityData:isInactiveMicModeSelection:
- _objc_msgSend$ccui_applyGlass
- _objc_msgSend$ccui_applySubduedGlass
- _objc_msgSend$inactiveMicModeSelectionAttributionChanged:
- _objectdestroy.258Tm
- _objectdestroy.355Tm
CStrings:
+ "@\"NSCountedSet\""
+ "Calculated customHorizontalPadding is not finite %s, pageControlFrame: %s"
+ "Calculated customVerticalPadding is not finite %s, pageControlFrame: %s"
+ "ControlCenterUIStaging"
+ "T@\"NSCountedSet\",R,C,N,V_activePointerRegions"
+ "TB,N,V_allowsGlassGrouping"
+ "_activePointerRegions"
+ "_allowsGlassGrouping"
+ "_displayedInactiveMicrophoneAttribution"
+ "_getCameraSensorActivityData:micSensorActivityData:isMutedMic:isInactiveMicModeSelection:"
+ "_inactiveMicrophoneAttribution"
+ "activePointerRegions"
+ "ccui_applyGlassWithGrouping:"
+ "ccui_applySubduedGlassWithGrouping:"
+ "ccui_disallowGlassGroupingForReason:"
+ "contentModuleContextRequestsMutedMicrophoneSensorActivityData:"
+ "disallowGlassGroupingAssertionsByIconView"
+ "disallowGlassGroupingForReason:"
+ "inactiveMicrophoneAttributionChanged:"
+ "isPointerActive"
+ "mutedMicrophoneSensorActivityData"
+ "pointerDidExitContentModuleContainerViewController:"
+ "pointerWillEnterContentModuleContainerViewController:"
+ "shouldPreviewOverlapMenuForIconView:"
+ "v48@0:8^@16^@24^B32^B40"
- "_displayedInactiveMicModeSelectionAttribution"
- "_getCameraSensorActivityData:micSensorActivityData:isInactiveMicModeSelection:"
- "_inactiveMicModeSelectionAttribution"
- "enforceLayoutInsetsForAxis:"
- "inactiveMicModeSelectionAttributionChanged:"
- "v40@0:8^@16^@24^B32"

```
