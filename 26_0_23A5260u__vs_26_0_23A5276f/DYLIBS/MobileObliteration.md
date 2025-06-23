## MobileObliteration

> `/System/Library/PrivateFrameworks/MobileObliteration.framework/MobileObliteration`

```diff

-346.0.0.0.0
-  __TEXT.__text: 0x700
-  __TEXT.__auth_stubs: 0x210
-  __TEXT.__cstring: 0x389
-  __TEXT.__const: 0x28
-  __TEXT.__oslogstring: 0x100
-  __TEXT.__unwind_info: 0x70
+350.0.0.0.0
+  __TEXT.__text: 0xb50
+  __TEXT.__auth_stubs: 0x280
+  __TEXT.__cstring: 0x3ec
+  __TEXT.__const: 0x30
+  __TEXT.__oslogstring: 0x205
+  __TEXT.__unwind_info: 0x78
   __TEXT.__objc_methname: 0x46
   __TEXT.__objc_stubs: 0x80
-  __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x128
+  __DATA_CONST.__got: 0x30
+  __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x20
-  __AUTH_CONST.__auth_got: 0x110
+  __AUTH_CONST.__auth_got: 0x148
   __AUTH_CONST.__const: 0x20
-  __AUTH_CONST.__cfstring: 0x400
+  __AUTH_CONST.__cfstring: 0x420
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/MobileSystemServices.framework/MobileSystemServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 680D163A-480A-3827-BE63-DE13A36F7B85
-  Functions: 12
-  Symbols:   112
-  CStrings:  81
+  UUID: 26380C8F-E857-3771-B215-D5F58FC0F94F
+  Functions: 20
+  Symbols:   137
+  CStrings:  93
 
Symbols:
+ _CFGetTypeID
+ _CFStringGetTypeID
+ _IOMainPort
+ _IOObjectRelease
+ _IORegistryEntryFromPath
+ _IORegistryEntrySetCFProperty
+ _OUTLINED_FUNCTION_2
+ _bootstrap_port
+ _kObliterationTypeMarkDirect
+ _objc_release_x21
+ _setOblitNVRAMKeyDirect
+ _setOblitNVRAMKeyDirect.cold.1
+ _setOblitNVRAMKeyDirect.cold.2
+ _setOblitNVRAMKeyDirect.cold.3
+ _setOblitNVRAMKeyDirect.cold.4
+ _setOblitNVRAMKeyDirect.cold.5
+ _setOblitNVRAMKeyDirect.cold.6
+ _snprintf
- _objc_release_x19
CStrings:
+ "%d"
+ "Could not create string for name or value"
+ "Could not get main port"
+ "Could not get options entry from the device tree"
+ "Could not save value:%08x"
+ "Error creating CFString for key IONVRAM-FORCESYNCNOW-PROPERTY"
+ "Failed setting the property IONVRAM-FORCESYNCNOW-PROPERTY"
+ "IODeviceTree:/options"
+ "IONVRAM-FORCESYNCNOW-PROPERTY"
+ "ObliterationTypeMarkDirect"
+ "oblit-inprogress"

```
