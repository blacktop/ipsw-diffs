## Trial

> `/System/Library/PrivateFrameworks/Trial.framework/Trial`

```diff

-511.1.2.0.0
-  __TEXT.__text: 0x650f4
-  __TEXT.__objc_methlist: 0x5bdc
+511.2.2.0.0
+  __TEXT.__text: 0x65688
+  __TEXT.__objc_methlist: 0x5bf4
   __TEXT.__const: 0xe22
-  __TEXT.__cstring: 0x8134
-  __TEXT.__oslogstring: 0x434b
-  __TEXT.__gcc_except_tab: 0x5274
+  __TEXT.__cstring: 0x8147
+  __TEXT.__oslogstring: 0x4494
+  __TEXT.__gcc_except_tab: 0x52b4
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x2678
+  __TEXT.__unwind_info: 0x2690
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0xb8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x20
-  __DATA_CONST.__objc_selrefs: 0x2d40
+  __DATA_CONST.__objc_selrefs: 0x2d60
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x280
   __DATA_CONST.__objc_arraydata: 0x150
   __DATA_CONST.__got: 0x6d8
   __AUTH_CONST.__const: 0xd80
-  __AUTH_CONST.__cfstring: 0x60e0
-  __AUTH_CONST.__objc_const: 0xa1c8
+  __AUTH_CONST.__cfstring: 0x6100
+  __AUTH_CONST.__objc_const: 0xa1e8
   __AUTH_CONST.__weak_auth_got: 0x28
   __AUTH_CONST.__objc_intobj: 0x120
   __AUTH_CONST.__objc_dictobj: 0x28

   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xe60
   __AUTH.__data: 0xb8
-  __DATA.__objc_ivar: 0x5cc
+  __DATA.__objc_ivar: 0x5d0
   __DATA.__data: 0xb8b
   __DATA.__common: 0x20
   __DATA_DIRTY.__objc_data: 0x1900

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2096
-  Symbols:   4374
-  CStrings:  1219
+  Functions: 2099
+  Symbols:   4380
+  CStrings:  1225
 
Symbols:
+ -[TRIActiveFactorProvidersParser _resolveExperimentEndDatesMap]
+ -[TRIActiveFactorProvidersParser isExperimentExpired:]
+ GCC_except_table37
+ GCC_except_table41
+ _OBJC_IVAR_$_TRIActiveFactorProvidersParserGuardedData.experimentEndDatesMap
+ ___54-[TRIActiveFactorProvidersParser isExperimentExpired:]_block_invoke
CStrings:
+ "Experiment %{public}@ has expired, not returning experiment identifiers"
+ "Experiment %{public}@ has expired, skipping factor provider"
+ "Experiment %{public}@ has expired, skipping global factor provider"
+ "Experiment end dates mapping does not exist in plplist: %@"
+ "Skipping expired experiment from enumerateActiveExperiments %{public}@"
+ "TrialXP_ClientFramework-511.2.2"
+ "experimentEndDates"
- "TrialXP_ClientFramework-511.1.2"
```
