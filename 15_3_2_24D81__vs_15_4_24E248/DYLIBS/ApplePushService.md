## ApplePushService

> `/System/Library/PrivateFrameworks/ApplePushService.framework/Versions/A/ApplePushService`

```diff

-1100.400.110.0.0
-  __TEXT.__text: 0x2a3a8
-  __TEXT.__auth_stubs: 0xd60
-  __TEXT.__objc_methlist: 0x194c
+1100.500.181.0.0
+  __TEXT.__text: 0x2ac1c
+  __TEXT.__auth_stubs: 0xd70
+  __TEXT.__objc_methlist: 0x1b4c
   __TEXT.__const: 0x120
   __TEXT.__gcc_except_tab: 0x5a0
-  __TEXT.__oslogstring: 0x34bf
-  __TEXT.__cstring: 0x22ec
+  __TEXT.__oslogstring: 0x35ed
+  __TEXT.__cstring: 0x2356
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0xa18
+  __TEXT.__unwind_info: 0xa58
   __TEXT.__objc_classname: 0x20f
-  __TEXT.__objc_methname: 0x3a8f
+  __TEXT.__objc_methname: 0x3aec
   __TEXT.__objc_methtype: 0x64b
-  __TEXT.__objc_stubs: 0x2a40
+  __TEXT.__objc_stubs: 0x2a80
   __DATA_CONST.__got: 0x278
-  __DATA_CONST.__const: 0x688
+  __DATA_CONST.__const: 0x6a0
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1118
+  __DATA_CONST.__objc_selrefs: 0x11b0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x78
-  __AUTH_CONST.__auth_got: 0x6c0
-  __AUTH_CONST.__const: 0x1288
-  __AUTH_CONST.__cfstring: 0x20e0
-  __AUTH_CONST.__objc_const: 0x3470
+  __AUTH_CONST.__auth_got: 0x6c8
+  __AUTH_CONST.__const: 0x12b8
+  __AUTH_CONST.__cfstring: 0x2140
+  __AUTH_CONST.__objc_const: 0x3108
   __AUTH.__objc_data: 0x730
   __DATA.__objc_ivar: 0x168
   __DATA.__data: 0x280

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 820562EA-8690-3F82-85F4-1B29DA257742
-  Functions: 1036
-  Symbols:   2385
-  CStrings:  1808
+  UUID: 66038D7B-96AA-3DBE-B544-0D4D1A0A5907
+  Functions: 1081
+  Symbols:   2441
+  CStrings:  1824
 
Symbols:
+ +[APSConnection _blockingXPCCallWithArgumentBlock:resultHandler:timeout:].cold.2
+ +[APSConnection geoRegion].cold.1
+ +[APSConnection serverTimeInNanoSeconds].cold.1
+ +[APSLog PUSHTRACE].cold.1
+ +[APSLog activityTracking].cold.1
+ +[APSLog alert].cold.1
+ +[APSLog certificate].cold.1
+ +[APSLog connectionServer].cold.1
+ +[APSLog connection].cold.1
+ +[APSLog courierOversized].cold.1
+ +[APSLog courier].cold.1
+ +[APSLog daemon].cold.1
+ +[APSLog database].cold.1
+ +[APSLog main].cold.1
+ +[APSLog networking].cold.1
+ +[APSLog nonce].cold.1
+ +[APSLog power].cold.1
+ +[APSLog preference].cold.1
+ +[APSLog protocolParserDetailed].cold.1
+ +[APSLog protocolParser].cold.1
+ +[APSLog proxy].cold.1
+ +[APSLog pubSub].cold.1
+ +[APSLog pushHistory].cold.1
+ +[APSLog shouldPowerLogEvent:].cold.1
+ +[APSLog simulator].cold.1
+ +[APSLog stream].cold.1
+ +[APSLog taskManager].cold.1
+ +[APSLog telemetry].cold.1
+ +[APSLog topicManagerOversized].cold.1
+ +[APSLog topicManager].cold.1
+ +[APSLog ttlCollection].cold.1
+ +[APSLog xpc].cold.1
+ +[APSMultiUserFS sharedInstance].cold.1
+ +[APSPreferences preferences].cold.1
+ +[APSSystemUser systemUserWithUserID:].cold.1
+ -[APSConnection forceClientIdentityProviderSwapWithCompletion:]
+ -[APSConnection hasIdentity].cold.1
+ -[APSConnection rollTokensAndReconnect:]
+ -[APSSystemUser initWithUserID:].cold.3
+ APSPowerLog.cold.1
+ APSPubSubPowerLog.cold.1
+ APSPubSubPowerLog.cold.2
+ GCC_except_table229
+ GCC_except_table232
+ GCC_except_table298
+ GCC_except_table323
+ GCC_except_table335
+ GCC_except_table341
+ GCC_except_table344
+ _APSForceMacSleep
+ _APSRollTokenEntitlement
+ _APSUseMultiIdentityProvider
+ __33-[APSConnection _deliverMessage:]_block_invoke.125
+ __39-[APSConnection _deliverToken:forInfo:]_block_invoke.154
+ __40-[APSConnection rollTokensAndReconnect:]_block_invoke.107
+ __42-[APSConnection _deliverURLToken:forInfo:]_block_invoke.157
+ __43-[APSConnection _sendOutgoingMessage:fake:]_block_invoke.227
+ __44-[APSConnection rollBAACertsWithCompletion:]_block_invoke.106
+ __46-[APSConnection subscribeToChannels:forTopic:]_block_invoke.271
+ __47-[APSConnection _deliverURLTokenError:forInfo:]_block_invoke.160
+ __50-[APSConnection registeredChannelsForTopic:error:]_block_invoke.292
+ __50-[APSConnection registeredChannelsForTopic:error:]_block_invoke.293
+ __51-[APSConnection _deliverToken:forTopic:identifier:]_block_invoke.149
+ __51-[APSConnection requestURLTokenForInfo:completion:]_block_invoke.248
+ __51-[APSConnection requestURLTokenForInfo:completion:]_block_invoke.248.cold.1
+ __54+[APSConnection _nonblockingXPCCallWithArgumentBlock:]_block_invoke.318
+ __54+[APSConnection _nonblockingXPCCallWithArgumentBlock:]_block_invoke.321
+ __54-[APSConnection invalidateURLTokenForInfo:completion:]_block_invoke.259
+ __54-[APSConnection invalidateURLTokenForInfo:completion:]_block_invoke.259.cold.1
+ __54-[APSConnection invalidateURLTokenForInfo:completion:]_block_invoke.263
+ __54-[APSConnection invalidateURLTokenForInfo:completion:]_block_invoke.263.cold.1
+ __59-[APSConnection signDataWithDeviceIdentity:withCompletion:]_block_invoke.100
+ __60-[APSConnection _deliverFailedChannelSubscriptions:onTopic:]_block_invoke.300
+ __62-[APSConnection getRegisteredChannelsForTopic:withCompletion:]_block_invoke.277
+ __62-[APSConnection getRegisteredChannelsForTopic:withCompletion:]_block_invoke.282
+ __62-[APSConnection getRegisteredChannelsForTopic:withCompletion:]_block_invoke.289
+ __62-[APSConnection getRegisteredChannelsForTopic:withCompletion:]_block_invoke_2.278
+ __63-[APSConnection forceClientIdentityProviderSwapWithCompletion:]_block_invoke.96
+ __65+[APSConnection _blockingXPCCallWithArgumentBlock:resultHandler:]_block_invoke.169
+ __80-[APSConnection _deliverOutgoingMessageResultWithID:error:sendRTT:ackTimestamp:]_block_invoke.140
+ __APSPubSubPowerLog_block_invoke.cold.1
+ ___40-[APSConnection rollTokensAndReconnect:]_block_invoke
+ ___63-[APSConnection forceClientIdentityProviderSwapWithCompletion:]_block_invoke
+ ___63-[APSConnection forceClientIdentityProviderSwapWithCompletion:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e33_v16?0"NSObject<OS_xpc_object>"8l
+ __block_literal_global.171
+ __block_literal_global.176
+ __block_literal_global.183
+ __block_literal_global.191
+ __block_literal_global.197
+ __block_literal_global.202
+ __block_literal_global.204
+ __block_literal_global.308
+ __block_literal_global.317
+ __block_literal_global.320
+ __block_literal_global.323
+ __block_literal_global.326
+ __block_literal_global.329
+ __block_literal_global.331
+ _arc4random_uniform
+ _isBAAPushIdentityEnabled
+ _objc_msgSend$initWithInt:
+ _objc_msgSend$intValue
+ _useMultiIdentityProvider
+ aps_path_watch_create_f.cold.6
+ isBAAPushIdentityEnabled.cold.1
+ isVirtualMachine.cold.1
- GCC_except_table221
- GCC_except_table224
- GCC_except_table291
- GCC_except_table316
- GCC_except_table328
- GCC_except_table334
- GCC_except_table337
- _OUTLINED_FUNCTION_32
- _OUTLINED_FUNCTION_33
- __33-[APSConnection _deliverMessage:]_block_invoke.122
- __39-[APSConnection _deliverToken:forInfo:]_block_invoke.151
- __42-[APSConnection _deliverURLToken:forInfo:]_block_invoke.154
- __43-[APSConnection _sendOutgoingMessage:fake:]_block_invoke.224
- __44-[APSConnection rollBAACertsWithCompletion:]_block_invoke.104
- __46-[APSConnection subscribeToChannels:forTopic:]_block_invoke.268
- __47-[APSConnection _deliverURLTokenError:forInfo:]_block_invoke.157
- __50-[APSConnection registeredChannelsForTopic:error:]_block_invoke.288
- __50-[APSConnection registeredChannelsForTopic:error:]_block_invoke.289
- __51-[APSConnection _deliverToken:forTopic:identifier:]_block_invoke.146
- __51-[APSConnection requestURLTokenForInfo:completion:]_block_invoke.245
- __51-[APSConnection requestURLTokenForInfo:completion:]_block_invoke.245.cold.1
- __54+[APSConnection _nonblockingXPCCallWithArgumentBlock:]_block_invoke.314
- __54+[APSConnection _nonblockingXPCCallWithArgumentBlock:]_block_invoke.317
- __54-[APSConnection invalidateURLTokenForInfo:completion:]_block_invoke.256
- __54-[APSConnection invalidateURLTokenForInfo:completion:]_block_invoke.256.cold.1
- __54-[APSConnection invalidateURLTokenForInfo:completion:]_block_invoke.260
- __54-[APSConnection invalidateURLTokenForInfo:completion:]_block_invoke.260.cold.1
- __59-[APSConnection signDataWithDeviceIdentity:withCompletion:]_block_invoke.98
- __60-[APSConnection _deliverFailedChannelSubscriptions:onTopic:]_block_invoke.296
- __62-[APSConnection getRegisteredChannelsForTopic:withCompletion:]_block_invoke.274
- __62-[APSConnection getRegisteredChannelsForTopic:withCompletion:]_block_invoke.279
- __62-[APSConnection getRegisteredChannelsForTopic:withCompletion:]_block_invoke.286
- __62-[APSConnection getRegisteredChannelsForTopic:withCompletion:]_block_invoke_2.275
- __65+[APSConnection _blockingXPCCallWithArgumentBlock:resultHandler:]_block_invoke.163
- __80-[APSConnection _deliverOutgoingMessageResultWithID:error:sendRTT:ackTimestamp:]_block_invoke.137
- __block_literal_global.162
- __block_literal_global.173
- __block_literal_global.177
- __block_literal_global.185
- __block_literal_global.194
- __block_literal_global.196
- __block_literal_global.201
- __block_literal_global.304
- __block_literal_global.313
- __block_literal_global.316
- __block_literal_global.319
- __block_literal_global.322
- __block_literal_global.325
- __block_literal_global.327
- _usingBAAClientIdentityProvider
CStrings:
+ "APSForceMacSleep"
+ "APSUsingMultiIdentityProvider"
+ "BAAPhysicalDevicesInternal"
+ "MultiIdentityProvider default not set, rolled %u, shouldUseMultiProvider %@?"
+ "MultiIdentityProvider default set to not use multi identity provider"
+ "MultiIdentityProvider default set to use multi identity provider"
+ "Received response to swap identity request"
+ "Requesting to roll tokens and force a reconnect"
+ "com.apple.apsd.roll-push-tokens"
+ "forceClientIdentityProviderSwapWithCompletion:"
+ "initWithInt:"
+ "intValue"
+ "rollTokensAndReconnect:"

```
