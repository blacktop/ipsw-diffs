## passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

-  __TEXT.__text: 0x59a468
+  __TEXT.__text: 0x59ad14
   __TEXT.__auth_stubs: 0x5c60
-  __TEXT.__objc_stubs: 0x717c0
-  __TEXT.__objc_methlist: 0x35914
+  __TEXT.__objc_stubs: 0x71800
+  __TEXT.__objc_methlist: 0x3592c
   __TEXT.__const: 0x4018
-  __TEXT.__cstring: 0x64d94
+  __TEXT.__cstring: 0x64df4
   __TEXT.__objc_classname: 0x7c08
-  __TEXT.__objc_methtype: 0x13d22
-  __TEXT.__gcc_except_tab: 0x7d64
-  __TEXT.__objc_methname: 0xa104c
-  __TEXT.__oslogstring: 0x50abb
+  __TEXT.__objc_methtype: 0x13d02
+  __TEXT.__gcc_except_tab: 0x7d6c
+  __TEXT.__objc_methname: 0xa115c
+  __TEXT.__oslogstring: 0x50bdb
   __TEXT.__ustring: 0x10
   __TEXT.__swift5_typeref: 0x2184
   __TEXT.__constg_swiftt: 0x1934

   __TEXT.__swift_as_cont: 0x3c
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_mpenum: 0x38
-  __TEXT.__unwind_info: 0x12618
+  __TEXT.__unwind_info: 0x12628
   __TEXT.__eh_frame: 0xff0
-  __DATA_CONST.__const: 0x2e210
-  __DATA_CONST.__cfstring: 0x32880
+  __DATA_CONST.__const: 0x2e230
+  __DATA_CONST.__cfstring: 0x328e0
   __DATA_CONST.__objc_classlist: 0x19c8
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x5d8

   __DATA_CONST.__objc_arrayobj: 0x558
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__auth_got: 0x2e40
-  __DATA_CONST.__got: 0x3508
+  __DATA_CONST.__got: 0x39e0
   __DATA_CONST.__auth_ptr: 0x6a8
-  __DATA.__objc_const: 0x41df0
-  __DATA.__objc_selrefs: 0x1f730
-  __DATA.__objc_ivar: 0x288c
+  __DATA.__objc_const: 0x41e58
+  __DATA.__objc_selrefs: 0x1f738
+  __DATA.__objc_ivar: 0x2898
   __DATA.__objc_data: 0x115a0
   __DATA.__data: 0x5f10
   __DATA.__bss: 0x38b0

   - /System/Library/PrivateFrameworks/CascadeSets.framework/Versions/A/CascadeSets
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreCDP.framework/Versions/A/CoreCDP
+  - /System/Library/PrivateFrameworks/CoreSuggestions.framework/Versions/A/CoreSuggestions
   - /System/Library/PrivateFrameworks/CoreUtils.framework/Versions/A/CoreUtils
   - /System/Library/PrivateFrameworks/FamilyCircle.framework/Versions/A/FamilyCircle
   - /System/Library/PrivateFrameworks/FinanceDaemon.framework/Versions/A/FinanceDaemon

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 27211
-  Symbols:   3367
-  CStrings:  41270
+  Functions: 27215
+  Symbols:   3362
+  CStrings:  41287
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA.__bss : content changed
~ __DATA.__common : content changed
Symbols:
+ _CFPreferencesCopyAppValue
- _$ss5NeverON
- _$ss5NeverOs5ErrorsWP
- _OBJC_CLASS_$_FKTrillianTransactionImporter
- _OBJC_CLASS_$_PKContent
- _OBJC_CLASS_$_PKWebServiceDocumentDeliveryFeature
- _PKDocumentDeliveryEnabled
CStrings:
+ "AppCanShowSiriSuggestionsBlacklist"
+ "CONTINUITY_PROVISIONING_PROMPT_NOTIFICATION_BODY_DEVICE_NAME"
+ "Client is not entitled to add passes"
+ "Coalescing delivered-notifications completions: %lu pending"
+ "Migrating database from user_version 26061 to 26062"
+ "Synchronized delivered-notifications. Running %lu completions"
+ "Synchronizing delivered-notifications..."
+ "T@\"PKContinuityProximityCBAdvertisement\",R,N,V_advertisement"
+ "TB,N,V_useGenericMessaging"
+ "Updating past due notification (%@) Mini-Miranda generic messaging flag (from:%d to:%d)"
+ "_isEntitledForSiriSuggestions"
+ "_isSyncingDeliveredNotifications"
+ "_migrateFrom26061To26062:context:"
+ "_pendingDeliveredNotificationCompletions"
+ "_syncDeliveredNotificationsLock"
+ "com.apple.suggestions"
+ "existingPendingProvisioningAccess"
+ "initWithGroupsBySessionIdentifier:destinationDeviceType:destinationDeviceName:selectedCredentialCount:"
+ "passesAdd"
+ "posterGeneric"
+ "setSecureElementIdentifiers:"
+ "setUseGenericMessaging:"
+ "siriSuggestionsAccess"
+ "updatePastDueNotificationWithAccount:userNotification:"
+ "v20@?0B8@\"PKAccount\"12"
+ "\xc1"
- "-[PDPaymentService addPendingProvisioning:]"
- "DocumentDelivery"
- "Inserting pending transaction registration"
- "_insertPendingTransactionRegistration:"
- "addPendingProvisioning:"
- "createWithFileURL:dataTypeIdentifier:"
- "fkPaymentTransaction"
- "initWithGroupsBySessionIdentifier:destinationDeviceType:destinationDeviceName:"
- "isEnabledWithWebService:"
- "registerPaymentTransaction:"
- "second"
- "v24@0:8@\"PKPendingProvisioning\"16"

```
