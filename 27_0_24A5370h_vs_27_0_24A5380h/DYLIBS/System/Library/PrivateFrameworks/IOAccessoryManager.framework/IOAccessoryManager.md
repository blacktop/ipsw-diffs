## IOAccessoryManager

> `/System/Library/PrivateFrameworks/IOAccessoryManager.framework/IOAccessoryManager`

```diff

-  __TEXT.__text: 0x23ce8
-  __TEXT.__objc_methlist: 0x3284
-  __TEXT.__const: 0x8d8
-  __TEXT.__oslogstring: 0x596b
-  __TEXT.__cstring: 0x4a58
+  __TEXT.__text: 0x22d9c
+  __TEXT.__objc_methlist: 0x3294
+  __TEXT.__const: 0x8b8
+  __TEXT.__oslogstring: 0x560c
+  __TEXT.__cstring: 0x4828
   __TEXT.__ustring: 0x154
-  __TEXT.__gcc_except_tab: 0x40
-  __TEXT.__unwind_info: 0x588
+  __TEXT.__unwind_info: 0x578
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x460
+  __DATA_CONST.__const: 0x440
   __DATA_CONST.__objc_classlist: 0x80
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1ce8
+  __DATA_CONST.__objc_selrefs: 0x1cb0
   __DATA_CONST.__objc_superrefs: 0x68
   __DATA_CONST.__objc_arraydata: 0x20
-  __DATA_CONST.__got: 0x300
+  __DATA_CONST.__got: 0x2f0
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x31a0
+  __AUTH_CONST.__cfstring: 0x3020
   __AUTH_CONST.__objc_const: 0x6b18
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x230
   __DATA.__objc_ivar: 0x7a4
-  __DATA.__data: 0x248
-  __DATA.__common: 0x58
+  __DATA.__data: 0x1e8
+  __DATA.__common: 0x50
   __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x2d0
   __DATA_DIRTY.__bss: 0x70
-  __DATA_DIRTY.__common: 0x170
+  __DATA_DIRTY.__common: 0x160
   - /System/Library/Frameworks/Accelerate.framework/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1413
-  Symbols:   4463
-  CStrings:  1364
+  Functions: 1407
+  Symbols:   4413
+  CStrings:  1300
 
Sections:
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH.__objc_data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[IOPortLDCMManagerV4 setForcePortWet:]
+ _objc_msgSend$initWithSuiteName:
+ _objc_msgSend$setForcePortWet:
- GCC_except_table171
- _OBJC_CLASS_$_ASAssetQuery
- _OBJC_EHTYPE_$_NSException
- _OUTLINED_FUNCTION_62
- _OUTLINED_FUNCTION_63
- __Unwind_Resume
- ___block_descriptor_36_e5_v8?0l
- ___objc_personality_v0
- _gAssetContext
- _gLdcmBehaviorPlist
- _kIOAMLDCMBehaviorDryThresholdDictionarykey
- _kIOAMLDCMBehaviorPlistBehaviorBitmaskKey
- _kIOAMLDCMBehaviorPlistConsecutiveDetectedInterval
- _kIOAMLDCMBehaviorPlistConsecutiveDetectedThresh
- _kIOAMLDCMBehaviorPlistConsecutiveNotDetectedInterval
- _kIOAMLDCMBehaviorPlistConsecutiveNotDetectedThresh
- _kIOAMLDCMBehaviorPlistDeviceGen1SubKey
- _kIOAMLDCMBehaviorPlistFdpBitmaskKey
- _kIOAMLDCMBehaviorPlistLegacySubKey
- _kIOAMLDCMBehaviorPlistVersionKey
- _kIOAMLDCMBehaviorThresholdDefaultKey
- _kIOAMLDCMBehaviorWetThresholdDictionaryKey
- _kMaximumErrorAssetQueryExtraSec
- _kMaximumRegularAssetQueryExtraSec
- _kMinimumErrorAssetQueryIntervalSec
- _kMinimumRegularAssetQueryIntervalSec
- _kSupportedLdcmBehaviorPlistVersion
- _objc_begin_catch
- _objc_end_catch
- _objc_msgSend$absoluteString
- _objc_msgSend$beginDownloadWithOptions:
- _objc_msgSend$description
- _objc_msgSend$dictionaryWithContentsOfURL:
- _objc_msgSend$initWithAssetType:
- _objc_msgSend$localURL
- _objc_msgSend$requiredDiskSpaceIsAvailable:error:
- _objc_msgSend$runQueryAndReturnError:
- _objc_msgSend$setDryTransitionCapacitanceThreshold:
- _objc_msgSend$setFdpBehaviorMask:
- _objc_msgSend$setQueriesLocalAssetInformationOnly:
- _objc_msgSend$setWetTransitionCapacitanceThreshold:
- _objc_msgSend$unsignedIntValue
- _performAssetQuery
- _processLdcmBehaviorPlist
CStrings:
+ "LDCM - Setting ForcePortWet in kernel: %d"
+ "com.apple.accessoryd.plugin"
- "%s\n"
- "%s finished local asset query\n"
- "%s finished remote asset query\n"
- "%s starting local asset query\n"
- "%s starting remote asset query\n"
- "%s: Asset not yet downloaded, fetching: %s"
- "%s: Asset on disk, found at: %s\n"
- "%s: LDCM behavior plist version: %u, supported %d\n"
- "%s: MobileAsset query results: %s\n"
- "%s: Skipping download for uninstalled asset. Error in asset %s: %s\n"
- "%s: commitPersistentConfigDictParams: success=%s"
- "%s: consecutive detected interval : %u\n"
- "%s: consecutive detected thresh : %u\n"
- "%s: consecutive not detected interval : %u\n"
- "%s: consecutive not detected thresh : %u\n"
- "%s: dictionaryWithContentsOfURL failed\n"
- "%s: dictionaryWithContentsOfURL succeeded\n"
- "%s: encountered error: %s\n"
- "%s: exception\n"
- "%s: failed\n"
- "%s: fdpBehaviorMask : %#x\n"
- "%s: getOrDownloadAsset: %s\n"
- "%s: load_dict failed\n"
- "%s: no persistent dictionary"
- "%s: success=%s\n"
- "%s: userBehaviorMask : %#x\n"
- "%s: wet threshold: %f dry threshold: %f\n"
- "BehaviorBitmask"
- "ConsecutiveDetectedInterval"
- "ConsecutiveDetectedThresh"
- "ConsecutiveNotDetectedInterval"
- "ConsecutiveNotDetectedThresh"
- "DeviceGen1"
- "DeviceLegacy"
- "DryThresholds"
- "FalsePreventionBitmask"
- "IOAccessoryHandleAttach_block_invoke"
- "IOAccessoryManagerLdcmBehavior.plist"
- "IOAccessoryServiceMatchingCallback_block_invoke"
- "Version"
- "WetThresholds"
- "commitPersistentConfigDictParams"
- "configDictionary"
- "downloadAssetWithError"
- "false"
- "getAsset"
- "load_dict"
- "performAssetQuery"
- "processLdcmBehaviorPlist"
- "processLdcmBehaviorPlistForVersion1"
- "processLdcmBehaviorPlistForVersion2"
- "retrievePersistentConfigDictParams"
- "true"

```
