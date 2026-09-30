## DumpPanic

> `/usr/libexec/DumpPanic`

```diff

-  __TEXT.__text: 0x2de0c
-  __TEXT.__auth_stubs: 0x1010
-  __TEXT.__objc_stubs: 0x2500
-  __TEXT.__objc_methlist: 0x87c
-  __TEXT.__cstring: 0x2b4b
+  __TEXT.__text: 0x2dd8c
+  __TEXT.__auth_stubs: 0xff0
+  __TEXT.__objc_stubs: 0x2540
+  __TEXT.__objc_methlist: 0x894
+  __TEXT.__cstring: 0x2bab
   __TEXT.__objc_classname: 0x11c
   __TEXT.__objc_methtype: 0x556
-  __TEXT.__objc_methname: 0x1f6a
+  __TEXT.__objc_methname: 0x1fd4
   __TEXT.__const: 0x2d0
-  __TEXT.__gcc_except_tab: 0xc34
+  __TEXT.__gcc_except_tab: 0xc14
   __TEXT.__oslogstring: 0x5018
   __TEXT.__constg_swiftt: 0x90
   __TEXT.__swift5_typeref: 0x8b
   __TEXT.__swift5_reflstr: 0x27
   __TEXT.__swift5_fieldmd: 0x34
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x8e8
+  __TEXT.__unwind_info: 0x8e0
   __TEXT.__eh_frame: 0xa0
   __DATA_CONST.__const: 0x7c8
   __DATA_CONST.__cfstring: 0x22c0

   __DATA_CONST.__objc_arrayobj: 0xc0
   __DATA_CONST.__objc_dictobj: 0xa0
   __DATA_CONST.__objc_intobj: 0x78
-  __DATA_CONST.__auth_got: 0x820
-  __DATA_CONST.__got: 0x280
+  __DATA_CONST.__auth_got: 0x810
+  __DATA_CONST.__got: 0x278
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA.__objc_const: 0xfb0
-  __DATA.__objc_selrefs: 0xaa8
-  __DATA.__objc_ivar: 0x94
+  __DATA.__objc_const: 0xfe0
+  __DATA.__objc_selrefs: 0xab8
+  __DATA.__objc_ivar: 0x98
   __DATA.__objc_data: 0x4d8
-  __DATA.__data: 0x3b8
+  __DATA.__data: 0x3d8
   __DATA.__common: 0x28
   __DATA.__bss: 0xaa8
   __INFO_FILTER.__disable: 0x0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 892
-  Symbols:   373
-  CStrings:  1633
+  Functions: 894
+  Symbols:   370
+  CStrings:  1639
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_intobj : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_data : content changed
Symbols:
+ __os_log_default
- _$ss042_stdlib_isOSVersionAtLeastOrVariantVersiondE0yBi1_Bw_BwBwBwBwBwtF
- _$ss5NeverON
- _$ss5NeverOs5ErrorsWP
- _swift_willThrowTypedImpl
CStrings:
+ "  -r, --rtkit-crashlog FILE\n              use raw RTKit crashlog binary file\n\n"
+ "T@\"NSURL\",&,V_rtkit_crashlog_binary"
+ "_rtkit_crashlog_binary"
+ "hs:i:p:r:b:e:o:"
+ "rtkit-crashlog"
+ "rtkit_crashlog_binary"
+ "setRtkit_crashlog_binary:"
- "hs:i:p:b:e:o:"

```
