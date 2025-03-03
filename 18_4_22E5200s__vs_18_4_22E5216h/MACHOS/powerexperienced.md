## powerexperienced

> `/usr/libexec/powerexperienced`

```diff

-57.100.6.0.0
-  __TEXT.__text: 0xca04
+57.100.8.0.0
+  __TEXT.__text: 0xcbc0
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_stubs: 0x1c80
+  __TEXT.__objc_stubs: 0x1d20
   __TEXT.__objc_methlist: 0x12d4
   __TEXT.__const: 0xd8
-  __TEXT.__cstring: 0x82f
-  __TEXT.__objc_methname: 0x2245
-  __TEXT.__oslogstring: 0x10db
+  __TEXT.__cstring: 0x831
+  __TEXT.__objc_methname: 0x22d9
+  __TEXT.__oslogstring: 0x1155
   __TEXT.__objc_classname: 0x263
   __TEXT.__objc_methtype: 0x659
   __TEXT.__gcc_except_tab: 0x48

   __DATA_CONST.__objc_superrefs: 0x80
   __DATA_CONST.__objc_intobj: 0x48
   __DATA.__objc_const: 0x2bf8
-  __DATA.__objc_selrefs: 0x988
+  __DATA.__objc_selrefs: 0x9b0
   __DATA.__objc_ivar: 0x11c
   __DATA.__objc_data: 0x5a0
   __DATA.__data: 0x3c0

   - /usr/lib/libobjc.A.dylib
   Functions: 402
   Symbols:   140
-  CStrings:  758
+  CStrings:  765
 
CStrings:
+ "COREOS_POWER_EXPERIENCE_POWER_TUNING"
+ "Trial experiment status. treatmentID %@, rolloutID %@, experimentID %@"
+ "Trial:CLPC tuning factor %lld"
+ "Updating CLPCInternal client RPC buffer size tp 16k"
+ "experimentIdentifiersWithNamespaceName:"
+ "numberWithUnsignedInt:"
+ "rolloutIdentifiersWithNamespaceName:"
+ "setRPCBufferSize:"
+ "treatmentIdWithNamespaceName:"
- "CoreOS_PowerExperience_PowerTuning"
- "Trial:CLPC turning factor %lld"

```
