## locationd

> `/usr/libexec/locationd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3186.0.12.0.0
-  __TEXT.__text: 0x1aecdf4
+3186.0.17.0.1
+  __TEXT.__text: 0x1aedd44
   __TEXT.__auth_stubs: 0x6550
-  __TEXT.__objc_stubs: 0x3e420
+  __TEXT.__objc_stubs: 0x3e4c0
   __TEXT.__init_offsets: 0xc08
-  __TEXT.__objc_methlist: 0x2e6d0
-  __TEXT.__const: 0x166848
-  __TEXT.__gcc_except_tab: 0xda4d0
-  __TEXT.__oslogstring: 0x291f05
-  __TEXT.__cstring: 0x210541
-  __TEXT.__objc_methname: 0x5d07f
+  __TEXT.__objc_methlist: 0x2e700
+  __TEXT.__const: 0x166878
+  __TEXT.__gcc_except_tab: 0xda518
+  __TEXT.__oslogstring: 0x2924c5
+  __TEXT.__cstring: 0x210791
+  __TEXT.__objc_methname: 0x5d09f
   __TEXT.__objc_classname: 0x8097
-  __TEXT.__objc_methtype: 0x39047
+  __TEXT.__objc_methtype: 0x39037
   __TEXT.__dlopen_cstrs: 0x4a
   __TEXT.__ustring: 0xa5e
   __TEXT.__constg_swiftt: 0x5ec

   __TEXT.__swift_as_cont: 0x1c
   __TEXT.__swift5_proto: 0x4c
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__unwind_info: 0x88f80
+  __TEXT.__unwind_info: 0x88fd0
   __TEXT.__eh_frame: 0xf38
-  __DATA_CONST.__const: 0xc1c08
+  __DATA_CONST.__const: 0xc1ba8
   __DATA_CONST.__cfstring: 0x44460
   __DATA_CONST.__objc_classlist: 0x14c0
   __DATA_CONST.__objc_catlist: 0xc8

   __DATA_CONST.__auth_got: 0x32c8
   __DATA_CONST.__got: 0x25e0
   __DATA_CONST.__auth_ptr: 0x6a0
-  __DATA.__objc_const: 0x4f690
-  __DATA.__objc_selrefs: 0x13b78
-  __DATA.__objc_ivar: 0x3bf8
+  __DATA.__objc_const: 0x4f670
+  __DATA.__objc_selrefs: 0x13b98
+  __DATA.__objc_ivar: 0x3bf4
   __DATA.__objc_data: 0xd528
   __DATA.__data: 0x62f08
   __DATA.__common: 0x22100

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 113470
+  Functions: 113489
   Symbols:   2915
-  CStrings:  85189
+  CStrings:  85216
 
CStrings:
+ "-[CMDeviceStateManager simulateDeviceStateEventForPropertyA:propertyA0:propertyA1:propertyB:propertyC:propertyD:delaySecs:]"
+ "-[CMDeviceStateManagerInternal feedDeviceStateEvent:propertyA0Type:propertyA1Type:propertyBType:propertyCType:propertyDType:timestamp:continuousTimestamp:timestampAPArrivalSecs:]"
+ "-[CMDeviceStateManagerInternal sendEventToClientPrivate]"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CoreLocation/Framework/CoreMotion/DeviceState/CMDeviceStateManager.mm"
+ "Dropping event after teardown in onDeviceStateData:."
+ "First PedNet steps received from AOP2, holding mode,%d,due to active override"
+ "GPSODOM,dropping stale accumulation,gnssOnly,%{public}.1lf,fAccumulatedDeltaDistanceDifferenceM,%{public}.1lf,baselineOffset,%{public}.1lf"
+ "GPSODOM,gnss-only cumulative distance discarded,gnssOnly,%{public}.1lf,fAccumulatedDeltaDistanceDifferenceM,%{public}.1lf,baselineOffset,%{public}.1lf"
+ "GPSODOM,odometer,%{public}.1lf,fAccumulatedDeltaDistanceDifferenceM,%{public}.1lf,baselineOffset,%{public}.1lf,isFromBufferedGnss,%{public}d"
+ "Invalid simulated propertyA value"
+ "Invalid simulated propertyA0 value"
+ "Invalid simulated propertyA1 value"
+ "Invalid simulated propertyB value"
+ "Invalid simulated propertyC value"
+ "Invalid simulated propertyD value"
+ "No internal state, ignoring onNotification."
+ "No internal state, skipping teardown."
+ "No internal state; ignoring startUpdatesPrivateToQueue:withHandler:"
+ "No internal state; ignoring startUpdatesToQueue:withHandler:"
+ "[CMDeviceStateEvent isValidPropertyA:propertyA0]"
+ "[CMDeviceStateEvent isValidPropertyA:propertyA1]"
+ "[CMDeviceStateEvent isValidPropertyA:propertyA]"
+ "[CMDeviceStateEvent isValidPropertyB:propertyB]"
+ "[CMDeviceStateEvent isValidPropertyC:propertyC]"
+ "[CMDeviceStateEvent isValidPropertyD:propertyD]"
+ "isValidPropertyA:"
+ "isValidPropertyB:"
+ "isValidPropertyBAngle:"
+ "isValidPropertyC:"
+ "isValidPropertyD:"
+ "v72@0:8q16q24q32q40q48q56d64"
+ "{\"msg%{public}.0s\":\"Invalid simulated propertyA value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"Invalid simulated propertyA0 value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"Invalid simulated propertyA1 value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"Invalid simulated propertyB value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"Invalid simulated propertyC value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
+ "{\"msg%{public}.0s\":\"Invalid simulated propertyD value\", \"event\":%{public, location:escape_only}s, \"condition\":%{private, location:escape_only}s}"
- "-[CMDeviceStateManager feedDeviceStateEvent:propertyA0Type:propertyA1Type:propertyBType:propertyCType:propertyDType:timestamp:continuousTimestamp:timestampAPArrivalSecs:]_block_invoke"
- "-[CMDeviceStateManager sendEventToClientPrivate]"
- "First PedNet steps received from AOP2, staying in LegacyOnly due to active override"
- "GPSODOM,dropping stale accumulation,gnssOnly,%{public}.1lf"
- "GPSODOM,gnss-only cumulative distance discarded,gnssOnly,%{public}.1lf,accumulated,%{public}.1lf,baselineOffset,%{public}.1lf"
- "GPSODOM,odometer,%.1lf,fAccumulatedDeltaDistanceDifferenceM,%.1lf,baselineOffset,%.1lf,isFromBufferedGnss,%d"
- "fNotifyAllClients"
- "simulateDeviceStateEvent:propertyB:propertyC:delaySecs:"
- "v36@0:8C16C20C24d28"
- "v48@0:8C16C20C24C28C32C36d40"
```
