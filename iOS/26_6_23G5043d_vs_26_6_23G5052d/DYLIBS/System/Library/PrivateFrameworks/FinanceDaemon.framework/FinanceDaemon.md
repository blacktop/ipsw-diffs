## FinanceDaemon

> `/System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon`

```diff

-  __TEXT.__text: 0x2e0728
-  __TEXT.__auth_stubs: 0x9410
+  __TEXT.__text: 0x2e03a4
+  __TEXT.__auth_stubs: 0x93f0
   __TEXT.__objc_methlist: 0x760
-  __TEXT.__const: 0xe568
-  __TEXT.__cstring: 0x837f
-  __TEXT.__oslogstring: 0xc9d1
-  __TEXT.__swift5_typeref: 0x60c0
+  __TEXT.__const: 0xe5d8
+  __TEXT.__cstring: 0x838f
+  __TEXT.__oslogstring: 0xca51
+  __TEXT.__swift5_typeref: 0x60f2
   __TEXT.__swift5_capture: 0x1b5c
-  __TEXT.__swift5_fieldmd: 0x4a4c
-  __TEXT.__constg_swiftt: 0x4fc8
-  __TEXT.__swift5_reflstr: 0x5753
+  __TEXT.__swift5_fieldmd: 0x4a68
+  __TEXT.__constg_swiftt: 0x4fe4
+  __TEXT.__swift5_reflstr: 0x5773
   __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_assocty: 0x7d8
   __TEXT.__swift5_protos: 0x11c
-  __TEXT.__swift5_proto: 0x858
-  __TEXT.__swift5_types: 0x57c
+  __TEXT.__swift5_proto: 0x85c
+  __TEXT.__swift5_types: 0x580
   __TEXT.__swift_as_entry: 0x768
   __TEXT.__swift_as_ret: 0x898
   __TEXT.__swift5_mpenum: 0x44
-  __TEXT.__unwind_info: 0x7ea8
-  __TEXT.__eh_frame: 0x1928c
+  __TEXT.__unwind_info: 0x7ed0
+  __TEXT.__eh_frame: 0x19304
   __TEXT.__objc_classname: 0x1521
-  __TEXT.__objc_methname: 0x58ed
+  __TEXT.__objc_methname: 0x593d
   __TEXT.__objc_methtype: 0x8c1
-  __TEXT.__objc_stubs: 0x56e0
-  __DATA_CONST.__got: 0x21c8
+  __TEXT.__objc_stubs: 0x5740
+  __DATA_CONST.__got: 0x21d0
   __DATA_CONST.__const: 0x1b0
   __DATA_CONST.__objc_classlist: 0x2b0
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1850
+  __DATA_CONST.__objc_selrefs: 0x1868
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x4a10
-  __AUTH_CONST.__const: 0x9ab8
+  __AUTH_CONST.__auth_got: 0x4a00
+  __AUTH_CONST.__const: 0x9b68
   __AUTH_CONST.__objc_const: 0x5508
   __AUTH.__objc_data: 0x408
   __AUTH.__data: 0x5838
   __DATA.__objc_ivar: 0x8
-  __DATA.__data: 0x36f8
+  __DATA.__data: 0x3708
   __DATA.__bss: 0xcd10
   __DATA.__common: 0x58
   __DATA_DIRTY.__objc_data: 0x518

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 7929
-  Symbols:   3987
-  CStrings:  2709
+  Functions: 7935
+  Symbols:   3993
+  CStrings:  2717
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_capture : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ _OBJC_CLASS_$_NSBatchUpdateResult
+ _objc_msgSend$lastNotifiedOrderUpdateDate
+ _objc_msgSend$mergeChangesFromRemoteContextSave:intoContexts:
+ _objc_msgSend$setLastNotifiedOrderUpdateDate:
+ _symbolic _____ 13FinanceDaemon50PostInstallBackfillLastNotifiedOrderUpdateDateTaskV
+ _symbolic ________________Sg35previousLastNotifiedOrderUpdateDatet 10FinanceKit21ManagedExtractedOrderC AA07TrackedE0O0A6DaemonE7ChangesV 10Foundation4DateV
+ _type_layout_string 13FinanceDaemon50PostInstallBackfillLastNotifiedOrderUpdateDateTaskV
- _symbolic ___________t 10FinanceKit21ManagedExtractedOrderC AA07TrackedE0O0A6DaemonE7ChangesV
CStrings:
+ "  previousLastNotifiedOrderUpdateDate "
+ "Backfilled lastNotifiedOrderUpdateDate for %ld extracted orders"
+ "Order update date %s has not advanced past last-notified watermark %s, skipping scheduling notifications."
+ "Successfully pruned: %ld invalid PassKit transaction(s) and %ld dangling public transaction(s). and %ld dangling action(s)."
+ "backfillLastNotifiedOrderUpdateDate"
+ "lastNotifiedOrderUpdateDate"
+ "mergeChangesFromRemoteContextSave:intoContexts:"
+ "orderContent.orderUpdateDate"
+ "setLastNotifiedOrderUpdateDate:"
- "SUBQUERY(\n    transactionObjects,\n    $transaction,\n    $transaction.insightsObject != SELF\n).@count == transactionObjects.@count"
- "Successfully pruned: %ld invalid PassKit transaction(s) and %ld dangling public transaction(s). and %ld dangling action(s). and %ld dangling insight(s)."

```
