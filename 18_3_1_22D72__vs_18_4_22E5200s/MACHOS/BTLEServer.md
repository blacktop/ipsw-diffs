## BTLEServer

> `/usr/sbin/BTLEServer`

```diff

-343.1.0.0.0
-  __TEXT.__text: 0x735e4
+344.25.0.0.0
+  __TEXT.__text: 0x7421c
   __TEXT.__auth_stubs: 0x1080
-  __TEXT.__objc_stubs: 0xbf60
-  __TEXT.__objc_methlist: 0x6428
-  __TEXT.__const: 0x508
-  __TEXT.__cstring: 0x313e
-  __TEXT.__objc_methname: 0x10ff0
-  __TEXT.__oslogstring: 0xb4bc
-  __TEXT.__objc_classname: 0x7f0
-  __TEXT.__objc_methtype: 0x2d86
-  __TEXT.__gcc_except_tab: 0xdf4
+  __TEXT.__objc_stubs: 0xbfa0
+  __TEXT.__objc_methlist: 0x6e24
+  __TEXT.__const: 0x510
+  __TEXT.__cstring: 0x314b
+  __TEXT.__objc_methname: 0x11138
+  __TEXT.__oslogstring: 0xb791
+  __TEXT.__objc_classname: 0x7f2
+  __TEXT.__objc_methtype: 0x2e42
+  __TEXT.__gcc_except_tab: 0xdfc
   __TEXT.__dlopen_cstrs: 0x13e
   __TEXT.__ustring: 0xc6
-  __TEXT.__unwind_info: 0x1768
+  __TEXT.__unwind_info: 0x17b8
   __DATA_CONST.__auth_got: 0x850
   __DATA_CONST.__got: 0x8a8
   __DATA_CONST.__auth_ptr: 0x18
-  __DATA_CONST.__const: 0x15a0
-  __DATA_CONST.__cfstring: 0x47a0
+  __DATA_CONST.__const: 0x15c8
+  __DATA_CONST.__cfstring: 0x47c0
   __DATA_CONST.__objc_classlist: 0x270
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0xb0

   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0x118
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0xee80
-  __DATA.__objc_selrefs: 0x3948
-  __DATA.__objc_ivar: 0x758
+  __DATA.__objc_const: 0xdd30
+  __DATA.__objc_selrefs: 0x3c78
+  __DATA.__objc_ivar: 0x75c
   __DATA.__objc_data: 0x1860
   __DATA.__data: 0x848
   __DATA.__bss: 0x1a8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2734
+  Functions: 2742
   Symbols:   544
-  CStrings:  4738
+  CStrings:  4758
 
CStrings:
+ "\x19"
+ "%s Health Observation TLVs for peripheral \"%{private, mask.hash}@\": numOfObservations %u"
+ "%s Health Observation for peripheral \"%{private, mask.hash}@\": bundle # %u,  numOfInfo %u"
+ "%s Health Observation for peripheral \"%{private, mask.hash}@\": bundle # %u,  supplementalInfo %u"
+ "%s Health Observation for peripheral \"%{private, mask.hash}@\": bundle # %u, classType %u"
+ "%s Health Observation for peripheral \"%{private, mask.hash}@\": bundle # %u, flags %u"
+ "%s Health Observation for peripheral \"%{private, mask.hash}@\": bundle # %u, len %u"
+ "%s Health Observation for peripheral \"%{private, mask.hash}@\": bundle # %u, observationType %d"
+ "Central %@ subscribed to NotificationSourceCharacteristic, interestedCategory %x"
+ "Missing observation type in %s health observation, bundle # %u, flags: %u"
+ "T@\"NSMutableDictionary\",&,N,V_activeCentralsInterestedCategories"
+ "_activeCentralsInterestedCategories"
+ "activeCentralsInterestedCategories"
+ "com.starkey."
+ "peripheralManager:didChannelSoundingProcedureEvent:results:error:"
+ "peripheralManager:didCloseL2CAPChannel:"
+ "peripheralManager:l2CapChannel:didReceiveData:"
+ "setActiveCentralsInterestedCategories:"
+ "v32@0:8@\"CBPeripheralManager\"16@\"CBL2CAPChannel\"24"
+ "v40@0:8@\"CBPeripheralManager\"16@\"CBL2CAPChannel\"24@\"NSData\"32"
+ "v48@0:8@\"CBPeripheralManager\"16@\"CBCentral\"24@\"NSDictionary\"32@\"NSError\"40"
- "Central %@ subscribed to NotificationSourceCharacteristic"

```
