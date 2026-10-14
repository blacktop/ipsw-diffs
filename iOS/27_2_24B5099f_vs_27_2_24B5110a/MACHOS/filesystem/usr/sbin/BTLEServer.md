## BTLEServer

> `/usr/sbin/BTLEServer`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

 2701.4.0.0.0
-  __TEXT.__text: 0x7e3e8
+  __TEXT.__text: 0x7ea14
   __TEXT.__auth_stubs: 0x1100
-  __TEXT.__objc_stubs: 0xd020
-  __TEXT.__objc_methlist: 0x7ed4
-  __TEXT.__const: 0x900
-  __TEXT.__cstring: 0x369f
-  __TEXT.__objc_methname: 0x1340d
-  __TEXT.__oslogstring: 0xd9c0
+  __TEXT.__objc_stubs: 0xd0e0
+  __TEXT.__objc_methlist: 0x7f1c
+  __TEXT.__const: 0x920
+  __TEXT.__cstring: 0x36a0
+  __TEXT.__objc_methname: 0x134d2
+  __TEXT.__oslogstring: 0xd9f9
   __TEXT.__objc_classname: 0x900
   __TEXT.__objc_methtype: 0x318a
   __TEXT.__gcc_except_tab: 0x13c4
   __TEXT.__dlopen_cstrs: 0x197
   __TEXT.__ustring: 0xc6
-  __TEXT.__unwind_info: 0x26a0
+  __TEXT.__unwind_info: 0x26b8
   __DATA_CONST.__const: 0x17c0
   __DATA_CONST.__cfstring: 0x4d40
   __DATA_CONST.__objc_classlist: 0x2c8

   __DATA_CONST.__auth_got: 0x898
   __DATA_CONST.__got: 0x9b8
   __DATA_CONST.__auth_ptr: 0x20
-  __DATA.__objc_const: 0xfcc8
-  __DATA.__objc_selrefs: 0x4320
-  __DATA.__objc_ivar: 0x8a0
+  __DATA.__objc_const: 0xfd58
+  __DATA.__objc_selrefs: 0x4350
+  __DATA.__objc_ivar: 0x8ac
   __DATA.__objc_data: 0x1bd0
   __DATA.__data: 0xa50
   __DATA.__common: 0x10

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 3169
+  Functions: 3179
   Symbols:   574
-  CStrings:  5273
+  CStrings:  5286
 
CStrings:
+ "Received UARP 0x02 report, but the UARP interface is nil"
+ "T@\"NSMutableData\",R,N,V_uarpData"
+ "T@\"NSObject<OS_dispatch_group>\",R,N,V_groupUARP"
+ "T@,&,N,V_uarp"
+ "_groupUARP"
+ "_uarp"
+ "_uarpData"
+ "getUARPHIDReportDescriptor"
+ "groupUARP"
+ "handleUARPData"
+ "setUarp:"
+ "uarp"
+ "uarpData"
```
