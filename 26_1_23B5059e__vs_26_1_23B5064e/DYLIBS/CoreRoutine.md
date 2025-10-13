## CoreRoutine

> `/System/Library/PrivateFrameworks/CoreRoutine.framework/CoreRoutine`

```diff

-1069.0.1.0.0
-  __TEXT.__text: 0x640d8
+1069.0.2.0.0
+  __TEXT.__text: 0x641d4
   __TEXT.__auth_stubs: 0x690
-  __TEXT.__objc_methlist: 0x7d84
+  __TEXT.__objc_methlist: 0x7d9c
   __TEXT.__const: 0x2c8
   __TEXT.__oslogstring: 0x331f
-  __TEXT.__cstring: 0x6466
+  __TEXT.__cstring: 0x64a9
   __TEXT.__gcc_except_tab: 0x368
-  __TEXT.__unwind_info: 0x1e00
+  __TEXT.__unwind_info: 0x1e08
   __TEXT.__objc_classname: 0xf9a
-  __TEXT.__objc_methname: 0xed42
+  __TEXT.__objc_methname: 0xee15
   __TEXT.__objc_methtype: 0x26d7
-  __TEXT.__objc_stubs: 0x74a0
+  __TEXT.__objc_stubs: 0x74c0
   __DATA_CONST.__got: 0x4a0
   __DATA_CONST.__const: 0x1290
   __DATA_CONST.__objc_classlist: 0x458
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2848
+  __DATA_CONST.__objc_selrefs: 0x2858
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x428
   __DATA_CONST.__objc_arraydata: 0x98
   __AUTH_CONST.__auth_got: 0x358
   __AUTH_CONST.__const: 0x3a0
-  __AUTH_CONST.__cfstring: 0x59a0
-  __AUTH_CONST.__objc_const: 0xe230
+  __AUTH_CONST.__cfstring: 0x59c0
+  __AUTH_CONST.__objc_const: 0xe260
+  __AUTH_CONST.__objc_doubleobj: 0x20
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__objc_arrayobj: 0x18
-  __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH.__objc_data: 0x14a0
-  __DATA.__objc_ivar: 0x80c
+  __DATA.__objc_ivar: 0x810
   __DATA.__data: 0x308
   __DATA_DIRTY.__objc_ivar: 0x130
   __DATA_DIRTY.__objc_data: 0x16d0

   - /System/Library/PrivateFrameworks/GeoServices.framework/GeoServices
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 54D3FBFD-2587-3366-8B6D-F9C45C1A0EF7
-  Functions: 2806
-  Symbols:   8761
-  CStrings:  4429
+  UUID: 0CD7079D-062A-375C-8D7E-C8002BDA3EFC
+  Functions: 2808
+  Symbols:   8767
+  CStrings:  4435
 
Symbols:
+ -[RTLocalBluePOIResult distanceToNearestAOILowerBound]
+ -[RTLocalBluePOIResult initWithPOIConfidences:aoiConfidences:distanceToNearestAOILowerBound:referenceLocation:queryTime:]
+ _OBJC_IVAR_$_RTLocalBluePOIResult._distanceToNearestAOILowerBound
+ _objc_msgSend$distanceToNearestAOILowerBound
+ _objc_msgSend$initWithPOIConfidences:aoiConfidences:distanceToNearestAOILowerBound:referenceLocation:queryTime:
- _objc_msgSend$initWithPOIConfidences:aoiConfidences:referenceLocation:queryTime:
CStrings:
+ "T@\"NSNumber\",R,N,V_distanceToNearestAOILowerBound"
+ "_distanceToNearestAOILowerBound"
+ "distanceToNearestAOILowerBound"
+ "initWithPOIConfidences:aoiConfidences:distanceToNearestAOILowerBound:referenceLocation:queryTime:"
+ "poiConfidences, %@, aoiConfidences, %@, referenceLocation, %@, queryTime, %@, distanceToNearestAOILowerBound, %@"
- "poiConfidences, %@, aoiConfidences, %@, referenceLocation, %@, queryTime, %@"

```
