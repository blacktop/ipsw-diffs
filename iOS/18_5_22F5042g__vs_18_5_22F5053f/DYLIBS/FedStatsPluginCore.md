## FedStatsPluginCore

> `/System/Library/PrivateFrameworks/FedStatsPluginCore.framework/FedStatsPluginCore`

```diff

-36.0.0.0.0
-  __TEXT.__text: 0x10154
+38.0.0.0.0
+  __TEXT.__text: 0x106b0
   __TEXT.__auth_stubs: 0x440
-  __TEXT.__objc_methlist: 0xbec
-  __TEXT.__const: 0xa8
-  __TEXT.__cstring: 0x1fe2
+  __TEXT.__objc_methlist: 0xc54
+  __TEXT.__const: 0xb0
+  __TEXT.__cstring: 0x2083
   __TEXT.__gcc_except_tab: 0x84
-  __TEXT.__oslogstring: 0x1242
-  __TEXT.__unwind_info: 0x320
-  __TEXT.__objc_classname: 0x3d3
-  __TEXT.__objc_methname: 0x25c1
-  __TEXT.__objc_methtype: 0x37e
-  __TEXT.__objc_stubs: 0x2100
-  __DATA_CONST.__got: 0x290
-  __DATA_CONST.__const: 0x158
-  __DATA_CONST.__objc_classlist: 0xf0
+  __TEXT.__oslogstring: 0x1277
+  __TEXT.__unwind_info: 0x330
+  __TEXT.__objc_classname: 0x3ef
+  __TEXT.__objc_methname: 0x2695
+  __TEXT.__objc_methtype: 0x385
+  __TEXT.__objc_stubs: 0x2200
+  __DATA_CONST.__got: 0x298
+  __DATA_CONST.__const: 0x168
+  __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9a0
-  __DATA_CONST.__objc_superrefs: 0x98
-  __DATA_CONST.__objc_arraydata: 0x108
+  __DATA_CONST.__objc_selrefs: 0x9e0
+  __DATA_CONST.__objc_superrefs: 0xa0
+  __DATA_CONST.__objc_arraydata: 0x118
   __AUTH_CONST.__auth_got: 0x230
-  __AUTH_CONST.__const: 0x1e0
-  __AUTH_CONST.__cfstring: 0x2600
-  __AUTH_CONST.__objc_const: 0x1e50
-  __AUTH_CONST.__objc_arrayobj: 0xd8
+  __AUTH_CONST.__const: 0x200
+  __AUTH_CONST.__cfstring: 0x26c0
+  __AUTH_CONST.__objc_const: 0x1f68
+  __AUTH_CONST.__objc_arrayobj: 0xc0
+  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0x960
-  __DATA.__objc_ivar: 0xc0
-  __DATA.__data: 0x148
+  __AUTH.__objc_data: 0x9b0
+  __DATA.__objc_ivar: 0xc8
+  __DATA.__data: 0x140
   __DATA.__bss: 0xb0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreLocation.framework/CoreLocation

   - /System/Library/PrivateFrameworks/Trial.framework/Trial
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 310
-  Symbols:   522
-  CStrings:  910
+  Functions: 319
+  Symbols:   537
+  CStrings:  930
 
Symbols:
+ _OBJC_CLASS_$_FedStatsCohortQueryLengthCappedField
+ _OBJC_CLASS_$_FedStatsPluginMaskingDataParameters
+ _OBJC_CLASS_$_NSConstantDictionary
+ _OBJC_METACLASS_$_FedStatsCohortQueryLengthCappedField
+ _OBJC_METACLASS_$_FedStatsPluginMaskingDataParameters
+ ___kCFBooleanFalse
+ _kFedStatsCohortQueryLengthCappedFieldPad
+ _kFedStatsDataCohortSafetyDataVersionCap
+ _kFedStatsPluginMaskingDataSignifierKey
- _OBJC_CLASS_$_FedStatsPluginDummyDataInjectionParameters
- _OBJC_CLASS_$_FedStatsUtilsUniformUnitIntervalDistribution
- _OBJC_METACLASS_$_FedStatsPluginDummyDataInjectionParameters
- _kFedStatsPluginDummyDataInjectionRateLowerBound
CStrings:
+ "%%FedStatsMaskingData%%"
+ "%@: cannot generate subsample decision"
+ "@\"FedStatsPluginMaskingDataParameters\""
+ "@32@0:8@16Q24"
+ "@32@0:8Q16@24"
+ "Adding masking results to actual query results."
+ "Cannot create masking data parameters from provided configuration"
+ "FedStatsCohortQueryLengthCappedField"
+ "FedStatsPluginMaskingDataParameters"
+ "Masking data = %@"
+ "Masking data parameters field names does not contain the data type '%@'"
+ "Masking data parameters required for this SQL query but not provided properly"
+ "No masking data parameters are available for this recipe."
+ "SQL query '%@' does not match any required pattern for masking data"
+ "SQL query '%@' matches the required pattern '%@' for masking data"
+ "T@\"FedStatsPluginMaskingDataParameters\",R,N,V_maskingDataParameters"
+ "T@\"NSString\",R,N,V_keyName"
+ "TQ,R,N,V_cap"
+ "TQ,R,N,V_resultCap"
+ "X"
+ "_cap"
+ "_keyName"
+ "_maskingDataParameters"
+ "_resultCap"
+ "`configuration['%@']` is not a non-negative number"
+ "addItems:"
+ "cap"
+ "cohortQueryFieldWithKey:cap:"
+ "com.apple.insights.other-analysis.analysisA"
+ "com.apple.insights.other-analysis.analysisB"
+ "fedstats:com.apple.insights.other-analysis.analysisA"
+ "fedstats:com.apple.insights.other-analysis.analysisB"
+ "initQueryFieldWithKey:cap:"
+ "initWithAssetProvider:recipeIdentifier:clientIdentifier:recordMetadata:dataTypeContent:sqlQuery:cohortNameList:defaultDonationParameters:maskingDataParameters:"
+ "initWithResultCap:fieldValueSets:"
+ "keyName"
+ "maskedResultsFrom:"
+ "maskingData"
+ "maskingDataParameters"
+ "padCohortValue:"
+ "resultCap"
+ "stringByPaddingToLength:withString:startingAtIndex:"
+ "subsample"
+ "subsampleBooleanValue:samplingRateTrue:samplingRateFalse:error:"
- "\x11"
- "@\"FedStatsPluginDummyDataInjectionParameters\""
- "@32@0:8d16@24"
- "Cannot create dummy data injection parameters from provided configuration"
- "Dummy data = %@"
- "Dummy data injection parameters field names does not contain the data type '%@'"
- "Dummy data injection parameters required for this SQL query but not provided properly"
- "FedStatsPluginDummyDataInjectionParameters"
- "Overriding injection rate %.2f to %.2f"
- "SQL query '%@' does not match any required pattern for dummy data injection"
- "SQL query '%@' matches the required pattern '%@' for dummy data injection"
- "T@\"FedStatsPluginDummyDataInjectionParameters\",R,N,V_dummyDataInjectionParameters"
- "Td,R,N,V_injectionRate"
- "^.*RegionalSafetyAnalysis\\.Disablement.*$"
- "^.*RegionalSafetyAnalysis\\.KeywordID.*$"
- "_dummyDataInjectionParameters"
- "_injectionRate"
- "`configuration['%@']` is not in [0.0,1.0]"
- "dummyData"
- "dummyDataInjectionParameters"
- "initWithAssetProvider:recipeIdentifier:clientIdentifier:recordMetadata:dataTypeContent:sqlQuery:cohortNameList:defaultDonationParameters:dummyDataInjectionParameters:"
- "initWithInjectionRate:fieldValueSets:"
- "injectionRate"
- "shouldInjectDummyData"

```
