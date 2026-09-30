## osanalyticshelper

> `/System/Library/CoreServices/osanalyticshelper`

```diff

-727.80.2.0.0
-  __TEXT.__text: 0x12e70
-  __TEXT.__auth_stubs: 0xab0
+758.100.43.0.0
+  __TEXT.__text: 0x131c8
+  __TEXT.__auth_stubs: 0xac0
   __TEXT.__objc_stubs: 0x2120
-  __TEXT.__objc_methlist: 0x640
-  __TEXT.__const: 0x12a
-  __TEXT.__oslogstring: 0x19ac
-  __TEXT.__cstring: 0x1a81
+  __TEXT.__objc_methlist: 0x780
+  __TEXT.__const: 0x13a
+  __TEXT.__oslogstring: 0x1a1c
+  __TEXT.__cstring: 0x1941
   __TEXT.__objc_classname: 0x14c
-  __TEXT.__objc_methtype: 0x3c6
-  __TEXT.__gcc_except_tab: 0x880
-  __TEXT.__objc_methname: 0x1c00
+  __TEXT.__objc_methtype: 0x3d7
+  __TEXT.__gcc_except_tab: 0x8dc
+  __TEXT.__objc_methname: 0x1c0f
   __TEXT.__constg_swiftt: 0x94
   __TEXT.__swift5_typeref: 0x78
   __TEXT.__swift5_reflstr: 0xd
   __TEXT.__swift5_fieldmd: 0x28
   __TEXT.__swift5_capture: 0x34
   __TEXT.__swift5_types: 0x4
-  __TEXT.__unwind_info: 0x478
-  __DATA_CONST.__auth_got: 0x570
+  __TEXT.__unwind_info: 0x498
+  __DATA_CONST.__auth_got: 0x578
   __DATA_CONST.__got: 0x468
   __DATA_CONST.__auth_ptr: 0x40
-  __DATA_CONST.__const: 0x9d8
-  __DATA_CONST.__cfstring: 0x1700
+  __DATA_CONST.__const: 0xa38
+  __DATA_CONST.__cfstring: 0x1800
   __DATA_CONST.__objc_classlist: 0x70
   __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_arraydata: 0x50
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_dictobj: 0x50
-  __DATA.__objc_const: 0x1170
-  __DATA.__objc_selrefs: 0x8d8
+  __DATA.__objc_const: 0xf28
+  __DATA.__objc_selrefs: 0x968
   __DATA.__objc_ivar: 0x84
   __DATA.__objc_data: 0x520
   __DATA.__data: 0x1a8

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 1595E386-FC0A-35ED-9F04-BBD34B23AD3E
-  Functions: 302
-  Symbols:   344
-  CStrings:  1022
+  UUID: 8A1C096B-8DEF-358A-84E2-82B14A744845
+  Functions: 314
+  Symbols:   345
+  CStrings:  1030
 
Symbols:
+ _xpc_array_apply
+ _xpc_array_get_string
+ _xpc_connection_get_audit_token
+ _xpc_copy_entitlement_for_token
+ _xpc_dictionary_get_array
- _$sSw10copyMemory4fromySW_tF
- _$sSwys5UInt8VSicis
- _$ss17_assertionFailure__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
- _$ss18_fatalErrorMessage__4file4line5flagss5NeverOs12StaticStringV_A2HSus6UInt32VtF
CStrings:
+ "B24@?0Q8@\"NSObject<OS_xpc_object>\"16"
+ "B40@0:8@16@24@32"
+ "HWModelStr"
+ "Received invalid log-writing request: client is not entitled to create logs. program name: %@, bug type: %@"
+ "com.apple.osanalytics.logs.clientMissingEntitlement"
+ "com.apple.private.osanalytics.write-logs.allow"
+ "com.apple.security.system-groups"
+ "createForSubmissionWithXPCRequest:fromConnection:forReply:"
+ "hwModel"
+ "missing entitlement"
+ "no_hw_model"
+ "progName"
+ "systemgroup.com.apple.osanalytics"
- "Fatal error"
- "Insufficient space allocated to copy string contents"
- "Swift/ContiguousArrayBuffer.swift"
- "Swift/StringTesting.swift"
- "Swift/StringUTF8View.swift"
- "Swift/UnsafeBufferPointer.swift"
- "Swift/UnsafePointer.swift"
- "Swift/UnsafeRawPointer.swift"
- "Unexpectedly found nil while unwrapping an Optional value"
- "UnsafeMutableBufferPointer with negative count"
- "UnsafeMutablePointer.initialize overlapping range"
- "UnsafeMutableRawPointer.initializeMemory overlapping range"
- "createForSubmissionWithXPCRequest:forReply:"
- "invalid Collection: less than 'count' elements in collection"

```
