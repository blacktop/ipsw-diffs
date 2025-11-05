## MatterPlugin

> `/System/Library/PrivateFrameworks/MatterPlugin.framework/Versions/A/MatterPlugin`

```diff

-28.4.2.0.0
-  __TEXT.__text: 0x3d17c
-  __TEXT.__auth_stubs: 0x4b0
-  __TEXT.__objc_methlist: 0x3718
-  __TEXT.__const: 0xc8
-  __TEXT.__cstring: 0xac0
-  __TEXT.__oslogstring: 0x41e8
-  __TEXT.__gcc_except_tab: 0x1cb8
-  __TEXT.__unwind_info: 0xf98
-  __TEXT.__objc_classname: 0x7c4
-  __TEXT.__objc_methname: 0x5fff
-  __TEXT.__objc_methtype: 0x12bb
-  __TEXT.__objc_stubs: 0x4bc0
-  __DATA_CONST.__got: 0x358
-  __DATA_CONST.__const: 0x150
-  __DATA_CONST.__objc_classlist: 0x1c0
-  __DATA_CONST.__objc_protolist: 0x68
+49.5.14.0.0
+  __TEXT.__text: 0x4bb38
+  __TEXT.__auth_stubs: 0x5d0
+  __TEXT.__objc_methlist: 0x46d4
+  __TEXT.__const: 0xf0
+  __TEXT.__cstring: 0x11fd
+  __TEXT.__oslogstring: 0x5421
+  __TEXT.__gcc_except_tab: 0x1d28
+  __TEXT.__unwind_info: 0x11a0
+  __TEXT.__objc_classname: 0x9a2
+  __TEXT.__objc_methname: 0x7671
+  __TEXT.__objc_methtype: 0x1547
+  __TEXT.__objc_stubs: 0x59c0
+  __DATA_CONST.__got: 0x460
+  __DATA_CONST.__const: 0x210
+  __DATA_CONST.__objc_classlist: 0x218
+  __DATA_CONST.__objc_catlist: 0x10
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1688
+  __DATA_CONST.__objc_selrefs: 0x1b48
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x158
+  __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x268
-  __AUTH_CONST.__const: 0x870
-  __AUTH_CONST.__cfstring: 0x1000
-  __AUTH_CONST.__objc_const: 0x5c30
-  __AUTH_CONST.__objc_intobj: 0x318
+  __AUTH_CONST.__auth_got: 0x2f8
+  __AUTH_CONST.__const: 0x9d0
+  __AUTH_CONST.__cfstring: 0x18c0
+  __AUTH_CONST.__objc_const: 0x6790
+  __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0x1180
-  __DATA.__objc_ivar: 0x2d4
-  __DATA.__data: 0x4e0
-  __DATA.__bss: 0xc0
+  __AUTH.__objc_data: 0x14f0
+  __DATA.__objc_ivar: 0x36c
+  __DATA.__data: 0x600
+  __DATA.__bss: 0xf0
+  __DATA.__common: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Matter.framework/Versions/A/Matter
+  - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/PrivateFrameworks/HMFoundation.framework/Versions/A/HMFoundation
   - /System/Library/PrivateFrameworks/HomeKitMetrics.framework/Versions/A/HomeKitMetrics
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 01555039-6B76-3876-9548-D4077079CA7A
-  Functions: 1382
-  Symbols:   2985
-  CStrings:  1817
+  UUID: 61C3281A-CBEA-309E-8CC8-5A744EB51756
+  Functions: 1642
+  Symbols:   3570
+  CStrings:  2249
 
Symbols:
+ +[MTRDeviceController(PairingStateManagement) swizzlePrewarm]
+ +[MTRDeviceController(PairingStateManagement) swizzlePrewarm].cold.1
+ +[MTRDeviceControllerFactory(PairingStateManagement) swizzlePrewarm]
+ +[MTRDeviceControllerFactory(PairingStateManagement) swizzlePrewarm].cold.1
+ +[MTRPlugin sharedInstance].cold.1
+ +[MTRPluginAttributeReportMetric attributeReportMetricForDevice:homeID:attributeReport:remoteMessageID:]
+ +[MTRPluginBulkReadAttributeMetric bulkReadAttributeMetricForDevice:homeID:remoteMessageID:]
+ +[MTRPluginClientConnection clientConnectionQueue].cold.1
+ +[MTRPluginClientManager sharedInstance].cold.1
+ +[MTRPluginDeviceActiveMetric deviceActiveMetricForDevice:homeID:remoteMessageID:]
+ +[MTRPluginDeviceCachePrimedMetric deviceCachePrimedMetricForDevice:homeID:remoteMessageID:]
+ +[MTRPluginDeviceConfigChangedMetric deviceConfigChangedMetricForDevice:homeID:remoteMessageID:]
+ +[MTRPluginDeviceControllerRegistry sharedInstance].cold.1
+ +[MTRPluginDeviceInternalStateUpdatedMetric deviceInternalStateUpdatedForDevice:homeID:remoteMessageID:]
+ +[MTRPluginDownloadDiagnosticLogMetric downloadDiagnosticMetricForDevice:homeID:clientType:logType:remoteMessageID:]
+ +[MTRPluginEventReportMetric eventReportMetricForDevice:homeID:eventReport:remoteMessageID:]
+ +[MTRPluginInvokeCommandExpectationMetric invokeCommandExpectationMetricForMetric:]
+ +[MTRPluginInvokeCommandMetric invokeBatchCommandMetricForDevice:homeID:clientType:commandPath:commandFields:remoteMessageID:]
+ +[MTRPluginInvokeCommandMetric invokeCommandMetricForDevice:homeID:clientType:endpointID:clusterID:commandID:commandFields:expectedValues:expectedValueInterval:timedInvoke:remoteMessageID:]
+ +[MTRPluginLocalClient localDispatchQueue].cold.1
+ +[MTRPluginMetric numberValueFromDataValueDictionary:]
+ +[MTRPluginMetricsCollector sharedInstance].cold.1
+ +[MTRPluginPBMCommandWithRequiredResponse(Helpers) commandWithRequiredResponse:]
+ +[MTRPluginPBMCommandWithRequiredResponse(Helpers) commandWithRequiredResponseFromMessage:]
+ +[MTRPluginPBMCommandWithRequiredResponses commandWithRequiredResponseValueType]
+ +[MTRPluginPBMCommandWithRequiredResponses(Helpers) commandWithRequiredResponses:]
+ +[MTRPluginPBMCommandWithRequiredResponses(Helpers) commandWithRequiredResponsesFromMessage:]
+ +[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage commandWithRequiredResponsesValueType]
+ +[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage(Helpers) _convertArray:]
+ +[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage(Helpers) deviceNodeInvokeBatchCommandMessageFromMessage:]
+ +[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage(Helpers) deviceNodeInvokeBatchCommandMessageWithNodeID:commands:]
+ +[MTRPluginProtobufOverModernTransport sharedInstance].cold.1
+ +[MTRPluginRVCCleanModeMetric commandPath]
+ +[MTRPluginRVCCleanModeMetric transformInvokeCommandExpectationMetric:]
+ +[MTRPluginRVCOperationalStateMetric commandPaths]
+ +[MTRPluginRVCOperationalStateMetric transformInvokeCommandExpectationMetric:]
+ +[MTRPluginRVCRunModeMetric commandPath]
+ +[MTRPluginRVCRunModeMetric transformInvokeCommandExpectationMetric:]
+ +[MTRPluginResidentServer sharedInstance].cold.1
+ +[MTRPluginServer serverWorkQueue]
+ +[MTRPluginServer serverWorkQueue].cold.1
+ +[MTRPluginServer sharedInstance].cold.1
+ +[MTRPluginServiceAreaMetric commandPaths]
+ +[MTRPluginServiceAreaMetric transformInvokeCommandExpectationMetric:]
+ +[MTRPluginStateChangedMetric stateChangedMetricForDevice:homeID:state:remoteMessageID:]
+ +[MTRPluginThirdPartyExclusions attributeReadDisallowedOverXPCWithEndpointID:clusterID:attribute:isPrivatelyEntitled:].cold.1
+ +[MTRPluginUpdateControllerConfigMetric updateControllerConfigMetricForHome:remoteMessageID:]
+ +[MTRPluginWriteAttributeMetric writeAttributeMetricForDevice:homeID:clientType:endpointID:clusterID:attributeID:timedWrite:remoteMessageID:]
+ -[MTRDeviceController(PairingStateManagement) __plugin__preWarmCommissioningSession]
+ -[MTRDeviceController(PairingStateManagement) __plugin__setupCommissioningSessionWithPayload:newNodeID:error:]
+ -[MTRDeviceControllerEntity initWithController:entityIdentifier:runningMode:]
+ -[MTRDeviceControllerEntity runningMode]
+ -[MTRDeviceControllerEntity setRunningMode:]
+ -[MTRDeviceControllerFactory(PairingStateManagement) __plugin__preWarmCommissioningSession]
+ -[MTRPlugin _pairingStartedNotification:]
+ -[MTRPlugin _pairingStoppedNotification:]
+ -[MTRPluginAttributeReportMetric .cxx_destruct]
+ -[MTRPluginAttributeReportMetric additionalCoreAnalyticsEventDictionary]
+ -[MTRPluginAttributeReportMetric attributePath]
+ -[MTRPluginAttributeReportMetric attributeReport]
+ -[MTRPluginAttributeReportMetric copyWithZone:]
+ -[MTRPluginAttributeReportMetric hash]
+ -[MTRPluginAttributeReportMetric isEqual:]
+ -[MTRPluginAttributeReportMetric setAttributePath:]
+ -[MTRPluginAttributeReportMetric setAttributeReport:]
+ -[MTRPluginAttributeReportMetric submitMetric]
+ -[MTRPluginClient clientType]
+ -[MTRPluginClient controllerUUID]
+ -[MTRPluginClient deviceController:deleteNodeID:]
+ -[MTRPluginClient deviceController:getNodesWithStoredDataWithReply:]
+ -[MTRPluginClient deviceController:nodeID:invokeCommands:completion:]
+ -[MTRPluginClient setClientType:]
+ -[MTRPluginClient setControllerUUID:]
+ -[MTRPluginClient xpcClientConnectionQueue]
+ -[MTRPluginClientConnection _assignHomeUUIDIfUnassigned:]
+ -[MTRPluginClientConnection deviceController:nodeID:downloadLogOfType:timeout:completion:].cold.1
+ -[MTRPluginClientConnection deviceController:nodeID:getDeviceCachePrimedWithReply:].cold.1
+ -[MTRPluginClientConnection deviceController:nodeID:getEstimatedStartTimeWithReply:].cold.1
+ -[MTRPluginClientConnection deviceController:nodeID:getEstimatedSubscriptionLatencyWithReply:].cold.1
+ -[MTRPluginClientConnection deviceController:nodeID:getStateWithReply:].cold.1
+ -[MTRPluginClientConnection deviceController:nodeID:invokeCommandWithEndpointID:clusterID:commandID:commandFields:expectedValues:expectedValueInterval:timedInvokeTimeout:serverSideProcessingTimeout:completion:].cold.1
+ -[MTRPluginClientConnection deviceController:nodeID:invokeCommands:completion:]
+ -[MTRPluginClientConnection deviceController:nodeID:invokeCommands:completion:].cold.1
+ -[MTRPluginClientConnection deviceController:nodeID:openCommissioningWindowWithSetupPasscode:discriminator:duration:completion:].cold.1
+ -[MTRPluginClientConnection deviceController:nodeID:readAttributePaths:withReply:].cold.1
+ -[MTRPluginClientConnection deviceController:nodeID:readAttributeWithEndpointID:clusterID:attributeID:params:withReply:].cold.1
+ -[MTRPluginClientConnection deviceController:nodeID:writeAttributeWithEndpointID:clusterID:attributeID:value:expectedValueInterval:timedWriteTimeout:].cold.1
+ -[MTRPluginClientConnection deviceController:updateControllerConfiguration:].cold.1
+ -[MTRPluginClientManager isPluginClientLowestHash:]
+ -[MTRPluginDeviceControllerRegistry _forceUpdateRunningModeForController:]
+ -[MTRPluginDeviceControllerRegistry _queryAndUpdateRunningModeForHomeUUID:]
+ -[MTRPluginDeviceControllerRegistry _resumeControllerForPotentialPairing:]
+ -[MTRPluginDeviceControllerRegistry _runningModeChanged:forHomeUUID:]
+ -[MTRPluginDeviceControllerRegistry _runningModeForUUID:]
+ -[MTRPluginDeviceControllerRegistry _runningModeForUUID:].cold.1
+ -[MTRPluginDeviceControllerRegistry _updateRunningMode:forceUpdateControllerConfiguration:forHomeUUID:]
+ -[MTRPluginDeviceControllerRegistry _updateRunningModeForAllControllers]
+ -[MTRPluginDeviceControllerRegistry _updateRunningModeOfAllClientsForHome:]
+ -[MTRPluginDeviceControllerRegistry _updateSuspendedStateBasedOnRunningMode:]
+ -[MTRPluginDeviceControllerRegistry devicesChangedForController:]
+ -[MTRPluginDownloadDiagnosticLogMetric clientType]
+ -[MTRPluginDownloadDiagnosticLogMetric setClientType:]
+ -[MTRPluginEventReportMetric .cxx_destruct]
+ -[MTRPluginEventReportMetric additionalCoreAnalyticsEventDictionary]
+ -[MTRPluginEventReportMetric copyWithZone:]
+ -[MTRPluginEventReportMetric eventPath]
+ -[MTRPluginEventReportMetric eventReport]
+ -[MTRPluginEventReportMetric hash]
+ -[MTRPluginEventReportMetric isEqual:]
+ -[MTRPluginEventReportMetric setEventPath:]
+ -[MTRPluginEventReportMetric setEventReport:]
+ -[MTRPluginEventReportMetric submitMetric]
+ -[MTRPluginInvokeCommandExpectationMetric .cxx_destruct]
+ -[MTRPluginInvokeCommandExpectationMetric additionalCoreAnalyticsEventDictionary]
+ -[MTRPluginInvokeCommandExpectationMetric invokeCommandMetric]
+ -[MTRPluginInvokeCommandExpectationMetric remoteMessageID]
+ -[MTRPluginInvokeCommandExpectationMetric setInvokeCommandMetric:]
+ -[MTRPluginInvokeCommandExpectationMetric setRemoteMessageID:]
+ -[MTRPluginInvokeCommandMetric attributeValueWaiter]
+ -[MTRPluginInvokeCommandMetric clientType]
+ -[MTRPluginInvokeCommandMetric commandFields]
+ -[MTRPluginInvokeCommandMetric expectedValueInterval]
+ -[MTRPluginInvokeCommandMetric expectedValues]
+ -[MTRPluginInvokeCommandMetric isBatchCommand]
+ -[MTRPluginInvokeCommandMetric isDeviceAtExpectedState]
+ -[MTRPluginInvokeCommandMetric setAttributeValueWaiter:]
+ -[MTRPluginInvokeCommandMetric setBatchCommand:]
+ -[MTRPluginInvokeCommandMetric setClientType:]
+ -[MTRPluginInvokeCommandMetric setCommandFields:]
+ -[MTRPluginInvokeCommandMetric setDeviceAtExpectedState:]
+ -[MTRPluginInvokeCommandMetric setExpectedValueInterval:]
+ -[MTRPluginInvokeCommandMetric setExpectedValues:]
+ -[MTRPluginLocalClient _deviceForControllerUUID:nodeID:requestedViaDelegate:]
+ -[MTRPluginLocalClient _deviceForControllerUUID:nodeID:requestedViaDelegate:].cold.1
+ -[MTRPluginLocalClient _registerDevice:addedViaDelegate:]
+ -[MTRPluginLocalClient deviceController:deleteNodeID:]
+ -[MTRPluginLocalClient deviceController:getNodesWithStoredDataWithReply:]
+ -[MTRPluginLocalClient deviceController:nodeID:invokeCommands:completion:]
+ -[MTRPluginLocalClient setTemporarilyRegisteredNodeIDs:]
+ -[MTRPluginLocalClient setTemporaryDeviceCleanupSource:]
+ -[MTRPluginLocalClient temporarilyRegisteredNodeIDs]
+ -[MTRPluginLocalClient temporaryDeviceCleanupSource]
+ -[MTRPluginMetric count]
+ -[MTRPluginMetric initMetricWithName:device:homeID:remoteMessageID:]
+ -[MTRPluginMetric initMetricWithName:sourceMetric:]
+ -[MTRPluginMetric remoteMessageID]
+ -[MTRPluginMetric setCount:]
+ -[MTRPluginMetric setRemoteMessageID:]
+ -[MTRPluginMetricsCollector countMetric:]
+ -[MTRPluginMetricsCollector metricCounter]
+ -[MTRPluginMetricsCollector setMetricCounter:]
+ -[MTRPluginMetricsCollector setTimer:]
+ -[MTRPluginMetricsCollector setTransformMetrics:]
+ -[MTRPluginMetricsCollector timerDidFire:]
+ -[MTRPluginMetricsCollector timer]
+ -[MTRPluginMetricsCollector transformMetrics]
+ -[MTRPluginMetricsObserver .cxx_destruct]
+ -[MTRPluginMetricsObserver didReceiveEventFromDispatcher:]
+ -[MTRPluginMetricsObserver init]
+ -[MTRPluginMetricsObserver metricsTransformer]
+ -[MTRPluginMetricsObserver setMetricsTransformer:]
+ -[MTRPluginMetricsTransformer .cxx_destruct]
+ -[MTRPluginMetricsTransformer commandPathRegistry]
+ -[MTRPluginMetricsTransformer dispatchInvokeCommandExpectationMetric:]
+ -[MTRPluginMetricsTransformer init]
+ -[MTRPluginMetricsTransformer registerCommandPath:class:]
+ -[MTRPluginMetricsTransformer setCommandPathRegistry:]
+ -[MTRPluginMetricsTransformer unregisterCommandPath:]
+ -[MTRPluginPBMCommandWithRequiredResponse .cxx_destruct]
+ -[MTRPluginPBMCommandWithRequiredResponse commandFields]
+ -[MTRPluginPBMCommandWithRequiredResponse commandPath]
+ -[MTRPluginPBMCommandWithRequiredResponse copyTo:]
+ -[MTRPluginPBMCommandWithRequiredResponse copyWithZone:]
+ -[MTRPluginPBMCommandWithRequiredResponse description]
+ -[MTRPluginPBMCommandWithRequiredResponse dictionaryRepresentation]
+ -[MTRPluginPBMCommandWithRequiredResponse hasCommandFields]
+ -[MTRPluginPBMCommandWithRequiredResponse hasCommandPath]
+ -[MTRPluginPBMCommandWithRequiredResponse hasRequiredResponse]
+ -[MTRPluginPBMCommandWithRequiredResponse hash]
+ -[MTRPluginPBMCommandWithRequiredResponse isEqual:]
+ -[MTRPluginPBMCommandWithRequiredResponse mergeFrom:]
+ -[MTRPluginPBMCommandWithRequiredResponse readFrom:]
+ -[MTRPluginPBMCommandWithRequiredResponse requiredResponse]
+ -[MTRPluginPBMCommandWithRequiredResponse setCommandFields:]
+ -[MTRPluginPBMCommandWithRequiredResponse setCommandPath:]
+ -[MTRPluginPBMCommandWithRequiredResponse setRequiredResponse:]
+ -[MTRPluginPBMCommandWithRequiredResponse writeTo:]
+ -[MTRPluginPBMCommandWithRequiredResponse(Helpers) commandWithRequiredResponse]
+ -[MTRPluginPBMCommandWithRequiredResponse(Helpers) isValid]
+ -[MTRPluginPBMCommandWithRequiredResponses .cxx_destruct]
+ -[MTRPluginPBMCommandWithRequiredResponses addCommandWithRequiredResponseValue:]
+ -[MTRPluginPBMCommandWithRequiredResponses clearCommandWithRequiredResponseValues]
+ -[MTRPluginPBMCommandWithRequiredResponses commandWithRequiredResponseValueAtIndex:]
+ -[MTRPluginPBMCommandWithRequiredResponses commandWithRequiredResponseValuesCount]
+ -[MTRPluginPBMCommandWithRequiredResponses commandWithRequiredResponseValues]
+ -[MTRPluginPBMCommandWithRequiredResponses copyTo:]
+ -[MTRPluginPBMCommandWithRequiredResponses copyWithZone:]
+ -[MTRPluginPBMCommandWithRequiredResponses description]
+ -[MTRPluginPBMCommandWithRequiredResponses dictionaryRepresentation]
+ -[MTRPluginPBMCommandWithRequiredResponses hash]
+ -[MTRPluginPBMCommandWithRequiredResponses isEqual:]
+ -[MTRPluginPBMCommandWithRequiredResponses mergeFrom:]
+ -[MTRPluginPBMCommandWithRequiredResponses readFrom:]
+ -[MTRPluginPBMCommandWithRequiredResponses setCommandWithRequiredResponseValues:]
+ -[MTRPluginPBMCommandWithRequiredResponses writeTo:]
+ -[MTRPluginPBMCommandWithRequiredResponses(Helpers) commandWithRequiredResponses]
+ -[MTRPluginPBMCommandWithRequiredResponses(Helpers) isValid]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage .cxx_destruct]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage addCommandWithRequiredResponsesValue:]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage clearCommandWithRequiredResponsesValues]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage commandWithRequiredResponsesValueAtIndex:]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage commandWithRequiredResponsesValuesCount]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage commandWithRequiredResponsesValues]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage copyTo:]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage copyWithZone:]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage description]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage dictionaryRepresentation]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage hasHeader]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage hasNode]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage hash]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage header]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage isEqual:]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage mergeFrom:]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage node]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage readFrom:]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage setCommandWithRequiredResponsesValues:]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage setHeader:]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage setNode:]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage writeTo:]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage(Helpers) commands]
+ -[MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage(Helpers) isValid]
+ -[MTRPluginProtobufMessageDispatcher handleNewSessionSetupForMessage:transport:errorBlock:].cold.1
+ -[MTRPluginRVCCleanModeMetric .cxx_destruct]
+ -[MTRPluginRVCCleanModeMetric additionalCoreAnalyticsEventDictionary]
+ -[MTRPluginRVCCleanModeMetric invokeCommandMetric]
+ -[MTRPluginRVCCleanModeMetric setInvokeCommandMetric:]
+ -[MTRPluginRVCOperationalStateMetric .cxx_destruct]
+ -[MTRPluginRVCOperationalStateMetric additionalCoreAnalyticsEventDictionary]
+ -[MTRPluginRVCOperationalStateMetric invokeCommandMetric]
+ -[MTRPluginRVCOperationalStateMetric setInvokeCommandMetric:]
+ -[MTRPluginRVCRunModeMetric .cxx_destruct]
+ -[MTRPluginRVCRunModeMetric additionalCoreAnalyticsEventDictionary]
+ -[MTRPluginRVCRunModeMetric invokeCommandMetric]
+ -[MTRPluginRVCRunModeMetric setInvokeCommandMetric:]
+ -[MTRPluginRemoteClient _closeRemoteServerSession]
+ -[MTRPluginRemoteClient description]
+ -[MTRPluginRemoteClient deviceController:deleteNodeID:]
+ -[MTRPluginRemoteClient deviceController:getNodesWithStoredDataWithReply:]
+ -[MTRPluginRemoteClient deviceController:nodeID:invokeCommands:completion:]
+ -[MTRPluginRemoteClient isSuspended]
+ -[MTRPluginRemoteClient resume]
+ -[MTRPluginRemoteClient sendControllerMessageToHomeWithID:controllerMessageType:queryRequestValue:metric:errorBlock:replyBlock:]
+ -[MTRPluginRemoteClient sendDeviceMessageToNodeWithID:homeID:deviceNodeMessageType:metric:errorBlock:replyBlock:]
+ -[MTRPluginRemoteClient sendMessageToHomeWithID:messageType:pbCodable:metrics:errorBlock:replyBlock:]
+ -[MTRPluginRemoteClient setSuspended:]
+ -[MTRPluginRemoteClient suspend]
+ -[MTRPluginResidentClientSession _sendMessageToHomeWithID:messageType:pbCodable:metric:errorBlock:replyBlock:]
+ -[MTRPluginResidentClientSession deviceBecameActiveSource]
+ -[MTRPluginResidentClientSession lastKnownInternalState]
+ -[MTRPluginResidentClientSession messageTransport:handleDeviceInvokeBatchCommand:]
+ -[MTRPluginResidentClientSession setDeviceBecameActiveSource:]
+ -[MTRPluginResidentClientSession setLastKnownInternalState:]
+ -[MTRPluginServer _registerForResidentChangedNotifications]
+ -[MTRPluginServer _safeQueryRunningModeFromDelegateForHomeUUID:]
+ -[MTRPluginServer _unsafeQueryRunningModeFromDelegateForHomeUUID:]
+ -[MTRPluginServer _unsafeQueryRunningModeFromDelegateForHomeUUID:].cold.1
+ -[MTRPluginServer dealloc]
+ -[MTRPluginServer handlePrimaryResidentUpdateNotification:]
+ -[MTRPluginServer homesWithPrimaryResidentUpdated]
+ -[MTRPluginServer primaryResidentUpdatedSource]
+ -[MTRPluginServer setHomesWithPrimaryResidentUpdated:]
+ -[MTRPluginServer setPrimaryResidentUpdatedSource:]
+ -[MTRPluginServiceAreaMetric .cxx_destruct]
+ -[MTRPluginServiceAreaMetric additionalCoreAnalyticsEventDictionary]
+ -[MTRPluginServiceAreaMetric invokeCommandMetric]
+ -[MTRPluginServiceAreaMetric setInvokeCommandMetric:]
+ -[MTRPluginWriteAttributeMetric clientType]
+ -[MTRPluginWriteAttributeMetric setClientType:]
+ GCC_except_table1
+ GCC_except_table106
+ GCC_except_table107
+ GCC_except_table112
+ GCC_except_table113
+ GCC_except_table114
+ GCC_except_table115
+ GCC_except_table26
+ GCC_except_table30
+ GCC_except_table40
+ GCC_except_table44
+ GCC_except_table50
+ GCC_except_table61
+ GCC_except_table63
+ GCC_except_table64
+ GCC_except_table65
+ GCC_except_table66
+ GCC_except_table67
+ MTRPluginForceRemoteControl.cold.1
+ MTRPluginMaxActiveClientSessions.cold.1
+ MTRUpdateRunningModeForController.cold.1
+ OBJC_IVAR_$_MTRDeviceControllerEntity._runningMode
+ OBJC_IVAR_$_MTRPluginAttributeReportMetric._attributePath
+ OBJC_IVAR_$_MTRPluginAttributeReportMetric._attributeReport
+ OBJC_IVAR_$_MTRPluginClient._clientType
+ OBJC_IVAR_$_MTRPluginClient._controllerUUID
+ OBJC_IVAR_$_MTRPluginDownloadDiagnosticLogMetric._clientType
+ OBJC_IVAR_$_MTRPluginEventReportMetric._eventPath
+ OBJC_IVAR_$_MTRPluginEventReportMetric._eventReport
+ OBJC_IVAR_$_MTRPluginInvokeCommandExpectationMetric._invokeCommandMetric
+ OBJC_IVAR_$_MTRPluginInvokeCommandMetric._attributeValueWaiter
+ OBJC_IVAR_$_MTRPluginInvokeCommandMetric._batchCommand
+ OBJC_IVAR_$_MTRPluginInvokeCommandMetric._clientType
+ OBJC_IVAR_$_MTRPluginInvokeCommandMetric._commandFields
+ OBJC_IVAR_$_MTRPluginInvokeCommandMetric._deviceAtExpectedState
+ OBJC_IVAR_$_MTRPluginInvokeCommandMetric._expectedValueInterval
+ OBJC_IVAR_$_MTRPluginInvokeCommandMetric._expectedValues
+ OBJC_IVAR_$_MTRPluginLocalClient._temporarilyRegisteredNodeIDs
+ OBJC_IVAR_$_MTRPluginLocalClient._temporaryDeviceCleanupSource
+ OBJC_IVAR_$_MTRPluginMetric._count
+ OBJC_IVAR_$_MTRPluginMetric._remoteMessageID
+ OBJC_IVAR_$_MTRPluginMetricsCollector._metricCounter
+ OBJC_IVAR_$_MTRPluginMetricsCollector._timer
+ OBJC_IVAR_$_MTRPluginMetricsCollector._transformMetrics
+ OBJC_IVAR_$_MTRPluginMetricsObserver._metricsTransformer
+ OBJC_IVAR_$_MTRPluginMetricsTransformer._commandPathRegistry
+ OBJC_IVAR_$_MTRPluginPBMCommandWithRequiredResponse._commandFields
+ OBJC_IVAR_$_MTRPluginPBMCommandWithRequiredResponse._commandPath
+ OBJC_IVAR_$_MTRPluginPBMCommandWithRequiredResponse._requiredResponse
+ OBJC_IVAR_$_MTRPluginPBMCommandWithRequiredResponses._commandWithRequiredResponseValues
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage._commandWithRequiredResponsesValues
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage._header
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage._node
+ OBJC_IVAR_$_MTRPluginRVCCleanModeMetric._invokeCommandMetric
+ OBJC_IVAR_$_MTRPluginRVCOperationalStateMetric._invokeCommandMetric
+ OBJC_IVAR_$_MTRPluginRVCRunModeMetric._invokeCommandMetric
+ OBJC_IVAR_$_MTRPluginRemoteClient._suspended
+ OBJC_IVAR_$_MTRPluginResidentClientSession._deviceBecameActiveSource
+ OBJC_IVAR_$_MTRPluginResidentClientSession._lastKnownInternalState
+ OBJC_IVAR_$_MTRPluginServer._homesWithPrimaryResidentUpdated
+ OBJC_IVAR_$_MTRPluginServer._primaryResidentUpdatedSource
+ OBJC_IVAR_$_MTRPluginServiceAreaMetric._invokeCommandMetric
+ OBJC_IVAR_$_MTRPluginWriteAttributeMetric._clientType
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
+ _MTRPluginIsPlatformBinaryFromAuditToken
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
+ __100-[MTRPluginProtobufMessageDispatcher invokeMessageHandlersForReceiver:message:transport:errorBlock:]_block_invoke.58
+ __100-[MTRPluginProtobufMessageDispatcher invokeMessageHandlersForReceiver:message:transport:errorBlock:]_block_invoke.58.cold.1
+ __100-[MTRPluginProtobufMessageDispatcher invokeMessageHandlersForReceiver:message:transport:errorBlock:]_block_invoke.61
+ __101-[MTRPluginRemoteClient sendMessageToHomeWithID:messageType:pbCodable:metrics:errorBlock:replyBlock:]_block_invoke.cold.1
+ __110-[MTRPluginResidentClientSession _sendMessageToHomeWithID:messageType:pbCodable:metric:errorBlock:replyBlock:]_block_invoke.cold.1
+ __110-[MTRPluginResidentClientSession _sendMessageToHomeWithID:messageType:pbCodable:metric:errorBlock:replyBlock:]_block_invoke.cold.2
+ __110-[MTRPluginResidentClientSession _sendMessageToHomeWithID:messageType:pbCodable:metric:errorBlock:replyBlock:]_block_invoke.cold.3
+ __116-[MTRPluginRemoteClient deviceController:nodeID:readAttributeWithEndpointID:clusterID:attributeID:params:withReply:]_block_invoke.71
+ __120-[MTRPluginClientConnection deviceController:nodeID:readAttributeWithEndpointID:clusterID:attributeID:params:withReply:]_block_invoke.155
+ __128-[MTRPluginClientConnection deviceController:nodeID:openCommissioningWindowWithSetupPasscode:discriminator:duration:completion:]_block_invoke.167
+ __205-[MTRPluginLocalClient deviceController:nodeID:invokeCommandWithEndpointID:clusterID:commandID:commandFields:expectedValues:expectedValueInterval:timedInvokeTimeout:serverSideProcessingTimeout:completion:]_block_invoke.37
+ __206-[MTRPluginRemoteClient deviceController:nodeID:invokeCommandWithEndpointID:clusterID:commandID:commandFields:expectedValues:expectedValueInterval:timedInvokeTimeout:serverSideProcessingTimeout:completion:]_block_invoke.86
+ __52-[MTRPluginResidentClientSession deviceCachePrimed:]_block_invoke.128
+ __54-[MTRPluginResidentClientSession device:stateChanged:]_block_invoke.122
+ __57-[MTRPluginLocalClient _registerDevice:addedViaDelegate:]_block_invoke.26
+ __61-[MTRPluginResidentClientSession device:receivedEventReport:]_block_invoke.127
+ __61-[MTRPluginResidentClientSession deviceConfigurationChanged:]_block_invoke.129
+ __62-[MTRPluginResidentClientSession device:internalStateUpdated:]_block_invoke.148
+ __65-[MTRPluginResidentClientSession device:receivedAttributeReport:]_block_invoke.126
+ __67-[MTRPluginRemoteClient deviceController:nodeID:getStateWithReply:]_block_invoke.64
+ __71-[MTRPluginClientConnection deviceController:nodeID:getStateWithReply:]_block_invoke.150
+ __71-[MTRPluginClientConnection deviceController:nodeID:getStateWithReply:]_block_invoke.151
+ __72-[MTRPluginRemoteClient deviceController:updateControllerConfiguration:]_block_invoke.61
+ __74-[MTRPluginLocalClient deviceController:nodeID:invokeCommands:completion:]_block_invoke.43
+ __75-[MTRPluginRemoteClient deviceController:nodeID:invokeCommands:completion:]_block_invoke.90
+ __75-[MTRPluginRemoteClient deviceController:nodeID:invokeCommands:completion:]_block_invoke.cold.1
+ __78-[MTRPluginRemoteClient deviceController:nodeID:readAttributePaths:withReply:]_block_invoke.79
+ __79-[MTRPluginRemoteClient deviceController:nodeID:getDeviceCachePrimedWithReply:]_block_invoke.66
+ __80-[MTRPluginRemoteClient deviceController:nodeID:getEstimatedStartTimeWithReply:]_block_invoke.67
+ __82-[MTRPluginClientConnection deviceController:nodeID:readAttributePaths:withReply:]_block_invoke.156
+ __83-[MTRPluginClientConnection deviceController:nodeID:getDeviceCachePrimedWithReply:]_block_invoke.152
+ __84-[MTRPluginClientConnection deviceController:nodeID:getEstimatedStartTimeWithReply:]_block_invoke.153
+ __85-[MTRPluginLocalClient deviceController:nodeID:downloadLogOfType:timeout:completion:]_block_invoke.47
+ __86-[MTRPluginRemoteClient deviceController:nodeID:downloadLogOfType:timeout:completion:]_block_invoke.93
+ __90-[MTRPluginClientConnection deviceController:nodeID:downloadLogOfType:timeout:completion:]_block_invoke.168
+ __90-[MTRPluginRemoteClient deviceController:nodeID:getEstimatedSubscriptionLatencyWithReply:]_block_invoke.68
+ __94-[MTRPluginClientConnection deviceController:nodeID:getEstimatedSubscriptionLatencyWithReply:]_block_invoke.154
+ __HMFNilUUIDBytes
+ __MTRValidateUserInfo
+ __OBJC_$_CATEGORY_CLASS_METHODS_MTRDeviceControllerFactory_$_PairingStateManagement
+ __OBJC_$_CATEGORY_CLASS_METHODS_MTRDeviceController_$_PairingStateManagement
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_MTRDeviceControllerFactory_$_PairingStateManagement
+ __OBJC_$_CATEGORY_INSTANCE_METHODS_MTRDeviceController_$_PairingStateManagement
+ __OBJC_$_CATEGORY_MTRDeviceControllerFactory_$_PairingStateManagement
+ __OBJC_$_CATEGORY_MTRDeviceController_$_PairingStateManagement
+ __OBJC_$_CLASS_METHODS_MTRPluginInvokeCommandExpectationMetric
+ __OBJC_$_CLASS_METHODS_MTRPluginMetric
+ __OBJC_$_CLASS_METHODS_MTRPluginPBMCommandWithRequiredResponse(Helpers)
+ __OBJC_$_CLASS_METHODS_MTRPluginPBMCommandWithRequiredResponses(Helpers)
+ __OBJC_$_CLASS_METHODS_MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage(Helpers)
+ __OBJC_$_CLASS_METHODS_MTRPluginRVCCleanModeMetric
+ __OBJC_$_CLASS_METHODS_MTRPluginRVCOperationalStateMetric
+ __OBJC_$_CLASS_METHODS_MTRPluginRVCRunModeMetric
+ __OBJC_$_CLASS_METHODS_MTRPluginServiceAreaMetric
+ __OBJC_$_CLASS_METHODS_MTRPluginUpdateControllerConfigMetric
+ __OBJC_$_INSTANCE_METHODS_MTRPluginAttributeReportMetric
+ __OBJC_$_INSTANCE_METHODS_MTRPluginEventReportMetric
+ __OBJC_$_INSTANCE_METHODS_MTRPluginInvokeCommandExpectationMetric
+ __OBJC_$_INSTANCE_METHODS_MTRPluginMetricsObserver
+ __OBJC_$_INSTANCE_METHODS_MTRPluginMetricsTransformer
+ __OBJC_$_INSTANCE_METHODS_MTRPluginPBMCommandWithRequiredResponse(Helpers)
+ __OBJC_$_INSTANCE_METHODS_MTRPluginPBMCommandWithRequiredResponses(Helpers)
+ __OBJC_$_INSTANCE_METHODS_MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage(Helpers)
+ __OBJC_$_INSTANCE_METHODS_MTRPluginRVCCleanModeMetric
+ __OBJC_$_INSTANCE_METHODS_MTRPluginRVCOperationalStateMetric
+ __OBJC_$_INSTANCE_METHODS_MTRPluginRVCRunModeMetric
+ __OBJC_$_INSTANCE_METHODS_MTRPluginServiceAreaMetric
+ __OBJC_$_INSTANCE_VARIABLES_MTRPluginAttributeReportMetric
+ __OBJC_$_INSTANCE_VARIABLES_MTRPluginEventReportMetric
+ __OBJC_$_INSTANCE_VARIABLES_MTRPluginInvokeCommandExpectationMetric
+ __OBJC_$_INSTANCE_VARIABLES_MTRPluginMetricsObserver
+ __OBJC_$_INSTANCE_VARIABLES_MTRPluginMetricsTransformer
+ __OBJC_$_INSTANCE_VARIABLES_MTRPluginPBMCommandWithRequiredResponse
+ __OBJC_$_INSTANCE_VARIABLES_MTRPluginPBMCommandWithRequiredResponses
+ __OBJC_$_INSTANCE_VARIABLES_MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage
+ __OBJC_$_INSTANCE_VARIABLES_MTRPluginRVCCleanModeMetric
+ __OBJC_$_INSTANCE_VARIABLES_MTRPluginRVCOperationalStateMetric
+ __OBJC_$_INSTANCE_VARIABLES_MTRPluginRVCRunModeMetric
+ __OBJC_$_INSTANCE_VARIABLES_MTRPluginServiceAreaMetric
+ __OBJC_$_PROP_LIST_MTRPluginAttributeReportMetric
+ __OBJC_$_PROP_LIST_MTRPluginEventReportMetric
+ __OBJC_$_PROP_LIST_MTRPluginInvokeCommandExpectationMetric
+ __OBJC_$_PROP_LIST_MTRPluginMetricsObserver
+ __OBJC_$_PROP_LIST_MTRPluginMetricsTransformer
+ __OBJC_$_PROP_LIST_MTRPluginProtobufMessageTransportDelegate
+ __OBJC_$_PROP_LIST_MTRPluginRVCCleanModeMetric
+ __OBJC_$_PROP_LIST_MTRPluginRVCOperationalStateMetric
+ __OBJC_$_PROP_LIST_MTRPluginRVCRunModeMetric
+ __OBJC_$_PROP_LIST_MTRPluginServiceAreaMetric
+ __OBJC_$_PROTOCOL_CLASS_METHODS_MTRPluginMetricTransformDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMFTimerDelegate
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMMLogEventObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMFTimerDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMMLogEventObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_MTRPluginMetricTransformDelegate
+ __OBJC_$_PROTOCOL_REFS_HMFTimerDelegate
+ __OBJC_$_PROTOCOL_REFS_HMMLogEventObserver
+ __OBJC_$_PROTOCOL_REFS_MTRPluginMetricTransformDelegate
+ __OBJC_CLASS_PROTOCOLS_$_MTRPluginDeviceControllerRegistry
+ __OBJC_CLASS_PROTOCOLS_$_MTRPluginMetricsCollector
+ __OBJC_CLASS_PROTOCOLS_$_MTRPluginMetricsObserver
+ __OBJC_CLASS_PROTOCOLS_$_MTRPluginPBMCommandWithRequiredResponse
+ __OBJC_CLASS_PROTOCOLS_$_MTRPluginPBMCommandWithRequiredResponses
+ __OBJC_CLASS_PROTOCOLS_$_MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage
+ __OBJC_CLASS_PROTOCOLS_$_MTRPluginRVCCleanModeMetric
+ __OBJC_CLASS_PROTOCOLS_$_MTRPluginRVCOperationalStateMetric
+ __OBJC_CLASS_PROTOCOLS_$_MTRPluginRVCRunModeMetric
+ __OBJC_CLASS_PROTOCOLS_$_MTRPluginServiceAreaMetric
+ __OBJC_CLASS_RO_$_MTRPluginInvokeCommandExpectationMetric
+ __OBJC_CLASS_RO_$_MTRPluginMetricsObserver
+ __OBJC_CLASS_RO_$_MTRPluginMetricsTransformer
+ __OBJC_CLASS_RO_$_MTRPluginPBMCommandWithRequiredResponse
+ __OBJC_CLASS_RO_$_MTRPluginPBMCommandWithRequiredResponses
+ __OBJC_CLASS_RO_$_MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage
+ __OBJC_CLASS_RO_$_MTRPluginRVCCleanModeMetric
+ __OBJC_CLASS_RO_$_MTRPluginRVCOperationalStateMetric
+ __OBJC_CLASS_RO_$_MTRPluginRVCRunModeMetric
+ __OBJC_CLASS_RO_$_MTRPluginServiceAreaMetric
+ __OBJC_CLASS_RO_$_MTRPluginUpdateControllerConfigMetric
+ __OBJC_LABEL_PROTOCOL_$_HMFTimerDelegate
+ __OBJC_LABEL_PROTOCOL_$_HMMLogEventObserver
+ __OBJC_LABEL_PROTOCOL_$_MTRPluginMetricTransformDelegate
+ __OBJC_METACLASS_RO_$_MTRPluginInvokeCommandExpectationMetric
+ __OBJC_METACLASS_RO_$_MTRPluginMetricsObserver
+ __OBJC_METACLASS_RO_$_MTRPluginMetricsTransformer
+ __OBJC_METACLASS_RO_$_MTRPluginPBMCommandWithRequiredResponse
+ __OBJC_METACLASS_RO_$_MTRPluginPBMCommandWithRequiredResponses
+ __OBJC_METACLASS_RO_$_MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage
+ __OBJC_METACLASS_RO_$_MTRPluginRVCCleanModeMetric
+ __OBJC_METACLASS_RO_$_MTRPluginRVCOperationalStateMetric
+ __OBJC_METACLASS_RO_$_MTRPluginRVCRunModeMetric
+ __OBJC_METACLASS_RO_$_MTRPluginServiceAreaMetric
+ __OBJC_METACLASS_RO_$_MTRPluginUpdateControllerConfigMetric
+ __OBJC_PROTOCOL_$_HMFTimerDelegate
+ __OBJC_PROTOCOL_$_HMMLogEventObserver
+ __OBJC_PROTOCOL_$_MTRPluginMetricTransformDelegate
+ ___101-[MTRPluginRemoteClient sendMessageToHomeWithID:messageType:pbCodable:metrics:errorBlock:replyBlock:]_block_invoke
+ ___110-[MTRPluginResidentClientSession _sendMessageToHomeWithID:messageType:pbCodable:metric:errorBlock:replyBlock:]_block_invoke
+ ___189+[MTRPluginInvokeCommandMetric invokeCommandMetricForDevice:homeID:clientType:endpointID:clusterID:commandID:commandFields:expectedValues:expectedValueInterval:timedInvoke:remoteMessageID:]_block_invoke
+ ___34+[MTRPluginServer serverWorkQueue]_block_invoke
+ ___38-[MTRPluginClient runningModeChanged:]_block_invoke
+ ___43-[MTRPluginServer startWithDelegate:queue:]_block_invoke
+ ___54-[MTRPluginLocalClient deviceController:deleteNodeID:]_block_invoke
+ ___57-[MTRPluginLocalClient _registerDevice:addedViaDelegate:]_block_invoke
+ ___59-[MTRPluginServer handlePrimaryResidentUpdateNotification:]_block_invoke
+ ___59-[MTRPluginServer handlePrimaryResidentUpdateNotification:]_block_invoke_2
+ ___61+[MTRDeviceController(PairingStateManagement) swizzlePrewarm]_block_invoke
+ ___61-[MTRPluginServer runningModeForHomeUUID:runningModeChanged:]_block_invoke
+ ___64-[MTRPluginServer _safeQueryRunningModeFromDelegateForHomeUUID:]_block_invoke
+ ___68+[MTRDeviceControllerFactory(PairingStateManagement) swizzlePrewarm]_block_invoke
+ ___73-[MTRPluginLocalClient deviceController:getNodesWithStoredDataWithReply:]_block_invoke
+ ___74-[MTRPluginLocalClient deviceController:nodeID:invokeCommands:completion:]_block_invoke
+ ___75-[MTRPluginRemoteClient deviceController:nodeID:invokeCommands:completion:]_block_invoke
+ ___79-[MTRPluginClientConnection deviceController:nodeID:invokeCommands:completion:]_block_invoke
+ ___82-[MTRPluginResidentClientSession messageTransport:handleDeviceInvokeBatchCommand:]_block_invoke
+ ___MTRSetPotentialPairing_block_invoke
+ ___block_descriptor_128_e8_32s40s48s56s64s72s80s88s96s104s112s120bs_e5_v8?0l
+ ___block_descriptor_40_e8_32s_e17_v16?0"NSError"8l
+ ___block_descriptor_48_e8_32s40r_e5_v8?0l
+ ___block_descriptor_49_e8_32s40s_e5_v8?0l
+ ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSError"8l
+ ___block_descriptor_72_e8_32s40s48s56s64bs_e29_v24?0"NSArray"8"NSError"16l
+ ___block_descriptor_80_e8_32s40s48s56s64s72r_e5_v8?0l
+ ___copy_helper_block_e8_32s40r
+ ___copy_helper_block_e8_32s40s48s56s64s72r
+ ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120b
+ ___destroy_helper_block_e8_32s40r
+ ___destroy_helper_block_e8_32s40s48s56s64s72r
+ ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s
+ ___kCFBooleanFalse
+ ___kCFBooleanTrue
+ ___matterPluginLogInitialize_block_invoke
+ __block_literal_global.18
+ __block_literal_global.24
+ __block_literal_global.36
+ __block_literal_global.78
+ __block_literal_global.87
+ _attributeValueFromExpectedAttributeReport
+ _audit_token_to_pid
+ _class_getInstanceMethod
+ _class_replaceMethod
+ _commandValueFromCommandFields
+ _csops_audittoken
+ _getpid
+ _kCFAllocatorDefault
+ _matterPluginLogInitialize
+ _matterPluginLog_default
+ _method_getImplementation
+ _method_getTypeEncoding
+ _objc_getAssociatedObject
+ _objc_msgSend$__plugin__preWarmCommissioningSession
+ _objc_msgSend$__plugin__setupCommissioningSessionWithPayload:newNodeID:error:
+ _objc_msgSend$_assignHomeUUIDIfUnassigned:
+ _objc_msgSend$_closeRemoteServerSession
+ _objc_msgSend$_deviceForControllerUUID:nodeID:requestedViaDelegate:
+ _objc_msgSend$_forceUpdateRunningModeForController:
+ _objc_msgSend$_queryAndUpdateRunningModeForHomeUUID:
+ _objc_msgSend$_queue
+ _objc_msgSend$_registerDevice:addedViaDelegate:
+ _objc_msgSend$_registerForResidentChangedNotifications
+ _objc_msgSend$_runningModeChanged:forHomeUUID:
+ _objc_msgSend$_runningModeForUUID:
+ _objc_msgSend$_safeQueryRunningModeFromDelegateForHomeUUID:
+ _objc_msgSend$_sendMessageToHomeWithID:messageType:pbCodable:metric:errorBlock:replyBlock:
+ _objc_msgSend$_unsafeQueryRunningModeFromDelegateForHomeUUID:
+ _objc_msgSend$_updateRunningMode:forceUpdateControllerConfiguration:forHomeUUID:
+ _objc_msgSend$_updateRunningModeForAllControllers
+ _objc_msgSend$_updateRunningModeOfAllClientsForHome:
+ _objc_msgSend$addCommandWithRequiredResponseValue:
+ _objc_msgSend$addCommandWithRequiredResponsesValue:
+ _objc_msgSend$addObserver:forEventClasses:
+ _objc_msgSend$attributeReport
+ _objc_msgSend$attributeReportMetricForDevice:homeID:attributeReport:remoteMessageID:
+ _objc_msgSend$auditToken
+ _objc_msgSend$bulkReadAttributeMetricForDevice:homeID:remoteMessageID:
+ _objc_msgSend$clearCommandWithRequiredResponseValues
+ _objc_msgSend$clearCommandWithRequiredResponsesValues
+ _objc_msgSend$clientType
+ _objc_msgSend$commandPathRegistry
+ _objc_msgSend$commandPaths
+ _objc_msgSend$commandWithRequiredResponse
+ _objc_msgSend$commandWithRequiredResponse:
+ _objc_msgSend$commandWithRequiredResponseValueAtIndex:
+ _objc_msgSend$commandWithRequiredResponseValues
+ _objc_msgSend$commandWithRequiredResponseValuesCount
+ _objc_msgSend$commandWithRequiredResponses
+ _objc_msgSend$commandWithRequiredResponses:
+ _objc_msgSend$commandWithRequiredResponsesValueAtIndex:
+ _objc_msgSend$commandWithRequiredResponsesValues
+ _objc_msgSend$commandWithRequiredResponsesValuesCount
+ _objc_msgSend$commands
+ _objc_msgSend$controllerUUID
+ _objc_msgSend$countMetric:
+ _objc_msgSend$deviceActiveMetricForDevice:homeID:remoteMessageID:
+ _objc_msgSend$deviceBecameActiveSource
+ _objc_msgSend$deviceCachePrimedMetricForDevice:homeID:remoteMessageID:
+ _objc_msgSend$deviceConfigChangedMetricForDevice:homeID:remoteMessageID:
+ _objc_msgSend$deviceController:deleteNodeID:
+ _objc_msgSend$deviceController:getNodesWithStoredDataWithReply:
+ _objc_msgSend$deviceController:nodeID:invokeCommands:completion:
+ _objc_msgSend$deviceInternalStateUpdatedForDevice:homeID:remoteMessageID:
+ _objc_msgSend$deviceNodeInvokeBatchCommandMessageFromMessage:
+ _objc_msgSend$deviceNodeInvokeBatchCommandMessageWithNodeID:commands:
+ _objc_msgSend$devices
+ _objc_msgSend$dictionaryWithDictionary:
+ _objc_msgSend$dispatchInvokeCommandExpectationMetric:
+ _objc_msgSend$downloadDiagnosticMetricForDevice:homeID:clientType:logType:remoteMessageID:
+ _objc_msgSend$durationMilliseconds
+ _objc_msgSend$eventReport
+ _objc_msgSend$eventReportMetricForDevice:homeID:eventReport:remoteMessageID:
+ _objc_msgSend$forgetDeviceWithNodeID:
+ _objc_msgSend$getUUIDBytes:
+ _objc_msgSend$hasCommandFields
+ _objc_msgSend$hasPrefix:
+ _objc_msgSend$hasRequiredResponse
+ _objc_msgSend$homesWithPrimaryResidentUpdated
+ _objc_msgSend$initMetricWithName:device:homeID:remoteMessageID:
+ _objc_msgSend$initMetricWithName:sourceMetric:
+ _objc_msgSend$initWithController:entityIdentifier:runningMode:
+ _objc_msgSend$initWithPath:commandFields:requiredResponse:
+ _objc_msgSend$initWithTimeInterval:options:
+ _objc_msgSend$invokeBatchCommandMetricForDevice:homeID:clientType:commandPath:commandFields:remoteMessageID:
+ _objc_msgSend$invokeCommandExpectationMetricForMetric:
+ _objc_msgSend$invokeCommandMetric
+ _objc_msgSend$invokeCommandMetricForDevice:homeID:clientType:endpointID:clusterID:commandID:commandFields:expectedValues:expectedValueInterval:timedInvoke:remoteMessageID:
+ _objc_msgSend$invokeCommands:queue:completion:
+ _objc_msgSend$isBatchCommand
+ _objc_msgSend$isPluginClientLowestHash:
+ _objc_msgSend$lastKnownInternalState
+ _objc_msgSend$length
+ _objc_msgSend$markEndTime
+ _objc_msgSend$member:
+ _objc_msgSend$metricCounter
+ _objc_msgSend$metricsTransformer
+ _objc_msgSend$networkCommissioningFeatures
+ _objc_msgSend$nodesWithStoredData
+ _objc_msgSend$numberValueFromDataValueDictionary:
+ _objc_msgSend$path
+ _objc_msgSend$postNotificationName:object:
+ _objc_msgSend$primaryResidentUpdatedSource
+ _objc_msgSend$registerCommandPath:class:
+ _objc_msgSend$remoteMessageID
+ _objc_msgSend$removeObserver:
+ _objc_msgSend$requiredResponse
+ _objc_msgSend$runningMode
+ _objc_msgSend$runningModeForHomeUUID:runningModeChanged:
+ _objc_msgSend$sendControllerMessageToHomeWithID:controllerMessageType:queryRequestValue:metric:errorBlock:replyBlock:
+ _objc_msgSend$sendDeviceMessageToNodeWithID:homeID:deviceNodeMessageType:metric:errorBlock:replyBlock:
+ _objc_msgSend$sendMessageToHomeWithID:messageType:pbCodable:metrics:errorBlock:replyBlock:
+ _objc_msgSend$serverWorkQueue
+ _objc_msgSend$setAttributeReport:
+ _objc_msgSend$setAttributeValueWaiter:
+ _objc_msgSend$setBatchCommand:
+ _objc_msgSend$setClientType:
+ _objc_msgSend$setCommandPathRegistry:
+ _objc_msgSend$setCommandWithRequiredResponsesValues:
+ _objc_msgSend$setControllerUUID:
+ _objc_msgSend$setCount:
+ _objc_msgSend$setDeviceBecameActiveSource:
+ _objc_msgSend$setError:
+ _objc_msgSend$setEventPath:
+ _objc_msgSend$setEventReport:
+ _objc_msgSend$setHomesWithPrimaryResidentUpdated:
+ _objc_msgSend$setInvokeCommandMetric:
+ _objc_msgSend$setLastKnownInternalState:
+ _objc_msgSend$setMetricCounter:
+ _objc_msgSend$setMetricsTransformer:
+ _objc_msgSend$setPrimaryResidentUpdatedSource:
+ _objc_msgSend$setRemoteMessageID:
+ _objc_msgSend$setRequiredResponse:
+ _objc_msgSend$setRunningMode:
+ _objc_msgSend$setTemporarilyRegisteredNodeIDs:
+ _objc_msgSend$setTemporaryDeviceCleanupSource:
+ _objc_msgSend$setTimer:
+ _objc_msgSend$setTransformMetrics:
+ _objc_msgSend$startTime
+ _objc_msgSend$stateChangedMetricForDevice:homeID:state:remoteMessageID:
+ _objc_msgSend$strongToStrongObjectsMapTable
+ _objc_msgSend$submitMetric
+ _objc_msgSend$swizzlePrewarm
+ _objc_msgSend$temporarilyRegisteredNodeIDs
+ _objc_msgSend$temporaryDeviceCleanupSource
+ _objc_msgSend$timer
+ _objc_msgSend$transformInvokeCommandExpectationMetric:
+ _objc_msgSend$transformMetrics
+ _objc_msgSend$updateControllerConfigMetricForHome:remoteMessageID:
+ _objc_msgSend$userInfo
+ _objc_msgSend$waitForAttributeValues:timeout:queue:completion:
+ _objc_msgSend$writeAttributeMetricForDevice:homeID:clientType:endpointID:clusterID:attributeID:timedWrite:remoteMessageID:
+ _objc_msgSend$xpcClientConnectionQueue
+ _objc_opt_self
+ _objc_retainBlock
+ _objc_setAssociatedObject
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _os_log_create
+ _sMTRPluginPairingStatusChangedSource
+ matterPluginLogInitialize.cold.1
+ matterPluginLogInitialize.onceToken
+ matterPluginLogInitialize.subsystem
+ serverWorkQueue.predicateNAME
+ serverWorkQueue.sSingleWorkerQueue
+ swizzlePrewarm.onceToken
+ swizzlePrewarm.onceToken.85
- +[MTRPluginAttributeReportMetric attributeReportMetricForDevice:homeID:remoteMode:]
- +[MTRPluginBulkReadAttributeMetric bulkReadAttributeMetricForDevice:homeID:remoteMode:]
- +[MTRPluginDeviceActiveMetric deviceActiveMetricForDevice:homeID:remoteMode:]
- +[MTRPluginDeviceCachePrimedMetric deviceCachePrimedMetricForDevice:homeID:remoteMode:]
- +[MTRPluginDeviceConfigChangedMetric deviceConfigChangedMetricForDevice:homeID:remoteMode:]
- +[MTRPluginDeviceInternalStateUpdatedMetric deviceInternalStateUpdatedForDevice:homeID:remoteMode:]
- +[MTRPluginDownloadDiagnosticLogMetric downloadDiagnosticMetricForDevice:homeID:logType:remoteMode:]
- +[MTRPluginEventReportMetric eventReportMetricForDevice:homeID:remoteMode:]
- +[MTRPluginInvokeCommandMetric invokeCommandMetricForDevice:homeID:endpointID:clusterID:commandID:timedInvoke:remoteMode:]
- +[MTRPluginStateChangedMetric stateChangedMetricForDevice:homeID:state:remoteMode:]
- +[MTRPluginWriteAttributeMetric writeAttributeMetricForDevice:homeID:endpointID:clusterID:attributeID:timedWrite:remoteMode:]
- -[MTRDeviceControllerEntity initWithController:entityIdentifier:]
- -[MTRPluginClient _updateSuspendedStateBasedOnRunningMode]
- -[MTRPluginClient currentRunningMode]
- -[MTRPluginClient registeredNodeIDs]
- -[MTRPluginClient setCurrentRunningMode:]
- -[MTRPluginClient setRegisteredNodeIDs:]
- -[MTRPluginClientConnection _runningModeForHomeUUID:runningModeChanged:]
- -[MTRPluginInvokeCommandMetric coreAnalyticsEventOptions]
- -[MTRPluginLocalClient _deviceForControllerUUID:nodeID:]
- -[MTRPluginLocalClient _registerDevice:]
- -[MTRPluginLocalClient isSuspended]
- -[MTRPluginLocalClient runningModeChanged:]
- -[MTRPluginLocalClient setSuspended:]
- -[MTRPluginMetric initMetricWithName:device:homeID:remoteMode:]
- -[MTRPluginMetric isRemoteMode]
- -[MTRPluginMetric setRemoteMode:]
- -[MTRPluginProtobufMessageDispatcher deregisterForRequestMessageWithType:forSessionID:].cold.1
- -[MTRPluginProtobufMessageDispatcher deregisterForRequestMessageWithType:forSessionID:].cold.2
- -[MTRPluginProtobufMessageDispatcher invokeMessageHandlersForReceiver:message:transport:errorBlock:].cold.1
- -[MTRPluginProtobufMessageDispatcher invokeMessageHandlersForReceiver:message:transport:errorBlock:].cold.2
- -[MTRPluginProtobufOverModernTransport _handleResponseWithPayload:error:forMessage:].cold.4
- -[MTRPluginProtobufOverModernTransport dispatchIncomingMessage:].cold.1
- -[MTRPluginProtobufOverModernTransport dispatchIncomingMessage:].cold.2
- -[MTRPluginRemoteClient sendControllerMessageToHomeWithID:controllerMessageType:queryRequestValue:errorBlock:replyBlock:]
- -[MTRPluginRemoteClient sendControllerMessageToHomeWithID:controllerMessageType:queryRequestValue:errorBlock:replyBlock:].cold.1
- -[MTRPluginRemoteClient sendDeviceMessageToNodeWithID:homeID:deviceNodeMessageType:errorBlock:replyBlock:]
- -[MTRPluginRemoteClient sendMessageToHomeWithID:messageType:pbCodable:errorBlock:replyBlock:]
- -[MTRPluginRemoteClient sendMessageToHomeWithID:messageType:pbCodable:errorBlock:replyBlock:].cold.1
- -[MTRPluginRemoteClient sendOnewayMessageToHomeWithID:messageType:pbCodable:].cold.1
- -[MTRPluginResidentClientSession _sendMessageToHomeWithID:messageType:pbCodable:errorBlock:replyBlock:]
- -[MTRPluginResidentClientSession _sendMessageToHomeWithID:messageType:pbCodable:errorBlock:replyBlock:].cold.1
- -[MTRPluginResidentClientSession _validateAndFindDeviceNodeForMessage:].cold.2
- -[MTRPluginResidentClientSession messageTransport:handleDeviceReadAttribute:].cold.3
- -[MTRPluginResidentClientSession messageTransport:handleDeviceReadMultipleAttributes:].cold.3
- -[MTRPluginResidentClientSession messageTransport:handleUpdateControllerConfig:].cold.2
- -[MTRPluginResidentServer _registerSessionForSessionID:incomingNewMessage:].cold.2
- -[MTRPluginServer _queryHomeRunningModeFromDelegateForHomeUUID:]
- GCC_except_table110
- GCC_except_table111
- GCC_except_table25
- GCC_except_table31
- GCC_except_table41
- GCC_except_table46
- GCC_except_table53
- GCC_except_table54
- GCC_except_table59
- GCC_except_table6
- GCC_except_table7
- OBJC_IVAR_$_MTRPluginClient._currentRunningMode
- OBJC_IVAR_$_MTRPluginClient._registeredNodeIDs
- OBJC_IVAR_$_MTRPluginLocalClient._suspended
- OBJC_IVAR_$_MTRPluginMetric._remoteMode
- _OUTLINED_FUNCTION_7
- __100-[MTRPluginProtobufMessageDispatcher invokeMessageHandlersForReceiver:message:transport:errorBlock:]_block_invoke.50
- __100-[MTRPluginProtobufMessageDispatcher invokeMessageHandlersForReceiver:message:transport:errorBlock:]_block_invoke.50.cold.1
- __100-[MTRPluginProtobufMessageDispatcher invokeMessageHandlersForReceiver:message:transport:errorBlock:]_block_invoke.53
- __103-[MTRPluginResidentClientSession _sendMessageToHomeWithID:messageType:pbCodable:errorBlock:replyBlock:]_block_invoke.cold.1
- __103-[MTRPluginResidentClientSession _sendMessageToHomeWithID:messageType:pbCodable:errorBlock:replyBlock:]_block_invoke.cold.2
- __103-[MTRPluginResidentClientSession _sendMessageToHomeWithID:messageType:pbCodable:errorBlock:replyBlock:]_block_invoke.cold.3
- __116-[MTRPluginRemoteClient deviceController:nodeID:readAttributeWithEndpointID:clusterID:attributeID:params:withReply:]_block_invoke.58
- __120-[MTRPluginClientConnection deviceController:nodeID:readAttributeWithEndpointID:clusterID:attributeID:params:withReply:]_block_invoke.139
- __128-[MTRPluginClientConnection deviceController:nodeID:openCommissioningWindowWithSetupPasscode:discriminator:duration:completion:]_block_invoke.151
- __205-[MTRPluginLocalClient deviceController:nodeID:invokeCommandWithEndpointID:clusterID:commandID:commandFields:expectedValues:expectedValueInterval:timedInvokeTimeout:serverSideProcessingTimeout:completion:]_block_invoke.21
- __206-[MTRPluginRemoteClient deviceController:nodeID:invokeCommandWithEndpointID:clusterID:commandID:commandFields:expectedValues:expectedValueInterval:timedInvokeTimeout:serverSideProcessingTimeout:completion:]_block_invoke.74
- __43-[MTRPluginLocalClient runningModeChanged:]_block_invoke.cold.1
- __52-[MTRPluginResidentClientSession deviceCachePrimed:]_block_invoke.122
- __53-[MTRPluginResidentClientSession deviceBecameActive:]_block_invoke.120
- __53-[MTRPluginResidentClientSession deviceBecameActive:]_block_invoke.cold.1
- __54-[MTRPluginResidentClientSession device:stateChanged:]_block_invoke.111
- __61-[MTRPluginResidentClientSession device:receivedEventReport:]_block_invoke.118
- __61-[MTRPluginResidentClientSession deviceConfigurationChanged:]_block_invoke.124
- __62-[MTRPluginResidentClientSession device:internalStateUpdated:]_block_invoke.126
- __65-[MTRPluginResidentClientSession device:receivedAttributeReport:]_block_invoke.116
- __67-[MTRPluginRemoteClient deviceController:nodeID:getStateWithReply:]_block_invoke.51
- __71-[MTRPluginClientConnection deviceController:nodeID:getStateWithReply:]_block_invoke.134
- __71-[MTRPluginClientConnection deviceController:nodeID:getStateWithReply:]_block_invoke.135
- __71-[MTRPluginLocalClient deviceController:updateControllerConfiguration:]_block_invoke.cold.1
- __72-[MTRPluginRemoteClient deviceController:updateControllerConfiguration:]_block_invoke.48
- __77-[MTRPluginResidentClientSession messageTransport:handleDeviceInvokeCommand:]_block_invoke.cold.1
- __78-[MTRPluginRemoteClient deviceController:nodeID:readAttributePaths:withReply:]_block_invoke.65
- __79-[MTRPluginRemoteClient deviceController:nodeID:getDeviceCachePrimedWithReply:]_block_invoke.52
- __79-[MTRPluginResidentClientSession messageTransport:handleDownloadDiagnosticLog:]_block_invoke.cold.1
- __80-[MTRPluginRemoteClient deviceController:nodeID:getEstimatedStartTimeWithReply:]_block_invoke.54
- __82-[MTRPluginClientConnection deviceController:nodeID:readAttributePaths:withReply:]_block_invoke.140
- __83-[MTRPluginClientConnection deviceController:nodeID:getDeviceCachePrimedWithReply:]_block_invoke.136
- __84-[MTRPluginClientConnection deviceController:nodeID:getEstimatedStartTimeWithReply:]_block_invoke.137
- __85-[MTRPluginLocalClient deviceController:nodeID:downloadLogOfType:timeout:completion:]_block_invoke.25
- __86-[MTRPluginRemoteClient deviceController:nodeID:downloadLogOfType:timeout:completion:]_block_invoke.77
- __90-[MTRPluginClientConnection deviceController:nodeID:downloadLogOfType:timeout:completion:]_block_invoke.152
- __90-[MTRPluginRemoteClient deviceController:nodeID:getEstimatedSubscriptionLatencyWithReply:]_block_invoke.55
- __93-[MTRPluginRemoteClient sendMessageToHomeWithID:messageType:pbCodable:errorBlock:replyBlock:]_block_invoke.cold.1
- __94-[MTRPluginClientConnection deviceController:nodeID:getEstimatedSubscriptionLatencyWithReply:]_block_invoke.138
- ___103-[MTRPluginResidentClientSession _sendMessageToHomeWithID:messageType:pbCodable:errorBlock:replyBlock:]_block_invoke
- ___40-[MTRPluginLocalClient _registerDevice:]_block_invoke
- ___43-[MTRPluginLocalClient runningModeChanged:]_block_invoke
- ___53-[MTRPluginResidentClientSession deviceBecameActive:]_block_invoke
- ___64-[MTRPluginServer _queryHomeRunningModeFromDelegateForHomeUUID:]_block_invoke
- ___93-[MTRPluginRemoteClient sendMessageToHomeWithID:messageType:pbCodable:errorBlock:replyBlock:]_block_invoke
- ___block_descriptor_136_e8_32s40s48s56s64s72s80s88s96s104s112s120s128bs_e5_v8?0l
- ___block_descriptor_48_e8_32s40s_e17_v16?0"NSError"8l
- ___block_descriptor_88_e8_32s40s48s56s64s72s80r_e5_v8?0l
- ___copy_helper_block_e8_32s40s48s56s64s72s80r
- ___copy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128b
- ___destroy_helper_block_e8_32s40s48s56s64s72s80r
- ___destroy_helper_block_e8_32s40s48s56s64s72s80s88s96s104s112s120s128s
- __block_literal_global.13
- __os_log_default
- _fmod
- _objc_msgSend$_deviceForControllerUUID:nodeID:
- _objc_msgSend$_queryHomeRunningModeFromDelegateForHomeUUID:
- _objc_msgSend$_registerDevice:
- _objc_msgSend$_runningModeForHomeUUID:runningModeChanged:
- _objc_msgSend$_sendMessageToHomeWithID:messageType:pbCodable:errorBlock:replyBlock:
- _objc_msgSend$_updateSuspendedStateBasedOnRunningMode
- _objc_msgSend$attributeReportMetricForDevice:homeID:remoteMode:
- _objc_msgSend$bulkReadAttributeMetricForDevice:homeID:remoteMode:
- _objc_msgSend$controllers
- _objc_msgSend$currentRunningMode
- _objc_msgSend$deviceActiveMetricForDevice:homeID:remoteMode:
- _objc_msgSend$deviceCachePrimedMetricForDevice:homeID:remoteMode:
- _objc_msgSend$deviceConfigChangedMetricForDevice:homeID:remoteMode:
- _objc_msgSend$deviceInternalStateUpdatedForDevice:homeID:remoteMode:
- _objc_msgSend$downloadDiagnosticMetricForDevice:homeID:logType:remoteMode:
- _objc_msgSend$eventReportMetricForDevice:homeID:remoteMode:
- _objc_msgSend$firstObject
- _objc_msgSend$initMetricWithName:device:homeID:remoteMode:
- _objc_msgSend$initWithController:entityIdentifier:
- _objc_msgSend$invokeCommandMetricForDevice:homeID:endpointID:clusterID:commandID:timedInvoke:remoteMode:
- _objc_msgSend$isRemoteMode
- _objc_msgSend$sendControllerMessageToHomeWithID:controllerMessageType:queryRequestValue:errorBlock:replyBlock:
- _objc_msgSend$sendDeviceMessageToNodeWithID:homeID:deviceNodeMessageType:errorBlock:replyBlock:
- _objc_msgSend$sendMessageToHomeWithID:messageType:pbCodable:errorBlock:replyBlock:
- _objc_msgSend$setCurrentRunningMode:
- _objc_msgSend$setRemoteMode:
- _objc_msgSend$stateChangedMetricForDevice:homeID:state:remoteMode:
- _objc_msgSend$writeAttributeMetricForDevice:homeID:endpointID:clusterID:attributeID:timedWrite:remoteMode:
CStrings:
+ "\v"
+ " => Assigning home UUID: %@ to connection: %@   controllerID: %@"
+ " => Device wasn't registered in temporary list, ignoring"
+ "!"
+ "%@  => *** Not cleaning up temporary device, as it's permanent now: %@"
+ "%@  => DOUBLE registering device (already registered): %@"
+ "%@  => registering device: %@ addedViaDelegate: %@"
+ "%@  => registering temporary device: %@ addedViaDelegate: %@"
+ "%@  => unregistering temporary device: %@"
+ "%@ <= Sending response %@ for incoming request HMFMessage (%@ : %{uuid_t}.16P)"
+ "%@ <= Sending response for incoming request HMFMessage (%@ : %{uuid_t}.16P) with error: %@"
+ "%@ => Done cleaning up temporary nodeIDs: %@"
+ "%@ Adding commandPath %@ with class %@, registry: %@"
+ "%@ Adding new session receiver delegate %@ for sessionID: %{uuid_t}.16P"
+ "%@ Attempting to add commandPath %@ with class %@, registry: %@"
+ "%@ Calling invokeHandler on delegate %p for session with identifier %{uuid_t}.16P for message: %@"
+ "%@ Cannot find controller for UUID %@ - returning unknown running mode, controller was not added to registry"
+ "%@ Cannot find controller for UUID %@ in %lu controllers - controller was not added to registry"
+ "%@ Cannot find device controller for client %@ nodeID %@ - controller was not added to registry"
+ "%@ Cleaning up temporary nodeIDs: %@  (permanent ones: %@)"
+ "%@ Deregistering selector for messageType: %@ on session: %{uuid_t}.16P"
+ "%@ Device controller delegate devices changed for controller UUID %@ devices count %lu"
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
+ "%@ Setting running mode for controller: %@ to local (forced pairing mode), unsuspending controller (devices count %lu)"
+ "%@ Setting running mode for controller: %@ to local, but no active devices, suspending controller (devices count %lu)"
+ "%@ Setting running mode for controller: %@ to local, resuming controller because we have active devices (devices count %lu)"
+ "%@ Setting running mode for controller: %@ to remote, suspending controller (devices count %lu)"
+ "%@ Setting running mode for controller: %@ to unknown, but no active devices, suspending controller (devices count %lu)"
+ "%@ Setting running mode for controller: %@ to unknown, resuming controller because we have active devices (devices count %lu)"
+ "%@ Successfully completed invokeBatchCommand with response: %@"
+ "%@ Suspended remote client"
+ "%@ Switching running mode from '%@' to '%@' for home %@"
+ "%@ Switching running mode to '%@' for home %@"
+ "%@ Tried to remove device controller, but wasn't present: %@"
+ "%@ Updating a controller configuration for home %@ update for running mode '%@' so the new endpoint has context: %@"
+ "%@ Updating running mode for all clients to '%@' for home %@"
+ "%@ Updating running mode for home %@ since primary resident updated with notification %@"
+ "%@ _forceUpdateRunningModeForController for controller %@"
+ "%@ _forceUpdateRunningModeForController found controller UUID %@ homeUUID %@ current running mode %@"
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
+ "<%@: %p xpc %p pid: %d, clientType: %@ registeredNodeIDs: %@>"
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
+ "T@\"NSMutableSet\",&,V_temporarilyRegisteredNodeIDs"
+ "T@\"NSNumber\",&,V_count"
+ "T@\"NSNumber\",&,V_expectedValueInterval"
+ "T@\"NSObject<OS_dispatch_source>\",&,V_deviceBecameActiveSource"
+ "T@\"NSObject<OS_dispatch_source>\",&,V_primaryResidentUpdatedSource"
+ "T@\"NSObject<OS_dispatch_source>\",&,V_temporaryDeviceCleanupSource"
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
+ "_deviceForControllerUUID:nodeID:requestedViaDelegate:"
+ "_eventPath"
+ "_eventReport"
+ "_forceUpdateRunningModeForController:"
+ "_homesWithPrimaryResidentUpdated"
+ "_invokeCommandMetric"
+ "_lastKnownInternalState"
+ "_metricCounter"
+ "_metricsTransformer"
+ "_pairingStartedNotification:"
+ "_pairingStoppedNotification:"
+ "_primaryResidentUpdatedSource"
+ "_queryAndUpdateRunningModeForHomeUUID:"
+ "_registerDevice:addedViaDelegate:"
+ "_registerForResidentChangedNotifications"
+ "_remoteMessageID"
+ "_requiredResponse"
+ "_resumeControllerForPotentialPairing:"
+ "_runningMode"
+ "_runningModeChanged:forHomeUUID:"
+ "_runningModeForUUID:"
+ "_safeQueryRunningModeFromDelegateForHomeUUID:"
+ "_sendMessageToHomeWithID:messageType:pbCodable:metric:errorBlock:replyBlock:"
+ "_temporarilyRegisteredNodeIDs"
+ "_temporaryDeviceCleanupSource"
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
+ "areaSkipped"
+ "areasSelected"
+ "assistant_service"
+ "attributeCounter"
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
+ "com.apple.application-identifier"
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
+ "devices"
+ "devicesChangedForController:"
+ "dictionaryWithDictionary:"
+ "didReceiveEventFromDispatcher:"
+ "dispatchInvokeCommandExpectationMetric:"
+ "downloadDiagnosticMetricForDevice:homeID:clientType:logType:remoteMessageID:"
+ "durationMilliseconds"
+ "durationMs"
+ "eventCounter"
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
+ "setTemporarilyRegisteredNodeIDs:"
+ "setTemporaryDeviceCleanupSource:"
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
+ "temporarilyRegisteredNodeIDs"
+ "temporaryDeviceCleanupSource"
+ "timer"
+ "timerDidFire:"
+ "transformInvokeCommandExpectationMetric:"
+ "transformMetrics"
+ "unregisterCommandPath:"
+ "updateControllerConfigMetricForHome:remoteMessageID:"
+ "userInfo"
+ "v24@0:8@\"HMFTimer\"16"
+ "v24@0:8@\"HMMLogEvent\"16"
+ "v24@0:8@\"MTRDeviceController\"16"
+ "v32@0:8@\"MTRDeviceController\"16@\"MTRCommissioneeInfo\"24"
+ "v32@0:8q16@24"
+ "v36@0:8q16B24@28"
+ "v60@0:8@16@24i32@36@?44@?52"
+ "v60@0:8@16i24@28@36@?44@?52"
+ "waitForAttributeValues:timeout:queue:completion:"
+ "writeAttributeMetricForDevice:homeID:clientType:endpointID:clusterID:attributeID:timedWrite:remoteMessageID:"
+ "xpcClientConnectionQueue"
- "\t"
- " *** Ignoring new home UUID: %@ for connection: %@, and invalidating"
- " => Assigning home UUID: %@ to connection: %@"
- "%@  => controller: %@ self.pluginClient.registeredNodeIDs: %@"
- "%@  => registering device: %@"
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
- "%@ Setting running mode for controller: %@ to local, unsuspending controller"
- "%@ Setting running mode for controller: %@ to remote, suspending controller"
- "%@ Setting running mode for controller: %@ to unknown, resuming controller"
- "%@ Successfully sent device became active"
- "%@ delegate denied access to operation: %ld for %@"
- "<%@: %p xpc %p pid: %d>"
- "@44@0:8@16@24@32B40"
- "@44@0:8@16@24Q32B40"
- "@44@0:8@16@24q32B40"
- "@64@0:8@16@24@32@40@48B56B60"
- "T@\"MTRDevice\",&,V_device"
- "TB,GisRemoteMode,V_remoteMode"
- "Tq,V_currentRunningMode"
- "_currentRunningMode"
- "_deviceForControllerUUID:nodeID:"
- "_queryHomeRunningModeFromDelegateForHomeUUID:"
- "_registerDevice:"
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
