## com.apple.driver.AppleT8150MCC

> `com.apple.driver.AppleT8150MCC`

```diff

-78.100.14.0.0
-  __TEXT.__cstring: 0x5545
-  __TEXT.__os_log: 0x2259
+120.0.0.0.0
   __TEXT.__const: 0x50
-  __TEXT_EXEC.__text: 0x14e14
+  __TEXT.__cstring: 0x5833
+  __TEXT.__os_log: 0x244a
+  __TEXT_EXEC.__text: 0x15bd0
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x8b70
-  __DATA.__common: 0x1c8
+  __DATA.__data: 0x9130
+  __DATA.__common: 0x1f0
   __DATA.__bss: 0x54
-  __DATA_CONST.__auth_got: 0x2d8
-  __DATA_CONST.__got: 0xc0
   __DATA_CONST.__mod_init_func: 0x20
   __DATA_CONST.__mod_term_func: 0x20
-  __DATA_CONST.__const: 0x3100
-  __DATA_CONST.__kalloc_type: 0x400
-  __DATA_CONST.__kalloc_var: 0x50
-  UUID: 1F0C80A1-6BFD-3BAB-B9B5-C56A98CF7A03
-  Functions: 526
+  __DATA_CONST.__const: 0x3370
+  __DATA_CONST.__kalloc_type: 0x440
+  __DATA_CONST.__kalloc_var: 0x140
+  __DATA_CONST.__auth_got: 0x2d8
+  __DATA_CONST.__got: 0xc0
+  UUID: C04C3CAD-8782-39E7-800A-69B98859101B
+  Functions: 562
   Symbols:   0
-  CStrings:  871
+  CStrings:  903
 
CStrings:
+ "  Counter[%d]: type=%d, idx=%d, blkNum=%d, valOffset=0x%x, totalValue=0x%llx\n"
+ "\"%s: \" \"AMCC aperture 0 not mapped correctly\" @%s:%d"
+ "\"%s: \" \"DCS aperture 0 not mapped correctly\" @%s:%d"
+ "\"%s: \" \"Failed to allocate AMCC aperture array (count: %d)\" @%s:%d"
+ "\"%s: \" \"Failed to allocate DCS aperture array (count: %d)\" @%s:%d"
+ "\"%s: \" \"Failed to allocate SoCNI aperture array (count: %d)\" @%s:%d"
+ "%s:%d:   Counter[%d]: type=%d, idx=%d, blkNum=%d, valOffset=0x%x, totalValue=0x%llx\n\n"
+ "%s:%d: DRAMECC: Not able to get dcs hashing result. Aborting error injection\n\n"
+ "%s:%d: DRAMECC: amccInstance %u dcsNumber %u\n\n"
+ "%s:%d: DSID management is disabled, but streams are loaded for enumeration\n"
+ "%s:%d: Invalid arguments. param1:%p param2:%p\n\n"
+ "%s:%d: Invalid counter type: %d for perfCounterId: %d\n\n"
+ "%s:%d: Invalid perfCounterId: %d (max: %d)\n\n"
+ "%s:%d: SoCNI does not exist for this SoC. Setting _socniApertureCnt to 0x0\n"
+ "%s:%d: readPerfCounterByID: perfCounterId=%d, type=%d, aggregateCount=%d, finalValue=0x%llx\n\n"
+ "112"
+ "1211111212221212111111111111111111111111112111111111111111111111111111111111111111111111111111111111111111111111111111211111112121111121"
+ "1211111212221212111111111111111111111111112111111111111111111111111111111111111111111111111111111111111111111111111111211111112121111121112222222222211111112111121211121212121212"
+ "122222112122211111111111111111111111111111111111111111111111111111111111111111111111111211122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
+ "AppleAMCPerfFunction"
+ "DRAMECC: Not able to get dcs hashing result. Aborting error injection\n"
+ "DRAMECC: amccInstance %u dcsNumber %u\n"
+ "DSID management is disabled, but streams are loaded for enumeration"
+ "Invalid arguments. param1:%p param2:%p\n"
+ "Invalid counter type: %d for perfCounterId: %d\n"
+ "Invalid perfCounterId: %d (max: %d)\n"
+ "SoCNI does not exist for this SoC. Setting _socniApertureCnt to 0x0"
+ "dcs-reg-idx"
+ "dram-ecc"
+ "getAmccInstance"
+ "kReserved0"
+ "kReserved1"
+ "kReserved2"
+ "kReserved3"
+ "kReserved4"
+ "kReserved5"
+ "kReserved6"
+ "kReserved7"
+ "kReserved8"
+ "readPerfCounterByID"
+ "readPerfCounterByID: perfCounterId=%d, type=%d, aggregateCount=%d, finalValue=0x%llx\n"
+ "site.AppleAMCPerfFunction"
+ "site.mem_aperture_t"
- "\"%s: \" \"Failed to read socni-count property\" @%s:%d"
- "\"%s: \" \"Register read failure. Requested instance:%d\\n\" @%s:%d"
- "\"%s: \" \"Register write failure. Requested instance:%d\\n\" @%s:%d"
- "\"%s: \" \"Unexpected number of apertures(%d) for property %s\" @%s:%d"
- "%s:%d: AMCCDCSOffset = %x\n"
- "%s:%d: AMCCDCSStride = %x\n"
- "12111112122212121111111111111111111111111121111111111111111111111111111111111111111111111111111111111111111111211111112121111121"
- "12111112122212121111111111111111111111111121111111111111111111111111111111111111111111111111111111111111111111211111112121111121112222222222221111111211111211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211211212121212"
- "1222221121222111111111111111111111111111111111111111111111111111111111111111111211122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222"
- "AMCCDCSOffset = %x"
- "AMCCDCSStride = %x"

```
