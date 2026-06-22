## AppleAVE2FW_H18.im4p

> `Firmware/ave/AppleAVE2FW_H18.im4p`

```diff

 
-  __TEXT.__text: 0x112044 sha256:0375e92738850b5f479745ec928e5a6b9463edbd805b50f28f26f36c09ab628b
-  __TEXT.__const: 0x20034 sha256:b6c8d8059ad7ae3daecdf33809e53918cde62052751d7c8334a0586e9cdccecf
-  __TEXT.__cstring: 0x19324 sha256:c0d64881929ddf4a84c769e7167496f5ed91a1d2a35be61b9f47250d6e7d878e
+  __TEXT.__text: 0x1136cc sha256:a73050f8be939a0ea734ae2aa2a2579c9aaf4413893867a2199d540f8641662f
+  __TEXT.__const: 0x2004c sha256:67a7dde3bbb48b763d3d5493bba44a74141221d9864dacb8615b89fc4ce8766f
+  __TEXT.__cstring: 0x1948d sha256:9cc0a8b2e4ca2bbff37bf29820bc1d6816a479071635386f2b4b064fbed8cc34
   __TEXT.__init_offsets: 0x0
-  __TEXT.__chain_starts: 0x18 sha256:5bda039a05f02bed9502f3dd53508683a0a8f3d3fb1dcdea82628ab9911ca88a
-  __DATA._rtk_patchbay: 0x211 sha256:eef2a6919fb7c4388ffb4ab981e9bf239a9eb82985970b21d26ca9e81614a344
-  __DATA.__data: 0x1590 sha256:c161f85d47bb1ecd65d7365840bbdc122e2c28ee666ba7c24289a4c2274f0cd8
-  __DATA._rtk_mtab: 0x2d0 sha256:e41b3fb7dc91c1ad846081762f3df0a8be3b8fb260ee19ad8b55a83ec4658782
-  __DATA.__const: 0x4710 sha256:6558182765d6a4960ed39d520204753bf54ed92bfc56dbda1157714e8d5c2ae0
-  __DATA._rtk_power: 0x3b8 sha256:cea1df9d7b1901b9225db2e37c527c3e42e91ff0eeebec5d230737e274af7cd6
+  __TEXT.__chain_starts: 0x18 sha256:a66e939319fe10cee87c0b138b311c4f9c8ad823069ea7e0ceed3a701effd880
+  __DATA._rtk_patchbay: 0x211 sha256:4aef4ecfe3b99a1ac93a3a468c230247f6264e523e4252a7f9e917001c90e089
+  __DATA.__data: 0x1590 sha256:25b7382351bac778ba0e90094300f693c1844436cf3827d7ea623487a58b879f
+  __DATA._rtk_mtab: 0x2d0 sha256:4c13837c966ac10e7a89952253d728909af37c6625824ca137f2537400843d2f
+  __DATA.__const: 0x4710 sha256:b6afa9c488e4505f7afcbc75df58f3d68f11208b67b75264377f04bad7bbaf3a
+  __DATA._rtk_power: 0x3b8 sha256:f62a18c22667a89eeec6b27e6460c650a52f2ddf98ae28351558bc1b920efe3a
   __DATA.__gxf_data: 0x10 sha256:374708fff7719dd5979ec875d56cd2286f6d3cf7ec317a3b25632aab28ec37bb
   __DATA._rtk_tunables: 0x6a0 sha256:f8865ee4dde1dac4e24c54b47aa716bc60eee57282a3c933dc867ac972101c33
   __DATA._rtk_init_stack: 0x10000 sha256:854fb91a21433799707bd85798d5fe48998be2719204088d0d153f31fdb39bd3

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xc6860 sha256:bf5ef433a609bc89609826bf7623544123e29cc764094d1e086760d92f943f86
-  UUID: 850E0E97-FDEF-3AED-A058-370D8689FA40
-  Functions: 1280
-  Symbols:   1785
-  CStrings:  2834
+  UUID: 78A3EA5F-76A4-3FDE-B4EB-9D4C449446A8
+  Functions: 1282
+  Symbols:   1787
+  CStrings:  2841
 
Symbols:
+ __ZN14AVE_PIODMACtrl5StartEjyjyjjj
+ __ZN15CMCTFController20LowLatencyCopyOutputEP14MCTF_FrameInfoP18AVE_PICMGMT_PARAMSb
+ __ZN15CMCTFController22GetStrengthTuningStatsEP14MCTF_FrameInfoP24sMctfStrengthTuningStats
+ __ZN15CMCTFController28MakeCompressedBufCopy_PIODMAEPPK15_S_AVE_CIBufExtPA2_S2_PA2_Kji
- __ZN14AVE_PIODMACtrl5StartEjyjyjj
- __ZN15CMCTFController20MakeFrameCopyForMCTFEPK20_S_AVE_CompressedBufP18AVE_PICMGMT_PARAMSbb
CStrings:
+ "%s:%d F %d after APL adjustment iMCTFStrength = %d "
+ "%s:%d F %d bGateOutCurrFrame %d iMCTFFilterStrength %d Gating En:%d"
+ "%s:%d gating: F %d  cap iMCTFStrength to 8"
+ "%s:%d gating: after previous frame strength adjustment  frame: %d  iMCTFStrength = %d "
+ "%s:%d gating: defore previous frame strength adjustment  frame: %d  iMCTFStrength = %d "
+ "%s:%d gating: from previous frame: %d  iMCTFStrengthStats = %d "
+ "%s:%d pipe FilterStrength_APLD = %d, FilterStrength_gradient =%d"
+ "(uint32_t)psSliceOffsetBuf[AVE_BufIdx_Header].iOffset + (((1152) + (32) - 1) & ~((32) - 1)) <= (uint32_t)EncCommParams.sSliceHeader.iSize"
+ "9013.12.1"
+ "Caller is /Library/Caches/com.apple.xbs/84CE49D2-F6DA-4B69-B0F2-7B946B205B16/TemporaryDirectory.6DQLGQ/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:855"
+ "Caller is /Library/Caches/com.apple.xbs/84CE49D2-F6DA-4B69-B0F2-7B946B205B16/TemporaryDirectory.6DQLGQ/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:860"
+ "Caller is /Library/Caches/com.apple.xbs/84CE49D2-F6DA-4B69-B0F2-7B946B205B16/TemporaryDirectory.6DQLGQ/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:901"
+ "Caller is /Library/Caches/com.apple.xbs/84CE49D2-F6DA-4B69-B0F2-7B946B205B16/TemporaryDirectory.6DQLGQ/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:913"
+ "Clearing output MCTF buffer for F%d bufIdx%d"
+ "GetStrengthTuningStats"
+ "MCTF PIODMA error:%d:[%d][%d] Dst: 0x%llx (Size:%d), Src: 0x%llx (Size:%d) CopySize:%u"
- "%s:%d F %d bGateOutCurrFrame %d iMCTFFilterStrength %d"
- "(shPos + 1) * (((((64) + (32) - 1) & ~((32) - 1))) > ((((1152) + (32) - 1) & ~((32) - 1))) ? ((((64) + (32) - 1) & ~((32) - 1))) : ((((1152) + (32) - 1) & ~((32) - 1)))) <= EncCommParams.sSliceHeader.iSize"
- "9012.99.0"
- "Caller is /Library/Caches/com.apple.xbs/1E0C5D33-D17B-4806-8C03-83FFDFD87C04/TemporaryDirectory.y2Ge43/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:853"
- "Caller is /Library/Caches/com.apple.xbs/1E0C5D33-D17B-4806-8C03-83FFDFD87C04/TemporaryDirectory.y2Ge43/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:858"
- "Caller is /Library/Caches/com.apple.xbs/1E0C5D33-D17B-4806-8C03-83FFDFD87C04/TemporaryDirectory.y2Ge43/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:899"
- "Caller is /Library/Caches/com.apple.xbs/1E0C5D33-D17B-4806-8C03-83FFDFD87C04/TemporaryDirectory.y2Ge43/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:911"
- "HH07172025 gating: %s:%d: F %d  cap iMCTFStrength to 8"
- "HH07182025 gating: %s:%d:after strength adjustment  frame: %d  iMCTFStrength = %d "

```
