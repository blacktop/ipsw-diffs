## Rapport

> `/System/Library/PrivateFrameworks/Rapport.framework/Rapport`

```diff

-706.100.1.0.0
-  __TEXT.__text: 0x9494c
+708.110.1.0.0
+  __TEXT.__text: 0x94ad0
   __TEXT.__auth_stubs: 0x1bb0
-  __TEXT.__objc_methlist: 0x8cfc
+  __TEXT.__objc_methlist: 0x8d3c
   __TEXT.__const: 0x3498
-  __TEXT.__cstring: 0x14784
+  __TEXT.__cstring: 0x147c4
   __TEXT.__gcc_except_tab: 0x16d0
   __TEXT.__oslogstring: 0x66b
   __TEXT.__swift5_typeref: 0x659

   __TEXT.__unwind_info: 0x23b0
   __TEXT.__eh_frame: 0x598
   __TEXT.__objc_classname: 0xa6b
-  __TEXT.__objc_methname: 0x109d1
+  __TEXT.__objc_methname: 0x10a50
   __TEXT.__objc_methtype: 0x2b8b
-  __TEXT.__objc_stubs: 0x8e20
+  __TEXT.__objc_stubs: 0x8e60
   __DATA_CONST.__got: 0x3a0
-  __DATA_CONST.__const: 0x26a0
+  __DATA_CONST.__const: 0x2680
   __DATA_CONST.__objc_classlist: 0x280
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x128
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3998
+  __DATA_CONST.__objc_selrefs: 0x39b8
   __DATA_CONST.__objc_protorefs: 0xc8
   __DATA_CONST.__objc_superrefs: 0x1d0
   __DATA_CONST.__objc_arraydata: 0xb0
   __AUTH_CONST.__auth_got: 0xde8
   __AUTH_CONST.__const: 0xe98
   __AUTH_CONST.__cfstring: 0x5040
-  __AUTH_CONST.__objc_const: 0x10388
+  __AUTH_CONST.__objc_const: 0x103c0
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x30
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH.__objc_data: 0x590
   __AUTH.__data: 0x7b0
-  __DATA.__objc_ivar: 0x1114
+  __DATA.__objc_ivar: 0x1118
   __DATA.__data: 0x1c38
   __DATA.__bss: 0x2240
   __DATA.__common: 0x48

   - /usr/lib/swift/libswiftCoreAudio.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftUniformTypeIdentifiers.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 98241B53-85B5-3D56-97C2-14617FF62A00
-  Functions: 4315
-  Symbols:   11904
-  CStrings:  6934
+  UUID: B280BEF3-8AA3-395F-9BDE-7B05F229842F
+  Functions: 4318
+  Symbols:   11905
+  CStrings:  6942
 
Symbols:
+ -[RPClient regenerateSelfIdentity:withCompletion:]
+ -[RPConnection _abortSendEntry:withError:]
+ -[RPConnection _eligiblePendingSendCount]
+ -[RPConnection _isEligibleToSendWithOptions:]
+ -[RPSession localIdentifier]
+ -[RPSession setLocalIdentifier:]
+ GCC_except_table135
+ GCC_except_table142
+ GCC_except_table146
+ _OBJC_IVAR_$_RPSession._localIdentifier
+ ___50-[RPClient regenerateSelfIdentity:withCompletion:]_block_invoke
+ ___50-[RPClient regenerateSelfIdentity:withCompletion:]_block_invoke_2
+ ___50-[RPClient regenerateSelfIdentity:withCompletion:]_block_invoke_3
+ ___block_literal_global.1342
+ ___block_literal_global.1360
+ _objc_msgSend$_abortSendEntry:withError:
+ _objc_msgSend$_eligiblePendingSendCount
+ _objc_msgSend$_isEligibleToSendWithOptions:
+ _objc_msgSend$regenerateSelfIdentity:withCompletion:
- -[RPClient startLocalIdentitySyncWithCompletion:]
- -[RPClient stopLocalIdentitySyncWithToken:completion:]
- GCC_except_table133
- GCC_except_table140
- GCC_except_table144
- ___49-[RPClient startLocalIdentitySyncWithCompletion:]_block_invoke
- ___49-[RPClient startLocalIdentitySyncWithCompletion:]_block_invoke_2
- ___54-[RPClient stopLocalIdentitySyncWithToken:completion:]_block_invoke
- ___54-[RPClient stopLocalIdentitySyncWithToken:completion:]_block_invoke_2
- ___block_literal_global.1338
- ___block_literal_global.1356
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_Rapport
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_Rapport
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_Rapport
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_Rapport
- _objc_msgSend$startLocalIdentitySyncWithCompletion:
- _objc_msgSend$stopLocalIdentitySyncWithToken:completion:
CStrings:
+ "-[RPConnection _abortSendEntry:withError:]"
+ "T@\"NSUUID\",C,N,V_localIdentifier"
+ "_abortSendEntry:withError:"
+ "_eligiblePendingSendCount"
+ "_isEligibleToSendWithOptions:"
+ "_localIdentifier"
+ "became present"
+ "localIdentifier"
+ "regenerateSelfIdentity:withCompletion:"
+ "setLocalIdentifier:"
- "startLocalIdentitySyncWithCompletion:"
- "stopLocalIdentitySyncWithToken:completion:"

```
