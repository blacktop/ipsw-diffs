## alwaysonexclavesd

> `/usr/libexec/alwaysonexclavesd`

```diff

-22.0.2.0.0
-  __TEXT.__text: 0x35a8
-  __TEXT.__auth_stubs: 0x6b0
+40.100.4.0.1
+  __TEXT.__text: 0x3d48
+  __TEXT.__auth_stubs: 0x720
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x166
-  __TEXT.__cstring: 0x2bb
+  __TEXT.__const: 0x17a
+  __TEXT.__cstring: 0x22b
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x128
-  __TEXT.__swift5_typeref: 0x82
-  __TEXT.__swift5_reflstr: 0x46
-  __TEXT.__swift5_fieldmd: 0x78
-  __TEXT.__oslogstring: 0x2a2
-  __TEXT.__swift5_types: 0xc
-  __TEXT.__objc_classname: 0x17
-  __TEXT.__objc_methname: 0x13f
-  __TEXT.__objc_methtype: 0xad
-  __TEXT.__swift5_capture: 0x14
+  __TEXT.__objc_classname: 0xa3
+  __TEXT.__objc_methname: 0x1e8
+  __TEXT.__objc_methtype: 0xf5
+  __TEXT.__constg_swiftt: 0x1c8
+  __TEXT.__swift5_typeref: 0xa2
+  __TEXT.__swift5_reflstr: 0x82
+  __TEXT.__swift5_fieldmd: 0xb8
+  __TEXT.__oslogstring: 0x32c
+  __TEXT.__swift5_types: 0x10
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x128
+  __TEXT.__swift5_capture: 0x14
+  __TEXT.__unwind_info: 0x148
   __TEXT.__eh_frame: 0x80
-  __DATA_CONST.__auth_got: 0x358
-  __DATA_CONST.__got: 0x90
-  __DATA_CONST.__auth_ptr: 0x60
-  __DATA_CONST.__const: 0x160
-  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__auth_got: 0x390
+  __DATA_CONST.__got: 0xb8
+  __DATA_CONST.__auth_ptr: 0x70
+  __DATA_CONST.__const: 0x188
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10
-  __DATA.__objc_const: 0x220
+  __DATA.__objc_const: 0x2f0
   __DATA.__objc_selrefs: 0xa0
-  __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x300
-  __DATA.__common: 0x28
+  __DATA.__objc_data: 0xf0
+  __DATA.__data: 0x450
+  __DATA.__common: 0x20
   __DATA.__bss: 0x80
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/AlwaysOnExclavesServices.framework/AlwaysOnExclavesServices

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 054C6873-974A-3A61-B3CA-6D87FB1A9A3B
-  Functions: 64
-  Symbols:   157
-  CStrings:  78
+  UUID: AEA9854F-1F7D-304A-9FAE-82FE24DCB652
+  Functions: 74
+  Symbols:   168
+  CStrings:  89
 
Symbols:
+ _$s8Dispatch0A13WorkItemFlagsVMa
+ _$s8Dispatch0A13WorkItemFlagsVMn
+ _$s8Dispatch0A13WorkItemFlagsVs10SetAlgebraAAMc
+ _$sBbWV
+ _$sBi64_WV
+ _$sSo17OS_dispatch_queueC8DispatchE5async5group3qos5flags7executeySo0a1_b1_F0CSg_AC0D3QoSVAC0D13WorkItemFlagsVyyXBtF
+ _objc_release
+ _objc_retainAutoreleasedReturnValue
+ _swift_bridgeObjectRelease_n
+ _xpc_dictionary_get_bool
+ _xpc_dictionary_get_value
+ _xpc_dictionary_set_bool
- _$ss18_DictionaryStorageC8allocate8capacityAByxq_GSi_tFZ
CStrings:
+ "[XPCService] AlwaysOnXPCService initialized"
+ "[XPCService] Sender does not have the required entitlement"
+ "[xpcService] AlwaysOnExclaves disabled by %s"
+ "[xpcService] AlwaysOnExclaves enabled by %s"
+ "[xpcService] No more requesters, exiting"
+ "[xpcService] xpc_dictionary_create_reply failed"
+ "_TtC17alwaysonexclavesd18AlwaysOnXPCService"
+ "alwaysonexclavesd/xpcService.swift"
+ "clientConnections"
+ "enable"
+ "enabledCount"
+ "forwarder"
+ "from"
+ "success"
+ "v8@?0"
- "[Forwarder] AlwaysOnExclavesForwarder initialized"
- "[Forwarder] Sender does not have the required entitlement"
- "[Forwarder] xpc_dictionary_create_reply failed"
- "alwaysonexclavesd/forwarder.swift"

```
