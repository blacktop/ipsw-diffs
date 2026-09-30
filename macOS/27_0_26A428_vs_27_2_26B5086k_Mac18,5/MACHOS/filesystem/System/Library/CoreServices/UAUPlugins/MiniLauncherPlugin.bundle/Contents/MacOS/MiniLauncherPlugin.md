## MiniLauncherPlugin

> `/System/Library/CoreServices/UAUPlugins/MiniLauncherPlugin.bundle/Contents/MacOS/MiniLauncherPlugin`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-7548.0.0.0.0
-  __TEXT.__text: 0x10ec8
-  __TEXT.__auth_stubs: 0x810
-  __TEXT.__objc_stubs: 0x2500
-  __TEXT.__objc_methlist: 0x111c
-  __TEXT.__gcc_except_tab: 0x180
-  __TEXT.__cstring: 0x2491
+7549.0.0.0.0
+  __TEXT.__text: 0x11764
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__objc_stubs: 0x2600
+  __TEXT.__objc_methlist: 0x118c
+  __TEXT.__gcc_except_tab: 0x17c
+  __TEXT.__cstring: 0x2581
   __TEXT.__objc_classname: 0x185
-  __TEXT.__objc_methname: 0x39b5
+  __TEXT.__objc_methname: 0x3aa5
   __TEXT.__objc_methtype: 0x46d
   __TEXT.__const: 0x20a
   __TEXT.__oslogstring: 0x57
   __TEXT.__swift5_typeref: 0x1d1
   __TEXT.__swift5_capture: 0x12c
   __TEXT.__swift5_fieldmd: 0xa4
-  __TEXT.__constg_swiftt: 0x15c
+  __TEXT.__constg_swiftt: 0x16c
   __TEXT.__swift5_reflstr: 0x9c
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_assocty: 0x18

   __TEXT.__swift_as_entry: 0x10
   __TEXT.__swift_as_ret: 0x14
   __TEXT.__swift_as_cont: 0x10
-  __TEXT.__unwind_info: 0x670
+  __TEXT.__unwind_info: 0x6a0
   __TEXT.__eh_frame: 0x248
-  __DATA_CONST.__const: 0xa40
-  __DATA_CONST.__cfstring: 0x1da0
+  __DATA_CONST.__const: 0xa50
+  __DATA_CONST.__cfstring: 0x1ea0
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__objc_superrefs: 0x18
+  __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x418
-  __DATA_CONST.__got: 0x1e0
+  __DATA_CONST.__auth_got: 0x420
+  __DATA_CONST.__got: 0x1e8
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA.__objc_const: 0x2030
-  __DATA.__objc_selrefs: 0xc98
+  __DATA.__objc_const: 0x2040
+  __DATA.__objc_selrefs: 0xce8
   __DATA.__objc_ivar: 0x150
-  __DATA.__objc_data: 0x400
+  __DATA.__objc_data: 0x410
   __DATA.__data: 0x218
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation

   - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftGLKit.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMLCompute.dylib

   - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
+  - /usr/lib/swift/libswiftSceneKit.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 544
-  Symbols:   177
-  CStrings:  966
+  Functions: 555
+  Symbols:   181
+  CStrings:  987
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftGLKit
+ __swift_FORCE_LOAD_$_swiftSceneKit
+ _kCFPreferencesAnyUser
+ _swift_dynamicCastObjCClass
CStrings:
+ "%@: %@\n"
+ "%@: non-nil\n"
+ "------------------\n"
+ "-[MBPerUserState _encodeBundleDefaults:]"
+ "-[MBPerUserState loadFromUserDefaults]"
+ "Build"
+ "Loaded dictionary into per-user state:\n%@"
+ "Loaded per-user state from defaults:\n%@"
+ "PostMacBuddyCleanupCompleted"
+ "Version"
+ "Writing per-user state:\n%@"
+ "_bundleDefaultsByDomainFromDataSources:"
+ "_bundleDefaultsToPersist"
+ "_encodeBundleDefaults:"
+ "_logString"
+ "allKeys"
+ "appendFormat:"
+ "appendString:"
+ "com.apple.setupassistant"
+ "containsString:"
+ "determineIfMacBuddyCleanupNeeded"
+ "failed to decode"
+ "writeOutMacBuddyCleanupCompleted"
- "-[MBPerUserState _encodeBundleDefaultsToDataFromDataSources:]"
- "Writing per-user state"
```
