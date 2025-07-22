## LocalAuthentication

> `/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`

```diff

-2005.0.40.0.0
-  __TEXT.__text: 0x35a50
+2005.0.49.0.0
+  __TEXT.__text: 0x35a5c
   __TEXT.__auth_stubs: 0xaa0
   __TEXT.__objc_methlist: 0x3648
   __TEXT.__const: 0x2d4

   __TEXT.__unwind_info: 0x12a8
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0x9c6
-  __TEXT.__objc_methname: 0x6de3
+  __TEXT.__objc_methname: 0x6dde
   __TEXT.__objc_methtype: 0x1c3a
   __TEXT.__objc_stubs: 0x4980
-  __DATA_CONST.__got: 0x530
+  __DATA_CONST.__got: 0x538
   __DATA_CONST.__const: 0x1bb8
   __DATA_CONST.__objc_classlist: 0x298
   __DATA_CONST.__objc_protolist: 0xf0

   - /usr/lib/swift/libswiftObservation.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  UUID: B6494BB5-C015-39F3-BE7E-57E7EC79A15C
+  UUID: 4BAC610F-DABC-3404-90D3-7F77A560071A
   Functions: 1453
-  Symbols:   5183
+  Symbols:   5184
   CStrings:  2216
 
Symbols:
+ _LACStorageOperationDataExchange
+ _objc_msgSend$isKeyAvailable:operation:
- _objc_msgSend$isKeyAvailableForDataExchange:
Functions:
~ -[LAStorage exchangeData:forKey:completionHandler:] : 740 -> 752
CStrings:
+ "Invalid uid: %u"
+ "isKeyAvailable:operation:"
- "Invalid uid: %d"
- "isKeyAvailableForDataExchange:"

```
