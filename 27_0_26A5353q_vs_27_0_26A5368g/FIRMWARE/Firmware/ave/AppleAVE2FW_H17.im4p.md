## AppleAVE2FW_H17.im4p

> `Firmware/ave/AppleAVE2FW_H17.im4p`

```diff

 
-  __TEXT.__text: 0x10fb44 sha256:a822662f8465d4c82e171276e7d538e48fb0316886bf3e47c2d6fa0ad63d0026
-  __TEXT.__const: 0x266b4 sha256:80bfa7f69cd41142071ee6eea11fd4ecdab63baf8e3a924c47373c8f0fbd87be
-  __TEXT.__cstring: 0x17abe sha256:0b96977ed41546210f533439378e33f90691568fbb9656748e2c9119d7d573b4
+  __TEXT.__text: 0x11144c sha256:9ddd4250514ba96177aedc966f015a4768eb15fa33650d1054b4c64873125701
+  __TEXT.__const: 0x266b4 sha256:d2115cc9d15a07bd95fd9e9de614fc40e28b8ee739f9a9b8837c2ad9ec879997
+  __TEXT.__cstring: 0x17b77 sha256:52ab715764c2aa93a3170f5b5f4477021cfb8d7bd7c14c1f3ca5f56a93c7c75d
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18 sha256:7ad3b784964fee099fad9d735acd81693422d3d631dbf7d0e35b28e3bb364588
-  __DATA._rtk_patchbay: 0x211 sha256:87a22db44ca54c12ca35d8b299dc50419071fe39f5d87c3784fbeb7012bb3912
-  __DATA.__data: 0x11b0 sha256:6d5fb2cc1a805c5ae5042dcc439200d4ddd5635e2a0e4096f9550b4721ae98d1
-  __DATA._rtk_mtab: 0x2d0 sha256:14b5c969021db0782f01f90e0fa8a1c0500c0c4a3c0b13aec3c293b6a58ab5d2
-  __DATA.__const: 0x3cd8 sha256:98ed1a27f5fa6cfe749246c9921323358dd0dad284082cfb67d471fad50a850e
+  __DATA._rtk_patchbay: 0x211 sha256:9ae075fc1b584afb30a0574a730ec99cb753609131fc1a224f3f580fd4008fa1
+  __DATA.__data: 0x11b0 sha256:015af7fd11f369919d5c6a95cd894e31ea35d914e5e548f7d6f8326b0a75f740
+  __DATA._rtk_mtab: 0x2d0 sha256:017a5723120414151df085aa96d48388ca38ab5f6734bb813658251b30658dc5
+  __DATA.__const: 0x3cd8 sha256:2b03d75111dcfc4ffb3887850df5933d669c7373563a2bb1c59ed7f14d134fd9
   __DATA._rtk_power: 0x3b8 sha256:e6828a1dd8dd675f469d71ab662939c06e66b903a03452c10045b271478c6542
   __DATA.__gxf_data: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   __DATA._rtk_tunables: 0x6a0 sha256:f8865ee4dde1dac4e24c54b47aa716bc60eee57282a3c933dc867ac972101c33

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xccf60 sha256:0a02aecfd94a55f4c8cdb644b6b1a58f09f492bb19fcad746f19027d817596e9
-  UUID: 8089B438-B299-357B-AFBB-3F67A6E7CEA5
-  Functions: 1216
-  Symbols:   1705
-  CStrings:  2685
+  UUID: B7C4FFCF-D0DA-3C67-91DD-75022F74B813
+  Functions: 1218
+  Symbols:   1707
+  CStrings:  2690
 
Symbols:
+ __ZN14AVE_PIODMACtrl5StartEjyjyjjj
+ __ZN15CMCTFController20LowLatencyCopyOutputEP14MCTF_FrameInfoP18AVE_PICMGMT_PARAMSb
+ __ZN15CMCTFController22GetStrengthTuningStatsEP14MCTF_FrameInfoP24sMctfStrengthTuningStats
+ __ZN15CMCTFController28MakeCompressedBufCopy_PIODMAEPPK15_S_AVE_CIBufExtPA2_S2_PA2_Kji
- __ZN14AVE_PIODMACtrl5StartEjyjyjj
- __ZN15CMCTFController20MakeFrameCopyForMCTFEPK20_S_AVE_CompressedBufP18AVE_PICMGMT_PARAMSbb
CStrings:
+ "%s::%s:%d %p bufIdx %u AvgMvX = %d, AvgMvY = %d"
+ "%s::%s:%d %p bufIdx %u AvgSADY = %d AvgSADUV = %d"
+ "(uint32_t)psSliceOffsetBuf[AVE_BufIdx_Header].iOffset + (((1152) + (32) - 1) & ~((32) - 1)) <= (uint32_t)EncCommParams.sSliceHeader.iSize"
+ "/AppleInternal/Library/BuildRoots/4~CRjhugDJia0PCW_Ej3Zq9XWFHp0LcVl0KeXY2WQ/Library/Caches/com.apple.xbs/TemporaryDirectory.jAk0EN/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp"
+ "9013.12.1"
+ "Caller is /AppleInternal/Library/BuildRoots/4~CRjhugDJia0PCW_Ej3Zq9XWFHp0LcVl0KeXY2WQ/Library/Caches/com.apple.xbs/TemporaryDirectory.jAk0EN/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:855"
+ "Caller is /AppleInternal/Library/BuildRoots/4~CRjhugDJia0PCW_Ej3Zq9XWFHp0LcVl0KeXY2WQ/Library/Caches/com.apple.xbs/TemporaryDirectory.jAk0EN/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:860"
+ "Caller is /AppleInternal/Library/BuildRoots/4~CRjhugDJia0PCW_Ej3Zq9XWFHp0LcVl0KeXY2WQ/Library/Caches/com.apple.xbs/TemporaryDirectory.jAk0EN/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:901"
+ "Caller is /AppleInternal/Library/BuildRoots/4~CRjhugDJia0PCW_Ej3Zq9XWFHp0LcVl0KeXY2WQ/Library/Caches/com.apple.xbs/TemporaryDirectory.jAk0EN/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:913"
+ "Clearing output MCTF buffer for F%d bufIdx%d"
+ "GetStrengthTuningStats"
+ "MCTF PIODMA error:%d:[%d][%d] Dst: 0x%llx (Size:%d), Src: 0x%llx (Size:%d) CopySize:%u"
- "(shPos + 1) * (((((64) + (32) - 1) & ~((32) - 1))) > ((((1152) + (32) - 1) & ~((32) - 1))) ? ((((64) + (32) - 1) & ~((32) - 1))) : ((((1152) + (32) - 1) & ~((32) - 1)))) <= EncCommParams.sSliceHeader.iSize"
- "/AppleInternal/Library/BuildRoots/4~CRCFugD1eH5DWV0EFgNEFz-18_vlxEAQqwd7MYU/Library/Caches/com.apple.xbs/TemporaryDirectory.I6bXau/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp"
- "9012.99.0"
- "Caller is /AppleInternal/Library/BuildRoots/4~CRCFugD1eH5DWV0EFgNEFz-18_vlxEAQqwd7MYU/Library/Caches/com.apple.xbs/TemporaryDirectory.I6bXau/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:853"
- "Caller is /AppleInternal/Library/BuildRoots/4~CRCFugD1eH5DWV0EFgNEFz-18_vlxEAQqwd7MYU/Library/Caches/com.apple.xbs/TemporaryDirectory.I6bXau/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:858"
- "Caller is /AppleInternal/Library/BuildRoots/4~CRCFugD1eH5DWV0EFgNEFz-18_vlxEAQqwd7MYU/Library/Caches/com.apple.xbs/TemporaryDirectory.I6bXau/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:899"
- "Caller is /AppleInternal/Library/BuildRoots/4~CRCFugD1eH5DWV0EFgNEFz-18_vlxEAQqwd7MYU/Library/Caches/com.apple.xbs/TemporaryDirectory.I6bXau/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:911"

```
