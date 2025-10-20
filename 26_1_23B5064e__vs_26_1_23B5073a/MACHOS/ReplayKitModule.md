## ReplayKitModule

> `/System/Library/ControlCenter/Bundles/ReplayKitModule.bundle/ReplayKitModule`

```diff

-680.5.1.0.0
-  __TEXT.__text: 0x8f24
-  __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_stubs: 0x18c0
-  __TEXT.__objc_methlist: 0xb00
-  __TEXT.__const: 0xb0
-  __TEXT.__objc_methname: 0x275d
-  __TEXT.__oslogstring: 0x6b8
-  __TEXT.__cstring: 0x16a7
+680.7.1.1.1
+  __TEXT.__text: 0x9fdc
+  __TEXT.__auth_stubs: 0x520
+  __TEXT.__objc_stubs: 0x1980
+  __TEXT.__objc_methlist: 0xb48
+  __TEXT.__const: 0xb8
+  __TEXT.__objc_methname: 0x283d
+  __TEXT.__oslogstring: 0xc0f
+  __TEXT.__cstring: 0x1868
   __TEXT.__objc_classname: 0x14d
   __TEXT.__objc_methtype: 0x75b
-  __TEXT.__gcc_except_tab: 0x154
-  __TEXT.__unwind_info: 0x288
-  __DATA_CONST.__auth_got: 0x278
+  __TEXT.__gcc_except_tab: 0x1bc
+  __TEXT.__unwind_info: 0x2c8
+  __DATA_CONST.__auth_got: 0x2a0
   __DATA_CONST.__got: 0x138
-  __DATA_CONST.__const: 0x378
-  __DATA_CONST.__cfstring: 0x560
+  __DATA_CONST.__const: 0x418
+  __DATA_CONST.__cfstring: 0x580
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA.__objc_const: 0x1990
-  __DATA.__objc_selrefs: 0xa40
-  __DATA.__objc_ivar: 0xb8
+  __DATA.__objc_const: 0x19f0
+  __DATA.__objc_selrefs: 0xa60
+  __DATA.__objc_ivar: 0xc0
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x240
   __DATA.__bss: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 614ADE86-A8F7-3F0C-A46B-DE54CAAE84DC
-  Functions: 169
-  Symbols:   139
-  CStrings:  699
+  UUID: 682311BB-04DA-3F8D-8964-5AC6CD8EF468
+  Functions: 190
+  Symbols:   144
+  CStrings:  737
 
Symbols:
+ __Block_object_dispose
+ __os_log_error_impl
+ _dispatch_queue_create
+ _dispatch_sync
+ _objc_retain_x23
+ _objc_setProperty_nonatomic_copy
- _objc_retain_x22
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
+ "_currentTimerString"
+ "_synchronizationQueue"
+ "activityAttribution"
+ "com.apple.replaykit.backgroundactivity"
+ "com.apple.systemstatus.background-activity.replaykit.callrecording.recording"
+ "length"
+ "setSynchronizationQueue:"
+ "synchronizationQueue"
+ "updateTimerString:"
- " [INFO] %{public}s:%d adding background activity attribution=%@"
- " [INFO] %{public}s:%d created new background activity attribution=%@"
- " [INFO] %{public}s:%d removing background activity attribution=%@"
- " [INFO] %{public}s:%d setting user interaction block"
- "center"

```
