## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`

```diff

-1030.0.0.0.0
-  __TEXT.__text: 0xddaec
+1031.0.0.0.0
+  __TEXT.__text: 0xe89b4
   __TEXT.__auth_stubs: 0x1180
-  __TEXT.__objc_methlist: 0xac04
-  __TEXT.__const: 0x2250
-  __TEXT.__cstring: 0xed77
-  __TEXT.__oslogstring: 0xfa19
-  __TEXT.__gcc_except_tab: 0x240c
+  __TEXT.__objc_methlist: 0xace4
+  __TEXT.__cstring: 0xee0c
+  __TEXT.__const: 0x2370
+  __TEXT.__gcc_except_tab: 0x2490
+  __TEXT.__oslogstring: 0xfb4d
   __TEXT.__dlopen_cstrs: 0x325
   __TEXT.__constg_swiftt: 0x2d8
   __TEXT.__swift5_typeref: 0x2ed

   __TEXT.__swift5_capture: 0x90
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0x2ea0
+  __TEXT.__unwind_info: 0x2ee8
   __TEXT.__eh_frame: 0x3e8
-  __TEXT.__objc_classname: 0x1f36
-  __TEXT.__objc_methname: 0x1565d
-  __TEXT.__objc_methtype: 0x2f4a
-  __TEXT.__objc_stubs: 0xc060
-  __DATA_CONST.__got: 0xd70
-  __DATA_CONST.__const: 0x3a30
-  __DATA_CONST.__objc_classlist: 0x7d8
+  __TEXT.__objc_classname: 0x1fac
+  __TEXT.__objc_methname: 0x15691
+  __TEXT.__objc_methtype: 0x2fb4
+  __TEXT.__objc_stubs: 0xc080
+  __DATA_CONST.__got: 0xd80
+  __DATA_CONST.__const: 0x3aa8
+  __DATA_CONST.__objc_classlist: 0x7f0
   __DATA_CONST.__objc_catlist: 0x98
-  __DATA_CONST.__objc_protolist: 0x1e0
+  __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4d80
-  __DATA_CONST.__objc_protorefs: 0x70
-  __DATA_CONST.__objc_superrefs: 0x560
+  __DATA_CONST.__objc_selrefs: 0x4d88
+  __DATA_CONST.__objc_protorefs: 0x78
+  __DATA_CONST.__objc_superrefs: 0x570
   __DATA_CONST.__objc_arraydata: 0xe0
   __AUTH_CONST.__auth_got: 0x8d0
-  __AUTH_CONST.__const: 0x5fc0
-  __AUTH_CONST.__cfstring: 0xcc00
-  __AUTH_CONST.__objc_const: 0x23460
-  __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__const: 0x7100
+  __AUTH_CONST.__cfstring: 0xcce0
+  __AUTH_CONST.__objc_const: 0x23700
   __AUTH_CONST.__objc_intobj: 0x120
+  __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x108
-  __AUTH.__objc_data: 0xb88
+  __AUTH.__objc_data: 0xc78
   __AUTH.__data: 0x1d8
-  __DATA.__objc_ivar: 0xb84
-  __DATA.__data: 0x1a18
+  __DATA.__objc_ivar: 0xb94
+  __DATA.__data: 0x1a40
   __DATA.__bss: 0x1080
-  __DATA.__common: 0x44
+  __DATA.__common: 0x91
   __DATA_DIRTY.__objc_data: 0x4510
   __DATA_DIRTY.__data: 0x90
-  __DATA_DIRTY.__bss: 0x1f0
+  __DATA_DIRTY.__bss: 0x200
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 3560C881-CBC6-3C26-A137-93145599D7BE
-  Functions: 4843
-  Symbols:   16031
-  CStrings:  8852
+  UUID: D206EB66-6B6D-3C91-AF33-F2F2045B327B
+  Functions: 4873
+  Symbols:   16129
+  CStrings:  8879
 
Symbols:
+ +[AAAccountServiceDaemonInterface XPCInterface]
+ +[AAAccountServiceDaemonInterface XPCInterface].cold.1
+ -[AAAccountServiceController .cxx_destruct]
+ -[AAAccountServiceController initWithDaemonXPCEndpoint:]
+ -[AAAccountServiceController init]
+ -[AAAccountServiceController updatePropertiesForAppleAccount:options:completion:]
+ -[AAAccountServiceDaemonConnection .cxx_destruct]
+ -[AAAccountServiceDaemonConnection _connectionInvalidationHandler]
+ -[AAAccountServiceDaemonConnection _connectionInvalidationHandler].cold.1
+ -[AAAccountServiceDaemonConnection _connection]
+ -[AAAccountServiceDaemonConnection dealloc]
+ -[AAAccountServiceDaemonConnection dealloc].cold.1
+ -[AAAccountServiceDaemonConnection initWithListenerEndpoint:]
+ -[AAAccountServiceDaemonConnection init]
+ -[AAAccountServiceDaemonConnection listenerEndpoint]
+ -[AAAccountServiceDaemonConnection remoteObjectProxyWithErrorHandler:]
+ -[AAAccountServiceDaemonConnection remoteObjectProxyWithErrorHandler:].cold.1
+ -[AAAccountServiceDaemonConnection synchronousRemoteObjectProxyWithErrorHandler:]
+ -[AAAccountServiceDaemonConnection synchronousRemoteObjectProxyWithErrorHandler:].cold.1
+ _AAAccountServiceMachService
+ _AASignOutClientEACS
+ _AASignOutClientInternetAccounts
+ _AASignOutClientSpyglass
+ _AASignOutClientUnknown
+ _OBJC_CLASS_$_AAAccountServiceController
+ _OBJC_CLASS_$_AAAccountServiceDaemonConnection
+ _OBJC_CLASS_$_AAAccountServiceDaemonInterface
+ _OBJC_IVAR_$_AAAccountServiceController._daemonConnection
+ _OBJC_IVAR_$_AAAccountServiceDaemonConnection._connection
+ _OBJC_IVAR_$_AAAccountServiceDaemonConnection._listenerEndpoint
+ _OBJC_IVAR_$_AAAccountServiceDaemonConnection._unfairLock
+ _OBJC_METACLASS_$_AAAccountServiceController
+ _OBJC_METACLASS_$_AAAccountServiceDaemonConnection
+ _OBJC_METACLASS_$_AAAccountServiceDaemonInterface
+ __OBJC_$_CATEGORY_ACAccountStore_$_AppleAccount
+ __OBJC_$_CATEGORY_NSString_$_AppleAccount
+ __OBJC_$_CLASS_METHODS_AAAccountServiceDaemonInterface
+ __OBJC_$_CLASS_METHODS_NSString(AppleAccount|AAMessage)
+ __OBJC_$_INSTANCE_METHODS_AAAccountServiceController
+ __OBJC_$_INSTANCE_METHODS_AAAccountServiceDaemonConnection
+ __OBJC_$_INSTANCE_METHODS_ACAccount(AADOBRepairState|AADOBRepairState_Internal|AppleAccount|AppleAccount_Deprecated|AppleAccount_Internal|AppleID|AppleIDInternal)
+ __OBJC_$_INSTANCE_METHODS_ACAccountStore(AppleAccount|AppleID)
+ __OBJC_$_INSTANCE_METHODS_NSString(AppleAccount|AAMessage)
+ __OBJC_$_INSTANCE_VARIABLES_AAAccountServiceController
+ __OBJC_$_INSTANCE_VARIABLES_AAAccountServiceDaemonConnection
+ __OBJC_$_PROP_LIST_AAAccountServiceDaemonConnection
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AAAccountServiceInterface
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AAAccountServiceInterface
+ __OBJC_CLASS_PROTOCOLS_$_AAAccountServiceController
+ __OBJC_CLASS_RO_$_AAAccountServiceController
+ __OBJC_CLASS_RO_$_AAAccountServiceDaemonConnection
+ __OBJC_CLASS_RO_$_AAAccountServiceDaemonInterface
+ __OBJC_LABEL_PROTOCOL_$_AAAccountServiceInterface
+ __OBJC_METACLASS_RO_$_AAAccountServiceController
+ __OBJC_METACLASS_RO_$_AAAccountServiceDaemonConnection
+ __OBJC_METACLASS_RO_$_AAAccountServiceDaemonInterface
+ __OBJC_PROTOCOL_$_AAAccountServiceInterface
+ __OBJC_PROTOCOL_REFERENCE_$_AAAccountServiceInterface
+ __PROTOCOLS_AADOBRepairStateUpdater.4
+ ___109-[AADataclassManager enableDataclassesWithoutLocalDataDataclassActionsForDataclasses:fromAccount:completion:]_block_invoke.137
+ ___109-[AADataclassManager enableDataclassesWithoutLocalDataDataclassActionsForDataclasses:fromAccount:completion:]_block_invoke.137.cold.1
+ ___47+[AAAccountServiceDaemonInterface XPCInterface]_block_invoke
+ ___47-[AAAccountServiceDaemonConnection _connection]_block_invoke
+ ___47-[AAAccountServiceDaemonConnection _connection]_block_invoke.41
+ ___47-[AAAccountServiceDaemonConnection _connection]_block_invoke.cold.1
+ ___47-[AAAccountServiceDaemonConnection _connection]_block_invoke_2
+ ___47-[AAAccountServiceDaemonConnection _connection]_block_invoke_2.cold.1
+ ___66-[AAAccountServiceDaemonConnection _connectionInvalidationHandler]_block_invoke
+ ___81-[AAAccountServiceController updatePropertiesForAppleAccount:options:completion:]_block_invoke
+ ___81-[AAAccountServiceController updatePropertiesForAppleAccount:options:completion:]_block_invoke_2
+ ___81-[AAAccountServiceController updatePropertiesForAppleAccount:options:completion:]_block_invoke_2.cold.1
+ ___block_descriptor_48_e8_32bs40r_e31_v24?0"ACAccount"8"NSError"16lr40l8s32l8
+ ___block_descriptor_48_e8_32s40bs_e17_v16?0"NSError"8ls40l8s32l8
+ ___block_literal_global.119
+ ___block_literal_global.125
+ _objc_msgSend$updatePropertiesForAppleAccount:options:completion:
- __OBJC_$_CATEGORY_ACAccountStore_$_AppleID
- __OBJC_$_CATEGORY_CLASS_METHODS_NSString_$_AAMessage
- __OBJC_$_CATEGORY_NSString_$_AAMessage
- __OBJC_$_INSTANCE_METHODS_ACAccount(AADOBRepairState|AADOBRepairState_Internal|AppleID|AppleIDInternal|AppleAccount|AppleAccount_Deprecated|AppleAccount_Internal)
- __OBJC_$_INSTANCE_METHODS_ACAccountStore(AppleID|AppleAccount)
- __OBJC_$_INSTANCE_METHODS_NSString(AAMessage|AppleAccount)
- __PROTOCOLS_AADOBRepairStateUpdater.2
- ___109-[AADataclassManager enableDataclassesWithoutLocalDataDataclassActionsForDataclasses:fromAccount:completion:]_block_invoke.134
- ___109-[AADataclassManager enableDataclassesWithoutLocalDataDataclassActionsForDataclasses:fromAccount:completion:]_block_invoke.134.cold.1
- ___block_literal_global.113
- ___block_literal_global.122
CStrings:
+ "@\"AAAccountServiceDaemonConnection\""
+ "AAAccountServiceController"
+ "AAAccountServiceDaemonConnection"
+ "AAAccountServiceDaemonConnection.m"
+ "AAAccountServiceDaemonInterface"
+ "AAAccountServiceInterface"
+ "Account service connection error handler called with: %@."
+ "Account service updating account properties for account with service: %@"
+ "Connection to account service initialized"
+ "Connection to account service interrupted"
+ "Connection to account serviceinvalidated"
+ "apple-account/update-account-properties"
+ "com.apple.aa.accountService.xpc"
+ "com.apple.journal"
+ "eacs"
+ "internetAccountDeletion"
+ "spyglassSignOut"
+ "unknown"
+ "updatePropertiesForAppleAccount:options:completion:"
+ "v40@0:8@\"ACAccount\"16@\"NSDictionary\"24@?<v@?@\"ACAccount\"@\"NSError\">32"

```
