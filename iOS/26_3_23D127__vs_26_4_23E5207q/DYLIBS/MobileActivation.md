## MobileActivation

> `/System/Library/PrivateFrameworks/MobileActivation.framework/MobileActivation`

```diff

-1068.80.3.0.0
-  __TEXT.__text: 0xe88c
-  __TEXT.__auth_stubs: 0x260
+1076.100.26.0.0
+  __TEXT.__text: 0xf384
+  __TEXT.__auth_stubs: 0x2a0
   __TEXT.__objc_methlist: 0x4cc
-  __TEXT.__cstring: 0x1de4
+  __TEXT.__cstring: 0x2120
   __TEXT.__const: 0x8a
-  __TEXT.__gcc_except_tab: 0x678
+  __TEXT.__gcc_except_tab: 0x6e4
   __TEXT.__oslogstring: 0xb
-  __TEXT.__unwind_info: 0x410
+  __TEXT.__unwind_info: 0x418
   __TEXT.__objc_classname: 0x59
-  __TEXT.__objc_methname: 0xfeb
+  __TEXT.__objc_methname: 0x1055
   __TEXT.__objc_methtype: 0x3df
-  __TEXT.__objc_stubs: 0xec0
-  __DATA_CONST.__got: 0xd8
-  __DATA_CONST.__const: 0x268
+  __TEXT.__objc_stubs: 0xfa0
+  __DATA_CONST.__got: 0xe8
+  __DATA_CONST.__const: 0x298
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4b0
+  __DATA_CONST.__objc_selrefs: 0x4e0
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__objc_arraydata: 0x490
-  __AUTH_CONST.__auth_got: 0x140
-  __AUTH_CONST.__const: 0x2c0
-  __AUTH_CONST.__cfstring: 0x2340
+  __DATA_CONST.__objc_arraydata: 0x4d0
+  __AUTH_CONST.__auth_got: 0x160
+  __AUTH_CONST.__const: 0x2f0
+  __AUTH_CONST.__cfstring: 0x26a0
   __AUTH_CONST.__objc_const: 0x3b0
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0x18
   __DATA.__objc_ivar: 0x4
   __DATA.__data: 0xe4
-  __DATA.__bss: 0x10
+  __DATA.__bss: 0x20
   __DATA_DIRTY.__objc_data: 0xa0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 81302A3D-495C-3F64-99AD-F525609B5815
-  Functions: 246
-  Symbols:   794
-  CStrings:  816
+  UUID: 2A288969-AEAD-3F7B-930D-531F21A7A8D8
+  Functions: 252
+  Symbols:   828
+  CStrings:  881
 
Symbols:
+ -[MadGate getUCRTSalvageState:]
+ GCC_except_table23
+ GCC_except_table67
+ GCC_except_table78
+ GCC_except_table92
+ _MAECopyDeviceRegionInfoWithError
+ _MAECopyDeviceRegionInfoWithError.onceToken
+ _MAECopyDeviceRegionInfoWithError.regionInfoFilePath
+ _MAEGetUCRTSalvageStateWithError
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSFileManager
+ ___31-[MadGate getUCRTSalvageState:]_block_invoke
+ ___31-[MadGate getUCRTSalvageState:]_block_invoke_2
+ ___MAECopyDeviceRegionInfoWithError_block_invoke
+ ___MAECopyDeviceRegionInfoWithError_block_invoke.cold.1
+ ___block_descriptor_40_e8_32r_e5_v8?0l
+ __os_crash
+ __os_feature_enabled_impl
+ _container_system_group_path_for_identifier
+ _free
+ _getUCRTSalvageState
+ _isNSDate
+ _kMADeviceRegionCountryCode
+ _kMADeviceRegionRegionInfo
+ _kMADeviceRegionSoftwareBehaviors
+ _kMAMobileActivationGroupContainerID
+ _kMAUCRTSLVGDate
+ _kMAUCRTSLVGState
+ _kMAUCRTSLVGStateKBBSharedSerial
+ _kMAUCRTSLVGStateKBBUniqueSerial
+ _kMAUCRTSLVGStateKGB
+ _kMAUCRTSLVGStateUnavailable
+ _objc_msgSend$containsString:
+ _objc_msgSend$defaultManager
+ _objc_msgSend$description
+ _objc_msgSend$fileExistsAtPath:
+ _objc_msgSend$getUCRTSalvageState:
+ _objc_msgSend$getUCRTSalvageStateWithCompletionBlock:
+ _objc_msgSend$hasSuffix:
+ _objc_msgSend$initWithContentsOfFile:
+ _objc_msgSend$stringByAppendingPathComponent:
+ _os_variant_is_darwinos
- -[MadGate copyRegionDataForGestalt:]
- GCC_except_table63
- GCC_except_table76
- GCC_except_table90
- _MAECopyRegionDataForGestaltWithError
- ___36-[MadGate copyRegionDataForGestalt:]_block_invoke
- ___36-[MadGate copyRegionDataForGestalt:]_block_invoke_2
- _copyRegionDataForGestalt
- _kMAManufacturingData
- _kMARegionDataForGestaltCountryCode
- _kMARegionDataForGestaltRegionInfo
- _kMARegionDataForGestaltSotwareBehaviors
- _objc_msgSend$copyRegionDataForGestalt:
- _objc_msgSend$copyRegionDataForGestaltWithCompletionBlock:
- _objc_retainAutoreleaseReturnValue
CStrings:
+ "-[MadGate getUCRTSalvageState:]_block_invoke"
+ "DEV"
+ "Device region is currently unknown."
+ "Device region is unsupported."
+ "DeviceRegionCountryCode"
+ "DeviceRegionInfoFromActivation"
+ "DeviceRegionRegionInfo"
+ "DeviceRegionSoftwareBehaviors"
+ "Devices"
+ "Failed to copy system container path for %@"
+ "Failed to get UCRT salvage state."
+ "Failed to query '%@'."
+ "Failed to retrieve the device region file path."
+ "HWModelStr"
+ "Invalid or missing UCRT salvage date."
+ "Invalid or missing UCRT salvage state."
+ "Library/region_info/region_info.plist"
+ "MAECopyDeviceRegionInfoWithError"
+ "MAECopyDeviceRegionInfoWithError_block_invoke"
+ "MAEGetUCRTSalvageStateWithError"
+ "SCARemoteView Appex"
+ "ShouldHactivate"
+ "UCRTSLVGDate"
+ "UCRTSLVGState"
+ "UCRTSLVGStateKBBSharedSerial"
+ "UCRTSLVGStateKBBUniqueSerial"
+ "UCRTSLVGStateKGB"
+ "UCRTSLVGStateUnavailable"
+ "anomalydetectiond"
+ "com.apple.MobileAsset.DownloadService.Backported"
+ "com.apple.MobileAsset.DownloadService.Builtin"
+ "containsString:"
+ "defaultManager"
+ "fileExistsAtPath:"
+ "fmdautomationtool"
+ "getUCRTSalvageState:"
+ "getUCRTSalvageStateWithCompletionBlock:"
+ "hasSuffix:"
+ "iFPGA"
+ "iOS Device Activator (MobileActivation-1076.100.26)"
+ "initWithContentsOfFile:"
+ "stringByAppendingPathComponent:"
+ "systemgroup.com.apple.mobileactivationd"
+ "triald"
+ "triald_system"
- "-[MadGate copyRegionDataForGestalt:]_block_invoke"
- "ManufacturingData"
- "RegionDataForGestaltCountryCode"
- "RegionDataForGestaltRegionInfo"
- "RegionDataForGestaltSotwareBehaviors"
- "copyRegionDataForGestalt:"
- "copyRegionDataForGestaltWithCompletionBlock:"
- "iOS Device Activator (MobileActivation-1068.80.3)"

```
