## IDS

> `/System/Library/PrivateFrameworks/IDS.framework/Versions/A/IDS`

```diff

-1926.400.131.1.1
-  __TEXT.__text: 0x14e0f8
-  __TEXT.__auth_stubs: 0x1900
-  __TEXT.__objc_methlist: 0xa5d4
+1926.500.181.0.0
+  __TEXT.__text: 0x151358
+  __TEXT.__auth_stubs: 0x18f0
+  __TEXT.__objc_methlist: 0xc9dc
   __TEXT.__const: 0x418
-  __TEXT.__gcc_except_tab: 0x4578
-  __TEXT.__cstring: 0xf136
-  __TEXT.__oslogstring: 0x1852d
+  __TEXT.__gcc_except_tab: 0x466c
+  __TEXT.__cstring: 0xf26f
+  __TEXT.__oslogstring: 0x187ef
   __TEXT.__dlopen_cstrs: 0x102
   __TEXT.__ustring: 0xac
-  __TEXT.__unwind_info: 0x4a00
-  __TEXT.__objc_classname: 0x184d
-  __TEXT.__objc_methname: 0x1e3a1
-  __TEXT.__objc_methtype: 0x7079
-  __TEXT.__objc_stubs: 0x12ee0
-  __DATA_CONST.__got: 0x1110
-  __DATA_CONST.__const: 0xbb8
-  __DATA_CONST.__objc_classlist: 0x560
+  __TEXT.__unwind_info: 0x4b58
+  __TEXT.__objc_classname: 0x1892
+  __TEXT.__objc_methname: 0x1eab6
+  __TEXT.__objc_methtype: 0x727c
+  __TEXT.__objc_stubs: 0x13160
+  __DATA_CONST.__got: 0x1180
+  __DATA_CONST.__const: 0xb80
+  __DATA_CONST.__objc_classlist: 0x568
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x1e0
+  __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6098
-  __DATA_CONST.__objc_protorefs: 0xe8
-  __DATA_CONST.__objc_superrefs: 0x440
-  __AUTH_CONST.__auth_got: 0xc90
-  __AUTH_CONST.__const: 0x5f90
-  __AUTH_CONST.__cfstring: 0x6f40
-  __AUTH_CONST.__objc_const: 0x3c458
-  __AUTH_CONST.__objc_intobj: 0x4b0
+  __DATA_CONST.__objc_selrefs: 0x6468
+  __DATA_CONST.__objc_protorefs: 0xf0
+  __DATA_CONST.__objc_superrefs: 0x448
+  __AUTH_CONST.__auth_got: 0xc88
+  __AUTH_CONST.__const: 0x6060
+  __AUTH_CONST.__cfstring: 0x6ee0
+  __AUTH_CONST.__objc_const: 0x38fe8
+  __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x15e0
-  __DATA.__objc_ivar: 0xca8
-  __DATA.__data: 0x16b0
-  __DATA.__bss: 0x1d38
+  __AUTH.__objc_data: 0x1630
+  __DATA.__objc_ivar: 0xcd8
+  __DATA.__data: 0x1710
+  __DATA.__bss: 0x1d40
   __DATA_DIRTY.__objc_data: 0x1fe0
   __DATA_DIRTY.__bss: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 9670C90E-A0E1-358E-BAAF-F809DA332B24
-  Functions: 6162
-  Symbols:   1427
-  CStrings:  9567
+  UUID: 4F68D78F-195B-3D97-B97A-C74902F1BDB1
+  Functions: 6325
+  Symbols:   1443
+  CStrings:  9648
 
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
+ "-[_IDSGroupSession session:didReceiveParticipantUpdateParticipantID:withContext:]"
+ "-[_IDSGroupSession sessionDidReceiveParticipantUpgrade:participantType:requestIdentifier:error:]"
+ "-[_IDSGroupSession updateParticipantType:members:withContext:triggeredLocally:timestamp:identifier:]"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IdentityServices_legacy/IDS/Client/IDSDataChannels.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IdentityServices_legacy/IDS/IDSDataChannelsUtils.m"
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/IdentityServices_legacy/IDS/IDSDataChannels_Direct.m"
+ "@\"<IDSKeyTransparencyManagerDelegate>\""
+ "@104@0:8@16@24@32Q40@48@56@64@72@80@88@96"
+ "@104@0:8@16i24i28@32@40@48@56@64Q72@80@88@96"
+ "@144@0:8@16@24@32Q40@48@56@64@72@80@88@96@104@112@120@128@136"
+ "B32@0:8q16@24"
+ "BAA signer adding iCloud BAA headers!"
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
+ "T@\"NSString\",R,N,V_baaCertSource"
+ "T@?,C,N,V_clientInvalidationHandler"
+ "Ti,V_registrationType"
+ "TransparencyIDSRegistrationResponse"
+ "_baaCertSource"
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
+ "baaCertSource"
+ "clientInvalidationHandler"
+ "decodeArrayOfObjectsOfClass:forKey:"
+ "didReceiveParticipantUpdateParticipantID identifier: %@, participantID: %llu, clientContext: %@"
+ "dsid"
+ "dumpDiagnosticsWithCompletion:"
+ "getCurrentRegistrationState:withCompletion:"
+ "handleRegistrationStateUpdate:"
+ "includeIcloudBAAHeaders"
+ "initWithDelegate:"
+ "initWithResultData:timestamp:error:currentTimestampInMs:icloudDigest:icloudAltDigest:icloudResultData:icloudAltResultData:icloudError:icloudAltError:baaCertSource:"
+ "initWithResultData:timestamp:error:currentTimestampInMs:icloudDigest:icloudAltDigest:icloudResultData:icloudAltResultData:icloudError:icloudAltError:hostCertChain:hostResultData:hostAltResultData:hostError:hostAltError:baaCertSource:"
+ "initWithSHA256Digest:requestBody:serverTimestamp:includeIcloudBAA:"
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
- "/AppleInternal/Library/BuildRoots/5c0393f9-de33-11ef-b07a-ca56a3f92201/Library/Caches/com.apple.xbs/Sources/IdentityServices_legacy/IDS/Client/IDSDataChannels.m"
- "/AppleInternal/Library/BuildRoots/5c0393f9-de33-11ef-b07a-ca56a3f92201/Library/Caches/com.apple.xbs/Sources/IdentityServices_legacy/IDS/IDSDataChannelsUtils.m"
- "/AppleInternal/Library/BuildRoots/5c0393f9-de33-11ef-b07a-ca56a3f92201/Library/Caches/com.apple.xbs/Sources/IdentityServices_legacy/IDS/IDSDataChannels_Direct.m"
- "@136@0:8@16@24@32Q40@48@56@64@72@80@88@96@104@112@120@128"
- "@44@0:8@16i24B28B32Q36"
- "@96@0:8@16@24@32Q40@48@56@64@72@80@88"
- "TB,V_containsAccountKey"
- "TB,V_containsDeviceSignature"
- "_containsAccountKey"
- "_containsDeviceSignature"
- "containsAccountKey"
- "containsDeviceSignature"
- "getCurrentRegistrationStateWithCompletion:"
- "initWithResultData:timestamp:error:currentTimestampInMs:icloudDigest:icloudAltDigest:icloudResultData:icloudAltResultData:icloudError:icloudAltError:"
- "initWithResultData:timestamp:error:currentTimestampInMs:icloudDigest:icloudAltDigest:icloudResultData:icloudAltResultData:icloudError:icloudAltError:hostCertChain:hostResultData:hostAltResultData:hostError:hostAltError:"
- "initWithSHA256Digest:requestBody:serverTimestamp:"
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
