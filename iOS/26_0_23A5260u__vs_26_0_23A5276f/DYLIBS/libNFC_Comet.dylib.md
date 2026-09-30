## libNFC_Comet.dylib

> `/usr/lib/libNFC_Comet.dylib`

```diff

-360.33.0.0.0
-  __TEXT.__text: 0xc4d00
+360.35.0.0.0
+  __TEXT.__text: 0xc50bc
   __TEXT.__auth_stubs: 0x2c0
   __TEXT.__const: 0x9d8
-  __TEXT.__cstring: 0x3c242
-  __TEXT.__unwind_info: 0x1068
+  __TEXT.__cstring: 0x3c456
+  __TEXT.__unwind_info: 0x1070
   __DATA_CONST.__got: 0x8
   __DATA_CONST.__const: 0x1f0
   __AUTH_CONST.__auth_got: 0x160

   __DATA_DIRTY.__common: 0xf0
   - /usr/lib/libNFC_HAL.dylib
   - /usr/lib/libSystem.B.dylib
-  UUID: 332E331F-DDD5-350A-A507-2AC114C13B4D
+  UUID: D688DC66-F88C-38C7-B966-54BE06823E03
   Functions: 1863
   Symbols:   149
-  CStrings:  5884
+  CStrings:  5890
 
CStrings:
+ "phFriNfc_MifStd_H_ChkRemainTLVs: Current NDEF message exceeds the Maximum Tag NDEF size"
+ "phLibNfc_Ioctl_PrbsTest: Invalid Input Parameter!"
+ "phLibNfc_Ioctl_PrbsTest: LIBNFC Not Initialized"
+ "phLibNfc_LoggingNtfHandler:Failed to allocate memory for Dynamic BBA Info events"
+ "phLibNfc_ProcessDeactComplete: Lower layer has returned failure status"
+ "phLibNfc_PropTagRemDetNtfHandler: Transition status is invalid"
+ "phLibNfc_ReActivateComplete: Lower layer has returned failure status"
+ "phLibNfc_SwpTest_CB: Prbs test failed"
+ "phLibNfc_SwpTest_CB: Prbs test passed"
+ "phNciNfc_PrbsTest: Invalid parameters"
+ "phNciNfc_PrbsTest: Memory allocation for payload buffer Failed!"
+ "phNciNfc_PrbsTest: Prbs test sequence failed!"
+ "phNciNfc_PrbsTest: Stack not initialized"
+ "phNciNfc_SendPrbsTestCmd: Invalid input parameter"
+ "phNciNfc_TagRemNtfClearRemDevInfo"
- "Buffer passed by Lower layer is NULL"
- "Ioctl_PrbsTest: Invalid Input Parameter!"
- "Ioctl_PrbsTest: LIBNFC Not Initialized"
- "Prbs test failed"
- "Prbs test passed"
- "PrbsTest: Invalid parameters"
- "PrbsTest: MemAlloc for Params Failed!"
- "PrbsTest: Prbs test sequence failed!"
- "PrbsTest: Stack not initialized"

```
