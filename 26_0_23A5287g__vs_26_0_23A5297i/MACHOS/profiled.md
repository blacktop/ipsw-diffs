## profiled

> `/usr/libexec/profiled`

```diff

-2424.0.0.0.0
-  __TEXT.__text: 0xa02dc
+2425.0.0.0.0
+  __TEXT.__text: 0xa0574
   __TEXT.__auth_stubs: 0x20d0
-  __TEXT.__objc_stubs: 0x10580
-  __TEXT.__objc_methlist: 0x5aac
+  __TEXT.__objc_stubs: 0x105c0
+  __TEXT.__objc_methlist: 0x5ad4
   __TEXT.__const: 0x20e
-  __TEXT.__gcc_except_tab: 0x1bec
-  __TEXT.__oslogstring: 0xd736
-  __TEXT.__cstring: 0x8a12
-  __TEXT.__objc_methname: 0x1450a
+  __TEXT.__gcc_except_tab: 0x1c2c
+  __TEXT.__oslogstring: 0xd7de
+  __TEXT.__cstring: 0x8a1e
+  __TEXT.__objc_methname: 0x145bf
   __TEXT.__objc_classname: 0xb5b
-  __TEXT.__objc_methtype: 0x2239
-  __TEXT.__unwind_info: 0x1740
+  __TEXT.__objc_methtype: 0x224d
+  __TEXT.__unwind_info: 0x1748
   __DATA_CONST.__auth_got: 0x1078
-  __DATA_CONST.__got: 0x1bb8
+  __DATA_CONST.__got: 0x1bc0
   __DATA_CONST.__const: 0x1b90
   __DATA_CONST.__cfstring: 0x85c0
   __DATA_CONST.__objc_classlist: 0x2d8

   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA.__objc_const: 0x6580
-  __DATA.__objc_selrefs: 0x48d8
+  __DATA.__objc_const: 0x6588
+  __DATA.__objc_selrefs: 0x48f8
   __DATA.__objc_ivar: 0x200
   __DATA.__objc_data: 0x1c70
   __DATA.__data: 0x540

   - /usr/lib/liblockdown.dylib
   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1109AE11-6E32-3ECE-A7EE-DE846045D7C6
-  Functions: 2043
-  Symbols:   1458
-  CStrings:  6134
+  UUID: 503EF65C-AC18-33E0-8DA0-5FF59D1480E3
+  Functions: 2046
+  Symbols:   1459
+  CStrings:  6142
 
Symbols:
+ _kMDMLAPasscodeContextKey
CStrings:
+ "-[MCInteractionClient requestCurrentPasscodeOutPasscodeContext:isLAContext:]"
+ "B32@0:8^@16^B24"
+ "B36@0:8B16^@20^B28"
+ "Have passcodeContext from ACMContext"
+ "Have passcodeContext from LAContext"
+ "MCFilterOutRestrictionPayloadKeys:"
+ "Unable to create extractable passcode context wrapper from passcode context. Error: %{public}@"
+ "_MCFilterRestrictionPayloadKeys:filterOut:"
+ "_requestCurrentPasscodeExtractable:outPasscodeContext:isLAContext:"
+ "didEnrollInMDMWithPasscode:duringMigration:"
+ "isUpdateFromFactoryVersionRequired"
+ "requestCurrentPasscodeOutPasscodeContext:isLAContext:"
- "-[MCInteractionClient requestCurrentPasscodeOutPasscodeContext:]"
- "B28@0:8B16^@20"
- "_requestCurrentPasscodeExtractable:outPasscodeContext:"
- "requestCurrentPasscodeOutPasscodeContext:"

```
