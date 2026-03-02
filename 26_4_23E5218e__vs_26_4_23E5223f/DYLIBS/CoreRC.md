## CoreRC

> `/System/Library/PrivateFrameworks/CoreRC.framework/CoreRC`

```diff

-272.0.0.0.0
-  __TEXT.__text: 0x4954c
-  __TEXT.__auth_stubs: 0x620
-  __TEXT.__objc_methlist: 0x4f1c
+273.0.0.0.0
+  __TEXT.__text: 0x49f44
+  __TEXT.__auth_stubs: 0x640
+  __TEXT.__objc_methlist: 0x4f2c
   __TEXT.__const: 0x3c8
-  __TEXT.__cstring: 0xfbaf
-  __TEXT.__gcc_except_tab: 0xec
+  __TEXT.__cstring: 0xffb0
+  __TEXT.__gcc_except_tab: 0x12c
   __TEXT.__oslogstring: 0x1d1
-  __TEXT.__unwind_info: 0x1560
+  __TEXT.__dlopen_cstrs: 0x58
+  __TEXT.__unwind_info: 0x15b0
   __TEXT.__objc_classname: 0x5ca
-  __TEXT.__objc_methname: 0x99cb
-  __TEXT.__objc_methtype: 0x28f1
-  __TEXT.__objc_stubs: 0x7fe0
+  __TEXT.__objc_methname: 0x9b02
+  __TEXT.__objc_methtype: 0x2902
+  __TEXT.__objc_stubs: 0x8140
   __DATA_CONST.__got: 0x250
-  __DATA_CONST.__const: 0x1ce0
+  __DATA_CONST.__const: 0x1d40
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_nlclslist: 0x10
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0xd0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x23c8
+  __DATA_CONST.__objc_selrefs: 0x2420
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x140
   __DATA_CONST.__objc_arraydata: 0x168
-  __AUTH_CONST.__auth_got: 0x320
+  __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0x60
-  __AUTH_CONST.__cfstring: 0x3460
+  __AUTH_CONST.__cfstring: 0x3540
   __AUTH_CONST.__objc_const: 0x4d10
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x168

   __AUTH.__objc_data: 0xd70
   __DATA.__objc_ivar: 0x300
   __DATA.__data: 0x1398
-  __DATA.__bss: 0x370
+  __DATA.__bss: 0x390
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
+  - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: C7BC5A53-B9A5-3DDB-81EB-8C1FDFF36720
-  Functions: 2439
-  Symbols:   7169
-  CStrings:  4018
+  UUID: F009A7A3-A915-3844-A90E-051251CEDAA7
+  Functions: 2458
+  Symbols:   7231
+  CStrings:  4056
 
Symbols:
+ -[CECInterface triggerTapToRadarForAddressConflict:cecAddress:deviceType:]
+ -[CECInterface triggerTapToRadarForAddressConflict:cecAddress:deviceType:].cold.1
+ -[CECInterface triggerTapToRadarForAddressConflict:cecAddress:deviceType:].cold.2
+ GCC_except_table16
+ GCC_except_table27
+ _TapToRadarKitLibrary
+ _TapToRadarKitLibrary.cold.1
+ _TapToRadarKitLibraryCore
+ _TapToRadarKitLibraryCore.frameworkLibrary
+ ___TapToRadarKitLibraryCore_block_invoke
+ ___block_descriptor_40_e8_32r_e5_v8?0lr32l8
+ ___block_descriptor_48_e8_32r_e5_v8?0lr32l8
+ ___getRadarComponentClass_block_invoke
+ ___getRadarComponentClass_block_invoke.cold.1
+ ___getRadarDraftClass_block_invoke
+ ___getRadarDraftClass_block_invoke.cold.1
+ ___getTapToRadarServiceClass_block_invoke
+ ___getTapToRadarServiceClass_block_invoke.cold.1
+ __sl_dlopen
+ _audit_stringTapToRadarKit
+ _getRadarComponentClass
+ _getRadarComponentClass.softClass
+ _getRadarDraftClass
+ _getRadarDraftClass.softClass
+ _getTapToRadarServiceClass
+ _getTapToRadarServiceClass.softClass
+ _objc_getClass
+ _objc_msgSend$createDraft:forProcessNamed:withDisplayReason:error:
+ _objc_msgSend$handleFailureInFunction:file:lineNumber:description:
+ _objc_msgSend$initWithName:version:identifier:
+ _objc_msgSend$setAutoDiagnostics:
+ _objc_msgSend$setClassification:
+ _objc_msgSend$setComponent:
+ _objc_msgSend$setIsUserInitiated:
+ _objc_msgSend$setProblemDescription:
+ _objc_msgSend$setTitle:
+ _objc_msgSend$shared
+ _objc_msgSend$triggerTapToRadarForAddressConflict:cecAddress:deviceType:
- -[CECInterface allocateCECAddress:forDeviceType:error:].cold.5
CStrings:
+ "%s"
+ "-[CECInterface triggerTapToRadarForAddressConflict:cecAddress:deviceType:]"
+ "A CEC logical address conflict was detected, indicating two devices attempted to use the same logical address.\n\nDiagnostic Information:\n- Address Mask: 0x%04x\n- CEC Address: 0x%02x\n- Device Type: %s\n- Interface: %@\n- Bus Delegate: %@\n- Devices on Bus: %@\n\nThis is a critical error that indicates either a bug in address allocation logic or unexpected behavior from a CEC device on the bus."
+ "All"
+ "CEC Address Conflict Detected: addressMask=0x%04x, address=0x%02x, type=%s"
+ "CECInterface.m"
+ "Class getRadarComponentClass(void)_block_invoke"
+ "Class getRadarDraftClass(void)_block_invoke"
+ "Class getTapToRadarServiceClass(void)_block_invoke"
+ "Failed to create Tap-to-Radar draft: %@\n"
+ "RadarComponent"
+ "RadarDraft"
+ "Tap-to-Radar draft created successfully for CEC address conflict\n"
+ "TapToRadarKit not available, cannot create radar draft\n"
+ "TapToRadarService"
+ "Unable to find class %s"
+ "an HDMI device inconsistency was found in display setup"
+ "createDraft:forProcessNamed:withDisplayReason:error:"
+ "handleFailureInFunction:file:lineNumber:description:"
+ "initWithName:version:identifier:"
+ "setAutoDiagnostics:"
+ "setClassification:"
+ "setComponent:"
+ "setIsUserInitiated:"
+ "setProblemDescription:"
+ "setTitle:"
+ "shared"
+ "softlink:o:path:/AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit"
+ "triggerTapToRadarForAddressConflict:cecAddress:deviceType:"
+ "v28@0:8S16C20C24"
+ "void *TapToRadarKitLibrary(void)"

```
