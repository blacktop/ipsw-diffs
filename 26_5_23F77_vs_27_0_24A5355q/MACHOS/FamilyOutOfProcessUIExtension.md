## FamilyOutOfProcessUIExtension

> `/System/Library/ExtensionKit/Extensions/FamilyOutOfProcessUIExtension.appex/FamilyOutOfProcessUIExtension`

```diff

-254.575.9.0.0
-  __TEXT.__text: 0x1f1bc
-  __TEXT.__auth_stubs: 0x1630
+279.3.1.2.0
+  __TEXT.__text: 0x1fa14
+  __TEXT.__auth_stubs: 0x1670
   __TEXT.__objc_stubs: 0xe60
   __TEXT.__objc_methlist: 0x718
-  __TEXT.__const: 0xfe8
-  __TEXT.__constg_swiftt: 0x700
-  __TEXT.__swift5_typeref: 0xb6b
   __TEXT.__objc_classname: 0x2ff
   __TEXT.__objc_methname: 0x1f0e
   __TEXT.__objc_methtype: 0xab7
-  __TEXT.__swift5_fieldmd: 0x53c
-  __TEXT.__cstring: 0xf67
+  __TEXT.__const: 0x1050
+  __TEXT.__constg_swiftt: 0x67c
+  __TEXT.__swift5_typeref: 0xbaf
+  __TEXT.__swift5_fieldmd: 0x548
+  __TEXT.__cstring: 0xd82
   __TEXT.__swift5_builtin: 0x28
-  __TEXT.__swift5_reflstr: 0x5ab
+  __TEXT.__swift5_reflstr: 0x62b
   __TEXT.__swift5_assocty: 0x148
   __TEXT.__swift5_proto: 0x6c
   __TEXT.__swift5_types: 0x54
-  __TEXT.__oslogstring: 0x437
-  __TEXT.__swift5_capture: 0x314
+  __TEXT.__oslogstring: 0x4c7
+  __TEXT.__swift5_capture: 0x418
   __TEXT.__swift_as_entry: 0x54
   __TEXT.__swift_as_ret: 0x78
+  __TEXT.__swift_as_cont: 0xf4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__unwind_info: 0x8f0
-  __TEXT.__eh_frame: 0x14a0
-  __DATA_CONST.__auth_got: 0xb20
-  __DATA_CONST.__got: 0x3d0
-  __DATA_CONST.__auth_ptr: 0x490
-  __DATA_CONST.__const: 0x9a0
+  __TEXT.__unwind_info: 0x8c0
+  __TEXT.__eh_frame: 0x1290
+  __DATA_CONST.__const: 0xc08
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x20
+  __DATA_CONST.__auth_got: 0xb40
+  __DATA_CONST.__got: 0x3a8
+  __DATA_CONST.__auth_ptr: 0x490
   __DATA.__objc_const: 0x1838
   __DATA.__objc_selrefs: 0x740
   __DATA.__objc_data: 0x810
-  __DATA.__data: 0xc50
-  __DATA.__bss: 0xdb8
+  __DATA.__data: 0xc70
+  __DATA.__bss: 0xd90
   __DATA.__common: 0x28
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftGLKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
-  - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftMetalKit.dylib
   - /usr/lib/swift/libswiftModelIO.dylib

   - /usr/lib/swift/libswiftSceneKit.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 68AF5AB3-E0E9-3B5F-8DA2-4E45C633C73B
-  Functions: 572
-  Symbols:   205
-  CStrings:  475
+  UUID: ECD79577-7EF2-35F5-96AE-5D17878D4832
+  Functions: 588
+  Symbols:   213
+  CStrings:  461
 
Symbols:
+ _objc_release_x9
+ _objc_retain_x28
+ _objc_retain_x4
+ _swift_release_n
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x28
+ _swift_release_x8
+ _swift_retain_x1
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_retain_x27
+ _swift_retain_x28
+ _swift_retain_x8
- ___stack_chk_fail
- ___stack_chk_guard
- __availability_version_check
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftMapKit
- __swift_FORCE_LOAD_$_swiftVideoToolbox
- _dispatch_once_f
- _dlsym
- _fclose
- _fopen
- _fread
- _free
- _fseek
- _ftell
- _malloc
- _objc_retain_x27
- _rewind
- _sscanf
- _swift_arrayDestroy
CStrings:
+ "Accessing Environment<%s>'s value outside of being installed on a View. This will always read the default value and will not update."
+ "AgeRangeAlertFlowStore"
- "%d.%d.%d"
- "/System/Library/CoreServices/SystemVersion.plist"
- "Accessing Environment's value outside of being installed on a View. This will always read the default value and will not update."
- "CFDataCreateWithBytesNoCopy"
- "CFDictionaryGetValue"
- "CFGetTypeID"
- "CFPropertyListCreateFromXMLData"
- "CFPropertyListCreateWithData"
- "CFRelease"
- "CFStringCreateWithCStringNoCopy"
- "CFStringGetCString"
- "CFStringGetTypeID"
- "ProductVersion"
- "View.task @ FamilyOutOfProcessUIExtension/FamilyOutOfProcessUIExtension.swift:"
- "kCFAllocatorNull"
- "r"

```
