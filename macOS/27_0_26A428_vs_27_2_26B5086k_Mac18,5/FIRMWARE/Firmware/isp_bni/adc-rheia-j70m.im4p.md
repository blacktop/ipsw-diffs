## adc-rheia-j70m.im4p

> `Firmware/isp_bni/adc-rheia-j70m.im4p`

### Sections with Same Size but Changed Content

- `__DATA.__const`
- `__DATA.__data`
- `__DATA.__data_copy`
- `__DATA._rtk_smp_main`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x96a220
-  __TEXT.__const: 0x314644
-  __TEXT.__cstring: 0xf185e
+  __TEXT.__text: 0x96a458
+  __TEXT.__const: 0x314660
+  __TEXT.__cstring: 0xf1925
   __TEXT.text_env: 0x4f1a4
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0

   __DATA.__zerofill: 0xd7fdf8
   Functions: 8591
   Symbols:   0
-  CStrings:  26425
+  CStrings:  26429
 
Functions:
~ sub_1dd30 : 2480 -> 2484
~ sub_25a30 -> sub_25a34 : 28336 -> 28340
~ sub_3fdeac -> sub_3fdeb4 : 1028 -> 1044
~ sub_4ae4c0 -> sub_4ae4d8 : 6532 -> 6636
~ sub_81b86c -> sub_81b8ec : 7756 -> 7840
~ sub_83e454 -> sub_83e528 : 3892 -> 3904
~ sub_844504 -> sub_8445e4 : 4524 -> 4528
~ sub_8456b0 -> sub_845794 : 27164 -> 27180
~ sub_875aac -> sub_875ba0 : 2364 -> 2684
~ sub_9596f0 -> sub_959924 : 328 -> 332
~ sub_96a0ec -> sub_96a324 : 308 -> 316
CStrings:
+ "IC[%zu] frameSkip set to 1 at ic stopping\n"
+ "MiscBufferRequest"
+ "ch %zu FC: %d Full Res Host Meta Data buffer not available, avail %zu inFlight %zu"
+ "ch %zu: forced ProcessStopped() after %u SIF errors in IC_STOPPING"
+ "ch%zu wasPaused %d now %f RVsync %f FVsync %f\n"
- "ch %zu FC: %d Full Res Host Meta Data buffer not available"
```
