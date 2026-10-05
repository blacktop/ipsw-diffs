## DataAccess

> `/System/Library/PrivateFrameworks/DataAccess.framework/DataAccess`

```diff

-2708.1.5.0.0
-  __TEXT.__text: 0x39c78
-  __TEXT.__objc_methlist: 0x488c
+2708.2.2.0.0
+  __TEXT.__text: 0x39d5c
+  __TEXT.__objc_methlist: 0x489c
   __TEXT.__const: 0x190
   __TEXT.__gcc_except_tab: 0x1694
   __TEXT.__cstring: 0x32dc

   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2dc0
+  __DATA_CONST.__objc_selrefs: 0x2dc8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1616
-  Symbols:   2929
+  Functions: 1617
+  Symbols:   2930
   CStrings:  779
 
Symbols:
+ -[DAAccount _removeXpcActivity]
Functions:
~ -[DAAccount shouldCancelTaskDueToOnPowerFetchMode] : 144 -> 172
~ -[DAAccount saveXpcActivity:] : 196 -> 224
~ -[DAAccount hasXpcActivity] : 16 -> 72
~ -[DAAccount incrementXpcActivityContinueCount] : 204 -> 228
~ -[DAAccount decrementXpcActivityContinueCount] : 232 -> 256
~ -[DAAccount removeXpcActivity] : 280 -> 68
+ -[DAAccount _removeXpcActivity]
```
