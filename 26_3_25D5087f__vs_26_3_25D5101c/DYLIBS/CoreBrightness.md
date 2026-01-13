## CoreBrightness

> `/System/Library/PrivateFrameworks/CoreBrightness.framework/Versions/A/CoreBrightness`

```diff

-2079.80.67.0.0
-  __TEXT.__text: 0x10b0a4
+2079.80.73.0.0
+  __TEXT.__text: 0x10b2c0
   __TEXT.__auth_stubs: 0x1e30
-  __TEXT.__objc_methlist: 0x9aec
-  __TEXT.__const: 0x11294
+  __TEXT.__objc_methlist: 0x9afc
+  __TEXT.__const: 0x11274
   __TEXT.__gcc_except_tab: 0x1a78
-  __TEXT.__cstring: 0xa7f4
-  __TEXT.__oslogstring: 0x13a09
+  __TEXT.__cstring: 0xa874
+  __TEXT.__oslogstring: 0x13a49
   __TEXT.__dlopen_cstrs: 0x10d
   __TEXT.__swift5_typeref: 0x44e
   __TEXT.__constg_swiftt: 0x190

   __TEXT.__swift5_proto: 0x6c
   __TEXT.__swift5_types: 0x28
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x38b0
+  __TEXT.__unwind_info: 0x38b8
   __TEXT.__eh_frame: 0x428
   __TEXT.__objc_classname: 0xe07
-  __TEXT.__objc_methname: 0x11fc8
+  __TEXT.__objc_methname: 0x11feb
   __TEXT.__objc_methtype: 0x441b
   __TEXT.__objc_stubs: 0xe7a0
   __DATA_CONST.__got: 0x4e0

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4480
+  __DATA_CONST.__objc_selrefs: 0x4488
   __DATA_CONST.__objc_protorefs: 0x60
   __DATA_CONST.__objc_superrefs: 0x460
   __DATA_CONST.__objc_arraydata: 0x778

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: EEF6B258-277D-300D-A22D-091B1ED882CB
-  Functions: 5559
-  Symbols:   11939
-  CStrings:  9675
+  UUID: C7BC17ED-356E-35A3-B2AD-260A1BD4B504
+  Functions: 5562
+  Symbols:   11942
+  CStrings:  9679
 
Symbols:
+ -[CBDisplayModuleSKL updateNitsCapLuminanceNotification]
+ -[CBGammaContrastPreservationPolicy rampDownLuxDeltaThresholdFor:].cold.1
+ -[CBGammaContrastPreservationPolicy rampUpLuxDeltaThresholdFor:].cold.1
+ GCC_except_table216
+ GCC_except_table231
+ __62-[CBDisplayModuleSKL rampSDRBrightness:withLength:properties:]_block_invoke.535
+ __62-[CBDisplayModuleSKL rampSDRBrightness:withLength:properties:]_block_invoke.535.cold.1
+ __65-[CBDisplayModuleSKL rampBrightnessScaler:withLength:properties:]_block_invoke.543
+ __65-[CBDisplayModuleSKL rampBrightnessScaler:withLength:properties:]_block_invoke.543.cold.1
+ __block_literal_global.538
+ _objc_msgSend$updateNitsCapLuminanceNotification
- GCC_except_table215
- GCC_except_table230
- _AAP_LuxThreshold
- _GCP_LuxThreshold
- __62-[CBDisplayModuleSKL rampSDRBrightness:withLength:properties:]_block_invoke.536
- __62-[CBDisplayModuleSKL rampSDRBrightness:withLength:properties:]_block_invoke.536.cold.1
- __65-[CBDisplayModuleSKL rampBrightnessScaler:withLength:properties:]_block_invoke.544
- __65-[CBDisplayModuleSKL rampBrightnessScaler:withLength:properties:]_block_invoke.544.cold.1
- __block_literal_global.539
- _objc_msgSend$initWithContainerUUID:andDisplayId:
CStrings:
+ "%s: Given value %f is not in valid range [0,1], clamping to %f"
+ "-[CBGammaContrastPreservationPolicy rampDownLuxDeltaThresholdFor:]"
+ "-[CBGammaContrastPreservationPolicy rampUpLuxDeltaThresholdFor:]"
+ "[AAP] Update for Lux change %f -> %f, Lux delta %f%% >= %f%% Lux threshold"
+ "brightness update: SDR=%f | EDR.applied=%f | EDR.nits=%f | EDR.req=%f | EDR.ref=%f | EDR.available=%f | EDR.max=%f | lux=%f | limit=%f | gcp=%f | pcc=%f"
+ "updateNitsCapLuminanceNotification"
- "[AAP] Update for Lux change %f -> %f, Lux delta %f%% > %f%% Lux threshold"
- "brightness update: SDR=%f | EDR.applied=%f | EDR.nits=%f | EDR.req=%f | EDR.ref=%f | EDR.available=%f | EDR.max=%f | lux=%f | limit=%f | gcp=%f"

```
