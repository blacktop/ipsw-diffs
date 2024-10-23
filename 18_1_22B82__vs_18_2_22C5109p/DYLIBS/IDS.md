## IDS

> `/System/Library/PrivateFrameworks/IDS.framework/IDS`

```diff

-1925.200.81.2.1
-  __TEXT.__text: 0x1352e8
+1926.300.121.0.0
+  __TEXT.__text: 0x13909c
   __TEXT.__auth_stubs: 0x1b60
-  __TEXT.__objc_methlist: 0xa444
+  __TEXT.__objc_methlist: 0xa97c
   __TEXT.__const: 0x430
-  __TEXT.__gcc_except_tab: 0x452c
-  __TEXT.__oslogstring: 0x18569
-  __TEXT.__cstring: 0xff5b
+  __TEXT.__gcc_except_tab: 0x450c
+  __TEXT.__oslogstring: 0x18766
+  __TEXT.__cstring: 0x10091
   __TEXT.__dlopen_cstrs: 0x102
   __TEXT.__ustring: 0xac
-  __TEXT.__unwind_info: 0x4a28
-  __TEXT.__objc_classname: 0x17fe
-  __TEXT.__objc_methname: 0x1e1dc
-  __TEXT.__objc_methtype: 0x7013
-  __TEXT.__objc_stubs: 0x13200
-  __DATA_CONST.__got: 0x1108
-  __DATA_CONST.__const: 0x4dc0
-  __DATA_CONST.__objc_classlist: 0x540
+  __TEXT.__unwind_info: 0x4ad8
+  __TEXT.__objc_classname: 0x18d0
+  __TEXT.__objc_methname: 0x1ee71
+  __TEXT.__objc_methtype: 0x70e5
+  __TEXT.__objc_stubs: 0x13760
+  __DATA_CONST.__got: 0x1138
+  __DATA_CONST.__const: 0x4df0
+  __DATA_CONST.__objc_classlist: 0x580
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x1e0
+  __DATA_CONST.__objc_protolist: 0x1e8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x60b0
-  __DATA_CONST.__objc_protorefs: 0xe0
-  __DATA_CONST.__objc_superrefs: 0x438
+  __DATA_CONST.__objc_selrefs: 0x62d8
+  __DATA_CONST.__objc_protorefs: 0xe8
+  __DATA_CONST.__objc_superrefs: 0x468
   __AUTH_CONST.__auth_got: 0xdc0
   __AUTH_CONST.__auth_ptr: 0x8
-  __AUTH_CONST.__const: 0x1720
-  __AUTH_CONST.__cfstring: 0x6ec0
-  __AUTH_CONST.__objc_const: 0x3bf30
+  __AUTH_CONST.__const: 0x1780
+  __AUTH_CONST.__cfstring: 0x7040
+  __AUTH_CONST.__objc_const: 0x3cfe8
   __AUTH_CONST.__objc_intobj: 0x4b0
   __AUTH_CONST.__objc_doubleobj: 0x20
-  __AUTH.__objc_data: 0x19a0
-  __DATA.__objc_ivar: 0xc88
-  __DATA.__data: 0x16b0
-  __DATA.__bss: 0x1b1c
+  __AUTH.__objc_data: 0x1c20
+  __DATA.__objc_ivar: 0xd18
+  __DATA.__data: 0x1710
+  __DATA.__bss: 0x1b3c
   __DATA_DIRTY.__objc_data: 0x1ae0
   __DATA_DIRTY.__bss: 0x330
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libnetwork.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 6104
-  Symbols:   1480
-  CStrings:  8734
+  Functions: 6223
+  Symbols:   1491
+  CStrings:  8904
 
Symbols:
+ _IDSDevicePropertyLocallyPresent
+ _IDSDevicePropertySelfHandle
+ _IDSDevicePropertySubServices
+ _IDSEventReportingManagerErrorDomain
+ _OBJC_CLASS_$_IDSEventReportingManager
+ _OBJC_CLASS_$_IDSKTState
+ _OBJC_CLASS_$_IDSReportClientEvent
+ _OBJC_CLASS_$_IDSXPCEventReportingInterface
+ _OBJC_METACLASS_$_IDSEventReportingManager
+ _OBJC_METACLASS_$_IDSKTState
+ _OBJC_METACLASS_$_IDSReportClientEvent
+ _OBJC_METACLASS_$_IDSXPCEventReportingInterface
- OBJC_IVAR_$_IDSDaemonListener._accountToDevices
CStrings:
+ "\x0f\x03!"
+ "\x1b"
+ "%!x(MISSING)"
+ "%!s(MISSING) called with invalid event -- returning"
+ "-[IDSEventReportingManager reportClientEvent:withCompletion:]"
+ "<%!@(MISSING) %!p(MISSING)>"
+ "<%!@(MISSING) %!p(MISSING)>: Dictionary representation %!@(MISSING)"
+ "@\"_IDSRegisteredDevice\""
+ "@\"_IDSRegistrationAccountManager\""
+ "@24@0:8^{?=*QqqICBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@iISQB[0C]}16"
+ "@44@0:8@16i24B28B32Q36"
+ "Adding new account %!@(MISSING) to tracked accounts list"
+ "Adding new device to known devices array %!@(MISSING)"
+ "Creating new device registration %!@(MISSING)"
+ "DatagramChannelHBHSecretLogging"
+ "Deleting unused device info %!@(MISSING)"
+ "Deleting unused registered device info %!@(MISSING)"
+ "Error fetching event reporting collaborator {error: %!@(MISSING)}"
+ "Full hbhDecryptionkey: %!@(MISSING)"
+ "Full hbhEncryptionkey: %!@(MISSING)"
+ "IDSEventReportingManager"
+ "IDSEventReportingManagerErrorDomain"
+ "IDSKTState"
+ "IDSReportClientEvent"
+ "IDSXPCEventReporting"
+ "IDSXPCEventReportingInterface"
+ "RegistrationManager"
+ "Reporting event of type %!@(MISSING) to server with completion"
+ "T@\"NSArray\",R,N,V_identities"
+ "T@\"NSArray\",R,N,V_linkedUserURIs"
+ "T@\"NSArray\",R,N,V_registeredDeviceInfo"
+ "T@\"NSArray\",R,N,V_subServices"
+ "T@\"NSData\",&,N,V_pushToken"
+ "T@\"NSDictionary\",&,N,V_privateDeviceData"
+ "T@\"NSDictionary\",&,N,V_report"
+ "T@\"NSDictionary\",R,N,V_clientData"
+ "T@\"NSMutableArray\",&,N,V_knownDevices"
+ "T@\"NSMutableArray\",&,N,V_knownRegistrations"
+ "T@\"NSMutableDictionary\",&,N,V_accountIDToAccounts"
+ "T@\"NSNumber\",&,N,V_maximumCompatibilityVersion"
+ "T@\"NSNumber\",&,N,V_minimumCompatibilityVersion"
+ "T@\"NSNumber\",&,N,V_pairingProtocolVersion"
+ "T@\"NSNumber\",&,N,V_pairingType"
+ "T@\"NSString\",&,N,V_deviceName"
+ "T@\"NSString\",&,N,V_hardwareVersion"
+ "T@\"NSString\",&,N,V_idsIdentifierOverride"
+ "T@\"NSString\",&,N,V_nsuuid"
+ "T@\"NSString\",&,N,V_reportType"
+ "T@\"NSString\",&,N,V_selfHandle"
+ "T@\"NSString\",&,V_userID"
+ "T@\"NSString\",R,N,V_accountID"
+ "T@\"NSString\",R,N,V_service"
+ "T@\"_IDSRegisteredDevice\",R,N,V_device"
+ "T@\"_IDSRegistrationAccountManager\",&,N,V_registrationAccountManager"
+ "TB,N,V_defaultLocalDevice"
+ "TB,N,V_defaultPariedDevice"
+ "TB,N,V_isActivePairedDevice"
+ "TB,N,V_isHSATrustedDevice"
+ "TB,N,V_locallyPresent"
+ "TB,V_containsAccountKey"
+ "TB,V_containsDeviceSignature"
+ "TQ,V_optedIn"
+ "Ti,V_status"
+ "Transparency requested our current KT registration state."
+ "^{?=*QqqICBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@iISQB[0C]}20@0:8B16"
+ "^{?=*QqqICBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@iISQB[0C]}54@0:8r^v16I24C28C32{?=cSCSC}36^{?=IQSCc[12S]CS{?=SSSSS}dQBQ[16C]BB}46"
+ "^{?=*QqqICBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@iISQB[0C]}62@0:8r^v16I24C28C32{?=cSCSC}36^{?=IQSCc[12S]CS{?=SSSSS}dQBQ[16C]BB}46@54"
+ "_IDSRegisteredAccount"
+ "_IDSRegisteredDevice"
+ "_IDSRegisteredDeviceInfo"
+ "_IDSRegistrationAccountManager"
+ "_accountIDToAccounts"
+ "_clientData"
+ "_containsAccountKey"
+ "_containsDeviceSignature"
+ "_defaultLocalDevice"
+ "_defaultPariedDevice"
+ "_deleteUnusedRegistrationData"
+ "_deviceName"
+ "_findOrCreateDeviceForDictionary:"
+ "_findOrCreateRegistrationInfoForDictionary:"
+ "_hardwareVersion"
+ "_hasSentCompoundPacket"
+ "_identities"
+ "_idsIdentifierOverride"
+ "_isActivePairedDevice"
+ "_isHSATrustedDevice"
+ "_knownDevices"
+ "_knownRegistrations"
+ "_linkedUserURIs"
+ "_locallyPresent"
+ "_maximumCompatibilityVersion"
+ "_minimumCompatibilityVersion"
+ "_optedIn"
+ "_privateDeviceData"
+ "_registeredDeviceInfo"
+ "_registrationAccountManager"
+ "_report"
+ "_reportType"
+ "_userID"
+ "accountID"
+ "accountIDToAccounts"
+ "accountIDToRegistrationMapping"
+ "accountKey"
+ "allAccountIDs"
+ "clientData"
+ "connectedDevicesChanged on connection %!@(MISSING) account %!@(MISSING) devices %!@(MISSING) num devices %!{(MISSING)public}lu"
+ "containsAccountKey"
+ "containsDeviceSignature"
+ "decodeInt32ForKey:"
+ "defaultLocalDevice"
+ "defaultPariedDevice"
+ "deviceName"
+ "deviceSignature"
+ "devicesChanged on connection %!@(MISSING) account %!@(MISSING) all devices %!@(MISSING) num devices %!{(MISSING)public}lu num delegates: %!l(MISSING)u"
+ "encodeInt32:forKey:"
+ "eventReporting"
+ "eventReportingCollaboratorWithCompletion:"
+ "eventReportingCollaboratorWithErrorHandler:"
+ "getCurrentRegistrationStateWithCompletion:"
+ "hardwareVersion"
+ "idsIdentifierOverride"
+ "initWithAccountID:service:registeredDeviceInfo:"
+ "initWithDictionary:device:"
+ "initWithReport:reportType:timeout:"
+ "initWithUserID:registrationStatus:containsAccountKey:containsDeviceSignature:optedIn:"
+ "isActivePairedDevice"
+ "isEqualToDictionary:"
+ "isHSATrustedDevice"
+ "knownDevices"
+ "knownRegistrations"
+ "maximumCompatibilityVersion"
+ "minimumCompatibilityVersion"
+ "optedIn"
+ "privateDeviceData"
+ "registeredDeviceInfo"
+ "registeredDeviceInfoForAccountID:"
+ "registrationAccountManager"
+ "removeAllRecords"
+ "report"
+ "report-type"
+ "reportClientEvent:withCompletion:"
+ "reportType"
+ "setAccountIDToAccounts:"
+ "setContainsAccountKey:"
+ "setContainsDeviceSignature:"
+ "setDefaultLocalDevice:"
+ "setDefaultPariedDevice:"
+ "setDeviceName:"
+ "setHardwareVersion:"
+ "setIdsIdentifierOverride:"
+ "setIsActivePairedDevice:"
+ "setIsHSATrustedDevice:"
+ "setKnownDevices:"
+ "setKnownRegistrations:"
+ "setLocallyPresent:"
+ "setMaximumCompatibilityVersion:"
+ "setMinimumCompatibilityVersion:"
+ "setNsuuid:"
+ "setOptedIn:"
+ "setPairingProtocolVersion:"
+ "setPrivateDeviceData:"
+ "setPushToken:"
+ "setRegistrationAccountManager:"
+ "setReport:"
+ "setReportType:"
+ "setUserID:"
+ "stringWithCapacity:"
+ "subServices"
+ "updateAccount:withRegistration:"
+ "userID"
+ "v16@?0@\"<IDSXPCEventReporting>\"8"
+ "v24@0:8@?<v@?@\"<IDSXPCEventReporting>\"@\"NSError\">16"
+ "v24@0:8^{?=*QqqICBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@iISQB[0C]}16"
+ "v32@0:8@\"IDSReportClientEvent\"16@?<v@?@\"NSDictionary\"@\"NSError\">24"
- "\x0f\x04"
- "@24@0:8^{?=*QqqICBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@iIS[0C]}16"
- "^{?=*QqqICBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@iIS[0C]}20@0:8B16"
- "^{?=*QqqICBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@iIS[0C]}54@0:8r^v16I24C28C32{?=cSCSC}36^{?=IQSCc[12S]CS{?=SSSSS}dQBQ[16C]BB}46"
- "^{?=*QqqICBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@iIS[0C]}62@0:8r^v16I24C28C32{?=cSCSC}36^{?=IQSCc[12S]CS{?=SSSSS}dQBQ[16C]BB}46@54"
- "_accountToDevices"
- "connectedDevicesChanged on connection %!@(MISSING) account %!@(MISSING) devices %!@(MISSING)"
- "devicesChanged on connection %!@(MISSING) account %!@(MISSING) all devices %!@(MISSING) num delegates: %!l(MISSING)u"
- "v24@0:8^{?=*QqqICBBBBBBBBBBBI{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}{sockaddr_storage=CC[6c]q[112c]}SCi[8{?=*Si[12S]QCSCBBS{?=SSSSS}BBi[4S]CBBBI}]ccid[16C]QQ@iIS[0C]}16"

```
