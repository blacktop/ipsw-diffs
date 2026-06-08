## MemoryDiagnostics

> `/System/Library/PrivateFrameworks/MemoryDiagnostics.framework/MemoryDiagnostics`

```diff

-314.120.5.0.0
-  __TEXT.__text: 0x109c
-  __TEXT.__auth_stubs: 0x300
+356.0.0.0.0
+  __TEXT.__text: 0x1000
   __TEXT.__const: 0x88
   __TEXT.__oslogstring: 0x14a
   __TEXT.__cstring: 0x5f8
   __TEXT.__gcc_except_tab: 0x60
-  __TEXT.__unwind_info: 0x90
-  __TEXT.__objc_methname: 0x86
-  __TEXT.__objc_stubs: 0xc0
-  __DATA_CONST.__got: 0x68
+  __TEXT.__unwind_info: 0x98
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_methname: 0x0
   __DATA_CONST.__const: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x190
+  __DATA_CONST.__got: 0x0
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x840
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__data: 0x208
-  __DATA.__bss: 0x10
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/ServiceManagement.framework/ServiceManagement
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AE3B0F2A-6CED-3255-A84E-EBBFEBC75ED9
+  UUID: 0C55A4B6-609E-301E-A6B0-6D5E85D1A42F
   Functions: 12
-  Symbols:   167
-  CStrings:  161
+  Symbols:   171
+  CStrings:  155
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retain
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x3
+ _objc_retain_x8
- _objc_retain_x21
- _objc_retain_x24
Functions:
~ _memgraph_from_task_save_immediate : 1056 -> 1008
~ _RMEGetXPCConnection : 100 -> 84
~ ___RMEGetXPCConnection_block_invoke_2 : 228 -> 180
~ _ReportMemoryExceptionFromTask : 1308 -> 1288
~ ___ReportMemoryExceptionFromTask_block_invoke : 612 -> 600
~ ___ReportMemoryExceptionFromTask_block_invoke.19 : 100 -> 96
~ _RMEHandleAnalyzeReply : 264 -> 256
CStrings:
- "UTF8String"
- "dictionaryWithObjects:forKeys:count:"
- "errorWithDomain:code:userInfo:"
- "initWithUTF8String:"
- "isEqualToString:"
- "stringWithFormat:"

```
