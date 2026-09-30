## IDS

> `/System/Library/PrivateFrameworks/IDS.framework/IDS`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__TEXT.__swift5_assocty`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH_CONST.__objc_intobj`
- `__DATA_DIRTY.__objc_data`

```diff

-1998.100.2.0.0
-  __TEXT.__text: 0x1a8bdc
-  __TEXT.__objc_methlist: 0xdb2c
-  __TEXT.__const: 0x5d98
-  __TEXT.__oslogstring: 0x1b514
-  __TEXT.__cstring: 0x11a76
+2000.100.2.2.1
+  __TEXT.__text: 0x1b56ac
+  __TEXT.__objc_methlist: 0xdc3c
+  __TEXT.__const: 0x5fe8
+  __TEXT.__oslogstring: 0x1b6f4
+  __TEXT.__cstring: 0x11b36
   __TEXT.__gcc_except_tab: 0x3da4
   __TEXT.__ustring: 0xac
   __TEXT.__dlopen_cstrs: 0x102
-  __TEXT.__swift5_typeref: 0x1ac4
-  __TEXT.__swift5_capture: 0x174
-  __TEXT.__swift_as_entry: 0x110
-  __TEXT.__swift_as_ret: 0x11c
-  __TEXT.__swift_as_cont: 0x254
-  __TEXT.__constg_swiftt: 0x14e4
-  __TEXT.__swift5_reflstr: 0xd35
-  __TEXT.__swift5_fieldmd: 0x161c
-  __TEXT.__swift5_proto: 0x3b4
-  __TEXT.__swift5_types: 0x230
+  __TEXT.__swift5_typeref: 0x1c5c
+  __TEXT.__swift5_capture: 0x19c
+  __TEXT.__swift_as_entry: 0x114
+  __TEXT.__swift_as_ret: 0x134
+  __TEXT.__swift_as_cont: 0x280
+  __TEXT.__constg_swiftt: 0x1658
+  __TEXT.__swift5_reflstr: 0xe3c
+  __TEXT.__swift5_fieldmd: 0x17d4
+  __TEXT.__swift5_proto: 0x3bc
+  __TEXT.__swift5_types: 0x250
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_mpenum: 0x28
   __TEXT.__swift5_protos: 0x28
   __TEXT.__swift5_assocty: 0x30
-  __TEXT.__unwind_info: 0x6cd8
-  __TEXT.__eh_frame: 0x2db8
+  __TEXT.__unwind_info: 0x6f88
+  __TEXT.__eh_frame: 0x3180
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x53f0
-  __DATA_CONST.__objc_classlist: 0x5e0
+  __DATA_CONST.__const: 0x5410
+  __DATA_CONST.__objc_classlist: 0x5f8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x248
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6cb0
+  __DATA_CONST.__objc_selrefs: 0x6d40
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x480
-  __DATA_CONST.__got: 0x1a98
-  __AUTH_CONST.__const: 0x54a8
+  __DATA_CONST.__got: 0x1ac8
+  __AUTH_CONST.__const: 0x5540
   __AUTH_CONST.__cfstring: 0x7700
-  __AUTH_CONST.__objc_const: 0x3d2c0
+  __AUTH_CONST.__objc_const: 0x3da18
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x588
-  __AUTH_CONST.__auth_got: 0x1dd0
-  __AUTH.__objc_data: 0x2058
-  __AUTH.__data: 0x1068
-  __DATA.__objc_ivar: 0xdf0
-  __DATA.__data: 0x2830
-  __DATA.__bss: 0x9770
+  __AUTH_CONST.__auth_got: 0x1ec0
+  __AUTH.__objc_data: 0x2168
+  __AUTH.__data: 0x1480
+  __DATA.__objc_ivar: 0xdf4
+  __DATA.__data: 0x2910
+  __DATA.__bss: 0x9910
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x1b80
   __DATA_DIRTY.__bss: 0x3c0

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9232
-  Symbols:   1865
-  CStrings:  3868
+  Functions: 9466
+  Symbols:   1874
+  CStrings:  3878
 
Symbols:
+ _CCDeriveKey
+ _CCKDFParametersCreateHkdf
+ _CCKDFParametersDestroy
+ _OBJC_CLASS_$__IDSCryptorPrimitives
+ _OBJC_CLASS_$__IDSRealTimeGroupSessionCryptorBackend
+ _OBJC_METACLASS_$__IDSCryptorPrimitives
+ _OBJC_METACLASS_$__IDSRealTimeGroupSessionCryptorBackend
+ _swift_dynamicCastObjCClass
+ _swift_release_x10
CStrings:
+ "%s: no cryptor backend available; returning an empty stream (session likely invalidated)"
+ "-[_IDSGroupSession requestMediaKeyMaterialForParticipants:]"
+ "-[_IDSGroupSession session:didReceiveMediaKeyMaterial:]"
+ "-[_IDSGroupSession session:shouldInvalidateMediaKeyMaterialByKeyIndexes:]"
+ "Can't deliver MKM to cryptor backend for session %@"
+ "Group session %@ didReceiveMediaKeyMaterial count=%lu"
+ "Ignoring group session didReceiveMediaKeyMaterial {self:%p, _uniqueID:%@, identifier:%@}"
+ "Ignoring group session shouldInvalidateMediaKeyMaterialByKeyIndexes, session doesn't match %@ vs. %@"
+ "RealTimeGroupSessionCryptor"
+ "cryptors(forTopic:keyMaterialSource:strategy:_:)"
+ "shouldInvalidateMediaKeyMaterialByKeyIndexes for session %@, expiredKeyIndexes: %@"
- "RealTimeGroupSessionCryptor implementation has not yet landed — see rdar://179268110."
```
