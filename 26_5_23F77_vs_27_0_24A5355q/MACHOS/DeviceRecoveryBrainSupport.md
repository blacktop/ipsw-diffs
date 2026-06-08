## DeviceRecoveryBrainSupport

> `/System/Library/PrivateFrameworks/DeviceRecoveryBrainSupport.framework/DeviceRecoveryBrainSupport`

```diff

-107.100.11.0.0
-  __TEXT.__text: 0x1cd40
-  __TEXT.__auth_stubs: 0xbb0
+142.0.0.0.0
+  __TEXT.__text: 0x1b648
   __TEXT.__objc_methlist: 0xd1c
   __TEXT.__const: 0x150
-  __TEXT.__oslogstring: 0x2bf1
-  __TEXT.__cstring: 0x3ee7
-  __TEXT.__gcc_except_tab: 0x5bc
-  __TEXT.__unwind_info: 0x5b0
-  __TEXT.__eh_frame: 0xa0
-  __TEXT.__objc_classname: 0x16b
-  __TEXT.__objc_methname: 0x209d
+  __TEXT.__oslogstring: 0x2c5a
+  __TEXT.__cstring: 0x4003
+  __TEXT.__gcc_except_tab: 0x538
+  __TEXT.__unwind_info: 0x568
+  __TEXT.__eh_frame: 0xa8
+  __TEXT.__objc_stubs: 0x1c20
+  __TEXT.__auth_stubs: 0xbe0
+  __TEXT.__objc_classname: 0x160
+  __TEXT.__objc_methname: 0x20be
   __TEXT.__objc_methtype: 0x490
-  __TEXT.__objc_stubs: 0x1bc0
-  __DATA_CONST.__got: 0x180
-  __DATA_CONST.__const: 0x900
+  __DATA_CONST.__const: 0x928
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa60
+  __DATA_CONST.__objc_selrefs: 0xa78
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_arraydata: 0x78
-  __AUTH_CONST.__auth_got: 0x5e8
+  __DATA_CONST.__got: 0x188
   __AUTH_CONST.__const: 0x2e0
-  __AUTH_CONST.__cfstring: 0x2340
+  __AUTH_CONST.__cfstring: 0x2420
   __AUTH_CONST.__objc_const: 0xdb8
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x50
+  __AUTH_CONST.__auth_got: 0x600
   __AUTH.__objc_data: 0x2d0
   __DATA.__objc_ivar: 0x68
   __DATA.__data: 0x23c

   - /System/Library/PrivateFrameworks/APFS.framework/APFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 49EE9BCE-996D-3730-8102-6897AB8FB1A5
-  Functions: 558
-  Symbols:   1358
-  CStrings:  1470
+  UUID: 99D0A05B-13FB-317F-8CFB-3EEA4DC5F2D6
+  Functions: 555
+  Symbols:   1355
+  CStrings:  1491
 
Symbols:
+ -[DeviceRecoveryBrainSpaceManager getFreeSpaceOnDeviceForUser:].cold.8
+ DREGetNVRAMAll.cold.1
+ _DRAnalyticsEventPerformDiagnosticsMode
+ _DRAnalyticsEventPerformEACS
+ _DRAnalyticsEventPerformNeRD
+ _DRAnalyticsEventPerformRecoveryMode
+ _DRAnalyticsKeyDuration
+ _DREGetNVRAMAll
+ _DRENVRAMValueToString
+ _IORegistryEntryCreateCFProperties
+ _OBJC_CLASS_$_NSMutableString
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$string
+ _objc_msgSend$stringValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x4
+ _objc_retain_x8
- GCC_except_table43
- _OUTLINED_FUNCTION_39
- _OUTLINED_FUNCTION_40
- _OUTLINED_FUNCTION_41
- __isOSVersionAtLeast.cold.1
- __isPlatformVersionAtLeast.cold.1
- __isPlatformVersionAtLeast.cold.2
- _objc_retain_x26
- _objc_retain_x27
- _objc_retain_x28
CStrings:
+ "%02x"
+ "%{public}s: Could not load NVRAM info (%d)"
+ "%{public}s: Failed to convert nvram value %{public}@ to string"
+ "%{public}s: Reading NVRAM var: %{public}@"
+ "((recoveryResultVal == DROverrideRecoveryResultNoOverride) || (recoveryResultVal == DROverrideRecoveryResultForceFailure) || (recoveryResultVal == DROverrideRecoveryResultRequireOSBootPhase) || (recoveryResultVal == DROverrideRecoveryResultRequirePostUserUnlockPhase) || (recoveryResultVal == DROverrideRecoveryResultRequireBothOSPhases))"
+ "/var/mnt/"
+ "/var/mnt//tmp-mount-XXXXXX"
+ "DREGetNVRAMAll"
+ "DRENVRAMValueToString"
+ "Duration"
+ "Unable to determine free space on update volume"
+ "appendFormat:"
+ "com.apple.DeviceRecovery.performDiagnosticsMode"
+ "com.apple.DeviceRecovery.performEACS"
+ "com.apple.DeviceRecovery.performNeRD"
+ "com.apple.DeviceRecovery.performRecoveryMode"
+ "string"
+ "stringValue"
- "%{public}s: Deleting NVRAM var: %{public}@"
- "((recoveryResultVal == DROverrideRecoveryResultNoOverride) || (recoveryResultVal == DROverrideBrainLoadResultForceFailure) || (recoveryResultVal == DROverrideRecoveryResultRequireOSBootPhase) || (recoveryResultVal == DROverrideRecoveryResultRequirePostUserUnlockPhase) || (recoveryResultVal == DROverrideRecoveryResultRequireBothOSPhases))"
- "/tmp/"
- "/tmp//tmp-mount-XXXXXX"

```
