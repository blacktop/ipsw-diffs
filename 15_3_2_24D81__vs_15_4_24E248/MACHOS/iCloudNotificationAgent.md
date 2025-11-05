## iCloudNotificationAgent

> `/System/Library/PrivateFrameworks/iCloudNotification.framework/iCloudNotificationAgent`

```diff

-301.22.3.0.0
-  __TEXT.__text: 0x21bc0
-  __TEXT.__auth_stubs: 0xb80
+301.22.4.7.0
+  __TEXT.__text: 0x2222c
+  __TEXT.__auth_stubs: 0xc20
   __TEXT.__objc_stubs: 0x33c0
-  __TEXT.__objc_methlist: 0x1024
-  __TEXT.__cstring: 0x17cf
+  __TEXT.__objc_methlist: 0x138c
+  __TEXT.__cstring: 0x180f
   __TEXT.__objc_classname: 0x349
   __TEXT.__objc_methname: 0x398c
   __TEXT.__objc_methtype: 0xd47
-  __TEXT.__const: 0x58a
+  __TEXT.__const: 0x5aa
   __TEXT.__gcc_except_tab: 0x1d4
-  __TEXT.__oslogstring: 0x2cb5
-  __TEXT.__swift5_typeref: 0x1ac
+  __TEXT.__oslogstring: 0x2e57
+  __TEXT.__swift5_typeref: 0x1f6
   __TEXT.__constg_swiftt: 0x134
   __TEXT.__swift5_fieldmd: 0xb8
   __TEXT.__swift5_types: 0x24

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x54
-  __TEXT.__unwind_info: 0x9b8
-  __TEXT.__eh_frame: 0x948
-  __DATA_CONST.__auth_got: 0x5d0
-  __DATA_CONST.__got: 0x3c8
+  __TEXT.__swift_as_entry: 0x2c
+  __TEXT.__swift_as_ret: 0x3c
+  __TEXT.__unwind_info: 0x9d0
+  __TEXT.__eh_frame: 0x980
+  __DATA_CONST.__auth_got: 0x620
+  __DATA_CONST.__got: 0x3d8
   __DATA_CONST.__auth_ptr: 0x120
-  __DATA_CONST.__const: 0x1160
+  __DATA_CONST.__const: 0x11b0
   __DATA_CONST.__cfstring: 0x1bc0
   __DATA_CONST.__objc_classlist: 0x110
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_superrefs: 0xd0
   __DATA_CONST.__objc_intobj: 0x78
   __DATA_CONST.__linkguard: 0x15
-  __DATA.__objc_const: 0x2d50
-  __DATA.__objc_selrefs: 0xf68
+  __DATA.__objc_const: 0x26e8
+  __DATA.__objc_selrefs: 0x1070
   __DATA.__objc_ivar: 0x124
   __DATA.__objc_data: 0xb00
-  __DATA.__data: 0x3b8
+  __DATA.__data: 0x3c8
   __DATA.__bss: 0xb00
   - /System/Library/Frameworks/Accounts.framework/Versions/A/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
+  - /usr/lib/swift/libswiftCoreImage.dylib
   - /usr/lib/swift/libswiftCoreMIDI.dylib
   - /usr/lib/swift/libswiftCryptoTokenKit.dylib
   - /usr/lib/swift/libswiftDarwin.dylib
+  - /usr/lib/swift/libswiftDataDetection.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftMetal.dylib

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 72E37482-DBD5-303D-B20D-40D7767FFD4F
-  Functions: 791
-  Symbols:   390
-  CStrings:  1536
+  UUID: D9B80CD1-A46E-39DC-A79F-936324A06D56
+  Functions: 812
+  Symbols:   404
+  CStrings:  1549
 
Symbols:
+ _$s14ACSEFoundation12TaskLimitersC7limiter3key7timeoutAA0B7LimiterCSS_s6UInt64VtF
+ _$syXlN
+ __os_log_default
+ __set_user_dir_suffix
+ __swift_FORCE_LOAD_$_swiftCoreImage
+ __swift_FORCE_LOAD_$_swiftDataDetection
+ _bzero
+ _confstr
+ _exit
+ _getenv
+ _getpwuid
+ _getuid
+ _realpath$DARWIN_EXTSN
+ _sandbox_init_with_parameters
+ _swift_arrayDestroy
+ _swift_setDeallocating
- _$s14ACSEFoundation12TaskLimitersC7limiter3keyAA0B7LimiterCSS_tF
- _$sSa12_endMutationyyFyXl_Ts5
CStrings:
+ "$HOME not set, falling back to using getpwuid"
+ "DARWIN_CACHE_DIR"
+ "Entering Sandbox."
+ "Failed to enter sandbox: %{public}s"
+ "Failed to get passwd entry for uid %u"
+ "Failed to initialize cache directory: %{darwin.errno}d"
+ "Failed to initialize temporary directory: %{darwin.errno}d"
+ "Failed to resolve cache directory: %{darwin.errno}d"
+ "Failed to resolve temporary directory: %{darwin.errno}d"
+ "Failed to resolve user's home directory: %{darwin.errno}d"
+ "HOME"
+ "TMPDIR"
+ "com.apple.iCloudNotificationAgent"

```
