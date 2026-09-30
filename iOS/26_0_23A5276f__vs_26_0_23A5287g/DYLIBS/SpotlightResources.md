## SpotlightResources

> `/System/Library/PrivateFrameworks/SpotlightResources.framework/SpotlightResources`

```diff

-2381.0.1.0.0
-  __TEXT.__text: 0x25ddc
-  __TEXT.__auth_stubs: 0x6f0
-  __TEXT.__objc_methlist: 0x14a8
+2385.1.0.1.0
+  __TEXT.__text: 0x25f1c
+  __TEXT.__auth_stubs: 0x740
+  __TEXT.__objc_methlist: 0x14b0
   __TEXT.__const: 0xe8
   __TEXT.__gcc_except_tab: 0xbac
-  __TEXT.__cstring: 0x2340
+  __TEXT.__cstring: 0x2348
   __TEXT.__oslogstring: 0x1cbf
-  __TEXT.__unwind_info: 0x7d0
+  __TEXT.__unwind_info: 0x890
   __TEXT.__objc_classname: 0x1ea
-  __TEXT.__objc_methname: 0x3381
-  __TEXT.__objc_methtype: 0x5a4
-  __TEXT.__objc_stubs: 0x3520
+  __TEXT.__objc_methname: 0x3395
+  __TEXT.__objc_methtype: 0x5a6
+  __TEXT.__objc_stubs: 0x3540
   __DATA_CONST.__got: 0x238
   __DATA_CONST.__const: 0x980
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xfa8
+  __DATA_CONST.__objc_selrefs: 0xfb0
   __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0x9a0
-  __AUTH_CONST.__auth_got: 0x388
+  __AUTH_CONST.__auth_got: 0x3b0
   __AUTH_CONST.__const: 0x4a0
   __AUTH_CONST.__cfstring: 0x4820
-  __AUTH_CONST.__objc_const: 0x20a8
+  __AUTH_CONST.__objc_const: 0x20c8
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x180
+  __DATA.__objc_ivar: 0x184
   __DATA.__data: 0x180
-  __DATA.__bss: 0x80
+  __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x690
   __DATA_DIRTY.__data: 0x258
-  __DATA_DIRTY.__bss: 0x2a0
+  __DATA_DIRTY.__bss: 0x298
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreSpotlight.framework/CoreSpotlight
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A6A34F02-1F93-38E3-B121-21911DC3D896
-  Functions: 732
-  Symbols:   2630
-  CStrings:  2165
+  UUID: 321276A7-740C-388A-AA53-007A35198ED2
+  Functions: 730
+  Symbols:   2631
+  CStrings:  2172
 
Symbols:
+ -[SRDefaultsManager hasTestAssets]
+ _OBJC_IVAR_$_SRXPCConnection._spid
+ _dispatch_block_create
+ _getpid
+ _handleMessage:error:.errorCount
+ _objc_msgSend$hasTestAssets
+ _qos_class_self
+ _xpc_dictionary_get_uint64
+ _xpc_dictionary_set_uint64
- +[SRXPCListener handleMessage:error:].cold.1
- -[SRXPCConnection sendMessageAsync:completion:].cold.1
- ___47-[SRXPCConnection sendMessageAsync:completion:]_block_invoke.cold.1
- _sMessageID
CStrings:
+ "HandleRequest"
+ "HandleRequestError"
+ "Q"
+ "SendRequest"
+ "_spid"
+ "hasTestAssets"
+ "pid"
+ "pid:%llu, qos:%llu"
+ "qid"
+ "qos:%llu"
- "Handle message %p"
- "Reply for message[%llu] = %p"
- "Sending message[%llu] = %p"

```
