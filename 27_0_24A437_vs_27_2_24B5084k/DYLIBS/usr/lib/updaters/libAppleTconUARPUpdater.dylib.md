## libAppleTconUARPUpdater.dylib

> `/usr/lib/updaters/libAppleTconUARPUpdater.dylib`

```diff

-1587.2.3.0.0
-  __TEXT.__text: 0x6f498
-  __TEXT.__objc_methlist: 0x6894
-  __TEXT.__cstring: 0x7771
+1587.40.26.502.1
+  __TEXT.__text: 0x6f7f8
+  __TEXT.__objc_methlist: 0x68cc
+  __TEXT.__cstring: 0x77e0
   __TEXT.__const: 0x110
-  __TEXT.__oslogstring: 0x388a
+  __TEXT.__oslogstring: 0x38c7
   __TEXT.__gcc_except_tab: 0x3c
-  __TEXT.__unwind_info: 0x2368
+  __TEXT.__unwind_info: 0x2388
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0x578
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1fb0
+  __DATA_CONST.__objc_selrefs: 0x1fd0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x568
   __DATA_CONST.__objc_arraydata: 0xd8
   __DATA_CONST.__got: 0x680
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x5580
-  __AUTH_CONST.__objc_const: 0xd2d8
+  __AUTH_CONST.__objc_const: 0xd2e0
   __AUTH_CONST.__objc_intobj: 0x408
   __AUTH_CONST.__objc_arrayobj: 0x90
   __AUTH_CONST.__auth_got: 0x3f0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2950
-  Symbols:   5727
-  CStrings:  1305
+  Functions: 2958
+  Symbols:   5738
+  CStrings:  1309
 
Symbols:
+ -[UARPEndpointLayer3 noFirmwareAvailable]
+ -[UARPEndpointLayer3 notifyEndpointRemoteNotResponding]
+ -[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackRemoteNotResponding:length:]
+ _OUTLINED_FUNCTION_19
+ _UARPEndpointLayer3RemoteNotResponding
+ _UARPLayer2RemoteNotResponding
+ ___41-[UARPEndpointLayer3 noFirmwareAvailable]_block_invoke
+ ___88-[UARPEndpointLayer3(Layer2EndpointCallbacks) layer2CallbackRemoteNotResponding:length:]_block_invoke
+ _objc_msgSend$layer2CallbackRemoteNotResponding:length:
+ _objc_msgSend$layer3EndpointRemoteNotResponding:
+ _objc_msgSend$notifyEndpointRemoteNotResponding
CStrings:
+ "%s: no firmware available"
+ "-[UARPEndpointLayer3 noFirmwareAvailable]_block_invoke"
+ "-[UARPEndpointLayer3 notifyEndpointRemoteNotResponding]"
+ "Endpoint %@: Remote Not Responding"
+ "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xc31"
- "\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xb31"
```
