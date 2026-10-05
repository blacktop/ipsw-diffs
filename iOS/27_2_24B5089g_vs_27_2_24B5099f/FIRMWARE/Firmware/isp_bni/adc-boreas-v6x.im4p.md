## adc-boreas-v6x.im4p

> `Firmware/isp_bni/adc-boreas-v6x.im4p`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__TEXT.__eh_frame`
- `__DATA._rtk_power`
- `__DATA.__data_copy`
- `__DATA._fwinfo`
- `__DATA._rtk_smp_main`
- `__DATA.__chain_starts`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0xb3e260
-  __TEXT.__const: 0x920408
-  __TEXT.__cstring: 0xccaf0
+  __TEXT.__text: 0xb3f328
+  __TEXT.__const: 0x920708
+  __TEXT.__cstring: 0xccfbc
   __TEXT._rtk_patchbay: 0x24a
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__eh_frame: 0x1bc
-  __DATA.__const: 0x89550
+  __DATA.__const: 0x89530
   __DATA._rtk_heap: 0x1000
   __DATA._copy_begin: 0x0
-  __DATA.__data: 0x11cb10
+  __DATA.__data: 0x11caf0
   __DATA._rtk_power: 0x3f8
   __DATA._copy_end: 0x0
   __DATA._rtk_init_stack: 0x2000

   __DATA._rtk_smp_main: 0x8
   __DATA._rtk_boot_l1: 0x80
   __DATA.__gxf_data: 0x10
-  __DATA._rtk_mtab: 0x320
+  __DATA._rtk_mtab: 0x308
   __DATA.__chain_starts: 0x38
   __DATA.__mod_init_func: 0xd8
   __DATA._rtk_threads: 0x0
-  __DATA.__zerofill: 0x5ffe00
-  Functions: 14949
+  __DATA.__zerofill: 0x5fbd00
+  Functions: 14952
   Symbols:   0
-  CStrings:  22249
+  CStrings:  22270
 
CStrings:
+ "                    d: tolerance error delta (um)\n"
+ "                    t: timer ticks, 0 = disable\n"
+ "  gmcOriginalRotationValid =%s\n"
+ "  gmcScanModeIdx     =%d\n"
+ "  propGMCDebug       =0x%x\n"
+ " [2]   [t] [d] [-]: Override shutdown duration (ticks) and target tolerance (um)\n"
+ "%s: %s: L:%u reg: %#zx CDR_LOCK: %#x\n"
+ "%s: %s: L:%u reg: %#zx EQ_DONE: %#x\n"
+ "%s: %s: ch %zu LPDP/ACI inter-lane align not done after %u ms"
+ "%s: %s: ch %zu LPDP/ACI lane clock recovery not done after %u ms"
+ "%s: %s: ch %zu LPDP/ACI lane link train not done after %u ms"
+ "Already in requested VA mode (%d)\n"
+ "CLcbManager.cpp"
+ "CRT: CPCECalibAlgoGmc.cpp:%d [DSI] GMC Scan Mode DEBUG: perturbing around operational rotation (iter %d)\n"
+ "Ch%zu unexpected shutdown request (phase %u, mode %d)\n"
+ "DPRXCInterLaneAlignDonePoll"
+ "DPRXCLaneClockRecoveryDonePoll"
+ "DPRXCLaneLinkTrainDonePoll"
+ "Invalid duration requested (%llu). Valid range: 0-%u\n"
+ "Overriding shutdown stop duration (%u ticks, 0 = disabled)\n"
+ "Overriding shutdown target tolerance (%.1fum)\n"
+ "VA Ch%zu: ignoring requested mode %d during shutdown\n"
+ "VADRV Ch%zu Begin shutdown: target %.1fum (tol %.1fum, max %u ticks)\n"
+ "VADRV Ch%zu OFF requested during shutdown; ending sequence\n"
+ "VADRV Ch%zu shutdown aperture reached target (delta: %.3f, %u ticks)\n"
+ "VADRV Ch%zu shutdown aperture timed out (delta: %.3f, %u ticks)\n"
+ "VaStopped"
- "!kb reg:%x"
- "ADDcn"
- "Already in requested VA mode\n"
- "FDDcn"
- "hADDcnProc != NULL"
- "hFDDcnProc != NULL"
```
