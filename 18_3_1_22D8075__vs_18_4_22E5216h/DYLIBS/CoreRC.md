## CoreRC

> `/System/Library/PrivateFrameworks/CoreRC.framework/CoreRC`

```diff

-249.80.2.0.0
-  __TEXT.__text: 0x456a0
+254.100.6.0.0
+  __TEXT.__text: 0x49474
   __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_methlist: 0x4558
-  __TEXT.__const: 0x3a0
-  __TEXT.__cstring: 0xf38e
+  __TEXT.__objc_methlist: 0x4d94
+  __TEXT.__const: 0x3f8
+  __TEXT.__cstring: 0xf5ae
   __TEXT.__gcc_except_tab: 0xec
-  __TEXT.__oslogstring: 0x1a5
-  __TEXT.__unwind_info: 0x1188
-  __TEXT.__objc_classname: 0x5b8
-  __TEXT.__objc_methname: 0x955f
-  __TEXT.__objc_methtype: 0x27a9
-  __TEXT.__objc_stubs: 0x7c40
-  __DATA_CONST.__got: 0x248
-  __DATA_CONST.__const: 0x1c40
-  __DATA_CONST.__objc_classlist: 0x170
+  __TEXT.__oslogstring: 0x1d1
+  __TEXT.__unwind_info: 0x1500
+  __TEXT.__objc_classname: 0x5ca
+  __TEXT.__objc_methname: 0x9785
+  __TEXT.__objc_methtype: 0x27f0
+  __TEXT.__objc_stubs: 0x7e00
+  __DATA_CONST.__got: 0x250
+  __DATA_CONST.__const: 0x1c90
+  __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_nlclslist: 0x10
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2248
+  __DATA_CONST.__objc_selrefs: 0x2350
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x138
-  __DATA_CONST.__objc_arraydata: 0x160
+  __DATA_CONST.__objc_superrefs: 0x140
+  __DATA_CONST.__objc_arraydata: 0x168
   __AUTH_CONST.__auth_got: 0x318
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x3300
-  __AUTH_CONST.__objc_const: 0x92a0
+  __AUTH_CONST.__cfstring: 0x3440
+  __AUTH_CONST.__objc_const: 0x8a20
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x150
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0xd20
-  __DATA.__objc_ivar: 0x2dc
+  __AUTH.__objc_data: 0xd70
+  __DATA.__objc_ivar: 0x300
   __DATA.__data: 0x1398
   __DATA.__bss: 0x370
   __DATA_DIRTY.__objc_data: 0x140

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1743
-  Symbols:   2051
-  CStrings:  3480
+  Functions: 2296
+  Symbols:   2773
+  CStrings:  3546
 
Symbols:
+ _OBJC_CLASS_$_CECEDIDAttributes
+ _OBJC_METACLASS_$_CECEDIDAttributes
+ _kCECInterfacePropertyEDIDAttributes
+ _objc_retain_x2
+ _objc_retain_x21
- _CoreCECPhysicalAddressForPackedPhysicalAddress
- _CoreCECPhysicalAddressIsOnStreamPath
- _CoreCECPhysicalAddressIsValid
- _CoreCECPhysicalAddressString
- _CoreRCVersionNumber
- _CoreRCVersionString
- _PackedPhysicalAddressForCoreCECPhysicalAddress
- _kCECInterfacePropertyEDID
- _objc_release_x25
- _objc_retain_x22
CStrings:
+ " %@"
+ " EDID: %@"
+ " PA: %s;"
+ " Route: %s;"
+ " pID: 0x%04lX;"
+ " vID: 0x%04lX;"
+ " year: %ld;"
+ "%@ %s ("
+ "%@ performRemoveFromBus:reply: called\n"
+ "-[CoreCECDevice removeFromBus]"
+ "-[CoreCECDeviceClient removeFromBus]"
+ "-[CoreRCDevice addOwningClient:]"
+ "-[CoreRCDevice removeAllOwningClients]"
+ "-[CoreRCDevice removeOwningClient:]"
+ "-[CoreRCXPCService connectionInvalidated:]_block_invoke"
+ "-[CoreRCXPCService(CEC) _performRemoveFromBus:reply:]"
+ "@\"CECEDIDAttributes\""
+ "@20@0:8S16"
+ "@24@0:8B16S20"
+ "@24@0:8q16"
+ "@44@0:8@16B24C28S32@36"
+ "@44@0:8@16B24C28S32Q36"
+ "@48@0:8C16S20@24@32Q40"
+ "@56@0:8@16C24S28@32@40Q48"
+ "Another device is already active source: %@, streamPath: %s\n"
+ "B24@0:8^S16"
+ "B32@0:8S16S20^@24"
+ "B32@0:8^B16^S24"
+ "B32@0:8^S16^Q24"
+ "B32@0:8^S16^S24"
+ "B36@0:8^@16^@24S32"
+ "B40@0:8^@16^@24S32C36"
+ "CECEDIDAttributes"
+ "Converting deprecated physical address: %lx"
+ "CoreCECBus removeDeviceWithType async operation failed %d\n"
+ "CoreCECDevice removeFromBus async operation failed %@\n"
+ "Ignored suspicious routing change %@, currentStreamPath=%s\n"
+ "Last known physical address: %s"
+ "No more owning clients, removing %@"
+ "Set stream path happened before adding the device, take active source now: %s"
+ "Storing physical address: %s"
+ "T@\"CECEDIDAttributes\",C,N,V_edidAttributes"
+ "T@\"NSMutableArray\",&,N,V_mappings"
+ "T@\"NSString\",C,N,V_modelName"
+ "T@\"NSString\",C,N,V_uuid"
+ "TS,N,V_address"
+ "TS,N,V_physicalAddress"
+ "TS,N,V_streamPath"
+ "TS,R,N,V_lastStreamPath"
+ "TS,R,N,V_physicalAddress"
+ "Tq,N,V_productID"
+ "Tq,N,V_vendorID"
+ "Tq,N,V_week"
+ "Tq,N,V_year"
+ "_address"
+ "_blockedMessages"
+ "_edidAttributes"
+ "_modelName"
+ "_performRemoveFromBus:reply:"
+ "_productID"
+ "_uuid"
+ "_week"
+ "_year"
+ "add owning client: %@  self:%@ %@"
+ "address"
+ "edidAttributes"
+ "initWithAttributes:"
+ "initWithInterface with physical address: %s"
+ "initWithModelName:"
+ "initWithVendorID:"
+ "kCECInterfacePropertyEDIDAttributes"
+ "modelName"
+ "performRemoveFromBus:reply:"
+ "previousCECPhysicalAddress"
+ "productID"
+ "remove all owning clients: %@  self:%@"
+ "remove owning client: %@  self:%@ %@"
+ "removeAllOwningClients"
+ "removeFromBus"
+ "removeFromBus %@"
+ "setAddress:"
+ "setBlockedMessages:"
+ "setEdidAttributes:"
+ "setModelName:"
+ "setProductID:"
+ "setUuid:"
+ "setWeek:"
+ "setYear:"
+ "uuid"
+ "v24@0:8B16S20"
+ "v28@0:8S16@?20"
+ "v28@0:8S16@?<v@?@\"CoreCECBus\"@\"NSError\">20"
+ "v40@0:8@\"CoreCECBus\"16B24S28@?<v@?@\"NSError\">32"
+ "v40@0:8@16B24S28@?32"
+ "v48@0:8@\"CoreCECDeviceBasicAttributes\"16@\"CoreCECBus\"24C32S36@?<v@?@\"CoreCECDevice\"@\"NSError\">40"
+ "v48@0:8@16@24C32S36@?40"
+ "week"
+ "year"
- " PA: %@;"
- " Route: %@;"
- "%@ %@ ("
- "-[NSDictionary(CoreCECInterfaceProperties) getLinkState:physicalAddress:]"
- "<invalid address: %08x>"
- "@28@0:8B16Q20"
- "@48@0:8@16B24C28Q32@40"
- "@48@0:8@16B24C28Q32Q40"
- "@52@0:8C16Q20@28@36Q44"
- "@60@0:8@16C24Q28@36@44Q52"
- "Another device is already active source: %@, streamPath: %@\n"
- "B32@0:8^B16^Q24"
- "B32@0:8^Q16^Q24"
- "B40@0:8Q16Q24^@32"
- "B40@0:8^@16^@24Q32"
- "B44@0:8^@16^@24Q32C40"
- "CoreCECBus removeDeviceWithType async operation failed\n"
- "Ignored suspicious routing change %@, currentStreamPath=%@\n"
- "Invalid Physical Address: %@\n"
- "Last known physical address: %@"
- "Set stream path happened before adding the device, take active source now: %@"
- "Storing physical address: %@"
- "T@\"NSMutableArray\",C,N,V_mappings"
- "TQ,N,V_physicalAddress"
- "TQ,N,V_streamPath"
- "TQ,R,N,V_lastStreamPath"
- "TQ,R,N,V_physicalAddress"
- "analyticsDelay"
- "initWithInterface with physical address: %@"
- "kCECInterfacePropertyEDID"
- "v28@0:8B16Q20"
- "v32@0:8Q16@?24"
- "v32@0:8Q16@?<v@?@\"CoreCECBus\"@\"NSError\">24"
- "v44@0:8@\"CoreCECBus\"16B24Q28@?<v@?@\"NSError\">36"
- "v44@0:8@16B24Q28@?36"
- "v52@0:8@\"CoreCECDeviceBasicAttributes\"16@\"CoreCECBus\"24C32Q36@?<v@?@\"CoreCECDevice\"@\"NSError\">44"
- "v52@0:8@16@24C32Q36@?44"

```
