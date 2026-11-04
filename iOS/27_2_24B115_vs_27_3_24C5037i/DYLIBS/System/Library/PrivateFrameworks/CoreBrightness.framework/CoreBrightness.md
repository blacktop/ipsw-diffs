## CoreBrightness

> `/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`

```diff

-2300.42.3.0.0
-  __TEXT.__text: 0x17c2b0
-  __TEXT.__objc_methlist: 0xdfb8
-  __TEXT.__cstring: 0xd475
-  __TEXT.__const: 0x1b788
-  __TEXT.__oslogstring: 0x1b5dd
-  __TEXT.__gcc_except_tab: 0x2a54
+2300.60.30.0.0
+  __TEXT.__text: 0x17f44c
+  __TEXT.__objc_methlist: 0xe140
+  __TEXT.__cstring: 0xd5da
+  __TEXT.__const: 0x1bb80
+  __TEXT.__oslogstring: 0x1bdda
+  __TEXT.__gcc_except_tab: 0x2ae4
   __TEXT.__dlopen_cstrs: 0x218
-  __TEXT.__swift5_typeref: 0xf3b
+  __TEXT.__swift5_typeref: 0xf3c
   __TEXT.__constg_swiftt: 0xd64
   __TEXT.__swift5_builtin: 0x118
-  __TEXT.__swift5_reflstr: 0xade
-  __TEXT.__swift5_fieldmd: 0x10f4
+  __TEXT.__swift5_reflstr: 0xadc
+  __TEXT.__swift5_fieldmd: 0x10e8
   __TEXT.__swift5_assocty: 0x288
   __TEXT.__swift5_proto: 0x328
   __TEXT.__swift5_types: 0x138
-  __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_capture: 0x3d0
   __TEXT.__swift5_mpenum: 0x28
-  __TEXT.__unwind_info: 0x7b60
+  __TEXT.__swift5_protos: 0x8
+  __TEXT.__unwind_info: 0x7c88
   __TEXT.__eh_frame: 0xb98
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x32d8
-  __DATA_CONST.__objc_classlist: 0x7a0
+  __DATA_CONST.__const: 0x3330
+  __DATA_CONST.__objc_classlist: 0x7b8
   __DATA_CONST.__objc_catlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x3a0
+  __DATA_CONST.__objc_protolist: 0x3b0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0x5e28
+  __DATA_CONST.__objc_selrefs: 0x5e80
   __DATA_CONST.__objc_protorefs: 0x158
-  __DATA_CONST.__objc_superrefs: 0x640
-  __DATA_CONST.__objc_arraydata: 0xda8
-  __DATA_CONST.__got: 0x800
-  __AUTH_CONST.__const: 0x3fc8
-  __AUTH_CONST.__cfstring: 0xeec0
-  __AUTH_CONST.__objc_const: 0x39520
+  __DATA_CONST.__objc_superrefs: 0x658
+  __DATA_CONST.__objc_arraydata: 0xdc0
+  __DATA_CONST.__got: 0x7f8
+  __AUTH_CONST.__const: 0x3fe0
+  __AUTH_CONST.__cfstring: 0xf140
+  __AUTH_CONST.__objc_const: 0x3a140
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_doubleobj: 0x80
   __AUTH_CONST.__objc_intobj: 0xdc8
-  __AUTH_CONST.__objc_arrayobj: 0x450
-  __AUTH_CONST.__objc_floatobj: 0x1b0
+  __AUTH_CONST.__objc_arrayobj: 0x468
   __AUTH_CONST.__objc_dictobj: 0x5f0
-  __AUTH_CONST.__auth_got: 0x13b0
-  __AUTH.__objc_data: 0x2d30
+  __AUTH_CONST.__objc_floatobj: 0x1b0
+  __AUTH_CONST.__auth_got: 0x1400
+  __AUTH.__objc_data: 0x2e20
   __AUTH.__data: 0x788
-  __DATA.__objc_ivar: 0x18c0
-  __DATA.__data: 0x351c0
+  __DATA.__objc_ivar: 0x190c
+  __DATA.__data: 0x35280
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x2238
   __DATA_DIRTY.__data: 0x4e8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9152
-  Symbols:   10797
-  CStrings:  4925
+  Functions: 9230
+  Symbols:   10895
+  CStrings:  4992
 
Symbols:
+ -[CBDisplayContaineriOS initialiseExtGenericDisplay]
+ -[CBDisplayContaineriOS tearDownExtGenericDisplay]
+ -[CBDisplayModuleExtGeneric commitBrightness:]
+ -[CBDisplayModuleExtGeneric copyPropertyForKey:]
+ -[CBDisplayModuleExtGeneric dealloc]
+ -[CBDisplayModuleExtGeneric displayMode]
+ -[CBDisplayModuleExtGeneric handleDisplayModeUpdate:withDuration:callback:]
+ -[CBDisplayModuleExtGeneric handleNotificationForKey:withProperty:]
+ -[CBDisplayModuleExtGeneric initWithService:andQueue:andDisplayId:]
+ -[CBDisplayModuleExtGeneric newStatusInfo]
+ -[CBDisplayModuleExtGeneric probeBrightnessAttempt:]
+ -[CBDisplayModuleExtGeneric readControl:currentValue:maxValue:]
+ -[CBDisplayModuleExtGeneric setDisplayMode:]
+ -[CBDisplayModuleExtGeneric setProperty:forKey:]
+ -[CBDisplayModuleExtGeneric start]
+ -[CBDisplayModuleExtGeneric stop]
+ -[CBDisplayModuleExtGeneric writeControl:value:]
+ -[CBIOAVServiceLookup dealloc]
+ -[CBIOAVServiceLookup edidBytesMatchDisplay:]
+ -[CBIOAVServiceLookup handleServiceArrival:]
+ -[CBIOAVServiceLookup initWithVendorId:productId:serialNumber:queue:]
+ -[CBIOAVServiceLookup registerNotificationBlock:]
+ -[CBIOAVServiceLookup start]
+ -[CBIOAVServiceLookup stop]
+ -[CBIOAVServiceLookup unregisterNotificationBlock]
+ -[CBIndicatorBrightnessModule jumpTo:]
+ -[CBSliderMappingGenericMac configureSegmentCoefficients]
+ -[CBSliderMappingGenericMac copyStatusInfo]
+ -[CBSliderMappingGenericMac initWithPanelParameters:]
+ -[CBSliderMappingGenericMac nitsForSlider:]
+ -[CBSliderMappingGenericMac sliderForNits:]
+ -[CBSliderMappingGenericMac validateParameters]
+ GCC_except_table68
+ _CBU_DeviceEnclosureColor
+ _CBU_isExtGenericDisplayEnabled
+ _CBU_isExtGenericDisplayEnabled.once
+ _CBU_isExtGenericDisplayEnabled.result
+ _CFStringGetIntValue
+ _IOAVServiceCopyEDID
+ _IOAVServiceCreateWithService
+ _IOAVServiceGetLocation
+ _IOAVServiceReadI2C
+ _IOAVServiceWriteI2C
+ _OBJC_CLASS_$_CBDisplayModuleExtGeneric
+ _OBJC_CLASS_$_CBIOAVServiceLookup
+ _OBJC_CLASS_$_CBSliderMappingGenericMac
+ _OBJC_IVAR_$_CBDisplayContaineriOS._extGenericModuleActive
+ _OBJC_IVAR_$_CBDisplayContaineriOS._extGenericServiceLookup
+ _OBJC_IVAR_$_CBDisplayModuleExtGeneric._avService
+ _OBJC_IVAR_$_CBDisplayModuleExtGeneric._displayId
+ _OBJC_IVAR_$_CBDisplayModuleExtGeneric._displayMode
+ _OBJC_IVAR_$_CBDisplayModuleExtGeneric._logHandle
+ _OBJC_IVAR_$_CBDisplayModuleExtGeneric._maxLevel
+ _OBJC_IVAR_$_CBDisplayModuleExtGeneric._slider
+ _OBJC_IVAR_$_CBDisplayModuleExtGeneric._userBrightness
+ _OBJC_IVAR_$_CBIOAVServiceLookup._foundBlock
+ _OBJC_IVAR_$_CBIOAVServiceLookup._logHandle
+ _OBJC_IVAR_$_CBIOAVServiceLookup._notificationPort
+ _OBJC_IVAR_$_CBIOAVServiceLookup._productId
+ _OBJC_IVAR_$_CBIOAVServiceLookup._queue
+ _OBJC_IVAR_$_CBIOAVServiceLookup._serialNumber
+ _OBJC_IVAR_$_CBIOAVServiceLookup._serviceIterator
+ _OBJC_IVAR_$_CBIOAVServiceLookup._vendorId
+ _OBJC_IVAR_$_CBSliderMappingGenericMac._b1
+ _OBJC_IVAR_$_CBSliderMappingGenericMac._b2
+ _OBJC_IVAR_$_CBSliderMappingGenericMac._m1
+ _OBJC_IVAR_$_CBSliderMappingGenericMac._m2
+ _OBJC_IVAR_$_CBSliderMappingGenericMac._panelParameters
+ _OBJC_IVAR_$_VMDisplayModule._requestDelegate
+ _OBJC_METACLASS_$_CBDisplayModuleExtGeneric
+ _OBJC_METACLASS_$_CBIOAVServiceLookup
+ _OBJC_METACLASS_$_CBSliderMappingGenericMac
+ __OBJC_$_INSTANCE_METHODS_CBDisplayModuleExtGeneric
+ __OBJC_$_INSTANCE_METHODS_CBIOAVServiceLookup
+ __OBJC_$_INSTANCE_METHODS_CBSliderMappingGenericMac
+ __OBJC_$_INSTANCE_VARIABLES_CBDisplayModuleExtGeneric
+ __OBJC_$_INSTANCE_VARIABLES_CBIOAVServiceLookup
+ __OBJC_$_INSTANCE_VARIABLES_CBSliderMappingGenericMac
+ __OBJC_$_PROP_LIST_CBDisplayModuleExtGeneric
+ __OBJC_$_PROP_LIST_CBIOAVServiceLookup
+ __OBJC_$_PROP_LIST_CBSliderMappingGenericMac
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CBServiceLookupProtocol
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_CBSliderMapping
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_VMRequestDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CBServiceLookupProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CBSliderMapping
+ __OBJC_$_PROTOCOL_METHOD_TYPES_VMRequestDelegate
+ __OBJC_$_PROTOCOL_REFS_CBServiceLookupProtocol
+ __OBJC_$_PROTOCOL_REFS_CBSliderMapping
+ __OBJC_$_PROTOCOL_REFS_VMRequestDelegate
+ __OBJC_CLASS_PROTOCOLS_$_CBDisplayModuleExtGeneric
+ __OBJC_CLASS_PROTOCOLS_$_CBIOAVServiceLookup
+ __OBJC_CLASS_PROTOCOLS_$_CBSliderMappingGenericMac
+ __OBJC_CLASS_RO_$_CBDisplayModuleExtGeneric
+ __OBJC_CLASS_RO_$_CBIOAVServiceLookup
+ __OBJC_CLASS_RO_$_CBSliderMappingGenericMac
+ __OBJC_LABEL_PROTOCOL_$_CBServiceLookupProtocol
+ __OBJC_LABEL_PROTOCOL_$_CBSliderMapping
+ __OBJC_LABEL_PROTOCOL_$_VMRequestDelegate
+ __OBJC_METACLASS_RO_$_CBDisplayModuleExtGeneric
+ __OBJC_METACLASS_RO_$_CBIOAVServiceLookup
+ __OBJC_METACLASS_RO_$_CBSliderMappingGenericMac
+ __OBJC_PROTOCOL_$_CBServiceLookupProtocol
+ __OBJC_PROTOCOL_$_CBSliderMapping
+ __OBJC_PROTOCOL_$_VMRequestDelegate
+ __ZN14CoreBrightnessL14sbimLimitsJ51xE
+ ___42-[CBDisplayModuleExtGeneric newStatusInfo]_block_invoke
+ ___52-[CBDisplayContaineriOS initialiseExtGenericDisplay]_block_invoke
+ ___52-[CBDisplayModuleExtGeneric probeBrightnessAttempt:]_block_invoke
+ ___CBU_isExtGenericDisplayEnabled_block_invoke
+ ___IOAVClassMatching
+ ___block_descriptor_40_e8_32o_e19_v40?0{?=QIBBffff}8ls32l8
+ ___block_descriptor_40_e8_32w_e8_v16?08lw32l8
+ ___block_descriptor_48_e8_32o40r_e25_v32?0"NSString"8Q16^B24ls32l8r40l8
+ ___block_descriptor_48_e8_32w40w_e11_v24?0816lw32l8w40l8
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_initWeak
+ _objc_loadWeak
+ _serviceArrivalCallback
- -[CBIndicatorBrightnessModule canJumpToTargetIndicatorBrightness]
- -[CBIndicatorBrightnessModule isPipelineStalled]
- -[CBIndicatorBrightnessModule isThermalPressureCritical]
- -[CBIndicatorBrightnessModule jumpTo:forReason:withForce:]
- -[CBIndicatorBrightnessModule recordSwapStall:]
- -[CBIndicatorBrightnessModule setThermalPressure:]
- -[CBIndicatorBrightnessModule startMonitoringForSwapStalls]
- -[CBIndicatorBrightnessModule stopMonitoringForSwapStalls]
- _OBJC_IVAR_$_CBIndicatorBrightnessModule._consecutiveSwapStalledCount
- _OBJC_IVAR_$_CBIndicatorBrightnessModule._swapStallObserverToken
- _OBJC_IVAR_$_VMDisplayModule._headroomRequestDelegate
- _OBJC_IVAR_$_VMDisplayModule._lastBrightnessTransaction
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_VMHeadroomRequestDelegate
- __OBJC_$_PROTOCOL_METHOD_TYPES_VMHeadroomRequestDelegate
- __OBJC_$_PROTOCOL_REFS_VMHeadroomRequestDelegate
- __OBJC_LABEL_PROTOCOL_$_VMHeadroomRequestDelegate
- __OBJC_PROTOCOL_$_VMHeadroomRequestDelegate
- ___47-[CBIndicatorBrightnessModule recordSwapStall:]_block_invoke
- ___59-[CBIndicatorBrightnessModule startMonitoringForSwapStalls]_block_invoke
- ___block_descriptor_40_e8_32o_e20_v40?0{?=QIBBBffff}8ls32l8
- ___block_descriptor_40_e8_32r_e20_v40?0{?=QIBBBffff}8lr32l8
- _xpc_retain
CStrings:
+ "AVService"
+ "B1"
+ "B2"
+ "CurrentLevel"
+ "DisplayServicesBrightness"
+ "DisplayServicesBrightnessCommit"
+ "DisplayServicesCanChangeBrightness"
+ "DisplayServicesSetBrightnessSmooth"
+ "EDID candidate: ven=0x%04x prod=0x%04x ser=0x%08x | expected: ven=0x%04llx prod=0x%04llx ser=0x%08llx"
+ "EDID does not match this display, skipping"
+ "EDID too short (%ld bytes), skipping"
+ "ExtGeneric"
+ "ExtGeneric: display module already present for displayID=%u, ignoring arrival"
+ "ExtGeneric: failed to create module for displayID=%u"
+ "ExtGeneric: lookup already in flight for displayID=%u"
+ "ExtGeneric: module failed to start for displayID=%u"
+ "ExtGeneric: module started for displayID=%u"
+ "ExtGeneric: no externalDisplayAttributes for displayID=%u, skipping"
+ "ExtGeneric: service lookup failed to start for displayID=%u"
+ "ExtGeneric: starting lookup for displayID=%u (vid=0x%04x pid=0x%04x)"
+ "Generic non-LUT"
+ "HID service arrived after ExtGeneric fallback, retiring ExtGeneric module"
+ "IOAVClassMatching returned NULL"
+ "IOAVService"
+ "IOAVServiceCopyEDID failed (0x%x), skipping"
+ "IOAVServiceCreateWithService returned NULL, skipping"
+ "Jumping to target indicator brightness: %f"
+ "L_Max"
+ "L_Mid"
+ "L_Min"
+ "M1"
+ "M2"
+ "MaxLevel"
+ "Multitouch event - X: %{private}f, Y: %{private}f, range: %{private}f, minor r: %{private}f, major r: %{private}f, touch: %{private}d, ALS[%d] obstruction %sdetected"
+ "Offline"
+ "Online (%p)"
+ "S_Max"
+ "S_Mid"
+ "S_Min"
+ "Thermal Pressure Critical! Snapping to target indicator brightness %f"
+ "brightness control read failed for display %u"
+ "com.apple.CoreBrightness.CBDisplayModuleExtGeneric"
+ "com.apple.CoreBrightness.CBIOAVServiceLookup"
+ "commitBrightness: rejecting non-finite value"
+ "commitBrightness: slider=%.3f -> level %u/%u"
+ "copyPropertyForKey: \"%@\""
+ "copyPropertyForKey: unknown key, returning nil"
+ "dealloc: displayId=%u avService=%p"
+ "display %u online — brightness %u/%u (%.2f)"
+ "ext_generic_display_brightness"
+ "failed to create notification port"
+ "failed to register IOService notification: 0x%x"
+ "handleServiceArrival: service=%u"
+ "init: avService=%p queue=%p"
+ "init: ven=0x%04llx prod=0x%04llx ser=0x%08llx"
+ "invalid iterator"
+ "invalid refcon"
+ "late probe gave up after %d attempts"
+ "late probe: attempt %d cur=%u -> %.3f"
+ "matched IOAVService for display ven=0x%04llx prod=0x%04llx"
+ "newStatusInfo: %@"
+ "read control reply failed: 0x%x"
+ "read control request failed: 0x%x"
+ "read control: bad reply — opcode=0x%02x (expected 0x%02x) result=0x%02x (expected 0x%02x) control=0x%02x (expected 0x%02x)"
+ "readControl: opcode=0x%02x (avService=%p)"
+ "requestDelegate is nil, cannot request brightness transaction"
+ "requestDelegate is nil, ignoring headroom request"
+ "setProperty: key=\"%@\" value=%@ class=%@"
+ "skipping embedded display"
+ "start: displayId=%u"
+ "start: probe OK — cur=%u max=%u userBrightness=%.4f"
+ "stop: displayId=%u avService=%p"
+ "v16@?0@8"
+ "v32@?0@\"NSString\"8Q16^B24"
+ "v40@?0{?=QIBBffff}8"
+ "write control 0x%02x failed: 0x%x"
+ "writeControl: opcode=0x%02x value=%u (avService=%p)"
- "Backboardd restarted"
- "Jumping to target indicator brightness: %f for reason: %s (forced=%d)"
- "Multitouch event - X: %f, Y: %f, range: %f, minor r: %f, major r: %f, touch: %d, ALS[%d] obstruction %sdetected"
- "Ramp too long"
- "Render pipeline stalled"
- "Swap stall state changed: stalled=%d (%u consecutive)"
- "Thermal pressure critical"
- "headroomRequestDelegate is nil, cannot request brightness transaction"
- "headroomRequestDelegate is nil, ignoring headroom request"
- "v40@?0{?=QIBBBffff}8"
```
