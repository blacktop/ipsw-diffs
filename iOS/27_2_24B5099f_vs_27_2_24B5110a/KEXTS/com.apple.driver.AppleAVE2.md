## com.apple.driver.AppleAVE2

> `com.apple.driver.AppleAVE2`

```diff

-913.63.1.0.0
+913.64.1.0.0
   __TEXT.__const: 0x4b6c0
-  __TEXT.__cstring: 0x491f4
-  __TEXT.__os_log: 0x5decc
-  __TEXT_EXEC.__text: 0x1d1a28
+  __TEXT.__cstring: 0x49270
+  __TEXT.__os_log: 0x5e03a
+  __TEXT_EXEC.__text: 0x1d1d48
   __TEXT_EXEC.__auth_stubs: 0x7b0
   __DATA.__data: 0x2c8
   __DATA.__common: 0x130

   __DATA_CONST.__auth_ptr: 0x8
   Functions: 2998
   Symbols:   0
-  CStrings:  9945
+  CStrings:  9949
 
Functions:
~ sub_fffffe000880064c -> sub_fffffe000880229c : 600 -> 608
~ __Z22AVE_Prop_Cfg_AV1_PrintP19_S_AVE_Prop_Cfg_AV1jiPKci : 37544 -> 37804
~ __Z17AVE_Client_VerifyP13_S_AVE_ClientbP35AVE_SessionSettings_UserKernel_Data : 752 -> 756
~ sub_fffffe00088811c8 -> sub_fffffe0008882f28 : 588 -> 584
~ __Z22AVE_Prop_Cfg_AVC_PrintP19_S_AVE_Prop_Cfg_AVCjiPKci : 36344 -> 36592
~ __ZN9AVE_PSGen4InitEyPv14_E_AVE_EncTypeii : 5824 -> 5864
~ sub_fffffe0008919694 -> sub_fffffe000891b510 : 676 -> 668
~ __Z23AVE_Prop_Cfg_HEVC_PrintP20_S_AVE_Prop_Cfg_HEVCjiPKci : 48784 -> 49044
~ sub_fffffe00089a2168 -> sub_fffffe00089a40e0 : 56 -> 48
CStrings:
+ "%lld %d AVE %s: %p %lld MachThreadPriorityForThreadEmittingFrames %d"
+ "%lld %d AVE %s: %p %lld MachThreadPriorityForThreadEmittingFrames %d\n"
+ "%p %lld MachThreadPriorityForThreadEmittingFrames %d"
+ "%p %lld MachThreadPriorityForThreadEmittingFrames %d\n"
+ "913.64.1"
- "913.63.1"
```
