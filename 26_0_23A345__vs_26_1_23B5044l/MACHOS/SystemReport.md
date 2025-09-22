## SystemReport

> `/Applications/DiagnosticsService.app/PlugIns/SystemReport.appex/SystemReport`

```diff

-1066.2.1.0.0
-  __TEXT.__text: 0x3c004
-  __TEXT.__auth_stubs: 0xd20
-  __TEXT.__objc_stubs: 0x4500
-  __TEXT.__objc_methlist: 0x1c54
-  __TEXT.__cstring: 0x417d4
+1066.40.34.0.0
+  __TEXT.__text: 0x3bcfc
+  __TEXT.__auth_stubs: 0xd10
+  __TEXT.__objc_stubs: 0x4460
+  __TEXT.__objc_methlist: 0x1bf4
+  __TEXT.__cstring: 0x416c6
   __TEXT.__const: 0x98
-  __TEXT.__oslogstring: 0x2050
-  __TEXT.__objc_methname: 0x3875
-  __TEXT.__objc_classname: 0x62b
-  __TEXT.__objc_methtype: 0x5d5
+  __TEXT.__oslogstring: 0x20ae
+  __TEXT.__objc_methname: 0x37cc
+  __TEXT.__objc_classname: 0x61d
+  __TEXT.__objc_methtype: 0x5ca
   __TEXT.__gcc_except_tab: 0x288
-  __TEXT.__unwind_info: 0x6d8
-  __DATA_CONST.__auth_got: 0x6a0
-  __DATA_CONST.__got: 0x2b0
+  __TEXT.__unwind_info: 0x6c0
+  __DATA_CONST.__auth_got: 0x698
+  __DATA_CONST.__got: 0x2b8
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x550
-  __DATA_CONST.__cfstring: 0x24ec0
-  __DATA_CONST.__objc_classlist: 0x228
+  __DATA_CONST.__const: 0x4d0
+  __DATA_CONST.__cfstring: 0x24e00
+  __DATA_CONST.__objc_classlist: 0x220
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8

   __DATA_CONST.__objc_arrayobj: 0x3c0
   __DATA_CONST.__objc_intobj: 0x690
   __DATA_CONST.__objc_dictobj: 0x168
-  __DATA.__objc_const: 0x3238
-  __DATA.__objc_selrefs: 0x1398
+  __DATA.__objc_const: 0x31a8
+  __DATA.__objc_selrefs: 0x1360
   __DATA.__objc_ivar: 0xbc
-  __DATA.__objc_data: 0x1590
+  __DATA.__objc_data: 0x1540
   __DATA.__data: 0x4a8
-  __DATA.__bss: 0xb8
+  __DATA.__bss: 0x90
   __DATA.__common: 0x20
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation

   - /System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/MobileInBoxUpdate
   - /System/Library/PrivateFrameworks/MobileSoftwareUpdate.framework/MobileSoftwareUpdate
   - /System/Library/PrivateFrameworks/MultitouchSupport.framework/MultitouchSupport
+  - /System/Library/PrivateFrameworks/NearField.framework/NearField
   - /System/Library/PrivateFrameworks/NearFieldAccessory.framework/NearFieldAccessory
   - /System/Library/PrivateFrameworks/PowerLog.framework/PowerLog
   - /System/Library/PrivateFrameworks/PowerUI.framework/PowerUI

   - /usr/lib/libTelephonyBasebandDynamic.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/updaters/libT200Updater.dylib
-  UUID: 6A41006D-0997-3368-8756-0DB2BDCBABDA
-  Functions: 697
-  Symbols:   345
-  CStrings:  13093
+  UUID: BABE3A2E-AD14-37B2-9BE1-62A5A92BF981
+  Functions: 686
+  Symbols:   344
+  CStrings:  13074
 
Symbols:
+ _OBJC_CLASS_$_NFSecureElement
- _OBJC_CLASS_$_DASoftLinking
- _dlopen
CStrings:
+ "-[ComponentSystemBase isInDiagnosticsMode]"
+ "BatteryManufacturingLockStatus"
+ "Error getting batteryManufacturingLockStatus: %@"
+ "Failed to get secure element serial with error %@"
+ "Near Field framework is not present at runtime."
+ "batteryManufacturingLockStatus"
+ "embeddedSecureElementWithError:"
- "#24@0:8@16"
- "-[ComponentSystem isInDiagnosticsMode]"
- "/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit"
- "/System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit"
- "/System/Library/PrivateFrameworks/NearField.framework/NearField"
- "/System/Library/PrivateFrameworks/NearFieldAccessory.framework/NearFieldAccessory"
- "Beta"
- "CRRepairStatus"
- "DASoftLinking"
- "NFSecureElement"
- "ReleaseType"
- "Repair data not available for this device, skipping."
- "biometricKitClass:"
- "coreRepairClass:"
- "embeddedSecureElement"
- "isBiometricKitFrameworkAvailable"
- "isCoreRepairFrameworkAvailable"
- "isNearFieldAccessoryFrameworkAvailable"
- "isNearFieldFrameworkAvailable"
- "nearFieldAccessoryClass:"
- "nearFieldClass:"

```
