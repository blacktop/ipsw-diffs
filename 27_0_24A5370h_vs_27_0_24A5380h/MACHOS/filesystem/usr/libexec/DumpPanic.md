## DumpPanic

> `/usr/libexec/DumpPanic`

```diff

-  __TEXT.__text: 0x2afa4
+  __TEXT.__text: 0x2aee4
   __TEXT.__auth_stubs: 0x1180
-  __TEXT.__objc_stubs: 0x2560
-  __TEXT.__objc_methlist: 0x844
-  __TEXT.__cstring: 0x2b3b
+  __TEXT.__objc_stubs: 0x25a0
+  __TEXT.__objc_methlist: 0x85c
+  __TEXT.__cstring: 0x2b9b
   __TEXT.__objc_classname: 0x11c
   __TEXT.__objc_methtype: 0x531
-  __TEXT.__objc_methname: 0x1eeb
+  __TEXT.__objc_methname: 0x1f55
   __TEXT.__const: 0x2e0
-  __TEXT.__gcc_except_tab: 0xb98
+  __TEXT.__gcc_except_tab: 0xb78
   __TEXT.__oslogstring: 0x48e8
   __TEXT.__ustring: 0x1c6
   __TEXT.__constg_swiftt: 0x90

   __DATA_CONST.__objc_dictobj: 0x78
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__auth_got: 0x8d8
-  __DATA_CONST.__got: 0x2b0
+  __DATA_CONST.__got: 0x2a8
   __DATA_CONST.__auth_ptr: 0x78
-  __DATA.__objc_const: 0xf80
-  __DATA.__objc_selrefs: 0xab8
-  __DATA.__objc_ivar: 0x90
+  __DATA.__objc_const: 0xfb0
+  __DATA.__objc_selrefs: 0xac8
+  __DATA.__objc_ivar: 0x94
   __DATA.__objc_data: 0x4d8
-  __DATA.__data: 0x398
+  __DATA.__data: 0x3b8
   __DATA.__common: 0x28
   __DATA.__bss: 0xab8
   __INFO_FILTER.__disable: 0x0

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 851
-  Symbols:   401
-  CStrings:  1601
+  Functions: 853
+  Symbols:   400
+  CStrings:  1607
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__unwind_info : content changed
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
+ _swift_release_x19
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
