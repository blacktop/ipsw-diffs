## identityservicesd

> `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

```diff

-1926.300.121.0.0
-  __TEXT.__text: 0x71bb44
+1926.300.152.0.0
+  __TEXT.__text: 0x71d7e8
   __TEXT.__auth_stubs: 0x54d0
-  __TEXT.__objc_stubs: 0x449c0
-  __TEXT.__objc_methlist: 0x2406c
-  __TEXT.__const: 0x42470
-  __TEXT.__gcc_except_tab: 0x29610
-  __TEXT.__objc_methname: 0x6fd4b
-  __TEXT.__cstring: 0x55fff
-  __TEXT.__oslogstring: 0x7b17b
-  __TEXT.__objc_classname: 0x4351
+  __TEXT.__objc_stubs: 0x44e60
+  __TEXT.__objc_methlist: 0x2429c
+  __TEXT.__const: 0x42480
+  __TEXT.__gcc_except_tab: 0x29664
+  __TEXT.__objc_methname: 0x70354
+  __TEXT.__cstring: 0x564ef
+  __TEXT.__oslogstring: 0x7b45b
+  __TEXT.__objc_classname: 0x4370
   __TEXT.__objc_methtype: 0x11950
   __TEXT.__ustring: 0x4ca
   __TEXT.__dlopen_cstrs: 0xea
-  __TEXT.__swift5_typeref: 0x3888
+  __TEXT.__swift5_typeref: 0x389c
   __TEXT.__swift5_capture: 0xde8
-  __TEXT.__constg_swiftt: 0x2d14
+  __TEXT.__constg_swiftt: 0x2d74
   __TEXT.__swift5_reflstr: 0x1f3d
   __TEXT.__swift5_fieldmd: 0x2128
   __TEXT.__swift5_builtin: 0x8c

   __TEXT.__swift5_types: 0x22c
   __TEXT.__swift5_assocty: 0x1f8
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0xf918
-  __TEXT.__eh_frame: 0x4ca4
+  __TEXT.__unwind_info: 0xf938
+  __TEXT.__eh_frame: 0x4c6c
   __DATA_CONST.__auth_got: 0x2a78
   __DATA_CONST.__got: 0x3380
-  __DATA_CONST.__auth_ptr: 0x6b8
-  __DATA_CONST.__const: 0x1c748
-  __DATA_CONST.__cfstring: 0x337a0
-  __DATA_CONST.__objc_classlist: 0xe90
+  __DATA_CONST.__auth_ptr: 0x618
+  __DATA_CONST.__const: 0x1c7f8
+  __DATA_CONST.__cfstring: 0x33bc0
+  __DATA_CONST.__objc_classlist: 0xea0
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x768
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x118
-  __DATA_CONST.__objc_superrefs: 0xb50
-  __DATA_CONST.__objc_intobj: 0x1980
-  __DATA_CONST.__objc_arraydata: 0x5e8
+  __DATA_CONST.__objc_superrefs: 0xb58
+  __DATA_CONST.__objc_intobj: 0x19b0
+  __DATA_CONST.__objc_arraydata: 0x5e0
   __DATA_CONST.__objc_arrayobj: 0x348
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x48bc0
-  __DATA.__objc_selrefs: 0x14790
-  __DATA.__objc_ivar: 0x3154
-  __DATA.__objc_data: 0xb628
-  __DATA.__data: 0xa0d8
-  __DATA.__bss: 0x8f40
+  __DATA.__objc_const: 0x48f20
+  __DATA.__objc_selrefs: 0x148e0
+  __DATA.__objc_ivar: 0x3184
+  __DATA.__objc_data: 0xb710
+  __DATA.__data: 0xa0e8
+  __DATA.__bss: 0x8f80
   __DATA.__common: 0x518
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 20305
+  Functions: 20358
   Symbols:   2630
-  CStrings:  33940
+  CStrings:  34056
 
CStrings:
+ "15:35:30"
+ "Current PAC state: %!@(MISSING)"
+ "EchnidaEncryptionDisabled"
+ "Error while attempting to fetch state of SIMs for PAC state: %!@(MISSING)"
+ "FailedAuthentication"
+ "FailedRegistration"
+ "Fetching PAC state"
+ "Fetching state of %!l(MISSING)u sim(s)"
+ "ForcedReregister"
+ "Gained a phone auth cert!"
+ "IDSPACRemovedErrorDomain"
+ "IDSPACState"
+ "IDSPACStateTracker"
+ "Lockdown Mode"
+ "Lockdown Mode blocked %!@(MISSING) from contacting you."
+ "NoTrackedRemoval"
+ "Noting phone auth cert removal! Reason: %!@(MISSING)"
+ "Oct 26 2024"
+ "PAC state tracker clearing last PNR failure"
+ "PAC state tracker noting a PNR failure"
+ "PAC state tracker noting authentication has begun"
+ "PAC state tracker noting authentication has finished"
+ "PAC was last removed due to %!@(MISSING)"
+ "PNR is complete, but authentication is still in flight"
+ "PNR is complete, but we have not yet kicked off authentication"
+ "PNRSucceededAwaitingAuthenticationForNewCert"
+ "PhoneNumberChanged"
+ "PushTokenChanged"
+ "SecondaryEncryptionDisabled"
+ "SecondaryRegistrationDisabled"
+ "ServerAskedToRefreshCredentials"
+ "ServerReprovisionPush"
+ "SessionEncryptionKeyExpireDuration"
+ "Sim status %!@(MISSING) | simType: %!@(MISSING) isPNRCapable: %!@(MISSING) isPNRReady: %!@(MISSING) isPNRInFlight: %!@(MISSING) "
+ "Sliced cellular interface - Failed to register com.apple.CoreTelephony.Slicing.Interfaces.Active.State change notification: %!d(MISSING)"
+ "Sliced cellular interface - isInternalInstall (%!@(MISSING)), isCarrierInstall (%!@(MISSING)), currentServerBagPercentage (%!l(MISSING)u), diceRoll (%!u(MISSING))"
+ "Sliced cellular interface - received bitmask: %!l(MISSING)lu"
+ "T@\"IDSRateLimiter\",&,N,V_firewallAggressiveRateLimiter"
+ "T@\"NSDictionary\",&,N,V_simStates"
+ "TB,N,V_isAnyPNRInFlight"
+ "TB,N,V_isAnySIMInserted"
+ "TB,N,V_isAnySIMPNRCapable"
+ "TB,N,V_isAnySIMPNRReady"
+ "TB,N,V_isAnySIMUsable"
+ "TB,N,V_isAuthenticationInFlight"
+ "TB,N,V_isAwaitingAuthentication"
+ "TB,N,V_isDualSIM"
+ "There is a recent tracked PAC removal, including in error chain"
+ "There is currently a PNR in flight"
+ "This device has atleast one PNR capable SIM but none are ready for PNR"
+ "This device has atleast one inserted SIM but none are usable"
+ "This device has no SIM capable of PNR"
+ "This device has no inserted SIM"
+ "Tq,N,V_simCount"
+ "UserRemoved"
+ "_disableSecondaryRegistrationPercentage"
+ "_firewallAggressiveRateLimiter"
+ "_isAnyPNRInFlight"
+ "_isAnySIMInserted"
+ "_isAnySIMPNRCapable"
+ "_isAnySIMPNRReady"
+ "_isAnySIMUsable"
+ "_isAuthenticationInFlight"
+ "_isAwaitingAuthentication"
+ "_isDualSIM"
+ "_notificationAggressiveLimitPerPeriod"
+ "_notificationAggressiveLimitTimePeriod"
+ "_pacRemovalReasonToString:"
+ "_rateLimiterForService:"
+ "_shouldDisableEchnidaEncryption"
+ "_shouldDisableEncryption:UserDefaultKey:"
+ "_shouldDisableSecondaryEncryption"
+ "_shouldDisableSecondaryRegistration"
+ "_simCount"
+ "_simStates"
+ "_simTypeString:"
+ "_sliceActiveNotificationToken"
+ "an unknown contact"
+ "com.apple.CoreTelephony.Slicing.Interfaces.Active.State"
+ "eSIM"
+ "fetchCurrentPACState"
+ "firewall-aggressive-limit"
+ "firewall-aggressive-time-period"
+ "firewallAggressiveRateLimiter"
+ "firewallNotificationRateLimitType"
+ "hardwareType"
+ "ids-disable-echnida-encryption"
+ "ids-disable-secondary-encryption"
+ "ids-disable-secondary-wave2-registration-percentage"
+ "isAnyPNRInFlight"
+ "isAnySIMInserted: %!@(MISSING), isAnySIMUsable: %!@(MISSING), isDualSIM: %!@(MISSING), simCount: %!l(MISSING)d, isAnySIMPNRCapable: %!@(MISSING), isAnySIMPNRReady: %!@(MISSING), isAnyPNRInFlight: %!@(MISSING), isAwaitingAuthentication: %!@(MISSING), isAuthenticationInFlight: %!@(MISSING)"
+ "isAnySIMPNRCapable"
+ "isAnySIMPNRReady"
+ "isAuthenticationInFlight"
+ "isAwaitingAuthentication"
+ "isDualSIM"
+ "materialProvider"
+ "noteAuthenticationFinished"
+ "noteAuthenticationStarted"
+ "notePNRError:"
+ "notePNRSuccess"
+ "notePhoneAuthCertGained"
+ "notePhoneAuthCertLost:"
+ "physical"
+ "setBool:forKey:"
+ "setFirewallAggressiveRateLimiter:"
+ "setIsAnyPNRInFlight:"
+ "setIsAnySIMInserted:"
+ "setIsAnySIMPNRCapable:"
+ "setIsAnySIMPNRReady:"
+ "setIsAnySIMUsable:"
+ "setIsAuthenticationInFlight:"
+ "setIsAwaitingAuthentication:"
+ "setIsDualSIM:"
+ "setSimCount:"
+ "setSimStates:"
+ "setSliceInterfaceBitMask:forSession:"
+ "simCount"
+ "simStates"
+ "underlyingErrorForPACState:"
- "21:11:27"
- "IDSSessionEndedReasonAllocbindErrorResponse"
- "Oct 20 2024"
- "Sliced cellular interface - isInternalInstall (%!@(MISSING)), currentServerBagPercentage (%!l(MISSING)u), diceRoll (%!u(MISSING))"

```
