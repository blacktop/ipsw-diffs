## biomesyncd

> `/usr/libexec/biomesyncd`

```diff

   __TEXT.__auth_stubs: 0xb80
   __TEXT.__objc_stubs: 0x8980
   __TEXT.__objc_methlist: 0x3c3c
-  __TEXT.__const: 0x1358
+  __TEXT.__const: 0x1350
   __TEXT.__gcc_except_tab: 0x8a4
   __TEXT.__objc_methname: 0xa45c
   __TEXT.__cstring: 0x5aec

   __TEXT.__objc_methtype: 0x1733
   __TEXT.__oslogstring: 0x661d
   __TEXT.__unwind_info: 0x10d0
-  __DATA_CONST.__const: 0x12e0
+  __DATA_CONST.__const: 0x1320
   __DATA_CONST.__cfstring: 0x4780
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x20

   __DATA_CONST.__linkguard: 0xf
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__auth_got: 0x5d0
-  __DATA_CONST.__got: 0x3e0
+  __DATA_CONST.__got: 0x450
   __DATA.__objc_const: 0x7718
   __DATA.__objc_selrefs: 0x2900
   __DATA.__objc_ivar: 0x3ec

   - /System/Library/PrivateFrameworks/CascadeSets.framework/Versions/A/CascadeSets
   - /System/Library/PrivateFrameworks/CloudKitDistributedSync.framework/Versions/A/CloudKitDistributedSync
   - /System/Library/PrivateFrameworks/ContextSync.framework/Versions/A/ContextSync
+  - /System/Library/PrivateFrameworks/IntelligenceTasks.framework/Versions/A/IntelligenceTasks
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/Versions/A/ProactiveSupport
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/Versions/A/ProtocolBuffer
   - /System/Library/PrivateFrameworks/Rapport.framework/Versions/A/Rapport

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
   Functions: 1680
-  Symbols:   326
+  Symbols:   334
   CStrings:  3716
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_imageinfo : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__data : content changed
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftIOKit
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swiftos

```
