## AppProtectionUI

> `/System/Library/PrivateFrameworks/AppProtectionUI.framework/AppProtectionUI`

```diff

-35.1.7.0.0
-  __TEXT.__text: 0x146cc
-  __TEXT.__auth_stubs: 0xb90
+35.2.1.0.0
+  __TEXT.__text: 0x151b4
+  __TEXT.__auth_stubs: 0xba0
   __TEXT.__objc_methlist: 0x8e8
   __TEXT.__const: 0x468
-  __TEXT.__gcc_except_tab: 0x54
-  __TEXT.__oslogstring: 0x583
-  __TEXT.__cstring: 0x1617
+  __TEXT.__gcc_except_tab: 0x80
+  __TEXT.__oslogstring: 0x593
+  __TEXT.__cstring: 0x16c7
   __TEXT.__constg_swiftt: 0x3cc
-  __TEXT.__swift5_typeref: 0x4a4
+  __TEXT.__swift5_typeref: 0x4e2
   __TEXT.__swift5_builtin: 0x78
   __TEXT.__swift5_reflstr: 0x144
   __TEXT.__swift5_fieldmd: 0x218
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x18
   __TEXT.__swift5_types: 0x30
-  __TEXT.__swift5_capture: 0x35c
+  __TEXT.__swift5_capture: 0x3b4
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x5b0
+  __TEXT.__unwind_info: 0x5d8
   __TEXT.__eh_frame: 0x78
   __TEXT.__objc_classname: 0x280
-  __TEXT.__objc_methname: 0x3074
+  __TEXT.__objc_methname: 0x309c
   __TEXT.__objc_methtype: 0xfc6
   __TEXT.__objc_stubs: 0x1ba0
-  __DATA_CONST.__got: 0x318
-  __DATA_CONST.__const: 0x370
+  __DATA_CONST.__got: 0x328
+  __DATA_CONST.__const: 0x3a0
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xa40
+  __DATA_CONST.__objc_selrefs: 0xa48
   __DATA_CONST.__objc_protorefs: 0x20
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__objc_arraydata: 0x80
-  __AUTH_CONST.__auth_got: 0x5d8
+  __AUTH_CONST.__auth_got: 0x5e0
   __AUTH_CONST.__auth_ptr: 0xb0
-  __AUTH_CONST.__const: 0x1038
+  __AUTH_CONST.__const: 0x1100
   __AUTH_CONST.__cfstring: 0x980
   __AUTH_CONST.__objc_const: 0x2938
   __AUTH_CONST.__objc_dictobj: 0x28

   __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreGraphics.framework/CoreGraphics
+  - /System/Library/Frameworks/CoreLocation.framework/CoreLocation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
+  - /usr/lib/swift/libswiftCoreLocation.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 564
-  Symbols:   531
-  CStrings:  871
+  Functions: 577
+  Symbols:   543
+  CStrings:  876
 
Symbols:
+ _OBJC_CLASS_$_CLLocationManager
+ __swift_FORCE_LOAD_$_swiftCoreLocation
+ __xpc_error_key_description
+ _xpc_dictionary_get_string
CStrings:
+ "TURN_OFF_ALWAYS_LOCATION_MESSAGE"
+ "TURN_OFF_ALWAYS_LOCATION_TO_HIDE_X"
+ "authorizationStatusForBundleIdentifier:"
+ "got error on listener error: %!s(MISSING)"
+ "prefs:root=Notifications&path="
+ "prefs:root=Privacy&path=LOCATION/"
- "got error on listener"

```
