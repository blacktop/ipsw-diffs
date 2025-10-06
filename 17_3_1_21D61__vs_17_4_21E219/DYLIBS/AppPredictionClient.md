## AppPredictionClient

> `/System/Library/PrivateFrameworks/AppPredictionClient.framework/AppPredictionClient`

```diff

-541.10.1.0.0
-  __TEXT.__text: 0x168654
+541.14.0.0.0
+  __TEXT.__text: 0x168658
   __TEXT.__auth_stubs: 0xe50
   __TEXT.__objc_methlist: 0x14818
   __TEXT.__const: 0x568

   __TEXT.__ustring: 0x18a
   __TEXT.__unwind_info: 0x5cb8
   __TEXT.__objc_classname: 0x33aa
-  __TEXT.__objc_methname: 0x2d547
+  __TEXT.__objc_methname: 0x2d56f
   __TEXT.__objc_methtype: 0x5ede
   __TEXT.__objc_stubs: 0x19840
   __DATA_CONST.__got: 0x2d8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x34858
   __DATA_CONST.__objc_selrefs: 0x8ae8
+  __DATA_CONST.__objc_protorefs: 0x98
+  __DATA_CONST.__objc_classrefs: 0x1260
+  __DATA_CONST.__objc_superrefs: 0xa88
   __DATA_CONST.__objc_arraydata: 0xaf0
   __AUTH_CONST.__cfstring: 0x12fa0
   __AUTH_CONST.__objc_const: 0xa5f8

   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__auth_got: 0x738
-  __AUTH.__objc_data: 0x3318
-  __DATA.__objc_protorefs: 0x98
-  __DATA.__objc_classrefs: 0x1260
-  __DATA.__objc_superrefs: 0xa88
+  __AUTH.__objc_data: 0x32c8
   __DATA.__objc_ivar: 0x18d8
-  __DATA.__data: 0x18e8
-  __DATA.__bss: 0x280
-  __DATA_DIRTY.__objc_data: 0x4678
+  __DATA.__data: 0x1900
+  __DATA.__bss: 0x268
+  __DATA_DIRTY.__objc_data: 0x46c8
   __DATA_DIRTY.__data: 0x88
   __DATA_DIRTY.__bss: 0x2a0
   - /System/Library/Frameworks/Contacts.framework/Contacts

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 21B27BC7-B42F-386A-8FA8-ADA0D95AEE52
+  UUID: 50937CA8-87B5-345E-A202-38BEB5F76319
   Functions: 9803
   Symbols:   31053
-  CStrings:  14288
+  CStrings:  14290
 
Symbols:
+ __OBJC_$_PROP_LIST_ATXActivitySuggestion.65
+ ___41-[ATXNotificationDigestRankerClient init]_block_invoke.64
+ ___42-[ATXWatchFaceConfigurationCollector init]_block_invoke.179
+ ___42-[ATXWatchFaceConfigurationCollector init]_block_invoke.179.cold.1
+ ___45-[ATXLockScreenNotificationRankerClient init]_block_invoke.55
+ ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.315
+ ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.315.cold.1
+ ___60-[ATXWatchFaceConfigurationCollector refreshWithCompletion:]_block_invoke.183
+ ___60-[ATXWatchFaceConfigurationCollector refreshWithCompletion:]_block_invoke.183.cold.1
+ ___60-[ATXWatchFaceConfigurationCollector refreshWithCompletion:]_block_invoke.183.cold.2
+ ___60-[ATXWatchFaceConfigurationCollector refreshWithCompletion:]_block_invoke.183.cold.3
+ ___60-[ATXWatchFaceConfigurationCollector refreshWithCompletion:]_block_invoke.183.cold.4
+ ___60-[ATXWatchFaceConfigurationCollector refreshWithCompletion:]_block_invoke.194
+ ___73+[ATXSpotlightClient rerankRecents_LimitCount:oneCountDays:twoCountDays:]_block_invoke.219
+ ___73+[ATXSpotlightClient rerankRecents_LimitCount:oneCountDays:twoCountDays:]_block_invoke.219.cold.1
+ ___73+[ATXSpotlightClient rerankRecents_LimitCount:oneCountDays:twoCountDays:]_block_invoke.219.cold.2
+ ___94-[ATXNotificationDigestRankerClient appsSortedByNotificationsReceivedInPreviousNumDays:reply:]_block_invoke.83
+ ___block_literal_global.178
+ ___block_literal_global.199
+ ___block_literal_global.202
+ ___block_literal_global.288
+ ___block_literal_global.327
+ ___block_literal_global.330
+ ___block_literal_global.66
+ __unnamed_array_storage.292
- __OBJC_$_PROP_LIST_ATXActivitySuggestion.64
- ___41-[ATXNotificationDigestRankerClient init]_block_invoke.63
- ___42-[ATXWatchFaceConfigurationCollector init]_block_invoke.178
- ___42-[ATXWatchFaceConfigurationCollector init]_block_invoke.178.cold.1
- ___45-[ATXLockScreenNotificationRankerClient init]_block_invoke.54
- ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.291
- ___48+[ATXContactModeEntity vipContactEmailAddresses]_block_invoke.291.cold.1
- ___60-[ATXWatchFaceConfigurationCollector refreshWithCompletion:]_block_invoke.182
- ___60-[ATXWatchFaceConfigurationCollector refreshWithCompletion:]_block_invoke.182.cold.1
- ___60-[ATXWatchFaceConfigurationCollector refreshWithCompletion:]_block_invoke.182.cold.2
- ___60-[ATXWatchFaceConfigurationCollector refreshWithCompletion:]_block_invoke.182.cold.3
- ___60-[ATXWatchFaceConfigurationCollector refreshWithCompletion:]_block_invoke.182.cold.4
- ___60-[ATXWatchFaceConfigurationCollector refreshWithCompletion:]_block_invoke.193
- ___73+[ATXSpotlightClient rerankRecents_LimitCount:oneCountDays:twoCountDays:]_block_invoke.216
- ___73+[ATXSpotlightClient rerankRecents_LimitCount:oneCountDays:twoCountDays:]_block_invoke.216.cold.1
- ___73+[ATXSpotlightClient rerankRecents_LimitCount:oneCountDays:twoCountDays:]_block_invoke.216.cold.2
- ___94-[ATXNotificationDigestRankerClient appsSortedByNotificationsReceivedInPreviousNumDays:reply:]_block_invoke.82
- ___block_literal_global.177
- ___block_literal_global.180
- ___block_literal_global.198
- ___block_literal_global.201
- ___block_literal_global.287
- ___block_literal_global.326
- ___block_literal_global.329
- __unnamed_array_storage.290
CStrings:
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",?,R,C,N"

```
