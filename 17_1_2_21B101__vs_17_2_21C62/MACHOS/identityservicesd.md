## identityservicesd

> `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

```diff

-1814.200.71.2.7
-  __TEXT.__text: 0x60167c
-  __TEXT.__auth_stubs: 0x4910
-  __TEXT.__objc_stubs: 0x3fe60
-  __TEXT.__objc_methlist: 0x20c28
-  __TEXT.__const: 0x40da0
-  __TEXT.__gcc_except_tab: 0x1b0cc
-  __TEXT.__objc_methname: 0x686e1
-  __TEXT.__cstring: 0x51ef8
-  __TEXT.__oslogstring: 0x7002f
-  __TEXT.__objc_classname: 0x3c1e
-  __TEXT.__objc_methtype: 0xfefb
+1814.300.81.2.2
+  __TEXT.__text: 0x604a14
+  __TEXT.__auth_stubs: 0x4900
+  __TEXT.__objc_stubs: 0x40280
+  __TEXT.__objc_methlist: 0x20de8
+  __TEXT.__const: 0x40fc0
+  __TEXT.__gcc_except_tab: 0x1b20c
+  __TEXT.__objc_methname: 0x68dcb
+  __TEXT.__cstring: 0x52078
+  __TEXT.__oslogstring: 0x70698
+  __TEXT.__objc_classname: 0x3c75
+  __TEXT.__objc_methtype: 0xff7a
   __TEXT.__ustring: 0x52a
   __TEXT.__dlopen_cstrs: 0xa1
   __TEXT.__swift5_typeref: 0xfcc

   __TEXT.__swift5_proto: 0x10c
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0xd808
+  __TEXT.__unwind_info: 0xd8a4
   __TEXT.__eh_frame: 0xcd0
-  __DATA_CONST.__auth_got: 0x2498
-  __DATA_CONST.__got: 0x2060
+  __DATA_CONST.__auth_got: 0x2490
+  __DATA_CONST.__got: 0x2090
   __DATA_CONST.__auth_ptr: 0xd8
-  __DATA_CONST.__const: 0x19b10
-  __DATA_CONST.__cfstring: 0x31ac0
-  __DATA_CONST.__objc_classlist: 0xd30
+  __DATA_CONST.__const: 0x19c50
+  __DATA_CONST.__cfstring: 0x31c60
+  __DATA_CONST.__objc_classlist: 0xd38
   __DATA_CONST.__objc_catlist: 0x58
-  __DATA_CONST.__objc_protolist: 0x5f8
+  __DATA_CONST.__objc_protolist: 0x600
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x16f8
+  __DATA_CONST.__objc_intobj: 0x1740
   __DATA_CONST.__objc_arraydata: 0x548
   __DATA_CONST.__objc_arrayobj: 0x330
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x416e8
-  __DATA.__objc_selrefs: 0x13008
+  __DATA.__objc_const: 0x419b8
+  __DATA.__objc_selrefs: 0x13128
   __DATA.__objc_protorefs: 0xb0
   __DATA.__objc_classrefs: 0x17b8
-  __DATA.__objc_superrefs: 0xab0
-  __DATA.__objc_ivar: 0x2ecc
-  __DATA.__objc_data: 0x9c08
-  __DATA.__data: 0x6f08
+  __DATA.__objc_superrefs: 0xab8
+  __DATA.__objc_ivar: 0x2ee8
+  __DATA.__objc_data: 0x9c58
+  __DATA.__data: 0x6f68
   __DATA.__bss: 0x42a8
   __DATA.__common: 0x340
   SMOOTH.SMOOTH: 0xc

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 17158
-  Symbols:   2482
-  CStrings:  31590
+  Functions: 17203
+  Symbols:   2487
+  CStrings:  31680
 
Symbols:
+ _IDSDeliveryForceQueryKey
+ _IDSDeliveryKeyTransparencyURIVerificationMapKey
+ _IDSQuickRelayUserTypeKey
+ _kFZServiceDefaultsSentinelAlias
+ _kIDSForceQuerySendParameterEntitlement
+ _kIDSKeyTransparencyCacheClearRequestEntitlement
- _IDSIsFaceTimeOriMessageRegistration
CStrings:
+ "\x01\x15"
+ "\x03\x1a"
+ "\x0f\x02"
+ "\x14\x11\x12!\x11\x12!!!\xf0\xf3\x11\x11\x11\x117\x14C,"
+ "                     kt-opt-in: %@"
+ "(("
+ "07:56:13"
+ "?0"
+ "@\"<IDSXPCFirewall>\"32@0:8@\"NSString\"16@\"IDSDXPCDaemon\"24"
+ "Checking cache first to populate mergeIDs for handles {%@}"
+ "Client requested force disable account with unique ID %@ (Environtment: %@)"
+ "Client requested to reset error state."
+ "EchnidaEncryptionDisabled"
+ "Failed to query for handles {%@}"
+ "Failed to query for merge id due to unsuccessful request"
+ "Force disable account with uniqueID %@ login ID %@ service %@ called (Environment: %@) %@"
+ "Forgetting peer tokens for URI: %@ service: %@ for all registered URIs."
+ "IDSKeyTransparencyEndpointFilterComponent"
+ "IDSKeyTransparencyEndpointFilterParameter"
+ "Invalid groupID or sessionID!"
+ "KTMessageEnforcement"
+ "Key Transparency is disabled for service. { service: %@ }"
+ "Message using force query parameter but does not have appropriate entitlement! { messageID: %@, service: %@}"
+ "Missing required entitlement to send cache clear request. {connection: %@}"
+ "Network unavailable."
+ "Not opted into KT for service, no KT filtering needed. { service: %@ }"
+ "Nov 12 2023"
+ "Performing fetch for self verification info."
+ "Query for KT verification failed. { uriToError: %@ }"
+ "Reached rate limit for clearing query cache. { URI: %@, Service: %@ }"
+ "Received cache clear request for unsupported service. { service: %@ }"
+ "Received request from transparency to clear cache. { CacheClearRequest: %@ }"
+ "Recipient endpoint is not opted into KT. Will send to this endpoint. { service: %@, uri: %@, token: %@ }"
+ "Recipient endpoint is opted into KT and is not verified, will not send to this endpoint. { service: %@, uri: %@, token: %@ }"
+ "Recipient endpoint is opted into KT and this endpoint is verified. Will send to this endpoint. { service: %@, uri: %@, token: %@ }"
+ "Registration push manager kt opt out"
+ "Repairing registration on accounts in response to registration push for KT opt out."
+ "SecondaryEncryptionDisabled"
+ "SecondaryRegistrationDisabled"
+ "Serializing and persisting updates to KT registration data."
+ "Still need to query handles {%@}"
+ "T@\"IDSIDStatusQueryController\",&,N,V_idStatusQueryController"
+ "T@\"NSDictionary\",&,N,V_ktURIVerificationMap"
+ "T@\"NSMutableDictionary\",&,N,V_cacheClearRateLimiterByService"
+ "T@\"NSNumber\",&,N,V_quickRelayUserType"
+ "Tried to force disable an account we don't know about, ignoring..."
+ "Tried to force disable an account with no unique ID, ignoring..."
+ "URIToQueryFrom:withPreferredFromURI:"
+ "_cacheClearRateLimiterByService"
+ "_clientChannelLock"
+ "_forceDisableAccountWithUniqueID:"
+ "_forceDisablePrimaryAccountWithUniqueID:"
+ "_handleKTOptOutActionForAllAccounts"
+ "_idStatusQueryController"
+ "_isKeyTransparencyDisabledViaServerBagProtocolVersion_FaceTime"
+ "_isKeyTransparencyDisabledViaServerBagProtocolVersion_Madrid"
+ "_isKeyTransparencyDisabledViaServerBagProtocolVersion_Multiplex"
+ "_ktURIVerificationMap"
+ "_queueMessage:service:dataToEncrypt:withEncryptedAttributes:fromID:fromIdentity:toID:toURIs:originallyToURIs:ktURIVerificationMap:canUseLargePayload:sendOnePerToken:registrationProperties:fakeMessage:alwaysSkipSelf:alwaysIncludeSelf:forceQuery:disallowRefresh:prioritizedTokenList:wantsFirewallDonation:destinationObject:willSendBlock:completionBlock:fromCoalesceQueue:"
+ "_quickRelayUserType"
+ "_sendFanoutMessage:account:toGroupMembers:fromURI:command:commandContext:toGroup:sessionID:reason:waitForMadridAcks:isUPlusOne:isInitiator:quickRelayUserType:requiredCapabilites:requiredLackOfCapabilities:completionBlock:"
+ "_sendFanoutMessage:account:toGroupMembers:fromURI:command:toGroup:sessionID:reason:isUPlusOne:isInitiator:quickRelayUserType:"
+ "_sendFanoutMessage:account:toGroupMembers:fromURI:command:toGroup:sessionID:reason:isUPlusOne:isInitiator:quickRelayUserType:requiredCapabilites:requiredLackOfCapabilities:"
+ "_sendMessage:dataToEncrypt:withEncryptedAttributes:onService:fromID:fromIdentity:toID:toURIs:canUseLargePayload:sendOnePerToken:allowPartialSendsToSucceed:registrationProperties:fakeMessage:alwaysSkipSelf:alwaysIncludeSelf:forceQuery:disallowRefresh:prioritizedTokenList:wantsFirewallDonation:destinationObject:willSendBlock:completionBlock:firstAttemptDate:ktURIVerificationMap:fromCoalesceQueue:withQueryCompletion:"
+ "_sendMessageDictionary:lastRetryInterval:dataToEncrypt:withEncryptedAttributes:onService:wantsResponse:canUseLargePayload:sendOnePerToken:allowPartialSendsToSucceed:highPriority:fireAndForget:expirationDate:enforceRemoteTimeouts:messageID:fromID:fromIdentity:toID:toURIs:accessToken:topic:registrationProperties:fakeMessage:alwaysSkipSelf:alwaysIncludeSelf:forceQuery:pushPriority:ignoreMaxRetryCount:disallowRefresh:originalTimestamp:prioritizedTokenList:wantsFirewallDonation:destinationObject:deliveryMinimumTimeDelay:sendMode:KTURIVerificationMap:ackBlock:willSendBlock:sendCompletionBlock:"
+ "_shouldDisableEchnidaEncryption"
+ "_shouldDisableEncryption:UserDefaultKey:"
+ "cacheClearRateLimiterByService"
+ "cacheClearRequest:"
+ "clientMultiplexerForIdentifier:"
+ "delivery_keyTransparency"
+ "failed to extract mki from payload, cannot report metrics"
+ "firewallCollaboratorForService:forXPCDaemon:"
+ "firewallCollaboratorForService:withCompletion:"
+ "forceDisableAccount %@ localObject %@"
+ "forceDisableAccount:"
+ "forceDisableAccount:messageContext:"
+ "forceDisableAccountWithUniqueID:"
+ "forceQuery"
+ "forgetPeerTokensForURI:service:"
+ "ids-disable-echnida-encryption"
+ "initWithService:queue:connection:"
+ "initWithTransparencyVerifier:"
+ "initWithVerifierResult:ticket:accountKey:queryResponseTime:ktOptIn:"
+ "keyTransparencyURIVerificationMap"
+ "kt-clear-cache-request-limit"
+ "kt-clear-cache-request-limit-time"
+ "kt-min-idv-ft"
+ "kt-min-idv-im"
+ "kt-min-idv-mp1"
+ "ktCacheClearRequestLimit"
+ "ktCacheClearRequestLimitTime"
+ "ktOptIn"
+ "ktURIVerificationMap"
+ "noteDidRegisterKTData:forKeyIndex:"
+ "notePublicIdentityDidRegisterLegacyData:ngmIdentityData:ngmPrekeyData:keyIndexToIdentityData:"
+ "prefixedAliasStringToQueryFrom:withPreferredFromURI:"
+ "quickRelayUserType"
+ "receivedFromGFT2"
+ "requestContexts"
+ "resetErrorState"
+ "sendMessageDictionary:messageID:dataToEncrypt:withEncryptedAttributes:onService:wantsResponse:expirationDate:enforceRemoteTimeouts:canUseLargePayload:sendOnePerToken:allowPartialSendsToSucceed:priority:fireAndForget:fromID:fromIdentity:toURIs:accessToken:topic:registrationProperties:fakeMessage:alwaysSkipSelf:alwaysIncludeSelf:forceQuery:pushPriority:ignoreMaxRetryCount:disallowRefresh:originalTimestamp:prioritizedTokenList:wantsFirewallDonation:destinationObject:deliveryMinimumTimeDelay:sendMode:KTURIVerificationMap:ackBlock:willSendBlock:sendCompletionBlock:"
+ "setBTOutOfBandKey:forCBUUID:"
+ "setCacheClearRateLimiterByService:"
+ "setClientMultiplexer:forIdentifier:"
+ "setIdStatusQueryController:"
+ "setKtURIVerificationMap:"
+ "setMultiplexer:forIdentifier:"
+ "setQuickRelayUserType:"
+ "setQuickRelayUserTypeForSession %u"
+ "setQuickRelayUserTypeForSession called for session: %@ with userType: %u"
+ "setQuickRelayUserTypeForSession:"
+ "setQuickRelayUserTypeForSession:withUserType:"
+ "setQuickRelayUserTypeForSession:withUserType:messageContext:"
+ "should-clear-id-status-on-130"
+ "v112@0:8@16@24@32@40q48@56@64C72B76@80@88@96@104"
+ "v132@0:8@16@24@32@40q48@56@64@72C80B84B88@92@100@108@116@?124"
+ "v176@0:8@16@24@32@40@48@56@64@72@80@88B96B100@104B112B116B120q124B132@136B144@148@?156@?164B172"
+ "v188@0:8@16@24@32@40@48@56@64@72B80B84B88@92B100B104B108q112B120@124B132@136@?144@?152@160@168B176@?180"
+ "v24@0:8@\"IDSCacheClearRequest\"16"
+ "v256@0:8@16@24@32@40@48B56@60B68B72B76B80q84B92@96@104@112@120@128@136B144B148B152q156@164B172B176@180@188B196@200@208@216@224@?232@?240@?248"
+ "v268@0:8@16d24@32@40@48B56B60B64B68B72B76@80B88@92@100@108@116@124@132@140@148B156B160B164q168@176B184B188@192@200B208@212@220@228@236@?244@?252@?260"
+ "v28@0:8@\"NSString\"16S24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"<IDSXPCFirewall>\"@\"NSError\">24"
+ "v96@0:8@16@24@32@40q48@56@64C72B76@80@88"
+ "verifiedPushTokens"
- "\x01\x14"
- "\x03\x19"
- "\x0f\x01"
- "\x14\x11\x12\x11\x11\x12!!!\xf0\xf3\x11\x11\x11\x117\x14C,"
- "%s _cbuuidToBTOutOfBandKeyDictionary is not initialized"
- "'("
- "-[IDSGroupAgent registerAgent]_block_invoke"
- "20:46:27"
- "@\"<IDSXPCFirewall>\"24@0:8@\"IDSDXPCDaemon\"16"
- "Apple ID account is not registered for service. Cannot perform self verification."
- "Found endpoints for handles {%@} out of requested handles {%@}"
- "Getting endpoints for handles {%@}"
- "No registered account matching fromID: %@, bailing..."
- "Oct  6 2023"
- "URIToQueryFrom:"
- "_isKeyTransparencyDisabledViaServerBag"
- "_queueMessage:service:dataToEncrypt:withEncryptedAttributes:fromID:fromIdentity:toID:toURIs:originallyToURIs:canUseLargePayload:sendOnePerToken:registrationProperties:fakeMessage:alwaysSkipSelf:alwaysIncludeSelf:disallowRefresh:prioritizedTokenList:wantsFirewallDonation:destinationObject:willSendBlock:completionBlock:fromCoalesceQueue:"
- "_sendFanoutMessage:account:toGroupMembers:fromURI:command:commandContext:toGroup:sessionID:reason:waitForMadridAcks:isUPlusOne:isInitiator:requiredCapabilites:requiredLackOfCapabilities:completionBlock:"
- "_sendFanoutMessage:account:toGroupMembers:fromURI:command:toGroup:sessionID:reason:isUPlusOne:isInitiator:"
- "_sendFanoutMessage:account:toGroupMembers:fromURI:command:toGroup:sessionID:reason:isUPlusOne:isInitiator:requiredCapabilites:requiredLackOfCapabilities:"
- "_sendMessage:dataToEncrypt:withEncryptedAttributes:onService:fromID:fromIdentity:toID:toURIs:canUseLargePayload:sendOnePerToken:allowPartialSendsToSucceed:registrationProperties:fakeMessage:alwaysSkipSelf:alwaysIncludeSelf:disallowRefresh:prioritizedTokenList:wantsFirewallDonation:destinationObject:willSendBlock:completionBlock:firstAttemptDate:fromCoalesceQueue:withQueryCompletion:"
- "_sendMessageDictionary:lastRetryInterval:dataToEncrypt:withEncryptedAttributes:onService:wantsResponse:canUseLargePayload:sendOnePerToken:allowPartialSendsToSucceed:highPriority:fireAndForget:expirationDate:enforceRemoteTimeouts:messageID:fromID:fromIdentity:toID:toURIs:accessToken:topic:registrationProperties:fakeMessage:alwaysSkipSelf:alwaysIncludeSelf:pushPriority:ignoreMaxRetryCount:disallowRefresh:originalTimestamp:prioritizedTokenList:wantsFirewallDonation:destinationObject:deliveryMinimumTimeDelay:sendMode:ackBlock:willSendBlock:sendCompletionBlock:"
- "com.apple.security.IDSEncryption.SecondaryEncryptionDisabled"
- "com.apple.security.IDSEncryption.SecondaryRegistrationDisabled"
- "firewallCollaboratorForXPCDaemon:"
- "firewallCollaboratorWithCompletion:"
- "initWithVerifierResult:ticket:accountKey:queryResponseTime:"
- "kt-disabled-v2"
- "notePublicIdentityDidRegisterLegacyData:ngmIdentityData:ngmPrekeyData:keyIndexToIdentityData:keyIndexToKTRegData:"
- "prefixedAliasStringToQueryFrom:"
- "refreshIDInfo"
- "resolve_handler: could not create session; Enable the IDSGroupAgentSessionControlFlow feature flag."
- "sendMessageDictionary:messageID:dataToEncrypt:withEncryptedAttributes:onService:wantsResponse:expirationDate:enforceRemoteTimeouts:canUseLargePayload:sendOnePerToken:allowPartialSendsToSucceed:priority:fireAndForget:fromID:fromIdentity:toURIs:accessToken:topic:registrationProperties:fakeMessage:alwaysSkipSelf:alwaysIncludeSelf:pushPriority:ignoreMaxRetryCount:disallowRefresh:originalTimestamp:prioritizedTokenList:wantsFirewallDonation:destinationObject:deliveryMinimumTimeDelay:sendMode:ackBlock:willSendBlock:sendCompletionBlock:"
- "v104@0:8@16@24@32@40q48@56@64C72B76@80@88@96"
- "v124@0:8@16@24@32@40q48@56@64@72C80B84B88@92@100@108@?116"
- "v160@0:8@16@24@32@40@48@56@64@72@80B88B92@96B104B108B112B116@120B128@132@?140@?148B156"
- "v172@0:8@16@24@32@40@48@56@64@72B80B84B88@92B100B104B108B112@116B124@128@?136@?144@152B160@?164"
- "v240@0:8@16@24@32@40@48B56@60B68B72B76B80q84B92@96@104@112@120@128@136B144B148B152@156B164B168@172@180B188@192@200@208@?216@?224@?232"
- "v24@0:8@?<v@?@\"<IDSXPCFirewall>\"@\"NSError\">16"
- "v252@0:8@16d24@32@40@48B56B60B64B68B72B76@80B88@92@100@108@116@124@132@140@148B156B160B164@168B176B180@184@192B200@204@212@220@?228@?236@?244"
- "v88@0:8@16@24@32@40q48@56@64C72B76@80"

```
