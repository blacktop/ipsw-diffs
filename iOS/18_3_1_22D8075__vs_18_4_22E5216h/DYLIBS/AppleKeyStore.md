## AppleKeyStore

> `/System/Library/PrivateFrameworks/AppleKeyStore.framework/AppleKeyStore`

```diff

-1827.80.10.0.0
-  __TEXT.__text: 0x4e884
-  __TEXT.__auth_stubs: 0x1340
-  __TEXT.__cstring: 0x356d
-  __TEXT.__const: 0x5681
+1827.100.152.502.1
+  __TEXT.__text: 0x47cfc
+  __TEXT.__auth_stubs: 0x1480
+  __TEXT.__cstring: 0x3273
+  __TEXT.__const: 0x3fb1
   __TEXT.__oslogstring: 0xd3
-  __TEXT.__constg_swiftt: 0x898
-  __TEXT.__swift5_typeref: 0x7ff
-  __TEXT.__swift5_reflstr: 0xa12
-  __TEXT.__swift5_fieldmd: 0xc80
-  __TEXT.__swift5_proto: 0x36c
-  __TEXT.__swift5_types: 0xb4
-  __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__swift5_assocty: 0x540
-  __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x12e0
-  __TEXT.__eh_frame: 0x1338
-  __DATA_CONST.__got: 0x228
-  __DATA_CONST.__const: 0x3688
-  __DATA_CONST.__objc_classlist: 0x20
+  __TEXT.__constg_swiftt: 0x4fc
+  __TEXT.__swift5_typeref: 0x2c4
+  __TEXT.__swift5_reflstr: 0x739
+  __TEXT.__swift5_fieldmd: 0x8b4
+  __TEXT.__swift5_types: 0x54
+  __TEXT.__swift5_protos: 0x4
+  __TEXT.__swift5_proto: 0x100
+  __TEXT.__swift5_types2: 0x4
+  __TEXT.__swift5_assocty: 0x168
+  __TEXT.__unwind_info: 0xf38
+  __TEXT.__eh_frame: 0x1390
+  __DATA_CONST.__got: 0x1f0
+  __DATA_CONST.__const: 0x36b0
+  __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __AUTH_CONST.__auth_got: 0x9a0
-  __AUTH_CONST.__auth_ptr: 0x5f0
-  __AUTH_CONST.__const: 0x1da8
+  __AUTH_CONST.__auth_got: 0xa40
+  __AUTH_CONST.__auth_ptr: 0x2f0
+  __AUTH_CONST.__const: 0xaa8
   __AUTH_CONST.__cfstring: 0x500
-  __AUTH_CONST.__objc_const: 0x358
-  __AUTH.__data: 0x6a0
-  __DATA.__data: 0xef0
-  __DATA.__bss: 0x4170
-  __DATA.__common: 0xa70
+  __AUTH_CONST.__objc_const: 0x268
+  __AUTH.__data: 0x480
+  __DATA.__data: 0xeb0
+  __DATA.__bss: 0x1d70
+  __DATA.__common: 0x7e0
   __DATA_DIRTY.__bss: 0x18
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /System/Library/PrivateFrameworks/APFS.framework/APFS
+  - /System/Library/PrivateFrameworks/SwiftASN1Internal.framework/SwiftASN1Internal
   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 1731
-  Symbols:   1082
-  CStrings:  603
+  Functions: 1744
+  Symbols:   1405
+  CStrings:  630
 
Symbols:
+ _AKSGetStashStats
+ _swift_allocateGenericClassMetadata
+ _swift_arrayInitWithTakeBackToFront
+ _swift_arrayInitWithTakeFrontToBack
+ _swift_beginAccess
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_initStructMetadataWithLayoutString
+ _swift_cvw_initWithCopy
+ _swift_cvw_initWithTake
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _swift_endAccess
+ _swift_getEnumTagSinglePayloadGeneric
+ _swift_getSingletonMetadata
+ _swift_initClassMetadata2
+ _swift_slowAlloc
+ _swift_slowDealloc
+ _swift_storeEnumTagSinglePayloadGeneric
- _swift_allocateGenericValueMetadata
- _swift_getAssociatedConformanceWitness
- _swift_getAssociatedTypeWitness
- _swift_initStructMetadata
- _swift_retain
- _swift_unexpectedError
- _swift_unknownObjectRelease_n
CStrings:
+ "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/backup_serialize.c"
+ "/Library/Caches/com.apple.xbs/Sources/AppleKeyStore_libs/shared_crypto.c"
+ "AKSGetStashStats"
+ "acmh"
+ "ad"
+ "ag"
+ "bc"
+ "bd"
+ "bk"
+ "cf"
+ "cmpg"
+ "d"
+ "ed"
+ "gp"
+ "grko"
+ "kt"
+ "kv"
+ "ms"
+ "o"
+ "oa"
+ "oc"
+ "ocwe"
+ "ocww"
+ "od"
+ "odel"
+ "oe"
+ "oecd"
+ "oece"
+ "oect"
+ "orwk"
+ "osgn"
+ "oska"
+ "oskc"
+ "osko"
+ "osks"
+ "ow"
+ "p"
+ "prsn"
+ "rf"
+ "ri"
+ "rk"
+ "ro"
+ "rsct"
+ "rskt"
+ "salt"
+ "seed"
+ "si"
+ "skck"
+ "skcs"
+ "skni"
+ "skos"
+ "spka"
+ "srkt"
+ "tf"
+ "tsi2"
+ "value"
+ "vuid"
- "ASN.1 tag incorrectly encoded in long form:"
- "ASN1Identifier(tagNumber: "
- "AppleKeyStore/ASN1.swift"
- "AppleKeyStore/ASN1Boolean.swift"
- "AppleKeyStore/ASN1Integer.swift"
- "AppleKeyStore/ASN1OctetString.swift"
- "AppleKeyStore/ObjectIdentifier.swift"
- "DER.ParserNode(identifier: "
- "Excessive stack depth was reached"
- "Excessively large field:"
- "Field length encoded in excessive number of bytes"
- "Field length encoded in long form, but DER requires to be encoded in short form"
- "INTEGER encoded with top bit set!"
- "INTEGER encoded with zero bytes"
- "INTEGER not encoded in fewest number of octets"
- "Indefinite form of field length not supported in DER."
- "Invalid byte for ASN1Bool"
- "Invalid content for ASN1Bool"
- "Invalid encoding for OID subidentifier"
- "OID subidentifier encoded with leading 0 byte"
- "Trailing unparsed data is present"
- "Unable to decode, no ASN.1 nodes to decode"
- "Unable to store OID subidentifier"
- "Unable to treat bytes as a"
- "_TtCV13AppleKeyStore9ASN1Error7Backing"
- "code"
- "file"
- "line"
- "reason"
- "unexpectedFieldType"

```
