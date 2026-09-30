## AskToCore

> `/System/Library/PrivateFrameworks/AskToCore.framework/AskToCore`

```diff

-57.2.1.1.0
-  __TEXT.__text: 0x40fd4
+59.1.0.0.0
+  __TEXT.__text: 0x4100c
   __TEXT.__auth_stubs: 0x15b0
   __TEXT.__objc_methlist: 0x9c0
   __TEXT.__const: 0x3df0

   __TEXT.__unwind_info: 0x13f0
   __TEXT.__eh_frame: 0x1aa0
   __TEXT.__objc_classname: 0x3b
-  __TEXT.__objc_methname: 0xee5
+  __TEXT.__objc_methname: 0xee4
   __TEXT.__objc_methtype: 0x100
   __DATA_CONST.__got: 0x390
-  __DATA_CONST.__const: 0x218
+  __DATA_CONST.__const: 0x1f8
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: D89ACB63-6227-3607-BB3D-C959FB4F4ECA
+  UUID: FAC7B59C-ADD7-39D8-AA13-B41641864746
   Functions: 1691
-  Symbols:   898
+  Symbols:   890
   CStrings:  584
 
Symbols:
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_AskToCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_AskToCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_AskToCore
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_AskToCore
Functions:
~ sub_250f6498c -> sub_251b2d85c : 764 -> 760
~ sub_250f76218 -> sub_251b3f0e4 : 4168 -> 4172
~ sub_250f787c8 -> sub_251b41698 : 5568 -> 5556
~ sub_250f7d6c8 -> sub_251b4658c : 536 -> 560
~ sub_250f7f254 -> sub_251b48130 : 312 -> 360
~ sub_250f86684 -> sub_251b4f590 : 188 -> 184
CStrings:
+ "payloadForSendRequest(question:recipientGroup:clientPayload:shouldValidateSendDestinations:)"
+ "payloadForSendRequestWithQuestion:recipientGroup:clientPayload:shouldValidateSendDestinations:completionHandler:"
+ "shouldValidateSendDestinations"
- "payloadForSendRequest(question:recipientGroup:clientPayload:shouldValidateSendDestionations:)"
- "payloadForSendRequestWithQuestion:recipientGroup:clientPayload:shouldValidateSendDestionations:completionHandler:"
- "shouldValidateSendDestionations"

```
