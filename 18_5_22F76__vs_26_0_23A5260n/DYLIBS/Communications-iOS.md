## Communications-iOS

> `/System/Library/CoreAccessories/PlugIns/Features/Communications-iOS.feature/Communications-iOS`

```diff

-1043.120.6.0.0
+1110.0.0.0.1
   __TEXT.__text: 0xba88
   __TEXT.__auth_stubs: 0x610
   __TEXT.__objc_methlist: 0x5b4
-  __TEXT.__cstring: 0xa0b
+  __TEXT.__cstring: 0xa74
   __TEXT.__const: 0x7c
   __TEXT.__oslogstring: 0xca4
   __TEXT.__ustring: 0xa

   __TEXT.__objc_methtype: 0x272
   __TEXT.__objc_stubs: 0x1a60
   __DATA_CONST.__got: 0x438
-  __DATA_CONST.__const: 0x770
+  __DATA_CONST.__const: 0x7b0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x40

   __DATA_CONST.__objc_arraydata: 0x20
   __AUTH_CONST.__auth_got: 0x318
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0xde0
+  __AUTH_CONST.__cfstring: 0xe60
   __AUTH_CONST.__objc_const: 0x5b0
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x30

   __DATA.__bss: 0x38
   __DATA_DIRTY.__objc_data: 0x50
   __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__common: 0xc
+  __DATA_DIRTY.__common: 0x10
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/ContactsUI.framework/ContactsUI

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A94EC1A0-C0EA-39CF-B213-88712424993B
+  UUID: 6130ED0D-DB4D-32C6-8031-B25AC89429CD
   Functions: 208
-  Symbols:   1208
-  CStrings:  626
+  Symbols:   1216
+  CStrings:  634
 
Symbols:
+ _ACCUserDefaultsAccessorydDomain
+ _ACCUserDefaultsKey_DisableAuthFailureTTRForXR
+ _ACCUserDefaultsKey_DisableInductiveAuthTTR
+ _ACCUserDefaultsKey_SysdiagnoseOnInductiveCTAFailure
+ ___58-[ACCCommunicationsFeaturePlugin addNotificationObservers]_block_invoke.45
+ ___59-[ACCCommunicationsFeaturePlugin sendDTMF:forCallWithUUID:]_block_invoke.93
+ ___59-[ACCCommunicationsFeaturePlugin sendDTMF:forCallWithUUID:]_block_invoke.93.cold.1
+ ___59-[ACCCommunicationsFeaturePlugin sendDTMF:forCallWithUUID:]_block_invoke.93.cold.2
+ ___61-[ACCCommunicationsFeaturePlugin endCallWithAction:callUUID:]_block_invoke.91
+ ___61-[ACCCommunicationsFeaturePlugin endCallWithAction:callUUID:]_block_invoke.91.cold.1
+ ___61-[ACCCommunicationsFeaturePlugin endCallWithAction:callUUID:]_block_invoke.91.cold.2
+ ___61-[ACCCommunicationsFeaturePlugin endCallWithAction:callUUID:]_block_invoke.91.cold.3
+ ___61-[ACCCommunicationsFeaturePlugin endCallWithAction:callUUID:]_block_invoke.91.cold.4
+ ___61-[ACCCommunicationsFeaturePlugin removeNotificationObservers]_block_invoke.54
+ ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.90
+ ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.90.cold.1
+ ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.90.cold.10
+ ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.90.cold.11
+ ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.90.cold.2
+ ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.90.cold.3
+ ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.90.cold.4
+ ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.90.cold.5
+ ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.90.cold.6
+ ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.90.cold.7
+ ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.90.cold.8
+ ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.90.cold.9
+ ___67-[ACCCommunicationsFeaturePlugin updateHoldStatus:forCallWithUUID:]_block_invoke.92
+ ___67-[ACCCommunicationsFeaturePlugin updateHoldStatus:forCallWithUUID:]_block_invoke.92.cold.1
+ ___block_literal_global.286
+ ___block_literal_global.288
+ ___block_literal_global.47
+ ___block_literal_global.56
+ _kCFACCUserDefaultsAccessorydDomain
+ _kCFACCUserDefaultsKey_DisableAuthFailureTTRForXR
+ _kCFACCUserDefaultsKey_DisableInductiveAuthTTR
+ _kCFACCUserDefaultsKey_SysdiagnoseOnInductiveCTAFailure
- ___58-[ACCCommunicationsFeaturePlugin addNotificationObservers]_block_invoke.27
- ___59-[ACCCommunicationsFeaturePlugin sendDTMF:forCallWithUUID:]_block_invoke.75
- ___59-[ACCCommunicationsFeaturePlugin sendDTMF:forCallWithUUID:]_block_invoke.75.cold.1
- ___59-[ACCCommunicationsFeaturePlugin sendDTMF:forCallWithUUID:]_block_invoke.75.cold.2
- ___61-[ACCCommunicationsFeaturePlugin endCallWithAction:callUUID:]_block_invoke.73
- ___61-[ACCCommunicationsFeaturePlugin endCallWithAction:callUUID:]_block_invoke.73.cold.1
- ___61-[ACCCommunicationsFeaturePlugin endCallWithAction:callUUID:]_block_invoke.73.cold.2
- ___61-[ACCCommunicationsFeaturePlugin endCallWithAction:callUUID:]_block_invoke.73.cold.3
- ___61-[ACCCommunicationsFeaturePlugin endCallWithAction:callUUID:]_block_invoke.73.cold.4
- ___61-[ACCCommunicationsFeaturePlugin removeNotificationObservers]_block_invoke.36
- ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.72
- ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.72.cold.1
- ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.72.cold.10
- ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.72.cold.11
- ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.72.cold.2
- ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.72.cold.3
- ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.72.cold.4
- ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.72.cold.5
- ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.72.cold.6
- ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.72.cold.7
- ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.72.cold.8
- ___64-[ACCCommunicationsFeaturePlugin acceptCallWithAction:callUUID:]_block_invoke.72.cold.9
- ___67-[ACCCommunicationsFeaturePlugin updateHoldStatus:forCallWithUUID:]_block_invoke.74
- ___67-[ACCCommunicationsFeaturePlugin updateHoldStatus:forCallWithUUID:]_block_invoke.74.cold.1
- ___block_literal_global.274
- ___block_literal_global.276
- ___block_literal_global.29
- ___block_literal_global.38
CStrings:
+ "DisableAuthFailureTTRForXR"
+ "DisableInductiveAuthTTR"
+ "SysdiagnoseOnInductiveCTAFailure"
+ "com.apple.accessoryd"

```
