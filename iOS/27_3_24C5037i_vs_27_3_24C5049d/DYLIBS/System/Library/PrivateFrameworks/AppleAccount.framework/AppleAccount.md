## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`

```diff

-1069.250.3.0.0
-  __TEXT.__text: 0x19dcc4
+1069.250.6.0.0
+  __TEXT.__text: 0x19f4f0
   __TEXT.__lazy_helpers: 0xa8
-  __TEXT.__objc_methlist: 0xb684
-  __TEXT.__cstring: 0x11722
-  __TEXT.__const: 0x10d70
-  __TEXT.__oslogstring: 0x13edd
-  __TEXT.__gcc_except_tab: 0x1c28
+  __TEXT.__objc_methlist: 0xb79c
+  __TEXT.__cstring: 0x11b02
+  __TEXT.__const: 0x10dc0
+  __TEXT.__oslogstring: 0x13fdd
+  __TEXT.__gcc_except_tab: 0x1c78
   __TEXT.__dlopen_cstrs: 0x325
   __TEXT.__swift5_typeref: 0x3a46
   __TEXT.__constg_swiftt: 0x2a50

   __TEXT.__swift5_fieldmd: 0x262c
   __TEXT.__swift5_builtin: 0x190
   __TEXT.__swift5_assocty: 0x3f0
-  __TEXT.__swift5_proto: 0xc70
+  __TEXT.__swift5_proto: 0xc74
   __TEXT.__swift5_types: 0x34c
   __TEXT.__swift5_mpenum: 0x6c
   __TEXT.__swift5_protos: 0x4c

   __TEXT.__swift_as_ret: 0x29c
   __TEXT.__swift_as_cont: 0x510
   __TEXT.__swift5_capture: 0x848
-  __TEXT.__unwind_info: 0x8280
+  __TEXT.__unwind_info: 0x8320
   __TEXT.__eh_frame: 0x77d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x4050
-  __DATA_CONST.__objc_classlist: 0x8b8
+  __DATA_CONST.__const: 0x4110
+  __DATA_CONST.__objc_classlist: 0x8c0
   __DATA_CONST.__objc_catlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x260
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5318
+  __DATA_CONST.__objc_selrefs: 0x5398
   __DATA_CONST.__objc_protorefs: 0xe0
-  __DATA_CONST.__objc_superrefs: 0x590
+  __DATA_CONST.__objc_superrefs: 0x598
   __DATA_CONST.__objc_arraydata: 0xe0
-  __DATA_CONST.__got: 0x1160
+  __DATA_CONST.__got: 0x1168
   __AUTH_CONST.__const: 0xd480
-  __AUTH_CONST.__cfstring: 0xd7e0
-  __AUTH_CONST.__objc_const: 0x26cc8
+  __AUTH_CONST.__cfstring: 0xd9c0
+  __AUTH_CONST.__objc_const: 0x26f00
   __AUTH_CONST.__lazy_load_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__auth_got: 0x1500
-  __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0xc04
-  __DATA.__data: 0x27fc
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0xc28
+  __DATA.__data: 0x281c
   __DATA.__common: 0xa8
   __DATA_DIRTY.__objc_data: 0x5cb0
   __DATA_DIRTY.__data: 0x3000

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9205
-  Symbols:   10073
-  CStrings:  3779
+  Functions: 9246
+  Symbols:   10132
+  CStrings:  3801
 
Symbols:
+ +[NSError(AppleAccount) aa_cloudKitErrorForXPCReply:]
+ -[AACustodianController repairCustodians:telemetryFlowID:completion:]
+ -[AAFollowUpController _verifyTermsCFUMessageWithUserInfo:]
+ -[AAMessagingService _invokeSendResultHandler:withOutcome:]
+ -[AAMessagingService _reportedErrorForIDSSendError:]
+ -[AAMessagingService _sendMessage:destinations:sendFromHandleUri:responseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:wantsDeliveryAcknowledgement:sendResultHandler:error:]
+ -[AAMessagingService aliasUris:containSenderAliasUri:]
+ -[AAMessagingService canSend]
+ -[AAMessagingService isRegisteredSenderAliasUri:]
+ -[AAMessagingService registerSendResultHandler:forIdentifier:]
+ -[AAMessagingService requiredReachabilityForDestination:completion:]
+ -[AAMessagingService sendMessage:destinations:sendFromHandleUri:responseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:sendResultHandler:error:]
+ -[AASendResultOutcome .cxx_destruct]
+ -[AASendResultOutcome error]
+ -[AASendResultOutcome initWithSuccess:error:]
+ -[AASendResultOutcome success]
+ GCC_except_table117
+ GCC_except_table53
+ GCC_except_table73
+ GCC_except_table76
+ GCC_except_table90
+ GCC_except_table95
+ _AAFollowUpUserInfoAccountUsername
+ _AAFollowUpUserInfoTelemetryFlowID
+ _AAStoreBoundedLocked
+ _OBJC_CLASS_$_AASendResultOutcome
+ _OBJC_IVAR_$_AAMessagingService._earlySendResultOrder
+ _OBJC_IVAR_$_AAMessagingService._earlySendResults
+ _OBJC_IVAR_$_AAMessagingService._reachabilityQueryTimeout
+ _OBJC_IVAR_$_AAMessagingService._sendResultHandlerLock
+ _OBJC_IVAR_$_AAMessagingService._sendResultHandlerOrder
+ _OBJC_IVAR_$_AAMessagingService._sendResultHandlers
+ _OBJC_IVAR_$_AAMessagingService._sendResultQueue
+ _OBJC_IVAR_$_AASendResultOutcome._error
+ _OBJC_IVAR_$_AASendResultOutcome._success
+ _OBJC_METACLASS_$_AASendResultOutcome
+ __OBJC_$_INSTANCE_METHODS_AASendResultOutcome
+ __OBJC_$_INSTANCE_VARIABLES_AASendResultOutcome
+ __OBJC_$_PROP_LIST_AASendResultOutcome
+ __OBJC_CLASS_RO_$_AASendResultOutcome
+ __OBJC_METACLASS_RO_$_AASendResultOutcome
+ ___193-[AAMessagingService _sendMessage:destinations:sendFromHandleUri:responseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:wantsDeliveryAcknowledgement:sendResultHandler:error:]_block_invoke
+ ___59-[AAMessagingService _invokeSendResultHandler:withOutcome:]_block_invoke
+ ___68-[AAMessagingService requiredReachabilityForDestination:completion:]_block_invoke
+ ___68-[AAMessagingService requiredReachabilityForDestination:completion:]_block_invoke_2
+ ___69-[AACustodianController repairCustodians:telemetryFlowID:completion:]_block_invoke
+ ___block_descriptor_48_e8_32bs40r_e8_v16?0q8lr40l8s32l8
+ ___block_descriptor_56_e8_32bs40r48r_e8_v12?0B8lr40l8r48l8s32l8
+ ___block_descriptor_56_e8_32bs40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_57_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ ___getFLNotificationOptionNotificationCenterSymbolLoc_block_invoke
+ ___getIDSErrorDomainSymbolLoc_block_invoke
+ _associated conformance 12AppleAccount17AADeviceListErrorO10Foundation13CustomNSErrorAAs0E0
+ _getFLNotificationOptionNotificationCenterSymbolLoc.ptr
+ _getIDSErrorDomain
+ _getIDSErrorDomainSymbolLoc
+ _getIDSErrorDomainSymbolLoc.ptr
+ _kAAAnalyticsEventCustodianHealthCheckOwnerCleanupPhantomCustodian
+ _kAAAnalyticsEventCustodianSetupSuccessFamily
+ _kAAAnalyticsEventCustodianSetupSuccessFamilyUnknown
+ _kAAAnalyticsEventCustodianSetupSuccessNonFamily
+ _kAAAnalyticsEventSetupFailSafePendingFamily
+ _kAAAnalyticsEventSetupFailSafePendingFamilyUnknown
+ _kAAAnalyticsEventSetupFailSafePendingNonFamily
+ _kAAAnalyticsEventSetupFailSafeReadyFamily
+ _kAAAnalyticsEventSetupFailSafeReadyFamilyUnknown
+ _kAAAnalyticsEventSetupFailSafeReadyNonFamily
- GCC_except_table116
- GCC_except_table120
- GCC_except_table48
- GCC_except_table89
- GCC_except_table94
- ___174-[AAMessagingService sendMessage:destinations:sendFromHandleUri:responseIdentifier:fireAndForget:requiredCapabilities:lackingCapabilities:wantsDeliveryAcknowledgement:error:]_block_invoke
- ___53-[AACustodianController repairCustodians:completion:]_block_invoke
- ___block_descriptor_56_e8_32bs40r48r_e5_v8?0lr40l8r48l8s32l8
CStrings:
+ "AAMessagingService: the custodian delegate declined the IDS ack. The sender gets no delivery acknowledgment."
+ "CKErrorDomain"
+ "FLNotificationOptionNotificationCenter"
+ "FOLLOWUP_VERIFY_TERMS_ACCOUNT_MESSAGE"
+ "IDSErrorDomain"
+ "NSString *getFLNotificationOptionNotificationCenter(void)"
+ "No messaging destination for the handle. Reporting not registered."
+ "The IDS reachability query did not complete in %.1f seconds. Reporting Unknown."
+ "accountUsername"
+ "com.apple.AAMessaging.sendResult"
+ "com.apple.appleaccount.custodian.healthcheck.owner.cleanupPhantomCustodian"
+ "com.apple.appleaccount.custodian.setup.success.family"
+ "com.apple.appleaccount.custodian.setup.success.familyUnknown"
+ "com.apple.appleaccount.custodian.setup.success.nonFamily"
+ "com.apple.appleaccount.custodian.setupFailSafe.pending.family"
+ "com.apple.appleaccount.custodian.setupFailSafe.pending.familyUnknown"
+ "com.apple.appleaccount.custodian.setupFailSafe.pending.nonFamily"
+ "com.apple.appleaccount.custodian.setupFailSafe.ready.family"
+ "com.apple.appleaccount.custodian.setupFailSafe.ready.familyUnknown"
+ "com.apple.appleaccount.custodian.setupFailSafe.ready.nonFamily"
+ "prefs:root=APPLE_ACCOUNT&aaaction=accountRecovery"
+ "telemetryFlowID"
+ "typeof (((typeof (IDSErrorDomain) (*)(void))0)()) getIDSErrorDomain(void)"
- "\x92"
```
