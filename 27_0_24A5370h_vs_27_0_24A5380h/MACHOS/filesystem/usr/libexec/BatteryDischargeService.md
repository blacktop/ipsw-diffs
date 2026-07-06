## BatteryDischargeService

> `/usr/libexec/BatteryDischargeService`

```diff

-  __TEXT.__text: 0x4ab8
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_stubs: 0x2a0
+  __TEXT.__text: 0x65c4
+  __TEXT.__auth_stubs: 0x7e0
+  __TEXT.__objc_stubs: 0x400
   __TEXT.__objc_methlist: 0x1cc
-  __TEXT.__const: 0x23a
-  __TEXT.__cstring: 0x1ba
-  __TEXT.__oslogstring: 0x405
+  __TEXT.__const: 0x2e2
+  __TEXT.__cstring: 0x24a
+  __TEXT.__oslogstring: 0x81e
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_classname: 0xf9
-  __TEXT.__objc_methname: 0x493
-  __TEXT.__objc_methtype: 0x1b5
-  __TEXT.__constg_swiftt: 0x23c
-  __TEXT.__swift5_typeref: 0xf6
-  __TEXT.__swift5_fieldmd: 0xcc
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0xfd
-  __TEXT.__swift5_assocty: 0x18
-  __TEXT.__swift5_proto: 0x8
-  __TEXT.__swift5_types: 0x10
-  __TEXT.__swift5_capture: 0x34
-  __TEXT.__unwind_info: 0x150
-  __DATA_CONST.__const: 0x1d8
+  __TEXT.__objc_methname: 0x5f5
+  __TEXT.__objc_methtype: 0x1bb
+  __TEXT.__constg_swiftt: 0x2d4
+  __TEXT.__swift5_typeref: 0x118
+  __TEXT.__swift5_fieldmd: 0xfc
+  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__swift5_reflstr: 0x14f
+  __TEXT.__swift5_assocty: 0x30
+  __TEXT.__swift5_proto: 0x10
+  __TEXT.__swift5_types: 0x14
+  __TEXT.__swift5_capture: 0x54
+  __TEXT.__unwind_info: 0x188
+  __DATA_CONST.__const: 0x298
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__auth_got: 0x398
-  __DATA_CONST.__got: 0x100
-  __DATA_CONST.__auth_ptr: 0x90
-  __DATA.__objc_const: 0x710
-  __DATA.__objc_selrefs: 0x180
-  __DATA.__objc_data: 0x328
-  __DATA.__data: 0x2b0
+  __DATA_CONST.__auth_got: 0x3f8
+  __DATA_CONST.__got: 0x110
+  __DATA_CONST.__auth_ptr: 0x98
+  __DATA.__objc_const: 0x790
+  __DATA.__objc_selrefs: 0x1d8
+  __DATA.__objc_data: 0x3c0
+  __DATA.__data: 0x2f0
   __DATA.__common: 0x30
-  __DATA.__bss: 0x100
+  __DATA.__bss: 0x200
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/BatteryDischarge.framework/BatteryDischarge
+  - /System/Library/PrivateFrameworks/LowPowerMode.framework/LowPowerMode
+  - /System/Library/PrivateFrameworks/OSIntelligence.framework/OSIntelligence
+  - /System/Library/PrivateFrameworks/PowerExperience.framework/PowerExperience
+  - /System/Library/PrivateFrameworks/PowerUI.framework/PowerUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 85
-  Symbols:   176
-  CStrings:  127
+  Functions: 108
+  Symbols:   190
+  CStrings:  162
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_entry : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
Symbols:
+ _$s10Foundation22_convertErrorToNSErrorySo0E0Cs0C0_pF
+ _$sSS10FoundationE36_unconditionallyBridgeFromObjectiveCySSSo8NSStringCSgFZ
+ _$ss5ErrorP10FoundationE20localizedDescriptionSSvg
+ _OBJC_CLASS_$_ResourceHint
+ _OBJC_CLASS_$__OSIBLMState
+ _OBJC_CLASS_$__PMLowPowerMode
+ _kPMLPMSourceSettings
+ _objc_release_x28
+ _objc_retain_x22
+ _objc_retain_x25
+ _objc_retain_x26
+ _swift_errorRelease
+ _swift_errorRetain
+ _swift_getErrorValue
+ _swift_release_x20
+ _swift_retain_x20
- _$sytN
- _swift_runtimeSupportsNoncopyableTypes
CStrings:
+ "Adaptive Power (IBLM) already off; nothing to disable"
+ "Adaptive Power (IBLM) not supported on this device; skipping"
+ "BatteryDischargeService: forcing discharge load onto the battery"
+ "Could not disable charger inflow; refusing to start discharge"
+ "Could not take inflow-disable assertion; refusing to start discharge"
+ "Created inflow-disable assertion (ID: %u); running off battery"
+ "Disabled Adaptive Power (IBLM) for discharge run (was on)"
+ "Failed to create ResourceHint — Hot in Pocket mitigation will not be toggled during discharge"
+ "Failed to create inflow-disable assertion: %d"
+ "Failed to force power mode to normal: %s (domain=%s code=%ld)"
+ "Failed to restore power mode to %ld: %s (domain=%s code=%ld)"
+ "Failed to update ResourceHint to active state"
+ "Failed to update ResourceHint to inactive state"
+ "Failed to update ResourceHint to inactive state during deinit"
+ "Forced power mode to normal for discharge run (was %ld)"
+ "Power mode already normal; nothing to disable"
+ "Released inflow-disable assertion (ID: %u); restored charger inflow"
+ "Restored Adaptive Power (IBLM) to on"
+ "Restored power mode to %ld"
+ "client:setIBLMState:"
+ "code"
+ "dischargeHint"
+ "domain"
+ "getPowerMode"
+ "inflowDisableAssertionID"
+ "initWithResourceType:andState:"
+ "isIBLMCurrentlyEnabled"
+ "isIBLMSupported"
+ "priorIBLMEnabled"
+ "priorPowerMode"
+ "processName"
+ "setPowerMode:fromSource:withCompletion:"
+ "sharedInstance"
+ "updateState:"
+ "v20@?0B8@\"NSError\"12"

```
