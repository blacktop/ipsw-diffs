## RemoteHID

> `/System/Library/PrivateFrameworks/RemoteHID.framework/RemoteHID`

```diff

-192.100.4.0.0
-  __TEXT.__text: 0xa260
-  __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_methlist: 0x408
-  __TEXT.__const: 0x244
-  __TEXT.__gcc_except_tab: 0x18c
-  __TEXT.__cstring: 0x48b
-  __TEXT.__oslogstring: 0xabb
-  __TEXT.__unwind_info: 0x200
-  __TEXT.__objc_classname: 0x5a
-  __TEXT.__objc_methname: 0xbd9
-  __TEXT.__objc_methtype: 0x425
-  __TEXT.__objc_stubs: 0xce0
-  __DATA_CONST.__got: 0x88
-  __DATA_CONST.__const: 0x248
-  __DATA_CONST.__objc_classlist: 0x20
+206.0.0.0.0
+  __TEXT.__text: 0xada4
+  __TEXT.__auth_stubs: 0x5e0
+  __TEXT.__objc_methlist: 0x4f4
+  __TEXT.__const: 0x260
+  __TEXT.__gcc_except_tab: 0x6a4
+  __TEXT.__cstring: 0x552
+  __TEXT.__oslogstring: 0x98a
+  __TEXT.__unwind_info: 0x350
+  __TEXT.__objc_classname: 0x73
+  __TEXT.__objc_methname: 0xd1b
+  __TEXT.__objc_methtype: 0x480
+  __TEXT.__objc_stubs: 0xe20
+  __DATA_CONST.__got: 0x80
+  __DATA_CONST.__const: 0x2e8
+  __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x360
-  __DATA_CONST.__objc_superrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x2b8
-  __AUTH_CONST.__const: 0x148
-  __AUTH_CONST.__cfstring: 0x240
-  __AUTH_CONST.__objc_const: 0x6c0
-  __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH.__objc_data: 0xa0
+  __DATA_CONST.__objc_selrefs: 0x3d0
+  __DATA_CONST.__objc_superrefs: 0x28
+  __AUTH_CONST.__auth_got: 0x308
+  __AUTH_CONST.__const: 0x1e0
+  __AUTH_CONST.__cfstring: 0x2c0
+  __AUTH_CONST.__objc_const: 0x830
+  __AUTH_CONST.__objc_intobj: 0x78
+  __AUTH.__objc_data: 0xf0
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x68
+  __DATA.__objc_ivar: 0x78
   __DATA.__bss: 0x18
   __DATA_DIRTY.__objc_data: 0xa0
   __DATA_DIRTY.__bss: 0x10

   - /System/Library/PrivateFrameworks/MobileBluetooth.framework/MobileBluetooth
   - /System/Library/PrivateFrameworks/TimeSync.framework/TimeSync
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3746CF5C-0FE4-3658-9CB8-BEEE84BC2C71
-  Functions: 285
-  Symbols:   882
-  CStrings:  360
+  UUID: 27D535DC-D20A-356A-9169-8DABA6B59FAA
+  Functions: 326
+  Symbols:   1022
+  CStrings:  389
 
Symbols:
+ -[HIDAACPRemoteEndpoint .cxx_destruct]
+ -[HIDAACPRemoteEndpoint addDevice:]
+ -[HIDAACPRemoteEndpoint handlePropertyChange:]
+ -[HIDAACPRemoteEndpoint registerPropertyNotification:]
+ -[HIDAACPRemoteEndpoint removeAllDevices]
+ -[HIDAACPRemoteEndpoint removeDevice:]
+ -[HIDAACPRemoteEndpoint server]
+ -[HIDAACPRemoteEndpoint setServer:]
+ -[HIDRemoteDevice enableTS]
+ -[HIDRemoteDevice endpoint]
+ -[HIDRemoteDevice getLastGetReport]
+ -[HIDRemoteDevice getLastSetReportStatus]
+ -[HIDRemoteDevice propertyNotify]
+ -[HIDRemoteDevice propertyPort]
+ -[HIDRemoteDevice setEnableTS:]
+ -[HIDRemoteDevice setEndpoint:]
+ -[HIDRemoteDevice setPropertyNotify:]
+ -[HIDRemoteDevice setPropertyPort:]
+ -[HIDRemoteDeviceAACPServer dealloc]
+ -[HIDRemoteDeviceAACPServer setMobileBluetoothInterface:]
+ -[HIDRemoteDeviceAACPServer timeSyncEnable:forEndpointID:]
+ -[HIDRemoteEndpoint devices]
+ GCC_except_table0
+ GCC_except_table11
+ GCC_except_table14
+ GCC_except_table17
+ GCC_except_table2
+ GCC_except_table20
+ GCC_except_table21
+ GCC_except_table27
+ GCC_except_table28
+ GCC_except_table29
+ GCC_except_table30
+ GCC_except_table31
+ GCC_except_table32
+ GCC_except_table34
+ GCC_except_table35
+ GCC_except_table37
+ GCC_except_table38
+ GCC_except_table39
+ GCC_except_table4
+ GCC_except_table41
+ GCC_except_table44
+ GCC_except_table5
+ GCC_except_table58
+ GCC_except_table59
+ GCC_except_table6
+ GCC_except_table62
+ GCC_except_table64
+ GCC_except_table69
+ GCC_except_table7
+ GCC_except_table70
+ _BTAccessoryManagerSensorStreamTimeSyncEnable
+ _IONotificationPortCreate
+ _IONotificationPortDestroy
+ _IONotificationPortSetDispatchQueue
+ _IOObjectRelease
+ _IOServiceAddInterestNotification
+ _OBJC_CLASS_$_HIDAACPRemoteEndpoint
+ _OBJC_IVAR_$_HIDAACPRemoteEndpoint._server
+ _OBJC_IVAR_$_HIDRemoteDevice._enableTS
+ _OBJC_IVAR_$_HIDRemoteDevice._endpoint
+ _OBJC_IVAR_$_HIDRemoteDevice._propertyNotify
+ _OBJC_IVAR_$_HIDRemoteDevice._propertyPort
+ _OBJC_IVAR_$_HIDRemoteDeviceAACPServer._mb
+ _OBJC_IVAR_$_HIDRemoteDeviceAACPServer._tsID
+ _OBJC_METACLASS_$_HIDAACPRemoteEndpoint
+ __OBJC_$_INSTANCE_METHODS_HIDAACPRemoteEndpoint
+ __OBJC_$_INSTANCE_VARIABLES_HIDAACPRemoteEndpoint
+ __OBJC_$_PROP_LIST_HIDAACPRemoteEndpoint
+ __OBJC_CLASS_RO_$_HIDAACPRemoteEndpoint
+ __OBJC_METACLASS_RO_$_HIDAACPRemoteEndpoint
+ __ZL10generation
+ __ZL25HIDAccessoryEventCallbackP22BTAccessoryManagerImpl16BTAccessoryEventP12BTDeviceImpl16BTAccessoryStatePv
+ __ZL26HIDTimeSyncPropertyHandlerPvjjS_
+ __ZL31HIDAccesoryServiceEventCallbackP12BTDeviceImplj18BTServiceEventTypejiPv
+ __ZL31HIDAccesorySessionEventCallbackP13BTSessionImpl14BTSessionEventiPv
+ __ZL31HIDAccesorySessionEventCallbackP13BTSessionImpl14BTSessionEventiPv.cold.1
+ __ZL32HIDAccesoryCustomMessageCallbackP22BTAccessoryManagerImplP12BTDeviceImpl28BTAccessoryCustomMessageTypePhmPv
+ __ZN24MobileBluetoothInterface21BTServiceAddCallbacksEP13BTSessionImplPFvP12BTDeviceImplj18BTServiceEventTypejiPvES5_
+ __ZN24MobileBluetoothInterface23BTLocalDeviceGetDefaultEP13BTSessionImplPP17BTLocalDeviceImpl
+ __ZN24MobileBluetoothInterface24BTDeviceGetAddressStringEP12BTDeviceImplPcm
+ __ZN24MobileBluetoothInterface24BTSessionAttachWithQueueEPKcPK18BTSessionCallbacksPvPU28objcproto17OS_dispatch_queue8NSObject
+ __ZN24MobileBluetoothInterface24BTSessionDetachWithQueueEPP13BTSessionImpl
+ __ZN24MobileBluetoothInterface25BTDeviceAddressFromStringEPKcP15BTDeviceAddress
+ __ZN24MobileBluetoothInterface28BTAccessoryManagerGetDefaultEP13BTSessionImplPP22BTAccessoryManagerImpl
+ __ZN24MobileBluetoothInterface28BTDeviceGetConnectedServicesEP12BTDeviceImplPj
+ __ZN24MobileBluetoothInterface30BTAccessoryManagerAddCallbacksEP22BTAccessoryManagerImplPK20BTAccessoryCallbacksPv
+ __ZN24MobileBluetoothInterface31BTAccessoryManagerGetTimeSyncIdEP22BTAccessoryManagerImplP12BTDeviceImplPy
+ __ZN24MobileBluetoothInterface32BTLocalDeviceGetConnectedDevicesEP17BTLocalDeviceImplPP12BTDeviceImplPmm
+ __ZN24MobileBluetoothInterface35BTAccessoryManagerSendCustomMessageEP22BTAccessoryManagerImpl28BTAccessoryCustomMessageTypeP12BTDeviceImplPhm
+ __ZN24MobileBluetoothInterface38BTAccessoryManagerGetFeatureCapabilityEP22BTAccessoryManagerImplP12BTDeviceImpl16FeatureDBEntry_tPj
+ __ZN24MobileBluetoothInterface38BTAccessoryManagerRemoteTimeSyncEnableEP22BTAccessoryManagerImplP12BTDeviceImplj
+ __ZN24MobileBluetoothInterface45BTAccessoryManagerRegisterCustomMessageClientEP22BTAccessoryManagerImplPK33BTAccessoryCustomMessageCallbacks28BTAccessoryCustomMessageTypePv
+ __ZN24MobileBluetoothInterface6createEv
+ __ZTI24MobileBluetoothInterface
+ __ZTS24MobileBluetoothInterface
+ __ZTV24MobileBluetoothInterface
+ __ZTVN10__cxxabiv117__class_type_infoE
+ __ZZ41-[HIDRemoteDeviceAACPServer addBTDevice:]E15messageCallback
+ __ZZ43-[HIDRemoteDeviceAACPServer btSessionInit:]E18accessoryCallbacks
+ __ZZ44-[HIDRemoteDeviceAACPServer btSessionCreate]E16sessionCallbacks
+ __ZdlPvSt19__type_descriptor_t
+ __ZnwmSt19__type_descriptor_t
+ ___28-[HIDRemoteEndpoint devices]_block_invoke
+ ___41-[HIDAACPRemoteEndpoint removeAllDevices]_block_invoke
+ ___46-[HIDAACPRemoteEndpoint handlePropertyChange:]_block_invoke
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.166
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.166.cold.1
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.166.cold.2
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.167
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.172
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.172.cold.1
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.172.cold.2
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.172.cold.3
+ ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.174
+ ___65-[HIDRemoteDeviceAACPServer btAccessoryEventHandler:event:state:]_block_invoke
+ ___65-[HIDRemoteDeviceAACPServer btAccessoryEventHandler:event:state:]_block_invoke_2
+ ___assert_rtn
+ ___block_descriptor_40_ea8_32r_e32_v32?0"HIDRemoteDevice"8Q16^B24lr32l8
+ ___block_descriptor_40_ea8_32s_e15_v32?0816^B24ls32l8
+ ___block_descriptor_40_ea8_32s_e32_v32?0"HIDRemoteDevice"8Q16^B24ls32l8
+ ___block_descriptor_40_ea8_32s_e5_v8?0ls32l8
+ ___block_descriptor_48_ea8_32r40r_e15_v32?0816^B24lr32l8r40l8
+ ___block_descriptor_48_ea8_32s40r_e32_v32?0"HIDRemoteDevice"8Q16^B24ls32l8r40l8
+ ___gxx_personality_v0
+ _kIOMainPortDefault
+ _objc_msgSend$devices
+ _objc_msgSend$dictionaryWithObjects:forKeys:count:
+ _objc_msgSend$enableTS
+ _objc_msgSend$endpoint
+ _objc_msgSend$enumerateObjectsUsingBlock:
+ _objc_msgSend$handlePropertyChange:
+ _objc_msgSend$numberWithBool:
+ _objc_msgSend$propertyForKey:
+ _objc_msgSend$propertyNotify
+ _objc_msgSend$propertyPort
+ _objc_msgSend$registerPropertyNotification:
+ _objc_msgSend$server
+ _objc_msgSend$setEnableTS:
+ _objc_msgSend$setEndpoint:
+ _objc_msgSend$setProperty:forKey:
+ _objc_msgSend$setPropertyNotify:
+ _objc_msgSend$setPropertyPort:
+ _objc_msgSend$setServer:
+ _objc_msgSend$timeSyncEnable:forEndpointID:
+ _objc_retain_x1
+ _strlcpy
- -[HIDRemoteDeviceAACPServer btAccessoryEventHandler:event:state:].cold.2
- -[HIDRemoteDeviceAACPServer btAccessoryEventHandler:event:state:].cold.3
- -[HIDRemoteDeviceAACPServer syncRemoteTimestamp:forEndpoint:]
- -[HIDRemoteDeviceAACPServer syncRemoteTimestamp:forEndpoint:].cold.1
- -[HIDRemoteDeviceServer remoteDeviceTimestampedReportHandler:device:packet:]
- -[HIDRemoteDeviceServer remoteDeviceTimestampedReportHandler:device:packet:].cold.1
- -[HIDRemoteDeviceServer remoteDeviceTimestampedReportHandler:device:packet:].cold.2
- -[HIDRemoteDeviceServer syncRemoteTimestamp:forEndpoint:]
- GCC_except_table46
- GCC_except_table47
- GCC_except_table50
- _HIDAccesoryCustomMessageCallback
- _HIDAccesoryServiceEventCallback
- _HIDAccesorySessionEventCallback
- _HIDAccesorySessionEventCallback.cold.1
- _HIDAccessoryEventCallback
- _OBJC_CLASS_$_TSClockManager
- _OBJC_IVAR_$_HIDRemoteDeviceAACPServer._coreTimeSyncManager
- _OBJC_IVAR_$_HIDRemoteDeviceAACPServer._endpointTimeSyncEnabled
- _OBJC_IVAR_$_HIDRemoteDeviceAACPServer._timeSyncClock
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.134
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.134.cold.1
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.134.cold.2
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.135
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.140
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.140.cold.1
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.140.cold.2
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.140.cold.3
- ___62-[HIDRemoteDeviceServer createRemoteDevice:deviceID:property:]_block_invoke.142
- ___block_descriptor_40_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_48_e8_32r40r_e15_v32?0816^B24lr32l8r40l8
- ___kCFBooleanFalse
- ___strlcpy_chk
- _addBTDevice:.messageCallback
- _btSessionCreate.sessionCallbacks
- _btSessionInit:.accessoryCallbacks
- _generation
- _mach_timebase_info
- _objc_msgSend$clockIdentifier
- _objc_msgSend$clockWithClockIdentifier:
- _objc_msgSend$convertFromDomainToMachAbsoluteTime:
- _objc_msgSend$handleReport:withTimestamp:error:
- _objc_msgSend$lockState
- _objc_msgSend$remoteDeviceTimestampedReportHandler:device:packet:
- _objc_msgSend$sharedClockManager
- _objc_msgSend$syncRemoteTimestamp:forEndpoint:
- _objc_msgSend$unsignedIntValue
CStrings:
+ "-[HIDAACPRemoteEndpoint registerPropertyNotification:]"
+ "0 == status"
+ "<HIDRemoteDeviceAACPServer timeSyncID:%llu %@>"
+ "@\"HIDRemoteEndpoint\""
+ "Active"
+ "Couldn't set %u timesync for device:%p status:%d"
+ "HIDAACPRemoteEndpoint"
+ "HIDRemoteDeviceAACPServer.mm"
+ "HIDTimeSyncProperties"
+ "HIDTimeSyncProtocol"
+ "IOGeneralInterest"
+ "Set %u timesync for device:%p"
+ "T@\"HIDRemoteDeviceAACPServer\",&,V_server"
+ "T@\"HIDRemoteEndpoint\",&,V_endpoint"
+ "TB,V_enableTS"
+ "TI,V_propertyNotify"
+ "TSClockID"
+ "T^{IONotificationPort=},V_propertyPort"
+ "^{IONotificationPort=}"
+ "^{IONotificationPort=}16@0:8"
+ "^{MobileBluetoothInterface=^^?}"
+ "_enableTS"
+ "_endpoint"
+ "_mb"
+ "_propertyNotify"
+ "_propertyPort"
+ "_server"
+ "_tsID"
+ "c"
+ "dealloc"
+ "devices"
+ "dictionaryWithObjects:forKeys:count:"
+ "enableTS"
+ "endpoint"
+ "enumerateObjectsUsingBlock:"
+ "getLastGetReport"
+ "getLastSetReportStatus"
+ "handlePropertyChange:"
+ "numberWithBool:"
+ "propertyForKey:"
+ "propertyNotify"
+ "propertyPort"
+ "registerPropertyNotification:"
+ "server"
+ "setEnableTS:"
+ "setEndpoint:"
+ "setMobileBluetoothInterface:"
+ "setProperty:forKey:"
+ "setPropertyNotify:"
+ "setPropertyPort:"
+ "setServer:"
+ "timeSyncEnable:forEndpointID:"
+ "v24@0:8^{IONotificationPort=}16"
+ "v24@0:8^{MobileBluetoothInterface=^^?}16"
+ "v28@0:8B16Q20"
+ "v32@?0@\"HIDRemoteDevice\"8Q16^B24"
- "&"
- "+"
- "-"
- "<HIDRemoteDeviceAACPServer timeSync:%s %@>"
- "@\"TSClockManager\""
- "@\"TSUserFilteredClock\""
- "B40@0:8@16@24^{?={?=b7b10b3b1b1b1b9}CQ[0C]}32"
- "Couldn't create TSClockManager!"
- "Couldn't create TSUserFilteredClock!"
- "Couldn't disable timesync for device:%p status:%d"
- "Couldn't enable timesync for device:%p status:%d"
- "Enabled timesync for device:%p"
- "Error syncing time with BT, dropping report! W2 TS:%llu"
- "NO"
- "Q32@0:8Q16@24"
- "Timesync: not locked, clockID: 0x%llx state: %d"
- "W2 btclk(ns):%llu local abs:%llu Synced ts:%llu remote->local latency(ns):%s%llu"
- "YES"
- "_coreTimeSyncManager"
- "_endpointTimeSyncEnabled"
- "_timeSyncClock"
- "clockIdentifier"
- "clockWithClockIdentifier:"
- "convertFromDomainToMachAbsoluteTime:"
- "handleReport:withTimestamp:error:"
- "lockState"
- "remoteDeviceTimestampedReportHandler:device:packet:"
- "sharedClockManager"
- "syncRemoteTimestamp:forEndpoint:"
- "unsignedIntValue"

```
