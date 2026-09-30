## DeviceAccess

> `/System/Library/PrivateFrameworks/DeviceAccess.framework/DeviceAccess`

```diff

-325.12.1.0.0
-  __TEXT.__text: 0x556f4
+325.14.0.0.0
+  __TEXT.__text: 0x56038
   __TEXT.__auth_stubs: 0x1640
-  __TEXT.__objc_methlist: 0x45bc
-  __TEXT.__const: 0x8e0
-  __TEXT.__cstring: 0x9d83
-  __TEXT.__gcc_except_tab: 0x12f8
+  __TEXT.__objc_methlist: 0x45e4
+  __TEXT.__const: 0x920
+  __TEXT.__cstring: 0x9e43
+  __TEXT.__gcc_except_tab: 0x1318
   __TEXT.__constg_swiftt: 0x3b8
   __TEXT.__swift5_typeref: 0x264
   __TEXT.__swift5_builtin: 0x3c

   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_protos: 0x8
   __TEXT.__swift5_capture: 0x1c
-  __TEXT.__unwind_info: 0x14d8
+  __TEXT.__unwind_info: 0x14f0
   __TEXT.__eh_frame: 0x5c0
   __TEXT.__objc_classname: 0x6b4
-  __TEXT.__objc_methname: 0x89c0
+  __TEXT.__objc_methname: 0x8a74
   __TEXT.__objc_methtype: 0xc26
-  __TEXT.__objc_stubs: 0x4a20
-  __DATA_CONST.__got: 0x518
+  __TEXT.__objc_stubs: 0x4b60
+  __DATA_CONST.__got: 0x530
   __DATA_CONST.__const: 0xe80
   __DATA_CONST.__objc_classlist: 0x1e8
   __DATA_CONST.__objc_catlist: 0x10
   __DATA_CONST.__objc_protolist: 0x70
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1f08
+  __DATA_CONST.__objc_selrefs: 0x1f50
   __DATA_CONST.__objc_protorefs: 0x38
   __DATA_CONST.__objc_superrefs: 0x180
   __DATA_CONST.__objc_arraydata: 0x30
   __AUTH_CONST.__auth_got: 0xb30
-  __AUTH_CONST.__const: 0x6b0
-  __AUTH_CONST.__cfstring: 0x34a0
+  __AUTH_CONST.__const: 0x6d0
+  __AUTH_CONST.__cfstring: 0x3500
   __AUTH_CONST.__objc_const: 0x7e08
   __AUTH_CONST.__objc_intobj: 0x90
   __AUTH_CONST.__objc_arrayobj: 0x18

   __AUTH.__data: 0x250
   __DATA.__objc_ivar: 0x6f8
   __DATA.__data: 0xc48
-  __DATA.__bss: 0x2e0
+  __DATA.__bss: 0x2f0
   __DATA.__common: 0x8
   __DATA_DIRTY.__objc_data: 0x780
   __DATA_DIRTY.__data: 0x78

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: FAD0DBA1-9ED2-351E-B030-FA7FD38A1377
-  Functions: 2283
-  Symbols:   6441
-  CStrings:  3714
+  UUID: 70030D89-3FBC-3DFC-92F4-C1E74D8FDCFD
+  Functions: 2292
+  Symbols:   6474
+  CStrings:  3741
 
Symbols:
+ +[DAAccessoryMessage _dateFormatter]
+ +[DAAccessoryMessage _dateFormatter].cold.1
+ +[DAAccessoryMessage intervalToDateFormat:]
+ -[DADeviceAppAccessInfo _hexStringFromData:]
+ -[DAExtension _reportEvent:].cold.3
+ -[DAExtensionCapability _resumeWithError:].cold.1
+ GCC_except_table106
+ GCC_except_table112
+ GCC_except_table116
+ GCC_except_table13
+ GCC_except_table28
+ GCC_except_table41
+ GCC_except_table47
+ GCC_except_table54
+ GCC_except_table62
+ GCC_except_table77
+ GCC_except_table81
+ _DAExtensionTypeToTransportType
+ _DATransportTypeToExtensionType
+ _OBJC_CLASS_$_NSDateFormatter
+ _OBJC_CLASS_$_NSLocale
+ _OBJC_CLASS_$_NSMutableString
+ ___36+[DAAccessoryMessage _dateFormatter]_block_invoke
+ __dateFormatter.sDateFormatter
+ __dateFormatter.sOnce
+ _objc_msgSend$_dateFormatter
+ _objc_msgSend$_hexStringFromData:
+ _objc_msgSend$accessoryMessages
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$dateWithTimeIntervalSince1970:
+ _objc_msgSend$intervalToDateFormat:
+ _objc_msgSend$localeWithLocaleIdentifier:
+ _objc_msgSend$setDateFormat:
+ _objc_msgSend$setLocale:
+ _objc_msgSend$stringFromDate:
+ _objc_msgSend$stringWithCapacity:
- GCC_except_table104
- GCC_except_table110
- GCC_except_table114
- GCC_except_table12
- GCC_except_table26
- GCC_except_table39
- GCC_except_table45
- GCC_except_table52
- GCC_except_table56
- GCC_except_table60
- GCC_except_table75
- GCC_except_table79
- GCC_except_table80
- _objc_msgSend$base64EncodedStringWithOptions:
CStrings:
+ "### missing event handler for %@"
+ "%02x"
+ "@24@0:8d16"
+ "Activate (Resume) %@"
+ "CBRID '%@'"
+ "Exp %@"
+ "FilePath '%@'"
+ "Last %@"
+ "QueueOneID '%@'"
+ "Received %@"
+ "RetryCount %ld"
+ "TsptPrio %ld"
+ "Vers %ld"
+ "_dateFormatter"
+ "_hexStringFromData:"
+ "appendFormat:"
+ "dateWithTimeIntervalSince1970:"
+ "en_US_POSIX"
+ "intervalToDateFormat:"
+ "localeWithLocaleIdentifier:"
+ "setDateFormat:"
+ "setLocale:"
+ "stringFromDate:"
+ "stringWithCapacity:"
+ "yyyy-MM-dd HH:mm:ss:SSSS"
- "base64EncodedStringWithOptions:"

```
