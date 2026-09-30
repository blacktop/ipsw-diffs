## powerd

> `/System/Library/CoreServices/powerd.bundle/powerd`

```diff

-1846.0.7.0.0
-  __TEXT.__text: 0x6ddcc
+1846.0.15.0.0
+  __TEXT.__text: 0x6dd64
   __TEXT.__auth_stubs: 0x1ba0
-  __TEXT.__objc_stubs: 0x4ce0
+  __TEXT.__objc_stubs: 0x4d00
   __TEXT.__objc_methlist: 0x284c
-  __TEXT.__const: 0x458
-  __TEXT.__cstring: 0x6800
-  __TEXT.__objc_methname: 0x69a3
-  __TEXT.__oslogstring: 0xbec9
+  __TEXT.__const: 0x408
+  __TEXT.__cstring: 0x680c
+  __TEXT.__objc_methname: 0x69b2
+  __TEXT.__oslogstring: 0xbecb
   __TEXT.__objc_classname: 0x328
   __TEXT.__objc_methtype: 0x871
   __TEXT.__gcc_except_tab: 0x4c0
   __TEXT.__dlopen_cstrs: 0x300
   __TEXT.__ustring: 0x10
-  __TEXT.__unwind_info: 0x1340
+  __TEXT.__unwind_info: 0x1338
   __DATA_CONST.__auth_got: 0xde0
   __DATA_CONST.__got: 0x368
   __DATA_CONST.__auth_ptr: 0x30
-  __DATA_CONST.__const: 0x24e0
+  __DATA_CONST.__const: 0x2508
   __DATA_CONST.__cfstring: 0x7160
   __DATA_CONST.__objc_classlist: 0xa8
   __DATA_CONST.__objc_protolist: 0x50

   __DATA_CONST.__objc_dictobj: 0x168
   __DATA_CONST.__objc_arrayobj: 0x300
   __DATA.__objc_const: 0x4920
-  __DATA.__objc_selrefs: 0x19b0
+  __DATA.__objc_selrefs: 0x19b8
   __DATA.__objc_ivar: 0x3a8
   __DATA.__objc_data: 0x690
   __DATA.__data: 0xa2c

   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libenergytrace.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: B2535643-B13A-394A-8491-1711D4B4FD0F
-  Functions: 2332
+  UUID: 73EE747F-8D49-3104-B368-4231E3C2C2EB
+  Functions: 2331
   Symbols:   565
-  CStrings:  4656
+  CStrings:  4657
 
CStrings:
+ " System Assertion Timeout: Device became inactive more than %llu seconds ago.%@ is not on the allow list. Dropping assertion %lld:%@ for pid %d %@. age:%llu."
+ "System Assertion Timer: setting timeout value to %llu"
+ "setCountLimit:"
- " System Assertion Timeout: Device became inactive %d seconds ago.%@ is not on the allow list. Dropping assertion %lld:%@ for pid %d %@. age:%llu."
- "System Assertion Timer: setting timeout value to %u"

```
