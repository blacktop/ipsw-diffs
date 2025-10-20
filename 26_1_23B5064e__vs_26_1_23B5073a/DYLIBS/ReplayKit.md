## ReplayKit

> `/System/Library/Frameworks/ReplayKit.framework/ReplayKit`

```diff

-680.5.1.0.0
-  __TEXT.__text: 0x2f4b4
+680.7.1.1.1
+  __TEXT.__text: 0x30670
   __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x2b68
+  __TEXT.__objc_methlist: 0x2bb8
   __TEXT.__const: 0x100
-  __TEXT.__gcc_except_tab: 0x108
-  __TEXT.__oslogstring: 0x483b
-  __TEXT.__cstring: 0x5960
-  __TEXT.__unwind_info: 0x988
-  __TEXT.__objc_classname: 0x6d9
-  __TEXT.__objc_methname: 0x7cc6
+  __TEXT.__gcc_except_tab: 0x170
+  __TEXT.__oslogstring: 0x4d92
+  __TEXT.__cstring: 0x5b21
+  __TEXT.__unwind_info: 0x9d0
+  __TEXT.__objc_classname: 0x6db
+  __TEXT.__objc_methname: 0x7d92
   __TEXT.__objc_methtype: 0x1adb
-  __TEXT.__objc_stubs: 0x54e0
+  __TEXT.__objc_stubs: 0x5580
   __DATA_CONST.__got: 0x480
-  __DATA_CONST.__const: 0x9b0
+  __DATA_CONST.__const: 0xa50
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0xf0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ce8
+  __DATA_CONST.__objc_selrefs: 0x1d08
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0xa8
   __AUTH_CONST.__auth_got: 0x570
   __AUTH_CONST.__const: 0x9f8
-  __AUTH_CONST.__cfstring: 0x1780
-  __AUTH_CONST.__objc_const: 0x5c90
+  __AUTH_CONST.__cfstring: 0x17a0
+  __AUTH_CONST.__objc_const: 0x5cf0
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0xa50
-  __DATA.__objc_ivar: 0x28c
+  __DATA.__objc_ivar: 0x294
   __DATA.__data: 0xb48
   __DATA.__bss: 0x118
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4A66AB80-5E81-360F-AC83-00AE0FECB8D2
-  Functions: 1131
-  Symbols:   4125
-  CStrings:  2528
+  UUID: 6ED51E8F-AD5C-3CDA-99BF-F26CF84CB612
+  Functions: 1151
+  Symbols:   4178
+  CStrings:  2565
 
Symbols:
+ -[RPBackgroundActivity currentTimerString]
+ -[RPBackgroundActivity dealloc]
+ -[RPBackgroundActivity initWithBackgroundActivityIdentifier:].cold.1
+ -[RPBackgroundActivity init]
+ -[RPBackgroundActivity publishNewDataWithUserInteractionHandler:].cold.1
+ -[RPBackgroundActivity publishNewDataWithUserInteractionHandler:].cold.2
+ -[RPBackgroundActivity publishNewDataWithUserInteractionHandler:].cold.3
+ -[RPBackgroundActivity setCurrentTimerString:]
+ -[RPBackgroundActivity setSynchronizationQueue:]
+ -[RPBackgroundActivity synchronizationQueue]
+ -[RPBackgroundActivity updateTimerString:]
+ -[RPBackgroundActivity updateTimerString:].cold.1
+ -[RPBackgroundActivity updateTimerString:].cold.2
+ GCC_except_table10
+ GCC_except_table5
+ _OBJC_IVAR_$_RPBackgroundActivity._currentTimerString
+ _OBJC_IVAR_$_RPBackgroundActivity._synchronizationQueue
+ ___34-[RPBackgroundActivity deactivate]_block_invoke
+ ___42-[RPBackgroundActivity updateTimerString:]_block_invoke
+ ___42-[RPBackgroundActivity updateTimerString:]_block_invoke.5
+ ___59-[RPBackgroundActivity activateWithUserInteractionHandler:]_block_invoke
+ ___65-[RPBackgroundActivity publishNewDataWithUserInteractionHandler:]_block_invoke.10
+ ___65-[RPBackgroundActivity publishNewDataWithUserInteractionHandler:]_block_invoke.10.cold.1
+ ___65-[RPBackgroundActivity publishNewDataWithUserInteractionHandler:]_block_invoke.11
+ ___65-[RPBackgroundActivity publishNewDataWithUserInteractionHandler:]_block_invoke.12
+ ___65-[RPBackgroundActivity publishNewDataWithUserInteractionHandler:]_block_invoke.9
+ ___block_descriptor_40_e8_32w_e118_v24?0"STMutableBackgroundActivitiesStatusDomainData"8"STMutableBackgroundActivitiesStatusDomainDataChangeContext"16lw32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0ls32l8r40l8
+ ___block_descriptor_56_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ _objc_msgSend$activityAttribution
+ _objc_msgSend$backgroundActivityIdentifier
+ _objc_msgSend$currentAttribution
+ _objc_msgSend$publisher
+ _objc_msgSend$setCurrentTimerString:
- GCC_except_table3
- ___65-[RPBackgroundActivity publishNewDataWithUserInteractionHandler:]_block_invoke.3
- ___65-[RPBackgroundActivity publishNewDataWithUserInteractionHandler:]_block_invoke.4
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
+ "_synchronizationQueue"
+ "activityAttribution"
+ "com.apple.replaykit.backgroundactivity"
+ "com.apple.systemstatus.background-activity.replaykit.callrecording.recording"
+ "setSynchronizationQueue:"
+ "synchronizationQueue"
+ "updateTimerString:"
- " [INFO] %{public}s:%d adding background activity attribution=%@"
- " [INFO] %{public}s:%d created new background activity attribution=%@"
- " [INFO] %{public}s:%d removing background activity attribution=%@"
- " [INFO] %{public}s:%d setting user interaction block"

```
