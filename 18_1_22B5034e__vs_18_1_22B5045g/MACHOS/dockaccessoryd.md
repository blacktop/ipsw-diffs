## dockaccessoryd

> `/usr/libexec/dockaccessoryd`

```diff

-230.1.0.0.0
-  __TEXT.__text: 0x1f7fb0
-  __TEXT.__auth_stubs: 0x35c0
+250.1.0.0.0
+  __TEXT.__text: 0x1f8afc
+  __TEXT.__auth_stubs: 0x35e0
   __TEXT.__objc_stubs: 0xc1e0
   __TEXT.__objc_methlist: 0x9100
-  __TEXT.__objc_methname: 0x15cf8
-  __TEXT.__cstring: 0xc4c5
+  __TEXT.__objc_methname: 0x15cb8
+  __TEXT.__cstring: 0xc525
   __TEXT.__objc_classname: 0x14a3
   __TEXT.__objc_methtype: 0x3484
   __TEXT.__const: 0x39b8
-  __TEXT.__oslogstring: 0x14322
+  __TEXT.__oslogstring: 0x14492
   __TEXT.__gcc_except_tab: 0xd4c
-  __TEXT.__swift5_typeref: 0x2546
+  __TEXT.__swift5_typeref: 0x2552
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x4e00
   __TEXT.__swift5_builtin: 0x1e0
   __TEXT.__swift5_reflstr: 0x219a
   __TEXT.__swift5_fieldmd: 0x24f4
   __TEXT.__swift5_assocty: 0x270
-  __TEXT.__swift5_capture: 0x13b8
+  __TEXT.__swift5_capture: 0x1410
   __TEXT.__swift5_proto: 0x21c
   __TEXT.__swift5_types: 0x1f0
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_mpenum: 0x10
-  __TEXT.__unwind_info: 0x4ce8
-  __TEXT.__eh_frame: 0x51e0
-  __DATA_CONST.__auth_got: 0x1af0
-  __DATA_CONST.__got: 0xba0
+  __TEXT.__unwind_info: 0x4cf0
+  __TEXT.__eh_frame: 0x51b0
+  __DATA_CONST.__auth_got: 0x1b00
+  __DATA_CONST.__got: 0xba8
   __DATA_CONST.__auth_ptr: 0x878
-  __DATA_CONST.__const: 0x7920
+  __DATA_CONST.__const: 0x7a08
   __DATA_CONST.__cfstring: 0x5be0
   __DATA_CONST.__objc_classlist: 0x638
   __DATA_CONST.__objc_catlist: 0x18

   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA.__objc_const: 0x17608
-  __DATA.__objc_selrefs: 0x4240
+  __DATA.__objc_selrefs: 0x4230
   __DATA.__objc_ivar: 0xa04
   __DATA.__objc_data: 0x6fa0
-  __DATA.__data: 0x6430
+  __DATA.__data: 0x6420
   __DATA.__objc_stublist: 0x8
   __DATA.__bss: 0x3cf0
   __DATA.__common: 0x580

   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
   - /System/Library/Frameworks/CoreHaptics.framework/CoreHaptics
   - /System/Library/Frameworks/CoreMotion.framework/CoreMotion
-  - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 6743
-  Symbols:   1392
-  CStrings:  7041
+  Functions: 6757
+  Symbols:   1395
+  CStrings:  7046
 
Symbols:
+ _$s8Dispatch0A13TimeoutResultO2eeoiySbAC_ACtFZ
+ _OBJC_CLASS_$_FBSDisplayLayoutMonitor
+ _OBJC_CLASS_$_FBSDisplayLayoutElement
+ _OBJC_CLASS_$_FBSDisplayLayoutMonitorConfiguration
+ _$sSo21OS_dispatch_semaphoreC8DispatchE4wait7timeoutAC0D13TimeoutResultOAC0D4TimeV_tF
+ _$s11DockKitCore0A6StatusOSYAAMc
- _OBJC_CLASS_$_RBSProcessStateDescriptor
- _OBJC_CLASS_$_LSApplicationRecord
- _OBJC_CLASS_$_RBSProcessState
CStrings:
+ "configurationForDefaultMainDisplayMonitor"
+ "monitorWithConfiguration:"
+ "Can't detect foreground app"
+ "setTransitionHandler:"
+ "v32@?0@\"FBSDisplayLayoutMonitor\"8@\"FBSDisplayLayout\"16@\"FBSDisplayLayoutTransitionContext\"24"
+ "Found these apps in foreground: %!s(MISSING)"
+ "buffer is incomplete, this is not expected. Not processing jarvis report further"
+ "Another instance of Jarvis monitoring is running, this is unusual - not starting another instance"
+ "Dock status has not changed, returning"
+ "bundleIdentifier"
+ "elements"
+ "Report length is not valid"
- "bundle"
- "statesForPredicate:withDescriptor:error:"
- "process"
- "setValues:"
- "setEndowmentNamespaces:"
- "initWithBundleIdentifier:allowPlaceholder:error:"
- "predicateMatchingProcessTypeApplication"

```
