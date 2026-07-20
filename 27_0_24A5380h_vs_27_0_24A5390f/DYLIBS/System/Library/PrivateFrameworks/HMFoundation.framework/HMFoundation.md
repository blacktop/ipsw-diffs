## HMFoundation

> `/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1484.2.0.0.0
-  __TEXT.__text: 0x97cbc
+1490.2.0.1.1
+  __TEXT.__text: 0x981c8
   __TEXT.__delay_stubs: 0x400
   __TEXT.__delay_helper: 0x294
-  __TEXT.__objc_methlist: 0x7944
-  __TEXT.__const: 0x3028
+  __TEXT.__objc_methlist: 0x7994
+  __TEXT.__const: 0x3010
   __TEXT.__dlopen_cstrs: 0xf8
   __TEXT.__swift5_typeref: 0xb6e
   __TEXT.__swift5_reflstr: 0x42a

   __TEXT.__swift5_fieldmd: 0x7c4
   __TEXT.__swift5_proto: 0x6c
   __TEXT.__swift5_types: 0xb4
-  __TEXT.__cstring: 0x312b
+  __TEXT.__cstring: 0x3197
   __TEXT.__swift5_capture: 0x670
   __TEXT.__swift_as_entry: 0x19c
   __TEXT.__swift_as_ret: 0x1c4
   __TEXT.__swift_as_cont: 0x228
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__oslogstring: 0x801d
-  __TEXT.__gcc_except_tab: 0x1970
+  __TEXT.__oslogstring: 0x8109
+  __TEXT.__gcc_except_tab: 0x1a9c
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x31e0
+  __TEXT.__unwind_info: 0x31e8
   __TEXT.__eh_frame: 0x3278
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x15c8
+  __DATA_CONST.__const: 0x1638
   __DATA_CONST.__objc_classlist: 0x478
   __DATA_CONST.__objc_catlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x1d8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3100
+  __DATA_CONST.__objc_selrefs: 0x3130
   __DATA_CONST.__objc_protorefs: 0x40
   __DATA_CONST.__objc_superrefs: 0x388
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__got: 0x820
   __AUTH_CONST.__const: 0x2338
-  __AUTH_CONST.__cfstring: 0x4ae0
-  __AUTH_CONST.__objc_const: 0xe638
+  __AUTH_CONST.__cfstring: 0x4b60
+  __AUTH_CONST.__objc_const: 0xe698
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1348
+  __AUTH_CONST.__auth_got: 0x1390
   __AUTH.__objc_data: 0x1b80
   __AUTH.__data: 0x310
   __AUTH.__thread_vars: 0x18

   __DATA.__objc_ivar: 0x1b0
   __DATA.__data: 0x27cc
   __DATA.__bss: 0xaa0
-  __DATA_DIRTY.__objc_ivar: 0x5a4
+  __DATA_DIRTY.__objc_ivar: 0x5ac
   __DATA_DIRTY.__objc_data: 0x1090
   __DATA_DIRTY.__bss: 0x538
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3657
-  Symbols:   6662
-  CStrings:  1415
+  Functions: 3664
+  Symbols:   6679
+  CStrings:  1426
 
Symbols:
+ +[HMFHTTPRequestHandler _isValidMethodPredicate:]
+ -[HMFMemoryMonitor setTriggerSuppressionExpiry:]
+ -[HMFMemoryMonitor triggerProcessMemoryWarning]
+ -[HMFMemoryMonitor triggerSuppressionExpiry]
+ -[__HMFNetAddressMonitor _handlePathUpdate:]
+ -[__HMFNetAddressMonitor currentPath]
+ -[__HMFNetAddressMonitor pathEvaluator]
+ -[__HMFNetAddressMonitor pathMonitor]
+ -[__HMFNetAddressMonitor setCurrentPath:]
+ -[__HMFNetAddressMonitor setPathEvaluator:]
+ -[__HMFNetAddressMonitor setPathMonitor:]
+ ___45-[__HMFNetAddressMonitor initWithNetAddress:]_block_invoke
+ ___HMFPathDescription
+ ___block_descriptor_40_e8_32w_e30_v16?0"NSObject<OS_nw_path>"8lw32l8
+ ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
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
+ _objc_msgSend$_isValidMethodPredicate:
+ _objc_msgSend$setTriggerSuppressionExpiry:
+ _objc_msgSend$triggerSuppressionExpiry
+ _sysctlbyname
- +[HMFHTTPRequestHandler _isValidMethodPrediate:]
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
- _objc_msgSend$_isValidMethodPrediate:
- _objc_msgSend$currentNetworkFlags
- _objc_msgSend$handleNetworkReachabilityChange:
- _objc_msgSend$setCurrentNetworkFlags:
CStrings:
+ "0"
+ "Error (%s) sending internal memory pressure event"
+ "Failed to create endpoint for %@"
+ "Failed to create network path monitor"
+ "Failed to create path evaluator for %@"
+ "Received path update: %@"
+ "Success sending internal memory pressure event"
+ "Suppressing observer dispatch for triggered %@"
+ "[%{public}@] Error (%s) sending internal memory pressure event"
+ "[%{public}@] Failed to create endpoint for %@"
+ "[%{public}@] Failed to create network path monitor"
+ "[%{public}@] Failed to create path evaluator for %@"
+ "[%{public}@] Received path update: %@"
+ "[%{public}@] Success sending internal memory pressure event"
+ "[%{public}@] Suppressing observer dispatch for triggered %@"
+ "cellular"
+ "invalid"
+ "kern.memorystatus_vm_pressure_send"
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
- "WWAN"
- "[%{public}@] Failed to create network reachability monitor%@."
- "[%{public}@] Failed to get initial reachability"
- "[%{public}@] Initial flags: %@"
- "[%{public}@] Received notification of updated flags: %@"
- "[%{public}@] Updating reachability to: %@"
- "for %@"
```
