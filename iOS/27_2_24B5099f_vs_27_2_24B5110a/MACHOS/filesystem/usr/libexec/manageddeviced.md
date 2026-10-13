## manageddeviced

> `usr/libexec/manageddeviced`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-31.0.0.0.0
-  __TEXT.__text: 0x42778
+31.42.1.0.0
+  __TEXT.__text: 0x427a8
   __TEXT.__auth_stubs: 0xd00
-  __TEXT.__objc_stubs: 0x92e0
-  __TEXT.__objc_methlist: 0x41ec
-  __TEXT.__const: 0x118
+  __TEXT.__objc_stubs: 0x9320
+  __TEXT.__objc_methlist: 0x41fc
+  __TEXT.__const: 0x120
   __TEXT.__gcc_except_tab: 0x708
-  __TEXT.__objc_methname: 0xa4a7
+  __TEXT.__objc_methname: 0xa4f0
   __TEXT.__objc_classname: 0xdab
   __TEXT.__cstring: 0x2f9e
   __TEXT.__objc_methtype: 0xe98
   __TEXT.__oslogstring: 0x6897
   __TEXT.__dlopen_cstrs: 0x55
   __TEXT.__ustring: 0x7d0
-  __TEXT.__unwind_info: 0x18d8
+  __TEXT.__unwind_info: 0x18e0
   __DATA_CONST.__const: 0x19b0
   __DATA_CONST.__cfstring: 0x34c0
   __DATA_CONST.__objc_classlist: 0x368

   __DATA_CONST.__auth_got: 0x690
   __DATA_CONST.__got: 0x9d0
   __DATA.__objc_const: 0x8e78
-  __DATA.__objc_selrefs: 0x2a40
+  __DATA.__objc_selrefs: 0x2a50
   __DATA.__objc_ivar: 0x214
   __DATA.__objc_data: 0x2210
   __DATA.__data: 0x4e0

   - /usr/lib/libmis.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsysdiagnose.dylib
-  Functions: 1756
+  Functions: 1757
   Symbols:   541
-  CStrings:  2779
+  CStrings:  2781
 
CStrings:
+ "_handoffCurrentReplyToQueue:block:"
+ "_performOnStateQueueForWaitingCaller:"
```
