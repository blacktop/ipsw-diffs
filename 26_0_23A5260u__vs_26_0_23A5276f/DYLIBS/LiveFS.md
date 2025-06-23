## LiveFS

> `/System/Library/PrivateFrameworks/LiveFS.framework/LiveFS`

```diff

-737.0.2.0.1
-  __TEXT.__text: 0x1d758
-  __TEXT.__auth_stubs: 0x830
-  __TEXT.__objc_methlist: 0x2004
+737.0.10.0.0
+  __TEXT.__text: 0x1cbac
+  __TEXT.__auth_stubs: 0x820
+  __TEXT.__objc_methlist: 0x1f64
   __TEXT.__const: 0x130
-  __TEXT.__cstring: 0x1029
-  __TEXT.__oslogstring: 0x1483
+  __TEXT.__cstring: 0xf87
+  __TEXT.__oslogstring: 0x1415
   __TEXT.__gcc_except_tab: 0xcf4
-  __TEXT.__unwind_info: 0xa08
-  __TEXT.__objc_classname: 0x334
-  __TEXT.__objc_methname: 0x4376
-  __TEXT.__objc_methtype: 0x2a91
-  __TEXT.__objc_stubs: 0x2860
-  __DATA_CONST.__got: 0x188
-  __DATA_CONST.__const: 0xdd0
-  __DATA_CONST.__objc_classlist: 0xd0
+  __TEXT.__unwind_info: 0x9e8
+  __TEXT.__objc_classname: 0x31c
+  __TEXT.__objc_methname: 0x4233
+  __TEXT.__objc_methtype: 0x2a22
+  __TEXT.__objc_stubs: 0x2780
+  __DATA_CONST.__got: 0x180
+  __DATA_CONST.__const: 0xda8
+  __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x1080
+  __DATA_CONST.__objc_selrefs: 0x1020
   __DATA_CONST.__objc_protorefs: 0x38
-  __DATA_CONST.__objc_superrefs: 0xb0
-  __AUTH_CONST.__auth_got: 0x428
+  __DATA_CONST.__objc_superrefs: 0xa8
+  __AUTH_CONST.__auth_got: 0x420
   __AUTH_CONST.__const: 0xc0
-  __AUTH_CONST.__cfstring: 0x840
-  __AUTH_CONST.__objc_const: 0x2ad8
-  __AUTH.__objc_data: 0x6e0
-  __DATA.__objc_ivar: 0x200
+  __AUTH_CONST.__cfstring: 0x760
+  __AUTH_CONST.__objc_const: 0x2a20
+  __AUTH.__objc_data: 0x690
+  __DATA.__objc_ivar: 0x1fc
   __DATA.__data: 0x720
   __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x28

   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: EF8423D9-11D5-3B69-B84D-4B078250C7FF
-  Functions: 791
-  Symbols:   2690
-  CStrings:  1376
+  UUID: 20822633-B8C4-3AF4-89F0-C87137D14435
+  Functions: 771
+  Symbols:   2632
+  CStrings:  1339
 
Symbols:
+ GCC_except_table22
+ GCC_except_table25
+ GCC_except_table31
+ GCC_except_table34
- -[LiveFSHexAndASCIIString .cxx_destruct]
- -[LiveFSHexAndASCIIString characterAtIndex:]
- -[LiveFSHexAndASCIIString data]
- -[LiveFSHexAndASCIIString getCharacters:range:]
- -[LiveFSHexAndASCIIString initWithData:]
- -[LiveFSHexAndASCIIString init]
- -[LiveFSHexAndASCIIString length]
- -[LiveFSMountClient mountVolume:fileSystem:displayName:provider:domainError:on:how:]
- -[LiveFSMountClient mountVolume:provider:on:how:]
- -[LiveFSMountClient unmountVolumeNamed:providerName:domainError:how:reply:]
- -[LiveFSServiceUserClient flushMetaBlocks:ranges:rangesCount:wait:]
- -[LiveFSServiceUserClient flushMetaBlocks:ranges:rangesCount:wait:].cold.1
- -[LiveFSServiceUserClient flushMetaBlocks:ranges:rangesCount:wait:].cold.2
- -[LiveFSServiceUserClient writeMetaAsync:buffer:offset:length:]
- -[LiveFSServiceUserClient writeMetaAsync:buffer:offset:length:].cold.1
- -[LiveFSServiceUserClient writeMetaAsync:buffer:offset:length:].cold.2
- GCC_except_table24
- GCC_except_table27
- GCC_except_table36
- GCC_except_table39
- OBJC_IVAR_$_LiveFSHexAndASCIIString.data
- _NSIntersectionRange
- _OBJC_CLASS_$_LiveFSHexAndASCIIString
- _OBJC_CLASS_$_NSMutableString
- _OBJC_METACLASS_$_LiveFSHexAndASCIIString
- _OBJC_METACLASS_$_NSString
- __OBJC_$_INSTANCE_METHODS_LiveFSHexAndASCIIString
- __OBJC_$_INSTANCE_VARIABLES_LiveFSHexAndASCIIString
- __OBJC_CLASS_RO_$_LiveFSHexAndASCIIString
- __OBJC_METACLASS_RO_$_LiveFSHexAndASCIIString
- ___75-[LiveFSMountClient unmountVolumeNamed:providerName:domainError:how:reply:]_block_invoke
- ___75-[LiveFSMountClient unmountVolumeNamed:providerName:domainError:how:reply:]_block_invoke.78
- ___75-[LiveFSMountClient unmountVolumeNamed:providerName:domainError:how:reply:]_block_invoke.cold.1
- ___block_descriptor_40_e8_32bs_e30_v24?0"NSError"8"NSString"16ls32l8
- _objc_msgSend$appendFormat:
- _objc_msgSend$appendString:
- _objc_msgSend$data
- _objc_msgSend$getCharacters:range:
- _objc_msgSend$initWithData:
- _objc_msgSend$setString:
- _objc_msgSend$unmountVolume:provider:how:domainError:reply:
CStrings:
- "\n"
- " "
- "  "
- "   "
- " %02hhx"
- "%08ld: "
- "%c"
- "-[LiveFSServiceUserClient flushMetaBlocks:ranges:rangesCount:wait:]"
- "-[LiveFSServiceUserClient writeMetaAsync:buffer:offset:length:]"
- "@44@0:8@16@24@32i40"
- "@68@0:8@16@24@32@40@48@56i64"
- "Encountered error on connection to the mounter: %@"
- "LiveFSHexAndASCIIString"
- "S24@0:8Q16"
- "appendFormat:"
- "appendString:"
- "characterAtIndex:"
- "data"
- "flushMetaBlocks:ranges:rangesCount:wait:"
- "flush_meta_blocks returned %d"
- "getCharacters:range:"
- "initWithData:"
- "mountVolume:fileSystem:displayName:provider:domainError:on:how:"
- "mountVolume:provider:on:how:"
- "setString:"
- "unmountVolumeNamed:providerName:domainError:how:reply:"
- "v40@0:8^S16{_NSRange=QQ}24"
- "v52@0:8@16@24@32i40@?44"
- "writeMetaAsync:buffer:offset:length:"
- "write_meta_async returned %d"

```
