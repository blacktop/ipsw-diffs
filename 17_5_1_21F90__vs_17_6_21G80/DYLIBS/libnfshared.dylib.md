## libnfshared.dylib

> `/usr/lib/libnfshared.dylib`

```diff

-345.7.0.0.0
-  __TEXT.__text: 0x25648
-  __TEXT.__auth_stubs: 0xca0
-  __TEXT.__objc_methlist: 0x197c
+346.4.0.0.0
+  __TEXT.__text: 0x25750
+  __TEXT.__auth_stubs: 0xcc0
+  __TEXT.__objc_methlist: 0x19a4
   __TEXT.__gcc_except_tab: 0x2b8
   __TEXT.__const: 0x1a8
   __TEXT.__cstring: 0x3b2e
-  __TEXT.__oslogstring: 0x1987
+  __TEXT.__oslogstring: 0x19ca
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x6e4
+  __TEXT.__unwind_info: 0x6dc
   __TEXT.__objc_classname: 0x34d
-  __TEXT.__objc_methname: 0x402e
-  __TEXT.__objc_methtype: 0x996
-  __TEXT.__objc_stubs: 0x2580
+  __TEXT.__objc_methname: 0x40c2
+  __TEXT.__objc_methtype: 0x9ad
+  __TEXT.__objc_stubs: 0x25e0
   __DATA_CONST.__got: 0x98
-  __DATA_CONST.__const: 0x838
+  __DATA_CONST.__const: 0x810
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x3b30
-  __DATA_CONST.__objc_selrefs: 0x1158
+  __DATA_CONST.__objc_const: 0x3b90
+  __DATA_CONST.__objc_selrefs: 0x1170
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_classrefs: 0x140
   __DATA_CONST.__objc_superrefs: 0xc8

   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x660
+  __AUTH_CONST.__auth_got: 0x670
   __AUTH.__objc_data: 0x460
-  __DATA.__objc_ivar: 0x204
+  __DATA.__objc_ivar: 0x20c
   __DATA.__data: 0x3d0
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_ivar: 0x18

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 2595270B-5362-34BE-AE60-944565FECEC5
-  Functions: 662
-  Symbols:   2411
-  CStrings:  2168
+  UUID: 764D7FF9-53EB-3072-B24A-55DB05FB18A4
+  Functions: 664
+  Symbols:   2421
+  CStrings:  2178
 
Symbols:
+ -[NFSecureXPCEventPublisher initWithMachPort:qosPropagation:qos:xpcConnectionQueue:eventSendQueue:]
+ -[NFSecureXPCEventPublisher qosPropagation]
+ -[NFSecureXPCEventPublisher qos]
+ _OBJC_IVAR_$_NFSecureXPCEventPublisher._qos
+ _OBJC_IVAR_$_NFSecureXPCEventPublisher._qosPropagation
+ ___99-[NFSecureXPCEventPublisher initWithMachPort:qosPropagation:qos:xpcConnectionQueue:eventSendQueue:]_block_invoke
+ _dispatch_block_create_with_qos_class
+ _objc_msgSend$initWithMachPort:qosPropagation:qos:xpcConnectionQueue:eventSendQueue:
+ _objc_msgSend$qos
+ _objc_msgSend$qosPropagation
+ _objc_retain_x27
+ _xpc_connection_send_message
- ___49-[NFSecureXPCEventPublisher _sendEvent:dispatch:]_block_invoke.14
- ___80-[NFSecureXPCEventPublisher initWithMachPort:xpcConnectionQueue:eventSendQueue:]_block_invoke
- ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
- _objc_retain_x25
CStrings:
+ "$"
+ "@48@0:8@16B24I28@32@40"
+ "NFSecureXPCEventPublisher_post"
+ "NFSecureXPCEventPublisher_post_wQOS"
+ "TB,R,N,V_qosPropagation"
+ "TI,R,N,V_qos"
+ "_qos"
+ "_qosPropagation"
+ "initWithMachPort:qosPropagation:qos:xpcConnectionQueue:eventSendQueue:"
+ "qos"
+ "qosPropagation"
- "\x14"

```
