## KeychainCircle

> `/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`

```diff

-61040.62.1.0.0
-  __TEXT.__text: 0x1a62c
+61040.80.10.0.1
+  __TEXT.__text: 0x1abec
   __TEXT.__auth_stubs: 0x8b0
-  __TEXT.__objc_methlist: 0x164c
+  __TEXT.__objc_methlist: 0x167c
   __TEXT.__const: 0x64
-  __TEXT.__gcc_except_tab: 0xb04
-  __TEXT.__cstring: 0x17be
-  __TEXT.__oslogstring: 0x29f3
+  __TEXT.__gcc_except_tab: 0xb50
+  __TEXT.__cstring: 0x19c3
+  __TEXT.__oslogstring: 0x2b88
   __TEXT.__ustring: 0x32
   __TEXT.__dlopen_cstrs: 0xfc
-  __TEXT.__unwind_info: 0x5d8
+  __TEXT.__unwind_info: 0x5e0
   __TEXT.__objc_classname: 0x2e3
-  __TEXT.__objc_methname: 0x33c3
-  __TEXT.__objc_methtype: 0xd94
-  __TEXT.__objc_stubs: 0x25e0
+  __TEXT.__objc_methname: 0x34b3
+  __TEXT.__objc_methtype: 0xdd0
+  __TEXT.__objc_stubs: 0x2660
   __DATA_CONST.__got: 0x70
-  __DATA_CONST.__const: 0x918
+  __DATA_CONST.__const: 0x938
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2268
-  __DATA_CONST.__objc_selrefs: 0xbf0
+  __DATA_CONST.__objc_const: 0x2298
+  __DATA_CONST.__objc_selrefs: 0xc18
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__cfstring: 0x1b80
+  __AUTH_CONST.__cfstring: 0x1d60
   __AUTH_CONST.__objc_const: 0xa00
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__objc_dictobj: 0xc8

   __DATA.__objc_protorefs: 0x8
   __DATA.__objc_classrefs: 0x120
   __DATA.__objc_superrefs: 0x88
-  __DATA.__objc_ivar: 0x19c
+  __DATA.__objc_ivar: 0x1a0
   __DATA.__data: 0x2c8
   __DATA.__bss: 0x70
   __DATA_DIRTY.__objc_data: 0x50

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 3D885DF0-DFF8-33BB-945E-CD04042F70A4
-  Functions: 558
-  Symbols:   2085
-  CStrings:  1407
+  UUID: 8BFE5F05-25E0-31DE-BDBC-8F7E33F225FC
+  Functions: 562
+  Symbols:   2102
+  CStrings:  1454
 
Symbols:
+ -[AAFAnalyticsEventSecurity canSendMetrics]
+ -[AAFAnalyticsEventSecurity initWithCKKSMetrics:altDSID:eventName:testsAreEnabled:category:sendMetric:]
+ -[AAFAnalyticsEventSecurity initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:canSendMetrics:category:]
+ -[AAFAnalyticsEventSecurity permittedToSendMetrics]
+ -[AAFAnalyticsEventSecurity setCanSendMetrics:]
+ -[KCJoiningRequestCircleSession encryptPeerInfo:]
+ GCC_except_table426
+ GCC_except_table435
+ GCC_except_table437
+ _AAAFoundationLibraryCore.frameworkLibrary.1093
+ _OBJC_IVAR_$_AAFAnalyticsEventSecurity._canSendMetrics
+ ___AAAFoundationLibraryCore_block_invoke.1094
+ ___Block_byref_object_copy_.420
+ ___Block_byref_object_copy_.842
+ ___Block_byref_object_dispose_.421
+ ___Block_byref_object_dispose_.843
+ ___block_literal_global.1091
+ ___block_literal_global.447
+ _audit_stringAAAFoundation.1097
+ _kSecurityRTCFieldAvgCKRecords
+ _kSecurityRTCFieldAvgErrorItemsProcessed
+ _kSecurityRTCFieldAvgRemoteKeys
+ _kSecurityRTCFieldAvgSuccessfulItemsProcessed
+ _kSecurityRTCFieldTotalCKRecords
+ _kSecurityRTCFieldTotalRemoteKeys
+ _objc_msgSend$canSendMetrics
+ _objc_msgSend$circleJoiningBlob:flowID:deviceSessionID:canSendMetrics:applicant:complete:
+ _objc_msgSend$encryptPeerInfo:
+ _objc_msgSend$initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:canSendMetrics:category:
+ _objc_msgSend$initialSyncCredentials:altDSID:flowID:deviceSessionID:canSendMetrics:complete:
+ _objc_msgSend$joinCircleWithBlob:altDSID:flowID:deviceSessionID:canSendMetrics:version:complete:
+ _objc_msgSend$myPeerInfo:flowID:deviceSessionID:canSendMetrics:complete:
+ _objc_msgSend$permittedToSendMetrics
+ _objc_msgSend$stashAccountCredential:altDSID:flowID:deviceSessionID:canSendMetrics:complete:
+ _objc_msgSend$testsEnabled
+ _objc_msgSend$validatedStashedAccountCredential:flowID:deviceSessionID:canSendMetrics:complete:
- -[AAFAnalyticsEventSecurity initWithCKKSMetrics:altDSID:eventName:testsAreEnabled:category:]
- -[AAFAnalyticsEventSecurity initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:category:]
- GCC_except_table425
- GCC_except_table434
- GCC_except_table436
- _AAAFoundationLibraryCore.frameworkLibrary.1061
- ___AAAFoundationLibraryCore_block_invoke.1062
- ___Block_byref_object_copy_.391
- ___Block_byref_object_copy_.822
- ___Block_byref_object_dispose_.392
- ___Block_byref_object_dispose_.823
- ___block_literal_global.1059
- ___block_literal_global.409
- _audit_stringAAAFoundation.1065
- _kSecurityRTCFieldNumCKRecords
- _kSecurityRTCFieldNumRemoteKeys
- _objc_msgSend$circleJoiningBlob:flowID:deviceSessionID:applicant:complete:
- _objc_msgSend$initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:category:
- _objc_msgSend$initialSyncCredentials:altDSID:flowID:deviceSessionID:complete:
- _objc_msgSend$joinCircleWithBlob:altDSID:flowID:deviceSessionID:version:complete:
- _objc_msgSend$myPeerInfo:flowID:deviceSessionID:complete:
- _objc_msgSend$stashAccountCredential:altDSID:flowID:deviceSessionID:complete:
- _objc_msgSend$validatedStashedAccountCredential:flowID:deviceSessionID:complete:
CStrings:
+ "@56@0:8@16@24@32B40@44B52"
+ "@72@0:8@16@24@32@40@48B56B60@64"
+ "Failed to decrypt circleBlob"
+ "Failed to process circleBlob"
+ "Missing voucher from acceptor"
+ "SOS not enabled for this platform"
+ "SOS not enabled, skipping peer info encryption"
+ "TB,V_canSendMetrics"
+ "Timed out waiting for epoch rpc"
+ "Timed out waiting for join rpc"
+ "Unable to piggyback with device due to lack of trust system support"
+ "_canSendMetrics"
+ "avgCKRecords"
+ "avgErrorItemsProcessed"
+ "avgRemoteKeys"
+ "avgSuccessfulItemsProcessed"
+ "canSendMetrics"
+ "circleJoiningBlob:flowID:deviceSessionID:canSendMetrics:applicant:complete:"
+ "device does not support SOS nor piggybacking version 2"
+ "device supports SOS, continuing flow with piggyV1"
+ "encryptPeerInfo:"
+ "expected acceptor epoch"
+ "failed to encrypt the SOS peer info"
+ "initWithCKKSMetrics:altDSID:eventName:testsAreEnabled:category:sendMetric:"
+ "initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:canSendMetrics:category:"
+ "initialSyncCredentials:altDSID:flowID:deviceSessionID:canSendMetrics:complete:"
+ "joinCircleWithBlob:altDSID:flowID:deviceSessionID:canSendMetrics:version:complete:"
+ "joining: circleBlob is nil"
+ "joining: device does not support SOS nor piggybacking version 2"
+ "joining: device does not support SOS, failing flow"
+ "joining: expected acceptor epoch! returning nil."
+ "joining: failed to copy srpMessage: %@"
+ "joining: failed to create encrypted peerInfo: %@"
+ "joining: failed to extract startMessage: %@"
+ "joining: failed to process SOS circle"
+ "joining: octagon refusing octagon acceptor since we don't have a selfEgo"
+ "myPeerInfo:flowID:deviceSessionID:canSendMetrics:complete:"
+ "permittedToSendMetrics"
+ "setCanSendMetrics:"
+ "stashAccountCredential:altDSID:flowID:deviceSessionID:canSendMetrics:complete:"
+ "testsEnabled"
+ "timed out producing octagon voucher"
+ "timed out waiting for rpcPrepareIdentityAsApplicantWithArguments"
+ "totalCKRecords"
+ "totalRemoteKeys"
+ "v52@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32B40@?<v@?@\"NSData\"@\"NSError\">44"
+ "v52@0:8@16@24@32B40@?44"
+ "v56@0:8I16@\"NSString\"20@\"NSString\"28@\"NSString\"36B44@?<v@?@\"NSArray\"@\"NSError\">48"
+ "v56@0:8I16@20@28@36B44@?48"
+ "v60@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40B48@?<v@?B@\"NSError\">52"
+ "v60@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32B40@\"NSData\"44@?<v@?@\"NSData\"@\"NSError\">52"
+ "v60@0:8@16@24@32@40B48@?52"
+ "v60@0:8@16@24@32B40@44@?52"
+ "v64@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40B48i52@?<v@?B@\"NSError\">56"
+ "v64@0:8@16@24@32@40B48i52@?56"
+ "validatedStashedAccountCredential:flowID:deviceSessionID:canSendMetrics:complete:"
- "@52@0:8@16@24@32B40@44"
- "@68@0:8@16@24@32@40@48B56@60"
- "circleJoiningBlob:flowID:deviceSessionID:applicant:complete:"
- "initWithCKKSMetrics:altDSID:eventName:testsAreEnabled:category:"
- "initWithKeychainCircleMetrics:altDSID:flowID:deviceSessionID:eventName:testsAreEnabled:category:"
- "initialSyncCredentials:altDSID:flowID:deviceSessionID:complete:"
- "joinCircleWithBlob:altDSID:flowID:deviceSessionID:version:complete:"
- "myPeerInfo:flowID:deviceSessionID:complete:"
- "no platform support for encryptedPeerInfo"
- "numCKRecords"
- "numRemoteKeys"
- "octagon refusing octagon acceptor since we don't have a selfEgo"
- "octagon: expected epoch! returning from piggybacking."
- "stashAccountCredential:altDSID:flowID:deviceSessionID:complete:"
- "v48@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@?<v@?@\"NSData\"@\"NSError\">40"
- "v48@0:8@16@24@32@?40"
- "v52@0:8I16@\"NSString\"20@\"NSString\"28@\"NSString\"36@?<v@?@\"NSArray\"@\"NSError\">44"
- "v52@0:8I16@20@28@36@?44"
- "v56@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@?<v@?B@\"NSError\">48"
- "v56@0:8@\"NSString\"16@\"NSString\"24@\"NSString\"32@\"NSData\"40@?<v@?@\"NSData\"@\"NSError\">48"
- "v56@0:8@16@24@32@40@?48"
- "v60@0:8@\"NSData\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40i48@?<v@?B@\"NSError\">52"
- "v60@0:8@16@24@32@40i48@?52"
- "validatedStashedAccountCredential:flowID:deviceSessionID:complete:"

```
