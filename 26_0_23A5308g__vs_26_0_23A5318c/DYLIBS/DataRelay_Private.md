## DataRelay_Private

> `/System/Library/PrivateFrameworks/DataRelay_Private.framework/DataRelay_Private`

```diff

-30.58.1.0.0
-  __TEXT.__text: 0xea3c
+30.59.1.7.0
+  __TEXT.__text: 0xed2c
   __TEXT.__auth_stubs: 0x450
-  __TEXT.__objc_methlist: 0xaa8
+  __TEXT.__objc_methlist: 0xac8
   __TEXT.__const: 0x60
-  __TEXT.__gcc_except_tab: 0x6a0
-  __TEXT.__cstring: 0x257a
-  __TEXT.__unwind_info: 0x4f0
+  __TEXT.__gcc_except_tab: 0x6b4
+  __TEXT.__cstring: 0x26c0
+  __TEXT.__unwind_info: 0x510
   __TEXT.__objc_classname: 0xc0
-  __TEXT.__objc_methname: 0x1dde
-  __TEXT.__objc_methtype: 0x2d5
-  __TEXT.__objc_stubs: 0x1880
-  __DATA_CONST.__got: 0x140
-  __DATA_CONST.__const: 0x7d0
+  __TEXT.__objc_methname: 0x1de1
+  __TEXT.__objc_methtype: 0x2ca
+  __TEXT.__objc_stubs: 0x18c0
+  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__const: 0x7c0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x7d8
   __DATA_CONST.__objc_superrefs: 0x60
   __DATA_CONST.__objc_arraydata: 0x130
   __AUTH_CONST.__auth_got: 0x238
-  __AUTH_CONST.__const: 0x120
-  __AUTH_CONST.__cfstring: 0x8c0
+  __AUTH_CONST.__const: 0xe0
+  __AUTH_CONST.__cfstring: 0x940
   __AUTH_CONST.__objc_const: 0x1128
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_arrayobj: 0x60

   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0258E572-959C-385A-A79C-EBC3CEEFDB5B
-  Functions: 399
-  Symbols:   1342
-  CStrings:  753
+  UUID: A459B791-190A-3ED1-8508-BA576E0D4A37
+  Functions: 402
+  Symbols:   1347
+  CStrings:  766
 
Symbols:
+ -[DRClient dataHandler:serviceID:opcode:data:].cold.1
+ -[DRClient routedWxDeviceChanged:].cold.1
+ -[DRPeer _activate:]
+ -[DRPeer _activate:].cold.1
+ -[DRPeer dispatchQueue]
+ -[DRPeer isActivated]
+ -[DRPeer setDispatchQueue:]
+ -[DRPeer setIsActivated:]
+ -[DRServer dealloc]
+ -[DRServer eventsHandler:].cold.1
+ -[DRServer serviceAddedHandler:].cold.1
+ -[DRServer serviceRemovedHandler:].cold.1
+ GCC_except_table17
+ _OBJC_IVAR_$_DRPeer._dispatchQueue
+ _OBJC_IVAR_$_DRPeer._isActivated
+ ___20-[DRPeer _activate:]_block_invoke
+ ___20-[DRPeer _activate:]_block_invoke.cold.1
+ ___20-[DRPeer _activate:]_block_invoke_2
+ ___20-[DRPeer _activate:]_block_invoke_3
+ ___20-[DRPeer _activate:]_block_invoke_3.cold.1
+ ___block_descriptor_56_e8_32s40bs48w_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls40l8w48l8s32l8
+ ___block_descriptor_64_e8_32s40bs48w_e17_v16?0"NSError"8lw48l8s40l8s32l8
+ ___block_literal_global.87
+ _dispatch_activate
+ _objc_msgSend$_activate:
+ _objc_msgSend$dispatchQueue
+ _objc_msgSend$isActivated
- -[DRClient dispatchQueue]
- -[DRClient setDispatchQueue:]
- -[DRServer dispatchQueue]
- -[DRServer setDispatchQueue:]
- GCC_except_table18
- GCC_except_table20
- _OBJC_CLASS_$_NSTimer
- _OBJC_IVAR_$_DRClient._dispatchQueue
- _OBJC_IVAR_$_DRServer._dispatchQueue
- ___17-[DRClient reset]_block_invoke.cold.1
- ___17-[DRClient reset]_block_invoke_3
- ___17-[DRServer reset]_block_invoke.cold.1
- ___17-[DRServer reset]_block_invoke_4
- ___19-[DRPeer activate:]_block_invoke.cold.1
- ___19-[DRPeer activate:]_block_invoke_2
- ___19-[DRPeer activate:]_block_invoke_2.cold.1
- ___19-[DRPeer activate:]_block_invoke_3
- ___19-[DRPeer activate:]_block_invoke_4
- ___19-[DRPeer activate:]_block_invoke_4.cold.1
- ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSTimer"8ls40l8s32l8
- ___block_descriptor_56_e8_32bs40w_e17_v16?0"NSError"8lw40l8s32l8
- ___block_descriptor_56_e8_32s40bs48w_e51_v32?0"NSDictionary"8"NSDictionary"16"NSError"24ls40l8s32l8w48l8
- ___block_literal_global.52
- ___block_literal_global.88
- _dispatch_resume
- _objc_msgSend$scheduledTimerWithTimeInterval:repeats:block:
CStrings:
+ "-[DRClient dataHandler:serviceID:opcode:data:]"
+ "-[DRClient routedWxDeviceChanged:]"
+ "-[DRPeer _activate:]"
+ "-[DRPeer _activate:]_block_invoke"
+ "-[DRPeer _activate:]_block_invoke_3"
+ "-[DRServer eventsHandler:]"
+ "-[DRServer serviceAddedHandler:]"
+ "-[DRServer serviceRemovedHandler:]"
+ "Event"
+ "Ignoring %s as DRClient has not been activated"
+ "Ignoring events as DRServer has not been activated yet"
+ "Ignoring serviceAdded as DRServer is not activated"
+ "Ignoring serviceRemoved as DRServer is not activated"
+ "ServiceAdded"
+ "ServiceRemoved"
+ "Skipping routedWxDeviceChanged as DRClient is not activated"
+ "T@\"NSObject<OS_dispatch_source>\",&,N,V_discoveryTimer"
+ "TB,V_isActivated"
+ "Unknown(%lu)"
+ "_activate:"
- "-[DRClient reset]_block_invoke"
- "-[DRPeer activate:]_block_invoke"
- "-[DRPeer activate:]_block_invoke_2"
- "-[DRPeer activate:]_block_invoke_4"
- "-[DRServer reset]_block_invoke"
- "@\"NSTimer\""
- "DRClient dispatch queue now cleared"
- "DRServer dispatch queue now cleared"
- "T@\"NSTimer\",&,N,V_discoveryTimer"
- "scheduledTimerWithTimeInterval:repeats:block:"
- "v16@?0@\"NSTimer\"8"

```
