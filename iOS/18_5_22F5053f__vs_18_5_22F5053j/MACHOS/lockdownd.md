## lockdownd

> `/usr/libexec/lockdownd`

```diff

-1329.120.9.502.2
+1329.120.12.0.0
   __TEXT.__text: 0x10b808
-  __TEXT.__auth_stubs: 0x2d40
+  __TEXT.__auth_stubs: 0x2d50
   __TEXT.__objc_stubs: 0x4400
   __TEXT.__objc_methlist: 0x3520
-  __TEXT.__cstring: 0x5092c
+  __TEXT.__cstring: 0x5098c
   __TEXT.__const: 0x161f0
   __TEXT.__oslogstring: 0x788
   __TEXT.__gcc_except_tab: 0x3d28

   __TEXT.__services: 0x2d8f
   __TEXT.__unwind_info: 0x3018
   __TEXT.__eh_frame: 0x10a0
-  __DATA_CONST.__auth_got: 0x16b8
+  __DATA_CONST.__auth_got: 0x16c0
   __DATA_CONST.__got: 0x680
   __DATA_CONST.__auth_ptr: 0x60
   __DATA_CONST.__const: 0xadd8
-  __DATA_CONST.__cfstring: 0x182c0
+  __DATA_CONST.__cfstring: 0x182e0
   __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x30

   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/PrivateFrameworks/AppSupport.framework/AppSupport
+  - /System/Library/PrivateFrameworks/AutomationMode.framework/AutomationMode
   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/Bom.framework/Bom

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
   Functions: 3465
-  Symbols:   931
-  CStrings:  9770
+  Symbols:   932
+  CStrings:  9772
 
Symbols:
+ _XAMIsAutomationModeEnabled
CStrings:
+ "Automation mode is enabled. Should not roll pair records."
+ "VinylRestore-78~7191"
+ "isPairingRecordSecurityRollingEnabled"
- "VinylRestore-78~7146"

```
