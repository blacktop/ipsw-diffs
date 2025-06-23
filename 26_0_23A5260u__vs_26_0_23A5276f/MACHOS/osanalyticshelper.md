## osanalyticshelper

> `/System/Library/CoreServices/osanalyticshelper`

```diff

-912.0.0.0.0
+917.0.0.0.0
   __TEXT.__text: 0x144f8
   __TEXT.__auth_stubs: 0xd40
   __TEXT.__objc_stubs: 0x2a40

   __DATA_CONST.__auth_got: 0x6b8
   __DATA_CONST.__got: 0x4f0
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x9c8
+  __DATA_CONST.__const: 0x9a8
   __DATA_CONST.__cfstring: 0x1ac0
   __DATA_CONST.__objc_classlist: 0x78
   __DATA_CONST.__objc_protolist: 0x18

   - /System/Library/PrivateFrameworks/BiomeStreams.framework/BiomeStreams
   - /System/Library/PrivateFrameworks/Categories.framework/Categories
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
+  - /System/Library/PrivateFrameworks/CoreDiagnostics.framework/CoreDiagnostics
   - /System/Library/PrivateFrameworks/CoreDuet.framework/CoreDuet
   - /System/Library/PrivateFrameworks/CoreSymbolication.framework/CoreSymbolication
   - /System/Library/PrivateFrameworks/CrashReporterSupport.framework/CrashReporterSupport

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 7DC95542-4F4D-33EE-9F2C-BF28AE4D42FB
+  UUID: 289BF3BC-2005-3F9D-88E8-AE35D7B75C3A
   Functions: 324
-  Symbols:   399
+  Symbols:   395
   CStrings:  1238
 
Symbols:
+ _OBJC_CLASS_$_CDStackshotReport
+ _OBJC_CLASS_$_CDTerminatingStackshotReport
- _OBJC_CLASS_$_OSACrackShotReport
- _OBJC_CLASS_$_OSAStackShotReport
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3

```
