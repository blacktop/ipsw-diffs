## SEService

> `/System/Library/PrivateFrameworks/SEService.framework/Versions/A/SEService`

```diff

-70.37.0.0.0
-  __TEXT.__text: 0xea114
-  __TEXT.__objc_methlist: 0x32d8
+70.39.1.0.0
+  __TEXT.__text: 0xea19c
+  __TEXT.__objc_methlist: 0x32f0
   __TEXT.__const: 0x160b0
-  __TEXT.__cstring: 0x6b35
+  __TEXT.__cstring: 0x6b65
   __TEXT.__oslogstring: 0x1e17
-  __TEXT.__gcc_except_tab: 0x107c
+  __TEXT.__gcc_except_tab: 0x1088
   __TEXT.__swift5_typeref: 0x3c98
   __TEXT.__constg_swiftt: 0x3304
   __TEXT.__swift5_fieldmd: 0x3534

   __TEXT.__swift_as_cont: 0x2f0
   __TEXT.__swift5_capture: 0xf8
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x4560
+  __TEXT.__unwind_info: 0x4568
   __TEXT.__eh_frame: 0x5820
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0x2a0
   __DATA_CONST.__objc_protolist: 0xc8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x15c0
+  __DATA_CONST.__objc_selrefs: 0x15d0
   __DATA_CONST.__objc_protorefs: 0x70
   __DATA_CONST.__objc_superrefs: 0xd8
   __DATA_CONST.__objc_arraydata: 0xd8
   __DATA_CONST.__got: 0x5e0
   __AUTH_CONST.__const: 0x9d28
-  __AUTH_CONST.__cfstring: 0x35e0
-  __AUTH_CONST.__objc_const: 0x6d10
+  __AUTH_CONST.__cfstring: 0x3620
+  __AUTH_CONST.__objc_const: 0x6d40
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_dictobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__auth_got: 0xc20
   __AUTH.__objc_data: 0x610
   __AUTH.__data: 0xa8
-  __DATA.__objc_ivar: 0x2f8
+  __DATA.__objc_ivar: 0x2fc
   __DATA.__data: 0x2dd8
   __DATA.__bss: 0x186c0
   __DATA.__common: 0x30

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 6214
-  Symbols:   4503
-  CStrings:  1029
+  Functions: 6218
+  Symbols:   4509
+  CStrings:  1031
 
Symbols:
+ -[SEEndPoint revocationReason]
+ -[SEEndPoint setRevocationReason:]
+ OBJC_IVAR_$_SEEndPoint._revocationReason
+ _SESEndPointDeleteWithReason
+ _SESEndPointRevokeWithReason
+ __SESEndPointDeleteWithReason
+ _objc_msgSend$revocationReason
- __SESEndPointDeleteWithSession
CStrings:
+ "\trevocationReason : %@\n"
+ "revocationReason"
```
