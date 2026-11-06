## AddressBookCore

> `/System/Library/PrivateFrameworks/AddressBookCore.framework/Versions/A/AddressBookCore`

```diff

-2765.100.1.1.1
-  __TEXT.__text: 0xe8544
-  __TEXT.__objc_methlist: 0x12b94
-  __TEXT.__const: 0x1f4
-  __TEXT.__cstring: 0xcc7e
-  __TEXT.__gcc_except_tab: 0x3f2c
-  __TEXT.__oslogstring: 0x5a03
+2768.200.91.0.0
+  __TEXT.__text: 0xe9a1c
+  __TEXT.__objc_methlist: 0x12bf4
+  __TEXT.__const: 0x1e4
+  __TEXT.__cstring: 0xcd74
+  __TEXT.__gcc_except_tab: 0x4010
+  __TEXT.__oslogstring: 0x5dd4
   __TEXT.__dlopen_cstrs: 0x239
-  __TEXT.__unwind_info: 0x5770
+  __TEXT.__unwind_info: 0x57b0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x92c8
+  __DATA_CONST.__objc_selrefs: 0x9320
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x698
   __DATA_CONST.__objc_arraydata: 0x148
-  __DATA_CONST.__got: 0x1818
-  __AUTH_CONST.__const: 0x5b50
-  __AUTH_CONST.__cfstring: 0xe3a0
-  __AUTH_CONST.__objc_const: 0x19fe8
+  __DATA_CONST.__got: 0x1828
+  __AUTH_CONST.__const: 0x5c10
+  __AUTH_CONST.__cfstring: 0xe400
+  __AUTH_CONST.__objc_const: 0x1a008
   __AUTH_CONST.__objc_arrayobj: 0xc0
   __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH_CONST.__auth_got: 0x840
+  __AUTH_CONST.__auth_got: 0x868
   __AUTH_CONST.__auth_ptr: 0x0
   __AUTH.__objc_data: 0x59b0
   __AUTH.__data: 0x20
-  __DATA.__objc_ivar: 0xb84
-  __DATA.__data: 0x1af8
+  __DATA.__objc_ivar: 0xb88
+  __DATA.__data: 0x1b00
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0xc78
   __DATA_DIRTY.__objc_data: 0x15e0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 7316
-  Symbols:   16813
-  CStrings:  2604
+  Functions: 7344
+  Symbols:   16851
+  CStrings:  2623
 
Symbols:
+ -[ABPushNotificationCenter commitEnabledTopicsForEnvironment:]
+ -[ABPushNotificationCenter connectionForEnvironment:]
+ -[ABPushNotificationCenter enabledTopicSetForEnvironment:]
+ -[ABPushNotificationCenter registerSource:forWebPushTopic:environment:]
+ -[ABPushNotificationCenter routeWebPushMessage:]
+ -[ABPushNotificationCenter unregisterWebPushTopic:environment:]
+ -[ABPushNotificationCenter webPushNotificationURLForTopic:vapidPublicKey:environment:error:]
+ -[PHXSource handleWebPushNotificationForTopic:userInfo:]
+ GCC_except_table186
+ OBJC_IVAR_$_ABPushNotificationCenter._sourcesByWebPushTopic
+ _ABPushWorkQueueKey
+ _OBJC_CLASS_$_APSURLTokenInfo
+ _OBJC_CLASS_$_NSLock
+ __45-[ABPushNotificationCenter unregisterSource:]_block_invoke
+ ___48-[ABPushNotificationCenter routeWebPushMessage:]_block_invoke
+ ___62-[ABPushNotificationCenter commitEnabledTopicsForEnvironment:]_block_invoke
+ ___63-[ABPushNotificationCenter unregisterWebPushTopic:environment:]_block_invoke
+ ___71-[ABPushNotificationCenter registerSource:forWebPushTopic:environment:]_block_invoke
+ ___92-[ABPushNotificationCenter webPushNotificationURLForTopic:vapidPublicKey:environment:error:]_block_invoke
+ ___block_descriptor_48_e8_32o40o_e36_v32?0"NSString"8"PHXSource"16^B24l
+ ___block_descriptor_64_e8_32o40o48o56r_e5_v8?0l
+ ___block_descriptor_64_e8_32o40o48r56r_e5_v8?0l
+ ___block_descriptor_80_e8_32o40o48r56r64r72r_e33_v24?0"APSURLToken"8"NSError"16l
+ ___copy_helper_block_e8_32o40o48r56r
+ ___copy_helper_block_e8_32o40o48r56r64r72r
+ ___destroy_helper_block_e8_32o40o48r56r
+ ___destroy_helper_block_e8_32o40o48r56r64r72r
+ _dispatch_get_specific
+ _dispatch_queue_set_specific
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _objc_msgSend$commitEnabledTopicsForEnvironment:
+ _objc_msgSend$connectionForEnvironment:
+ _objc_msgSend$enabledTopicSetForEnvironment:
+ _objc_msgSend$handleWebPushNotificationForTopic:userInfo:
+ _objc_msgSend$initWithTopic:vapidPublicKey:
+ _objc_msgSend$requestURLTokenForInfo:completion:
+ _objc_msgSend$routeWebPushMessage:
+ _objc_msgSend$tokenURL
- GCC_except_table183
- GCC_except_table185
CStrings:
+ "A web push URL token cannot be requested from the push work queue"
+ "A web push URL token needs both a topic and a VAPID key"
+ "No source registered for web push topic %{public}@; dropping. Registered topics: %{public}@"
+ "Obtained web push URL token for topic %{public}@ (%lu chars)"
+ "Registered web push topic %{public}@ for source %@"
+ "Timed out waiting for a web push URL token for topic %{public}@"
+ "Timed out waiting for a web push URL token from apsd"
+ "Unregistered web push topic %{public}@"
+ "Web push URL token for topic %{public}@ arrived as we gave up waiting; using it"
+ "Web push message with no topic; dropping"
+ "apsd refused a web push URL token for topic %{public}@: %{public}@"
+ "didReceiveIncomingMessage topic=%{public}@ userInfoKeys=%{public}@ hasPushKey=%{public}d"
+ "dropping incoming message for topic %{public}@: this process does not handle incoming messages (bundle %{public}@)"
+ "enabledTopics for %{public}@ now (%lu): %{public}@"
+ "registerSource:forWebPushTopic: called with no topic or no source"
+ "routing web push for topic %{public}@ to source %{public}@"
+ "v24@?0@\"APSURLToken\"8@\"NSError\"16"
+ "v32@?0@\"NSString\"8@\"PHXSource\"16^B24"
+ "webPushNotificationURLForTopic: called on the push work queue; the completion could never run"
+ "webPushNotificationURLForTopic: needs a topic and a VAPID key"
- "didReceiveIncomingMessage with topic: %@ userInfo: %@"
```
