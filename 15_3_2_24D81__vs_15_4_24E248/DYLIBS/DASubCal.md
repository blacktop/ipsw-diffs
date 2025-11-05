## DASubCal

> `/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DASubCal.framework/Versions/A/DASubCal`

```diff

-2673.0.0.0.0
-  __TEXT.__text: 0x964c
+2673.5.2.0.0
+  __TEXT.__text: 0x9610
   __TEXT.__auth_stubs: 0x2d0
-  __TEXT.__objc_methlist: 0x944
+  __TEXT.__objc_methlist: 0xcf0
   __TEXT.__const: 0x60
   __TEXT.__cstring: 0x4ee
   __TEXT.__oslogstring: 0x91c
-  __TEXT.__unwind_info: 0x230
+  __TEXT.__unwind_info: 0x240
   __TEXT.__objc_classname: 0x17a
   __TEXT.__objc_methname: 0x2ab1
   __TEXT.__objc_methtype: 0xb30

   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xb80
+  __DATA_CONST.__objc_selrefs: 0xc88
   __DATA_CONST.__objc_superrefs: 0x10
   __AUTH_CONST.__auth_got: 0x170
   __AUTH_CONST.__const: 0x100
   __AUTH_CONST.__cfstring: 0x7e0
-  __AUTH_CONST.__objc_const: 0x2020
+  __AUTH_CONST.__objc_const: 0x1978
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0xa0
   __DATA.__data: 0x360

   - /System/Library/PrivateFrameworks/iCalendar.framework/Versions/A/iCalendar
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4D04F3A7-D63F-372B-993E-FD8E45B10359
-  Functions: 223
-  Symbols:   805
+  UUID: 30E55A1C-B05E-3005-B012-C4EB88B57307
+  Functions: 226
+  Symbols:   808
   CStrings:  802
 
Symbols:
+ +[SubCalURLRequest _cachedICSFilesDirectory].cold.1
+ -[SubCalAccount initWithBackingAccountInfo:].cold.1
+ -[SubCalURLRequest initWithURL:wasUserRequested:].cold.1
Functions:
~ -[SubCalAccount initWithBackingAccountInfo:] : 256 -> 240
~ -[SubCalAccount removeDataFromCalendar:forAccountChange:] : 1908 -> 1904
~ +[SubCalLocalDBHelper initializeSourceWithExternalId:inStore:needsSave:error:] : 252 -> 232
~ -[SubCalURLRequest initWithURL:wasUserRequested:] : 228 -> 176
~ -[SubCalURLRequest setDelegate:] : 120 -> 116
~ -[SubCalURLRequest _respondToChallenge:withCredential:noCredentialBehavior:completionHandler:] : 624 -> 516
~ +[SubCalURLRequest _cachedICSFilesDirectory] : 84 -> 68
~ -[SubCalDATask finishWithError:] : 156 -> 148
~ -[SubCalValidationTask _isInvalidVCalBeginningForData:] : 164 -> 168
~ -[SubCalValidationTask _searchForCalNameInConnectionData:] : 340 -> 336

```
