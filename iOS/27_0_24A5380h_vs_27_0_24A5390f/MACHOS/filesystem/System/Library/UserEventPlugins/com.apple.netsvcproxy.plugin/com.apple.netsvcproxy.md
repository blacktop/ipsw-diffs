## com.apple.netsvcproxy

> `/System/Library/UserEventPlugins/com.apple.netsvcproxy.plugin/com.apple.netsvcproxy`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA.__cfstring`
- `__DATA.__objc_classlist`
- `__DATA.__objc_protolist`
- `__DATA.__objc_superrefs`
- `__DATA.__objc_data`
- `__DATA.__data`
- `__DATA.__objc_arraydata`
- `__DATA.__objc_arrayobj`
- `__DATA.__got`

```diff

-976.0.0.0.0
-  __TEXT.__text: 0x9ff4
+980.0.0.0.0
+  __TEXT.__text: 0xa30c
   __TEXT.__auth_stubs: 0x820
-  __TEXT.__objc_stubs: 0x1c20
-  __TEXT.__objc_methlist: 0xac0
-  __TEXT.__objc_methname: 0x2944
-  __TEXT.__cstring: 0xf92
+  __TEXT.__objc_stubs: 0x1cc0
+  __TEXT.__objc_methlist: 0xb00
+  __TEXT.__objc_methname: 0x2a36
+  __TEXT.__cstring: 0xfa7
   __TEXT.__objc_classname: 0x6d
   __TEXT.__objc_methtype: 0x300
   __TEXT.__const: 0x2a0
   __TEXT.__gcc_except_tab: 0x268
-  __TEXT.__oslogstring: 0xb2b
-  __TEXT.__unwind_info: 0x2b0
-  __DATA.__const: 0x670
+  __TEXT.__oslogstring: 0xb72
+  __TEXT.__unwind_info: 0x2b8
+  __DATA.__const: 0x690
   __DATA.__cfstring: 0x14e0
   __DATA.__objc_classlist: 0x20
   __DATA.__objc_protolist: 0x10
   __DATA.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0xfa8
-  __DATA.__objc_selrefs: 0x970
+  __DATA.__objc_const: 0x1008
+  __DATA.__objc_selrefs: 0x998
   __DATA.__objc_superrefs: 0x10
-  __DATA.__objc_ivar: 0x110
+  __DATA.__objc_ivar: 0x118
   __DATA.__objc_data: 0x140
   __DATA.__data: 0xd4
   __DATA.__objc_arraydata: 0x18

   - /System/Library/PrivateFrameworks/MobileKeyBag.framework/MobileKeyBag
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 308
+  Functions: 315
   Symbols:   217
-  CStrings:  757
+  CStrings:  769
 
CStrings:
+ "Failed to create token aggregation timer"
+ "T@\"NSDate\",&,V_tokenAggregationDate"
+ "T@\"NSTimer\",&,V_tokenAggregationTimer"
+ "TokenAggregationDate"
+ "_tokenAggregationDate"
+ "_tokenAggregationTimer"
+ "setTokenAggregationDate:"
+ "setTokenAggregationInterval:"
+ "setTokenAggregationTimer:"
+ "token aggregation timer fired"
+ "tokenAggregationDate"
+ "tokenAggregationTimer"
```
