## WritingToolsSuggestionsPlugin

> `/System/Library/Siri/DM/SiriSuggestions/Owners/WritingToolsSuggestionsPlugin.bundle/WritingToolsSuggestionsPlugin`

```diff

-110.2.0.0.0
+113.0.0.0.0
   __TEXT.__text: 0xc2c
   __TEXT.__auth_stubs: 0x210
   __TEXT.__const: 0x106

   __DATA_CONST.__auth_got: 0x108
   __DATA_CONST.__got: 0x28
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x100
+  __DATA_CONST.__const: 0x140
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x90

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
   Functions: 28
-  Symbols:   46
+  Symbols:   54
   CStrings:  5
 
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
