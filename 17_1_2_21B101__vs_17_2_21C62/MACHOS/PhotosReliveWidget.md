## PhotosReliveWidget

> `/Applications/MobileSlideShow.app/PlugIns/PhotosReliveWidget.appex/PhotosReliveWidget`

```diff

-612.0.160.0.0
-  __TEXT.__text: 0x255b4
-  __TEXT.__auth_stubs: 0x1540
+622.0.130.0.0
+  __TEXT.__text: 0x25b18
+  __TEXT.__auth_stubs: 0x1560
   __TEXT.__objc_methlist: 0x16c
   __TEXT.__const: 0x1704
-  __TEXT.__swift5_typeref: 0x3892
-  __TEXT.__objc_methname: 0xa8f
+  __TEXT.__swift5_typeref: 0x387e
   __TEXT.__constg_swiftt: 0xa3c
-  __TEXT.__swift5_fieldmd: 0x5cc
+  __TEXT.__swift5_fieldmd: 0x5c0
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x350
+  __TEXT.__swift5_reflstr: 0x370
   __TEXT.__swift5_assocty: 0x260
   __TEXT.__swift5_capture: 0x15c
-  __TEXT.__cstring: 0x1987
+  __TEXT.__cstring: 0x1a87
+  __TEXT.__objc_methname: 0xb0d
   __TEXT.__swift5_protos: 0x10
   __TEXT.__swift5_proto: 0x100
   __TEXT.__swift5_types: 0xa0
   __TEXT.__swift5_entry: 0x8
   __TEXT.__objc_classname: 0x9
   __TEXT.__objc_methtype: 0xad
-  __TEXT.__unwind_info: 0x870
-  __TEXT.__eh_frame: 0x164
-  __DATA_CONST.__auth_got: 0xaa0
+  __TEXT.__unwind_info: 0x880
+  __TEXT.__eh_frame: 0x194
+  __DATA_CONST.__auth_got: 0xab0
   __DATA_CONST.__got: 0x380
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x1520
+  __DATA_CONST.__const: 0x1510
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x838
-  __DATA.__objc_selrefs: 0x298
+  __DATA.__objc_selrefs: 0x2b0
   __DATA.__objc_protorefs: 0x10
-  __DATA.__objc_classrefs: 0x98
+  __DATA.__objc_classrefs: 0xa8
   __DATA.__objc_data: 0x578
-  __DATA.__data: 0x1190
+  __DATA.__data: 0x1188
   __DATA.__bss: 0x1e78
   __DATA.__common: 0x98
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CoreText.framework/CoreText
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Intents.framework/Intents

   - /System/Library/PrivateFrameworks/PhotoLibraryServicesCore.framework/PhotoLibraryServicesCore
   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore
+  - /System/Library/PrivateFrameworks/PrivacyDisclosureCore.framework/PrivacyDisclosureCore
   - /System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 88DE0972-B1E3-3BCB-98B9-DBAF86CE543A
-  Functions: 1006
-  Symbols:   209
-  CStrings:  251
+  UUID: 2E76BEE0-9ACD-367C-BD17-CD24A4166543
+  Functions: 1012
+  Symbols:   212
+  CStrings:  259
 
Symbols:
+ _OBJC_CLASS_$_LSApplicationRecord
+ _OBJC_CLASS_$_PDCPreflightManager
+ _swift_willThrow
CStrings:
+ "Cannot access application record for Photos error %s"
+ "Photos requires privacy disclosure"
+ "com.apple.mobileslideshow"
+ "initWithBundleIdentifier:allowPlaceholder:error:"
+ "initWithTargetQueue:"
+ "isPreflightFeatureEnabled"
+ "privacyDisclosure"
+ "privacyDisclosureEntryForContentType:"
+ "requiresPreflightForApplicationRecord:"
+ "should not be accessing photoLibrary when role is privacyDisclosure"
- "initWithPhotoLibraryURL:"
- "systemPhotoLibraryURL"

```
