## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`

```diff

-10.1.13.2.1
-  __TEXT.__text: 0x8706c4
+10.1.17.0.0
+  __TEXT.__text: 0x87b28c
+  __TEXT.__delay_helper: 0x114
   __TEXT.__lazy_helpers: 0x42f4
-  __TEXT.__objc_methlist: 0x25544
-  __TEXT.__const: 0x64140
+  __TEXT.__objc_methlist: 0x2581c
+  __TEXT.__const: 0x645a0
   __TEXT.__dlopen_cstrs: 0x990
-  __TEXT.__cstring: 0x30e0c
-  __TEXT.__swift5_typeref: 0x90bf
-  __TEXT.__swift5_reflstr: 0x681e
-  __TEXT.__swift5_assocty: 0x13b0
-  __TEXT.__constg_swiftt: 0x7b68
+  __TEXT.__cstring: 0x313c6
+  __TEXT.__swift5_typeref: 0x9207
+  __TEXT.__swift5_reflstr: 0x696e
+  __TEXT.__swift5_assocty: 0x1398
+  __TEXT.__constg_swiftt: 0x7c98
   __TEXT.__swift5_builtin: 0x53c
-  __TEXT.__swift5_fieldmd: 0x7d60
-  __TEXT.__swift5_proto: 0x17d0
-  __TEXT.__swift5_types: 0x8fc
-  __TEXT.__swift_as_entry: 0xb00
-  __TEXT.__swift_as_ret: 0xdb4
-  __TEXT.__swift_as_cont: 0x1aa8
-  __TEXT.__swift5_capture: 0x7810
+  __TEXT.__swift5_fieldmd: 0x7f1c
+  __TEXT.__swift5_proto: 0x17f4
+  __TEXT.__swift5_types: 0x91c
+  __TEXT.__swift_as_entry: 0xb10
+  __TEXT.__swift_as_ret: 0xde0
+  __TEXT.__swift_as_cont: 0x1b24
+  __TEXT.__swift5_capture: 0x7970
   __TEXT.__swift5_mpenum: 0xd4
   __TEXT.__swift5_protos: 0x15c
-  __TEXT.__oslogstring: 0x385a8
-  __TEXT.__gcc_except_tab: 0x547c
+  __TEXT.__oslogstring: 0x38892
+  __TEXT.__gcc_except_tab: 0x54c4
   __TEXT.__ustring: 0x204
-  __TEXT.__unwind_info: 0x1a640
-  __TEXT.__eh_frame: 0x201b4
+  __TEXT.__unwind_info: 0x1aea0
+  __TEXT.__eh_frame: 0x20604
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd868
-  __DATA_CONST.__objc_classlist: 0x16c0
+  __DATA_CONST.__const: 0xd938
+  __DATA_CONST.__objc_classlist: 0x16d8
   __DATA_CONST.__objc_catlist: 0xf0
-  __DATA_CONST.__objc_protolist: 0x4e8
+  __DATA_CONST.__objc_protolist: 0x510
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x106d0
-  __DATA_CONST.__objc_protorefs: 0x278
+  __DATA_CONST.__objc_selrefs: 0x10820
+  __DATA_CONST.__objc_protorefs: 0x290
   __DATA_CONST.__objc_superrefs: 0xd28
   __DATA_CONST.__objc_arraydata: 0x5f8
-  __DATA_CONST.__got: 0x1b40
-  __AUTH_CONST.__const: 0x3c780
-  __AUTH_CONST.__cfstring: 0x24340
-  __AUTH_CONST.__objc_const: 0x42050
+  __DATA_CONST.__got: 0x1b68
+  __AUTH_CONST.__const: 0x3d080
+  __AUTH_CONST.__cfstring: 0x244a0
+  __AUTH_CONST.__objc_const: 0x423a8
   __AUTH_CONST.__lazy_load_got: 0x638
   __AUTH_CONST.__objc_intobj: 0xd20
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH_CONST.__auth_got: 0x27c0
-  __AUTH.__objc_data: 0xb290
-  __AUTH.__data: 0x3530
-  __DATA.__objc_ivar: 0x1a78
-  __DATA.__data: 0x91b0
+  __AUTH_CONST.__auth_got: 0x27d8
+  __AUTH.__objc_data: 0xb440
+  __AUTH.__data: 0x35c0
+  __DATA.__objc_ivar: 0x1a70
+  __DATA.__data: 0x93d4
   __DATA.__common: 0xb6c
   __DATA_DIRTY.__objc_ivar: 0x72c
   __DATA_DIRTY.__objc_data: 0x5db8
-  __DATA_DIRTY.__data: 0x2fc8
+  __DATA_DIRTY.__data: 0x2fd0
   __DATA_DIRTY.__bss: 0x62e0
   __DATA_DIRTY.__common: 0xa8
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/AppleMediaServicesKitInternal.framework/AppleMediaServicesKitInternal
   - /System/Library/PrivateFrameworks/AsyncAlgorithmsInternal.framework/AsyncAlgorithmsInternal
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
+  - /System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit
   - /System/Library/PrivateFrameworks/CollectionsInternal.framework/CollectionsInternal
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport
   - /System/Library/PrivateFrameworks/CryptoKitPrivate.framework/CryptoKitPrivate

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 35824
-  Symbols:   27341
-  CStrings:  9845
+  Functions: 36159
+  Symbols:   27439
+  CStrings:  9886
 
Symbols:
+ +[AMSData contentTypeForEncoding:]
+ +[AMSDevice frontCameraOffsetFromCenterOfDisplayAtIndex:]
+ +[AMSFinancePaymentSheetResponse _preloadPromiseForSalableIconURL:activePurchaseTask:logKey:]
+ +[AMSProcessInfo attributionBundleIdentifierForProxyAppBundleID:hasAttributionEntitlement:]
+ +[AMSProcessInfo hasNetworkAttributionEntitlement]
+ +[AMSPurchaseRequestEncoder shouldCompressRequestPropertiesUsingBag:]
+ +[AMSTreatmentStore isExcludedTreatmentStoreError:]
+ +[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespace:bag:canonicalAccountIdentifierProvider:reportsErrorsToMetrics:]
+ +[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespaces:canonicalAccountIdentifierProvider:reportsErrorsToMetrics:]
+ +[AMSURLSession _configurationForClientInfo:]
+ +[NSURLSessionConfiguration(AppleMediaServices_Project) ams_defaultConfiguration]
+ -[AMSFollowUp _activeMediaAccountDSID]
+ -[AMSFollowUp _clearGroupedHardwareFollowUpsForOtherAccounts:groupingDSID:]
+ -[AMSFollowUp _isEligibleForGroupedHardwareOffer:]
+ -[AMSMediaSharedProperties _initWithClientIdentifier:sessionCacheKey:account:bag:clientInfo:URLKnownToBeTrusted:URLSessionConfiguration:]
+ -[AMSMediaSharedProperties sessionCacheKey]
+ -[AMSTreatmentStore _encodeExperimentData:reportsErrorsToMetrics:]
+ -[AMSTreatmentStore _reportFailureToMetrics:reportsErrorsToMetrics:]
+ -[AMSTreatmentStore _reportPropagatedFailureToMetrics:failureReason:reportsErrorsToMetrics:]
+ -[AMSTreatmentStore activeTreatmentsForAreas:canonicalAccountIdentifierProvider:reportsErrorsToMetrics:]
+ -[AMSTreatmentStore activeTreatmentsForAreas:userId:canonicalAccountIdentifier:reportsErrorsToMetrics:]
+ -[AMSTreatmentStore activeTreatmentsForAreas:userId:canonicalAccountIdentifierProvider:reportsErrorsToMetrics:]
+ -[AMSTreatmentStore areasForNamespaces:reportsErrorsToMetrics:]
+ -[AMSTreatmentStore areasForTopics:reportsErrorsToMetrics:]
+ -[AMSTreatmentStore areasWithIDs:reportsErrorsToMetrics:]
+ -[AMSTreatmentStore encodeExperimentDataForTopic:userId:canonicalAccountIdentifier:reportsErrorsToMetrics:]
+ -[AMSTreatmentStore experimentDataForAreas:userId:canonicalAccountIdentifier:reportsErrorsToMetrics:]
+ -[AMSTreatmentStore treatmentsForAreas:startDate:endDate:userId:canonicalAccountIdentifier:reportsErrorsToMetrics:]
+ -[AMSURLRequestEncoder reportsTreatmentErrorsToMetrics]
+ -[AMSURLRequestEncoder setReportsTreatmentErrorsToMetrics:]
+ -[AMSURLRequestProperties initWithLogUUID:]
+ -[NSMutableURLRequest(AppleMediaServices) ams_addProductTypeHeader]
+ -[NSMutableURLRequest(AppleMediaServices) ams_compressBodyWithLogUUID:loggingFor:]
+ _AMSBagKeyPurchaseRequestCompressionEnabled
+ _MGCopyAnswerForDisplayAtIndex
+ _MobileGestalt_get_current_device
+ _MobileGestalt_get_deviceSupportsSecureDoubleClick
+ _MobileGestalt_get_touchIDCapability
+ _OBJC_CLASS_$_AMSPasscodeEngagementModel
+ _OBJC_CLASS_$_AMSRequestBody
+ _OBJC_CLASS_$_BKDevice
+ _OBJC_CLASS_$_BKDevice$loadHelper_x2
+ _OBJC_CLASS_$_BKDeviceDescriptor
+ _OBJC_CLASS_$_BKDeviceDescriptor$loadHelper_x8
+ _OBJC_CLASS_$_DIDocUploadSession$lazyGOT$loadHelper_x8$for$_OUTLINED_FUNCTION_65+8
+ _OBJC_CLASS_$_DIUploadAsset$lazyGOT$loadHelper_x2$for$_OUTLINED_FUNCTION_42+12
+ _OBJC_IVAR_$_AMSMediaSharedProperties._sessionCacheKey
+ _OBJC_IVAR_$_AMSURLRequestEncoder._reportsTreatmentErrorsToMetrics
+ _OBJC_METACLASS_$_AMSPasscodeEngagementModel
+ _OBJC_METACLASS_$_AMSRequestBody
+ _OBJC_METACLASS_$__TtC18AppleMediaServicesP33_0C3F1A1405D21E15EFF43EDC83308B7B25SelfieBiometricKitMatcher
+ __CLASS_METHODS_AMSPasscodeEngagementModel
+ __CLASS_METHODS_AMSRequestBody
+ __CLASS_PROPERTIES_AMSPasscodeEngagementModel
+ __DATA_AMSPasscodeEngagementModel
+ __DATA_AMSRequestBody
+ __DATA__TtC18AppleMediaServicesP33_0C3F1A1405D21E15EFF43EDC83308B7B25SelfieBiometricKitMatcher
+ __INSTANCE_METHODS_AMSPasscodeEngagementModel
+ __INSTANCE_METHODS_AMSRequestBody
+ __INSTANCE_METHODS__TtC18AppleMediaServicesP33_0C3F1A1405D21E15EFF43EDC83308B7B25SelfieBiometricKitMatcher
+ __IVARS_AMSPasscodeEngagementModel
+ __IVARS_AMSRequestBody
+ __IVARS__TtC18AppleMediaServicesP33_0C3F1A1405D21E15EFF43EDC83308B7B25SelfieBiometricKitMatcher
+ __METACLASS_DATA_AMSPasscodeEngagementModel
+ __METACLASS_DATA_AMSRequestBody
+ __METACLASS_DATA__TtC18AppleMediaServicesP33_0C3F1A1405D21E15EFF43EDC83308B7B25SelfieBiometricKitMatcher
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKMatchOperationDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_BKOperationDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKMatchOperationDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_BKOperationDelegate
+ __OBJC_$_PROTOCOL_REFS_BKMatchOperationDelegate
+ __OBJC_$_PROTOCOL_REFS_BKOperationDelegate
+ __OBJC_LABEL_PROTOCOL_$_BKMatchOperationDelegate
+ __OBJC_LABEL_PROTOCOL_$_BKOperationDelegate
+ __OBJC_PROTOCOL_$_BKMatchOperationDelegate
+ __OBJC_PROTOCOL_$_BKOperationDelegate
+ __PROPERTIES_AMSPasscodeEngagementModel
+ __PROPERTIES_AMSRequestBody
+ __PROTOCOLS_AMSPasscodeEngagementModel
+ __PROTOCOLS__TtC18AppleMediaServicesP33_0C3F1A1405D21E15EFF43EDC83308B7B25SelfieBiometricKitMatcher
+ __PROTOCOL_INSTANCE_METHODS__TtP18AppleMediaServices36SelfieAuthenticationServiceInterface_
+ __PROTOCOL_METHOD_TYPES__TtP18AppleMediaServices36SelfieAuthenticationServiceInterface_
+ __PROTOCOL__TtP18AppleMediaServices36SelfieAuthenticationServiceInterface_
+ ___101-[AMSTreatmentStore experimentDataForAreas:userId:canonicalAccountIdentifier:reportsErrorsToMetrics:]_block_invoke
+ ___103-[AMSTreatmentStore activeTreatmentsForAreas:userId:canonicalAccountIdentifier:reportsErrorsToMetrics:]_block_invoke
+ ___103-[AMSTreatmentStore activeTreatmentsForAreas:userId:canonicalAccountIdentifier:reportsErrorsToMetrics:]_block_invoke_2
+ ___107-[AMSTreatmentStore encodeExperimentDataForTopic:userId:canonicalAccountIdentifier:reportsErrorsToMetrics:]_block_invoke
+ ___107-[AMSTreatmentStore encodeExperimentDataForTopic:userId:canonicalAccountIdentifier:reportsErrorsToMetrics:]_block_invoke_2
+ ___111-[AMSTreatmentStore activeTreatmentsForAreas:userId:canonicalAccountIdentifierProvider:reportsErrorsToMetrics:]_block_invoke
+ ___111-[AMSTreatmentStore activeTreatmentsForAreas:userId:canonicalAccountIdentifierProvider:reportsErrorsToMetrics:]_block_invoke_2
+ ___115-[AMSTreatmentStore treatmentsForAreas:startDate:endDate:userId:canonicalAccountIdentifier:reportsErrorsToMetrics:]_block_invoke
+ ___115-[AMSTreatmentStore treatmentsForAreas:startDate:endDate:userId:canonicalAccountIdentifier:reportsErrorsToMetrics:]_block_invoke_2
+ ___115-[AMSTreatmentStore treatmentsForAreas:startDate:endDate:userId:canonicalAccountIdentifier:reportsErrorsToMetrics:]_block_invoke_3
+ ___137+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespaces:canonicalAccountIdentifierProvider:reportsErrorsToMetrics:]_block_invoke
+ ___137+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespaces:canonicalAccountIdentifierProvider:reportsErrorsToMetrics:]_block_invoke_2
+ ___137+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespaces:canonicalAccountIdentifierProvider:reportsErrorsToMetrics:]_block_invoke_3
+ ___137+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespaces:canonicalAccountIdentifierProvider:reportsErrorsToMetrics:]_block_invoke_4
+ ___140+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespace:bag:canonicalAccountIdentifierProvider:reportsErrorsToMetrics:]_block_invoke
+ ___54-[AMSPurchaseRequestEncoder initWithPurchaseInfo:bag:]_block_invoke
+ ___57-[AMSTreatmentStore areasWithIDs:reportsErrorsToMetrics:]_block_invoke
+ ___57-[AMSTreatmentStore areasWithIDs:reportsErrorsToMetrics:]_block_invoke_2
+ ___57-[AMSTreatmentStore areasWithIDs:reportsErrorsToMetrics:]_block_invoke_3
+ ___57-[AMSTreatmentStore areasWithIDs:reportsErrorsToMetrics:]_block_invoke_4
+ ___59-[AMSTreatmentStore areasForTopics:reportsErrorsToMetrics:]_block_invoke
+ ___59-[AMSTreatmentStore areasForTopics:reportsErrorsToMetrics:]_block_invoke_2
+ ___59-[AMSTreatmentStore areasForTopics:reportsErrorsToMetrics:]_block_invoke_3
+ ___59-[AMSTreatmentStore areasForTopics:reportsErrorsToMetrics:]_block_invoke_4
+ ___63-[AMSTreatmentStore areasForNamespaces:reportsErrorsToMetrics:]_block_invoke
+ ___63-[AMSTreatmentStore areasForNamespaces:reportsErrorsToMetrics:]_block_invoke_2
+ ___63-[AMSTreatmentStore areasForNamespaces:reportsErrorsToMetrics:]_block_invoke_3
+ ___63-[AMSTreatmentStore areasForNamespaces:reportsErrorsToMetrics:]_block_invoke_4
+ ___69+[AMSPurchaseRequestEncoder shouldCompressRequestPropertiesUsingBag:]_block_invoke
+ ___75-[AMSFollowUp _clearGroupedHardwareFollowUpsForOtherAccounts:groupingDSID:]_block_invoke
+ ___75-[AMSFollowUp _clearGroupedHardwareFollowUpsForOtherAccounts:groupingDSID:]_block_invoke_2
+ ___92-[AMSPurchaseProtocolHandler reconfigureNewRequest:originalTask:redirect:completionHandler:]_block_invoke_2
+ ___93+[AMSFinancePaymentSheetResponse _preloadPromiseForSalableIconURL:activePurchaseTask:logKey:]_block_invoke
+ ___block_descriptor_105_e8_32s40s48s56s64s72s80s88r_e5_v8?0lr88l8s32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_40_e46_"AMSPromise"24?0"AMSURLResult"8"NSError"16l
+ ___block_descriptor_40_e8_32s_e20_v16?0"AMSBoolean"8ls32l8
+ ___block_descriptor_40_e8_32s_e24_B16?0"FLFollowUpItem"8ls32l8
+ ___block_descriptor_41_e8_32s_e17_v16?0"NSError"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e34_v24?0"AMSURLAction"8"NSError"16ls32l8s40l8
+ ___block_descriptor_49_e8_32s40s_e17_v16?0"NSError"8ls32l8s40l8
+ ___block_descriptor_57_e8_32s40s48s_e33_"AMSPromise"16?0"AMSOptional"8ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48bs_e46_"AMSPromise"24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e32_v24?0"AMSBoolean"8"NSError"16ls32l8s40l8s56l8s48l8
+ ___block_descriptor_65_e8_32s40s48s56s_e34_"AMSPromise"16?0"NSDictionary"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_65_e8_32s40s48s_e34_"AMSPromise"16?0"NSDictionary"8ls32l8s40l8s48l8
+ ___block_descriptor_73_e8_32s40s48s56bs_e46_"AMSPromise"24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_73_e8_32s40s48s56s64bs_e20_v20?0B8"NSError"12ls32l8s40l8s48l8s64l8s56l8
+ ___swift_closure_destructor.24Tm
+ ___swift_closure_destructor.31Tm
+ ___swift_closure_destructor.49Tm
+ ___swift_memcpy351_8
+ ___swift_memcpy711_8
+ _associated conformance 10Foundation4DateV18AppleMediaServicesE24ISO8601UTCTimeZoneFormatOSHADSQ
+ _associated conformance 10Foundation4DateV18AppleMediaServicesE26ISO8601LocalTimeZoneFormatOSHADSQ
+ _associated conformance 18AppleMediaServices23SelfieBiometricKitErrorO10Foundation13CustomNSErrorAAs0G0
+ _associated conformance 18AppleMediaServices23SelfieBiometricKitErrorOSHAASQ
+ _dlopenHelper$BiometricKit
+ _dlopenHelperFlag$BiometricKit
+ _flat unique 18AppleMediaServices36SelfieAuthenticationServiceInterface_p
+ _get_enum_tag_for_layout_string 18AppleMediaServices15RequestBodyCoreO8EncodingO
+ _kMGDisplayIndexedQueryFrontCameraOffsetFromDisplayCenter
+ _symbolic $s18AppleMediaServices36SelfieAuthenticationServiceInterfaceP
+ _symbolic ScCySb______pGSg s5ErrorP
+ _symbolic ScCy_____Sg_____G 18AppleMediaServices20AutoBugCaptureReportC8Reporter33_53E9BFD2965C81AFBEDE880E2C1BF3BALLV s5NeverO
+ _symbolic So16BKMatchOperationC
+ _symbolic So8BKDeviceC
+ _symbolic _____ 10Foundation4DateV18AppleMediaServicesE24ISO8601UTCTimeZoneFormatO
+ _symbolic _____ 10Foundation4DateV18AppleMediaServicesE26ISO8601LocalTimeZoneFormatO
+ _symbolic _____ 18AppleMediaServices15RequestBodyCoreO
+ _symbolic _____ 18AppleMediaServices15RequestBodyCoreO0E0V
+ _symbolic _____ 18AppleMediaServices15RequestBodyCoreO8EncodingO
+ _symbolic _____ 18AppleMediaServices20AutoBugCaptureReportC8Reporter33_53E9BFD2965C81AFBEDE880E2C1BF3BALLV
+ _symbolic _____ 18AppleMediaServices23SelfieBiometricKitErrorO
+ _symbolic _____ 18AppleMediaServices25SelfieBiometricKitMatcher33_0C3F1A1405D21E15EFF43EDC83308B7BLLC
+ _symbolic _____Sg 18AppleMediaServices20AutoBugCaptureReportC8Reporter33_53E9BFD2965C81AFBEDE880E2C1BF3BALLV
+ _symbolic ______p 18AppleMediaServices36SelfieAuthenticationServiceInterfaceP
+ _symbolic ______pSg 18AppleMediaServices36SelfieAuthenticationServiceInterfaceP
+ _symbolic ______pSgIegn_ 18AppleMediaServices36SelfieAuthenticationServiceInterfaceP
+ _symbolic xSgz_______p_lXX 18AppleMediaServices36SelfieAuthenticationServiceInterfaceP
+ _type_layout_string 18AppleMediaServices15RequestBodyCoreO0E0V
+ _type_layout_string 18AppleMediaServices15RequestBodyCoreO8EncodingO
+ _type_layout_string 18AppleMediaServices20AutoBugCaptureReportC8Reporter33_53E9BFD2965C81AFBEDE880E2C1BF3BALLV
- +[AMSProcessInfo attributionBundleIdentifierForProxyAppBundleID:hasImpersonateEntitlement:]
- +[AMSProcessInfo hasNetworkImpersonationEntitlement]
- +[AMSURLSession _defaultConfiguration]
- -[AMSFinanceActionResponse _runAction:completionHandler:]
- -[AMSFinanceActionResponse asyncQueue]
- -[AMSFinanceActionResponse detached]
- -[AMSFinanceActionResponse setAsyncQueue:]
- -[AMSFinanceActionResponse setDetached:]
- -[AMSFinanceDialogResponse asyncQueue]
- -[AMSFinanceDialogResponse detached]
- -[AMSFinanceDialogResponse setAsyncQueue:]
- -[AMSFinanceDialogResponse setDetached:]
- -[AMSMediaSharedProperties _initWithClientIdentifier:account:bag:clientInfo:URLKnownToBeTrusted:URLSessionConfiguration:]
- -[AMSTreatmentStore _encodeExperimentData:]
- -[NSMutableURLRequest(AppleMediaServices) ams_addContentLengthHeaderForData:]
- -[NSMutableURLRequest(AppleMediaServices) ams_addContentTypeHeaderForEncoding:]
- _OBJC_CLASS_$_DIDocUploadSession$lazyGOT$loadHelper_x8$for$_OUTLINED_FUNCTION_56+8
- _OBJC_CLASS_$_DIUploadAsset$lazyGOT$loadHelper_x2$for$_OUTLINED_FUNCTION_39+12
- _OBJC_IVAR_$_AMSFinanceActionResponse._asyncQueue
- _OBJC_IVAR_$_AMSFinanceActionResponse._detached
- _OBJC_IVAR_$_AMSFinanceDialogResponse._asyncQueue
- _OBJC_IVAR_$_AMSFinanceDialogResponse._detached
- ___114+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespaces:canonicalAccountIdentifierProvider:]_block_invoke
- ___114+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespaces:canonicalAccountIdentifierProvider:]_block_invoke_2
- ___114+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespaces:canonicalAccountIdentifierProvider:]_block_invoke_3
- ___114+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespaces:canonicalAccountIdentifierProvider:]_block_invoke_4
- ___117+[AMSURLRequestDecoration addTreatmentHeadersToRequest:forTreatmentNamespace:bag:canonicalAccountIdentifierProvider:]_block_invoke
- ___34-[AMSTreatmentStore areasWithIDs:]_block_invoke
- ___34-[AMSTreatmentStore areasWithIDs:]_block_invoke_2
- ___34-[AMSTreatmentStore areasWithIDs:]_block_invoke_3
- ___34-[AMSTreatmentStore areasWithIDs:]_block_invoke_4
- ___36-[AMSTreatmentStore areasForTopics:]_block_invoke
- ___36-[AMSTreatmentStore areasForTopics:]_block_invoke_2
- ___36-[AMSTreatmentStore areasForTopics:]_block_invoke_3
- ___36-[AMSTreatmentStore areasForTopics:]_block_invoke_4
- ___40-[AMSTreatmentStore areasForNamespaces:]_block_invoke
- ___40-[AMSTreatmentStore areasForNamespaces:]_block_invoke_2
- ___40-[AMSTreatmentStore areasForNamespaces:]_block_invoke_3
- ___40-[AMSTreatmentStore areasForNamespaces:]_block_invoke_4
- ___57-[AMSFinanceActionResponse _runAction:completionHandler:]_block_invoke
- ___66-[AMSFinanceActionResponse performWithTaskInfo:completionHandler:]_block_invoke_2
- ___78-[AMSTreatmentStore experimentDataForAreas:userId:canonicalAccountIdentifier:]_block_invoke
- ___80-[AMSTreatmentStore activeTreatmentsForAreas:userId:canonicalAccountIdentifier:]_block_invoke
- ___80-[AMSTreatmentStore activeTreatmentsForAreas:userId:canonicalAccountIdentifier:]_block_invoke_2
- ___84-[AMSTreatmentStore encodeExperimentDataForTopic:userId:canonicalAccountIdentifier:]_block_invoke
- ___84-[AMSTreatmentStore encodeExperimentDataForTopic:userId:canonicalAccountIdentifier:]_block_invoke_2
- ___88-[AMSTreatmentStore activeTreatmentsForAreas:userId:canonicalAccountIdentifierProvider:]_block_invoke
- ___88-[AMSTreatmentStore activeTreatmentsForAreas:userId:canonicalAccountIdentifierProvider:]_block_invoke_2
- ___92-[AMSTreatmentStore treatmentsForAreas:startDate:endDate:userId:canonicalAccountIdentifier:]_block_invoke
- ___92-[AMSTreatmentStore treatmentsForAreas:startDate:endDate:userId:canonicalAccountIdentifier:]_block_invoke_2
- ___92-[AMSTreatmentStore treatmentsForAreas:startDate:endDate:userId:canonicalAccountIdentifier:]_block_invoke_3
- ___block_descriptor_32_e22_v16?0"AMSURLAction"8l
- ___block_descriptor_40_e8_32bs_e34_v24?0"AMSURLAction"8"NSError"16ls32l8
- ___block_descriptor_56_e8_32s40s48s_e33_"AMSPromise"16?0"AMSOptional"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48bs_e46_"AMSPromise"24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56s_e34_"AMSPromise"16?0"NSDictionary"8ls32l8s40l8s48l8s56l8
- ___block_descriptor_64_e8_32s40s48s_e34_"AMSPromise"16?0"NSDictionary"8ls32l8s40l8s48l8
- ___block_descriptor_65_e8_32s40s48s56bs_e20_v20?0B8"NSError"12ls32l8s40l8s56l8s48l8
- ___block_descriptor_72_e8_32s40s48s56bs_e46_"AMSPromise"24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_descriptor_97_e8_32s40s48s56s64s72s80r_e5_v8?0lr80l8s32l8s40l8s48l8s56l8s64l8s72l8
- ___swift_closure_destructor.20Tm
- ___swift_closure_destructor.28Tm
- ___swift_closure_destructor.41Tm
- ___swift_memcpy343_8
- ___swift_memcpy695_8
- _objc_retain_x7
- _symbolic _____Sg 18AppleMediaServices30AutoBugCaptureCallbackDelegate33_53E9BFD2965C81AFBEDE880E2C1BF3BALLC
CStrings:
+ "%{public}@: Dropping hardware offer follow up %{public}@: its account is not the active Media account."
+ "%{public}@: Migration: Failed to clear grouped hardware follow ups belonging to other accounts. Error: %@"
+ "%{public}@: Migration: No active iTunes account. Leaving hardware follow ups as they are."
+ "%{public}@: Migration: clearing grouped hardware follow ups belonging to other accounts: %@"
+ "%{public}@: No grouped hardware offer follow up with identifier %{public}@"
+ "%{public}@: [%{public}@] Failed to obtain front camera offset for display %{public}ld: %{public}d"
+ "%{public}@: [%{public}@] Failed to resolve the canonical account identifier (error: %{public}@)"
+ "%{public}@: [%{public}@] Nil clientIdentifier; every such caller shares one session cache entry"
+ "%{public}@Unable to compress request body. Using uncompressed body. error = %{public}@"
+ "/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit"
+ "AppleMediaServices.PasscodeEngagementModel"
+ "AppleMediaServices.SelfieBiometricKitMatcher"
+ "AppleMediaServices_BridgedInterface.RequestBody"
+ "BK faceid failed. Falling back to LA."
+ "Failed to fetch area identifiers for namespaces"
+ "Failed to fetch area identifiers for topics"
+ "Failed to fetch areas"
+ "Failed to fetch treatments"
+ "Failed to resolve the canonical account identifier"
+ "Failed to start match operation: "
+ "Failed to synchronize treatments"
+ "Grouped hardware offers are only shown for the active Media account"
+ "Inactive Account"
+ "Match result. matched: "
+ "Match session started"
+ "Match went on hold (timeout); cancelling."
+ "Matching failed with reason: "
+ "Operation finished with reason: "
+ "PassLibraryCacheWarming"
+ "Pre-evaluation failed: neither FaceID nor TouchID-with-intent constraints were satisfied"
+ "Pre-evaluation failed: passcode is not the sole alternative to the conjunction"
+ "Pre-evaluation failed: signing is not a TouchID and button press conjunction"
+ "PreloadSalableIconAtKnownURL"
+ "Presence detected while in lockout: "
+ "Running FaceIDBK Auth"
+ "TreatmentStoreErrorMetrics"
+ "Treatments"
+ "X-Apple-Product-Type"
+ "com.apple.AppleMediaServices.AgeVerificationExtension"
+ "com.apple.AppleMediaServices.SelfieBiometricKitError"
+ "com.apple.ams.selfie.faceid.bkmatch"
+ "com.apple.private.network.socket-delegate"
+ "faceIDBK"
+ "performBiometricAuthentication()"
+ "purchase-request-compression-enabled"
+ "tiltCorrectionThreshold"
+ "touchIDWithUserIntent"
+ "treatments"
+ "v16@?0@\"AMSBoolean\"8"
- "%{public}@Failed to gzip request body. error = %{public}@"
- "%{public}@Unable to compress request body. Using uncompressed body."
- "CompressPurchaseRequestBodies"
- "Pre-evaluation failed: FaceID constraints not satisfied"
- "com.apple.AMSFinanceActionResponse"
- "com.apple.AMSFinanceDialogResponse"
- "com.apple.private.nsurlsession.impersonate"
- "detached"
```
