## MatterPlugin

> `/System/Library/PrivateFrameworks/MatterPlugin.framework/MatterPlugin`

```diff

-49.0.0.0.0
-  __TEXT.__text: 0x3e4d8
-  __TEXT.__auth_stubs: 0x7a0
-  __TEXT.__objc_methlist: 0x40ec
-  __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x1091
-  __TEXT.__oslogstring: 0x49da
-  __TEXT.__gcc_except_tab: 0x19e8
-  __TEXT.__unwind_info: 0xfa8
-  __TEXT.__objc_classname: 0x909
-  __TEXT.__objc_methname: 0x6c1e
-  __TEXT.__objc_methtype: 0x1445
-  __TEXT.__objc_stubs: 0x5360
-  __DATA_CONST.__got: 0x478
-  __DATA_CONST.__const: 0x7a0
-  __DATA_CONST.__objc_classlist: 0x200
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
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0x78
+  __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1990
+  __DATA_CONST.__objc_selrefs: 0x1b10
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x168
+  __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x3e0
-  __AUTH_CONST.__const: 0x200
-  __AUTH_CONST.__cfstring: 0x17e0
-  __AUTH_CONST.__objc_const: 0x60c0
-  __AUTH_CONST.__objc_intobj: 0x3f0
+  __AUTH_CONST.__auth_got: 0x3f8
+  __AUTH_CONST.__const: 0x220
+  __AUTH_CONST.__cfstring: 0x18c0
+  __AUTH_CONST.__objc_const: 0x6700
+  __AUTH_CONST.__objc_intobj: 0x438
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0x13b0
-  __DATA.__objc_ivar: 0x330
-  __DATA.__data: 0x5a0
-  __DATA.__bss: 0x78
+  __AUTH.__objc_data: 0x14a0
+  __DATA.__objc_ivar: 0x368
+  __DATA.__data: 0x600
+  __DATA.__bss: 0x80
+  __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1486
-  Symbols:   1939
-  CStrings:  1928
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
+ _MTRPluginPBMCommandWithRequiredResponseReadFrom
+ _MTRPluginPBMCommandWithRequiredResponsesReadFrom
+ _MTRPluginPBMDeviceNodeInvokeBatchCommmandMessageReadFrom
+ _OBJC_CLASS_$_HMFTimer
+ _OBJC_CLASS_$_MTRCommandWithRequiredResponse
+ _OBJC_CLASS_$_MTRPluginPBMCommandWithRequiredResponse
+ _OBJC_CLASS_$_MTRPluginPBMCommandWithRequiredResponses
+ _OBJC_CLASS_$_MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage
+ _OBJC_METACLASS_$_MTRPluginPBMCommandWithRequiredResponse
+ _OBJC_METACLASS_$_MTRPluginPBMCommandWithRequiredResponses
+ _OBJC_METACLASS_$_MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage
+ _matterPluginLogInitialize
+ _matterPluginLog_default
+ _objc_opt_self
+ _objc_retain_x9
+ _os_log_create
- _MTRErrorKey
- _MTREventIsHistoricalKey
- _MTREventNumberKey
- _MTREventPriorityKey
- _MTREventSystemUpTimeKey
- _MTREventTimeTypeKey
- _MTREventTimestampDateKey
- __os_log_default
CStrings:
+ "\x05"
+ "\x15"
+ "\x17"
+ "!"
+ "%@  => DOUBLE registering device (already registered): %@"
+ "%@ Cannot find controller for UUID %@ - returning unknown running mode, controller was not added to registry"
+ "%@ Cannot find controller for UUID %@ in %lu controllers - controller was not added to registry"
+ "%@ Cannot find device controller for client %@ nodeID %@ - controller was not added to registry"
+ "%@ Failed to complete invokeBatchCommand with error: %@"
+ "%@ Failed to invoke batch commands for nodeID: %@, with error %@, for message %@"
+ "%@ Forwarding remote request to invokeBatchCommand: commands (%@), from device nodeID (%@) for controllerID %@"
+ "%@ Ignoring notification %@ since delegate / delegateQueue is nil"
+ "%@ Ignoring notification %@ since homeUUID is nil"
+ "%@ Invoking Batch Commands on: nodeID %@ message (%@) commands %@"
+ "%@ No receiver delegate for new session setup message: %@, sending error"
+ "%@ Received message %@ but delegate %@ is suspended, sending error response to close remote session"
+ "%@ Received resident update notification %@"
+ "%@ Resumed remote client"
+ "%@ Successfully completed invokeBatchCommand with response: %@"
+ "%@ Suspended remote client"
+ "%@ Updating running mode for all clients to '%@' for home %@"
+ "%@ Updating running mode for home %@ since primary resident updated with notification %@"
+ "%@ deviceController %@ getNodesWithStoredDataWithReply"
+ "%@ deviceController: %@ getNodesWithStoredDataWithReply"
+ "%@ invokeCommands: controllerUUID %@ nodeID %@ commands %@"
+ "%@ invokeCommands: controllerUUID %@ nodeID %@ completed with error %@"
+ "%@ metrics counter fired, submitting count for %ld metrics"
+ "%@ responding to invoke batch command for nodeID: %@, for message %@"
+ "%@ resuming remote server session for home %@ since running mode is remote"
+ "%@ suspending remote server session for home %@ since running mode is local"
+ "<%@: %p, clientType: %@>"
+ "@\"HMFTimer\""
+ "@\"MTRAttributePath\""
+ "@\"MTREventPath\""
+ "@60@0:8@16@24i32@36@44@52"
+ "@72@0:8@16@24i32@36@44@52B60@64"
+ "Default"
+ "Found Bundle Identifier %@ for XPC connection %@"
+ "HMDResidentDeviceConfirmedStateChangedNotification"
+ "HMDResidentDeviceHomeUUIDNotificationKey"
+ "HMDResidentDeviceManagerUpdatePrimaryResidentNotification"
+ "HMDResidentDeviceManagerUpdateResidentNotification"
+ "HMFTimerDelegate"
+ "HomeAppWidget"
+ "InvokeBatchCommand"
+ "MTRPluginPBMCommandWithRequiredResponse"
+ "MTRPluginPBMCommandWithRequiredResponses"
+ "MTRPluginPBMDeviceNodeInvokeBatchCommmandMessage"
+ "T@\"HMFTimer\",&,V_timer"
+ "T@\"MTRAttributePath\",&,V_attributePath"
+ "T@\"MTRCommandWithRequiredResponse\",R,N"
+ "T@\"MTREventPath\",&,V_eventPath"
+ "T@\"MTRPluginPBMVariableValue\",&,N,V_requiredResponse"
+ "T@\"NSMutableArray\",&,N,V_commandWithRequiredResponseValues"
+ "T@\"NSMutableArray\",&,N,V_commandWithRequiredResponsesValues"
+ "T@\"NSMutableSet\",&,V_homesWithPrimaryResidentUpdated"
+ "T@\"NSMutableSet\",&,V_metricCounter"
+ "T@\"NSNumber\",&,V_count"
+ "T@\"NSObject<OS_dispatch_source>\",&,V_primaryResidentUpdatedSource"
+ "TB,?,R,GisSuspended"
+ "TB,GisBatchCommand,V_batchCommand"
+ "TB,GisSuspended,V_suspended"
+ "Vv32@0:8@\"NSUUID\"16@?<v@?@\"NSArray\">24"
+ "Vv32@0:8@16@?24"
+ "Vv48@0:8@\"NSUUID\"16@\"NSNumber\"24@\"NSArray\"32@?<v@?@\"NSArray\"@\"NSError\">40"
+ "_batchCommand"
+ "_closeRemoteServerSession"
+ "_commandWithRequiredResponseValues"
+ "_commandWithRequiredResponsesValues"
+ "_count"
+ "_eventPath"
+ "_homesWithPrimaryResidentUpdated"
+ "_metricCounter"
+ "_primaryResidentUpdatedSource"
+ "_registerForResidentChangedNotifications"
+ "_requiredResponse"
+ "_suspended"
+ "_timer"
+ "_updateRunningModeOfAllClientsForHome:"
+ "addCommandWithRequiredResponseValue:"
+ "addCommandWithRequiredResponsesValue:"
+ "areaSkipped"
+ "areasSelected"
+ "batchCommand"
+ "clearCommandWithRequiredResponseValues"
+ "clearCommandWithRequiredResponsesValues"
+ "com.apple.Home.HomeWidget.Interactive"
+ "com.apple.HomeAppIntentsExtension"
+ "com.apple.springboard"
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
+ "countMetric:"
+ "deviceController:getNodesWithStoredDataWithReply:"
+ "deviceController:nodeID:invokeCommands:completion:"
+ "deviceNodeInvokeBatchCommandMessageFromMessage:"
+ "deviceNodeInvokeBatchCommandMessageWithNodeID:commands:"
+ "eventCount"
+ "handlePrimaryResidentUpdateNotification:"
+ "hasRequiredResponse"
+ "homesWithPrimaryResidentUpdated"
+ "initWithPath:commandFields:requiredResponse:"
+ "initWithTimeInterval:options:"
+ "invokeBatchCommandMetricForDevice:homeID:clientType:commandPath:commandFields:remoteMessageID:"
+ "invokeCommands:queue:completion:"
+ "isBatchCommand"
+ "isPluginClientLowestHash:"
+ "member:"
+ "messageTransport:handleDeviceInvokeBatchCommand:"
+ "metricCounter"
+ "nodesWithStoredData"
+ "path"
+ "primaryResidentUpdatedSource"
+ "reportCount"
+ "requiredResponse"
+ "sendMessageToHomeWithID:messageType:pbCodable:metrics:errorBlock:replyBlock:"
+ "setBatchCommand:"
+ "setCommandWithRequiredResponseValues:"
+ "setCommandWithRequiredResponsesValues:"
+ "setCount:"
+ "setHomesWithPrimaryResidentUpdated:"
+ "setMetricCounter:"
+ "setPrimaryResidentUpdatedSource:"
+ "setRequiredResponse:"
+ "setSuspended:"
+ "setTimer:"
+ "suspended"
+ "timer"
+ "timerDidFire:"
+ "v24@0:8@\"HMFTimer\"16"
+ "writeAttributeMetricForDevice:homeID:clientType:endpointID:clusterID:attributeID:timedWrite:remoteMessageID:"
- "\x01\x11"
- "%@ Cannot find controller for UUID %@ - returning unknown running mode"
- "%@ Cannot find controller for UUID %@ in %lu controllers - returning first available controller"
- "%@ Cannot find device controller for client %@ nodeID %@"
- "@68@0:8@16@24@32@40@48B56@60"
- "T@\"MTRPluginInvokeCommandMetric\",&,V_originalInvokeCommandMetric"
- "T@\"NSDictionary\",&,V_eventEntry"
- "T@\"NSDictionary\",&,V_reportEntry"
- "_eventEntry"
- "_originalInvokeCommandMetric"
- "_reportEntry"
- "attributeValue"
- "com.apple.SpringBoard"
- "eventEntry"
- "eventIsHistorical"
- "eventNumber"
- "eventPriority"
- "eventSystemUptime"
- "eventTime"
- "eventTimestamp"
- "eventValue"
- "expectedRVCOperationalState"
- "firstObject"
- "originalInvokeCommandMetric"
- "reportEntry"
- "sendMessageToHomeWithID:messageType:pbCodable:metric:errorBlock:replyBlock:"
- "setEventEntry:"
- "setOriginalInvokeCommandMetric:"
- "setReportEntry:"
- "totalAreasSelected"
- "v40@0:8@16@24@?32"
- "writeAttributeMetricForDevice:homeID:endpointID:clusterID:attributeID:timedWrite:remoteMessageID:"

```
