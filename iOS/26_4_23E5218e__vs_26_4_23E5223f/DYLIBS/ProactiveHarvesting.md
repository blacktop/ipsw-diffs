## ProactiveHarvesting

> `/System/Library/PrivateFrameworks/ProactiveHarvesting.framework/ProactiveHarvesting`

```diff

-1311.5.0.1.0
-  __TEXT.__text: 0x3e2bc
+1311.6.0.0.0
+  __TEXT.__text: 0x3e3a4
   __TEXT.__auth_stubs: 0xa30
   __TEXT.__objc_methlist: 0x7b94
   __TEXT.__const: 0x19e
-  __TEXT.__gcc_except_tab: 0xad4
+  __TEXT.__gcc_except_tab: 0xad8
   __TEXT.__cstring: 0x252e
-  __TEXT.__oslogstring: 0x43c6
+  __TEXT.__oslogstring: 0x4425
   __TEXT.__unwind_info: 0xb90
-  __TEXT.__objc_classname: 0x57c
+  __TEXT.__objc_classname: 0x57e
   __TEXT.__objc_methname: 0x96fa
   __TEXT.__objc_methtype: 0xcd3
   __TEXT.__objc_stubs: 0x46a0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
-  UUID: 670F413B-0861-3E08-A0EA-13CB723FAC11
+  UUID: B033C6C8-F862-3277-9AE0-8C994E951649
   Functions: 2809
   Symbols:   7419
-  CStrings:  4166
+  CStrings:  4167
 
Symbols:
+ ___41-[HVQueue _deleteWithFilter:memory:disk:]_block_invoke.237
+ ___48-[HVQueue cleanupWithError:shouldContinueBlock:]_block_invoke.325
+ ___80-[HVQueue _filterBlockForBundleIdentifier:contentIdentifierSet:domainSelection:]_block_invoke.266
+ ___80-[HVQueue _filterBlockForBundleIdentifier:contentIdentifierSet:domainSelection:]_block_invoke.272
+ ___Block_byref_object_copy_.1125
+ ___Block_byref_object_copy_.1221
+ ___Block_byref_object_copy_.1754
+ ___Block_byref_object_copy_.249
+ ___Block_byref_object_dispose_.1126
+ ___Block_byref_object_dispose_.1222
+ ___Block_byref_object_dispose_.1755
+ ___Block_byref_object_dispose_.250
+ ___block_descriptor_144_e8_32s40s48s56s64bs72bs80r88r96r104r112r_e26_B24?0"BMStoreEvent"8^B16lr80l8s32l8r88l8u120l8r96l8u136l8r104l8s64l8s40l8s48l8s72l8r112l8s56l8
+ ___block_literal_global.1055
+ ___block_literal_global.1166
+ ___block_literal_global.1180
+ ___block_literal_global.1256
+ ___block_literal_global.15.1242
+ ___block_literal_global.1644
+ ___block_literal_global.1791
+ ___block_literal_global.1841
+ ___block_literal_global.1922
+ ___block_literal_global.268
+ ___block_literal_global.323
+ ___block_literal_global.370
+ ___block_literal_global.374
- ___41-[HVQueue _deleteWithFilter:memory:disk:]_block_invoke.236
- ___48-[HVQueue cleanupWithError:shouldContinueBlock:]_block_invoke.324
- ___80-[HVQueue _filterBlockForBundleIdentifier:contentIdentifierSet:domainSelection:]_block_invoke.265
- ___80-[HVQueue _filterBlockForBundleIdentifier:contentIdentifierSet:domainSelection:]_block_invoke.270
- ___Block_byref_object_copy_.1122
- ___Block_byref_object_copy_.1218
- ___Block_byref_object_copy_.1751
- ___Block_byref_object_copy_.248
- ___Block_byref_object_dispose_.1123
- ___Block_byref_object_dispose_.1219
- ___Block_byref_object_dispose_.1752
- ___Block_byref_object_dispose_.249
- ___block_descriptor_128_e8_32s40s48s56s64bs72bs80r88r96r104r_e26_B24?0"BMStoreEvent"8^B16lr80l8s32l8r88l8u112l8r96l8s64l8s40l8s48l8s72l8r104l8s56l8
- ___block_literal_global.1052
- ___block_literal_global.1163
- ___block_literal_global.1177
- ___block_literal_global.1253
- ___block_literal_global.15.1239
- ___block_literal_global.1641
- ___block_literal_global.1788
- ___block_literal_global.1838
- ___block_literal_global.1919
- ___block_literal_global.267
- ___block_literal_global.322
- ___block_literal_global.369
- ___block_literal_global.373
Functions:
~ ___41-[HVQueue _deleteWithFilter:memory:disk:]_block_invoke : 1728 -> 1800
~ ___80-[HVQueue _filterBlockForBundleIdentifier:contentIdentifierSet:domainSelection:]_block_invoke.271 : 372 -> 400
~ ___41-[HVQueue _deleteWithFilter:memory:disk:]_block_invoke.236 -> ___41-[HVQueue _deleteWithFilter:memory:disk:]_block_invoke.237 : 816 -> 976
~ ___80-[HVQueue _filterBlockForBundleIdentifier:contentIdentifierSet:domainSelection:]_block_invoke.270 -> ___80-[HVQueue _filterBlockForBundleIdentifier:contentIdentifierSet:domainSelection:]_block_invoke.272 : 400 -> 372
CStrings:
+ "5D` `"
+ "HVQueue<%{public}@>: deleteContentWithRequest: deleting old Mail event to mitigate 167995340!"
+ "Item %{public}@ is older than 90 days (creationDate: %{public}@, now: %{public}@, cutoff: %{public}@)"
- "5C`"
- "Item %{public}@ is older than a year (creationDate: %{public}@, now: %{public}@, cutoff: %{public}@)"

```
