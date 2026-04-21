## ScreenTimeCore

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore`

```diff

-605.5.9.0.0
-  __TEXT.__text: 0xc42f8
+605.5.10.0.0
+  __TEXT.__text: 0xc4314
   __TEXT.__auth_stubs: 0x1620
   __TEXT.__objc_methlist: 0x9380
-  __TEXT.__const: 0x2400
-  __TEXT.__cstring: 0x9ccc
-  __TEXT.__oslogstring: 0xa01f
-  __TEXT.__gcc_except_tab: 0x1c34
+  __TEXT.__const: 0x2410
+  __TEXT.__cstring: 0x9c6c
+  __TEXT.__oslogstring: 0xa07f
+  __TEXT.__gcc_except_tab: 0x1c18
   __TEXT.__constg_swiftt: 0x8d0
   __TEXT.__swift5_typeref: 0xbb2
   __TEXT.__swift5_builtin: 0x78

   __TEXT.__unwind_info: 0x3068
   __TEXT.__eh_frame: 0x16e0
   __TEXT.__objc_classname: 0x1e50
-  __TEXT.__objc_methname: 0x19450
+  __TEXT.__objc_methname: 0x19470
   __TEXT.__objc_methtype: 0x2b51
   __TEXT.__objc_stubs: 0xe240
   __DATA_CONST.__got: 0xbf0

   __DATA_CONST.__objc_arraydata: 0x260
   __AUTH_CONST.__auth_got: 0xb20
   __AUTH_CONST.__const: 0x1d50
-  __AUTH_CONST.__cfstring: 0x94a0
-  __AUTH_CONST.__objc_const: 0x11b58
+  __AUTH_CONST.__cfstring: 0x9460
+  __AUTH_CONST.__objc_const: 0x11b68
   __AUTH_CONST.__objc_intobj: 0x180
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_arrayobj: 0x180

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: E7FC0FEE-4693-33CD-A00A-1E31D34401BD
-  Functions: 4779
+  UUID: 96A8B3C6-978C-320F-A177-821FA98C606D
+  Functions: 4778
   Symbols:   12613
-  CStrings:  7351
+  CStrings:  7349
 
Symbols:
+ ___104+[STBlueprint(UsageLimit) displayNameForUsageLimitWithCategoryIdentifiers:bundleIdentifiers:webDomains:]_block_invoke.58
- ___104+[STBlueprint(UsageLimit) displayNameForUsageLimitWithCategoryIdentifiers:bundleIdentifiers:webDomains:]_block_invoke.68
Functions:
~ +[STBlueprint(UsageLimit) saveUsageLimitWithIdentifier:user:bundleIdentifiers:webDomains:categoryIdentifiers:dailyBudgetLimit:budgetLimitByWeekday:enabled:behaviorType:error:] : 6512 -> 6600
- _OUTLINED_FUNCTION_7
~ +[STBlueprint(UsageLimit) saveUsageLimitWithIdentifier:user:bundleIdentifiers:webDomains:categoryIdentifiers:dailyBudgetLimit:budgetLimitByWeekday:enabled:behaviorType:error:].cold.1 : 128 -> 64
~ +[STBlueprint(UsageLimit) saveUsageLimitWithIdentifier:user:bundleIdentifiers:webDomains:categoryIdentifiers:dailyBudgetLimit:budgetLimitByWeekday:enabled:behaviorType:error:].cold.3 : 76 -> 84
~ +[STBlueprint(UsageLimit) saveUsageLimitWithIdentifier:user:bundleIdentifiers:webDomains:categoryIdentifiers:dailyBudgetLimit:budgetLimitByWeekday:enabled:behaviorType:error:].cold.4 : 76 -> 84
~ +[STBlueprint(UsageLimit) saveUsageLimitWithIdentifier:user:bundleIdentifiers:webDomains:categoryIdentifiers:dailyBudgetLimit:budgetLimitByWeekday:enabled:behaviorType:error:].cold.6 : 76 -> 84
CStrings:
+ "Attempted to save usage limit with no bundle identifiers, web domains, or category identifiers"
+ "lastPasscodeActivityNotificationSentDate"
- "STBlueprint+UsageLimit.m"
- "hasBundleIdentifiers || hasWebDomains || hasCategoryIdentifiers"

```
