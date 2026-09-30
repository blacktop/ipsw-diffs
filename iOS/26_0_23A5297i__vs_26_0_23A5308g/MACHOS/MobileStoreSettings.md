## MobileStoreSettings

> `/System/Library/PreferenceBundles/MobileStoreSettings.bundle/MobileStoreSettings`

```diff

-12.0.60.1.1
-  __TEXT.__text: 0x328fc
-  __TEXT.__auth_stubs: 0x1780
+12.0.66.0.0
+  __TEXT.__text: 0x36aa0
+  __TEXT.__auth_stubs: 0x18d0
   __TEXT.__objc_stubs: 0x600
-  __TEXT.__objc_methlist: 0x42c
-  __TEXT.__cstring: 0x1699
-  __TEXT.__const: 0x1738
-  __TEXT.__constg_swiftt: 0x9c8
-  __TEXT.__swift5_typeref: 0x3444
-  __TEXT.__swift5_fieldmd: 0x3d4
-  __TEXT.__swift5_reflstr: 0x64a
+  __TEXT.__objc_methlist: 0x464
+  __TEXT.__const: 0x1818
+  __TEXT.__cstring: 0x1759
+  __TEXT.__constg_swiftt: 0xa1c
+  __TEXT.__swift5_typeref: 0x3762
+  __TEXT.__swift5_reflstr: 0x6fa
+  __TEXT.__swift5_fieldmd: 0x438
   __TEXT.__swift5_assocty: 0x1c0
-  __TEXT.__swift5_proto: 0x5c
-  __TEXT.__swift5_types: 0x4c
+  __TEXT.__swift5_capture: 0x3ac
+  __TEXT.__oslogstring: 0x710
+  __TEXT.__swift5_proto: 0x60
+  __TEXT.__swift5_types: 0x50
+  __TEXT.__objc_classname: 0xaf
+  __TEXT.__objc_methname: 0x1307
+  __TEXT.__objc_methtype: 0x227
   __TEXT.__swift_as_entry: 0x54
-  __TEXT.__objc_methname: 0x1276
-  __TEXT.__swift5_capture: 0x310
-  __TEXT.__oslogstring: 0x2f0
-  __TEXT.__objc_classname: 0x97
-  __TEXT.__objc_methtype: 0x1ff
   __TEXT.__swift_as_ret: 0x4c
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xab8
-  __TEXT.__eh_frame: 0x116c
-  __DATA_CONST.__auth_got: 0xbc8
-  __DATA_CONST.__got: 0x540
-  __DATA_CONST.__auth_ptr: 0x5a8
-  __DATA_CONST.__const: 0xf00
+  __TEXT.__unwind_info: 0xb50
+  __TEXT.__eh_frame: 0x11cc
+  __DATA_CONST.__auth_got: 0xc70
+  __DATA_CONST.__got: 0x590
+  __DATA_CONST.__auth_ptr: 0x5e0
+  __DATA_CONST.__const: 0x1098
   __DATA_CONST.__cfstring: 0x120
-  __DATA_CONST.__objc_classlist: 0x40
-  __DATA_CONST.__objc_protolist: 0x38
+  __DATA_CONST.__objc_classlist: 0x48
+  __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA.__objc_const: 0xb00
-  __DATA.__objc_selrefs: 0x6a0
+  __DATA.__objc_const: 0xbd8
+  __DATA.__objc_selrefs: 0x6d0
   __DATA.__objc_ivar: 0x14
-  __DATA.__objc_data: 0x900
-  __DATA.__data: 0xe90
-  __DATA.__bss: 0xda8
+  __DATA.__objc_data: 0x950
+  __DATA.__data: 0x11b0
+  __DATA.__bss: 0xe38
   __DATA.__common: 0x38
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/Combine.framework/Combine

   - /System/Library/PrivateFrameworks/AppStoreDaemon.framework/AppStoreDaemon
   - /System/Library/PrivateFrameworks/AppleMediaServices.framework/AppleMediaServices
   - /System/Library/PrivateFrameworks/AppleMediaServicesKitInternal.framework/AppleMediaServicesKitInternal
+  - /System/Library/PrivateFrameworks/AuthKit.framework/AuthKit
+  - /System/Library/PrivateFrameworks/AuthKitUI.framework/AuthKitUI
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
   - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit

   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: EC3EE35E-6021-3D0F-97A9-1AAC939AF75C
-  Functions: 869
-  Symbols:   254
-  CStrings:  440
+  UUID: 2F065872-E4AC-3A24-836C-28E224BD3403
+  Functions: 933
+  Symbols:   256
+  CStrings:  478
 
Symbols:
+ _OBJC_CLASS_$_AKAppleIDAuthenticationController
+ _OBJC_CLASS_$_AKAppleIDAuthenticationUISurrogateContext
CStrings:
+ "@24@0:8@\"NSCoder\"16"
+ "About to authenticate using surrogate context"
+ "Attempted surrogate auth but got neither results nor error"
+ "Attempting to get current hosting controller"
+ "Can’t present AuthKit UI because no context ID is available"
+ "Can’t present AuthKit UI because no view controller is available"
+ "Could not create AuthKit context"
+ "Could not create AuthKit controller"
+ "Created AuthKit controller"
+ "Created AuthKit surrogate context: %@"
+ "Creating AuthKit controller"
+ "Creating AuthKit surrogate context with ID: %s"
+ "Failed to authenticate using surrogate context: %@"
+ "Finished AuthKit surrogate auth from onAppear"
+ "Finished AuthKit surrogate auth from onChange"
+ "Finishing AuthKit surrogate auth from onAppear"
+ "Finishing AuthKit surrogate auth from onChange"
+ "Got auth results: %s"
+ "Got hosting controller: %@"
+ "Got new AuthKit context ID: %s"
+ "NSCoding"
+ "NSSecureCoding"
+ "Parsed AuthKit context ID from URL: %s"
+ "Set view controller on context: %@"
+ "Started authentication using surrogate context"
+ "TB,R"
+ "_$observationRegistrar"
+ "_TtC19MobileStoreSettings19AuthKitContextIDBox"
+ "_authKitContextID"
+ "ak_redactedCopy"
+ "authKitContextID"
+ "authenticateWithContext:completion:"
+ "encodeWithCoder:"
+ "initWithSurrogateID:"
+ "setPresentingViewController:"
+ "supportsSecureCoding"
+ "v24@0:8@\"NSCoder\"16"
+ "v24@?0@\"NSDictionary\"8@\"NSError\"16"

```
