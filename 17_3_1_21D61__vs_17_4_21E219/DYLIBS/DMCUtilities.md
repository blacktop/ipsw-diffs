## DMCUtilities

> `/System/Library/PrivateFrameworks/DMCUtilities.framework/DMCUtilities`

```diff

-3.26.4.1.0
-  __TEXT.__text: 0x28be0
-  __TEXT.__auth_stubs: 0xe00
-  __TEXT.__objc_methlist: 0x21bc
-  __TEXT.__const: 0xa8
-  __TEXT.__gcc_except_tab: 0x460
-  __TEXT.__cstring: 0x2a49
-  __TEXT.__oslogstring: 0x3570
-  __TEXT.__dlopen_cstrs: 0x108
-  __TEXT.__unwind_info: 0xa8c
-  __TEXT.__objc_classname: 0x3e4
-  __TEXT.__objc_methname: 0x8078
-  __TEXT.__objc_methtype: 0x110a
-  __TEXT.__objc_stubs: 0x4cc0
-  __DATA_CONST.__got: 0x3a0
-  __DATA_CONST.__const: 0xd10
-  __DATA_CONST.__objc_classlist: 0x130
+3.26.5.12.0
+  __TEXT.__text: 0x2a844
+  __TEXT.__auth_stubs: 0xe20
+  __TEXT.__objc_methlist: 0x22d4
+  __TEXT.__const: 0xb0
+  __TEXT.__gcc_except_tab: 0x4c8
+  __TEXT.__cstring: 0x2dc6
+  __TEXT.__oslogstring: 0x4025
+  __TEXT.__dlopen_cstrs: 0x165
+  __TEXT.__unwind_info: 0xaec
+  __TEXT.__objc_classname: 0x3ef
+  __TEXT.__objc_methname: 0x83ce
+  __TEXT.__objc_methtype: 0x1120
+  __TEXT.__objc_stubs: 0x4e80
+  __DATA_CONST.__got: 0x3a8
+  __DATA_CONST.__const: 0xd98
+  __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2b98
-  __DATA_CONST.__objc_selrefs: 0x1d28
-  __AUTH_CONST.__cfstring: 0x3260
-  __AUTH_CONST.__objc_const: 0xfc0
-  __AUTH_CONST.__const: 0xba0
-  __AUTH_CONST.__objc_intobj: 0x60
-  __AUTH_CONST.__auth_got: 0x710
-  __AUTH.__objc_data: 0xb90
-  __DATA.__objc_classrefs: 0x268
-  __DATA.__objc_superrefs: 0x88
-  __DATA.__objc_ivar: 0x194
+  __DATA_CONST.__objc_const: 0x2c60
+  __DATA_CONST.__objc_selrefs: 0x1df8
+  __DATA_CONST.__objc_classrefs: 0x268
+  __DATA_CONST.__objc_superrefs: 0x88
+  __AUTH_CONST.__cfstring: 0x3560
+  __AUTH_CONST.__objc_const: 0x1008
+  __AUTH_CONST.__const: 0xbe0
+  __AUTH_CONST.__objc_intobj: 0x120
+  __AUTH_CONST.__auth_got: 0x720
+  __AUTH.__objc_data: 0xbe0
+  __DATA.__objc_ivar: 0x19c
   __DATA.__data: 0x3a1
-  __DATA.__bss: 0x7a0
+  __DATA.__bss: 0x7e8
   __DATA_DIRTY.__objc_data: 0x50
-  __DATA_DIRTY.__bss: 0xa0
+  __DATA_DIRTY.__bss: 0xa8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreTelephony.framework/CoreTelephony

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1026
-  Symbols:   3895
-  CStrings:  2186
+  Functions: 1064
+  Symbols:   4020
+  CStrings:  2301
 
Symbols:
+ +[DMCDateFormatterFactory isoDateFormatter]
+ +[DMCDefaults ADETestModeEnabled]
+ +[DMCFeatureFlags isVisionMDMEnabled]
+ +[DMCFeatureFlags isVisionProfileEnrollEnabled]
+ +[DMCFeatureOverrides forceAppInstallUnremovability]
+ +[DMCFeatureOverrides forceAppRemovalOnUnenroll]
+ +[DMCFeatureOverrides forceMediaCommandSupport]
+ +[DMCFeatureOverrides shouldSimulateDEPCommunication]
+ +[DMCFeatureOverrides simluatedMDMAccountDrivenEnrollmentAuthenticationResults]
+ +[DMCFeatureOverrides simulatedCloudConfigProfile]
+ +[DMCFeatureOverrides simulatedMDMEnrollmentProfile]
+ +[DMCMobileGestalt isAppleSiliconMac]
+ +[DMCMobileGestalt isVisionDevice]
+ +[DMCRatchet _ratchetCalloutForOperation:]
+ +[DMCRatchet _ratchetCountdownForOperation:]
+ +[DMCRatchet _ratchetReasonForOperation:]
+ +[DMCRatchet _ratchetTextForOperation:]
+ +[DMCRatchet _ratchetTitleForOperation:]
+ +[DMCRatchet isAuthorizedForOperation:]
+ +[DMCRatchet isEnabled]
+ -[DMCHTTPTransaction ignoreAuthenticatorError]
+ -[DMCHTTPTransaction setIgnoreAuthenticatorError:]
+ -[DMCObliterationShelter isSupervised]
+ -[DMCObliterationShelter setIsSupervised:]
+ _DMCDefaultsKeyADETestModeEnabled
+ _DMCDefaultsKeyEnableMediaCommands
+ _DMCDefaultsKeyForceAppInstallUnremovability
+ _DMCDefaultsKeyForceAppRemovalOnUnenroll
+ _DMCDefaultsKeySimulateDEPCommunication
+ _DMCDefaultsKeySimulatedCloudConfigProfile
+ _DMCDefaultsKeySimulatedMDMAccountDrivenEnrollmentAuthenticationResults
+ _DMCDefaultsKeySimulatedMDMEnrollmentProfile
+ _DMCEnrollmentTypeBYOD
+ _DMCLocationErrorDomain
+ _DMCSystemLostModeRequestPath
+ _DMCSystemLostModeRequestPath.once
+ _DMCSystemLostModeRequestPath.str
+ _LocalAuthenticationLibrary
+ _LocalAuthenticationLibraryCore.frameworkLibrary
+ _OBJC_CLASS_$_DMCRatchet
+ _OBJC_IVAR_$_DMCHTTPTransaction._ignoreAuthenticatorError
+ _OBJC_IVAR_$_DMCObliterationShelter._isSupervised
+ _OBJC_METACLASS_$_DMCRatchet
+ __OBJC_$_CLASS_METHODS_DMCRatchet
+ __OBJC_CLASS_RO_$_DMCRatchet
+ __OBJC_METACLASS_RO_$_DMCRatchet
+ __SCNetworkInterfaceGetFamilySubType
+ __SCNetworkInterfaceGetFamilyType
+ ___127-[DMCAccountUtilities _signIniTunesAccountWithAuthenticationResult:personaID:canMakeAccountActive:baseViewController:outError:]_block_invoke.23
+ ___34+[DMCMobileGestalt isVisionDevice]_block_invoke
+ ___39+[DMCRatchet isAuthorizedForOperation:]_block_invoke
+ ___43+[DMCDateFormatterFactory isoDateFormatter]_block_invoke
+ ___48-[DMCAccountUtilities signOutAllPrimaryAccounts]_block_invoke.26
+ ___DMCSystemLostModeRequestPath_block_invoke
+ ___LocalAuthenticationLibraryCore_block_invoke
+ ___block_descriptor_56_e8_32s40r48r_e43_v24?0"AMSAuthenticateResult"8"NSError"16lr40l8r48l8s32l8
+ ___block_literal_global.111
+ ___block_literal_global.176
+ ___block_literal_global.194
+ ___block_literal_global.200
+ ___block_literal_global.57
+ ___block_literal_global.64
+ ___getLARatchetClass_block_invoke
+ ___getLARatchetClass_block_invoke.cold.1
+ ___getLARatchetManagerClass_block_invoke
+ ___getLARatchetManagerClass_block_invoke.cold.1
+ ___kCFBooleanFalse
+ __isUsefulIPv6Protocol
+ _audit_stringLocalAuthentication
+ _getLARatchetClass
+ _getLARatchetClass.softClass
+ _getLARatchetManagerClass
+ _getLARatchetManagerClass.softClass
+ _isVisionDevice.isVisionDevice
+ _isVisionDevice.onceToken
+ _isoDateFormatter.dateFormatter
+ _isoDateFormatter.onceToken
+ _kDMCErrorDetailsSUInfoKey
+ _objc_msgSend$_ratchetCalloutForOperation:
+ _objc_msgSend$_ratchetCountdownForOperation:
+ _objc_msgSend$_ratchetReasonForOperation:
+ _objc_msgSend$_ratchetTextForOperation:
+ _objc_msgSend$_ratchetTitleForOperation:
+ _objc_msgSend$armWithOptions:completion:
+ _objc_msgSend$complete
+ _objc_msgSend$ignoreAuthenticatorError
+ _objc_msgSend$initWithIdentifier:
+ _objc_msgSend$isEnabled
+ _objc_msgSend$isFeatureEnabled
+ _objc_msgSend$isSupervised
+ _objc_msgSend$resultWithCompletion:
+ _objc_msgSend$setIsSupervised:
+ _objc_msgSend$waitForCompletion
- +[DMCFeatureOverrides simulatedMDMAccountDrivenEnrollmentProfile]
- _DMCDefaultsKeySimulatedMDMAccountDrivenEnrollmentProfile
- ___48-[DMCAccountUtilities signOutAllPrimaryAccounts]_block_invoke.24
- ___block_literal_global.114
- ___block_literal_global.171
- ___block_literal_global.179
- ___block_literal_global.195
- ___block_literal_global.47
- ___block_literal_global.54
- ___block_literal_global.61
- _objc_msgSend$resultWithError:
CStrings:
+ "@24@0:8Q16"
+ "ADETestModeEnabled"
+ "B24@0:8Q16"
+ "DMCADETestModeEnabled"
+ "DMCDefaultsKeyForceAppInstallUnremovability"
+ "DMCDefaultsKeyForceAppRemovalOnUnenroll"
+ "DMCDeviceIsNetworkTethered: BSD name from service ID %{public}@ is: %{public}@"
+ "DMCDeviceIsNetworkTethered: Cannot get service ref for service ID %{public}@"
+ "DMCDeviceIsNetworkTethered: Checking service ID %{public}@"
+ "DMCDeviceIsNetworkTethered: Found tethered Ethernet at Service ID %{public}@!!"
+ "DMCDeviceIsNetworkTethered: Got IPv4 addresses: %{public}@"
+ "DMCDeviceIsNetworkTethered: Got IPv4 keys: %{public}@"
+ "DMCDeviceIsNetworkTethered: Got IPv4 netmasks: %{public}@"
+ "DMCDeviceIsNetworkTethered: Got IPv4 service dict: %{public}@"
+ "DMCDeviceIsNetworkTethered: Got IPv6 addresses: %{public}@"
+ "DMCDeviceIsNetworkTethered: Got IPv6 info: %{public}@"
+ "DMCDeviceIsNetworkTethered: Got IPv6 keys: %{public}@"
+ "DMCDeviceIsNetworkTethered: Got IPv6 netmasks: %{public}@"
+ "DMCDeviceIsNetworkTethered: Got useful IPv6 manual config!"
+ "DMCDeviceIsNetworkTethered: Got useful dynamic IPv4 config!"
+ "DMCDeviceIsNetworkTethered: Got useful dynamic IPv6 config!"
+ "DMCDeviceIsNetworkTethered: Got useful manual config of IPv4!"
+ "DMCDeviceIsNetworkTethered: IPv4 config method: %{public}@"
+ "DMCDeviceIsNetworkTethered: IPv4 info: %{public}@"
+ "DMCDeviceIsNetworkTethered: No network set!"
+ "DMCDeviceIsNetworkTethered: Unable to create network service entry"
+ "DMCDeviceIsNetworkTethered: Unable to get IPv4 info and/or it's disabled"
+ "DMCDeviceIsNetworkTethered: Unable to get IPv6 info and/or it's disabled"
+ "DMCDeviceIsNetworkTethered: cannot get interface for service ID %{public}@"
+ "DMCDeviceIsNetworkTethered: could not create dynamic store!"
+ "DMCDeviceIsNetworkTethered: could not get BSD name from service ID %{public}@"
+ "DMCDeviceIsNetworkTethered: could not get IPv4 info for service ID %{public}@"
+ "DMCDeviceIsNetworkTethered: could not get IPv6 info for service ID %{public}@"
+ "DMCDeviceIsNetworkTethered: could not get network link info from service ID %{public}@"
+ "DMCDeviceIsNetworkTethered: could not network link from service ID %{public}@"
+ "DMCDeviceIsNetworkTethered: got useful IPv4 info for service ID %{public}@!"
+ "DMCDeviceIsNetworkTethered: got useful IPv6 info for service ID %{public}@!"
+ "DMCDeviceIsNetworkTethered: netlink for service ID %{public}@ is not active"
+ "DMCDeviceIsNetworkTethered: service ID %{public}@ has netlink info: %{public}@"
+ "DMCDeviceIsNetworkTethered: service ID %{public}@ is not USB Ethernet"
+ "DMCDeviceIsNetworkTethered: service ID %{public}@ is not enabled"
+ "DMCEnableMediaCommands"
+ "DMCLocationQueryInProgressError"
+ "DMCRatchet"
+ "DMCRatchet is authorized because biometry is not enrolled"
+ "DMCRatchet is authorized because passcode is not set"
+ "DMCRatchet is authorized with result: %{public}@"
+ "DMCRatchet is unarmed with result: %{public}@"
+ "DMCRatchet is unarmed with user info: %{public}@"
+ "DMC_SDP_RATCHET_CALLOUT_INSTALL_PROFILE"
+ "DMC_SDP_RATCHET_CALLOUT_MDM_ENROLL"
+ "DMC_SDP_RATCHET_COUNTDOWN_INSTALL_PROFILE"
+ "DMC_SDP_RATCHET_COUNTDOWN_MDM_ENROLL"
+ "DMC_SDP_RATCHET_REASON_INSTALL_PROFILE"
+ "DMC_SDP_RATCHET_REASON_MDM_ENROLL"
+ "DMC_SDP_RATCHET_TEXT_INSTALL_PROFILE"
+ "DMC_SDP_RATCHET_TEXT_MDM_ENROLL"
+ "DMC_SDP_RATCHET_TITLE_INSTALL_PROFILE"
+ "DMC_SDP_RATCHET_TITLE_MDM_ENROLL"
+ "HTTP_ERROR_403_RESPONSE_SOFTWARE_UPDATE_REQUIRED"
+ "Interface family sub-type: %{public}@"
+ "Interface family: %{public}@"
+ "Interface type: %{public}@"
+ "IsSupervised"
+ "LARatchet"
+ "LARatchet is unavailable"
+ "LARatchetManager"
+ "LARatchetManager is unavailable"
+ "LostModeRequest.plist"
+ "RealityDevice"
+ "SimulateDEPCommunication"
+ "SimulatedCloudConfigProfile"
+ "SimulatedMDMAccountDrivenEnrollmentAuthenticationResults"
+ "SimulatedMDMEnrollmentProfile"
+ "SoftwareUpdateInfo"
+ "T@\"NSString\",?,R,C"
+ "TB,N,V_ignoreAuthenticatorError"
+ "TB,N,V_isSupervised"
+ "TB,R,N,GisVisionMDMEnabled"
+ "TB,R,N,GisVisionProfileEnrollEnabled"
+ "Tether"
+ "VisionMDM"
+ "VisionMDMEnabled"
+ "VisionProfileEnroll"
+ "VisionProfileEnrollEnabled"
+ "_ignoreAuthenticatorError"
+ "_isSupervised"
+ "_ratchetCalloutForOperation:"
+ "_ratchetCountdownForOperation:"
+ "_ratchetReasonForOperation:"
+ "_ratchetTextForOperation:"
+ "_ratchetTitleForOperation:"
+ "armWithOptions:completion:"
+ "com.apple.devicemanagementclient.DMCRatchet"
+ "forceAppInstallUnremovability"
+ "forceAppRemovalOnUnenroll"
+ "forceMediaCommandSupport"
+ "ignoreAuthenticatorError"
+ "initWithIdentifier:"
+ "isAppleSiliconMac"
+ "isAuthorizedForOperation:"
+ "isEnabled"
+ "isFeatureEnabled"
+ "isSupervised"
+ "isVisionDevice"
+ "isVisionMDMEnabled"
+ "isVisionProfileEnrollEnabled"
+ "isoDateFormatter"
+ "prefs:root=General&path=ManagedConfigurationList"
+ "resultWithCompletion:"
+ "setIgnoreAuthenticatorError:"
+ "setIsSupervised:"
+ "shouldSimulateDEPCommunication"
+ "simluatedMDMAccountDrivenEnrollmentAuthenticationResults"
+ "simulatedCloudConfigProfile"
+ "simulatedMDMEnrollmentProfile"
+ "softlink:r:path:/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication"
+ "v24@?0@\"AMSAuthenticateResult\"8@\"NSError\"16"
- "HTTP_ERROR_403_RESPONSE_SOFTWARE_UPDATE_REQUIRED_%@"
- "SimulatedMDMAccountDrivenEnrollmentProfile"
- "resultWithError:"
- "simulatedMDMAccountDrivenEnrollmentProfile"

```
