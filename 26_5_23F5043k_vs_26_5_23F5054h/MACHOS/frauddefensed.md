## frauddefensed

> `filesystem/usr/libexec/frauddefensed`

```diff

-69.5.0.0.0
-  __TEXT.__text: 0x9d2c0
-  __TEXT.__auth_stubs: 0x2100
-  __TEXT.__objc_stubs: 0x1140
-  __TEXT.__objc_methlist: 0x400
-  __TEXT.__const: 0x5f9c
-  __TEXT.__swift5_typeref: 0x1770
-  __TEXT.__swift5_capture: 0x6c4
-  __TEXT.__cstring: 0x7dfb
-  __TEXT.__objc_methtype: 0x717
+70.5.2.0.0
+  __TEXT.__text: 0x9f664
+  __TEXT.__auth_stubs: 0x2120
+  __TEXT.__objc_stubs: 0x11c0
+  __TEXT.__objc_methlist: 0x450
+  __TEXT.__const: 0x5fdc
+  __TEXT.__swift5_typeref: 0x1758
+  __TEXT.__swift5_capture: 0x6bc
+  __TEXT.__cstring: 0x807b
+  __TEXT.__objc_methtype: 0x6e7
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__constg_swiftt: 0x1b70
+  __TEXT.__constg_swiftt: 0x1bbc
   __TEXT.__swift5_builtin: 0x78
-  __TEXT.__swift5_reflstr: 0x1af3
-  __TEXT.__swift5_fieldmd: 0x1f74
+  __TEXT.__swift5_reflstr: 0x1b43
+  __TEXT.__swift5_fieldmd: 0x1ffc
   __TEXT.__swift5_assocty: 0x298
   __TEXT.__swift5_proto: 0x318
-  __TEXT.__swift5_types: 0x1e0
-  __TEXT.__objc_classname: 0x6e2
+  __TEXT.__swift5_types: 0x1e4
+  __TEXT.__objc_classname: 0x6f2
   __TEXT.__swift_as_entry: 0x1e4
   __TEXT.__swift_as_ret: 0x2d0
-  __TEXT.__objc_methname: 0x14c2
+  __TEXT.__objc_methname: 0x1542
   __TEXT.__swift5_protos: 0x50
   __TEXT.__swift5_mpenum: 0x10
   __TEXT.__oslogstring: 0xbf
-  __TEXT.__unwind_info: 0x24a0
-  __TEXT.__eh_frame: 0x6900
-  __DATA_CONST.__auth_got: 0x1088
-  __DATA_CONST.__got: 0x5e0
-  __DATA_CONST.__auth_ptr: 0x610
-  __DATA_CONST.__const: 0x4490
-  __DATA_CONST.__objc_classlist: 0xf8
+  __TEXT.__unwind_info: 0x24d0
+  __TEXT.__eh_frame: 0x68d0
+  __DATA_CONST.__auth_got: 0x1098
+  __DATA_CONST.__got: 0x5e8
+  __DATA_CONST.__auth_ptr: 0x618
+  __DATA_CONST.__const: 0x44a0
+  __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x48
-  __DATA.__objc_const: 0x1d00
-  __DATA.__objc_selrefs: 0x560
-  __DATA.__objc_data: 0xb90
-  __DATA.__data: 0x3550
-  __DATA.__common: 0x1b8
+  __DATA.__objc_const: 0x1e48
+  __DATA.__objc_selrefs: 0x580
+  __DATA.__objc_data: 0xc80
+  __DATA.__data: 0x35c8
+  __DATA.__common: 0x1e0
   __DATA.__bss: 0x57a0
   - /System/Library/Frameworks/CloudKit.framework/CloudKit
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 49D8D16D-7B5D-3770-96F2-4DA55DF9DE72
-  Functions: 2439
-  Symbols:   848
-  CStrings:  909
+  UUID: E28DA4E5-8873-3383-B7A7-71EBC626DD81
+  Functions: 2455
+  Symbols:   851
+  CStrings:  927
 
Symbols:
+ _$sSo17NSKeyedUnarchiverC10FoundationE31unarchiveTopLevelObjectWithDatayypSgAC0I0VKFZ
+ _$ss27_bridgeAnythingToObjectiveCyyXlxlF
+ _OBJC_CLASS_$_NSKeyedUnarchiver
CStrings:
+ "/Library/Caches/com.apple.xbs/<UUID>/TemporaryDirectory.<TMP>/Sources/TrustKit/frauddefensed/ServerProtocol.swift"
+ "Decision info contains non-archivable types."
+ "Decision info contains non-archivable types. { failures="
+ "Failed to decode decision info for XPC transport."
+ "Failed to decode decision info for XPC transport. { error="
+ "Failed to decode previous decision info for XPC transport. { error="
+ "Failed to encode decision info. { error="
+ "Failed to encode previous decision info for XPC transport. { error="
+ "TKFDInference"
+ "archivedDataWithRootObject:requiringSecureCoding:error:"
+ "containsValueForKey:"
+ "decision"
+ "decisionInfo"
+ "decodeBoolForKey:"
+ "encodeBool:forKey:"
+ "frauddefensed.Inference"
+ "isChatBot"
+ "spamDecisionManagerImageInference:completionHandler:"
+ "spamDecisionManagerInference:completionHandler:"
+ "v32@0:8@\"TKFDImageSpamDecisioningInput\"16@?<v@?@\"TKFDInference\"@\"NSError\">24"
+ "v32@0:8@\"TKFDTextSpamDecisioningInput\"16@?<v@?@\"TKFDInference\"@\"NSError\">24"
+ "v32@0:8@16@?24"
- "spamDecisionManagerImageInference:decisionInfo:completionHandler:"
- "spamDecisionManagerInference:decisionInfo:completionHandler:"
- "v40@0:8@\"TKFDImageSpamDecisioningInput\"16@\"NSDictionary\"24@?<v@?@\"NSString\"@\"NSDictionary\"@\"NSError\">32"
- "v40@0:8@\"TKFDTextSpamDecisioningInput\"16@\"NSDictionary\"24@?<v@?@\"NSString\"@\"NSDictionary\"@\"NSError\">32"

```
