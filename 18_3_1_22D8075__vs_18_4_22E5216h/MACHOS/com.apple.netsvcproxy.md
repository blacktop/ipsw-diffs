## com.apple.netsvcproxy

> `/System/Library/UserEventPlugins/com.apple.netsvcproxy.plugin/com.apple.netsvcproxy`

```diff

-847.80.2.0.0
-  __TEXT.__text: 0xa4f8
-  __TEXT.__auth_stubs: 0x850
-  __TEXT.__objc_stubs: 0x1da0
-  __TEXT.__objc_methlist: 0xa80
-  __TEXT.__objc_methname: 0x2947
-  __TEXT.__cstring: 0xf64
+868.0.0.0.0
+  __TEXT.__text: 0xa380
+  __TEXT.__auth_stubs: 0x810
+  __TEXT.__objc_stubs: 0x1c20
+  __TEXT.__objc_methlist: 0xac0
+  __TEXT.__objc_methname: 0x2944
+  __TEXT.__cstring: 0xf88
   __TEXT.__objc_classname: 0x78
-  __TEXT.__objc_methtype: 0x37e
-  __TEXT.__const: 0x298
-  __TEXT.__oslogstring: 0xadc
-  __TEXT.__gcc_except_tab: 0x290
-  __TEXT.__unwind_info: 0x260
-  __DATA.__auth_got: 0x438
-  __DATA.__got: 0x1b0
-  __DATA.__const: 0x648
-  __DATA.__cfstring: 0x14c0
+  __TEXT.__objc_methtype: 0x300
+  __TEXT.__const: 0x2a0
+  __TEXT.__gcc_except_tab: 0x2b0
+  __TEXT.__oslogstring: 0xb2b
+  __TEXT.__unwind_info: 0x2a8
+  __DATA.__auth_got: 0x418
+  __DATA.__got: 0x1b8
+  __DATA.__const: 0x670
+  __DATA.__cfstring: 0x14e0
   __DATA.__objc_classlist: 0x20
   __DATA.__objc_protolist: 0x10
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x1000
-  __DATA.__objc_selrefs: 0x958
+  __DATA.__objc_const: 0xfa8
+  __DATA.__objc_selrefs: 0x970
   __DATA.__objc_superrefs: 0x10
   __DATA.__objc_ivar: 0x110
   __DATA.__objc_data: 0x140

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 297
-  Symbols:   218
-  CStrings:  774
+  Functions: 308
+  Symbols:   215
+  CStrings:  779
 
Symbols:
+ _NEHelperCacheCopyAppUUIDMapping
+ __Block_object_dispose
+ __xpc_type_uuid
+ _xpc_array_apply
+ _xpc_uuid_get_bytes
- _freemptcpinfo
- _nw_endpoint_copy_address_string
- _nw_endpoint_copy_port_string
- _nw_interface_create_with_index
- _nw_interface_get_index
- _nw_interface_get_name
- _nw_parameters_get_multipath_service
- _nw_path_copy_interface
CStrings:
+ ";;"
+ "="
+ "Adding/replacing header %@ with value \"%@\" due to user-configured headers"
+ "B24@?0Q8@\"NSObject<OS_xpc_object>\"16"
+ "Removing header %@ due to user-configured headers, current value is %@"
+ "Skipping malformed header override: %@"
+ "copyUUIDsForSigningIdentifier:executablePath:"
+ "firstObject"
+ "lastObject"
+ "mergeHTTPHeaders:headerOverrides:"
+ "objectForKey:"
+ "removeObjectForKey:"
+ "setValue:forKey:"
- "%s@%s"
- "Failed to create an nw_interface object with interface index %d"
- "Failed to get the interface name from %@"
- "fillOutConnectionInfo:withPath:interface:remoteEndpoint:parameters:outputHandler:"
- "initWithBytes:length:"
- "initWithBytesNoCopy:length:"
- "numberWithUnsignedShort:"
- "v64@0:8@16@24@32@40@48^{nw_protocol=[16C]^{nw_protocol_identifier}^{nw_protocol_callbacks}^{nw_protocol}^v^{nw_protocol}^v}56"

```
