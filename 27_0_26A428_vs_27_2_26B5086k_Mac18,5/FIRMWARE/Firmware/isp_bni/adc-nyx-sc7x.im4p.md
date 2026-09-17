## adc-nyx-sc7x.im4p

> `Firmware/isp_bni/adc-nyx-sc7x.im4p`

### Sections with Same Size but Changed Content

- `__DATA.__const`
- `__DATA.__data`
- `__DATA.__data_copy`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x8f2ac4
-  __TEXT.__const: 0x240170
+  __TEXT.__text: 0x8f2e0c
+  __TEXT.__const: 0x24018c
   __TEXT.text_env: 0x8e0
-  __TEXT.__cstring: 0xe5621
+  __TEXT.__cstring: 0xe56ef
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __DATA.__const: 0x3b688

   __DATA.__zerofill: 0xe25af8
   Functions: 8334
   Symbols:   0
-  CStrings:  25341
+  CStrings:  25345
 
Functions:
~ sub_1d52c : 2480 -> 2484
~ sub_20cfc -> sub_20d00 : 28048 -> 28052
~ sub_3e1c38 -> sub_3e1c40 : 1016 -> 1032
~ sub_48b6fc -> sub_48b714 : 6532 -> 6636
~ sub_7a9f18 -> sub_7a9f98 : 15604 -> 15840
~ sub_7e5658 -> sub_7e57c4 : 3188 -> 3288
~ sub_7eb160 -> sub_7eb330 : 17300 -> 17316
~ sub_7ef4f4 -> sub_7ef6d4 : 552 -> 908
~ sub_8e1b90 -> sub_8e1ed4 : 380 -> 384
~ sub_8f2980 -> sub_8f2cc8 : 324 -> 332
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
