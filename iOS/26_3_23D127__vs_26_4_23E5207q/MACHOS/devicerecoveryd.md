## devicerecoveryd

> `/System/Library/PrivateFrameworks/DeviceRecovery.framework/Support/devicerecoveryd`

```diff

-103.80.1.0.1
-  __TEXT.__text: 0x21cac
-  __TEXT.__auth_stubs: 0xe80
+107.100.11.0.0
+  __TEXT.__text: 0x1fb90
+  __TEXT.__auth_stubs: 0xe30
   __TEXT.__objc_stubs: 0x21c0
   __TEXT.__objc_methlist: 0xbbc
-  __TEXT.__cstring: 0x68ff
+  __TEXT.__cstring: 0x69d2
   __TEXT.__const: 0x58
   __TEXT.__objc_methname: 0x23f1
-  __TEXT.__oslogstring: 0x32b6
+  __TEXT.__oslogstring: 0x3215
   __TEXT.__objc_classname: 0x125
   __TEXT.__objc_methtype: 0x541
-  __TEXT.__gcc_except_tab: 0x71c
-  __TEXT.__unwind_info: 0x638
-  __DATA_CONST.__auth_got: 0x750
+  __TEXT.__gcc_except_tab: 0x6fc
+  __TEXT.__unwind_info: 0x680
+  __DATA_CONST.__auth_got: 0x728
   __DATA_CONST.__got: 0x1c8
   __DATA_CONST.__auth_ptr: 0x10
   __DATA_CONST.__const: 0xc00
-  __DATA_CONST.__cfstring: 0x2460
+  __DATA_CONST.__cfstring: 0x2360
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA_CONST.__objc_arraydata: 0x58
-  __DATA_CONST.__objc_arrayobj: 0x30
+  __DATA_CONST.__objc_arraydata: 0x18
+  __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x13c8
   __DATA.__objc_selrefs: 0xa68
   __DATA.__objc_ivar: 0xb8

   - /System/Library/PrivateFrameworks/UserManagementLayout.framework/UserManagementLayout
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3B72DA89-13D2-3D65-A716-3706AAB402DC
-  Functions: 650
-  Symbols:   302
-  CStrings:  1760
+  UUID: 9C60EE76-0BA3-3FA5-94D2-E08D74A323D0
+  Functions: 708
+  Symbols:   297
+  CStrings:  1743
 
Symbols:
+ _CFPreferencesSetMultiple
+ _objc_retain_x25
+ _objc_retain_x27
- _CFPreferencesSetValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x26
- _objc_retain_x3
- _objc_retain_x9
CStrings:
+ "%{public}s: Completed accessibility restoration with errors"
+ "%{public}s: Failed to synchronize preferences for domain: %@"
+ "%{public}s: Found %lu accessibility domains to restore"
+ "%{public}s: Invalid or empty preferences for domain: %@"
+ "%{public}s: No accessibility preferences were restored"
+ "%{public}s: Successfully restored %lu accessibility preferences' keys"
+ "/Library/Caches/com.apple.xbs/B00B08DE-3C06-4FE4-B2FF-E260184E7410/TemporaryDirectory.PXiZc7/Sources/DeviceRecovery/Common/DeviceRecoveryEnvironmentWorker.m"
+ "/Library/Caches/com.apple.xbs/B00B08DE-3C06-4FE4-B2FF-E260184E7410/TemporaryDirectory.PXiZc7/Sources/DeviceRecovery/Common/DeviceRecoveryHelpers.m"
+ "/Library/Caches/com.apple.xbs/B00B08DE-3C06-4FE4-B2FF-E260184E7410/TemporaryDirectory.PXiZc7/Sources/DeviceRecovery/Common/DeviceRecoveryOverrides.m"
+ "/Library/Caches/com.apple.xbs/B00B08DE-3C06-4FE4-B2FF-E260184E7410/TemporaryDirectory.PXiZc7/Sources/DeviceRecovery/Daemon/DeviceRecoveryOverrideService.m"
+ "/Library/Caches/com.apple.xbs/B00B08DE-3C06-4FE4-B2FF-E260184E7410/TemporaryDirectory.PXiZc7/Sources/DeviceRecovery/Daemon/DeviceRecoveryService.m"
+ "/Library/Caches/com.apple.xbs/B00B08DE-3C06-4FE4-B2FF-E260184E7410/TemporaryDirectory.PXiZc7/Sources/DeviceRecovery/Daemon/devicerecoveryd_main.m"
+ "/Library/Caches/com.apple.xbs/B00B08DE-3C06-4FE4-B2FF-E260184E7410/TemporaryDirectory.PXiZc7/Sources/DeviceRecovery/DeviceRecovery_Framework/DeviceRecoveryOverrideClient.m"
+ "22:51:18"
+ "Feb  9 2026"
- "%{public}s: Completed accessibility restoration with some errors (%lu domains restored)"
- "%{public}s: Domain %@ not found in stashed preferences, skipping"
- "%{public}s: Found %lu total stashed domains, will selectively restore from %lu known domains"
- "%{public}s: Invalid preferences format for domain: %@"
- "%{public}s: No known accessibility domains were found in stashed preferences"
- "%{public}s: Successfully restored %lu accessibility domains from stash"
- "%{public}s: Warning: Failed to synchronize preferences for domain: %@"
- "/Library/Caches/com.apple.xbs/Sources/DeviceRecovery/Common/DeviceRecoveryEnvironmentWorker.m"
- "/Library/Caches/com.apple.xbs/Sources/DeviceRecovery/Common/DeviceRecoveryHelpers.m"
- "/Library/Caches/com.apple.xbs/Sources/DeviceRecovery/Common/DeviceRecoveryOverrides.m"
- "/Library/Caches/com.apple.xbs/Sources/DeviceRecovery/Daemon/DeviceRecoveryOverrideService.m"
- "/Library/Caches/com.apple.xbs/Sources/DeviceRecovery/Daemon/DeviceRecoveryService.m"
- "/Library/Caches/com.apple.xbs/Sources/DeviceRecovery/Daemon/devicerecoveryd_main.m"
- "/Library/Caches/com.apple.xbs/Sources/DeviceRecovery/DeviceRecovery_Framework/DeviceRecoveryOverrideClient.m"
- "20:46:42"
- "Jan 28 2026"
- "com.apple.Accessibility"
- "com.apple.Accessibility.SwitchControl"
- "com.apple.Accessibility.TouchAccommodations"
- "com.apple.AssistiveTouch"
- "com.apple.SpeakSelection"
- "com.apple.VoiceOverTouch"
- "com.apple.ZoomTouch"
- "com.apple.mediaaccessibility"

```
