## DigitalAccess

> `/System/Library/PrivateFrameworks/DigitalAccess.framework/DigitalAccess`

```diff

-  __TEXT.__text: 0x39700
-  __TEXT.__objc_methlist: 0x2adc
+  __TEXT.__text: 0x3ab0c
+  __TEXT.__objc_methlist: 0x2c1c
   __TEXT.__const: 0x700
-  __TEXT.__cstring: 0x892d
-  __TEXT.__oslogstring: 0x2334
-  __TEXT.__gcc_except_tab: 0x11cc
-  __TEXT.__unwind_info: 0xdc8
+  __TEXT.__cstring: 0x8bc2
+  __TEXT.__oslogstring: 0x23fe
+  __TEXT.__gcc_except_tab: 0x1208
+  __TEXT.__unwind_info: 0xe18
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1180
-  __DATA_CONST.__objc_classlist: 0x138
+  __DATA_CONST.__const: 0x11a8
+  __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x90
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1598
+  __DATA_CONST.__objc_selrefs: 0x1618
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0x120
+  __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0xc0
-  __DATA_CONST.__got: 0x240
-  __AUTH_CONST.__const: 0x380
-  __AUTH_CONST.__cfstring: 0x2a60
-  __AUTH_CONST.__objc_const: 0x4b40
+  __DATA_CONST.__got: 0x250
+  __AUTH_CONST.__const: 0x3a0
+  __AUTH_CONST.__cfstring: 0x2c60
+  __AUTH_CONST.__objc_const: 0x4ef0
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_arrayobj: 0x120
   __AUTH_CONST.__auth_got: 0x0
-  __AUTH.__objc_data: 0x370
-  __DATA.__objc_ivar: 0x364
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x398
   __DATA.__data: 0x6c0
-  __DATA.__bss: 0x78
-  __DATA_DIRTY.__objc_data: 0x8c0
-  __DATA_DIRTY.__bss: 0x20
+  __DATA.__bss: 0x80
+  __DATA_DIRTY.__objc_data: 0xc30
+  __DATA_DIRTY.__bss: 0x28
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/SESShared.framework/SESShared

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1067
-  Symbols:   3488
-  CStrings:  1313
+  Functions: 1098
+  Symbols:   3595
+  CStrings:  1354
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA.__data : content changed
Symbols:
+ +[DAKeySharingInvitationParsedData supportsSecureCoding]
+ +[DAPairingTimestamp sharedInstance]
+ -[DAKeyPairingConfig initWithPassword:displayName:transport:bindingAttestation:brand:ppid:pendingPairingIdentifier:enableConnectionTimeout:additionalParameters:pairingStartTime:]
+ -[DAKeyPairingConfig pairingStartTime]
+ -[DAKeySharingInvitationParsedData .cxx_destruct]
+ -[DAKeySharingInvitationParsedData accessProfile]
+ -[DAKeySharingInvitationParsedData accountRole]
+ -[DAKeySharingInvitationParsedData description]
+ -[DAKeySharingInvitationParsedData encodeWithCoder:]
+ -[DAKeySharingInvitationParsedData friendlyName]
+ -[DAKeySharingInvitationParsedData initWithCoder:]
+ -[DAKeySharingInvitationParsedData initWithInvitationIdentifier:accessProfile:friendlyName:notBefore:notAfter:accountRole:secondFactorRequired:supportedTransports:sharingPasswordLength:]
+ -[DAKeySharingInvitationParsedData invitationIdentifier]
+ -[DAKeySharingInvitationParsedData notAfter]
+ -[DAKeySharingInvitationParsedData notBefore]
+ -[DAKeySharingInvitationParsedData secondFactorRequired]
+ -[DAKeySharingInvitationParsedData sharingPasswordLength]
+ -[DAKeySharingInvitationParsedData supportedTransports]
+ -[DAKeySharingSession parseSharingInvitation:completionHandler:]
+ -[DAPairingTimestamp .cxx_destruct]
+ -[DAPairingTimestamp init]
+ -[DAPairingTimestamp recordPreWarmStartForManufacturer:]
+ -[DAPairingTimestamp retrieveMostRecentPreWarmTimestamp]
+ GCC_except_table39
+ GCC_except_table45
+ GCC_except_table98
+ _OBJC_CLASS_$_DAKeySharingInvitationParsedData
+ _OBJC_CLASS_$_DAPairingTimestamp
+ _OBJC_IVAR_$_DAKeyPairingConfig._pairingStartTime
+ _OBJC_IVAR_$_DAKeySharingInvitationParsedData._accessProfile
+ _OBJC_IVAR_$_DAKeySharingInvitationParsedData._accountRole
+ _OBJC_IVAR_$_DAKeySharingInvitationParsedData._friendlyName
+ _OBJC_IVAR_$_DAKeySharingInvitationParsedData._invitationIdentifier
+ _OBJC_IVAR_$_DAKeySharingInvitationParsedData._notAfter
+ _OBJC_IVAR_$_DAKeySharingInvitationParsedData._notBefore
+ _OBJC_IVAR_$_DAKeySharingInvitationParsedData._secondFactorRequired
+ _OBJC_IVAR_$_DAKeySharingInvitationParsedData._sharingPasswordLength
+ _OBJC_IVAR_$_DAKeySharingInvitationParsedData._supportedTransports
+ _OBJC_IVAR_$_DAPairingTimestamp._expiryTime
+ _OBJC_IVAR_$_DAPairingTimestamp._lock
+ _OBJC_IVAR_$_DAPairingTimestamp._timestamp
+ _OBJC_METACLASS_$_DAKeySharingInvitationParsedData
+ _OBJC_METACLASS_$_DAPairingTimestamp
+ __OBJC_$_CLASS_METHODS_DAKeySharingInvitationParsedData
+ __OBJC_$_CLASS_METHODS_DAPairingTimestamp
+ __OBJC_$_CLASS_PROP_LIST_DAKeySharingInvitationParsedData
+ __OBJC_$_INSTANCE_METHODS_DAKeySharingInvitationParsedData
+ __OBJC_$_INSTANCE_METHODS_DAPairingTimestamp
+ __OBJC_$_INSTANCE_VARIABLES_DAKeySharingInvitationParsedData
+ __OBJC_$_INSTANCE_VARIABLES_DAPairingTimestamp
+ __OBJC_$_PROP_LIST_DAKeySharingInvitationParsedData
+ __OBJC_CLASS_PROTOCOLS_$_DAKeySharingInvitationParsedData
+ __OBJC_CLASS_RO_$_DAKeySharingInvitationParsedData
+ __OBJC_CLASS_RO_$_DAPairingTimestamp
+ __OBJC_METACLASS_RO_$_DAKeySharingInvitationParsedData
+ __OBJC_METACLASS_RO_$_DAPairingTimestamp
+ ___36+[DAPairingTimestamp sharedInstance]_block_invoke
+ ___64-[DAKeySharingSession parseSharingInvitation:completionHandler:]_block_invoke
+ ___block_descriptor_48_e8_32r40r_e54_v24?0"DAKeySharingInvitationParsedData"8"NSError"16lr32l8r40l8
+ _kmlUtcDateFormatter
+ _kmlUtilDateFromTimeData
+ _objc_msgSend$compare:
+ _objc_msgSend$dateByAddingTimeInterval:
+ _objc_msgSend$dateFromString:
+ _objc_msgSend$initWithPassword:displayName:transport:bindingAttestation:brand:ppid:pendingPairingIdentifier:enableConnectionTimeout:additionalParameters:pairingStartTime:
+ _objc_msgSend$parseSharingInvitation:completionHandler:
+ _objc_msgSend$recordPreWarmStartForManufacturer:
+ _objc_msgSend$retrieveMostRecentPreWarmTimestamp
+ _objc_msgSend$sharedInstance
+ _objc_msgSend$timeIntervalSinceDate:
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
+ _sharedInstance.instance
+ _sharedInstance.onceToken
- GCC_except_table20
- GCC_except_table32
- GCC_except_table44
- GCC_except_table51
- GCC_except_table54
CStrings:
+ "%s : %i : No timestamp stored"
+ "%s : %i : Recorded preWarm start for manufacturer: %{public}@ at %{public}@"
+ "%s : %i : Retrieved timestamp (age: %.2f seconds), cleared"
+ "%s : %i : Timestamp expired, cleared"
+ "-[DAKeySharingSession parseSharingInvitation:completionHandler:]"
+ "-[DAKeySharingSession parseSharingInvitation:completionHandler:]_block_invoke"
+ "-[DAPairingTimestamp recordPreWarmStartForManufacturer:]"
+ "-[DAPairingTimestamp retrieveMostRecentPreWarmTimestamp]"
+ "2nd Factor Required   : %@\n"
+ "Access Profile        : 0x%02x\n"
+ "Account Role          : 0x%04x\n"
+ "Friendly Name         : %@\n"
+ "Not After             : %@\n"
+ "Not Before            : %@\n"
+ "Sharing Pwd Length    : %u"
+ "Supported Transports  : %@\n"
+ "accessProfile"
+ "accountRole"
+ "friendlyName"
+ "notAfter"
+ "notBefore"
+ "pairingStartTime"
+ "secondFactorRequired"
+ "sharingPasswordLength"
+ "v24@?0@\"DAKeySharingInvitationParsedData\"8@\"NSError\"16"

```
