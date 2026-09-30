## SwiftCRLite

> `/System/Library/PrivateFrameworks/SwiftCRLite.framework/SwiftCRLite`

```diff

 134.0.21.0.0
-  __TEXT.__text: 0xb6a34
-  __TEXT.__objc_methlist: 0x54c
-  __TEXT.__const: 0x9354
-  __TEXT.__cstring: 0x40fc
-  __TEXT.__oslogstring: 0x181e
-  __TEXT.__swift5_typeref: 0x1ebd
-  __TEXT.__swift5_reflstr: 0x1e8c
-  __TEXT.__swift5_assocty: 0x3e0
-  __TEXT.__constg_swiftt: 0x1c08
-  __TEXT.__swift5_fieldmd: 0x2c3c
+  __TEXT.__text: 0xbb16c
+  __TEXT.__objc_methlist: 0x564
+  __TEXT.__const: 0x9594
+  __TEXT.__cstring: 0x44bc
+  __TEXT.__oslogstring: 0x195e
+  __TEXT.__swift5_typeref: 0x1f15
+  __TEXT.__swift5_reflstr: 0x1f3c
+  __TEXT.__swift5_assocty: 0x3f8
+  __TEXT.__constg_swiftt: 0x1c68
+  __TEXT.__swift5_fieldmd: 0x2d88
   __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_proto: 0x6dc
-  __TEXT.__swift5_types: 0x278
-  __TEXT.__swift5_capture: 0x474
+  __TEXT.__swift5_proto: 0x6fc
+  __TEXT.__swift5_types: 0x280
+  __TEXT.__swift5_capture: 0x4a0
   __TEXT.__swift5_protos: 0x1c
-  __TEXT.__swift_as_entry: 0x80
-  __TEXT.__swift_as_ret: 0xa8
-  __TEXT.__swift_as_cont: 0xa8
+  __TEXT.__swift_as_entry: 0x84
+  __TEXT.__swift_as_ret: 0xac
+  __TEXT.__swift_as_cont: 0xb0
   __TEXT.__swift5_mpenum: 0x94
-  __TEXT.__unwind_info: 0x2680
-  __TEXT.__eh_frame: 0x5024
+  __TEXT.__unwind_info: 0x27b8
+  __TEXT.__eh_frame: 0x549c
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_protolist: 0x60
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4a8
+  __DATA_CONST.__objc_selrefs: 0x4b0
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0x18
   __DATA_CONST.__got: 0x578
-  __AUTH_CONST.__const: 0x5d69
+  __AUTH_CONST.__const: 0x6011
   __AUTH_CONST.__cfstring: 0x40
   __AUTH_CONST.__objc_const: 0x19e0
   __AUTH_CONST.__auth_got: 0x1220
   __AUTH.__objc_data: 0xe0
   __AUTH.__data: 0x308
   __DATA.__objc_ivar: 0x28
-  __DATA.__data: 0x11e0
+  __DATA.__data: 0x1218
   __DATA.__common: 0x20
-  __DATA_DIRTY.__objc_data: 0x698
-  __DATA_DIRTY.__data: 0x2008
+  __DATA_DIRTY.__objc_data: 0x6a0
+  __DATA_DIRTY.__data: 0x2010
   __DATA_DIRTY.__bss: 0x2980
   __DATA_DIRTY.__common: 0xc0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_DarwinFoundation1.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 3422
-  Symbols:   1446
-  CStrings:  543
+  Functions: 3511
+  Symbols:   1457
+  CStrings:  576
 
Symbols:
+ -[SwiftCRLiteClient isPhotoRevoked:error:]
+ ___swift_closure_destructor.56Tm
+ _associated conformance 11SwiftCRLite11PRLMetaDataV10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLOSHAASQ
+ _associated conformance 11SwiftCRLite11PRLMetaDataV10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLOs0E3KeyAAs23CustomStringConvertible
+ _associated conformance 11SwiftCRLite11PRLMetaDataV10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLOs0E3KeyAAs28CustomDebugStringConvertible
+ _objc_msgSend$isPhotoRevoked:error:
+ _symbolic Si8expected_Si6actualt
+ _symbolic _____ 11SwiftCRLite11PRLMetaDataV
+ _symbolic _____ 11SwiftCRLite11PRLMetaDataV10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLO
+ _symbolic _____y_____G s22KeyedDecodingContainerV 11SwiftCRLite11PRLMetaDataV10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLO
+ _symbolic _____y_____G s22KeyedEncodingContainerV 11SwiftCRLite11PRLMetaDataV10CodingKeys33_E6FBEEB7D9D657A6F6332D4066B56307LLO
+ _type_layout_string 11SwiftCRLite11PRLMetaDataV
- ___swift_closure_destructor.47Tm
CStrings:
+ "    CREATE TABLE IF NOT EXISTS prl(\n       photo_id BLOB PRIMARY KEY NOT NULL\n    );"
+ "DELETE FROM prl WHERE photo_id = ?"
+ "DELETE FROM prl;"
+ "DROP TABLE IF EXISTS prl;"
+ "INSERT INTO main.prl SELECT * FROM "
+ "INSERT OR REPLACE INTO prl (photo_id) VALUES (?)"
+ "PRL data"
+ "PRL data length"
+ "PRL data length missing"
+ "PRL data missing"
+ "PRL entry"
+ "PRL entry count"
+ "PRL entry count mismatch: expected "
+ "PRL entry count missing"
+ "PRL entry data missing"
+ "PRL is deprecated and no longer maintained. Software upgrade required."
+ "PRL metadata"
+ "PRL metadata length"
+ "PRL metadata length missing"
+ "PRL metadata missing"
+ "PRL query failed, treating photo as not revoked: %@"
+ "PRL version is unsupported (expected 1): %ld"
+ "PRL: Full update, clearing existing PRL data"
+ "PRL: Inserting %ld revoked photo IDs"
+ "PRL: Received deprecated flag - PRL is no longer maintained"
+ "PRL: Successfully stored %ld entries%s"
+ "SELECT 1 FROM prl WHERE photo_id = ? LIMIT 1"
+ "SELECT ival FROM admin WHERE key = ? LIMIT 1"
+ "SELECT photo_id FROM prl LIMIT ?"
+ "expected actual "
+ "fullPRLUpdate"
+ "numEntries"
+ "prl_deprecated"
```
