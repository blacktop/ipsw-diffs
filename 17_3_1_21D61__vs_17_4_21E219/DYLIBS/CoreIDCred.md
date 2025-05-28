## CoreIDCred

> `/System/Library/PrivateFrameworks/CoreIDCred.framework/CoreIDCred`

```diff

-6.300.0.0.0
-  __TEXT.__text: 0x156f0
+6.406.0.0.0
+  __TEXT.__text: 0x15aa0
   __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__objc_methlist: 0x18d8
+  __TEXT.__objc_methlist: 0x1960
   __TEXT.__const: 0x40
-  __TEXT.__cstring: 0x1453
+  __TEXT.__cstring: 0x14d3
   __TEXT.__oslogstring: 0x2dad
   __TEXT.__gcc_except_tab: 0x68
-  __TEXT.__unwind_info: 0x5d8
-  __TEXT.__objc_classname: 0x2e6
-  __TEXT.__objc_methname: 0x3cfe
-  __TEXT.__objc_methtype: 0xdeb
-  __TEXT.__objc_stubs: 0x2100
+  __TEXT.__unwind_info: 0x5f4
+  __TEXT.__objc_classname: 0x30b
+  __TEXT.__objc_methname: 0x3e56
+  __TEXT.__objc_methtype: 0xe16
+  __TEXT.__objc_stubs: 0x2160
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x5f8
-  __DATA_CONST.__objc_classlist: 0xc8
+  __DATA_CONST.__objc_classlist: 0xd0
   __DATA_CONST.__objc_catlist: 0x0
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_const: 0x2b40
-  __DATA_CONST.__objc_selrefs: 0xb08
-  __AUTH_CONST.__objc_const: 0x0
-  __AUTH_CONST.__cfstring: 0x17c0
+  __DATA_CONST.__objc_const: 0x2c10
+  __DATA_CONST.__objc_selrefs: 0xb28
+  __DATA_CONST.__objc_protorefs: 0x18
+  __DATA_CONST.__objc_classrefs: 0xf8
+  __DATA_CONST.__objc_superrefs: 0xd0
+  __AUTH_CONST.__objc_const: 0x90
+  __AUTH_CONST.__cfstring: 0x1840
+  __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__auth_got: 0x1e0
-  __DATA.__objc_protorefs: 0x18
-  __DATA.__objc_classrefs: 0xf0
-  __DATA.__objc_superrefs: 0xc8
-  __DATA.__objc_ivar: 0x20c
+  __AUTH.__objc_data: 0x50
+  __DATA.__objc_ivar: 0x218
   __DATA.__data: 0x2a0
   __DATA.__bss: 0x10
-  __DATA_DIRTY.__const: 0x120
+  __DATA_DIRTY.__const: 0xa0
   __DATA_DIRTY.__objc_const: 0xc18
   __DATA_DIRTY.__objc_data: 0x7d0
   __DATA_DIRTY.__bss: 0x50

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 860
-  Symbols:   2516
-  CStrings:  1156
+  Functions: 869
+  Symbols:   2550
+  CStrings:  1173
 
Symbols:
+ +[DCPresentmentProposalReaderAnalytics supportsSecureCoding]
+ -[DCPresentmentProposal initWithCredentialIdentifier:presentmentKeyIdentifier:presentmentPublicKey:partition:docType:elements:authACL:readerAuthCertificateData:readerMetadata:readerAnalytics:]
+ -[DCPresentmentProposal readerAnalytics]
+ -[DCPresentmentProposalReaderAnalytics .cxx_destruct]
+ -[DCPresentmentProposalReaderAnalytics description]
+ -[DCPresentmentProposalReaderAnalytics encodeWithCoder:]
+ -[DCPresentmentProposalReaderAnalytics initWithCoder:]
+ -[DCPresentmentProposalReaderAnalytics initWithUntrustedIdentifier:untrustedOrganization:]
+ -[DCPresentmentProposalReaderAnalytics untrustedIdentifier]
+ -[DCPresentmentProposalReaderAnalytics untrustedOrganization]
+ _OBJC_CLASS_$_DCPresentmentProposalReaderAnalytics
+ _OBJC_IVAR_$_DCPresentmentProposal._readerAnalytics
+ _OBJC_IVAR_$_DCPresentmentProposalReaderAnalytics._untrustedIdentifier
+ _OBJC_IVAR_$_DCPresentmentProposalReaderAnalytics._untrustedOrganization
+ _OBJC_METACLASS_$_DCPresentmentProposalReaderAnalytics
+ __OBJC_$_CLASS_METHODS_DCPresentmentProposalReaderAnalytics
+ __OBJC_$_CLASS_PROP_LIST_DCPresentmentProposalReaderAnalytics
+ __OBJC_$_INSTANCE_METHODS_DCPresentmentProposalReaderAnalytics
+ __OBJC_$_INSTANCE_VARIABLES_DCPresentmentProposalReaderAnalytics
+ __OBJC_$_PROP_LIST_DCPresentmentProposalReaderAnalytics
+ __OBJC_CLASS_PROTOCOLS_$_DCPresentmentProposalReaderAnalytics
+ __OBJC_CLASS_RO_$_DCPresentmentProposalReaderAnalytics
+ __OBJC_METACLASS_RO_$_DCPresentmentProposalReaderAnalytics
+ ___52-[DCPresentmentSession interpretRequest:completion:]_block_invoke.473
+ ___61-[DCPresentmentSession buildResponseForSelection:completion:]_block_invoke.474
+ ___64-[DCPresentmentSession buildErrorResponseWithStatus:completion:]_block_invoke.476
+ ___71-[DCPresentmentSession buildCredentialResponseForSelection:completion:]_block_invoke.475
+ ___72-[DCPresentmentSession generateTransportKeyForSpecification:completion:]_block_invoke.472
+ ___block_literal_global.155
+ ___block_literal_global.201
+ ___block_literal_global.205
+ ___block_literal_global.99
+ _objc_msgSend$readerAnalytics
+ _objc_msgSend$untrustedIdentifier
+ _objc_msgSend$untrustedOrganization
- -[DCPresentmentProposal initWithCredentialIdentifier:presentmentKeyIdentifier:presentmentPublicKey:partition:docType:elements:authACL:readerAuthCertificateData:readerMetadata:]
- ___52-[DCPresentmentSession interpretRequest:completion:]_block_invoke.440
- ___61-[DCPresentmentSession buildResponseForSelection:completion:]_block_invoke.441
- ___64-[DCPresentmentSession buildErrorResponseWithStatus:completion:]_block_invoke.443
- ___71-[DCPresentmentSession buildCredentialResponseForSelection:completion:]_block_invoke.442
- ___72-[DCPresentmentSession generateTransportKeyForSpecification:completion:]_block_invoke.439
- ___block_literal_global.154
- ___block_literal_global.200
- ___block_literal_global.204
- ___block_literal_global.98
CStrings:
+ "\n"
+ "<%@ %p; credentialIdentifier = %@; presentmentKeyIdentifier = %@; partition = %@; docType = %@; elements = %@; readerMetadata = %@>"
+ "<%@ %p; untrustedIdentifier = %@; untrustedOrganization = %@>"
+ "@\"DCPresentmentProposalReaderAnalytics\""
+ "@96@0:8@16@24@32@40@48@56@64@72@80@88"
+ "DCPresentmentProposalReaderAnalytics"
+ "T@\"DCPresentmentProposalReaderAnalytics\",R,N,V_readerAnalytics"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,N,V_untrustedIdentifier"
+ "T@\"NSString\",R,N,V_untrustedOrganization"
+ "_readerAnalytics"
+ "_untrustedIdentifier"
+ "_untrustedOrganization"
+ "initWithCredentialIdentifier:presentmentKeyIdentifier:presentmentPublicKey:partition:docType:elements:authACL:readerAuthCertificateData:readerMetadata:readerAnalytics:"
+ "initWithUntrustedIdentifier:untrustedOrganization:"
+ "readerAnalytics"
+ "untrustedIdentifier"
+ "untrustedOrganization"
- "\t"
- "@88@0:8@16@24@32@40@48@56@64@72@80"
- "DCPresentmentProposal credentialIdentifier = %@, presentmentKeyIdentifier = %@, partition = %@, docType = %@, elements = %@"
- "initWithCredentialIdentifier:presentmentKeyIdentifier:presentmentPublicKey:partition:docType:elements:authACL:readerAuthCertificateData:readerMetadata:"

```
