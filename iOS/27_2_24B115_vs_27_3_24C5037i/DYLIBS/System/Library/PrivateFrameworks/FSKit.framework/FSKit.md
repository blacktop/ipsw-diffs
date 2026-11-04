## FSKit

> `/System/Library/PrivateFrameworks/FSKit.framework/FSKit`

```diff

-974.40.12.0.0
-  __TEXT.__text: 0x525a4
-  __TEXT.__objc_methlist: 0x6378
+974.60.5.0.0
+  __TEXT.__text: 0x52708
+  __TEXT.__objc_methlist: 0x6390
   __TEXT.__const: 0x498
   __TEXT.__gcc_except_tab: 0xe64
-  __TEXT.__oslogstring: 0x3fb6
-  __TEXT.__cstring: 0x67df
+  __TEXT.__oslogstring: 0x40d6
+  __TEXT.__cstring: 0x682f
   __TEXT.__swift5_typeref: 0x264
   __TEXT.__swift5_capture: 0xec
   __TEXT.__swift_as_entry: 0x1c

   __TEXT.__constg_swiftt: 0x210
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x2230
+  __TEXT.__unwind_info: 0x2240
   __TEXT.__eh_frame: 0x478
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2c30
+  __DATA_CONST.__objc_selrefs: 0x2c40
   __DATA_CONST.__objc_protorefs: 0x150
   __DATA_CONST.__objc_superrefs: 0x2e8
   __DATA_CONST.__objc_arraydata: 0x488
   __DATA_CONST.__got: 0x488
   __AUTH_CONST.__const: 0x6f0
-  __AUTH_CONST.__cfstring: 0x2b00
-  __AUTH_CONST.__objc_const: 0xb2e8
+  __AUTH_CONST.__cfstring: 0x2b20
+  __AUTH_CONST.__objc_const: 0xb308
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_dictobj: 0x2a8
   __AUTH_CONST.__objc_arrayobj: 0x288
   __AUTH_CONST.__auth_got: 0x930
   __AUTH.__objc_data: 0x1bd8
   __AUTH.__data: 0x58
-  __DATA.__objc_ivar: 0x640
+  __DATA.__objc_ivar: 0x644
   __DATA.__data: 0x1598
   __DATA_DIRTY.__objc_data: 0x958
   __DATA_DIRTY.__data: 0x80

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 2711
-  Symbols:   4263
-  CStrings:  1104
+  Functions: 2714
+  Symbols:   4267
+  CStrings:  1108
 
Symbols:
+ -[FSItemAttributes validMask]
+ -[FSItemSetAttributesRequest reportedConsumedAttributes]
+ _OBJC_IVAR_$_FSItemSetAttributesRequest._consumedAttributesReported
+ _gWarnedUnreportedConsumedAttributes
CStrings:
+ "%s: module completed setAttributes without setting FSItemSetAttributesRequest.consumedAttributes. FSKit has to assume every requested attribute was applied. Explicitly set consumedAttributes to 0 if nothing was applied."
+ "%s: module did not consume attributes 0x%llx of requested 0x%llx"
+ "-[FSItemSetAttributesRequest reportedConsumedAttributes]"
+ "FSItemAttrConsumedSet"
```
