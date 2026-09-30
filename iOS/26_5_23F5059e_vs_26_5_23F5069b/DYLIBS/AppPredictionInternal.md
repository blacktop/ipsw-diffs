## AppPredictionInternal

> `/System/Library/PrivateFrameworks/AppPredictionInternal.framework/AppPredictionInternal`

```diff

-627.12.0.0.0
-  __TEXT.__text: 0x4a0f0c
+627.13.0.1.0
+  __TEXT.__text: 0x4a10a4
   __TEXT.__auth_stubs: 0x40e0
-  __TEXT.__objc_methlist: 0x38d44
+  __TEXT.__objc_methlist: 0x38d4c
   __TEXT.__const: 0x423a
   __TEXT.__cstring: 0x58a72
-  __TEXT.__oslogstring: 0x3b0c9
+  __TEXT.__oslogstring: 0x3b139
   __TEXT.__gcc_except_tab: 0xfea0
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__ustring: 0x90

   __TEXT.__unwind_info: 0xf428
   __TEXT.__eh_frame: 0x2774
   __TEXT.__objc_classname: 0x9a2a
-  __TEXT.__objc_methname: 0xaefbc
+  __TEXT.__objc_methname: 0xaefdc
   __TEXT.__objc_methtype: 0x18444
-  __TEXT.__objc_stubs: 0x4d9e0
-  __DATA_CONST.__got: 0x39b8
+  __TEXT.__objc_stubs: 0x4da00
+  __DATA_CONST.__got: 0x39c0
   __DATA_CONST.__const: 0xbfb8
   __DATA_CONST.__objc_classlist: 0x1f88
   __DATA_CONST.__objc_catlist: 0x138
   __DATA_CONST.__objc_protolist: 0x4d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1be90
+  __DATA_CONST.__objc_selrefs: 0x1be98
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x1520
   __DATA_CONST.__objc_arraydata: 0x1298

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 426288F4-439C-3990-BA6F-B075F3628C57
-  Functions: 25674
-  Symbols:   77861
-  CStrings:  42931
+  UUID: 5EA62833-0F35-306F-B9A1-29570FD70678
+  Functions: 25675
+  Symbols:   77865
+  CStrings:  42933
 
Symbols:
+ -[ATXNotificationAndSuggestionDatabase _purgeNotificationBiomeStreamsIfNeeded]
+ GCC_except_table173
+ GCC_except_table178
+ ___47-[ATXNotificationAndSuggestionDatabase analyze]_block_invoke.341
+ ___47-[ATXNotificationAndSuggestionDatabase analyze]_block_invoke.341.cold.1
+ ___53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.289
+ ___53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.289.cold.1
+ ___53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.290
+ ___53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.290.cold.1
+ ___64-[ATXNotificationAndSuggestionDatabase currentActiveSuggestions]_block_invoke.204
+ ___64-[ATXNotificationAndSuggestionDatabase currentActiveSuggestions]_block_invoke.204.cold.1
+ ___68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke.131
+ ___68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke_2.132
+ ___68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke_3.133
+ ___68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke_3.133.cold.1
+ ___79-[ATXNotificationAndSuggestionDatabase allBundleIdsOfNotificationsOnLockscreen]_block_invoke.286
+ ___79-[ATXNotificationAndSuggestionDatabase allBundleIdsOfNotificationsOnLockscreen]_block_invoke.286.cold.1
+ ___84-[ATXNotificationAndSuggestionDatabase allNotificationsFromBundleId:sinceTimestamp:]_block_invoke.276
+ ___84-[ATXNotificationAndSuggestionDatabase allNotificationsFromBundleId:sinceTimestamp:]_block_invoke.276.cold.1
+ ___89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke.317
+ ___89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke.326
+ ___89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke.333
+ ___89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.327
+ ___89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.327.cold.1
+ ___89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.335
+ ___89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.335.cold.1
+ ___91-[ATXNotificationAndSuggestionDatabase pruneNotificationsBasedOnHardLimitsWithXPCActivity:]_block_invoke.304
+ ___91-[ATXNotificationAndSuggestionDatabase pruneNotificationsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.306
+ ___91-[ATXNotificationAndSuggestionDatabase pruneNotificationsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.306.cold.1
+ ___block_literal_global.197
+ ___block_literal_global.229
+ ___block_literal_global.282
+ ___block_literal_global.288
+ ___block_literal_global.308
+ ___block_literal_global.322
+ ___block_literal_global.329
+ ___block_literal_global.337
+ ___block_literal_global.343
+ __kATXBiomeNotificationPurgeCompleteKey
+ _objc_msgSend$_purgeNotificationBiomeStreamsIfNeeded
- GCC_except_table172
- GCC_except_table177
- ___47-[ATXNotificationAndSuggestionDatabase analyze]_block_invoke.337
- ___47-[ATXNotificationAndSuggestionDatabase analyze]_block_invoke.337.cold.1
- ___53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.285
- ___53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.285.cold.1
- ___53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.286
- ___53-[ATXNotificationAndSuggestionDatabase deleteAllData]_block_invoke.286.cold.1
- ___64-[ATXNotificationAndSuggestionDatabase currentActiveSuggestions]_block_invoke.200
- ___64-[ATXNotificationAndSuggestionDatabase currentActiveSuggestions]_block_invoke.200.cold.1
- ___68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke.127
- ___68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke_2.128
- ___68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke_3.129
- ___68-[ATXNotificationAndSuggestionDatabase updateNotificationFromEvent:]_block_invoke_3.129.cold.1
- ___79-[ATXNotificationAndSuggestionDatabase allBundleIdsOfNotificationsOnLockscreen]_block_invoke.282
- ___79-[ATXNotificationAndSuggestionDatabase allBundleIdsOfNotificationsOnLockscreen]_block_invoke.282.cold.1
- ___84-[ATXNotificationAndSuggestionDatabase allNotificationsFromBundleId:sinceTimestamp:]_block_invoke.272
- ___84-[ATXNotificationAndSuggestionDatabase allNotificationsFromBundleId:sinceTimestamp:]_block_invoke.272.cold.1
- ___89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke.313
- ___89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke.322
- ___89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke.329
- ___89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.323
- ___89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.323.cold.1
- ___89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.331
- ___89-[ATXNotificationAndSuggestionDatabase pruneSuggestionsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.331.cold.1
- ___91-[ATXNotificationAndSuggestionDatabase pruneNotificationsBasedOnHardLimitsWithXPCActivity:]_block_invoke.296
- ___91-[ATXNotificationAndSuggestionDatabase pruneNotificationsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.302
- ___91-[ATXNotificationAndSuggestionDatabase pruneNotificationsBasedOnHardLimitsWithXPCActivity:]_block_invoke_2.302.cold.1
- ___block_literal_global.187
- ___block_literal_global.189
- ___block_literal_global.225
- ___block_literal_global.278
- ___block_literal_global.284
- ___block_literal_global.304
- ___block_literal_global.318
- ___block_literal_global.325
- ___block_literal_global.333
- ___block_literal_global.339
Functions:
~ -[ATXNotificationsLoggingServer logNotificationEvent:notification:reason:interactionUI:] : 1328 -> 1464
~ -[ATXNotificationAndSuggestionDatabase init] : 160 -> 168
+ -[ATXNotificationAndSuggestionDatabase _purgeNotificationBiomeStreamsIfNeeded]
CStrings:
+ "ATXNotificationAndSuggestionDatabase: Purging private notification streams to remove persisted text content"
+ "_purgeNotificationBiomeStreamsIfNeeded"

```
