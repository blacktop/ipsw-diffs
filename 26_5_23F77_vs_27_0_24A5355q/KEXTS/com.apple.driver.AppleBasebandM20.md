## com.apple.driver.AppleBasebandM20

> `com.apple.driver.AppleBasebandM20`

```diff

-1054.0.0.0.0
+1114.0.0.0.0
   __TEXT.__const: 0x39d
-  __TEXT.__cstring: 0xa28e
-  __TEXT.__os_log: 0x9762
-  __TEXT_EXEC.__text: 0x48aac
+  __TEXT.__cstring: 0xa534
+  __TEXT.__os_log: 0x9998
+  __TEXT_EXEC.__text: 0x49784
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x190
+  __DATA.__data: 0x1d8
   __DATA.__common: 0x2c8
   __DATA.__bss: 0x2d1
-  __DATA_CONST.__auth_got: 0x2c0
-  __DATA_CONST.__got: 0xb8
   __DATA_CONST.__mod_init_func: 0x90
   __DATA_CONST.__mod_term_func: 0x90
-  __DATA_CONST.__const: 0x63d8
+  __DATA_CONST.__const: 0x6418
   __DATA_CONST.__kalloc_type: 0x580
-  __DATA_CONST.__kalloc_var: 0x320
-  UUID: ADADDCB1-9B1A-382A-A7DF-D2CC85B9A5EF
-  Functions: 839
+  __DATA_CONST.__kalloc_var: 0x3c0
+  __DATA_CONST.__auth_got: 0x2c0
+  __DATA_CONST.__got: 0xb8
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
