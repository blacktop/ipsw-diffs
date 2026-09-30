## libFDRDecode.dylib

> `/usr/lib/libFDRDecode.dylib`

```diff

-1300.40.2.0.0
-  __TEXT.__text: 0xa2e0
+1300.60.12.0.0
+  __TEXT.__text: 0xa70c
   __TEXT.__auth_stubs: 0x230
   __TEXT.__const: 0x8b4
-  __TEXT.__cstring: 0x4ab6
-  __TEXT.__unwind_info: 0x190
+  __TEXT.__cstring: 0x4c25
+  __TEXT.__unwind_info: 0x1a0
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x180
   __AUTH_CONST.__auth_got: 0x118

   __DATA_DIRTY.__bss: 0x8
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
-  Functions: 101
-  Symbols:   138
-  CStrings:  419
+  Functions: 104
+  Symbols:   141
+  CStrings:  426
 
Symbols:
+ _AMFDRDecodeVerifyMultiCombinedDataIntegrity
CStrings:
+ "%!s(MISSING): Failed to get payload sequence and set manifest from multi combined data"
+ "%!s(MISSING): combinedData is required to be set"
+ "%!s(MISSING): found an empty data class in multi combined data"
+ "AMFDRDecodeVerifyMultiCombinedDataIntegrity"
+ "_AMFDRDecodeFindDataFromMultiCombined"
+ "_AMFDRDecodeGetPayloadSeqAndSetManifestFromMultiCombinedData"
+ "_AMFDRDecodeTolerateErrorsForOptions"
+ "_AMFDRDecodeVerifyMultiCombinedDataInternal"
- "_AMFDRDecodeMultiCombined"

```
