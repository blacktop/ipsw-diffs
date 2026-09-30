## AppleAVE2FW_H17G.im4p

> `Firmware/ave/AppleAVE2FW_H17G.im4p`

```diff

 
-  __TEXT.__text: 0x10faa4 sha256:d419efb4de652ea084fe40a0a59e0494fc3c7ce57e3ad37d05c5354c6069b43a
-  __TEXT.__const: 0x258c4 sha256:dc1cf7cd2f2ab805f521d83ed3d28073adfbbaa7eacdad8791366375b11827cc
-  __TEXT.__cstring: 0x17abc sha256:b98029dc7441bf8f85a77b5d0152aa9d7c7d88a280d363e2234a723590de4bef
+  __TEXT.__text: 0x1113bc sha256:289f551d430d65f9206d9f59c18fc4d46c2c1037181117e965efca1c27d30794
+  __TEXT.__const: 0x258c4 sha256:f92dd3159faf50f816068a0bd6f23211421bdf0fe892db1f6059e8fad169b3cf
+  __TEXT.__cstring: 0x17b75 sha256:77a9909b300e99ac71b4717a3cf26142ff501ea1fbcf69fc8f366b88a73ade99
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x18 sha256:7ad3b784964fee099fad9d735acd81693422d3d631dbf7d0e35b28e3bb364588
-  __DATA._rtk_patchbay: 0x211 sha256:18504d79badda287280e881367e3d1a2a56f9eaeb5f292c6fcefe19a89ed5cba
-  __DATA.__data: 0x11b0 sha256:1206d4c9ff34d7300f40a322760a1c08d1f04e4a983f6b2b6a26ece3b5cf61ea
-  __DATA._rtk_mtab: 0x2d0 sha256:cae9d3c5336e2b088ba12f44e2e29fef9e7e26558b0c0711d92ec697075627a8
-  __DATA.__const: 0x3cd8 sha256:1fbde5d0618e5310bb320564b990e02b04f7142505715ead9f1dfb1553290d70
+  __DATA._rtk_patchbay: 0x211 sha256:e42fe07dc1cb2a749e880e0166391555132ffc2d74da74bda411f32210ac6ac1
+  __DATA.__data: 0x11b0 sha256:8925eac2113ace26ae366bbe41fc42984ff259fae782d4ff50ea96084e447d3e
+  __DATA._rtk_mtab: 0x2d0 sha256:c4df1bdd445358ab191fcbb63980c302c6c6d1209e9fcd92f223477297d14031
+  __DATA.__const: 0x3cd8 sha256:61179934a6f16b52dd1ad38a4420d98aee0ad5263c48de6f6a1b0215ff6e8c36
   __DATA._rtk_power: 0x3b8 sha256:e6828a1dd8dd675f469d71ab662939c06e66b903a03452c10045b271478c6542
   __DATA.__gxf_data: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   __DATA._rtk_tunables: 0x6a0 sha256:f8865ee4dde1dac4e24c54b47aa716bc60eee57282a3c933dc867ac972101c33

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xc9ba0 sha256:836743c6bab9eeae67a7fb8793769387fc4d3135fcadd27b0a77c5c7e3df5462
-  UUID: F3EB1BEF-977E-34B4-B2C8-D4B7AB77EBD7
-  Functions: 1215
-  Symbols:   1704
-  CStrings:  2685
+  UUID: 72FEB013-170D-34ED-92D5-6A7821EBD105
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
