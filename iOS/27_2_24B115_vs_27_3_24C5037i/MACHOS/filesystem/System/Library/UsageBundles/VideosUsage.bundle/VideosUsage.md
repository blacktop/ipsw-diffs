## VideosUsage

> `/System/Library/UsageBundles/VideosUsage.bundle/VideosUsage`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1145.11.2.0.0
-  __TEXT.__text: 0x5d68
-  __TEXT.__auth_stubs: 0x420
-  __TEXT.__objc_stubs: 0x17e0
+1145.20.7.0.2
+  __TEXT.__text: 0x5d78
+  __TEXT.__auth_stubs: 0x410
+  __TEXT.__objc_stubs: 0x1800
   __TEXT.__objc_methlist: 0x8c0
   __TEXT.__const: 0x10
-  __TEXT.__objc_methname: 0x1ba8
+  __TEXT.__objc_methname: 0x1bbe
   __TEXT.__cstring: 0x36c
   __TEXT.__objc_classname: 0xe7
   __TEXT.__objc_methtype: 0x40e

   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
-  __DATA_CONST.__auth_got: 0x220
-  __DATA_CONST.__got: 0x1c0
+  __DATA_CONST.__auth_got: 0x218
+  __DATA_CONST.__got: 0x1c8
   __DATA.__objc_const: 0x1208
-  __DATA.__objc_selrefs: 0x858
+  __DATA.__objc_selrefs: 0x860
   __DATA.__objc_ivar: 0x88
   __DATA.__objc_data: 0x230
   __DATA.__data: 0x120

   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaPlayerUI.framework/MediaPlayerUI
   - /System/Library/PrivateFrameworks/Preferences.framework/Preferences
-  - /System/Library/PrivateFrameworks/WatchListKit.framework/WatchListKit
+  - /System/Library/PrivateFrameworks/VideosUICore.framework/VideosUICore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 168
   Symbols:   140
-  CStrings:  433
+  CStrings:  434
 
Symbols:
+ _OBJC_CLASS_$_VUIDevice
- _WLKIsRegulatedSKU
Functions:
~ sub_2114 : 840 -> 848
~ sub_24c0 -> sub_24c8 : 204 -> 212
CStrings:
+ "isBuiltForChinaMarket"
```
