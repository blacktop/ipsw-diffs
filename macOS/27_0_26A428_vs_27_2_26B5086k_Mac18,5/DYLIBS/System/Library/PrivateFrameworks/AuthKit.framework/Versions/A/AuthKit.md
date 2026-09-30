## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/Versions/A/AuthKit`

### Sections with Same Size but Changed Content

- `__TEXT.__ustring`

```diff

-559.0.0.0.0
-  __TEXT.__text: 0x2bf6ec
-  __TEXT.__objc_methlist: 0x1032c
+560.125.4.1.0
+  __TEXT.__text: 0x2c56fc
+  __TEXT.__objc_methlist: 0x106dc
   __TEXT.__const: 0x3ac40
-  __TEXT.__cstring: 0x129a0
-  __TEXT.__oslogstring: 0x1565d
-  __TEXT.__gcc_except_tab: 0x65d4
+  __TEXT.__cstring: 0x12c43
+  __TEXT.__oslogstring: 0x15bdf
+  __TEXT.__gcc_except_tab: 0x6698
   __TEXT.__dlopen_cstrs: 0x250
   __TEXT.__ustring: 0x34a
-  __TEXT.__unwind_info: 0x7068
+  __TEXT.__unwind_info: 0x71b8
   __TEXT.__eh_frame: 0xc0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x5d00
-  __DATA_CONST.__objc_classlist: 0x7b0
+  __DATA_CONST.__const: 0x5dd0
+  __DATA_CONST.__objc_classlist: 0x7d8
   __DATA_CONST.__objc_catlist: 0x88
-  __DATA_CONST.__objc_protolist: 0x240
+  __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7f08
+  __DATA_CONST.__objc_selrefs: 0x80a8
   __DATA_CONST.__objc_protorefs: 0xf0
-  __DATA_CONST.__objc_superrefs: 0x4c8
+  __DATA_CONST.__objc_superrefs: 0x4f0
   __DATA_CONST.__objc_arraydata: 0x368
-  __DATA_CONST.__got: 0xa60
-  __AUTH_CONST.__const: 0xb730
-  __AUTH_CONST.__cfstring: 0x13c20
-  __AUTH_CONST.__objc_const: 0x2e150
+  __DATA_CONST.__got: 0xa70
+  __AUTH_CONST.__const: 0xb720
+  __AUTH_CONST.__cfstring: 0x13ea0
+  __AUTH_CONST.__objc_const: 0x2edc0
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__auth_got: 0x568
-  __AUTH.__objc_data: 0x3700
-  __DATA.__objc_ivar: 0x1228
-  __DATA.__data: 0x2098
+  __AUTH.__objc_data: 0x3890
+  __DATA.__objc_ivar: 0x1270
+  __DATA.__data: 0x20f8
   __DATA.__common: 0xa20
   __DATA_DIRTY.__objc_data: 0x15e0
   __DATA_DIRTY.__bss: 0x320

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 6200
-  Symbols:   14588
-  CStrings:  4559
+  Functions: 6280
+  Symbols:   14789
+  CStrings:  4604
 
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
+ GCC_except_table101
+ GCC_except_table103
+ GCC_except_table105
+ GCC_except_table106
+ GCC_except_table108
+ GCC_except_table145
+ GCC_except_table147
+ GCC_except_table148
+ GCC_except_table149
+ GCC_except_table152
+ GCC_except_table159
+ GCC_except_table189
+ GCC_except_table204
+ GCC_except_table213
+ GCC_except_table241
+ GCC_except_table242
+ GCC_except_table246
+ GCC_except_table248
+ GCC_except_table251
+ GCC_except_table297
+ GCC_except_table315
+ GCC_except_table318
+ GCC_except_table321
+ GCC_except_table330
+ GCC_except_table331
+ GCC_except_table332
+ GCC_except_table333
+ GCC_except_table334
+ GCC_except_table335
+ GCC_except_table336
+ GCC_except_table370
+ GCC_except_table379
+ GCC_except_table380
+ GCC_except_table393
+ GCC_except_table394
+ GCC_except_table395
+ GCC_except_table396
+ GCC_except_table397
+ GCC_except_table398
+ GCC_except_table45
+ GCC_except_table48
+ GCC_except_table68
+ OBJC_IVAR_$_AKAppleIDAuthenticationCommandLineContext._childAppleID
+ OBJC_IVAR_$_AKApprovalFlowCardCopy._primaryActionTitle
+ OBJC_IVAR_$_AKApprovalFlowCardCopy._subtitle
+ OBJC_IVAR_$_AKApprovalFlowCardCopy._title
+ OBJC_IVAR_$_AKApprovalFlowContext._cardCopy
+ OBJC_IVAR_$_AKApprovalFlowContext._messageId
+ OBJC_IVAR_$_AKApprovalFlowContext._pushInfo
+ OBJC_IVAR_$_AKApprovalFlowContext._ruiURLString
+ OBJC_IVAR_$_AKApprovalFlowPushInfo._idmsData
+ OBJC_IVAR_$_AKApprovalFlowPushInfo._pushCommand
+ OBJC_IVAR_$_AKBasicServerRequest._additionalHeaders
+ OBJC_IVAR_$_AKCLIServerUIFlowController._consecutiveRepeatCount
+ OBJC_IVAR_$_AKCLIServerUIFlowController._lastProcessedResponseDataHash
+ OBJC_IVAR_$_AKCLIServerUIFlowController._lastProcessedResponseURL
+ OBJC_IVAR_$_AKCLIServerUIFlowController._totalStepCount
+ OBJC_IVAR_$_AKDeviceListDeltaMessagePayload._stableID
+ OBJC_IVAR_$_AKDeviceListRequestContext._telemetryFlowID
+ OBJC_IVAR_$_AKServerBackoffHelper._aaaFoundationBackoffController
+ OBJC_IVAR_$_AKServerRequestConfiguration._continuationHeaders
+ OBJC_IVAR_$_AKServerRequestConfiguration._shouldReturnContinuationHeaders
+ OBJC_IVAR_$_AKSignoutInfo._telemetryFlowID
+ OBJC_IVAR_$_AKURLCachePolicyContext._bypassesURLCache
+ OBJC_IVAR_$_AKUserInformation._tcEligibility
+ _AKLogAASecurity.log
+ _AKLogAASecurity.onceToken
+ _AKNumberPropertyKeyTCEligibility
+ _AKPrivateConnectionEntitlement
+ _AKTrustLossNotification
+ _AKURLCachePolicyNSURLPropertyKey
+ _OBJC_CLASS_$_AKApprovalFlowCardCopy
+ _OBJC_CLASS_$_AKApprovalFlowPushInfo
+ _OBJC_CLASS_$_AKServerBackoffCLIController
+ _OBJC_CLASS_$_AKTransparencyController
+ _OBJC_CLASS_$_AKURLCachePolicyContext
+ _OBJC_METACLASS_$_AKApprovalFlowCardCopy
+ _OBJC_METACLASS_$_AKApprovalFlowPushInfo
+ _OBJC_METACLASS_$_AKServerBackoffCLIController
+ _OBJC_METACLASS_$_AKTransparencyController
+ _OBJC_METACLASS_$_AKURLCachePolicyContext
+ __119-[AKServerBackoffCLIController injectBackoffForURLBagKey:clientBundleID:proxiedAppBundleID:durationSeconds:completion:]_block_invoke
+ __64-[AKServerBackoffCLIController clearBackoffCacheWithCompletion:]_block_invoke
+ __65-[AKServerBackoffCLIController readCacheForURLBagKey:completion:]_block_invoke
+ __65-[AKTransparencyController metadataForAltDSID:flowId:completion:]_block_invoke
+ __69-[AKScopedTokenCLIController _refreshAllTokensForAltDSID:completion:]_block_invoke
+ __AKCallerContactRecencyWindowSecondsOverrideKey
+ __AKInformationStableIDKey
+ __AKLogAASecurity
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
+ ___block_descriptor_56_e8_32s40s48s_e35_v32?0"NSString"8"NSString"16^B24l
+ ___getAAFServerBackoffControllerClass_block_invoke
+ ___os_log_helper_16_2_3_8_0_8_64_8_64
+ _getAAFServerBackoffControllerClass
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
+ getAAFServerBackoffControllerClass.softClass
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
- GCC_except_table111
- GCC_except_table114
- GCC_except_table115
- GCC_except_table125
- GCC_except_table128
- GCC_except_table160
- GCC_except_table165
- GCC_except_table179
- GCC_except_table196
- GCC_except_table205
- GCC_except_table216
- GCC_except_table217
- GCC_except_table220
- GCC_except_table226
- GCC_except_table238
- GCC_except_table24
- GCC_except_table271
- GCC_except_table272
- GCC_except_table273
- GCC_except_table275
- GCC_except_table277
- GCC_except_table278
- GCC_except_table282
- GCC_except_table284
- GCC_except_table304
- GCC_except_table305
- GCC_except_table323
- GCC_except_table326
- GCC_except_table341
- GCC_except_table342
- GCC_except_table343
- GCC_except_table344
- GCC_except_table345
- GCC_except_table346
- GCC_except_table347
- GCC_except_table348
- GCC_except_table378
- GCC_except_table387
- GCC_except_table388
- GCC_except_table42
- GCC_except_table58
- GCC_except_table61
- GCC_except_table78
- OBJC_IVAR_$_AKApprovalFlowContext._baseURLString
- OBJC_IVAR_$_AKApprovalFlowContext._initialXML
- OBJC_IVAR_$_AKApprovalFlowContext._lock
- OBJC_IVAR_$_AKRemoteDevice._secureDeviceId
- OBJC_IVAR_$_AKRemoteDevice._stableId
- _AKAuthenticationBackgroundSignInKey
- _AKCarouselAlertSupplementViewApprovalFlow
- _AKCarouselApprovalFlowAlertIdentifier
- _AKDeviceStableIdKey
- _AKPreviousAccountInfoRefreshDateKey
- _AKSecureDeviceIdKey
- __81-[AKAppleIDAuthenticationController __presentTestApprovalFlowWithXML:completion:]_block_invoke
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
- ___block_descriptor_48_e8_32r40r_e5_v8?0l
- ___block_descriptor_80_e8_32bs40r48r56r_e34_v24?0"NSDictionary"8"NSError"16l
- _kAKApprovalFlowBaseURLStringKey
- _kAKApprovalFlowInitialXMLKey
- _objc_msgSend$__presentTestApprovalFlowWithXML:completion:
- _objc_msgSend$_retrieveContinuationHeaders
- _objc_msgSend$baseURLString
- _objc_msgSend$encodeObject:
- _objc_msgSend$initWithCodeType:baseURLString:initialXML:
- _objc_msgSend$initialXML
- _objc_msgSend$isTrustedDeviceIdEnabled
- _objc_msgSend$setChildAppleID:
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
