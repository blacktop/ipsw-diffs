## deviceaccessd

> `/usr/libexec/deviceaccessd`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2701.6.0.0.0
-  __TEXT.__text: 0x93278
-  __TEXT.__auth_stubs: 0x2280
-  __TEXT.__objc_stubs: 0x83a0
-  __TEXT.__objc_methlist: 0x2810
-  __TEXT.__const: 0x1c88
-  __TEXT.__cstring: 0x16154
+2702.5.0.0.0
+  __TEXT.__text: 0x9567c
+  __TEXT.__auth_stubs: 0x22a0
+  __TEXT.__objc_stubs: 0x85c0
+  __TEXT.__objc_methlist: 0x28a0
+  __TEXT.__const: 0x1d68
+  __TEXT.__cstring: 0x16aa4
   __TEXT.__objc_classname: 0x3f5
-  __TEXT.__objc_methtype: 0x1b9a
-  __TEXT.__gcc_except_tab: 0x432c
-  __TEXT.__objc_methname: 0xa8a4
+  __TEXT.__objc_methtype: 0x1bda
+  __TEXT.__gcc_except_tab: 0x4610
+  __TEXT.__objc_methname: 0xab1f
   __TEXT.__dlopen_cstrs: 0x62
   __TEXT.__swift5_typeref: 0x9ee
   __TEXT.__swift5_fieldmd: 0x490

   __TEXT.__swift_as_ret: 0x24
   __TEXT.__swift_as_cont: 0x3c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x2460
+  __TEXT.__unwind_info: 0x24a8
   __TEXT.__eh_frame: 0x10a8
   __DATA_CONST.__const: 0x29c0
-  __DATA_CONST.__cfstring: 0x2240
+  __DATA_CONST.__cfstring: 0x22a0
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x48
-  __DATA_CONST.__objc_arraydata: 0x80
+  __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_intobj: 0xc0
-  __DATA_CONST.__auth_got: 0x1150
-  __DATA_CONST.__got: 0x8d0
+  __DATA_CONST.__auth_got: 0x1160
+  __DATA_CONST.__got: 0x8d8
   __DATA_CONST.__auth_ptr: 0x2b8
-  __DATA.__objc_const: 0x3698
-  __DATA.__objc_selrefs: 0x2868
-  __DATA.__objc_ivar: 0x2f8
+  __DATA.__objc_const: 0x3728
+  __DATA.__objc_selrefs: 0x28e8
+  __DATA.__objc_ivar: 0x308
   __DATA.__objc_data: 0x8c0
   __DATA.__data: 0x13e8
   __DATA.__common: 0x38

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2554
-  Symbols:   915
-  CStrings:  4079
+  Functions: 2573
+  Symbols:   918
+  CStrings:  4157
 
Symbols:
+ _DAExtensionCapabilityFlagsEligible
+ _DAExtensionCapabilityFlagsToTCCStrings
+ _OBJC_CLASS_$_DAExtensionEventEligibility
CStrings:
+ "### Device's app info not found: %@, %@"
+ "### GetDevices: app access entry for '%@' on %@ unusable (appInfo %@, bundleID %@): %@"
+ "### GetDevices: devices directory unreadable at %@: %@"
+ "### GetEligibleCapabilityFlags failed: %@, from %@"
+ "### RequestFeatureAuthorization create reply failed"
+ "### RequestFeatureAuthorization failed: %@ from %@"
+ "'%@' does not implement %@"
+ "'%@' has no access to device '%@': %@"
+ "'%@' has no accessory '%@' to enroll"
+ "'%@' may not enroll '%@'"
+ "+[DAExtensionCoordinator extensionIdentityForType:bundleID:capabilityFlags:error:]"
+ "+[DAExtensionCoordinator extensionIdentityForType:bundleID:capabilityFlags:error:]_block_invoke"
+ "+[DAExtensionCoordinator validateCapabilityID:capabilityFlag:error:]_block_invoke"
+ "-[DADaemonServer _activate]_block_invoke_11"
+ "-[DADaemonServer _activate]_block_invoke_5"
+ "-[DADaemonServer _eligibilityDomainChanged]"
+ "-[DADaemonServer _handleExtensionSessionCommandRuntime:appID:error:]"
+ "-[DADaemonServer _handleExtensionSessionCommandRuntime:appID:error:]_block_invoke"
+ "-[DADaemonServer extensionSessionExecuteCommand:appID:error:]_block_invoke"
+ "-[DADaemonServer getDevicesWithFlags:appID:error:]_block_invoke_2"
+ "-[DADaemonXPCConnection _xpcGetEligibleCapabilityFlags:]"
+ "-[DADaemonXPCConnection _xpcGetEligibleCapabilityFlags:]_block_invoke"
+ "-[DADaemonXPCConnection _xpcRequestFeatureAuthorization:]"
+ "-[DADaemonXPCConnection _xpcRequestFeatureAuthorization:]_block_invoke"
+ "-[DAExtensionCoordinator _activateExtension:capabilityFlags:assertedFlags:]"
+ "-[DAExtensionCoordinator _extensionEnsureStopped:reason:]"
+ "-[DAExtensionCoordinator _recomputeCapabilityFlags]"
+ "-[DAExtensionCoordinator _updateAssertedFlags:]"
+ "<all>"
+ "@48@0:8q16@24^Q32^@40"
+ "AccessoryTransportExtension"
+ "Activate: %@, AccessLevel %d, AppID %@, ParentAppID %@"
+ "AsrtFl %@"
+ "AssertedFlags: %@ -> %@"
+ "DataDeliverySuccess: %@ untracked, deleting anyway"
+ "Device '%@' has no authorized feature"
+ "Device services changed: %@"
+ "ElFl %@"
+ "ElgF"
+ "Eligibility changed: %@, ElFl %@"
+ "EligibleFlags: %@ -> %@"
+ "EnsureStopped: %@, Reason %@"
+ "ExecuteCommand: %@, from %@"
+ "Extension should run %s: Type %@, Connection %@, KED %s, CapFl %@, EnFl %@, AsrtFl %@, ElFl %@"
+ "GetDevices: %lu device record(s) on disk, %lu with app access, %lu with services"
+ "GetDevices: %lu of %lu device record(s) matched flags %@ for '%@'"
+ "GetDevices: DvF %@, AppID '%@'"
+ "GetDevices: app access for '%@' holds %lu device(s) %@, from %@"
+ "GetDevices: no accessory services directory at %@: %@"
+ "GetDevices: services for %@ hold no '%@' dictionary"
+ "GetDevices: services for %@ unreadable at %@"
+ "GetDevices: skipping %@, flags %@ do not match query %@"
+ "GetEligibleCapabilityFlags: %@ -> %@, from %@"
+ "Internal build with prefs TestExtensionBundleID '%@', overriding access level for %@: %d -> %d"
+ "NULL"
+ "No TCC service for %@"
+ "No device identifier"
+ "RequestFeatureAuthorization: %@ for '%@' on %@, level %tu, from %@"
+ "Resolved capabilities for '%@': %@"
+ "RqFA"
+ "Runnable %@, resuming TransportBluetooth so it can open a feature session: %@"
+ "Skipped invalid capability ID: %@"
+ "T@\"NSString\",R,C,N,V_prefTestExtensionBundleID"
+ "_activateExtension:capabilityFlags:assertedFlags:"
+ "_assertedFlags"
+ "_eligibilityDomainChanged"
+ "_eligibilityDomainChangedNotifyToken"
+ "_eligibleCapabilityFlags"
+ "_eligibleFlags"
+ "_extensionEnsureStopped:reason:"
+ "_handleExtensionSessionCommandRuntime:appID:error:"
+ "_recomputeCapabilityFlags"
+ "_stopReasonForCapabilityFlags:"
+ "_updateAssertedFlags:"
+ "_updateAssertedFlagsForDaemonSession:"
+ "_xpcGetEligibleCapabilityFlags:"
+ "_xpcRequestFeatureAuthorization:"
+ "auL"
+ "clientPID"
+ "com.apple.os-eligibility-domain.change"
+ "eligibleFlags"
+ "exElF"
+ "extensionIdentityForType:bundleID:capabilityFlags:error:"
+ "extensionSessionExecuteCommand:appID:error:"
+ "global session requires private entitlement: Session AppID '%@', AppID '%@', ParentAppID '%@'"
+ "initWithCapacity:"
+ "invalid feature requested: %@"
+ "isListeningForEvent:"
+ "missing capability ID"
+ "missing out flag"
+ "not eligible: %@"
+ "not permitted to activate session for '%@': AppID '%@', ParentAppID '%@'"
+ "not permitted to command: no app identity, AppID '%@', ParentAppID '%@'"
+ "only one capability may be requested at a time, received %@"
+ "prefTestExtensionBundleID"
+ "runnableFlags"
+ "setEligibleFlags:"
+ "setEnrolledFlags:assertedFlags:"
+ "updateAssertedFlags:"
+ "v40@0:8@16@24^@32"
+ "v40@0:8@16Q24Q32"
+ "validateCapabilityID:capabilityFlag:error:"
- "-[DADaemonServer _activate]_block_invoke_3"
- "-[DADaemonServer _activate]_block_invoke_9"
- "-[DADaemonServer _handleExtensionSessionCommandRuntime:error:]"
- "-[DADaemonServer _handleExtensionSessionCommandRuntime:error:]_block_invoke"
- "-[DADaemonServer extensionSessionExecuteCommand:error:]_block_invoke"
- "-[DAExtensionCoordinator _activateExtension:capabilityFlags:]"
- "-[DAExtensionCoordinator _extensionEnsureStopped:]"
- "-[DAExtensionCoordinator _extensionIdentityForType:]"
- "-[DAExtensionCoordinator _extensionIdentityForType:]_block_invoke"
- "-[DAExtensionCoordinator _validateCapabilityID:capabilityFlag:error:]_block_invoke"
- "EnsureStopped: %@"
- "ExecuteCommand: %@"
- "Extension should run %s: Type %@, Connection %@, KED %s, CapFl %@, EnFl %@"
- "Skip event reporting, configuration is not listening for data events %@: %@"
- "Skip event reporting, configuration is not listening for lifecycle events %@: %@"
- "Skip event reporting, configuration is not listening for this capability %@: %@"
- "_activateExtension:capabilityFlags:"
- "_extensionEnsureStopped:"
- "_handleExtensionSessionCommandRuntime:error:"
- "_validateCapabilityID:capabilityFlag:error:"
- "extensionSessionExecuteCommand:error:"
- "missing capability ID: %@"
- "missing out flag: %@"
- "setEnrolledFlags:"
```
