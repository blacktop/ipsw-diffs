## adc-boreas-v6x.im4p

> `AssetData/boot/Firmware/isp_bni/adc-boreas-v6x.im4p`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__TEXT.__eh_frame`
- `__DATA.__data`
- `__DATA._rtk_power`
- `__DATA.__data_copy`
- `__DATA._rtk_mtab`
- `__DATA.__chain_starts`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0xb3f328
-  __TEXT.__const: 0x920708
-  __TEXT.__cstring: 0xccfbc
+  __TEXT.__text: 0xb412e8
+  __TEXT.__const: 0x920988
+  __TEXT.__cstring: 0xcd5bc
   __TEXT._rtk_patchbay: 0x24a
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__eh_frame: 0x1bc
-  __DATA.__const: 0x89530
+  __DATA.__const: 0x895c8
   __DATA._rtk_heap: 0x1000
   __DATA._copy_begin: 0x0
   __DATA.__data: 0x11caf0

   __DATA.__mod_init_func: 0xd8
   __DATA._rtk_threads: 0x0
   __DATA.__zerofill: 0x5fbd00
-  Functions: 14952
+  Functions: 14961
   Symbols:   0
-  CStrings:  22270
+  CStrings:  22303
 
CStrings:
+ " | "
+ "%#zx: %#x %#x\n"
+ "%-30s0x%02X [%s]\n"
+ "%s: global rails off, TS: %f \n"
+ "%s: global rails on, TS: %f \n"
+ "===== SENSOR_DIAG ch %zu BEGIN %s =====\n"
+ "===== SENSOR_DIAG ch %zu END =====\n"
+ "BOOT"
+ "DmaErr %s dva=%zx strideLu=%u offset=%u,%u\n"
+ "DmaErr %s size=%ux%u sttBase=%u npages=%u\n"
+ "FRAMEDONE_STALL"
+ "IGNORE cmd %zu, as other ch is active! %x"
+ "IMX%x: no LOWLIGHT table for HIRES expType %u, fall back to QSUB!"
+ "IMX914 M3 KDF signed update failed (status90 0x%x mode 0x%x); retrying on next RVSync (%u/%u)\n"
+ "IMX914 M3 KDF signed update still failing after %u attempts (status90 0x%x mode 0x%x); giving up this request\n"
+ "NO_FIRST_RVSYNC"
+ "NO_FRAMEDONE"
+ "OutputEnableControl: ch=%ld i=%d ref buffer not big enough yet, deferring pending enable"
+ "OutputEnableControl: ch=%ld i=%d ref buffer too small for already-enabled stream, disabling until it regrows"
+ "RVSYNC_STALL"
+ "SENSOR_0"
+ "SENSOR_1"
+ "SENSOR_2"
+ "SENSOR_3"
+ "SENSOR_4"
+ "SENSOR_5"
+ "SENSOR_6"
+ "SENSOR_DIAG %s: frame counter (0x%04x):\n"
+ "SENSOR_DIAG %s: mode %#x modeSel %#x fc %u kdf90 %#x\n"
+ "SENSOR_DIAG %s: sec %#x op %#x err %#x link %#x/%#x rdFail %d\n"
+ "SENSOR_DIAG ch %zu %s for %llu us, fc %d\n"
+ "SENSOR_DIAG ch %zu --- %s registers ---\n"
+ "SENSOR_DIAG ch %zu --- DPRX lane status ---\n"
+ "SENSOR_DIAG ch %zu pwr cnt/st sns %u/%d foc %u/%d stb %u/%d hwk %u/%d efs %u/%d fpd %u/%d\n"
+ "SecureM3 supported:"
+ "SecureM3 unknown bits:"
+ "VIO input %ux%u stride %u (factor %u) unsupported: rejecting"
+ "[%s] ch %zu send MotionAEDetect params to LC, sensitivityMultiplier %.2f delayMultiplier %.2f\n"
+ "[SetMotionAEDetectCount] delayMultiplier %.2f (base-value scaling not yet implemented)\n"
+ "[SetMotionAEDetectThreshold] sensitivityMultiplier %.2f (base-value scaling not yet implemented)\n"
+ "ch %d, MotionAE: setEnable %d, minBlankForOISUs %u, minShutterAngleForOisMotionAE %u, motionDetectorLLVLuxThresh %.2f\n"
+ "none (0x0)"
+ "rails missing %zu %zu - %p %p\n"
- "%s%s \n"
- "%s: global rails off, ts %llu ticks \n"
- "%s: global rails on, ts %llu ticks\n"
- "%s[%zu]%-*s%#08llX \n"
- "BTR: "
- "ENT: GlobalRailSeqWalk"
- "IGNORE cmd, as other ch is active!"
- "IMX982RegSetting.cpp"
- "[%s] ch %zu send MotionAEDetect params to LC, threshold %u count %u\n"
- "ch %d, MotionAE: setEnable %d\n"
```
