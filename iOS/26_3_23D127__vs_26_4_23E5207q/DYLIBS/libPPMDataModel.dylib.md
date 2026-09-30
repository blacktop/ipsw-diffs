## libPPMDataModel.dylib

> `/usr/lib/libPPMDataModel.dylib`

```diff

-1035.80.9.0.0
-  __TEXT.__text: 0xb838
-  __TEXT.__auth_stubs: 0x1c0
+1035.100.46.0.0
+  __TEXT.__text: 0xbfc4
+  __TEXT.__auth_stubs: 0x1e0
   __TEXT.__objc_methlist: 0xfb4
   __TEXT.__cstring: 0x4b5
-  __TEXT.__unwind_info: 0x1e8
+  __TEXT.__unwind_info: 0x280
   __TEXT.__objc_classname: 0x41
   __TEXT.__objc_methname: 0x2606
   __TEXT.__objc_methtype: 0x275

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xa50
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0xe8
+  __AUTH_CONST.__auth_got: 0xf8
   __AUTH_CONST.__cfstring: 0x8c0
   __AUTH_CONST.__objc_const: 0x12f0
   __AUTH.__objc_data: 0xf0

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 75FD881C-5AEA-322C-B979-C9088F9D0EF6
+  UUID: 1E57E5FE-AFAC-37F9-BD58-6AA889146577
   Functions: 335
-  Symbols:   965
+  Symbols:   967
   CStrings:  606
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
+ _objc_retain_x21
- _objc_claimAutoreleasedReturnValue
Functions:
~ -[OTAResistanceData resistance25CAtIndex:] : 180 -> 188
~ -[OTAResistanceData temperatureCoeffAtIndex:] : 180 -> 188
~ -[OTAResistanceData description] : 164 -> 176
~ -[OTAResistanceData dictionaryRepresentation] : 176 -> 188
~ _OTAResistanceDataReadFrom : 1076 -> 1088
~ -[OTAResistanceData writeTo:] : 200 -> 196
~ -[OTAResistanceData mergeFrom:] : 176 -> 184
~ -[OTAParamRC agingCoeffForR0AtIndex:] : 180 -> 188
~ -[OTAParamRC agingCoeffForR0TemperatureCoeffAtIndex:] : 180 -> 188
~ -[OTAParamRC agingCoeffForR1AtIndex:] : 180 -> 188
~ -[OTAParamRC agingCoeffForR1TemperatureCoeffAtIndex:] : 180 -> 188
~ -[OTAParamRC agingCoeffForR2AtIndex:] : 180 -> 188
~ -[OTAParamRC agingCoeffForR2TemperatureCoeffAtIndex:] : 180 -> 188
~ -[OTAParamRC baselineRdcAtIndex:] : 180 -> 188
~ -[OTAParamRC gridOCVAtIndex:] : 180 -> 188
~ -[OTAParamRC slopeForR0ExtrapAtIndex:] : 180 -> 188
~ -[OTAParamRC slopeForR1ExtrapAtIndex:] : 180 -> 188
~ -[OTAParamRC slopeForR2ExtrapAtIndex:] : 180 -> 188
~ -[OTAParamRC slopeForR3ExtrapAtIndex:] : 180 -> 188
~ -[OTAParamRC agingCoeffForR3AtIndex:] : 180 -> 188
~ -[OTAParamRC agingCoeffForR3TemperatureCoeffAtIndex:] : 180 -> 188
~ -[OTAParamRC agingCoeffForRCFreq1AtIndex:] : 180 -> 188
~ -[OTAParamRC agingCoeffForRCFreq2AtIndex:] : 180 -> 188
~ -[OTAParamRC agingCoeffForRCFreq3AtIndex:] : 180 -> 188
~ -[OTAParamRC agingCoeffForRCFreq4AtIndex:] : 180 -> 188
~ -[OTAParamRC agingCoeffForRCFreq1TemperatureCoeffAtIndex:] : 180 -> 188
~ -[OTAParamRC agingCoeffForRCFreq2TemperatureCoeffAtIndex:] : 180 -> 188
~ -[OTAParamRC agingCoeffForRCFreq3TemperatureCoeffAtIndex:] : 180 -> 188
~ -[OTAParamRC agingCoeffForRCFreq4TemperatureCoeffAtIndex:] : 180 -> 188
~ -[OTAParamRC mLBConfigAsString:] : 132 -> 136
~ -[OTAParamRC StringAsMLBConfig:] : 88 -> 92
~ -[OTAParamRC gridWRdcRatioAtIndex:] : 180 -> 188
~ -[OTAParamRC coeffSOCAtIndex:] : 180 -> 188
~ -[OTAParamRC coeffVAtIndex:] : 180 -> 188
~ -[OTAParamRC agingCoeffForRdcAtIndex:] : 180 -> 188
~ -[OTAParamRC agingCoeffForRdcTemperatureCoeffAtIndex:] : 180 -> 188
~ -[OTAParamRC qmaxAtIndex:] : 180 -> 188
~ -[OTAParamRC description] : 164 -> 176
~ -[OTAParamRC dictionaryRepresentation] : 2916 -> 3136
~ _OTAParamRCReadFrom : 9328 -> 9472
~ -[OTAParamRC writeTo:] : 2724 -> 2720
~ -[OTAParamRC mergeFrom:] : 2716 -> 2720
~ -[OTAParamRC setR0:] : 20 -> 80
~ -[OTAParamRC setR1:] : 20 -> 80
~ -[OTAParamRC setBaselineR1:] : 20 -> 80
~ -[OTAParamRC setR2:] : 20 -> 80
~ -[OTAParamRC setBaselineR2:] : 20 -> 80
~ -[OTAParamRC setRCFreq1:] : 20 -> 80
~ -[OTAParamRC setRCFreq2:] : 20 -> 80
~ -[OTAParamRC setRCFreq3:] : 20 -> 80
~ -[OTAParamRC setBaselineR0:] : 20 -> 80
~ -[OTAParamRC setBmuResistance:] : 20 -> 80
~ -[OTAParamRC setBaselineR3:] : 20 -> 80
~ -[OTAParamRC setR3:] : 20 -> 80
~ -[OTAParamRC setRCFreq4:] : 20 -> 80
~ -[OTAParamRC setBaselineR4:] : 20 -> 80
~ -[OTAParamRC setBaselineRCFreq1:] : 20 -> 80
~ -[OTAParamRC setBaselineRCFreq2:] : 20 -> 80
~ -[OTAParamRC setBaselineRCFreq3:] : 20 -> 80
~ -[OTAParamRC setBaselineRCFreq4:] : 20 -> 80
~ -[OTAParamRC setRdc:] : 20 -> 80
~ -[OTABMUResistance description] : 164 -> 176
~ -[OTABMUResistance dictionaryRepresentation] : 676 -> 716
~ _OTABMUResistanceReadFrom : 2088 -> 2124
~ -[OTABMUResistance copyTo:] : 420 -> 440
~ -[OTABMUResistance mergeFrom:] : 420 -> 440

```
