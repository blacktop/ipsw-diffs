## AccessoryNotifications

> `/System/Library/Frameworks/AccessoryNotifications.framework/AccessoryNotifications`

```diff

-  __TEXT.__text: 0x607e8
+  __TEXT.__text: 0x60cd4
   __TEXT.__objc_methlist: 0x1b4
-  __TEXT.__const: 0x9660
-  __TEXT.__swift5_typeref: 0x226a
-  __TEXT.__cstring: 0x138d
-  __TEXT.__constg_swiftt: 0x1890
-  __TEXT.__swift5_reflstr: 0xcb9
-  __TEXT.__swift5_fieldmd: 0x1964
-  __TEXT.__swift5_proto: 0x898
-  __TEXT.__swift5_types: 0x248
-  __TEXT.__swift5_capture: 0x428
-  __TEXT.__oslogstring: 0xefa
+  __TEXT.__const: 0x96ac
+  __TEXT.__constg_swiftt: 0x18ac
+  __TEXT.__swift5_typeref: 0x225d
+  __TEXT.__swift5_fieldmd: 0x198c
+  __TEXT.__swift5_reflstr: 0xcc5
+  __TEXT.__swift5_proto: 0x89c
+  __TEXT.__swift5_types: 0x24c
+  __TEXT.__cstring: 0x13c1
   __TEXT.__swift5_assocty: 0x198
-  __TEXT.__swift5_builtin: 0x64
   __TEXT.__swift_as_entry: 0xf8
   __TEXT.__swift_as_ret: 0xd0
-  __TEXT.__swift_as_cont: 0x16c
-  __TEXT.__swift5_mpenum: 0x34
+  __TEXT.__swift_as_cont: 0x170
+  __TEXT.__oslogstring: 0xf44
+  __TEXT.__swift5_capture: 0x448
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x1d70
-  __TEXT.__eh_frame: 0x2b30
+  __TEXT.__swift5_builtin: 0x64
+  __TEXT.__swift5_mpenum: 0x34
+  __TEXT.__unwind_info: 0x1d78
+  __TEXT.__eh_frame: 0x2b58
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_selrefs: 0x1c8
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x47f0
+  __AUTH_CONST.__const: 0x48b9
   __AUTH_CONST.__objc_const: 0xb40
-  __AUTH_CONST.__auth_got: 0xb10
-  __AUTH.__objc_data: 0x450
-  __AUTH.__data: 0x828
-  __DATA.__data: 0x1430
-  __DATA.__bss: 0xcf00
-  __DATA.__common: 0x10
-  __DATA_DIRTY.__data: 0xba8
-  __DATA_DIRTY.__bss: 0x4300
-  __DATA_DIRTY.__common: 0x18
+  __AUTH_CONST.__auth_got: 0xb18
+  __AUTH.__objc_data: 0xd8
+  __AUTH.__data: 0x80
+  __DATA.__data: 0x1328
+  __DATA.__bss: 0xcd80
+  __DATA.__common: 0x8
+  __DATA_DIRTY.__objc_data: 0x378
+  __DATA_DIRTY.__data: 0x1450
+  __DATA_DIRTY.__bss: 0x4500
+  __DATA_DIRTY.__common: 0x20
   - /System/Library/Frameworks/AccessorySetupKit.framework/AccessorySetupKit
   - /System/Library/Frameworks/AccessoryTransportExtension.framework/AccessoryTransportExtension
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/ImageIO.framework/ImageIO
   - /System/Library/Frameworks/UIKit.framework/UIKit
   - /System/Library/PrivateFrameworks/BaseBoard.framework/BaseBoard
+  - /System/Library/PrivateFrameworks/FeatureFlags.framework/FeatureFlags
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftAccelerate.dylib

   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2565
-  Symbols:   1443
-  CStrings:  214
+  Functions: 2569
+  Symbols:   1451
+  CStrings:  217
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift_as_entry : content changed
~ __TEXT.__swift_as_ret : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_protos : content changed
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_selrefs : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __AUTH_CONST.__objc_const : content changed
Symbols:
+ ___swift_closure_destructor.174Tm
+ ___swift_exist.box.addr_destructor
+ ___swift_memcpy41_8
+ _symbolic _____ 22AccessoryNotifications0aB11FeatureFlagV
+ _symbolic _____ s12StaticStringV
+ _type_layout_string 22AccessoryNotifications0aB11FeatureFlagV
- ___swift_closure_destructor.176Tm
- _get_type_metadata 15Synchronization5MutexVy3XPC10XPCSessionCSgG noncopyable
- _get_type_metadata 15Synchronization5MutexVySayScCySo15NSXPCConnectionCs5Error_pGGG noncopyable
- _get_type_metadata 15Synchronization5MutexVySo15NSXPCConnectionCSgG noncopyable
- _swift_runtimeSupportsNoncopyableTypes
CStrings:
+ "%s AccessoryNotifications feature flag disabled; not opening XPC session."
+ "AccessoryNotifications feature disabled."
+ "UserNotifications"

```
