## libsystem_dnssd.dylib

> `/usr/lib/system/libsystem_dnssd.dylib`

```diff

-2881.80.4.0.1
-  __TEXT.__text: 0x6368
+2881.100.53.0.0
+  __TEXT.__text: 0x620c
   __TEXT.__auth_stubs: 0x3a0
-  __TEXT.__const: 0x14a
+  __TEXT.__const: 0x142
   __TEXT.__cstring: 0x1a8e
   __TEXT.__unwind_info: 0x1c0
   __DATA_CONST.__got: 0x18

   - /usr/lib/system/libsystem_platform.dylib
   - /usr/lib/system/libsystem_pthread.dylib
   - /usr/lib/system/libxpc.dylib
-  UUID: 93B445EA-A98A-342B-BBC6-647F49FFB351
+  UUID: B34F1ABF-FBC7-30DF-BA37-947089ECE0F1
   Functions: 94
   Symbols:   204
   CStrings:  133
Functions:
~ _create_hdr : 272 -> 264
~ _InternalTXTRecordSearch : 180 -> 172
~ _TXTRecordGetValuePtr : 100 -> 96
~ _handle_browse_response : 476 -> 504
~ _DNSServiceQueryRecordInternal : 980 -> 968
~ _DNSServiceProcessResult : 1088 -> 1064
~ _handle_query_response : 692 -> 696
~ _DNSServiceResolveEx : 12 -> 4
~ _DNSServiceQueryRecordEx : 12 -> 4
~ _get_validation_data_from_tlvs : 120 -> 88
~ _get_tracker_hostname_from_tlvs : 148 -> 120
~ _put_tlvs_for_defaults : 312 -> 256
~ _TXTRecordGetCount : 64 -> 52
~ _TXTRecordGetItemAtIndex : 296 -> 284
~ _DNSServiceQueryRecordWithAttribute : 12 -> 4
~ _put_attribute_tlvs : 376 -> 384
~ _put_tlvs_for_validation_attr : 236 -> 220
~ _DNSServiceGetPID : 228 -> 232
~ _handle_resolve_response : 440 -> 444
~ _DNSServiceGetAddrInfoInternal : 844 -> 848
~ _handle_addrinfo_response : 832 -> 808
~ _DNSServiceSetDefaultDomainForUser : 216 -> 228
~ _handle_regservice_response : 452 -> 376
~ _DNSServiceRegisterWithAttribute : 36 -> 12
~ _handle_enumeration_response : 192 -> 168
~ _DNSServiceRegisterRecordInternal : 924 -> 932
~ _DNSServiceRegisterRecordWithAttribute : 36 -> 4
~ _DNSServiceReconfirmRecord : 388 -> 392
~ _PeerConnectionRelease : 336 -> 348
~ _handle_port_mapping_response : 132 -> 120
~ __DNSServiceSleepKeepalive_sockaddr : 832 -> 824

```
