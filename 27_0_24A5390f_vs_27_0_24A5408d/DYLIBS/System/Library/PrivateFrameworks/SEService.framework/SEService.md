## SEService

> `/System/Library/PrivateFrameworks/SEService.framework/SEService`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
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
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`
- `__DATA_DIRTY.__data`

```diff

-70.37.0.0.0
-  __TEXT.__text: 0x11433c
-  __TEXT.__objc_methlist: 0x3cb4
+70.39.1.0.0
+  __TEXT.__text: 0x114224
+  __TEXT.__objc_methlist: 0x3ccc
   __TEXT.__const: 0x18930
-  __TEXT.__gcc_except_tab: 0x1ac8
-  __TEXT.__cstring: 0x8e75
+  __TEXT.__gcc_except_tab: 0x1ab4
+  __TEXT.__cstring: 0x8e85
   __TEXT.__oslogstring: 0x2e57
   __TEXT.__dlopen_cstrs: 0x64
   __TEXT.__swift5_typeref: 0x4430

   __TEXT.__swift_as_cont: 0x374
   __TEXT.__swift5_capture: 0x1e4
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x5388
+  __TEXT.__unwind_info: 0x5380
   __TEXT.__eh_frame: 0x6700
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1b68
+  __DATA_CONST.__objc_selrefs: 0x1b78
   __DATA_CONST.__objc_protorefs: 0xa0
   __DATA_CONST.__objc_superrefs: 0x100
   __DATA_CONST.__objc_arraydata: 0xe8
   __DATA_CONST.__got: 0x740
   __AUTH_CONST.__const: 0xa9f0
-  __AUTH_CONST.__cfstring: 0x46a0
-  __AUTH_CONST.__objc_const: 0x83f8
+  __AUTH_CONST.__cfstring: 0x46e0
+  __AUTH_CONST.__objc_const: 0x8428
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0x118
   __AUTH_CONST.__objc_intobj: 0x78
   __AUTH_CONST.__auth_got: 0x1040
   __AUTH.__objc_data: 0x7c0
   __AUTH.__data: 0xa8
-  __DATA.__objc_ivar: 0x390
+  __DATA.__objc_ivar: 0x394
   __DATA.__data: 0x3750
   __DATA.__bss: 0x1c790
   __DATA.__common: 0x40

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 7228
-  Symbols:   5316
-  CStrings:  1353
+  Functions: 7231
+  Symbols:   5319
+  CStrings:  1355
 
Symbols:
+ -[SEEndPoint revocationReason]
+ -[SEEndPoint setRevocationReason:]
+ GCC_except_table100
+ GCC_except_table102
+ GCC_except_table104
+ GCC_except_table106
+ GCC_except_table108
+ GCC_except_table110
+ GCC_except_table112
+ GCC_except_table114
+ GCC_except_table116
+ GCC_except_table118
+ GCC_except_table120
+ GCC_except_table122
+ GCC_except_table124
+ GCC_except_table131
+ GCC_except_table133
+ GCC_except_table34
+ GCC_except_table37
+ GCC_except_table64
+ GCC_except_table70
+ GCC_except_table74
+ GCC_except_table77
+ GCC_except_table79
+ GCC_except_table81
+ GCC_except_table84
+ GCC_except_table87
+ GCC_except_table91
+ GCC_except_table93
+ GCC_except_table96
+ GCC_except_table98
+ _OBJC_IVAR_$_SEEndPoint._revocationReason
+ _SESEndPointDeleteWithReason
+ _SESEndPointRevokeWithReason
+ __SESEndPointDeleteWithReason
+ ___SESEndPointRevokeWithReason_block_invoke
+ ___SESEndPointRevokeWithReason_block_invoke_2
+ ____SESEndPointDeleteWithReason_block_invoke
+ ___block_descriptor_88_e8_32s40s48s56s64s72r80r_e5_v8?0ls32l8s40l8s48l8s56l8s64l8r72l8r80l8
+ _objc_msgSend$deleteEndPointWithProxy:identifier:mustBeTerminated:reason:reply:
+ _objc_msgSend$listEndPointsWithProxy:reconciliation:reply:
+ _objc_msgSend$revocationReason
+ _objc_msgSend$revokeEndPointWithIdentifier:nonce:metaData:reason:reply:
- GCC_except_table101
- GCC_except_table103
- GCC_except_table105
- GCC_except_table107
- GCC_except_table109
- GCC_except_table111
- GCC_except_table113
- GCC_except_table115
- GCC_except_table117
- GCC_except_table119
- GCC_except_table121
- GCC_except_table123
- GCC_except_table130
- GCC_except_table132
- GCC_except_table31
- GCC_except_table33
- GCC_except_table36
- GCC_except_table48
- GCC_except_table66
- GCC_except_table69
- GCC_except_table72
- GCC_except_table76
- GCC_except_table78
- GCC_except_table80
- GCC_except_table83
- GCC_except_table86
- GCC_except_table90
- GCC_except_table92
- GCC_except_table95
- GCC_except_table97
- GCC_except_table99
- __SESEndPointDeleteWithSession
- ___SESEndPointDelete_block_invoke
- ___SESEndPointRevoke_block_invoke
- ___SESEndPointRevoke_block_invoke_2
- ____SESEndPointDeleteWithSession_block_invoke
- ___block_descriptor_80_e8_32s40s48s56s64r72r_e5_v8?0ls32l8s40l8s48l8s56l8r64l8r72l8
- _objc_msgSend$deleteEndPointWithProxy:identifier:mustBeTerminated:reply:
- _objc_msgSend$listEndPointsWithProxy:mandatoryReconciliation:reply:
- _objc_msgSend$revokeEndPointWithIdentifier:nonce:metaData:reply:
CStrings:
+ "\trevocationReason : %@\n"
+ "SESEndPointRevokeWithReason -> revokeEndPointWithIdentifier"
+ "Unspecified"
+ "_SESEndPointDeleteWithReason -> deleteEndPointWithProxy"
+ "revocationReason"
- "SESEndPointDelete -> deleteEndPointWithProxy"
- "SESEndPointRevoke -> revokeEndPointWithIdentifier"
- "_SESEndPointDeleteWithSession -> deleteEndPointWithProxy"
```
