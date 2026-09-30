## libcoreroutine.dylib

> `/usr/lib/libcoreroutine.dylib`

```diff

-1062.0.1.0.0
-  __TEXT.__text: 0x5ec8ec
+1062.0.1.0.1
+  __TEXT.__text: 0x5ecba0
   __TEXT.__auth_stubs: 0x2190
-  __TEXT.__objc_methlist: 0x31030
+  __TEXT.__objc_methlist: 0x31038
   __TEXT.__const: 0x4640
   __TEXT.__dlopen_cstrs: 0x1d2
   __TEXT.__swift5_typeref: 0x1d3
-  __TEXT.__oslogstring: 0x7630c
-  __TEXT.__cstring: 0x4538e
+  __TEXT.__oslogstring: 0x762d1
+  __TEXT.__cstring: 0x45365
   __TEXT.__swift5_capture: 0x9c
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x1c

   __TEXT.__unwind_info: 0xdc50
   __TEXT.__eh_frame: 0x390
   __TEXT.__objc_classname: 0x58ca
-  __TEXT.__objc_methname: 0x915ca
-  __TEXT.__objc_methtype: 0xcf9f
-  __TEXT.__objc_stubs: 0x55a80
+  __TEXT.__objc_methname: 0x915e9
+  __TEXT.__objc_methtype: 0xcfa5
+  __TEXT.__objc_stubs: 0x55aa0
   __DATA_CONST.__got: 0x30f0
   __DATA_CONST.__const: 0xf4f8
   __DATA_CONST.__objc_classlist: 0x1548
   __DATA_CONST.__objc_catlist: 0x3a8
   __DATA_CONST.__objc_protolist: 0x358
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19420
+  __DATA_CONST.__objc_selrefs: 0x19428
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x1198
   __DATA_CONST.__objc_arraydata: 0x2a00
   __AUTH_CONST.__auth_got: 0x10d8
   __AUTH_CONST.__const: 0x3260
-  __AUTH_CONST.__cfstring: 0x28800
+  __AUTH_CONST.__cfstring: 0x287e0
   __AUTH_CONST.__objc_const: 0x50a60
   __AUTH_CONST.__objc_intobj: 0x4608
   __AUTH_CONST.__objc_arrayobj: 0xe70

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A1CFFE5C-96C1-3E66-82E1-265D106754F2
-  Functions: 20179
-  Symbols:   65151
-  CStrings:  40140
+  UUID: 96E2609E-4D2C-34E8-A095-854E0424A5F0
+  Functions: 20180
+  Symbols:   65154
+  CStrings:  40139
 
Symbols:
+ -[RTPersistenceMirroringManager _changeCountForManagedObjectContext:currentExporterToken:error:]
+ -[RTPersistenceMirroringManager _countChangesInTransactionsFromContext:store:predicate:error:]
+ -[RTPersistenceMirroringManager _fetchHistoryTransactionBatchFromContext:store:predicate:offset:limit:error:]
+ _objc_msgSend$_changeCountForManagedObjectContext:currentExporterToken:error:
+ _objc_msgSend$_countChangesInTransactionsFromContext:store:predicate:error:
+ _objc_msgSend$_fetchHistoryTransactionBatchFromContext:store:predicate:offset:limit:error:
- -[RTPersistenceMirroringManager _changeCountForManagedObjectContext:currentExporterToken:excludeImport:error:]
- -[RTPersistenceMirroringManager _createHistoryChangeRequestWithManagedObjectContext:currentExporterToken:excludeImport:store:]
- _objc_msgSend$_changeCountForManagedObjectContext:currentExporterToken:excludeImport:error:
- _objc_msgSend$_createHistoryChangeRequestWithManagedObjectContext:currentExporterToken:excludeImport:store:
CStrings:
+ "%@, change count exceeded limit (%d), terminating count early"
+ "%@, change count, %lu"
+ "%@, failed to extract batch transactions, error, %@"
+ "%@, failed to get cloud store"
+ "03:13:29"
+ "@64@0:8@16@24@32Q40Q48^@56"
+ "Aug 28 2025"
+ "_changeCountForManagedObjectContext:currentExporterToken:error:"
+ "_countChangesInTransactionsFromContext:store:predicate:error:"
+ "_fetchHistoryTransactionBatchFromContext:store:predicate:offset:limit:error:"
- "%@, failed to create transactionrequest"
- "%@, failed to extract transactions, error, %@"
- "%@, invalid inputs, managedObjectContext, %@, store, %@"
- "%@, transactionRequest, %@, transactionRequest.fetchRequest, %@, change count, %lu"
- "02:51:52"
- "Aug  5 2025"
- "Q44@0:8@16@24B32^@36"
- "Total change count from all authors, %lu"
- "_changeCountForManagedObjectContext:currentExporterToken:excludeImport:error:"
- "_createHistoryChangeRequestWithManagedObjectContext:currentExporterToken:excludeImport:store:"

```
