## iosdiagnosticsd

> `/System/Library/PrivateFrameworks/iOSDiagnostics.framework/iosdiagnosticsd`

```diff

-1066.2.1.0.0
-  __TEXT.__text: 0xd874
-  __TEXT.__auth_stubs: 0x690
+1066.40.34.0.0
+  __TEXT.__text: 0xd1a0
+  __TEXT.__auth_stubs: 0x650
   __TEXT.__objc_stubs: 0x2500
-  __TEXT.__objc_methlist: 0x15f4
-  __TEXT.__const: 0x88
-  __TEXT.__gcc_except_tab: 0x6f4
-  __TEXT.__objc_methname: 0x33a0
-  __TEXT.__oslogstring: 0xc31
-  __TEXT.__cstring: 0xba0
-  __TEXT.__objc_classname: 0x34a
+  __TEXT.__objc_methlist: 0x15fc
+  __TEXT.__const: 0x78
+  __TEXT.__gcc_except_tab: 0x704
+  __TEXT.__objc_methname: 0x3429
+  __TEXT.__oslogstring: 0xbc7
+  __TEXT.__cstring: 0xbe6
+  __TEXT.__objc_classname: 0x349
   __TEXT.__objc_methtype: 0x104b
-  __TEXT.__dlopen_cstrs: 0xfc
-  __TEXT.__unwind_info: 0x4d8
-  __DATA_CONST.__auth_got: 0x358
-  __DATA_CONST.__got: 0x230
-  __DATA_CONST.__const: 0x5f0
-  __DATA_CONST.__cfstring: 0xd00
+  __TEXT.__unwind_info: 0x4b0
+  __DATA_CONST.__auth_got: 0x338
+  __DATA_CONST.__got: 0x248
+  __DATA_CONST.__const: 0x598
+  __DATA_CONST.__cfstring: 0xd20
   __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__objc_superrefs: 0x78
   __DATA_CONST.__objc_intobj: 0x18
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x46f0
+  __DATA.__objc_const: 0x4750
   __DATA.__objc_selrefs: 0xd18
-  __DATA.__objc_ivar: 0x14c
+  __DATA.__objc_ivar: 0x154
   __DATA.__objc_data: 0x820
   __DATA.__data: 0x5a0
-  __DATA.__bss: 0x98
+  __DATA.__bss: 0x60
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security

   - /System/Library/PrivateFrameworks/IDS.framework/IDS
   - /System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
+  - /System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry
   - /System/Library/PrivateFrameworks/Sharing.framework/Sharing
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7F9AA9B6-A2EC-31C3-943E-0130D1F11EA5
-  Functions: 410
-  Symbols:   188
-  CStrings:  1069
+  UUID: E761C14D-AF2C-32D1-827F-7F4E003A020E
+  Functions: 398
+  Symbols:   187
+  CStrings:  1067
 
Symbols:
+ _DeviceIdentityIssueClientCertificateWithCompletion
+ _NRDevicePropertyIsPaired
+ _OBJC_CLASS_$_NRDevice
+ _OBJC_CLASS_$_NRPairedDeviceRegistry
+ _os_variant_has_internal_content
- _MGGetBoolAnswer
- __sl_dlopen
- _abort_report_np
- _dlerror
- _dlsym
- _objc_getClass
CStrings:
+ "<%@: %p; displayDeviceIdentifier: %d; deviceIdentifier: %@; fullscreenPromptsEnabled: %d; allowCellularSizeThreshold: %lu; overrideDisplayBrightness: %d; requestedDisplayBrightness: %f; overrideTrueToneSettings: %d; requestedTrueToneSetting: %d;>"
+ "Failed to obtain device identity key, error: %@"
+ "TB,R,N,V_overrideTrueToneSettings"
+ "TB,R,N,V_requestedTrueToneSetting"
+ "_overrideTrueToneSettings"
+ "_requestedTrueToneSetting"
+ "com.apple.Diagnostics"
+ "overrideTrueToneSettings"
+ "requestedTrueToneSetting"
+ "v32@?0^{__SecKey=}8@\"NSArray\"16@\"NSError\"24"
+ "weakToStrongObjectsMapTable"
- "%s"
- "<%@: %p; displayDeviceIdentifier: %d; deviceIdentifier: %@; fullscreenPromptsEnabled: %d; allowCellularSizeThreshold: %lu; overrideDisplayBrightness: %d; requestedDisplayBrightness: %f>"
- "Cannot get attestation certificate because CoreRepairCore is not available on this device"
- "CoreRepairCore is unavailable. Falling back to attestation blob"
- "InternalBuild"
- "NRDevice"
- "NRDevicePropertyIsPaired"
- "NRPairedDeviceRegistry"
- "SFDevice"
- "Unable to find class %s"
- "bleDevice"
- "isEqualToSFDevice:"
- "mapTableWithWeakToStrongObjects"
- "softlink:o:path:/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore"
- "softlink:o:path:/System/Library/PrivateFrameworks/NanoRegistry.framework/NanoRegistry"
- "softlink:o:path:/System/Library/PrivateFrameworks/Sharing.framework/Sharing"

```
