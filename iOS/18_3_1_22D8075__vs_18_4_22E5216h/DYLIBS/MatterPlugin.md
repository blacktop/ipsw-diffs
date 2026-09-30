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
+49.5.7.0.0
+  __TEXT.__text: 0x445b4
+  __TEXT.__auth_stubs: 0x7d0
+  __TEXT.__objc_methlist: 0x4694
+  __TEXT.__const: 0xf0
+  __TEXT.__cstring: 0x11d6
+  __TEXT.__oslogstring: 0x502a
+  __TEXT.__gcc_except_tab: 0x1ca0
+  __TEXT.__unwind_info: 0x1118
+  __TEXT.__objc_classname: 0x9a1
+  __TEXT.__objc_methname: 0x74d4
+  __TEXT.__objc_methtype: 0x1516
+  __TEXT.__objc_stubs: 0x58e0
+  __DATA_CONST.__got: 0x460
+  __DATA_CONST.__const: 0x850
+  __DATA_CONST.__objc_classlist: 0x218
+  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1688
+  __DATA_CONST.__objc_selrefs: 0x1b10
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x158
+  __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x360
-  __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0x1000
-  __AUTH_CONST.__objc_const: 0x5c30
-  __AUTH_CONST.__objc_intobj: 0x318
+  __AUTH_CONST.__auth_got: 0x3f8
+  __AUTH_CONST.__const: 0x220
+  __AUTH_CONST.__cfstring: 0x18c0
+  __AUTH_CONST.__objc_const: 0x6700
+  __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0x1130
-  __DATA.__objc_ivar: 0x2d4
-  __DATA.__data: 0x4e0
-  __DATA.__bss: 0x50
+  __AUTH.__objc_data: 0x14a0
+  __DATA.__objc_ivar: 0x368
+  __DATA.__data: 0x600
+  __DATA.__bss: 0x80
+  __DATA.__common: 0x8
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
+  Functions: 1605
+  Symbols:   2067
+  CStrings:  2043
 
Symbols:
+ OBJC_IVAR_$_MTRPluginPBMCommandWithRequiredResponse._commandFields
+ OBJC_IVAR_$_MTRPluginPBMCommandWithRequiredResponse._commandPath
+ OBJC_IVAR_$_MTRPluginPBMCommandWithRequiredResponse._requiredResponse
+ OBJC_IVAR_$_MTRPluginPBMCommandWithRequiredResponses._commandWithRequiredResponseValues
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage._commandWithRequiredResponsesValues
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage._header
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage._node
+ _CFRelease
+ _MTRArrayValueType
+ _MTRAssociateControllerWithHomeUUID
+ _MTRAttributePathKey
+ _MTRBooleanValueType
+ _MTRContextTagKey
+ _MTRDataKey
+ _MTRDoubleValueType
+ _MTREventPathKey
+ _MTRFloatValueType
+ _MTRGetAssociatedHomeUUIDWithController
+ _MTRGetClientTypeForXPCConnection
+ _MTRIsPotentiallyPairing
+ _MTRPluginHMFMessageDescription
+ _MTRPluginHomeRunnningModeAsString
+ _MTRPluginPBMCommandWithRequiredResponseReadFrom
+ _MTRPluginPBMCommandWithRequiredResponsesReadFrom
+ _MTRPluginPBMDeviceNodeInvokeBatchCommmandMessageReadFrom
+ _MTRSetPotentialPairing
+ _MTRSignedIntegerValueType
+ _MTRStructureValueType
+ _MTRSwizzleMethods
+ _MTRTypeKey
+ _MTRUnsignedIntegerValueType
+ _MTRUpdateRunningModeForController
+ _MTRValueKey
+ _NSClassFromString
+ _OBJC_CLASS_$_HMFTimer
+ _OBJC_CLASS_$_MTRCommandWithRequiredResponse
+ _OBJC_CLASS_$_MTRDeviceController
+ _OBJC_CLASS_$_MTRDeviceControllerFactory
+ _OBJC_CLASS_$_MTRPluginInvokeCommandExpectationMetric
+ _OBJC_CLASS_$_MTRPluginMetricsObserver
+ _OBJC_CLASS_$_MTRPluginMetricsTransformer
+ _OBJC_CLASS_$_MTRPluginPBMCommandWithRequiredResponse
+ _OBJC_CLASS_$_MTRPluginPBMCommandWithRequiredResponses
+ _OBJC_CLASS_$_MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage
+ _OBJC_CLASS_$_MTRPluginRVCCleanModeMetric
+ _OBJC_CLASS_$_MTRPluginRVCOperationalStateMetric
+ _OBJC_CLASS_$_MTRPluginRVCRunModeMetric
+ _OBJC_CLASS_$_MTRPluginServiceAreaMetric
+ _OBJC_CLASS_$_MTRPluginUpdateControllerConfigMetric
+ _OBJC_CLASS_$_NSMapTable
+ _OBJC_METACLASS_$_MTRPluginInvokeCommandExpectationMetric
+ _OBJC_METACLASS_$_MTRPluginMetricsObserver
+ _OBJC_METACLASS_$_MTRPluginMetricsTransformer
+ _OBJC_METACLASS_$_MTRPluginPBMCommandWithRequiredResponse
+ _OBJC_METACLASS_$_MTRPluginPBMCommandWithRequiredResponses
+ _OBJC_METACLASS_$_MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage
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
+ _matterPluginLogInitialize
+ _matterPluginLog_default
+ _method_getImplementation
+ _method_getTypeEncoding
+ _objc_getAssociatedObject
+ _objc_opt_self
+ _objc_retainBlock
+ _objc_retain_x9
+ _objc_setAssociatedObject
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _os_log_create
- __os_log_default
- _fmod
CStrings:
+ "\x05"
+ "\v"
+ "\x14"
+ "\x15"
+ "\x17"
+ "\x1e"
+ " => Assigning home UUID: %@ to connection: %@   controllerID: %@"
+ "!"
+ "%@  => DOUBLE registering device (already registered): %@"
+ "%@ <= Sending response %@ for incoming request HMFMessage (%@ : %{uuid_t}.16P)"
+ "%@ <= Sending response for incoming request HMFMessage (%@ : %{uuid_t}.16P) with error: %@"
+ "%@ Adding commandPath %@ with class %@, registry: %@"
+ "%@ Adding new session receiver delegate %@ for sessionID: %{uuid_t}.16P"
+ "%@ Attempting to add commandPath %@ with class %@, registry: %@"
+ "%@ Calling invokeHandler on delegate %p for session with identifier %{uuid_t}.16P for message: %@"
+ "%@ Cannot find controller for UUID %@ - returning unknown running mode, controller was not added to registry"
+ "%@ Cannot find controller for UUID %@ in %lu controllers - controller was not added to registry"
+ "%@ Cannot find device controller for client %@ nodeID %@ - controller was not added to registry"
+ "%@ Deregistering selector for messageType: %@ on session: %{uuid_t}.16P"
+ "%@ Failed to complete invokeBatchCommand with error: %@"
+ "%@ Failed to deregister selector for messageType: %@ on session: %{uuid_t}.16P since session is not valid"
+ "%@ Failed to invoke batch commands for nodeID: %@, with error %@, for message %@"
+ "%@ Failed to register selector %@ for messageType: %@ on session: %{uuid_t}.16P since session is not valid"
+ "%@ Forcing running mode to local for home %@, since we are potentially pairing"
+ "%@ Forwarding remote request to invokeBatchCommand: commands (%@), from device nodeID (%@) for controllerID %@"
+ "%@ Found class %@ matching commandPath %@ to transform invoke command expectation metric %@"
+ "%@ Handling notification %@ and re-querying running mode for all homes"
+ "%@ Home delegate returned running mode: %@ for homeUUID: %@"
+ "%@ Ignoring handling notification %@ since and server running state is NO"
+ "%@ Ignoring notification %@ since delegate / delegateQueue is nil"
+ "%@ Ignoring notification %@ since homeUUID is nil"
+ "%@ Invoking Batch Commands on: nodeID %@ message (%@) commands %@"
+ "%@ No receiver delegate for new session setup message: %@, sending error"
+ "%@ Not querying running mode, we are not running"
+ "%@ Overriding running mode for home %@ to local since we are in potentially pairing window"
+ "%@ Potentially updating running mode for home %@, due to notification %@"
+ "%@ Received message %@ but delegate %@ is suspended, sending error response to close remote session"
+ "%@ Received resident update notification %@"
+ "%@ Registering selector %@ for messageType: %@ on session: %{uuid_t}.16P"
+ "%@ Removing delegate %@ for session: %{uuid_t}.16P"
+ "%@ Removing device controller entity: %@"
+ "%@ Resumed remote client"
+ "%@ Running mode '%@' unchanged for home %@"
+ "%@ Running mode response was: %ld (%@)"
+ "%@ Successfully completed invokeBatchCommand with response: %@"
+ "%@ Suspended remote client"
+ "%@ Switching running mode from '%@' to '%@' for home %@"
+ "%@ Switching running mode to '%@' for home %@"
+ "%@ Tried to remove device controller, but wasn't present: %@"
+ "%@ Updating a controller configuration for home %@ update for running mode '%@' so the new endpoint has context: %@"
+ "%@ Updating running mode for all clients to '%@' for home %@"
+ "%@ Updating running mode for home %@ since primary resident updated with notification %@"
+ "%@ delegate denied access for operation: %ld for %@"
+ "%@ deviceController %@ deleteNodeID %@"
+ "%@ deviceController %@ getNodesWithStoredDataWithReply"
+ "%@ deviceController: %@ deleteNodeID: %@"
+ "%@ deviceController: %@ getNodesWithStoredDataWithReply"
+ "%@ dispatching invoke command expectation metric for event %@"
+ "%@ internalState is same as lastKnownInternalState, ignoring sending update to remote clients"
+ "%@ invokeCommands: controllerUUID %@ nodeID %@ commands %@"
+ "%@ invokeCommands: controllerUUID %@ nodeID %@ completed with error %@"
+ "%@ metrics counter fired, submitting count for %ld metrics"
+ "%@ responding to invoke batch command for nodeID: %@, for message %@"
+ "%@ resuming remote server session for home %@ since running mode is remote"
+ "%@ suspending remote server session for home %@ since running mode is local"
+ "*** We are potentially pairing, forcing/returning local mode without querying delegate"
+ "<%@: %p xpc %p pid: %d, clientType: %@>"
+ "<%@: %p, clientType: %@>"
+ "<HMFMessage: %p ID: %@ Dest: %@>"
+ "<invalid value>"
+ "@\"HMFTimer\""
+ "@\"MTRAttributePath\""
+ "@\"MTRAttributeValueWaiter\""
+ "@\"MTREventPath\""
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
+ "@60@0:8@16@24i32@36@44@52"
+ "@72@0:8@16@24i32@36@44@52B60@64"
+ "@96@0:8@16@24i32@36@44@52@60@68@76B84@88"
+ "B40@0:8@16@24^@32"
+ "Default"
+ "Done potential pairing"
+ "FirstPartyApp"
+ "Found Bundle Identifier %@ for XPC connection %@"
+ "HMDHomeManagerFirstProcessDidBecomeActiveNotification"
+ "HMDHomeManagerLastProcessDidBecomeInactiveNotification"
+ "HMDResidentDeviceConfirmedStateChangedNotification"
+ "HMDResidentDeviceHomeUUIDNotificationKey"
+ "HMDResidentDeviceManagerUpdatePrimaryResidentNotification"
+ "HMDResidentDeviceManagerUpdateResidentNotification"
+ "HMDXPCConnectionClientIdentifierKey"
+ "HMFTimerDelegate"
+ "HMMLogEventObserver"
+ "HomeApp"
+ "HomeAppWidget"
+ "HomeKitDaemon"
+ "Ignoring process activation for %@, not com.apple.Home.HomeUIService"
+ "Ignoring process de-activation for %@, not com.apple.Home.HomeUIService"
+ "InvokeBatchCommand"
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
+ "MTRPluginPBMCommandWithRequiredResponse"
+ "MTRPluginPBMCommandWithRequiredResponses"
+ "MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage"
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
+ "T@\"HMFTimer\",&,V_timer"
+ "T@\"MTRAttributePath\",&,V_attributePath"
+ "T@\"MTRAttributeValueWaiter\",&,V_attributeValueWaiter"
+ "T@\"MTRCommandWithRequiredResponse\",R,N"
+ "T@\"MTRDevice\",W,V_device"
+ "T@\"MTREventPath\",&,V_eventPath"
+ "T@\"MTRPluginInvokeCommandMetric\",&,V_invokeCommandMetric"
+ "T@\"MTRPluginMetricsObserver\",&,V_transformMetrics"
+ "T@\"MTRPluginMetricsTransformer\",&,V_metricsTransformer"
+ "T@\"MTRPluginPBMVariableValue\",&,N,V_requiredResponse"
+ "T@\"NSArray\",&,V_attributeReport"
+ "T@\"NSArray\",&,V_eventReport"
+ "T@\"NSArray\",&,V_expectedValues"
+ "T@\"NSDictionary\",&,V_lastKnownInternalState"
+ "T@\"NSMapTable\",&,V_commandPathRegistry"
+ "T@\"NSMutableArray\",&,N,V_commandWithRequiredResponseValues"
+ "T@\"NSMutableArray\",&,N,V_commandWithRequiredResponsesValues"
+ "T@\"NSMutableSet\",&,V_homesWithPrimaryResidentUpdated"
+ "T@\"NSMutableSet\",&,V_metricCounter"
+ "T@\"NSNumber\",&,V_count"
+ "T@\"NSNumber\",&,V_expectedValueInterval"
+ "T@\"NSObject<OS_dispatch_source>\",&,V_deviceBecameActiveSource"
+ "T@\"NSObject<OS_dispatch_source>\",&,V_primaryResidentUpdatedSource"
+ "T@\"NSUUID\",&,V_controllerUUID"
+ "T@\"NSUUID\",&,V_remoteMessageID"
+ "T@,&,V_commandFields"
+ "TB,?,R,GisSuspended"
+ "TB,GisBatchCommand,V_batchCommand"
+ "TB,GisDeviceAtExpectedState,V_deviceAtExpectedState"
+ "ThirdPartyApp"
+ "Ti,V_clientType"
+ "Tq,V_runningMode"
+ "URL %@ has nil lastPathComponent: %@"
+ "Unknown"
+ "Vv32@0:8@\"NSUUID\"16@?<v@?@\"NSArray\">24"
+ "Vv32@0:8@16@?24"
+ "Vv48@0:8@\"NSUUID\"16@\"NSNumber\"24@\"NSArray\"32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "__plugin__preWarmCommissioningSession"
+ "__plugin__setupCommissioningSessionWithPayload:newNodeID:error:"
+ "_assignHomeUUIDIfUnassigned:"
+ "_attributeReport"
+ "_attributeValueWaiter"
+ "_batchCommand"
+ "_clientType"
+ "_closeRemoteServerSession"
+ "_commandPathRegistry"
+ "_commandWithRequiredResponseValues"
+ "_commandWithRequiredResponsesValues"
+ "_controllerUUID"
+ "_count"
+ "_deviceAtExpectedState"
+ "_deviceBecameActiveSource"
+ "_eventPath"
+ "_eventReport"
+ "_homesWithPrimaryResidentUpdated"
+ "_invokeCommandMetric"
+ "_lastKnownInternalState"
+ "_metricCounter"
+ "_metricsTransformer"
+ "_pairingStartedNotification:"
+ "_pairingStoppedNotification:"
+ "_primaryResidentUpdatedSource"
+ "_queryAndUpdateRunningModeForHomeUUID:"
+ "_registerForResidentChangedNotifications"
+ "_remoteMessageID"
+ "_requiredResponse"
+ "_resumeControllerForPotentialPairing:"
+ "_runningMode"
+ "_runningModeChanged:forHomeUUID:"
+ "_runningModeForUUID:"
+ "_safeQueryRunningModeFromDelegateForHomeUUID:"
+ "_sendMessageToHomeWithID:messageType:pbCodable:metric:errorBlock:replyBlock:"
+ "_timer"
+ "_transformMetrics"
+ "_unsafeQueryRunningModeFromDelegateForHomeUUID:"
+ "_updateRunningMode:forceUpdateControllerConfiguration:forHomeUUID:"
+ "_updateRunningModeForAllControllers"
+ "_updateRunningModeOfAllClientsForHome:"
+ "_updateSuspendedStateBasedOnRunningMode:"
+ "addCommandWithRequiredResponseValue:"
+ "addCommandWithRequiredResponsesValue:"
+ "addObserver:forEventClasses:"
+ "allAreasSelected"
+ "apple."
+ "application-identifier"
+ "areaSkipped"
+ "areasSelected"
+ "assistant_service"
+ "attributeReport"
+ "attributeReportMetricForDevice:homeID:attributeReport:remoteMessageID:"
+ "attributeValueWaiter"
+ "auditToken"
+ "batchCommand"
+ "bulkReadAttributeMetricForDevice:homeID:remoteMessageID:"
+ "clearCommandWithRequiredResponseValues"
+ "clearCommandWithRequiredResponsesValues"
+ "clientType"
+ "com.apple"
+ "com.apple.Home.HomeUIService"
+ "com.apple.Home.HomeWidget.Interactive"
+ "com.apple.HomeAppIntentsExtension"
+ "com.apple.PineBoard"
+ "com.apple.Siri"
+ "com.apple.matter.invokeCommandExpectationEvent"
+ "com.apple.matter.rvcCleanModeEvent"
+ "com.apple.matter.rvcOperationalStateEvent"
+ "com.apple.matter.rvcRunModeEvent"
+ "com.apple.matter.serviceAreaEvent"
+ "com.apple.matter.updateControllerConfigMetric"
+ "com.apple.springboard"
+ "commandPathRegistry"
+ "commandPaths"
+ "commandWithRequiredResponse"
+ "commandWithRequiredResponse:"
+ "commandWithRequiredResponseFromMessage:"
+ "commandWithRequiredResponseValue"
+ "commandWithRequiredResponseValueAtIndex:"
+ "commandWithRequiredResponseValueType"
+ "commandWithRequiredResponseValues"
+ "commandWithRequiredResponseValuesCount"
+ "commandWithRequiredResponses"
+ "commandWithRequiredResponses:"
+ "commandWithRequiredResponsesFromMessage:"
+ "commandWithRequiredResponsesValue"
+ "commandWithRequiredResponsesValueAtIndex:"
+ "commandWithRequiredResponsesValueType"
+ "commandWithRequiredResponsesValues"
+ "commandWithRequiredResponsesValuesCount"
+ "commands"
+ "controller:readCommissioneeInfo:"
+ "controllerUUID"
+ "countMetric:"
+ "deviceActiveMetricForDevice:homeID:remoteMessageID:"
+ "deviceAtExpectedState"
+ "deviceBecameActiveSource"
+ "deviceCachePrimedMetricForDevice:homeID:remoteMessageID:"
+ "deviceConfigChangedMetricForDevice:homeID:remoteMessageID:"
+ "deviceController:deleteNodeID:"
+ "deviceController:getNodesWithStoredDataWithReply:"
+ "deviceController:nodeID:invokeCommands:completion:"
+ "deviceInternalStateUpdatedForDevice:homeID:remoteMessageID:"
+ "deviceNodeInvokeBatchCommandMessageFromMessage:"
+ "deviceNodeInvokeBatchCommandMessageWithNodeID:commands:"
+ "dictionaryWithDictionary:"
+ "didReceiveEventFromDispatcher:"
+ "dispatchInvokeCommandExpectationMetric:"
+ "downloadDiagnosticMetricForDevice:homeID:clientType:logType:remoteMessageID:"
+ "durationMilliseconds"
+ "durationMs"
+ "eventCount"
+ "eventReport"
+ "eventReportMetricForDevice:homeID:eventReport:remoteMessageID:"
+ "expectedRVCCleanMode"
+ "expectedRVCRunMode"
+ "forgetDeviceWithNodeID:"
+ "getUUIDBytes:"
+ "handlePrimaryResidentUpdateNotification:"
+ "hasPrefix:"
+ "hasRequiredResponse"
+ "homesWithPrimaryResidentUpdated"
+ "initMetricWithName:device:homeID:remoteMessageID:"
+ "initMetricWithName:sourceMetric:"
+ "initWithController:entityIdentifier:runningMode:"
+ "initWithPath:commandFields:requiredResponse:"
+ "initWithStartTime:homeUUID:"
+ "initWithTimeInterval:options:"
+ "invokeBatchCommandMetricForDevice:homeID:clientType:commandPath:commandFields:remoteMessageID:"
+ "invokeCommandExpectationMetricForMetric:"
+ "invokeCommandMetric"
+ "invokeCommandMetricForDevice:homeID:clientType:endpointID:clusterID:commandID:commandFields:expectedValues:expectedValueInterval:timedInvoke:remoteMessageID:"
+ "invokeCommands:queue:completion:"
+ "isBatchCommand"
+ "isDeviceAtExpectedState"
+ "isPluginClientLowestHash:"
+ "lastKnownInternalState"
+ "length"
+ "markEndTime"
+ "member:"
+ "messageTransport:handleDeviceInvokeBatchCommand:"
+ "metricCounter"
+ "metricsTransformer"
+ "networkCommissioningFeatures"
+ "nodesWithStoredData"
+ "numberValueFromDataValueDictionary:"
+ "path"
+ "postNotificationName:object:"
+ "preWarmCommissioningSession"
+ "primaryResidentUpdatedSource"
+ "registerCommandPath:class:"
+ "remoteMessageID"
+ "removeObserver:"
+ "reportCount"
+ "requiredResponse"
+ "runningMode"
+ "rvcCleanMode"
+ "rvcOperationalState"
+ "rvcRunMode"
+ "sendControllerMessageToHomeWithID:controllerMessageType:queryRequestValue:metric:errorBlock:replyBlock:"
+ "sendDeviceMessageToNodeWithID:homeID:deviceNodeMessageType:metric:errorBlock:replyBlock:"
+ "sendMessageToHomeWithID:messageType:pbCodable:metrics:errorBlock:replyBlock:"
+ "serverWorkQueue"
+ "setAttributeReport:"
+ "setAttributeValueWaiter:"
+ "setBatchCommand:"
+ "setClientType:"
+ "setCommandPathRegistry:"
+ "setCommandWithRequiredResponseValues:"
+ "setCommandWithRequiredResponsesValues:"
+ "setControllerUUID:"
+ "setCount:"
+ "setDeviceAtExpectedState:"
+ "setDeviceBecameActiveSource:"
+ "setEventReport:"
+ "setHomesWithPrimaryResidentUpdated:"
+ "setInvokeCommandMetric:"
+ "setLastKnownInternalState:"
+ "setMetricCounter:"
+ "setMetricsTransformer:"
+ "setPrimaryResidentUpdatedSource:"
+ "setRemoteMessageID:"
+ "setRequiredResponse:"
+ "setRunningMode:"
+ "setTimer:"
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
+ "timer"
+ "timerDidFire:"
+ "transformInvokeCommandExpectationMetric:"
+ "transformMetrics"
+ "unregisterCommandPath:"
+ "updateControllerConfigMetricForHome:remoteMessageID:"
+ "userInfo"
+ "v24@0:8@\"HMFTimer\"16"
+ "v24@0:8@\"HMMLogEvent\"16"
+ "v32@0:8@\"MTRDeviceController\"16@\"MTRCommissioneeInfo\"24"
+ "v32@0:8q16@24"
+ "v36@0:8q16B24@28"
+ "v60@0:8@16@24i32@36@?44@?52"
+ "v60@0:8@16i24@28@36@?44@?52"
+ "waitForAttributeValues:timeout:queue:completion:"
+ "writeAttributeMetricForDevice:homeID:clientType:endpointID:clusterID:attributeID:timedWrite:remoteMessageID:"
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
- "%@ Cannot find controller for UUID %@ in %lu controllers - returning first available controller"
- "%@ Cannot find device controller for client %@ nodeID %@"
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
- "Tq,V_currentRunningMode"
- "_currentRunningMode"
- "_queryHomeRunningModeFromDelegateForHomeUUID:"
- "_remoteMode"
- "_runningModeForHomeUUID:runningModeChanged:"
- "_sendMessageToHomeWithID:messageType:pbCodable:errorBlock:replyBlock:"
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
- "firstObject"
- "initMetricWithName:device:homeID:remoteMode:"
- "initWithController:entityIdentifier:"
- "invokeCommandMetricForDevice:homeID:endpointID:clusterID:commandID:timedInvoke:remoteMode:"
- "isRemoteMode"
- "sendControllerMessageToHomeWithID:controllerMessageType:queryRequestValue:errorBlock:replyBlock:"
- "sendDeviceMessageToNodeWithID:homeID:deviceNodeMessageType:errorBlock:replyBlock:"
- "sendMessageToHomeWithID:messageType:pbCodable:errorBlock:replyBlock:"
- "setCurrentRunningMode:"
- "setRemoteMode:"
- "stateChangedMetricForDevice:homeID:state:remoteMode:"
- "v40@0:8@16@24@?32"
- "v52@0:8@16@24i32@?36@?44"
- "v52@0:8@16i24@28@?36@?44"
- "writeAttributeMetricForDevice:homeID:endpointID:clusterID:attributeID:timedWrite:remoteMode:"

```
