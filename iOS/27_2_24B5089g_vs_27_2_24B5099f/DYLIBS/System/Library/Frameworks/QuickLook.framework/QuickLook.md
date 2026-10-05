## QuickLook

> `/System/Library/Frameworks/QuickLook.framework/QuickLook`

```diff

-1034.1.3.0.0
-  __TEXT.__text: 0xd57ec
-  __TEXT.__delay_helper: 0x948
-  __TEXT.__objc_methlist: 0xb894
-  __TEXT.__const: 0x3b94
-  __TEXT.__gcc_except_tab: 0x175c
-  __TEXT.__cstring: 0x5354
-  __TEXT.__oslogstring: 0x57d7
+1034.1.4.0.0
+  __TEXT.__text: 0xd56a4
+  __TEXT.__delay_helper: 0xa24
+  __TEXT.__objc_methlist: 0xb8d4
+  __TEXT.__const: 0x3b64
+  __TEXT.__gcc_except_tab: 0x1760
+  __TEXT.__cstring: 0x54ba
+  __TEXT.__oslogstring: 0x5887
   __TEXT.__ustring: 0x1c
   __TEXT.__swift5_typeref: 0x1d4a
   __TEXT.__swift5_reflstr: 0x9a7
   __TEXT.__swift5_assocty: 0x368
-  __TEXT.__constg_swiftt: 0x1854
+  __TEXT.__constg_swiftt: 0x185c
   __TEXT.__swift5_fieldmd: 0xb4c
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_proto: 0x198
   __TEXT.__swift5_types: 0x120
-  __TEXT.__swift5_capture: 0x1008
+  __TEXT.__swift5_capture: 0xff8
   __TEXT.__swift_as_entry: 0x1b4
-  __TEXT.__swift_as_ret: 0x1e4
-  __TEXT.__swift_as_cont: 0x4ec
+  __TEXT.__swift_as_ret: 0x1e0
+  __TEXT.__swift_as_cont: 0x4f0
   __TEXT.__swift5_protos: 0x18
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__unwind_info: 0x5628
-  __TEXT.__eh_frame: 0x49ac
+  __TEXT.__unwind_info: 0x5630
+  __TEXT.__eh_frame: 0x48ec
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x70
   __DATA_CONST.__objc_protolist: 0x398
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x74b8
+  __DATA_CONST.__objc_selrefs: 0x74f8
   __DATA_CONST.__objc_protorefs: 0x120
   __DATA_CONST.__objc_superrefs: 0x2a0
   __DATA_CONST.__objc_arraydata: 0x98
-  __DATA_CONST.__got: 0xfe8
+  __DATA_CONST.__got: 0xff0
   __AUTH_CONST.__const: 0x3938
   __AUTH_CONST.__cfstring: 0x3360
-  __AUTH_CONST.__objc_const: 0x11bb0
+  __AUTH_CONST.__objc_const: 0x11bb8
   __AUTH_CONST.__objc_intobj: 0x228
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__auth_got: 0x1548
   __AUTH.__objc_data: 0x2c68
-  __AUTH.__data: 0x1670
+  __AUTH.__data: 0x1680
   __DATA.__objc_ivar: 0xc20
-  __DATA.__data: 0x3480
+  __DATA.__data: 0x3484
   __DATA.__common: 0xa0
   __DATA_DIRTY.__objc_data: 0x4b0
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio

   - /System/Library/PrivateFrameworks/DeviceManagement.framework/DeviceManagement
   - /System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices
   - /System/Library/PrivateFrameworks/IconServices.framework/IconServices
+  - /System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/PhotosFormats.framework/PhotosFormats
   - /System/Library/PrivateFrameworks/PhotosUICore.framework/PhotosUICore

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 5745
-  Symbols:   7548
-  CStrings:  906
+  Functions: 5748
+  Symbols:   7556
+  CStrings:  913
 
Symbols:
+ -[QLPreviewCollection _currentItemCanEnterFullScreen]
+ -[QLPreviewCollection _itemViewControllerCanEnterFullScreen:]
+ -[QLPreviewController itemStore:canEnterFullScreenForItem:]
+ -[QLPreviewController mayMoveContentToUnmanagedDestination]
+ GCC_except_table123
+ GCC_except_table124
+ GCC_except_table159
+ GCC_except_table181
+ GCC_except_table182
+ GCC_except_table185
+ GCC_except_table203
+ GCC_except_table207
+ GCC_except_table92
+ GCC_except_table93
+ _OBJC_CLASS_$_MCProfileConnection
+ _OBJC_CLASS_$_MCProfileConnection$loadHelper_x8
+ ___swift_closure_destructor.105Tm
+ ___swift_closure_destructor.195Tm
+ ___swift_closure_destructor.89Tm
+ ___swift_closure_destructor.93Tm
+ _dlopenHelper$ManagedConfiguration
+ _dlopenHelperFlag$ManagedConfiguration
- GCC_except_table120
- GCC_except_table121
- GCC_except_table158
- GCC_except_table178
- GCC_except_table179
- GCC_except_table183
- GCC_except_table202
- GCC_except_table206
- GCC_except_table90
- GCC_except_table91
- ___swift_closure_destructor.102Tm
- ___swift_closure_destructor.192Tm
- ___swift_closure_destructor.86Tm
- ___swift_closure_destructor.90Tm
CStrings:
+ "/System/Library/PrivateFrameworks/ManagedConfiguration.framework/ManagedConfiguration"
+ "MDM : Managed content may not be moved to an unmanaged destination #PreviewController"
+ "Service side: ignoring %s, the preview collection is already gone"
+ "getPreviewCollectionUUIDWithCompletionHandler(completionHandler:)"
+ "preparePreviewCollectionForInvalidationWithCompletionHandler(completionHandler:)"
+ "setAllowInteractiveTransitions(_:)"
+ "setHostApplicationBundleIdentifier(_:)"
```
