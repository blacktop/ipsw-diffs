## CPMLBestShim

> `/System/Library/PrivateFrameworks/CPMLBestShim.framework/CPMLBestShim`

```diff

 117.0.0.0.0
-  __TEXT.__text: 0x378
-  __TEXT.__auth_stubs: 0x110
+  __TEXT.__text: 0x358
   __TEXT.__objc_methlist: 0xac
-  __TEXT.__cstring: 0x2c4
+  __TEXT.__cstring: 0x2c6
   __TEXT.__unwind_info: 0x80
-  __TEXT.__objc_classname: 0x33
-  __TEXT.__objc_methname: 0x13b
-  __TEXT.__objc_methtype: 0x56
-  __TEXT.__objc_stubs: 0x120
-  __DATA_CONST.__got: 0x18
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x120
   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x90
+  __DATA_CONST.__got: 0x18
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x420
   __AUTH_CONST.__objc_const: 0x1f0
+  __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0xf0
   __DATA.__objc_ivar: 0x4
   __DATA.__common: 0x10

   - /System/Library/PrivateFrameworks/CorePrediction.framework/CorePrediction
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 06AFC5A7-90E8-3D71-A3C7-E9B7B1239009
+  UUID: C0B4CD8E-9086-3EA7-A636-B34980C72C03
   Functions: 14
-  Symbols:   117
-  CStrings:  92
+  Symbols:   118
+  CStrings:  67
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x19
Functions:
~ +[CPMLBestAppShim bestShimWithDBPath:withModelPath:withPListPath:] : 84 -> 68
~ -[CPMLBestAppShim rankItems:withMetaInfo:withNumOfRankItem:] : 172 -> 168
~ ___60-[CPMLBestAppShim rankItems:withMetaInfo:withNumOfRankItem:]_block_invoke : 260 -> 248
CStrings:
- ".cxx_destruct"
- "@\"NSArray\""
- "@16@0:8"
- "@40@0:8@16@24@32"
- "@40@0:8@16@24Q32"
- "CPMLBestAppShim"
- "CPMLBestShim"
- "CPMLBestShimContext"
- "T@\"NSArray\",&,VorderedSuggestions"
- "bestShim"
- "bestShimWithDBPath:withModelPath:withPListPath:"
- "copy"
- "count"
- "feedback:withItemsVisited:"
- "integerValue"
- "mutableCopy"
- "orderedSuggestions"
- "rankItems:withMetaInfo:withNumOfRankItem:"
- "removeObjectsInRange:"
- "setOrderedSuggestions:"
- "sortedArrayUsingComparator:"
- "v16@0:8"
- "v24@0:8@16"
- "v32@0:8@16@24"
- "valueForKey:"

```
