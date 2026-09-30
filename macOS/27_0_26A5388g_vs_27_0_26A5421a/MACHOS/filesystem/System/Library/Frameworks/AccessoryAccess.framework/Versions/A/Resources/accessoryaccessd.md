## accessoryaccessd

> `/System/Library/Frameworks/AccessoryAccess.framework/Versions/A/Resources/accessoryaccessd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__cfstring`

```diff

-308.0.0.0.0
-  __TEXT.__text: 0x37424
-  __TEXT.__auth_stubs: 0xe00
-  __TEXT.__objc_stubs: 0x240
-  __TEXT.__const: 0x3fe8
-  __TEXT.__gcc_except_tab: 0x418c
-  __TEXT.__cstring: 0xf5c
-  __TEXT.__oslogstring: 0xa8b
-  __TEXT.__objc_methname: 0x15c
-  __TEXT.__unwind_info: 0x14c8
-  __DATA_CONST.__const: 0xec8
+308.1.7.0.0
+  __TEXT.__text: 0x393f0
+  __TEXT.__auth_stubs: 0xdf0
+  __TEXT.__objc_stubs: 0x2a0
+  __TEXT.__const: 0x4158
+  __TEXT.__gcc_except_tab: 0x4458
+  __TEXT.__cstring: 0xf3d
+  __TEXT.__oslogstring: 0xb4b
+  __TEXT.__objc_methname: 0x1ae
+  __TEXT.__unwind_info: 0x15a0
+  __DATA_CONST.__const: 0x1030
   __DATA_CONST.__cfstring: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x710
-  __DATA_CONST.__got: 0x1f0
-  __DATA.__objc_selrefs: 0x90
+  __DATA_CONST.__auth_got: 0x708
+  __DATA_CONST.__got: 0x200
+  __DATA.__objc_selrefs: 0xa8
   __DATA.__crash_info: 0x148
   __DATA.__bss: 0x54
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/Frameworks/IOUSBHost.framework/Versions/A/IOUSBHost
   - /System/Library/Frameworks/Security.framework/Versions/A/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/Versions/A/SystemConfiguration
+  - /System/Library/PrivateFrameworks/SetupAssistantFramework.framework/Versions/A/SetupAssistantFramework
   - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 622
-  Symbols:   300
-  CStrings:  205
+  Functions: 652
+  Symbols:   301
+  CStrings:  210
 
Symbols:
+ _OBJC_CLASS_$_SAUserSetupState
+ _kCGSSessionUserIDKey
- _os_release
CStrings:
+ "Client (pid: %{private, mask.hash}d, session: %{private, mask.hash}d) is not on console (session: %{private, mask.hash}d)"
+ "Could not get responsible audit token for pid %{private, mask.hash}d."
+ "SetupUserMonitor"
+ "getSetupStateForUser:"
+ "notifyWhenUserIsSetup:withCompletionBlock:"
+ "unsignedIntValue"
- "com.apple.accessoryaccessd.usb-device-connected"
```
