## adc-eris-j129.im4p

> `Firmware/isp_bni/adc-eris-j129.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.text_env`
- `__TEXT._rtk_mtab`
- `__TEXT.__data_copy`
- `__DATA.__const`
- `__DATA.__data`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x7c2a94
-  __TEXT.__const: 0x1fb8d4
+  __TEXT.__text: 0x7c32f8
+  __TEXT.__const: 0x1fb954
   __TEXT.text_env: 0x5dba8
   __TEXT._rtk_mtab: 0x2b8
-  __TEXT.__cstring: 0xf496d
+  __TEXT.__cstring: 0xf4b60
   __TEXT.__data_copy: 0x190000
   __TEXT.__constructor: 0x0
   __TEXT.__chain_starts: 0x0

   __DATA.__zerofill: 0x31edf8
   Functions: 0
   Symbols:   0
-  CStrings:  27057
+  CStrings:  27066
 
CStrings:
+ "%s: ch %zu syncLeader %zu statsMaster %zu isStreaming %d aeSuspended %d\n"
+ "%s:CmdSuspendAutoResume: autoSuspendMask 0x%x, master_ch %zu, channelsToSuspend 0x%x, slave %zu\n"
+ "%s:ResumeAllSuspendedChannels: channelsToSuspend 0x%x\n"
+ "%s:RunProcess: statsmaster ch %zu added to channelsToSuspend 0x%x\n"
+ "%s:RunProcess:ch%zu fc %2d m %d autoSuspendMask 0x%x, startedSlaveChMask 0x%x, channelsToSuspend 0x%x, AE# %u, %u\n"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.e612g6/Sources/AppleH16ISPFirmware_h16/h10isp/filters/IC/CImageCaptureCoreExclave.cpp"
+ "19:55:44"
+ "EXTSYNC setting framerate property to %d on channel %u"
+ "FrameLength %u->%u, CIT %u clamped to %u\n"
+ "M2S B channel above lattice range (%.4f > 1), blendFactor=%.4f"
+ "M2S B channel below lattice range (%.4f < 0), blendFactor=%.4f"
+ "M2S Linear mapping result for blending: R=%.2f B=%.2f"
+ "M2S R channel above lattice range (%.4f > 1), blendFactor=%.4f"
+ "M2S R channel below lattice range (%.4f < 0), blendFactor=%.4f"
+ "ManualAE ch:%d, acctime:%d %d \n"
+ "Reset SetMinMaxFrameRate() to locked %d fps\n"
+ "SIFR Disabled SPD %d \n"
+ "SIFR enabled, SPD %d \n"
+ "ch:%d, max:%d %llu \n"
+ "no slave camera found for setfileVer %u\n"
- "%s: ch %zu statsMaster %zu isStreaming %d aeSuspended %d\n"
- "%s:CmdSuspendAutoResume: autoSuspendMask 0x%x, masterCh %zu, slave %zu\n"
- "%s:RunProcess: autoSuspendMask 0x%x, startedSlaveChMask 0x%x, AE# %u, %u\n"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oKUToE/Sources/AppleH16ISPFirmware_h16/h10isp/filters/IC/CImageCaptureCoreExclave.cpp"
- "00:38:25"
- "EXTSYNC setting Accurateframerate property to %d on channel %u"
- "ManualAE ch:%d, acctime:%d %d"
- "[DSI] Invalid Structure size allocated!"
- "ch:%d, max:%d %llu"
- "ch=%zu, EnterFrameRate(%d) should be not larger than ExitFrameRate(%d)"
- "ch=%zu, EnterThreshold(%d) should be not less than ExitThreshold(%d)"
```
