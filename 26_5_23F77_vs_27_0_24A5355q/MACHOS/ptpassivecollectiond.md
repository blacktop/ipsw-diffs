## ptpassivecollectiond

> `/usr/libexec/ptpassivecollectiond`

```diff

-250.2.0.0.0
-  __TEXT.__text: 0x12d60
-  __TEXT.__auth_stubs: 0xb40
-  __TEXT.__objc_stubs: 0x1b60
-  __TEXT.__objc_methlist: 0xd70
-  __TEXT.__const: 0x16a
-  __TEXT.__gcc_except_tab: 0x3a4
-  __TEXT.__cstring: 0x1207
-  __TEXT.__oslogstring: 0x1de9
+262.0.0.0.0
+  __TEXT.__text: 0x11f30
+  __TEXT.__auth_stubs: 0xc00
+  __TEXT.__objc_stubs: 0x19a0
+  __TEXT.__objc_methlist: 0xbfc
+  __TEXT.__const: 0x162
+  __TEXT.__gcc_except_tab: 0x408
+  __TEXT.__cstring: 0x1557
+  __TEXT.__oslogstring: 0x1fd9
   __TEXT.__dlopen_cstrs: 0x59
-  __TEXT.__objc_methname: 0x2560
-  __TEXT.__objc_classname: 0x1ac
-  __TEXT.__objc_methtype: 0x62e
-  __TEXT.__swift5_typeref: 0xa5
+  __TEXT.__objc_methname: 0x2180
+  __TEXT.__objc_classname: 0x1bc
+  __TEXT.__objc_methtype: 0x65e
+  __TEXT.__swift5_typeref: 0x95
   __TEXT.__constg_swiftt: 0xb0
   __TEXT.__swift5_reflstr: 0x27
   __TEXT.__swift5_fieldmd: 0x44
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x558
+  __TEXT.__unwind_info: 0x4c0
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0x5b0
-  __DATA_CONST.__got: 0x128
-  __DATA_CONST.__auth_ptr: 0x48
-  __DATA_CONST.__const: 0x610
-  __DATA_CONST.__cfstring: 0xd60
-  __DATA_CONST.__objc_classlist: 0x38
+  __DATA_CONST.__const: 0x6f8
+  __DATA_CONST.__cfstring: 0x1020
+  __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA.__objc_const: 0xd68
-  __DATA.__objc_selrefs: 0x918
-  __DATA.__objc_ivar: 0x5c
-  __DATA.__objc_data: 0x270
-  __DATA.__data: 0x308
-  __DATA.__bss: 0x1b8
+  __DATA_CONST.__objc_arraydata: 0x48
+  __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__auth_got: 0x610
+  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__auth_ptr: 0x48
+  __DATA.__objc_const: 0xd20
+  __DATA.__objc_selrefs: 0x8c0
+  __DATA.__objc_ivar: 0x48
+  __DATA.__objc_data: 0x2c0
+  __DATA.__data: 0x368
+  __DATA.__bss: 0x1c8
   __DATA.__common: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: E9970728-FE54-3F16-94CD-07BDDA249275
-  Functions: 414
-  Symbols:   249
-  CStrings:  871
+  UUID: 28A7B326-23CD-383E-B1E8-CFED2E63A51A
+  Functions: 379
+  Symbols:   263
+  CStrings:  909
 
Symbols:
+ _$sSD10FoundationE36_unconditionallyBridgeFromObjectiveCySDyxq_GSo12NSDictionaryCSgFZ
+ _$sSSSHsWP
+ _OBJC_CLASS_$_NSConstantArray
+ _objc_claimAutoreleasedReturnValue
+ _objc_opt_new
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x8
+ _objc_setProperty_nonatomic_copy
+ _swift_bridgeObjectRetain_n
+ _swift_getObjCClassMetadata
+ _swift_release_x19
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x8
+ _swift_retain_x21
- _$ss10_HashTableV12previousHole6beforeAB6BucketVAF_tF
- _$ss18_DictionaryStorageC8allocate8capacityAByxq_GSi_tFZ
- _objc_retain_x28
- _swift_retain
CStrings:
+ "'dataCategories' must be an array"
+ "'dataCategories' must contain only strings"
+ "'options' keys must be strings"
+ "'options' must be a dictionary"
+ "'options' value for key '%@' must be an array"
+ "'options' value for key '%@' must contain only strings"
+ "@\"NSArray\""
+ "@24@0:8^{_NSZone=}16"
+ "Collection configuration dictionary must not be nil"
+ "Collection configuration is unavailable"
+ "Collection configuration keys must be non-empty strings"
+ "Collection configuration must contain at least one data source"
+ "Collection configuration name %@:\nCollection configuration: %@\nCollect MSS: %@\nCollect App InFocus: %@\nCollect PerfPowerMetrics (Logging): %@\nCollect Hangs (Logging): %@\nCollect User Interaction (Logging): %@\nCollect Metal FramePacing (Logging): %@\nCollect Scrolling (Logging): %@\nCollect AppLaunch (Logging): %@\nLogging data categories: %@"
+ "Collection configuration value for key '%@' must be a PTPCDataSourceConfig"
+ "CollectionConfigClearFailed"
+ "CollectionConfigMigrationPersistFailed"
+ "CollectionConfigParseError"
+ "CollectionConfigPersistFailed"
+ "CollectionConfigReset"
+ "CollectionConfigUpdated"
+ "Data source configuration dictionary must not be nil"
+ "DataCategories"
+ "Failed to clear corrupted collection configuration: %{public}@"
+ "Failed to parse persisted collection configuration, clearing corrupted data: %{public}@"
+ "Failed to persist collection configuration: %{public}@"
+ "Failed to persist migrated legacy collection configuration: %{public}@"
+ "Invalid configuration for data source '%@': %@"
+ "Logging"
+ "MetricKit"
+ "Microstackshot"
+ "NSCopying"
+ "Non-string key in collection configuration dictionary"
+ "Options"
+ "PTPCDataSourceConfig"
+ "PointsOfInterest"
+ "StateReporting"
+ "T@\"NSArray\",C,N,V_dataCategories"
+ "T@\"NSDictionary\",C,N,V_options"
+ "T@\"NSDictionary\",R,N,V_collectionConfiguration"
+ "TB,D,N"
+ "Updated collection configuration: %{public}@"
+ "Value for data source '%@' must be a dictionary"
+ "_collectionConfiguration"
+ "_dataCategories"
+ "_options"
+ "arrayByAddingObject:"
+ "collectLoggingMetricKit"
+ "collectLoggingPointsOfInterest"
+ "collectLoggingStateReporting"
+ "collectionConfiguration"
+ "configFromDictionary:errorOut:"
+ "containsObject:"
+ "copy"
+ "copyWithZone:"
+ "dataCategories"
+ "dictionaryRepresentation"
+ "getCollectionConfiguration:"
+ "hasAnyKey:"
+ "includesDataSource:dataCategory:"
+ "initWithCapacity:"
+ "initWithDataCategories:options:errorOut:"
+ "initWithName:collectionConfiguration:"
+ "length"
+ "options"
+ "removeObject:"
+ "resetCollectionConfiguration"
+ "resetCollectionConfiguration:"
+ "setCollectLoggingMetricKit:"
+ "setCollectLoggingPointsOfInterest:"
+ "setCollectLoggingStateReporting:"
+ "setCollectionConfiguration:callback:"
+ "setDataCategories:"
+ "setInclude:dataSource:dataCategory:"
+ "setOptions:"
+ "updateCollectionConfiguration:"
+ "v24@0:8@?<v@?@\"NSDictionary\"@\"NSError\">16"
+ "v32@0:8@\"NSDictionary\"16@?<v@?@\"NSError\">24"
+ "v36@0:8B16@20@28"
- "@56@0:8@16B24B28B32B36B40B44B48B52"
- "Collection configuration name %@:\nCollect MSS: %@\nCollect App InFocus: %@\nCollect PerfPowerMetrics (Logging): %@\nCollect Hangs (Logging): %@\nCollect User Interaction (Logging): %@\nCollect Metal FramePacing (Logging): %@\nCollect Scrolling (Logging): %@\nCollect AppLaunch (Logging): %@\nLogging data categories: %@"
- "TB,N"
- "TB,R,N,V_collectAppInFocus"
- "TB,R,N,V_collectLoggingAppLaunch"
- "TB,R,N,V_collectLoggingHangs"
- "TB,R,N,V_collectLoggingMetalFramePacing"
- "TB,R,N,V_collectLoggingPerfPowerMetrics"
- "TB,R,N,V_collectLoggingScrolling"
- "TB,R,N,V_collectLoggingUserInteraction"
- "TB,R,N,V_collectMSS"
- "_collectAppInFocus"
- "_collectLoggingAppLaunch"
- "_collectLoggingHangs"
- "_collectLoggingMetalFramePacing"
- "_collectLoggingPerfPowerMetrics"
- "_collectLoggingScrolling"
- "_collectLoggingUserInteraction"
- "_collectMSS"
- "collectAppInFocusNum"
- "collectLoggingAppLaunchNum"
- "collectLoggingHangsNum"
- "collectLoggingMetalFramePacingNum"
- "collectLoggingPerfPowerMetricsNum"
- "collectLoggingScrollingNum"
- "collectLoggingUserInteractionNum"
- "collectMSSNum"
- "initWithName:collectMSS:collectAppInFocus:collectLoggingPerfPowerMetrics:collectLoggingHangs:collectLoggingUserInteraction:collectLoggingMetalFramePacing:collectLoggingScrolling:collectLoggingAppLaunch:"
- "resetCollectAppInFocus"
- "resetCollectAppInFocus:"
- "resetCollectLoggingAppLaunch"
- "resetCollectLoggingAppLaunch:"
- "resetCollectLoggingHangs"
- "resetCollectLoggingHangs:"
- "resetCollectLoggingMetalFramePacing"
- "resetCollectLoggingMetalFramePacing:"
- "resetCollectLoggingPerfPowerMetrics"
- "resetCollectLoggingPerfPowerMetrics:"
- "resetCollectLoggingScrolling"
- "resetCollectLoggingScrolling:"
- "resetCollectLoggingUserInteraction"
- "resetCollectLoggingUserInteraction:"
- "resetCollectMSS"
- "resetCollectMSS:"
- "setCollectAppInFocus:callback:"
- "setCollectAppInFocusNum:"
- "setCollectLoggingAppLaunch:callback:"
- "setCollectLoggingAppLaunchNum:"
- "setCollectLoggingHangs:callback:"
- "setCollectLoggingHangsNum:"
- "setCollectLoggingMetalFramePacing:callback:"
- "setCollectLoggingMetalFramePacingNum:"
- "setCollectLoggingPerfPowerMetrics:callback:"
- "setCollectLoggingPerfPowerMetricsNum:"
- "setCollectLoggingScrolling:callback:"
- "setCollectLoggingScrollingNum:"
- "setCollectLoggingUserInteraction:callback:"
- "setCollectLoggingUserInteractionNum:"
- "setCollectMSS:callback:"
- "setCollectMSSNum:"
- "v28@0:8B16@?20"
- "v28@0:8B16@?<v@?@\"NSError\">20"

```
