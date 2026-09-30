## DeviceInterface

> `/System/Library/Templates/Data/Library/Apple/System/Library/PrivateFrameworks/DeviceInterface.framework/Versions/A/DeviceInterface`

```diff

-205.0.0.0.0
-  __TEXT.__text: 0x84b0c
+208.120.5.0.0
+  __TEXT.__text: 0x85abc
   __TEXT.__auth_stubs: 0x640
-  __TEXT.__objc_methlist: 0x5a8c
+  __TEXT.__objc_methlist: 0x5b6c
   __TEXT.__const: 0x64
   __TEXT.__cstring: 0x4821
   __TEXT.__gcc_except_tab: 0x8a4
-  __TEXT.__oslogstring: 0x3db7
-  __TEXT.__unwind_info: 0x1358
-  __TEXT.__objc_classname: 0xd2a
-  __TEXT.__objc_methname: 0xd107
-  __TEXT.__objc_methtype: 0x6378
-  __TEXT.__objc_stubs: 0x60a0
-  __DATA_CONST.__got: 0x238
+  __TEXT.__oslogstring: 0x3e95
+  __TEXT.__unwind_info: 0x1380
+  __TEXT.__objc_classname: 0xd4b
+  __TEXT.__objc_methname: 0xd38e
+  __TEXT.__objc_methtype: 0x642f
+  __TEXT.__objc_stubs: 0x62e0
+  __DATA_CONST.__got: 0x240
   __DATA_CONST.__const: 0x60
-  __DATA_CONST.__objc_classlist: 0x2d8
+  __DATA_CONST.__objc_classlist: 0x2e0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x21f0
+  __DATA_CONST.__objc_selrefs: 0x2260
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x2c8
+  __DATA_CONST.__objc_superrefs: 0x2d0
   __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0x7c0
   __AUTH_CONST.__cfstring: 0x620
-  __AUTH_CONST.__objc_const: 0xc1a0
+  __AUTH_CONST.__objc_const: 0xc3c0
   __AUTH_CONST.__objc_intobj: 0x120
-  __AUTH.__objc_data: 0x1c70
-  __AUTH.__data: 0x4a0
-  __DATA.__objc_ivar: 0xa44
+  __AUTH.__objc_data: 0x1cc0
+  __AUTH.__data: 0x4a8
+  __DATA.__objc_ivar: 0xa64
   __DATA.__data: 0x4b0
   __DATA.__bss: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  Functions: 2465
-  Symbols:   4881
-  CStrings:  3225
+  Functions: 2487
+  Symbols:   4936
+  CStrings:  3263
 
Symbols:
+ -[DebugUSBInterfaceIOUSBHost createHardwareBuffer:]
+ -[DebugUSBInterfaceIOUSBHostClient createHardwareBuffer:]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerial clientConnected]
+ -[DockChannelSerialInterfaceIOUserDockChannelSerial setClientConnected:]
+ -[KISInterfaceDebugUSB setStaticIdentificationBuffer:]
+ -[KISInterfaceDebugUSB startFullExploreForSegment:]
+ -[KISInterfaceDebugUSB staticIdentificationBuffer]
+ -[KISInterfaceDebugUSBBuffer initWithInterfaceClient:data:size:hardwareBuffer:]
+ -[KISInterfaceIdentificationBuffer .cxx_destruct]
+ -[KISInterfaceIdentificationBuffer bufferPointer]
+ -[KISInterfaceIdentificationBuffer buffer]
+ -[KISInterfaceIdentificationBuffer complete]
+ -[KISInterfaceIdentificationBuffer initWithSize:maxSegmentSize:]
+ -[KISInterfaceIdentificationBuffer maxSegmentSize]
+ -[KISInterfaceIdentificationBuffer receivedSegmentCount]
+ -[KISInterfaceIdentificationBuffer segmentSizeForSegment:]
+ -[KISInterfaceIdentificationBuffer segments]
+ -[KISInterfaceIdentificationBuffer size]
+ -[KISInterfaceIdentificationBuffer writeData:length:segment:]
+ OBJC_IVAR_$_DockChannelSerialInterfaceIOUserDockChannelSerial._clientConnected
+ OBJC_IVAR_$_KISInterfaceDebugUSB._staticIdentificationBuffer
+ OBJC_IVAR_$_KISInterfaceIdentificationBuffer._buffer
+ OBJC_IVAR_$_KISInterfaceIdentificationBuffer._complete
+ OBJC_IVAR_$_KISInterfaceIdentificationBuffer._maxSegmentSize
+ OBJC_IVAR_$_KISInterfaceIdentificationBuffer._receivedSegmentCount
+ OBJC_IVAR_$_KISInterfaceIdentificationBuffer._segments
+ OBJC_IVAR_$_KISInterfaceIdentificationBuffer._size
+ _OBJC_CLASS_$_KISInterfaceIdentificationBuffer
+ _OBJC_METACLASS_$_KISInterfaceIdentificationBuffer
+ __OBJC_$_INSTANCE_METHODS_KISInterfaceIdentificationBuffer
+ __OBJC_$_INSTANCE_VARIABLES_KISInterfaceIdentificationBuffer
+ __OBJC_$_PROP_LIST_KISInterfaceIdentificationBuffer
+ __OBJC_CLASS_RO_$_KISInterfaceIdentificationBuffer
+ __OBJC_METACLASS_RO_$_KISInterfaceIdentificationBuffer
+ ___44-[RSMInterfaceKIS unlockInterfaceForClient:]_block_invoke_2
+ ___block_descriptor_65_e8_32s_e11_v20?0i8Q12l
+ _debug_usb_interface_client_create_hardware_buffer
+ _debug_usb_interface_client_transfer_buffer
+ _debug_usb_interface_client_transfer_buffer_async
+ _debug_usb_interface_iousbhost_create_hardware_buffer
+ _debug_usb_interface_iousbhost_transfer_buffer
+ _debug_usb_interface_iousbhost_transfer_buffer_async
+ _dock_channel_serial_interface_iouserdockchannelserial_read_data_available_space
+ _objc_msgSend$bufferPointer
+ _objc_msgSend$clientConnected
+ _objc_msgSend$complete
+ _objc_msgSend$createHardwareBuffer:
+ _objc_msgSend$currentDoorbells
+ _objc_msgSend$currentProtocol
+ _objc_msgSend$currentProtocolVersion
+ _objc_msgSend$initWithInterfaceClient:data:size:hardwareBuffer:
+ _objc_msgSend$initWithSize:maxSegmentSize:
+ _objc_msgSend$maxSegmentSize
+ _objc_msgSend$protocolClients
+ _objc_msgSend$protocolGenerationCounter
+ _objc_msgSend$receivedSegmentCount
+ _objc_msgSend$segmentSizeForSegment:
+ _objc_msgSend$segments
+ _objc_msgSend$setClientConnected:
+ _objc_msgSend$size
+ _objc_msgSend$startFullExploreForSegment:
+ _objc_msgSend$writeData:length:segment:
- -[KISInterfaceDebugUSBBuffer initWithInterfaceClient:data:size:]
- ___block_descriptor_73_e8_32s_e11_v20?0i8Q12l
- _debug_usb_interface_client_transfer
- _debug_usb_interface_client_transfer_async
- _debug_usb_interface_iousbhost_transfer
- _debug_usb_interface_iousbhost_transfer_async
- _objc_msgSend$closeFile
CStrings:
+ "!\x13\x12"
+ "%s: sendCommandResult: %x, readResponseResult: %x"
+ "@\"KISInterfaceIdentificationBuffer\""
+ "@24@0:8I16I20"
+ "@28@0:8r*16I24"
+ "@36@0:8@16r*24I32"
+ "@40@0:8^{debug_usb_interface_client_t=^v^{debug_usb_interface_client_functions_t}}16r^v24I32B36"
+ "B32@0:8r*16I24I28"
+ "Error retrieving pipe descriptors."
+ "KISInterfaceIdentificationBuffer"
+ "KIS[0x%llx] Received full explore segment %d/%d."
+ "KIS[0x%llx] Starting full explore segment %d/%d."
+ "Pipe stall encountered in transfer: %@"
+ "T@\"KISInterfaceIdentificationBuffer\",&,N,V_staticIdentificationBuffer"
+ "T@\"NSMutableData\",R,N,V_buffer"
+ "TB,N,V_clientConnected"
+ "TB,R,N,V_complete"
+ "TI,R,N,V_maxSegmentSize"
+ "TI,R,N,V_receivedSegmentCount"
+ "TI,R,N,V_segments"
+ "_clientConnected"
+ "_complete"
+ "_maxSegmentSize"
+ "_receivedSegmentCount"
+ "_segments"
+ "_staticIdentificationBuffer"
+ "bufferPointer"
+ "clientConnected"
+ "complete"
+ "createHardwareBuffer:"
+ "initWithInterfaceClient:data:size:hardwareBuffer:"
+ "initWithSize:maxSegmentSize:"
+ "maxSegmentSize"
+ "receivedSegmentCount"
+ "segmentSizeForSegment:"
+ "segments"
+ "setClientConnected:"
+ "setStaticIdentificationBuffer:"
+ "startFullExploreForSegment:"
+ "staticIdentificationBuffer"
+ "writeData:length:segment:"
+ "\xe8\""
- "\x11\x13\x12"
- "@28@0:8*16I24"
- "closeFile"
- "\xe7\""

```
