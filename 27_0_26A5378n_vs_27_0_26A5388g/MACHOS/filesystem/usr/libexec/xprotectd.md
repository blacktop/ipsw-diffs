## xprotectd

> `/usr/libexec/xprotectd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_types2`
- `__TEXT.__swift5_mpenum`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__common`

```diff

-291.0.3.0.0
-  __TEXT.__text: 0x6ae3c
-  __TEXT.__auth_stubs: 0x1b40
+291.0.4.0.0
+  __TEXT.__text: 0x6cd90
+  __TEXT.__auth_stubs: 0x1bf0
   __TEXT.__objc_stubs: 0x240
   __TEXT.__objc_methlist: 0x104
-  __TEXT.__const: 0x8d84
-  __TEXT.__swift5_typeref: 0x245c
-  __TEXT.__swift5_capture: 0x50c
-  __TEXT.__cstring: 0x231c
+  __TEXT.__const: 0x8fc4
+  __TEXT.__swift5_typeref: 0x251e
+  __TEXT.__swift5_capture: 0x564
+  __TEXT.__cstring: 0x23cc
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift_as_entry: 0xd8
-  __TEXT.__swift_as_ret: 0xc4
-  __TEXT.__swift_as_cont: 0x12c
-  __TEXT.__constg_swiftt: 0x2708
-  __TEXT.__swift5_reflstr: 0x17af
-  __TEXT.__swift5_fieldmd: 0x235c
-  __TEXT.__objc_methname: 0x4d5
+  __TEXT.__swift_as_entry: 0xe0
+  __TEXT.__swift_as_ret: 0xc8
+  __TEXT.__swift_as_cont: 0x130
+  __TEXT.__constg_swiftt: 0x284c
+  __TEXT.__swift5_reflstr: 0x183a
+  __TEXT.__swift5_fieldmd: 0x244c
+  __TEXT.__objc_methname: 0x4e5
   __TEXT.__objc_methtype: 0x6d6
-  __TEXT.__swift5_builtin: 0x26c
-  __TEXT.__swift5_proto: 0x6f4
-  __TEXT.__swift5_types: 0x36c
+  __TEXT.__swift5_builtin: 0x280
+  __TEXT.__swift5_proto: 0x704
+  __TEXT.__swift5_types: 0x388
   __TEXT.__swift5_assocty: 0x5b0
-  __TEXT.__swift5_protos: 0x60
+  __TEXT.__swift5_protos: 0x64
   __TEXT.__objc_classname: 0x1d0
   __TEXT.__oslogstring: 0x3
   __TEXT.__swift5_types2: 0xc
   __TEXT.__swift5_mpenum: 0x38
-  __TEXT.__unwind_info: 0x2080
-  __TEXT.__eh_frame: 0x3348
-  __DATA_CONST.__const: 0x6590
+  __TEXT.__unwind_info: 0x2118
+  __TEXT.__eh_frame: 0x33c8
+  __DATA_CONST.__const: 0x68b8
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x18
-  __DATA_CONST.__auth_got: 0xda8
-  __DATA_CONST.__got: 0x418
-  __DATA_CONST.__auth_ptr: 0x770
-  __DATA.__objc_const: 0xe18
+  __DATA_CONST.__auth_got: 0xe00
+  __DATA_CONST.__got: 0x420
+  __DATA_CONST.__auth_ptr: 0x790
+  __DATA.__objc_const: 0xe80
   __DATA.__objc_selrefs: 0x130
   __DATA.__objc_data: 0x50
-  __DATA.__data: 0x1e00
-  __DATA.__bss: 0xe420
+  __DATA.__data: 0x1e30
+  __DATA.__bss: 0xe6a0
   __DATA.__common: 0x32
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/Versions/A/CryptoKit

   - /System/Library/PrivateFrameworks/SystemPolicy.framework/Versions/A/SystemPolicy
   - /usr/lib/libEndpointSecurity.dylib
   - /usr/lib/libSystem.B.dylib
+  - /usr/lib/libbsm.0.dylib
   - /usr/lib/libcurl.4.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/swift/libswiftCore.dylib

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftIOKit.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
+  - /usr/lib/swift/libswiftSynchronization.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2826
-  Symbols:   709
-  CStrings:  346
+  Functions: 2869
+  Symbols:   722
+  CStrings:  352
 
Symbols:
+ _$s15Synchronization5MutexVMn
+ _$s15Synchronization5_CellVMa
+ _$sSD15reserveCapacityyySiF
+ _$sSa15reserveCapacityyySiF
+ _$sSayxGSmsMc
+ _$sScP13userInitiatedScPvgZ
+ _$sSlsE7isEmptySbvg
+ _$sSmsE11removeFirst7ElementQzyF
+ _$sSp12deinitialize5countSvSi_tF
+ _CFPasteboardInvalidateGeneralPasteboardCachesForUID
+ _audit_token_to_ruid
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
CStrings:
+ "[ApplePlatformTracer] deny: "
+ "[ApplePlatformTracer] pasteboard cache invalidation failed: "
+ "[Monitor] paste denied"
+ "[Monitor] paste denied (cached block)"
+ "blockStore"
+ "maxEntries"
```
