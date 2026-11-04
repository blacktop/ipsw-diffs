## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`

```diff

-10.1.18.2.1
-  __TEXT.__text: 0x87be80
+10.2.12.0.0
+  __TEXT.__text: 0x89244c
   __TEXT.__delay_helper: 0x114
   __TEXT.__lazy_helpers: 0x42f4
-  __TEXT.__objc_methlist: 0x25914
-  __TEXT.__const: 0x645d0
-  __TEXT.__dlopen_cstrs: 0x990
-  __TEXT.__cstring: 0x313e6
-  __TEXT.__swift5_typeref: 0x9219
-  __TEXT.__swift5_reflstr: 0x69ce
-  __TEXT.__swift5_assocty: 0x1398
-  __TEXT.__constg_swiftt: 0x7cdc
-  __TEXT.__swift5_builtin: 0x53c
-  __TEXT.__swift5_fieldmd: 0x7f74
-  __TEXT.__swift5_proto: 0x17f4
-  __TEXT.__swift5_types: 0x920
-  __TEXT.__swift_as_entry: 0xb10
-  __TEXT.__swift_as_ret: 0xddc
-  __TEXT.__swift_as_cont: 0x1b1c
-  __TEXT.__swift5_capture: 0x7970
+  __TEXT.__objc_methlist: 0x26484
+  __TEXT.__const: 0x64e20
+  __TEXT.__dlopen_cstrs: 0xa54
+  __TEXT.__cstring: 0x320cf
+  __TEXT.__swift5_typeref: 0x9473
+  __TEXT.__swift5_reflstr: 0x6cce
+  __TEXT.__swift5_assocty: 0x13b0
+  __TEXT.__constg_swiftt: 0x7f18
+  __TEXT.__swift5_builtin: 0x550
+  __TEXT.__swift5_fieldmd: 0x8258
+  __TEXT.__swift5_proto: 0x1848
+  __TEXT.__swift5_types: 0x958
+  __TEXT.__swift_as_entry: 0xb34
+  __TEXT.__swift_as_ret: 0xe10
+  __TEXT.__swift_as_cont: 0x1b94
+  __TEXT.__swift5_capture: 0x7cdc
   __TEXT.__swift5_mpenum: 0xd4
-  __TEXT.__swift5_protos: 0x15c
-  __TEXT.__oslogstring: 0x38892
-  __TEXT.__gcc_except_tab: 0x54c4
+  __TEXT.__swift5_protos: 0x160
+  __TEXT.__oslogstring: 0x3934a
+  __TEXT.__gcc_except_tab: 0x5638
   __TEXT.__ustring: 0x204
-  __TEXT.__unwind_info: 0x1af30
-  __TEXT.__eh_frame: 0x205ac
+  __TEXT.__unwind_info: 0x1ba48
+  __TEXT.__eh_frame: 0x20c2c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xd968
-  __DATA_CONST.__objc_classlist: 0x16e0
+  __DATA_CONST.__const: 0xdbd8
+  __DATA_CONST.__objc_classlist: 0x1730
   __DATA_CONST.__objc_catlist: 0xf0
-  __DATA_CONST.__objc_protolist: 0x510
+  __DATA_CONST.__objc_protolist: 0x518
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10868
-  __DATA_CONST.__objc_protorefs: 0x290
-  __DATA_CONST.__objc_superrefs: 0xd28
+  __DATA_CONST.__objc_selrefs: 0x10d28
+  __DATA_CONST.__objc_protorefs: 0x288
+  __DATA_CONST.__objc_superrefs: 0xd40
   __DATA_CONST.__objc_arraydata: 0x5f8
-  __DATA_CONST.__got: 0x1b68
-  __AUTH_CONST.__const: 0x3d060
-  __AUTH_CONST.__cfstring: 0x244a0
-  __AUTH_CONST.__objc_const: 0x42550
+  __DATA_CONST.__got: 0x1ba8
+  __AUTH_CONST.__const: 0x3e380
+  __AUTH_CONST.__cfstring: 0x24b20
+  __AUTH_CONST.__objc_const: 0x436f8
   __AUTH_CONST.__lazy_load_got: 0x638
-  __AUTH_CONST.__objc_intobj: 0xd20
+  __AUTH_CONST.__objc_intobj: 0xd38
   __AUTH_CONST.__objc_arrayobj: 0x180
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH_CONST.__auth_got: 0x27d8
-  __AUTH.__objc_data: 0xb530
-  __AUTH.__data: 0x35e0
-  __DATA.__objc_ivar: 0x1a74
-  __DATA.__data: 0x93f4
-  __DATA.__common: 0xb6c
-  __DATA_DIRTY.__objc_ivar: 0x72c
-  __DATA_DIRTY.__objc_data: 0x5db8
-  __DATA_DIRTY.__data: 0x2fd0
-  __DATA_DIRTY.__bss: 0x62e0
-  __DATA_DIRTY.__common: 0xa8
+  __AUTH_CONST.__auth_got: 0x2830
+  __AUTH.__objc_data: 0xb990
+  __AUTH.__data: 0x37a0
+  __DATA.__objc_ivar: 0x1b0c
+  __DATA.__data: 0x9614
+  __DATA.__common: 0xb74
+  __DATA_DIRTY.__objc_ivar: 0x758
+  __DATA_DIRTY.__objc_data: 0x5d68
+  __DATA_DIRTY.__data: 0x2de0
+  __DATA_DIRTY.__bss: 0x6340
+  __DATA_DIRTY.__common: 0xa0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 36209
-  Symbols:   27454
-  CStrings:  9886
+  Functions: 36836
+  Symbols:   27850
+  CStrings:  10022
 
Symbols:
+ +[AMSHTTPArchive _flushPendingEntriesWithTracker:archiveService:timeout:]
+ +[AMSHTTPArchive _recordTaskInfo:responseData:route:tracker:]
+ +[AMSHTTPArchive _sharedRecordingTracker]
+ +[AMSHTTPArchive flushPendingEntriesPromiseWithTimeout:]
+ +[AMSHTTPArchiveService _sharedConnectionQueue]
+ +[AMSHTTPArchiveService _sharedService]
+ +[AMSMetricsLoadURLEvent _isBuyFlowEventForContext:metricsDictionary:]
+ +[AMSPaymentSheetTask _spkPaymentSheetDisabledBagKey]
+ +[AMSPurchase _identifierFromUUID:]
+ +[AMSRequestDecorator sharedDecorator]
+ +[AMSSecureThreeDomainInterruptionRequestHandler bodyByInjectingSessionId:intoRequest:]
+ +[AMSSecureThreeDomainInterruptionRequestHandler formURLEncodedQueryFromItems:]
+ +[AMSSecureThreeDomainInterruptionRequestHandler percentEncodedFormComponent:]
+ +[AMSSecureThreeDomainInterruptionRequestHandler updateBodyOnAction:withSessionId:originatingTaskInfo:]
+ +[AMSStreamHTTPArchiveEntryController _maxBufferSizeForMemoryPressureStatus:]
+ +[AMSStreamHTTPArchiveEntryController ams_flushAllEntriesToDisk]
+ -[AMSAccountCachedServerDataFields ageSignalConflict]
+ -[AMSAccountCachedServerDataFields setAgeSignalConflict:]
+ -[AMSAuthenticateOptions purchaseIdentifier]
+ -[AMSAuthenticateOptions setPurchaseIdentifier:]
+ -[AMSFinanceResponse _actionDecisionForDictionary:]
+ -[AMSFinanceResponse metricsOutcome]
+ -[AMSHARRecordingTracker .cxx_destruct]
+ -[AMSHARRecordingTracker hasRecorded]
+ -[AMSHARRecordingTracker init]
+ -[AMSHARRecordingTracker notifyWhenIdleOnQueue:block:]
+ -[AMSHARRecordingTracker trackedRecordingBlock:]
+ -[AMSHTTPArchiveService flushPromise]
+ -[AMSHTTPArchiveService initWithRecordingConnection:]
+ -[AMSHTTPArchiveService lostConnection]
+ -[AMSHTTPArchiveService setLostConnection:]
+ -[AMSMetricsLoadURLContext disableLoadURLMetrics]
+ -[AMSMetricsLoadURLContext loadURLOverlay]
+ -[AMSMetricsLoadURLContext logUUID]
+ -[AMSMetricsLoadURLContext outcome]
+ -[AMSMetricsLoadURLContext purchaseId]
+ -[AMSMetricsLoadURLContext purchaseMetricsOverlay]
+ -[AMSMetricsLoadURLContext setOutcome:]
+ -[AMSMetricsLoadURLEvent outcome]
+ -[AMSMetricsLoadURLEvent setOutcome:]
+ -[AMSPaymentRequest ams_tagRequestWithPurchaseIdentifier:]
+ -[AMSPaymentRequest purchaseIdentifier]
+ -[AMSPaymentRequest setPurchaseIdentifier:]
+ -[AMSPaymentSheetPerformanceMetrics _baseEventWithType:]
+ -[AMSPaymentSheetPerformanceMetrics _finalizeEvent:withOverlay:]
+ -[AMSPaymentSheetPerformanceMetrics enqueueDismissalMetricsEventWithOverlay:]
+ -[AMSPaymentSheetPerformanceMetrics pageRenderSamplePromise]
+ -[AMSPaymentSheetPerformanceMetrics purchaseUUID]
+ -[AMSPaymentSheetPerformanceMetrics recordUserResponseTimeIfNeeded]
+ -[AMSPaymentSheetPerformanceMetrics setPageRenderSamplePromise:]
+ -[AMSPaymentSheetPerformanceMetrics setPurchaseUUID:]
+ -[AMSPaymentSheetPerformanceMetrics setUserResponseTime:]
+ -[AMSPaymentSheetPerformanceMetrics userResponseTime]
+ -[AMSPaymentSheetRequest purchaseIdentifier]
+ -[AMSPaymentSheetRequest setPurchaseIdentifier:]
+ -[AMSPaymentSheetRequest(PassKit) _requestForExpandableInfoURL:requestType:bag:session:error:]
+ -[AMSPaymentSheetResult applePayClassicInvoked]
+ -[AMSPaymentSheetResult setApplePayClassicInvoked:]
+ -[AMSPaymentSheetTask _authenticationTimingMethodForBiometricsType:]
+ -[AMSPaymentSheetTask _isSPKPaymentSheetFeatureFlagEnabled]
+ -[AMSPaymentSheetTask _isUserInitiatedCancellationType:]
+ -[AMSPaymentSheetTask _recordAuthenticationTimingEventWithMethod:startTime:endTime:challengeRenderTime:success:]
+ -[AMSPaymentSheetTask _recordUserResponseTimeIfUserInitiatedCancellation]
+ -[AMSPurchase purchaseUUID]
+ -[AMSPurchase servicesPaymentViewServiceListener]
+ -[AMSPurchase setServicesPaymentViewServiceListener:]
+ -[AMSPurchaseInfo applePayClassicInvoked]
+ -[AMSPurchaseInfo setApplePayClassicInvoked:]
+ -[AMSPurchaseQueueConfiguration excludesServerPayloadFromErrors]
+ -[AMSPurchaseQueueConfiguration setExcludesServerPayloadFromErrors:]
+ -[AMSPurchaseTask _promiseExcludingServerPayload:]
+ -[AMSPurchaseTask endTime]
+ -[AMSPurchaseTask excludesServerPayloadFromErrors]
+ -[AMSPurchaseTask setEndTime:]
+ -[AMSPurchaseTask setExcludesServerPayloadFromErrors:]
+ -[AMSPurchaseTask setStartTime:]
+ -[AMSPurchaseTask startTime]
+ -[AMSRequestDecorator addAbsintheHeadersToRequest:buyParams:bag:shouldUseRemoteSigningIfAvailable:]
+ -[AMSRequestDecorator addAcceptEncodingHeaderToRequest:]
+ -[AMSRequestDecorator addAcceptLanguageHeaderToRequest:]
+ -[AMSRequestDecorator addAnisetteHeadersToRequest:account:type:bag:]
+ -[AMSRequestDecorator addAuthKitHeadersToRequest:]
+ -[AMSRequestDecorator addBiometricsHeadersToRequest:forAccount:options:]
+ -[AMSRequestDecorator addCacheBusterParameterToRequest:preservingQueryEncoding:]
+ -[AMSRequestDecorator addCachePolicyHeaderToRequest:]
+ -[AMSRequestDecorator addClientIdentifierHeaderToRequest:forClient:]
+ -[AMSRequestDecorator addClientVersionsToRequest:forClient:]
+ -[AMSRequestDecorator addConnectionTypeHeaderToRequest:]
+ -[AMSRequestDecorator addCookiesToRequest:forAccount:clientInfo:bag:cleanupGlobalCookies:excludeAccountIdentifierCookies:]
+ -[AMSRequestDecorator addFPDIHeadersToRequest:buyParams:bag:retryCount:fairPlayDeviceIdentity:fpdiNetworkProvider:]
+ -[AMSRequestDecorator addForwardedForHeaderToRequest:]
+ -[AMSRequestDecorator addGSTokenToRequest:forAccount:identifier:]
+ -[AMSRequestDecorator addGUIDHeaderToRequest:matchingURL:bag:]
+ -[AMSRequestDecorator addGUIDParameterToRequest:matchingURL:bag:preservingQueryEncoding:]
+ -[AMSRequestDecorator addGroupDSIDsToRequest:primaryAccount:groupAccounts:]
+ -[AMSRequestDecorator addIdentifierHeadersToRequest:forAccount:]
+ -[AMSRequestDecorator addIssuingProcessHeaderToRequest:]
+ -[AMSRequestDecorator addMMeClientInfoAndDeviceHeadersToRequest:]
+ -[AMSRequestDecorator addMescalHeaderToRequest:type:bag:logKey:]
+ -[AMSRequestDecorator addPrimaryiCloudIdentifierHeaderToRequest:]
+ -[AMSRequestDecorator addProductTypeHeaderToRequest:]
+ -[AMSRequestDecorator addRequestingProcessHeaderToRequest:forClient:]
+ -[AMSRequestDecorator addStorefrontHeaderToRequest:forAccount:mediaType:bag:]
+ -[AMSRequestDecorator addTimezoneOffsetHeaderToRequest:]
+ -[AMSRequestDecorator addTreatmentHeadersToRequest:forTreatmentNamespace:bag:canonicalAccountIdentifierProvider:reportsErrorsToMetrics:]
+ -[AMSRequestDecorator addUserAgentHeaderToRequest:forClient:]
+ -[AMSRequestDecorator compressBodyInRequest:logUUID:loggingFor:]
+ -[AMSRequestDecorator disableCookieHandlingInRequest:]
+ -[AMSRequestDecorator encodeBodyParametersInRequest:parameters:encoding:error:]
+ -[AMSRequestDecorator sortQueryParametersInRequest:]
+ -[AMSSecureThreeDomainInterruptionTask .cxx_destruct]
+ -[AMSSecureThreeDomainInterruptionTask _makeInterruptionWithSceneIdentifier:]
+ -[AMSSecureThreeDomainInterruptionTask _presentInterruption:]
+ -[AMSSecureThreeDomainInterruptionTask _presentInterruptionWithSceneIdentifier:]
+ -[AMSSecureThreeDomainInterruptionTask _resolvePresentationTargetAndPresent]
+ -[AMSSecureThreeDomainInterruptionTask activeInterruption]
+ -[AMSSecureThreeDomainInterruptionTask challengeResponse]
+ -[AMSSecureThreeDomainInterruptionTask customData]
+ -[AMSSecureThreeDomainInterruptionTask hostAppAuditTokenData]
+ -[AMSSecureThreeDomainInterruptionTask initWithSceneIdentifier:]
+ -[AMSSecureThreeDomainInterruptionTask initWithURLTaskInfo:]
+ -[AMSSecureThreeDomainInterruptionTask perform]
+ -[AMSSecureThreeDomainInterruptionTask sceneIdentifier]
+ -[AMSSecureThreeDomainInterruptionTask setActiveInterruption:]
+ -[AMSSecureThreeDomainInterruptionTask setChallengeResponse:]
+ -[AMSSecureThreeDomainInterruptionTask setCustomData:]
+ -[AMSSecureThreeDomainInterruptionTask setHostAppAuditTokenData:]
+ -[AMSSecureThreeDomainInterruptionTask setSceneIdentifier:]
+ -[AMSSecureThreeDomainInterruptionTask setUrlTaskInfo:]
+ -[AMSSecureThreeDomainInterruptionTask urlTaskInfo]
+ -[AMSSubscriptionInviteTask .cxx_destruct]
+ -[AMSSubscriptionInviteTask _hostAppAuditTokenData]
+ -[AMSSubscriptionInviteTask _presentInterruption]
+ -[AMSSubscriptionInviteTask bag]
+ -[AMSSubscriptionInviteTask cancel]
+ -[AMSSubscriptionInviteTask initWithRequest:sceneIdentifier:]
+ -[AMSSubscriptionInviteTask initWithSubscriptionInfo:sceneIdentifier:]
+ -[AMSSubscriptionInviteTask interruption]
+ -[AMSSubscriptionInviteTask perform]
+ -[AMSSubscriptionInviteTask request]
+ -[AMSSubscriptionInviteTask sceneIdentifier]
+ -[AMSSubscriptionInviteTask setBag:]
+ -[AMSSubscriptionInviteTask setInterruption:]
+ -[AMSSystemEngagementTask _createRemoteAlertHandle]
+ -[AMSSystemEngagementTask _handleSceneRemoteAlertDeactivation:]
+ -[AMSSystemEngagementTask _isViewServiceProcessAlive]
+ -[AMSSystemEngagementTask _presentationTargetHandle]
+ -[AMSSystemEngagementTask _remoteAlertHandleNeedingRecreation:]
+ -[AMSSystemEngagementTask _remoteAlertTornDown]
+ -[AMSSystemEngagementTask remoteAlertActivationPending]
+ -[AMSSystemEngagementTask remoteAlertHandleNeedsRecreation]
+ -[AMSSystemEngagementTask remoteAlertTaskIdentifier]
+ -[AMSSystemEngagementTask remoteAlertTornDown]
+ -[AMSSystemEngagementTask sceneRemoteAlertEnabled]
+ -[AMSSystemEngagementTask setRemoteAlertActivationPending:]
+ -[AMSSystemEngagementTask setRemoteAlertHandleNeedsRecreation:]
+ -[AMSSystemEngagementTask setRemoteAlertTaskIdentifier:]
+ -[AMSSystemEngagementTask setRemoteAlertTornDown:]
+ -[AMSSystemEngagementTask setSceneRemoteAlertEnabled:]
+ -[AMSSystemEngagementTask setViewServiceProcessIdentifier:]
+ -[AMSSystemEngagementTask viewServiceProcessIdentifier]
+ -[AMSTimedBiometricsSignatureResult .cxx_destruct]
+ -[AMSTimedBiometricsSignatureResult endTime]
+ -[AMSTimedBiometricsSignatureResult setEndTime:]
+ -[AMSTimedBiometricsSignatureResult setSignatureError:]
+ -[AMSTimedBiometricsSignatureResult setSignatureResult:]
+ -[AMSTimedBiometricsSignatureResult signatureError]
+ -[AMSTimedBiometricsSignatureResult signatureResult]
+ -[AMSTreatmentStore metricsReporter]
+ -[AMSTreatmentStore setMetricsReporter:]
+ -[AMSTreatmentStoreMetricsReporter reportTreatmentStoreFailureEvent:]
+ -[AMSURLRequestEncoder _addCookiesToRequest:account:decorator:]
+ -[AMSURLRequestEncoder currentProcess]
+ -[AMSURLRequestEncoder decorator]
+ -[AMSURLRequestEncoder purchaseIdentifier]
+ -[AMSURLRequestEncoder setCurrentProcess:]
+ -[AMSURLRequestEncoder setDecorator:]
+ -[AMSURLRequestEncoder setPurchaseIdentifier:]
+ -[AMSURLRequestProperties purchaseIdentifier]
+ -[AMSURLRequestProperties setPurchaseIdentifier:]
+ -[AMSURLTaskInfo outcome]
+ -[AMSURLTaskInfo setOutcome:]
+ -[NSError(AppleMediaServices_Project) ams_errorByRemovingUserInfoKeys:]
+ -[_PaymentSheetState passwordChallengeRenderTime]
+ -[_PaymentSheetState setPasswordChallengeRenderTime:]
+ GCC_except_table108
+ GCC_except_table127
+ GCC_except_table63
+ GCC_except_table68
+ GCC_except_table72
+ GCC_except_table87
+ _AMSBagKeySPKPaymentSheetMacOSDisabled
+ _AMSBagKeySystemEngagementSceneRemoteAlertEnabled
+ _AMSDefaultsSamplingIdentifierMetricsLogging
+ _AMSErrorByRemovingUserInfoKeys
+ _AMSFinanceDialogMetricsKeyPurchaseId
+ _AMSHashForLog
+ _AMSMetricsOutcomeNone
+ _OBJC_CLASS_$_AMSFinanceSubscriptionInviteResponse
+ _OBJC_CLASS_$_AMSHARRecordingTracker
+ _OBJC_CLASS_$_AMSMetricsServicesAnalyticsKitEnqueueContext
+ _OBJC_CLASS_$_AMSRequestDecorator
+ _OBJC_CLASS_$_AMSSecureThreeDomainInterruptionRequestHandler
+ _OBJC_CLASS_$_AMSSecureThreeDomainInterruptionTask
+ _OBJC_CLASS_$_AMSSubscriptionInviteTask
+ _OBJC_CLASS_$_AMSTimedBiometricsSignatureResult
+ _OBJC_CLASS_$_AMSTreatmentStoreMetricsReporter
+ _OBJC_CLASS_$_AMSUnderlyingErrorTreeBridge
+ _OBJC_CLASS_$_NFReaderSession$lazyGOT$loadHelper_x2$for$_OUTLINED_FUNCTION_81+8
+ _OBJC_CLASS_$_NSMutableCharacterSet
+ _OBJC_CLASS_$_NSPredicate
+ _OBJC_IVAR_$_AMSAccountCachedServerDataFields._ageSignalConflict
+ _OBJC_IVAR_$_AMSAuthenticateOptions._purchaseIdentifier
+ _OBJC_IVAR_$_AMSHARRecordingTracker._group
+ _OBJC_IVAR_$_AMSHARRecordingTracker._hasRecorded
+ _OBJC_IVAR_$_AMSHTTPArchiveService._lostConnection
+ _OBJC_IVAR_$_AMSMetricsLoadURLContext._disableLoadURLMetrics
+ _OBJC_IVAR_$_AMSMetricsLoadURLContext._loadURLOverlay
+ _OBJC_IVAR_$_AMSMetricsLoadURLContext._logUUID
+ _OBJC_IVAR_$_AMSMetricsLoadURLContext._outcome
+ _OBJC_IVAR_$_AMSMetricsLoadURLContext._purchaseId
+ _OBJC_IVAR_$_AMSMetricsLoadURLContext._purchaseMetricsOverlay
+ _OBJC_IVAR_$_AMSPaymentRequest._purchaseIdentifier
+ _OBJC_IVAR_$_AMSPaymentSheetPerformanceMetrics._pageRenderSamplePromise
+ _OBJC_IVAR_$_AMSPaymentSheetPerformanceMetrics._purchaseUUID
+ _OBJC_IVAR_$_AMSPaymentSheetPerformanceMetrics._userResponseTime
+ _OBJC_IVAR_$_AMSPaymentSheetRequest._purchaseIdentifier
+ _OBJC_IVAR_$_AMSPaymentSheetResult._applePayClassicInvoked
+ _OBJC_IVAR_$_AMSPurchase._purchaseUUID
+ _OBJC_IVAR_$_AMSPurchase._servicesPaymentViewServiceListener
+ _OBJC_IVAR_$_AMSPurchaseInfo._applePayClassicInvoked
+ _OBJC_IVAR_$_AMSPurchaseQueueConfiguration._excludesServerPayloadFromErrors
+ _OBJC_IVAR_$_AMSPurchaseTask._endTime
+ _OBJC_IVAR_$_AMSPurchaseTask._excludesServerPayloadFromErrors
+ _OBJC_IVAR_$_AMSPurchaseTask._startTime
+ _OBJC_IVAR_$_AMSSystemEngagementTask._remoteAlertActivationPending
+ _OBJC_IVAR_$_AMSSystemEngagementTask._remoteAlertHandleNeedsRecreation
+ _OBJC_IVAR_$_AMSSystemEngagementTask._remoteAlertTornDown
+ _OBJC_IVAR_$_AMSSystemEngagementTask._sceneRemoteAlertEnabled
+ _OBJC_IVAR_$_AMSSystemEngagementTask._viewServiceProcessIdentifier
+ _OBJC_IVAR_$_AMSTimedBiometricsSignatureResult._endTime
+ _OBJC_IVAR_$_AMSTimedBiometricsSignatureResult._signatureError
+ _OBJC_IVAR_$_AMSTimedBiometricsSignatureResult._signatureResult
+ _OBJC_IVAR_$_AMSTreatmentStore._metricsReporter
+ _OBJC_IVAR_$_AMSURLRequestEncoder._currentProcess
+ _OBJC_IVAR_$_AMSURLRequestEncoder._decorator
+ _OBJC_IVAR_$_AMSURLRequestEncoder._purchaseIdentifier
+ _OBJC_IVAR_$_AMSURLRequestProperties._purchaseIdentifier
+ _OBJC_IVAR_$_AMSURLTaskInfo._outcome
+ _OBJC_IVAR_$__PaymentSheetState._passwordChallengeRenderTime
+ _OBJC_METACLASS_$_AMSFinanceSubscriptionInviteResponse
+ _OBJC_METACLASS_$_AMSHARRecordingTracker
+ _OBJC_METACLASS_$_AMSMetricsServicesAnalyticsKitEnqueueContext
+ _OBJC_METACLASS_$_AMSRequestDecorator
+ _OBJC_METACLASS_$_AMSSecureThreeDomainInterruptionRequestHandler
+ _OBJC_METACLASS_$_AMSSecureThreeDomainInterruptionTask
+ _OBJC_METACLASS_$_AMSSubscriptionInviteTask
+ _OBJC_METACLASS_$_AMSTimedBiometricsSignatureResult
+ _OBJC_METACLASS_$_AMSTreatmentStoreMetricsReporter
+ _OBJC_METACLASS_$_AMSUnderlyingErrorTreeBridge
+ __CLASS_METHODS_AMSFinanceSubscriptionInviteResponse
+ __CLASS_METHODS_AMSMetricsServicesAnalyticsKitBridge
+ __CLASS_METHODS_AMSUnderlyingErrorTreeBridge
+ __CLASS_PROPERTIES_AMSMetricsServicesAnalyticsKitBridge
+ __DATA_AMSFinanceSubscriptionInviteResponse
+ __DATA_AMSMetricsServicesAnalyticsKitEnqueueContext
+ __DATA_AMSUnderlyingErrorTreeBridge
+ __DATA__TtC18AppleMediaServices31LazyServicesAnalyticsKitMetrics
+ __INSTANCE_METHODS_AMSFinanceSubscriptionInviteResponse
+ __INSTANCE_METHODS_AMSMetricsServicesAnalyticsKitEnqueueContext
+ __INSTANCE_METHODS_AMSUnderlyingErrorTreeBridge
+ __IVARS_AMSFinanceSubscriptionInviteResponse
+ __IVARS_AMSMetricsServicesAnalyticsKitEnqueueContext
+ __IVARS__TtC18AppleMediaServices31LazyServicesAnalyticsKitMetrics
+ __METACLASS_DATA_AMSFinanceSubscriptionInviteResponse
+ __METACLASS_DATA_AMSMetricsServicesAnalyticsKitEnqueueContext
+ __METACLASS_DATA_AMSUnderlyingErrorTreeBridge
+ __METACLASS_DATA__TtC18AppleMediaServices31LazyServicesAnalyticsKitMetrics
+ __OBJC_$_CATEGORY_NSDate_$_AppleMediaServices
+ __OBJC_$_CATEGORY_NSHTTPCookie_$_AppleMediaServices
+ __OBJC_$_CLASS_METHODS_AMSRequestDecorator
+ __OBJC_$_CLASS_METHODS_AMSSecureThreeDomainInterruptionRequestHandler
+ __OBJC_$_CLASS_METHODS_NSDate(AppleMediaServices|AMSFormattingUtilities)
+ __OBJC_$_CLASS_METHODS_NSHTTPCookie(AppleMediaServices|AMSCookieProperties|NSSecureCoding_Temporary|AMSCookieExpiry)
+ __OBJC_$_CLASS_METHODS_NSString(AppleMediaServices|AppleMediaServices|AMSFormattingUtilities)
+ __OBJC_$_CLASS_PROP_LIST_AMSRequestDecorator
+ __OBJC_$_INSTANCE_METHODS_AMSHARRecordingTracker
+ __OBJC_$_INSTANCE_METHODS_AMSRequestDecorator
+ __OBJC_$_INSTANCE_METHODS_AMSSecureThreeDomainInterruptionTask
+ __OBJC_$_INSTANCE_METHODS_AMSSubscriptionInviteTask
+ __OBJC_$_INSTANCE_METHODS_AMSTimedBiometricsSignatureResult
+ __OBJC_$_INSTANCE_METHODS_AMSTreatmentStoreMetricsReporter
+ __OBJC_$_INSTANCE_METHODS_NSDate(AppleMediaServices|AMSFormattingUtilities)
+ __OBJC_$_INSTANCE_METHODS_NSHTTPCookie(AppleMediaServices|AMSCookieProperties|NSSecureCoding_Temporary|AMSCookieExpiry)
+ __OBJC_$_INSTANCE_METHODS_NSString(AppleMediaServices|AppleMediaServices|AMSFormattingUtilities)
+ __OBJC_$_INSTANCE_VARIABLES_AMSHARRecordingTracker
+ __OBJC_$_INSTANCE_VARIABLES_AMSSecureThreeDomainInterruptionTask
+ __OBJC_$_INSTANCE_VARIABLES_AMSSubscriptionInviteTask
+ __OBJC_$_INSTANCE_VARIABLES_AMSTimedBiometricsSignatureResult
+ __OBJC_$_PROP_LIST_AMSHARRecordingTracker
+ __OBJC_$_PROP_LIST_AMSRequestDecorator
+ __OBJC_$_PROP_LIST_AMSSecureThreeDomainInterruptionTask
+ __OBJC_$_PROP_LIST_AMSSubscriptionInviteTask
+ __OBJC_$_PROP_LIST_AMSTimedBiometricsSignatureResult
+ __OBJC_$_PROP_LIST_AMSTreatmentStoreMetricsReporter
+ __OBJC_$_PROP_LIST_NSHTTPCookie_$_AppleMediaServices
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AMSRequestDecorating
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AMSTreatmentStoreMetricsReporting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AMSRequestDecorating
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AMSTreatmentStoreMetricsReporting
+ __OBJC_$_PROTOCOL_REFS_AMSRequestDecorating
+ __OBJC_$_PROTOCOL_REFS_AMSTreatmentStoreMetricsReporting
+ __OBJC_CLASS_PROTOCOLS_$_AMSRequestDecorator
+ __OBJC_CLASS_PROTOCOLS_$_AMSTreatmentStoreMetricsReporter
+ __OBJC_CLASS_PROTOCOLS_$_NSHTTPCookie(AppleMediaServices|AMSCookieProperties|NSSecureCoding_Temporary|AMSCookieExpiry)
+ __OBJC_CLASS_RO_$_AMSHARRecordingTracker
+ __OBJC_CLASS_RO_$_AMSRequestDecorator
+ __OBJC_CLASS_RO_$_AMSSecureThreeDomainInterruptionRequestHandler
+ __OBJC_CLASS_RO_$_AMSSecureThreeDomainInterruptionTask
+ __OBJC_CLASS_RO_$_AMSSubscriptionInviteTask
+ __OBJC_CLASS_RO_$_AMSTimedBiometricsSignatureResult
+ __OBJC_CLASS_RO_$_AMSTreatmentStoreMetricsReporter
+ __OBJC_LABEL_PROTOCOL_$_AMSRequestDecorating
+ __OBJC_LABEL_PROTOCOL_$_AMSTreatmentStoreMetricsReporting
+ __OBJC_METACLASS_RO_$_AMSHARRecordingTracker
+ __OBJC_METACLASS_RO_$_AMSRequestDecorator
+ __OBJC_METACLASS_RO_$_AMSSecureThreeDomainInterruptionRequestHandler
+ __OBJC_METACLASS_RO_$_AMSSecureThreeDomainInterruptionTask
+ __OBJC_METACLASS_RO_$_AMSSubscriptionInviteTask
+ __OBJC_METACLASS_RO_$_AMSTimedBiometricsSignatureResult
+ __OBJC_METACLASS_RO_$_AMSTreatmentStoreMetricsReporter
+ __OBJC_PROTOCOL_$_AMSRequestDecorating
+ __OBJC_PROTOCOL_$_AMSTreatmentStoreMetricsReporting
+ __PROTOCOLS_AMSFinanceSubscriptionInviteResponse
+ ___35-[AMSSubscriptionInviteTask cancel]_block_invoke
+ ___36-[AMSSubscriptionInviteTask perform]_block_invoke
+ ___37-[AMSHTTPArchiveService flushPromise]_block_invoke
+ ___37-[AMSHTTPArchiveService flushPromise]_block_invoke_2
+ ___37-[AMSHTTPArchiveService flushPromise]_block_invoke_3
+ ___38+[AMSRequestDecorator sharedDecorator]_block_invoke
+ ___39+[AMSHTTPArchiveService _sharedService]_block_invoke
+ ___41+[AMSHTTPArchive _sharedRecordingTracker]_block_invoke
+ ___47+[AMSHTTPArchiveService _sharedConnectionQueue]_block_invoke
+ ___47-[AMSSecureThreeDomainInterruptionTask perform]_block_invoke
+ ___48-[AMSHARRecordingTracker trackedRecordingBlock:]_block_invoke
+ ___49-[AMSSubscriptionInviteTask _presentInterruption]_block_invoke
+ ___50-[AMSPurchaseTask _promiseExcludingServerPayload:]_block_invoke
+ ___54-[AMSHARRecordingTracker notifyWhenIdleOnQueue:block:]_block_invoke
+ ___56+[AMSHTTPArchive flushPendingEntriesPromiseWithTimeout:]_block_invoke
+ ___56-[AMSMetrics _enqueueFigaroEvents:scheduleDelayedFlush:]_block_invoke_2
+ ___56-[AMSSystemEngagementTask remoteAlertHandleDidActivate:]_block_invoke
+ ___61+[AMSHTTPArchive _recordTaskInfo:responseData:route:tracker:]_block_invoke
+ ___61-[AMSSecureThreeDomainInterruptionTask _presentInterruption:]_block_invoke
+ ___62-[AMSSystemEngagementTask listener:shouldAcceptNewConnection:]_block_invoke
+ ___63-[AMSSystemEngagementTask _handleSceneRemoteAlertDeactivation:]_block_invoke
+ ___63-[AMSURLRequestEncoder _addCookiesToRequest:account:decorator:]_block_invoke
+ ___70-[AMSPaymentSheetTask _authorizePaymentWithBiometricsRequest:payment:]_block_invoke_4
+ ___73+[AMSHTTPArchive _flushPendingEntriesWithTracker:archiveService:timeout:]_block_invoke
+ ___73+[AMSHTTPArchive _flushPendingEntriesWithTracker:archiveService:timeout:]_block_invoke_2
+ ___73+[AMSHTTPArchive _flushPendingEntriesWithTracker:archiveService:timeout:]_block_invoke_3
+ ___73+[AMSHTTPArchive _flushPendingEntriesWithTracker:archiveService:timeout:]_block_invoke_4
+ ___76-[AMSSecureThreeDomainInterruptionTask _resolvePresentationTargetAndPresent]_block_invoke
+ ___77-[AMSPaymentSheetPerformanceMetrics enqueueDismissalMetricsEventWithOverlay:]_block_invoke
+ ___78+[AMSSecureThreeDomainInterruptionRequestHandler percentEncodedFormComponent:]_block_invoke
+ ___87+[AMSSecureThreeDomainInterruptionRequestHandler bodyByInjectingSessionId:intoRequest:]_block_invoke
+ ___AMSExcludedPurchaseErrorKeys_block_invoke
+ ___AMSURLRequestEncoderIsAppStoreProcess_block_invoke
+ ___block_descriptor_32_e28_"AMSHTTPArchiveService"8?0l
+ ___block_descriptor_32_e62_"AMSPromise"24?0"AMSBiometricsSignatureResult"8"NSError"16l
+ ___block_descriptor_40_e8_32s_e16_v16?0"NSData"8ls32l8
+ ___block_descriptor_40_e8_32s_e41_B24?0"NSURLQueryItem"8"NSDictionary"16ls32l8
+ ___block_descriptor_48_e8_32s40s_e32_v24?0"AMSBoolean"8"NSError"16ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e16_v16?0"NSData"8lw40l8s32l8
+ ___block_descriptor_48_e8_32w40w_e5_v8?0lw32l8w40l8
+ ___block_descriptor_49_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
+ ___block_descriptor_56_e8_32s40bs_e20_v20?0B8"NSError"12ls40l8s32l8
+ ___block_descriptor_56_e8_32s40bs_e46_"AMSPromise"24?0"NSDictionary"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s48s_e41_"AMSPromise"24?0"NSArray"8"NSError"16ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48r56r_e43_v24?0"AMSSQLiteQueryResults"8"NSError"16ls32l8r48l8r56l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56r_e30_"AMSPromise"16?0"NSNumber"8ls32l8s40l8s48l8r56l8
+ ___block_descriptor_64_e8_32s40s48s56r_e34_"AMSPromise"16?0"NSDictionary"8lr56l8s32l8s40l8s48l8
+ ___block_descriptor_64_e8_32s40s48s56s_e38_"AMSBinaryPromise"20?0B8"NSError"12ls32l8s40l8s48l8s56l8
+ ___block_descriptor_64_e8_32s40s48s56s_e44_"AMSPromise"24?0"AMSBoolean"8"NSError"16ls32l8s40l8s48l8s56l8
+ ___block_descriptor_72_e8_32s40s48s56r64r_e30_"AMSPromise"16?0"NSNumber"8ls32l8s40l8r56l8s48l8r64l8
+ ___block_descriptor_72_e8_32s40s48s56s64s_e33_v28?0"NSNumber"8B16"NSError"20ls32l8s40l8s48l8s56l8s64l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e45_"AMSPromise"24?0"AMSOptional"8"NSError"16lr72l8s32l8s40l8s48l8s56l8s64l8
+ ___getSPKSecureThreeDomainInterruptionClass_block_invoke
+ ___getSPKSubscriptionInviteInterruptionClass_block_invoke
+ ___swift_closure_destructor.101Tm
+ ___swift_closure_destructor.172Tm
+ ___swift_closure_destructor.176Tm
+ ___swift_closure_destructor.180Tm
+ ___swift_closure_destructor.279Tm
+ ___swift_closure_destructor.323Tm
+ ___swift_closure_destructor.404Tm
+ ___swift_closure_destructor.408Tm
+ ___swift_closure_destructor.98Tm
+ _associated conformance 18AppleMediaServices13HARBufferCoreO6EffectOSHAASQ
+ _associated conformance 18AppleMediaServices16MusicRestrictionOSHAASQ
+ _associated conformance 18AppleMediaServices26NearFieldRedeemReadingModeO5EventOSHAASQ
+ _associated conformance 18AppleMediaServices26NearFieldRedeemReadingModeO5PhaseOSHAASQ
+ _associated conformance So36AMSMetricsServicesAnalyticsKitBridgeC010AppleMediaB0E5ErrorO10Foundation09LocalizedH0ACsAD
+ _associated conformance So36AMSMetricsServicesAnalyticsKitBridgeC010AppleMediaB0E5ErrorO10Foundation13CustomNSErrorACsAD
+ _dispatch_group_create
+ _dispatch_group_enter
+ _dispatch_group_leave
+ _dispatch_group_notify
+ _sharedService
+ _swift_isUniquelyReferenced_nonNull
+ _symbolic $sSo36AMSMetricsServicesAnalyticsKitBridgeC010AppleMediaB0E12EventMatcherP
+ _symbolic SS11description_Si9errorCodet
+ _symbolic Sb21recordedSinceLastTick_t
+ _symbolic Sb8buffered_t
+ _symbolic SbyYbc
+ _symbolic Sd26cardSessionKeyValidityTime_t
+ _symbolic So12AMSURLActionCSgIegg_
+ _symbolic So12AMSURLActionCSgIeyBy_
+ _symbolic So25AMSSubscriptionInviteTaskC
+ _symbolic So36AMSSecureThreeDomainInterruptionTaskC
+ _symbolic So37AMSFinancePaymentInterruptionResponseCXDXMT
+ _symbolic So44AMSMetricsServicesAnalyticsKitEnqueueContextC
+ _symbolic _____ 18AppleMediaServices04LazyC19AnalyticsKitMetricsC
+ _symbolic _____ 18AppleMediaServices13HARBufferCoreO
+ _symbolic _____ 18AppleMediaServices13HARBufferCoreO5EventO
+ _symbolic _____ 18AppleMediaServices13HARBufferCoreO5PhaseO
+ _symbolic _____ 18AppleMediaServices13HARBufferCoreO6EffectO
+ _symbolic _____ 18AppleMediaServices16MusicRestrictionO
+ _symbolic _____ 18AppleMediaServices25NearFieldMetricsEventCoreO
+ _symbolic _____ 18AppleMediaServices26NearFieldRedeemReadingModeO
+ _symbolic _____ 18AppleMediaServices26NearFieldRedeemReadingModeO5EventO
+ _symbolic _____ 18AppleMediaServices26NearFieldRedeemReadingModeO5PhaseO
+ _symbolic _____ 18AppleMediaServices26NearFieldRedeemReadingModeO6ActionO
+ _symbolic _____ So36AMSMetricsServicesAnalyticsKitBridgeC010AppleMediaB0E17TopicEventMatcherV
+ _symbolic _____ So36AMSMetricsServicesAnalyticsKitBridgeC010AppleMediaB0E18MetricsProcessInfoV
+ _symbolic _____ So36AMSMetricsServicesAnalyticsKitBridgeC010AppleMediaB0E19BuyFlowEventMatcherV
+ _symbolic _____ So36AMSMetricsServicesAnalyticsKitBridgeC010AppleMediaB0E5ErrorO
+ _symbolic _____ So38AMSSecureThreeDomainInterruptionStatusV
+ _symbolic _____Sg 20ServicesAnalyticsKit30OriginProcessAMSMetricsContextV
+ _symbolic _____Sg So38AMSSecureThreeDomainInterruptionStatusV
+ _symbolic _____Sg s15SuspendingClockV7InstantV
+ _symbolic ______Sd26cardSessionKeyValidityTimet 18AppleMediaServices26NearFieldRedeemReadingModeO5PhaseO
+ _symbolic ___________t 18AppleMediaServices26NearFieldRedeemReadingModeO AC5EventO
+ _symbolic ______p So36AMSMetricsServicesAnalyticsKitBridgeC010AppleMediaB0E12EventMatcherP
+ _symbolic ______ypt s11AnyHashableV
+ _symbolic ______yptSg s11AnyHashableV
+ _symbolic _____ySo15NFReaderSessionCSgG 15Synchronization5MutexVAARi_zrlE
+ _symbolic _____y______pG s23_ContiguousArrayStorageC So36AMSMetricsServicesAnalyticsKitBridgeC010AppleMediaE0E12EventMatcherP
+ _symbolic _____y_____y_____y_____GGG s16IteratorSequenceV s08IndexingA0V s10ArraySliceV s5UInt8V
+ _type_layout_string So36AMSMetricsServicesAnalyticsKitBridgeC010AppleMediaB0E17TopicEventMatcherV
+ _type_layout_string So36AMSMetricsServicesAnalyticsKitBridgeC010AppleMediaB0E19BuyFlowEventMatcherV
+ _type_layout_string So36AMSMetricsServicesAnalyticsKitBridgeC010AppleMediaB0E5ErrorO
- -[AMSMetrics setSakBridge:]
- -[AMSMetricsLoadURLContext properties]
- -[AMSMetricsLoadURLContext setBuyParams:]
- -[AMSMetricsLoadURLContext setProperties:]
- -[AMSPurchase _generateIdentifier]
- -[AMSURLRequestEncoder _addCookiesToRequest:account:]
- GCC_except_table66
- GCC_except_table69
- GCC_except_table70
- GCC_except_table85
- GCC_except_table94
- GCC_except_table97
- _OBJC_CLASS_$_NFReaderSession$lazyGOT$loadHelper_x2$for$_OUTLINED_FUNCTION_86+8
- _OBJC_IVAR_$_AMSMetricsLoadURLContext._properties
- __DATA__TtC18AppleMediaServices41MetricsServicesAnalyticsKitBridgeInternal
- __IVARS__TtC18AppleMediaServices41MetricsServicesAnalyticsKitBridgeInternal
- __METACLASS_DATA__TtC18AppleMediaServices41MetricsServicesAnalyticsKitBridgeInternal
- __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDate_$_AMSFormattingUtilities
- __OBJC_$_CATEGORY_NSDate_$_AMSFormattingUtilities
- __OBJC_$_CATEGORY_NSHTTPCookie_$_AMSCookieExpiry
- __OBJC_$_CLASS_METHODS_NSDate(AMSFormattingUtilities|AppleMediaServices)
- __OBJC_$_CLASS_METHODS_NSHTTPCookie(AMSCookieExpiry|AppleMediaServices|AMSCookieProperties|NSSecureCoding_Temporary)
- __OBJC_$_CLASS_METHODS_NSString(AppleMediaServices|AMSFormattingUtilities|AppleMediaServices)
- __OBJC_$_INSTANCE_METHODS_NSHTTPCookie(AMSCookieExpiry|AppleMediaServices|AMSCookieProperties|NSSecureCoding_Temporary)
- __OBJC_$_INSTANCE_METHODS_NSString(AppleMediaServices|AMSFormattingUtilities|AppleMediaServices)
- __OBJC_$_PROP_LIST_NSDate_$_AMSFormattingUtilities
- __OBJC_CLASS_PROTOCOLS_$_NSHTTPCookie(AMSCookieExpiry|AppleMediaServices|AMSCookieProperties|NSSecureCoding_Temporary)
- ___37+[AMSHTTPArchiveService _sharedProxy]_block_invoke_3
- ___45+[AMSStreamHTTPArchiveEntryController buffer]_block_invoke_2
- ___53-[AMSURLRequestEncoder _addCookiesToRequest:account:]_block_invoke
- ___56+[AMSHTTPArchive ams_recordTaskInfo:responseData:route:]_block_invoke
- ___block_descriptor_48_e8_32s40s_e41_"AMSPromise"24?0"NSArray"8"NSError"16ls32l8s40l8
- ___block_descriptor_56_e8_32s40s48r_e30_"AMSPromise"16?0"NSNumber"8ls32l8s40l8r48l8
- ___block_descriptor_56_e8_32s40s48r_e34_"AMSPromise"16?0"NSDictionary"8lr48l8s32l8s40l8
- ___block_descriptor_56_e8_32s40s48s_e44_"AMSPromise"24?0"AMSBoolean"8"NSError"16ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48r56r_e30_"AMSPromise"16?0"NSNumber"8ls32l8s40l8r48l8r56l8
- ___block_descriptor_64_e8_32s40s48r_e43_v24?0"AMSSQLiteQueryResults"8"NSError"16ls32l8r48l8s40l8
- ___block_descriptor_64_e8_32s40s48s56s_e33_v28?0"NSNumber"8B16"NSError"20ls32l8s40l8s48l8s56l8
- ___block_descriptor_72_e8_32s40s48s56s64r_e45_"AMSPromise"24?0"AMSOptional"8"NSError"16lr64l8s32l8s40l8s48l8s56l8
- ___swift_closure_destructor.170Tm
- ___swift_closure_destructor.174Tm
- ___swift_closure_destructor.178Tm
- ___swift_closure_destructor.277Tm
- ___swift_closure_destructor.312Tm
- ___swift_closure_destructor.393Tm
- ___swift_closure_destructor.399Tm
- ___swift_closure_destructor.87Tm
- __sharedProxy.sharedService
- _flat unique So39AMSMetricsBagConfigurationStoreProtocol_p
- _symbolic So28AMSMetricsDatabaseDataSourceC
- _symbolic _____ 18AppleMediaServices07MetricsC26AnalyticsKitBridgeInternalC
- _symbolic _____ 18AppleMediaServices07MetricsC26AnalyticsKitBridgeInternalC0D11ProcessInfoV
- _symbolic ______SDySSypGt 20ServicesAnalyticsKit7MetricsV
- _symbolic ______SDySSypGtSg 20ServicesAnalyticsKit7MetricsV
- _symbolic ______pSg So39AMSMetricsBagConfigurationStoreProtocolP
CStrings:
+ "  musicRestriction: "
+ " events destined to it"
+ "!\xb3"
+ "%20"
+ "%{public}@: [%{public}@] Buy flow redirection to ServicesAnalyticsKit is disabled via bag, sampling buy flow loadUrl event normally"
+ "%{public}@: [%{public}@] Collecting buy flow loadUrl event without sampling"
+ "%{public}@: [%{public}@] Deactivated remote alert invalidated, recreating handle on next activation"
+ "%{public}@: [%{public}@] Embedded remote alert deactivated, recreating handle on next activation"
+ "%{public}@: [%{public}@] Gave up flushing pending HAR records; the archive may be truncated. %{public}@"
+ "%{public}@: [%{public}@] Initial activation finished. error: %{public}@"
+ "%{public}@: [%{public}@] Metrics dictionary unavailable, treating buy flow redirection to ServicesAnalyticsKit as enabled"
+ "%{public}@: [%{public}@] Purchase id absent in loadUrl context, sampling buy flow loadUrl event normally"
+ "%{public}@: [%{public}@] Remote alert handle created. sceneRemoteAlert: %d, valid: %d"
+ "%{public}@: [%{public}@] Scene remote alert enabled: %d, bagError: %{public}@"
+ "%{public}@: [%{public}@] Skipping re-activation: activation pending or handle already active"
+ "%{public}@: [%{public}@] View service connection invalidated"
+ "%{public}@: [%{public}@] View service terminated"
+ "%{public}@Enqueuing paymentSheetDismissal event. userResponseTime: %{public}@, purchaseId: %{public}@"
+ "%{public}@Excluded the server response body from the purchase error"
+ "%{public}@Failed to decode 3DS body as UTF-8"
+ "%{public}@Failed to parse 3DS form body"
+ "%{public}@Not logging Payment Sheet dismissal, no topic provided."
+ "%{public}@Not logging Payment Sheet dismissal, pageRender was never enqueued."
+ "%{public}@Not logging Payment Sheet dismissal, pageRender was not sampled in."
+ "%{public}@Not logging Payment Sheet dismissal, the sheet never presented."
+ "%{public}@Not logging Payment Sheet dismissal, userResponseTime was never recorded."
+ "%{public}@Not updating body for content type: %{public}@"
+ "%{public}@Recording authentication timing event. method: %{public}@, success: %{public}@"
+ "%{public}@ServicesPaymentKit does not accept clientData, dropping it"
+ "%{public}@ServicesPaymentKit does not accept subscriptionInfo, so the sheet will look the subscription up on the server"
+ "%{public}@SubsForGroups feature disabled (subscriptionFamilyId=%{public}@, sceneIdentifier=%{public}@)"
+ "%{public}s Failed to restart waiting for tap: %{private,mask.hash}s"
+ "%{public}s Failed to start keyed reading after first tap: %{private,mask.hash}s"
+ "%{public}s Ignoring callback from an ended reader session"
+ "%{public}s Reading event %{public}s -> %{public}s"
+ "%{public}s SE key validity expired; waiting for tap again"
+ "%{public}s Start waiting for tap..."
+ "%{public}s Started polling, waiting for tap"
+ "%{public}s Timed out waiting for tap"
+ "-._~"
+ "-paymentInterruption"
+ "38BC2C08-01A6-451D-9ABE-791707FBD11C"
+ "3D Secure Interruption Failed"
+ "3DS UI process reported an internal error"
+ "3DS authentication was cancelled by the user"
+ "3DS authentication was rejected by the issuer"
+ "3DS interruption cancelled by user; failing purchase"
+ "3DS interruption failed with internal error; failing purchase. reason="
+ "3DS interruption failed: "
+ "3DS interruption rejected by issuer; failing purchase"
+ "3DS interruption resolved, replaying purchase"
+ "<%@ authentication timing event>"
+ "<%@ dialog event>"
+ "<%@ pageRender event>"
+ "<%@ paymentSheetDismissal event>"
+ "@\"AMSHTTPArchiveService\"8@?0"
+ "AMSAuthenticateOptionsPurchaseIdentifierKey"
+ "AMSError.MetricsServicesAnalyticsKitBridge"
+ "AMSMetrics.bag was nil, won't be able to enqueue metrics events to ServicesAnalyticsKit based on topic allowlist"
+ "AccountIdentity(altDSID: "
+ "AppleMediaServices_BridgedInterface.AMSFinanceSubscriptionInviteResponse"
+ "B24@?0@\"NSURLQueryItem\"8@\"NSDictionary\"16"
+ "Buy flow redirection to SAK disabled via bag"
+ "CardBlocked"
+ "CardUnredeemable"
+ "Event destined to ServicesAnalyticsKit: "
+ "Event didn't match due to buy flow redirection being disabled via bag"
+ "Event didn't match due to losing internal-only dice roll"
+ "Event didn't match due to missing "
+ "Event didn't match due to missing eventType"
+ "Event didn't match due to unsupported eventType: "
+ "Event didn't match due to unsupported topic: "
+ "Failed to construct retry action"
+ "Failed to construct retry action after 3DS resolution"
+ "Failed to instantiate SPKSecureThreeDomainInterruption"
+ "Failed to instantiate SPKSubscriptionInviteInterruption"
+ "H:%02x%02x%x%x%02x%02x"
+ "HAR Recording Connection Invalidated"
+ "InvalidLink"
+ "MaxAttemptFraudCode"
+ "MetricsLogging"
+ "Not passing origin process AMSMetrics context to SAK since there was no bag"
+ "Payment authorization failed unexpectedly."
+ "RateLimitFraudCode"
+ "Request has no subscriptionFamilyId"
+ "SKBuyFlowLatencyPurchaseEnd"
+ "SKBuyFlowLatencyPurchaseError"
+ "SKBuyFlowLatencyPurchaseStart"
+ "SPKPaymentSheet_macOS"
+ "SPKSecureThreeDomainInterruption"
+ "SPKSubscriptionInviteInterruption"
+ "ServicesAnalyticsKit is not available on this OS variant"
+ "ServicesAnalyticsKit is unavailable on this OS variant, dropping "
+ "ServicesAnalyticsKit-eligible topics from bag: "
+ "Starting 3DS interruption with response"
+ "SubsForGroups"
+ "SubsForGroups feature disabled"
+ "Subscription Invite Failed"
+ "Subscription invite failed: "
+ "Subscription invite was cancelled"
+ "Successfully matched buy flow event with eventType="
+ "Unknown paymentInterruption sub-type"
+ "amsPurchaseTaskEndTime"
+ "amsPurchaseTaskStartTime"
+ "applePayClassicInvoked"
+ "application/x-www-form-urlencoded"
+ "buyFlowRedirectToSAKDisabled"
+ "challengeRenderTime"
+ "connectionInterrupted"
+ "connectionInvalidated"
+ "dailyLimitExceeded"
+ "delegateAuthChallenge"
+ "endTime"
+ "goBack"
+ "goto"
+ "groupSubscriptionInfo"
+ "invalidArguments"
+ "kAgeSignalConflict"
+ "kApplePayClassicInvoked"
+ "kPurchaseIdentifier"
+ "metricsConfigDictionary is nil, won't enqueue metrics events to ServicesAnalyticsKit based on topic allowlist"
+ "openURL"
+ "opticID"
+ "outcome"
+ "paymentSheet"
+ "paymentSheetConfirmation"
+ "paymentSheetDismissal"
+ "platformNotSupported"
+ "purchaseIdentifier"
+ "purchaseUUID"
+ "randomizedSuppression"
+ "redirect"
+ "requestThrottled"
+ "retryRestore"
+ "seed"
+ "selfie_sing"
+ "serverError"
+ "serviceInterrupted"
+ "serviceUnavailable"
+ "snapshotTypeDoesNotConformToNSSecureCoding"
+ "spk-payment-sheet-macos-disabled"
+ "startTime"
+ "subscriptionInvite"
+ "systemEngagementSceneRemoteAlertEnabled"
+ "taskIdentifier"
+ "unknownAction"
+ "userResponseTime"
+ "v16@?0@\"NSData\"8"
+ "verifyPayment"
- "!\xa1"
- "<private>"
- "AMSMetrics.bag was nil, unable to enqueue any metrics events to ServicesAnalyticsKit"
- "CardStatusBlocked"
- "CardStatusUnredeemable"
- "Failed to read cached metrics dictionary for bag, enqueueing all events to AMS database"
- "H:"
- "RateLimitExceeded"
- "ServicesAnalyticsKit"
- "ServicesAnalyticsKit symbol not found, enqueueing all events to AMS database"
- "ServicesAnalyticsKit topics missing in metrics config in bag, enqueueing all events to AMS database"
- "ServicesAnalyticsKit-eligible topics: "
- "TreatmentStoreErrorMetrics"
```
