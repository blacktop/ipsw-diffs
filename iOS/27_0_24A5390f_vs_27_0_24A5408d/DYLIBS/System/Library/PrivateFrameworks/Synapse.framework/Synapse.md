## Synapse

> `/System/Library/PrivateFrameworks/Synapse.framework/Synapse`

```diff

-148.0.0.0.0
-  __TEXT.__text: 0x37a5c
-  __TEXT.__objc_methlist: 0x325c
+149.0.0.0.0
+  __TEXT.__text: 0x37944
+  __TEXT.__objc_methlist: 0x322c
   __TEXT.__const: 0x158
-  __TEXT.__gcc_except_tab: 0xb4c
-  __TEXT.__cstring: 0x2f89
-  __TEXT.__oslogstring: 0x4459
+  __TEXT.__gcc_except_tab: 0xb38
+  __TEXT.__cstring: 0x2f3d
+  __TEXT.__oslogstring: 0x4431
   __TEXT.__dlopen_cstrs: 0x5b0
   __TEXT.__ustring: 0x154
-  __TEXT.__unwind_info: 0x1278
+  __TEXT.__unwind_info: 0x1268
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x14f8
+  __DATA_CONST.__const: 0x14d8
   __DATA_CONST.__objc_classlist: 0x240
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xf0
+  __DATA_CONST.__objc_protolist: 0xe8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1cb8
-  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_selrefs: 0x1cb0
+  __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__got: 0x388
-  __AUTH_CONST.__const: 0x440
-  __AUTH_CONST.__cfstring: 0x2480
-  __AUTH_CONST.__objc_const: 0xdbb8
+  __AUTH_CONST.__const: 0x400
+  __AUTH_CONST.__cfstring: 0x24a0
+  __AUTH_CONST.__objc_const: 0xdb00
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x8c0
   __DATA.__objc_ivar: 0x2bc
-  __DATA.__data: 0xb40
+  __DATA.__data: 0xae0
   __DATA.__bss: 0x1b1
   __DATA_DIRTY.__objc_data: 0xdc0
   __DATA_DIRTY.__data: 0x1

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1491
-  Symbols:   3285
-  CStrings:  740
+  Functions: 1487
+  Symbols:   3272
+  CStrings:  739
 
Symbols:
+ -[SYBacklinkMonitorOperation backlinkFilterCache]
+ -[SYBacklinkMonitorOperation setBacklinkFilterCache:]
+ -[SYBacklinkMonitorService _filterCachesByActivityType]
+ -[SYBacklinkMonitorService set_filterCachesByActivityType:]
+ _OBJC_IVAR_$_SYBacklinkMonitorOperation._backlinkFilterCache
+ _OBJC_IVAR_$_SYBacklinkMonitorService.__filterCachesByActivityType
+ _SYPathByRemovingPrivatePrefix
+ _objc_msgSend$_filterCachesByActivityType
+ _objc_msgSend$backlinkFilterCache
+ _objc_msgSend$setBacklinkFilterCache:
+ _objc_msgSend$substringFromIndex:
- -[SYBacklinkMonitorClient _filterCache]
- -[SYBacklinkMonitorClient _previousFilterCacheMatched]
- -[SYBacklinkMonitorClient set_filterCache:]
- -[SYBacklinkMonitorClient set_previousFilterCacheMatched:]
- -[SYBacklinkMonitorClient updateWithFilterCache:]
- -[SYBacklinkMonitorServiceHandle setFilterCache:]
- _OBJC_IVAR_$_SYBacklinkMonitorClient.__filterCache
- _OBJC_IVAR_$_SYBacklinkMonitorClient.__previousFilterCacheMatched
- __OBJC_$_PROTOCOL_INSTANCE_METHODS_SYBacklinkMonitorClientProtocol
- __OBJC_$_PROTOCOL_METHOD_TYPES_SYBacklinkMonitorClientProtocol
- __OBJC_$_PROTOCOL_REFS_SYBacklinkMonitorClientProtocol
- __OBJC_CLASS_PROTOCOLS_$_SYBacklinkMonitorClient
- __OBJC_LABEL_PROTOCOL_$_SYBacklinkMonitorClientProtocol
- __OBJC_PROTOCOL_$_SYBacklinkMonitorClientProtocol
- __OBJC_PROTOCOL_REFERENCE_$_SYBacklinkMonitorClientProtocol
- ___49-[SYBacklinkMonitorServiceHandle setFilterCache:]_block_invoke
- ___54-[SYBacklinkMonitorService _notesActivationDidChange:]_block_invoke
- ___block_descriptor_32_e57_v32?0"NSNumber"8"SYBacklinkMonitorServiceHandle"16^B24l
- _objc_msgSend$_filterCache
- _objc_msgSend$_previousFilterCacheMatched
- _objc_msgSend$setFilterCache:
- _objc_msgSend$set_filterCache:
- _objc_msgSend$set_previousFilterCacheMatched:
- _objc_msgSend$updateWithFilterCache:
CStrings:
+ "/private"
+ "/private/var/"
+ "BacklinkOperation %p: Filter cache miss, skipping query and hiding indicator."
+ "\xa1"
- "/var/mobile/Library/Mail/AttachmentData/"
- "BacklinkClient: Changed activity was filtered out: %p."
- "BacklinkServiceHandle: Error creating remote service proxy: %@"
- "v32@?0@\"NSNumber\"8@\"SYBacklinkMonitorServiceHandle\"16^B24"
- "\x91"
```
