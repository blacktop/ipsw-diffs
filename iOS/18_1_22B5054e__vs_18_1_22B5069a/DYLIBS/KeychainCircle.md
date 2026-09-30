## KeychainCircle

> `/System/Library/PrivateFrameworks/KeychainCircle.framework/KeychainCircle`

```diff

-61439.40.54.0.0
-  __TEXT.__text: 0x208d8
-  __TEXT.__auth_stubs: 0xeb0
-  __TEXT.__objc_methlist: 0x16ec
-  __TEXT.__const: 0xc4
-  __TEXT.__gcc_except_tab: 0xf70
-  __TEXT.__cstring: 0x1ff2
-  __TEXT.__oslogstring: 0x2e6c
+61439.42.1.0.1
+  __TEXT.__text: 0x269ec
+  __TEXT.__auth_stubs: 0x1010
+  __TEXT.__objc_methlist: 0x18e4
+  __TEXT.__const: 0xd0
+  __TEXT.__cstring: 0x22df
+  __TEXT.__gcc_except_tab: 0x12ec
+  __TEXT.__oslogstring: 0x3398
+  __TEXT.__dlopen_cstrs: 0x200
   __TEXT.__ustring: 0x32
-  __TEXT.__dlopen_cstrs: 0x152
-  __TEXT.__unwind_info: 0x760
-  __TEXT.__objc_classname: 0x2e3
-  __TEXT.__objc_methname: 0x36e9
-  __TEXT.__objc_methtype: 0xe51
-  __TEXT.__objc_stubs: 0x28c0
-  __DATA_CONST.__got: 0x200
-  __DATA_CONST.__const: 0xf30
+  __TEXT.__unwind_info: 0x858
+  __TEXT.__objc_classname: 0x2e4
+  __TEXT.__objc_methname: 0x3dcb
+  __TEXT.__objc_methtype: 0xec7
+  __TEXT.__objc_stubs: 0x2e20
+  __DATA_CONST.__got: 0x2d0
+  __DATA_CONST.__const: 0x1050
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcb8
+  __DATA_CONST.__objc_selrefs: 0xe60
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x88
-  __AUTH_CONST.__auth_got: 0x768
-  __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x1a0
-  __AUTH_CONST.__cfstring: 0x2500
-  __AUTH_CONST.__objc_const: 0x2cc8
-  __AUTH_CONST.__objc_intobj: 0x30
+  __AUTH_CONST.__auth_got: 0x818
+  __AUTH_CONST.__auth_ptr: 0x10
+  __AUTH_CONST.__const: 0x1e0
+  __AUTH_CONST.__cfstring: 0x27a0
+  __AUTH_CONST.__objc_const: 0x2ea8
+  __AUTH_CONST.__objc_intobj: 0x60
   __AUTH.__objc_data: 0x640
-  __DATA.__objc_ivar: 0x1a4
+  __DATA.__objc_ivar: 0x1cc
   __DATA.__data: 0x318
-  __DATA.__bss: 0x188
+  __DATA.__bss: 0x1d0
   __DATA_DIRTY.__objc_data: 0x50
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 676
-  Symbols:   1156
-  CStrings:  1362
+  Functions: 761
+  Symbols:   1297
+  CStrings:  1515
 
Symbols:
+ _CFArrayGetTypeID
+ _CFDictionaryContainsKey
+ _CFErrorCopyUserInfo
+ _CFErrorCreate
+ _CFErrorGetCode
+ _CFErrorGetDomain
+ _CFNumberGetValue
+ _GetKeybagAssertionQueue
+ _IOConnectCallMethod
+ _IOServiceClose
+ _IOServiceGetMatchingService
+ _IOServiceMatching
+ _IOServiceOpen
+ _OBJC_CLASS_$_NSMutableArray
+ _PairingPacketKey_EndOfSession
+ _PairingPacketKey_PCSData
+ _PairingPacketKey_PCSDataAck
+ _PairingPacketKey_PCSDataFromAcceptor
+ _PairingPacketKey_PCSDataKeyPrefix
+ _PairingPacketKey_PCSDataPacketNumber
+ _PairingPacketKey_PCSDataRequest
+ _SecAKSCopyBackupBagWithSecret
+ _SecAKSDoWithKeybagLockAssertion
+ _SecAKSDoWithKeybagLockAssertionSoftly
+ _SecAKSKeybagDropLockAssertion
+ _SecAKSKeybagHoldLockAssertion
+ _SecAKSSanitizedKeyclass
+ _SecAllocationError
+ _SecCFCreateErrorWithFormat
+ _SecCFCreateErrorWithFormatAndArguments
+ _SecCheckErrno
+ _SecError
+ _SecItemAdd
+ _SecItemCopyMatching
+ _SecItemUpdate
+ _SecKernError
+ _SecRequirementError
+ ___error
+ ___kCFBooleanFalse
+ ___stdoutp
+ _calloc
+ _fprintf
+ _kCFErrorDescriptionKey
+ _kCFErrorDomainMach
+ _kCFErrorDomainOSStatus
+ _kCFErrorDomainPOSIX
+ _kCFErrorUnderlyingErrorKey
+ _kIOMasterPortDefault
+ _kSOSCountKey
+ _kSecAttrAccessControl
+ _kSecAttrAccessGroup
+ _kSecAttrAccount
+ _kSecAttrPath
+ _kSecAttrServer
+ _kSecAttrSyncViewHint
+ _kSecAttrSynchronizable
+ _kSecClass
+ _kSecClassInternetPassword
+ _kSecMatchLimit
+ _kSecMatchLimitAll
+ _kSecReturnAttributes
+ _kSecReturnData
+ _kSecUseDataProtectionKeychain
+ _kSecValueData
+ _kUserKeybagStateChangeNotification
+ _lockAssertType
+ _mach_task_self_
+ _memcpy
+ _objc_retain_x5
+ _strerror
CStrings:
+ "%!@(MISSING)+%!l(MISSING)d"
+ "%!@(MISSING)-%!d(MISSING)"
+ "%!@(MISSING): [%!d(MISSING)] %!s(MISSING)"
+ "%!s(MISSING)%!s(MISSING):%!s(MISSING)%!s(MISSING)%!s(MISSING)%!s(MISSING)%!u(MISSING):%!s(MISSING)%!u(MISSING):%!s(MISSING) aks connection failed%!s(MISSING)\n"
+ "123456"
+ "4\x1a"
+ ":"
+ "@\"NSArray\""
+ "@\"NSNumber\""
+ "@24@0:8^v16"
+ "@36@0:8@16@24B32"
+ "@40@0:8@16Q24Q32"
+ "ACAccountStore"
+ "AKS Lock Assertion Queue"
+ "AppleKeyStore"
+ "B20@0:8i16"
+ "B56@0:8@16@24@32@40^@48"
+ "Bag CFData Allocation Failed"
+ "Did not receive expected ack number, re-attempting PCS key transfer"
+ "Dropping lock assertion"
+ "IOService:/IOResources/AppleKeyStore"
+ "Invalid size: %!z(MISSING)u"
+ "Kern return error"
+ "Received ack number: %!@(MISSING)"
+ "Requesting lock assertion for %!l(MISSING)ld seconds"
+ "SanitizeKeyclass"
+ "SecAKSDoWithKeybagLockAssertionSoftly: failed to get assertion for %!d(MISSING) proceeding bravely: %!@(MISSING)"
+ "SecItemAdd: failed to add PCS item to the keychain"
+ "SecItemCopyMatching: failed to fetch pcs data from the keychain"
+ "SecItemUpdate: failed to update PCS item in the keychain"
+ "SecureBackupIsGuitarfishEnabled"
+ "Sending ack %!@(MISSING)"
+ "T@\"NSArray\",&,N,V_allPCSItems"
+ "T@\"NSNumber\",&,N,V_ackNumber"
+ "T@\"NSNumber\",&,N,V_countOfReceivedItems"
+ "T@\"NSNumber\",&,N,V_countOfSentItems"
+ "T@\"NSNumber\",&,N,V_sizeOfPacket"
+ "T@\"NSString\",&,N,V_dsidForTest"
+ "TB,N,V_grabbedLockAssertion"
+ "TB,V_acceptorWillSendPCSData"
+ "TB,V_initiatorExpectPCSData"
+ "TQ,N,V_itemIndex"
+ "_acceptorWillSendPCSData"
+ "_ackNumber"
+ "_allPCSItems"
+ "_countOfReceivedItems"
+ "_countOfSentItems"
+ "_create_bag"
+ "_dsidForTest"
+ "_grabbedLockAssertion"
+ "_initiatorExpectPCSData"
+ "_itemIndex"
+ "_sizeOfPacket"
+ "a"
+ "aa_personID"
+ "aa_primaryAppleAccount"
+ "acceptor packet will include pcs data"
+ "acceptor received ACK from initiator"
+ "acceptor will send PCS data"
+ "acceptor will send initiator (%!l(MISSING)u) items: %!@(MISSING)"
+ "acceptorPCSDataPacket: received unexpected return type from SecItemCopyMatching, typeID: %!l(MISSING)u"
+ "acceptorPCSDataPacket:complete:"
+ "acceptorWaitForAck:complete:"
+ "acceptorWillSendPCSData"
+ "ackNumber"
+ "adding keychain entry data %!@(MISSING)"
+ "adding keychain entry key: %!@(MISSING)"
+ "aks"
+ "aks-client-queue"
+ "aks_assert_drop"
+ "aks_assert_hold"
+ "aks_save_bag"
+ "aks_unload_bag"
+ "allPCSItems"
+ "array"
+ "bag allocation failed: %!d(MISSING)"
+ "com.apple.ProtectedCloudStorage"
+ "com.apple.mobile.keybagd.lock_status"
+ "copySubsetFrom:begin:end:"
+ "countOfReceivedItems"
+ "countOfSentItems"
+ "createPacket:results:endSession:"
+ "createTempPacket:pcsItem:octagonData:keyForItem:"
+ "createTempPacketAndCheckSize:pcsItem:octagonData:keyForItem:error:"
+ "defaultStore"
+ "dsidForTest"
+ "e"
+ "evaluateResults:"
+ "failed to open connection to %!s(MISSING)\n"
+ "fetchAcceptorWillSendPCSData"
+ "fetchCountOfReceivedItemsForTesting"
+ "fetchCountOfSentItemsForTesting"
+ "fetchNumberOfPCSKeychainItems"
+ "fetchPCSItems:"
+ "fetchSizeOfPacketForTesting"
+ "formNextPacket"
+ "grabbedLockAssertion"
+ "i24@0:8r^^v16"
+ "initWithLength:"
+ "initiator will import PCS data"
+ "initiator will wait for PCS data"
+ "initiatorExpectPCSData"
+ "initiatorPCSDataPacket:complete:"
+ "intValue"
+ "integerValue"
+ "isEqualToNumber:"
+ "isPacketSizeAcceptable:error:"
+ "item by itself is too large for the pairing channel: %!@(MISSING)"
+ "itemIndex"
+ "k"
+ "lockassertions"
+ "n"
+ "numberWithInt:"
+ "objectAtIndexedSubscript:"
+ "pairing, SecItemUpdate failed %!d(MISSING)"
+ "pairing: Failed to drop AKS lock assertion: %!@(MISSING)"
+ "pairing: Unable to acquire AKS lock assertion: %!@(MISSING)"
+ "pairing: failed to add PCS item: %!d(MISSING)"
+ "pairing: failed to compress packet. will not add anymore items, error: %!@(MISSING)"
+ "pairing: failed to serialize temp packet: %!@(MISSING)"
+ "pairing: fetched no results, ending session"
+ "pairing: no octagon data, ending session"
+ "pairing: temp packet size is too large for the channel. will not add anymore items"
+ "pcsdata"
+ "populateKeychainForTestingWithNumberOfKeychainItems:"
+ "populateKeychainWithLargeItemsForTestingWithCount:"
+ "populateKeychainWithMixedLargeItemsForTestingWithCount:"
+ "populateKeychainWithTooLargeItemsForTestingWithCount:"
+ "s"
+ "sanitizing request for keyclass %!d(MISSING) to keyclass %!d(MISSING)"
+ "save bag failed: %!d(MISSING)"
+ "secaks"
+ "setAcceptorWillSendPCSData:"
+ "setAckNumber:"
+ "setAllPCSItems:"
+ "setCountOfReceivedItems:"
+ "setCountOfSentItems:"
+ "setDSIDForTest:"
+ "setDsidForTest:"
+ "setGrabbedLockAssertion:"
+ "setInitiatorExpectPCSData:"
+ "setItemIndex:"
+ "setObject:atIndexedSubscript:"
+ "setSizeOfPacket:"
+ "sizeOfPacket"
+ "softlink:o:path:/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount"
+ "softlink:o:path:/System/Library/PrivateFrameworks/CloudServices.framework/CloudServices"
+ "successfully added pcs item: %!@(MISSING)"
+ "successfully updated pcs item: %!@(MISSING)"
+ "unload bag failed: %!d(MISSING)"
+ "updateItem:"
+ "will attempt to add more items to the packet"
+ "y"
+ "zesty"
- "("

```
