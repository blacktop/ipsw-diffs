## AudioSessionServer

> `/System/Library/PrivateFrameworks/AudioSessionServer.framework/AudioSessionServer`

```diff

-449.107.0.0.0
-  __TEXT.__text: 0x6e384
+449.203.0.0.0
+  __TEXT.__text: 0x6e46c
   __TEXT.__realtime: 0x49c
   __TEXT.__objc_methlist: 0xc4c
-  __TEXT.__gcc_except_tab: 0xa638
+  __TEXT.__gcc_except_tab: 0xa648
   __TEXT.__const: 0xbd0
   __TEXT.__cstring: 0x490c
-  __TEXT.__oslogstring: 0x547e
+  __TEXT.__oslogstring: 0x54e9
   __TEXT.__dlopen_cstrs: 0x5a
   __TEXT.__unwind_info: 0x30b8
   __TEXT.__objc_stubs: 0x0

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1673
-  Symbols:   2755
-  CStrings:  1014
+  Functions: 1675
+  Symbols:   2763
+  CStrings:  1015
 
Symbols:
+ GCC_except_table114
+ GCC_except_table118
+ GCC_except_table129
+ GCC_except_table133
+ GCC_except_table134
+ GCC_except_table137
+ GCC_except_table143
+ GCC_except_table169
+ GCC_except_table235
+ GCC_except_table242
+ GCC_except_table243
+ ___block_descriptor_56_ea8_40c69_ZTSNSt3__110shared_ptrIN4avas6server18DeviceTimeObserver8TimeInfoEEE_e53_v16?0r^{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}8l
+ ___copy_helper_block_ea8_40c69_ZTSNSt3__110shared_ptrIN4avas6server18DeviceTimeObserver8TimeInfoEEE
+ ___destroy_helper_block_ea8_40c69_ZTSNSt3__110shared_ptrIN4avas6server18DeviceTimeObserver8TimeInfoEEE
- GCC_except_table113
- GCC_except_table131
- GCC_except_table232
- GCC_except_table233
- GCC_except_table239
- ___block_descriptor_56_ea8_32c69_ZTSNSt3__110shared_ptrIN4avas6server18DeviceTimeObserver8TimeInfoEEE_e53_v16?0r^{AudioTimeStamp=dQdQ{SMPTETime=ssIIIssss}II}8l
Functions:
~ ____ZN4avas6server18DeviceTimeObserver10DeviceSlot15timestampWriterEv_block_invoke : 296 -> 312
+ ___copy_helper_block_ea8_40c69_ZTSNSt3__110shared_ptrIN4avas6server18DeviceTimeObserver8TimeInfoEEE
+ ___destroy_helper_block_ea8_40c69_ZTSNSt3__110shared_ptrIN4avas6server18DeviceTimeObserver8TimeInfoEEE
~ __ZN4avas6server18DeviceTimeObserver12createDeviceENS1_9DeviceKeyEyb : 1216 -> 1220
~ ____ZN4avas6server18DeviceTimeObserver10DeviceSlot20timestampWriterBTPtsEv_block_invoke : 740 -> 752
~ __ZN4avas6server18DeviceTimeObserver28sessionsObservingDeviceEventEj24AVAudioIOControllerEventbNSt3__18optionalIjEES5_ : 1528 -> 1676
~ __ZNSt3__14pairIN4avas6server18DeviceTimeObserver9DeviceKeyENS3_10DeviceInfoEEC2B9fqe220106INS_25__check_pair_constructionIS4_S5_EELi0EEEv : 208 -> 212
CStrings:
+ "%25s:%-5d dto stopping stale BT presentation time poller on start, a stop event was missed (device ID: %u)"
```
