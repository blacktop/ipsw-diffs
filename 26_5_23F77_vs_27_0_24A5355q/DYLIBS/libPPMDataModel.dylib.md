## libPPMDataModel.dylib

> `/usr/lib/libPPMDataModel.dylib`

```diff

-1035.100.47.0.0
-  __TEXT.__text: 0xbfc4
-  __TEXT.__auth_stubs: 0x1e0
+1177.0.0.502.4
+  __TEXT.__text: 0xc0dc
   __TEXT.__objc_methlist: 0xfb4
-  __TEXT.__cstring: 0x4b5
-  __TEXT.__unwind_info: 0x280
-  __TEXT.__objc_classname: 0x41
-  __TEXT.__objc_methname: 0x2606
-  __TEXT.__objc_methtype: 0x275
-  __TEXT.__objc_stubs: 0x1440
-  __DATA_CONST.__got: 0x38
+  __TEXT.__cstring: 0x4be
+  __TEXT.__unwind_info: 0x1e8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa50
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0xf8
+  __DATA_CONST.__got: 0x38
   __AUTH_CONST.__cfstring: 0x8c0
   __AUTH_CONST.__objc_const: 0x12f0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x10c
   __DATA.__data: 0x60

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 30669965-A620-3BF7-812A-5EE218593223
+  UUID: D86CBB93-2AC2-343D-854E-EB954E761D53
   Functions: 335
-  Symbols:   967
-  CStrings:  606
+  Symbols:   965
+  CStrings:  140
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_release_x9
- _objc_release_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
- _objc_retain_x21
Functions:
~ -[OTAResistanceData resistance25Cs] : 16 -> 20
~ -[OTAResistanceData resistance25CAtIndex:] : 188 -> 180
~ -[OTAResistanceData temperatureCoeffs] : 16 -> 20
~ -[OTAResistanceData temperatureCoeffAtIndex:] : 188 -> 180
~ -[OTAResistanceData description] : 176 -> 164
~ -[OTAResistanceData dictionaryRepresentation] : 188 -> 176
~ _OTAResistanceDataReadFrom : 1088 -> 1072
~ -[OTAResistanceData writeTo:] : 196 -> 208
~ -[OTAResistanceData mergeFrom:] : 184 -> 176
~ -[OTAParamRC hasR0] : 24 -> 28
~ -[OTAParamRC hasR1] : 24 -> 28
~ -[OTAParamRC hasBaselineR1] : 24 -> 28
~ -[OTAParamRC hasR2] : 24 -> 28
~ -[OTAParamRC hasBaselineR2] : 24 -> 28
~ -[OTAParamRC hasRCFreq1] : 24 -> 28
~ -[OTAParamRC hasRCFreq2] : 24 -> 28
~ -[OTAParamRC hasRCFreq3] : 24 -> 28
~ -[OTAParamRC agingCoeffForR0s] : 16 -> 20
~ -[OTAParamRC agingCoeffForR0AtIndex:] : 188 -> 180
~ -[OTAParamRC agingCoeffForR0TemperatureCoeffs] : 16 -> 20
~ -[OTAParamRC agingCoeffForR0TemperatureCoeffAtIndex:] : 188 -> 180
~ -[OTAParamRC agingCoeffForR1s] : 16 -> 20
~ -[OTAParamRC agingCoeffForR1AtIndex:] : 188 -> 180
~ -[OTAParamRC agingCoeffForR1TemperatureCoeffs] : 16 -> 20
~ -[OTAParamRC agingCoeffForR1TemperatureCoeffAtIndex:] : 188 -> 180
~ -[OTAParamRC agingCoeffForR2s] : 16 -> 20
~ -[OTAParamRC agingCoeffForR2AtIndex:] : 188 -> 180
~ -[OTAParamRC agingCoeffForR2TemperatureCoeffs] : 16 -> 20
~ -[OTAParamRC agingCoeffForR2TemperatureCoeffAtIndex:] : 188 -> 180
~ -[OTAParamRC baselineRdcs] : 16 -> 20
~ -[OTAParamRC baselineRdcAtIndex:] : 188 -> 180
~ -[OTAParamRC hasBaselineR0] : 24 -> 28
~ -[OTAParamRC hasBmuResistance] : 24 -> 28
~ -[OTAParamRC gridOCVs] : 16 -> 20
~ -[OTAParamRC gridOCVAtIndex:] : 188 -> 180
~ -[OTAParamRC hasBaselineR3] : 24 -> 28
~ -[OTAParamRC setMaxRdcRatio:] : 36 -> 44
~ -[OTAParamRC setHasMaxRdcRatio:] : 40 -> 44
~ -[OTAParamRC hasMaxRdcRatio] : 20 -> 24
~ -[OTAParamRC setMaxRdcRatioR2Extrap:] : 36 -> 44
~ -[OTAParamRC setHasMaxRdcRatioR2Extrap:] : 40 -> 44
~ -[OTAParamRC hasMaxRdcRatioR2Extrap] : 20 -> 24
~ -[OTAParamRC setBaselineWRdc:] : 36 -> 44
~ -[OTAParamRC setHasBaselineWRdc:] : 28 -> 32
~ -[OTAParamRC hasBaselineWRdc] : 20 -> 24
~ -[OTAParamRC slopeForR0Extraps] : 16 -> 20
~ -[OTAParamRC slopeForR0ExtrapAtIndex:] : 188 -> 180
~ -[OTAParamRC slopeForR1Extraps] : 16 -> 20
~ -[OTAParamRC slopeForR1ExtrapAtIndex:] : 188 -> 180
~ -[OTAParamRC slopeForR2Extraps] : 16 -> 20
~ -[OTAParamRC slopeForR2ExtrapAtIndex:] : 188 -> 180
~ -[OTAParamRC slopeForR3Extraps] : 16 -> 20
~ -[OTAParamRC slopeForR3ExtrapAtIndex:] : 188 -> 180
~ -[OTAParamRC hasR3] : 24 -> 28
~ -[OTAParamRC hasRCFreq4] : 24 -> 28
~ -[OTAParamRC hasBaselineR4] : 24 -> 28
~ -[OTAParamRC hasBaselineRCFreq1] : 24 -> 28
~ -[OTAParamRC hasBaselineRCFreq2] : 24 -> 28
~ -[OTAParamRC hasBaselineRCFreq3] : 24 -> 28
~ -[OTAParamRC hasBaselineRCFreq4] : 24 -> 28
~ -[OTAParamRC agingCoeffForR3s] : 16 -> 20
~ -[OTAParamRC agingCoeffForR3AtIndex:] : 188 -> 180
~ -[OTAParamRC agingCoeffForR3TemperatureCoeffs] : 16 -> 20
~ -[OTAParamRC agingCoeffForR3TemperatureCoeffAtIndex:] : 188 -> 180
~ -[OTAParamRC agingCoeffForRCFreq1s] : 16 -> 20
~ -[OTAParamRC agingCoeffForRCFreq1AtIndex:] : 188 -> 180
~ -[OTAParamRC agingCoeffForRCFreq2s] : 16 -> 20
~ -[OTAParamRC agingCoeffForRCFreq2AtIndex:] : 188 -> 180
~ -[OTAParamRC agingCoeffForRCFreq3s] : 16 -> 20
~ -[OTAParamRC agingCoeffForRCFreq3AtIndex:] : 188 -> 180
~ -[OTAParamRC agingCoeffForRCFreq4s] : 16 -> 20
~ -[OTAParamRC agingCoeffForRCFreq4AtIndex:] : 188 -> 180
~ -[OTAParamRC agingCoeffForRCFreq1TemperatureCoeffs] : 16 -> 20
~ -[OTAParamRC agingCoeffForRCFreq1TemperatureCoeffAtIndex:] : 188 -> 180
~ -[OTAParamRC agingCoeffForRCFreq2TemperatureCoeffs] : 16 -> 20
~ -[OTAParamRC agingCoeffForRCFreq2TemperatureCoeffAtIndex:] : 188 -> 180
~ -[OTAParamRC agingCoeffForRCFreq3TemperatureCoeffs] : 16 -> 20
~ -[OTAParamRC agingCoeffForRCFreq3TemperatureCoeffAtIndex:] : 188 -> 180
~ -[OTAParamRC agingCoeffForRCFreq4TemperatureCoeffs] : 16 -> 20
~ -[OTAParamRC agingCoeffForRCFreq4TemperatureCoeffAtIndex:] : 188 -> 180
~ -[OTAParamRC mLBConfig] : 40 -> 48
~ -[OTAParamRC setMLBConfig:] : 36 -> 44
~ -[OTAParamRC setHasMLBConfig:] : 40 -> 44
~ -[OTAParamRC hasMLBConfig] : 20 -> 24
~ -[OTAParamRC mLBConfigAsString:] : 136 -> 132
~ -[OTAParamRC StringAsMLBConfig:] : 92 -> 88
~ -[OTAParamRC setWRdcRatioThresh:] : 36 -> 44
~ -[OTAParamRC setHasWRdcRatioThresh:] : 40 -> 44
~ -[OTAParamRC hasWRdcRatioThresh] : 20 -> 24
~ -[OTAParamRC gridWRdcRatios] : 16 -> 20
~ -[OTAParamRC gridWRdcRatioAtIndex:] : 188 -> 180
~ -[OTAParamRC coeffSOCs] : 16 -> 20
~ -[OTAParamRC coeffSOCAtIndex:] : 188 -> 180
~ -[OTAParamRC coeffVs] : 16 -> 20
~ -[OTAParamRC coeffVAtIndex:] : 188 -> 180
~ -[OTAParamRC hasRdc] : 24 -> 28
~ -[OTAParamRC agingCoeffForRdcs] : 16 -> 20
~ -[OTAParamRC agingCoeffForRdcAtIndex:] : 188 -> 180
~ -[OTAParamRC agingCoeffForRdcTemperatureCoeffs] : 16 -> 20
~ -[OTAParamRC agingCoeffForRdcTemperatureCoeffAtIndex:] : 188 -> 180
~ -[OTAParamRC qmaxs] : 16 -> 20
~ -[OTAParamRC qmaxAtIndex:] : 188 -> 180
~ -[OTAParamRC setMaxRdcR25Ratio:] : 36 -> 44
~ -[OTAParamRC setHasMaxRdcR25Ratio:] : 40 -> 44
~ -[OTAParamRC hasMaxRdcR25Ratio] : 20 -> 24
~ -[OTAParamRC description] : 176 -> 164
~ -[OTAParamRC dictionaryRepresentation] : 3136 -> 3024
~ _OTAParamRCReadFrom : 9472 -> 9388
~ -[OTAParamRC writeTo:] : 2720 -> 2944
~ -[OTAParamRC copyTo:] : 2816 -> 2952
~ -[OTAParamRC copyWithZone:] : 1496 -> 1708
~ -[OTAParamRC isEqual:] : 1684 -> 1900
~ -[OTAParamRC hash] : 2140 -> 2208
~ -[OTAParamRC mergeFrom:] : 2720 -> 2928
~ -[OTAParamRC r0] : 16 -> 20
~ -[OTAParamRC setR0:] : 80 -> 20
~ -[OTAParamRC r1] : 16 -> 20
~ -[OTAParamRC setR1:] : 80 -> 20
~ -[OTAParamRC baselineR1] : 16 -> 20
~ -[OTAParamRC setBaselineR1:] : 80 -> 20
~ -[OTAParamRC r2] : 16 -> 20
~ -[OTAParamRC setR2:] : 80 -> 20
~ -[OTAParamRC baselineR2] : 16 -> 20
~ -[OTAParamRC setBaselineR2:] : 80 -> 20
~ -[OTAParamRC rCFreq1] : 16 -> 20
~ -[OTAParamRC setRCFreq1:] : 80 -> 20
~ -[OTAParamRC rCFreq2] : 16 -> 20
~ -[OTAParamRC setRCFreq2:] : 80 -> 20
~ -[OTAParamRC rCFreq3] : 16 -> 20
~ -[OTAParamRC setRCFreq3:] : 80 -> 20
~ -[OTAParamRC baselineR0] : 16 -> 20
~ -[OTAParamRC setBaselineR0:] : 80 -> 20
~ -[OTAParamRC bmuResistance] : 16 -> 20
~ -[OTAParamRC setBmuResistance:] : 80 -> 20
~ -[OTAParamRC chemID] : 16 -> 20
~ -[OTAParamRC setChemID:] : 16 -> 20
~ -[OTAParamRC baselineR3] : 16 -> 20
~ -[OTAParamRC setBaselineR3:] : 80 -> 20
~ -[OTAParamRC maxRdcRatio] : 16 -> 20
~ -[OTAParamRC maxRdcRatioR2Extrap] : 16 -> 20
~ -[OTAParamRC baselineWRdc] : 16 -> 20
~ -[OTAParamRC r3] : 16 -> 20
~ -[OTAParamRC setR3:] : 80 -> 20
~ -[OTAParamRC rCFreq4] : 16 -> 20
~ -[OTAParamRC setRCFreq4:] : 80 -> 20
~ -[OTAParamRC baselineR4] : 16 -> 20
~ -[OTAParamRC setBaselineR4:] : 80 -> 20
~ -[OTAParamRC baselineRCFreq1] : 16 -> 20
~ -[OTAParamRC setBaselineRCFreq1:] : 80 -> 20
~ -[OTAParamRC baselineRCFreq2] : 16 -> 20
~ -[OTAParamRC setBaselineRCFreq2:] : 80 -> 20
~ -[OTAParamRC baselineRCFreq3] : 16 -> 20
~ -[OTAParamRC setBaselineRCFreq3:] : 80 -> 20
~ -[OTAParamRC baselineRCFreq4] : 16 -> 20
~ -[OTAParamRC setBaselineRCFreq4:] : 80 -> 20
~ -[OTAParamRC wRdcRatioThresh] : 16 -> 20
~ -[OTAParamRC rdc] : 16 -> 20
~ -[OTAParamRC setRdc:] : 80 -> 20
~ -[OTAParamRC maxRdcR25Ratio] : 16 -> 20
~ -[OTABMUResistance setTraceResistance25C:] : 36 -> 44
~ -[OTABMUResistance setHasTraceResistance25C:] : 40 -> 44
~ -[OTABMUResistance hasTraceResistance25C] : 20 -> 24
~ -[OTABMUResistance setTraceResistanceTemperatureCoeff:] : 36 -> 44
~ -[OTABMUResistance setHasTraceResistanceTemperatureCoeff:] : 40 -> 44
~ -[OTABMUResistance hasTraceResistanceTemperatureCoeff] : 20 -> 24
~ -[OTABMUResistance setSystemEquivalentResistance:] : 36 -> 44
~ -[OTABMUResistance setHasSystemEquivalentResistance:] : 40 -> 44
~ -[OTABMUResistance hasSystemEquivalentResistance] : 20 -> 24
~ -[OTABMUResistance setDownstreamCommonResistance:] : 36 -> 44
~ -[OTABMUResistance setHasDownstreamCommonResistance:] : 28 -> 32
~ -[OTABMUResistance hasDownstreamCommonResistance] : 20 -> 24
~ -[OTABMUResistance setDownstreamNorthResistance:] : 36 -> 44
~ -[OTABMUResistance setHasDownstreamNorthResistance:] : 40 -> 44
~ -[OTABMUResistance hasDownstreamNorthResistance] : 20 -> 24
~ -[OTABMUResistance setResistanceGGToVcut:] : 36 -> 44
~ -[OTABMUResistance setHasResistanceGGToVcut:] : 40 -> 44
~ -[OTABMUResistance hasResistanceGGToVcut] : 20 -> 24
~ -[OTABMUResistance setResistancePMUToVcut:] : 36 -> 44
~ -[OTABMUResistance setHasResistancePMUToVcut:] : 40 -> 44
~ -[OTABMUResistance hasResistancePMUToVcut] : 20 -> 24
~ -[OTABMUResistance setResistanceVcutToPmax:] : 36 -> 44
~ -[OTABMUResistance setHasResistanceVcutToPmax:] : 40 -> 44
~ -[OTABMUResistance hasResistanceVcutToPmax] : 20 -> 24
~ -[OTABMUResistance setResistanceCellTabToGG:] : 36 -> 44
~ -[OTABMUResistance setHasResistanceCellTabToGG:] : 40 -> 44
~ -[OTABMUResistance hasResistanceCellTabToGG] : 20 -> 24
~ -[OTABMUResistance description] : 176 -> 164
~ -[OTABMUResistance writeTo:] : 400 -> 440
~ -[OTABMUResistance copyTo:] : 440 -> 496
~ -[OTABMUResistance copyWithZone:] : 420 -> 496
~ -[OTABMUResistance isEqual:] : 476 -> 556
~ -[OTABMUResistance hash] : 1280 -> 1248
~ -[OTABMUResistance mergeFrom:] : 440 -> 496
~ -[OTABMUResistance traceResistance25C] : 16 -> 20
~ -[OTABMUResistance traceResistanceTemperatureCoeff] : 16 -> 20
~ -[OTABMUResistance systemEquivalentResistance] : 16 -> 20
~ -[OTABMUResistance downstreamCommonResistance] : 16 -> 20
~ -[OTABMUResistance downstreamNorthResistance] : 16 -> 20
~ -[OTABMUResistance resistanceGGToVcut] : 16 -> 20
~ -[OTABMUResistance resistancePMUToVcut] : 16 -> 20
~ -[OTABMUResistance resistanceVcutToPmax] : 16 -> 20
~ -[OTABMUResistance resistanceCellTabToGG] : 16 -> 20
CStrings:
- ".cxx_destruct"
- "@\"OTABMUResistance\""
- "@\"OTAResistanceData\""
- "@16@0:8"
- "@20@0:8i16"
- "@24@0:8^{_NSZone=}16"
- "B16@0:8"
- "B24@0:8@16"
- "I"
- "I16@0:8"
- "NSCopying"
- "OTABMUResistance"
- "OTAParamRC"
- "OTAResistanceData"
- "Q16@0:8"
- "StringAsMLBConfig:"
- "T@\"OTABMUResistance\",&,N,V_bmuResistance"
- "T@\"OTAResistanceData\",&,N,V_baselineR0"
- "T@\"OTAResistanceData\",&,N,V_baselineR1"
- "T@\"OTAResistanceData\",&,N,V_baselineR2"
- "T@\"OTAResistanceData\",&,N,V_baselineR3"
- "T@\"OTAResistanceData\",&,N,V_baselineR4"
- "T@\"OTAResistanceData\",&,N,V_baselineRCFreq1"
- "T@\"OTAResistanceData\",&,N,V_baselineRCFreq2"
- "T@\"OTAResistanceData\",&,N,V_baselineRCFreq3"
- "T@\"OTAResistanceData\",&,N,V_baselineRCFreq4"
- "T@\"OTAResistanceData\",&,N,V_r0"
- "T@\"OTAResistanceData\",&,N,V_r1"
- "T@\"OTAResistanceData\",&,N,V_r2"
- "T@\"OTAResistanceData\",&,N,V_r3"
- "T@\"OTAResistanceData\",&,N,V_rCFreq1"
- "T@\"OTAResistanceData\",&,N,V_rCFreq2"
- "T@\"OTAResistanceData\",&,N,V_rCFreq3"
- "T@\"OTAResistanceData\",&,N,V_rCFreq4"
- "T@\"OTAResistanceData\",&,N,V_rdc"
- "TB,N"
- "TB,R,N"
- "TI,N,V_chemID"
- "TQ,R,N"
- "T^f,R,N"
- "Tf,N,V_baselineWRdc"
- "Tf,N,V_downstreamCommonResistance"
- "Tf,N,V_downstreamNorthResistance"
- "Tf,N,V_maxRdcR25Ratio"
- "Tf,N,V_maxRdcRatio"
- "Tf,N,V_maxRdcRatioR2Extrap"
- "Tf,N,V_resistanceCellTabToGG"
- "Tf,N,V_resistanceGGToVcut"
- "Tf,N,V_resistancePMUToVcut"
- "Tf,N,V_resistanceVcutToPmax"
- "Tf,N,V_systemEquivalentResistance"
- "Tf,N,V_traceResistance25C"
- "Tf,N,V_traceResistanceTemperatureCoeff"
- "Tf,N,V_wRdcRatioThresh"
- "Ti,N,V_mLBConfig"
- "^f16@0:8"
- "_agingCoeffForR0TemperatureCoeffs"
- "_agingCoeffForR0s"
- "_agingCoeffForR1TemperatureCoeffs"
- "_agingCoeffForR1s"
- "_agingCoeffForR2TemperatureCoeffs"
- "_agingCoeffForR2s"
- "_agingCoeffForR3TemperatureCoeffs"
- "_agingCoeffForR3s"
- "_agingCoeffForRCFreq1TemperatureCoeffs"
- "_agingCoeffForRCFreq1s"
- "_agingCoeffForRCFreq2TemperatureCoeffs"
- "_agingCoeffForRCFreq2s"
- "_agingCoeffForRCFreq3TemperatureCoeffs"
- "_agingCoeffForRCFreq3s"
- "_agingCoeffForRCFreq4TemperatureCoeffs"
- "_agingCoeffForRCFreq4s"
- "_agingCoeffForRdcTemperatureCoeffs"
- "_agingCoeffForRdcs"
- "_baselineR0"
- "_baselineR1"
- "_baselineR2"
- "_baselineR3"
- "_baselineR4"
- "_baselineRCFreq1"
- "_baselineRCFreq2"
- "_baselineRCFreq3"
- "_baselineRCFreq4"
- "_baselineRdcs"
- "_baselineWRdc"
- "_bmuResistance"
- "_chemID"
- "_coeffSOCs"
- "_coeffVs"
- "_downstreamCommonResistance"
- "_downstreamNorthResistance"
- "_gridOCVs"
- "_gridWRdcRatios"
- "_has"
- "_mLBConfig"
- "_maxRdcR25Ratio"
- "_maxRdcRatio"
- "_maxRdcRatioR2Extrap"
- "_qmaxs"
- "_r0"
- "_r1"
- "_r2"
- "_r3"
- "_rCFreq1"
- "_rCFreq2"
- "_rCFreq3"
- "_rCFreq4"
- "_rdc"
- "_resistance25Cs"
- "_resistanceCellTabToGG"
- "_resistanceGGToVcut"
- "_resistancePMUToVcut"
- "_resistanceVcutToPmax"
- "_setError"
- "_slopeForR0Extraps"
- "_slopeForR1Extraps"
- "_slopeForR2Extraps"
- "_slopeForR3Extraps"
- "_systemEquivalentResistance"
- "_temperatureCoeffs"
- "_traceResistance25C"
- "_traceResistanceTemperatureCoeff"
- "_wRdcRatioThresh"
- "addAgingCoeffForR0:"
- "addAgingCoeffForR0TemperatureCoeff:"
- "addAgingCoeffForR1:"
- "addAgingCoeffForR1TemperatureCoeff:"
- "addAgingCoeffForR2:"
- "addAgingCoeffForR2TemperatureCoeff:"
- "addAgingCoeffForR3:"
- "addAgingCoeffForR3TemperatureCoeff:"
- "addAgingCoeffForRCFreq1:"
- "addAgingCoeffForRCFreq1TemperatureCoeff:"
- "addAgingCoeffForRCFreq2:"
- "addAgingCoeffForRCFreq2TemperatureCoeff:"
- "addAgingCoeffForRCFreq3:"
- "addAgingCoeffForRCFreq3TemperatureCoeff:"
- "addAgingCoeffForRCFreq4:"
- "addAgingCoeffForRCFreq4TemperatureCoeff:"
- "addAgingCoeffForRdc:"
- "addAgingCoeffForRdcTemperatureCoeff:"
- "addBaselineRdc:"
- "addCoeffSOC:"
- "addCoeffV:"
- "addGridOCV:"
- "addGridWRdcRatio:"
- "addQmax:"
- "addResistance25C:"
- "addSlopeForR0Extrap:"
- "addSlopeForR1Extrap:"
- "addSlopeForR2Extrap:"
- "addSlopeForR3Extrap:"
- "addTemperatureCoeff:"
- "agingCoeffForR0AtIndex:"
- "agingCoeffForR0TemperatureCoeffAtIndex:"
- "agingCoeffForR0TemperatureCoeffs"
- "agingCoeffForR0TemperatureCoeffsCount"
- "agingCoeffForR0s"
- "agingCoeffForR0sCount"
- "agingCoeffForR1AtIndex:"
- "agingCoeffForR1TemperatureCoeffAtIndex:"
- "agingCoeffForR1TemperatureCoeffs"
- "agingCoeffForR1TemperatureCoeffsCount"
- "agingCoeffForR1s"
- "agingCoeffForR1sCount"
- "agingCoeffForR2AtIndex:"
- "agingCoeffForR2TemperatureCoeffAtIndex:"
- "agingCoeffForR2TemperatureCoeffs"
- "agingCoeffForR2TemperatureCoeffsCount"
- "agingCoeffForR2s"
- "agingCoeffForR2sCount"
- "agingCoeffForR3AtIndex:"
- "agingCoeffForR3TemperatureCoeffAtIndex:"
- "agingCoeffForR3TemperatureCoeffs"
- "agingCoeffForR3TemperatureCoeffsCount"
- "agingCoeffForR3s"
- "agingCoeffForR3sCount"
- "agingCoeffForRCFreq1AtIndex:"
- "agingCoeffForRCFreq1TemperatureCoeffAtIndex:"
- "agingCoeffForRCFreq1TemperatureCoeffs"
- "agingCoeffForRCFreq1TemperatureCoeffsCount"
- "agingCoeffForRCFreq1s"
- "agingCoeffForRCFreq1sCount"
- "agingCoeffForRCFreq2AtIndex:"
- "agingCoeffForRCFreq2TemperatureCoeffAtIndex:"
- "agingCoeffForRCFreq2TemperatureCoeffs"
- "agingCoeffForRCFreq2TemperatureCoeffsCount"
- "agingCoeffForRCFreq2s"
- "agingCoeffForRCFreq2sCount"
- "agingCoeffForRCFreq3AtIndex:"
- "agingCoeffForRCFreq3TemperatureCoeffAtIndex:"
- "agingCoeffForRCFreq3TemperatureCoeffs"
- "agingCoeffForRCFreq3TemperatureCoeffsCount"
- "agingCoeffForRCFreq3s"
- "agingCoeffForRCFreq3sCount"
- "agingCoeffForRCFreq4AtIndex:"
- "agingCoeffForRCFreq4TemperatureCoeffAtIndex:"
- "agingCoeffForRCFreq4TemperatureCoeffs"
- "agingCoeffForRCFreq4TemperatureCoeffsCount"
- "agingCoeffForRCFreq4s"
- "agingCoeffForRCFreq4sCount"
- "agingCoeffForRdcAtIndex:"
- "agingCoeffForRdcTemperatureCoeffAtIndex:"
- "agingCoeffForRdcTemperatureCoeffs"
- "agingCoeffForRdcTemperatureCoeffsCount"
- "agingCoeffForRdcs"
- "agingCoeffForRdcsCount"
- "allocWithZone:"
- "baselineRdcAtIndex:"
- "baselineRdcs"
- "baselineRdcsCount"
- "clearAgingCoeffForR0TemperatureCoeffs"
- "clearAgingCoeffForR0s"
- "clearAgingCoeffForR1TemperatureCoeffs"
- "clearAgingCoeffForR1s"
- "clearAgingCoeffForR2TemperatureCoeffs"
- "clearAgingCoeffForR2s"
- "clearAgingCoeffForR3TemperatureCoeffs"
- "clearAgingCoeffForR3s"
- "clearAgingCoeffForRCFreq1TemperatureCoeffs"
- "clearAgingCoeffForRCFreq1s"
- "clearAgingCoeffForRCFreq2TemperatureCoeffs"
- "clearAgingCoeffForRCFreq2s"
- "clearAgingCoeffForRCFreq3TemperatureCoeffs"
- "clearAgingCoeffForRCFreq3s"
- "clearAgingCoeffForRCFreq4TemperatureCoeffs"
- "clearAgingCoeffForRCFreq4s"
- "clearAgingCoeffForRdcTemperatureCoeffs"
- "clearAgingCoeffForRdcs"
- "clearBaselineRdcs"
- "clearCoeffSOCs"
- "clearCoeffVs"
- "clearGridOCVs"
- "clearGridWRdcRatios"
- "clearQmaxs"
- "clearResistance25Cs"
- "clearSlopeForR0Extraps"
- "clearSlopeForR1Extraps"
- "clearSlopeForR2Extraps"
- "clearSlopeForR3Extraps"
- "clearTemperatureCoeffs"
- "coeffSOCAtIndex:"
- "coeffSOCs"
- "coeffSOCsCount"
- "coeffVAtIndex:"
- "coeffVs"
- "coeffVsCount"
- "copyTo:"
- "copyWithZone:"
- "data"
- "dealloc"
- "description"
- "dictionary"
- "dictionaryRepresentation"
- "exceptionWithName:reason:userInfo:"
- "f"
- "f16@0:8"
- "f24@0:8Q16"
- "getBytes:range:"
- "gridOCVAtIndex:"
- "gridOCVs"
- "gridOCVsCount"
- "gridWRdcRatioAtIndex:"
- "gridWRdcRatios"
- "gridWRdcRatiosCount"
- "hasBaselineR0"
- "hasBaselineR1"
- "hasBaselineR2"
- "hasBaselineR3"
- "hasBaselineR4"
- "hasBaselineRCFreq1"
- "hasBaselineRCFreq2"
- "hasBaselineRCFreq3"
- "hasBaselineRCFreq4"
- "hasBaselineWRdc"
- "hasBmuResistance"
- "hasDownstreamCommonResistance"
- "hasDownstreamNorthResistance"
- "hasError"
- "hasMLBConfig"
- "hasMaxRdcR25Ratio"
- "hasMaxRdcRatio"
- "hasMaxRdcRatioR2Extrap"
- "hasR0"
- "hasR1"
- "hasR2"
- "hasR3"
- "hasRCFreq1"
- "hasRCFreq2"
- "hasRCFreq3"
- "hasRCFreq4"
- "hasRdc"
- "hasResistanceCellTabToGG"
- "hasResistanceGGToVcut"
- "hasResistancePMUToVcut"
- "hasResistanceVcutToPmax"
- "hasSystemEquivalentResistance"
- "hasTraceResistance25C"
- "hasTraceResistanceTemperatureCoeff"
- "hasWRdcRatioThresh"
- "hash"
- "i"
- "i16@0:8"
- "i24@0:8@16"
- "init"
- "isEqual:"
- "isEqualToString:"
- "isMemberOfClass:"
- "length"
- "mLBConfig"
- "mLBConfigAsString:"
- "mergeFrom:"
- "numberWithFloat:"
- "numberWithUnsignedInt:"
- "position"
- "qmaxAtIndex:"
- "qmaxs"
- "qmaxsCount"
- "r0"
- "r1"
- "r2"
- "r3"
- "rCFreq1"
- "rCFreq2"
- "rCFreq3"
- "rCFreq4"
- "raise"
- "rdc"
- "readFrom:"
- "resistance25CAtIndex:"
- "resistance25Cs"
- "resistance25CsCount"
- "setAgingCoeffForR0TemperatureCoeffs:count:"
- "setAgingCoeffForR0s:count:"
- "setAgingCoeffForR1TemperatureCoeffs:count:"
- "setAgingCoeffForR1s:count:"
- "setAgingCoeffForR2TemperatureCoeffs:count:"
- "setAgingCoeffForR2s:count:"
- "setAgingCoeffForR3TemperatureCoeffs:count:"
- "setAgingCoeffForR3s:count:"
- "setAgingCoeffForRCFreq1TemperatureCoeffs:count:"
- "setAgingCoeffForRCFreq1s:count:"
- "setAgingCoeffForRCFreq2TemperatureCoeffs:count:"
- "setAgingCoeffForRCFreq2s:count:"
- "setAgingCoeffForRCFreq3TemperatureCoeffs:count:"
- "setAgingCoeffForRCFreq3s:count:"
- "setAgingCoeffForRCFreq4TemperatureCoeffs:count:"
- "setAgingCoeffForRCFreq4s:count:"
- "setAgingCoeffForRdcTemperatureCoeffs:count:"
- "setAgingCoeffForRdcs:count:"
- "setBaselineR0:"
- "setBaselineR1:"
- "setBaselineR2:"
- "setBaselineR3:"
- "setBaselineR4:"
- "setBaselineRCFreq1:"
- "setBaselineRCFreq2:"
- "setBaselineRCFreq3:"
- "setBaselineRCFreq4:"
- "setBaselineRdcs:count:"
- "setBaselineWRdc:"
- "setBmuResistance:"
- "setChemID:"
- "setCoeffSOCs:count:"
- "setCoeffVs:count:"
- "setDownstreamCommonResistance:"
- "setDownstreamNorthResistance:"
- "setGridOCVs:count:"
- "setGridWRdcRatios:count:"
- "setHasBaselineWRdc:"
- "setHasDownstreamCommonResistance:"
- "setHasDownstreamNorthResistance:"
- "setHasMLBConfig:"
- "setHasMaxRdcR25Ratio:"
- "setHasMaxRdcRatio:"
- "setHasMaxRdcRatioR2Extrap:"
- "setHasResistanceCellTabToGG:"
- "setHasResistanceGGToVcut:"
- "setHasResistancePMUToVcut:"
- "setHasResistanceVcutToPmax:"
- "setHasSystemEquivalentResistance:"
- "setHasTraceResistance25C:"
- "setHasTraceResistanceTemperatureCoeff:"
- "setHasWRdcRatioThresh:"
- "setMLBConfig:"
- "setMaxRdcR25Ratio:"
- "setMaxRdcRatio:"
- "setMaxRdcRatioR2Extrap:"
- "setObject:forKey:"
- "setPosition:"
- "setQmaxs:count:"
- "setR0:"
- "setR1:"
- "setR2:"
- "setR3:"
- "setRCFreq1:"
- "setRCFreq2:"
- "setRCFreq3:"
- "setRCFreq4:"
- "setRdc:"
- "setResistance25Cs:count:"
- "setResistanceCellTabToGG:"
- "setResistanceGGToVcut:"
- "setResistancePMUToVcut:"
- "setResistanceVcutToPmax:"
- "setSlopeForR0Extraps:count:"
- "setSlopeForR1Extraps:count:"
- "setSlopeForR2Extraps:count:"
- "setSlopeForR3Extraps:count:"
- "setSystemEquivalentResistance:"
- "setTemperatureCoeffs:count:"
- "setTraceResistance25C:"
- "setTraceResistanceTemperatureCoeff:"
- "setWRdcRatioThresh:"
- "slopeForR0ExtrapAtIndex:"
- "slopeForR0Extraps"
- "slopeForR0ExtrapsCount"
- "slopeForR1ExtrapAtIndex:"
- "slopeForR1Extraps"
- "slopeForR1ExtrapsCount"
- "slopeForR2ExtrapAtIndex:"
- "slopeForR2Extraps"
- "slopeForR2ExtrapsCount"
- "slopeForR3ExtrapAtIndex:"
- "slopeForR3Extraps"
- "slopeForR3ExtrapsCount"
- "stringWithFormat:"
- "temperatureCoeffAtIndex:"
- "temperatureCoeffs"
- "temperatureCoeffsCount"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8I16"
- "v20@0:8f16"
- "v20@0:8i16"
- "v24@0:8@16"
- "v32@0:8^f16Q24"
- "writeTo:"
- "{?=\"baselineWRdc\"b1\"mLBConfig\"b1\"maxRdcR25Ratio\"b1\"maxRdcRatio\"b1\"maxRdcRatioR2Extrap\"b1\"wRdcRatioThresh\"b1}"
- "{?=\"downstreamCommonResistance\"b1\"downstreamNorthResistance\"b1\"resistanceCellTabToGG\"b1\"resistanceGGToVcut\"b1\"resistancePMUToVcut\"b1\"resistanceVcutToPmax\"b1\"systemEquivalentResistance\"b1\"traceResistance25C\"b1\"traceResistanceTemperatureCoeff\"b1}"
- "{?=\"list\"^f\"count\"Q\"size\"Q}"

```
