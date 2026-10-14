## dasd

> `/usr/libexec/dasd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
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
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-2467.40.47.0.0
-  __TEXT.__text: 0x1766e4
+2467.40.49.0.0
+  __TEXT.__text: 0x176ab0
   __TEXT.__auth_stubs: 0x2280
-  __TEXT.__objc_stubs: 0x1b540
-  __TEXT.__objc_methlist: 0x1346c
-  __TEXT.__const: 0x1588
-  __TEXT.__objc_methname: 0x2ee35
-  __TEXT.__cstring: 0x10886
-  __TEXT.__oslogstring: 0x17379
+  __TEXT.__objc_stubs: 0x1b600
+  __TEXT.__objc_methlist: 0x135b4
+  __TEXT.__const: 0x1598
+  __TEXT.__objc_methname: 0x2f525
+  __TEXT.__cstring: 0x10aa6
+  __TEXT.__oslogstring: 0x173b9
   __TEXT.__objc_classname: 0x1cd8
   __TEXT.__objc_methtype: 0x42e1
   __TEXT.__gcc_except_tab: 0x5044

   __TEXT.__swift_as_cont: 0x80
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x65b0
+  __TEXT.__unwind_info: 0x65b8
   __TEXT.__eh_frame: 0xbd0
   __DATA_CONST.__const: 0x5038
-  __DATA_CONST.__cfstring: 0x11ca0
+  __DATA_CONST.__cfstring: 0x11e20
   __DATA_CONST.__objc_classlist: 0x710
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x220

   __DATA_CONST.__auth_got: 0x1150
   __DATA_CONST.__got: 0xe50
   __DATA_CONST.__auth_ptr: 0x190
-  __DATA.__objc_const: 0x34450
-  __DATA.__objc_selrefs: 0x9ea0
-  __DATA.__objc_ivar: 0x1654
+  __DATA.__objc_const: 0x34690
+  __DATA.__objc_selrefs: 0x9f90
+  __DATA.__objc_ivar: 0x1684
   __DATA.__objc_data: 0x4958
   __DATA.__data: 0x2200
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 8447
+  Functions: 8474
   Symbols:   1023
-  CStrings:  12585
+  CStrings:  12652
 
CStrings:
+ "IdleStack thermal max (start/run): low %d/%d, medium %d/%d, high %d/%d"
+ "PolicyDeviceActivityIdleStackHighBlockRunOnEarlyThermal"
+ "PolicyDeviceActivityIdleStackHighBlockStartOnEarlyThermal"
+ "PolicyDeviceActivityIdleStackLowBlockRunOnEarlyThermal"
+ "PolicyDeviceActivityIdleStackLowBlockStartOnEarlyThermal"
+ "PolicyDeviceActivityIdleStackMediumBlockRunOnEarlyThermal"
+ "PolicyDeviceActivityIdleStackMediumBlockStartOnEarlyThermal"
+ "PolicyThermalIdleStackHighMaxAllowableToRun"
+ "PolicyThermalIdleStackHighMaxAllowableToStart"
+ "PolicyThermalIdleStackLowMaxAllowableToRun"
+ "PolicyThermalIdleStackLowMaxAllowableToStart"
+ "PolicyThermalIdleStackMediumMaxAllowableToRun"
+ "PolicyThermalIdleStackMediumMaxAllowableToStart"
+ "TB,N,V_idleStackHighBlockRunOnEarlyThermal"
+ "TB,N,V_idleStackHighBlockStartOnEarlyThermal"
+ "TB,N,V_idleStackLowBlockRunOnEarlyThermal"
+ "TB,N,V_idleStackLowBlockStartOnEarlyThermal"
+ "TB,N,V_idleStackMediumBlockRunOnEarlyThermal"
+ "TB,N,V_idleStackMediumBlockStartOnEarlyThermal"
+ "Ti,N,V_idleStackHighRunMax"
+ "Ti,N,V_idleStackHighStartMax"
+ "Ti,N,V_idleStackLowRunMax"
+ "Ti,N,V_idleStackLowStartMax"
+ "Ti,N,V_idleStackMediumRunMax"
+ "Ti,N,V_idleStackMediumStartMax"
+ "_idleStackHighBlockRunOnEarlyThermal"
+ "_idleStackHighBlockStartOnEarlyThermal"
+ "_idleStackHighRunMax"
+ "_idleStackHighStartMax"
+ "_idleStackLowBlockRunOnEarlyThermal"
+ "_idleStackLowBlockStartOnEarlyThermal"
+ "_idleStackLowRunMax"
+ "_idleStackLowStartMax"
+ "_idleStackMediumBlockRunOnEarlyThermal"
+ "_idleStackMediumBlockStartOnEarlyThermal"
+ "_idleStackMediumRunMax"
+ "_idleStackMediumStartMax"
+ "activityTransferSize == %lu"
+ "boolTrialFactor:default:"
+ "idleStackHighBlockRunOnEarlyThermal"
+ "idleStackHighBlockStartOnEarlyThermal"
+ "idleStackHighRunMax"
+ "idleStackHighStartMax"
+ "idleStackLowBlockRunOnEarlyThermal"
+ "idleStackLowBlockStartOnEarlyThermal"
+ "idleStackLowRunMax"
+ "idleStackLowStartMax"
+ "idleStackMaxAllowableForActivity:"
+ "idleStackMediumBlockRunOnEarlyThermal"
+ "idleStackMediumBlockStartOnEarlyThermal"
+ "idleStackMediumRunMax"
+ "idleStackMediumStartMax"
+ "isHighPriorityIdleStackTask"
+ "isMediumPriorityIdleStackTask"
+ "rawTrialLevelForFactor:"
+ "setIdleStackHighBlockRunOnEarlyThermal:"
+ "setIdleStackHighBlockStartOnEarlyThermal:"
+ "setIdleStackHighRunMax:"
+ "setIdleStackHighStartMax:"
+ "setIdleStackLowBlockRunOnEarlyThermal:"
+ "setIdleStackLowBlockStartOnEarlyThermal:"
+ "setIdleStackLowRunMax:"
+ "setIdleStackLowStartMax:"
+ "setIdleStackMediumBlockRunOnEarlyThermal:"
+ "setIdleStackMediumBlockStartOnEarlyThermal:"
+ "setIdleStackMediumRunMax:"
+ "setIdleStackMediumStartMax:"
+ "shouldBlockIdleStackActivityOnEarlyThermal:withContext:"
+ "\x87"
- " Size %lu upload:%d, [wifiLQM] Required=%ld, Observed=%ld, [cellLQM] Required=%ld Observed=%ld\n"
- "W"
```
