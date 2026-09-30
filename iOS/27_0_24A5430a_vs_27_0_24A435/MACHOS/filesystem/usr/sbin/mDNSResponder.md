## mDNSResponder

> `/usr/sbin/mDNSResponder`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA.__data`

```diff

 3111.0.5.0.1
-  __TEXT.__text: 0x10abd0
+  __TEXT.__text: 0x10abd4
   __TEXT.__auth_stubs: 0x2fc0
   __TEXT.__objc_stubs: 0x20c0
   __TEXT.__objc_methlist: 0x694
Functions:
~ _AdvertiseInterface : 1876 -> 1880
~ _mDNS_Execute : 25424 -> 25440
~ _putDomainNameAsLabels : 524 -> 528
~ _GetLargeResourceRecord : 1104 -> 1108
~ _SendResponses : 7588 -> 7592
~ _mDNSCoreReceiveNoUnicastAnswers : 18636 -> 18600
~ _GetRRDisplayString_rdb : 2864 -> 2868
~ _DNSMessageExtractRData : 1416 -> 1420
```
