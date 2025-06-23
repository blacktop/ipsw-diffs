## AskPermission

> `/System/Library/PrivateFrameworks/AskPermission.framework/AskPermission`

```diff

-129.0.17.0.0
-  __TEXT.__text: 0x884c
-  __TEXT.__auth_stubs: 0x700
-  __TEXT.__objc_methlist: 0x9fc
+129.0.20.0.0
+  __TEXT.__text: 0x95b8
+  __TEXT.__auth_stubs: 0x710
+  __TEXT.__objc_methlist: 0xa0c
   __TEXT.__const: 0xe2
-  __TEXT.__gcc_except_tab: 0x338
-  __TEXT.__cstring: 0x768
-  __TEXT.__oslogstring: 0x93b
+  __TEXT.__gcc_except_tab: 0x37c
+  __TEXT.__cstring: 0x788
+  __TEXT.__oslogstring: 0xa88
   __TEXT.__swift5_typeref: 0x94
   __TEXT.__swift5_capture: 0x70
   __TEXT.__swift_as_entry: 0x14

   __TEXT.__unwind_info: 0x348
   __TEXT.__eh_frame: 0x1d0
   __TEXT.__objc_classname: 0x169
-  __TEXT.__objc_methname: 0x199b
+  __TEXT.__objc_methname: 0x19c4
   __TEXT.__objc_methtype: 0x54e
-  __TEXT.__objc_stubs: 0x1060
+  __TEXT.__objc_stubs: 0x1080
   __DATA_CONST.__got: 0x118
-  __DATA_CONST.__const: 0x440
+  __DATA_CONST.__const: 0x420
   __DATA_CONST.__objc_classlist: 0x60
   __DATA_CONST.__objc_catlist: 0x38
   __DATA_CONST.__objc_protolist: 0x38
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x710
+  __DATA_CONST.__objc_selrefs: 0x718
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__auth_got: 0x390
+  __AUTH_CONST.__auth_got: 0x398
   __AUTH_CONST.__const: 0x180
-  __AUTH_CONST.__cfstring: 0xb20
-  __AUTH_CONST.__objc_const: 0x1088
+  __AUTH_CONST.__cfstring: 0xb60
+  __AUTH_CONST.__objc_const: 0x1090
   __AUTH_CONST.__objc_intobj: 0x48
   __AUTH_CONST.__objc_arrayobj: 0x18
   __DATA.__objc_ivar: 0x5c

   - /usr/lib/swift/libswiftCore.dylib
   - /usr/lib/swift/libswiftCoreFoundation.dylib
   - /usr/lib/swift/libswiftCoreImage.dylib
-  - /usr/lib/swift/libswiftDarwin.dylib
   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftMetal.dylib
   - /usr/lib/swift/libswiftOSLog.dylib

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation1.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  - /usr/lib/swift/libswift_DarwinFoundation3.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: A5A9BC74-A281-3DBF-A327-E3CBC39CF7F4
-  Functions: 225
-  Symbols:   953
-  CStrings:  612
+  UUID: A3CB8B29-AF4E-347C-BC98-25172455B87D
+  Functions: 227
+  Symbols:   952
+  CStrings:  623
 
Symbols:
+ +[APRequestHandler getRequestWithItemIdentifier:completion:]
+ GCC_except_table14
+ GCC_except_table17
+ _NSStringFromSelector
+ ___44-[APConnectionNotifier _newRemoteConnection]_block_invoke.79
+ ___57+[APMetricsEvent nonIdentifiableMetricsFieldsForAccount:]_block_invoke.61
+ ___60+[APRequestHandler getRequestWithItemIdentifier:completion:]_block_invoke
+ ___block_descriptor_56_e8_32s_e42_"AMSPromise"24?0"NSString"8"NSError"16ls32l8
+ ___block_descriptor_56_e8_32s_e59_"AMSPromise"24?0"AMSMetricsIdentifierStore"8"NSError"16ls32l8
+ ___block_descriptor_64_e8_32s40s_e46_"AMSPromise"24?0"NSDictionary"8"NSError"16ls32l8s40l8
+ _objc_msgSend$getRequestWithItemIdentifier:completion:
- ___44-[APConnectionNotifier _newRemoteConnection]_block_invoke.78
- ___57+[APMetricsEvent nonIdentifiableMetricsFieldsForAccount:]_block_invoke.54
- ___block_descriptor_48_e8_32s40s_e46_"AMSPromise"24?0"NSDictionary"8"NSError"16ls32l8s40l8
- ___block_descriptor_48_e8_32s_e42_"AMSPromise"24?0"NSString"8"NSError"16ls32l8
- ___block_descriptor_48_e8_32s_e59_"AMSPromise"24?0"AMSMetricsIdentifierStore"8"NSError"16ls32l8
- __swift_FORCE_LOAD_$_swiftDarwin
- __swift_FORCE_LOAD_$_swiftDarwin_$_AskPermission
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1
- __swift_FORCE_LOAD_$_swift_DarwinFoundation1_$_AskPermission
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2
- __swift_FORCE_LOAD_$_swift_DarwinFoundation2_$_AskPermission
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3
- __swift_FORCE_LOAD_$_swift_DarwinFoundation3_$_AskPermission
CStrings:
+ "%@: %@ "
+ "%@: [%@] %@ "
+ "%{public}@: Get Request Data with itemIdentifier/adamID: %{public}@"
+ "%{public}@Creating metrics event. Account: %{public}@ | Request: %{public}@"
+ "%{public}@Error loading Metrics Store for userID: %@"
+ "%{public}@Error loading Metrics clientID: %@"
+ "%{public}@Error obtaining metrics fields: %{public}@"
+ "%{public}@Generating metrics fields for account: %{public}@"
+ "%{public}@LOB is not App Store. Enqueueing standard metrics."
+ "%{public}@Loaded Metrics clientID: %@"
+ "%{public}@Loaded Metrics event fields: %@"
+ "%{public}@Obtained metrics fields: %{public}@"
+ "%{public}@Request is for App Store LOB."
+ "getRequestWithItemIdentifier:completion:"
- "%{public}@: Error loading Metrics Store for userID: %@"
- "%{public}@: Error loading Metrics clientID: %@"
- "%{public}@: LOB is not App Store. Enqueueing standard metrics."
- "%{public}@: Loaded Metrics clientID: %@"
- "%{public}@: Loaded Metrics event fields: %@"

```
