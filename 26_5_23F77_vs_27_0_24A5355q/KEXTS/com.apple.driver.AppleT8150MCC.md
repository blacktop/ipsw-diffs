## com.apple.driver.AppleT8150MCC

> `com.apple.driver.AppleT8150MCC`

```diff

-78.100.14.0.0
-  __TEXT.__cstring: 0x5545 sha256:1adcb7d7a82d6fc84e36062443e4b258a4e5a79e4ee35b06280135328aecbee0
-  __TEXT.__os_log: 0x2259 sha256:fb9709bbd7b40cded68399cc0b39897186309d395d3d6723870403c7f326e16b
-  __TEXT.__const: 0x50 sha256:a1b334a1f613a2e91da10c45d129b957e6c8717211562bd8cbc319a27b26bf69
-  __TEXT_EXEC.__text: 0x14e14 sha256:9d9ea9c54d71530eae7835ba3759fbdda341aaa0c867b6fccb27c2c4c840b429
+120.0.0.0.0
+  __TEXT.__const: 0x50 sha256:d286682f23a67ee50eff5899c281dd20cd1cdf36757f3e052cd40ea84e0d7840
+  __TEXT.__cstring: 0x5833 sha256:aa9f926ea85d755a3f9822b368e68e02b0e29e9b2b7766e0ca0bfbf928678aa8
+  __TEXT.__os_log: 0x244a sha256:600c53f3efab43f4e4efe945b56e21c528a20cfbb2d194b788ff482e3481cb69
+  __TEXT_EXEC.__text: 0x15bd0 sha256:b8fb456932f0e59794e943695d588c32a6eb632a3cb39d154996c7d7cd12ccb2
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x8b70 sha256:75223dd00ed6e231494c48b6553513eb4e5220054ea49c8c13973c9b2cc4c4ef
-  __DATA.__common: 0x1c8 sha256:b960fb5cb94682dfc4a873035d65f8befdcb9bed0e7db0feb905f0dcf437b38c
+  __DATA.__data: 0x9130 sha256:d50536b0a545a1177bd5135a66c6c25ed0c30f25fc738732f22c8e8d223eb4c9
+  __DATA.__common: 0x1f0 sha256:882993b55cc0c527f0a6059b69b3faf4ef3ccb9cecd3d8847ca0e49a1444debe
   __DATA.__bss: 0x54 sha256:4fea5e6a3ec5f5474a26d858bc77b6d7bd3ab864ea02d988683fdc648602b248
-  __DATA_CONST.__auth_got: 0x2d8 sha256:0c9304450de1677edc022f5fce2f7c059a7ee9c902769f96c363439c270e5de8
-  __DATA_CONST.__got: 0xc0 sha256:7a02747b0ed5d240203373a59e37bd7292c1d80f1a960e730380135e2ce41533
-  __DATA_CONST.__mod_init_func: 0x20 sha256:7092e45da6db30864e23548d156b675eb10b0a6786091efcbff06fd58b3a2028
-  __DATA_CONST.__mod_term_func: 0x20 sha256:b6dbd8d1725ace261cf5e2e53594943a0cc6a646d9e3eca001fcdac6e3d3cd15
-  __DATA_CONST.__const: 0x3100 sha256:66abfc8be0e4cc1306fed169a97e14ab44b225df8365e9de17037ef148075cfb
-  __DATA_CONST.__kalloc_type: 0x400 sha256:c785e11c2dd30fdd64819d64598af818c38f68d45a8f370a315375fce9ab00c1
-  __DATA_CONST.__kalloc_var: 0x50 sha256:a721d6e7a6d6df6b61c6d03f2966c9561dbfc3c8ed7fd18a09a978998d5b250a
-  UUID: 1F0C80A1-6BFD-3BAB-B9B5-C56A98CF7A03
-  Functions: 526
+  __DATA_CONST.__mod_init_func: 0x20 sha256:d3a6f652b6f61a227472afb943e6b27d3da4ef5f5bfcb1fda78f596e4ce786fc
+  __DATA_CONST.__mod_term_func: 0x20 sha256:82bcb7d40df7d9b3ce8c2d4ce81241ef5c4eff0fe4fc63da8904eed9b1b425b4
+  __DATA_CONST.__const: 0x3370 sha256:5677ddee64c66c393b4f9de331e598be8b88e4ca909598d06de7ba5aa3cfff9c
+  __DATA_CONST.__kalloc_type: 0x440 sha256:6066fc27bbea0fbb14f3bd7f05e11d4e645600eca36794c1f66cfdcef6d332f4
+  __DATA_CONST.__kalloc_var: 0x140 sha256:14d0bc6c64eba5ac6ab80eda108cec86b49df24f572f681fcb02fd8da914c1fd
+  __DATA_CONST.__auth_got: 0x2d8 sha256:043f34c3f5dbbea5a03acca1cc35d3e82d348be327ba997967488490328d9f93
+  __DATA_CONST.__got: 0xc0 sha256:4d1cc04eab6d4a6bc3da864e3185775df14f1fbd18931b091dd82c85a0a5edf5
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
