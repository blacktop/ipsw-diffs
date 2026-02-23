## com.apple.driver.AppleSPMIPMU

> `com.apple.driver.AppleSPMIPMU`

```diff

-1360.100.4.0.0
-  __TEXT.__cstring: 0x27fc
+1360.100.5.0.0
+  __TEXT.__cstring: 0x281e
   __TEXT.__const: 0x26
-  __TEXT_EXEC.__text: 0xbf20
+  __TEXT_EXEC.__text: 0xbefc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x320
   __DATA.__common: 0xc0

   __DATA_CONST.__mod_term_func: 0x10
   __DATA_CONST.__const: 0xf00
   __DATA_CONST.__kalloc_type: 0x140
-  UUID: 882C7F61-E717-30A9-8F41-6ABF8E8DB3DF
+  UUID: B734CA92-7D75-3979-B346-FA4AAF76CEDB
   Functions: 167
   Symbols:   0
-  CStrings:  356
+  CStrings:  354
 
Functions:
~ __ZN18AppleDialogSPMIPMU13_setLpemStateEhhhhhhh -> sub_fffffe000931a990 : 432 -> 420
~ __ZN18AppleDialogSPMIPMU21_setLpemBluetoothFWOKEh -> sub_fffffe000931ab34 : 372 -> 360
~ sub_fffffe000933cab0 -> sub_fffffe000931b6b8 : 812 -> 772
~ __ZN18AppleDialogSPMIPMU17_writeLpemLogDataEv : 480 -> 508
CStrings:
+ "%s::%sPMU-LPM: Unable to write LPM log (%x)\n\n"
+ "%s::%sPMU-LPM: error (%x)\n\n"
+ "%s::%sPMU-LPM: get PDOD error (%x)\n\n"
+ "%s::%sPMU-LPM: log save error (%x)\n\n"
+ "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 21:38:05 Feb 17 2026\n"
+ "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 21:38:05 Feb 17 2026\n"
+ "%s::start: %s _pmuNub: %p ** configuration not found ** built 21:38:05 Feb 17 2026\n"
+ "%s::start: %s _pmuNub: %p built 21:38:05 Feb 17 2026\n"
+ "/Library/Caches/com.apple.xbs/34AE379D-0062-4135-9F03-2F7AFF666D3E/TemporaryDirectory.DQQcQ4/Sources/AppleDialogPMU/SPMI/AppleDialogSPMIPMU.cpp"
+ "PMU-LPM: FWOK=%d FLAGS=0x%x\n"
+ "PMU-LPM: LPEM control dictionary is uninitialized"
+ "PMU-LPM: LPMS cleared\n"
+ "PMU-LPM: Log data is NOT valid. 0x%x 0x%x\n"
+ "PMU-LPM: ctrl read failed\n"
+ "PMU-LPM: ctrl write failed\n"
+ "PMU-LPM: get log data error\n"
+ "PMU-LPM: log header: %08Xh:%08Xh:%08Xh:%08Xh\n"
+ "PMU-LPM: lpms=0x%x lpmi=0x%x lpmi2=0x%x\n"
- "%s::%s LPM error (%x)\n\n"
- "%s::%s LPM get PDOD error (%x)\n\n"
- "%s::%s LPM log save error (%x)\n\n"
- "%s::%s Unable to write LPM log (%x)\n\n"
- "%s::%sLPEM control dictionary is uninitialized\n"
- "%s::%sLPM: fwok=%d flags=0x%x\n\n"
- "%s::%sLPM: lpms=0x%x lpmi=0x%x lpmi2=0x%x\n\n"
- "%s::handleStart: %s _pmuNub: %p ** configuration not found ** built 21:10:27 Feb  5 2026\n"
- "%s::handleStart: ro=%d nvram=%d helper=%d %s _pmuNub: %p 0x%04x:0x%04x-0x%04x built 21:10:27 Feb  5 2026\n"
- "%s::start: %s _pmuNub: %p ** configuration not found ** built 21:10:27 Feb  5 2026\n"
- "%s::start: %s _pmuNub: %p built 21:10:27 Feb  5 2026\n"
- "/Library/Caches/com.apple.xbs/41E15A5C-6C9A-441B-9FBB-82EE3AF1CF24/TemporaryDirectory.EhPcDg/Sources/AppleDialogPMU/SPMI/AppleDialogSPMIPMU.cpp"
- "LPM state clear\n"
- "LPM: Log data is NOT valid. 0x%x 0x%x\n"
- "LPM: ctrl read failed\n"
- "LPM: ctrl write failed\n"
- "LPM: get log data error\n"
- "_lpemCtrlDict"
- "_setLpemBluetoothFWOK"
- "_setLpemState"

```
