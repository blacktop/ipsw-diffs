## libswiftDemangle.dylib

> `/usr/lib/swift/libswiftDemangle.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__weak_auth_got`

```diff

-6.4.0.27.101
-  __TEXT.__text: 0x59da0
-  __TEXT.__cstring: 0x5380
+6.4.0.31.4
+  __TEXT.__text: 0x59fec
+  __TEXT.__cstring: 0x539c
   __TEXT.__const: 0x158
   __TEXT.__unwind_info: 0x758
   __TEXT.__auth_stubs: 0x0

   - /usr/lib/libc++.1.dylib
   Functions: 667
   Symbols:   664
-  CStrings:  1345
+  CStrings:  1346
 
Functions:
~ sub_2c255818c -> sub_2c231618c : 48 -> 52
~ __ZN5swift8Demangle9Demangler30demangleFunctionSpecializationEv : 1096 -> 1104
~ __ZN5swift8Demangle9Demangler21demangleFuncSpecParamENS0_4Node4KindE : 2856 -> 2992
~ __ZN5swift8Demangle11NodePrinter5printEPNS0_4NodeEjb : 27628 -> 27640
~ __ZN5swift8Demangle11NodePrinter36printFunctionSigSpecializationParamsEPNS0_4NodeEj : 2760 -> 2792
~ __ZN12_GLOBAL__N_19Remangler42mangleFunctionSignatureSpecializationParamEPN5swift8Demangle4NodeEj : 6148 -> 6544
CStrings:
+ "Escaping Closure Propagated"
```
