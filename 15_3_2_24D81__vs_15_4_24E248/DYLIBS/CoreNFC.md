## CoreNFC

> `/System/iOSSupport/System/Library/Frameworks/CoreNFC.framework/Versions/A/CoreNFC`

```diff

-353.3.0.0.0
-  __TEXT.__text: 0x32504
-  __TEXT.__auth_stubs: 0xbd0
-  __TEXT.__objc_methlist: 0x1500
+354.27.0.0.0
+  __TEXT.__text: 0x32618
+  __TEXT.__auth_stubs: 0xbc0
+  __TEXT.__objc_methlist: 0x1d34
   __TEXT.__const: 0x9c8
-  __TEXT.__gcc_except_tab: 0x9cc
-  __TEXT.__cstring: 0x256d
+  __TEXT.__gcc_except_tab: 0x9c8
+  __TEXT.__cstring: 0x250d
   __TEXT.__oslogstring: 0x2385
   __TEXT.__swift5_typeref: 0x4a1
   __TEXT.__swift5_fieldmd: 0x4f0

   __TEXT.__swift5_assocty: 0x48
   __TEXT.__swift5_mpenum: 0x18
   __TEXT.__swift5_proto: 0x3c
-  __TEXT.__unwind_info: 0xda8
-  __TEXT.__eh_frame: 0x338
+  __TEXT.__swift_as_entry: 0x38
+  __TEXT.__swift_as_ret: 0x18
+  __TEXT.__unwind_info: 0xdc8
+  __TEXT.__eh_frame: 0x380
   __TEXT.__objc_classname: 0x39b
   __TEXT.__objc_methname: 0x3516
   __TEXT.__objc_methtype: 0x13c5

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x120
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xce8
+  __DATA_CONST.__objc_selrefs: 0xda0
   __DATA_CONST.__objc_protorefs: 0xa8
   __DATA_CONST.__objc_superrefs: 0xa8
-  __AUTH_CONST.__auth_got: 0x5f8
+  __AUTH_CONST.__auth_got: 0x5f0
   __AUTH_CONST.__const: 0x1120
   __AUTH_CONST.__cfstring: 0xe40
-  __AUTH_CONST.__objc_const: 0xaec8
+  __AUTH_CONST.__objc_const: 0x9fd8
   __AUTH.__objc_data: 0xaf0
   __AUTH.__data: 0x5d8
   __DATA.__objc_ivar: 0x118

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: 065C2500-3ED8-34BE-B773-F0C46D01EB71
-  Functions: 1199
-  Symbols:   2234
-  CStrings:  1321
+  UUID: 3A2F9E32-B2BF-344E-B521-0ABE60D8A2C8
+  Functions: 1212
+  Symbols:   2256
+  CStrings:  1319
 
Symbols:
+ +[NFCHardwareManager sharedHardwareManager].cold.1
+ +[NFCHardwareManagerCallbacks interface].cold.1
+ +[NFCHardwareManagerInterface interface].cold.1
+ +[NFCISO15693ReaderSessionTag decodeIdentifier:manufacturerCode:serialNumber:].cold.1
+ -[NFCNDEFTag copyWithZone:].cold.1
+ -[NFCNDEFTag copyWithZone:].cold.2
+ -[NFCNDEFTag initWithCoder:].cold.1
+ -[NFCNDEFTag initWithSession:tag:startupConfig:].cold.1
+ -[NFCNDEFTag initWithSession:tag:startupConfig:].cold.2
+ -[NFCNDEFTag initWithSession:tag:startupConfig:].cold.3
+ -[NFCTag copyWithZone:].cold.1
+ -[NFCTag initWithCoder:].cold.1
+ -[NFCTag initWithSession:tag:startupConfig:].cold.1
+ -[NFCTag initWithSession:tag:startupConfig:].cold.2
+ -[NFCTag initWithSession:tag:startupConfig:].cold.3
+ _OUTLINED_FUNCTION_0
+ _OUTLINED_FUNCTION_1
+ ___swift_async_entry_functlets
+ ___swift_async_ret_functlets
+ __block_literal_global.42
- __block_literal_global.36
CStrings:
- "Swift/UnsafePointer.swift"
- "UnsafeMutablePointer.initialize overlapping range"

```
