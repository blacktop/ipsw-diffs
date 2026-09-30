## nearbyd

> `/usr/libexec/nearbyd`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-575.0.5.0.0
-  __TEXT.__text: 0x54dbe4
+575.0.6.0.0
+  __TEXT.__text: 0x54e254
   __TEXT.__auth_stubs: 0x30f0
-  __TEXT.__objc_stubs: 0x17600
+  __TEXT.__objc_stubs: 0x17640
   __TEXT.__init_offsets: 0x6fc
-  __TEXT.__objc_methlist: 0xf8bc
-  __TEXT.__gcc_except_tab: 0x558ac
-  __TEXT.__const: 0x3faaa0
-  __TEXT.__cstring: 0x38e52
-  __TEXT.__objc_methname: 0x23aa5
-  __TEXT.__oslogstring: 0x63ada
+  __TEXT.__objc_methlist: 0xf8e4
+  __TEXT.__gcc_except_tab: 0x5595c
+  __TEXT.__const: 0x3faab0
+  __TEXT.__cstring: 0x38eb2
+  __TEXT.__objc_methname: 0x23b25
+  __TEXT.__oslogstring: 0x63c1a
   __TEXT.__objc_classname: 0x20be
-  __TEXT.__objc_methtype: 0x22dfd
+  __TEXT.__objc_methtype: 0x22e0d
   __TEXT.__ustring: 0x60
   __TEXT.__swift5_typeref: 0x7ec
   __TEXT.__swift5_capture: 0x574

   __TEXT.__swift_as_entry: 0x60
   __TEXT.__swift_as_ret: 0x2c
   __TEXT.__swift_as_cont: 0x80
-  __TEXT.__unwind_info: 0x22138
+  __TEXT.__unwind_info: 0x22170
   __TEXT.__eh_frame: 0x5a0
   __DATA_CONST.__const: 0x1f5c0
-  __DATA_CONST.__cfstring: 0x177a0
+  __DATA_CONST.__cfstring: 0x17800
   __DATA_CONST.__objc_classlist: 0x640
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x330

   __DATA_CONST.__auth_got: 0x1890
   __DATA_CONST.__got: 0xe68
   __DATA_CONST.__auth_ptr: 0x300
-  __DATA.__objc_const: 0x1b900
-  __DATA.__objc_selrefs: 0x71c0
-  __DATA.__objc_ivar: 0x1a34
+  __DATA.__objc_const: 0x1b940
+  __DATA.__objc_selrefs: 0x71d0
+  __DATA.__objc_ivar: 0x1a3c
   __DATA.__objc_data: 0x4a18
   __DATA.__data: 0x42cc
   __DATA.__common: 0xe80

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 23613
+  Functions: 23619
   Symbols:   1312
-  CStrings:  19977
+  CStrings:  19989
 
CStrings:
+ "#ses-loc,DL-TDoA background runtime budget (%.0fs) elapsed; force-closing session."
+ "#ses-loc,DL-TDoA background session NOT supported"
+ "#ses-loc,DL-TDoA session started while Not Foreground: %d; will be force-closed after %.0fs."
+ "#ses-loc,Skipping client update: no valid DL-TDoA anchors in range while app is backgrounded"
+ "DL-TDoA background session NOT supported"
+ "NIDLTDOABackgroundLaunchEnabled"
+ "_appLaunchedFromBackground"
+ "_checkIsInternalToolProxtool"
+ "_isClientBackgrounded"
+ "_sessionLaunchedFromBackground"
+ "isBackgroundSession"
+ "sessionInvalidateWithReason:isLaunchedFromBackground:"
+ "v24@0:8C16B20"
- "sessionInvalidateWithReason:"
```
