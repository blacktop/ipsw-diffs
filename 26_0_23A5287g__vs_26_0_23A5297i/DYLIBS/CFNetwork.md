## CFNetwork

> `/System/Library/Frameworks/CFNetwork.framework/CFNetwork`

```diff

-3857.100.1.0.0
-  __TEXT.__text: 0x2614a8
+3859.100.1.0.0
+  __TEXT.__text: 0x2614d0
   __TEXT.__auth_stubs: 0x5510
   __TEXT.__delay_stubs: 0x840
   __TEXT.__delay_helper: 0x19ec
   __TEXT.__objc_methlist: 0x9b8c
   __TEXT.__const: 0xc9b9c
   __TEXT.__cstring: 0x18696
-  __TEXT.__gcc_except_tab: 0x148c4
-  __TEXT.__oslogstring: 0xf842
+  __TEXT.__gcc_except_tab: 0x148cc
+  __TEXT.__oslogstring: 0xf840
   __TEXT.__dof_CFNetwork: 0xf3b
   __TEXT.__unwind_info: 0xba80
   __TEXT.__objc_classname: 0x1484

   - /usr/lib/libsp.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 1F8F3F64-5519-3335-B3A7-DB646A4128EA
+  UUID: 693A4DC2-D091-31F4-852E-227E4BC83198
   Functions: 12628
   Symbols:   36033
   CStrings:  11124
Functions:
~ -[__NSCFBackgroundSessionTask cookiesForRequest:] : 636 -> 668
~ ___49-[__NSCFBackgroundSessionTask cookiesForRequest:]_block_invoke : 60 -> 64
~ -[NSURLCache initWithMemoryCapacity:diskCapacity:directoryURL:] : 340 -> 344
CStrings:
+ "[Telemetry]: Calling symptoms. The number of transactions are %u"
- "[Telemetry]: Calling symptoms. The number of transactions are %llu"

```
