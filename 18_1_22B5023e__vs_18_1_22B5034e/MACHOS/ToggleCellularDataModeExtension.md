## ToggleCellularDataModeExtension

> `/System/Library/ExtensionKit/Extensions/ToggleCellularDataModeExtension.appex/ToggleCellularDataModeExtension`

```diff

-12101.0.0.0.0
-  __TEXT.__text: 0x1648
-  __TEXT.__auth_stubs: 0x360
+12103.0.1.0.0
+  __TEXT.__text: 0x1fe4
+  __TEXT.__auth_stubs: 0x400
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__const: 0x2b4
-  __TEXT.__constg_swiftt: 0x178
-  __TEXT.__swift5_typeref: 0x1dc
+  __TEXT.__const: 0x2c4
+  __TEXT.__constg_swiftt: 0x198
+  __TEXT.__swift5_typeref: 0x3d8
   __TEXT.__swift5_fieldmd: 0x74
-  __TEXT.__swift5_reflstr: 0x39
-  __TEXT.__swift5_assocty: 0x68
+  __TEXT.__swift5_reflstr: 0x49
+  __TEXT.__swift5_assocty: 0x80
   __TEXT.__swift5_proto: 0x1c
   __TEXT.__swift5_types: 0x14
-  __TEXT.__cstring: 0x13f
-  __TEXT.__unwind_info: 0x108
-  __TEXT.__eh_frame: 0x68
-  __DATA_CONST.__auth_got: 0x1b0
-  __DATA_CONST.__got: 0x80
-  __DATA_CONST.__auth_ptr: 0x1a0
+  __TEXT.__cstring: 0x16f
+  __TEXT.__objc_methname: 0x2f
+  __TEXT.__unwind_info: 0x148
+  __TEXT.__eh_frame: 0x88
+  __DATA_CONST.__auth_got: 0x200
+  __DATA_CONST.__got: 0xa8
+  __DATA_CONST.__auth_ptr: 0x220
   __DATA_CONST.__const: 0x1a8
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x148
-  __DATA.__data: 0x208
+  __DATA.__objc_selrefs: 0x10
+  __DATA.__data: 0x288
   __DATA.__bss: 0x380
   __DATA.__common: 0x18
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/WidgetKit.framework/WidgetKit
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 61
-  Symbols:   62
-  CStrings:  6
+  Functions: 70
+  Symbols:   72
+  CStrings:  9
 
Symbols:
+ _free
+ _objc_retainAutoreleasedReturnValue
+ _swift_retain
+ _objc_release_x26
+ __CTServerConnectionGetCellularDataSettings
+ _objc_release_x19
+ _malloc
+ _MCFeatureAppCellularDataModificationAllowed
+ _objc_msgSend
+ _swift_release
+ _OBJC_CLASS_$_MCProfileConnection
- _objc_release_x27
CStrings:
+ "The state of cellular data enabled"
+ "effectiveBoolValueForSetting:"
+ "sharedConnection"

```
