## remindd

> `filesystem/usr/libexec/remindd`

```diff

-3973.11.0.0.0
-  __TEXT.__text: 0x812a90
+3975.0.0.0.0
+  __TEXT.__text: 0x812710
   __TEXT.__auth_stubs: 0x87c0
-  __TEXT.__objc_stubs: 0x1b760
+  __TEXT.__objc_stubs: 0x1b740
   __TEXT.__objc_methlist: 0xa8e0
-  __TEXT.__const: 0x287a8
-  __TEXT.__objc_methname: 0x27a11
+  __TEXT.__const: 0x287f8
+  __TEXT.__objc_methname: 0x279f1
   __TEXT.__objc_classname: 0x60b6
   __TEXT.__objc_methtype: 0x4267
   __TEXT.__gcc_except_tab: 0x2540
   __TEXT.__cstring: 0x180b7
-  __TEXT.__oslogstring: 0x5ea60
+  __TEXT.__oslogstring: 0x5e8b0
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_typeref: 0x14042
   __TEXT.__swift5_fieldmd: 0xa4e8

   __TEXT.__swift5_protos: 0x2d4
   __TEXT.__swift5_proto: 0x18e8
   __TEXT.__swift5_types: 0xafc
-  __TEXT.__swift_as_entry: 0x1a4
-  __TEXT.__swift_as_ret: 0x204
+  __TEXT.__swift_as_entry: 0x1a8
+  __TEXT.__swift_as_ret: 0x208
   __TEXT.__swift5_mpenum: 0xc4
-  __TEXT.__unwind_info: 0xff28
-  __TEXT.__eh_frame: 0x1f82c
+  __TEXT.__unwind_info: 0xff40
+  __TEXT.__eh_frame: 0x1f89c
   __DATA_CONST.__auth_got: 0x43f0
   __DATA_CONST.__got: 0x3418
   __DATA_CONST.__auth_ptr: 0x2820

   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_doubleobj: 0x30
   __DATA.__objc_const: 0x1d3c0
-  __DATA.__objc_selrefs: 0x7b00
+  __DATA.__objc_selrefs: 0x7af8
   __DATA.__objc_ivar: 0x480
   __DATA.__objc_data: 0x8450
-  __DATA.__data: 0x1e5e0
+  __DATA.__data: 0x1e630
   __DATA.__objc_stublist: 0x38
   __DATA.__bss: 0x237f0
   __DATA.__common: 0x9f0

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: CF530ACF-D3E7-3B30-9711-0A4D65F13820
-  Functions: 22210
+  UUID: 0FF0ADF3-C119-3204-A3C4-17D3D9C558E0
+  Functions: 22212
   Symbols:   4183
-  CStrings:  12688
+  CStrings:  12682
 
CStrings:
+ "RDUrgentAlarmConsumer: updateLastBannerPresentationDate END {reminderID: %{public}@, lastBannerPresentationDate: %{public}s}"
+ "RDUrgentAlarmConsumer: updateLastBannerPresentationDate FAIL {reminderID: %{public}@, error: %s}"
+ "RDUrgentAlarmConsumer: updateLastBannerPresentationDate START {reminderID: %{public}@, lastBannerPresentationDate: %{public}s}"
+ "TimeDataSourceAlarms: Failed to get REMReminder, REMAlarm or triggerEvent from cdTrigger -- skipping {cdTrigger: %@}"
- "RDUrgentAlarmConsumer: updateLastBannerPresentationDates END"
- "RDUrgentAlarmConsumer: updateLastBannerPresentationDates START\n     reminderCount: %ld"
- "RDUrgentAlarmConsumer: updateLastBannerPresentationDates {reminderID: %{public}@, lastBannerPresentationDate: %{public}s}"
- "RDUrgentAlarmConsumer: updateLastBannerPresentationDates | Save failed: %{public}s}"
- "TimeDataSourceAlarms: Failed to get REMReminder, REMAlarm from cdTrigger -- skipping {cdTrigger: %{public}@}"
- "TimeDataSourceAlarms: Failed to get fireDate from trigger -- skipping {cdTrigger: %{public}@}"
- "TimeDataSourceAlarms: Failed to unwrap cdAlarm or cdReminder -- skipping {cdTrigger: %{public}@}"
- "TimeDataSourceAlarms: Finished fetching alarms\n      input: %{public}*ld\n     result: %{public}*ld\n    skipped: %{public}*ld"
- "TimeDataSourceAlarms: Phantom reminder is missing account or list. Skipping {reminderID: %@}"
- "initWithStore:list:storage:"

```
