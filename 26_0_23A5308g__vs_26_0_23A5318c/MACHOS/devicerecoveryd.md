## devicerecoveryd

> `/System/Library/PrivateFrameworks/DeviceRecovery.framework/Support/devicerecoveryd`

```diff

-95.0.0.0.1
-  __TEXT.__text: 0x1fb5c
-  __TEXT.__auth_stubs: 0xe10
-  __TEXT.__objc_stubs: 0x2080
-  __TEXT.__objc_methlist: 0xb64
-  __TEXT.__cstring: 0x6481
+96.0.0.0.1
+  __TEXT.__text: 0x204b4
+  __TEXT.__auth_stubs: 0xe40
+  __TEXT.__objc_stubs: 0x20a0
+  __TEXT.__objc_methlist: 0xb8c
+  __TEXT.__cstring: 0x662a
   __TEXT.__const: 0x58
-  __TEXT.__objc_methname: 0x226e
-  __TEXT.__oslogstring: 0x2c90
+  __TEXT.__objc_methname: 0x22b8
+  __TEXT.__oslogstring: 0x2fbf
   __TEXT.__objc_classname: 0x125
   __TEXT.__objc_methtype: 0x4d7
   __TEXT.__gcc_except_tab: 0x6f0
-  __TEXT.__unwind_info: 0x600
-  __DATA_CONST.__auth_got: 0x718
-  __DATA_CONST.__got: 0x178
+  __TEXT.__unwind_info: 0x608
+  __DATA_CONST.__auth_got: 0x730
+  __DATA_CONST.__got: 0x180
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0xba8
-  __DATA_CONST.__cfstring: 0x2140
+  __DATA_CONST.__cfstring: 0x22a0
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0x1368
-  __DATA.__objc_selrefs: 0xa00
+  __DATA_CONST.__objc_arraydata: 0x40
+  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA.__objc_const: 0x1370
+  __DATA.__objc_selrefs: 0xa10
   __DATA.__objc_ivar: 0xb0
   __DATA.__objc_data: 0x1e0
   __DATA.__data: 0x220

   - /System/Library/PrivateFrameworks/UserManagementLayout.framework/UserManagementLayout
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 09BB74BC-3916-3F1D-B146-C1C97FBE4549
-  Functions: 622
-  Symbols:   285
-  CStrings:  1651
+  UUID: 0A1F13E4-5C11-3613-BB91-A7A0135C382E
+  Functions: 625
+  Symbols:   290
+  CStrings:  1688
 
Symbols:
+ _CFPreferencesSetValue
+ _CFPreferencesSynchronize
+ _MSUCopyStashedAccessibilityPrefs
+ _OBJC_CLASS_$_NSConstantArray
+ _kCFPreferencesAnyHost
CStrings:
+ "%{public}s: Attempting to restore accessibility settings from stash"
+ "%{public}s: Completed accessibility restoration with some errors (%lu domains restored)"
+ "%{public}s: Domain %@ not found in stashed preferences, skipping"
+ "%{public}s: Failed to mount update volume: %d"
+ "%{public}s: Found %lu total stashed domains, will selectively restore from %lu known domains"
+ "%{public}s: Invalid preferences format for domain: %@"
+ "%{public}s: Loading accessibility settings to defaults"
+ "%{public}s: No accessibility domains found in stashed preferences"
+ "%{public}s: No known accessibility domains were found in stashed preferences"
+ "%{public}s: No stashed accessibility preferences found"
+ "%{public}s: Restoring %lu preferences for domain: %@"
+ "%{public}s: Successfully restored %lu accessibility domains from stash"
+ "%{public}s: Warning: Failed to synchronize preferences for domain: %@"
+ "-[DeviceRecoveryService _loadAccessibilitySettingsToDefaults]"
+ "-[DeviceRecoveryService loadAccessibilitySettingsToDefaults:]"
+ "23:35:17"
+ "AccessibilityDomains"
+ "Aug  6 2025"
+ "Failed to load accessibility settings to defaults"
+ "_loadAccessibilitySettingsToDefaults"
+ "com.apple.Accessibility"
+ "com.apple.Accessibility.SwitchControl"
+ "com.apple.Accessibility.TouchAccommodations"
+ "com.apple.AssistiveTouch"
+ "com.apple.SpeakSelection"
+ "com.apple.VoiceOverTouch"
+ "com.apple.ZoomTouch"
+ "com.apple.mediaaccessibility"
+ "loadAccessibilitySettingsToDefaults:"
- "%{public}s: failed to mount update volume: %d"
- "21:20:44"
- "Jul 31 2025"

```
