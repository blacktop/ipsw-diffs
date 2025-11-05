## StatusKit

> `/System/Library/PrivateFrameworks/StatusKit.framework/Versions/A/StatusKit`

```diff

-80.400.131.0.0
-  __TEXT.__text: 0x1a1b0
+80.500.181.0.0
+  __TEXT.__text: 0x1a5d8
   __TEXT.__auth_stubs: 0x300
-  __TEXT.__objc_methlist: 0x1458
+  __TEXT.__objc_methlist: 0x1838
   __TEXT.__const: 0xa0
   __TEXT.__cstring: 0xc81
-  __TEXT.__oslogstring: 0x3aaa
-  __TEXT.__gcc_except_tab: 0xb34
-  __TEXT.__unwind_info: 0x798
+  __TEXT.__oslogstring: 0x3aec
+  __TEXT.__gcc_except_tab: 0xb70
+  __TEXT.__unwind_info: 0x7d0
   __TEXT.__objc_classname: 0x386
-  __TEXT.__objc_methname: 0x3af2
+  __TEXT.__objc_methname: 0x3b1c
   __TEXT.__objc_methtype: 0xbbf
   __TEXT.__objc_stubs: 0x1ba0
   __DATA_CONST.__got: 0x110

   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa00
+  __DATA_CONST.__objc_selrefs: 0xa90
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xa8
   __AUTH_CONST.__auth_got: 0x190
   __AUTH_CONST.__const: 0x980
   __AUTH_CONST.__cfstring: 0x820
-  __AUTH_CONST.__objc_const: 0x41d8
+  __AUTH_CONST.__objc_const: 0x3ae0
   __AUTH.__objc_data: 0x690
   __DATA.__objc_ivar: 0x148
   __DATA.__data: 0x4e0

   - /System/Library/PrivateFrameworks/IDSFoundation.framework/Versions/A/IDSFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4EC8BF8C-C0D2-3C4C-BD5A-DBCE30DABCE8
-  Functions: 663
-  Symbols:   1566
-  CStrings:  992
+  UUID: 0D0808BF-39D0-33AC-A9CA-7DDB6F453CCC
+  Functions: 679
+  Symbols:   1583
+  CStrings:  994
 
Symbols:
+ +[SKHandleInvitability logger].cold.1
+ +[SKInvitationPayload logger].cold.1
+ +[SKPresence _logger].cold.1
+ +[SKPresence _oversizeLogger].cold.1
+ +[SKPresenceDaemonConnection logger].cold.1
+ +[SKPresencePayload logger].cold.1
+ +[SKPresentDevice logger].cold.1
+ +[SKStatusPayload logger].cold.1
+ +[SKStatusProvisionPayload logger].cold.1
+ +[SKStatusPublishingDaemonConnection logger].cold.1
+ +[SKStatusPublishingService logger].cold.1
+ +[SKStatusSubscription logger].cold.1
+ +[SKStatusSubscriptionDaemonConnection logger].cold.1
+ +[SKStatusSubscriptionService logger].cold.1
+ -[SKStatusSubscriptionService personalStatusSubscriptionWithCompletion:]
+ GCC_except_table20
+ GCC_except_table34
+ GCC_except_table39
+ GCC_except_table44
+ GCC_except_table52
+ GCC_except_table53
+ GCC_except_table54
+ GCC_except_table72
+ GCC_except_table79
+ __123-[SKStatusSubscriptionService validatePersonalStatusSubscriptionMatchesSubscriptionValidationTokens:fromSender:completion:]_block_invoke.25
+ __123-[SKStatusSubscriptionService validatePersonalStatusSubscriptionMatchesSubscriptionValidationTokens:fromSender:completion:]_block_invoke.25.cold.1
+ __123-[SKStatusSubscriptionService validatePersonalStatusSubscriptionMatchesSubscriptionValidationTokens:fromSender:completion:]_block_invoke.25.cold.2
+ __123-[SKStatusSubscriptionService validatePersonalStatusSubscriptionMatchesSubscriptionValidationTokens:fromSender:completion:]_block_invoke.25.cold.3
+ __124-[SKStatusSubscriptionService allStatusSubscriptionsWithPersistentSubscriptionAssertionForApplicationIdentifier:completion:]_block_invoke.17
+ __124-[SKStatusSubscriptionService allStatusSubscriptionsWithPersistentSubscriptionAssertionForApplicationIdentifier:completion:]_block_invoke.17.cold.1
+ __71-[SKStatusSubscriptionService _registerForDelegateCallbacksIfNecessary]_block_invoke.30
+ __71-[SKStatusSubscriptionService _registerForDelegateCallbacksIfNecessary]_block_invoke.30.cold.1
+ __72-[SKStatusSubscriptionService personalStatusSubscriptionWithCompletion:]_block_invoke.9
+ __72-[SKStatusSubscriptionService personalStatusSubscriptionWithCompletion:]_block_invoke.9.cold.1
+ __72-[SKStatusSubscriptionService personalStatusSubscriptionWithCompletion:]_block_invoke.cold.1
+ __73-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveAssertions]_block_invoke.10
+ __73-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveAssertions]_block_invoke.10.cold.1
+ __73-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveAssertions]_block_invoke.10.cold.2
+ __73-[SKStatusSubscriptionService subscriptionInvitationReceived:completion:]_block_invoke.45
+ __75-[SKStatusSubscriptionService subscriptionReceivedStatusUpdate:completion:]_block_invoke.42
+ __75-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:error:]_block_invoke.20
+ __75-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:error:]_block_invoke.20.cold.1
+ __75-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:error:]_block_invoke.20.cold.2
+ __76-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveSubscriptions]_block_invoke.15
+ __76-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveSubscriptions]_block_invoke.15.cold.1
+ __76-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveSubscriptions]_block_invoke.15.cold.2
+ __80-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:completion:]_block_invoke.24
+ __80-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:completion:]_block_invoke.24.cold.1
+ __80-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:completion:]_block_invoke.24.cold.2
+ __83-[SKStatusSubscriptionService subscriptionStateChangedForSubscriptions:completion:]_block_invoke.37
+ __84-[SKStatusSubscriptionService _allStatusSubscriptionsIncludingPersonalSubscription:]_block_invoke.16
+ __84-[SKStatusSubscriptionService _allStatusSubscriptionsIncludingPersonalSubscription:]_block_invoke.16.cold.1
+ __84-[SKStatusSubscriptionService _allStatusSubscriptionsIncludingPersonalSubscription:]_block_invoke.16.cold.2
+ ___72-[SKStatusSubscriptionService personalStatusSubscriptionWithCompletion:]_block_invoke
- GCC_except_table22
- GCC_except_table36
- GCC_except_table41
- GCC_except_table46
- GCC_except_table50
- GCC_except_table69
- _OUTLINED_FUNCTION_7
- __123-[SKStatusSubscriptionService validatePersonalStatusSubscriptionMatchesSubscriptionValidationTokens:fromSender:completion:]_block_invoke.24
- __123-[SKStatusSubscriptionService validatePersonalStatusSubscriptionMatchesSubscriptionValidationTokens:fromSender:completion:]_block_invoke.24.cold.1
- __123-[SKStatusSubscriptionService validatePersonalStatusSubscriptionMatchesSubscriptionValidationTokens:fromSender:completion:]_block_invoke.24.cold.2
- __123-[SKStatusSubscriptionService validatePersonalStatusSubscriptionMatchesSubscriptionValidationTokens:fromSender:completion:]_block_invoke.24.cold.3
- __124-[SKStatusSubscriptionService allStatusSubscriptionsWithPersistentSubscriptionAssertionForApplicationIdentifier:completion:]_block_invoke.16
- __124-[SKStatusSubscriptionService allStatusSubscriptionsWithPersistentSubscriptionAssertionForApplicationIdentifier:completion:]_block_invoke.16.cold.1
- __71-[SKStatusSubscriptionService _registerForDelegateCallbacksIfNecessary]_block_invoke.29
- __71-[SKStatusSubscriptionService _registerForDelegateCallbacksIfNecessary]_block_invoke.29.cold.1
- __73-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveAssertions]_block_invoke.9
- __73-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveAssertions]_block_invoke.9.cold.1
- __73-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveAssertions]_block_invoke.9.cold.2
- __73-[SKStatusSubscriptionService subscriptionInvitationReceived:completion:]_block_invoke.44
- __75-[SKStatusSubscriptionService subscriptionReceivedStatusUpdate:completion:]_block_invoke.41
- __75-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:error:]_block_invoke.19
- __75-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:error:]_block_invoke.19.cold.1
- __75-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:error:]_block_invoke.19.cold.2
- __76-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveSubscriptions]_block_invoke.14
- __76-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveSubscriptions]_block_invoke.14.cold.1
- __76-[SKStatusSubscriptionService allStatusSubscriptionsWithActiveSubscriptions]_block_invoke.14.cold.2
- __80-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:completion:]_block_invoke.23
- __80-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:completion:]_block_invoke.23.cold.1
- __80-[SKStatusSubscriptionService subscriptionValidationTokensForHandle:completion:]_block_invoke.23.cold.2
- __83-[SKStatusSubscriptionService subscriptionStateChangedForSubscriptions:completion:]_block_invoke.36
- __84-[SKStatusSubscriptionService _allStatusSubscriptionsIncludingPersonalSubscription:]_block_invoke.15
- __84-[SKStatusSubscriptionService _allStatusSubscriptionsIncludingPersonalSubscription:]_block_invoke.15.cold.1
- __84-[SKStatusSubscriptionService _allStatusSubscriptionsIncludingPersonalSubscription:]_block_invoke.15.cold.2
CStrings:
+ "Fetching personal subscription (async) for statusType: %{public}@"
+ "personalStatusSubscriptionWithCompletion:"

```
