## appleaccountd

> `/usr/libexec/appleaccountd`

```diff

-1007.100.1.1.0
-  __TEXT.__text: 0x282474
+1007.100.5.0.0
+  __TEXT.__text: 0x288a58
   __TEXT.__auth_stubs: 0x24c0
   __TEXT.__objc_methlist: 0x614
-  __TEXT.__objc_methname: 0x4009
+  __TEXT.__objc_methname: 0x400b
   __TEXT.__objc_classname: 0x20e
   __TEXT.__objc_methtype: 0x1429
-  __TEXT.__cstring: 0x7f64
-  __TEXT.__swift5_typeref: 0x5d89
+  __TEXT.__cstring: 0x7ea4
+  __TEXT.__swift5_typeref: 0x5e2b
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0xc0d0
-  __TEXT.__constg_swiftt: 0x977c
-  __TEXT.__swift5_reflstr: 0x4e84
-  __TEXT.__swift5_fieldmd: 0x4fbc
+  __TEXT.__const: 0xc140
+  __TEXT.__constg_swiftt: 0x9994
+  __TEXT.__swift5_reflstr: 0x4fa4
+  __TEXT.__swift5_fieldmd: 0x5068
   __TEXT.__swift5_builtin: 0x1a4
   __TEXT.__swift5_assocty: 0x620
-  __TEXT.__swift5_proto: 0x994
+  __TEXT.__swift5_proto: 0x99c
   __TEXT.__swift5_types: 0x4bc
-  __TEXT.__oslogstring: 0x15cf6
-  __TEXT.__swift5_protos: 0x1c8
-  __TEXT.__swift5_capture: 0x547c
+  __TEXT.__oslogstring: 0x161b6
+  __TEXT.__swift5_protos: 0x1cc
+  __TEXT.__swift5_capture: 0x5560
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x50c0
-  __TEXT.__eh_frame: 0x4f10
+  __TEXT.__unwind_info: 0x51a0
+  __TEXT.__eh_frame: 0x5138
   __DATA_CONST.__auth_got: 0x1260
-  __DATA_CONST.__got: 0xbb0
-  __DATA_CONST.__auth_ptr: 0x1c78
-  __DATA_CONST.__const: 0x105d8
-  __DATA_CONST.__objc_classlist: 0x4d8
+  __DATA_CONST.__got: 0xbb8
+  __DATA_CONST.__auth_ptr: 0x1e70
+  __DATA_CONST.__const: 0x10850
+  __DATA_CONST.__objc_classlist: 0x4e0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x160
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xb0
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0x13878
+  __DATA.__objc_const: 0x13a40
   __DATA.__objc_selrefs: 0x1178
   __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0x26d8
-  __DATA.__data: 0xf2b0
-  __DATA.__objc_stublist: 0x70
+  __DATA.__objc_data: 0x26e0
+  __DATA.__data: 0xf5e0
+  __DATA.__objc_stublist: 0x68
   __DATA.__bss: 0xeb80
-  __DATA.__common: 0x3c0
+  __DATA.__common: 0x3d8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 7580
+  Functions: 7638
   Symbols:   1129
-  CStrings:  3180
+  CStrings:  3201
 
Symbols:
+ _kInheritanceCleanupStaleRecordsEventName
- _kAACustodianGenerateEvent
CStrings:
+ "Cleaned up stale records. Continuing with preflight...."
+ "Changing CK record status to declined..."
+ "Custodian recovery session object destroyed, sessionID: %!s(MISSING), recoverySessionID: %!s(MISSING)"
+ "%!s(MISSING) Finished reporting successful event."
+ "%!s(MISSING) - Event is nil: %!@(MISSING)"
+ "ProcessInfo.processInfo.environment[XCTestConfigurationFilePath]: %!s(MISSING)"
+ "LCDeletionChangeCKStatusToDeclined feature is not enabled. Begin removal without declining the record."
+ "No declined records found. Aborting cleanup."
+ "inheritanceRecordCleanup"
+ "Is XCTestConfigurationFilePath nil: %!{(MISSING)bool}d"
+ "Fetching benefactor to remove..."
+ "Continuing with preflight...."
+ "lcDeletionChangeCKStatusToDeclined is on"
+ "isLCDeletionChangeCKStatusToDeclinedEnabled"
+ "Unable to load Info.plist of %!@(MISSING)"
+ "_inheritanceRequestManager"
+ "🌞 Successfully completed cleaning up beneficiary."
+ "%!s(MISSING) - Reporting Record Cleaning Event %!s(MISSING)"
+ "Stating Cleanup for %!s(MISSING)"
+ "👾 Failed cleaning up beneficiary with error: %!@(MISSING)"
+ "Error fetching beneficiary record: %!@(MISSING)"
+ "Failed to clean up beneficiary: %!@(MISSING)"
+ "_TtC13appleaccountd25InheritanceRecordsCleaner"
+ "requestController"
+ "activities: %!s(MISSING)"
+ "%!s(MISSING) Finished reporting failed event."
+ "Failed to fetch invitations %!@(MISSING)"
+ "_inheritanceRecordCleaner"
+ "lcDeletionChangeCKStatusToDeclined is off"
+ "Unable to read %!s(MISSING) from Info.plist of %!@(MISSING)"
+ "_preferences"
+ "%!l(MISSING)d declined record(s) found, starting cleanup"
+ "internalBuild: %!{(MISSING)bool}d"
+ "Successfully cleaning up beneficiary."
- "Unable to load Info.plist of "
- "appleaccountd.CustodianRecoveryAnalyticsEvent"
- "Fetching benefactor to decline..."
- "numCodeEntryAttempts"
- "com.apple.appleaccount.CustodianRecovery"
- "LCDeletionChangeCKStatusToDeclined feature is enabled. Changing CK record status to declined..."
- "appleaccountd/CloudKitContainerStore.swift"
- " from Info.plist of "
- "_TtC13appleaccountd31CustodianRecoveryAnalyticsEvent"
- "isDataOnlyRecovery"
- "LCDeletionChangeCKStatusToDeclined"

```
