## AppleAVE2FW_H15G.im4p

> `Firmware/ave/AppleAVE2FW_H15G.im4p`

```diff

 
-  __TEXT.__text: 0xf3e0c sha256:7b8cc41a568ced7f304900d4b21bbb50a9646da2ec6f8c1d4553ca611c39f8e9
-  __TEXT.__const: 0x21754 sha256:036c194f20e9f894727bdce905ae8e401156abf271c1268a4b6882be5c8248e1
-  __TEXT.__cstring: 0x1625b sha256:9e42506c4b294fcd36c75cde169595ff69c64773c78b6a8fdc4658cc71544c7b
+  __TEXT.__text: 0xf4e50 sha256:edabb4476385858c61f21eedf50b146466201395b6537ce615adc4afa431d5bf
+  __TEXT.__const: 0x21754 sha256:e0c12529ae9371d1a4608521a39d385596be87101698ae51dfdce6af02cbcc36
+  __TEXT.__cstring: 0x16314 sha256:ceea67f08e31c1899baaeb56ec06cb69e330641ccd364f8eb2e03bf0b1c6c780
   __TEXT.__init_offsets: 0x0
-  __TEXT.__chain_starts: 0x18 sha256:b2fb9f49815b5b0f60df7f1966aa7a20c117b60b0f5df53ec49490d80413abfa
-  __DATA._rtk_patchbay: 0x211 sha256:c73654ed2e85faa9f95d0604360be9bc26c7dc9c619be509433e24a7d5106234
-  __DATA.__data: 0x1190 sha256:9c9dc40e05a65a10420dae6aaddc3aa27c203cd0827c68792a071a91357cd576
-  __DATA._rtk_mtab: 0x2d0 sha256:03614f073682db451f30fc50a09f623df738cdcd7f8878c3db5d974ffd79d76b
-  __DATA.__const: 0x3b60 sha256:3bebd0b1148387a3fa1152b2ce2c97c70c13962db1d657fb976400ae5a31a4a3
-  __DATA._rtk_power: 0x3b8 sha256:9918326c591731d37beebc15b916b54b8bdab3ad50a3513cae704ee1ae080cf6
+  __TEXT.__chain_starts: 0x18 sha256:32157f04dd2c2462bf5bee5e478a9899d168eaf4662ac24d1cc4c8e3dfab2e72
+  __DATA._rtk_patchbay: 0x211 sha256:ca5b89df6d08bac6b36207a11b14060308689943c1f4a2a58fdf51270bac6442
+  __DATA.__data: 0x1190 sha256:010f0b65aa7e556c353f79e0c1abfa0dabf52cdebfd58419f68acb6f0b16e1d8
+  __DATA._rtk_mtab: 0x2d0 sha256:ebd8ef2e74694b92dd4a19046dcc9a9bac951f0222b98af50f58f2799150679d
+  __DATA.__const: 0x3b60 sha256:daa0400d0baf3cd4f5d0149ecf769eb735da8a7bf97fc461b7b2ca8cc698ff71
+  __DATA._rtk_power: 0x3b8 sha256:e77ab39a0b563b53ae64cfbfd12c23ffa9ccf3127163deffdf9156eb12ad0362
   __DATA.__gxf_data: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   __DATA._rtk_tunables: 0x5b0 sha256:6b06640d4fe2ca4170b84c9c8083d4ceef29d646c40cb5431d64d14b10d735d3
   __DATA._rtk_init_stack: 0x10000 sha256:854fb91a21433799707bd85798d5fe48998be2719204088d0d153f31fdb39bd3

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xc67e0 sha256:97e2b894ee672676e83a96e0cb7b5fc8d793571b1b78a2b22f15e2ec5f1cc957
-  UUID: A692663E-B615-34ED-8CD5-D75FC458D5CB
-  Functions: 1166
-  Symbols:   1617
-  CStrings:  2514
+  UUID: 6CF15AC0-B288-3625-8869-3717C3313E12
+  Functions: 1168
+  Symbols:   1619
+  CStrings:  2519
 
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
