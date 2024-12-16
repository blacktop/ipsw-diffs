## Anvil

> `/System/Library/PrivateFrameworks/Anvil.framework/Anvil`

```diff

-43.121.0.0.0
-  __TEXT.__text: 0x100040
-  __TEXT.__auth_stubs: 0x2890
+43.650.0.0.0
+  __TEXT.__text: 0x100354
+  __TEXT.__auth_stubs: 0x28b0
   __TEXT.__objc_methlist: 0x100
-  __TEXT.__const: 0xa300
-  __TEXT.__cstring: 0x3113
+  __TEXT.__const: 0xa308
+  __TEXT.__cstring: 0x317d
   __TEXT.__constg_swiftt: 0x1df0
-  __TEXT.__swift5_typeref: 0x24fc
+  __TEXT.__swift5_typeref: 0x252a
   __TEXT.__swift5_builtin: 0x64
-  __TEXT.__swift5_reflstr: 0x16ab
+  __TEXT.__swift5_reflstr: 0x16c3
   __TEXT.__swift5_assocty: 0x480
+  __TEXT.__swift5_fieldmd: 0x2be8
   __TEXT.__swift5_proto: 0xb48
   __TEXT.__swift5_types: 0x320
-  __TEXT.__swift5_fieldmd: 0x2be8
-  __TEXT.__oslogstring: 0x3055
   __TEXT.__swift5_capture: 0x84c
-  __TEXT.__swift5_protos: 0xc
+  __TEXT.__oslogstring: 0x3089
   __TEXT.__swift5_mpenum: 0x20
-  __TEXT.__unwind_info: 0x3da0
-  __TEXT.__eh_frame: 0x83a8
+  __TEXT.__swift5_protos: 0xc
+  __TEXT.__unwind_info: 0x3da8
+  __TEXT.__eh_frame: 0x839c
   __TEXT.__objc_classname: 0x61
   __TEXT.__objc_methname: 0xa58
   __TEXT.__objc_methtype: 0x67a
-  __DATA_CONST.__got: 0x728
+  __DATA_CONST.__got: 0x730
   __DATA_CONST.__const: 0x140
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x210
   __DATA_CONST.__objc_protorefs: 0x28
-  __AUTH_CONST.__auth_got: 0x1448
-  __AUTH_CONST.__auth_ptr: 0x630
+  __AUTH_CONST.__auth_got: 0x1458
+  __AUTH_CONST.__auth_ptr: 0x650
   __AUTH_CONST.__const: 0x77c0
   __AUTH_CONST.__objc_const: 0x1468
   __AUTH.__objc_data: 0x350
-  __AUTH.__data: 0x19c0
-  __DATA.__data: 0x2a48
+  __AUTH.__data: 0x19c8
+  __DATA.__data: 0x2a68
   __DATA.__bss: 0x166f0
   __DATA.__common: 0x130
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Security.framework/Security
   - /System/Library/Frameworks/SwiftData.framework/SwiftData
+  - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/GenerativeFunctionsFoundation.framework/GenerativeFunctionsFoundation
   - /System/Library/PrivateFrameworks/GenerativeFunctionsInstrumentation.framework/GenerativeFunctionsInstrumentation
   - /System/Library/PrivateFrameworks/GenerativeModelsFoundation.framework/GenerativeModelsFoundation

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 4651
-  Symbols:   268
-  CStrings:  801
+  Functions: 4655
+  Symbols:   271
+  CStrings:  804
 
Symbols:
+ _AnalyticsSendEvent
CStrings:
+ " does not support random seeds!"
+ "%s does not support random seeds!"
+ "Preparing request:\n  previousChoiceID: %s\n  configuration: %s\n  model: nil\n  input: <private>\n  inputHint: %s\n  tools: %s\n  toolChoice: %s\n  toolCallOutputs: <count=%ld>\n  temperature: %s\n  responseFormat: %s"
+ "com.apple.PartnerCloudAuth"
- "Preparing request:\n  previousChoiceID: %s\n  configuration: %s\n  model: nil\n  input: <private>\n  inputHint: %s\n  tools: %s\n  toolChoice: %s\n  toolCallOutputs: <count=%ld>\n  seed: %s\n  temperature: %s\n  responseFormat: %s"

```
