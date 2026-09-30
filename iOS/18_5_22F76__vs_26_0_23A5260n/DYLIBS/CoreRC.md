## CoreRC

> `/System/Library/PrivateFrameworks/CoreRC.framework/CoreRC`

```diff

-254.120.2.0.0
-  __TEXT.__text: 0x4948c
-  __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x4d94
-  __TEXT.__const: 0x3f8
-  __TEXT.__cstring: 0xf5ae
+267.0.0.0.0
+  __TEXT.__text: 0x4ad20
+  __TEXT.__auth_stubs: 0x620
+  __TEXT.__objc_methlist: 0x4f1c
+  __TEXT.__const: 0x3e8
+  __TEXT.__cstring: 0xfb56
   __TEXT.__gcc_except_tab: 0xec
   __TEXT.__oslogstring: 0x1d1
-  __TEXT.__unwind_info: 0x1500
+  __TEXT.__unwind_info: 0x1528
   __TEXT.__objc_classname: 0x5ca
-  __TEXT.__objc_methname: 0x9785
-  __TEXT.__objc_methtype: 0x27f0
-  __TEXT.__objc_stubs: 0x7e00
+  __TEXT.__objc_methname: 0x99cb
+  __TEXT.__objc_methtype: 0x28f1
+  __TEXT.__objc_stubs: 0x7fe0
   __DATA_CONST.__got: 0x250
-  __DATA_CONST.__const: 0x1c90
+  __DATA_CONST.__const: 0x1ce0
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_nlclslist: 0x10
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2350
+  __DATA_CONST.__objc_selrefs: 0x23c8
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0x168
-  __AUTH_CONST.__auth_got: 0x318
+  __AUTH_CONST.__auth_got: 0x320
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x3440
-  __AUTH_CONST.__objc_const: 0x8a20
+  __AUTH_CONST.__cfstring: 0x3460
+  __AUTH_CONST.__objc_const: 0x4d10
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x150

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9C957CA6-78A0-3D57-A43D-314EA0B7AF15
-  Functions: 2296
-  Symbols:   7014
-  CStrings:  3964
+  UUID: D7E0EB4A-F9C6-3CE9-992E-F42BF14901C5
+  Functions: 2348
+  Symbols:   6979
+  CStrings:  4016
 
Symbols:
+ +[CECMessage supportsSecureCoding]
+ -[CECMessage encodeWithCoder:]
+ -[CECMessage initWithCoder:]
+ -[CoreCECBus didReceiveRXMessage:]
+ -[CoreCECBus didReceiveRXMessage:].cold.1
+ -[CoreCECBus didSendTXMessage:error:]
+ -[CoreCECBus didSendTXMessage:error:].cold.1
+ -[CoreCECBus injectRXMessage:error:]
+ -[CoreCECBus injectTXMessage:error:]
+ -[CoreCECBusClient injectRXMessage:error:]
+ -[CoreCECBusClient injectRXMessage:error:].cold.1
+ -[CoreCECBusClient injectTXMessage:error:]
+ -[CoreCECBusClient injectTXMessage:error:].cold.1
+ -[CoreCECBusProvider injectRXMessage:error:]
+ -[CoreCECBusProvider injectRXMessage:error:].cold.1
+ -[CoreCECBusProvider injectTXMessage:error:]
+ -[CoreCECBusProvider injectTXMessage:error:].cold.1
+ -[CoreCECBusProvider injectTXMessage:error:].cold.2
+ -[CoreCECBusProvider injectTXMessage:error:].cold.3
+ -[CoreIRLearningSession addMappingWithProtocolID:options:commandToMap:command:repeat:]
+ -[CoreIRLearningSessionClient addMappingWithProtocolID:options:commandToMap:command:repeat:]
+ -[CoreIRLearningSessionClient addMappingWithProtocolID:options:commandToMap:command:repeat:].cold.1
+ -[CoreIRLearningSessionClient addMappingWithProtocolID:options:commandToMap:command:repeat:].cold.2
+ -[CoreIRLearningSessionProvider addMappingWithProtocolID:options:commandToMap:command:repeat:]
+ -[CoreRCManagerClient(CEC) cecBus:rxMessageReceived:]
+ -[CoreRCManagerClient(CEC) cecBus:txMessageSent:error:]
+ -[CoreRCManagerClient(CEC) injectRXMessageAsync:forBus:reply:]
+ -[CoreRCManagerClient(CEC) injectTXMessageAsync:forBus:reply:]
+ -[CoreRCManagerClient(IR) addMappingWithDeviceAsync:withProtocolID:options:commandToMap:command:repeat:reply:]
+ -[CoreRCXPCService(CEC) _injectRXMessageAsync:forBus:reply:]
+ -[CoreRCXPCService(CEC) _injectRXMessageAsync:forBus:reply:].cold.1
+ -[CoreRCXPCService(CEC) _injectRXMessageAsync:forBus:reply:].cold.2
+ -[CoreRCXPCService(CEC) _injectTXMessageAsync:forBus:reply:]
+ -[CoreRCXPCService(CEC) _injectTXMessageAsync:forBus:reply:].cold.1
+ -[CoreRCXPCService(CEC) _injectTXMessageAsync:forBus:reply:].cold.2
+ -[CoreRCXPCService(CEC) cecBus:rxMessageReceived:]
+ -[CoreRCXPCService(CEC) cecBus:rxMessageReceived:].cold.1
+ -[CoreRCXPCService(CEC) cecBus:txMessageSent:error:]
+ -[CoreRCXPCService(CEC) cecBus:txMessageSent:error:].cold.1
+ -[CoreRCXPCService(CEC) injectRXMessageAsync:forBus:reply:]
+ -[CoreRCXPCService(CEC) injectRXMessageAsync:forBus:reply:].cold.1
+ -[CoreRCXPCService(CEC) injectTXMessageAsync:forBus:reply:]
+ -[CoreRCXPCService(CEC) injectTXMessageAsync:forBus:reply:].cold.1
+ -[CoreRCXPCService(IR) _addMappingWithDeviceAsync:withProtocolID:options:commandToMap:command:repeat:reply:]
+ -[CoreRCXPCService(IR) _addMappingWithDeviceAsync:withProtocolID:options:commandToMap:command:repeat:reply:].cold.1
+ -[CoreRCXPCService(IR) _addMappingWithDeviceAsync:withProtocolID:options:commandToMap:command:repeat:reply:].cold.2
+ -[CoreRCXPCService(IR) _addMappingWithDeviceAsync:withProtocolID:options:commandToMap:command:repeat:reply:].cold.3
+ -[CoreRCXPCService(IR) addMappingWithDeviceAsync:withProtocolID:options:commandToMap:command:repeat:reply:]
+ -[CoreRCXPCService(IR) addMappingWithDeviceAsync:withProtocolID:options:commandToMap:command:repeat:reply:].cold.1
+ __OBJC_$_CLASS_PROP_LIST_CECMessage
+ __OBJC_CLASS_PROTOCOLS_$_CECMessage
+ ___107-[CoreRCXPCService(IR) addMappingWithDeviceAsync:withProtocolID:options:commandToMap:command:repeat:reply:]_block_invoke
+ ___42-[CoreCECBusClient injectRXMessage:error:]_block_invoke
+ ___42-[CoreCECBusClient injectTXMessage:error:]_block_invoke
+ ___50-[CoreRCXPCService(CEC) cecBus:rxMessageReceived:]_block_invoke
+ ___52-[CoreRCXPCService(CEC) cecBus:txMessageSent:error:]_block_invoke
+ ___53-[CoreRCManagerClient(CEC) cecBus:rxMessageReceived:]_block_invoke
+ ___55-[CoreRCManagerClient(CEC) cecBus:txMessageSent:error:]_block_invoke
+ ___59-[CoreRCXPCService(CEC) injectRXMessageAsync:forBus:reply:]_block_invoke
+ ___59-[CoreRCXPCService(CEC) injectTXMessageAsync:forBus:reply:]_block_invoke
+ ___92-[CoreIRLearningSessionClient addMappingWithProtocolID:options:commandToMap:command:repeat:]_block_invoke
+ ___block_descriptor_74_e8_32o40o_e24_v16?0?<v?"NSError">8ls32l8s40l8
+ ___block_descriptor_82_e8_32o40o48b_e5_v8?0ls32l8s40l8s48l8
+ _objc_msgSend$_addMappingWithDeviceAsync:withProtocolID:options:commandToMap:command:repeat:reply:
+ _objc_msgSend$_injectRXMessageAsync:forBus:reply:
+ _objc_msgSend$_injectTXMessageAsync:forBus:reply:
+ _objc_msgSend$addMappingWithDeviceAsync:withProtocolID:options:commandToMap:command:repeat:reply:
+ _objc_msgSend$addMappingWithProtocolID:options:commandToMap:command:repeat:
+ _objc_msgSend$cecBus:rxMessageReceived:
+ _objc_msgSend$cecBus:txMessageSent:error:
+ _objc_msgSend$decodeArrayOfObjCType:count:at:
+ _objc_msgSend$didReceiveRXMessage:
+ _objc_msgSend$didSendTXMessage:error:
+ _objc_msgSend$encodeArrayOfObjCType:count:at:
+ _objc_msgSend$injectRXMessage:error:
+ _objc_msgSend$injectRXMessageAsync:forBus:reply:
+ _objc_msgSend$injectTXMessage:error:
+ _objc_msgSend$injectTXMessageAsync:forBus:reply:
+ _objc_release_x25
- -[CoreCECBusProvider sendMessage:withRetryCount:error:].cold.2
CStrings:
+ "%@ injectTXMessage message: %@"
+ "%@ injectTXMessageAsync: %@ forBus: %@ reply: called\n"
+ "-[CoreCECBus didReceiveRXMessage:]"
+ "-[CoreCECBus didSendTXMessage:error:]"
+ "-[CoreCECBusProvider injectRXMessage:error:]"
+ "-[CoreCECBusProvider injectTXMessage:error:]"
+ "-[CoreIRLearningSessionClient addMappingWithProtocolID:options:commandToMap:command:repeat:]"
+ "-[CoreIRLearningSessionProvider addMappingWithProtocolID:options:commandToMap:command:repeat:]"
+ "-[CoreRCManagerClient(CEC) cecBus:rxMessageReceived:]_block_invoke"
+ "-[CoreRCManagerClient(CEC) cecBus:txMessageSent:error:]_block_invoke"
+ "-[CoreRCXPCService(CEC) _injectRXMessageAsync:forBus:reply:]"
+ "-[CoreRCXPCService(CEC) _injectTXMessageAsync:forBus:reply:]"
+ "-[CoreRCXPCService(CEC) cecBus:rxMessageReceived:]"
+ "-[CoreRCXPCService(CEC) cecBus:txMessageSent:error:]"
+ "-[CoreRCXPCService(IR) _addMappingWithDeviceAsync:withProtocolID:options:commandToMap:command:repeat:reply:]"
+ "B48@0:8C16C20Q24Q32Q40"
+ "CoreIRLearningSessionClient addMappingWithProtocolID\n"
+ "CoreRCManagerClient NOTIFY txMessageSent %@\n"
+ "Handling incoming IR command %@"
+ "NOTIFY %@ %@ NEW RX MESSAGE RECEIVED \n"
+ "NOTIFY %@ %@ NEW TX MESSAGE SENT\n"
+ "NOTIFY %@ cecbus:rxMessageReceived %@\n"
+ "NOTIFY %@ cecbus:txMessageSent %@\n"
+ "NOTIFY cecBus %@ rxMessageReceived\n"
+ "_addMappingWithDeviceAsync:withProtocolID:options:commandToMap:command:repeat:reply:"
+ "_injectRXMessageAsync:forBus:reply:"
+ "_injectTXMessageAsync:forBus:reply:"
+ "addMappingWithDeviceAsync:withProtocolID:options:commandToMap:command:repeat:reply:"
+ "addMappingWithProtocolID %d, %d, %d, %x, %x"
+ "addMappingWithProtocolID:options:commandToMap:command:repeat:"
+ "cecBus:rxMessageReceived:"
+ "cecBus:txMessageSent:error:"
+ "decodeArrayOfObjCType:count:at:"
+ "didReceiveRXMessage:"
+ "didSendTXMessage:error:"
+ "encodeArrayOfObjCType:count:at:"
+ "injectRXMessage:error:"
+ "injectRXMessageAsync:forBus:reply:"
+ "injectTXMessage: [%@] from ATV on bus %@ \n"
+ "injectTXMessage: [%@]from ATV \n"
+ "injectTXMessage:error:"
+ "injectTXMessageAsync:forBus:reply:"
+ "status : [%d] injectRXMessage: [%@] to ATV on bus %@ \n"
+ "status: [%d] injectRXMessage: [%@] to ATV \n"
+ "v32@0:8@\"CoreCECBus\"16@\"CECMessage\"24"
+ "v40@0:8@\"CECMessage\"16@\"CoreCECBus\"24@?<v@?@\"NSError\">32"
+ "v40@0:8@\"CoreCECBus\"16@\"CECMessage\"24@\"NSError\"32"
+ "v64@0:8@\"CoreIRDevice\"16C24C28Q32Q40Q48@?<v@?@\"NSError\">56"
+ "v64@0:8@16C24C28Q32Q40Q48@?56"

```
