## AppleAVE2FW_H19.im4p

> `Firmware/ave/AppleAVE2FW_H19.im4p`

### Sections with Same Size but Changed Content

- `__DATA._rtk_patchbay`
- `__DATA.__data`
- `__DATA._rtk_mtab`
- `__DATA._rtk_power`
- `__DATA.__mod_init_func`

```diff

-  __TEXT.__text: 0x1190b4
-  __TEXT.__const: 0x1dc34
-  __TEXT.__cstring: 0x1a383
+  __TEXT.__text: 0x11a074
+  __TEXT.__const: 0x1e034
+  __TEXT.__cstring: 0x1a5b1
   __TEXT.__init_offsets: 0x0
   __TEXT.__chain_starts: 0x1c
   __DATA._rtk_patchbay: 0x21a
   __DATA.__data: 0x1268
   __DATA._rtk_mtab: 0x298
-  __DATA.__const: 0x7598
+  __DATA.__const: 0x75b0
   __DATA._rtk_power: 0x3b8
   __DATA.__gxf_data: 0x10
   __DATA._rtk_tunables: 0x7e0

   __DATA._rtk_threads: 0x0
   __DATA.__constructor: 0x0
   __DATA.__zerofill: 0xc68e0
-  Functions: 1320
-  Symbols:   1802
-  CStrings:  2948
+  Functions: 1327
+  Symbols:   1807
+  CStrings:  2960
 
Symbols:
+ __Z19AVE_AV1_Quant_AcQtxiiiPi
+ __Z33AVE_AV1_Quant_Find_Qindex_For_AcQii
+ __ZN21ConstantQpRateControl11initRQModelEPv
+ __ZN21ConstantQpRateControl12InitQPLadderEv
+ __ZN21ConstantQpRateControl13updateFixedQPEi
CStrings:
+ "%s:%d %s | iBitDepth must be 8 or 10"
+ "%s::%s ConfigureMCPUs failed (%d)"
+ "%s::%s slice header count (%d) out of range [0, %d]"
+ "%s::%s:%d %s | GetSliceHeaderForFW rejected slice header (%d)"
+ "%s::%s:%d %s | setPipe failed (%d)"
+ "%s::%s:%d DTS %lld TimeScale %d m_fps %d.%02d"
+ "%s::%s:%d FixQp P/B QP configured without I QP, ladder base is the default %d (flag 0x%x)"
+ "%s::%s:%d FixQp ladder: encType %d base %d qpSet 0x%x -> %d %d %d %d %d (final step ratio x1000 %d %d %d %d %d)"
+ "%s::%s:%d FixQp: (%lld %lld) type %d tid %d ladder %d qp %d\n"
+ "9013.59.1"
+ "AVE_AV1_Quant_AcQtx"
+ "Caller is /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:1139"
+ "Caller is /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:1144"
+ "Caller is /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:1192"
+ "Caller is /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:1204"
+ "InitQPLadder"
+ "iBitDepth == 8 || iBitDepth == 10"
+ "iSlhBits >= 0"
+ "iSliceHdrBits >= 0"
- "%s::%s getPPSHeaderForFW count (%d) > length (%d)"
- "%s::%s:%d FixQp: %d\n"
- "9013.55.1"
- "Caller is /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:1019"
- "Caller is /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:1024"
- "Caller is /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:1072"
- "Caller is /Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/AppleAVE2FW/External/Algorithm/RateControl.cpp:1084"
```
