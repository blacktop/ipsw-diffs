## PDSAgent

> `/System/Library/PrivateFrameworks/PDSAgent.framework/PDSAgent`

```diff

-1814.100.1.2.2
-  __TEXT.__text: 0x19c98
-  __TEXT.__auth_stubs: 0x600
-  __TEXT.__objc_methlist: 0x1d64
+1814.200.71.2.7
+  __TEXT.__text: 0x1a1c0
+  __TEXT.__auth_stubs: 0x610
+  __TEXT.__objc_methlist: 0x1d74
   __TEXT.__const: 0x70
-  __TEXT.__cstring: 0xfa6
-  __TEXT.__gcc_except_tab: 0x2e4
-  __TEXT.__oslogstring: 0xc81
-  __TEXT.__unwind_info: 0x70c
+  __TEXT.__cstring: 0xfdb
+  __TEXT.__gcc_except_tab: 0x310
+  __TEXT.__oslogstring: 0xcd1
+  __TEXT.__unwind_info: 0x718
   __TEXT.__objc_classname: 0x393
-  __TEXT.__objc_methname: 0x4622
+  __TEXT.__objc_methname: 0x466e
   __TEXT.__objc_methtype: 0xfc6
-  __TEXT.__objc_stubs: 0x3a60
+  __TEXT.__objc_stubs: 0x3ac0
   __DATA_CONST.__got: 0xe0
-  __DATA_CONST.__const: 0x5c0
+  __DATA_CONST.__const: 0x610
   __DATA_CONST.__objc_classlist: 0xf8
   __DATA_CONST.__objc_catlist: 0x18
   __DATA_CONST.__objc_protolist: 0x80
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_const: 0x4720
-  __DATA_CONST.__objc_selrefs: 0x1298
+  __DATA_CONST.__objc_selrefs: 0x12b0
   __DATA_CONST.__objc_arraydata: 0x10
-  __AUTH_CONST.__cfstring: 0x13c0
+  __AUTH_CONST.__cfstring: 0x1460
   __AUTH_CONST.__objc_const: 0xb70
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__const: 0xe0
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x310
+  __AUTH_CONST.__auth_got: 0x318
   __AUTH.__objc_data: 0xa0
-  __DATA.__objc_classrefs: 0x238
+  __DATA.__objc_classrefs: 0x240
   __DATA.__objc_superrefs: 0xc8
   __DATA.__objc_ivar: 0x1b8
   __DATA.__data: 0x600

   - /System/Library/PrivateFrameworks/ProtocolBuffer.framework/ProtocolBuffer
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: F8A6170A-7FA8-3934-9B31-AA4E12462FC6
-  Functions: 678
-  Symbols:   2542
-  CStrings:  1497
+  UUID: 1B104CDA-BA4F-3AFB-984F-4B0E5F2EB985
+  Functions: 682
+  Symbols:   2557
+  CStrings:  1513
 
Symbols:
+ -[PDSDaemon _setupSysdiagnoseDump]
+ _IMLogRegisterStateToSysdiagnoseBlock
+ _OBJC_CLASS_$_NSMutableString
+ ___34-[PDSDaemon _setupSysdiagnoseDump]_block_invoke
+ ___57-[PDSRequestQueue _reAuthAndContinueWithRequest:forUser:]_block_invoke.cold.1
+ ___57-[PDSRequestQueue _reAuthAndContinueWithRequest:forUser:]_block_invoke_3
+ ___block_descriptor_40_e8_32s_e15_"NSString"8?0ls32l8
+ ___block_descriptor_56_e8_32s40s48s_e5_v8?0ls32l8s40l8s48l8
+ _objc_msgSend$_setupSysdiagnoseDump
+ _objc_msgSend$appendFormat:
+ _objc_msgSend$appendString:
+ _objc_msgSend$initWithURL:defaultsDomain:defaultBag:apsEnvironmentName:sosDomain:hashAlgorithm:requiresIDSHost:validateAgainstIDSPolicy:bagType:bypassProcessChecks:logCategory:
- _objc_msgSend$initWithURL:defaultsDomain:defaultBag:apsEnvironmentName:sosDomain:hashAlgorithm:requiresIDSHost:bagType:bypassProcessChecks:logCategory:
CStrings:
+ "\t%@\n"
+ "%@\n"
+ "@\"NSString\"8@?0"
+ "Credential refresh failed for user: %@ error: %@"
+ "Entries:\n"
+ "Kicked off refresh for user %@"
+ "PDS-State"
+ "Users:\n"
+ "_setupSysdiagnoseDump"
+ "appendFormat:"
+ "appendString:"
+ "initWithURL:defaultsDomain:defaultBag:apsEnvironmentName:sosDomain:hashAlgorithm:requiresIDSHost:validateAgainstIDSPolicy:bagType:bypassProcessChecks:logCategory:"
- "initWithURL:defaultsDomain:defaultBag:apsEnvironmentName:sosDomain:hashAlgorithm:requiresIDSHost:bagType:bypassProcessChecks:logCategory:"

```
