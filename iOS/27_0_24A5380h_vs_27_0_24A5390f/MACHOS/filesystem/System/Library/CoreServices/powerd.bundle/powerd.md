## powerd

> `/System/Library/CoreServices/powerd.bundle/powerd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2043.0.13.502.1
-  __TEXT.__text: 0x77744
+2043.0.31.0.0
+  __TEXT.__text: 0x77d44
   __TEXT.__auth_stubs: 0x1bf0
   __TEXT.__objc_stubs: 0x5900
-  __TEXT.__objc_methlist: 0x2c54
-  __TEXT.__const: 0x4e0
-  __TEXT.__cstring: 0x6ec2
-  __TEXT.__objc_methname: 0x71e8
-  __TEXT.__oslogstring: 0xe0b2
+  __TEXT.__objc_methlist: 0x2c6c
+  __TEXT.__const: 0x540
+  __TEXT.__cstring: 0x6e93
+  __TEXT.__objc_methname: 0x720c
+  __TEXT.__oslogstring: 0xe24a
   __TEXT.__objc_classname: 0x3f3
-  __TEXT.__objc_methtype: 0xa8e
+  __TEXT.__objc_methtype: 0xaa0
   __TEXT.__gcc_except_tab: 0x4fc
   __TEXT.__dlopen_cstrs: 0x300
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x1668
-  __DATA_CONST.__const: 0x26a0
-  __DATA_CONST.__cfstring: 0x76e0
+  __TEXT.__unwind_info: 0x1690
+  __DATA_CONST.__const: 0x26c0
+  __DATA_CONST.__cfstring: 0x76a0
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__auth_got: 0xe08
   __DATA_CONST.__got: 0x3c0
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA.__objc_const: 0x56a8
-  __DATA.__objc_selrefs: 0x1c28
+  __DATA.__objc_const: 0x56b0
+  __DATA.__objc_selrefs: 0x1c30
   __DATA.__objc_ivar: 0x3d4
   __DATA.__objc_data: 0x910
   __DATA.__data: 0xbbc
-  __DATA.__bss: 0xdc0
+  __DATA.__bss: 0xdd8
   __DATA.__common: 0x1270
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2632
+  Functions: 2648
   Symbols:   575
-  CStrings:  4066
+  CStrings:  4074
 
CStrings:
+ "3.2"
+ "Battery P0 threshold is not set (packId=%u)\n"
+ "Failed to get Battery health P0 threshold value (packId=%u)\n"
+ "Received notification for batteryHealthP0Threshold. Value set to %llu\n"
+ "Retrieved p0 threshold for pack (packId=%u packThreshold=%d batteryHealthP0Threshold=%llu)"
+ "ShipChargeLimit: Cleared battery level limit\n"
+ "ShipChargeLimit: Failed to %s battery limit: %#x\n"
+ "ShipChargeLimit: Failed to clear battery level limit %#x\n"
+ "ShipChargeLimit: Failed to register battery limit token: %#x\n"
+ "ShipChargeLimit: Failed to set battery level limit: %#x\n"
+ "ShipChargeLimit: Set battery level limit\n"
+ "WeightedRa(%d) is >= threshold(%d) (packId=%u)\n"
+ "batteryHealthP0Threshold set to %llu\n"
+ "clear"
+ "getPowerModeUserInitiatedWithReply:"
+ "set"
+ "v24@0:8@?<v@?B>16"
- "3.1"
- "Battery P0 threshold is not set\n"
- "Failed to get Battery health P0 threshold value\n"
- "Received notification for batteryHealthP0Threshold. Value set to %lld\n"
- "ShipChargeLimitCompliant"
- "ShipChargeLimitData incomplete\n"
- "ShippingChargeLimitSystemStatus"
- "WeightedRa(%d) is >= threshold(%llu)\n"
- "batteryHealthP0Threshold set to %lld\n"
```
