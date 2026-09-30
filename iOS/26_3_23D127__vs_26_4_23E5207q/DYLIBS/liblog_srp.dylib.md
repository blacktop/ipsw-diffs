## liblog_srp.dylib

> `/usr/lib/log/liblog_srp.dylib`

```diff

-2881.80.4.0.1
-  __TEXT.__text: 0x7ff8
-  __TEXT.__auth_stubs: 0x1a0
+2881.100.53.0.0
+  __TEXT.__text: 0x7f74
+  __TEXT.__auth_stubs: 0x180
   __TEXT.__cstring: 0xad7
-  __TEXT.__unwind_info: 0x128
+  __TEXT.__unwind_info: 0x130
   __TEXT.__objc_methname: 0x4f
   __TEXT.__objc_stubs: 0xc0
   __DATA_CONST.__got: 0x20
   __DATA_CONST.__const: 0x9f8
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x30
-  __AUTH_CONST.__auth_got: 0xd8
+  __AUTH_CONST.__auth_got: 0xc8
   __AUTH_CONST.__const: 0x150
   __AUTH_CONST.__cfstring: 0xe0
   __DATA.__bss: 0x90

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AC60476D-9931-30B3-9B9A-144735B134E6
+  UUID: 9529513B-EAF2-3DC0-824E-DC241A5003BA
   Functions: 65
-  Symbols:   166
+  Symbols:   164
   CStrings:  316
 
Symbols:
+ _objc_release_x21
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_release_x20
- _objc_release_x23
- _objc_retain
Functions:
~ _DomainNameToString : 336 -> 316
~ __DNSMessageExtractRecordEx : 352 -> 348
~ _DNSMessageExtractRData : 1192 -> 1168
~ _DNSMessageGetExtendedDNSError : 252 -> 248
~ _DNSMessageWriteQuery : 220 -> 212
~ _DNSMessageCollapse : 1356 -> 1372
~ _DomainNameAppendString : 336 -> 352
~ _DomainLabelEqual : 84 -> 76
~ _DNSMessageToString : 10212 -> 10020
~ _DNSRecordDataToStringEx : 7648 -> 7764
~ __DNSRecordDataAppendTypeBitMap : 436 -> 408
~ _srp_os_log_copy_formatted_string_domain_name : 540 -> 548
~ _srp_os_log_copy_formatted_string_ipv6_addr_segment : 748 -> 756
~ _mdns_parse_uint16_be : 88 -> 84
~ _mdns_parse_printable_ascii_run : 140 -> 136

```
