## askpermissiond

> `/System/Library/PrivateFrameworks/AskPermission.framework/Support/askpermissiond`

```diff

-128.5.6.0.0
-  __TEXT.__text: 0x2599c
-  __TEXT.__auth_stubs: 0x5d0
-  __TEXT.__objc_stubs: 0x37e0
-  __TEXT.__objc_methlist: 0x1d34
-  __TEXT.__const: 0x50
-  __TEXT.__objc_methname: 0x4737
-  __TEXT.__oslogstring: 0x3195
-  __TEXT.__cstring: 0x1376
+129.0.17.0.0
+  __TEXT.__text: 0x281f4
+  __TEXT.__auth_stubs: 0x5f0
+  __TEXT.__objc_stubs: 0x3c20
+  __TEXT.__objc_methlist: 0x1e34
+  __TEXT.__const: 0x58
+  __TEXT.__objc_methname: 0x49db
+  __TEXT.__oslogstring: 0x375e
+  __TEXT.__cstring: 0x1452
   __TEXT.__objc_classname: 0x3db
-  __TEXT.__objc_methtype: 0xe32
-  __TEXT.__gcc_except_tab: 0x354
+  __TEXT.__objc_methtype: 0xe52
+  __TEXT.__gcc_except_tab: 0x394
   __TEXT.__dlopen_cstrs: 0x4a
-  __TEXT.__unwind_info: 0x5d0
-  __DATA_CONST.__auth_got: 0x2f8
-  __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0x898
-  __DATA_CONST.__cfstring: 0x1d40
+  __TEXT.__unwind_info: 0x610
+  __DATA_CONST.__auth_got: 0x308
+  __DATA_CONST.__got: 0x2f0
+  __DATA_CONST.__const: 0x960
+  __DATA_CONST.__cfstring: 0x1e20
   __DATA_CONST.__objc_classlist: 0x150
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0xb0
-  __DATA_CONST.__objc_intobj: 0x60
+  __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0x40
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA.__objc_const: 0x40a8
-  __DATA.__objc_selrefs: 0x1168
-  __DATA.__objc_ivar: 0x270
+  __DATA.__objc_const: 0x4228
+  __DATA.__objc_selrefs: 0x11f8
+  __DATA.__objc_ivar: 0x290
   __DATA.__objc_data: 0xd20
   __DATA.__data: 0x360
   __DATA.__bss: 0xc0

   - /System/Library/PrivateFrameworks/BiomeLibrary.framework/BiomeLibrary
   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/FamilyCircle.framework/FamilyCircle
+  - /System/Library/PrivateFrameworks/ScreenTimeCore.framework/ScreenTimeCore
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 31AC737F-5298-3F5C-9530-E373E7C27340
-  Functions: 585
-  Symbols:   200
-  CStrings:  1643
+  UUID: 180D476A-7D86-3417-87F3-8AA06A7FDDB5
+  Functions: 616
+  Symbols:   204
+  CStrings:  1706
 
Symbols:
+ _OBJC_CLASS_$_AMSBuyParams
+ _OBJC_CLASS_$_STExceptionApp
+ _dispatch_queue_attr_make_with_autorelease_frequency
+ _objc_retain_x9
CStrings:
+ "%{public}@: Buy params indicate we don’t need to submit an exception approval."
+ "%{public}@: Checking response for exception approval. Request ID: %{public}@"
+ "%{public}@: Error loading push environment value from bag: %{public}@"
+ "%{public}@: Error notifying Screen Time of the exception: %{public}@"
+ "%{public}@: Missing adamId, can’t submit exception approval."
+ "%{public}@: Missing bundle identifier, can’t submit exception approval."
+ "%{public}@: Missing created date, can’t submit exception approval."
+ "%{public}@: Missing rating value, can’t submit exception approval."
+ "%{public}@: Missing requestID, can’t submit exception approval."
+ "%{public}@: Missing requester DSID, can’t submit exception approval."
+ "%{public}@: Neither a result nor an error returned from bag."
+ "%{public}@: Notifying Screen Time of the exception. Bundle ID: %{public}@ | adamID: %llu | distributorID: %{public}@ | ratingValue: %llu | exceptionApp = %{public}@"
+ "%{public}@: Request is NOT an exception - nothing to submit."
+ "%{public}@: Response body is empty, can’t check for exception approval."
+ "%{public}@: Response body is empty, can’t find age rating value."
+ "%{public}@: Response buy params are empty, can’t check for exception approval."
+ "%{public}@: Response buy params are empty, can’t find age rating value."
+ "%{public}@: Response buy params missing `ageRatingValue`."
+ "%{public}@: Successfully notified Screen Time of the exception."
+ "%{public}@: Unexpected push environment value from bag: %{public}@"
+ "01:37:20"
+ "@\"<AMSBagProtocol>\""
+ "@\"AMSPromise\"24@?0@\"NSString\"8@\"NSError\"16"
+ "@16@?0@\"RequestStoreItem\"8"
+ "@216@0:8@16@24@32@40@48@56@64@72@80B88@92@100@108@116@124@132@140@148@156@164@172@180q188B196@200@208"
+ "May 25 2025"
+ "T@\"<AMSBagProtocol>\",&,N,V_bag"
+ "T@\"NSNumber\",&,N,V_ageRatingValue"
+ "T@\"NSNumber\",R,N,V_ageRatingValue"
+ "TB,N,V_isException"
+ "TB,R,N,V_isException"
+ "_ageRatingValue"
+ "_isException"
+ "_notifyScreenTimeIfNeededForApprovalForRequestWithID:response:"
+ "addExceptionWithCompletionHandler:"
+ "ageRatingValue"
+ "ageRatingValueFromBuyParams:"
+ "com.apple.AppStore"
+ "continueWithBlock:"
+ "development"
+ "effectiveNotificationEnvironmentPromise"
+ "initWithItemIdentifier:requestIdentifier:uniqueIdentifier:ageRating:ageRatingValue:approverDSID:requesterDSID:createdDate:modifiedDate:isException:itemBundleID:itemDesc:itemTitle:localizedPrice:previewURL:productType:productTypeName:productURL:offerName:requestString:requestSummary:priceSummary:status:suppressClientResume:starRating:thumbnailURLString:"
+ "initWithRequesterDSID:bundleIdentifier:adamID:distributorID:ratingValue:"
+ "initWithString:"
+ "isException"
+ "isExceptionRequest"
+ "isResponseAnExceptionRequest:"
+ "longLongValue"
+ "notificationEnvironment"
+ "numberWithLongLong:"
+ "overlayItem:"
+ "production"
+ "push-notifications/environment"
+ "setAgeRatingValue:"
+ "setIsException:"
+ "unsignedIntegerValue"
+ "unsignedLongLongValue"
+ "v24@?0@\"NSNumber\"8@\"NSError\"16"
+ "valuePromise"
- "06:37:31"
- "@196@0:8@16@24@32@40@48@56@64@72@80@88@96@104@112@120@128@136@144@152@160q168B176@180@188"
- "APSDevelopmentEnvironment"
- "Apr 19 2025"
- "initWithItemIdentifier:requestIdentifier:uniqueIdentifier:ageRating:approverDSID:requesterDSID:createdDate:modifiedDate:itemDesc:itemTitle:localizedPrice:previewURL:productType:productTypeName:productURL:offerName:requestString:requestSummary:priceSummary:status:suppressClientResume:starRating:thumbnailURLString:"

```
