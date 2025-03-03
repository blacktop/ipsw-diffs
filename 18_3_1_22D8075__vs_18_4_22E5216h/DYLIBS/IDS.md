## IDS

> `/System/Library/PrivateFrameworks/IDS.framework/IDS`

```diff

-1926.400.131.2.2
-  __TEXT.__text: 0x1367a4
-  __TEXT.__auth_stubs: 0x1b60
-  __TEXT.__objc_methlist: 0xa5fc
+1926.500.161.2.2
+  __TEXT.__text: 0x1393bc
+  __TEXT.__auth_stubs: 0x1b50
+  __TEXT.__objc_methlist: 0xca2c
   __TEXT.__const: 0x430
-  __TEXT.__gcc_except_tab: 0x450c
-  __TEXT.__oslogstring: 0x1871a
-  __TEXT.__cstring: 0x100fb
+  __TEXT.__gcc_except_tab: 0x4600
+  __TEXT.__oslogstring: 0x189b6
+  __TEXT.__cstring: 0x10234
   __TEXT.__dlopen_cstrs: 0x102
   __TEXT.__ustring: 0xac
-  __TEXT.__unwind_info: 0x4a50
-  __TEXT.__objc_classname: 0x186a
-  __TEXT.__objc_methname: 0x1e50a
-  __TEXT.__objc_methtype: 0x70ab
-  __TEXT.__objc_stubs: 0x133a0
-  __DATA_CONST.__got: 0x1120
-  __DATA_CONST.__const: 0x4df0
-  __DATA_CONST.__objc_classlist: 0x560
+  __TEXT.__unwind_info: 0x4be0
+  __TEXT.__objc_classname: 0x18af
+  __TEXT.__objc_methname: 0x1eb9c
+  __TEXT.__objc_methtype: 0x72a6
+  __TEXT.__objc_stubs: 0x135e0
+  __DATA_CONST.__got: 0x1190
+  __DATA_CONST.__const: 0x4e30
+  __DATA_CONST.__objc_classlist: 0x568
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x1e8
+  __DATA_CONST.__objc_protolist: 0x1f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6160
-  __DATA_CONST.__objc_protorefs: 0xe8
-  __DATA_CONST.__objc_superrefs: 0x448
-  __AUTH_CONST.__auth_got: 0xdc0
+  __DATA_CONST.__objc_selrefs: 0x64b0
+  __DATA_CONST.__objc_protorefs: 0xf0
+  __DATA_CONST.__objc_superrefs: 0x450
+  __AUTH_CONST.__auth_got: 0xdb8
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x1760
-  __AUTH_CONST.__cfstring: 0x70a0
-  __AUTH_CONST.__objc_const: 0x3c828
-  __AUTH_CONST.__objc_intobj: 0x4b0
+  __AUTH_CONST.__const: 0x17a0
+  __AUTH_CONST.__cfstring: 0x7040
+  __AUTH_CONST.__objc_const: 0x39338
+  __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH.__objc_data: 0x19f0
-  __DATA.__objc_ivar: 0xcac
-  __DATA.__data: 0x1710
-  __DATA.__bss: 0x1b2c
-  __DATA_DIRTY.__objc_data: 0x1bd0
-  __DATA_DIRTY.__bss: 0x330
+  __DATA.__objc_ivar: 0xcd8
+  __DATA.__data: 0x1770
+  __DATA.__bss: 0x1b14
+  __DATA_DIRTY.__objc_data: 0x1c20
+  __DATA_DIRTY.__bss: 0x350
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 6147
-  Symbols:   1489
-  CStrings:  8804
+  Functions: 6309
+  Symbols:   1505
+  CStrings:  8885
 
Symbols:
+ _IDSBAACertHeader
+ _IDSBAADeviceTypeHeader
+ _IDSBAAErrorHeader
+ _IDSBAAHostCertHeader
+ _IDSBAAHostErrorHeader
+ _IDSBAAHostSigAltHeader
+ _IDSBAAHostSigHeader
+ _IDSBAASigAltHeader
+ _IDSBAASigHeader
+ _IDSBAASourceHeader
+ _IDSBAASupportedHeader
+ _IDSBAATimeHeader
+ _IDSBAAVersionHeader
+ _IDSSendMessageOptionGoupUUIDKey
+ _IDSSendMessageOptionTimestampKey
+ _OBJC_CLASS_$_IDSRegistrationStateRequest
+ _OBJC_METACLASS_$_IDSRegistrationStateRequest
- _strcmp
CStrings:
+ "\x06\x11"
+ "\x16\x13"
+ "-[_IDSGroupSession session:didReceiveParticipantUpdateParticipantID:withContext:]"
+ "-[_IDSGroupSession sessionDidReceiveParticipantUpgrade:participantType:requestIdentifier:error:]"
+ "-[_IDSGroupSession updateParticipantType:members:withContext:triggeredLocally:timestamp:identifier:]"
+ "@\"<IDSKeyTransparencyManagerDelegate>\""
+ "@104@0:8@16i24i28@32@40@48@56@64Q72@80@88@96"
+ "B32@0:8q16@24"
+ "Class getTransparencyIDSRegistrationResponseClass(void)_block_invoke"
+ "IDSRegistrationStateRequest"
+ "IDSSendMessageOptionGoupUUIDKey"
+ "IDSSendMessageOptionTimestampKey"
+ "IDSXPCKeyTransparencyManagerClient"
+ "Ignoring didReceiveParticipantUpdateParticipantID, session doesn't match %@ vs. %@"
+ "Invalid metric type: %ld"
+ "Metric type IncomingMessageMetrics requires a timestampDictionary."
+ "Metric type StorageMessagesProcessed requires a timestamp."
+ "No valid service identifier to noteMetricOfType."
+ "Readding aliases to account in case we missed the authenticated state"
+ "Setting up xpc for new IDSKeyTransparencyManager"
+ "T@\"<IDSKeyTransparencyManagerDelegate>\",W,N,V_delegate"
+ "T@\"NSArray\",&,N,V_servicesToFetch"
+ "T@\"NSData\",&,V_deviceSignature"
+ "T@\"NSData\",&,V_ktAccountKey"
+ "T@\"NSData\",&,V_ktDataForRegistration"
+ "T@\"NSDate\",&,V_ktAccountKeyTimestamp"
+ "T@\"NSDate\",&,V_ktOptInTimestamp"
+ "T@\"NSNumber\",&,V_ktAccountKeyErrorCode"
+ "T@\"NSNumber\",&,V_ktOptInErrorCode"
+ "T@\"NSString\",&,V_dsid"
+ "T@?,C,N,V_clientInvalidationHandler"
+ "Ti,V_registrationType"
+ "TransparencyIDSRegistrationResponse"
+ "_clientInvalidationHandler"
+ "_deviceSignature"
+ "_dsid"
+ "_ktAccountKey"
+ "_ktAccountKeyErrorCode"
+ "_ktAccountKeyTimestamp"
+ "_ktDataForRegistration"
+ "_ktOptInErrorCode"
+ "_ktOptInTimestamp"
+ "_registrationType"
+ "_servicesToFetch"
+ "_setupXPC:"
+ "accountKeyErrorCode"
+ "accountKeyTimestamp"
+ "clientInvalidationHandler"
+ "decodeArrayOfObjectsOfClass:forKey:"
+ "didReceiveParticipantUpdateParticipantID identifier: %@, participantID: %llu, clientContext: %@"
+ "dsid"
+ "dumpDiagnosticsWithCompletion:"
+ "getCurrentRegistrationState:withCompletion:"
+ "handleRegistrationStateUpdate:"
+ "initWithDelegate:"
+ "initWithServicesToFetch:"
+ "initWithUserID:registrationType:registrationStatus:ktAccountKey:accountKeyTimestamp:accountKeyErrorCode:deviceSignature:ktDataForRegistration:optedIn:optedInTimestamp:optedInErrorCode:dsid:"
+ "ktAccountKey"
+ "ktAccountKeyErrorCode"
+ "ktAccountKeyTimestamp"
+ "ktDataForRegistration"
+ "ktOptInErrorCode"
+ "ktOptInTimestamp"
+ "noteMetricOfType:context:"
+ "noteMetricOfType:context:serviceName:"
+ "optedInErrorCode"
+ "optedInTimestamp"
+ "regType"
+ "registrationMightNeedUpdate:"
+ "registrationType"
+ "servicesToFetch"
+ "session:didReceiveParticipantUpdateParticipantID:withContext:"
+ "sessionDidReceiveParticipantUpgrade %@, type: %u, requestIdentifier: %llu, error: %@"
+ "sessionDidReceiveParticipantUpgrade:participantType:requestIdentifier:error:"
+ "setClientInvalidationHandler:"
+ "setDedupeTimestamp:"
+ "setDeviceSignature:"
+ "setDsid:"
+ "setGroupSessionUUID:"
+ "setKtAccountKey:"
+ "setKtAccountKeyErrorCode:"
+ "setKtAccountKeyTimestamp:"
+ "setKtDataForRegistration:"
+ "setKtOptInErrorCode:"
+ "setKtOptInTimestamp:"
+ "setRegistrationType:"
+ "setServicesToFetch:"
+ "setupKeyTransparencyManager:uuid:"
+ "timestampDictionary"
+ "transparencyManager:registrationStateUpdated:"
+ "updateParticipantType to %u, _destinationsLightweightStatus: %@ withIdentifier: %llu"
+ "updateParticipantType:forGroup:sessionID:members:triggeredLocally:withContext:lightweightStatusDict:timestamp:identifier:"
+ "updateParticipantType:members:withContext:triggeredLocally:timestamp:identifier:"
+ "v24@0:8@\"TransparencyIDSRegistrationResponse\"16"
+ "v32@0:8@\"<IDSXPCKeyTransparencyManagerClient>\"16@\"NSString\"24"
+ "v32@0:8@\"IDSRegistrationStateRequest\"16@?<v@?@\"NSDictionary\">24"
+ "v40@0:8q16@\"IDSServiceMetricContext\"24@\"NSString\"32"
+ "v44@0:8@\"NSString\"16S24Q28@\"NSError\"36"
+ "v44@0:8@16S24Q28@36"
+ "v56@0:8S16@20@28B36d40Q48"
+ "v80@0:8S16@\"NSString\"20@\"NSString\"28@\"NSArray\"36B44@\"NSData\"48@\"NSDictionary\"56d64Q72"
+ "v80@0:8S16@20@28@36B44@48@56d64Q72"
- "@44@0:8@16i24B28B32Q36"
- "TB,V_containsAccountKey"
- "TB,V_containsDeviceSignature"
- "_containsAccountKey"
- "_containsDeviceSignature"
- "containsAccountKey"
- "containsDeviceSignature"
- "getCurrentRegistrationStateWithCompletion:"
- "initWithUserID:registrationStatus:containsAccountKey:containsDeviceSignature:optedIn:"
- "setContainsAccountKey:"
- "setContainsDeviceSignature:"
- "x-apple-baa-cert"
- "x-apple-baa-error"
- "x-apple-baa-host-cert"
- "x-apple-baa-host-error"
- "x-apple-baa-host-sig"
- "x-apple-baa-host-sig-alt"
- "x-apple-baa-sig"
- "x-apple-baa-sig-alt"
- "x-apple-baa-supported"
- "x-apple-baa-time"
- "x-apple-baa-version"
- "x-apple-i-device-type"

```
