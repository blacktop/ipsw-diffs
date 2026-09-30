## BatteryDischargeService

> `/usr/libexec/BatteryDischargeService`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`

```diff

 16.0.0.0.0
-  __TEXT.__text: 0x65c4
-  __TEXT.__auth_stubs: 0x7e0
-  __TEXT.__objc_stubs: 0x400
-  __TEXT.__objc_methlist: 0x1cc
-  __TEXT.__const: 0x2e2
-  __TEXT.__cstring: 0x24a
-  __TEXT.__oslogstring: 0x81e
+  __TEXT.__text: 0x9314
+  __TEXT.__auth_stubs: 0x940
+  __TEXT.__objc_stubs: 0x460
+  __TEXT.__objc_methlist: 0x1fc
+  __TEXT.__const: 0x2f2
+  __TEXT.__cstring: 0x3b3
+  __TEXT.__oslogstring: 0xc7e
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_classname: 0xf9
-  __TEXT.__objc_methname: 0x5f5
-  __TEXT.__objc_methtype: 0x1bb
-  __TEXT.__constg_swiftt: 0x2d4
-  __TEXT.__swift5_typeref: 0x118
-  __TEXT.__swift5_fieldmd: 0xfc
+  __TEXT.__objc_methname: 0x698
+  __TEXT.__objc_methtype: 0x23e
+  __TEXT.__constg_swiftt: 0x314
+  __TEXT.__swift5_typeref: 0x159
+  __TEXT.__swift5_fieldmd: 0x114
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0x14f
+  __TEXT.__swift5_reflstr: 0x193
   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x10
   __TEXT.__swift5_types: 0x14
-  __TEXT.__swift5_capture: 0x54
-  __TEXT.__unwind_info: 0x188
-  __DATA_CONST.__const: 0x298
+  __TEXT.__swift5_capture: 0xa8
+  __TEXT.__unwind_info: 0x1a8
+  __DATA_CONST.__const: 0x388
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__auth_got: 0x3f8
-  __DATA_CONST.__got: 0x110
-  __DATA_CONST.__auth_ptr: 0x98
-  __DATA.__objc_const: 0x790
-  __DATA.__objc_selrefs: 0x1d8
-  __DATA.__objc_data: 0x3c0
-  __DATA.__data: 0x2f0
+  __DATA_CONST.__auth_got: 0x4a8
+  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__auth_ptr: 0xa0
+  __DATA.__objc_const: 0x7c0
+  __DATA.__objc_selrefs: 0x200
+  __DATA.__objc_data: 0x408
+  __DATA.__data: 0x310
   __DATA.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 108
-  Symbols:   190
-  CStrings:  162
+  Functions: 134
+  Symbols:   217
+  CStrings:  201
 
Symbols:
+ _$s10Foundation4DateV18addingTimeIntervalyACSdF
+ _$s10Foundation4DateV1loiySbAC_ACtFZ
+ _$s8Dispatch0A12TimeIntervalO7secondsyACSicACmFWC
+ _$s8Dispatch0A13TimeoutResultO2eeoiySbAC_ACtFZ
+ _$s8Dispatch0A3QoSV0B6SClassO7defaultyA2EmFWC
+ _$s8Dispatch0A3QoSV0B6SClassOMa
+ _$s8Dispatch1poiyAA0A4TimeVAD_AA0aB8IntervalOtF
+ _$sSo17OS_dispatch_queueC8DispatchE6global3qosAbC0D3QoSV0G6SClassO_tFZ
+ _$sSo21OS_dispatch_semaphoreC8DispatchE4wait7timeoutAC0D13TimeoutResultOAC0D4TimeV_tF
+ _$sSo21OS_dispatch_semaphoreC8DispatchE6signalSiyF
+ _$ss018_bridgeAnyObjectToB0yypyXlSgF
+ _$ss38_bridgeAnythingNonVerbatimToObjectiveCyyXlxnlF
+ _$ss5Int32VMn
+ _IOPSShippingChargeLimitEnable
+ _IOPSShippingChargeLimitGetState
+ _OBJC_CLASS_$_NSNumber
+ ___stack_chk_fail
+ ___stack_chk_guard
+ _dispatch_semaphore_create
+ _notify_cancel
+ _notify_register_dispatch
+ _objc_release_x9
+ _objc_retain_x24
+ _objc_retain_x27
+ _swift_release_n
+ _swift_release_x21
+ _swift_release_x28
+ _swift_retain_x28
- _objc_release_x28
CStrings:
+ "% UISOC without compliance"
+ "Battery shipping-compliant after engaging ship mode; no discharge needed"
+ "Compliance state still pending after %fs"
+ "Compliant; ship mode engaged"
+ "Device not supported"
+ "Device not supported (shipping charge limit unavailable)"
+ "Disabled shipping charge limit feature on cancel/abort"
+ "Discharge already running, ignoring shipping-compliance start request"
+ "Failed to enable shipping charge limit"
+ "Failed to read shipping charge limit state"
+ "Failed to read shipping charge limit state while awaiting compliance settle"
+ "IOPSShippingChargeLimitEnable completion did not fire within timeout"
+ "IOPSShippingChargeLimitEnable completion reported failure: %d"
+ "IOPSShippingChargeLimitEnable setup failed: %d"
+ "IOPSShippingChargeLimitEnable(false) failed: %d"
+ "IOPSShippingChargeLimitGetState failed: %d"
+ "ShipChargeLimitComplianceStatePending"
+ "ShipChargeLimitCompliant"
+ "ShipChargeLimitEnabled"
+ "ShipChargeLimitSupported"
+ "Shipping compliance reached in %lds"
+ "Shipping compliance reached in %lds (poll)"
+ "Shipping-compliance poll: UISOC %ld%%, not yet compliant"
+ "ShippingChargeLimit dict: %@"
+ "Starting shipping-compliance discharge with thermal mode %ld"
+ "UISOC %ld%% hit %ld%% safety floor without compliance; aborting"
+ "__swift_objectForKeyedSubscript:"
+ "boolValue"
+ "com.apple.system.powersources"
+ "getShippingComplianceStatusWithReply:"
+ "notify_register_dispatch failed: %u; compliance detection degraded to 10-minute poll only"
+ "shippingNotifyToken"
+ "sleepForTimeInterval:"
+ "startShippingComplianceDischargeWithThermalMode:completion:"
+ "v12@?0i8"
+ "v20@?0i8r^{__CFDictionary=}12"
+ "v24@0:8@?<v@?BBB>16"
+ "v32@0:8q16@?24"
+ "v32@0:8q16@?<v@?B@\"NSString\">24"
```
