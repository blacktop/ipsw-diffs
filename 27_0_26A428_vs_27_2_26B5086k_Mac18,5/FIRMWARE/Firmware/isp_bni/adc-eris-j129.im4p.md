## adc-eris-j129.im4p

> `Firmware/isp_bni/adc-eris-j129.im4p`

### Sections with Same Size but Changed Content

- `__DATA.__const`
- `__DATA.__data`
- `__DATA.__data_copy`
- `__DATA._rtk_smp_main`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x9871c4
-  __TEXT.__const: 0x24fcd4
+  __TEXT.__text: 0x9874a4
+  __TEXT.__const: 0x24fcf0
   __TEXT.text_env: 0xef0
-  __TEXT.__cstring: 0xf55d1
+  __TEXT.__cstring: 0xf569f
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __DATA.__const: 0x3b310

   __DATA.__zerofill: 0x85eef8
   Functions: 8456
   Symbols:   0
-  CStrings:  27107
+  CStrings:  27111
 
Functions:
~ sub_1dd30 : 2480 -> 2484
~ sub_23518 -> sub_2351c : 26844 -> 26848
~ sub_3f28f8 -> sub_3f2900 : 1016 -> 1032
~ sub_827390 -> sub_8273a8 : 15612 -> 15848
~ sub_864e60 -> sub_864f64 : 3188 -> 3288
~ sub_86acf4 -> sub_86ae5c : 17108 -> 17124
~ sub_86efc8 -> sub_86f140 : 552 -> 908
~ sub_97962c -> sub_979908 : 328 -> 332
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
