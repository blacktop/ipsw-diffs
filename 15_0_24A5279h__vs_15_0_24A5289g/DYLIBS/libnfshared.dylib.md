## libnfshared.dylib

> `/usr/lib/libnfshared.dylib`

```diff

-350.26.1.0.0
-  __TEXT.__text: 0x238f8
-  __TEXT.__auth_stubs: 0xa80
-  __TEXT.__objc_methlist: 0x17fc
+350.28.0.0.0
+  __TEXT.__text: 0x23a0c
+  __TEXT.__auth_stubs: 0xac0
+  __TEXT.__objc_methlist: 0x1824
   __TEXT.__gcc_except_tab: 0x3ec
   __TEXT.__const: 0x1c8
   __TEXT.__cstring: 0x3ba4
-  __TEXT.__oslogstring: 0x170f
+  __TEXT.__oslogstring: 0x1753
   __TEXT.__dlopen_cstrs: 0x58
-  __TEXT.__unwind_info: 0x6c0
+  __TEXT.__unwind_info: 0x6b8
   __TEXT.__objc_classname: 0x318
-  __TEXT.__objc_methname: 0x3c24
-  __TEXT.__objc_methtype: 0x8ea
-  __TEXT.__objc_stubs: 0x2300
+  __TEXT.__objc_methname: 0x3cb8
+  __TEXT.__objc_methtype: 0x901
+  __TEXT.__objc_stubs: 0x2360
   __DATA_CONST.__got: 0x1d0
   __DATA_CONST.__const: 0x3f0
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1080
+  __DATA_CONST.__objc_selrefs: 0x1098
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_arraydata: 0x3c8
-  __AUTH_CONST.__auth_got: 0x550
+  __AUTH_CONST.__auth_got: 0x570
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x5d0
+  __AUTH_CONST.__const: 0x5a0
   __AUTH_CONST.__cfstring: 0x35c0
-  __AUTH_CONST.__objc_const: 0x3c80
+  __AUTH_CONST.__objc_const: 0x3ce0
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0xa00
-  __DATA.__objc_ivar: 0x1fc
+  __DATA.__objc_ivar: 0x204
   __DATA.__data: 0x408
-  __DATA.__bss: 0x140
-  __DATA.__common: 0x58
+  __DATA.__bss: 0x138
+  __DATA.__common: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 642
-  Symbols:   1652
+  Functions: 644
+  Symbols:   1662
   CStrings:  619
 
Symbols:
+ -[NFSecureXPCEventPublisher initWithMachPort:qosPropagation:qos:xpcConnectionQueue:eventSendQueue:]
+ -[NFSecureXPCEventPublisher qosPropagation]
+ -[NFSecureXPCEventPublisher qos]
+ OBJC_IVAR_$_NFSecureXPCEventPublisher._qos
+ OBJC_IVAR_$_NFSecureXPCEventPublisher._qosPropagation
+ ___99-[NFSecureXPCEventPublisher initWithMachPort:qosPropagation:qos:xpcConnectionQueue:eventSendQueue:]_block_invoke
+ __os_signpost_emit_with_name_impl
+ _dispatch_block_create_with_qos_class
+ _objc_msgSend$initWithMachPort:qosPropagation:qos:xpcConnectionQueue:eventSendQueue:
+ _objc_msgSend$qos
+ _objc_msgSend$qosPropagation
+ _os_signpost_enabled
+ _xpc_connection_send_message
- __49-[NFSecureXPCEventPublisher _sendEvent:dispatch:]_block_invoke.14
- ___80-[NFSecureXPCEventPublisher initWithMachPort:xpcConnectionQueue:eventSendQueue:]_block_invoke
- ___block_descriptor_40_e8_32bs_e5_v8?0l

```
