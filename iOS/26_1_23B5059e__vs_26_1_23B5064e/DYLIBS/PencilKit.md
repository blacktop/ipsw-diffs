## PencilKit

> `/System/Library/Frameworks/PencilKit.framework/PencilKit`

```diff

-574.0.0.0.0
-  __TEXT.__text: 0x3215a8
+576.0.0.0.0
+  __TEXT.__text: 0x3227f4
   __TEXT.__auth_stubs: 0x3280
-  __TEXT.__objc_methlist: 0x2522c
-  __TEXT.__const: 0x7484
+  __TEXT.__objc_methlist: 0x252d4
+  __TEXT.__const: 0x7494
   __TEXT.__dlopen_cstrs: 0x569
   __TEXT.__cstring: 0xd1ee
-  __TEXT.__constg_swiftt: 0xf80
-  __TEXT.__swift5_typeref: 0x12d0
+  __TEXT.__constg_swiftt: 0xf88
+  __TEXT.__swift5_typeref: 0x12f2
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_reflstr: 0xdf2
   __TEXT.__swift5_fieldmd: 0x12f8
   __TEXT.__swift5_assocty: 0x4b0
   __TEXT.__swift5_proto: 0x308
   __TEXT.__swift5_types: 0x148
-  __TEXT.__swift5_capture: 0x59c
-  __TEXT.__swift_as_entry: 0xc0
+  __TEXT.__swift5_capture: 0x5bc
+  __TEXT.__swift_as_entry: 0xc8
   __TEXT.__swift_as_ret: 0x94
-  __TEXT.__oslogstring: 0xdf37
+  __TEXT.__oslogstring: 0xe06c
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__gcc_except_tab: 0x24fb8
+  __TEXT.__gcc_except_tab: 0x2506c
   __TEXT.__ustring: 0x21a
-  __TEXT.__unwind_info: 0xfa98
-  __TEXT.__eh_frame: 0x2758
-  __TEXT.__objc_classname: 0x5583
-  __TEXT.__objc_methname: 0x65a4a
-  __TEXT.__objc_methtype: 0x188e6
-  __TEXT.__objc_stubs: 0x3b640
+  __TEXT.__unwind_info: 0xfaf8
+  __TEXT.__eh_frame: 0x2828
+  __TEXT.__objc_classname: 0x5586
+  __TEXT.__objc_methname: 0x65c3b
+  __TEXT.__objc_methtype: 0x18938
+  __TEXT.__objc_stubs: 0x3b760
   __DATA_CONST.__got: 0x2040
   __DATA_CONST.__const: 0x6e78
   __DATA_CONST.__objc_classlist: 0x10f0
   __DATA_CONST.__objc_catlist: 0x80
   __DATA_CONST.__objc_protolist: 0x7c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13010
+  __DATA_CONST.__objc_selrefs: 0x13078
   __DATA_CONST.__objc_protorefs: 0x100
   __DATA_CONST.__objc_superrefs: 0xd68
   __DATA_CONST.__objc_arraydata: 0x830
   __AUTH_CONST.__auth_got: 0x1958
-  __AUTH_CONST.__const: 0x6e48
+  __AUTH_CONST.__const: 0x6e70
   __AUTH_CONST.__cfstring: 0xe160
-  __AUTH_CONST.__objc_const: 0x47018
+  __AUTH_CONST.__objc_const: 0x470b0
   __AUTH_CONST.__objc_intobj: 0x930
   __AUTH_CONST.__objc_arrayobj: 0x648
   __AUTH_CONST.__objc_doubleobj: 0xd0
   __AUTH_CONST.__objc_dictobj: 0x3c0
-  __AUTH.__objc_data: 0x9888
+  __AUTH.__objc_data: 0x9890
   __AUTH.__data: 0x758
-  __DATA.__objc_ivar: 0x2b84
-  __DATA.__data: 0x64a0
-  __DATA.__bss: 0x5eb0
+  __DATA.__objc_ivar: 0x2b8c
+  __DATA.__data: 0x64a8
+  __DATA.__bss: 0x5eb8
   __DATA.__common: 0x128
-  __DATA_DIRTY.__objc_ivar: 0x1184
+  __DATA_DIRTY.__objc_ivar: 0x1188
   __DATA_DIRTY.__objc_data: 0x17c0
   __DATA_DIRTY.__data: 0x38
   __DATA_DIRTY.__bss: 0x700

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 01CA3796-C133-333F-8AB7-2A3A0EF6D720
-  Functions: 17212
-  Symbols:   56413
-  CStrings:  22859
+  UUID: 83146813-9ECF-352E-A339-146EFFA4B288
+  Functions: 17236
+  Symbols:   56476
+  CStrings:  22883
 
Symbols:
+ -[PKAutoRefineTask isInvalidatedGivenDrawing:autoRefineController:currentStrokes:inStrokesToReplace:lineDrawing:strokeGroups:outStrokeGroupsToReplace:outStrokesToPreserve:]
+ -[PKAutoRefineTask strokesAnimationCompletedWithSuccess:]
+ -[PKAutoRefineTaskCoordinator setUserInteractionDelay:]
+ -[PKPencilSqueezeController textEffectsWindowDidChangeBounds]
+ -[PKPencilSqueezeInteraction textEffectsWindowDidChangeWindowBounds:]
+ -[PKTextEffectsWindowObserver dealloc]
+ -[PKTextEffectsWindowObserver observeValueForKeyPath:ofObject:change:context:]
+ -[PKTiledView _recentStrokesForAutoRefine]
+ -[PKTiledView _trimRecentStrokes]
+ -[PKTiledView _updateTimestampForLatestUserInteraction]
+ -[PKTiledView externalAutoRefineTaskCoordinator]
+ -[PKTiledView setExternalAutoRefineTaskCoordinator:]
+ -[UIView(PKAdditions) _pk_hide]
+ -[UIView(PKAdditions) _pk_show]
+ GCC_except_table216
+ GCC_except_table246
+ GCC_except_table251
+ GCC_except_table252
+ GCC_except_table260
+ GCC_except_table265
+ GCC_except_table273
+ GCC_except_table278
+ GCC_except_table279
+ GCC_except_table286
+ GCC_except_table294
+ GCC_except_table295
+ GCC_except_table301
+ GCC_except_table302
+ GCC_except_table303
+ GCC_except_table310
+ GCC_except_table314
+ GCC_except_table315
+ GCC_except_table322
+ GCC_except_table328
+ GCC_except_table329
+ GCC_except_table336
+ GCC_except_table340
+ GCC_except_table341
+ GCC_except_table345
+ GCC_except_table346
+ GCC_except_table352
+ GCC_except_table353
+ GCC_except_table354
+ GCC_except_table359
+ GCC_except_table360
+ GCC_except_table365
+ GCC_except_table369
+ GCC_except_table382
+ GCC_except_table383
+ GCC_except_table388
+ GCC_except_table389
+ GCC_except_table390
+ GCC_except_table456
+ _$s9PencilKit21RecognitionControllerC17setAutoRefineMode_2inyAC0fgH0O_So12PKCanvasViewCSgtYaFyyYacfU_
+ _$s9PencilKit21RecognitionControllerC17setAutoRefineMode_2inyAC0fgH0O_So12PKCanvasViewCSgtYaFyyYacfU_TA
+ _$s9PencilKit21RecognitionControllerC17setAutoRefineMode_2inyAC0fgH0O_So12PKCanvasViewCSgtYaFyyYacfU_TATQ0_
+ _$s9PencilKit21RecognitionControllerC17setAutoRefineMode_2inyAC0fgH0O_So12PKCanvasViewCSgtYaFyyYacfU_TATu
+ _$s9PencilKit21RecognitionControllerC17setAutoRefineMode_2inyAC0fgH0O_So12PKCanvasViewCSgtYaFyyYacfU_TY0_
+ _$s9PencilKit21RecognitionControllerC17setAutoRefineMode_2inyAC0fgH0O_So12PKCanvasViewCSgtYaFyyYacfU_TY1_
+ _$s9PencilKit21RecognitionControllerC17setAutoRefineMode_2inyAC0fgH0O_So12PKCanvasViewCSgtYaFyyYacfU_TY2_
+ _$s9PencilKit21RecognitionControllerC17setAutoRefineMode_2inyAC0fgH0O_So12PKCanvasViewCSgtYaFyyYacfU_TY3_
+ _$s9PencilKit21RecognitionControllerC17setAutoRefineMode_2inyAC0fgH0O_So12PKCanvasViewCSgtYaFyyYacfU_TY4_
+ _$s9PencilKit21RecognitionControllerC17setAutoRefineMode_2inyAC0fgH0O_So12PKCanvasViewCSgtYaFyyYacfU_TY5_
+ _$s9PencilKit21RecognitionControllerC17setAutoRefineMode_2inyAC0fgH0O_So12PKCanvasViewCSgtYaFyyYacfU_TY6_
+ _$s9PencilKit21RecognitionControllerC17setAutoRefineMode_2inyAC0fgH0O_So12PKCanvasViewCSgtYaFyyYacfU_Tu
+ _$s9PencilKit21RecognitionControllerC24removeAsRefinableStrokesyySayAA8PKStrokeVGYaF
+ _$s9PencilKit21RecognitionControllerC24removeAsRefinableStrokesyySayAA8PKStrokeVGYaFTY0_
+ _$s9PencilKit21RecognitionControllerC24removeAsRefinableStrokesyySayAA8PKStrokeVGYaFTY1_
+ _$s9PencilKit21RecognitionControllerC24removeAsRefinableStrokesyySayAA8PKStrokeVGYaFTY2_
+ _$s9PencilKit21RecognitionControllerC24removeAsRefinableStrokesyySayAA8PKStrokeVGYaFTu
+ _$s9PencilKit21RecognitionControllerC33setAutoRefineUserInteractionDelayyySdF
+ _$s9PencilKit21RecognitionControllerC33setAutoRefineUserInteractionDelayyySdFytSgyYaScMYccfU_
+ _$s9PencilKit21RecognitionControllerC33setAutoRefineUserInteractionDelayyySdFytSgyYaScMYccfU_TA
+ _$s9PencilKit21RecognitionControllerC33setAutoRefineUserInteractionDelayyySdFytSgyYaScMYccfU_TATQ0_
+ _$s9PencilKit21RecognitionControllerC33setAutoRefineUserInteractionDelayyySdFytSgyYaScMYccfU_TATu
+ _$s9PencilKit21RecognitionControllerC33setAutoRefineUserInteractionDelayyySdFytSgyYaScMYccfU_TY0_
+ _$s9PencilKit21RecognitionControllerC33setAutoRefineUserInteractionDelayyySdFytSgyYaScMYccfU_Tu
+ _$s9PencilKit33AutoRefineTaskCoordinatorDelegate33_C07EB3BA79DD666E822D6A98FF7ECB3BLLC04autodeF13RecentStrokesySayAA8PKStrokeVGSo06PKAutodeF0CFTo
+ _.str.61
+ _.str.63
+ _OBJC_IVAR_$_PKAutoRefineTaskCoordinator._userInteractionDelay
+ _OBJC_IVAR_$_PKTiledView._timestampForLatestUserInteraction
+ __MergedGlobals.291
+ __PROTOCOLS__TtC9PencilKitP33_C07EB3BA79DD666E822D6A98FF7ECB3B33AutoRefineTaskCoordinatorDelegate.27
+ ___111-[PKAutoRefineTaskCoordinator autoRefineTask:synthesizeRefinedDrawingForStrokes:transcription:completionBlock:]_block_invoke.12
+ ___111-[PKAutoRefineTaskCoordinator autoRefineTask:synthesizeRefinedDrawingForStrokes:transcription:completionBlock:]_block_invoke.14
+ ___111-[PKAutoRefineTaskCoordinator autoRefineTask:synthesizeRefinedDrawingForStrokes:transcription:completionBlock:]_block_invoke.8
+ ___111-[PKAutoRefineTaskCoordinator autoRefineTask:synthesizeRefinedDrawingForStrokes:transcription:completionBlock:]_block_invoke_2.19
+ ___54-[PKTiledView _updateWantsExtendedDynamicRangeContent]_block_invoke.368
+ ___block_descriptor_112_e8_32s40s48s56s64s72s80s88s96w_e61_v64?0"NSArray"8"NSArray"16"CHDrawing"24q32d40d48?<v?>56lw96l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_descriptor_168_e8_32s40s48s56s64s72s80s88s96s104s112s120bs128w_e5_v8?0lw128l8s120l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8s112l8
+ ___block_descriptor_88_ea8_32r_e27_v24?0"PKStrokePoint"8^B16lr32l8
+ ___block_literal_global.1498
+ ___block_literal_global.1505
+ ___block_literal_global.362
+ ___block_literal_global.540
+ ___const.<block>.paths.64
+ _block_copy_helper.52
+ _block_copy_helper.58
+ _block_copy_helper.64
+ _block_copy_helper.70
+ _block_descriptor.54
+ _block_descriptor.60
+ _block_descriptor.66
+ _block_descriptor.72
+ _block_destroy_helper.53
+ _block_destroy_helper.59
+ _block_destroy_helper.65
+ _block_destroy_helper.71
+ _objc_msgSend$_pk_hide
+ _objc_msgSend$_pk_show
+ _objc_msgSend$_trimRecentStrokes
+ _objc_msgSend$_updateTimestampForLatestUserInteraction
+ _objc_msgSend$autoRefineTaskCoordinatorRecentStrokes:
+ _objc_msgSend$isAutoCorrectionAllowed
+ _objc_msgSend$isPredictiveKeyboardAllowed
+ _objc_msgSend$isSpellCheckAllowed
+ _objc_msgSend$textEffectsWindowDidChangeWindowBounds:
+ _objectdestroy.47Tm
+ _symbolic So27PKAutoRefineTaskCoordinatorC
- -[PKAutoRefineTask isInvalidatedGivenDrawing:autoRefineController:currentStroke:inStrokesToReplace:lineDrawing:strokeGroups:outStrokeGroupsToReplace:outStrokesToPreserve:]
- -[PKAutoRefineTask logEventCompletionWithSuccess:]
- GCC_except_table232
- GCC_except_table233
- GCC_except_table234
- GCC_except_table239
- GCC_except_table248
- GCC_except_table250
- GCC_except_table257
- GCC_except_table258
- GCC_except_table262
- GCC_except_table263
- GCC_except_table268
- GCC_except_table276
- GCC_except_table284
- GCC_except_table285
- GCC_except_table289
- GCC_except_table297
- GCC_except_table298
- GCC_except_table304
- GCC_except_table305
- GCC_except_table306
- GCC_except_table323
- GCC_except_table325
- GCC_except_table332
- GCC_except_table333
- GCC_except_table337
- GCC_except_table339
- GCC_except_table343
- GCC_except_table349
- GCC_except_table350
- GCC_except_table351
- GCC_except_table355
- GCC_except_table356
- GCC_except_table357
- GCC_except_table362
- GCC_except_table363
- GCC_except_table368
- GCC_except_table372
- GCC_except_table385
- GCC_except_table386
- GCC_except_table451
- _$s9PencilKit21RecognitionControllerC17setAutoRefineMode_2inyAC0fgH0O_So12PKCanvasViewCSgtYaFytSgyYacfU_
- _$s9PencilKit21RecognitionControllerC17setAutoRefineMode_2inyAC0fgH0O_So12PKCanvasViewCSgtYaFytSgyYacfU_TA
- _$s9PencilKit21RecognitionControllerC17setAutoRefineMode_2inyAC0fgH0O_So12PKCanvasViewCSgtYaFytSgyYacfU_TATQ0_
- _$s9PencilKit21RecognitionControllerC17setAutoRefineMode_2inyAC0fgH0O_So12PKCanvasViewCSgtYaFytSgyYacfU_TATu
- _$s9PencilKit21RecognitionControllerC17setAutoRefineMode_2inyAC0fgH0O_So12PKCanvasViewCSgtYaFytSgyYacfU_TY0_
- _$s9PencilKit21RecognitionControllerC17setAutoRefineMode_2inyAC0fgH0O_So12PKCanvasViewCSgtYaFytSgyYacfU_TY1_
- _$s9PencilKit21RecognitionControllerC17setAutoRefineMode_2inyAC0fgH0O_So12PKCanvasViewCSgtYaFytSgyYacfU_TY2_
- _$s9PencilKit21RecognitionControllerC17setAutoRefineMode_2inyAC0fgH0O_So12PKCanvasViewCSgtYaFytSgyYacfU_TY3_
- _$s9PencilKit21RecognitionControllerC17setAutoRefineMode_2inyAC0fgH0O_So12PKCanvasViewCSgtYaFytSgyYacfU_TY4_
- _$s9PencilKit21RecognitionControllerC17setAutoRefineMode_2inyAC0fgH0O_So12PKCanvasViewCSgtYaFytSgyYacfU_TY5_
- _$s9PencilKit21RecognitionControllerC17setAutoRefineMode_2inyAC0fgH0O_So12PKCanvasViewCSgtYaFytSgyYacfU_Tu
- _.str.60
- _.str.62
- __PROTOCOLS__TtC9PencilKitP33_C07EB3BA79DD666E822D6A98FF7ECB3B33AutoRefineTaskCoordinatorDelegate.23
- ___111-[PKAutoRefineTaskCoordinator autoRefineTask:synthesizeRefinedDrawingForStrokes:transcription:completionBlock:]_block_invoke.10
- ___111-[PKAutoRefineTaskCoordinator autoRefineTask:synthesizeRefinedDrawingForStrokes:transcription:completionBlock:]_block_invoke.6
- ___111-[PKAutoRefineTaskCoordinator autoRefineTask:synthesizeRefinedDrawingForStrokes:transcription:completionBlock:]_block_invoke_2.16
- ___54-[PKTiledView _updateWantsExtendedDynamicRangeContent]_block_invoke.367
- ___block_descriptor_104_e8_32s40s48s56s64s72s80s88w_e61_v64?0"NSArray"8"NSArray"16"CHDrawing"24q32d40d48?<v?>56lw88l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8
- ___block_descriptor_160_e8_32s40s48s56s64s72s80s88s96s104s112bs120w_e5_v8?0lw120l8s112l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8s96l8s104l8
- ___block_descriptor_40_ea8_32r_e27_v24?0"PKStrokePoint"8^B16lr32l8
- ___block_literal_global.1489
- ___block_literal_global.1496
- ___block_literal_global.361
- ___block_literal_global.539
- ___const.<block>.paths.63
- _block_copy_helper.47
- _block_copy_helper.53
- _block_copy_helper.59
- _block_copy_helper.65
- _block_descriptor.49
- _block_descriptor.55
- _block_descriptor.61
- _block_descriptor.67
- _block_destroy_helper.48
- _block_destroy_helper.54
- _block_destroy_helper.60
- _block_destroy_helper.66
- _objectdestroy.42Tm
CStrings:
+ "@\"NSArray\"24@0:8@\"PKAutoRefineTaskCoordinator\"16"
+ "Cancel active task given query item."
+ "Cancel active task given refinable stroke."
+ "Cancel all tasks"
+ "Cancel task given query item."
+ "Cancel task given refinable stroke."
+ "T@\"PKAutoRefineTaskCoordinator\",W,N,V_externalAutoRefineTaskCoordinator"
+ "Tried to remove refinable strokes when auto-refine wasn't enabled."
+ "UITEW bounds did change to: %{private}@, paletteVisible: %{BOOL}d"
+ "_externalAutoRefineTaskCoordinator"
+ "_pk_hide"
+ "_pk_show"
+ "_recentStrokesForAutoRefine"
+ "_trimRecentStrokes"
+ "_updateTimestampForLatestUserInteraction"
+ "_userInteractionDelay"
+ "autoRefineTaskCoordinatorRecentStrokes:"
+ "externalAutoRefineTaskCoordinator"
+ "isAutoCorrectionAllowed"
+ "isPredictiveKeyboardAllowed"
+ "isSpellCheckAllowed"
+ "maximumConcurrentCompilationTaskCount"
+ "setExternalAutoRefineTaskCoordinator:"
+ "textEffectsWindowDidChangeWindowBounds:"
+ "{?=\"delegateSupportsTiledView\"b1\"delegateSupportsReplaceStrokes\"b1\"delegateSupportsRecentStrokes\"b1}"
- "{?=\"delegateSupportsTiledView\"b1\"delegateSupportsReplaceStrokes\"b1}"

```
