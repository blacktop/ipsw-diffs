## AppleAVE2FW_H15S.im4p

> `Firmware/ave/AppleAVE2FW_H15S.im4p`

```diff

 
-  __TEXT.__text: 0x10dbcc sha256:cb43db66ca227b449f3044fecc87dfc9e6d82c12ee62ec39352ba688c37c26bd
-  __TEXT.__const: 0x25dd4 sha256:03b80b7199d12e56411036eef066df8a13769c5967b0696bec985d459eb00a68
-  __TEXT.__cstring: 0x17974 sha256:f7d48859e09715f8191351709d84d50fa6cf56aa515304b84744a2aab9777aaa
+  __TEXT.__text: 0x10f404 sha256:edfbe9da3d26aa1f5ac465a807cbb27be679ea16899721b7fa03fe8f13ae65b1
+  __TEXT.__const: 0x25de4 sha256:8b27a69dc24ea4f1dcc975f746cac667c31ff0d815dbc8e1d073abebf4ab5340
+  __TEXT.__cstring: 0x17a2d sha256:0e3382bd833f492844efcb9b9e75a33532f06e7e1a3f3b343b6f2faf92fb0ae6
   __TEXT.__init_offsets: 0x0
-  __TEXT.__chain_starts: 0x18 sha256:18562f6640e514e188fea73125fcd146cdc7d79d7d15b4e19465ac991be31934
-  __DATA._rtk_patchbay: 0x211 sha256:25b99c115767cfd6df992b0aefb09ff5acc0e2a8bf7beb44b58979f84247441b
-  __DATA.__data: 0x11b0 sha256:535a742dcb9d9c5f5a0f493d25c0f2aea52246a2291cae783f67351d6db3f1c8
-  __DATA._rtk_mtab: 0x2d0 sha256:220a2339508ff7a49f6690c6392858376716a84a98c72966f6fb38755d140683
-  __DATA.__const: 0x3cc8 sha256:9d6fabb66d19f233b1a9c9f08e40521519297542bd3a72d7cd5018093338270c
-  __DATA._rtk_power: 0x3b8 sha256:20cfeb28e2da3c6e368713aa0d6d5037d659e8374c159e75ab8f3711c9244785
+  __TEXT.__chain_starts: 0x18 sha256:7ad3b784964fee099fad9d735acd81693422d3d631dbf7d0e35b28e3bb364588
+  __DATA._rtk_patchbay: 0x211 sha256:a2609f107d3226db2d384b50e8e200d2dc608a976f67e419c07244836eef0b5f
+  __DATA.__data: 0x11b0 sha256:5a27532214f350dc64ccfc47e7465f1797d85d1200ce51710b113a922618759a
+  __DATA._rtk_mtab: 0x2d0 sha256:1aaff40395107d59d52aab6e9aa5ca9111c0c8cd5c682198b2f4ac6b04504dba
+  __DATA.__const: 0x3cc8 sha256:a1a4bf00770846250204fdef76fc8cfd8cb46a10d390659e46ae9a8511fed1a6
+  __DATA._rtk_power: 0x3b8 sha256:ffbef00583bed4fe1ef9d18193c5709d50c07bfdbb3ad502ead4f2825ee205e8
   __DATA.__gxf_data: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   __DATA._rtk_tunables: 0x5b0 sha256:6b06640d4fe2ca4170b84c9c8083d4ceef29d646c40cb5431d64d14b10d735d3
   __DATA._rtk_init_stack: 0x10000 sha256:854fb91a21433799707bd85798d5fe48998be2719204088d0d153f31fdb39bd3

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xc9ba0 sha256:836743c6bab9eeae67a7fb8793769387fc4d3135fcadd27b0a77c5c7e3df5462
-  UUID: A4E54F57-4E4E-3EF1-AD41-485CC0FD4B19
-  Functions: 1214
-  Symbols:   1702
-  CStrings:  2680
+  UUID: 4D187F14-E8D5-31FA-A591-00382CCD4D99
+  Functions: 1216
+  Symbols:   1704
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
