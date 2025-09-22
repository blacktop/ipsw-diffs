## EmailCore

> `/System/Library/PrivateFrameworks/EmailCore.framework/EmailCore`

```diff

-3864.100.1.2.9
-  __TEXT.__text: 0x54674
+3864.200.33.2.2
+  __TEXT.__text: 0x548cc
   __TEXT.__auth_stubs: 0x1040
-  __TEXT.__objc_methlist: 0x4f28
+  __TEXT.__objc_methlist: 0x4f40
   __TEXT.__const: 0xe70
-  __TEXT.__gcc_except_tab: 0x6e94
+  __TEXT.__gcc_except_tab: 0x6eb4
   __TEXT.__cstring: 0x7d04
-  __TEXT.__oslogstring: 0xcd8
+  __TEXT.__oslogstring: 0xcf9
   __TEXT.__ustring: 0x90
   __TEXT.__swift5_typeref: 0x52
   __TEXT.__swift5_reflstr: 0x13
   __TEXT.__swift5_assocty: 0x18
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x2800
+  __TEXT.__unwind_info: 0x2818
   __TEXT.__objc_classname: 0xcfc
-  __TEXT.__objc_methname: 0xae68
+  __TEXT.__objc_methname: 0xae83
   __TEXT.__objc_methtype: 0x171b
-  __TEXT.__objc_stubs: 0x7620
-  __DATA_CONST.__got: 0x6a8
+  __TEXT.__objc_stubs: 0x7660
+  __DATA_CONST.__got: 0x6b0
   __DATA_CONST.__const: 0x2208
   __DATA_CONST.__objc_classlist: 0x328
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2978
+  __DATA_CONST.__objc_selrefs: 0x2988
   __DATA_CONST.__objc_protorefs: 0x18
   __DATA_CONST.__objc_superrefs: 0x278
   __DATA_CONST.__objc_arraydata: 0x80
   __AUTH_CONST.__auth_got: 0x830
-  __AUTH_CONST.__const: 0x718
+  __AUTH_CONST.__const: 0x738
   __AUTH_CONST.__cfstring: 0x52a0
-  __AUTH_CONST.__objc_const: 0x9cf8
+  __AUTH_CONST.__objc_const: 0x9d18
   __AUTH_CONST.__objc_arrayobj: 0xf0
   __AUTH_CONST.__objc_intobj: 0x198
   __AUTH.__objc_data: 0x390
   __AUTH.__data: 0x88
   __DATA.__objc_ivar: 0x4a4
   __DATA.__data: 0xd44
-  __DATA.__bss: 0x3b0
+  __DATA.__bss: 0x3d0
   __DATA.__common: 0x24
   __DATA_DIRTY.__objc_data: 0x1c20
   __DATA_DIRTY.__data: 0xb50
-  __DATA_DIRTY.__bss: 0x208
+  __DATA_DIRTY.__bss: 0x218
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /System/Library/PrivateFrameworks/EmailAddressing.framework/EmailAddressing
   - /System/Library/PrivateFrameworks/EmailFoundation.framework/EmailFoundation
   - /System/Library/PrivateFrameworks/MessageSecurity.framework/MessageSecurity
+  - /System/Library/PrivateFrameworks/NetworkServiceProxy.framework/NetworkServiceProxy
   - /System/Library/PrivateFrameworks/URLFormatting.framework/URLFormatting
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libicucore.A.dylib

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: 600E850A-D118-3C1C-92D5-FCC209745882
-  Functions: 1921
-  Symbols:   7584
-  CStrings:  4461
+  UUID: CAB804AD-938E-3FD9-A1BB-21AC5568795F
+  Functions: 1926
+  Symbols:   7606
+  CStrings:  4464
 
Symbols:
+ +[ECDNSClient log]
+ -[ECDNSClient _txtRecordsForDomain:error:].cold.1
+ _OBJC_CLASS_$_PrivacyProxyClient
+ __OBJC_$_CLASS_METHODS_ECDNSClient
+ __OBJC_$_CLASS_PROP_LIST_ECDNSClient
+ ___18+[ECDNSClient log]_block_invoke
+ ___42-[ECDNSClient _txtRecordsForDomain:error:]_block_invoke_2
+ ___42-[ECDNSClient _txtRecordsForDomain:error:]_block_invoke_2.cold.1
+ __txtRecordsForDomain:error:.dns_agent_uuid
+ __txtRecordsForDomain:error:.onceToken
+ _objc_msgSend$dnsAgentUUID
+ _objc_msgSend$getUUIDBytes:
CStrings:
+ "Failed to fetch a DNS agent UUID"
+ "dnsAgentUUID"
+ "getUUIDBytes:"

```
