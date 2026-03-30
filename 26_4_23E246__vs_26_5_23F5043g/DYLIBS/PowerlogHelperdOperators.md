## PowerlogHelperdOperators

> `/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`

```diff

-3031.102.1.0.0
-  __TEXT.__text: 0x1d6b70
+3031.120.21.0.0
+  __TEXT.__text: 0x1d7450
   __TEXT.__auth_stubs: 0x1b70
-  __TEXT.__objc_methlist: 0xf150
+  __TEXT.__objc_methlist: 0xf1f0
   __TEXT.__const: 0x6c8
   __TEXT.__cstring: 0x24057
   __TEXT.__oslogstring: 0x12db4

   __TEXT.__ustring: 0x10
   __TEXT.__unwind_info: 0x3910
   __TEXT.__objc_classname: 0xc33
-  __TEXT.__objc_methname: 0x32c65
-  __TEXT.__objc_methtype: 0x29c8
-  __TEXT.__objc_stubs: 0x1f560
+  __TEXT.__objc_methname: 0x32f1c
+  __TEXT.__objc_methtype: 0x29d6
+  __TEXT.__objc_stubs: 0x1f720
   __DATA_CONST.__got: 0xec8
   __DATA_CONST.__const: 0x4420
   __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_nlclslist: 0x108
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9c68
+  __DATA_CONST.__objc_selrefs: 0x9ce0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x290
   __DATA_CONST.__objc_arraydata: 0x14bb0
   __AUTH_CONST.__auth_got: 0xdd0
   __AUTH_CONST.__const: 0x18a0
   __AUTH_CONST.__cfstring: 0x31b00
-  __AUTH_CONST.__objc_const: 0x132d0
+  __AUTH_CONST.__objc_const: 0x133f0
   __AUTH_CONST.__objc_intobj: 0x2808
   __AUTH_CONST.__objc_dictobj: 0x34d0
   __AUTH_CONST.__objc_doubleobj: 0xb90
   __AUTH_CONST.__objc_arrayobj: 0x2be0
   __AUTH.__objc_data: 0x938
-  __DATA.__objc_ivar: 0x1340
+  __DATA.__objc_ivar: 0x1358
   __DATA.__data: 0x400
   __DATA.__bss: 0x2350
   __DATA.__common: 0x74

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 6D10F4D7-05E3-3AE7-A65C-FE81A75D610A
-  Functions: 8003
-  Symbols:   27206
-  CStrings:  22671
+  UUID: 7877B297-8FF7-30CE-87DB-C0E1923D26A5
+  Functions: 8016
+  Symbols:   27252
+  CStrings:  22699
 
Symbols:
+ +[PLUtilities bucketForValue:forBucketSize:]
+ -[PLCoalitionSample cpuEnergyWithVouchers]
+ -[PLCoalitionSample cpuEnergyWithoutVouchers]
+ -[PLCoalitionSample cpuTimeWithVouchers]
+ -[PLCoalitionSample cpuTimeWithoutVouchers]
+ -[PLCoalitionSample gpuEnergyWithVouchers]
+ -[PLCoalitionSample gpuEnergyWithoutVouchers]
+ -[PLCoalitionSample setCpuEnergyWithVouchers:]
+ -[PLCoalitionSample setCpuEnergyWithoutVouchers:]
+ -[PLCoalitionSample setCpuTimeWithVouchers:]
+ -[PLCoalitionSample setCpuTimeWithoutVouchers:]
+ -[PLCoalitionSample setGpuEnergyWithVouchers:]
+ -[PLCoalitionSample setGpuEnergyWithoutVouchers:]
+ GCC_except_table144
+ GCC_except_table155
+ GCC_except_table160
+ GCC_except_table199
+ GCC_except_table206
+ GCC_except_table208
+ GCC_except_table83
+ _OBJC_IVAR_$_PLCoalitionSample._cpuEnergyWithVouchers
+ _OBJC_IVAR_$_PLCoalitionSample._cpuEnergyWithoutVouchers
+ _OBJC_IVAR_$_PLCoalitionSample._cpuTimeWithVouchers
+ _OBJC_IVAR_$_PLCoalitionSample._cpuTimeWithoutVouchers
+ _OBJC_IVAR_$_PLCoalitionSample._gpuEnergyWithVouchers
+ _OBJC_IVAR_$_PLCoalitionSample._gpuEnergyWithoutVouchers
+ ___57-[PLPowerMetricMonitorService collectMetricsWithTimeout:]_block_invoke.303
+ ___57-[PLPowerMetricMonitorService collectMetricsWithTimeout:]_block_invoke.303.cold.1
+ ___block_literal_global.313
+ ___block_literal_global.628
+ ___block_literal_global.634
+ ___block_literal_global.974
+ _objc_msgSend$cpuEnergyWithVouchers
+ _objc_msgSend$cpuEnergyWithoutVouchers
+ _objc_msgSend$cpuTimeWithVouchers
+ _objc_msgSend$cpuTimeWithoutVouchers
+ _objc_msgSend$gpuEnergyWithVouchers
+ _objc_msgSend$gpuEnergyWithoutVouchers
+ _objc_msgSend$setCpuEnergyWithVouchers:
+ _objc_msgSend$setCpuEnergyWithoutVouchers:
+ _objc_msgSend$setCpuSecondsWithVouchers:
+ _objc_msgSend$setCpuSecondsWithoutVouchers:
+ _objc_msgSend$setCpuTimeWithVouchers:
+ _objc_msgSend$setCpuTimeWithoutVouchers:
+ _objc_msgSend$setGpuEnergyWithVouchers:
+ _objc_msgSend$setGpuEnergyWithoutVouchers:
- GCC_except_table120
- GCC_except_table148
- GCC_except_table187
- GCC_except_table194
- GCC_except_table196
- GCC_except_table71
- ___57-[PLPowerMetricMonitorService collectMetricsWithTimeout:]_block_invoke.273
- ___57-[PLPowerMetricMonitorService collectMetricsWithTimeout:]_block_invoke.273.cold.1
- ___block_literal_global.281
- ___block_literal_global.283
- ___block_literal_global.595
- ___block_literal_global.598
- ___block_literal_global.604
- ___block_literal_global.972
CStrings:
+ "TQ,V_cpuEnergyWithVouchers"
+ "TQ,V_cpuEnergyWithoutVouchers"
+ "TQ,V_cpuTimeWithVouchers"
+ "TQ,V_cpuTimeWithoutVouchers"
+ "TQ,V_gpuEnergyWithVouchers"
+ "TQ,V_gpuEnergyWithoutVouchers"
+ "_cpuEnergyWithVouchers"
+ "_cpuEnergyWithoutVouchers"
+ "_cpuTimeWithVouchers"
+ "_cpuTimeWithoutVouchers"
+ "_gpuEnergyWithVouchers"
+ "_gpuEnergyWithoutVouchers"
+ "bucketForValue:forBucketSize:"
+ "cpuEnergyWithVouchers"
+ "cpuEnergyWithoutVouchers"
+ "cpuTimeWithVouchers"
+ "cpuTimeWithoutVouchers"
+ "gpuEnergyWithVouchers"
+ "gpuEnergyWithoutVouchers"
+ "q28@0:8q16i24"
+ "setCpuEnergyWithVouchers:"
+ "setCpuEnergyWithoutVouchers:"
+ "setCpuSecondsWithVouchers:"
+ "setCpuSecondsWithoutVouchers:"
+ "setCpuTimeWithVouchers:"
+ "setCpuTimeWithoutVouchers:"
+ "setGpuEnergyWithVouchers:"
+ "setGpuEnergyWithoutVouchers:"

```
