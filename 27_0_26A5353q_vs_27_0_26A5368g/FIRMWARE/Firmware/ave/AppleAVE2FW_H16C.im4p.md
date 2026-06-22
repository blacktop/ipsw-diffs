## AppleAVE2FW_H16C.im4p

> `Firmware/ave/AppleAVE2FW_H16C.im4p`

```diff

 
-  __TEXT.__text: 0x10f914 sha256:18ff0aa515c8f7e9af14272269880d4d0c3ebc191313615afa59ff9cd1889838
-  __TEXT.__const: 0x27734 sha256:ae5e65f6df77750a7f1cbfdb93f3438713f43d0a9b95f383e8d037819b422d9c
-  __TEXT.__cstring: 0x17aeb sha256:ef3b47a3ba02df0c60283ab83b27d3d4b4bf334a676bf4747e380bf1035f58ec
+  __TEXT.__text: 0x11121c sha256:aa57970d94a9fe020f7a01aa4d8c40374486698cfd36b01cbd79bb3404fe16e6
+  __TEXT.__const: 0x27734 sha256:512e4d740a36ac2057b5f81a39d9cda4ccc59791a4718d8dd0852bfb7b6b5be5
+  __TEXT.__cstring: 0x17ba4 sha256:abd72b6ac09489c57696896c40ab12457f2b719123f07a61dff939b7767b5215
   __TEXT.__init_offsets: 0x0
-  __TEXT.__chain_starts: 0x18 sha256:7ad3b784964fee099fad9d735acd81693422d3d631dbf7d0e35b28e3bb364588
-  __DATA._rtk_patchbay: 0x211 sha256:55c771fdf73df7ce1ca3a9ce388acbb557319f56fb9b73c52cedabbc0895d944
-  __DATA.__data: 0x11b0 sha256:121e759cbfd4832aa37b2c668b1fda26263a64a8f5fee7eda7eb9ee6182fa538
-  __DATA._rtk_mtab: 0x2d0 sha256:12594cc5fbee3b7f5d0114bb99159ed155fd9e39a95a01240b0e731108197d67
-  __DATA.__const: 0x3cc8 sha256:317e4e8473fc3fc51052b7f6422772fda0a38d82cd393775a1d4b302b8e6f8c8
-  __DATA._rtk_power: 0x3b8 sha256:ffbef00583bed4fe1ef9d18193c5709d50c07bfdbb3ad502ead4f2825ee205e8
+  __TEXT.__chain_starts: 0x18 sha256:a3f88d70c32326ba262f0399f8c92eeb0c6fc950e59b330381eadc281cc2be4f
+  __DATA._rtk_patchbay: 0x211 sha256:f6238c3a55ff250d18357dac95fa57ab07b83b119c83ec8a14e1fb5c83f1e4a9
+  __DATA.__data: 0x11b0 sha256:3452b360aa45b7bad1ebe139be1834eed9ddb91aa034467ecdb83484d3ad1942
+  __DATA._rtk_mtab: 0x2d0 sha256:1056bf54d53379f4a225b5837296f93520fbeb91a5039ae38a46e2194f83f272
+  __DATA.__const: 0x3cc8 sha256:88b016a9c6a158809acf816029bea6951d06c19fc64c0f926f4c9bda81763a06
+  __DATA._rtk_power: 0x3b8 sha256:368b227e2debd8e244ef2bfaccc096463d199c42a96673c428ffb8c8bec03b0e
   __DATA.__gxf_data: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   __DATA._rtk_tunables: 0x6a0 sha256:f8865ee4dde1dac4e24c54b47aa716bc60eee57282a3c933dc867ac972101c33
   __DATA._rtk_init_stack: 0x10000 sha256:854fb91a21433799707bd85798d5fe48998be2719204088d0d153f31fdb39bd3

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xccf60 sha256:0a02aecfd94a55f4c8cdb644b6b1a58f09f492bb19fcad746f19027d817596e9
-  UUID: 17EC10E9-3C8A-387F-970A-A104E752215E
-  Functions: 1216
-  Symbols:   1706
-  CStrings:  2687
+  UUID: 8F1867CD-DA2C-3803-B431-034D6ED3718F
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
