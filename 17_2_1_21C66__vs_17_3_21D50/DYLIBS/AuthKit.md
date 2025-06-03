## AuthKit

> `/System/Library/PrivateFrameworks/AuthKit.framework/AuthKit`

```diff

-466.7.12.0.0
-  __TEXT.__text: 0xada48
-  __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_methlist: 0x97a0
+466.7.15.0.0
+  __TEXT.__text: 0xb046c
+  __TEXT.__auth_stubs: 0xd30
+  __TEXT.__objc_methlist: 0x9b28
   __TEXT.__const: 0x1760
-  __TEXT.__cstring: 0xb6e1
-  __TEXT.__oslogstring: 0xcb41
+  __TEXT.__cstring: 0xba4a
+  __TEXT.__oslogstring: 0xced5
   __TEXT.__gcc_except_tab: 0x3d50
   __TEXT.__ustring: 0x1b8
-  __TEXT.__unwind_info: 0x320c
-  __TEXT.__objc_classname: 0x14e2
-  __TEXT.__objc_methname: 0x19c45
-  __TEXT.__objc_methtype: 0x3606
-  __TEXT.__objc_stubs: 0xbce0
-  __DATA_CONST.__got: 0x2e8
-  __DATA_CONST.__const: 0x4648
-  __DATA_CONST.__objc_classlist: 0x478
+  __TEXT.__unwind_info: 0x32ac
+  __TEXT.__objc_classname: 0x15b5
+  __TEXT.__objc_methname: 0x1a659
+  __TEXT.__objc_methtype: 0x3775
+  __TEXT.__objc_stubs: 0xbfe0
+  __DATA_CONST.__got: 0x2f8
+  __DATA_CONST.__const: 0x46d8
+  __DATA_CONST.__objc_classlist: 0x4b0
   __DATA_CONST.__objc_catlist: 0x80
-  __DATA_CONST.__objc_protolist: 0x190
+  __DATA_CONST.__objc_protolist: 0x198
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1a8e0
-  __DATA_CONST.__objc_selrefs: 0x55a0
+  __DATA_CONST.__objc_const: 0x1b498
+  __DATA_CONST.__objc_selrefs: 0x5758
   __DATA_CONST.__objc_arraydata: 0x128
-  __AUTH_CONST.__cfstring: 0xbe00
-  __AUTH_CONST.__objc_const: 0x41e0
+  __AUTH_CONST.__cfstring: 0xc0a0
+  __AUTH_CONST.__objc_const: 0x4420
   __AUTH_CONST.__const: 0xf50
-  __AUTH_CONST.__objc_intobj: 0x1c8
+  __AUTH_CONST.__objc_intobj: 0x210
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x168
-  __AUTH_CONST.__auth_got: 0x6a0
-  __AUTH.__objc_data: 0x1a90
+  __AUTH_CONST.__auth_got: 0x6a8
+  __AUTH.__objc_data: 0x1cc0
   __DATA.__objc_protorefs: 0xd0
-  __DATA.__objc_classrefs: 0x578
-  __DATA.__objc_superrefs: 0x2a8
-  __DATA.__objc_ivar: 0xca0
-  __DATA.__data: 0x1500
+  __DATA.__objc_classrefs: 0x5b8
+  __DATA.__objc_superrefs: 0x2d8
+  __DATA.__objc_ivar: 0xd04
+  __DATA.__data: 0x1560
   __DATA.__bss: 0x360
   __DATA_DIRTY.__objc_data: 0x1220
   __DATA_DIRTY.__bss: 0x1f8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1AA08F1F-82A7-3859-9EAA-4C5518C3AFAC
-  Functions: 5134
-  Symbols:   16680
-  CStrings:  8933
+  UUID: 73FB6887-E3C4-3BD9-BABF-C699A0E7EED4
+  Functions: 5228
+  Symbols:   16990
+  CStrings:  9119
 
Symbols:
+ +[AKBiometricRatchetUtility armingMethodFromRatchetResult:]
+ +[AKBiometricRatchetUtility ratchetIdentifier]
+ +[AKBiometricRatchetUtility resultForNonArmingFromError:]
+ +[AKBiometricRatchetUtility resultForNonArmingFromError:].cold.1
+ +[AKBiometricRatchetUtility resultForNonArmingFromError:].cold.2
+ +[AKBiometricRatchetUtility resultForSuccessfulArmingFromResponse:]
+ +[AKBiometricRatchetUtility resultForSuccessfulArmingFromResponse:].cold.1
+ +[AKBiometricRatchetUtility setRatchetIdentifier:]
+ +[AKBiometricRatchetUtility setRatchetIdentifier:].cold.1
+ +[AKBiometricRatchetUtility stateFromLARatchetState:]
+ +[AKDeviceSafetyRestrictionState(SecureCoding) supportsSecureCoding]
+ -[AKBiometricRatchetContext .cxx_destruct]
+ -[AKBiometricRatchetContext beginRatchetBody]
+ -[AKBiometricRatchetContext beginRatchetTitle]
+ -[AKBiometricRatchetContext calloutReason]
+ -[AKBiometricRatchetContext countdownText]
+ -[AKBiometricRatchetContext debugDescription]
+ -[AKBiometricRatchetContext deeplinkURL]
+ -[AKBiometricRatchetContext description]
+ -[AKBiometricRatchetContext fallbackToNoAuth]
+ -[AKBiometricRatchetContext findMyErrorMessage]
+ -[AKBiometricRatchetContext findMyErrorTitle]
+ -[AKBiometricRatchetContext initWithReason:calloutReason:deeplinkURL:fallbackToNoAuth:useShortExpiration:]
+ -[AKBiometricRatchetContext initWithReason:calloutReason:deeplinkURL:fallbackToNoAuth:useShortExpiration:beginRatchetTitle:beginRatchetBody:showsLocationWarning:countdownText:findMyErrorTitle:findMyErrorMessage:metaContext:]
+ -[AKBiometricRatchetContext metaContext]
+ -[AKBiometricRatchetContext reason]
+ -[AKBiometricRatchetContext showsLocationWarning]
+ -[AKBiometricRatchetContext useShortExpiration]
+ -[AKBiometricRatchetController armWithContext:completion:]
+ -[AKBiometricRatchetController armWithContext:completion:].cold.1
+ -[AKBiometricRatchetController armWithContext:completion:].cold.2
+ -[AKBiometricRatchetController cancelWithReason:completion:]
+ -[AKBiometricRatchetController currentRachetState]
+ -[AKBiometricRatchetController currentRachetState].cold.1
+ -[AKBiometricRatchetController currentRachetState].cold.2
+ -[AKBiometricRatchetController init]
+ -[AKBiometricRatchetController isCriticalEditAllowedForAltDSID:completion:]
+ -[AKBiometricRatchetController isDTOEnabled]
+ -[AKBiometricRatchetController isDTOEnabled].cold.1
+ -[AKBiometricRatchetController stateWithCompletion:]
+ -[AKBiometricRatchetResult .cxx_destruct]
+ -[AKBiometricRatchetResult armingMethod]
+ -[AKBiometricRatchetResult initWithRatchetState:armingMethod:]
+ -[AKBiometricRatchetResult ratchetState]
+ -[AKBiometricRatchetResult setArmingMethod:]
+ -[AKConfiguration criticalAccountEditsAllowedOverride]
+ -[AKConfiguration deviceSafetyRestrictionReasonOverride]
+ -[AKConfiguration setCriticalAccountEditsAllowedOverride:]
+ -[AKConfiguration setDeviceSafetyRestrictionReasonOverride:]
+ -[AKDeviceListRequestContext fetchDeviceSafetyState]
+ -[AKDeviceListRequestContext setFetchDeviceSafetyState:]
+ -[AKDeviceListResponse updateWithDeviceRestrictionState:]
+ -[AKDeviceListResponse updateWithDeviceRestrictionState:].cold.1
+ -[AKDeviceSafetyRestrictionState .cxx_destruct]
+ -[AKDeviceSafetyRestrictionState description]
+ -[AKDeviceSafetyRestrictionState initWithDeviceMID:serialNumber:restrictionReason:]
+ -[AKDeviceSafetyRestrictionState initWithResponse:error:]
+ -[AKDeviceSafetyRestrictionState initWithResponse:error:].cold.1
+ -[AKDeviceSafetyRestrictionState initWithResponse:error:].cold.2
+ -[AKDeviceSafetyRestrictionState machineId]
+ -[AKDeviceSafetyRestrictionState reason]
+ -[AKDeviceSafetyRestrictionState serialNumber]
+ -[AKDeviceSafetyRestrictionState(SecureCoding) encodeWithCoder:]
+ -[AKDeviceSafetyRestrictionState(SecureCoding) initWithCoder:]
+ -[AKFeatureManager init].cold.8
+ -[AKFeatureManager isDTOEnabled]
+ -[AKRatchetState .cxx_destruct]
+ -[AKRatchetState data]
+ -[AKRatchetState initWithRawState:data:]
+ -[AKRatchetState rawState]
+ -[AKRatchetState toString:]
+ -[AKRatchetStateData duration]
+ -[AKRatchetStateData initWithDuration:]
+ -[AKRatchetStateData setDuration:]
+ -[AKRemoteDevice deviceRestrictionState]
+ -[AKRemoteDevice setDeviceRestrictionState:]
+ -[AKURLBag deviceInfoURL]
+ -[AKUserInformation criticalAccountEditsAllowed]
+ -[AKUserInformation criticalAccountEditsAllowed].cold.1
+ -[AKUserInformation setCriticalAccountEditsAllowed:]
+ -[NSError(AuthKit) ak_isLAUserCancelError]
+ _AKBiometricRatchetStateDidChangeNotification
+ _AKCriticalAccountEditsAllowedKey
+ _AKURLBagKeyDeviceInfo
+ _LAErrorDomain
+ _LARatchetErrorUserInfoKeyState
+ _OBJC_CLASS_$_AKBiometricRatchetContext
+ _OBJC_CLASS_$_AKBiometricRatchetController
+ _OBJC_CLASS_$_AKBiometricRatchetResult
+ _OBJC_CLASS_$_AKBiometricRatchetUtility
+ _OBJC_CLASS_$_AKDeviceSafetyRestrictionState
+ _OBJC_CLASS_$_AKRatchetState
+ _OBJC_CLASS_$_AKRatchetStateData
+ _OBJC_CLASS_$_LARatchet
+ _OBJC_CLASS_$_LARatchetManager
+ _OBJC_IVAR_$_AKBiometricRatchetContext._beginRatchetBody
+ _OBJC_IVAR_$_AKBiometricRatchetContext._beginRatchetTitle
+ _OBJC_IVAR_$_AKBiometricRatchetContext._calloutReason
+ _OBJC_IVAR_$_AKBiometricRatchetContext._countdownText
+ _OBJC_IVAR_$_AKBiometricRatchetContext._deeplinkURL
+ _OBJC_IVAR_$_AKBiometricRatchetContext._fallbackToNoAuth
+ _OBJC_IVAR_$_AKBiometricRatchetContext._findMyErrorMessage
+ _OBJC_IVAR_$_AKBiometricRatchetContext._findMyErrorTitle
+ _OBJC_IVAR_$_AKBiometricRatchetContext._metaContext
+ _OBJC_IVAR_$_AKBiometricRatchetContext._reason
+ _OBJC_IVAR_$_AKBiometricRatchetContext._showsLocationWarning
+ _OBJC_IVAR_$_AKBiometricRatchetContext._useShortExpiration
+ _OBJC_IVAR_$_AKBiometricRatchetController._dtoLock
+ _OBJC_IVAR_$_AKBiometricRatchetResult._armingMethod
+ _OBJC_IVAR_$_AKBiometricRatchetResult._ratchetState
+ _OBJC_IVAR_$_AKDeviceListRequestContext._fetchDeviceSafetyState
+ _OBJC_IVAR_$_AKDeviceSafetyRestrictionState._machineId
+ _OBJC_IVAR_$_AKDeviceSafetyRestrictionState._reason
+ _OBJC_IVAR_$_AKDeviceSafetyRestrictionState._serialNumber
+ _OBJC_IVAR_$_AKFeatureManager._cachedIsDTOEnabled
+ _OBJC_IVAR_$_AKRatchetState._data
+ _OBJC_IVAR_$_AKRatchetState._rawState
+ _OBJC_IVAR_$_AKRatchetStateData._duration
+ _OBJC_IVAR_$_AKRemoteDevice._deviceRestrictionState
+ _OBJC_IVAR_$_AKUserInformation._criticalAccountEditsAllowed
+ _OBJC_METACLASS_$_AKBiometricRatchetContext
+ _OBJC_METACLASS_$_AKBiometricRatchetController
+ _OBJC_METACLASS_$_AKBiometricRatchetResult
+ _OBJC_METACLASS_$_AKBiometricRatchetUtility
+ _OBJC_METACLASS_$_AKDeviceSafetyRestrictionState
+ _OBJC_METACLASS_$_AKRatchetState
+ _OBJC_METACLASS_$_AKRatchetStateData
+ __OBJC_$_CLASS_METHODS_AKBiometricRatchetUtility
+ __OBJC_$_CLASS_METHODS_AKDeviceSafetyRestrictionState(SecureCoding)
+ __OBJC_$_INSTANCE_METHODS_AKBiometricRatchetContext
+ __OBJC_$_INSTANCE_METHODS_AKBiometricRatchetController
+ __OBJC_$_INSTANCE_METHODS_AKBiometricRatchetResult
+ __OBJC_$_INSTANCE_METHODS_AKDeviceSafetyRestrictionState(SecureCoding)
+ __OBJC_$_INSTANCE_METHODS_AKRatchetState
+ __OBJC_$_INSTANCE_METHODS_AKRatchetStateData
+ __OBJC_$_INSTANCE_VARIABLES_AKBiometricRatchetContext
+ __OBJC_$_INSTANCE_VARIABLES_AKBiometricRatchetController
+ __OBJC_$_INSTANCE_VARIABLES_AKBiometricRatchetResult
+ __OBJC_$_INSTANCE_VARIABLES_AKDeviceSafetyRestrictionState
+ __OBJC_$_INSTANCE_VARIABLES_AKRatchetState
+ __OBJC_$_INSTANCE_VARIABLES_AKRatchetStateData
+ __OBJC_$_PROP_LIST_AKBiometricRatchetContext
+ __OBJC_$_PROP_LIST_AKBiometricRatchetController
+ __OBJC_$_PROP_LIST_AKBiometricRatchetResult
+ __OBJC_$_PROP_LIST_AKDeviceSafetyRestrictionState
+ __OBJC_$_PROP_LIST_AKRatchetState
+ __OBJC_$_PROP_LIST_AKRatchetStateData
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_AKBiometricRatchetProtocol
+ __OBJC_$_PROTOCOL_METHOD_TYPES_AKBiometricRatchetProtocol
+ __OBJC_$_PROTOCOL_REFS_AKBiometricRatchetProtocol
+ __OBJC_CLASS_PROTOCOLS_$_AKBiometricRatchetController
+ __OBJC_CLASS_PROTOCOLS_$_AKDeviceSafetyRestrictionState(SecureCoding)
+ __OBJC_CLASS_RO_$_AKBiometricRatchetContext
+ __OBJC_CLASS_RO_$_AKBiometricRatchetController
+ __OBJC_CLASS_RO_$_AKBiometricRatchetResult
+ __OBJC_CLASS_RO_$_AKBiometricRatchetUtility
+ __OBJC_CLASS_RO_$_AKDeviceSafetyRestrictionState
+ __OBJC_CLASS_RO_$_AKRatchetState
+ __OBJC_CLASS_RO_$_AKRatchetStateData
+ __OBJC_LABEL_PROTOCOL_$_AKBiometricRatchetProtocol
+ __OBJC_METACLASS_RO_$_AKBiometricRatchetContext
+ __OBJC_METACLASS_RO_$_AKBiometricRatchetController
+ __OBJC_METACLASS_RO_$_AKBiometricRatchetResult
+ __OBJC_METACLASS_RO_$_AKBiometricRatchetUtility
+ __OBJC_METACLASS_RO_$_AKDeviceSafetyRestrictionState
+ __OBJC_METACLASS_RO_$_AKRatchetState
+ __OBJC_METACLASS_RO_$_AKRatchetStateData
+ __OBJC_PROTOCOL_$_AKBiometricRatchetProtocol
+ ___52-[AKBiometricRatchetController stateWithCompletion:]_block_invoke
+ ___52-[AKBiometricRatchetController stateWithCompletion:]_block_invoke.cold.1
+ ___57-[AKDeviceListResponse updateWithDeviceRestrictionState:]_block_invoke
+ ___57-[AKDeviceListResponse updateWithDeviceRestrictionState:]_block_invoke.cold.1
+ ___57-[AKDeviceListResponse updateWithDeviceRestrictionState:]_block_invoke.cold.2
+ ___60-[AKBiometricRatchetController cancelWithReason:completion:]_block_invoke
+ ___75-[AKBiometricRatchetController isCriticalEditAllowedForAltDSID:completion:]_block_invoke
+ ___75-[AKBiometricRatchetController isCriticalEditAllowedForAltDSID:completion:]_block_invoke.cold.1
+ ___block_descriptor_40_e8_32bs_e36_v24?0"LARatchetState"8"NSError"16ls32l8
+ ___block_descriptor_40_e8_32s_e27_B24?0"AKRemoteDevice"8Q16ls32l8
+ ___block_literal_global.313
+ _exit
+ _objc_msgSend$ak_deviceListErrorWithCode:
+ _objc_msgSend$armingMethodFromRatchetResult:
+ _objc_msgSend$cancelWithReason:completion:
+ _objc_msgSend$criticalAccountEditsAllowed
+ _objc_msgSend$criticalAccountEditsAllowedOverride
+ _objc_msgSend$duration
+ _objc_msgSend$initWithDeviceMID:serialNumber:restrictionReason:
+ _objc_msgSend$initWithDuration:
+ _objc_msgSend$initWithRatchetState:armingMethod:
+ _objc_msgSend$initWithRawState:data:
+ _objc_msgSend$isFeatureAvailable
+ _objc_msgSend$isFeatureEnabled
+ _objc_msgSend$isFeatureSupported
+ _objc_msgSend$machineId
+ _objc_msgSend$presentRatchetUIWithCompletion:
+ _objc_msgSend$ratchetIdentifier
+ _objc_msgSend$ratchetState
+ _objc_msgSend$rawState
+ _objc_msgSend$rawValue
+ _objc_msgSend$setCriticalAccountEditsAllowed:
+ _objc_msgSend$setDeviceRestrictionState:
+ _objc_msgSend$stateFromLARatchetState:
+ _objc_msgSend$stateWithCompletion:
+ _objc_msgSend$value
- ___block_literal_global.310
CStrings:
+ "\x0f\x04!\x1f\x0f\x06"
+ "\x1f\x02\x12"
+ "+[AKBiometricRatchetUtility setRatchetIdentifier:]"
+ "<%@: %p {\n\tgivenName: %@,\n\tfamilyName: %@,\n\tforwardingEmail: %@,\n\tprimaryEmailAddress: %@,\n\taccountName: %@,\n\taccountAliases: %@,\n\treachableEmails: %@,\n\tauthorizedApplicationsListVersion: %@,\n\tmasterKeyID: %@,\n\tvettedPrimaryEmail: %@,\n\tphoneAsAppleID: %@,\n\tisUnderage: %@,\n\tisSenior: %@,\n\tageOfMajority: %@,\n\tisLegacyStudent: %@,\n\tappleIDCountryCode: %@,\n\thasUsedAuthorization: %@, \n\tprivateAttestationEnabled: %@, \n\tappleIDSecurityLevel: %lu,\n\tauthMode: %lu,\n\tisMdmInfoRequired: %@,\n\trepairState: %lu,\n\tselectedEmail: %@,\n\tcanBeCustodian: %@,\n\tcanHaveCustodian: %@,\n\tcustodianEnabled: %@,\n\tcanBeBeneficiary: %@,\n\tcanHaveBeneficiary: %@,\n\thasMDM: %@,\n\tmanagedOrganizationType: %@,\n\tmanagedOrganizationName: %@,\n\tisNotificationEmailAvailable: %@,\n\tnotificationEmail: %@,\n\tadditionalInfo: %@,\n\ttrustedPhoneNumbers: %@,\n\tsecurityKeys: %@,\n\tloginHandles: %@,\n\tprivateEmailListVersion: %@,\n\tisProximityAuthEligible: %@,\n\twebAccessEnabled: %@,\n\tserverExperimentalFeatures: %@,\n\tcustodianInfos: %@,\n\tbeneficiaryInfo: %@,\n\tpasskeyEligible: %@,\n\tpasskeyPresent: %@,\n\tgroupKitEligibility: %@,\n\tpasscodeAuthEnabled: %@,\n\taskToBuy: %@,\n\thasSOSActiveDevice: %@,\n\tSOSNeeded: %@,\n\tdeviceListVersion: %@,\n\tconfigDataVersion: %@,\n\tbirthYear: %@,\n\tcriticalAccountEditsAllowed: %@,\n\thasModernRecoveryKey: %@,\n}>"
+ "<%@: %p>"
+ "<%@: %p> \n\treason: %@,\n\tcalloutReason: %@,\n\tdeeplinkURL: %@,\n\tfallbackToNoAuth: %@,\n\tseShortExpiration: %@,\n\tbeginRatchetTitle: %@,\n\tbeginRatchetBody: %@,\n\tshowsLocationWarning: %@,\n\tcountdownText: %@,\n\tfindMyErrorTitle: %@,\n\tfindMyErrorMessage: %@,\n"
+ "<%@:%p> Name: %@, SN: %@, Build: %@, OS: %@, Version: %@, Model: %@, Timestamp: %@, Trusted: %d, Safety State' %@, Circle Status: %d, Color Code: %@, Additional Info %@, services: %@, lastCacheUpdatedDate: %@, deletedDate: %@, removalReason: %ld "
+ "<%@:%p> machineId: %@, serial: %@, reason: %d, "
+ "@\"AKDeviceSafetyRestrictionState\""
+ "@\"AKRatchetState\""
+ "@\"AKRatchetState\"16@0:8"
+ "@\"AKRatchetStateData\""
+ "@100@0:8@16@24@32B40B44@48@56B64@68@76@84@92"
+ "@24@0:8d16"
+ "@32@0:8Q16@24"
+ "@40@0:8@16@24q32"
+ "@48@0:8@16@24@32B40B44"
+ "AKBiometricRatchetContext"
+ "AKBiometricRatchetController"
+ "AKBiometricRatchetIdentifierKey"
+ "AKBiometricRatchetProtocol"
+ "AKBiometricRatchetResult"
+ "AKBiometricRatchetStateDidChangeNotification"
+ "AKBiometricRatchetUtility"
+ "AKDeviceSafetyRestrictionReasonOverride"
+ "AKDeviceSafetyRestrictionState"
+ "AKOverrideCriticalAccountEdits"
+ "AKRatchetState"
+ "AKRatchetStateData"
+ "B24@?0@\"AKRemoteDevice\"8Q16"
+ "BEGIN [%lld]: RatchetFetchState  enableTelemetry=YES "
+ "DTO"
+ "DTOEnabled"
+ "Did not recieve %{public}@ key on device restriction state, failing init"
+ "Did not recieve a serial or machineID on device restriction state, failing init"
+ "END [%lld] %fs:RatchetFetchState "
+ "Failed to fetch user info for altDSID (%@) with error (%@)"
+ "Failed to find device for serial number %{mask.hash}@ or mid %{mask.hash}@"
+ "Feature DTO is supported. Is DTO enabled - %@"
+ "Found device for machineId %{mask.hash}@"
+ "Found device for serial number %{mask.hash}@"
+ "LARatchet state: %lu"
+ "Presenting Ratchet UI"
+ "Ratchet UI context doesn't respond to presentBiometricRatchetArmingUIWithCompletion"
+ "Ratchet is armed with state: %@"
+ "Ratchet is not armed - error: %@, ratchet state: %@"
+ "Ratchet state: %lu"
+ "Ratchet stateWithCompletion failed with error: %@"
+ "RatchetFetchState"
+ "SecureCoding"
+ "T@\"AKDeviceSafetyRestrictionState\",&,N,V_deviceRestrictionState"
+ "T@\"AKRatchetState\",R,C,N,V_ratchetState"
+ "T@\"AKRatchetStateData\",R,N,V_data"
+ "T@\"NSNumber\",C,N,V_criticalAccountEditsAllowed"
+ "T@\"NSString\",R,C,N,V_beginRatchetBody"
+ "T@\"NSString\",R,C,N,V_beginRatchetTitle"
+ "T@\"NSString\",R,C,N,V_calloutReason"
+ "T@\"NSString\",R,C,N,V_countdownText"
+ "T@\"NSString\",R,C,N,V_findMyErrorMessage"
+ "T@\"NSString\",R,C,N,V_findMyErrorTitle"
+ "T@\"NSString\",R,C,N,V_machineId"
+ "T@\"NSString\",R,C,N,V_metaContext"
+ "T@\"NSString\",R,C,N,V_reason"
+ "T@\"NSURL\",R,N,V_deeplinkURL"
+ "TB,N,V_fetchDeviceSafetyState"
+ "TB,R,N,GisDTOEnabled"
+ "TB,R,N,V_fallbackToNoAuth"
+ "TB,R,N,V_showsLocationWarning"
+ "TB,R,N,V_useShortExpiration"
+ "TQ,N,V_armingMethod"
+ "TQ,R,N,V_rawState"
+ "Td,N,V_duration"
+ "Tq,R,N,V_reason"
+ "User selected Quick Exit, calling exit(0) on purpose"
+ "_armingMethod"
+ "_beginRatchetBody"
+ "_beginRatchetTitle"
+ "_cachedIsDTOEnabled"
+ "_calloutReason"
+ "_countdownText"
+ "_criticalAccountEditsAllowed"
+ "_deeplinkURL"
+ "_deviceRestrictionState"
+ "_dtoLock"
+ "_duration"
+ "_fallbackToNoAuth"
+ "_fetchDeviceSafetyState"
+ "_findMyErrorMessage"
+ "_findMyErrorTitle"
+ "_metaContext"
+ "_ratchetState"
+ "_rawState"
+ "_showsLocationWarning"
+ "_useShortExpiration"
+ "ak_isLAUserCancelError"
+ "armWithContext:completion:"
+ "armingMethod"
+ "armingMethodFromRatchetResult:"
+ "beginRatchetBody"
+ "beginRatchetTitle"
+ "calloutReason"
+ "cancelWithReason:completion:"
+ "collapsed"
+ "countdownText"
+ "criticalAccountEditsAllowed"
+ "criticalAccountEditsAllowed finalValue: %d"
+ "criticalAccountEditsAllowedOverride"
+ "currentRachetState"
+ "deeplinkURL"
+ "deviceInfo"
+ "deviceInfoURL"
+ "deviceRestrictionState"
+ "deviceSafetyRestrictionReasonOverride"
+ "dtoEnabled: %@"
+ "fallbackToNoAuth"
+ "fetchDeviceInfo"
+ "fetchDeviceSafetyState"
+ "findMyErrorMessage"
+ "findMyErrorTitle"
+ "initWithDeviceMID:serialNumber:restrictionReason:"
+ "initWithDuration:"
+ "initWithRatchetState:armingMethod:"
+ "initWithRawState:data:"
+ "initWithReason:calloutReason:deeplinkURL:fallbackToNoAuth:useShortExpiration:"
+ "initWithReason:calloutReason:deeplinkURL:fallbackToNoAuth:useShortExpiration:beginRatchetTitle:beginRatchetBody:showsLocationWarning:countdownText:findMyErrorTitle:findMyErrorMessage:metaContext:"
+ "initWithResponse:error:"
+ "initial"
+ "isCriticalAccountEditAllowed"
+ "isCriticalEditAllowedForAltDSID:completion:"
+ "isDTOEnabled"
+ "isFeatureAvailable"
+ "isFeatureEnabled"
+ "isFeatureSupported"
+ "lostMode"
+ "metaContext"
+ "presentRatchetUIWithCompletion:"
+ "ratchetIdentifier"
+ "ratchetState"
+ "rawState"
+ "rawValue"
+ "ready"
+ "resultForNonArmingFromError:"
+ "resultForSuccessfulArmingFromResponse:"
+ "setArmingMethod:"
+ "setCriticalAccountEditsAllowed:"
+ "setCriticalAccountEditsAllowedOverride:"
+ "setDeviceRestrictionState:"
+ "setDeviceSafetyRestrictionReasonOverride:"
+ "setDuration:"
+ "setFetchDeviceSafetyState:"
+ "setRatchetIdentifier:"
+ "showsLocationWarning"
+ "stateFromLARatchetState:"
+ "stateWithCompletion:"
+ "toString:"
+ "unknown"
+ "updateWithDeviceRestrictionState:"
+ "useShortExpiration"
+ "v24@0:8@?<v@?@\"AKRatchetState\"@\"NSError\">16"
+ "v24@?0@\"LARatchetState\"8@\"NSError\"16"
+ "v32@0:8@\"AKBiometricRatchetContext\"16@?<v@?@\"AKBiometricRatchetResult\"@\"NSError\">24"
+ "v32@0:8@\"NSString\"16@?<v@?B>24"
+ "waitingCoolOff"
+ "waitingSecondAuth"
+ "{<%@:%p>: type: %ld, altDSID: %@, forceFetch: %d, fetchDeviceSafetyState: %d, os: %@, services: %@, untrusted: %d, family: %d, serialNumbers: %@, }"
- "\x0f\x04!\x1f\x0f\x05"
- "\x1f\x02\x11"
- "<%@: %p {\n\tgivenName: %@,\n\tfamilyName: %@,\n\tforwardingEmail: %@,\n\tprimaryEmailAddress: %@,\n\taccountName: %@,\n\taccountAliases: %@,\n\treachableEmails: %@,\n\tauthorizedApplicationsListVersion: %@,\n\tmasterKeyID: %@,\n\tvettedPrimaryEmail: %@,\n\tphoneAsAppleID: %@,\n\tisUnderage: %@,\n\tisSenior: %@,\n\tageOfMajority: %@,\n\tisLegacyStudent: %@,\n\tappleIDCountryCode: %@,\n\thasUsedAuthorization: %@, \n\tprivateAttestationEnabled: %@, \n\tappleIDSecurityLevel: %lu,\n\tauthMode: %lu,\n\tisMdmInfoRequired: %@,\n\trepairState: %lu,\n\tselectedEmail: %@,\n\tcanBeCustodian: %@,\n\tcanHaveCustodian: %@,\n\tcustodianEnabled: %@,\n\tcanBeBeneficiary: %@,\n\tcanHaveBeneficiary: %@,\n\thasMDM: %@,\n\tmanagedOrganizationType: %@,\n\tmanagedOrganizationName: %@,\n\tisNotificationEmailAvailable: %@,\n\tnotificationEmail: %@,\n\tadditionalInfo: %@,\n\ttrustedPhoneNumbers: %@,\n\tsecurityKeys: %@,\n\tloginHandles: %@,\n\tprivateEmailListVersion: %@,\n\tisProximityAuthEligible: %@,\n\twebAccessEnabled: %@,\n\tserverExperimentalFeatures: %@,\n\tcustodianInfos: %@,\n\tbeneficiaryInfo: %@,\n\tpasskeyEligible: %@,\n\tpasskeyPresent: %@,\n\tgroupKitEligibility: %@,\n\tpasscodeAuthEnabled: %@,\n\taskToBuy: %@,\n\thasSOSActiveDevice: %@,\n\tSOSNeeded: %@,\n\tdeviceListVersion: %@,\n\tconfigDataVersion: %@,\n\tbirthYear: %@,\n\thasModernRecoveryKey: %@,\n}>"
- "<%@:%p> Name: %@, SN: %@, Build: %@, OS: %@, Version: %@, Model: %@, Timestamp: %@, Trusted: %d, Circle Status: %d, Color Code: %@, Additional Info %@, services: %@, lastCacheUpdatedDate: %@, deletedDate: %@, removalReason: %ld "
- "{<%@:%p>: type: %ld, altDSID: %@, forceFetch: %d, os: %@, services: %@, untrusted: %d, family: %d, serialNumbers: %@, }"

```
