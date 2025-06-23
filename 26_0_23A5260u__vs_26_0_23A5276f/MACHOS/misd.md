## misd

> `/usr/libexec/misd`

```diff

-346.0.0.0.2
-  __TEXT.__text: 0x200a4
+352.0.0.502.2
+  __TEXT.__text: 0x201b8
   __TEXT.__auth_stubs: 0x11e0
   __TEXT.__objc_stubs: 0x4e0
   __TEXT.__objc_methlist: 0x38c
   __TEXT.__const: 0x158
-  __TEXT.__cstring: 0xa47d
+  __TEXT.__cstring: 0xaed3
   __TEXT.__oslogstring: 0x1e
   __TEXT.__objc_methname: 0x8f6
   __TEXT.__objc_classname: 0x74
   __TEXT.__objc_methtype: 0x69e
-  __TEXT.__unwind_info: 0x4c0
+  __TEXT.__unwind_info: 0x4b8
   __DATA_CONST.__auth_got: 0x8f8
   __DATA_CONST.__got: 0x2b0
-  __DATA_CONST.__const: 0x638
+  __DATA_CONST.__const: 0x9d8
   __DATA_CONST.__cfstring: 0xb40
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x18

   __DATA.__objc_selrefs: 0x2c0
   __DATA.__objc_ivar: 0x1c
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0x398
+  __DATA.__data: 0x3a0
   __DATA.__common: 0xa0
   __DATA.__bss: 0x5d1
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libmrc.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7B03D600-733E-34E1-9F97-CB5E56675519
-  Functions: 428
+  UUID: BD975602-61E4-3E9F-82A2-806B177A97E9
+  Functions: 427
   Symbols:   380
-  CStrings:  1667
+  CStrings:  1788
 
CStrings:
+ "%s: bridged mode doesn't support setting the MTU"
+ "%s: creating a network based on XPC request"
+ "%s: encountered a connection error trying to activate tethering, tearing down personal hotspot"
+ "%s: invalid MTU %u"
+ "%s: mtu mismatch, if %s %d, network %s %d"
+ "???"
+ "connectionActivationError: %s (%d)"
+ "kAirplaneModeDialFailure"
+ "kAnsweredElsewhere"
+ "kAppTemporaryFailure"
+ "kBBDualSimConflict"
+ "kBadPinFormatError"
+ "kBasebandCrash"
+ "kCallBarred"
+ "kCallEndFade"
+ "kCallHandedToAnotherDevice"
+ "kCallRejected"
+ "kCallReorder"
+ "kCannotReplaceSm"
+ "kClass0NotSupported"
+ "kCommandCannotBeActioned"
+ "kCommandUnsupported"
+ "kCongestion"
+ "kDADMissing"
+ "kDataBearerUnavailable"
+ "kDataBlockedByVoiceCall"
+ "kDataCallThrottled"
+ "kDataCodingSchemeNotSupported"
+ "kDataNotAllowed"
+ "kDataNotAttached"
+ "kDataNotConfigured"
+ "kDataNotSupported"
+ "kDestinationOutOfOrder"
+ "kEmergencySessionRequired"
+ "kFacilityRejected"
+ "kGprsEsmProcTimeOut"
+ "kGprsGgsnReject"
+ "kGprsIllegalMe"
+ "kGprsIllegalMs"
+ "kGprsInvalidMobileClass"
+ "kGprsIpv4Disallowed"
+ "kGprsIpv6Disallowed"
+ "kGprsLocationAreaNotAllowed"
+ "kGprsMissingorUnknownAPN"
+ "kGprsOptionTempOOO"
+ "kGprsPDPAuthenticationInfoRejectedByBaseband"
+ "kGprsPdpAuthenticationFailure"
+ "kGprsPdpConnDoesNotExist"
+ "kGprsPlmnNotAllowed"
+ "kGprsPrefixUnavailable"
+ "kGprsRoamingNotAllowedInLocationArea"
+ "kGprsServiceOptionNotSubscribed"
+ "kGprsServiceOptionNotSupported"
+ "kGprsServiceOptionTemporarilyOutOfOrder"
+ "kGprsServicesNotAllowed"
+ "kGprsSingleAddrBearerOnly"
+ "kGprsUnknownPdpAddressOrPdpType"
+ "kGprsUnspecified"
+ "kHandoverIpConflict"
+ "kIRatRecommendsNonCellular"
+ "kImsPrefUnavailable"
+ "kImsSipError"
+ "kImsTimeout"
+ "kIncorrectPassword"
+ "kInformationElementNonExistant"
+ "kInterworkingError"
+ "kInterworkingNotSupported"
+ "kIntlRoamingNotAllowed"
+ "kIntlRoamingNotAllowedReasonMMS"
+ "kInvalidMandatoryInformation"
+ "kInvalidNumberFormat"
+ "kInvalidRat"
+ "kInvalidTransactionIdentifier"
+ "kLocalSocketError"
+ "kMediaError"
+ "kMediaHoldHeartbeatTimeout"
+ "kMediaServerCrash"
+ "kMediaStartFailure"
+ "kMediaTimeout"
+ "kMessageNotCompatibleWithProtocolState"
+ "kMessageTypeNonExistant"
+ "kNetworkDownUACCheckFailed"
+ "kNetworkFailure"
+ "kNetworkOutOfOrder"
+ "kNoError"
+ "kNoNetworkService"
+ "kNoReconnectionMustBeAttempted"
+ "kNoUserResponding"
+ "kNumberChanged"
+ "kNumberNotAllowed"
+ "kOperatorDeterminedBarring"
+ "kOtaspSPCError"
+ "kPdnNonTransferable"
+ "kPhoneLocked"
+ "kProtocolErrorUnspecified"
+ "kRadioFailure"
+ "kRejectedBySimSmsControl"
+ "kRequestedFacilityNotImplemented"
+ "kRequestedFacilityNotSubscribed"
+ "kResourcesUnavailable"
+ "kScBusy"
+ "kSecondaryDeviceAlreadyInUse"
+ "kSemanticallyIncorrectMessage"
+ "kShortMessageTransferRejected"
+ "kSimFailure"
+ "kSimMemoryFailure"
+ "kSimNotInserted"
+ "kSimPinRequired"
+ "kSimPukRequired"
+ "kTemporaryFailure"
+ "kTpduNotSupported"
+ "kUnassignedNumber"
+ "kUncertifiedWifiCallingFatalError"
+ "kUnidentifiedSubscriber"
+ "kUnknownError"
+ "kUnknownSubscriber"
+ "kUnspecifiedDcsError"
+ "kUnspecifiedPid"
+ "kUnspecifiedTpCommandError"
+ "kUserBusy"
+ "kiWLanForceReset"
+ "kiWLanNeedBackoff"
+ "kiWLanNotAllowed"
+ "networkMtu"
- "%s: legacy code, creating a network based on XPC request"
- "%s: mtu mismatch, if %s, network %s"
- "connectionActivationError %d"

```
