## HealthDaemonFoundation

> `/System/Library/PrivateFrameworks/HealthDaemonFoundation.framework/HealthDaemonFoundation`

```diff

-6200.3.4.0.0
-  __TEXT.__text: 0x4ddb4
+6200.3.8.0.0
+  __TEXT.__text: 0x4dde0
   __TEXT.__auth_stubs: 0x1770
   __TEXT.__objc_methlist: 0x339c
   __TEXT.__const: 0xf12

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 2DB1DFCC-7F3E-3CAC-A53C-E7705AE92ADB
+  UUID: 6AE7918A-81E1-324B-A004-8E630283BD13
   Functions: 2089
   Symbols:   5839
   CStrings:  2937
Symbols:
+ ___63-[HDXPCPeriodicActivity _performCurrentActivityWithCompletion:]_block_invoke.313
+ ___64-[HDSQLiteDatabase performTransactionWithType:error:usingBlock:]_block_invoke.382
+ ___block_literal_global.309
+ ___block_literal_global.315
+ ___block_literal_global.399
+ ___block_literal_global.443
+ ___block_literal_global.527
+ ___block_literal_global.660
+ ___block_literal_global.663
+ ___hd_xpc_dispatch_event_block_invoke.328
- ___63-[HDXPCPeriodicActivity _performCurrentActivityWithCompletion:]_block_invoke.304
- ___64-[HDSQLiteDatabase performTransactionWithType:error:usingBlock:]_block_invoke.373
- ___block_literal_global.300
- ___block_literal_global.306
- ___block_literal_global.390
- ___block_literal_global.434
- ___block_literal_global.518
- ___block_literal_global.651
- ___block_literal_global.654
- ___hd_xpc_dispatch_event_block_invoke.319
Functions:
~ -[HDContentProtectionManager _handleKeyBagLockStatusNotification] : 140 -> 136
~ -[HDContentProtectionManager _keyBagLockState] : 64 -> 60
~ -[HDPriorityQueue _lock_heapifyUp] : 116 -> 112
~ -[HDPriorityQueue _lock_heapifyDown] : 172 -> 168
~ -[HDSQLiteEntity getValuesForProperties:database:error:handler:] : 1720 -> 1724
~ __ZNSt3__16vectorIPKcNS_9allocatorIS2_EEE11__vallocateB8ne200100Em : 60 -> 64
~ -[HDSQLiteQuery enumerateProperties:error:enumerationHandler:] : 1172 -> 1164
~ __ZNKSt3__120__shared_ptr_pointerIPNS_13__empty_stateIcEENS_10shared_ptrIS2_E27__shared_ptr_default_deleteIS2_S2_EENS_9allocatorIS2_EEE13__get_deleterERKSt9type_info : 60 -> 64
~ __ZNSt3__16vectorINS_9sub_matchIPKcEENS_9allocatorIS4_EEE11__vallocateB8ne200100Em : 76 -> 80
~ __ZNSt3__16vectorINS_7__stateIcEENS_9allocatorIS2_EEE24__emplace_back_slow_pathIJS2_EEEPS2_DpOT_ : 376 -> 380
~ __ZNSt3__16vectorINS_4pairImPKcEENS_9allocatorIS4_EEE11__vallocateB8ne200100Em : 60 -> 64
~ __ZNSt3__16vectorINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEENS4_IS6_EEE24__emplace_back_slow_pathIJRKS6_EEEPS6_DpOT_ : 320 -> 316
~ __ZNSt3__15dequeINS_7__stateIcEENS_9allocatorIS2_EEE19__add_back_capacityEv : 468 -> 472
~ __ZNSt3__114__split_bufferIPNS_7__stateIcEENS_9allocatorIS3_EEE13emplace_frontIJS3_EEEvDpOT_ : 268 -> 272
~ -[HDDatabaseConnectionPool _semaphoreForCheckOutOptions:] : 88 -> 76
~ -[HDDatabaseConnectionPool _addDatabaseWrapperToCheckoutMap:] : 108 -> 116
~ -[HDSQLiteStatementCache _setCachedStatement:forKey:] : 104 -> 116
~ -[_HDSQLiteStatementCacheStorage clearStatements] : 68 -> 76
~ -[HDXPCPeriodicActivity _lock_errorCount] : 112 -> 108
~ -[HDXPCPeriodicActivity _lock_incrementErrorCount] : 140 -> 152
~ -[HDAsynchronousTaskTree _lock_insertPendingSubtasks] : 112 -> 120
~ -[HDAsynchronousTaskTree _lock_reportResult:] : 220 -> 216
~ -[HDPriorityQueue _lock_swapIndicies:with:] : 160 -> 176
~ -[HDDatabaseAssertionManager _startTimer] : 348 -> 344

```
