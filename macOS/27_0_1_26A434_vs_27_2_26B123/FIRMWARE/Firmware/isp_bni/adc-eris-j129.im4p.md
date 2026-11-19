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
+  __TEXT.__text: 0x9875d4
+  __TEXT.__const: 0x24fd30
   __TEXT.text_env: 0xef0
-  __TEXT.__cstring: 0xf55d1
+  __TEXT.__cstring: 0xf56ab
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __DATA.__const: 0x3b310

   __DATA.__mod_init_func: 0x8
   __DATA._rtk_threads: 0x0
   __DATA.__zerofill: 0x85eef8
-  Functions: 8456
+  Functions: 8459
   Symbols:   0
-  CStrings:  27107
+  CStrings:  27111
 
CStrings:
+ "20:30:08"
+ "NVM header revision invalid %d - off %d\n"
+ "cam[%zu] frameSkip set to 1 at ic stopping\n"
+ "ch %zu SIF maskCount %d\n"
+ "ch %zu fc %d state %d skip %d isStream %d"
+ "ch %zu fc %d state %d skip %d isStream %d pendingStopChMask %#x -> %#x\n"
+ "ch %zu heartbeat fc %d state %d skip %d RVsync %f FVsync %f\n"
+ "ch%zu wasPaused %d now %f RVsync %f FVsync %f\n"
- "19:26:17"
- "NVM header revision invalid\n"
- "bPendingStop %d pendingStopChMask %#x"
- "wasPaused %d now %llu RVsync %llu FVsync %llu\n"
```
