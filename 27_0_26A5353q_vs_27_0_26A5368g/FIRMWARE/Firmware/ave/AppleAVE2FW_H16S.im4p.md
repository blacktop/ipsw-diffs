## AppleAVE2FW_H16S.im4p

> `Firmware/ave/AppleAVE2FW_H16S.im4p`

```diff

 
-  __TEXT.__text: 0x10f814 sha256:db9b3b53cc1b66ea1a58d44c35548b14c9f8cab819c0e30b82031ec40f6e4f94
-  __TEXT.__const: 0x27724 sha256:6e347a637786a4058cdb1027ffd2395d69bc0ff340f500dc72660c1127d25767
-  __TEXT.__cstring: 0x17abc sha256:62b7a767985ea49dcbfe74cd91137852a45ef19123ba063e1be91edbede7a4d4
+  __TEXT.__text: 0x11113c sha256:32cad4bad210ee5811d7395b0d2277be4fb70fc619b6bc0879040ad01608e64f
+  __TEXT.__const: 0x27724 sha256:f85e0a2de61cbc4aecdbd549fb49a97c910d561b752f510fa5ecab25f36aafd5
+  __TEXT.__cstring: 0x17b75 sha256:d610ebbff25acd0b2d0681ec894f77007cf4ef8303ec710a0824f57fa0028da3
   __TEXT.__init_offsets: 0x0
-  __TEXT.__chain_starts: 0x18 sha256:7ad3b784964fee099fad9d735acd81693422d3d631dbf7d0e35b28e3bb364588
-  __DATA._rtk_patchbay: 0x211 sha256:3bc0f818d78eda6e9a07da7cdafcf0673c5997dcaf6f4cbab1871bc172d75268
-  __DATA.__data: 0x11b0 sha256:89995789810da660eb9030c7a118ea9900697bffa81b523645e73e52c21cf326
-  __DATA._rtk_mtab: 0x2d0 sha256:dcab2c141b5d5f53f32ec7f07812760cbf14566f6561b4703f6a75a6ac361e62
-  __DATA.__const: 0x3cc8 sha256:b11ec2089cf2b0405ba0989dfb03bc6ab4c840b61e56c283416fd436a44cb3ca
-  __DATA._rtk_power: 0x3b8 sha256:ffbef00583bed4fe1ef9d18193c5709d50c07bfdbb3ad502ead4f2825ee205e8
+  __TEXT.__chain_starts: 0x18 sha256:a3f88d70c32326ba262f0399f8c92eeb0c6fc950e59b330381eadc281cc2be4f
+  __DATA._rtk_patchbay: 0x211 sha256:2d2038c8f4875803e7feab499274ed75a124986296805c62007613a7c0e9258d
+  __DATA.__data: 0x11b0 sha256:021f6282ee0e61d072e9156c0fed64d567ebfadd40d0592a8ea8f94bd19939ba
+  __DATA._rtk_mtab: 0x2d0 sha256:1cfe4d8e86ae37ed569785dce64714f8cfacfd078521c7d5ebbb78df92fa5871
+  __DATA.__const: 0x3cc8 sha256:c01ed02a8902f164021384b01e8514de24cbe272c7305a9eaf4cd0da55e03da6
+  __DATA._rtk_power: 0x3b8 sha256:368b227e2debd8e244ef2bfaccc096463d199c42a96673c428ffb8c8bec03b0e
   __DATA.__gxf_data: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   __DATA._rtk_tunables: 0x6a0 sha256:f8865ee4dde1dac4e24c54b47aa716bc60eee57282a3c933dc867ac972101c33
   __DATA._rtk_init_stack: 0x10000 sha256:854fb91a21433799707bd85798d5fe48998be2719204088d0d153f31fdb39bd3

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xc9ba0 sha256:836743c6bab9eeae67a7fb8793769387fc4d3135fcadd27b0a77c5c7e3df5462
-  UUID: E40FCEE7-71C9-3F87-A935-831DF4C55726
-  Functions: 1215
-  Symbols:   1704
-  CStrings:  2685
+  UUID: 92DC87DE-9940-3CDB-8F43-7F659E043D8C
+  Functions: 1217
+  Symbols:   1706
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
