## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices`

```diff

-9.2.21.0.0
-  __TEXT.__text: 0x76bdc8
+9.2.23.2.2
+  __TEXT.__text: 0x772d18
   __TEXT.__auth_stubs: 0x4b30
-  __TEXT.__objc_methlist: 0x22f7c
-  __TEXT.__const: 0x5d680
+  __TEXT.__objc_methlist: 0x23094
+  __TEXT.__const: 0x5d6f0
   __TEXT.__dlopen_cstrs: 0x98b
-  __TEXT.__cstring: 0x2df8b
-  __TEXT.__swift5_typeref: 0x697b
-  __TEXT.__swift5_reflstr: 0x3ab4
+  __TEXT.__cstring: 0x2e2d4
+  __TEXT.__swift5_typeref: 0x6a37
+  __TEXT.__swift5_reflstr: 0x3ac4
   __TEXT.__swift5_assocty: 0xf00
   __TEXT.__constg_swiftt: 0x53bc
   __TEXT.__swift5_builtin: 0x320
   __TEXT.__swift5_fieldmd: 0x4e0c
   __TEXT.__swift5_proto: 0x1144
   __TEXT.__swift5_types: 0x62c
-  __TEXT.__swift_as_entry: 0x734
-  __TEXT.__swift_as_ret: 0x8b4
-  __TEXT.__swift5_capture: 0x31c0
+  __TEXT.__swift_as_entry: 0x748
+  __TEXT.__swift_as_ret: 0x8c8
+  __TEXT.__swift5_capture: 0x332c
   __TEXT.__swift5_mpenum: 0x7c
   __TEXT.__swift5_protos: 0xf0
-  __TEXT.__oslogstring: 0x3129b
-  __TEXT.__gcc_except_tab: 0x5e88
+  __TEXT.__oslogstring: 0x3187c
+  __TEXT.__gcc_except_tab: 0x5fa8
   __TEXT.__ustring: 0x1b2
-  __TEXT.__unwind_info: 0x118e8
-  __TEXT.__eh_frame: 0x15eb8
-  __TEXT.__objc_classname: 0x40ba
-  __TEXT.__objc_methname: 0x458fb
-  __TEXT.__objc_methtype: 0x7a03
-  __TEXT.__objc_stubs: 0x2ef00
-  __DATA_CONST.__got: 0x1a80
-  __DATA_CONST.__const: 0xc6a8
-  __DATA_CONST.__objc_classlist: 0x14e8
+  __TEXT.__unwind_info: 0x11a10
+  __TEXT.__eh_frame: 0x161b4
+  __TEXT.__objc_classname: 0x40f2
+  __TEXT.__objc_methname: 0x45a6b
+  __TEXT.__objc_methtype: 0x7a6e
+  __TEXT.__objc_stubs: 0x2f040
+  __DATA_CONST.__got: 0x1a88
+  __DATA_CONST.__const: 0xc710
+  __DATA_CONST.__objc_classlist: 0x14f8
   __DATA_CONST.__objc_catlist: 0xf8
-  __DATA_CONST.__objc_protolist: 0x448
+  __DATA_CONST.__objc_protolist: 0x450
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf428
-  __DATA_CONST.__objc_protorefs: 0x218
-  __DATA_CONST.__objc_superrefs: 0xce0
+  __DATA_CONST.__objc_selrefs: 0xf478
+  __DATA_CONST.__objc_protorefs: 0x220
+  __DATA_CONST.__objc_superrefs: 0xce8
   __DATA_CONST.__objc_arraydata: 0x580
   __AUTH_CONST.__auth_got: 0x25b0
-  __AUTH_CONST.__const: 0x2dd88
-  __AUTH_CONST.__cfstring: 0x22d40
-  __AUTH_CONST.__objc_const: 0x3d658
+  __AUTH_CONST.__const: 0x2e088
+  __AUTH_CONST.__cfstring: 0x22dc0
+  __AUTH_CONST.__objc_const: 0x3d7d8
   __AUTH_CONST.__objc_intobj: 0xc60
   __AUTH_CONST.__objc_arrayobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH.__objc_data: 0x98c0
-  __AUTH.__data: 0x27d8
-  __DATA.__objc_ivar: 0x18f0
-  __DATA.__data: 0x7898
+  __AUTH.__objc_data: 0x9980
+  __AUTH.__data: 0x27f8
+  __DATA.__objc_ivar: 0x18f8
+  __DATA.__data: 0x7988
   __DATA.__bss: 0x1cc89
   __DATA.__common: 0xb68
   __DATA_DIRTY.__objc_ivar: 0x718
   __DATA_DIRTY.__objc_data: 0x5ac0
-  __DATA_DIRTY.__data: 0x1b18
+  __DATA_DIRTY.__data: 0x1b28
   __DATA_DIRTY.__bss: 0x40e0
   __DATA_DIRTY.__common: 0x90
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D91F8575-B3DD-3F80-A282-42CECF867A25
-  Functions: 26768
-  Symbols:   53047
-  CStrings:  25947
+  UUID: 08AA4140-BB5B-3A33-8D4A-16886772A50F
+  Functions: 26884
+  Symbols:   53275
+  CStrings:  26002
 
Symbols:
+ +[AMSDaemonConnectionInterface _safariDataUpdateServiceInterface]
+ +[AMSServerDataCacheMigrator _syncCachedServerDataCacheUsingAccount:]
+ -[AMSDaemonConnection safariDataUpdateServiceProxy]
+ -[AMSDelegatePurchaseTask delegateAuthenticateUrl]
+ -[AMSPushHandler _passesiCloudTermsVerification:]
+ -[AMSSafariDataUpdate .cxx_destruct]
+ -[AMSSafariDataUpdate _handleUpdateAvailableNotification:]
+ -[AMSSafariDataUpdate _invokeHandlersWithURL:]
+ -[AMSSafariDataUpdate dealloc]
+ -[AMSSafariDataUpdate init]
+ -[AMSSafariDataUpdate publishUpdate:]
+ -[AMSSafariDataUpdate queue]
+ -[AMSSafariDataUpdate registerForUpdatesWithHandler:]
+ -[AMSSafariDataUpdate setQueue:]
+ -[AMSSafariDataUpdate setUpdateHandlers:]
+ -[AMSSafariDataUpdate updateHandlers]
+ GCC_except_table78
+ _AMSMetricsIdentifierStorePrivateIdentifiersInteropErrorDomain
+ _OBJC_CLASS_$_AMSMetricsIdentifierStorePrivateIdentifiersInterop
+ _OBJC_CLASS_$_AMSSafariDataUpdate
+ _OBJC_IVAR_$_AMSSafariDataUpdate._queue
+ _OBJC_IVAR_$_AMSSafariDataUpdate._updateHandlers
+ _OBJC_METACLASS_$_AMSMetricsIdentifierStorePrivateIdentifiersInterop
+ _OBJC_METACLASS_$_AMSSafariDataUpdate
+ _OUTLINED_FUNCTION_186
+ _OUTLINED_FUNCTION_187
+ _OUTLINED_FUNCTION_188
+ _OUTLINED_FUNCTION_189
+ _OUTLINED_FUNCTION_190
+ _OUTLINED_FUNCTION_191
+ _OUTLINED_FUNCTION_192
+ _OUTLINED_FUNCTION_193
+ _OUTLINED_FUNCTION_194
+ _OUTLINED_FUNCTION_195
+ _OUTLINED_FUNCTION_196
+ _OUTLINED_FUNCTION_197
+ _OUTLINED_FUNCTION_198
+ _OUTLINED_FUNCTION_199
+ _OUTLINED_FUNCTION_200
+ _OUTLINED_FUNCTION_201
+ _OUTLINED_FUNCTION_202
+ _OUTLINED_FUNCTION_203
+ _OUTLINED_FUNCTION_204
+ _OUTLINED_FUNCTION_205
+ _OUTLINED_FUNCTION_206
+ __CLASS_METHODS_AMSMetricsIdentifierStorePrivateIdentifiersInterop
+ __DATA_AMSMetricsIdentifierStorePrivateIdentifiersInterop
+ __INSTANCE_METHODS_AMSMetricsIdentifierStorePrivateIdentifiersInterop
+ __METACLASS_DATA_AMSMetricsIdentifierStorePrivateIdentifiersInterop
+ __OBJC_$_INSTANCE_METHODS_AMSSafariDataUpdate
+ __OBJC_$_INSTANCE_VARIABLES_AMSSafariDataUpdate
+ __OBJC_$_PROP_LIST_AMSSafariDataUpdate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AMSSafariDataUpdateServiceInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AMSSafariDataUpdateServiceInterface
+ __OBJC_$_PROTOCOL_REFS_AMSSafariDataUpdateServiceInterface
+ __OBJC_CLASS_RO_$_AMSSafariDataUpdate
+ __OBJC_LABEL_PROTOCOL_$_AMSSafariDataUpdateServiceInterface
+ __OBJC_METACLASS_RO_$_AMSSafariDataUpdate
+ __OBJC_PROTOCOL_$_AMSSafariDataUpdateServiceInterface
+ __OBJC_PROTOCOL_REFERENCE_$_AMSSafariDataUpdateServiceInterface
+ ___37-[AMSSafariDataUpdate publishUpdate:]_block_invoke
+ ___37-[AMSSafariDataUpdate publishUpdate:]_block_invoke.19
+ ___46-[AMSSafariDataUpdate _invokeHandlersWithURL:]_block_invoke
+ ___51-[AMSDaemonConnection safariDataUpdateServiceProxy]_block_invoke
+ ___51-[AMSDaemonConnection safariDataUpdateServiceProxy]_block_invoke_2
+ ___53-[AMSSafariDataUpdate registerForUpdatesWithHandler:]_block_invoke
+ ___58-[AMSSafariDataUpdate _handleUpdateAvailableNotification:]_block_invoke
+ ___58-[AMSSafariDataUpdate _handleUpdateAvailableNotification:]_block_invoke.22
+ ___58-[AMSSafariDataUpdate _handleUpdateAvailableNotification:]_block_invoke.23
+ ___71+[AMSMetricsIdentifierStore performUserResetForStoresInBag:forAccount:]_block_invoke.121
+ ___71+[AMSMetricsIdentifierStore performUserResetForStoresInBag:forAccount:]_block_invoke.122
+ ___85+[AMSMetricsIdentifierStore _promiseToRotateIdentifiersForAccount:bag:namespaceList:]_block_invoke.125
+ ___block_descriptor_48_e8_32s40r_e30_v24?0"NSString"8"NSError"16ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e59_v24?0"<AMSSafariDataUpdateServiceInterface>"8"NSError"16ls32l8r40l8
+ ___block_descriptor_48_e8_32s40s_e79_v24?0"<AMSSafariDataUpdateServiceInterface><NSXPCProxyCreating>"8"NSError"16ls32l8s40l8
+ ___block_descriptor_56_e8_32s40s_e30_v24?0"NSNumber"8"NSError"16ls32l8s40l8
+ ___block_descriptor_64_e8_32s40s48s56r_e59_v24?0"<AMSSafariDataUpdateServiceInterface>"8"NSError"16ls32l8s40l8r56l8s48l8
+ ___block_literal_global.124
+ ___block_literal_global.128
+ _block_copy_helper.84
+ _block_copy_helper.95
+ _block_descriptor.86
+ _block_descriptor.97
+ _block_destroy_helper.85
+ _block_destroy_helper.96
+ _objc_msgSend$_invokeHandlersWithURL:
+ _objc_msgSend$_passesiCloudTermsVerification:
+ _objc_msgSend$_safariDataUpdateServiceInterface
+ _objc_msgSend$_syncCachedServerDataCacheUsingAccount:
+ _objc_msgSend$fetchPendingSafariDataUpdate:
+ _objc_msgSend$getSafariDataUpdateServiceProxyWithReplyHandler:
+ _objc_msgSend$performPostSignInTasksInDaemonForAccount:credentialSource:
+ _objc_msgSend$performPrivateIdentifiersUserInitiatedRotationWithBag:dsid:completionHandler:
+ _objc_msgSend$promiseWithFlattenedPromises:
+ _objc_msgSend$publishSafariDataUpdate:completion:
+ _objc_msgSend$safariDataUpdateServiceProxy
+ _objectdestroy.160Tm
+ _objectdestroy.268Tm
+ _symbolic SS______t 18AppleMediaServices14RotationActionO
+ _symbolic So18AMSAccountIdentityCSg
+ _symbolic So50AMSMetricsIdentifierStorePrivateIdentifiersInteropCXMo
+ _symbolic So7NSErrorCSgIeyBy_Sg
+ _symbolic _____9accountID_SS08consumerB0_____15serverTimestampt 18AppleMediaServices15AccountIdentityV 10Foundation4DateV
+ _symbolic _____ySS_____G s18_DictionaryStorageC 18AppleMediaServices14RotationActionO
+ _symbolic _____ySS______tG s23_ContiguousArrayStorageC 18AppleMediaServices14RotationActionO
+ _symbolic _____y_____y______GG s23_ContiguousArrayStorageC 18AppleMediaServices26PrivateIdentifiersProviderV16AccountSpecifierO AC0J8IdentityV4DSIDV
- +[AMSServerDataCacheMigrator _primeCachedServerDataCacheUsingAccount:]
- -[AMSDelegatePurchaseTask _delegateAuthenticateURL]
- ___70+[AMSServerDataCacheMigrator _primeCachedServerDataCacheUsingAccount:]_block_invoke
- ___70+[AMSServerDataCacheMigrator _primeCachedServerDataCacheUsingAccount:]_block_invoke_2
- ___85+[AMSMetricsIdentifierStore _promiseToRotateIdentifiersForAccount:bag:namespaceList:]_block_invoke.120
- ___block_descriptor_32_e52_v24?0"<AMSAccountCachedServerString>"8"NSError"16l
- ___block_descriptor_40_e52_v24?0"<AMSAccountCachedServerString>"8"NSError"16l
- ___block_descriptor_48_e8_32s_e30_v24?0"NSNumber"8"NSError"16ls32l8
- _block_copy_helper.68
- _block_copy_helper.75
- _block_descriptor.70
- _block_descriptor.77
- _block_destroy_helper.69
- _block_destroy_helper.76
- _objc_msgSend$_primeCachedServerDataCacheUsingAccount:
- _objectdestroy.252Tm
- _symbolic SS10consumerID______15serverTimestampt 10Foundation4DateV
CStrings:
+ "%{public}@: Cannot register nil handler"
+ "%{public}@: Dropping notification. iCloud account needed to handle notification, but not available."
+ "%{public}@: Failed to get proxy for fetch: %{public}@"
+ "%{public}@: Failed to get proxy for publish: %{public}@"
+ "%{public}@: Fetch failed: %{public}@"
+ "%{public}@: Fetched pending update: %{public}@"
+ "%{public}@: Handler threw exception: %{public}@"
+ "%{public}@: Initialized and observing distributed notifications"
+ "%{public}@: Invalid URL for publish"
+ "%{public}@: Invoking %ld handler(s) with URL: %{public}@"
+ "%{public}@: No handlers registered, skipping fetch"
+ "%{public}@: No pending update available (may have expired)"
+ "%{public}@: Publish failed: %{public}@"
+ "%{public}@: Publish succeeded"
+ "%{public}@: Publishing Safari Data Update: %{public}@"
+ "%{public}@: Received distributed notification for Safari Data Update"
+ "%{public}@: Registered handler, total handlers: %ld"
+ "%{public}@: [%{public}@] Performing user reset of metrics identifier store identifiers for account %{public}@"
+ "%{public}@: [%{public}@] Performing user reset of private identifiers for account %{public}@"
+ "%{public}@: [%{public}@] Private identifer config is not present in the bag, not performing user initiated private identifer rotation for account %{public}@"
+ "%{public}@: [%{public}@] User initiated metrics identifier store identifer rotation completed for account %{public}@"
+ "%{public}@: [%{public}@] User initiated metrics identifier store identifer rotation failed for account %{public}@: %{public}@"
+ "%{public}@: [%{public}@] User initiated private identifer rotation completed for account %{public}@"
+ "%{public}@: [%{public}@] User initiated private identifier rotation failed for account %{public}@: %{public}@"
+ "%{public}@: _ntv flag present, but account validation disabled. Handling notification"
+ "AMSMetricsIdentifierStorePrivateIdentifiersInterop"
+ "AMSMetricsIdentifierStorePrivateIdentifiersInteropErrorDomain"
+ "AMSSafariDataUpdate"
+ "AMSSafariDataUpdate Error"
+ "AMSSafariDataUpdateServiceInterface"
+ "Found value result in sequence:"
+ "Invalid URL for publish"
+ "Performing XPC to daemon for account data"
+ "Performing XPC to daemon for account data manual sync"
+ "Performing XPC to daemon for account data metrics event"
+ "Performing XPC to daemon for account data set autoplay"
+ "Performing XPC to daemon for account data set personalization"
+ "_handleUpdateAvailableNotification:"
+ "_invokeHandlersWithURL:"
+ "_passesiCloudTermsVerification:"
+ "_safariDataUpdateServiceInterface"
+ "_syncCachedServerDataCacheUsingAccount:"
+ "accountID consumerID serverTimestamp "
+ "com.apple.AMS.SafariDataUpdate"
+ "com.apple.AMSSafariDataUpdate"
+ "fetchPendingSafariDataUpdate:"
+ "filteredSequence "
+ "getSafariDataUpdateServiceProxyWithReplyHandler:"
+ "performPrivateIdentifiersUserInitiatedRotationWithBag:dsid:completionHandler:"
+ "publishSafariDataUpdate:completion:"
+ "publishUpdate:"
+ "registerForUpdatesWithHandler:"
+ "safariDataUpdateServiceProxy"
+ "v24@0:8@?<v@?@\"<AMSSafariDataUpdateServiceInterface>\"@\"NSError\">16"
+ "v24@?0@\"<AMSSafariDataUpdateServiceInterface>\"8@\"NSError\"16"
+ "v24@?0@\"<AMSSafariDataUpdateServiceInterface><NSXPCProxyCreating>\"8@\"NSError\"16"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
+ "v40@0:8@\"<AMSBagProtocol>\"16@\"NSNumber\"24@?<v@?@\"NSError\">32"
- "%{public}@: [%{public}@] Performing user reset for account %{public}@"
- "%{public}@: [%{public}@] Priming account data cache due to migration."
- "%{public}@: [%{public}@] User initiated identifer rotation completed"
- "%{public}@: [%{public}@] User initiated identifer rotation failed: %{public}@"
- "_delegateAuthenticateURL"
- "_primeCachedServerDataCacheUsingAccount:"
- "consumerID serverTimestamp "

```
