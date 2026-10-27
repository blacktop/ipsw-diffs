## CoreAI

> `/System/Library/Frameworks/CoreAI.framework/Versions/A/CoreAI`

```diff

-3600.83.2.14.1
+3605.6.4.0.0
   __TEXT.__text: 0x0
   __TEXT.__const: 0x32
-  __DATA_CONST.__const: 0x40
+  __DATA_CONST.__const: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/SubFrameworks/CoreAIDelegates.framework/Versions/A/CoreAIDelegates

   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswiftos.dylib
+  - /usr/lib/swift/libswiftsimd.dylib
   Functions: 0
-  Symbols:   8
+  Symbols:   10
   CStrings:  0
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftsimd
```
