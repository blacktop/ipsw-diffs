## AppleSPUAccCompassPlugin

> `/System/Library/HIDPlugins/AppleSPUAccCompassPlugin.plugin/AppleSPUAccCompassPlugin`

```diff

-1014.120.3.0.0
-  __TEXT.__text: 0x1a20
-  __TEXT.__auth_stubs: 0x340
+1046.0.1.0.0
+  __TEXT.__text: 0x15bc
+  __TEXT.__auth_stubs: 0x2e0
   __TEXT.__gcc_except_tab: 0x20
-  __TEXT.__const: 0x68
-  __TEXT.__cstring: 0xf0
-  __TEXT.__oslogstring: 0x282
-  __TEXT.__unwind_info: 0x108
-  __TEXT.__objc_methname: 0x2d
-  __TEXT.__objc_stubs: 0x40
+  __TEXT.__const: 0x28
+  __TEXT.__cstring: 0x7c
+  __TEXT.__oslogstring: 0x17c
+  __TEXT.__unwind_info: 0xf8
   __DATA_CONST.__got: 0x38
   __DATA_CONST.__const: 0x20
-  __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x1b0
+  __AUTH_CONST.__auth_got: 0x178
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x100
   __AUTH.__data: 0x78
   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
-  - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  - /usr/lib/libobjc.A.dylib
-  UUID: BE5C4A6E-E92A-3F1E-B726-60C6C1C47921
-  Functions: 46
-  Symbols:   95
-  CStrings:  42
+  UUID: 7A76F040-4CC4-3796-BB07-A8CC6518A7C2
+  Functions: 42
+  Symbols:   85
+  CStrings:  29
 
Symbols:
+ _CFAllocatorAllocateTyped
+ _kIOMainPortDefault
- _CFAllocatorAllocate
- _MGGetProductType
- __ZN24AppleSPUAccCompassPlugin21checkForBatteryRepairEP14ServiceContext
- __getBatteryChemID
- __hadHadAuthorizedBatteryRepair
- _dlclose
- _dlopen
- _dlsym
- _kIOMasterPortDefault
- _objc_claimAutoreleasedReturnValue
- _objc_msgSend
- _objc_release_x19
CStrings:
- "/System/Library/PrivateFrameworks/CoreRepairKit.framework/CoreRepairKit"
- "Authorized battery repair check returned False!"
- "Authorized battery repair check returned True!"
- "Detected N84!"
- "Error updating CBCC values!"
- "Got chemID 0x%x"
- "Murata batteries detected"
- "Neither Murata nor ATL/SDI batteries found, ignoring..."
- "OBJC_CLASS_$_CRRepairStatus"
- "SDI/ATL batteries detected"
- "getDeviceChemID"
- "hasHadAuthorizedRepairForComponent:"
- "intValue"

```
