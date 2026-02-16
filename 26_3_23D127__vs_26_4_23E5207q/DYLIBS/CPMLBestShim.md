## CPMLBestShim

> `/System/Library/PrivateFrameworks/CPMLBestShim.framework/CPMLBestShim`

```diff

 117.0.0.0.0
-  __TEXT.__text: 0x358
-  __TEXT.__auth_stubs: 0x120
+  __TEXT.__text: 0x378
+  __TEXT.__auth_stubs: 0x110
   __TEXT.__objc_methlist: 0xac
   __TEXT.__cstring: 0x2c4
   __TEXT.__unwind_info: 0x80

   __DATA_CONST.__objc_classlist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x70
-  __AUTH_CONST.__auth_got: 0x98
+  __AUTH_CONST.__auth_got: 0x90
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x420
   __AUTH_CONST.__objc_const: 0x1f0

   - /System/Library/PrivateFrameworks/CorePrediction.framework/CorePrediction
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 59A48867-DE78-35C4-B87B-BA3D6DF5339F
+  UUID: 60FBCB62-49A9-3663-BA5B-6679FA769578
   Functions: 14
-  Symbols:   118
+  Symbols:   117
   CStrings:  92
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x19
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
Functions:
~ +[CPMLBestAppShim bestShimWithDBPath:withModelPath:withPListPath:] : 68 -> 84
~ -[CPMLBestAppShim rankItems:withMetaInfo:withNumOfRankItem:] : 168 -> 172
~ ___60-[CPMLBestAppShim rankItems:withMetaInfo:withNumOfRankItem:]_block_invoke : 248 -> 260

```
