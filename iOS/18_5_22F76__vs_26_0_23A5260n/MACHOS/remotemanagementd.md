## remotemanagementd

> `/System/Library/PrivateFrameworks/RemoteManagement.framework/remotemanagementd`

```diff

-560.4.11.0.0
-  __TEXT.__text: 0x91924
-  __TEXT.__auth_stubs: 0x860
-  __TEXT.__objc_stubs: 0xc1c0
-  __TEXT.__objc_methlist: 0x48c8
+578.0.1.0.0
+  __TEXT.__text: 0x921e8
+  __TEXT.__auth_stubs: 0x840
+  __TEXT.__objc_stubs: 0xc220
+  __TEXT.__objc_methlist: 0x4958
   __TEXT.__const: 0xf0
-  __TEXT.__gcc_except_tab: 0x4914
-  __TEXT.__cstring: 0x2e2d
-  __TEXT.__objc_classname: 0xfc8
-  __TEXT.__objc_methname: 0xef15
-  __TEXT.__objc_methtype: 0x2674
-  __TEXT.__oslogstring: 0xbbba
+  __TEXT.__gcc_except_tab: 0x4908
+  __TEXT.__cstring: 0x2e66
+  __TEXT.__objc_classname: 0x1004
+  __TEXT.__objc_methname: 0xeff0
+  __TEXT.__objc_methtype: 0x2692
+  __TEXT.__oslogstring: 0xbd3e
   __TEXT.__ustring: 0x246
-  __TEXT.__unwind_info: 0x1f90
-  __DATA_CONST.__auth_got: 0x440
-  __DATA_CONST.__got: 0x960
-  __DATA_CONST.__const: 0x2648
+  __TEXT.__unwind_info: 0x1fb8
+  __DATA_CONST.__auth_got: 0x430
+  __DATA_CONST.__got: 0x958
+  __DATA_CONST.__const: 0x26d0
   __DATA_CONST.__cfstring: 0x32e0
-  __DATA_CONST.__objc_classlist: 0x2e0
+  __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x1c0
+  __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_intobj: 0x138
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x8368
-  __DATA.__objc_selrefs: 0x3490
-  __DATA.__objc_ivar: 0x2a8
-  __DATA.__objc_data: 0x1cc0
+  __DATA.__objc_const: 0x8520
+  __DATA.__objc_selrefs: 0x34b8
+  __DATA.__objc_ivar: 0x2b0
+  __DATA.__objc_data: 0x1d60
   __DATA.__data: 0xc68
-  __DATA.__bss: 0x550
+  __DATA.__bss: 0x560
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/AppleIDSSOAuthentication.framework/AppleIDSSOAuthentication
   - /System/Library/PrivateFrameworks/ApplePushService.framework/ApplePushService
   - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
+  - /System/Library/PrivateFrameworks/BackgroundSystemTasks.framework/BackgroundSystemTasks
   - /System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities
   - /System/Library/PrivateFrameworks/DeviceIdentity.framework/DeviceIdentity
   - /System/Library/PrivateFrameworks/MDMClientLibrary.framework/MDMClientLibrary

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7A1745F4-480A-3A8E-93B4-D3CA06BE7082
-  Functions: 2521
-  Symbols:   441
-  CStrings:  4409
+  UUID: 27A95CE9-4368-3B1F-9B13-4D845A0CC83D
+  Functions: 2536
+  Symbols:   438
+  CStrings:  4432
 
Symbols:
+ _OBJC_CLASS_$_BGSystemTaskScheduler
- _OBJC_CLASS_$_NSBackgroundActivityScheduler
- _XPC_ACTIVITY_REQUIRE_NETWORK_CONNECTIVITY
- _xpc_dictionary_create
- _xpc_dictionary_set_bool
CStrings:
+ "@\"BGSystemTask\""
+ "@\"RMBackgroundTask\""
+ "Deallocated task: %{public}@"
+ "Expiration handler called for task: %{public}@"
+ "Failed to register task: %{public}@"
+ "Initialized task: %{public}@"
+ "Launch handler called for task: %{public}@"
+ "Q44@0:8@16B24@28^@36"
+ "RMBGSystemTaskWrapper"
+ "RMBackgroundTask"
+ "RMBackgroundTaskScheduler"
+ "StoreXPCListenerDelegate: WaitForDeclarationsToBeProcessed from proxy handler"
+ "T@\"BGSystemTask\",&,N,V_task"
+ "T@\"NSString\",&,N,V_identifier"
+ "T@\"RMBackgroundTask\",&,N,V_onRebootTask"
+ "T@\"RMBackgroundTask\",&,N,V_periodicSyncTask"
+ "Triggered on reboot background task"
+ "Triggered periodic sync background task"
+ "Wait for declarations to be processed failed: %{public}@"
+ "Wait for declarations to be processed success"
+ "WaitForDeclarations already running"
+ "WaitForDeclarations completed after notification with %{public}@..."
+ "WaitForDeclarations completes immediately with %{public}@..."
+ "WaitForDeclarations notification result %{public}@..."
+ "WaitForDeclarations timed out with %{public}@..."
+ "WaitForDeclarationsToBeProcessed with %{public}@..."
+ "WaitForProcessingOfDeclarations with %{public}@..."
+ "_checkActiveDeclarations:mustBeValid:storeIdentifier:error:"
+ "_initBackgroundTasks"
+ "_onRebootTask"
+ "_periodicSyncTask"
+ "_task"
+ "_waitForDeclarations:mustBeValid:timeout:storeIdentifier:completionHandler:"
+ "backgroundTask"
+ "backgroundTaskScheduler"
+ "deregisterTaskWithIdentifier:"
+ "initWithIdentifier:queue:callback:"
+ "initWithTask:"
+ "onRebootTask"
+ "periodicSyncTask"
+ "registerForTaskWithIdentifier:usingQueue:launchHandler:"
+ "setExpirationHandler:"
+ "setOnRebootTask:"
+ "setPeriodicSyncTask:"
+ "setTask:"
+ "setTaskCompleted"
+ "sharedScheduler"
+ "task"
+ "v16@?0@\"BGSystemTask\"8"
+ "v16@?0@\"RMBGSystemTaskWrapper\"8"
+ "v52@0:8@16B24d28@36@?44"
+ "waitForProcessingOfDeclarations:timeout:storeIdentifier:completionHandler:"
- "@\"NSBackgroundActivityScheduler\""
- "Q40@0:8@16@24^@32"
- "RMXPCActivityScheduler"
- "Schedule on reboot"
- "Schedule periodic sync"
- "T@\"NSBackgroundActivityScheduler\",&,N,V_onRebootActivity"
- "T@\"NSBackgroundActivityScheduler\",&,N,V_periodicSyncActivity"
- "Triggered on reboot"
- "Triggered periodic sync"
- "WaitForActiveAndValidDeclarations already running"
- "WaitForActiveAndValidDeclarations completed after notification with %{public}@..."
- "WaitForActiveAndValidDeclarations completes immediately with %{public}@..."
- "WaitForActiveAndValidDeclarations notification result %{public}@..."
- "WaitForActiveAndValidDeclarations timed out with %{public}@..."
- "_checkActiveAndValidDeclarations:storeIdentifier:error:"
- "_forceSyncWithCompletion:"
- "_onRebootActivity"
- "_onRebootWithCompletion:"
- "_periodicSyncActivity"
- "_scheduleOnReboot"
- "_schedulePeriodicSync"
- "_setAdditionalXPCActivityProperties:"
- "initWithIdentifier:"
- "onRebootActivity"
- "periodicSyncActivity"
- "scheduleWithBlock:"
- "setOnRebootActivity:"
- "setPeriodicSyncActivity:"
- "setPreregistered:"
- "v16@?0@?<v@?q>8"
- "xpcActivityScheduler"

```
