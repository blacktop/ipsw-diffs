## DeviceManagementTools

> `/System/Library/PrivateFrameworks/DeviceManagementTools.framework/Versions/A/DeviceManagementTools`

```diff

 73.0.0.0.0
-  __TEXT.__text: 0x1f278
+  __TEXT.__text: 0x1f180
   __TEXT.__auth_stubs: 0x4d0
-  __TEXT.__objc_methlist: 0x1f48
+  __TEXT.__objc_methlist: 0x2744
   __TEXT.__const: 0xe8
   __TEXT.__cstring: 0x2129
   __TEXT.__oslogstring: 0x1ba1
-  __TEXT.__gcc_except_tab: 0x36c
+  __TEXT.__gcc_except_tab: 0x368
   __TEXT.__ustring: 0x3e6
-  __TEXT.__unwind_info: 0x7d8
+  __TEXT.__unwind_info: 0x848
   __TEXT.__objc_classname: 0xbae
   __TEXT.__objc_methname: 0x6704
   __TEXT.__objc_methtype: 0x1007
   __TEXT.__objc_stubs: 0x49c0
   __DATA_CONST.__got: 0x2c8
-  __DATA_CONST.__const: 0x428
+  __DATA_CONST.__const: 0x440
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1598
+  __DATA_CONST.__objc_selrefs: 0x1648
   __DATA_CONST.__objc_superrefs: 0x128
   __DATA_CONST.__objc_arraydata: 0x108
   __AUTH_CONST.__auth_got: 0x278
   __AUTH_CONST.__const: 0x870
   __AUTH_CONST.__cfstring: 0x27a0
-  __AUTH_CONST.__objc_const: 0x6e90
+  __AUTH_CONST.__objc_const: 0x60a0
   __AUTH_CONST.__objc_dictobj: 0x258
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x60

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 624663CF-9F8D-394C-A9FE-CFF2FE4A9FAF
-  Functions: 885
-  Symbols:   2739
+  UUID: 6571C931-491F-3685-BA46-06D8468574E0
+  Functions: 909
+  Symbols:   2762
   CStrings:  2138
 
Symbols:
+ +[DMTConfigurationPayloadBase payloadSubclassesByPayloadType].cold.1
+ +[DMTPerformAutomatedDeviceEnrollmentOperation validateRequest:error:].cold.2
+ -[DMTDeauthorizationKitBackedErasePrimitives performEraseWithCompletion:].cold.2
+ -[DMTDisassociateWiFiNetworkOperation disassociateCurrentNetworkWithInterface:].cold.5
+ -[DMTMobileGestaltBackedDeviceInformationPrimitives deviceUDID].cold.1
+ DMTErrorWithCodeAndUserInfo.cold.1
+ DMTisWAPI.cold.1
+ _DMTLogEnrollment.cold.1
+ _DMTLogGeneral.cold.1
+ _DMTLogOperation.cold.1
+ __61+[DMTConfigurationPayloadBase payloadSubclassesByPayloadType]_block_invoke.cold.1
+ __96-[DMTMDMClientLibraryBackedAutomatedDeviceEnrollmentPrimitives enrollWithNonce:completionBlock:]_block_invoke.cold.1

```
