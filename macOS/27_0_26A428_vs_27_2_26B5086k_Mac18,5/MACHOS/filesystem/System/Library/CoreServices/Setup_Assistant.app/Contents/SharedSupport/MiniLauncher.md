## MiniLauncher

> `/System/Library/CoreServices/Setup Assistant.app/Contents/SharedSupport/MiniLauncher`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_nlclslist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__data`

```diff

-7548.0.0.0.0
-  __TEXT.__text: 0x5f52c
-  __TEXT.__auth_stubs: 0x16a0
-  __TEXT.__objc_stubs: 0xb0c0
-  __TEXT.__objc_methlist: 0x61d4
+7549.0.0.0.0
+  __TEXT.__text: 0x5fe88
+  __TEXT.__auth_stubs: 0x16b0
+  __TEXT.__objc_stubs: 0xb1c0
+  __TEXT.__objc_methlist: 0x6244
   __TEXT.__objc_classname: 0xd8f
-  __TEXT.__objc_methtype: 0x21fb
+  __TEXT.__objc_methtype: 0x221b
   __TEXT.__const: 0xd5c
-  __TEXT.__cstring: 0x11f5e
-  __TEXT.__objc_methname: 0x10ef5
+  __TEXT.__cstring: 0x1206e
+  __TEXT.__objc_methname: 0x11005
   __TEXT.__gcc_except_tab: 0x7dc
   __TEXT.__dlopen_cstrs: 0xa1
   __TEXT.__oslogstring: 0x57
   __TEXT.__ustring: 0x122
   __TEXT.__swift5_typeref: 0x9c6
-  __TEXT.__constg_swiftt: 0x9ac
+  __TEXT.__constg_swiftt: 0x9bc
   __TEXT.__swift5_reflstr: 0x562
   __TEXT.__swift5_fieldmd: 0x4e4
   __TEXT.__swift5_types: 0x78

   __TEXT.__swift5_assocty: 0xd8
   __TEXT.__swift5_builtin: 0x8c
   __TEXT.__swift5_proto: 0x54
-  __TEXT.__unwind_info: 0x1f48
+  __TEXT.__unwind_info: 0x1f70
   __TEXT.__eh_frame: 0x8c0
-  __DATA_CONST.__const: 0x2900
-  __DATA_CONST.__cfstring: 0xa3a0
+  __DATA_CONST.__const: 0x2910
+  __DATA_CONST.__cfstring: 0xa4e0
   __DATA_CONST.__objc_classlist: 0x1b0
   __DATA_CONST.__objc_nlclslist: 0x8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x200
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x118
-  __DATA_CONST.__objc_superrefs: 0xb0
+  __DATA_CONST.__objc_superrefs: 0xb8
   __DATA_CONST.__objc_intobj: 0x90
   __DATA_CONST.__objc_arraydata: 0x110
   __DATA_CONST.__objc_dictobj: 0x190
   __DATA_CONST.__objc_arrayobj: 0x60
-  __DATA_CONST.__auth_got: 0xb60
-  __DATA_CONST.__got: 0x878
+  __DATA_CONST.__auth_got: 0xb68
+  __DATA_CONST.__got: 0x880
   __DATA_CONST.__auth_ptr: 0x1b0
-  __DATA.__objc_const: 0xf4f0
-  __DATA.__objc_selrefs: 0x3af8
+  __DATA.__objc_const: 0xf500
+  __DATA.__objc_selrefs: 0x3b48
   __DATA.__objc_ivar: 0x504
-  __DATA.__objc_data: 0x1db0
+  __DATA.__objc_data: 0x1dc0
   __DATA.__data: 0x1578
   __DATA.__common: 0x10
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts

   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCoreMediaIO.dylib
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
-  Functions: 2557
-  Symbols:   748
-  CStrings:  4774
+  Functions: 2568
+  Symbols:   751
+  CStrings:  4796
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftGLKit
+ __swift_FORCE_LOAD_$_swiftSceneKit
+ _swift_dynamicCastObjCClass
CStrings:
+ "%@: %@\n"
+ "%@: non-nil\n"
+ "------------------\n"
+ "-[MBPerUserState _encodeBundleDefaults:]"
+ "-[MBPerUserState loadFromUserDefaults]"
+ "Attempting MBSA post buddy tasks"
+ "Build"
+ "Loaded dictionary into per-user state:\n%@"
+ "Loaded per-user state from defaults:\n%@"
+ "MBSA post buddy cleanup: %@"
+ "PostMacBuddyCleanupCompleted"
+ "Timed out waiting for MBSA post buddy cleanup. Moving on."
+ "Version"
+ "Writing per-user state:\n%@"
+ "_bundleDefaultsByDomainFromDataSources:"
+ "_bundleDefaultsToPersist"
+ "_encodeBundleDefaults:"
+ "_logString"
+ "acAccount"
+ "appendFormat:"
+ "appendString:"
+ "containsString:"
+ "determineIfMacBuddyCleanupNeeded"
+ "failed to decode"
+ "int main(int, const char **)_block_invoke"
+ "performFastUserSwitchToLocallyCreatedUserWithUID:withPassword:isDemoUser:initialPerUserState:completionBlock:"
+ "v48@0:8I16@\"NSString\"20B28@\"NSDictionary\"32@?<v@?B>40"
+ "v48@0:8I16@20B28@32@?40"
+ "writeOutMacBuddyCleanupCompleted"
- "-[LocalUserAccountManager runFastUserSwitchTasks]_block_invoke"
- "-[MBPerUserState _encodeBundleDefaultsToDataFromDataSources:]"
- "Writing per-user state"
- "Wrote per user state with success: %i"
- "performFastUserSwitchToLocallyCreatedUserWithUID:withPassword:isDemoUser:completionBlock:"
- "v40@0:8I16@\"NSString\"20B28@?<v@?B>32"
- "v40@0:8I16@20B28@?32"
```
