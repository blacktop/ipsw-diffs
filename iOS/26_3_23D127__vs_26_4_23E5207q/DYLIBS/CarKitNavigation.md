## CarKitNavigation

> `/System/Library/PrivateFrameworks/CarKitNavigation.framework/CarKitNavigation`

```diff

-746.24.2.0.0
-  __TEXT.__text: 0x68d0
-  __TEXT.__auth_stubs: 0x330
-  __TEXT.__objc_methlist: 0x954
+774.8.0.0.0
+  __TEXT.__text: 0x7280
+  __TEXT.__auth_stubs: 0x2f0
+  __TEXT.__objc_methlist: 0x974
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x36f
-  __TEXT.__oslogstring: 0x897
+  __TEXT.__cstring: 0x387
+  __TEXT.__oslogstring: 0x8d7
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x230
-  __TEXT.__objc_classname: 0x157
-  __TEXT.__objc_methname: 0x15b7
+  __TEXT.__unwind_info: 0x258
+  __TEXT.__objc_classname: 0x159
+  __TEXT.__objc_methname: 0x1637
   __TEXT.__objc_methtype: 0x4d1
-  __TEXT.__objc_stubs: 0xfc0
+  __TEXT.__objc_stubs: 0x1040
   __DATA_CONST.__got: 0xd0
   __DATA_CONST.__const: 0x130
   __DATA_CONST.__objc_classlist: 0x48
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x618
+  __DATA_CONST.__objc_selrefs: 0x630
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x28
-  __AUTH_CONST.__auth_got: 0x1a0
+  __AUTH_CONST.__auth_got: 0x180
   __AUTH_CONST.__const: 0xa0
   __AUTH_CONST.__cfstring: 0x3c0
-  __AUTH_CONST.__objc_const: 0x1748
+  __AUTH_CONST.__objc_const: 0x1778
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH.__objc_data: 0xf0
-  __DATA.__objc_ivar: 0x50
+  __DATA.__objc_ivar: 0x54
   __DATA.__data: 0x360
   __DATA.__bss: 0x10
   __DATA_DIRTY.__objc_data: 0x1e0

   - /System/Library/PrivateFrameworks/AccessoryNavigation.framework/AccessoryNavigation
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 910AC06D-2C1C-3779-84E4-676615CAB4CB
-  Functions: 159
-  Symbols:   720
-  CStrings:  431
+  UUID: 5C93FD76-0152-39D6-AECE-F2FC60C92F0F
+  Functions: 166
+  Symbols:   737
+  CStrings:  436
 
Symbols:
+ -[CRAccNavInfoCache lastWindowStartIndex]
+ -[CRAccNavInfoCache setLastWindowStartIndex:]
+ -[CRAccNavInfoCache windowIndexChanged:]
+ _OBJC_IVAR_$_CRAccNavInfoCache._lastWindowStartIndex
+ _OUTLINED_FUNCTION_4
+ _OUTLINED_FUNCTION_5
+ _OUTLINED_FUNCTION_6
+ _objc_msgSend$isEqual:
+ _objc_msgSend$lastWindowStartIndex
+ _objc_msgSend$setLastWindowStartIndex:
+ _objc_msgSend$windowIndexChanged:
+ _objc_retainAutoreleasedReturnValue
+ _objc_retain_x26
+ _objc_retain_x28
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x2
- _objc_retain_x25
- _objc_retain_x3
- _objc_retain_x8
CStrings:
+ "%{public}@ sendLaneGuidances done indexChanged=%@ source.count=%lu cache=%{public}@"
+ "%{public}@ sendManeuvers done indexChanged=%@ source.count=%lu cache=%{public}@"
+ "%{public}@ sendNavInfo fromIndex=%{public}@ lastWindowStartIndex=%{public}@ sentIndexes=%lu source=%lu cache=(%p)%lu/%lu"
+ "<%@: %p countLimit=%lu count=%lu lastWindowStartIndex=%@ indexes=[%@]>"
+ "T@\"NSNumber\",&,N,V_lastWindowStartIndex"
+ "_lastWindowStartIndex"
+ "lastWindowStartIndex"
+ "setLastWindowStartIndex:"
+ "windowIndexChanged:"
- "%{public}@ sendLaneGuidances done source.count=%lu cache=%{public}@"
- "%{public}@ sendManeuvers done source.count=%lu cache=%{public}@"
- "%{public}@ sendNavInfo fromIndex=%{public}@ sentIndexes=%lu source=%lu cache=(%p)%lu/%lu"
- "<%@: %p countLimit=%lu count=%lu indexes=[%@]>"

```
