## libBasebandManagerICE.dylib

> `/usr/lib/libBasebandManagerICE.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__weak_got`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__cfstring`
- `__AUTH_CONST.__weak_auth_got`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-1580.0.0.0.0
-  __TEXT.__text: 0x2737f8
+1585.0.0.0.0
+  __TEXT.__text: 0x2737a4
   __TEXT.__init_offsets: 0x17c
-  __TEXT.__objc_methlist: 0x52c
+  __TEXT.__objc_methlist: 0x544
   __TEXT.__const: 0x13d00
   __TEXT.__dlopen_cstrs: 0x52
-  __TEXT.__gcc_except_tab: 0x39918
-  __TEXT.__oslogstring: 0xcf7d
-  __TEXT.__cstring: 0x8612
-  __TEXT.__unwind_info: 0xac60
+  __TEXT.__gcc_except_tab: 0x39924
+  __TEXT.__oslogstring: 0xcf98
+  __TEXT.__cstring: 0x8622
+  __TEXT.__unwind_info: 0xac70
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x168
-  __DATA_CONST.__objc_selrefs: 0x688
+  __DATA_CONST.__objc_selrefs: 0x690
   __DATA_CONST.__objc_superrefs: 0x28
   __DATA_CONST.__got: 0x2300
   __AUTH_CONST.__const: 0x10ec8
   __AUTH_CONST.__cfstring: 0xb40
-  __AUTH_CONST.__objc_const: 0xa68
+  __AUTH_CONST.__objc_const: 0xa98
   __AUTH_CONST.__weak_auth_got: 0x20
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH_CONST.__auth_got: 0x1b60
   __AUTH.__objc_data: 0x140
-  __DATA.__objc_ivar: 0x4c
+  __DATA.__objc_ivar: 0x50
   __DATA.__data: 0x58c
   __DATA.__bss: 0x10
   __DATA.__common: 0x49

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libprotobuf-lite.dylib
   - /usr/lib/libprotobuf.dylib
-  Functions: 6830
-  Symbols:   11949
-  CStrings:  2596
+  Functions: 6832
+  Symbols:   11951
+  CStrings:  2597
 
Symbols:
+ -[AccessoryDetection fAlreadyStarted]
+ -[AccessoryDetection setFAlreadyStarted:]
+ _OBJC_IVAR_$_AccessoryDetection._fAlreadyStarted
- _objc_msgSend$registerDelegate:
CStrings:
+ ".*ATCS_TIMEOUT.*"
+ "AppleBasebandManager-AppleBasebandServices_Manager-1585"
+ "AppleBasebandServices_Manager-1585"
+ "Re-sending %zu cached accessory(ies) to baseband on start"
- "AppleBasebandManager-AppleBasebandServices_Manager-1580"
- "AppleBasebandServices_Manager-1580"
- "Failed to get Accessory State!"
```
