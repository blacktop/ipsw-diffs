## IPConfiguration

> `/System/Library/SystemConfiguration/IPConfiguration.bundle/IPConfiguration`

```diff

-534.120.2.0.0
-  __TEXT.__text: 0x5b2a8
-  __TEXT.__auth_stubs: 0x1050
+551.0.0.0.0
+  __TEXT.__text: 0x5c984
+  __TEXT.__auth_stubs: 0x1070
   __TEXT.__const: 0x300
-  __TEXT.__oslogstring: 0x6023
-  __TEXT.__cstring: 0x413d
-  __TEXT.__unwind_info: 0xc38
-  __DATA_CONST.__auth_got: 0x828
-  __DATA_CONST.__got: 0x3a8
-  __DATA_CONST.__auth_ptr: 0xf8
-  __DATA_CONST.__const: 0x1da0
-  __DATA_CONST.__cfstring: 0x2ae0
+  __TEXT.__oslogstring: 0x61a9
+  __TEXT.__cstring: 0x4226
+  __TEXT.__unwind_info: 0xc48
+  __DATA_CONST.__const: 0x1dc8
+  __DATA_CONST.__cfstring: 0x2b20
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__auth_got: 0x838
+  __DATA_CONST.__got: 0x3b8
+  __DATA_CONST.__auth_ptr: 0xf8
   __DATA.__data: 0x118
-  __DATA.__bss: 0x1f8
+  __DATA.__bss: 0x210
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
-  UUID: 1A7ED215-267E-316B-B199-7286F174505C
-  Functions: 1020
-  Symbols:   485
-  CStrings:  2063
+  UUID: A4591080-6F76-358A-8967-AA6D14AB6AC8
+  Functions: 1031
+  Symbols:   489
+  CStrings:  2088
 
Symbols:
+ _CFArrayInsertValueAtIndex
+ __Block_object_dispose
+ _in6addr_any
+ _in6addr_loopback
CStrings:
+ "%s 127.0.0.1 is reserved"
+ "%s(%s) %d.%d.%d.%d"
+ "%s(%s) %s"
+ "%s(%s) cleared"
+ "%s(%s): hwaddr_length %d > %d, truncating"
+ "%s(%s): if_link_length %d > %d"
+ "%s: %@ serviceID %@ method %s"
+ "%s: clearing IPv6 state on first launch"
+ "%s: service_populate_router_arpinfo router MAC missing"
+ "'%@' adding DHCP server IP %s"
+ "'%@' known DHCP server IP %s"
+ "DisablePowerNotification"
+ "IFStateListHandlePublishNeedsAttention"
+ "IFState_copy_serviceIDs_block_invoke"
+ "IFState_init"
+ "IPConfiguration: %s %@ is reserved"
+ "Plugin:IPConfigurationConfiguredInterfaces"
+ "Power notifications are %s%s"
+ "disabled"
+ "enabled"
+ "forced "
+ "service_router_set_hwaddr"
+ "service_router_set_iaddr"

```
