## VSAppIntents

> `/System/Library/ExtensionKit/Extensions/VSAppIntents.appex/VSAppIntents`

```diff

-561.40.17.0.0
-  __TEXT.__text: 0x5980
-  __TEXT.__auth_stubs: 0x720
-  __TEXT.__const: 0x75a
+587.0.0.0.0
+  __TEXT.__text: 0x5690
+  __TEXT.__auth_stubs: 0x730
+  __TEXT.__const: 0x7e2
   __TEXT.__swift5_typeref: 0x374
-  __TEXT.__objc_methname: 0xdd
+  __TEXT.__objc_methname: 0xa2
   __TEXT.__swift5_capture: 0x14
-  __TEXT.__cstring: 0x5e3
+  __TEXT.__cstring: 0x493
   __TEXT.__swift_as_entry: 0x40
   __TEXT.__swift_as_ret: 0x2c
   __TEXT.__swift5_reflstr: 0x92

   __TEXT.__swift5_proto: 0x70
   __TEXT.__swift5_types: 0x10
   __TEXT.__unwind_info: 0x288
-  __TEXT.__eh_frame: 0x3b0
-  __DATA_CONST.__auth_got: 0x390
+  __TEXT.__eh_frame: 0x3a8
+  __DATA_CONST.__auth_got: 0x398
   __DATA_CONST.__got: 0x100
-  __DATA_CONST.__auth_ptr: 0x418
-  __DATA_CONST.__const: 0x1a8
+  __DATA_CONST.__auth_ptr: 0x420
+  __DATA_CONST.__const: 0x188
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_selrefs: 0x50
-  __DATA.__data: 0x2b8
+  __DATA.__objc_selrefs: 0x48
+  __DATA.__data: 0x238
   __DATA.__common: 0x60
   __DATA.__bss: 0xe08
   - /System/Library/Frameworks/AppIntents.framework/AppIntents

   - /System/Library/PrivateFrameworks/VideoSubscriberAccountUI.framework/VideoSubscriberAccountUI
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
+  - /usr/lib/swift/libswiftAccelerate.dylib
   - /usr/lib/swift/libswiftCompression.dylib
   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreLocation.dylib
-  - /usr/lib/swift/libswiftCoreMIDI.dylib
-  - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIntents.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_errno.dylib
-  - /usr/lib/swift/libswift_math.dylib
-  - /usr/lib/swift/libswift_signal.dylib
-  - /usr/lib/swift/libswift_stdio.dylib
-  - /usr/lib/swift/libswift_time.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
+  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  - /usr/lib/swift/libswiftsys_time.dylib
-  - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 69C67956-9594-3972-910D-7922C9CA4CBD
-  Functions: 160
-  Symbols:   93
-  CStrings:  41
+  UUID: FB39EE75-A158-31CD-9964-1EFC8339AC92
+  Functions: 161
+  Symbols:   89
+  CStrings:  34
 
Symbols:
+ __swift_FORCE_LOAD_$_swiftAccelerate
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation1
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation2
+ __swift_FORCE_LOAD_$_swift_DarwinFoundation3
+ _swift_coroFrameAlloc
- __swift_FORCE_LOAD_$_swiftCoreMIDI
- __swift_FORCE_LOAD_$_swiftCryptoTokenKit
- __swift_FORCE_LOAD_$_swift_errno
- __swift_FORCE_LOAD_$_swift_math
- __swift_FORCE_LOAD_$_swift_signal
- __swift_FORCE_LOAD_$_swift_stdio
- __swift_FORCE_LOAD_$_swift_time
- __swift_FORCE_LOAD_$_swiftsys_time
- __swift_FORCE_LOAD_$_swiftunistd
- _objc_release_x24
CStrings:
+ "General → TV Provider → Sign in"
+ "General → TV Provider → Sign out"
+ "settings-navigation://com.apple.Settings.General/TV_PROVIDER/"
- "Description text of `OpenTVProviderDeepLinks` 'Remove TV Provider' intent display representation."
- "REMOVE_TV_PROVIDER_DESCRIPTION_TEXT"
- "REMOVE_TV_PROVIDER_SUBTITLE"
- "Remove the stored TV Provider."
- "Subtitle of `OpenTVProviderDeepLinks` 'Remove TV Provider' intent display representation."
- "TV Provider → Remove TV Provider"
- "TV Provider → Sign in"
- "TV Provider → Sign out"
- "isFullySupportedForRequestsExpectingAuthenticationSchemes:"
- "settings-navigation://com.apple.Settings.TVProvider/"

```
