## AppleLOM

> `/System/Library/PrivateFrameworks/AppleLOM.framework/Versions/A/AppleLOM`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__DATA.__data`

```diff

-74.0.0.0.0
-  __TEXT.__text: 0x1f688
+74.0.1.0.0
+  __TEXT.__text: 0x1f704
   __TEXT.__objc_methlist: 0xe04
   __TEXT.__const: 0xc8
   __TEXT.__gcc_except_tab: 0xb78
-  __TEXT.__oslogstring: 0x35a0
+  __TEXT.__oslogstring: 0x35b9
   __TEXT.__cstring: 0x1125
   __TEXT.__unwind_info: 0x6f8
   __TEXT.__objc_stubs: 0x0

   __DATA_CONST.__got: 0x210
   __AUTH_CONST.__const: 0x9d0
   __AUTH_CONST.__cfstring: 0x12e0
-  __AUTH_CONST.__objc_const: 0x2008
+  __AUTH_CONST.__objc_const: 0x2028
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__auth_got: 0x0
   __AUTH.__objc_data: 0x550
-  __DATA.__objc_ivar: 0x144
+  __DATA.__objc_ivar: 0x148
   __DATA.__data: 0x420
   __DATA.__bss: 0x80
   __DATA.__common: 0x4

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libpcap.A.dylib
   Functions: 626
-  Symbols:   1350
+  Symbols:   1351
   CStrings:  615
 
Symbols:
+ OBJC_IVAR_$_LOMConnection._responseSent
CStrings:
+ "%@ Response Ack timeout %d sec responseSent:%d"
+ "%@ sendResponse completion error:%@"
- "%@ Response Ack timeout %d sec"
- "%@ sendResponse completion"
```
