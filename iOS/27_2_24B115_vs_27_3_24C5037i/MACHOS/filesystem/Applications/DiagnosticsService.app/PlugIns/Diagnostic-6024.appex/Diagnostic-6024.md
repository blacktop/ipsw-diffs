## Diagnostic-6024

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-6024.appex/Diagnostic-6024`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__objc_methname`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1374.42.1.0.0
+1374.60.20.0.0
   __TEXT.__text: 0x38d8
   __TEXT.__auth_stubs: 0x600
   __TEXT.__objc_stubs: 0x160
   __TEXT.__objc_methlist: 0x38
-  __TEXT.__const: 0x2ec
-  __TEXT.__objc_classname: 0xcc
+  __TEXT.__const: 0x2d4
+  __TEXT.__objc_classname: 0xb4
   __TEXT.__objc_methname: 0x1ab
-  __TEXT.__objc_methtype: 0x49
+  __TEXT.__objc_methtype: 0x47
   __TEXT.__constg_swiftt: 0x200
-  __TEXT.__swift5_typeref: 0x15b
-  __TEXT.__swift5_reflstr: 0xdc
+  __TEXT.__swift5_typeref: 0x157
+  __TEXT.__swift5_reflstr: 0xc7
   __TEXT.__swift5_fieldmd: 0x128
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__cstring: 0x146
+  __TEXT.__cstring: 0x133
   __TEXT.__swift5_capture: 0x158
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x14
Symbols:
+ _OBJC_CLASS_$_CMMagicPoseManager
- _OBJC_CLASS_$_CMDeviceStateManager
CStrings:
+ "CMMagicPoseManager not available on this device"
+ "MagicPose changed — hingeState: %ld"
+ "MagicPose update error: %{public}@"
+ "MagicPoseController"
+ "Tearing down MagicPose controller"
+ "Timed out waiting for MagicPose update"
+ "_TtC15Diagnostic_6024P33_F0FCA500233238AE6772E0701C1B22AC10FinishOnce"
+ "_TtC15Diagnostic_6024P33_F0FCA500233238AE6772E0701C1B22AC16MagicPoseMonitor"
+ "hingeState"
+ "v24@?0@\"CMMagicPoseEvent\"8@\"NSError\"16"
- "CMDeviceStateManager not available on this device"
- "Device state changed — propertyB: %ld"
- "Device state update error: %{public}@"
- "DeviceMotionStateController"
- "Tearing down device motion state controller"
- "Timed out waiting for device state update"
- "_TtC15Diagnostic_6024P33_0C1BDCE4CF1032359B930B5818B2C02F10FinishOnce"
- "_TtC15Diagnostic_6024P33_0C1BDCE4CF1032359B930B5818B2C02F24DeviceMotionStateMonitor"
- "propertyB"
- "v24@?0@\"CMDeviceStateEvent\"8@\"NSError\"16"
```
