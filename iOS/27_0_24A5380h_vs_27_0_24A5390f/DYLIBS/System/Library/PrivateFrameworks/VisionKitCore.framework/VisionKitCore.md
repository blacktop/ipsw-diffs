## VisionKitCore

> `/System/Library/PrivateFrameworks/VisionKitCore.framework/VisionKitCore`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__DATA.__common`

```diff

-341.0.0.0.0
-  __TEXT.__text: 0xe6bd0
-  __TEXT.__objc_methlist: 0x105bc
+342.0.0.0.0
+  __TEXT.__text: 0xe70bc
+  __TEXT.__objc_methlist: 0x10624
   __TEXT.__const: 0x1e80
-  __TEXT.__gcc_except_tab: 0x26dc
+  __TEXT.__gcc_except_tab: 0x26e8
   __TEXT.__cstring: 0x829d
-  __TEXT.__oslogstring: 0x4137
-  __TEXT.__dlopen_cstrs: 0x78d
+  __TEXT.__oslogstring: 0x41a7
+  __TEXT.__dlopen_cstrs: 0x7f7
   __TEXT.__ustring: 0x4e
   __TEXT.__constg_swiftt: 0x19c8
   __TEXT.__swift5_typeref: 0x6f0

   __TEXT.__swift_as_cont: 0x18
   __TEXT.__swift5_capture: 0x134
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x4378
+  __TEXT.__unwind_info: 0x4380
   __TEXT.__eh_frame: 0x4c8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x3c58
+  __DATA_CONST.__const: 0x3c70
   __DATA_CONST.__objc_classlist: 0x680
   __DATA_CONST.__objc_catlist: 0x100
   __DATA_CONST.__objc_protolist: 0x298
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x9850
+  __DATA_CONST.__objc_selrefs: 0x9890
   __DATA_CONST.__objc_protorefs: 0x78
   __DATA_CONST.__objc_superrefs: 0x390
   __DATA_CONST.__objc_arraydata: 0x2a0
   __DATA_CONST.__got: 0xf70
   __AUTH_CONST.__const: 0x19c0
   __AUTH_CONST.__cfstring: 0x68c0
-  __AUTH_CONST.__objc_const: 0x31120
+  __AUTH_CONST.__objc_const: 0x311d0
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x3f0
   __AUTH_CONST.__objc_doubleobj: 0xe0
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__auth_got: 0x1088
-  __AUTH.__objc_data: 0x4d38
-  __AUTH.__data: 0x11d8
-  __DATA.__objc_ivar: 0x113c
-  __DATA.__data: 0x20d0
-  __DATA.__bss: 0x14b0
+  __AUTH.__objc_data: 0x43c0
+  __AUTH.__data: 0x11e0
+  __DATA.__objc_ivar: 0x1140
+  __DATA.__data: 0x2130
+  __DATA.__bss: 0x1490
   __DATA.__common: 0x68
-  __DATA_DIRTY.__objc_data: 0x910
-  __DATA_DIRTY.__bss: 0xd8
+  __DATA_DIRTY.__objc_data: 0x1288
+  __DATA_DIRTY.__data: 0x28
+  __DATA_DIRTY.__bss: 0x110
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 6769
-  Symbols:   14200
-  CStrings:  1618
+  Functions: 6776
+  Symbols:   14210
+  CStrings:  1620
 
Symbols:
+ -[VKAVCaptureFrameProvider videoRotationAngle]
+ -[VKCImageAnalysisBaseView setViConfig:]
+ -[VKCImageAnalysisBaseView viConfig]
+ -[VKCImageAnalysisInteraction setViConfig:]
+ -[VKCImageAnalysisInteraction viConfig]
+ GCC_except_table203
+ GCC_except_table228
+ _OBJC_IVAR_$_VKCImageAnalysisBaseView._viConfig
+ _objc_msgSend$initWithRequestConfig:
+ _objc_msgSend$instancesRespondToSelector:
+ _objc_msgSend$setViConfig:
+ _objc_msgSend$viConfig
- GCC_except_table199
- GCC_except_table226
CStrings:
+ "AQ1\xf0A\""
+ "Created VI Coordinator with request type: %lu, environmentBundleID: %@"
+ "Created generic VI Coordinator without config"
- "AQ1\xf01\""
```
