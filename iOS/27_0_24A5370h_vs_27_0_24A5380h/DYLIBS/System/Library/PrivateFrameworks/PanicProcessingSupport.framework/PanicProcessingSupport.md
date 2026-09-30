## PanicProcessingSupport

> `/System/Library/PrivateFrameworks/PanicProcessingSupport.framework/PanicProcessingSupport`

```diff

-  __TEXT.__text: 0xc578
-  __TEXT.__objc_methlist: 0x81c
+  __TEXT.__text: 0xcb5c
+  __TEXT.__objc_methlist: 0x82c
   __TEXT.__const: 0x188
-  __TEXT.__cstring: 0x152a
+  __TEXT.__cstring: 0x15ba
   __TEXT.__oslogstring: 0xb85
   __TEXT.__gcc_except_tab: 0x124
   __TEXT.__swift5_typeref: 0x66

   __TEXT.__swift5_reflstr: 0x1a
   __TEXT.__swift5_fieldmd: 0x1c
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x2e8
+  __TEXT.__unwind_info: 0x300
   __TEXT.__eh_frame: 0xe0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6b8
+  __DATA_CONST.__objc_selrefs: 0x6d0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x38
-  __DATA_CONST.__objc_arraydata: 0x148
+  __DATA_CONST.__objc_arraydata: 0x170
   __DATA_CONST.__got: 0x1c8
   __AUTH_CONST.__const: 0x98
-  __AUTH_CONST.__cfstring: 0x2080
-  __AUTH_CONST.__objc_const: 0x1118
-  __AUTH_CONST.__objc_arrayobj: 0x18
+  __AUTH_CONST.__cfstring: 0x2180
+  __AUTH_CONST.__objc_const: 0x1138
+  __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_dictobj: 0x118
-  __AUTH_CONST.__auth_got: 0x4b0
+  __AUTH_CONST.__auth_got: 0x4b8
   __AUTH.__objc_data: 0x3a0
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x120
-  __DATA.__data: 0x190
+  __DATA.__objc_ivar: 0x124
+  __DATA.__data: 0x1a0
   __DATA.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 265
-  Symbols:   768
-  CStrings:  596
+  Functions: 270
+  Symbols:   773
+  CStrings:  612
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
Symbols:
+ -[PanicReport useCrashlogContainers:]
+ GCC_except_table41
+ _OBJC_IVAR_$_PanicReport._crashlogContainerArray
+ _objc_msgSend$mutableCopy
+ _objc_msgSend$removeObjectForKey:
- GCC_except_table40
CStrings:
+ "CrashlogContainer"
+ "CrashlogContainers"
+ "chassisID"
+ "ensembleID"
+ "hw.osenvironment"
+ "platformSOCDBuffer"
+ "totalNodeNumber"
+ "totalReportNumber"
+ "unique_crash_event_id"
- "kern.osvariant_status"

```
