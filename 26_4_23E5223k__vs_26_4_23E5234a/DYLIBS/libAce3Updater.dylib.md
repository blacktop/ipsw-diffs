## libAce3Updater.dylib

> `/usr/lib/updaters/libAce3Updater.dylib`

```diff

-1345.100.165.0.0
-  __TEXT.__text: 0x1f00c
-  __TEXT.__auth_stubs: 0x860
+1345.102.1.0.0
+  __TEXT.__text: 0x1f19c
+  __TEXT.__auth_stubs: 0x880
   __TEXT.__objc_methlist: 0x3b4
-  __TEXT.__cstring: 0x5e5a
+  __TEXT.__cstring: 0x5ec6
   __TEXT.__const: 0x200
   __TEXT.__oslogstring: 0x7
   __TEXT.__unwind_info: 0x7a8
   __TEXT.__objc_classname: 0x84
-  __TEXT.__objc_methname: 0xa27
+  __TEXT.__objc_methname: 0xa38
   __TEXT.__objc_methtype: 0x852
-  __TEXT.__objc_stubs: 0x980
+  __TEXT.__objc_stubs: 0x9c0
   __DATA_CONST.__got: 0xc0
   __DATA_CONST.__const: 0x5e0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2b8
+  __DATA_CONST.__objc_selrefs: 0x2c0
   __DATA_CONST.__objc_superrefs: 0x18
-  __AUTH_CONST.__auth_got: 0x438
-  __AUTH_CONST.__cfstring: 0xf20
+  __AUTH_CONST.__auth_got: 0x448
+  __AUTH_CONST.__cfstring: 0xfc0
   __AUTH_CONST.__objc_const: 0x918
   __AUTH.__objc_data: 0x190
   __DATA.__objc_ivar: 0x98

   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
+  - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libcompression.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 98854C54-3E03-39EB-B4B0-0FE603818E89
+  UUID: 6207BE9B-080B-3EBF-9CB3-537AD76D84B8
   Functions: 955
-  Symbols:   1670
-  CStrings:  991
+  Symbols:   1674
+  CStrings:  1002
 
Symbols:
+ _MGCopyAnswer
+ _objc_msgSend$setUpdaterMode:
+ _objc_msgSend$unsignedIntValue
+ _objc_release_x27
Functions:
~ -[Ace3UpdateController createUpdaterInstanceFor:helper:options:] : 308 -> 708
CStrings:
+ "Board ID: %@"
+ "BoardId"
+ "Chip ID: %@"
+ "Is Display & has Preflight Tickets - setting to Stage 1"
+ "Options Passed: %@"
+ "unsignedIntValue"

```
