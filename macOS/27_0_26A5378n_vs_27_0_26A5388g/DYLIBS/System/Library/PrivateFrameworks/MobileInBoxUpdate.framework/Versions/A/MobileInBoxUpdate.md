## MobileInBoxUpdate

> `/System/Library/PrivateFrameworks/MobileInBoxUpdate.framework/Versions/A/MobileInBoxUpdate`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_doubleobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-274.0.0.0.0
-  __TEXT.__text: 0x353a8
-  __TEXT.__objc_methlist: 0x18f0
+274.0.9.0.0
+  __TEXT.__text: 0x354d8
+  __TEXT.__objc_methlist: 0x1900
   __TEXT.__const: 0xbda3
-  __TEXT.__cstring: 0x1881
+  __TEXT.__cstring: 0x18d1
   __TEXT.__gcc_except_tab: 0x234
-  __TEXT.__oslogstring: 0x2659
+  __TEXT.__oslogstring: 0x2679
   __TEXT.__swift5_typeref: 0xdc
   __TEXT.__swift5_fieldmd: 0x30
   __TEXT.__constg_swiftt: 0x64

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xf40
+  __DATA_CONST.__objc_selrefs: 0xf48
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_arraydata: 0x378
   __DATA_CONST.__got: 0x2b8
   __AUTH_CONST.__const: 0x2cc8
-  __AUTH_CONST.__cfstring: 0x1d40
+  __AUTH_CONST.__cfstring: 0x1dc0
   __AUTH_CONST.__objc_const: 0x2870
   __AUTH_CONST.__objc_intobj: 0x1308
   __AUTH_CONST.__objc_arrayobj: 0x3c0

   __AUTH.__objc_data: 0x750
   __AUTH.__data: 0x50
   __DATA.__objc_ivar: 0x1b0
-  __DATA.__data: 0x15f8
+  __DATA.__data: 0x1ca0
   __DATA.__bss: 0x40
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 1422
-  Symbols:   2375
-  CStrings:  492
+  Functions: 1423
+  Symbols:   2380
+  CStrings:  496
 
Symbols:
+ +[MIBUCertHelper _pandoraCertificatesForContext:error:]
+ +[MIBUCertHelper pandoraCertsDataForContext:error:]
+ -[MIBUTestPreferences reportingServerURL]
+ __55+[MIBUCertHelper _pandoraCertificatesForContext:error:]_block_invoke
+ ___55+[MIBUCertHelper _pandoraCertificatesForContext:error:]_block_invoke
+ _fdr_pandoraks_personalization_nonprod_cert_pem
+ _fdr_pandoraks_personalization_nonprod_cert_pem_len
+ _fdr_pandoraks_personalization_prod_cert_pem
+ _fdr_pandoraks_personalization_prod_cert_pem_len
+ _objc_msgSend$_pandoraCertificatesForContext:error:
- +[MIBUCertHelper _pandoraCertificates:]
- +[MIBUCertHelper pandoraCertsData:]
- __39+[MIBUCertHelper _pandoraCertificates:]_block_invoke
- ___39+[MIBUCertHelper _pandoraCertificates:]_block_invoke
- _objc_msgSend$_pandoraCertificates:
CStrings:
+ "ReportingServerURL"
+ "Unrecognized pandora cert context: %@"
+ "Use Pandora Key Server certificates of grade: %{public}@, use case: %{public}@"
+ "personalization"
+ "seaship"
- "Use Pandora Key Server certificates of grade: %{public}@"
```
