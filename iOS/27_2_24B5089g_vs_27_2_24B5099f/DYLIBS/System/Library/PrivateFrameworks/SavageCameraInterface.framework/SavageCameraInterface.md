## SavageCameraInterface

> `/System/Library/PrivateFrameworks/SavageCameraInterface.framework/SavageCameraInterface`

```diff

-10.60.0.0.0
-  __TEXT.__text: 0x28c8
+10.61.0.0.0
+  __TEXT.__text: 0x2a58
   __TEXT.__const: 0xc0
   __TEXT.__gcc_except_tab: 0x68
   __TEXT.__cstring: 0x67e
-  __TEXT.__oslogstring: 0x422
+  __TEXT.__oslogstring: 0x4a4
   __TEXT.__unwind_info: 0xc8
   __TEXT.__auth_stubs: 0x0
   __DATA_CONST.__const: 0x78

   - /usr/lib/libc++.1.dylib
   Functions: 18
   Symbols:   100
-  CStrings:  95
+  CStrings:  97
 
Functions:
~ __Z30sendSynchronousXpcMsgWithReplyP13xpcConnection25ISPServicesRemoteProperty29ISPServicesRemotePropertyTypeP28ISPServicesRemotePropertySet : 1332 -> 1416
~ _SavageCamInterfaceOpen : 800 -> 900
~ _SavageCamInterfaceGetSensorInfo : 680 -> 788
~ _SavageCamInterfaceColdBootPowerCycle : 452 -> 560
CStrings:
+ "%s: Missing ISP Driver version information in PropertyType Get, returning\n"
+ "%s: Missing ISP Driver version information, returning\n"
```
