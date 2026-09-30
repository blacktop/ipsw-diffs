## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`

```diff

-90.0.0.0.0
-  __TEXT.__text: 0x3b554
+94.0.0.0.0
+  __TEXT.__text: 0x3ca9c
   __TEXT.__auth_stubs: 0xc80
-  __TEXT.__objc_methlist: 0x30a4
+  __TEXT.__objc_methlist: 0x3254
   __TEXT.__const: 0x250
-  __TEXT.__cstring: 0x2cd9
-  __TEXT.__oslogstring: 0x4076
+  __TEXT.__cstring: 0x2db9
+  __TEXT.__oslogstring: 0x4166
   __TEXT.__gcc_except_tab: 0x2f4
   __TEXT.__swift5_typeref: 0x10d
   __TEXT.__swift5_capture: 0x88

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x1c
   __TEXT.__swift_as_ret: 0x1c
-  __TEXT.__unwind_info: 0xb20
+  __TEXT.__unwind_info: 0xb48
   __TEXT.__eh_frame: 0x2e8
-  __TEXT.__objc_classname: 0x727
-  __TEXT.__objc_methname: 0x727a
+  __TEXT.__objc_classname: 0x77c
+  __TEXT.__objc_methname: 0x7583
   __TEXT.__objc_methtype: 0xaf7
-  __TEXT.__objc_stubs: 0x5720
-  __DATA_CONST.__got: 0xd70
-  __DATA_CONST.__const: 0xbe0
-  __DATA_CONST.__objc_classlist: 0x1f8
+  __TEXT.__objc_stubs: 0x5a80
+  __DATA_CONST.__got: 0xd88
+  __DATA_CONST.__const: 0xca0
+  __DATA_CONST.__objc_classlist: 0x210
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x18a8
+  __DATA_CONST.__objc_selrefs: 0x1970
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x168
+  __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0xb8
   __AUTH_CONST.__auth_got: 0x650
-  __AUTH_CONST.__const: 0xaa0
-  __AUTH_CONST.__cfstring: 0x3020
-  __AUTH_CONST.__objc_const: 0x5960
-  __AUTH_CONST.__objc_intobj: 0xaf8
+  __AUTH_CONST.__const: 0xae0
+  __AUTH_CONST.__cfstring: 0x3200
+  __AUTH_CONST.__objc_const: 0x5ce0
+  __AUTH_CONST.__objc_intobj: 0xb88
   __AUTH_CONST.__objc_arrayobj: 0xf0
-  __AUTH.__objc_data: 0x798
+  __AUTH.__objc_data: 0x888
   __AUTH.__data: 0x28
-  __DATA.__objc_ivar: 0x3f0
+  __DATA.__objc_ivar: 0x414
   __DATA.__data: 0x3b0
-  __DATA.__bss: 0x120
+  __DATA.__bss: 0x140
   __DATA_DIRTY.__objc_data: 0xc58
   __DATA_DIRTY.__data: 0x48
   __DATA_DIRTY.__bss: 0x200

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D6741FE3-83DC-3620-A452-2ADD9FF02B8F
-  Functions: 1378
+  UUID: 74D266E8-B64C-3278-862F-56638D38A326
+  Functions: 1414
   Symbols:   556
-  CStrings:  2497
+  CStrings:  2575
 
Symbols:
+ _IAPayloadKeyImageGenerationImageIndex
+ _IASignalImageGenerationImageInserted
+ _IASignalImageGenerationPreviewGenerationStarted
+ _OBJC_METACLASS_$_NSMutableDictionary
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
CStrings:
+ "FeedbackServiceActive"
+ "FeedbackUIPresented"
+ "IASImageGenerationDetailsEvent"
+ "IASImageGenerationImageDetails"
+ "IASSafeMutableDictionary"
+ "IASSafeMutableDictionary tried to remove object for nil key"
+ "IASSafeMutableDictionary tried to set key %{sensitive}@ to nil"
+ "IASSafeMutableDictionary tried to set nil key to nil object"
+ "IASSafeMutableDictionary tried to set nil key to object %{sensitive}@"
+ "Index inconsistent"
+ "IntentsCached"
+ "SmartReplySelected"
+ "T@\"NSMutableArray\",&,N,V_imageDetails"
+ "T@\"NSMutableDictionary\",&,N,V_internalDictionary"
+ "TB,N,V_isCopied"
+ "TB,N,V_isInserted"
+ "TB,N,V_isSaved"
+ "TB,N,V_isShared"
+ "TB,N,V_isViewed"
+ "TQ,N,V_currentImageIndex"
+ "TQ,N,V_currentPromptIndex"
+ "TQ,N,V_numRetry"
+ "Y"
+ "[%{private}@] Enumerating details event for image %lu"
+ "_currentImageIndex"
+ "_currentPromptIndex"
+ "_imageDetails"
+ "_internalDictionary"
+ "_isCopied"
+ "_isInserted"
+ "_isSaved"
+ "_isShared"
+ "_isViewed"
+ "_numRetry"
+ "addNewImage"
+ "clientSideSessionErrors"
+ "com.apple.inputAnalytics.imageGenerationDetails"
+ "currentImageIndex"
+ "currentPromptIndex"
+ "enumerateImageLevelAnalytics"
+ "enumeratePromptLevelAnalytics"
+ "enumerateSubstringsInRange:options:usingBlock:"
+ "imageDetails"
+ "internalDictionary"
+ "isCopied"
+ "isInserted"
+ "isSaved"
+ "isShared"
+ "isViewed"
+ "keyEnumerator"
+ "modelLanguage"
+ "previewIndex"
+ "promptIndex"
+ "setCurrentImageIndex:"
+ "setCurrentPromptIndex:"
+ "setImageDetails:"
+ "setInternalDictionary:"
+ "setIsCopied:"
+ "setIsInserted:"
+ "setIsSaved:"
+ "setIsShared:"
+ "setIsViewed:"
+ "setNumRetry:"
+ "updateImageDetailsIfGeneratingWithGenerationStatus:"
+ "v56@?0@\"NSString\"8{_NSRange=QQ}16{_NSRange=QQ}32^B48"
- "FinalImageGenerating"
- "InitialPreviewGenerated"
- "InitialPreviewGenerating"
- "PreviewGeneratedFailed"
- "SubsequentPreviewGenerated"
- "TB,N,V_didGenerationStart"
- "[%{private}@] state %{private}@ with signal %{private}@"
- "_didGenerationStart"
- "didGenerationStart"
- "setDidGenerationStart:"

```
