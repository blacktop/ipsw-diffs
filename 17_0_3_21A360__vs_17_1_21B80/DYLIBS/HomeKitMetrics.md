## HomeKitMetrics

> `/System/Library/PrivateFrameworks/HomeKitMetrics.framework/HomeKitMetrics`

```diff

-1054.1.7.1.4
-  __TEXT.__text: 0xe37c
-  __TEXT.__auth_stubs: 0x4c0
-  __TEXT.__objc_methlist: 0x1314
+1076.2.8.1.1
+  __TEXT.__text: 0x137bc
+  __TEXT.__auth_stubs: 0x4e0
+  __TEXT.__objc_methlist: 0x18a4
   __TEXT.__const: 0x30
-  __TEXT.__gcc_except_tab: 0x1e4
-  __TEXT.__cstring: 0x50c
-  __TEXT.__oslogstring: 0xb45
-  __TEXT.__unwind_info: 0x500
-  __TEXT.__objc_classname: 0x50d
-  __TEXT.__objc_methname: 0x35b6
-  __TEXT.__objc_methtype: 0xbc7
-  __TEXT.__objc_stubs: 0x2920
-  __DATA_CONST.__got: 0xd0
-  __DATA_CONST.__const: 0x368
-  __DATA_CONST.__objc_classlist: 0x140
+  __TEXT.__gcc_except_tab: 0x550
+  __TEXT.__cstring: 0x6ef
+  __TEXT.__oslogstring: 0xe20
+  __TEXT.__unwind_info: 0x728
+  __TEXT.__objc_classname: 0x62c
+  __TEXT.__objc_methname: 0x3d94
+  __TEXT.__objc_methtype: 0xcd9
+  __TEXT.__objc_stubs: 0x2e80
+  __DATA_CONST.__got: 0xc8
+  __DATA_CONST.__const: 0x3e0
+  __DATA_CONST.__objc_classlist: 0x180
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0xa8
+  __DATA_CONST.__objc_protolist: 0xc0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2f18
-  __DATA_CONST.__objc_selrefs: 0xcf8
-  __DATA_CONST.__objc_arraydata: 0x8
-  __AUTH_CONST.__objc_const: 0x1090
+  __DATA_CONST.__objc_const: 0x3780
+  __DATA_CONST.__objc_selrefs: 0xf00
+  __DATA_CONST.__objc_arraydata: 0x10
+  __AUTH_CONST.__objc_const: 0x1558
+  __AUTH_CONST.__cfstring: 0xa60
   __AUTH_CONST.__objc_floatobj: 0x20
-  __AUTH_CONST.__cfstring: 0x840
   __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__objc_intobj: 0x90
+  __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x270
-  __AUTH.__objc_data: 0x1e0
+  __AUTH_CONST.__objc_arrayobj: 0x30
+  __AUTH_CONST.__auth_got: 0x280
+  __AUTH.__objc_data: 0x5f0
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x1e0
-  __DATA.__objc_superrefs: 0xf0
-  __DATA.__objc_ivar: 0x1cc
-  __DATA.__data: 0x7e8
+  __DATA.__objc_classrefs: 0x228
+  __DATA.__objc_superrefs: 0x120
+  __DATA.__objc_ivar: 0x220
+  __DATA.__data: 0x928
   __DATA.__bss: 0x58
-  __DATA_DIRTY.__objc_data: 0xaa0
+  __DATA_DIRTY.__objc_data: 0x910
   __DATA_DIRTY.__bss: 0xa0
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/PrivateFrameworks/SiriInstrumentation.framework/SiriInstrumentation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 329EA291-4A5F-370F-ACDB-FB67999ADB77
-  Functions: 415
-  Symbols:   1915
-  CStrings:  1036
+  UUID: 8F4A6EF4-090B-3C09-9BC8-CAF72CD3FBDB
+  Functions: 528
+  Symbols:   2325
+  CStrings:  1185
 
Symbols:
+ +[HMMAccessoryGroupSpecifier descriptorTypeNamePrefix]
+ +[HMMCoreDataAccessoryGroup(CoreDataProperties) fetchRequest]
+ +[HMMCoreDataGroupCounter(CoreDataProperties) fetchRequest]
+ +[HMMCoreDataGroupValueStatistics(CoreDataProperties) fetchRequest]
+ +[HMMCoreDataHomeGroup(CoreDataProperties) fetchRequest]
+ +[HMMCoreDataNamedGroup(CoreDataProperties) fetchRequest]
+ +[HMMHomeGroupSpecifier descriptorTypeNamePrefix]
+ +[HMMNamedGroupSpecifier descriptorTypeNamePrefix]
+ +[HMMStandardCounterGroup deleteCountersUsingPredicate:coreDataStorage:]
+ +[HMMStandardCounterGroup deletePartitionsAfterDate:coreDataStorage:]
+ +[HMMStandardCounterGroup deletePartitionsBeforeDate:coreDataStorage:]
+ +[HMMStandardCounterGroup groupFromSpecifier:partitionProvider:coreDataStorage:]
+ +[HMMStandardStatisticsGroup deletePartitionsAfterDate:coreDataStorage:]
+ +[HMMStandardStatisticsGroup deletePartitionsBeforeDate:coreDataStorage:]
+ +[HMMStandardStatisticsGroup deleteStatisticsUsingPredicate:coreDataStorage:]
+ +[HMMStandardStatisticsGroup groupFromSpecifier:partitionProvider:coreDataStorage:]
+ -[HMMAccessoryGroupSpecifier .cxx_destruct]
+ -[HMMAccessoryGroupSpecifier accessoryUUID]
+ -[HMMAccessoryGroupSpecifier coreDataGroupUsingContext:]
+ -[HMMAccessoryGroupSpecifier description]
+ -[HMMAccessoryGroupSpecifier descriptor]
+ -[HMMAccessoryGroupSpecifier hash]
+ -[HMMAccessoryGroupSpecifier initWithAccessoryUUID:homeUUID:groupName:]
+ -[HMMAccessoryGroupSpecifier isEqual:]
+ -[HMMAccessoryGroupSpecifier isEqualToAccessoryGroupSpecifier:]
+ -[HMMCoreDataAccessoryGroup(HMMGroupSpecifier) groupSpecifier]
+ -[HMMCoreDataCounterStorage initWithModelName:atPath:radarInitiator:]
+ -[HMMCoreDataGroupValueStatistics(HMMCounterStatistics) addValue:]
+ -[HMMCoreDataGroupValueStatistics(HMMCounterStatistics) counterStatistics]
+ -[HMMCoreDataHomeGroup(HMMGroupSpecifier) groupSpecifier]
+ -[HMMCoreDataNamedGroup(HMMGroupSpecifier) groupSpecifier]
+ -[HMMCounterStatistics averageValue]
+ -[HMMCounterStatistics initWithMinValue:maxValue:sumOfValues:valueCount:]
+ -[HMMCounterStatistics maxValue]
+ -[HMMCounterStatistics minValue]
+ -[HMMCounterStatistics valueCount]
+ -[HMMCountersManager activeEphemeralContainers]
+ -[HMMCountersManager addEphemeralContainer:]
+ -[HMMCountersManager coreDataStorage]
+ -[HMMCountersManager counterGroupForAccessoryUUID:homeUUID:groupName:]
+ -[HMMCountersManager counterGroupForSpecifier:coreDataGroup:]
+ -[HMMCountersManager counterGroups]
+ -[HMMCountersManager deactivateEphemeralContainer:]
+ -[HMMCountersManager deletePartitionsAfterDate:]
+ -[HMMCountersManager deletePartitionsBeforeDate:]
+ -[HMMCountersManager enumerateCounterGroupsUsingBlock:]
+ -[HMMCountersManager enumerateStatisticsGroupsUsingBlock:]
+ -[HMMCountersManager initWithDataModelName:atPath:radarInitiator:]
+ -[HMMCountersManager initWithDataModelName:atPath:radarInitiator:dateProvider:]
+ -[HMMCountersManager loadAllCounterGroups]
+ -[HMMCountersManager loadAllStatisticsGroups]
+ -[HMMCountersManager removeEphemeralContainer:]
+ -[HMMCountersManager statisticsGroupForAccessoryUUID:homeUUID:groupName:]
+ -[HMMCountersManager statisticsGroupForHomeUUID:groupName:]
+ -[HMMCountersManager statisticsGroupForHomeUUIDFromLogEvent:groupName:]
+ -[HMMCountersManager statisticsGroupForName:]
+ -[HMMCountersManager statisticsGroupForSpecifier:coreDataGroup:]
+ -[HMMCountersManager statisticsGroups]
+ -[HMMEphemeralCounterContainer .cxx_destruct]
+ -[HMMEphemeralCounterContainer active]
+ -[HMMEphemeralCounterContainer counters]
+ -[HMMEphemeralCounterContainer incrementCounter:by:]
+ -[HMMEphemeralCounterContainer init]
+ -[HMMEphemeralCounterContainer isActive]
+ -[HMMEphemeralCounterContainer isEmpty]
+ -[HMMEphemeralCounterContainer setActive:]
+ -[HMMEphemeralCounterContainer valueForCounter:]
+ -[HMMEphemeralStatisticsContainer .cxx_destruct]
+ -[HMMEphemeralStatisticsContainer active]
+ -[HMMEphemeralStatisticsContainer addValue:toStatistics:]
+ -[HMMEphemeralStatisticsContainer init]
+ -[HMMEphemeralStatisticsContainer isActive]
+ -[HMMEphemeralStatisticsContainer isEmpty]
+ -[HMMEphemeralStatisticsContainer setActive:]
+ -[HMMEphemeralStatisticsContainer statistics:]
+ -[HMMEphemeralStatisticsContainer statistics]
+ -[HMMHomeGroupSpecifier .cxx_destruct]
+ -[HMMHomeGroupSpecifier coreDataGroupUsingContext:]
+ -[HMMHomeGroupSpecifier description]
+ -[HMMHomeGroupSpecifier descriptor]
+ -[HMMHomeGroupSpecifier hash]
+ -[HMMHomeGroupSpecifier homeUUID]
+ -[HMMHomeGroupSpecifier initWithHomeUUID:groupName:]
+ -[HMMHomeGroupSpecifier isEqual:]
+ -[HMMHomeGroupSpecifier isEqualToHomeGroupSpecifier:]
+ -[HMMMutableCounterStatistics addValue:]
+ -[HMMMutableCounterStatistics statistics]
+ -[HMMNamedGroupSpecifier .cxx_destruct]
+ -[HMMNamedGroupSpecifier copyWithZone:]
+ -[HMMNamedGroupSpecifier coreDataGroupUsingContext:]
+ -[HMMNamedGroupSpecifier description]
+ -[HMMNamedGroupSpecifier descriptor]
+ -[HMMNamedGroupSpecifier groupName]
+ -[HMMNamedGroupSpecifier hash]
+ -[HMMNamedGroupSpecifier initWithGroupName:]
+ -[HMMNamedGroupSpecifier isEqual:]
+ -[HMMNamedGroupSpecifier isEqualToGroupNameSpecifier:]
+ -[HMMStandardCounterGroup .cxx_destruct]
+ -[HMMStandardCounterGroup addEphemeralContainer:]
+ -[HMMStandardCounterGroup addObserver:forCounter:]
+ -[HMMStandardCounterGroup coreDataGroup]
+ -[HMMStandardCounterGroup coreDataStorage]
+ -[HMMStandardCounterGroup countersInDatePartition:]
+ -[HMMStandardCounterGroup countersInEphemeralContainer:]
+ -[HMMStandardCounterGroup datePartitions]
+ -[HMMStandardCounterGroup deactivateEphemeralContainer:]
+ -[HMMStandardCounterGroup ephemeralContainerNames]
+ -[HMMStandardCounterGroup ephemeralContainers]
+ -[HMMStandardCounterGroup incrementCounter:]
+ -[HMMStandardCounterGroup incrementCounter:by:]
+ -[HMMStandardCounterGroup initWithCoreDataGroup:partitionProvider:coreDataStorage:]
+ -[HMMStandardCounterGroup notifyObserversForCounter:previousCount:newCount:]
+ -[HMMStandardCounterGroup observersForCounter:]
+ -[HMMStandardCounterGroup observers]
+ -[HMMStandardCounterGroup partitionProvider]
+ -[HMMStandardCounterGroup removeEphemeralContainer:]
+ -[HMMStandardCounterGroup setCoreDataGroup:]
+ -[HMMStandardCounterGroup sumOfCountersInDatePartition:]
+ -[HMMStandardCounterGroup sumOfCountersInEphemeralContainer:]
+ -[HMMStandardCounterGroup valueForCounter:inDatePartition:]
+ -[HMMStandardCounterGroup valueForCounter:inEphemeralContainer:]
+ -[HMMStandardStatisticsGroup .cxx_destruct]
+ -[HMMStandardStatisticsGroup addEphemeralContainer:]
+ -[HMMStandardStatisticsGroup addMaxValueObserver:forStatistics:]
+ -[HMMStandardStatisticsGroup addValue:toStatistics:]
+ -[HMMStandardStatisticsGroup coreDataGroup]
+ -[HMMStandardStatisticsGroup coreDataStorage]
+ -[HMMStandardStatisticsGroup datePartitions]
+ -[HMMStandardStatisticsGroup deactivateEphemeralContainer:]
+ -[HMMStandardStatisticsGroup ephemeralContainerNames]
+ -[HMMStandardStatisticsGroup ephemeralContainers]
+ -[HMMStandardStatisticsGroup initWithCoreDataGroup:partitionProvider:coreDataStorage:]
+ -[HMMStandardStatisticsGroup notifyObserversForStatistics:previousMax:newMax:]
+ -[HMMStandardStatisticsGroup observersForStatistics:]
+ -[HMMStandardStatisticsGroup observers]
+ -[HMMStandardStatisticsGroup partitionProvider]
+ -[HMMStandardStatisticsGroup removeEphemeralContainer:]
+ -[HMMStandardStatisticsGroup setCoreDataGroup:]
+ -[HMMStandardStatisticsGroup statistics:inDatePartition:]
+ -[HMMStandardStatisticsGroup statistics:inEphemeralContainer:]
+ -[HMMStandardStatisticsGroup statisticsInDatePartition:]
+ -[HMMStandardStatisticsGroup statisticsInEphemeralContainer:]
+ GCC_except_table108
+ GCC_except_table133
+ GCC_except_table137
+ GCC_except_table173
+ GCC_except_table174
+ GCC_except_table175
+ GCC_except_table176
+ GCC_except_table177
+ GCC_except_table178
+ GCC_except_table179
+ GCC_except_table185
+ GCC_except_table187
+ GCC_except_table190
+ GCC_except_table191
+ GCC_except_table197
+ GCC_except_table232
+ GCC_except_table233
+ GCC_except_table234
+ GCC_except_table246
+ GCC_except_table247
+ GCC_except_table248
+ GCC_except_table249
+ GCC_except_table250
+ GCC_except_table251
+ GCC_except_table252
+ GCC_except_table254
+ GCC_except_table258
+ GCC_except_table260
+ GCC_except_table262
+ GCC_except_table266
+ GCC_except_table267
+ GCC_except_table273
+ GCC_except_table308
+ GCC_except_table494
+ GCC_except_table495
+ GCC_except_table496
+ GCC_except_table497
+ GCC_except_table498
+ GCC_except_table504
+ GCC_except_table507
+ GCC_except_table513
+ _HMMGroupDescriptorAccessoryUUID
+ _HMMGroupDescriptorGroupName
+ _HMMGroupDescriptorHomeUUID
+ _HMMGroupDescriptorSingleString
+ _OBJC_CLASS_$_HMMAccessoryGroupSpecifier
+ _OBJC_CLASS_$_HMMCoreDataAccessoryGroup
+ _OBJC_CLASS_$_HMMCoreDataGroupCounter
+ _OBJC_CLASS_$_HMMCoreDataGroupValueStatistics
+ _OBJC_CLASS_$_HMMCoreDataHomeGroup
+ _OBJC_CLASS_$_HMMCoreDataNamedGroup
+ _OBJC_CLASS_$_HMMCounterStatistics
+ _OBJC_CLASS_$_HMMEphemeralCounterContainer
+ _OBJC_CLASS_$_HMMEphemeralStatisticsContainer
+ _OBJC_CLASS_$_HMMHomeGroupSpecifier
+ _OBJC_CLASS_$_HMMMutableCounterStatistics
+ _OBJC_CLASS_$_HMMNamedGroupSpecifier
+ _OBJC_CLASS_$_HMMStandardCounterGroup
+ _OBJC_CLASS_$_HMMStandardStatisticsGroup
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_IVAR_$_HMMAccessoryGroupSpecifier._accessoryUUID
+ _OBJC_IVAR_$_HMMCoreDataCounterStorage._radarInitiator
+ _OBJC_IVAR_$_HMMCounterStatistics._maxValue
+ _OBJC_IVAR_$_HMMCounterStatistics._minValue
+ _OBJC_IVAR_$_HMMCounterStatistics._sumOfValues
+ _OBJC_IVAR_$_HMMCounterStatistics._valueCount
+ _OBJC_IVAR_$_HMMCountersManager._coreDataStorage
+ _OBJC_IVAR_$_HMMCountersManager._counterGroups
+ _OBJC_IVAR_$_HMMCountersManager._ephemeralContainerNames
+ _OBJC_IVAR_$_HMMCountersManager._statisticsGroups
+ _OBJC_IVAR_$_HMMEphemeralCounterContainer._active
+ _OBJC_IVAR_$_HMMEphemeralCounterContainer._counters
+ _OBJC_IVAR_$_HMMEphemeralStatisticsContainer._active
+ _OBJC_IVAR_$_HMMEphemeralStatisticsContainer._statistics
+ _OBJC_IVAR_$_HMMHomeGroupSpecifier._homeUUID
+ _OBJC_IVAR_$_HMMMutableCounterStatistics._maxValue
+ _OBJC_IVAR_$_HMMMutableCounterStatistics._minValue
+ _OBJC_IVAR_$_HMMMutableCounterStatistics._sumOfValues
+ _OBJC_IVAR_$_HMMMutableCounterStatistics._valueCount
+ _OBJC_IVAR_$_HMMNamedGroupSpecifier._groupName
+ _OBJC_IVAR_$_HMMStandardCounterGroup._coreDataGroup
+ _OBJC_IVAR_$_HMMStandardCounterGroup._coreDataGroupToken
+ _OBJC_IVAR_$_HMMStandardCounterGroup._coreDataStorage
+ _OBJC_IVAR_$_HMMStandardCounterGroup._ephemeralContainers
+ _OBJC_IVAR_$_HMMStandardCounterGroup._lock
+ _OBJC_IVAR_$_HMMStandardCounterGroup._observers
+ _OBJC_IVAR_$_HMMStandardCounterGroup._partitionProvider
+ _OBJC_IVAR_$_HMMStandardStatisticsGroup._coreDataGroup
+ _OBJC_IVAR_$_HMMStandardStatisticsGroup._coreDataGroupToken
+ _OBJC_IVAR_$_HMMStandardStatisticsGroup._coreDataStorage
+ _OBJC_IVAR_$_HMMStandardStatisticsGroup._ephemeralContainers
+ _OBJC_IVAR_$_HMMStandardStatisticsGroup._lock
+ _OBJC_IVAR_$_HMMStandardStatisticsGroup._observers
+ _OBJC_IVAR_$_HMMStandardStatisticsGroup._partitionProvider
+ _OBJC_METACLASS_$_HMMAccessoryGroupSpecifier
+ _OBJC_METACLASS_$_HMMCoreDataAccessoryGroup
+ _OBJC_METACLASS_$_HMMCoreDataGroupCounter
+ _OBJC_METACLASS_$_HMMCoreDataGroupValueStatistics
+ _OBJC_METACLASS_$_HMMCoreDataHomeGroup
+ _OBJC_METACLASS_$_HMMCoreDataNamedGroup
+ _OBJC_METACLASS_$_HMMCounterStatistics
+ _OBJC_METACLASS_$_HMMEphemeralCounterContainer
+ _OBJC_METACLASS_$_HMMEphemeralStatisticsContainer
+ _OBJC_METACLASS_$_HMMHomeGroupSpecifier
+ _OBJC_METACLASS_$_HMMMutableCounterStatistics
+ _OBJC_METACLASS_$_HMMNamedGroupSpecifier
+ _OBJC_METACLASS_$_HMMStandardCounterGroup
+ _OBJC_METACLASS_$_HMMStandardStatisticsGroup
+ __OBJC_$_CLASS_METHODS_HMMAccessoryGroupSpecifier
+ __OBJC_$_CLASS_METHODS_HMMCoreDataAccessoryGroup(HMMGroupSpecifier|CoreDataProperties)
+ __OBJC_$_CLASS_METHODS_HMMCoreDataGroupCounter(CoreDataProperties)
+ __OBJC_$_CLASS_METHODS_HMMCoreDataGroupValueStatistics(HMMCounterStatistics|CoreDataProperties)
+ __OBJC_$_CLASS_METHODS_HMMCoreDataHomeGroup(HMMGroupSpecifier|CoreDataProperties)
+ __OBJC_$_CLASS_METHODS_HMMCoreDataNamedGroup(HMMGroupSpecifier|CoreDataProperties)
+ __OBJC_$_CLASS_METHODS_HMMHomeGroupSpecifier
+ __OBJC_$_CLASS_METHODS_HMMNamedGroupSpecifier
+ __OBJC_$_CLASS_METHODS_HMMStandardCounterGroup
+ __OBJC_$_CLASS_METHODS_HMMStandardStatisticsGroup
+ __OBJC_$_CLASS_PROP_LIST_HMMGroupSpecifier
+ __OBJC_$_CLASS_PROP_LIST_HMMNamedGroupSpecifier
+ __OBJC_$_INSTANCE_METHODS_HMMAccessoryGroupSpecifier
+ __OBJC_$_INSTANCE_METHODS_HMMCoreDataAccessoryGroup(HMMGroupSpecifier|CoreDataProperties)
+ __OBJC_$_INSTANCE_METHODS_HMMCoreDataGroupValueStatistics(HMMCounterStatistics|CoreDataProperties)
+ __OBJC_$_INSTANCE_METHODS_HMMCoreDataHomeGroup(HMMGroupSpecifier|CoreDataProperties)
+ __OBJC_$_INSTANCE_METHODS_HMMCoreDataNamedGroup(HMMGroupSpecifier|CoreDataProperties)
+ __OBJC_$_INSTANCE_METHODS_HMMCounterStatistics
+ __OBJC_$_INSTANCE_METHODS_HMMEphemeralCounterContainer
+ __OBJC_$_INSTANCE_METHODS_HMMEphemeralStatisticsContainer
+ __OBJC_$_INSTANCE_METHODS_HMMHomeGroupSpecifier
+ __OBJC_$_INSTANCE_METHODS_HMMMutableCounterStatistics
+ __OBJC_$_INSTANCE_METHODS_HMMNamedGroupSpecifier
+ __OBJC_$_INSTANCE_METHODS_HMMStandardCounterGroup
+ __OBJC_$_INSTANCE_METHODS_HMMStandardStatisticsGroup
+ __OBJC_$_INSTANCE_VARIABLES_HMMAccessoryGroupSpecifier
+ __OBJC_$_INSTANCE_VARIABLES_HMMCounterStatistics
+ __OBJC_$_INSTANCE_VARIABLES_HMMEphemeralCounterContainer
+ __OBJC_$_INSTANCE_VARIABLES_HMMEphemeralStatisticsContainer
+ __OBJC_$_INSTANCE_VARIABLES_HMMHomeGroupSpecifier
+ __OBJC_$_INSTANCE_VARIABLES_HMMMutableCounterStatistics
+ __OBJC_$_INSTANCE_VARIABLES_HMMNamedGroupSpecifier
+ __OBJC_$_INSTANCE_VARIABLES_HMMStandardCounterGroup
+ __OBJC_$_INSTANCE_VARIABLES_HMMStandardStatisticsGroup
+ __OBJC_$_PROP_LIST_HMMAccessoryGroupSpecifier
+ __OBJC_$_PROP_LIST_HMMCounterStatistics
+ __OBJC_$_PROP_LIST_HMMEphemeralCounterContainer
+ __OBJC_$_PROP_LIST_HMMEphemeralStatisticsContainer
+ __OBJC_$_PROP_LIST_HMMGroupSpecifier
+ __OBJC_$_PROP_LIST_HMMHomeGroupSpecifier
+ __OBJC_$_PROP_LIST_HMMMutableCounterStatistics
+ __OBJC_$_PROP_LIST_HMMNamedGroupSpecifier
+ __OBJC_$_PROP_LIST_HMMStandardCounterGroup
+ __OBJC_$_PROP_LIST_HMMStandardStatisticsGroup
+ __OBJC_$_PROP_LIST_HMMStatisticsGroup
+ __OBJC_$_PROTOCOL_CLASS_METHODS_HMMGroupSpecifier
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMMGroupSpecifier
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMMStatisticsGroup
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSCopying
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMMGroupSpecifier
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMMStatisticsGroup
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSCopying
+ __OBJC_$_PROTOCOL_REFS_HMMGroupSpecifier
+ __OBJC_$_PROTOCOL_REFS_HMMStatisticsGroup
+ __OBJC_CLASS_PROTOCOLS_$_HMMNamedGroupSpecifier
+ __OBJC_CLASS_PROTOCOLS_$_HMMStandardCounterGroup
+ __OBJC_CLASS_PROTOCOLS_$_HMMStandardStatisticsGroup
+ __OBJC_CLASS_RO_$_HMMAccessoryGroupSpecifier
+ __OBJC_CLASS_RO_$_HMMCoreDataAccessoryGroup
+ __OBJC_CLASS_RO_$_HMMCoreDataGroupCounter
+ __OBJC_CLASS_RO_$_HMMCoreDataGroupValueStatistics
+ __OBJC_CLASS_RO_$_HMMCoreDataHomeGroup
+ __OBJC_CLASS_RO_$_HMMCoreDataNamedGroup
+ __OBJC_CLASS_RO_$_HMMCounterStatistics
+ __OBJC_CLASS_RO_$_HMMEphemeralCounterContainer
+ __OBJC_CLASS_RO_$_HMMEphemeralStatisticsContainer
+ __OBJC_CLASS_RO_$_HMMHomeGroupSpecifier
+ __OBJC_CLASS_RO_$_HMMMutableCounterStatistics
+ __OBJC_CLASS_RO_$_HMMNamedGroupSpecifier
+ __OBJC_CLASS_RO_$_HMMStandardCounterGroup
+ __OBJC_CLASS_RO_$_HMMStandardStatisticsGroup
+ __OBJC_LABEL_PROTOCOL_$_HMMGroupSpecifier
+ __OBJC_LABEL_PROTOCOL_$_HMMStatisticsGroup
+ __OBJC_LABEL_PROTOCOL_$_NSCopying
+ __OBJC_METACLASS_RO_$_HMMAccessoryGroupSpecifier
+ __OBJC_METACLASS_RO_$_HMMCoreDataAccessoryGroup
+ __OBJC_METACLASS_RO_$_HMMCoreDataGroupCounter
+ __OBJC_METACLASS_RO_$_HMMCoreDataGroupValueStatistics
+ __OBJC_METACLASS_RO_$_HMMCoreDataHomeGroup
+ __OBJC_METACLASS_RO_$_HMMCoreDataNamedGroup
+ __OBJC_METACLASS_RO_$_HMMCounterStatistics
+ __OBJC_METACLASS_RO_$_HMMEphemeralCounterContainer
+ __OBJC_METACLASS_RO_$_HMMEphemeralStatisticsContainer
+ __OBJC_METACLASS_RO_$_HMMHomeGroupSpecifier
+ __OBJC_METACLASS_RO_$_HMMMutableCounterStatistics
+ __OBJC_METACLASS_RO_$_HMMNamedGroupSpecifier
+ __OBJC_METACLASS_RO_$_HMMStandardCounterGroup
+ __OBJC_METACLASS_RO_$_HMMStandardStatisticsGroup
+ __OBJC_PROTOCOL_$_HMMGroupSpecifier
+ __OBJC_PROTOCOL_$_HMMStatisticsGroup
+ __OBJC_PROTOCOL_$_NSCopying
+ ___41-[HMMStandardCounterGroup datePartitions]_block_invoke
+ ___42-[HMMCountersManager loadAllCounterGroups]_block_invoke
+ ___44-[HMMStandardStatisticsGroup datePartitions]_block_invoke
+ ___45-[HMMCountersManager loadAllStatisticsGroups]_block_invoke
+ ___45-[HMMEphemeralStatisticsContainer statistics]_block_invoke
+ ___47-[HMMStandardCounterGroup incrementCounter:by:]_block_invoke
+ ___51-[HMMStandardCounterGroup countersInDatePartition:]_block_invoke
+ ___52-[HMMStandardStatisticsGroup addValue:toStatistics:]_block_invoke
+ ___55-[HMMCountersManager enumerateCounterGroupsUsingBlock:]_block_invoke
+ ___56-[HMMStandardCounterGroup sumOfCountersInDatePartition:]_block_invoke
+ ___56-[HMMStandardStatisticsGroup statisticsInDatePartition:]_block_invoke
+ ___57-[HMMStandardStatisticsGroup statistics:inDatePartition:]_block_invoke
+ ___58-[HMMCountersManager enumerateStatisticsGroupsUsingBlock:]_block_invoke
+ ___59-[HMMStandardCounterGroup valueForCounter:inDatePartition:]_block_invoke
+ ___72+[HMMStandardCounterGroup deleteCountersUsingPredicate:coreDataStorage:]_block_invoke
+ ___77+[HMMStandardStatisticsGroup deleteStatisticsUsingPredicate:coreDataStorage:]_block_invoke
+ ___80+[HMMStandardCounterGroup groupFromSpecifier:partitionProvider:coreDataStorage:]_block_invoke
+ ___83+[HMMStandardStatisticsGroup groupFromSpecifier:partitionProvider:coreDataStorage:]_block_invoke
+ ___Block_byref_object_copy_.1050
+ ___Block_byref_object_copy_.707
+ ___Block_byref_object_dispose_.1051
+ ___Block_byref_object_dispose_.708
+ ___block_descriptor_40_e8_32bs_e55_v32?0"<HMMGroupSpecifier>"8"<HMMCounterGroup>"16^B24ls32l8
+ ___block_descriptor_40_e8_32bs_e58_v32?0"<HMMGroupSpecifier>"8"<HMMStatisticsGroup>"16^B24ls32l8
+ ___block_descriptor_40_e8_32s_e54_v32?0"NSString"8"HMMMutableCounterStatistics"16^B24ls32l8
+ ___block_descriptor_48_e8_32s40r_e32_v16?0"NSManagedObjectContext"8lr40l8s32l8
+ ___block_descriptor_48_e8_32s_e32_v16?0"NSManagedObjectContext"8ls32l8
+ ___block_literal_global.1181
+ ___block_literal_global.1448
+ ___block_literal_global.164
+ ___block_literal_global.1746
+ ___block_literal_global.1855
+ ___block_literal_global.247
+ ___block_literal_global.640
+ ___block_literal_global.861
+ __unnamed_array_storage.724
+ _logCategory._hmf_once_t1.1745
+ _logCategory._hmf_once_v2.1747
+ _objc_msgSend$accessoryUUID
+ _objc_msgSend$addEphemeralContainer:
+ _objc_msgSend$addValue:
+ _objc_msgSend$addValue:toStatistics:
+ _objc_msgSend$allKeys
+ _objc_msgSend$coreDataStorage
+ _objc_msgSend$counterGroupForSpecifier:coreDataGroup:
+ _objc_msgSend$counterStatistics
+ _objc_msgSend$counters
+ _objc_msgSend$countersInEphemeralContainer:
+ _objc_msgSend$deactivateEphemeralContainer:
+ _objc_msgSend$deleteCountersUsingPredicate:coreDataStorage:
+ _objc_msgSend$deletePartitionsAfterDate:coreDataStorage:
+ _objc_msgSend$deletePartitionsBeforeDate:coreDataStorage:
+ _objc_msgSend$deleteStatisticsUsingPredicate:coreDataStorage:
+ _objc_msgSend$descriptor
+ _objc_msgSend$enumerateKeysAndObjectsUsingBlock:
+ _objc_msgSend$groupFromSpecifier:partitionProvider:coreDataStorage:
+ _objc_msgSend$groupSpecifier
+ _objc_msgSend$initWithAccessoryUUID:homeUUID:groupName:
+ _objc_msgSend$initWithCoreDataGroup:partitionProvider:coreDataStorage:
+ _objc_msgSend$initWithDataModelName:atPath:radarInitiator:dateProvider:
+ _objc_msgSend$initWithGroupName:
+ _objc_msgSend$initWithHomeUUID:groupName:
+ _objc_msgSend$initWithMinValue:maxValue:sumOfValues:valueCount:
+ _objc_msgSend$initWithModelName:atPath:radarInitiator:
+ _objc_msgSend$integerValue
+ _objc_msgSend$isEmpty
+ _objc_msgSend$isEqualToAccessoryGroupSpecifier:
+ _objc_msgSend$isEqualToGroupNameSpecifier:
+ _objc_msgSend$isEqualToHomeGroupSpecifier:
+ _objc_msgSend$isEqualToString:
+ _objc_msgSend$isMemberOfClass:
+ _objc_msgSend$loadAllCounterGroups
+ _objc_msgSend$loadAllStatisticsGroups
+ _objc_msgSend$longLongValue
+ _objc_msgSend$longValue
+ _objc_msgSend$notifyObserversForStatistics:previousMax:newMax:
+ _objc_msgSend$numberWithLong:
+ _objc_msgSend$observersForStatistics:
+ _objc_msgSend$removeEphemeralContainer:
+ _objc_msgSend$requestRadarWithMessage:radarTitle:
+ _objc_msgSend$set
+ _objc_msgSend$setAccessoryUUID:
+ _objc_msgSend$setActive:
+ _objc_msgSend$statistics
+ _objc_msgSend$statistics:
+ _objc_msgSend$statisticsGroupForHomeUUID:groupName:
+ _objc_msgSend$statisticsGroupForSpecifier:coreDataGroup:
+ _objc_msgSend$valueForCounter:
+ _objc_retain_x4
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _sharedInstance._hmf_once_t0.1180
+ _sharedInstance._hmf_once_t0.1854
+ _sharedInstance._hmf_once_v1.1182
+ _sharedInstance._hmf_once_v1.1856
- +[HMMHomeGroup(CoreDataProperties) fetchRequest]
- +[HMMNamedGroup(CoreDataProperties) fetchRequest]
- +[HMMNamedGroupCounter(CoreDataProperties) fetchRequest]
- +[HMMNamedGroupValueStatistics(CoreDataProperties) fetchRequest]
- -[HMMCoreDataCounterStorage initWithModelName:atPath:]
- -[HMMCountersManager deleteCountersAfterDate:]
- -[HMMCountersManager deleteCountersBeforeDate:]
- -[HMMCountersManager deleteCountersUsingPredicate:]
- -[HMMCountersManager homeGroups]
- -[HMMCountersManager initWithDataModelName:atPath:]
- -[HMMCountersManager initWithDataModelName:atPath:dateProvider:]
- -[HMMCountersManager namedGroups]
- -[HMMCountersManager primaryStorage]
- -[HMMHomeCounterGroup .cxx_destruct]
- -[HMMHomeCounterGroup coreDataGroupUsingContext:]
- -[HMMHomeCounterGroup coreDataGroup]
- -[HMMHomeCounterGroup homeUUID]
- -[HMMHomeCounterGroup initWithGroupName:homeUUID:partitionProvider:primaryStorage:]
- -[HMMHomeCounterGroup setCoreDataGroup:]
- -[HMMNamedCounterGroup .cxx_destruct]
- -[HMMNamedCounterGroup addObserver:forCounterName:]
- -[HMMNamedCounterGroup coreDataGroupUsingContext:]
- -[HMMNamedCounterGroup coreDataGroup]
- -[HMMNamedCounterGroup countersInDatePartition:]
- -[HMMNamedCounterGroup datePartitions]
- -[HMMNamedCounterGroup groupName]
- -[HMMNamedCounterGroup incrementCounter:]
- -[HMMNamedCounterGroup incrementCounter:by:]
- -[HMMNamedCounterGroup initWithGroupName:partitionProvider:primaryStorage:]
- -[HMMNamedCounterGroup notifyObserversForCounter:previousCount:newCount:]
- -[HMMNamedCounterGroup observersForCounter:]
- -[HMMNamedCounterGroup observers]
- -[HMMNamedCounterGroup partitionProvider]
- -[HMMNamedCounterGroup primaryStorage]
- -[HMMNamedCounterGroup sampleValue:forCounter:]
- -[HMMNamedCounterGroup setCoreDataGroup:]
- -[HMMNamedCounterGroup statisticsForCounter:inDatePartition:minValue:maxValue:average:updateCount:]
- -[HMMNamedCounterGroup sumOfCountersInDatePartition:]
- -[HMMNamedCounterGroup valueForCounter:inDatePartition:]
- GCC_except_table111
- GCC_except_table136
- GCC_except_table140
- GCC_except_table181
- GCC_except_table182
- GCC_except_table194
- GCC_except_table198
- GCC_except_table200
- GCC_except_table204
- GCC_except_table206
- GCC_except_table214
- GCC_except_table215
- GCC_except_table240
- GCC_except_table407
- GCC_except_table408
- _NSInvalidArgumentException
- _OBJC_CLASS_$_HMMHomeCounterGroup
- _OBJC_CLASS_$_HMMHomeGroup
- _OBJC_CLASS_$_HMMNamedCounterGroup
- _OBJC_CLASS_$_HMMNamedGroup
- _OBJC_CLASS_$_HMMNamedGroupCounter
- _OBJC_CLASS_$_HMMNamedGroupValueStatistics
- _OBJC_IVAR_$_HMMCountersManager._homeGroups
- _OBJC_IVAR_$_HMMCountersManager._namedGroups
- _OBJC_IVAR_$_HMMCountersManager._primaryStorage
- _OBJC_IVAR_$_HMMHomeCounterGroup._coreDataGroup
- _OBJC_IVAR_$_HMMHomeCounterGroup._coreDataGroupToken
- _OBJC_IVAR_$_HMMHomeCounterGroup._homeUUID
- _OBJC_IVAR_$_HMMNamedCounterGroup._coreDataGroup
- _OBJC_IVAR_$_HMMNamedCounterGroup._coreDataGroupToken
- _OBJC_IVAR_$_HMMNamedCounterGroup._groupName
- _OBJC_IVAR_$_HMMNamedCounterGroup._lock
- _OBJC_IVAR_$_HMMNamedCounterGroup._observers
- _OBJC_IVAR_$_HMMNamedCounterGroup._partitionProvider
- _OBJC_IVAR_$_HMMNamedCounterGroup._primaryStorage
- _OBJC_METACLASS_$_HMMHomeCounterGroup
- _OBJC_METACLASS_$_HMMHomeGroup
- _OBJC_METACLASS_$_HMMNamedCounterGroup
- _OBJC_METACLASS_$_HMMNamedGroup
- _OBJC_METACLASS_$_HMMNamedGroupCounter
- _OBJC_METACLASS_$_HMMNamedGroupValueStatistics
- __OBJC_$_CLASS_METHODS_HMMHomeGroup(CoreDataProperties)
- __OBJC_$_CLASS_METHODS_HMMNamedGroup(CoreDataProperties)
- __OBJC_$_CLASS_METHODS_HMMNamedGroupCounter(CoreDataProperties)
- __OBJC_$_CLASS_METHODS_HMMNamedGroupValueStatistics(CoreDataProperties)
- __OBJC_$_INSTANCE_METHODS_HMMHomeCounterGroup
- __OBJC_$_INSTANCE_METHODS_HMMNamedCounterGroup
- __OBJC_$_INSTANCE_VARIABLES_HMMHomeCounterGroup
- __OBJC_$_INSTANCE_VARIABLES_HMMNamedCounterGroup
- __OBJC_$_PROP_LIST_HMMHomeCounterGroup
- __OBJC_$_PROP_LIST_HMMNamedCounterGroup
- __OBJC_CLASS_PROTOCOLS_$_HMMNamedCounterGroup
- __OBJC_CLASS_RO_$_HMMHomeCounterGroup
- __OBJC_CLASS_RO_$_HMMHomeGroup
- __OBJC_CLASS_RO_$_HMMNamedCounterGroup
- __OBJC_CLASS_RO_$_HMMNamedGroup
- __OBJC_CLASS_RO_$_HMMNamedGroupCounter
- __OBJC_CLASS_RO_$_HMMNamedGroupValueStatistics
- __OBJC_METACLASS_RO_$_HMMHomeCounterGroup
- __OBJC_METACLASS_RO_$_HMMHomeGroup
- __OBJC_METACLASS_RO_$_HMMNamedCounterGroup
- __OBJC_METACLASS_RO_$_HMMNamedGroup
- __OBJC_METACLASS_RO_$_HMMNamedGroupCounter
- __OBJC_METACLASS_RO_$_HMMNamedGroupValueStatistics
- ___38-[HMMNamedCounterGroup datePartitions]_block_invoke
- ___44-[HMMNamedCounterGroup incrementCounter:by:]_block_invoke
- ___47-[HMMNamedCounterGroup sampleValue:forCounter:]_block_invoke
- ___48-[HMMNamedCounterGroup countersInDatePartition:]_block_invoke
- ___49-[HMMHomeCounterGroup coreDataGroupUsingContext:]_block_invoke
- ___50-[HMMNamedCounterGroup coreDataGroupUsingContext:]_block_invoke
- ___51-[HMMCountersManager deleteCountersUsingPredicate:]_block_invoke
- ___53-[HMMNamedCounterGroup sumOfCountersInDatePartition:]_block_invoke
- ___56-[HMMNamedCounterGroup valueForCounter:inDatePartition:]_block_invoke
- ___99-[HMMNamedCounterGroup statisticsForCounter:inDatePartition:minValue:maxValue:average:updateCount:]_block_invoke
- ___Block_byref_object_copy_.765
- ___Block_byref_object_dispose_.766
- ___block_descriptor_48_e8_32s40s_e32_v16?0"NSManagedObjectContext"8ls32l8s40l8
- ___block_descriptor_96_e8_32s40s48s56r_e32_v16?0"NSManagedObjectContext"8ls32l8s40l8s48l8r56l8
- ___block_literal_global.1099
- ___block_literal_global.1291
- ___block_literal_global.138
- ___block_literal_global.1398
- ___block_literal_global.237
- ___block_literal_global.448
- ___block_literal_global.625
- ___block_literal_global.892
- _logCategory._hmf_once_t1.1290
- _logCategory._hmf_once_v2.1292
- _objc_msgSend$deleteCountersUsingPredicate:
- _objc_msgSend$initWithDataModelName:atPath:dateProvider:
- _objc_msgSend$initWithGroupName:homeUUID:partitionProvider:primaryStorage:
- _objc_msgSend$initWithGroupName:partitionProvider:primaryStorage:
- _objc_msgSend$initWithModelName:atPath:
- _objc_msgSend$primaryStorage
- _objc_msgSend$setCoreDataGroup:
- _sharedInstance._hmf_once_t0.1397
- _sharedInstance._hmf_once_t0.891
- _sharedInstance._hmf_once_v1.1399
- _sharedInstance._hmf_once_v1.893
CStrings:
+ "\x11\x14"
+ "\x16"
+ "%@/%@"
+ "%@/%@/%@"
+ "%{public}@Can't create counter group due to failure to retrieve database group"
+ "%{public}@Ephemeral container already exists: %@"
+ "%{public}@Error deleting statistics where %{public}@: %{public}@"
+ "%{public}@Error getting accessory group %{public}@: %{public}@"
+ "%{public}@Error getting all statistics in group %{public}@ on date %{public}@: %{public}@"
+ "%{public}@Error getting statistics %{public}@ in group %{public}@ on date %{public}@: %{public}@"
+ "%{public}@Error loading all groups: %{public}@"
+ "%{public}@Failed to load persistent store for counters from model %@ at path %@: %@."
+ "%{public}@Unexpected extra accessory groups returned for group %{public}@"
+ "%{public}@Unexpected extra statistics returned for counter %{public}@ in group %{public}@"
+ "%{public}@Unexpected extra statistics returned for statistic %{public}@ in group %{public}@"
+ "(name == %@) && (homeUUID == %@) && (accessoryUUID == %@)"
+ "@\"<HMMRadarInitiating>\""
+ "@\"HMMCoreDataNamedGroup\""
+ "@\"HMMCoreDataNamedGroup\"24@0:8@\"NSManagedObjectContext\"16"
+ "@\"HMMCounterStatistics\"32@0:8@\"NSString\"16@\"NSDate\"24"
+ "@\"HMMCounterStatistics\"32@0:8@\"NSString\"16@\"NSString\"24"
+ "@\"NSDictionary\"24@0:8@\"NSString\"16"
+ "@\"NSMutableSet\""
+ "@24@0:8^{_NSZone=}16"
+ "@48@0:8q16q24q32q40"
+ "AccessoryGroup"
+ "B24@0:8@\"NSString\"16"
+ "Failed to load persistent counter storage; please file a radar"
+ "GroupCounter"
+ "GroupValueStatistics"
+ "HMMAccessoryGroupSpecifier"
+ "HMMCoreDataAccessoryGroup"
+ "HMMCoreDataGroupCounter"
+ "HMMCoreDataGroupValueStatistics"
+ "HMMCoreDataHomeGroup"
+ "HMMCoreDataNamedGroup"
+ "HMMCounterStatistics"
+ "HMMEphemeralCounterContainer"
+ "HMMEphemeralStatisticsContainer"
+ "HMMGroupSpecifier"
+ "HMMHomeGroupSpecifier"
+ "HMMMutableCounterStatistics"
+ "HMMNamedGroupSpecifier"
+ "HMMStandardCounterGroup"
+ "HMMStandardStatisticsGroup"
+ "HMMStatisticsGroup"
+ "NSCopying"
+ "T@\"<HMMGroupSpecifier>\",R,N"
+ "T@\"HMMCoreDataCounterStorage\",R,N,V_coreDataStorage"
+ "T@\"HMMCoreDataNamedGroup\",&,D,N"
+ "T@\"HMMCoreDataNamedGroup\",&,N,V_coreDataGroup"
+ "T@\"HMMCounterStatistics\",R,C,N"
+ "T@\"NSArray\",R,C,N"
+ "T@\"NSDictionary\",R,C,N"
+ "T@\"NSMutableDictionary\",R,N,V_counterGroups"
+ "T@\"NSMutableDictionary\",R,N,V_ephemeralContainers"
+ "T@\"NSMutableDictionary\",R,N,V_statisticsGroups"
+ "T@\"NSUUID\",R,N,V_accessoryUUID"
+ "TB,N,GisActive,V_active"
+ "TB,R,N"
+ "TTR: Failed to load persistent counter storage"
+ "Tq,R,N"
+ "Tq,R,N,V_maxValue"
+ "Tq,R,N,V_minValue"
+ "Tq,R,N,V_valueCount"
+ "_accessoryUUID"
+ "_coreDataStorage"
+ "_counterGroups"
+ "_counters"
+ "_ephemeralContainerNames"
+ "_ephemeralContainers"
+ "_maxValue"
+ "_minValue"
+ "_radarInitiator"
+ "_statistics"
+ "_statisticsGroups"
+ "_sumOfValues"
+ "_valueCount"
+ "accessoryGroup"
+ "accessoryGroup: %@/%@/%@"
+ "accessoryUUID"
+ "activeEphemeralContainers"
+ "addEphemeralContainer:"
+ "addMaxValueObserver:forStatistics:"
+ "addObserver:forCounter:"
+ "addValue:"
+ "addValue:toStatistics:"
+ "allKeys"
+ "averageValue"
+ "copyWithZone:"
+ "coreDataStorage"
+ "counterGroupForAccessoryUUID:homeUUID:groupName:"
+ "counterGroupForSpecifier:coreDataGroup:"
+ "counterGroups"
+ "counterStatistics"
+ "counters.@count > 0"
+ "countersInEphemeralContainer:"
+ "deactivateEphemeralContainer:"
+ "deleteCountersUsingPredicate:coreDataStorage:"
+ "deletePartitionsAfterDate:"
+ "deletePartitionsAfterDate:coreDataStorage:"
+ "deletePartitionsBeforeDate:"
+ "deletePartitionsBeforeDate:coreDataStorage:"
+ "deleteStatisticsUsingPredicate:coreDataStorage:"
+ "descriptor"
+ "descriptorTypeNamePrefix"
+ "enumerateCounterGroupsUsingBlock:"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "enumerateStatisticsGroupsUsingBlock:"
+ "ephemeralContainerNames"
+ "ephemeralContainers"
+ "groupDescriptor"
+ "groupFromSpecifier:partitionProvider:coreDataStorage:"
+ "groupSpecifier"
+ "homeGroup"
+ "homeGroup: %@/%@"
+ "initWithAccessoryUUID:homeUUID:groupName:"
+ "initWithCoreDataGroup:partitionProvider:coreDataStorage:"
+ "initWithDataModelName:atPath:radarInitiator:"
+ "initWithDataModelName:atPath:radarInitiator:dateProvider:"
+ "initWithGroupName:"
+ "initWithHomeUUID:groupName:"
+ "initWithMinValue:maxValue:sumOfValues:valueCount:"
+ "initWithModelName:atPath:radarInitiator:"
+ "integerValue"
+ "isEmpty"
+ "isEqualToAccessoryGroupSpecifier:"
+ "isEqualToGroupNameSpecifier:"
+ "isEqualToHomeGroupSpecifier:"
+ "isEqualToString:"
+ "loadAllCounterGroups"
+ "loadAllStatisticsGroups"
+ "longLongValue"
+ "longValue"
+ "maxValue"
+ "minValue"
+ "namedGroup"
+ "namedGroup: %@"
+ "notifyObserversForStatistics:previousMax:newMax:"
+ "numberWithLong:"
+ "observersForStatistics:"
+ "q24@0:8@\"NSString\"16"
+ "q32@0:8@\"NSString\"16@\"NSString\"24"
+ "removeEphemeralContainer:"
+ "requestRadarWithMessage:radarTitle:"
+ "set"
+ "setAccessoryUUID:"
+ "setActive:"
+ "statistics"
+ "statistics:"
+ "statistics:inDatePartition:"
+ "statistics:inEphemeralContainer:"
+ "statisticsGroupForAccessoryUUID:homeUUID:groupName:"
+ "statisticsGroupForHomeUUID:groupName:"
+ "statisticsGroupForHomeUUIDFromLogEvent:groupName:"
+ "statisticsGroupForName:"
+ "statisticsGroupForSpecifier:coreDataGroup:"
+ "statisticsGroups"
+ "statisticsInDatePartition:"
+ "statisticsInEphemeralContainer:"
+ "sumOfCountersInEphemeralContainer:"
+ "v32@?0@\"<HMMGroupSpecifier>\"8@\"<HMMCounterGroup>\"16^B24"
+ "v32@?0@\"<HMMGroupSpecifier>\"8@\"<HMMStatisticsGroup>\"16^B24"
+ "v32@?0@\"NSString\"8@\"HMMMutableCounterStatistics\"16^B24"
+ "valueCount"
+ "valueForCounter:"
+ "valueForCounter:inEphemeralContainer:"
+ "valueStatistics.@count > 0"
- "\x11\x13"
- "\x15"
- "%{public}@Trying to get statistics for counter %{public}@ in group %{public}@ when it's not sampled"
- "@\"HMMHomeGroup\""
- "@\"HMMNamedGroup\""
- "B64@0:8@\"NSString\"16@\"NSDate\"24^q32^q40^q48^q56"
- "B64@0:8@16@24^q32^q40^q48^q56"
- "Can't load persistent store for counters from model %@ at path %@"
- "HMMHomeCounterGroup"
- "HMMHomeGroup"
- "HMMNamedCounterGroup"
- "HMMNamedGroup"
- "HMMNamedGroupCounter"
- "HMMNamedGroupValueStatistics"
- "NamedGroupCounter"
- "NamedGroupValueStatistics"
- "T@\"HMMCoreDataCounterStorage\",R,N,V_primaryStorage"
- "T@\"HMMHomeGroup\",&,N,V_coreDataGroup"
- "T@\"HMMNamedGroup\",&,D,N"
- "T@\"HMMNamedGroup\",&,N,V_coreDataGroup"
- "T@\"NSMutableDictionary\",R,N,V_homeGroups"
- "T@\"NSMutableDictionary\",R,N,V_namedGroups"
- "T@\"NSPersistentContainer\",R,N"
- "_homeGroups"
- "_namedGroups"
- "_primaryStorage"
- "addObserver:forCounterName:"
- "deleteCountersAfterDate:"
- "deleteCountersBeforeDate:"
- "deleteCountersUsingPredicate:"
- "homeGroups"
- "initWithDataModelName:atPath:"
- "initWithDataModelName:atPath:dateProvider:"
- "initWithGroupName:homeUUID:partitionProvider:primaryStorage:"
- "initWithGroupName:partitionProvider:primaryStorage:"
- "initWithModelName:atPath:"
- "namedGroups"
- "primaryStorage"
- "sampleValue:forCounter:"
- "statisticsForCounter:inDatePartition:minValue:maxValue:average:updateCount:"

```
