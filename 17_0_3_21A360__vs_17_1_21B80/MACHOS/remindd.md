## remindd

> `/usr/libexec/remindd`

```diff

-948.0.0.0.0
-  __TEXT.__text: 0x73ff2c
+981.0.0.0.0
+  __TEXT.__text: 0x7417ac
   __TEXT.__auth_stubs: 0x5510
-  __TEXT.__objc_stubs: 0xf940
+  __TEXT.__objc_stubs: 0xf960
   __TEXT.__objc_methlist: 0x8610
-  __TEXT.__const: 0x1fa94
-  __TEXT.__objc_methname: 0x20f72
+  __TEXT.__const: 0x1fad4
+  __TEXT.__objc_methname: 0x20f9a
   __TEXT.__objc_classname: 0x148e
   __TEXT.__objc_methtype: 0x3638
   __TEXT.__gcc_except_tab: 0x1aa4
-  __TEXT.__cstring: 0x5a720
-  __TEXT.__oslogstring: 0x1a5af
+  __TEXT.__cstring: 0x5a890
+  __TEXT.__oslogstring: 0x1a5a2
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_typeref: 0x12b13
-  __TEXT.__swift5_fieldmd: 0x98b8
-  __TEXT.__constg_swiftt: 0xab74
+  __TEXT.__swift5_typeref: 0x12b7b
+  __TEXT.__swift5_fieldmd: 0x98d4
+  __TEXT.__constg_swiftt: 0xab98
   __TEXT.__swift5_builtin: 0x320
-  __TEXT.__swift5_reflstr: 0xb7bd
+  __TEXT.__swift5_reflstr: 0xb7ed
   __TEXT.__swift5_assocty: 0x20f8
-  __TEXT.__swift5_capture: 0x5b90
+  __TEXT.__swift5_capture: 0x5ba0
   __TEXT.__swift5_protos: 0x23c
-  __TEXT.__swift5_proto: 0x16b8
-  __TEXT.__swift5_types: 0x97c
+  __TEXT.__swift5_proto: 0x16bc
+  __TEXT.__swift5_types: 0x980
   __TEXT.__swift5_mpenum: 0xac
-  __TEXT.__unwind_info: 0x1258c
-  __TEXT.__eh_frame: 0x1e630
+  __TEXT.__unwind_info: 0x12580
+  __TEXT.__eh_frame: 0x1e600
   __DATA_CONST.__auth_got: 0x2a98
-  __DATA_CONST.__got: 0x17e8
+  __DATA_CONST.__got: 0x17f8
   __DATA_CONST.__auth_ptr: 0x990
-  __DATA_CONST.__const: 0x221e0
-  __DATA_CONST.__cfstring: 0x4bc0
+  __DATA_CONST.__const: 0x222b0
+  __DATA_CONST.__cfstring: 0x4c40
   __DATA_CONST.__objc_classlist: 0xa60
   __DATA_CONST.__objc_catlist: 0x168
   __DATA_CONST.__objc_protolist: 0x4c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_intobj: 0x360
+  __DATA_CONST.__objc_intobj: 0x378
   __DATA_CONST.__objc_arraydata: 0x2e0
   __DATA_CONST.__objc_arrayobj: 0x270
   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA.__objc_const: 0x1ce00
-  __DATA.__objc_selrefs: 0x7390
+  __DATA.__objc_selrefs: 0x7398
   __DATA.__objc_protorefs: 0x218
   __DATA.__objc_classrefs: 0xdb0
   __DATA.__objc_superrefs: 0x138
   __DATA.__objc_ivar: 0x42c
   __DATA.__objc_data: 0x74f0
-  __DATA.__data: 0x23d10
+  __DATA.__data: 0x23d60
   __DATA.__objc_stublist: 0x28
   __DATA.__bss: 0x21c30
   __DATA.__common: 0x8f0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 399C5516-33DA-327E-AAC1-11762FFE59AF
-  Functions: 26747
-  Symbols:   2802
-  CStrings:  12137
+  UUID: 1247FD3E-95EC-35F7-86F3-727A14628824
+  Functions: 26754
+  Symbols:   2804
+  CStrings:  12152
 
Symbols:
+ _$s19ReminderKitInternal18measureTimeElapsed_5level5blockSdSS_So13os_log_type_tayyKXEtKF
+ _$s19ReminderKitInternal24REMRemindersListDataViewO32GroceryAutoCategorizationMessageO13encodedStringSSSgvg
+ _REMRadarUtilitiesAlertMessageDefault
+ _REMRadarUtilitiesBugDescriptionDefault
- _$s19ReminderKitInternal18measureTimeElapsed_5blockSdSS_yyKXEtKF
- _$s19ReminderKitInternal24REMRemindersListDataViewO32GroceryAutoCategorizationMessageO20stringRepresentationSSSgvg
CStrings:
+ "%@\n%@"
+ "REMCDAlarm.generateNonce(): alarm does not belong to CK account, skip generateNonce() {alarmID: %{public}s}"
+ "REMCDAlarm.generateNonce(): alarm.reminder.account unexpectedly nil trying to call generateNonce() {alarmID: %{public}s}"
+ "executeSuggestConversionToGroceryList"
+ "groceryToast"
+ "ja"
+ "ko"
+ "nil localDeletedObjectIDs in RDStoreController.l_markAccountStoreDeletedAndDeleteData"
+ "os_transaction INIT {name: com.apple.remindd.RDGroceryOperationQueue.handleIncompleteOperationQueueItems}"
+ "os_transaction INIT {name: com.apple.remindd.RDTemplateOperationQueue.handleIncompleteOperationQueueItems}"
+ "os_transaction RELEASE {name: com.apple.remindd.RDGroceryOperationQueue.handleIncompleteOperationQueueItems}"
+ "os_transaction RELEASE {name: com.apple.remindd.RDTemplateOperationQueue.handleIncompleteOperationQueueItems}"
+ "removeHideEmptySectionsForGroceryList:"
+ "zh-Hans"
+ "zh-Hant"
- "%@.\nPlease run 'remindtool diagnose --privacy normal' and attach the generated diagnose tar file to the radar (However, if you do not wish to disclose your reminders database, run `remindtool diagnose` instead so the database ie excluded)."
- "REMReminderStorage.dueDateDeltaAlertsData should not practically be mutated, use `dueDateDeltaAlertsToUpsert` or `dueDateDeltaAlertIdentifiersToDelete` instead {callstack: %s}"
- "SET %@ <- %@"
- "You encountered a serious bug in remindd. Will you please file a Radar?"

```
