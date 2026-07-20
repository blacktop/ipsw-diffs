## IDS

> `/System/Library/PrivateFrameworks/IDS.framework/Versions/A/IDS`

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

```diff

-1998.100.2.0.0
-  __TEXT.__text: 0x1b8cc4
-  __TEXT.__objc_methlist: 0xdabc
-  __TEXT.__const: 0x5d88
-  __TEXT.__oslogstring: 0x1b324
-  __TEXT.__cstring: 0x10a56
+2000.100.2.1.1
+  __TEXT.__text: 0x1c5984
+  __TEXT.__objc_methlist: 0xdbcc
+  __TEXT.__const: 0x5fd8
+  __TEXT.__oslogstring: 0x1b504
+  __TEXT.__cstring: 0x10b06
   __TEXT.__gcc_except_tab: 0x3dcc
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
-  __TEXT.__unwind_info: 0x6b18
-  __TEXT.__eh_frame: 0x2db8
+  __TEXT.__unwind_info: 0x6dd0
+  __TEXT.__eh_frame: 0x3180
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xce8
-  __DATA_CONST.__objc_classlist: 0x5e0
+  __DATA_CONST.__const: 0xd08
+  __DATA_CONST.__objc_classlist: 0x5f8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x240
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6c50
+  __DATA_CONST.__objc_selrefs: 0x6ce0
   __DATA_CONST.__objc_protorefs: 0x128
   __DATA_CONST.__objc_superrefs: 0x478
-  __DATA_CONST.__got: 0x1a80
-  __AUTH_CONST.__const: 0xa1e8
+  __DATA_CONST.__got: 0x1ab0
+  __AUTH_CONST.__const: 0xa280
   __AUTH_CONST.__cfstring: 0x75a0
-  __AUTH_CONST.__objc_const: 0x3cf38
+  __AUTH_CONST.__objc_const: 0x3d690
   __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0x588
-  __AUTH_CONST.__auth_got: 0x1bd0
-  __AUTH.__objc_data: 0x2058
-  __AUTH.__data: 0x1058
-  __DATA.__objc_ivar: 0xdec
-  __DATA.__data: 0x2790
-  __DATA.__bss: 0x9720
+  __AUTH_CONST.__auth_got: 0x1cb8
+  __AUTH.__objc_data: 0x2118
+  __AUTH.__data: 0x1468
+  __DATA.__objc_ivar: 0xdf0
+  __DATA.__data: 0x2870
+  __DATA.__bss: 0x98c0
   __DATA.__common: 0x10
-  __DATA_DIRTY.__objc_data: 0x1b80
-  __DATA_DIRTY.__bss: 0x3ba
+  __DATA_DIRTY.__objc_data: 0x1bd0
+  __DATA_DIRTY.__bss: 0x3ca
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/Network.framework/Versions/A/Network

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 9246
-  Symbols:   1777
-  CStrings:  3797
+  Functions: 9480
+  Symbols:   1785
+  CStrings:  3807
 
Symbols:
+ _CCDeriveKey
+ _CCKDFParametersCreateHkdf
+ _CCKDFParametersDestroy
+ _OBJC_CLASS_$__IDSCryptorPrimitives
+ _OBJC_CLASS_$__IDSRealTimeGroupSessionCryptorBackend
+ _OBJC_METACLASS_$__IDSCryptorPrimitives
+ _OBJC_METACLASS_$__IDSRealTimeGroupSessionCryptorBackend
+ _swift_dynamicCastObjCClass
CStrings:
+ "%s: no cryptor backend available; returning an empty stream (session likely invalidated)"
+ "-[_IDSGroupSession requestMediaKeyMaterialForParticipants:]"
+ "-[_IDSGroupSession session:didReceiveMediaKeyMaterial:]"
+ "-[_IDSGroupSession session:shouldInvalidateMediaKeyMaterialByKeyIndexes:]"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oSiy64/Sources/IdentityServices_legacy/IDS/Client API/Device/Client/IDSDataChannels.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oSiy64/Sources/IdentityServices_legacy/IDS/Client API/Device/IDSDataChannelsUtils.m"
+ "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.oSiy64/Sources/IdentityServices_legacy/IDS/Client API/Device/IDSDataChannels_Direct.m"
+ "Can't deliver MKM to cryptor backend for session %@"
+ "Group session %@ didReceiveMediaKeyMaterial count=%lu"
+ "Ignoring group session didReceiveMediaKeyMaterial {self:%p, _uniqueID:%@, identifier:%@}"
+ "Ignoring group session shouldInvalidateMediaKeyMaterialByKeyIndexes, session doesn't match %@ vs. %@"
+ "RealTimeGroupSessionCryptor"
+ "cryptors(forTopic:keyMaterialSource:strategy:_:)"
+ "shouldInvalidateMediaKeyMaterialByKeyIndexes for session %@, expiredKeyIndexes: %@"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FEv4PW/Sources/IdentityServices_legacy/IDS/Client API/Device/Client/IDSDataChannels.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FEv4PW/Sources/IdentityServices_legacy/IDS/Client API/Device/IDSDataChannelsUtils.m"
- "/AppleInternal/Library/BuildRoots/<BUILDROOT>/Library/Caches/com.apple.xbs/TemporaryDirectory.FEv4PW/Sources/IdentityServices_legacy/IDS/Client API/Device/IDSDataChannels_Direct.m"
- "RealTimeGroupSessionCryptor implementation has not yet landed — see rdar://179268110."
```
