## SavageCameraInterface

> `/System/Library/PrivateFrameworks/SavageCameraInterface.framework/SavageCameraInterface`

```diff

-10.7.0.0.0
-  __TEXT.__text: 0x18fc
-  __TEXT.__auth_stubs: 0x200
+10.22.0.0.0
+  __TEXT.__text: 0x1bbc
+  __TEXT.__auth_stubs: 0x240
   __TEXT.__const: 0x50
-  __TEXT.__cstring: 0x318
-  __TEXT.__oslogstring: 0x2f2
-  __TEXT.__unwind_info: 0x80
+  __TEXT.__cstring: 0x379
+  __TEXT.__oslogstring: 0x322
+  __TEXT.__unwind_info: 0x8c
   __DATA_CONST.__got: 0x50
   __DATA_CONST.__const: 0x70
   __AUTH_CONST.__const: 0x20
   __AUTH_CONST.__cfstring: 0x20
   __AUTH_CONST.__auth_ptr: 0x10
-  __AUTH_CONST.__auth_got: 0x100
+  __AUTH_CONST.__auth_got: 0x120
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
-  Functions: 15
-  Symbols:   70
-  CStrings:  47
+  Functions: 17
+  Symbols:   75
+  CStrings:  50
 
Symbols:
+ _CFDataGetBytePtr
+ _CFDataGetLength
+ _CFStringGetCStringPtr
+ _SavageCamInterfacePublishToRegistry
+ _os_variant_is_recovery
+ _xpc_dictionary_set_string
- _IORegistryEntryFromPath
CStrings:
+ "%s: Interface to SavageCam not open, returning\n"
+ "H16ISPServicesRemoteIORegPropertyDataKey"
+ "H16ISPServicesRemoteIORegPropertyNameKey"
+ "SavageCamInterfacePublishToRegistry"
- "IODeviceTree:/chosen"

```
