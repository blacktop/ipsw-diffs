## Synapse

> `/System/Library/PrivateFrameworks/Synapse.framework/Versions/A/Synapse`

```diff

-148.0.0.0.0
-  __TEXT.__text: 0x3a42c
-  __TEXT.__objc_methlist: 0x3154
+149.0.0.0.0
+  __TEXT.__text: 0x3a30c
+  __TEXT.__objc_methlist: 0x3124
   __TEXT.__const: 0x160
-  __TEXT.__gcc_except_tab: 0xa00
-  __TEXT.__cstring: 0x2d48
-  __TEXT.__oslogstring: 0x44f3
+  __TEXT.__gcc_except_tab: 0x9ec
+  __TEXT.__cstring: 0x2cfc
+  __TEXT.__oslogstring: 0x44cb
   __TEXT.__ustring: 0x16e
   __TEXT.__dlopen_cstrs: 0x412
-  __TEXT.__unwind_info: 0x1190
+  __TEXT.__unwind_info: 0x1180
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x468
+  __DATA_CONST.__const: 0x448
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x10
-  __DATA_CONST.__objc_protolist: 0xe8
+  __DATA_CONST.__objc_protolist: 0xe0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1cb0
-  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_selrefs: 0x1ca8
+  __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x168
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__got: 0x360
-  __AUTH_CONST.__const: 0x1670
-  __AUTH_CONST.__cfstring: 0x2400
-  __AUTH_CONST.__objc_const: 0xc4a8
+  __AUTH_CONST.__const: 0x1630
+  __AUTH_CONST.__cfstring: 0x2420
+  __AUTH_CONST.__objc_const: 0xc3f0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x5f0
   __DATA.__objc_ivar: 0x2b0
-  __DATA.__data: 0xaf0
+  __DATA.__data: 0xa90
   __DATA.__bss: 0xf9
   __DATA_DIRTY.__objc_data: 0xf00
   __DATA_DIRTY.__data: 0x1

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1482
-  Symbols:   3281
-  CStrings:  730
+  Functions: 1478
+  Symbols:   3266
+  CStrings:  729
 
Symbols:
+ -[SYBacklinkMonitorOperation backlinkFilterCache]
+ -[SYBacklinkMonitorOperation setBacklinkFilterCache:]
+ -[SYBacklinkMonitorService _filterCachesByActivityType]
+ -[SYBacklinkMonitorService set_filterCachesByActivityType:]
+ OBJC_IVAR_$_SYBacklinkMonitorOperation._backlinkFilterCache
+ OBJC_IVAR_$_SYBacklinkMonitorService.__filterCachesByActivityType
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
- GCC_except_table18
- OBJC_IVAR_$_SYBacklinkMonitorClient.__filterCache
- OBJC_IVAR_$_SYBacklinkMonitorClient.__previousFilterCacheMatched
- __49-[SYBacklinkMonitorServiceHandle setFilterCache:]_block_invoke
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
