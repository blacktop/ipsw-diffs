## RPControlCenterModuleHQLR

> `/System/Library/ControlCenter/Bundles/RPControlCenterModuleHQLR.bundle/RPControlCenterModuleHQLR`

```diff

-680.5.1.0.0
-  __TEXT.__text: 0x1da20
-  __TEXT.__auth_stubs: 0xf40
-  __TEXT.__objc_stubs: 0x17a0
-  __TEXT.__objc_methlist: 0xc78
-  __TEXT.__const: 0x1138
-  __TEXT.__cstring: 0x1ccb
-  __TEXT.__objc_methname: 0x29e3
+680.7.1.1.1
+  __TEXT.__text: 0x1fa54
+  __TEXT.__auth_stubs: 0xf70
+  __TEXT.__objc_stubs: 0x18a0
+  __TEXT.__objc_methlist: 0xcc8
+  __TEXT.__const: 0x13d8
+  __TEXT.__cstring: 0x1e6b
+  __TEXT.__objc_methname: 0x2ae7
   __TEXT.__objc_classname: 0x115
   __TEXT.__objc_methtype: 0x6ba
-  __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__oslogstring: 0xaae
-  __TEXT.__swift5_typeref: 0x1234
+  __TEXT.__gcc_except_tab: 0xbc
+  __TEXT.__oslogstring: 0x100e
+  __TEXT.__swift5_typeref: 0x10e0
   __TEXT.__swift5_capture: 0xe4
   __TEXT.__swift5_reflstr: 0x347
   __TEXT.__swift5_assocty: 0x140

   __TEXT.__swift5_fieldmd: 0x398
   __TEXT.__swift5_proto: 0x54
   __TEXT.__swift5_types: 0x60
-  __TEXT.__unwind_info: 0x8e0
-  __DATA_CONST.__auth_got: 0x7b0
-  __DATA_CONST.__got: 0x2c0
+  __TEXT.__unwind_info: 0x900
+  __DATA_CONST.__auth_got: 0x7c8
+  __DATA_CONST.__got: 0x2c8
   __DATA_CONST.__auth_ptr: 0x318
-  __DATA_CONST.__const: 0xb98
-  __DATA_CONST.__cfstring: 0x4a0
+  __DATA_CONST.__const: 0xc60
+  __DATA_CONST.__cfstring: 0x4c0
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x1c10
-  __DATA.__objc_selrefs: 0xaf0
-  __DATA.__objc_ivar: 0xc4
+  __DATA.__objc_const: 0x1c70
+  __DATA.__objc_selrefs: 0xb20
+  __DATA.__objc_ivar: 0xcc
   __DATA.__objc_data: 0x7c8
-  __DATA.__data: 0xd60
-  __DATA.__bss: 0xd08
-  __DATA.__common: 0xf0
+  __DATA.__data: 0xd50
+  __DATA.__bss: 0xcf8
+  __DATA.__common: 0xe0
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EAA2553C-2724-3D15-A62A-FF193458ED5A
-  Functions: 877
-  Symbols:   238
-  CStrings:  808
+  UUID: 2E14723D-2168-38A8-9091-77F52FC38995
+  Functions: 890
+  Symbols:   247
+  CStrings:  847
 
Symbols:
+ _RPCCUICallRecordingViewHeight
+ _RPCCUIModuleSpacing
+ _UILayoutFittingCompressedSize
+ __Block_object_dispose
+ __os_log_error_impl
+ _dispatch_queue_create
+ _dispatch_sync
+ _objc_retain_x23
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
+ "_currentTimerString"
+ "_synchronizationQueue"
+ "activityAttribution"
+ "com.apple.replaykit.backgroundactivity"
+ "com.apple.systemstatus.background-activity.replaykit.callrecording.recording"
+ "length"
+ "setSynchronizationQueue:"
+ "synchronizationQueue"
+ "systemLayoutSizeFittingSize:"
+ "updateTimerString:"
- " [INFO] %{public}s:%d adding background activity attribution=%@"
- " [INFO] %{public}s:%d created new background activity attribution=%@"
- " [INFO] %{public}s:%d removing background activity attribution=%@"
- " [INFO] %{public}s:%d setting user interaction block"
- "CONTROL_CENTER_HQLR_FOOTER"

```
