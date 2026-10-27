## adc-nyx-sc7x.im4p

> `Firmware/isp_bni/adc-nyx-sc7x.im4p`

### Sections with Same Size but Changed Content

- `__DATA.__data`
- `__DATA._rtk_power`
- `__DATA._rtk_patchbay`
- `__DATA.__data_copy`
- `__DATA._rtk_mtab`
- `__DATA.__chain_starts`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x8f2ac4
-  __TEXT.__const: 0x240170
+  __TEXT.__text: 0x8f2f50
+  __TEXT.__const: 0x24030c
   __TEXT.text_env: 0x8e0
-  __TEXT.__cstring: 0xe5621
+  __TEXT.__cstring: 0xe5837
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
-  __DATA.__const: 0x3b688
+  __DATA.__const: 0x3b748
   __DATA._rtk_heap: 0x1000
   __DATA.__data: 0xd9040
   __DATA._rtk_power: 0x3b8

   __DATA.__mod_init_func: 0x8
   __DATA._rtk_threads: 0x0
   __DATA.__zerofill: 0xe25af8
-  Functions: 8334
+  Functions: 8337
   Symbols:   0
-  CStrings:  25341
+  CStrings:  25353
 
CStrings:
+ "20:30:09"
+ "NVM header revision invalid %d - off %d\n"
+ "cam[%zu] frameSkip set to 1 at ic stopping\n"
+ "ch %zu SIF maskCount %d\n"
+ "ch %zu fc %d state %d skip %d isStream %d"
+ "ch %zu fc %d state %d skip %d isStream %d pendingStopChMask %#x -> %#x\n"
+ "ch %zu heartbeat fc %d state %d skip %d RVsync %f FVsync %f\n"
+ "ch%zu wasPaused %d now %f RVsync %f FVsync %f\n"
+ "transition_mode019_to_mode550_revert_step0"
+ "transition_mode019_to_mode550_revert_step1"
+ "transition_mode019_to_mode550_step0"
+ "transition_mode019_to_mode550_step1"
+ "transition_mode019_to_mode650_revert_step0"
+ "transition_mode019_to_mode650_revert_step1"
+ "transition_mode019_to_mode650_step0"
+ "transition_mode019_to_mode650_step1"
- "19:26:18"
- "NVM header revision invalid\n"
- "bPendingStop %d pendingStopChMask %#x"
- "wasPaused %d now %llu RVsync %llu FVsync %llu\n"
```
