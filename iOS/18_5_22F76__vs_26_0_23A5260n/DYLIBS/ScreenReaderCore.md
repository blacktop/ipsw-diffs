## ScreenReaderCore

> `/System/Library/PrivateFrameworks/ScreenReaderCore.framework/ScreenReaderCore`

```diff

-247.4.0.0.0
-  __TEXT.__text: 0x24738
+262.0.0.0.0
+  __TEXT.__text: 0x249f4
   __TEXT.__auth_stubs: 0xcf0
-  __TEXT.__objc_methlist: 0x2aac
+  __TEXT.__objc_methlist: 0x2abc
   __TEXT.__cstring: 0x284c
   __TEXT.__const: 0x7a0
   __TEXT.__ustring: 0x2a

   __TEXT.__dlopen_cstrs: 0x4f
   __TEXT.__unwind_info: 0xa28
   __TEXT.__objc_classname: 0x6df
-  __TEXT.__objc_methname: 0x5acb
+  __TEXT.__objc_methname: 0x5b1d
   __TEXT.__objc_methtype: 0x1106
-  __TEXT.__objc_stubs: 0x4aa0
+  __TEXT.__objc_stubs: 0x4ac0
   __DATA_CONST.__got: 0x2d0
-  __DATA_CONST.__const: 0x3b0
+  __DATA_CONST.__const: 0x3d8
   __DATA_CONST.__objc_classlist: 0x1b8
   __DATA_CONST.__objc_catlist: 0x90
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x19e8
+  __DATA_CONST.__objc_selrefs: 0x19f8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x150
   __DATA_CONST.__objc_arraydata: 0x238
   __AUTH_CONST.__auth_got: 0x688
   __AUTH_CONST.__const: 0x200
   __AUTH_CONST.__cfstring: 0x4b00
-  __AUTH_CONST.__objc_const: 0x42c0
+  __AUTH_CONST.__objc_const: 0x42e0
   __AUTH_CONST.__objc_arrayobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x50
   __AUTH_CONST.__objc_intobj: 0x78
-  __DATA.__objc_ivar: 0x2c4
+  __DATA.__objc_ivar: 0x2c8
   __DATA.__data: 0x2e0
-  __DATA.__crash_info: 0x40
+  __DATA.__crash_info: 0x148
   __DATA.__bss: 0x1f0
   __DATA.__common: 0x38
   __DATA_DIRTY.__objc_data: 0x1130

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 82E422CC-50F9-34DF-8DF5-163F4EA3E5D8
-  Functions: 931
-  Symbols:   3549
-  CStrings:  2535
+  UUID: 4E18B046-D4C2-3194-B2D9-08B668B7E8F4
+  Functions: 934
+  Symbols:   3558
+  CStrings:  2538
 
Symbols:
+ -[NSString(SCRCStringExtras) scrStringByReplacingCharactersInSet:withString:]
+ -[NSString(SCRCStringExtras) scrStringByTrimmingLeadingCharactersInSet:]
+ -[NSString(SCRCStringExtras) scrStringByTrimmingTrailingCharactersInSet:]
+ -[SCRCGestureFactory tapTotalFingerCount]
+ -[SCRCIndexMap _ensureCodableAttributedString:]
+ GCC_except_table22
+ _OBJC_IVAR_$_SCRCGestureFactory._tapTotalFingerCount
+ ___47-[SCRCIndexMap _ensureCodableAttributedString:]_block_invoke
+ ___block_descriptor_40_e8_32s_e41_v40?0"NSDictionary"8{_NSRange=QQ}16^B32ls32l8
+ _objc_msgSend$_ensureCodableAttributedString:
- -[NSString(SCRCStringExtras) stringByReplacingCharactersInSet:withString:]
- -[NSString(SCRCStringExtras) stringByTrimmingLeadingCharactersInSet:]
- -[NSString(SCRCStringExtras) stringByTrimmingTrailingCharactersInSet:]
- GCC_except_table20
CStrings:
+ "_ensureCodableAttributedString:"
+ "_tapTotalFingerCount"
+ "scrStringByReplacingCharactersInSet:withString:"
+ "scrStringByTrimmingLeadingCharactersInSet:"
+ "scrStringByTrimmingTrailingCharactersInSet:"
+ "tapTotalFingerCount"
- "stringByReplacingCharactersInSet:withString:"
- "stringByTrimmingLeadingCharactersInSet:"
- "stringByTrimmingTrailingCharactersInSet:"

```
