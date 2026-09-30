## com.apple.driver.AppleSARService

> `com.apple.driver.AppleSARService`

```diff

-1380.0.0.0.0
-  __TEXT.__os_log: 0xf0f3
+1384.1.0.0.0
+  __TEXT.__os_log: 0xf1ea
   __TEXT.__const: 0xfd8
-  __TEXT.__cstring: 0xd97b
-  __TEXT_EXEC.__text: 0x71e50
+  __TEXT.__cstring: 0xdab4
+  __TEXT_EXEC.__text: 0x72174
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x128
   __DATA.__common: 0x638

   __DATA_CONST.__got: 0xa8
   __DATA_CONST.__mod_init_func: 0x60
   __DATA_CONST.__mod_term_func: 0x68
-  __DATA_CONST.__const: 0x5868
+  __DATA_CONST.__const: 0x5838
   __DATA_CONST.__kalloc_type: 0x3e00
   __DATA_CONST.__kalloc_var: 0x190
-  UUID: D966FE29-FD8E-35AF-B927-9828C2DB7C89
-  Functions: 646
+  UUID: BB56D178-0566-3884-A92F-481CFA8BDD1A
+  Functions: 642
   Symbols:   0
-  CStrings:  1756
+  CStrings:  1767
 
CStrings:
+ "#D: %s::%s:%d: Reported Cellular SAR Boost"
+ "%s::%s:%d: Failed to create the CA report timer"
+ "%s::%s:%d: Failed to send boost signal to connectivity"
+ "%s::%s:%d: Failed to send boost signal to modem"
+ "%s::%s:%d: Invalid timer or workloop in callback"
+ "%s::%s:%d: Reporting timer has already started"
+ "%s::%s:%d: Sending Budget to modem: Sem: %u, Seq: %u, SAR Budget: %s W/kg, SAR Budget Cluster[0]: %s W/kg, SAR Budget Cluster[1]: %s W/kg, MPE Budget: %s mW/cm^2, Period: %u seconds, Operating Mode: %s, SAR Budget Cluster[2]: %s W/kg, SAR Budget Cluster[3]: %s W/kg, TER Consumed (Average): %u %%"
+ "%s::%s:%d: Triggering coredump due to an SPMI error\n"
+ "com.apple.Telephony.cellularSarBoost"
+ "startAnalyticsReportingTimer"
+ "startAnalyticsReportingTimer_block_invoke"
- "%s::%s:%d: Failed to allocate timer object"
- "%s::%s:%d: Sending Budget to modem: Sem: %u, Seq: %u, SAR Budget: %s W/kg, SAR Budget Cluster[0]: %s W/kg, SAR Budget Cluster[1]: %s W/kg, MPE Budget: %s mW/cm^2, Period: %u seconds, Operating Mode: %s\n, SAR Budget Cluster[2]: %s W/kg, SAR Budget Cluster[3]: %s W/kg, TER Consumed (Average): %u %%"
- "%s::%s:%d: Triggering coredump due to a SPMI error\n"
- "com.apple.cellularSarBoost"
- "startTaskTimer"

```
