## handwritingd

> `/usr/libexec/handwritingd`

```diff

-490.0.0.0.0
-  __TEXT.__text: 0x127f4
-  __TEXT.__auth_stubs: 0x750
-  __TEXT.__objc_stubs: 0x2d00
+492.2.0.0.0
+  __TEXT.__text: 0x12db8
+  __TEXT.__auth_stubs: 0x760
+  __TEXT.__objc_stubs: 0x2d80
   __TEXT.__objc_methlist: 0x8a0
   __TEXT.__const: 0x80
-  __TEXT.__gcc_except_tab: 0x1964
-  __TEXT.__cstring: 0x1271
-  __TEXT.__objc_methname: 0x33d4
+  __TEXT.__gcc_except_tab: 0x1a04
+  __TEXT.__cstring: 0x12a5
+  __TEXT.__objc_methname: 0x3471
   __TEXT.__objc_classname: 0x22c
-  __TEXT.__objc_methtype: 0x896
+  __TEXT.__objc_methtype: 0x897
   __TEXT.__dlopen_cstrs: 0x4f
-  __TEXT.__oslogstring: 0x1670
-  __TEXT.__unwind_info: 0x680
-  __DATA_CONST.__auth_got: 0x3c0
+  __TEXT.__oslogstring: 0x16f4
+  __TEXT.__unwind_info: 0x698
+  __DATA_CONST.__auth_got: 0x3c8
   __DATA_CONST.__got: 0x310
-  __DATA_CONST.__const: 0x5d8
-  __DATA_CONST.__cfstring: 0xe80
+  __DATA_CONST.__const: 0x640
+  __DATA_CONST.__cfstring: 0xec0
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_protolist: 0x48
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x118
   __DATA_CONST.__objc_arrayobj: 0x48
   __DATA.__objc_const: 0x1868
-  __DATA.__objc_selrefs: 0xc60
+  __DATA.__objc_selrefs: 0xc80
   __DATA.__objc_ivar: 0xdc
   __DATA.__objc_data: 0x3c0
   __DATA.__data: 0x360

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 243
-  Symbols:   230
-  CStrings:  863
+  Functions: 245
+  Symbols:   231
+  CStrings:  873
 
Symbols:
+ _dispatch_get_global_queue
CStrings:
+ "0"
+ "@\"CHSynthesisResult\"48@?0@\"NSString\"8Q16Q24@?<v@?@\"CHSynthesisResult\"@\"NSError\">32@?<@\"NSArray\"@?@\"NSArray\">40"
+ "@32@0:8@16^B24"
+ "B24@?0@\"NSString\"8@\"NSString\"16"
+ "Only fast path queries should end up on non-synchronized synthesis queues"
+ "Remote request handled on synchronized synthesis queue=%!@(MISSING)"
+ "_queueForRequest:outIsSynchronizedSynthesisQueue:"
+ "checkSegmentsAndDrawingConsistencyForSynthesisResult:bundleIdentifier:withReply:"
+ "com.apple.handwritingd.ongoingSynthesisCheck"
+ "initWithLocationRange:comment:kind:"
+ "isFastPath"
+ "o"
+ "setLocales:"
+ "styleSamplesForInputSample:prompt:samplingAlgorithm:maxNumOfSamples:"
- "@\"CHSynthesisResult\"40@?0@\"NSString\"8Q16@?<v@?@\"CHSynthesisResult\"@\"NSError\">24@?<@\"CHRemoteSynthesisRequest\"@?@\"CHSynthesisStyleSample\">32"
- "checkSegmentsAndDrawingConsistencyForSynthesisResult:bundleIdentifier:"
- "initWithLocation:comment:kind:"
- "v32@0:8@16@24"

```
