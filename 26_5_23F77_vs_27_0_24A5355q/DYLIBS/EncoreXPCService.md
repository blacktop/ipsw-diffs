## EncoreXPCService

> `/System/Library/PrivateFrameworks/EncoreXPCService.framework/EncoreXPCService`

```diff

-3525.4.4.0.0
-  __TEXT.__text: 0xfd84
-  __TEXT.__auth_stubs: 0xc00
+3600.22.4.0.0
+  __TEXT.__text: 0xfe64
   __TEXT.__objc_methlist: 0x350
   __TEXT.__const: 0x860
+  __TEXT.__cstring: 0x1d6
   __TEXT.__oslogstring: 0x698
   __TEXT.__constg_swiftt: 0x450
   __TEXT.__swift5_typeref: 0x4d2
   __TEXT.__swift5_reflstr: 0x16e
   __TEXT.__swift5_fieldmd: 0x21c
   __TEXT.__swift5_types: 0x2c
-  __TEXT.__cstring: 0x1c6
   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_proto: 0x50
   __TEXT.__swift5_capture: 0xfc
   __TEXT.__swift_as_entry: 0xc
   __TEXT.__swift_as_ret: 0x10
+  __TEXT.__swift_as_cont: 0x28
   __TEXT.__swift5_protos: 0x4
   __TEXT.__unwind_info: 0x4b0
-  __TEXT.__eh_frame: 0x3a8
-  __TEXT.__objc_classname: 0x167
-  __TEXT.__objc_methname: 0x616
-  __TEXT.__objc_methtype: 0x267
-  __TEXT.__objc_stubs: 0x320
-  __DATA_CONST.__got: 0x160
+  __TEXT.__eh_frame: 0x3e0
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xc0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__objc_selrefs: 0x1b0
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x8
-  __AUTH_CONST.__auth_got: 0x608
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x648
   __AUTH_CONST.__objc_const: 0x770
+  __AUTH_CONST.__auth_got: 0x6e0
   __AUTH.__objc_data: 0x208
   __AUTH.__data: 0xb8
   __DATA.__objc_ivar: 0x4
-  __DATA.__data: 0x438
+  __DATA.__data: 0x440
   __DATA.__bss: 0xa00
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x3f8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 618987AB-B493-32A4-B2AF-4EE51BAF39F6
-  Functions: 420
-  Symbols:   416
-  CStrings:  161
+  UUID: C75D53A9-06F0-378A-B2F9-EADE1363D1FC
+  Functions: 417
+  Symbols:   475
+  CStrings:  43
 
Symbols:
+ ___swift_async_cont_functlets
+ ___swift_closure_destructor
+ ___swift_closure_destructor.2
+ ___swift_closure_destructor.25
+ ___swift_closure_destructor.28
+ ___swift_closure_destructor.2Tm
+ ___swift_closure_destructor.35
+ ___swift_closure_destructor.35Tm
+ ___swift_closure_destructor.41
+ ___swift_closure_destructor.48
+ ___swift_closure_destructor.55
+ ___swift_closure_destructor.58
+ ___swift_closure_destructor.8
+ __swift_implicitisolationactor_to_executor_cast
+ _block_copy_helper.30
+ _block_descriptor.32
+ _block_destroy_helper.31
+ _objc_claimAutoreleasedReturnValue
+ _swift_continuation_await
+ _swift_continuation_init
+ _swift_release_x1
+ _swift_release_x10
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x27
+ _swift_release_x8
+ _swift_retain_x1
+ _swift_retain_x10
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_retain_x8
+ _swift_retain_x9
- _block_copy_helper.31
- _block_descriptor.33
- _block_destroy_helper.32
- _objc_retain_x25
- _objectdestroy.2Tm
- _objectdestroy.35Tm
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"EncoreService\""
- "@\"NSString\"16@0:8"
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@\"NSCoder\"16"
- "@24@0:8@16"
- "@32@0:8:16@24"
- "@40@0:8:16@24@32"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@\"NSXPCListener\"16@\"NSXPCConnection\"24"
- "B32@0:8@16@24"
- "ENCEncoreServiceLauncher"
- "EncoreEvent"
- "EncoreService"
- "NSCoding"
- "NSObject"
- "NSSecureCoding"
- "NSXPCListenerDelegate"
- "Q16@0:8"
- "T#,R"
- "T@\"EncoreService\",N,R"
- "T@\"EncoreService\",R,N,V_encoreService"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",N,R"
- "T@\"NSString\",R,C"
- "TB,N,R"
- "TB,R"
- "TQ,R"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_TtC16EncoreXPCService12AsyncService"
- "_TtC16EncoreXPCService14SnippetService"
- "_TtP16EncoreXPCService12Receptionist_"
- "_TtP16EncoreXPCService23DistributedEventHandler_"
- "_TtP16EncoreXPCService6Encore_"
- "_encoreService"
- "anonymousListener"
- "archivedDataWithRootObject:requiringSecureCoding:error:"
- "autorelease"
- "broadcastWithEvent:"
- "class"
- "conformsToProtocol:"
- "connection"
- "continuation"
- "data"
- "dealloc"
- "debugDescription"
- "description"
- "echoWithEvent:"
- "encodeObject:forKey:"
- "encodeWithCoder:"
- "encore"
- "encoreService"
- "endpoint"
- "eventHandler"
- "events"
- "handleEventWithEvent:"
- "hash"
- "id"
- "init"
- "initWithArray:"
- "initWithCoder:"
- "initWithListenerEndpoint:"
- "initWithMachServiceName:"
- "initWithMachServiceName:options:"
- "interfaceWithProtocol:"
- "isEqual:"
- "isKindOfClass:"
- "isMemberOfClass:"
- "isProxy"
- "jsonDecoder"
- "jsonEncoder"
- "listener"
- "listener:shouldAcceptNewConnection:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "publishWithEvent:"
- "queue"
- "registerWithClient:name:with:"
- "release"
- "remoteObjectProxy"
- "remoteObjectProxyWithErrorHandler:"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "self"
- "service"
- "serviceName"
- "setClasses:forSelector:argumentIndex:ofReply:"
- "setDelegate:"
- "setExportedInterface:"
- "setExportedObject:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setRemoteObjectInterface:"
- "subscribeWithCompletion:"
- "superclass"
- "supportsSecureCoding"
- "v12@?0B8"
- "v16@0:8"
- "v16@?0@\"NSError\"8"
- "v24@0:8@\"EncoreEvent\"16"
- "v24@0:8@\"NSCoder\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?@\"EncoreEvent\">16"
- "v40@0:8@\"NSXPCListenerEndpoint\"16@\"NSString\"24@?<v@?B>32"
- "v40@0:8@16@24@?32"
- "v8@?0"
- "zone"

```
