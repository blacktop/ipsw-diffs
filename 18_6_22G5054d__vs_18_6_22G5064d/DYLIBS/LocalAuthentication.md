## LocalAuthentication

> `/System/Library/Frameworks/LocalAuthentication.framework/LocalAuthentication`

```diff

-1656.140.3.0.0
-  __TEXT.__text: 0x36474
+1656.140.4.0.0
+  __TEXT.__text: 0x35594
   __TEXT.__auth_stubs: 0xac0
-  __TEXT.__objc_methlist: 0x37b8
+  __TEXT.__objc_methlist: 0x3728
   __TEXT.__const: 0x2d4
   __TEXT.__gcc_except_tab: 0xfe8
   __TEXT.__cstring: 0x19a0
   __TEXT.__dlopen_cstrs: 0x1cd
-  __TEXT.__oslogstring: 0x2779
+  __TEXT.__oslogstring: 0x2557
   __TEXT.__swift5_typeref: 0x6e
   __TEXT.__constg_swiftt: 0x38
   __TEXT.__swift5_builtin: 0x14

   __TEXT.__swift5_assocty: 0x30
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x12d0
+  __TEXT.__unwind_info: 0x12b0
   __TEXT.__eh_frame: 0x48
   __TEXT.__objc_classname: 0xa4c
-  __TEXT.__objc_methname: 0x6ecf
-  __TEXT.__objc_methtype: 0x1d3b
-  __TEXT.__objc_stubs: 0x4960
+  __TEXT.__objc_methname: 0x6db7
+  __TEXT.__objc_methtype: 0x1cce
+  __TEXT.__objc_stubs: 0x48e0
   __DATA_CONST.__got: 0x4f0
-  __DATA_CONST.__const: 0x1c48
+  __DATA_CONST.__const: 0x1b80
   __DATA_CONST.__objc_classlist: 0x2b8
   __DATA_CONST.__objc_protolist: 0xf8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1bc0
+  __DATA_CONST.__objc_selrefs: 0x1b80
   __DATA_CONST.__objc_protorefs: 0x28
   __DATA_CONST.__objc_superrefs: 0x1f8
   __AUTH_CONST.__auth_got: 0x570
   __AUTH_CONST.__const: 0x320
   __AUTH_CONST.__cfstring: 0x1980
-  __AUTH_CONST.__objc_const: 0x8988
+  __AUTH_CONST.__objc_const: 0x8968
   __AUTH_CONST.__objc_intobj: 0x1f8
   __AUTH.__objc_data: 0x5a0
   __DATA.__objc_ivar: 0x2b8

   - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 67E76038-F122-3C92-B8FC-897156A7FA23
-  Functions: 1470
-  Symbols:   5273
-  CStrings:  2263
+  UUID: D96BAC63-8636-37F8-854F-E2C4F63C48B4
+  Functions: 1454
+  Symbols:   5232
+  CStrings:  2243
 
Symbols:
+ GCC_except_table103
+ GCC_except_table155
+ GCC_except_table59
+ GCC_except_table61
+ GCC_except_table65
+ GCC_except_table72
+ GCC_except_table82
+ GCC_except_table84
+ GCC_except_table99
- -[LAClient analyticsAction:dismissing:reply:]
- -[LAClient analyticsMechanism:result:reply:]
- -[LAClient analyticsMechanism:starting:reply:]
- -[LAClient analyticsSessionStarting:dialogID:bundleID:reply:]
- -[LAContext analyticsAction:dismissing:]
- -[LAContext analyticsMechanism:result:]
- -[LAContext analyticsMechanism:starting:]
- -[LAContext analyticsSessionStarting:dialogID:bundleID:]
- GCC_except_table111
- GCC_except_table115
- GCC_except_table163
- GCC_except_table69
- GCC_except_table73
- GCC_except_table75
- GCC_except_table80
- GCC_except_table90
- GCC_except_table92
- ___39-[LAContext analyticsMechanism:result:]_block_invoke
- ___40-[LAContext analyticsAction:dismissing:]_block_invoke
- ___41-[LAContext analyticsMechanism:starting:]_block_invoke
- ___44-[LAClient analyticsMechanism:result:reply:]_block_invoke
- ___45-[LAClient analyticsAction:dismissing:reply:]_block_invoke
- ___46-[LAClient analyticsMechanism:starting:reply:]_block_invoke
- ___56-[LAContext analyticsSessionStarting:dialogID:bundleID:]_block_invoke
- ___61-[LAClient analyticsSessionStarting:dialogID:bundleID:reply:]_block_invoke
- ___block_descriptor_53_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_descriptor_57_e8_32s40s48s_e25_v16?0?<v?B"NSError">8ls32l8s40l8s48l8
- ___block_descriptor_60_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_descriptor_61_e8_32s40s_e20_v20?0B8"NSError"12ls32l8s40l8
- ___block_descriptor_68_e8_32s40s48s_e20_v20?0B8"NSError"12ls32l8s40l8s48l8
- _objc_msgSend$analyticsAction:dismissing:reply:
- _objc_msgSend$analyticsMechanism:result:reply:
- _objc_msgSend$analyticsMechanism:starting:reply:
- _objc_msgSend$analyticsSessionStarting:dialogID:bundleID:reply:
CStrings:
- "analyticsAction:%d dismissing:%d on %{public}@ cid:%u"
- "analyticsAction:%d on %{public}@ cid:%u returned %{public}@"
- "analyticsAction:dismissing:"
- "analyticsAction:dismissing:reply:"
- "analyticsMechanism:%d result: %{public}@ on %{public}@ cid:%u returned %{public}@"
- "analyticsMechanism:%d result:%{public}@ on %{public}@ cid:%u"
- "analyticsMechanism:%d starting:%d on %{public}@ cid:%u"
- "analyticsMechanism:%d starting:%d on %{public}@ cid:%u returned %{public}@"
- "analyticsMechanism:result:"
- "analyticsMechanism:result:reply:"
- "analyticsMechanism:starting:"
- "analyticsMechanism:starting:reply:"
- "analyticsSessionStarting:%d dialogID:%{public}@ bundleID:%{private}@ on %{public}@ cid:%u"
- "analyticsSessionStarting:%d on %{public}@ cid:%u returned %{public}@"
- "analyticsSessionStarting:dialogID:bundleID:"
- "analyticsSessionStarting:dialogID:bundleID:reply:"
- "v28@0:8q16B24"
- "v36@0:8B16@20@28"
- "v44@0:8B16@\"NSString\"20@\"NSString\"28@?<v@?B@\"NSError\">36"
- "v44@0:8B16@20@28@?36"

```
