## com.apple.driver.ApplePMGR

> `com.apple.driver.ApplePMGR`

```diff

-1774.0.4.0.0
-  __TEXT.__cstring: 0xf1c3
+1774.0.7.0.0
+  __TEXT.__cstring: 0xf2b3
   __TEXT.__const: 0x280
-  __TEXT_EXEC.__text: 0x66214
+  __TEXT_EXEC.__text: 0x6734c
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x138
   __DATA.__common: 0x5b0

   __DATA_CONST.__mod_term_func: 0x40
   __DATA_CONST.__const: 0xb5c8
   __DATA_CONST.__kalloc_type: 0x980
-  __DATA_CONST.__kalloc_var: 0xe60
-  UUID: F57CEA2B-97B2-3701-84C4-582BD8047DC9
-  Functions: 2700
+  __DATA_CONST.__kalloc_var: 0xf00
+  UUID: 86EB94FA-A50D-336F-9DD2-DCC0DF1FB8EF
+  Functions: 2708
   Symbols:   0
-  CStrings:  1721
+  CStrings:  1730
 
CStrings:
+ "ApplePMGR: [Die %d] PwrGateRetentionV2 devID:0x%x reg:0x%x, %s data:0x%x\n"
+ "OFF"
+ "ON"
+ "_retentFFData"
+ "_retentMemData"
+ "retention_config_ff"
+ "retention_config_mem"
+ "site.PwrgateRetentionData"
+ "void ApplePMGR::_setPwrGateRetentionV2(DeviceID, bool, UInt32)"

```
