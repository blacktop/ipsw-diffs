## remotepairingd

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/RemotePairing.framework/Versions/A/XPCServices/remotepairingd.xpc/Contents/MacOS/remotepairingd`

```diff

-199.100.20.0.0
-  __TEXT.__text: 0x7a65c
-  __TEXT.__auth_stubs: 0x3270
+199.120.5.0.0
+  __TEXT.__text: 0x7bb8c
+  __TEXT.__auth_stubs: 0x32b0
   __TEXT.__objc_stubs: 0x80
   __TEXT.__objc_methlist: 0x1b4
   __TEXT.__const: 0x1608
-  __TEXT.__oslogstring: 0x499f
+  __TEXT.__oslogstring: 0x4f2f
   __TEXT.__cstring: 0x53ca
   __TEXT.__objc_methname: 0x534
-  __TEXT.__swift5_typeref: 0x153c
+  __TEXT.__swift5_typeref: 0x1542
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x1618
+  __TEXT.__constg_swiftt: 0x1620
   __TEXT.__swift5_builtin: 0xb4
   __TEXT.__swift5_reflstr: 0xe59
   __TEXT.__swift5_fieldmd: 0xb14
   __TEXT.__swift5_assocty: 0xc0
-  __TEXT.__swift5_capture: 0xbc8
+  __TEXT.__swift5_capture: 0xc10
   __TEXT.__swift5_proto: 0xc8
   __TEXT.__swift5_types: 0xa0
   __TEXT.__swift5_mpenum: 0x2c
   __TEXT.__swift5_protos: 0xc
-  __TEXT.__unwind_info: 0x12c0
+  __TEXT.__unwind_info: 0x12d0
   __TEXT.__eh_frame: 0x1288
-  __DATA_CONST.__auth_got: 0x1940
-  __DATA_CONST.__got: 0x770
-  __DATA_CONST.__auth_ptr: 0x660
-  __DATA_CONST.__const: 0x1fb0
+  __DATA_CONST.__auth_got: 0x1960
+  __DATA_CONST.__got: 0x788
+  __DATA_CONST.__auth_ptr: 0x760
+  __DATA_CONST.__const: 0x2050
   __DATA_CONST.__cfstring: 0x580
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x28

   __DATA.__objc_protorefs: 0x28
   __DATA.__objc_classrefs: 0x88
   __DATA.__objc_data: 0x3f0
-  __DATA.__data: 0x2c59
+  __DATA.__data: 0x2c69
   __DATA.__s_async_hook: 0x190
   __DATA.__swift56_hooks: 0xb0
   __DATA.__common: 0x148

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2460
+  Functions: 2477
   Symbols:   368
-  CStrings:  822
+  CStrings:  829
 
CStrings:
+ "%{public}s Defaults.hostPairingViaLockdownPreference prefers performing pairing unconditionally through lockdown, but device does not support it. Downgrading preference from createNewPairingsThroughLockdown->upgradeExistingPairingsOnly"
+ "%{public}s configuring OOB pairing handler on connection. Lockdown pairings will be used for interaction-free pairing on the device but if no lockdown pairing exists we will do PairSetup through RemotePairing control channel."
+ "%{public}s configuring OOB pairing handler on connection. Pairing will be performed unconditionally through MobileDevice."
+ "%{public}s not configuring OOB pairing handler on connection (Defaults.hostPairingViaLockdownPreference=%s, peerSupportsPairingFirstThroughMobileDevice=%{bool}d, rsdDeviceForChannel=%{public}s, deviceSupportsLockdown=%{public}s"
+ "%{public}s: Failed to validate lockdown pairing over RSD for out-of-band pairing: %s. Declining ownership of pairing attempt. Pairing will proceed through standard control channel path"
+ "%{public}s: Proactive lockdown pairing upgrade completed with result %{public}s but connection has since been invalidated with reason: %{public}s. Discarding channel and will not proceed to create a device entry for this channel"
+ "%{public}s: Proactive validation of lockdown pairing record completed with result %{public}s but connection has since been invalidated with reason: %{public}s. Discarding channel and will not proceed with pairing upgrade"
+ "%{public}s: Successfully validating lockdown pairing over RSD for out-of-band pairing (automation=%{bool}d). Accepting ownership of pairing attempt"
+ "%{public}s: Validating lockdown pairing over RSD to perform interaction-free pairing if available."
- "%{public}s configuring OOB pairing handler on connection. Pairing will be performed through MobileDevice."
- "%{public}s not configuring OOB pairing handler on connection (Defaults.hostPreferPairingViaLockdown=%{bool}d, peerSupportsPairingFirstThroughMobileDevice=%{bool}d, rsdDeviceForChannel=%{public}s, deviceSupportsLockdown=%{public}s"

```
