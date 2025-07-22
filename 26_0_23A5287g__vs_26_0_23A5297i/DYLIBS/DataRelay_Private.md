## DataRelay_Private

> `/System/Library/PrivateFrameworks/DataRelay_Private.framework/DataRelay_Private`

```diff

-30.51.1.1.1
-  __TEXT.__text: 0xc578
-  __TEXT.__auth_stubs: 0x380
-  __TEXT.__objc_methlist: 0x998
-  __TEXT.__const: 0x50
-  __TEXT.__gcc_except_tab: 0x594
-  __TEXT.__cstring: 0x2252
-  __TEXT.__unwind_info: 0x430
-  __TEXT.__objc_classname: 0xa5
-  __TEXT.__objc_methname: 0x1bf1
-  __TEXT.__objc_methtype: 0x274
-  __TEXT.__objc_stubs: 0x1700
-  __DATA_CONST.__got: 0x118
-  __DATA_CONST.__const: 0x600
+30.54.2.1.1
+  __TEXT.__text: 0xe4d4
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_methlist: 0xa30
+  __TEXT.__const: 0x60
+  __TEXT.__gcc_except_tab: 0x670
+  __TEXT.__cstring: 0x253d
+  __TEXT.__unwind_info: 0x4d0
+  __TEXT.__objc_classname: 0xa8
+  __TEXT.__objc_methname: 0x1d3f
+  __TEXT.__objc_methtype: 0x2a9
+  __TEXT.__objc_stubs: 0x17e0
+  __DATA_CONST.__got: 0x130
+  __DATA_CONST.__const: 0x7a8
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x770
+  __DATA_CONST.__objc_selrefs: 0x7a0
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x100
-  __AUTH_CONST.__auth_got: 0x1d0
-  __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x820
-  __AUTH_CONST.__objc_const: 0xf78
-  __AUTH_CONST.__objc_intobj: 0xf0
+  __AUTH_CONST.__auth_got: 0x238
+  __AUTH_CONST.__const: 0x120
+  __AUTH_CONST.__cfstring: 0x8c0
+  __AUTH_CONST.__objc_const: 0x1068
+  __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x280
-  __DATA.__objc_ivar: 0xc0
+  __DATA.__objc_ivar: 0xd4
   __DATA.__data: 0x4e0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0xf0

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 24095D60-FE9E-3C31-B4C2-CED3B23E6B2C
-  Functions: 344
-  Symbols:   1178
-  CStrings:  703
+  UUID: 764A9FF4-00A8-3C66-B056-5F4FF8FC89AD
+  Functions: 388
+  Symbols:   1310
+  CStrings:  733
 
Symbols:
+ -[DRClient activate:]
+ -[DRClient dealloc]
+ -[DRClient dispatchQueue]
+ -[DRClient rapportSemaphore]
+ -[DRClient removeRequestedDataTypes:completion:]
+ -[DRClient setDispatchQueue:]
+ -[DRClient setRapportSemaphore:]
+ -[DRServer _removeRequestedDataTypes:completion:]
+ -[DRServer _removeRequestedDataTypes:completion:].cold.1
+ -[DRServer addAvailableDataTypes:fromServer:completion:]
+ -[DRServer dispatchQueue]
+ -[DRServer rapportSemaphore]
+ -[DRServer setDispatchQueue:]
+ -[DRServer setRapportSemaphore:]
+ -[DRServerManager clientDictionaryQueue]
+ -[DRServerManager setClientDictionaryQueue:]
+ GCC_except_table10
+ GCC_except_table14
+ GCC_except_table19
+ GCC_except_table20
+ GCC_except_table22
+ GCC_except_table23
+ GCC_except_table26
+ _CFDictionaryGetInt64
+ _OBJC_IVAR_$_DRClient._dispatchQueue
+ _OBJC_IVAR_$_DRClient._rapportSemaphore
+ _OBJC_IVAR_$_DRServer._dispatchQueue
+ _OBJC_IVAR_$_DRServer._rapportSemaphore
+ _OBJC_IVAR_$_DRServerManager._clientDictionaryQueue
+ _RPOptionPeerVerifiedIdentity
+ _RPOptionStatusFlags
+ __Block_object_dispose
+ ___17-[DRClient reset]_block_invoke.cold.1
+ ___17-[DRClient reset]_block_invoke_3
+ ___17-[DRServer reset]_block_invoke.cold.1
+ ___17-[DRServer reset]_block_invoke_4
+ ___19-[DRClient dealloc]_block_invoke
+ ___21-[DRClient activate:]_block_invoke
+ ___21-[DRClient activate:]_block_invoke_2
+ ___26-[DRServer eventsHandler:]_block_invoke
+ ___26-[DRServer eventsHandler:]_block_invoke.cold.1
+ ___27-[DRServerManager setupAAS]_block_invoke_4
+ ___27-[DRServerManager setupAAS]_block_invoke_4.cold.1
+ ___29-[DRClient setReportHandler:]_block_invoke
+ ___29-[DRClient setReportHandler:]_block_invoke.cold.1
+ ___31-[DRClientManager setupRapport]_block_invoke_4
+ ___31-[DRClientManager setupRapport]_block_invoke_4.cold.1
+ ___32-[DRServer serviceAddedHandler:]_block_invoke.cold.2
+ ___32-[DRServer serviceAddedHandler:]_block_invoke_2
+ ___32-[DRServer serviceAddedHandler:]_block_invoke_2.cold.1
+ ___33-[DRPeer deviceFound:completion:]_block_invoke_3.cold.2
+ ___34-[DRClient routedWxDeviceChanged:]_block_invoke.cold.1
+ ___34-[DRClient routedWxDeviceChanged:]_block_invoke_2
+ ___34-[DRServer serviceRemovedHandler:]_block_invoke
+ ___34-[DRServer serviceRemovedHandler:]_block_invoke.cold.1
+ ___45-[DRClient addAvailableDataTypes:completion:]_block_invoke.cold.1
+ ___45-[DRClient addAvailableDataTypes:completion:]_block_invoke_2
+ ___46-[DRClient dataHandler:serviceID:opcode:data:]_block_invoke
+ ___47-[DRServerManager addRequestedDataTypes:types:]_block_invoke.cold.1
+ ___47-[DRServerManager addRequestedDataTypes:types:]_block_invoke_3
+ ___47-[DRServerManager addRequestedDataTypes:types:]_block_invoke_4
+ ___47-[DRServerManager addRequestedDataTypes:types:]_block_invoke_4.cold.1
+ ___48-[DRClient removeAvailableDataTypes:completion:]_block_invoke.cold.1
+ ___48-[DRClient removeAvailableDataTypes:completion:]_block_invoke_2
+ ___48-[DRClient removeRequestedDataTypes:completion:]_block_invoke
+ ___48-[DRClient removeRequestedDataTypes:completion:]_block_invoke.cold.1
+ ___48-[DRClient removeRequestedDataTypes:completion:]_block_invoke.cold.2
+ ___48-[DRClient removeRequestedDataTypes:completion:]_block_invoke.cold.3
+ ___48-[DRClient removeRequestedDataTypes:completion:]_block_invoke.cold.4
+ ___49-[DRServer _removeRequestedDataTypes:completion:]_block_invoke
+ ___50-[DRServerManager removeRequestedDataTypes:types:]_block_invoke
+ ___50-[DRServerManager removeRequestedDataTypes:types:]_block_invoke_2
+ ___50-[DRServerManager removeRequestedDataTypes:types:]_block_invoke_3
+ ___50-[DRServerManager removeRequestedDataTypes:types:]_block_invoke_3.cold.1
+ ___56-[DRServer addAvailableDataTypes:fromServer:completion:]_block_invoke
+ ___56-[DRServer addAvailableDataTypes:fromServer:completion:]_block_invoke.cold.1
+ ___72-[DRClientManager addAvailableDataTypes:dataTypes:wxAddress:fromServer:]_block_invoke_2
+ ___72-[DRClientManager addAvailableDataTypes:dataTypes:wxAddress:fromServer:]_block_invoke_2.cold.1
+ ___83-[DRServerManager addAvailableDataTypesToClient:dataTypes:connectionID:completion:]_block_invoke.cold.1
+ ___83-[DRServerManager addAvailableDataTypesToClient:dataTypes:connectionID:completion:]_block_invoke_3
+ ___83-[DRServerManager addAvailableDataTypesToClient:dataTypes:connectionID:completion:]_block_invoke_3.cold.1
+ ___86-[DRServerManager removeAvailableDataTypesToClient:dataTypes:connectionID:completion:]_block_invoke_2
+ ___86-[DRServerManager removeAvailableDataTypesToClient:dataTypes:connectionID:completion:]_block_invoke_3
+ ___86-[DRServerManager removeAvailableDataTypesToClient:dataTypes:connectionID:completion:]_block_invoke_3.cold.1
+ ___Block_byref_object_copy_
+ ___Block_byref_object_dispose_
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e5_v8?0ls40l8s32l8
+ ___block_descriptor_48_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
+ ___block_descriptor_56_e8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
+ ___block_descriptor_56_e8_32s40bs48w_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls40l8s32l8w48l8
+ ___block_descriptor_56_e8_32s40r48w_e17_v16?0"NSError"8lr40l8w48l8s32l8
+ ___block_descriptor_56_e8_32s40w48w_e17_v16?0"NSError"8ls32l8w40l8w48l8
+ ___block_descriptor_56_e8_32s40w48w_e17_v16?0"NSError"8lw40l8s32l8w48l8
+ ___block_descriptor_56_e8_32s40w_e5_v8?0ls32l8w40l8
+ ___block_descriptor_64_e8_32s40bs48r56w_e17_v16?0"NSError"8ls40l8r48l8w56l8s32l8
+ ___block_descriptor_64_e8_32s40bs48w_e17_v16?0"NSError"8ls40l8w48l8s32l8
+ ___block_descriptor_64_e8_32s40s48r56r_e5_v8?0lr48l8s32l8s40l8r56l8
+ ___block_descriptor_64_e8_32s40s48r_e5_v8?0lr48l8s32l8s40l8
+ ___block_descriptor_68_e8_32s40bs48w_e5_v8?0ls32l8w48l8s40l8
+ ___block_descriptor_72_e8_32s40s_e5_v8?0ls32l8s40l8
+ ___block_descriptor_80_e8_32s40s48s56w64w_e17_v16?0"NSError"8ls32l8w56l8s40l8s48l8w64l8
+ ___block_descriptor_84_e8_32s40s48bs56r64w_e5_v8?0lr56l8s32l8s40l8s48l8w64l8
+ ___block_literal_global.37
+ ___block_literal_global.48
+ ___block_literal_global.83
+ __dispatch_source_type_timer
+ _dispatch_resume
+ _dispatch_semaphore_create
+ _dispatch_semaphore_signal
+ _dispatch_semaphore_wait
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
+ _dispatch_sync
+ _dispatch_time
+ _objc_msgSend$_removeRequestedDataTypes:completion:
+ _objc_msgSend$addAvailableDataTypes:fromServer:completion:
+ _objc_msgSend$clientDictionaryQueue
+ _objc_msgSend$identifier
+ _objc_msgSend$serverDictionary
+ _objc_msgSend$serverFoundHandler
+ _objc_msgSend$serverLostHandler
+ _objc_msgSend$setWxRoute:
+ _objc_msgSend$stringWithFormat:
+ _objc_retainBlock
+ _objc_retain_x25
+ _rapportTransportFlagToString
- -[DRClient addAvailableDataTypes:completion:].cold.1
- -[DRClient removeAvailableDataTypes:completion:].cold.1
- -[DRClient removeRequestedDataTypes:]
- -[DRClient removeRequestedDataTypes:].cold.1
- -[DRClient removeRequestedDataTypes:].cold.2
- -[DRClient removeRequestedDataTypes:].cold.3
- -[DRClient removeRequestedDataTypes:].cold.4
- -[DRClient routedWxDeviceChanged:].cold.1
- -[DRClient setReportHandler:].cold.1
- -[DRClientManager addAvailableDataTypes:dataTypes:wxAddress:fromServer:].cold.1
- -[DRServer addAvailableDataTypes:fromServer:]
- -[DRServer addAvailableDataTypes:fromServer:].cold.1
- -[DRServer serviceAddedHandler:].cold.1
- -[DRServer serviceAddedHandler:].cold.2
- -[DRServer serviceRemovedHandler:].cold.1
- -[DRServerManager addAvailableDataTypesToClient:dataTypes:connectionID:completion:].cold.1
- -[DRServerManager addAvailableDataTypesToClient:dataTypes:connectionID:completion:].cold.2
- -[DRServerManager addRequestedDataTypes:types:].cold.1
- -[DRServerManager addRequestedDataTypes:types:].cold.2
- -[DRServerManager removeRequestedDataTypes:types:].cold.1
- GCC_except_table12
- GCC_except_table13
- GCC_except_table7
- ___27-[DRServerManager setupAAS]_block_invoke_3.cold.1
- ___31-[DRClientManager setupRapport]_block_invoke.33
- ___31-[DRClientManager setupRapport]_block_invoke_3.cold.1
- ___47-[DRServerManager addRequestedDataTypes:types:]_block_invoke_2.cold.1
- ___48-[DRServer removeRequestedDataTypes:completion:]_block_invoke.cold.1
- ___48-[DRServer removeRequestedDataTypes:completion:]_block_invoke_2
- ___83-[DRServerManager addAvailableDataTypesToClient:dataTypes:connectionID:completion:]_block_invoke_2.cold.1
- ___86-[DRServerManager removeAvailableDataTypesToClient:dataTypes:connectionID:completion:]_block_invoke.cold.1
- ___block_descriptor_40_e8_32bs_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls32l8
- ___block_descriptor_40_e8_32s_e17_v16?0"NSTimer"8ls32l8
- ___block_descriptor_48_e8_32bs40w_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24lw40l8s32l8
- ___block_descriptor_48_e8_32s_e5_v8?0ls32l8
- ___block_descriptor_56_e8_32bs40w_e17_v16?0"NSError"8ls32l8w40l8
- ___block_descriptor_56_e8_32s40bs_e5_v8?0ls40l8s32l8
- ___block_descriptor_56_e8_32s40s48s_e17_v16?0"NSError"8ls32l8s40l8s48l8
- ___block_descriptor_64_e8_32s40s48s56bs_e17_v16?0"NSError"8ls56l8s32l8s40l8s48l8
- ___block_descriptor_72_e8_32s40s48w56w_e17_v16?0"NSError"8lw48l8s32l8s40l8w56l8
- ___block_descriptor_76_e8_32s40s48bs56w_e5_v8?0ls32l8s40l8w56l8s48l8
- ___block_literal_global.36
- _objc_msgSend$addAvailableDataTypes:fromServer:
- _objc_msgSend$removeRequestedDataTypes:
- _objc_retain_x24
CStrings:
+ "%llu"
+ "-[DRClient addAvailableDataTypes:completion:]_block_invoke"
+ "-[DRClient removeAvailableDataTypes:completion:]_block_invoke"
+ "-[DRClient removeRequestedDataTypes:completion:]_block_invoke"
+ "-[DRClient reset]_block_invoke"
+ "-[DRClient routedWxDeviceChanged:]_block_invoke"
+ "-[DRClient setReportHandler:]_block_invoke"
+ "-[DRClientManager addAvailableDataTypes:dataTypes:wxAddress:fromServer:]_block_invoke_2"
+ "-[DRClientManager setupRapport]_block_invoke_4"
+ "-[DRServer _removeRequestedDataTypes:completion:]"
+ "-[DRServer addAvailableDataTypes:fromServer:completion:]_block_invoke"
+ "-[DRServer eventsHandler:]_block_invoke"
+ "-[DRServer reset]_block_invoke"
+ "-[DRServer serviceAddedHandler:]_block_invoke_2"
+ "-[DRServer serviceRemovedHandler:]_block_invoke"
+ "-[DRServerManager addAvailableDataTypesToClient:dataTypes:connectionID:completion:]_block_invoke_3"
+ "-[DRServerManager addRequestedDataTypes:types:]_block_invoke"
+ "-[DRServerManager addRequestedDataTypes:types:]_block_invoke_4"
+ "-[DRServerManager removeAvailableDataTypesToClient:dataTypes:connectionID:completion:]_block_invoke_3"
+ "-[DRServerManager removeRequestedDataTypes:types:]_block_invoke_3"
+ "-[DRServerManager setupAAS]_block_invoke_4"
+ "@\"NSObject<OS_dispatch_semaphore>\""
+ "@\"NSObject<OS_dispatch_source>\""
+ "AWDL"
+ "BT"
+ "DRClient dispatch queue now cleared"
+ "DRServer dispatch queue now cleared"
+ "Magnet"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_clientDictionaryQueue"
+ "T@\"NSObject<OS_dispatch_semaphore>\",&,N,V_rapportSemaphore"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_eventSendTimer"
+ "WiFi"
+ "_clientDictionaryQueue"
+ "_rapportSemaphore"
+ "_removeRequestedDataTypes:completion:"
+ "activate done for new client, adding availableDataTypes, identifier %@, dataTypes %@"
+ "addAvailableDataTypes - initializing new client with identifier: %@"
+ "addAvailableDataTypes:fromServer:completion:"
+ "addRequestedDataTypes - initializing new client with identifier: %@"
+ "clientDictionaryQueue"
+ "com.apple.DataRelay.clientDictionaryQueue"
+ "com.apple.datarelay.DRClient"
+ "com.apple.datarelay.DRServer"
+ "com.apple.datarelay.request"
+ "discoveryClient: other device found, identifier: %@, desired identifier: %@"
+ "rapportClient: activateWithCompletion succeeded for identifier: %@, transport: %@"
+ "rapportClient: activateWithCompletion: failed for identifier %@, transport: %@, with error %@"
+ "rapportSemaphore"
+ "setClientDictionaryQueue:"
+ "setRapportSemaphore:"
+ "stringWithFormat:"
- "-[DRClient addAvailableDataTypes:completion:]"
- "-[DRClient removeAvailableDataTypes:completion:]"
- "-[DRClient removeRequestedDataTypes:]"
- "-[DRClient routedWxDeviceChanged:]"
- "-[DRClient setReportHandler:]"
- "-[DRClientManager addAvailableDataTypes:dataTypes:wxAddress:fromServer:]"
- "-[DRClientManager setupRapport]_block_invoke_3"
- "-[DRServer addAvailableDataTypes:fromServer:]"
- "-[DRServer eventsHandler:]"
- "-[DRServer removeRequestedDataTypes:completion:]_block_invoke"
- "-[DRServer serviceAddedHandler:]"
- "-[DRServer serviceRemovedHandler:]"
- "-[DRServerManager addRequestedDataTypes:types:]_block_invoke_2"
- "-[DRServerManager removeAvailableDataTypesToClient:dataTypes:connectionID:completion:]_block_invoke"
- "-[DRServerManager removeRequestedDataTypes:types:]"
- "-[DRServerManager setupAAS]_block_invoke_3"
- "Initializing new DRClient with identifier: %@"
- "T@\"NSTimer\",&,N,V_eventSendTimer"
- "addAvailableDataTypes:fromServer:"
- "com.apple.datarelay.setreport"
- "created new client, adding availableDataTypes, identifier %@, dataTypes %@"
- "discoveryClient: other device found, identifier: %@"
- "new client with identifier: %@"
- "not publishing serviceID %@ due to routing state: addr=%@"
- "rapportClient: activateWithCompletion: %@"
- "v28@0:8Q16B24"

```
