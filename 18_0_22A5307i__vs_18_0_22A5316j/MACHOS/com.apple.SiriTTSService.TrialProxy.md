## com.apple.SiriTTSService.TrialProxy

> `/System/Library/PrivateFrameworks/SiriTTSService.framework/XPCServices/com.apple.SiriTTSService.TrialProxy.xpc/com.apple.SiriTTSService.TrialProxy`

```diff

-3400.104.1.0.0
+3400.107.1.0.0
   __TEXT.__text: 0x900
   __TEXT.__auth_stubs: 0x230
   __TEXT.__const: 0x70

   __DATA_CONST.__auth_got: 0x118
   __DATA_CONST.__got: 0x40
   __DATA_CONST.__auth_ptr: 0x10
-  __DATA_CONST.__const: 0x128
+  __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_protolist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x10

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftNaturalLanguage.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 18
-  Symbols:   49
+  Symbols:   50
   CStrings:  46
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftOSLog

```
