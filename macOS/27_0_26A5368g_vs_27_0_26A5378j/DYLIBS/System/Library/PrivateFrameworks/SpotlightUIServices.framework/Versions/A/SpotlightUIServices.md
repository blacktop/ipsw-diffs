## SpotlightUIServices

> `/System/Library/PrivateFrameworks/SpotlightUIServices.framework/Versions/A/SpotlightUIServices`

```diff

-  __TEXT.__text: 0x5e820
+  __TEXT.__text: 0x5f3a8
   __TEXT.__delay_helper: 0x114
-  __TEXT.__objc_methlist: 0x4c40
-  __TEXT.__const: 0xd14
-  __TEXT.__cstring: 0x2682
+  __TEXT.__objc_methlist: 0x4c70
+  __TEXT.__const: 0xd34
+  __TEXT.__cstring: 0x26b2
   __TEXT.__ustring: 0x40
-  __TEXT.__oslogstring: 0x80b
+  __TEXT.__oslogstring: 0x9db
   __TEXT.__gcc_except_tab: 0x32c
   __TEXT.__swift5_typeref: 0x54e
   __TEXT.__constg_swiftt: 0x694

   __TEXT.__swift_as_cont: 0x88
   __TEXT.__swift5_assocty: 0xa8
   __TEXT.__swift5_builtin: 0x3c
-  __TEXT.__unwind_info: 0x1460
+  __TEXT.__unwind_info: 0x1480
   __TEXT.__eh_frame: 0x6b8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x318
+  __DATA_CONST.__const: 0x320
   __DATA_CONST.__objc_classlist: 0x2f0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2fc0
+  __DATA_CONST.__objc_selrefs: 0x2fe8
   __DATA_CONST.__objc_superrefs: 0x268
   __DATA_CONST.__objc_arraydata: 0x68
-  __DATA_CONST.__got: 0x1540
+  __DATA_CONST.__got: 0x1548
   __AUTH_CONST.__const: 0x1158
-  __AUTH_CONST.__cfstring: 0x2a60
+  __AUTH_CONST.__cfstring: 0x2aa0
   __AUTH_CONST.__objc_const: 0x71d8
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0xba8
-  __AUTH.__objc_data: 0x688
-  __AUTH.__data: 0x138
+  __AUTH_CONST.__auth_got: 0xbb0
+  __AUTH.__objc_data: 0x518
+  __AUTH.__data: 0x110
   __DATA.__objc_ivar: 0x4c0
-  __DATA.__data: 0x21c
-  __DATA.__bss: 0xad0
-  __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x1d30
-  __DATA_DIRTY.__data: 0x370
-  __DATA_DIRTY.__bss: 0x2a0
-  __DATA_DIRTY.__common: 0x40
+  __DATA.__data: 0x1f4
+  __DATA.__bss: 0xab0
+  __DATA.__common: 0x8
+  __DATA_DIRTY.__objc_data: 0x1ea0
+  __DATA_DIRTY.__data: 0x3c0
+  __DATA_DIRTY.__bss: 0x2c0
+  __DATA_DIRTY.__common: 0x58
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/Contacts.framework/Versions/A/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftQuickLookUI.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2210
-  Symbols:   5023
-  CStrings:  798
+  Functions: 2214
+  Symbols:   5033
+  CStrings:  809
 
Sections:
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift_as_cont : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
Symbols:
+ +[SPUISAskSiriResultBuilder syntheticAskSiriResultForQueryContext:]
+ +[SPUISUtilities elevatedResultShouldInvokeSiri:]
+ +[SPUISUtilities isFirstSectionElevatable:]
+ +[SPUISUtilities splitSections:forElevation:elevatedSections:regularSections:]
+ __swift_FORCE_LOAD_$_swiftQuickLookUI
+ __swift_FORCE_LOAD_$_swiftQuickLookUI_$_SpotlightUIServices
+ _objc_autorelease
+ _objc_msgSend$isFirstSectionElevatable:
+ _objc_msgSend$setUsesTopHitDisplay:
+ _objc_msgSend$shouldElevateTopHitResult:
CStrings:
+ "(nil)"
+ "SearchInAppSectionBuilder: building — askSiriResult=%@ searchInAppInfo=%lu hiddenBundles=%lu"
+ "SearchInAppSectionBuilder: shouldSkipSection=YES (entities=%lu, SSShowSearchInApps=%d)"
+ "SectionBuilder input: bundle=%@ resultCount=%lu"
+ "SectionBuilder output: bundle=%@ resultCount=%lu"
+ "SectionBuilder: DROPPED empty section bundle=%@"
+ "SectionBuilder: output sectionCount=%lu"
+ "SectionBuilder: renderState=%ld askSiriResult=%@ searchInAppInfo=%lu inputSectionCount=%lu"
+ "com.apple.parsec.itunes.iosSoftware"

```
