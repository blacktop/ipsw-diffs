## AppleMediaServices

> `/System/Library/PrivateFrameworks/AppleMediaServices.framework/Versions/A/AppleMediaServices`

```diff

-8.4.25.1.2
-  __TEXT.__text: 0x8672ec
-  __TEXT.__auth_stubs: 0x4490
-  __TEXT.__objc_methlist: 0x1ffb4
-  __TEXT.__const: 0xb52b3
+8.5.2.1.1
+  __TEXT.__text: 0x869cec
+  __TEXT.__auth_stubs: 0x44a0
+  __TEXT.__objc_methlist: 0x20124
+  __TEXT.__const: 0xb5423
   __TEXT.__dlopen_cstrs: 0x705
-  __TEXT.__cstring: 0x28041
-  __TEXT.__swift5_typeref: 0x38d9
-  __TEXT.__swift5_reflstr: 0x1b28
+  __TEXT.__cstring: 0x285a1
+  __TEXT.__swift5_typeref: 0x3a09
+  __TEXT.__swift5_reflstr: 0x1b98
   __TEXT.__swift5_assocty: 0x8e8
-  __TEXT.__constg_swiftt: 0x2610
+  __TEXT.__constg_swiftt: 0x272c
   __TEXT.__swift5_builtin: 0x1cc
-  __TEXT.__swift5_fieldmd: 0x218c
+  __TEXT.__swift5_fieldmd: 0x2238
   __TEXT.__swift5_proto: 0x5e8
-  __TEXT.__swift5_types: 0x2c0
+  __TEXT.__swift5_types: 0x2d4
   __TEXT.__swift_as_entry: 0x400
   __TEXT.__swift_as_ret: 0x41c
   __TEXT.__swift5_capture: 0x1b04
   __TEXT.__swift5_mpenum: 0x48
   __TEXT.__swift5_protos: 0x7c
-  __TEXT.__oslogstring: 0x2b3d9
+  __TEXT.__oslogstring: 0x2b424
   __TEXT.__gcc_except_tab: 0x1684c
   __TEXT.__ustring: 0x210
-  __TEXT.__unwind_info: 0x10d90
+  __TEXT.__unwind_info: 0x10e48
   __TEXT.__eh_frame: 0xa604
   __TEXT.__objc_classname: 0x3b6f
-  __TEXT.__objc_methname: 0x3f66f
+  __TEXT.__objc_methname: 0x3f787
   __TEXT.__objc_methtype: 0x7268
-  __TEXT.__objc_stubs: 0x2ba20
+  __TEXT.__objc_stubs: 0x2ba80
   __DATA_CONST.__got: 0x1758
-  __DATA_CONST.__const: 0x55f8
-  __DATA_CONST.__objc_classlist: 0x1238
+  __DATA_CONST.__const: 0x5608
+  __DATA_CONST.__objc_classlist: 0x1260
   __DATA_CONST.__objc_catlist: 0xf8
-  __DATA_CONST.__objc_protolist: 0x368
+  __DATA_CONST.__objc_protolist: 0x378
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe260
-  __DATA_CONST.__objc_protorefs: 0x198
+  __DATA_CONST.__objc_selrefs: 0xe2a8
+  __DATA_CONST.__objc_protorefs: 0x1a8
   __DATA_CONST.__objc_superrefs: 0xc38
-  __DATA_CONST.__objc_arraydata: 0x3b8
-  __AUTH_CONST.__auth_got: 0x2260
-  __AUTH_CONST.__auth_ptr: 0xa00
-  __AUTH_CONST.__const: 0x3db80
-  __AUTH_CONST.__cfstring: 0x208e0
-  __AUTH_CONST.__objc_const: 0x36dc0
+  __DATA_CONST.__objc_arraydata: 0x390
+  __AUTH_CONST.__auth_got: 0x2268
+  __AUTH_CONST.__auth_ptr: 0xa10
+  __AUTH_CONST.__const: 0x3dc30
+  __AUTH_CONST.__cfstring: 0x207e0
+  __AUTH_CONST.__objc_const: 0x37150
   __AUTH_CONST.__objc_intobj: 0xc30
-  __AUTH_CONST.__objc_arrayobj: 0x108
+  __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x78
-  __AUTH.__objc_data: 0x6880
-  __AUTH.__data: 0x1ae8
+  __AUTH.__objc_data: 0x6c38
+  __AUTH.__data: 0x1ba8
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x8
-  __DATA.__objc_ivar: 0x1dd0
-  __DATA.__data: 0x61e0
-  __DATA.__bss: 0xc1c8
+  __DATA.__objc_ivar: 0x1dd4
+  __DATA.__data: 0x6230
+  __DATA.__bss: 0xc1f8
   __DATA.__common: 0x1570
   __DATA_DIRTY.__objc_data: 0x5d70
   __DATA_DIRTY.__data: 0x70

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 21750
-  Symbols:   36031
-  CStrings:  19923
+  Functions: 21857
+  Symbols:   36126
+  CStrings:  19965
 
Symbols:
+ +[AMSMetrics _detectAnomaliesForMetricsEvent:]
+ +[AMSMetrics _makeMetricsEventAnomaliesDetector]
+ -[AMSEngagementEnqueueRequest processIdentifier]
+ -[AMSEngagementEnqueueRequest setProcessIdentifier:]
+ OBJC_IVAR_$_AMSEngagementEnqueueRequest._processIdentifier
+ _OBJC_CLASS_$_AMSDefaultsIdentifierHistoryProvider
+ _OBJC_CLASS_$_AMSDeviceGeneratedIdentifierAnomalyDetector
+ _OBJC_CLASS_$_AMSExperimentDataAnomalyDetector
+ _OBJC_CLASS_$_AMSMetricsEventAnomaliesDetector
+ _OBJC_CLASS_$_AMSMetricsEventAnomaly
+ _OBJC_METACLASS_$_AMSDefaultsIdentifierHistoryProvider
+ _OBJC_METACLASS_$_AMSDeviceGeneratedIdentifierAnomalyDetector
+ _OBJC_METACLASS_$_AMSExperimentDataAnomalyDetector
+ _OBJC_METACLASS_$_AMSMetricsEventAnomaliesDetector
+ _OBJC_METACLASS_$_AMSMetricsEventAnomaly
+ __36-[AMSMetrics _processOperationQueue]_block_invoke.81
+ __36-[AMSMetrics _processOperationQueue]_block_invoke.88
+ __36-[AMSMetrics _processOperationQueue]_block_invoke_2.82
+ __42-[AMSMetricsDatabase _performTransaction:]_block_invoke.234
+ __44-[AMSMetrics _handleFlushIntervalWithStyle:]_block_invoke.99
+ __50-[AMSMetrics _beginFlushIntervalWithStyle:events:]_block_invoke.93
+ __50-[AMSMetrics _beginFlushIntervalWithStyle:events:]_block_invoke.95
+ __97-[AMSPurchaseTask _recordEngagementEventWithInfo:responseDictionary:finalizedBlindedItems:error:]_block_invoke.111
+ __97-[AMSPurchaseTask _recordEngagementEventWithInfo:responseDictionary:finalizedBlindedItems:error:]_block_invoke.117
+ __97-[AMSPurchaseTask _recordEngagementEventWithInfo:responseDictionary:finalizedBlindedItems:error:]_block_invoke.126
+ __97-[AMSPurchaseTask _recordEngagementEventWithInfo:responseDictionary:finalizedBlindedItems:error:]_block_invoke.134
+ __DATA_AMSDefaultsIdentifierHistoryProvider
+ __DATA_AMSDeviceGeneratedIdentifierAnomalyDetector
+ __DATA_AMSExperimentDataAnomalyDetector
+ __DATA_AMSMetricsEventAnomaliesDetector
+ __DATA_AMSMetricsEventAnomaly
+ __INSTANCE_METHODS_AMSMetricsEventAnomaliesDetector
+ __INSTANCE_METHODS_AMSMetricsEventAnomaly
+ __IVARS_AMSDeviceGeneratedIdentifierAnomalyDetector
+ __IVARS_AMSMetricsEventAnomaliesDetector
+ __IVARS_AMSMetricsEventAnomaly
+ __METACLASS_DATA_AMSDefaultsIdentifierHistoryProvider
+ __METACLASS_DATA_AMSDeviceGeneratedIdentifierAnomalyDetector
+ __METACLASS_DATA_AMSExperimentDataAnomalyDetector
+ __METACLASS_DATA_AMSMetricsEventAnomaliesDetector
+ __METACLASS_DATA_AMSMetricsEventAnomaly
+ __OBJC_$_INSTANCE_METHODS_AMSDefaultsIdentifierHistoryProvider(AppleMediaServices)
+ __OBJC_$_INSTANCE_METHODS_AMSDeviceGeneratedIdentifierAnomalyDetector(AppleMediaServices)
+ __OBJC_$_INSTANCE_METHODS_AMSExperimentDataAnomalyDetector(AppleMediaServices)
+ __OBJC_CLASS_PROTOCOLS_$_AMSDefaultsIdentifierHistoryProvider(AppleMediaServices)
+ __OBJC_CLASS_PROTOCOLS_$_AMSDeviceGeneratedIdentifierAnomalyDetector(AppleMediaServices)
+ __OBJC_CLASS_PROTOCOLS_$_AMSExperimentDataAnomalyDetector(AppleMediaServices)
+ __PROPERTIES_AMSMetricsEventAnomaly
+ __PROTOCOL_AMSDeviceGeneratedIdentifierHistoryProvider
+ __PROTOCOL_AMSMetricsEventAnomalyDetector
+ __PROTOCOL_INSTANCE_METHODS_AMSDeviceGeneratedIdentifierHistoryProvider
+ __PROTOCOL_INSTANCE_METHODS_AMSMetricsEventAnomalyDetector
+ __PROTOCOL_METHOD_TYPES_AMSDeviceGeneratedIdentifierHistoryProvider
+ __PROTOCOL_METHOD_TYPES_AMSMetricsEventAnomalyDetector
+ ___46+[AMSMetrics _detectAnomaliesForMetricsEvent:]_block_invoke
+ ___46+[AMSMetrics _detectAnomaliesForMetricsEvent:]_block_invoke_2
+ ___46+[AMSMetrics _detectAnomaliesForMetricsEvent:]_block_invoke_3
+ ___46+[AMSMetrics _detectAnomaliesForMetricsEvent:]_block_invoke_4
+ __block_literal_global.62
+ __block_literal_global.74
+ _flat unique So30AMSMetricsEventAnomalyDetector_p
+ _flat unique So43AMSDeviceGeneratedIdentifierHistoryProvider_p
+ _objc_msgSend$_detectAnomaliesForMetricsEvent:
+ _objc_msgSend$_makeMetricsEventAnomaliesDetector
+ _objc_msgSend$details
+ _objc_msgSend$detectAnomaliesForMetricsEvent:
+ _objc_msgSend$initWithAnomalyDetectors:
+ _objc_msgSend$setProcessIdentifier:
+ _symbolic $s18AppleMediaServices27MetricsEventAnomalyDetectorP
+ _symbolic $s18AppleMediaServices40DeviceGeneratedIdentifierHistoryProviderP
+ _symbolic Say______pG 18AppleMediaServices27MetricsEventAnomalyDetectorP
+ _symbolic _____ 18AppleMediaServices19MetricsEventAnomalyC
+ _symbolic _____ 18AppleMediaServices29ExperimentDataAnomalyDetectorC
+ _symbolic _____ 18AppleMediaServices29MetricsEventAnomaliesDetectorC
+ _symbolic _____ 18AppleMediaServices33DefaultsIdentifierHistoryProviderC
+ _symbolic _____ 18AppleMediaServices40DeviceGeneratedIdentifierAnomalyDetectorC
+ _symbolic ______p 18AppleMediaServices27MetricsEventAnomalyDetectorP
+ _symbolic ______p 18AppleMediaServices40DeviceGeneratedIdentifierHistoryProviderP
+ _symbolic _____ySSSDy_____ypGG s17_NativeDictionaryV s11AnyHashableV
+ _symbolic _____y_____ypG s17_NativeDictionaryV s11AnyHashableV
- -[AMSMetrics _showTTRWithEvent:]
- __36-[AMSMetrics _processOperationQueue]_block_invoke.66
- __36-[AMSMetrics _processOperationQueue]_block_invoke.73
- __36-[AMSMetrics _processOperationQueue]_block_invoke_2.67
- __42-[AMSMetricsDatabase _performTransaction:]_block_invoke.235
- __44-[AMSMetrics _handleFlushIntervalWithStyle:]_block_invoke.84
- __50-[AMSMetrics _beginFlushIntervalWithStyle:events:]_block_invoke.78
- __50-[AMSMetrics _beginFlushIntervalWithStyle:events:]_block_invoke.80
- __97-[AMSPurchaseTask _recordEngagementEventWithInfo:responseDictionary:finalizedBlindedItems:error:]_block_invoke.110
- __97-[AMSPurchaseTask _recordEngagementEventWithInfo:responseDictionary:finalizedBlindedItems:error:]_block_invoke.115
- __97-[AMSPurchaseTask _recordEngagementEventWithInfo:responseDictionary:finalizedBlindedItems:error:]_block_invoke.125
- __97-[AMSPurchaseTask _recordEngagementEventWithInfo:responseDictionary:finalizedBlindedItems:error:]_block_invoke.133
- __block_literal_global.95
- _objc_msgSend$eventTime
- _objc_msgSend$setTtrMetricsClickStreamUserIdHistory:
- _objc_msgSend$ttrMetricsClickStreamUserIdHistory
CStrings:
+ "%@ in %@: %@ container is corrupt"
+ "%{public}@ [%{public}@] Metrics event anomaly detected: %{public}@"
+ "%{public}@: Database locked or busy: sqlResult=%d"
+ ", \nCurrent userId: "
+ ", \nLast userId: "
+ ", \nMetrics event: "
+ ", \nProduct page optimization areaId: "
+ "@\"AMSMetricsEventAnomaly\"24@0:8@\"AMSMetricsEvent\"16"
+ "A device-generated identifier (aka. a KID) of 24 characters in length was detected in App Store clickstream data in the `userId` field, following a CID identifier of 35 characters in length for the same `clientId` value. It appears that the `userId` has unexpectedly flipped. \nLogKey: "
+ "A different `userId` was detected in `"
+ "AMSDefaultsIdentifierHistoryProvider"
+ "AMSDeviceGeneratedIdentifierAnomalyDetector"
+ "AMSDeviceGeneratedIdentifierHistoryProvider"
+ "AMSExperimentDataAnomalyDetector"
+ "AMSMetricsEventAnomaliesDetector"
+ "AMSMetricsEventAnomaly"
+ "AMSMetricsEventAnomalyDetector"
+ "App Store clickstream event is missing a treatment for product page optimization area \nLogKey: "
+ "AppleMediaServices.DeviceGeneratedIdentifierAnomalyDetector"
+ "AppleMediaServices.MetricsEventAnomaliesDetector"
+ "AppleMediaServices.MetricsEventAnomaly"
+ "Device-generated KID flip-flop detected in App Store clickstream"
+ "Missing product page optimization treatment"
+ "PSD2_AMS_RESUME_3D_STEP_UP_COMPLETED_%@_%d"
+ "PSD2_AMS_RESUME_3D_STEP_UP_COMPLETED_SUCCESS"
+ "Ti,V_processIdentifier"
+ "Unexpected userId change detected in `"
+ "[%@] %@"
+ "[AMS] Fault Detected"
+ "_detectAnomaliesForMetricsEvent:"
+ "_makeMetricsEventAnomaliesDetector"
+ "_processIdentifier"
+ "` clickstream data in the `userId` field, following multiple earlier `userId` values for the same `clientId`. It appears that the `userId` has unexpectedly flipped more than once, since `"
+ "` userIds should not rotate for a given clientId. One rotation can occur due to initial conflict resolution, but not multiple. \nLogKey: "
+ "anomalyDetectors"
+ "com.apple.AppleMediaServices.KIDFlipFlopAnomalyIdentifier"
+ "com.apple.AppleMediaServices.MetricsEventAnomaliesDetection"
+ "com.apple.AppleMediaServices.MissingProductPageOptimizationTreatmentAnomalyIdentifier"
+ "com.apple.AppleMediaServices.UnexpectedUserIdChangeAnomalyIdentifier"
+ "descriptionOverride"
+ "detectAnomaliesForMetricsEvent:"
+ "detectAnomalyFor:"
+ "identifierHistoryFor:"
+ "identifierHistoryProvider"
+ "initWithAnomalyDetectors:"
+ "initWithIdentifierHistoryProvider:"
+ "seed"
+ "setIdentifierHistory:for:"
+ "setProcessIdentifier:"
- "%{public}@ [%{public}@] Error: %{public}@"
- "<private>"
- "A device-generated identifier (aka. a KID) of 24 characters in length was detected in App Store clickstream data in the `userId` field, following a CID identifier of 35 characters in length for the same `clientId` value. It appears that the `userId` has unexpectedly flipped. \nLogKey: %@, \nCurrent userId: %@, \nLast userId: %@, \neventTime: %@"
- "A different `userId` was detected in `%@` clickstream data in the `userId` field, following multiple earlier `userId` values for the same `clientId`. It appears that the `userId` has unexpectedly flipped more than once, since `%@` userIds should not rotate for a given clientId. One rotation can occur due to initial conflict resolution, but not multiple. \nLogKey: %@, \nCurrent userId: %@, \nLast userId: %@, \neventTime: %@"
- "[%@] %@ in %@: %@ container is corrupt"
- "[%@] Device-generated KID flip-flop detected in App Store clickstream"
- "[%@] Unexpected userId change detected in `%@` clickstream"
- "[AMS] Fatal Error Detected"
- "_showTTRWithEvent:"
- "userIds"

```
