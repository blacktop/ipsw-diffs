## CoreUARP

> `/System/Library/PrivateFrameworks/CoreUARP.framework/CoreUARP`

```diff

-916.0.46.0.0
-  __TEXT.__text: 0x5ac98
-  __TEXT.__auth_stubs: 0x840
-  __TEXT.__objc_methlist: 0x55dc
+916.40.22.0.2
+  __TEXT.__text: 0x5b95c
+  __TEXT.__auth_stubs: 0x860
+  __TEXT.__objc_methlist: 0x5684
   __TEXT.__const: 0xe0
-  __TEXT.__cstring: 0x5058
+  __TEXT.__cstring: 0x5121
   __TEXT.__gcc_except_tab: 0x638
-  __TEXT.__oslogstring: 0x393c
+  __TEXT.__oslogstring: 0x39d8
   __TEXT.__dlopen_cstrs: 0xa4
-  __TEXT.__unwind_info: 0x1a30
-  __TEXT.__objc_classname: 0xbb1
-  __TEXT.__objc_methname: 0xb21a
-  __TEXT.__objc_methtype: 0x3380
-  __TEXT.__objc_stubs: 0x7660
+  __TEXT.__unwind_info: 0x1a54
+  __TEXT.__objc_classname: 0xbce
+  __TEXT.__objc_methname: 0xb386
+  __TEXT.__objc_methtype: 0x33c6
+  __TEXT.__objc_stubs: 0x7720
   __DATA_CONST.__got: 0x48
-  __DATA_CONST.__const: 0x1920
-  __DATA_CONST.__objc_classlist: 0x320
+  __DATA_CONST.__const: 0x1938
+  __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x7fc8
-  __DATA_CONST.__objc_selrefs: 0x2670
-  __AUTH_CONST.__cfstring: 0x4a40
-  __AUTH_CONST.__objc_const: 0x2d30
+  __DATA_CONST.__objc_const: 0x8160
+  __DATA_CONST.__objc_selrefs: 0x26b8
+  __AUTH_CONST.__cfstring: 0x4b00
+  __AUTH_CONST.__objc_const: 0x2d78
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__objc_intobj: 0xac8
-  __AUTH_CONST.__auth_got: 0x430
-  __AUTH.__objc_data: 0x17c0
+  __AUTH_CONST.__auth_got: 0x440
+  __AUTH.__objc_data: 0x1810
   __DATA.__objc_protorefs: 0x8
-  __DATA.__objc_classrefs: 0x388
-  __DATA.__objc_superrefs: 0x308
-  __DATA.__objc_ivar: 0x7a8
+  __DATA.__objc_classrefs: 0x390
+  __DATA.__objc_superrefs: 0x310
+  __DATA.__objc_ivar: 0x7c0
   __DATA.__data: 0x2c3
   __DATA.__bss: 0x1f0
   __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__bss: 0x258
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog

   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
-  UUID: 0E66EDCD-6CF4-35BE-8955-4FA86D1A7645
-  Functions: 2711
-  Symbols:   8257
-  CStrings:  4162
+  UUID: 5C5A96F7-25D2-39C8-B7DF-1152AC6ADF1C
+  Functions: 2730
+  Symbols:   8317
+  CStrings:  4195
 
Symbols:
+ -[UARPAccessoryHIDPersonality getHash]
+ -[UARPAccessoryHIDPersonality initWithVendorID:productID:]
+ -[UARPAccessoryHIDPersonality isEqual:]
+ -[UARPAccessoryHIDPersonality personalityIdentifier:]
+ -[UARPAccessoryHIDPersonality productID]
+ -[UARPAccessoryHIDPersonality vendorID]
+ -[UARPAccessoryHardwareHID .cxx_destruct]
+ -[UARPAccessoryHardwareHID addPersonality:]
+ -[UARPAccessoryHardwareHID personalities]
+ -[UARPController firmwareStagingProgress:assetID:bytesSent:bytesTotal:filterProgress:]
+ -[UARPControllerXPC stagingCompleteForAccessoryID:assetID:status:]
+ -[UARPSupportedAccessory setUpdateRequiresPowerAssertion:]
+ -[UARPSupportedAccessory updateRequiresPowerAssertion]
+ -[UARPUploader firmwareStagingProgress:assetID:bytesSent:bytesTotal:filterProgress:]
+ -[UARPUploaderUARP shouldSendFirmwareStagingProgressForAccessory:asset:]
+ GCC_except_table33
+ GCC_except_table37
+ GCC_except_table40
+ GCC_except_table49
+ GCC_except_table52
+ GCC_except_table55
+ GCC_except_table58
+ GCC_except_table61
+ _IOPMAssertionCreateWithName
+ _IOPMAssertionRelease
+ _OBJC_CLASS_$_UARPAccessoryHIDPersonality
+ _OBJC_IVAR_$_UARPAccessoryHIDPersonality._productID
+ _OBJC_IVAR_$_UARPAccessoryHIDPersonality._vendorID
+ _OBJC_IVAR_$_UARPAccessoryHardwareHID._personalities
+ _OBJC_IVAR_$_UARPSupportedAccessory._updateRequiresPowerAssertion
+ _OBJC_IVAR_$_UARPUploaderUARP._isInternalBuild
+ _OBJC_IVAR_$_UARPUploaderUARP._lastReportedProgressTime
+ _OBJC_METACLASS_$_UARPAccessoryHIDPersonality
+ __OBJC_$_INSTANCE_METHODS_UARPAccessoryHIDPersonality
+ __OBJC_$_INSTANCE_VARIABLES_UARPAccessoryHIDPersonality
+ __OBJC_$_PROP_LIST_UARPAccessoryHIDPersonality
+ __OBJC_CLASS_RO_$_UARPAccessoryHIDPersonality
+ __OBJC_METACLASS_RO_$_UARPAccessoryHIDPersonality
+ ___34-[UARPControllerXPC xpcConnection]_block_invoke.111
+ ___45-[UARPControllerXPC getSupportedAccessories:]_block_invoke.135
+ ___46-[UARPControllerXPC getAssetIDForAccessoryID:]_block_invoke.131
+ ___48-[UARPControllerXPC getAttestationCertificates:]_block_invoke.137
+ ___56-[UARPControllerXPC getSandboxExtensionTokenForAssetID:]_block_invoke.139
+ ___60-[UARPControllerXPC getSupplementalAssetNameForAccessoryID:]_block_invoke.133
+ ___86-[UARPController firmwareStagingProgress:assetID:bytesSent:bytesTotal:filterProgress:]_block_invoke
+ ___block_literal_global.636
+ ___block_literal_global.638
+ _createPowerAssertion
+ _createPowerAssertion.cold.1
+ _createPowerAssertion.cold.2
+ _kUARPSupportedAccessoryCaseModelNameIdentifier
+ _kUARPSupportedAccessoryKeyPersonalities
+ _kUARPSupportedAccessoryKeyUpdateRequiresPowerAssertion
+ _objc_msgSend$addPersonality:
+ _objc_msgSend$firmwareStagingProgress:assetID:bytesSent:bytesTotal:filterProgress:
+ _objc_msgSend$isEqualToSet:
+ _objc_msgSend$personalities
+ _objc_msgSend$shouldSendFirmwareStagingProgressForAccessory:asset:
+ _objc_msgSend$supportsInternalSettings
+ _releasePowerAssertion
+ _releasePowerAssertion.cold.1
- -[UARPController firmwareStagingProgress:assetID:bytesSent:bytesTotal:]
- -[UARPUploader firmwareStagingProgress:assetID:bytesSent:bytesTotal:]
- GCC_except_table39
- GCC_except_table42
- GCC_except_table48
- GCC_except_table51
- GCC_except_table54
- GCC_except_table57
- GCC_except_table60
- ___34-[UARPControllerXPC xpcConnection]_block_invoke.108
- ___45-[UARPControllerXPC getSupportedAccessories:]_block_invoke.132
- ___46-[UARPControllerXPC getAssetIDForAccessoryID:]_block_invoke.128
- ___48-[UARPControllerXPC getAttestationCertificates:]_block_invoke.134
- ___56-[UARPControllerXPC getSandboxExtensionTokenForAssetID:]_block_invoke.136
- ___60-[UARPControllerXPC getSupplementalAssetNameForAccessoryID:]_block_invoke.130
- ___71-[UARPController firmwareStagingProgress:assetID:bytesSent:bytesTotal:]_block_invoke
- ___block_literal_global.627
- ___block_literal_global.629
CStrings:
+ "\x02\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xe2\x11"
+ "%@.%04x.%04x"
+ "%s: Failed to create power assertion %@ with error %d"
+ "%s: Failed to release power assertion with error %d"
+ "%s: Invalid powerAssertionID received from caller"
+ "<VendorID = 0x%04x, ProductID = 0x%04x>"
+ "BOOL createPowerAssertion(NSString *__strong, IOPMAssertionID *)"
+ "BOOL releasePowerAssertion(IOPMAssertionID)"
+ "Case"
+ "DawnB"
+ "HID, "
+ "Personalities"
+ "PreventUserIdleSystemSleep"
+ "TB,V_updateRequiresPowerAssertion"
+ "UARPAccessoryHIDPersonality"
+ "UpdateRequiresPowerAssertion"
+ "_lastReportedProgressTime"
+ "_personalities"
+ "_updateRequiresPowerAssertion"
+ "addPersonality:"
+ "firmwareStagingProgress:assetID:bytesSent:bytesTotal:filterProgress:"
+ "getHash"
+ "isEqualToSet:"
+ "personalities"
+ "personalityIdentifier:"
+ "setUpdateRequiresPowerAssertion:"
+ "shouldSendFirmwareStagingProgressForAccessory:asset:"
+ "updateRequiresPowerAssertion"
+ "v40@0:8@\"UARPAccessoryID\"16@\"UARPAssetID\"24Q32"
+ "v52@0:8@16@24Q32Q40B48"
- "\x02\xf0\xf0\xf0\xf0\xf0\xf0\xf0\xe2"
- "Dawn"
- "HID, VendorID = 0x%04x, ProductID = 0x%04x"

```
