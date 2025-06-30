## com.apple.driver.AppleH16CameraInterface

> `com.apple.driver.AppleH16CameraInterface`

```diff

-3.702.1.0.0
+3.703.0.0.0
   __TEXT.__const: 0xa110
-  __TEXT.__cstring: 0x17bd8
-  __TEXT.__os_log: 0x140d8
-  __TEXT_EXEC.__text: 0x98fa8
+  __TEXT.__cstring: 0x17bdf
+  __TEXT.__os_log: 0x140df
+  __TEXT_EXEC.__text: 0x98fb4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2a0
   __DATA.__common: 0x4c8

   __DATA_CONST.__const: 0xdbd0
   __DATA_CONST.__kalloc_type: 0x11c0
   __DATA_CONST.__kalloc_var: 0xa50
-  UUID: 05EC7137-ABE3-329E-A477-0023EFCD65CF
+  UUID: CAE66D0E-428F-3C0F-9097-EE4B942441EC
   Functions: 1740
   Symbols:   0
   CStrings:  3081
Functions:
~ __ZN13AppleH16CamIn21ISP_ECReadNVMSequenceEv : 604 -> 608
~ __ZN13AppleH16CamIn29ISP_PowerOnSecureSensor_gatedEj22eCIspSensorBootOptions -> sub_fffffff00916ebd4 : 320 -> 324
~ __ZN13AppleH16CamIn30ISP_PowerOffSecureSensor_gatedEj : 308 -> 312
CStrings:
+ "AppleH16CamIn:%s - Secure sensor power on failed - bootOpt: %d, chan: %d, res: 0x%08X\n"
- "AppleH16CamIn:%s - Secure sensor power on - bootOpt: %d, chan: %d, res: 0x%08X\n"

```
