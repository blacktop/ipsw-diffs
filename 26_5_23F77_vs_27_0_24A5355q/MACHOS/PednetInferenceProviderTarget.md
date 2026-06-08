## PednetInferenceProviderTarget

> `/System/Library/ExtensionKit/Extensions/PednetInferenceProviderTarget.appex/PednetInferenceProviderTarget`

```diff

-3075.0.8.0.0
-  __TEXT.__text: 0xcd34
-  __TEXT.__auth_stubs: 0xa40
+3164.0.0.0.0
+  __TEXT.__text: 0xdfd8
+  __TEXT.__auth_stubs: 0xad0
   __TEXT.__objc_stubs: 0xa0
-  __TEXT.__objc_methlist: 0x94
-  __TEXT.__const: 0xbc8
+  __TEXT.__objc_methlist: 0xd0
+  __TEXT.__const: 0xbf8
+  __TEXT.__oslogstring: 0x1c6
   __TEXT.__objc_classname: 0x138
-  __TEXT.__objc_methname: 0x140
-  __TEXT.__constg_swiftt: 0x310
-  __TEXT.__swift5_typeref: 0x268
-  __TEXT.__swift5_reflstr: 0x173
-  __TEXT.__swift5_fieldmd: 0x210
+  __TEXT.__objc_methname: 0x19c
+  __TEXT.__constg_swiftt: 0x350
+  __TEXT.__swift5_typeref: 0x264
+  __TEXT.__swift5_reflstr: 0x18c
+  __TEXT.__swift5_fieldmd: 0x234
+  __TEXT.__cstring: 0x13b
   __TEXT.__swift5_proto: 0x78
   __TEXT.__swift5_types: 0x30
   __TEXT.__swift_as_entry: 0x50
   __TEXT.__swift_as_ret: 0x30
-  __TEXT.__oslogstring: 0x1d6
+  __TEXT.__swift_as_cont: 0x44
   __TEXT.__swift5_assocty: 0xc0
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__cstring: 0x10a
-  __TEXT.__objc_methtype: 0xad
-  __TEXT.__unwind_info: 0x528
-  __TEXT.__eh_frame: 0x830
-  __DATA_CONST.__auth_got: 0x528
-  __DATA_CONST.__got: 0x110
-  __DATA_CONST.__auth_ptr: 0x340
-  __DATA_CONST.__const: 0x3f8
+  __TEXT.__objc_methtype: 0x108
+  __TEXT.__unwind_info: 0x560
+  __TEXT.__eh_frame: 0x860
+  __DATA_CONST.__const: 0x420
   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA.__objc_const: 0x2f8
-  __DATA.__objc_selrefs: 0x70
-  __DATA.__objc_data: 0x240
-  __DATA.__data: 0x580
-  __DATA.__bss: 0xfa0
-  __DATA.__common: 0x68
+  __DATA_CONST.__auth_got: 0x570
+  __DATA_CONST.__got: 0x110
+  __DATA_CONST.__auth_ptr: 0x360
+  __DATA.__objc_const: 0x318
+  __DATA.__objc_selrefs: 0x98
+  __DATA.__objc_data: 0x288
+  __DATA.__data: 0x578
+  __DATA.__bss: 0xfc0
+  __DATA.__common: 0x70
   - /System/Library/Frameworks/CoreML.framework/CoreML
   - /System/Library/Frameworks/ExtensionFoundation.framework/ExtensionFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 30EB3290-0E58-3B9C-8072-268A812307F9
-  Functions: 399
-  Symbols:   118
-  CStrings:  63
+  UUID: 8B52752D-7289-3CD7-936A-9C47F31D0D7D
+  Functions: 421
+  Symbols:   123
+  CStrings:  76
 
Symbols:
+ _objc_release_x26
+ _objc_retain_x19
+ _swift_release_x20
+ _swift_release_x21
+ _swift_release_x22
+ _swift_release_x23
+ _swift_release_x8
+ _swift_retain_x19
+ _swift_retain_x20
- _objc_release_x23
- _objc_release_x25
- _objc_release_x27
- _swift_bridgeObjectRelease_n
CStrings:
+ "%s"
+ "Grab airpods pednet from %s"
+ "Running %ld inferences over %ld samples with stride %ld"
+ "Serializing and returning %ld values for %ld inferences"
+ "_TtC29PednetInferenceProviderTarget11PednetModel"
+ "inference_stride"
+ "isDryRun"
+ "is_indoor"
+ "outputCount"
+ "q16@0:8"
+ "setDryRun:"
+ "setInferenceStride:"
+ "setIsIndoor:"
+ "setSensorDataFlat:::::::::"
+ "v20@0:8B16"
+ "v20@0:8f16"
+ "v24@0:8q16"
+ "v88@0:8r^f16r^f24r^f32r^f40r^f48r^f56q64r^f72q80"
- "Inference run. Output: %s"
- "Received request with timestamp %llu"
- "Serializing and returning output vector: %s"
- "Tensor converted, about to run inference..."
- "_TtC29PednetInferenceProviderTarget11CMb788Model"

```
