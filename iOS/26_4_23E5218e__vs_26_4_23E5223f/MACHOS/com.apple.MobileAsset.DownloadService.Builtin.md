## com.apple.MobileAsset.DownloadService.Builtin

> `/System/Library/PrivateFrameworks/MobileAssetDaemon.framework/XPCServices/com.apple.MobileAsset.DownloadService.Builtin.xpc/com.apple.MobileAsset.DownloadService.Builtin`

```diff

-1837.100.250.0.0
-  __TEXT.__text: 0x23064
-  __TEXT.__auth_stubs: 0xc60
-  __TEXT.__objc_stubs: 0x4520
-  __TEXT.__objc_methlist: 0x1df4
-  __TEXT.__const: 0x6ac
-  __TEXT.__cstring: 0x41c0
-  __TEXT.__gcc_except_tab: 0x1390
-  __TEXT.__objc_methname: 0x5c5f
-  __TEXT.__oslogstring: 0x5bb3
+1837.100.266.0.0
+  __TEXT.__text: 0x23a44
+  __TEXT.__auth_stubs: 0xc70
+  __TEXT.__objc_stubs: 0x4600
+  __TEXT.__objc_methlist: 0x1e3c
+  __TEXT.__const: 0x69c
+  __TEXT.__cstring: 0x415c
+  __TEXT.__gcc_except_tab: 0x1424
+  __TEXT.__objc_methname: 0x5e4c
+  __TEXT.__oslogstring: 0x5f41
   __TEXT.__objc_classname: 0x35e
   __TEXT.__objc_methtype: 0x1224
   __TEXT.__swift5_typeref: 0xda

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_proto: 0x24
   __TEXT.__swift5_types: 0xc
-  __TEXT.__unwind_info: 0x888
+  __TEXT.__unwind_info: 0x880
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0x640
+  __DATA_CONST.__auth_got: 0x648
   __DATA_CONST.__got: 0x348
   __DATA_CONST.__auth_ptr: 0x160
   __DATA_CONST.__const: 0x860
-  __DATA_CONST.__cfstring: 0x2b40
+  __DATA_CONST.__cfstring: 0x2ba0
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80

   __DATA_CONST.__objc_arraydata: 0x388
   __DATA_CONST.__objc_dictobj: 0x140
   __DATA_CONST.__objc_arrayobj: 0x78
-  __DATA.__objc_const: 0x3130
-  __DATA.__objc_selrefs: 0x1500
-  __DATA.__objc_ivar: 0x268
+  __DATA.__objc_const: 0x31c0
+  __DATA.__objc_selrefs: 0x1540
+  __DATA.__objc_ivar: 0x274
   __DATA.__objc_data: 0x5b8
   __DATA.__data: 0x698
   __DATA.__crash_info: 0x148
-  __DATA.__bss: 0x500
+  __DATA.__bss: 0x520
   - /System/Library/Frameworks/AuthenticationServices.framework/AuthenticationServices
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: FE7DDA1B-9E66-3E2B-A006-2F11F1D568C5
-  Functions: 670
-  Symbols:   331
-  CStrings:  2275
+  UUID: 2340C778-F1EB-3A05-8F79-5D8E42EA9207
+  Functions: 678
+  Symbols:   332
+  CStrings:  2308
 
Symbols:
+ _MKBGetDeviceLockState
CStrings:
+ "#"
+ "DownloadManagerSyncDelaySecs"
+ "DownloadServiceFailRegistration-%@"
+ "Exiting service(FailRegistration default set)"
+ "SupportedFeaturesOverride-%@"
+ "T@\"NSString\",&,V_serviceName"
+ "TB,V_firstUnlockNotificationTokenValid"
+ "TB,V_lockStateChangedNotificationTokenValid"
+ "Ti,V_firstUnlockNotificationToken"
+ "Ti,V_lockStateChangedNotificationToken"
+ "[MADownloadServiceBuiltin]: Attempting to start up builtin service built Feb 23 2026 04:31:03"
+ "[MAUnlockMonitor]: Failed to register for first unlock notification"
+ "[MAUnlockMonitor]: Failed to register for lock state changed notifications"
+ "[MAUnlockMonitor]: FirstUnlockNotification: Handling notification"
+ "[MAUnlockMonitor]: FirstUnlockNotification: Object invalid"
+ "[MAUnlockMonitor]: LockStateChanged notification received | state:%{public}d"
+ "[MAUnlockMonitor]: LockStateChanged: Device unlocked | KeybagState:%{public}d"
+ "[MAUnlockMonitor]: LockStateChanged: Object invalid"
+ "[MAUnlockMonitor]: Notifying client about beyond first unlock | BeyondFirstUnlock:%{public}@ | Error:%{public}@"
+ "[Manager]: Delay completed. Re-attempting sync with nsurlsessiond"
+ "[Manager]: Delaying sync with nsurlsessiond due to default | Delay:%{public}@"
+ "[RegisterClient]: Feature set override is set but in a unexpected format"
+ "[RegisterClient]: Using overridden feature set | %{public}@"
+ "_firstUnlockNotificationToken"
+ "_firstUnlockNotificationTokenValid"
+ "_lockStateChangedNotificationToken"
+ "_lockStateChangedNotificationTokenValid"
+ "_serviceName"
+ "com.apple.mobile.keybagd.lock_status"
+ "firstUnlockNotificationToken"
+ "firstUnlockNotificationTokenValid"
+ "intValue"
+ "lockStateChangedNotificationToken"
+ "lockStateChangedNotificationTokenValid"
+ "longLongValue"
+ "serviceName"
+ "setFirstUnlockNotificationToken:"
+ "setFirstUnlockNotificationTokenValid:"
+ "setLockStateChangedNotificationToken:"
+ "setLockStateChangedNotificationTokenValid:"
+ "setServiceName:"
- "Assertion failed: (status == NOTIFY_STATUS_OK), Should be able to register for first unlock notification"
- "BUG IN MobileAsset: Assertion failed: (status == NOTIFY_STATUS_OK), Should be able to register for first unlock notification"
- "TB,V_notificationTokenValid"
- "Ti,V_notificationToken"
- "[MADownloadServiceBuiltin]: Attempting to start up builtin service built Feb 16 2026 02:15:55"
- "_notificationToken"
- "_notificationTokenValid"
- "notificationToken"
- "notificationTokenValid"
- "setNotificationToken:"
- "setNotificationTokenValid:"

```
