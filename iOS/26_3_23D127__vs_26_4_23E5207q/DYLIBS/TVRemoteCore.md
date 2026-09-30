## TVRemoteCore

> `/System/Library/PrivateFrameworks/TVRemoteCore.framework/TVRemoteCore`

```diff

-548.30.4.0.0
-  __TEXT.__text: 0x420a4
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x59dc
+548.40.44.0.0
+  __TEXT.__text: 0x461b4
+  __TEXT.__auth_stubs: 0x6b0
+  __TEXT.__objc_methlist: 0x5a1c
   __TEXT.__const: 0x230
-  __TEXT.__gcc_except_tab: 0xbec
-  __TEXT.__cstring: 0x2ff8
-  __TEXT.__oslogstring: 0x6aaa
-  __TEXT.__unwind_info: 0x1000
+  __TEXT.__gcc_except_tab: 0xc04
+  __TEXT.__cstring: 0x3013
+  __TEXT.__oslogstring: 0x6afc
+  __TEXT.__unwind_info: 0x14e8
   __TEXT.__objc_classname: 0x828
-  __TEXT.__objc_methname: 0xc820
+  __TEXT.__objc_methname: 0xc880
   __TEXT.__objc_methtype: 0x209c
-  __TEXT.__objc_stubs: 0x7ee0
+  __TEXT.__objc_stubs: 0x7f20
   __DATA_CONST.__got: 0x498
-  __DATA_CONST.__const: 0x1390
+  __DATA_CONST.__const: 0x13a8
   __DATA_CONST.__objc_classlist: 0x218
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2e58
+  __DATA_CONST.__objc_selrefs: 0x2e68
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x1a0
   __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__auth_got: 0x368
   __AUTH_CONST.__const: 0x440
-  __AUTH_CONST.__cfstring: 0x3e80
-  __AUTH_CONST.__objc_const: 0x88a0
+  __AUTH_CONST.__cfstring: 0x3ee0
+  __AUTH_CONST.__objc_const: 0x88e8
   __AUTH_CONST.__objc_intobj: 0x258
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_doubleobj: 0x50
   __AUTH.__objc_data: 0x13b0
-  __DATA.__objc_ivar: 0x5b0
+  __DATA.__objc_ivar: 0x5b4
   __DATA.__data: 0x9d0
   __DATA.__bss: 0xf8
   __DATA_DIRTY.__objc_data: 0x140

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: BAF7BF20-97D9-3694-943D-42DA6AFB1FA5
-  Functions: 1862
-  Symbols:   6335
-  CStrings:  4145
+  UUID: 20C3F966-86A2-3C43-88B9-7F88637363F7
+  Functions: 1873
+  Symbols:   6412
+  CStrings:  4155
 
Symbols:
+ -[TVRCRPCompanionLinkClientWrapper negotiatedVersion]
+ -[TVRCRPCompanionLinkClientWrapper setNegotiatedVersion:]
+ -[TVRCRapportDeviceImpl negotiatedVersion]
+ -[TVRXDevice negotiatedVersion]
+ _OBJC_IVAR_$_TVRCRPCompanionLinkClientWrapper._negotiatedVersion
+ _OUTLINED_FUNCTION_10
+ _OUTLINED_FUNCTION_11
+ _OUTLINED_FUNCTION_12
+ _TVRCCurrentProtocolVersion
+ _TVRCLuckierEAlignedVersion
+ _TVRCProtocolVersionKey
+ ___60-[TVRCRPCompanionLinkClientWrapper _launchApplicationOrURL:]_block_invoke.159
+ ___60-[TVRCRPCompanionLinkClientWrapper _launchApplicationOrURL:]_block_invoke.159.cold.1
+ ___60-[TVRCRPCompanionLinkClientWrapper _setupMediaEventsManager]_block_invoke.126
+ ___60-[TVRCRPCompanionLinkClientWrapper _setupMediaEventsManager]_block_invoke.126.cold.1
+ ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.152
+ ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.152.cold.1
+ ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.153
+ ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.153.cold.1
+ ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.154
+ ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.154.cold.1
+ ___66-[TVRCRPCompanionLinkClientWrapper _setupLegacyMediaEventsManager]_block_invoke.128
+ ___66-[TVRCRPCompanionLinkClientWrapper _setupLegacyMediaEventsManager]_block_invoke.128.cold.1
+ ___block_literal_global.130
+ ___block_literal_global.144
+ _objc_msgSend$negotiatedVersion
+ _objc_msgSend$setNegotiatedVersion:
- ___60-[TVRCRPCompanionLinkClientWrapper _launchApplicationOrURL:]_block_invoke.156
- ___60-[TVRCRPCompanionLinkClientWrapper _launchApplicationOrURL:]_block_invoke.156.cold.1
- ___60-[TVRCRPCompanionLinkClientWrapper _setupMediaEventsManager]_block_invoke.123
- ___60-[TVRCRPCompanionLinkClientWrapper _setupMediaEventsManager]_block_invoke.123.cold.1
- ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.149
- ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.149.cold.1
- ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.150
- ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.150.cold.1
- ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.151
- ___63-[TVRCRPCompanionLinkClientWrapper _handleSideEffectsForEvent:]_block_invoke.151.cold.1
- ___66-[TVRCRPCompanionLinkClientWrapper _setupLegacyMediaEventsManager]_block_invoke.125
- ___66-[TVRCRPCompanionLinkClientWrapper _setupLegacyMediaEventsManager]_block_invoke.125.cold.1
- ___block_literal_global.127
- ___block_literal_global.141
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x3
- _objc_retain_x4
- _objc_retain_x9
CStrings:
+ "1.0"
+ "1.1"
+ "ProtocolVersionKey"
+ "Session started for companionLinkClient %{public}@ \n currentVersion: %{public}@ peerVersion: %{public}@ negotiatedVersion: %{public}@"
+ "T@\"NSString\",C,N,V_negotiatedVersion"
+ "_negotiatedVersion"
+ "negotiatedVersion"
+ "setNegotiatedVersion:"
- "Session started for companionLinkClient %{public}@."

```
