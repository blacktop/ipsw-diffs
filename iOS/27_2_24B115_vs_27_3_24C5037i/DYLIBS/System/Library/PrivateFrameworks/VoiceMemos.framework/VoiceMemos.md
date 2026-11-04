## VoiceMemos

> `/System/Library/PrivateFrameworks/VoiceMemos.framework/VoiceMemos`

```diff

-1446.1.1.0.0
-  __TEXT.__text: 0x460a4
-  __TEXT.__objc_methlist: 0x3f6c
+1453.0.0.0.0
+  __TEXT.__text: 0x46354
+  __TEXT.__objc_methlist: 0x3f7c
   __TEXT.__const: 0x2b8
-  __TEXT.__cstring: 0x6833
-  __TEXT.__oslogstring: 0x2f62
+  __TEXT.__cstring: 0x686d
+  __TEXT.__oslogstring: 0x2ff2
   __TEXT.__gcc_except_tab: 0x17e0
   __TEXT.__ustring: 0x22
-  __TEXT.__unwind_info: 0x2088
+  __TEXT.__unwind_info: 0x2098
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x98
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f30
+  __DATA_CONST.__objc_selrefs: 0x2f38
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0xf8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2000
-  Symbols:   3287
-  CStrings:  925
+  Functions: 2006
+  Symbols:   3292
+  CStrings:  929
 
Symbols:
+ -[RCSavedRecordingsModel existingUserFolderWithObjectID:]
+ GCC_except_table129
+ GCC_except_table144
+ GCC_except_table150
+ GCC_except_table155
+ GCC_except_table158
+ GCC_except_table161
+ GCC_except_table164
+ GCC_except_table167
+ GCC_except_table170
+ GCC_except_table173
+ GCC_except_table177
+ GCC_except_table180
+ _RCDeviceSupportsLiveActivitiesQFA
+ _RCLiveActivitiesQFAFeatureFlagIsEnabled
+ _RCLiveActivitiesQFAIsAvailable
- GCC_except_table128
- GCC_except_table143
- GCC_except_table149
- GCC_except_table154
- GCC_except_table157
- GCC_except_table160
- GCC_except_table163
- GCC_except_table166
- GCC_except_table169
- GCC_except_table172
- GCC_except_table176
Functions:
~ _RCDeviceSupportsOverdubRecording : 424 -> 468
+ -[RCSavedRecordingsModel existingUserFolderWithObjectID:]
+ _RCDeviceSupportsLiveActivitiesQFA
+ _RCLiveActivitiesQFAIsAvailable
+ _RCLiveActivitiesQFAFeatureFlagIsEnabled
~ ___108+[RCSavedRecordingsModel(ExportAdditions) fetchMetadataForRecordingWithUUID:includeAsset:completionHandler:]_block_invoke : 296 -> 548
+ -[RCSavedRecordingsModel existingUserFolderWithObjectID:].cold.1
~ ___108+[RCSavedRecordingsModel(ExportAdditions) fetchMetadataForRecordingWithUUID:includeAsset:completionHandler:]_block_invoke.cold.1 : 68 -> 76
+ ___108+[RCSavedRecordingsModel(ExportAdditions) fetchMetadataForRecordingWithUUID:includeAsset:completionHandler:]_block_invoke.2.cold.1
CStrings:
+ "%s -- Asset missing security scoped resource URL"
+ "%s -- ERROR: Unable to fetch user folder (%@.)"
+ "%s -- Failed to access security scoped resource"
+ "-[RCSavedRecordingsModel existingUserFolderWithObjectID:]"
```
