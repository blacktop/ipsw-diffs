## Security

> `/System/Library/Frameworks/Security.framework/Security`

```diff

-61439.140.8.0.0
-  __TEXT.__text: 0x1736ec
+61439.140.10.0.0
+  __TEXT.__text: 0x173524
   __TEXT.__auth_stubs: 0x3e50
   __TEXT.__objc_methlist: 0x6008
   __TEXT.__const: 0xb950
   __TEXT.__dlopen_cstrs: 0x359
   __TEXT.__cstring: 0x17d7b
-  __TEXT.__gcc_except_tab: 0x8c18
+  __TEXT.__gcc_except_tab: 0x8bb4
   __TEXT.__oslogstring: 0xf0f2
   __TEXT.__ustring: 0x406
   __TEXT.__dof_codesign: 0x1ffd

   - /usr/lib/libcoretls_cfhelpers.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 07AD0C37-B991-3658-9199-76332F0C1561
+  UUID: 5FA37C31-2A4E-3E62-AA54-7E1B2B4F5A6C
   Functions: 6814
   Symbols:   20176
   CStrings:  10917
Functions:
~ __ZN8Security11SecCFObject6handleEb : 120 -> 140
~ __ZN8Security14SecPointerBaseC2EPNS_11SecCFObjectE : 108 -> 132
~ __ZN8Security14SecPointerBaseD2Ev : 88 -> 104
~ __ZN8Security14SecPointerBase6assignEPNS_11SecCFObjectE : 152 -> 188
~ _SecCodeSignerCreate : 832 -> 776
~ __ZN8Security11CodeSigning11FileDiskRep19defaultRequirementsEPKNS_12ArchitectureERKNS0_7DiskRep14SigningContextE : 1104 -> 1056
~ ____ZN8Security11CodeSigning13SecStaticCode14reportProgressEj_block_invoke : 224 -> 196
~ __ZN8Security11CodeSigning13SecStaticCode16validateResourceEPK14__CFDictionaryNSt3__112basic_stringIcNS5_11char_traitsIcEENS5_9allocatorIcEEEEbRNS1_17ValidationContextEjj : 6700 -> 6596
~ __ZN8Security11CodeSigning13SecStaticCode14staticValidateEjPKNS0_14SecRequirementE : 4020 -> 3964
~ __ZN8Security11CodeSigning13SecStaticCode23visitOtherArchitecturesEU13block_pointerFvPS1_E : 1384 -> 1332
~ __ZN8Security11CodeSigning13SecStaticCode22staticValidateResourceENSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEjPKNS0_14SecRequirementE : 4460 -> 4408
~ ____ZN8Security11CodeSigning13SecStaticCode22staticValidateResourceENSt3__112basic_stringIcNS2_11char_traitsIcEENS2_9allocatorIcEEEEjPKNS0_14SecRequirementE_block_invoke : 1288 -> 1240
~ ____ZN8Security11CodeSigning13SecCodeSigner6Signer14buildResourcesENSt3__112basic_stringIcNS3_11char_traitsIcEENS3_9allocatorIcEEEES9_PK14__CFDictionary_block_invoke_2 : 2452 -> 2396
~ _SecCodeSignerRemoteCreate : 1180 -> 1128

```
