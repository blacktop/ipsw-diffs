## CoreBluetooth

> `/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`

```diff

-190.47.3.0.0
-  __TEXT.__text: 0xb43f8
+190.50.0.0.0
+  __TEXT.__text: 0xb4c98
   __TEXT.__auth_stubs: 0x13a0
-  __TEXT.__objc_methlist: 0xa09c
+  __TEXT.__objc_methlist: 0xa0cc
   __TEXT.__const: 0x271b
   __TEXT.__oslogstring: 0x2b1b
-  __TEXT.__cstring: 0x14f66
+  __TEXT.__cstring: 0x150e1
   __TEXT.__gcc_except_tab: 0x2f40
   __TEXT.__ustring: 0x82
-  __TEXT.__unwind_info: 0x2150
+  __TEXT.__unwind_info: 0x2160
   __TEXT.__eh_frame: 0x98
   __TEXT.__objc_classname: 0x805
-  __TEXT.__objc_methname: 0x16c24
+  __TEXT.__objc_methname: 0x16cc3
   __TEXT.__objc_methtype: 0x251a
-  __TEXT.__objc_stubs: 0xb6e0
+  __TEXT.__objc_stubs: 0xb720
   __DATA_CONST.__got: 0x3b8
   __DATA_CONST.__const: 0x5580
   __DATA_CONST.__objc_classlist: 0x238
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5018
+  __DATA_CONST.__objc_selrefs: 0x5038
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x160
   __DATA_CONST.__objc_arraydata: 0x130
   __AUTH_CONST.__auth_got: 0x9e0
   __AUTH_CONST.__const: 0x400
-  __AUTH_CONST.__cfstring: 0xdc40
+  __AUTH_CONST.__cfstring: 0xde80
   __AUTH_CONST.__objc_const: 0x11e78
   __AUTH_CONST.__objc_intobj: 0x900
   __AUTH_CONST.__objc_dictobj: 0xf0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8864EDD5-77C1-33F0-815E-74CBDFDD7B1E
-  Functions: 4242
-  Symbols:   13799
-  CStrings:  10452
+  UUID: AB1C5792-FDDE-3096-A404-B53CC88A7253
+  Functions: 4250
+  Symbols:   13820
+  CStrings:  10497
 
Symbols:
+ +[CBDevice convertFromWHBEvent:]
+ +[CBDevice convertFromWHBEvent:].cold.1
+ +[CBDevice convertToWHBEvent:]
+ +[CBDevice convertToWHBEvent:].cold.1
+ +[CBDevice convertToWHBEvent:].cold.2
+ +[CBDevice updateRemoteReceivedEvent:withDeviceKey:withCBXPCKey:]
+ +[CBDevice updateRemoteReceivedEvent:withDeviceKey:withCBXPCKey:].cold.1
+ +[CBDevice updateRemoteSendEvent:fromDeviceInfo:withDeviceKey:withCBXPCKey:]
+ _CBAssignedL2CAPPSMForCompanionServices
+ _objc_msgSend$updateRemoteReceivedEvent:withDeviceKey:withCBXPCKey:
+ _objc_msgSend$updateRemoteSendEvent:fromDeviceInfo:withDeviceKey:withCBXPCKey:
CStrings:
+ "+[CBDevice convertFromWHBEvent:]"
+ "+[CBDevice convertToWHBEvent:]"
+ "+[CBDevice updateRemoteReceivedEvent:withDeviceKey:withCBXPCKey:]"
+ "MobileBluetooth-190.50"
+ "blAM"
+ "blATM"
+ "blAt"
+ "blCh"
+ "convertFromWHBEvent:"
+ "convertFromWHBEvent: receivedEvent null"
+ "convertToWHBEvent:"
+ "convertToWHBEvent: originalDeviceInfo null"
+ "convertToWHBEvent: remoteEvent null"
+ "hkAI"
+ "hkAT"
+ "hkCN"
+ "hkCV"
+ "hkCa"
+ "hkDI"
+ "hkFl"
+ "hkII"
+ "hkS1"
+ "hkS2"
+ "hkSH"
+ "hkVa"
+ "updateRemoteReceivedEvent: no value for xpc key %@"
+ "updateRemoteReceivedEvent:withDeviceKey:withCBXPCKey:"
+ "updateRemoteSendEvent:fromDeviceInfo:withDeviceKey:withCBXPCKey:"
- "MobileBluetooth-190.47.3"

```
