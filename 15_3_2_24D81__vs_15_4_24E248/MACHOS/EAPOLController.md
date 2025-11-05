## EAPOLController

> `/System/Library/SystemConfiguration/EAPOLController.bundle/Contents/MacOS/EAPOLController`

```diff

-364.0.0.0.0
-  __TEXT.__text: 0x588c
-  __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__const: 0x80
-  __TEXT.__cstring: 0x13a
-  __TEXT.__oslogstring: 0x64b
-  __TEXT.__unwind_info: 0x158
-  __DATA_CONST.__auth_got: 0x370
+365.0.0.0.0
+  __TEXT.__text: 0x65d8
+  __TEXT.__auth_stubs: 0x7e0
+  __TEXT.__const: 0x88
+  __TEXT.__cstring: 0x264
+  __TEXT.__oslogstring: 0x90b
+  __TEXT.__unwind_info: 0x150
+  __DATA_CONST.__auth_got: 0x3f0
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x4a8
-  __DATA_CONST.__cfstring: 0x180
+  __DATA_CONST.__const: 0x4e8
+  __DATA_CONST.__cfstring: 0x240
   __DATA.__data: 0xc
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
   - /System/Library/PrivateFrameworks/EAP8021X.framework/Versions/A/EAP8021X
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  UUID: 349A6E55-4C16-3EBC-9340-5C7EE0FBAAF8
-  Functions: 90
-  Symbols:   188
-  CStrings:  71
+  UUID: 789FF321-6BA5-388F-9954-88AE0354ED03
+  Functions: 94
+  Symbols:   205
+  CStrings:  104
 
Symbols:
+ _CFDataGetBytes
+ _CFDataGetLength
+ _CFDataGetTypeID
+ _CFDictionaryAddValue
+ _CFDictionaryCreateCopy
+ _CFNumberGetTypeID
+ _CFNumberGetValue
+ _CFStringCompare
+ _SCPreferencesCommitChanges
+ _SCPreferencesCreateWithOptions
+ _SCPreferencesGetValue
+ _SCPreferencesRemoveValue
+ _SCPreferencesSetValue
+ __NSConcreteGlobalBlock
+ _dispatch_once
+ _os_boot_mode_query
+ _sysctlbyname
CStrings:
+ "AuthenticatorMAC"
+ "BootUUID"
+ "EAPOLController: %s is no longer configured, stopping to monitor"
+ "EAPOLController: %s: SCPreferencesCreateWithOptions() failed for [%@]"
+ "EAPOLController: %s: added [%@] in auto-detect status with info %@"
+ "EAPOLController: %s: auto-detect status already has interface info for [%@]"
+ "EAPOLController: %s: boot mode unavailable"
+ "EAPOLController: %s: boot mode: %s"
+ "EAPOLController: %s: boot uuids don't match"
+ "EAPOLController: %s: no BootUUID found"
+ "EAPOLController: %s: no current boot uuid found"
+ "EAPOLController: %s: no interfaces found"
+ "EAPOLController: %s: sysctlbyname failed to read kern.bootuuid %s (%d)"
+ "EAPOLController: adding [%@] to auto-detect status"
+ "EAPOLController: auto detected interfaces: %@"
+ "EAPOLController: no auto detected interfaces found"
+ "Identifier"
+ "Interfaces"
+ "add_interface_to_auto_detect_status"
+ "cleanup_auto_detect_status"
+ "com.apple.network.eapol.auto-detect.plist"
+ "copy_interfaces_from_auto_detect_status"
+ "fvunlock"
+ "get_boot_uuid_block_invoke"
+ "is_fvunlock_current_boot_mode"
+ "kern.bootuuid"
+ "use-preboot-volume"
+ "v8@?0"
- "EAPOLController: monitor %s recv failed %s"

```
