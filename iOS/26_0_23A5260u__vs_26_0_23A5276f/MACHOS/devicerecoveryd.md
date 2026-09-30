## devicerecoveryd

> `/System/Library/PrivateFrameworks/DeviceRecovery.framework/Support/devicerecoveryd`

```diff

-74.0.0.0.2
-  __TEXT.__text: 0x1def0
+82.0.0.502.1
+  __TEXT.__text: 0x1e22c
   __TEXT.__auth_stubs: 0xd80
-  __TEXT.__objc_stubs: 0x1d40
-  __TEXT.__objc_methlist: 0xa04
-  __TEXT.__cstring: 0x628c
+  __TEXT.__objc_stubs: 0x1e60
+  __TEXT.__objc_methlist: 0xa3c
+  __TEXT.__cstring: 0x633d
   __TEXT.__const: 0x58
-  __TEXT.__oslogstring: 0x2647
-  __TEXT.__gcc_except_tab: 0x524
-  __TEXT.__objc_methname: 0x1f66
+  __TEXT.__objc_methname: 0x20b3
+  __TEXT.__oslogstring: 0x26e6
   __TEXT.__objc_classname: 0x134
   __TEXT.__objc_methtype: 0x51e
-  __TEXT.__unwind_info: 0x550
+  __TEXT.__gcc_except_tab: 0x524
+  __TEXT.__unwind_info: 0x568
   __DATA_CONST.__auth_got: 0x6d0
-  __DATA_CONST.__got: 0x160
+  __DATA_CONST.__got: 0x168
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0xad0
-  __DATA_CONST.__cfstring: 0x1fe0
+  __DATA_CONST.__const: 0xad8
+  __DATA_CONST.__cfstring: 0x2020
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x48
-  __DATA.__objc_const: 0x14f0
-  __DATA.__objc_selrefs: 0x908
-  __DATA.__objc_ivar: 0xa8
+  __DATA.__objc_const: 0x1550
+  __DATA.__objc_selrefs: 0x950
+  __DATA.__objc_ivar: 0xb0
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x288
   __DATA.__bss: 0x1d0

   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/DeviceRecoveryBrainSupport.framework/DeviceRecoveryBrainSupport
   - /System/Library/PrivateFrameworks/LoggingSupport.framework/LoggingSupport
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaKit.framework/MediaKit
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /System/Library/PrivateFrameworks/OSASubmissionClient.framework/OSASubmissionClient

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 438C57ED-B9E6-3C04-A06A-654BED5BF2F5
-  Functions: 574
-  Symbols:   273
-  CStrings:  1563
+  UUID: FF0E008C-37A8-3422-874F-ACAF0080A43A
+  Functions: 581
+  Symbols:   274
+  CStrings:  1586
 
Symbols:
+ _OBJC_CLASS_$_MCProfileConnection
CStrings:
+ "%{public}s: Mounted System Data Volume: %{public}@"
+ "%{public}s: Mounted User Data Volume: %{public}@"
+ "%{public}s: unlockScreenType = %d, simplePasscodeType = %d"
+ "-[DeviceRecoveryService initWithEnvironmentService:]_block_invoke_2"
+ "-[DeviceRecoveryService mountSystemDataVolume]"
+ "00:44:51"
+ "Jun 17 2025"
+ "SimplePasscodeType"
+ "Ti,N,V_simplePasscodeType"
+ "Ti,N,V_unlockScreenType"
+ "UnlockScreenType"
+ "_simplePasscodeType"
+ "_unlockScreenType"
+ "mountSystemDataVolume"
+ "numberWithUnsignedChar:"
+ "setSimplePasscodeType:"
+ "setUnlockScreenType:"
+ "sharedConnection"
+ "simplePasscodeType"
+ "success && (error == nil)"
+ "unlockScreenType"
+ "unlockScreenTypeForSharedDataVolume:OutSimplePasscodeType:"
+ "unlockScreenTypeWithOutSimplePasscodeType:"
+ "\xa1"
- "21:21:17"
- "Jun  1 2025"
- "\x91"

```
