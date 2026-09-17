## adc-nyx-bc6x.im4p

> `Firmware/isp_bni/adc-nyx-bc6x.im4p`

### Sections with Same Size but Changed Content

- `__DATA.__const`
- `__DATA.__data`
- `__DATA.__data_copy`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x8cb240
-  __TEXT.__const: 0x240618
+  __TEXT.__text: 0x8cb520
+  __TEXT.__const: 0x240634
   __TEXT.text_env: 0x8e0
-  __TEXT.__cstring: 0xe2153
+  __TEXT.__cstring: 0xe2221
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __DATA.__const: 0x3a448

   __DATA.__zerofill: 0xe50ff8
   Functions: 8030
   Symbols:   0
-  CStrings:  24996
+  CStrings:  25000
 
Functions:
~ sub_1d52c : 2480 -> 2484
~ sub_21788 -> sub_2178c : 26740 -> 26744
~ sub_3de418 -> sub_3de420 : 1016 -> 1032
~ sub_796838 -> sub_796850 : 15604 -> 15840
~ sub_7d1f78 -> sub_7d207c : 3188 -> 3288
~ sub_7d7904 -> sub_7d7a6c : 17152 -> 17168
~ sub_7dbc04 -> sub_7dbd7c : 552 -> 908
~ sub_8be174 -> sub_8be450 : 380 -> 384
CStrings:
+ "cam[%zu] frameSkip set to 1 at ic stopping\n"
+ "ch %zu SIF maskCount %d\n"
+ "ch %zu fc %d state %d skip %d isStream %d"
+ "ch %zu fc %d state %d skip %d isStream %d pendingStopChMask %#x -> %#x\n"
+ "ch %zu heartbeat fc %d state %d skip %d RVsync %f FVsync %f\n"
+ "ch%zu wasPaused %d now %f RVsync %f FVsync %f\n"
- "bPendingStop %d pendingStopChMask %#x"
- "wasPaused %d now %llu RVsync %llu FVsync %llu\n"
```
