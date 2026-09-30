## Security

> `/System/Library/Frameworks/Security.framework/Versions/A/Security`

```diff

-61901.160.44.701.4
-  __TEXT.__text: 0x353598
+61901.160.44.702.5
+  __TEXT.__text: 0x353600
   __TEXT.__auth_stubs: 0x4e40
   __TEXT.__delay_helper: 0x264
   __TEXT.__objc_methlist: 0x642c
   __TEXT.__const: 0x18f48
   __TEXT.__dlopen_cstrs: 0x112
-  __TEXT.__cstring: 0x2916c
+  __TEXT.__cstring: 0x29196
   __TEXT.__oslogstring: 0x20ff1
-  __TEXT.__gcc_except_tab: 0x3046c
+  __TEXT.__gcc_except_tab: 0x3047c
   __TEXT.__ustring: 0x40a
   __TEXT.__dof_codesign: 0x2535
   __TEXT.__dof_syspolicy: 0xc27

   - /usr/lib/libz.1.dylib
   Functions: 12656
   Symbols:   25935
-  CStrings:  12609
+  CStrings:  12610
 
Functions:
~ -[AcmeCertRequest acmeRequest] : 1516 -> 1548
~ __ZN8Security11CodeSigning13SecStaticCode17validateDirectoryEv : 5156 -> 5228
CStrings:
+ "CMS has %zu signers, expected exactly one"
```
