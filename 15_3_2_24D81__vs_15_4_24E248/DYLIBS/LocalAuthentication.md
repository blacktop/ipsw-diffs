## LocalAuthentication

> `/System/Library/Frameworks/LocalAuthentication.framework/Versions/A/LocalAuthentication`

```diff

-1656.80.6.0.0
-  __TEXT.__text: 0x3adf4
-  __TEXT.__auth_stubs: 0x920
-  __TEXT.__objc_methlist: 0x2c10
-  __TEXT.__const: 0x2e0
-  __TEXT.__gcc_except_tab: 0x1318
-  __TEXT.__cstring: 0x1b22
+1656.100.223.0.0
+  __TEXT.__text: 0x3bf0c
+  __TEXT.__auth_stubs: 0x940
+  __TEXT.__objc_methlist: 0x3498
+  __TEXT.__const: 0x2f0
+  __TEXT.__gcc_except_tab: 0x1330
+  __TEXT.__cstring: 0x1b5e
   __TEXT.__dlopen_cstrs: 0x177
-  __TEXT.__oslogstring: 0x2a97
+  __TEXT.__oslogstring: 0x2cb9
   __TEXT.__swift5_typeref: 0x6e
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x12a8
+  __TEXT.__unwind_info: 0x1378
   __TEXT.__eh_frame: 0x48
-  __TEXT.__objc_classname: 0x8ff
-  __TEXT.__objc_methname: 0x6687
-  __TEXT.__objc_methtype: 0x1e0f
-  __TEXT.__objc_stubs: 0x4640
-  __DATA_CONST.__got: 0x4d0
+  __TEXT.__objc_classname: 0x8fb
+  __TEXT.__objc_methname: 0x68d4
+  __TEXT.__objc_methtype: 0x1ead
+  __TEXT.__objc_stubs: 0x4740
+  __DATA_CONST.__got: 0x4c0
   __DATA_CONST.__const: 0x3a8
   __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19a8
+  __DATA_CONST.__objc_selrefs: 0x1b00
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x1c8
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__auth_got: 0x4a0
-  __AUTH_CONST.__const: 0x2020
-  __AUTH_CONST.__cfstring: 0x1940
-  __AUTH_CONST.__objc_const: 0x8ad0
+  __AUTH_CONST.__auth_got: 0x4b0
+  __AUTH_CONST.__const: 0x20e0
+  __AUTH_CONST.__cfstring: 0x1980
+  __AUTH_CONST.__objc_const: 0x7db8
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1680
-  __DATA.__objc_ivar: 0x284
+  __DATA.__objc_ivar: 0x28c
   __DATA.__data: 0xbb0
   __DATA.__bss: 0x488
   - /System/Library/Frameworks/Combine.framework/Versions/A/Combine

   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 691D2454-FF90-30F5-81C6-519F317A49FF
-  Functions: 1468
-  Symbols:   3660
-  CStrings:  2206
+  UUID: C6DED4B2-2E53-3F35-AC45-3E2B8CC5556A
+  Functions: 1510
+  Symbols:   3723
+  CStrings:  2243
 
Symbols:
+ +[LAClient _queue].cold.1
+ +[LAContext notifyEvent:completionHandler:].cold.1
+ +[LAEnvironment currentUser].cold.1
+ +[LAKeyStoreBackendBuilder buildBackend].cold.1
+ +[LARatchetManager sharedInstance].cold.1
+ +[LARightStore sharedStore].cold.1
+ +[_LAMKBLog log].cold.1
+ -[LAClient analyticsAction:dismissing:reply:]
+ -[LAClient analyticsMechanism:result:reply:]
+ -[LAClient analyticsMechanism:starting:reply:]
+ -[LAClient analyticsSessionStarting:dialogID:bundleID:reply:]
+ -[LAContext analyticsAction:dismissing:]
+ -[LAContext analyticsMechanism:result:]
+ -[LAContext analyticsMechanism:starting:]
+ -[LAContext analyticsSessionStarting:dialogID:bundleID:]
+ -[LAContext initWithCoder:].cold.1
+ -[LAContext initWithExternalizedContext:userSession:].cold.1
+ -[LAContext optionDialogID]
+ -[LAContext optionDisableConcurrentEvaluation]
+ -[LAContext setOptionDialogID:]
+ -[LAContext setOptionDisableConcurrentEvaluation:]
+ -[LAEnvironment _handleDarwinNotification]
+ -[LAStorage dictionaryForKey:]
+ -[LAStorage dictionaryForKey:completionHandler:]
+ -[LAStorage dictionaryForKey:error:]
+ -[LAStorage setDictionary:forKey:completionHandler:]
+ -[LAStorage setDictionary:forKey:error:]
+ GCC_except_table100
+ GCC_except_table112
+ GCC_except_table114
+ GCC_except_table131
+ GCC_except_table135
+ GCC_except_table14
+ GCC_except_table141
+ GCC_except_table145
+ GCC_except_table191
+ GCC_except_table49
+ GCC_except_table51
+ GCC_except_table54
+ GCC_except_table66
+ GCC_except_table71
+ GCC_except_table83
+ GCC_except_table89
+ GCC_except_table93
+ LA_LOG.cold.1
+ LA_LOG_coreauthd_client.cold.1
+ LA_LOG_laabio.cold.1
+ OBJC_IVAR_$_LAEnvironment._notificationQueue
+ OBJC_IVAR_$_LAEnvironment._stateLock
+ _OBJC_CLASS_$_LACCachedExternalizedContext
+ __23-[LAContext invalidate]_block_invoke.57
+ __29-[LAContext encodeWithCoder:]_block_invoke.48
+ __29-[LAContext encodeWithCoder:]_block_invoke.48.cold.1
+ __29-[LAContext encodeWithCoder:]_block_invoke.48.cold.2
+ __32-[LAStorage _connectToEndpoint:]_block_invoke.122
+ __44-[LAStorage objectForKey:completionHandler:]_block_invoke.29
+ __48-[LAStorage setObject:forKey:completionHandler:]_block_invoke.26
+ __50-[LAStorage removeObjectForKey:completionHandler:]_block_invoke.30
+ __51-[LAStorage exchangeData:forKey:completionHandler:]_block_invoke.34
+ __68-[LAStorage _callProxyBlock:authenticationPolicy:completionHandler:]_block_invoke.131
+ __68-[LAStorage _callProxyBlock:authenticationPolicy:completionHandler:]_block_invoke.cold.1
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACContextCallbackXPC
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACContextExternalizing
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LACContextExternalizing
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACContextCallbackXPC
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACContextExternalizing
+ __OBJC_$_PROTOCOL_REFS_LACContextExternalizing
+ __OBJC_LABEL_PROTOCOL_$_LACContextCallbackXPC
+ __OBJC_LABEL_PROTOCOL_$_LACContextExternalizing
+ __OBJC_PROTOCOL_$_LACContextCallbackXPC
+ __OBJC_PROTOCOL_$_LACContextExternalizing
+ ___36-[LAStorage dictionaryForKey:error:]_block_invoke
+ ___39-[LAContext analyticsMechanism:result:]_block_invoke
+ ___40-[LAContext analyticsAction:dismissing:]_block_invoke
+ ___40-[LAStorage setDictionary:forKey:error:]_block_invoke
+ ___41-[LAContext analyticsMechanism:starting:]_block_invoke
+ ___42-[LAEnvironment _handleDarwinNotification]_block_invoke
+ ___44-[LAClient analyticsMechanism:result:reply:]_block_invoke
+ ___45-[LAClient analyticsAction:dismissing:reply:]_block_invoke
+ ___46-[LAClient analyticsMechanism:starting:reply:]_block_invoke
+ ___56-[LAContext analyticsSessionStarting:dialogID:bundleID:]_block_invoke
+ ___61-[LAClient analyticsSessionStarting:dialogID:bundleID:reply:]_block_invoke
+ ___block_descriptor_53_e8_32s40s_e20_v20?0B8"NSError"12l
+ ___block_descriptor_57_e8_32s40s48s_e25_v16?0?<v?B"NSError">8l
+ ___block_descriptor_60_e8_32s40s_e20_v20?0B8"NSError"12l
+ ___block_descriptor_61_e8_32s40s_e20_v20?0B8"NSError"12l
+ ___block_descriptor_68_e8_32s40s48s_e20_v20?0B8"NSError"12l
+ __block_literal_global.18
+ __block_literal_global.234
+ __block_literal_global.30
+ __block_literal_global.60
+ __block_literal_global.62
+ _objc_msgSend$_handleDarwinNotification
+ _objc_msgSend$analyticsAction:dismissing:reply:
+ _objc_msgSend$analyticsMechanism:result:reply:
+ _objc_msgSend$analyticsMechanism:starting:reply:
+ _objc_msgSend$analyticsSessionStarting:dialogID:bundleID:reply:
+ _objc_msgSend$dictionaryForKey:completionHandler:
+ _objc_msgSend$dictionaryForKey:error:
+ _objc_msgSend$setDictionary:forKey:completionHandler:
+ _os_unfair_lock_assert_owner
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- GCC_except_table104
- GCC_except_table106
- GCC_except_table123
- GCC_except_table127
- GCC_except_table133
- GCC_except_table137
- GCC_except_table182
- GCC_except_table21
- GCC_except_table43
- GCC_except_table47
- GCC_except_table50
- GCC_except_table75
- GCC_except_table77
- GCC_except_table81
- GCC_except_table92
- _LACPolicyOptionAllowEnablementGracePeriod
- _OBJC_CLASS_$_LACDTORatchetState
- _OBJC_CLASS_$_LACachedExternalizedContext
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_11
- _OUTLINED_FUNCTION_12
- __23-[LAContext invalidate]_block_invoke.54
- __29-[LAContext encodeWithCoder:]_block_invoke.45
- __29-[LAContext encodeWithCoder:]_block_invoke.45.cold.1
- __29-[LAContext encodeWithCoder:]_block_invoke.45.cold.2
- __32-[LAStorage _connectToEndpoint:]_block_invoke.117
- __44-[LAStorage objectForKey:completionHandler:]_block_invoke.27
- __48-[LAStorage setObject:forKey:completionHandler:]_block_invoke.24
- __50-[LAStorage removeObjectForKey:completionHandler:]_block_invoke.28
- __51-[LAStorage exchangeData:forKey:completionHandler:]_block_invoke.32
- __68-[LAStorage _callProxyBlock:authenticationPolicy:completionHandler:]_block_invoke.126
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LAContextCallbackXPC
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_LAContextExternalizationProt
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_LAContextExternalizationProt
- __OBJC_$_PROTOCOL_METHOD_TYPES_LAContextCallbackXPC
- __OBJC_$_PROTOCOL_METHOD_TYPES_LAContextExternalizationProt
- __OBJC_$_PROTOCOL_REFS_LAContextExternalizationProt
- __OBJC_LABEL_PROTOCOL_$_LAContextCallbackXPC
- __OBJC_LABEL_PROTOCOL_$_LAContextExternalizationProt
- __OBJC_PROTOCOL_$_LAContextCallbackXPC
- __OBJC_PROTOCOL_$_LAContextExternalizationProt
- ___22-[LAEnvironment state]_block_invoke
- ___block_descriptor_48_e8_32r40w_e5_v8?0l
- ___copy_helper_block_e8_32r40w
- ___destroy_helper_block_e8_32r40w
- __block_literal_global.15
- __block_literal_global.225
- __block_literal_global.27
- __block_literal_global.57
- __block_literal_global.59
- _dispatch_assert_queue$V2
CStrings:
+ "@\"LACCachedExternalizedContext\""
+ "Helper context invalidated"
+ "LACContextCallbackXPC"
+ "LACContextExternalizing"
+ "LAEnvironment notification queue"
+ "T@\"LACCachedExternalizedContext\",&,V_cachedExternalizedContext"
+ "_handleDarwinNotification"
+ "_notificationQueue"
+ "_stateLock"
+ "analyticsAction:%d dismissing:%d on %{public}@ cid:%u"
+ "analyticsAction:%d on %{public}@ cid:%u returned %{public}@"
+ "analyticsAction:dismissing:"
+ "analyticsAction:dismissing:reply:"
+ "analyticsMechanism:%d result: %{public}@ on %{public}@ cid:%u returned %{public}@"
+ "analyticsMechanism:%d result:%{public}@ on %{public}@ cid:%u"
+ "analyticsMechanism:%d starting:%d on %{public}@ cid:%u"
+ "analyticsMechanism:%d starting:%d on %{public}@ cid:%u returned %{public}@"
+ "analyticsMechanism:result:"
+ "analyticsMechanism:result:reply:"
+ "analyticsMechanism:starting:"
+ "analyticsMechanism:starting:reply:"
+ "analyticsSessionStarting:%d dialogID:%{public}@ bundleID:%{private}@ on %{public}@ cid:%u"
+ "analyticsSessionStarting:%d on %{public}@ cid:%u returned %{public}@"
+ "analyticsSessionStarting:dialogID:bundleID:"
+ "analyticsSessionStarting:dialogID:bundleID:reply:"
+ "dictionaryForKey:"
+ "dictionaryForKey:completionHandler:"
+ "dictionaryForKey:error:"
+ "optionDialogID"
+ "optionDisableConcurrentEvaluation"
+ "setDictionary:forKey:completionHandler:"
+ "setDictionary:forKey:error:"
+ "setOptionDialogID:"
+ "setOptionDisableConcurrentEvaluation:"
+ "v24@0:8@?<v@?@\"<LACAgentProxyXPC>\"@\"NSError\">16"
+ "v28@0:8q16B24"
+ "v36@0:8B16@20@28"
+ "v44@0:8B16@\"NSString\"20@\"NSString\"28@?<v@?B@\"NSError\">36"
+ "v44@0:8B16@20@28@?36"
+ "v48@0:8@\"NSData\"16@\"<LACContextCallbackXPC>\"24Q32@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">40"
+ "v64@0:8@\"NSUUID\"16@\"<LACContextCallbackXPC>\"24Q32@\"NSData\"40@\"NSData\"48@?<v@?@\"<LAContextXPC>\"@\"NSString\"@\"NSError\">56"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"
- "@\"LACachedExternalizedContext\""
- "LAContextCallbackXPC"
- "LAContextExternalizationProt"
- "T@\"LACachedExternalizedContext\",&,V_cachedExternalizedContext"
- "v24@0:8@?<v@?@\"<LAAgentProxyXPC>\"@\"NSError\">16"
- "v48@0:8@\"NSData\"16@\"<LAContextCallbackXPC>\"24Q32@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">40"
- "v64@0:8@\"NSUUID\"16@\"<LAContextCallbackXPC>\"24Q32@\"NSData\"40@\"NSData\"48@?<v@?@\"<LAContextXPC>\"@\"NSString\"@\"NSError\">56"

```
