## MatterPlugin

> `/System/Library/PrivateFrameworks/MatterPlugin.framework/MatterPlugin`

```diff

-21.0.0.0.0
-  __TEXT.__text: 0x340cc
-  __TEXT.__auth_stubs: 0x620
-  __TEXT.__objc_methlist: 0x3480
-  __TEXT.__const: 0xc0
-  __TEXT.__gcc_except_tab: 0x1c2c
-  __TEXT.__oslogstring: 0x40d1
-  __TEXT.__cstring: 0x8bd
-  __TEXT.__unwind_info: 0xf50
-  __TEXT.__objc_classname: 0x699
-  __TEXT.__objc_methname: 0x5511
-  __TEXT.__objc_methtype: 0x1279
-  __TEXT.__objc_stubs: 0x4460
-  __DATA_CONST.__got: 0x2a8
-  __DATA_CONST.__const: 0x568
-  __DATA_CONST.__objc_classlist: 0x170
-  __DATA_CONST.__objc_protolist: 0x70
+28.3.1.0.0
+  __TEXT.__text: 0x35570
+  __TEXT.__auth_stubs: 0x6a0
+  __TEXT.__objc_methlist: 0x332c
+  __TEXT.__const: 0xc8
+  __TEXT.__cstring: 0x83c
+  __TEXT.__oslogstring: 0x411e
+  __TEXT.__gcc_except_tab: 0x19e8
+  __TEXT.__unwind_info: 0xee0
+  __TEXT.__objc_classname: 0x601
+  __TEXT.__objc_methname: 0x565b
+  __TEXT.__objc_methtype: 0x1246
+  __TEXT.__objc_stubs: 0x44a0
+  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__const: 0x670
+  __DATA_CONST.__objc_classlist: 0x150
+  __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1488
+  __DATA_CONST.__objc_selrefs: 0x14a8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA_CONST.__objc_superrefs: 0x160
+  __DATA_CONST.__objc_superrefs: 0x148
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x320
-  __AUTH_CONST.__const: 0x120
+  __AUTH_CONST.__auth_got: 0x360
+  __AUTH_CONST.__const: 0x160
   __AUTH_CONST.__cfstring: 0xd40
-  __AUTH_CONST.__objc_const: 0x53e8
-  __AUTH_CONST.__objc_intobj: 0x348
+  __AUTH_CONST.__objc_const: 0x4f20
+  __AUTH_CONST.__objc_intobj: 0x318
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0xe60
-  __DATA.__objc_ivar: 0x2b0
-  __DATA.__data: 0x540
-  __DATA.__bss: 0x90
+  __AUTH.__objc_data: 0xcd0
+  __DATA.__objc_ivar: 0x290
+  __DATA.__data: 0x480
+  __DATA.__bss: 0x50
+  __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Matter.framework/Matter

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1336
-  Symbols:   1674
-  CStrings:  1582
+  Functions: 1345
+  Symbols:   1693
+  CStrings:  1560
 
Symbols:
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeDownloadDiagnosticLog._has
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeDownloadDiagnosticLog._header
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeDownloadDiagnosticLog._logType
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeDownloadDiagnosticLog._node
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeDownloadDiagnosticLog._timeoutInterval
+ OBJC_IVAR_$_MTRPluginPBMVariableValueResponseMessage._checkinRequested
+ OBJC_IVAR_$_MTRPluginPBMVariableValueResponseMessage._has
+ _MTRBufferedExecutionBlock
+ _MTRDeviceControllerRegistrationNodeIDKey
+ _MTRDeviceControllerRegistrationNodeIDsKey
+ _MTRPluginPBMDeviceNodeDownloadDiagnosticLogReadFrom
+ _NSFilePosixPermissions
+ _NSTemporaryDirectory
+ _OBJC_CLASS_$_MTRPluginPBMDeviceNodeDownloadDiagnosticLog
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_METACLASS_$_MTRPluginPBMDeviceNodeDownloadDiagnosticLog
+ __dispatch_source_type_timer
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _getuid
+ _objc_autorelease
+ _objc_retain_x5
- OBJC_IVAR_$_MTRPluginPBMHeader._controllerID
- _OBJC_CLASS_$_HMFTimer
- _OBJC_CLASS_$_MTRPluginLocalDeviceDelegateProxy
- _OBJC_CLASS_$_MTRPluginLocalDispatch
- _OBJC_CLASS_$_MTRPluginReadAttributeWorkItem
- _OBJC_CLASS_$_MTRPluginTimedWatermarkQueue
- _OBJC_CLASS_$_MTRPluginWorkItem
- _OBJC_METACLASS_$_MTRPluginLocalDeviceDelegateProxy
- _OBJC_METACLASS_$_MTRPluginLocalDispatch
- _OBJC_METACLASS_$_MTRPluginReadAttributeWorkItem
- _OBJC_METACLASS_$_MTRPluginTimedWatermarkQueue
- _OBJC_METACLASS_$_MTRPluginWorkItem
- _objc_unsafeClaimAutoreleasedReturnValue
CStrings:
+ "\x01\x11!"
+ "\r"
+ "\x11\x11"
+ "\x13\x11"
+ "%!@(MISSING)  => controller: %!@(MISSING) register device: %!@(MISSING)"
+ "%!@(MISSING)  => controller: %!@(MISSING) register nodeID: %!@(MISSING)"
+ "%!@(MISSING)  => controller: %!@(MISSING) self.pluginClient.registeredNodeIDs: %!@(MISSING)"
+ "%!@(MISSING)  => controller: %!@(MISSING) self.registeredNodeIDs: %!@(MISSING)"
+ "%!@(MISSING)  => controller: %!@(MISSING) unregister device: %!@(MISSING)"
+ "%!@(MISSING)  => controller: %!@(MISSING) unregister nodeIDToUnregister: %!@(MISSING)"
+ "%!@(MISSING) => Received new incoming protobuf message: %!@(MISSING) without checkin, requesting piggyback checkin as part of response"
+ "%!@(MISSING) => Received responseValue for message %!@(MISSING) that is requesting a checkin, scheduling a checkin"
+ "%!@(MISSING) Adding Client %!@(MISSING) for xpc connection %!@(MISSING) queue: %!@(MISSING)"
+ "%!@(MISSING) Attempting to send message %!@(MISSING) to home hub and homeID: %!@(MISSING)"
+ "%!@(MISSING) Attempting to send message %!@(MISSING) to homeID: %!@(MISSING), destination: %!{(MISSING)private}@"
+ "%!@(MISSING) Attempting to send one way message %!@(MISSING) to home hub and homeID: %!@(MISSING)"
+ "%!@(MISSING) Failed to complete download diagnostic log with error: %!@(MISSING)"
+ "%!@(MISSING) Failed to convert response payload into data format"
+ "%!@(MISSING) Failed to create diagnostic log directory"
+ "%!@(MISSING) Failed to create diagnostic log file %!@(MISSING)"
+ "%!@(MISSING) Failed to download diagnostic log of type %!d(MISSING) for nodeID: %!@(MISSING), with error %!@(MISSING), for message %!@(MISSING)"
+ "%!@(MISSING) Failed to send message type %!d(MISSING) (%!@(MISSING)) to homeID: %!@(MISSING), destination: %!{(MISSING)private}@ as it is invalid"
+ "%!@(MISSING) Failed to send message type %!d(MISSING) for (%!@(MISSING)) to home hub for home %!@(MISSING) since it is invalid"
+ "%!@(MISSING) Failed to send one way message type %!d(MISSING) for (%!@(MISSING)) to home hub for home %!@(MISSING) since it is invalid"
+ "%!@(MISSING) Forwarding remote request to downloadLogOfType: (%!d(MISSING)), timeout (%!l(MISSING)f), from device nodeID (%!@(MISSING)) for controllerID %!@(MISSING)"
+ "%!@(MISSING) Forwarding remote request to updateControllerConfiguration: %!@(MISSING) state: %!@(MISSING)"
+ "%!@(MISSING) Got updateControllerConfiguration %!@(MISSING)"
+ "%!@(MISSING) Invoking download diagnostic log of type (%!d(MISSING)), timeout (%!l(MISSING)f), from device nodeID (%!@(MISSING)) for message %!@(MISSING)"
+ "%!@(MISSING) MTRPlugin active clients: %!l(MISSING)u (%!@(MISSING))"
+ "%!@(MISSING) Removing sessionID %!@(MISSING), since the peer requested to close the session"
+ "%!@(MISSING) Response received for message %!d(MISSING) (%!@(MISSING)) from homeID %!@(MISSING)"
+ "%!@(MISSING) Response received for message %!d(MISSING) (%!@(MISSING)) from homeID %!@(MISSING) with error: %!@(MISSING)"
+ "%!@(MISSING) Response received for message type %!d(MISSING) (%!@(MISSING)) from homeID %!@(MISSING)"
+ "%!@(MISSING) Response received for message type %!d(MISSING) (%!@(MISSING)) from homeID %!@(MISSING) with error: %!@(MISSING)"
+ "%!@(MISSING) Sending request to resident for homeID: %!@(MISSING), for message type: %!d(MISSING)"
+ "%!@(MISSING) Sending request to resident for homeID: %!@(MISSING), nodeID: %!@(MISSING), for message type: %!d(MISSING)"
+ "%!@(MISSING) Sending session close to resident session for controller %!@(MISSING)"
+ "%!@(MISSING) Setting delegate on device: %!@(MISSING) queue: %!@(MISSING)"
+ "%!@(MISSING) URL (%!@(MISSING)) from response diagnostic log, error: %!@(MISSING)"
+ "%!@(MISSING) controller %!@(MISSING) suspendedChangedTo: %!@(MISSING)"
+ "%!@(MISSING) deviceController %!@(MISSING) (buffered) updateControllerConfiguration %!@(MISSING)"
+ "%!@(MISSING) deviceController %!@(MISSING) updateControllerConfiguration %!@(MISSING)"
+ "%!@(MISSING) downloadLogOfType: %!d(MISSING)  nodeID: %!@(MISSING)"
+ "%!@(MISSING) initialized with xpcConnection %!@(MISSING) queue: %!@(MISSING)"
+ "%!@(MISSING) responding to download log of type %!d(MISSING) for nodeID: %!@(MISSING), for message %!@(MISSING)"
+ "/Matter/DiagnosticLog/"
+ "<%!@(MISSING): %!p(MISSING) xpc %!p(MISSING) pid: %!d(MISSING) sessionID: %!@(MISSING) Home: %!@(MISSING) Running: %!@(MISSING)>"
+ "<MTRPluginPBMHeader: mid: %!@(MISSING), type: %!u(MISSING) (%!@(MISSING)) , sid: %!@(MISSING), hid: %!@(MISSING), direction: %!@(MISSING)>"
+ "<MTRPluginProtobufMessage: mid: %!@(MISSING), type: %!u(MISSING) (%!@(MISSING)), sid: %!@(MISSING), hid: %!@(MISSING), direction: %!@(MISSING)>"
+ "@\"NSObject<OS_dispatch_source>\""
+ "@40@0:8q16d24@32"
+ "B40@0:8@16@24@?32"
+ "CloseSession"
+ "ControllerConfigUpdate"
+ "Could not create directory path %!@(MISSING) - error %!@(MISSING)"
+ "DownloadDiagnosticLog"
+ "Exception calling remote proxy: %!@(MISSING)"
+ "Failed to create daemon cache directory for user %!d(MISSING) at %!{(MISSING)public}@: %!{(MISSING)public}@"
+ "Invalid nodeIDInfo: %!@(MISSING)"
+ "MTRPluginLocalDispatchQueue"
+ "MTRPluginPBMDeviceNodeDownloadDiagnosticLog"
+ "T@\"MTRPluginClient\",W,V_pluginClient"
+ "T@\"MTRPluginPBMHeader\",&,V_messageHeader"
+ "T@\"NSArray\",&,N"
+ "T@\"NSData\",&,V_messageData"
+ "T@\"NSDictionary\",&,N"
+ "T@\"NSDictionary\",&,V_controllerConfiguration"
+ "T@\"NSMutableArray\",&,V_controllerEntities"
+ "T@\"NSMutableSet\",&,V_registeredMTRDeviceControllerIDs"
+ "T@\"NSMutableSet\",&,V_subscribedMTRDevices"
+ "T@\"NSNumber\",R"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_queue"
+ "T@\"NSObject<OS_dispatch_source>\",&,V_internalStateUpdateSource"
+ "T@\"NSObject<OS_dispatch_source>\",&,V_updateControllerConfigurationTimer"
+ "T@\"NSSet\",&,N"
+ "T@\"NSUUID\",&,V_entityIdentifier"
+ "T@\"NSUUID\",R"
+ "TB,GisSuspended,V_suspended"
+ "TB,N,V_checkinRequested"
+ "TB,V_hintRequestCheckinMessageFromPeer"
+ "Td,N,V_timeoutInterval"
+ "Ti,N,V_logType"
+ "Vv56@0:8@\"NSUUID\"16@\"NSNumber\"24q32d40@?<v@?@\"NSURL\"@\"NSError\">48"
+ "Vv56@0:8@16@24q32d40@?48"
+ "_checkinRequested"
+ "_controllerConfiguration"
+ "_hintRequestCheckinMessageFromPeer"
+ "_installResponseHandlerForIncomingProtobufMessage:hmfMessage:"
+ "_internalStateUpdateSource"
+ "_logType"
+ "_registeredMTRDeviceControllerIDs"
+ "_sendMessageToHomeWithID:messageType:pbCodable:errorBlock:replyBlock:"
+ "_subscribedMTRDevices"
+ "_suspended"
+ "_timeoutInterval"
+ "_updateControllerConfigurationTimer"
+ "addClientForXPCConnection:sessionID:queue:"
+ "checkinRequested"
+ "clientConnectionQueue"
+ "com.apple.homed"
+ "controllerConfiguration"
+ "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
+ "createFileAtPath:contents:attributes:"
+ "dataWithContentsOfURL:"
+ "defaultManager"
+ "device:injectAttributeReport:"
+ "device:injectEventReport:"
+ "deviceController:nodeID:downloadLogOfType:timeout:completion:"
+ "deviceController:updateControllerConfiguration:"
+ "deviceNodeDownloadDiagnosticLogMessageFromMessage:"
+ "deviceNodeDownloadDiagnosticLogOfType:timeout:nodeID:"
+ "downloadLogOfType:timeout:queue:completion:"
+ "fileExistsAtPath:isDirectory:"
+ "fileURLWithPath:"
+ "hasCheckinRequested"
+ "hasLogType"
+ "hasTimeoutInterval"
+ "headerWithSessionID:homeID:messageType:"
+ "hintRequestCheckinMessageFromPeer"
+ "initWithTransport:workQueue:sessionID:homeID:peerAddress:"
+ "initWithXPCConnection:sessionID:queue:"
+ "intValue"
+ "internalStateUpdateSource"
+ "localDispatchQueue"
+ "logType"
+ "messageTransport:handleCloseSession:"
+ "messageTransport:handleControllerConfigUpdate:"
+ "messageTransport:handleDownloadDiagnosticLog:"
+ "messageTransport:handleGetControllerNodeID:"
+ "numberWithInt:"
+ "onewayHeaderWithSessionID:homeID:messageType:"
+ "registeredMTRDeviceControllerIDs"
+ "requestHeaderWithSessionID:homeID:messageType:"
+ "responseHeaderForRequestHeader"
+ "retainArguments"
+ "sendControllerMessageToHomeWithID:controllerMessageType:queryRequestValue:errorBlock:replyBlock:"
+ "sendDeviceMessageToNodeWithID:homeID:deviceNodeMessageType:errorBlock:replyBlock:"
+ "sendMessageToHomeWithID:messageType:pbCodable:errorBlock:replyBlock:"
+ "sendOnewayMessageToHomeWithID:messageType:pbCodable:"
+ "setAttributes:ofItemAtPath:error:"
+ "setCheckinRequested:"
+ "setControllerConfiguration:"
+ "setHasCheckinRequested:"
+ "setHasLogType:"
+ "setHasTimeoutInterval:"
+ "setHintRequestCheckinMessageFromPeer:"
+ "setInternalStateUpdateSource:"
+ "setLogType:"
+ "setQueue:"
+ "setRegisteredMTRDeviceControllerIDs:"
+ "setSubscribedMTRDevices:"
+ "setSuspended:"
+ "setTimeoutInterval:"
+ "setUpdateControllerConfigurationTimer:"
+ "stringByAppendingPathComponent:"
+ "stringByAppendingString:"
+ "subscribedMTRDevices"
+ "suspended"
+ "timeoutInterval"
+ "updateControllerConfigurationForRemotePeer"
+ "updateControllerConfigurationTimer"
+ "urlFromResponsePayload:error:"
+ "v24@?0@\"NSURL\"8@\"NSError\"16"
+ "v36@0:8@16i24@28"
+ "{?=\"checkinRequested\"b1}"
+ "{?=\"timeoutInterval\"b1\"logType\"b1}"
- "\x01\x15"
- "\x02\x11!"
- "\x03\x11"
- "\x05"
- "\f"
- "\x11\""
- "\x12"
- "%!@(MISSING)  => controller: %!@(MISSING) device: %!@(MISSING)"
- "%!@(MISSING)  => device %!@(MISSING) attributeValue %!@(MISSING)"
- "%!@(MISSING) => calling remote proxy object %!@(MISSING)"
- "%!@(MISSING) Adding Client %!@(MISSING) for xpc connection %!@(MISSING)"
- "%!@(MISSING) Attempting to send message %!@(MISSING) to controllerID: %!@(MISSING), destination: %!{(MISSING)private}@"
- "%!@(MISSING) Attempting to send message %!@(MISSING) to home hub and controllerID: %!@(MISSING)"
- "%!@(MISSING) Canceling work item queue"
- "%!@(MISSING) Cannot add existing delegate proxy %!@(MISSING) again"
- "%!@(MISSING) Cannot find device delegate proxy for delegateID %!@(MISSING)"
- "%!@(MISSING) Connected device delegate proxy %!@(MISSING) to device %!@(MISSING)"
- "%!@(MISSING) Device controller does not support run assertion: %!@(MISSING)"
- "%!@(MISSING) Failed to send message type %!d(MISSING) (%!@(MISSING)) to controllerID: %!@(MISSING), destination: %!{(MISSING)private}@ as it is invalid"
- "%!@(MISSING) Failed to send message type %!d(MISSING) for (%!@(MISSING)) to home hub for controller %!@(MISSING) since it is invalid"
- "%!@(MISSING) Forwarding remote request shutdown controller node ID for controllerID: %!@(MISSING)"
- "%!@(MISSING) Forwarding remote request to checking with context %!@(MISSING) for controllerID: %!@(MISSING)"
- "%!@(MISSING) Forwarding remote request to register nodeID: %!@(MISSING) for controllerID: %!@(MISSING)"
- "%!@(MISSING) Forwarding remote request to unregister nodeID: %!@(MISSING) for controllerID: %!@(MISSING)"
- "%!@(MISSING) Got check-in context %!@(MISSING)"
- "%!@(MISSING) MTRPlugin active clients: %!l(MISSING)u"
- "%!@(MISSING) Read %!l(MISSING)u remote bulk attributes from nodeID: %!@(MISSING), controllerID: %!@(MISSING) "
- "%!@(MISSING) Removing run assertion on device controller: %!@(MISSING)"
- "%!@(MISSING) Response received for message %!d(MISSING) (%!@(MISSING)) from controllerID %!@(MISSING)"
- "%!@(MISSING) Response received for message %!d(MISSING) (%!@(MISSING)) from controllerID %!@(MISSING) with error: %!@(MISSING)"
- "%!@(MISSING) Response received for message type %!d(MISSING) (%!@(MISSING)) from controllerID %!@(MISSING)"
- "%!@(MISSING) Response received for message type %!d(MISSING) (%!@(MISSING)) from controllerID %!@(MISSING) with error: %!@(MISSING)"
- "%!@(MISSING) Running read bulk attributes on total of %!l(MISSING)u requests for nodeID: %!@(MISSING), controllerID: %!@(MISSING)"
- "%!@(MISSING) Running work item queue"
- "%!@(MISSING) Sending request to resident controllerID: %!@(MISSING), for message type: %!d(MISSING)"
- "%!@(MISSING) Sending request to resident controllerID: %!@(MISSING), nodeID: %!@(MISSING), for message type: %!d(MISSING)"
- "%!@(MISSING) Setting delegate on device: %!@(MISSING)"
- "%!@(MISSING) Taking run assertion on device controller: %!@(MISSING)"
- "%!@(MISSING) Timer fired, running pending work items"
- "%!@(MISSING) _currentTarget: %!@(MISSING) suspended: %!@(MISSING) "
- "%!@(MISSING) deviceController %!@(MISSING) registerNodeID %!@(MISSING)"
- "%!@(MISSING) deviceController %!@(MISSING) unregisterNodeID %!@(MISSING)"
- "%!@(MISSING) downloadLogOfType not implemented"
- "%!@(MISSING) failed to find nodeID for incoming device request message %!@(MISSING)"
- "%!@(MISSING) informing delegate to run a total of %!l(MISSING)u pending work items"
- "%!@(MISSING) initialized with client %!@(MISSING)"
- "%!@(MISSING) initialized with pluginClient %!@(MISSING) delegateID %!@(MISSING)"
- "%!@(MISSING) initialized with xpcConnection %!@(MISSING)"
- "%!@(MISSING) logState with %!l(MISSING)u delegate proxies:"
- "%!@(MISSING) no delegate proxy is setup, so ensuring we have one for delegate id: %!@(MISSING)"
- "%!@(MISSING) responding to ShutdownController with success for message %!@(MISSING)"
- "%!@(MISSING) responding to controller checkin with success for message %!@(MISSING)"
- "%!@(MISSING) responding to controller register(%!@(MISSING)) for nodeID: %!@(MISSING), for message %!@(MISSING)"
- "%!@(MISSING) shutdownDeviceController controllerUUID %!@(MISSING)"
- "<%!@(MISSING): %!p(MISSING) client %!@(MISSING)>"
- "<%!@(MISSING): %!p(MISSING) delegateID %!@(MISSING)>"
- "<%!@(MISSING): %!p(MISSING) xpc %!p(MISSING) pid: %!d(MISSING) UUID: %!@(MISSING) Home: %!@(MISSING) Running: %!@(MISSING)>"
- "<MTRPluginPBMHeader: uniqueIdentifier: %!@(MISSING), messageType: %!u(MISSING) (%!@(MISSING)) , sessionIdentifier: %!@(MISSING), homeIdentifier: %!@(MISSING), direction: %!@(MISSING)>"
- "<MTRPluginProtobufMessage: uniqueIdentifier: %!@(MISSING), messageType: %!u(MISSING) (%!@(MISSING)), sessionIdentifier: %!@(MISSING), homeIdentifier: %!@(MISSING), isRequest: %!@(MISSING)>"
- "<MTRPluginTimedWatermarkQueue: watermarkLevel: %!l(MISSING)u, waitPeriod: %!l(MISSING)f, waitingWorkItems size %!l(MISSING)u>"
- "@\"<MTRPluginTimedWatermarkQueueDelegate>\""
- "@\"HMFTimer\""
- "@\"MTRPluginLocalDispatch\""
- "@\"MTRPluginTimedWatermarkQueue\""
- "@\"NSNumber\""
- "@32@0:8Q16d24"
- "@64@0:8@16@24@32@40@48@56"
- "B40@0:8@16@24@32"
- "ControllerCheckin"
- "HMFTimerDelegate"
- "MTRPluginLocalClient dealloc: %!p(MISSING)"
- "MTRPluginLocalDeviceDelegateProxy"
- "MTRPluginLocalDeviceDelegateProxy dealloc: %!p(MISSING)"
- "MTRPluginLocalDispatch"
- "MTRPluginReadAttributeWorkItem"
- "MTRPluginTimedWatermarkQueue"
- "MTRPluginTimedWatermarkQueueDelegate"
- "MTRPluginWorkItem"
- "RegisterNodeID"
- "ShutdownController"
- "T@\"<MTRPluginTimedWatermarkQueueDelegate>\",W,V_delegate"
- "T@\"HMFTimer\",&,V_waitPeriodTimer"
- "T@\"MTRDeviceController\",R,&"
- "T@\"MTRPluginLocalClient\",W,V_pluginClient"
- "T@\"MTRPluginLocalDispatch\",&,V_dispatch"
- "T@\"MTRPluginPBMHeader\",C,V_messageHeader"
- "T@\"MTRPluginPBMUUID\",&,N,V_controllerID"
- "T@\"MTRPluginTimedWatermarkQueue\",&,V_timedWatermarkQueue"
- "T@\"NSArray\",C,N"
- "T@\"NSData\",C,V_messageData"
- "T@\"NSDictionary\",C,N"
- "T@\"NSMutableArray\",&,V_waitingWorkItems"
- "T@\"NSMutableArray\",C,V_controllerEntities"
- "T@\"NSMutableSet\",&,V_devices"
- "T@\"NSMutableSet\",&,V_registeredMTRDevices"
- "T@\"NSNumber\",&,V_attributeID"
- "T@\"NSNumber\",&,V_clusterID"
- "T@\"NSNumber\",&,V_delegateID"
- "T@\"NSNumber\",&,V_endpointID"
- "T@\"NSNumber\",&,V_nodeID"
- "T@\"NSNumber\",R,C"
- "T@\"NSObject<OS_dispatch_queue>\",R,&,V_queue"
- "T@\"NSSet\",C,N"
- "T@\"NSUUID\",&,V_UUID"
- "T@\"NSUUID\",&,V_controllerID"
- "T@\"NSUUID\",C,V_controllerUUIDForAssertion"
- "T@\"NSUUID\",C,V_entityIdentifier"
- "T@\"NSUUID\",R,C"
- "TB,R,GisRequest"
- "TQ,V_watermarkLevel"
- "Td,V_waitPeriod"
- "UnregisterNodeID"
- "Vv32@0:8@\"NSUUID\"16@\"NSUUID\"24"
- "_UUID"
- "__kickWaitingItemsDueToTimerExpiration:"
- "_controllerID"
- "_controllerUUIDForAssertion"
- "_delegateID"
- "_devices"
- "_dispatch"
- "_handleNodeIDRegistrationRequestChangeForMessage:registerNodeID:"
- "_registeredMTRDevices"
- "_sendMessageToControllerWithID:messageType:pbCodable:errorBlock:replyBlock:"
- "_timedWatermarkQueue"
- "_waitPeriod"
- "_waitPeriodTimer"
- "_waitingWorkItems"
- "_watermarkLevel"
- "addClientForXPCConnection:"
- "addDeviceDelegateProxy:"
- "addRunAssertion"
- "addWorkItem:"
- "cancel"
- "controllerID"
- "controllerUUIDForAssertion"
- "delegateID"
- "deviceController:shutdownDeviceController:"
- "deviceDelegateProxyForDelegateID:"
- "devices"
- "dispatch"
- "empty controller UUID or nodeID, bailing"
- "ensureControllerAssertionWithUUID:"
- "ensureDelegateProxySetup"
- "hasControllerID"
- "initWithControllerID:nodeID:endpointID:clusterID:attributeID:"
- "initWithPluginClient:delegateID:"
- "initWithTimeInterval:options:"
- "initWithTransport:workQueue:sessionID:controllerID:homeID:peerAddress:"
- "initWithWatermarkLevel:timedWaitPeriod:"
- "initWithXPCConnection:"
- "messageTransport:handleControllerCheckin:"
- "messageTransport:handleGetControllerNodID:"
- "messageTransport:handleRegisterNodeID:"
- "messageTransport:handleShutdownController:"
- "messageTransport:handleUnregisterNodeID:"
- "queryControllerWithID:controllerMessageType:queryRequestValue:errorBlock:replyBlock:"
- "queryDeviceNodeWithID:controllerID:deviceNodeMessageType:errorBlock:replyBlock:"
- "registeredMTRDevices"
- "removeControllerAssertion"
- "removeDeviceDelegateProxy:"
- "removeRunAssertion"
- "removeWorkItem:"
- "request"
- "requestHeaderWithSessionID:controllerID:messageType:"
- "run"
- "sendMessageToControllerWithID:messageType:pbCodable:errorBlock:replyBlock:"
- "setControllerID:"
- "setControllerUUIDForAssertion:"
- "setDelegateID:"
- "setDevices:"
- "setDispatch:"
- "setRegisteredMTRDevices:"
- "setTimedWatermarkQueue:"
- "setUUID:"
- "setWaitPeriod:"
- "setWaitPeriodTimer:"
- "setWaitingWorkItems:"
- "setWatermarkLevel:"
- "shutdown"
- "suspend"
- "timedWatermarkQueue"
- "timedWatermarkQueue:runPendingWorkItems:"
- "timerDidFire:"
- "v16@?0@\"NSArray\"8"
- "v24@0:8@\"HMFTimer\"16"
- "v32@0:8@\"MTRPluginTimedWatermarkQueue\"16@\"NSArray\"24"
- "waitPeriod"
- "waitPeriodTimer"
- "waitingWorkItems"
- "watermarkLevel"

```
