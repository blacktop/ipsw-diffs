## dasd

> `/usr/libexec/dasd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2467.40.41.0.0
-  __TEXT.__text: 0x1763b8
-  __TEXT.__auth_stubs: 0x2250
-  __TEXT.__objc_stubs: 0x1b520
-  __TEXT.__objc_methlist: 0x1343c
+2467.40.47.0.0
+  __TEXT.__text: 0x1766e4
+  __TEXT.__auth_stubs: 0x2280
+  __TEXT.__objc_stubs: 0x1b540
+  __TEXT.__objc_methlist: 0x1346c
   __TEXT.__const: 0x1588
-  __TEXT.__objc_methname: 0x2ed55
-  __TEXT.__cstring: 0x10806
-  __TEXT.__oslogstring: 0x172e9
+  __TEXT.__objc_methname: 0x2ee35
+  __TEXT.__cstring: 0x10886
+  __TEXT.__oslogstring: 0x17379
   __TEXT.__objc_classname: 0x1cd8
   __TEXT.__objc_methtype: 0x42e1
   __TEXT.__gcc_except_tab: 0x5044

   __TEXT.__swift_as_cont: 0x80
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x65a0
+  __TEXT.__unwind_info: 0x65b0
   __TEXT.__eh_frame: 0xbd0
   __DATA_CONST.__const: 0x5038
-  __DATA_CONST.__cfstring: 0x11c20
+  __DATA_CONST.__cfstring: 0x11ca0
   __DATA_CONST.__objc_classlist: 0x710
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x220

   __DATA_CONST.__objc_arrayobj: 0x1e0
   __DATA_CONST.__objc_dictobj: 0x230
   __DATA_CONST.__objc_doubleobj: 0x50
-  __DATA_CONST.__auth_got: 0x1138
-  __DATA_CONST.__got: 0xe58
+  __DATA_CONST.__auth_got: 0x1150
+  __DATA_CONST.__got: 0xe50
   __DATA_CONST.__auth_ptr: 0x190
-  __DATA.__objc_const: 0x34420
-  __DATA.__objc_selrefs: 0x9e88
-  __DATA.__objc_ivar: 0x1650
+  __DATA.__objc_const: 0x34450
+  __DATA.__objc_selrefs: 0x9ea0
+  __DATA.__objc_ivar: 0x1654
   __DATA.__objc_data: 0x4958
   __DATA.__data: 0x2200
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8441
-  Symbols:   1020
-  CStrings:  12573
+  Functions: 8447
+  Symbols:   1023
+  CStrings:  12585
 
Symbols:
+ _IOIteratorNext
+ _IORegistryEntryCreateCFProperty
+ _IOServiceGetMatchingServices
CStrings:
+ "%s unavailable across all AppleSmartBatteryPack nodes"
+ "%{public}@: %{public}@ is not present in the list of %lu foregrounded applications: %@"
+ "(unknown)"
+ "AppleChargerData"
+ "AppleSmartBatteryPack"
+ "BatteryData"
+ "BatteryTemperatureReader returning value %ld (centi-C)"
+ "Foregrounded App Count"
+ "No match for AppleSmartBatteryPack IOService"
+ "TB,N,V_disableSpecialCasedThermalPolicyForDuo"
+ "Unable to get valid battery temperature from AppleSmartBattery"
+ "VirtualTemperature"
+ "_disableSpecialCasedThermalPolicyForDuo"
+ "batteryTemperatureReader"
+ "disableSpecialCasedThermalPolicyForDuo"
+ "maxBatteryTemperatureAcrossPacks"
+ "notChargingReasonUnionAcrossPacks"
+ "setDisableSpecialCasedThermalPolicyForDuo:"
- "%{public}@: Foregrounded apps (%@) don't include expected identifier: %@"
- "BatteryTemperatureReader returning value %@"
- "Foregrounded Apps"
- "Temperature"
- "Unable to get valid battery temperature: %@"
- "batteryTemperatureKey"
```
