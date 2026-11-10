## DataAccess

> `/System/Library/PrivateFrameworks/DataAccess.framework/Versions/A/DataAccess`

```diff

-2708.0.0.0.0
-  __TEXT.__text: 0x342a0
-  __TEXT.__objc_methlist: 0x3afc
+2708.2.3.0.0
+  __TEXT.__text: 0x343a8
+  __TEXT.__objc_methlist: 0x3b0c
   __TEXT.__const: 0x180
   __TEXT.__gcc_except_tab: 0x153c
   __TEXT.__cstring: 0x2b76

   __DATA_CONST.__objc_catlist: 0x48
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x27b0
+  __DATA_CONST.__objc_selrefs: 0x27b8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x130
   __DATA_CONST.__objc_arraydata: 0x8

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1348
-  Symbols:   3234
+  Functions: 1349
+  Symbols:   3236
   CStrings:  654
 
Symbols:
+ -[DAAccount _removeXpcActivity]
+ _objc_msgSend$_removeXpcActivity
Functions:
~ -[DAAccount shouldCancelTaskDueToOnPowerFetchMode] : 148 -> 180
~ -[DAAccount saveXpcActivity:] : 208 -> 240
~ -[DAAccount hasXpcActivity] : 16 -> 76
~ -[DAAccount incrementXpcActivityContinueCount] : 212 -> 240
~ -[DAAccount decrementXpcActivityContinueCount] : 240 -> 268
~ -[DAAccount removeXpcActivity] : 288 -> 84
+ -[DAAccount _removeXpcActivity]
```
