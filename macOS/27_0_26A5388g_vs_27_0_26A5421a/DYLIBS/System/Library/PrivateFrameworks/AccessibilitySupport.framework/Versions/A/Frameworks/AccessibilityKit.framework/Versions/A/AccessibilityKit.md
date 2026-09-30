## AccessibilityKit

> `/System/Library/PrivateFrameworks/AccessibilitySupport.framework/Versions/A/Frameworks/AccessibilityKit.framework/Versions/A/AccessibilityKit`

```diff

-450.0.0.0.0
-  __TEXT.__text: 0x4bb70
-  __TEXT.__objc_methlist: 0x3a84
-  __TEXT.__const: 0x319
+453.0.0.0.0
+  __TEXT.__text: 0x50a34
+  __TEXT.__objc_methlist: 0x4234
+  __TEXT.__const: 0x339
   __TEXT.__gcc_except_tab: 0x568
-  __TEXT.__cstring: 0x3348
+  __TEXT.__cstring: 0x33db
   __TEXT.__ustring: 0x12e
   __TEXT.__dlopen_cstrs: 0x72
   __TEXT.__oslogstring: 0x830
-  __TEXT.__unwind_info: 0x1118
+  __TEXT.__unwind_info: 0x1250
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x260
-  __DATA_CONST.__objc_classlist: 0x1e8
+  __DATA_CONST.__const: 0x2a0
+  __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x58
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2d90
-  __DATA_CONST.__objc_superrefs: 0x118
+  __DATA_CONST.__objc_selrefs: 0x30e8
+  __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0xf8
-  __DATA_CONST.__got: 0x708
-  __AUTH_CONST.__const: 0x13e0
-  __AUTH_CONST.__cfstring: 0x18e0
-  __AUTH_CONST.__objc_const: 0x7460
+  __DATA_CONST.__got: 0x768
+  __AUTH_CONST.__const: 0x13d0
+  __AUTH_CONST.__cfstring: 0x19c0
+  __AUTH_CONST.__objc_const: 0x9360
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x480
-  __AUTH.__objc_data: 0x12c0
-  __DATA.__objc_ivar: 0x3b8
-  __DATA.__data: 0x422
-  __DATA.__bss: 0x1b0
+  __AUTH_CONST.__auth_got: 0x498
+  __AUTH.__objc_data: 0x1680
+  __DATA.__objc_ivar: 0x454
+  __DATA.__data: 0x542
+  __DATA.__bss: 0x1d0
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x38
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit

   - /System/Library/PrivateFrameworks/SoftLinking.framework/Versions/A/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1865
-  Symbols:   4179
-  CStrings:  513
+  Functions: 2014
+  Symbols:   4595
+  CStrings:  521
 
Symbols:
+ +[AXKApplicationController isSpotlightApplicationIdentifier:]
+ +[AXKDescribeSessionContext contextWithContentRoot:window:blocks:]
+ +[AXKFetchContext contextForWindow:duration:scrollArea:]
+ +[AXKFrameTargetScrollStrategy sharedStrategy]
+ +[AXKLoadMoreRequest requestFromSession:direction:fetchContext:]
+ +[AXKLoadMoreResult emptyResult]
+ +[AXKLoadMoreResult resultWithBlocks:boundaryStale:]
+ +[AXKPageActionStrategy sharedStrategy]
+ -[AXKContentExtractor _gatherAttributedContentForElement:contentRange:visibleRange:fallbackLabel:didExtractFullRange:]
+ -[AXKContentWalker walkContentForWinner:boundary:direction:seenBlockTexts:context:]
+ -[AXKDelegateDispatcher signalBoundaryInvalidInDirection:toDelegate:]
+ -[AXKDelegateDispatcher signalContentNotFoundToDelegate:]
+ -[AXKDelegateDispatcher signalDidFinishDescribingElementsInDirection:readableContent:toDelegate:]
+ -[AXKDelegateDispatcher signalHasNoContentInDirection:toDelegate:]
+ -[AXKDescribeSessionContext .cxx_destruct]
+ -[AXKDescribeSessionContext _cachedScrollAreaResolved]
+ -[AXKDescribeSessionContext _cachedScrollArea]
+ -[AXKDescribeSessionContext _positionProviderResolved]
+ -[AXKDescribeSessionContext _positionProvider]
+ -[AXKDescribeSessionContext backwardBoundary]
+ -[AXKDescribeSessionContext contentRoot]
+ -[AXKDescribeSessionContext forwardBoundary]
+ -[AXKDescribeSessionContext init]
+ -[AXKDescribeSessionContext lastBackwardFrontierPosition]
+ -[AXKDescribeSessionContext lastForwardFrontierPosition]
+ -[AXKDescribeSessionContext reachedEndBackward]
+ -[AXKDescribeSessionContext reachedEndForward]
+ -[AXKDescribeSessionContext recordBlocks:]
+ -[AXKDescribeSessionContext resolvePositionProvider]
+ -[AXKDescribeSessionContext resolveScrollArea]
+ -[AXKDescribeSessionContext seedInitialFrontierPositionsForwardEdge:backwardEdge:]
+ -[AXKDescribeSessionContext seenBlockTexts]
+ -[AXKDescribeSessionContext setBackwardBoundary:]
+ -[AXKDescribeSessionContext setContentRoot:]
+ -[AXKDescribeSessionContext setForwardBoundary:]
+ -[AXKDescribeSessionContext setLastBackwardFrontierPosition:]
+ -[AXKDescribeSessionContext setLastForwardFrontierPosition:]
+ -[AXKDescribeSessionContext setReachedEndBackward:]
+ -[AXKDescribeSessionContext setReachedEndForward:]
+ -[AXKDescribeSessionContext setSeenBlockTexts:]
+ -[AXKDescribeSessionContext setWindowElement:]
+ -[AXKDescribeSessionContext set_cachedScrollArea:]
+ -[AXKDescribeSessionContext set_cachedScrollAreaResolved:]
+ -[AXKDescribeSessionContext set_positionProvider:]
+ -[AXKDescribeSessionContext set_positionProviderResolved:]
+ -[AXKDescribeSessionContext updateFrontierPosition:forDirection:]
+ -[AXKDescribeSessionContext windowElement]
+ -[AXKFetchContext .cxx_destruct]
+ -[AXKFetchContext cachedScrollArea]
+ -[AXKFetchContext setCachedScrollArea:]
+ -[AXKFramePosition compare:]
+ -[AXKFramePosition debugDescription]
+ -[AXKFramePosition initWithValue:]
+ -[AXKFramePosition signedDistanceTo:]
+ -[AXKFramePosition value]
+ -[AXKFramePositionProvider .cxx_destruct]
+ -[AXKFramePositionProvider _windowElement]
+ -[AXKFramePositionProvider currentPosition]
+ -[AXKFramePositionProvider initWithWindowElement:]
+ -[AXKFramePositionProvider positionForElement:]
+ -[AXKFramePositionProvider set_windowElement:]
+ -[AXKFramePositionProvider signalIsStableAcrossVirtualization]
+ -[AXKFramePositionProvider significantSeekDistance]
+ -[AXKFramePositionProvider trySeekToPosition:]
+ -[AXKFrameTargetScrollStrategy applyToWinner:boundary:scrollArea:direction:]
+ -[AXKFrameTargetScrollStrategy canApplyToWinner:boundary:scrollArea:direction:]
+ -[AXKFrameTargetScrollStrategy isIterationSafe]
+ -[AXKHarvestAccumulator .cxx_destruct]
+ -[AXKHarvestAccumulator _direction]
+ -[AXKHarvestAccumulator _mutableBlocks]
+ -[AXKHarvestAccumulator _mutableSeen]
+ -[AXKHarvestAccumulator addBlocks:]
+ -[AXKHarvestAccumulator blocks]
+ -[AXKHarvestAccumulator characterCount]
+ -[AXKHarvestAccumulator initWithDirection:seenSeed:]
+ -[AXKHarvestAccumulator seenKeys]
+ -[AXKHarvestAccumulator setCharacterCount:]
+ -[AXKHarvestAccumulator set_direction:]
+ -[AXKHarvestAccumulator set_mutableBlocks:]
+ -[AXKHarvestAccumulator set_mutableSeen:]
+ -[AXKLoadMoreRequest .cxx_destruct]
+ -[AXKLoadMoreRequest boundary]
+ -[AXKLoadMoreRequest direction]
+ -[AXKLoadMoreRequest fetchContext]
+ -[AXKLoadMoreRequest initWithWinner:boundary:direction:fetchContext:seenBlockTexts:recordedFrontierPosition:positionProvider:]
+ -[AXKLoadMoreRequest positionProvider]
+ -[AXKLoadMoreRequest recordedFrontierPosition]
+ -[AXKLoadMoreRequest seenBlockTexts]
+ -[AXKLoadMoreRequest winner]
+ -[AXKLoadMoreResult .cxx_destruct]
+ -[AXKLoadMoreResult blocks]
+ -[AXKLoadMoreResult boundaryStale]
+ -[AXKLoadMoreResult initWithBlocks:boundaryStale:]
+ -[AXKLoaderHarvestPrep .cxx_destruct]
+ -[AXKLoaderHarvestPrep abortHarvest]
+ -[AXKLoaderHarvestPrep accumulator]
+ -[AXKLoaderHarvestPrep boundary]
+ -[AXKLoaderHarvestPrep setAbortHarvest:]
+ -[AXKLoaderHarvestPrep setAccumulator:]
+ -[AXKLoaderHarvestPrep setBoundary:]
+ -[AXKPageActionStrategy applyToWinner:boundary:scrollArea:direction:]
+ -[AXKPageActionStrategy canApplyToWinner:boundary:scrollArea:direction:]
+ -[AXKPageActionStrategy isIterationSafe]
+ -[AXKScreenDescriber _loadMoreContentInDirection:]
+ -[AXKScreenDescriber _scrollLoader]
+ -[AXKScreenDescriber _sessionContext]
+ -[AXKScreenDescriber hasReachedEndInDirection:]
+ -[AXKScreenDescriber loadMoreContentInDirection:]
+ -[AXKScreenDescriber set_scrollLoader:]
+ -[AXKScreenDescriber set_sessionContext:]
+ -[AXKScreenDescriberReadableContent canonicalBlockKey]
+ -[AXKScreenDescriberReadableContent coversFullTextRange]
+ -[AXKScreenDescriberReadableContent initWithElement:applicationElement:windowElement:topLevelElement:content:contentTitle:applicationIdentifier:contentURL:frame:coversFullTextRange:]
+ -[AXKScrollLoader .cxx_destruct]
+ -[AXKScrollLoader _harvestMaterializedFromChildren:boundaryIndex:direction:seen:context:]
+ -[AXKScrollLoader _materializedResultForRequest:]
+ -[AXKScrollLoader _prepareSourceForHarvestWithRequest:scrollArea:]
+ -[AXKScrollLoader _reAnchorBoundaryForWinner:scrollArea:direction:seenBlocks:recordedFrontierPosition:positionProvider:context:]
+ -[AXKScrollLoader _runScrollLoopWithAccumulator:request:boundary:scrollArea:]
+ -[AXKScrollLoader _scrollResultForRequest:scrollArea:]
+ -[AXKScrollLoader _setStrategiesForTesting:]
+ -[AXKScrollLoader _strategies]
+ -[AXKScrollLoader _walkContentIntoAccumulator:request:boundary:]
+ -[AXKScrollLoader _walker]
+ -[AXKScrollLoader initWithWalker:strategies:]
+ -[AXKScrollLoader loadMoreForRequest:]
+ -[AXKScrollLoader set_strategies:]
+ -[AXKScrollLoader set_walker:]
+ -[AXKScrollbarPosition compare:]
+ -[AXKScrollbarPosition debugDescription]
+ -[AXKScrollbarPosition initWithValue:]
+ -[AXKScrollbarPosition signedDistanceTo:]
+ -[AXKScrollbarPosition value]
+ -[AXKScrollbarPositionProvider .cxx_destruct]
+ -[AXKScrollbarPositionProvider _scrollArea]
+ -[AXKScrollbarPositionProvider currentPosition]
+ -[AXKScrollbarPositionProvider initWithScrollArea:]
+ -[AXKScrollbarPositionProvider positionForElement:]
+ -[AXKScrollbarPositionProvider set_scrollArea:]
+ -[AXKScrollbarPositionProvider signalIsStableAcrossVirtualization]
+ -[AXKScrollbarPositionProvider significantSeekDistance]
+ -[AXKScrollbarPositionProvider trySeekToPosition:]
+ GCC_except_table112
+ OBJC_IVAR_$_AXKDescribeSessionContext.__cachedScrollArea
+ OBJC_IVAR_$_AXKDescribeSessionContext.__cachedScrollAreaResolved
+ OBJC_IVAR_$_AXKDescribeSessionContext.__positionProvider
+ OBJC_IVAR_$_AXKDescribeSessionContext.__positionProviderResolved
+ OBJC_IVAR_$_AXKDescribeSessionContext._backwardBoundary
+ OBJC_IVAR_$_AXKDescribeSessionContext._contentRoot
+ OBJC_IVAR_$_AXKDescribeSessionContext._forwardBoundary
+ OBJC_IVAR_$_AXKDescribeSessionContext._lastBackwardFrontierPosition
+ OBJC_IVAR_$_AXKDescribeSessionContext._lastForwardFrontierPosition
+ OBJC_IVAR_$_AXKDescribeSessionContext._reachedEndBackward
+ OBJC_IVAR_$_AXKDescribeSessionContext._reachedEndForward
+ OBJC_IVAR_$_AXKDescribeSessionContext._seenBlockTexts
+ OBJC_IVAR_$_AXKDescribeSessionContext._windowElement
+ OBJC_IVAR_$_AXKFetchContext._cachedScrollArea
+ OBJC_IVAR_$_AXKFramePosition._value
+ OBJC_IVAR_$_AXKFramePositionProvider.__windowElement
+ OBJC_IVAR_$_AXKHarvestAccumulator.__direction
+ OBJC_IVAR_$_AXKHarvestAccumulator.__mutableBlocks
+ OBJC_IVAR_$_AXKHarvestAccumulator.__mutableSeen
+ OBJC_IVAR_$_AXKHarvestAccumulator._characterCount
+ OBJC_IVAR_$_AXKLoadMoreRequest._boundary
+ OBJC_IVAR_$_AXKLoadMoreRequest._direction
+ OBJC_IVAR_$_AXKLoadMoreRequest._fetchContext
+ OBJC_IVAR_$_AXKLoadMoreRequest._positionProvider
+ OBJC_IVAR_$_AXKLoadMoreRequest._recordedFrontierPosition
+ OBJC_IVAR_$_AXKLoadMoreRequest._seenBlockTexts
+ OBJC_IVAR_$_AXKLoadMoreRequest._winner
+ OBJC_IVAR_$_AXKLoadMoreResult._blocks
+ OBJC_IVAR_$_AXKLoadMoreResult._boundaryStale
+ OBJC_IVAR_$_AXKLoaderHarvestPrep._abortHarvest
+ OBJC_IVAR_$_AXKLoaderHarvestPrep._accumulator
+ OBJC_IVAR_$_AXKLoaderHarvestPrep._boundary
+ OBJC_IVAR_$_AXKScreenDescriber.__scrollLoader
+ OBJC_IVAR_$_AXKScreenDescriber.__sessionContext
+ OBJC_IVAR_$_AXKScreenDescriberReadableContent._coversFullTextRange
+ OBJC_IVAR_$_AXKScrollLoader.__strategies
+ OBJC_IVAR_$_AXKScrollLoader.__walker
+ OBJC_IVAR_$_AXKScrollbarPosition._value
+ OBJC_IVAR_$_AXKScrollbarPositionProvider.__scrollArea
+ _AXFApplicationIdentifierCampo
+ _CGRectContainsPoint
+ _CGRectGetMidY
+ _CGRectZero
+ _OBJC_CLASS_$_AXKDescribeSessionContext
+ _OBJC_CLASS_$_AXKFramePosition
+ _OBJC_CLASS_$_AXKFramePositionProvider
+ _OBJC_CLASS_$_AXKFrameTargetScrollStrategy
+ _OBJC_CLASS_$_AXKHarvestAccumulator
+ _OBJC_CLASS_$_AXKLoadMoreRequest
+ _OBJC_CLASS_$_AXKLoadMoreResult
+ _OBJC_CLASS_$_AXKLoaderHarvestPrep
+ _OBJC_CLASS_$_AXKPageActionStrategy
+ _OBJC_CLASS_$_AXKScrollLoader
+ _OBJC_CLASS_$_AXKScrollbarPosition
+ _OBJC_CLASS_$_AXKScrollbarPositionProvider
+ _OBJC_CLASS_$_NSIndexSet
+ _OBJC_METACLASS_$_AXKDescribeSessionContext
+ _OBJC_METACLASS_$_AXKFramePosition
+ _OBJC_METACLASS_$_AXKFramePositionProvider
+ _OBJC_METACLASS_$_AXKFrameTargetScrollStrategy
+ _OBJC_METACLASS_$_AXKHarvestAccumulator
+ _OBJC_METACLASS_$_AXKLoadMoreRequest
+ _OBJC_METACLASS_$_AXKLoadMoreResult
+ _OBJC_METACLASS_$_AXKLoaderHarvestPrep
+ _OBJC_METACLASS_$_AXKPageActionStrategy
+ _OBJC_METACLASS_$_AXKScrollLoader
+ _OBJC_METACLASS_$_AXKScrollbarPosition
+ _OBJC_METACLASS_$_AXKScrollbarPositionProvider
+ __AXKAnchorForFrameTarget
+ __AXKCaptureScrollSnapshot
+ __AXKElementIsScrollable
+ __AXKElementSupportsAnyPageAction
+ __AXKEnclosingScrollAreaForElement
+ __AXKPageActionNamesForDirection
+ __AXKReadingOrderSiblingOf
+ __AXKRealizeIfVirtualized
+ __AXKScrollAreaForFrameTarget
+ __AXKScrollbarValueForScrollArea
+ __AXKSetScrollbarValueForScrollArea
+ __AXKVerticalScrollBarForScrollArea
+ __OBJC_$_CLASS_METHODS_AXKApplicationController
+ __OBJC_$_CLASS_METHODS_AXKDescribeSessionContext
+ __OBJC_$_CLASS_METHODS_AXKFrameTargetScrollStrategy
+ __OBJC_$_CLASS_METHODS_AXKLoadMoreRequest
+ __OBJC_$_CLASS_METHODS_AXKLoadMoreResult
+ __OBJC_$_CLASS_METHODS_AXKPageActionStrategy
+ __OBJC_$_INSTANCE_METHODS_AXKDescribeSessionContext
+ __OBJC_$_INSTANCE_METHODS_AXKFramePosition
+ __OBJC_$_INSTANCE_METHODS_AXKFramePositionProvider
+ __OBJC_$_INSTANCE_METHODS_AXKFrameTargetScrollStrategy
+ __OBJC_$_INSTANCE_METHODS_AXKHarvestAccumulator
+ __OBJC_$_INSTANCE_METHODS_AXKLoadMoreRequest
+ __OBJC_$_INSTANCE_METHODS_AXKLoadMoreResult
+ __OBJC_$_INSTANCE_METHODS_AXKLoaderHarvestPrep
+ __OBJC_$_INSTANCE_METHODS_AXKPageActionStrategy
+ __OBJC_$_INSTANCE_METHODS_AXKScrollLoader
+ __OBJC_$_INSTANCE_METHODS_AXKScrollbarPosition
+ __OBJC_$_INSTANCE_METHODS_AXKScrollbarPositionProvider
+ __OBJC_$_INSTANCE_VARIABLES_AXKDescribeSessionContext
+ __OBJC_$_INSTANCE_VARIABLES_AXKFramePosition
+ __OBJC_$_INSTANCE_VARIABLES_AXKFramePositionProvider
+ __OBJC_$_INSTANCE_VARIABLES_AXKHarvestAccumulator
+ __OBJC_$_INSTANCE_VARIABLES_AXKLoadMoreRequest
+ __OBJC_$_INSTANCE_VARIABLES_AXKLoadMoreResult
+ __OBJC_$_INSTANCE_VARIABLES_AXKLoaderHarvestPrep
+ __OBJC_$_INSTANCE_VARIABLES_AXKScrollLoader
+ __OBJC_$_INSTANCE_VARIABLES_AXKScrollbarPosition
+ __OBJC_$_INSTANCE_VARIABLES_AXKScrollbarPositionProvider
+ __OBJC_$_PROP_LIST_AXKDescribeSessionContext
+ __OBJC_$_PROP_LIST_AXKFramePosition
+ __OBJC_$_PROP_LIST_AXKFramePositionProvider
+ __OBJC_$_PROP_LIST_AXKFrameTargetScrollStrategy
+ __OBJC_$_PROP_LIST_AXKHarvestAccumulator
+ __OBJC_$_PROP_LIST_AXKLoadMoreRequest
+ __OBJC_$_PROP_LIST_AXKLoadMoreResult
+ __OBJC_$_PROP_LIST_AXKLoaderHarvestPrep
+ __OBJC_$_PROP_LIST_AXKPageActionStrategy
+ __OBJC_$_PROP_LIST_AXKScrollLoader
+ __OBJC_$_PROP_LIST_AXKScrollStrategy
+ __OBJC_$_PROP_LIST_AXKScrollbarPosition
+ __OBJC_$_PROP_LIST_AXKScrollbarPositionProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AXKDocumentPosition
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AXKPositionProvider
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AXKScrollStrategy
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AXKDocumentPosition
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AXKPositionProvider
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AXKScrollStrategy
+ __OBJC_$_PROTOCOL_REFS_AXKDocumentPosition
+ __OBJC_$_PROTOCOL_REFS_AXKPositionProvider
+ __OBJC_$_PROTOCOL_REFS_AXKScrollStrategy
+ __OBJC_CLASS_PROTOCOLS_$_AXKFramePosition
+ __OBJC_CLASS_PROTOCOLS_$_AXKFramePositionProvider
+ __OBJC_CLASS_PROTOCOLS_$_AXKFrameTargetScrollStrategy
+ __OBJC_CLASS_PROTOCOLS_$_AXKPageActionStrategy
+ __OBJC_CLASS_PROTOCOLS_$_AXKScrollbarPosition
+ __OBJC_CLASS_PROTOCOLS_$_AXKScrollbarPositionProvider
+ __OBJC_CLASS_RO_$_AXKDescribeSessionContext
+ __OBJC_CLASS_RO_$_AXKFramePosition
+ __OBJC_CLASS_RO_$_AXKFramePositionProvider
+ __OBJC_CLASS_RO_$_AXKFrameTargetScrollStrategy
+ __OBJC_CLASS_RO_$_AXKHarvestAccumulator
+ __OBJC_CLASS_RO_$_AXKLoadMoreRequest
+ __OBJC_CLASS_RO_$_AXKLoadMoreResult
+ __OBJC_CLASS_RO_$_AXKLoaderHarvestPrep
+ __OBJC_CLASS_RO_$_AXKPageActionStrategy
+ __OBJC_CLASS_RO_$_AXKScrollLoader
+ __OBJC_CLASS_RO_$_AXKScrollbarPosition
+ __OBJC_CLASS_RO_$_AXKScrollbarPositionProvider
+ __OBJC_LABEL_PROTOCOL_$_AXKDocumentPosition
+ __OBJC_LABEL_PROTOCOL_$_AXKPositionProvider
+ __OBJC_LABEL_PROTOCOL_$_AXKScrollStrategy
+ __OBJC_METACLASS_RO_$_AXKDescribeSessionContext
+ __OBJC_METACLASS_RO_$_AXKFramePosition
+ __OBJC_METACLASS_RO_$_AXKFramePositionProvider
+ __OBJC_METACLASS_RO_$_AXKFrameTargetScrollStrategy
+ __OBJC_METACLASS_RO_$_AXKHarvestAccumulator
+ __OBJC_METACLASS_RO_$_AXKLoadMoreRequest
+ __OBJC_METACLASS_RO_$_AXKLoadMoreResult
+ __OBJC_METACLASS_RO_$_AXKLoaderHarvestPrep
+ __OBJC_METACLASS_RO_$_AXKPageActionStrategy
+ __OBJC_METACLASS_RO_$_AXKScrollLoader
+ __OBJC_METACLASS_RO_$_AXKScrollbarPosition
+ __OBJC_METACLASS_RO_$_AXKScrollbarPositionProvider
+ __OBJC_PROTOCOL_$_AXKDocumentPosition
+ __OBJC_PROTOCOL_$_AXKPositionProvider
+ __OBJC_PROTOCOL_$_AXKScrollStrategy
+ __SupportedPageActionForElement
+ ___39+[AXKPageActionStrategy sharedStrategy]_block_invoke
+ ___46+[AXKFrameTargetScrollStrategy sharedStrategy]_block_invoke
+ ___49-[AXKScreenDescriber loadMoreContentInDirection:]_block_invoke
+ ___57-[AXKDelegateDispatcher signalContentNotFoundToDelegate:]_block_invoke
+ ___66-[AXKDelegateDispatcher signalHasNoContentInDirection:toDelegate:]_block_invoke
+ ___69-[AXKDelegateDispatcher signalBoundaryInvalidInDirection:toDelegate:]_block_invoke
+ ___97-[AXKDelegateDispatcher signalDidFinishDescribingElementsInDirection:readableContent:toDelegate:]_block_invoke
+ ___block_descriptor_32_e38_v16?0"<AXKScreenDescriberDelegate>"8l
+ ___block_descriptor_40_e38_v16?0"<AXKScreenDescriberDelegate>"8l
+ ___block_descriptor_48_e8_32s_e34_v16?0"AXKApplicationController"8l
+ _objc_msgSend$_accessibilityNextContentSibling
+ _objc_msgSend$_accessibilityPreviousContentSibling
+ _objc_msgSend$_cachedScrollArea
+ _objc_msgSend$_cachedScrollAreaResolved
+ _objc_msgSend$_direction
+ _objc_msgSend$_gatherAttributedContentForElement:contentRange:visibleRange:fallbackLabel:didExtractFullRange:
+ _objc_msgSend$_harvestMaterializedFromChildren:boundaryIndex:direction:seen:context:
+ _objc_msgSend$_loadMoreContentInDirection:
+ _objc_msgSend$_materializedResultForRequest:
+ _objc_msgSend$_mutableBlocks
+ _objc_msgSend$_mutableSeen
+ _objc_msgSend$_positionProvider
+ _objc_msgSend$_positionProviderResolved
+ _objc_msgSend$_prepareSourceForHarvestWithRequest:scrollArea:
+ _objc_msgSend$_reAnchorBoundaryForWinner:scrollArea:direction:seenBlocks:recordedFrontierPosition:positionProvider:context:
+ _objc_msgSend$_runScrollLoopWithAccumulator:request:boundary:scrollArea:
+ _objc_msgSend$_scrollArea
+ _objc_msgSend$_scrollLoader
+ _objc_msgSend$_scrollResultForRequest:scrollArea:
+ _objc_msgSend$_sessionContext
+ _objc_msgSend$_strategies
+ _objc_msgSend$_walkContentIntoAccumulator:request:boundary:
+ _objc_msgSend$_windowElement
+ _objc_msgSend$abortHarvest
+ _objc_msgSend$accessibilityValueAsNumber
+ _objc_msgSend$accumulator
+ _objc_msgSend$addBlocks:
+ _objc_msgSend$applyToWinner:boundary:scrollArea:direction:
+ _objc_msgSend$backwardBoundary
+ _objc_msgSend$blocks
+ _objc_msgSend$boundary
+ _objc_msgSend$boundaryStale
+ _objc_msgSend$cachedScrollArea
+ _objc_msgSend$canApplyToWinner:boundary:scrollArea:direction:
+ _objc_msgSend$canonicalBlockKey
+ _objc_msgSend$characterCount
+ _objc_msgSend$contentRoot
+ _objc_msgSend$contextForWindow:duration:scrollArea:
+ _objc_msgSend$contextWithContentRoot:window:blocks:
+ _objc_msgSend$coversFullTextRange
+ _objc_msgSend$direction
+ _objc_msgSend$emptyResult
+ _objc_msgSend$fetchContext
+ _objc_msgSend$forwardBoundary
+ _objc_msgSend$hasReachedEndInDirection:
+ _objc_msgSend$indexSetWithIndexesInRange:
+ _objc_msgSend$initWithBlocks:boundaryStale:
+ _objc_msgSend$initWithDirection:seenSeed:
+ _objc_msgSend$initWithElement:applicationElement:windowElement:topLevelElement:content:contentTitle:applicationIdentifier:contentURL:frame:coversFullTextRange:
+ _objc_msgSend$initWithScrollArea:
+ _objc_msgSend$initWithValue:
+ _objc_msgSend$initWithWalker:strategies:
+ _objc_msgSend$initWithWindowElement:
+ _objc_msgSend$initWithWinner:boundary:direction:fetchContext:seenBlockTexts:recordedFrontierPosition:positionProvider:
+ _objc_msgSend$insertObjects:atIndexes:
+ _objc_msgSend$isIterationSafe
+ _objc_msgSend$isPromotable
+ _objc_msgSend$isSpotlightApplicationIdentifier:
+ _objc_msgSend$lastBackwardFrontierPosition
+ _objc_msgSend$lastForwardFrontierPosition
+ _objc_msgSend$loadMoreForRequest:
+ _objc_msgSend$minusSet:
+ _objc_msgSend$positionForElement:
+ _objc_msgSend$positionProvider
+ _objc_msgSend$reachedEndBackward
+ _objc_msgSend$reachedEndForward
+ _objc_msgSend$recordBlocks:
+ _objc_msgSend$recordedFrontierPosition
+ _objc_msgSend$requestFromSession:direction:fetchContext:
+ _objc_msgSend$resolvePositionProvider
+ _objc_msgSend$resolveScrollArea
+ _objc_msgSend$resultWithBlocks:boundaryStale:
+ _objc_msgSend$screenDescriberBoundaryInvalidInDirection:
+ _objc_msgSend$screenDescriberContentNotFound
+ _objc_msgSend$screenDescriberDidFinishDescribingElementsInDirection:readableContent:
+ _objc_msgSend$screenDescriberHasNoContentInDirection:
+ _objc_msgSend$seedInitialFrontierPositionsForwardEdge:backwardEdge:
+ _objc_msgSend$seenBlockTexts
+ _objc_msgSend$seenKeys
+ _objc_msgSend$setAbortHarvest:
+ _objc_msgSend$setAccumulator:
+ _objc_msgSend$setBackwardBoundary:
+ _objc_msgSend$setBoundary:
+ _objc_msgSend$setCachedScrollArea:
+ _objc_msgSend$setCharacterCount:
+ _objc_msgSend$setContentRoot:
+ _objc_msgSend$setForwardBoundary:
+ _objc_msgSend$setLastBackwardFrontierPosition:
+ _objc_msgSend$setLastForwardFrontierPosition:
+ _objc_msgSend$setReachedEndBackward:
+ _objc_msgSend$setReachedEndForward:
+ _objc_msgSend$setWindowElement:
+ _objc_msgSend$setWithCapacity:
+ _objc_msgSend$set_cachedScrollArea:
+ _objc_msgSend$set_cachedScrollAreaResolved:
+ _objc_msgSend$set_direction:
+ _objc_msgSend$set_mutableBlocks:
+ _objc_msgSend$set_mutableSeen:
+ _objc_msgSend$set_positionProvider:
+ _objc_msgSend$set_positionProviderResolved:
+ _objc_msgSend$set_scrollArea:
+ _objc_msgSend$set_scrollLoader:
+ _objc_msgSend$set_sessionContext:
+ _objc_msgSend$set_strategies:
+ _objc_msgSend$set_windowElement:
+ _objc_msgSend$sharedStrategy
+ _objc_msgSend$signalBoundaryInvalidInDirection:toDelegate:
+ _objc_msgSend$signalContentNotFoundToDelegate:
+ _objc_msgSend$signalDidFinishDescribingElementsInDirection:readableContent:toDelegate:
+ _objc_msgSend$signalHasNoContentInDirection:toDelegate:
+ _objc_msgSend$signedDistanceTo:
+ _objc_msgSend$significantSeekDistance
+ _objc_msgSend$trySeekToPosition:
+ _objc_msgSend$updateFrontierPosition:forDirection:
+ _objc_msgSend$walkContentForWinner:boundary:direction:seenBlockTexts:context:
+ _objc_msgSend$windowElement
+ _objc_msgSend$winner
+ _usleep
+ sharedStrategy.instance
+ sharedStrategy.onceToken
- +[AXKFetchContext contextForWindow:duration:]
- -[AXKContentExtractor _gatherAttributedContentForElement:contentRange:visibleRange:fallbackLabel:]
- -[AXKDelegateDispatcher signalContentNotFoundForElement:toDelegate:]
- -[AXKDelegateDispatcher signalDidFinishDescribingElement:toDelegate:]
- -[AXKDelegateDispatcher signalDidFinishDescribingElementsStartingFrom:ofWindow:inDirection:readableContent:toDelegate:]
- -[AXKDelegateDispatcher signalHasNoContentForWindow:inDirection:toDelegate:]
- -[AXKScreenDescriber describeContentStartingFrom:inPage:ofWindow:inDirection:]
- -[AXKScreenDescriber scrollToElement:inPage:ofWindow:inDirection:]
- -[AXKScreenDescriberReadableContent initWithElement:applicationElement:windowElement:topLevelElement:content:contentTitle:applicationIdentifier:contentURL:frame:]
- ___119-[AXKDelegateDispatcher signalDidFinishDescribingElementsStartingFrom:ofWindow:inDirection:readableContent:toDelegate:]_block_invoke
- ___68-[AXKDelegateDispatcher signalContentNotFoundForElement:toDelegate:]_block_invoke
- ___69-[AXKDelegateDispatcher signalDidFinishDescribingElement:toDelegate:]_block_invoke
- ___76-[AXKDelegateDispatcher signalHasNoContentForWindow:inDirection:toDelegate:]_block_invoke
- ___block_descriptor_40_e8_32bs_e34_v16?0"AXKApplicationController"8l
- ___block_descriptor_64_e8_32s40s48s_e38_v16?0"<AXKScreenDescriberDelegate>"8l
- _objc_msgSend$_gatherAttributedContentForElement:contentRange:visibleRange:fallbackLabel:
- _objc_msgSend$contextForWindow:duration:
- _objc_msgSend$initWithElement:applicationElement:windowElement:topLevelElement:content:contentTitle:applicationIdentifier:contentURL:frame:
- _objc_msgSend$screenDescriberContentNotFoundForElement:
- _objc_msgSend$screenDescriberDidFinishDescribingElement:
- _objc_msgSend$screenDescriberDidFinishDescribingElementsStartingFrom:ofWindow:inDirection:readableContent:
- _objc_msgSend$screenDescriberHasNoContentFor:inDirection:
- _objc_msgSend$signalContentNotFoundForElement:toDelegate:
- _objc_msgSend$signalDidFinishDescribingElement:toDelegate:
CStrings:
+ "\""
+ "<FramePosition %.1f>"
+ "<ScrollbarPosition %.4f>"
+ "AXScrollDownByPage"
+ "AXScrollNextPage"
+ "AXScrollPreviousPage"
+ "AXScrollToVisible"
+ "AXScrollUpByPage"
```
