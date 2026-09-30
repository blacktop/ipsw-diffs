## TrustedClockingServices

> `/System/Library/PrivateFrameworks/TrustedClockingServices.framework/TrustedClockingServices`

```diff

-95.0.0.0.0
-  __TEXT.__text: 0x111b8
-  __TEXT.__objc_methlist: 0x76c
+95.202.0.0.0
+  __TEXT.__text: 0x115b8
+  __TEXT.__objc_methlist: 0x7dc
   __TEXT.__const: 0xb28
-  __TEXT.__gcc_except_tab: 0x4c8
+  __TEXT.__gcc_except_tab: 0x570
   __TEXT.__oslogstring: 0x80c
-  __TEXT.__cstring: 0x1cac
+  __TEXT.__cstring: 0x1dac
   __TEXT.__swift5_typeref: 0x29b
   __TEXT.__swift5_fieldmd: 0x4a0
   __TEXT.__constg_swiftt: 0x684

   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_proto: 0x74
-  __TEXT.__unwind_info: 0xa10
+  __TEXT.__unwind_info: 0xa50
   __TEXT.__eh_frame: 0x690
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2f8
+  __DATA_CONST.__objc_selrefs: 0x348
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__got: 0x150
+  __DATA_CONST.__got: 0x160
   __AUTH_CONST.__const: 0x8d8
-  __AUTH_CONST.__cfstring: 0x360
-  __AUTH_CONST.__objc_const: 0x1bf0
+  __AUTH_CONST.__cfstring: 0x3c0
+  __AUTH_CONST.__objc_const: 0x1c90
   __AUTH_CONST.__weak_auth_got: 0x18
-  __AUTH_CONST.__auth_got: 0x6a0
+  __AUTH_CONST.__auth_got: 0x6b8
   __AUTH.__objc_data: 0x4e8
   __AUTH.__data: 0x7c8
-  __DATA.__objc_ivar: 0x64
+  __DATA.__objc_ivar: 0x74
   __DATA.__data: 0x288
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 610
-  Symbols:   835
-  CStrings:  134
+  Functions: 618
+  Symbols:   864
+  CStrings:  137
 
Symbols:
+ -[TrustedClockingManager beginQoSOverrideWithClass:forUseCaseID:]
+ -[TrustedClockingManager endQoSOverrideForUseCaseID:]
+ -[TrustedClockingManager setThreadsByUseCase:]
+ -[TrustedClockingManager threadsByUseCase]
+ -[TrustedClockingThread beginQoSOverrideWithClass:]
+ -[TrustedClockingThread endActiveQoSOverride]
+ -[TrustedClockingThread endQoSOverride]
+ GCC_except_table17
+ GCC_except_table19
+ GCC_except_table24
+ _OBJC_CLASS_$_NSMutableDictionary
+ _OBJC_CLASS_$_NSNumber
+ _OBJC_IVAR_$_TrustedClockingManager._threadsByUseCase
+ _OBJC_IVAR_$_TrustedClockingThread._activeOverride
+ _OBJC_IVAR_$_TrustedClockingThread._overrideMutex
+ _OBJC_IVAR_$_TrustedClockingThread._threadHandle
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_TrustedClockingThreadProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_TrustedClockingThreadProtocol
+ __ZNK5caulk6thread13native_handleEv
+ _objc_msgSend$beginQoSOverrideWithClass:
+ _objc_msgSend$endActiveQoSOverride
+ _objc_msgSend$endQoSOverride
+ _objc_msgSend$numberWithUnsignedInt:
+ _objc_msgSend$objectForKeyedSubscript:
+ _objc_msgSend$setObject:forKeyedSubscript:
+ _objc_msgSend$setThreadsByUseCase:
+ _objc_msgSend$threadsByUseCase
+ _objc_opt_new
+ _objc_retain_x26
+ _objc_retain_x28
+ _pthread_override_qos_class_end_np
+ _pthread_override_qos_class_start_np
+ _pthread_self
- GCC_except_table20
- _objc_release_x26
- _objc_retain_x22
- _objc_retain_x25
CStrings:
+ "TrustedClockingManager: No thread registered for useCaseID %u, cannot begin QoS override"
+ "TrustedClockingManager: No thread registered for useCaseID %u, ignoring endQoSOverride"
+ "TrustedClockingThread::beginQoSOverrideWithClass: Failed to start override for qosClass %u"
+ "\x97"
- "\x96"
```
