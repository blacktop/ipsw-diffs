## seserviced

> `/usr/libexec/seserviced`

```diff

-51.3.3.0.0
-  __TEXT.__text: 0x350ae8
-  __TEXT.__auth_stubs: 0x39f0
+51.5.1.0.0
+  __TEXT.__text: 0x3579ac
+  __TEXT.__auth_stubs: 0x3a10
   __TEXT.__objc_stubs: 0x8ba0
-  __TEXT.__objc_methlist: 0x4100
-  __TEXT.__const: 0x9330
-  __TEXT.__gcc_except_tab: 0x29f0
-  __TEXT.__objc_methname: 0x11d28
-  __TEXT.__oslogstring: 0x14f2f
-  __TEXT.__cstring: 0x2c10a
+  __TEXT.__objc_methlist: 0x40f0
+  __TEXT.__const: 0x93a0
+  __TEXT.__gcc_except_tab: 0x29dc
+  __TEXT.__objc_methname: 0x11d68
+  __TEXT.__oslogstring: 0x151af
+  __TEXT.__cstring: 0x2c40b
   __TEXT.__objc_classname: 0x116c
-  __TEXT.__objc_methtype: 0x605f
-  __TEXT.__swift5_typeref: 0x3950
-  __TEXT.__constg_swiftt: 0x3d54
-  __TEXT.__swift5_reflstr: 0x3e9a
-  __TEXT.__swift5_fieldmd: 0x40a0
+  __TEXT.__objc_methtype: 0x603a
+  __TEXT.__swift5_typeref: 0x3a9c
+  __TEXT.__constg_swiftt: 0x3c98
+  __TEXT.__swift5_reflstr: 0x3eea
+  __TEXT.__swift5_fieldmd: 0x40c4
   __TEXT.__swift5_builtin: 0x2bc
-  __TEXT.__swift5_assocty: 0x570
-  __TEXT.__swift5_capture: 0x2054
-  __TEXT.__swift5_proto: 0x640
+  __TEXT.__swift5_assocty: 0x588
+  __TEXT.__swift5_capture: 0x1fdc
+  __TEXT.__swift5_proto: 0x64c
   __TEXT.__swift5_types: 0x41c
   __TEXT.__swift5_protos: 0x4c
   __TEXT.__swift5_mpenum: 0x88
-  __TEXT.__unwind_info: 0x84f8
-  __TEXT.__eh_frame: 0xfeb0
-  __DATA_CONST.__auth_got: 0x1d08
-  __DATA_CONST.__got: 0xfb0
-  __DATA_CONST.__auth_ptr: 0xb70
-  __DATA_CONST.__const: 0xf238
-  __DATA_CONST.__cfstring: 0x11ac0
-  __DATA_CONST.__objc_classlist: 0x6f0
+  __TEXT.__unwind_info: 0x84d0
+  __TEXT.__eh_frame: 0xfea4
+  __DATA_CONST.__auth_got: 0x1d18
+  __DATA_CONST.__got: 0xfc0
+  __DATA_CONST.__auth_ptr: 0xb50
+  __DATA_CONST.__const: 0xf0f0
+  __DATA_CONST.__cfstring: 0x11a80
+  __DATA_CONST.__objc_classlist: 0x6e8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x400
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x2e8
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_intobj: 0x8d0
-  __DATA.__objc_const: 0x18510
-  __DATA.__objc_selrefs: 0x36b8
+  __DATA.__objc_const: 0x183e0
+  __DATA.__objc_selrefs: 0x36c8
   __DATA.__objc_ivar: 0xbf0
-  __DATA.__objc_data: 0x61a8
-  __DATA.__data: 0xa1c8
-  __DATA.__bss: 0xb740
-  __DATA.__common: 0x592
+  __DATA.__objc_data: 0x6150
+  __DATA.__data: 0xa018
+  __DATA.__bss: 0xb8c0
+  __DATA.__common: 0x58a
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth
   - /System/Library/Frameworks/CoreData.framework/CoreData

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 10098
-  Symbols:   1595
-  CStrings:  9870
+  Functions: 10116
+  Symbols:   1602
+  CStrings:  9901
 
Symbols:
+ _$s9SEService17JPKIInternalTypesO13InternalErrorO20processNotForegroundyAESS_tcAEmFWC
+ _$s9SEService17JPKIInternalTypesO15CertificateInfoVMa
+ _$s9SEService17JPKIInternalTypesO15CertificateInfoV4type18authTriesRemainingAeC0D4TypeO_s5UInt8VtcfC
+ _$s9SEService17JPKIInternalTypesO15CertificateInfoVMn
+ _$s9SEService17JPKIInternalTypesO13InternalErrorO31userAuthenticationMethodBlockedyA2EmFWC
+ _$s9SEService15JPKIXPCResponseO28getInstalledCertificateTypesyACSayAA012JPKIInternalF0O0E4InfoVGcACmFWC
+ _$s9SEService17JPKIInternalTypesO13InternalErrorO27incorrectUserAuthenticationyAESi_tcAEmFWC
+ _$sSD4KeysVMn
- _$s9SEService15JPKIXPCResponseO28getInstalledCertificateTypesyACSayAA012JPKIInternalF0O0E4TypeOGcACmFWC
CStrings:
+ "Treating unknown vehicle applet version as v1"
+ "setupNotificationCallbacks()"
+ "biolockoutRSSIThreshold"
+ "refreshAllObjects"
+ "Invalid certificate type provided to get remaining tries "
+ "expressPassConfigsWithError:"
+ "Incorrect user authentication, %!l(MISSING)d retries left"
+ "-[KmlVersions updateVehicleSupportedAppletVersions:]"
+ "outgoingTimerDuration"
+ "Ranging setup M3 message"
+ "Unable to create RBSProcessHandle"
+ "NSData *kmlUtilGenerateAccountInfoHash(NSData *__strong, NSData *__strong)"
+ "Got RBSProcessState %!@(MISSING)"
+ "exception trigger status"
+ "Unable to create RBSProcessIdentifier"
+ "User authentication method blocked"
+ "com.apple.seserviced.viennaReporting"
+ "-[KmlEndpointManager setBindingAttestation:]"
+ "-[KmlVersions updateVehicleSupportedFrameworkVersions:]"
+ "supportedRadioTechnologies"
+ "Restarted timer for %!s(MISSING) message: %!s(MISSING)"
+ "lyonexpress.state"
+ "Invalid auth string provided, cannot decode %!s(MISSING) in ascii"
+ "Waiting for message %!s(MISSING) of type %!s(MISSING), cannot restart timer for %!s(MISSING) message"
+ "Authentication invalid and failed with error %!s(MISSING)"
+ "updatedSpecCompliance"
+ "incomingTimerDuration"
+ " returned during "
+ "Unexpected status word "
+ "Expected ascii string but got "
+ "Timer ended for incoming message, disconnecting %!s(MISSING)"
+ "%!s(MISSING): self is unexpectedly nil"
+ "biolockoutBackoffDuration"
+ "Ranging M2 message"
+ "Connection from %!s(MISSING) privateEntitlement %!{(MISSING)bool}d"
+ "Failed to get express pass configurations"
+ "%!s(MISSING): Remote notification proxy is unexpectedly nil"
+ "Started timer for %!s(MISSING) message: %!s(MISSING)"
+ "Process %!s(MISSING) is not in the foreground"
+ "Truncated Reader Group Identifier"
+ "sessionEndedWithError:"
+ "Pause ranging request"
+ "Cannot restart when in idle state"
+ "Ranging resume request"
+ "Ranging setup M1 message"
+ "connectionRSSIThreshold"
+ "initiateAccessProtocolMessage"
+ "performStandardAuthentication(secureElement:certificateType:standard:)"
+ "iOS (18.1) - SecureElementService-51.5.1"
+ "Unable to create RBSProcessHandle for identifier %!@(MISSING)"
+ "Ended timer for %!s(MISSING) message: %!s(MISSING)"
+ "startWiredModeWithApplets:selectOnStart:externalAuth:completion:"
+ "Waiting for message %!s(MISSING) of type %!s(MISSING), cannot start timer for %!s(MISSING) in %!s(MISSING)"
+ "expressModeControlState"
+ "Treating unknown vehicle version as v1"
+ "Registered delegate for event %!{(MISSING)public}@, pending %!{(MISSING)public}d"
+ "Skipping Aliro Daily Transaction Statistics since Lyon is not running"
- "Remote notification proxy is unexpectedly nil"
- "sessionEndedWithError:completionHandler:"
- "Session became invalid"
- "_TtC10seserviced19SECPersistenceStore"
- "expressModeControlState:"
- "%!s(MISSING): Unexpected nil persistence controller"
- "Failed to get express pass config"
- "sessionDirtyCredentialCallback"
- "Failed to get express control state"
- "Failure retrieving proximity chip information"
- "Registered delegate for event %!@(MISSING), pending %!d(MISSING)"
- "NSData *kmlUtilGenerateAccountIdHash(NSData *__strong, NSData *__strong)"
- "Timer ended for incoming message for peer %!s(MISSING)"
- "com.apple.seserviced.reporting"
- "@\"SESExpressConfiguration\"24@0:8^@16"
- "getExpressConfiguration:"
- "Ended timer for %!s(MISSING) message"
- "iOS (18.1) - SecureElementService-51.3.3"
- "Waiting for message type %!s(MISSING), cannot start timer for %!s(MISSING)"
- "modifyAccessForCredential(_:addingOwners:removingOwners:addingUsers:removingUsers:reply:)"
- "UWB express update"
- "getExpressPassConfigWithError:"
- "Started timer for %!s(MISSING) message"
- "Currently authentication invalid and failed with error %!s(MISSING)"
- "updatedSpec"
- "FailedProximityChipQuery"
- "Session %!s(MISSING) Install finished callback is unexpectedly nil"
- "persistenceStore"

```
