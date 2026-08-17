## PosterUIFoundation

> `/System/Library/PrivateFrameworks/PosterUIFoundation.framework/PosterUIFoundation`

```diff

-355.0.5.0.0
-  __TEXT.__text: 0x94d08
-  __TEXT.__objc_methlist: 0xab7c
+355.0.8.0.0
+  __TEXT.__text: 0x950a8
+  __TEXT.__objc_methlist: 0xabdc
   __TEXT.__const: 0xdc4
-  __TEXT.__oslogstring: 0x3a21
-  __TEXT.__cstring: 0x6783
-  __TEXT.__gcc_except_tab: 0x17ac
+  __TEXT.__oslogstring: 0x3a51
+  __TEXT.__cstring: 0x67b3
+  __TEXT.__gcc_except_tab: 0x17bc
   __TEXT.__dlopen_cstrs: 0x216
   __TEXT.__swift5_typeref: 0x80a
   __TEXT.__constg_swiftt: 0x708

   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x2c
   __TEXT.__swift5_capture: 0x30
-  __TEXT.__unwind_info: 0x29e0
+  __TEXT.__unwind_info: 0x29e8
   __TEXT.__eh_frame: 0x40
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x5910
+  __DATA_CONST.__objc_selrefs: 0x5930
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x410
   __DATA_CONST.__objc_arraydata: 0x18e0
   __DATA_CONST.__got: 0xfb8
   __AUTH_CONST.__const: 0x1100
-  __AUTH_CONST.__cfstring: 0x7fc0
-  __AUTH_CONST.__objc_const: 0x1efb0
+  __AUTH_CONST.__cfstring: 0x8000
+  __AUTH_CONST.__objc_const: 0x1f038
   __AUTH_CONST.__objc_dictobj: 0xcf8
   __AUTH_CONST.__objc_intobj: 0xdb0
   __AUTH_CONST.__objc_doubleobj: 0x2b0

   __AUTH_CONST.__auth_got: 0x10c0
   __AUTH.__objc_data: 0x2410
   __AUTH.__data: 0x1a0
-  __DATA.__objc_ivar: 0xbe0
+  __DATA.__objc_ivar: 0xbe4
   __DATA.__data: 0x17a8
   __DATA.__bss: 0x900
   __DATA.__common: 0x18

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4155
-  Symbols:   9678
-  CStrings:  1504
+  Functions: 4161
+  Symbols:   9687
+  CStrings:  1507
 
Symbols:
+ -[FBSMutableSceneSettings(PosterUIFoundation) pui_setRenderSessionTimeoutInterval:]
+ -[FBSSceneSettings(PosterUIFoundation) pui_renderSessionTimeoutInterval]
+ -[PUIPosterSnapshotHostConfigurationDescriptor captureTimeoutInterval]
+ -[PUIPosterSnapshotHostConfigurationDescriptor copyWithCaptureTimeoutInterval:]
+ -[PUIPosterSnapshotHostConfigurationDescriptor initWithHostWorkQueue:waitUntilReady:inProcessSnapshot:abortsIfBacklightNotFull:captureTimeoutInterval:]
+ _OBJC_IVAR_$_PUIPosterSnapshotHostConfigurationDescriptor._captureTimeoutInterval
+ _PUIPosterSnapshotDefaultCaptureTimeoutInterval
+ _objc_msgSend$captureTimeoutInterval
+ _objc_msgSend$pui_renderSessionTimeoutInterval
+ _objc_msgSend$pui_setRenderSessionTimeoutInterval:
- -[PUIPosterSnapshotHostConfigurationDescriptor initWithHostWorkQueue:waitUntilReady:inProcessSnapshot:abortsIfBacklightNotFull:]
CStrings:
+ "(%p) waiting up to %.1fs for scene readiness"
+ "_captureTimeoutInterval"
+ "captureTimeoutInterval"
```
