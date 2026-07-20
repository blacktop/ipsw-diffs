## TrustedClockingServices

> `/System/Library/PrivateFrameworks/TrustedClockingServices.framework/TrustedClockingServices`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH.__data`
- `__DATA.__data`

```diff

-93.1.0.0.0
-  __TEXT.__text: 0x11268
-  __TEXT.__objc_methlist: 0x73c
-  __TEXT.__const: 0xaf8
-  __TEXT.__gcc_except_tab: 0x488
+95.0.0.0.0
+  __TEXT.__text: 0x11688
+  __TEXT.__objc_methlist: 0x76c
+  __TEXT.__const: 0xb28
+  __TEXT.__gcc_except_tab: 0x4c8
   __TEXT.__oslogstring: 0x80c
-  __TEXT.__cstring: 0x1c2c
+  __TEXT.__cstring: 0x1cac
   __TEXT.__swift5_typeref: 0x29b
   __TEXT.__swift5_fieldmd: 0x4a0
   __TEXT.__constg_swiftt: 0x684

   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_proto: 0x74
-  __TEXT.__unwind_info: 0x740
+  __TEXT.__unwind_info: 0x768
   __TEXT.__eh_frame: 0x688
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x480
-  __DATA_CONST.__objc_classlist: 0xb0
+  __DATA_CONST.__const: 0x510
+  __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e0
+  __DATA_CONST.__objc_selrefs: 0x2f8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__got: 0x150
   __AUTH_CONST.__const: 0x8d8
-  __AUTH_CONST.__cfstring: 0x320
-  __AUTH_CONST.__objc_const: 0x1b60
+  __AUTH_CONST.__cfstring: 0x360
+  __AUTH_CONST.__objc_const: 0x1bf0
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__auth_got: 0x690
-  __AUTH.__objc_data: 0x498
+  __AUTH_CONST.__auth_got: 0x6a0
+  __AUTH.__objc_data: 0x4e8
   __AUTH.__data: 0x7c8
   __DATA.__objc_ivar: 0x64
   __DATA.__data: 0x288

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 605
-  Symbols:   813
-  CStrings:  132
+  Functions: 610
+  Symbols:   835
+  CStrings:  134
 
Symbols:
+ +[TrustedClockingThreadPriorityResolver specForThreadConfig:routingConfig:]
+ -[TrustedClockingManager createThreadForUseCaseID:]
+ -[TrustedClockingThread .cxx_construct]
+ -[TrustedClockingThread .cxx_destruct]
+ -[TrustedClockingThread initWithWorkload:attributes:]
+ -[TrustedClockingThread initWithWorkload:qosClass:]
+ -[TrustedClockingThread initWithWorkload:realtimeConstraints:]
+ -[TrustedClockingThreadFactory createThreadForUseCaseID:workload:]
+ GCC_except_table13
+ GCC_except_table20
+ _OBJC_CLASS_$_TrustedClockingThread
+ _OBJC_CLASS_$_TrustedClockingThreadPriorityResolver
+ _OBJC_IVAR_$_TrustedClockingThread._thread
+ _OBJC_IVAR_$_TrustedClockingThread._workload
+ _OBJC_METACLASS_$_TrustedClockingThread
+ _OBJC_METACLASS_$_TrustedClockingThreadPriorityResolver
+ __OBJC_$_CLASS_METHODS_TrustedClockingThreadPriorityResolver
+ __OBJC_$_INSTANCE_METHODS_TrustedClockingThread
+ __OBJC_$_INSTANCE_VARIABLES_TrustedClockingThread
+ __OBJC_$_PROP_LIST_TrustedClockingThread
+ __OBJC_$_PROTOCOL_REFS_TrustedClockingThreadProtocol
+ __OBJC_CLASS_PROTOCOLS_$_TrustedClockingThread
+ __OBJC_CLASS_RO_$_TrustedClockingThread
+ __OBJC_CLASS_RO_$_TrustedClockingThreadPriorityResolver
+ __OBJC_LABEL_PROTOCOL_$_TrustedClockingThreadProtocol
+ __OBJC_METACLASS_RO_$_TrustedClockingThread
+ __OBJC_METACLASS_RO_$_TrustedClockingThreadPriorityResolver
+ __OBJC_PROTOCOL_$_TrustedClockingThreadProtocol
+ __ZL14kThreadConfigs
+ __ZL15kRoutingConfigs
+ __ZL24kRoutingDevices_MockTest
+ __ZL27kRoutingDevices_ConvCapture
+ __ZL27kRoutingDevices_Siri2ndPass
+ __ZN5caulk12thread_proxyINSt3__15tupleIJNS_6thread10attributesEZ53-[TrustedClockingThread initWithWorkload:attributes:]E3$_0NS2_IJEEEEEEEEPvS8_
+ __ZNSt18bad_variant_accessD1Ev
+ __ZNSt3__110unique_ptrINS_5tupleIJN5caulk6thread10attributesEZ53-[TrustedClockingThread initWithWorkload:attributes:]E3$_0NS1_IJEEEEEENS_14default_deleteIS7_EEED1B9fqe220106Ev
+ __ZNSt3__126__throw_bad_variant_accessB9fqe220106Ev
+ __ZNSt3__18optionalINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEaSB9fqe220106IRA38_KcLi0EEERS7_OT_
+ __ZNSt9exceptionD2Ev
+ __ZTISt18bad_variant_access
+ __ZTVSt18bad_variant_access
+ ___51-[TrustedClockingManager createThreadForUseCaseID:]_block_invoke
+ _objc_msgSend$createThreadForUseCaseID:
+ _objc_msgSend$createThreadForUseCaseID:workload:
+ _objc_msgSend$initWithWorkload:attributes:
+ _objc_msgSend$initWithWorkload:qosClass:
+ _objc_msgSend$specForThreadConfig:routingConfig:
+ _objc_retain_x21
+ _objc_retain_x3
- -[TrustedClockingManager createRealtimeThread:sampleRate:useCaseID:]
- -[TrustedClockingRealtimeThread .cxx_construct]
- -[TrustedClockingRealtimeThread .cxx_destruct]
- -[TrustedClockingRealtimeThread initWithWorkload:realtimeConstraints:]
- -[TrustedClockingThreadFactory createRealtimeThread:frameSize:workload:]
- GCC_except_table16
- GCC_except_table18
- _OBJC_CLASS_$_TrustedClockingRealtimeThread
- _OBJC_IVAR_$_TrustedClockingRealtimeThread._thread
- _OBJC_IVAR_$_TrustedClockingRealtimeThread._workload
- _OBJC_METACLASS_$_TrustedClockingRealtimeThread
- __OBJC_$_INSTANCE_METHODS_TrustedClockingRealtimeThread
- __OBJC_$_INSTANCE_VARIABLES_TrustedClockingRealtimeThread
- __OBJC_$_PROP_LIST_TrustedClockingRealtimeThread
- __OBJC_$_PROTOCOL_REFS_TrustedClockingRealtimeThreadProtocol
- __OBJC_CLASS_PROTOCOLS_$_TrustedClockingRealtimeThread
- __OBJC_CLASS_RO_$_TrustedClockingRealtimeThread
- __OBJC_LABEL_PROTOCOL_$_TrustedClockingRealtimeThreadProtocol
- __OBJC_METACLASS_RO_$_TrustedClockingRealtimeThread
- __OBJC_PROTOCOL_$_TrustedClockingRealtimeThreadProtocol
- __ZN5caulk12thread_proxyINSt3__15tupleIJNS_6thread10attributesEZ70-[TrustedClockingRealtimeThread initWithWorkload:realtimeConstraints:]E3$_0NS2_IJEEEEEEEEPvS8_
- __ZNSt3__110unique_ptrINS_5tupleIJN5caulk6thread10attributesEZ70-[TrustedClockingRealtimeThread initWithWorkload:realtimeConstraints:]E3$_0NS1_IJEEEEEENS_14default_deleteIS7_EEED1B9fqe220106Ev
- __ZNSt3__18optionalINS_12basic_stringIcNS_11char_traitsIcEENS_9allocatorIcEEEEEaSB9fqe220106IRA27_KcLi0EEERS7_OT_
- ___68-[TrustedClockingManager createRealtimeThread:sampleRate:useCaseID:]_block_invoke
- _objc_msgSend$createRealtimeThread:frameSize:workload:
- _objc_msgSend$createRealtimeThread:sampleRate:useCaseID:
- _objc_retain_x4
CStrings:
+ "TrustedClockingThread::initWithWorkload: Exception: %s"
+ "TrustedClockingThreadFactory: No config found for useCaseID %u"
+ "TrustedClockingThreadFactory: useCaseID %u -> qos class %u"
+ "TrustedClockingThreadFactory: useCaseID %u -> realtime period=%u quantum=%u constraint=%u"
+ "com.apple.trustedclocking.audiothread"
- "TrustedClockingRealtimeThread::initWithWorkload: Exception: %s"
- "TrustedClockingRealtimeThread::initWithWorkload: Launching trusted clocking real time thread."
- "trusted_clocking_rt_thread"
```
