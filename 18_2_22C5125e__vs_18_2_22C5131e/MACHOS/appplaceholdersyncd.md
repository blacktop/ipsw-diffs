## appplaceholdersyncd

> `/System/Library/CoreServices/appplaceholdersyncd`

```diff

-30.0.0.0.0
-  __TEXT.__text: 0x5124
-  __TEXT.__auth_stubs: 0x7b0
+30.1.0.0.0
+  __TEXT.__text: 0x5300
+  __TEXT.__auth_stubs: 0x820
   __TEXT.__const: 0x10c
   __TEXT.__swift5_typeref: 0x8a
-  __TEXT.__oslogstring: 0x330
+  __TEXT.__oslogstring: 0x320
   __TEXT.__swift5_capture: 0x20
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0x57e
+  __TEXT.__cstring: 0x59e
   __TEXT.__constg_swiftt: 0xe0
   __TEXT.__swift5_reflstr: 0x34
   __TEXT.__swift5_fieldmd: 0x60

   __TEXT.__swift5_types: 0xc
   __TEXT.__unwind_info: 0x138
   __TEXT.__eh_frame: 0x108
-  __DATA_CONST.__auth_got: 0x3d8
+  __DATA_CONST.__auth_got: 0x410
   __DATA_CONST.__got: 0x78
   __DATA_CONST.__auth_ptr: 0x68
-  __DATA_CONST.__const: 0x1f0
+  __DATA_CONST.__const: 0x200
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA.__objc_const: 0x170

   - /System/Library/PrivateFrameworks/AppPlaceholderSync.framework/AppPlaceholderSync
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib

   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
   Functions: 80
-  Symbols:   175
-  CStrings:  59
+  Symbols:   184
+  CStrings:  60
 
Symbols:
+ _$s18AppPlaceholderSync0C7ManagerC017syncPublisherWithA10ProtectionyyFTj
+ _$s18AppPlaceholderSync0C7ManagerC7upgradeyyFZ
+ _$s18AppPlaceholderSync14PublisherStoreC7upgradeyyFZ
+ _$s18AppPlaceholderSync14PublisherStoreCMa
+ _$s18AppPlaceholderSync8DefaultsV13schemaVersionSivg
+ _$s18AppPlaceholderSync8DefaultsV17lastSchemaVersionSivs
+ _$s18AppPlaceholderSync8DefaultsV6sharedACvMZ
+ __swift_FORCE_LOAD_$_swiftCompression
+ __swift_FORCE_LOAD_$_swiftOSLog
CStrings:
+ "%!s(MISSING): Devices changed, do we care?"
+ "%!s(MISSING): Not yet implemented!"
+ "%!s(MISSING): handle %!s(MISSING)"
+ "hidden-apps-changed"
- "%!s(MISSING)[%!l(MISSING)d]: Devices changed, do we care?"
- "%!s(MISSING)[%!l(MISSING)d]: Not yet implemented!"
- "%!s(MISSING)[%!l(MISSING)d]: handle %!s(MISSING)"

```
