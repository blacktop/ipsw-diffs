## CoreDuet

> `/System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet`

```diff

-1852.0.1.2.0
-  __TEXT.__text: 0x1918ec
+1852.4.2.0.3
+  __TEXT.__text: 0x191e14
   __TEXT.__auth_stubs: 0x1460
-  __TEXT.__objc_methlist: 0xfed4
-  __TEXT.__cstring: 0x174b9
-  __TEXT.__oslogstring: 0x17f71
+  __TEXT.__objc_methlist: 0xff2c
+  __TEXT.__cstring: 0x17546
+  __TEXT.__oslogstring: 0x17f49
   __TEXT.__const: 0x3d8
-  __TEXT.__gcc_except_tab: 0x60f4
+  __TEXT.__gcc_except_tab: 0x6114
   __TEXT.__dlopen_cstrs: 0x5e
-  __TEXT.__unwind_info: 0x52ec
+  __TEXT.__unwind_info: 0x532c
   __TEXT.__objc_classname: 0x2c28
-  __TEXT.__objc_methname: 0x24ca9
-  __TEXT.__objc_methtype: 0x6027
-  __TEXT.__objc_stubs: 0x166c0
+  __TEXT.__objc_methname: 0x24db7
+  __TEXT.__objc_methtype: 0x6040
+  __TEXT.__objc_stubs: 0x16760
   __DATA_CONST.__got: 0x340
-  __DATA_CONST.__const: 0x38c0
+  __DATA_CONST.__const: 0x3950
   __DATA_CONST.__objc_classlist: 0xc20
   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x1c680
-  __DATA_CONST.__objc_selrefs: 0x7b90
+  __DATA_CONST.__objc_selrefs: 0x7bd0
   __DATA_CONST.__objc_arraydata: 0x630
-  __AUTH_CONST.__cfstring: 0x12ea0
+  __AUTH_CONST.__cfstring: 0x12f00
   __AUTH_CONST.__objc_const: 0x8c30
-  __AUTH_CONST.__const: 0x1800
+  __AUTH_CONST.__const: 0x1860
   __AUTH_CONST.__objc_intobj: 0x2298
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x588

   __DATA.__objc_classrefs: 0xdf8
   __DATA.__objc_superrefs: 0x690
   __DATA.__objc_ivar: 0x179c
-  __DATA.__data: 0x21a0
-  __DATA.__bss: 0x368
+  __DATA.__data: 0x2190
+  __DATA.__bss: 0x390
   __DATA.__common: 0x38
   __DATA_DIRTY.__const: 0x18
   __DATA_DIRTY.__objc_data: 0x2f30

   - /usr/lib/libarchive.2.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 8816
-  Symbols:   27118
-  CStrings:  11749
+  Functions: 8825
+  Symbols:   27152
+  CStrings:  11765
 
Symbols:
+ +[_CDInteraction conversationIdPercentEscapes]
+ +[_CDInteraction inverseConversationIdPercentEscapes]
+ -[_CDAttachment descriptionRedacted:]
+ -[_CDAttachment redactedDescription]
+ -[_CDInteraction descriptionOfArray:redacted:]
+ -[_CDInteraction descriptionRedacted:]
+ -[_CDInteraction redactedDescription]
+ -[_DKThrottledActivity performNoMoreOftenInMinutesThan:name:queue:activityBlock:throttleBlock:]
+ GCC_except_table114
+ GCC_except_table62
+ ___46-[_CDInteraction descriptionOfArray:redacted:]_block_invoke
+ ___66+[_CDInteraction generateConversationIdFromInteractionRecipients:]_block_invoke
+ ___66+[_CDInteraction generateConversationIdFromInteractionRecipients:]_block_invoke_2
+ ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.536
+ ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.536.cold.1
+ ___67+[_CDInteraction recipientIdentifiersFromMobileMailConversationId:]_block_invoke
+ ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke.182
+ ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke.184
+ ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke.187
+ ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke_2.183
+ ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke_2.185
+ ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke_2.185.cold.1
+ ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke_2.185.cold.2
+ ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke_2.188
+ ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke_2.188.cold.1
+ ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke_2.188.cold.2
+ ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke_2.188.cold.3
+ ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke_2.188.cold.4
+ ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke_2.188.cold.5
+ ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.525
+ ___86-[_DKSyncCloudKitKnowledgeStorage performUpdateSourceDeviceIdentifiersWithCompletion:]_block_invoke_2
+ ___94-[_DKActivityThrottler _performOrScheduleWithTimeInterval:name:queue:activityBlock:callDepth:]_block_invoke.56
+ ___95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.540
+ ___95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.540.cold.1
+ ___95-[_DKThrottledActivity performNoMoreOftenInMinutesThan:name:queue:activityBlock:throttleBlock:]_block_invoke
+ ___block_descriptor_32_e30_"NSString"16?0"_CDContact"8l
+ ___block_descriptor_32_e35_q24?0"_CDContact"8"_CDContact"16l
+ ___block_descriptor_40_e8_32r_e18_"NSString"16?08lr32l8
+ ___block_descriptor_40_e8_32s_e22_v24?0"NSString"8^B16ls32l8
+ ___block_literal_global.416
+ ___block_literal_global.457
+ ___block_literal_global.503
+ ___block_literal_global.644
+ ___block_literal_global.647
+ ___block_literal_global.676
+ ___block_literal_global.836
+ ___initPercentEscapes_block_invoke
+ __unnamed_array_storage.542
+ __unnamed_array_storage.559
+ _initPercentEscapes.onceToken
+ _inversePercentEscapes
+ _objc_msgSend$addCharactersInRange:
+ _objc_msgSend$conversationIdPercentEscapes
+ _objc_msgSend$descriptionOfArray:redacted:
+ _objc_msgSend$descriptionRedacted:
+ _objc_msgSend$enumerateLinesUsingBlock:
+ _objc_msgSend$generateConversationIdFromHandle:
+ _objc_msgSend$inverseConversationIdPercentEscapes
+ _objc_msgSend$performNoMoreOftenInMinutesThan:name:queue:activityBlock:throttleBlock:
+ _objc_msgSend$rangeOfCharacterFromSet:options:
+ _objc_msgSend$redactedDescription
+ _percentEscapes
+ _sharedInstance.initialized.413
+ _sharedInstance.initialized.454
+ _sharedInstance.sharedInstance.414
+ _sharedInstance.sharedInstance.455
- +[_CDInteraction generateConversationIdFromHandle:].cold.1
- +[_CDInteraction generateConversationIdFromInteractionRecipients:].cold.1
- +[_CDInteraction generateConversationIdFromInteractionRecipients:].cold.2
- -[_CDInteraction descriptionOfArray:]
- GCC_except_table112
- GCC_except_table61
- ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.539
- ___66-[_CDSpotlightItemRecorder addUserAction:withItem:withCompletion:]_block_invoke.539.cold.1
- ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke.181
- ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke.183
- ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke.186
- ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke_2.182
- ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke_2.184
- ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke_2.184.cold.1
- ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke_2.184.cold.2
- ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke_2.187
- ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke_2.187.cold.1
- ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke_2.187.cold.2
- ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke_2.187.cold.3
- ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke_2.187.cold.4
- ___67-[_DKSyncCloudKitKnowledgeStorage fetchChangedZonesWithCompletion:]_block_invoke_2.187.cold.5
- ___79-[_CDSpotlightItemRecorder addOrUpdateSearchableItems:bundleID:withCompletion:]_block_invoke.528
- ___94-[_DKActivityThrottler _performOrScheduleWithTimeInterval:name:queue:activityBlock:callDepth:]_block_invoke.54
- ___95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.543
- ___95-[_CDSpotlightItemRecorder deleteSearchableItemsWithDomainIdentifiers:bundleID:withCompletion:]_block_invoke.543.cold.1
- ___block_literal_global.456
- ___block_literal_global.506
- ___block_literal_global.654
- __unnamed_array_storage.545
- __unnamed_array_storage.562
- _objc_msgSend$derivedIntentId
- _objc_msgSend$descriptionOfArray:
- _objc_msgSend$domainId
- _objc_msgSend$performWithMinimumIntervalInMinutesOf:name:queue:activityBlock:
- _objc_msgSend$recipientsId
- _sharedInstance.initialized.453
- _sharedInstance.sharedInstance.454
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightRecorder.m:559"
+ "@\"NSString\"16@?0@\"_CDContact\"8"
+ "@\"NSString\"16@?0@8"
+ "Missing sharingSourceBundleID or targetBundleID on share sheet feedback for interaction %{sensitive}@"
+ "No corresponding share sheet feedback for interaction %{sensitive}@"
+ "Not recording %{sensitive}@ as it is not a valid interaction, error: %@"
+ "Performing privacy maintenance for installedAppExtensions: %@"
+ "Performing privacy maintenance for installedApps: %@"
+ "Publishing deleted XPC event with interactions %{sensitive}@"
+ "Publishing recorded XPC event with interactions %{sensitive}@"
+ "addCharactersInRange:"
+ "conversationIdPercentEscapes"
+ "descriptionOfArray:redacted:"
+ "descriptionRedacted:"
+ "enumerateLinesUsingBlock:"
+ "inverseConversationIdPercentEscapes"
+ "performNoMoreOftenInMinutesThan:name:queue:activityBlock:throttleBlock:"
+ "q24@?0@\"_CDContact\"8@\"_CDContact\"16"
+ "rangeOfCharacterFromSet:options:"
+ "recordInteractionsBatch - recorded %tu interactions, %{sensitive}@"
+ "recordInteractionsBatch - recording: %tu interactions %{sensitive}@"
+ "redacted"
+ "redacted (%tu items)"
+ "redactedDescription"
+ "v24@?0@\"NSString\"8^B16"
+ "v56@0:8d16@24@32@?40@?48"
- "/Library/Caches/com.apple.xbs/Sources/CoreDuet/CoreDuetFramework/CoreDuetFramework/_CDSpotlightRecorder.m:557"
- "Conversation ID for recipients %@ not generated since JSON serialization failed: %@"
- "Conversation ID for recipients not generated since some recipient has nil identifier"
- "Missing sharingSourceBundleID or targetBundleID on share sheet feedback for interaction %{private}@"
- "No corresponding share sheet feedback for interaction %{private}@"
- "Not recording %{private}@ as it is not a valid interaction, error: %@"
- "Publishing deleted XPC event with interactions %{private}@"
- "Publishing recorded XPC event with interactions %{private}@"
- "descriptionOfArray:"
- "recordInteractionsBatch - recorded %tu interactions, %{private}@"
- "recordInteractionsBatch - recording: %tu interactions %{private}@"

```
