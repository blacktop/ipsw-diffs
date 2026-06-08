## CoreAccessories

> `/System/Library/PrivateFrameworks/CoreAccessories.framework/CoreAccessories`

```diff

-1147.120.2.0.0
-  __TEXT.__text: 0x29978
-  __TEXT.__auth_stubs: 0x6e0
-  __TEXT.__objc_methlist: 0x18c4
+1176.0.26.502.1
+  __TEXT.__text: 0x26380
+  __TEXT.__objc_methlist: 0x1954
   __TEXT.__const: 0x150
-  __TEXT.__cstring: 0x3bb8
-  __TEXT.__oslogstring: 0x40cd
-  __TEXT.__gcc_except_tab: 0xce8
+  __TEXT.__cstring: 0x3c16
+  __TEXT.__oslogstring: 0x4087
+  __TEXT.__gcc_except_tab: 0x820
   __TEXT.__ustring: 0xa
-  __TEXT.__unwind_info: 0xa40
-  __TEXT.__objc_classname: 0x25a
-  __TEXT.__objc_methname: 0x485c
-  __TEXT.__objc_methtype: 0x15e0
-  __TEXT.__objc_stubs: 0x2ec0
-  __DATA_CONST.__got: 0x148
-  __DATA_CONST.__const: 0x1ed8
+  __TEXT.__unwind_info: 0xa20
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0x1f60
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf00
+  __DATA_CONST.__objc_selrefs: 0xf30
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0xd8
-  __AUTH_CONST.__auth_got: 0x380
-  __AUTH_CONST.__const: 0xa20
-  __AUTH_CONST.__cfstring: 0x39c0
-  __AUTH_CONST.__objc_const: 0x2318
+  __DATA_CONST.__got: 0x138
+  __AUTH_CONST.__const: 0xb40
+  __AUTH_CONST.__cfstring: 0x3a40
+  __AUTH_CONST.__objc_const: 0x2348
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
+  __AUTH_CONST.__auth_got: 0x0
   __DATA.__objc_ivar: 0xdc
   __DATA.__data: 0x758
-  __DATA.__bss: 0xd8
+  __DATA.__bss: 0x178
   __DATA_DIRTY.__objc_data: 0x320
   __DATA_DIRTY.__data: 0x138
-  __DATA_DIRTY.__bss: 0x90
+  __DATA_DIRTY.__bss: 0x38
   __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AB0EC9C3-A328-31F2-9D5E-27CCAEC7BA0F
-  Functions: 784
-  Symbols:   4094
-  CStrings:  2102
+  UUID: 502B0A89-3D8B-32CD-9ED8-B1715C1D5BFC
+  Functions: 821
+  Symbols:   4185
+  CStrings:  1325
 
Symbols:
+ -[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:componentIndex:]
+ -[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:componentIndex:].cold.1
+ -[ACCHWComponentAuth authenticateLASWithChallenge:completionHandler:updateRegistry:componentIndex:]
+ -[ACCHWComponentAuth authenticateLASWithChallenge:completionHandler:updateRegistry:componentIndex:].cold.1
+ -[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:componentIndex:]
+ -[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:componentIndex:].cold.1
+ -[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:componentIndex:]
+ -[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:componentIndex:].cold.1
+ -[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:componentIndex:]
+ -[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:componentIndex:].cold.1
+ -[ACCHWComponentAuth signVeridianChallenge:completionHandler:componentIndex:]
+ -[ACCHWComponentAuth signVeridianChallenge:completionHandler:componentIndex:].cold.1
+ -[ACCTransportClient propertiesDidChange:forConnectionWithUUID:previousProperties:].cold.5
+ -[ACCTransportClient propertiesDidChange:forEndpointWithUUID:previousProperties:connectionUUID:].cold.5
+ -[ACCTransportPlugin connectionPropertiesDidChangeHandler:].cold.3
+ -[ACCTransportPlugin endpointPropertiesDidChangeHandler:].cold.3
+ __MergedGlobals.4
+ ___111-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:componentIndex:]_block_invoke
+ ___111-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:componentIndex:]_block_invoke.41
+ ___111-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:componentIndex:]_block_invoke.41.cold.1
+ ___111-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:componentIndex:]_block_invoke.41.cold.2
+ ___111-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:componentIndex:]_block_invoke.41.cold.3
+ ___111-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:componentIndex:]_block_invoke_2
+ ___111-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:componentIndex:]_block_invoke_2.cold.1
+ ___111-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:componentIndex:]_block_invoke_2.cold.2
+ ___136-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:componentIndex:]_block_invoke
+ ___136-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:componentIndex:]_block_invoke.44
+ ___136-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:componentIndex:]_block_invoke.44.cold.1
+ ___136-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:componentIndex:]_block_invoke.44.cold.2
+ ___136-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:componentIndex:]_block_invoke.44.cold.3
+ ___136-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:componentIndex:]_block_invoke_2
+ ___136-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:componentIndex:]_block_invoke_2.cold.1
+ ___136-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:componentIndex:]_block_invoke_2.cold.2
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.212
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.214
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.214.cold.1
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.214.cold.2
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.216
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.216.cold.1
+ ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.216.cold.2
+ ___54-[ACCCarPlay isCarPlayPairedWithCertSerial:withReply:]_block_invoke.21
+ ___54-[ACCCarPlay isCarPlayPairedWithCertSerial:withReply:]_block_invoke.21.cold.1
+ ___54-[ACCCarPlay isCarPlayPairedWithCertSerial:withReply:]_block_invoke.21.cold.2
+ ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.233
+ ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.233.cold.1
+ ___58-[ACCCarPlay carPlayAppLinksStateForCertSerial:withReply:]_block_invoke.24
+ ___58-[ACCCarPlay carPlayAppLinksStateForCertSerial:withReply:]_block_invoke.24.cold.1
+ ___58-[ACCCarPlay carPlayAppLinksStateForCertSerial:withReply:]_block_invoke.24.cold.2
+ ___59-[ACCHWComponentAuth verifyBatteryMatch:completionHandler:]_block_invoke.47
+ ___59-[ACCHWComponentAuth verifyBatteryMatch:completionHandler:]_block_invoke.47.cold.1
+ ___59-[ACCHWComponentAuth verifyBatteryMatch:completionHandler:]_block_invoke.47.cold.2
+ ___59-[ACCHWComponentAuth verifyBatteryMatch:completionHandler:]_block_invoke.47.cold.3
+ ___60-[ACCCarPlay carPlayStartSessionForConnectionID:properties:]_block_invoke.28
+ ___60-[ACCCarPlay carPlayStartSessionForConnectionID:properties:]_block_invoke.28.cold.1
+ ___60-[ACCCarPlay carPlayStartSessionForConnectionID:properties:]_block_invoke.28.cold.2
+ ___62-[ACCCarPlay isWirelessCarPlayAllowedForCertSerial:withReply:]_block_invoke.23
+ ___62-[ACCCarPlay isWirelessCarPlayAllowedForCertSerial:withReply:]_block_invoke.23.cold.1
+ ___62-[ACCCarPlay isWirelessCarPlayAllowedForCertSerial:withReply:]_block_invoke.23.cold.2
+ ___68-[ACCAppLinksIconInfo getIconDataForBundleID:forIconSize:withReply:]_block_invoke.12
+ ___70-[ACCCarPlay carPlaySendConnectionTimeEvent:connectionType:eventTime:]_block_invoke.38
+ ___70-[ACCCarPlay carPlaySendConnectionTimeEvent:connectionType:eventTime:]_block_invoke.38.cold.1
+ ___70-[ACCCarPlay carPlaySendConnectionTimeEvent:connectionType:eventTime:]_block_invoke.38.cold.2
+ ___71-[ACCCarPlay carPlayIconStateForCertSerial:andAppCategories:withReply:]_block_invoke.26
+ ___71-[ACCCarPlay carPlayIconStateForCertSerial:andAppCategories:withReply:]_block_invoke.26.cold.1
+ ___71-[ACCCarPlay carPlayIconStateForCertSerial:andAppCategories:withReply:]_block_invoke.26.cold.2
+ ___77-[ACCHWComponentAuth signVeridianChallenge:completionHandler:componentIndex:]_block_invoke
+ ___77-[ACCHWComponentAuth signVeridianChallenge:completionHandler:componentIndex:]_block_invoke.45
+ ___77-[ACCHWComponentAuth signVeridianChallenge:completionHandler:componentIndex:]_block_invoke.45.cold.1
+ ___77-[ACCHWComponentAuth signVeridianChallenge:completionHandler:componentIndex:]_block_invoke.45.cold.2
+ ___77-[ACCHWComponentAuth signVeridianChallenge:completionHandler:componentIndex:]_block_invoke.45.cold.3
+ ___77-[ACCHWComponentAuth signVeridianChallenge:completionHandler:componentIndex:]_block_invoke_2
+ ___77-[ACCHWComponentAuth signVeridianChallenge:completionHandler:componentIndex:]_block_invoke_2.cold.1
+ ___77-[ACCHWComponentAuth signVeridianChallenge:completionHandler:componentIndex:]_block_invoke_2.cold.2
+ ___78-[ACCCarPlay filterMatchingDigitalCarKeys:forAccessory:withCompletionHandler:]_block_invoke.34
+ ___78-[ACCCarPlay filterMatchingDigitalCarKeys:forAccessory:withCompletionHandler:]_block_invoke.34.cold.1
+ ___78-[ACCCarPlay filterMatchingDigitalCarKeys:forAccessory:withCompletionHandler:]_block_invoke.34.cold.2
+ ___88-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:componentIndex:]_block_invoke
+ ___88-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:componentIndex:]_block_invoke.38
+ ___88-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:componentIndex:]_block_invoke.38.cold.1
+ ___88-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:componentIndex:]_block_invoke.38.cold.2
+ ___88-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:componentIndex:]_block_invoke.38.cold.3
+ ___88-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:componentIndex:]_block_invoke_2
+ ___88-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:componentIndex:]_block_invoke_2.cold.1
+ ___88-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:componentIndex:]_block_invoke_2.cold.2
+ ___89-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:componentIndex:]_block_invoke
+ ___89-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:componentIndex:]_block_invoke.43
+ ___89-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:componentIndex:]_block_invoke.43.cold.1
+ ___89-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:componentIndex:]_block_invoke.43.cold.2
+ ___89-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:componentIndex:]_block_invoke.43.cold.3
+ ___89-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:componentIndex:]_block_invoke_2
+ ___89-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:componentIndex:]_block_invoke_2.cold.1
+ ___89-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:componentIndex:]_block_invoke_2.cold.2
+ ___99-[ACCHWComponentAuth authenticateLASWithChallenge:completionHandler:updateRegistry:componentIndex:]_block_invoke
+ ___99-[ACCHWComponentAuth authenticateLASWithChallenge:completionHandler:updateRegistry:componentIndex:]_block_invoke.42
+ ___99-[ACCHWComponentAuth authenticateLASWithChallenge:completionHandler:updateRegistry:componentIndex:]_block_invoke.42.cold.1
+ ___99-[ACCHWComponentAuth authenticateLASWithChallenge:completionHandler:updateRegistry:componentIndex:]_block_invoke.42.cold.2
+ ___99-[ACCHWComponentAuth authenticateLASWithChallenge:completionHandler:updateRegistry:componentIndex:]_block_invoke.42.cold.3
+ ___99-[ACCHWComponentAuth authenticateLASWithChallenge:completionHandler:updateRegistry:componentIndex:]_block_invoke_2
+ ___99-[ACCHWComponentAuth authenticateLASWithChallenge:completionHandler:updateRegistry:componentIndex:]_block_invoke_2.cold.1
+ ___99-[ACCHWComponentAuth authenticateLASWithChallenge:completionHandler:updateRegistry:componentIndex:]_block_invoke_2.cold.2
+ ___block_descriptor_64_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ ___block_descriptor_65_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ ___block_descriptor_67_e8_32s40s48s56bs_e5_v8?0ls32l8s56l8s40l8s48l8
+ ___block_descriptor_tmp.3
+ ___block_literal_global.222
+ ___block_literal_global.224
+ ___block_literal_global.302
+ ___block_literal_global.33
+ ___block_literal_global.334
+ ___block_literal_global.37
+ ___block_literal_global.388
+ ___block_literal_global.40
+ ___block_literal_global.61
+ ___block_literal_global.66
+ ___block_literal_global.68
+ ___logObjectForModule_block_invoke
+ ___logObjectForModule_block_invoke.cold.1
+ ___signVeridianChallengeWithIndex_block_invoke
+ ___signVeridianChallengeWithIndex_block_invoke.cold.1
+ _kACCProperties_Connection_Inductive_ExtendedID
+ _kACCProperties_Connection_Inductive_FamilyID
+ _kACCProperties_Connection_QiAuth_QiID
+ _kACCProperties_Connection_QiAuth_WpcPolicyExtension
+ _kCFACCProperties_Connection_Inductive_ExtendedID
+ _kCFACCProperties_Connection_Inductive_FamilyID
+ _kCFACCProperties_Connection_QiAuth_QiID
+ _kCFACCProperties_Connection_QiAuth_WpcPolicyExtension
+ _logObjectForModule.onceToken
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$authenticateBatteryWithChallenge:completionHandler:componentIndex:
+ _objc_msgSend$authenticateLASWithChallenge:completionHandler:updateRegistry:componentIndex:
+ _objc_msgSend$authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:componentIndex:
+ _objc_msgSend$authenticateVeridianWithChallenge:completionHandler:componentIndex:
+ _objc_msgSend$authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:componentIndex:
+ _objc_msgSend$signVeridianChallenge:completionHandler:componentIndex:
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x5
+ _objc_retain_x8
+ _signVeridianChallengeWithIndex
+ _signVeridianChallengeWithIndex.cold.1
- -[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:].cold.1
- -[ACCHWComponentAuth authenticateLASWithChallenge:completionHandler:updateRegistry:].cold.1
- -[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:].cold.1
- -[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:].cold.1
- -[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:].cold.1
- -[ACCHWComponentAuth signVeridianChallenge:completionHandler:].cold.1
- _OUTLINED_FUNCTION_10
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- __MergedGlobals.2
- ___121-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke
- ___121-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke.31
- ___121-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke.31.cold.1
- ___121-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke.31.cold.2
- ___121-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke.31.cold.3
- ___121-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke_2
- ___121-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke_2.cold.1
- ___121-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:]_block_invoke_2.cold.2
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.213
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.215
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.215.cold.1
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.215.cold.2
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.217
- ___48-[ACCExternalAccessoryProvider connectToServer:]_block_invoke.217.cold.1
- ___54-[ACCCarPlay isCarPlayPairedWithCertSerial:withReply:]_block_invoke.22
- ___54-[ACCCarPlay isCarPlayPairedWithCertSerial:withReply:]_block_invoke.22.cold.1
- ___54-[ACCCarPlay isCarPlayPairedWithCertSerial:withReply:]_block_invoke.22.cold.2
- ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.234
- ___57-[ACCExternalAccessoryProvider ExternalAccessoryArrived:]_block_invoke.234.cold.1
- ___58-[ACCCarPlay carPlayAppLinksStateForCertSerial:withReply:]_block_invoke.25
- ___58-[ACCCarPlay carPlayAppLinksStateForCertSerial:withReply:]_block_invoke.25.cold.1
- ___58-[ACCCarPlay carPlayAppLinksStateForCertSerial:withReply:]_block_invoke.25.cold.2
- ___59-[ACCHWComponentAuth verifyBatteryMatch:completionHandler:]_block_invoke.34
- ___59-[ACCHWComponentAuth verifyBatteryMatch:completionHandler:]_block_invoke.34.cold.1
- ___59-[ACCHWComponentAuth verifyBatteryMatch:completionHandler:]_block_invoke.34.cold.2
- ___59-[ACCHWComponentAuth verifyBatteryMatch:completionHandler:]_block_invoke.34.cold.3
- ___60-[ACCCarPlay carPlayStartSessionForConnectionID:properties:]_block_invoke.29
- ___60-[ACCCarPlay carPlayStartSessionForConnectionID:properties:]_block_invoke.29.cold.1
- ___60-[ACCCarPlay carPlayStartSessionForConnectionID:properties:]_block_invoke.29.cold.2
- ___62-[ACCCarPlay isWirelessCarPlayAllowedForCertSerial:withReply:]_block_invoke.24
- ___62-[ACCCarPlay isWirelessCarPlayAllowedForCertSerial:withReply:]_block_invoke.24.cold.1
- ___62-[ACCCarPlay isWirelessCarPlayAllowedForCertSerial:withReply:]_block_invoke.24.cold.2
- ___62-[ACCHWComponentAuth signVeridianChallenge:completionHandler:]_block_invoke
- ___62-[ACCHWComponentAuth signVeridianChallenge:completionHandler:]_block_invoke.32
- ___62-[ACCHWComponentAuth signVeridianChallenge:completionHandler:]_block_invoke.32.cold.1
- ___62-[ACCHWComponentAuth signVeridianChallenge:completionHandler:]_block_invoke.32.cold.2
- ___62-[ACCHWComponentAuth signVeridianChallenge:completionHandler:]_block_invoke.32.cold.3
- ___62-[ACCHWComponentAuth signVeridianChallenge:completionHandler:]_block_invoke_2
- ___62-[ACCHWComponentAuth signVeridianChallenge:completionHandler:]_block_invoke_2.cold.1
- ___62-[ACCHWComponentAuth signVeridianChallenge:completionHandler:]_block_invoke_2.cold.2
- ___68-[ACCAppLinksIconInfo getIconDataForBundleID:forIconSize:withReply:]_block_invoke.13
- ___70-[ACCCarPlay carPlaySendConnectionTimeEvent:connectionType:eventTime:]_block_invoke.39
- ___70-[ACCCarPlay carPlaySendConnectionTimeEvent:connectionType:eventTime:]_block_invoke.39.cold.1
- ___70-[ACCCarPlay carPlaySendConnectionTimeEvent:connectionType:eventTime:]_block_invoke.39.cold.2
- ___71-[ACCCarPlay carPlayIconStateForCertSerial:andAppCategories:withReply:]_block_invoke.27
- ___71-[ACCCarPlay carPlayIconStateForCertSerial:andAppCategories:withReply:]_block_invoke.27.cold.1
- ___71-[ACCCarPlay carPlayIconStateForCertSerial:andAppCategories:withReply:]_block_invoke.27.cold.2
- ___73-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:]_block_invoke
- ___73-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:]_block_invoke.25
- ___73-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:]_block_invoke.25.cold.1
- ___73-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:]_block_invoke.25.cold.2
- ___73-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:]_block_invoke.25.cold.3
- ___73-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:]_block_invoke_2
- ___73-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:]_block_invoke_2.cold.1
- ___73-[ACCHWComponentAuth authenticateBatteryWithChallenge:completionHandler:]_block_invoke_2.cold.2
- ___74-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:]_block_invoke
- ___74-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:]_block_invoke.30
- ___74-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:]_block_invoke.30.cold.1
- ___74-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:]_block_invoke.30.cold.2
- ___74-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:]_block_invoke.30.cold.3
- ___74-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:]_block_invoke_2
- ___74-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:]_block_invoke_2.cold.1
- ___74-[ACCHWComponentAuth authenticateVeridianWithChallenge:completionHandler:]_block_invoke_2.cold.2
- ___78-[ACCCarPlay filterMatchingDigitalCarKeys:forAccessory:withCompletionHandler:]_block_invoke.35
- ___78-[ACCCarPlay filterMatchingDigitalCarKeys:forAccessory:withCompletionHandler:]_block_invoke.35.cold.1
- ___78-[ACCCarPlay filterMatchingDigitalCarKeys:forAccessory:withCompletionHandler:]_block_invoke.35.cold.2
- ___84-[ACCHWComponentAuth authenticateLASWithChallenge:completionHandler:updateRegistry:]_block_invoke
- ___84-[ACCHWComponentAuth authenticateLASWithChallenge:completionHandler:updateRegistry:]_block_invoke.29
- ___84-[ACCHWComponentAuth authenticateLASWithChallenge:completionHandler:updateRegistry:]_block_invoke.29.cold.1
- ___84-[ACCHWComponentAuth authenticateLASWithChallenge:completionHandler:updateRegistry:]_block_invoke.29.cold.2
- ___84-[ACCHWComponentAuth authenticateLASWithChallenge:completionHandler:updateRegistry:]_block_invoke.29.cold.3
- ___84-[ACCHWComponentAuth authenticateLASWithChallenge:completionHandler:updateRegistry:]_block_invoke_2
- ___84-[ACCHWComponentAuth authenticateLASWithChallenge:completionHandler:updateRegistry:]_block_invoke_2.cold.1
- ___84-[ACCHWComponentAuth authenticateLASWithChallenge:completionHandler:updateRegistry:]_block_invoke_2.cold.2
- ___96-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:]_block_invoke
- ___96-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:]_block_invoke.28
- ___96-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:]_block_invoke.28.cold.1
- ___96-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:]_block_invoke.28.cold.2
- ___96-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:]_block_invoke.28.cold.3
- ___96-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:]_block_invoke_2
- ___96-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:]_block_invoke_2.cold.1
- ___96-[ACCHWComponentAuth authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:]_block_invoke_2.cold.2
- ___block_descriptor_57_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
- ___block_descriptor_59_e8_32s40s48bs_e5_v8?0ls32l8s48l8s40l8
- ___block_literal_global.32
- ___block_literal_global.34
- ___block_literal_global.38
- ___block_literal_global.41
- ___block_literal_global.54
- ___signVeridianChallenge_block_invoke
- ___signVeridianChallenge_block_invoke.cold.1
- ___verifyBatteryMatch_block_invoke
- ___verifyBatteryMatch_block_invoke.cold.1
- _objc_msgSend$authenticateBatteryWithChallenge:completionHandler:
- _objc_msgSend$authenticateLASWithChallenge:completionHandler:updateRegistry:
- _objc_msgSend$authenticateVeridianWithChallenge:completionHandler:
- _objc_msgSend$signVeridianChallenge:completionHandler:
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x28
- _signVeridianChallenge.cold.1
- _verifyBatteryMatch
- _verifyBatteryMatch.cold.1
CStrings:
+ "Inductive_ExtendedID"
+ "Inductive_FamilyID"
+ "PearlIDCapability"
+ "QiAuth_QiID"
+ "QiAuth_WpcPolicyExtension"
- "#16@0:8"
- ".cxx_destruct"
- "8olRm6C1xqr7AJGpLRnpSw"
- "@\"<ACCConnectionInfoConfigStreamDelegateProtocol>\""
- "@\"<ACCConnectionInfoPrivateDelegateProtocol>\""
- "@\"<ACCConnectionInfoXPCServerProtocol>\""
- "@\"<ACCExternalAccessoryProviderProtocol>\""
- "@\"<ACCTransportClientDelegate>\""
- "@\"<ACCTransportPluginManagerProtocol>\""
- "@\"ACCTransportClient\""
- "@\"NSDictionary\""
- "@\"NSDictionary\"24@0:8@\"NSString\"16"
- "@\"NSLock\""
- "@\"NSMutableDictionary\""
- "@\"NSMutableSet\""
- "@\"NSNumber\""
- "@\"NSObject<OS_dispatch_queue>\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSXPCConnection\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@28@0:8@16i24"
- "@28@0:8i16@20"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24@32"
- "@44@0:8i16i20@24@32B40"
- "@52@0:8i16i20@24@?32@40B48"
- "@?"
- "@?16@0:8"
- "ACCAppLinksIconInfo"
- "ACCAppLinksIconServiceProtocol"
- "ACCCarPlay"
- "ACCCarPlayServiceProtocol"
- "ACCConnectionInfo"
- "ACCConnectionInfoXPCClientProtocol"
- "ACCConnectionInfoXPCServerProtocol"
- "ACCExternalAccessoryProvider"
- "ACCExternalAccessoryXPCClientProtocol"
- "ACCExternalAccessoryXPCServerProtocol"
- "ACCHWComponentAuth"
- "ACCHWComponentAuthServiceProtocol"
- "ACCPluginProtocol"
- "ACCTransportClient"
- "ACCTransportClientBridge"
- "ACCTransportClientDelegate"
- "ACCTransportPlugin"
- "ACCTransportPluginProtocol"
- "ACCTransportXPCClientProtocol"
- "ACCTransportXPCServerProtocol"
- "ACCUserDefaults"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B28@0:8B16@20"
- "B32@0:8@16@24"
- "B36@0:8@16@24C32"
- "B40@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32"
- "B40@0:8@16@24@32"
- "B40@0:8@16@24@?32"
- "B40@0:8i16@20B28@32"
- "B48@0:8C16S20@24@32@?40"
- "EAAccessoryArrived:"
- "EAAccessoryLeft:"
- "ExternalAccessoryArrived:"
- "ExternalAccessoryLeft:"
- "JSONObjectWithData:options:error:"
- "NSObject"
- "Q"
- "Q16@0:8"
- "T#,R"
- "T@\"<ACCConnectionInfoConfigStreamDelegateProtocol>\",W,N,V_configStreamDelegate"
- "T@\"<ACCConnectionInfoPrivateDelegateProtocol>\",W,N,V_delegate"
- "T@\"<ACCConnectionInfoPrivateDelegateProtocol>\",W,N,V_delegateForIdentifier"
- "T@\"<ACCConnectionInfoXPCServerProtocol>\",&,V_remoteObject"
- "T@\"<ACCExternalAccessoryProviderProtocol>\",W,N,V_delegate"
- "T@\"<ACCTransportClientDelegate>\",W,N,V_delegate"
- "T@\"<ACCTransportPluginManagerProtocol>\",W,N,V_delegate"
- "T@\"ACCTransportClient\",&,N,V_transportClient"
- "T@\"NSDictionary\",&,V_eaClientRegistrationInfo"
- "T@\"NSDictionary\",&,V_fullAccessoryInfo"
- "T@\"NSDictionary\",R,V_accessoryFilterDictionary"
- "T@\"NSLock\",&,N,V_listLock"
- "T@\"NSLock\",&,N,V_serverConnectionLock"
- "T@\"NSMutableDictionary\",&,N,V_connectionList"
- "T@\"NSMutableDictionary\",&,N,V_connectionPropertyChangeHandlers"
- "T@\"NSMutableDictionary\",&,N,V_endpointList"
- "T@\"NSMutableDictionary\",&,N,V_endpointPropertyChangeHandlers"
- "T@\"NSMutableDictionary\",&,V_connectionPropertyChangeHandlers"
- "T@\"NSMutableDictionary\",&,V_endpointDataOutHandlers"
- "T@\"NSMutableDictionary\",&,V_endpointPropertyChangeHandlers"
- "T@\"NSMutableDictionary\",&,V_endpointSecureTunnelDataHandlers"
- "T@\"NSMutableSet\",&,N,V_activeConnectionUUIDs"
- "T@\"NSMutableSet\",&,V_currentlyConnectedAccessories"
- "T@\"NSNumber\",&,V_isMFiCharger"
- "T@\"NSNumber\",&,V_productID"
- "T@\"NSNumber\",&,V_transportType"
- "T@\"NSNumber\",&,V_vendorID"
- "T@\"NSObject<OS_dispatch_queue>\",&,N,V_endpointEventHandlerQueue"
- "T@\"NSObject<OS_dispatch_queue>\",&,V_connectionQueue"
- "T@\"NSString\",&,N,V_identifier"
- "T@\"NSString\",&,N,V_providerUID"
- "T@\"NSString\",&,V_firmwareRevisionActive"
- "T@\"NSString\",&,V_firmwareRevisionPending"
- "T@\"NSString\",&,V_hardwareRevision"
- "T@\"NSString\",&,V_manufacturer"
- "T@\"NSString\",&,V_model"
- "T@\"NSString\",&,V_name"
- "T@\"NSString\",&,V_ppid"
- "T@\"NSString\",&,V_primaryUUID"
- "T@\"NSString\",&,V_serial"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"NSString\",R,N,V_pluginName"
- "T@\"NSXPCConnection\",&,N"
- "T@\"NSXPCConnection\",&,N,V_serverConnection"
- "T@\"NSXPCConnection\",&,N,V_xpcConnection"
- "T@\"NSXPCConnection\",&,V_serverConnection"
- "T@?,C,N,V_configStreamGetResponseHandler"
- "T@?,C,N,V_connectionAuthStatusChangedHandler"
- "T@?,C,N,V_connectionPropertiesChangedHandler"
- "T@?,C,N,V_endpointPropertiesChangedHandler"
- "T@?,C,N,V_serverDisconnectedHandler"
- "TB,R,N"
- "TB,V_isClientRegistered"
- "TQ,R"
- "TQ,V_destinationSharingOptions"
- "Ti,V_clientCapabilities"
- "UTF8String"
- "UUID"
- "UUIDString"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_ACCExternalAccessoryInfo"
- "_accessoryFilterDictionary"
- "_activeConnectionUUIDs"
- "_clientCapabilities"
- "_configStreamDelegate"
- "_configStreamGetResponseHandler"
- "_connectionAuthStatusChangedHandler"
- "_connectionList"
- "_connectionPropertiesChangedHandler"
- "_connectionPropertyChangeHandlers"
- "_connectionQueue"
- "_constructClientRegistrationInfo"
- "_currentlyConnectedAccessories"
- "_delegate"
- "_delegateForIdentifier"
- "_destinationSharingOptions"
- "_eaClientRegistrationInfo"
- "_endpointDataOutHandlers"
- "_endpointEventHandlerQueue"
- "_endpointList"
- "_endpointPropertiesChangedHandler"
- "_endpointPropertyChangeHandlers"
- "_endpointSecureTunnelDataHandlers"
- "_findAccessoryForPrimaryUUID:"
- "_firmwareRevisionActive"
- "_firmwareRevisionPending"
- "_fullAccessoryInfo"
- "_handleConnectionInterruption"
- "_handleConnectionInvalidation"
- "_hardwareRevision"
- "_identifier"
- "_init"
- "_isClientRegistered"
- "_isMFiCharger"
- "_listLock"
- "_manufacturer"
- "_model"
- "_name"
- "_pluginName"
- "_ppid"
- "_primaryUUID"
- "_productID"
- "_providerUID"
- "_remoteObject"
- "_removeAccessoryForPrimaryUUID:"
- "_removeAllAccessories"
- "_safeRemoteObject"
- "_safeSynchronousRemoteObject"
- "_serial"
- "_serverConnection"
- "_serverConnectionLock"
- "_serverDisconnectedHandler"
- "_transportClient"
- "_transportType"
- "_vendorID"
- "_xpcConnection"
- "accessoryCloseExternalAccessorySession:"
- "accessoryClosedEASession:"
- "accessoryConnectionAttached:type:"
- "accessoryConnectionAttached:type:info:properties:"
- "accessoryConnectionDetached:"
- "accessoryConnectionFiltered:withFilter:"
- "accessoryConnectionInfoPropertyChanged:"
- "accessoryConnectionInfoPropertyChanged:properties:"
- "accessoryConnectionType:"
- "accessoryDictionaryForLogging:"
- "accessoryEndpointAttached:transportType:protocol:forConnection:"
- "accessoryEndpointAttached:transportType:protocol:properties:forConnection:"
- "accessoryEndpointDetached:forConnection:"
- "accessoryEndpointFiltered:withFilter:forConnection:"
- "accessoryEndpointInfoPropertyChanged:forConnection:"
- "accessoryEndpointInfoPropertyChanged:properties:forConnection:"
- "accessoryEndpointProtocolType:connection:"
- "accessoryEndpointTransportType:connection:"
- "accessoryEndpointUpdate:protocol:forConnection:"
- "accessoryEndpointUpdate:protocol:properties:forConnection:"
- "accessoryEndpointsForConnection:withReply:"
- "accessoryFilterDictionary"
- "accessoryInfoForConnection:withReply:"
- "accessoryInfoForConnectionSync:"
- "accessoryInfoForConnectionWithUUID:"
- "accessoryInfoForConnectionWithUUID:withReply:"
- "accessoryInfoForEndpoint:connection:withReply:"
- "accessoryInfoForEndpointSync:connection:"
- "accessoryInfoForEndpointWithUUID:"
- "accessoryInfoForEndpointWithUUID:withReply:"
- "accessoryProperty:forConnection:withReply:"
- "accessoryProperty:forEndpoint:connection:withReply:"
- "accessoryPropertySync:forConnection:"
- "accessoryPropertySync:forEndpoint:connection:"
- "activateLocationForUUID:"
- "activeConnectionUUIDs"
- "addObject:"
- "addObserver:selector:name:object:"
- "addToDictionaryProperty:values:forConnectionWithUUID:"
- "addToDictionaryProperty:values:forConnectionWithUUID:withReply:"
- "addToDictionaryProperty:values:forEndpointWithUUID:"
- "addToDictionaryProperty:values:forEndpointWithUUID:withReply:"
- "allConnectionUUIDs"
- "allEndpointsUUIDs"
- "allKeys"
- "allObjects"
- "anyObject"
- "appendFormat:"
- "appendToArrayProperty:values:forConnectionWithUUID:"
- "appendToArrayProperty:values:forConnectionWithUUID:withReply:"
- "appendToArrayProperty:values:forEndpointWithUUID:"
- "appendToArrayProperty:values:forEndpointWithUUID:withReply:"
- "array"
- "arrayForKey:"
- "arrayWithObjects:count:"
- "authStateDidChange:forConnectionWithUUID:previousAuthState:authType:connectionIsAuthenticated:connectionWasAuthenticated:"
- "authStateForConnectionWithUUID:authType:"
- "authStatusDidChange:forConnectionWithUUID:previousAuthStatus:authType:connectionIsAuthenticated:connectionWasAuthenticated:"
- "authStatusDidChangeHandler:"
- "authStatusForConnectionWithUUID:authType:"
- "authStatusForConnectionWithUUID:authType:withReply:"
- "authenticateBatteryWithChallenge:completionHandler:"
- "authenticateLASWithChallenge:completionHandler:updateRegistry:"
- "authenticateTouchControllerWithChallenge:completionHandler:"
- "authenticateTouchControllerWithChallenge:completionHandler:updateRegistry:"
- "authenticateVeridianWithChallenge:completionHandler:"
- "authenticateVeridianWithChallenge:completionHandler:updateRegistry:updateUIProperty:logToAnalytics:"
- "autorelease"
- "base64EncodedStringWithOptions:"
- "beginUserKeyErase:withReply:"
- "beginVendorKeyErase:withReply:"
- "boolForKey:"
- "boolValue"
- "bundleIdentifier"
- "bundleWithIdentifier:"
- "bytes"
- "cancelUserKeyErase:withReply:"
- "cancelVendorKeyErase:withReply:"
- "carPlayAppLinksStateForCertSerial:withReply:"
- "carPlayIconStateForCertSerial:andAppCategories:withReply:"
- "carPlaySendConnectionTimeEvent:connectionType:eventTime:"
- "carPlaySendConnectionTimeEvent:connectionType:eventTime:withReply:"
- "carPlayStartSessionForConnectionID:properties:"
- "carPlayStartSessionForConnectionID:properties:withReply:"
- "certificateCapabilitiesForConnectionWithUUID:"
- "certificateDataForConnectionWithUUID:"
- "certificateSerialForConnectionWithUUID:"
- "certificateSerialStringForConnectionWithUUID:"
- "characterSetWithCharactersInString:"
- "class"
- "clientCapabilities"
- "clientCloseExternalAccessorySession:"
- "closeExternalAccessorySession:"
- "compare:"
- "componentsJoinedByString:"
- "componentsSeparatedByCharactersInSet:"
- "configStreamCategoriesRequest:connection:"
- "configStreamCategoriesRequest:connection:withReply:"
- "configStreamCategoriesResponse:forEndpoint:connection:success:"
- "configStreamCategoryListReady:connection:"
- "configStreamDelegate"
- "configStreamGetResponseHandler"
- "configStreamPropertyRequest:forCategory:forEndpoint:connection:"
- "configStreamPropertyRequest:forCategory:forEndpoint:connection:withReply:"
- "configStreamPropertyResponse:forCategory:forEndpoint:connection:value:success:"
- "configStreamPropertySetValue:forProperty:forCategory:forEndpoint:connection:"
- "conformsToProtocol:"
- "connectToServer"
- "connectToServer:"
- "connectedThroughAdapter:"
- "connectionAuthStatusChangedHandler"
- "connectionList"
- "connectionPropertiesChangedHandler"
- "connectionPropertiesDidChangeHandler:"
- "connectionPropertyChangeHandlers"
- "connectionQueue"
- "connectionTypeForConnectionWithUUID:"
- "connectionUUIDForEndpointWithUUID:"
- "connectionUUIDForEndpointWithUUID:withReply:"
- "containsObject:"
- "containsString:"
- "continueUserKeyErase:withSignature:andAccessoryNonce:forEndpoint:withReply:"
- "continueVendorKeyErase:withSignature:andAccessoryNonce:forEndpoint:withReply:"
- "copy"
- "copyAccessoryInfo"
- "copyLocalizedAccessoryName:"
- "copyLocalizedAccessoryName:withReply:"
- "copyLocalizedAccessoryNameFromDaemon:"
- "copyUserPrivateKey:withReply:"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createConnectionWithType:andIdentifier:"
- "createConnectionWithType:andIdentifier:withReply:"
- "createEndpointWithTransportType:andProtocol:andIdentifier:andDataOutHandler:forConnectionWithUUID:publishConnection:"
- "createEndpointWithTransportType:andProtocol:andIdentifier:dataOutHandler:forConnectionWithUUID:"
- "createEndpointWithTransportType:andProtocol:andIdentifier:forConnectionWithUUID:publishConnection:"
- "createEndpointWithTransportType:andProtocol:andIdentifier:forConnectionWithUUID:withReply:"
- "createExternalAccessorySessionForProtocol:accessoryUUID:withEASessionReply:"
- "createExternalAccessorySessionForProtocol:accessoryUUID:withReply:"
- "currentCalendar"
- "currentVehicleInfo:"
- "currentlyConnectedAccessories"
- "dataWithBytes:length:"
- "dataWithContentsOfFile:"
- "dataWithJSONObject:options:error:"
- "date"
- "dateFromComponents:"
- "dateWithTimeInterval:sinceDate:"
- "dealloc"
- "debugDescription"
- "defaultCenter"
- "delegate"
- "delegateForIdentifier"
- "description"
- "destinationInformation:forUUID:"
- "destinationSharingOptions"
- "destinationSharingStatus:forDestinationUUID:supportedParams:forUUID:"
- "destroyConnectionWithUUID:"
- "destroyConnectionWithUUID:withReply:"
- "destroyEndpointWithUUID:"
- "destroyEndpointWithUUID:withReply:"
- "dictionaryForKey:"
- "dictionaryWithDictionary:"
- "dictionaryWithObjects:forKeys:count:"
- "doubleForKey:"
- "duration"
- "eaClientRegistrationInfo"
- "enableSecureTunnelDataReceiveHandlerForEndpoint:"
- "endpointDataOutHandlers"
- "endpointEventHandlerQueue"
- "endpointPropertiesChangedHandler"
- "endpointPropertiesDidChangeHandler:"
- "endpointPropertyChangeHandlers"
- "endpointSecureTunnelDataHandlers"
- "endpointUUIDsForConnectionWithUUID:"
- "endpointUUIDsForConnectionWithUUID:withReply:"
- "enqueueLocationNMEASentence:forUUID:withTimestamps:"
- "filterAccessoryInfo:"
- "filterMatchingDigitalCarKeys:forAccessory:withCompletionHandler:"
- "filterMatchingDigitalCarKeys:forAccessory:withReply:"
- "firmwareRevisionActive"
- "firmwareRevisionPending"
- "fullAccessoryInfo"
- "getAccessoryUserName:withReply:"
- "getFilterForClient:"
- "getIconDataForBundleID:forIconSize:withReply:"
- "getInterceptCountForEndpoint:connection:"
- "getInterceptCountForEndpoint:connection:withReply:"
- "getPairingStatus:withReply:"
- "getPrivateNVMKeyValues:forEndpoint:withReply:"
- "getPublicNVMKeyValues:forEndpoint:withReply:"
- "handleIncomingExternalAccessoryData:forEASessionIdentifier:withReply:"
- "handleIncomingNotification:withPayload:aboutAccessory:"
- "handleInterceptData:forEndpoint:connection:"
- "hardwareRevision"
- "hasEAEntitlement"
- "hasEAProtocols"
- "hasEASandbox"
- "hash"
- "hexadecimalCharacterSet"
- "i16@0:8"
- "i24@0:8@16"
- "i28@0:8@16i24"
- "i32@0:8@16@24"
- "identifier"
- "identifierForConnectionWithUUID:"
- "identifierForConnectionWithUUID:withReply:"
- "identifierForEndpointWithUUID:"
- "identifierForEndpointWithUUID:withReply:"
- "init"
- "initConnection:"
- "initConnectionToServer:"
- "initPlugin"
- "initWithAccessoryInfoDictionary:"
- "initWithBase64EncodedString:options:"
- "initWithDelegate:"
- "initWithDelegate:capabilities:"
- "initWithMachServiceName:options:"
- "initWithServiceName:"
- "initWithStartDate:endDate:"
- "initWithSuiteName:"
- "initialEAAccessoriesAttachedAfterClientConnection:"
- "instancesRespondToSelector:"
- "intValue"
- "integerForKey:"
- "integerValue"
- "interceptIncomingNTimes:forEndpoint:connection:"
- "interfaceWithProtocol:"
- "invalidate"
- "invertedSet"
- "isCarPlayPairedWithCertSerial:withReply:"
- "isClientRegistered"
- "isConnectionAuthenticated:"
- "isConnectionAuthenticatedForUUID:withReply:"
- "isEqual:"
- "isEqualToString:"
- "isKindOfClass:"
- "isMFiCharger"
- "isMemberOfClass:"
- "isProxy"
- "isRunning"
- "isValidJSONObject:"
- "isWirelessCarPlayAllowedForCertSerial:withReply:"
- "launchServer"
- "length"
- "listLock"
- "localizedFailureReason"
- "localizedStringForKey:value:table:"
- "lock"
- "mainBundle"
- "manufacturer"
- "model"
- "mutableCopy"
- "name"
- "nmeaSentenceArrived:forAccessoryUUID:withTimestamps:"
- "notifyDelegateOfServerDisconnectAndCleanup"
- "notifyOfClient:bundleID:withFilter:"
- "notifyOfClient:bundleID:withFilter:forIdentifier:"
- "numberWithDouble:"
- "numberWithInt:"
- "numberWithUnsignedLongLong:"
- "objectAtIndexedSubscript:"
- "objectForInfoDictionaryKey:"
- "objectForKey:"
- "objectForKeyedSubscript:"
- "objectsPassingTest:"
- "openSocketForAccessoryToApp:"
- "openSocketForAppToAccessory:"
- "openSocketFromAccessoryToApp:"
- "openSocketFromAppToAccessory:"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "pluginClassAndName"
- "pluginName"
- "postNotificationName:object:userInfo:"
- "ppid"
- "primaryUUID"
- "processIncomingData:forEndpointWithUUID:"
- "processIncomingData:forEndpointWithUUID:withReply:"
- "processOutgoingExternalAccessoryData:forEASessionIdentifier:withReply:"
- "processOutgoingSecureTunnelData:forEndpoint:forType:"
- "productID"
- "propertiesDidChange:forConnectionWithUUID:previousProperties:"
- "propertiesDidChange:forEndpointWithUUID:previousProperties:connectionUUID:"
- "propertiesForConnectionWithUUID:"
- "propertiesForConnectionWithUUID:withReply:"
- "propertiesForEndpointWithUUID:"
- "propertiesForEndpointWithUUID:withReply:"
- "protocolForEndpointWithUUID:"
- "providerUID"
- "provisionAccessoryForFindMy:withReply:"
- "publishConnectionWithUUID:"
- "publishConnectionWithUUID:withReply:"
- "punctuationCharacterSet"
- "raise:format:"
- "received response. authError=%d"
- "receivedSecureTunnelData:forEndpoint:"
- "registerClientInformation:onInstantiation:withReply:"
- "registerDelegate:"
- "registerDelegate:withFilter:"
- "registerDelegate:withIdentifier:"
- "release"
- "remoteObject"
- "remoteObjectProxyWithErrorHandler:"
- "removeAllObjects"
- "removeObject:"
- "removeObjectForKey:"
- "removeObjectsForKeys:"
- "removeObserver:name:object:"
- "removeProperty:forConnectionWithUUID:"
- "removeProperty:forConnectionWithUUID:withReply:"
- "removeProperty:forEndpointWithUUID:"
- "removeProperty:forEndpointWithUUID:withReply:"
- "requestAccessoryWiFiCredentials:"
- "requestAccessoryWifiCredentials:"
- "resetPairingInformation:withReply:"
- "respondsToSelector:"
- "resume"
- "resumeEASessionData:"
- "retain"
- "retainCount"
- "routeOutgoingData:forEndpointWithUUID:connectionUUID:"
- "self"
- "sendData:forEndpoint:connection:"
- "sendDeviceIdentifierNotification:usbIdentifier:forUUID:"
- "sendGPRMCDataStatus:ValueV:ValueX:forAccessoryUUID:"
- "sendGPRMCDataStatus:ValueV:ValueX:forUUID:"
- "sendNMEAFilterList:forAccessoryUUID:"
- "sendNMEAFilterList:forUUID:"
- "sendOutgoingData:forEndpointWithUUID:connectionUUID:"
- "sendOutgoingData:forEndpointWithUUID:connectionUUID:withReply:"
- "sendOutgoingExternalAccessoryData:forEASessionIdentifier:withReply:"
- "sendOutgoingSecureTunnelData:forEndpointWithUUID:forType:withResult:"
- "sendWiredCarPlayAvailable:usbIdentifier:wirelessAvailable:bluetoothIdentifier:forUUID:"
- "sendWiredCarPlayAvailable:usbIdentifier:wirelessAvailable:bluetoothIdentifier:themeAssetsAvailable:forUUID:"
- "serial"
- "serverConnection"
- "serverConnectionLock"
- "serverDisconnectedHandler"
- "setAccessoryInfo:forEndpointWithUUID:"
- "setAccessoryInfo:forEndpointWithUUID:withReply:"
- "setAccessoryUserName:forEndpoint:withReply:"
- "setActiveConnectionUUIDs:"
- "setAuthenticationStatus:andCertificateData:authCTA:forConnectionWithUUID:"
- "setBool:forKey:"
- "setClientCapabilities:"
- "setConfigStreamDelegate:"
- "setConfigStreamGetResponseHandler:"
- "setConnectionAuthStatusChangedHandler:"
- "setConnectionAuthenticated:state:"
- "setConnectionList:"
- "setConnectionPropertiesChangedHandler:"
- "setConnectionPropertyChangeHandlers:"
- "setConnectionQueue:"
- "setCurrentlyConnectedAccessories:"
- "setDay:"
- "setDelegate:"
- "setDelegateForIdentifier:"
- "setDestinationSharingOptions:"
- "setDouble:forKey:"
- "setEaClientRegistrationInfo:"
- "setEndpointDataOutHandlers:"
- "setEndpointEventHandlerQueue:"
- "setEndpointList:"
- "setEndpointPropertiesChangedHandler:"
- "setEndpointPropertyChangeHandlers:"
- "setEndpointSecureTunnelDataHandlers:"
- "setExportedInterface:"
- "setExportedObject:"
- "setFirmwareRevisionActive:"
- "setFirmwareRevisionPending:"
- "setFullAccessoryInfo:"
- "setHandler:forConnectionProperty:"
- "setHandler:forEndpointProperty:"
- "setHardwareRevision:"
- "setIdentifier:"
- "setInteger:forKey:"
- "setInterruptionHandler:"
- "setInvalidationHandler:"
- "setIsClientRegistered:"
- "setIsMFiCharger:"
- "setListLock:"
- "setManufacturer:"
- "setModel:"
- "setMonth:"
- "setName:"
- "setObject:forKey:"
- "setPpid:"
- "setPrimaryUUID:"
- "setPrivateNVMKeyValues:forEndpoint:withReply:"
- "setProductID:"
- "setProperties:forConnectionWithUUID:"
- "setProperties:forConnectionWithUUID:withReply:"
- "setProperties:forEndpointWithUUID:"
- "setProperties:forEndpointWithUUID:withReply:"
- "setProperty:value:forConnectionWithUUID:"
- "setProperty:value:forEndpointWithUUID:"
- "setProviderUID:"
- "setPublicNVMKeyValues:forEndpoint:withReply:"
- "setRemoteObject:"
- "setRemoteObjectInterface:"
- "setSecureTunnelDataReceiveHandler:forEndpoint:"
- "setSerial:"
- "setServerConnection:"
- "setServerConnectionLock:"
- "setServerDisconnectedHandler:"
- "setSupervisedTransportsRestricted:forConnectionWithUUID:"
- "setTransportClient:"
- "setTransportType:"
- "setVendorID:"
- "setWithArray:"
- "setWithSet:"
- "setXpcConnection:"
- "setYear:"
- "sharedBridge"
- "sharedClient"
- "sharedDefaults"
- "sharedDefaultsIapd"
- "sharedDefaultsLogging"
- "sharedInstance"
- "sharedManager"
- "signVeridianChallenge:completionHandler:"
- "startDestinationSharingForUUID:"
- "startDestinationSharingForUUID:options:"
- "startLocationInformationForAccessoryUUID:"
- "startPlugin"
- "startSafeConnectionTransaction"
- "stopDestinationSharingForUUID:"
- "stopLocationForUUID:"
- "stopLocationInformationForAccessoryUUID:"
- "stopPlugin"
- "stopSafeConnectionTransaction"
- "stringByTrimmingCharactersInSet:"
- "stringForKey:"
- "stringWithCString:encoding:"
- "stringWithFormat:"
- "stringWithString:"
- "superclass"
- "synchronousRemoteObjectProxyWithErrorHandler:"
- "timeIntervalSince1970"
- "timeIntervalSinceReferenceDate"
- "transportClient"
- "transportClient:authStatusDidChange:forConnectionWithUUID:"
- "transportClient:propertiesDidChange:forConnectionWithUUID:previousProperties:"
- "transportClient:propertiesDidChange:forEndpointWithUUID:previousProperties:connectionUUID:"
- "transportClientServerDisconnected:"
- "transportTypeForEndpointWithUUID:"
- "unlock"
- "unsignedIntValue"
- "updateAccessoryInfo:"
- "updateAccessoryInfo:forUUID:"
- "userInfo"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"ACCTransportClient\"16"
- "v24@0:8@\"NSDictionary\"16"
- "v24@0:8@\"NSString\"16"
- "v24@0:8@16"
- "v24@0:8@?16"
- "v24@0:8@?<v@?B>16"
- "v24@0:8Q16"
- "v28@0:8@\"NSString\"16B24"
- "v28@0:8@16B24"
- "v28@0:8I16@20"
- "v32@0:8@\"NSArray\"16@\"NSString\"24"
- "v32@0:8@\"NSData\"16@\"NSString\"24"
- "v32@0:8@\"NSData\"16@?<v@?@\"NSData\"@\"NSData\"i>24"
- "v32@0:8@\"NSData\"16@?<v@?B>24"
- "v32@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24"
- "v32@0:8@\"NSData\"16@?<v@?Q>24"
- "v32@0:8@\"NSData\"16@?<v@?i>24"
- "v32@0:8@\"NSDictionary\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16@\"NSDictionary\"24"
- "v32@0:8@\"NSString\"16@\"NSString\"24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSData\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSString\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSArray\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSDictionary\">24"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSError\">24"
- "v32@0:8@\"NSString\"16@?<v@?B>24"
- "v32@0:8@\"NSString\"16@?<v@?i@\"NSError\">24"
- "v32@0:8@\"NSString\"16Q24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v32@0:8@16Q24"
- "v32@0:8@?16@24"
- "v36@0:8@\"ACCTransportClient\"16B24@\"NSString\"28"
- "v36@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24B32"
- "v36@0:8@\"NSDictionary\"16B24@?<v@?B@\"NSArray\">28"
- "v36@0:8@\"NSString\"16i24@?<v@?i>28"
- "v36@0:8@16@?24B32"
- "v36@0:8@16B24@28"
- "v36@0:8@16B24@?28"
- "v36@0:8@16i24@?28"
- "v36@0:8B16B20B24@\"NSString\"28"
- "v36@0:8B16B20B24@28"
- "v36@0:8I16@\"NSDictionary\"20@?<v@?B@\"NSError\">28"
- "v36@0:8I16@20@?28"
- "v36@0:8i16@\"NSString\"20@\"NSString\"28"
- "v36@0:8i16@\"NSString\"20@?<v@?B@\"NSString\">28"
- "v36@0:8i16@20@28"
- "v36@0:8i16@20@?28"
- "v40@0:8@\"NSArray\"16@\"NSString\"24@?<v@?@\"NSArray\"@\"NSError\">32"
- "v40@0:8@\"NSArray\"16@\"NSString\"24@?<v@?@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32"
- "v40@0:8@\"NSData\"16@\"NSString\"24@?<v@?B>32"
- "v40@0:8@\"NSData\"16Q24@?<v@?@\"NSArray\">32"
- "v40@0:8@\"NSDictionary\"16@\"NSString\"24@\"NSDictionary\"32"
- "v40@0:8@\"NSDictionary\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSDictionary\"16@\"NSString\"24@?<v@?B>32"
- "v40@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSDictionary\"32"
- "v40@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSString\"32"
- "v40@0:8@\"NSString\"16@\"NSNumber\"24@?<v@?B>32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@\"NSArray\"32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSError\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSString\"@\"NSString\"@\"NSDictionary\">32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSString\"@\"NSString\"@>32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?@\"NSString\"@\"NSString\"i>32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?B>32"
- "v40@0:8@\"NSString\"16@\"NSString\"24@?<v@?BBQ@\"NSString\">32"
- "v40@0:8@\"NSString\"16d24@?<v@?@\"NSData\">32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16Q24@?32"
- "v40@0:8@16d24@?32"
- "v40@0:8C16S20@\"NSString\"24@\"NSString\"32"
- "v40@0:8C16S20@24@32"
- "v40@0:8q16q24@32"
- "v44@0:8@\"NSData\"16@\"NSString\"24S32@?<v@?B>36"
- "v44@0:8@\"NSData\"16@?<v@?B@\"NSData\"@\"NSData\"Bi>24B32B36B40"
- "v44@0:8@\"NSDictionary\"16@\"NSString\"24@\"NSString\"32B40"
- "v44@0:8@\"NSString\"16i24@\"NSDictionary\"28@\"NSDictionary\"36"
- "v44@0:8@\"NSString\"16i24@\"NSDictionary\"28@\"NSString\"36"
- "v44@0:8@16@24@32B40"
- "v44@0:8@16@24S32@?36"
- "v44@0:8@16@?24B32B36B40"
- "v44@0:8@16i24@28@36"
- "v44@0:8B16@\"NSString\"20@\"NSArray\"28@\"NSString\"36"
- "v44@0:8B16@20@28@36"
- "v44@0:8i16@\"NSString\"20i28i32B36B40"
- "v44@0:8i16@20i28i32B36B40"
- "v48@0:8@\"ACCTransportClient\"16@\"NSDictionary\"24@\"NSString\"32@\"NSDictionary\"40"
- "v48@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@?<v@?B>40"
- "v48@0:8@\"NSData\"16C24S28@\"NSString\"32@\"NSString\"40"
- "v48@0:8@\"NSDictionary\"16@\"NSString\"24@\"NSDictionary\"32@\"NSString\"40"
- "v48@0:8@\"NSString\"16@\"NSArray\"24@\"NSString\"32@?<v@?B>40"
- "v48@0:8@\"NSString\"16@\"NSDictionary\"24@\"NSString\"32@?<v@?B>40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSDictionary\"32@\"NSString\"40"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSString\"@\"NSString\"@\"NSString\"@>40"
- "v48@0:8@\"NSString\"16i24i28@\"NSDictionary\"32@\"NSString\"40"
- "v48@0:8@16@24@32@40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16C24S28@32@40"
- "v48@0:8@16i24i28@32@40"
- "v48@0:8Q16Q24@\"NSDate\"32@?<v@?B@\"NSError\">40"
- "v48@0:8Q16Q24@32@?40"
- "v48@0:8i16i20@\"NSString\"24@\"NSString\"32@?<v@?B@\"NSString\">40"
- "v48@0:8i16i20@24@32@?40"
- "v52@0:8C16S20@\"NSString\"24@\"NSString\"32@\"NSData\"40B48"
- "v52@0:8C16S20@24@32@40B48"
- "v56@0:8@\"ACCTransportClient\"16@\"NSDictionary\"24@\"NSString\"32@\"NSDictionary\"40@\"NSString\"48"
- "v56@0:8@\"NSData\"16@\"NSData\"24@\"NSData\"32@\"NSString\"40@?<v@?@\"NSError\">48"
- "v56@0:8@\"NSNumber\"16@\"NSString\"24@\"NSNumber\"32@\"NSString\"40@\"NSString\"48"
- "v56@0:8@16@24@32@40@48"
- "v56@0:8@16@24@32@40@?48"
- "v64@0:8@\"NSNumber\"16@\"NSString\"24@\"NSNumber\"32@\"NSString\"40@\"NSNumber\"48@\"NSString\"56"
- "v64@0:8@16@24@32@40@48@56"
- "vehicleInformationForUUID:withReply:"
- "vehicleStatusUpdate:forAccessoryUUID:"
- "vehicleStatusUpdate:forUUID:"
- "vendorID"
- "verifyAccessoryConnectionStatus:legacyConnectionID:withReply:"
- "verifyBatteryMatch:completionHandler:"
- "verifying battery match using cert %@"
- "whitespaceAndNewlineCharacterSet"
- "writeToFile:atomically:"
- "xpcConnection"
- "zone"

```
