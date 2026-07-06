## UIKitCore

> `/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`

```diff

-  __TEXT.__text: 0x1b55254
+  __TEXT.__text: 0x1b553bc
   __TEXT.__auth_stubs: 0xdb60
   __TEXT.__delay_helper: 0x1bc
   __TEXT.__init_offsets: 0x4
-  __TEXT.__objc_methlist: 0x1948d0
+  __TEXT.__objc_methlist: 0x1948d8
   __TEXT.__const: 0x40d98
   __TEXT.__dlopen_cstrs: 0x4a2f
   __TEXT.__swift5_typeref: 0x13dda

   __TEXT.__swift5_protos: 0x200
   __TEXT.__swift5_proto: 0x1ec8
   __TEXT.__swift5_types: 0x1760
-  __TEXT.__oslogstring: 0x4cb34
+  __TEXT.__oslogstring: 0x4cc1a
   __TEXT.__swift_as_entry: 0x18c
   __TEXT.__swift_as_ret: 0x130
   __TEXT.__swift5_mpenum: 0x21c

   __TEXT.__unwind_info: 0x719a0
   __TEXT.__eh_frame: 0x7000
   __TEXT.__objc_classname: 0x3c8e3
-  __TEXT.__objc_methname: 0x3214ea
+  __TEXT.__objc_methname: 0x32151a
   __TEXT.__objc_methtype: 0x790da
   __TEXT.__objc_stubs: 0x1e3e20
   __DATA_CONST.__got: 0x7950

   __DATA_CONST.__objc_catlist: 0x328
   __DATA_CONST.__objc_protolist: 0x31b8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x92a78
+  __DATA_CONST.__objc_selrefs: 0x92a80
   __DATA_CONST.__objc_protorefs: 0xc30
   __DATA_CONST.__objc_superrefs: 0x73f8
   __DATA_CONST.__objc_arraydata: 0x4648

   __AUTH_CONST.__objc_floatobj: 0x20
   __AUTH.__objc_data: 0x52130
   __AUTH.__data: 0x8c28
-  __DATA.__objc_ivar: 0x1168c
+  __DATA.__objc_ivar: 0x11690
   __DATA.__data: 0x2eed8
   __DATA.__uikit_ip: 0x898
   __DATA.__uikit_ipl: 0x18
   __DATA.__bss: 0x35150
   __DATA.__common: 0x28a8
-  __DATA_DIRTY.__objc_ivar: 0x8a88
+  __DATA_DIRTY.__objc_ivar: 0x8a84
   __DATA_DIRTY.__objc_data: 0x2bae8
   __DATA_DIRTY.__uikit_ip: 0x11e8
   __DATA_DIRTY.__data: 0x7488

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 173511
-  Symbols:   437869
-  CStrings:  181225
+  Functions: 173512
+  Symbols:   437873
+  CStrings:  181227
 
Sections:
~ __TEXT.__const : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__cstring : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_types2 : content changed
~ __TEXT.__gcc_except_tab : content changed
~ __TEXT.__unwind_info : content changed
~ __TEXT.__eh_frame : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__auth_got : content changed
~ __AUTH_CONST.__const : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __AUTH_CONST.__objc_doubleobj : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_dictobj : content changed
~ __AUTH_CONST.__objc_floatobj : content changed
~ __AUTH.__objc_data : content changed
~ __AUTH.__data : content changed
~ __DATA.__data : content changed
~ __DATA.__uikit_ipl : content changed
~ __DATA_DIRTY.__objc_data : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ -[UIKeyboardLayoutCursor _logMajorToggleMissingCurrentKeyplane]
+ _OBJC_IVAR_$_UIKeyboardLayoutStar._keyboardName
+ __logMajorToggleMissingCurrentKeyplane.faultCount
Functions:
+ -[UIKeyboardLayoutCursor _logMajorToggleMissingCurrentKeyplane]
~ -[UIKeyboardLayoutStar .cxx_destruct] : 1188 -> 1192
CStrings:
+ "_logMajorToggleMissingCurrentKeyplane"
+ "rdar://176560598: Play/Pause keyplane toggle reached with no current keyplane; skipped keyplane toggle to avoid NSNotFound crash. keyboard=%{public}@ keyplaneName=%{public}@ keyplaneIsNil=%d subtreeCount=%lu suppressOperations=%d"

```
