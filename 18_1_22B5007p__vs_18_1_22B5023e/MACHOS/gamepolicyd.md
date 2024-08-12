## gamepolicyd

> `/usr/libexec/gamepolicyd`

```diff

-2.0.23.0.0
-  __TEXT.__text: 0x27d9c
+2.0.25.0.0
+  __TEXT.__text: 0x27d84
   __TEXT.__auth_stubs: 0x1070
   __TEXT.__objc_stubs: 0x20
   __TEXT.__objc_methlist: 0x1b4

   __TEXT.__objc_methname: 0xc84
   __TEXT.__objc_classname: 0xd5
   __TEXT.__objc_methtype: 0x2ed
-  __TEXT.__cstring: 0x26bb
-  __TEXT.__swift5_typeref: 0x8b7
+  __TEXT.__cstring: 0x26cb
+  __TEXT.__swift5_typeref: 0x8b5
   __TEXT.__swift5_entry: 0x8
   __TEXT.__constg_swiftt: 0x11ec
   __TEXT.__swift5_reflstr: 0xd5c

   __TEXT.__swift5_types: 0x78
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_protos: 0x18
-  __TEXT.__swift5_capture: 0x330
-  __TEXT.__oslogstring: 0x948
+  __TEXT.__swift5_capture: 0x358
+  __TEXT.__oslogstring: 0x958
   __TEXT.__info_plist: 0x528
-  __TEXT.__unwind_info: 0x7a8
+  __TEXT.__unwind_info: 0x7a0
   __TEXT.__eh_frame: 0x700
   __DATA_CONST.__auth_got: 0x840
   __DATA_CONST.__got: 0x268
-  __DATA_CONST.__auth_ptr: 0x268
-  __DATA_CONST.__const: 0xe70
+  __DATA_CONST.__auth_ptr: 0x270
+  __DATA_CONST.__const: 0xf00
   __DATA_CONST.__cfstring: 0x40
   __DATA_CONST.__objc_classlist: 0xc0
   __DATA_CONST.__objc_protolist: 0xa0

   __DATA.__objc_const: 0x2630
   __DATA.__objc_selrefs: 0x3c0
   __DATA.__objc_data: 0x868
-  __DATA.__data: 0x1f10
+  __DATA.__data: 0x1f20
   __DATA.__common: 0x70
   __DATA.__bss: 0xe00
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswiftQuartzCore.dylib
   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
   Functions: 674
-  Symbols:   404
+  Symbols:   412
   CStrings:  492
 
Symbols:
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
CStrings:
+ "Foreground games identified - holding transaction"
+ "Foreground games no longer identified - releasing transaction"
+ "gamepolicyd is actively monitoring an identified foreground game"
- "Games identified - holding transaction"
- "Games no longer identified - releasing transaction"
- "gamepolicyd is actively monitoring an identified game"

```
