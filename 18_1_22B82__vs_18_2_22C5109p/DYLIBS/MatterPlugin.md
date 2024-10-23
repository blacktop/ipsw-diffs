## MatterPlugin

> `/System/Library/PrivateFrameworks/MatterPlugin.framework/MatterPlugin`

```diff

-5.2.2.0.0
-  __TEXT.__text: 0x3360
-  __TEXT.__auth_stubs: 0x470
-  __TEXT.__objc_methlist: 0x1e0
-  __TEXT.__const: 0x50
-  __TEXT.__oslogstring: 0x14c
-  __TEXT.__cstring: 0xd2e
-  __TEXT.__gcc_except_tab: 0x60
-  __TEXT.__unwind_info: 0x108
-  __TEXT.__objc_classname: 0x7f
-  __TEXT.__objc_methname: 0xbb4
-  __TEXT.__objc_methtype: 0x2e8
-  __TEXT.__objc_stubs: 0x460
-  __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0xb8
-  __DATA_CONST.__objc_classlist: 0x20
-  __DATA_CONST.__objc_protolist: 0x10
+21.0.0.0.0
+  __TEXT.__text: 0x340cc
+  __TEXT.__auth_stubs: 0x620
+  __TEXT.__objc_methlist: 0x3480
+  __TEXT.__const: 0xc0
+  __TEXT.__gcc_except_tab: 0x1c2c
+  __TEXT.__oslogstring: 0x40d1
+  __TEXT.__cstring: 0x8bd
+  __TEXT.__unwind_info: 0xf50
+  __TEXT.__objc_classname: 0x699
+  __TEXT.__objc_methname: 0x5511
+  __TEXT.__objc_methtype: 0x1279
+  __TEXT.__objc_stubs: 0x4460
+  __DATA_CONST.__got: 0x2a8
+  __DATA_CONST.__const: 0x568
+  __DATA_CONST.__objc_classlist: 0x170
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b0
-  __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x248
-  __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x380
-  __AUTH_CONST.__objc_const: 0x7b0
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x24
-  __DATA.__data: 0xc0
-  __DATA.__bss: 0x30
+  __DATA_CONST.__objc_selrefs: 0x1488
+  __DATA_CONST.__objc_protorefs: 0x10
+  __DATA_CONST.__objc_superrefs: 0x160
+  __DATA_CONST.__objc_arraydata: 0x40
+  __AUTH_CONST.__auth_got: 0x320
+  __AUTH_CONST.__const: 0x120
+  __AUTH_CONST.__cfstring: 0xd40
+  __AUTH_CONST.__objc_const: 0x53e8
+  __AUTH_CONST.__objc_intobj: 0x348
+  __AUTH_CONST.__objc_arrayobj: 0x60
+  __AUTH.__objc_data: 0xe60
+  __DATA.__objc_ivar: 0x2b0
+  __DATA.__data: 0x540
+  __DATA.__bss: 0x90
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Matter.framework/Matter
-  - /System/Library/PrivateFrameworks/IMFoundation.framework/IMFoundation
+  - /System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation
+  - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 51
-  Symbols:   110
-  CStrings:  212
+  Functions: 1336
+  Symbols:   1674
+  CStrings:  1582
 
Symbols:
+ <redacted>
+ OBJC_IVAR_$_MTRPluginPBMAttributePath._attributeID
+ OBJC_IVAR_$_MTRPluginPBMAttributePath._clusterPath
+ OBJC_IVAR_$_MTRPluginPBMAttributePath._has
+ OBJC_IVAR_$_MTRPluginPBMClusterPath._clusterID
+ OBJC_IVAR_$_MTRPluginPBMClusterPath._endpointID
+ OBJC_IVAR_$_MTRPluginPBMClusterPath._has
+ OBJC_IVAR_$_MTRPluginPBMCommandPath._clusterPath
+ OBJC_IVAR_$_MTRPluginPBMCommandPath._commandID
+ OBJC_IVAR_$_MTRPluginPBMCommandPath._has
+ OBJC_IVAR_$_MTRPluginPBMDate._has
+ OBJC_IVAR_$_MTRPluginPBMDate._value
+ OBJC_IVAR_$_MTRPluginPBMDeviceControllerMessage._header
+ OBJC_IVAR_$_MTRPluginPBMDeviceControllerMessage._value
+ OBJC_IVAR_$_MTRPluginPBMDeviceNode._has
+ OBJC_IVAR_$_MTRPluginPBMDeviceNode._nodeID
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeInvokeCommmandMessage._commandFields
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeInvokeCommmandMessage._commandPath
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeInvokeCommmandMessage._expectedValueInterval
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeInvokeCommmandMessage._expectedValues
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeInvokeCommmandMessage._has
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeInvokeCommmandMessage._header
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeInvokeCommmandMessage._node
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeInvokeCommmandMessage._serverSideProcessingTimeout
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeInvokeCommmandMessage._timedInvokeTimeout
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeMessage._header
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeMessage._node
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeMessage._value
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeReadAttributeMessage._attributePath
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeReadAttributeMessage._header
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeReadAttributeMessage._node
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeReadAttributeMessage._readParams
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeReadMultipleAttributesMessage._attributePaths
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeReadMultipleAttributesMessage._header
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeReadMultipleAttributesMessage._node
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeWriteAttributeMessage._attributePath
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeWriteAttributeMessage._expectedValueInterval
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeWriteAttributeMessage._has
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeWriteAttributeMessage._header
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeWriteAttributeMessage._node
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeWriteAttributeMessage._timedWriteTimeout
+ OBJC_IVAR_$_MTRPluginPBMDeviceNodeWriteAttributeMessage._value
+ OBJC_IVAR_$_MTRPluginPBMError._code
+ OBJC_IVAR_$_MTRPluginPBMError._domain
+ OBJC_IVAR_$_MTRPluginPBMError._has
+ OBJC_IVAR_$_MTRPluginPBMEventPath._clusterPath
+ OBJC_IVAR_$_MTRPluginPBMEventPath._eventID
+ OBJC_IVAR_$_MTRPluginPBMEventPath._has
+ OBJC_IVAR_$_MTRPluginPBMHeader._controllerID
+ OBJC_IVAR_$_MTRPluginPBMHeader._has
+ OBJC_IVAR_$_MTRPluginPBMHeader._homeID
+ OBJC_IVAR_$_MTRPluginPBMHeader._messageDirection
+ OBJC_IVAR_$_MTRPluginPBMHeader._messageID
+ OBJC_IVAR_$_MTRPluginPBMHeader._messageType
+ OBJC_IVAR_$_MTRPluginPBMHeader._protocol
+ OBJC_IVAR_$_MTRPluginPBMHeader._schema
+ OBJC_IVAR_$_MTRPluginPBMHeader._sessionID
+ OBJC_IVAR_$_MTRPluginPBMHeader._version
+ OBJC_IVAR_$_MTRPluginPBMHeaderMessage._header
+ OBJC_IVAR_$_MTRPluginPBMReadParams._assumeUnknownAttributesReportable
+ OBJC_IVAR_$_MTRPluginPBMReadParams._filterByFabric
+ OBJC_IVAR_$_MTRPluginPBMReadParams._has
+ OBJC_IVAR_$_MTRPluginPBMReadParams._minEventNumber
+ OBJC_IVAR_$_MTRPluginPBMURL._value
+ OBJC_IVAR_$_MTRPluginPBMUUID._value
+ OBJC_IVAR_$_MTRPluginPBMVariableKeyValuePair._key
+ OBJC_IVAR_$_MTRPluginPBMVariableKeyValuePair._value
+ OBJC_IVAR_$_MTRPluginPBMVariableValue._arrayValue
+ OBJC_IVAR_$_MTRPluginPBMVariableValue._attributePathValue
+ OBJC_IVAR_$_MTRPluginPBMVariableValue._clusterPathValue
+ OBJC_IVAR_$_MTRPluginPBMVariableValue._commandPathValue
+ OBJC_IVAR_$_MTRPluginPBMVariableValue._dataValue
+ OBJC_IVAR_$_MTRPluginPBMVariableValue._dateValue
+ OBJC_IVAR_$_MTRPluginPBMVariableValue._dictionaryValue
+ OBJC_IVAR_$_MTRPluginPBMVariableValue._doubleValue
+ OBJC_IVAR_$_MTRPluginPBMVariableValue._errorValue
+ OBJC_IVAR_$_MTRPluginPBMVariableValue._eventPathValue
+ OBJC_IVAR_$_MTRPluginPBMVariableValue._has
+ OBJC_IVAR_$_MTRPluginPBMVariableValue._integerValue
+ OBJC_IVAR_$_MTRPluginPBMVariableValue._setValue
+ OBJC_IVAR_$_MTRPluginPBMVariableValue._stringValue
+ OBJC_IVAR_$_MTRPluginPBMVariableValue._unsignedIntegerValue
+ OBJC_IVAR_$_MTRPluginPBMVariableValue._urlValue
+ OBJC_IVAR_$_MTRPluginPBMVariableValue._uuidValue
+ OBJC_IVAR_$_MTRPluginPBMVariableValueDictionary._pairs
+ OBJC_IVAR_$_MTRPluginPBMVariableValueList._values
+ OBJC_IVAR_$_MTRPluginPBMVariableValueResponseMessage._errorValue
+ OBJC_IVAR_$_MTRPluginPBMVariableValueResponseMessage._header
+ OBJC_IVAR_$_MTRPluginPBMVariableValueResponseMessage._value
+ OBJC_IVAR_$_PBDataReader._bytes
+ OBJC_IVAR_$_PBDataReader._error
+ OBJC_IVAR_$_PBDataReader._length
+ OBJC_IVAR_$_PBDataReader._pos
+ _CFNotificationCenterAddObserver
+ _CFNotificationCenterGetDarwinNotifyCenter
+ _CFNotificationCenterRemoveObserver
+ _CFNumberGetType
+ _MTRPluginCheckProtocolContainsSelector
+ _MTRPluginEqualObjects
+ _MTRPluginErrorDomain
+ _MTRPluginForceRemoteControl
+ _MTRPluginMatterRequestKey
+ _MTRPluginMaxActiveClientSessions
+ _MTRPluginPBMAttributePathReadFrom
+ _MTRPluginPBMClusterPathReadFrom
+ _MTRPluginPBMCommandPathReadFrom
+ _MTRPluginPBMDateReadFrom
+ _MTRPluginPBMDeviceControllerMessageReadFrom
+ _MTRPluginPBMDeviceNodeInvokeCommmandMessageReadFrom
+ _MTRPluginPBMDeviceNodeMessageReadFrom
+ _MTRPluginPBMDeviceNodeReadAttributeMessageReadFrom
+ _MTRPluginPBMDeviceNodeReadFrom
+ _MTRPluginPBMDeviceNodeReadMultipleAttributesMessageReadFrom
+ _MTRPluginPBMDeviceNodeWriteAttributeMessageReadFrom
+ _MTRPluginPBMErrorReadFrom
+ _MTRPluginPBMEventPathReadFrom
+ _MTRPluginPBMHeaderMessageReadFrom
+ _MTRPluginPBMHeaderReadFrom
+ _MTRPluginPBMReadParamsReadFrom
+ _MTRPluginPBMURLReadFrom
+ _MTRPluginPBMUUIDReadFrom
+ _MTRPluginPBMVariableKeyValuePairReadFrom
+ _MTRPluginPBMVariableValueDictionaryReadFrom
+ _MTRPluginPBMVariableValueListReadFrom
+ _MTRPluginPBMVariableValueReadFrom
+ _MTRPluginPBMVariableValueResponseMessageReadFrom
+ _NSSelectorFromString
+ _NSStringFromClass
+ _NSStringFromSelector
+ _NSSystemClockDidChangeNotification
+ _NSSystemTimeZoneDidChangeNotification
+ _OBJC_CLASS_$_HMFMessage
+ _OBJC_CLASS_$_HMFTimer
+ _OBJC_CLASS_$_MTRAttributePath
+ _OBJC_CLASS_$_MTRAttributeRequestPath
+ _OBJC_CLASS_$_MTRClusterPath
+ _OBJC_CLASS_$_MTRCommandPath
+ _OBJC_CLASS_$_MTRDeviceControllerEntity
+ _OBJC_CLASS_$_MTREventPath
+ _OBJC_CLASS_$_MTRPluginClient
+ _OBJC_CLASS_$_MTRPluginClientConnection
+ _OBJC_CLASS_$_MTRPluginClientManager
+ _OBJC_CLASS_$_MTRPluginClientXPCProxy
+ _OBJC_CLASS_$_MTRPluginLocalClient
+ _OBJC_CLASS_$_MTRPluginLocalDeviceDelegateProxy
+ _OBJC_CLASS_$_MTRPluginLocalDispatch
+ _OBJC_CLASS_$_MTRPluginPBMAttributePath
+ _OBJC_CLASS_$_MTRPluginPBMClusterPath
+ _OBJC_CLASS_$_MTRPluginPBMCommandPath
+ _OBJC_CLASS_$_MTRPluginPBMDate
+ _OBJC_CLASS_$_MTRPluginPBMDeviceControllerMessage
+ _OBJC_CLASS_$_MTRPluginPBMDeviceNode
+ _OBJC_CLASS_$_MTRPluginPBMDeviceNodeInvokeCommmandMessage
+ _OBJC_CLASS_$_MTRPluginPBMDeviceNodeMessage
+ _OBJC_CLASS_$_MTRPluginPBMDeviceNodeReadAttributeMessage
+ _OBJC_CLASS_$_MTRPluginPBMDeviceNodeReadMultipleAttributesMessage
+ _OBJC_CLASS_$_MTRPluginPBMDeviceNodeWriteAttributeMessage
+ _OBJC_CLASS_$_MTRPluginPBMError
+ _OBJC_CLASS_$_MTRPluginPBMEventPath
+ _OBJC_CLASS_$_MTRPluginPBMHeader
+ _OBJC_CLASS_$_MTRPluginPBMHeaderMessage
+ _OBJC_CLASS_$_MTRPluginPBMReadParams
+ _OBJC_CLASS_$_MTRPluginPBMURL
+ _OBJC_CLASS_$_MTRPluginPBMUUID
+ _OBJC_CLASS_$_MTRPluginPBMVariableKeyValuePair
+ _OBJC_CLASS_$_MTRPluginPBMVariableValue
+ _OBJC_CLASS_$_MTRPluginPBMVariableValueDictionary
+ _OBJC_CLASS_$_MTRPluginPBMVariableValueList
+ _OBJC_CLASS_$_MTRPluginPBMVariableValueResponseMessage
+ _OBJC_CLASS_$_MTRPluginPairType
+ _OBJC_CLASS_$_MTRPluginProtobufMessage
+ _OBJC_CLASS_$_MTRPluginProtobufMessageDispatcher
+ _OBJC_CLASS_$_MTRPluginProtobufMessageReceiver
+ _OBJC_CLASS_$_MTRPluginProtobufOverModernTransport
+ _OBJC_CLASS_$_MTRPluginReadAttributeWorkItem
+ _OBJC_CLASS_$_MTRPluginRemoteClient
+ _OBJC_CLASS_$_MTRPluginResidentClientSession
+ _OBJC_CLASS_$_MTRPluginResidentServer
+ _OBJC_CLASS_$_MTRPluginServer
+ _OBJC_CLASS_$_MTRPluginThirdPartyExclusions
+ _OBJC_CLASS_$_MTRPluginTimedWatermarkQueue
+ _OBJC_CLASS_$_MTRPluginWorkItem
+ _OBJC_CLASS_$_NSArray
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ _OBJC_CLASS_$_NSData
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSError
+ _OBJC_CLASS_$_NSIndexSet
+ _OBJC_CLASS_$_NSInvocation
+ _OBJC_CLASS_$_NSMutableSet
+ _OBJC_CLASS_$_NSNotificationCenter
+ _OBJC_CLASS_$_NSSet
+ _OBJC_CLASS_$_NSSortDescriptor
+ _OBJC_CLASS_$_NSString
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$_NSUserDefaults
+ _OBJC_CLASS_$_NSXPCInterface
+ _OBJC_CLASS_$_PBCodable
+ _OBJC_EHTYPE_$_NSException
+ _OBJC_METACLASS_$_MTRDeviceControllerEntity
+ _OBJC_METACLASS_$_MTRPluginClient
+ _OBJC_METACLASS_$_MTRPluginClientConnection
+ _OBJC_METACLASS_$_MTRPluginClientManager
+ _OBJC_METACLASS_$_MTRPluginClientXPCProxy
+ _OBJC_METACLASS_$_MTRPluginLocalClient
+ _OBJC_METACLASS_$_MTRPluginLocalDeviceDelegateProxy
+ _OBJC_METACLASS_$_MTRPluginLocalDispatch
+ _OBJC_METACLASS_$_MTRPluginPBMAttributePath
+ _OBJC_METACLASS_$_MTRPluginPBMClusterPath
+ _OBJC_METACLASS_$_MTRPluginPBMCommandPath
+ _OBJC_METACLASS_$_MTRPluginPBMDate
+ _OBJC_METACLASS_$_MTRPluginPBMDeviceControllerMessage
+ _OBJC_METACLASS_$_MTRPluginPBMDeviceNode
+ _OBJC_METACLASS_$_MTRPluginPBMDeviceNodeInvokeCommmandMessage
+ _OBJC_METACLASS_$_MTRPluginPBMDeviceNodeMessage
+ _OBJC_METACLASS_$_MTRPluginPBMDeviceNodeReadAttributeMessage
+ _OBJC_METACLASS_$_MTRPluginPBMDeviceNodeReadMultipleAttributesMessage
+ _OBJC_METACLASS_$_MTRPluginPBMDeviceNodeWriteAttributeMessage
+ _OBJC_METACLASS_$_MTRPluginPBMError
+ _OBJC_METACLASS_$_MTRPluginPBMEventPath
+ _OBJC_METACLASS_$_MTRPluginPBMHeader
+ _OBJC_METACLASS_$_MTRPluginPBMHeaderMessage
+ _OBJC_METACLASS_$_MTRPluginPBMReadParams
+ _OBJC_METACLASS_$_MTRPluginPBMURL
+ _OBJC_METACLASS_$_MTRPluginPBMUUID
+ _OBJC_METACLASS_$_MTRPluginPBMVariableKeyValuePair
+ _OBJC_METACLASS_$_MTRPluginPBMVariableValue
+ _OBJC_METACLASS_$_MTRPluginPBMVariableValueDictionary
+ _OBJC_METACLASS_$_MTRPluginPBMVariableValueList
+ _OBJC_METACLASS_$_MTRPluginPBMVariableValueResponseMessage
+ _OBJC_METACLASS_$_MTRPluginPairType
+ _OBJC_METACLASS_$_MTRPluginProtobufMessage
+ _OBJC_METACLASS_$_MTRPluginProtobufMessageDispatcher
+ _OBJC_METACLASS_$_MTRPluginProtobufMessageReceiver
+ _OBJC_METACLASS_$_MTRPluginProtobufOverModernTransport
+ _OBJC_METACLASS_$_MTRPluginReadAttributeWorkItem
+ _OBJC_METACLASS_$_MTRPluginRemoteClient
+ _OBJC_METACLASS_$_MTRPluginResidentClientSession
+ _OBJC_METACLASS_$_MTRPluginResidentServer
+ _OBJC_METACLASS_$_MTRPluginServer
+ _OBJC_METACLASS_$_MTRPluginThirdPartyExclusions
+ _OBJC_METACLASS_$_MTRPluginTimedWatermarkQueue
+ _OBJC_METACLASS_$_MTRPluginWorkItem
+ _OBJC_METACLASS_$_PBCodable
+ _PBDataWriterWriteBOOLField
+ _PBDataWriterWriteDataField
+ _PBDataWriterWriteDoubleField
+ _PBDataWriterWriteInt32Field
+ _PBDataWriterWriteInt64Field
+ _PBDataWriterWriteStringField
+ _PBDataWriterWriteSubmessage
+ _PBDataWriterWriteUint32Field
+ _PBDataWriterWriteUint64Field
+ _PBReaderPlaceMark
+ _PBReaderReadData
+ _PBReaderReadString
+ _PBReaderRecallMark
+ _PBReaderSkipValueWithTag
+ __Block_object_dispose
+ __os_log_debug_impl
+ __os_log_error_impl
+ _dispatch_after
+ _dispatch_assert_queue$V2
+ _dispatch_async
+ _dispatch_sync
+ _dispatch_time
+ _fmod
+ _objc_alloc
+ _objc_autoreleasePoolPop
+ _objc_autoreleasePoolPush
+ _objc_begin_catch
+ _objc_copyWeak
+ _objc_destroyWeak
+ _objc_end_catch
+ _objc_initWeak
+ _objc_loadWeakRetained
+ _objc_opt_isKindOfClass
+ _objc_opt_respondsToSelector
+ _objc_release_x9
+ _objc_retainAutorelease
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x1
+ _objc_retain_x4
+ _objc_retain_x6
+ _objc_retain_x7
+ _objc_setProperty_atomic
+ _objc_storeWeak
+ _objc_unsafeClaimAutoreleasedReturnValue
+ _protocol_getMethodDescription
- _IMGetXPCArrayFromDictionary
- _IMGetXPCCodableFromDictionaryWithStandardAllowlist
- _IMGetXPCDictionaryFromDictionary
- _IMGetXPCStringFromDictionary
- _IMInsertCodableObjectsToXPCDictionary
- _IMInsertNSStringsToXPCDictionary
- _IMXPCCreateServerConnectionWithQueue
- _NSLog
- _OBJC_CLASS_$_MTRDevicePluginServer
- _OBJC_CLASS_$_MTRDevicePluginSyncManager
- _OBJC_METACLASS_$_MTRDevicePluginServer
- _OBJC_METACLASS_$_MTRDevicePluginSyncManager
- __IMAlwaysLog
- __IMWillLog
- ___XPC_MTRRemoteDeviceController_initWithParameters_response
- ___XPC_MTRRemoteDevice_delegate_deviceBecameActive
- ___XPC_MTRRemoteDevice_delegate_receivedAttributeReport
- ___XPC_MTRRemoteDevice_delegate_receivedEventReport
- ___XPC_MTRRemoteDevice_delegate_stateChanged
- ___XPC_MTRRemoteDevice_estimatedStartTime_response
- ___XPC_MTRRemoteDevice_invokeCommand_response
- ___XPC_MTRRemoteDevice_readAttribute_response
- __xpc_error_connection_interrupted
- __xpc_error_connection_invalid
- __xpc_error_termination_imminent
- __xpc_type_dictionary
- __xpc_type_error
- _free
- _objc_retainBlock
- _objc_retain_x5
- _xpc_connection_activate
- _xpc_connection_cancel
- _xpc_connection_get_pid
- _xpc_connection_send_message
- _xpc_connection_send_message_with_reply
- _xpc_copy_description
- _xpc_dictionary_create
- _xpc_dictionary_create_reply
- _xpc_dictionary_get_bool
- _xpc_dictionary_get_int64
- _xpc_dictionary_set_int64
- _xpc_get_type
CStrings:
+ "\x01\x12"
+ "\x01\x15"
+ "\x02\x11!"
+ "\x03"
+ "\x03\x11"
+ "\x04"
+ "\x05"
+ "\t"
+ "\f"
+ "\x11"
+ "\x11\""
+ "\x12"
+ "\x13"
+ "\x18"
+ "   => %!@(MISSING) Registered nodeIDs: %!@(MISSING)"
+ " *** Failed to sendMessage to primary home hub with error: %!@(MISSING)"
+ " *** Ignoring new home UUID: %!@(MISSING) for connection: %!@(MISSING), and invalidating"
+ " => Assigning home UUID: %!@(MISSING) to connection: %!@(MISSING)"
+ " => Device wasn't registered, ignoring"
+ " => Ignoring, already added"
+ " => Ignoring, not present"
+ " => Interrupted MTRPluginClientConnection: %!@(MISSING)"
+ " => Invalidated MTRPluginClientConnection: %!@(MISSING)"
+ "$"
+ "%!@(MISSING)     => %!@(MISSING)"
+ "%!@(MISSING)  => controller %!@(MISSING) controllerNodeID %!@(MISSING)"
+ "%!@(MISSING)  => controller %!@(MISSING) isRunning %!@(MISSING)"
+ "%!@(MISSING)  => controller %!@(MISSING) uniqueIdentifier %!@(MISSING)"
+ "%!@(MISSING)  => controller: %!@(MISSING) device: %!@(MISSING)"
+ "%!@(MISSING)  => device %!@(MISSING)"
+ "%!@(MISSING)  => device %!@(MISSING) attributeValue %!@(MISSING)"
+ "%!@(MISSING)  => device %!@(MISSING) deviceCachePrimed %!l(MISSING)u"
+ "%!@(MISSING)  => device %!@(MISSING) estimatedStartTime %!@(MISSING)"
+ "%!@(MISSING)  => device %!@(MISSING) estimatedSubscriptionLatency %!@(MISSING)"
+ "%!@(MISSING)  => device %!@(MISSING) readAttributePaths %!@(MISSING)"
+ "%!@(MISSING)  => device %!@(MISSING) state %!l(MISSING)u"
+ "%!@(MISSING)  => registering device: %!@(MISSING)"
+ "%!@(MISSING)  => unregistering device: %!@(MISSING)"
+ "%!@(MISSING) %!@(MISSING)"
+ "%!@(MISSING) ** Failed to create session: %!@(MISSING) for sessionID : %!@(MISSING)  controllerID: %!@(MISSING)  homeID: %!@(MISSING)"
+ "%!@(MISSING) *** Failed to sendMessage with error: %!@(MISSING)"
+ "%!@(MISSING) *** No device created for nodeID: %!@(MISSING)"
+ "%!@(MISSING) *** No device to unregister for nodeID: %!@(MISSING)"
+ "%!@(MISSING) *** No session found to remove: %!@(MISSING) for sessionID : %!@(MISSING)"
+ "%!@(MISSING) *** commandFields is invalid type %!@(MISSING):%!@(MISSING)"
+ "%!@(MISSING) *** commandFields is missing type %!@(MISSING):%!@(MISSING)"
+ "%!@(MISSING) *** deviceController nil (not found) for controllerUUID: %!@(MISSING)"
+ "%!@(MISSING) <= Sending message to delegate %!@(MISSING) to deliver to home hub"
+ "%!@(MISSING) <= Sending message: %!@(MISSING) to remote peer: %!@(MISSING)"
+ "%!@(MISSING) <= Sending response %!@(MISSING) for incoming request HMFMessage (%!@(MISSING) : %!@(MISSING))"
+ "%!@(MISSING) <= Sending response for incoming request HMFMessage (%!@(MISSING) : %!@(MISSING)) with error: %!@(MISSING)"
+ "%!@(MISSING) => Delivering message: %!@(MISSING) to delegate: %!@(MISSING) homeUUID: %!@(MISSING)"
+ "%!@(MISSING) => Received incoming HMFMessage %!@(MISSING)"
+ "%!@(MISSING) => Received incoming protobuf message: %!@(MISSING) from HMFMessage (%!@(MISSING): %!@(MISSING))"
+ "%!@(MISSING) => Received invalid HMFMessage (%!@(MISSING) : %!@(MISSING)), failed to unpack protobuf data"
+ "%!@(MISSING) => Received invalid HMFMessage payload in response for message %!@(MISSING) as it is missing protobuf payload"
+ "%!@(MISSING) => Received invalid HMFMessage payload in response for message %!@(MISSING), failed to unpack protobuf data"
+ "%!@(MISSING) => Received invalid incoming HMFMessage (%!@(MISSING): %!@(MISSING)) to dispatch as it is missing protobuf payload"
+ "%!@(MISSING) => Received invalid responseValue in response for protobuf message %!@(MISSING)"
+ "%!@(MISSING) => Received responseValue in response for protobuf message %!@(MISSING)"
+ "%!@(MISSING) => Removing tracked client %!@(MISSING)"
+ "%!@(MISSING) => calling remote proxy object %!@(MISSING)"
+ "%!@(MISSING) Adding Client %!@(MISSING) for xpc connection %!@(MISSING)"
+ "%!@(MISSING) Adding control channel receiver delegate %!@(MISSING)"
+ "%!@(MISSING) Adding delegate for MTRDevice: %!@(MISSING)"
+ "%!@(MISSING) Adding device controller: %!@(MISSING) for entityIdentifier %!@(MISSING)"
+ "%!@(MISSING) Adding new session receiver delegate %!@(MISSING) for sessionID: %!@(MISSING)"
+ "%!@(MISSING) Attempting to send message %!@(MISSING) to controllerID: %!@(MISSING), destination: %!{(MISSING)private}@"
+ "%!@(MISSING) Attempting to send message %!@(MISSING) to home hub and controllerID: %!@(MISSING)"
+ "%!@(MISSING) Calling invokeHandler on delegate %!p(MISSING) for session with identifier %!@(MISSING) for message: %!@(MISSING)"
+ "%!@(MISSING) Canceling work item queue"
+ "%!@(MISSING) Cannot add client for same xpc connection %!@(MISSING)"
+ "%!@(MISSING) Cannot add existing delegate proxy %!@(MISSING) again"
+ "%!@(MISSING) Cannot call addDelegate again to device %!@(MISSING) - ignoring"
+ "%!@(MISSING) Cannot find and remove client for xpc connection %!@(MISSING)"
+ "%!@(MISSING) Cannot find client for xpc connection %!@(MISSING)"
+ "%!@(MISSING) Cannot find controller for UUID %!@(MISSING) in %!l(MISSING)u controllers - returning first available controller"
+ "%!@(MISSING) Cannot find device %!@(MISSING) to removeDelegate - ignoring"
+ "%!@(MISSING) Cannot find device controller for client %!@(MISSING) nodeID %!@(MISSING)"
+ "%!@(MISSING) Cannot find device delegate proxy for delegateID %!@(MISSING)"
+ "%!@(MISSING) Connected device delegate proxy %!@(MISSING) to device %!@(MISSING)"
+ "%!@(MISSING) Created remote dispatcher with session ID: %!@(MISSING)"
+ "%!@(MISSING) De-registering for signification time change notifications"
+ "%!@(MISSING) Deregistering selector for messageType: %!@(MISSING) on session: %!@(MISSING)"
+ "%!@(MISSING) Device controller does not support run assertion: %!@(MISSING)"
+ "%!@(MISSING) Failed to _deliverMessagePayloadToPrimaryResident for connection: %!@(MISSING)"
+ "%!@(MISSING) Failed to complete invokeCommand with error: %!@(MISSING)"
+ "%!@(MISSING) Failed to deregister selector for messageType: %!@(MISSING) on session: %!@(MISSING) since session is not valid"
+ "%!@(MISSING) Failed to get cachePrimed of device %!@(MISSING) from controller %!@(MISSING)"
+ "%!@(MISSING) Failed to get state of device %!@(MISSING) from controller %!@(MISSING)"
+ "%!@(MISSING) Failed to getEstimatedStartTime of device %!@(MISSING) from controller %!@(MISSING)"
+ "%!@(MISSING) Failed to getEstimatedSubscriptionLatency of device %!@(MISSING) from controller %!@(MISSING)"
+ "%!@(MISSING) Failed to invoke command for nodeID: %!@(MISSING), with error %!@(MISSING), for message %!@(MISSING)"
+ "%!@(MISSING) Failed to readAttribute with error: %!@(MISSING)"
+ "%!@(MISSING) Failed to readMultipleAttributes with error: %!@(MISSING)"
+ "%!@(MISSING) Failed to register selector %!@(MISSING) for messageType: %!@(MISSING) on session: %!@(MISSING) since session is not valid"
+ "%!@(MISSING) Failed to register session due to invalid session, controller or home ID, message source: %!@(MISSING)"
+ "%!@(MISSING) Failed to respond to incoming protobuf message %!@(MISSING) due to malformed response"
+ "%!@(MISSING) Failed to send attribute report with error: %!@(MISSING)"
+ "%!@(MISSING) Failed to send device became active with error: %!@(MISSING)"
+ "%!@(MISSING) Failed to send device cache primed with error: %!@(MISSING)"
+ "%!@(MISSING) Failed to send device configChanged with error: %!@(MISSING)"
+ "%!@(MISSING) Failed to send device internal state updated with error: %!@(MISSING)"
+ "%!@(MISSING) Failed to send event report with error: %!@(MISSING)"
+ "%!@(MISSING) Failed to send message type %!d(MISSING) (%!@(MISSING)) to controllerID: %!@(MISSING), destination: %!{(MISSING)private}@ as it is invalid"
+ "%!@(MISSING) Failed to send message type %!d(MISSING) for (%!@(MISSING)) to home hub for controller %!@(MISSING) since it is invalid"
+ "%!@(MISSING) Failed to send state changed value with error: %!@(MISSING)"
+ "%!@(MISSING) Failed to unregister session due to invalid session, controller or home ID "
+ "%!@(MISSING) Forwarding remote request shutdown controller node ID for controllerID: %!@(MISSING)"
+ "%!@(MISSING) Forwarding remote request to checking with context %!@(MISSING) for controllerID: %!@(MISSING)"
+ "%!@(MISSING) Forwarding remote request to get controller node ID for controllerID: %!@(MISSING)"
+ "%!@(MISSING) Forwarding remote request to get controller run state for controllerID: %!@(MISSING)"
+ "%!@(MISSING) Forwarding remote request to get controller unique ID for controllerID: %!@(MISSING)"
+ "%!@(MISSING) Forwarding remote request to get device estimatedStartTime for nodeID: %!@(MISSING) for controllerID: %!@(MISSING)"
+ "%!@(MISSING) Forwarding remote request to get device estimatedSubscriptionLatency for nodeID: %!@(MISSING) for controllerID: %!@(MISSING)"
+ "%!@(MISSING) Forwarding remote request to get device is cache primed for nodeID: %!@(MISSING) for controllerID: %!@(MISSING)"
+ "%!@(MISSING) Forwarding remote request to get device state for nodeID: %!@(MISSING) for controllerID: %!@(MISSING)"
+ "%!@(MISSING) Forwarding remote request to invokeCommand: endpointID (%!@(MISSING)), clusterID (%!@(MISSING)), commandID (%!@(MISSING)), commandFields (%!@(MISSING)), expectedValues (%!@(MISSING)),                expectedValueInterval (%!@(MISSING)), timedInvokeTimeout (%!@(MISSING)), serverSideProcessingTimeout (%!@(MISSING)), from device nodeID (%!@(MISSING)) for controllerID %!@(MISSING)"
+ "%!@(MISSING) Forwarding remote request to read multiple attributes: %!@(MISSING) from device nodeID (%!@(MISSING)) for controllerID %!@(MISSING)"
+ "%!@(MISSING) Forwarding remote request to readAttribute: endpointID (%!@(MISSING)), clusterID (%!@(MISSING)), attributeID (%!@(MISSING)), readParams (%!@(MISSING)) from device nodeID (%!@(MISSING)) for controllerID %!@(MISSING)"
+ "%!@(MISSING) Forwarding remote request to register nodeID: %!@(MISSING) for controllerID: %!@(MISSING)"
+ "%!@(MISSING) Forwarding remote request to unregister nodeID: %!@(MISSING) for controllerID: %!@(MISSING)"
+ "%!@(MISSING) Forwarding remote request to writeAttribute: endpointID (%!@(MISSING)), clusterID (%!@(MISSING)), attributeID (%!@(MISSING)), value (%!@(MISSING)) from device nodeID (%!@(MISSING)) for controllerID %!@(MISSING)"
+ "%!@(MISSING) Found existing controller %!@(MISSING) for entity UUID %!@(MISSING), ignoring add request"
+ "%!@(MISSING) Found no handler for incoming new session message; %!@(MISSING)"
+ "%!@(MISSING) Found session to remove: %!@(MISSING) for sessionID : %!@(MISSING)"
+ "%!@(MISSING) Got check-in context %!@(MISSING)"
+ "%!@(MISSING) IGNORING request to remove device controller: %!@(MISSING)"
+ "%!@(MISSING) Invalidating remote client"
+ "%!@(MISSING) Invalidating session %!@(MISSING)"
+ "%!@(MISSING) Invoking command on: endpointID (%!@(MISSING)), clusterID (%!@(MISSING)), commandID (%!@(MISSING)), commandFields (%!@(MISSING)), expectedValues (%!@(MISSING)),                      expectedValueInterval (%!@(MISSING)), timedInvokeTimeout (%!@(MISSING)), serverSideProcessingTimeout (%!@(MISSING)), from device nodeID (%!@(MISSING)) for message %!@(MISSING)"
+ "%!@(MISSING) Invoking delegate %!@(MISSING) to handle all messages for message: %!@(MISSING)"
+ "%!@(MISSING) MTRPlugin active clients: %!l(MISSING)u"
+ "%!@(MISSING) MatterPlugin is overridden to be in remote mode, forcing YES for isInRemoteMode"
+ "%!@(MISSING) No connection\u00a0found to _deliverMessagePayloadToPrimaryResident for message: %!@(MISSING)"
+ "%!@(MISSING) No known attributes to report"
+ "%!@(MISSING) Read %!l(MISSING)u remote bulk attributes from nodeID: %!@(MISSING), controllerID: %!@(MISSING) "
+ "%!@(MISSING) Reading attribute: endpointID (%!@(MISSING)), clusterID (%!@(MISSING)), attributeID (%!@(MISSING)), readParams (%!@(MISSING)) from local device nodeID (%!@(MISSING)) connection for message %!@(MISSING)"
+ "%!@(MISSING) Reading multiple attributes: (%!@(MISSING)), from local device nodeID (%!@(MISSING)) connection for message %!@(MISSING)"
+ "%!@(MISSING) Received attribute report for node ID: %!@(MISSING), report: %!@(MISSING)"
+ "%!@(MISSING) Received device became active for node ID: %!@(MISSING)"
+ "%!@(MISSING) Received device cache primed for node ID: %!@(MISSING)"
+ "%!@(MISSING) Received device configChanged for node ID: %!@(MISSING)"
+ "%!@(MISSING) Received device internal state changed for node ID: %!@(MISSING)"
+ "%!@(MISSING) Received error %!@(MISSING) in response for message: %!@(MISSING)"
+ "%!@(MISSING) Received event report for node ID: %!@(MISSING), report: %!@(MISSING)"
+ "%!@(MISSING) Received message %!@(MISSING) with new session identifier"
+ "%!@(MISSING) Received new session with identifier: %!@(MISSING)"
+ "%!@(MISSING) Received significant time changed notification, resetting all session times"
+ "%!@(MISSING) Received state changed for node ID: %!@(MISSING), state: %!@(MISSING)"
+ "%!@(MISSING) Receiver delegate %!@(MISSING) has no handler for message: %!@(MISSING)"
+ "%!@(MISSING) Registered session: %!@(MISSING) for sessionID : %!@(MISSING)  controllerID: %!@(MISSING)  homeID: %!@(MISSING)"
+ "%!@(MISSING) Registering for signification time change notifications"
+ "%!@(MISSING) Registering selector %!@(MISSING) for messageType: %!@(MISSING) on session: %!@(MISSING)"
+ "%!@(MISSING) Registering to receive new session and control channel information"
+ "%!@(MISSING) Remote controller %!@(MISSING) isRunning: %!@(MISSING)"
+ "%!@(MISSING) Remote device %!@(MISSING) running state is %!l(MISSING)u"
+ "%!@(MISSING) Removing client %!@(MISSING)  for xpc connection: %!@(MISSING)"
+ "%!@(MISSING) Removing client session with identifier: %!@(MISSING)"
+ "%!@(MISSING) Removing control channel delegate %!@(MISSING)"
+ "%!@(MISSING) Removing delegate %!@(MISSING) for session: %!@(MISSING)"
+ "%!@(MISSING) Removing run assertion on device controller: %!@(MISSING)"
+ "%!@(MISSING) Removing sessionID %!@(MISSING), since the peer rejected with an error message"
+ "%!@(MISSING) Reporting all known attributes %!l(MISSING)u"
+ "%!@(MISSING) Response received for message %!d(MISSING) (%!@(MISSING)) from controllerID %!@(MISSING)"
+ "%!@(MISSING) Response received for message %!d(MISSING) (%!@(MISSING)) from controllerID %!@(MISSING) with error: %!@(MISSING)"
+ "%!@(MISSING) Response received for message type %!d(MISSING) (%!@(MISSING)) from controllerID %!@(MISSING)"
+ "%!@(MISSING) Response received for message type %!d(MISSING) (%!@(MISSING)) from controllerID %!@(MISSING) with error: %!@(MISSING)"
+ "%!@(MISSING) Response received, updating timeOfActivity to: %!@(MISSING)"
+ "%!@(MISSING) Running read bulk attributes on total of %!l(MISSING)u requests for nodeID: %!@(MISSING), controllerID: %!@(MISSING)"
+ "%!@(MISSING) Running work item queue"
+ "%!@(MISSING) Sending request to resident controllerID: %!@(MISSING), for message type: %!d(MISSING)"
+ "%!@(MISSING) Sending request to resident controllerID: %!@(MISSING), nodeID: %!@(MISSING), for message type: %!d(MISSING)"
+ "%!@(MISSING) Setting delegate on device: %!@(MISSING)"
+ "%!@(MISSING) Starting Matter remote message transport over HomeKit Modern Transport"
+ "%!@(MISSING) Starting resident server to listen on incoming requests"
+ "%!@(MISSING) Stopping Matter remote message transport over HomeKit Modern Transport"
+ "%!@(MISSING) Stopping resident server from listening for incoming requests"
+ "%!@(MISSING) Successfully completed invokeCommand with response: %!@(MISSING)"
+ "%!@(MISSING) Successfully finished readAttribute with value: %!@(MISSING)"
+ "%!@(MISSING) Successfully finished readMultipleAttributes with value: %!@(MISSING)"
+ "%!@(MISSING) Successfully sent attribute report"
+ "%!@(MISSING) Successfully sent device became active"
+ "%!@(MISSING) Successfully sent device cache primed active"
+ "%!@(MISSING) Successfully sent device configChanged"
+ "%!@(MISSING) Successfully sent device internal state updated"
+ "%!@(MISSING) Successfully sent event report"
+ "%!@(MISSING) Successfully sent state changed report"
+ "%!@(MISSING) Taking run assertion on device controller: %!@(MISSING)"
+ "%!@(MISSING) Timer fired, running pending work items"
+ "%!@(MISSING) Total sessions %!l(MISSING)u reached above limit of %!l(MISSING)u, removing oldest session "
+ "%!@(MISSING) Unable to send message over to home hub since message is nil"
+ "%!@(MISSING) Unable to send message over to remote peer since message is nil"
+ "%!@(MISSING) Updating timeOfActivity to: %!@(MISSING)"
+ "%!@(MISSING) Writing attribute: endpointID (%!@(MISSING)), clusterID (%!@(MISSING)), attributeID (%!@(MISSING)), value (%!@(MISSING)) from local device nodeID (%!@(MISSING)) connection for message %!@(MISSING)"
+ "%!@(MISSING) _currentTarget: %!@(MISSING) suspended: %!@(MISSING) "
+ "%!@(MISSING) addDelegateForDevice: %!@(MISSING) interestedPathsForAttributes: %!@(MISSING) interestedPathsForEvents: %!@(MISSING)"
+ "%!@(MISSING) commandFields allKeys: %!@(MISSING)"
+ "%!@(MISSING) commandFields allObjects: %!@(MISSING)"
+ "%!@(MISSING) commandFields objectForKey: 'value' class: %!@(MISSING)"
+ "%!@(MISSING) commandFields: %!@(MISSING)"
+ "%!@(MISSING) controllerNodeIDWithReply controllerUUID %!@(MISSING)"
+ "%!@(MISSING) dealloc: %!p(MISSING)"
+ "%!@(MISSING) delegate denied access to operation: %!l(MISSING)d for %!@(MISSING)"
+ "%!@(MISSING) device %!@(MISSING) internalStateUpdated"
+ "%!@(MISSING) device %!@(MISSING) internalStateUpdated with value: %!@(MISSING)"
+ "%!@(MISSING) device %!@(MISSING) receivedAttributeReport %!@(MISSING), sending to remote controller"
+ "%!@(MISSING) device %!@(MISSING) receivedAttributeReport %!l(MISSING)d"
+ "%!@(MISSING) device %!@(MISSING) receivedEventReport %!@(MISSING)"
+ "%!@(MISSING) device %!@(MISSING) receivedEventReport %!l(MISSING)d"
+ "%!@(MISSING) device %!@(MISSING) stateChanged %!l(MISSING)u"
+ "%!@(MISSING) deviceBecameActive %!@(MISSING)"
+ "%!@(MISSING) deviceCachePrimed %!@(MISSING)"
+ "%!@(MISSING) deviceConfigurationChanged %!@(MISSING)"
+ "%!@(MISSING) deviceController %!@(MISSING) registerNodeID %!@(MISSING)"
+ "%!@(MISSING) deviceController %!@(MISSING) unregisterNodeID %!@(MISSING)"
+ "%!@(MISSING) downloadLogOfType not implemented"
+ "%!@(MISSING) failed to decode message for incoming controller request message %!@(MISSING)"
+ "%!@(MISSING) failed to decode message for incoming device request message %!@(MISSING)"
+ "%!@(MISSING) failed to decode read attribute message for incoming device request message %!@(MISSING)"
+ "%!@(MISSING) failed to decode read multiple attribute message for incoming device request message %!@(MISSING)"
+ "%!@(MISSING) failed to decode write attribute message for incoming device request message %!@(MISSING)"
+ "%!@(MISSING) failed to find controller for home for incoming request message %!@(MISSING)"
+ "%!@(MISSING) failed to find node for read attribute for incoming device request message %!@(MISSING)"
+ "%!@(MISSING) failed to find node for write attribute for incoming device request message %!@(MISSING)"
+ "%!@(MISSING) failed to find nodeID (%!@(MISSING)) for incoming device request message %!@(MISSING)"
+ "%!@(MISSING) failed to find nodeID for incoming device request message %!@(MISSING)"
+ "%!@(MISSING) forwardingTargetForSelector %!@(MISSING) to: %!@(MISSING)"
+ "%!@(MISSING) getDeviceCachePrimed controllerUUID %!@(MISSING) nodeID %!@(MISSING)"
+ "%!@(MISSING) getEstimatedStartTime controllerUUID %!@(MISSING) nodeID %!@(MISSING)"
+ "%!@(MISSING) getEstimatedSubscriptionLatency controllerUUID %!@(MISSING) nodeID %!@(MISSING)"
+ "%!@(MISSING) getIsRunningWithReply controllerUUID %!@(MISSING)"
+ "%!@(MISSING) getState controllerUUID %!@(MISSING) nodeID %!@(MISSING)"
+ "%!@(MISSING) getUniqueIdentifierWithReply controllerUUID %!@(MISSING)"
+ "%!@(MISSING) informing delegate to run a total of %!l(MISSING)u pending work items"
+ "%!@(MISSING) initWithClient %!@(MISSING)"
+ "%!@(MISSING) initialized with client %!@(MISSING)"
+ "%!@(MISSING) initialized with pluginClient %!@(MISSING)"
+ "%!@(MISSING) initialized with pluginClient %!@(MISSING) delegateID %!@(MISSING)"
+ "%!@(MISSING) initialized with xpcConnection %!@(MISSING)"
+ "%!@(MISSING) invalidate"
+ "%!@(MISSING) invalidating registered nodeIDs; %!@(MISSING)"
+ "%!@(MISSING) invokeCommandWithEndpointID controllerUUID %!@(MISSING) nodeID %!@(MISSING) endpointID %!@(MISSING) clusterID %!@(MISSING) commandID %!@(MISSING) commandFields %!@(MISSING) expectedValues %!@(MISSING) expectedValueInterval %!@(MISSING) timedInvokeTimeout %!@(MISSING)"
+ "%!@(MISSING) logState for %!l(MISSING)u devices:"
+ "%!@(MISSING) logState with %!l(MISSING)u delegate proxies:"
+ "%!@(MISSING) no delegate proxy is setup, so ensuring we have one for delegate id: %!@(MISSING)"
+ "%!@(MISSING) openCommissioningWindowWithSetupPasscode not implemented"
+ "%!@(MISSING) overridden to: %!l(MISSING)u"
+ "%!@(MISSING) readAttributePaths controllerUUID %!@(MISSING) nodeID %!@(MISSING) attributePaths %!@(MISSING)"
+ "%!@(MISSING) readAttributeWithEndpointID controllerUUID %!@(MISSING) nodeID %!@(MISSING) endpointID %!@(MISSING) clusterID %!@(MISSING) attribute %!@(MISSING) params %!@(MISSING)"
+ "%!@(MISSING) received invalid attribute report format from message: %!@(MISSING)"
+ "%!@(MISSING) received invalid device became active format from message: %!@(MISSING)"
+ "%!@(MISSING) received invalid device configurationChanged format from message: %!@(MISSING)"
+ "%!@(MISSING) received invalid device event report format from message: %!@(MISSING)"
+ "%!@(MISSING) received invalid device internalStateUpdated format from message: %!@(MISSING)"
+ "%!@(MISSING) received invalid device is cached primed format from message: %!@(MISSING)"
+ "%!@(MISSING) received invalid device state changed from message: %!@(MISSING)"
+ "%!@(MISSING) register nodeID: %!@(MISSING), forController: %!@(MISSING), device: %!@(MISSING)"
+ "%!@(MISSING) removing delegate on device: %!@(MISSING)"
+ "%!@(MISSING) responding to ShutdownController with success for message %!@(MISSING)"
+ "%!@(MISSING) responding to controller checkin with success for message %!@(MISSING)"
+ "%!@(MISSING) responding to controller get nodeID with: %!@(MISSING) for message %!@(MISSING)"
+ "%!@(MISSING) responding to controller get uniqueID with: %!@(MISSING) for message %!@(MISSING)"
+ "%!@(MISSING) responding to controller is running state with: %!@(MISSING) for message %!@(MISSING)"
+ "%!@(MISSING) responding to controller register(%!@(MISSING)) for nodeID: %!@(MISSING), for message %!@(MISSING)"
+ "%!@(MISSING) responding to device cachePrimed for nodeID: %!@(MISSING), for message %!@(MISSING)"
+ "%!@(MISSING) responding to device estimatedStartTime for nodeID: %!@(MISSING), for message %!@(MISSING)"
+ "%!@(MISSING) responding to device estimatedSubscriptionLatency for nodeID: %!@(MISSING), for message %!@(MISSING)"
+ "%!@(MISSING) responding to device read attribute for nodeID: %!@(MISSING), for message %!@(MISSING)"
+ "%!@(MISSING) responding to device read multiple attribute for nodeID: %!@(MISSING), for message %!@(MISSING)"
+ "%!@(MISSING) responding to device state for nodeID: %!@(MISSING), for message %!@(MISSING)"
+ "%!@(MISSING) responding to invoke command for nodeID: %!@(MISSING), for message %!@(MISSING)"
+ "%!@(MISSING) set to default value of: %!l(MISSING)u"
+ "%!@(MISSING) shutdownDeviceController controllerUUID %!@(MISSING)"
+ "%!@(MISSING) unregister nodeID: %!@(MISSING), forController: %!@(MISSING), device: %!@(MISSING)"
+ "%!@(MISSING) writeAttributeWithEndpointID controllerUUID %!@(MISSING) nodeID %!@(MISSING) endpointID %!@(MISSING) clusterID %!@(MISSING) attribute %!@(MISSING) value %!@(MISSING) expectedValueInterval %!@(MISSING) timedWriteTimeout %!@(MISSING)"
+ "(unknown: %!i(MISSING))"
+ "** Tried to register nil device"
+ "** Tried to unregister nil device"
+ "*** IGNORING Stopping MTRPlugin: %!p(MISSING)"
+ "5"
+ "<%!@(MISSING) : %!p(MISSING)>"
+ "<%!@(MISSING): %!@(MISSING), entityIdentifier: %!@(MISSING)>"
+ "<%!@(MISSING): %!p(MISSING) client %!@(MISSING)>"
+ "<%!@(MISSING): %!p(MISSING) client: %!@(MISSING)>"
+ "<%!@(MISSING): %!p(MISSING) delegateID %!@(MISSING)>"
+ "<%!@(MISSING): %!p(MISSING) sid: %!@(MISSING) hid: %!@(MISSING) lastActivity: %!@(MISSING)>"
+ "<%!@(MISSING): %!p(MISSING) xpc %!p(MISSING) pid: %!d(MISSING) UUID: %!@(MISSING) Home: %!@(MISSING) Running: %!@(MISSING)>"
+ "<%!@(MISSING): %!p(MISSING) xpc %!p(MISSING) pid: %!d(MISSING)>"
+ "<%!@(MISSING): %!p(MISSING)>"
+ "<MTRPluginPBMHeader: uniqueIdentifier: %!@(MISSING), messageType: %!u(MISSING) (%!@(MISSING)) , sessionIdentifier: %!@(MISSING), homeIdentifier: %!@(MISSING), direction: %!@(MISSING)>"
+ "<MTRPluginProtobufMessage: uniqueIdentifier: %!@(MISSING), messageType: %!u(MISSING) (%!@(MISSING)), sessionIdentifier: %!@(MISSING), homeIdentifier: %!@(MISSING), isRequest: %!@(MISSING)>"
+ "<MTRPluginProtobufMessageReceiver: delegate: %!p(MISSING)>"
+ "<MTRPluginTimedWatermarkQueue: watermarkLevel: %!l(MISSING)u, waitPeriod: %!l(MISSING)f, waitingWorkItems size %!l(MISSING)u>"
+ "="
+ "@"
+ "@\"<MTRPluginClientConnectionDelegate>\""
+ "@\"<MTRPluginProtobufMessageTransport>\""
+ "@\"<MTRPluginProtobufMessageTransportDelegate>\""
+ "@\"<MTRPluginServerDelegate>\""
+ "@\"<MTRPluginTimedWatermarkQueueDelegate>\""
+ "@\"HMFTimer\""
+ "@\"MTRDeviceController\""
+ "@\"MTRPluginClient\""
+ "@\"MTRPluginClientXPCProxy\""
+ "@\"MTRPluginLocalClient\""
+ "@\"MTRPluginLocalDispatch\""
+ "@\"MTRPluginPBMAttributePath\""
+ "@\"MTRPluginPBMClusterPath\""
+ "@\"MTRPluginPBMCommandPath\""
+ "@\"MTRPluginPBMDate\""
+ "@\"MTRPluginPBMDeviceNode\""
+ "@\"MTRPluginPBMError\""
+ "@\"MTRPluginPBMEventPath\""
+ "@\"MTRPluginPBMHeader\""
+ "@\"MTRPluginPBMReadParams\""
+ "@\"MTRPluginPBMURL\""
+ "@\"MTRPluginPBMUUID\""
+ "@\"MTRPluginPBMVariableValue\""
+ "@\"MTRPluginPBMVariableValueDictionary\""
+ "@\"MTRPluginPBMVariableValueList\""
+ "@\"MTRPluginProtobufMessageDispatcher\""
+ "@\"MTRPluginProtobufMessageReceiver\""
+ "@\"MTRPluginRemoteClient\""
+ "@\"MTRPluginTimedWatermarkQueue\""
+ "@\"NSArray\""
+ "@\"NSData\""
+ "@\"NSDate\""
+ "@\"NSDictionary\""
+ "@\"NSMutableSet\""
+ "@\"NSNumber\""
+ "@\"NSString\""
+ "@\"NSUUID\""
+ "@\"NSXPCConnection\""
+ "@20@0:8I16"
+ "@20@0:8i16"
+ "@24@0:8Q16"
+ "@24@0:8^{_NSZone=}16"
+ "@28@0:8@16B24"
+ "@32@0:8@16@?24"
+ "@32@0:8@16^@24"
+ "@32@0:8Q16d24"
+ "@36@0:8@16@24i32"
+ "@56@0:8@16@24@32@40@48"
+ "@56@0:8@16B24i28@32@40@48"
+ "@64@0:8@16@24@32@40@48@56"
+ "@72@0:8@16@24@32@40@48@56@64"
+ "@88@0:8@16@24@32@40@48@56@64@72@80"
+ "@?"
+ "@?16@0:8"
+ "Adding client connection: %!@(MISSING)"
+ "AttributeReport"
+ "B"
+ "B32@0:8@\"NSNumber\"16@\"NSUUID\"24"
+ "B32@0:8@16@24"
+ "B32@0:8@16@?24"
+ "B40@0:8@\"NSNumber\"16:24@\"NSUUID\"32"
+ "B40@0:8@16:24@32"
+ "B40@0:8@16@24@32"
+ "B44@0:8@16@24@32B40"
+ "BecameActive"
+ "CachePrimed"
+ "ConfigurationChanged"
+ "ControllerCheckin"
+ "ERROR: Attribute read disallowed over XPC: EP %!@(MISSING), Cluster %!@(MISSING), Attribute %!@(MISSING)"
+ "ERROR: Attribute write disallowed over XPC: EP %!@(MISSING), Cluster %!@(MISSING), Attribute %!@(MISSING)"
+ "ERROR: Command disallowed over XPC: EP %!@(MISSING), Cluster %!@(MISSING), Command %!@(MISSING)"
+ "EventReport"
+ "Exception forwarding MTRXPCClientProtocol method: %!@(MISSING)"
+ "Failed to create message header %!@(MISSING) from protobuf data"
+ "GetControllerNodeID"
+ "GetControllerUniqueID"
+ "GetEstimatedStartTime"
+ "GetEstimatedSubscriptionLatency"
+ "GetIsCachePrimed"
+ "GetIsControllerRunning"
+ "GetState"
+ "HMDHomeMatterRequestKey"
+ "HMDHomeMatterRequestProtobufPayloadKey"
+ "HMFTimerDelegate"
+ "Helpers"
+ "I"
+ "I16@0:8"
+ "InternalStateUpdated"
+ "Invalidating MTRPluginClientConnection: %!@(MISSING)"
+ "InvokeCommand"
+ "MATTER_V1"
+ "MTRDeviceControllerDelegate"
+ "MTRDeviceControllerEntity"
+ "MTRPluginClient"
+ "MTRPluginClientConnection"
+ "MTRPluginClientManager"
+ "MTRPluginClientQueue"
+ "MTRPluginClientXPCProxy"
+ "MTRPluginLocalClient"
+ "MTRPluginLocalClient dealloc: %!p(MISSING)"
+ "MTRPluginLocalDeviceDelegateProxy"
+ "MTRPluginLocalDeviceDelegateProxy dealloc: %!p(MISSING)"
+ "MTRPluginLocalDispatch"
+ "MTRPluginMaxActiveClientSessions"
+ "MTRPluginPBMAttributePath"
+ "MTRPluginPBMClusterPath"
+ "MTRPluginPBMCommandPath"
+ "MTRPluginPBMDate"
+ "MTRPluginPBMDeviceControllerMessage"
+ "MTRPluginPBMDeviceNode"
+ "MTRPluginPBMDeviceNodeInvokeCommmandMessage"
+ "MTRPluginPBMDeviceNodeMessage"
+ "MTRPluginPBMDeviceNodeReadAttributeMessage"
+ "MTRPluginPBMDeviceNodeReadMultipleAttributesMessage"
+ "MTRPluginPBMDeviceNodeWriteAttributeMessage"
+ "MTRPluginPBMError"
+ "MTRPluginPBMEventPath"
+ "MTRPluginPBMHeader"
+ "MTRPluginPBMHeaderMessage"
+ "MTRPluginPBMReadParams"
+ "MTRPluginPBMURL"
+ "MTRPluginPBMUUID"
+ "MTRPluginPBMVariableKeyValuePair"
+ "MTRPluginPBMVariableValue"
+ "MTRPluginPBMVariableValueDictionary"
+ "MTRPluginPBMVariableValueList"
+ "MTRPluginPBMVariableValueResponseMessage"
+ "MTRPluginPairType"
+ "MTRPluginProtobufMessage"
+ "MTRPluginProtobufMessageDispatcher"
+ "MTRPluginProtobufMessageReceiver"
+ "MTRPluginProtobufMessageTransport"
+ "MTRPluginProtobufMessageTransportDelegate"
+ "MTRPluginProtobufOverModernTransport"
+ "MTRPluginReadAttributeWorkItem"
+ "MTRPluginRemoteClient"
+ "MTRPluginResidentClientSession"
+ "MTRPluginResidentServer"
+ "MTRPluginResidentServerQueue"
+ "MTRPluginServer"
+ "MTRPluginThirdPartyExclusions"
+ "MTRPluginTimedWatermarkQueue"
+ "MTRPluginTimedWatermarkQueueDelegate"
+ "MTRPluginWorkItem"
+ "MTRXPCClientProtocol"
+ "MTRXPCClientProtocol_MTRDevice"
+ "MTRXPCClientProtocol_MTRDeviceController"
+ "MTRXPCServerProtocol"
+ "MTRXPCServerProtocol_MTRDevice"
+ "MTRXPCServerProtocol_MTRDeviceController"
+ "MatterPlugin is NOT overridden to be in remote mode"
+ "MatterPluginAlwaysEnableIsInRemoteMode"
+ "NSCopying"
+ "Oneway"
+ "Q"
+ "ReadAttribute"
+ "ReadMultipleAttributes"
+ "RegisterNodeID"
+ "Removing client connection: %!@(MISSING)"
+ "Request"
+ "Response"
+ "Resuming MTRPluginClientConnection: %!@(MISSING)"
+ "SCHEMA_V1"
+ "Setting up MTRPluginClientConnection: %!@(MISSING) pluginClient : %!@(MISSING)"
+ "ShutdownController"
+ "SignificantTimeChangeNotification"
+ "Starting MTRPluginServer: %!p(MISSING)"
+ "StateChanged"
+ "Stopping MTRPluginServer: %!p(MISSING)"
+ "StringAsMessageDirection:"
+ "StringAsProtocol:"
+ "StringAsSchema:"
+ "StringAsVersion:"
+ "T@\"<MTRPluginClientConnectionDelegate>\",&,V_delegate"
+ "T@\"<MTRPluginProtobufMessageTransport>\",&,V_transport"
+ "T@\"<MTRPluginProtobufMessageTransportDelegate>\",W,V_delegate"
+ "T@\"<MTRPluginServerDelegate>\",&,V_delegate"
+ "T@\"<MTRPluginTimedWatermarkQueueDelegate>\",W,V_delegate"
+ "T@\"HMFTimer\",&,V_waitPeriodTimer"
+ "T@\"MTRAttributePath\",&,N"
+ "T@\"MTRClusterPath\",&,N"
+ "T@\"MTRCommandPath\",&,N"
+ "T@\"MTRDeviceController\",&,V_controller"
+ "T@\"MTRDeviceController\",R,&"
+ "T@\"MTREventPath\",&,N"
+ "T@\"MTRPluginClient\",&,V_pluginClient"
+ "T@\"MTRPluginClient\",W,V_client"
+ "T@\"MTRPluginClientXPCProxy\",&,V_clientProxy"
+ "T@\"MTRPluginLocalClient\",&,V_localClient"
+ "T@\"MTRPluginLocalClient\",W,V_pluginClient"
+ "T@\"MTRPluginLocalDispatch\",&,V_dispatch"
+ "T@\"MTRPluginPBMAttributePath\",&,N,V_attributePath"
+ "T@\"MTRPluginPBMAttributePath\",&,N,V_attributePathValue"
+ "T@\"MTRPluginPBMClusterPath\",&,N,V_clusterPath"
+ "T@\"MTRPluginPBMClusterPath\",&,N,V_clusterPathValue"
+ "T@\"MTRPluginPBMCommandPath\",&,N,V_commandPath"
+ "T@\"MTRPluginPBMCommandPath\",&,N,V_commandPathValue"
+ "T@\"MTRPluginPBMDate\",&,N,V_dateValue"
+ "T@\"MTRPluginPBMDeviceNode\",&,N,V_node"
+ "T@\"MTRPluginPBMError\",&,N,V_errorValue"
+ "T@\"MTRPluginPBMEventPath\",&,N,V_eventPathValue"
+ "T@\"MTRPluginPBMHeader\",&,N,V_header"
+ "T@\"MTRPluginPBMHeader\",C,V_messageHeader"
+ "T@\"MTRPluginPBMReadParams\",&,N,V_readParams"
+ "T@\"MTRPluginPBMURL\",&,N,V_urlValue"
+ "T@\"MTRPluginPBMUUID\",&,N,V_controllerID"
+ "T@\"MTRPluginPBMUUID\",&,N,V_homeID"
+ "T@\"MTRPluginPBMUUID\",&,N,V_messageID"
+ "T@\"MTRPluginPBMUUID\",&,N,V_sessionID"
+ "T@\"MTRPluginPBMUUID\",&,N,V_uuidValue"
+ "T@\"MTRPluginPBMVariableValue\",&,N,V_commandFields"
+ "T@\"MTRPluginPBMVariableValue\",&,N,V_minEventNumber"
+ "T@\"MTRPluginPBMVariableValue\",&,N,V_value"
+ "T@\"MTRPluginPBMVariableValueDictionary\",&,N,V_dictionaryValue"
+ "T@\"MTRPluginPBMVariableValueList\",&,N,V_arrayValue"
+ "T@\"MTRPluginPBMVariableValueList\",&,N,V_expectedValues"
+ "T@\"MTRPluginPBMVariableValueList\",&,N,V_setValue"
+ "T@\"MTRPluginProtobufMessageDispatcher\",&,V_messageDispatcher"
+ "T@\"MTRPluginProtobufMessageReceiver\",&,V_controlChannelReceiver"
+ "T@\"MTRPluginRemoteClient\",&,V_remoteClient"
+ "T@\"MTRPluginTimedWatermarkQueue\",&,V_timedWatermarkQueue"
+ "T@\"MTRReadParams\",&,N"
+ "T@\"NSArray\",C,N"
+ "T@\"NSArray\",R,&,V_controllers"
+ "T@\"NSArray\",R,N"
+ "T@\"NSData\",&,N,V_dataValue"
+ "T@\"NSData\",C,V_messageData"
+ "T@\"NSDate\",&,N"
+ "T@\"NSDate\",&,V_timeOfLastActivity"
+ "T@\"NSDictionary\",&,V_context"
+ "T@\"NSDictionary\",C,N"
+ "T@\"NSError\",&,N"
+ "T@\"NSMutableArray\",&,N,V_attributePaths"
+ "T@\"NSMutableArray\",&,N,V_pairs"
+ "T@\"NSMutableArray\",&,N,V_values"
+ "T@\"NSMutableArray\",&,V_clients"
+ "T@\"NSMutableArray\",&,V_sessions"
+ "T@\"NSMutableArray\",&,V_waitingWorkItems"
+ "T@\"NSMutableArray\",C,V_controllerEntities"
+ "T@\"NSMutableDictionary\",&,V_context"
+ "T@\"NSMutableDictionary\",&,V_delegateProxies"
+ "T@\"NSMutableDictionary\",&,V_messageSelectors"
+ "T@\"NSMutableSet\",&,V__clientConnections"
+ "T@\"NSMutableSet\",&,V_devices"
+ "T@\"NSMutableSet\",&,V_messageReceivers"
+ "T@\"NSMutableSet\",&,V_registeredMTRDevices"
+ "T@\"NSMutableSet\",&,V_registeredNodeIDs"
+ "T@\"NSNumber\",&,V_attributeID"
+ "T@\"NSNumber\",&,V_clusterID"
+ "T@\"NSNumber\",&,V_delegateID"
+ "T@\"NSNumber\",&,V_endpointID"
+ "T@\"NSNumber\",&,V_nodeID"
+ "T@\"NSNumber\",R,C"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_delegateQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",&,V_workQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",R,&,V_queue"
+ "T@\"NSSet\",C,N"
+ "T@\"NSSet\",R,&"
+ "T@\"NSString\",&,N,V_domain"
+ "T@\"NSString\",&,N,V_key"
+ "T@\"NSString\",&,N,V_stringValue"
+ "T@\"NSString\",&,N,V_value"
+ "T@\"NSURL\",&,N"
+ "T@\"NSUUID\",&,N"
+ "T@\"NSUUID\",&,V_UUID"
+ "T@\"NSUUID\",&,V_controllerID"
+ "T@\"NSUUID\",&,V_homeID"
+ "T@\"NSUUID\",&,V_homeUUID"
+ "T@\"NSUUID\",&,V_sessionID"
+ "T@\"NSUUID\",C,V_controllerUUIDForAssertion"
+ "T@\"NSUUID\",C,V_entityIdentifier"
+ "T@\"NSUUID\",R,C"
+ "T@\"NSXPCConnection\",&,V_connection"
+ "T@\"NSXPCConnection\",&,V_xpcConnection"
+ "T@,&,N"
+ "T@,&,V_first"
+ "T@,&,V_peerAddress"
+ "T@,&,V_second"
+ "T@,&,V_sourceAddress"
+ "T@?,C,V_responseHandler"
+ "TB,GisRunning,V_running"
+ "TB,N"
+ "TB,N,V_assumeUnknownAttributesReportable"
+ "TB,N,V_filterByFabric"
+ "TB,R,GisInRemoteMode"
+ "TB,R,GisRequest"
+ "TB,R,GisValid"
+ "TB,R,N"
+ "TB,R,N,GisValid"
+ "TB,V_backgroundModeEntitled"
+ "TB,V_running"
+ "TI,N,V_attributeID"
+ "TI,N,V_clusterID"
+ "TI,N,V_commandID"
+ "TI,N,V_endpointID"
+ "TI,N,V_eventID"
+ "TI,N,V_messageType"
+ "TQ,N,V_code"
+ "TQ,N,V_expectedValueInterval"
+ "TQ,N,V_nodeID"
+ "TQ,N,V_serverSideProcessingTimeout"
+ "TQ,N,V_timedInvokeTimeout"
+ "TQ,N,V_timedWriteTimeout"
+ "TQ,N,V_unsignedIntegerValue"
+ "TQ,V_watermarkLevel"
+ "Td,N,V_doubleValue"
+ "Td,N,V_value"
+ "Td,V_repeatStateLoggingInterval"
+ "Td,V_responseTimeout"
+ "Td,V_waitPeriod"
+ "Ti,N,V_messageDirection"
+ "Ti,N,V_protocol"
+ "Ti,N,V_schema"
+ "Ti,N,V_version"
+ "Ti,V_pid"
+ "Tq,N,V_integerValue"
+ "UUID"
+ "UnregisterNodeID"
+ "VERSION_V1"
+ "Vv104@0:8@\"NSUUID\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@56@\"NSArray\"64@\"NSNumber\"72@\"NSNumber\"80@\"NSNumber\"88@?<v@?@\"NSArray\"@\"NSError\">96"
+ "Vv104@0:8@16@24@32@40@48@56@64@72@80@88@?96"
+ "Vv24@0:8@\"NSNumber\"16"
+ "Vv24@0:8@16"
+ "Vv32@0:8@\"NSNumber\"16@\"NSArray\"24"
+ "Vv32@0:8@\"NSNumber\"16@\"NSDictionary\"24"
+ "Vv32@0:8@\"NSNumber\"16Q24"
+ "Vv32@0:8@\"NSUUID\"16@\"NSDictionary\"24"
+ "Vv32@0:8@\"NSUUID\"16@\"NSNumber\"24"
+ "Vv32@0:8@\"NSUUID\"16@\"NSUUID\"24"
+ "Vv32@0:8@\"NSUUID\"16@?<v@?@\"NSNumber\">24"
+ "Vv32@0:8@\"NSUUID\"16@?<v@?@\"NSUUID\">24"
+ "Vv32@0:8@\"NSUUID\"16@?<v@?B>24"
+ "Vv32@0:8@16@24"
+ "Vv32@0:8@16@?24"
+ "Vv32@0:8@16Q24"
+ "Vv40@0:8@\"NSUUID\"16@\"NSNumber\"24@?<v@?@\"NSDate\">32"
+ "Vv40@0:8@\"NSUUID\"16@\"NSNumber\"24@?<v@?@\"NSNumber\">32"
+ "Vv40@0:8@\"NSUUID\"16@\"NSNumber\"24@?<v@?B>32"
+ "Vv40@0:8@\"NSUUID\"16@\"NSNumber\"24@?<v@?Q>32"
+ "Vv40@0:8@16@24@?32"
+ "Vv48@0:8@\"NSUUID\"16@\"NSNumber\"24@\"NSArray\"32@?<v@?@\"NSArray\">40"
+ "Vv48@0:8@16@24@32@?40"
+ "Vv48@0:8q16@\"NSNumber\"24d32@?<v@?@\"NSURL\"@\"NSError\">40"
+ "Vv48@0:8q16@24d32@?40"
+ "Vv64@0:8@\"NSUUID\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@?<v@?@\"MTRSetupPayload\"@\"NSError\">56"
+ "Vv64@0:8@16@24@32@40@48@?56"
+ "Vv72@0:8@\"NSUUID\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@\"MTRReadParams\"56@?<v@?@\"NSDictionary\">64"
+ "Vv72@0:8@16@24@32@40@48@56@?64"
+ "Vv80@0:8@\"NSUUID\"16@\"NSNumber\"24@\"NSNumber\"32@\"NSNumber\"40@\"NSNumber\"48@56@\"NSNumber\"64@\"NSNumber\"72"
+ "Vv80@0:8@16@24@32@40@48@56@64@72"
+ "WriteAttribute"
+ "_UUID"
+ "__clientConnections"
+ "__kickWaitingItemsDueToTimerExpiration:"
+ "_arrayValue"
+ "_assumeUnknownAttributesReportable"
+ "_attributeID"
+ "_attributePath"
+ "_attributePathValue"
+ "_attributePaths"
+ "_backgroundModeEntitled"
+ "_checkForMaxSessionsLimit"
+ "_client"
+ "_clientConnections"
+ "_clientProxy"
+ "_clientSessionForSessionID:"
+ "_clients"
+ "_clusterID"
+ "_clusterPath"
+ "_clusterPathValue"
+ "_code"
+ "_commandFields"
+ "_commandID"
+ "_commandPath"
+ "_commandPathValue"
+ "_connection"
+ "_context"
+ "_controlChannelReceiver"
+ "_controller"
+ "_controllerEntities"
+ "_controllerID"
+ "_controllerUUIDForAssertion"
+ "_convertArray:"
+ "_currentTarget"
+ "_dataValue"
+ "_dateValue"
+ "_delegateID"
+ "_delegateProxies"
+ "_deliverMessagePayloadToPrimaryResident:responseHandler:"
+ "_deliverMessageToDelegate:homeUUID:"
+ "_deregisterForSignificantTimeChangeNotifications"
+ "_deviceControllerEntityForIdentifier:"
+ "_deviceForControllerUUID:nodeID:"
+ "_deviceNodeMessageForDevice:messageValue:"
+ "_devices"
+ "_dictionaryFromCommandFields:"
+ "_dictionaryValue"
+ "_dispatch"
+ "_domain"
+ "_doubleValue"
+ "_endpointID"
+ "_entityIdentifier"
+ "_errorValue"
+ "_eventID"
+ "_eventPathValue"
+ "_expectedValueInterval"
+ "_expectedValues"
+ "_filterByFabric"
+ "_findClientForXPCConnection:remove:"
+ "_findMessageReceiverMatchingDelegate:"
+ "_findMessageReceiverMatchingSessionID:"
+ "_first"
+ "_handleNodeIDRegistrationRequestChangeForMessage:registerNodeID:"
+ "_handleResponseWithPayload:error:forMessage:"
+ "_has"
+ "_header"
+ "_homeID"
+ "_homeUUID"
+ "_injectAttributeReport:fromSubscription:"
+ "_injectEventReport:"
+ "_integerValue"
+ "_interfaceForClientProtocol"
+ "_interfaceForServerProtocol"
+ "_isRunning"
+ "_key"
+ "_localClient"
+ "_localTarget"
+ "_messageData"
+ "_messageDirection"
+ "_messageDispatcher"
+ "_messageHeader"
+ "_messageID"
+ "_messageReceivers"
+ "_messageSelectors"
+ "_messageType"
+ "_minEventNumber"
+ "_node"
+ "_nodeID"
+ "_pairs"
+ "_peerAddress"
+ "_pid"
+ "_pluginClient"
+ "_protocol"
+ "_readParams"
+ "_registerDevice:"
+ "_registerForMessages"
+ "_registerForSignificantTimeChangeNotifications"
+ "_registerNodeID:"
+ "_registerSessionForSessionID:incomingNewMessage:"
+ "_registeredMTRDevices"
+ "_registeredNodeIDs"
+ "_remoteClient"
+ "_remoteTarget"
+ "_repeatStateLoggingInterval"
+ "_responseHandler"
+ "_responseTimeout"
+ "_running"
+ "_scheduleNextStateLog"
+ "_schema"
+ "_second"
+ "_sendMessageToControllerWithID:messageType:pbCodable:errorBlock:replyBlock:"
+ "_sendMessageToPrimaryHomeHub:"
+ "_sendMessageToRemotePeer:peerDestination:"
+ "_serverSideProcessingTimeout"
+ "_sessionID"
+ "_sessions"
+ "_setObject:"
+ "_setValue"
+ "_setupConnection"
+ "_sourceAddress"
+ "_startStateLoggingIfNeeded"
+ "_stopStateLogging"
+ "_stringValue"
+ "_timeOfLastActivity"
+ "_timedInvokeTimeout"
+ "_timedWatermarkQueue"
+ "_timedWriteTimeout"
+ "_transport"
+ "_unregisterDevice:"
+ "_unregisterNodeID:"
+ "_unregisterSessionForSessionID:"
+ "_unsignedIntegerValue"
+ "_urlValue"
+ "_uuidValue"
+ "_validateAndFindDeviceControllerForMessage:deviceControllerMessage:"
+ "_validateAndFindDeviceControllerMatchingHomeInMessage:"
+ "_validateAndFindDeviceNodeForMessage:"
+ "_value"
+ "_values"
+ "_version"
+ "_waitPeriod"
+ "_waitPeriodTimer"
+ "_waitingWorkItems"
+ "_watermarkLevel"
+ "_workQueue"
+ "absoluteString"
+ "addAttributePaths:"
+ "addClientConnection:"
+ "addClientForXPCConnection:"
+ "addDelegate:queue:"
+ "addDelegateForDevice:interestedPathsForAttributes:interestedPathsForEvents:"
+ "addDeviceController:forEntityWithIdentifier:"
+ "addDeviceControllerDelegate:queue:"
+ "addDeviceDelegateProxy:"
+ "addObserver:selector:name:object:"
+ "addPair:"
+ "addRunAssertion"
+ "addValue:"
+ "addWorkItem:"
+ "allKeys"
+ "allObjects"
+ "allocWithZone:"
+ "arrayValue"
+ "arrayWithCapacity:"
+ "arrayWithObjects:count:"
+ "assumeUnknownAttributesReportable"
+ "attribute"
+ "attributePath"
+ "attributePathValue"
+ "attributePathWithEndpointID:clusterID:attributeID:"
+ "attributePaths"
+ "attributePathsAtIndex:"
+ "attributePathsCount"
+ "attributePathsType"
+ "attributeReadDisallowedOverXPCWithEndpointID:clusterID:attribute:isPrivatelyEntitled:"
+ "attributeRequestPaths"
+ "attributeWriteDisallowedOverXPCWithEndpointID:clusterID:attribute:isPrivatelyEntitled:"
+ "backgroundModeEntitled"
+ "boolValue"
+ "callRemoteProxyObject:"
+ "cancel"
+ "clearAttributePaths"
+ "clearPairs"
+ "clearValues"
+ "client"
+ "clientConnections"
+ "clientForXPCConnection:"
+ "clientProxy"
+ "clients"
+ "cluster"
+ "clusterPath"
+ "clusterPathValue"
+ "clusterPathWithEndpointID:clusterID:"
+ "code"
+ "com.apple.private.homekit"
+ "command"
+ "commandDisallowedOverXPCWithEndpointID:clusterID:commandID:isPrivatelyEntitled:"
+ "commandPath"
+ "commandPathValue"
+ "commandPathWithEndpointID:clusterID:commandID:"
+ "connection"
+ "connection:allowsOperationWithHome:operationType:nodeId:commandId:endpointId:clusterId:attributeId:"
+ "connection:sendMessagePayloadToPrimaryResident:responseHandler:error:"
+ "connectionIsPrivatelyEntitled:"
+ "context"
+ "controlChannelReceiver"
+ "controller"
+ "controller:commissioningComplete:"
+ "controller:commissioningComplete:nodeID:"
+ "controller:commissioningComplete:nodeID:metrics:"
+ "controller:commissioningSessionEstablishmentDone:"
+ "controller:isSuspended:"
+ "controller:readCommissioningInfo:"
+ "controller:statusUpdate:"
+ "controller:suspendedChangedTo:"
+ "controllerEntities"
+ "controllerID"
+ "controllerUUIDForAssertion"
+ "copy"
+ "copyTo:"
+ "copyWithZone:"
+ "d"
+ "d16@0:8"
+ "data"
+ "dataValue"
+ "date"
+ "dateValue"
+ "dealloc"
+ "defaultCenter"
+ "delegate"
+ "delegateID"
+ "delegateProxies"
+ "delegateQueue"
+ "deregisterForRequestMessageWithType:forSessionID:"
+ "destination"
+ "device:internalStateUpdated:"
+ "deviceCachePrimed"
+ "deviceController:checkInWithContext:"
+ "deviceController:controllerNodeIDWithReply:"
+ "deviceController:getIsRunningWithReply:"
+ "deviceController:getUniqueIdentifierWithReply:"
+ "deviceController:nodeID:getDeviceCachePrimedWithReply:"
+ "deviceController:nodeID:getEstimatedStartTimeWithReply:"
+ "deviceController:nodeID:getEstimatedSubscriptionLatencyWithReply:"
+ "deviceController:nodeID:getStateWithReply:"
+ "deviceController:nodeID:invokeCommandWithEndpointID:clusterID:commandID:commandFields:expectedValues:expectedValueInterval:timedInvokeTimeout:serverSideProcessingTimeout:completion:"
+ "deviceController:nodeID:openCommissioningWindowWithSetupPasscode:discriminator:duration:completion:"
+ "deviceController:nodeID:readAttributePaths:withReply:"
+ "deviceController:nodeID:readAttributeWithEndpointID:clusterID:attributeID:params:withReply:"
+ "deviceController:nodeID:writeAttributeWithEndpointID:clusterID:attributeID:value:expectedValueInterval:timedWriteTimeout:"
+ "deviceController:registerNodeID:"
+ "deviceController:shutdownDeviceController:"
+ "deviceController:unregisterNodeID:"
+ "deviceControllerForUUID:"
+ "deviceControllerMessageFromMessage:"
+ "deviceDelegateProxyForDelegateID:"
+ "deviceNodeInvokeCommandMessageFromMessage:"
+ "deviceNodeInvokeCommandMessageWithNodeID:invokeCommandWithEndpointID:clusterID:commandID:commandFields:expectedValues:expectedValueInterval:timedInvokeTimeout:serverSideProcessingTimeout:"
+ "deviceNodeMessageFromMessage:"
+ "deviceNodeMessageWithNodeID:"
+ "deviceNodeReadAttributeMessageFromMessage:"
+ "deviceNodeReadAttributeMessageWithNodeID:endpointID:clusterID:attributeID:readParams:"
+ "deviceNodeReadMultipleAttributesMessageFromMessage:"
+ "deviceNodeReadMultipleAttributesMessageWithNodeID:readAttributePaths:"
+ "deviceNodeWithNodeID:"
+ "deviceNodeWriteAttributeMessageFromMessage:"
+ "deviceNodeWriteAttributeMessageWithNodeID:endpointID:clusterID:attributeID:value:expectedValueInterval:timedWriteTimeout:"
+ "devices"
+ "dictionaryRepresentation"
+ "dictionaryValue"
+ "dictionaryWithObjects:forKeys:count:"
+ "dispatch"
+ "dispatchIncomingMessage:"
+ "domain"
+ "doubleValue"
+ "downloadLogOfType:nodeID:timeout:completion:"
+ "empty controller UUID or nodeID, bailing"
+ "endpoint"
+ "ensureControllerAssertionWithUUID:"
+ "ensureDelegateProxySetup"
+ "entityIdentifier"
+ "enumerateKeysAndObjectsUsingBlock:"
+ "errorValue"
+ "errorWithDomain:code:userInfo:"
+ "estimatedSubscriptionLatency"
+ "event"
+ "eventID"
+ "eventPath"
+ "eventPathValue"
+ "eventPathWithEndpointID:clusterID:eventID:"
+ "first"
+ "firstObject"
+ "forwardInvocation:"
+ "forwardingTargetForSelector:"
+ "getAllAttributesReport"
+ "handleIncomingMessage:"
+ "handleNewSessionSetupForMessage:transport:errorBlock:"
+ "hasArrayValue"
+ "hasAssumeUnknownAttributesReportable"
+ "hasAttributeID"
+ "hasAttributePath"
+ "hasAttributePathValue"
+ "hasClusterID"
+ "hasClusterPath"
+ "hasClusterPathValue"
+ "hasCode"
+ "hasCommandFields"
+ "hasCommandID"
+ "hasCommandPath"
+ "hasCommandPathValue"
+ "hasControllerID"
+ "hasDataValue"
+ "hasDateValue"
+ "hasDictionaryValue"
+ "hasDomain"
+ "hasDoubleValue"
+ "hasEndpointID"
+ "hasErrorValue"
+ "hasEventID"
+ "hasEventPathValue"
+ "hasExpectedValueInterval"
+ "hasExpectedValues"
+ "hasFilterByFabric"
+ "hasHeader"
+ "hasHomeID"
+ "hasIntegerValue"
+ "hasKey"
+ "hasMessageDirection"
+ "hasMessageID"
+ "hasMessageType"
+ "hasMinEventNumber"
+ "hasNode"
+ "hasNodeID"
+ "hasProtocol"
+ "hasReadParams"
+ "hasSchema"
+ "hasServerSideProcessingTimeout"
+ "hasSessionID"
+ "hasSetValue"
+ "hasStringValue"
+ "hasTimedInvokeTimeout"
+ "hasTimedWriteTimeout"
+ "hasUnsignedIntegerValue"
+ "hasUrlValue"
+ "hasUuidValue"
+ "hasValue"
+ "hasVersion"
+ "header"
+ "hmf_dataForKey:"
+ "homeID"
+ "homeIdentifier"
+ "homeUUID"
+ "i"
+ "i16@0:8"
+ "i24@0:8@16"
+ "identifier"
+ "inRemoteMode"
+ "indexSetWithIndexesInRange:"
+ "initWithArray:"
+ "initWithAttributePath:"
+ "initWithCapacity:"
+ "initWithClient:"
+ "initWithClient:queue:"
+ "initWithClientConnection:backgroundModeEntitled:pid:context:delegate:delegateQueue:"
+ "initWithClusterPath:"
+ "initWithCommandPath:"
+ "initWithController:entityIdentifier:"
+ "initWithControllerID:nodeID:endpointID:clusterID:attributeID:"
+ "initWithData:"
+ "initWithDate:"
+ "initWithDelegate:delegateQueue:sessionID:"
+ "initWithDictionary:"
+ "initWithError:"
+ "initWithEventPath:"
+ "initWithFirst:second:"
+ "initWithObjectValue:"
+ "initWithObjectValue:forKey:"
+ "initWithPluginClient:"
+ "initWithPluginClient:delegateID:"
+ "initWithProtobufData:responseHandler:"
+ "initWithReadParams:"
+ "initWithSet:"
+ "initWithString:"
+ "initWithTimeInterval:options:"
+ "initWithTimeIntervalSinceReferenceDate:"
+ "initWithTransport:workQueue:sessionID:controllerID:homeID:peerAddress:"
+ "initWithURL:"
+ "initWithUUID:"
+ "initWithUUIDString:"
+ "initWithWatermarkLevel:timedWaitPeriod:"
+ "initWithXPCConnection:"
+ "integerValue"
+ "interfaceWithProtocol:"
+ "interrupted"
+ "invalidate"
+ "invalidated"
+ "invocationWithMethodSignature:"
+ "invokeMessageHandlersForMessage:transport:errorBlock:"
+ "invokeMessageHandlersForReceiver:message:transport:errorBlock:"
+ "invokeWithTarget:"
+ "isInRemoteMode"
+ "isRequest"
+ "isRunning"
+ "isSuspended"
+ "isValid"
+ "kMTRPluginErrorDomain"
+ "key"
+ "localClient"
+ "logState"
+ "longLongValue"
+ "mergeFrom:"
+ "messageData"
+ "messageDirection"
+ "messageDirectionAsString:"
+ "messageDispatcher"
+ "messageHeader"
+ "messageID"
+ "messagePayload"
+ "messageReceivers"
+ "messageSelectors"
+ "messageTransport:handleControllerCheckin:"
+ "messageTransport:handleDeviceAttributeReport:"
+ "messageTransport:handleDeviceBecameActive:"
+ "messageTransport:handleDeviceCachePrimed:"
+ "messageTransport:handleDeviceConfigurationChanged:"
+ "messageTransport:handleDeviceEventReport:"
+ "messageTransport:handleDeviceInternalStateUpdated:"
+ "messageTransport:handleDeviceInvokeCommand:"
+ "messageTransport:handleDeviceReadAttribute:"
+ "messageTransport:handleDeviceReadMultipleAttributes:"
+ "messageTransport:handleDeviceStateChanged:"
+ "messageTransport:handleDeviceWriteAttribute:"
+ "messageTransport:handleGetControllerIsRunning:"
+ "messageTransport:handleGetControllerNodID:"
+ "messageTransport:handleGetControllerUniqueID:"
+ "messageTransport:handleGetDeviceEstimatedStartTime:"
+ "messageTransport:handleGetDeviceEstimatedSubscriptionLatency:"
+ "messageTransport:handleGetDeviceIsCachePrimed:"
+ "messageTransport:handleGetDeviceState:"
+ "messageTransport:handleIncomingMessage:"
+ "messageTransport:handleRegisterNodeID:"
+ "messageTransport:handleShutdownController:"
+ "messageTransport:handleUnregisterNodeID:"
+ "messageTransport:updateTimeOfActivity:"
+ "messageType"
+ "messageTypeAsString:"
+ "messageWithName:destination:payload:"
+ "messageWithProtobufData:"
+ "messageWithProtobufData:responseHandler:"
+ "methodSignatureForSelector:"
+ "minEventNumber"
+ "mutableCopy"
+ "name"
+ "node"
+ "numberWithBool:"
+ "numberWithDouble:"
+ "numberWithLongLong:"
+ "numberWithUnsignedInt:"
+ "numberWithUnsignedLongLong:"
+ "object"
+ "objectAtIndex:"
+ "objectAtIndexedSubscript:"
+ "objectForKey:"
+ "objectsAtIndexes:"
+ "pair"
+ "pairAtIndex:"
+ "pairType"
+ "pairs"
+ "pairsCount"
+ "peerAddress"
+ "pid"
+ "pluginClient"
+ "processIdentifier"
+ "protocol"
+ "protocolAsString:"
+ "q"
+ "q16@0:8"
+ "queryControllerWithID:controllerMessageType:queryRequestValue:errorBlock:replyBlock:"
+ "queryDeviceNodeWithID:controllerID:deviceNodeMessageType:errorBlock:replyBlock:"
+ "queue"
+ "readAttributePaths:"
+ "readFrom:"
+ "readParams"
+ "registerForRequestMessageWithType:requestHandler:forSessionID:"
+ "registeredMTRDevices"
+ "registeredNodeIDs"
+ "remoteClient"
+ "remoteObjectProxy"
+ "removeAllObjects"
+ "removeClientConnection:"
+ "removeClientForXPCConnection:"
+ "removeControllerAssertion"
+ "removeDelegate:"
+ "removeDelegateForDevice:"
+ "removeDeviceControllerDelegate:"
+ "removeDeviceDelegateProxy:"
+ "removeObjectForKey:"
+ "removeObjectsAtIndexes:"
+ "removeObserver:name:object:"
+ "removeResidentClientSession:"
+ "removeRunAssertion"
+ "removeWorkItem:"
+ "repeatStateLoggingInterval"
+ "replaceObjectAtIndex:withObject:"
+ "reportAllAttributesForDevice:"
+ "request"
+ "requestHeaderWithSessionID:controllerID:messageType:"
+ "requestPathWithEndpointID:clusterID:attributeID:"
+ "respondWithError:"
+ "respondWithPayload:"
+ "responseHandler"
+ "responseTimeout"
+ "resume"
+ "run"
+ "running"
+ "schema"
+ "schemaAsString:"
+ "second"
+ "selector"
+ "sendMessage:homeUUID:error:"
+ "sendMessageToControllerWithID:messageType:pbCodable:errorBlock:replyBlock:"
+ "sendMessageToPrimaryHomeHub:"
+ "sendMessageToRemotePeer:peerDestination:"
+ "sessionID"
+ "sessionIdentifier"
+ "sessions"
+ "set"
+ "setArgument:atIndex:"
+ "setArray:"
+ "setArrayValue:"
+ "setAssumeUnknownAttributesReportable:"
+ "setAttributeID:"
+ "setAttributePath:"
+ "setAttributePathValue:"
+ "setAttributePaths:"
+ "setBackgroundModeEntitled:"
+ "setClasses:forSelector:argumentIndex:ofReply:"
+ "setClient:"
+ "setClientProxy:"
+ "setClients:"
+ "setClusterID:"
+ "setClusterPath:"
+ "setClusterPathValue:"
+ "setCode:"
+ "setCommandFields:"
+ "setCommandID:"
+ "setCommandPath:"
+ "setCommandPathValue:"
+ "setConnection:"
+ "setContext:"
+ "setControlChannelReceiver:"
+ "setController:"
+ "setControllerEntities:"
+ "setControllerID:"
+ "setControllerUUIDForAssertion:"
+ "setDataValue:"
+ "setDate:"
+ "setDateValue:"
+ "setDelegate:"
+ "setDelegate:delegateQueue:"
+ "setDelegate:delegateQueue:forSessionID:"
+ "setDelegateID:"
+ "setDelegateProxies:"
+ "setDelegateQueue:"
+ "setDevices:"
+ "setDictionary:"
+ "setDictionaryValue:"
+ "setDispatch:"
+ "setDomain:"
+ "setDoubleValue:"
+ "setEndpointID:"
+ "setEntityIdentifier:"
+ "setError:"
+ "setErrorValue:"
+ "setEventID:"
+ "setEventPath:"
+ "setEventPathValue:"
+ "setExpectedValueInterval:"
+ "setExpectedValues:"
+ "setExportedInterface:"
+ "setExportedObject:"
+ "setFirst:"
+ "setHasAssumeUnknownAttributesReportable:"
+ "setHasAttributeID:"
+ "setHasClusterID:"
+ "setHasCode:"
+ "setHasCommandID:"
+ "setHasDoubleValue:"
+ "setHasEndpointID:"
+ "setHasEventID:"
+ "setHasExpectedValueInterval:"
+ "setHasFilterByFabric:"
+ "setHasIntegerValue:"
+ "setHasMessageDirection:"
+ "setHasMessageType:"
+ "setHasNodeID:"
+ "setHasProtocol:"
+ "setHasSchema:"
+ "setHasServerSideProcessingTimeout:"
+ "setHasTimedInvokeTimeout:"
+ "setHasTimedWriteTimeout:"
+ "setHasUnsignedIntegerValue:"
+ "setHasValue:"
+ "setHasVersion:"
+ "setHeader:"
+ "setHomeID:"
+ "setHomeUUID:"
+ "setIntegerValue:"
+ "setKey:"
+ "setLocalClient:"
+ "setMessageData:"
+ "setMessageDirection:"
+ "setMessageDispatcher:"
+ "setMessageHeader:"
+ "setMessageID:"
+ "setMessageReceivers:"
+ "setMessageSelectors:"
+ "setMessageType:"
+ "setMinEventNumber:"
+ "setNode:"
+ "setNodeID:"
+ "setObject:"
+ "setObject:forKey:"
+ "setPairs:"
+ "setPeerAddress:"
+ "setPid:"
+ "setPluginClient:"
+ "setProtocol:"
+ "setReadParams:"
+ "setRegisteredMTRDevices:"
+ "setRegisteredNodeIDs:"
+ "setRemoteClient:"
+ "setRemoteObjectInterface:"
+ "setRepeatStateLoggingInterval:"
+ "setResponseHandler:"
+ "setResponseTimeout:"
+ "setRunning:"
+ "setSchema:"
+ "setSecond:"
+ "setSelector:"
+ "setServerSideProcessingTimeout:"
+ "setSessionID:"
+ "setSessions:"
+ "setSet:"
+ "setSetValue:"
+ "setSourceAddress:"
+ "setStringValue:"
+ "setTarget:"
+ "setTimeOfLastActivity:"
+ "setTimedInvokeTimeout:"
+ "setTimedWatermarkQueue:"
+ "setTimedWriteTimeout:"
+ "setTransport:"
+ "setUUID:"
+ "setUnsignedIntegerValue:"
+ "setUrl:"
+ "setUrlValue:"
+ "setUuid:"
+ "setUuidValue:"
+ "setValue"
+ "setValue:"
+ "setValues:"
+ "setVersion:"
+ "setWaitPeriod:"
+ "setWaitPeriodTimer:"
+ "setWaitingWorkItems:"
+ "setWatermarkLevel:"
+ "setWithArray:"
+ "setWithSet:"
+ "setWorkQueue:"
+ "setXpcConnection:"
+ "set_clientConnections:"
+ "shortDescription"
+ "shouldAssumeUnknownAttributesReportable"
+ "shouldFilterByFabric"
+ "shutdown"
+ "sortDescriptorWithKey:ascending:"
+ "sortUsingDescriptors:"
+ "sourceAddress"
+ "standardUserDefaults"
+ "startWithDelegate:queue:"
+ "stringValue"
+ "stringWithFormat:"
+ "suspend"
+ "timeIntervalSinceReferenceDate"
+ "timeOfLastActivity"
+ "timeZoneOrTimeChanged:"
+ "timedWatermarkQueue"
+ "timedWatermarkQueue:runPendingWorkItems:"
+ "timerDidFire:"
+ "transport"
+ "type"
+ "unsignedIntValue"
+ "unsignedIntegerValue"
+ "unsignedLongLongValue"
+ "unsignedLongValue"
+ "url"
+ "urlValue"
+ "uuid"
+ "uuidValue"
+ "v16@?0@\"<MTRXPCClientProtocol>\"8"
+ "v16@?0@\"NSArray\"8"
+ "v16@?0@\"NSError\"8"
+ "v16@?0@8"
+ "v20@0:8B16"
+ "v20@0:8I16"
+ "v20@0:8i16"
+ "v24@0:8@\"<MTRPluginProtobufMessageTransportDelegate>\"16"
+ "v24@0:8@\"HMFTimer\"16"
+ "v24@0:8@\"MTRPluginProtobufMessage\"16"
+ "v24@0:8@?16"
+ "v24@0:8Q16"
+ "v24@0:8d16"
+ "v24@0:8q16"
+ "v24@?0@\"NSError\"8@\"NSDictionary\"16"
+ "v24@?0@\"NSError\"8@16"
+ "v28@0:8@\"MTRDeviceController\"16B24"
+ "v28@0:8@16B24"
+ "v32@0:8@\"<MTRPluginProtobufMessageTransport>\"16@\"MTRPluginProtobufMessage\"24"
+ "v32@0:8@\"<MTRPluginProtobufMessageTransport>\"16@\"NSDate\"24"
+ "v32@0:8@\"<MTRPluginProtobufMessageTransportDelegate>\"16@\"NSObject<OS_dispatch_queue>\"24"
+ "v32@0:8@\"MTRDeviceController\"16@\"MTRProductIdentity\"24"
+ "v32@0:8@\"MTRDeviceController\"16@\"NSError\"24"
+ "v32@0:8@\"MTRDeviceController\"16q24"
+ "v32@0:8@\"MTRPluginProtobufMessage\"16@24"
+ "v32@0:8@\"MTRPluginTimedWatermarkQueue\"16@\"NSArray\"24"
+ "v32@0:8@16q24"
+ "v32@?0@\"NSString\"8@16^B24"
+ "v40@0:8@\"<MTRPluginProtobufMessageTransportDelegate>\"16@\"NSObject<OS_dispatch_queue>\"24@\"NSUUID\"32"
+ "v40@0:8@\"MTRDeviceController\"16@\"NSError\"24@\"NSNumber\"32"
+ "v40@0:8@16@24@32"
+ "v40@0:8@16@24@?32"
+ "v48@0:8@\"MTRDeviceController\"16@\"NSError\"24@\"NSNumber\"32@\"MTRMetrics\"40"
+ "v48@0:8@16@24@32@40"
+ "v48@0:8@16@24@32@?40"
+ "v52@0:8@16@24i32@?36@?44"
+ "v52@0:8@16i24@28@?36@?44"
+ "valid"
+ "valueAtIndex:"
+ "valueForEntitlement:"
+ "valueType"
+ "values"
+ "valuesCount"
+ "variableValueFromResponsePayloadData:"
+ "version"
+ "versionAsString:"
+ "waitPeriod"
+ "waitPeriodTimer"
+ "waitingWorkItems"
+ "watermarkLevel"
+ "workQueue"
+ "writeTo:"
+ "xpcConnection"
+ "{?=\"assumeUnknownAttributesReportable\"b1\"filterByFabric\"b1}"
+ "{?=\"attributeID\"b1}"
+ "{?=\"clusterID\"b1\"endpointID\"b1}"
+ "{?=\"code\"b1}"
+ "{?=\"commandID\"b1}"
+ "{?=\"doubleValue\"b1\"integerValue\"b1\"unsignedIntegerValue\"b1}"
+ "{?=\"eventID\"b1}"
+ "{?=\"expectedValueInterval\"b1\"serverSideProcessingTimeout\"b1\"timedInvokeTimeout\"b1}"
+ "{?=\"expectedValueInterval\"b1\"timedWriteTimeout\"b1}"
+ "{?=\"messageDirection\"b1\"messageType\"b1\"protocol\"b1\"schema\"b1\"version\"b1}"
+ "{?=\"nodeID\"b1}"
+ "{?=\"value\"b1}"
- "\x06"
- "-[MTRDevicePluginServer handleDeviceControllerInitWithParameters_xpcConnection:requestMessage:responseMessage:completionBlock:controllerIdentifierString:responseIdentifierString:]"
- "-[MTRDevicePluginServer handleDeviceEstimatedStartTime_xpcConnection:requestMessage:responseMessage:completionBlock:controllerIdentifierString:responseIdentifierString:nodeID:]"
- "-[MTRDevicePluginServer handleDeviceInvokeCommand_xpcConnection:requestMessage:responseMessage:completionBlock:controllerIdentifierString:responseIdentifierString:nodeID:endpointID:clusterID:commandID:commandFields:expectedValues:expectedValueInterval:timedInvokeTimeout:serverSideProcessingTimeout:]"
- "-[MTRDevicePluginServer handleDeviceReadAttribute_xpcConnection:requestMessage:responseMessage:completionBlock:controllerIdentifierString:responseIdentifierString:nodeID:endpointID:clusterID:attributeID:filterByFabric:]"
- "-[MTRDevicePluginServer handleDeviceRegisterDelegate_xpcConnection:requestMessage:responseMessage:completionBlock:controllerIdentifierString:nodeID:]"
- "-[MTRDevicePluginServer handleDeviceUnregisterDelegate_xpcConnection:requestMessage:responseMessage:completionBlock:controllerIdentifierString:nodeID:]"
- "-[MTRDevicePluginServer handleDeviceWriteAttribute_xpcConnection:requestMessage:responseMessage:completionBlock:controllerIdentifierString:nodeID:endpointID:clusterID:attributeID:value:expectedValueInterval:timedWriteTimeout:]"
- "@\"<MTRDevicePluginServerDelegate>\""
- "@\"<MTRDevicePluginSyncManagerDelegate>\""
- "@\"NSObject<OS_xpc_object>\""
- "@48@0:8r*16@24@32@40"
- "Adding device controller, but ignoring since it's already added: %!p(MISSING)"
- "Adding device controller: %!p(MISSING)"
- "JEFFTEST S: %!s(MISSING)"
- "JEFFTEST S: %!s(MISSING) nodeID: %!@(MISSING)"
- "JEFFTEST S: %!s(MISSING) xpc_connection %!@(MISSING)"
- "JEFFTEST S: MTRDevicePluginServer event handler"
- "JEFFTEST S: MTRDevicePluginServer invalidation handler"
- "JEFFTEST S: MTRDevicePluginServer terminate handler"
- "JEFFTEST S: controller %!@(MISSING)"
- "JEFFTEST S: controller add %!@(MISSING)"
- "JEFFTEST S: controller lookup %!@(MISSING)"
- "JEFFTEST S: controller lookup %!@(MISSING) =? %!@(MISSING) %!@(MISSING)"
- "JEFFTEST S: controller remove %!@(MISSING)"
- "JEFFTEST S: device %!@(MISSING) deviceBecameActive"
- "JEFFTEST S: device %!@(MISSING) receivedAttributeReport: %!l(MISSING)u"
- "JEFFTEST S: device %!@(MISSING) receivedEventReport: %!l(MISSING)u"
- "JEFFTEST S: device %!@(MISSING) stateChanged: %!l(MISSING)u"
- "JEFFTEST S: read result uuid %!@(MISSING) device %!@(MISSING) dataValueDict %!@(MISSING)"
- "JEFFTEST S: should not get duplicate controllers - replacing %!@(MISSING) with %!@(MISSING)"
- "MTRDevicePluginServer"
- "MTRDevicePluginServer: initialized with %!l(MISSING)u controllers"
- "MTRDevicePluginSyncManager"
- "MTRDevicePluginSyncManager init"
- "MTRDevicePluginSyncManager receiveMessage"
- "Removing device controller: %!p(MISSING)"
- "Setting up MTRDeviceControllerRegistry shared instance: %!p(MISSING)"
- "Setting up MTRPlugin shared instance: %!p(MISSING)"
- "Stopping MTRPlugin: %!p(MISSING)"
- "T@\"NSMutableArray\",C,V_controllers"
- "Tried to remove device controller, but wasn't present: %!p(MISSING)"
- "XPC"
- "__XPC_MTRRemoteDeviceController_initWithParameters_response"
- "__XPC_MTRRemoteDevice_delegate_deviceBecameActive"
- "__XPC_MTRRemoteDevice_delegate_receivedAttributeReport"
- "__XPC_MTRRemoteDevice_delegate_receivedEventReport"
- "__XPC_MTRRemoteDevice_delegate_stateChanged"
- "__XPC_MTRRemoteDevice_estimatedStartTime_response"
- "__XPC_MTRRemoteDevice_invokeCommand_response"
- "__XPC_MTRRemoteDevice_readAttribute_response"
- "__xpc__event_code__"
- "__xpc_wants_reply__"
- "_deviceControllerConnectionMap"
- "_deviceControllerMap"
- "addController:"
- "addControllers:"
- "attributeReport"
- "controllerConnectionForDevice:deviceControllerUniqueIdentifierString:"
- "controllerForUniqueIdentifierString:"
- "controllerIdentifierString"
- "dataValueDictionary"
- "eventReport"
- "getAllCurrentAttributes"
- "handleDeviceControllerInitWithParameters_xpcConnection:requestMessage:responseMessage:completionBlock:controllerIdentifierString:responseIdentifierString:"
- "handleDeviceEstimatedStartTime_xpcConnection:requestMessage:responseMessage:completionBlock:controllerIdentifierString:responseIdentifierString:nodeID:"
- "handleDeviceInvokeCommand_xpcConnection:requestMessage:responseMessage:completionBlock:controllerIdentifierString:responseIdentifierString:nodeID:endpointID:clusterID:commandID:commandFields:expectedValues:expectedValueInterval:timedInvokeTimeout:serverSideProcessingTimeout:"
- "handleDeviceReadAttribute_xpcConnection:requestMessage:responseMessage:completionBlock:controllerIdentifierString:responseIdentifierString:nodeID:endpointID:clusterID:attributeID:filterByFabric:"
- "handleDeviceRegisterDelegate_xpcConnection:requestMessage:responseMessage:completionBlock:controllerIdentifierString:nodeID:"
- "handleDeviceUnregisterDelegate_xpcConnection:requestMessage:responseMessage:completionBlock:controllerIdentifierString:nodeID:"
- "handleDeviceWriteAttribute_xpcConnection:requestMessage:responseMessage:completionBlock:controllerIdentifierString:nodeID:endpointID:clusterID:attributeID:value:expectedValueInterval:timedWriteTimeout:"
- "handleXPCConnection:messageEvent:"
- "initWithEndpoint:delegate:queue:"
- "initWithName:delegate:queue:knownControllers:"
- "invokeResponse"
- "mtrdeviceplugin.workqueue"
- "peer(%!d(MISSING)) received XPC_ERROR_CONNECTION_INTERRUPTED"
- "peer(%!d(MISSING)) received XPC_ERROR_CONNECTION_INVALID"
- "peer(%!d(MISSING)) received XPC_ERROR_TERMINATION_IMMINENT"
- "processReceivedMessage:"
- "processReceivedMessage: not yet implemented"
- "receiveMessage:"
- "received message from peer(%!d(MISSING)): %!s(MISSING)"
- "removeController:"
- "responseIdentifierString"
- "setControllers:"
- "setDelegate:queue:"
- "setDelegate:queue:setUpSubscription:"
- "v100@0:8@16@24@32@?40@48@56@64@72@80@88B96"
- "v112@0:8@16@24@32@?40@48@56@64@72@80@88@96@104"
- "v136@0:8@16@24@32@?40@48@56@64@72@80@88@96@104@112@120@128"
- "v24@?0@\"NSObject<OS_xpc_object>\"8@\"NSObject<OS_xpc_object>\"16"
- "v64@0:8@16@24@32@?40@48@56"
- "v72@0:8@16@24@32@?40@48@56@64"

```
