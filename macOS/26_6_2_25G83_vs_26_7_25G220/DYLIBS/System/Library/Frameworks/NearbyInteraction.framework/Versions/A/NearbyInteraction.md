## NearbyInteraction

> `/System/Library/Frameworks/NearbyInteraction.framework/Versions/A/NearbyInteraction`

```diff

 524.0.7.0.0
-  __TEXT.__text: 0x3493c
+  __TEXT.__text: 0x34f00
   __TEXT.__auth_stubs: 0x740
-  __TEXT.__objc_methlist: 0x3c80
-  __TEXT.__gcc_except_tab: 0x548c
-  __TEXT.__cstring: 0x4e8e
+  __TEXT.__objc_methlist: 0x3cd0
+  __TEXT.__gcc_except_tab: 0x5548
+  __TEXT.__cstring: 0x4e99
   __TEXT.__const: 0x4d0
-  __TEXT.__oslogstring: 0xe6b
+  __TEXT.__oslogstring: 0xf03
   __TEXT.__swift5_typeref: 0x83
   __TEXT.__swift5_reflstr: 0x4b
   __TEXT.__swift5_assocty: 0x48

   __TEXT.__swift5_builtin: 0x28
   __TEXT.__swift5_proto: 0x28
   __TEXT.__swift5_types: 0x10
-  __TEXT.__unwind_info: 0x1e90
+  __TEXT.__unwind_info: 0x1ee0
   __TEXT.__eh_frame: 0x130
   __TEXT.__objc_classname: 0x5a4
-  __TEXT.__objc_methname: 0x87ec
-  __TEXT.__objc_methtype: 0x13ee
-  __TEXT.__objc_stubs: 0x4a80
+  __TEXT.__objc_methname: 0x88ed
+  __TEXT.__objc_methtype: 0x141a
+  __TEXT.__objc_stubs: 0x4ae0
   __DATA_CONST.__got: 0x280
   __DATA_CONST.__const: 0x570
   __DATA_CONST.__objc_classlist: 0x190
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bf8
+  __DATA_CONST.__objc_selrefs: 0x1c30
   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x178
   __DATA_CONST.__objc_arraydata: 0x40
   __AUTH_CONST.__auth_got: 0x3b0
   __AUTH_CONST.__const: 0xb38
-  __AUTH_CONST.__cfstring: 0x5520
-  __AUTH_CONST.__objc_const: 0x6f38
+  __AUTH_CONST.__cfstring: 0x5540
+  __AUTH_CONST.__objc_const: 0x6fb0
   __AUTH_CONST.__objc_intobj: 0x2b8
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH.__objc_data: 0x370

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1446
-  Symbols:   3264
-  CStrings:  2381
+  Functions: 1451
+  Symbols:   3280
+  CStrings:  2393
 
Symbols:
+ +[NIPlatformInfo supportsDeviceCVPerception]
+ -[NISession didUpdateDeviceAssociationStatus:]
+ -[NISession object:didUpdateCVDistance:]
+ -[NISession object:didUpdateCVRegion:previousRegion:]
+ GCC_except_table100
+ GCC_except_table101
+ GCC_except_table113
+ GCC_except_table143
+ GCC_except_table148
+ GCC_except_table157
+ GCC_except_table170
+ GCC_except_table171
+ GCC_except_table172
+ GCC_except_table173
+ GCC_except_table174
+ GCC_except_table190
+ GCC_except_table191
+ GCC_except_table192
+ GCC_except_table193
+ GCC_except_table194
+ GCC_except_table206
+ GCC_except_table207
+ GCC_except_table210
+ GCC_except_table220
+ GCC_except_table223
+ GCC_except_table236
+ GCC_except_table239
+ GCC_except_table243
+ GCC_except_table244
+ GCC_except_table246
+ GCC_except_table254
+ GCC_except_table268
+ GCC_except_table275
+ GCC_except_table277
+ GCC_except_table282
+ GCC_except_table287
+ GCC_except_table296
+ GCC_except_table306
+ GCC_except_table309
+ GCC_except_table310
+ GCC_except_table320
+ GCC_except_table321
+ GCC_except_table322
+ GCC_except_table324
+ GCC_except_table325
+ GCC_except_table329
+ GCC_except_table334
+ GCC_except_table76
+ ___40-[NISession object:didUpdateCVDistance:]_block_invoke
+ ___46-[NISession didUpdateDeviceAssociationStatus:]_block_invoke
+ ___53-[NISession object:didUpdateCVRegion:previousRegion:]_block_invoke
+ _objc_msgSend$session:didUpdateDeviceAssociationStatus:
+ _objc_msgSend$session:object:didUpdateCVDistance:
+ _objc_msgSend$session:object:didUpdateCVRegion:previousRegion:
- GCC_except_table118
- GCC_except_table119
- GCC_except_table149
- GCC_except_table154
- GCC_except_table182
- GCC_except_table184
- GCC_except_table185
- GCC_except_table186
- GCC_except_table187
- GCC_except_table195
- GCC_except_table196
- GCC_except_table197
- GCC_except_table198
- GCC_except_table199
- GCC_except_table200
- GCC_except_table212
- GCC_except_table216
- GCC_except_table219
- GCC_except_table238
- GCC_except_table248
- GCC_except_table252
- GCC_except_table253
- GCC_except_table262
- GCC_except_table266
- GCC_except_table269
- GCC_except_table274
- GCC_except_table281
- GCC_except_table283
- GCC_except_table285
- GCC_except_table294
- GCC_except_table308
- GCC_except_table315
- GCC_except_table316
- GCC_except_table318
- GCC_except_table323
- GCC_except_table328
- GCC_except_table71
- GCC_except_table98
CStrings:
+ "DelegateProxy: updated cv distance: %.3f. Object: %{private}@"
+ "DelegateProxy: updated cv region %{private}@ (previous: %{private}@). Object: %{private}@"
+ "Perception"
+ "didUpdateDeviceAssociationStatus:"
+ "object:didUpdateCVDistance:"
+ "object:didUpdateCVRegion:previousRegion:"
+ "session:didUpdateDeviceAssociationStatus:"
+ "session:object:didUpdateCVDistance:"
+ "session:object:didUpdateCVRegion:previousRegion:"
+ "supportsDeviceCVPerception"
+ "v32@0:8@\"NINearbyObject\"16d24"
+ "v32@0:8@16d24"
```
