## CarCommandsFlowDelegatePlugin

> `/System/Library/Assistant/FlowDelegatePlugins/CarCommandsFlowDelegatePlugin.bundle/CarCommandsFlowDelegatePlugin`

```diff

-3400.104.1.0.0
-  __TEXT.__text: 0x149424
-  __TEXT.__auth_stubs: 0x3300
+3401.3.1.0.0
+  __TEXT.__text: 0x1487a0
+  __TEXT.__auth_stubs: 0x3360
   __TEXT.__objc_stubs: 0x6e0
   __TEXT.__objc_methlist: 0x4b0
-  __TEXT.__const: 0xa8e4
+  __TEXT.__const: 0xaa14
   __TEXT.__gcc_except_tab: 0x120
   __TEXT.__objc_methname: 0x20f3
-  __TEXT.__cstring: 0x11ddd
+  __TEXT.__cstring: 0x11f1d
   __TEXT.__oslogstring: 0x84f
   __TEXT.__objc_classname: 0x17a
   __TEXT.__objc_methtype: 0x805
-  __TEXT.__constg_swiftt: 0x6bbc
-  __TEXT.__swift5_typeref: 0x4500
-  __TEXT.__swift5_fieldmd: 0x38e8
+  __TEXT.__constg_swiftt: 0x6d24
+  __TEXT.__swift5_typeref: 0x4544
+  __TEXT.__swift5_fieldmd: 0x3910
   __TEXT.__swift5_builtin: 0xa0
-  __TEXT.__swift5_reflstr: 0x3f33
+  __TEXT.__swift5_reflstr: 0x3e93
   __TEXT.__swift5_assocty: 0x1150
   __TEXT.__swift5_proto: 0x980
-  __TEXT.__swift5_types: 0x3d8
+  __TEXT.__swift5_types: 0x3dc
   __TEXT.__swift5_protos: 0x144
-  __TEXT.__swift5_capture: 0x594
+  __TEXT.__swift5_capture: 0x5bc
   __TEXT.__swift5_mpenum: 0x18
-  __TEXT.__unwind_info: 0x6e90
-  __TEXT.__eh_frame: 0x13a0c
-  __DATA_CONST.__auth_got: 0x1990
-  __DATA_CONST.__got: 0xab8
-  __DATA_CONST.__auth_ptr: 0x1e20
-  __DATA_CONST.__const: 0xa1a0
+  __TEXT.__unwind_info: 0x6fe0
+  __TEXT.__eh_frame: 0x13a8c
+  __DATA_CONST.__auth_got: 0x19c0
+  __DATA_CONST.__got: 0xac8
+  __DATA_CONST.__auth_ptr: 0x1d28
+  __DATA_CONST.__const: 0xa1b0
   __DATA_CONST.__cfstring: 0x20
-  __DATA_CONST.__objc_classlist: 0x280
+  __DATA_CONST.__objc_classlist: 0x288
   __DATA_CONST.__objc_protolist: 0x168
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0xd8
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_intobj: 0x30
-  __DATA.__objc_const: 0x63f0
+  __DATA.__objc_const: 0x5f48
   __DATA.__objc_selrefs: 0xa88
   __DATA.__objc_ivar: 0x20
-  __DATA.__objc_data: 0x2068
-  __DATA.__data: 0xb970
-  __DATA.__common: 0x370
+  __DATA.__objc_data: 0x26a8
+  __DATA.__data: 0xbef0
+  __DATA.__common: 0x440
   __DATA.__bss: 0xcc00
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftVideoToolbox.dylib
   - /usr/lib/swift/libswiftWebKit.dylib
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
-  Functions: 8528
-  Symbols:   324
-  CStrings:  1914
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 8592
+  Symbols:   334
+  CStrings:  1920
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
+ _swift_weakDestroy
+ _swift_weakInit
+ _swift_weakLoadStrong
- _objc_retain_x26
CStrings:
+ "\n    hasUserVocabMatchForOtherDomain: "
+ "$__lazy_storage_$_hasUserVocabMatchForOtherDomain"
+ "Making carCommandsSignal#intentHandledResponse failed refresh Output"
+ "Making carCommandsSignal#intentHandledResponse initial presentation Output"
+ "Making carCommandsSignal#intentHandledResponse refresh Output"
+ "This parse has a user vocab match for another domain, but does not have an exact user vocab match for CarCommands. Rejecting parse."
+ "_TtC29CarCommandsFlowDelegatePlugin14SnippetManager"
+ "carCommandsSignal#intentHandledResponse"
+ "init(from:unitProvider:)"
+ "snippetManager"
+ "unitProvider"
+ "updatableSnippetIsPresented"
- "\n    hasUserVocabForOtherDomain: "
- " initial presentation Output"
- "$__lazy_storage_$_hasUserVocabExactMatchForOtherDomain"
- "This parse has an exact user vocab match for another domain, but does not have an exact user vocab match for CarCommands. Rejecting parse."
- "shouldRefreshCurrentlyPresentedSnippet"
- "shouldRefreshSnippetKey"

```
