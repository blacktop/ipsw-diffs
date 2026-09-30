## com.apple.driver.AppleT8140MCC

> `com.apple.driver.AppleT8140MCC`

```diff

-43.100.13.0.0
+78.0.0.0.0
   __TEXT.__const: 0x48
-  __TEXT.__cstring: 0x5024
-  __TEXT.__os_log: 0x2118
-  __TEXT_EXEC.__text: 0x150d4
+  __TEXT.__cstring: 0x5194
+  __TEXT.__os_log: 0x2135
+  __TEXT_EXEC.__text: 0x15680
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x7eb0
   __DATA.__common: 0x1c8
   __DATA.__bss: 0x54
-  __DATA_CONST.__auth_got: 0x2c0
+  __DATA_CONST.__auth_got: 0x2d8
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x3040
+  __DATA_CONST.__const: 0x30d0
   __DATA_CONST.__kalloc_type: 0x400
   __DATA_CONST.__kalloc_var: 0x50
-  UUID: C119C66B-A78E-3765-A566-A463BDD341FC
-  Functions: 507
+  UUID: C7FBED0A-5D47-3E65-848C-0C0507EED9AC
+  Functions: 515
   Symbols:   0
-  CStrings:  833
+  CStrings:  845
 
CStrings:
+ "\"%s: \" \"Failed to read ptd-range-ctrl2drv property\" @%s:%d"
+ "\"%s: \" \"Failed to read ptd-range-drv2ctrl property\" @%s:%d"
+ "%s:%d: DRAMECC: PA received is 0x%lx\n\n"
+ "%s:%d: DRAMECC: register error injection for ecc\n"
+ "%s:%d: _amccNum = %d _planeNumPerAMCC = %d _maxWayCount = %d\n"
+ "121111121222121211111111111111111111111112111111111111111111111111111111111111111111111111111111111111111111121111111212111112111222222222221111111211111211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211212121212"
+ "DRAMECC: PA received is 0x%lx\n"
+ "DRAMECC: register error injection for ecc"
+ "IODeviceTree:/arm-io/pmp0/iop-pmp0-nub"
+ "_amccNum = %d _planeNumPerAMCC = %d _maxWayCount = %d"
+ "dcs_error_inject"
+ "kANE_ANE1_IntermediateSpillsHi"
+ "kANE_ANE1_IntermediateSpillsLo"
+ "kANE_ANE_BondedIntermediateSpillsLo"
+ "kANE_BondedIntermediateSpillsHi"
+ "kANE_BondedKernelReads"
+ "kISP_ClrProcTSegDmaDstWSeg"
+ "max-way-count"
- "%s:%d: Failed to get PTD indices for driver to control communication\n"
- "%s:%d: _amccNum = %d _planeNumPerAMCC = %d\n"
- "12111112122212121111111111111111111111111211111111111111111111111111111111111111111111111111111111111111111112111111121211111211122222222221111111211111211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211212121212"
- "Failed to get PTD indices for driver to control communication"
- "IODeviceTree:/arm-io/pmp/iop-pmp0-nub"
- "_amccNum = %d _planeNumPerAMCC = %d"

```
