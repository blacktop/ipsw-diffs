## HMFoundation

> `/System/Library/PrivateFrameworks/HMFoundation.framework/HMFoundation`

```diff

-875.0.0.0.0
-  __TEXT.__text: 0x83ac0
+880.0.0.0.0
+  __TEXT.__text: 0x83ff4
   __TEXT.__auth_stubs: 0x20e0
-  __TEXT.__objc_methlist: 0x75cc
-  __TEXT.__const: 0x25c8
+  __TEXT.__objc_methlist: 0x7644
+  __TEXT.__const: 0x25d8
   __TEXT.__dlopen_cstrs: 0xf8
-  __TEXT.__cstring: 0x3163
-  __TEXT.__swift5_typeref: 0x9d3
+  __TEXT.__cstring: 0x3181
+  __TEXT.__swift5_typeref: 0x9d5
   __TEXT.__swift5_capture: 0x5f0
   __TEXT.__swift_as_entry: 0x168
   __TEXT.__swift_as_ret: 0x194

   __TEXT.__swift5_reflstr: 0x367
   __TEXT.__swift5_fieldmd: 0x670
   __TEXT.__swift5_types: 0x9c
-  __TEXT.__swift5_proto: 0x3c
+  __TEXT.__oslogstring: 0x418e
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__oslogstring: 0x4108
+  __TEXT.__swift5_proto: 0x3c
   __TEXT.__swift5_assocty: 0x18
-  __TEXT.__gcc_except_tab: 0x1b6c
+  __TEXT.__gcc_except_tab: 0x1c00
   __TEXT.__ustring: 0x8
-  __TEXT.__unwind_info: 0x2d60
-  __TEXT.__eh_frame: 0x2e5c
-  __TEXT.__objc_classname: 0x10cb
-  __TEXT.__objc_methname: 0xc0d3
-  __TEXT.__objc_methtype: 0x26ca
-  __TEXT.__objc_stubs: 0x8a80
-  __DATA_CONST.__got: 0x7e8
-  __DATA_CONST.__const: 0x1558
+  __TEXT.__unwind_info: 0x2da8
+  __TEXT.__eh_frame: 0x2e60
+  __TEXT.__objc_classname: 0x10e0
+  __TEXT.__objc_methname: 0xc230
+  __TEXT.__objc_methtype: 0x26df
+  __TEXT.__objc_stubs: 0x8b00
+  __DATA_CONST.__got: 0x7e0
+  __DATA_CONST.__const: 0x1560
   __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0xa0
-  __DATA_CONST.__objc_protolist: 0x1a8
+  __DATA_CONST.__objc_protolist: 0x1b0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ed8
+  __DATA_CONST.__objc_selrefs: 0x2f10
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x380
+  __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x1080
   __AUTH_CONST.__const: 0x1f90
   __AUTH_CONST.__cfstring: 0x4cc0
-  __AUTH_CONST.__objc_const: 0xe218
+  __AUTH_CONST.__objc_const: 0xe280
+  __AUTH_CONST.__objc_intobj: 0x60
+  __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x1130
   __AUTH.__data: 0x150
   __AUTH.__thread_vars: 0x18
   __AUTH.__thread_bss: 0x8
   __DATA.__objc_ivar: 0x198
-  __DATA.__data: 0x23a0
+  __DATA.__data: 0x2400
   __DATA.__bss: 0x514
-  __DATA_DIRTY.__objc_ivar: 0x5a8
+  __DATA_DIRTY.__objc_ivar: 0x5ac
   __DATA_DIRTY.__objc_data: 0x19f0
   __DATA_DIRTY.__bss: 0x538
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: E8E8A068-6E8F-3DB3-B707-BFA137EE2F38
-  Functions: 3356
-  Symbols:   9143
-  CStrings:  4530
+  UUID: 047BFAD4-0E3D-3977-ACCB-95017013E4B1
+  Functions: 3365
+  Symbols:   9168
+  CStrings:  4545
 
Symbols:
+ -[HMFMessageDispatcher _configureMemoryPressureHandler]
+ -[HMFMessageDispatcher didRegisterWithMemoryMonitor]
+ -[HMFMessageDispatcher makeSureToRegisterWithMemoryMonitor]
+ -[HMFMessageDispatcher memoryMonitor:didReceiveMemoryEvent:]
+ -[HMFMessageDispatcher setDidRegisterWithMemoryMonitor:]
+ -[HMFMessageDispatcher setMsgBindingsCache:]
+ -[HMFMessageDispatcher setReceiverCache:]
+ -[NSError(HMFError) hmfAggregatedErrors]
+ GCC_except_table30
+ _OBJC_CLASS_$_NSConstantArray
+ _OBJC_CLASS_$_NSConstantIntegerNumber
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_HMFMemoryObserver
+ __OBJC_$_PROTOCOL_METHOD_TYPES_HMFMemoryObserver
+ __OBJC_$_PROTOCOL_REFS_HMFMemoryObserver
+ __OBJC_LABEL_PROTOCOL_$_HMFMemoryObserver
+ __OBJC_PROTOCOL_$_HMFMemoryObserver
+ ___61-[HMFMessageDispatcher messageBindingForReceiver:forMessage:]_block_invoke
+ ___block_descriptor_40_e8_32s_e27_B16?0"HMFMessageBinding"8ls32l8
+ _objc_msgSend$_configureMemoryPressureHandler
+ _objc_msgSend$addObserver:debounceInterval:events:
+ _objc_msgSend$isHMFError
+ _objc_msgSend$makeSureToRegisterWithMemoryMonitor
+ _objc_msgSend$memoryMonitor
- _OBJC_CLASS_$_NSCache
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_HMFoundation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_HMFoundation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_HMFoundation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_HMFoundation
- _objc_msgSend$msgBindingsCache
CStrings:
+ "%{public}@Clearing cache after receiving memory pressure notification: [receiverCache: %@], [msgBindingCache: %@]"
+ "%{public}@[NewFlow: %@ {\"Feature\":\"Error\"}] Incorrect Flow Usage: Expected, but did not find, flow for message: %@"
+ "B16@?0@\"HMFMessageBinding\"8"
+ "HMFMemoryObserver"
+ "T@\"<HMFMessageReceiver>\",R,W,N,V_messageReceiver"
+ "T@\"NSMapTable\",&,N,V_msgBindingsCache"
+ "T@\"NSMapTable\",&,N,V_receiverCache"
+ "T@\"NSObject<OS_dispatch_queue>\",R,&"
+ "T@\"NSObject<OS_dispatch_queue>\",R,&,N,V_workQueue"
+ "T@\"NSObject<OS_dispatch_queue>\",R,&,V_workQueue"
+ "TB,V_didRegisterWithMemoryMonitor"
+ "_configureMemoryPressureHandler"
+ "_didRegisterWithMemoryMonitor"
+ "didRegisterWithMemoryMonitor"
+ "hmfAggregatedErrors"
+ "makeSureToRegisterWithMemoryMonitor"
+ "setDidRegisterWithMemoryMonitor:"
+ "setMsgBindingsCache:"
+ "setReceiverCache:"
+ "v32@0:8@\"HMFMemoryMonitor\"16q24"
- "%{public}@[NewFlow: %@] Incorrect Flow Usage: Expected, but did not find, flow for message: %@"
- "@\"NSCache\""
- "T@\"<HMFMessageReceiver>\",R,N,V_messageReceiver"
- "T@\"NSCache\",R,N,V_msgBindingsCache"
- "T@\"NSCache\",R,N,V_receiverCache"
- "T@\"NSObject<OS_dispatch_queue>\",R,V_workQueue"

```
