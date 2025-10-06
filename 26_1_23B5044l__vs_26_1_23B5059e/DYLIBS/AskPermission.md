## AskPermission

> `/System/Library/PrivateFrameworks/AskPermission.framework/AskPermission`

```diff

-129.1.1.0.0
-  __TEXT.__text: 0x9874
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__objc_methlist: 0xa0c
-  __TEXT.__const: 0xea
+129.1.6.0.0
+  __TEXT.__text: 0xa464
+  __TEXT.__auth_stubs: 0x730
+  __TEXT.__objc_methlist: 0xa9c
+  __TEXT.__const: 0xfa
   __TEXT.__gcc_except_tab: 0x37c
-  __TEXT.__cstring: 0x788
-  __TEXT.__oslogstring: 0xaa1
+  __TEXT.__cstring: 0x7a8
+  __TEXT.__oslogstring: 0xc7d
   __TEXT.__swift5_typeref: 0x94
   __TEXT.__swift5_capture: 0x80
   __TEXT.__swift_as_entry: 0x14
   __TEXT.__swift_as_ret: 0x14
-  __TEXT.__unwind_info: 0x350
+  __TEXT.__unwind_info: 0x368
   __TEXT.__eh_frame: 0x1f8
   __TEXT.__objc_classname: 0x169
-  __TEXT.__objc_methname: 0x19d0
-  __TEXT.__objc_methtype: 0x556
-  __TEXT.__objc_stubs: 0x1080
+  __TEXT.__objc_methname: 0x1bb6
+  __TEXT.__objc_methtype: 0x6af
+  __TEXT.__objc_stubs: 0x1140
   __DATA_CONST.__got: 0x118
-  __DATA_CONST.__const: 0x418
+  __DATA_CONST.__const: 0x470
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x718
+  __DATA_CONST.__objc_selrefs: 0x748
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x3a0
+  __AUTH_CONST.__auth_got: 0x3a8
   __AUTH_CONST.__const: 0x1a8
-  __AUTH_CONST.__cfstring: 0xb60
-  __AUTH_CONST.__objc_const: 0x1090
+  __AUTH_CONST.__cfstring: 0xba0
+  __AUTH_CONST.__objc_const: 0x10c0
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x2d0

   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 2B7009D4-6757-3A4E-BD7A-39DE2AC8B78E
-  Functions: 230
-  Symbols:   950
-  CStrings:  623
+  UUID: 4E00E6B7-4E48-3D65-A272-92E2118F0001
+  Functions: 238
+  Symbols:   977
+  CStrings:  646
 
Symbols:
+ +[APRequestHandler addExceptionRequestWithUUID:type:title:message:bundleIdentifier:adamID:distributorID:ageRatingValue:preApprove:postApprove:preDecline:postDecline:responseBundleIdentifier:customData:withCompletion:]
+ +[APRequestHandler getExceptionRequestWithDistributorIdentifier:completionHandler:]
+ +[APRequestHandler getExceptionRequestWithUniqueIdentifier:completionHandler:]
+ +[APRequestHandler getExceptionRequestsWithBundleIdentifier:completionHandler:]
+ +[APRequestHandler getExceptionRequestsWithCompletion:]
+ +[APRequestHandler updateExceptionRequestWithUniqueIdentifier:action:completionHandler:]
+ GCC_except_table18
+ GCC_except_table20
+ GCC_except_table22
+ GCC_except_table25
+ ___217+[APRequestHandler addExceptionRequestWithUUID:type:title:message:bundleIdentifier:adamID:distributorID:ageRatingValue:preApprove:postApprove:preDecline:postDecline:responseBundleIdentifier:customData:withCompletion:]_block_invoke
+ ___44-[APConnectionNotifier _newRemoteConnection]_block_invoke.89
+ ___55+[APRequestHandler getExceptionRequestsWithCompletion:]_block_invoke
+ ___block_descriptor_40_e8_32bs_e17_v16?0"NSArray"8ls32l8
+ ___block_descriptor_48_e8_32bs_e20_v20?0B8"NSError"12ls32l8
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftCoreImage_$_AskPermission
+ _objc_msgSend$addExceptionRequestWithUUID:type:title:message:bundleIdentifier:adamID:distributorID:ageRatingValue:preApprove:postApprove:preDecline:postDecline:responseBundleIdentifier:customData:withCompletion:
+ _objc_msgSend$getExceptionRequestWithDistributorIdentifier:completionHandler:
+ _objc_msgSend$getExceptionRequestWithUniqueIdentifier:completionHandler:
+ _objc_msgSend$getExceptionRequestsWithBundleIdentifier:completionHandler:
+ _objc_msgSend$getExceptionRequestsWithCompletion:
+ _objc_msgSend$updateExceptionRequestWithUniqueIdentifier:action:completionHandler:
+ _objc_retain_x6
- GCC_except_table10
- GCC_except_table12
- GCC_except_table14
- GCC_except_table17
- ___44-[APConnectionNotifier _newRemoteConnection]_block_invoke.79
CStrings:
+ "%{public}@: Adding Exception Request: %@, adamID: %@, distributor: %@, ageRatingValue: %@"
+ "%{public}@: Exception Request Added Successfully"
+ "%{public}@: Failed to Add Exception Request: %@"
+ "%{public}@: Getting Exception Requests for BundleID: %@"
+ "%{public}@: Getting Exception Requests for DistributorID: %@"
+ "%{public}@: Getting Exception Requests for UniqueID: %@"
+ "%{public}@: Getting Exception Requests."
+ "%{public}@: Updating Exception Request with UniqueID: %@ action: %ld - (%@)"
+ "Approve"
+ "Decline"
+ "addExceptionRequestWithUUID:type:title:message:bundleIdentifier:adamID:distributorID:ageRatingValue:preApprove:postApprove:preDecline:postDecline:responseBundleIdentifier:customData:withCompletion:"
+ "getExceptionRequestWithDistributorIdentifier:completionHandler:"
+ "getExceptionRequestWithUniqueIdentifier:completionHandler:"
+ "getExceptionRequestsWithBundleIdentifier:completionHandler:"
+ "getExceptionRequestsWithCompletion:"
+ "updateExceptionRequestWithUniqueIdentifier:action:completionHandler:"
+ "v136@0:8@\"NSUUID\"16q24@\"NSString\"32@\"NSString\"40@\"NSString\"48@\"NSString\"56@\"NSString\"64@\"NSNumber\"72@\"NSString\"80@\"NSString\"88@\"NSString\"96@\"NSString\"104@\"NSString\"112@\"NSData\"120@?<v@?B@\"NSError\">128"
+ "v136@0:8@16q24@32@40@48@56@64@72@80@88@96@104@112@120@?128"
+ "v20@?0B8@\"NSError\"12"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSArray\">24"
+ "v32@0:8@\"NSString\"16@?<v@?@\"NSDictionary\">24"

```
