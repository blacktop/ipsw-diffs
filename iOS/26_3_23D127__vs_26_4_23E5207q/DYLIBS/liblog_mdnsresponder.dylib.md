## liblog_mdnsresponder.dylib

> `/usr/lib/log/liblog_mdnsresponder.dylib`

```diff

-2881.80.4.0.1
-  __TEXT.__text: 0x8d54
-  __TEXT.__auth_stubs: 0x200
+2881.100.53.0.0
+  __TEXT.__text: 0x8da4
+  __TEXT.__auth_stubs: 0x1e0
   __TEXT.__cstring: 0xfab
-  __TEXT.__unwind_info: 0x150
+  __TEXT.__unwind_info: 0x148
   __TEXT.__objc_methname: 0xa1
   __TEXT.__objc_stubs: 0x160
   __DATA_CONST.__got: 0x30
   __DATA_CONST.__const: 0xa58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0x58
-  __AUTH_CONST.__auth_got: 0x108
+  __AUTH_CONST.__auth_got: 0xf8
   __AUTH_CONST.__const: 0x1d0
   __AUTH_CONST.__cfstring: 0x7a0
   __DATA.__bss: 0x90

   - /System/Library/PrivateFrameworks/CoreUtils.framework/CoreUtils
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 36755E97-8E66-3DE1-B34F-BEF3EF2F2F19
+  UUID: D3541D75-B731-3E43-9F4E-31DE53565ED0
   Functions: 74
-  Symbols:   195
+  Symbols:   193
   CStrings:  440
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retain
- _objc_retain_x1
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
~ _MDNSOLCopyFormattedStringMDNSNameHashTypeBytes : 512 -> 540
~ _MDNSOLCopyFormattedStringmDNSMACAddr : 488 -> 496
~ _MDNSOLCopyFormattedStringDataLinkEvent : 544 -> 564
~ _MDNSOLCopyFormattedStringmDNSIPAddr : 508 -> 516
~ _MDNSOLCopyFormattedStringHexSequence : 276 -> 316
~ _MDNSOLCopyFormattedStringmDNSLabel : 688 -> 700
~ _MDNSOLCopyFormattedStringmDNSLabelSequenceName : 480 -> 492
~ _MDNSOLCopyFormattedStringDNSScopeType : 180 -> 184
~ _MDNSOLCopyFormattedStringD2DServiceEvent : 260 -> 264
~ _mdns_parse_uint16_be : 88 -> 84
~ _mdns_parse_printable_ascii_run : 140 -> 136

```
