## liblog_mdns.dylib

> `/usr/lib/log/liblog_mdns.dylib`

```diff

-2881.120.11.0.0
-  __TEXT.__text: 0x8c1c
-  __TEXT.__auth_stubs: 0x1e0
-  __TEXT.__cstring: 0xe72
-  __TEXT.__unwind_info: 0x190
-  __TEXT.__objc_methname: 0xd1
-  __TEXT.__objc_stubs: 0x180
-  __DATA_CONST.__got: 0x30
-  __DATA_CONST.__const: 0xc48
+3066.0.0.502.1
+  __TEXT.__text: 0x585c
+  __TEXT.__objc_methlist: 0x14c
+  __TEXT.__cstring: 0xdbb
+  __TEXT.__const: 0x20
+  __TEXT.__unwind_info: 0x150
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
+  __DATA_CONST.__const: 0xab8
+  __DATA_CONST.__objc_classlist: 0x10
+  __DATA_CONST.__objc_protolist: 0x18
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x60
-  __AUTH_CONST.__auth_got: 0xf8
-  __AUTH_CONST.__const: 0x2c0
-  __AUTH_CONST.__cfstring: 0x5a0
-  __DATA.__bss: 0x30
-  __DATA_DIRTY.__bss: 0x60
+  __DATA_CONST.__objc_selrefs: 0x120
+  __DATA_CONST.__objc_superrefs: 0x8
+  __DATA_CONST.__got: 0x0
+  __AUTH_CONST.__const: 0x310
+  __AUTH_CONST.__cfstring: 0x5c0
+  __AUTH_CONST.__objc_const: 0x2f8
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0xa0
+  __DATA.__data: 0x120
+  __DATA.__bss: 0x38
+  __DATA_DIRTY.__bss: 0x10
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AE17A659-1257-34CF-BF46-A984D26655D9
-  Functions: 101
-  Symbols:   242
-  CStrings:  450
+  UUID: DA760504-479C-3D34-A2A9-959A00AC756B
+  Functions: 84
+  Symbols:   284
+  CStrings:  427
 
Symbols:
+ -[OS_log_mdns_object dealloc]
+ -[OS_log_mdns_object debugDescription]
+ -[OS_log_mdns_object description]
+ -[OS_log_mdns_object isEqual:]
+ -[OS_log_mdns_object redactedDescription]
+ _CFStringCreateWithCStringNoCopy
+ _OBJC_CLASS_$_OS_log_mdns_mdns_string_builder
+ _OBJC_CLASS_$_OS_log_mdns_object
+ _OBJC_CLASS_$_OS_object
+ _OBJC_METACLASS_$_NSObject
+ _OBJC_METACLASS_$_OS_log_mdns_mdns_string_builder
+ _OBJC_METACLASS_$_OS_log_mdns_object
+ _OBJC_METACLASS_$_OS_object
+ __AppendHexString
+ __DNSRecordDataToStringEx2
+ __DNSRecordDataToStringEx2.kBase32ExtendedHex
+ __OBJC_$_INSTANCE_METHODS_OS_log_mdns_object
+ __OBJC_$_PROP_LIST_NSObject
+ __OBJC_$_PROP_LIST_OS_log_mdns_mdns_string_builder
+ __OBJC_$_PROP_LIST_OS_log_mdns_object
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_NSObject
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_NSObject
+ __OBJC_$_PROTOCOL_METHOD_TYPES_NSObject
+ __OBJC_$_PROTOCOL_REFS_OS_log_mdns_mdns_string_builder
+ __OBJC_$_PROTOCOL_REFS_OS_log_mdns_object
+ __OBJC_CLASS_PROTOCOLS_$_OS_log_mdns_mdns_string_builder
+ __OBJC_CLASS_PROTOCOLS_$_OS_log_mdns_object
+ __OBJC_CLASS_RO_$_OS_log_mdns_mdns_string_builder
+ __OBJC_CLASS_RO_$_OS_log_mdns_object
+ __OBJC_LABEL_PROTOCOL_$_NSObject
+ __OBJC_LABEL_PROTOCOL_$_OS_log_mdns_mdns_string_builder
+ __OBJC_LABEL_PROTOCOL_$_OS_log_mdns_object
+ __OBJC_METACLASS_RO_$_OS_log_mdns_mdns_string_builder
+ __OBJC_METACLASS_RO_$_OS_log_mdns_object
+ __OBJC_PROTOCOL_$_NSObject
+ __OBJC_PROTOCOL_$_OS_log_mdns_mdns_string_builder
+ __OBJC_PROTOCOL_$_OS_log_mdns_object
+ ____mdns_siphash_get_per_process_key_block_invoke
+ ___block_descriptor_tmp.220
+ ___block_descriptor_tmp.224
+ ___block_descriptor_tmp.422
+ ___block_literal_global.222
+ ___block_literal_global.226
+ ___block_literal_global.420
+ ___error
+ __log_mdns_format_domain_label_hash
+ __log_mdns_format_domain_name_hash
+ __log_mdns_format_hash_with_prefix
+ __log_mdns_format_hex_hash
+ __log_mdns_format_ip_hash
+ __log_mdns_format_ipv4_hash
+ __log_mdns_format_ipv6_hash
+ __log_mdns_format_mac_hash
+ __log_mdns_format_rdata_hash
+ __log_mdns_format_string_hash
+ __mdns_obj_copy_description
+ __mdns_obj_copy_description_as_cfstring
+ __mdns_siphash_get_per_process_key.s_siphash_key
+ __mdns_siphash_get_per_process_key.s_siphash_key_once
+ __mdns_siphash_with_key_ex
+ __mdns_string_builder_append_private_string
+ __mdns_string_builder_copy_description
+ __mdns_string_builder_finalize
+ __mdns_string_builder_grow_buffer
+ __mdns_string_builder_kind
+ __objc_empty_cache
+ __os_object_alloc
+ _arc4random_buf
+ _asprintf
+ _if_indextoname
+ _inet_ntop
+ _kCFAllocatorMalloc
+ _malloc_good_size
+ _mdns_base64_encode_u32_unpadded
+ _mdns_base64_encode_u32_unpadded.base64_charset
+ _mdns_obj_kind
+ _mdns_privacy_obfuscate_domain_name_str
+ _mdns_privacy_obfuscate_ipv4_address
+ _mdns_privacy_obfuscate_ipv6_address
+ _mdns_siphash_u32
+ _mdns_string_builder_append_escaped_ascii_string
+ _mdns_string_builder_append_formatted
+ _mdns_string_builder_append_ipv4_address
+ _mdns_string_builder_append_ipv6_address
+ _mdns_string_builder_copy_string
+ _mdns_string_builder_create
+ _objc_claimAutoreleasedReturnValue
+ _objc_msgSend$stringWithFormat:
+ _objc_msgSend$unsignedIntValue
+ _objc_msgSendSuper2
+ _objc_release_x21
+ _objc_retain
+ _objc_retain_x1
+ _objc_retain_x2
+ _objc_retain_x20
+ _objc_retain_x21
+ _objc_retain_x8
+ _os_release
+ _vsnprintf
- _DNSClassTypeToString
- _DNSComputeDNSKeyTag
- _DNSExtendedDNSErrorCodeToString
- _DNSMessageCollapse
- _DNSMessageExtractQuestion
- _DNSMessageExtractRData
- _DNSMessageExtractRecord
- _DNSMessageGetAnswerSection
- _DNSMessageGetExtendedDNSError
- _DNSMessageGetOptRecord
- _DNSMessagePrintObfuscatedIPv4Address
- _DNSMessagePrintObfuscatedIPv6Address
- _DNSMessagePrintObfuscatedString
- _DNSMessageToString
- _DNSMessageWriteQuery
- _DNSRCodeFromString
- _DNSRCodeFromString.sTable
- _DNSRCodeToString
- _DNSRecordDataToStringEx
- _DNSRecordDataToStringEx.kBase32ExtendedHex
- _DNSRecordTypeStringToValue
- _DomainLabelEqual
- _DomainNameAppendDomainName
- _DomainNameAppendString
- _DomainNameDupEx
- _DomainNameFromString
- _DomainNameLabelCount
- _DomainNameLength
- __AppendDomainNameStringEx
- __AppendEscapedASCIIString
- __AppendIPAddress
- __AppendIPv4Address
- __AppendIPv6Address
- __DNSMessagePrintObfuscatedIPAddress
- __DNSRCodeFromStringCmp
- __GetCUSymAddr_DataBuffer_Append.sAddr
- __GetCUSymAddr_DataBuffer_Append.sOnce
- __GetCUSymAddr_DataBuffer_AppendF.sAddr
- __GetCUSymAddr_DataBuffer_AppendF.sOnce
- __GetCUSymAddr_DataBuffer_Detach.sAddr
- __GetCUSymAddr_DataBuffer_Detach.sOnce
- __GetCUSymAddr_DataBuffer_Free.sAddr
- __GetCUSymAddr_DataBuffer_Free.sOnce
- __GetCUSymAddr_DataBuffer_Init.sAddr
- __GetCUSymAddr_DataBuffer_Init.sOnce
- __GetCUSymAddr_SNPrintF.sAddr
- __GetCUSymAddr_SNPrintF.sOnce
- __NameIsPrivate
- ____GetCUSymAddr_DataBuffer_AppendF_block_invoke
- ____GetCUSymAddr_DataBuffer_Append_block_invoke
- ____GetCUSymAddr_DataBuffer_Detach_block_invoke
- ____GetCUSymAddr_DataBuffer_Free_block_invoke
- ____GetCUSymAddr_DataBuffer_Init_block_invoke
- ____GetCUSymAddr_SNPrintF_block_invoke
- ___block_descriptor_tmp.218
- ___block_descriptor_tmp.222
- ___block_descriptor_tmp.233
- ___block_descriptor_tmp.237
- ___block_descriptor_tmp.241
- ___block_descriptor_tmp.251
- ___block_descriptor_tmp.255
- ___block_descriptor_tmp.262
- ___block_literal_global.220
- ___block_literal_global.224
- ___block_literal_global.235
- ___block_literal_global.239
- ___block_literal_global.243
- ___block_literal_global.253
- ___block_literal_global.257
- ___block_literal_global.264
- ___memcpy_chk
- __log_mdns_negative_reason_to_string
- __log_mdns_protocol_to_string
- __log_mdns_session_event_to_string
- __log_mdns_termination_reason_to_string
- _dnssec_insecure_validation_state_to_description
- _dnssec_result_to_description
- _mdns_dns_service_type_description
- _mdns_memcmp_us_ascii_case_insensitive
- _mdns_memcpy_bits
- _mdns_parse_length_prefixed_string
- _mdns_parse_printable_ascii_run
- _mdns_parse_uint16_be
- _objc_retainAutoreleasedReturnValue
CStrings:
+ " %d%02d%02d%02d%02d%02d"
+ " %s%s"
+ " '"
+ "%%%s"
+ "%%%u"
+ "%*s"
+ "%.*s"
+ "%02X"
+ "%s %s"
+ "'"
+ ":%d"
+ "<%s: %p>"
+ "<%s: %p>: "
+ "<%s:%s>"
+ "<dn:%s>"
+ "<ipv4:%s>"
+ "<ipv6:%s>"
+ "=\""
+ "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
+ "capacity: %zu, string length: %zu"
+ "dl"
+ "dl_hash"
+ "dn"
+ "dn_hash"
+ "hex"
+ "hex_hash"
+ "ip"
+ "ip_hash"
+ "ipv4"
+ "ipv4_hash"
+ "ipv6"
+ "ipv6_hash"
+ "mac"
+ "mac_hash"
+ "mdns_obj"
+ "mdns_string_builder"
+ "ohttp"
+ "rd"
+ "rd_hash"
+ "s"
+ "s_hash"
+ "tls-supported-groups"
- "\n"
- "\n\t"
- "\nADDITIONAL SECTION\n"
- "\nANSWER SECTION\n"
- "\nAUTHORITY SECTION\n"
- "\nQUESTION SECTION\n"
- "\n]"
- " %#H"
- " %-5s"
- " %-5s\n"
- " %.4H"
- " %2s"
- " %6u %2s"
- " %s=\""
- " %u%02u%02u%02u%02u%02u"
- " '%H'"
- " TYPE%u\n"
- "%#.4a"
- "%#H"
- "%#{txt}"
- "%-30s"
- "%-42s"
- "%.16a"
- "%.4H"
- "%s "
- "%s OPT %u"
- "%s%.*a"
- "%s%~s"
- "%~-30s"
- "%~-42s"
- "%~s"
- "%~s "
- ",\n\t"
- "Additional count: %u\n"
- "Answer count:     %u\n"
- "Authority count:  %u\n"
- "BADALG"
- "BADCOOKIE"
- "BADKEY"
- "BADMODE"
- "BADNAME"
- "BADTIME"
- "BADTRUNC"
- "BADVERS"
- "CF"
- "DataBuffer_Append"
- "DataBuffer_AppendF"
- "DataBuffer_Detach"
- "DataBuffer_Free"
- "DataBuffer_Init"
- "Flags:            0x%04X %c/"
- "ID:               0x%04X (%u)\n"
- "Question count:   %u\n"
- "SNPrintF"
- "appendFormat:"
- "appendString:"
- "boolValue"
- "bytes"
- "initWithBytesNoCopy:length:encoding:freeWhenDone:"
- "initWithCapacity:"
- "initWithFormat:"
- "initWithString:"
- "length"
- "longLongValue"
- "stringWithUTF8String:"
- "unsignedLongLongValue"

```
