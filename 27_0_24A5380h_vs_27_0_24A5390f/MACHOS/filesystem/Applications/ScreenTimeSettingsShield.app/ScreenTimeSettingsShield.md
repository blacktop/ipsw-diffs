## ScreenTimeSettingsShield

> `/Applications/ScreenTimeSettingsShield.app/ScreenTimeSettingsShield`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__cstring`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_entry`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_data`

```diff

-87.1.101.0.0
-  __TEXT.__text: 0x17574
-  __TEXT.__auth_stubs: 0x14b0
-  __TEXT.__objc_stubs: 0x360
+91.1.0.0.0
+  __TEXT.__text: 0x1a1c8
+  __TEXT.__auth_stubs: 0x14e0
+  __TEXT.__objc_stubs: 0x3a0
   __TEXT.__objc_methlist: 0x6f0
-  __TEXT.__const: 0xb34
-  __TEXT.__constg_swiftt: 0x594
-  __TEXT.__swift5_typeref: 0xf6a
+  __TEXT.__const: 0xbf4
+  __TEXT.__constg_swiftt: 0x618
+  __TEXT.__swift5_typeref: 0x103e
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0x1f7
-  __TEXT.__swift5_fieldmd: 0x26c
+  __TEXT.__swift5_reflstr: 0x217
+  __TEXT.__swift5_fieldmd: 0x2a8
   __TEXT.__swift5_assocty: 0xe8
-  __TEXT.__swift5_capture: 0x110
+  __TEXT.__swift5_capture: 0x140
   __TEXT.__cstring: 0x52a
-  __TEXT.__swift5_proto: 0x38
+  __TEXT.__swift5_proto: 0x40
   __TEXT.__swift5_types: 0x48
-  __TEXT.__oslogstring: 0x624
+  __TEXT.__oslogstring: 0x914
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_classname: 0x238
-  __TEXT.__objc_methname: 0x15c7
+  __TEXT.__objc_methname: 0x1617
   __TEXT.__objc_methtype: 0xcc0
-  __TEXT.__swift_as_entry: 0x10
-  __TEXT.__swift_as_ret: 0x10
-  __TEXT.__swift_as_cont: 0x14
-  __TEXT.__unwind_info: 0x4a8
-  __TEXT.__eh_frame: 0x41c
-  __DATA_CONST.__const: 0x628
+  __TEXT.__swift5_protos: 0x8
+  __TEXT.__swift_as_entry: 0x18
+  __TEXT.__swift_as_ret: 0x18
+  __TEXT.__swift_as_cont: 0x28
+  __TEXT.__unwind_info: 0x510
+  __TEXT.__eh_frame: 0x5ac
+  __DATA_CONST.__const: 0x6c0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__auth_got: 0xa60
-  __DATA_CONST.__got: 0x2a8
-  __DATA_CONST.__auth_ptr: 0x3f8
-  __DATA.__objc_const: 0x970
-  __DATA.__objc_selrefs: 0x4b8
+  __DATA_CONST.__auth_got: 0xa78
+  __DATA_CONST.__got: 0x2d0
+  __DATA_CONST.__auth_ptr: 0x410
+  __DATA.__objc_const: 0x990
+  __DATA.__objc_selrefs: 0x4c8
   __DATA.__objc_data: 0x3a0
-  __DATA.__data: 0xb70
+  __DATA.__data: 0xba0
   __DATA.__bss: 0x770
   __DATA.__common: 0x18
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AppRestrictionsCore.framework/AppRestrictionsCore

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 370
-  Symbols:   546
-  CStrings:  334
+  Functions: 398
+  Symbols:   554
+  CStrings:  347
 
Symbols:
+ _$s10Foundation3URLVSQAAMc
+ _$s10Foundation3URLVs23CustomStringConvertibleAAMc
+ _$s14MarketplaceKit14AppDistributorO18requestProductPage_6itemID07versionI0ySS_s6UInt64VAHSgtYaKFZ
+ _$s14MarketplaceKit14AppDistributorO18requestProductPage_6itemID07versionI0ySS_s6UInt64VAHSgtYaKFZTu
+ _$ss6UInt64VMn
+ _$syycWV
+ _objc_retain_x25
+ _swift_arrayDestroy
+ _swift_retain_x28
- _objc_retain_x28
CStrings:
+ "App is from distributor or web. No app store url: %{private}s"
+ "Cannot open in third party marketplace: distributor app is not installed"
+ "Cannot open in third party marketplace: fromDistributorOrWeb=%{bool,public}d, hasDistributorId=%{bool,public}d, hasBundleId=%{bool,public}d"
+ "Cannot open store page for %{private}s"
+ "Could not show product page for %{private}s: %{public}s"
+ "Could not show product page for record: %{private}s"
+ "Failed opening app store page for %{private}s,\nstoreUrl: %{public}s"
+ "Failed to load application record while opening Ask Permission flow: %{public}s"
+ "Invalid adamID for app: %{private}s"
+ "No application record to open"
+ "Opened third party product page for %{private}s"
+ "Opening app store page for %{private}s"
+ "Opening third party app details page for %{private}s"
+ "Requesting third party product page for %{private}s"
+ "applicationIsInstalled:"
+ "https://itunes.apple.com/app/id"
+ "isInstalledFromDistributorOrWeb"
+ "openInMarketplace"
- "Error fetching adamID for %s"
- "No App Store URL to open"
- "No adamID for %{public}s"
- "Unable to construct App Store URL for Adam identifier %{private}llu."
- "https://apps.apple.com/app/id"
```
