## com.apple.driver.AppleAVE2

> `com.apple.driver.AppleAVE2`

```diff

-904.88.0.0.0
-  __TEXT.__const: 0x42470
-  __TEXT.__cstring: 0x3ff65
-  __TEXT.__os_log: 0x51d21
-  __TEXT_EXEC.__text: 0x19ede0
+904.97.1.0.0
+  __TEXT.__const: 0x426a0
+  __TEXT.__cstring: 0x400a3
+  __TEXT.__os_log: 0x51f83
+  __TEXT_EXEC.__text: 0x19f6bc
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2b8
   __DATA.__common: 0x130
-  __DATA.__bss: 0x3e8
+  __DATA.__bss: 0x3f0
   __DATA_CONST.__auth_got: 0x3c8
   __DATA_CONST.__got: 0xc8
   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x38
   __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x8830
+  __DATA_CONST.__const: 0x8b60
   __DATA_CONST.__kalloc_type: 0x4900
   __DATA_CONST.__kalloc_var: 0x2030
-  UUID: 90C9376D-68C1-35F4-8ECC-A0443579F18E
-  Functions: 2774
+  UUID: BC30F43F-782A-38C0-8637-73D5A52CB28A
+  Functions: 2768
   Symbols:   0
-  CStrings:  8941
+  CStrings:  8951
 
CStrings:
+ "%lld %d AVE %s: %s:%d %d %d %d %d %d %d| %d %d | %d %d"
+ "%lld %d AVE %s: %s:%d %d %d %d %d %d %d| %d %d | %d %d\n"
+ "%lld %d AVE %s: %s:%d %p %lld F %d PTS:%lld-%d, Hint:%d - %d"
+ "%lld %d AVE %s: %s:%d %p %lld F %d PTS:%lld-%d, Hint:%d - %d\n"
+ "%lld %d AVE %s: %s:%d %p %lld Frame disp %d FrameType %d"
+ "%lld %d AVE %s: %s:%d %p %lld Frame disp %d FrameType %d\n"
+ "%lld %d AVE %s: %s:%d %p invalid position disable scenecut %d %d"
+ "%lld %d AVE %s: %s:%d %p invalid position disable scenecut %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | fail to copy stats %p %lld %d %d"
+ "%lld %d AVE %s: %s:%d %s | fail to copy stats %p %lld %d %d\n"
+ "%lld %d AVE %s: %s:%d %s | invalid frame info %p %lld %d %d"
+ "%lld %d AVE %s: %s:%d %s | invalid frame info %p %lld %d %d\n"
+ "%lld %d AVE %s: %s:%d axi2af_parity_enable 0x%x"
+ "%lld %d AVE %s: %s:%d axi2af_parity_enable 0x%x\n"
+ "%lld %d AVE %s: %s::%s:%d %p %d AXI2AF parity register value 0x%x %d 0x%x 0x%x"
+ "%lld %d AVE %s: %s::%s:%d %p %d AXI2AF parity register value 0x%x %d 0x%x 0x%x\n"
+ "%lld %d AVE %s: %s::%s:%d %p %d AXI2AF register value 0x%x %d 0x%x 0x%x"
+ "%lld %d AVE %s: %s::%s:%d %p %d AXI2AF register value 0x%x %d 0x%x 0x%x\n"
+ "%lld %d AVE %s: %s::%s:%d %p %d | %p %d || %d %d %d 0x%llx %d || %p %d || 0x%x"
+ "%lld %d AVE %s: %s::%s:%d %p %d | %p %d || %d %d %d 0x%llx %d || %p %d || 0x%x\n"
+ "%lld %d AVE %s: %s::%s:%d %p %lld fail %d %d"
+ "%lld %d AVE %s: %s::%s:%d %p %lld fail %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | Incorrect number of LA stats %p %lld %d %d %d %d"
+ "%lld %d AVE %s: %s::%s:%d %s | Incorrect number of LA stats %p %lld %d %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to enable AXI2AF Parity %p %p %d"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to enable AXI2AF Parity %p %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d Invalid gopM %d"
+ "%lld %d AVE %s: %s::%s:%d Invalid gopM %d\n"
+ "21:28:58"
+ "904.97.1"
+ "CopyRCFrameStats"
+ "Oct  1 2025"
+ "SetParity"
+ "axi2af_parity_enable"
+ "iCount < sizeof(psParam->saLAStats) / sizeof(*psParam->saLAStats)"
- "\"0\" @%s:%d"
- "\"getQueueLength() + gopM <= m_queueSize\" @%s:%d"
- "\"iCount < sizeof(psParam->saLAStats) / sizeof(*psParam->saLAStats)\" @%s:%d"
- "\"m_cAnalyzer.getQueuedTotalCnt() >= frameNumberInGOP\" @%s:%d"
- "\"m_putCnt >= m_getCnt\" @%s:%d"
- "\"maxM == 4 || maxM == 2 || maxM == 1\" @%s:%d"
- "\"scenecut < (int32_t)gopM\" @%s:%d"
- "%lld %d AVE %s: %s:%d %d %d %d %d| %d %d | %d %d"
- "%lld %d AVE %s: %s:%d %d %d %d %d| %d %d | %d %d\n"
- "%lld %d AVE %s: %s:%d %s | invalid frame info %d %d"
- "%lld %d AVE %s: %s:%d %s | invalid frame info %d %d\n"
- "%lld %d AVE %s: %s:%d AXI2AF register value 0x%x %d 0x%x 0x%x"
- "%lld %d AVE %s: %s:%d AXI2AF register value 0x%x %d 0x%x 0x%x\n"
- "%lld %d AVE %s: %s:%d F %d PTS:%lld-%d, Hint:%d - %d"
- "%lld %d AVE %s: %s:%d F %d PTS:%lld-%d, Hint:%d - %d\n"
- "%lld %d AVE %s: %s:%d Frame disp %d FrameType %d"
- "%lld %d AVE %s: %s:%d Frame disp %d FrameType %d\n"
- "%lld %d AVE %s: %s::%s:%d %p %d | %p %d || %d %d %d 0x%llx %d || %p %d"
- "%lld %d AVE %s: %s::%s:%d %p %d | %p %d || %d %d %d 0x%llx %d || %p %d\n"
- "20:30:35"
- "904.88.0"
- "AVE_LAGOP.cpp"
- "Analyzer.cpp"
- "Analyzer.h"
- "Sep 16 2025"

```
