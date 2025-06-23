## fileproviderctl

> `/usr/bin/fileproviderctl`

```diff

-3762.0.0.0.0
-  __TEXT.__text: 0xfb10
-  __TEXT.__auth_stubs: 0xb90
-  __TEXT.__objc_stubs: 0x1e20
-  __TEXT.__objc_methlist: 0x1f4
-  __TEXT.__const: 0x26a
-  __TEXT.__gcc_except_tab: 0x62c
+3833.0.0.502.1
+  __TEXT.__text: 0xfca0
+  __TEXT.__auth_stubs: 0xbb0
+  __TEXT.__objc_stubs: 0x1ea0
+  __TEXT.__objc_methlist: 0x344
+  __TEXT.__const: 0x27a
+  __TEXT.__gcc_except_tab: 0x634
   __TEXT.__cstring: 0x1d78
   __TEXT.__ustring: 0x65c
   __TEXT.__oslogstring: 0x129
-  __TEXT.__objc_classname: 0x4a
-  __TEXT.__objc_methname: 0x1851
-  __TEXT.__objc_methtype: 0x174
+  __TEXT.__objc_methname: 0x1c98
+  __TEXT.__objc_classname: 0x6e
+  __TEXT.__objc_methtype: 0x2ae
   __TEXT.__dlopen_cstrs: 0x94
   __TEXT.__swift5_typeref: 0x13b
   __TEXT.__swift5_capture: 0x54

   __TEXT.__swift_as_ret: 0x14
   __TEXT.__unwind_info: 0x460
   __TEXT.__eh_frame: 0x1b0
-  __DATA_CONST.__auth_got: 0x5d8
-  __DATA_CONST.__got: 0x2a0
+  __DATA_CONST.__auth_got: 0x5e8
+  __DATA_CONST.__got: 0x2a8
   __DATA_CONST.__auth_ptr: 0xe0
-  __DATA_CONST.__const: 0xfe8
+  __DATA_CONST.__const: 0xfc8
   __DATA_CONST.__cfstring: 0x18a0
-  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_catlist: 0x8
-  __DATA_CONST.__objc_protolist: 0x10
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
+  __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x2c8
-  __DATA.__objc_selrefs: 0x878
-  __DATA.__objc_ivar: 0x4
-  __DATA.__objc_data: 0xc0
-  __DATA.__data: 0x180
+  __DATA.__objc_const: 0x828
+  __DATA.__objc_selrefs: 0x948
+  __DATA.__objc_ivar: 0xc
+  __DATA.__objc_data: 0x110
+  __DATA.__data: 0x1e0
   __DATA.__common: 0x18
   __DATA.__bss: 0x340
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 06163785-589D-347D-9721-64587A62C098
-  Functions: 243
-  Symbols:   332
-  CStrings:  754
+  UUID: 564124EA-3620-3674-B13A-2B66CE7AE7F1
+  Functions: 247
+  Symbols:   331
+  CStrings:  804
 
Symbols:
+ _SANDBOX_CHECK_NOFOLLOW
+ _objc_alloc_init
+ _objc_getProperty
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "@\"NSOperationQueue\""
+ "@\"NSOperationQueue\"16@0:8"
+ "@\"NSSet\"16@0:8"
+ "@\"NSURL\""
+ "@\"NSURL\"16@0:8"
+ "NSFilePresenter"
+ "NoopFilePresenter"
+ "T@\"NSOperationQueue\",R,&"
+ "T@\"NSOperationQueue\",R,&,V_presentedItemOperationQueue"
+ "T@\"NSSet\",?,R"
+ "T@\"NSURL\",?,R,C"
+ "T@\"NSURL\",R,C"
+ "T@\"NSURL\",R,C,V_presentedItemURL"
+ "_presentedItemOperationQueue"
+ "_presentedItemURL"
+ "accommodatePresentedItemDeletionWithCompletionHandler:"
+ "accommodatePresentedItemEvictionWithCompletionHandler:"
+ "accommodatePresentedSubitemDeletionAtURL:completionHandler:"
+ "addFilePresenter:"
+ "initWithURL:"
+ "observedPresentedItemUbiquityAttributes"
+ "presentedItemDidChange"
+ "presentedItemDidChangeUbiquityAttributes:"
+ "presentedItemDidGainVersion:"
+ "presentedItemDidLoseVersion:"
+ "presentedItemDidMoveToURL:"
+ "presentedItemDidResolveConflictVersion:"
+ "presentedItemOperationQueue"
+ "presentedItemURL"
+ "presentedSubitemAtURL:didGainVersion:"
+ "presentedSubitemAtURL:didLoseVersion:"
+ "presentedSubitemAtURL:didMoveToURL:"
+ "presentedSubitemAtURL:didResolveConflictVersion:"
+ "presentedSubitemDidAppearAtURL:"
+ "presentedSubitemDidChangeAtURL:"
+ "primaryPresentedItemURL"
+ "relinquishPresentedItemToReader:"
+ "relinquishPresentedItemToWriter:"
+ "removeFilePresenter:"
+ "savePresentedItemChangesWithCompletionHandler:"
+ "setMaxConcurrentOperationCount:"
+ "v24@0:8@\"NSFileVersion\"16"
+ "v24@0:8@\"NSSet\"16"
+ "v24@0:8@\"NSURL\"16"
+ "v24@0:8@?<v@?@\"NSError\">16"
+ "v24@0:8@?<v@?@?<v@?>>16"
+ "v32@0:8@\"NSURL\"16@\"NSFileVersion\"24"
+ "v32@0:8@\"NSURL\"16@\"NSURL\"24"
+ "v32@0:8@\"NSURL\"16@?<v@?@\"NSError\">24"
+ "v32@0:8@16@?24"

```
