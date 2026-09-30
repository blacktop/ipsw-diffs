## GenerativeModelsDiagnostics

> `/System/Library/PrivateFrameworks/GenerativeExperiencesRuntime.framework/Versions/A/GenerativeModelsDiagnostics.appex/Contents/MacOS/GenerativeModelsDiagnostics`

```diff

-119.0.0.0.0
+128.100.0.0.0
   __TEXT.__text: 0x41c4
   __TEXT.__auth_stubs: 0x690
   __TEXT.__objc_methlist: 0x2c

   __DATA_CONST.__auth_got: 0x348
   __DATA_CONST.__got: 0x70
   __DATA_CONST.__auth_ptr: 0x90
-  __DATA_CONST.__const: 0x148
+  __DATA_CONST.__const: 0x160
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x70

   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
+  - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswiftos.dylib
   Functions: 120
-  Symbols:   69
+  Symbols:   72
   CStrings:  25
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftMetal
+ __swift_FORCE_LOAD_$_swiftQuartzCore
+ __swift_FORCE_LOAD_$_swiftUniformTypeIdentifiers

```
