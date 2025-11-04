## SetupAssistant

> `/System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant`

```diff

-5380.0.0.0.0
-  __TEXT.__text: 0x455d8
+5381.1.2.0.0
+  __TEXT.__text: 0x456a8
   __TEXT.__auth_stubs: 0xd80
   __TEXT.__objc_methlist: 0x4124
   __TEXT.__const: 0x138
   __TEXT.__gcc_except_tab: 0x1158
   __TEXT.__oslogstring: 0x58e9
-  __TEXT.__cstring: 0x3032
+  __TEXT.__cstring: 0x309c
   __TEXT.__dlopen_cstrs: 0x138b
   __TEXT.__ustring: 0x12
   __TEXT.__unwind_info: 0x1338

   __DATA_CONST.__objc_arraydata: 0x178
   __AUTH_CONST.__auth_got: 0x6d0
   __AUTH_CONST.__const: 0xaa0
-  __AUTH_CONST.__cfstring: 0x36e0
+  __AUTH_CONST.__cfstring: 0x3740
   __AUTH_CONST.__objc_const: 0x61c0
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x60

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 9A8FFDB7-4E12-30DB-B6B4-E143D9C674C2
+  UUID: 7D98056A-321E-39D3-BDBB-B68F5FC23625
   Functions: 1772
   Symbols:   6499
-  CStrings:  3644
+  CStrings:  3650
 
Symbols:
+ _BYFlowSkipIdentifierAppleIntelligence
+ ___42-[BYFlowSkipController registerActivities]_block_invoke.125
+ ___42-[BYFlowSkipController registerActivities]_block_invoke_2.126
+ ___42-[BYFlowSkipController registerActivities]_block_invoke_2.126.cold.1
+ ___84-[BYFlowSkipController _registerWiFiObserverActivityWithNeedsActivity:handlerQueue:]_block_invoke.117
+ ___block_literal_global.121
+ ___block_literal_global.38
- _BYPrivacySubscriptionBundleIdentifier
- ___42-[BYFlowSkipController registerActivities]_block_invoke.113
- ___42-[BYFlowSkipController registerActivities]_block_invoke_2.114
- ___42-[BYFlowSkipController registerActivities]_block_invoke_2.114.cold.1
- ___84-[BYFlowSkipController _registerWiFiObserverActivityWithNeedsActivity:handlerQueue:]_block_invoke.105
Functions:
~ ___45+[BYFlowSkipController _supportedIdentifiers]_block_invoke : 212 -> 224
~ -[BYFlowSkipController _postFollowUpItemForFlowSkipIdentifiers:previousFollowUpItem:forceNotification:] : 1680 -> 1856
~ -[BYFlowSkipController revisePendingFollowUpsForcingRepost:] : 1416 -> 1436
CStrings:
+ "FOLLOWUP_DETAIL_APPLE_INTELLIGENCE_EXCLUSIVE"
+ "FOLLOWUP_DETAIL_FACEID_APPLEINTELLIGENCE"
+ "FOLLOWUP_DETAIL_TOUCHID_APPLEINTELLIGENCE"
+ "appleIntelligence"
- "com.apple.onboarding.subscriptionbundle"

```
