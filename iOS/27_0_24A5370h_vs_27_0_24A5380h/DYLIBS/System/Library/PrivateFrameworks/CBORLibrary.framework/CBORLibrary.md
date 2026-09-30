## CBORLibrary

> `/System/Library/PrivateFrameworks/CBORLibrary.framework/CBORLibrary`

```diff

-  __TEXT.__text: 0x28814
+  __TEXT.__text: 0x2b444
   __TEXT.__objc_methlist: 0x604
-  __TEXT.__const: 0x1848
-  __TEXT.__cstring: 0xab1
-  __TEXT.__swift5_typeref: 0x458
+  __TEXT.__const: 0x1878
+  __TEXT.__cstring: 0xc6d
+  __TEXT.__swift5_typeref: 0x474
   __TEXT.__swift5_reflstr: 0x271
   __TEXT.__swift5_assocty: 0x90
   __TEXT.__swift5_fieldmd: 0x410
   __TEXT.__constg_swiftt: 0x734
-  __TEXT.__swift5_capture: 0x100
+  __TEXT.__swift5_capture: 0x110
   __TEXT.__swift5_builtin: 0x3c
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_proto: 0xc0
   __TEXT.__swift5_types: 0x68
   __TEXT.__swift5_mpenum: 0x8
-  __TEXT.__oslogstring: 0x75
+  __TEXT.__oslogstring: 0x9a2
   __TEXT.__gcc_except_tab: 0x2c
-  __TEXT.__unwind_info: 0xa38
-  __TEXT.__eh_frame: 0x1c40
+  __TEXT.__unwind_info: 0xa40
+  __TEXT.__eh_frame: 0x1c70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0xc0
+  __DATA_CONST.__const: 0x100
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x590
+  __DATA_CONST.__objc_selrefs: 0x5b0
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA_CONST.__got: 0x238
-  __AUTH_CONST.__const: 0x938
+  __DATA_CONST.__got: 0x250
+  __AUTH_CONST.__const: 0x978
   __AUTH_CONST.__cfstring: 0x840
   __AUTH_CONST.__objc_const: 0xf50
   __AUTH_CONST.__objc_intobj: 0x210
-  __AUTH_CONST.__auth_got: 0x9f8
+  __AUTH_CONST.__auth_got: 0xa40
+  __AUTH.__objc_data: 0x98
   __DATA.__objc_ivar: 0x6c
-  __DATA.__data: 0x2e0
-  __DATA.__common: 0x18
+  __DATA.__data: 0x2f8
+  __DATA.__common: 0x28
   __DATA.__bss: 0x1100
-  __DATA_DIRTY.__objc_data: 0x2b8
+  __DATA_DIRTY.__objc_data: 0x220
   __DATA_DIRTY.__data: 0x758
   __DATA_DIRTY.__bss: 0x700
   - /System/Library/Frameworks/Combine.framework/Combine

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 912
-  Symbols:   892
-  CStrings:  182
+  Functions: 914
+  Symbols:   925
+  CStrings:  255
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__swift5_fieldmd : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_mpenum : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __AUTH_CONST.__cfstring : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __DATA_DIRTY.__data : content changed
Symbols:
+ _OBJC_CLASS_$_NSMutableSet
+ __NSConcreteGlobalBlock
+ ___38-[CBOR _calculateDictionaryHash:hash:]_block_invoke
+ ____randomHashSeed_block_invoke
+ ___block_descriptor_32_e15_i24?0r^v8r^v16l
+ ___block_descriptor_tmp
+ ___block_literal_global
+ ___unnamed_35
+ __os_log_impl
+ __randomHashSeed.once
+ __randomHashSeed.seed
+ _abort
+ _arc4random_buf
+ _cbor_fnv1a_hash
+ _cbor_fnv1a_hash_64
+ _cbor_fnv1a_hash_with_offsetBasis
+ _cbor_fnv1a_hash_with_offsetBasis_64
+ _dispatch_once
+ _free
+ _malloc_type_calloc
+ _objc_msgSend$containsObject:
+ _objc_msgSend$initWithArray:
+ _objc_msgSend$isEqual:
+ _objc_msgSend$isEqualToArray:
+ _objc_msgSend$isEqualToDictionary:
+ _qsort_b
+ _swift_getAssociatedConformanceWitness
+ _swift_getAssociatedTypeWitness
+ _swift_release_x24
+ _swift_unknownObjectRelease_n
+ _symbolic SDy_____SE_pG s11AnyHashableV
+ _symbolic Sz_p
+ _symbolic _____3key_SE_p5valuet s11AnyHashableV
- ___30-[COSE _searchForHeaderLabel:]_block_invoke_2
- ___unnamed_34
- _swift_release_x28
- _symbolic _____y_____G s23_ContiguousArrayStorageC s5UInt8V
CStrings:
+ "%s: Algorithm %@ not implemented."
+ "%s: Allocation failure"
+ "%s: COSEContentType %ld does not match tag %{private}@"
+ "%s: Duplicated key found, %{private}@"
+ "%s: Encoded item is not well-formed, header=0x%02X"
+ "%s: Error interpreting date time string: %{private}@"
+ "%s: Error interpreting date time string: %{public}@"
+ "%s: Failure decoding infinite item list"
+ "%s: Indefinite-length string violates internal invariant"
+ "%s: Insufficient data"
+ "%s: Invalid CBOR data type in indefinite-length string"
+ "%s: Invalid COSE data type: %{private}@"
+ "%s: Invalid COSE tag for message identification: %ld"
+ "%s: Invalid COSE_Sign1 data type: %lu"
+ "%s: Invalid UTF8 string"
+ "%s: Invalid data length!  Dropping rest of data as CBOR is invalid"
+ "%s: Invalid data marked by Tag 24"
+ "%s: Invalid format string, %{private}@"
+ "%s: Invalid fractional digits, %{private}@"
+ "%s: Invalid payload type: %lu"
+ "%s: Invalid protected header: %{private}@"
+ "%s: Invalid string length, %{private}@"
+ "%s: Invalid time string, %{private}@"
+ "%s: Invalid timezone format, %{private}@"
+ "%s: Invalid timezone specifier, %{private}@"
+ "%s: Major type 1 negative int64 underflow"
+ "%s: Malformed chunk found in indefinite-length string"
+ "%s: Malformed map; mismatch in expected entries"
+ "%s: Missing data length"
+ "%s: Missing termination break in indefinite-length string"
+ "%s: Missing unprotected header"
+ "%s: Nested indefinite-length string found"
+ "%s: No chunks found; creates empty string"
+ "%s: Not implemented counter signature parsing"
+ "%s: Number of items is greater than buffer size"
+ "%s: Only %zu fractional digits is supported"
+ "%s: ParseHeader: COSE Header-IV"
+ "%s: ParseHeader: COSE Header-algo"
+ "%s: ParseHeader: COSE Header-contentType"
+ "%s: ParseHeader: COSE Header-counter signature"
+ "%s: ParseHeader: COSE Header-crit"
+ "%s: ParseHeader: COSE Header-kid"
+ "%s: ParseHeader: COSE Header-partial IV"
+ "%s: Protected header decode failure"
+ "%s: RSA key support not implemented."
+ "%s: Skipping unexpected label: %{private}@"
+ "%s: Unexpected # of elements in COS structure: %lu"
+ "%s: Unexpected COSE key type: %lu"
+ "%s: Unexpected KTY type: %lu"
+ "%s: Unexpected characters after timezone, %{private}@"
+ "%s: Unexpected data chunk"
+ "%s: Unexpected key type: %{private}@, value: %{private}@"
+ "%s: Unexpected payload: %{private}@"
+ "%s: Unexpected signature: %{private}@"
+ "%s: Unexpected tag type: %{private}@"
+ "%s: Unexpected tag: %{private}@"
+ "%s: Unexpected type: %{private}@"
+ "%s: key is nil"
+ "-[CBOR _calculateDictionaryHash:hash:]"
+ "-[CBOR(Decoder) asJSON]"
+ "-[COSE _getProtectedHeadererDictionary:]"
+ "-[COSE _parseCommonHeaderParameters:]"
+ "-[COSE _parseCommonStructure:]"
+ "-[COSE _searchForHeaderLabel:]_block_invoke"
+ "-[COSE initWithCBOR:]"
+ "-[COSE initWithData:type:]"
+ "-[COSEKey initWithCBOR:]"
+ "-[COSE_Mac0 initWithCBOR:]"
+ "-[COSE_Sign1 initWithCBOR:]"
+ "NSDate *parseDateString(NSString *__strong)"
+ "Unsupported type for CodingKey "
+ "i24@?0r^v8r^v16"
+ "v8@?0"

```
