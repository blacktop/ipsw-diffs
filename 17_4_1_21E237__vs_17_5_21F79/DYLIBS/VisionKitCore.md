## VisionKitCore

> `/System/Library/PrivateFrameworks/VisionKitCore.framework/VisionKitCore`

```diff

-252.6.0.0.0
-  __TEXT.__text: 0xc356c
+252.7.0.0.0
+  __TEXT.__text: 0xc3604
   __TEXT.__auth_stubs: 0x14a0
-  __TEXT.__objc_methlist: 0xcb48
+  __TEXT.__objc_methlist: 0xcb68
   __TEXT.__const: 0x804
   __TEXT.__gcc_except_tab: 0x2200
-  __TEXT.__cstring: 0x7739
+  __TEXT.__cstring: 0x774e
   __TEXT.__oslogstring: 0x3004
   __TEXT.__dlopen_cstrs: 0x419
   __TEXT.__ustring: 0xa0
-  __TEXT.__unwind_info: 0x3c58
+  __TEXT.__unwind_info: 0x3c74
   __TEXT.__eh_frame: 0x74
   __TEXT.__objc_classname: 0x1740
-  __TEXT.__objc_methname: 0x25cfe
+  __TEXT.__objc_methname: 0x25d56
   __TEXT.__objc_methtype: 0x5e51
-  __TEXT.__objc_stubs: 0x19ea0
+  __TEXT.__objc_stubs: 0x19f00
   __DATA_CONST.__got: 0x520
   __DATA_CONST.__const: 0x38b0
   __DATA_CONST.__objc_classlist: 0x540
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x1c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x1b4e8
-  __DATA_CONST.__objc_selrefs: 0x8028
+  __DATA_CONST.__objc_const: 0x1b4f8
+  __DATA_CONST.__objc_selrefs: 0x8040
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_classrefs: 0xa58
   __DATA_CONST.__objc_superrefs: 0x380
   __DATA_CONST.__objc_arraydata: 0x220
-  __AUTH_CONST.__cfstring: 0x63e0
+  __AUTH_CONST.__cfstring: 0x6440
   __AUTH_CONST.__objc_const: 0x4040
   __AUTH_CONST.__const: 0xdb0
   __AUTH_CONST.__objc_intobj: 0x3f0

   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_ptr: 0x8
   __AUTH_CONST.__auth_got: 0xa68
-  __AUTH.__objc_data: 0x20d0
+  __AUTH.__objc_data: 0x1f90
   __DATA.__objc_ivar: 0x1030
-  __DATA.__data: 0x1670
-  __DATA.__bss: 0x388
-  __DATA_DIRTY.__objc_data: 0x13b0
-  __DATA_DIRTY.__bss: 0x110
+  __DATA.__data: 0x16c0
+  __DATA.__bss: 0x348
+  __DATA_DIRTY.__objc_data: 0x14f0
+  __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 5900
-  Symbols:   19539
-  CStrings:  8486
+  Functions: 5903
+  Symbols:   19548
+  CStrings:  8492
 
Symbols:
+ -[VKAnalyticsEvent bundleIdentifierCleansingIfNecessaryWithCustomIdentifier:]
+ -[VKAnalyticsEvent cleansesBundleID]
+ -[VKAnalyticsSubjectEvent cleansesBundleID]
+ _objc_msgSend$bundleIdentifierCleansingIfNecessaryWithCustomIdentifier:
+ _objc_msgSend$cleansesBundleID
+ _objc_msgSend$hasPrefix:
CStrings:
+ "%@ \n eventType: %@ \n interactionType: %@ \n subjectFound: %@ \n processingDuration: %f \n automatedTest: %@ \n bundleId: %@ "
+ "3rdparty"
+ "bundleId"
+ "bundleIdentifierCleansingIfNecessaryWithCustomIdentifier:"
+ "cleansesBundleID"
+ "com.apple."
+ "hasPrefix:"
- "%@ \n eventType: %@ \n interactionType: %@ \n subjectFound: %@ \n processingDuration: %f \n automatedTest: %@ \n bundleIdentifier: %@ "

```
