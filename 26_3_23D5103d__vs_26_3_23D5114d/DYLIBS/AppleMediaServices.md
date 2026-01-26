## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`

```diff

-9.3.2.0.0
-  __TEXT.__text: 0x777224
+9.3.4.0.0
+  __TEXT.__text: 0x777188
   __TEXT.__auth_stubs: 0x4b40
-  __TEXT.__objc_methlist: 0x230cc
-  __TEXT.__const: 0x5da80
+  __TEXT.__objc_methlist: 0x22f0c
+  __TEXT.__const: 0x5da50
   __TEXT.__dlopen_cstrs: 0x98b
-  __TEXT.__cstring: 0x2e57c
+  __TEXT.__cstring: 0x2e5ce
   __TEXT.__swift5_typeref: 0x6bb7
-  __TEXT.__swift5_reflstr: 0x3af4
+  __TEXT.__swift5_reflstr: 0x3ae4
   __TEXT.__swift5_assocty: 0xf00
   __TEXT.__constg_swiftt: 0x562c
   __TEXT.__swift5_builtin: 0x320

   __TEXT.__swift5_capture: 0x349c
   __TEXT.__swift5_mpenum: 0x7c
   __TEXT.__swift5_protos: 0x104
-  __TEXT.__oslogstring: 0x31759
-  __TEXT.__gcc_except_tab: 0x5ee8
+  __TEXT.__oslogstring: 0x3195b
+  __TEXT.__gcc_except_tab: 0x5ee0
   __TEXT.__ustring: 0x1b2
-  __TEXT.__unwind_info: 0x11b58
+  __TEXT.__unwind_info: 0x11b30
   __TEXT.__eh_frame: 0x162d4
-  __TEXT.__objc_classname: 0x40f2
-  __TEXT.__objc_methname: 0x45a12
-  __TEXT.__objc_methtype: 0x7a4f
-  __TEXT.__objc_stubs: 0x2ef80
+  __TEXT.__objc_classname: 0x40ba
+  __TEXT.__objc_methname: 0x458e5
+  __TEXT.__objc_methtype: 0x7a5b
+  __TEXT.__objc_stubs: 0x2ef60
   __DATA_CONST.__got: 0x1a98
-  __DATA_CONST.__const: 0xc688
-  __DATA_CONST.__objc_classlist: 0x1510
+  __DATA_CONST.__const: 0xc708
+  __DATA_CONST.__objc_classlist: 0x1500
   __DATA_CONST.__objc_catlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x450
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf468
+  __DATA_CONST.__objc_selrefs: 0xf3a8
   __DATA_CONST.__objc_protorefs: 0x220
-  __DATA_CONST.__objc_superrefs: 0xce8
+  __DATA_CONST.__objc_superrefs: 0xce0
   __DATA_CONST.__objc_arraydata: 0x580
   __AUTH_CONST.__auth_got: 0x25b8
   __AUTH_CONST.__const: 0x2e5d8
-  __AUTH_CONST.__cfstring: 0x22e40
-  __AUTH_CONST.__objc_const: 0x3d930
+  __AUTH_CONST.__cfstring: 0x22e60
+  __AUTH_CONST.__objc_const: 0x3d6f8
   __AUTH_CONST.__objc_intobj: 0xc60
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH.__objc_data: 0x9a60
-  __AUTH.__data: 0x2908
-  __DATA.__objc_ivar: 0x18f8
-  __DATA.__data: 0x7998
+  __AUTH.__objc_data: 0x99c0
+  __AUTH.__data: 0x2928
+  __DATA.__objc_ivar: 0x18f4
+  __DATA.__data: 0x7968
   __DATA.__bss: 0x1cf09
   __DATA.__common: 0xb68
   __DATA_DIRTY.__objc_ivar: 0x718

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B7F0DEAD-1F76-3F5E-AEEA-4DAAAB899A74
-  Functions: 27069
-  Symbols:   53355
-  CStrings:  26015
+  UUID: 206A451D-999F-3C1E-A7B3-933F87C3F903
+  Functions: 27030
+  Symbols:   53284
+  CStrings:  25993
 
Symbols:
+ -[AMSFollowUp _getIsInTreatmentGroupWithAreaID:treatmentID:]
+ -[AMSFollowUp _getStringFromBag:forKey:description:defaultValue:]
+ -[AMSFollowUp _getTreatmentIDByStrippingDebugInformationFromID:]
+ -[AMSFollowUp _migrateHardwareFollowUpsIfNeededWithConfig:error:]
+ -[AMSFollowUp bag]
+ -[AMSFollowUp initWithFollowUpController:treatmentStore:bag:]
+ -[AMSFollowUp setBag:]
+ -[AMSFollowUp setTreatmentStore:]
+ -[AMSFollowUp treatmentStore]
+ GCC_except_table48
+ _AMSBagKeyFollowUpUIABTestAreaID
+ _AMSBagKeyFollowUpUIABTestNewUITreatmentID
+ _OBJC_IVAR_$_AMSFollowUp._bag
+ _OBJC_IVAR_$_AMSFollowUp._treatmentStore
+ ___112+[AMSFinancePaymentSheetResponse _flexListDictionaryForValues:styles:account:shouldUppercaseText:designVersion:]_block_invoke.315
+ ___112+[AMSFinancePaymentSheetResponse _flexListDictionaryForValues:styles:account:shouldUppercaseText:designVersion:]_block_invoke.317
+ ___45-[AMSFollowUp _clearGroupedHardwareFollowUps]_block_invoke.127
+ ___50-[AMSFollowUp clearFollowUpWithBackingIdentifier:]_block_invoke.25
+ ___53-[AMSFollowUp _getHardwareOffersFeatureConfigFromBag]_block_invoke_2
+ ___58-[AMSFollowUp _getHardwareFollowUpGroupingEnabledWithBag:]_block_invoke.98
+ ___60-[AMSFollowUp _getIsInTreatmentGroupWithAreaID:treatmentID:]_block_invoke
+ ___60-[AMSFollowUp _getIsInTreatmentGroupWithAreaID:treatmentID:]_block_invoke.90
+ ___65-[AMSFollowUp _getStringFromBag:forKey:description:defaultValue:]_block_invoke
+ ___65-[AMSFollowUp _migrateHardwareFollowUpsIfNeededWithConfig:error:]_block_invoke
+ ___65-[AMSFollowUp _migrateHardwareFollowUpsIfNeededWithConfig:error:]_block_invoke.136
+ ___72-[AMSFinancePaymentSheetResponse performWithTaskInfo:completionHandler:]_block_invoke.297
+ ___77+[AMSFinancePaymentSheetResponse _attributedListDictionaryForValues:account:]_block_invoke.307
+ ___77+[AMSFinancePaymentSheetResponse _attributedListDictionaryForValues:account:]_block_invoke_2.310
+ ___85-[AMSFinancePaymentSheetResponse _performPaymentSheetWithTaskInfo:completionHandler:]_block_invoke.334
+ ___block_descriptor_56_e8_32s40s48s_e34_"AMSPromise"16?0"NSDictionary"8ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e29_"AMSPromise"16?0"NSError"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_65_e8_32s40s48s56s_e32_"AMSPromise"16?0"AMSBoolean"8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.132
+ _objc_msgSend$_getIsInTreatmentGroupWithAreaID:treatmentID:
+ _objc_msgSend$_getStringFromBag:forKey:description:defaultValue:
+ _objc_msgSend$_getTreatmentIDByStrippingDebugInformationFromID:
+ _objc_msgSend$_migrateHardwareFollowUpsIfNeededWithConfig:error:
+ _objc_msgSend$initWithFollowUpController:treatmentStore:bag:
+ _objc_msgSend$primaryDataParseEndTime
+ _objc_msgSend$primaryDataParseStartTime
- -[AMSFollowUp _getHardwareFollowUpSheetURLWithBag:]
- -[AMSFollowUp _getHardwareOffersSheetURL]
- -[AMSPageRenderMetricsEvent init]
- -[AMSPageRenderMetricsEvent pageAppearTime]
- -[AMSPageRenderMetricsEvent pageEndTime]
- -[AMSPageRenderMetricsEvent pageId]
- -[AMSPageRenderMetricsEvent pageInterruptTime]
- -[AMSPageRenderMetricsEvent pageReappearTime]
- -[AMSPageRenderMetricsEvent pageRequestTime]
- -[AMSPageRenderMetricsEvent pageType]
- -[AMSPageRenderMetricsEvent pageUrl]
- -[AMSPageRenderMetricsEvent pageUserInteractiveTime]
- -[AMSPageRenderMetricsEvent placement]
- -[AMSPageRenderMetricsEvent resourceRequestEndTime]
- -[AMSPageRenderMetricsEvent resourceRequestStartTime]
- -[AMSPageRenderMetricsEvent setPageAppearTime:]
- -[AMSPageRenderMetricsEvent setPageEndTime:]
- -[AMSPageRenderMetricsEvent setPageId:]
- -[AMSPageRenderMetricsEvent setPageInterruptTime:]
- -[AMSPageRenderMetricsEvent setPageReappearTime:]
- -[AMSPageRenderMetricsEvent setPageRequestTime:]
- -[AMSPageRenderMetricsEvent setPageType:]
- -[AMSPageRenderMetricsEvent setPageUrl:]
- -[AMSPageRenderMetricsEvent setPageUserInteractiveTime:]
- -[AMSPageRenderMetricsEvent setPlacement:]
- -[AMSPageRenderMetricsEvent setResourceRequestEndTime:]
- -[AMSPageRenderMetricsEvent setResourceRequestStartTime:]
- -[AMSPageRenderMetricsPresenter .cxx_destruct]
- -[AMSPageRenderMetricsPresenter bag]
- -[AMSPageRenderMetricsPresenter dictionaryForPosting]
- -[AMSPageRenderMetricsPresenter endWithActivity:pageMetrics:]
- -[AMSPageRenderMetricsPresenter enqueueEvent]
- -[AMSPageRenderMetricsPresenter importTimings:]
- -[AMSPageRenderMetricsPresenter initWithBag:metrics:]
- -[AMSPageRenderMetricsPresenter metrics]
- -[AMSPageRenderMetricsPresenter pageRenderEvent]
- -[AMSPageRenderMetricsPresenter setBag:]
- -[AMSPageRenderMetricsPresenter setMetrics:]
- -[AMSPageRenderMetricsPresenter setPageRenderEvent:]
- -[AMSPageRenderMetricsPresenter startWithActivity:]
- -[AMSPageRenderMetricsPresenter viewDidAppear]
- -[AMSPageRenderMetricsPresenter viewDidDisappear]
- -[AMSPageRenderMetricsPresenter viewDidLoad]
- -[AMSPageRenderMetricsPresenter viewWillAppear]
- -[AMSPageRenderMetricsPresenter viewWillDisappear]
- _AMSPageRenderMetricsTopic
- _OBJC_CLASS_$_AMSPageRenderMetricsEvent
- _OBJC_CLASS_$_AMSPageRenderMetricsPresenter
- _OBJC_IVAR_$_AMSPageRenderMetricsPresenter._bag
- _OBJC_IVAR_$_AMSPageRenderMetricsPresenter._metrics
- _OBJC_IVAR_$_AMSPageRenderMetricsPresenter._pageRenderEvent
- _OBJC_METACLASS_$_AMSPageRenderMetricsEvent
- _OBJC_METACLASS_$_AMSPageRenderMetricsPresenter
- __OBJC_$_INSTANCE_METHODS_AMSPageRenderMetricsEvent
- __OBJC_$_INSTANCE_METHODS_AMSPageRenderMetricsPresenter
- __OBJC_$_INSTANCE_VARIABLES_AMSPageRenderMetricsPresenter
- __OBJC_$_PROP_LIST_AMSPageRenderMetricsEvent
- __OBJC_$_PROP_LIST_AMSPageRenderMetricsPresenter
- __OBJC_CLASS_RO_$_AMSPageRenderMetricsEvent
- __OBJC_CLASS_RO_$_AMSPageRenderMetricsPresenter
- __OBJC_METACLASS_RO_$_AMSPageRenderMetricsEvent
- __OBJC_METACLASS_RO_$_AMSPageRenderMetricsPresenter
- ___112+[AMSFinancePaymentSheetResponse _flexListDictionaryForValues:styles:account:shouldUppercaseText:designVersion:]_block_invoke.312
- ___112+[AMSFinancePaymentSheetResponse _flexListDictionaryForValues:styles:account:shouldUppercaseText:designVersion:]_block_invoke.314
- ___45-[AMSFollowUp _clearGroupedHardwareFollowUps]_block_invoke.115
- ___45-[AMSPageRenderMetricsPresenter enqueueEvent]_block_invoke
- ___47-[AMSFollowUp migrateHardwareFollowUpsIfNeeded]_block_invoke.19
- ___47-[AMSFollowUp migrateHardwareFollowUpsIfNeeded]_block_invoke.23
- ___50-[AMSFollowUp clearFollowUpWithBackingIdentifier:]_block_invoke.14
- ___51-[AMSFollowUp _getHardwareFollowUpSheetURLWithBag:]_block_invoke
- ___58-[AMSFollowUp _getHardwareFollowUpGroupingEnabledWithBag:]_block_invoke.84
- ___72-[AMSFinancePaymentSheetResponse performWithTaskInfo:completionHandler:]_block_invoke.294
- ___77+[AMSFinancePaymentSheetResponse _attributedListDictionaryForValues:account:]_block_invoke.304
- ___77+[AMSFinancePaymentSheetResponse _attributedListDictionaryForValues:account:]_block_invoke_2.307
- ___85-[AMSFinancePaymentSheetResponse _performPaymentSheetWithTaskInfo:completionHandler:]_block_invoke.331
- ___block_literal_global.117
- _objc_msgSend$_getHardwareFollowUpSheetURLWithBag:
- _objc_msgSend$pageRenderEvent
- _objc_msgSend$setPageAppearTime:
- _objc_msgSend$setPageId:
- _objc_msgSend$setPageRenderEvent:
- _objc_msgSend$setPageType:
- _objc_msgSend$setPageUrl:
- _objc_msgSend$setPageUserInteractiveTime:
CStrings:
+ "%{public}@: Failed to fetch active treatments for area ID: %@. Error: %@"
+ "%{public}@: Failed to load %@ from bag with key \"%@\". Error: %@"
+ "%{public}@: Failed to post follow up item with identifier %{public}@; Error: %{public}@"
+ "%{public}@: Found active treatment for area ID '%@'. Active treatment ID: '%@'. User is in treatment: %@"
+ "%{public}@: Hardware offer configuration: featureFlagEnabled: %@, areaID: %@, treatmentID: %@, isInTreatment: %@, sheet URL: %@, groupingEnabled: %@"
+ "%{public}@: Migration: Failed to clear old hardware follow after migration to grouped follow ups. Error: %@"
+ "%{public}@: Migration: Failed to group individual hardware follow ups into a grouped follow up."
+ "%{public}@: Migration: Failed to run hardware follow up migration. Loading pending follow up items failed with error: %@"
+ "%{public}@: Migration: Finished migrating to grouped follow up."
+ "%{public}@: Migration: No hardware follow ups to migrate"
+ "%{public}@: Migration: Running migration (grouping) on the following follow ups: %@"
+ "%{public}@: Migration: follow up grouping has been disabled. Clearing grouped follow up..."
+ "%{public}@: Missing area ID or treatment ID, skipping treatment check"
+ "%{public}@: No active treatments for area ID: %@"
+ "%{public}@: Posting/updating grouped hardware offer follow up item with grouped items: %@"
+ "%{public}@: Read property directly from ephemeral account. key = %@ | value = %@"
+ "%{public}@: Set property directly on ephemeral account. key = %@ | value = %@"
+ "%{public}@: Successfully %{public}@ed grouped hardware offer follow up with identifier %{public}@"
+ "@\"<AMSTreatmentStoreProtocol>\""
+ "@\"<FLFollowUpControllerProtocol>\""
+ "@\"AMSPromise\"16@?0@\"AMSBoolean\"8"
+ "AppleInAppPurchase"
+ "T@\"<AMSTreatmentStoreProtocol>\",&,N,V_treatmentStore"
+ "T@\"<FLFollowUpControllerProtocol>\",&,N,V_followUpController"
+ "_getIsInTreatmentGroupWithAreaID:treatmentID:"
+ "_getStringFromBag:forKey:description:defaultValue:"
+ "_getTreatmentIDByStrippingDebugInformationFromID:"
+ "_migrateHardwareFollowUpsIfNeededWithConfig:error:"
+ "com.apple.AMSFollowUpIdentifier.Offer.AppleOne"
+ "follow-up-ui-ab-test-area-id"
+ "follow-up-ui-ab-test-new-ui-treatment-id"
+ "hardware offers A/B area ID"
+ "hardware offers A/B treatment ID"
+ "hardware offers sheet URL"
+ "initWithFollowUpController:treatmentStore:bag:"
- "%{public}@: Failed to clear old hardware follow after migration to grouped follow ups. Error: %@"
- "%{public}@: Failed to group individual hardware follow ups into a grouped follow up."
- "%{public}@: Failed to load hardware offers sheet URL from bag with key \"%@\". Using fallback URL: \"%@\" Error: %@"
- "%{public}@: Finished grouping hardware follow ups"
- "%{public}@: Grouped hardware follow ups feature flag is disabled. Running clear..."
- "%{public}@: Hardware offer configuration: isGroupingEnabled: %@, sheet URL: %@"
- "%{public}@: Ignoring attempt to set a property on ephemeral account. key = %@ | value = %@"
- "%{public}@: No hardware follow ups to migrate"
- "%{public}@: Posting/updating grouped hardware offer follow up item"
- "%{public}@: Property directly from ephemeral account. key = %@ | value = %@"
- "%{public}@: Reading property directly from ephemeral account. key = %@"
- "%{public}@: Successfully  %{public}@ed grouped hardware offer follow up with identifier %{public}@"
- "%{public}@: [%{public}@] Importing PageRender timings from JS: %@"
- "%{public}@: [%{public}@] init"
- "@\"AMSPageRenderMetricsEvent\""
- "@\"FLFollowUpController\""
- "AMSPageRenderMetricsEvent"
- "AMSPageRenderMetricsPresenter"
- "T@\"AMSMetrics\",&,N,V_metrics"
- "T@\"AMSPageRenderMetricsEvent\",&,N,V_pageRenderEvent"
- "T@\"FLFollowUpController\",&,N,V_followUpController"
- "_getHardwareFollowUpSheetURLWithBag:"
- "_getHardwareOffersSheetURL"
- "_pageRenderEvent"
- "endWithActivity:pageMetrics:"
- "enqueueEvent"
- "importTimings:"
- "initWithBag:metrics:"
- "page-render-metrics-enabled"
- "pageAppearTime"
- "pageInterruptTime"
- "pageReappearTime"
- "pageRenderEvent"
- "pageUrl"
- "pageUserInteractiveTime"
- "setPageAppearTime:"
- "setPageId:"
- "setPageInterruptTime:"
- "setPageReappearTime:"
- "setPageRenderEvent:"
- "setPageType:"
- "setPageUrl:"
- "setPageUserInteractiveTime:"
- "setPlacement:"
- "startWithActivity:"
- "viewDidAppear"
- "viewDidDisappear"
- "viewDidLoad"
- "viewWillAppear"
- "viewWillDisappear"
- "xp_ase_ams_perf"

```
