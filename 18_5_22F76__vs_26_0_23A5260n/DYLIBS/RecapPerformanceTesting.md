## RecapPerformanceTesting

> `/System/Library/PrivateFrameworks/RecapPerformanceTesting.framework/RecapPerformanceTesting`

```diff

-50.0.0.0.0
-  __TEXT.__text: 0xe03c
-  __TEXT.__auth_stubs: 0x5d0
+51.0.0.0.0
+  __TEXT.__text: 0xe154
+  __TEXT.__auth_stubs: 0x5e0
   __TEXT.__objc_methlist: 0x1f88
   __TEXT.__const: 0x298
-  __TEXT.__gcc_except_tab: 0x294
-  __TEXT.__cstring: 0x75b
+  __TEXT.__gcc_except_tab: 0x2a4
+  __TEXT.__cstring: 0x79b
   __TEXT.__oslogstring: 0x11a5
-  __TEXT.__unwind_info: 0x588
+  __TEXT.__unwind_info: 0x580
   __TEXT.__objc_classname: 0x529
-  __TEXT.__objc_methname: 0x4442
+  __TEXT.__objc_methname: 0x4449
   __TEXT.__objc_methtype: 0x1284
-  __TEXT.__objc_stubs: 0x22c0
+  __TEXT.__objc_stubs: 0x22e0
   __DATA_CONST.__got: 0x138
   __DATA_CONST.__const: 0x328
   __DATA_CONST.__objc_classlist: 0xe8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xec0
+  __DATA_CONST.__objc_selrefs: 0xec8
   __DATA_CONST.__objc_superrefs: 0xc0
-  __AUTH_CONST.__auth_got: 0x300
+  __AUTH_CONST.__auth_got: 0x308
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x4e0
+  __AUTH_CONST.__cfstring: 0x480
   __AUTH_CONST.__objc_const: 0x7480
   __AUTH_CONST.__objc_doubleobj: 0x10
   __DATA.__objc_ivar: 0x204

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 44F68DD4-7F3E-31D4-919C-3222CE0945E7
-  Functions: 540
-  Symbols:   2134
-  CStrings:  1023
+  UUID: EA02281A-BF49-3DFC-BF26-EDB1DC1A94EF
+  Functions: 544
+  Symbols:   2146
+  CStrings:  1018
 
Symbols:
+ __ZNSt3__119__allocate_at_leastB8nn200100INS_9allocatorIdEEEENS_19__allocation_resultINS_16allocator_traitsIT_E7pointerEEERS5_m
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE11__vallocateB8nn200100Em
+ __ZNSt3__16vectorIdNS_9allocatorIdEEE20__throw_length_errorB8nn200100Ev
+ __ZNSt3__16vectorIdNS_9allocatorIdEEEC2B8nn200100ESt16initializer_listIdE
+ __ZSt28__throw_bad_array_new_lengthB8nn200100v
+ __ZnwmSt19__type_descriptor_t
+ ___62-[RPTScrollViewTestParameters completeAfterScrollEndSignpost:]_block_invoke.17
+ _abort
+ _objc_msgSend$length
- __Znwm
- ___62-[RPTScrollViewTestParameters completeAfterScrollEndSignpost:]_block_invoke.26
CStrings:
+ "category=='ScrollView' AND ((subsystem=='com.apple.UIKit' AND signpostName=='Scroll_Deceleration') OR (subsystem=='com.apple.AppKit' AND signpostName=='ScrollGesture')) AND message CONTAINS 'id=%@'"
+ "length"
- "ScrollView"
- "Scroll_Deceleration"
- "com.apple.UIKit"
- "subsystem=='%@' AND category=='%@' AND signpostName=='%@' AND message CONTAINS 'id=%@'"

```
