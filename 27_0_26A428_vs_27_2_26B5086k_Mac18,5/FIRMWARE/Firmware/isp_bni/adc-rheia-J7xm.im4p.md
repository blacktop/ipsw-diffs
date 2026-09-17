## adc-rheia-J7xm.im4p

> `Firmware/isp_bni/adc-rheia-J7xm.im4p`

### Sections with Same Size but Changed Content

- `__DATA.__const`
- `__DATA.__data`
- `__DATA.__data_copy`
- `__DATA._rtk_mtab`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x8efde4
-  __TEXT.__const: 0x348930
+  __TEXT.__text: 0x8f001c
+  __TEXT.__const: 0x34894c
   __TEXT.text_env: 0x45b74
-  __TEXT.__cstring: 0xe7d15
+  __TEXT.__cstring: 0xe7ddc
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __DATA.__const: 0x37140

   __DATA.__zerofill: 0x2de5f8
   Functions: 8359
   Symbols:   0
-  CStrings:  25637
+  CStrings:  25641
 
Functions:
~ sub_1d52c : 2480 -> 2484
~ sub_2340c -> sub_23410 : 28272 -> 28276
~ sub_3ebc34 -> sub_3ebc3c : 1028 -> 1044
~ sub_497d2c -> sub_497d44 : 6532 -> 6636
~ sub_7a4830 -> sub_7a48b0 : 7756 -> 7840
~ sub_7c7434 -> sub_7c7508 : 3912 -> 3924
~ sub_7cd7a8 -> sub_7cd888 : 4412 -> 4416
~ sub_7ce8e4 -> sub_7ce9c8 : 27192 -> 27208
~ sub_7fe760 -> sub_7fe854 : 2264 -> 2584
~ sub_8d9bac -> sub_8d9de0 : 380 -> 384
~ sub_8efca0 -> sub_8efed8 : 324 -> 332
CStrings:
+ "IC[%zu] frameSkip set to 1 at ic stopping\n"
+ "MiscBufferRequest"
+ "ch %zu FC: %d Full Res Host Meta Data buffer not available, avail %zu inFlight %zu"
+ "ch %zu: forced ProcessStopped() after %u SIF errors in IC_STOPPING"
+ "ch%zu wasPaused %d now %f RVsync %f FVsync %f\n"
- "ch %zu FC: %d Full Res Host Meta Data buffer not available"
```
