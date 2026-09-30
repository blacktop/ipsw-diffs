## IDS

> `/System/Library/PrivateFrameworks/IDS.framework/IDS`

```diff

-1926.300.181.0.0
-  __TEXT.__text: 0x1393b8
+1926.400.110.0.0
+  __TEXT.__text: 0x136798
   __TEXT.__auth_stubs: 0x1b60
-  __TEXT.__objc_methlist: 0xa984
+  __TEXT.__objc_methlist: 0xa5fc
   __TEXT.__const: 0x430
   __TEXT.__gcc_except_tab: 0x450c
-  __TEXT.__oslogstring: 0x187e2
-  __TEXT.__cstring: 0x10133
+  __TEXT.__oslogstring: 0x1871a
+  __TEXT.__cstring: 0x100f1
   __TEXT.__dlopen_cstrs: 0x102
   __TEXT.__ustring: 0xac
-  __TEXT.__unwind_info: 0x4ac0
-  __TEXT.__objc_classname: 0x18d0
-  __TEXT.__objc_methname: 0x1ee8d
-  __TEXT.__objc_methtype: 0x70e5
-  __TEXT.__objc_stubs: 0x13780
-  __DATA_CONST.__got: 0x1138
+  __TEXT.__unwind_info: 0x4a50
+  __TEXT.__objc_classname: 0x186a
+  __TEXT.__objc_methname: 0x1e50a
+  __TEXT.__objc_methtype: 0x70ab
+  __TEXT.__objc_stubs: 0x133a0
+  __DATA_CONST.__got: 0x1120
   __DATA_CONST.__const: 0x4df0
-  __DATA_CONST.__objc_classlist: 0x580
+  __DATA_CONST.__objc_classlist: 0x560
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x62e0
+  __DATA_CONST.__objc_selrefs: 0x6160
   __DATA_CONST.__objc_protorefs: 0xe8
-  __DATA_CONST.__objc_superrefs: 0x468
+  __DATA_CONST.__objc_superrefs: 0x448
   __AUTH_CONST.__auth_got: 0xdc0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x1780
-  __AUTH_CONST.__cfstring: 0x70c0
-  __AUTH_CONST.__objc_const: 0x3cfe8
+  __AUTH_CONST.__const: 0x1760
+  __AUTH_CONST.__cfstring: 0x7080
+  __AUTH_CONST.__objc_const: 0x3c828
   __AUTH_CONST.__objc_intobj: 0x4b0
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x1a90
-  __DATA.__objc_ivar: 0xd18
+  __AUTH.__objc_data: 0x19f0
+  __DATA.__objc_ivar: 0xcac
   __DATA.__data: 0x1710
-  __DATA.__bss: 0x1b1c
-  __DATA_DIRTY.__objc_data: 0x1c70
-  __DATA_DIRTY.__bss: 0x350
+  __DATA.__bss: 0x1b2c
+  __DATA_DIRTY.__objc_data: 0x1bd0
+  __DATA_DIRTY.__bss: 0x330
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Network.framework/Network

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 6227
-  Symbols:   1491
-  CStrings:  8912
+  Functions: 6147
+  Symbols:   1489
+  CStrings:  8803
 
Symbols:
+ OBJC_IVAR_$_IDSDaemonListener._accountToDevices
- _IDSDevicePropertyLocallyPresent
- _IDSDevicePropertySelfHandle
- _IDSDevicePropertySubServices
CStrings:
+ "\x0f\x04"
+ "_accountToDevices"
- "\x0f\x03!"
- "\x1b"
- "<%@ %p>"
- "<%@ %p>: Dictionary representation %@"
- "@\"_IDSRegisteredDevice\""
- "@\"_IDSRegistrationAccountManager\""
- "Adding new account %@ to tracked accounts list"
- "Adding new device to known devices array %@"
- "Creating new device registration %@"
- "Deleting unused device info %@"
- "Deleting unused registered device info %@"
- "RegistrationManager"
- "T@\"NSArray\",R,N,V_identities"
- "T@\"NSArray\",R,N,V_linkedUserURIs"
- "T@\"NSArray\",R,N,V_registeredDeviceInfo"
- "T@\"NSArray\",R,N,V_subServices"
- "T@\"NSData\",&,N,V_pushToken"
- "T@\"NSDictionary\",&,N,V_privateDeviceData"
- "T@\"NSDictionary\",R,N,V_clientData"
- "T@\"NSMutableArray\",&,N,V_knownDevices"
- "T@\"NSMutableArray\",&,N,V_knownRegistrations"
- "T@\"NSMutableDictionary\",&,N,V_accountIDToAccounts"
- "T@\"NSNumber\",&,N,V_maximumCompatibilityVersion"
- "T@\"NSNumber\",&,N,V_minimumCompatibilityVersion"
- "T@\"NSNumber\",&,N,V_pairingProtocolVersion"
- "T@\"NSNumber\",&,N,V_pairingType"
- "T@\"NSString\",&,N,V_deviceName"
- "T@\"NSString\",&,N,V_hardwareVersion"
- "T@\"NSString\",&,N,V_idsIdentifierOverride"
- "T@\"NSString\",&,N,V_nsuuid"
- "T@\"NSString\",&,N,V_selfHandle"
- "T@\"NSString\",R,N,V_accountID"
- "T@\"NSString\",R,N,V_service"
- "T@\"_IDSRegisteredDevice\",R,N,V_device"
- "T@\"_IDSRegistrationAccountManager\",&,N,V_registrationAccountManager"
- "TB,N,V_defaultLocalDevice"
- "TB,N,V_defaultPariedDevice"
- "TB,N,V_isActivePairedDevice"
- "TB,N,V_isHSATrustedDevice"
- "TB,N,V_locallyPresent"
- "_IDSRegisteredAccount"
- "_IDSRegisteredDevice"
- "_IDSRegisteredDeviceInfo"
- "_IDSRegistrationAccountManager"
- "_accountIDToAccounts"
- "_clientData"
- "_defaultLocalDevice"
- "_defaultPariedDevice"
- "_deleteUnusedRegistrationData"
- "_deviceName"
- "_findOrCreateDeviceForDictionary:"
- "_findOrCreateRegistrationInfoForDictionary:"
- "_hardwareVersion"
- "_identities"
- "_idsIdentifierOverride"
- "_isActivePairedDevice"
- "_isHSATrustedDevice"
- "_knownDevices"
- "_knownRegistrations"
- "_linkedUserURIs"
- "_locallyPresent"
- "_maximumCompatibilityVersion"
- "_minimumCompatibilityVersion"
- "_privateDeviceData"
- "_registeredDeviceInfo"
- "_registrationAccountManager"
- "accountID"
- "accountIDToAccounts"
- "accountIDToRegistrationMapping"
- "allAccountIDs"
- "clientData"
- "defaultLocalDevice"
- "defaultPariedDevice"
- "deviceName"
- "hardwareVersion"
- "idsIdentifierOverride"
- "initWithAccountID:service:registeredDeviceInfo:"
- "initWithDictionary:device:"
- "isActivePairedDevice"
- "isEqualToDictionary:"
- "isHSATrustedDevice"
- "knownDevices"
- "knownRegistrations"
- "maximumCompatibilityVersion"
- "minimumCompatibilityVersion"
- "privateDeviceData"
- "registeredDeviceInfo"
- "registeredDeviceInfoForAccountID:"
- "registrationAccountManager"
- "removeAllRecords"
- "setAccountIDToAccounts:"
- "setDefaultLocalDevice:"
- "setDefaultPariedDevice:"
- "setDeviceName:"
- "setHardwareVersion:"
- "setIdsIdentifierOverride:"
- "setIsActivePairedDevice:"
- "setIsHSATrustedDevice:"
- "setKnownDevices:"
- "setKnownRegistrations:"
- "setLocallyPresent:"
- "setMaximumCompatibilityVersion:"
- "setMinimumCompatibilityVersion:"
- "setNsuuid:"
- "setPairingProtocolVersion:"
- "setPrivateDeviceData:"
- "setPushToken:"
- "setRegistrationAccountManager:"
- "subServices"
- "updateAccount:withRegistration:"

```
