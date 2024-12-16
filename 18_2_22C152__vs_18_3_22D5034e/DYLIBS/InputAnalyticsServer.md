## InputAnalyticsServer

> `/System/Library/PrivateFrameworks/InputAnalyticsServer.framework/InputAnalyticsServer`

```diff

-64.218.1.0.0
-  __TEXT.__text: 0x29cd4
+64.223.0.0.0
+  __TEXT.__text: 0x2b544
   __TEXT.__auth_stubs: 0xa70
-  __TEXT.__objc_methlist: 0x1f14
+  __TEXT.__objc_methlist: 0x20e4
   __TEXT.__const: 0x1b0
-  __TEXT.__cstring: 0x2339
-  __TEXT.__oslogstring: 0x32e6
+  __TEXT.__cstring: 0x2439
+  __TEXT.__oslogstring: 0x36c6
   __TEXT.__gcc_except_tab: 0x2a8
   __TEXT.__swift5_typeref: 0xa7
   __TEXT.__swift5_capture: 0x88
   __TEXT.__constg_swiftt: 0x4c
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x7f8
+  __TEXT.__unwind_info: 0x858
   __TEXT.__eh_frame: 0x2e8
-  __TEXT.__objc_classname: 0x45e
-  __TEXT.__objc_methname: 0x51ab
-  __TEXT.__objc_methtype: 0x6fd
-  __TEXT.__objc_stubs: 0x3fa0
-  __DATA_CONST.__got: 0x9b0
-  __DATA_CONST.__const: 0x928
-  __DATA_CONST.__objc_classlist: 0x138
+  __TEXT.__objc_classname: 0x498
+  __TEXT.__objc_methname: 0x568c
+  __TEXT.__objc_methtype: 0x747
+  __TEXT.__objc_stubs: 0x4300
+  __DATA_CONST.__got: 0x9e0
+  __DATA_CONST.__const: 0x960
+  __DATA_CONST.__objc_classlist: 0x148
   __DATA_CONST.__objc_protolist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1190
+  __DATA_CONST.__objc_selrefs: 0x1280
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0xd0
-  __DATA_CONST.__objc_arraydata: 0x60
+  __DATA_CONST.__objc_superrefs: 0xe0
+  __DATA_CONST.__objc_arraydata: 0x68
   __AUTH_CONST.__auth_got: 0x548
   __AUTH_CONST.__auth_ptr: 0x90
-  __AUTH_CONST.__const: 0x788
-  __AUTH_CONST.__cfstring: 0x2380
-  __AUTH_CONST.__objc_const: 0x4008
+  __AUTH_CONST.__const: 0x7a8
+  __AUTH_CONST.__cfstring: 0x2500
+  __AUTH_CONST.__objc_const: 0x4388
   __AUTH_CONST.__objc_intobj: 0x570
-  __AUTH_CONST.__objc_arrayobj: 0x78
-  __AUTH.__objc_data: 0x4f0
+  __AUTH_CONST.__objc_arrayobj: 0x90
+  __AUTH.__objc_data: 0x590
   __AUTH.__data: 0x50
-  __DATA.__objc_ivar: 0x2c0
+  __DATA.__objc_ivar: 0x2f0
   __DATA.__data: 0x350
-  __DATA.__bss: 0x110
+  __DATA.__bss: 0x120
   __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__bss: 0x100
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 951
-  Symbols:   430
-  CStrings:  1581
+  Functions: 996
+  Symbols:   436
+  CStrings:  1667
 
Symbols:
+ _IAPayloadKeyGenmojiCreationFaceID
+ _IAPayloadKeyGenmojiCreationFaceIDList
+ _IAPayloadKeyGenmojiCreationNumItems
+ _IAPayloadKeyGenmojiCreationPickerType
+ _IAPayloadValueGenmojiCreationPickerTypePhoto
+ _IASignalGenmojiCreationFacePickerCarouselDismissed
CStrings:
+ "\x11\x11\x11\x11\x13A1"
+ " Second ImageGenerated received"
+ " Second ImageGenerationStarted received"
+ " Second ImageNotGenerated received while no active timer"
+ "@\"IASGenmojiFacePickerModel\""
+ "@\"IASGenmojiPeoplePickerModel\""
+ "FacePickerModel %{private}@ payload %{private}@ value was not a NSString. Got %{private}@"
+ "FacePickerModel %{private}@ payload %{private}@ was not a NSArray"
+ "FacePickerModel resetting on UpdatingFaces"
+ "H"
+ "IASGenmojiFacePickerModel"
+ "IASGenmojiPeoplePickerModel"
+ "IXAXPCProtocol"
+ "J"
+ "K"
+ "PeoplePickerModel %{private}@ payload %{private}@ value was not a NSString"
+ "PeoplePickerModel Did not update numPhotosInGrid to %{private}@ on %{private}@"
+ "PeoplePickerModel Got %{private}@ while panel is not up"
+ "PeoplePickerModel Ignoring %{private}@ while panel is not up"
+ "PeoplePickerModel Ignoring face picker signal %{private}@ while face picker is not up"
+ "PeoplePickerModel Ignoring numPhotosInGrid update to %lu on %{private}@ while panel is not up"
+ "PeoplePickerModel Ignoring selectedPickerType %{private}@ on %{private}@ while panel is not up"
+ "PeoplePickerModel Picker requested"
+ "PeoplePickerModel Updated numPhotosInGrid to %lu on %{private}@"
+ "PeoplePickerModel Updated selectedPickerType %{private}@"
+ "PeoplePickerModel received %{private}@ when face picker is not currently active"
+ "Q32@0:8d16@24"
+ "T@\"IASGenmojiFacePickerModel\",&,N,V_facePickerModel"
+ "T@\"IASGenmojiPeoplePickerModel\",&,N,V_peoplePicker"
+ "T@\"NSDate\",C,N,V_facePickerAppearTime"
+ "T@\"NSMutableDictionary\",&,N,V_carouselFaces"
+ "T@\"NSNumber\",C,N,V_didPersonalize"
+ "T@\"NSNumber\",C,N,V_numPhotosInGrid"
+ "T@\"NSNumber\",C,N,V_selectedFace"
+ "T@\"NSString\",&,N,V_selectedPickerType"
+ "T@\"NSUUID\",C,N,V_sessionID"
+ "TB,N,V_facePickerActive"
+ "TB,N,V_imageGenerationStartedSeen"
+ "TB,N,V_peoplePickerActive"
+ "TB,N,V_peoplePickerAppeared"
+ "[%{private}@] Detected end of panel session and terminating from state %{private}@ with signal %{private}@. Num images inserted: %lu"
+ "[%{private}@] End current model for initial image. Current=%f Total=%f"
+ "[%{private}@] Handled PeoplePicker signal %{private}@ with error %{private}@"
+ "_carouselFaces"
+ "_facePickerActive"
+ "_facePickerAppearTime"
+ "_facePickerModel"
+ "_imageGenerationStartedSeen"
+ "_numPhotosInGrid"
+ "_peoplePicker"
+ "_peoplePickerActive"
+ "_peoplePickerAppeared"
+ "_selectedFace"
+ "_selectedPickerType"
+ "_sessionID"
+ "carouselFaces"
+ "com.apple.StickerKit.StickerPickerService"
+ "distantFuture"
+ "facePickerActive"
+ "facePickerAppearTime"
+ "facePickerAppeared"
+ "facePickerModel"
+ "imageGenerationStartedSeen"
+ "numEmptyCarousel"
+ "numEmptyCarouselWithinTimeInterval:facePickerAppearTime:"
+ "numInserted"
+ "numOfferedCarousel"
+ "numPhotosAvailable"
+ "numPhotosInGrid"
+ "peoplePicker"
+ "peoplePickerActive"
+ "peoplePickerAppeared"
+ "removeObject:"
+ "selectedFace"
+ "selectedPickerType"
+ "sessionID"
+ "sessionId"
+ "setCarouselFaces:"
+ "setFacePickerActive:"
+ "setFacePickerAppearTime:"
+ "setFacePickerModel:"
+ "setImageGenerationStartedSeen:"
+ "setNumPhotosInGrid:"
+ "setPeoplePicker:"
+ "setPeoplePickerActive:"
+ "setPeoplePickerAppeared:"
+ "setSelectedFace:"
+ "setSelectedPickerType:"
+ "setSessionID:"
+ "shouldIgnoreSignal:"
+ "willHandleSignal:"
- "\x11\x11\x11\x11\x13A"
- "IAXPCProtocol"
- "T@\"NSNumber\",&,N,V_didPersonalize"
- "[%{private}@] Detected end of panel seession and terminating from state %{private}@ with signal %{private}@. Num images inserted: %lu"
- "[%{private}@] End current model for intiial image. Current=%f Total=%f"
- "[%{private}@] Latched isLowConfidenceFromCharacterPicker in %{private}@"

```
