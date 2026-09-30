## LinkPresentation

> `/System/Library/Frameworks/LinkPresentation.framework/LinkPresentation`

```diff

-272.13.0.0.0
-  __TEXT.__text: 0xf7fa0
+272.14.0.0.0
+  __TEXT.__text: 0xf8080
   __TEXT.__auth_stubs: 0x19a0
-  __TEXT.__objc_methlist: 0x10214
+  __TEXT.__objc_methlist: 0x1022c
   __TEXT.__cstring: 0x96b0
-  __TEXT.__gcc_except_tab: 0x21c78
-  __TEXT.__const: 0x16e4
+  __TEXT.__gcc_except_tab: 0x21cac
+  __TEXT.__const: 0x1714
   __TEXT.__ustring: 0x3cc
   __TEXT.__oslogstring: 0x37cc
   __TEXT.__dlopen_cstrs: 0xa5e

   __TEXT.__unwind_info: 0x79f8
   __TEXT.__eh_frame: 0x5f8
   __TEXT.__objc_classname: 0x23bf
-  __TEXT.__objc_methname: 0x2091e
+  __TEXT.__objc_methname: 0x20aa3
   __TEXT.__objc_methtype: 0x453e
-  __TEXT.__objc_stubs: 0x181c0
+  __TEXT.__objc_stubs: 0x18200
   __DATA_CONST.__got: 0xd10
   __DATA_CONST.__const: 0x2680
   __DATA_CONST.__objc_classlist: 0x8b8
   __DATA_CONST.__objc_catlist: 0x98
   __DATA_CONST.__objc_protolist: 0x228
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7480
+  __DATA_CONST.__objc_selrefs: 0x74a0
   __DATA_CONST.__objc_protorefs: 0x90
   __DATA_CONST.__objc_superrefs: 0x670
   __DATA_CONST.__objc_arraydata: 0x14f0
   __AUTH_CONST.__auth_got: 0xce8
   __AUTH_CONST.__const: 0x1720
   __AUTH_CONST.__cfstring: 0xd840
-  __AUTH_CONST.__objc_const: 0x2c550
+  __AUTH_CONST.__objc_const: 0x2c590
   __AUTH_CONST.__objc_intobj: 0x288
   __AUTH_CONST.__objc_arrayobj: 0x450
   __AUTH_CONST.__objc_dictobj: 0xc8
   __AUTH_CONST.__objc_doubleobj: 0x60
   __AUTH.__objc_data: 0x2fd0
   __AUTH.__data: 0x438
-  __DATA.__objc_ivar: 0x171c
-  __DATA.__data: 0x1b90
+  __DATA.__objc_ivar: 0x1720
+  __DATA.__data: 0x1b70
   __DATA.__bss: 0x1658
   __DATA.__common: 0x1f0
   __DATA_DIRTY.__objc_data: 0x2968

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 048E5420-6452-3142-BEFE-153B6BBD529F
-  Functions: 6213
-  Symbols:   22421
-  CStrings:  10268
+  UUID: 2F0DCF20-E46F-39DA-9BAD-D5900D27D94A
+  Functions: 6215
+  Symbols:   22428
+  CStrings:  10274
 
Symbols:
+ -[LPMetadataProvider setSourceApplicationSecondaryIdentifierForRequiringPrivacyProxyFailingClosed:]
+ -[LPMetadataProvider sourceApplicationSecondaryIdentifierForRequiringPrivacyProxyFailingClosed]
+ _OBJC_IVAR_$_LPMetadataProvider._sourceApplicationSecondaryIdentifierForRequiringPrivacyProxyFailingClosed
+ ___40-[LPMetadataProvider _fetchSubresources]_block_invoke.121
+ ___40-[LPMetadataProvider _fetchSubresources]_block_invoke.123
+ ___42-[LPMetadataProvider _completedWithError:]_block_invoke.143
+ ___48-[LPMetadataProvider _willStartFetchingMetadata]_block_invoke.31
+ ___72-[LPMetadataProvider startFetchingMetadataForRequest:completionHandler:]_block_invoke.37
+ ___86-[LPMetadataProvider _internalPostProcessResolvedMetadataWithEvent:completionHandler:]_block_invoke.150
+ ___86-[LPMetadataProvider _internalPostProcessResolvedMetadataWithEvent:completionHandler:]_block_invoke.154
+ ___86-[LPMetadataProvider _internalPostProcessResolvedMetadataWithEvent:completionHandler:]_block_invoke_2.152
+ ___86-[LPMetadataProvider _internalPostProcessResolvedMetadataWithEvent:completionHandler:]_block_invoke_2.155
+ ___86-[LPMetadataProvider _internalPostProcessResolvedMetadataWithEvent:completionHandler:]_block_invoke_3.156
+ ___Block_byref_object_copy_.140
+ ___Block_byref_object_dispose_.141
+ _objc_msgSend$_setPrivacyProxyFailClosed:
+ _objc_msgSend$setSourceApplicationSecondaryIdentifier:
- ___40-[LPMetadataProvider _fetchSubresources]_block_invoke.120
- ___40-[LPMetadataProvider _fetchSubresources]_block_invoke.122
- ___42-[LPMetadataProvider _completedWithError:]_block_invoke.141
- ___48-[LPMetadataProvider _willStartFetchingMetadata]_block_invoke.30
- ___72-[LPMetadataProvider startFetchingMetadataForRequest:completionHandler:]_block_invoke.36
- ___86-[LPMetadataProvider _internalPostProcessResolvedMetadataWithEvent:completionHandler:]_block_invoke.149
- ___86-[LPMetadataProvider _internalPostProcessResolvedMetadataWithEvent:completionHandler:]_block_invoke.152
- ___86-[LPMetadataProvider _internalPostProcessResolvedMetadataWithEvent:completionHandler:]_block_invoke_2.151
- ___86-[LPMetadataProvider _internalPostProcessResolvedMetadataWithEvent:completionHandler:]_block_invoke_2.154
- ___86-[LPMetadataProvider _internalPostProcessResolvedMetadataWithEvent:completionHandler:]_block_invoke_3.155
- ___Block_byref_object_copy_.139
- ___Block_byref_object_dispose_.140
CStrings:
+ "T@\"NSString\",C,N,V_sourceApplicationSecondaryIdentifierForRequiringPrivacyProxyFailingClosed"
+ "_setPrivacyProxyFailClosed:"
+ "_sourceApplicationSecondaryIdentifierForRequiringPrivacyProxyFailingClosed"
+ "setSourceApplicationSecondaryIdentifier:"
+ "setSourceApplicationSecondaryIdentifierForRequiringPrivacyProxyFailingClosed:"
+ "sourceApplicationSecondaryIdentifierForRequiringPrivacyProxyFailingClosed"

```
