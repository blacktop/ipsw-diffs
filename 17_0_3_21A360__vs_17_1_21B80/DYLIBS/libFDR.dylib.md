## libFDR.dylib

> `/usr/lib/libFDR.dylib`

```diff

-1113.0.11.0.0
-  __TEXT.__text: 0x6d024
-  __TEXT.__auth_stubs: 0x12c0
+1113.40.6.0.0
+  __TEXT.__text: 0x6d260
+  __TEXT.__auth_stubs: 0x12d0
   __TEXT.__const: 0x1f03
-  __TEXT.__cstring: 0x1e04a
+  __TEXT.__cstring: 0x1e172
   __TEXT.__ustring: 0x38
   __TEXT.__unwind_info: 0x9c8
   __TEXT.__objc_methname: 0x22
   __TEXT.__objc_stubs: 0x20
   __DATA_CONST.__got: 0xe8
-  __DATA_CONST.__const: 0x8c8
+  __DATA_CONST.__const: 0x8f8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x8
-  __AUTH_CONST.__const: 0x900
-  __AUTH_CONST.__cfstring: 0xd6c0
-  __AUTH_CONST.__auth_ptr: 0x30
-  __AUTH_CONST.__auth_got: 0x968
+  __AUTH_CONST.__const: 0x920
+  __AUTH_CONST.__cfstring: 0xd7a0
+  __AUTH_CONST.__auth_ptr: 0x38
+  __AUTH_CONST.__auth_got: 0x970
   __DATA.__objc_classrefs: 0x8
-  __DATA.__data: 0x150
-  __DATA.__bss: 0xd8
+  __DATA.__data: 0x158
+  __DATA.__bss: 0xe8
   __DATA_DIRTY.__data: 0x20
   __DATA_DIRTY.__bss: 0xc0
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libamsupport.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 800
-  Symbols:   2042
-  CStrings:  3617
+  Functions: 802
+  Symbols:   2052
+  CStrings:  3628
 
Symbols:
+ _AMFDRSealingMapCopyDataInstanceForSealingMapEntry
+ _AMFDRSealingMapSetKeyQueryRetry
+ _ZhuGeCopyValue
+ ____isZhuGeLegacyAvailable_block_invoke
+ ___block_descriptor_tmp.1054
+ ___block_descriptor_tmp.1058
+ ___block_descriptor_tmp.1069
+ ___block_descriptor_tmp.1143
+ ___block_descriptor_tmp.1203
+ ___block_descriptor_tmp.1206
+ ___block_descriptor_tmp.1354
+ ___block_descriptor_tmp.193
+ ___block_literal_global.1056
+ ___block_literal_global.1060
+ ___block_literal_global.1071
+ ___block_literal_global.1205
+ ___block_literal_global.1208
+ __isZhuGeLegacyAvailable.isAvailable
+ __isZhuGeLegacyAvailable.onceToken
+ _gKeyQueryRetry
- _AMFDRSealingMapCopyDataInstanceForSealingMapEntryNoRetry
- ___block_descriptor_tmp.1039
- ___block_descriptor_tmp.1043
- ___block_descriptor_tmp.1117
- ___block_descriptor_tmp.1177
- ___block_descriptor_tmp.1180
- ___block_descriptor_tmp.1328
- ___block_descriptor_tmp.178
- ___block_literal_global.1041
- ___block_literal_global.1045
- ___block_literal_global.1179
- ___block_literal_global.1182
CStrings:
+ "AMFDRSealingMapCallMGCopyAnswer %@ for %@, error=%d."
+ "AMFDRSealingMapCallMGCopyAnswer failed for %@, error=%@."
+ "CFNumberCreate failed for retryNumber/retryInterval"
+ "RetryInterval"
+ "RetryNumber"
+ "ZhuGeCopyValue is unavailable!"
+ "ZhuGeCopyValue symbol is not supported"
+ "ZhuGeCopyValueWithError failed: %d"
+ "ZhuGeCopyValueWithError is unavailable!"
+ "_createZhuGePreferences"
+ "_createZhuGePreferences failed"
+ "_isZhuGeLegacyAvailable_block_invoke"
+ "failed"
+ "timed out waiting"
- "AMFDRSealingMapCallMGCopyAnswer failed for %@, error=%d."
- "AMFDRSealingMapCallMGCopyAnswer timed out waiting for %@, error=%d."
- "ZhuGeSupport is unavailable!"

```
