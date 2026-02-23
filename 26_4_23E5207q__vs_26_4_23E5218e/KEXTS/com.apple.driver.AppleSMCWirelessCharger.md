## com.apple.driver.AppleSMCWirelessCharger

> `com.apple.driver.AppleSMCWirelessCharger`

```diff

-118.100.5.0.0
+118.100.7.0.0
   __TEXT.__const: 0x60
-  __TEXT.__cstring: 0x2b0a
+  __TEXT.__cstring: 0x2bdc
   __TEXT.__os_log: 0x553
-  __TEXT_EXEC.__text: 0xf014
+  __TEXT_EXEC.__text: 0xf0a0
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x68

   __DATA_CONST.__const: 0xee0
   __DATA_CONST.__kalloc_type: 0x80
   __DATA_CONST.__kalloc_var: 0x1e0
-  UUID: F245BC4F-C9E8-3E73-8FB4-901AB8915019
+  UUID: 385F7540-21C5-3980-AB98-50A1882F9019
   Functions: 180
   Symbols:   0
-  CStrings:  388
+  CStrings:  391
 
Functions:
~ sub_fffffe000931fa20 -> sub_fffffe00092fe5c0 : 4192 -> 4304
~ sub_fffffe0009321768 -> sub_fffffe0009300378 : 2572 -> 2700
~ sub_fffffe00093223e4 -> sub_fffffe0009301074 : 316 -> 24
~ sub_fffffe0009322520 -> sub_fffffe000930108c : 32 -> 236
~ sub_fffffe0009322540 -> sub_fffffe0009301178 : 3396 -> 32
~ sub_fffffe0009323284 -> sub_fffffe0009301198 : 24 -> 3396
~ sub_fffffe0009323ddc -> sub_fffffe0009302a1c : 1192 -> 1172
CStrings:
+ "/Library/Caches/com.apple.xbs/95A6977C-C3AE-4FD0-A5EB-76E65C391917/TemporaryDirectory.nQeVgT/Sources/AppleC26Charger/AppleSMCWirelessCharger.cpp"
+ "CRC 159 attempt %d/%d: Fail; computed 0x%x, expected 0x%x; reset Chromite\n"
+ "CRC 159 attempt %d/%d: Pass; computed 0x%x, expected 0x%x\n"
+ "Failed to reset Chromite via WAFC/Fw_Ctrl_Cmd_Blocking_Fw_Update; ret=0x%x\n"
- "/Library/Caches/com.apple.xbs/1D9AC652-4CC0-4B04-85C5-95BDC396ED0F/TemporaryDirectory.pHoiqC/Sources/AppleC26Charger/AppleSMCWirelessCharger.cpp"

```
