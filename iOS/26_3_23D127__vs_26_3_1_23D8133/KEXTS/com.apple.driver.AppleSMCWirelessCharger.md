## com.apple.driver.AppleSMCWirelessCharger

> `com.apple.driver.AppleSMCWirelessCharger`

```diff

-118.80.6.0.0
+118.92.2.0.0
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0x2acb
+  __TEXT.__cstring: 0x2b9d
   __TEXT.__os_log: 0x553
-  __TEXT_EXEC.__text: 0x1028c
+  __TEXT_EXEC.__text: 0x102fc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x68

   __DATA_CONST.__const: 0xee0
   __DATA_CONST.__kalloc_type: 0x80
   __DATA_CONST.__kalloc_var: 0x1e0
-  UUID: 01A11A8A-DCF6-3982-96F3-BE3D35993AF2
+  UUID: 40E42EA1-B7FB-37C3-BC77-4F51DEFD60CD
   Functions: 180
   Symbols:   0
-  CStrings:  388
+  CStrings:  391
 
Functions:
~ sub_fffffe0009bd32f0 -> sub_fffffe0009bdcb10 : 4372 -> 4484
CStrings:
+ "CRC 159 attempt %d/%d: Fail; computed 0x%x, expected 0x%x; reset Chromite\n"
+ "CRC 159 attempt %d/%d: Pass; computed 0x%x, expected 0x%x\n"
+ "Failed to reset Chromite via WAFC/Fw_Ctrl_Cmd_Blocking_Fw_Update; ret=0x%x\n"

```
