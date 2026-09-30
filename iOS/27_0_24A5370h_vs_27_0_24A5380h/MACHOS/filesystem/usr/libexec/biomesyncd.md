## biomesyncd

> `/usr/libexec/biomesyncd`

```diff

   __TEXT.__auth_stubs: 0xd00
   __TEXT.__objc_stubs: 0x8900
   __TEXT.__objc_methlist: 0x3c24
-  __TEXT.__const: 0x1348
+  __TEXT.__const: 0x134a
   __TEXT.__gcc_except_tab: 0x89c
   __TEXT.__objc_methname: 0xa3f4
   __TEXT.__cstring: 0x59f8

   __TEXT.__objc_methtype: 0x1733
   __TEXT.__oslogstring: 0x6468
   __TEXT.__unwind_info: 0x10b0
-  __DATA_CONST.__const: 0x1128
+  __DATA_CONST.__const: 0x1160
   __DATA_CONST.__cfstring: 0x4740
   __DATA_CONST.__objc_classlist: 0x1c0
   __DATA_CONST.__objc_catlist: 0x20

   __DATA_CONST.__linkguard: 0xe
   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__auth_got: 0x690
-  __DATA_CONST.__got: 0x3d8
+  __DATA_CONST.__got: 0x448
   __DATA.__objc_const: 0x7708
   __DATA.__objc_selrefs: 0x28e0
   __DATA.__objc_ivar: 0x3ec

   - /System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets
   - /System/Library/PrivateFrameworks/CloudKitDistributedSync.framework/CloudKitDistributedSync
   - /System/Library/PrivateFrameworks/ContextSync.framework/ContextSync
+  - /System/Library/PrivateFrameworks/IntelligenceTasks.framework/IntelligenceTasks
   - /System/Library/PrivateFrameworks/ProactiveSupport.framework/ProactiveSupport
   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /System/Library/PrivateFrameworks/Rapport.framework/Rapport

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
+  - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
   Functions: 1625
-  Symbols:   349
+  Symbols:   356
   CStrings:  3691
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__unwind_info : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_imageinfo : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __DATA_CONST.__objc_arrayobj : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__objc_dictobj : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
~ __DATA.__objc_data : content changed
~ __DATA.__data : content changed
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreFoundation
+ __swift_FORCE_LOAD_$_swiftDispatch
+ __swift_FORCE_LOAD_$_swiftFoundation
+ __swift_FORCE_LOAD_$_swiftObjectiveC
+ __swift_FORCE_LOAD_$_swiftXPC
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swiftos

```
