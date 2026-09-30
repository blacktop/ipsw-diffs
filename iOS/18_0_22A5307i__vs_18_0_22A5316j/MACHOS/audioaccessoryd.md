## audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

-20.45.2.0.0
-  __TEXT.__text: 0x197b08
+20.47.3.0.0
+  __TEXT.__text: 0x197cac
   __TEXT.__auth_stubs: 0x2760
-  __TEXT.__objc_stubs: 0xda00
-  __TEXT.__objc_methlist: 0x5898
-  __TEXT.__const: 0x3740
-  __TEXT.__gcc_except_tab: 0x33d8
-  __TEXT.__cstring: 0x289d3
-  __TEXT.__objc_methname: 0x13d34
+  __TEXT.__objc_stubs: 0xdac0
+  __TEXT.__objc_methlist: 0x58b8
+  __TEXT.__const: 0x3760
+  __TEXT.__gcc_except_tab: 0x33dc
+  __TEXT.__cstring: 0x28a03
+  __TEXT.__objc_methname: 0x13e14
   __TEXT.__objc_classname: 0x64f
   __TEXT.__objc_methtype: 0x233b
   __TEXT.__dlopen_cstrs: 0x5a

   __TEXT.__swift5_protos: 0x14
   __TEXT.__swift5_mpenum: 0x14
   __TEXT.__info_plist: 0x599
-  __TEXT.__unwind_info: 0x3680
+  __TEXT.__unwind_info: 0x3678
   __TEXT.__eh_frame: 0x1ea0
   __DATA_CONST.__auth_got: 0x13c0
   __DATA_CONST.__got: 0xac8
-  __DATA_CONST.__auth_ptr: 0x6a0
-  __DATA_CONST.__const: 0xa2c8
-  __DATA_CONST.__cfstring: 0x6780
+  __DATA_CONST.__auth_ptr: 0x6c0
+  __DATA_CONST.__const: 0xa2a8
+  __DATA_CONST.__cfstring: 0x67a0
   __DATA_CONST.__objc_classlist: 0x1c8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x100

   __DATA_CONST.__objc_dictobj: 0x4b0
   __DATA_CONST.__objc_intobj: 0x180
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x10648
-  __DATA.__objc_selrefs: 0x44a0
-  __DATA.__objc_ivar: 0xc60
+  __DATA.__objc_const: 0x106d8
+  __DATA.__objc_selrefs: 0x44d8
+  __DATA.__objc_ivar: 0xc68
   __DATA.__objc_data: 0x1bf0
   __DATA.__data: 0x3028
   __DATA.__bss: 0x6680

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5560
+  Functions: 5562
   Symbols:   1113
-  CStrings:  8382
+  CStrings:  8395
 
CStrings:
+ "-[AADeviceManagerDaemon _accessoryDevicePerformActionsOnChange:]"
+ "-[AAServicesXPCConnection _shouldSendXPCMessage]"
+ "-[AAServicesXPCConnection _shouldSendXPCMessage]_block_invoke"
+ "."
+ "AADevice config applied locally: %!@(MISSING)"
+ "AADevice defaults applied: %!@(MISSING)"
+ "AADevice identifier %!@(MISSING) updated with SR state %!@(MISSING) --> %!@(MISSING)"
+ "AADevice not found"
+ "AADeviceRecord changed: %!@(MISSING)"
+ "AAServicesXPCConnection[%!{(MISSING)pid}]: Reached max outstanding messages (%!d(MISSING)), issue require reset"
+ "AAServicesXPCConnection[%!{(MISSING)pid}]: reset messages count %!d(MISSING),"
+ "Evaluator: skip, SR disabled on current connected source"
+ "SR disabled on current connected source"
+ "TC,N,V_earTipFitTestCapability"
+ "_accessoryDevicePerformActionsOnChange:"
+ "_earTipFitTestCapability"
+ "_shouldSendXPCMessage"
+ "_xpcMessageCounter"
+ "aaServicesRequireReset"
+ "componentsSeparatedByString:"
+ "earTipFitTestCapability"
+ "erFt"
+ "objectAtIndex:"
+ "scheduleSendBarrierBlock:"
+ "setEarTipFitTestCapability:"
+ "smartRoutingStateFlags"
+ "smartRoutingStateUpdated: No AudioAccessoryDevice found for identifier %!@(MISSING)"
- "-[AADeviceManagerDaemon _accessoryDeviceActionsOnFirstConnection:]"
- "-[AADeviceManagerDaemon _accessoryDeviceOverrideListeningMode:]"
- "-[AADeviceManagerDaemon _accessoryDeviceOverrideListeningMode:]_block_invoke"
- "AADeviceRecord found from persistent storage %!@(MISSING)"
- "Applied accessory config locally to device %!@(MISSING)"
- "Applied defaults to device: %!@(MISSING)"
- "Connected device not apple headphone %!@(MISSING)"
- "Evaluator: skip, SR disabled on current connected device"
- "Overriding current listening mode for device %!@(MISSING) --> new config <%!@(MISSING)>"
- "SR disabled on current connected device"
- "_accessoryDeviceActionsOnFirstConnection:"
- "_accessoryDeviceOverrideListeningMode:"
- "device not found"
- "smartRoutingStateUpdated: No Audio Accessory Device found"

```
