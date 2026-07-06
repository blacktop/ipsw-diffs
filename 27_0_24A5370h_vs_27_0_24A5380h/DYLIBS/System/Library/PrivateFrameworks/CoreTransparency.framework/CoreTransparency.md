## CoreTransparency

> `/System/Library/PrivateFrameworks/CoreTransparency.framework/CoreTransparency`

```diff

-  __TEXT.__text: 0x3f128
-  __TEXT.__const: 0x70e4
-  __TEXT.__cstring: 0x9be
-  __TEXT.__swift5_typeref: 0x17ca
-  __TEXT.__swift5_reflstr: 0x202d
+  __TEXT.__text: 0x4655c
+  __TEXT.__const: 0x7164
+  __TEXT.__cstring: 0xc8e
+  __TEXT.__swift5_typeref: 0x1862
+  __TEXT.__swift5_reflstr: 0x2064
   __TEXT.__swift5_assocty: 0x568
-  __TEXT.__constg_swiftt: 0x1ae8
-  __TEXT.__swift5_fieldmd: 0x1b64
+  __TEXT.__constg_swiftt: 0x1b34
+  __TEXT.__swift5_fieldmd: 0x1bd8
   __TEXT.__swift5_proto: 0x414
-  __TEXT.__swift5_types: 0x15c
+  __TEXT.__swift5_types: 0x164
   __TEXT.__swift5_protos: 0x9c
+  __TEXT.__oslogstring: 0x3
   __TEXT.__swift5_builtin: 0xc8
   __TEXT.__swift5_mpenum: 0x60
+  __TEXT.__swift5_capture: 0x150
   __TEXT.__swift5_types2: 0xc
-  __TEXT.__unwind_info: 0x16b0
-  __TEXT.__eh_frame: 0x1df0
+  __TEXT.__unwind_info: 0x17c0
+  __TEXT.__eh_frame: 0x20d4
   __TEXT.__auth_stubs: 0x0
-  __DATA_CONST.__const: 0x30
+  __DATA_CONST.__const: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x3638
-  __AUTH_CONST.__auth_got: 0x880
-  __AUTH.__data: 0x990
-  __DATA.__data: 0x9f0
-  __DATA.__bss: 0x7380
+  __AUTH_CONST.__const: 0x3a30
+  __AUTH_CONST.__auth_got: 0x958
+  __AUTH.__data: 0xa10
+  __DATA.__data: 0x9a0
+  __DATA.__bss: 0x7080
   __DATA.__common: 0x3c0
-  __DATA_DIRTY.__data: 0x8
-  __DATA_DIRTY.__bss: 0x100
+  __DATA_DIRTY.__data: 0xb0
+  __DATA_DIRTY.__bss: 0x400
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CryptoKit.framework/CryptoKit
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
+  - /usr/lib/swift/libswiftOSLog.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
-  Functions: 2754
-  Symbols:   1628
-  CStrings:  76
+  - /usr/lib/swift/libswiftos.dylib
+  Functions: 2837
+  Symbols:   1692
+  CStrings:  93
 
Sections:
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __TEXT.__swift5_types2 : content changed
Symbols:
+ ___swift_closure_destructor
+ ___swift_destroy_boxed_opaque_existential_0
+ ___swift_destroy_boxed_opaque_existential_1Tm
+ ___swift_memcpy120_8
+ __os_log_impl
+ __swift_FORCE_LOAD_$_swiftOSLog
+ __swift_FORCE_LOAD_$_swiftOSLog_$_CoreTransparency
+ __swift_FORCE_LOAD_$_swiftos
+ __swift_FORCE_LOAD_$_swiftos_$_CoreTransparency
+ _objc_release
+ _os_log_type_enabled
+ _swift_arrayDestroy
+ _swift_bridgeObjectRelease_n
+ _swift_bridgeObjectRetain_n
+ _swift_deallocClassInstance
+ _swift_deallocObject
+ _swift_getObjectType
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x25
+ _swift_retain_x22
+ _swift_retain_x25
+ _swift_retain_x26
+ _swift_retain_x28
+ _swift_setDeallocating
+ _swift_slowDealloc
+ _swift_unknownObjectRetain
+ _symbolic SSIego_
+ _symbolic Si6offset______7elementt 16CoreTransparency19CTEscapableMapProofV
+ _symbolic Si6offset______7elementtSg 16CoreTransparency19CTEscapableMapProofV
+ _symbolic _____ 16CoreTransparency20AETEscapableVerifierV14MapProofResult33_85266BF824721A9CDF7464F5EF259C44LLV
+ _symbolic _____ 16CoreTransparency8CTLoggerV
+ _symbolic _____ 2os6LoggerV
+ _symbolic _____y__________Say_____GG 16CoreTransparency16VerifiedLogEntryV AA23CTEscapableSignedObjectV AA10CTELogHeadV s5UInt8V
+ _symbolic _____yySpy_____Gz_SpySo8NSObjectCSgGSgzSpyypGSgztcG s23_ContiguousArrayStorageC s5UInt8V
+ _symbolic yyc
+ _type_layout_string 16CoreTransparency20AETEscapableVerifierV14MapProofResult33_85266BF824721A9CDF7464F5EF259C44LLV
- _get_type_metadata 16CoreTransparency13RawSpanBufferV noncopyable
- _get_type_metadata 16CoreTransparency16WireFormatReaderV noncopyable
- _swift_runtimeSupportsNoncopyableTypes
CStrings:
+ " consistencyResponses="
+ "%s"
+ "com.apple.CoreTransparency"
+ "parseEvents: mapProofs="
+ "verifyConsistencyProofs: count="
+ "verifyConsistencyProofs: failed to verify consistency "
+ "verifyConsistencyProofs: failed to verify endSLH signature: "
+ "verifyConsistencyProofs: failed to verify startSLH signature: "
+ "verifyConsistencyProofs: verified consistency "
+ "verifyConsistencyProofs: verified endSLH "
+ "verifyConsistencyProofs: verified startSLH "
+ "verifyMapProofs: failed to parse map leaf: "
+ "verifyMapProofs: failed to verify map proof: "
+ "verifyMapProofs: mapProofCount="
+ "verifyMapProofs: mismatched PAT heads "
+ "verifyMapProofs: no PAT entry found in any map proof ["
+ "verifyMapProofs: proof["

```
