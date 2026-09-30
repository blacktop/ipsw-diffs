## com.apple.driver.AppleBasebandM20

> `com.apple.driver.AppleBasebandM20`

```diff

-1054.0.0.0.0
+1114.0.0.0.0
   __TEXT.__const: 0x39d sha256:39515daf3ac3cb9808d25c373e1b6a4ae04ae009233ff4d14252ffaf430fb65a
-  __TEXT.__cstring: 0xa28e sha256:24c51821b1e5ed534889cb93c4d88cdabbfbfb1bd4ffa467f21f59a6795a652e
-  __TEXT.__os_log: 0x9762 sha256:cff5711adabeb96cc36f22b1707e3f1ae6344ca2fcf7bfc1d10dd910fc5c3f62
-  __TEXT_EXEC.__text: 0x48aac sha256:b8ea1085dca218d5ff994aef245bf1ba6ffb49c876777a4ac859854ceb072de2
+  __TEXT.__cstring: 0xa534 sha256:5deebe3f63e837f1dfb185adde664f8b5812993ee8ce37fc45e27ef4e3ae127d
+  __TEXT.__os_log: 0x9998 sha256:bc53714ed3615d29d194c4a38b78fde5c06fbef329aca95a932bc097f7e54549
+  __TEXT_EXEC.__text: 0x49784 sha256:5c6cabf00403ae5e2c19fbcded2591ae23589380aebddb5d8299afecf8fb1b05
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x190 sha256:0510b42eaaffe455f2c23f67b414f81de1c4402a44941e9ce1164dee7dc5f360
+  __DATA.__data: 0x1d8 sha256:ccf1173d53e68a85b4985034e17ef135178ae146a4b45660598619893fe640ba
   __DATA.__common: 0x2c8 sha256:283de789c3f9ae6115e627ecb921b7b39bdaa1b82289eca5e60da0b76d07a502
   __DATA.__bss: 0x2d1 sha256:0782dfda506cb45fd2541d473b203e3902e9affb4eae0c4dbf4e9b10b792e71f
-  __DATA_CONST.__auth_got: 0x2c0 sha256:e2edc696be28643536f695f413f7b3434fbcb9a0939d6007bcb2cfad5576c844
-  __DATA_CONST.__got: 0xb8 sha256:05b7e74241dc718f0f22573ece3b9a19d1956911eaef341bbaa80279f39d62ae
-  __DATA_CONST.__mod_init_func: 0x90 sha256:0899902801b69219fd18b9f84994077bd99e6a19aaab4ee34c4dc3d9713817e6
-  __DATA_CONST.__mod_term_func: 0x90 sha256:958e16ed6125219b554dd85338def50eab12e65e1231697b131ec3979949b49c
-  __DATA_CONST.__const: 0x63d8 sha256:27ff0a50d8641fc3528844926a34e7e94710133205367bf300d9208a94a7ff57
-  __DATA_CONST.__kalloc_type: 0x580 sha256:0d4a0f22db919a357c2b8e25389489755b1854c7d516466e0e6e7167790ee2ca
-  __DATA_CONST.__kalloc_var: 0x320 sha256:5eb11310d8b6816cea319045577b8cc3638e677fff249d182b91fce10ab007cb
-  UUID: ADADDCB1-9B1A-382A-A7DF-D2CC85B9A5EF
-  Functions: 839
+  __DATA_CONST.__mod_init_func: 0x90 sha256:ef3f7ad8890edbb6fdc45276d375072b5027259d90fa241023127b29cc2a482a
+  __DATA_CONST.__mod_term_func: 0x90 sha256:82da31440b3ff70a19957882935ead419a5005b6448a5776c599e69bbc0b5677
+  __DATA_CONST.__const: 0x6418 sha256:248648b06e8ee42131099efd21da989f6f56bd49c44851336132d3c35512f6e8
+  __DATA_CONST.__kalloc_type: 0x580 sha256:19a0439d532f8848c533d6b032a5ef03dcb61b81ab05598a43e5f4dbb489d7df
+  __DATA_CONST.__kalloc_var: 0x3c0 sha256:30e2fdb3d610dcdf52684a0ec07dc8d17749c7eca10c8c55ab8b3d535550d56f
+  __DATA_CONST.__auth_got: 0x2c0 sha256:b8c9ce45f8ef0559e405a5dbcbf848cb548f5d8bd9fde8cdfd75e42ae2ba2a7c
+  __DATA_CONST.__got: 0xb8 sha256:c79653df379f86a90ea2b3f3792966ea23239ad7990af1550e06261cf3dbe9ce
+  UUID: 6B570852-C62A-3F6E-87BC-D0129F5563FB
+  Functions: 843
   Symbols:   0
-  CStrings:  1473
+  CStrings:  1497
 
CStrings:
+ "%06ld.%06d %s::%s: Baseband reset detected but endpoint is missing! Ignoring...\n"
+ "%06ld.%06d %s::%s: Loaded baseband-no-toggle-vdd-clk=%u\n"
+ "%06ld.%06d %s::%s: baseband device ID = %u\n"
+ "%06ld.%06d %s::%s: fix device tree property \"radio-devid-chipid-map\"; choosing static mappings"
+ "%06ld.%06d %s::%s: invalid baseband device ID = %u\n"
+ "%06ld.%06d %s::%s: property \"radio-devid-chipid-map\" devid %x, chipid %x\n"
+ "%s: %s failed to allocate deviceIDmap\n"
+ "%s: property \"radio-devid-chipid-map\" does not have the expected type. it is a %s\n\n"
+ "454"
+ "549"
+ "564"
+ "630"
+ "638"
+ "661"
+ "BasebandChipID"
+ "BasebandDeviceID"
+ "BasebandRadioType"
+ "baseband-no-toggle-vdd-clk"
+ "isInt1"
+ "radio-devid-chipid-map"
+ "resetDetectInterrupt"
+ "site.struct deviceIDmap"
- "356"
- "451"
- "466"
- "532"
- "540"
- "563"

```
