## RemoteHID

> `/System/Library/PrivateFrameworks/RemoteHID.framework/RemoteHID`

```diff

-210.100.2.0.0
-  __TEXT.__text: 0xb5e8
-  __TEXT.__auth_stubs: 0x600
+223.0.0.0.0
+  __TEXT.__text: 0xae0c
   __TEXT.__objc_methlist: 0x550
   __TEXT.__const: 0x260
-  __TEXT.__gcc_except_tab: 0x6cc
-  __TEXT.__cstring: 0x602
+  __TEXT.__gcc_except_tab: 0x5f4
+  __TEXT.__cstring: 0x60e
   __TEXT.__oslogstring: 0xa54
-  __TEXT.__unwind_info: 0x398
-  __TEXT.__objc_classname: 0x74
-  __TEXT.__objc_methname: 0xe67
-  __TEXT.__objc_methtype: 0x50a
-  __TEXT.__objc_stubs: 0xfc0
-  __DATA_CONST.__got: 0x80
+  __TEXT.__unwind_info: 0x4a8
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x3a8
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x430
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x318
+  __DATA_CONST.__got: 0x80
   __AUTH_CONST.__const: 0x228
   __AUTH_CONST.__cfstring: 0x2e0
   __AUTH_CONST.__objc_const: 0x8a0
+  __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH_CONST.__auth_got: 0x320
   __AUTH.__objc_data: 0xf0
   __AUTH.__data: 0x10
   __DATA.__objc_ivar: 0x88

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 6E138725-89EB-32C5-ABF4-3205598BC1F9
-  Functions: 344
-  Symbols:   1098
-  CStrings:  414
+  UUID: 287602F3-A9E7-3952-910D-88D3D57FCF64
+  Functions: 340
+  Symbols:   1085
+  CStrings:  167
 
Symbols:
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.172
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.172.cold.1
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.172.cold.2
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.178
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.178.cold.1
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.178.cold.2
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.178.cold.3
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.180
+ ___block_literal_global.158
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x4
+ _objc_retain_x5
+ _objc_retain_x8
- GCC_except_table59
- GCC_except_table65
- GCC_except_table71
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.173.cold.1
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.173.cold.2
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.174
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.179
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.179.cold.1
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.179.cold.2
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.179.cold.3
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.181
- ___block_literal_global.159
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x25
- _objc_retain_x27
CStrings:
- ".cxx_destruct"
- "@\"HIDRemoteDeviceAACPServer\""
- "@\"HIDRemoteEndpoint\""
- "@\"NSData\""
- "@\"NSMutableArray\""
- "@\"NSMutableData\""
- "@\"NSMutableDictionary\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSObject<OS_dispatch_semaphore>\""
- "@16@0:8"
- "@24@0:8@16"
- "@24@0:8Q16"
- "B"
- "B16@0:8"
- "B32@0:8@16^{?=b7b10b3b1b1b1b9}24"
- "B32@0:8@16^{?={?=b7b10b3b1b1b1b9}C[0C]}24"
- "B40@0:8@16Q24@32"
- "C"
- "C16@0:8"
- "HIDAACPRemoteEndpoint"
- "HIDRemoteDevice"
- "HIDRemoteDeviceAACPServer"
- "HIDRemoteDeviceServer"
- "HIDRemoteEndpoint"
- "I"
- "I16@0:8"
- "Q16@0:8"
- "Q32@0:8@16Q24"
- "T@\"HIDRemoteDeviceAACPServer\",&,V_server"
- "T@\"HIDRemoteEndpoint\",&,V_endpoint"
- "T@\"NSData\",&,V_lastGetReport"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_btQueue"
- "T@\"NSObject<OS_dispatch_queue>\",R,V_queue"
- "T@\"NSObject<OS_dispatch_semaphore>\",&,V_semaphore"
- "TB,V_cancelled"
- "TB,V_enableTS"
- "TB,V_waitForReport"
- "TC,V_primarySide"
- "TC,V_side"
- "TC,V_transportVersion"
- "TI,V_handleReportCount"
- "TI,V_handleReportError"
- "TI,V_propertyNotify"
- "TQ,V_deviceID"
- "TQ,V_endpointID"
- "T^{IONotificationPort=},V_propertyPort"
- "Ti,V_lastSetReportStatus"
- "^{BTAccessoryManagerImpl=}"
- "^{BTSessionImpl=}"
- "^{IONotificationPort=}"
- "^{IONotificationPort=}16@0:8"
- "^{MobileBluetoothInterface=^^?}"
- "^{os_state_data_s=I(?=b32I){os_state_data_decoder_s=[64c][64c]}[64c][0C]}24@0:8^{os_state_hints_s=I*II}16"
- "_asyncQueue"
- "_btQueue"
- "_cancelled"
- "_decodeBuff"
- "_deviceID"
- "_devices"
- "_disconnectEndpointID:"
- "_enableTS"
- "_endpoint"
- "_endpointID"
- "_endpoints"
- "_handleReportCount"
- "_handleReportError"
- "_lastGetReport"
- "_lastSetReportStatus"
- "_lock"
- "_manager"
- "_mb"
- "_me"
- "_prevDeviceLog"
- "_primarySide"
- "_propertyNotify"
- "_propertyPort"
- "_queue"
- "_refreshCounts"
- "_removeDeviceID:"
- "_semaphore"
- "_server"
- "_session"
- "_side"
- "_stateHandler"
- "_transportVersion"
- "_tsID"
- "_waitForReport"
- "activate"
- "addBTDevice:"
- "addDevice:"
- "addObject:"
- "allValues"
- "btAccessoryEventHandler:event:state:"
- "btDeviceMessageHandler:type:data:size:"
- "btQueue"
- "btServiceEventHandler:services:eventType:event:result:"
- "btSessionCreate"
- "btSessionEventHandler:event:result:"
- "btSessionInit:"
- "bytes"
- "cancel"
- "cancelled"
- "connectEndpoint:"
- "copy"
- "copyState"
- "count"
- "createRemoteDevice:deviceID:property:"
- "dataWithBytes:length:"
- "dataWithBytesNoCopy:length:freeWhenDone:"
- "dataWithLength:"
- "dataWithPropertyList:format:options:error:"
- "dealloc"
- "description"
- "deviceID"
- "devices"
- "dictionaryWithObjects:forKeys:count:"
- "disconnectAll"
- "disconnectEndpointID:"
- "enableTS"
- "endpoint"
- "endpointID"
- "endpointMessageHandler:data:size:"
- "endpointPacketHandler:packet:transportVersion:side:"
- "endpoints"
- "enumerateKeysAndObjectsUsingBlock:"
- "enumerateObjectsUsingBlock:"
- "getDevice:"
- "getEndpoint:"
- "getLastGetReport"
- "getLastSetReportStatus"
- "getRefreshCountForEndpoint:deviceID:"
- "getReportHandler:reportID:report:reportLength:"
- "handlePropertyChange:"
- "handleReport:error:"
- "handleReportCount"
- "handleReportError"
- "i16@0:8"
- "i28@0:8i16C20i24"
- "i40@0:8i16C20*24Q32"
- "i44@0:8@16q24C32@36"
- "i48@0:8^{BTDeviceImpl=}16*24Q32C40C44"
- "init"
- "initWithBytes:length:encoding:"
- "initWithData:encoding:"
- "initWithID:"
- "initWithLength:"
- "initWithProperties:"
- "initWithQueue:"
- "isEqual:"
- "lastGetReport"
- "lastSetReportStatus"
- "length"
- "logRemovedDevice:"
- "mutableBytes"
- "mutableCopy"
- "numberWithBool:"
- "numberWithUnsignedChar:"
- "numberWithUnsignedInt:"
- "numberWithUnsignedInteger:"
- "numberWithUnsignedLongLong:"
- "objectForKeyedSubscript:"
- "primarySide"
- "propertyForKey:"
- "propertyListWithData:options:format:error:"
- "propertyNotify"
- "propertyPort"
- "queue"
- "registerPropertyNotification:"
- "remoteDeviceConfirmConnectHandler:packet:transportVersion:side:"
- "remoteDeviceConnectHandler:packet:transportVersion:side:"
- "remoteDeviceGetReport:type:reportID:report:"
- "remoteDeviceGetReportHandler:packet:"
- "remoteDeviceRefresh:deviceID:transportVersion:side:"
- "remoteDeviceReportHandler:header:"
- "remoteDeviceReportHandler:packet:"
- "remoteDeviceSetReport:type:reportID:report:"
- "remoteDeviceSetReportHandler:packet:"
- "removeAllBTDevices"
- "removeAllDevices"
- "removeAllObjects"
- "removeBTDevice:"
- "removeDeviceID:"
- "removeObjectAtIndex:"
- "removeObjectForKey:"
- "semaphore"
- "sendMessageBTDevice:data:size:transportVersion:side:"
- "server"
- "service"
- "setBtQueue:"
- "setCancelHandler:"
- "setCancelled:"
- "setDeviceID:"
- "setDispatchQueue:"
- "setEnableTS:"
- "setEndpoint:"
- "setEndpointID:"
- "setGetReportHandler:"
- "setHandleReportCount:"
- "setHandleReportError:"
- "setLastGetReport:"
- "setLastSetReportStatus:"
- "setMobileBluetoothInterface:"
- "setObject:forKeyedSubscript:"
- "setPrimarySide:"
- "setProperty:forKey:"
- "setPropertyNotify:"
- "setPropertyPort:"
- "setRefreshCountForEndpoint:deviceID:count:"
- "setReportHandler:reportID:status:"
- "setSemaphore:"
- "setServer:"
- "setSetReportHandler:"
- "setSide:"
- "setTransportVersion:"
- "setWaitForReport:"
- "side"
- "stateHandler:"
- "stringWithFormat:"
- "timeSyncEnable:forEndpointID:"
- "transportVersion"
- "unsignedIntValue"
- "unsignedIntegerValue"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8C16"
- "v20@0:8I16"
- "v20@0:8i16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8^{BTDeviceImpl=}16"
- "v24@0:8^{BTSessionImpl=}16"
- "v24@0:8^{IONotificationPort=}16"
- "v24@0:8^{MobileBluetoothInterface=^^?}16"
- "v28@0:8B16Q20"
- "v32@0:8^{BTDeviceImpl=}16i24i28"
- "v32@0:8^{BTSessionImpl=}16i24i28"
- "v40@0:8@16*24Q32"
- "v40@0:8@16Q24C32C36"
- "v40@0:8@16Q24Q32"
- "v40@0:8@16^{?=b7b10b3b1b1b1b9}24C32C36"
- "v40@0:8@16^{?={?=b7b10b3b1b1b1b9}[0C]}24C32C36"
- "v40@0:8^{BTDeviceImpl=}16I24i28I32i36"
- "v44@0:8^{BTDeviceImpl=}16i24*28Q36"
- "waitForReport"
- "{os_unfair_recursive_lock_s=\"ourl_lock\"{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}\"ourl_count\"I}"

```
