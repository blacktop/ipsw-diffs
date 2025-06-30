## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`

```diff

-8.6.6.0.0
-  __TEXT.__text: 0x693580
-  __TEXT.__auth_stubs: 0x40d0
-  __TEXT.__objc_methlist: 0x20b6c
-  __TEXT.__const: 0x540d0
+8.6.7.0.0
+  __TEXT.__text: 0x694b8c
+  __TEXT.__auth_stubs: 0x40c0
+  __TEXT.__objc_methlist: 0x20b44
+  __TEXT.__const: 0x540e0
   __TEXT.__dlopen_cstrs: 0x8d3
-  __TEXT.__cstring: 0x25053
+  __TEXT.__cstring: 0x25186
   __TEXT.__swift5_typeref: 0x3eb1
-  __TEXT.__swift5_reflstr: 0x1ee8
+  __TEXT.__swift5_reflstr: 0x1f18
   __TEXT.__swift5_assocty: 0x9d8
   __TEXT.__constg_swiftt: 0x2df0
   __TEXT.__swift5_builtin: 0x21c
-  __TEXT.__swift5_fieldmd: 0x2650
+  __TEXT.__swift5_fieldmd: 0x265c
   __TEXT.__swift5_proto: 0x700
   __TEXT.__swift5_types: 0x330
   __TEXT.__swift_as_entry: 0x43c

   __TEXT.__swift5_capture: 0x1e10
   __TEXT.__swift5_mpenum: 0x48
   __TEXT.__swift5_protos: 0x80
-  __TEXT.__oslogstring: 0x2e61a
-  __TEXT.__gcc_except_tab: 0x7a30
+  __TEXT.__oslogstring: 0x2e72b
+  __TEXT.__gcc_except_tab: 0x7b34
   __TEXT.__ustring: 0x1b2
-  __TEXT.__unwind_info: 0xd450
+  __TEXT.__unwind_info: 0xd468
   __TEXT.__eh_frame: 0xd314
-  __TEXT.__objc_classname: 0x3c02
-  __TEXT.__objc_methname: 0x40eea
-  __TEXT.__objc_methtype: 0x735e
-  __TEXT.__objc_stubs: 0x2d180
+  __TEXT.__objc_classname: 0x3bf6
+  __TEXT.__objc_methname: 0x410a3
+  __TEXT.__objc_methtype: 0x7374
+  __TEXT.__objc_stubs: 0x2d1a0
   __DATA_CONST.__got: 0x17d0
-  __DATA_CONST.__const: 0xb9b8
-  __DATA_CONST.__objc_classlist: 0x12c8
+  __DATA_CONST.__const: 0xba78
+  __DATA_CONST.__objc_classlist: 0x12c0
   __DATA_CONST.__objc_catlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x3a8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe6c0
+  __DATA_CONST.__objc_selrefs: 0xe6c8
   __DATA_CONST.__objc_protorefs: 0x1b8
   __DATA_CONST.__objc_superrefs: 0xc58
   __DATA_CONST.__objc_arraydata: 0x4f8
-  __AUTH_CONST.__auth_got: 0x2080
-  __AUTH_CONST.__const: 0x24df0
-  __AUTH_CONST.__cfstring: 0x21160
-  __AUTH_CONST.__objc_const: 0x384c8
+  __AUTH_CONST.__auth_got: 0x2078
+  __AUTH_CONST.__const: 0x24e10
+  __AUTH_CONST.__cfstring: 0x211c0
+  __AUTH_CONST.__objc_const: 0x38400
   __AUTH_CONST.__objc_intobj: 0xcd8
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH.__objc_data: 0x7f40
   __AUTH.__data: 0x12b0
-  __DATA.__objc_ivar: 0x17d0
+  __DATA.__objc_ivar: 0x17d8
   __DATA.__data: 0x4d80
   __DATA.__bss: 0xa0c1
   __DATA.__common: 0xb78
   __DATA_DIRTY.__objc_ivar: 0x65c
-  __DATA_DIRTY.__objc_data: 0x54c8
+  __DATA_DIRTY.__objc_data: 0x5478
   __DATA_DIRTY.__data: 0x1ae0
   __DATA_DIRTY.__bss: 0x3320
   __DATA_DIRTY.__common: 0x70

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 833133B9-552F-3207-8FD1-95208BDC26C4
-  Functions: 19888
-  Symbols:   46159
-  CStrings:  23966
+  UUID: CFC4E8CE-F6B7-331E-9B09-1D596DA462DD
+  Functions: 19890
+  Symbols:   46165
+  CStrings:  23990
 
Symbols:
+ -[AMSURLProtocolHandler fraudReportRefreshScoreBlock]
+ -[AMSURLProtocolHandler fraudReportStateStorageFactoryBlock]
+ -[AMSURLProtocolHandler initWithFraudReportRefreshScoreBlock:fraudReportStateStorageFactoryBlock:]
+ -[AMSURLProtocolHandler initWithMetricsHandler:fairPlayDeviceIdentity:fraudReportRefreshScoreBlock:fraudReportStateStorageFactoryBlock:]
+ -[AMSURLRequestProperties hash]
+ -[AMSURLRequestProperties isEqual:]
+ _AMSFraudReportFallbackAccountForAccount
+ _AMSFraudReportHandleResponseWithDetachedHandling
+ _AMSFraudReportResponseHandlingDefaultRefreshScoreBlock_block_invoke
+ _AMSFraudReportResponseHandlingDefaultStateStorageFactoryBlock_block_invoke_2
+ _AMSFraudReportUpdateInitURLStateStorage
+ _OBJC_IVAR_$_AMSURLProtocolHandler._fraudReportRefreshScoreBlock
+ _OBJC_IVAR_$_AMSURLProtocolHandler._fraudReportStateStorageFactoryBlock
+ ___46-[AMSURLProtocolHandler _handleResponse:task:]_block_invoke.120
+ ___46-[AMSURLProtocolHandler _handleResponse:task:]_block_invoke.129
+ ___46-[AMSURLProtocolHandler _handleResponse:task:]_block_invoke.137
+ ___46-[AMSURLProtocolHandler _handleResponse:task:]_block_invoke.146
+ ___46-[AMSURLProtocolHandler _handleResponse:task:]_block_invoke.149
+ ___46-[AMSURLProtocolHandler _handleResponse:task:]_block_invoke_2.148
+ ___AMSFraudReportGetFSRHeadersForFraudReportResponse_block_invoke.58
+ ___AMSFraudReportHandleCallbackFraudReportResponse_block_invoke.66
+ ___AMSFraudReportHandleInitURLFraudReportResponse_block_invoke.40
+ ___AMSFraudReportHandleResponseWithDetachedHandling_block_invoke
+ ___AMSFraudReportHandleResponse_block_invoke
+ ___block_descriptor_32_e41_"AMSFraudReportDatabaseStateStorage"8?0l
+ ___block_descriptor_40_e8_32s_e52_"AMSBinaryPromise"24?0"AMSURLResult"8"NSError"16ls32l8
+ ___block_descriptor_56_e8_32s40s48bs_e46_"AMSPromise"24?0"NSDictionary"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e52_"AMSBinaryPromise"24?0"AMSURLResult"8"NSError"16ls32l8s48l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56s64s72bs_e52_"AMSBinaryPromise"24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8s56l8s72l8s64l8
+ ___block_descriptor_88_e8_32s40s48s56s64s72bs80bs_e30_"AMSPromise"16?0"NSNumber"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
+ ___block_descriptor_97_e8_32s40s48s56s64s72s80bs88bs_e36_"AMSBinaryPromise"16?0"NSNumber"8ls32l8s40l8s48l8s56l8s64l8s80l8s72l8s88l8
+ ___block_literal_global.24
+ _objc_msgSend$initWithMetricsHandler:fairPlayDeviceIdentity:fraudReportRefreshScoreBlock:fraudReportStateStorageFactoryBlock:
- +[AMSFraudReport bagKeySet]
- +[AMSFraudReport bagSubProfileVersion]
- +[AMSFraudReport bagSubProfile]
- +[AMSFraudReport createBagForSubProfile]
- +[AMSFraudReport(Deprecated) addDeviceIdentityCertificateAndSignatureToRequest:parameters:bag:]
- +[AMSFraudReport(Deprecated) handleResponse:account:bag:]
- +[AMSFraudReport(Deprecated) isFeatureSupportedForBag:]
- -[AMSURLRequest setProperties:]
- _AMSFraudReportHandleResponseDefaultRefreshScoreBlock_block_invoke
- _OBJC_CLASS_$_AMSFraudReport
- _OBJC_METACLASS_$_AMSFraudReport
- __OBJC_$_CLASS_METHODS_AMSFraudReport(Deprecated)
- __OBJC_$_CLASS_PROP_LIST_AMSFraudReport
- __OBJC_$_PROP_LIST_AMSFraudReport
- __OBJC_CLASS_PROTOCOLS_$_AMSFraudReport
- __OBJC_CLASS_RO_$_AMSFraudReport
- __OBJC_METACLASS_RO_$_AMSFraudReport
- ___46-[AMSURLProtocolHandler _handleResponse:task:]_block_invoke.119
- ___46-[AMSURLProtocolHandler _handleResponse:task:]_block_invoke.127
- ___46-[AMSURLProtocolHandler _handleResponse:task:]_block_invoke.136
- ___46-[AMSURLProtocolHandler _handleResponse:task:]_block_invoke.145
- ___46-[AMSURLProtocolHandler _handleResponse:task:]_block_invoke.148
- ___46-[AMSURLProtocolHandler _handleResponse:task:]_block_invoke_2.147
- ___95+[AMSFraudReport(Deprecated) addDeviceIdentityCertificateAndSignatureToRequest:parameters:bag:]_block_invoke
- ___AMSFraudReportGetFSRHeadersForFraudReportResponse_block_invoke.42
- ___AMSFraudReportHandleCallbackFraudReportResponse_block_invoke.47
- ___AMSFraudReportShouldCallInitURL_block_invoke
- ____AMSFraudReportHandleResponse_block_invoke
- ___block_descriptor_64_e8_32s40s48s56s_e46_"AMSPromise"24?0"NSDictionary"8"NSError"16ls32l8s40l8s48l8s56l8
- ___block_descriptor_88_e8_32s40s48s56s64s72s80bs_e30_"AMSPromise"16?0"NSNumber"8ls32l8s40l8s48l8s56l8s64l8s72l8s80l8
CStrings:
+ "@\"AMSBinaryPromise\"16@?0@\"NSNumber\"8"
+ "@\"AMSBinaryPromise\"24@?0@\"AMSURLResult\"8@\"NSError\"16"
+ "@\"AMSFraudReportDatabaseStateStorage\"8@?0"
+ "@48@0:8@16@24@?32@?40"
+ "AMSFraudReport [%{public}@] Calling callback URL."
+ "AMSFraudReport [%{public}@] Calling init URL."
+ "AMSFraudReport [%{public}@] Failed to report new fraud score to the callback url: %{public}@."
+ "AMSFraudReport [%{public}@] Retrying original request with updated score."
+ "AMSFraudReport [%{public}@] Successfully reported new fraud score to the callback url."
+ "AMSFraudReport: [%{public}@] Skipping fraud report score refresh because fraud report is not enabled in the bag."
+ "AMSFraudReport: [%{public}@] Updated Init URL persistent state."
+ "AMSFraudReportInitURLPersistenceKey"
+ "AMSFraudReportInitURLUpdatedState"
+ "FSR callback URL not found in response"
+ "FSR init URL not found in response"
+ "T#,&,V_paymentSheetTaskClass"
+ "T@\"<AMSBagProtocol>\",&,V_bag"
+ "T@\"<AMSResponseDecoding>\",&,V_responseDecoder"
+ "T@\"ACAccount\",C,V_account"
+ "T@\"AMSKeychainOptions\",C,V_keychainOptions"
+ "T@\"AMSProcessInfo\",C,V_clientInfo"
+ "T@\"AMSPurchaseInfo\",&,V_purchaseInfo"
+ "T@\"AMSURLRequestProperties\",R,N,V_properties"
+ "T@\"NSDictionary\",C,V_additionalMetrics"
+ "T@\"NSDictionary\",C,V_userInfo"
+ "T@\"NSString\",C,V_gsTokenIdentifier"
+ "T@\"NSString\",C,V_logUUID"
+ "T@?,R,N,V_fraudReportRefreshScoreBlock"
+ "T@?,R,N,V_fraudReportStateStorageFactoryBlock"
+ "TB,V_disableBiometricsResponseHandling"
+ "TB,V_disableLoadURLMetrics"
+ "TB,V_knownToBeTrusted"
+ "TB,V_remoteSecuritySigningEnabled"
+ "TSDataSyncMetricsErrorEnhancements"
+ "Tq,V_maxRetryCount"
+ "Tq,V_reversePushType"
+ "_fraudReportRefreshScoreBlock"
+ "_fraudReportStateStorageFactoryBlock"
+ "fraudReportRefreshScoreBlock"
+ "fraudReportStateStorageFactoryBlock"
+ "initWithFraudReportRefreshScoreBlock:fraudReportStateStorageFactoryBlock:"
+ "initWithMetricsHandler:fairPlayDeviceIdentity:fraudReportRefreshScoreBlock:fraudReportStateStorageFactoryBlock:"
- "AMSFraudReport [%{public}@] Failed reporting the new fraud score to the callback url: %{public}@."
- "AMSFraudReport [%{public}@] Successfully reported the new fraud score to the callback url."
- "AMSFraudReport: [%{public}@] Skipping fraud report score refresh."
- "Deprecated"
- "FraudScoreReport"
- "T@\"NSDictionary\",C,N,V_additionalMetrics"
- "TB,N,V_disableBiometricsResponseHandling"
- "TB,N,V_disableLoadURLMetrics"
- "TB,N,V_disableResponseDecoding"
- "TB,N,V_excludeIdentifierHeadersForAccount"
- "TB,N,V_knownToBeTrusted"
- "TB,N,V_remoteSecuritySigningEnabled"
- "TB,N,V_shouldSetCookiesFromResponse"
- "TB,N,V_shouldSetStorefrontFromResponse"
- "Tq,N,V_anisetteType"
- "Tq,N,V_dialogOptions"
- "Tq,N,V_maxRetryCount"
- "Tq,N,V_mescalType"
- "Tq,N,V_reversePushType"
- "addDeviceIdentityCertificateAndSignatureToRequest:parameters:bag:"
- "handleResponse:account:bag:"
- "isFeatureSupportedForBag:"

```
