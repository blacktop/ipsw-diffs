## MatterPlugin

> `/System/Library/PrivateFrameworks/MatterPlugin.framework/MatterPlugin`

```diff

-28.4.2.0.0
-  __TEXT.__text: 0x38080
-  __TEXT.__auth_stubs: 0x6a0
-  __TEXT.__objc_methlist: 0x3718
-  __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0xac0
-  __TEXT.__oslogstring: 0x41e8
-  __TEXT.__gcc_except_tab: 0x1c80
-  __TEXT.__unwind_info: 0xf38
-  __TEXT.__objc_classname: 0x7c4
-  __TEXT.__objc_methname: 0x5fff
-  __TEXT.__objc_methtype: 0x12bb
-  __TEXT.__objc_stubs: 0x4bc0
-  __DATA_CONST.__got: 0x358
-  __DATA_CONST.__const: 0x740
-  __DATA_CONST.__objc_classlist: 0x1c0
-  __DATA_CONST.__objc_protolist: 0x68
+49.0.0.0.0
+  __TEXT.__text: 0x3e4d8
+  __TEXT.__auth_stubs: 0x7a0
+  __TEXT.__objc_methlist: 0x40ec
+  __TEXT.__const: 0xd8
+  __TEXT.__cstring: 0x1091
+  __TEXT.__oslogstring: 0x49da
+  __TEXT.__gcc_except_tab: 0x19e8
+  __TEXT.__unwind_info: 0xfa8
+  __TEXT.__objc_classname: 0x909
+  __TEXT.__objc_methname: 0x6c1e
+  __TEXT.__objc_methtype: 0x1445
+  __TEXT.__objc_stubs: 0x5360
+  __DATA_CONST.__got: 0x478
+  __DATA_CONST.__const: 0x7a0
+  __DATA_CONST.__objc_classlist: 0x200
+  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_protolist: 0x78
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1688
+  __DATA_CONST.__objc_selrefs: 0x1990
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x158
+  __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x360
-  __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x1000
-  __AUTH_CONST.__objc_const: 0x5c30
-  __AUTH_CONST.__objc_intobj: 0x318
+  __AUTH_CONST.__auth_got: 0x3e0
+  __AUTH_CONST.__const: 0x200
+  __AUTH_CONST.__cfstring: 0x17e0
+  __AUTH_CONST.__objc_const: 0x60c0
+  __AUTH_CONST.__objc_intobj: 0x3f0
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0x1130
-  __DATA.__objc_ivar: 0x2d4
-  __DATA.__data: 0x4e0
-  __DATA.__bss: 0x50
+  __AUTH.__objc_data: 0x13b0
+  __DATA.__objc_ivar: 0x330
+  __DATA.__data: 0x5a0
+  __DATA.__bss: 0x78
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Matter.framework/Matter
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation
   - /System/Library/PrivateFrameworks/HomeKitMetrics.framework/HomeKitMetrics
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1352
-  Symbols:   1738
-  CStrings:  1702
+  Functions: 1486
+  Symbols:   1939
+  CStrings:  1928
 
Symbols:
+ _CFRelease
+ _MTRArrayValueType
+ _MTRAssociateControllerWithHomeUUID
+ _MTRAttributePathKey
+ _MTRBooleanValueType
+ _MTRContextTagKey
+ _MTRDataKey
+ _MTRDoubleValueType
+ _MTRErrorKey
+ _MTREventIsHistoricalKey
+ _MTREventNumberKey
+ _MTREventPathKey
+ _MTREventPriorityKey
+ _MTREventSystemUpTimeKey
+ _MTREventTimeTypeKey
+ _MTREventTimestampDateKey
+ _MTRFloatValueType
+ _MTRGetAssociatedHomeUUIDWithController
+ _MTRGetClientTypeForXPCConnection
+ _MTRIsPotentiallyPairing
+ _MTRPluginHMFMessageDescription
+ _MTRPluginHomeRunnningModeAsString
+ _MTRSetPotentialPairing
+ _MTRSignedIntegerValueType
+ _MTRStructureValueType
+ _MTRSwizzleMethods
+ _MTRTypeKey
+ _MTRUnsignedIntegerValueType
+ _MTRUpdateRunningModeForController
+ _MTRValueKey
+ _NSClassFromString
+ _OBJC_CLASS_$_MTRDeviceController
+ _OBJC_CLASS_$_MTRDeviceControllerFactory
+ _OBJC_CLASS_$_MTRPluginInvokeCommandExpectationMetric
+ _OBJC_CLASS_$_MTRPluginMetricsObserver
+ _OBJC_CLASS_$_MTRPluginMetricsTransformer
+ _OBJC_CLASS_$_MTRPluginRVCCleanModeMetric
+ _OBJC_CLASS_$_MTRPluginRVCOperationalStateMetric
+ _OBJC_CLASS_$_MTRPluginRVCRunModeMetric
+ _OBJC_CLASS_$_MTRPluginServiceAreaMetric
+ _OBJC_CLASS_$_MTRPluginUpdateControllerConfigMetric
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_METACLASS_$_MTRPluginInvokeCommandExpectationMetric
+ _OBJC_METACLASS_$_MTRPluginMetricsObserver
+ _OBJC_METACLASS_$_MTRPluginMetricsTransformer
+ _OBJC_METACLASS_$_MTRPluginRVCCleanModeMetric
+ _OBJC_METACLASS_$_MTRPluginRVCOperationalStateMetric
+ _OBJC_METACLASS_$_MTRPluginRVCRunModeMetric
+ _OBJC_METACLASS_$_MTRPluginServiceAreaMetric
+ _OBJC_METACLASS_$_MTRPluginUpdateControllerConfigMetric
+ _SecTaskCopySigningIdentifier
+ _SecTaskCopyValueForEntitlement
+ _SecTaskCreateFromSelf
+ _SecTaskCreateWithAuditToken
+ __HMFNilUUIDBytes
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
+ _audit_token_to_pid
+ _class_getInstanceMethod
+ _class_replaceMethod
+ _csops_audittoken
+ _getpid
+ _kCFAllocatorDefault
+ _method_getImplementation
+ _method_getTypeEncoding
+ _objc_getAssociatedObject
+ _objc_retainBlock
+ _objc_setAssociatedObject
+ _objc_unsafeClaimAutoreleasedReturnValue
- _fmod
CStrings:
+ "\x01\x11"
+ "\v"
+ "\x14"
+ "\x1e"
+ " => Assigning home UUID: %@ to connection: %@   controllerID: %@"
+ "%@ <= Sending response %@ for incoming request HMFMessage (%@ : %{uuid_t}.16P)"
+ "%@ <= Sending response for incoming request HMFMessage (%@ : %{uuid_t}.16P) with error: %@"
+ "%@ Adding commandPath %@ with class %@, registry: %@"
+ "%@ Adding new session receiver delegate %@ for sessionID: %{uuid_t}.16P"
+ "%@ Attempting to add commandPath %@ with class %@, registry: %@"
+ "%@ Calling invokeHandler on delegate %p for session with identifier %{uuid_t}.16P for message: %@"
+ "%@ Cannot find controller for UUID %@ - returning unknown running mode"
+ "%@ Deregistering selector for messageType: %@ on session: %{uuid_t}.16P"
+ "%@ Failed to deregister selector for messageType: %@ on session: %{uuid_t}.16P since session is not valid"
+ "%@ Failed to register selector %@ for messageType: %@ on session: %{uuid_t}.16P since session is not valid"
+ "%@ Forcing running mode to local for home %@, since we are potentially pairing"
+ "%@ Found class %@ matching commandPath %@ to transform invoke command expectation metric %@"
+ "%@ Handling notification %@ and re-querying running mode for all homes"
+ "%@ Home delegate returned running mode: %@ for homeUUID: %@"
+ "%@ Ignoring handling notification %@ since and server running state is NO"
+ "%@ Not querying running mode, we are not running"
+ "%@ Overriding running mode for home %@ to local since we are in potentially pairing window"
+ "%@ Potentially updating running mode for home %@, due to notification %@"
+ "%@ Registering selector %@ for messageType: %@ on session: %{uuid_t}.16P"
+ "%@ Removing delegate %@ for session: %{uuid_t}.16P"
+ "%@ Removing device controller entity: %@"
+ "%@ Running mode '%@' unchanged for home %@"
+ "%@ Running mode response was: %ld (%@)"
+ "%@ Switching running mode from '%@' to '%@' for home %@"
+ "%@ Switching running mode to '%@' for home %@"
+ "%@ Tried to remove device controller, but wasn't present: %@"
+ "%@ Updating a controller configuration for home %@ update for running mode '%@' so the new endpoint has context: %@"
+ "%@ delegate denied access for operation: %ld for %@"
+ "%@ deviceController %@ deleteNodeID %@"
+ "%@ deviceController: %@ deleteNodeID: %@"
+ "%@ dispatching invoke command expectation metric for event %@"
+ "%@ internalState is same as lastKnownInternalState, ignoring sending update to remote clients"
+ "*** We are potentially pairing, forcing/returning local mode without querying delegate"
+ "<%@: %p xpc %p pid: %d, clientType: %@>"
+ "<HMFMessage: %p ID: %@ Dest: %@>"
+ "<invalid value>"
+ "@\"MTRAttributeValueWaiter\""
+ "@\"MTRPluginInvokeCommandMetric\""
+ "@\"MTRPluginMetric\"24@0:8@\"MTRPluginInvokeCommandExpectationMetric\"16"
+ "@\"MTRPluginMetricsObserver\""
+ "@\"MTRPluginMetricsTransformer\""
+ "@\"NSMapTable\""
+ "@32@0:8@16#24"
+ "@40@0:8@16@24q32"
+ "@48@0:8@16@24@32@40"
+ "@48@0:8@16@24Q32@40"
+ "@52@0:8@16@24i32q36@44"
+ "@68@0:8@16@24@32@40@48B56@60"
+ "@96@0:8@16@24i32@36@44@52@60@68@76B84@88"
+ "B40@0:8@16@24^@32"
+ "Done potential pairing"
+ "FirstPartyApp"
+ "HMDHomeManagerFirstProcessDidBecomeActiveNotification"
+ "HMDHomeManagerLastProcessDidBecomeInactiveNotification"
+ "HMDXPCConnectionClientIdentifierKey"
+ "HMMLogEventObserver"
+ "HomeApp"
+ "HomeKitDaemon"
+ "Ignoring process activation for %@, not com.apple.Home.HomeUIService"
+ "Ignoring process de-activation for %@, not com.apple.Home.HomeUIService"
+ "Local"
+ "MTRDeviceController"
+ "MTRDeviceControllerFactory"
+ "MTRDeviceController_Concrete"
+ "MTRDeviceInternalPropertyDeviceCachePrimed"
+ "MTRDeviceInternalPropertyDeviceInternalState"
+ "MTRDeviceInternalPropertyDeviceState"
+ "MTRDeviceInternalPropertyNetworkFeatures"
+ "MTRDeviceInternalStateKeyProductID"
+ "MTRDeviceInternalStateKeyVendorID"
+ "MTRPluginInvokeCommandExpectationMetric"
+ "MTRPluginMetricTransformDelegate"
+ "MTRPluginMetricsObserver"
+ "MTRPluginMetricsTransformer"
+ "MTRPluginPairingPotentiallyCompletedNotification"
+ "MTRPluginPairingPotentiallyStartingNotification"
+ "MTRPluginRVCCleanModeMetric"
+ "MTRPluginRVCOperationalStateMetric"
+ "MTRPluginRVCRunModeMetric"
+ "MTRPluginServerQueue"
+ "MTRPluginServiceAreaMetric"
+ "MTRPluginUpdateControllerConfigMetric"
+ "PairingStateManagement"
+ "PlatformBinary"
+ "Process activation for %@"
+ "Process de-activation for %@"
+ "Remote"
+ "RemoteClient"
+ "Siri"
+ "SpringBoard"
+ "Starting potential pairing from prewarming"
+ "Starting potential pairing from prewarming on factory"
+ "Starting potential pairing from setupCommissioningSessionWithPayload"
+ "Starting potential pairing: %@   home: %@"
+ "Swizzing method for orignal class %@, target class %@, original selector: %@, swizzledSelector: %@"
+ "Swizzling MTRController methods for pairing"
+ "Swizzling MTRDeviceControllerFactory methods for pairing"
+ "T@\"MTRAttributeValueWaiter\",&,V_attributeValueWaiter"
+ "T@\"MTRDevice\",W,V_device"
+ "T@\"MTRPluginInvokeCommandMetric\",&,V_invokeCommandMetric"
+ "T@\"MTRPluginInvokeCommandMetric\",&,V_originalInvokeCommandMetric"
+ "T@\"MTRPluginMetricsObserver\",&,V_transformMetrics"
+ "T@\"MTRPluginMetricsTransformer\",&,V_metricsTransformer"
+ "T@\"NSArray\",&,V_attributeReport"
+ "T@\"NSArray\",&,V_eventReport"
+ "T@\"NSArray\",&,V_expectedValues"
+ "T@\"NSDictionary\",&,V_eventEntry"
+ "T@\"NSDictionary\",&,V_lastKnownInternalState"
+ "T@\"NSDictionary\",&,V_reportEntry"
+ "T@\"NSMapTable\",&,V_commandPathRegistry"
+ "T@\"NSNumber\",&,V_expectedValueInterval"
+ "T@\"NSObject<OS_dispatch_source>\",&,V_deviceBecameActiveSource"
+ "T@\"NSUUID\",&,V_controllerUUID"
+ "T@\"NSUUID\",&,V_remoteMessageID"
+ "T@,&,V_commandFields"
+ "TB,GisDeviceAtExpectedState,V_deviceAtExpectedState"
+ "ThirdPartyApp"
+ "Ti,V_clientType"
+ "Tq,V_runningMode"
+ "URL %@ has nil lastPathComponent: %@"
+ "Unknown"
+ "__plugin__preWarmCommissioningSession"
+ "__plugin__setupCommissioningSessionWithPayload:newNodeID:error:"
+ "_assignHomeUUIDIfUnassigned:"
+ "_attributeReport"
+ "_attributeValueWaiter"
+ "_clientType"
+ "_commandPathRegistry"
+ "_controllerUUID"
+ "_deviceAtExpectedState"
+ "_deviceBecameActiveSource"
+ "_eventEntry"
+ "_eventReport"
+ "_invokeCommandMetric"
+ "_lastKnownInternalState"
+ "_metricsTransformer"
+ "_originalInvokeCommandMetric"
+ "_pairingStartedNotification:"
+ "_pairingStoppedNotification:"
+ "_queryAndUpdateRunningModeForHomeUUID:"
+ "_remoteMessageID"
+ "_reportEntry"
+ "_resumeControllerForPotentialPairing:"
+ "_runningMode"
+ "_runningModeChanged:forHomeUUID:"
+ "_runningModeForUUID:"
+ "_safeQueryRunningModeFromDelegateForHomeUUID:"
+ "_sendMessageToHomeWithID:messageType:pbCodable:metric:errorBlock:replyBlock:"
+ "_transformMetrics"
+ "_unsafeQueryRunningModeFromDelegateForHomeUUID:"
+ "_updateRunningMode:forceUpdateControllerConfiguration:forHomeUUID:"
+ "_updateRunningModeForAllControllers"
+ "_updateSuspendedStateBasedOnRunningMode:"
+ "addObserver:forEventClasses:"
+ "allAreasSelected"
+ "apple."
+ "application-identifier"
+ "assistant_service"
+ "attributeReport"
+ "attributeReportMetricForDevice:homeID:attributeReport:remoteMessageID:"
+ "attributeValue"
+ "attributeValueWaiter"
+ "auditToken"
+ "bulkReadAttributeMetricForDevice:homeID:remoteMessageID:"
+ "clientType"
+ "com.apple"
+ "com.apple.Home.HomeUIService"
+ "com.apple.PineBoard"
+ "com.apple.Siri"
+ "com.apple.SpringBoard"
+ "com.apple.matter.invokeCommandExpectationEvent"
+ "com.apple.matter.rvcCleanModeEvent"
+ "com.apple.matter.rvcOperationalStateEvent"
+ "com.apple.matter.rvcRunModeEvent"
+ "com.apple.matter.serviceAreaEvent"
+ "com.apple.matter.updateControllerConfigMetric"
+ "commandPathRegistry"
+ "commandPaths"
+ "controller:readCommissioneeInfo:"
+ "controllerUUID"
+ "deviceActiveMetricForDevice:homeID:remoteMessageID:"
+ "deviceAtExpectedState"
+ "deviceBecameActiveSource"
+ "deviceCachePrimedMetricForDevice:homeID:remoteMessageID:"
+ "deviceConfigChangedMetricForDevice:homeID:remoteMessageID:"
+ "deviceController:deleteNodeID:"
+ "deviceInternalStateUpdatedForDevice:homeID:remoteMessageID:"
+ "dictionaryWithDictionary:"
+ "didReceiveEventFromDispatcher:"
+ "dispatchInvokeCommandExpectationMetric:"
+ "downloadDiagnosticMetricForDevice:homeID:clientType:logType:remoteMessageID:"
+ "durationMilliseconds"
+ "durationMs"
+ "eventEntry"
+ "eventIsHistorical"
+ "eventNumber"
+ "eventPriority"
+ "eventReport"
+ "eventReportMetricForDevice:homeID:eventReport:remoteMessageID:"
+ "eventSystemUptime"
+ "eventTime"
+ "eventTimestamp"
+ "eventValue"
+ "expectedRVCCleanMode"
+ "expectedRVCOperationalState"
+ "expectedRVCRunMode"
+ "forgetDeviceWithNodeID:"
+ "getUUIDBytes:"
+ "hasPrefix:"
+ "initMetricWithName:device:homeID:remoteMessageID:"
+ "initMetricWithName:sourceMetric:"
+ "initWithController:entityIdentifier:runningMode:"
+ "initWithStartTime:homeUUID:"
+ "invokeCommandExpectationMetricForMetric:"
+ "invokeCommandMetric"
+ "invokeCommandMetricForDevice:homeID:clientType:endpointID:clusterID:commandID:commandFields:expectedValues:expectedValueInterval:timedInvoke:remoteMessageID:"
+ "isDeviceAtExpectedState"
+ "lastKnownInternalState"
+ "length"
+ "markEndTime"
+ "metricsTransformer"
+ "networkCommissioningFeatures"
+ "numberValueFromDataValueDictionary:"
+ "originalInvokeCommandMetric"
+ "postNotificationName:object:"
+ "preWarmCommissioningSession"
+ "registerCommandPath:class:"
+ "remoteMessageID"
+ "removeObserver:"
+ "reportEntry"
+ "runningMode"
+ "rvcCleanMode"
+ "rvcOperationalState"
+ "rvcRunMode"
+ "sendControllerMessageToHomeWithID:controllerMessageType:queryRequestValue:metric:errorBlock:replyBlock:"
+ "sendDeviceMessageToNodeWithID:homeID:deviceNodeMessageType:metric:errorBlock:replyBlock:"
+ "sendMessageToHomeWithID:messageType:pbCodable:metric:errorBlock:replyBlock:"
+ "serverWorkQueue"
+ "setAttributeReport:"
+ "setAttributeValueWaiter:"
+ "setClientType:"
+ "setCommandPathRegistry:"
+ "setControllerUUID:"
+ "setDeviceAtExpectedState:"
+ "setDeviceBecameActiveSource:"
+ "setEventEntry:"
+ "setEventReport:"
+ "setInvokeCommandMetric:"
+ "setLastKnownInternalState:"
+ "setMetricsTransformer:"
+ "setOriginalInvokeCommandMetric:"
+ "setRemoteMessageID:"
+ "setReportEntry:"
+ "setRunningMode:"
+ "setTransformMetrics:"
+ "setupCommissioningSessionWithPayload:newNodeID:error:"
+ "startTime"
+ "stateChangedMetricForDevice:homeID:state:remoteMessageID:"
+ "strongToStrongObjectsMapTable"
+ "submitMetric"
+ "supportsEthernet"
+ "supportsThread"
+ "supportsWiFi"
+ "swizzlePrewarm"
+ "totalAreasSelected"
+ "transformInvokeCommandExpectationMetric:"
+ "transformMetrics"
+ "unregisterCommandPath:"
+ "updateControllerConfigMetricForHome:remoteMessageID:"
+ "userInfo"
+ "v24@0:8@\"HMMLogEvent\"16"
+ "v32@0:8@\"MTRDeviceController\"16@\"MTRCommissioneeInfo\"24"
+ "v32@0:8q16@24"
+ "v36@0:8q16B24@28"
+ "v60@0:8@16@24i32@36@?44@?52"
+ "v60@0:8@16i24@28@36@?44@?52"
+ "waitForAttributeValues:timeout:queue:completion:"
+ "writeAttributeMetricForDevice:homeID:endpointID:clusterID:attributeID:timedWrite:remoteMessageID:"
+ "xpcClientConnectionQueue"
- "\a\x16"
- "\t"
- "\x12"
- " *** Ignoring new home UUID: %@ for connection: %@, and invalidating"
- " => Assigning home UUID: %@ to connection: %@"
- "%@ <= Sending response %@ for incoming request HMFMessage (%@ : %@)"
- "%@ <= Sending response for incoming request HMFMessage (%@ : %@) with error: %@"
- "%@ Adding new session receiver delegate %@ for sessionID: %@"
- "%@ Calling invokeHandler on delegate %p for session with identifier %@ for message: %@"
- "%@ Deregistering selector for messageType: %@ on session: %@"
- "%@ Failed to deregister selector for messageType: %@ on session: %@ since session is not valid"
- "%@ Failed to register selector %@ for messageType: %@ on session: %@ since session is not valid"
- "%@ Failed to send device became active with error: %@"
- "%@ IGNORING request to remove device controller: %@"
- "%@ Registering selector %@ for messageType: %@ on session: %@"
- "%@ Removing delegate %@ for session: %@"
- "%@ Running mode response was: %ld"
- "%@ Successfully sent device became active"
- "%@ delegate denied access to operation: %ld for %@"
- "<%@: %p xpc %p pid: %d>"
- "@36@0:8@16@24B32"
- "@44@0:8@16@24@32B40"
- "@44@0:8@16@24Q32B40"
- "@44@0:8@16@24q32B40"
- "@64@0:8@16@24@32@40@48B56B60"
- "T@\"MTRDevice\",&,V_device"
- "TB,GisRemoteMode,V_remoteMode"
- "TB,GisSuspended,V_suspended"
- "Tq,V_currentRunningMode"
- "_currentRunningMode"
- "_queryHomeRunningModeFromDelegateForHomeUUID:"
- "_remoteMode"
- "_runningModeForHomeUUID:runningModeChanged:"
- "_sendMessageToHomeWithID:messageType:pbCodable:errorBlock:replyBlock:"
- "_suspended"
- "_updateSuspendedStateBasedOnRunningMode"
- "attributeReportMetricForDevice:homeID:remoteMode:"
- "bulkReadAttributeMetricForDevice:homeID:remoteMode:"
- "currentRunningMode"
- "deviceActiveMetricForDevice:homeID:remoteMode:"
- "deviceCachePrimedMetricForDevice:homeID:remoteMode:"
- "deviceConfigChangedMetricForDevice:homeID:remoteMode:"
- "deviceInternalStateUpdatedForDevice:homeID:remoteMode:"
- "downloadDiagnosticMetricForDevice:homeID:logType:remoteMode:"
- "eventReportMetricForDevice:homeID:remoteMode:"
- "initMetricWithName:device:homeID:remoteMode:"
- "initWithController:entityIdentifier:"
- "invokeCommandMetricForDevice:homeID:endpointID:clusterID:commandID:timedInvoke:remoteMode:"
- "isRemoteMode"
- "sendControllerMessageToHomeWithID:controllerMessageType:queryRequestValue:errorBlock:replyBlock:"
- "sendDeviceMessageToNodeWithID:homeID:deviceNodeMessageType:errorBlock:replyBlock:"
- "sendMessageToHomeWithID:messageType:pbCodable:errorBlock:replyBlock:"
- "setCurrentRunningMode:"
- "setRemoteMode:"
- "setSuspended:"
- "stateChangedMetricForDevice:homeID:state:remoteMode:"
- "suspended"
- "v52@0:8@16@24i32@?36@?44"
- "v52@0:8@16i24@28@?36@?44"
- "writeAttributeMetricForDevice:homeID:endpointID:clusterID:attributeID:timedWrite:remoteMode:"

```
