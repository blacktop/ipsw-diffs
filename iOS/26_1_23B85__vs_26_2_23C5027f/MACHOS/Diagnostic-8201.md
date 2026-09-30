## Diagnostic-8201

> `/Applications/DiagnosticsService.app/PlugIns/Diagnostic-8201.appex/Diagnostic-8201`

```diff

 57.0.0.0.0
-  __TEXT.__text: 0x26530
+  __TEXT.__text: 0x2652c
   __TEXT.__auth_stubs: 0x830
   __TEXT.__objc_stubs: 0xa60
   __TEXT.__init_offsets: 0x4

   __TEXT.__cstring: 0x5954
   __TEXT.__objc_classname: 0x55
   __TEXT.__objc_methname: 0xba1
-  __TEXT.__objc_methtype: 0x657
+  __TEXT.__objc_methtype: 0x65d
   __TEXT.__oslogstring: 0x99e
   __TEXT.__unwind_info: 0x750
   __DATA_CONST.__auth_got: 0x428

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: FDEB3C0A-756A-31B3-8F9D-7B212C4256A5
+  UUID: 225D7EE7-A3C8-3669-A9D2-30600400ABD3
   Functions: 464
   Symbols:   415
   CStrings:  1465
Functions:
~ sub_100016b48 : 272 -> 268
CStrings:
+ "{vector<PearlConfiguration, std::allocator<PearlConfiguration>>=\"__begin_\"^{PearlConfiguration}\"__end_\"^{PearlConfiguration}\"\"{?=\"__cap_\"^{PearlConfiguration}}}"
- "{vector<PearlConfiguration, std::allocator<PearlConfiguration>>=\"__begin_\"^{PearlConfiguration}\"__end_\"^{PearlConfiguration}\"__cap_\"^{PearlConfiguration}}"

```
