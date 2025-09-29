## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-1062.0.1.0.1
-  __TEXT.__text: 0x5ee0dc
+1062.0.1.0.2
+  __TEXT.__text: 0x5ee1fc
   __TEXT.__auth_stubs: 0x2190
   __TEXT.__objc_methlist: 0x31038
   __TEXT.__const: 0x4658
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__swift5_typeref: 0x1d3
-  __TEXT.__oslogstring: 0x76586
+  __TEXT.__oslogstring: 0x765cb
   __TEXT.__cstring: 0x454a7
   __TEXT.__swift5_capture: 0x9c
   __TEXT.__swift_as_entry: 0x18

   __TEXT.__unwind_info: 0xdc78
   __TEXT.__eh_frame: 0x390
   __TEXT.__objc_classname: 0x58ca
-  __TEXT.__objc_methname: 0x915e9
-  __TEXT.__objc_methtype: 0xcfa5
+  __TEXT.__objc_methname: 0x915e6
+  __TEXT.__objc_methtype: 0xcfa2
   __TEXT.__objc_stubs: 0x55b00
   __DATA_CONST.__got: 0x30f8
   __DATA_CONST.__const: 0xf538

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F78E139F-AD2C-322D-BBE6-B6217C03F8C3
+  UUID: 740DD24C-309D-3136-9C9C-88B725DFF667
   Functions: 20187
   Symbols:   65174
-  CStrings:  40164
+  CStrings:  40165
 
Symbols:
+ -[RTPersistenceMirroringManager _countChangesInTransactionsFromContext:store:startingToken:error:]
+ -[RTPersistenceMirroringManager _fetchHistoryTransactionBatchFromContext:store:fromToken:limit:error:]
+ _objc_msgSend$_countChangesInTransactionsFromContext:store:startingToken:error:
+ _objc_msgSend$_fetchHistoryTransactionBatchFromContext:store:fromToken:limit:error:
- -[RTPersistenceMirroringManager _countChangesInTransactionsFromContext:store:predicate:error:]
- -[RTPersistenceMirroringManager _fetchHistoryTransactionBatchFromContext:store:predicate:offset:limit:error:]
- _objc_msgSend$_countChangesInTransactionsFromContext:store:predicate:error:
- _objc_msgSend$_fetchHistoryTransactionBatchFromContext:store:predicate:offset:limit:error:
Functions:
~ -[RTPersistenceMirroringManager _fetchHistoryTransactionBatchFromContext:store:predicate:offset:limit:error:] -> -[RTPersistenceMirroringManager _fetchHistoryTransactionBatchFromContext:store:fromToken:limit:error:] : 452 -> 680
~ -[RTPersistenceMirroringManager _changeCountForManagedObjectContext:currentExporterToken:error:] : 896 -> 660
~ -[RTPersistenceMirroringManager _countChangesInTransactionsFromContext:store:predicate:error:] -> -[RTPersistenceMirroringManager _countChangesInTransactionsFromContext:store:startingToken:error:] : 988 -> 1284
CStrings:
+ "%@, currentToken, %@, transactionNumber, %lld, transactionCount, %lu"
+ "21:03:41"
+ "@56@0:8@16@24@32Q40^@48"
+ "Sep 18 2025"
+ "_countChangesInTransactionsFromContext:store:startingToken:error:"
+ "_fetchHistoryTransactionBatchFromContext:store:fromToken:limit:error:"
- "21:56:50"
- "@64@0:8@16@24@32Q40Q48^@56"
- "Aug 25 2025"
- "_countChangesInTransactionsFromContext:store:predicate:error:"
- "_fetchHistoryTransactionBatchFromContext:store:predicate:offset:limit:error:"

```
