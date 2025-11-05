## com.apple.driver.IODARTFamily

> `com.apple.driver.IODARTFamily`

```diff

-350.60.3.0.0
-  __TEXT.__cstring: 0x2197
-  __TEXT.__const: 0x14
-  __TEXT_EXEC.__text: 0x13b04
+354.100.4.0.0
+  __TEXT.__cstring: 0x22bb
+  __TEXT.__const: 0x20
+  __TEXT_EXEC.__text: 0x14280
   __TEXT_EXEC.__auth_stubs: 0x0
   __DATA.__data: 0xc8
   __DATA.__common: 0x178

   __DATA_CONST.__got: 0xb8
   __DATA_CONST.__mod_init_func: 0x38
   __DATA_CONST.__mod_term_func: 0x38
-  __DATA_CONST.__const: 0x3fc8
+  __DATA_CONST.__const: 0x3fe0
   __DATA_CONST.__kalloc_type: 0x400
   __DATA_CONST.__kalloc_var: 0x410
-  UUID: 191DEF9C-CC61-3285-B56B-5DF364C43FD6
-  Functions: 374
-  Symbols:   883
-  CStrings:  222
+  UUID: 5331ACD5-643A-374D-B33C-7AB81325DBF3
+  Functions: 375
+  Symbols:   888
+  CStrings:  227
 
Symbols:
+ _ZN12IODARTMapper9_iovmFreeEP13IODARTVMSpaceb.cold.1
+ __ZN12IODARTMapper20_findVMSpaceReservedEjj
+ __ZN17IODARTVMAllocator15vmAllocReservedEjjjjjb
+ __ZN24IODARTVMAllocatorGeneric15vmAllocReservedEjjjjjb
+ __ZZN12IODARTMapper16_addBatchSegmentEmymjjE21kalloc_type_view_3941
+ __ZZN12IODARTMapper16_addBatchSegmentEmymjjE21kalloc_type_view_3948
- __ZZN12IODARTMapper16_addBatchSegmentEmymjjE21kalloc_type_view_3878
- __ZZN12IODARTMapper16_addBatchSegmentEmymjjE21kalloc_type_view_3885
CStrings:
+ "(%s) %s::%s: Allocated %d pages from page 0x%x in reserved DVA range [0x%016llx..0x%016llx)\n"
+ "(%s) %s::%s: Failed to allocate %d pages from page 0x%x in reserved DVA range [0x%016llx..0x%016llx)\n"
+ "(%s) %s::%s: failed to get VM space for allocation at 0x%x\n"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IODARTFamily/AllocGeneric.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IODARTFamily/IODART.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IODARTFamily/IODARTClient.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IODARTFamily/IODARTMapper.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IODARTFamily/IODARTMapperClient.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IODARTFamily/IODARTPrivate.h"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IODARTFamily/IODARTVMAllocator.cpp"
+ "/AppleInternal/Library/BuildRoots/17229e79-0523-11f0-a80c-fe9e33ca05fa/Library/Caches/com.apple.xbs/Sources/IODARTFamily/IODARTVMSpace.cpp"
+ "_findVMSpaceReserved"
+ "vmAllocReserved"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IODARTFamily/AllocGeneric.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IODARTFamily/IODART.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IODARTFamily/IODARTClient.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IODARTFamily/IODARTMapper.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IODARTFamily/IODARTMapperClient.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IODARTFamily/IODARTPrivate.h"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IODARTFamily/IODARTVMAllocator.cpp"
- "/AppleInternal/Library/BuildRoots/1a84d2b1-c913-11ef-bd9f-d285688f7a47/Library/Caches/com.apple.xbs/Sources/IODARTFamily/IODARTVMSpace.cpp"

```
