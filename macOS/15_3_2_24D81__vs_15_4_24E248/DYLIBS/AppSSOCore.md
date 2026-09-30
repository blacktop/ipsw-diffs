## AppSSOCore

> `/System/Library/PrivateFrameworks/AppSSOCore.framework/Versions/A/AppSSOCore`

```diff

-417.80.4.0.0
-  __TEXT.__text: 0x1480c
+417.100.37.0.0
+  __TEXT.__text: 0x148f4
   __TEXT.__auth_stubs: 0x5f0
-  __TEXT.__objc_methlist: 0xfd8
+  __TEXT.__objc_methlist: 0x121c
   __TEXT.__const: 0x118
-  __TEXT.__cstring: 0x1878
+  __TEXT.__cstring: 0x1885
   __TEXT.__oslogstring: 0x1bf2
   __TEXT.__gcc_except_tab: 0x388
-  __TEXT.__unwind_info: 0x510
+  __TEXT.__unwind_info: 0x578
   __TEXT.__objc_classname: 0x223
   __TEXT.__objc_methname: 0x2787
   __TEXT.__objc_methtype: 0x7d5

   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x938
+  __DATA_CONST.__objc_selrefs: 0x9c8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x78
-  __DATA_CONST.__objc_arraydata: 0x100
+  __DATA_CONST.__objc_arraydata: 0x108
   __AUTH_CONST.__auth_got: 0x308
   __AUTH_CONST.__const: 0x6d0
-  __AUTH_CONST.__cfstring: 0xfa0
-  __AUTH_CONST.__objc_const: 0x3020
+  __AUTH_CONST.__cfstring: 0xfc0
+  __AUTH_CONST.__objc_const: 0x2bf8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH.__objc_data: 0xa0

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8F2B76E9-0269-3FE4-983E-8E7055DA4FBC
-  Functions: 520
-  Symbols:   1327
-  CStrings:  1017
+  UUID: 2E3F12B3-BE8B-3F90-A773-8402598CFAF4
+  Functions: 537
+  Symbols:   1345
+  CStrings:  1019
 
Symbols:
+ +[SOAuthorizationCore(Process) isExtensionProcessWithAuditToken:completion:].cold.1
+ +[SOClient _queue].cold.1
+ +[SOConfigurationClient defaultClient].cold.2
+ +[SOInternalProtocols interfaceWithInternalProtocol:].cold.1
+ +[SOUtils currentProcessContainerPath].cold.1
+ +[SOUtils currentProcessInSystemSession].cold.1
+ +[SOUtils isAppSSOServiceAvailable].cold.1
+ +[SOUtils isInternalBuild].cold.1
+ SO_LOG_SOAuthorizationCore.cold.1
+ SO_LOG_SOClient.cold.1
+ SO_LOG_SOClientImpl.cold.1
+ SO_LOG_SOConfiguration.cold.1
+ SO_LOG_SOConfigurationClient.cold.1
+ SO_LOG_SOConfigurationVersion.cold.1
+ SO_LOG_SOErrorHelper.cold.1
+ SO_LOG_SOFullProfile.cold.1
+ SO_LOG_SOServiceConnection.cold.1
+ SO_LOG_SOUtils.cold.1
+ appSSO_init.cold.1
+ appSSO_willHandle.cold.1
+ appSSO_willPerform.cold.1
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
CStrings:
+ "mediaparserd"

```
