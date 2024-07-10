## UARPUpdaterServiceDFU

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceDFU.xpc/Contents/MacOS/UARPUpdaterServiceDFU`

```diff

-1163.0.0.0.0
-  __TEXT.__text: 0x17948
-  __TEXT.__auth_stubs: 0x4e0
-  __TEXT.__objc_stubs: 0x15c0
+1155.0.0.0.0
+  __TEXT.__text: 0x19ce0
+  __TEXT.__auth_stubs: 0x550
+  __TEXT.__objc_stubs: 0x1980
   __TEXT.__objc_methlist: 0x70c
   __TEXT.__const: 0xa0
-  __TEXT.__cstring: 0x1eba
-  __TEXT.__objc_methname: 0x2344
-  __TEXT.__oslogstring: 0xd8c
+  __TEXT.__cstring: 0x1fc9
+  __TEXT.__objc_methname: 0x2664
+  __TEXT.__oslogstring: 0xf67
   __TEXT.__objc_classname: 0x112
   __TEXT.__objc_methtype: 0x2f22
-  __TEXT.__unwind_info: 0x548
-  __DATA_CONST.__auth_got: 0x278
-  __DATA_CONST.__got: 0xf0
+  __TEXT.__unwind_info: 0x5d0
+  __DATA_CONST.__auth_got: 0x2b0
+  __DATA_CONST.__got: 0x130
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x468
-  __DATA_CONST.__cfstring: 0x320
+  __DATA_CONST.__const: 0x4a8
+  __DATA_CONST.__cfstring: 0x480
   __DATA_CONST.__objc_classlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__objc_intobj: 0x108
+  __DATA_CONST.__objc_intobj: 0x120
   __DATA_CONST.__objc_arraydata: 0x20
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x20d8
-  __DATA.__objc_selrefs: 0x698
+  __DATA.__objc_selrefs: 0x788
   __DATA.__objc_ivar: 0xd8
   __DATA.__objc_data: 0x1e0
-  __DATA.__data: 0x251
-  __DATA.__bss: 0x1168
+  __DATA.__data: 0x291
+  __DATA.__bss: 0x11b0
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 628
-  Symbols:   449
-  CStrings:  255
+  Functions: 721
+  Symbols:   545
+  CStrings:  269
 
Symbols:
+ _IOPMAssertionCreateWithName
+ _IOPMAssertionRelease
+ _InternalStorageDirectoryPath
+ _NSFilePosixPermissions
+ _OBJC_CLASS_$_NSDictionary
+ _OBJC_CLASS_$_NSFileHandle
+ _OBJC_CLASS_$_NSFileManager
+ _OBJC_CLASS_$_NSMutableString
+ _OBJC_CLASS_$_NSURL
+ _OBJC_CLASS_$_NSUUID
+ _OBJC_CLASS_$_UARPSuperBinaryAsset
+ _UARPAccessoryHardwareFusingToString
+ _UARPStringDynamicAssetsFilepath
+ _UARPStringTempFilesFilepath
+ _UARPUtilsBuildURLForTemporaryFile
+ _UARPUtilsCreateTemporaryFolder
+ __NSConcreteGlobalBlock
+ _appendFirstUarpFilenameToFilepath
+ _currentTrainName
+ _dataFromHexString
+ _isDynamicAssetAnalytics
+ _isDynamicAssetHeySiri
+ _isDynamicAssetLogs
+ _isDynamicAssetMappedAnalytics
+ _isDynamicAssetPersonalization
+ _isDynamicAssetSysConfig
+ _isDynamicAssetVoiceAssist
+ _notify_post
+ _notify_register_check
+ _notify_set_state
+ _nullableObjectsEqual
+ _postStagingStatusForModelIdentifier
+ _uarpAnalyticsAssetFinalize
+ _uarpAnalyticsAssetInitialize
+ _uarpAssetTagAnalytics
+ _uarpAssetTagAnalytics4cc
+ _uarpAssetTagHeySiriModel
+ _uarpAssetTagHeySiriModel4cc
+ _uarpAssetTagLogs
+ _uarpAssetTagLogs4cc
+ _uarpAssetTagMappedAnalytics
+ _uarpAssetTagMappedAnalytics4cc
+ _uarpAssetTagPersonalization
+ _uarpAssetTagPersonalization4cc
+ _uarpAssetTagPersonalizedFirmware
+ _uarpAssetTagPersonalizedFirmware4cc
+ _uarpAssetTagStructAnalytics
+ _uarpAssetTagStructHeySiriModel
+ _uarpAssetTagStructLogs
+ _uarpAssetTagStructMappedAnalytics
+ _uarpAssetTagStructPersonalization
+ _uarpAssetTagStructPersonalizedFirmware
+ _uarpAssetTagStructSysconfig
+ _uarpAssetTagStructVoiceAssist
+ _uarpAssetTagSysconfig
+ _uarpAssetTagSysconfig4cc
+ _uarpAssetTagVoiceAssist
+ _uarpAssetTagVoiceAssist4cc
+ _uarpBuildMappedAnalyticsAsset
+ _uarpDynamicAssetComponentURL
+ _uarpDynamicAssetURL
+ _uarpFirmwareForAccessory
+ _uarpOuiAnalytics
+ _uarpOuiHeySiriModel
+ _uarpOuiLogs
+ _uarpOuiMappedAnalytics
+ _uarpOuiPersonalization
+ _uarpOuiSysconfig
+ _uarpOuiVoiceAssist
+ _uarpPersonalizationRequestAddBoardID
+ _uarpPersonalizationRequestAddBoardID64
+ _uarpPersonalizationRequestAddChipEpoch
+ _uarpPersonalizationRequestAddChipID
+ _uarpPersonalizationRequestAddChipRevision
+ _uarpPersonalizationRequestAddDigest
+ _uarpPersonalizationRequestAddECID
+ _uarpPersonalizationRequestAddEnableMixMatch
+ _uarpPersonalizationRequestAddLogicalUnitNumber
+ _uarpPersonalizationRequestAddManifestPrefix
+ _uarpPersonalizationRequestAddMeasurement
+ _uarpPersonalizationRequestAddMeasurementWithOverrides
+ _uarpPersonalizationRequestAddNonce
+ _uarpPersonalizationRequestAddNonceHash
+ _uarpPersonalizationRequestAddPayloadTag
+ _uarpPersonalizationRequestAddPrefixLUN
+ _uarpPersonalizationRequestAddPrefixNeedsLUN
+ _uarpPersonalizationRequestAddProductionMode
+ _uarpPersonalizationRequestAddRemoteAssetID
+ _uarpPersonalizationRequestAddRemoteAssetPayloadIndex
+ _uarpPersonalizationRequestAddSecurityDomain
+ _uarpPersonalizationRequestAddSecurityMode
+ _uarpPersonalizationRequestAddSoCLiveNonce
+ _uarpPersonalizationRequestAddSuffixLUN
+ _uarpPersonalizationRequestAddTicketPrefixLUN
+ _uarpPersonalizationRequestAssetFinalize
+ _uarpPersonalizationRequestAssetInitialize
+ _uarpPersonalizationRequestMoreRequestsToFollow
+ _uarpPersonalizationRequestPreparePayload
+ _uarpUtilsConcatenateURLs
+ _uarpVersionCompareStrings
- _uarpPlatformGetMaxRxPayloadLength
- _uarpPlatformGetMaxTxPayloadLength
- _uarpPlatformSetMaxRxPayloadLength
- _uarpPlatformSetMaxTxPayloadLength
CStrings:
+ "$RC_RELEASE"
+ "$SIDEBUILD_PARENT_TRAIN"
+ "%!@(MISSING)/%!@(MISSING)"
+ "%!@(MISSING)/%!@(MISSING)-%!c(MISSING)%!c(MISSING)%!c(MISSING)%!c(MISSING)"
+ "%!s(MISSING)"
+ "%!s(MISSING)%!@(MISSING)"
+ "-%!@(MISSING)"
+ ".uarp"
+ "/%!@(MISSING)"
+ "BOOL createPowerAssertion(NSString *__strong, IOPMAssertionID *)"
+ "BOOL releasePowerAssertion(IOPMAssertionID)"
+ "PreventUserIdleSystemSleep"
+ "com.apple.uarp.stagingstatus."
+ "uarpFirmwareForAccessory"

```
