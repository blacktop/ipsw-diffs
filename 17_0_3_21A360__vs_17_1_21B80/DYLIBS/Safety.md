## Safety

> `/System/Library/Health/FeedItemPlugins/Safety.healthplugin/Safety`

```diff

-4146.0.1.7.0
+4146.1.11.3.0
   __TEXT.__text: 0x830bc
   __TEXT.__auth_stubs: 0x2730
   __TEXT.__objc_methlist: 0x610

   __TEXT.__objc_methtype: 0x4cf
   __TEXT.__objc_stubs: 0x440
   __DATA_CONST.__got: 0x7a0
-  __DATA_CONST.__const: 0x148
+  __DATA_CONST.__const: 0x150
   __DATA_CONST.__objc_classlist: 0x138
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0xd8

   - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
+  - /usr/lib/swift/libswiftCoreML.dylib
   - /usr/lib/swift/libswiftCoreMedia.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 9C81BE16-DD44-3A2A-ACB4-9699D09AE8E7
+  UUID: 556EE312-82B1-36EA-9EC0-73E5BAB570D1
   Functions: 2601
-  Symbols:   278
+  Symbols:   279
   CStrings:  1002
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftCoreML

```
