## libusrtcp.dylib

> `/usr/lib/libusrtcp.dylib`

```diff

-3762.82.2.0.0
-  __TEXT.__text: 0x4fcf4
-  __TEXT.__auth_stubs: 0xba0
+3762.102.1.0.0
+  __TEXT.__text: 0x4fe90
+  __TEXT.__auth_stubs: 0xbb0
   __TEXT.__objc_methlist: 0x14
   __TEXT.__const: 0x184
-  __TEXT.__oslogstring: 0xa281
-  __TEXT.__cstring: 0x1741
+  __TEXT.__oslogstring: 0xa34f
+  __TEXT.__cstring: 0x175c
   __TEXT.__unwind_info: 0x3dc
   __TEXT.__objc_classname: 0x13
   __TEXT.__objc_methname: 0x8

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x48
   __DATA_CONST.__objc_selrefs: 0x8
+  __DATA_CONST.__objc_classrefs: 0x8
+  __DATA_CONST.__objc_superrefs: 0x8
   __AUTH_CONST.__const: 0x168
   __AUTH_CONST.__objc_const: 0x48
-  __AUTH_CONST.__auth_got: 0x5d0
+  __AUTH_CONST.__auth_got: 0x5d8
   __AUTH.__data: 0x190
-  __DATA.__objc_classrefs: 0x8
-  __DATA.__objc_superrefs: 0x8
   __DATA.__data: 0x10
   __DATA.__bss: 0x6a0
   __DATA_DIRTY.__objc_data: 0x50

   - /System/Library/Frameworks/Network.framework/Network
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C4B37182-1603-3479-9813-477D2F03B9FE
+  UUID: 05D8BD8D-ED03-3FB4-BB8F-D304689ADE43
   Functions: 314
-  Symbols:   863
-  CStrings:  884
+  Symbols:   864
+  CStrings:  888
 
Symbols:
+ _____nw_signpost_is_enabled_block_invoke.130
+ _____nw_signpost_is_enabled_block_invoke.431
+ ___block_descriptor_tmp.129
+ ___block_descriptor_tmp.193
+ ___block_descriptor_tmp.424
+ ___block_literal_global.126
+ ___block_literal_global.425
+ _nw_ip_metadata_get_dscp_value
- _____nw_signpost_is_enabled_block_invoke.138
- _____nw_signpost_is_enabled_block_invoke.439
- ___block_descriptor_tmp.137
- ___block_descriptor_tmp.201
- ___block_descriptor_tmp.432
- ___block_literal_global.134
- ___block_literal_global.433
CStrings:
+ "%{public}s called with null (dscp_value <= _MAX_DSCP)"
+ "%{public}s called with null (dscp_value <= _MAX_DSCP), dumping backtrace:%{public}s"
+ "%{public}s called with null (dscp_value <= _MAX_DSCP), no backtrace"
+ "B16@?0^{nw_frame={os_object_header_s=^vii}{?=^{nw_frame}^^{nw_frame}}{?=^{nw_frame}^^{nw_frame}}IIII{?=^{nw_frame_protocol_metadata}^^{nw_frame_protocol_metadata}}^?^v^{dispatch_data_s}^{nw_mem_buffer_manager}*{nw_frame_protocol_metadata={?=^{nw_frame_protocol_metadata}^^{nw_frame_protocol_metadata}}[16C]QQ^{nw_protocol_metadata}iiCb2b1b1b1b1b1b1[6C]}ISSCCCCb1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b6[1C]}8"
+ "__nw_frame_set_dscp_value"
- "B16@?0^{nw_frame={os_object_header_s=^vii}{?=^{nw_frame}^^{nw_frame}}{?=^{nw_frame}^^{nw_frame}}IIII{?=^{nw_frame_protocol_metadata}^^{nw_frame_protocol_metadata}}^?^v^{dispatch_data_s}^{nw_mem_buffer_manager}*{nw_frame_protocol_metadata={?=^{nw_frame_protocol_metadata}^^{nw_frame_protocol_metadata}}[16C]QQ^{nw_protocol_metadata}iib2b1b1b1b1b1b1[7C]}ISSCCCCb1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b1b6[1C]}8"

```
