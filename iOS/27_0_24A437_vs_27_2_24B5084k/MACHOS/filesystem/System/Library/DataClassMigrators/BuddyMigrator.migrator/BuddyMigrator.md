## BuddyMigrator

> `/System/Library/DataClassMigrators/BuddyMigrator.migrator/BuddyMigrator`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__cstring`
- `__TEXT.__oslogstring`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-5411.101.0.0.0
-  __TEXT.__text: 0x2c0f0
-  __TEXT.__auth_stubs: 0x1230
-  __TEXT.__objc_stubs: 0x3100
-  __TEXT.__objc_methlist: 0x1c48
+5411.103.0.0.0
+  __TEXT.__text: 0x2bc84
+  __TEXT.__auth_stubs: 0x1220
+  __TEXT.__objc_stubs: 0x3080
+  __TEXT.__objc_methlist: 0x1c40
   __TEXT.__const: 0xf80
-  __TEXT.__gcc_except_tab: 0x2b8
-  __TEXT.__objc_methname: 0x4d93
+  __TEXT.__gcc_except_tab: 0x2ac
+  __TEXT.__objc_methname: 0x4ced
   __TEXT.__cstring: 0x10a2
   __TEXT.__oslogstring: 0x2e89
   __TEXT.__objc_classname: 0xd9a
   __TEXT.__objc_methtype: 0xdbd
-  __TEXT.__dlopen_cstrs: 0x2ac
+  __TEXT.__dlopen_cstrs: 0x254
   __TEXT.__constg_swiftt: 0xab4
   __TEXT.__swift5_typeref: 0xbbc
   __TEXT.__swift5_builtin: 0x64

   __TEXT.__swift_as_entry: 0x9c
   __TEXT.__swift_as_ret: 0xa0
   __TEXT.__swift_as_cont: 0xa8
-  __TEXT.__unwind_info: 0xf90
+  __TEXT.__unwind_info: 0xf80
   __TEXT.__eh_frame: 0x104c
-  __DATA_CONST.__const: 0x12f0
-  __DATA_CONST.__cfstring: 0xae0
+  __DATA_CONST.__const: 0x12d0
+  __DATA_CONST.__cfstring: 0xaa0
   __DATA_CONST.__objc_classlist: 0x158
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x140

   __DATA_CONST.__objc_protorefs: 0xc0
   __DATA_CONST.__objc_superrefs: 0x40
   __DATA_CONST.__objc_intobj: 0x18
-  __DATA_CONST.__auth_got: 0x928
-  __DATA_CONST.__got: 0x4a8
+  __DATA_CONST.__auth_got: 0x920
+  __DATA_CONST.__got: 0x4a0
   __DATA_CONST.__auth_ptr: 0x1b8
-  __DATA.__objc_const: 0x3ac0
-  __DATA.__objc_selrefs: 0x1130
+  __DATA.__objc_const: 0x3ab8
+  __DATA.__objc_selrefs: 0x1110
   __DATA.__objc_ivar: 0x114
   __DATA.__objc_data: 0x1958
   __DATA.__data: 0x1170

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftSceneKit.dylib
   - /usr/lib/swift/libswiftSpatial.dylib
-  - /usr/lib/swift/libswiftSpriteKit.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1010
-  Symbols:   423
-  CStrings:  1297
+  Functions: 1007
+  Symbols:   421
+  CStrings:  1290
 
Symbols:
- _BYPrivacyPrivacyPaneIdentifier
- __swift_FORCE_LOAD_$_swiftSpriteKit
CStrings:
+ "BuddyMigrator: Queueing Diagnostics & Usage mini-buddy for auto-opt-in"
+ "Is the multitasking feature applicable: %{bool}d"
+ "Should the multitasking feature flow be shown: %{bool}d"
- "%s isFeatureApplicable: %{bool}d"
- "%s shouldShowFlow: %{bool}d"
- "BuddyMigrator: Queueing Diagnostics & Usage mini-buddy for re-opt-in"
- "BuddyMigrator: Queueing mini-buddy to show the privacy pane"
- "OBBundle"
- "bundleWithIdentifier:"
- "contentVersion"
- "isDataAndPrivacyBundleEnabled"
- "privacyFlow"
- "softlink:r:path:/System/Library/PrivateFrameworks/OnBoardingKit.framework/OnBoardingKit"
```
