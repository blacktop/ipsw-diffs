## KeychainCircle

> `/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`

```diff

-61439.82.1.0.0
-  __TEXT.__text: 0x26be0
-  __TEXT.__auth_stubs: 0x1030
-  __TEXT.__objc_methlist: 0x18e4
-  __TEXT.__const: 0xd0
-  __TEXT.__cstring: 0x23f2
-  __TEXT.__gcc_except_tab: 0x130c
-  __TEXT.__oslogstring: 0x33c8
+61439.100.301.0.0
+  __TEXT.__text: 0x28ecc
+  __TEXT.__auth_stubs: 0x1010
+  __TEXT.__objc_methlist: 0x1d44
+  __TEXT.__const: 0xd8
   __TEXT.__dlopen_cstrs: 0x200
+  __TEXT.__gcc_except_tab: 0x15d8
+  __TEXT.__cstring: 0x2cbc
+  __TEXT.__oslogstring: 0x383b
   __TEXT.__ustring: 0x32
-  __TEXT.__unwind_info: 0x860
+  __TEXT.__unwind_info: 0x858
   __TEXT.__objc_classname: 0x2e4
-  __TEXT.__objc_methname: 0x3df5
-  __TEXT.__objc_methtype: 0xec7
-  __TEXT.__objc_stubs: 0x2e60
-  __DATA_CONST.__got: 0x2d8
-  __DATA_CONST.__const: 0x1050
+  __TEXT.__objc_methname: 0x40d5
+  __TEXT.__objc_methtype: 0xf52
+  __TEXT.__objc_stubs: 0x2ea0
+  __DATA_CONST.__got: 0x2d0
+  __DATA_CONST.__const: 0x10a0
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xe70
+  __DATA_CONST.__objc_selrefs: 0xfe8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x828
-  __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__const: 0x220
-  __AUTH_CONST.__cfstring: 0x2800
-  __AUTH_CONST.__objc_const: 0x2ea8
+  __AUTH_CONST.__auth_got: 0x818
+  __AUTH_CONST.__auth_ptr: 0x8
+  __AUTH_CONST.__const: 0x1e0
+  __AUTH_CONST.__cfstring: 0x3060
+  __AUTH_CONST.__objc_const: 0x2ac0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x5a0
-  __DATA.__objc_ivar: 0x1cc
+  __DATA.__objc_ivar: 0x1f8
   __DATA.__data: 0x318
-  __DATA.__bss: 0x188
+  __DATA.__bss: 0x170
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__bss: 0x68
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/Frameworks/Security.framework/Security
+  - /System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 763
-  Symbols:   1302
-  CStrings:  1522
+  Functions: 777
+  Symbols:   1353
+  CStrings:  1615
 
Symbols:
+ _aks_assert_drop
+ _aks_assert_hold
+ _aks_create_bag
+ _aks_save_bag
+ _aks_unload_bag
+ _kSecMatchLimitOne
+ _kSecReturnPersistentRef
+ _kSecValuePersistentRef
+ _kSecurityRTCEventNameEstablish
+ _kSecurityRTCEventNameEstablishOperation
+ _kSecurityRTCEventNameFetchAfterEstablish
+ _kSecurityRTCEventNameFetchRecoverableTLKShares
+ _kSecurityRTCEventNameHandleRecoveryResults
+ _kSecurityRTCEventNameHandleRecoveryResultsResetAndEstablish
+ _kSecurityRTCEventNameJoinWithVoucherInTPH
+ _kSecurityRTCEventNameJoinWithVoucherOperation
+ _kSecurityRTCEventNameOnqueueEstablishTPH
+ _kSecurityRTCEventNamePairingFailedToFetchItemForPersistentRef
+ _kSecurityRTCEventNamePerformEscrowRecovery
+ _kSecurityRTCEventNamePerformSilentEscrowRecovery
+ _kSecurityRTCEventNamePiggybackingAcceptorInitialMessage
+ _kSecurityRTCEventNamePiggybackingAcceptorProcessApplication
+ _kSecurityRTCEventNamePiggybackingAcceptorProcessMessage
+ _kSecurityRTCEventNamePiggybackingCircleInitiatorHandleCircleBlobMessage
+ _kSecurityRTCEventNamePiggybackingCircleInitiatorInitialMessage
+ _kSecurityRTCEventNamePiggybackingSessionInitiatorHandleChallenge
+ _kSecurityRTCEventNamePiggybackingSessionInitiatorHandleVerification
+ _kSecurityRTCEventNamePiggybackingSessionInitiatorInitialMessage
+ _kSecurityRTCEventNamePreflightVouchWithBottle
+ _kSecurityRTCEventNameRecoverSilentWithCDPContext
+ _kSecurityRTCEventNameRecoverWithCDPContext
+ _kSecurityRTCEventNameRecoverWithInfo
+ _kSecurityRTCEventNameRestoreFromBottleEvent
+ _kSecurityRTCEventNameRestoreKeychainAsyncWithPassword
+ _kSecurityRTCEventNameVouchWithBottle
+ _kSecurityRTCEventNameVouchWithBottleTPH
+ _kSecurityRTCFieldMissingDigest
+ _kSecurityRTCFieldMissingPassword
+ _kSecurityRTCFieldRecordDataMissing
+ _kSecurityRTCFieldTotalNumberOfCustodians
+ _kSecurityRTCFieldTotalNumberOfDistrustedRecoveryKeys
+ _kSecurityRTCFieldTotalNumberOfPeers
+ _kSecurityRTCFieldTotalNumberOfPreapprovals
+ _kSecurityRTCFieldTotalNumberOfRecoveryKeys
+ _kSecurityRTCFieldTotalNumberOfTrustedCustodians
+ _kSecurityRTCFieldTotalNumberOfTrustedRecoveryKeys
+ _objc_retain_x6
- _IOConnectCallMethod
- _IOServiceClose
- _IOServiceGetMatchingService
- _IOServiceMatching
- _IOServiceOpen
- ___stdoutp
- _calloc
- _fprintf
- _kIOMasterPortDefault
- _kSecurityRTCEventNameJoin
- _kSecurityRTCEventNameTrustedDeviceListRefresh
- _mach_task_self_
- _memcpy
CStrings:
+ "\x12\x11\x11&"
+ "\x12\x16"
+ "\x141"
+ "\x1b"
+ "@64@0:8@16@24@32@40@48^@56"
+ "@64@0:8@16Q24@32@40@48^@56"
+ "@72@0:8@16@24@32@40@48@56^@64"
+ "@72@0:8@16Q24@32@40@48^{ccrng_state=^?}56^@64"
+ "@80@0:8@16@24@32Q40@48@56@64^@72"
+ "@80@0:8@16@24Q32@40@48@56^{ccrng_state=^?}64^@72"
+ "Failed to copy srpMessage"
+ "Failed to copy start message"
+ "Failed to create challenge message"
+ "Failed to create circle blob response message"
+ "Failed to create error response message"
+ "Failed to create response message"
+ "Failed to create response message: %@"
+ "Failed to create tlk request response message"
+ "Failed to decrypt and verify circleBlob"
+ "Failed to decrypt and verify message"
+ "Failed to encode data"
+ "Failed to encrypt encoded data"
+ "Failed to extract startMessage"
+ "Failed to process SOS Application"
+ "Failed to process circle join data"
+ "L"
+ "SecItemCopyMatching: %d"
+ "T@\"NSArray\",&,N,V_allPCSItemPersistentRefs"
+ "T@\"NSString\",&,N,V_altDSID"
+ "T@\"NSString\",&,N,V_deviceSessionID"
+ "T@\"NSString\",&,N,V_flowID"
+ "T@\"NSString\",&,V_deviceSessionID"
+ "T@\"NSString\",&,V_flowID"
+ "TB,N,V_accountIsGuitarfish"
+ "Voucher creation failed"
+ "_accountIsGuitarfish"
+ "_allPCSItemPersistentRefs"
+ "accountIsGuitarfish"
+ "allPCSItemPersistentRefs"
+ "com.apple.security.establish"
+ "com.apple.security.establishOperation"
+ "com.apple.security.fetchAfterEstablish"
+ "com.apple.security.fetchRecoverableTLKShares"
+ "com.apple.security.handleRecoveryResults"
+ "com.apple.security.joinWithVoucherInTPH"
+ "com.apple.security.joinWithVoucherOperation"
+ "com.apple.security.onqueueEstablishTPH"
+ "com.apple.security.pairingFailedToFetchItemForPersistentRef"
+ "com.apple.security.performEscrowRecovery"
+ "com.apple.security.performSilentEscrowRecovery"
+ "com.apple.security.piggybackingAcceptorInitialMessage"
+ "com.apple.security.piggybackingAcceptorProcessApplication"
+ "com.apple.security.piggybackingAcceptorProcessMessage"
+ "com.apple.security.piggybackingCircleInitiatorHandleCircleBlobMessage"
+ "com.apple.security.piggybackingCircleInitiatorInitialMessage"
+ "com.apple.security.piggybackingSessionInitiatorHandleChallenge"
+ "com.apple.security.piggybackingSessionInitiatorHandleVerification"
+ "com.apple.security.piggybackingSessionInitiatorInitialMessage"
+ "com.apple.security.preflightVouchWithBottle"
+ "com.apple.security.recoverSilentWithCDPContext"
+ "com.apple.security.recoverWithCDPContext"
+ "com.apple.security.recoverWithInfo"
+ "com.apple.security.recoveryResultsResetAndEstablish"
+ "com.apple.security.restoreFromBottleEvent"
+ "com.apple.security.restoreKeychainAsyncWithPassword"
+ "com.apple.security.vouchWithBottle"
+ "com.apple.security.vouchWithBottleTPH"
+ "decode from der failed"
+ "decrypt and verify failed"
+ "errorData is nil"
+ "failed to copy response"
+ "failed to create initial message"
+ "failed to create peerinfo response"
+ "failed to create response message"
+ "failed to create version 1 message"
+ "failed to create version 2 message: %@"
+ "failed to create version initial message: %@"
+ "failed to encrypt initial message"
+ "failed to encrypt peer info"
+ "failed to fetch dsid"
+ "failed to fetch persistent ref %@, error: %@, continuing"
+ "failed to handle challenge data"
+ "failed to initial peerinfo message"
+ "fetchItemForPersistentRef: failed to fetch persistent ref: %@"
+ "fetchItemForPersistentRef: unexpected keychain item type fetched for persistent ref: %@, type: %lu"
+ "fetchItemForPersistentRef:error:"
+ "fetchPCSItemPersistentRefs:error:"
+ "i32@0:8r^^v16^@24"
+ "initWithCircleDelegate:session:altDSID:flowID:deviceSessionID:error:"
+ "initWithCircleDelegate:session:otcontrol:altDSID:flowID:deviceSessionID:error:"
+ "initWithSecretDelegate:circleDelegate:dsid:altDSID:flowID:deviceSessionID:rng:error:"
+ "initWithSecretDelegate:dsid:altDSID:flowID:deviceSessionID:error:"
+ "initWithSecretDelegate:dsid:altDSID:flowID:deviceSessionID:rng:error:"
+ "joining: Failed to copy response message: %@"
+ "joining: Verification failed: %@, error: %@"
+ "joining: decode from der failed: %@"
+ "joining: decrypt and verify failed: %@"
+ "joining: error preparing identity: %@"
+ "joining: error producing octagon voucher: %@"
+ "joining: expected acceptor epoch! returning nil. error: %@"
+ "joining: expected vertification message type: %@"
+ "joining: failed to create challenge message: %@"
+ "joining: failed to create encrypted peer info: %@"
+ "joining: failed to decrypt and verify circle blob message failed %@"
+ "joining: failed to encrypt initial message: %@"
+ "joining: failed to handle challenge data: %@"
+ "joining: failed to join octagon: %@"
+ "joining: failed to prepare identity: %@"
+ "joining: failed to process SOS circle: %@"
+ "joining: initial message creation failed: %@"
+ "joining: next secret is nil: %@"
+ "missingDigest"
+ "missingPassword"
+ "next secret is nil"
+ "octagon, failed to create pairing message from JoiningMessage: %@"
+ "processResponse: errorData is nil, error: %@"
+ "processResponse: failed to create error response message: %@"
+ "processResponse: successfully created response message"
+ "recordDataMissing"
+ "sessionWithCircleDelegate:session:altDSID:flowID:deviceSessionID:error:"
+ "sessionWithInitialMessage:secretDelegate:circleDelegate:dsid:altDSID:flowID:deviceSessionID:error:"
+ "sessionWithSecretDelegate:dsid:altDSID:flowID:deviceSessionID:error:"
+ "setAccountIsGuitarfish:"
+ "setAllPCSItemPersistentRefs:"
+ "successfully copied response message"
+ "successfully handled challenge data"
+ "totalNumberOfCustodians"
+ "totalNumberOfDistrustedRecoveryKeys"
+ "totalNumberOfPeers"
+ "totalNumberOfPreapprovals"
+ "totalNumberOfRecoveryKeys"
+ "totalNumberOfTrustedCustodians"
+ "totalNumberOfTrustedRecoveryKeys"
+ "unexpected keychain item type fetched for persistent ref"
- "\v"
- "\x12\x11\x11$"
- "\x12\x13"
- "\x121"
- "%s%s:%s%s%s%s%u:%s%u:%s aks connection failed%s\n"
- ":"
- "@48@0:8@16Q24^{ccrng_state=^?}32^@40"
- "@56@0:8@16@24Q32^{ccrng_state=^?}40^@48"
- "AppleKeyStore"
- "Failed to decrypt circleBlob"
- "IOService:/IOResources/AppleKeyStore"
- "T@\"NSArray\",&,N,V_allPCSItems"
- "Verification failed: %@"
- "_allPCSItems"
- "_create_bag"
- "aks"
- "aks-client-queue"
- "aks_assert_drop"
- "aks_assert_hold"
- "aks_save_bag"
- "aks_unload_bag"
- "allPCSItems"
- "com.apple.security.joinWithVoucher"
- "com.apple.security.trustedDeviceListRefresh"
- "error producing octagon voucher: %@"
- "failed to open connection to %s\n"
- "fetchPCSItems:"
- "i24@0:8r^^v16"
- "initWithCircleDelegate:session:error:"
- "initWithCircleDelegate:session:otcontrol:error:"
- "initWithSecretDelegate:circleDelegate:dsid:rng:error:"
- "initWithSecretDelegate:dsid:error:"
- "initWithSecretDelegate:dsid:rng:error:"
- "joining: circleBlob is nil"
- "joining: expected acceptor epoch! returning nil."
- "joining: failed to process SOS circle"
- "octagon, failed to create pairing message from JoiningMessage"
- "octagon: error preparing identity: %@"
- "request-session"
- "setAllPCSItems:"

```
