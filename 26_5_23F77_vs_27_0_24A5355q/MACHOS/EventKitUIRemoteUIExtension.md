## EventKitUIRemoteUIExtension

> `/System/Library/ExtensionKit/Extensions/EventKitUIRemoteUIExtension.appex/EventKitUIRemoteUIExtension`

```diff

-1529.4.12.0.0
-  __TEXT.__text: 0x1a864
-  __TEXT.__auth_stubs: 0xe00
-  __TEXT.__objc_stubs: 0x1200
-  __TEXT.__objc_methlist: 0x918
-  __TEXT.__const: 0x1994
-  __TEXT.__objc_methname: 0x275f
-  __TEXT.__objc_methtype: 0xc49
-  __TEXT.__constg_swiftt: 0x1104
-  __TEXT.__swift5_typeref: 0xb60
-  __TEXT.__swift5_reflstr: 0xa8a
-  __TEXT.__swift5_fieldmd: 0x6e8
+1560.0.0.0.0
+  __TEXT.__text: 0x1a198
+  __TEXT.__auth_stubs: 0xf50
+  __TEXT.__objc_stubs: 0x12c0
+  __TEXT.__objc_methlist: 0x980
+  __TEXT.__const: 0x1974
+  __TEXT.__objc_methname: 0x299b
+  __TEXT.__objc_methtype: 0xc69
+  __TEXT.__constg_swiftt: 0x1124
+  __TEXT.__swift5_typeref: 0xb7e
+  __TEXT.__swift5_reflstr: 0xaaa
+  __TEXT.__swift5_fieldmd: 0x6f4
   __TEXT.__swift5_builtin: 0xdc
   __TEXT.__swift5_assocty: 0x2d8
-  __TEXT.__swift5_capture: 0x418
-  __TEXT.__cstring: 0x2780
+  __TEXT.__swift5_capture: 0x438
+  __TEXT.__cstring: 0x2850
   __TEXT.__oslogstring: 0x9fe
   __TEXT.__swift5_proto: 0xb8
   __TEXT.__swift5_types: 0x88
   __TEXT.__objc_classname: 0x6ab
   __TEXT.__swift5_entry: 0x8
   __TEXT.__swift5_protos: 0x8
-  __TEXT.__unwind_info: 0x680
+  __TEXT.__unwind_info: 0x678
   __TEXT.__eh_frame: 0x48
-  __DATA_CONST.__auth_got: 0x708
-  __DATA_CONST.__got: 0x1f0
-  __DATA_CONST.__auth_ptr: 0x340
-  __DATA_CONST.__const: 0x1410
+  __DATA_CONST.__const: 0x1480
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x190
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xc8
-  __DATA.__objc_const: 0x15a0
-  __DATA.__objc_selrefs: 0x790
+  __DATA_CONST.__auth_got: 0x7b0
+  __DATA_CONST.__got: 0x1e8
+  __DATA_CONST.__auth_ptr: 0x340
+  __DATA.__objc_const: 0x1600
+  __DATA.__objc_selrefs: 0x7f8
   __DATA.__objc_data: 0x5d8
-  __DATA.__data: 0x1c98
+  __DATA.__data: 0x1cb8
   __DATA.__bss: 0x1720
-  __DATA.__common: 0x58
+  __DATA.__common: 0x60
   - /System/Library/Frameworks/Combine.framework/Combine
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/EventKit.framework/EventKit

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib
-  - /usr/lib/swift/libswiftMapKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftMetalKit.dylib
+  - /usr/lib/swift/libswiftModelIO.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
-  - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 048D499A-4342-3319-A8D8-339AD28C219E
-  Functions: 660
-  Symbols:   171
-  CStrings:  590
+  UUID: FF082721-5230-3407-A885-027C87095E05
+  Functions: 654
+  Symbols:   191
+  CStrings:  607
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftMetalKit
+ __swift_FORCE_LOAD_$_swiftModelIO
+ _swift_release_x1
+ _swift_release_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x24
+ _swift_release_x25
+ _swift_release_x26
+ _swift_release_x8
+ _swift_retain_x1
+ _swift_retain_x19
+ _swift_retain_x2
+ _swift_retain_x20
+ _swift_retain_x21
+ _swift_retain_x22
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_retain_x26
+ _swift_retain_x27
+ _swift_retain_x28
- __swift_FORCE_LOAD_$_swiftCoreMedia
- __swift_FORCE_LOAD_$_swiftMapKit
- __swift_FORCE_LOAD_$_swiftVideoToolbox
CStrings:
+ "EKEventEditScene reportAConcern: The connection is nil"
+ "EKEventEditScene reportAConcern: remoteObjectProxy is nil or not of type EKEventEditViewHostInterface"
+ "cancelButtonTapped"
+ "eventViewController:didCompleteEditingWithAction:"
+ "eventViewControllerEditButtonShouldBeShownDidChange:"
+ "eventViewControllerEditingDoneButtonShouldBeEnabledDidChange:"
+ "eventViewControllerEditingModeDidChange:"
+ "eventViewControllerShouldHideEditingToolbar:"
+ "eventViewControllerShouldHideNavigationDetailsCancelButton:"
+ "eventViewControllerShouldHideNavigationEditButtons:"
+ "hasReportAConcernAction"
+ "onReportAConcernAction"
+ "reportAConcernButtonTapped"
+ "setDisableAutoFocus:"
+ "setReportAConcernAction:"
+ "title"
+ "updateDateIntervalImplicit:"

```
