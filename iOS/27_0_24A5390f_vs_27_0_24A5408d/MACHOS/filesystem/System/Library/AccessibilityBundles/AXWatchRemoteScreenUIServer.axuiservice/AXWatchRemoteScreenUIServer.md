## AXWatchRemoteScreenUIServer

> `/System/Library/AccessibilityBundles/AXWatchRemoteScreenUIServer.axuiservice/AXWatchRemoteScreenUIServer`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_types`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_got`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3237.1.0.0.0
-  __TEXT.__text: 0x2a60
+3240.3.0.0.0
+  __TEXT.__text: 0x2a94
   __TEXT.__auth_stubs: 0x610
-  __TEXT.__objc_stubs: 0x1a0
+  __TEXT.__objc_stubs: 0x1c0
   __TEXT.__objc_methlist: 0x3ac
   __TEXT.__const: 0xa8
   __TEXT.__objc_classname: 0xb6
-  __TEXT.__objc_methname: 0x915
+  __TEXT.__objc_methname: 0x975
   __TEXT.__objc_methtype: 0x417
   __TEXT.__constg_swiftt: 0x48
   __TEXT.__swift5_typeref: 0xa1
   __TEXT.__swift5_reflstr: 0x23
   __TEXT.__swift5_fieldmd: 0x28
-  __TEXT.__cstring: 0x13f
+  __TEXT.__cstring: 0x169
   __TEXT.__swift5_capture: 0x58
   __TEXT.__oslogstring: 0xac
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x138
+  __TEXT.__unwind_info: 0x140
   __TEXT.__eh_frame: 0x48
   __DATA_CONST.__const: 0x218
+  __DATA_CONST.__cfstring: 0x20
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__got: 0x80
   __DATA_CONST.__auth_ptr: 0x40
   __DATA.__objc_const: 0x478
-  __DATA.__objc_selrefs: 0x1f8
+  __DATA.__objc_selrefs: 0x200
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x168
   __DATA.__data: 0x180
   __DATA.__bss: 0x10
+  - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AXCoreUtilities.framework/AXCoreUtilities

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 72
-  Symbols:   111
-  CStrings:  135
+  Symbols:   112
+  CStrings:  137
 
Symbols:
+ ___CFConstantStringClassReference
Functions:
~ sub_16a8 -> sub_1758 : 184 -> 236
CStrings:
+ "addContentViewController:withUserInteractionEnabled:forService:forSceneClientIdentifier:context:userInterfaceStyle:forWindowScene:completion:"
+ "kAXTwiceRemoteScreenSceneClientIdentifier"
+ "setActiveSceneTrackingEnabled:forSceneClientIdentifier:"
- "addContentViewController:withUserInteractionEnabled:forService:context:userInterfaceStyle:completion:"
```
