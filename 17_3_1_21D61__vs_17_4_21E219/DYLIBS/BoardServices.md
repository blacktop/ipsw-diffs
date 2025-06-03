## BoardServices

> `/System/Library/PrivateFrameworks/BoardServices.framework/BoardServices`

```diff

-651.5.0.0.0
-  __TEXT.__text: 0x41d58
-  __TEXT.__auth_stubs: 0xa10
-  __TEXT.__objc_methlist: 0x1094
+652.108.0.0.0
+  __TEXT.__text: 0x42fe8
+  __TEXT.__auth_stubs: 0xa30
+  __TEXT.__objc_methlist: 0x10ac
   __TEXT.__const: 0x68
-  __TEXT.__gcc_except_tab: 0x6e4c
-  __TEXT.__cstring: 0x4fa8
-  __TEXT.__oslogstring: 0x1da2
+  __TEXT.__gcc_except_tab: 0x7090
+  __TEXT.__cstring: 0x51ab
+  __TEXT.__oslogstring: 0x1de0
   __TEXT.__dlopen_cstrs: 0x264
-  __TEXT.__unwind_info: 0x150c
+  __TEXT.__unwind_info: 0x1560
   __TEXT.__objc_classname: 0x70b
-  __TEXT.__objc_methname: 0x3772
-  __TEXT.__objc_methtype: 0x1181
-  __TEXT.__objc_stubs: 0x1f40
-  __DATA_CONST.__got: 0xc8
-  __DATA_CONST.__const: 0xe30
+  __TEXT.__objc_methname: 0x3896
+  __TEXT.__objc_methtype: 0x119a
+  __TEXT.__objc_stubs: 0x2080
+  __DATA_CONST.__got: 0xd8
+  __DATA_CONST.__const: 0xea8
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x100
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x45b0
-  __DATA_CONST.__objc_selrefs: 0xd18
+  __DATA_CONST.__objc_selrefs: 0xd78
+  __DATA_CONST.__objc_protorefs: 0x48
+  __DATA_CONST.__objc_classrefs: 0x238
+  __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0x20
-  __AUTH_CONST.__cfstring: 0x3f00
+  __AUTH_CONST.__cfstring: 0x3fc0
   __AUTH_CONST.__objc_const: 0xca0
   __AUTH_CONST.__const: 0x380
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__auth_got: 0x518
+  __AUTH_CONST.__auth_got: 0x528
   __AUTH.__objc_data: 0x50
-  __DATA.__objc_protorefs: 0x48
-  __DATA.__objc_classrefs: 0x238
-  __DATA.__objc_superrefs: 0xd8
   __DATA.__objc_ivar: 0x3c4
   __DATA.__data: 0xc10
   __DATA.__bss: 0x8

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 453AFBE4-D789-33F7-B2E3-32B0E868185D
-  Functions: 659
-  Symbols:   2965
-  CStrings:  2120
+  UUID: AA7F585B-19B1-3E82-9DB2-EAB5E0DC0A9C
+  Functions: 666
+  Symbols:   3003
+  CStrings:  2150
 
Symbols:
+ +[BSServiceConnectionEndpoint endpointOfLaunchIdentifier:fromLaunchResponse:withService:instance:error:]
+ -[BSServiceDomainSpecification loadRBSLaunchIdentifiers]
+ -[BSServiceInterface invertInterface:]
+ _NSMachErrorDomain
+ _NSPOSIXErrorDomain
+ ___104+[BSServiceConnectionEndpoint endpointOfLaunchIdentifier:fromLaunchResponse:withService:instance:error:]_block_invoke
+ ___104+[BSServiceConnectionEndpoint endpointOfLaunchIdentifier:fromLaunchResponse:withService:instance:error:]_block_invoke_2
+ ___104+[BSServiceConnectionEndpoint endpointOfLaunchIdentifier:fromLaunchResponse:withService:instance:error:]_block_invoke_3
+ ___56-[BSServiceDomainSpecification loadRBSLaunchIdentifiers]_block_invoke
+ ___64+[BSServicesConfiguration _configurationFromPlist:postfixBlock:]_block_invoke.118
+ ___64+[BSServicesConfiguration _configurationFromPlist:postfixBlock:]_block_invoke.33
+ ___64+[BSServicesConfiguration _configurationFromPlist:postfixBlock:]_block_invoke.98
+ _____handleEvent_block_invoke.219
+ ___block_descriptor_40_ea8_32s_e30_v16?0"<BSErrorConfiguring>"8ls32l8
+ ___block_descriptor_48_ea8_32s40s_e42_v32?0"NSString"8"RBSMachEndpoint"16^B24ls32l8s40l8
+ ___block_descriptor_64_ea8_32s40s48s56s_e30_v16?0"<BSErrorConfiguring>"8ls32l8s40l8s48l8s56l8
+ ___block_literal_global.134
+ ___block_literal_global.221
+ ___block_literal_global.246
+ ___block_literal_global.250
+ ___error
+ _objc_msgSend$bs_errorWithDomain:code:configuration:
+ _objc_msgSend$endpoint
+ _objc_msgSend$error
+ _objc_msgSend$identity
+ _objc_msgSend$isXPCService
+ _objc_msgSend$managedEndpointByLaunchIdentifier
+ _objc_msgSend$process
+ _objc_msgSend$setFailureReason:
+ _objc_msgSend$setUnderlyingError:
+ _objc_msgSend$uuid
+ _unsetenv
- ___64+[BSServicesConfiguration _configurationFromPlist:postfixBlock:]_block_invoke.117
- ___64+[BSServicesConfiguration _configurationFromPlist:postfixBlock:]_block_invoke.32
- ___64+[BSServicesConfiguration _configurationFromPlist:postfixBlock:]_block_invoke.97
- _____handleEvent_block_invoke.218
- ___block_literal_global.133
- ___block_literal_global.158
- ___block_literal_global.220
- ___block_literal_global.243
- ___block_literal_global.247
CStrings:
+ "+[BSServiceConnectionEndpoint endpointOfLaunchIdentifier:fromLaunchResponse:withService:instance:error:]"
+ "@56@0:8@16@24@32@40o^@48"
+ "RBSLaunchResponse"
+ "T@\"NSString\",?,R,C"
+ "[_bs_assert_object isKindOfClass:RBSLaunchResponseClass]"
+ "bs_errorWithDomain:code:configuration:"
+ "cannot query RBSLaunchIdentifiers if BoardServices infrastructure has not initialized"
+ "could not find launch identifier '%@' in returned endpoints of %@ : %@"
+ "endpointOfLaunchIdentifier:fromLaunchResponse:withService:instance:error:"
+ "error"
+ "failed to unsetenv(BSServiceDomains) : errno=%{darwin.errno}d"
+ "identity"
+ "invalid xpcEndpoint for %@ with launch identifier '%@' from %@"
+ "invertInterface:"
+ "isXPCService"
+ "launch response did not return a process"
+ "loadRBSLaunchIdentifiers"
+ "managedEndpointByLaunchIdentifier"
+ "process"
+ "setFailureReason:"
+ "setUnderlyingError:"
+ "uuid"
+ "v16@?0@\"<BSErrorConfiguring>\"8"
+ "v32@?0@\"NSString\"8@\"RBSMachEndpoint\"16^B24"

```
