## identityservicesd

> `/System/Library/PrivateFrameworks/IDS.framework/identityservicesd.app/identityservicesd`

```diff

 1968.100.1.2.1
-  __TEXT.__text: 0x92359c
+  __TEXT.__text: 0x924ef4
   __TEXT.__auth_stubs: 0x5a50
-  __TEXT.__objc_stubs: 0x45e60
-  __TEXT.__objc_methlist: 0x291bc
+  __TEXT.__objc_stubs: 0x46020
+  __TEXT.__objc_methlist: 0x29274
   __TEXT.__const: 0x638d0
   __TEXT.__gcc_except_tab: 0x29c98
-  __TEXT.__objc_methname: 0x723f7
-  __TEXT.__cstring: 0x59047
-  __TEXT.__oslogstring: 0x7a08b
+  __TEXT.__objc_methname: 0x725e9
+  __TEXT.__cstring: 0x59127
+  __TEXT.__oslogstring: 0x7a3bb
   __TEXT.__objc_classname: 0x43a3
   __TEXT.__objc_methtype: 0x12303
   __TEXT.__ustring: 0x4ca

   __TEXT.__swift_as_ret: 0x6c
   __TEXT.__swift5_assocty: 0xfa8
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x121a8
+  __TEXT.__unwind_info: 0x121b8
   __TEXT.__eh_frame: 0x9934
   __DATA_CONST.__auth_got: 0x2d38
-  __DATA_CONST.__got: 0x3800
+  __DATA_CONST.__got: 0x3820
   __DATA_CONST.__auth_ptr: 0x770
-  __DATA_CONST.__const: 0x2dc48
-  __DATA_CONST.__cfstring: 0x34480
+  __DATA_CONST.__const: 0x2dc68
+  __DATA_CONST.__cfstring: 0x34560
   __DATA_CONST.__objc_classlist: 0x1110
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x750
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x108
   __DATA_CONST.__objc_superrefs: 0xb90
-  __DATA_CONST.__objc_intobj: 0x1a88
+  __DATA_CONST.__objc_intobj: 0x1aa0
   __DATA_CONST.__objc_arraydata: 0x5a0
   __DATA_CONST.__objc_arrayobj: 0x360
   __DATA_CONST.__objc_doubleobj: 0x10
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x47998
-  __DATA.__objc_selrefs: 0x15ae8
+  __DATA.__objc_const: 0x479c0
+  __DATA.__objc_selrefs: 0x15b68
   __DATA.__objc_ivar: 0x3278
   __DATA.__objc_data: 0xd260
   __DATA.__data: 0xea60

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 320C3603-B38E-3C50-A421-86C49EB6AE55
-  Functions: 25110
-  Symbols:   2732
-  CStrings:  41241
+  UUID: 16B16CEE-DA29-3091-ADA0-D88F0DCB3EDA
+  Functions: 25132
+  Symbols:   2736
+  CStrings:  41282
 
Symbols:
+ _IDSAccountSyncKeySPSCompanionDeviceUDID
+ _IDSAccountSyncKeySPSPrimaryPhoneNumbers
+ _IDSServiceNameiMessageLiteRelay
+ _OBJC_CLASS_$_IDSPhoneNumberFetchResult
CStrings:
+ "        DeviceID: %@, UDID: %@\n"
+ "21:57:25"
+ "<%@: %p { GUID: %@, deviceInfo: %@, phoneInfos: %@, sessionKeyCount: %ld, smsConfig: %@, companionPhoneNumbers: %@, companionDeviceUDIDs: %@, clear: %@ }>"
+ "Adding companion device tokens to message { companionDeviceUDIDs: %@, message: %@ }"
+ "Adding companion phone numbers to message { companionPhoneNumbers: %@, message: %@ }"
+ "Aug 12 2025"
+ "Client requested fetch phone numbers of type: %@"
+ "CompanionDeviceIDToUDID"
+ "CompanionPhoneNumbers"
+ "CompanionPushTokens"
+ "Handling traditional device unpair with deviceID: %@"
+ "Incoming sps provisioning info { phoneNumberURIs: %@ deviceID: %@ deviceUDID: %@ }"
+ "New paired device added, scheduling request { deviceUDID: %@ }"
+ "No valid fetch type provided."
+ "Note should sync sps provisioning info"
+ "Received account sync incoming SPS provisioning info while current device is not traditionally paired"
+ "Received incoming iMessage Lite: %@ with Metadata %@ senderShortHandle: %@ senderURI: %@ recipientShortHandle: %@ recipientURI: %@ isRelay: %@"
+ "SPSProvisioningData"
+ "Should continue syncing SPS provisioning info"
+ "Syncing SPS provisioning info {guid: %@ phoneNumbers: %@ deviceUDID: %@}"
+ "Told to handle companion device token sync { deviceID: %@ deviceUDID: %@ }"
+ "Told to handle companion device unpair { deviceID: %@ }"
+ "_updateSPSProvisioningInfo:fromID:"
+ "addCompanionDeviceUDIDsRequest:"
+ "addCompanionPhoneNumbersRequest:"
+ "fetchPhoneNumbersOfType:withCompletion:"
+ "handleCompanionDeviceSyncWithPhoneNumbers:deviceID:deviceUDID:"
+ "handleCompanionDeviceUnpairWithDeviceID:"
+ "initWithTelURI:fetchType:"
+ "isRelay"
+ "linkedDeviceUDIDs"
+ "noteShouldSynchronizeSPSProvisioningInfo"
+ "persistCompanionDeviceIDToUDID:"
+ "persistCompanionPhoneNumbers:"
+ "persistedCompanionDeviceIDToUDID"
+ "persistedCompanionPhoneNumbers"
+ "wantsCompanionDeviceUDIDs"
+ "wantsCompanionPhoneNumbers"
- "00:08:55"
- "<%@: %p { GUID: %@, deviceInfo: %@, phoneInfos: %@, sessionKeyCount: %ld, smsConfig: %@, clear: %@ }>"
- "Aug 28 2025"
- "Received incoming iMessage Lite: %@ with Metadata %@ senderShortHandle: %@ senderURI: %@ recipientShortHandle: %@ recipientURI: %@"

```
