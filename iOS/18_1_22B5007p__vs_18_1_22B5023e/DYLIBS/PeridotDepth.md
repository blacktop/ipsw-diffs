## PeridotDepth

> `/System/Library/PrivateFrameworks/PeridotDepth.framework/PeridotDepth`

```diff

-37.0.0.0.0
-  __TEXT.__text: 0x10d604
-  __TEXT.__auth_stubs: 0x1770
+38.0.0.0.0
+  __TEXT.__text: 0x120c90
+  __TEXT.__auth_stubs: 0x17c0
   __TEXT.__objc_methlist: 0x1004
-  __TEXT.__gcc_except_tab: 0x733c
-  __TEXT.__cstring: 0x4b44
-  __TEXT.__const: 0x18290
+  __TEXT.__gcc_except_tab: 0x7564
+  __TEXT.__cstring: 0x4d9c
+  __TEXT.__const: 0x18540
   __TEXT.__oslogstring: 0x1242
-  __TEXT.__unwind_info: 0x19e0
+  __TEXT.__unwind_info: 0x1a70
   __TEXT.__eh_frame: 0x50
   __TEXT.__objc_classname: 0x1e1
-  __TEXT.__objc_methname: 0x4976
-  __TEXT.__objc_methtype: 0x588a
+  __TEXT.__objc_methname: 0x4985
+  __TEXT.__objc_methtype: 0x58d1
   __TEXT.__objc_stubs: 0x1f80
   __DATA_CONST.__got: 0x3f8
   __DATA_CONST.__const: 0x140

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xca8
   __DATA_CONST.__objc_superrefs: 0x70
-  __AUTH_CONST.__auth_got: 0xbc8
+  __AUTH_CONST.__auth_got: 0xbf0
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__const: 0x4e8
-  __AUTH_CONST.__cfstring: 0x3860
+  __AUTH_CONST.__cfstring: 0x39a0
   __AUTH_CONST.__objc_const: 0x2bc0
   __AUTH_CONST.__objc_floatobj: 0x10
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH.__objc_data: 0x3c0
-  __AUTH.__data: 0x8
+  __AUTH.__data: 0x18
   __DATA.__objc_ivar: 0x274
   __DATA.__data: 0x12770
   __DATA.__bss: 0x28a824

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1419
-  Symbols:   2028
-  CStrings:  1799
+  Functions: 1444
+  Symbols:   2059
+  CStrings:  1818
 
Symbols:
+ _CFDataGetBytes
+ _MGGetStringAnswer
+ _PDPeridotCalibCalibrationBlobsFromNVMForDevice
+ _PDPeridotCalibCopySerialNumber
+ __Z23peridot_depth_log_debugPKcz
+ __Z23peridot_depth_log_errorPKcz
+ __Z24nvmGetModuleSerialNumberPKhmRA32_c
+ __Z26bumpPeridotCalibOneVersionIN7peridot12CalibHistory2v813_PeridotCalibENS1_2v913_PeridotCalibEEvRKT_RT0_
+ __Z8nvmToFDRPK8__CFDataS1_PKcR11PeridotAFDR
+ __ZN16nvmGrnagerStruct20initNvmGrnagerStructEPhm
+ __ZN16nvmGrnagerStructC1EPK8__CFData
+ __ZN16nvmGrnagerStructC1Ev
+ __ZN16nvmGrnagerStructC2EPK8__CFData
+ __ZN16nvmGrnagerStructC2Ev
+ __ZN16nvmGrnagerStructD1Ev
+ __ZN16nvmGrnagerStructD2Ev
+ __ZN7peridot12CalibManager12blobsFromNVMEPK8__CFDataS3_PKc
+ __ZN7peridot12CalibManager16fillPeridotCalibEPK8__CFDataS3_PKcP13_PeridotCalib
+ __ZNSt3__112basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEE7replaceEmmPKcm
+ __ZNSt3__14stoiERKNS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEPmi
+ _peridot_depth_log_debug_function
+ _peridot_depth_log_error_function
+ _strchr
- __ZN7peridot12CalibManager12blobsFromNVMEPK8__CFDataS3_
CStrings:
+ "0123456789ABCDEFGHJKLMNPQRSTUVWXYZ"
+ "0123456789ABCDEFGHJKLMNPQRSTUVWXYZ+"
+ "?012345678??????9ABCDEFGHI??????JKLMNOPQRS??????TUVWXYZ+"
+ "@24@0:8^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?=[32c]{?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i}16"
+ "@32@0:8^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?=[32c]{?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i}16@24"
+ "@44@0:8r^f16Q24f32r^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?=[32c]{?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i}36"
+ "HWModelStr"
+ "NULL cfGrangerNVMBuffer detected"
+ "No backglass info for device %!s(MISSING). Will use defaults"
+ "No extrinsics info for device %!s(MISSING). Will use zeros"
+ "Reading quark NVM - unidentified logic mask id: %!f(MISSING)"
+ "T^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?=[32c]{?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i},N,V_unitInfo"
+ "T^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?=[32c]{?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i},R,N,V_unitInfo"
+ "Tr^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?=[32c]{?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i},N,V_unitInfo"
+ "^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?=[32c]{?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i}"
+ "^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?=[32c]{?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i}16@0:8"
+ "^{_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?=[32c]{?=[11d]ddd}[16C][16C]CCCCCCCC}}16@0:8"
+ "afdrDest.jlnl.Tx_VDDLAS != 0"
+ "extractFromCalsAndComp"
+ "fail to parse granger buffer"
+ "false && \"unknow comp buffer version\""
+ "null granger buffer"
+ "null quark buffer"
+ "nvmToFDR"
+ "nvmUtils.mm"
+ "pixelSkewUnpacked.size() == 4*2*14*138"
+ "r^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?=[32c]{?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i}"
+ "r^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?=[32c]{?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i}16@0:8"
+ "unknow VSR buffer version"
+ "unknow comp buffer version"
+ "unknown granger data"
+ "unsupported granger file version %!d(MISSING)"
+ "v24@0:8^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?=[32c]{?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i}16"
+ "v24@0:8r^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?=[32c]{?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i}16"
+ "{_PeridotCalib=\"version\"I\"stateFlags\"I\"vbdm\"{?=\"vbdSpx\"[16C]\"vbdSpBM\"S\"reserved\"S\"VBDadj\"[16f]\"VBD70C\"f\"VBD33C\"f\"VSPAD_OFFSET_TO_VBDDIE_70C\"f\"Tx_VDDLAS\"f}\"QE\"{?=\"QE\"[84[108f]]}\"nominalPDE\"{?=\"dtm\"[3f]\"dts\"[3f]\"meanPDE\"f\"sigmaPDE\"f}\"adcVoltageOffsets\"{?=\"dm_vddl2_measure_offset\"f\"dm_vddl1_measure_offset\"f\"dm_vddio_measure_offset\"f\"dm_vddh_measure_offset\"f}\"pulseShape\"{?=\"normalRange\"{?=\"banks\"[8{?=\"imPulseShape\"[64f]\"refStrayShape\"[64f]\"echoPulseShape\"[64f]\"tailParams\"[5f]}]}\"macroMode\"{?=\"banks\"[8{?=\"imPulseShape\"[64f]\"refStrayShape\"[64f]\"echoPulseShape\"[64f]\"tailParams\"[5f]}]}\"leftAnkleWavelength\"f\"rightAnkleWavelength\"f\"centroidWavelength\"f\"spectralWidth\"f}\"spots\"{?=\"banks\"[8{?=\"spots\"[14{?=\"emitterID\"C\"reserved\"[3C]\"spotSizeMacro\"f\"spotSizeNormal\"f\"spotContrastNormal\"f\"spotPowerWide\"f\"spotPowerNarrow\"f\"strayDRImpact\"f}]\"strayWP2NP\"f\"reserved\"f\"strayMap\"[84[108f]]}]\"calibSpotsGrangerTempMacro\"f\"calibSpotsGrangerTempNormal\"f\"calibSpotsQuarkNearTempMacro\"f\"calibSpotsQuarkNearTempNormal\"f}\"factorySpotLocations\"{?=\"normalRange\"{?=\"banks\"[8{?=\"spots\"[14{?=\"x\"f\"y\"f}]}]\"calibDistance\"f\"isSphere\"C\"reserved\"[3C]}\"macroMode\"{?=\"banks\"[8{?=\"spots\"[14{?=\"x\"f\"y\"f}]}]\"calibDistance\"f\"isSphere\"C\"reserved\"[3C]}}\"operationalSpotLocations\"{?=\"normalRange\"{?=\"banks\"[8{?=\"spots\"[14{?=\"x\"f\"y\"f}]}]\"calibDistance\"f\"isSphere\"C\"reserved\"[3C]}\"macroMode\"{?=\"banks\"[8{?=\"spots\"[14{?=\"x\"f\"y\"f}]}]\"calibDistance\"f\"isSphere\"C\"reserved\"[3C]}}\"nominalT0Ref\"{?=\"TRGOUTDLY\"s\"TDCOFSET_im_hs1\"S\"TDCOFSET_im_hs2\"S\"TDCOFSET_im_hp\"S\"TDCOFSET_ref\"S\"reserved\"s\"nomRef\"{?=\"banks\"[8{?=\"refs\"[4c]}]}}\"skews\"{?=\"pixelSkews\"{?=\"pixelSkews\"{?=\"tdcs\"[14{?=\"nominalPositions\"[4{?=\"hists\"[2{?=\"positions\"[150c]}]}]}]}\"pixelScale\"c\"P2PScanPatternVersion\"C\"reserved\"[6c]\"priConfigs\"[3{?=\"PLLFREQ_I\"S\"PLLFREQ_F_MSB\"C\"PLLFREQ_F_LSB\"C\"CCPRD\"C\"TRGNUM\"C\"reserved\"s}]}\"refSkews\"{?=\"refTimingGrangerTemperature\"f\"refTimingQuarkTemperature\"f\"refTimingVDDL1\"f\"refTimingVDDH\"f\"banks\"[8{?=\"refs\"[2{?=\"refIntensityNarrow\"f\"refIntensityWide\"f\"refTimingNarrow\"S\"refTimingWide\"S\"refFallingEdgeNarrow\"S\"refFallingEdgeWide\"S\"refRisingEdgeNarrow\"S\"refRisingEdgeWide\"S}]}]}\"straySkews\"{?=\"banks\"[8{?=\"widePulse\"[14s]\"narrowPulse\"[14s]}]}\"absSkews\"{?=\"banks\"[8{?=\"widePulse\"[14s]\"narrowPulse\"[14s]}]\"absSkewGrangerTemperature\"f\"absSkewQuarkTemperature\"f\"absSkewVDDL1\"f\"absSkewVDDH\"f}\"reserverd\"I}\"nvm\"{?=\"granger\"[896C]\"quark\"[32768C]}\"reserved2\"I\"irIntrinsics\"{?=\"efl\"d\"pixelSize\"d\"principalPoint\"[2d]\"undistortLUT\"[256d]\"distortLUT\"[256d]\"distortionCenter\"[2d]\"calibResX\"S\"calibResY\"S\"rsvd0\"I}\"factoryWideExtrinsics\"{?=\"rows\"[3[4d]]}\"operationalWideExtrinsics\"{?=\"rows\"[3[4d]]}\"additionalParams\"{?=\"serialNumber\"[32c]\"jlin\"{?=\"distortVendor\"[11d]\"tempSubstrate\"d\"tempProjector\"d\"tempSensor\"d}\"uuidFF\"[16C]\"uuidMPC\"[16C]\"jlnlVersion\"C\"jlpqVersion\"C\"jlpsVersion\"C\"jlnmVersion\"C\"jlskVersion\"C\"jlnvVersion\"C\"jlinVersion\"C\"jlexVersion\"C}}"
- "@24@0:8^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?={?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i}16"
- "@32@0:8^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?={?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i}16@24"
- "@44@0:8r^f16Q24f32r^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?={?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i}36"
- "T^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?={?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i},N,V_unitInfo"
- "T^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?={?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i},R,N,V_unitInfo"
- "Tr^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?={?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i},N,V_unitInfo"
- "^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?={?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i}"
- "^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?={?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i}16@0:8"
- "^{_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?={?=[11d]ddd}[16C][16C]CCCCCCCC}}16@0:8"
- "pCalib != nullptr"
- "parsing NVM not implemented yet"
- "r^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?={?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i}"
- "r^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?={?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i}16@0:8"
- "v24@0:8^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?={?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i}16"
- "v24@0:8r^{PeridotUnitInfo={_PeridotCalib=II{?=[16C]SS[16f]ffff}{?=[84[108f]]}{?=[3f][3f]ff}{?=ffff}{?={?=[8{?=[64f][64f][64f][5f]}]}{?=[8{?=[64f][64f][64f][5f]}]}ffff}{?=[8{?=[14{?=C[3C]ffffff}]ff[84[108f]]}]ffff}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?={?=[8{?=[14{?=ff}]}]fC[3C]}{?=[8{?=[14{?=ff}]}]fC[3C]}}{?=sSSSSs{?=[8{?=[4c]}]}}{?={?={?=[14{?=[4{?=[2{?=[150c]}]}]}]}cC[6c][3{?=SCCCCs}]}{?=ffff[8{?=[2{?=ffSSSSSS}]}]}{?=[8{?=[14s][14s]}]}{?=[8{?=[14s][14s]}]ffff}I}{?=[896C][32768C]}I{?=dd[2d][256d][256d][2d]SSI}{?=[3[4d]]}{?=[3[4d]]}{?={?=[11d]ddd}[16C][16C]CCCCCCCC}}@@{?=[8{?=[14{?=ff}]}]fC[3C]}i}16"
- "{_PeridotCalib=\"version\"I\"reserved\"I\"vbdm\"{?=\"vbdSpx\"[16C]\"vbdSpBM\"S\"reserved\"S\"VBDadj\"[16f]\"VBD70C\"f\"VBD33C\"f\"VSPAD_OFFSET_TO_VBDDIE_70C\"f\"Tx_VDDLAS\"f}\"QE\"{?=\"QE\"[84[108f]]}\"nominalPDE\"{?=\"dtm\"[3f]\"dts\"[3f]\"meanPDE\"f\"sigmaPDE\"f}\"adcVoltageOffsets\"{?=\"dm_vddl2_measure_offset\"f\"dm_vddl1_measure_offset\"f\"dm_vddio_measure_offset\"f\"dm_vddh_measure_offset\"f}\"pulseShape\"{?=\"normalRange\"{?=\"banks\"[8{?=\"imPulseShape\"[64f]\"refStrayShape\"[64f]\"echoPulseShape\"[64f]\"tailParams\"[5f]}]}\"macroMode\"{?=\"banks\"[8{?=\"imPulseShape\"[64f]\"refStrayShape\"[64f]\"echoPulseShape\"[64f]\"tailParams\"[5f]}]}\"leftAnkleWavelength\"f\"rightAnkleWavelength\"f\"centroidWavelength\"f\"spectralWidth\"f}\"spots\"{?=\"banks\"[8{?=\"spots\"[14{?=\"emitterID\"C\"reserved\"[3C]\"spotSizeMacro\"f\"spotSizeNormal\"f\"spotContrastNormal\"f\"spotPowerWide\"f\"spotPowerNarrow\"f\"strayDRImpact\"f}]\"strayWP2NP\"f\"reserved\"f\"strayMap\"[84[108f]]}]\"calibSpotsGrangerTempMacro\"f\"calibSpotsGrangerTempNormal\"f\"calibSpotsQuarkNearTempMacro\"f\"calibSpotsQuarkNearTempNormal\"f}\"factorySpotLocations\"{?=\"normalRange\"{?=\"banks\"[8{?=\"spots\"[14{?=\"x\"f\"y\"f}]}]\"calibDistance\"f\"isSphere\"C\"reserved\"[3C]}\"macroMode\"{?=\"banks\"[8{?=\"spots\"[14{?=\"x\"f\"y\"f}]}]\"calibDistance\"f\"isSphere\"C\"reserved\"[3C]}}\"operationalSpotLocations\"{?=\"normalRange\"{?=\"banks\"[8{?=\"spots\"[14{?=\"x\"f\"y\"f}]}]\"calibDistance\"f\"isSphere\"C\"reserved\"[3C]}\"macroMode\"{?=\"banks\"[8{?=\"spots\"[14{?=\"x\"f\"y\"f}]}]\"calibDistance\"f\"isSphere\"C\"reserved\"[3C]}}\"nominalT0Ref\"{?=\"TRGOUTDLY\"s\"TDCOFSET_im_hs1\"S\"TDCOFSET_im_hs2\"S\"TDCOFSET_im_hp\"S\"TDCOFSET_ref\"S\"reserved\"s\"nomRef\"{?=\"banks\"[8{?=\"refs\"[4c]}]}}\"skews\"{?=\"pixelSkews\"{?=\"pixelSkews\"{?=\"tdcs\"[14{?=\"nominalPositions\"[4{?=\"hists\"[2{?=\"positions\"[150c]}]}]}]}\"pixelScale\"c\"P2PScanPatternVersion\"C\"reserved\"[6c]\"priConfigs\"[3{?=\"PLLFREQ_I\"S\"PLLFREQ_F_MSB\"C\"PLLFREQ_F_LSB\"C\"CCPRD\"C\"TRGNUM\"C\"reserved\"s}]}\"refSkews\"{?=\"refTimingGrangerTemperature\"f\"refTimingQuarkTemperature\"f\"refTimingVDDL1\"f\"refTimingVDDH\"f\"banks\"[8{?=\"refs\"[2{?=\"refIntensityNarrow\"f\"refIntensityWide\"f\"refTimingNarrow\"S\"refTimingWide\"S\"refFallingEdgeNarrow\"S\"refFallingEdgeWide\"S\"refRisingEdgeNarrow\"S\"refRisingEdgeWide\"S}]}]}\"straySkews\"{?=\"banks\"[8{?=\"widePulse\"[14s]\"narrowPulse\"[14s]}]}\"absSkews\"{?=\"banks\"[8{?=\"widePulse\"[14s]\"narrowPulse\"[14s]}]\"absSkewGrangerTemperature\"f\"absSkewQuarkTemperature\"f\"absSkewVDDL1\"f\"absSkewVDDH\"f}\"reserverd\"I}\"nvm\"{?=\"granger\"[896C]\"quark\"[32768C]}\"reserved2\"I\"irIntrinsics\"{?=\"efl\"d\"pixelSize\"d\"principalPoint\"[2d]\"undistortLUT\"[256d]\"distortLUT\"[256d]\"distortionCenter\"[2d]\"calibResX\"S\"calibResY\"S\"rsvd0\"I}\"factoryWideExtrinsics\"{?=\"rows\"[3[4d]]}\"operationalWideExtrinsics\"{?=\"rows\"[3[4d]]}\"additionalParams\"{?=\"jlin\"{?=\"distortVendor\"[11d]\"tempSubstrate\"d\"tempProjector\"d\"tempSensor\"d}\"uuidFF\"[16C]\"uuidMPC\"[16C]\"jlnlVersion\"C\"jlpqVersion\"C\"jlpsVersion\"C\"jlnmVersion\"C\"jlskVersion\"C\"jlnvVersion\"C\"jlinVersion\"C\"jlexVersion\"C}}"

```
