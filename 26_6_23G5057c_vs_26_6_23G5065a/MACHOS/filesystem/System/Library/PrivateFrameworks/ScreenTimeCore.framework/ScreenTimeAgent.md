## ScreenTimeAgent

> `/System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_doubleobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__bss`
- `__DATA.__common`

```diff

-  __TEXT.__text: 0x13624c
-  __TEXT.__auth_stubs: 0x2440
-  __TEXT.__objc_stubs: 0x12fe0
-  __TEXT.__objc_methlist: 0xa3b4
-  __TEXT.__const: 0x50a8
+  __TEXT.__text: 0x136f00
+  __TEXT.__auth_stubs: 0x2460
+  __TEXT.__objc_stubs: 0x13060
+  __TEXT.__objc_methlist: 0xa3ec
+  __TEXT.__const: 0x5118
   __TEXT.__gcc_except_tab: 0x22f4
-  __TEXT.__cstring: 0xac9e
-  __TEXT.__oslogstring: 0x14b70
-  __TEXT.__objc_methname: 0x1dda7
-  __TEXT.__objc_classname: 0x2d02
-  __TEXT.__objc_methtype: 0x5e62
-  __TEXT.__constg_swiftt: 0x35f0
-  __TEXT.__swift5_typeref: 0x2d52
+  __TEXT.__cstring: 0xacde
+  __TEXT.__oslogstring: 0x14c90
+  __TEXT.__objc_methname: 0x1de17
+  __TEXT.__objc_classname: 0x2d32
+  __TEXT.__objc_methtype: 0x5e72
+  __TEXT.__constg_swiftt: 0x364c
+  __TEXT.__swift5_typeref: 0x2d58
+  __TEXT.__swift5_fieldmd: 0x165c
   __TEXT.__swift5_builtin: 0x118
   __TEXT.__swift5_reflstr: 0x2129
-  __TEXT.__swift5_fieldmd: 0x164c
   __TEXT.__swift5_assocty: 0x2e8
   __TEXT.__swift5_proto: 0x288
-  __TEXT.__swift5_types: 0x190
+  __TEXT.__swift5_types: 0x198
   __TEXT.__swift5_capture: 0x2200
   __TEXT.__swift_as_entry: 0x264
   __TEXT.__swift_as_ret: 0x19c
   __TEXT.__swift5_protos: 0xc8
   __TEXT.__swift5_mpenum: 0x1c
-  __TEXT.__unwind_info: 0x4870
+  __TEXT.__unwind_info: 0x4888
   __TEXT.__eh_frame: 0x6240
-  __DATA_CONST.__auth_got: 0x1230
-  __DATA_CONST.__got: 0x13a8
-  __DATA_CONST.__auth_ptr: 0x6b8
-  __DATA_CONST.__const: 0x9d08
-  __DATA_CONST.__cfstring: 0x4ce0
-  __DATA_CONST.__objc_classlist: 0x6a8
+  __DATA_CONST.__auth_got: 0x1240
+  __DATA_CONST.__got: 0x13b0
+  __DATA_CONST.__auth_ptr: 0x6c0
+  __DATA_CONST.__const: 0x9d38
+  __DATA_CONST.__cfstring: 0x4d00
+  __DATA_CONST.__objc_classlist: 0x6b0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x510
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x90
   __DATA_CONST.__objc_arrayobj: 0x90
   __DATA_CONST.__objc_dictobj: 0xa0
-  __DATA.__objc_const: 0x1edc0
-  __DATA.__objc_selrefs: 0x5870
+  __DATA.__objc_const: 0x1ee08
+  __DATA.__objc_selrefs: 0x5890
   __DATA.__objc_ivar: 0x814
-  __DATA.__objc_data: 0x4de8
-  __DATA.__data: 0x7558
+  __DATA.__objc_data: 0x4e98
+  __DATA.__data: 0x75b8
   __DATA.__bss: 0x37c0
   __DATA.__common: 0xe8
   - /AppleInternal/Library/Frameworks/TapToRadarKit.framework/TapToRadarKit

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/ScreenTime.framework/ScreenTime
+  - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SystemConfiguration.framework/SystemConfiguration
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6295
-  Symbols:   1360
-  CStrings:  7363
+  Functions: 6305
+  Symbols:   1363
+  CStrings:  7374
 
Symbols:
+ _$sSo10CFErrorRefas5Error10FoundationMc
+ _SecTaskCopySigningIdentifier
+ _SecTaskCreateWithAuditToken
CStrings:
+ "Denying web history access: caller %{public}s is not authorized for web application %{public}s"
+ "Failed to create sec task"
+ "Failed to resolve signing record for web history caller: %{public}@"
+ "STWebHistoryAccessAuthorizer"
+ "Unable to determine caller bundle identifier, denying web history access"
+ "UnsupportedWebBrowserError"
+ "bundleForClass:"
+ "isConnection:authorizedForWebApplication:"
+ "localizedStringForKey:value:table:"
+ "supportedWebBrowserBundleIdentifiersForDeviceFamily:"
+ "webHistoryAccess"
```
