## Silex

> `/System/iOSSupport/System/Library/PrivateFrameworks/Silex.framework/Versions/A/Silex`

```diff

-5626.0.0.0.0
-  __TEXT.__text: 0x10ef44
-  __TEXT.__auth_stubs: 0xf50
-  __TEXT.__objc_methlist: 0x17c7c
+5676.0.3.0.0
+  __TEXT.__text: 0x11377c
+  __TEXT.__auth_stubs: 0xf60
+  __TEXT.__objc_methlist: 0x1dd94
   __TEXT.__const: 0x4bc
-  __TEXT.__cstring: 0x998d
-  __TEXT.__gcc_except_tab: 0x2388
-  __TEXT.__oslogstring: 0x1f1b
+  __TEXT.__cstring: 0x9d04
+  __TEXT.__gcc_except_tab: 0x23b8
+  __TEXT.__oslogstring: 0x2236
   __TEXT.__ustring: 0x6c
-  __TEXT.__unwind_info: 0x50e0
-  __TEXT.__objc_classname: 0x7488
-  __TEXT.__objc_methname: 0x39dc8
-  __TEXT.__objc_methtype: 0xdfec
-  __TEXT.__objc_stubs: 0x22e40
-  __DATA_CONST.__got: 0x2458
-  __DATA_CONST.__const: 0x3ab8
-  __DATA_CONST.__objc_classlist: 0x1c08
-  __DATA_CONST.__objc_catlist: 0xc0
-  __DATA_CONST.__objc_protolist: 0xce0
+  __TEXT.__unwind_info: 0x51f0
+  __TEXT.__objc_classname: 0x75a4
+  __TEXT.__objc_methname: 0x3adbf
+  __TEXT.__objc_methtype: 0xe3e6
+  __TEXT.__objc_stubs: 0x23900
+  __DATA_CONST.__got: 0x24b0
+  __DATA_CONST.__const: 0x3b70
+  __DATA_CONST.__objc_classlist: 0x1c68
+  __DATA_CONST.__objc_catlist: 0xc8
+  __DATA_CONST.__objc_protolist: 0xcf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa768
-  __DATA_CONST.__objc_protorefs: 0x550
-  __DATA_CONST.__objc_superrefs: 0xfd0
+  __DATA_CONST.__objc_selrefs: 0xb5b0
+  __DATA_CONST.__objc_protorefs: 0x568
+  __DATA_CONST.__objc_superrefs: 0x1018
   __DATA_CONST.__objc_arraydata: 0x3cc8
-  __AUTH_CONST.__auth_got: 0x7c0
-  __AUTH_CONST.__const: 0x3b60
-  __AUTH_CONST.__cfstring: 0x93e0
-  __AUTH_CONST.__objc_const: 0x59390
+  __AUTH_CONST.__auth_got: 0x7c8
+  __AUTH_CONST.__const: 0x3be0
+  __AUTH_CONST.__cfstring: 0x9580
+  __AUTH_CONST.__objc_const: 0x50668
   __AUTH_CONST.__objc_intobj: 0x3d8
   __AUTH_CONST.__objc_arrayobj: 0x300
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x2aa8
-  __AUTH.__objc_data: 0x62c0
-  __DATA.__objc_ivar: 0x1ea0
-  __DATA.__data: 0x9b50
-  __DATA.__bss: 0xc8
-  __DATA.__common: 0x8
+  __AUTH.__objc_data: 0x6680
+  __DATA.__objc_ivar: 0x1f28
+  __DATA.__data: 0x9ca8
+  __DATA.__bss: 0xd8
+  __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0xb590
   __DATA_DIRTY.__bss: 0x150
   __DATA_DIRTY.__common: 0x48

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4F6B7768-8260-31DD-AAF3-94E6A37A5612
-  Functions: 8241
-  Symbols:   25182
-  CStrings:  14190
+  UUID: 022F1F88-E89B-3D90-8322-E6EC57726D78
+  Functions: 8416
+  Symbols:   25617
+  CStrings:  14443
 
Symbols:
+ +[SXComponentLayoutRules(Definitions) bodyComponentLayoutRules].cold.1
+ +[SXComponentLayoutRules(Definitions) defaultLayoutRules].cold.1
+ +[SXComponentLayoutRules(Definitions) fullWidthLayoutRules].cold.1
+ +[SXComponentLayoutRules(Definitions) twoColumnLayoutRules].cold.1
+ +[SXComponentTextRules(Definitions) bodyTextRules].cold.1
+ +[SXComponentTextRules(Definitions) defaultTextRules].cold.1
+ +[SXComponentTextRules(Definitions) headingTextRules].cold.1
+ +[SXComponentTextRules(Definitions) smallTextRules].cold.1
+ +[SXComponentTextRules(Definitions) titleTextRules].cold.1
+ +[SXDocumentTextContentProvider sharedQueue].cold.1
+ +[SXEmbedVideoComponentView sharedConfiguration].cold.1
+ +[SXExperiment jsonPropertyNameForObjCPropertyName:]
+ +[SXExperimentationStoreItems deserialize:]
+ +[SXExperimentationStoreReset performStoreReset]
+ +[SXImageDecodingTools sharedInstance].cold.1
+ +[SXJSONObject propertyDefinitions].cold.1
+ +[SXJSONObject propertyHashTable].cold.1
+ +[SXJSONObject protocolPropertyDefinitions].cold.1
+ +[SXJSONObjectComponentSupport shared].cold.1
+ +[SXLegacySupport deprecatedComponents].cold.1
+ +[SXMapSnapShotter serialQueue].cold.1
+ +[UIDevice(SXAdditions) sx_isSpectreDevice].cold.1
+ -[NSDate(SXAdditions) isExpired]
+ -[NSDate(SXJSONObject) initWithJSONObject:andVersion:]
+ -[NSDate(SXJSONObject) initWithJSONObject:andVersion:].cold.1
+ -[SXArticleSearchManager .cxx_destruct]
+ -[SXArticleSearchManager activateHighlightAtIndex:icc:isActive:keyboardHeight:]
+ -[SXArticleSearchManager activeIndex]
+ -[SXArticleSearchManager clearSearchHighlights:]
+ -[SXArticleSearchManager highlightController]
+ -[SXArticleSearchManager highlights]
+ -[SXArticleSearchManager init]
+ -[SXArticleSearchManager isFirstOccurrence]
+ -[SXArticleSearchManager moveHighlightWithContext:icc:]
+ -[SXArticleSearchManager reloadWithItems:icc:]
+ -[SXArticleSearchManager searchItems:withContext:icc:]
+ -[SXArticleSearchManager searchTextStorage:forContext:withOptions:icc:currentCount:]
+ -[SXArticleSearchManager setActiveIndex:]
+ -[SXArticleSearchManager setHighlightController:]
+ -[SXArticleSearchManager setHighlights:]
+ -[SXArticleSearchManager setIsFirstOccurrence:]
+ -[SXArticleSearchManager tskSearchOptions:]
+ -[SXComponent accessibilityLabel]
+ -[SXConditionHints experimentVariantWithValue:withType:]
+ -[SXConditionValidationContext experiment]
+ -[SXConditionValidationContext initWithLayoutOptions:experiment:]
+ -[SXConditionValidationContextFactory createContextWithLayoutOptions:experiment:]
+ -[SXDOMModificationContext experiment]
+ -[SXDOMModificationContext initWithLayoutOptions:specVersion:experiment:]
+ -[SXExperimentConditionValidator .cxx_destruct]
+ -[SXExperimentConditionValidator experimentationManager]
+ -[SXExperimentConditionValidator initWithExperimentationManager:]
+ -[SXExperimentConditionValidator validateCondition:context:]
+ -[SXExperimentationManager .cxx_destruct]
+ -[SXExperimentationManager getTreatmentGroupForExperiment:]
+ -[SXExperimentationManager getTreatmentGroupForExperiment:].cold.1
+ -[SXExperimentationManager getTreatmentGroupForExperiment:].cold.2
+ -[SXExperimentationManager initWithStore:]
+ -[SXExperimentationManager setupExperimentationForDocument:experimentationDelegate:]
+ -[SXExperimentationManager setupExperimentationForDocument:experimentationDelegate:].cold.1
+ -[SXExperimentationManager store]
+ -[SXExperimentationStore .cxx_destruct]
+ -[SXExperimentationStore filterExpiredExperiments:]
+ -[SXExperimentationStore findStoreItemForExperimentIdentifier:]
+ -[SXExperimentationStore loadStore]
+ -[SXExperimentationStore readStore]
+ -[SXExperimentationStore setStore:]
+ -[SXExperimentationStore storeTreatmentGroup:forExperimentIdentifier:expiryDate:]
+ -[SXExperimentationStore storeTreatmentGroup:forExperimentIdentifier:expiryDate:].cold.1
+ -[SXExperimentationStore store]
+ -[SXExperimentationStore treatmentGroupForExperimentIdentifier:]
+ -[SXExperimentationStore writeStore:]
+ -[SXExperimentationStore writeStore:].cold.1
+ -[SXExperimentationStoreItem .cxx_destruct]
+ -[SXExperimentationStoreItem experimentIdentifier]
+ -[SXExperimentationStoreItem expiryDate]
+ -[SXExperimentationStoreItem isEqual:]
+ -[SXExperimentationStoreItem setExperimentIdentifier:]
+ -[SXExperimentationStoreItem setExpiryDate:]
+ -[SXExperimentationStoreItem setStartDate:]
+ -[SXExperimentationStoreItem setTreatmentGroup:]
+ -[SXExperimentationStoreItem startDate]
+ -[SXExperimentationStoreItem treatmentGroup]
+ -[SXExperimentationStoreItems .cxx_destruct]
+ -[SXExperimentationStoreItems init]
+ -[SXExperimentationStoreItems isEqual:]
+ -[SXExperimentationStoreItems items]
+ -[SXExperimentationStoreItems serialize]
+ -[SXExperimentationStoreItems setItems:]
+ -[SXHighlightController .cxx_destruct]
+ -[SXHighlightController activeLayers]
+ -[SXHighlightController applyHighlightForStorage:withRect:inRange:icc:isActive:keyboardHeight:isReload:]
+ -[SXHighlightController clearHighlights]
+ -[SXHighlightController highlightLayers]
+ -[SXHighlightController init]
+ -[SXHighlightController removeActiveLayers]
+ -[SXHighlightController setActiveLayers:]
+ -[SXHighlightController setHighlightLayers:]
+ -[SXImageDecodingTools P3ColorSpace].cold.1
+ -[SXImageDecodingTools RGBColorSpace].cold.1
+ -[SXMediaPlaybackController viewport:appearStateChangedFromState:].cold.1
+ -[SXScrollViewController experimentationDelegate]
+ -[SXScrollViewController experimentationManager]
+ -[SXScrollViewController initWithScrollView:documentControllerContainer:resourceDataSourceContainer:analyticsReportingContainer:presentationDelegateContainer:presentationAttributeManager:viewport:tangierController:componentController:interactor:appStateMonitor:viewControllerPresentingManager:scrollPositionManager:documentStyleRenderer:componentInteractionManager:interactionContextManager:hoverStyleManager:scrollReporter:videoPlayerViewControllerManager:mediaSharingPolicyProvider:fontIndex:documentProvider:transitionDataSourceProvider:DOMObjectProvider:experimentationManager:]
+ -[SXScrollViewController isSearchActive]
+ -[SXScrollViewController reloadSearch]
+ -[SXScrollViewController searchWithContext:]
+ -[SXScrollViewController setExperimentationDelegate:]
+ -[SXScrollViewController setIsSearchActive:]
+ -[SXScrollViewController setupArticleExperimentation]
+ -[SXSearchContext action]
+ -[SXSearchContext index]
+ -[SXSearchContext initWithSearchTerm:options:total:index:action:isBeginningFilterActive:keyboardHeight:]
+ -[SXSearchContext isBeginningFilterActive]
+ -[SXSearchContext keyboardHeight]
+ -[SXSearchContext options]
+ -[SXSearchContext searchTerm]
+ -[SXSearchContext setAction:]
+ -[SXSearchContext setIndex:]
+ -[SXSearchContext setIsBeginningFilterActive:]
+ -[SXSearchContext setKeyboardHeight:]
+ -[SXSearchContext setOptions:]
+ -[SXSearchContext setSearchTerm:]
+ -[SXSearchContext setTotal:]
+ -[SXSearchContext total]
+ -[SXSearchHighlight .cxx_destruct]
+ -[SXSearchHighlight index]
+ -[SXSearchHighlight initWithRects:ranges:item:index:]
+ -[SXSearchHighlight item]
+ -[SXSearchHighlight ranges]
+ -[SXSearchHighlight rects]
+ -[SXSearchHighlight setIndex:]
+ -[SXSearchHighlight setItem:]
+ -[SXSearchResults index]
+ -[SXSearchResults initWithTotal:index:]
+ -[SXSearchResults setIndex:]
+ -[SXSearchResults setTotal:]
+ -[SXSearchResults total]
+ -[SXSubscriptionButtonComponent accessibilityLabel]
+ -[SXTangierController reloadSearch]
+ -[SXTangierController searchWithContext:]
+ -[SXTangierTextRenderCollector getAllItemsWithICC:]
+ -[SXTangierTextRenderCollector initWithSearchManager:]
+ -[SXTangierTextRenderCollector reloadWithICC:]
+ -[SXTangierTextRenderCollector searchManager]
+ -[SXTangierTextRenderCollector searchWithContext:icc:]
+ -[SXTangierTextRenderCollector setSearchManager:]
+ OBJC_IVAR_$_SXArticleSearchManager._activeIndex
+ OBJC_IVAR_$_SXArticleSearchManager._highlightController
+ OBJC_IVAR_$_SXArticleSearchManager._highlights
+ OBJC_IVAR_$_SXArticleSearchManager._isFirstOccurrence
+ OBJC_IVAR_$_SXComponent.accessibilityLabel
+ OBJC_IVAR_$_SXConditionValidationContext._experiment
+ OBJC_IVAR_$_SXDOMModificationContext._experiment
+ OBJC_IVAR_$_SXExperimentConditionValidator._experimentationManager
+ OBJC_IVAR_$_SXExperimentationManager._store
+ OBJC_IVAR_$_SXExperimentationStore._store
+ OBJC_IVAR_$_SXExperimentationStoreItem._experimentIdentifier
+ OBJC_IVAR_$_SXExperimentationStoreItem._expiryDate
+ OBJC_IVAR_$_SXExperimentationStoreItem._startDate
+ OBJC_IVAR_$_SXExperimentationStoreItem._treatmentGroup
+ OBJC_IVAR_$_SXExperimentationStoreItems._items
+ OBJC_IVAR_$_SXHighlightController._activeLayers
+ OBJC_IVAR_$_SXHighlightController._highlightLayers
+ OBJC_IVAR_$_SXScrollViewController._experimentationDelegate
+ OBJC_IVAR_$_SXScrollViewController._experimentationManager
+ OBJC_IVAR_$_SXScrollViewController._isSearchActive
+ OBJC_IVAR_$_SXSearchContext._action
+ OBJC_IVAR_$_SXSearchContext._index
+ OBJC_IVAR_$_SXSearchContext._isBeginningFilterActive
+ OBJC_IVAR_$_SXSearchContext._keyboardHeight
+ OBJC_IVAR_$_SXSearchContext._options
+ OBJC_IVAR_$_SXSearchContext._searchTerm
+ OBJC_IVAR_$_SXSearchContext._total
+ OBJC_IVAR_$_SXSearchHighlight._index
+ OBJC_IVAR_$_SXSearchHighlight._item
+ OBJC_IVAR_$_SXSearchHighlight._ranges
+ OBJC_IVAR_$_SXSearchHighlight._rects
+ OBJC_IVAR_$_SXSearchResults._index
+ OBJC_IVAR_$_SXSearchResults._total
+ OBJC_IVAR_$_SXTangierTextRenderCollector._searchManager
+ SXBundle.cold.1
+ SXConditionTypes.cold.1
+ SXSetupLogging.cold.1
+ _NSFontAttributeName
+ _OBJC_$_PROP_LIST_SXArticleLinkComponent.103
+ _OBJC_$_PROP_LIST_SXArticleThumbnailComponent.106
+ _OBJC_$_PROP_LIST_SXButtonComponent.117
+ _OBJC_$_PROP_LIST_SXCondition.186
+ _OBJC_$_PROP_LIST_SXConditionHints.120
+ _OBJC_$_PROP_LIST_SXConditionValidationContext.106
+ _OBJC_$_PROP_LIST_SXDOMModificationContext.68
+ _OBJC_$_PROP_LIST_SXIssueCoverComponent.108
+ _OBJC_$_PROP_LIST_SXQuickLookComponent.116
+ _OBJC_$_PROP_LIST_SXWebContentComponent.123
+ _OBJC_CLASS_$_CATextLayer
+ _OBJC_CLASS_$_SXArticleSearchManager
+ _OBJC_CLASS_$_SXExperiment
+ _OBJC_CLASS_$_SXExperimentConditionValidator
+ _OBJC_CLASS_$_SXExperimentationManager
+ _OBJC_CLASS_$_SXExperimentationStore
+ _OBJC_CLASS_$_SXExperimentationStoreItem
+ _OBJC_CLASS_$_SXExperimentationStoreItems
+ _OBJC_CLASS_$_SXExperimentationStoreReset
+ _OBJC_CLASS_$_SXHighlightController
+ _OBJC_CLASS_$_SXSearchContext
+ _OBJC_CLASS_$_SXSearchHighlight
+ _OBJC_CLASS_$_SXSearchResults
+ _OBJC_METACLASS_$_SXArticleSearchManager
+ _OBJC_METACLASS_$_SXExperiment
+ _OBJC_METACLASS_$_SXExperimentConditionValidator
+ _OBJC_METACLASS_$_SXExperimentationManager
+ _OBJC_METACLASS_$_SXExperimentationStore
+ _OBJC_METACLASS_$_SXExperimentationStoreItem
+ _OBJC_METACLASS_$_SXExperimentationStoreItems
+ _OBJC_METACLASS_$_SXExperimentationStoreReset
+ _OBJC_METACLASS_$_SXHighlightController
+ _OBJC_METACLASS_$_SXSearchContext
+ _OBJC_METACLASS_$_SXSearchHighlight
+ _OBJC_METACLASS_$_SXSearchResults
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_2
+ _OUTLINED_FUNCTION_3
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ _SXConditionExperimentVariant
+ _SXExperimentationLog
+ _SXExperimentationStoreItemExperimentIdentifierKey
+ _SXExperimentationStoreItemExpiryDateKey
+ _SXExperimentationStoreItemStartDateKey
+ _SXExperimentationStoreItemTreatmentGroupKey
+ _SXExperimentationStoreItemsKey
+ _SXExperimentationStoreKey
+ __MergedGlobals
+ __OBJC_$_CATEGORY_NSDate_$_SXJSONObject
+ __OBJC_$_CLASS_METHODS_SXExperiment
+ __OBJC_$_CLASS_METHODS_SXExperimentationStoreItems
+ __OBJC_$_CLASS_METHODS_SXExperimentationStoreReset
+ __OBJC_$_INSTANCE_METHODS_NSDate(SXJSONObject|SXAdditions)
+ __OBJC_$_INSTANCE_METHODS_SXArticleSearchManager
+ __OBJC_$_INSTANCE_METHODS_SXExperimentConditionValidator
+ __OBJC_$_INSTANCE_METHODS_SXExperimentationManager
+ __OBJC_$_INSTANCE_METHODS_SXExperimentationStore
+ __OBJC_$_INSTANCE_METHODS_SXExperimentationStoreItem
+ __OBJC_$_INSTANCE_METHODS_SXExperimentationStoreItems
+ __OBJC_$_INSTANCE_METHODS_SXHighlightController
+ __OBJC_$_INSTANCE_METHODS_SXSearchContext
+ __OBJC_$_INSTANCE_METHODS_SXSearchHighlight
+ __OBJC_$_INSTANCE_METHODS_SXSearchResults
+ __OBJC_$_INSTANCE_METHODS_SXSubscriptionButtonComponent
+ __OBJC_$_INSTANCE_VARIABLES_SXArticleSearchManager
+ __OBJC_$_INSTANCE_VARIABLES_SXExperimentConditionValidator
+ __OBJC_$_INSTANCE_VARIABLES_SXExperimentationManager
+ __OBJC_$_INSTANCE_VARIABLES_SXExperimentationStore
+ __OBJC_$_INSTANCE_VARIABLES_SXExperimentationStoreItem
+ __OBJC_$_INSTANCE_VARIABLES_SXExperimentationStoreItems
+ __OBJC_$_INSTANCE_VARIABLES_SXHighlightController
+ __OBJC_$_INSTANCE_VARIABLES_SXSearchContext
+ __OBJC_$_INSTANCE_VARIABLES_SXSearchHighlight
+ __OBJC_$_INSTANCE_VARIABLES_SXSearchResults
+ __OBJC_$_PROP_LIST_SXArticleSearchManager
+ __OBJC_$_PROP_LIST_SXExperiment
+ __OBJC_$_PROP_LIST_SXExperimentConditionValidator
+ __OBJC_$_PROP_LIST_SXExperimentationManager
+ __OBJC_$_PROP_LIST_SXExperimentationStore
+ __OBJC_$_PROP_LIST_SXExperimentationStoreItem
+ __OBJC_$_PROP_LIST_SXExperimentationStoreItems
+ __OBJC_$_PROP_LIST_SXHighlightController
+ __OBJC_$_PROP_LIST_SXSearchContext
+ __OBJC_$_PROP_LIST_SXSearchHighlight
+ __OBJC_$_PROP_LIST_SXSearchResults
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_TSKSearchable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SXExperimentationManager
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_SXExperimentationStore
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SXExperimentationManager
+ __OBJC_$_PROTOCOL_METHOD_TYPES_SXExperimentationStore
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TSKSearchable
+ __OBJC_$_PROTOCOL_REFS_SXExperimentationManager
+ __OBJC_$_PROTOCOL_REFS_SXExperimentationStore
+ __OBJC_$_PROTOCOL_REFS_TSKSearchable
+ __OBJC_CLASS_PROTOCOLS_$_SXExperimentConditionValidator
+ __OBJC_CLASS_PROTOCOLS_$_SXExperimentationManager
+ __OBJC_CLASS_PROTOCOLS_$_SXExperimentationStore
+ __OBJC_CLASS_RO_$_SXArticleSearchManager
+ __OBJC_CLASS_RO_$_SXExperiment
+ __OBJC_CLASS_RO_$_SXExperimentConditionValidator
+ __OBJC_CLASS_RO_$_SXExperimentationManager
+ __OBJC_CLASS_RO_$_SXExperimentationStore
+ __OBJC_CLASS_RO_$_SXExperimentationStoreItem
+ __OBJC_CLASS_RO_$_SXExperimentationStoreItems
+ __OBJC_CLASS_RO_$_SXExperimentationStoreReset
+ __OBJC_CLASS_RO_$_SXHighlightController
+ __OBJC_CLASS_RO_$_SXSearchContext
+ __OBJC_CLASS_RO_$_SXSearchHighlight
+ __OBJC_CLASS_RO_$_SXSearchResults
+ __OBJC_LABEL_PROTOCOL_$_SXExperimentationManager
+ __OBJC_LABEL_PROTOCOL_$_SXExperimentationStore
+ __OBJC_LABEL_PROTOCOL_$_TSKSearchable
+ __OBJC_METACLASS_RO_$_SXArticleSearchManager
+ __OBJC_METACLASS_RO_$_SXExperiment
+ __OBJC_METACLASS_RO_$_SXExperimentConditionValidator
+ __OBJC_METACLASS_RO_$_SXExperimentationManager
+ __OBJC_METACLASS_RO_$_SXExperimentationStore
+ __OBJC_METACLASS_RO_$_SXExperimentationStoreItem
+ __OBJC_METACLASS_RO_$_SXExperimentationStoreItems
+ __OBJC_METACLASS_RO_$_SXExperimentationStoreReset
+ __OBJC_METACLASS_RO_$_SXHighlightController
+ __OBJC_METACLASS_RO_$_SXSearchContext
+ __OBJC_METACLASS_RO_$_SXSearchHighlight
+ __OBJC_METACLASS_RO_$_SXSearchResults
+ __OBJC_PROTOCOL_$_SXExperimentationManager
+ __OBJC_PROTOCOL_$_SXExperimentationStore
+ __OBJC_PROTOCOL_$_TSKSearchable
+ __OBJC_PROTOCOL_REFERENCE_$_SXExperimentationManager
+ __OBJC_PROTOCOL_REFERENCE_$_SXExperimentationStore
+ __OBJC_PROTOCOL_REFERENCE_$_TSKSearchable
+ ___32-[SXDOMAssembly loadInRegistry:]_block_invoke_77
+ ___33-[SXCoreAssembly loadInRegistry:]_block_invoke_28
+ ___33-[SXCoreAssembly loadInRegistry:]_block_invoke_29
+ ___51-[SXTangierTextRenderCollector getAllItemsWithICC:]_block_invoke
+ ___54-[NSDate(SXJSONObject) initWithJSONObject:andVersion:]_block_invoke
+ ___84-[SXArticleSearchManager searchTextStorage:forContext:withOptions:icc:currentCount:]_block_invoke
+ ___block_descriptor_136_e8_32s40s48s56s64s72s80s88s96r104r112r_e30_v16?0"<TSKSearchReference>"8ls32l8s40l8r96l8s48l8r104l8s56l8s64l8s72l8s80l8s88l8r112l8
+ ___block_descriptor_32_e48_"<SXExperimentationStore>"16?0"<TFResolver>"8l
+ ___block_descriptor_32_e50_"<SXExperimentationManager>"16?0"<TFResolver>"8l
+ ___block_descriptor_40_e8_32s_e79_q24?0"SXTangierTextRenderCollectorItem"8"SXTangierTextRenderCollectorItem"16ls32l8
+ __block_literal_global.239
+ __block_literal_global.253
+ __block_literal_global.268
+ __block_literal_global.287
+ __block_literal_global.291
+ __block_literal_global.301
+ __block_literal_global.305
+ __block_literal_global.308
+ __block_literal_global.312
+ __block_literal_global.315
+ __block_literal_global.319
+ __block_literal_global.322
+ __block_literal_global.326
+ __block_literal_global.329
+ __block_literal_global.343
+ __block_literal_global.347
+ __block_literal_global.355
+ __block_literal_global.358
+ __block_literal_global.361
+ __block_literal_global.419
+ __block_literal_global.422
+ __block_literal_global.425
+ __block_literal_global.428
+ __block_literal_global.432
+ __block_literal_global.435
+ __block_literal_global.438
+ __block_literal_global.441
+ __block_literal_global.444
+ __block_literal_global.447
+ __block_literal_global.450
+ __block_literal_global.453
+ __block_literal_global.456
+ __block_literal_global.459
+ __block_literal_global.462
+ __block_literal_global.465
+ __block_literal_global.468
+ __block_literal_global.470
+ __block_literal_global.472
+ __block_literal_global.474
+ __block_literal_global.482
+ __block_literal_global.488
+ __block_literal_global.493
+ __block_literal_global.496
+ __block_literal_global.498
+ __block_literal_global.501
+ __block_literal_global.503
+ _objc_msgSend$activateHighlightAtIndex:icc:isActive:keyboardHeight:
+ _objc_msgSend$activeIndex
+ _objc_msgSend$activeLayers
+ _objc_msgSend$applyHighlightForStorage:withRect:inRange:icc:isActive:keyboardHeight:isReload:
+ _objc_msgSend$clearHighlights
+ _objc_msgSend$clearSearchHighlights:
+ _objc_msgSend$continueSearch:
+ _objc_msgSend$createContextWithLayoutOptions:experiment:
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$deserialize:
+ _objc_msgSend$didStartExperimentForDocument:experimentIdentifier:treatmentGroup:
+ _objc_msgSend$experiment
+ _objc_msgSend$experimentIdentifier
+ _objc_msgSend$experimentTreatmentGroup
+ _objc_msgSend$experimentationDelegate
+ _objc_msgSend$experimentationManager
+ _objc_msgSend$expiryDate
+ _objc_msgSend$filterExpiredExperiments:
+ _objc_msgSend$findStoreItemForExperimentIdentifier:
+ _objc_msgSend$fontDescriptorWithName:size:
+ _objc_msgSend$fontDescriptorWithSymbolicTraits:
+ _objc_msgSend$fontWithDescriptor:size:
+ _objc_msgSend$getAllItemsWithICC:
+ _objc_msgSend$getTreatmentGroupForExperiment:
+ _objc_msgSend$highlightController
+ _objc_msgSend$highlightLayers
+ _objc_msgSend$highlights
+ _objc_msgSend$index
+ _objc_msgSend$initWithExperimentationManager:
+ _objc_msgSend$initWithLayoutOptions:experiment:
+ _objc_msgSend$initWithLayoutOptions:specVersion:experiment:
+ _objc_msgSend$initWithRects:ranges:item:index:
+ _objc_msgSend$initWithScrollView:documentControllerContainer:resourceDataSourceContainer:analyticsReportingContainer:presentationDelegateContainer:presentationAttributeManager:viewport:tangierController:componentController:interactor:appStateMonitor:viewControllerPresentingManager:scrollPositionManager:documentStyleRenderer:componentInteractionManager:interactionContextManager:hoverStyleManager:scrollReporter:videoPlayerViewControllerManager:mediaSharingPolicyProvider:fontIndex:documentProvider:transitionDataSourceProvider:DOMObjectProvider:experimentationManager:
+ _objc_msgSend$initWithSearchManager:
+ _objc_msgSend$initWithStore:
+ _objc_msgSend$initWithTotal:index:
+ _objc_msgSend$isBeginningFilterActive
+ _objc_msgSend$isEqualToDate:
+ _objc_msgSend$isExperimentationEnabled
+ _objc_msgSend$isExpired
+ _objc_msgSend$isSearchActive
+ _objc_msgSend$item
+ _objc_msgSend$keyboardHeight
+ _objc_msgSend$lightGrayColor
+ _objc_msgSend$loadStore
+ _objc_msgSend$moveHighlightWithContext:icc:
+ _objc_msgSend$rangeOfString:searchOptions:updatingSearchRange:
+ _objc_msgSend$ranges
+ _objc_msgSend$readStore
+ _objc_msgSend$rects
+ _objc_msgSend$reloadSearch
+ _objc_msgSend$reloadWithICC:
+ _objc_msgSend$reloadWithItems:icc:
+ _objc_msgSend$removeActiveLayers
+ _objc_msgSend$searchForString:options:onHit:
+ _objc_msgSend$searchItems:withContext:icc:
+ _objc_msgSend$searchManager
+ _objc_msgSend$searchTerm
+ _objc_msgSend$searchTextStorage:forContext:withOptions:icc:currentCount:
+ _objc_msgSend$searchWithContext:
+ _objc_msgSend$searchWithContext:icc:
+ _objc_msgSend$serialize
+ _objc_msgSend$setActiveIndex:
+ _objc_msgSend$setContentsScale:
+ _objc_msgSend$setExperimentIdentifier:
+ _objc_msgSend$setExpiryDate:
+ _objc_msgSend$setFontSize:
+ _objc_msgSend$setForegroundColor:
+ _objc_msgSend$setHighlights:
+ _objc_msgSend$setIsFirstOccurrence:
+ _objc_msgSend$setIsSearchActive:
+ _objc_msgSend$setShowGrayOverlay:
+ _objc_msgSend$setTreatmentGroup:
+ _objc_msgSend$setupArticleExperimentation
+ _objc_msgSend$setupExperimentationForDocument:experimentationDelegate:
+ _objc_msgSend$sizeOfScrollViewEnclosingCanvas
+ _objc_msgSend$sizeWithAttributes:
+ _objc_msgSend$stopScrollingAndZooming
+ _objc_msgSend$store
+ _objc_msgSend$storeTreatmentGroup:forExperimentIdentifier:expiryDate:
+ _objc_msgSend$synchronize
+ _objc_msgSend$systemYellowColor
+ _objc_msgSend$total
+ _objc_msgSend$treatmentGroup
+ _objc_msgSend$treatmentGroupForExperimentIdentifier:
+ _objc_msgSend$treatmentGroups
+ _objc_msgSend$tskSearchOptions:
+ _objc_msgSend$whitespaceCharacterSet
+ _objc_msgSend$wordMetricsAtCharIndex:
+ _objc_msgSend$writeStore:
+ _objc_release_x2
+ initWithJSONObject:andVersion:.dateFormatter
+ initWithJSONObject:andVersion:.onceToken
- -[SXConditionValidationContext initWithLayoutOptions:]
- -[SXConditionValidationContextFactory createContextWithLayoutOptions:]
- -[SXDOMModificationContext initWithLayoutOptions:specVersion:]
- -[SXScrollViewController initWithScrollView:documentControllerContainer:resourceDataSourceContainer:analyticsReportingContainer:presentationDelegateContainer:presentationAttributeManager:viewport:tangierController:componentController:interactor:appStateMonitor:viewControllerPresentingManager:scrollPositionManager:documentStyleRenderer:componentInteractionManager:interactionContextManager:hoverStyleManager:scrollReporter:videoPlayerViewControllerManager:mediaSharingPolicyProvider:fontIndex:documentProvider:transitionDataSourceProvider:DOMObjectProvider:]
- -[SXTangierTextRenderCollector init]
- _OBJC_$_PROP_LIST_SXArticleLinkComponent.101
- _OBJC_$_PROP_LIST_SXArticleThumbnailComponent.104
- _OBJC_$_PROP_LIST_SXButtonComponent.115
- _OBJC_$_PROP_LIST_SXCondition.178
- _OBJC_$_PROP_LIST_SXConditionHints.117
- _OBJC_$_PROP_LIST_SXConditionValidationContext.99
- _OBJC_$_PROP_LIST_SXDOMModificationContext.61
- _OBJC_$_PROP_LIST_SXIssueCoverComponent.106
- _OBJC_$_PROP_LIST_SXQuickLookComponent.114
- _OBJC_$_PROP_LIST_SXWebContentComponent.121
- __block_literal_global.234
- __block_literal_global.272
- __block_literal_global.276
- __block_literal_global.282
- __block_literal_global.293
- __block_literal_global.296
- __block_literal_global.300
- __block_literal_global.303
- __block_literal_global.307
- __block_literal_global.310
- __block_literal_global.317
- __block_literal_global.324
- __block_literal_global.328
- __block_literal_global.339
- __block_literal_global.342
- __block_literal_global.346
- __block_literal_global.418
- __block_literal_global.421
- __block_literal_global.424
- __block_literal_global.427
- __block_literal_global.431
- __block_literal_global.434
- __block_literal_global.437
- __block_literal_global.440
- __block_literal_global.443
- __block_literal_global.446
- __block_literal_global.449
- __block_literal_global.452
- __block_literal_global.455
- __block_literal_global.458
- __block_literal_global.461
- __block_literal_global.464
- __block_literal_global.467
- __block_literal_global.469
- __block_literal_global.471
- __block_literal_global.473
- __block_literal_global.478
- __block_literal_global.489
- __block_literal_global.492
- __block_literal_global.494
- __block_literal_global.497
- __block_literal_global.499
- _objc_msgSend$createContextWithLayoutOptions:
- _objc_msgSend$initWithLayoutOptions:
- _objc_msgSend$initWithLayoutOptions:specVersion:
- _objc_msgSend$initWithScrollView:documentControllerContainer:resourceDataSourceContainer:analyticsReportingContainer:presentationDelegateContainer:presentationAttributeManager:viewport:tangierController:componentController:interactor:appStateMonitor:viewControllerPresentingManager:scrollPositionManager:documentStyleRenderer:componentInteractionManager:interactionContextManager:hoverStyleManager:scrollReporter:videoPlayerViewControllerManager:mediaSharingPolicyProvider:fontIndex:documentProvider:transitionDataSourceProvider:DOMObjectProvider:
- preferredFontSizeForUsage:contentSizeCategoryName:fontSize:.__textStyleBodyLeadingCache
- preferredFontSizeForUsage:contentSizeCategoryName:fontSize:.onceToken
CStrings:
+ "-[SXExperimentationStore readStore]"
+ "-[SXExperimentationStore storeTreatmentGroup:forExperimentIdentifier:expiryDate:]"
+ "-[SXExperimentationStore treatmentGroupForExperimentIdentifier:]"
+ "-[SXExperimentationStore writeStore:]"
+ "/AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/Modules/silex/Silex/Experimentation/SXExperimentationStore.m"
+ "/AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/Modules/silex/Silex/JSONObject/UIColor+SXJSONObject.m"
+ "/AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/Modules/silex/Silex/Text/SXTextSource.m"
+ "/AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/Modules/silex/Silex/Text/Tangier/SXContainerLayout.m"
+ "/AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/Modules/silex/Silex/Text/Tangier/SXStandaloneTextLayout.m"
+ "/AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/Modules/silex/Silex/Text/Tangier/SXTangierCanvasUtilities.mm"
+ "/AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/Modules/silex/Silex/Text/Tangier/SXTextTangierFlowLayout.m"
+ "/AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/Modules/silex/Silex/Text/Tangier/SXTextTangierLayout.mm"
+ "/AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/Modules/silex/Silex/Text/Tangier/SXTextTangierStorage.m"
+ "/AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/Modules/silex/Silex/Text/Tangier/SXTextTangierTextWrapper.mm"
+ "/AppleInternal/Library/BuildRoots/28f4b4c9-00e0-11f0-8e4b-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/Modules/silex/Silex/Text/Tangier/TSWPRep+SXAccessibility.m"
+ "1.29"
+ "@\"<SXConditionValidationContext>\"32@0:8@\"SXLayoutOptions\"16@\"SXExperiment\"24"
+ "@\"<SXExperimentationDelegate>\""
+ "@\"<SXExperimentationManager>\""
+ "@\"<SXExperimentationManager>\"16@?0@\"<TFResolver>\"8"
+ "@\"<SXExperimentationStore>\""
+ "@\"<SXExperimentationStore>\"16@?0@\"<TFResolver>\"8"
+ "@\"NSString\"24@0:8@\"SXExperiment\"16"
+ "@\"SXArticleSearchManager\""
+ "@\"SXExperiment\""
+ "@\"SXExperiment\"16@0:8"
+ "@\"SXExperimentationManager\""
+ "@\"SXExperimentationStoreItems\""
+ "@\"SXHighlightController\""
+ "@\"SXTangierTextRenderCollectorItem\""
+ "@\"TSKReplaceAllChildCommand\"24@0:8@\"TSKReplaceAllCommand\"16"
+ "@\"TSKSearch\"24@0:8@?<v@?@\"<TSKSearchReference>\">16"
+ "@\"TSKSearch\"40@0:8@\"NSString\"16Q24@?<v@?@\"<TSKSearchReference>\">32"
+ "@216@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200@208"
+ "@48@0:8@16@24@32Q40"
+ "@68@0:8@16Q24Q32Q40Q48B56Q60"
+ "ANFExperimentation"
+ "Experiment found without valid expiration date. experimentIdentifier=%@"
+ "Found treatmentGroup in store. experimentIdentifier=%@, treatmentGroup=%@"
+ "Loaded empty experimentation store"
+ "Loaded experimentation store, entryCount = %ld"
+ "Loading experimentation store"
+ "NSFontNameAttribute"
+ "No treatmentGroups for experiment. experimentIdentifier=%@"
+ "Not starting experiment, it has expired. experimentIdentifier=%@, expirationDate=%@"
+ "Not writing store, no data"
+ "Overriding treatmentGroup of previously stored experiment. experimentIdentifier=%@, treatmentGroup=%@, previousTreatmentGroup=%@"
+ "Q56@0:8@16@24Q32@40Q48"
+ "Reset experimentation store"
+ "SXArticleSearchManager"
+ "SXExperiment"
+ "SXExperimentConditionValidator"
+ "SXExperimentationManager"
+ "SXExperimentationStore"
+ "SXExperimentationStoreItem"
+ "SXExperimentationStoreItems"
+ "SXExperimentationStoreReset"
+ "SXHighlightController"
+ "SXSearchContext"
+ "SXSearchHighlight"
+ "SXSearchResults"
+ "Selected experiment treatmentGroup. experimentIdentifier=%@, treatmentGroup=%@"
+ "Starting experiment. experimentIdentifier=%@, treatmentGroup=%@"
+ "Storing treatmentGroup. experimentIdentifier=%@, treatmentGroup=%@"
+ "T@\"<SXExperimentationDelegate>\",W,N,V_experimentationDelegate"
+ "T@\"<SXExperimentationManager>\",R,N,V_experimentationManager"
+ "T@\"<SXExperimentationStore>\",R,N,V_store"
+ "T@\"NSArray\",&,N,V_items"
+ "T@\"NSArray\",R,N,V_ranges"
+ "T@\"NSArray\",R,N,V_rects"
+ "T@\"NSDate\",&,N,V_expiryDate"
+ "T@\"NSDate\",&,N,V_startDate"
+ "T@\"NSMutableArray\",&,N,V_activeLayers"
+ "T@\"NSMutableArray\",&,N,V_highlightLayers"
+ "T@\"NSMutableArray\",&,N,V_highlights"
+ "T@\"NSString\",&,N,V_experimentIdentifier"
+ "T@\"NSString\",&,N,V_treatmentGroup"
+ "T@\"NSString\",N,V_searchTerm"
+ "T@\"NSString\",R,N,VaccessibilityLabel"
+ "T@\"SXArticleSearchManager\",&,N,V_searchManager"
+ "T@\"SXExperiment\",R,D,N"
+ "T@\"SXExperiment\",R,N"
+ "T@\"SXExperiment\",R,N,V_experiment"
+ "T@\"SXExperimentationManager\",R,N,V_experimentationManager"
+ "T@\"SXExperimentationStoreItems\",&,N,V_store"
+ "T@\"SXHighlightController\",&,N,V_highlightController"
+ "T@\"SXTangierTextRenderCollectorItem\",&,N,V_item"
+ "TB,N,V_isBeginningFilterActive"
+ "TB,N,V_isFirstOccurrence"
+ "TB,N,V_isSearchActive"
+ "TQ,N,V_action"
+ "TQ,N,V_index"
+ "TQ,N,V_keyboardHeight"
+ "TQ,N,V_options"
+ "TQ,N,V_total"
+ "TSKSearchable"
+ "This operation must only be performed on the main thread."
+ "Tq,N,V_activeIndex"
+ "_activeIndex"
+ "_activeLayers"
+ "_experiment"
+ "_experimentIdentifier"
+ "_experimentationDelegate"
+ "_experimentationManager"
+ "_expiryDate"
+ "_highlightController"
+ "_highlightLayers"
+ "_highlights"
+ "_isBeginningFilterActive"
+ "_isFirstOccurrence"
+ "_isSearchActive"
+ "_item"
+ "_keyboardHeight"
+ "_ranges"
+ "_rects"
+ "_searchManager"
+ "_searchTerm"
+ "_store"
+ "_total"
+ "_treatmentGroup"
+ "_webView:backForwardListItemAdded:removed:"
+ "_webView:shouldGoToBackForwardListItem:inPageCache:completionHandler:"
+ "activateHighlightAtIndex:icc:isActive:keyboardHeight:"
+ "activeIndex"
+ "activeLayers"
+ "applyHighlightForStorage:withRect:inRange:icc:isActive:keyboardHeight:isReload:"
+ "childCommandForReplaceAllCommand:"
+ "clearHighlights"
+ "clearSearchHighlights:"
+ "continueAnnotationSearch:"
+ "continueSearch:"
+ "createContextWithLayoutOptions:experiment:"
+ "dateWithTimeIntervalSince1970:"
+ "deserialize:"
+ "didStartExperimentForDocument:experimentIdentifier:treatmentGroup:"
+ "experiment"
+ "experimentIdentifier"
+ "experimentTreatmentGroup"
+ "experimentVariant"
+ "experimentVariantWithValue:withType:"
+ "experimentationDelegate"
+ "experimentationManager"
+ "expiresAt"
+ "expiryDate"
+ "filterExpiredExperiments:"
+ "findStoreItemForExperimentIdentifier:"
+ "fontDescriptorWithName:size:"
+ "fontDescriptorWithSymbolicTraits:"
+ "fontWithDescriptor:size:"
+ "getAllItemsWithICC:"
+ "getTreatmentGroupForExperiment:"
+ "highlightController"
+ "highlightLayers"
+ "highlights"
+ "id"
+ "index"
+ "initWithExperimentationManager:"
+ "initWithLayoutOptions:experiment:"
+ "initWithLayoutOptions:specVersion:experiment:"
+ "initWithRects:ranges:item:index:"
+ "initWithScrollView:documentControllerContainer:resourceDataSourceContainer:analyticsReportingContainer:presentationDelegateContainer:presentationAttributeManager:viewport:tangierController:componentController:interactor:appStateMonitor:viewControllerPresentingManager:scrollPositionManager:documentStyleRenderer:componentInteractionManager:interactionContextManager:hoverStyleManager:scrollReporter:videoPlayerViewControllerManager:mediaSharingPolicyProvider:fontIndex:documentProvider:transitionDataSourceProvider:DOMObjectProvider:experimentationManager:"
+ "initWithSearchManager:"
+ "initWithSearchTerm:options:total:index:action:isBeginningFilterActive:keyboardHeight:"
+ "initWithStore:"
+ "initWithTotal:index:"
+ "isBeginningFilterActive"
+ "isEqualToDate:"
+ "isExperimentationEnabled"
+ "isExpired"
+ "isFirstOccurrence"
+ "isSearchActive"
+ "item"
+ "keyboardHeight"
+ "lightGrayColor"
+ "loadStore"
+ "moveHighlightWithContext:icc:"
+ "performStoreReset"
+ "q24@?0@\"SXTangierTextRenderCollectorItem\"8@\"SXTangierTextRenderCollectorItem\"16"
+ "rangeOfString:searchOptions:updatingSearchRange:"
+ "ranges"
+ "readStore"
+ "rects"
+ "reloadSearch"
+ "reloadWithICC:"
+ "reloadWithItems:icc:"
+ "removeActiveLayers"
+ "searchForAnnotationsWithHitBlock:"
+ "searchForString:options:onHit:"
+ "searchItems:withContext:icc:"
+ "searchManager"
+ "searchTerm"
+ "searchTextStorage:forContext:withOptions:icc:currentCount:"
+ "searchWithContext:"
+ "searchWithContext:icc:"
+ "serialize"
+ "setAction:"
+ "setActiveIndex:"
+ "setActiveLayers:"
+ "setContentsScale:"
+ "setExperimentIdentifier:"
+ "setExperimentationDelegate:"
+ "setExpiryDate:"
+ "setFontSize:"
+ "setForegroundColor:"
+ "setHighlightController:"
+ "setHighlightLayers:"
+ "setHighlights:"
+ "setIndex:"
+ "setIsBeginningFilterActive:"
+ "setIsFirstOccurrence:"
+ "setIsSearchActive:"
+ "setItem:"
+ "setKeyboardHeight:"
+ "setOptions:"
+ "setSearchManager:"
+ "setSearchTerm:"
+ "setShowGrayOverlay:"
+ "setStore:"
+ "setTotal:"
+ "setTreatmentGroup:"
+ "setupArticleExperimentation"
+ "setupExperimentationForDocument:experimentationDelegate:"
+ "sizeWithAttributes:"
+ "stopScrollingAndZooming"
+ "store"
+ "storeTreatmentGroup:forExperimentIdentifier:expiryDate:"
+ "synchronize"
+ "systemYellowColor"
+ "total"
+ "treatmentGroup"
+ "treatmentGroupByExperiment"
+ "treatmentGroupForExperimentIdentifier:"
+ "treatmentGroups"
+ "tskSearchOptions:"
+ "v16@?0@\"<TSKSearchReference>\"8"
+ "v24@0:8@\"TSKSearch\"16"
+ "v32@0:8@\"SXDocument\"16@\"<SXExperimentationDelegate>\"24"
+ "v40@0:8@\"NSString\"16@\"NSString\"24@\"NSDate\"32"
+ "v40@0:8@\"WKWebView\"16@\"WKBackForwardListItem\"24@\"NSArray\"32"
+ "v44@0:8@\"WKWebView\"16@\"WKBackForwardListItem\"24B32@?<v@?B>36"
+ "v44@0:8@16@24B32@?36"
+ "v44@0:8Q16@24B32Q36"
+ "v48@0:8@\"WKWebView\"16@\"WKOpenPanelParameters\"24@\"WKFrameInfo\"32@?<v@?@\"NSArray\">40"
+ "v96@0:8@16{CGRect={CGPoint=dd}{CGSize=dd}}24{_NSRange=QQ}56@72B80Q84B92"
+ "variants"
+ "webView:runOpenPanelWithParameters:initiatedByFrame:completionHandler:"
+ "webView:shouldGoToBackForwardListItem:willUseInstantBack:completionHandler:"
+ "whitespaceCharacterSet"
+ "wordMetricsAtCharIndex:"
+ "writeStore:"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/Modules/silex/Silex/JSONObject/UIColor+SXJSONObject.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/Modules/silex/Silex/Text/SXTextSource.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/Modules/silex/Silex/Text/Tangier/SXContainerLayout.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/Modules/silex/Silex/Text/Tangier/SXStandaloneTextLayout.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/Modules/silex/Silex/Text/Tangier/SXTangierCanvasUtilities.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/Modules/silex/Silex/Text/Tangier/SXTextTangierFlowLayout.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/Modules/silex/Silex/Text/Tangier/SXTextTangierLayout.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/Modules/silex/Silex/Text/Tangier/SXTextTangierStorage.m"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/Modules/silex/Silex/Text/Tangier/SXTextTangierTextWrapper.mm"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/FeldsparServicesUI/Modules/silex/Silex/Text/Tangier/TSWPRep+SXAccessibility.m"
- "1.28"
- "@\"<SXConditionValidationContext>\"24@0:8@\"SXLayoutOptions\"16"
- "@208@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160@168@176@184@192@200"
- "createContextWithLayoutOptions:"
- "initWithLayoutOptions:"
- "initWithLayoutOptions:specVersion:"
- "initWithScrollView:documentControllerContainer:resourceDataSourceContainer:analyticsReportingContainer:presentationDelegateContainer:presentationAttributeManager:viewport:tangierController:componentController:interactor:appStateMonitor:viewControllerPresentingManager:scrollPositionManager:documentStyleRenderer:componentInteractionManager:interactionContextManager:hoverStyleManager:scrollReporter:videoPlayerViewControllerManager:mediaSharingPolicyProvider:fontIndex:documentProvider:transitionDataSourceProvider:DOMObjectProvider:"

```
