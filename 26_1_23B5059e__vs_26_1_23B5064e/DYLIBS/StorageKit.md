## StorageKit

> `/System/Library/PrivateFrameworks/StorageKit.framework/StorageKit`

```diff

-1024.40.6.0.1
-  __TEXT.__text: 0x2be88
+1024.40.8.0.0
+  __TEXT.__text: 0x2bb68
   __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_methlist: 0x34f4
+  __TEXT.__objc_methlist: 0x34fc
   __TEXT.__const: 0x10a
-  __TEXT.__oslogstring: 0x143d
-  __TEXT.__cstring: 0x303c
+  __TEXT.__oslogstring: 0x142a
+  __TEXT.__cstring: 0x301c
   __TEXT.__gcc_except_tab: 0x13b8
   __TEXT.__swift5_typeref: 0x56
   __TEXT.__swift5_fieldmd: 0x30
   __TEXT.__constg_swiftt: 0x74
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0xc30
+  __TEXT.__unwind_info: 0xc28
   __TEXT.__objc_classname: 0x697
-  __TEXT.__objc_methname: 0x6bfa
-  __TEXT.__objc_methtype: 0xf54
-  __TEXT.__objc_stubs: 0x6260
+  __TEXT.__objc_methname: 0x6bf5
+  __TEXT.__objc_methtype: 0xef9
+  __TEXT.__objc_stubs: 0x6280
   __DATA_CONST.__got: 0x328
-  __DATA_CONST.__const: 0x930
+  __DATA_CONST.__const: 0x908
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d90
+  __DATA_CONST.__objc_selrefs: 0x1d98
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x130
-  __DATA_CONST.__objc_arraydata: 0xf8
+  __DATA_CONST.__objc_arraydata: 0xf0
   __AUTH_CONST.__auth_got: 0x5b8
-  __AUTH_CONST.__const: 0x5a8
-  __AUTH_CONST.__cfstring: 0x35c0
-  __AUTH_CONST.__objc_const: 0x7ae0
+  __AUTH_CONST.__const: 0x588
+  __AUTH_CONST.__cfstring: 0x35a0
+  __AUTH_CONST.__objc_const: 0x7b00
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x48
-  __AUTH_CONST.__objc_arrayobj: 0x78
+  __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH.__objc_data: 0x1080
-  __DATA.__objc_ivar: 0x358
+  __DATA.__objc_ivar: 0x35c
   __DATA.__data: 0xa98
   __DATA.__bss: 0x78
   __DATA_DIRTY.__objc_data: 0x538

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: 9E7E5941-486D-3E91-8656-6DFC720D21F4
-  Functions: 1192
-  Symbols:   4552
-  CStrings:  2733
+  UUID: CD797EB8-7ECA-3E53-B7E8-DD3B5A7CFFE5
+  Functions: 1190
+  Symbols:   4548
+  CStrings:  2731
 
Symbols:
+ -[SKHelperClient connectionDone]
+ -[SKHelperClient remoteObjectProxyWithSync:errorHandler:]
+ -[SKHelperClient setConnectionDone:]
+ GCC_except_table51
+ GCC_except_table58
+ GCC_except_table60
+ GCC_except_table68
+ GCC_except_table86
+ _OBJC_IVAR_$_SKHelperClient._connectionDone
+ ___37-[SKHelperClient createXPCConnection]_block_invoke.108
+ ___61-[SKHelperClient recacheDisk:options:blocking:callbackBlock:]_block_invoke.80
+ _objc_msgSend$connectionDone
+ _objc_msgSend$remoteObjectProxyWithSync:errorHandler:
+ _objc_msgSend$setConnectionDone:
- -[SKHelperClient setDaemonOptionsWithLanguage:authRef:withCompletionBlock:]
- GCC_except_table56
- GCC_except_table65
- GCC_except_table73
- GCC_except_table90
- ___22-[SKHelperClient init]_block_invoke
- ___22-[SKHelperClient init]_block_invoke.83
- ___37-[SKHelperClient createXPCConnection]_block_invoke.126
- ___61-[SKHelperClient recacheDisk:options:blocking:callbackBlock:]_block_invoke.100
- ___75-[SKHelperClient setDaemonOptionsWithLanguage:authRef:withCompletionBlock:]_block_invoke
- ___75-[SKHelperClient setDaemonOptionsWithLanguage:authRef:withCompletionBlock:]_block_invoke_2
- ___block_descriptor_40_e8_32s_e8_v12?0B8ls32l8
- ___block_literal_global.86
- _objc_msgSend$setDaemonOptionsWithLanguage:authRef:withCompletionBlock:
- _objc_msgSend$setDaemonOptionsWithLanguage:authRef:withCompletionUUID:
CStrings:
+ "%s: Going to send first message from client, in %s mode"
+ "-[SKHelperClient remoteObjectProxyWithSync:errorHandler:]"
+ "@28@0:8B16@?20"
+ "TB,V_connectionDone"
+ "_connectionDone"
+ "async"
+ "connectionDone"
+ "remoteObjectProxyWithSync:errorHandler:"
+ "setConnectionDone:"
+ "sync"
- "-[SKHelperClient setDaemonOptionsWithLanguage:authRef:withCompletionBlock:]"
- "Connected to daemon. Language set to: %{public}@"
- "Daemon failed to respond."
- "English"
- "SKHelperClient.m"
- "setDaemonOptionsWithLanguage:authRef:withCompletionBlock:"
- "setDaemonOptionsWithLanguage:authRef:withCompletionUUID:"
- "v36@0:8@\"NSString\"16C24@\"NSString\"28"
- "v36@0:8@\"NSString\"16C24@?<v@?B>28"
- "v36@0:8@16C24@28"
- "v36@0:8@16C24@?28"

```
