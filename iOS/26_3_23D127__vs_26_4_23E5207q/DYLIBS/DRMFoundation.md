## DRMFoundation

> `/System/Library/PrivateFrameworks/DRMFoundation.framework/DRMFoundation`

```diff

-234.80.6.0.0
-  __TEXT.__text: 0x2b38
-  __TEXT.__auth_stubs: 0x3e0
+234.100.11.0.0
+  __TEXT.__text: 0x2e2c
+  __TEXT.__auth_stubs: 0x3c0
   __TEXT.__objc_methlist: 0x3d4
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x140
   __TEXT.__cstring: 0x1a6
-  __TEXT.__unwind_info: 0x1a8
+  __TEXT.__unwind_info: 0x1c8
   __TEXT.__objc_classname: 0x7a
   __TEXT.__objc_methname: 0xa6e
   __TEXT.__objc_methtype: 0x148

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x2f0
   __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x200
+  __AUTH_CONST.__auth_got: 0x1f0
   __AUTH_CONST.__const: 0x60
   __AUTH_CONST.__cfstring: 0xa0
   __AUTH_CONST.__objc_const: 0x750

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D8C7CB2A-9D2C-3C61-8D0C-0528296B19C8
+  UUID: 0017B2B7-E10B-390E-9F74-CC12AB9BF373
   Functions: 96
-  Symbols:   429
+  Symbols:   427
   CStrings:  188
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x23
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x5
- _objc_retain_x8
Functions:
~ -[_OSDataProtectionManager handleKeyBagLockNotification] : 884 -> 892
~ ___56-[_OSDataProtectionManager handleKeyBagLockNotification]_block_invoke : 296 -> 316
~ +[_OSDataProtectionStateMonitor dataProtectionClassA] : 16 -> 64
~ +[_OSDataProtectionStateMonitor dataProtectionClassC] : 16 -> 64
~ ___56-[_OSDataProtectionManager handleKeyBagLockNotification]_block_invoke_2 : 388 -> 400
~ -[_OSPriorityQueue init] : 104 -> 108
~ -[_OSPriorityQueue addObject:withPriority:] : 336 -> 340
~ -[_OSPriorityQueue popFirst] : 552 -> 572
~ ___28-[_OSPriorityQueue popFirst]_block_invoke : 204 -> 212
~ -[_OSPriorityQueue popLast] : 544 -> 560
~ ___27-[_OSPriorityQueue popLast]_block_invoke : 204 -> 212
~ -[_OSPriorityQueue removeObject:atPriority:] : 224 -> 232
~ ___30-[_OSPriorityQueue allObjects]_block_invoke : 240 -> 244
~ -[_OSPriorityQueue description] : 216 -> 228
~ -[_OSPriorityQueue setObjects:] : 12 -> 64
~ -[_OSPriorityQueue setLowestPriority:] : 12 -> 64
~ -[_OSPriorityQueue setHighestPriority:] : 12 -> 64
~ +[_OSDataProtectionManager sharedInstance] : 160 -> 176
~ -[_OSDataProtectionManager init] : 736 -> 776
~ ___47-[_OSDataProtectionManager isDataAvailableFor:]_block_invoke : 116 -> 120
~ -[_OSDataProtectionManager deregisterStateChangeHandler:] : 152 -> 160
~ +[_OSDataProtectionStateMonitor dataProtectionClassD] : 16 -> 64
~ -[_OSDataProtectionStateMonitor init] : 128 -> 132
~ -[_OSDataProtectionStateMonitor setChangeHandler:] : 148 -> 144
~ ___34-[NSString(_OSDeduping) _os_dedup]_block_invoke : 60 -> 64
~ ___34-[NSString(_OSDeduping) _os_dedup]_block_invoke_2 : 104 -> 108
~ ___34-[NSNumber(_DKDeduping) _os_dedup]_block_invoke : 60 -> 64
~ ___34-[NSNumber(_DKDeduping) _os_dedup]_block_invoke_2 : 104 -> 108
~ -[NSDate(_DKDeduping) _os_dedup] : 404 -> 412
~ ___32-[NSDate(_DKDeduping) _os_dedup]_block_invoke : 60 -> 64
~ ___32-[NSDate(_DKDeduping) _os_dedup]_block_invoke_2 : 104 -> 108
~ -[_OSBatchingQueue initWithName:maxBatchingDelay:maxQueueDepth:queue:workItemsHandler:] : 648 -> 664
~ +[_OSBatchingQueue queueWithName:maxBatchingDelay:maxQueueDepth:queue:workItemsHandler:] : 168 -> 160
~ -[_OSBatchingQueue unprotectedExecuteWorkItems] : 236 -> 240
~ ___47-[_OSBatchingQueue unprotectedExecuteWorkItems]_block_invoke : 92 -> 96
~ -[_OSBatchingQueue addWorkItem:] : 152 -> 160
~ -[_OSBatchingQueue setSyncQueue:] : 12 -> 64
~ -[_OSBatchingQueue setExecutionQueue:] : 12 -> 64
~ -[_OSBatchingQueue setWorkItems:] : 12 -> 64
~ -[_OSBatchingQueue setTimer:] : 12 -> 64

```
