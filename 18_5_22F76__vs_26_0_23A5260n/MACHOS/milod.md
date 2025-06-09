## milod

> `/usr/libexec/milod`

```diff

-27.0.28.0.7
-  __TEXT.__text: 0x210
-  __TEXT.__auth_stubs: 0x100
-  __TEXT.__objc_stubs: 0xe0
+27.0.60.0.7
+  __TEXT.__text: 0x11c
+  __TEXT.__auth_stubs: 0xb0
+  __TEXT.__objc_stubs: 0x60
   __TEXT.__oslogstring: 0xe
-  __TEXT.__cstring: 0xe6
-  __TEXT.__objc_methname: 0x9f
+  __TEXT.__cstring: 0x2c
+  __TEXT.__objc_methname: 0x16
   __TEXT.__unwind_info: 0x68
-  __DATA_CONST.__auth_got: 0x88
-  __DATA_CONST.__got: 0x28
-  __DATA_CONST.__const: 0x80
-  __DATA_CONST.__cfstring: 0x20
+  __DATA_CONST.__auth_got: 0x60
+  __DATA_CONST.__got: 0x10
+  __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x38
+  __DATA.__objc_selrefs: 0x18
   __DATA.__data: 0x10
-  __DATA.__bss: 0x8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon
   - /System/Library/PrivateFrameworks/MicroLocationUtilities.framework/MicroLocationUtilities
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 0EAF0A19-E256-3B87-85A3-069A2359CA59
+  UUID: 825110A3-70EB-3705-AD72-79E00089CEE5
   Functions: 3
-  Symbols:   26
-  CStrings:  17
+  Symbols:   17
+  CStrings:  7
 
Symbols:
+ _OBJC_CLASS_$_NSRunLoop
+ _OBJC_CLASS_$_ULLifeCycleManager
+ _objc_opt_new
+ _objc_release_x19
- _OBJC_CLASS_$_NSXPCListener
- _OBJC_CLASS_$_ULEnvironment
- _OBJC_CLASS_$_ULServer
- ___CFConstantStringClassReference
- __dispatch_main_q
- __xpc_event_key_name
- _dispatch_main
- _objc_alloc
- _objc_release_x21
- _objc_release_x8
- _strcmp
- _xpc_dictionary_get_string
- _xpc_set_event_stream_handler
Functions:
~ sub_100000990 -> sub_1000008f0 : 292 -> 196
~ sub_100000ab4 -> sub_1000009b4 : 168 -> 68
~ sub_100000b5c -> sub_1000009f8 : 68 -> 20
CStrings:
+ "mainRunLoop"
+ "run"
+ "start"
- "RTLocationsOfInterestDidClearNotification"
- "com.apple.Preferences.ResetPrivacyWarningsNotification"
- "com.apple.milod.xpc.service"
- "com.apple.notifyd.matching"
- "initWithEnvironment:"
- "initWithMachServiceName:"
- "locationsOfInterestDidClearNotification"
- "resetPrivacyWarningsNotification"
- "resume"
- "setDelegate:"
- "standardEnvironment"
- "v16@?0@\"NSObject<OS_xpc_object>\"8"

```
