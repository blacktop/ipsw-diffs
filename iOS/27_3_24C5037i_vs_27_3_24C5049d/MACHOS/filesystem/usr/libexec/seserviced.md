## seserviced

> `/usr/libexec/seserviced`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_reflstr`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift5_mpenum`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA.__objc_ivar`
- `__DATA.__objc_data`

```diff

-72.2.0.0.0
-  __TEXT.__text: 0x486ba4
-  __TEXT.__auth_stubs: 0x53e0
+72.4.0.0.0
+  __TEXT.__text: 0x4889ec
+  __TEXT.__auth_stubs: 0x5400
   __TEXT.__delay_stubs: 0x40
   __TEXT.__delay_helper: 0x33c
   __TEXT.__objc_stubs: 0xe800
-  __TEXT.__objc_methlist: 0x71b4
-  __TEXT.__const: 0x16330
+  __TEXT.__objc_methlist: 0x71c4
+  __TEXT.__const: 0x16380
   __TEXT.__gcc_except_tab: 0x32e0
-  __TEXT.__objc_methname: 0x197dd
-  __TEXT.__oslogstring: 0x32d68
-  __TEXT.__cstring: 0x23096
-  __TEXT.__objc_classname: 0x3198
-  __TEXT.__objc_methtype: 0x7ffd
-  __TEXT.__swift5_typeref: 0x5d52
-  __TEXT.__constg_swiftt: 0x61ac
+  __TEXT.__objc_methname: 0x1985d
+  __TEXT.__oslogstring: 0x32e38
+  __TEXT.__cstring: 0x230e6
+  __TEXT.__objc_classname: 0x31c8
+  __TEXT.__objc_methtype: 0x800d
+  __TEXT.__swift5_typeref: 0x5d62
+  __TEXT.__constg_swiftt: 0x61e8
   __TEXT.__swift5_builtin: 0x410
   __TEXT.__swift5_reflstr: 0x668a
-  __TEXT.__swift5_fieldmd: 0x6754
+  __TEXT.__swift5_fieldmd: 0x6764
   __TEXT.__swift5_assocty: 0x828
   __TEXT.__swift5_proto: 0xbcc
-  __TEXT.__swift5_types: 0x6b8
-  __TEXT.__swift_as_entry: 0x528
-  __TEXT.__swift_as_cont: 0xf88
-  __TEXT.__swift5_capture: 0x34ac
+  __TEXT.__swift5_types: 0x6bc
+  __TEXT.__swift_as_entry: 0x52c
+  __TEXT.__swift_as_cont: 0xf8c
+  __TEXT.__swift5_capture: 0x3530
   __TEXT.__swift_as_ret: 0x62c
   __TEXT.__swift5_mpenum: 0xdc
   __TEXT.__swift5_protos: 0x6c
-  __TEXT.__unwind_info: 0xd2f8
-  __TEXT.__eh_frame: 0x16bec
-  __DATA_CONST.__const: 0x16618
+  __TEXT.__unwind_info: 0xcef0
+  __TEXT.__eh_frame: 0x16c1c
+  __DATA_CONST.__const: 0x167a8
   __DATA_CONST.__cfstring: 0x8b80
-  __DATA_CONST.__objc_classlist: 0x890
+  __DATA_CONST.__objc_classlist: 0x898
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x470
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arrayobj: 0x1e0
   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_intobj: 0x870
-  __DATA_CONST.__auth_got: 0x2a08
-  __DATA_CONST.__got: 0x2178
-  __DATA_CONST.__auth_ptr: 0x1048
-  __DATA.__objc_const: 0x19420
-  __DATA.__objc_selrefs: 0x4b08
+  __DATA_CONST.__auth_got: 0x2a18
+  __DATA_CONST.__got: 0x2188
+  __DATA_CONST.__auth_ptr: 0x1050
+  __DATA.__objc_const: 0x194b8
+  __DATA.__objc_selrefs: 0x4b10
   __DATA.__objc_ivar: 0xcfc
   __DATA.__objc_data: 0x6c30
-  __DATA.__data: 0xe8f4
+  __DATA.__data: 0xe9d4
   __DATA.__common: 0x838
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth

   - /System/Library/PrivateFrameworks/SESUIServiceCore.framework/SESUIServiceCore
   - /System/Library/PrivateFrameworks/SEService.framework/SEService
   - /System/Library/PrivateFrameworks/STSXPCHelperClient.framework/STSXPCHelperClient
+  - /System/Library/PrivateFrameworks/SetupAssistant.framework/SetupAssistant
   - /System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking
   - /System/Library/PrivateFrameworks/SoftPosReader.framework/SoftPosReader
   - /System/Library/PrivateFrameworks/SpringBoardServices.framework/SpringBoardServices

   - /usr/lib/swift/libswift_StringProcessing.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 13513
-  Symbols:   2613
-  CStrings:  11721
+  Functions: 13533
+  Symbols:   2617
+  CStrings:  11729
 
Symbols:
+ _$ss4Int8Vs23CustomStringConvertiblesWP
+ _BYSetupAssistantFinishedDarwinNotification
+ _BYSetupAssistantNeedsToRun
+ _notify_cancel
CStrings:
+ "Aliro passive entry disabled (threshold "
+ "AliroPassiveEntryDisabled"
+ "Failed to register for Setup Assistant notification %u"
+ "Setup Assistant finished"
+ "Setup Assistant finished while registering"
+ "Setup Assistant is running, waiting for it to finish"
+ "_TtC10seserviced17DSKSetupAssistant"
+ "homeDidUpdateUnrecognizedUserSettings:"
+ "iOS (27.3) - SecureElementService-72.4"
- "iOS (27.3) - SecureElementService-72.2"
```
