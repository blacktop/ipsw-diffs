## HealthAppHealthDaemon

> `/System/Library/PrivateFrameworks/HealthAppHealthDaemon.framework/HealthAppHealthDaemon`

### Sections with Same Size but Changed Content

- `__TEXT.__oslogstring`

```diff

-7027.1.54.2.3
-  __TEXT.__text: 0x47708
-  __TEXT.__objc_methlist: 0x1ee0
+7027.1.56.2.9
+  __TEXT.__text: 0x479e0
+  __TEXT.__objc_methlist: 0x1f60
   __TEXT.__const: 0x2250
-  __TEXT.__gcc_except_tab: 0x138
-  __TEXT.__cstring: 0x1855
+  __TEXT.__gcc_except_tab: 0x148
+  __TEXT.__cstring: 0x18e5
   __TEXT.__oslogstring: 0x2514
   __TEXT.__constg_swiftt: 0x9bc
   __TEXT.__swift5_typeref: 0x8b8

   __TEXT.__swift_as_ret: 0x10
   __TEXT.__swift_as_cont: 0x1c
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x19a0
+  __TEXT.__unwind_info: 0x19b8
   __TEXT.__eh_frame: 0x20f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x690
+  __DATA_CONST.__const: 0x728
   __DATA_CONST.__objc_classlist: 0x130
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x158
+  __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1490
+  __DATA_CONST.__objc_selrefs: 0x1488
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__got: 0x878
-  __AUTH_CONST.__const: 0x1598
-  __AUTH_CONST.__cfstring: 0x900
-  __AUTH_CONST.__objc_const: 0x3220
+  __DATA_CONST.__got: 0x880
+  __AUTH_CONST.__const: 0x1558
+  __AUTH_CONST.__cfstring: 0x960
+  __AUTH_CONST.__objc_const: 0x3280
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x10f0
+  __AUTH_CONST.__auth_got: 0x1100
   __AUTH.__objc_data: 0x4d8
   __AUTH.__data: 0x118
-  __DATA.__objc_ivar: 0x124
-  __DATA.__data: 0x1100
+  __DATA.__objc_ivar: 0x11c
+  __DATA.__data: 0x1160
   __DATA.__objc_stublist: 0x8
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0xc98

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1681
-  Symbols:   1530
-  CStrings:  319
+  Functions: 1688
+  Symbols:   1552
+  CStrings:  324
 
Symbols:
+ +[HDHAHealthAppPluginHostConnection sharedConnection]
+ -[HDHAHealthAppPluginHostConnection connectionInvalidated]
+ -[HDHAHealthAppPluginHostConnection exportedInterface]
+ -[HDHAHealthAppPluginHostConnection remoteInterface]
+ -[HDHAHealthAppPluginHostConnection withProxy:]
+ -[HDHealthAppProfileExtension _notifyPluginHostIfDatabaseWasRecreated:]
+ _OBJC_CLASS_$_HKDaemonConnection
+ _OBJC_CLASS_$_HKDaemonProxyProvider
+ _OBJC_IVAR_$_HDHAHealthAppPluginHostConnection._proxyProvider
+ _OUTLINED_FUNCTION_4
+ __OBJC_$_CLASS_METHODS_HDHAHealthAppPluginHostConnection
+ __OBJC_$_PROP_LIST_HDHAHealthAppPluginHostConnection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT__HKXPCExportable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS__HKXPCExportable
+ __OBJC_$_PROTOCOL_METHOD_TYPES__HKXPCExportable
+ __OBJC_$_PROTOCOL_REFS__HKXPCExportable
+ __OBJC_CLASS_PROTOCOLS_$_HDHAHealthAppPluginHostConnection
+ __OBJC_LABEL_PROTOCOL_$__HKXPCExportable
+ __OBJC_PROTOCOL_$__HKXPCExportable
+ ___47-[HDHAHealthAppPluginHostConnection withProxy:]_block_invoke
+ ___47-[HDHAHealthAppPluginHostConnection withProxy:]_block_invoke_2
+ ___53+[HDHAHealthAppPluginHostConnection sharedConnection]_block_invoke
+ ___53-[HDHAHealthAppPluginHostConnection synchronousProxy]_block_invoke_2
+ ___67-[HDHAHealthPluginHostFeedGenerator handleJournaledSharingEntries:]_block_invoke_2
+ ___block_descriptor_40_e5_v8?0l
+ ___block_descriptor_40_e8_32bs_e8_v16?08ls32l8
+ ___block_descriptor_40_e8_32r_e8_v16?08lr32l8
+ ___block_descriptor_40_e8_32s_e33_v16?0"<HKHealthAppPluginHost>"8ls32l8
+ _dispatch_once
+ _objc_release_x1
+ _sharedConnection.onceToken
+ _sharedConnection.sharedConnection
- -[HDHAHealthAppPluginHostConnection dealloc]
- -[HDHAHealthAppPluginHostConnection proxy]
- -[HDHAHealthAppPluginHostConnection resumeIfNecessary]
- -[HDHAHealthPluginHostFeedGenerator healthAppPluginHost]
- _OBJC_CLASS_$_NSXPCConnection
- _OBJC_IVAR_$_HDHAHealthAppPluginHostConnection._connection
- _OBJC_IVAR_$_HDHAHealthAppPluginHostConnection._lock
- _OBJC_IVAR_$_HDHAHealthAppPluginHostConnection._resumed
- ___42-[HDHAHealthAppPluginHostConnection proxy]_block_invoke
- ___54-[HDHAHealthAppPluginHostConnection resumeIfNecessary]_block_invoke
CStrings:
+ "Could not read the Health database identifier: %{public}@"
+ "Health database was recreated, running background generation"
+ "HealthAppHealthDaemon.LastReadyDatabaseIdentifier"
+ "com.apple.healthappd.launch"
+ "com.apple.healthappd.pluginhost"
+ "v16@?0@\"<HKHealthAppPluginHost>\"8"
+ "v16@?0@8"
- "HDHAHealthAppPluginHostConnection remote proxy interrupted"
- "HDHAHealthAppPluginHostConnection remote proxy invalidated"
```
