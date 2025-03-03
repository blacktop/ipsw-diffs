## DigitalAccess

> `/System/Library/PrivateFrameworks/DigitalAccess.framework/DigitalAccess`

```diff

-53.2.0.0.0
-  __TEXT.__text: 0x1f524
-  __TEXT.__auth_stubs: 0x650
-  __TEXT.__objc_methlist: 0x13f4
+54.20.1.0.0
+  __TEXT.__text: 0x20cd0
+  __TEXT.__auth_stubs: 0x640
+  __TEXT.__objc_methlist: 0x1b84
   __TEXT.__const: 0x610
-  __TEXT.__cstring: 0x730e
+  __TEXT.__cstring: 0x7682
   __TEXT.__oslogstring: 0xb
-  __TEXT.__gcc_except_tab: 0xde0
-  __TEXT.__unwind_info: 0x9d0
-  __TEXT.__objc_classname: 0x445
-  __TEXT.__objc_methname: 0x489b
-  __TEXT.__objc_methtype: 0x16de
-  __TEXT.__objc_stubs: 0x23c0
-  __DATA_CONST.__got: 0x1d8
+  __TEXT.__gcc_except_tab: 0xe54
+  __TEXT.__unwind_info: 0xa30
+  __TEXT.__objc_classname: 0x48e
+  __TEXT.__objc_methname: 0x4c43
+  __TEXT.__objc_methtype: 0x1797
+  __TEXT.__objc_stubs: 0x2500
+  __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__const: 0xf30
-  __DATA_CONST.__objc_classlist: 0xe8
+  __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc20
+  __DATA_CONST.__objc_selrefs: 0xd78
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0xd0
+  __DATA_CONST.__objc_superrefs: 0xe0
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x338
+  __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x2300
-  __AUTH_CONST.__objc_const: 0x3ea8
+  __AUTH_CONST.__cfstring: 0x2520
+  __AUTH_CONST.__objc_const: 0x37d8
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0xd8
-  __DATA.__objc_ivar: 0x254
+  __AUTH.__objc_data: 0xa0
+  __DATA.__objc_ivar: 0x274
   __DATA.__data: 0x660
   __DATA.__bss: 0x72
   __DATA_DIRTY.__objc_data: 0x910

   - /usr/lib/libSESShared.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 635
-  Symbols:   836
-  CStrings:  1520
+  Functions: 717
+  Symbols:   926
+  CStrings:  1588
 
Symbols:
+ _OBJC_CLASS_$_DAKeySharing2FAConfiguration
+ _OBJC_CLASS_$_DASharingSecondFactorRequestConfiguration
+ _OBJC_METACLASS_$_DAKeySharing2FAConfiguration
+ _OBJC_METACLASS_$_DASharingSecondFactorRequestConfiguration
+ _SESEndPointIsSharingEnabled
+ _SESEndpointgetSupportedAliroVersions
- _SESEndpointGetSupportedLyonVersions
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x28
CStrings:
+ "\x01<"
+ "\x13"
+ "-[DAKeyManagementSession getSecondFactorRequestForConfigs:completionHandler:]"
+ "-[DAKeyManagementSession getSecondFactorRequestForConfigs:completionHandler:]_block_invoke"
+ "-[DAKeySharingSession acceptInvitationWithIdentifier:passcode:sharingFlow:completionHandler:]"
+ "-[DAKeySharingSession acceptInvitationWithIdentifier:passcode:sharingFlow:completionHandler:]_block_invoke"
+ "-[DAKeySharingSession getSecondFactorRequestForConfigs:completionHandler:]"
+ "-[DAKeySharingSession getSecondFactorRequestForConfigs:completionHandler:]_block_invoke"
+ "@44@0:8@16@24B32@36"
+ "DAKeySharing2FAConfiguration"
+ "DASharingSecondFactorRequestConfiguration"
+ "Invitation ID              : %@\n"
+ "Key ID                     : %@\n"
+ "MaxRetries        : %ld\n"
+ "No"
+ "Passcode Length   : %ld\n"
+ "Recipient Flow             : %@\n"
+ "Second factor config count : %ld\n"
+ "Sharing Flow          : %ld\n"
+ "T@\"NSArray\",R,N,V_secondFactorList"
+ "T@\"NSData\",&,N,V_metaData"
+ "T@\"NSString\",&,N,V_deviceEnteredPasscode"
+ "T@\"NSString\",&,N,V_displayName"
+ "T@\"NSString\",&,N,V_proprietaryEntitlements"
+ "T@\"NSString\",R,N,V_keyIdentifier"
+ "T@\"NSString\",R,N,V_passcode"
+ "TB,N,V_enableVehicleEnteredPasscode"
+ "TB,R,N,V_recipientFlow"
+ "TQ,N,V_maxRetriesForDeviceEnteredPasscode"
+ "TQ,N,V_profile"
+ "TQ,R,N,V_maxRetriesAllowed"
+ "This function is deprecated, please use acceptInvitationWithIdentifier:passcode:sharingFlow:completionHandler instead"
+ "Tq,N,V_sharingFlow"
+ "Tq,N,V_targetDeviceType"
+ "Type              : %ld\n"
+ "Vv32@0:8@\"NSArray\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "Vv72@0:8@\"DACarKeySharingMessage\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40q48@\"DAAlishaKeyEncryptedRequest\"56@?<v@?@\"DACarKeySharingMessage\"@\"DAKeyInformation\"@\"NSError\">64"
+ "Vv72@0:8@16@24@32@40q48@56@?64"
+ "Yes"
+ "_keyIdentifier"
+ "_maxRetriesAllowed"
+ "_passcode"
+ "_recipientFlow"
+ "_secondFactorList"
+ "_sharingFlow"
+ "_upgradeEnabledForFriendKey"
+ "_upgradeEnabledForOwnerKey"
+ "acceptInvitationWithIdentifier:passcode:sharingFlow:completionHandler:"
+ "acceptSharingInvitation:withIdentifier:fromMailboxIdentifier:passcode:sharingFlow:productPlanIdentifier:completionHandler:"
+ "decodeObjectOfClasses:forKey:"
+ "getSecondFactorRequestForConfigs:completionHandler:"
+ "initForDeviceVerifiedPasscode:maxRetries:"
+ "initForSecondFactorNone"
+ "initForServerVerifiedPasscode:"
+ "initForVehicleVerifiedPasscode"
+ "initWithArray:copyItems:"
+ "initWithInvitationIdentifier:keyIdentifier:recipientFlow:secondFactorList:"
+ "isSharingEnabledForManufacturer:brand:ppid:error:"
+ "keyIdentifier"
+ "maxRetriesAllowed"
+ "passcode"
+ "recipientFlow"
+ "secondFactorList"
+ "setDeviceEnteredPasscode:"
+ "setDisplayName:"
+ "setEnableVehicleEnteredPasscode:"
+ "setMaxRetriesForDeviceEnteredPasscode:"
+ "setMetaData:"
+ "setProfile:"
+ "setProprietaryEntitlements:"
+ "setSharingFlow:"
+ "setTargetDeviceType:"
+ "sharingFlow"
+ "v24@0:8q16"
+ "v32@0:8@\"NSArray\"16@?<v@?@\"NSArray\"@\"NSError\">24"
+ "v48@0:8@16@24q32@?40"
+ "vehicleSupportedBluetoothVersionsTlvAsData"
- "\x01="
- "-[DAKeySharingSession acceptInvitationWithIdentifier:passcode:completionHandler:]_block_invoke"
- "T@\"NSData\",R,N,V_metaData"
- "T@\"NSData\",R,N,V_vehicleSupportedBluetoothtVersionsTlvAsData"
- "T@\"NSString\",R,N,V_deviceEnteredPasscode"
- "T@\"NSString\",R,N,V_displayName"
- "T@\"NSString\",R,N,V_proprietaryEntitlements"
- "TB,R,N,V_enableVehicleEnteredPasscode"
- "TQ,R,N,V_maxRetriesForDeviceEnteredPasscode"
- "TQ,R,N,V_profile"
- "Vv64@0:8@\"DACarKeySharingMessage\"16@\"NSString\"24@\"NSString\"32@\"NSString\"40@\"DAAlishaKeyEncryptedRequest\"48@?<v@?@\"DACarKeySharingMessage\"@\"DAKeyInformation\"@\"NSError\">56"
- "_upgradeEnabled"
- "_vehicleSupportedBluetoothtVersionsTlvAsData"
- "acceptSharingInvitation:withIdentifier:fromMailboxIdentifier:passcode:productPlanIdentifier:completionHandler:"
- "vehicleSupportedBluetoothtVersionsTlvAsData"

```
