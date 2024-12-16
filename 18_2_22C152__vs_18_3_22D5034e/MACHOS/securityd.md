## securityd

> `/usr/libexec/securityd`

```diff

-61439.62.1.0.0
-  __TEXT.__text: 0x23075c
+61439.80.11.0.0
+  __TEXT.__text: 0x2308e4
   __TEXT.__auth_stubs: 0x38c0
   __TEXT.__objc_stubs: 0x1a4c0
   __TEXT.__objc_methlist: 0x128e4
   __TEXT.__const: 0x8cd
-  __TEXT.__cstring: 0x1f937
-  __TEXT.__oslogstring: 0x29037
+  __TEXT.__cstring: 0x1f929
+  __TEXT.__oslogstring: 0x29062
   __TEXT.__gcc_except_tab: 0xacb0
   __TEXT.__objc_classname: 0x2284
-  __TEXT.__objc_methname: 0x292ad
-  __TEXT.__objc_methtype: 0x99e2
+  __TEXT.__objc_methname: 0x292e2
+  __TEXT.__objc_methtype: 0x9a89
   __TEXT.__dlopen_cstrs: 0x1c8
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x6218
+  __TEXT.__unwind_info: 0x6220
   __DATA_CONST.__auth_got: 0x1c70
-  __DATA_CONST.__got: 0x1040
+  __DATA_CONST.__got: 0x1048
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA_CONST.__const: 0x13080
-  __DATA_CONST.__cfstring: 0x1a5a0
+  __DATA_CONST.__const: 0x13058
+  __DATA_CONST.__cfstring: 0x1a560
   __DATA_CONST.__objc_classlist: 0x870
   __DATA_CONST.__objc_catlist: 0x68
   __DATA_CONST.__objc_protolist: 0x210

   - /usr/lib/libprequelite.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 9066
-  Symbols:   1451
-  CStrings:  15147
+  Functions: 9067
+  Symbols:   1452
+  CStrings:  15148
 
Symbols:
+ __xpc_type_fd
CStrings:
+ "-[CuttlefishXPCWrapper dumpWithSpecificUser:fileDescriptor:reply:]_block_invoke"
+ "Error in status RPC for arguments (%@): %@"
+ "dumpWithSpecificUser:fileDescriptor:reply:"
+ "rpcStatus:reply:"
+ "setXPCType:forSelector:argumentIndex:ofReply:"
+ "status:xpcFd:reply:"
+ "v40@0:8@\"OTControlArguments\"16@\"NSObject<OS_xpc_object>\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
+ "v40@0:8@\"TPSpecificUser\"16@\"NSObject<OS_xpc_object>\"24@?<v@?@\"NSError\">32"
- "-[CuttlefishXPCWrapper dumpWithSpecificUser:reply:]_block_invoke"
- "cleanseErrorForXPC:"
- "contextDump"
- "contextDumpError"
- "dumpWithSpecificUser:reply:"
- "rpcStatus:"
- "status:reply:"

```
