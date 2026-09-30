## AdID

> `/System/Library/PrivateFrameworks/AdID.framework/AdID`

```diff

-637.4.6.0.0
-  __TEXT.__text: 0x1af78
+637.4.7.0.0
+  __TEXT.__text: 0x1b044
   __TEXT.__auth_stubs: 0x620
   __TEXT.__objc_methlist: 0x10bc
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x660
-  __TEXT.__cstring: 0x6cf8
+  __TEXT.__cstring: 0x6d60
   __TEXT.__unwind_info: 0x638
   __TEXT.__objc_classname: 0x1ba
   __TEXT.__objc_methname: 0x401b

   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x320
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x4400
+  __AUTH_CONST.__cfstring: 0x4440
   __AUTH_CONST.__objc_const: 0x2600
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: E6C8C3EE-96FC-32F9-8F9C-511ED1871CA9
+  UUID: 06103FF2-1011-3D0D-8677-46C6629D5437
   Functions: 419
   Symbols:   1973
-  CStrings:  1964
+  CStrings:  1969
 
Symbols:
+ ___block_literal_global.297
+ ___block_literal_global.94
- ___block_literal_global.290
- ___block_literal_global.86
Functions:
~ ___37-[ADAdTrackingSchedulingManager init]_block_invoke_2 : 916 -> 1044
~ -[ADSegmentDataManager handleSuccessfulJingleSegmentResponse:dsidRecord:completionHandler:] : 3604 -> 3680
CStrings:
+ "AdPrivacyD launched by com.apple.ap.rotatedAnonymousIdRotated"
+ "[%@]: Personalized Ads is OFF and the RAID has rotated since last fetch."
+ "[%@]: Personalized Ads is OFF and we have not applied noise before OR RAID has rotated since last fetch. Running noise calculation now."
+ "com.apple.ap.rotatedAnonymousIdRotated"
+ "raidRotated"
- "[%@]: Personalized Ads is OFF and we have already calculated noise before. No noise applied and basel year is honored."
- "[%@]: Personalized Ads is OFF and we have not applied noise before. Running noise calculation now."

```
