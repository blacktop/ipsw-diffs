## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-525.125.2.1.0
-  __TEXT.__text: 0x176640
-  __TEXT.__auth_stubs: 0xb90
-  __TEXT.__objc_methlist: 0xda04
+525.126.1.1.0
+  __TEXT.__text: 0x176c74
+  __TEXT.__auth_stubs: 0xbc0
+  __TEXT.__objc_methlist: 0xda2c
   __TEXT.__const: 0x69c8
-  __TEXT.__cstring: 0xf19c
-  __TEXT.__oslogstring: 0x11785
-  __TEXT.__gcc_except_tab: 0x9a7c
+  __TEXT.__cstring: 0xf208
+  __TEXT.__oslogstring: 0x1189f
+  __TEXT.__gcc_except_tab: 0x9ab8
   __TEXT.__dlopen_cstrs: 0x305
   __TEXT.__ustring: 0x1b8
   __TEXT.__unwind_info: 0x4008
   __TEXT.__objc_classname: 0x1c33
-  __TEXT.__objc_methname: 0x21e45
-  __TEXT.__objc_methtype: 0x4639
-  __TEXT.__objc_stubs: 0xf660
+  __TEXT.__objc_methname: 0x21ee3
+  __TEXT.__objc_methtype: 0x4655
+  __TEXT.__objc_stubs: 0xf620
   __DATA_CONST.__got: 0xa38
-  __DATA_CONST.__const: 0x9ff8
+  __DATA_CONST.__const: 0xa018
   __DATA_CONST.__objc_classlist: 0x628
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x208
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6ef0
+  __DATA_CONST.__objc_selrefs: 0x6f08
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0x3e0
   __DATA_CONST.__objc_arraydata: 0x2c8
-  __AUTH_CONST.__auth_got: 0x5d8
+  __AUTH_CONST.__auth_got: 0x5f0
   __AUTH_CONST.__const: 0x1320
-  __AUTH_CONST.__cfstring: 0xf7a0
-  __AUTH_CONST.__objc_const: 0x25210
+  __AUTH_CONST.__cfstring: 0xf820
+  __AUTH_CONST.__objc_const: 0x25240
   __AUTH_CONST.__objc_intobj: 0x2d0
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x3e8
-  __AUTH.__objc_data: 0x2670
-  __DATA.__objc_ivar: 0xfc4
+  __AUTH.__objc_data: 0x28a0
+  __DATA.__objc_ivar: 0xfc8
   __DATA.__data: 0x1900
   __DATA.__bss: 0x6c8
-  __DATA_DIRTY.__objc_data: 0x1720
+  __DATA_DIRTY.__objc_data: 0x14f0
   __DATA_DIRTY.__bss: 0x2a0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0219D278-D2E9-34D4-8E72-22ADB3B24ED4
-  Functions: 5303
-  Symbols:   20153
-  CStrings:  11630
+  UUID: 128B9771-125E-31C4-84D3-7D6B91A9827A
+  Functions: 5306
+  Symbols:   20165
+  CStrings:  11655
 
Symbols:
+ +[AKSecurityHelper secItemAddWithQuery:result:]
+ +[AKSecurityHelper secItemCopyMatchingWithQuery:result:]
+ +[AKSecurityHelper secItemDeleteWithQuery:]
+ -[AKFeatureManager isAgeAssuranceEnabled]
+ _AKAppleIDSetupUIServiceBundleID
+ _AKAppleIDSetupUIServiceClassName
+ _AKFollowUpExtensionTypeThreatNotification
+ _AKFollowUpGroupIdentifierAccount
+ _AKFollowUpGroupIdentifierNoGroup
+ _AKFollowUpPayloadGroupIdKey
+ _AKFollowUpThreatNotificationPushIdentifier
+ _OBJC_IVAR_$_AKFeatureManager._cachedAgeAssuranceEnabled
+ _SecItemAdd
+ _SecItemCopyMatching
+ _SecItemDelete
- -[AKFollowUpFactoryImpl _uniqueIdentifierFromPayload:]
- _AKFollowUpThreatNotificationIdMSExtensionType
- _AKFollowUpThreatNotificationIdMSIdentifier
- _AKFollowUpThreatNotificationIdentifier
- _objc_msgSend$_uniqueIdentifierFromPayload:
- _objc_msgSend$isThreatNotificationCFUEnabled
CStrings:
+ "AgeAssurance"
+ "AppleIDSetupUIService.SetupAlertViewController"
+ "Failed to save account after setting safety screen seen property: %@"
+ "Feature AgeAssurance enabled - %@"
+ "SecItemAdd failed with status: %d"
+ "SecItemAdd with query: %@"
+ "SecItemCopyMatching failed with status: %d"
+ "SecItemCopyMatching with query: %@"
+ "SecItemDelete failed with status: %d"
+ "SecItemDelete with query: %@"
+ "Successfully saved account with safety screen seen property: %@"
+ "TB,R,N,GisAgeAssuranceEnabled"
+ "_cachedAgeAssuranceEnabled"
+ "ageAssuranceEnabled"
+ "com.apple.AppleIDSetupUIService"
+ "groupId"
+ "i24@0:8@16"
+ "i32@0:8@16r^^v24"
+ "isAgeAssuranceEnabled"
+ "noGroup"
+ "secItemAddWithQuery:result:"
+ "secItemCopyMatchingWithQuery:result:"
+ "secItemDeleteWithQuery:"
- "Excluding threat notification follow up from returned items because it is not supported."
- "_uniqueIdentifierFromPayload:"

```
