## SideButtonSettings

> `/System/Library/Settings/SideButtonSettings.settings/SideButtonSettings`

```diff

-3510.7.2.11.6
-  __TEXT.__text: 0xd61c
-  __TEXT.__auth_stubs: 0xb50
-  __TEXT.__objc_methlist: 0x14c
-  __TEXT.__const: 0x650
-  __TEXT.__objc_methname: 0x42c
-  __TEXT.__cstring: 0x715
-  __TEXT.__constg_swiftt: 0x3c8
-  __TEXT.__swift5_typeref: 0xcc1
-  __TEXT.__swift5_reflstr: 0x15b
+3515.8.1.0.0
+  __TEXT.__text: 0xefcc
+  __TEXT.__auth_stubs: 0xba0
+  __TEXT.__objc_methlist: 0x19c
+  __TEXT.__const: 0x710
+  __TEXT.__objc_methname: 0x4cc
+  __TEXT.__cstring: 0x8c5
+  __TEXT.__constg_swiftt: 0x464
+  __TEXT.__swift5_typeref: 0xe6b
+  __TEXT.__swift5_reflstr: 0x1af
   __TEXT.__swift5_assocty: 0x78
-  __TEXT.__swift5_fieldmd: 0x128
+  __TEXT.__swift5_fieldmd: 0x168
   __TEXT.__swift5_proto: 0x1c
-  __TEXT.__swift5_types: 0x14
-  __TEXT.__swift5_capture: 0x10c
+  __TEXT.__swift5_types: 0x18
+  __TEXT.__swift5_capture: 0x17c
   __TEXT.__swift_as_entry: 0x10
-  __TEXT.__objc_classname: 0x28
-  __TEXT.__objc_methtype: 0xb5
+  __TEXT.__objc_classname: 0x3b
+  __TEXT.__objc_methtype: 0xd7
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__unwind_info: 0x3e0
-  __TEXT.__eh_frame: 0x3bc
-  __DATA_CONST.__auth_got: 0x5a8
-  __DATA_CONST.__got: 0x200
-  __DATA_CONST.__auth_ptr: 0x280
-  __DATA_CONST.__const: 0x590
-  __DATA_CONST.__objc_classlist: 0x18
-  __DATA_CONST.__objc_protolist: 0x20
+  __TEXT.__unwind_info: 0x460
+  __TEXT.__eh_frame: 0x3ec
+  __DATA_CONST.__auth_got: 0x5d0
+  __DATA_CONST.__got: 0x240
+  __DATA_CONST.__auth_ptr: 0x2a8
+  __DATA_CONST.__const: 0x720
+  __DATA_CONST.__objc_classlist: 0x20
+  __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x10
-  __DATA.__objc_const: 0x480
-  __DATA.__objc_selrefs: 0x1c8
-  __DATA.__objc_data: 0x298
-  __DATA.__data: 0x568
-  __DATA.__bss: 0x3f0
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA.__objc_const: 0x590
+  __DATA.__objc_selrefs: 0x1f8
+  __DATA.__objc_data: 0x3d0
+  __DATA.__data: 0x650
+  __DATA.__bss: 0x410
   __DATA.__common: 0x18
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AssistantServices.framework/AssistantServices
+  - /System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/Settings.framework/Settings
   - /System/Library/PrivateFrameworks/SystemVoiceAssistantServices.framework/SystemVoiceAssistantServices
   - /System/Library/PrivateFrameworks/_IconServices_SwiftUI.framework/_IconServices_SwiftUI
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 71F50EDF-8116-3BE8-932F-423DAD4EF8D6
-  Functions: 300
-  Symbols:   134
-  CStrings:  136
+  UUID: 3D86CCEB-6CCA-3FDB-B881-764E57896CD8
+  Functions: 352
+  Symbols:   143
+  CStrings:  155
 
Symbols:
+ _MobileGestalt_get_current_device
+ _MobileGestalt_get_pearlIDCapability
+ _MobileGestalt_get_touchIDCapability
+ _OBJC_CLASS_$_BKDevice
+ _OBJC_CLASS_$_BKDeviceDescriptor
+ _OBJC_CLASS_$_BKIdentity
+ _OBJC_CLASS_$_LSObserver
+ _objc_retain_x26
+ _objc_retain_x27
CStrings:
+ "LSObserverDelegate"
+ "Subtitle used in Side Button apps list when the app is marked as potentially dangerous"
+ "Subtitle used in Side Button apps list when the app is unavailable"
+ "Unavailable because it requires Touch ID"
+ "Unavailable because it requires a passcode"
+ "_TtC18SideButtonSettings20SideButtonLSObserver"
+ "_datasetIdentifier"
+ "callback"
+ "deviceDescriptorForType:"
+ "deviceWithDescriptor:error:"
+ "identitiesWithError:"
+ "lsObserver"
+ "lsObserverDelegate"
+ "observerDidObserveDatabaseChange:"
+ "startObserving"
+ "updateSystemAssistantPreferenceModel"
+ "v24@0:8@\"LSObserver\"16"
+ "v24@0:8@16"

```
