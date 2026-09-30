## com.apple.driver.AppleAVE2

> `com.apple.driver.AppleAVE2`

```diff

-904.17.0.0.0
-  __TEXT.__const: 0x35320
-  __TEXT.__cstring: 0x40bdf
-  __TEXT.__os_log: 0x51232
-  __TEXT_EXEC.__text: 0x19c090
+904.33.0.0.0
+  __TEXT.__const: 0x420e0
+  __TEXT.__cstring: 0x4116a
+  __TEXT.__os_log: 0x516cc
+  __TEXT_EXEC.__text: 0x19dfa4
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0x2b8
   __DATA.__common: 0x130

   __DATA_CONST.__auth_ptr: 0x8
   __DATA_CONST.__mod_init_func: 0x38
   __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x7f98
+  __DATA_CONST.__const: 0x86c8
   __DATA_CONST.__kalloc_type: 0x4900
   __DATA_CONST.__kalloc_var: 0x2030
-  UUID: A5CD2F91-3420-3BEF-85EE-8A72E77D0720
-  Functions: 2838
+  UUID: E8DFA9F7-8A6C-304C-ACBA-8E436EE983CC
+  Functions: 2853
   Symbols:   0
-  CStrings:  8911
+  CStrings:  8960
 
CStrings:
+ "\"IOPBootup\" @%s:%d"
+ "\"iRevision < sizeof(gsc_saAVE_AXI2AF_Cfg_Ares_8160[0]) / sizeof(gsc_saAVE_AXI2AF_Cfg_Ares_8160[0][0])\" @%s:%d"
+ "\"iSVEID < sizeof(gsc_saAVE_AXI2AF_Cfg_Ares_8160) / sizeof(gsc_saAVE_AXI2AF_Cfg_Ares_8160[0])\" @%s:%d"
+ "%lld %d AVE %s: %s:%d %d %d %d %d| %d %d | %d %d"
+ "%lld %d AVE %s: %s:%d %d %d %d %d| %d %d | %d %d\n"
+ "%lld %d AVE %s: %s:%d %d %d | %d %d %d %d | %lld %d | %d %d"
+ "%lld %d AVE %s: %s:%d %d %d | %d %d %d %d | %lld %d | %d %d\n"
+ "%lld %d AVE %s: %s:%d %p %lld %p %p | %d %d %lld %d %d | %d %d"
+ "%lld %d AVE %s: %s:%d %p %lld %p %p | %d %d %lld %d %d | %d %d\n"
+ "%lld %d AVE %s: %s:%d Frame %d %d %d DS %p | %p %d %p | inter %d %d %d %d"
+ "%lld %d AVE %s: %s:%d Frame %d %d %d DS %p | %p %d %p | inter %d %d %d %d\n"
+ "%lld %d AVE %s: %s:%d invalid codec"
+ "%lld %d AVE %s: %s:%d invalid codec\n"
+ "%lld %d AVE %s: %s::%s Enter %p %d %d %d %d 0x%d"
+ "%lld %d AVE %s: %s::%s Enter %p %d %d %d %d 0x%d\n"
+ "%lld %d AVE %s: %s::%s Enter %p %d %d 0x%x"
+ "%lld %d AVE %s: %s::%s Enter %p %d %d 0x%x\n"
+ "%lld %d AVE %s: %s::%s Enter %p %lld %p %p %p %p %d %p %p %p %p %p"
+ "%lld %d AVE %s: %s::%s Enter %p %lld %p %p %p %p %d %p %p %p %p %p\n"
+ "%lld %d AVE %s: %s::%s Exit %p %d %d %d %d 0x%x %d"
+ "%lld %d AVE %s: %s::%s Exit %p %d %d %d %d 0x%x %d\n"
+ "%lld %d AVE %s: %s::%s Exit %p %d %d 0x%x"
+ "%lld %d AVE %s: %s::%s Exit %p %d %d 0x%x\n"
+ "%lld %d AVE %s: %s::%s Exit %p %d %d 0x%x %d"
+ "%lld %d AVE %s: %s::%s Exit %p %d %d 0x%x %d\n"
+ "%lld %d AVE %s: %s::%s Exit %p %lld %p %p %p %p %d %p %p %p %p %p %d"
+ "%lld %d AVE %s: %s::%s Exit %p %lld %p %p %p %p %d %p %p %p %p %p %d\n"
+ "%lld %d AVE %s: %s::%s:%d %p %d reset PSD state %s"
+ "%lld %d AVE %s: %s::%s:%d %p %d reset PSD state %s\n"
+ "%lld %d AVE %s: %s::%s:%d %p %lld %d Var %d Cost Intra %d Inter %d %d L0 %d L1 %d L0L1 %d"
+ "%lld %d AVE %s: %s::%s:%d %p %lld %d Var %d Cost Intra %d Inter %d %d L0 %d L1 %d L0L1 %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | PSD domain %s is not supported/enabled %p %d %d %d"
+ "%lld %d AVE %s: %s::%s:%d %s | PSD domain %s is not supported/enabled %p %d %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | PSD is not supported"
+ "%lld %d AVE %s: %s::%s:%d %s | PSD is not supported\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to allocate block buffer %p %lld %d"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to allocate block buffer %p %lld %d\n"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to reset PSD state %p %d %d 0x%x"
+ "%lld %d AVE %s: %s::%s:%d %s | failed to reset PSD state %p %d %d 0x%x\n"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong block buffer size %p %lld %p %p %p %p %d %p %p %p %p %p | %d %d"
+ "%lld %d AVE %s: %s::%s:%d %s | wrong block buffer size %p %lld %p %p %p %p %d %p %p %p %p %p | %d %d\n"
+ "%lld %d AVE %s: %s::%s:%d LRFS %p %p resolution %dx%d, zeroMVBinCnt[%d] = %d"
+ "%lld %d AVE %s: %s::%s:%d LRFS %p %p resolution %dx%d, zeroMVBinCnt[%d] = %d\n"
+ "%lld %d AVE %s: DevCap Throughput %s | %p | %d"
+ "%lld %d AVE %s: DevCap Throughput %s | %p | %d\n"
+ "%lld %d AVE %s: Throughput %p | %d - %d %d %lld %lld %d"
+ "%lld %d AVE %s: Throughput %p | %d - %d %d %lld %lld %d\n"
+ "%lld %d AVE %s: ThroughputMode %d"
+ "%lld %d AVE %s: ThroughputMode %d\n"
+ "%lld %d AVE %s: iOutputBufSizeFactor %d"
+ "%lld %d AVE %s: iOutputBufSizeFactor %d\n"
+ "(m_iHwFeature & AVE_DEVCAP_HW_FEATURE_PSD) != 0"
+ "111121211222222222222"
+ "1121122222222222222222222222222"
+ "1222221111111222221111"
+ "21122222222222222222222222222222222222222222222222222"
+ "23:07:03"
+ "904.33.0"
+ "AVE_Client_DecidePFThroughputMode"
+ "AVE_Enc_DecidePFThroughputMode"
+ "AVE_IOP_CheckIdle_Ares"
+ "AVE_IOP_Config_Ares"
+ "AVE_IOP_GetCurrTime_Ares"
+ "AVE_IOP_Start_Ares"
+ "CalcZeroMVBinCnt"
+ "DevCap Throughput %s | %p | %d"
+ "DevCap Throughput %s | %p | %d\n"
+ "Jun 30 2025"
+ "ResetPSD"
+ "Throughput %p | %d - %d %d %lld %lld %d"
+ "Throughput %p | %d - %d %d %lld %lld %d\n"
+ "ThroughputMode %d"
+ "ThroughputMode %d\n"
+ "iOutputBufSizeFactor %d"
+ "iOutputBufSizeFactor %d\n"
+ "pd < AVE_PMGR_PD_Max"
+ "piLFSResult != nullptr && 0 <= iRefIdx && iRefIdx <= 1 && piLRMEZeroMVBinCnt != nullptr"
- "%lld %d AVE %s: %s:%d %d %d %d DS %p | RS %d %p | inter %d %d %d %d"
- "%lld %d AVE %s: %s:%d %d %d %d DS %p | RS %d %p | inter %d %d %d %d\n"
- "%lld %d AVE %s: %s:%d %p %lld %p %p | %d %d %d %d %d %lld %d %d | %d %d %d"
- "%lld %d AVE %s: %s:%d %p %lld %p %p | %d %d %d %d %d %lld %d %d | %d %d %d\n"
- "%lld %d AVE %s: %s::%s Enter %p %lld %p %p %p %d %p %p %p"
- "%lld %d AVE %s: %s::%s Enter %p %lld %p %p %p %d %p %p %p\n"
- "%lld %d AVE %s: %s::%s Exit %p %lld %p %p %p %d %p %p %p %d"
- "%lld %d AVE %s: %s::%s Exit %p %lld %p %p %p %d %p %p %p %d\n"
- "%lld %d AVE %s: %s::%s:%d %p %lld %d Var %f Cost Intra %d Inter %d %d L0 %d L1 %d L0L1 %d"
- "%lld %d AVE %s: %s::%s:%d %p %lld %d Var %f Cost Intra %d Inter %d %d L0 %d L1 %d L0L1 %d\n"
- "%lld %d AVE %s: %s::%s:%d %s | wrong block buffer size %p %lld %p %p %p %d %p %p %p | %d %d"
- "%lld %d AVE %s: %s::%s:%d %s | wrong block buffer size %p %lld %p %p %p %d %p %p %p | %d %d\n"
- "%lld %d AVE %s: bPrioritizeEncodingSpeedOverQuality %d"
- "%lld %d AVE %s: bPrioritizeEncodingSpeedOverQuality %d\n"
- "%lld %d AVE %s: iOutputBufSizeFactor %d bPrioritizeEncodingSpeedOverQuality %d"
- "%lld %d AVE %s: iOutputBufSizeFactor %d bPrioritizeEncodingSpeedOverQuality %d\n"
- "11112111222222222222"
- "112112222222222222222222222222"
- "12221111111222221111"
- "20:54:44"
- "21122222222222222222222222222222222222222222222222"
- "904.17.0"
- "AVE_Client_DecideThroughputMode"
- "Jun 18 2025"
- "bPrioritizeEncodingSpeedOverQuality %d"
- "bPrioritizeEncodingSpeedOverQuality %d\n"
- "iOutputBufSizeFactor %d bPrioritizeEncodingSpeedOverQuality %d"
- "iOutputBufSizeFactor %d bPrioritizeEncodingSpeedOverQuality %d\n"

```
