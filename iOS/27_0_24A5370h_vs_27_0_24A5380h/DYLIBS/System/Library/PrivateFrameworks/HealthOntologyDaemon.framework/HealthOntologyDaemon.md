## HealthOntologyDaemon

> `/System/Library/PrivateFrameworks/HealthOntologyDaemon.framework/HealthOntologyDaemon`

```diff

-  __TEXT.__text: 0x2d32c
+  __TEXT.__text: 0x2d5f8
   __TEXT.__objc_methlist: 0x21ac
   __TEXT.__const: 0x282
-  __TEXT.__gcc_except_tab: 0x628
+  __TEXT.__gcc_except_tab: 0x668
   __TEXT.__cstring: 0x33bc
-  __TEXT.__oslogstring: 0x1d5a
+  __TEXT.__oslogstring: 0x1d7a
   __TEXT.__swift5_proto: 0x8
   __TEXT.__swift5_typeref: 0xb1
   __TEXT.__swift5_fieldmd: 0x40
   __TEXT.__constg_swiftt: 0xbc
   __TEXT.__swift5_protos: 0x10
-  __TEXT.__unwind_info: 0xe68
+  __TEXT.__unwind_info: 0xe88
   __TEXT.__eh_frame: 0x80
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1978
+  __DATA_CONST.__const: 0x19f0
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x58
   __DATA_CONST.__objc_protolist: 0x120

   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0xf8
   __DATA_CONST.__objc_arraydata: 0x2b0
-  __DATA_CONST.__got: 0x3e0
+  __DATA_CONST.__got: 0x3f8
   __AUTH_CONST.__const: 0x381
-  __AUTH_CONST.__cfstring: 0x2220
-  __AUTH_CONST.__objc_const: 0x3f20
+  __AUTH_CONST.__cfstring: 0x2240
+  __AUTH_CONST.__objc_const: 0x3f40
   __AUTH_CONST.__objc_arrayobj: 0x150
   __AUTH_CONST.__objc_intobj: 0x1f8
-  __AUTH_CONST.__auth_got: 0x4a0
-  __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x1e8
+  __AUTH_CONST.__auth_got: 0x4b8
+  __AUTH.__objc_data: 0xf0
+  __DATA.__objc_ivar: 0x1ec
   __DATA.__data: 0xc90
   __DATA.__bss: 0x8
-  __DATA_DIRTY.__objc_data: 0xc30
-  __DATA_DIRTY.__data: 0x8
+  __DATA_DIRTY.__objc_data: 0xc80
+  __DATA_DIRTY.__data: 0x10
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1093
-  Symbols:   3956
-  CStrings:  723
+  Functions: 1098
+  Symbols:   3970
+  CStrings:  724
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__const : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA.__data : content changed
Symbols:
+ GCC_except_table68
+ GCC_except_table81
+ _OBJC_IVAR_$_HDOntologyUpdateCoordinator._bgstCompletionQueue
+ ___117-[HDOntologyUpdateCoordinator _runOntologyUpdateWithShouldDefer:addExpirationHandler:reason:activityName:completion:]_block_invoke_2
+ ___block_descriptor_40_e8_32bs_e5_v8?0ls32l8
+ ___block_descriptor_56_e8_32s40bs48r_e20_v24?0q8"NSError"16ls32l8r48l8s40l8
+ ___block_descriptor_56_e8_32s40s48bs_e5_v8?0ls32l8s40l8s48l8
+ _dispatch_async
+ _objc_sync_enter
+ _objc_sync_exit
- GCC_except_table79
CStrings:
+ "%{public}@: Expiration handler fired, cancelling in-flight ontology update work and acking BGST as deferred"
+ "bgst-completion"
- "%{public}@: Expiration handler fired, cancelling in-flight ontology update work"
- "\xa1"

```
