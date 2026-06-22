## AppleAVE2FW_H16G.im4p

> `Firmware/ave/AppleAVE2FW_H16G.im4p`

```diff

 
-  __TEXT.__text: 0x10f824 sha256:7fa99577bec967c81efc71340aa297c16db359d5fafb043cc3ce35c76b7721f7
-  __TEXT.__const: 0x258b4 sha256:9e7e31af9656dd64b98c54bea480bedd8f9da1e40cdf8abce6aa3c573cb7e990
-  __TEXT.__cstring: 0x17abb sha256:a9db52e2170bc9a5c89dfcdb26ac6d5b2fa7c1ed05678dde68e98e8178948d37
+  __TEXT.__text: 0x11113c sha256:6a42593aee17bdea4f16ee73bd7857b68311828fded0f25c0e3262e058f9d9b6
+  __TEXT.__const: 0x258b4 sha256:3e851f04d5080488ff4bf76794272a1cad512b62fabc8d05b10bc64a27a94639
+  __TEXT.__cstring: 0x17b74 sha256:326043e3e680af2107db5e05b17df64092f762589ae3c306c6483bc8639fcbce
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18 sha256:7ad3b784964fee099fad9d735acd81693422d3d631dbf7d0e35b28e3bb364588
-  __DATA._rtk_patchbay: 0x211 sha256:a558c0b8663aafc19de93b1984990b431bd61a51d07a3d52dfa856be728a3bc3
-  __DATA.__data: 0x11b0 sha256:128d471cc5d49d87bbfe016e711abc3042e5767e301201d0f710ed9b4b653a19
-  __DATA._rtk_mtab: 0x2d0 sha256:9c665e4e2ac24dd511825982aebf3e64db0d139c599b1f435dbecfec0edeaca4
-  __DATA.__const: 0x3cd8 sha256:6106f1b2d5ab121ad9530dfdda089c3d46a34b1a1dab2c7e5b70e5d38dcd9532
+  __DATA._rtk_patchbay: 0x211 sha256:bdc561fc140f4ecf2a38078b31abe1ba2cc87e850f2befda9619f87408ae20d9
+  __DATA.__data: 0x11b0 sha256:7468bf9e4b51a34aff46b99780836d68b897c14393604f870b0e7ae187ccb9e7
+  __DATA._rtk_mtab: 0x2d0 sha256:1cfe4d8e86ae37ed569785dce64714f8cfacfd078521c7d5ebbb78df92fa5871
+  __DATA.__const: 0x3cd8 sha256:df12c5cf9caad53027f8d55767b348ef21c359e926efa62dc1c8334d2f33a928
   __DATA._rtk_power: 0x3b8 sha256:e6828a1dd8dd675f469d71ab662939c06e66b903a03452c10045b271478c6542
   __DATA.__gxf_data: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   __DATA._rtk_tunables: 0x6a0 sha256:f8865ee4dde1dac4e24c54b47aa716bc60eee57282a3c933dc867ac972101c33

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xc9ba0 sha256:836743c6bab9eeae67a7fb8793769387fc4d3135fcadd27b0a77c5c7e3df5462
-  UUID: 6ACF41AF-6A9C-3A2A-BA09-F5FAE72E9E88
-  Functions: 1215
-  Symbols:   1704
-  CStrings:  2685
+  UUID: 027B463F-9C2F-30B9-BB21-0155683CA177
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
