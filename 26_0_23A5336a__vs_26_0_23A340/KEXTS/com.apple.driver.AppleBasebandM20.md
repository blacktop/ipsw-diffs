## com.apple.driver.AppleBasebandM20

> `com.apple.driver.AppleBasebandM20`

```diff

 1031.0.0.0.0
   __TEXT.__const: 0x435
-  __TEXT.__cstring: 0x9960
-  __TEXT.__os_log: 0x8c9a
-  __TEXT_EXEC.__text: 0x4aa08
+  __TEXT.__cstring: 0xa16a
+  __TEXT.__os_log: 0x9657
+  __TEXT_EXEC.__text: 0x4e228
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x190
   __DATA.__common: 0x2c8

   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__mod_init_func: 0x90
   __DATA_CONST.__mod_term_func: 0x90
-  __DATA_CONST.__const: 0x6398
+  __DATA_CONST.__const: 0x63d8
   __DATA_CONST.__kalloc_type: 0x580
   __DATA_CONST.__kalloc_var: 0x320
-  UUID: D47C17CF-C06D-3ADA-B5DF-504CF9BCE872
-  Functions: 822
+  UUID: FE9778BB-B4E4-32C3-A1C9-2FF072CBB61A
+  Functions: 831
   Symbols:   0
-  CStrings:  1405
+  CStrings:  1466
 
CStrings:
+ "%06ld.%06d %s::%s: \tPower estimation - 1 millisecond average power: %umW\n"
+ "%06ld.%06d %s::%s: \tPower estimation - 1 second average power: %umW\n"
+ "%06ld.%06d %s::%s: \tPower estimation - 100 millisecond average power: %umW\n"
+ "%06ld.%06d %s::%s: \tPower estimation - thermal 1 average power: %umW\n"
+ "%06ld.%06d %s::%s: \tPower estimation - thermal 2 average power: %umW\n"
+ "%06ld.%06d %s::%s: \tPower estimation - thermal 3 average power: %umW\n"
+ "%06ld.%06d %s::%s: \tPower estimation - thermal 4 average power: %umW\n"
+ "%06ld.%06d %s::%s: \tPower measurement - averaged power: %umW\n"
+ "%06ld.%06d %s::%s: \tThermal sensor ID %u, value: %u\n"
+ "%06ld.%06d %s::%s: AP awake interrupt triggered successfully\n"
+ "%06ld.%06d %s::%s: AP sleep interrupt triggered successfully, detaching all SPMI interrupts now\n"
+ "%06ld.%06d %s::%s: Billboard message CRC calculation: %u\n"
+ "%06ld.%06d %s::%s: Expecting the baseband OCP sequence number to be %d, and received %u\n"
+ "%06ld.%06d %s::%s: Failed to trigger AP awake interrupt, ret = 0x%x\n"
+ "%06ld.%06d %s::%s: Failed to trigger AP sleep interrupt, ret = 0x%x\n"
+ "%06ld.%06d %s::%s: OCP Magic Word does not match! OCP Magic Word: (0x%x)(expect: 0x%x) (0x%x)(expect: 0x%x) (0x%x)(expect: 0x%x)\n"
+ "%06ld.%06d %s::%s: Received NULL OCP data\n"
+ "%06ld.%06d %s::%s: Received power estimation report\n"
+ "%06ld.%06d %s::%s: Received power measurement report\n"
+ "%06ld.%06d %s::%s: Received thermal data report\n"
+ "%06ld.%06d %s::%s: Update report is not supported for this vendor\n"
+ "%06ld.%06d %s::%s: [%s] The OCP buffer payload length (%u) should not be beyond %u\n"
+ "%06ld.%06d %s::%s: [%s] baseband OCP sequence number is %u while expecting number %u. Updating the next expecting number to %u\n"
+ "%s: %s fired with NULL transport object\n"
+ "%s: AppleBasebandSPMITransport: %s fired!\n"
+ "Billboard INIT_DONE interrupt"
+ "Billboard TX_DONE interrupt"
+ "Billboard TX_START interrupt"
+ "Billboard WAKE_DONE interrupt"
+ "billboardTransactionFailure"
+ "checkOCPPacketValidDAL"
+ "readyToFillTimerExpired"
+ "setThermalPowerReportDalGated"
+ "setThermalPowerReportDal_block_invoke"
+ "updateConfigs_block_invoke"
+ "wakeDoneTimerExpired"

```
