## passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

-  __TEXT.__text: 0x60e550
-  __TEXT.__auth_stubs: 0x7880
-  __TEXT.__objc_stubs: 0x77e60
-  __TEXT.__objc_methlist: 0x36ecc
+  __TEXT.__text: 0x60eca8
+  __TEXT.__auth_stubs: 0x7890
+  __TEXT.__objc_stubs: 0x77ea0
+  __TEXT.__objc_methlist: 0x36edc
   __TEXT.__const: 0x5f28
-  __TEXT.__cstring: 0x68b94
+  __TEXT.__cstring: 0x68bf4
   __TEXT.__objc_classname: 0x8158
-  __TEXT.__objc_methtype: 0x14e42
-  __TEXT.__gcc_except_tab: 0x90cc
-  __TEXT.__objc_methname: 0xa835c
-  __TEXT.__oslogstring: 0x5b92b
+  __TEXT.__objc_methtype: 0x14e22
+  __TEXT.__gcc_except_tab: 0x90d8
+  __TEXT.__objc_methname: 0xa84ac
+  __TEXT.__oslogstring: 0x5ba2b
   __TEXT.__ustring: 0x10
   __TEXT.__swift5_typeref: 0x4130
   __TEXT.__constg_swiftt: 0x24cc

   __TEXT.__swift_as_cont: 0x19c
   __TEXT.__swift5_protos: 0x34
   __TEXT.__swift5_mpenum: 0x40
-  __TEXT.__unwind_info: 0x14568
+  __TEXT.__unwind_info: 0x14570
   __TEXT.__eh_frame: 0x3438
-  __DATA_CONST.__const: 0x32a58
-  __DATA_CONST.__cfstring: 0x354c0
+  __DATA_CONST.__const: 0x32a78
+  __DATA_CONST.__cfstring: 0x35520
   __DATA_CONST.__objc_classlist: 0x1a88
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x658

   __DATA_CONST.__objc_dictobj: 0x2a8
   __DATA_CONST.__objc_arrayobj: 0x6a8
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA_CONST.__auth_got: 0x3c50
-  __DATA_CONST.__got: 0x4378
+  __DATA_CONST.__auth_got: 0x3c58
+  __DATA_CONST.__got: 0x4890
   __DATA_CONST.__auth_ptr: 0xa40
-  __DATA.__objc_const: 0x45070
-  __DATA.__objc_selrefs: 0x20d88
-  __DATA.__objc_ivar: 0x2b1c
+  __DATA.__objc_const: 0x450d8
+  __DATA.__objc_selrefs: 0x20d90
+  __DATA.__objc_ivar: 0x2b28
   __DATA.__objc_data: 0x122a0
   __DATA.__data: 0x7d30
   __DATA.__bss: 0x46b0

   - /System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred
   - /System/Library/PrivateFrameworks/CoreIDV.framework/CoreIDV
   - /System/Library/PrivateFrameworks/CoreODI.framework/CoreODI
+  - /System/Library/PrivateFrameworks/CoreSuggestions.framework/CoreSuggestions
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle
   - /System/Library/PrivateFrameworks/FinanceDaemon.framework/FinanceDaemon

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 29682
-  Symbols:   4319
-  CStrings:  43835
+  Functions: 29686
+  Symbols:   4317
+  CStrings:  43851
 
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
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
~ __DATA.__bss : content changed
~ __DATA.__common : content changed
Symbols:
+ _CFPreferencesCopyAppValue
+ _PKAppleCardUpcomingTransactionsEnabled
- _OBJC_CLASS_$_FKTrillianTransactionImporter
- _OBJC_CLASS_$_PKContent
- _OBJC_CLASS_$_PKWebServiceDocumentDeliveryFeature
- _PKDocumentDeliveryEnabled
CStrings:
+ "AppCanShowSiriSuggestionsBlacklist"
+ "CONTINUITY_PROVISIONING_PROMPT_NOTIFICATION_BODY_DEVICE_NAME"
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
- "initWithGroupsBySessionIdentifier:destinationDeviceType:destinationDeviceName:"
- "isEnabledWithWebService:"
- "registerPaymentTransaction:"
- "second"
- "v24@0:8@\"PKPendingProvisioning\"16"

```
