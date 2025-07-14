## distnoted

> `/usr/sbin/distnoted`

```diff

-2420.0.0.0.0
-  __TEXT.__text: 0x3c8c
-  __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__objc_stubs: 0x3c0
-  __TEXT.__objc_methlist: 0x22c
+2503.1.0.0.0
+  __TEXT.__text: 0x3ac8
+  __TEXT.__auth_stubs: 0x6a0
+  __TEXT.__objc_stubs: 0x460
+  __TEXT.__objc_methlist: 0x264
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x24
-  __TEXT.__objc_methname: 0x585
-  __TEXT.__cstring: 0x6a6
+  __TEXT.__objc_methname: 0x57e
+  __TEXT.__cstring: 0x67e
   __TEXT.__objc_classname: 0x53
-  __TEXT.__objc_methtype: 0x2ad
+  __TEXT.__objc_methtype: 0x276
   __TEXT.__oslogstring: 0x176
   __TEXT.__dof_distnoted: 0xb18
-  __TEXT.__unwind_info: 0x164
-  __DATA_CONST.__auth_got: 0x380
+  __TEXT.__unwind_info: 0x16c
+  __DATA_CONST.__auth_got: 0x360
   __DATA_CONST.__got: 0x78
-  __DATA_CONST.__const: 0x2a8
+  __DATA_CONST.__const: 0x290
   __DATA_CONST.__cfstring: 0x200
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_classrefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x18
-  __DATA.__objc_const: 0xb00
-  __DATA.__objc_selrefs: 0x140
-  __DATA.__objc_ivar: 0x8c
+  __DATA.__objc_const: 0xa08
+  __DATA.__objc_selrefs: 0x168
+  __DATA.__objc_ivar: 0x68
   __DATA.__objc_data: 0xf0
   __DATA.__data: 0x118
-  __DATA.__bss: 0x30
+  __DATA.__bss: 0x38
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1CF4D1AE-8278-399C-90F3-DDE66D8F7DF6
-  Functions: 72
-  Symbols:   135
-  CStrings:  227
+  UUID: EC25D8D1-7866-3734-9AF0-9527094761E9
+  Functions: 76
+  Symbols:   131
+  CStrings:  230
 
Symbols:
+ _dispatch_set_target_queue
+ _objc_release_x1
+ _objc_release_x21
+ _xpc_connection_get_euid
+ _xpc_dictionary_set_int64
+ _xpc_dictionary_set_string
- _dispatch_async
- _dispatch_group_create
- _dispatch_group_enter
- _dispatch_group_leave
- _dispatch_queue_create_with_target$V2
- _dispatch_retain
- _objc_release_x22
- _pthread_mutex_init
- _pthread_mutex_lock
- _pthread_mutex_unlock
CStrings:
+ "@\"_NSDNXPCServer\""
+ "@24@0:8@16"
+ "@28@0:8@16B24"
+ "@28@0:8@16i24"
+ "I16@0:8"
+ "T@\"ClientOfLocalNoteServer\",&"
+ "TI,R"
+ "_parent"
+ "com.apple.distnote.work.target"
+ "dump"
+ "euid"
+ "forward:"
+ "initWithEndpoint:"
+ "initWithPeerConnection:"
+ "initWithReceivedConnection:"
+ "initWithServiceName:privileged:"
+ "initWithXPCConnection:type:"
+ "methodclients"
+ "monitor"
+ "pid"
+ "process"
+ "registrations"
+ "setMonitor:"
+ "start:"
+ "startMonitoring"
+ "v24@0:8@\"NSObject<OS_dispatch_queue>\"16"
- "@\"NSObject<OS_dispatch_group>\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@32@0:8@16@24"
- "@36@0:8@16B24@28"
- "@36@0:8@16i24@28"
- "_connectionQueue"
- "_dgroup"
- "_dq"
- "_lock"
- "_mseqno"
- "_sconn"
- "_target"
- "com.apple.distnoted.xpc"
- "com.apple.distnoted.xpc.mach"
- "dispatchQueue"
- "initWithEndpoint:target:"
- "initWithPeerConnection:target:"
- "initWithReceivedConnection:target:"
- "initWithServiceName:privileged:target:"
- "initWithXPCConnection:type:target:"
- "start"
- "v24@?0@\"NSObject<OS_xpc_object>\"8q16"
- "{_opaque_pthread_mutex_t=\"__sig\"q\"__opaque\"[56c]}"

```
