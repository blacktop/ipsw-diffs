## VisionKitCore

> `/System/Library/PrivateFrameworks/VisionKitCore.framework/Versions/A/VisionKitCore`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
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
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__DATA.__data`

```diff

-341.0.0.0.0
-  __TEXT.__text: 0xa21c0
-  __TEXT.__objc_methlist: 0xb298
+342.0.0.0.0
+  __TEXT.__text: 0xa2810
+  __TEXT.__objc_methlist: 0xb2d8
   __TEXT.__const: 0xa9c
-  __TEXT.__gcc_except_tab: 0x17f0
+  __TEXT.__gcc_except_tab: 0x17fc
   __TEXT.__cstring: 0x68b4
-  __TEXT.__dlopen_cstrs: 0x310
-  __TEXT.__oslogstring: 0x2cdd
+  __TEXT.__dlopen_cstrs: 0x37a
+  __TEXT.__oslogstring: 0x2d5d
   __TEXT.__ustring: 0x4e
   __TEXT.__constg_swiftt: 0x254
   __TEXT.__swift5_typeref: 0x156

   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0xc
   __TEXT.__swift_as_cont: 0x18
-  __TEXT.__unwind_info: 0x2ff8
+  __TEXT.__unwind_info: 0x3000
   __TEXT.__eh_frame: 0x158
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xc20
+  __DATA_CONST.__const: 0xc38
   __DATA_CONST.__objc_classlist: 0x3c0
   __DATA_CONST.__objc_catlist: 0x108
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6918
+  __DATA_CONST.__objc_selrefs: 0x6950
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x230
   __DATA_CONST.__objc_arraydata: 0x2d0
   __DATA_CONST.__got: 0x948
   __AUTH_CONST.__const: 0x3088
   __AUTH_CONST.__cfstring: 0x5e20
-  __AUTH_CONST.__objc_const: 0x13620
+  __AUTH_CONST.__objc_const: 0x13670
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x108
   __AUTH_CONST.__objc_intobj: 0x300
   __AUTH_CONST.__objc_dictobj: 0xa0
   __AUTH_CONST.__objc_doubleobj: 0x70
   __AUTH_CONST.__auth_got: 0xa18
-  __AUTH.__objc_data: 0x12b8
-  __AUTH.__data: 0xa0
-  __DATA.__objc_ivar: 0xb6c
+  __AUTH.__objc_data: 0x1110
+  __AUTH.__data: 0x78
+  __DATA.__objc_ivar: 0xb70
   __DATA.__data: 0x10a0
-  __DATA.__bss: 0x620
-  __DATA_DIRTY.__objc_data: 0x1540
+  __DATA.__bss: 0x630
+  __DATA_DIRTY.__objc_data: 0x16e8
+  __DATA_DIRTY.__data: 0x28
   __DATA_DIRTY.__bss: 0xd8
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 4816
-  Symbols:   10290
-  CStrings:  1283
+  Functions: 4822
+  Symbols:   10302
+  CStrings:  1284
 
Symbols:
+ -[VKCImageAnalysisBaseView setViConfig:]
+ -[VKCImageAnalysisBaseView viConfig]
+ -[VKCImageAnalysisBaseView visualIntelligenceView:didPresentActionWindow:forAction:closeHandler:]
+ -[VKCImageAnalysisOverlayView setViConfig:]
+ -[VKCImageAnalysisOverlayView viConfig]
+ -[VKCImageAnalysisOverlayView visualIntelligenceDidPresentActionWindow:forAction:closeHandler:]
+ GCC_except_table150
+ GCC_except_table160
+ GCC_except_table237
+ GCC_except_table254
+ GCC_except_table98
+ OBJC_IVAR_$_VKCImageAnalysisBaseView._viConfig
+ _objc_msgSend$imageAnalysisOverlay:didPresentActionWindow:forAction:closeHandler:
+ _objc_msgSend$initWithRequestConfig:
+ _objc_msgSend$instancesRespondToSelector:
+ _objc_msgSend$setPreferredImageVisibility:
+ _objc_msgSend$setViConfig:
+ _objc_msgSend$viConfig
+ _objc_msgSend$visualIntelligenceDidPresentActionWindow:forAction:closeHandler:
- -[VKCImageAnalysisOverlayView visualIntelligenceDidPresentActionWindow:forAction:]
- -[VKCImageAnalysisOverlayView visualIntelligenceDidPresentImageSearchWindow:]
- GCC_except_table149
- GCC_except_table159
- GCC_except_table236
- GCC_except_table252
- _objc_msgSend$imageAnalysisOverlay:didPresentImageSearchWindow:
CStrings:
+ "Created VI Coordinator with request type: %lu, environmentBundleID: %@"
+ "Created generic VI Coordinator without config"
- "AQ1\xf1!\""
```
