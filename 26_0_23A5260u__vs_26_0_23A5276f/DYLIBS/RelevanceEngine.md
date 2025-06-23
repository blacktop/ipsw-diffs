## RelevanceEngine

> `/System/Library/PrivateFrameworks/RelevanceEngine.framework/RelevanceEngine`

```diff

-561.0.0.0.0
-  __TEXT.__text: 0x100f08
+565.0.0.0.0
+  __TEXT.__text: 0x1012cc
   __TEXT.__auth_stubs: 0x1cd0
-  __TEXT.__objc_methlist: 0x10374
+  __TEXT.__objc_methlist: 0x10394
   __TEXT.__const: 0x1818
-  __TEXT.__cstring: 0x7b0d
-  __TEXT.__gcc_except_tab: 0x39f0
-  __TEXT.__oslogstring: 0x45bd
+  __TEXT.__cstring: 0x7b2d
+  __TEXT.__gcc_except_tab: 0x3a10
+  __TEXT.__oslogstring: 0x46bd
   __TEXT.__dlopen_cstrs: 0xa4f
   __TEXT.__ustring: 0x168
   __TEXT.__swift5_typeref: 0x2a9

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x4f08
+  __TEXT.__unwind_info: 0x4f18
   __TEXT.__eh_frame: 0x330
-  __TEXT.__objc_classname: 0x3121
-  __TEXT.__objc_methname: 0x18f64
-  __TEXT.__objc_methtype: 0x4bc8
+  __TEXT.__objc_classname: 0x3122
+  __TEXT.__objc_methname: 0x18ff7
+  __TEXT.__objc_methtype: 0x4bdc
   __TEXT.__objc_stubs: 0x13c40
   __DATA_CONST.__got: 0x1008
-  __DATA_CONST.__const: 0x4890
+  __DATA_CONST.__const: 0x4870
   __DATA_CONST.__objc_classlist: 0xb88
   __DATA_CONST.__objc_catlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x3b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x60b8
+  __DATA_CONST.__objc_selrefs: 0x60c8
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x928
   __DATA_CONST.__objc_arraydata: 0x600
   __AUTH_CONST.__auth_got: 0xe80
-  __AUTH_CONST.__const: 0x2ee8
-  __AUTH_CONST.__cfstring: 0x7a40
-  __AUTH_CONST.__objc_const: 0x1ebe0
+  __AUTH_CONST.__const: 0x2ec8
+  __AUTH_CONST.__cfstring: 0x7a20
+  __AUTH_CONST.__objc_const: 0x1ec40
   __AUTH_CONST.__objc_intobj: 0x8d0
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH.__objc_data: 0x3758
   __AUTH.__data: 0xf8
-  __DATA.__objc_ivar: 0x10b8
+  __DATA.__objc_ivar: 0x10c0
   __DATA.__data: 0x2db0
-  __DATA.__bss: 0x18e0
+  __DATA.__bss: 0x18d0
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x3bd8
   __DATA_DIRTY.__data: 0x270

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5C082041-9981-37D5-A214-5A4E18F404BD
-  Functions: 7226
-  Symbols:   23266
-  CStrings:  8095
+  UUID: 8E1B857C-B184-36E0-B4D6-7C3F63D081B3
+  Functions: 7227
+  Symbols:   23260
+  CStrings:  8100
 
Symbols:
+ +[REMLElementComparator comparatorWithFilteringRules:rankingRules:model:elementsHiddenByDefault:]
+ +[_RERuleMLElementComparator comparatorWithFilteringRules:rankingRules:model:elementsHiddenByDefault:]
+ -[REElementRelevanceEngine addElement:section:].cold.1
+ -[REMLModelManager predictionForLogicalElement:]
+ -[REMutableRelevanceEngineConfiguration setElementsHiddenByDefault:]
+ -[RERelevanceEngineConfiguration elementsHiddenByDefault]
+ -[RERelevanceProviderEnvironment addRelevanceProviderDidTriggerException:completion:]
+ -[REUpNextDisjointSet addItemDidTriggerException:]
+ -[REUpNextDisjointSet addItemDidTriggerException:].cold.1
+ -[_RERuleMLElementComparator initWithFilteringRules:rankingRules:model:elementsHiddenByDefault:]
+ _OBJC_IVAR_$_REMLModelManager._elementsHiddenByDefault
+ _OBJC_IVAR_$__RERuleMLElementComparator._elementsHiddenByDefault
+ __REGetIsInternalBuildDebug150813772
+ __REGetIsInternalBuildDebug150813772.cold.1
+ ___32-[REPeriodOfDayPredictor update]_block_invoke.368
+ ___32-[REPeriodOfDayPredictor update]_block_invoke.372
+ ___54-[REActiveWorkoutPredictor _queue_fetchWorkoutHistory]_block_invoke.319
+ ___67-[REPeriodOfDayPredictor _getHistoricSleepIntervalsWithCompletion:]_block_invoke.384
+ ___67-[REPeriodOfDayPredictor _getHistoricSleepIntervalsWithCompletion:]_block_invoke.384.cold.1
+ ___68-[REPeriodOfDayPredictor _getPredictedSleepIntervalsWithCompletion:]_block_invoke.379
+ ___68-[REPeriodOfDayPredictor _getPredictedSleepIntervalsWithCompletion:]_block_invoke.379.cold.1
+ ___68-[REPeriodOfDayPredictor _getPredictedSleepIntervalsWithCompletion:]_block_invoke.380
+ ___96-[_RERuleMLElementComparator initWithFilteringRules:rankingRules:model:elementsHiddenByDefault:]_block_invoke
+ ___96-[_RERuleMLElementComparator initWithFilteringRules:rankingRules:model:elementsHiddenByDefault:]_block_invoke_2
+ ___block_descriptor_64_e8_32s40s48s56s_e26_v32?0"REFeature"8Q16^B24ls32l8s40l8s48l8s56l8
+ ___block_literal_global.272
+ ___block_literal_global.277
+ ___block_literal_global.279
+ ___block_literal_global.338
+ ___block_literal_global.371
+ ___block_literal_global.40
+ ___block_literal_global.47
+ _objc_msgSend$addItemDidTriggerException:
+ _objc_msgSend$addRelevanceProviderDidTriggerException:completion:
+ _objc_msgSend$comparatorWithFilteringRules:rankingRules:model:elementsHiddenByDefault:
+ _objc_msgSend$elementsHiddenByDefault
+ _objc_msgSend$initWithFilteringRules:rankingRules:model:elementsHiddenByDefault:
+ _objc_msgSend$predictionForLogicalElement:
- +[REMLElementComparator comparatorWithFilteringRules:rankingRules:model:]
- +[_RERuleMLElementComparator comparatorWithFilteringRules:rankingRules:model:]
- -[REMLExplanation _formattedNameForFeature:style:]
- -[REMLExplanation _formattedNameForFeature:style:].cold.1
- -[REMLModelManager predicitionForLogicalElement:]
- -[_RERuleMLElementComparator initWithFilteringRules:rankingRules:model:]
- GCC_except_table55
- ___32-[REPeriodOfDayPredictor update]_block_invoke.365
- ___32-[REPeriodOfDayPredictor update]_block_invoke.369
- ___50-[REMLExplanation _formattedNameForFeature:style:]_block_invoke
- ___54-[REActiveWorkoutPredictor _queue_fetchWorkoutHistory]_block_invoke.316
- ___67-[REPeriodOfDayPredictor _getHistoricSleepIntervalsWithCompletion:]_block_invoke.381
- ___67-[REPeriodOfDayPredictor _getHistoricSleepIntervalsWithCompletion:]_block_invoke.381.cold.1
- ___68-[REPeriodOfDayPredictor _getPredictedSleepIntervalsWithCompletion:]_block_invoke.374
- ___68-[REPeriodOfDayPredictor _getPredictedSleepIntervalsWithCompletion:]_block_invoke.376
- ___68-[REPeriodOfDayPredictor _getPredictedSleepIntervalsWithCompletion:]_block_invoke.376.cold.1
- ___72-[_RERuleMLElementComparator initWithFilteringRules:rankingRules:model:]_block_invoke
- ___72-[_RERuleMLElementComparator initWithFilteringRules:rankingRules:model:]_block_invoke_2
- ___block_descriptor_80_e8_32s40s48s56s64s_e26_v32?0"REFeature"8Q16^B24ls32l8s40l8s48l8s56l8s64l8
- ___block_literal_global.268
- ___block_literal_global.273
- ___block_literal_global.368
- __formattedNameForFeature:style:.CamelCaseRegex
- __formattedNameForFeature:style:.onceToken
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_RelevanceEngine
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_RelevanceEngine
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_RelevanceEngine
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_RelevanceEngine
- _objc_msgSend$_formattedNameForFeature:style:
- _objc_msgSend$_isSystemFeature:
- _objc_msgSend$comparatorWithFilteringRules:rankingRules:model:
- _objc_msgSend$initWithFilteringRules:rankingRules:model:
- _objc_msgSend$localizedLowercaseString
- _objc_msgSend$predicitionForLogicalElement:
CStrings:
+ "%@ value for %@"
+ "%{public}@ adding elements %{public}@ to section %{public}@"
+ "@44@0:8@16@24@32B40"
+ "Attempted to add provider %@"
+ "Encountered rdar://150813772 - Item already in disjoint set. Element: %@, predictedElement: %@"
+ "Evaluating ShouldHideElement for %@ with %lu rules with %lu populated features, hiding elements by default: %s"
+ "Item already in disjoint set - see rdar://150813772"
+ "Scheduling imminent update for relevance provider %{public}@"
+ "Scheduling imminent update for relevance provider manager %{public}@"
+ "_elementsHiddenByDefault"
+ "addItemDidTriggerException:"
+ "addRelevanceProviderDidTriggerException:completion:"
+ "comparatorWithFilteringRules:rankingRules:model:elementsHiddenByDefault:"
+ "doesn't contain"
+ "elementsHiddenByDefault"
+ "initWithFilteringRules:rankingRules:model:elementsHiddenByDefault:"
+ "predictionForLogicalElement:"
+ "setElementsHiddenByDefault:"
+ "updateElementRelevance: finished reloading %{public}@ %{public}@"
+ "updateElementRelevance: not loaded %{public}@"
+ "updateElementRelevance: reloading without cached feature map for %{public}@"
- " feature"
- " relevance"
- "%@ adding elements %@ to section %@"
- "%@contains %@"
- "%@contains value for %@"
- "Evaluating ShouldHideElement for %@ with %lu rules with %lu populated features"
- "Scheduling imminent update for relevance provider %@"
- "Scheduling imminent update for relevance provider manager %@"
- "_formattedNameForFeature:style:"
- "comparatorWithFilteringRules:rankingRules:model:"
- "doesn't"
- "initWithFilteringRules:rankingRules:model:"
- "localizedLowercaseString"
- "predicitionForLogicalElement:"
- "updateElementRelevance: finished reloading %@ %@"
- "updateElementRelevance: not loaded %@"
- "updateElementRelevance: reloading without cached feature map for %@"

```
