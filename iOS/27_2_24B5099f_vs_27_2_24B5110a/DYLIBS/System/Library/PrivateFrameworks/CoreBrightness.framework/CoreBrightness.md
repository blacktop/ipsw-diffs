## CoreBrightness

> `/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`

```diff

-2300.40.47.0.4
-  __TEXT.__text: 0x17b894
-  __TEXT.__objc_methlist: 0xdf50
-  __TEXT.__cstring: 0xd3d5
-  __TEXT.__const: 0x1b6c8
-  __TEXT.__oslogstring: 0x1b59d
-  __TEXT.__gcc_except_tab: 0x2a40
+2300.42.3.0.0
+  __TEXT.__text: 0x17c2b0
+  __TEXT.__objc_methlist: 0xdfb8
+  __TEXT.__cstring: 0xd475
+  __TEXT.__const: 0x1b788
+  __TEXT.__oslogstring: 0x1b5dd
+  __TEXT.__gcc_except_tab: 0x2a54
   __TEXT.__dlopen_cstrs: 0x218
   __TEXT.__swift5_typeref: 0xf3b
   __TEXT.__constg_swiftt: 0xd64
   __TEXT.__swift5_builtin: 0x118
-  __TEXT.__swift5_reflstr: 0xace
-  __TEXT.__swift5_fieldmd: 0x10e8
+  __TEXT.__swift5_reflstr: 0xade
+  __TEXT.__swift5_fieldmd: 0x10f4
   __TEXT.__swift5_assocty: 0x288
   __TEXT.__swift5_proto: 0x328
   __TEXT.__swift5_types: 0x138
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_capture: 0x3d0
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x7b38
+  __TEXT.__unwind_info: 0x7b60
   __TEXT.__eh_frame: 0xb98
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3270
+  __DATA_CONST.__const: 0x32d8
   __DATA_CONST.__objc_classlist: 0x7a0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x3a0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x5de8
+  __DATA_CONST.__objc_selrefs: 0x5e28
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x640
-  __DATA_CONST.__objc_arraydata: 0xcf8
-  __DATA_CONST.__got: 0x7f8
-  __AUTH_CONST.__const: 0x3fc0
-  __AUTH_CONST.__cfstring: 0xee80
-  __AUTH_CONST.__objc_const: 0x394c0
+  __DATA_CONST.__objc_arraydata: 0xda8
+  __DATA_CONST.__got: 0x800
+  __AUTH_CONST.__const: 0x3fc8
+  __AUTH_CONST.__cfstring: 0xeec0
+  __AUTH_CONST.__objc_const: 0x39520
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x80
-  __AUTH_CONST.__objc_intobj: 0xd98
-  __AUTH_CONST.__objc_arrayobj: 0x420
+  __AUTH_CONST.__objc_intobj: 0xdc8
+  __AUTH_CONST.__objc_arrayobj: 0x450
   __AUTH_CONST.__objc_floatobj: 0x1b0
-  __AUTH_CONST.__objc_dictobj: 0x550
+  __AUTH_CONST.__objc_dictobj: 0x5f0
   __AUTH_CONST.__auth_got: 0x13b0
   __AUTH.__objc_data: 0x2d30
   __AUTH.__data: 0x788
-  __DATA.__objc_ivar: 0x18b4
+  __DATA.__objc_ivar: 0x18c0
   __DATA.__data: 0x351c0
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x2238

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9138
-  Symbols:   10779
-  CStrings:  4916
+  Functions: 9152
+  Symbols:   10797
+  CStrings:  4925
 
Symbols:
+ -[CBHIDEventManager addUnfilteredClient:]
+ -[CBIndicatorBrightnessModule canJumpToTargetIndicatorBrightness]
+ -[CBIndicatorBrightnessModule isPipelineStalled]
+ -[CBIndicatorBrightnessModule isThermalPressureCritical]
+ -[CBIndicatorBrightnessModule jumpTo:forReason:withForce:]
+ -[CBIndicatorBrightnessModule recordSwapStall:]
+ -[CBIndicatorBrightnessModule setThermalPressure:]
+ -[CBIndicatorBrightnessModule startMonitoringForSwapStalls]
+ -[CBIndicatorBrightnessModule stopMonitoringForSwapStalls]
+ _OBJC_IVAR_$_CBHIDEventManager._unfilteredClients
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._consecutiveSwapStalledCount
+ _OBJC_IVAR_$_CBIndicatorBrightnessModule._swapStallObserverToken
+ ___35-[CBHIDEventManager addHIDService:]_block_invoke_3
+ ___38-[CBHIDEventManager removeHIDService:]_block_invoke_2
+ ___41-[CBHIDEventManager addUnfilteredClient:]_block_invoke
+ ___47-[CBIndicatorBrightnessModule recordSwapStall:]_block_invoke
+ ___52-[CBHIDEventManager hidEventCallbackWithEvent:from:]_block_invoke_2
+ ___59-[CBIndicatorBrightnessModule startMonitoringForSwapStalls]_block_invoke
+ ___block_descriptor_40_e8_32o_e20_v40?0{?=QIBBBffff}8ls32l8
+ ___block_descriptor_40_e8_32o_e36_v24?0"<CBHIDServiceProtocol>"8^B16ls32l8
+ ___block_descriptor_40_e8_32r_e20_v40?0{?=QIBBBffff}8lr32l8
- -[CBIndicatorBrightnessModule jumpTo:]
- GCC_except_table68
- ___block_descriptor_40_e8_32o_e19_v40?0{?=QIBBffff}8ls32l8
CStrings:
+ "Add unfiltered client %@"
+ "Backboardd restarted"
+ "DisplayIntegrated"
+ "Jumping to target indicator brightness: %f for reason: %s (forced=%d)"
+ "Overriding Boot-nits: %.2f -> %.2f nits"
+ "Ramp too long"
+ "Render pipeline stalled"
+ "Swap stall state changed: stalled=%d (%u consecutive)"
+ "Thermal pressure critical"
+ "override-boot-brightness-nits"
+ "v24@?0@\"<CBHIDServiceProtocol>\"8^B16"
+ "v40@?0{?=QIBBBffff}8"
- "Jumping to target indicator brightness: %f"
- "Thermal Pressure Critical! Snapping to target indicator brightness %f"
- "v40@?0{?=QIBBffff}8"
```
