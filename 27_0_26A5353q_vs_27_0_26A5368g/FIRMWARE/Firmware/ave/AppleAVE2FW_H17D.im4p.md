## AppleAVE2FW_H17D.im4p

> `Firmware/ave/AppleAVE2FW_H17D.im4p`

```diff

 
-  __TEXT.__text: 0x10fbb4 sha256:18454e28ed6d16183c06a3732d9363521628585585f3eef12b3e1888f0fea1cd
-  __TEXT.__const: 0x27c84 sha256:b2b8b2f2696015d7b366fb689dda0952500dc5c7c23564d95f44b194026fa2bc
-  __TEXT.__cstring: 0x17aeb sha256:5d189f4f1edda5805e9b374e171faac0554a75b4cacd20ebdb8cc5f97bbd6391
+  __TEXT.__text: 0x1114cc sha256:9615f531032c1d087b11d43aa448596c135b51aa8ac21b1181a66ed67601ccd4
+  __TEXT.__const: 0x27c84 sha256:60e030125811d3f35b7fc2a18f0f23f2877085fcde651d002a783800169ff35c
+  __TEXT.__cstring: 0x17ba4 sha256:5a85d7c08b3ec4f13e96e6e6e36a6c37fe852bbcd0eea419b95b61ddb4e6378d
   __TEXT.__init_offsets: 0x0
-  __TEXT.__chain_starts: 0x18 sha256:7ad3b784964fee099fad9d735acd81693422d3d631dbf7d0e35b28e3bb364588
-  __DATA._rtk_patchbay: 0x211 sha256:64466bf067323dd607c06ce46490e52d56f1a386b6ac7f0113e923e0d34b3279
-  __DATA.__data: 0x11b0 sha256:78f29c968928ca1d41d6ab02388688ea88e15f7226dbf6928a538ba0a9998e2e
-  __DATA._rtk_mtab: 0x2d0 sha256:29313195b4cc743520531d1774021b56b9b5a64c1e542b09eb08918597da1a68
-  __DATA.__const: 0x3cd8 sha256:12e1f4a41c0bd4926183227b1de66c377d0d5fa6539f164a577018e89380aa30
-  __DATA._rtk_power: 0x3b8 sha256:e6828a1dd8dd675f469d71ab662939c06e66b903a03452c10045b271478c6542
+  __TEXT.__chain_starts: 0x18 sha256:a3f88d70c32326ba262f0399f8c92eeb0c6fc950e59b330381eadc281cc2be4f
+  __DATA._rtk_patchbay: 0x211 sha256:be918ca05b169d3edfbea1e60287ed27e3efed11e1796ec11bf270177d847e97
+  __DATA.__data: 0x11b0 sha256:0c067ed68e7aa1a47f35b5339777a0364716acb0c527a46f2f0f7dbffe26ede4
+  __DATA._rtk_mtab: 0x2d0 sha256:9a5f37d29d4bdaa6de0709ac89a4aa567b88a7235909dc9a0335a09f3ade2882
+  __DATA.__const: 0x3cd8 sha256:a12cb31d0f2f5a397e5265f7fac8c8180132115a32b80c57037478a6aba26bb1
+  __DATA._rtk_power: 0x3b8 sha256:14d1d38e17d8548cb97ccd01351019e7406b452bbb052c3b1cdaa1ce6beb277d
   __DATA.__gxf_data: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   __DATA._rtk_tunables: 0x6a0 sha256:f8865ee4dde1dac4e24c54b47aa716bc60eee57282a3c933dc867ac972101c33
   __DATA._rtk_init_stack: 0x10000 sha256:854fb91a21433799707bd85798d5fe48998be2719204088d0d153f31fdb39bd3

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xd3720 sha256:2b1574a07080b1ff79ff78a60b2c30709d49c0d05b91838b8bb9d29e8607cf54
-  UUID: BE37BA83-41B3-3564-92BF-24DB0385CAE4
-  Functions: 1216
-  Symbols:   1706
-  CStrings:  2687
+  UUID: 7C89228A-5705-37B0-B8D6-461D409FD5D6
+  Functions: 1218
+  Symbols:   1708
+  CStrings:  2692
 
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
