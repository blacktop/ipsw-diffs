## BuddyMigrator

> `/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator`

```diff

-5076.0.0.0.0
-  __TEXT.__text: 0x7548
-  __TEXT.__auth_stubs: 0x530
-  __TEXT.__objc_stubs: 0x1660
-  __TEXT.__objc_methlist: 0x630
+5116.0.0.0.0
+  __TEXT.__text: 0x7914
+  __TEXT.__auth_stubs: 0x550
+  __TEXT.__objc_stubs: 0x16e0
+  __TEXT.__objc_methlist: 0x634
   __TEXT.__const: 0x18
-  __TEXT.__gcc_except_tab: 0x148
-  __TEXT.__objc_methname: 0x19e3
-  __TEXT.__cstring: 0x7c8
-  __TEXT.__oslogstring: 0x1203
+  __TEXT.__gcc_except_tab: 0x170
+  __TEXT.__objc_methname: 0x1a81
+  __TEXT.__cstring: 0x7c2
+  __TEXT.__oslogstring: 0x1302
   __TEXT.__objc_classname: 0x119
   __TEXT.__objc_methtype: 0x28b
   __TEXT.__dlopen_cstrs: 0x166
-  __TEXT.__unwind_info: 0x1f8
-  __DATA_CONST.__auth_got: 0x2a8
-  __DATA_CONST.__got: 0x110
-  __DATA_CONST.__const: 0x330
+  __TEXT.__unwind_info: 0x204
+  __DATA_CONST.__auth_got: 0x2b8
+  __DATA_CONST.__got: 0x128
+  __DATA_CONST.__const: 0x358
   __DATA_CONST.__cfstring: 0x9c0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_classrefs: 0x180
+  __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x1190
-  __DATA.__objc_selrefs: 0x6f8
-  __DATA.__objc_classrefs: 0x180
-  __DATA.__objc_superrefs: 0x28
+  __DATA.__objc_const: 0x1170
+  __DATA.__objc_selrefs: 0x720
   __DATA.__objc_ivar: 0x7c
   __DATA.__objc_data: 0x280
   __DATA.__data: 0x1e0

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3FD86387-530B-3A59-BD4C-1545C955A7FB
-  Functions: 168
-  Symbols:   215
-  CStrings:  632
+  UUID: 1D3A2588-4E30-35E7-9E7A-9898A0F69923
+  Functions: 170
+  Symbols:   220
+  CStrings:  640
 
Symbols:
+ _BYAssistantScreenShouldRunForVTConfirmation
+ _BYBuddyRunCombinedDiagnosticsMismatchMiniBuddy
+ _BYBuddyRunStolenDeviceProtectionMiniBuddy
+ _BYFlowSkipIdentifierSiri
+ _MCFeatureAppAnalyticsAllowed
+ __os_log_debug_impl
+ _sleep
- _MCFeatureDiagnosticsSubmissionModificationAllowed
- _os_variant_has_internal_ui
CStrings:
+ "BuddyMigrator: Posting follow-up for voice trigger confirmation"
+ "BuddyMigrator: Queueing Diagnostics & Usage mini-buddy for chlorine"
+ "BuddyMigrator: Routine manager supplied state %d (%d)"
+ "BuddyMigrator: Will call routine manager again after 1 second delay."
+ "CoreCDP"
+ "T@\"AMSBagKeySet\",?,R,N"
+ "T@\"NSString\",?,R,C"
+ "UseCDPContextSecretInsteadOfSBDSecret"
+ "UseCDPContextSecretInsteadOfSBDSecret = %{BOOL}d"
+ "_needsVoiceTriggerConfirmation"
+ "defaultManager"
+ "didSkipFlow:"
+ "eligibleForChlorine"
+ "isAppAnalyticsRestricted"
+ "isDeviceAnalyticsRestricted"
+ "isUseCDPContextSecretInsteadOfSBDSecretEnabled"
+ "migrateWithStoredMigratorVersion:userDataDisposition:"
- "ActionButton"
- "BuddyMigrator: Routine manager supplied state %d"
- "ButtonInteractionClassic"
- "SpringBoard"
- "T@\"AMSBagKeySet\",R,N"
- "isActionButtonEnabled"
- "isBoolSettingLockedDownByRestrictions:"
- "isButtonInteractionClassicEnabled"

```
