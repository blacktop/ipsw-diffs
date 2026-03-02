## passd

> `/System/Library/PrivateFrameworks/PassKitCore.framework/passd`

```diff

-1642.5.14.3.0
-  __TEXT.__text: 0x616f7c
-  __TEXT.__auth_stubs: 0x6f30
-  __TEXT.__objc_stubs: 0x75260
-  __TEXT.__objc_methlist: 0x3554c
+1642.5.15.0.0
+  __TEXT.__text: 0x61769c
+  __TEXT.__auth_stubs: 0x6f40
+  __TEXT.__objc_stubs: 0x753a0
+  __TEXT.__objc_methlist: 0x355cc
   __TEXT.__const: 0x5638
-  __TEXT.__cstring: 0x63cf4
-  __TEXT.__objc_classname: 0x7d98
+  __TEXT.__cstring: 0x63d44
+  __TEXT.__objc_classname: 0x7db8
   __TEXT.__objc_methtype: 0x13fd2
   __TEXT.__gcc_except_tab: 0x9e5c
-  __TEXT.__objc_methname: 0xa3d2c
-  __TEXT.__oslogstring: 0x589ab
+  __TEXT.__objc_methname: 0xa3ecc
+  __TEXT.__oslogstring: 0x58a4b
   __TEXT.__ustring: 0x10
   __TEXT.__swift5_typeref: 0x3af0
   __TEXT.__constg_swiftt: 0x1f30

   __TEXT.__swift_as_ret: 0xd0
   __TEXT.__swift5_protos: 0x38
   __TEXT.__swift5_mpenum: 0x30
-  __TEXT.__unwind_info: 0x142e0
+  __TEXT.__unwind_info: 0x14318
   __TEXT.__eh_frame: 0x3008
-  __DATA_CONST.__auth_got: 0x37a8
-  __DATA_CONST.__got: 0x3f68
+  __DATA_CONST.__auth_got: 0x37b0
+  __DATA_CONST.__got: 0x3f58
   __DATA_CONST.__auth_ptr: 0x998
-  __DATA_CONST.__const: 0x30fe0
-  __DATA_CONST.__cfstring: 0x34220
-  __DATA_CONST.__objc_classlist: 0x1990
+  __DATA_CONST.__const: 0x31008
+  __DATA_CONST.__cfstring: 0x34240
+  __DATA_CONST.__objc_classlist: 0x1998
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x620
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xe0
   __DATA_CONST.__objc_superrefs: 0xf20
   __DATA_CONST.__objc_intobj: 0x1650
-  __DATA_CONST.__objc_arraydata: 0x650
+  __DATA_CONST.__objc_arraydata: 0x660
   __DATA_CONST.__objc_dictobj: 0x280
-  __DATA_CONST.__objc_arrayobj: 0x648
+  __DATA_CONST.__objc_arrayobj: 0x678
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x42608
-  __DATA.__objc_selrefs: 0x20078
-  __DATA.__objc_ivar: 0x29a0
-  __DATA.__objc_data: 0x11240
+  __DATA.__objc_const: 0x426c8
+  __DATA.__objc_selrefs: 0x200c8
+  __DATA.__objc_ivar: 0x29a4
+  __DATA.__objc_data: 0x11290
   __DATA.__data: 0x7500
-  __DATA.__bss: 0x3f70
+  __DATA.__bss: 0x3f80
   __DATA.__common: 0xb0
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 5181F53D-FFDB-3FC3-8467-05CD31E0D17D
-  Functions: 28698
-  Symbols:   4030
-  CStrings:  42690
+  UUID: 37C23B74-17B5-3BD9-8264-BC556BC0C82D
+  Functions: 28712
+  Symbols:   4029
+  CStrings:  42705
 
Symbols:
+ _NSClassFromString
+ _OBJC_CLASS_$_PKPaymentSetupRequest
- _PKPassLibraryDidAddPassNotification
- _PKPassLibraryDidRemovePassNotification
- _PKPassLibraryPassSourceUserInfoKey
CStrings:
+ "@\"PDCandidateRelevantPass\"16@?0@\"PDCandidateRelevantPass\"8"
+ "Deleting receipt for queued notification that will never be delivered due to denied authorization. receipt=%@"
+ "NPKPassLibraryCoordinator"
+ "PDWatchPassLibraryCoordinatorHelper"
+ "The next user activity signals was scheduled for: %@ "
+ "_cleanupUndeliveredReceiptsForDeniedAuthorization"
+ "_resolvedBoardingPassCandidates"
+ "_resolvedCandidates"
+ "_scheduleNextWeeklyActivity"
+ "initWithPassStyle:databaseManager:"
+ "notePassAddedWithUniqueID:passSource:"
+ "notePassRemovedWithUniqueID:"
+ "notePassUpdatedWithUniqueID:passSource:"
+ "openPaymentUIWithMerchantIdentifier:completion:"
+ "reportCampaignIdentifier:eventType:referralSource:deepLinkType:productType:"
+ "resolveCandidatesIfNecessary"
+ "resolvedCandidatePasses"
+ "resolvedLocatedCandidatePasses"
+ "resolvedLocatedDatelessCandidatePasses"
+ "resolvedUnlocatedCandidatePasses"
+ "userNotificationCenterDidReceiveDeniedAuthorization:"
+ "v24@0:8@\"PDUserNotificationCenter\"16"
+ "\xf0\xb1"
- "@\"PDCandidateRelevantPassFactory\""
- "_candidatePassFactory"
- "_previousCollectionDateIntervalWithRandomOffsetWeekly"
- "_resolveCandidatePasses:"
- "resolvedCandidatePassesOfStyle:"
- "resolvedLocatedCandidatePassesOfStyle:"
- "resolvedLocatedDatelessCandidatePassesOfStyle:"
- "resolvedUnlocatedCandidatePassesOfStyle:"
- "\xf0\xc1"

```
