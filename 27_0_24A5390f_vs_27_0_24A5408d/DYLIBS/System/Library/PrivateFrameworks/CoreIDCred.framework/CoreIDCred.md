## CoreIDCred

> `/System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__AUTH_CONST.__cfstring`
- `__AUTH.__objc_data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-9.38.0.0.0
-  __TEXT.__text: 0x3ec00
-  __TEXT.__objc_methlist: 0x204c
+9.42.0.0.0
+  __TEXT.__text: 0x3e7f8
+  __TEXT.__objc_methlist: 0x20ec
   __TEXT.__const: 0x3680
   __TEXT.__cstring: 0x229b
-  __TEXT.__oslogstring: 0x2bbc
+  __TEXT.__oslogstring: 0x317c
   __TEXT.__gcc_except_tab: 0x14
-  __TEXT.__swift5_typeref: 0xcf3
-  __TEXT.__constg_swiftt: 0x800
+  __TEXT.__swift5_typeref: 0xcdf
+  __TEXT.__constg_swiftt: 0x7f4
   __TEXT.__swift5_builtin: 0x1b8
-  __TEXT.__swift5_reflstr: 0x334
-  __TEXT.__swift5_fieldmd: 0x668
+  __TEXT.__swift5_reflstr: 0x324
+  __TEXT.__swift5_fieldmd: 0x650
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__swift5_proto: 0x2cc
   __TEXT.__swift5_types: 0xe8

   __TEXT.__swift_as_entry: 0x6c
   __TEXT.__swift_as_ret: 0x6c
   __TEXT.__swift_as_cont: 0x12c
-  __TEXT.__unwind_info: 0x1510
+  __TEXT.__unwind_info: 0x1548
   __TEXT.__eh_frame: 0x1528
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0xe0
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xc48
+  __DATA_CONST.__objc_selrefs: 0xc70
   __DATA_CONST.__objc_protorefs: 0x30
   __DATA_CONST.__objc_superrefs: 0xa0
-  __DATA_CONST.__got: 0x318
-  __AUTH_CONST.__const: 0x1b80
+  __DATA_CONST.__got: 0x2e0
+  __AUTH_CONST.__const: 0x1c08
   __AUTH_CONST.__cfstring: 0x1560
-  __AUTH_CONST.__objc_const: 0x3740
-  __AUTH_CONST.__auth_got: 0x7e0
+  __AUTH_CONST.__objc_const: 0x3768
+  __AUTH_CONST.__auth_got: 0x798
   __AUTH.__objc_data: 0x240
-  __AUTH.__data: 0x90
   __DATA.__objc_ivar: 0x210
-  __DATA.__data: 0xd40
+  __DATA.__data: 0xcd0
   __DATA.__bss: 0x5980
   __DATA_DIRTY.__objc_data: 0x7d0
   __DATA_DIRTY.__data: 0x160

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2111
-  Symbols:   1921
-  CStrings:  425
+  Functions: 2145
+  Symbols:   1943
+  CStrings:  444
 
Symbols:
+ -[DCCredentialStore deleteCredential:reason:completion:]
+ -[DCCredentialStore deletePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:credentialIdentifier:reason:completion:]
+ -[DCCredentialStore resetCredentialOperationLogForCredential:completion:]
+ -[DCCredentialStore retrieveCredentialOperationLogsWithCompletion:]
+ -[DCCredentialStoreClient deleteCredential:reason:completion:]
+ -[DCCredentialStoreClient deletePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:credentialIdentifier:reason:completion:]
+ -[DCCredentialStoreClient resetCredentialOperationLogForCredential:completion:]
+ -[DCCredentialStoreClient retrieveCredentialOperationLogsWithCompletion:]
+ -[DCCredentialStoreClient storePIIDataInSyncableKeyStoreForIdentifier:data:keystoreType:piiDataType:credentialIdentifier:reason:completion:]
+ ___132-[DCCredentialStore deletePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:credentialIdentifier:reason:completion:]_block_invoke
+ ___138-[DCCredentialStoreClient deletePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:credentialIdentifier:reason:completion:]_block_invoke
+ ___138-[DCCredentialStoreClient deletePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:credentialIdentifier:reason:completion:]_block_invoke_2
+ ___140-[DCCredentialStoreClient storePIIDataInSyncableKeyStoreForIdentifier:data:keystoreType:piiDataType:credentialIdentifier:reason:completion:]_block_invoke
+ ___140-[DCCredentialStoreClient storePIIDataInSyncableKeyStoreForIdentifier:data:keystoreType:piiDataType:credentialIdentifier:reason:completion:]_block_invoke_2
+ ___56-[DCCredentialStore deleteCredential:reason:completion:]_block_invoke
+ ___62-[DCCredentialStoreClient deleteCredential:reason:completion:]_block_invoke
+ ___67-[DCCredentialStore retrieveCredentialOperationLogsWithCompletion:]_block_invoke
+ ___73-[DCCredentialStore resetCredentialOperationLogForCredential:completion:]_block_invoke
+ ___73-[DCCredentialStoreClient retrieveCredentialOperationLogsWithCompletion:]_block_invoke
+ ___73-[DCCredentialStoreClient retrieveCredentialOperationLogsWithCompletion:]_block_invoke_2
+ ___79-[DCCredentialStoreClient resetCredentialOperationLogForCredential:completion:]_block_invoke
+ ___swift_memcpy40_8
+ _objc_msgSend$deleteCredential:reason:completion:
+ _objc_msgSend$deletePIIDataFromSyncableKeyStoreForIdentifier:keystoreType:piiDataType:credentialIdentifier:reason:completion:
+ _objc_msgSend$initWithCredentialIdentifier:presentmentKeyIdentifier:presentmentPublicKey:partition:docType:elements:authACL:readerAuthCertificateData:issuerSignerCertificateData:readerMetadata:readerAnalytics:region:issuingJurisdiction:credentialRevocationInfo:
+ _objc_msgSend$resetCredentialOperationLogForCredential:completion:
+ _objc_msgSend$retrieveCredentialOperationLogsWithCompletion:
+ _objc_msgSend$storePIIDataInSyncableKeyStoreForIdentifier:data:keystoreType:piiDataType:credentialIdentifier:reason:completion:
+ _type_layout_string 10CoreIDCred15DocumentRequestV
- _swift_cvw_initStructMetadataWithLayoutString
- _swift_cvw_initWithTake
- _swift_getEnumTagSinglePayloadGeneric
- _swift_getSingletonMetadata
- _swift_storeEnumTagSinglePayloadGeneric
- _symbolic _____Sg 10Foundation6LocaleV6RegionV
- _symbolic _____Sg_ABt 10Foundation6LocaleV6RegionV
CStrings:
+ "DCCredentialStore deleteCredential:reason:"
+ "DCCredentialStore deletePIIDataFromSyncableKeyStoreForIdentifier:reason:"
+ "DCCredentialStore resetCredentialOperationLogForCredential"
+ "DCCredentialStore retrieveCredentialOperationLogs"
+ "DCCredentialStoreClient deleteCredential:reason:"
+ "DCCredentialStoreClient deleteCredential:reason: returned successfully"
+ "DCCredentialStoreClient deleteCredential:reason: returned with error %{public}@"
+ "DCCredentialStoreClient deletePIIDataFromSyncableKeyStoreForIdentifier:reason:"
+ "DCCredentialStoreClient deletePIIDataFromSyncableKeyStoreForIdentifier:reason: returned successfully"
+ "DCCredentialStoreClient deletePIIDataFromSyncableKeyStoreForIdentifier:reason: returned with error %{public}@"
+ "DCCredentialStoreClient resetCredentialOperationLogForCredential"
+ "DCCredentialStoreClient resetCredentialOperationLogForCredential returned successfully"
+ "DCCredentialStoreClient resetCredentialOperationLogForCredential returned with error %{public}@"
+ "DCCredentialStoreClient retrieveCredentialOperationLogs"
+ "DCCredentialStoreClient retrieveCredentialOperationLogs returned successfully"
+ "DCCredentialStoreClient retrieveCredentialOperationLogs returned with error %{public}@"
+ "DCCredentialStoreClient storePIIDataInSyncableKeyStoreForIdentifier:reason:"
+ "DCCredentialStoreClient storePIIDataInSyncableKeyStoreForIdentifier:reason: returned successfully"
+ "DCCredentialStoreClient storePIIDataInSyncableKeyStoreForIdentifier:reason: returned with error %{public}@"
```
