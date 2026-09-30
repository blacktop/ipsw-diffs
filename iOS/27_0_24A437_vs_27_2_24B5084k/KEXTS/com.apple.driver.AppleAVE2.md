## com.apple.driver.AppleAVE2

> `com.apple.driver.AppleAVE2`

```diff

-913.43.1.0.0
+913.48.1.0.0
   __TEXT.__const: 0x4b6f0
-  __TEXT.__cstring: 0x4804a
-  __TEXT.__os_log: 0x5cabd
-  __TEXT_EXEC.__text: 0x1cde78
+  __TEXT.__cstring: 0x48053
+  __TEXT.__os_log: 0x5cac2
+  __TEXT_EXEC.__text: 0x1cde98
   __TEXT_EXEC.__auth_stubs: 0x7b0
   __DATA.__data: 0x2c8
   __DATA.__common: 0x130
Functions:
~ sub_fffffe00087c3e54 -> sub_fffffe000885c764 : 1896 -> 1900
~ __Z27AVE_CHM_MakeFwCmd_Start_AV1P10_S_AVE_CHMyjP14_S_AVE_TimeOutP16sCAveCmdAv1Start : 1732 -> 1736
~ __Z25AVE_CHM_SetDataInfo_FwBufP10_S_AVE_CHMP14_S_AVE_CmdInfoP16_S_AVE_FrameInfoP14_S_AVE_DPB_SetP18AVE_PICMGMT_PARAMS : 23044 -> 23072
~ sub_fffffe000894ddb8 -> sub_fffffe00089e66ec : 56 -> 52
CStrings:
+ "%lld %d AVE %s: %s:%d %s | invalid MB/CTU stats firmware buffer %p %d %lld %p %lld | %d"
+ "%lld %d AVE %s: %s:%d %s | invalid MB/CTU stats firmware buffer %p %d %lld %p %lld | %d\n"
+ "2 <= pInfo->VideoParamsDriver.userDPBnumFrames && pInfo->VideoParamsDriver.userDPBnumFrames <= (((16) > (15) ? (16) : (15)) + 1)"
+ "913.48.1"
+ "num_ref_frame <= ((16) > (15) ? (16) : (15))"
+ "pInfo->sBufPFSet.saMBStats[m].iAddr != 0"
- "%lld %d AVE %s: %s:%d %s | invalid MB/CTU stats firmware buffer %p %d %lld %p %lld"
- "%lld %d AVE %s: %s:%d %s | invalid MB/CTU stats firmware buffer %p %d %lld %p %lld\n"
- "2 <= pInfo->VideoParamsDriver.userDPBnumFrames && pInfo->VideoParamsDriver.userDPBnumFrames <= (((16) > (16) ? (16) : (16)) + 1)"
- "913.43.1"
- "num_ref_frame <= ((16) > (16) ? (16) : (16))"
- "pInfo->sBufPFSet.sMBStats.iAddr != 0"
```
