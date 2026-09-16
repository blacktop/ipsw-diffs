## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

### Sections with Same Size but Changed Content

- `__TEXT.__ustring`

```diff

-559.0.0.0.0
-  __TEXT.__text: 0x19f218
-  __TEXT.__objc_methlist: 0x10584
+560.125.4.1.0
+  __TEXT.__text: 0x1a528c
+  __TEXT.__objc_methlist: 0x10934
   __TEXT.__const: 0xd30
-  __TEXT.__cstring: 0x12f98
-  __TEXT.__oslogstring: 0x15b61
-  __TEXT.__gcc_except_tab: 0x6638
+  __TEXT.__cstring: 0x1323c
+  __TEXT.__oslogstring: 0x160e3
+  __TEXT.__gcc_except_tab: 0x66fc
   __TEXT.__dlopen_cstrs: 0x267
   __TEXT.__ustring: 0x34a
-  __TEXT.__unwind_info: 0x6f08
+  __TEXT.__unwind_info: 0x7050
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7908
-  __DATA_CONST.__objc_classlist: 0x7d0
+  __DATA_CONST.__const: 0x79c8
+  __DATA_CONST.__objc_classlist: 0x7f8
   __DATA_CONST.__objc_catlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x240
+  __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x81c0
+  __DATA_CONST.__objc_selrefs: 0x8360
   __DATA_CONST.__objc_protorefs: 0xf0
-  __DATA_CONST.__objc_superrefs: 0x4c8
+  __DATA_CONST.__objc_superrefs: 0x4f0
   __DATA_CONST.__objc_arraydata: 0x358
-  __DATA_CONST.__got: 0xbc8
-  __AUTH_CONST.__const: 0x1400
-  __AUTH_CONST.__cfstring: 0x13fc0
-  __AUTH_CONST.__objc_const: 0x2e8c0
+  __DATA_CONST.__got: 0xbd8
+  __AUTH_CONST.__const: 0x1420
+  __AUTH_CONST.__cfstring: 0x14240
+  __AUTH_CONST.__objc_const: 0x2f530
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_dictobj: 0x410
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__auth_got: 0x528
-  __AUTH.__objc_data: 0x3890
-  __DATA.__objc_ivar: 0x1248
-  __DATA.__data: 0x1bf0
+  __AUTH.__objc_data: 0x3a20
+  __DATA.__objc_ivar: 0x1290
+  __DATA.__data: 0x1c50
   __DATA_DIRTY.__objc_data: 0x1590
   __DATA_DIRTY.__bss: 0x2f0
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6112
-  Symbols:   14640
-  CStrings:  4633
+  Functions: 6192
+  Symbols:   14848
+  CStrings:  4678
 
Symbols:
+ +[AKApprovalFlowCardCopy supportsSecureCoding]
+ +[AKApprovalFlowPushInfo supportsSecureCoding]
+ +[AKChildAccountModel emailComponentsFromEmail:]
+ +[AKURLCachePolicyContext supportsSecureCoding]
+ -[AKAccountManager _propertyForKey:account:]
+ -[AKAccountManager _setValue:forKey:account:]
+ -[AKAccountManager dateFromAccount:withKey:]
+ -[AKAccountManager numberFromAccount:withKey:]
+ -[AKAccountManager setDate:forAccount:withKey:]
+ -[AKAccountManager setNumber:forAccount:withKey:]
+ -[AKAccountManager setString:forAccount:withKey:]
+ -[AKAccountManager stringFromAccount:withKey:]
+ -[AKAccountRecoveryStepLocalAuthentication _pinViewAttributesFromResponse:]
+ -[AKAppleIDAuthenticationCommandLineContext childAppleID]
+ -[AKAppleIDAuthenticationCommandLineContext setChildAppleID:]
+ -[AKAppleIDServerResourceLoadDelegate continuationHeaders]
+ -[AKAppleIDServerResourceLoadDelegate setContinuationHeaders:]
+ -[AKApprovalFlowCardCopy .cxx_destruct]
+ -[AKApprovalFlowCardCopy copyWithZone:]
+ -[AKApprovalFlowCardCopy description]
+ -[AKApprovalFlowCardCopy encodeWithCoder:]
+ -[AKApprovalFlowCardCopy initWithCoder:]
+ -[AKApprovalFlowCardCopy initWithTitle:subtitle:primaryActionTitle:]
+ -[AKApprovalFlowCardCopy primaryActionTitle]
+ -[AKApprovalFlowCardCopy subtitle]
+ -[AKApprovalFlowCardCopy title]
+ -[AKApprovalFlowContext cardCopy]
+ -[AKApprovalFlowContext initWithCodeType:messageId:ruiURLString:pushInfo:cardCopy:serverRequestConfiguration:]
+ -[AKApprovalFlowContext messageId]
+ -[AKApprovalFlowContext pushInfo]
+ -[AKApprovalFlowContext ruiURLString]
+ -[AKApprovalFlowPushInfo .cxx_destruct]
+ -[AKApprovalFlowPushInfo copyWithZone:]
+ -[AKApprovalFlowPushInfo description]
+ -[AKApprovalFlowPushInfo encodeWithCoder:]
+ -[AKApprovalFlowPushInfo idmsData]
+ -[AKApprovalFlowPushInfo initWithCoder:]
+ -[AKApprovalFlowPushInfo initWithPushCommand:idmsData:]
+ -[AKApprovalFlowPushInfo pushCommand]
+ -[AKBasicServerRequest additionalHeaders]
+ -[AKBasicServerRequest setAdditionalHeaders:]
+ -[AKCLIServerUIFlowController _resetLoopProtectionState]
+ -[AKCLIServerUIFlowController _shouldAbortForRepeatedOrExcessiveResponse:]
+ -[AKChildAccountModel resolvedAppleIDWithServerInfo:]
+ -[AKChildAccountRequestHelper _logResponseForStep:data:httpResponse:]
+ -[AKChildAccountRequestHelper _maskedHeaderFields:]
+ -[AKConfiguration callerContactRecencyWindowSecondsOverride]
+ -[AKConfiguration setCallerContactRecencyWindowSecondsOverride:]
+ -[AKDeviceListDeltaMessagePayload stableID]
+ -[AKDeviceListRequestContext setTelemetryFlowID:]
+ -[AKDeviceListRequestContext telemetryFlowID]
+ -[AKScopedTokenCLIController _refreshAllTokensForAltDSID:completion:]
+ -[AKScopedTokenCLIController refreshAllTokensForAltDSID:completion:]
+ -[AKServerBackoffCLIController clearBackoffCacheWithCompletion:]
+ -[AKServerBackoffCLIController init]
+ -[AKServerBackoffCLIController injectBackoffForURLBagKey:clientBundleID:proxiedAppBundleID:durationSeconds:completion:]
+ -[AKServerBackoffCLIController readCacheForURLBagKey:completion:]
+ -[AKServerBackoffController _clientInfoForContext:urlBagKey:]
+ -[AKServerBackoffController _sendBackoffEventNamed:clientInfo:]
+ -[AKServerBackoffController reportClientBackoffTelemetryForContext:urlBagKey:]
+ -[AKServerBackoffHelper _backoffControllerWhenFeatureEnabled]
+ -[AKServerBackoffHelper shouldBackoffRequest:urlBagKey:]
+ -[AKServerRequestConfiguration continuationHeaders]
+ -[AKServerRequestConfiguration setContinuationHeaders:]
+ -[AKServerRequestConfiguration setShouldReturnContinuationHeaders:]
+ -[AKServerRequestConfiguration shouldReturnContinuationHeaders]
+ -[AKSignoutInfo setTelemetryFlowID:]
+ -[AKSignoutInfo telemetryFlowID]
+ -[AKTransparencyController init]
+ -[AKTransparencyController metadataForAltDSID:flowId:completion:]
+ -[AKURLCachePolicyContext bypassesURLCache]
+ -[AKURLCachePolicyContext copyWithZone:]
+ -[AKURLCachePolicyContext encodeWithCoder:]
+ -[AKURLCachePolicyContext initWithBypassesURLCache:]
+ -[AKURLCachePolicyContext initWithCoder:]
+ -[AKURLSession URLSession:dataTask:willCacheResponse:completionHandler:]
+ -[AKURLSession requestByEnforcingURLCachePolicy:]
+ -[AKURLSession shouldBypassURLCacheForRequest:]
+ -[AKUserInformation setTcEligibility:]
+ -[AKUserInformation tcEligibility]
+ -[NSMutableURLRequest(AKURLCachePolicy) ak_updateWithURLCachePolicyContext:]
+ -[NSURLRequest(AKURLCachePolicy) ak_extractURLCachePolicyContext]
+ GCC_except_table100
+ GCC_except_table114
+ GCC_except_table139
+ GCC_except_table141
+ GCC_except_table142
+ GCC_except_table143
+ GCC_except_table152
+ GCC_except_table153
+ GCC_except_table175
+ GCC_except_table179
+ GCC_except_table189
+ GCC_except_table192
+ GCC_except_table201
+ GCC_except_table203
+ GCC_except_table229
+ GCC_except_table230
+ GCC_except_table232
+ GCC_except_table235
+ GCC_except_table236
+ GCC_except_table239
+ GCC_except_table241
+ GCC_except_table282
+ GCC_except_table301
+ GCC_except_table304
+ GCC_except_table307
+ GCC_except_table316
+ GCC_except_table317
+ GCC_except_table318
+ GCC_except_table319
+ GCC_except_table320
+ GCC_except_table321
+ GCC_except_table322
+ GCC_except_table356
+ GCC_except_table365
+ GCC_except_table366
+ GCC_except_table379
+ GCC_except_table380
+ GCC_except_table381
+ GCC_except_table382
+ GCC_except_table383
+ GCC_except_table384
+ GCC_except_table64
+ GCC_except_table97
+ GCC_except_table99
+ _AKNumberPropertyKeyTCEligibility
+ _AKPrivateConnectionEntitlement
+ _AKTrustLossNotification
+ _AKURLCachePolicyNSURLPropertyKey
+ _OBJC_CLASS_$_AKApprovalFlowCardCopy
+ _OBJC_CLASS_$_AKApprovalFlowPushInfo
+ _OBJC_CLASS_$_AKServerBackoffCLIController
+ _OBJC_CLASS_$_AKTransparencyController
+ _OBJC_CLASS_$_AKURLCachePolicyContext
+ _OBJC_IVAR_$_AKAppleIDAuthenticationCommandLineContext._childAppleID
+ _OBJC_IVAR_$_AKApprovalFlowCardCopy._primaryActionTitle
+ _OBJC_IVAR_$_AKApprovalFlowCardCopy._subtitle
+ _OBJC_IVAR_$_AKApprovalFlowCardCopy._title
+ _OBJC_IVAR_$_AKApprovalFlowContext._cardCopy
+ _OBJC_IVAR_$_AKApprovalFlowContext._messageId
+ _OBJC_IVAR_$_AKApprovalFlowContext._pushInfo
+ _OBJC_IVAR_$_AKApprovalFlowContext._ruiURLString
+ _OBJC_IVAR_$_AKApprovalFlowPushInfo._idmsData
+ _OBJC_IVAR_$_AKApprovalFlowPushInfo._pushCommand
+ _OBJC_IVAR_$_AKBasicServerRequest._additionalHeaders
+ _OBJC_IVAR_$_AKCLIServerUIFlowController._consecutiveRepeatCount
+ _OBJC_IVAR_$_AKCLIServerUIFlowController._lastProcessedResponseDataHash
+ _OBJC_IVAR_$_AKCLIServerUIFlowController._lastProcessedResponseURL
+ _OBJC_IVAR_$_AKCLIServerUIFlowController._totalStepCount
+ _OBJC_IVAR_$_AKDeviceListDeltaMessagePayload._stableID
+ _OBJC_IVAR_$_AKDeviceListRequestContext._telemetryFlowID
+ _OBJC_IVAR_$_AKServerBackoffHelper._aaaFoundationBackoffController
+ _OBJC_IVAR_$_AKServerRequestConfiguration._continuationHeaders
+ _OBJC_IVAR_$_AKServerRequestConfiguration._shouldReturnContinuationHeaders
+ _OBJC_IVAR_$_AKSignoutInfo._telemetryFlowID
+ _OBJC_IVAR_$_AKURLCachePolicyContext._bypassesURLCache
+ _OBJC_IVAR_$_AKUserInformation._tcEligibility
+ _OBJC_METACLASS_$_AKApprovalFlowCardCopy
+ _OBJC_METACLASS_$_AKApprovalFlowPushInfo
+ _OBJC_METACLASS_$_AKServerBackoffCLIController
+ _OBJC_METACLASS_$_AKTransparencyController
+ _OBJC_METACLASS_$_AKURLCachePolicyContext
+ __AKCallerContactRecencyWindowSecondsOverrideKey
+ __AKInformationStableIDKey
+ __AKLogAASecurity
+ __AKLogAASecurity.log
+ __AKLogAASecurity.onceToken
+ __AKURLCachePolicyContextBypassesURLCacheKey
+ __OBJC_$_CLASS_METHODS_AKApprovalFlowCardCopy
+ __OBJC_$_CLASS_METHODS_AKApprovalFlowPushInfo
+ __OBJC_$_CLASS_METHODS_AKChildAccountModel
+ __OBJC_$_CLASS_METHODS_AKURLCachePolicyContext
+ __OBJC_$_CLASS_METHODS_NSMutableURLRequest(AKTokenScoping|AKURLCachePolicy|AuthKit)
+ __OBJC_$_CLASS_PROP_LIST_AKApprovalFlowCardCopy
+ __OBJC_$_CLASS_PROP_LIST_AKApprovalFlowPushInfo
+ __OBJC_$_CLASS_PROP_LIST_AKURLCachePolicyContext
+ __OBJC_$_INSTANCE_METHODS_AKApprovalFlowCardCopy
+ __OBJC_$_INSTANCE_METHODS_AKApprovalFlowPushInfo
+ __OBJC_$_INSTANCE_METHODS_AKServerBackoffCLIController
+ __OBJC_$_INSTANCE_METHODS_AKTransparencyController
+ __OBJC_$_INSTANCE_METHODS_AKURLCachePolicyContext
+ __OBJC_$_INSTANCE_METHODS_NSMutableURLRequest(AKTokenScoping|AKURLCachePolicy|AuthKit)
+ __OBJC_$_INSTANCE_METHODS_NSURLRequest(AKTokenScoping|AKURLCachePolicy|AuthKit)
+ __OBJC_$_INSTANCE_VARIABLES_AKApprovalFlowCardCopy
+ __OBJC_$_INSTANCE_VARIABLES_AKApprovalFlowPushInfo
+ __OBJC_$_INSTANCE_VARIABLES_AKURLCachePolicyContext
+ __OBJC_$_PROP_LIST_AKApprovalFlowCardCopy
+ __OBJC_$_PROP_LIST_AKApprovalFlowPushInfo
+ __OBJC_$_PROP_LIST_AKTransparencyController
+ __OBJC_$_PROP_LIST_AKURLCachePolicyContext
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AKTransparencyInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AKTransparencyInterface
+ __OBJC_$_PROTOCOL_REFS_AKTransparencyInterface
+ __OBJC_CLASS_PROTOCOLS_$_AKApprovalFlowCardCopy
+ __OBJC_CLASS_PROTOCOLS_$_AKApprovalFlowPushInfo
+ __OBJC_CLASS_PROTOCOLS_$_AKTransparencyController
+ __OBJC_CLASS_PROTOCOLS_$_AKURLCachePolicyContext
+ __OBJC_CLASS_RO_$_AKApprovalFlowCardCopy
+ __OBJC_CLASS_RO_$_AKApprovalFlowPushInfo
+ __OBJC_CLASS_RO_$_AKServerBackoffCLIController
+ __OBJC_CLASS_RO_$_AKTransparencyController
+ __OBJC_CLASS_RO_$_AKURLCachePolicyContext
+ __OBJC_LABEL_PROTOCOL_$_AKTransparencyInterface
+ __OBJC_METACLASS_RO_$_AKApprovalFlowCardCopy
+ __OBJC_METACLASS_RO_$_AKApprovalFlowPushInfo
+ __OBJC_METACLASS_RO_$_AKServerBackoffCLIController
+ __OBJC_METACLASS_RO_$_AKTransparencyController
+ __OBJC_METACLASS_RO_$_AKURLCachePolicyContext
+ __OBJC_PROTOCOL_$_AKTransparencyInterface
+ ___119-[AKServerBackoffCLIController injectBackoffForURLBagKey:clientBundleID:proxiedAppBundleID:durationSeconds:completion:]_block_invoke
+ ___51-[AKChildAccountRequestHelper _maskedHeaderFields:]_block_invoke
+ ___64-[AKServerBackoffCLIController clearBackoffCacheWithCompletion:]_block_invoke
+ ___65-[AKServerBackoffCLIController readCacheForURLBagKey:completion:]_block_invoke
+ ___65-[AKTransparencyController metadataForAltDSID:flowId:completion:]_block_invoke
+ ___68-[AKScopedTokenCLIController refreshAllTokensForAltDSID:completion:]_block_invoke
+ ___69-[AKScopedTokenCLIController _refreshAllTokensForAltDSID:completion:]_block_invoke
+ ____AKLogAASecurity_block_invoke
+ ___block_descriptor_56_e8_32s40s48s_e35_v32?0"NSString"8"NSString"16^B24ls32l8s40l8s48l8
+ ___block_descriptor_64_e8_32bs40r_e17_v16?0"NSError"8ls32l8r40l8
+ ___block_descriptor_64_e8_32bs40r_e30_v24?0"NSString"8"NSError"16ls32l8r40l8
+ ___getAAFServerBackoffControllerClass_block_invoke
+ ___os_log_helper_16_2_3_8_0_8_64_8_64
+ _getAAFServerBackoffControllerClass
+ _getAAFServerBackoffControllerClass.softClass
+ _kAKAnalyticsContextType
+ _kAKAnalyticsEventBackoffClient
+ _kAKAnalyticsEventBackoffServer
+ _kAKAnalyticsEventSignoutEnd
+ _kAKAnalyticsEventSignoutStart
+ _kAKAnalyticsEventTDIDTrustLoss
+ _kAKAnalyticsEventTDLChangePushReceived
+ _kAKApprovalFlowCardCopyKey
+ _kAKApprovalFlowCardCopyPrimaryActionTitleKey
+ _kAKApprovalFlowCardCopySubtitleKey
+ _kAKApprovalFlowCardCopyTitleKey
+ _kAKApprovalFlowContextKey
+ _kAKApprovalFlowMessageIdKey
+ _kAKApprovalFlowPushInfoIdMSDataKey
+ _kAKApprovalFlowPushInfoKey
+ _kAKApprovalFlowPushInfoPushCommandKey
+ _kAKApprovalFlowRUIURLStringKey
+ _kAKBasicServerRequestAdditionalHeaders
+ _kAKSignoutInfoTelemetryFlowIDKey
+ _objc_msgSend$_backoffControllerWhenFeatureEnabled
+ _objc_msgSend$_clientInfoForContext:urlBagKey:
+ _objc_msgSend$_logResponseForStep:data:httpResponse:
+ _objc_msgSend$_maskedHeaderFields:
+ _objc_msgSend$_pinViewAttributesFromResponse:
+ _objc_msgSend$_propertyForKey:account:
+ _objc_msgSend$_refreshAllTokensForAltDSID:completion:
+ _objc_msgSend$_resetLoopProtectionState
+ _objc_msgSend$_sendBackoffEventNamed:clientInfo:
+ _objc_msgSend$_setValue:forKey:account:
+ _objc_msgSend$_shouldAbortForRepeatedOrExcessiveResponse:
+ _objc_msgSend$ak_extractURLCachePolicyContext
+ _objc_msgSend$bypassesURLCache
+ _objc_msgSend$cardCopy
+ _objc_msgSend$clearServerBackoffCacheWithCompletion:
+ _objc_msgSend$continuationHeaders
+ _objc_msgSend$emailComponentsFromEmail:
+ _objc_msgSend$idmsData
+ _objc_msgSend$initWithAppServerName:userDefaults:
+ _objc_msgSend$initWithBypassesURLCache:
+ _objc_msgSend$initWithCodeType:messageId:ruiURLString:pushInfo:cardCopy:serverRequestConfiguration:
+ _objc_msgSend$initWithPushCommand:idmsData:
+ _objc_msgSend$initWithTitle:subtitle:primaryActionTitle:
+ _objc_msgSend$injectServerBackoffForURLBagKey:clientBundleID:proxiedAppBundleID:durationSeconds:completion:
+ _objc_msgSend$instancesRespondToSelector:
+ _objc_msgSend$messageId
+ _objc_msgSend$percentEncodedPath
+ _objc_msgSend$percentEncodedQuery
+ _objc_msgSend$primaryActionTitle
+ _objc_msgSend$processBackoffInfoFrom:
+ _objc_msgSend$pushCommand
+ _objc_msgSend$pushInfo
+ _objc_msgSend$readServerBackoffCacheForURLBagKey:completion:
+ _objc_msgSend$refreshAllTokensForAltDSID:completion:
+ _objc_msgSend$reportClientBackoffTelemetryForContext:urlBagKey:
+ _objc_msgSend$requestByEnforcingURLCachePolicy:
+ _objc_msgSend$resolvedAppleIDWithServerInfo:
+ _objc_msgSend$ruiURLString
+ _objc_msgSend$setCachePolicy:
+ _objc_msgSend$setContinuationHeaders:
+ _objc_msgSend$setPercentEncodedPath:
+ _objc_msgSend$setPercentEncodedQuery:
+ _objc_msgSend$setShouldReturnContinuationHeaders:
+ _objc_msgSend$setTcEligibility:
+ _objc_msgSend$shouldBackoffForURLBagKey:clientBundleID:proxiedAppBundleID:
+ _objc_msgSend$shouldBackoffRequest:urlBagKey:
+ _objc_msgSend$shouldBypassURLCacheForRequest:
+ _objc_msgSend$subtitle
+ _objc_msgSend$transparencyMetadataForAltDSID:flowId:completion:
- -[AKAccountManager previousAccountInfoRefreshDateForAccount:]
- -[AKAccountManager setPreviousAccountInfoRefreshDate:forAccount:]
- -[AKAppleIDAuthenticationController __presentTestApprovalFlowWithXML:completion:]
- -[AKAppleIDServerResourceLoadDelegate _retrieveContinuationHeaders]
- -[AKApprovalFlowContext baseURLString]
- -[AKApprovalFlowContext initWithCodeType:baseURLString:initialXML:]
- -[AKApprovalFlowContext initialXML]
- -[AKApprovalFlowContext setServerRequestConfiguration:]
- -[AKFeatureManager isBackgroundiCloudSignInEnabled]
- -[AKFeatureManager isTrustedDeviceIdEnabled]
- -[AKRemoteDevice secureDeviceId]
- -[AKRemoteDevice setSecureDeviceId:]
- -[AKRemoteDevice setStableId:]
- -[AKRemoteDevice stableId]
- -[AKURLBag isBackgroundiCloudSignInEnabled]
- GCC_except_table119
- GCC_except_table154
- GCC_except_table171
- GCC_except_table173
- GCC_except_table184
- GCC_except_table193
- GCC_except_table205
- GCC_except_table208
- GCC_except_table211
- GCC_except_table215
- GCC_except_table225
- GCC_except_table226
- GCC_except_table257
- GCC_except_table258
- GCC_except_table259
- GCC_except_table261
- GCC_except_table263
- GCC_except_table264
- GCC_except_table268
- GCC_except_table291
- GCC_except_table309
- GCC_except_table312
- GCC_except_table327
- GCC_except_table328
- GCC_except_table329
- GCC_except_table330
- GCC_except_table331
- GCC_except_table332
- GCC_except_table333
- GCC_except_table334
- GCC_except_table364
- GCC_except_table373
- GCC_except_table374
- GCC_except_table54
- GCC_except_table59
- GCC_except_table60
- _AKAuthenticationBackgroundSignInKey
- _AKCarouselAlertSupplementViewApprovalFlow
- _AKCarouselApprovalFlowAlertIdentifier
- _AKDeviceStableIdKey
- _AKPreviousAccountInfoRefreshDateKey
- _AKSecureDeviceIdKey
- _OBJC_IVAR_$_AKApprovalFlowContext._baseURLString
- _OBJC_IVAR_$_AKApprovalFlowContext._initialXML
- _OBJC_IVAR_$_AKApprovalFlowContext._lock
- _OBJC_IVAR_$_AKRemoteDevice._secureDeviceId
- _OBJC_IVAR_$_AKRemoteDevice._stableId
- __AKURLBagKeyBackgroundiCloudSignInConfigKey
- __OBJC_$_CLASS_METHODS_NSMutableURLRequest(AKTokenScoping|AuthKit)
- __OBJC_$_INSTANCE_METHODS_NSMutableURLRequest(AKTokenScoping|AuthKit)
- __OBJC_$_INSTANCE_METHODS_NSURLRequest(AKTokenScoping|AuthKit)
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_AKAuthKitUIMacServiceProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_AKAuthKitUIMacServiceProtocol
- ___51-[AKApprovalFlowContext serverRequestConfiguration]_block_invoke
- ___55-[AKApprovalFlowContext setServerRequestConfiguration:]_block_invoke
- ___81-[AKAppleIDAuthenticationController __presentTestApprovalFlowWithXML:completion:]_block_invoke
- ___96-[AKAuthorizationController fetchPrimaryApplicationInformationForWebServiceWithInfo:completion:]_block_invoke_2
- ___block_descriptor_48_e8_32r40r_e5_v8?0lr32l8r40l8
- ___block_descriptor_48_e8_32s40bs_e46_v32?0"NSData"8"NSURLResponse"16"NSError"24ls32l8s40l8
- ___block_descriptor_80_e8_32bs40r48r56r_e34_v24?0"NSDictionary"8"NSError"16lr40l8r48l8r56l8s32l8
- _kAKApprovalFlowBaseURLStringKey
- _kAKApprovalFlowInitialXMLKey
- _objc_msgSend$__presentTestApprovalFlowWithXML:completion:
- _objc_msgSend$_retrieveContinuationHeaders
- _objc_msgSend$baseURLString
- _objc_msgSend$encodeObject:
- _objc_msgSend$initWithCodeType:baseURLString:initialXML:
- _objc_msgSend$initialXML
- _objc_msgSend$isTrustedDeviceIdEnabled
- _objc_msgSend$setServerRequestConfiguration:
CStrings:
+ "<%@: %p codeType=%@ messageId=%@ ruiURLString=%@ hasPushInfo=%@ cardCopy=%@>"
+ "<%@: %p pushCommand=%lu hasIdMSData=%@>"
+ "<%@: %p title=%@ subtitle=%@ primaryActionTitle=%@>"
+ "<%@: %p; altDSID=%@, urlBagKey=%@, requestBody=%@, additionalHeaders=%@, expectedResponseFormat=%lu, requestBodyFormat=%lu, telemetryFlowID=%@>"
+ "<%@: reason=%ld, processName=%@, signOutBeginTime=%@, signOutFinishTime=%@, signOutError=%@, telemetryFlowID=%@>"
+ "<%@:%p> Name: %@, SN: %@, TrustedDeviceId: %@, Build: %@, OS: %@, Version: %@, Model: %@, Timestamp: %@, Trusted: %d, Safety State' %@, Circle Status: %d, Color Code: %@, Additional Info %@, services: %@, lastCacheUpdatedDate: %@, deletedDate: %@, removalReason: %ld, isThisDevice: %d "
+ "AAAFoundation backoff controller unavailable or selector-mismatched; falling back to legacy controller."
+ "AAFServerBackoffController"
+ "AKApprovalFlowContext failed to archive the server request configuration, %@"
+ "AKApprovalFlowContext initialization failed, nil cardCopy"
+ "AKApprovalFlowContext initialization failed, nil messageId"
+ "AKApprovalFlowContext initialization failed, nil ruiURLString"
+ "AKApprovalFlowContext initialization failed, nil serverRequestConfiguration data"
+ "AKApprovalFlowContext initialization failed, unreadable serverRequestConfiguration, %@"
+ "AKServerBackoffController - No cached directive for urlBagKey %{public}@; reporting context-only client backoff"
+ "AuthPostProcessing"
+ "BEGIN [%lld]: ScopedTokenCLI-Refresh  enableTelemetry=YES "
+ "BEGIN [%lld]: TransparencyMetadata_Client  enableTelemetry=YES "
+ "Clear server backoff cache returned an error: %@"
+ "Clear server backoff cache was successful."
+ "Dispatching refresh all scoped tokens to AKD."
+ "END [%lld] %fs:ScopedTokenCLI-Refresh "
+ "END [%lld] %fs:TransparencyMetadata_Client "
+ "Exception caught fetching property %@: %@"
+ "Exception caught setting property %@: %@"
+ "Failed to decode AKURLCachePolicyContext: %@"
+ "Failed to encode AKURLCachePolicyContext: %@"
+ "Fetching transparency metadata for altDSID: %{mask.hash}@"
+ "Flow exceeded %lu total steps; aborting to avoid an infinite loop"
+ "Inject server backoff returned an error: %@"
+ "Inject server backoff was successful."
+ "Local authentication failed: push-style response (xa=push) has no pinView element with a usable url"
+ "PiggybackEscapeHatchContinuationData"
+ "PiggybackNonConnectableAdvertising"
+ "Push-style local authentication (xa=push): reading challenge from pinView. headerFields: %@, data: %@"
+ "Read server backoff cache returned an error: %@"
+ "Read server backoff cache was successful."
+ "Refresh all scoped tokens reply received: %@"
+ "ScopedTokenCLI-Refresh"
+ "Server returned the identical response %lu times in a row; aborting to avoid an infinite loop"
+ "TransparencyMetadata_Client"
+ "[%@] No usable email prefix from caller childAppleID or cachedServerInfo"
+ "[%@] Response body (%lu bytes, keys): %@"
+ "[%@] Response body: %lu bytes (non-dict JSON, not printed)"
+ "[%@] Response headers (HTTP %ld): %@"
+ "[%@] Skipping account-name/primary-email overrides: no usable childAppleID or auto-generated email"
+ "[Redirect] HTTP %ld from %@ has no '%@' continuation headers — following redirect as-is"
+ "_AKCallerContactRecencyWindowSecondsOverride"
+ "_bypassesURLCache"
+ "_cardCopy"
+ "_continuationHeaders"
+ "_messageId"
+ "_primaryActionTitle"
+ "_pushCommand"
+ "_pushInfo"
+ "_ruiURLString"
+ "_shouldReturnContinuationHeaders"
+ "_subtitle"
+ "_tcEligibility"
+ "additionalHeaders"
+ "appleAccountSecurity"
+ "approvalFlowContext"
+ "com.apple.authkit.TDIDTrustLoss"
+ "com.apple.authkit.TDLChangePushReceived"
+ "com.apple.authkit.TDLTDIDAvailability"
+ "com.apple.authkit.client.private"
+ "com.apple.authkit.signoutEnd"
+ "com.apple.authkit.signoutStart"
+ "com.apple.authkit.trust-loss"
+ "com.apple.authkit.urlcachepolicycontext"
+ "contextType"
+ "set-cookie"
+ "stid"
+ "tcEligibility"
+ "x-apple-i-cont"
- "<%@: %p codeType=%@ baseURLString=%@ hasInitialXML=%@ hasServerRequestConfiguration=%@>"
- "<%@: %p; altDSID=%@, urlBagKey=%@, requestBody=%@, expectedResponseFormat=%lu, requestBodyFormat=%lu, telemetryFlowID=%@>"
- "<%@: reason=%ld, processName=%@, signOutBeginTime=%@, signOutFinishTime=%@, signOutError=%@>"
- "<%@:%p> Name: %@, SN: %@, SDID: %@, TrustedDeviceId: %@, Build: %@, OS: %@, Version: %@, Model: %@, Timestamp: %@, Trusted: %d, Safety State' %@, Circle Status: %d, Color Code: %@, Additional Info %@, services: %@, lastCacheUpdatedDate: %@, deletedDate: %@, removalReason: %ld, stableId: %@, isThisDevice: %d "
- "AKApprovalFlowContext initialization failed, invalid base URL string"
- "AKApprovalFlowContext initialization failed, nil initial XML"
- "BackgroundiCloudSignIn"
- "Calling out to remote auth service to present test approval flow"
- "Ignoring duplicate primary bundle ID completion (XPC interrupt race)."
- "Local authentication failed: missing clientInfo element"
- "Local authentication: using push-style URL %@"
- "Not an Internal Build. Aborting test approval flow."
- "Redirect session is missing continuation header's."
- "Result of present test approval flow: error=%{public}@"
- "ServerDrivenApprovalFlowSMS"
- "TrustedDeviceId"
- "[%@] Auto-generated email has empty prefix"
- "[%@] Auto-generated email has no @ separator"
- "[%@] No auto-generated email in cachedServerInfo"
- "_baseURLString"
- "_initialXML"
- "_secureDeviceId"
- "_stableId"
- "background-iCloud-SignIn-enable"
- "com.apple.AuthKit.AKApprovalFlow"
- "com.apple.AuthKit.ApprovalFlowAlert"
- "com.apple.authkit.TDIDAvailability"
- "isEligibleForBackgroundSignIn"
- "previousAccountInfoRefreshDate"
- "sdid"
```
