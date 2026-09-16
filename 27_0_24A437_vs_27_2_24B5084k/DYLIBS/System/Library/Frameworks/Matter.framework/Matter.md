## Matter

> `/System/Library/Frameworks/Matter.framework/Matter`

```diff

-324.0.0.0.0
-  __TEXT.__text: 0x82cbf4
-  __TEXT.__objc_methlist: 0x5e054
-  __TEXT.__const: 0x64189
-  __TEXT.__gcc_except_tab: 0xc4460
-  __TEXT.__cstring: 0x301aa
-  __TEXT.__oslogstring: 0x1b37e
+331.0.0.0.0
+  __TEXT.__text: 0x8328c8
+  __TEXT.__objc_methlist: 0x5eedc
+  __TEXT.__const: 0x651b9
+  __TEXT.__gcc_except_tab: 0xc6fe0
+  __TEXT.__cstring: 0x30b45
+  __TEXT.__oslogstring: 0x1b314
   __TEXT.__dlopen_cstrs: 0x45
-  __TEXT.__unwind_info: 0x52f50
+  __TEXT.__unwind_info: 0x53968
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x12c40
-  __DATA_CONST.__objc_classlist: 0x30a0
+  __DATA_CONST.__const: 0x12d08
+  __DATA_CONST.__objc_classlist: 0x30f8
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1c7e8
+  __DATA_CONST.__objc_selrefs: 0x1cd28
   __DATA_CONST.__objc_protorefs: 0x20
-  __DATA_CONST.__objc_superrefs: 0x2248
+  __DATA_CONST.__objc_superrefs: 0x2280
   __DATA_CONST.__objc_arraydata: 0x38
-  __DATA_CONST.__got: 0x23b0
-  __AUTH_CONST.__const: 0x1c820
-  __AUTH_CONST.__cfstring: 0x183c0
-  __AUTH_CONST.__objc_const: 0x76178
+  __DATA_CONST.__got: 0x23f8
+  __AUTH_CONST.__const: 0x1cdc0
+  __AUTH_CONST.__cfstring: 0x18900
+  __AUTH_CONST.__objc_const: 0x76f20
   __AUTH_CONST.__weak_auth_got: 0x38
-  __AUTH_CONST.__objc_intobj: 0x6a68
+  __AUTH_CONST.__objc_intobj: 0x6de0
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x28
-  __AUTH_CONST.__auth_got: 0x998
-  __AUTH.__objc_data: 0x1e640
+  __AUTH_CONST.__auth_got: 0x9d8
+  __AUTH.__objc_data: 0x1e9b0
   __AUTH.__data: 0x1a0
   __AUTH.__thread_vars: 0x30
   __AUTH.__thread_bss: 0x180
-  __DATA.__objc_ivar: 0x4038
-  __DATA.__data: 0x6110
+  __DATA.__objc_ivar: 0x40c0
+  __DATA.__data: 0x6118
   __DATA.__common: 0x490
   __DATA_DIRTY.__data: 0x10
   __DATA_DIRTY.__common: 0x6b0

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/NearField.framework/NearField
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libdns_services.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 52650
-  Symbols:   3455
-  CStrings:  8934
+  Functions: 52973
+  Symbols:   3482
+  CStrings:  9001
 
Symbols:
+ _CFEqual
+ _CFStringCreateWithCStringNoCopy
+ _CFStringFind
+ _OBJC_CLASS_$_MTRAccountLoginClusterGetDeviceAuthURIParams
+ _OBJC_CLASS_$_MTRAccountLoginClusterGetDeviceAuthURIResponseParams
+ _OBJC_CLASS_$_MTRAmbientSensingUnionClusterContributorStatusChangeStruct
+ _OBJC_CLASS_$_MTRClusterAppleAccessoryConfiguration
+ _OBJC_CLASS_$_MTRClusterAppleProximityBLEAdvertising
+ _OBJC_CLASS_$_MTRMessagesClusterMessageNotPresentedEvent
+ _OBJC_CLASS_$_MTRProximityRangingClusterRangingConstraintStruct
+ _OBJC_CLASS_$_MTRPushAVStreamTransportClusterUpdateMotionZoneOptionsParams
+ _OBJC_METACLASS_$_MTRAccountLoginClusterGetDeviceAuthURIParams
+ _OBJC_METACLASS_$_MTRAccountLoginClusterGetDeviceAuthURIResponseParams
+ _OBJC_METACLASS_$_MTRAmbientSensingUnionClusterContributorStatusChangeStruct
+ _OBJC_METACLASS_$_MTRClusterAppleAccessoryConfiguration
+ _OBJC_METACLASS_$_MTRClusterAppleProximityBLEAdvertising
+ _OBJC_METACLASS_$_MTRMessagesClusterMessageNotPresentedEvent
+ _OBJC_METACLASS_$_MTRProximityRangingClusterRangingConstraintStruct
+ _OBJC_METACLASS_$_MTRPushAVStreamTransportClusterUpdateMotionZoneOptionsParams
+ _SCNetworkInterfaceGetInterfaceType
+ __SCNetworkInterfaceCreateWithBSDName
+ __SCNetworkInterfaceGetIOPath
+ __SCNetworkInterfaceIsHiddenConfiguration
+ __SCNetworkInterfaceIsHiddenInterface
+ _kCFAllocatorNull
+ _kSCNetworkInterfaceTypeEthernet
+ _kSCNetworkInterfaceTypeIEEE80211
CStrings:
+ "%s:%d false: %s"
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CHIPFramework/connectedhomeip/src/protocols/bdx/AsyncTransferFacilitator.h"
+ "<%@: connectionID:%@; motionZones:%@; motionSensitivity:%@; >"
+ "<%@: contributorIndex:%@; previousContributorStatus:%@; currentContributorStatus:%@; >"
+ "<%@: contributorNodeID:%@; contributorEndpointID:%@; contributorName:%@; contributorStatus:%@; >"
+ "<%@: contributorStatusChange:%@; >"
+ "<%@: messageID:%@; priority:%@; messageControl:%@; startTime:%@; duration:%@; messageText:%@; responses:%@; languageCode:%@; messageURI:%@; >"
+ "<%@: messageID:%@; removedFromQueue:%@; fabricIndex:%@; >"
+ "<%@: role:%@; peerBLEDeviceID:%@; blerbcSecurityMode:%@; sessionKey:%@; >"
+ "<%@: technology:%@; frequencyBand:%@; bandwidth:%@; supportedRangingRoles:%@; rdrCapability:%@; periodicRangingSupport:%@; maxConcurrentSessions:%@; >"
+ "<%@: technology:%@; role:%@; enabled:%@; minRangingInterval:%@; maxSessionDuration:%@; maxRangingInstances:%@; >"
+ "<%@: technology:%@; wiFiRangingDeviceRoleConfig:%@; bleRangingDeviceRoleConfig:%@; bltChannelSoundingDeviceRoleConfig:%@; frequencyBand:%@; bandwidth:%@; trigger:%@; reportingCondition:%@; >"
+ "<%@: tripMechanism:%@; protectionClass:%@; protectionType:%@; maxContinuousOperatingVoltage:%@; maxVoltageProtection:%@; maxTemporaryVoltage:%@; nominalDischargeCurrent:%@; maximumDischargeCurrent:%@; ratedShortCircuitCurrent:%@; ratedShortTimeWithstandCurrent:%@; energyAbsorptionCapability:%@; responseTime:%@; >"
+ "<%@: userCode:%@; verificationURI:%@; verificationURIComplete:%@; expiresIn:%@; interval:%@; >"
+ "AV Analysis Node"
+ "AdditionalAccessoryConfigurationAvailable"
+ "Advertiser not initialized"
+ "AdvertisingEnabled"
+ "AppleAccessoryConfiguration"
+ "AppleDelayedEndTime"
+ "AppleDelayedStartTime"
+ "AppleProximityBLEAdvertising"
+ "AppleReadyState"
+ "AppleUSB"
+ "Arc Fault Circuit Interrupter"
+ "Attestation nonce length is invalid"
+ "BDXTransferTimeoutInSeconds"
+ "BlockingAccessoryFunctionality"
+ "CSR nonce length is invalid"
+ "CondPumpEnabled"
+ "CondRunCount"
+ "Country code is too large"
+ "Darwin IP address scorer installed"
+ "DeviceRebootCompleted"
+ "DeviceRebootDurationToRecovery"
+ "DeviceSessionLossCount"
+ "Electrical Surge Protector"
+ "Error %s"
+ "Failed to advertise commissionable node"
+ "Failed to advertise operational node"
+ "Failed to establish CASE session with peer <%08X%08X, %d>. Error: %s"
+ "Failed to finalize service update"
+ "Failed to initialize advertiser"
+ "Failed to remove advertised services"
+ "Failed to start commissioning"
+ "Failure accepting incoming connection"
+ "Food Thermometer"
+ "GetDeviceAuthURI"
+ "GetDeviceAuthURIResponse"
+ "Got a user default value for BDX transfer timeout - %d seconds"
+ "Irrigation System"
+ "MessageNotPresented"
+ "No Wi-Fi credentials configured at commissioner!"
+ "OAuthLoggedIn"
+ "PROXY:%u"
+ "Posting DNS-SD platform initialized event failed with"
+ "ProxyTransport: activating session %u"
+ "ProxyTransport: deactivating session %u"
+ "ProxyTransport: empty message for session %u"
+ "ProxyTransport: forwarding %u bytes for session %u"
+ "ProxyTransport: injecting %u bytes for session %u into Matter stack"
+ "ProxyTransport: out of memory for received message"
+ "ProxyTransport: received message for unknown session %u (active=%d, expected=%u)"
+ "RangingConstraints"
+ "ResetCountBootRelativeTime"
+ "Residual Current Circuit Breaker"
+ "SetUpCodePairer: dropping duplicate discovered rendezvous parameters"
+ "Subscription 0x%08x to peer <%08X%08X, %d>: CASE session hung, initiating recovery"
+ "SuccessOrDie failure %s at %s:%d"
+ "SupportedLanguageCodes"
+ "ThreadFirstRestartCompleted"
+ "ThreadFirstRestartConnectivityState"
+ "ThreadFirstRestartRecoveryTime"
+ "ThreadRecoveryAttemptCount"
+ "ThreadRestartCount"
+ "ThreadTransportLossCount"
+ "Too many targeted endpoints in invoke, capping at %u"
+ "Treating NetworkIDNotFound as success for network removal"
+ "UpdateMotionZoneOptions"
+ "VerifyOrDie failure at %s:%d"
+ "WiFiCredentials.credentials is too large"
+ "WiFiCredentials.ssid is too large"
+ "WiFiFirstRestartCompleted"
+ "WiFiFirstRestartConnectivityState"
+ "WiFiFirstRestartRecoveryTime"
+ "WiFiRecoveryAttemptCount"
+ "WiFiRestartCount"
+ "WiFiTransportLossCount"
+ "ir0"
+ "src/app/CommandHandler.h"
+ "src/app/MessageDef/InvokeRequestMessage.cpp"
+ "src/protocols/bdx/StatusCode.cpp"
+ "src/transport/raw/ProxyTransport.cpp"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CHIPFramework/connectedhomeip/src/app/CommandHandler.h"
- "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/CHIPFramework/connectedhomeip/src/lib/support/Variant.h"
- "<%@: contributorNodeID:%@; contributorEndpointID:%@; contributorName:%@; contributorHealth:%@; >"
- "<%@: messageID:%@; priority:%@; messageControl:%@; startTime:%@; duration:%@; messageText:%@; responses:%@; >"
- "<%@: resultCode:%@; sessionID:%@; >"
- "<%@: role:%@; peerBLEDeviceID:%@; >"
- "<%@: statusChangedContributor:%@; >"
- "<%@: technology:%@; frequencyBand:%@; periodicRangingSupport:%@; >"
- "<%@: technology:%@; wiFiRangingDeviceRoleConfig:%@; bleRangingDeviceRoleConfig:%@; bltChannelSoundingDeviceRoleConfig:%@; frequencyBand:%@; bandwidth:%@; securityMode:%@; trigger:%@; reportingCondition:%@; >"
- "<%@: tripMechanism:%@; protectionClass:%@; protectionType:%@; maxContinuousOperatingVoltage:%@; maxVoltageProtection:%@; maxTemporaryVoltage:%@; nominalDischargeCurrent:%@; maximumDishargeCurrent:%@; ratedShortCircuitCurrent:%@; ratedShortTimeWithstandCurrent:%@; energyAbsorptionCapability:%@; responseTime:%@; >"
- "AppleFoodThermometerConnected"
- "AppleFoodThermometerCurrentTemperature"
- "AppleFoodThermometerTargetTemperature"
- "Country code is too large: %u"
- "Failed to advertise commissionable node: %s"
- "Failed to advertise operational node: %s"
- "Failed to finalize service update: %s"
- "Failed to initialize advertiser: %s"
- "Failed to start commissioning: %s"
- "Failure accepting incoming connection: %s"
- "NFCBase::OnNfcTagResponse"
- "Posting DNS-SD platform initialized event failed with: %s"
- "Wifi credentials are too large"
- "discriminator == (discriminator & kShortMask)"
- "mValue.type == Value::Type::kChipErrorCode"
- "mValue.type == Value::Type::kInt32"
```
