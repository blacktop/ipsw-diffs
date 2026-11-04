## HMFoundation

> `/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation`

```diff

-1520.2.7.1.3
-  __TEXT.__text: 0x9a9e8
+1535.0.0.0.2
+  __TEXT.__text: 0x9b740
   __TEXT.__delay_stubs: 0x400
   __TEXT.__delay_helper: 0x294
-  __TEXT.__objc_methlist: 0x79dc
-  __TEXT.__const: 0x33f0
+  __TEXT.__objc_methlist: 0x7b34
+  __TEXT.__const: 0x3460
   __TEXT.__dlopen_cstrs: 0xf8
-  __TEXT.__cstring: 0x3235
-  __TEXT.__swift5_typeref: 0xc7a
+  __TEXT.__cstring: 0x324b
+  __TEXT.__swift5_typeref: 0xc78
   __TEXT.__swift5_capture: 0x6b4
   __TEXT.__swift_as_entry: 0x1cc
   __TEXT.__swift_as_ret: 0x1f8
   __TEXT.__swift_as_cont: 0x274
   __TEXT.__constg_swiftt: 0xf5c
-  __TEXT.__swift5_reflstr: 0x48a
+  __TEXT.__swift5_reflstr: 0x47a
   __TEXT.__swift5_fieldmd: 0x890
   __TEXT.__swift5_types: 0xc8
   __TEXT.__swift5_proto: 0x7c
   __TEXT.__swift5_protos: 0x20
-  __TEXT.__oslogstring: 0x8107
+  __TEXT.__oslogstring: 0x80c2
   __TEXT.__swift5_assocty: 0x88
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__gcc_except_tab: 0x1a9c
+  __TEXT.__gcc_except_tab: 0x1b68
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x3cb8
+  __TEXT.__unwind_info: 0x3d48
   __TEXT.__eh_frame: 0x3a40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1668
-  __DATA_CONST.__objc_classlist: 0x478
-  __DATA_CONST.__objc_catlist: 0xa8
-  __DATA_CONST.__objc_protolist: 0x1d8
+  __DATA_CONST.__const: 0x1640
+  __DATA_CONST.__objc_classlist: 0x480
+  __DATA_CONST.__objc_catlist: 0xb0
+  __DATA_CONST.__objc_protolist: 0x1e0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3160
+  __DATA_CONST.__objc_selrefs: 0x31a8
   __DATA_CONST.__objc_protorefs: 0x40
-  __DATA_CONST.__objc_superrefs: 0x388
+  __DATA_CONST.__objc_superrefs: 0x390
   __DATA_CONST.__objc_arraydata: 0x20
-  __DATA_CONST.__got: 0x858
-  __AUTH_CONST.__const: 0x26d0
-  __AUTH_CONST.__cfstring: 0x4ba0
-  __AUTH_CONST.__objc_const: 0xe6e0
+  __DATA_CONST.__got: 0x860
+  __AUTH_CONST.__const: 0x2710
+  __AUTH_CONST.__cfstring: 0x4bc0
+  __AUTH_CONST.__objc_const: 0xe990
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x1468
-  __AUTH.__objc_data: 0x1b80
+  __AUTH_CONST.__auth_got: 0x1470
+  __AUTH.__objc_data: 0x1bd0
   __AUTH.__data: 0x310
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0x1b0
-  __DATA.__data: 0x29d4
-  __DATA_DIRTY.__objc_ivar: 0x5ac
+  __DATA.__data: 0x2a2c
+  __DATA_DIRTY.__objc_ivar: 0x5bc
   __DATA_DIRTY.__objc_data: 0x1090
   __DATA_DIRTY.__bss: 0x538
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3817
-  Symbols:   5556
-  CStrings:  1431
+  Functions: 3846
+  Symbols:   5610
+  CStrings:  1430
 
Symbols:
+ +[HMFNetMonitor monitorWithNetAddress:queue:]
+ +[HMFSystemDefaultNetworkPathMonitor logCategory]
+ +[HMFSystemDefaultNetworkPathMonitor shared]
+ -[HMFNetMonitor _notifyReachabilityDidChange:]
+ -[HMFScheduler initWithOperationQueue:]
+ -[HMFScheduler operationQueue]
+ -[HMFSystemDefaultNetworkPathMonitor .cxx_destruct]
+ -[HMFSystemDefaultNetworkPathMonitor _applyInitialPath:]
+ -[HMFSystemDefaultNetworkPathMonitor _handlePathUpdate:]
+ -[HMFSystemDefaultNetworkPathMonitor _notifyReachabilityDidChange:]
+ -[HMFSystemDefaultNetworkPathMonitor addObserver:]
+ -[HMFSystemDefaultNetworkPathMonitor currentPath]
+ -[HMFSystemDefaultNetworkPathMonitor dealloc]
+ -[HMFSystemDefaultNetworkPathMonitor initWithQueue:]
+ -[HMFSystemDefaultNetworkPathMonitor logIdentifier]
+ -[HMFSystemDefaultNetworkPathMonitor observers]
+ -[HMFSystemDefaultNetworkPathMonitor pathMonitor]
+ -[HMFSystemDefaultNetworkPathMonitor queue]
+ -[HMFSystemDefaultNetworkPathMonitor reachabilityPath]
+ -[HMFSystemDefaultNetworkPathMonitor removeObserver:]
+ -[HMFSystemDefaultNetworkPathMonitor setCurrentPath:]
+ -[__HMFNetAddressMonitor _applyInitialPath:]
+ -[__HMFNetAddressMonitor initWithNetAddress:queue:]
+ -[__HMFNetAddressMonitor queue]
+ _HMFProductInfoEclipseCOSVersion
+ _HMFProductInfoFizzCOSVersion
+ _HMFProductInfoLotusCOSVersion
+ _HMFProductInfoOrchidCOSVersion
+ _HMFProductInfoRaveCOSVersion
+ _OBJC_CLASS_$_HMFSystemDefaultNetworkPathMonitor
+ _OBJC_METACLASS_$_HMFSystemDefaultNetworkPathMonitor
+ __OBJC_$_CATEGORY_NSOperation_$_HMFScheduler
+ __OBJC_$_CLASS_METHODS_HMFSystemDefaultNetworkPathMonitor
+ __OBJC_$_CLASS_PROP_LIST_HMFSystemDefaultNetworkPathMonitor
+ __OBJC_$_INSTANCE_METHODS_HMFSystemDefaultNetworkPathMonitor
+ __OBJC_$_INSTANCE_VARIABLES_HMFSystemDefaultNetworkPathMonitor
+ __OBJC_$_PROP_LIST_HMFNetworkPathMonitoring
+ __OBJC_$_PROP_LIST_HMFScheduler
+ __OBJC_$_PROP_LIST_HMFSystemDefaultNetworkPathMonitor
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMFNetworkPathMonitoring
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMFNetworkPathMonitoring
+ __OBJC_$_PROTOCOL_REFS_HMFNetworkPathMonitoring
+ __OBJC_CATEGORY_PROTOCOLS_$_NSOperation_$_HMFScheduler
+ __OBJC_CLASS_PROTOCOLS_$_HMFSystemDefaultNetworkPathMonitor
+ __OBJC_CLASS_RO_$_HMFSystemDefaultNetworkPathMonitor
+ __OBJC_LABEL_PROTOCOL_$_HMFNetworkPathMonitoring
+ __OBJC_METACLASS_RO_$_HMFSystemDefaultNetworkPathMonitor
+ __OBJC_PROTOCOL_$_HMFNetworkPathMonitoring
+ ___44+[HMFSystemDefaultNetworkPathMonitor shared]_block_invoke
+ ___49+[HMFSystemDefaultNetworkPathMonitor logCategory]_block_invoke
+ ___51-[__HMFNetAddressMonitor initWithNetAddress:queue:]_block_invoke
+ ___52-[HMFSystemDefaultNetworkPathMonitor initWithQueue:]_block_invoke
+ ___HMFNetMonitorNotify
+ ___HMFNetPathCopyDefault
+ ___HMFNetPathMonitorCreate
+ ___HMFNetPathReachabilityPath
+ _dispatch_queue_create_with_target$V2
+ _nw_path_create_default_evaluator
- -[HMFScheduler initWithQueue:]
- ___45-[__HMFNetAddressMonitor initWithNetAddress:]_block_invoke
- ___block_descriptor_48_e8_32s40w_e5_v8?0lw40l8s32l8
- _inet_ntoa
CStrings:
+ "[%{public}@] inet_ntop() failed with '%s' (%d) for sockaddr_in: %@"
+ "defaultPathNetMonitor"
+ "inet_ntop() failed with '%s' (%d) for sockaddr_in: %@"
- "Notifying delegate address is reachable"
- "Notifying delegate address is unreachable"
- "[%{public}@] Notifying delegate address is reachable"
- "[%{public}@] Notifying delegate address is unreachable"
```
