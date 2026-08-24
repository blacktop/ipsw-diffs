## HMFoundation

> `/System/Library/PrivateFrameworks/HMFoundation.framework/Versions/A/HMFoundation`

```diff

-1490.2.0.0.0
-  __TEXT.__text: 0x9b8fc
+1493.1.5.4.1
+  __TEXT.__text: 0x9c2d4
   __TEXT.__delay_helper: 0xdc
-  __TEXT.__objc_methlist: 0x773c
-  __TEXT.__const: 0x3028
+  __TEXT.__objc_methlist: 0x7794
+  __TEXT.__const: 0x3100
   __TEXT.__dlopen_cstrs: 0x10a
   __TEXT.__swift5_typeref: 0xb6e
   __TEXT.__swift5_reflstr: 0x42a

   __TEXT.__swift5_fieldmd: 0x7c4
   __TEXT.__swift5_proto: 0x6c
   __TEXT.__swift5_types: 0xb4
-  __TEXT.__cstring: 0x2fab
+  __TEXT.__cstring: 0x3029
   __TEXT.__swift5_capture: 0x670
   __TEXT.__swift_as_entry: 0x19c
   __TEXT.__swift_as_ret: 0x1c4
   __TEXT.__swift_as_cont: 0x230
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__oslogstring: 0x7abd
-  __TEXT.__gcc_except_tab: 0x18ec
+  __TEXT.__oslogstring: 0x7a62
+  __TEXT.__gcc_except_tab: 0x19c8
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x30d8
+  __TEXT.__unwind_info: 0x30e8
   __TEXT.__eh_frame: 0x3268
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x7c0
+  __DATA_CONST.__const: 0x7e0
   __DATA_CONST.__objc_classlist: 0x470
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x1b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3078
+  __DATA_CONST.__objc_selrefs: 0x30a8
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x380
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x800
-  __AUTH_CONST.__const: 0x32c0
-  __AUTH_CONST.__cfstring: 0x47a0
-  __AUTH_CONST.__objc_const: 0xdfe0
+  __AUTH_CONST.__const: 0x3320
+  __AUTH_CONST.__cfstring: 0x4860
+  __AUTH_CONST.__objc_const: 0xe030
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x10d8
+  __AUTH_CONST.__auth_got: 0x1118
   __AUTH.__objc_data: 0x1180
   __AUTH.__data: 0x1e8
   __AUTH.__thread_vars: 0x18

   __DATA.__objc_ivar: 0x19c
   __DATA.__data: 0x250c
   __DATA.__bss: 0xa10
-  __DATA_DIRTY.__objc_ivar: 0x55c
+  __DATA_DIRTY.__objc_ivar: 0x560
   __DATA_DIRTY.__objc_data: 0x1a40
   __DATA_DIRTY.__data: 0x270
   __DATA_DIRTY.__bss: 0x5c8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3650
-  Symbols:   6504
-  CStrings:  1369
+  Functions: 3659
+  Symbols:   6534
+  CStrings:  1375
 
Symbols:
+ +[NSData(FastEncoding) hmf_fastEncodedDataForObject:]
+ +[NSData(FastEncoding) hmf_fastEncodedSizeForObject:]
+ -[__HMFNetAddressMonitor _handlePathUpdate:]
+ -[__HMFNetAddressMonitor currentPath]
+ -[__HMFNetAddressMonitor pathEvaluator]
+ -[__HMFNetAddressMonitor pathMonitor]
+ -[__HMFNetAddressMonitor setCurrentPath:]
+ -[__HMFNetAddressMonitor setPathEvaluator:]
+ -[__HMFNetAddressMonitor setPathMonitor:]
+ _HMFFastEncodedSize
+ _HMFProductInfoEclipseBOSVersion
+ _HMFProductInfoEclipsePopOSVersion
+ _HMFProductInfoFizzBOSVersion
+ _HMFProductInfoFizzPopOSVersion
+ _HMFProductInfoLotusBOSVersion
+ _HMFProductInfoLotusPopOSVersion
+ _HMFProductInfoOrchidBOSVersion
+ _HMFProductInfoOrchidPopOSVersion
+ _HMFProductInfoRaveBOSVersion
+ _HMFProductInfoRavePopOSVersion
+ __45-[__HMFNetAddressMonitor initWithNetAddress:]_block_invoke
+ __OBJC_$_PROP_LIST_HMFFastEncodable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_HMFFastEncodable
+ ___45-[__HMFNetAddressMonitor initWithNetAddress:]_block_invoke
+ ___HMFPathDescription
+ ___block_descriptor_40_e8_32w_e30_v16?0"NSObject<OS_nw_path>"8l
+ ___block_descriptor_48_e8_32s40w_e5_v8?0l
+ ___copy_helper_block_e8_32s40w
+ _nw_endpoint_create_host
+ _nw_parameters_create
+ _nw_path_create_evaluator_for_endpoint
+ _nw_path_evaluator_cancel
+ _nw_path_evaluator_copy_path
+ _nw_path_evaluator_set_update_handler
+ _nw_path_get_status
+ _nw_path_monitor_cancel
+ _nw_path_monitor_create
+ _nw_path_monitor_set_queue
+ _nw_path_monitor_set_update_handler
+ _nw_path_monitor_start
+ _nw_path_uses_interface_type
+ _objc_msgSend$_handlePathUpdate:
+ _objc_msgSend$hmf_fastEncodedSize
+ _objc_msgSend$hmf_fastEncodedSizeForObject:
- -[__HMFNetAddressMonitor currentNetworkFlags]
- -[__HMFNetAddressMonitor handleNetworkReachabilityChange:]
- -[__HMFNetAddressMonitor networkReachabilityRef]
- -[__HMFNetAddressMonitor setCurrentNetworkFlags:]
- _SCNetworkReachabilityCreateWithAddress
- _SCNetworkReachabilityCreateWithName
- _SCNetworkReachabilityGetFlags
- _SCNetworkReachabilitySetCallback
- _SCNetworkReachabilitySetDispatchQueue
- ___SCNetworkReachabilityFlagsToString
- __networkReachabilityChangeCallback
- _objc_msgSend$currentNetworkFlags
- _objc_msgSend$handleNetworkReachabilityChange:
- _objc_msgSend$setCurrentNetworkFlags:
CStrings:
+ "0"
+ "Failed to create endpoint for %@"
+ "Failed to create network path monitor"
+ "Failed to create path evaluator for %@"
+ "Received path update: %@"
+ "Unexpected object type %@ (%@) in fast encoding"
+ "[%{public}@] Failed to create endpoint for %@"
+ "[%{public}@] Failed to create network path monitor"
+ "[%{public}@] Failed to create path evaluator for %@"
+ "[%{public}@] Received path update: %@"
+ "cellular"
+ "invalid"
+ "satisfiable"
+ "satisfied"
+ "unsatisfied"
+ "v16@?0@\"NSObject<OS_nw_path>\"8"
+ "wifi"
+ "wired"
- "Failed to create network reachability monitor%@."
- "Failed to get initial reachability"
- "Initial flags: %@"
- "Reachable"
- "Received notification of updated flags: %@"
- "Updating reachability to: %@"
- "[%{public}@] Failed to create network reachability monitor%@."
- "[%{public}@] Failed to get initial reachability"
- "[%{public}@] Initial flags: %@"
- "[%{public}@] Received notification of updated flags: %@"
- "[%{public}@] Updating reachability to: %@"
- "for %@"
```
