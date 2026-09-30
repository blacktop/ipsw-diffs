## ReminderKitDataConsumer

> `/System/Library/PrivateFrameworks/ExchangeSync.framework/Versions/A/DataConsumers/ReminderKitDataConsumer.dataconsumer/Contents/MacOS/ReminderKitDataConsumer`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2075.0.0.0.0
-  __TEXT.__text: 0x69d8
-  __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__objc_stubs: 0x1d60
-  __TEXT.__objc_methlist: 0x57c
-  __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x1e8
-  __TEXT.__objc_methname: 0x1ca6
-  __TEXT.__oslogstring: 0xfd9
+2080.200.31.0.0
+  __TEXT.__text: 0x7980
+  __TEXT.__auth_stubs: 0x1f0
+  __TEXT.__objc_stubs: 0x1fc0
+  __TEXT.__objc_methlist: 0x5d4
+  __TEXT.__const: 0xd0
+  __TEXT.__cstring: 0x1ec
+  __TEXT.__objc_methname: 0x1f44
+  __TEXT.__oslogstring: 0x135e
   __TEXT.__objc_classname: 0x4d
-  __TEXT.__objc_methtype: 0x38b
-  __TEXT.__unwind_info: 0x198
-  __DATA_CONST.__const: 0xd0
-  __DATA_CONST.__cfstring: 0x260
+  __TEXT.__objc_methtype: 0x3bf
+  __TEXT.__unwind_info: 0x1e0
+  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__cfstring: 0x280
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0xf8
-  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__auth_got: 0x100
+  __DATA_CONST.__got: 0x100
   __DATA.__objc_const: 0x480
-  __DATA.__objc_selrefs: 0x8e8
+  __DATA.__objc_selrefs: 0x980
   __DATA.__objc_ivar: 0x24
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x120

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 97
-  Symbols:   70
-  CStrings:  435
+  Functions: 119
+  Symbols:   74
+  CStrings:  463
 
Symbols:
+ _NSCalendarIdentifierGregorian
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSMutableDictionary
+ _objc_retainBlock
CStrings:
+ "B32@0:8@16^@24"
+ "B64@0:8@16@24@32@40@48@56"
+ "EXSReminderKitTaskDataConsumer Failed to save changeItem changes, discarding %lu identity write-back(s): %{private}@"
+ "EXSReminderKitTaskDataConsumer list lookup by external ID %{public}@ failed: %{private}@"
+ "EXSReminderKitTaskDataConsumer parent list for folder externalID=%{public}@ did not resolve from the stored object ID but exists; using it and repairing the folder row"
+ "EXSReminderKitTaskDataConsumer pushListChangeItem changeID=%ld externalID=%{public}@ is already present under a different object ID; updating it and repairing the folder row instead of adding a duplicate"
+ "EXSReminderKitTaskDataConsumer pushListChangeItem changeID=%ld externalID=%{public}@ was already staged by this batch; folding this change item onto it instead of adding a duplicate"
+ "EXSReminderKitTaskDataConsumer pushListChangeItem delete found no list for changeID=%ld externalID=%{public}@"
+ "EXSReminderKitTaskDataConsumer pushListChangeItem update failed, no list resolved for changeID=%ld externalID=%{public}@"
+ "EXSReminderKitTaskDataConsumer pushReminderChangeItem add failed to pull parent folder, dropping changeID=%ld externalID=%{public}@"
+ "EXSReminderKitTaskDataConsumer pushReminderChangeItem add failed to pull parent list, dropping changeID=%ld externalID=%{public}@ parentExternalID=%{public}@"
+ "ReminderKitDataConsumer: change token unchanged; no new Reminders history to consume for account: %@"
+ "ReminderKitDataConsumer: stored REMChangeToken is unusable as a cursor (comparison result %ld); forcing a full resync for account: %@"
+ "UTC"
+ "_dateComponents:fallOnSameDayAs:"
+ "_existingListWithExternalIdentifier:"
+ "_listChangeForParentFolder:withSaveRequest:stagedListChanges:pendingIdentityUpdates:"
+ "_stageListChange:forExternalID:stagedListChanges:pendingIdentityUpdates:"
+ "calendarWithIdentifier:"
+ "changeTokenPolicyForComparisonResult:"
+ "code"
+ "day"
+ "fetchListIncludingSpecialContainerWithExternalIdentifier:error:"
+ "itemDidFailToSync: kind=%{public}@ externalID=%{public}@ error=%{private}@"
+ "length"
+ "month"
+ "objectForKeyedSubscript:"
+ "pushListChangeItem:forAccountChange:withSaveRequest:preloadedLists:stagedListChanges:pendingIdentityUpdates:"
+ "pushReminderChangeItem:forAccountChange:withSaveRequest:preloadedReminders:stagedListChanges:pendingIdentityUpdates:"
+ "q24@0:8q16"
+ "rem_isAllDayDateComponents"
+ "rem_strippingTimeZone"
+ "reminderMinutesBeforeStartSpecified"
+ "saveRequestSynchronously:error:"
+ "setDueDateComponentsWithAlarmsIfNeeded:"
+ "setObject:forKeyedSubscript:"
+ "timeZoneWithName:"
+ "year"
- "EXSReminderKitTaskDataConsumer Failed to save changeItem changes: %{public}@"
- "EXSReminderKitTaskDataConsumer pushListChangeItem delete failed as change item %ld has no internal ID"
- "EXSReminderKitTaskDataConsumer pushListChangeItem update failed as change item %ld has no internal ID"
- "EXSReminderKitTaskDataConsumer pushReminderChangeItem add failed to pull parent folder"
- "EXSReminderKitTaskDataConsumer pushReminderChangeItem add failed to pull parent list"
- "ReminderKitDataConsumer: REMChangeTokenComparisonError comparing REMChangeTokens during reminders change processing for account: %@"
- "ReminderKitDataConsumer: Unexpected comparison result during reminders change processing for account: %@"
- "pushListChangeItem:forAccountChange:withSaveRequest:preloadedLists:"
- "pushReminderChangeItem:forAccountChange:withSaveRequest:preloadedReminders:"
- "setDueDateComponents:"
```
