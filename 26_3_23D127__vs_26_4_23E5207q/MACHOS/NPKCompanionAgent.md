## NPKCompanionAgent

> `/System/Library/PrivateFrameworks/NanoPassKit.framework/NPKCompanionAgent`

```diff

-1289.1.7.0.0
-  __TEXT.__text: 0x43154
-  __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_stubs: 0x7860
-  __TEXT.__objc_methlist: 0x33e0
+1289.16.0.0.0
+  __TEXT.__text: 0x47b40
+  __TEXT.__auth_stubs: 0xce0
+  __TEXT.__objc_stubs: 0x7900
+  __TEXT.__objc_methlist: 0x3470
   __TEXT.__const: 0xf8
-  __TEXT.__gcc_except_tab: 0x12a4
-  __TEXT.__cstring: 0x2632
-  __TEXT.__objc_methname: 0xbe35
-  __TEXT.__oslogstring: 0x9310
+  __TEXT.__gcc_except_tab: 0x1264
+  __TEXT.__cstring: 0x2781
+  __TEXT.__objc_methname: 0xbf51
+  __TEXT.__oslogstring: 0x98c0
   __TEXT.__objc_classname: 0x6c1
-  __TEXT.__objc_methtype: 0x359b
-  __TEXT.__unwind_info: 0xdf0
-  __DATA_CONST.__auth_got: 0x698
-  __DATA_CONST.__got: 0x6c8
+  __TEXT.__objc_methtype: 0x35dd
+  __TEXT.__unwind_info: 0xf70
+  __DATA_CONST.__auth_got: 0x680
+  __DATA_CONST.__got: 0x6b8
   __DATA_CONST.__const: 0x1e48
-  __DATA_CONST.__cfstring: 0x1140
+  __DATA_CONST.__cfstring: 0x1180
   __DATA_CONST.__objc_classlist: 0x98
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x100

   __DATA_CONST.__objc_superrefs: 0x88
   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x5ae0
-  __DATA.__objc_selrefs: 0x2788
+  __DATA.__objc_const: 0x5af8
+  __DATA.__objc_selrefs: 0x27c0
   __DATA.__objc_ivar: 0x1a8
   __DATA.__objc_data: 0x5f0
-  __DATA.__data: 0xc00
+  __DATA.__data: 0xc08
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 8E81381D-22DA-3378-B174-5849AC873256
-  Functions: 1112
-  Symbols:   441
-  CStrings:  2789
+  UUID: 32EB0EAD-0B07-3C5B-A8CB-870EE8C68720
+  Functions: 1125
+  Symbols:   436
+  CStrings:  2821
 
Symbols:
+ _NPKDomainAccessorForDomainWithDevice
+ _objc_setProperty_atomic_copy
- _NPKMaximumRelevancyResultsAge
- _OBJC_CLASS_$_NPSDomainAccessor
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x4
- _objc_retain_x5
- _objc_retain_x9
CStrings:
+ "-[NPDCompanionPassLibrary flightSubscriptionsWithCompletion:]"
+ "-[NPDCompanionPassLibrary flightsWithScheduledDepartureFromStartDate:endDate:completion:]"
+ "/Library/Caches/com.apple.xbs/0F1AA8BC-C7BB-4547-9807-95BC87A5E14D/TemporaryDirectory.nBzNEL/Sources/NanoPassbook/NPKCompanionAgent/NPKCompanionAgent.m"
+ "/Library/Caches/com.apple.xbs/0F1AA8BC-C7BB-4547-9807-95BC87A5E14D/TemporaryDirectory.nBzNEL/Sources/NanoPassbook/NPKCompanionAgent/NPKRemoteAdminConnectionServiceAgent.m"
+ "6C4614A2-332F-481C-B7DE-7E80973B07BF"
+ "E6F0AB1C-332F-481C-B7DE-7E80973B07BF"
+ "Error: Failed to fetch balance reminder for pass %@ due to %@"
+ "Error: Failed to fetch commute plan reminder interval for pass %@ due to %@"
+ "Error: Unable to read NPKBalanceReminderIdentifierWithBalanceAndUniqueID in NPS; domain accessor not found"
+ "Error: Unable to read NPKDefaultPaymentPassDefault in NPS; domain accessor not found"
+ "Error: Unable to read NPKExpressFelicaTransitPaymentPassUniqueIDDefault in NPS; domain accessor not found"
+ "Error: Unable to read PKUserHasDisabledPeerPaymentKey in NPS; domain accessor not found"
+ "Error: Unable to read _commutePlanReminderIdentifierWithCommutePlan from NPS; domain accessor not found"
+ "Error: Unable to update NPKBalanceReminderIdentifierWithBalanceAndUniqueID in NPS; domain accessor not found"
+ "Error: Unable to update PKUserHasDisabledPeerPaymentKey in NPS; domain accessor not found"
+ "Error: Unable to update _commutePlanReminderIdentifierWithCommutePlan from NPS; domain accessor not found"
+ "Error: Unable to update _commutePlanReminderIdentifierWithCommutePlan in NPS; domain accessor not found"
+ "Error: Unable to update passDatabase; no domain accessor found"
+ "Error: Watch fails to set balance reminder %@ for balance %@ of pass %@"
+ "Error: Watch fails to set commute plan reminder %@ for pass %@"
+ "NPKCompletedMigrations"
+ "NPKMigrationResyncPassSettings_v1"
+ "Notice: (PKPaymentCommutePlanDetail get) Request for plans for unique ID %@; returning %@"
+ "Notice: (PKPaymentCommutePlanDetail set) Got updated plans %@ for pass with unique ID %@. Processing subject to first unlock and paired sync."
+ "Notice: Executing migration: Resyncing pass settings for all passes."
+ "Notice: Got plans: %@ for pass with unique ID %@; sending to %@"
+ "Notice: Migration: Performing settings sync for pass %@"
+ "Notice: Running migration: %@"
+ "Notice: Skipping migration (already run): %@"
+ "T@\"NSString\",C,V_initializedPairingIdentifier"
+ "_migration_resyncPassSettings"
+ "_performMigrations"
+ "_shouldSyncPassSettingsFromCompanionPassLibrary:"
+ "commutePlansForPassWithUniqueID:"
+ "handlePlanUpdate:forUniqueID:"
+ "paymentPassWithUniqueIdentifier:didUpdateWithPlans:"
+ "plansForPaymentPassWithUniqueIdentifier:completion:"
+ "setCommutePlans:forPassWithUniqueID:"
+ "v32@0:8@\"NSArray\"16@\"NSString\"24"
+ "v32@0:8@\"NSString\"16@\"NSArray\"24"
- "/Library/Caches/com.apple.xbs/Sources/NanoPassbook/NPKCompanionAgent/NPKCompanionAgent.m"
- "/Library/Caches/com.apple.xbs/Sources/NanoPassbook/NPKCompanionAgent/NPKRemoteAdminConnectionServiceAgent.m"
- "6C4614A2-1ECC-4405-9FEE-B5F0A5666961"
- "E6F0AB1C-320C-4941-9948-D2EAE7BA9A51"
- "Notice: Fails to fetch balance reminder for pass %@ due to %@"
- "Notice: Fails to fetch commute plan reminder interval for pass %@ due to %@"
- "Notice: Watch fails to set balance reminder %@ for balance %@ of pass %@"
- "Notice: Watch fails to set commute plan reminder %@ for pass %@"
- "T@\"NSString\",&,N,V_initializedPairingIdentifier"
- "initWithDomain:"

```
