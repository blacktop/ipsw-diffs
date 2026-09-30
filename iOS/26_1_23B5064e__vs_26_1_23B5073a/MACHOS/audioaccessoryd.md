## audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

-31.8.1.1.0
-  __TEXT.__text: 0x1fa128
-  __TEXT.__auth_stubs: 0x2b10
-  __TEXT.__objc_stubs: 0x18560
-  __TEXT.__objc_methlist: 0xbd34
-  __TEXT.__const: 0x39e0
-  __TEXT.__gcc_except_tab: 0x4dc0
-  __TEXT.__cstring: 0x43663
-  __TEXT.__objc_classname: 0xa46
-  __TEXT.__objc_methname: 0x24787
-  __TEXT.__objc_methtype: 0x32ec
+31.10.0.0.0
+  __TEXT.__text: 0x1fc01c
+  __TEXT.__auth_stubs: 0x2b00
+  __TEXT.__objc_stubs: 0x183e0
+  __TEXT.__objc_methlist: 0xbc2c
+  __TEXT.__const: 0x3f60
+  __TEXT.__gcc_except_tab: 0x4dc8
+  __TEXT.__cstring: 0x435b3
+  __TEXT.__objc_classname: 0xa27
+  __TEXT.__objc_methname: 0x24553
+  __TEXT.__objc_methtype: 0x32e2
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__oslogstring: 0x83ca
   __TEXT.__ustring: 0x10

   __TEXT.__swift5_capture: 0x1960
   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
-  __TEXT.__unwind_info: 0x5810
+  __TEXT.__unwind_info: 0x57d0
   __TEXT.__eh_frame: 0x20a8
-  __DATA_CONST.__auth_got: 0x1598
-  __DATA_CONST.__got: 0xca0
+  __DATA_CONST.__auth_got: 0x1590
+  __DATA_CONST.__got: 0xca8
   __DATA_CONST.__auth_ptr: 0x570
-  __DATA_CONST.__const: 0xab38
-  __DATA_CONST.__cfstring: 0x9b80
-  __DATA_CONST.__objc_classlist: 0x2f8
+  __DATA_CONST.__const: 0xab40
+  __DATA_CONST.__cfstring: 0x9c20
+  __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x78
-  __DATA_CONST.__objc_superrefs: 0x198
+  __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_doubleobj: 0x40
   __DATA_CONST.__objc_intobj: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x2f0
   __DATA_CONST.__objc_dictobj: 0x500
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA.__objc_const: 0x1a4c8
-  __DATA.__objc_selrefs: 0x7be8
-  __DATA.__objc_ivar: 0x14cc
-  __DATA.__objc_data: 0x2ab8
-  __DATA.__data: 0x42d8
-  __DATA.__bss: 0x6ae0
+  __DATA.__objc_const: 0x1a328
+  __DATA.__objc_selrefs: 0x7b60
+  __DATA.__objc_ivar: 0x14b4
+  __DATA.__objc_data: 0x2a68
+  __DATA.__data: 0x4268
+  __DATA.__bss: 0x6ad0
   __DATA.__common: 0x398
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B100BDF6-61CD-3096-AD57-D9A07ECFD3A6
-  Functions: 9379
+  UUID: CC1B22CD-4CAC-3397-AB3A-0CC62BE7BEB9
+  Functions: 9342
   Symbols:   1242
-  CStrings:  14758
+  CStrings:  14719
 
Symbols:
+ _FBSOpenApplicationOptionKeyUnlockDevice
+ _xpc_connection_copy_invalidation_reason
- _CUXPCEncodeNSError
- _xpc_copy
CStrings:
+ "### Activate failed: CID 0x%X, %@"
+ "### Invalidated unexpectedly for reason %s"
+ "-[AAController _activateXPC:]"
+ "-[AAController _activateXPCCompleted:]"
+ "-[AAController _activate]"
+ "-[AAFeatureOnboarding _receivedAssetManagerPTAppDownloadNotificationAction:forDevice:withAddress:]"
+ "-[AAFeatureOnboarding _receivedAssetManagerPTAppDownloadNotificationAction:forDevice:withAddress:]_block_invoke"
+ "-[AAFeatureOnboarding showAssetManagerDownloadPTAppNotificationForDevice:withErrorHandler:]_block_invoke_4"
+ "-[AAGestureControl _handleDualBudLongPressGestureForIdentifier:]"
+ "-[AAGestureControl _handleDualBudLongPressGestureForIdentifier:]_block_invoke"
+ "-[AAGestureControl _handleDualBudLongPressGestureForIdentifier:]_block_invoke_2"
+ "-[BTSmartRoutingDaemon triggerBtStateUpdate]_block_invoke"
+ "-[SRSourceDevice setBluetoothState:]"
+ "AAAssetManagerMissingTranslateAppNotifications"
+ "Activate: CID 0x%X"
+ "Activated: CID 0x%X"
+ "AssetManager PT App download notification delivered. deviceId: %@"
+ "AssetManager PT App download notification not delivered. deviceId: %@, error: %@"
+ "EvaluateNearbyDevicesForConnection: Invalid BT state %s, triggering update"
+ "PERSONAL_TRANSLATOR_DOWNLOAD_ALERT_BODY"
+ "PERSONAL_TRANSLATOR_DOWNLOAD_ALERT_CANCEL"
+ "PERSONAL_TRANSLATOR_DOWNLOAD_ALERT_INSTALL"
+ "PERSONAL_TRANSLATOR_DOWNLOAD_ALERT_TITLE"
+ "PERSONAL_TRANSLATOR_DOWNLOAD_BODY"
+ "PERSONAL_TRANSLATOR_DOWNLOAD_TITLE"
+ "PT App Download notification shown"
+ "PT App Download: Unable to deeplink to address %@"
+ "PT App notification not shown due to %{error}"
+ "Re-activate: CID 0x%X"
+ "Setting bluetoothState %s -> %s"
+ "Showing PT App Download alert!"
+ "TI,N,V_coreBluetoothInternalFlag"
+ "TriggerBtStateUpdate: Failed. cbDiscovery is null"
+ "TriggerBtStateUpdate: cbDiscoveryBT %s sourceBT %s"
+ "Unable to find device for identifier: %@, skipping PT App Download Notification"
+ "User clicked on AssetManager PT App download notification for device: %@, open settings page for device %@ URL %@"
+ "User dismissed AssetManager PT App download notification for device: %@"
+ "_activateXPC:"
+ "_activateXPCCompleted:"
+ "_coreBluetoothInternalFlag"
+ "_handleDualBudLongPressGestureForIdentifier:"
+ "_notificationContentForPTAppDownload:"
+ "_receivedAssetManagerPTAppDownloadNotificationAction:forDevice:withAddress:"
+ "coreBluetoothInternalFlag"
+ "itms-apps://apps.apple.com/app/translate/id1514844618"
+ "openSensitiveURL:withOptions:error:"
+ "service:account:inviteDroppedForSessionID:fromID:context:error:"
+ "setCoreBluetoothInternalFlag:"
+ "settings-navigation://"
+ "showAssetManagerDownloadPTAppNotificationForDevice:withErrorHandler:"
+ "triggerBtStateUpdate"
+ "v64@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSData\"48@\"NSError\"56"
- "### Register controller failed: %@"
- "### Registration with manager failed: CID 0x%X, %@"
- "### Shared XPC connection interrupted"
- "### Shared XPC connection invalidated"
- "### Shared connection activation failed: %@"
- "-[AAController _registerWithSharedManager:]"
- "-[AAController _registerWithSharedManager:]_block_invoke"
- "-[AAController activateWithCompletion:]"
- "-[AAControllerSharedXPCManager _activateSharedConnection]"
- "-[AAControllerSharedXPCManager _ensureSharedConnectionWithCompletion:]"
- "-[AAControllerSharedXPCManager _handleActivationReply:]"
- "-[AAControllerSharedXPCManager _handleConnectionInterruption]"
- "-[AAControllerSharedXPCManager _handleXPCEvent:]"
- "-[AAControllerSharedXPCManager _processPendingMessages]"
- "-[AAControllerSharedXPCManager _sendMessage:controller:queue:replyHandler:]"
- "-[AAControllerSharedXPCManager _sendMessage:controller:queue:replyHandler:]_block_invoke_2"
- "-[AAControllerSharedXPCManager init]"
- "-[AAControllerSharedXPCManager invalidate]_block_invoke"
- "-[AAControllerSharedXPCManager registerController:completion:]_block_invoke"
- "-[AAControllerSharedXPCManager sendMessage:controller:queue:replyHandler:]_block_invoke"
- "-[AAControllerSharedXPCManager unregisterController:]_block_invoke"
- "-[AAGestureControl _handleDualBudLongPressGesture]"
- "-[AAGestureControl _handleDualBudLongPressGesture]_block_invoke"
- "AAControllerSharedXPCManager"
- "AAControllerSharedXPCManager initialized"
- "Activating shared XPC connection"
- "Already registered with manager: CID 0x%X"
- "Attempting to reestablish connection after interruption"
- "Controller not registered"
- "Establishing shared XPC connection"
- "Invalidating AAControllerSharedXPCManager"
- "Manager invalidated"
- "No XPC connection"
- "No more registered controllers, keeping connection alive for reuse"
- "Processing %lu pending messages"
- "Queued message for controller %@, pending count: %lu"
- "Received XPC reply for controller %@: %@"
- "Registered controller %@, total: %lu"
- "Registered with manager: CID 0x%X"
- "Registering with shared manager: CID 0x%X"
- "Sending XPC message for controller %@: %@"
- "Shared XPC connection activated successfully"
- "T@\"NSMutableArray\",&,N,V_pendingMessages"
- "T@\"NSMutableSet\",&,N,V_registeredControllers"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_managerQueue"
- "TB,N,V_connectionActive"
- "TB,N,V_invalidateCalled"
- "Unregistered controller %@, remaining: %lu"
- "_activateSharedConnection"
- "_connectionActive"
- "_connectionEstablished"
- "_distributeDeviceInfoArray:"
- "_distributeXPCMessage:"
- "_ensureSharedConnectionWithCompletion:"
- "_handleActivationReply:"
- "_handleConnectionInterruption"
- "_handleConnectionInvalidation"
- "_handleDualBudLongPressGesture"
- "_handleXPCEvent:"
- "_invalidateConnection"
- "_managerQueue"
- "_pendingActivations"
- "_pendingMessages"
- "_processPendingMessages"
- "_registerWithSharedManager:"
- "_registeredControllers"
- "_registeredWithManager"
- "_sendMessage:controller:queue:replyHandler:"
- "_sharedXPCConnection"
- "com.apple.AAControllerSharedXPCManager"
- "connectionActive"
- "controller"
- "errC"
- "errD"
- "errM"
- "errO"
- "invalidateCalled"
- "pendingMessages"
- "registerController:completion:"
- "registeredControllers"
- "replyHandler"
- "sendMessage:controller:queue:replyHandler:"
- "service:account:inviteDroppedForSessionID:fromID:error:"
- "setConnectionActive:"
- "setInvalidateCalled:"
- "setManagerQueue:"
- "setPendingMessages:"
- "setRegisteredControllers:"
- "sharedManager"
- "unregisterController:"
- "v48@0:8@16@24@32@?40"
- "v56@0:8@\"IDSService\"16@\"IDSAccount\"24@\"NSString\"32@\"NSString\"40@\"NSError\"48"

```
