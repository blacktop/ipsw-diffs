## AppleAVE2FW_H18.im4p

> `Firmware/ave/AppleAVE2FW_H18.im4p`

### Sections with Same Size but Changed Content

- `__TEXT.__chain_starts`
- `__DATA._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA.__const`
- `__DATA._rtk_power`

```diff

-  __TEXT.__text: 0x1138d8
-  __TEXT.__const: 0x20044
-  __TEXT.__cstring: 0x1948d
+  __TEXT.__text: 0x1157a8
+  __TEXT.__const: 0x17064
+  __TEXT.__cstring: 0x19615
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18
   __DATA._rtk_patchbay: 0x211

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xc6860
-  Functions: 1282
-  Symbols:   1787
-  CStrings:  2841
+  Functions: 1288
+  Symbols:   1791
+  CStrings:  2849
 
Symbols:
+ __ZN10CAVEClient15GetCommandQueueE19_E_Proc_Mode_Queues
+ __ZN10CAVEClient22ProcessDirectFrameCmdsEi
+ __ZN14CAVCController32PipeProcessStandaloneRateControlEP18AVE_PICMGMT_PARAMSP23_S_AVE_Syntax_PFCfg_AVC
+ __ZN14CAVERefManager9UpdatePTSEP11RCFrameInfoP11_S_AVE_Timei
+ __ZN15CHEVCController32PipeProcessStandaloneRateControlEP18AVE_PICMGMT_PARAMSP13_S_HEVC_Slice
+ __ZN9BlurRatio6updateERK10FrameStats
- _iaHDRLUTQPModTables_LA
- _iaSDRLUTQPModTables_LA
CStrings:
+ "!MIDR: 0x%x"
+ "%s Enter %p %p %d %lld"
+ "%s: Frame:%u bufIdx %d"
+ "%s:%d FrameType: %d FrameNum: %lld POC: %d qp: %d"
+ "%s:%d HiMode: %d TID: %d %d"
+ "%s:%d after APL adjustment frame %d iMCTFStrength = %d -> %d"
+ "%s:%d gating: after previous frame strength adjustment  frame: %d, iMCTFStrength = %d -> %d "
+ "%s:%d gating: frame: %d  cap iMCTFStrength to 8"
+ "%s::%s:%d  Failed to Queue AVE_Cmd_Process for client_id: %lld %lld"
+ "%s::%s:%d %s | Fail to dequeue frame %d"
+ "%s::%s:%d %s | Failed to enqueue frame %lld"
+ "%s::%s:%d BITBOX (%lld %lld) type %d current blur %d.%06d filtered blur %d.%06d transcodeBits %d cplxFiltered %d.%06d"
+ "%s::%s:%d Failed to Queue AVE_Cmd_Process for client_id: %lld %lld"
+ "9013.35.1"
+ "PipeProcessStandaloneRateControl"
+ "ProcessDirectFrameCmds"
+ "bDequeued"
+ "bEnqueueResult"
- "!MIDR: 0x%llx"
- "%s Enter %p %p %d"
- "%s: bufIdx %d"
- "%s:%d F %d after APL adjustment iMCTFStrength = %d "
- "%s:%d gating: F %d  cap iMCTFStrength to 8"
- "%s:%d gating: after previous frame strength adjustment  frame: %d  iMCTFStrength = %d "
- "%s:%d gating: defore previous frame strength adjustment  frame: %d  iMCTFStrength = %d "
- "+ConfigReadDMA::Frame %lld"
- "9013.12.1"
- "Apply default gating"
```
