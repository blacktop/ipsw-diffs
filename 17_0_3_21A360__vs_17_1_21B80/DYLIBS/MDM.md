## MDM

> `/System/Library/PrivateFrameworks/MDM.framework/MDM`

```diff

-3.26.0.0.0
-  __TEXT.__text: 0x3a724
+3.26.2.3.0
+  __TEXT.__text: 0x3a9b0
   __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_methlist: 0x2100
+  __TEXT.__objc_methlist: 0x2128
   __TEXT.__const: 0x98
-  __TEXT.__gcc_except_tab: 0xa44
-  __TEXT.__cstring: 0x3b87
-  __TEXT.__oslogstring: 0x42b1
+  __TEXT.__gcc_except_tab: 0xa4c
+  __TEXT.__cstring: 0x3bec
+  __TEXT.__oslogstring: 0x42de
   __TEXT.__dlopen_cstrs: 0x55
   __TEXT.__unwind_info: 0xb68
   __TEXT.__objc_classname: 0x37c
-  __TEXT.__objc_methname: 0x9e94
+  __TEXT.__objc_methname: 0x9f9a
   __TEXT.__objc_methtype: 0x10b8
-  __TEXT.__objc_stubs: 0x86a0
-  __DATA_CONST.__got: 0x968
-  __DATA_CONST.__const: 0x1530
+  __TEXT.__objc_stubs: 0x8740
+  __DATA_CONST.__got: 0x980
+  __DATA_CONST.__const: 0x1558
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3728
-  __DATA_CONST.__objc_selrefs: 0x2428
+  __DATA_CONST.__objc_const: 0x3758
+  __DATA_CONST.__objc_selrefs: 0x2450
   __DATA_CONST.__objc_arraydata: 0x68
   __AUTH_CONST.__objc_const: 0xa30
-  __AUTH_CONST.__cfstring: 0x4260
+  __AUTH_CONST.__cfstring: 0x42c0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__auth_got: 0x5b8
   __AUTH.__objc_data: 0x6e0
   __DATA.__objc_protorefs: 0x20
-  __DATA.__objc_classrefs: 0x558
+  __DATA.__objc_classrefs: 0x560
   __DATA.__objc_superrefs: 0x50
-  __DATA.__objc_ivar: 0x19c
+  __DATA.__objc_ivar: 0x1a0
   __DATA.__data: 0x5a0
   __DATA.__bss: 0x198
   __DATA_DIRTY.__objc_data: 0x140

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
-  Functions: 952
-  Symbols:   4369
-  CStrings:  2597
+  Functions: 955
+  Symbols:   4386
+  CStrings:  2608
 
Symbols:
+ -[MDMServerCore _memberQueueLogLatestPushTokenIfNeeded:]
+ -[MDMServerCore memberQueueLastLoggedPushToken]
+ -[MDMServerCore setMemberQueueLastLoggedPushToken:]
+ GCC_except_table127
+ GCC_except_table129
+ GCC_except_table134
+ GCC_except_table145
+ GCC_except_table150
+ GCC_except_table196
+ GCC_except_table207
+ GCC_except_table211
+ GCC_except_table221
+ GCC_except_table225
+ GCC_except_table241
+ _DMCEventsTopicPushToken
+ _DMCEventsTopicServerResponse
+ _MCInstallationErrorDomain
+ _OBJC_CLASS_$_DMCEvents
+ _OBJC_IVAR_$_MDMServerCore._memberQueueLastLoggedPushToken
+ ___41-[MDMServerCore uprootMDMWithCompletion:]_block_invoke.117
+ ___50-[MDMServerCore connection:didReceivePublicToken:]_block_invoke.222
+ ___50-[MDMServerCore connection:didReceivePublicToken:]_block_invoke_2.223
+ ___50-[MDMServerCore connection:didReceivePublicToken:]_block_invoke_2.224
+ ___55-[MDMServerCore _executeBlockWhenPushTokenIsAvailable:]_block_invoke.211
+ ___61-[MDMServerCore requestInstallOfAppsInRestoreWithCompletion:]_block_invoke.189
+ ___62-[MDMServerCore _executionQueueRemoveMDMProfileWithAssertion:]_block_invoke.237
+ ___63-[MDMServerCore connection:didReceiveMessageForTopic:userInfo:]_block_invoke.228
+ ___63-[MDMServerCore connection:didReceiveMessageForTopic:userInfo:]_block_invoke.230
+ ___72-[MDMServerCore _executionQueueHandleRequest:assertion:completionBlock:]_block_invoke.95
+ ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke.77
+ ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke.82
+ ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke_2.83
+ ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke_3.88
+ ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.76
+ ___block_descriptor_64_e8_32s40s48s56r_e5_v8?0ls32l8s40l8s48l8r56l8
+ ___block_literal_global.240
+ ___block_literal_global.294
+ _objc_msgSend$_memberQueueLogLatestPushTokenIfNeeded:
+ _objc_msgSend$logErrorEventForTopic:reason:error:details:
+ _objc_msgSend$logRegularEventForTopic:reason:details:
+ _objc_msgSend$memberQueueLastLoggedPushToken
+ _objc_msgSend$setMemberQueueLastLoggedPushToken:
- GCC_except_table126
- GCC_except_table128
- GCC_except_table133
- GCC_except_table144
- GCC_except_table149
- GCC_except_table195
- GCC_except_table206
- GCC_except_table210
- GCC_except_table220
- GCC_except_table224
- GCC_except_table240
- ___41-[MDMServerCore uprootMDMWithCompletion:]_block_invoke.113
- ___50-[MDMServerCore connection:didReceivePublicToken:]_block_invoke.212
- ___50-[MDMServerCore connection:didReceivePublicToken:]_block_invoke_2.213
- ___50-[MDMServerCore connection:didReceivePublicToken:]_block_invoke_2.214
- ___55-[MDMServerCore _executeBlockWhenPushTokenIsAvailable:]_block_invoke.207
- ___61-[MDMServerCore requestInstallOfAppsInRestoreWithCompletion:]_block_invoke.185
- ___62-[MDMServerCore _executionQueueRemoveMDMProfileWithAssertion:]_block_invoke.224
- ___63-[MDMServerCore connection:didReceiveMessageForTopic:userInfo:]_block_invoke.218
- ___63-[MDMServerCore connection:didReceiveMessageForTopic:userInfo:]_block_invoke.220
- ___72-[MDMServerCore _executionQueueHandleRequest:assertion:completionBlock:]_block_invoke.91
- ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke.73
- ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke.78
- ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke_2.79
- ___82-[MDMServerCore _executionQueuePollServerForCommandWithAssertion:completionBlock:]_block_invoke_3.84
- ___88-[MDMServerCore _executionQueueTellServerAboutDeviceTokenWithAssertion:completionBlock:]_block_invoke.72
- ___block_literal_global.227
- ___block_literal_global.281
CStrings:
+ "Failed to fetch eligible configuration with error: %{public}@"
+ "Failed to get device UDID from MobileGestalt"
+ "New Push Token Received"
+ "Received 401 / 403(code: Unrecognized) error from server"
+ "T\x1f\b#"
+ "T@\"NSData\",&,N,V_memberQueueLastLoggedPushToken"
+ "Token Update failed"
+ "_memberQueueLastLoggedPushToken"
+ "_memberQueueLogLatestPushTokenIfNeeded:"
+ "logErrorEventForTopic:reason:error:details:"
+ "logRegularEventForTopic:reason:details:"
+ "memberQueueLastLoggedPushToken"
+ "setMemberQueueLastLoggedPushToken:"
- "Failed to fetch eligible configuraiton with error: %{public}@"
- "T\x1f\a#"

```
