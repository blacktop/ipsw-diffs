## AdID

> `/System/Library/PrivateFrameworks/AdID.framework/AdID`

```diff

-637.2.1.0.0
-  __TEXT.__text: 0x19760
+637.2.2.0.0
+  __TEXT.__text: 0x19868
   __TEXT.__auth_stubs: 0x650
   __TEXT.__objc_methlist: 0x10bc
   __TEXT.__const: 0x60
   __TEXT.__gcc_except_tab: 0x6e8
-  __TEXT.__cstring: 0x6c35
+  __TEXT.__cstring: 0x6cf8
   __TEXT.__unwind_info: 0x5b8
   __TEXT.__objc_classname: 0x1ba
   __TEXT.__objc_methname: 0x401b

   __DATA_CONST.__objc_arraydata: 0x18
   __AUTH_CONST.__auth_got: 0x338
   __AUTH_CONST.__const: 0x280
-  __AUTH_CONST.__cfstring: 0x43a0
+  __AUTH_CONST.__cfstring: 0x4400
   __AUTH_CONST.__objc_const: 0x2600
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: A0A6AAA8-BAB0-32A9-B96A-86F7F50ED8DE
+  UUID: 4A44D4D2-F68E-30A4-BC08-91E6F6ABA971
   Functions: 419
   Symbols:   1976
-  CStrings:  1958
+  CStrings:  1964
 
Functions:
~ -[ADSegmentDataManager parseBirthYearFromSegmentData:] : 312 -> 576
CStrings:
+ "JSON was valid, but did not contain the expected structure for birth year."
+ "segmentData is nil or empty. Unable to parse."
+ "segmentData is not in JSON format. Unable to parse segmentData. Error: %@"

```
