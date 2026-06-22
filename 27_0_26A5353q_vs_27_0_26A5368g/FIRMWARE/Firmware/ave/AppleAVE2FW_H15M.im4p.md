## AppleAVE2FW_H15M.im4p

> `Firmware/ave/AppleAVE2FW_H15M.im4p`

```diff

 
-  __TEXT.__text: 0x10dc4c sha256:f22657d19cd9b2e171298ff08d1de0df0d310f7b8257950b4b95cc44c74f6bad
-  __TEXT.__const: 0x25de4 sha256:1c3ccda747b5a0ce796e5119b15411e49ac9c5b10e9e34fa342f1c1c9ea5733b
-  __TEXT.__cstring: 0x17974 sha256:f7d48859e09715f8191351709d84d50fa6cf56aa515304b84744a2aab9777aaa
+  __TEXT.__text: 0x10f484 sha256:723a6f3fe53d3722101dbfe6c98af4f795f912eeb5e374b9488ea3337a9c3c3c
+  __TEXT.__const: 0x25df4 sha256:44012e297b38e5b9ec5a6cadebbcbd8a19773703fad4b163ec1228bb5aaad3ed
+  __TEXT.__cstring: 0x17a2d sha256:0e3382bd833f492844efcb9b9e75a33532f06e7e1a3f3b343b6f2faf92fb0ae6
   __TEXT.__init_offsets: 0x0
-  __TEXT.__chain_starts: 0x18 sha256:18562f6640e514e188fea73125fcd146cdc7d79d7d15b4e19465ac991be31934
-  __DATA._rtk_patchbay: 0x211 sha256:a4cbae03bc4624555b3566118a10bf226635eb6f2892290369d51980c5da3345
-  __DATA.__data: 0x11b0 sha256:7f9bb34347df2ee6352ad08e30133692956163fafc07c93974c30a0eff164132
-  __DATA._rtk_mtab: 0x2d0 sha256:f776dd38cbab2e29e69e8ed53fba93d2fcfea13784b74ab48eab69eab05a5e84
-  __DATA.__const: 0x3cc8 sha256:42257b3f6c8c1ef6116d91474be853981a267c3fc533505afcc78f25da3d4d30
-  __DATA._rtk_power: 0x3b8 sha256:20cfeb28e2da3c6e368713aa0d6d5037d659e8374c159e75ab8f3711c9244785
+  __TEXT.__chain_starts: 0x18 sha256:7ad3b784964fee099fad9d735acd81693422d3d631dbf7d0e35b28e3bb364588
+  __DATA._rtk_patchbay: 0x211 sha256:12730a4c06c681a9aa4e52eca15ab86bdef003abc78c438f827de6203a8a4351
+  __DATA.__data: 0x11b0 sha256:23f4cddbb6ca6f9984428b3daf87160f21a295a3dd8d0838748f3d8d12551bee
+  __DATA._rtk_mtab: 0x2d0 sha256:5d3d26780f3ee334db2959f62246cc4a9c8dc772311df5a2de64c3f9f902dd6b
+  __DATA.__const: 0x3cc8 sha256:2f26ff17c7024332c17d03698b7a9ace7280e66dd05e885b90dbe85378092c11
+  __DATA._rtk_power: 0x3b8 sha256:ffbef00583bed4fe1ef9d18193c5709d50c07bfdbb3ad502ead4f2825ee205e8
   __DATA.__gxf_data: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   __DATA._rtk_tunables: 0x5b0 sha256:6b06640d4fe2ca4170b84c9c8083d4ceef29d646c40cb5431d64d14b10d735d3
   __DATA._rtk_init_stack: 0x10000 sha256:854fb91a21433799707bd85798d5fe48998be2719204088d0d153f31fdb39bd3

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xd3720 sha256:2b1574a07080b1ff79ff78a60b2c30709d49c0d05b91838b8bb9d29e8607cf54
-  UUID: 0963FD30-9E75-3F6F-A766-08E558696094
-  Functions: 1215
-  Symbols:   1703
-  CStrings:  2680
+  UUID: 1BE8E260-DF17-35C4-9409-EBD176F0F75E
+  Functions: 1217
+  Symbols:   1705
+  CStrings:  2685
 
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
