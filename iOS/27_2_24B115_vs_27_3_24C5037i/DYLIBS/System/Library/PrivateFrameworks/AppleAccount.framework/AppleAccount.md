## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`

```diff

-1069.125.7.0.0
-  __TEXT.__text: 0x19c830
+1069.250.3.0.0
+  __TEXT.__text: 0x19dcc4
   __TEXT.__lazy_helpers: 0xa8
-  __TEXT.__objc_methlist: 0xb59c
-  __TEXT.__cstring: 0x11552
-  __TEXT.__const: 0x10d60
-  __TEXT.__oslogstring: 0x13bdd
-  __TEXT.__gcc_except_tab: 0x1bf8
+  __TEXT.__objc_methlist: 0xb684
+  __TEXT.__cstring: 0x11722
+  __TEXT.__const: 0x10d70
+  __TEXT.__oslogstring: 0x13edd
+  __TEXT.__gcc_except_tab: 0x1c28
   __TEXT.__dlopen_cstrs: 0x325
   __TEXT.__swift5_typeref: 0x3a46
   __TEXT.__constg_swiftt: 0x2a50

   __TEXT.__swift_as_ret: 0x29c
   __TEXT.__swift_as_cont: 0x510
   __TEXT.__swift5_capture: 0x848
-  __TEXT.__unwind_info: 0x8200
+  __TEXT.__unwind_info: 0x8280
   __TEXT.__eh_frame: 0x77d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3fb0
+  __DATA_CONST.__const: 0x4050
   __DATA_CONST.__objc_classlist: 0x8b8
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5278
+  __DATA_CONST.__objc_selrefs: 0x5318
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x590
   __DATA_CONST.__objc_arraydata: 0xe0
   __DATA_CONST.__got: 0x1160
-  __AUTH_CONST.__const: 0xd460
-  __AUTH_CONST.__cfstring: 0xd760
-  __AUTH_CONST.__objc_const: 0x26bd8
+  __AUTH_CONST.__const: 0xd480
+  __AUTH_CONST.__cfstring: 0xd7e0
+  __AUTH_CONST.__objc_const: 0x26cc8
   __AUTH_CONST.__lazy_load_got: 0x10
-  __AUTH_CONST.__objc_intobj: 0x120
+  __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x1500
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0xbf0
+  __DATA.__objc_ivar: 0xc04
   __DATA.__data: 0x27fc
   __DATA.__common: 0xa8
   __DATA_DIRTY.__objc_data: 0x5cb0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9170
-  Symbols:   10029
-  CStrings:  3758
+  Functions: 9205
+  Symbols:   10073
+  CStrings:  3779
 
Symbols:
+ +[AAFeatureFlags isRemoteUITermsMigrationEnabled]
+ +[AAUrlBagHelper _completeWithRemoteUITermsFeatureFlagFallback:]
+ +[AAUrlBagHelper isRemoteUITermsEnabledWithCompletion:]
+ -[AAMessagingService _attachAckCompletionToCustodianMessage:context:]
+ -[AAMessagingService _beginInFlightMessageWithGUID:]
+ -[AAMessagingService _deliverInheritanceMessage:custodianMessage:]
+ -[AAMessagingService _endInFlightMessageWithGUID:]
+ -[AAMessagingService _faultIfStillPendingAfterDelay:]
+ -[AAMessagingService _optionsDictionaryWithResponseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:sendFromHandleUri:wantsDeliveryAcknowledgement:]
+ -[AAMessagingService _processDeliveredMessageIdentifier:transaction:]
+ -[AAMessagingService _processPendingDeliveredMessageIdentifiers]
+ -[AAMessagingService pendingDeliveredMessageIdentifiers]
+ -[AAMessagingService sendMessage:destinations:sendFromHandleUri:responseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:wantsDeliveryAcknowledgement:error:]
+ -[AAMessagingService service:account:identifier:hasBeenDeliveredWithContext:]
+ -[AAPendingIDSMessage ackCompletion]
+ -[AAPendingIDSMessage setAckCompletion:]
+ -[AAPendingIDSMessage setTransaction:]
+ -[AAPendingIDSMessage transaction]
+ -[AAURLSession _sessionQueue_dequeueTask:withResponse:headerFields:error:]
+ -[NSError(AppleAccount) aa_isAccountsDaemonConnectionError]
+ GCC_except_table56
+ GCC_except_table59
+ GCC_except_table62
+ _OBJC_IVAR_$_AAMessagingService._inFlightMessageGUIDs
+ _OBJC_IVAR_$_AAMessagingService._pendingDeliveredMessageIdentifiers
+ _OBJC_IVAR_$_AAMessagingService._pendingDeliveredTransaction
+ _OBJC_IVAR_$_AAPendingIDSMessage._ackCompletion
+ _OBJC_IVAR_$_AAPendingIDSMessage._transaction
+ __AAUrlBagRemoteUITermsConfigKey
+ __AAUrlBagRemoteUITermsEnabledKey
+ ___174-[AAMessagingService sendMessage:destinations:sendFromHandleUri:responseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:wantsDeliveryAcknowledgement:error:]_block_invoke
+ ___53-[AAMessagingService _faultIfStillPendingAfterDelay:]_block_invoke
+ ___55+[AAUrlBagHelper isRemoteUITermsEnabledWithCompletion:]_block_invoke
+ ___69-[AAMessagingService _attachAckCompletionToCustodianMessage:context:]_block_invoke
+ ___69-[AAMessagingService _attachAckCompletionToCustodianMessage:context:]_block_invoke_2
+ ___69-[AAMessagingService _processDeliveredMessageIdentifier:transaction:]_block_invoke
+ ___98-[AASignInFlowController _onqueue_validateAndEnrollCDPStateForAccount:withAuthResults:completion:]_block_invoke_2
+ ___98-[AASignInFlowController _onqueue_validateAndEnrollCDPStateForAccount:withAuthResults:completion:]_block_invoke_3
+ ___AARunOnce_block_invoke
+ ___block_descriptor_48_e8_32w40w_e5_v8?0lw32l8w40l8
+ ___block_descriptor_56_e8_32bs40r48r_e5_v8?0lr40l8r48l8s32l8
+ ___block_descriptor_64_e8_32s40s48s56w_e5_v8?0lw56l8s32l8s40l8s48l8
+ ___getIDSSendMessageOptionWantsClientAcknowledgementKeySymbolLoc_block_invoke
+ _getIDSSendMessageOptionWantsClientAcknowledgementKey
+ _getIDSSendMessageOptionWantsClientAcknowledgementKeySymbolLoc
+ _getIDSSendMessageOptionWantsClientAcknowledgementKeySymbolLoc.ptr
+ _kAAAnalyticsEventDeviceListCacheHit
+ _kAAAnalyticsEventDeviceListCacheMiss
+ _kAAAnalyticsEventDeviceListCacheValidation
+ _kAAPreflightSaveDaemonRetryDelay
- +[AAUrlBagHelper canRepairCustodian]
- -[AAMessagingService _optionsDictionaryWithResponseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:sendFromHandleUri:]
- -[AAURLSession _sessionQueue_dequeueTask:withResponse:error:]
- GCC_except_table61
- __AAUrlBagCanRepairCustodianKey
- ___145-[AAMessagingService sendMessage:destinations:sendFromHandleUri:responseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:error:]_block_invoke
CStrings:
+ "AAMessagingService: message %@ is already in flight. Ignoring the duplicate."
+ "AAMessagingService: message of type %ld still waits for its delegate after %lld s"
+ "Custodian delegate %@ does not handle delivery acknowledgements, dropping %@"
+ "Delivered message has an identifier that is not a UUID: %@"
+ "IDSSendMessageOptionWantsClientAcknowledgementKey"
+ "Message %@ has been delivered"
+ "MessagingService lost strong ref processing delivery acknowledgement"
+ "PreflightSave failed because accountsd went away, retrying once after a short delay..."
+ "RUI Terms: Failed to fetch RUI terms config from URL bag: %@"
+ "RUI Terms: Falling back to OS FeatureFlag: %d"
+ "RUI Terms: Returning remoteUITermsEnabled from urlbag: %@"
+ "RUI Terms: Unexpected config value type: %@"
+ "RUI Terms: remoteUITermsMigrationCfgs from urlbag: %@"
+ "RemoteUITermsMigration"
+ "Sending %@: %@ in response to %@, wants delivery acknowledgement: %@"
+ "Sending %@: %@, wants delivery acknowledgement: %@"
+ "Sending to %@"
+ "com.apple.aa.messaging.ack"
+ "com.apple.aa.messaging.delivered"
+ "com.apple.aa.messaging.incomingData"
+ "com.apple.appleaccount.deviceListCache.hit"
+ "com.apple.appleaccount.deviceListCache.miss"
+ "com.apple.appleaccount.deviceListCache.validation"
+ "remoteUITermsEnabled"
+ "remoteUITermsMigrationCfgs"
+ "typeof (((typeof (IDSSendMessageOptionWantsClientAcknowledgementKey) (*)(void))0)()) getIDSSendMessageOptionWantsClientAcknowledgementKey(void)"
+ "\x92"
- "DecoupleOTPeerID"
- "Returning canRepairCustodianV2 from urlbag: %@"
- "Sending %@: %@ to %@"
- "Sending %@: %@ to %@ in response to %@"
- "b"
- "canRepairCustodianV2"
```
