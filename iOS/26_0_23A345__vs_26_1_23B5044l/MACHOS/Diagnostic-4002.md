## Diagnostic-4002

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-4002.appex/Diagnostic-4002`

```diff

-1066.2.1.0.0
-  __TEXT.__text: 0x232c
-  __TEXT.__auth_stubs: 0x370
-  __TEXT.__objc_stubs: 0x7c0
-  __TEXT.__objc_methlist: 0x3b4
+1066.40.34.0.0
+  __TEXT.__text: 0x2068
+  __TEXT.__auth_stubs: 0x330
+  __TEXT.__objc_stubs: 0x720
+  __TEXT.__objc_methlist: 0x34c
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x246
-  __TEXT.__oslogstring: 0x4eb
-  __TEXT.__objc_classname: 0x6b
-  __TEXT.__objc_methtype: 0x2e1
-  __TEXT.__objc_methname: 0x99d
+  __TEXT.__cstring: 0xef
+  __TEXT.__oslogstring: 0x55b
+  __TEXT.__objc_classname: 0x5d
+  __TEXT.__objc_methtype: 0x2d6
+  __TEXT.__objc_methname: 0x8e0
   __TEXT.__gcc_except_tab: 0x60
-  __TEXT.__unwind_info: 0x100
-  __DATA_CONST.__auth_got: 0x1c8
-  __DATA_CONST.__got: 0x40
-  __DATA_CONST.__const: 0x140
-  __DATA_CONST.__cfstring: 0x200
-  __DATA_CONST.__objc_classlist: 0x20
+  __TEXT.__unwind_info: 0xf0
+  __DATA_CONST.__auth_got: 0x1a8
+  __DATA_CONST.__got: 0x58
+  __DATA_CONST.__const: 0xa0
+  __DATA_CONST.__cfstring: 0x120
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA.__objc_const: 0x580
-  __DATA.__objc_selrefs: 0x320
+  __DATA.__objc_const: 0x4f0
+  __DATA.__objc_selrefs: 0x2e0
   __DATA.__objc_ivar: 0x24
-  __DATA.__objc_data: 0x140
+  __DATA.__objc_data: 0xf0
   __DATA.__data: 0xc0
-  __DATA.__bss: 0x40
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/DiagnosticsKit.framework/DiagnosticsKit
   - /System/Library/PrivateFrameworks/DiagnosticsSupport.framework/DiagnosticsSupport
+  - /System/Library/PrivateFrameworks/NearField.framework/NearField
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 66E95D84-42AF-35AA-8606-BC24DD583875
-  Functions: 76
-  Symbols:   84
-  CStrings:  227
+  UUID: A80EDEF5-A721-318F-9E00-02E92AC29240
+  Functions: 60
+  Symbols:   80
+  CStrings:  205
 
Symbols:
+ _OBJC_CLASS_$_NFHardwareManager
+ _OBJC_CLASS_$_NFRemoteAdminManager
+ _OBJC_CLASS_$_NFSecureElement
- _NSClassFromString
- _OBJC_CLASS_$_DASoftLinking
- _OBJC_METACLASS_$_DASoftLinking
- __NSConcreteGlobalBlock
- _dispatch_once
- _dlopen
- _objc_retainAutoreleaseReturnValue
CStrings:
+ "Failed to get NearField embedded SN with error: %@"
+ "NearField.fwk is missing, assuming Apple Pay is not present."
+ "embeddedSecureElementWithError:"
- "#24@0:8@16"
- "/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit"
- "/System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit"
- "/System/Library/PrivateFrameworks/NearField.framework/NearField"
- "/System/Library/PrivateFrameworks/NearFieldAccessory.framework/NearFieldAccessory"
- "DASoftLinking"
- "NFHardwareManager"
- "NFRemoteAdminManager"
- "NFSecureElement"
- "UTF8String"
- "biometricKitClass:"
- "coreRepairClass:"
- "isBiometricKitFrameworkAvailable"
- "isCoreRepairFrameworkAvailable"
- "isNearFieldAccessoryFrameworkAvailable"
- "isNearFieldFrameworkAvailable"
- "nearFieldAccessoryClass:"
- "nearFieldClass:"

```
