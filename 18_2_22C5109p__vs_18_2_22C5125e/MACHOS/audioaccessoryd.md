## audioaccessoryd

> `/usr/libexec/audioaccessoryd`

```diff

-22.3.0.0.0
-  __TEXT.__text: 0x1b6260
-  __TEXT.__auth_stubs: 0x27a0
-  __TEXT.__objc_stubs: 0xe080
+22.6.0.0.0
+  __TEXT.__text: 0x1b6450
+  __TEXT.__auth_stubs: 0x27b0
+  __TEXT.__objc_stubs: 0xe0c0
   __TEXT.__objc_methlist: 0x5d18
-  __TEXT.__const: 0x3a60
+  __TEXT.__const: 0x3a70
   __TEXT.__gcc_except_tab: 0x352c
   __TEXT.__cstring: 0x2a783
-  __TEXT.__objc_methname: 0x1501d
+  __TEXT.__objc_methname: 0x1503e
   __TEXT.__objc_classname: 0x689
   __TEXT.__objc_methtype: 0x23e0
   __TEXT.__dlopen_cstrs: 0x5a
-  __TEXT.__oslogstring: 0x836a
+  __TEXT.__oslogstring: 0x83ca
   __TEXT.__constg_swiftt: 0x18ec
   __TEXT.__swift5_typeref: 0x19cc
   __TEXT.__swift5_builtin: 0xb4

   __TEXT.__swift5_mpenum: 0x14
   __TEXT.__unwind_info: 0x3920
   __TEXT.__eh_frame: 0x21d8
-  __DATA_CONST.__auth_got: 0x13e0
+  __DATA_CONST.__auth_got: 0x13e8
   __DATA_CONST.__got: 0xae0
-  __DATA_CONST.__auth_ptr: 0x690
-  __DATA_CONST.__const: 0xad00
+  __DATA_CONST.__auth_ptr: 0x6e8
+  __DATA_CONST.__const: 0xad08
   __DATA_CONST.__cfstring: 0x6820
   __DATA_CONST.__objc_classlist: 0x1d8
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_intobj: 0x180
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_const: 0x114b8
-  __DATA.__objc_selrefs: 0x4900
+  __DATA.__objc_selrefs: 0x4910
   __DATA.__objc_ivar: 0xcc0
   __DATA.__objc_data: 0x20e8
   __DATA.__data: 0x32c8

   - /System/Library/PrivateFrameworks/HeadGestures.framework/HeadGestures
   - /System/Library/PrivateFrameworks/HearingModeService_Private.framework/HearingModeService_Private
   - /System/Library/PrivateFrameworks/IDS.framework/IDS
+  - /System/Library/PrivateFrameworks/IDSFoundation.framework/IDSFoundation
   - /System/Library/PrivateFrameworks/MediaExperience.framework/MediaExperience
   - /System/Library/PrivateFrameworks/MediaRemote.framework/MediaRemote
   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib
   - /usr/lib/swift/libswiftMetal.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 5864
-  Symbols:   1129
-  CStrings:  8755
+  Functions: 5865
+  Symbols:   1131
+  CStrings:  8758
 
Symbols:
+ __IDSStringFromIDSRegistrationStatus
+ __swift_FORCE_LOAD_$_swiftOSLog
CStrings:
+ "MUC - Active service accounts changed - %!s(MISSING), accounts %!l(MISSING)u, R: %!d(MISSING), %!@(MISSING)"
+ "MUC - devicesChanged, R: %!l(MISSING)d, %!@(MISSING) - %!@(MISSING)"
+ "No devices found even though IDS Account registered, C: %!l(MISSING)d, R: %!l(MISSING)d %!@(MISSING)"
+ "iCloudAccount"
+ "registrationStatus"
- "MUC - Active service accounts changed - %!s(MISSING), accounts %!l(MISSING)u"
- "MUC - devicesChanged - %!@(MISSING)"

```
