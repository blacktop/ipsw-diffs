## seserviced

> `/usr/libexec/seserviced`

```diff

-44.24.0.0.0
-  __TEXT.__text: 0x1a5200
-  __TEXT.__auth_stubs: 0x2da0
+45.4.5.0.0
+  __TEXT.__text: 0x1af970
+  __TEXT.__auth_stubs: 0x2eb0
   __TEXT.__objc_stubs: 0xbbe0
-  __TEXT.__objc_methlist: 0x55ac
-  __TEXT.__const: 0x3f98
-  __TEXT.__gcc_except_tab: 0x27f0
-  __TEXT.__objc_methname: 0x11b56
+  __TEXT.__objc_methlist: 0x55b4
+  __TEXT.__const: 0x44b8
+  __TEXT.__gcc_except_tab: 0x2818
+  __TEXT.__objc_methname: 0x11b34
   __TEXT.__oslogstring: 0x9d1c
-  __TEXT.__cstring: 0x26597
-  __TEXT.__objc_classname: 0x134c
+  __TEXT.__cstring: 0x26ddc
+  __TEXT.__objc_classname: 0x134e
   __TEXT.__objc_methtype: 0x5f4b
-  __TEXT.__constg_swiftt: 0xd44
-  __TEXT.__swift5_typeref: 0x12e7
-  __TEXT.__swift5_builtin: 0x118
-  __TEXT.__swift5_reflstr: 0xec0
-  __TEXT.__swift5_fieldmd: 0x124c
-  __TEXT.__swift5_assocty: 0x180
-  __TEXT.__swift5_proto: 0x28c
-  __TEXT.__swift5_types: 0x134
+  __TEXT.__constg_swiftt: 0x10f0
+  __TEXT.__swift5_typeref: 0x1455
+  __TEXT.__swift5_builtin: 0x140
+  __TEXT.__swift5_reflstr: 0x10c0
+  __TEXT.__swift5_fieldmd: 0x148c
+  __TEXT.__swift5_assocty: 0x1f8
+  __TEXT.__swift5_proto: 0x2b0
+  __TEXT.__swift5_types: 0x168
+  __TEXT.__swift5_capture: 0x5c0
   __TEXT.__swift5_mpenum: 0x5c
-  __TEXT.__swift5_protos: 0x14
-  __TEXT.__swift5_capture: 0x5bc
-  __TEXT.__unwind_info: 0x4b14
-  __TEXT.__eh_frame: 0x5020
-  __DATA_CONST.__auth_got: 0x16e0
-  __DATA_CONST.__got: 0x6f8
-  __DATA_CONST.__auth_ptr: 0xa0
-  __DATA_CONST.__const: 0x7890
-  __DATA_CONST.__cfstring: 0x11260
-  __DATA_CONST.__objc_classlist: 0x4e0
+  __TEXT.__swift5_protos: 0x18
+  __TEXT.__unwind_info: 0x4cdc
+  __TEXT.__eh_frame: 0x5000
+  __DATA_CONST.__auth_got: 0x1768
+  __DATA_CONST.__got: 0x700
+  __DATA_CONST.__auth_ptr: 0xd8
+  __DATA_CONST.__const: 0x7cd0
+  __DATA_CONST.__cfstring: 0x11280
+  __DATA_CONST.__objc_classlist: 0x500
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x310
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x240
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_intobj: 0x978
-  __DATA.__objc_const: 0x14960
-  __DATA.__objc_selrefs: 0x3980
+  __DATA.__objc_const: 0x14d78
+  __DATA.__objc_selrefs: 0x3970
   __DATA.__objc_ivar: 0xf04
-  __DATA.__objc_data: 0x36d0
-  __DATA.__data: 0x4a28
-  __DATA.__bss: 0x4bf8
-  __DATA.__common: 0x16a
+  __DATA.__objc_data: 0x3770
+  __DATA.__data: 0x50d0
+  __DATA.__bss: 0x5088
+  __DATA.__common: 0x17a
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6371
-  Symbols:   1207
-  CStrings:  8545
+  Functions: 6559
+  Symbols:   1226
+  CStrings:  8596
 
Symbols:
+ _$s8Dispatch0A12TimeIntervalO7secondsyACSicACmFWC
+ _$s8Dispatch0A12TimeIntervalOMa
+ _$s8Dispatch0A12TimeIntervalOMn
+ _$s8Dispatch0A4TimeV3nowACyFZ
+ _$s8Dispatch0A4TimeV8advanced2byAcA0aB8IntervalO_tF
+ _$s8Dispatch0A4TimeVMa
+ _$sSD11descriptionSSvg
+ _$sSSs23CustomStringConvertiblesWP
+ _$sSh15minimumCapacityShyxGSi_tcfC
+ _$sSo10CFErrorRefas5Error10FoundationMc
+ _$sSo17OS_dispatch_queueC8DispatchE10asyncAfter8deadline3qos5flags7executeyAC0D4TimeV_AC0D3QoSVAC0D13WorkItemFlagsVyyXBtF
+ _$ss32_diagnoseUnexpectedEnumCaseValue4type03rawE0s5NeverOxm_q_tr0_lF
+ _$syycWV
+ _swift_getKeyPath
+ _swift_initEnumMetadataSinglePayload
+ _swift_readAtKeyPath
+ _swift_setAtReferenceWritableKeyPath
+ _tcc_authorization_record_get_authorization_right
+ _tcc_authorization_record_get_subject_identity
+ _tcc_identity_get_identifier
+ _tcc_server_create
+ _tcc_server_message_get_authorization_records_by_service
+ _tcc_service_singleton_for_CF_name
- _$syXlN
- _TCCAccessCopyInformationForBundleId
- _kTCCInfoGranted
- _kTCCInfoService
CStrings:
+ "\n shouldShowDefaultContactlessAppPane "
+ "\n shouldShowSECTCCPane "
+ "\nshouldShowHCETCCPane "
+ "1"
+ "Cannot fire in state null!"
+ "Current Default app?"
+ "Default app %s has TCC access to %s while out of region -- showing limited pane"
+ "Default app is Passbook while out of region -- should not show pane"
+ "Default app localized name missing even after migration"
+ "DefaultAppReconciliation"
+ "Error %s while getting auth records for service %s"
+ "Failed to create tcc server"
+ "Firing %s"
+ "Found auth record for bundle ID %s with authorization %s for service %s"
+ "Ignoring unexpected darwin event %s"
+ "Loaded TCC information for service %s --> %s"
+ "Loading TCC information for %s"
+ "Malformed dict %s when forming default app info"
+ "Migrating from v1 schema to v2"
+ "MigrationListener"
+ "No authorizationRecord / identity for tccService %s"
+ "No default app, nothing to migrate"
+ "Notify for client %s in state %s"
+ "Overwriting %s to default app candidate list due to default app found upon restore"
+ "Overwriting empty list to default app candidate list due to no default app found upon restore"
+ "Read current Pane Config %s"
+ "Received notification %ld"
+ "Reconcile Default Contactless: Ineligible to use default app, overwriting passbook as default"
+ "ReconciliationUserDefaults"
+ "Reconciling with regular in-region flow"
+ "SettingsPaneReconciliation"
+ "TCC_AUTHORIZATION_RIGHT_ADD_MODIFY_ADDED"
+ "TCC_AUTHORIZATION_RIGHT_ALLOWED"
+ "TCC_AUTHORIZATION_RIGHT_DENIED"
+ "TCC_AUTHORIZATION_RIGHT_LIMITED"
+ "TCC_AUTHORIZATION_RIGHT_SESSION_PID"
+ "TCC_AUTHORIZATION_RIGHT_UNKNOWN"
+ "URL Session error %s : attempt %ld of %ld"
+ "Unable to create tcc Service string %s"
+ "Unexpected no default app found on restore, nuke UD"
+ "We are super doomed -- unable to initialize Settings Suite!?"
+ "Writing Pane Config %s"
+ "_TtC10seserviced10TCCContext"
+ "_TtC10seserviced25SECSettingsPaneReconciler"
+ "_TtC10seserviced34SECDataMigrationCompletionListener"
+ "_TtCC10seserviced25SECSettingsPaneReconciler10PaneConfig"
+ "_deviceIntentConfidence"
+ "coealescer"
+ "com.apple.os-eligibility-domain.change.silicon"
+ "computeShouldShowPanes: Error %s when initializing LSApplicationRecord for %s"
+ "default.app.candidates"
+ "default.app.localized.name"
+ "defaultAppCandidates: Error %s when initializing LSApplicationRecord for %s"
+ "defaultContactlessAppCandidates"
+ "delay"
+ "deviceIntentConfidence"
+ "hceService"
+ "iOS (17.5) - SecureElementService-45.4.5"
+ "localizedName"
+ "migrateV1ToV2: Error %s when getting app record Current default app no longer installed, overwriting passbook as default"
+ "outputFunc"
+ "paneConfig"
+ "secService"
+ "seserviced/SECSettingsReconciliationUserDefaults.swift"
+ "seserviced/TriggerCoalesce.swift"
+ "shouldShowDefaultContactlessAppPane"
+ "shouldShowHCETCCPane"
+ "shouldShowSECTCCPane"
+ "tccContext"
+ "v24@?0@\"<OS_tcc_authorization_record>\"8^{__CFError=}16"
- "Default app %s does not have TCC access to %s while out of region -- showing pane"
- "No default external app found"
- "Overwriting current default as result of reconciliation"
- "Passbook is default while out of region -- not showing pane"
- "Received notification %s"
- "Reconcile Default Contactless: Ineligible to use default app, -- no op"
- "Registered notification controller for %s and %s"
- "Should show HCE Default %{bool}d"
- "Should show HCE TCC %{bool}d"
- "Should show SEC Default %{bool}d"
- "Should show SEC TCC %{bool}d"
- "Should show default contactless pane %{bool}d, should show hce TCC pane %{bool}d, should show sec TCC pane %{bool}d"
- "Unexpected domain when reconciling panes while out of region --  no op"
- "Unexpected event %s received"
- "Unexpected nil for default app info"
- "_isDeviceIntentSent"
- "bundleIdentifier"
- "developerType"
- "enumeratorWithOptions:"
- "iOS (17.4) - SecureElementService-44.24"

```
