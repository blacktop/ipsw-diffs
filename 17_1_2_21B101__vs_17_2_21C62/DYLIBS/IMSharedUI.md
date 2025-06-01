## IMSharedUI

> `/System/Library/PrivateFrameworks/IMSharedUI.framework/IMSharedUI`

```diff

-1261.200.71.2.16
-  __TEXT.__text: 0xf5c8
-  __TEXT.__auth_stubs: 0x630
-  __TEXT.__objc_methlist: 0x19ec
+1262.300.81.2.13
+  __TEXT.__text: 0x10994
+  __TEXT.__auth_stubs: 0x700
+  __TEXT.__objc_methlist: 0x1bec
   __TEXT.__const: 0x1b0
-  __TEXT.__gcc_except_tab: 0x1a0
-  __TEXT.__cstring: 0xa43
+  __TEXT.__gcc_except_tab: 0x1c8
+  __TEXT.__cstring: 0xb97
   __TEXT.__oslogstring: 0x645
-  __TEXT.__unwind_info: 0x5e4
-  __TEXT.__objc_classname: 0x3f5
-  __TEXT.__objc_methname: 0x4cc8
-  __TEXT.__objc_methtype: 0xaa8
-  __TEXT.__objc_stubs: 0x3c20
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x378
-  __DATA_CONST.__objc_classlist: 0xc0
+  __TEXT.__unwind_info: 0x674
+  __TEXT.__objc_classname: 0x41d
+  __TEXT.__objc_methname: 0x513e
+  __TEXT.__objc_methtype: 0xb75
+  __TEXT.__objc_stubs: 0x3f60
+  __DATA_CONST.__got: 0x1a0
+  __DATA_CONST.__const: 0x438
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2c50
-  __DATA_CONST.__objc_selrefs: 0x1428
+  __DATA_CONST.__objc_const: 0x2eb8
+  __DATA_CONST.__objc_selrefs: 0x1550
   __DATA_CONST.__objc_arraydata: 0xa8
-  __AUTH_CONST.__objc_const: 0x9f8
-  __AUTH_CONST.__cfstring: 0xa00
+  __AUTH_CONST.__objc_const: 0xad0
+  __AUTH_CONST.__cfstring: 0xa80
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0xc0
-  __AUTH_CONST.__const: 0x260
-  __AUTH_CONST.__auth_got: 0x328
-  __AUTH.__objc_data: 0x730
-  __DATA.__objc_classrefs: 0x1d8
-  __DATA.__objc_superrefs: 0x90
-  __DATA.__objc_ivar: 0x1fc
+  __AUTH_CONST.__const: 0x280
+  __AUTH_CONST.__auth_got: 0x390
+  __AUTH.__objc_data: 0x7d0
+  __DATA.__objc_classrefs: 0x1f0
+  __DATA.__objc_superrefs: 0xa0
+  __DATA.__objc_ivar: 0x228
   __DATA.__data: 0x3c8
   __DATA.__bss: 0x120
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/PrivateFrameworks/ResponseKit.framework/ResponseKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 5E6554AC-4F28-3847-9E53-C98152AE8D23
-  Functions: 600
-  Symbols:   282
-  CStrings:  1342
+  UUID: B2D97287-7D70-3BAB-9ED1-F4FF0F2117F6
+  Functions: 655
+  Symbols:   305
+  CStrings:  1421
 
Symbols:
+ _CFBinaryHeapAddValue
+ _CFBinaryHeapCreate
+ _CFBinaryHeapGetMinimum
+ _CFBinaryHeapRemoveAllValues
+ _CFBinaryHeapRemoveMinimumValue
+ _NSInternalInconsistencyException
+ _NSInvalidArgumentException
+ _OBJC_CLASS_$_IMDispatchQueue
+ _OBJC_CLASS_$_NSException
+ _OBJC_CLASS_$__IMDispatchQueueBlock
+ _OBJC_METACLASS_$_IMDispatchQueue
+ _OBJC_METACLASS_$__IMDispatchQueueBlock
+ __IMDispatchQueueBlockCompare
+ __dispatch_queue_attr_concurrent
+ _bzero
+ _dispatch_get_global_queue
+ _dispatch_resume
+ _dispatch_set_target_queue
+ _dispatch_suspend
+ _dispatch_sync
+ _kCFTypeDictionaryValueCallBacks
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x3
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "$"
+ "@\"NSMutableDictionary\""
+ "@\"NSObject<OS_dispatch_queue>\""
+ "@48@0:8@?16@24q32Q40"
+ "IMDispatchQueue"
+ "T@\"NSMutableDictionary\",&,N,V_dispatchQueueBlocks"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_dispatchQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_lockQueue"
+ "T@\"NSString\",C,N,V_key"
+ "TB,N,GisCancelled,V_cancelled"
+ "TB,N,GisSuspended,V_suspended"
+ "TQ,N,SsetFIFO:,V_fifo"
+ "T^{__CFBinaryHeap=},&,N,V_heap"
+ "Tq,N,V_priority"
+ "Tried to add block for key %@ to IMDispatchQueue with priority NSNotFound, which is reserved."
+ "Tried to add block for key %@ to a cancelled IMDispatchQueue."
+ "Tried to add block for key %@ which IMDispatchQueue already contains."
+ "[_IMDispatchQueueBlock block:%@ key:%@ priority:%ld fifo:%ld %@]"
+ "^{__CFBinaryHeap=}"
+ "^{__CFBinaryHeap=}16@0:8"
+ "_IMDispatchQueueBlock"
+ "_cancelled"
+ "_dispatchQueue"
+ "_dispatchQueueBlocks"
+ "_fifo"
+ "_heap"
+ "_initWithDispatchAttr:dispatchPriority:"
+ "_key"
+ "_lockQueue"
+ "_priority"
+ "_suspended"
+ "addBlock:"
+ "addBlock:withQueuePriority:"
+ "addBlock:withQueuePriority:forKey:"
+ "allKeys"
+ "allKeysOfOutstandingBlocks"
+ "cancel"
+ "cancelled"
+ "compare:"
+ "concurrentQueueWithDispatchPriority:"
+ "containsOutstandingBlockForKey:"
+ "dispatchQueue"
+ "dispatchQueueBlocks"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "fifo"
+ "heap"
+ "initWithBlock:key:priority:fifo:"
+ "isCancelled"
+ "isSuspended"
+ "key"
+ "lockQueue"
+ "priority"
+ "q24@0:8@16"
+ "queuePriorityOfOutstandingBlockForKey:"
+ "raise:format:"
+ "removeAllOutstandingBlocks"
+ "removeObjectForKey:"
+ "removeOutstandingBlockForKey:"
+ "serialQueueWithDispatchPriority:"
+ "setCancelled:"
+ "setDispatchQueue:"
+ "setDispatchQueueBlocks:"
+ "setFIFO:"
+ "setHeap:"
+ "setKey:"
+ "setLockQueue:"
+ "setPriority:"
+ "setQueuePriority:ofOutstandingBlockForKey:"
+ "setSuspended:"
+ "suspended"
+ "v24@0:8^{__CFBinaryHeap=}16"
+ "v32@0:8@?16q24"
+ "v32@0:8q16@24"
+ "v32@?0@\"NSString\"8@\"_IMDispatchQueueBlock\"16^B24"
+ "v40@0:8@?16q24@32"

```
