## SessionFoundation

> `/System/Library/PrivateFrameworks/SessionFoundation.framework/SessionFoundation`

```diff

-268.5.9.0.0
-  __TEXT.__text: 0x84f0
-  __TEXT.__auth_stubs: 0x8d0
+304.0.0.0.0
+  __TEXT.__text: 0x87d8
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x780
+  __TEXT.__const: 0x790
   __TEXT.__constg_swiftt: 0x3f8
   __TEXT.__swift5_typeref: 0x2ea
   __TEXT.__swift5_reflstr: 0x168

   __TEXT.__swift5_capture: 0x10c
   __TEXT.__swift5_assocty: 0x88
   __TEXT.__swift5_proto: 0x24
-  __TEXT.__swift_as_entry: 0x10
-  __TEXT.__swift_as_ret: 0x10
+  __TEXT.__swift_as_entry: 0x14
+  __TEXT.__swift_as_ret: 0x14
+  __TEXT.__swift_as_cont: 0xc
   __TEXT.__swift5_protos: 0x8
   __TEXT.__cstring: 0x102
   __TEXT.__oslogstring: 0xf5
-  __TEXT.__unwind_info: 0x340
-  __TEXT.__eh_frame: 0x158
-  __TEXT.__objc_classname: 0xaa
-  __TEXT.__objc_methname: 0x21d
-  __TEXT.__objc_methtype: 0xb4
-  __TEXT.__objc_stubs: 0xc0
-  __DATA_CONST.__got: 0xf8
+  __TEXT.__unwind_info: 0x370
+  __TEXT.__eh_frame: 0x188
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x80
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xd0
   __DATA_CONST.__objc_protorefs: 0x20
-  __AUTH_CONST.__auth_got: 0x470
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x778
   __AUTH_CONST.__objc_const: 0x6a0
-  __AUTH.__objc_data: 0x50
-  __DATA.__data: 0x328
+  __AUTH_CONST.__auth_got: 0x520
+  __DATA.__data: 0x318
   __DATA.__bss: 0x400
-  __DATA_DIRTY.__data: 0x498
+  __DATA_DIRTY.__objc_data: 0x50
+  __DATA_DIRTY.__data: 0x4d0
   __DATA_DIRTY.__bss: 0x80
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 4B82DE1F-C323-3811-BF80-177CAEE61B99
-  Functions: 255
-  Symbols:   281
-  CStrings:  73
+  UUID: 09205894-BEFF-30E1-A87E-6A4FE0A1237E
+  Functions: 262
+  Symbols:   334
+  CStrings:  11
 
Symbols:
+ ___swift__destructor
+ ___swift_allocate_boxed_opaque_existential_0
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.11
+ ___swift_closure_destructor.14
+ ___swift_closure_destructor.18
+ ___swift_closure_destructor.2
+ ___swift_closure_destructor.21
+ ___swift_closure_destructor.21Tm
+ ___swift_closure_destructor.27
+ ___swift_closure_destructor.5
+ ___swift_closure_destructorTm
+ ___swift_project_boxed_opaque_existential_0
+ __swift_implicitisolationactor_to_executor_cast
+ _objc_retain_x20
+ _swift_allocBox
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x27
+ _swift_release_x8
+ _swift_release_x9
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x27
+ _swift_retain_x28
+ _swift_retain_x8
- _objectdestroy.21Tm
- _objectdestroyTm
- _swift_bridgeObjectRelease_n
CStrings:
- "#16@0:8"
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "NSObject"
- "OS_dispatch_source"
- "OS_dispatch_source_signal"
- "OS_os_transaction"
- "Q16@0:8"
- "T#,R"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC17SessionFoundation10UnfairLock"
- "_TtC17SessionFoundation20KeepAliveTransaction"
- "_lock"
- "_lock_buffer"
- "_lock_cancelled"
- "_lock_waiting"
- "activate"
- "autorelease"
- "class"
- "conformsToProtocol:"
- "connectionWithEndpoint:"
- "debugDescription"
- "description"
- "endpointForMachName:service:instance:"
- "hash"
- "invalidate"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "lock"
- "logger"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "publisher"
- "reason"
- "release"
- "remoteTarget"
- "respondsToSelector:"
- "retain"
- "retainCount"
- "self"
- "setDomain:"
- "signalSource"
- "subscription"
- "superclass"
- "transaction"
- "v8@?0"
- "zone"

```
