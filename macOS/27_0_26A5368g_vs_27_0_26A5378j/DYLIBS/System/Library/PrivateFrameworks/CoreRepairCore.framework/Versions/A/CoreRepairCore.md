## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/Versions/A/CoreRepairCore`

```diff

-  __TEXT.__text: 0x77114
-  __TEXT.__objc_methlist: 0x3e24
+  __TEXT.__text: 0x78468
+  __TEXT.__objc_methlist: 0x405c
   __TEXT.__const: 0x866
-  __TEXT.__cstring: 0x593b
-  __TEXT.__oslogstring: 0x8ded
-  __TEXT.__gcc_except_tab: 0x1398
-  __TEXT.__unwind_info: 0x1178
+  __TEXT.__cstring: 0x5c0f
+  __TEXT.__oslogstring: 0x90e2
+  __TEXT.__gcc_except_tab: 0x1380
+  __TEXT.__unwind_info: 0x11b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1e0
-  __DATA_CONST.__objc_classlist: 0x270
+  __DATA_CONST.__objc_classlist: 0x288
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x60
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2598
+  __DATA_CONST.__objc_selrefs: 0x2680
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x178
+  __DATA_CONST.__objc_superrefs: 0x188
   __DATA_CONST.__objc_arraydata: 0x588
-  __DATA_CONST.__got: 0x4f0
-  __AUTH_CONST.__const: 0xdc0
-  __AUTH_CONST.__cfstring: 0x6a20
-  __AUTH_CONST.__objc_const: 0x59f0
+  __DATA_CONST.__got: 0x510
+  __AUTH_CONST.__const: 0xe20
+  __AUTH_CONST.__cfstring: 0x6c40
+  __AUTH_CONST.__objc_const: 0x5e18
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_dictobj: 0x190
   __AUTH_CONST.__objc_arrayobj: 0x438
-  __AUTH_CONST.__auth_got: 0xa48
-  __AUTH.__objc_data: 0xfa0
-  __DATA.__objc_ivar: 0x36c
-  __DATA.__data: 0x598
-  __DATA.__bss: 0xc8
+  __AUTH_CONST.__auth_got: 0xa40
+  __AUTH.__objc_data: 0x1090
+  __DATA.__objc_ivar: 0x390
+  __DATA.__data: 0x5f8
+  __DATA.__bss: 0x100
   __DATA.__common: 0x18
   __DATA_DIRTY.__objc_data: 0x8c0
-  __DATA_DIRTY.__bss: 0x148
+  __DATA_DIRTY.__bss: 0x180
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libauthinstall.dylib
   - /usr/lib/libimage4.dylib
   - /usr/lib/libobjc.A.dylib
-  - /usr/lib/updaters/libT200Updater.dylib
-  Functions: 2273
-  Symbols:   576
-  CStrings:  2964
+  Functions: 2325
+  Symbols:   577
+  CStrings:  3028
 
Sections:
~ __TEXT.__const : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ _CFStringGetCStringPtr
+ _OBJC_CLASS_$_CRBatteryUpdaterFactory
+ _OBJC_METACLASS_$_CRBatteryUpdaterFactory
+ _dlclose
- _T200UpdaterCopyFirmwareWithLogging
- _T200UpdaterCreateRequestWithLogging
- _isVeridianUpdateRequired
CStrings:
+ " NOT"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.q4Tq0M/Sources/Mesa/AppleBiometricServices/MesaFactoryC/MesaFactoryC.c"
+ "/usr/lib/updaters/libT200Updater.dylib"
+ "AppleGasGaugeUpdate"
+ "BC__getInfo"
+ "Battery FW update is%s required, error: %@"
+ "BatteryGetBoardIdFromDT is nil"
+ "BatteryUpdaterCopyFirmwareWithLogging is nil"
+ "BatteryUpdaterCreate is nil"
+ "BatteryUpdaterCreateRequestWithLogging is nil"
+ "BatteryUpdaterExecCommand is nil"
+ "BatteryUpdaterGetInfo failed with rc: %d"
+ "BatteryUpdaterGetInfo is nil"
+ "BatteryUpdaterIsDone is nil"
+ "BatteryUpdaterIsFWUpdateRequired is nil"
+ "Configuration"
+ "DNVDSector1"
+ "DNVDSector2"
+ "Failed to create shared instance for battery firmware updater"
+ "Failed to get version info for battery"
+ "Failed to load updater dylib"
+ "Failed to open T200 updater dylib"
+ "Failed to resolve GetBoardIdFromDT"
+ "Failed to resolve T200 symbols"
+ "Failed to resolve UpdaterCopyFirmwareWithLogging"
+ "Failed to resolve UpdaterCreateRequestWithLogging"
+ "Failed to resolve UpdaterExecCommand"
+ "Failed to resolve UpdaterIsDone"
+ "Failed to resolve isUpdateRequired"
+ "Firmware"
+ "Firmware update required: %d, system partition path %@"
+ "GetBoardIdFromDT failed, error: %d"
+ "Instantiating CRT200Updater"
+ "Missing updater context"
+ "Request created by battery updater: %@"
+ "Setting up updater with options: %@"
+ "T200"
+ "T200 dylib handle nil"
+ "T200GetBoardIdFromDT"
+ "T200Updater dylib not correctly loaded"
+ "T200UpdaterCopyFirmwareWithLogging"
+ "T200UpdaterCreate"
+ "T200UpdaterCreate failed"
+ "T200UpdaterCreateRequestWithLogging"
+ "T200UpdaterExecCommand"
+ "T200UpdaterGetInfo is not supported or missing arguments"
+ "T200UpdaterIsDone"
+ "Underlying battery controller is Veridian or Volchok"
+ "batteryFirmware"
+ "isVeridianUpdateRequired"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.actPQQ/Sources/Mesa/AppleBiometricServices/MesaFactoryC/MesaFactoryC.c"
- "isVeridianUpdateRequired :%@:%d"
- "veridianFirmware"

```
