## AppleLOM

> `/System/Library/PrivateFrameworks/AppleLOM.framework/Versions/A/AppleLOM`

```diff

 70.0.0.0.0
-  __TEXT.__text: 0x22cb8
-  __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_methlist: 0xc64
+  __TEXT.__text: 0x224d0
+  __TEXT.__auth_stubs: 0xc90
+  __TEXT.__objc_methlist: 0xe04
   __TEXT.__const: 0xc8
-  __TEXT.__gcc_except_tab: 0xdac
+  __TEXT.__gcc_except_tab: 0xddc
   __TEXT.__oslogstring: 0x32f2
-  __TEXT.__cstring: 0x10ee
-  __TEXT.__unwind_info: 0x660
+  __TEXT.__cstring: 0x10e7
+  __TEXT.__unwind_info: 0x718
   __TEXT.__objc_classname: 0x1d2
   __TEXT.__objc_methname: 0x187b
   __TEXT.__objc_methtype: 0x6c2

   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x708
+  __DATA_CONST.__objc_selrefs: 0x798
   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x650
+  __AUTH_CONST.__auth_got: 0x658
   __AUTH_CONST.__const: 0x9a0
   __AUTH_CONST.__cfstring: 0x1280
-  __AUTH_CONST.__objc_const: 0x22f0
+  __AUTH_CONST.__objc_const: 0x2008
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x550
   __DATA.__objc_ivar: 0x144

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: 8178BE0B-76FD-3071-886D-711B9F39ECFD
-  Functions: 592
-  Symbols:   1531
-  CStrings:  1177
+  UUID: F484B537-CC33-33B6-B31E-652086A9147D
+  Functions: 609
+  Symbols:   1540
+  CStrings:  1175
 
Symbols:
+ -[LOMDeviceServerConsolidated remove:error:].cold.1
+ -[LOMDeviceServerRemote registerBootVolumeNotification].cold.1
+ -[LOMDeviceServerRemote remove:error:].cold.2
+ GCC_except_table10
+ GCC_except_table13
+ LOMLog.cold.1
+ LOMNVEnableNetworkInterface.cold.1
+ LOMNVGetSecondaryIPV6Addresses.cold.1
+ LOMSecStoreIdentityPreference.cold.2
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _OUTLINED_FUNCTION_13
+ _OUTLINED_FUNCTION_14
+ _OUTLINED_FUNCTION_15
+ _OUTLINED_FUNCTION_16
+ _OUTLINED_FUNCTION_17
+ _OUTLINED_FUNCTION_18
+ _OUTLINED_FUNCTION_7
+ _OUTLINED_FUNCTION_8
+ _OUTLINED_FUNCTION_9
+ __MergedGlobals
+ _memset
+ getGenerationID.cold.1
- -[LOMControllerRequest initWithAttributes:queue:].cold.1
- -[LOMControllerRequest initWithAttributes:queue:].cold.2
- -[LOMControllerRequest initWithAttributes:queue:].cold.3
- -[LOMControllerRequest initWithAttributes:queue:].cold.4
- -[LOMControllerRequest initWithAttributes:queue:].cold.5
- -[LOMControllerRequest initWithAttributes:queue:].cold.6
- -[LOMDeviceServer initWithServiceName:].cold.1
- -[LOMDeviceServer refereshCertsAndKeys].cold.1
- -[LOMDeviceServerConsolidated copySMCService].cold.1
- -[LOMDeviceServerConsolidated copySMCService].cold.2
- -[LOMDeviceServerConsolidated setupPowerStateNotification].cold.1
- -[LOMDeviceServerConsolidated smcOpen].cold.1
- -[LOMDeviceServerConsolidated smcOpen].cold.2
- -[LOMDeviceServerConsolidated smcSetResetGPIO:].cold.1
- -[LOMDeviceServerConsolidated start].cold.1
- -[LOMDeviceServerConsolidated start].cold.2
- -[LOMDeviceServerLocal initWithServiceName:].cold.1
- -[LOMDeviceServerRemote getCompatibleBridgeOSVersion:].cold.1
- -[LOMDeviceServerRemote getVersionData].cold.1
- -[LOMDeviceServerRemote getVolumeUUID].cold.1
- -[LOMDeviceServerRemote handleBootStateNotification:].cold.1
- -[LOMDeviceServerRemote handleBootStateNotification:].cold.2
- -[LOMDeviceServerRemote handleBootStateNotification:].cold.3
- -[LOMDeviceServerRemote handleBootStateNotification:].cold.4
- -[LOMDeviceServerRemote initWithServiceName:].cold.1
- -[LOMDeviceServerRemote start].cold.1
- LOMNVSendData.cold.1
- LOMNVSendData.cold.2
- LOMNVSendMagicPacketForIPV6.cold.1
- LOMNVSendMagicPacketForIPV6.cold.2
- LOMNVSendMagicPacketForIPV6.cold.3
- LOMNVSendMagicPacketForIPV6.cold.4
- LOMNVSendMagicPacketForIPV6.cold.5
- LOMNVSendMagicPacketForIPV6.cold.6
- LOMNVSendMagicPacketForIPV6.cold.7
- LOMNVSendMagicPacketForIPV6.cold.8
- LOMNVSendMagicPacketForIPV6.cold.9
- LOMSecCreateIdentityFromPersistantCertificateAndKeyData.cold.1
- LOMSecCreateIdentityFromPersistantCertificateAndKeyData.cold.2
- LOMSecCreatePrivateKeyDataFromPersistantRef.cold.1
- LOMSecCreatePrivateKeyDataFromPersistantRef.cold.2
- LOMSecLoadIdentityPreference.cold.1
- SetupNetworkPolicyWithName.onceToken
- _nwSession
- copyAQCService.cold.1
- copyAQCService.cold.2
CStrings:
- "en"
- "lom"

```
