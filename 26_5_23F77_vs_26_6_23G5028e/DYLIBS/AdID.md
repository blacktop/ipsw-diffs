## AdID

> `/System/Library/PrivateFrameworks/AdID.framework/AdID`

```diff

-637.5.1.0.0
-  __TEXT.__text: 0x1b044
+637.6.2.0.0
+  __TEXT.__text: 0x1b2dc
   __TEXT.__auth_stubs: 0x620
   __TEXT.__objc_methlist: 0x10bc
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x660
-  __TEXT.__cstring: 0x6d60
-  __TEXT.__unwind_info: 0x638
+  __TEXT.__cstring: 0x6e81
+  __TEXT.__unwind_info: 0x640
   __TEXT.__objc_classname: 0x1ba
-  __TEXT.__objc_methname: 0x401b
+  __TEXT.__objc_methname: 0x40d0
   __TEXT.__objc_methtype: 0x6f2
-  __TEXT.__objc_stubs: 0x4260
+  __TEXT.__objc_stubs: 0x4320
   __DATA_CONST.__got: 0x3d0
-  __DATA_CONST.__const: 0xaa0
+  __DATA_CONST.__const: 0xac8
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x13a0
+  __DATA_CONST.__objc_selrefs: 0x13d0
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x320
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x4440
-  __AUTH_CONST.__objc_const: 0x2600
+  __AUTH_CONST.__cfstring: 0x4520
+  __AUTH_CONST.__objc_const: 0x2620
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_doubleobj: 0x10

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AE086028-8A9F-3557-9C0B-226732A82B70
-  Functions: 419
-  Symbols:   1973
-  CStrings:  1969
+  UUID: 8981C3A2-4628-3E74-B089-DE4B5D09E271
+  Functions: 420
+  Symbols:   1982
+  CStrings:  1989
 
Symbols:
+ GCC_except_table24
+ ___83-[ADSegmentDataManager handleJingleSegmentResponse:activeRecord:completionHandler:]_block_invoke
+ ___block_descriptor_56_e8_32s40s48bs_e8_v12?0B8ls32l8s40l8s48l8
+ _objc_msgSend$isEducationManagedAccount
+ _objc_msgSend$isEnterpriseManagedAccount
+ _objc_msgSend$isManagedEducationaliTunesAccount
+ _objc_msgSend$isManagedEnterpriseiTunesAccount
+ _objc_msgSend$setIsEducationManagedAccount:
+ _objc_msgSend$setIsEnterpriseManagedAccount:
- GCC_except_table19
Functions:
~ -[DSIDRecord(Private) isEqual:] : 984 -> 1040
~ -[ADSegmentDataManager retrieveSegmentData:forceSegments:ignoreTimestamps:completionHandler:] : 928 -> 992
~ -[ADSegmentDataManager handleJingleSegmentResponse:activeRecord:completionHandler:] : 1704 -> 1928
+ ___83-[ADSegmentDataManager handleJingleSegmentResponse:activeRecord:completionHandler:]_block_invoke
~ -[ADSegmentDataManager handleSuccessfulJingleSegmentResponse:dsidRecord:completionHandler:] : 3680 -> 3724
CStrings:
+ "No retry scheduled."
+ "Scheduling reconcile retry backoff."
+ "Scheduling retry after 1601 weak token reauthentication."
+ "[%@ retrieveSegmentData]: Reauthentication after 1601 %@. %@"
+ "[%@ retrieveSegmentData]: Received weak token 1601 after retry. No action is possible by iAd, the user must log into the account."
+ "[%@ retrieveSegmentData]: Received weak token 1601. Reauthenticating."
+ "[%@]: The current account is: EDU: %d. Managed: %d. ManagedEdu: %d. ManagedEnterprise: %d. U13: %d. T13: %d. U18: %d. Unknown Age: %d. Proto U13: %d. Proto Teen: %d"
+ "failed"
+ "isEducationManagedAccount"
+ "isEnterpriseManagedAccount"
+ "isManagedEducationaliTunesAccount"
+ "isManagedEnterpriseiTunesAccount"
+ "setIsEducationManagedAccount:"
+ "setIsEnterpriseManagedAccount:"
+ "succeeded"
- "[%@ retrieveSegmentData]: The Jingle Weak Token for this user has expired. No action is possible by iAd, the user must log into the account."
- "[%@]: The current account is: EDU: %d. Managed: %d. U13: %d. T13: %d. U18: %d. Unknown Age: %d. Proto U13: %d. Proto Teen: %d"

```
