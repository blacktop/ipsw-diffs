## liblog_mdns.dylib

> `/usr/lib/log/liblog_mdns.dylib`

```diff

-2881.80.4.0.1
-  __TEXT.__text: 0x8c08
-  __TEXT.__auth_stubs: 0x230
+2881.100.53.0.0
+  __TEXT.__text: 0x8c1c
+  __TEXT.__auth_stubs: 0x1e0
   __TEXT.__cstring: 0xe72
-  __TEXT.__unwind_info: 0x188
+  __TEXT.__unwind_info: 0x190
   __TEXT.__objc_methname: 0xd1
   __TEXT.__objc_stubs: 0x180
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0xc48
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x60
-  __AUTH_CONST.__auth_got: 0x120
+  __AUTH_CONST.__auth_got: 0xf8
   __AUTH_CONST.__const: 0x2c0
   __AUTH_CONST.__cfstring: 0x5a0
   __DATA.__bss: 0x30

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 33F08D14-EBCB-3975-B84A-4980709A8F19
+  UUID: F9E7CDE7-8AA6-3F11-9BA4-8ABC84DAD401
   Functions: 101
-  Symbols:   247
+  Symbols:   242
   CStrings:  450
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_release_x21
- _objc_retain
- _objc_retain_x1
- _objc_retain_x21
- _objc_retain_x8
Functions:
~ _DomainNameToString : 336 -> 316
~ __DNSMessageExtractRecordEx : 352 -> 348
~ _DNSMessageExtractRData : 1264 -> 1240
~ _DNSMessageGetExtendedDNSError : 252 -> 248
~ _DNSMessageWriteQuery : 220 -> 212
~ _DNSMessageCollapse : 1508 -> 1532
~ _DomainNameAppendString : 336 -> 352
~ _DomainLabelEqual : 84 -> 76
~ _DNSMessageToString : 10508 -> 10396
~ _DNSRecordDataToStringEx : 7676 -> 7796
~ __DNSRecordDataAppendTypeBitMap : 444 -> 416
~ _mdns_parse_uint16_be : 88 -> 84
~ _mdns_parse_printable_ascii_run : 140 -> 136
~ __log_mdns_create_record_data_attributed_string : 92 -> 100
~ __log_mdns_format_symptom_result : 96 -> 100
~ __log_mdns_format_session_event : 88 -> 92
~ __log_mdns_format_powerlog_event_subtype : 132 -> 140
~ __log_mdns_format_mortality : 76 -> 80
~ __log_mdns_format_gai_options : 280 -> 284
~ __log_mdns_format_dnssec_result : 132 -> 140
~ __log_mdns_format_dnssec_insecure_validation_state : 132 -> 140
~ __log_mdns_format_dns_service_type : 132 -> 140
~ __log_mdns_format_dns_id_and_flags : 116 -> 120
~ __log_mdns_format_dns_record_type : 116 -> 120
~ __log_mdns_format_dns_counts : 156 -> 160
~ __log_mdns_format_record_type_data : 252 -> 264
~ __log_mdns_extract_record_type_and_rdata : 156 -> 144
~ __log_mdns_format_record_data : 84 -> 80
~ __log_mdns_format_dns_message : 100 -> 104
~ __log_mdns_format_dns_header : 100 -> 104
~ __log_mdns_format_base64 : 240 -> 244

```
