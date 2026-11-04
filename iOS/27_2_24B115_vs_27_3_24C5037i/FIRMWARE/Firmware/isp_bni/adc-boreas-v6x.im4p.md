## adc-boreas-v6x.im4p

> `Firmware/isp_bni/adc-boreas-v6x.im4p`

### Sections with Same Size but Changed Content

- `__TEXT._rtk_patchbay`
- `__TEXT.__eh_frame`
- `__DATA._rtk_power`
- `__DATA.__data_copy`
- `__DATA._fwinfo`
- `__DATA._rtk_smp_main`
- `__DATA._rtk_mtab`
- `__DATA.__chain_starts`

```diff

-  __TEXT.__text: 0xb412e8
-  __TEXT.__const: 0x920988
-  __TEXT.__cstring: 0xcd5bc
+  __TEXT.__text: 0xb3c30c
+  __TEXT.__const: 0x91f918
+  __TEXT.__cstring: 0xce1be
   __TEXT._rtk_patchbay: 0x24a
   __TEXT.__constructor: 0x0
   __TEXT.__init_offsets: 0x0
   __TEXT.__eh_frame: 0x1bc
-  __DATA.__const: 0x895c8
+  __DATA.__const: 0x87258
   __DATA._rtk_heap: 0x1000
   __DATA._copy_begin: 0x0
-  __DATA.__data: 0x11caf0
+  __DATA.__data: 0x11cf30
   __DATA._rtk_power: 0x3f8
   __DATA._copy_end: 0x0
   __DATA._rtk_init_stack: 0x2000

   __DATA.__gxf_data: 0x10
   __DATA._rtk_mtab: 0x308
   __DATA.__chain_starts: 0x38
-  __DATA.__mod_init_func: 0xd8
+  __DATA.__mod_init_func: 0xb0
   __DATA._rtk_threads: 0x0
-  __DATA.__zerofill: 0x5fbd00
-  Functions: 14961
+  __DATA.__zerofill: 0x602300
+  Functions: 14943
   Symbols:   0
-  CStrings:  22303
+  CStrings:  22352
 
CStrings:
+ " CLAMPED"
+ "!tunableh_initialized()"
+ "%.2fKB"
+ "%.2fMB"
+ "%lluB"
+ "%s %s 0x4013 ch=%zu dropping streams %#x owned by other channels"
+ "%s %s CPDEProc::SpecialFn: unknown arg0=%llu"
+ "%s %s PCE reg override idx=%llu v0=%llu v1=%llu accepted=%d"
+ "%s %s PCE reg override rejected: idx=%llu out of range (NUMTYPES=%u)"
+ "%s: %s: in 0x%x (%.2fx), base %.2fx (full %u curr %u), raw 0x%x, out 0x%x (%.2fx)%s\n"
+ "%s: ACLPMODE_A/DCLPMODE_A: 0x%x / 0x%x\n"
+ "%s: AGC 0x%x: 0x%x\n"
+ "%s: BINNING_MODE H/V: 0x%x / 0x%x\n"
+ "%s: COARSE_INT_HI 0x%x: 0x%x%x%x\n"
+ "%s: CONTEXT_IDX sensor 0x%x%x%x%x host 0x%x%x%x%x\n"
+ "%s: DIG_GAIN_GLOBAL 0x%x: 0x%x\n"
+ "%s: DIG_SCOPE_X_SIZE_A: 0x%x%x - 0x%x%x\n"
+ "%s: DIG_SCOPE_Y_STA_A: 0x%x%x - 0x%x%x\n"
+ "%s: FRAME_CNT 0x%x: 0x%x\n"
+ "%s: FRAME_LENGTH_HI 0x%x: 0x%x%x%x\n"
+ "%s: HACK FCAM world rot Z %f -> %f\n"
+ "%s: KDF_STATUS90 0x%x: 0x%x\n"
+ "%s: LINE_LENGTH_HI 0x%x: 0x%x%x\n"
+ "%s: LINK_ENABLE/LANE_COUNT_SET: 0x%x / 0x%x\n"
+ "%s: MODE_SELECT 0x%x: 0x%x\n"
+ "%s: MULTI_SYNC_MODE 0x%x: 0x%x\n"
+ "%s: ORIENTATION 0x%x: 0x%x\n"
+ "%s: S:converted baseEIT %llu %llu in sus, sRatio %.3f\n"
+ "%s: SENSOR_MODE 0x%x: 0x%x\n"
+ "%s: SharedRawBufferPoolInfoGet: chBitMask 0x%x has no WIDE/TELE/SWIDE channel"
+ "%s: TEMPERATURE 0x%x: 0x%x%x\n"
+ "%s: X_ADD_STA_READ_A 0x%x: 0x%x%x - 0x%x%x\n"
+ "%s: Y_ADD_STA_READ_A 0x%x: 0x%x%x - 0x%x%x\n"
+ "%s: exclave Frame done timeout, fc %d rvcnt %d ts %f mICState %d\n"
+ "%s: global rail %u/%u: %s -> %s (pre %u us, post %u us) \n"
+ "%s:%d:%s: %s\n"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleH19ISPFirmware_h19/h10isp/common/misc/H19/StaticTunables/t8160/tunableh_chip_family.c"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleH19ISPFirmware_h19/h10isp/common/misc/H19/StaticTunables/tunableh.c"
+ "AST_CONTROL_CONFIG_C3"
+ "CAneClient.cpp"
+ "CViSeg: ch %u references stranded after %u retries; leaking pool, marking channel dead, requesting ISP reset\n"
+ "IGNORE cmd, as other ch is active!"
+ "MXWRAP_CTRR locked and SecureM3 FW loaded by mBoot (resume=%d)!\n"
+ "SET_DSID_CLR_BC_REG_BASE: base already set at cold boot, rejecting\n"
+ "SET_DSID_CLR_MULTI_BC_REG_BASE: base already set at cold boot, rejecting\n"
+ "TS=%llu ch=%u extremeLowLightMode=%u Quadra %u lux=%d LumaBinningMode=%d msOverallZoomFactor0_1024=%u fps=%d\nInput: WHS %d,%d,%d RO ROI XYWH=%d,%d,%d,%d, OffsetToOrigin XY=%d,%d. \nOutput: startX %d, startY %d, endX %d, endY %d, sizeX %d, sizeY %d, byteStrideDX %d, byteStrideScore %d, offset %d, scale %d DxOutputOffset %u\n"
+ "ZF CH[%d]: dynamicCal.isValid=%d useDynamicCal=%d\n"
+ "ZF: getDynamicCalControl(ch=%zu): control=%s initValid=%s useDynamicCal=%s\n"
+ "ZF: setDynamicCalControl(ch=%zu, control=%u)\n"
+ "ZF:CH%zu SMART_TAP_CAL overrideLegacyCalWithDynCal=%d: pCal=%d useDynamicCal=%d isRoiValid=%d\n"
+ "ZF:CH%zu WARNING: dynamicCal control ON rejected, initial cal is invalid\n"
+ "ZF:CH%zu dynamicCal control(value=0x%08X) ignored\n"
+ "ZF:CH%zu dynamicCal initValid=%d control=%u -> useDynamicCal=%d\n"
+ "[%s] CH = 0x%x LACC Image File rejected: malformed header/descriptors, size=%u\n"
+ "[%s] LACC Image File itcm ptr = %p size = %d, dtcm ptr = %p size = %d\n"
+ "[%s]AICamProc ch %zu ChannelStop timed out (rc %d)\n"
+ "[%s]CH: %u ViSeg buffer stranded in recovery; requesting ISP cold reset+reload\n"
+ "[DSI] %s: forcing sequence end for stop (frameIdxTbcSequence=%u, ctrlState=%u)"
+ "[DSI] FuseSplitPD: 0x402A rejected: SplitPD fusion unsupported on this device, ch %zu; dual/flip SplitPD remains enabled"
+ "[DSI] SPD meta json dump format failed/truncated ch%u (%d)"
+ "[DSI] SPD meta txt dump format failed/truncated ch%u (%d)"
+ "ch %u mask %u: %zu/%u slots in queue, retrying release"
+ "has_supported_board"
+ "has_supported_chip"
+ "has_supported_chip_rev"
+ "non-exist IPC Memory %p %u"
+ "tunableh_apply"
+ "tunableh_chip_family_check_device"
+ "tunableh_fig_get_mask"
+ "tunableh_fig_get_value"
+ "tunableh_get_fig() == NULL"
+ "tunableh_init"
+ "tunableh_module_evaluate"
+ "tunableh_read"
+ "tunableh_write"
+ "vc %zu fc %d exclave CIL ON->OFF before 1st RVSync, from previous camera session; muted (fc %d ts %f)\n"
+ "{\"input\":{\"frame\":{\"fw_platform_id\":%d,\"channel\":%d,\"timestamp\":%llu,\"framecount\":%d,\"x_pos_um\":%s,\"y_pos_um\":%s,\"z_pos_um\":%s,\"z_pos_dac\":%d,\"um_per_dac\":%s},\"rect\":{\"start\":{\"x\":%d,\"y\":%d},\"size\":{\"w\":%d,\"h\":%d}},\"size\":{\"w\":%d,\"h\":%d},\"stride\":%d},\"output\":{\"rect\":{\"start\":{\"x\":%d,\"y\":%d},\"size\":{\"w\":%d,\"h\":%d}},\"size\":{\"w\":%d,\"h\":%d},\"dx\":{\"stride\":%d,\"offset\":%d,\"scale\":%d},\"score\":{\"stride\":%d}}}"
- "%s BHARANI SensorSeqLoad: rID %04x chip 0x%x state %02x\n"
- "%s: %s: base zoom factor %.2fx, width full %u curr %u, adjusted zoom %.2fx\n"
- "===== SENSOR_DIAG ch %zu BEGIN %s =====\n"
- "===== SENSOR_DIAG ch %zu END =====\n"
- "AST_CONTROL_CONFIG_C4"
- "FRAMEDONE_STALL"
- "IGNORE cmd %zu, as other ch is active! %x"
- "MXWRAP_CTRR locked and SecureM3 FW loaded by iBoot (resume=%d)!\n"
- "NO_FIRST_RVSYNC"
- "NO_FRAMEDONE"
- "RVSYNC_STALL"
- "SENSOR_DIAG %s: frame counter (0x%04x):\n"
- "SENSOR_DIAG %s: mode %#x modeSel %#x fc %u kdf90 %#x\n"
- "SENSOR_DIAG %s: sec %#x op %#x err %#x link %#x/%#x rdFail %d\n"
- "SENSOR_DIAG ch %zu %s for %llu us, fc %d\n"
- "SENSOR_DIAG ch %zu --- %s registers ---\n"
- "SENSOR_DIAG ch %zu --- DPRX lane status ---\n"
- "SENSOR_DIAG ch %zu pwr cnt/st sns %u/%d foc %u/%d stb %u/%d hwk %u/%d efs %u/%d fpd %u/%d\n"
- "ZF CH[%d]: dynamicCal.isValid=%d\n"
- "ZF:CH%zu SMART_TAP_CAL overrideLegacyCalWithDynCal=%d: pCal=%d dynamicCal.isValid=%d isRoiValid=%d\n"
- "[%s] LACC Image File algoId = 0x%x\n"
- "[%s] LACC Image File descriptorOffsets[%d] = %d descType = %d\n"
- "[%s] LACC Image File dtcm ptr = %p size = %d\n"
- "[%s] LACC Image File itcm ptr = %p size = %d\n"
- "[DSI] FuseSplitPD: no fusion factory for channel %zu"
- "pParams->mode < CISP_CAMERA_CONFIG_MODE_TOTAL"
- "pSensorNoiseModel->mode < CISP_CAMERA_CONFIG_MODE_TOTAL"
- "rails missing %zu %zu - %p %p\n"
```
