## OSAnalytics

> `/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics`

```diff

-927.40.3.0.0
-  __TEXT.__text: 0x469a4
+927.40.4.0.0
+  __TEXT.__text: 0x470d8
   __TEXT.__auth_stubs: 0x1980
-  __TEXT.__objc_methlist: 0x1bd8
+  __TEXT.__objc_methlist: 0x1bf0
   __TEXT.__const: 0x6e8
-  __TEXT.__oslogstring: 0x392c
-  __TEXT.__cstring: 0x9206
+  __TEXT.__oslogstring: 0x3b0c
+  __TEXT.__cstring: 0x9236
   __TEXT.__gcc_except_tab: 0x12ac
   __TEXT.__dlopen_cstrs: 0x21f
   __TEXT.__constg_swiftt: 0x130

   __TEXT.__swift5_types: 0xc
   __TEXT.__swift5_reflstr: 0x18
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0xca8
+  __TEXT.__unwind_info: 0xcb8
   __TEXT.__eh_frame: 0x170
   __TEXT.__objc_classname: 0x318
-  __TEXT.__objc_methname: 0x510d
+  __TEXT.__objc_methname: 0x5123
   __TEXT.__objc_methtype: 0xc05
-  __TEXT.__objc_stubs: 0x4920
+  __TEXT.__objc_stubs: 0x4940
   __DATA_CONST.__got: 0x400
   __DATA_CONST.__const: 0x1310
   __DATA_CONST.__objc_classlist: 0x100
   __DATA_CONST.__objc_catlist: 0x30
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1628
+  __DATA_CONST.__objc_selrefs: 0x1638
   __DATA_CONST.__objc_superrefs: 0x98
   __DATA_CONST.__objc_arraydata: 0x970
   __AUTH_CONST.__auth_got: 0xcd0
   __AUTH_CONST.__const: 0x4a1
   __AUTH_CONST.__cfstring: 0xa120
-  __AUTH_CONST.__objc_const: 0x38a8
+  __AUTH_CONST.__objc_const: 0x38b8
   __AUTH_CONST.__objc_intobj: 0x4c8
   __AUTH_CONST.__objc_dictobj: 0x550
   __AUTH_CONST.__objc_arrayobj: 0x108

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 69D6500E-4948-3955-A1E3-79516487A46E
-  Functions: 1139
-  Symbols:   3936
-  CStrings:  4320
+  UUID: 90A674AB-F1D4-34AE-B343-0A901CF062BE
+  Functions: 1150
+  Symbols:   3963
+  CStrings:  4334
 
Symbols:
+ -[OSASystemConfiguration(optIn) optInDRE]
+ -[OSASystemConfiguration(optIn) optInDRE].cold.1
+ -[OSASystemConfiguration(optIn) optInDRE].cold.2
+ -[OSASystemConfiguration(optIn) optInDRE].cold.3
+ -[OSASystemConfiguration(optIn) optInDRE].cold.4
+ -[OSASystemConfiguration(optIn) optInDRE].cold.5
+ -[OSASystemConfiguration(optIn) setDREOptIn:]
+ -[OSASystemConfiguration(optIn) setDREOptIn:].cold.1
+ -[OSASystemConfiguration(optIn) setDREOptIn:].cold.2
+ -[OSASystemConfiguration(optIn) setDREOptIn:].cold.3
+ -[OSASystemConfiguration(optIn) setDREOptIn:].cold.4
+ -[OSASystemConfiguration(optIn) setDREOptIn:].cold.5
+ ___block_literal_global.24
+ _objc_msgSend$optInDRE
- ___block_literal_global.20
CStrings:
+ "Failed to retrieve DRE opt-in value"
+ "Failed to set DRE opt-in value to %d"
+ "No reply received from osanalyticshelper for DRE opt-in get request"
+ "No reply received from osanalyticshelper for DRE opt-in request"
+ "Not in DRE, ignoring request to set DRE opt-in."
+ "Opted in for DRE"
+ "Retrieved DRE opt-in value: %d"
+ "Successfully set DRE opt-in value to %d"
+ "Unable to get XPC connection to osanalyticshelper for DRE opt-in"
+ "Unable to get XPC connection to osanalyticshelper for DRE opt-in get"
+ "dre_optInValue"
+ "dre_optIn_operation"
+ "optInDRE"
+ "setDREOptIn:"

```
