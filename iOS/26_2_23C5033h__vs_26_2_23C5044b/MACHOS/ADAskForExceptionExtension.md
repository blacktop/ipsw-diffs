## ADAskForExceptionExtension

> `/System/Library/ExtensionKit/Extensions/ADAskForExceptionExtension.appex/ADAskForExceptionExtension`

```diff

-3.2.11.0.0
-  __TEXT.__text: 0x1eb44
-  __TEXT.__auth_stubs: 0x1510
+3.2.14.2.10
+  __TEXT.__text: 0x1de54
+  __TEXT.__auth_stubs: 0x1550
   __TEXT.__objc_stubs: 0x140
-  __TEXT.__objc_methlist: 0x58c
-  __TEXT.__const: 0xe34
-  __TEXT.__cstring: 0x119a
+  __TEXT.__objc_methlist: 0x4f4
+  __TEXT.__const: 0xb64
+  __TEXT.__cstring: 0x104a
   __TEXT.__gcc_except_tab: 0x5c
-  __TEXT.__objc_methname: 0x1593
-  __TEXT.__oslogstring: 0x830
-  __TEXT.__objc_classname: 0x128
-  __TEXT.__objc_methtype: 0x8b4
+  __TEXT.__objc_methname: 0x1433
+  __TEXT.__oslogstring: 0x8f3
+  __TEXT.__objc_classname: 0xd7
+  __TEXT.__objc_methtype: 0x7c3
   __TEXT.__dlopen_cstrs: 0x62
-  __TEXT.__constg_swiftt: 0x514
-  __TEXT.__swift5_typeref: 0x7d0
-  __TEXT.__swift5_fieldmd: 0x3d8
+  __TEXT.__constg_swiftt: 0x494
+  __TEXT.__swift5_typeref: 0x6ea
+  __TEXT.__swift5_fieldmd: 0x2c0
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_reflstr: 0xa4
-  __TEXT.__swift5_assocty: 0x100
-  __TEXT.__swift5_proto: 0x48
-  __TEXT.__swift5_types: 0x40
-  __TEXT.__swift5_capture: 0x1e4
-  __TEXT.__swift_as_entry: 0x3c
+  __TEXT.__swift5_reflstr: 0x64
+  __TEXT.__swift5_assocty: 0xc8
+  __TEXT.__swift5_proto: 0x38
+  __TEXT.__swift5_types: 0x30
+  __TEXT.__swift5_capture: 0x1c0
+  __TEXT.__swift_as_entry: 0x38
   __TEXT.__swift_as_ret: 0x44
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x6c0
-  __TEXT.__eh_frame: 0xb50
-  __DATA_CONST.__auth_got: 0xa98
-  __DATA_CONST.__got: 0x358
-  __DATA_CONST.__auth_ptr: 0x3c0
-  __DATA_CONST.__const: 0x9a8
-  __DATA_CONST.__objc_classlist: 0x48
-  __DATA_CONST.__objc_protolist: 0x88
+  __TEXT.__unwind_info: 0x650
+  __TEXT.__eh_frame: 0xb18
+  __DATA_CONST.__auth_got: 0xab8
+  __DATA_CONST.__got: 0x368
+  __DATA_CONST.__auth_ptr: 0x3b0
+  __DATA_CONST.__const: 0x780
+  __DATA_CONST.__objc_classlist: 0x40
+  __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x40
+  __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0xb80
-  __DATA.__objc_selrefs: 0x688
+  __DATA.__objc_const: 0xa40
+  __DATA.__objc_selrefs: 0x630
   __DATA.__objc_ivar: 0x8
-  __DATA.__objc_data: 0x730
-  __DATA.__data: 0xc88
-  __DATA.__bss: 0x970
-  __DATA.__common: 0x48
+  __DATA.__objc_data: 0x668
+  __DATA.__data: 0xb08
+  __DATA.__bss: 0x770
+  __DATA.__common: 0x50
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication
   - /System/Library/Frameworks/MarketplaceKit.framework/MarketplaceKit
-  - /System/Library/Frameworks/StoreKit.framework/StoreKit
   - /System/Library/Frameworks/SwiftUI.framework/SwiftUI
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/AppStoreComponents.framework/AppStoreComponents

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D283A1B8-9CFE-3C42-9ECE-67C77B4F8FBE
-  Functions: 483
-  Symbols:   236
-  CStrings:  429
+  UUID: 49F7EDD4-8D4F-38C0-80C0-5489153DBA6A
+  Functions: 430
+  Symbols:   234
+  CStrings:  404
 
Symbols:
- _OBJC_CLASS_$_SKStoreProductViewController
- _SKStoreProductParameterITunesItemIdentifier
CStrings:
+ "Primary button press is ignored, response has already been handled and there is no install progress being monitoring"
+ "Primary button pressed again, but can not pause/resume app install progress because app or progress not found"
+ "Primary button pressed again, pausing/resuming app install progress"
+ "[%@] Error handling App Store approval: %{public}@"
+ "[%@] Received an unknown ApprovalSheetResponse"
+ "responseHandled"
- "ADAskForExceptionExtension.ProductPageViewControllerWrapper"
- "ADAskForExceptionExtension/AppStoreApprovalSheet.swift"
- "SKStoreProductViewControllerDelegate"
- "SKStoreProductViewControllerDelegatePrivate"
- "[%@] Error fetching localized strings for product page: %{public}@"
- "[%@] Error loading product with parameters: %{public}s: %{public}@"
- "[%@] Product page view controller successfully loaded"
- "_TtCV26ADAskForExceptionExtension21AppStoreApprovalSheet32ProductPageViewControllerWrapper"
- "authContext"
- "initWithUnsignedLongLong:"
- "loadProductWithParameters:completionBlock:"
- "parameters"
- "productPageViewController"
- "productViewController:didFinishWithResult:"
- "productViewController:presentProductWithRequest:animated:"
- "productViewController:userDidInteractWithProduct:"
- "productViewControllerDidFinish:"
- "setAskToBuy:"
- "setCancelButtonTitle:"
- "setPromptString:"
- "setRightBarButtonTitle:"
- "setShowsRightBarButton:"
- "v20@?0B8@\"NSError\"12"
- "v24@0:8@\"SKStoreProductViewController\"16"
- "v32@0:8@\"SKStoreProductViewController\"16Q24"
- "v32@0:8@\"SKStoreProductViewController\"16q24"
- "v32@0:8@16Q24"
- "v32@0:8@16q24"
- "v36@0:8@\"SKStoreProductViewController\"16@\"SKStorePageRequest\"24B32"
- "v36@0:8@16@24B32"

```
