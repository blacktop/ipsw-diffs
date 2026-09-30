## TextInputUI

> `/System/Library/PrivateFrameworks/TextInputUI.framework/TextInputUI`

```diff

-9126.2.3.1.103
-  __TEXT.__text: 0xd7530
+9126.2.4.1.105
+  __TEXT.__text: 0xdab68
   __TEXT.__auth_stubs: 0x2bc0
-  __TEXT.__objc_methlist: 0xc28c
+  __TEXT.__objc_methlist: 0xc56c
   __TEXT.__const: 0x2170
   __TEXT.__dlopen_cstrs: 0x1c4
-  __TEXT.__cstring: 0xa1ac
+  __TEXT.__cstring: 0xa217
   __TEXT.__swift5_typeref: 0xe7a
-  __TEXT.__oslogstring: 0x2cc0
+  __TEXT.__oslogstring: 0x2db1
   __TEXT.__swift5_capture: 0x2a8
   __TEXT.__constg_swiftt: 0xb44
   __TEXT.__swift5_reflstr: 0x468

   __TEXT.__swift_as_ret: 0x34
   __TEXT.__swift5_mpenum: 0x14
   __TEXT.__ustring: 0x78
-  __TEXT.__unwind_info: 0x2de8
+  __TEXT.__unwind_info: 0x2e38
   __TEXT.__eh_frame: 0xc6c
-  __TEXT.__objc_classname: 0x1586
-  __TEXT.__objc_methname: 0x2323c
-  __TEXT.__objc_methtype: 0x4f4e
-  __TEXT.__objc_stubs: 0x1b700
-  __DATA_CONST.__got: 0x1178
-  __DATA_CONST.__const: 0x72a0
-  __DATA_CONST.__objc_classlist: 0x528
+  __TEXT.__objc_classname: 0x15b5
+  __TEXT.__objc_methname: 0x23cb8
+  __TEXT.__objc_methtype: 0x4f8f
+  __TEXT.__objc_stubs: 0x1bea0
+  __DATA_CONST.__got: 0x1180
+  __DATA_CONST.__const: 0x72d0
+  __DATA_CONST.__objc_classlist: 0x530
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x170
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x84d0
+  __DATA_CONST.__objc_selrefs: 0x86c8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x360
   __DATA_CONST.__objc_arraydata: 0x568
   __AUTH_CONST.__auth_got: 0x15e8
-  __AUTH_CONST.__const: 0x1608
-  __AUTH_CONST.__cfstring: 0xb5e0
-  __AUTH_CONST.__objc_const: 0x133a8
+  __AUTH_CONST.__const: 0x1628
+  __AUTH_CONST.__cfstring: 0xb640
+  __AUTH_CONST.__objc_const: 0x13868
   __AUTH_CONST.__objc_intobj: 0x360
   __AUTH_CONST.__objc_arrayobj: 0x1f8
   __AUTH_CONST.__objc_doubleobj: 0x170
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_floatobj: 0xe0
-  __AUTH.__objc_data: 0x2110
+  __AUTH.__objc_data: 0x2160
   __AUTH.__data: 0x5d0
-  __DATA.__objc_ivar: 0xe7c
+  __DATA.__objc_ivar: 0xed4
   __DATA.__data: 0x1930
-  __DATA.__bss: 0x1638
+  __DATA.__bss: 0x1648
   __DATA.__common: 0x168
   __DATA_DIRTY.__objc_data: 0x19f0
   __DATA_DIRTY.__data: 0xd8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 456CB13B-FDCE-30FE-8C23-D065E8188527
-  Functions: 4822
-  Symbols:   16053
-  CStrings:  10045
+  UUID: 462ACB22-C141-3C2C-9728-7C96361BCC0D
+  Functions: 4889
+  Symbols:   16282
+  CStrings:  10175
 
Symbols:
+ -[TUIKBKeyView fullRowMultiplier]
+ -[TUIKBKeyView prepareUpdatesForStyle:toStyle:startRows:endRows:]
+ -[TUIKBKeyView setTransitionWidthConstraint:]
+ -[TUIKBKeyView showDebugColor:]
+ -[TUIKBKeyView smallRowMultiplier]
+ -[TUIKBKeyView transitionWidthConstraint]
+ -[TUIKey coreNameString]
+ -[TUIKey fullRowMultiplier]
+ -[TUIKey isPaddingForType:]
+ -[TUIKey isPaddingWhenFull]
+ -[TUIKey isPaddingWhenSmall]
+ -[TUIKey isPadding]
+ -[TUIKey isZeroWidthPadding]
+ -[TUIKey matchesKey:]
+ -[TUIKey pairKeyForTransition:]
+ -[TUIKey setFullRowMultiplier:]
+ -[TUIKey setPaddingWhenFull:]
+ -[TUIKey setPaddingWhenSmall:]
+ -[TUIKey setSmallRowMultiplier:]
+ -[TUIKey setTransitionPairKey:]
+ -[TUIKey smallRowMultiplier]
+ -[TUIKey transitionPairKey]
+ -[TUIKeyplane(TransitionSupport) findCoreKeysBetweenRows:isSpaceRow:]
+ -[TUIKeyplane(TransitionSupport) findFloatingTransitionRowsForLayoutName:screenTraits:]
+ -[TUIKeyplane(TransitionSupport) keyFromOriginalKey:]
+ -[TUIKeyplaneRow buildTransitionRowWithKeys:fullWidthMultiplier:currentLayoutClass:]
+ -[TUIKeyplaneRow constrainKeys:inView:]
+ -[TUIKeyplaneRow fullSpaceMultiplier]
+ -[TUIKeyplaneRow keyViewsForTransition]
+ -[TUIKeyplaneRow preppedTransitionKeyViewForKey:widthGuide:]
+ -[TUIKeyplaneRow setFullSpaceMultiplier:]
+ -[TUIKeyplaneRow setSmallSpaceMultiplier:]
+ -[TUIKeyplaneRow setTransitionKeyViews:]
+ -[TUIKeyplaneRow setTransitionKeyWidthGuide:]
+ -[TUIKeyplaneRow setTransitionRowData:]
+ -[TUIKeyplaneRow setTransitionWidthForSpaceRow:]
+ -[TUIKeyplaneRow smallSpaceMultiplier]
+ -[TUIKeyplaneRow transitionKeyViews]
+ -[TUIKeyplaneRow transitionKeyWidthGuide]
+ -[TUIKeyplaneRow transitionRowData]
+ -[TUIKeyplaneRow transitionWidthForSpaceRow]
+ -[TUIKeyplaneTransitionRow .cxx_destruct]
+ -[TUIKeyplaneTransitionRow coreKeys]
+ -[TUIKeyplaneTransitionRow fullNumberOfRows]
+ -[TUIKeyplaneTransitionRow leftFullKeys]
+ -[TUIKeyplaneTransitionRow leftSmallKeys]
+ -[TUIKeyplaneTransitionRow middlePaddingFullRow]
+ -[TUIKeyplaneTransitionRow middlePaddingSmallRow]
+ -[TUIKeyplaneTransitionRow rightFullKeys]
+ -[TUIKeyplaneTransitionRow rightSmallKeys]
+ -[TUIKeyplaneTransitionRow setCoreKeys:]
+ -[TUIKeyplaneTransitionRow setFullNumberOfRows:]
+ -[TUIKeyplaneTransitionRow setLeftFullKeys:]
+ -[TUIKeyplaneTransitionRow setLeftSmallKeys:]
+ -[TUIKeyplaneTransitionRow setMiddlePaddingFullRow:]
+ -[TUIKeyplaneTransitionRow setMiddlePaddingSmallRow:]
+ -[TUIKeyplaneTransitionRow setRightFullKeys:]
+ -[TUIKeyplaneTransitionRow setRightSmallKeys:]
+ -[TUIKeyplaneTransitionRow setSmallNumberOfRows:]
+ -[TUIKeyplaneTransitionRow smallNumberOfRows]
+ -[TUIKeyplaneView currentVisualState]
+ -[TUIKeyplaneView defaultBottomRowMultiplierForLayoutClass:]
+ -[TUIKeyplaneView hasRowDiff]
+ -[TUIKeyplaneView keyplaneInsetsForClass:]
+ -[TUIKeyplaneView setCurrentVisualState:]
+ -[TUIKeyplaneView setHasRowDiff:]
+ _OBJC_CLASS_$_TUIKeyplaneTransitionRow
+ _OBJC_IVAR_$_TUIKBKeyView._transitionWidthConstraint
+ _OBJC_IVAR_$_TUIKey._fullRowMultiplier
+ _OBJC_IVAR_$_TUIKey._paddingWhenFull
+ _OBJC_IVAR_$_TUIKey._paddingWhenSmall
+ _OBJC_IVAR_$_TUIKey._smallRowMultiplier
+ _OBJC_IVAR_$_TUIKey._transitionPairKey
+ _OBJC_IVAR_$_TUIKeyplaneRow._fullSpaceMultiplier
+ _OBJC_IVAR_$_TUIKeyplaneRow._smallSpaceMultiplier
+ _OBJC_IVAR_$_TUIKeyplaneRow._transitionKeyViews
+ _OBJC_IVAR_$_TUIKeyplaneRow._transitionKeyWidthGuide
+ _OBJC_IVAR_$_TUIKeyplaneRow._transitionRowData
+ _OBJC_IVAR_$_TUIKeyplaneRow._transitionWidthForSpaceRow
+ _OBJC_IVAR_$_TUIKeyplaneTransitionRow._coreKeys
+ _OBJC_IVAR_$_TUIKeyplaneTransitionRow._fullNumberOfRows
+ _OBJC_IVAR_$_TUIKeyplaneTransitionRow._leftFullKeys
+ _OBJC_IVAR_$_TUIKeyplaneTransitionRow._leftSmallKeys
+ _OBJC_IVAR_$_TUIKeyplaneTransitionRow._middlePaddingFullRow
+ _OBJC_IVAR_$_TUIKeyplaneTransitionRow._middlePaddingSmallRow
+ _OBJC_IVAR_$_TUIKeyplaneTransitionRow._rightFullKeys
+ _OBJC_IVAR_$_TUIKeyplaneTransitionRow._rightSmallKeys
+ _OBJC_IVAR_$_TUIKeyplaneTransitionRow._smallNumberOfRows
+ _OBJC_IVAR_$_TUIKeyplaneView._currentVisualState
+ _OBJC_IVAR_$_TUIKeyplaneView._hasRowDiff
+ _OBJC_METACLASS_$_TUIKeyplaneTransitionRow
+ _UIKBAttributeNameIgnoreShiftRendering
+ _UIKitLibrary.2891
+ _UIKitLibraryCore.frameworkLibrary.2894
+ _UIKitLibraryCore.frameworkLibrary.3580
+ __OBJC_$_INSTANCE_METHODS_TUIKeyplane(TransitionSupport)
+ __OBJC_$_INSTANCE_METHODS_TUIKeyplaneTransitionRow
+ __OBJC_$_INSTANCE_VARIABLES_TUIKeyplaneTransitionRow
+ __OBJC_$_PROP_LIST_TUIKeyplaneTransitionRow
+ __OBJC_CLASS_RO_$_TUIKeyplaneTransitionRow
+ __OBJC_METACLASS_RO_$_TUIKeyplaneTransitionRow
+ __TUIKeyboardTrackingLogger.8609
+ __TUIKeyboardTrackingLogger.log.8615
+ __TUIKeyboardTrackingLogger.onceToken.8613
+ __TUIKeyplaneLogger
+ __TUIKeyplaneLogger.log
+ __TUIKeyplaneLogger.onceToken
+ ___33-[TUIKeyplaneView updateAllTrees]_block_invoke.102
+ ___69-[TUIKeyplane(TransitionSupport) findCoreKeysBetweenRows:isSpaceRow:]_block_invoke
+ ___84-[TUIKeyplaneView animatingTransitionFromState:toState:animationType:totalDuration:]_block_invoke_7
+ ___84-[TUIKeyplaneView animatingTransitionFromState:toState:animationType:totalDuration:]_block_invoke_8
+ ___84-[TUIKeyplaneView animatingTransitionFromState:toState:animationType:totalDuration:]_block_invoke_9
+ ___Block_byref_object_copy_.12851
+ ___Block_byref_object_copy_.2043
+ ___Block_byref_object_copy_.2888
+ ___Block_byref_object_copy_.3337
+ ___Block_byref_object_copy_.5567
+ ___Block_byref_object_copy_.5937
+ ___Block_byref_object_copy_.8351
+ ___Block_byref_object_copy_.9939
+ ___Block_byref_object_dispose_.12852
+ ___Block_byref_object_dispose_.2044
+ ___Block_byref_object_dispose_.2889
+ ___Block_byref_object_dispose_.3338
+ ___Block_byref_object_dispose_.5568
+ ___Block_byref_object_dispose_.5938
+ ___Block_byref_object_dispose_.8352
+ ___Block_byref_object_dispose_.9940
+ ___UIKitLibraryCore_block_invoke.2895
+ ___UIKitLibraryCore_block_invoke.3581
+ ____TUIKeyboardTrackingLogger_block_invoke.8618
+ ____TUIKeyplaneLogger_block_invoke
+ ___block_descriptor_112_8_32s40s48s56s64s72s80s88s_e11_v24?0Q8Q16ls32l8s40l8s48l8s56l8s64l8s72l8s80l8s88l8
+ ___block_literal_global.10.10896
+ ___block_literal_global.10041
+ ___block_literal_global.10583
+ ___block_literal_global.10901
+ ___block_literal_global.11086
+ ___block_literal_global.11426
+ ___block_literal_global.11584
+ ___block_literal_global.11857
+ ___block_literal_global.12861
+ ___block_literal_global.13102
+ ___block_literal_global.1323
+ ___block_literal_global.13604
+ ___block_literal_global.1418
+ ___block_literal_global.1756
+ ___block_literal_global.18.8406
+ ___block_literal_global.1863
+ ___block_literal_global.20.10038
+ ___block_literal_global.20.9500
+ ___block_literal_global.2071
+ ___block_literal_global.22.9502
+ ___block_literal_global.2553
+ ___block_literal_global.2824
+ ___block_literal_global.2932
+ ___block_literal_global.3010
+ ___block_literal_global.3192
+ ___block_literal_global.3339
+ ___block_literal_global.3833
+ ___block_literal_global.4.13125
+ ___block_literal_global.4095
+ ___block_literal_global.4278
+ ___block_literal_global.43.2533
+ ___block_literal_global.4501
+ ___block_literal_global.5390
+ ___block_literal_global.5600
+ ___block_literal_global.6.11088
+ ___block_literal_global.6053
+ ___block_literal_global.61.13100
+ ___block_literal_global.667
+ ___block_literal_global.6743
+ ___block_literal_global.6865
+ ___block_literal_global.7129
+ ___block_literal_global.7397
+ ___block_literal_global.760
+ ___block_literal_global.764
+ ___block_literal_global.7794
+ ___block_literal_global.7962
+ ___block_literal_global.8410
+ ___block_literal_global.8614
+ ___block_literal_global.8816
+ ___block_literal_global.9231
+ ___block_literal_global.9413
+ ___block_literal_global.9493
+ ___block_literal_global.9575
+ ___block_literal_global.9948
+ _audit_stringUIKit.2898
+ _audit_stringUIKit.3586
+ _objc_msgSend$buildTransitionRowWithKeys:fullWidthMultiplier:currentLayoutClass:
+ _objc_msgSend$configForAppearance:inputMode:traitEnvironment:
+ _objc_msgSend$constrainKeys:inView:
+ _objc_msgSend$coreKeys
+ _objc_msgSend$coreNameString
+ _objc_msgSend$currentVisualState
+ _objc_msgSend$defaultBottomRowMultiplierForLayoutClass:
+ _objc_msgSend$findCoreKeysBetweenRows:isSpaceRow:
+ _objc_msgSend$findFloatingTransitionRowsForLayoutName:screenTraits:
+ _objc_msgSend$fullNumberOfRows
+ _objc_msgSend$fullRowMultiplier
+ _objc_msgSend$fullSpaceMultiplier
+ _objc_msgSend$hasRowDiff
+ _objc_msgSend$inheritedAnimationDuration
+ _objc_msgSend$isPadding
+ _objc_msgSend$isPaddingForType:
+ _objc_msgSend$isPaddingWhenFull
+ _objc_msgSend$isPaddingWhenSmall
+ _objc_msgSend$isZeroWidthPadding
+ _objc_msgSend$keyFromOriginalKey:
+ _objc_msgSend$keyViewsForTransition
+ _objc_msgSend$keyplaneInsetsForClass:
+ _objc_msgSend$leftFullKeys
+ _objc_msgSend$leftSmallKeys
+ _objc_msgSend$matchesKey:
+ _objc_msgSend$middlePaddingSmallRow
+ _objc_msgSend$pairKeyForTransition:
+ _objc_msgSend$prepareUpdatesForStyle:toStyle:startRows:endRows:
+ _objc_msgSend$preppedTransitionKeyViewForKey:widthGuide:
+ _objc_msgSend$rightFullKeys
+ _objc_msgSend$rightSmallKeys
+ _objc_msgSend$setCoreKeys:
+ _objc_msgSend$setCurrentVisualState:
+ _objc_msgSend$setEnableAnimation:
+ _objc_msgSend$setFullNumberOfRows:
+ _objc_msgSend$setFullRowMultiplier:
+ _objc_msgSend$setFullSpaceMultiplier:
+ _objc_msgSend$setHasRowDiff:
+ _objc_msgSend$setLeftFullKeys:
+ _objc_msgSend$setLeftSmallKeys:
+ _objc_msgSend$setMiddlePaddingFullRow:
+ _objc_msgSend$setMiddlePaddingSmallRow:
+ _objc_msgSend$setPaddingWhenFull:
+ _objc_msgSend$setPaddingWhenSmall:
+ _objc_msgSend$setRightFullKeys:
+ _objc_msgSend$setRightSmallKeys:
+ _objc_msgSend$setSmallNumberOfRows:
+ _objc_msgSend$setSmallRowMultiplier:
+ _objc_msgSend$setSmallSpaceMultiplier:
+ _objc_msgSend$setTransitionKeyViews:
+ _objc_msgSend$setTransitionKeyWidthGuide:
+ _objc_msgSend$setTransitionPairKey:
+ _objc_msgSend$setTransitionRowData:
+ _objc_msgSend$setTransitionWidthConstraint:
+ _objc_msgSend$setTransitionWidthForSpaceRow:
+ _objc_msgSend$smallNumberOfRows
+ _objc_msgSend$smallRowMultiplier
+ _objc_msgSend$smallSpaceMultiplier
+ _objc_msgSend$transitionKeyViews
+ _objc_msgSend$transitionKeyWidthGuide
+ _objc_msgSend$transitionPairKey
+ _objc_msgSend$transitionRowData
+ _objc_msgSend$transitionWidthConstraint
+ _objc_msgSend$transitionWidthForSpaceRow
+ _sharedInstance.__instance.10897
+ _sharedInstance.onceToken.10037
+ _sharedInstance.onceToken.10895
+ _sharedInstance.onceToken.6864
+ _shouldGenerateCandidateForContext:.onceToken.9954
- -[TUIKBKeyView prepareUpdatesForStyle:toStyle:]
- -[TUIKeyplaneRow updateKeysInRowWithData:]
- -[TUIKeyplaneView updateKeysForRow:withKeys:]
- -[TUILiveKeyView renderConfig]
- -[TUILiveKeyView setRenderConfig:]
- _OBJC_IVAR_$_TUILiveKeyView._renderConfig
- _UIKitLibrary.2873
- _UIKitLibraryCore.frameworkLibrary.2876
- _UIKitLibraryCore.frameworkLibrary.3565
- __OBJC_$_INSTANCE_METHODS_TUIKeyplane
- __TUIKeyboardTrackingLogger.8543
- __TUIKeyboardTrackingLogger.log.8549
- __TUIKeyboardTrackingLogger.onceToken.8547
- ___33-[TUIKeyplaneView updateAllTrees]_block_invoke.103
- ___Block_byref_object_copy_.12776
- ___Block_byref_object_copy_.2031
- ___Block_byref_object_copy_.2870
- ___Block_byref_object_copy_.3321
- ___Block_byref_object_copy_.5497
- ___Block_byref_object_copy_.5867
- ___Block_byref_object_copy_.8285
- ___Block_byref_object_copy_.9878
- ___Block_byref_object_dispose_.12777
- ___Block_byref_object_dispose_.2032
- ___Block_byref_object_dispose_.2871
- ___Block_byref_object_dispose_.3322
- ___Block_byref_object_dispose_.5498
- ___Block_byref_object_dispose_.5868
- ___Block_byref_object_dispose_.8286
- ___Block_byref_object_dispose_.9879
- ___UIKitLibraryCore_block_invoke.2877
- ___UIKitLibraryCore_block_invoke.3566
- ____TUIKeyboardTrackingLogger_block_invoke.8552
- ___block_literal_global.10.10830
- ___block_literal_global.10515
- ___block_literal_global.10835
- ___block_literal_global.11020
- ___block_literal_global.11354
- ___block_literal_global.11509
- ___block_literal_global.11782
- ___block_literal_global.12786
- ___block_literal_global.13027
- ___block_literal_global.1320
- ___block_literal_global.13486
- ___block_literal_global.1415
- ___block_literal_global.1748
- ___block_literal_global.18.8340
- ___block_literal_global.1858
- ___block_literal_global.20.9439
- ___block_literal_global.20.9977
- ___block_literal_global.2062
- ___block_literal_global.22.9441
- ___block_literal_global.2535
- ___block_literal_global.2806
- ___block_literal_global.2914
- ___block_literal_global.2992
- ___block_literal_global.3176
- ___block_literal_global.3323
- ___block_literal_global.3818
- ___block_literal_global.4.13050
- ___block_literal_global.4080
- ___block_literal_global.4263
- ___block_literal_global.43.2515
- ___block_literal_global.4479
- ___block_literal_global.5322
- ___block_literal_global.5530
- ___block_literal_global.5986
- ___block_literal_global.6.11022
- ___block_literal_global.61.13025
- ___block_literal_global.6676
- ___block_literal_global.6797
- ___block_literal_global.7061
- ___block_literal_global.7329
- ___block_literal_global.748
- ___block_literal_global.752
- ___block_literal_global.7726
- ___block_literal_global.7896
- ___block_literal_global.8344
- ___block_literal_global.8548
- ___block_literal_global.8751
- ___block_literal_global.9170
- ___block_literal_global.9352
- ___block_literal_global.9432
- ___block_literal_global.9514
- ___block_literal_global.9887
- ___block_literal_global.9980
- _audit_stringUIKit.2880
- _audit_stringUIKit.3571
- _objc_msgSend$backgroundInsetsForStyle:
- _objc_msgSend$prepareUpdatesForStyle:toStyle:
- _objc_msgSend$updateKeysInRowWithData:
- _sharedInstance.__instance.10831
- _sharedInstance.onceToken.10829
- _sharedInstance.onceToken.6796
- _sharedInstance.onceToken.9976
- _shouldGenerateCandidateForContext:.onceToken.9893
CStrings:
+ "#T"
+ "%"
+ "@\"TUIKeyplaneTransitionRow\""
+ "BaseKeyWidthGuide"
+ "DynamicKeyplane"
+ "Exactly two rows required to find core keys (actual: %li)"
+ "Floating transition core keys: %@"
+ "Floating transition floating row\nLeft: %@\nRight: %@"
+ "Floating transition full row\nLeft: %@\nRight: %@"
+ "T@\"NSArray\",&,N,V_coreKeys"
+ "T@\"NSArray\",&,N,V_leftFullKeys"
+ "T@\"NSArray\",&,N,V_leftSmallKeys"
+ "T@\"NSArray\",&,N,V_rightFullKeys"
+ "T@\"NSArray\",&,N,V_rightSmallKeys"
+ "T@\"NSArray\",&,N,V_transitionKeyViews"
+ "T@\"NSLayoutConstraint\",&,N,V_transitionWidthConstraint"
+ "T@\"NSLayoutConstraint\",&,N,V_transitionWidthForSpaceRow"
+ "T@\"TUIKey\",&,N,V_transitionPairKey"
+ "T@\"TUIKeyplaneTransitionRow\",&,N,V_transitionRowData"
+ "T@\"UILayoutGuide\",&,N,V_transitionKeyWidthGuide"
+ "TB,N,GisPaddingWhenFull,V_paddingWhenFull"
+ "TB,N,GisPaddingWhenSmall,V_paddingWhenSmall"
+ "TB,N,V_hasRowDiff"
+ "TQ,N,V_fullNumberOfRows"
+ "TQ,N,V_smallNumberOfRows"
+ "TUIKeyplaneTransitionRow"
+ "Td,N,V_fullRowMultiplier"
+ "Td,N,V_fullSpaceMultiplier"
+ "Td,N,V_middlePaddingFullRow"
+ "Td,N,V_middlePaddingSmallRow"
+ "Td,N,V_smallRowMultiplier"
+ "Td,N,V_smallSpaceMultiplier"
+ "Tq,N,V_currentVisualState"
+ "TransitionSupport"
+ "UIKBAttributeNameIgnoreShiftRendering"
+ "Unable to create floating transition rows for %@"
+ "_coreKeys"
+ "_currentVisualState"
+ "_fullNumberOfRows"
+ "_fullRowMultiplier"
+ "_fullSpaceMultiplier"
+ "_hasRowDiff"
+ "_leftFullKeys"
+ "_leftSmallKeys"
+ "_middlePaddingFullRow"
+ "_middlePaddingSmallRow"
+ "_paddingWhenFull"
+ "_paddingWhenSmall"
+ "_rightFullKeys"
+ "_rightSmallKeys"
+ "_smallNumberOfRows"
+ "_smallRowMultiplier"
+ "_smallSpaceMultiplier"
+ "_transitionKeyViews"
+ "_transitionKeyWidthGuide"
+ "_transitionPairKey"
+ "_transitionRowData"
+ "_transitionWidthConstraint"
+ "_transitionWidthForSpaceRow"
+ "buildTransitionRowWithKeys:fullWidthMultiplier:currentLayoutClass:"
+ "configForAppearance:inputMode:traitEnvironment:"
+ "constrainKeys:inView:"
+ "coreKeys"
+ "coreNameString"
+ "currentVisualState"
+ "defaultBottomRowMultiplierForLayoutClass:"
+ "findCoreKeysBetweenRows:isSpaceRow:"
+ "findFloatingTransitionRowsForLayoutName:screenTraits:"
+ "fullNumberOfRows"
+ "fullRowMultiplier"
+ "fullSpaceMultiplier"
+ "hasRowDiff"
+ "ignore-shift-rendering"
+ "inheritedAnimationDuration"
+ "isPadding"
+ "isPaddingForType:"
+ "isPaddingWhenFull"
+ "isPaddingWhenSmall"
+ "isZeroWidthPadding"
+ "keyFromOriginalKey:"
+ "keyViewsForTransition"
+ "keyplaneInsetsForClass:"
+ "leftFullKeys"
+ "leftSmallKeys"
+ "matchesKey:"
+ "middlePaddingFullRow"
+ "middlePaddingSmallRow"
+ "paddingWhenFull"
+ "paddingWhenSmall"
+ "pairKeyForTransition:"
+ "prepareUpdatesForStyle:toStyle:startRows:endRows:"
+ "preppedTransitionKeyViewForKey:widthGuide:"
+ "rightFullKeys"
+ "rightSmallKeys"
+ "setCoreKeys:"
+ "setCurrentVisualState:"
+ "setEnableAnimation:"
+ "setFullNumberOfRows:"
+ "setFullRowMultiplier:"
+ "setFullSpaceMultiplier:"
+ "setHasRowDiff:"
+ "setLeftFullKeys:"
+ "setLeftSmallKeys:"
+ "setMiddlePaddingFullRow:"
+ "setMiddlePaddingSmallRow:"
+ "setPaddingWhenFull:"
+ "setPaddingWhenSmall:"
+ "setRightFullKeys:"
+ "setRightSmallKeys:"
+ "setSmallNumberOfRows:"
+ "setSmallRowMultiplier:"
+ "setSmallSpaceMultiplier:"
+ "setTransitionKeyViews:"
+ "setTransitionKeyWidthGuide:"
+ "setTransitionPairKey:"
+ "setTransitionRowData:"
+ "setTransitionWidthConstraint:"
+ "setTransitionWidthForSpaceRow:"
+ "showDebugColor:"
+ "smallNumberOfRows"
+ "smallRowMultiplier"
+ "smallSpaceMultiplier"
+ "transitionKeyViews"
+ "transitionKeyWidthGuide"
+ "transitionPairKey"
+ "transitionRowData"
+ "transitionWidthConstraint"
+ "transitionWidthForSpaceRow"
+ "v24@?0Q8Q16"
+ "v40@0:8@16d24q32"
+ "v48@0:8q16q24Q32Q40"
+ "z"
- "&"
- "prepareUpdatesForStyle:toStyle:"
- "updateKeysForRow:withKeys:"
- "updateKeysInRowWithData:"

```
