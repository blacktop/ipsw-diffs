## libFDRDecode.dylib

> `/usr/lib/libFDRDecode.dylib`

```diff

-1300.120.3.0.0
-  __TEXT.__text: 0xb054
+1499.0.4.0.0
+  __TEXT.__text: 0xb370
   __TEXT.__auth_stubs: 0x240
   __TEXT.__const: 0x8cc
-  __TEXT.__cstring: 0x4c25
-  __TEXT.__unwind_info: 0x1c0
+  __TEXT.__cstring: 0x4d4b
+  __TEXT.__unwind_info: 0x1c8
   __DATA_CONST.__got: 0x10
   __DATA_CONST.__const: 0x180
   __AUTH_CONST.__auth_got: 0x120

   __DATA_DIRTY.__bss: 0x8
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
-  UUID: 27269028-6A4C-3DCF-97F0-6BC84EAE2FF8
-  Functions: 202
-  Symbols:   482
-  CStrings:  426
+  UUID: 43330A8A-BE94-3A95-B78F-95945B73396C
+  Functions: 205
+  Symbols:   485
+  CStrings:  431
 
Symbols:
+ _AMFDRDecodeIterateMultiCombinedDataBeginWithRawData
+ _AMFDRDecodeIterateMultiCombinedDataDestroy
+ _AMFDRDecodeIterateMultiCombinedDataNext
CStrings:
+ "%s: FDR failed to get restitched manifest from multi combined data"
+ "%s: No restitch manifest, but allow unsealed, try to proceed with the data manifest..."
+ "%s: cannot begin with an already initialized iterator"
+ "%s: failed to allocate *multiCombinedDataIterator"
+ "AMFDRDecodeIterateMultiCombinedDataBeginWithRawData"
+ "AMFDRDecodeIterateMultiCombinedDataNext"
- "%s: FDR failed to get manifest from multi combined data"

```
