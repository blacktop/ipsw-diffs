## FeedbackLogger

> `/System/Library/PrivateFrameworks/FeedbackLogger.framework/FeedbackLogger`

```diff

-3302.18.2.0.0
-  __TEXT.__text: 0xb2c4
+3303.5.1.0.0
+  __TEXT.__text: 0xb83c
   __TEXT.__auth_stubs: 0x6d0
-  __TEXT.__objc_methlist: 0xc88
+  __TEXT.__objc_methlist: 0xd70
   __TEXT.__const: 0x78
-  __TEXT.__gcc_except_tab: 0x134
-  __TEXT.__cstring: 0x1737
-  __TEXT.__oslogstring: 0x14cf
-  __TEXT.__unwind_info: 0x330
-  __TEXT.__objc_classname: 0x111
-  __TEXT.__objc_methname: 0x25ff
-  __TEXT.__objc_methtype: 0x64a
-  __TEXT.__objc_stubs: 0x1a40
+  __TEXT.__gcc_except_tab: 0x140
+  __TEXT.__cstring: 0x1762
+  __TEXT.__oslogstring: 0x15b3
+  __TEXT.__unwind_info: 0x364
+  __TEXT.__objc_classname: 0x126
+  __TEXT.__objc_methname: 0x2956
+  __TEXT.__objc_methtype: 0x672
+  __TEXT.__objc_stubs: 0x1c00
   __DATA_CONST.__got: 0x50
-  __DATA_CONST.__const: 0x300
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__const: 0x328
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1608
-  __DATA_CONST.__objc_selrefs: 0x920
+  __DATA_CONST.__objc_const: 0x1750
+  __DATA_CONST.__objc_selrefs: 0x9c0
   __DATA_CONST.__objc_arraydata: 0x18
-  __AUTH_CONST.__objc_const: 0x90
-  __AUTH_CONST.__cfstring: 0x600
-  __AUTH_CONST.__const: 0x60
+  __AUTH_CONST.__objc_const: 0xd8
+  __AUTH_CONST.__cfstring: 0x660
+  __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__auth_got: 0x378
-  __AUTH.__objc_data: 0x50
+  __AUTH.__objc_data: 0xa0
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0xc0
-  __DATA.__objc_superrefs: 0x30
-  __DATA.__objc_ivar: 0x100
+  __DATA.__objc_classrefs: 0xe8
+  __DATA.__objc_superrefs: 0x38
+  __DATA.__objc_ivar: 0x114
   __DATA.__data: 0x120
-  __DATA.__bss: 0x10
-  __DATA_DIRTY.__const: 0x40
+  __DATA.__bss: 0x20
+  __DATA_DIRTY.__const: 0x20
   __DATA_DIRTY.__objc_const: 0x2c8
   __DATA_DIRTY.__objc_data: 0x230
   __DATA_DIRTY.__common: 0x8

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
+  - /System/Library/PrivateFrameworks/RunningBoardServices.framework/RunningBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 66DDBA59-215E-3485-BBC1-CD86DC666835
-  Functions: 292
-  Symbols:   1129
-  CStrings:  808
+  UUID: 2751323D-9541-3EF0-A457-DA1D7F60B518
+  Functions: 311
+  Symbols:   1200
+  CStrings:  850
 
Symbols:
+ +[FLLogger isManagedProcess]
+ -[FLLogger _cancelWriteTransactionTTLTimer]
+ -[FLLogger _claimWriteTransaction]
+ -[FLLogger _isHoldingWriteTransaction]
+ -[FLLogger _nextStoreCacheTimerFireDateForManagedProcess]
+ -[FLLogger _nextStoreCacheTimerFireDateForUnmanagedProcess]
+ -[FLLogger _nextStoreCacheTimerFireDate]
+ -[FLLogger _relinquishWriteTransaction]
+ -[FLLogger _scheduleWriteTransactionTTLTimer]
+ -[FLLogger _setupWriteTransactionTTLTimer]
+ -[FLLogger _writeTransactionTTLTimerDidFire]
+ -[FLLogger cancelWriteTransactionTTLTimer]
+ -[FLLogger isHoldingWriteTransaction]
+ -[FLLogger managedProcessPersistentStoreCacheTTLInSeconds]
+ -[FLLogger mostRecentWriteTransactionExpiry]
+ -[FLLogger setManagedProcessPersistentStoreCacheTTLInSeconds:]
+ -[FLLogger setMostRecentWriteTransactionExpiry:]
+ -[FLLogger setWriteTransaction:]
+ -[FLLogger setWriteTransactionTTLTimer:]
+ -[FLLogger writeTransactionTTLTimer]
+ -[FLWriteTransaction .cxx_destruct]
+ -[FLWriteTransaction dealloc]
+ -[FLWriteTransaction init]
+ -[FLWriteTransaction log]
+ -[FLWriteTransaction rbsAssertion]
+ -[FLWriteTransaction setLog:]
+ -[FLWriteTransaction setRbsAssertion:]
+ -[FLWriteTransaction setTransaction:]
+ -[FLWriteTransaction transaction]
+ GCC_except_table203
+ GCC_except_table227
+ GCC_except_table282
+ GCC_except_table57
+ GCC_except_table63
+ GCC_except_table77
+ GCC_except_table79
+ GCC_except_table95
+ _OBJC_CLASS_$_FLWriteTransaction
+ _OBJC_CLASS_$_RBSAssertion
+ _OBJC_CLASS_$_RBSDomainAttribute
+ _OBJC_CLASS_$_RBSProcessHandle
+ _OBJC_CLASS_$_RBSTarget
+ _OBJC_IVAR_$_FLLogger._isHoldingWriteTransaction
+ _OBJC_IVAR_$_FLLogger._managedProcessPersistentStoreCacheTTLInSeconds
+ _OBJC_IVAR_$_FLLogger._mostRecentWriteTransactionExpiry
+ _OBJC_IVAR_$_FLLogger._writeTransactionTTLTimer
+ _OBJC_IVAR_$_FLWriteTransaction._log
+ _OBJC_IVAR_$_FLWriteTransaction._rbsAssertion
+ _OBJC_IVAR_$_FLWriteTransaction._transaction
+ _OBJC_METACLASS_$_FLWriteTransaction
+ __OBJC_$_INSTANCE_METHODS_FLWriteTransaction
+ __OBJC_$_INSTANCE_VARIABLES_FLWriteTransaction
+ __OBJC_$_PROP_LIST_FLWriteTransaction
+ __OBJC_$_PROP_LIST_NSObject.747
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.748
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.749
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.750
+ __OBJC_CLASS_RO_$_FLWriteTransaction
+ __OBJC_METACLASS_RO_$_FLWriteTransaction
+ ___26-[FLLogger closeAllStores]_block_invoke
+ ___28+[FLLogger isManagedProcess]_block_invoke
+ ___42-[FLLogger _setupWriteTransactionTTLTimer]_block_invoke
+ ___Block_byref_object_copy_.385
+ ___Block_byref_object_dispose_.386
+ ___block_descriptor_48_e8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_literal_global.29
+ ___block_literal_global.403
+ ___block_literal_global.575
+ ___block_literal_global.756
+ __unnamed_array_storage.112
+ _dispatch_queue_create
+ _isManagedProcess._isManagedProcess
+ _isManagedProcess.onceToken
+ _objc_msgSend$_cancelWriteTransactionTTLTimer
+ _objc_msgSend$_claimWriteTransaction
+ _objc_msgSend$_isHoldingWriteTransaction
+ _objc_msgSend$_nextStoreCacheTimerFireDate
+ _objc_msgSend$_nextStoreCacheTimerFireDateForManagedProcess
+ _objc_msgSend$_nextStoreCacheTimerFireDateForUnmanagedProcess
+ _objc_msgSend$_relinquishWriteTransaction
+ _objc_msgSend$_scheduleWriteTransactionTTLTimer
+ _objc_msgSend$_setupWriteTransactionTTLTimer
+ _objc_msgSend$_writeTransactionTTLTimerDidFire
+ _objc_msgSend$acquireWithError:
+ _objc_msgSend$attributeWithDomain:name:
+ _objc_msgSend$cancelWriteTransactionTTLTimer
+ _objc_msgSend$currentProcess
+ _objc_msgSend$initWithExplanation:target:attributes:
+ _objc_msgSend$invalidate
+ _objc_msgSend$isManaged
+ _objc_msgSend$isManagedProcess
+ _objc_msgSend$managedProcessPersistentStoreCacheTTLInSeconds
+ _objc_msgSend$mostRecentWriteTransactionExpiry
+ _objc_msgSend$setWriteTransactionTTLTimer:
+ _objc_msgSend$writeTransactionTTLTimer
+ _objc_opt_class
- -[FLLogger _cancelTransactionTTLTimer]
- -[FLLogger _nextTimerFireDate]
- -[FLLogger _scheduleTransactionTTLTimer]
- -[FLLogger _setupTransactionTTLTimer]
- -[FLLogger _transactionTTLTimerDidFire]
- -[FLLogger cancelTransactionTTLTimer]
- -[FLLogger persistentStoreCacheTTL]
- -[FLLogger setPersistentStoreCacheTTL:]
- -[FLLogger setTransactionTTLTimer:]
- -[FLLogger transactionTTLTimer]
- GCC_except_table193
- GCC_except_table217
- GCC_except_table272
- GCC_except_table49
- GCC_except_table55
- GCC_except_table73
- GCC_except_table75
- GCC_except_table89
- _OBJC_IVAR_$_FLLogger._persistentStoreCacheTTL
- _OBJC_IVAR_$_FLLogger._transactionTTLTimer
- __OBJC_$_PROP_LIST_NSObject.707
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject.708
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject.709
- __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject.710
- ___19-[FLLogger dealloc]_block_invoke
- ___27-[FLLogger _closeAllStores]_block_invoke
- ___37-[FLLogger _setupTransactionTTLTimer]_block_invoke
- ___Block_byref_object_copy_.380
- ___Block_byref_object_dispose_.381
- ___block_literal_global.28
- ___block_literal_global.398
- ___block_literal_global.572
- ___block_literal_global.716
- __unnamed_array_storage.106
- _dispatch_queue_create_with_target$V2
- _dispatch_workloop_copy_current
- _objc_msgSend$_cancelTransactionTTLTimer
- _objc_msgSend$_nextTimerFireDate
- _objc_msgSend$_scheduleTransactionTTLTimer
- _objc_msgSend$_setupTransactionTTLTimer
- _objc_msgSend$_transactionTTLTimerDidFire
- _objc_msgSend$cancelTransactionTTLTimer
- _objc_msgSend$setTransactionTTLTimer:
- _objc_msgSend$transactionTTLTimer
CStrings:
+ "\x03"
+ "\x14\x13\x12"
+ "@\"FLWriteTransaction\""
+ "@\"RBSAssertion\""
+ "B"
+ "Error acquiring write assertion: %@."
+ "FLWriteTransaction"
+ "FinishTaskUninterruptable"
+ "Scheduling store cache TTL timer for %f seconds from now."
+ "Scheduling the write transaction TTL timer for %lu seconds from now."
+ "Store cache TTL timer fired."
+ "T@\"FLWriteTransaction\",&,N,V_writeTransaction"
+ "T@\"NSDate\",&,N,V_mostRecentWriteTransactionExpiry"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_writeTransactionTTLTimer"
+ "T@\"NSObject<OS_os_transaction>\",&,N,V_transaction"
+ "T@\"RBSAssertion\",&,N,V_rbsAssertion"
+ "TB,R,N,V_isHoldingWriteTransaction"
+ "TQ,N,V_managedProcessPersistentStoreCacheTTLInSeconds"
+ "Write transaction TTL timer fired."
+ "_cancelWriteTransactionTTLTimer"
+ "_claimWriteTransaction"
+ "_isHoldingWriteTransaction"
+ "_managedProcessPersistentStoreCacheTTLInSeconds"
+ "_mostRecentWriteTransactionExpiry"
+ "_nextStoreCacheTimerFireDate"
+ "_nextStoreCacheTimerFireDateForManagedProcess"
+ "_nextStoreCacheTimerFireDateForUnmanagedProcess"
+ "_rbsAssertion"
+ "_relinquishWriteTransaction"
+ "_scheduleWriteTransactionTTLTimer"
+ "_setupWriteTransactionTTLTimer"
+ "_transaction"
+ "_writeTransactionTTLTimer"
+ "_writeTransactionTTLTimerDidFire"
+ "acquireWithError:"
+ "attributeWithDomain:name:"
+ "cancelWriteTransactionTTLTimer"
+ "com.apple.common"
+ "currentProcess"
+ "initWithExplanation:target:attributes:"
+ "invalidate"
+ "isHoldingWriteTransaction"
+ "isManaged"
+ "isManagedProcess"
+ "managedProcessPersistentStoreCacheTTLInSeconds"
+ "mostRecentWriteTransactionExpiry"
+ "rbsAssertion"
+ "setManagedProcessPersistentStoreCacheTTLInSeconds:"
+ "setMostRecentWriteTransactionExpiry:"
+ "setRbsAssertion:"
+ "setTransaction:"
+ "setWriteTransaction:"
+ "setWriteTransactionTTLTimer:"
+ "transaction"
+ "writeTransactionTTLTimer"
- "\x15\x12\x11"
- "T@\"NSObject<OS_dispatch_source>\",&,N,V_transactionTTLTimer"
- "T@\"NSObject<OS_os_transaction>\",R,N,V_writeTransaction"
- "TQ,N,V_persistentStoreCacheTTL"
- "_cancelTransactionTTLTimer"
- "_nextTimerFireDate"
- "_persistentStoreCacheTTL"
- "_scheduleTransactionTTLTimer"
- "_setupTransactionTTLTimer"
- "_transactionTTLTimer"
- "_transactionTTLTimerDidFire"
- "cancelTransactionTTLTimer"
- "persistentStoreCacheTTL"
- "setPersistentStoreCacheTTL:"
- "setTransactionTTLTimer:"
- "transactionTTLTimer"

```
