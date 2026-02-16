## iCloudNotification

> `/System/Library/PrivateFrameworks/iCloudNotification.framework/iCloudNotification`

```diff

-301.23.3.2.0
-  __TEXT.__text: 0x50c4
-  __TEXT.__auth_stubs: 0x360
-  __TEXT.__objc_methlist: 0x564
+301.23.4.7.0
+  __TEXT.__text: 0x5b1c
+  __TEXT.__auth_stubs: 0x2f0
+  __TEXT.__objc_methlist: 0x5c4
   __TEXT.__const: 0x48
-  __TEXT.__gcc_except_tab: 0x298
+  __TEXT.__gcc_except_tab: 0x320
   __TEXT.__cstring: 0x5cb
-  __TEXT.__oslogstring: 0x54a
+  __TEXT.__oslogstring: 0x62d
   __TEXT.__dlopen_cstrs: 0x54
-  __TEXT.__unwind_info: 0x250
+  __TEXT.__unwind_info: 0x2b0
   __TEXT.__objc_classname: 0x87
-  __TEXT.__objc_methname: 0x10ef
-  __TEXT.__objc_methtype: 0x8cd
-  __TEXT.__objc_stubs: 0x900
+  __TEXT.__objc_methname: 0x119e
+  __TEXT.__objc_methtype: 0x920
+  __TEXT.__objc_stubs: 0x980
   __DATA_CONST.__got: 0xa0
   __DATA_CONST.__const: 0x2c8
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x460
+  __DATA_CONST.__objc_selrefs: 0x480
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x10
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x1c0
+  __AUTH_CONST.__auth_got: 0x188
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x420
-  __AUTH_CONST.__objc_const: 0x630
+  __AUTH_CONST.__objc_const: 0x650
   __AUTH_CONST.__objc_arrayobj: 0x30
   __DATA.__objc_ivar: 0x18
   __DATA.__data: 0x180

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 93E7C264-C320-33A1-94AE-3F7FEEB1DA91
-  Functions: 134
-  Symbols:   541
-  CStrings:  357
+  UUID: 99780EE0-18A7-36C2-9C26-81472573ACB4
+  Functions: 154
+  Symbols:   584
+  CStrings:  367
 
Symbols:
+ -[INDaemonConnection handleChatterboxURL:completion:]
+ -[INDaemonConnection handleChatterboxURL:completion:].cold.1
+ -[INDaemonConnection notifyAMSEngagementAppDidBecomeActiveWithCompletion:]
+ -[INDaemonConnection performAMSEngagementWithParameters:completion:]
+ -[INDaemonConnection performPostPurchaseTeardownWithCompletion:]
+ GCC_except_table50
+ GCC_except_table53
+ GCC_except_table56
+ GCC_except_table63
+ GCC_except_table74
+ _OUTLINED_FUNCTION_6
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ ___53-[INDaemonConnection handleChatterboxURL:completion:]_block_invoke
+ ___53-[INDaemonConnection handleChatterboxURL:completion:]_block_invoke.41
+ ___53-[INDaemonConnection handleChatterboxURL:completion:]_block_invoke.cold.1
+ ___64-[INDaemonConnection displayDelayedOfferWithContext:completion:]_block_invoke.38
+ ___64-[INDaemonConnection performPostPurchaseTeardownWithCompletion:]_block_invoke
+ ___64-[INDaemonConnection performPostPurchaseTeardownWithCompletion:]_block_invoke.37
+ ___64-[INDaemonConnection performPostPurchaseTeardownWithCompletion:]_block_invoke.cold.1
+ ___68-[INDaemonConnection performAMSEngagementWithParameters:completion:]_block_invoke
+ ___68-[INDaemonConnection performAMSEngagementWithParameters:completion:]_block_invoke.35
+ ___68-[INDaemonConnection performAMSEngagementWithParameters:completion:]_block_invoke.cold.1
+ ___74-[INDaemonConnection notifyAMSEngagementAppDidBecomeActiveWithCompletion:]_block_invoke
+ ___74-[INDaemonConnection notifyAMSEngagementAppDidBecomeActiveWithCompletion:]_block_invoke.36
+ ___74-[INDaemonConnection notifyAMSEngagementAppDidBecomeActiveWithCompletion:]_block_invoke.cold.1
+ ___85-[INDaemonConnection unregisterDeviceFromLoggedOutiCloudNotificationsWithCompletion:]_block_invoke.40
+ ___89-[INDaemonConnection registerDeviceForLoggedOutiCloudNotificationsWithReason:completion:]_block_invoke.39
+ _objc_msgSend$handleChatterboxURL:completion:
+ _objc_msgSend$notifyAMSEngagementAppDidBecomeActiveWithCompletion:
+ _objc_msgSend$performAMSEngagementWithParameters:completion:
+ _objc_msgSend$performPostPurchaseTeardownWithCompletion:
+ _objc_retainAutoreleasedReturnValue
- GCC_except_table54
- ___64-[INDaemonConnection displayDelayedOfferWithContext:completion:]_block_invoke.35
- ___85-[INDaemonConnection unregisterDeviceFromLoggedOutiCloudNotificationsWithCompletion:]_block_invoke.37
- ___89-[INDaemonConnection registerDeviceForLoggedOutiCloudNotificationsWithReason:completion:]_block_invoke.36
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x2
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x8
- _objc_retain_x9
CStrings:
+ "Failed to connect to ind for AMS engagement task re-activation: %@"
+ "Failed to connect to ind for AMS engagement task: %@"
+ "Failed to connect to ind for post-purchase teardown: %@"
+ "Sending chatterbox URL handling request to daemon."
+ "handleChatterboxURL:completion:"
+ "notifyAMSEngagementAppDidBecomeActiveWithCompletion:"
+ "performAMSEngagementWithParameters:completion:"
+ "performPostPurchaseTeardownWithCompletion:"
+ "v32@0:8@\"NSDictionary\"16@?<v@?B@\"NSError\">24"
+ "v32@0:8@\"NSURL\"16@?<v@?B@\"NSError\">24"

```
