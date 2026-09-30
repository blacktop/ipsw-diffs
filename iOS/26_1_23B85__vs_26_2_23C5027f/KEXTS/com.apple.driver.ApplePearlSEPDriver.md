## com.apple.driver.ApplePearlSEPDriver

> `com.apple.driver.ApplePearlSEPDriver`

```diff

-873.40.8.0.0
+873.60.2.0.0
   __TEXT.__const: 0x318
-  __TEXT.__cstring: 0xa805
-  __TEXT.__os_log: 0x48b0
-  __TEXT_EXEC.__text: 0x402c4
+  __TEXT.__cstring: 0xa847
+  __TEXT.__os_log: 0x48ed
+  __TEXT_EXEC.__text: 0x403dc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xcd
   __DATA.__common: 0x1d8

   __DATA_CONST.__const: 0x2050
   __DATA_CONST.__kalloc_type: 0x580
   __DATA_CONST.__kalloc_var: 0x1e0
-  UUID: 540F79AD-D470-32A0-B1F9-1416509586A8
-  Functions: 624
+  UUID: A570D954-16D9-38BE-BBE4-30A0F0FFC5FD
+  Functions: 623
   Symbols:   0
-  CStrings:  1663
+  CStrings:  1668
 
CStrings:
+ "%s <- caller:%s, cancelTimeout:%d\n"
+ "%s <- caller:%s, timeoutMs:%u\n"
+ "%s <- lock:%d\n"
+ "delayedHoldMatchEventCancel"
+ "delayedHoldMatchEventSchedule"
+ "unknown"
- "%s <- ApplePearlSEPDriver::sendMatchResultToClients (%d)\n"

```
