## CMPhoto

> `/System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto`

```diff

-488.40.6.0.0
-  __TEXT.__text: 0x2966a8
+488.60.5.0.0
+  __TEXT.__text: 0x2c1cac
   __TEXT.__objc_methlist: 0x89c
-  __TEXT.__const: 0x1bf80
-  __TEXT.__cstring: 0x4d867
-  __TEXT.__oslogstring: 0x7f65
+  __TEXT.__const: 0x1cc78
+  __TEXT.__cstring: 0x4f2d1
+  __TEXT.__oslogstring: 0x8247
   __TEXT.__gcc_except_tab: 0x20e4
   __TEXT.__ustring: 0x170
-  __TEXT.__swift5_typeref: 0x1f39
-  __TEXT.__constg_swiftt: 0x3658
-  __TEXT.__swift5_reflstr: 0x4a2c
-  __TEXT.__swift5_fieldmd: 0x4480
-  __TEXT.__swift5_proto: 0x604
-  __TEXT.__swift5_types: 0x344
-  __TEXT.__swift5_capture: 0xd54
-  __TEXT.__swift5_assocty: 0x270
-  __TEXT.__swift5_builtin: 0xdc
-  __TEXT.__swift5_mpenum: 0x60
+  __TEXT.__swift5_typeref: 0x21f2
+  __TEXT.__constg_swiftt: 0x388c
+  __TEXT.__swift5_reflstr: 0x4de4
+  __TEXT.__swift5_fieldmd: 0x4908
+  __TEXT.__swift5_proto: 0x630
+  __TEXT.__swift5_types: 0x398
+  __TEXT.__swift5_capture: 0xf38
+  __TEXT.__swift5_assocty: 0x288
+  __TEXT.__swift5_builtin: 0xf0
+  __TEXT.__swift5_mpenum: 0x68
   __TEXT.__swift5_protos: 0x3c
-  __TEXT.__unwind_info: 0x7e80
-  __TEXT.__eh_frame: 0x6dd4
+  __TEXT.__unwind_info: 0x85b0
+  __TEXT.__eh_frame: 0x8014
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x992c0
+  __DATA_CONST.__const: 0x99460
   __DATA_CONST.__objc_classlist: 0x198
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x10
-  __DATA_CONST.__objc_selrefs: 0xc30
+  __DATA_CONST.__objc_selrefs: 0xc38
   __DATA_CONST.__objc_superrefs: 0x20
   __DATA_CONST.__objc_arraydata: 0x2b0
-  __DATA_CONST.__got: 0x1e88
-  __AUTH_CONST.__const: 0x10140
-  __AUTH_CONST.__cfstring: 0x60ac0
+  __DATA_CONST.__got: 0x1f40
+  __AUTH_CONST.__const: 0x10fe8
+  __AUTH_CONST.__cfstring: 0x60dc0
   __AUTH_CONST.__objc_const: 0x4b58
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x270
   __AUTH_CONST.__objc_arrayobj: 0x210
   __AUTH_CONST.__objc_doubleobj: 0x10
-  __AUTH_CONST.__auth_got: 0x2a68
+  __AUTH_CONST.__auth_got: 0x2af8
   __AUTH.__objc_data: 0x520
-  __AUTH.__data: 0x30c0
+  __AUTH.__data: 0x3288
   __DATA.__objc_ivar: 0x110
-  __DATA.__data: 0x1510
-  __DATA.__common: 0x4ac0
+  __DATA.__data: 0x1698
+  __DATA.__common: 0x4b38
   __DATA_DIRTY.__objc_data: 0xf0
   __DATA_DIRTY.__data: 0x1ff0
   __DATA_DIRTY.__bss: 0x5b8

   - /System/Library/Frameworks/QuartzCore.framework/QuartzCore
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/VideoToolbox.framework/VideoToolbox
+  - /System/Library/PrivateFrameworks/ASRKit.framework/ASRKit
   - /System/Library/PrivateFrameworks/AppleJPEG.framework/AppleJPEG
   - /System/Library/PrivateFrameworks/AppleJPEGXL.framework/AppleJPEGXL
   - /System/Library/PrivateFrameworks/ByteMatrixVerification.framework/ByteMatrixVerification

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 9780
-  Symbols:   12519
-  CStrings:  14043
+  Functions: 10228
+  Symbols:   12671
+  CStrings:  14233
 
Symbols:
+ _CMPhotoAIMarkerCopyBoxInformation
+ _CMPhotoAIMarkerCopyCarryOver
+ _CMPhotoAIMarkerCopyFileAndInsertAIMarker
+ _CMPhotoAIMarkerCopyFileAndModifyAIMarkerInfo
+ _CMPhotoAIMarkerCopyHEIFCodedItems
+ _CMPhotoAIMarkerCopyJFIFLayout
+ _CMPhotoAIMarkerCreateBox
+ _CMPhotoAIMarkerCreateBoxListingHEIFItems
+ _CMPhotoAIMarkerCreateCarriedOverHEIFBox
+ _CMPhotoAIMarkerCreateContentHash
+ _CMPhotoAIMarkerCreateHash
+ _CMPhotoAIMarkerCreateHashComponents
+ _CMPhotoAIMarkerCreateJPEGWithCarriedOverAIMarker
+ _CMPhotoAIMarkerCreateJPEGWithoutAIMarker
+ _CMPhotoAIMarkerCreateJPEGXTSegments
+ _CMPhotoAIMarkerGetJPEGSignedBoxes
+ _CMPhotoAIMarkerModifyBoxSignature
+ _CMPhotoAIMarkerVerify
+ _CMPhotoCompressionSessionAddAIMarker
+ _CMPhotoEvaluateProcessedSigningCertificateChain
+ _CMPhotoGetMPFEntriesFromJFIFByteStream
+ _CMPhotoHEIFFileWriterSetAIMarkerCarryOver
+ _CMPhotoHEIFFileWriterSetAIMarkerPlaceholderBox
+ _CMPhotoSerializeAIMarkerInformation
+ _SecKeyCopyAttributes
+ _SecRandomCopyBytes
+ __DATA__TtC7CMPhoto20JPEGXTBoxReassembler
+ __IVARS__TtC7CMPhoto20JPEGXTBoxReassembler
+ __METACLASS_DATA__TtC7CMPhoto20JPEGXTBoxReassembler
+ ___CMPhotoGetMPFEntriesFromJFIFByteStream_block_invoke
+ ____getFirstMarkerOffset_block_invoke
+ ___swift_closure_destructor.2Tm
+ ___swift_memcpy104_8
+ ___swift_memcpy19_8
+ ___swift_memcpy35_8
+ ___swift_memcpy40_8
+ ___swift_memcpy72_8
+ ___swift_memcpy88_8
+ __addSerializedAIMarker
+ __appendAIMarkerBox
+ __getExistingSignedBoxes
+ __getFirstMarkerOffset
+ __getImageCountFromMPFSegment
+ _asr_check_parser
+ _associated conformance 7CMPhoto17AIMarkerErrorKindOSHAASQ
+ _associated conformance 7CMPhoto19JPEGXTBoxIdentifierVSHAASQ
+ _associated conformance 7CMPhoto23AIMarkerContainerFormatOSHAASQ
+ _associated conformance 7CMPhoto23ProvenanceSignatureDataV17SwiftASN1Internal21DERImplicitlyTaggableAaD12DERParseable
+ _associated conformance 7CMPhoto23ProvenanceSignatureDataV17SwiftASN1Internal21DERImplicitlyTaggableAaD15DERSerializable
+ _associated conformance 7CMPhoto26AIMarkerSignatureAlgorithmOSHAASQ
+ _associated conformance 7CMPhoto26ProvenanceStructureVersionV17SwiftASN1Internal21DERImplicitlyTaggableAaD12DERParseable
+ _associated conformance 7CMPhoto26ProvenanceStructureVersionV17SwiftASN1Internal21DERImplicitlyTaggableAaD15DERSerializable
+ _associated conformance 7CMPhoto29ProvenanceSignatureParametersV17SwiftASN1Internal21DERImplicitlyTaggableAaD12DERParseable
+ _associated conformance 7CMPhoto29ProvenanceSignatureParametersV17SwiftASN1Internal21DERImplicitlyTaggableAaD15DERSerializable
+ _get_enum_tag_for_layout_string 7CMPhoto12AIMarkerSlotV8LocationO
+ _kCMPhotoAIMarkerBoxOption_CertificateChain
+ _kCMPhotoAIMarkerBoxOption_Description
+ _kCMPhotoAIMarkerBoxOption_PlaceholderSignature
+ _kCMPhotoAIMarkerBoxOption_SignatureAlgorithm
+ _kCMPhotoAIMarkerBoxOption_SigningTime
+ _kCMPhotoAIMarkerContentKind_Unknown
+ _kCMPhotoAIMarkerHEIFItem_CodecConfigurations
+ _kCMPhotoAIMarkerHEIFItem_Extents
+ _kCMPhotoAIMarkerHEIFItem_ItemID
+ _kCMPhotoAIMarkerHEIFItem_ItemType
+ _kCMPhotoAIMarkerHashComponent_AIMarkerBoxHash
+ _kCMPhotoAIMarkerHashComponent_CombinedHash
+ _kCMPhotoAIMarkerHashComponent_ContentHash
+ _kCMPhotoAIMarkerHashComponent_SignatureInput
+ _kCMPhotoAIMarkerJFIFLayout_FirstSOSOffset
+ _kCMPhotoAIMarkerJFIFLayout_InsertionOffset
+ _kCMPhotoAIMarkerJFIFLayout_JPEGXTSegmentRanges
+ _kCMPhotoAIMarkerJFIFLayout_MPEntriesBigEndian
+ _kCMPhotoAIMarkerJFIFLayout_MPEntriesOffset
+ _kCMPhotoAIMarkerJFIFLayout_MPEntryCount
+ _kCMPhotoAIMarkerJFIFLayout_MPHeaderOffset
+ _kCMPhotoAIMarkerResult_AIMarkerBoxHash
+ _kCMPhotoAIMarkerResult_AllCodedItemsSigned
+ _kCMPhotoAIMarkerResult_CertificateChainData
+ _kCMPhotoAIMarkerResult_CertificateSecTrustVerified
+ _kCMPhotoAIMarkerResult_CertificateSecTrustVerifiedWithQASigningPolicy
+ _kCMPhotoAIMarkerResult_ContentHash
+ _kCMPhotoAIMarkerResult_ContentKind
+ _kCMPhotoAIMarkerResult_Description
+ _kCMPhotoAIMarkerResult_ListedItemIDs
+ _kCMPhotoAIMarkerResult_SignatureAlgorithmOID
+ _kCMPhotoAIMarkerResult_SignatureVerified
+ _kCMPhotoAIMarkerResult_SigningTime
+ _kCMPhotoAIMarkerResult_SpecVersion
+ _kCMPhotoAIMarkerResult_Verified
+ _kCMPhotoAIMarkerSignatureAlgorithm_CompositeMLDSA87RSA3072PSS
+ _kCMPhotoAIMarkerSignatureAlgorithm_ECDSAP256SHA384
+ _kCMPhotoAIMarkerSignatureAlgorithm_ECDSAP256SHA512
+ _kSecAttrKeySizeInBits
+ _kSecAttrKeyType
+ _kSecAttrKeyTypeECSECPrimeRandom
+ _kSecKeyAlgorithmECDSASignatureMessageX962SHA384
+ _kSecRandomDefault
+ _swift_release_x12
+ _swift_retain_x12
+ _symbolic SDySSypGSg
+ _symbolic SDy_____Say_____GG 10Foundation4DataV s6UInt32V
+ _symbolic SDy_____Say_____GGSg 10Foundation4DataV s6UInt32V
+ _symbolic SDy__________G s6UInt32V 7CMPhoto14HEIFCodedItemsV4ItemV
+ _symbolic SaySny_____GG13segmentRanges_AC04bodyB0_____14instanceNumbert s6UInt64V s6UInt16V
+ _symbolic SaySny_____GGSg s6UInt64V
+ _symbolic Say_____G 7CMPhoto12AIMarkerSlotV
+ _symbolic Say_____G 7CMPhoto9JPEGXTBoxV
+ _symbolic Shy_____G 10Foundation4UUIDV
+ _symbolic Shy_____G s6UInt16V
+ _symbolic SnySiG5range______11replacementt 10Foundation4DataV
+ _symbolic _____ 17SwiftASN1Internal0B16ObjectIdentifierV
+ _symbolic _____ 7CMPhoto10JPEGXTScanV
+ _symbolic _____ 7CMPhoto10MPFEntriesV
+ _symbolic _____ 7CMPhoto11AIMarkerBoxV
+ _symbolic _____ 7CMPhoto12AIMarkerSlotV
+ _symbolic _____ 7CMPhoto12AIMarkerSlotV8LocationO
+ _symbolic _____ 7CMPhoto14HEIFCodedItemsV
+ _symbolic _____ 7CMPhoto14HEIFCodedItemsV4ItemV
+ _symbolic _____ 7CMPhoto17AIMarkerCarryOver021_7E112BE7E9EC9FC9E2E6F9A0069BDE7LLV
+ _symbolic _____ 7CMPhoto17AIMarkerErrorKindO
+ _symbolic _____ 7CMPhoto18AIMarkerFileLayoutV
+ _symbolic _____ 7CMPhoto19AIMarkerStatusErrorV
+ _symbolic _____ 7CMPhoto19JPEGXTBoxIdentifierV
+ _symbolic _____ 7CMPhoto19JPEGXTSegmentHeaderV
+ _symbolic _____ 7CMPhoto20AIMarkerStreamHasherV
+ _symbolic _____ 7CMPhoto20JPEGXTBoxReassemblerC
+ _symbolic _____ 7CMPhoto21AIMarkerSignatureDataO
+ _symbolic _____ 7CMPhoto22AIMarkerHashComponentsV
+ _symbolic _____ 7CMPhoto23AIMarkerContainerFormatO
+ _symbolic _____ 7CMPhoto23AIMarkerDescriptionTypeO
+ _symbolic _____ 7CMPhoto23ProvenanceSignatureDataV
+ _symbolic _____ 7CMPhoto26AIMarkerSignatureAlgorithmO
+ _symbolic _____ 7CMPhoto26ProvenanceStructureVersionV
+ _symbolic _____ 7CMPhoto27AIMarkerSignatureParametersV
+ _symbolic _____ 7CMPhoto29ProvenanceSignatureParametersV
+ _symbolic _____ 7CMPhoto35AIMarkerSignatureParametersEncoding33_12EBF7471ABFBDD8449B11466969801DLLV
+ _symbolic _____ 7CMPhoto9JPEGXTBoxV
+ _symbolic _____ 9CryptoKit6SHA512V
+ _symbolic _____3key______5valuet 10Foundation4UUIDV 7CMPhoto20JPEGXTBoxReassemblerC
+ _symbolic _____3key______5valuet 7CMPhoto19JPEGXTBoxIdentifierV 10Foundation4UUIDV
+ _symbolic _____6offset_t s5Int64V
+ _symbolic _____Sg 7CMPhoto10MPFEntriesV
+ _symbolic _____Sg 7CMPhoto12AIMarkerSlotV
+ _symbolic _____Sg_ABt 17SwiftASN1Internal0B4NodeV
+ _symbolic ___________t 7CMPhoto26ProvenanceStructureVersionV 10Foundation4DataV
+ _symbolic ___________t s5Int32V 7CMPhoto22AIMarkerHashComponentsV
+ _symbolic _____ySnySiG5range______11replacementtG s23_ContiguousArrayStorageC 10Foundation4DataV
+ _symbolic _____ySny_____G5range______14instanceNumbertG s23_ContiguousArrayStorageC s6UInt64V s6UInt16V
+ _symbolic _____y_____ABG s18_DictionaryStorageC s6UInt32V
+ _symbolic _____y_____G 7CMPhoto12GenericErrorV AA08AIMarkerC4KindO
+ _symbolic _____y_____G s11_SetStorageC 7CMPhoto19JPEGXTBoxIdentifierV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 7CMPhoto12AIMarkerSlotV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 7CMPhoto19JPEGXTBoxIdentifierV
+ _symbolic _____y_____G s23_ContiguousArrayStorageC 7CMPhoto9JPEGXTBoxV
+ _symbolic _____y_____SSG s18_DictionaryStorageC s6UInt32V
+ _symbolic _____y_____Say_____GG s18_DictionaryStorageC 10Foundation4DataV s6UInt32V
+ _symbolic _____y__________G s18_DictionaryStorageC 10Foundation4UUIDV 7CMPhoto20JPEGXTBoxReassemblerC
+ _symbolic _____y__________G s18_DictionaryStorageC 7CMPhoto19JPEGXTBoxIdentifierV 10Foundation4UUIDV
+ _symbolic _____y__________G s18_DictionaryStorageC 7CMPhoto19JPEGXTBoxIdentifierV AC0D11ReassemblerC
+ _symbolic _____y__________G s18_DictionaryStorageC s6UInt32V 7CMPhoto14HEIFCodedItemsV4ItemV
+ _type_layout_string 7CMPhoto10JPEGXTScanV
+ _type_layout_string 7CMPhoto10MPFEntriesV
+ _type_layout_string 7CMPhoto11AIMarkerBoxV
+ _type_layout_string 7CMPhoto12AIMarkerSlotV
+ _type_layout_string 7CMPhoto12AIMarkerSlotV8LocationO
+ _type_layout_string 7CMPhoto14HEIFCodedItemsV
+ _type_layout_string 7CMPhoto14HEIFCodedItemsV4ItemV
+ _type_layout_string 7CMPhoto17AIMarkerCarryOver021_7E112BE7E9EC9FC9E2E6F9A0069BDE7LLV
+ _type_layout_string 7CMPhoto18AIMarkerFileLayoutV
+ _type_layout_string 7CMPhoto19AIMarkerStatusErrorV
+ _type_layout_string 7CMPhoto19JPEGXTBoxIdentifierV
+ _type_layout_string 7CMPhoto22AIMarkerHashComponentsV
+ _type_layout_string 7CMPhoto23ProvenanceSignatureDataV
+ _type_layout_string 7CMPhoto26ProvenanceStructureVersionV
+ _type_layout_string 7CMPhoto35AIMarkerSignatureParametersEncoding33_12EBF7471ABFBDD8449B11466969801DLLV
- __DATA__TtC7CMPhotoP33_EC084C477FF75FD5BF0502F9D422061E20JPEGXTBoxReassembler
- __IVARS__TtC7CMPhotoP33_EC084C477FF75FD5BF0502F9D422061E20JPEGXTBoxReassembler
- __METACLASS_DATA__TtC7CMPhotoP33_EC084C477FF75FD5BF0502F9D422061E20JPEGXTBoxReassembler
- ___swift_closure_destructor.157Tm
- _associated conformance 7CMPhoto19JPEGXTBoxIdentifier33_EC084C477FF75FD5BF0502F9D422061ELLVSHAASQ
- _associated conformance 7CMPhoto23ProvenanceSignatureData33_EC084C477FF75FD5BF0502F9D422061ELLV17SwiftASN1Internal21DERImplicitlyTaggableAaE12DERParseable
- _associated conformance 7CMPhoto23ProvenanceSignatureData33_EC084C477FF75FD5BF0502F9D422061ELLV17SwiftASN1Internal21DERImplicitlyTaggableAaE15DERSerializable
- _associated conformance 7CMPhoto26ProvenanceStructureVersion33_EC084C477FF75FD5BF0502F9D422061ELLV17SwiftASN1Internal21DERImplicitlyTaggableAaE12DERParseable
- _associated conformance 7CMPhoto26ProvenanceStructureVersion33_EC084C477FF75FD5BF0502F9D422061ELLV17SwiftASN1Internal21DERImplicitlyTaggableAaE15DERSerializable
- _associated conformance 7CMPhoto29ProvenanceSignatureParameters33_EC084C477FF75FD5BF0502F9D422061ELLV17SwiftASN1Internal21DERImplicitlyTaggableAaE12DERParseable
- _associated conformance 7CMPhoto29ProvenanceSignatureParameters33_EC084C477FF75FD5BF0502F9D422061ELLV17SwiftASN1Internal21DERImplicitlyTaggableAaE15DERSerializable
- _symbolic _____ 7CMPhoto19JPEGXTBoxIdentifier33_EC084C477FF75FD5BF0502F9D422061ELLV
- _symbolic _____ 7CMPhoto19JPEGXTSegmentHeader33_EC084C477FF75FD5BF0502F9D422061ELLV
- _symbolic _____ 7CMPhoto20JPEGXTBoxReassembler33_EC084C477FF75FD5BF0502F9D422061ELLC
- _symbolic _____ 7CMPhoto23ProvenanceSignatureData33_EC084C477FF75FD5BF0502F9D422061ELLV
- _symbolic _____ 7CMPhoto26ProvenanceStructureVersion33_EC084C477FF75FD5BF0502F9D422061ELLV
- _symbolic _____ 7CMPhoto29ProvenanceSignatureParameters33_EC084C477FF75FD5BF0502F9D422061ELLV
- _symbolic _____3key______5valuet 10Foundation4UUIDV 7CMPhoto20JPEGXTBoxReassembler33_EC084C477FF75FD5BF0502F9D422061ELLC
- _symbolic _____3key______5valuet 7CMPhoto19JPEGXTBoxIdentifier33_EC084C477FF75FD5BF0502F9D422061ELLV 10Foundation4UUIDV
- _symbolic _____y__________G s18_DictionaryStorageC 10Foundation4UUIDV 7CMPhoto20JPEGXTBoxReassembler33_EC084C477FF75FD5BF0502F9D422061ELLC
- _symbolic _____y__________G s18_DictionaryStorageC 7CMPhoto19JPEGXTBoxIdentifier33_EC084C477FF75FD5BF0502F9D422061ELLV 10Foundation4UUIDV
- _type_layout_string 7CMPhoto19JPEGXTBoxIdentifier33_EC084C477FF75FD5BF0502F9D422061ELLV
- _type_layout_string 7CMPhoto23ProvenanceSignatureData33_EC084C477FF75FD5BF0502F9D422061ELLV
- _type_layout_string 7CMPhoto26ProvenanceStructureVersion33_EC084C477FF75FD5BF0502F9D422061ELLV
CStrings:
+ "%{public}s: %d"
+ "1.2.840.10045.4.3.3"
+ "1.2.840.10045.4.3.4"
+ "1.3.6.1.5.5.7.6.52"
+ "6BEFF598-F635-480B-B213-D14F40790965"
+ "A file with provenance metadata cannot carry an AI Marker"
+ "AI Marker Box contents do not fit the box size"
+ "AI Marker Box does not map onto its segments"
+ "AI Marker Box field out of range"
+ "AI Marker Box instance number is used by another uuid box"
+ "AI Marker Box segments are not consecutive"
+ "AI Marker Box too large"
+ "AI Marker Box uses a 64-bit length"
+ "AI Marker description is not valid UTF-8"
+ "AI Marker error: %s"
+ "AI Marker functions take a CFData or a file CFURL"
+ "AIMarkerBoxHash"
+ "AllCodedItemsSigned"
+ "Box too large"
+ "CMByteStreamWrite failed: status=%d, wrote=%ld, expected=%ld"
+ "CMPhoto/CMPhotoAIMarker.swift"
+ "CMPhoto/CMPhotoAIMarkerBox.swift"
+ "CMPhoto/CMPhotoAIMarkerContainer.swift"
+ "CMPhotoAIMarkerCopyBoxInformation(_:_:_:)"
+ "CMPhotoAIMarkerCopyCarryOver(_:_:)"
+ "CMPhotoAIMarkerCopyFileAndInsertAIMarker(_:_:_:_:)"
+ "CMPhotoAIMarkerCopyFileAndModifyAIMarkerInfo(_:_:_:_:)"
+ "CMPhotoAIMarkerCreateBoxListingHEIFItems(_:_:_:)"
+ "CMPhotoAIMarkerCreateCarriedOverHEIFBox(_:_:_:)"
+ "CMPhotoAIMarkerCreateContentHash(_:_:_:_:)"
+ "CMPhotoAIMarkerCreateJPEGWithCarriedOverAIMarker(_:_:_:)"
+ "CMPhotoAIMarkerCreateJPEGWithoutAIMarker(_:_:)"
+ "CMPhotoAIMarkerGetJPEGSignedBoxes(_:_:_:)"
+ "CMPhotoAIMarkerModifyBoxSignature(_:_:_:_:)"
+ "CMPhotoAIMarkerVerify(_:_:_:)"
+ "Certificate is not a SEQUENCE"
+ "CertificateChain"
+ "Codec configuration of item is not available"
+ "Codec configuration too large"
+ "CodecConfigurations"
+ "Coded image item has no codec configuration"
+ "ContentKind"
+ "Could not copy the input for writing"
+ "Could not evaluate the certificate chain"
+ "Could not extract the public key of the signing certificate"
+ "Could not generate the AI Marker nonce"
+ "Could not get the length of the input"
+ "Could not open the input for reading"
+ "Could not parse the JPEG marker segments"
+ "Could not parse the signing certificate"
+ "Could not read the HEIF image items"
+ "Could not split the AI Marker Box into segments"
+ "Dropping the AI Marker Box: a listed item was changed or removed"
+ "Dropping the AI Marker Box: its items are too large to fingerprint"
+ "Dropping the AI Marker Box: the file carries provenance metadata"
+ "Dropping the AI Marker Box: the image data changed"
+ "Dropping the AI Marker Box: the rewritten items are too large to fingerprint"
+ "Extensions field does not hold exactly one SEQUENCE"
+ "Extents"
+ "File has more than one or an unreadable AI Marker Box"
+ "FirstSOSOffset"
+ "HEIF AI Marker Box must list at least one item"
+ "HEIF AI Marker carry-over does not match its box"
+ "HEIF AI Marker carry-over has no items"
+ "HEIF file does not start with ftyp"
+ "Input is neither HEIF nor JPEG"
+ "InsertionOffset"
+ "Invalid AI Marker carry-over"
+ "Invalid HEIF item description"
+ "Invalid HEIF item list"
+ "Invalid JFIF layout"
+ "Invalid JPEG-XT segment range"
+ "Invalid SignatureData: %s"
+ "Invalid SignatureParameters: %s"
+ "Invalid codec configuration"
+ "Item data is not available in the file"
+ "Item data too large"
+ "Item listed more than once"
+ "JPEG AI Marker Box must not list items"
+ "JPEG AI Marker carry-over has no Content Hash"
+ "JPEGXTSegmentRanges"
+ "Listed item does not exist"
+ "ListedItemIDs"
+ "ListedItemsByFingerprint"
+ "MP Entries out of bounds"
+ "MP Entry out of range"
+ "MPEntriesBigEndian"
+ "MPEntriesOffset"
+ "MPEntryCount"
+ "MPHeaderOffset"
+ "No AI Marker Box"
+ "No JPEG-XT instance number left"
+ "No JPEG-XT segments"
+ "No byte stream"
+ "No writable copy"
+ "Not a JPEG"
+ "Not an AI Marker Box"
+ "Option must be an integer"
+ "PlaceholderSignature"
+ "Range out of bounds"
+ "Signature algorithm %{public}s is no longer allowed by the AI Marker spec"
+ "Signature algorithm parameters are not supported"
+ "SignatureAlgorithm"
+ "SignatureAlgorithmOID"
+ "SignatureParameters must contain between 1 and 10 certificates"
+ "SignatureVerified"
+ "SigningTime"
+ "Skipping unreadable JPEG-XT segment: %s"
+ "SpecVersion"
+ "The AI Marker Box does not verify for this file"
+ "The AI Marker Box must be the same size as the one it replaces"
+ "The AI Marker Box must list items in a HEIF file and none in a JPEG file"
+ "The AI Marker Box to replace cannot be read"
+ "The AI Marker Box would be larger than 1 MiB"
+ "The Content Hash must be a 64-byte SHA-512"
+ "The file has no coded image item whose Content Hash is defined"
+ "The signature does not verify with the signing certificate"
+ "The signature must not be empty"
+ "Too many items to list in an AI Marker Box"
+ "Too many top-level boxes"
+ "Trailing bytes after SignatureData"
+ "Trailing bytes after SignatureParameters"
+ "Unexpected element in SignatureData"
+ "Unexpected element in SignatureParameters"
+ "Unsupported AI Marker spec_major %hu"
+ "Unsupported SignatureData version"
+ "Unsupported SignatureParameters version"
+ "Unsupported coded image item type"
+ "Unsupported signature algorithm"
+ "Verified"
+ "av01"
+ "avc1"
+ "byteStreamLength(_:)"
+ "certificateChain(options:)"
+ "codecConfiguration(of:)"
+ "com.apple.cmphoto.aimarker"
+ "com.apple.cmphoto.dicom"
+ "com.apple.cmphoto.heics"
+ "com.apple.cmphoto.heif"
+ "com.apple.cmphoto.jfif"
+ "com.apple.cmphoto.jpeg"
+ "com.apple.cmphoto.jpegxl"
+ "com.apple.cmphoto.slim"
+ "com.apple.cmphoto.videotoolbox"
+ "contentHash(byteStream:layout:box:)"
+ "contentHashParameter(_:)"
+ "createByteStreamForReading(_:)"
+ "createWritableCopy(of:)"
+ "data"
+ "descriptionField(options:)"
+ "doesNotFit"
+ "encode(certificates:algorithm:)"
+ "encode(rawSignature:)"
+ "free"
+ "ftyp"
+ "hashComponents(fileData:)"
+ "hashInput(of:byteStream:into:)"
+ "hvc1"
+ "init(byteStream:)"
+ "insertingAIMarkerBox(_:into:layout:)"
+ "insertingJPEGBox(_:into:layout:)"
+ "int64Option(_:_:)"
+ "itemIDsParameter(_:)"
+ "kCMPhotoAIMarkerBoxOption_CertificateChain must hold 1 to 10 certificates"
+ "kCMPhotoAIMarkerBoxOption_CertificateChain must hold DER certificates"
+ "kCMPhotoAIMarkerBoxOption_Description must be a string or data"
+ "kCMPhotoAIMarkerBoxOption_PlaceholderSignature must be non-empty data"
+ "kCMPhotoAIMarkerBoxOption_SignatureAlgorithm must be a kCMPhotoAIMarkerSignatureAlgorithm_* value"
+ "listedItemIDs lists an item more than once"
+ "listedItemIDs must hold 1 to 65535 item IDs"
+ "listedItemIDs must hold item IDs"
+ "listedItemIDs(of:)"
+ "notFound"
+ "publicKeyOfSigningCertificate(_:)"
+ "readWholeInput(_:)"
+ "serializedWithoutPadding(_:)"
+ "signatureAlgorithm(of:)"
+ "signatureAlgorithm(options:)"
+ "signedBoxData(_:rawSignature:contentHash:container:)"
+ "unsignedBox(options:algorithm:itemIDs:)"
+ "unsupportedAlgorithm"
+ "unsupportedSpecVersion"
+ "update(from:range:)"
+ "updateMPFEntries(_:in:entriesOffset:firstImageSizeChange:relativeOffsetChange:)"
+ "utf8"
+ "validateListedItemIDs(_:)"
+ "validatePlacement(of:box:layout:)"
+ "verifyECDSASignature: ECDSA X9.62 %{public}s algorithm not supported by key"
+ "verifyECDSASignature: Signature verification failed"
+ "verifyECDSASignature: Verification failed - %s (code: %ld)"
+ "verifySignature(box:boxData:contentHash:container:)"
+ "writeAIMarkerBox(_:into:byteStream:)"
+ "writeBytes(_:to:at:)"
- "CMPhotoVerifySEPSignature: ECDSA X9.62 SHA-256 algorithm not supported by key"
- "CMPhotoVerifySEPSignature: Signature verification failed"
- "CMPhotoVerifySEPSignature: Verification failed - %s (code: %ld)"
```
