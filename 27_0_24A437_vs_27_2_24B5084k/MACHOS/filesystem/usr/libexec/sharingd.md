## sharingd

> `/usr/libexec/sharingd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methtype`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`

```diff

-2131.10.1.2.11
-  __TEXT.__text: 0x672dc0
-  __TEXT.__auth_stubs: 0xb060
-  __TEXT.__objc_stubs: 0x37840
-  __TEXT.__objc_methlist: 0x1e634
-  __TEXT.__cstring: 0x3efd1
-  __TEXT.__objc_methname: 0x4ecd5
-  __TEXT.__objc_classname: 0x5af7
+2131.20.65.2.1
+  __TEXT.__text: 0x67b928
+  __TEXT.__auth_stubs: 0xb180
+  __TEXT.__objc_stubs: 0x378e0
+  __TEXT.__objc_methlist: 0x1e694
+  __TEXT.__cstring: 0x3f301
+  __TEXT.__objc_methname: 0x4ee35
+  __TEXT.__objc_classname: 0x5b67
   __TEXT.__objc_methtype: 0xbcc2
-  __TEXT.__const: 0x15eb8
-  __TEXT.__gcc_except_tab: 0x68a8
-  __TEXT.__oslogstring: 0x3d183
+  __TEXT.__const: 0x160a8
+  __TEXT.__gcc_except_tab: 0x68cc
+  __TEXT.__oslogstring: 0x3d653
   __TEXT.__ustring: 0x94
   __TEXT.__dlopen_cstrs: 0x438
-  __TEXT.__swift5_typeref: 0x80e2
-  __TEXT.__swift5_fieldmd: 0x5fec
-  __TEXT.__constg_swiftt: 0x78f4
+  __TEXT.__swift5_typeref: 0x816a
+  __TEXT.__swift5_fieldmd: 0x604c
+  __TEXT.__constg_swiftt: 0x79b8
   __TEXT.__swift5_builtin: 0x2f8
-  __TEXT.__swift5_reflstr: 0x5b39
-  __TEXT.__swift5_assocty: 0xcc0
+  __TEXT.__swift5_reflstr: 0x5b59
+  __TEXT.__swift5_assocty: 0xcf0
   __TEXT.__swift5_protos: 0xd4
-  __TEXT.__swift5_proto: 0xccc
-  __TEXT.__swift5_types: 0x5f4
-  __TEXT.__swift_as_entry: 0xe3c
-  __TEXT.__swift_as_cont: 0x220c
-  __TEXT.__swift5_capture: 0x51f0
-  __TEXT.__swift_as_ret: 0xf5c
+  __TEXT.__swift5_proto: 0xce0
+  __TEXT.__swift5_types: 0x5fc
+  __TEXT.__swift_as_entry: 0xe60
+  __TEXT.__swift_as_cont: 0x222c
+  __TEXT.__swift5_capture: 0x52a4
+  __TEXT.__swift_as_ret: 0xf78
   __TEXT.__swift5_mpenum: 0x24
-  __TEXT.__unwind_info: 0x19570
-  __TEXT.__eh_frame: 0x24844
-  __DATA_CONST.__const: 0x1ccc0
-  __DATA_CONST.__cfstring: 0x19740
-  __DATA_CONST.__objc_classlist: 0xe10
+  __TEXT.__unwind_info: 0x19c60
+  __TEXT.__eh_frame: 0x2590c
+  __DATA_CONST.__const: 0x1ce28
+  __DATA_CONST.__cfstring: 0x198c0
+  __DATA_CONST.__objc_classlist: 0xe20
   __DATA_CONST.__objc_catlist: 0x40
   __DATA_CONST.__objc_protolist: 0x748
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x288
-  __DATA_CONST.__objc_superrefs: 0x6f8
+  __DATA_CONST.__objc_superrefs: 0x700
   __DATA_CONST.__objc_intobj: 0xdc8
   __DATA_CONST.__objc_arraydata: 0x22f8
   __DATA_CONST.__objc_dictobj: 0x1720
   __DATA_CONST.__objc_arrayobj: 0x720
   __DATA_CONST.__objc_doubleobj: 0x20
-  __DATA_CONST.__auth_got: 0x5840
-  __DATA_CONST.__got: 0x3a38
-  __DATA_CONST.__auth_ptr: 0x4418
-  __DATA.__objc_const: 0x386f8
-  __DATA.__objc_selrefs: 0x11138
-  __DATA.__objc_ivar: 0x2948
-  __DATA.__objc_data: 0xa150
-  __DATA.__data: 0x14a78
+  __DATA_CONST.__auth_got: 0x58d0
+  __DATA_CONST.__got: 0x3b68
+  __DATA_CONST.__auth_ptr: 0x4478
+  __DATA.__objc_const: 0x38840
+  __DATA.__objc_selrefs: 0x11168
+  __DATA.__objc_ivar: 0x294c
+  __DATA.__objc_data: 0xa200
+  __DATA.__data: 0x14bf8
   __DATA.__common: 0x978
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /System/Library/PrivateFrameworks/SpringBoardUIServices.framework/SpringBoardUIServices
+  - /System/Library/PrivateFrameworks/SymptomDiagnosticReporter.framework/SymptomDiagnosticReporter
   - /System/Library/PrivateFrameworks/SystemStatus.framework/SystemStatus
   - /System/Library/PrivateFrameworks/TCC.framework/TCC
   - /System/Library/PrivateFrameworks/ToneLibrary.framework/ToneLibrary

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 26394
-  Symbols:   5018
-  CStrings:  27581
+  Functions: 26462
+  Symbols:   5076
+  CStrings:  27634
 
Symbols:
+ _$s2os6LoggerV7SharingE15accessReportingACvgZ
+ _$s7Sharing14SFAccessReportV7process10invocationACSS_SStcfC
+ _$s7Sharing14SFAccessReportVMa
+ _$s7Sharing16SFClientIdentityO16shortDescriptionSSvg
+ _$s7Sharing16SFClientIdentityO20untrustedProcessNameSSSgvg
+ _$s7Sharing19SFAccessReportStoreC11hasReported_3forSbAA0bC0V_SStFTj
+ _$s7Sharing19SFAccessReportStoreC6record_3foryAA0bC0V_SStFTj
+ _$s7Sharing19SFAccessReportStoreC6sharedACvgZ
+ _$s7Sharing19SFAccessReportStoreCMa
+ _$s7Sharing19SFAccessReportStoreCScAAAMc
+ _$s7Sharing19SFClientAccessLevelV10CapabilityO11entitlementSSvg
+ _$s7Sharing19SFClientAccessLevelV10CapabilityO12accountStateyA2EmFWC
+ _$s7Sharing19SFClientAccessLevelV10CapabilityO13airDropClientyA2EmFWC
+ _$s7Sharing19SFClientAccessLevelV10CapabilityO15airDropInternalyA2EmFWC
+ _$s7Sharing19SFClientAccessLevelV10CapabilityO15airDropSettingsyA2EmFWC
+ _$s7Sharing19SFClientAccessLevelV10CapabilityO17continuityStreamsyA2EmFWC
+ _$s7Sharing19SFClientAccessLevelV10CapabilityO19allowRestrictedBoopyA2EmFWC
+ _$s7Sharing19SFClientAccessLevelV10CapabilityO4nameSSvg
+ _$s7Sharing19SFClientAccessLevelV10CapabilityO7hotspotyA2EmFWC
+ _$s7Sharing19SFClientAccessLevelV10CapabilityOMa
+ _$s7Sharing19SFClientAccessLevelV11descriptionSSvg
+ _$s7Sharing19SFClientAccessLevelV13xpcConnectionACSo15NSXPCConnectionC_tcfC
+ _$s7Sharing19SFClientAccessLevelV8containsySbAC10CapabilityOF
+ _$s7Sharing20SFAirDropInvocationsO27SetTTRInactivityNudgeOptOutCAA22SFXPCInvocableProtocolAAMc
+ _$s7Sharing20SFAirDropInvocationsO27SetTTRInactivityNudgeOptOutCMa
+ _$s7Sharing20SFAirDropInvocationsO27SetTTRInactivityNudgeOptOutCMn
+ _$s7Sharing20SFAirDropInvocationsO29FetchTTRInactivityNudgeOptOutCAA22SFXPCInvocableProtocolAAMc
+ _$s7Sharing20SFAirDropInvocationsO29FetchTTRInactivityNudgeOptOutCMa
+ _$s7Sharing20SFAirDropInvocationsO29FetchTTRInactivityNudgeOptOutCMn
+ _$s7Sharing21SFAirDropUserDefaultsC24ttrInactivityNudgeOptOutSbvg
+ _$s7Sharing21SFAirDropUserDefaultsC24ttrInactivityNudgeOptOutSbvs
+ _$s7Sharing22SFPinAutoAcceptRequestVMa
+ _$sScP10backgroundScPvgZ
+ _$ss6HasherV5_hash4seed5bytes5countS2i_s6UInt64VSitFZ
+ _OBJC_CLASS_$_SDRDiagnosticReporter
+ _kSymptomDiagnosticActionCrashAndSpinLogs
+ _kSymptomDiagnosticActionDiagnosticExtensions
+ _kSymptomDiagnosticActionGetNetworkInfo
+ _kSymptomDiagnosticActionLogArchive
+ _kSymptomDiagnosticErrorConfigurationIneligible
+ _kSymptomDiagnosticErrorDailyLimitExceeded
+ _kSymptomDiagnosticErrorDisabled
+ _kSymptomDiagnosticErrorHourlyLimitExceeded
+ _kSymptomDiagnosticErrorInvalidParameters
+ _kSymptomDiagnosticErrorInvalidSignature
+ _kSymptomDiagnosticErrorNone
+ _kSymptomDiagnosticErrorNotSupported
+ _kSymptomDiagnosticErrorOperationallySuppressed
+ _kSymptomDiagnosticErrorPayloadSandboxTokenError
+ _kSymptomDiagnosticErrorRandomizedSuppression
+ _kSymptomDiagnosticErrorRequestThrottled
+ _kSymptomDiagnosticErrorServiceInterrupted
+ _kSymptomDiagnosticErrorServiceNotReady
+ _kSymptomDiagnosticErrorServiceUnavailable
+ _kSymptomDiagnosticErrorSessionNotFound
+ _kSymptomDiagnosticErrorSignatureIneligible
+ _kSymptomDiagnosticReplyReason
+ _kSymptomDiagnosticReplyReasonString
+ _kSymptomDiagnosticReplySessionID
+ _kSymptomDiagnosticReplySuccess
+ _kSymptomDiagnosticSignatureBundleIdentifier
- _$s7Sharing19SFClientAccessLevelV19allowRestrictedBoopACvgZ
- _$s7Sharing19SFClientAccessLevelVs10SetAlgebraAAMc
- _$ss10SetAlgebraP10isSuperset2ofSbx_tFTj
CStrings:
+ "### Client error retry expired after %f secs, not retrying for %@\n"
+ "%{public}s %{public}s is entitled for %{public}s -- allowing {level: %{public}s}"
+ "%{public}s %{public}s is missing %{public}s for %{public}s -- serving anyway, reporting"
+ "%{public}s %{public}s is missing %{public}s for %{public}s -- serving anyway, reporting {accessLevel: %{public}s}"
+ "%{public}s %{public}s was already reported for %{public}s at %{public}s on this device -- skipping"
+ "%{public}s ABC accepted the case -- done {sessionID: %{public}s}"
+ "%{public}s ABC did not take the case with %{public}s -- not recording, so the next call reports {invocation: %{public}s, detail: %{public}s}"
+ "%{public}s ABC refused the snapshot parameters -- giving up"
+ "%{public}s ABC rejected the case with %{public}s -- giving up {reason: %{public}d, detail: %{public}s}"
+ "%{public}s Could not build a signature for %{public}s -- giving up"
+ "%{public}s Could not name the calling process -- skipping {entitlement: %{public}s, invocation: %{public}s}"
+ "%{public}s Filing %{public}s/%{public}s/%{public}s/%{public}s against %{public}s -- submitting to ABC"
+ "AirDropTTR"
+ "AppleAccountSignedIn"
+ "AppleAccountSignedOut"
+ "Client error retry after %f secs for %@\n"
+ "ConfigurationIneligible"
+ "CreateCompanionServiceManager"
+ "CreateHotspotSession"
+ "CreateStreamsForMessage"
+ "DailyLimitExceeded"
+ "DisableService"
+ "EnableHotspotForDevice"
+ "EnableService"
+ "HourlyLimitExceeded"
+ "InvalidParameters"
+ "InvalidSignature"
+ "MissingEntitlement"
+ "OperationallySuppressed"
+ "PayloadSandboxTokenError"
+ "Pref client error expiry secs: %f -> %f\n"
+ "RandomizedSuppression"
+ "RequestThrottled"
+ "SDAccessReporter"
+ "ServiceInterrupted"
+ "ServiceUnavailable"
+ "SignatureIneligible"
+ "StartBrowsing"
+ "StopBrowsing"
+ "TQ,N,V_clientProvidedErrorTicks"
+ "UpdateLowLatencyFilter"
+ "[%{public}s] %{public}s is entitled for %{public}s -- allowing {level: %{public}s}"
+ "_TtC16DaemoniOSLibraryP33_86415E0687F64CDE9F6BA5BEA88B0A1C9Submitter"
+ "_clientProvidedErrorTicks"
+ "_prefClientErrorExpirySecs"
+ "chClientErrorExpirySecs"
+ "clientProvidedErrorTicks"
+ "com.apple.boop-session"
+ "com.apple.boop-setting"
+ "performShortcutActivityInHostWithBundleID:singleUseToken:sourceAppIsManaged:"
+ "profileConnectionDidReceiveAllowCloudSyncChangedNotification:userInfo:"
+ "reportIfConnection:missingAccountStateAccessForInvocation:"
+ "reportIfConnection:missingContinuityStreamsAccessForInvocation:"
+ "reportIfConnection:missingHotspotAccessForInvocation:"
+ "setClientProvidedErrorTicks:"
+ "signatureWithDomain:type:subType:subtypeContext:detectedProcess:triggerThresholdValues:"
+ "snapshotWithSignature:delay:events:payload:actions:reply:"
+ "tail"
+ "v36@0:8@\"NSString\"16@\"NSString\"24B32"
+ "verdict(from:signature:actions:)"
- "TB,N,V_clientProvidedError"
- "_clientProvidedError"
- "clientProvidedError"
- "com.apple.sharing.airdrop.boop-session"
- "com.apple.sharing.airdrop.boop-setting"
- "performShortcutActivityInHostWithBundleID:singleUseToken:"
- "setClientProvidedError:"
```
