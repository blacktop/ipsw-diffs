## OnboardingPromptExtension

> `/System/Library/Frameworks/ContactsUI.framework/PlugIns/OnboardingPromptExtension.appex/OnboardingPromptExtension`

```diff

-1264.0.0.0.0
+1268.0.0.0.0
   __TEXT.__text: 0x40e8
   __TEXT.__auth_stubs: 0x630
   __TEXT.__objc_stubs: 0x320

   __DATA_CONST.__auth_got: 0x320
   __DATA_CONST.__got: 0xb0
   __DATA_CONST.__auth_ptr: 0x130
-  __DATA_CONST.__const: 0x90
+  __DATA_CONST.__const: 0xd0
   __DATA_CONST.__cfstring: 0xe0
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_protolist: 0x10

   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 89
-  Symbols:   83
+  Symbols:   91
   CStrings:  139
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd

```