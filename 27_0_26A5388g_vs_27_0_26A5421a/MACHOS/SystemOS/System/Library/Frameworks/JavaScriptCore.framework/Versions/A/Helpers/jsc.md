## jsc

> `/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`

```diff

-625.1.24.11.2
-  __TEXT.__text: 0x39610
+625.1.29.11.25
+  __TEXT.__text: 0x396f8
   __TEXT.__auth_stubs: 0x1810
   __TEXT.__const: 0x260
-  __TEXT.__cstring: 0x6d2a
+  __TEXT.__cstring: 0x6dad
   __DATA_CONST.__const: 0x1748
   __DATA_CONST.__jsc_ops: 0x0
   __DATA_CONST.__auth_got: 0xc08

   - /usr/lib/libedit.3.dylib
   Functions: 321
   Symbols:   439
-  CStrings:  918
+  CStrings:  922
 
Functions:
~ sub_100018b10 : 1036 -> 820
~ sub_100019b3c -> sub_100019a64 : 36 -> 40
~ sub_10001e4e0 -> sub_10001e40c : 58768 -> 59208
~ sub_10002cbe4 -> sub_10002ccc8 : 24 -> 28
CStrings:
+ "dfgThresholdScaleForLowP0Cores"
+ "ftlThresholdScaleForLowP0Cores"
+ "numberOfP0CoresOverrides"
+ "useB3EliminateWasmGCAllocations"
+ "wasmOMGEntryIncrementSizeReference"
- "useIterationIntrinsics"
```
