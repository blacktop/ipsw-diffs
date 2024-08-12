## BackgroundShortcutRunner

> `/System/Library/PrivateFrameworks/WorkflowKit.framework/XPCServices/BackgroundShortcutRunner.xpc/BackgroundShortcutRunner`

```diff

-3032.0.7.1.0
-  __TEXT.__text: 0x5b874
-  __TEXT.__auth_stubs: 0x1ec0
+3100.0.1.0.0
+  __TEXT.__text: 0x5bcd4
+  __TEXT.__auth_stubs: 0x1f20
   __TEXT.__objc_stubs: 0xce0
   __TEXT.__objc_methlist: 0x290
-  __TEXT.__const: 0xc48
-  __TEXT.__cstring: 0x13fb
-  __TEXT.__constg_swiftt: 0x4e8
-  __TEXT.__swift5_typeref: 0xab3
+  __TEXT.__const: 0xac0
+  __TEXT.__cstring: 0x13bb
+  __TEXT.__constg_swiftt: 0x4bc
+  __TEXT.__swift5_typeref: 0xa63
   __TEXT.__swift5_reflstr: 0x3ee
-  __TEXT.__swift5_fieldmd: 0x430
-  __TEXT.__objc_methname: 0x1de9
-  __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_assocty: 0xd8
-  __TEXT.__swift5_proto: 0x9c
-  __TEXT.__swift5_types: 0x64
-  __TEXT.__swift5_capture: 0x434
-  __TEXT.__oslogstring: 0x577
+  __TEXT.__swift5_fieldmd: 0x414
+  __TEXT.__objc_methname: 0x1d64
+  __TEXT.__swift5_builtin: 0x8c
+  __TEXT.__swift5_assocty: 0xa8
+  __TEXT.__swift5_proto: 0x84
+  __TEXT.__swift5_types: 0x60
+  __TEXT.__swift5_capture: 0x474
+  __TEXT.__oslogstring: 0x567
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__swift5_protos: 0x4
   __TEXT.__objc_classname: 0x78
   __TEXT.__objc_methtype: 0x44c
-  __TEXT.__unwind_info: 0x1110
-  __TEXT.__eh_frame: 0x3480
-  __DATA_CONST.__auth_got: 0xf68
-  __DATA_CONST.__got: 0x9d0
-  __DATA_CONST.__auth_ptr: 0x318
-  __DATA_CONST.__const: 0x10f0
+  __TEXT.__unwind_info: 0x1100
+  __TEXT.__eh_frame: 0x33a8
+  __DATA_CONST.__auth_got: 0xf98
+  __DATA_CONST.__got: 0x9f0
+  __DATA_CONST.__auth_ptr: 0x310
+  __DATA_CONST.__const: 0x11b0
   __DATA_CONST.__cfstring: 0x3c0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8

   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA.__objc_const: 0xe78
-  __DATA.__objc_selrefs: 0x7b0
+  __DATA.__objc_selrefs: 0x778
   __DATA.__objc_data: 0x3b0
-  __DATA.__data: 0x10f8
-  __DATA.__bss: 0x1280
+  __DATA.__data: 0x10a8
+  __DATA.__bss: 0xf80
   __DATA.__common: 0x10
   - /System/Library/Frameworks/CoreData.framework/CoreData
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAVFoundation.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1700
-  Symbols:   302
-  CStrings:  525
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 1723
+  Symbols:   307
+  CStrings:  517
 
Symbols:
+ _OBJC_CLASS_$_WFLinkEntityAction
+ _OBJC_CLASS_$_WFLinkSearchAction
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _swift_dynamicCastClass
+ _swift_isClassType
- _OBJC_CLASS_$_WFDeviceAttributeIdiomRequirement
- _OBJC_CLASS_$_WFDeviceAttributesResource
- _OBJC_CLASS_$_WFDeviceCapabilityResource
- _WFLocalizedDisplayNameResourceForContentCategory
- _swift_taskGroup_destroy
- _swift_taskGroup_initialize
- _swift_taskGroup_initializeWithFlags
- _swift_unexpectedError
CStrings:
+ "Failed to index primitive: %!s(MISSING): %!@(MISSING)"
+ "localizedCategoryWithContext:"
- "Failed to index category %!@(MISSING) for action: %!s(MISSING) (%!l(MISSING)ld) in locale: %!s(MISSING)"
- "_Concurrency/DiscardingTaskGroup.swift"
- "categories"
- "idiom"
- "isEqual"
- "isFeatureFlagBasedCapability"
- "isMobileGestaltBasedCapability"
- "localizedSubcategoryForCategory:withContext:"
- "requiredDeviceIdioms"
- "valueAsBool"

```
