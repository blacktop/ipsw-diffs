## SignpostSupport

> `/System/Library/PrivateFrameworks/SignpostSupport.framework/SignpostSupport`

```diff

-121.0.0.0.0
-  __TEXT.__text: 0x31ae0
+125.0.0.0.0
+  __TEXT.__text: 0x33d40
   __TEXT.__auth_stubs: 0x520
-  __TEXT.__objc_methlist: 0x3d24
+  __TEXT.__objc_methlist: 0x3fac
   __TEXT.__const: 0x114
-  __TEXT.__cstring: 0x15244
+  __TEXT.__cstring: 0x1556f
   __TEXT.__oslogstring: 0xd2e
   __TEXT.__gcc_except_tab: 0x148
   __TEXT.__ustring: 0x3e
-  __TEXT.__unwind_info: 0xca0
-  __TEXT.__objc_classname: 0x9be
-  __TEXT.__objc_methname: 0xa965
-  __TEXT.__objc_methtype: 0xc2b
-  __TEXT.__objc_stubs: 0x6440
+  __TEXT.__unwind_info: 0xcf4
+  __TEXT.__objc_classname: 0xa67
+  __TEXT.__objc_methname: 0xa99d
+  __TEXT.__objc_methtype: 0xc73
+  __TEXT.__objc_stubs: 0x65c0
   __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0x728
-  __DATA_CONST.__objc_classlist: 0x230
+  __DATA_CONST.__const: 0x750
+  __DATA_CONST.__objc_classlist: 0x248
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x6f90
-  __DATA_CONST.__objc_selrefs: 0x1e10
+  __DATA_CONST.__objc_const: 0x7968
+  __DATA_CONST.__objc_selrefs: 0x1e80
+  __DATA_CONST.__objc_classrefs: 0x230
+  __DATA_CONST.__objc_superrefs: 0x1e0
   __DATA_CONST.__objc_arraydata: 0x4e58
-  __AUTH_CONST.__cfstring: 0x15d40
+  __AUTH_CONST.__cfstring: 0x161c0
   __AUTH_CONST.__objc_arrayobj: 0x2e8
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__objc_intobj: 0xa8
+  __AUTH_CONST.__const: 0xe0
+  __AUTH_CONST.__objc_const: 0x168
+  __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__auth_got: 0x2a0
-  __DATA.__objc_classrefs: 0x218
-  __DATA.__objc_superrefs: 0x1d8
-  __DATA.__objc_ivar: 0x5e0
-  __DATA.__data: 0x2c8
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x614
+  __DATA.__data: 0x470
   __DATA.__bss: 0x308
-  __DATA_DIRTY.__const: 0x720
+  __DATA_DIRTY.__const: 0x6a0
   __DATA_DIRTY.__objc_const: 0x19d8
   __DATA_DIRTY.__objc_data: 0x15e0
   __DATA_DIRTY.__bss: 0x20

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1519
-  Symbols:   5068
-  CStrings:  4852
+  Functions: 1571
+  Symbols:   5265
+  CStrings:  4923
 
Symbols:
+ +[SignpostAggregation sumOfAggregation0:aggregation1:errorOut:]
+ +[SignpostAggregationGroup _sumOfGroup0:group1:errorOut:]
+ +[SignpostAggregationGroupDuration _sumOfDuration0:duration1:errorOut:]
+ +[SignpostAggregationGroupMeasuredValue _sumOfValue0:value1:errorOut:]
+ +[SignpostAggregationValueStats sumOfStats0:stats1:errorOut:]
+ -[SignpostAggregation _groupToTypeToMeasuredValue]
+ -[SignpostAggregation _handleValueSegment:placeholderType:parser:]
+ -[SignpostAggregation _processMetadataSegment:parser:]
+ -[SignpostAggregation _updateValueDict:withParser:placeholderType:class:]
+ -[SignpostAggregation set_groupToTypeToMeasuredValue:]
+ -[SignpostAggregationGroup measuredValueTypeToMeasuredValueDict]
+ -[SignpostAggregationGroup setMeasuredValueTypeToMeasuredValueDict:]
+ -[SignpostAggregationGroupDuration _coreAnalyticsMaxFieldName]
+ -[SignpostAggregationGroupDuration _coreAnalyticsMinFieldName]
+ -[SignpostAggregationGroupDuration _coreAnalyticsStdDevFieldName]
+ -[SignpostAggregationGroupDuration _coreAnalyticsTotalFieldName]
+ -[SignpostAggregationGroupDuration _durationValue]
+ -[SignpostAggregationGroupDuration _initWithGroup:type:]
+ -[SignpostAggregationGroupDuration _initWithParser:]
+ -[SignpostAggregationGroupDuration _isTotalDuration]
+ -[SignpostAggregationGroupDuration max]
+ -[SignpostAggregationGroupDuration min]
+ -[SignpostAggregationGroupDuration setTelemetryEnabled:]
+ -[SignpostAggregationGroupDuration shouldAdd]
+ -[SignpostAggregationGroupDuration stats]
+ -[SignpostAggregationGroupDuration stddev]
+ -[SignpostAggregationGroupDuration total]
+ -[SignpostAggregationGroupDuration unit]
+ -[SignpostAggregationGroupMeasuredValue .cxx_destruct]
+ -[SignpostAggregationGroupMeasuredValue _coreAnalyticsMaxFieldName]
+ -[SignpostAggregationGroupMeasuredValue _coreAnalyticsMinFieldName]
+ -[SignpostAggregationGroupMeasuredValue _coreAnalyticsStdDevFieldName]
+ -[SignpostAggregationGroupMeasuredValue _coreAnalyticsTotalFieldName]
+ -[SignpostAggregationGroupMeasuredValue _dictionaryRepresentation]
+ -[SignpostAggregationGroupMeasuredValue _initWithParser:]
+ -[SignpostAggregationGroupMeasuredValue average]
+ -[SignpostAggregationGroupMeasuredValue copyWithZone:]
+ -[SignpostAggregationGroupMeasuredValue count]
+ -[SignpostAggregationGroupMeasuredValue groupName]
+ -[SignpostAggregationGroupMeasuredValue initWithGroupName:type:unit:]
+ -[SignpostAggregationGroupMeasuredValue isEqual:]
+ -[SignpostAggregationGroupMeasuredValue max]
+ -[SignpostAggregationGroupMeasuredValue min]
+ -[SignpostAggregationGroupMeasuredValue setTelemetryEnabled:]
+ -[SignpostAggregationGroupMeasuredValue shouldAdd]
+ -[SignpostAggregationGroupMeasuredValue stats]
+ -[SignpostAggregationGroupMeasuredValue stddev]
+ -[SignpostAggregationGroupMeasuredValue telemetryEnabled]
+ -[SignpostAggregationGroupMeasuredValue total]
+ -[SignpostAggregationGroupMeasuredValue type]
+ -[SignpostAggregationGroupMeasuredValue unit]
+ -[SignpostAggregationValueStats .cxx_destruct]
+ -[SignpostAggregationValueStats _finalizeState]
+ -[SignpostAggregationValueStats _rawAverage]
+ -[SignpostAggregationValueStats _rawTotal]
+ -[SignpostAggregationValueStats average]
+ -[SignpostAggregationValueStats copyWithZone:]
+ -[SignpostAggregationValueStats count]
+ -[SignpostAggregationValueStats isEqual:]
+ -[SignpostAggregationValueStats max]
+ -[SignpostAggregationValueStats min]
+ -[SignpostAggregationValueStats setCount:]
+ -[SignpostAggregationValueStats setMax:]
+ -[SignpostAggregationValueStats setMin:]
+ -[SignpostAggregationValueStats setStddev:]
+ -[SignpostAggregationValueStats set_rawAverage:]
+ -[SignpostAggregationValueStats set_rawTotal:]
+ -[SignpostAggregationValueStats stddev]
+ -[SignpostAggregationValueStats total]
+ -[_SignpostAggregationValueSegmentParser .cxx_destruct]
+ -[_SignpostAggregationValueSegmentParser _clearFields]
+ -[_SignpostAggregationValueSegmentParser group]
+ -[_SignpostAggregationValueSegmentParser processSegment:placeholderType:]
+ -[_SignpostAggregationValueSegmentParser setGroup:]
+ -[_SignpostAggregationValueSegmentParser setTelemetryEnabled:]
+ -[_SignpostAggregationValueSegmentParser setType:]
+ -[_SignpostAggregationValueSegmentParser setUnit:]
+ -[_SignpostAggregationValueSegmentParser setValue:]
+ -[_SignpostAggregationValueSegmentParser telemetryEnabled]
+ -[_SignpostAggregationValueSegmentParser type]
+ -[_SignpostAggregationValueSegmentParser unit]
+ -[_SignpostAggregationValueSegmentParser value]
+ _OBJC_CLASS_$_SignpostAggregationGroupMeasuredValue
+ _OBJC_CLASS_$_SignpostAggregationValueStats
+ _OBJC_CLASS_$__SignpostAggregationValueSegmentParser
+ _OBJC_IVAR_$_SignpostAggregation.__groupToTypeToMeasuredValue
+ _OBJC_IVAR_$_SignpostAggregationGroup._measuredValueTypeToMeasuredValueDict
+ _OBJC_IVAR_$_SignpostAggregationGroupDuration.__durationValue
+ _OBJC_IVAR_$_SignpostAggregationGroupDuration.__isTotalDuration
+ _OBJC_IVAR_$_SignpostAggregationGroupDuration._stats
+ _OBJC_IVAR_$_SignpostAggregationGroupMeasuredValue._groupName
+ _OBJC_IVAR_$_SignpostAggregationGroupMeasuredValue._stats
+ _OBJC_IVAR_$_SignpostAggregationGroupMeasuredValue._telemetryEnabled
+ _OBJC_IVAR_$_SignpostAggregationGroupMeasuredValue._type
+ _OBJC_IVAR_$_SignpostAggregationGroupMeasuredValue._unit
+ _OBJC_IVAR_$_SignpostAggregationValueStats.__rawAverage
+ _OBJC_IVAR_$_SignpostAggregationValueStats.__rawTotal
+ _OBJC_IVAR_$_SignpostAggregationValueStats._count
+ _OBJC_IVAR_$_SignpostAggregationValueStats._max
+ _OBJC_IVAR_$_SignpostAggregationValueStats._min
+ _OBJC_IVAR_$_SignpostAggregationValueStats._stddev
+ _OBJC_IVAR_$__SignpostAggregationValueSegmentParser._group
+ _OBJC_IVAR_$__SignpostAggregationValueSegmentParser._telemetryEnabled
+ _OBJC_IVAR_$__SignpostAggregationValueSegmentParser._type
+ _OBJC_IVAR_$__SignpostAggregationValueSegmentParser._unit
+ _OBJC_IVAR_$__SignpostAggregationValueSegmentParser._value
+ _OBJC_METACLASS_$_SignpostAggregationGroupMeasuredValue
+ _OBJC_METACLASS_$_SignpostAggregationValueStats
+ _OBJC_METACLASS_$__SignpostAggregationValueSegmentParser
+ __OBJC_$_CLASS_METHODS_SignpostAggregationGroupMeasuredValue
+ __OBJC_$_CLASS_METHODS_SignpostAggregationValueStats
+ __OBJC_$_INSTANCE_METHODS_SignpostAggregationGroupMeasuredValue
+ __OBJC_$_INSTANCE_METHODS_SignpostAggregationValueStats
+ __OBJC_$_INSTANCE_METHODS__SignpostAggregationValueSegmentParser
+ __OBJC_$_INSTANCE_VARIABLES_SignpostAggregationGroupMeasuredValue
+ __OBJC_$_INSTANCE_VARIABLES_SignpostAggregationValueStats
+ __OBJC_$_INSTANCE_VARIABLES__SignpostAggregationValueSegmentParser
+ __OBJC_$_PROP_LIST_SignpostAggregationGroupMeasuredValue
+ __OBJC_$_PROP_LIST_SignpostAggregationValueStats
+ __OBJC_$_PROP_LIST__SignpostAggregationValue
+ __OBJC_$_PROP_LIST__SignpostAggregationValueSegmentParser
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SignpostAggregationCAPayloadGenerator
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__SignpostAggregationValue
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SignpostAggregationCAPayloadGenerator
+ __OBJC_$_PROTOCOL_METHOD_TYPES__SignpostAggregationValue
+ __OBJC_$_PROTOCOL_REFS__SignpostAggregationCAPayloadGenerator
+ __OBJC_$_PROTOCOL_REFS__SignpostAggregationValue
+ __OBJC_CLASS_PROTOCOLS_$_SignpostAggregationGroupMeasuredValue
+ __OBJC_CLASS_RO_$_SignpostAggregationGroupMeasuredValue
+ __OBJC_CLASS_RO_$_SignpostAggregationValueStats
+ __OBJC_CLASS_RO_$__SignpostAggregationValueSegmentParser
+ __OBJC_LABEL_PROTOCOL_$__SignpostAggregationCAPayloadGenerator
+ __OBJC_LABEL_PROTOCOL_$__SignpostAggregationValue
+ __OBJC_METACLASS_RO_$_SignpostAggregationGroupMeasuredValue
+ __OBJC_METACLASS_RO_$_SignpostAggregationValueStats
+ __OBJC_METACLASS_RO_$__SignpostAggregationValueSegmentParser
+ __OBJC_PROTOCOL_$__SignpostAggregationCAPayloadGenerator
+ __OBJC_PROTOCOL_$__SignpostAggregationValue
+ ___41-[SignpostAggregationGroup copyWithZone:]_block_invoke_2
+ ___block_descriptor_40_e8_32s_e64_v32?0"NSString"8"SignpostAggregationGroupMeasuredValue"16^B24ls32l8
+ ___block_literal_global.1218
+ ___block_literal_global.405
+ ___block_literal_global.481
+ ___block_literal_global.516
+ ___block_literal_global.758
+ ___block_literal_global.767
+ __addToPayloadDictionary
+ __combinedStdDev
+ _kAggAverageDurationNsKey
+ _kAggAverageKey
+ _kAggBeginTimeDateKey
+ _kAggBeginTimeMCTKey
+ _kAggBeginTimeNsKey
+ _kAggCategoryKey
+ _kAggDescriptionKey
+ _kAggDurationDictKey
+ _kAggDurationNsKey
+ _kAggDurationStdDevNsKey
+ _kAggEndTimeDateKey
+ _kAggEndTimeMCTKey
+ _kAggEndTimeNsKey
+ _kAggGroupNameKey
+ _kAggGroupNameToGroupKey
+ _kAggMaxDurationNsKey
+ _kAggMaxValueKey
+ _kAggMeasuredValueDictKey
+ _kAggMinDurationNsKey
+ _kAggMinValueKey
+ _kAggNameKey
+ _kAggSubsystemKey
+ _kAggTelemetryEnabledKey
+ _kAggTimeRangeArrayKey
+ _kAggTotalDurationNsKey
+ _kAggTotalKey
+ _kAggTypeKey
+ _kAggUnitOfMeasureKey
+ _kAggValueStdDevKey
+ _objc_msgSend$_clearFields
+ _objc_msgSend$_coreAnalyticsMaxFieldName
+ _objc_msgSend$_coreAnalyticsMinFieldName
+ _objc_msgSend$_coreAnalyticsStdDevFieldName
+ _objc_msgSend$_coreAnalyticsTotalFieldName
+ _objc_msgSend$_finalizeState
+ _objc_msgSend$_groupToTypeToMeasuredValue
+ _objc_msgSend$_handleValueSegment:placeholderType:parser:
+ _objc_msgSend$_initWithGroup:type:
+ _objc_msgSend$_initWithParser:
+ _objc_msgSend$_processMetadataSegment:parser:
+ _objc_msgSend$_rawAverage
+ _objc_msgSend$_rawTotal
+ _objc_msgSend$_sumOfDuration0:duration1:errorOut:
+ _objc_msgSend$_sumOfGroup0:group1:errorOut:
+ _objc_msgSend$_sumOfValue0:value1:errorOut:
+ _objc_msgSend$_updateValueDict:withParser:placeholderType:class:
+ _objc_msgSend$average
+ _objc_msgSend$group
+ _objc_msgSend$initWithGroupName:type:unit:
+ _objc_msgSend$max
+ _objc_msgSend$measuredValueTypeToMeasuredValueDict
+ _objc_msgSend$min
+ _objc_msgSend$processSegment:placeholderType:
+ _objc_msgSend$setCount:
+ _objc_msgSend$setGroup:
+ _objc_msgSend$setMax:
+ _objc_msgSend$setMeasuredValueTypeToMeasuredValueDict:
+ _objc_msgSend$setMin:
+ _objc_msgSend$setStddev:
+ _objc_msgSend$setType:
+ _objc_msgSend$setUnit:
+ _objc_msgSend$setValue:
+ _objc_msgSend$set_groupToTypeToMeasuredValue:
+ _objc_msgSend$set_rawAverage:
+ _objc_msgSend$set_rawTotal:
+ _objc_msgSend$shouldAdd
+ _objc_msgSend$stats
+ _objc_msgSend$stddev
+ _objc_msgSend$sumOfStats0:stats1:errorOut:
+ _objc_msgSend$total
+ _objc_msgSend$unit
+ _objc_msgSend$value
+ _serializationTypeNumber.onceToken.402
+ _serializationTypeNumber.onceToken.478
+ _serializationTypeNumber.serializationTypeNumber.403
+ _serializationTypeNumber.serializationTypeNumber.479
- +[SignpostAggregation sumOfAggregation1:aggregation2:errorOut:]
- +[SignpostAggregationGroup _sumOfGroup1:group2:errorOut:]
- +[SignpostAggregationGroupDuration _combinedStdDevFromDuration0:duration1:]
- +[SignpostAggregationGroupDuration _combinedStdDevNsFromCount0:totalDurationNs0:stdDevNs0:count1:totalDurationNs1:stdDevNs1:]
- +[SignpostAggregationGroupDuration _sumOfDuration1:duration2:errorOut:]
- -[SignpostAggregation _checkGroupTypeTuplesForPlaceholderType:errors:]
- -[SignpostAggregation _groupToTypeToDurationStdDevNs]
- -[SignpostAggregation _groupToTypeToMaxDurationNs]
- -[SignpostAggregation _groupToTypeToMinDurationNs]
- -[SignpostAggregation _handleDurationSegment:placeholderType:]
- -[SignpostAggregation _handleDurationStdDevSegment:]
- -[SignpostAggregation _handleMaxDurationSegment:]
- -[SignpostAggregation _handleMinDurationSegment:]
- -[SignpostAggregation _handleTotalDurationSegment:]
- -[SignpostAggregation _processMetadataSegment:]
- -[SignpostAggregation _updateDict:withGroup:type:durationNs:namespaceType:]
- -[SignpostAggregation set_groupToTypeToDurationStdDevNs:]
- -[SignpostAggregation set_groupToTypeToMaxDurationNs:]
- -[SignpostAggregation set_groupToTypeToMinDurationNs:]
- -[SignpostAggregationGroupDuration _addToPayloadDictionary:]
- -[SignpostAggregationGroupDuration _coreAnalyticsDurationStdDevFieldName]
- -[SignpostAggregationGroupDuration _coreAnalyticsMaxDurationFieldName]
- -[SignpostAggregationGroupDuration _coreAnalyticsMinDurationFieldName]
- -[SignpostAggregationGroupDuration _coreAnalyticsTotalDurationFieldName]
- -[SignpostAggregationGroupDuration _initWithMetadataSegment:errorOut:]
- -[SignpostAggregationGroupDuration _initWithType:groupName:durationNs:telemetryEnabled:]
- -[SignpostAggregationGroupDuration _initializeAsSumOfDuration1:duration2:]
- -[SignpostAggregationGroupDuration parentGroup]
- -[SignpostAggregationGroupDuration setMaxDurationNs:]
- -[SignpostAggregationGroupDuration setMinDurationNs:]
- -[SignpostAggregationGroupDuration setParentGroup:]
- -[SignpostAggregationGroupDuration setStdDevNs:]
- _OBJC_IVAR_$_SignpostAggregation.__groupToTypeToDurationStdDevNs
- _OBJC_IVAR_$_SignpostAggregation.__groupToTypeToMaxDurationNs
- _OBJC_IVAR_$_SignpostAggregation.__groupToTypeToMinDurationNs
- _OBJC_IVAR_$_SignpostAggregationGroupDuration._maxDurationNs
- _OBJC_IVAR_$_SignpostAggregationGroupDuration._minDurationNs
- _OBJC_IVAR_$_SignpostAggregationGroupDuration._parentGroup
- _OBJC_IVAR_$_SignpostAggregationGroupDuration._stdDevNs
- _OBJC_IVAR_$_SignpostAggregationGroupDuration._totalDurationNs
- ___block_literal_global.1217
- ___block_literal_global.404
- ___block_literal_global.480
- ___block_literal_global.515
- ___block_literal_global.578
- ___block_literal_global.587
- __unknownAggregationError
- _objc_msgSend$_addToPayloadDictionary:
- _objc_msgSend$_checkGroupTypeTuplesForPlaceholderType:errors:
- _objc_msgSend$_combinedStdDevFromDuration0:duration1:
- _objc_msgSend$_combinedStdDevNsFromCount0:totalDurationNs0:stdDevNs0:count1:totalDurationNs1:stdDevNs1:
- _objc_msgSend$_coreAnalyticsDurationStdDevFieldName
- _objc_msgSend$_coreAnalyticsMaxDurationFieldName
- _objc_msgSend$_coreAnalyticsMinDurationFieldName
- _objc_msgSend$_coreAnalyticsTotalDurationFieldName
- _objc_msgSend$_groupToTypeToDurationStdDevNs
- _objc_msgSend$_groupToTypeToMaxDurationNs
- _objc_msgSend$_groupToTypeToMinDurationNs
- _objc_msgSend$_handleDurationSegment:placeholderType:
- _objc_msgSend$_handleDurationStdDevSegment:
- _objc_msgSend$_handleMaxDurationSegment:
- _objc_msgSend$_handleMinDurationSegment:
- _objc_msgSend$_handleTotalDurationSegment:
- _objc_msgSend$_initWithType:groupName:durationNs:telemetryEnabled:
- _objc_msgSend$_initializeAsSumOfDuration1:duration2:
- _objc_msgSend$_processMetadataSegment:
- _objc_msgSend$_sumOfDuration1:duration2:errorOut:
- _objc_msgSend$_sumOfGroup1:group2:errorOut:
- _objc_msgSend$_updateDict:withGroup:type:durationNs:namespaceType:
- _objc_msgSend$parentGroup
- _objc_msgSend$setMaxDurationNs:
- _objc_msgSend$setMinDurationNs:
- _objc_msgSend$setParentGroup:
- _objc_msgSend$setStdDevNs:
- _objc_msgSend$set_groupToTypeToDurationStdDevNs:
- _objc_msgSend$set_groupToTypeToMaxDurationNs:
- _objc_msgSend$set_groupToTypeToMinDurationNs:
- _objc_msgSend$unsignedLongValue
- _serializationTypeNumber.onceToken.401
- _serializationTypeNumber.onceToken.477
- _serializationTypeNumber.serializationTypeNumber.402
- _serializationTypeNumber.serializationTypeNumber.478
CStrings:
+ "\x05\x15"
+ "\x14"
+ "$"
+ "%@__%@__MaxValue"
+ "%@__%@__MinValue"
+ "%@__%@__TotalValue"
+ "%@__%@__ValueStdDev"
+ "@\"SignpostAggregationValueStats\""
+ "@\"SignpostAggregationValueStats\"16@0:8"
+ "@24@0:8@\"_SignpostAggregationValueSegmentParser\"16"
+ "@36@0:8@16C24@28"
+ "@44@0:8@16@24C32#36"
+ "AggregationDescription"
+ "AverageDurationNs"
+ "AverageValue"
+ "Cannot add nil measured values"
+ "Cannot add stats with and without average value"
+ "Cannot add stats with and without maximum value"
+ "Cannot add stats with and without minimum value"
+ "Cannot add stats with and without stddev value"
+ "Cannot add stats with and without total value"
+ "Cannot specify both raw total and average value"
+ "Collision on stats property: '_rawAverage'"
+ "Collision on stats property: '_rawTotal'"
+ "Collision on stats property: 'max'"
+ "Collision on stats property: 'min'"
+ "Collision on stats property: 'stddev'"
+ "Duplicate telemetry enabled placeholder token for type: %u"
+ "Duplicate units for placeholder type '%@'"
+ "DurationTypeToGroupDurations"
+ "Either total or average is required"
+ "Failed to init duration/value"
+ "Group '%@' was specified by one or more measured values but has no count"
+ "Group '%@', duration type '%@': %@"
+ "Group '%@', measured value type '%@': %@"
+ "GroupName"
+ "MaxValue"
+ "MeasuredValueTypeToMeasuredValues"
+ "Min is greather than max"
+ "MinValue"
+ "Mismatched unit values: %@ vs. %@"
+ "Missing 'count'"
+ "Negative count not supported"
+ "Negative stddev is invalid"
+ "Non-zero average with zero count"
+ "Non-zero raw total with zero count"
+ "SignpostAggregationGroupMeasuredValue"
+ "SignpostAggregationValueStats"
+ "T@\"NSDictionary\",&,N,V_measuredValueTypeToMeasuredValueDict"
+ "T@\"NSMutableDictionary\",&,N,V__groupToTypeToMeasuredValue"
+ "T@\"NSNumber\",&,N,V__rawAverage"
+ "T@\"NSNumber\",&,N,V__rawTotal"
+ "T@\"NSNumber\",&,N,V_count"
+ "T@\"NSNumber\",&,N,V_max"
+ "T@\"NSNumber\",&,N,V_min"
+ "T@\"NSNumber\",&,N,V_stddev"
+ "T@\"NSNumber\",&,N,V_value"
+ "T@\"NSNumber\",R,N,V__durationValue"
+ "T@\"NSString\",&,N,V_group"
+ "T@\"NSString\",&,N,V_type"
+ "T@\"NSString\",&,N,V_unit"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,N,V_unit"
+ "T@\"SignpostAggregationValueStats\",R,N"
+ "T@\"SignpostAggregationValueStats\",R,N,V_stats"
+ "TB,R,N,V__isTotalDuration"
+ "TotalValue"
+ "Tried to add measured values with different group names: %@ vs. %@"
+ "Tried to add measured values with different type: %@ vs. %@"
+ "Unexpected placeholder type: %u"
+ "Unexpected telemetry enabled placeholder token for type: %u"
+ "UnitOfMeasure"
+ "ValueStdDev"
+ "_SignpostAggregationCAPayloadGenerator"
+ "_SignpostAggregationValue"
+ "_SignpostAggregationValueSegmentParser"
+ "__durationValue"
+ "__groupToTypeToMeasuredValue"
+ "__isTotalDuration"
+ "__rawAverage"
+ "__rawTotal"
+ "_clearFields"
+ "_coreAnalyticsMaxFieldName"
+ "_coreAnalyticsMinFieldName"
+ "_coreAnalyticsStdDevFieldName"
+ "_coreAnalyticsTotalFieldName"
+ "_durationValue"
+ "_finalizeState"
+ "_group"
+ "_groupToTypeToMeasuredValue"
+ "_handleValueSegment:placeholderType:parser:"
+ "_initWithGroup:type:"
+ "_initWithParser:"
+ "_isTotalDuration"
+ "_max"
+ "_measuredValueTypeToMeasuredValueDict"
+ "_min"
+ "_processMetadataSegment:parser:"
+ "_rawAverage"
+ "_rawTotal"
+ "_stats"
+ "_stddev"
+ "_sumOfDuration0:duration1:errorOut:"
+ "_sumOfGroup0:group1:errorOut:"
+ "_sumOfValue0:value1:errorOut:"
+ "_unit"
+ "_updateValueDict:withParser:placeholderType:class:"
+ "_value"
+ "a"
+ "average"
+ "average_duration_ns"
+ "group"
+ "initWithGroupName:type:unit:"
+ "max"
+ "measure_average"
+ "measure_max"
+ "measure_min"
+ "measure_stddev"
+ "measure_total"
+ "measure_unit="
+ "measuredValueTypeToMeasuredValueDict"
+ "min"
+ "processSegment:placeholderType:"
+ "seconds"
+ "setCount:"
+ "setGroup:"
+ "setMax:"
+ "setMeasuredValueTypeToMeasuredValueDict:"
+ "setMin:"
+ "setStddev:"
+ "setType:"
+ "setUnit:"
+ "setValue:"
+ "set_groupToTypeToMeasuredValue:"
+ "set_rawAverage:"
+ "set_rawTotal:"
+ "shouldAdd"
+ "stats"
+ "stddev"
+ "sumOfAggregation0:aggregation1:errorOut:"
+ "sumOfStats0:stats1:errorOut:"
+ "total"
+ "unit"
+ "v32@?0@\"NSString\"8@\"SignpostAggregationGroupMeasuredValue\"16^B24"
+ "value"
- "\x05\x17"
- "\x12\x13"
- "#"
- "'group' specified multiple times for aggregation duration"
- "'telemetry=enabled' specified multiple times for aggregation duration"
- "'type' specified multiple times for aggregation duration"
- "@\"SignpostAggregationGroup\""
- "@44@0:8@16@24Q32B40"
- "@64@0:8Q16Q24d32Q40Q48d56"
- "Cannot add durations with and without duration stddev value"
- "Cannot add durations with and without maximum value"
- "Cannot add durations with and without minimum value"
- "Duplicate %@ duration for group '%@', type '%@'"
- "Duplicate group duration type: '%@'"
- "DurationNameToGroupDurations"
- "Group '%@', duration type '%@': min duration > max duration"
- "Invalid type for aggregation duration"
- "Invalid type namespace for aggregation duration"
- "No 'group' specified for aggregation duration"
- "No 'type' specified for aggregation duration"
- "No total duration for group '%@', type '%@' (%@)"
- "T@\"NSMutableDictionary\",&,N,V__groupToTypeToDurationStdDevNs"
- "T@\"NSMutableDictionary\",&,N,V__groupToTypeToMaxDurationNs"
- "T@\"NSMutableDictionary\",&,N,V__groupToTypeToMinDurationNs"
- "T@\"NSNumber\",&,N,V_maxDurationNs"
- "T@\"NSNumber\",&,N,V_minDurationNs"
- "T@\"NSNumber\",&,N,V_stdDevNs"
- "T@\"SignpostAggregationGroup\",W,N,V_parentGroup"
- "TQ,R,N,V_totalDurationNs"
- "Telemetry not permitted for placeholder type '%@'"
- "Unexpected argument type for specified for aggregation duration"
- "__groupToTypeToDurationStdDevNs"
- "__groupToTypeToMaxDurationNs"
- "__groupToTypeToMinDurationNs"
- "_addToPayloadDictionary:"
- "_checkGroupTypeTuplesForPlaceholderType:errors:"
- "_combinedStdDevFromDuration0:duration1:"
- "_combinedStdDevNsFromCount0:totalDurationNs0:stdDevNs0:count1:totalDurationNs1:stdDevNs1:"
- "_coreAnalyticsDurationStdDevFieldName"
- "_coreAnalyticsMaxDurationFieldName"
- "_coreAnalyticsMinDurationFieldName"
- "_coreAnalyticsTotalDurationFieldName"
- "_groupToTypeToDurationStdDevNs"
- "_groupToTypeToMaxDurationNs"
- "_groupToTypeToMinDurationNs"
- "_handleDurationSegment:placeholderType:"
- "_handleDurationStdDevSegment:"
- "_handleMaxDurationSegment:"
- "_handleMinDurationSegment:"
- "_handleTotalDurationSegment:"
- "_initWithType:groupName:durationNs:telemetryEnabled:"
- "_initializeAsSumOfDuration1:duration2:"
- "_maxDurationNs"
- "_minDurationNs"
- "_parentGroup"
- "_processMetadataSegment:"
- "_stdDevNs"
- "_sumOfDuration1:duration2:errorOut:"
- "_sumOfGroup1:group2:errorOut:"
- "_totalDurationNs"
- "_updateDict:withGroup:type:durationNs:namespaceType:"
- "parentGroup"
- "setMaxDurationNs:"
- "setMinDurationNs:"
- "setParentGroup:"
- "setStdDevNs:"
- "set_groupToTypeToDurationStdDevNs:"
- "set_groupToTypeToMaxDurationNs:"
- "set_groupToTypeToMinDurationNs:"
- "sumOfAggregation1:aggregation2:errorOut:"
- "unsignedLongValue"
- "v28@0:8C16@20"

```
