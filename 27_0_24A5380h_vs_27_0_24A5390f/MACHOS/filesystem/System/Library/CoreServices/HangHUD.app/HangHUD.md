## HangHUD

> `/System/Library/CoreServices/HangHUD.app/HangHUD`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-421.0.0.0.0
-  __TEXT.__text: 0x2f624
+424.0.0.0.0
+  __TEXT.__text: 0x2f638
   __TEXT.__auth_stubs: 0xbf0
   __TEXT.__objc_stubs: 0x5b20
   __TEXT.__objc_methlist: 0x3374
   __TEXT.__const: 0x4c0
   __TEXT.__gcc_except_tab: 0x33c
-  __TEXT.__objc_methname: 0xa78d
-  __TEXT.__cstring: 0x3891
+  __TEXT.__objc_methname: 0xa797
+  __TEXT.__cstring: 0x3895
   __TEXT.__objc_classname: 0x46d
-  __TEXT.__objc_methtype: 0x19f9
+  __TEXT.__objc_methtype: 0x19f1
   __TEXT.__oslogstring: 0x5130
   __TEXT.__unwind_info: 0xc38
-  __DATA_CONST.__const: 0x1ab0
+  __DATA_CONST.__const: 0x1ad0
   __DATA_CONST.__cfstring: 0x5300
   __DATA_CONST.__objc_classlist: 0x178
   __DATA_CONST.__objc_protolist: 0x68

   - /usr/lib/libobjc.A.dylib
   Functions: 1532
   Symbols:   294
-  CStrings:  3098
+  CStrings:  3097
 
Functions:
~ sub_100004130 : 496 -> 548
~ sub_100004320 -> sub_100004354 : 300 -> 308
~ sub_1000044cc -> sub_100004508 : 776 -> 736
CStrings:
+ "@56@0:8@16Q24Q32Q40Q48"
+ "end_matu"
+ "intervalsByClippingIntervals:toHangStart:hangEnd:sampleStart:sampleEnd:"
+ "jsonStringForIntervals:"
+ "start_matu"
- "@32@0:8@16Q24"
- "@40@0:8@16Q24Q32"
- "end_ms"
- "intervalsByClippingIntervals:toWindowStart:end:"
- "jsonStringForIntervals:hangStartMATU:"
- "start_ms"
```
