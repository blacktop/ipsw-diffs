## TranslationAPIExtension

> `/System/Library/ExtensionKit/Extensions/TranslationAPIExtension.appex/Contents/MacOS/TranslationAPIExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_entry`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-385.0.0.0.0
-  __TEXT.__text: 0x23ee4
-  __TEXT.__auth_stubs: 0x1720
+389.0.0.0.0
+  __TEXT.__text: 0x23d84
+  __TEXT.__auth_stubs: 0x1730
   __TEXT.__objc_stubs: 0x5a0
   __TEXT.__objc_methlist: 0x1d4
   __TEXT.__const: 0x158c

   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x20
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x878
+  __TEXT.__unwind_info: 0x870
   __TEXT.__eh_frame: 0x5e0
   __DATA_CONST.__const: 0x980
   __DATA_CONST.__objc_classlist: 0x18

   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__auth_got: 0xb98
+  __DATA_CONST.__auth_got: 0xba0
   __DATA_CONST.__got: 0x3d8
   __DATA_CONST.__auth_ptr: 0x520
   __DATA.__objc_const: 0x5b8

   - /System/iOSSupport/System/Library/Frameworks/SwiftUI.framework/Versions/A/SwiftUI
   - /System/iOSSupport/System/Library/Frameworks/UIKit.framework/Versions/A/UIKit
   - /System/iOSSupport/System/Library/PrivateFrameworks/TranslationAPISupport.framework/Versions/A/TranslationAPISupport
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 713
-  Symbols:   184
+  Functions: 712
+  Symbols:   186
   CStrings:  182
 
Symbols:
+ _MobileGestalt_get_current_device
+ _MobileGestalt_get_deviceSupportsInstructionFollowingPruningModels
```
