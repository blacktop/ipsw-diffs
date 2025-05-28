## BuddyMigrator

> `/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator`

```diff

-5125.0.0.0.0
-  __TEXT.__text: 0x7914
+5129.0.0.0.0
+  __TEXT.__text: 0x82a4
   __TEXT.__auth_stubs: 0x550
-  __TEXT.__objc_stubs: 0x16e0
-  __TEXT.__objc_methlist: 0x634
+  __TEXT.__objc_stubs: 0x1aa0
+  __TEXT.__objc_methlist: 0x7d4
   __TEXT.__const: 0x18
   __TEXT.__gcc_except_tab: 0x170
-  __TEXT.__objc_methname: 0x1a81
-  __TEXT.__cstring: 0x7c2
+  __TEXT.__objc_methname: 0x1f7d
+  __TEXT.__cstring: 0x8c6
   __TEXT.__oslogstring: 0x1302
-  __TEXT.__objc_classname: 0x119
-  __TEXT.__objc_methtype: 0x28b
+  __TEXT.__objc_classname: 0x12f
+  __TEXT.__objc_methtype: 0x2a0
   __TEXT.__dlopen_cstrs: 0x166
-  __TEXT.__unwind_info: 0x204
+  __TEXT.__unwind_info: 0x228
   __DATA_CONST.__auth_got: 0x2b8
   __DATA_CONST.__got: 0x128
-  __DATA_CONST.__const: 0x358
-  __DATA_CONST.__cfstring: 0x9c0
-  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__const: 0x3b8
+  __DATA_CONST.__cfstring: 0xb60
+  __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_classrefs: 0x180
-  __DATA_CONST.__objc_superrefs: 0x28
+  __DATA_CONST.__objc_classrefs: 0x188
+  __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x1170
-  __DATA.__objc_selrefs: 0x720
-  __DATA.__objc_ivar: 0x7c
-  __DATA.__objc_data: 0x280
+  __DATA.__objc_const: 0x1450
+  __DATA.__objc_selrefs: 0x830
+  __DATA.__objc_ivar: 0xac
+  __DATA.__objc_data: 0x2d0
   __DATA.__data: 0x1e0
   __DATA.__bss: 0x70
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 170
-  Symbols:   220
-  CStrings:  562
+  Functions: 203
+  Symbols:   234
+  CStrings:  637
 
Symbols:
+ _BuddySetupAnalyticsActiveDurationKey
+ _BuddySetupAnalyticsBackgroundDurationKey
+ _BuddySetupAnalyticsDataTransferMethodKey
+ _BuddySetupAnalyticsFollowUpItemsCount
+ _BuddySetupAnalyticsHasCompletedInitialSetupKey
+ _BuddySetupAnalyticsInAppleStoreKey
+ _BuddySetupAnalyticsIsSignedIntoAppleID
+ _BuddySetupAnalyticsNumberOfPanesPresentedKey
+ _BuddySetupAnalyticsOtherDurationKey
+ _BuddySetupAnalyticsPreferenceKey
+ _BuddySetupAnalyticsSoftwareUpdatePerformedKey
+ _BuddySetupAnalyticsUsedProximitySetupKey
+ _OBJC_CLASS_$_BuddySetupAnalytics
+ _OBJC_METACLASS_$_BuddySetupAnalytics
CStrings:
+ "BuddySetupAnalytics"
+ "T@\"BYPreferencesController\",&,N,V_preferences"
+ "TB,N,V_hasCompletedInitialSetup"
+ "TB,N,V_inAppleStore"
+ "TB,N,V_isSignedIntoAppleID"
+ "TB,N,V_softwareUpdatePerformed"
+ "TB,N,V_usedProximitySetup"
+ "TQ,N,V_dataTransferMethod"
+ "TQ,N,V_followUpItemsCount"
+ "TQ,N,V_numberOfPanesPresented"
+ "Td,N,V_activeDuration"
+ "Td,N,V_backgroundDuration"
+ "Td,N,V_otherDuration"
+ "_activeDuration"
+ "_backgroundDuration"
+ "_dataTransferMethod"
+ "_dictionaryRepresentation"
+ "_followUpItemsCount"
+ "_hasCompletedInitialSetup"
+ "_inAppleStore"
+ "_isSignedIntoAppleID"
+ "_numberOfPanesPresented"
+ "_otherDuration"
+ "_preferences"
+ "_softwareUpdatePerformed"
+ "_usedProximitySetup"
+ "activeDuration"
+ "addEvent:withPayload:persist:"
+ "addEventUsingAnalyticsManager:"
+ "backgroundDuration"
+ "com.apple.setupassistant.ios.setup"
+ "d"
+ "d16@0:8"
+ "dataTransferMethod"
+ "doubleValue"
+ "followUpItemsCount"
+ "hasCompletedInitialSetup"
+ "inAppleStore"
+ "initWithPreferences:"
+ "isEqualToAnalytics:"
+ "isSignedIntoAppleID"
+ "loadFromDiskWithPreferences:"
+ "numberOfPanesPresented"
+ "numberWithDouble:"
+ "otherDuration"
+ "preferences"
+ "removeFromDiskWithPreferences:"
+ "setActiveDuration:"
+ "setBackgroundDuration:"
+ "setDataTransferMethod:"
+ "setFollowUpItemsCount:"
+ "setHasCompletedInitialSetup:"
+ "setInAppleStore:"
+ "setIsSignedIntoAppleID:"
+ "setNumberOfPanesPresented:"
+ "setOtherDuration:"
+ "setPreferences:"
+ "setSoftwareUpdatePerformed:"
+ "setUsedProximitySetup:"
+ "setupAnalytics"
+ "softwareUpdatePerformed"
+ "usedProximitySetup"
+ "v24@0:8d16"

```
