## ModuleBase

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/ModuleBase.framework/ModuleBase`

```diff

-1656.120.6.0.0
-  __TEXT.__text: 0x5500
-  __TEXT.__auth_stubs: 0x470
-  __TEXT.__objc_methlist: 0x7e4
+2005.0.13.0.0
+  __TEXT.__text: 0x5858
+  __TEXT.__auth_stubs: 0x450
+  __TEXT.__objc_methlist: 0x854
   __TEXT.__const: 0xc0
-  __TEXT.__cstring: 0x72c
-  __TEXT.__gcc_except_tab: 0xbc
-  __TEXT.__oslogstring: 0x436
-  __TEXT.__unwind_info: 0x1e8
-  __TEXT.__objc_classname: 0x107
-  __TEXT.__objc_methname: 0x1b2c
-  __TEXT.__objc_methtype: 0xa97
-  __TEXT.__objc_stubs: 0x1200
-  __DATA_CONST.__got: 0x160
+  __TEXT.__cstring: 0x77c
+  __TEXT.__gcc_except_tab: 0xc8
+  __TEXT.__oslogstring: 0x47c
+  __TEXT.__unwind_info: 0x1f0
+  __TEXT.__objc_classname: 0x124
+  __TEXT.__objc_methname: 0x1c0b
+  __TEXT.__objc_methtype: 0xb42
+  __TEXT.__objc_stubs: 0x1240
+  __DATA_CONST.__got: 0x170
   __DATA_CONST.__const: 0x158
   __DATA_CONST.__objc_classlist: 0x38
-  __DATA_CONST.__objc_protolist: 0x30
+  __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x720
+  __DATA_CONST.__objc_selrefs: 0x750
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
-  __AUTH_CONST.__auth_got: 0x248
+  __AUTH_CONST.__auth_got: 0x238
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x8a0
-  __AUTH_CONST.__objc_const: 0x10c0
-  __AUTH_CONST.__objc_intobj: 0xd8
+  __AUTH_CONST.__cfstring: 0x900
+  __AUTH_CONST.__objc_const: 0x1120
+  __AUTH_CONST.__objc_intobj: 0xc0
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_ivar: 0xa0
-  __DATA.__data: 0x240
+  __DATA.__objc_ivar: 0xa4
+  __DATA.__data: 0x2a0
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x190
   __DATA_DIRTY.__bss: 0x50

   - /System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9926CA35-97F3-320A-9BCF-79AAB2377250
-  Functions: 139
-  Symbols:   701
-  CStrings:  598
+  UUID: A71F74C7-60C2-37B5-90B2-3D3950158FD8
+  Functions: 147
+  Symbols:   725
+  CStrings:  619
 
Symbols:
+ -[ContextPlugin credentialEncodingSeedWithReply:]
+ -[ContextPlugin credentialsUUIDWithOriginator:reply:]
+ -[ContextPlugin disposable]
+ -[ContextPlugin initWithContextOwner:underlyingPtr:flags:moduleRef:]
+ -[ContextPlugin setCredentialsUUID:originator:reply:]
+ -[Module contextPluginWithExternalizedContext:flags:reply:]
+ -[Module untrackProxy:fromPlugin:reason:]
+ _LACDTOLocationStateRawValueUnavailable
+ _LACPolicyOptionCallerAuditToken
+ _OBJC_CLASS_$_LACAuditToken
+ _OBJC_IVAR_$_ContextPlugin._disposable
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_LACLegacyNotificationPosting
+ __OBJC_$_PROTOCOL_METHOD_TYPES_LACLegacyNotificationPosting
+ __OBJC_$_PROTOCOL_REFS_LACLegacyNotificationPosting
+ __OBJC_LABEL_PROTOCOL_$_LACLegacyNotificationPosting
+ __OBJC_PROTOCOL_$_LACLegacyNotificationPosting
+ ___25-[DaemonProxy connection]_block_invoke.68
+ ___25-[DaemonProxy connection]_block_invoke.68.cold.1
+ ___25-[DaemonProxy connection]_block_invoke.cold.1
+ _objc_msgSend$data
+ _objc_msgSend$initWithRawValue:
+ _objc_msgSend$isPurposeSecureUIRecording
+ _objc_msgSend$reset
+ _objc_msgSend$setInvalidationHandler:
- -[ContextPlugin initWithContextOwner:underlyingPtr:moduleRef:]
- -[Module contextPluginWithExternalizedContext:reply:]
- _NSGetSizeAndAlignment
- _OBJC_CLASS_$_NSData
- _malloc_type_malloc
- _objc_msgSend$dataWithBytes:length:
- _objc_msgSend$objCType
- _objc_msgSend$value:withObjCType:
CStrings:
+ "@44@0:8B16^v20q28@36"
+ "DaemonProxy Connection interrupted"
+ "DaemonProxy Connection invalidated"
+ "LACLegacyNotificationPosting"
+ "TB,R,N,V_disposable"
+ "_disposable"
+ "connectToExistingContext:callback:clientId:flags:reply:"
+ "contextPluginWithExternalizedContext:flags:reply:"
+ "credentialEncodingSeedWithReply:"
+ "credentialsUUID"
+ "credentialsUUIDWithOriginator:reply:"
+ "data"
+ "disposable"
+ "initWithContextOwner:underlyingPtr:flags:moduleRef:"
+ "initWithRawValue:"
+ "isPurposeSecureUIRecording"
+ "setCredentialsUUID:originator:"
+ "setCredentialsUUID:originator:reply:"
+ "setInvalidationHandler:"
+ "untrackProxy:fromPlugin:reason:"
+ "v32@0:8@\"<LACOriginatorProt>\"16@?<v@?@\"NSUUID\"@\"NSError\">24"
+ "v40@0:8@\"NSUUID\"16@\"<LACOriginatorProt>\"24@?<v@?B@\"NSError\">32"
+ "v40@0:8@16q24@?32"
+ "v56@0:8@\"NSData\"16@\"<LACContextCallbackXPC>\"24Q32q40@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">48"
+ "v56@0:8@16@24Q32q40@?48"
- "@36@0:8B16^v20@28"
- "connectToExistingContext:callback:clientId:reply:"
- "contextPluginWithExternalizedContext:reply:"
- "dataWithBytes:length:"
- "initWithContextOwner:underlyingPtr:moduleRef:"
- "objCType"
- "v48@0:8@\"NSData\"16@\"<LACContextCallbackXPC>\"24Q32@?<v@?@\"<LAContextXPC>\"@\"NSUUID\"@\"NSString\"@\"NSError\">40"
- "value:withObjCType:"

```
