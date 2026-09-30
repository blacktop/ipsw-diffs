## FedStats

> `/System/Library/PrivateFrameworks/FedStats.framework/FedStats`

```diff

-40.0.0.0.0
-  __TEXT.__text: 0x14240
-  __TEXT.__auth_stubs: 0x510
-  __TEXT.__objc_methlist: 0x153c
-  __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0x29fa
-  __TEXT.__oslogstring: 0x34b
+43.0.0.0.0
+  __TEXT.__text: 0x17cc8
+  __TEXT.__auth_stubs: 0x530
+  __TEXT.__objc_methlist: 0x178c
+  __TEXT.__const: 0xd8
+  __TEXT.__cstring: 0x3380
+  __TEXT.__oslogstring: 0x604
   __TEXT.__ustring: 0x1e
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__unwind_info: 0x3f0
-  __TEXT.__objc_classname: 0x5cb
-  __TEXT.__objc_methname: 0x2cfb
-  __TEXT.__objc_methtype: 0x735
-  __TEXT.__objc_stubs: 0x2620
-  __DATA_CONST.__got: 0x270
-  __DATA_CONST.__const: 0x308
-  __DATA_CONST.__objc_classlist: 0x130
-  __DATA_CONST.__objc_catlist: 0x10
+  __TEXT.__unwind_info: 0x450
+  __TEXT.__objc_classname: 0x62b
+  __TEXT.__objc_methname: 0x31c5
+  __TEXT.__objc_methtype: 0x796
+  __TEXT.__objc_stubs: 0x2940
+  __DATA_CONST.__got: 0x298
+  __DATA_CONST.__const: 0x2f8
+  __DATA_CONST.__objc_classlist: 0x138
+  __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xba8
+  __DATA_CONST.__objc_selrefs: 0xc90
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xd8
-  __DATA_CONST.__objc_arraydata: 0x660
-  __AUTH_CONST.__auth_got: 0x298
+  __DATA_CONST.__objc_superrefs: 0xe0
+  __DATA_CONST.__objc_arraydata: 0x690
+  __AUTH_CONST.__auth_got: 0x2a8
   __AUTH_CONST.__const: 0xa0
-  __AUTH_CONST.__cfstring: 0x2be0
-  __AUTH_CONST.__objc_const: 0x4568
-  __AUTH_CONST.__objc_intobj: 0x168
+  __AUTH_CONST.__cfstring: 0x3320
+  __AUTH_CONST.__objc_const: 0x4de0
+  __AUTH_CONST.__objc_intobj: 0x1b0
+  __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH.__objc_data: 0xbe0
-  __DATA.__objc_ivar: 0x128
-  __DATA.__data: 0x318
+  __AUTH.__objc_data: 0xc30
+  __DATA.__objc_ivar: 0x14c
+  __DATA.__data: 0x370
   __DATA.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 1A5AE6B0-69A1-3347-AC70-4322A9F845AD
-  Functions: 383
-  Symbols:   1758
-  CStrings:  1381
+  UUID: DB6A4CCC-23A7-3718-AA78-6FC545EC4865
+  Functions: 435
+  Symbols:   1938
+  CStrings:  1564
 
Symbols:
+ +[FedStatsCategoricalType kOutOfCategories]
+ +[FedStatsDataEncoder encodeDataArrayAndRecord:dataTypeContent:metadata:baseKey:errorOut:].cold.10
+ +[FedStatsDataEncoder encodeDataArrayAndRecord:dataTypeContent:metadata:baseKey:errorOut:].cold.11
+ +[FedStatsDataEncoder encodeDataArrayAndRecord:dataTypeContent:metadata:baseKey:errorOut:].cold.12
+ +[FedStatsDataEncoder encodeDataArrayAndRecord:dataTypeContent:metadata:baseKey:errorOut:].cold.13
+ +[FedStatsDataEncoder encodeDataArrayAndRecord:dataTypeContent:metadata:baseKey:errorOut:].cold.14
+ +[FedStatsDataEncoder encodeDataArrayAndRecord:dataTypeContent:metadata:baseKey:errorOut:].cold.15
+ +[FedStatsDataEncoder encodeDataArrayAndRecord:dataTypeContent:metadata:baseKey:errorOut:].cold.6
+ +[FedStatsDataEncoder encodeDataArrayAndRecord:dataTypeContent:metadata:baseKey:errorOut:].cold.7
+ +[FedStatsDataEncoder encodeDataArrayAndRecord:dataTypeContent:metadata:baseKey:errorOut:].cold.8
+ +[FedStatsDataEncoder encodeDataArrayAndRecord:dataTypeContent:metadata:baseKey:errorOut:].cold.9
+ +[FedStatsDataEncoder mutateCollectionKeyForHistogramType:]
+ +[FedStatsHistogramType createFromDict:possibleError:]
+ +[FedStatsUtils normL2:]
+ +[NSArray(FloatArithmetic) arrayWithData:]
+ +[NSArray(RepeatedInitializer) arrayWithObject:repeated:]
+ +[NSData(FloatArrayInitializer) dataWithArray:]
+ -[FedStatsBooleanType decodeFromHistogramVector:possibleError:]
+ -[FedStatsBooleanType encodeToHistogramVector:possibleError:]
+ -[FedStatsBoundedULongType decodeFromHistogramVector:possibleError:]
+ -[FedStatsBoundedULongType encodeToHistogramVector:possibleError:]
+ -[FedStatsDataEncoder encodeDataArray:error:]
+ -[FedStatsDataEncoder encodeDataArray:error:].cold.1
+ -[FedStatsDataEncoder encodeDataArray:error:].cold.2
+ -[FedStatsDataEncoder encodeDataArray:error:].cold.3
+ -[FedStatsDataEncoder encodeDataArray:error:].cold.4
+ -[FedStatsDataEncoder encodeToHistogramVector:error:]
+ -[FedStatsDataEncoder initWithHistogramType:typeName:]
+ -[FedStatsDataEncoder isVectorDimensionAllowed]
+ -[FedStatsDataEncoder resultType]
+ -[FedStatsHistogramType .cxx_destruct]
+ -[FedStatsHistogramType classCount]
+ -[FedStatsHistogramType clippingBound]
+ -[FedStatsHistogramType dataType]
+ -[FedStatsHistogramType decodeFromHistogramVector:possibleError:]
+ -[FedStatsHistogramType decodeFromIndex:possibleError:]
+ -[FedStatsHistogramType decodeFromOneHotVector:possibleError:]
+ -[FedStatsHistogramType defaultFeatureFactor]
+ -[FedStatsHistogramType encodeToHistogramVector:possibleError:]
+ -[FedStatsHistogramType encodeToIndex:possibleError:]
+ -[FedStatsHistogramType encodeToOneHotVector:possibleError:]
+ -[FedStatsHistogramType featureFactors]
+ -[FedStatsHistogramType featureField]
+ -[FedStatsHistogramType featureType]
+ -[FedStatsHistogramType initWithFeatureType:metricField:clippingBound:featureFactors:defaultFeatureFactor:featureField:normType:normDediscoTaskConfig:]
+ -[FedStatsHistogramType invertScaleAndShift:]
+ -[FedStatsHistogramType metricField]
+ -[FedStatsHistogramType normDediscoTypeConfig]
+ -[FedStatsHistogramType normType]
+ -[FedStatsHistogramType sampleForIndex:]
+ -[FedStatsHistogramType scaleAndShift:]
+ -[FedStatsInvalidDataType decodeFromHistogramVector:possibleError:]
+ -[FedStatsInvalidDataType encodeToHistogramVector:possibleError:]
+ -[NSArray(FlatDescription) flatDescription]
+ -[NSArray(FloatArithmetic) arrayByElementwiseAdd:]
+ -[NSArray(FloatArithmetic) arrayByScalingWith:]
+ -[NSDictionary(FlatDescription) flatDescription]
+ _OBJC_CLASS_$_FedStatsHistogramType
+ _OBJC_CLASS_$_NSConstantDoubleNumber
+ _OBJC_CLASS_$_NSException
+ _OBJC_CLASS_$__DPFloatValueRecorder
+ _OBJC_IVAR_$_FedStatsDataEncoder._resultType
+ _OBJC_IVAR_$_FedStatsHistogramType._clippingBound
+ _OBJC_IVAR_$_FedStatsHistogramType._defaultFeatureFactor
+ _OBJC_IVAR_$_FedStatsHistogramType._featureFactors
+ _OBJC_IVAR_$_FedStatsHistogramType._featureField
+ _OBJC_IVAR_$_FedStatsHistogramType._featureType
+ _OBJC_IVAR_$_FedStatsHistogramType._metricField
+ _OBJC_IVAR_$_FedStatsHistogramType._normDediscoTypeConfig
+ _OBJC_IVAR_$_FedStatsHistogramType._normType
+ _OBJC_METACLASS_$_FedStatsHistogramType
+ _OUTLINED_FUNCTION_4
+ __OBJC_$_CATEGORY_CLASS_METHODS_NSData_$_FloatArrayInitializer
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_NSDictionary_$_FlatDescription
+ __OBJC_$_CATEGORY_NSArray_$_RepeatedInitializer
+ __OBJC_$_CATEGORY_NSData_$_FloatArrayInitializer
+ __OBJC_$_CATEGORY_NSDictionary_$_FlatDescription
+ __OBJC_$_CLASS_METHODS_FedStatsHistogramType
+ __OBJC_$_CLASS_METHODS_NSArray(RepeatedInitializer|FlatDescription|FloatArithmetic)
+ __OBJC_$_INSTANCE_METHODS_FedStatsHistogramType
+ __OBJC_$_INSTANCE_METHODS_NSArray(RepeatedInitializer|FlatDescription|FloatArithmetic)
+ __OBJC_$_INSTANCE_VARIABLES_FedStatsHistogramType
+ __OBJC_$_PROP_LIST_FedStatsHistogramType
+ __OBJC_CLASS_PROTOCOLS_$_FedStatsHistogramType
+ __OBJC_CLASS_RO_$_FedStatsHistogramType
+ __OBJC_METACLASS_RO_$_FedStatsHistogramType
+ _kDPMetadataDediscoTaskConfig
+ _kDPMetadataSchemaVersion
+ _kFedStatsHistogramTypeClippingBoundKey
+ _kFedStatsHistogramTypeDefaultFeatureFactorKey
+ _kFedStatsHistogramTypeFeatureFactorScaleKey
+ _kFedStatsHistogramTypeFeatureFactorShiftKey
+ _kFedStatsHistogramTypeFeatureFactorsKey
+ _kFedStatsHistogramTypeFeatureTypesKey
+ _kFedStatsHistogramTypeMetricFieldKey
+ _kFedStatsHistogramTypeNormTypeKey
+ _kFedStatsHistogramTypeShiftFactorKey
+ _ldiv
+ _objc_exception_throw
+ _objc_msgSend$arrayByElementwiseAdd:
+ _objc_msgSend$arrayByScalingWith:
+ _objc_msgSend$arrayWithData:
+ _objc_msgSend$arrayWithObject:repeated:
+ _objc_msgSend$clippingBound
+ _objc_msgSend$dataWithArray:
+ _objc_msgSend$defaultFeatureFactor
+ _objc_msgSend$encodeDataArray:error:
+ _objc_msgSend$encodeToHistogramVector:error:
+ _objc_msgSend$encodeToHistogramVector:possibleError:
+ _objc_msgSend$exceptionWithName:reason:userInfo:
+ _objc_msgSend$featureFactors
+ _objc_msgSend$featureField
+ _objc_msgSend$featureType
+ _objc_msgSend$initWithFeatureType:metricField:clippingBound:featureFactors:defaultFeatureFactor:featureField:normType:normDediscoTaskConfig:
+ _objc_msgSend$initWithHistogramType:typeName:
+ _objc_msgSend$isEqualToNumber:
+ _objc_msgSend$isVectorDimensionAllowed
+ _objc_msgSend$metricField
+ _objc_msgSend$mutateCollectionKeyForHistogramType:
+ _objc_msgSend$normDediscoTypeConfig
+ _objc_msgSend$normL2:
+ _objc_msgSend$normType
+ _objc_msgSend$recordFloatVectors:metadata:
+ _objc_msgSend$removeObjectForKey:
+ _objc_msgSend$resultType
+ _objc_msgSend$scaleAndShift:
+ _objc_msgSend$stringByReplacingOccurrencesOfString:withString:
- +[FedStatsCombinationType kAvailableTypes]
- +[FedStatsDataEncoder encodeDataArray:dataTypeContent:resultType:errorOut:].cold.1
- +[FedStatsDataEncoder encodeDataArray:dataTypeContent:resultType:errorOut:].cold.2
- +[FedStatsDataEncoder encodeDataArray:dataTypeContent:resultType:errorOut:].cold.3
- -[FedStatsCategoricalType kOutOfCategories]
- _objc_msgSend$encodeDataArray:dataTypeContent:resultType:errorOut:
- _objc_msgSend$kAvailableTypes
- _objc_msgSend$localizedDescription
CStrings:
+ "%@: %@"
+ "2.0"
+ "@\"<FedStatsDataTypeProtocol>\""
+ "@\"FedStatsBucketedType\""
+ "@20@0:8f16"
+ "@80@0:8@16@24@32@40@48@56@64@72"
+ "Cannot create histogram type \"%@\""
+ "Cannot decode feature value for histogram"
+ "Cannot encode data to histogram"
+ "Could not decode \"%@\" value in the combination"
+ "DimensionMismatch"
+ "Error encoding \"%@\" type"
+ "Every entry in the value of the key \"%@\"must be a string"
+ "Every value in the \"%@\" dictionary must be a class conforming to FedStatsDataTypeProtocol"
+ "FedStatsHistogramType"
+ "FlatDescription"
+ "FloatArithmetic"
+ "FloatArrayInitializer"
+ "FloatDataSizeNotDivisibleBy4"
+ "Histogram type encoder input data cannot be encoded to an index"
+ "Histogram type encoder input data is missing value for the field \"%@\""
+ "Histogram type encoder input is missing the key '%@'"
+ "Histogram type encoder input's value for '%@' is not a number"
+ "Histogram vector cannot have multiple indices with non-zero value"
+ "Histogram vector is not implemented for this type."
+ "HistogramType"
+ "HistogramType `dataTypeParams[\"%@\"][\"%@\"]` does not conform to FedStatsDataTypeProtocol"
+ "HistogramType `dataTypeParams[\"%@\"][\"%@\"]` is missing"
+ "HistogramType `dataTypeParams[\"%@\"][\"%@\"]` is not a bucketed type"
+ "HistogramType `dataTypeParams[\"%@\"][\"%@\"]` is not a number"
+ "HistogramType `dataTypeParams[\"%@\"][\"%@\"]` is not a positive number"
+ "HistogramType `dataTypeParams[\"%@\"][%lu][\"%@\"]` missing"
+ "HistogramType `dataTypeParams[\"%@\"][%lu][\"%@\"]` not a number"
+ "HistogramType `dataTypeParams[\"%@\"][%lu][\"%@\"]` not a positive number"
+ "HistogramType `dataTypeParams[\"%@\"][%lu]` cannot be encoded as a feature"
+ "HistogramType `dataTypeParams[\"%@\"]` contains a non-dictionary typed element"
+ "HistogramType `dataTypeParams[\"%@\"]` contains a non-string typed element"
+ "HistogramType `dataTypeParams[\"%@\"]` is missing"
+ "HistogramType `dataTypeParams[\"%@\"]` is not a dictionary"
+ "HistogramType `dataTypeParams[\"%@\"]` is not an array of dictionaries"
+ "HistogramType `dataTypeParams[\"%@\"]` not a non-empty array"
+ "HistogramType `dataTypeParams[\"%@\"]` not a positive number"
+ "HistogramType `dataTypeParams[\"%@\"]` not a string"
+ "HistogramType cannot create feature type"
+ "HistogramType cannot find feature value"
+ "InputDataTooLong"
+ "ItemNotNSNumber"
+ "NSArrayConstructorWithData"
+ "NSArrayElementwiseAdd"
+ "NSDataConstructorWithArray"
+ "RepeatedInitializer"
+ "Result type not supported"
+ "Resulting vector dimension is larger than max dimension %lu"
+ "T@\"<FedStatsDataTypeProtocol>\",R,N,V_featureType"
+ "T@\"FedStatsBucketedType\",R,N,V_normType"
+ "T@\"NSDictionary\",R,N,V_defaultFeatureFactor"
+ "T@\"NSDictionary\",R,N,V_featureFactors"
+ "T@\"NSDictionary\",R,N,V_normDediscoTypeConfig"
+ "T@\"NSNumber\",R,N,V_clippingBound"
+ "T@\"NSString\",R,N,V_featureField"
+ "T@\"NSString\",R,N,V_metricField"
+ "TQ,R,N,V_resultType"
+ "The data type content can have at most one histogram type"
+ "The data type content cannot have one histogram type and combination types"
+ "This API is only available for single histogram type in encoding schema"
+ "[%@]"
+ "_clippingBound"
+ "_defaultFeatureFactor"
+ "_featureFactors"
+ "_featureField"
+ "_featureType"
+ "_metricField"
+ "_normDediscoTypeConfig"
+ "_normType"
+ "_resultType"
+ "aggregated."
+ "arrayByElementwiseAdd:"
+ "arrayByScalingWith:"
+ "arrayWithData:"
+ "arrayWithObject:repeated:"
+ "clippingBound"
+ "dataWithArray:"
+ "decodeFromHistogramVector:possibleError:"
+ "decoding from index not implemented for histogram type"
+ "decoding from vector not implemented for histogram type"
+ "defaultFeatureFactor"
+ "encodeDataArray:error:"
+ "encodeDataArrayAndRecord cannot create norm recorder for key '%@'"
+ "encodeDataArrayAndRecord cannot record histogram norm for key '%@'. Error: %@"
+ "encodeDataArrayAndRecord fail to record histogram norm for key '%@'"
+ "encodeDataArrayAndRecord failed at constructor"
+ "encodeDataArrayAndRecord failed to record vector for key '%@'"
+ "encodeDataArrayAndRecord float recorder metadata = %@"
+ "encodeDataArrayAndRecord histogram vector recorded successfully."
+ "encodeDataArrayAndRecord multi-hot recorder metadata = %@"
+ "encodeDataArrayAndRecord norm recorded successfully for key '%@'"
+ "encodeDataArrayAndRecord norm recorder metadata = %@"
+ "encodeDataArrayAndRecord one-hot recorder metadata = %@"
+ "encodeDataArrayAndRecord skipping to record histogram norm for key '%@'"
+ "encodeToHistogramVector:error:"
+ "encodeToHistogramVector:possibleError:"
+ "encoding to index not implemented for histogram type"
+ "encoding to one-hot vector not implemented for histogram type"
+ "exceptionWithName:reason:userInfo:"
+ "featureFactors"
+ "featureField"
+ "featureType"
+ "featureTypes"
+ "flatDescription"
+ "initWithFeatureType:metricField:clippingBound:featureFactors:defaultFeatureFactor:featureField:normType:normDediscoTaskConfig:"
+ "initWithHistogramType:typeName:"
+ "invertScaleAndShift:"
+ "isEqualToNumber:"
+ "isVectorDimensionAllowed"
+ "metricField"
+ "mutateCollectionKeyForHistogramType:"
+ "normDediscoTypeConfig"
+ "normL2:"
+ "normType"
+ "recordFloatVectors:metadata:"
+ "removeObjectForKey:"
+ "resultType"
+ "scaleAndShift:"
+ "shift"
+ "shiftFactor"
+ "stringByReplacingOccurrencesOfString:withString:"
+ "{%@}"
- "Could not decode \"%@\" value in the combination: %@"
- "Error encoding \"%@\" type: %@"
- "Every entry in the value of the key \"%@\" must be a string"
- "Every value in the \"%@\" dictionary must be a class conforming to %@"
- "Resulting dimensionality %lu is larger than max dimensionality %lu"
- "kAvailableTypes"
- "localizedDescription"

```
