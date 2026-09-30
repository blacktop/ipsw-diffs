## DeviceRecovery

> `/System/Library/PrivateFrameworks/DeviceRecovery.framework/DeviceRecovery`

```diff

-95.0.0.0.1
-  __TEXT.__text: 0x1ed80
+96.0.0.0.1
+  __TEXT.__text: 0x1f4dc
   __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_methlist: 0x5c0
+  __TEXT.__objc_methlist: 0x5dc
   __TEXT.__const: 0x188
   __TEXT.__gcc_except_tab: 0x2d4
-  __TEXT.__cstring: 0x3a70
-  __TEXT.__oslogstring: 0xc6a
-  __TEXT.__unwind_info: 0x590
+  __TEXT.__cstring: 0x3b1b
+  __TEXT.__oslogstring: 0xcf4
+  __TEXT.__unwind_info: 0x5a0
   __TEXT.__objc_classname: 0xa2
-  __TEXT.__objc_methname: 0xfe7
+  __TEXT.__objc_methname: 0x103f
   __TEXT.__objc_methtype: 0x28a
-  __TEXT.__objc_stubs: 0x9e0
+  __TEXT.__objc_stubs: 0xa00
   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__const: 0x4b8
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x470
+  __DATA_CONST.__objc_selrefs: 0x480
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x18
   __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0x180
   __AUTH_CONST.__cfstring: 0xea0
-  __AUTH_CONST.__objc_const: 0x778
+  __AUTH_CONST.__objc_const: 0x780
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0x5c

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 34691EBB-2924-3A7E-BA04-5D02A90F162E
-  Functions: 727
-  Symbols:   1625
-  CStrings:  823
+  UUID: 9BE89C9D-83B2-33B7-82C9-AEFBF2B9C4C3
+  Functions: 735
+  Symbols:   1642
+  CStrings:  829
 
Symbols:
+ -[DeviceRecoveryController loadAccessibilitySettingsToDefaultsWithCompletion:]
+ -[DeviceRecoveryController loadAccessibilitySettingsToDefaultsWithCompletion:].cold.1
+ -[DeviceRecoveryController loadAccessibilitySettingsToDefaultsWithCompletion:].cold.2
+ -[DeviceRecoveryController loadAccessibilitySettingsToDefaultsWithCompletion:].cold.3
+ GCC_except_table106
+ GCC_except_table107
+ GCC_except_table108
+ GCC_except_table82
+ ___32-[DeviceRecoveryController init]_block_invoke.30
+ ___32-[DeviceRecoveryController init]_block_invoke.30.cold.1
+ ___32-[DeviceRecoveryController init]_block_invoke.35
+ ___32-[DeviceRecoveryController init]_block_invoke.35.cold.1
+ ___32-[DeviceRecoveryController init]_block_invoke.35.cold.2
+ ___32-[DeviceRecoveryController init]_block_invoke.35.cold.3
+ ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.53
+ ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.53.cold.1
+ ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.53.cold.2
+ ___52-[DeviceRecoveryController disableRecoveryAutoBoot:]_block_invoke.84
+ ___52-[DeviceRecoveryController disableRecoveryAutoBoot:]_block_invoke.84.cold.1
+ ___54-[DeviceRecoveryController recoverDeviceFromBootedOS:]_block_invoke.83
+ ___54-[DeviceRecoveryController recoverDeviceFromBootedOS:]_block_invoke.83.cold.1
+ ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.81
+ ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.81.cold.1
+ ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.81.cold.2
+ ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.80
+ ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.80.cold.1
+ ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.80.cold.2
+ ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.52
+ ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.52.cold.1
+ ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.52.cold.2
+ ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.77
+ ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.77.cold.1
+ ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.77.cold.2
+ ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.79
+ ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.79.cold.1
+ ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.79.cold.2
+ ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.78
+ ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.78.cold.1
+ ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.78.cold.2
+ ___77-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke.82
+ ___77-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke.82.cold.1
+ ___77-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke.82.cold.2
+ ___78-[DeviceRecoveryController loadAccessibilitySettingsToDefaultsWithCompletion:]_block_invoke
+ ___78-[DeviceRecoveryController loadAccessibilitySettingsToDefaultsWithCompletion:]_block_invoke.85
+ ___78-[DeviceRecoveryController loadAccessibilitySettingsToDefaultsWithCompletion:]_block_invoke.85.cold.1
+ ___78-[DeviceRecoveryController loadAccessibilitySettingsToDefaultsWithCompletion:]_block_invoke.cold.1
+ ___block_literal_global.28
+ _objc_msgSend$loadAccessibilitySettingsToDefaults:
- GCC_except_table103
- GCC_except_table104
- GCC_except_table105
- GCC_except_table79
- ___32-[DeviceRecoveryController init]_block_invoke.28
- ___32-[DeviceRecoveryController init]_block_invoke.29.cold.1
- ___32-[DeviceRecoveryController init]_block_invoke.34
- ___32-[DeviceRecoveryController init]_block_invoke.34.cold.1
- ___32-[DeviceRecoveryController init]_block_invoke.34.cold.2
- ___32-[DeviceRecoveryController init]_block_invoke.34.cold.3
- ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.52
- ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.52.cold.1
- ___42-[DeviceRecoveryController resetRecovery:]_block_invoke.52.cold.2
- ___52-[DeviceRecoveryController disableRecoveryAutoBoot:]_block_invoke.83
- ___52-[DeviceRecoveryController disableRecoveryAutoBoot:]_block_invoke.83.cold.1
- ___54-[DeviceRecoveryController recoverDeviceFromBootedOS:]_block_invoke.82
- ___54-[DeviceRecoveryController recoverDeviceFromBootedOS:]_block_invoke.82.cold.1
- ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.80
- ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.80.cold.1
- ___56-[DeviceRecoveryController recoverDeviceWithCompletion:]_block_invoke.80.cold.2
- ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.79
- ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.79.cold.1
- ___56-[DeviceRecoveryController scanForIssuesWithCompletion:]_block_invoke.79.cold.2
- ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.51
- ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.51.cold.1
- ___57-[DeviceRecoveryController enableTestModeWithCompletion:]_block_invoke.51.cold.2
- ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.75
- ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.75.cold.1
- ___57-[DeviceRecoveryController userAuthenticated:completion:]_block_invoke.76.cold.2
- ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.78
- ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.78.cold.1
- ___60-[DeviceRecoveryController loadRecoveryBrainWithCompletion:]_block_invoke.78.cold.2
- ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.77
- ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.77.cold.1
- ___68-[DeviceRecoveryController reportNetworkAvailabilityWithCompletion:]_block_invoke.77.cold.2
- ___77-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke.81
- ___77-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke.81.cold.1
- ___77-[DeviceRecoveryController _shutdownWithCompletion:andReboot:andSetNeRDBoot:]_block_invoke.81.cold.2
- ___block_literal_global.32
CStrings:
+ "%{public}s: Load accessibility settings to defaults failed: %{public}@"
+ "%{public}s: Successfully loaded accessibility settings to defaults"
+ "-[DeviceRecoveryController loadAccessibilitySettingsToDefaultsWithCompletion:]"
+ "-[DeviceRecoveryController loadAccessibilitySettingsToDefaultsWithCompletion:]_block_invoke"
+ "loadAccessibilitySettingsToDefaults:"
+ "loadAccessibilitySettingsToDefaultsWithCompletion:"

```
