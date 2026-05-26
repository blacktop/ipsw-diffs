## SwiftMLS

> `/System/Library/PrivateFrameworks/SwiftMLS.framework/SwiftMLS`

```diff

-195.122.4.0.0
-  __TEXT.__text: 0x2cdb58
+195.160.27.0.0
+  __TEXT.__text: 0x2d5a20
   __TEXT.__auth_stubs: 0x2fa0
   __TEXT.__objc_methlist: 0x80
-  __TEXT.__const: 0x24bb8
-  __TEXT.__constg_swiftt: 0x4830
-  __TEXT.__swift5_typeref: 0x38e4
-  __TEXT.__swift5_reflstr: 0x5961
-  __TEXT.__swift5_fieldmd: 0x5eac
+  __TEXT.__const: 0x24c78
+  __TEXT.__constg_swiftt: 0x484c
+  __TEXT.__swift5_typeref: 0x38ea
+  __TEXT.__swift5_reflstr: 0x5981
+  __TEXT.__swift5_fieldmd: 0x5ee0
   __TEXT.__swift5_builtin: 0x104
   __TEXT.__swift5_assocty: 0xb08
-  __TEXT.__swift5_proto: 0xdc0
-  __TEXT.__swift5_types: 0x6a4
+  __TEXT.__swift5_proto: 0xdc4
+  __TEXT.__swift5_types: 0x6a8
   __TEXT.__swift5_capture: 0x2a4
   __TEXT.__swift5_protos: 0x40
-  __TEXT.__oslogstring: 0x5dd2
-  __TEXT.__cstring: 0x3c3d
-  __TEXT.__swift_as_entry: 0x604
+  __TEXT.__oslogstring: 0x5fa8
+  __TEXT.__cstring: 0x3d4d
+  __TEXT.__swift_as_entry: 0x600
   __TEXT.__swift_as_ret: 0xba0
   __TEXT.__swift5_mpenum: 0x138
-  __TEXT.__unwind_info: 0xa310
-  __TEXT.__eh_frame: 0x202b0
+  __TEXT.__unwind_info: 0xa390
+  __TEXT.__eh_frame: 0x20440
   __TEXT.__objc_classname: 0x38b
-  __TEXT.__objc_methname: 0x69d
+  __TEXT.__objc_methname: 0x6bd
   __TEXT.__objc_methtype: 0x71
-  __TEXT.__objc_stubs: 0x300
-  __DATA_CONST.__got: 0x950
+  __TEXT.__objc_stubs: 0x320
+  __DATA_CONST.__got: 0x958
   __DATA_CONST.__const: 0x100
   __DATA_CONST.__objc_classlist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd8
+  __DATA_CONST.__objc_selrefs: 0xe0
   __AUTH_CONST.__auth_got: 0x17d8
-  __AUTH_CONST.__const: 0xc5c8
+  __AUTH_CONST.__const: 0xc660
   __AUTH_CONST.__objc_const: 0x10e0
   __AUTH.__objc_data: 0x2d8
   __AUTH.__data: 0x4a08
-  __DATA.__data: 0x3318
+  __DATA.__data: 0x3320
   __DATA.__bss: 0x1b300
   __DATA.__common: 0x570
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 7AFAA82B-1C88-3595-A2CE-252B50818585
-  Functions: 10450
-  Symbols:   2312
-  CStrings:  914
+  UUID: 6B5A9012-50D8-3008-BB77-7CF912F5163B
+  Functions: 10472
+  Symbols:   2318
+  CStrings:  926
 
Symbols:
+ _OBJC_CLASS_$_NSThread
+ __objc_autoreleasePoolPop
+ __objc_autoreleasePoolPush
+ _objc_msgSend$sleepForTimeInterval:
+ _symbolic _____ 8SwiftMLS0B0O9ExtensionO017SubjectCommitmentC0V
+ _type_layout_string 8SwiftMLS0B0O9ExtensionO017SubjectCommitmentC0V
CStrings:
+ " — use readCiphersuiteID() at parse time"
+ "%s: Adopting fresh continuity token from era %u upgrade Welcome"
+ "%s: FileInfo has no subject, leaving subject_commitment unchanged"
+ "%s: new era: all committed group metadata keys are present, no request needed"
+ "%s: new era: missing continuity token, will request group metadata keys"
+ "%s: new era: missing icon key, will request group metadata keys"
+ "%s: new era: missing subject key, will request group metadata keys"
+ "%s: receiver's HPKE key in message state %s differs from current state, failing to avoid self-heal loop"
+ "CiphersuiteID.outer called on unvalidated rawValue "
+ "SwiftMLS/CertificationRequestInfo.swift"
+ "SwiftMLS/CiphersuiteID.swift"
+ "invalid DER-encoded ECDSA signature"
+ "invalid public key"
+ "isValidSuccessor: successor issuanceDate is not strictly later than predecessor"
+ "sleepForTimeInterval:"
- "%s: Missing continuity token, requesting group metadata keys"
- "%s: We %s the correct group metadata keys"
- "%s: group metadata keys request not needed since name isn't set"

```
