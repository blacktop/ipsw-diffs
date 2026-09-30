## CoreFollowUp

> `/System/Library/PrivateFrameworks/CoreFollowUp.framework/Versions/A/CoreFollowUp`

```diff

-254.0.0.0.0
-  __TEXT.__text: 0x22c60
-  __TEXT.__auth_stubs: 0xad0
-  __TEXT.__objc_methlist: 0x12c8
+256.0.0.0.0
+  __TEXT.__text: 0x22714
+  __TEXT.__auth_stubs: 0xac0
+  __TEXT.__objc_methlist: 0x1644
   __TEXT.__const: 0xb7c
-  __TEXT.__cstring: 0x1f6b
+  __TEXT.__cstring: 0x1f9b
   __TEXT.__oslogstring: 0x1496
   __TEXT.__gcc_except_tab: 0x3ac
   __TEXT.__swift5_typeref: 0x373

   __TEXT.__swift5_types: 0x24
   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_capture: 0x114
-  __TEXT.__unwind_info: 0xa90
-  __TEXT.__eh_frame: 0x470
+  __TEXT.__swift_as_entry: 0x24
+  __TEXT.__swift_as_ret: 0x28
+  __TEXT.__unwind_info: 0xab8
+  __TEXT.__eh_frame: 0x448
   __TEXT.__objc_classname: 0x2b8
   __TEXT.__objc_methname: 0x33f2
   __TEXT.__objc_methtype: 0x71b
   __TEXT.__objc_stubs: 0x20e0
-  __DATA_CONST.__got: 0x138
+  __DATA_CONST.__got: 0x130
   __DATA_CONST.__const: 0x438
   __DATA_CONST.__objc_classlist: 0xb8
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x68
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xd18
+  __DATA_CONST.__objc_selrefs: 0xdb8
   __DATA_CONST.__objc_arraydata: 0x50
-  __AUTH_CONST.__auth_got: 0x578
-  __AUTH_CONST.__const: 0xf70
-  __AUTH_CONST.__cfstring: 0x1e80
-  __AUTH_CONST.__objc_const: 0x5010
+  __AUTH_CONST.__auth_got: 0x570
+  __AUTH_CONST.__const: 0xf90
+  __AUTH_CONST.__cfstring: 0x1ec0
+  __AUTH_CONST.__objc_const: 0x49b8
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x50
   __AUTH.__data: 0x110

   __DATA.__objc_superrefs: 0x58
   __DATA.__objc_ivar: 0x1a0
   __DATA.__data: 0x678
-  __DATA.__bss: 0x1120
+  __DATA.__bss: 0x1130
   __DATA.__common: 0x10
   __DATA_DIRTY.__objc_data: 0x6e0
   __DATA_DIRTY.__data: 0x8

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: CD30967D-9FC2-3253-A002-A8514E38F8F5
-  Functions: 1024
-  Symbols:   1718
-  CStrings:  1378
+  UUID: 488A4253-3DDF-3087-A997-8C9CC60B55AD
+  Functions: 1053
+  Symbols:   1747
+  CStrings:  1382
 
Symbols:
+ +[FLApprovedItemsFilter sharedFilter].cold.1
+ +[FLDaemon sharedInstance].cold.1
+ +[FLExtensionHostContext _extensionAuxiliaryHostProtocol].cold.1
+ +[FLExtensionHostContext _extensionAuxiliaryVendorProtocol].cold.1
+ +[FLFollowUpAction _validURLToLaunch:].cold.2
+ +[FLFollowUpItem _expirationDateFormatter].cold.1
+ +[FLHeadlessExtensionLoader _isBundleExecutableAppleSigned:].cold.4
+ +[FLHeadlessExtensionLoader sharedExtensionQueue].cold.1
+ +[FLTelemetryFactory sharedTelemetryController].cold.1
+ +[FLUIHelperController sharedInstance].cold.1
+ -[FLEnvironment isInternal].cold.1
+ -[FLEnvironment shouldHideAllFollowUps].cold.1
+ -[FLEnvironment stressBundleIdentifiers].cold.1
+ -[FLEnvironment stressMode].cold.1
+ -[FLEnvironment supportedNotifyingAppIds].cold.1
+ FLLocDeviceSpecific.cold.1
+ FLLocDeviceSpecific.cold.2
+ _FLLogSystem.cold.1
+ _FLLogSystemQuery.cold.1
+ _FLSignpostGetNanoseconds.cold.1
+ _FLSignpostLogSystem.cold.1
+ ___38+[FLFollowUpAction _validURLToLaunch:]_block_invoke
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ _validURLToLaunch:.approvedURLSchemes
+ _validURLToLaunch:.onceToken
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/CoreFollowUp/CoreFollowUp/FLHeadlessExtensionLoader.m"
+ "com.apple.Home-private"
+ "com.apple.homed.hh2-upgrade"
- "/AppleInternal/Library/BuildRoots/b73fa48b-bc8d-11ef-a2a7-aabfac210453/Library/Caches/com.apple.xbs/Sources/CoreFollowUp/CoreFollowUp/FLHeadlessExtensionLoader.m"

```
