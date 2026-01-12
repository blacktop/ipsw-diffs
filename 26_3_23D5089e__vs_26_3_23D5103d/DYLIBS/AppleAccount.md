## AppleAccount

> `/System/Library/PrivateFrameworks/AppleAccount.framework/AppleAccount`

```diff

-1037.325.1.0.0
-  __TEXT.__text: 0xeb984
+1037.325.2.0.0
+  __TEXT.__text: 0xeb978
   __TEXT.__auth_stubs: 0x1180
   __TEXT.__objc_methlist: 0xaeec
   __TEXT.__const: 0x23e0

   __TEXT.__unwind_info: 0x2fa0
   __TEXT.__eh_frame: 0x3e8
   __TEXT.__objc_classname: 0x1fc6
-  __TEXT.__objc_methname: 0x15e0a
+  __TEXT.__objc_methname: 0x15e12
   __TEXT.__objc_methtype: 0x30f8
   __TEXT.__objc_stubs: 0xc440
   __DATA_CONST.__got: 0xd80

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 2F793D47-F772-3573-8A6C-E5916866DC11
+  UUID: 1D040687-C811-36AC-B73E-076ADB42771B
   Functions: 4946
   Symbols:   16348
   CStrings:  9026
Symbols:
+ _objc_msgSend$initWithEventName:eventCategory:initData:altDSID:
- _objc_msgSend$initWithEventName:eventCategory:initData:
Functions:
~ +[AAFAnalyticsEvent(AppleAccount) analyticsEventWithName:altDSID:flowID:] : 468 -> 456
CStrings:
+ "initWithEventName:eventCategory:initData:altDSID:"
- "initWithEventName:eventCategory:initData:"

```
