## CoreRepairCore

> `/System/Library/PrivateFrameworks/CoreRepairCore.framework/CoreRepairCore`

```diff

-  __TEXT.__text: 0x8b738
-  __TEXT.__objc_methlist: 0x45ac
+  __TEXT.__text: 0x8ca88
+  __TEXT.__objc_methlist: 0x47d4
   __TEXT.__const: 0x858
-  __TEXT.__cstring: 0x6ff8
-  __TEXT.__oslogstring: 0x9a50
+  __TEXT.__cstring: 0x72cc
+  __TEXT.__oslogstring: 0x9d45
   __TEXT.__gcc_except_tab: 0x171c
-  __TEXT.__unwind_info: 0x1420
+  __TEXT.__unwind_info: 0x1458
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0xaa0
-  __DATA_CONST.__objc_classlist: 0x318
+  __DATA_CONST.__objc_classlist: 0x330
   __DATA_CONST.__objc_catlist: 0x28
-  __DATA_CONST.__objc_protolist: 0x68
+  __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x25c0
+  __DATA_CONST.__objc_selrefs: 0x26a0
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x1d8
+  __DATA_CONST.__objc_superrefs: 0x1e8
   __DATA_CONST.__objc_arraydata: 0xb68
-  __DATA_CONST.__got: 0x5d0
-  __AUTH_CONST.__const: 0x540
-  __AUTH_CONST.__cfstring: 0x84c0
-  __AUTH_CONST.__objc_const: 0x64e8
+  __DATA_CONST.__got: 0x660
+  __AUTH_CONST.__const: 0x5a0
+  __AUTH_CONST.__cfstring: 0x86e0
+  __AUTH_CONST.__objc_const: 0x6910
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_dictobj: 0x1e0
   __AUTH_CONST.__objc_arrayobj: 0x8b8
-  __AUTH_CONST.__auth_got: 0xbb8
-  __AUTH.__objc_data: 0x1180
-  __DATA.__objc_ivar: 0x358
-  __DATA.__data: 0x5f8
-  __DATA.__bss: 0xe8
+  __AUTH_CONST.__auth_got: 0xba8
+  __AUTH.__objc_data: 0x1220
+  __DATA.__objc_ivar: 0x37c
+  __DATA.__data: 0x658
+  __DATA.__bss: 0x120
   __DATA.__common: 0x28
-  __DATA_DIRTY.__objc_data: 0xd70
-  __DATA_DIRTY.__bss: 0x168
+  __DATA_DIRTY.__objc_data: 0xdc0
+  __DATA_DIRTY.__bss: 0x1a0
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/updaters/libSavageRestoreInfo_iOS.dylib
   - /usr/lib/updaters/libSavageUpdater_iOS.dylib
-  - /usr/lib/updaters/libT200Updater.dylib
-  Functions: 2517
+  Functions: 2568
   Symbols:   664
-  CStrings:  3542
+  CStrings:  3606
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
Symbols:
+ _OBJC_CLASS_$_CRBatteryUpdaterFactory
+ _OBJC_METACLASS_$_CRBatteryUpdaterFactory
+ _dlclose
- _T200UpdaterCopyFirmwareWithLogging
- _T200UpdaterCreateRequestWithLogging
- _isVeridianUpdateRequired
CStrings:
+ " NOT"
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
- "isVeridianUpdateRequired :%@:%d"
- "veridianFirmware"

```
