## imagent

> `/System/Library/PrivateFrameworks/IMCore.framework/imagent.app/imagent`

```diff

-1261.200.71.2.16
-  __TEXT.__text: 0x7f1c0
-  __TEXT.__auth_stubs: 0x1670
-  __TEXT.__objc_stubs: 0x74e0
-  __TEXT.__objc_methlist: 0x27f0
+1262.300.81.2.13
+  __TEXT.__text: 0x6bcdc
+  __TEXT.__auth_stubs: 0x1660
+  __TEXT.__objc_stubs: 0x7640
+  __TEXT.__objc_methlist: 0x2830
   __TEXT.__const: 0xdd4
-  __TEXT.__gcc_except_tab: 0x6b80
-  __TEXT.__cstring: 0x8021
-  __TEXT.__oslogstring: 0x6aa2
-  __TEXT.__objc_methname: 0xe732
-  __TEXT.__objc_classname: 0x8cb
-  __TEXT.__objc_methtype: 0x32f5
+  __TEXT.__gcc_except_tab: 0x6b04
+  __TEXT.__cstring: 0x2f41
+  __TEXT.__oslogstring: 0x6b48
+  __TEXT.__objc_methname: 0xe8f4
+  __TEXT.__objc_classname: 0x911
+  __TEXT.__objc_methtype: 0x337c
   __TEXT.__swift5_typeref: 0x2f3
   __TEXT.__swift5_fieldmd: 0x184
   __TEXT.__constg_swiftt: 0x364

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x60
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x275c
+  __TEXT.__unwind_info: 0x2758
   __TEXT.__eh_frame: 0x46c
-  __DATA_CONST.__auth_got: 0xb48
-  __DATA_CONST.__got: 0x4c8
+  __DATA_CONST.__auth_got: 0xb40
+  __DATA_CONST.__got: 0x590
   __DATA_CONST.__auth_ptr: 0x50
-  __DATA_CONST.__const: 0x1ab0
-  __DATA_CONST.__cfstring: 0x4e60
+  __DATA_CONST.__const: 0x19b0
+  __DATA_CONST.__cfstring: 0x17c0
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x1f0
+  __DATA_CONST.__objc_protolist: 0x200
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x38
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA_CONST.__objc_intobj: 0xd8
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x6b18
-  __DATA.__objc_selrefs: 0x2d98
+  __DATA.__objc_const: 0x6c48
+  __DATA.__objc_selrefs: 0x2e00
   __DATA.__objc_protorefs: 0xc0
-  __DATA.__objc_classrefs: 0x498
+  __DATA.__objc_classrefs: 0x4a0
   __DATA.__objc_superrefs: 0x20
   __DATA.__objc_ivar: 0xc0
   __DATA.__objc_data: 0x980
-  __DATA.__data: 0x1670
+  __DATA.__data: 0x1738
   __DATA.__bss: 0xd20
   __DATA.__common: 0xa8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A9786D5F-E1F9-3630-8FF9-A64AE29EF513
+  UUID: F6FA13AC-D3AD-3F05-AC3F-E8E49B5075DB
   Functions: 1375
-  Symbols:   575
-  CStrings:  4044
+  Symbols:   600
+  CStrings:  3233
 
Symbols:
+ _IMCloudKitTelemetrySyncVersion
+ _IMDMessageRecordCloudKitStatisticServerCountsKey
+ _IMFileTransferFilenameKey
+ _IMFileTransferGUIDKey
+ _IMGetDomainIntForKey
+ _IMServiceInfoAccountInfoKey
+ _IMServiceInfoAccountsKey
+ _IMServiceInfoActiveAccountsKey
+ _IMServiceInfoDefaultAccountSettingsKey
+ _IMServiceInfoDefaultsKey
+ _IMServiceInfoInternalNameKey
+ _IMServiceInfoPropertiesKey
+ _IMSetupInfoAliasToCNIDMapKey
+ _IMSetupInfoBlackholedChatsExistKey
+ _IMSetupInfoChatsKey
+ _IMSetupInfoDBModificationStampKey
+ _IMSetupInfoFileTransfersKey
+ _IMSetupInfoFileTransfersStampKey
+ _IMSetupInfoFilteredIMessageChatsExistKey
+ _IMSetupInfoGroupPhotoFileTransfersKey
+ _IMSetupInfoKeyTransparencyInfoKey
+ _IMSetupInfoLastFailedMessageDateKey
+ _IMSetupInfoPersistentPropertiesKey
+ _IMSetupInfoPersonMergedChatsKey
+ _IMSetupInfoPropertiesKey
+ _IMSetupInfoServiceNamesKey
+ _IMSetupInfoServicesKey
+ _IMSetupInfoUnreadMessageCountKey
+ _IMSetupInfoVCCapabilitiesKey
+ _OBJC_CLASS_$_IMDKeyTransparencyController
+ _OBJC_CLASS_$_IMDLegacyDTController
- _IMCloudKitRampStateFeatureAllowed
- _IMCloudKitRampStateFeatureVisible
- _IMCloudKitRampStateFetchSucceeded
- _MarcoLogMadridLevel
- _MarcoShouldLogMadridLevel
- _OBJC_CLASS_$_IMDLegactDTController
CStrings:
+ "%s: Tried to schedule telemetry sync but encountered error %@"
+ "-[IMDaemonCloudKitManager _registerForTelemetrySyncing]"
+ "20:09:18"
+ "20:09:22"
+ "@\"<IMDaemonListenerKeyTransparencyProtocol>\"16@0:8"
+ "@24@0:8B16B20"
+ "Adding unread message count (%ld) and lastFailedMessageDate (%ld) to setup info."
+ "Client does not want KT info"
+ "Fetched cloudkit ramp state featurePromoted(%@) fetchHadServerError(%@)"
+ "IMDaemonListenerKeyTransparencyProtocol"
+ "IMDaemonListenerSetupProtocol"
+ "Not adding unread message count or last failed message date to setup info due to missing capability."
+ "Nov 29 2023"
+ "Received sendRepositionStickerMessage request"
+ "T@\"<IMDaemonListenerKeyTransparencyProtocol>\",R,N"
+ "UnreadMessageCount"
+ "_addKeyTransparencyToSetupInfo:capabilities:context:"
+ "_hasFinishedTelemetrySync"
+ "_registerForTelemetrySyncing"
+ "broadcasterForKeyTransparencyListeners"
+ "clearLocalCountsWhenSafe"
+ "current cloudkit ramp state featurePromoted(%@) fetchHadServerError(%@)"
+ "currentStorageOnDevice"
+ "currentStorageOnDeviceWithReply:"
+ "currentTelemetryVersion"
+ "estimateQuotaAvailability:"
+ "keyTransparencyOptInStateChanged:"
+ "rampStateDictionaryFromPromoted:featureHadServerError:"
+ "refreshStatusForKTPeerURI:"
+ "scheduleTelemetrySyncWithDelegate:"
+ "sendRepositionStickerMessage:chatIdentifier:accountID:style:"
+ "simulateCloudKitSyncWithSyncState called with sync state %@"
+ "simulateCloudKitSyncWithSyncState:"
+ "v16@?0B8B12"
+ "v24@0:8@?<v@?Q>16"
+ "v44@0:8@\"IMMessageItem\"16@\"NSString\"24@\"NSString\"32C40"
+ "v44@0:8@16@24@32C40"
- "22:34:11"
- "22:34:14"
- "@36@0:8B16B20B24B28B32"
- "Cached Feature allowed. Calling completion block immediately"
- "DBModificationStamp"
- "Fetched cloudkit ramp state succeeded(%@) featureAllowed(%@) featurePromoted(%@) featureVisible(%@) fetchHadServerError(%@)"
- "IMDMessageRecordCloudKitStatisticServerCountsKey"
- "IMFileTransferFilenameKey"
- "IMFileTransferGUID"
- "Not ramped in. Requesting ramp state as user indicated intent"
- "Oct 11 2023"
- "_fetchRampStateIfNeededWithCompletion:"
- "accountInfo"
- "activeAccounts"
- "current cloudkit ramp state featureAllowed(%@) featurePromoted(%@) featureVisible(%@) fetchHadServerError(%@)"
- "fileTransfers-groupPhoto"
- "fileTransfers-stamp"
- "personMergedChats"
- "rampStateDictionaryFromState:featureAllowed:fetchPromoted:featureVisible:featureHadServerError:"
- "serviceNames"
- "services"
- "v24@?0B8B12B16B20"
- "v28@?0B8B12B16B20B24"

```
