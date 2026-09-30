## ContactsFoundation

> `/System/Library/PrivateFrameworks/ContactsFoundation.framework/ContactsFoundation`

```diff

-1387.100.3.0.0
-  __TEXT.__text: 0x87e98
-  __TEXT.__auth_stubs: 0x1b60
-  __TEXT.__objc_methlist: 0xa80c
-  __TEXT.__cstring: 0x70d8
-  __TEXT.__const: 0x6d8
-  __TEXT.__oslogstring: 0x248b
+1390.100.1.0.0
+  __TEXT.__text: 0x89c0c
+  __TEXT.__auth_stubs: 0x1c20
+  __TEXT.__objc_methlist: 0xa8bc
+  __TEXT.__cstring: 0x7264
+  __TEXT.__const: 0x6e4
+  __TEXT.__oslogstring: 0x24c8
   __TEXT.__gcc_except_tab: 0x1254
   __TEXT.__ustring: 0x2e2
   __TEXT.__dlopen_cstrs: 0x167
-  __TEXT.__swift5_typeref: 0x2e8
+  __TEXT.__swift5_typeref: 0x35c
   __TEXT.__constg_swiftt: 0x350
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8

   __TEXT.__swift5_fieldmd: 0x1dc
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x2c
-  __TEXT.__swift5_capture: 0x90
+  __TEXT.__swift5_capture: 0x104
   __TEXT.__swift_as_entry: 0x28
   __TEXT.__swift_as_ret: 0x2c
-  __TEXT.__unwind_info: 0x33d8
+  __TEXT.__unwind_info: 0x3450
   __TEXT.__eh_frame: 0x508
-  __TEXT.__objc_classname: 0x2549
-  __TEXT.__objc_methname: 0x12c80
-  __TEXT.__objc_methtype: 0x2f7d
-  __TEXT.__objc_stubs: 0xd6a0
-  __DATA_CONST.__got: 0xdd8
-  __DATA_CONST.__const: 0x3808
-  __DATA_CONST.__objc_classlist: 0xa68
+  __TEXT.__objc_classname: 0x254b
+  __TEXT.__objc_methname: 0x12d48
+  __TEXT.__objc_methtype: 0x2f81
+  __TEXT.__objc_stubs: 0xd6e0
+  __DATA_CONST.__got: 0xde8
+  __DATA_CONST.__const: 0x37f0
+  __DATA_CONST.__objc_classlist: 0xa70
   __DATA_CONST.__objc_catlist: 0x98
-  __DATA_CONST.__objc_protolist: 0x1e8
+  __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4af8
-  __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__objc_selrefs: 0x4b18
+  __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x568
   __DATA_CONST.__objc_arraydata: 0x9c90
-  __AUTH_CONST.__auth_got: 0xdc0
-  __AUTH_CONST.__const: 0x2228
-  __AUTH_CONST.__cfstring: 0xad60
-  __AUTH_CONST.__objc_const: 0x15c58
+  __AUTH_CONST.__auth_got: 0xe20
+  __AUTH_CONST.__const: 0x2608
+  __AUTH_CONST.__cfstring: 0xada0
+  __AUTH_CONST.__objc_const: 0x15d48
   __AUTH_CONST.__objc_dictobj: 0x2580
   __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH_CONST.__objc_arrayobj: 0x60
-  __AUTH.__objc_data: 0x35a0
-  __AUTH.__data: 0x178
-  __DATA.__objc_ivar: 0x7f4
-  __DATA.__data: 0x1908
+  __AUTH.__objc_data: 0x3610
+  __AUTH.__data: 0x1b0
+  __DATA.__objc_ivar: 0x7f8
+  __DATA.__data: 0x1980
   __DATA.__bss: 0x670
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x3520

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 0AEA9C53-1310-3D75-A8A7-C6B47CF24B4D
-  Functions: 4628
-  Symbols:   15333
-  CStrings:  7294
+  UUID: 5D612152-727C-32E4-B9B1-AA75890F67FD
+  Functions: 4709
+  Symbols:   15439
+  CStrings:  7320
 
Symbols:
+ +[CNScheduler serialWorkloopSchedulerWithName:]
+ -[CNSchedulerProvider initWithBackgroundScheduler:mainThreadScheduler:inlineScheduler:immediateScheduler:serialSchedulerProvider:workloopSchedulerProvider:synchronousSerialSchedulerProvider:readerWriterSchedulerProvider:]
+ -[CNSchedulerProvider newWorkloopSchedulerWithName:]
+ -[CNSchedulerProvider workloopSchedulerProvider]
+ _OBJC_CLASS_$_CNRoundRobinScheduler
+ _OBJC_IVAR_$_CNSchedulerProvider._backgroundScheduler
+ _OBJC_IVAR_$_CNSchedulerProvider._immediateScheduler
+ _OBJC_IVAR_$_CNSchedulerProvider._inlineScheduler
+ _OBJC_IVAR_$_CNSchedulerProvider._mainThreadScheduler
+ _OBJC_IVAR_$_CNSchedulerProvider._readerWriterSchedulerProvider
+ _OBJC_IVAR_$_CNSchedulerProvider._serialSchedulerProvider
+ _OBJC_IVAR_$_CNSchedulerProvider._synchronousSerialSchedulerProvider
+ _OBJC_IVAR_$_CNSchedulerProvider._workloopSchedulerProvider
+ _OBJC_METACLASS_$_CNRoundRobinScheduler
+ __DATA_CNRoundRobinScheduler
+ __INSTANCE_METHODS_CNRoundRobinScheduler
+ __IVARS_CNRoundRobinScheduler
+ __METACLASS_DATA_CNRoundRobinScheduler
+ __OBJC_$_PROP_LIST_CNSchedulerProvider.114
+ __PROPERTIES_CNRoundRobinScheduler
+ __PROTOCOLS_CNRoundRobinScheduler
+ __PROTOCOLS_CNRoundRobinScheduler.17
+ _block_copy_helper.10
+ _block_copy_helper.13
+ _block_copy_helper.18
+ _block_copy_helper.25
+ _block_copy_helper.31
+ _block_copy_helper.38
+ _block_copy_helper.4
+ _block_copy_helper.45
+ _block_copy_helper.52
+ _block_copy_helper.7
+ _block_descriptor.12
+ _block_descriptor.15
+ _block_descriptor.20
+ _block_descriptor.27
+ _block_descriptor.33
+ _block_descriptor.40
+ _block_descriptor.47
+ _block_descriptor.54
+ _block_descriptor.6
+ _block_descriptor.9
+ _block_destroy_helper.11
+ _block_destroy_helper.14
+ _block_destroy_helper.19
+ _block_destroy_helper.26
+ _block_destroy_helper.32
+ _block_destroy_helper.39
+ _block_destroy_helper.46
+ _block_destroy_helper.5
+ _block_destroy_helper.53
+ _block_destroy_helper.8
+ _dispatch_workloop_create
+ _flat unique So11CNScheduler_p
+ _objc_msgSend$initWithBackgroundScheduler:mainThreadScheduler:inlineScheduler:immediateScheduler:serialSchedulerProvider:workloopSchedulerProvider:synchronousSerialSchedulerProvider:readerWriterSchedulerProvider:
+ _objc_msgSend$serialWorkloopSchedulerWithName:
+ _objc_msgSend$workloopSchedulerProvider
+ _sReaderWriterSchedulerProvider_block_invoke_4
+ _sSerialWorkloopSchedulerProvider_block_invoke_2
+ _sSynchronousSerialDispatchQueueSchedulerProvider_block_invoke_3
+ _swift_getObjCClassFromMetadata
+ _symbolic IeyB_
+ _symbolic So18CNCancelationTokenC
+ _symbolic So18CNCancelationTokenCIegg_
+ _symbolic So18CNCancelationTokenCIeyBy_
+ _symbolic ______p So11CNSchedulerP
- -[CNSchedulerProvider initWithBackgroundScheduler:mainThreadScheduler:inlineScheduler:immediateScheduler:serialSchedulerProvider:synchronousSerialSchedulerProvider:readerWriterSchedulerProvider:]
- OBJC_IVAR_$_CNSchedulerProvider._backgroundScheduler
- OBJC_IVAR_$_CNSchedulerProvider._immediateScheduler
- OBJC_IVAR_$_CNSchedulerProvider._inlineScheduler
- OBJC_IVAR_$_CNSchedulerProvider._mainThreadScheduler
- OBJC_IVAR_$_CNSchedulerProvider._readerWriterSchedulerProvider
- OBJC_IVAR_$_CNSchedulerProvider._serialSchedulerProvider
- OBJC_IVAR_$_CNSchedulerProvider._synchronousSerialSchedulerProvider
- __OBJC_$_PROP_LIST_CNSchedulerProvider.107
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_ContactsFoundation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_ContactsFoundation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_ContactsFoundation
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_ContactsFoundation
- _objc_msgSend$initWithBackgroundScheduler:mainThreadScheduler:inlineScheduler:immediateScheduler:serialSchedulerProvider:synchronousSerialSchedulerProvider:readerWriterSchedulerProvider:
- _sReaderWriterSchedulerProvider_block_invoke_3
- _sSynchronousSerialDispatchQueueSchedulerProvider_block_invoke_2
CStrings:
+ "@80@0:8@16@24@32@40@?48@?56@?64@?72"
+ "API Service Workloop Scheduling"
+ "CNRoundRobinScheduler"
+ "ContactsFoundation/RoundRobinScheduler.swift"
+ "Fatal error"
+ "RoundRobinScheduler"
+ "Selected scheduler at index %ld with %ld pending blocks"
+ "T@?,R,C,N,V_workloopSchedulerProvider"
+ "Td,N,R"
+ "Tq,R,N,V_activeBlockCount"
+ "Tq,R,N,V_completedBlockCount"
+ "Tq,R,N,V_pendingBlockCount"
+ "Use init(schedulers:) instead"
+ "_workloopSchedulerProvider"
+ "api_service_workloop_scheduling"
+ "https?://(?:www\\.)?(x\\.com)/(?:#!/)?([%\\w\\d]+)/?$"
+ "initWithBackgroundScheduler:mainThreadScheduler:inlineScheduler:immediateScheduler:serialSchedulerProvider:workloopSchedulerProvider:synchronousSerialSchedulerProvider:readerWriterSchedulerProvider:"
+ "initWithSchedulers:"
+ "newWorkloopSchedulerWithName:"
+ "schedulers"
+ "serialWorkloopSchedulerWithName:"
+ "workloopSchedulerProvider"
- "@72@0:8@16@24@32@40@?48@?56@?64"
- "TQ,R,N,V_activeBlockCount"
- "TQ,R,N,V_completedBlockCount"
- "TQ,R,N,V_pendingBlockCount"
- "initWithBackgroundScheduler:mainThreadScheduler:inlineScheduler:immediateScheduler:serialSchedulerProvider:synchronousSerialSchedulerProvider:readerWriterSchedulerProvider:"

```
