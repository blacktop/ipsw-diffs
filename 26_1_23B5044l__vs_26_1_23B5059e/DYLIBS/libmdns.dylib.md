## libmdns.dylib

> `/usr/lib/libmdns.dylib`

```diff

-2881.40.10.0.0
-  __TEXT.__text: 0x32114
+2881.40.17.0.0
+  __TEXT.__text: 0x321f4
   __TEXT.__auth_stubs: 0x1d30
   __TEXT.__objc_methlist: 0x2ec
   __TEXT.__cstring: 0x21a3
   __TEXT.__const: 0x1ad
   __TEXT.__gcc_except_tab: 0xf4
-  __TEXT.__oslogstring: 0x3814
+  __TEXT.__oslogstring: 0x3863
   __TEXT.__unwind_info: 0x990
   __TEXT.__eh_frame: 0x74
   __TEXT.__objc_classname: 0x57f

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: AE08C4E9-B0B6-33F7-9EC5-56672224CE9B
+  UUID: 00C3E415-2046-3768-8CF6-D72D380622FA
   Functions: 817
   Symbols:   3037
-  CStrings:  1180
+  CStrings:  1181
 
Functions:
~ __mdns_resolver_penalize_server_ex : 1132 -> 1356
CStrings:
+ "%{public}sPenalizing unresponsive server %@ for 60 seconds -- symptom report: %{mdns:symptom_result}u"
+ "Trying to report unresponsive symptom for server without IP address: %@"
- "%{public}sWithholding unresponsive server symptom: Lack of response is for local. IN SOA query"

```
