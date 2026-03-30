## com.apple.driver.ApplePMGR

> `com.apple.driver.ApplePMGR`

```diff

-1774.100.98.0.0
-  __TEXT.__cstring: 0xf3d8
+1774.120.2.0.0
+  __TEXT.__cstring: 0xf5ab
   __TEXT.__const: 0x2b0
-  __TEXT_EXEC.__text: 0x5e848
+  __TEXT_EXEC.__text: 0x5ed34
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x138
   __DATA.__common: 0x5e0

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x40
   __DATA_CONST.__mod_term_func: 0x40
-  __DATA_CONST.__const: 0xb820
+  __DATA_CONST.__const: 0xb838
   __DATA_CONST.__kalloc_type: 0x9c0
-  __DATA_CONST.__kalloc_var: 0xf00
-  UUID: 7CADBEC6-6F39-3DE0-860B-A977B92A02A0
-  Functions: 2790
+  __DATA_CONST.__kalloc_var: 0xfa0
+  UUID: A31F6739-C4AD-3223-9BB6-D82935D5A7EE
+  Functions: 2804
   Symbols:   0
-  CStrings:  1740
+  CStrings:  1751
 
CStrings:
+ "PerfState ApplePMGR::_getPerfDomainCurrentState(PerfDomainID)"
+ "PerfState ApplePMGR::_getPerfDomainDeviceState(PerfDomainID, DeviceID, UInt32)"
+ "SInt32 ApplePMGR::_getPMPDeviceIndex(DeviceID, UInt32)"
+ "_devicePerfStateList"
+ "_devicePerfStateList[i]"
+ "id - kPMPDomainIDBegin < kNumPMPDomains"
+ "id >= kPMPDomainIDBegin"
+ "perf-state-change-enhanced"
+ "pmpDevHandle < MAX_PMP_DEVICE_CNT"
+ "site.UInt32*"
+ "void ApplePMGR::_updatePerfDomainDeviceState(PerfDomainID, PerfState, DeviceID, UInt32)"

```
