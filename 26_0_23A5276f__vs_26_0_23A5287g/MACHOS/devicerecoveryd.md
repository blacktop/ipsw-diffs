## devicerecoveryd

> `/System/Library/PrivateFrameworks/DeviceRecovery.framework/Support/devicerecoveryd`

```diff

-82.0.0.502.1
-  __TEXT.__text: 0x1e22c
-  __TEXT.__auth_stubs: 0xd80
-  __TEXT.__objc_stubs: 0x1e60
+85.0.0.0.9
+  __TEXT.__text: 0x1edf4
+  __TEXT.__auth_stubs: 0xdf0
+  __TEXT.__objc_stubs: 0x1ee0
   __TEXT.__objc_methlist: 0xa3c
-  __TEXT.__cstring: 0x633d
+  __TEXT.__cstring: 0x6422
   __TEXT.__const: 0x58
-  __TEXT.__objc_methname: 0x20b3
-  __TEXT.__oslogstring: 0x26e6
+  __TEXT.__objc_methname: 0x20f5
+  __TEXT.__oslogstring: 0x2b42
   __TEXT.__objc_classname: 0x134
   __TEXT.__objc_methtype: 0x51e
-  __TEXT.__gcc_except_tab: 0x524
-  __TEXT.__unwind_info: 0x568
-  __DATA_CONST.__auth_got: 0x6d0
-  __DATA_CONST.__got: 0x168
+  __TEXT.__gcc_except_tab: 0x5c4
+  __TEXT.__unwind_info: 0x580
+  __DATA_CONST.__auth_got: 0x708
+  __DATA_CONST.__got: 0x178
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xad8
-  __DATA_CONST.__cfstring: 0x2020
+  __DATA_CONST.__const: 0xae8
+  __DATA_CONST.__cfstring: 0x2140
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x1550
-  __DATA.__objc_selrefs: 0x950
+  __DATA.__objc_selrefs: 0x970
   __DATA.__objc_ivar: 0xb0
   __DATA.__objc_data: 0x190
-  __DATA.__data: 0x288
+  __DATA.__data: 0x280
   __DATA.__bss: 0x1d0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaKit.framework/MediaKit
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
+  - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
+  - /System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate
   - /System/Library/PrivateFrameworks/OSASubmissionClient.framework/OSASubmissionClient
   - /System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics
   - /System/Library/PrivateFrameworks/OSAnalyticsPrivate.framework/OSAnalyticsPrivate
   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /System/Library/PrivateFrameworks/UserManagementLayout.framework/UserManagementLayout
-  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FF0E008C-37A8-3422-874F-ACAF0080A43A
-  Functions: 581
-  Symbols:   274
-  CStrings:  1586
+  UUID: 1305C67F-5683-349F-A516-503CF95D64CA
+  Functions: 582
+  Symbols:   283
+  CStrings:  1619
 
Symbols:
+ _MASetPallasAudienceForType
+ _MASetPallasEnabled
+ _MASetPallasUrlForType
+ _MASetServerUrlOverride
+ _MKBGetDeviceLockStateInfo
+ _MSUCopyEnvInfoForNeRD
+ _OBJC_CLASS_$_NSURL
+ _kMKBInfoBackOff
+ _objc_retain_x25
+ _os_variant_allows_internal_security_policies
- _MGGetBoolAnswer
CStrings:
+ "%lu"
+ "%{public}s: %{public}s: AssertMacros: %{public}s, %{public}s file: %{public}s, line: %{public}d\n"
+ "%{public}s: Event payload data \"%{public}@\" is unsupported type \"%{public}@\". Supported Types: NSString, NSNumber, NSData, NSDate, NSError"
+ "%{public}s: Unable to mount update partition: %{public}d"
+ "%{public}s: Unsupported value for pallas-server-override detected. Ignoring"
+ "%{public}s: [DownloadRecoveryBrain]: Disabling pallas due to override"
+ "%{public}s: [DownloadRecoveryBrain]: No URL override found for DeviceRecoveryBrain asset download. Using default"
+ "%{public}s: [DownloadRecoveryBrain]: No asset audience override found for DeviceRecoveryBrain. Using default asset audience for brain download"
+ "%{public}s: [DownloadRecoveryBrain]: No data passed in from BootedOS. Using default asset audience/URL for brain download"
+ "%{public}s: [DownloadRecoveryBrain]: Pallas is enabled"
+ "%{public}s: [DownloadRecoveryBrain]: Setting pallas URL to customer instance due to override"
+ "%{public}s: [DownloadRecoveryBrain]: Setting pallas URL to internal instance due to override"
+ "%{public}s: [DownloadRecoveryBrain]: Updating URL for DeviceRecoveryBrain asset download to '%@'"
+ "%{public}s: [DownloadRecoveryBrain]: Updating asset audience for DeviceRecoveryBrain asset to '%@'"
+ "%{public}s: user authentication failed - invalid passcode - backoff = %g seconds"
+ "-[DeviceRecoveryService initWithEnvironmentService:]_block_invoke"
+ "22:02:16"
+ "BooteOSDREBrainAssetURL"
+ "BootedOSDREBrainAssetAudience"
+ "BootedOSHasPallasDisabled"
+ "Error talking to DeviceRecoveryBrain"
+ "Error talking to the DeviceRecoveryBrain"
+ "Failed to mount user data volume - invalid passcode: %@"
+ "Failed to mount user data volume: %@"
+ "Jul  1 2025"
+ "PasscodeBackOffEndDate"
+ "StaticString"
+ "URLWithString:"
+ "customer"
+ "dateWithTimeIntervalSinceNow:"
+ "doubleValue"
+ "https://gdmf-staging-int.apple.com/v2/assets"
+ "https://gdmf.apple.com/v2/assets"
+ "internal"
+ "pallas-server-override"
+ "userInfo"
- "%@: %@"
- "%{public}s: %{public}s: AssertMacros: %{public}s, %{public}s file: %{public}s, line: %d\n"
- "%{public}s: Event payload data \"%{public}@\" is unsupported type \"%{public}@\". Supported Types: NSString, NSNumber, NSData, NSDate"
- "-[DeviceRecoveryService initWithEnvironmentService:]_block_invoke_2"
- "00:44:51"
- "Failed to mount user data volume"
- "Failed to mount user data volume - invalid passcode"
- "InternalBuild"
- "IsInternalBuild"
- "Jun 17 2025"
- "LBJfwOEzExRxzlAnSuI7eg"
- "failed to mount update volume: %d"

```
