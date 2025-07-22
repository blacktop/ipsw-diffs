## SoftwareUpdateUIMobileSettingsPlugin

> `/System/Library/PreferenceBundles/SoftwareUpdateUIMobileSettingsPlugin.bundle/SoftwareUpdateUIMobileSettingsPlugin`

```diff

-508.0.1.502.1
-  __TEXT.__text: 0x539f0
-  __TEXT.__auth_stubs: 0x1280
+508.0.30.0.0
+  __TEXT.__text: 0x4db28
+  __TEXT.__auth_stubs: 0x1240
   __TEXT.__objc_methlist: 0x44
-  __TEXT.__const: 0x1ca0
-  __TEXT.__constg_swiftt: 0x538
-  __TEXT.__swift5_typeref: 0x1a42
-  __TEXT.__swift5_fieldmd: 0x25c
-  __TEXT.__swift5_reflstr: 0x375
+  __TEXT.__const: 0x1cf0
+  __TEXT.__constg_swiftt: 0x56c
+  __TEXT.__swift5_typeref: 0x1b0a
+  __TEXT.__swift5_fieldmd: 0x250
+  __TEXT.__swift5_reflstr: 0x355
   __TEXT.__swift5_assocty: 0xf0
   __TEXT.__swift5_proto: 0x44
-  __TEXT.__swift5_types: 0x60
-  __TEXT.__swift5_capture: 0x21bc
-  __TEXT.__cstring: 0x105d
-  __TEXT.__objc_methname: 0x3a4
-  __TEXT.__oslogstring: 0xb5a
-  __TEXT.__swift_as_entry: 0x48
-  __TEXT.__swift_as_ret: 0x3c
+  __TEXT.__swift5_types: 0x64
+  __TEXT.__swift5_capture: 0x1e2c
+  __TEXT.__cstring: 0x108d
+  __TEXT.__objc_methname: 0x36b
+  __TEXT.__oslogstring: 0xbaa
+  __TEXT.__swift_as_entry: 0x38
+  __TEXT.__swift_as_ret: 0x30
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__unwind_info: 0x1768
-  __TEXT.__eh_frame: 0x548
-  __DATA_CONST.__auth_got: 0x940
-  __DATA_CONST.__got: 0x380
-  __DATA_CONST.__auth_ptr: 0x480
-  __DATA_CONST.__const: 0x57f8
+  __TEXT.__unwind_info: 0x1558
+  __TEXT.__eh_frame: 0x570
+  __DATA_CONST.__auth_got: 0x920
+  __DATA_CONST.__got: 0x390
+  __DATA_CONST.__auth_ptr: 0x488
+  __DATA_CONST.__const: 0x4f38
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x260
-  __DATA.__objc_selrefs: 0x138
+  __DATA.__objc_selrefs: 0x128
   __DATA.__objc_data: 0x108
   __DATA.__data: 0x860
   __DATA.__bss: 0xa10
   - /System/Library/Frameworks/Combine.framework/Combine
-  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/Settings.framework/Settings
   - /System/Library/PrivateFrameworks/SettingsCellularUI.framework/SettingsCellularUI
   - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SoftwareUpdateCore.framework/SoftwareUpdateCore
   - /System/Library/PrivateFrameworks/SoftwareUpdateCoreSupport.framework/SoftwareUpdateCoreSupport
   - /System/Library/PrivateFrameworks/SoftwareUpdateServices.framework/SoftwareUpdateServices

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 21A9363D-1496-3CD2-872E-B56BB153058E
-  Functions: 1996
-  Symbols:   108
-  CStrings:  160
+  UUID: AD49DC57-DDF7-3668-B49E-8790942280DA
+  Functions: 1833
+  Symbols:   107
+  CStrings:  153
 
Symbols:
- _OBJC_CLASS_$_NSTimer
CStrings:
+ "%s.%s: Failed to perform update action: %s"
+ "Atempting to perform update action \"%s\" to resolve the deep link action: %s"
+ "Attempted to perform an update action without a preferred descriptor."
+ "Automatically download and install OSName software updates and system files when this ProductFamilyName is connected to WLAN, charging, and locked. ProductFamilyName may reserve storage space to ensure updates can be installed."
+ "Automatically download and install OSName software updates and system files when this ProductFamilyName is connected to Wi-Fi, charging, and locked. ProductFamilyName may reserve storage space to ensure updates can be installed."
+ "Could not perform the deep link action %s as the descriptor\nis in an unknown state. Aborting the request."
+ "Could not perform the deep link action %s as the descriptor\nis not available to download or available to install. Aborting the request."
+ "System files improve ProductFamilyName functionality without changing the software version. ProductFamilyName may reserve storage space to ensure updates can be installed."
+ "handleUpdateAction(forContext:andDescriptor:withActionType:)"
- "%s.%s: Cache TTL (%s) < %s, refreshing scan results"
- "%s.%s: Failed to downloadAndSchedule: %@"
- "%s.%s: Refresh timer fired but cache is already updated."
- "%s.%s: Refresh timer fired. Checking for updates..."
- "%s.%s: Setting timer to reload cache in: %f seconds"
- "%s.%s: Unable to get the base chache TTL duration. Can't set a timer."
- "Automatically download and install OSName software updates and system files when this ProductFamilyName is connected to WLAN, charging, and locked."
- "Automatically download and install OSName software updates and system files when this ProductFamilyName is connected to Wi-Fi, charging, and locked."
- "System files improve ProductFamilyName functionality without changing the software version."
- "handleUpdateAction(forContext:withActionType:)"
- "invalidate"
- "scheduleTimerForScanResultsTTL(withTimeInterval:)"
- "scheduledTimerWithTimeInterval:repeats:block:"
- "startRefreshScanResultsCacheTimer(forExsitingTtl:)"
- "startToRefreshScanResultsCacheTimerForBaseTTL()"
- "v16@?0@\"NSTimer\"8"

```
