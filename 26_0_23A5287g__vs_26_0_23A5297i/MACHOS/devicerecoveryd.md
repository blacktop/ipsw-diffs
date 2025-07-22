## devicerecoveryd

> `/System/Library/PrivateFrameworks/DeviceRecovery.framework/Support/devicerecoveryd`

```diff

-85.0.0.0.9
-  __TEXT.__text: 0x1edf4
-  __TEXT.__auth_stubs: 0xdf0
-  __TEXT.__objc_stubs: 0x1ee0
-  __TEXT.__objc_methlist: 0xa3c
-  __TEXT.__cstring: 0x6422
+88.0.0.0.4
+  __TEXT.__text: 0x1f78c
+  __TEXT.__auth_stubs: 0xe00
+  __TEXT.__objc_stubs: 0x1fa0
+  __TEXT.__objc_methlist: 0xb2c
+  __TEXT.__cstring: 0x63f9
   __TEXT.__const: 0x58
-  __TEXT.__objc_methname: 0x20f5
-  __TEXT.__oslogstring: 0x2b42
-  __TEXT.__objc_classname: 0x134
-  __TEXT.__objc_methtype: 0x51e
-  __TEXT.__gcc_except_tab: 0x5c4
-  __TEXT.__unwind_info: 0x580
-  __DATA_CONST.__auth_got: 0x708
+  __TEXT.__objc_methname: 0x2193
+  __TEXT.__oslogstring: 0x2c46
+  __TEXT.__objc_classname: 0x125
+  __TEXT.__objc_methtype: 0x4d7
+  __TEXT.__gcc_except_tab: 0x6f0
+  __TEXT.__unwind_info: 0x5f0
+  __DATA_CONST.__auth_got: 0x710
   __DATA_CONST.__got: 0x178
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xae8
-  __DATA_CONST.__cfstring: 0x2140
-  __DATA_CONST.__objc_classlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__const: 0xb98
+  __DATA_CONST.__cfstring: 0x20c0
+  __DATA_CONST.__objc_classlist: 0x30
+  __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x1550
-  __DATA.__objc_selrefs: 0x970
-  __DATA.__objc_ivar: 0xb0
-  __DATA.__objc_data: 0x190
-  __DATA.__data: 0x280
-  __DATA.__bss: 0x1d0
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x30
+  __DATA_CONST.__objc_intobj: 0x60
+  __DATA.__objc_const: 0x1308
+  __DATA.__objc_selrefs: 0x9c8
+  __DATA.__objc_ivar: 0xa8
+  __DATA.__objc_data: 0x1e0
+  __DATA.__data: 0x220
+  __DATA.__bss: 0x1e0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /System/Library/PrivateFrameworks/UserManagementLayout.framework/UserManagementLayout
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1305C67F-5683-349F-A516-503CF95D64CA
-  Functions: 582
-  Symbols:   283
-  CStrings:  1619
+  UUID: 211A4108-6049-3AB9-981F-47D617FD6809
+  Functions: 616
+  Symbols:   284
+  CStrings:  1627
 
Symbols:
+ _objc_setProperty_atomic
CStrings:
+ "%{public}s: Device Recovery Override Service connection interrupted"
+ "%{public}s: Device Recovery Override Service connection invalidated"
+ "%{public}s: Error removing override: %{public}@"
+ "%{public}s: Error setting override: %{public}@ -> %{public}@"
+ "%{public}s: Error talking to DeviceRecoveryOverrideService: %{public}@"
+ "%{public}s: Found internal DeviceRecovery cookie file but did not find a '%{public}@' entry"
+ "%{public}s: LockStateInfo: %@"
+ "-[DeviceRecoveryEnvironmentWorker populateDREDescription:]"
+ "-[DeviceRecoveryEnvironmentWorker populateDREReason]"
+ "-[DeviceRecoveryOverrideClient allOverrides]"
+ "-[DeviceRecoveryOverrideClient allOverrides]_block_invoke"
+ "-[DeviceRecoveryOverrideClient fetchOverride:]"
+ "-[DeviceRecoveryOverrideClient fetchOverride:]_block_invoke"
+ "-[DeviceRecoveryOverrideClient init]"
+ "-[DeviceRecoveryOverrideClient init]_block_invoke"
+ "-[DeviceRecoveryOverrideClient removeAllOverrides]"
+ "-[DeviceRecoveryOverrideClient removeAllOverrides]_block_invoke"
+ "-[DeviceRecoveryOverrideClient setOverride:value:]"
+ "-[DeviceRecoveryOverrideClient setOverride:value:]_block_invoke"
+ "-[DeviceRecoveryService init]"
+ "-[DeviceRecoveryService init]_block_invoke"
+ "/Library/Caches/com.apple.xbs/Sources/DeviceRecovery/Common/DeviceRecoveryEnvironmentWorker.m"
+ "/Library/Caches/com.apple.xbs/Sources/DeviceRecovery/DeviceRecovery_Framework/DeviceRecoveryOverrideClient.m"
+ "/var/db/com.apple.DeviceRecovery.entryInfo"
+ "01:59:00"
+ "@20@0:8i16"
+ "CreateCookieAndCleanup"
+ "DREEntryDescription"
+ "DREEntryReasonEnum"
+ "DREIsRunningInDeviceRecoveryEnvironment"
+ "DREStringFromEntryReason:"
+ "DeviceHandle"
+ "DeviceRecoveryEnvironmentWorker"
+ "DeviceRecoveryOverrideClient"
+ "Jul 12 2025"
+ "T@\"NSDictionary\",R,N"
+ "T@\"NSNumber\",&,N"
+ "T@\"NSString\",&,N"
+ "T@\"NSXPCConnection\",&,V_serviceConnection"
+ "Ti,N"
+ "_serviceConnection"
+ "allOverrides"
+ "fetchOverride:"
+ "removeAllOverrides"
+ "self.serviceConnection != nil"
+ "serviceConnection"
+ "setBrainBundlePath:"
+ "setBrainLoadResult:"
+ "setBrainType:"
+ "setFreeSpaceThreshold:"
+ "setIssuesScanResult:"
+ "setNetworkAvailableResult:"
+ "setOverride:value:"
+ "setRecoveryResult:"
+ "setServiceConnection:"
+ "setSystemDataPath:"
+ "setUpdateVolumePath:"
+ "setUserAuthResult:"
+ "setUserDataPath:"
+ "sharedWorker"
+ "v16@?0@\"NSDictionary\"8"
+ "v16@?0@8"
+ "\x91"
- "!"
- "%{public}s: Could not create an NSXPCInterface for: %{public}@"
- "%{public}s: DREEntryReason error: %{public}@"
- "%{public}s: DeviceRecoveryEnvironmentService start failed: %{public}@"
- "-[DeviceRecoveryEnvironmentService listener:shouldAcceptNewConnection:]"
- "-[DeviceRecoveryEnvironmentService listener:shouldAcceptNewConnection:]_block_invoke"
- "-[DeviceRecoveryEnvironmentService populateDREDescription:]"
- "-[DeviceRecoveryEnvironmentService populateDREReason]"
- "-[DeviceRecoveryEnvironmentService startService]"
- "-[DeviceRecoveryService initWithEnvironmentService:]"
- "-[DeviceRecoveryService initWithEnvironmentService:]_block_invoke"
- "/Library/Caches/com.apple.xbs/Sources/DeviceRecovery/Common/DeviceRecoveryEnvironment.m"
- "/Library/Caches/com.apple.xbs/Sources/DeviceRecovery/Daemon/DeviceRecoveryEnvironmentService.m"
- "22:02:16"
- "@\"DeviceRecoveryEnvironmentService\""
- "DREEntryDescription_block_invoke"
- "DREEntryReasonEnum_block_invoke"
- "DREIsRunningInDeviceRecoveryEnvironemnt"
- "Device Recovery Entry Description: %@"
- "Device Recovery Entry Reason: %@"
- "DeviceRecoveryEnvironmentService"
- "DeviceRecoveryEnvironmentServiceInterface"
- "EntryReason override has an invalid value: %d (must be between 0 and %d)"
- "EntryReason override is not an NSNumber (%s)"
- "GetDREEntryDescription"
- "GetDREEntryReason"
- "GetServiceConnection"
- "Jul  1 2025"
- "T@\"DeviceRecoveryEnvironmentService\",&,N,V_environmentService"
- "T@\"NSXPCConnection\",W,N,V_clientConnection"
- "_clientConnection"
- "_environmentService"
- "clientConnection"
- "com.apple.DeviceRecoveryEnvironmentService"
- "connection != nil"
- "entryReason < RECOVERY_REASON_SIZE"
- "environmentEntryDescription"
- "environmentEntryReason"
- "environmentService"
- "environmentService != nil"
- "fetchDREEntryDescription:"
- "fetchDREEntryReason:"
- "initWithEnvironmentService:"
- "overrideEnvEntryDesc"
- "overrideEnvEntryReason"
- "setClientConnection:"
- "setEnvironmentService:"
- "v12@?0i8"
- "v16@?0@\"NSString\"8"
- "v24@0:8@?<v@?@\"NSString\">16"
- "v24@0:8@?<v@?i>16"
- "\xa1"

```
