## SystemApertureUI

> `/System/Library/PrivateFrameworks/SystemApertureUI.framework/SystemApertureUI`

```diff

-85.0.0.0.0
-  __TEXT.__text: 0x12b60
-  __TEXT.__auth_stubs: 0x560
-  __TEXT.__objc_methlist: 0x1dbc
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0xa4d
-  __TEXT.__oslogstring: 0x9e1
-  __TEXT.__gcc_except_tab: 0xa00
-  __TEXT.__unwind_info: 0x7e8
-  __TEXT.__objc_classname: 0x59d
-  __TEXT.__objc_methname: 0x48c8
-  __TEXT.__objc_methtype: 0x12b9
-  __TEXT.__objc_stubs: 0x2ac0
-  __DATA_CONST.__got: 0x198
-  __DATA_CONST.__const: 0x4f8
-  __DATA_CONST.__objc_classlist: 0x70
+96.0.0.0.0
+  __TEXT.__text: 0x15028
+  __TEXT.__objc_methlist: 0x243c
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0xcad
+  __TEXT.__oslogstring: 0xaa4
+  __TEXT.__gcc_except_tab: 0xac4
+  __TEXT.__unwind_info: 0x900
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x500
+  __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x100
+  __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xea8
-  __DATA_CONST.__objc_superrefs: 0x68
-  __AUTH_CONST.__auth_got: 0x2c0
+  __DATA_CONST.__objc_selrefs: 0x10b0
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x80
+  __DATA_CONST.__got: 0x1c8
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x8e0
-  __AUTH_CONST.__objc_const: 0x5188
-  __DATA.__objc_ivar: 0x148
-  __DATA.__data: 0xc00
-  __DATA_DIRTY.__objc_data: 0x460
+  __AUTH_CONST.__cfstring: 0xa80
+  __AUTH_CONST.__objc_const: 0x6648
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x1ac
+  __DATA.__data: 0xf00
+  __DATA_DIRTY.__objc_data: 0x550
   __DATA_DIRTY.__bss: 0x28
   __DATA_DIRTY.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SystemAperture.framework/SystemAperture
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 206F18D5-3B2C-3807-A8FA-5EDE069AE81E
-  Functions: 484
-  Symbols:   1999
-  CStrings:  1048
+  UUID: BC10CDB9-EFBA-3CFB-8507-C5D3DF89701E
+  Functions: 602
+  Symbols:   2429
+  CStrings:  226
 
Symbols:
+ +[SAUILayoutContext instanceWithBlock:]
+ +[SAUILayoutContext mutatorClass]
+ +[SAUILayoutMetrics supportsSecureCoding]
+ -[SAUIBlankingRegionElementViewController .cxx_destruct]
+ -[SAUIBlankingRegionElementViewController _canShowWhileLocked]
+ -[SAUIBlankingRegionElementViewController _enumerateObserversRespondingToSelector:usingBlock:]
+ -[SAUIBlankingRegionElementViewController addElementViewControllingObserver:]
+ -[SAUIBlankingRegionElementViewController elementViewProvider]
+ -[SAUIBlankingRegionElementViewController element]
+ -[SAUIBlankingRegionElementViewController handleElementLongPress:]
+ -[SAUIBlankingRegionElementViewController handleElementTap:]
+ -[SAUIBlankingRegionElementViewController handleLongPress:]
+ -[SAUIBlankingRegionElementViewController handleTap:]
+ -[SAUIBlankingRegionElementViewController initWithElement:]
+ -[SAUIBlankingRegionElementViewController initWithElement:].cold.1
+ -[SAUIBlankingRegionElementViewController removeElementViewControllingObserver:]
+ -[SAUIBlankingRegionElementViewController viewDidAppear:]
+ -[SAUIBlankingRegionElementViewController viewDidDisappear:]
+ -[SAUIBlankingRegionElementViewController viewWillAppear:]
+ -[SAUIBlankingRegionElementViewController viewWillDisappear:]
+ -[SAUIElementView _layoutProvidedView:transformView:frame:animated:]
+ -[SAUIElementView customTransformView]
+ -[SAUIElementView layoutDirection]
+ -[SAUIElementView setLayoutDirection:]
+ -[SAUIElementViewController customViewTransform]
+ -[SAUIElementViewController layoutDirection]
+ -[SAUIElementViewController setCustomViewTransform:]
+ -[SAUIElementViewController setLayoutDirection:]
+ -[SAUIIndicatorElementViewController associatedBlankingRegionIdentifierDidInvalidateForLayoutSpecifier:]
+ -[SAUIIndicatorElementViewController fixedIndicatorRegionFrameDidUpdate]
+ -[SAUILayoutContext _setMaximumCompactSize:]
+ -[SAUILayoutContext _setMaximumExpandedSize:]
+ -[SAUILayoutContext _setMaximumHorizontalMinimalViewSize:]
+ -[SAUILayoutContext _setMaximumLeadingTrailingViewSize:]
+ -[SAUILayoutContext _setMaximumMinimalSize:]
+ -[SAUILayoutContext _setMinimumCompactSize:]
+ -[SAUILayoutContext _setMinimumExpandedSize:]
+ -[SAUILayoutContext _setMinimumMinimalSize:]
+ -[SAUILayoutContext copyWithBlock:]
+ -[SAUILayoutContext copyWithZone:]
+ -[SAUILayoutContext hash]
+ -[SAUILayoutContext isEqual:]
+ -[SAUILayoutContext maximumCompactSize]
+ -[SAUILayoutContext maximumExpandedSize]
+ -[SAUILayoutContext maximumHorizontalMinimalViewSize]
+ -[SAUILayoutContext maximumLeadingTrailingViewSize]
+ -[SAUILayoutContext maximumMinimalSize]
+ -[SAUILayoutContext minimumCompactSize]
+ -[SAUILayoutContext minimumExpandedSize]
+ -[SAUILayoutContext minimumMinimalSize]
+ -[SAUILayoutContextMutator .cxx_destruct]
+ -[SAUILayoutContextMutator initWithLayoutContext:]
+ -[SAUILayoutContextMutator maximumCompactSize]
+ -[SAUILayoutContextMutator maximumExpandedSize]
+ -[SAUILayoutContextMutator maximumHorizontalMinimalViewSize]
+ -[SAUILayoutContextMutator maximumLeadingTrailingViewSize]
+ -[SAUILayoutContextMutator maximumMinimalSize]
+ -[SAUILayoutContextMutator minimumCompactSize]
+ -[SAUILayoutContextMutator minimumExpandedSize]
+ -[SAUILayoutContextMutator minimumMinimalSize]
+ -[SAUILayoutContextMutator setMaximumCompactSize:]
+ -[SAUILayoutContextMutator setMaximumExpandedSize:]
+ -[SAUILayoutContextMutator setMaximumHorizontalMinimalViewSize:]
+ -[SAUILayoutContextMutator setMaximumLeadingTrailingViewSize:]
+ -[SAUILayoutContextMutator setMaximumMinimalSize:]
+ -[SAUILayoutContextMutator setMinimumCompactSize:]
+ -[SAUILayoutContextMutator setMinimumExpandedSize:]
+ -[SAUILayoutContextMutator setMinimumMinimalSize:]
+ -[SAUILayoutMetrics copyWithZone:]
+ -[SAUILayoutMetrics description]
+ -[SAUILayoutMetrics encodeWithCoder:]
+ -[SAUILayoutMetrics hash]
+ -[SAUILayoutMetrics initWithCoder:]
+ -[SAUILayoutMetrics initWithMinimumExpandedSize:maximumExpandedSize:minimumMinimalSize:maximumMinimalSize:minimumCompactSize:maximumCompactSize:maximumHorizontalMinimalViewSize:maximumLeadingTrailingViewSize:]
+ -[SAUILayoutMetrics isEqual:]
+ -[SAUILayoutMetrics maximumCompactSize]
+ -[SAUILayoutMetrics maximumExpandedSize]
+ -[SAUILayoutMetrics maximumHorizontalMinimalViewSize]
+ -[SAUILayoutMetrics maximumLeadingTrailingViewSize]
+ -[SAUILayoutMetrics maximumMinimalSize]
+ -[SAUILayoutMetrics minimumCompactSize]
+ -[SAUILayoutMetrics minimumExpandedSize]
+ -[SAUILayoutMetrics minimumMinimalSize]
+ -[SAUILayoutSpecifyingElementViewController cooperativeTransitionAssertion]
+ -[SAUILayoutSpecifyingElementViewController isDisplayedWithLimitedSize]
+ -[SAUILayoutSpecifyingElementViewController layoutContextForLayoutSpecifier:]
+ -[SAUILayoutSpecifyingElementViewController layoutDirection]
+ -[SAUILayoutSpecifyingElementViewController layoutHostContextDidUpdateTo:withPreviousLayoutHostContext:]
+ -[SAUILayoutSpecifyingElementViewController layoutHostMetricsDidUpdateTo:withPreviousLayoutHostMetrics:]
+ -[SAUILayoutSpecifyingElementViewController layoutMetricsForLayoutSpecifier:]
+ -[SAUILayoutSpecifyingElementViewController requestCooperativeTransitionAssertionWithReason:]
+ -[SAUILayoutSpecifyingElementViewController setDisplayedWithLimitedSize:]
+ -[SAUILayoutSpecifyingElementViewController setLayoutDirection:]
+ -[SAUILayoutSpecifyingElementViewController(SubclassSupport) setLayoutDirection:]
+ -[SAUISystemApertureManager adoptElementViewController:forElement:]
+ -[SAUISystemApertureManager associatedBlankingRegionIdentifierDidInvalidateForLayoutSpecifier:]
+ -[SAUISystemApertureManager blankingRegionElementViewControllers]
+ -[SAUISystemApertureManager destinationToken]
+ -[SAUISystemApertureManager fixedIndicatorRegionInContentView:]
+ -[SAUISystemApertureManager initWithElementAuthority:uniqueIdentifier:]
+ -[SAUISystemApertureManager initWithElementAuthority:uniqueIdentifier:].cold.1
+ -[SAUISystemApertureManager layoutContextForLayoutSpecifier:]
+ -[SAUISystemApertureManager layoutMetricsForLayoutSpecifier:]
+ -[SAUISystemApertureManager registerElement:].cold.1
+ -[SAUISystemApertureManager relinquishElement:withReason:]
+ -[SAUISystemApertureManager relinquishElement:withReason:].cold.1
+ GCC_except_table102
+ GCC_except_table105
+ GCC_except_table15
+ GCC_except_table16
+ GCC_except_table20
+ GCC_except_table27
+ GCC_except_table28
+ GCC_except_table41
+ GCC_except_table42
+ GCC_except_table45
+ GCC_except_table57
+ GCC_except_table58
+ GCC_except_table59
+ GCC_except_table60
+ GCC_except_table62
+ GCC_except_table64
+ GCC_except_table65
+ GCC_except_table70
+ GCC_except_table72
+ GCC_except_table78
+ GCC_except_table80
+ GCC_except_table82
+ _BSSizeSwap
+ _OBJC_CLASS_$_BSEqualsBuilder
+ _OBJC_CLASS_$_BSHashBuilder
+ _OBJC_CLASS_$_SAUIBlankingRegionElementViewController
+ _OBJC_CLASS_$_SAUILayoutContext
+ _OBJC_CLASS_$_SAUILayoutContextMutator
+ _OBJC_CLASS_$_SAUILayoutMetrics
+ _OBJC_IVAR_$_SAUIBlankingRegionElementViewController._element
+ _OBJC_IVAR_$_SAUIBlankingRegionElementViewController._observers
+ _OBJC_IVAR_$_SAUIElementView._customTransformView
+ _OBJC_IVAR_$_SAUIElementView._layoutDirection
+ _OBJC_IVAR_$_SAUIElementViewController._customViewTransform
+ _OBJC_IVAR_$_SAUILayoutContext._maximumCompactSize
+ _OBJC_IVAR_$_SAUILayoutContext._maximumExpandedSize
+ _OBJC_IVAR_$_SAUILayoutContext._maximumHorizontalMinimalViewSize
+ _OBJC_IVAR_$_SAUILayoutContext._maximumLeadingTrailingViewSize
+ _OBJC_IVAR_$_SAUILayoutContext._maximumMinimalSize
+ _OBJC_IVAR_$_SAUILayoutContext._minimumCompactSize
+ _OBJC_IVAR_$_SAUILayoutContext._minimumExpandedSize
+ _OBJC_IVAR_$_SAUILayoutContext._minimumMinimalSize
+ _OBJC_IVAR_$_SAUILayoutContextMutator._layoutContext
+ _OBJC_IVAR_$_SAUILayoutMetrics._maximumCompactSize
+ _OBJC_IVAR_$_SAUILayoutMetrics._maximumExpandedSize
+ _OBJC_IVAR_$_SAUILayoutMetrics._maximumHorizontalMinimalViewSize
+ _OBJC_IVAR_$_SAUILayoutMetrics._maximumLeadingTrailingViewSize
+ _OBJC_IVAR_$_SAUILayoutMetrics._maximumMinimalSize
+ _OBJC_IVAR_$_SAUILayoutMetrics._minimumCompactSize
+ _OBJC_IVAR_$_SAUILayoutMetrics._minimumExpandedSize
+ _OBJC_IVAR_$_SAUILayoutMetrics._minimumMinimalSize
+ _OBJC_IVAR_$_SAUILayoutSpecifyingElementViewController._cooperativeTransitionAssertion
+ _OBJC_IVAR_$_SAUILayoutSpecifyingElementViewController._layoutDirection
+ _OBJC_IVAR_$_SAUISystemApertureManager._blankingRegionElementsToElementViewControllers
+ _OBJC_IVAR_$_SAUISystemApertureManager._destinationToken
+ _OBJC_METACLASS_$_SAUIBlankingRegionElementViewController
+ _OBJC_METACLASS_$_SAUILayoutContext
+ _OBJC_METACLASS_$_SAUILayoutContextMutator
+ _OBJC_METACLASS_$_SAUILayoutMetrics
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _SAHasBlankingRegionBehavior
+ _SAUIElementViewProviderForElementInDestination
+ _SAUIElementViewProviderForElementInDestination.cold.1
+ _SAUILayoutSpecifyingOverriderForElementInDestination
+ _SAUILayoutSpecifyingOverriderForElementViewProvider
+ __OBJC_$_CLASS_METHODS_SAUILayoutContext
+ __OBJC_$_CLASS_METHODS_SAUILayoutMetrics
+ __OBJC_$_CLASS_PROP_LIST_NSSecureCoding
+ __OBJC_$_CLASS_PROP_LIST_SAUIBlockMutating
+ __OBJC_$_CLASS_PROP_LIST_SAUILayoutContext
+ __OBJC_$_CLASS_PROP_LIST_SAUILayoutMetrics
+ __OBJC_$_INSTANCE_METHODS_SAUIBlankingRegionElementViewController
+ __OBJC_$_INSTANCE_METHODS_SAUILayoutContext
+ __OBJC_$_INSTANCE_METHODS_SAUILayoutContextMutator
+ __OBJC_$_INSTANCE_METHODS_SAUILayoutMetrics
+ __OBJC_$_INSTANCE_VARIABLES_SAUIBlankingRegionElementViewController
+ __OBJC_$_INSTANCE_VARIABLES_SAUILayoutContext
+ __OBJC_$_INSTANCE_VARIABLES_SAUILayoutContextMutator
+ __OBJC_$_INSTANCE_VARIABLES_SAUILayoutMetrics
+ __OBJC_$_PROP_LIST_SAElementViewProviding
+ __OBJC_$_PROP_LIST_SAUIBlankingRegionElementViewController
+ __OBJC_$_PROP_LIST_SAUICooperativeTransitionHosting
+ __OBJC_$_PROP_LIST_SAUICooperativeTransitioning
+ __OBJC_$_PROP_LIST_SAUILayoutContext
+ __OBJC_$_PROP_LIST_SAUILayoutContextMutator
+ __OBJC_$_PROP_LIST_SAUILayoutDirectionObserving
+ __OBJC_$_PROP_LIST_SAUILayoutMetrics
+ __OBJC_$_PROTOCOL_CLASS_METHODS_NSSecureCoding
+ __OBJC_$_PROTOCOL_CLASS_METHODS_SAUIBlockMutating
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCoding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SAElementViewProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SAUILayoutDirectionObserving
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SAElementViewProviding
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SAUIBlockMutating
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SAUICooperativeTransitionHosting
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SAUICooperativeTransitioning
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SAUIIndicatorElementViewControlling
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSSecureCoding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SAElementViewProviding
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SAUIBlockMutating
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SAUICooperativeTransitionHosting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SAUICooperativeTransitioning
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SAUIIndicatorElementViewControlling
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SAUILayoutDirectionObserving
+ __OBJC_$_PROTOCOL_REFS_NSSecureCoding
+ __OBJC_$_PROTOCOL_REFS_SAElementViewProviding
+ __OBJC_$_PROTOCOL_REFS_SAUIBlockMutating
+ __OBJC_$_PROTOCOL_REFS_SAUICooperativeTransitionHosting
+ __OBJC_$_PROTOCOL_REFS_SAUICooperativeTransitioning
+ __OBJC_$_PROTOCOL_REFS_SAUIIndicatorElementViewControlling
+ __OBJC_$_PROTOCOL_REFS_SAUILayoutDirectionObserving
+ __OBJC_CLASS_PROTOCOLS_$_SAUIBlankingRegionElementViewController
+ __OBJC_CLASS_PROTOCOLS_$_SAUILayoutContext
+ __OBJC_CLASS_PROTOCOLS_$_SAUILayoutMetrics
+ __OBJC_CLASS_RO_$_SAUIBlankingRegionElementViewController
+ __OBJC_CLASS_RO_$_SAUILayoutContext
+ __OBJC_CLASS_RO_$_SAUILayoutContextMutator
+ __OBJC_CLASS_RO_$_SAUILayoutMetrics
+ __OBJC_LABEL_PROTOCOL_$_NSCoding
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_LABEL_PROTOCOL_$_NSSecureCoding
+ __OBJC_LABEL_PROTOCOL_$_SAElementViewProviding
+ __OBJC_LABEL_PROTOCOL_$_SAUIBlockMutating
+ __OBJC_LABEL_PROTOCOL_$_SAUICooperativeTransitionHosting
+ __OBJC_LABEL_PROTOCOL_$_SAUICooperativeTransitioning
+ __OBJC_LABEL_PROTOCOL_$_SAUIIndicatorElementViewControlling
+ __OBJC_LABEL_PROTOCOL_$_SAUILayoutDirectionObserving
+ __OBJC_METACLASS_RO_$_SAUIBlankingRegionElementViewController
+ __OBJC_METACLASS_RO_$_SAUILayoutContext
+ __OBJC_METACLASS_RO_$_SAUILayoutContextMutator
+ __OBJC_METACLASS_RO_$_SAUILayoutMetrics
+ __OBJC_PROTOCOL_$_NSCoding
+ __OBJC_PROTOCOL_$_NSCopying
+ __OBJC_PROTOCOL_$_NSSecureCoding
+ __OBJC_PROTOCOL_$_SAElementViewProviding
+ __OBJC_PROTOCOL_$_SAUIBlockMutating
+ __OBJC_PROTOCOL_$_SAUICooperativeTransitionHosting
+ __OBJC_PROTOCOL_$_SAUICooperativeTransitioning
+ __OBJC_PROTOCOL_$_SAUIIndicatorElementViewControlling
+ __OBJC_PROTOCOL_$_SAUILayoutDirectionObserving
+ __OBJC_PROTOCOL_REFERENCE_$_SAUICooperativeTransitionHosting
+ __OBJC_PROTOCOL_REFERENCE_$_SAUICooperativeTransitioning
+ __SAUIFrameTransformedForLayoutDirection
+ ___29-[SAUILayoutContext isEqual:]_block_invoke
+ ___29-[SAUILayoutContext isEqual:]_block_invoke_2
+ ___29-[SAUILayoutContext isEqual:]_block_invoke_3
+ ___29-[SAUILayoutContext isEqual:]_block_invoke_4
+ ___29-[SAUILayoutContext isEqual:]_block_invoke_5
+ ___29-[SAUILayoutContext isEqual:]_block_invoke_6
+ ___29-[SAUILayoutContext isEqual:]_block_invoke_7
+ ___29-[SAUILayoutContext isEqual:]_block_invoke_8
+ ___57-[SAUIBlankingRegionElementViewController viewDidAppear:]_block_invoke
+ ___58-[SAUIBlankingRegionElementViewController viewWillAppear:]_block_invoke
+ ___60-[SAUIBlankingRegionElementViewController viewDidDisappear:]_block_invoke
+ ___61-[SAUIBlankingRegionElementViewController viewWillDisappear:]_block_invoke
+ ___67-[SAUISystemApertureManager adoptElementViewController:forElement:]_block_invoke
+ ___68-[SAUIElementView _layoutProvidedView:transformView:frame:animated:]_block_invoke
+ ___93-[SAUILayoutSpecifyingElementViewController requestCooperativeTransitionAssertionWithReason:]_block_invoke
+ ___95-[SAUILayoutSpecifyingElementViewController _updatePreferredLayoutModeAssertionWithPreference:]_block_invoke.130
+ ___95-[SAUILayoutSpecifyingElementViewController _updatePreferredLayoutModeAssertionWithPreference:]_block_invoke.131
+ ___block_descriptor_40_e8_32s_e15_{CGSize=dd}8?0ls32l8
+ ___block_descriptor_89_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_literal_global.150
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$_layoutProvidedView:transformView:frame:animated:
+ _objc_msgSend$_performWithoutRetargetingAnimations:
+ _objc_msgSend$_setMaximumCompactSize:
+ _objc_msgSend$_setMaximumExpandedSize:
+ _objc_msgSend$_setMaximumHorizontalMinimalViewSize:
+ _objc_msgSend$_setMaximumLeadingTrailingViewSize:
+ _objc_msgSend$_setMaximumMinimalSize:
+ _objc_msgSend$_setMinimumCompactSize:
+ _objc_msgSend$_setMinimumExpandedSize:
+ _objc_msgSend$_setMinimumMinimalSize:
+ _objc_msgSend$appendCGSize:
+ _objc_msgSend$appendCGSize:counterpart:
+ _objc_msgSend$associatedBlankingRegionIdentifierDidInvalidateForLayoutSpecifier:
+ _objc_msgSend$beginCooperativeDismissal
+ _objc_msgSend$builder
+ _objc_msgSend$conformsToProtocol:
+ _objc_msgSend$cooperativeTransitionAssertion
+ _objc_msgSend$copyWithBlock:
+ _objc_msgSend$decodeCGSizeForKey:
+ _objc_msgSend$encodeCGSize:forKey:
+ _objc_msgSend$fixedIndicatorRegionInContentView:
+ _objc_msgSend$handleFailureInFunction:file:lineNumber:description:
+ _objc_msgSend$hash
+ _objc_msgSend$initWithElement:
+ _objc_msgSend$initWithElementAuthority:uniqueIdentifier:
+ _objc_msgSend$initWithLayoutContext:
+ _objc_msgSend$initWithMinimumExpandedSize:maximumExpandedSize:minimumMinimalSize:maximumMinimalSize:minimumCompactSize:maximumCompactSize:maximumHorizontalMinimalViewSize:maximumLeadingTrailingViewSize:
+ _objc_msgSend$isDisplayedWithLimitedSize
+ _objc_msgSend$isEqual
+ _objc_msgSend$layoutContextForLayoutSpecifier:
+ _objc_msgSend$layoutHostContextDidUpdateTo:withPreviousLayoutHostContext:
+ _objc_msgSend$layoutHostMetricsDidUpdateTo:withPreviousLayoutHostMetrics:
+ _objc_msgSend$layoutMetricsForLayoutSpecifier:
+ _objc_msgSend$maximumCompactSize
+ _objc_msgSend$maximumExpandedSize
+ _objc_msgSend$maximumHorizontalMinimalViewSize
+ _objc_msgSend$maximumLeadingTrailingViewSize
+ _objc_msgSend$maximumMinimalSize
+ _objc_msgSend$minimumCompactSize
+ _objc_msgSend$minimumExpandedSize
+ _objc_msgSend$minimumMinimalSize
+ _objc_msgSend$mutatorClass
+ _objc_msgSend$removeBehaviorOverridingParticipant:
+ _objc_msgSend$setCooperativeTransitionHost:
+ _objc_msgSend$setDisplayedWithLimitedSize:
+ _objc_msgSend$setLayoutDirection:
+ _objc_msgSend$stringWithUTF8String:
+ _objc_msgSend$viewProviderForDestinationToken:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x8
- -[SAUIElementView layoutAxis]
- -[SAUIElementView setLayoutAxis:]
- -[SAUIElementViewController layoutAxis]
- -[SAUIElementViewController setLayoutAxis:]
- -[SAUISystemApertureManager initWithElementAuthority:].cold.1
- -[SAUISystemApertureManager interSensorRegionInContentView:]
- GCC_except_table23
- GCC_except_table24
- GCC_except_table35
- GCC_except_table36
- GCC_except_table37
- GCC_except_table39
- GCC_except_table46
- GCC_except_table49
- GCC_except_table50
- GCC_except_table55
- GCC_except_table56
- GCC_except_table6
- GCC_except_table69
- GCC_except_table71
- GCC_except_table73
- GCC_except_table91
- GCC_except_table94
- _OBJC_IVAR_$_SAUIElementView._layoutAxis
- __OBJC_$_PROP_LIST_SAUIElementLayoutAxisObserving
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_SAUIElementLayoutAxisObserving
- __OBJC_$_PROTOCOL_METHOD_TYPES_SAUIElementLayoutAxisObserving
- __OBJC_$_PROTOCOL_REFS_SAUIElementLayoutAxisObserving
- __OBJC_LABEL_PROTOCOL_$_SAUIElementLayoutAxisObserving
- __OBJC_PROTOCOL_$_SAUIElementLayoutAxisObserving
- ___33-[SAUIElementView layoutSubviews]_block_invoke_2
- ___33-[SAUIElementView layoutSubviews]_block_invoke_3
- ___33-[SAUIElementView layoutSubviews]_block_invoke_4
- ___33-[SAUIElementView layoutSubviews]_block_invoke_5
- ___95-[SAUILayoutSpecifyingElementViewController _updatePreferredLayoutModeAssertionWithPreference:]_block_invoke.119
- ___95-[SAUILayoutSpecifyingElementViewController _updatePreferredLayoutModeAssertionWithPreference:]_block_invoke.120
- ___block_descriptor_40_e85_v56?0"_SAUIProvidedViewContainerView"8"UIView"16{CGRect={CGPoint=dd}{CGSize=dd}}24l
- ___block_descriptor_88_e8_32s40s48bs_e5_v8?0ls48l8s32l8s40l8
- ___block_literal_global.85
- _objc_msgSend$hasActivityBehavior
- _objc_msgSend$hasAlertBehavior
- _objc_msgSend$layoutAxis
- _objc_msgSend$setLayoutAxis:
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "<%@: %p; minimumExpandedSize=%@; maximumExpandedSize=%@; maximumLeadingTrailingViewSize=%@>"
+ "Adopting element view controller: %{public}@ for element: %{public}@"
+ "Asked to relinquish element that has no view controller: %{public}@"
+ "Element %@ unexpectedly did not return a valid view provider for %@"
+ "Element must respond to _either_ `viewProvider` or `viewProviderForDestinationToken:`."
+ "Relinquishing element: %{public}@ with reason: %{public}@"
+ "SAUIBlankingRegionElementViewController.m"
+ "SAUIUtilities.m"
+ "id<SAElementViewProviding>  _Nonnull SAUIElementViewProviderForElementInDestination(__strong id<SAElement> _Nonnull, id<NSObject>  _Nullable __strong)"
+ "maximumCompactSize"
+ "maximumExpandedSize"
+ "maximumHorizontalMinimalViewSize"
+ "maximumLeadingTrailingViewSize"
+ "maximumMinimalSize"
+ "minimumCompactSize"
+ "minimumExpandedSize"
+ "minimumMinimalSize"
+ "{CGSize=dd}8@?0"
+ "\x811"
+ "\xc1!"
- "#16@0:8"
- ".cxx_destruct"
- "@"
- "@\"<SAAutomaticallyInvalidatable>\""
- "@\"<SAAutomaticallyInvalidatable>\"16@0:8"
- "@\"<SAAutomaticallyInvalidatable>\"24@0:8@\"NSString\"16"
- "@\"<SAAutomaticallyInvalidatable>\"28@0:8@\"NSString\"16B24"
- "@\"<SABehaviorOverridingParticipant>\"24@0:8@\"<SABehaviorOverridingParticipant>\"16"
- "@\"<SAElement>\""
- "@\"<SAElementConsidering>\""
- "@\"<SAElementViewProviding>\""
- "@\"<SAElementViewProviding>\"16@0:8"
- "@\"<SAInvalidatable>\"24@0:8@\"<SAElement>\"16"
- "@\"<SAUIElementViewDelegate>\""
- "@\"<SAUIElementViewProviding>\""
- "@\"<SAUIIndicatorElementViewProviding>\""
- "@\"<SAUIIndicatorLayoutHosting>\""
- "@\"<SAUILayoutHosting>\""
- "@\"<SAUILayoutHosting>\"16@0:8"
- "@\"<SAUILayoutModePreferring>\"16@0:8"
- "@\"<SAUILayoutModePreferring>\"32@0:8@\"<SAUILayoutSpecifyingOverriding>\"16^B24"
- "@\"<SAUILayoutSpecifying>\"16@0:8"
- "@\"<SAUILayoutSpecifyingOverridingParticipant>\"32@0:8@\"<SAUILayoutSpecifyingOverridingParticipant>\"16:24"
- "@\"<SAUISystemApertureManagerDelegate>\""
- "@\"NSArray\""
- "@\"NSArray\"16@0:8"
- "@\"NSHashTable\""
- "@\"NSMapTable\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSPointerArray\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSUUID\"16@0:8"
- "@\"SAAutomaticallyInvalidatingAssertion\""
- "@\"SAUIElementView\""
- "@\"SAUILayoutModePreference\""
- "@\"SAUIPreferredLayoutModeAssertion\""
- "@\"SAUIPreferredLayoutModeAssertion\"16@0:8"
- "@\"SAUIPreferredLayoutModeAssertion\"32@0:8@\"<SAUILayoutSpecifyingOverriding>\"16^B24"
- "@\"UIImageView\""
- "@\"UIView\""
- "@\"UIViewController<SAUIElementViewControlling>\""
- "@\"_SAUIElementViewControllerSnapshotAssertion\""
- "@\"_SAUIPortalView\""
- "@\"_SAUIProvidedViewContainerView\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16:24"
- "@32@0:8@16@24"
- "@32@0:8@16@?24"
- "@32@0:8@16^B24"
- "@32@0:8@16d24"
- "@32@0:8@16q24"
- "@32@0:8q16q24"
- "@36@0:8@16B24q28"
- "@36@0:8B16@20@?28"
- "@40@0:8:16@24@32"
- "@40@0:8@16q24q32"
- "@40@0:8{CGPoint=dd}16@32"
- "@48@0:8{CGRect={CGPoint=dd}{CGSize=dd}}16"
- "@?24@0:8@16"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"<SAElementViewProviding>\"16"
- "B24@0:8@\"NSString\"16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@\"SAUIElementView\"16"
- "B24@0:8@\"UIGestureRecognizer\"16"
- "B24@0:8@16"
- "B24@0:8Q16"
- "B32@0:8@\"<SAUILayoutSpecifyingOverriding>\"16^B24"
- "B32@0:8@\"UIView\"16q24"
- "B32@0:8@16^B24"
- "B32@0:8@16q24"
- "B40@0:8^@16@24@?32"
- "B48@0:8@\"UIView\"16q24@\"<SAUILayoutSpecifyingOverriding>\"32^B40"
- "B48@0:8@16q24@32^B40"
- "NSObject"
- "Q16@0:8"
- "Q24@0:8q16"
- "Q40@0:8q16@\"<SAUILayoutSpecifyingOverriding>\"24^B32"
- "Q40@0:8q16@24^B32"
- "SAActivityHosting"
- "SAActivityHostingPrivate"
- "SAAlertHosting"
- "SAAlertingConfiguring"
- "SABehaviorOverriding"
- "SABehaviorOverridingParticipant"
- "SAElementHosting"
- "SAElementIdentifying"
- "SAElementRegistering"
- "SAElementUniquelyIdentifying"
- "SAUIAlertingAssertion"
- "SAUIContentTransitioning"
- "SAUIElementAssertion"
- "SAUIElementLayoutAxisObserving"
- "SAUIElementSubcomponentPreferencesAccepting"
- "SAUIElementSubcomponentPreferencesProviding"
- "SAUIElementView"
- "SAUIElementViewController"
- "SAUIElementViewControlling"
- "SAUIElementViewControllingObservable"
- "SAUIElementViewControllingObserving"
- "SAUIElementViewDelegate"
- "SAUIElementViewPreferencesAccepting"
- "SAUIElementViewPreferencesProviding"
- "SAUIIndicatorElementViewController"
- "SAUIIndicatorElementViewPreferencesProviding"
- "SAUIIndicatorLayoutHosting"
- "SAUILayoutHosting"
- "SAUILayoutHostingPrivate"
- "SAUILayoutModePreference"
- "SAUILayoutModePreferring"
- "SAUILayoutSpecifying"
- "SAUILayoutSpecifyingElementViewController"
- "SAUILayoutSpecifyingOverrider"
- "SAUILayoutSpecifyingOverriding"
- "SAUILayoutSpecifyingOverridingParticipant"
- "SAUILayoutSpecifyingPrivate"
- "SAUIPreferredLayoutModeAssertion"
- "SAUISnapshotReasonProviding"
- "SAUISystemApertureManager"
- "SAUISystemApertureViewControllerTransitioning"
- "SAUITransitionTracking"
- "SubclassSupport"
- "SystemApertureUIAdditions"
- "SystemApertureUIInternalAdditions"
- "T#,R"
- "T@\"<SAAutomaticallyInvalidatable>\",R,N"
- "T@\"<SAAutomaticallyInvalidatable>\",R,N,V_alertAssertion"
- "T@\"<SAAutomaticallyInvalidatable>\",R,W,N"
- "T@\"<SAAutomaticallyInvalidatable>\",R,W,N,V_alertingActivityAssertion"
- "T@\"<SAElement>\",R,W,N,V_element"
- "T@\"<SAElement>\",R,W,N,V_representedElement"
- "T@\"<SAElementViewProviding>\",R,N"
- "T@\"<SAElementViewProviding>\",R,N,V_elementViewProvider"
- "T@\"<SAUIElementViewDelegate>\",W,N,V_delegate"
- "T@\"<SAUIElementViewProviding>\",R,N"
- "T@\"<SAUIElementViewProviding>\",R,N,V_elementViewProvider"
- "T@\"<SAUIIndicatorElementViewProviding>\",R,N,V_elementViewProvider"
- "T@\"<SAUIIndicatorLayoutHosting>\",W,N,V_layoutHost"
- "T@\"<SAUILayoutHosting>\",?,W,N"
- "T@\"<SAUILayoutHosting>\",?,W,N,V_layoutHost"
- "T@\"<SAUILayoutModePreferring>\",?,R,N"
- "T@\"<SAUILayoutSpecifying>\",R,W,N"
- "T@\"<SAUILayoutSpecifyingOverriding>\",R,N"
- "T@\"<SAUISystemApertureManagerDelegate>\",W,N,V_delegate"
- "T@\"NSArray\",?,R,C,N"
- "T@\"NSArray\",R,C,N"
- "T@\"NSArray\",R,C,N,V_orderedElementViewControllers"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,C,N"
- "T@\"NSString\",R,C,N,V_clientIdentifier"
- "T@\"NSString\",R,C,N,V_elementIdentifier"
- "T@\"NSString\",R,C,N,V_snapshotReason"
- "T@\"NSUUID\",R,C,N"
- "T@\"SAUIElementView\",W,N,V_elementView"
- "T@\"SAUIPreferredLayoutModeAssertion\",?,R,N"
- "T@\"SAUIPreferredLayoutModeAssertion\",R,N,V_preferredLayoutModeAssertion"
- "T@\"UIView\",&,N,V_providedView"
- "T@\"UIView\",&,N,V_sourceView"
- "T@\"UIView\",R,N,G_containerView"
- "T@\"UIView\",R,N,G_contentView"
- "T@\"UIView\",R,N,V_contentView"
- "T@\"UIViewController<SAUIElementViewControlling>\",R,N"
- "T@\"_SAUIProvidedViewContainerView\",&,N,V_leadingTransformView"
- "T@\"_SAUIProvidedViewContainerView\",&,N,V_minimalTransformView"
- "T@\"_SAUIProvidedViewContainerView\",&,N,V_trailingTransformView"
- "T@,R,W,N"
- "T@,R,W,N,V_behaviorOverridingTarget"
- "TB,?,R,N,GisInteractiveDismissalEnabled"
- "TB,?,R,N,GisMinimalPresentationPossible"
- "TB,?,R,N,GisRequestingMenuPresentation"
- "TB,R,N"
- "TB,R,N,G_isNotInCustomLayoutOrTransitionFromCustomLayout"
- "TB,R,N,G_isObstructedBySensorRegion"
- "TB,R,N,GisSauiBlurConfigured"
- "TB,R,N,GisTrackingTransition"
- "TB,R,N,V_portalsProvidedView"
- "TQ,?,N"
- "TQ,?,N,V_layoutAxis"
- "TQ,R"
- "Td,N"
- "Td,N,SsetSauiBlurRadius:"
- "Td,N,V_customContentBlurProgress"
- "Td,N,V_leadingViewAlpha"
- "Td,N,V_leadingViewBlurProgress"
- "Td,N,V_leadingViewSquishProgress"
- "Td,N,V_minimalViewAlpha"
- "Td,N,V_minimalViewBlurProgress"
- "Td,N,V_minimalViewSquishProgress"
- "Td,N,V_snapshotViewBlurProgress"
- "Td,N,V_trailingViewAlpha"
- "Td,N,V_trailingViewBlurProgress"
- "Td,N,V_trailingViewSquishProgress"
- "Td,R,N"
- "Td,R,N,V_fixedIndicatorViewAlpha"
- "Td,R,N,V_fixedIndicatorViewBlurProgress"
- "Td,R,N,V_indicatorViewAlpha"
- "Td,R,N,V_indicatorViewBlurProgress"
- "Tq,N,V_invalidationLayoutModeChangeReason"
- "Tq,R,N"
- "Tq,R,N,G_previousLayoutMode"
- "Tq,R,N,V_layoutMode"
- "Tq,R,N,V_layoutModeChangeReason"
- "Tq,R,N,V_preferredLayoutMode"
- "T{CGAffineTransform=dddddd},?,N"
- "T{CGAffineTransform=dddddd},?,N,V_leadingViewTransform"
- "T{CGAffineTransform=dddddd},?,N,V_minimalViewTransform"
- "T{CGAffineTransform=dddddd},?,N,V_trailingViewTransform"
- "T{CGAffineTransform=dddddd},?,R,N"
- "T{CGAffineTransform=dddddd},R,N"
- "T{CGAffineTransform=dddddd},R,N,V_fixedIndicatorViewTransform"
- "T{CGAffineTransform=dddddd},R,N,V_indicatorViewTransform"
- "T{CGSize=dd},?,R,N"
- "T{CGSize=dd},N"
- "T{CGSize=dd},N,V_leadingViewScale"
- "T{CGSize=dd},N,V_minimalViewScale"
- "T{CGSize=dd},N,V_trailingViewScale"
- "T{CGSize=dd},R,N,G_obstructedRegionSize"
- "UUID"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_SAUIElementViewContentView"
- "_SAUIElementViewControllerSnapshotAssertion"
- "_SAUIPortalView"
- "_SAUIProvidedViewContainerView"
- "_addInvalidatedAssertion:forElement:"
- "_alertAssertion"
- "_alertingActivityAssertion"
- "_alertingActivityAssertionWithReason:implicitlyDismissable:withPreferredLayoutMode:"
- "_appearState"
- "_appliedLayoutModeForSquishTransition"
- "_assertionForElement:"
- "_assertionForElementCreatingIfNecessary:"
- "_axCollapseIfExpandedByUserInteraction"
- "_axLayoutSpecifierRequestsCollapseIfExpandedByUserInteraction:"
- "_axLayoutSpecifierRequestsDiminishment:"
- "_axRequestDiminishment"
- "_behaviorOverridingParticipantSubordinate:toParticipant:passingTest:"
- "_behaviorOverridingTarget"
- "_blurProgress"
- "_canShowWhileLocked"
- "_clientIdentifier"
- "_compactElements"
- "_configureAlertAssertionIfNecessary"
- "_configureBlurFilterIfNecessary"
- "_configureLeadingTransformViewIfNecessary"
- "_configureMinimalTransformViewIfNecessary"
- "_configurePortalViewIfNeeded"
- "_configureTrailingTransformViewIfNecessary"
- "_configureTransformView:ifNecessaryWithProvidedView:assertIfConfigurationRequired:"
- "_configureTransitionShadowViewIfNecessary"
- "_containerView"
- "_contentView"
- "_contentsTransitionShadowView"
- "_cooldownAssertion"
- "_createPortalView"
- "_customContentBlurProgress"
- "_defaultAlertingDuration"
- "_delegate"
- "_descriptionConstituents"
- "_didLayoutResizedTransformView:"
- "_effectiveMinimalView"
- "_effectiveProvidedMinimalView"
- "_element"
- "_elementAssertionDidInvalidate:"
- "_elementAuthority"
- "_elementHost"
- "_elementIdentifier"
- "_elementRequiresBeingDisplayedAlone:"
- "_elementView"
- "_elementViewControllerForElement:creatingIfNecessary:"
- "_elementViewProvider"
- "_elements"
- "_elementsToAssertions"
- "_elementsToElementViewControllers"
- "_elementsToInvalidatedAssertions"
- "_enumerateObserversRespondingToSelector:usingBlock:"
- "_expandToCustomLayoutModeFromUserActionIfPossible"
- "_firstParticipantThatRespondsToSelector:"
- "_fixedIndicatorViewAlpha"
- "_fixedIndicatorViewBlurProgress"
- "_fixedIndicatorViewTransform"
- "_indicatorElementViewController"
- "_indicatorViewAlpha"
- "_indicatorViewBlurProgress"
- "_indicatorViewTransform"
- "_insertContentSnapshotView"
- "_insertSnapshotView:"
- "_invalidateElementPromotionPreferences"
- "_invalidatePreferredLayoutModeAssertionWithReason:"
- "_invalidatePromotedState"
- "_invalidateTemporallyOrderedElements"
- "_invalidatedAssertionForElement:"
- "_invalidationLayoutModeChangeReason"
- "_isInRetargetableAnimationBlock"
- "_isNotInCustomLayoutOrTransitionFromCustomLayout"
- "_isObstructedBySensorRegion"
- "_isSystemApertureTransitioningOptionEnabled:"
- "_lastSize"
- "_layoutAxis"
- "_layoutHost"
- "_layoutMode"
- "_layoutModeChangeReason"
- "_layoutModePreference"
- "_layoutTransitionShadowView"
- "_leadingTransformView"
- "_leadingViewAlpha"
- "_leadingViewBlurProgress"
- "_leadingViewScale"
- "_leadingViewSquishProgress"
- "_leadingViewTransform"
- "_maximumNumberOfSimultaneouslyVisibleElements"
- "_minimalTransformView"
- "_minimalViewAlpha"
- "_minimalViewBlurProgress"
- "_minimalViewScale"
- "_minimalViewSquishProgress"
- "_minimalViewTransform"
- "_modifyAnimationsByDecomposingGeometricTypes:animations:"
- "_modifyAnimationsWithPreferredFrameRateRange:updateReason:animations:"
- "_mostPromotedElements"
- "_observers"
- "_obstructedRegionSize"
- "_orderedBehaviorOverridingParticipants"
- "_orderedElementViewControllers"
- "_overrideWithPreference:"
- "_paddingForView:fromProvider:inLayoutMode:"
- "_portalView"
- "_portalsProvidedView"
- "_preferredLayoutMode"
- "_preferredLayoutModeAssertion"
- "_preferredLayoutModeAssertions"
- "_previousLayoutMode"
- "_promotedStateIsValid"
- "_providedView"
- "_purgeRemovedElementViewControllers"
- "_reasonsToAlertingActivityAssertions"
- "_recreatePortalViewIfNeeded"
- "_reevaluatePromotedElements"
- "_removeAllRetargetableAnimations:"
- "_removeAssertionForElement:"
- "_removeElementViewController:"
- "_removeInvalidatedAssertionForElement:"
- "_removePortalView"
- "_removedElementViewControllers"
- "_representedElement"
- "_requestHostNeedsLayout"
- "_sauiBlurInputRadiusKeyPath"
- "_sauiBlurKeyPath"
- "_sensorObscuringShadowProgress"
- "_setBlurProgress:forView:"
- "_setPreviousLayoutMode:"
- "_setSquishProgress:additionalScale:additionalTransform:forProvidedView:transformView:isLeading:isMinimal:"
- "_setSystemApertureTransitioningOption:enabled:"
- "_shouldReverseLayoutDirection"
- "_snapshotReason"
- "_snapshotView"
- "_snapshotViewAssertion"
- "_snapshotViewBlurProgress"
- "_sourceView"
- "_synchronizeBlurProgress:alpha:squishProgress:additionalTransform:isLeading:isMinimal:ofTransformView:providedView:"
- "_temporallyOrderedElements"
- "_temporallyOrderedVisibleAlertAndActivityElements"
- "_trailingTransformView"
- "_trailingViewAlpha"
- "_trailingViewBlurProgress"
- "_trailingViewScale"
- "_trailingViewSquishProgress"
- "_trailingViewTransform"
- "_transitionIDsToReasons"
- "_updatePreferredLayoutModeAssertionWithPreference:"
- "addAnimation:forKey:"
- "addBehaviorOverridingParticipant:"
- "addCommitHandler:forPhase:"
- "addElementViewControllingObserver:"
- "addInvalidationBlock:"
- "addObject:"
- "addPointer:"
- "addSubview:"
- "alertAssertion"
- "alertWithReason:implicitlyDismissable:"
- "alertingActivityAssertion"
- "alertingDurationForHost:"
- "allObjects"
- "allowsReparentingByLayoutHost"
- "alpha"
- "animateAlongsideTransition:completion:"
- "appendFormat:"
- "appendString:"
- "arrayByAddingObject:"
- "arrayWithObjects:count:"
- "autorelease"
- "beginRequiringSnapshotForReason:"
- "beginTrackingTransitionWithUniqueIdentifier:reason:"
- "behaviorOverridingParticipantSubordinateToParticipant:"
- "behaviorOverridingParticipantSuperiorToParticipant:"
- "behaviorOverridingRole"
- "behaviorOverridingTarget"
- "bounds"
- "bs_map:"
- "bs_mapNoNulls:"
- "bundleForClass:"
- "class"
- "clientIdentifier"
- "concentricPaddingForProvidedView:fromViewProvider:"
- "conformsToProtocol:"
- "containerView"
- "contentProviderWillTransitionToSize:inContainerView:transitionCoordinator:"
- "contentView"
- "copy"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "creationDate"
- "currentHandler"
- "currentPhase"
- "currentState"
- "customContentAlpha"
- "customContentBlurProgress"
- "customizationOptionsForLayoutMode:"
- "customizationOptionsForLayoutMode:forTargetWithOverrider:isDefaultValue:"
- "d"
- "d16@0:8"
- "d24@0:8@\"<SAElementViewProviding>\"16"
- "d24@0:8@16"
- "d32@0:8@\"UIView\"16@\"<SAElementViewProviding>\"24"
- "d32@0:8@16@24"
- "d40@0:8@16@24q32"
- "dealloc"
- "debugDescription"
- "delegate"
- "description"
- "detachedMinimalView"
- "dictionaryWithObjects:forKeys:count:"
- "didMoveToWindow"
- "didUpdateFixedIndicatorViewAlpha:"
- "didUpdateFixedIndicatorViewBlurProgress:"
- "didUpdateFixedIndicatorViewTransform:"
- "didUpdateIndicatorViewAlpha:"
- "didUpdateIndicatorViewBlurProgress:"
- "didUpdateIndicatorViewTransform:"
- "didUpdateInterSensorRegionFrameInScreenSpace:"
- "displayScale"
- "edgeOutsetsForSize:"
- "elementAssertionForElement:"
- "elementIdentifier"
- "elementRequestsNegativeResponse:"
- "elementRequestsSignificantUpdateTransition:"
- "elementRequiresBeingDisplayedAlone:"
- "elementView"
- "elementView:didConfigureLeadingTransformView:"
- "elementView:didConfigureMinimalTransformView:"
- "elementView:didConfigureTrailingTransformView:"
- "elementView:didLayoutResizedLeadingTransformView:"
- "elementView:didLayoutResizedMinimalTransformView:"
- "elementView:didLayoutResizedTrailingTransformView:"
- "elementViewControllerForElement:"
- "elementViewControllingDidAppear:"
- "elementViewControllingDidDisappear:"
- "elementViewControllingWillAppear:"
- "elementViewControllingWillDisappear:"
- "elementViewShouldCenterProvidedContent:"
- "elementsOrderedByPromotionFromTemporallyOrderedElements:withPreviousOrdering:"
- "endTrackingTransitionWithUniqueIdentifier:"
- "enumerateObjectsWithOptions:usingBlock:"
- "fixedIndicatorView"
- "fixedIndicatorViewAlpha"
- "fixedIndicatorViewBlurProgress"
- "fixedIndicatorViewTransform"
- "floatValue"
- "handleElementLongPress:"
- "handleElementTap:"
- "handleElementViewEvent:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "handleLongPress:"
- "handleTap:"
- "hasActivityBehavior"
- "hasAlertBehavior"
- "hash"
- "hashTableWithOptions:"
- "hitTest:withEvent:"
- "hostWillPerformLayout"
- "image"
- "imageNamed:inBundle:"
- "imageWithRenderingMode:"
- "indicatorElementViewController"
- "indicatorNeedsDisplayWellKnownLocationDidInvalidateForLayoutSpecifier:"
- "indicatorView"
- "indicatorViewAlpha"
- "indicatorViewBlurProgress"
- "indicatorViewTransform"
- "init"
- "initWithCapacity:"
- "initWithElement:invalidationHandler:"
- "initWithElement:snapshotReason:"
- "initWithElementAuthority:"
- "initWithElementViewProvider:"
- "initWithFormat:"
- "initWithFrame:"
- "initWithImage:"
- "initWithIndicatorElementViewProvider:"
- "initWithInvalidationInterval:"
- "initWithNibName:bundle:"
- "initWithObjects:"
- "initWithPreferredLayoutMode:reason:"
- "initWithPreferredLayoutModeAssertion:invalidationInterval:"
- "initWithRepresentedElement:layoutModePreference:"
- "initWithRepresentedElement:preferredLayoutMode:reason:"
- "initWithTarget:"
- "initWithType:"
- "initialize"
- "insertPointer:atIndex:"
- "insertSubview:belowSubview:"
- "interSensorRegionInContentView:"
- "interactiveDismissalEnabled"
- "invalidatePromotedElements"
- "invalidateWithReason:"
- "invalidateWithReason:layoutModeChangeReason:"
- "isDescendantOfView:"
- "isEqual:"
- "isEqualToString:"
- "isInteractiveDismissalEnabled"
- "isInteractiveDismissalEnabledForTargetWithOverrider:isDefaultValue:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isMinimalPresentationPossible"
- "isMinimalPresentationPossibleForTargetWithOverrider:isDefaultValue:"
- "isMinimalViewIsolatedForElementView:"
- "isPerformingSystemApertureCustomContentTransition"
- "isPerformingSystemApertureInertTransition"
- "isProvidedViewConcentric:inLayoutMode:"
- "isProvidedViewConcentric:inLayoutMode:forTargetWithOverrider:isDefaultValue:"
- "isProxy"
- "isRequestingMenuPresentation"
- "isRequestingMenuPresentationForTargetWithOverrider:isDefaultValue:"
- "isSauiBlurConfigured"
- "isTrackingTransition"
- "isTrackingTransitionWithReason:"
- "isValid"
- "isViewLoaded"
- "lastObject"
- "layer"
- "layerClass"
- "layoutAxis"
- "layoutDirection"
- "layoutHost"
- "layoutHostContainerViewDidLayoutSubviews:"
- "layoutHostContainerViewDidLayoutSubviews:forTargetWithOverrider:"
- "layoutHostContainerViewWillLayoutSubviews:"
- "layoutHostContainerViewWillLayoutSubviews:forTargetWithOverrider:"
- "layoutIfNeeded"
- "layoutMode"
- "layoutModeForElementView:"
- "layoutModeForTargetWithOverrider:isDefaultValue:"
- "layoutModePreference"
- "layoutModePreferenceForTargetWithOverrider:isDefaultValue:"
- "layoutModePreferenceMayBeImplicitlyInvalidated"
- "layoutSpecifyingOverridingParticipantSubordinateToParticipant:thatRespondsToSelector:"
- "layoutSpecifyingOverridingParticipantSuperiorToParticipant:thatRespondsToSelector:"
- "layoutSpecifyingOverridingTarget"
- "layoutSubviews"
- "leadingTransformView"
- "leadingView"
- "leadingViewAlpha"
- "leadingViewBlurProgress"
- "leadingViewScale"
- "leadingViewSquishProgress"
- "leadingViewTransform"
- "length"
- "loadViewIfNeeded"
- "locationInView:"
- "maximumAvailableSizeForProvidedLeadingView:fromViewProvider:"
- "maximumAvailableSizeForProvidedMinimalView:fromViewProvider:"
- "maximumAvailableSizeForProvidedTrailingView:fromViewProvider:"
- "maximumSizeOfLeadingViewForElementView:"
- "maximumSizeOfMinimalViewForElementView:"
- "maximumSizeOfTrailingViewForElementView:"
- "maximumSupportedLayoutMode"
- "maximumSupportedLayoutModeForTargetWithOverrider:isDefaultValue:"
- "menuPresentationRequestDidChangeForLayoutSpecifier:"
- "minimalPresentationPossible"
- "minimalTransformView"
- "minimalView"
- "minimalViewAlpha"
- "minimalViewBlurProgress"
- "minimalViewScale"
- "minimalViewSquishProgress"
- "minimalViewTransform"
- "minimumSupportedLayoutMode"
- "minimumSupportedLayoutModeForTargetWithOverrider:isDefaultValue:"
- "mutableCopy"
- "notInCustomLayoutOrTransitionFromCustomLayout"
- "numberWithDouble:"
- "numberWithUnsignedInteger:"
- "objectAtIndex:"
- "objectForKey:"
- "obstructedBySensorRegion"
- "obstructedRegionSize"
- "orderedElementViewControllers"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performWithoutAnimation:"
- "pointInside:withEvent:"
- "pointerAtIndex:"
- "portalLayer"
- "portalsProvidedView"
- "preferredComponentViewSizeDidInvalidateForLayoutSpecifier:"
- "preferredEdgeOutsetsDidInvalidateForLayoutSpecifier:"
- "preferredEdgeOutsetsForLayoutMode:suggestedOutsets:maximumOutsets:"
- "preferredEdgeOutsetsForLayoutMode:suggestedOutsets:maximumOutsets:forTargetWithOverrider:isDefaultValue:"
- "preferredLayoutModeAssertion"
- "preferredLayoutModeAssertionForTargetWithOverrider:isDefaultValue:"
- "preferredLayoutModeAssertions"
- "preferredLayoutModeDidInvalidateForLayoutSpecifier:"
- "preferredLayoutModeForTargetWithOverrider:isDefaultValue:"
- "preferredPromotionDidInvalidateForLayoutSpecifier:"
- "previousLayoutMode"
- "providedView"
- "q"
- "q16@0:8"
- "q24@0:8@\"SAUIElementView\"16"
- "q24@0:8@\"UIGestureRecognizer\"16"
- "q24@0:8@16"
- "q32@0:8@\"<SAUILayoutSpecifyingOverriding>\"16^B24"
- "q32@0:8@16^B24"
- "registerElement:"
- "registeredElements"
- "release"
- "removeBehaviorOverridingParticipant:"
- "removeBehaviorOverridingParticipantWithRole:"
- "removeElementViewControllingObserver:"
- "removeFromSuperview"
- "removeObject:"
- "removeObjectForKey:"
- "removePointerAtIndex:"
- "replacePointerAtIndex:withPointer:"
- "requestingMenuPresentation"
- "resetAutomaticInvalidationTimer"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "sa_compact"
- "sa_lastPointer"
- "sauiBlurConfigured"
- "sauiBlurRadius"
- "self"
- "sensorObscuringShadowProgress"
- "sensorRegionInContentView:fromViewProvider:"
- "sensorRegionObstructingViewProvider:inContentView:"
- "setActivityHost:"
- "setAlertHost:"
- "setAlpha:"
- "setAutomaticallyInvalidatable:"
- "setAutoresizingMask:"
- "setBlurRadius:"
- "setBounds:"
- "setCenter:"
- "setContentMode:"
- "setCustomContentAlpha:"
- "setCustomContentBlurProgress:"
- "setDelegate:"
- "setDuration:"
- "setElementHost:"
- "setElementView:"
- "setFillMode:"
- "setFilters:"
- "setFixedIndicatorViewAlpha:"
- "setFixedIndicatorViewBlurProgress:"
- "setFixedIndicatorViewTransform:"
- "setFrame:"
- "setHitTestsAsOpaque:"
- "setIndicatorViewAlpha:"
- "setIndicatorViewBlurProgress:"
- "setIndicatorViewTransform:"
- "setInvalidationLayoutModeChangeReason:"
- "setLayoutAxis:"
- "setLayoutHost:"
- "setLayoutMode:"
- "setLayoutMode:reason:"
- "setLayoutMode:reason:forTargetWithOverrider:"
- "setLeadingTransformView:"
- "setLeadingViewAlpha:"
- "setLeadingViewBlurProgress:"
- "setLeadingViewScale:"
- "setLeadingViewSquishProgress:"
- "setLeadingViewTransform:"
- "setMinimalTransformView:"
- "setMinimalViewAlpha:"
- "setMinimalViewBlurProgress:"
- "setMinimalViewScale:"
- "setMinimalViewSquishProgress:"
- "setMinimalViewTransform:"
- "setNeedsLayout"
- "setObject:forKey:"
- "setOverrideUserInterfaceStyle:"
- "setPerformingSystemApertureCustomContentTransition:"
- "setPerformingSystemApertureInertTransition:"
- "setPreferredLayoutMode:reason:"
- "setPreferredLayoutMode:reason:forTargetWithOverrider:"
- "setProvidedView:"
- "setRemovedOnCompletion:"
- "setSauiBlurRadius:"
- "setSensorObscuringShadowProgress:"
- "setSnapshotViewAlpha:"
- "setSnapshotViewBlurProgress:"
- "setSourceLayer:"
- "setSourcePoints:"
- "setSourceView:"
- "setTintColor:"
- "setTrailingTransformView:"
- "setTrailingViewAlpha:"
- "setTrailingViewBlurProgress:"
- "setTrailingViewScale:"
- "setTrailingViewSquishProgress:"
- "setTrailingViewTransform:"
- "setTransform:"
- "setUserInteractionEnabled:"
- "setUsesNormalizedCoordinates:"
- "setValue:forKeyPath:"
- "size"
- "sizeThatFits:"
- "sizeThatFitsSize:forProvidedView:inLayoutMode:"
- "sizeThatFitsSize:forProvidedView:inLayoutMode:forTargetWithOverrider:isDefaultValue:"
- "snapshotView"
- "snapshotViewAfterScreenUpdates:"
- "snapshotViewAlpha"
- "snapshotViewBlurProgress"
- "sortUsingComparator:"
- "sourceLayer"
- "sourceView"
- "stringByAppendingFormat:"
- "stringWithFormat:"
- "strongToStrongObjectsMapTable"
- "strongToWeakObjectsMapTable"
- "suggestedOutsetsForLayoutMode:maximumOutsets:"
- "superclass"
- "superview"
- "systemApertureLayoutSpecifyingOverrider"
- "systemApertureManagerMaximumNumberOfSimultaneouslyVisibleElements:"
- "systemApertureManagerRequestsHostNeedsLayout:"
- "systemManagedAlertingActivityAssertionWithReason:"
- "systemManagedAlertingActivityAssertionWithReason:preferredLayoutMode:"
- "systemOrangeColor"
- "temporallyOrderedAlertingActivityAssertions"
- "timeIntervalSinceDate:"
- "tintColor"
- "trackingTransition"
- "trailingTransformView"
- "trailingView"
- "trailingViewAlpha"
- "trailingViewBlurProgress"
- "trailingViewScale"
- "trailingViewSquishProgress"
- "trailingViewTransform"
- "traitCollection"
- "transform"
- "uniqueElementIdentifier"
- "uniquelyIdentifyElement"
- "unsignedIntegerValue"
- "v112@0:8d16d24d32{CGAffineTransform=dddddd}40B88B92@96@104"
- "v112@0:8d16{CGSize=dd}24{CGAffineTransform=dddddd}40@88@96B104B108"
- "v16@0:8"
- "v20@0:8B16"
- "v24@0:8@\"<SABehaviorOverridingParticipant>\"16"
- "v24@0:8@\"<SAElement>\"16"
- "v24@0:8@\"<SAUIElementViewControlling>\"16"
- "v24@0:8@\"<SAUIElementViewControllingObserving>\"16"
- "v24@0:8@\"<SAUIIndicatorLayoutSpecifying>\"16"
- "v24@0:8@\"<SAUILayoutHosting>\"16"
- "v24@0:8@\"<SAUILayoutSpecifying>\"16"
- "v24@0:8@\"NSUUID\"16"
- "v24@0:8@\"UIView\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v24@0:8q16"
- "v28@0:8Q16B24"
- "v32@0:8:16@?24"
- "v32@0:8@\"NSUUID\"16@\"NSString\"24"
- "v32@0:8@\"SAUIElementView\"16@\"UIView\"24"
- "v32@0:8@\"UIView\"16@\"<SAUILayoutSpecifyingOverriding>\"24"
- "v32@0:8@16@24"
- "v32@0:8@16q24"
- "v32@0:8d16@24"
- "v32@0:8q16q24"
- "v32@0:8{CGSize=dd}16"
- "v40@0:8q16q24@\"<SAUILayoutSpecifyingOverriding>\"32"
- "v40@0:8q16q24@32"
- "v40@0:8{CGSize=dd}16@32"
- "v48@0:8{CGSize=dd}16@\"UIView\"32@\"<UIViewControllerTransitionCoordinator>\"40"
- "v48@0:8{CGSize=dd}16@32@40"
- "v56@?0@\"_SAUIProvidedViewContainerView\"8@\"UIView\"16{CGRect={CGPoint=dd}{CGSize=dd}}24"
- "v64@0:8{CGAffineTransform=dddddd}16"
- "valueForKey:"
- "valueForKeyPath:"
- "valueWithCGPoint:"
- "view"
- "viewDidAppear:"
- "viewDidDisappear:"
- "viewDidLayoutSubviews"
- "viewDidLoad"
- "viewIfLoaded"
- "viewProvider"
- "viewProviderSensorShadowOpacityFactor:"
- "viewProviderShouldMakeSensorShadowVisible:"
- "viewWillAppear:"
- "viewWillDisappear:"
- "viewWillLayoutSubviews"
- "viewWillTransitionToSize:withTransitionCoordinator:"
- "weakObjectsPointerArray"
- "weakToStrongObjectsMapTable"
- "willMoveToWindow:"
- "window"
- "zone"
- "{CGAffineTransform=\"a\"d\"b\"d\"c\"d\"d\"d\"tx\"d\"ty\"d}"
- "{CGAffineTransform=dddddd}16@0:8"
- "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8@\"UIView\"16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}24@0:8@16"
- "{CGRect={CGPoint=dd}{CGSize=dd}}32@0:8@\"<SAElementViewProviding>\"16@\"UIView\"24"
- "{CGRect={CGPoint=dd}{CGSize=dd}}32@0:8@\"UIView\"16@\"<SAElementViewProviding>\"24"
- "{CGRect={CGPoint=dd}{CGSize=dd}}32@0:8@16@24"
- "{CGSize=\"width\"d\"height\"d}"
- "{CGSize=dd}16@0:8"
- "{CGSize=dd}24@0:8@\"SAUIElementView\"16"
- "{CGSize=dd}24@0:8@16"
- "{CGSize=dd}32@0:8@\"UIView\"16@\"<SAElementViewProviding>\"24"
- "{CGSize=dd}32@0:8@16@24"
- "{CGSize=dd}48@0:8{CGSize=dd}16@\"UIView\"32q40"
- "{CGSize=dd}48@0:8{CGSize=dd}16@32q40"
- "{CGSize=dd}64@0:8{CGSize=dd}16@\"UIView\"32q40@\"<SAUILayoutSpecifyingOverriding>\"48^B56"
- "{CGSize=dd}64@0:8{CGSize=dd}16@32q40@48^B56"
- "{NSDirectionalEdgeInsets=dddd}104@0:8q16{NSDirectionalEdgeInsets=dddd}24{NSDirectionalEdgeInsets=dddd}56@\"<SAUILayoutSpecifyingOverriding>\"88^B96"
- "{NSDirectionalEdgeInsets=dddd}104@0:8q16{NSDirectionalEdgeInsets=dddd}24{NSDirectionalEdgeInsets=dddd}56@88^B96"
- "{NSDirectionalEdgeInsets=dddd}32@0:8{CGSize=dd}16"
- "{NSDirectionalEdgeInsets=dddd}56@0:8q16{NSDirectionalEdgeInsets=dddd}24"
- "{NSDirectionalEdgeInsets=dddd}88@0:8q16{NSDirectionalEdgeInsets=dddd}24{NSDirectionalEdgeInsets=dddd}56"
- "\xa1!"

```
