## remindd

> `/usr/libexec/remindd`

```diff

-1202.0.0.0.0
-  __TEXT.__text: 0x7531ec
+1203.0.0.0.0
+  __TEXT.__text: 0x7533a0
   __TEXT.__auth_stubs: 0x7a10
-  __TEXT.__objc_stubs: 0xfd60
+  __TEXT.__objc_stubs: 0xfd80
   __TEXT.__objc_methlist: 0x8b00
   __TEXT.__const: 0x205a4
-  __TEXT.__objc_methname: 0x21fd9
+  __TEXT.__objc_methname: 0x21fe6
   __TEXT.__objc_classname: 0x152f
   __TEXT.__objc_methtype: 0x36cc
   __TEXT.__gcc_except_tab: 0x2618
   __TEXT.__cstring: 0x1c427
-  __TEXT.__oslogstring: 0x5ab40
+  __TEXT.__oslogstring: 0x5ada0
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_typeref: 0x12efb
   __TEXT.__swift5_fieldmd: 0x98bc

   __TEXT.__swift5_proto: 0x1670
   __TEXT.__swift5_types: 0x9dc
   __TEXT.__swift5_mpenum: 0xa4
-  __TEXT.__unwind_info: 0x10978
+  __TEXT.__unwind_info: 0x10970
   __TEXT.__eh_frame: 0x1e534
   __DATA_CONST.__auth_got: 0x3d18
   __DATA_CONST.__got: 0x30c8
-  __DATA_CONST.__auth_ptr: 0x2f08
-  __DATA_CONST.__const: 0x23458
+  __DATA_CONST.__auth_ptr: 0x2bd8
+  __DATA_CONST.__const: 0x23450
   __DATA_CONST.__cfstring: 0x4ee0
   __DATA_CONST.__objc_classlist: 0xb10
   __DATA_CONST.__objc_catlist: 0x110

   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_doubleobj: 0x20
   __DATA.__objc_const: 0x1e668
-  __DATA.__objc_selrefs: 0x75f0
+  __DATA.__objc_selrefs: 0x75f8
   __DATA.__objc_ivar: 0x458
   __DATA.__objc_data: 0x80f8
   __DATA.__data: 0x1c620

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 22296
-  Symbols:   3816
-  CStrings:  11742
+  Functions: 22295
+  Symbols:   3815
+  CStrings:  11745
 
Symbols:
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
CStrings:
+ "REMNSPersistentHistoryTracking resultChangeSet: Did fetch transactions {author: %!{(MISSING)public}@, elapsedTime: %!l(MISSING)f ms, transactions.count: %!l(MISSING)lu}"
+ "REMNSPersistentHistoryTracking resultChangeSet: Did generate changeSet for transactions {author: %!{(MISSING)public}@, cumulativeElapsedTime: %!l(MISSING)f ms, transactions.count: %!l(MISSING)lu}"
+ "REMNSPersistentHistoryTracking resultChangeSet: Failed to fetch transactions {author: %!{(MISSING)public}@, elapsedTime: %!l(MISSING)f ms, error: %!@(MISSING)}"
+ "REMNSPersistentHistoryTracking resultChangeSet: Skipped generating changeSet for a transaction. Failed to get account objectID from storeID {storeID: %!@(MISSING)}"
+ "REMNSPersistentHistoryTracking resultChangeSet: Skipped generating changeSet for a transaction. REMNSPersistentHistoryTransaction has no storeID {transaction: %!@(MISSING)}"
+ "REMNSPersistentHistoryTracking resultChangeSet: Will fetch transactions {author: %!{(MISSING)public}@}"
+ "rem_log_fault_if(!historyResult) -- REMNSPersistentHistoryTracking resultChangeSet: Failed to get HistoryResult from request {request: %!@(MISSING)}"
+ "transactions"
- "COREDATA NSPersistentHistoryChangeRequest EXECUTED {author: %!{(MISSING)public}@, txn.count: %!l(MISSING)lu}"
- "COREDATA NSPersistentHistoryChangeRequest FAILED {author: %!{(MISSING)public}@, error: %!@(MISSING)}"
- "Failed to get account objectID from storeID {storeID: %!@(MISSING)}"
- "REMNSPersistentHistoryTransaction has no storeID {transaction: %!@(MISSING)}"
- "rem_log_fault_if(!historyResult) -- Failed to get HistoryResult from request {request: %!@(MISSING)}"

```
