## Security

> `/System/Library/Frameworks/Security.framework/Security`

```diff

-61439.62.1.0.0
-  __TEXT.__text: 0x16f7e4
-  __TEXT.__auth_stubs: 0x3d60
-  __TEXT.__objc_methlist: 0x51f0
+61439.80.11.0.0
+  __TEXT.__text: 0x1704bc
+  __TEXT.__auth_stubs: 0x3d80
+  __TEXT.__objc_methlist: 0x5308
   __TEXT.__const: 0x9b38
-  __TEXT.__cstring: 0x178ff
-  __TEXT.__gcc_except_tab: 0x8ce8
-  __TEXT.__oslogstring: 0xece8
+  __TEXT.__cstring: 0x17927
+  __TEXT.__gcc_except_tab: 0x8cf8
+  __TEXT.__oslogstring: 0xed40
   __TEXT.__dlopen_cstrs: 0x359
   __TEXT.__ustring: 0x406
   __TEXT.__dof_codesign: 0x1ffd
   __TEXT.__dof_security_: 0x325
-  __TEXT.__unwind_info: 0x5ed8
-  __TEXT.__objc_classname: 0xa8f
-  __TEXT.__objc_methname: 0xb446
-  __TEXT.__objc_methtype: 0x3439
-  __TEXT.__objc_stubs: 0x8640
-  __DATA_CONST.__got: 0x708
+  __TEXT.__unwind_info: 0x5f00
+  __TEXT.__objc_classname: 0xadd
+  __TEXT.__objc_methname: 0xb655
+  __TEXT.__objc_methtype: 0x34b7
+  __TEXT.__objc_stubs: 0x8800
+  __DATA_CONST.__got: 0x720
   __DATA_CONST.__const: 0x11cf0
-  __DATA_CONST.__objc_classlist: 0x2f8
+  __DATA_CONST.__objc_classlist: 0x310
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2ed8
+  __DATA_CONST.__objc_selrefs: 0x2f60
   __DATA_CONST.__objc_protorefs: 0x58
-  __DATA_CONST.__objc_superrefs: 0x2a8
+  __DATA_CONST.__objc_superrefs: 0x2c0
   __DATA_CONST.__objc_arraydata: 0xf8
-  __AUTH_CONST.__auth_got: 0x1ec8
+  __AUTH_CONST.__auth_got: 0x1ed8
   __AUTH_CONST.__auth_ptr: 0x18
   __AUTH_CONST.__const: 0x4360
-  __AUTH_CONST.__cfstring: 0x15240
-  __AUTH_CONST.__objc_const: 0xab50
+  __AUTH_CONST.__cfstring: 0x15280
+  __AUTH_CONST.__objc_const: 0xae00
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_intobj: 0x138
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH.__objc_data: 0x1c20
+  __AUTH.__objc_data: 0x1d10
   __AUTH.__data: 0xd10
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x48
-  __DATA.__objc_ivar: 0x5a8
+  __DATA.__objc_ivar: 0x5bc
   __DATA.__data: 0x20c0
-  __DATA.__bss: 0x9e8
+  __DATA.__bss: 0x9f0
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__data: 0x40

   - /usr/lib/libcoretls_cfhelpers.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 6788
-  Symbols:   9376
-  CStrings:  8044
+  Functions: 6814
+  Symbols:   9407
+  CStrings:  8082
 
Symbols:
+ _NSPOSIXErrorDomain
+ _OBJC_CLASS_$_NSFileHandle
+ __xpc_type_fd
+ _pipe
+ _xpc_fd_create
CStrings:
+ "@\"NSFileHandle\""
+ "@\"NSMutableData\""
+ "AsyncPiper"
+ "AsyncPiperFailPipeForTesting"
+ "AsyncPiperFailXpcFdWrappingForTesting"
+ "Attempting to read data..."
+ "Could not box FD: %d"
+ "Could not create pipe: %d"
+ "Read %u bytes"
+ "T@\"NSFileHandle\",&,V_readHandle"
+ "T@\"NSMutableData\",&,V_bigData"
+ "T@\"NSObject<OS_dispatch_semaphore>\",&,V_semaForTestingOnly"
+ "T@\"NSObject<OS_xpc_object>\",&,V_writeXpcFd"
+ "_bigData"
+ "_readHandle"
+ "_semaForTestingOnly"
+ "_writeXpcFd"
+ "availableData"
+ "bigData"
+ "contextDump"
+ "contextDumpError"
+ "dictWithError:"
+ "initWithError:"
+ "initWithFileDescriptor:closeOnDealloc:"
+ "moreData"
+ "readHandle"
+ "semaForTestingOnly"
+ "setBigData:"
+ "setReadHandle:"
+ "setSemaForTestingOnly:"
+ "setWriteXpcFd:"
+ "setXPCType:forSelector:argumentIndex:ofReply:"
+ "status:xpcFd:reply:"
+ "v40@0:8@\"OTControlArguments\"16@\"NSObject<OS_xpc_object>\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "waitAndReleaseFd_ForTestingOnly"
+ "writeXpcFd"
+ "xpcFd"

```
