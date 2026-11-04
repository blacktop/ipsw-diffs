## SecureAudioPasscode

> `/System/Library/PrivateFrameworks/SecureAudioPasscode.framework/SecureAudioPasscode`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_reflstr`

```diff

 210.3.0.0.0
-  __TEXT.__text: 0x5d78
+  __TEXT.__text: 0x76f4
   __TEXT.__objc_methlist: 0x2c
-  __TEXT.__const: 0x630
-  __TEXT.__constg_swiftt: 0x514
-  __TEXT.__swift5_typeref: 0x11d
-  __TEXT.__swift5_builtin: 0x28
+  __TEXT.__const: 0x6d8
+  __TEXT.__constg_swiftt: 0x54c
+  __TEXT.__swift5_typeref: 0x138
+  __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_reflstr: 0x1f6
-  __TEXT.__swift5_assocty: 0x18
-  __TEXT.__cstring: 0x88
-  __TEXT.__swift5_proto: 0x2c
-  __TEXT.__swift5_types: 0x34
-  __TEXT.__swift5_fieldmd: 0x248
-  __TEXT.__oslogstring: 0x6a5
+  __TEXT.__swift5_assocty: 0x30
+  __TEXT.__cstring: 0xc9
+  __TEXT.__swift5_proto: 0x34
+  __TEXT.__swift5_types: 0x38
+  __TEXT.__swift5_fieldmd: 0x254
+  __TEXT.__oslogstring: 0x7f5
   __TEXT.__swift5_capture: 0x54
   __TEXT.__swift_as_entry: 0x8
   __TEXT.__swift_as_ret: 0x8
   __TEXT.__swift_as_cont: 0xc
   __TEXT.__gcc_except_tab: 0x18
-  __TEXT.__unwind_info: 0x310
-  __TEXT.__eh_frame: 0x288
+  __TEXT.__unwind_info: 0x360
+  __TEXT.__eh_frame: 0x2e8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__const: 0xa0
   __DATA_CONST.__objc_classlist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x28
-  __DATA_CONST.__got: 0x90
-  __AUTH_CONST.__const: 0x410
+  __DATA_CONST.__objc_selrefs: 0x40
+  __DATA_CONST.__got: 0xd8
+  __AUTH_CONST.__const: 0x458
   __AUTH_CONST.__cfstring: 0x20
-  __AUTH_CONST.__objc_const: 0x680
+  __AUTH_CONST.__objc_const: 0x6a0
   __AUTH_CONST.__weak_auth_got: 0x10
-  __AUTH_CONST.__auth_got: 0x2e8
+  __AUTH_CONST.__auth_got: 0x450
   __AUTH.__objc_data: 0x50
-  __AUTH.__data: 0x6f0
-  __DATA.__data: 0x60
-  __DATA.__common: 0x18
+  __AUTH.__data: 0x710
+  __DATA.__data: 0x78
+  __DATA.__common: 0x30
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/AVFoundation.framework/AVFoundation
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
+  - /System/Library/PrivateFrameworks/AudioSession.framework/AudioSession
   - /System/Library/PrivateFrameworks/IsolatedCoreAudioClient.framework/IsolatedCoreAudioClient
   - /System/Library/PrivateFrameworks/Tightbeam.framework/Tightbeam
   - /usr/lib/libMobileGestalt.dylib

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 243
-  Symbols:   252
-  CStrings:  46
+  Functions: 268
+  Symbols:   290
+  CStrings:  54
 
Symbols:
+ _AVAudioSessionCategoryPlayback
+ _AVAudioSessionCategoryRecord
+ _AVAudioSessionModeDefault
+ _AVAudioSessionModeRaw
+ _OBJC_CLASS_$_AVAudioSecureSession
+ _RegisterForIsolatedAudio
+ ___stack_chk_fail
+ ___stack_chk_guard
+ ___swift_destroy_boxed_opaque_existential_0
+ __os_signpost_emit_with_name_impl
+ __swiftEmptyArrayStorage
+ __swiftImmortalRefCount
+ __swift_stdlib_bridgeErrorToNSError
+ __swift_stdlib_malloc_size
+ _malloc_size
+ _memcpy
+ _memmove
+ _objc_allocWithZone
+ _objc_release_x28
+ _objc_retain_x20
+ _objc_retain_x23
+ _objc_retain_x25
+ _objc_retain_x26
+ _objc_retain_x8
+ _swift_arrayDestroy
+ _swift_errorRetain
+ _swift_getErrorValue
+ _swift_getObjectType
+ _swift_isUniquelyReferenced_nonNull_native
+ _swift_release_n
+ _swift_release_x23
+ _swift_release_x24
+ _swift_retain_x23
+ _swift_retain_x24
+ _swift_unknownObjectRetain
+ _symbolic _____ So23IsolatedAudio_UseCaseIDV
+ _symbolic _____ s6UInt32V
+ _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
CStrings:
+ "Failed to activate AVAudioSecureSession %@"
+ "Failed to activate audio session"
+ "Failed to deactivate AVAudioSecureSession %@"
+ "Failed to set AVAudioSecureSession category: %s, mode: %s, error: %s"
+ "Failed to start recording - deactivating audio session"
+ "SessionActivate"
+ "Unsupported isolated audio use case: %u"
+ "[Error] Interval already ended"
```
