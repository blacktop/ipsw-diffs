## UARPUpdaterServiceUSBPD

> `/System/Library/PrivateFrameworks/MobileAccessoryUpdater.framework/XPCServices/UARPUpdaterServiceUSBPD.xpc/Contents/MacOS/UARPUpdaterServiceUSBPD`

```diff

-1163.0.0.0.0
-  __TEXT.__text: 0x70fbc
-  __TEXT.__auth_stubs: 0x730
-  __TEXT.__objc_stubs: 0x33c0
+1155.0.0.0.0
+  __TEXT.__text: 0x7325c
+  __TEXT.__auth_stubs: 0x750
+  __TEXT.__objc_stubs: 0x3660
   __TEXT.__objc_methlist: 0x12f4
   __TEXT.__const: 0x76800
-  __TEXT.__oslogstring: 0x26ef
-  __TEXT.__cstring: 0x29c0
+  __TEXT.__oslogstring: 0x28ca
+  __TEXT.__cstring: 0x2acb
   __TEXT.__objc_classname: 0x205
   __TEXT.__objc_methtype: 0x338a
-  __TEXT.__objc_methname: 0x430a
+  __TEXT.__objc_methname: 0x4525
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__unwind_info: 0xc30
+  __TEXT.__unwind_info: 0xcb0
   __TEXT.__eh_frame: 0x318
-  __DATA_CONST.__auth_got: 0x3a8
-  __DATA_CONST.__got: 0x170
+  __DATA_CONST.__auth_got: 0x3b8
+  __DATA_CONST.__got: 0x178
   __DATA_CONST.__auth_ptr: 0x38
-  __DATA_CONST.__const: 0x18d0
-  __DATA_CONST.__cfstring: 0x660
+  __DATA_CONST.__const: 0x1910
+  __DATA_CONST.__cfstring: 0x7a0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x4070
-  __DATA.__objc_selrefs: 0xe88
+  __DATA.__objc_selrefs: 0xf30
   __DATA.__objc_ivar: 0x228
   __DATA.__objc_data: 0x3c0
-  __DATA.__data: 0x3d5
-  __DATA.__bss: 0x1174
+  __DATA.__data: 0x405
+  __DATA.__bss: 0x11af
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libcompression.dylib
   - /usr/lib/liblzma.5.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1459
-  Symbols:   535
-  CStrings:  343
+  Functions: 1540
+  Symbols:   609
+  CStrings:  356
 
Symbols:
+ _IOPMAssertionCreateWithName
+ _IOPMAssertionRelease
+ _InternalStorageDirectoryPath
+ _NSFilePosixPermissions
+ _UARPStringDynamicAssetsFilepath
+ _UARPStringTempFilesFilepath
+ _UARPUtilsBuildURLForTemporaryFile
+ _UARPUtilsCreateTemporaryFolder
+ __NSConcreteGlobalBlock
+ _appendFirstUarpFilenameToFilepath
+ _currentTrainName
+ _dataFromHexString
+ _isDynamicAssetHeySiri
+ _isDynamicAssetMappedAnalytics
+ _isDynamicAssetPersonalization
+ _isDynamicAssetSysConfig
+ _isDynamicAssetVoiceAssist
+ _notify_post
+ _notify_register_check
+ _notify_set_state
+ _nullableObjectsEqual
+ _postStagingStatusForModelIdentifier
+ _uarpAssetTagHeySiriModel
+ _uarpAssetTagHeySiriModel4cc
+ _uarpAssetTagMappedAnalytics
+ _uarpAssetTagMappedAnalytics4cc
+ _uarpAssetTagPersonalization
+ _uarpAssetTagPersonalization4cc
+ _uarpAssetTagPersonalizedFirmware
+ _uarpAssetTagPersonalizedFirmware4cc
+ _uarpAssetTagStructHeySiriModel
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
+ _uarpFirmwareForAccessory
+ _uarpOuiHeySiriModel
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
