## icloudmailagent

> `/usr/libexec/icloudmailagent`

```diff

-37.1.0.0.0
-  __TEXT.__text: 0x21d68
-  __TEXT.__auth_stubs: 0xf40
-  __TEXT.__objc_stubs: 0x3c0
-  __TEXT.__objc_methlist: 0x36c
-  __TEXT.__const: 0x5a4
-  __TEXT.__oslogstring: 0x38e
-  __TEXT.__objc_methname: 0x108c
-  __TEXT.__cstring: 0x233b
-  __TEXT.__objc_classname: 0x6a
-  __TEXT.__objc_methtype: 0x32d
-  __TEXT.__swift5_typeref: 0x5cb
-  __TEXT.__constg_swiftt: 0x50c
+2023.2.4.0.0
+  __TEXT.__text: 0x22eb0
+  __TEXT.__auth_stubs: 0xeb0
+  __TEXT.__objc_stubs: 0x80
+  __TEXT.__objc_methlist: 0x358
+  __TEXT.__const: 0x5fa
+  __TEXT.__oslogstring: 0x46
+  __TEXT.__cstring: 0x285d
+  __TEXT.__swift5_typeref: 0x5de
+  __TEXT.__objc_methname: 0xfbb
+  __TEXT.__constg_swiftt: 0x604
   __TEXT.__swift5_proto: 0x24
-  __TEXT.__swift5_types: 0x3c
-  __TEXT.__swift5_fieldmd: 0x2cc
-  __TEXT.__swift5_reflstr: 0x3d9
+  __TEXT.__swift5_types: 0x44
+  __TEXT.__swift5_fieldmd: 0x310
+  __TEXT.__swift5_reflstr: 0x43b
   __TEXT.__swift5_capture: 0x184
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x658
+  __TEXT.__objc_classname: 0x36
+  __TEXT.__objc_methtype: 0x2dd
+  __TEXT.__unwind_info: 0x678
   __TEXT.__eh_frame: 0x8d0
-  __DATA_CONST.__auth_got: 0x7a8
+  __DATA_CONST.__auth_got: 0x760
   __DATA_CONST.__got: 0x228
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0xd00
-  __DATA_CONST.__cfstring: 0x40
+  __DATA_CONST.__const: 0xc58
   __DATA_CONST.__objc_classlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x40
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_arraydata: 0x8
-  __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0xd30
-  __DATA.__objc_selrefs: 0x430
-  __DATA.__objc_protorefs: 0x28
-  __DATA.__objc_classrefs: 0xf0
-  __DATA.__objc_superrefs: 0x10
-  __DATA.__objc_ivar: 0xc
-  __DATA.__objc_data: 0x920
-  __DATA.__data: 0x880
-  __DATA.__bss: 0x490
-  __DATA.__common: 0x38
+  __DATA.__objc_const: 0xc88
+  __DATA.__objc_selrefs: 0x418
+  __DATA.__objc_protorefs: 0x40
+  __DATA.__objc_classrefs: 0xc8
+  __DATA.__objc_data: 0xa88
+  __DATA.__data: 0x940
+  __DATA.__bss: 0x480
+  __DATA.__common: 0x70
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: F13FC082-ABCA-3687-9C02-114E7C6EB20B
-  Functions: 502
-  Symbols:   405
-  CStrings:  425
+  UUID: ECAE6BF7-EDD3-33ED-B2CF-EA49C592F5D8
+  Functions: 515
+  Symbols:   394
+  CStrings:  416
 
Symbols:
+ _$sSo8NSObjectC10ObjectiveCE2eeoiySbAB_ABtFZ
+ _OBJC_CLASS_$_EFScheduler
- _OBJC_CLASS_$_NSConstantArray
- __NSConcreteGlobalBlock
- ___CFConstantStringClassReference
- __os_log_debug_impl
- __os_log_error_impl
- _dispatch_once
- _objc_alloc
- _objc_alloc_init
- _objc_enumerationMutation
- _objc_opt_new
- _objc_release_x1
- _objc_retain_x4
- _objc_storeStrong
CStrings:
+ "Invalid entitlement on connection %@"
+ "MCCSecretAgentService listCertificatesWithEmail is called for email: %s"
+ "Resuming XPC listener for Mach service %s..."
+ "Serverside error: %@"
+ "T@\"NSXPCListener\",N,&,VsecretAgentServiceListener"
+ "T@\"_TtC15icloudmailagent25MCCAgentConnectionManager\",N,R"
+ "_TtC15icloudmailagent21MCCSecretAgentService"
+ "_TtC15icloudmailagent25MCCAgentConnectionManager"
+ "agent_connection_manager"
+ "certificateManager"
+ "cloudKitKVSManager"
+ "https://p98-mccgateway.icloud.com/smime/v1/request/encryption"
+ "https://p98-mccgateway.icloud.com/smime/v1/request/signing"
+ "https://p98-mccgateway.icloud.com/smime/v1/revoke"
+ "immediateScheduler"
+ "secret_agent_service"
- "\x01"
- "\x02"
- "@\"CertificateManager\""
- "@\"CloudKitKVSManager\""
- "@\"NSXPCListener\""
- "Invalid entitlement on connection: %@"
- "MCCAgentConnectionManager"
- "MCCSecretAgentService"
- "MCCSecretAgentService listCertificatesWithEmail is called for email:%@"
- "Resuming XPC listener for Mach service %@..."
- "T@\"NSXPCListener\",&,N,V_secretAgentServiceListener"
- "_certificateManager"
- "_cloudKitKvsManager"
- "_hasValidEntitlementsOnConnection:"
- "_secretAgentServiceListener"
- "_setupServices"
- "boolValue"
- "countByEnumeratingWithState:objects:count:"
- "https://p01-mccgateway.icloud.com/smime/v1/request/encryption"
- "https://p01-mccgateway.icloud.com/smime/v1/request/signing"
- "https://p01-mccgateway.icloud.com/smime/v1/revoke"
- "v20@?0B8@\"NSError\"12"
- "v24@?0@\"MCCSigningAndEncryptionMessagesStatus\"8@\"NSError\"16"
- "v24@?0@\"NSArray\"8@\"NSError\"16"

```
