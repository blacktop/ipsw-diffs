## ReplayKitAngel

> `/Applications/ReplayKitAngel.app/ReplayKitAngel`

```diff

-680.5.1.0.0
-  __TEXT.__text: 0x3f810
-  __TEXT.__auth_stubs: 0x1150
-  __TEXT.__objc_stubs: 0x1540
-  __TEXT.__objc_methlist: 0x181c
-  __TEXT.__const: 0x1a94
-  __TEXT.__gcc_except_tab: 0xdc
-  __TEXT.__oslogstring: 0x1755
-  __TEXT.__cstring: 0x2dee
-  __TEXT.__objc_methname: 0x41f9
+680.7.1.1.1
+  __TEXT.__text: 0x416a4
+  __TEXT.__auth_stubs: 0x1160
+  __TEXT.__objc_stubs: 0x1640
+  __TEXT.__objc_methlist: 0x187c
+  __TEXT.__const: 0x1c24
+  __TEXT.__gcc_except_tab: 0x144
+  __TEXT.__oslogstring: 0x1ca5
+  __TEXT.__cstring: 0x2f6e
+  __TEXT.__objc_methname: 0x431e
   __TEXT.__objc_classname: 0x312
   __TEXT.__objc_methtype: 0x18bb
   __TEXT.__swift5_typeref: 0x8bc

   __TEXT.__swift5_types: 0xdc
   __TEXT.__swift_as_entry: 0x18
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0xe08
+  __TEXT.__unwind_info: 0xe40
   __TEXT.__eh_frame: 0x508
-  __DATA_CONST.__auth_got: 0x8b8
+  __DATA_CONST.__auth_got: 0x8c0
   __DATA_CONST.__got: 0x3d0
   __DATA_CONST.__auth_ptr: 0x400
-  __DATA_CONST.__const: 0x1a70
-  __DATA_CONST.__cfstring: 0x300
+  __DATA_CONST.__const: 0x1b10
+  __DATA_CONST.__cfstring: 0x320
   __DATA_CONST.__objc_classlist: 0xb0
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x5d00
-  __DATA.__objc_selrefs: 0x1140
-  __DATA.__objc_ivar: 0x84
+  __DATA.__objc_const: 0x5d60
+  __DATA.__objc_selrefs: 0x1180
+  __DATA.__objc_ivar: 0x8c
   __DATA.__objc_data: 0x16c0
   __DATA.__data: 0x1230
   __DATA.__bss: 0x2098

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 08058D70-355E-3025-B79E-F5BDC6016FDB
-  Functions: 1475
-  Symbols:   560
-  CStrings:  1333
+  UUID: 65983F74-A211-3161-B517-2F3297A9B73E
+  Functions: 1495
+  Symbols:   561
+  CStrings:  1375
 
Symbols:
+ _objc_setProperty_nonatomic_copy
CStrings:
+ " [ERROR] %{public}s:%d Failed to create STActivityAttribution"
+ " [ERROR] %{public}s:%d Failed to create background activity attribution"
+ " [ERROR] %{public}s:%d Invalid identifier provided, using default"
+ " [ERROR] %{public}s:%d Nil timer string provided to updateTimerString"
+ " [ERROR] %{public}s:%d Publisher has been invalidated, cannot update timer string"
+ " [ERROR] %{public}s:%d Publisher is nil, cannot publish data"
+ " [ERROR] %{public}s:%d Publisher was invalidated during operation, cannot set handlers"
+ " [INFO] %{public}s:%d Activating background activity"
+ " [INFO] %{public}s:%d Adding background activity attribution=%@"
+ " [INFO] %{public}s:%d Background activity already active, skipping activation"
+ " [INFO] %{public}s:%d Background activity not active, skipping deactivation"
+ " [INFO] %{public}s:%d Background activity not active, storing timer string for later use"
+ " [INFO] %{public}s:%d Clearing user interaction handler"
+ " [INFO] %{public}s:%d Created new background activity attribution=%@"
+ " [INFO] %{public}s:%d Deactivating background activity"
+ " [INFO] %{public}s:%d Deallocating RPBackgroundActivity"
+ " [INFO] %{public}s:%d Initializing with identifier: %@"
+ " [INFO] %{public}s:%d No current attribution to update with timer string"
+ " [INFO] %{public}s:%d Publishing new data with active state: %d"
+ " [INFO] %{public}s:%d Removing background activity attribution=%@"
+ " [INFO] %{public}s:%d Self was deallocated during publish operation"
+ " [INFO] %{public}s:%d Self was deallocated during timer update"
+ " [INFO] %{public}s:%d Setting user interaction handler"
+ " [INFO] %{public}s:%d User interaction detected"
+ " [INFO] %{public}s:%d timer=%@"
+ "-[RPBackgroundActivity activateWithUserInteractionHandler:]_block_invoke"
+ "-[RPBackgroundActivity deactivate]_block_invoke"
+ "-[RPBackgroundActivity dealloc]"
+ "-[RPBackgroundActivity publishNewDataWithUserInteractionHandler:]_block_invoke_2"
+ "-[RPBackgroundActivity updateTimerString:]"
+ "-[RPBackgroundActivity updateTimerString:]_block_invoke"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_synchronizationQueue"
+ "T@\"NSString\",C,N,V_currentTimerString"
+ "_canShowWhileLocked"
+ "_currentTimerString"
+ "_synchronizationQueue"
+ "activityAttribution"
+ "com.apple.replaykit.backgroundactivity"
+ "currentTimerString"
+ "length"
+ "setCurrentTimerString:"
+ "setSynchronizationQueue:"
+ "synchronizationQueue"
+ "updateTimerString:"
- " [INFO] %{public}s:%d adding background activity attribution=%@"
- " [INFO] %{public}s:%d created new background activity attribution=%@"
- " [INFO] %{public}s:%d removing background activity attribution=%@"
- " [INFO] %{public}s:%d setting user interaction block"

```
