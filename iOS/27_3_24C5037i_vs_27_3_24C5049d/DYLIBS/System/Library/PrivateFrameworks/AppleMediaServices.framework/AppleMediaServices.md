## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`

```diff

-10.2.12.0.0
-  __TEXT.__text: 0x89244c
+10.2.18.0.0
+  __TEXT.__text: 0x8a91e0
   __TEXT.__delay_helper: 0x114
   __TEXT.__lazy_helpers: 0x42f4
-  __TEXT.__objc_methlist: 0x26484
-  __TEXT.__const: 0x64e20
+  __TEXT.__objc_methlist: 0x26a7c
+  __TEXT.__const: 0x65a38
   __TEXT.__dlopen_cstrs: 0xa54
-  __TEXT.__cstring: 0x320cf
-  __TEXT.__swift5_typeref: 0x9473
-  __TEXT.__swift5_reflstr: 0x6cce
-  __TEXT.__swift5_assocty: 0x13b0
-  __TEXT.__constg_swiftt: 0x7f18
-  __TEXT.__swift5_builtin: 0x550
-  __TEXT.__swift5_fieldmd: 0x8258
-  __TEXT.__swift5_proto: 0x1848
-  __TEXT.__swift5_types: 0x958
-  __TEXT.__swift_as_entry: 0xb34
-  __TEXT.__swift_as_ret: 0xe10
-  __TEXT.__swift_as_cont: 0x1b94
-  __TEXT.__swift5_capture: 0x7cdc
-  __TEXT.__swift5_mpenum: 0xd4
-  __TEXT.__swift5_protos: 0x160
-  __TEXT.__oslogstring: 0x3934a
-  __TEXT.__gcc_except_tab: 0x5638
+  __TEXT.__cstring: 0x32a83
+  __TEXT.__swift5_typeref: 0x98a3
+  __TEXT.__swift5_reflstr: 0x735e
+  __TEXT.__swift5_assocty: 0x14d0
+  __TEXT.__constg_swiftt: 0x8170
+  __TEXT.__swift5_builtin: 0x58c
+  __TEXT.__swift5_fieldmd: 0x8670
+  __TEXT.__swift5_proto: 0x18e0
+  __TEXT.__swift5_types: 0x99c
+  __TEXT.__swift_as_entry: 0xb40
+  __TEXT.__swift_as_ret: 0xe1c
+  __TEXT.__swift_as_cont: 0x1bac
+  __TEXT.__swift5_capture: 0x7e3c
+  __TEXT.__swift5_mpenum: 0xf0
+  __TEXT.__swift5_protos: 0x164
+  __TEXT.__oslogstring: 0x395ba
+  __TEXT.__gcc_except_tab: 0x5650
   __TEXT.__ustring: 0x204
-  __TEXT.__unwind_info: 0x1ba48
-  __TEXT.__eh_frame: 0x20c2c
+  __TEXT.__unwind_info: 0x1b700
+  __TEXT.__eh_frame: 0x2114c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xdbd8
-  __DATA_CONST.__objc_classlist: 0x1730
+  __DATA_CONST.__const: 0xdd50
+  __DATA_CONST.__objc_classlist: 0x1758
   __DATA_CONST.__objc_catlist: 0xf0
-  __DATA_CONST.__objc_protolist: 0x518
+  __DATA_CONST.__objc_protolist: 0x520
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10d28
-  __DATA_CONST.__objc_protorefs: 0x288
+  __DATA_CONST.__objc_selrefs: 0x11078
+  __DATA_CONST.__objc_protorefs: 0x290
   __DATA_CONST.__objc_superrefs: 0xd40
   __DATA_CONST.__objc_arraydata: 0x5f8
-  __DATA_CONST.__got: 0x1ba8
-  __AUTH_CONST.__const: 0x3e380
-  __AUTH_CONST.__cfstring: 0x24b20
-  __AUTH_CONST.__objc_const: 0x436f8
+  __DATA_CONST.__got: 0x1c38
+  __AUTH_CONST.__const: 0x3efe0
+  __AUTH_CONST.__cfstring: 0x24fe0
+  __AUTH_CONST.__objc_const: 0x43dd8
   __AUTH_CONST.__lazy_load_got: 0x638
   __AUTH_CONST.__objc_intobj: 0xd38
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH_CONST.__auth_got: 0x2830
-  __AUTH.__objc_data: 0xb990
-  __AUTH.__data: 0x37a0
-  __DATA.__objc_ivar: 0x1b0c
-  __DATA.__data: 0x9614
+  __AUTH_CONST.__auth_got: 0x28e0
+  __AUTH.__objc_data: 0xbc50
+  __AUTH.__data: 0x3900
+  __DATA.__objc_ivar: 0x1b54
+  __DATA.__data: 0x97c4
   __DATA.__common: 0xb74
-  __DATA_DIRTY.__objc_ivar: 0x758
+  __DATA_DIRTY.__objc_ivar: 0x75c
   __DATA_DIRTY.__objc_data: 0x5d68
-  __DATA_DIRTY.__data: 0x2de0
-  __DATA_DIRTY.__bss: 0x6340
+  __DATA_DIRTY.__data: 0x2e30
+  __DATA_DIRTY.__bss: 0x6330
   __DATA_DIRTY.__common: 0xa0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 36836
-  Symbols:   27850
-  CStrings:  10022
+  Functions: 37409
+  Symbols:   28094
+  CStrings:  10111
 
Symbols:
+ +[AMSDefaults harMaxDirectorySizeMegabytes]
+ +[AMSDefaults setUseIDCaptureTestImages:]
+ +[AMSDefaults useIDCaptureTestImages]
+ +[AMSFinanceActionResponse URLStringForActionDictionary:]
+ +[AMSFinanceActionResponse metricsDestinationForURLString:]
+ +[AMSFinanceDialogResponse metricsDialogIdForResponseDictionary:]
+ +[AMSFinanceDialogResponse metricsDictionary:byReportingGotoURL:containerPresented:]
+ +[AMSHandleDialogResultTask _applyMetricsTimingFromRequest:toEvent:]
+ +[AMSPaymentSheetTask _biometricRetryLimitForBagValue:]
+ +[AMSPurchaseRequestEncoder _reportCallerSuppliedContentTypeIfNeeded:]
+ +[AMSPurchaseTask _applyCommonPurchaseIdentityToEvent:info:]
+ +[AMSPurchaseTask _recordEngagementSignalEventWithInfo:bag:eventType:outcome:logKey:]
+ +[AMSPurchaseTask(AppleMediaServices_Project) _engagementIncomingDecisionForEnqueueError:hasEngagementRequest:canHandleEngagementRequest:]
+ +[AMSSecureThreeDomainInterruptionRequestHandler jsonBodyByInjectingSessionId:intoBody:]
+ +[AMSStreamHTTPArchiveEntryController _discardTemporaryFileURL:stream:]
+ -[AMSCookieService _acquireDaemonConnection]
+ -[AMSEngagement _enqueueIntoServicesAnalyticsKitIfNeeded:]
+ -[AMSEngagement initForMetricsWithBag:]
+ -[AMSEngagement initWithBag:servicesAnalyticsKitBridge:]
+ -[AMSEngagement servicesAnalyticsKitBridge]
+ -[AMSFinanceResponse _metricsOutcomeForGotoActionDictionary:]
+ -[AMSFinanceResponse _metricsOutcomeForNormalDialog]
+ -[AMSMetrics isBuyFlowRedirectToSAKEnabled]
+ -[AMSMetricsEvent isEngagementEvent]
+ -[AMSMetricsLoadURLContext buyFlowRedirectToSAKEnabled]
+ -[AMSMetricsLoadURLContext setBuyFlowRedirectToSAKEnabled:]
+ -[AMSMetricsLoadURLContext webContainerEndTime]
+ -[AMSMetricsLoadURLEvent setWebContainerEncounterEndTime:]
+ -[AMSMetricsLoadURLEvent webContainerEncounterEndTime]
+ -[AMSPaymentSheetPerformanceMetrics _enqueuePageRenderEvent:sampled:samplePromise:]
+ -[AMSPaymentSheetPerformanceMetrics _resolveSamplingForEvent:samplePercentage:sessionDuration:samplePromise:]
+ -[AMSPaymentSheetPerformanceMetrics initialInterfaceOrientation]
+ -[AMSPaymentSheetPerformanceMetrics logKey]
+ -[AMSPaymentSheetPerformanceMetrics primaryDataFetchStartTime]
+ -[AMSPaymentSheetPerformanceMetrics recordInterfaceOrientation:]
+ -[AMSPaymentSheetPerformanceMetrics setLogKey:]
+ -[AMSPaymentSheetPerformanceMetrics setPrimaryDataFetchStartTime:]
+ -[AMSPaymentSheetPerformanceMetrics setUserConfirmationTime:]
+ -[AMSPaymentSheetPerformanceMetrics terminalInterfaceOrientation]
+ -[AMSPaymentSheetPerformanceMetrics userConfirmationTime]
+ -[AMSPaymentSheetRequest physicalButtonConfirmationTitle]
+ -[AMSPaymentSheetRequest setPhysicalButtonConfirmationTitle:]
+ -[AMSPaymentSheetResult renderingFramework]
+ -[AMSPaymentSheetResult setRenderingFramework:]
+ -[AMSPaymentSheetTask _applyBiometricRetryLimit:toPaymentRequest:]
+ -[AMSPaymentSheetTask _errorByAdoptingRenderingFrameworkFromRemoteError:]
+ -[AMSPaymentSheetTask _errorByAttachingRenderingFrameworkIfNeeded:]
+ -[AMSPaymentSheetTask _isRunningInPaymentViewService]
+ -[AMSPaymentSheetTask _recordEnterPasswordCancelled]
+ -[AMSPaymentSheetTask _recordEnterPasswordPressed]
+ -[AMSPaymentSheetTask _resetRenderingFrameworkTelemetry]
+ -[AMSPaymentSheetTask _workflowAuthorizationDidFinishWithResult:]
+ -[AMSPaymentSheetTask paymentSheet:didUpdateDisplayState:]
+ -[AMSPaymentSheetTask paymentSheetDidConfirmUserIntent:]
+ -[AMSPaymentSheetTask paymentSheetDidFinishPresenting:]
+ -[AMSPaymentSheetTask paymentSheetDidReportBiometricEvaluationStarted:]
+ -[AMSPaymentSheetTask workflowSignposter]
+ -[AMSPurchaseInfo renderingFramework]
+ -[AMSPurchaseInfo setRenderingFramework:]
+ -[AMSPurchaseInfo setWorkflowSignposter:]
+ -[AMSPurchaseInfo workflowSignposter]
+ -[AMSSecureThreeDomainInterruptionTask _customDataIncludingMetricsTopic]
+ -[AMSSubscriptionInviteTask _presentInterruptionWithOriginalTransactionId:]
+ -[AMSSubscriptionInviteTask _present]
+ -[AMSSystemAlertDialogTask _beginMetricsTimingOnRequestWithInitiationTime:]
+ -[AMSSystemAlertDialogTask _clearMetricsTimingValueForKey:]
+ -[AMSSystemAlertDialogTask _setMetricsTimingValue:forKey:]
+ -[AMSSystemAlertDialogTask _updateMetricsTimingResetting:usingBlock:]
+ -[AMSURLMetricsLoadURLHandler _buyFlowRedirectToSAKEnabledForMetrics:]
+ -[AMSURLMetricsLoadURLHandler _enqueueLoadURLEvent:toMetrics:forContext:]
+ -[AMSURLSession _recordHTTPArchiveForTaskInfo:]
+ -[AMSURLTaskInfo setWebContainerEndTime:]
+ -[AMSURLTaskInfo webContainerEndTime]
+ -[NSMutableURLRequest(AppleMediaServices) ams_setBodyParameters:encoding:replacingContentType:error:]
+ -[_PaymentSheetState biometricStartTime]
+ -[_PaymentSheetState setBiometricStartTime:]
+ GCC_except_table116
+ GCC_except_table119
+ GCC_except_table59
+ GCC_except_table70
+ GCC_except_table85
+ GCC_except_table88
+ _AMSAuthenticationTimingEventType
+ _AMSBagKeyPaymentSheetBiometricRetryLimit
+ _AMSDialogMetricsTimingKeyInitiationTime
+ _AMSDialogMetricsTimingKeyOnScreenResourcesAppearEndTime
+ _AMSDialogMetricsTimingKeyUserResponseTime
+ _AMSDialogRequestUserInfoKeyMetricsTiming
+ _AMSEngagementSignalEventTypeConcluded
+ _AMSEngagementSignalEventTypeIncoming
+ _AMSErrorUserInfoKeyHTTPStatusCode
+ _AMSMediaTaskPlatformHomeAccessory
+ _AMSMetricsEventKeyAnonymous
+ _AMSMetricsEventKeyClientOnlyEnqueueTimeAccountIdentifier
+ _AMSMetricsEventKeyClientOnlyEventDate
+ _AMSMetricsEventKeyClientOnlyProperties
+ _AMSPaymentSheetDismissalEventType
+ _AMSProcessInfoDefaultClientVersion
+ _AMSPurchaseEventType
+ _AMSPurchaseResponseBodyDialogKey
+ _AMSStringForPaymentSheetRenderingFramework
+ _CFBooleanGetTypeID
+ _NSFileSize
+ _NSFileType
+ _NSFileTypeDirectory
+ _NSFileTypeRegular
+ _OBJC_CLASS_$_AMSBuyFlowLatencySignposter
+ _OBJC_CLASS_$_AMSBuyWorkflowSignposter
+ _OBJC_CLASS_$_AMSHARStore
+ _OBJC_CLASS_$_AMSPageRenderSignposter
+ _OBJC_IVAR_$_AMSCookieService._daemonConnection
+ _OBJC_IVAR_$_AMSEngagement._servicesAnalyticsKitBridge
+ _OBJC_IVAR_$_AMSMetricsLoadURLContext._buyFlowRedirectToSAKEnabled
+ _OBJC_IVAR_$_AMSMetricsLoadURLContext._webContainerEndTime
+ _OBJC_IVAR_$_AMSPaymentSheetPerformanceMetrics._initialInterfaceOrientation
+ _OBJC_IVAR_$_AMSPaymentSheetPerformanceMetrics._interfaceOrientationFrozen
+ _OBJC_IVAR_$_AMSPaymentSheetPerformanceMetrics._interfaceOrientationLock
+ _OBJC_IVAR_$_AMSPaymentSheetPerformanceMetrics._latestInterfaceOrientation
+ _OBJC_IVAR_$_AMSPaymentSheetPerformanceMetrics._logKey
+ _OBJC_IVAR_$_AMSPaymentSheetPerformanceMetrics._primaryDataFetchStartTime
+ _OBJC_IVAR_$_AMSPaymentSheetPerformanceMetrics._terminalInterfaceOrientation
+ _OBJC_IVAR_$_AMSPaymentSheetPerformanceMetrics._userConfirmationTime
+ _OBJC_IVAR_$_AMSPaymentSheetRequest._physicalButtonConfirmationTitle
+ _OBJC_IVAR_$_AMSPaymentSheetResult._renderingFramework
+ _OBJC_IVAR_$_AMSPurchaseInfo._renderingFramework
+ _OBJC_IVAR_$_AMSPurchaseInfo._workflowSignposter
+ _OBJC_IVAR_$_AMSURLTaskInfo._webContainerEndTime
+ _OBJC_IVAR_$__PaymentSheetState._biometricStartTime
+ _OBJC_METACLASS_$_AMSBuyFlowLatencySignposter
+ _OBJC_METACLASS_$_AMSBuyWorkflowSignposter
+ _OBJC_METACLASS_$_AMSHARStore
+ _OBJC_METACLASS_$_AMSPageRenderSignposter
+ _OBJC_METACLASS_$__TtC18AppleMediaServicesP33_FC9CAB294B3A4847C349C10968996CDC26BuyWorkflowSignposterState
+ __CLASS_METHODS_AMSBuyFlowLatencySignposter
+ __CLASS_METHODS_AMSBuyWorkflowSignposter
+ __CLASS_METHODS_AMSHARStore
+ __CLASS_METHODS_AMSPageRenderSignposter
+ __DATA_AMSBuyFlowLatencySignposter
+ __DATA_AMSBuyWorkflowSignposter
+ __DATA_AMSHARStore
+ __DATA_AMSPageRenderSignposter
+ __DATA__TtC18AppleMediaServicesP33_FC9CAB294B3A4847C349C10968996CDC26BuyWorkflowSignposterState
+ __INSTANCE_METHODS_AMSBuyFlowLatencySignposter
+ __INSTANCE_METHODS_AMSBuyWorkflowSignposter
+ __INSTANCE_METHODS_AMSHARStore
+ __INSTANCE_METHODS_AMSPageRenderSignposter
+ __INSTANCE_METHODS__TtC18AppleMediaServicesP33_FC9CAB294B3A4847C349C10968996CDC26BuyWorkflowSignposterState
+ __IVARS_AMSBuyWorkflowSignposter
+ __IVARS__TtC18AppleMediaServicesP33_FC9CAB294B3A4847C349C10968996CDC26BuyWorkflowSignposterState
+ __METACLASS_DATA_AMSBuyFlowLatencySignposter
+ __METACLASS_DATA_AMSBuyWorkflowSignposter
+ __METACLASS_DATA_AMSHARStore
+ __METACLASS_DATA_AMSPageRenderSignposter
+ __METACLASS_DATA__TtC18AppleMediaServicesP33_FC9CAB294B3A4847C349C10968996CDC26BuyWorkflowSignposterState
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDate_$_AMSFormattingUtilities
+ __OBJC_$_CATEGORY_NSDate_$_AMSFormattingUtilities
+ __OBJC_$_CATEGORY_NSHTTPCookie_$_AMSCookieExpiry
+ __OBJC_$_CLASS_METHODS_AMSHandleDialogResultTask
+ __OBJC_$_CLASS_METHODS_NSDate(AMSFormattingUtilities|AppleMediaServices)
+ __OBJC_$_CLASS_METHODS_NSHTTPCookie(AMSCookieExpiry|AppleMediaServices|AMSCookieProperties|NSSecureCoding_Temporary)
+ __OBJC_$_CLASS_METHODS_NSString(AppleMediaServices|AMSFormattingUtilities|AppleMediaServices)
+ __OBJC_$_INSTANCE_METHODS_AMSSubscriptionInviteTask(AppleMediaServices)
+ __OBJC_$_INSTANCE_METHODS_NSHTTPCookie(AMSCookieExpiry|AppleMediaServices|AMSCookieProperties|NSSecureCoding_Temporary)
+ __OBJC_$_INSTANCE_METHODS_NSString(AppleMediaServices|AMSFormattingUtilities|AppleMediaServices)
+ __OBJC_$_PROP_LIST_NSDate_$_AMSFormattingUtilities
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_AMSMetricsProtocol
+ __OBJC_CLASS_PROTOCOLS_$_NSHTTPCookie(AMSCookieExpiry|AppleMediaServices|AMSCookieProperties|NSSecureCoding_Temporary)
+ __PROTOCOL_AMSSubscriptionInvitePresenting
+ __PROTOCOL_INSTANCE_METHODS_AMSSubscriptionInvitePresenting
+ __PROTOCOL_METHOD_TYPES_AMSSubscriptionInvitePresenting
+ __PROTOCOL_PROTOCOLS_AMSSubscriptionInvitePresenting
+ ___109-[AMSPaymentSheetPerformanceMetrics _resolveSamplingForEvent:samplePercentage:sessionDuration:samplePromise:]_block_invoke
+ ___110-[AMSCookieService updateCookiesWithCookiePropertiesToAdd:cookiePropertiesToRemove:forAccount:withCompletion:]_block_invoke_3
+ ___35-[AMSURLSession _retryTask:action:]_block_invoke_4
+ ___38-[AMSMetrics initWithContainerID:bag:]_block_invoke
+ ___44-[AMSPaymentSheetTask _performInProcessTask]_block_invoke_5
+ ___52-[AMSFinanceResponse _metricsOutcomeForNormalDialog]_block_invoke
+ ___58-[AMSSystemAlertDialogTask _setMetricsTimingValue:forKey:]_block_invoke
+ ___59-[AMSSystemAlertDialogTask _clearMetricsTimingValueForKey:]_block_invoke
+ ___70+[AMSPurchaseRequestEncoder _reportCallerSuppliedContentTypeIfNeeded:]_block_invoke
+ ___74-[AMSPurchaseProtocolHandler didCreateTask:fromRequest:completionHandler:]_block_invoke
+ ___75-[AMSSubscriptionInviteTask _presentInterruptionWithOriginalTransactionId:]_block_invoke
+ ___75-[AMSSystemAlertDialogTask _beginMetricsTimingOnRequestWithInitiationTime:]_block_invoke
+ ___block_descriptor_40_e34_v24?0"NSDictionary"8"NSError"16l
+ ___block_descriptor_40_e8_32s_e29_v16?0"NSMutableDictionary"8ls32l8
+ ___block_descriptor_48_e8_32s40bs_e30_v24?0"NSNumber"8"NSError"16ls32l8s40l8
+ ___block_descriptor_49_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_64_e8_32r40r48r_e53_"AMSPromise"24?0"AMSOpenActionResult"8"NSError"16lr32l8r40l8r48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e30_v16?0"NSURLSessionDataTask"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e44_"AMSPromise"16?0"AMSMetricsLoadURLEvent"8ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s_e41_"AMSPromise"24?0"NSArray"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_88_e8_32s40s48s56r64r72r_e44_"AMSPromise"24?0"AMSBoolean"8"NSError"16ls32l8s40l8s48l8r56l8r64l8r72l8
+ ___block_descriptor_88_e8_32s40s48s56r64r72r_e45_"AMSPromise"24?0"AMSOptional"8"NSError"16ls32l8r56l8r64l8s40l8r72l8s48l8
+ ___swift_closure_destructor.14Tm
+ __xpc_type_double
+ __xpc_type_uint64
+ _associated conformance 18AppleMediaServices10HTTPMethodVSHAASQ
+ _associated conformance 18AppleMediaServices10HTTPMethodVs26ExpressibleByStringLiteralAA0gH4TypesADP_s01_ef7BuiltingH0
+ _associated conformance 18AppleMediaServices10HTTPMethodVs26ExpressibleByStringLiteralAAs0ef23ExtendedGraphemeClusterH0
+ _associated conformance 18AppleMediaServices10HTTPMethodVs33ExpressibleByUnicodeScalarLiteralAA0ghI4TypesADP_s01_ef7BuiltinghI0
+ _associated conformance 18AppleMediaServices10HTTPMethodVs43ExpressibleByExtendedGraphemeClusterLiteralAA0ghiJ4TypesADP_s01_ef7BuiltinghiJ0
+ _associated conformance 18AppleMediaServices10HTTPMethodVs43ExpressibleByExtendedGraphemeClusterLiteralAAs0ef13UnicodeScalarJ0
+ _associated conformance 18AppleMediaServices10HeaderNameVSHAASQ
+ _associated conformance 18AppleMediaServices10HeaderNameVs26ExpressibleByStringLiteralAA0hI4TypesADP_s01_fg7BuiltinhI0
+ _associated conformance 18AppleMediaServices10HeaderNameVs26ExpressibleByStringLiteralAAs0fg23ExtendedGraphemeClusterI0
+ _associated conformance 18AppleMediaServices10HeaderNameVs33ExpressibleByUnicodeScalarLiteralAA0hiJ4TypesADP_s01_fg7BuiltinhiJ0
+ _associated conformance 18AppleMediaServices10HeaderNameVs43ExpressibleByExtendedGraphemeClusterLiteralAA0hijK4TypesADP_s01_fg7BuiltinhijK0
+ _associated conformance 18AppleMediaServices10HeaderNameVs43ExpressibleByExtendedGraphemeClusterLiteralAAs0fg13UnicodeScalarK0
+ _associated conformance 18AppleMediaServices12HARStoreCoreO4KindOSHAASQ
+ _associated conformance 18AppleMediaServices19BuyWorkflowIntervalOSHAASQ
+ _associated conformance 18AppleMediaServices19BuyWorkflowIntervalOs12CaseIterableAA8AllCasessADP_Sl
+ _associated conformance 18AppleMediaServices19BuyWorkflowSignpostOSHAASQ
+ _associated conformance 18AppleMediaServices19BuyWorkflowSignpostOs12CaseIterableAA8AllCasessADP_Sl
+ _associated conformance 18AppleMediaServices22PageRenderSignpostNameOSHAASQ
+ _associated conformance 18AppleMediaServices22PageRenderSignpostNameOs12CaseIterableAA8AllCasessADP_Sl
+ _associated conformance 18AppleMediaServices26BuyFlowLatencySignpostNameOSHAASQ
+ _associated conformance 18AppleMediaServices26BuyFlowLatencySignpostNameOs12CaseIterableAA8AllCasessADP_Sl
+ _associated conformance So19NSFileAttributeTypeaSHSCSQ
+ _associated conformance So19NSFileAttributeTypeas20_SwiftNewtypeWrapperSCSY
+ _associated conformance So19NSFileAttributeTypeas20_SwiftNewtypeWrapperSCs35_HasCustomAnyHashableRepresentation
+ _flat unique So31AMSSubscriptionInvitePresenting_p
+ _getSPKSubscriptionInviteInterruptionClass
+ _get_enum_tag_for_layout_string So36AMSMetricsServicesAnalyticsKitBridgeC010AppleMediaB0E5ErrorO
+ _keypath_get_selector_presenter
+ _mach_continuous_time
+ _mach_timebase_info
+ _os_unfair_recursive_lock_lock
+ _symbolic $s18AppleMediaServices0C25AnalyticsKitRoutableEventP
+ _symbolic $s18AppleMediaServices28SubscriptionInvitePresentingP
+ _symbolic SDy__________G 18AppleMediaServices19BuyWorkflowIntervalO 2os010OSSignpostF5StateC
+ _symbolic SS7keyType_SS11descriptionSi9errorCodet
+ _symbolic SaySJG
+ _symbolic Say_____G 18AppleMediaServices19BuyWorkflowIntervalO
+ _symbolic Say_____G 18AppleMediaServices19BuyWorkflowSignpostO
+ _symbolic Say_____G 18AppleMediaServices22PageRenderSignpostNameO
+ _symbolic Say_____G 18AppleMediaServices26BuyFlowLatencySignpostNameO
+ _symbolic So15AMSDialogResultCSgSo7NSErrorCSgIeyByy_
+ _symbolic So15AMSDialogResultCSg______pSgIeggg_ s5ErrorP
+ _symbolic So19AMSEngagementResultCSgSo7NSErrorCSgIeyByy_
+ _symbolic So19AMSEngagementResultCSg______pSgIeggg_ s5ErrorP
+ _symbolic So21AMSAuthenticateResultCSgSo7NSErrorCSgIeyByy_
+ _symbolic So21AMSAuthenticateResultCSg______pSgIeggg_ s5ErrorP
+ _symbolic So24AMSBuyWorkflowSignposterCSg
+ _symbolic _____ 18AppleMediaServices10HTTPMethodV
+ _symbolic _____ 18AppleMediaServices10HeaderNameV
+ _symbolic _____ 18AppleMediaServices12HARStoreCoreO
+ _symbolic _____ 18AppleMediaServices12HARStoreCoreO14FileNamePrefixV
+ _symbolic _____ 18AppleMediaServices12HARStoreCoreO4KindO
+ _symbolic _____ 18AppleMediaServices12HARStoreCoreO5EntryV
+ _symbolic _____ 18AppleMediaServices12HARStoreCoreO9SizeLimitV
+ _symbolic _____ 18AppleMediaServices18PageRenderSignpostO
+ _symbolic _____ 18AppleMediaServices19BuyWorkflowIntervalO
+ _symbolic _____ 18AppleMediaServices19BuyWorkflowSignpostO
+ _symbolic _____ 18AppleMediaServices22BuyFlowLatencySignpostV
+ _symbolic _____ 18AppleMediaServices22PageRenderSignpostNameO
+ _symbolic _____ 18AppleMediaServices26BuyFlowLatencySignpostNameO
+ _symbolic _____ 18AppleMediaServices26BuyWorkflowSignposterState33_FC9CAB294B3A4847C349C10968996CDCLLC
+ _symbolic _____ So19NSFileAttributeTypea
+ _symbolic _____ So36AMSMetricsServicesAnalyticsKitBridgeC010AppleMediaB0E15EngagementEventV
+ _symbolic _____ So36AMSMetricsServicesAnalyticsKitBridgeC010AppleMediaB0E22EngagementEventMatcherV
+ _symbolic ______SSt 10Foundation4DateV
+ _symbolic ______Sd2att 18AppleMediaServices22PageRenderSignpostNameO
+ _symbolic ______Sd4fromSd2tot 18AppleMediaServices22PageRenderSignpostNameO
+ _symbolic ______p 18AppleMediaServices28SubscriptionInvitePresentingP
+ _symbolic ______p 20ServicesAnalyticsKit7MetricsV5EventV10FieldValueP
+ _symbolic _____ySDy__________GG 15Synchronization5MutexVAARi_zrlE 18AppleMediaServices19BuyWorkflowIntervalO 2os010OSSignpostH5StateC
+ _symbolic _____ySJG s23_ContiguousArrayStorageC
+ _symbolic _____ySS_______ptG s23_ContiguousArrayStorageC 20ServicesAnalyticsKit7MetricsV5EventV10FieldValueP
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 18AppleMediaServices12HARStoreCoreO5EntryV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 18AppleMediaServices18PageRenderSignpostO
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 18AppleMediaServices22BuyFlowLatencySignpostV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC So36AMSMetricsServicesAnalyticsKitBridgeC010AppleMediaE0E15EngagementEventV
+ _symbolic _____y______SdtG s23_ContiguousArrayStorageC 18AppleMediaServices26BuyFlowLatencySignpostNameO
+ _symbolic _____y__________G s17_NativeDictionaryV 18AppleMediaServices19BuyWorkflowIntervalO 2os010OSSignpostH5StateC
+ _symbolic _____y_____y_____GG 15Synchronization5MutexVAARi_zrlE 18AppleMediaServices8OnceGateV AD19BuyWorkflowSignpostO
+ _symbolic ypXp
+ _type_layout_string 18AppleMediaServices10HTTPMethodV
+ _type_layout_string 18AppleMediaServices10HeaderNameV
+ _type_layout_string 18AppleMediaServices12HARStoreCoreO14FileNamePrefixV
+ _type_layout_string 18AppleMediaServices12HARStoreCoreO9SizeLimitV
+ _type_layout_string 18AppleMediaServices22BuyFlowLatencySignpostV
+ _type_layout_string So36AMSMetricsServicesAnalyticsKitBridgeC010AppleMediaB0E15EngagementEventV
+ _type_layout_string So36AMSMetricsServicesAnalyticsKitBridgeC010AppleMediaB0E22EngagementEventMatcherV
+ _unlink
+ _xpc_connection_copy_entitlement_value
+ _xpc_double_get_value
+ _xpc_uint64_get_value
- +[AMSHTTPArchive _timeIntervalFromFilename:]
- +[AMSStreamHTTPArchiveEntryController _createNewFileNameWithExtension:]
- +[AMSStreamHTTPArchiveEntryController _createNewFileWithFileName:outputDirectory:error:]
- -[AMSMetrics initWithContainerID:bag:bagConfigurationStore:]
- -[AMSMetrics initWithContainerID:bag:flushTaskClass:]
- -[AMSMetricsEvent engagementEvent]
- -[AMSSubscriptionInviteTask _presentInterruption]
- -[AMSURLMetricsLoadURLHandler _enqueueLoadURLEvent:forContext:]
- GCC_except_table108
- GCC_except_table110
- GCC_except_table127
- GCC_except_table68
- GCC_except_table72
- GCC_except_table87
- _OBJC_CLASS_$_NSScanner
- _OUTLINED_FUNCTION_425
- _OUTLINED_FUNCTION_426
- _OUTLINED_FUNCTION_427
- _OUTLINED_FUNCTION_428
- __OBJC_$_CATEGORY_NSDate_$_AppleMediaServices
- __OBJC_$_CATEGORY_NSHTTPCookie_$_AppleMediaServices
- __OBJC_$_CLASS_METHODS_NSDate(AppleMediaServices|AMSFormattingUtilities)
- __OBJC_$_CLASS_METHODS_NSHTTPCookie(AppleMediaServices|AMSCookieProperties|NSSecureCoding_Temporary|AMSCookieExpiry)
- __OBJC_$_CLASS_METHODS_NSString(AppleMediaServices|AppleMediaServices|AMSFormattingUtilities)
- __OBJC_$_INSTANCE_METHODS_AMSSubscriptionInviteTask
- __OBJC_$_INSTANCE_METHODS_NSDate(AppleMediaServices|AMSFormattingUtilities)
- __OBJC_$_INSTANCE_METHODS_NSHTTPCookie(AppleMediaServices|AMSCookieProperties|NSSecureCoding_Temporary|AMSCookieExpiry)
- __OBJC_$_INSTANCE_METHODS_NSString(AppleMediaServices|AppleMediaServices|AMSFormattingUtilities)
- __OBJC_$_PROP_LIST_AMSSubscriptionInviteTask
- __OBJC_$_PROP_LIST_NSHTTPCookie_$_AppleMediaServices
- __OBJC_CLASS_PROTOCOLS_$_NSHTTPCookie(AppleMediaServices|AMSCookieProperties|NSSecureCoding_Temporary|AMSCookieExpiry)
- ___49-[AMSSubscriptionInviteTask _presentInterruption]_block_invoke
- ___53-[AMSMetrics initWithContainerID:bag:flushTaskClass:]_block_invoke
- ___79+[AMSDevice(Offers) postAllDeviceOfferFollowUpsForAccount:priority:bag:logKey:]_block_invoke
- ___79+[AMSDevice(Offers) postAllDeviceOfferFollowUpsForAccount:priority:bag:logKey:]_block_invoke_2
- ___block_descriptor_32_e24_B16?0"AMSDeviceOffer"8l
- ___block_descriptor_40_e8_32s_e41_v24?0"AMSEngagementResult"8"NSError"16ls32l8
- ___block_descriptor_56_e8_32r40r_e53_"AMSPromise"24?0"AMSOpenActionResult"8"NSError"16lr32l8r40l8
- ___block_descriptor_56_e8_32s40s48s_e30_v16?0"NSURLSessionDataTask"8ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e41_"AMSPromise"24?0"NSArray"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_56_e8_32s40s48s_e44_"AMSPromise"16?0"AMSMetricsLoadURLEvent"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48r56r_e45_"AMSPromise"24?0"AMSOptional"8"NSError"16ls32l8r48l8r56l8s40l8
- ___block_descriptor_80_e8_32s40s48s56r64r_e44_"AMSPromise"24?0"AMSBoolean"8"NSError"16ls32l8s40l8s48l8r56l8r64l8
CStrings:
+ " HAR files, the first with: "
+ "%{public}@3DS JSON body is not a top-level object; not updating body"
+ "%{public}@3DS metrics topic: %{public}@ (from %{public}@)"
+ "%{public}@: Failed to capture auto bug report for a caller-supplied Content-Type. error = %{public}@"
+ "%{public}@: Failed to write the entry separator to the har logging stream."
+ "%{public}@: Skipping an entry that couldn't be decompressed."
+ "%{public}@Applying biometric retry limit %{public}@"
+ "%{public}@Collecting buy flow pageRender event without sampling"
+ "%{public}@Enqueuing paymentSheetDismissal event. purchaseId: %{public}@"
+ "%{public}@Failed to archive the client info: %{public}@"
+ "%{public}@Failed to serialize 3DS JSON body: %{public}@"
+ "%{public}@Failed to undo the request body's Content-Encoding: %{public}@"
+ "%{public}@Ignoring Content-Type in AMSPurchase.additionalHeaders. client = %{public}@ | contentType = %{public}@"
+ "%{public}@Recording %{public}@ engagement signal event. outcome: %{public}@"
+ "%{public}@ServicesPaymentKit does not accept appAdamId or appBundleId, dropping them"
+ "%{public}@SubsForGroups feature disabled (originalTransactionId=%{public}@, sceneIdentifier=%{public}@)"
+ "%{public}@Warning: system dialog dismissed in under %.0f ms — likely never rendered. Check the system notification server's logs (e.g. PineBoard on tvOS) for CFUserNotification authorization failures or other rejections."
+ "%{public}@paymentSheet: %{public}@ | interfaceOrientation: %ld"
+ "%{signpost.description:begin_time}lluid=%llu, instant=%f"
+ "%{signpost.description:end_time}lluid=%llu, instant=%f"
+ "%{signpost.description:event_time}lluid=%llu, instant=%f"
+ "<%@ %@ event>"
+ "A key of the event payload is not a string"
+ "AMSDevice+Offers: [%{public}@] Skipping device offer follow up: %{public}@. Device offer follow ups are server driven."
+ "AMSDevice+Offers: [%{public}@] Skipping device offer follow ups for account: %{public}@. Device offer follow ups are server driven."
+ "AMSDialogRequestUserInfoKeyMetricsTiming"
+ "AMSHARMaxDirectorySizeMB"
+ "AMSHTTPStatusCode"
+ "AMSPurchase additionalHeaders Content-Type"
+ "AMSRenderingFramework"
+ "AMSUIPaymentViewService_tvOS"
+ "AMSUseIDCaptureTestImages"
+ "AppleMediaServices.BuyWorkflowSignposterState"
+ "AppleMediaServices_BridgedInterface.BuyWorkflowSignposter"
+ "BuyRequest"
+ "CUIBuyFlowLatency"
+ "CompanionServices"
+ "Failed to remove "
+ "PassKit"
+ "Request has neither originalTransactionId nor subscriptionInfo"
+ "ServicesPaymentKit does not accept originalTransactionId"
+ "SheetFinish"
+ "Subscription invite failed"
+ "The payment sheet could not be shown because AssistiveTouch or Switch Control confirmation is unavailable."
+ "The payment sheet was not shown because the device confirms with AssistiveTouch or Switch Control, which is turned off"
+ "_isAMSEngagementEvent"
+ "abandoned=1"
+ "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._-"
+ "authenticationChallengeRenderTime"
+ "authenticationEndTime"
+ "authenticationPresented"
+ "authenticationResponded"
+ "authenticationStartTime"
+ "authorizationFailed"
+ "biometricRetryLimit"
+ "biometricsOptInFinished"
+ "biometricsOptInStarted"
+ "buy params"
+ "buyStarted"
+ "com.apple.AppleMediaServices.AMSCookieService.updateCompletion"
+ "com.apple.AppleMediaServices.AMSEngagement"
+ "contentType"
+ "customData"
+ "dialogInitiationTime"
+ "dialogOnScreenResourcesAppearEndTime"
+ "dialogPresented"
+ "dialogResponded"
+ "dialogUserResponseTime"
+ "engagementConcluded"
+ "engagementIncoming"
+ "engagementPresented"
+ "engagementResponded"
+ "expressCheckoutPresented"
+ "expressCheckoutResponded"
+ "externalURLOpened"
+ "failed"
+ "flow=%{public}ld"
+ "hadDialog"
+ "homeAccessory"
+ "initiationTime"
+ "kPhysicalButtonTitle"
+ "kRenderingFramework"
+ "metrics/%@"
+ "modelConstruction"
+ "originatingApp"
+ "originatingAppVersion"
+ "payment-sheet-biometric-retry-limit"
+ "paymentDialogOrientationInitial"
+ "paymentDialogOrientationTerminal"
+ "paymentInterruptionPresented"
+ "paymentInterruptionResponded"
+ "paymentSheetUserResponseTime"
+ "physicalButtonConfirmationTitle"
+ "primaryDataFetchStartTime"
+ "primaryDataParse"
+ "primaryDataResponse"
+ "purchaseCanceled"
+ "purchaseFailed"
+ "purchaseSucceeded"
+ "radar"
+ "rdar://190727138"
+ "renderingFramework"
+ "resourceRequest"
+ "sheetAuthorized"
+ "statusCode=%{public}ld errorDomain=%{public}@ errorCode=%{public}ld"
+ "userConfirmationTime"
+ "webContainerEncounterEndTime"
+ "xp_amp_payments"
- "!\xb3"
- "%@_%lld_streamwrite%@"
- "%{public}@Enqueuing paymentSheetDismissal event. userResponseTime: %{public}@, purchaseId: %{public}@"
- "%{public}@SubsForGroups feature disabled (subscriptionFamilyId=%{public}@, sceneIdentifier=%{public}@)"
- "%{public}@Warning: system dialog dismissed in under 50 ms — likely never rendered. Check PineBoard logs for CFUserNotification authorization failures or other rejections."
- ".temp"
- "AMSDevice+Offers: [%{public}@] Failed to post device offer for account with <nil> DSID"
- "AMSDevice+Offers: [%{public}@] Failed to post follow up with identifier: %{public}@, error: %{public}@"
- "AMSDevice+Offers: [%{public}@] Found %{public}@ AppleMusic offers, posting follow-up"
- "AMSDevice+Offers: [%{public}@] Found %{public}@ iCloud offers, posting follow-up"
- "AMSDevice+Offers: [%{public}@] No offers were found for which to post follow-up(s)"
- "AMSDevice+Offers: [%{public}@] Not posting follow up with identifier %{public}@: item could not be built"
- "AMSDevice+Offers: [%{public}@] Offers count - Total: %{public}@, iCloud: %{public}@, Apple Music: %{public}@"
- "AMSDevice+Offers: [%{public}@] Posted follow up with identifier: %{public}@"
- "AMSDevice+Offers: [%{public}@] Posting all follow ups for account: %{public}@"
- "AMSDevice+Offers: [%{public}@] Posting unified followup for iCloud and Apple Music"
- "B16@?0@\"AMSDeviceOffer\"8"
- "Request has no subscriptionFamilyId"
- "_streamwrite.har"
```
