## StorageKit

> `/System/Library/PrivateFrameworks/StorageKit.framework/StorageKit`

```diff

-1000.0.0.0.0
-  __TEXT.__text: 0x2bf28
-  __TEXT.__auth_stubs: 0xb20
-  __TEXT.__objc_methlist: 0x344c
+1014.0.0.0.1
+  __TEXT.__text: 0x2bde8
+  __TEXT.__auth_stubs: 0xb50
+  __TEXT.__objc_methlist: 0x34c4
   __TEXT.__const: 0x10a
-  __TEXT.__oslogstring: 0x13f1
-  __TEXT.__cstring: 0x30cc
-  __TEXT.__gcc_except_tab: 0x1398
+  __TEXT.__oslogstring: 0x143d
+  __TEXT.__cstring: 0x303c
+  __TEXT.__gcc_except_tab: 0x13b8
   __TEXT.__swift5_typeref: 0x56
   __TEXT.__swift5_fieldmd: 0x30
   __TEXT.__constg_swiftt: 0x74
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_types: 0x8
   __TEXT.__unwind_info: 0xc28
-  __TEXT.__objc_classname: 0x67c
-  __TEXT.__objc_methname: 0x6b1a
-  __TEXT.__objc_methtype: 0xf6c
-  __TEXT.__objc_stubs: 0x6160
-  __DATA_CONST.__got: 0x320
-  __DATA_CONST.__const: 0x900
-  __DATA_CONST.__objc_classlist: 0x210
+  __TEXT.__objc_classname: 0x68c
+  __TEXT.__objc_methname: 0x6bbd
+  __TEXT.__objc_methtype: 0xf54
+  __TEXT.__objc_stubs: 0x6240
+  __DATA_CONST.__got: 0x328
+  __DATA_CONST.__const: 0x930
+  __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_protolist: 0xa0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1d40
+  __DATA_CONST.__objc_selrefs: 0x1d78
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__objc_superrefs: 0x120
+  __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0xf8
-  __AUTH_CONST.__auth_got: 0x5a0
+  __AUTH_CONST.__auth_got: 0x5b8
   __AUTH_CONST.__const: 0x5c8
-  __AUTH_CONST.__cfstring: 0x3580
-  __AUTH_CONST.__objc_const: 0x7978
+  __AUTH_CONST.__cfstring: 0x35c0
+  __AUTH_CONST.__objc_const: 0x7aa0
   __AUTH_CONST.__objc_dictobj: 0x168
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x10d0
-  __DATA.__objc_ivar: 0x34c
+  __AUTH.__objc_data: 0x1120
+  __DATA.__objc_ivar: 0x358
   __DATA.__data: 0xa98
-  __DATA.__bss: 0x80
+  __DATA.__bss: 0x88
   __DATA_DIRTY.__objc_data: 0x498
   __DATA_DIRTY.__data: 0x50
   __DATA_DIRTY.__bss: 0x58

   - /usr/lib/libutil.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
-  UUID: B5FC6AF4-1BA7-3D1C-B7DC-C17D095E2B2C
-  Functions: 1181
-  Symbols:   4513
-  CStrings:  2710
+  UUID: 6CEDC19D-8421-3B57-B8DD-FEBF8F74A496
+  Functions: 1190
+  Symbols:   4546
+  CStrings:  2729
 
Symbols:
+ +[SKManager initializedManager]
+ -[SKHelperClient hasDaemonAccess]
+ -[SKHelperClient retrieveFilesystems]
+ -[SKHelperClient setHasDaemonAccess:]
+ -[SKHelperClient syncAllDisks]
+ -[SKSyncXPCCaller .cxx_destruct]
+ -[SKSyncXPCCaller group]
+ -[SKSyncXPCCaller helperClient]
+ -[SKSyncXPCCaller initWithHelperClient:]
+ -[SKSyncXPCCaller queueWithCompletionBlock:]
+ -[SKSyncXPCCaller setGroup:]
+ -[SKSyncXPCCaller setHelperClient:]
+ -[SKSyncXPCCaller syncRemoteObject]
+ -[SKSyncXPCCaller wait]
+ GCC_except_table12
+ GCC_except_table15
+ GCC_except_table20
+ GCC_except_table21
+ GCC_except_table26
+ GCC_except_table28
+ GCC_except_table32
+ GCC_except_table56
+ GCC_except_table63
+ GCC_except_table71
+ GCC_except_table90
+ _OBJC_CLASS_$_SKSyncXPCCaller
+ _OBJC_IVAR_$_SKHelperClient._hasDaemonAccess
+ _OBJC_IVAR_$_SKSyncXPCCaller._group
+ _OBJC_IVAR_$_SKSyncXPCCaller._helperClient
+ _OBJC_METACLASS_$_SKSyncXPCCaller
+ _SANDBOX_CHECK_NO_REPORT
+ __OBJC_$_INSTANCE_METHODS_SKSyncXPCCaller
+ __OBJC_$_INSTANCE_VARIABLES_SKSyncXPCCaller
+ __OBJC_$_PROP_LIST_SKSyncXPCCaller
+ __OBJC_CLASS_RO_$_SKSyncXPCCaller
+ __OBJC_METACLASS_RO_$_SKSyncXPCCaller
+ ___22-[SKHelperClient init]_block_invoke.83
+ ___30-[SKHelperClient syncAllDisks]_block_invoke
+ ___31+[SKManager initializedManager]_block_invoke
+ ___35-[SKSyncXPCCaller syncRemoteObject]_block_invoke
+ ___37-[SKHelperClient createXPCConnection]_block_invoke.126
+ ___37-[SKHelperClient retrieveFilesystems]_block_invoke
+ ___37-[SKHelperClient retrieveFilesystems]_block_invoke_2
+ ___44-[SKSyncXPCCaller queueWithCompletionBlock:]_block_invoke
+ ___50-[SKHelperClient syncAllDisksWithCompletionBlock:]_block_invoke
+ ___50-[SKHelperClient syncAllDisksWithCompletionBlock:]_block_invoke_2
+ ___61-[SKHelperClient recacheDisk:options:blocking:callbackBlock:]_block_invoke.100
+ ___71-[SKHelperClient physicalStoresForAPFSVolume:blocking:completionBlock:]_block_invoke_6
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSArray"8ls32l8
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSArray"8ls32l8r40l8
+ ___block_descriptor_48_e8_32s40r_e5_v8?0lr40l8s32l8
+ ___block_literal_global.86
+ _getpid
+ _initializedManager.once
+ _objc_msgSend$filesystemsWithCallbackBlock:
+ _objc_msgSend$group
+ _objc_msgSend$hasDaemonAccess
+ _objc_msgSend$helperClient
+ _objc_msgSend$initWithHelperClient:
+ _objc_msgSend$initializedManager
+ _objc_msgSend$queueWithCompletionBlock:
+ _objc_msgSend$retrieveFilesystems
+ _objc_msgSend$setHasDaemonAccess:
+ _objc_msgSend$syncRemoteObject
+ _objc_msgSend$synchronousRemoteObjectProxyWithErrorHandler:
+ _objc_msgSend$wait
+ _objc_release_x10
+ _sandbox_check
- -[SKHelperClient diskForPath:blocking:withCallbackBlock:]
- -[SKHelperClient diskForPath:withCallbackBlock:]
- -[SKHelperClient filesystemsWithBlocking:callbackBlock:]
- -[SKHelperClient syncAllDisksWithBlocking:completionBlock:]
- GCC_except_table13
- GCC_except_table14
- GCC_except_table25
- GCC_except_table29
- GCC_except_table31
- GCC_except_table34
- GCC_except_table54
- GCC_except_table58
- GCC_except_table66
- GCC_except_table83
- GCC_except_table9
- ___22-[SKHelperClient init]_block_invoke.59
- ___24-[SKManager filesystems]_block_invoke_2
- ___25-[SKManager diskForPath:]_block_invoke
- ___37-[SKHelperClient createXPCConnection]_block_invoke.96
- ___56-[SKHelperClient filesystemsWithBlocking:callbackBlock:]_block_invoke
- ___56-[SKHelperClient filesystemsWithBlocking:callbackBlock:]_block_invoke_2
- ___57-[SKHelperClient diskForPath:blocking:withCallbackBlock:]_block_invoke
- ___57-[SKHelperClient diskForPath:blocking:withCallbackBlock:]_block_invoke_2
- ___57-[SKHelperClient diskForPath:blocking:withCallbackBlock:]_block_invoke_3
- ___59-[SKHelperClient syncAllDisksWithBlocking:completionBlock:]_block_invoke
- ___59-[SKHelperClient syncAllDisksWithBlocking:completionBlock:]_block_invoke_2
- ___61-[SKHelperClient recacheDisk:options:blocking:callbackBlock:]_block_invoke.76
- ___71-[SKHelperClient physicalStoresForAPFSVolume:blocking:completionBlock:]_block_invoke.85
- ___block_descriptor_56_e8_32s40s48bs_e17_v16?0"NSArray"8ls32l8s48l8s40l8
- ___block_literal_global.62
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_StorageKit
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_StorageKit
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_StorageKit
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_StorageKit
- _objc_msgSend$diskForPath:blocking:withCallbackBlock:
- _objc_msgSend$diskForPath:withCompletionUUID:
- _objc_msgSend$filesystemsWithBlocking:callbackBlock:
- _objc_msgSend$filesystemsWithCompletionUUID:
- _objc_msgSend$syncAllDisksWithBlocking:completionBlock:
CStrings:
+ "%s: Client %@ access to storagekitd"
+ "-[SKHelperClient createXPCConnection]"
+ "-[SKHelperClient physicalStoresForAPFSVolume:blocking:completionBlock:]_block_invoke_6"
+ "-[SKHelperClient syncAllDisksWithCompletionBlock:]"
+ "-[SKSyncXPCCaller syncRemoteObject]_block_invoke"
+ "@\"NSObject<OS_dispatch_group>\""
+ "@\"SKHelperClient\""
+ "SKSyncXPCCaller"
+ "Skipping sync command, no daemon access"
+ "T@\"NSObject<OS_dispatch_group>\",&,N,V_group"
+ "T@\"SKHelperClient\",&,N,V_helperClient"
+ "TB,V_hasDaemonAccess"
+ "_group"
+ "_hasDaemonAccess"
+ "_helperClient"
+ "doesn't have"
+ "group"
+ "has"
+ "hasDaemonAccess"
+ "helperClient"
+ "initWithHelperClient:"
+ "initializedManager"
+ "mach-lookup"
+ "queueWithCompletionBlock:"
+ "retrieveFilesystems"
+ "setGroup:"
+ "setHasDaemonAccess:"
+ "setHelperClient:"
+ "syncRemoteObject"
+ "synchronousRemoteObjectProxyWithErrorHandler:"
+ "wait"
- "-[SKHelperClient diskForPath:blocking:withCallbackBlock:]"
- "-[SKHelperClient diskForPath:blocking:withCallbackBlock:]_block_invoke_3"
- "-[SKHelperClient filesystemsWithBlocking:callbackBlock:]"
- "-[SKHelperClient filesystemsWithBlocking:callbackBlock:]_block_invoke_2"
- "-[SKHelperClient physicalStoresForAPFSVolume:blocking:completionBlock:]_block_invoke_5"
- "-[SKHelperClient syncAllDisksWithBlocking:completionBlock:]"
- "diskForPath:blocking:withCallbackBlock:"
- "diskForPath:withCallbackBlock:"
- "diskForPath:withCompletionUUID:"
- "filesystemsWithBlocking:callbackBlock:"
- "filesystemsWithCompletionUUID:"
- "syncAllDisksWithBlocking:completionBlock:"
- "v32@0:8@\"NSString\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16@?<v@?@\"SKDisk\">24"

```
