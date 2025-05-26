## BTLEServer

> `/usr/sbin/BTLEServer`

```diff

-334.14.0.0.0
-  __TEXT.__text: 0x4f0a4
-  __TEXT.__auth_stubs: 0x1000
-  __TEXT.__objc_stubs: 0x9aa0
-  __TEXT.__objc_methlist: 0x4f34
-  __TEXT.__const: 0x2f8
+336.2.0.0.0
+  __TEXT.__text: 0x50e14
+  __TEXT.__auth_stubs: 0x1020
+  __TEXT.__objc_stubs: 0x9c80
+  __TEXT.__objc_methlist: 0x5074
+  __TEXT.__const: 0x330
   __TEXT.__gcc_except_tab: 0x7ac
-  __TEXT.__cstring: 0x25fe
-  __TEXT.__oslogstring: 0x6549
-  __TEXT.__objc_methname: 0xd1ca
-  __TEXT.__objc_classname: 0x670
-  __TEXT.__objc_methtype: 0x1f16
+  __TEXT.__cstring: 0x26bd
+  __TEXT.__oslogstring: 0x6773
+  __TEXT.__objc_methname: 0xd38c
+  __TEXT.__objc_classname: 0x689
+  __TEXT.__objc_methtype: 0x1f62
   __TEXT.__ustring: 0xc6
-  __TEXT.__unwind_info: 0x11cc
-  __DATA_CONST.__auth_got: 0x810
+  __TEXT.__unwind_info: 0x1230
+  __DATA_CONST.__auth_got: 0x820
   __DATA_CONST.__got: 0x450
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x1170
-  __DATA_CONST.__cfstring: 0x3620
-  __DATA_CONST.__objc_classlist: 0x1f8
+  __DATA_CONST.__const: 0x11b0
+  __DATA_CONST.__cfstring: 0x37a0
+  __DATA_CONST.__objc_classlist: 0x200
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x3c8
-  __DATA_CONST.__objc_superrefs: 0x1c0
-  __DATA_CONST.__objc_intobj: 0x540
+  __DATA_CONST.__objc_classrefs: 0x3d0
+  __DATA_CONST.__objc_superrefs: 0x1c8
+  __DATA_CONST.__objc_intobj: 0x5d0
   __DATA_CONST.__objc_arraydata: 0x188
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_dictobj: 0x118
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xc688
-  __DATA.__objc_selrefs: 0x2ef0
-  __DATA.__objc_ivar: 0x59c
-  __DATA.__objc_data: 0x13b0
+  __DATA.__objc_const: 0xc848
+  __DATA.__objc_selrefs: 0x2f68
+  __DATA.__objc_ivar: 0x5a8
+  __DATA.__objc_data: 0x1400
   __DATA.__data: 0x788
   __DATA.__bss: 0x100
   __DATA.__common: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2168
-  Symbols:   483
-  CStrings:  3693
+  Functions: 2204
+  Symbols:   485
+  CStrings:  3737
 
Symbols:
+ __os_signpost_emit_with_name_impl
+ _os_signpost_enabled
CStrings:
+ "\x1f\x02"
+ "%02x:%02x:%02x:%02x:%02x:%02x"
+ "%@ notifying pencil that wireless charging is %s"
+ "%@ received HID charger notification: %@"
+ "%@ unexpectedly receiving authentication status: success=%{BOOL}d"
+ "%{public, signpost.description:begin_time}llu"
+ "A2538"
+ "A2538_AuthenticationDidSucceed"
+ "ChargingConnInterval"
+ "ChargingConnLatency"
+ "Connection exists!"
+ "DoAPSiri - SiriState changed 0x%0X -> 0x%0X"
+ "Failed to create haptics interface"
+ "Failed to create motion interface"
+ "HIDApplePencilGen3Device"
+ "Ignoring no accessories notification"
+ "No accessories on charger"
+ "NormalConnInterval"
+ "NormalConnLatency"
+ "Pencil3"
+ "Posting Find My specific auth successful notification for: %@"
+ "Posting auth failed notification for: %@"
+ "Posting auth successful notification for: %@"
+ "Previously connected peripheral .."
+ "SendPencilFeedback"
+ "T@\"CBL2CAPChannel\",&,N,V_mfiAuthChannel"
+ "_mfiAuthChannel"
+ "blePairingNoAccessories:"
+ "copy"
+ "identifierForConnectionWithUUID:"
+ "kCBMsgArgRemoteAddress"
+ "mfiAuthChannel"
+ "mutableBytes"
+ "newHapticsDevice:keyholeID:"
+ "newMotionDevice:keyholeID:"
+ "no accessories"
+ "notifyPencilOnChargerState:"
+ "retrieveConnectedPeripheralsWithServices:allowAll:"
+ "retrievePairingInfoForPeripheral:"
+ "setChargingConnParamDefaults"
+ "setMfiAuthChannel:"
+ "setNormalConnParamDefaults"
+ "stateToStr:"
+ "supportedAccessories:forProductGroup:isComplete:"
+ "transportClientServerDisconnected!!"
+ "v24@0:8@\"ACCBLEPairingProvider\"16"
+ "v36@0:8@\"NSSet\"16@\"UARPProductGroup\"24B32"
- "\x1f\x01"
- "DoAPSiri- SiriState changed 0x%0X -> 0x%0X"
- "Received HID charger notification: %s"

```
